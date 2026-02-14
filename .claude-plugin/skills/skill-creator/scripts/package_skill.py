#!/usr/bin/env python3
"""
Package a skill into a distributable .skill file.

Usage:
    python package_skill.py <path/to/skill-folder> [output-directory]

Example:
    python package_skill.py ./my-skill
    python package_skill.py ./my-skill ./dist
"""

import argparse
import os
import sys
import zipfile
import yaml
from pathlib import Path


def validate_skill(skill_path: Path) -> tuple[bool, list[str]]:
    """Validate a skill directory and return (is_valid, errors)."""

    errors = []

    # Check SKILL.md exists
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        errors.append(f"Missing required file: SKILL.md")
        return False, errors

    # Parse and validate SKILL.md
    content = skill_md.read_text()

    # Check frontmatter exists
    if not content.startswith("---"):
        errors.append("SKILL.md must start with YAML frontmatter (---)")
        return False, errors

    # Extract frontmatter
    parts = content.split("---", 2)
    if len(parts) < 3:
        errors.append("SKILL.md frontmatter not properly closed (missing closing ---)")
        return False, errors

    frontmatter_text = parts[1].strip()

    try:
        frontmatter = yaml.safe_load(frontmatter_text)
    except yaml.YAMLError as e:
        errors.append(f"Invalid YAML in frontmatter: {e}")
        return False, errors

    # Check required fields
    if not frontmatter:
        errors.append("Frontmatter is empty")
        return False, errors

    if "name" not in frontmatter:
        errors.append("Missing required field in frontmatter: name")

    if "description" not in frontmatter:
        errors.append("Missing required field in frontmatter: description")

    # Validate description quality
    description = frontmatter.get("description", "")
    if description and len(description) < 20:
        errors.append("Description is too short. Include what the skill does and when to use it.")

    if description and "TODO" in description:
        errors.append("Description contains TODO - please complete it before packaging")

    # Check for body content
    body = parts[2].strip()
    if not body:
        errors.append("SKILL.md body is empty - add instructions for using the skill")

    if "TODO" in body:
        errors.append("SKILL.md body contains TODO items - please complete them before packaging")

    # Validate directory structure
    valid_dirs = {"scripts", "references", "assets"}
    for item in skill_path.iterdir():
        if item.is_dir() and item.name not in valid_dirs and not item.name.startswith("."):
            errors.append(f"Unexpected directory: {item.name}. Valid directories are: {valid_dirs}")

    # Check for forbidden files
    forbidden_files = {"README.md", "INSTALLATION_GUIDE.md", "QUICK_REFERENCE.md", "CHANGELOG.md"}
    for item in skill_path.iterdir():
        if item.is_file() and item.name in forbidden_files:
            errors.append(f"Remove {item.name} - skills should not include auxiliary documentation")

    return len(errors) == 0, errors


def package_skill(skill_path: Path, output_dir: Path) -> Path:
    """Package a skill into a .skill file (zip archive)."""

    skill_name = skill_path.name
    output_file = output_dir / f"{skill_name}.skill"

    with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zf:
        for file_path in skill_path.rglob("*"):
            if file_path.is_file():
                # Skip hidden files and __pycache__
                if any(part.startswith(".") or part == "__pycache__" for part in file_path.parts):
                    continue

                arcname = file_path.relative_to(skill_path)
                zf.write(file_path, arcname)
                print(f"  Added: {arcname}")

    return output_file


def main():
    parser = argparse.ArgumentParser(
        description="Validate and package a skill into a distributable .skill file"
    )
    parser.add_argument(
        "skill_path",
        help="Path to the skill directory"
    )
    parser.add_argument(
        "output_dir",
        nargs="?",
        default=".",
        help="Output directory for the .skill file (default: current directory)"
    )

    args = parser.parse_args()

    skill_path = Path(args.skill_path).resolve()
    output_dir = Path(args.output_dir).resolve()

    # Check skill path exists
    if not skill_path.exists():
        print(f"Error: Skill path does not exist: {skill_path}")
        return 1

    if not skill_path.is_dir():
        print(f"Error: Skill path is not a directory: {skill_path}")
        return 1

    print(f"Validating skill: {skill_path.name}")
    print("-" * 40)

    # Validate
    is_valid, errors = validate_skill(skill_path)

    if errors:
        print("Validation errors:")
        for error in errors:
            print(f"  ❌ {error}")
        print()

    if not is_valid:
        print("Validation failed. Fix errors and try again.")
        return 1

    print("✓ Validation passed")
    print()

    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)

    # Package
    print(f"Packaging skill...")
    output_file = package_skill(skill_path, output_dir)

    print()
    print(f"✓ Skill packaged successfully: {output_file}")
    print(f"  Size: {output_file.stat().st_size:,} bytes")

    return 0


if __name__ == "__main__":
    exit(main())
