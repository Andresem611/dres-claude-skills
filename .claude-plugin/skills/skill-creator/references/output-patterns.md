# Output Design Patterns

Reference for output formats and quality standards in skills.

## Template Patterns

### File Generation

```markdown
## Output: [Filename]

Generate with this structure:

```[language]
[template with {{PLACEHOLDERS}}]
```

**Placeholders:**
- `{{NAME}}`: Description
- `{{DATE}}`: YYYY-MM-DD format
```

### Report Structure

```markdown
# [Title]

## Summary
- Key finding 1
- Key finding 2

## Details
[Content sections]

## Recommendations
1. Recommendation 1
2. Recommendation 2
```

## Quality Checklists

### Code Output

```markdown
Before returning code:
- [ ] Handles edge cases
- [ ] Includes error handling
- [ ] Has appropriate comments
- [ ] Follows project conventions
```

### Document Output

```markdown
Before returning document:
- [ ] Clear structure
- [ ] Complete information
- [ ] No placeholders remaining
- [ ] Appropriate length
```

## Format Standards

### Markdown
- ATX headers (# not underlines)
- One blank line before headers
- Code blocks with language specified

### JSON
- Pretty-printed, 2-space indent
- Consistent key casing
- Dates in ISO 8601

### Code
- Follow language conventions
- Include type hints where applicable
- Handle errors gracefully

## Response Patterns

### Structured Response

```markdown
## Answer
[Direct answer]

## Explanation
[Context and reasoning]

## Next Steps
[Suggested actions]
```

### Step-by-Step

```markdown
1. **[Step name]**
   ```[language]
   [code]
   ```
   [Explanation]

2. **[Step name]**
   ...
```

### Comparison

```markdown
| Option | Pros | Cons | Best For |
|--------|------|------|----------|
| A      | ...  | ...  | ...      |
| B      | ...  | ...  | ...      |

## Recommendation
[Which option and why]
```
