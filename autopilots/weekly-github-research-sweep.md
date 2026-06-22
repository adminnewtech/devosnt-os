# Autopilot — Weekly GitHub Research Sweep

- **ID:** `8393adbb-7250-4738-9a5b-b3bbf3480132`
- **Status:** `active`
- **Execution mode:** `create_issue`
- **Assignee:** `ce249709-eb0c-4a45-ad59-007e27564dc0` (agent)
- **Last run:** 2026-06-22T07:00:06Z
- **Created:** 2026-05-26T16:42:47Z

## Description / Steps

```markdown
Weekly GitHub Research Sweep — keeps the workspace's skill ecosystem fresh. Runs every Monday 10:00 Asia/Kuwait (GMT+3). Mode=create_issue (project: 09 - Research Intelligence, id e977793d-b825-448a-a3f1-bb8f59cc1266).

CRITICAL SAFETY RULES:
- Mode is create_issue. Do not create additional issues except the up-to-3 sub-issues for skill-builder dispatch in step (6).
- NEVER mention the CEO (d9f942b9-e245-4e28-99eb-8f12fbebc2c3) in any comment — assignment is the trigger.
- NEVER mention any agent in a wrap-up or thank-you. Only mention an agent on the dispatch sub-issues, and only if assignment alone is insufficient.
- NEVER touch DEV-36 (the workspace-operations dialog).
- Read each issue's metadata before pinning anything; do not log run state. Stay within the issue this autopilot creates and the dispatch sub-issues it spawns.

SOURCES MONITORED (every Monday — continue on per-source failure, log "skipped <source>: <reason>" to stdout):
- anthropics/claude-code — releases, /skills, /hooks, /subagents, /mcp directories
- anthropic-experimental/* — every public repo under that org (filter for "skill"/"agent")
- awesome-claude-code-toolkit
- awesome-claude-code-subagents
- awesome-agent-skills
- supabase/* — any repo with topic agent / skill / mcp
- hanoi-rainbow (https://github.com/hanoi-rainbow)
- MCP servers index (https://github.com/modelcontextprotocol/servers + https://mcpservers.org)

STEPS:

(1) Scope the scan window. Treat `since = now - 7 days` (RFC3339, UTC). Use `gh` CLI where possible; fall back to `curl` ONLY against public GitHub raw URLs (never against Multica). For every CLI call use `--output json`. Continue on single-call failure.

(2) Per source, collect new or changed items in the window:
   - For repos: `gh api repos/<owner>/<name>/commits?since=<since>` and `gh api repos/<owner>/<name>/releases` filtered by published_at >= since.
   - For org listings (anthropic-experimental, supabase, hanoi-rainbow): `gh api orgs/<org>/repos?type=public&sort=pushed` and keep repos pushed in the window.
   - For awesome-* lists: diff the README at HEAD vs HEAD~7days (`gh api repos/<o>/<r>/contents/README.md` then compare). New bullet = new item.
   - For MCP servers index: diff the servers list (servers.json or README) the same way.
   Deduplicate by canonical URL. Cap the candidate set at 40 items per sweep — if more, keep the 40 with most-recent activity.

(3) Classify each candidate as MCP or non-MCP. MCP candidates include: anything with `modelcontextprotocol` in the URL or topics, anything named `mcp-*` or `*-mcp`, anything that ships a Model Context Protocol server. Everything else is non-MCP (skill / subagent / template).

(4) Evaluate each candidate:
   - MCP candidates → invoke the `mcp-server-evaluator` skill (depends on DEV-54). If that skill is not yet available, fall back to the lightweight inline checklist: (a) what protocol surface it exposes, (b) does it duplicate any tool we already have, (c) install footprint (deps / runtime / auth), (d) maintenance signal (last commit, open issues, stars), (e) any obvious security smell (writes to disk, requires broad OAuth scopes, third-party API exfil).
   - Non-MCP candidates → run the lightweight inline `skill-evaluator` rubric: (a) maps cleanly to a Multica skill shape (purpose, trigger, input, steps, output, quality checklist), (b) is it already covered by an existing skill (search `multica skill list --output json` for name overlap), (c) license check (MIT/Apache/BSD = green; AGPL/copyleft/none = needs decision), (d) maintenance signal, (e) security smell.

(5) Bucket each candidate into one of four labels and write the report. Post ONE comment on this autopilot's created issue with this exact shape:

```
# Weekly GitHub Research Sweep — <YYYY-MM-DD>

