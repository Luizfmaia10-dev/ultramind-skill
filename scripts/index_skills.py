#!/usr/bin/env python3
"""Create a small index of skills without reading their full instructions.

Only the YAML-style header of each SKILL.md is read. This script never
executes skills, follows URLs, or reads their supporting files.
Requires Python 3.9+; no third-party packages are needed.
"""

import argparse
import json
import re
from pathlib import Path


SKILL_FILE = "SKILL.md"
MAX_HEADER_SIZE = 32_768  # Stop reading if a skill has an unusually large header.
DEFAULT_DESCRIPTION_LIMIT = 400
VALID_NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
ALLOWED_FIELDS = {"name", "description", "compatibility"}
MULTILINE_MARKERS = {">", ">-", ">+", "|", "|-", "|+"}


def read_header(path):
    """Read only the frontmatter, stopping at the second '---' line."""
    fields = {}
    multiline_field = None
    characters_read = 0

    with path.open(encoding="utf-8-sig") as file:
        while True:
            # Limit each read so the skill body cannot be accidentally loaded.
            remaining = MAX_HEADER_SIZE - characters_read
            if remaining <= 0:
                raise ValueError("frontmatter exceeds size limit")
            line = file.readline(remaining + 1)
            if not line:
                raise ValueError("missing closing frontmatter delimiter")
            characters_read += len(line)
            if characters_read > MAX_HEADER_SIZE:
                raise ValueError("frontmatter exceeds size limit")

            # The first line must start the header; the next delimiter ends it.
            if characters_read == len(line):
                if line.strip() != "---":
                    raise ValueError("missing opening frontmatter delimiter")
                continue
            if line.strip() == "---":
                return fields

            # Indented lines belong to a multiline description or compatibility.
            if line[:1].isspace():
                if multiline_field and line.strip():
                    fields[multiline_field] += " " + line.strip()
                continue

            multiline_field = None
            if ":" not in line:
                continue
            key, value = line.split(":", 1)
            if key not in ALLOWED_FIELDS:
                continue

            value = value.strip()
            if value in MULTILINE_MARKERS:
                fields[key] = ""
                multiline_field = key
            else:
                fields[key] = value.strip("\"'")


def metadata(path, description_limit=DEFAULT_DESCRIPTION_LIMIT):
    """Validate a skill header and return its compact index entry."""
    if description_limit < 1:
        raise ValueError("description_limit must be positive")

    fields = read_header(path)
    name = fields.get("name", "")
    description = fields.get("description", "").strip()

    if not VALID_NAME.fullmatch(name):
        raise ValueError("invalid skill name")
    if not description:
        raise ValueError("missing skill description")

    # Shorten only the index entry. The original SKILL.md stays unchanged.
    truncated = len(description) > description_limit
    short_description = description[:description_limit].rstrip()
    if truncated:
        short_description += "..."

    return {
        "name": name,
        "description": short_description,
        "compatibility": fields.get("compatibility", ""),
        "status": "installed",
        "source": str(path),
        "description_truncated": truncated,
    }


def skill_files(root):
    """Find a SKILL.md in the root or its immediate subfolders."""
    direct_file = root / SKILL_FILE
    if direct_file.is_file() and not direct_file.is_symlink():
        yield direct_file

    # Do not scan recursively or follow symlinked folders.
    for folder in sorted(root.iterdir()):
        if folder.is_dir() and not folder.is_symlink():
            path = folder / SKILL_FILE
            if path.is_file() and not path.is_symlink():
                yield path


def inventory(roots, description_limit=DEFAULT_DESCRIPTION_LIMIT):
    """Index each authorized skills root once, reporting invalid entries."""
    skills = []
    warnings = []
    seen_roots = set()
    seen_names = set()

    for root_name in roots:
        root = Path(root_name).expanduser().resolve()
        if root in seen_roots:
            continue
        seen_roots.add(root)

        if not root.is_dir():
            warnings.append(f"Skill root is missing or not a directory: {root}")
            continue

        try:
            # Load only short metadata; never inspect the rest of a skill here.
            for path in skill_files(root):
                try:
                    skill = metadata(path, description_limit)
                except (OSError, UnicodeError, ValueError) as error:
                    warnings.append(f"{path}: {error}")
                    continue

                # Prevent the orchestrator from selecting itself.
                if skill["name"] == "ultramind-skill":
                    continue
                if skill["name"] in seen_names:
                    warnings.append(f"Duplicate skill name ignored: {skill['name']} ({path})")
                    continue

                seen_names.add(skill["name"])
                skills.append(skill)
        except OSError as error:
            warnings.append(f"Cannot list root {root}: {error}")

    return {"skills": skills, "warnings": warnings, "summary_only": True}


def main():
    """Allow users to build an index from the command line."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", action="append", required=True,
                        help="Authorized skills root; repeat for multiple roots")
    parser.add_argument("--output", type=Path,
                        help="Optional JSON output file (default: stdout)")
    parser.add_argument("--description-limit", type=int, default=DEFAULT_DESCRIPTION_LIMIT,
                        help="Maximum description length (default: 400)")
    args = parser.parse_args()

    if args.description_limit < 1:
        parser.error("--description-limit must be positive")

    result = inventory(args.root, args.description_limit)
    output = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(output, encoding="utf-8")
    else:
        print(output, end="")


if __name__ == "__main__":
    main()
