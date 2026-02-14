---
name: memory
description: Manage and update Claude Code memory files. Use when capturing business context, personal preferences, key decisions, session outcomes, or creating tool-specific guides. Invoked by "/memory", "update memory", or at end of sessions.
---

# Memory Management Skill

Guides you through updating memory files and creating tool-specific guides for persistent context across sessions.

## Trigger Phrases

- "/memory", "update memory", "save to memory"
- "remember this", "add to memory"
- End of session updates
- "create guide for [tool]"

## Memory Files Overview

| File | Purpose | Update When |
|------|---------|-------------|
| `business_context.md` | Company/product info | Quarterly, major pivots, funding changes |
| `personal_preferences.md` | Work style, communication | Style shifts, new tool preferences |
| `major_memory.md` | Strategic decisions, milestones | Key decisions, blockers resolved, partnerships |
| `minor_memory.md` | Session outcomes, active work | Every session end, weekly task updates |

**Location:** `Agent Knowledge/Memory/`

## Workflow

### Step 1: Identify What to Capture

Ask if unclear:

> "What should I capture?"
> 1. **Session outcome** - What we accomplished today (→ minor_memory)
> 2. **Key decision** - Strategic choice with long-term impact (→ major_memory)
> 3. **Business change** - Product/company direction shift (→ business_context)
> 4. **Preference update** - Work style or tool preference (→ personal_preferences)
> 5. **Tool guide** - First-time tool setup, URLs, structure (→ Guides folder)

### Step 2: Read Current File

Read the relevant memory file to understand current state before updating.

### Step 3: Update with Correct Format

**For minor_memory.md (session outcomes):**
```markdown
| Date | Focus | Key Outcomes |
|------|-------|--------------|
| YYYY-MM-DD | [Topic] | [2-3 key outcomes] |
```

**For major_memory.md (strategic decisions):**
```markdown
**Date**: YYYY-MM-DD
**Category**: Decision | Blocker | Milestone | Strategic Pivot
**Title**: [Brief, searchable title]
**Context**: [What led to this]
**Outcome/Resolution**: [Decision or how resolved]
**Impact**: [Long-term significance]
```

**For business_context.md:**
- Update relevant section (Problem, Solution, Priorities, etc.)
- Keep concise, factual
- Update "Last Updated" date

**For personal_preferences.md:**
- Update relevant section
- Keep bullet format
- No fluff

### Step 4: Confirm Update

Show the user what was added/changed before saving.

---

## Tool-Specific Guides

When encountering a new tool integration (Notion, Google Drive, etc.), create orientation guides.

**Location:** `Agent Knowledge/Guides/`

**Guide Template:**
```markdown
# [Tool] Guide

## Overview
What this tool is used for in this workspace.

## Key Locations
- [Page/folder name]: [URL] - [Purpose]
- [Database name]: [URL] - [Purpose]

## Common Operations
- How to [task 1]
- How to [task 2]

## Notes
- Quirks, gotchas, or special considerations
```

**Existing Guides:**
- `email-language-guide.md` - Email tone/style by audience

**Create guides for:**
- Notion (databases, page hierarchy, common operations)
- Google Drive (folder structure, shared drives)
- Other tools as encountered

---

## Quick Reference

| Scenario | File | Action |
|----------|------|--------|
| End of session | minor_memory | Add session row |
| Made strategic decision | major_memory | Add decision entry |
| Company milestone | major_memory | Add milestone entry |
| Quarterly review | business_context | Update relevant sections |
| New tool preference | personal_preferences | Update Technical Preferences |
| First time using tool | Guides/ | Create [tool]-guide.md |

---

## Session End Checklist

At end of day or significant session:
1. Update `minor_memory.md` with session outcome
2. Flag any major decisions for `major_memory.md`
3. Note if any tool guides need creation
4. Prompt user: "Anything else to capture before we wrap?"
