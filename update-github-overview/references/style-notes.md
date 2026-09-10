# Style notes for drafted Featured Project entries

Pulled from the current `7kim/7kim` README so new entries don't clash with
the existing ones. Re-derive these from the live README each run instead of
trusting this file blindly — the user may restyle things over time.

- **Heading format**: `### <emoji> [<Repo Display Name>](https://github.com/<username>/<repo>)`
  — pick an emoji that loosely matches the repo's domain (🤖 for
  agents/automation, 🧩 for tooling/skills, 📚 for docs/reference, etc.),
  don't reuse an emoji already used by another entry.
- **Logo/screenshot**: centered `<p align="center">` block with an `<img>`
  pointing at `raw.githubusercontent.com/<username>/<repo>/<default-branch>/assets/logo.*`
  if that path exists; otherwise omit — don't fabricate an image path.
- **Blurb**: 1–3 sentences, plain prose, no marketing superlatives beyond
  what the repo's own description/README uses. Technical specifics (counts,
  stack, architecture terms) are good when they come from the repo itself.
- **Badge row**: `<p align="left">` with shields.io `for-the-badge`-style or
  flat badges, using colors already present elsewhere in the README
  (`#A855F7` purple, `#2563EB`/`#6366F1` blues, `#2496ED` Docker blue) rather
  than introducing new arbitrary colors.
- **Separator**: `---` between entries.
- Entries are ordered most-recently-added last (new drafts go at the bottom
  of the Featured Projects section, before the closing footer `<p>`).
