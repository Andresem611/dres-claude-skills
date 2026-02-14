# Claude Code Sync Plugin

Personal Claude Code configuration plugin for syncing skills, agents, and settings across devices.

## Installation

### On your main machine (where you already have your setup):

1. Initialize git repo:
```bash
cd ~/.claude-plugin-sync
git init
git add .
git commit -m "Initial Claude Code config sync"
git remote add origin https://github.com/YOUR-USERNAME/claude-code-sync.git
git branch -M main
git push -u origin main
```

2. Install the plugin locally:
```bash
claude /plugin install ~/.claude-plugin-sync
```

### On other devices (Replit, secondary machine, etc):

1. Clone the repo:
```bash
git clone https://github.com/YOUR-USERNAME/claude-code-sync.git ~/.claude-plugin-sync
```

2. Install the plugin:
```bash
claude /plugin install ~/.claude-plugin-sync
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

## Plugin Structure

```
.claude-plugin/
├── plugin.json          # Plugin manifest
├── settings.json        # Claude Code settings
├── mcp.json            # MCP server config (if needed)
├── skills/             # Your custom skills
│   ├── skill-name/
│   │   ├── instructions.md
│   │   └── [other files]
│   └── ...
└── agents/             # Your custom agents (if any)
    ├── agent-name/
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