**Window:** <since> → <now> (UTC)
**Sources scanned:** <N covered> / 8  (skipped: <list with reasons or "none">)
**Candidates discovered:** N (MCP=N, non-MCP=N)

## Imported (ready to PR)
1. **<name>** — <url>
   - Type: <skill|mcp-server|template|subagent>
   - One-liner: <what it does>
   - PR-ready spec: <link to gist or inline 5-line spec>
   - Security review: <green|pending #DEV-NN>

(repeat for each)

## Adapted (needs rework before import)
1. **<name>** — <url>
   - Gap: <what we'd change>
   - Effort: S | M | L

## Recreated as Multica skill (cleaner version)
1. **<name>** — proposed Multica skill: `<our-skill-name>`
   - Why recreate vs import: <reason>

## Rejected
1. **<name>** — <url>
   - Reason: <license | duplicate | unmaintained | security smell | scope mismatch>

## Top 3 imports → routed to skill-builder
- DEV-NN — <import #1>
- DEV-NN — <import #2>
- DEV-NN — <import #3>

## Next sweep window
<next-monday-10:00-Asia/Kuwait RFC3339>
```

Post via: `multica issue comment add <this-issue-id> --content-stdin` (HEREDOC the body in). Do NOT include any `mention://agent/...` link in this comment.

(6) Auto-dispatch the Top 3 imports as sub-issues. Selection rule: the 3 highest-confidence items in the "Imported" bucket (or fewer if fewer than 3 imports landed — never invent fillers). For each, create a sub-issue:

   - Title: "SKILL IMPORT: <name>"
   - Parent: this autopilot's issue id
   - Project: 09 - Research Intelligence (e977793d-b825-448a-a3f1-bb8f59cc1266)
   - Priority: high
   - Status: backlog initially (gate on security review — see below)
   - Assignee: skill-builder (5822179b-4e9e-40ea-bca2-70f4c80d2a19)
   - Description includes: source URL, license, what it does, proposed Multica skill name, PR-ready spec, Acceptance Criteria, DoD.

   SECURITY GATE — before flipping any dispatch sub-issue from `backlog → todo`, create one sibling security-review sub-issue assigned to security-auditor (17759d29-f9bb-4c4c-910c-b4476723db87) referencing the dispatch sub-issue. Title: "SECURITY REVIEW: <skill name> import". Body cites the source URL, install footprint, and required scopes from step (4). When the security-review sub-issue lands in `done` with `decision=green`, promote the dispatch sub-issue: `multica issue status <dispatch-id> todo`. If security review returns red, leave the dispatch sub-issue `backlog` and pin `blocked_reason=security_review_failed` to the dispatch sub-issue. Do NOT auto-import without the green stamp.

(7) Pin metadata on this issue ONLY when materially useful for future runs. Recommended keys:
   - `sweep_window_end` (RFC3339)
   - `candidates_total` (number)
   - `imported_count` (number)
   - `dispatched_count` (number, expect 0–3)
   - `sources_skipped` (string, comma-separated, only if non-empty)
   Use `multica issue metadata set` once each; skip any key whose value matches what `metadata list` already shows.

(8) Flip this issue's status to `in_review` so the CEO Command Squad can verify (`multica issue status <this-issue-id> in_review`). Do NOT close it — CEO verifies week-over-week trend. Dispatch sub-issues stay `backlog` until security-auditor clears them, then auto-promote per step (6).

(9) Output to stdout (one line only, no comment): `GH Sweep @ <RFC3339> | sources=<covered>/8 | candidates=N | imported=N adapted=N recreated=N rejected=N | dispatched=N`.

OPERATING RULES:
- Never block on a single CLI/`gh`/HTTP failure. Log "skipped <source>: <reason>" and continue.
- Cap each sweep at 40 candidates total; cap dispatch at 3 sub-issues hard.
- Read metadata before pinning. Only update keys that changed since last sweep.
- All comments go on the auto-created issue or on the dispatch/security sub-issues this run spawned. Never comment on DEV-36 or any other unrelated issue.
- Never assign an import sub-issue `todo` until its sibling security review is `done` + `decision=green`.
- mcp-server-evaluator dependency: DEV-54 SKILL: mcp-server-evaluator. If the skill is not yet published, use the inline MCP rubric in step (4) and add a one-line note to the report: "mcp-server-evaluator skill not yet published — used inline rubric."
```
