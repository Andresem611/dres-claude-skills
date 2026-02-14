---
name: thoven-financials
description: Manage Thoven burn rate tracker. Use when user wants to add expenses, log funding, check burn rate/runway, update budgets, or review financial status. Triggers "add $X [category]", "received $X from", "show burn rate", "what's my runway", "budget vs actual", "update [category] budget"
---

# Thoven Financials

Conversational interface for managing the Thoven burn rate tracker spreadsheet.

## File Location

`/Users/andresmartinez/Vaults/Executive Assistant/Thoven_Burn_Rate_Tracker.xlsx`

## Core Operations

### 1. Add Expense

**User says:** "Add $200 Meta Ads spend"

**Process:**
1. Parse amount and category from natural language
2. Run: `python scripts/tracker.py` with add_expense()
3. Respond with confirmation and updated totals

**Response format:**
```
✓ Added $200 to Meta Ads
Meta Ads spend this month: $200 / $500 budget (40%)
Cash balance: $2,900
```

**Categories:**
- Meta Ads, Google Ads, Claude Code, Metabase, Canva, Contractors, Travel, Other SaaS, Teacher Onboarding

### 2. Add Funding

**User says:** "Received $1000 from Keri's dad"

**Process:**
1. Parse amount and source
2. Run add_funding()
3. Respond with new balance and runway

**Response format:**
```
✓ Added funding: $1,000 from Keri's dad
New balance: $3,900 | Runway: 3.3 months
```

### 3. Check Status

**User says:** "What's my runway?" or "Show burn rate"

**Response format:**
```
Cash: $3,900 | Burn: $1,200/mo | Runway: 3.3 months
```

### 4. Budget vs Actual

**User says:** "Show budget vs actual"

**Response format:**
```
Budget vs Actual (MTD)

Meta Ads:      $450 / $500  (90%) ⚠️
Google Ads:    $0 / $375    (0%)
Claude Code:   $200 / $200  (100%) ⚠️
Metabase:      $100 / $100  (100%) ⚠️
Canva:         $67 / $67    (100%) ⚠️
Contractors:   $225 / $225  (100%) ⚠️
Travel:        $0 / $0      (-)
Other SaaS:    $0 / $0      (-)

Total: $1,042 / $1,467 (71%)
```

### 5. Update Budget

**User says:** "Update Meta Ads budget to $600"

**Response:** `✓ Updated Meta Ads budget: $500 → $600`

## Implementation

All operations use `scripts/tracker.py`:

```python
import sys
sys.path.append('/Users/andresmartinez/.claude/skills/thoven-financials/scripts')
from tracker import add_expense, add_funding, get_status, get_budget_status, update_budget

# Examples
result = add_expense("Meta Ads", 200, "Lead gen")
result = add_funding("Keri's dad", 1000)
status = get_status()
budget = get_budget_status()
result = update_budget("Meta Ads", 600)
```

## Natural Language Variations

**Add Expense:** "Add $X [category]", "Log $X [category]", "Spent $X on [category]"
**Add Funding:** "Received $X from [source]", "Got $X from [source]"
**Check Status:** "What's my runway?", "Show burn rate", "Current balance?"
**Budget Review:** "Show budget vs actual", "Budget status"
**Update Budget:** "Update [category] budget to $X", "Set [category] at $X"

## Error Handling

Invalid category:
```
✗ Unknown category: Office Supplies
Valid: Meta Ads, Google Ads, Claude Code, Metabase, Canva, Contractors, Travel, Other SaaS
```

## Warnings

- Budget >80%: Show ⚠️
- Over budget: "OVER BUDGET ⚠️"
- Runway <2 months: Suggest reviewing expenses or securing funding

## References

- Detailed examples: [references/examples.md](references/examples.md)
