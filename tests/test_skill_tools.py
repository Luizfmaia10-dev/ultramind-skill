
"""Tests for ultramind-skill indexing and ranking scripts.

Run from the project folder with:
    python -m unittest discover -s tests -v

The tests use only Python's standard library and fake skills. They do not
install, modify, or execute any real user skills.
"""

import json
import math
import sys
import tempfile
import unittest
from pathlib import Path


# Find the scripts folder even when tests are started from another directory.
PROJECT_DIR = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = PROJECT_DIR / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

import index_skills  # noqa: E402
import rank_skills  # noqa: E402


class TestSkillIndex(unittest.TestCase):
    """Check that the indexer reads only necessary skill information."""

    def test_reads_header_without_skill_body(self):
        """A large skill body must not be included in the compact index."""
        with tempfile.TemporaryDirectory() as temporary_folder:
            root = Path(temporary_folder)
            skill_folder = root / "my-backend"
            skill_folder.mkdir()

            # The header is short, but the body is deliberately very large.
            content = (
                "---\n"
                "name: my-backend\n"
                "description: >\n"
                "  Backend\n"
                "  architecture help\n"
                "---\n"
                "# LARGE BODY\n"
                + "private example text\n" * 10000
            )
            (skill_folder / "SKILL.md").write_text(content, encoding="utf-8")

            result = index_skills.inventory([str(root)])

            self.assertEqual(len(result["skills"]), 1)
            self.assertEqual(
                result["skills"][0]["description"], "Backend architecture help"
            )
            self.assertNotIn("LARGE BODY", str(result))
            self.assertNotIn("private example text", str(result))

    def test_does_not_index_itself(self):
        """The orchestrator must not select itself as a helper skill."""
        with tempfile.TemporaryDirectory() as temporary_folder:
            root = Path(temporary_folder)
            skill_folder = root / "ultramind-skill"
            skill_folder.mkdir()
            (skill_folder / "SKILL.md").write_text(
                "---\nname: ultramind-skill\ndescription: Meta skill\n---\n",
                encoding="utf-8",
            )

            result = index_skills.inventory([str(root)])
            self.assertEqual(result["skills"], [])

    def test_shortens_description_but_keeps_file_path(self):
        """Short descriptions save tokens without changing the source file."""
        with tempfile.TemporaryDirectory() as temporary_folder:
            root = Path(temporary_folder)
            skill_folder = root / "large-skill"
            skill_folder.mkdir()
            skill_file = skill_folder / "SKILL.md"
            skill_file.write_text(
                "---\nname: large-skill\ndescription: " + "A" * 500 + "\n---\n",
                encoding="utf-8",
            )

            # Repeating a root must not create duplicate entries.
            result = index_skills.inventory(
                [str(root), str(root)], description_limit=32
            )

            self.assertEqual(len(result["skills"]), 1)
            entry = result["skills"][0]
            self.assertEqual(entry["description"], "A" * 32 + "...")
            self.assertTrue(entry["description_truncated"])
            self.assertEqual(entry["source"], str(skill_file))
            self.assertIn("A" * 500, skill_file.read_text(encoding="utf-8"))

    def test_reports_invalid_header(self):
        """A broken SKILL.md must cause a warning, not a false skill entry."""
        with tempfile.TemporaryDirectory() as temporary_folder:
            root = Path(temporary_folder)
            skill_folder = root / "broken-skill"
            skill_folder.mkdir()
            (skill_folder / "SKILL.md").write_text(
                "---\nname: broken-skill\ndescription: No closing marker\n",
                encoding="utf-8",
            )

            result = index_skills.inventory([str(root)])
            self.assertEqual(result["skills"], [])
            self.assertEqual(len(result["warnings"]), 1)

    def test_ignores_deeply_nested_folders(self):
        """Only the root and its direct subfolders are included in discovery."""
        with tempfile.TemporaryDirectory() as temporary_folder:
            root = Path(temporary_folder)
            nested = root / "group" / "hidden-skill"
            nested.mkdir(parents=True)
            (nested / "SKILL.md").write_text(
                "---\nname: hidden-skill\ndescription: Not a direct child\n---\n",
                encoding="utf-8",
            )

            result = index_skills.inventory([str(root)])
            self.assertEqual(result["skills"], [])


