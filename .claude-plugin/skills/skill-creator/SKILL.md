---
name: skill-creator
description: Guide for creating effective skills. Use when users want to create a new skill (or update an existing skill) that extends Claude's capabilities with specialized knowledge, workflows, or tool integrations.
---

# Skill Creator

This skill provides guidance for creating effective skills.

## About Skills

Skills are modular, self-contained packages that extend Claude's capabilities by providing specialized knowledge, workflows, and tools. Think of them as "onboarding guides" for specific domains or tasks—they transform Claude from a general-purpose agent into a specialized agent equipped with procedural knowledge that no model can fully possess.

## What Skills Provide

- **Specialized workflows** - Multi-step procedures for specific domains
- **Tool integrations** - Instructions for working with specific file formats or APIs
- **Domain expertise** - Company-specific knowledge, schemas, business logic
- **Bundled resources** - Scripts, references, and assets for complex and repetitive tasks

## Core Principles

### Concise is Key

The context window is a public good. Skills share the context window with everything else Claude needs: system prompt, conversation history, other Skills' metadata, and the actual user request.

**Default assumption**: Claude is already very smart. Only add context Claude doesn't already have. Challenge each piece of information: "Does Claude really need this explanation?" and "Does this paragraph justify its token cost?"

Prefer concise examples over verbose explanations.

### Set Appropriate Degrees of Freedom

Match the level of specificity to the task's fragility and variability:

- **High freedom** (text-based instructions): Use when multiple approaches are valid, decisions depend on context, or heuristics guide the approach.
- **Medium freedom** (pseudocode or scripts with parameters): Use when a preferred pattern exists, some variation is acceptable, or configuration affects behavior.
- **Low freedom** (specific scripts, few parameters): Use when operations are fragile and error-prone, consistency is critical, or a specific sequence must be followed.

Think of Claude as exploring a path: a narrow bridge with cliffs needs specific guardrails (low freedom), while an open field allows many routes (high freedom).

## Anatomy of a Skill

Every skill consists of a required SKILL.md file and optional bundled resources:

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter metadata (required)
│   │   ├── name: (required)
│   │   └── description: (required)
│   └── Markdown instructions (required)
└── Bundled Resources (optional)
    ├── scripts/          - Executable code (Python/Bash/etc.)
    ├── references/       - Documentation loaded into context as needed
    └── assets/           - Files used in output (templates, icons, fonts, etc.)
```

### SKILL.md (required)

Every SKILL.md consists of:

- **Frontmatter (YAML)**: Contains `name` and `description` fields. These are the only fields that Claude reads to determine when the skill gets used.
- **Body (Markdown)**: Instructions and guidance for using the skill. Only loaded AFTER the skill triggers.

### Bundled Resources (optional)

**Scripts** (`scripts/`): Executable code for tasks requiring deterministic reliability or repeatedly rewritten code.

**References** (`references/`): Documentation loaded as needed into context. Keeps SKILL.md lean.

**Assets** (`assets/`): Files not loaded into context, but used within the output Claude produces (templates, images, etc.).

## What NOT to Include in a Skill

Do NOT create extraneous documentation or auxiliary files:
- README.md
- INSTALLATION_GUIDE.md
- QUICK_REFERENCE.md
- CHANGELOG.md

The skill should only contain information needed for an AI agent to do the job.

## Progressive Disclosure Design Principle

Skills use a three-level loading system to manage context efficiently:

1. **Metadata** (name + description) - Always in context (~100 words)
2. **SKILL.md body** - When skill triggers (<5k words)
3. **Bundled resources** - As needed by Claude

Keep SKILL.md body to the essentials and under 500 lines. Split content into separate files when approaching this limit.

## Skill Creation Process

### Step 1: Understand the Skill with Concrete Examples

Ask questions like:
- "What functionality should the skill support?"
- "Can you give examples of how this skill would be used?"
- "What would a user say that should trigger this skill?"

### Step 2: Plan the Reusable Skill Contents

Analyze each example to identify:
- What scripts would be helpful
- What references would be needed
- What assets should be included

### Step 3: Initialize the Skill

Run the init script to create the skill structure:

```bash
python ~/.claude/skills/skill-creator/scripts/init_skill.py <skill-name> --path <output-directory>
```

### Step 4: Edit the Skill

Implement resources and write SKILL.md. Remember:
- Start with reusable resources (scripts, references, assets)
- Test any scripts by running them
- Delete example files not needed

**SKILL.md Frontmatter**:
- `name`: The skill name
- `description`: Primary triggering mechanism. Include both what the Skill does and when to use it.

### Step 5: Package the Skill

```bash
python ~/.claude/skills/skill-creator/scripts/package_skill.py <path/to/skill-folder>
```

The script validates and packages the skill into a distributable `.skill` file.

### Step 6: Iterate

Test the skill on real tasks and refine based on struggles or inefficiencies.

## Design Patterns

For multi-step processes, see [references/workflows.md](references/workflows.md).

For output formats and quality standards, see [references/output-patterns.md](references/output-patterns.md).
