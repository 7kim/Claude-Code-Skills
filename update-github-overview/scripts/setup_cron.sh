#!/usr/bin/env bash
# Prints the scheduler command to add for a weekly overview sync.
# This script only PRINTS instructions — it never edits crontab or
# Task Scheduler itself. The user reviews and adds it themselves.

set -euo pipefail

SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PROMPT="Run the update-github-overview skill for 7kim/7kim."

echo "== macOS / Linux (cron) =="
echo "Run 'crontab -e' and add this line (Mondays at 9am):"
echo ""
echo "0 9 * * 1 cd $SKILL_DIR && /usr/local/bin/claude -p \"$PROMPT\" >> /tmp/update-github-overview.log 2>&1"
echo ""
echo "== Windows (Task Scheduler) =="
echo "In an elevated PowerShell, review and run:"
echo ""
cat <<'EOF'
schtasks /create /tn "UpdateGitHubOverview" /tr "claude -p \"Run the update-github-overview skill for 7kim/7kim.\"" /sc weekly /d MON /st 09:00
EOF
echo ""
echo "Notes:"
echo "- Requires 'claude' (Claude Code CLI) on PATH and 'gh auth login' already done for the account that owns the cron/task."
echo "- Each run opens a PR — it does not auto-merge. Check github.com/7kim/7kim/pulls periodically."
echo "- Log output goes to /tmp/update-github-overview.log on macOS/Linux; check Task Scheduler's history tab on Windows."