class TestSkillRanking(unittest.TestCase):
    """Check ranking, permissions, and requirement coverage."""

    def test_prefers_installed_skills_and_keeps_gaps(self):
        """Unavailable backups must not hide an uncovered requirement."""
        task = {
            "requirements": ["api", "tests", "security"],
            "candidates": [
                {"name": "installed-api", "focus": 70, "prompt_alignment": 85,
                 "covers": ["api"], "status": "installed"},
                {"name": "backup-api", "focus": 100, "prompt_alignment": 100,
                 "covers": ["api"], "status": "unverified"},
                {"name": "installed-tests", "focus": 70, "prompt_alignment": 85,
                 "covers": ["tests"], "status": "installed"},
            ],
        }

        result = rank_skills.rank_and_select(task)

        self.assertEqual(result["selected"], ["installed-api", "installed-tests"])
        self.assertEqual(result["uncovered_requirements"], ["security"])

        # Ranking is not the same as permission to use a skill.
        self.assertEqual(result["ranking"][0]["name"], "backup-api")

    def test_backup_requires_authorization(self):
        """An available backup is selected only when authorized."""
        task = {
            "requirements": ["api"],
            "candidates": [
                {"name": "backup", "focus": 95, "prompt_alignment": 95,
                 "covers": ["api"], "status": "available", "authorized": False}
            ],
        }

        denied_result = rank_skills.rank_and_select(task)
        self.assertEqual(denied_result["selected"], [])
        self.assertEqual(denied_result["uncovered_requirements"], ["api"])

        # Change only the permission so we can compare both outcomes.
        task["candidates"][0]["authorized"] = True
        allowed_result = rank_skills.rank_and_select(task)
        self.assertEqual(allowed_result["selected"], ["backup"])

    def test_installed_skills_beat_available_backup(self):
        """Two installed skills take priority over one available backup."""
        task = {
            "requirements": ["api", "tests"],
            "candidates": [
                {"name": "api-skill", "focus": 80, "prompt_alignment": 80,
                 "covers": ["api"], "status": "installed"},
                {"name": "test-skill", "focus": 80, "prompt_alignment": 80,
                 "covers": ["tests"], "status": "installed"},
                {"name": "backup-all", "focus": 100, "prompt_alignment": 100,
                 "covers": ["api", "tests"], "status": "available", "authorized": True},
            ],
        }

        result = rank_skills.rank_and_select(task)
        self.assertEqual(result["selected"], ["api-skill", "test-skill"])

    def test_denied_installed_skill_is_not_selected(self):
        """Explicit permission denial applies even to installed skills."""
        task = {
            "requirements": ["api"],
            "candidates": [
                {"name": "restricted", "focus": 100, "prompt_alignment": 100,
                 "covers": ["api"], "status": "installed", "authorized": False}
            ],
        }

        result = rank_skills.rank_and_select(task)
        self.assertEqual(result["selected"], [])
        self.assertEqual(result["uncovered_requirements"], ["api"])

    def test_chooses_smallest_skill_combination(self):
        """Two complementary skills can be better than three separate skills."""
        task = {
            "requirements": ["a", "b", "c", "d", "e", "f"],
            "candidates": [
                {"name": "wide", "focus": 100, "prompt_alignment": 100,
                 "covers": ["a", "b", "c", "d"], "status": "installed"},
                {"name": "part-one", "focus": 85, "prompt_alignment": 85,
                 "covers": ["a", "b", "e"], "status": "installed"},
                {"name": "part-two", "focus": 85, "prompt_alignment": 85,
                 "covers": ["c", "d", "f"], "status": "installed"},
                {"name": "only-e", "focus": 80, "prompt_alignment": 80,
                 "covers": ["e"], "status": "installed"},
                {"name": "only-f", "focus": 80, "prompt_alignment": 80,
                 "covers": ["f"], "status": "installed"},
            ],
        }

        result = rank_skills.rank_and_select(task)
        self.assertEqual(result["selected"], ["part-one", "part-two"])
        self.assertEqual(result["uncovered_requirements"], [])

    def test_backend_task_fixture_v1(self):
        """The existing backend example must keep its expected v1 results."""
        file_path = PROJECT_DIR / "tests" / "backend-task.json"
        task = json.loads(file_path.read_text(encoding="utf-8"))

        result = rank_skills.rank_and_select(task)
        expected = task["expected"]

        self.assertEqual(result["metric_version"], "v1")
        self.assertEqual(result["ranking"][0]["name"], expected["highest_ranked"])
        self.assertEqual(result["selected"], expected["selected"])
        self.assertEqual(result["uncovered_requirements"], expected["uncovered_requirements"])
        self.assertEqual(result["ranking"][0]["X"], 100.0)

        # Confirm that no excluded candidate was used in the final selection.
        for excluded in expected["excluded_from_selection"]:
            self.assertNotIn(excluded, result["selected"])

        # Every requirement must be covered or reported as missing.
        by_name = {skill["name"]: skill for skill in task["candidates"]}
        covered = set(result["uncovered_requirements"])
        for selected_name in result["selected"]:
            skill = by_name[selected_name]
            covered.update(skill["covers"])
        self.assertEqual(covered, set(task["requirements"]))

    def test_backend_task_fixture_v2(self):
        """The v2 example must use focus, prompt alignment, and coverage."""
        file_path = PROJECT_DIR / "tests" / "backend-task-v2.json"
        task = json.loads(file_path.read_text(encoding="utf-8"))

        result = rank_skills.rank_and_select(task)
        expected = task["expected"]
        ranking = {skill["name"]: skill for skill in result["ranking"]}

        self.assertEqual(result["metric_version"], "v2")
        self.assertEqual(result["selected"], expected["selected"])
        self.assertEqual(result["uncovered_requirements"], expected["uncovered_requirements"])

        self.assertAlmostEqual(
            ranking["spring-backend"]["coverage_score"],
            expected["coverage_for_spring_backend"],
        )
        self.assertAlmostEqual(
            ranking["spring-backend"]["X"],
            expected["metric_x_for_spring_backend"],
        )
        self.assertNotIn("unverified-all-in-one", result["selected"])

    def test_rejects_unknown_requirement(self):
        """A skill cannot claim coverage for a requirement not in the task."""
        task = {
            "requirements": ["api"],
            "candidates": [
                {"name": "incorrect", "focus": 90, "prompt_alignment": 90,
                 "covers": ["unknown"], "status": "installed"}
            ],
        }

        with self.assertRaises(ValueError):
            rank_skills.rank_and_select(task)

    def test_rejects_invalid_scores(self):
        """Scores must be ordinary numbers between 0 and 100."""
        invalid_scores = [True, math.nan, math.inf, -1, 101]

        for invalid in invalid_scores:
            with self.subTest(score=invalid):
                task = {
                    "requirements": ["api"],
                    "candidates": [
                        {"name": "example", "focus": invalid,
                         "prompt_alignment": 80, "covers": ["api"],
                         "status": "installed"}
                    ],
                }

                with self.assertRaises(ValueError):
                    rank_skills.rank_and_select(task)

    def test_rejects_unknown_metric_version(self):
        """An unknown formula version must be rejected, not guessed."""
        with self.assertRaises(ValueError):
            rank_skills.rank_and_select({"requirements": [], "metric_version": "v3"})


if __name__ == "__main__":
    unittest.main()
