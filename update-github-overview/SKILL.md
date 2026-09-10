---
name: update-github-overview
description: Checks a GitHub user's repos and syncs their profile README (the special same-name-as-username repo shown on their GitHub profile page) — updates the repo-count badge and drafts Featured Project entries for repos that aren't covered yet. Use this whenever the user asks to "update my GitHub overview/profile page", "sync my README with my repos", "check if my profile README is out of date", or asks for a recurring/weekly GitHub profile refresh. Works in Claude Code (can open a PR) and in claude.ai chat (read-only preview of the diff).
---

# Update GitHub Overview

Keeps a GitHub profile README (`github.com/<username>/<username>`) in sync with
the user's actual repos: refreshes the repo-count badge and drafts a Featured
Projects entry for any repo that isn't represented yet, in the same visual
format as the existing entries. It never invents facts about a repo — every
drafted blurb is built only from data pulled from GitHub (description, README,
topics, primary language).

Config for this skill (edit if the user's setup differs):
- **username**: `7kim`
- **overview repo**: `7kim/7kim`
- **branch**: `main`

If the user asks to point this at a different username/repo, update those
three values — everything else below is generic.

## Before anything else: check the environment

Run:

```bash
gh auth status
```

- **Authenticated** → full workflow below, can open a PR (Claude Code / any
  environment with a real shell and persisted `gh` auth).
- **Not authenticated / `gh` not installed / running in claude.ai chat** →
  fall back to the **read-only mode** in Step 5. Tell the user up front which
  mode you're in — don't silently degrade.

If `gh auth status` fails, do not ask the user to paste a token into the
chat. Tokens typed into a chat message aren't a durable or safe way to
authenticate a recurring skill — point them to `gh auth login` (Claude Code)
instead, and offer read-only mode for this session in the meantime.

## Step 1: Pull the current repo list

```bash
gh repo list <username> --limit 200 --json name,description,url,updatedAt,pushedAt,primaryLanguage,isFork,isArchived
```

Filter out `isFork: true` and `isArchived: true` unless the user says
otherwise — forks and archived repos aren't normally "yours" to feature.

## Step 2: Pull the current README

```bash
gh api repos/<username>/<username>/contents/README.md --jq '.content' | base64 -d > /tmp/current-readme.md
```

Read it. Two things to extract:
1. The repo-count badge — look for a shields.io badge with `repos-<N>` in the
   URL (e.g. `img.shields.io/badge/repos-3-2563EB`). If the format differs,
   search for any badge whose label is "repos".
2. The Featured Projects section — every `github.com/<username>/<repo-name>`
   link inside it. Build a set of repo names already featured.

## Step 3: Diff

- `repo_count` = count from Step 1 (post-filter) vs the badge number in Step 2.
- `unfeatured` = repos from Step 1 whose name isn't in the featured set from
  Step 2.

If both are already in sync, tell the user the overview is up to date and
stop — don't open an empty PR or rewrite the file for no reason.

## Step 4: Draft entries for unfeatured repos

For each repo in `unfeatured`:

```bash
gh repo view <username>/<repo> --json description,repositoryTopics,primaryLanguage
```

Also check for an `assets/logo.*` or a screenshot the existing entries
reference:

```bash
gh api repos/<username>/<repo>/contents/assets --jq '.[].name' 2>/dev/null
```

Build one entry matching the **exact block structure** of the existing
Featured Projects entries in the current README (heading with emoji + repo
link, optional centered logo/screenshot, a 1–3 sentence blurb, a row of
shields.io badges). Base the blurb only on the repo's actual description,
topics, and README — if the repo has no description and no README worth
summarizing, say so instead of inventing one, and list it as "needs a
description before I can draft this" rather than guessing.

Match the tone of the existing entries (see `references/style-notes.md` for
what to preserve — badge color palette, heading emoji conventions, etc.)
rather than introducing a new format.

## Step 5: Apply — two modes

### A. Full mode (gh authenticated)

1. Create a branch: `git checkout -b sync-overview-<date>`
2. Update the repo-count badge in place.
3. Insert the new Featured Project block(s) at the end of the Featured
   Projects section, preserving everything else byte-for-byte.
4. Commit, push, and open a PR:
   ```bash
   gh pr create --repo <username>/<username> --title "Sync overview: <N> new repo(s) drafted" \
     --body "Auto-drafted by update-github-overview. Review each new entry before merging — descriptions are generated from repo metadata and may need a human pass."
   ```
5. Report the PR URL to the user. **Do not merge it yourself** — merging is
   the user's approval step.

### B. Read-only mode (no gh auth — e.g. claude.ai chat)

1. Don't write or commit anything.
2. Show the user:
   - Current badge count vs actual count
   - The list of unfeatured repos
   - The drafted entry text for each (as a code block, so it's easy to copy)
3. Tell them to run this in Claude Code (or paste the diff themselves) to
   actually publish it.

## Recurring / scheduled use

Claude Code has no built-in scheduler, so "weekly" means an OS-level cron job
that invokes Claude Code headlessly. See `scripts/setup_cron.sh` — it prints
(does not silently install) the correct `crontab` line for macOS/Linux, and
the `schtasks` equivalent for Windows, for the user to review and add
themselves. Never install a cron job without the user explicitly running that
step — a skill silently scheduling itself is a bad surprise.

Each scheduled run should still open a PR, never auto-merge — the point of
the PR gate is that drafted blurbs get a human read before going live on a
public profile, and that shouldn't be skipped just because the run was
unattended.

## Things this skill should never do

- Never push directly to `main` / commit without a PR, even if asked to "just
  do it" — the profile README is public-facing and drafted copy needs review.
- Never touch the GitHub-stats images (readme-stats, top-langs, streak) —
  those already self-update via the image service and aren't part of this
  skill's job.
- Never fabricate stars, download counts, or project outcomes not present in
  the repo's actual metadata/README.
