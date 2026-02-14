# Dres Claude Skills Plugin

Personal Claude Code plugin for syncing skills and settings across devices.

**GitHub:** https://github.com/Andresem611/dres-claude-skills

## Installation

### On your main machine:

Plugin is already set up. Just install it:
```bash
claude /plugin install ~/.claude-plugin-sync
```

Verify it loaded:
```bash
claude /plugin list
# You should see "andres-sync" in the output
```

### On other devices (Replit, secondary machine, etc):

1. Clone the repo:
```bash
git clone https://github.com/Andresem611/dres-claude-skills.git ~/.claude-plugin-sync
```

2. Install the plugin:
```bash
claude /plugin install ~/.claude-plugin-sync
```

3. Verify:
```bash
claude /plugin list
```

## Keeping in Sync

After making changes to skills or settings:

```bash
# Update the plugin directory
cp ~/.claude/settings.json ~/.claude-plugin-sync/.claude-plugin/
cp -r ~/.claude/skills/* ~/.claude-plugin-sync/.claude-plugin/skills/

# Commit and push
cd ~/.claude-plugin-sync
git add .
git commit -m "Update skills and settings - $(date +%Y-%m-%d)"
git push
```

Or use the provided sync script (see below).

## Sync Script (Optional)

Create `~/.local/bin/claude-sync`:

```bash
#!/bin/bash
cp ~/.claude/settings.json ~/.claude-plugin-sync/.claude-plugin/
cp -r ~/.claude/skills/* ~/.claude-plugin-sync/.claude-plugin/skills/
cd ~/.claude-plugin-sync
git add .
git commit -m "Auto-sync Claude Code config - $(date +%Y-%m-%d\ %H:%M:%S)" || echo "Nothing to commit"
git push
echo "✓ Claude Code sync complete"
```

Make executable: `chmod +x ~/.local/bin/claude-sync`

Then just run: `claude-sync`

## What's Included

**30+ Skills:**
- email-writing, humanizer, memory, todo-manager
- thoven-boardroom, canopy, thoven-financials, thoven-notion-workflow
- product-strategy-brainstorming, founder-first-principles-framework
- call-prep, prompt-generator, research-orchestration
- edtech-learning-science, customer-obsession-design-thinking
- market-research-vc-intelligence, technical-spec-generator
- testing-runbook-generator, skill-creator, subagent-creator
- notion-workspace-executor, mama-frontend, remotion
- And more...

**Settings:**
- Plugin preferences and configuration
- Enabled MCP servers (GitHub, Notion, Sentry, etc.)

## Plugin Structure

```
.claude-plugin/
├── plugin.json          # Plugin manifest
├── settings.json        # Claude Code settings
└── skills/              # 30+ custom skills
    ├── email-writing/
    ├── thoven-boardroom/
    ├── memory/
    └── ...
```

## Troubleshooting

**Plugin not loading on Replit?**
- Make sure you've run `claude /plugin install ~/.claude-plugin-sync`
- Check that paths are correct: `pwd` should show `/home/user` or similar
- Restart the Claude Code session

**Merge conflicts when syncing?**
```bash
cd ~/.claude-plugin-sync
git pull --rebase origin main
# Resolve conflicts in skills/ or settings.json
git add .
git rebase --continue
```

**Skills still not available?**
- Reload Claude Code: `claude clear` then restart
- Verify plugin is enabled: `claude /plugin list`
