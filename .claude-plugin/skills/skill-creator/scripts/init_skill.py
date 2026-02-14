#!/usr/bin/env python3
"""
Initialize a new skill with the proper directory structure and templates.

Usage:
    python init_skill.py <skill-name> --path <output-directory>

Example:
    python init_skill.py pdf-editor --path ~/.claude/skills/
"""

import argparse
import os
from pathlib import Path
from datetime import datetime


def create_skill_structure(skill_name: str, output_path: str) -> None:
    """Create the skill directory structure with template files."""

    skill_dir = Path(output_path) / skill_name

    # Create directories
    directories = [
        skill_dir,
        skill_dir / "scripts",
        skill_dir / "references",
        skill_dir / "assets",
    ]

    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)
        print(f"Created: {directory}")

    # Create SKILL.md template
    skill_md_content = f'''---
name: {skill_name}
description: TODO - Describe what this skill does and when to use it. Include specific triggers.
---

# {skill_name.replace("-", " ").title()}

## Overview

TODO - Brief description of the skill's purpose.

## Instructions

TODO - Step-by-step guidance for using this skill.

## Examples

TODO - Concrete examples of using this skill.

## References

- For additional details, see [references/details.md](references/details.md)
'''

    skill_md_path = skill_dir / "SKILL.md"
    skill_md_path.write_text(skill_md_content)
    print(f"Created: {skill_md_path}")

    # Create example reference file
    reference_content = '''# Reference Details

TODO - Add detailed reference information here.

This file is loaded by Claude only when needed, keeping the main SKILL.md lean.
'''

    reference_path = skill_dir / "references" / "details.md"
    reference_path.write_text(reference_content)
    print(f"Created: {reference_path}")

    # Create example script
    script_content = '''#!/usr/bin/env python3
"""
Example script for the skill.

TODO - Replace with actual implementation.
"""

def main():
    print("Hello from the skill script!")

if __name__ == "__main__":
    main()
'''

    script_path = skill_dir / "scripts" / "example.py"
    script_path.write_text(script_content)
    os.chmod(script_path, 0o755)
    print(f"Created: {script_path}")

    # Create .gitkeep in assets (empty directory placeholder)
    gitkeep_path = skill_dir / "assets" / ".gitkeep"
    gitkeep_path.touch()
    print(f"Created: {gitkeep_path}")

    print(f"\nSkill '{skill_name}' initialized successfully at {skill_dir}")
    print("\nNext steps:")
    print("1. Edit SKILL.md frontmatter (name, description)")
    print("2. Write instructions in SKILL.md body")
    print("3. Add scripts, references, and assets as needed")
    print("4. Delete any example files you don't need")
    print("5. Package with: python package_skill.py", skill_dir)


def main():
    parser = argparse.ArgumentParser(
        description="Initialize a new skill with proper structure and templates"
    )
    parser.add_argument(
        "skill_name",
        help="Name of the skill (use kebab-case, e.g., 'pdf-editor')"
    )
    parser.add_argument(
        "--path",
        default=".",
        help="Output directory where the skill folder will be created (default: current directory)"
    )

    args = parser.parse_args()

    # Validate skill name
    if not args.skill_name.replace("-", "").replace("_", "").isalnum():
        print("Error: Skill name should only contain letters, numbers, hyphens, and underscores")
        return 1

    create_skill_structure(args.skill_name, args.path)
    return 0


if __name__ == "__main__":
    exit(main())
