#!/usr/bin/env python3
"""Rank documented skills and choose a combination that covers task requirements.

This script receives already evaluated skills as JSON. It does not read user
prompts, install or execute skills, or grant permissions.

v1 (default): X = 0.45 * focus + 0.55 * prompt_alignment
v2 (optional): X = 0.30 * focus + 0.35 * prompt_alignment + 0.35 * coverage
"""

import argparse
import json
import math
from pathlib import Path


VALID_STATUSES = {"installed", "available", "unverified", "unavailable"}
MAX_EXACT_REQUIREMENTS = 14


def checked_score(value, name, field):
    """Accept a normal numeric score from 0 to 100 only."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{name}: {field} must be a finite number from 0 to 100")
    if not math.isfinite(value) or not 0 <= value <= 100:
        raise ValueError(f"{name}: {field} must be a finite number from 0 to 100")
    return float(value)


def get_requirements(data):
    """Keep requirement IDs exactly as supplied by the user."""
    requirements = data.get("requirements", [])
    if not isinstance(requirements, list):
        raise ValueError("requirements must be a list of nonempty strings")
    if any(not isinstance(item, str) or not item.strip() for item in requirements):
        raise ValueError("requirements must be a list of nonempty strings")
    if len(set(requirements)) != len(requirements):
        raise ValueError("duplicate requirement IDs")
    return requirements


def get_candidates(data, requirements, version):
    """Check input claims and calculate Metric X for each candidate."""
    raw_candidates = data.get("candidates", [])
    if not isinstance(raw_candidates, list):
        raise ValueError("candidates must be a list")

    results = []
    seen = set()
    for skill in raw_candidates:
        if not isinstance(skill, dict):
            raise ValueError("each candidate must be an object")

        name = skill.get("name")
        if not isinstance(name, str) or not name.strip() or name in seen:
            raise ValueError("invalid or duplicate candidate name")
        seen.add(name)
        if name == "ultramind-skill":
            continue  # Never rank this orchestrator as its own helper.

        focus = checked_score(skill.get("focus"), name, "focus")
        alignment = checked_score(skill.get("prompt_alignment"), name, "prompt_alignment")
        covers = skill.get("covers", [])
        if not isinstance(covers, list) or any(not isinstance(r, str) for r in covers):
            raise ValueError(f"{name}: covers must be a list of requirement IDs")
        if not set(covers).issubset(requirements):
            raise ValueError(f"{name}: covers references an unknown requirement")

        status = skill.get("status", "unverified")
        if status not in VALID_STATUSES:
            raise ValueError(f"{name}: invalid availability status")
        authorized = skill.get("authorized", status == "installed")
        if not isinstance(authorized, bool):
            raise ValueError(f"{name}: authorized must be a boolean")

        # Coverage reflects only declared requirement IDs, never a guessed ability.
        unique_coverage = set(covers)
        coverage = 100 * len(unique_coverage) / len(requirements) if requirements else 0
        if version == "v2":
            score = 0.30 * focus + 0.35 * alignment + 0.35 * coverage
        else:
            score = 0.45 * focus + 0.55 * alignment

        candidate = {
            "name": name,
            "X": round(score, 2),
            "status": status,
            "covers": sorted(unique_coverage),
            "authorized": authorized,
        }
        if version == "v2":
            candidate["coverage_score"] = round(coverage, 2)
        results.append(candidate)

    return results


def selection_key(skills):
    """Prefer fewer skills; use higher scores and names to break ties."""
    return (
        len(skills),
        -sum(skill["X"] for skill in skills),
        tuple(sorted(skill["name"] for skill in skills)),
    )


def exact_cover(candidates, targets):
    """Find the smallest set of skills for up to 14 requirements.

    Each dictionary key is a group of already covered requirements.
    Each value is the best selection found for that group.
    """
    best = {frozenset(): []}
    targets = set(targets)

    for skill in candidates:
        skill_coverage = frozenset(skill["covers"]) & targets
        if not skill_coverage:
            continue

        # Copy existing states so a skill is never selected twice.
        for covered, selected in list(best.items()):
            new_covered = covered | skill_coverage
            if new_covered == covered:
                continue

            option = selected + [skill]
            previous = best.get(new_covered)
            if previous is None or selection_key(option) < selection_key(previous):
                best[new_covered] = option

    return best[frozenset(targets)]


def greedy_cover(candidates, targets):
    """Use a simpler, faster approximation for large tasks."""
    uncovered = set(targets)
    remaining = list(candidates)
    selected = []

    while uncovered:
        # Choose the skill that covers the most requirements still missing.
        options = [skill for skill in remaining if set(skill["covers"]) & uncovered]
        if not options:
            break
        best = min(options, key=lambda skill: (
            -len(set(skill["covers"]) & uncovered), -skill["X"], skill["name"]
        ))
        selected.append(best)
        uncovered.difference_update(best["covers"])
        remaining.remove(best)

    return selected


def select_from_tier(candidates, missing):
    """Cover what this availability tier can, leaving other gaps untouched."""
    possible = set()
    for skill in candidates:
        possible.update(set(skill["covers"]) & missing)

    if not possible:
        return []
    if len(possible) <= MAX_EXACT_REQUIREMENTS:
        return exact_cover(candidates, possible)
    return greedy_cover(candidates, possible)


def rank_and_select(data):
    """Rank candidates, prefer installed skills, and report missing coverage."""
    if not isinstance(data, dict):
        raise ValueError("input must be a JSON object")

    version = data.get("metric_version", "v1")
    if version not in {"v1", "v2"}:
        raise ValueError("metric_version must be 'v1' or 'v2'")

    requirements = get_requirements(data)
    candidates = get_candidates(data, requirements, version)
    ranking = sorted(candidates, key=lambda skill: (-skill["X"], skill["name"]))
    missing = set(requirements)
    selected_names = []

    # First use installed skills. Then use available, authorized backups.
    for status in ("installed", "available"):
        eligible = [skill for skill in candidates
                    if skill["status"] == status and skill["authorized"]]
        for skill in select_from_tier(eligible, missing):
            selected_names.append(skill["name"])
            missing.difference_update(skill["covers"])

    # Never hide requirements that the chosen skills cannot address.
    return {
        "metric_version": version,
        "ranking": ranking,
        "selected": selected_names,
        "uncovered_requirements": sorted(missing),
        "note": (
            "Selection uses exact minimum-cardinality coverage within each tier "
            "for up to 14 requirements, then a greedy fallback. Verify skill "
            "instructions, dependencies, permissions, and requirements before execution."
        ),
    }


def main():
    """Run the ranking tool from a JSON input file."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Task definition in JSON")
    parser.add_argument("--output", type=Path, help="Optional JSON output file")
    args = parser.parse_args()

    try:
        data = json.loads(args.input.read_text(encoding="utf-8"))
        result = rank_and_select(data)
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as error:
        parser.error(str(error))

    output = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(output, encoding="utf-8")
    else:
        print(output, end="")


if __name__ == "__main__":
    main()
