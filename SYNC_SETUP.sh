#!/bin/bash

echo "Claude Code Sync Plugin - Setup Script"
echo "======================================"
echo ""
echo "This script sets up your Claude Code configuration for cross-device sync."
echo ""
echo "STEP 1: Create a GitHub repository"
echo "   1. Go to https://github.com/new"
echo "   2. Create a NEW repository called 'claude-code-sync'"
echo "   3. Make it PRIVATE (important for security)"
echo "   4. DO NOT initialize with README, .gitignore, or license"
echo "   5. Copy the HTTPS clone URL"
echo ""
read -p "Press enter when you've created the repo and have the clone URL ready..."
echo ""
read -p "Paste your GitHub clone URL here: " github_url

echo ""
echo "STEP 2: Initializing git repository..."
cd ~/.claude-plugin-sync

git init
git add .
git commit -m "Initial Claude Code sync - $(date +%Y-%m-%d)"
git remote add origin "$github_url"
git branch -M main
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "✓ Successfully pushed to GitHub!"
    echo ""
    echo "STEP 3: Install the plugin locally"
    echo "   Run: claude /plugin install ~/.claude-plugin-sync"
    echo ""
    echo "STEP 4: On other devices"
    echo "   1. Clone the repo: git clone $github_url ~/.claude-plugin-sync"
    echo "   2. Install plugin: claude /plugin install ~/.claude-plugin-sync"
    echo ""
    echo "STEP 5 (Optional): Create sync shortcut"
    echo "   Copy the sync script from README.md to ~/.local/bin/claude-sync"
    echo ""
else
    echo "✗ Failed to push to GitHub. Check your URL and try again."
    exit 1
fi
