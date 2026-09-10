# 🔄 Update GitHub Overview

Checks a GitHub user's repos and keeps their profile README (the special
`<username>/<username>` repo shown on the GitHub profile page) in sync —
refreshes the repo-count badge and drafts a Featured Project entry, in the
existing visual format, for any repo that isn't represented yet.

**Problem it solves:** profile READMEs go stale the moment you push a new
project — the repo count badge drifts and new work never makes it into the
"Featured Projects" section unless you remember to hand-write an entry for it.

**What it does:**
- Pulls the user's repo list via `gh` and compares it against what's already
  linked in the Featured Projects section of the profile README
- Refreshes the repo-count badge to the real number
- For each unfeatured repo, drafts a full entry (heading, logo/screenshot if
  one exists, a blurb built only from the repo's actual description/topics,
  and a matching badge row) — never invents details a repo doesn't have
- Opens a PR rather than pushing to `main`, so drafted copy gets a human read
  before it's live on a public profile — even on scheduled/unattended runs
- Falls back to a read-only diff preview when `gh` isn't authenticated (e.g.
  running in claude.ai chat instead of Claude Code)

**Use it by saying:** *"update my GitHub overview page"*, *"sync my README
with my repos"*, *"check if my profile README is out of date"*.

➡️ See [`SKILL.md`](./SKILL.md) for the full workflow, and
[`scripts/setup_cron.sh`](./scripts/setup_cron.sh) for wiring up a weekly
check (prints the cron/Task Scheduler line — never installs it silently).
