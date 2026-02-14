---
name: daily-work-log
description: Generate end-of-day work journal entries. Use when user says "eod", "end of day", "daily log", or requests to capture daily work. Creates a comprehensive log of tasks, meetings, decisions, and notes in Daily Work folder.
---

# Daily Work Log

Capture everything from the day into a journal-style log entry.

## Trigger Phrases

Activate this skill when user says:
- "eod" or "end of day"
- "daily log" or "daily work log"
- "log today's work"
- "what did I do today"
- "capture today"

---

## Workflow

### Step 1: Read Todos

Read `todo.md` directly to get the current task list. Do NOT trigger a Notion sync -- the Thoven Work section is manually maintained and Notion is managed separately.

### Step 2: Gather Context & Show Todos

Review the current session for:
- Tasks worked on
- Decisions made
- Blockers encountered
- Files created or modified

Then display active todos from the sync:

> "Here are your active todos:
>
> **Personal:**
> - [list personal todos from todo.md]
>
> **Thoven Work:**
> - [list high-priority Notion tasks]
>
> What did you accomplish today?"

### Step 3: Ask for Additional Context

After showing todos, ask the user:

> "Let me capture the full day:
>
> 1. **What did you complete today?** (I'll cross-reference with your todos)
> 2. **Meetings/calls today?** (names, key takeaways)
> 3. **Any decisions made?** (product, strategy, personal)
> 4. **Blockers or open items?**
> 5. **Notes or observations?** (ideas, errands, anything else)
> 6. **Top priorities for tomorrow?**"

Wait for user response before proceeding.

**Cross-reference completed work**: When user mentions completed tasks, check if they match any active todos and suggest marking them complete.

### Step 4: Mark Completed Todos

After user responds with completed work:

1. **Identify matching todos**: Cross-reference completed work with active todos
2. **Suggest completions**: "I see you completed [task]. Should I mark it as done in your todos?"
3. **Mark complete**: If user confirms, use `Skill` tool to invoke `todo-manager` with args `done: [task name]`
4. **Track for daily log**: Keep list of completed todos to add to "## Completed" section

### Step 5: Generate Entry

Create the daily log using this structure:

```markdown
# Daily Work - [Day, Month Date, Year]

## Summary
[2-3 sentence overview of the day's main focus and outcomes]

## Completed
- [Task] - [outcome/context]
- [Include completed todos from todo-manager]
- [Other completed work]

## Meetings & Calls
- [Time] [Meeting name] - [key takeaways]

## Decisions Made
- [Decision] - [reasoning/context]

## Blockers / Open Items
- [Issue] - [status/next step]

## Notes
- [Observation, idea, errand, or reminder]

## Tomorrow's Focus
- [High-priority todos from todo.md]
- [Priority 1]
- [Priority 2]
```

**Integration with Todo Manager:**
- **Completed section**: Include all todos marked complete today
- **Tomorrow's Focus**: Pull high-priority Notion tasks and personal todos from `todo.md`

### Step 4: Save Entry

Save to: `Daily Work/YYYY-MM-DD.md`

**File naming**: Use ISO date format (e.g., `2025-01-06.md`)

**If file exists**:
- Read existing content
- Append new information under appropriate sections
- Or ask user if they want to replace or merge

### Step 5: Confirm

After saving, confirm:

> "Daily log saved to `Daily Work/[date].md`. Anything to add?"

---

## Entry Quality Guidelines

### Good Entries Include:
- Specific task names, not vague descriptions
- Context for why decisions were made
- Concrete next steps for blockers
- Actionable tomorrow's priorities

### Avoid:
- Generic summaries ("worked on stuff")
- Missing context ("had a call")
- No follow-up items when blockers exist

---

## Integration Notes

- **Separate from minor_memory.md**: Daily Work is human-readable journal; minor_memory is Claude session context
- **Flag major decisions**: If a significant decision was made, note it should be added to `major_memory.md`
- **Link to related notes**: If relevant Obsidian notes exist, use `[[double brackets]]` to link

---

## Quick Reference

| Element | Format |
|---------|--------|
| File location | `Daily Work/YYYY-MM-DD.md` |
| Date format | ISO 8601 (2025-01-06) |
| Entry title | `# Daily Work - Monday, January 6, 2025` |
| Task format | `- [Task] - [outcome]` |
| Meeting format | `- [Time] [Name] - [takeaways]` |
