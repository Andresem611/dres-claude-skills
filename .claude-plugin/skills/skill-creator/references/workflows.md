# Workflow Design Patterns

Reference for designing multi-step processes in skills.

## Sequential Workflows

For tasks that must be completed in order:

```markdown
## Workflow

1. **Gather inputs**
   - Collect required information
   - Validate inputs

2. **Process**
   - Perform the main operation
   - Handle edge cases

3. **Output**
   - Format results
   - Save or display
```

## Conditional Workflows

For tasks with branching logic:

```markdown
## Decision Tree

1. **Analyze the situation**
   - If condition A → Step 2A
   - If condition B → Step 2B
   - Otherwise → Step 2C

2A. **Handle case A**
    [specific instructions]

2B. **Handle case B**
    [specific instructions]
```

## Iterative Workflows

For tasks requiring refinement:

```markdown
## Iterative Process

1. **Initial attempt**
   - Create first version

2. **Review and validate**
   - Check against requirements
   - Identify gaps

3. **Refine**
   - Address gaps
   - Repeat 2-3 until satisfactory
```

## Error Handling

```markdown
## Error Handling

**If [error] occurs:**
1. Log context
2. Attempt recovery: [steps]
3. If fails: [fallback]

**Common issues:**
- Issue 1 → Solution
- Issue 2 → Solution
```

## Validation Checkpoints

```markdown
## Checkpoint

After Step X, verify:
- [ ] Condition 1 met
- [ ] Condition 2 met
- [ ] No errors

If any fails, return to Step Y.
```

## Best Practices

1. Keep steps atomic - one thing per step
2. Include decision criteria for branches
3. Provide escape hatches for failures
4. Use checklists for validation
5. Link to details for complex steps
