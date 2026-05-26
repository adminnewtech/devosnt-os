# Autopilot — Monthly Architecture & Tool-stack Review

- **ID:** `048a7b9c-15dc-4baa-861f-d008c19b675a`
- **Status:** `active`
- **Execution mode:** `create_issue`
- **Assignee:** `77da9a0d-924e-4087-9278-59ba1182b599` (agent)
- **Last run:** 2026-05-26T16:50:51Z
- **Created:** 2026-05-26T16:47:51Z

## Description / Steps

```markdown
Monthly Architecture & Tool-stack Review — keeps ADRs current, default tech stack honest, and per-integration posture fresh. Runs on the 1st of each month at 11:00 Asia/Kuwait (GMT+3) — Multica's cron parser does not support "nth weekday of month", so day-1 was chosen over "every Sunday + self-gate" to avoid spawning 3 auto-cancelled issues per month. Mode=create_issue (project: 00 - Factory Brain, id 1a1c2fb3-41ee-4b99-b820-d10f1c564052).

CRITICAL SAFETY RULES:
- Mode is create_issue. Do NOT create additional issues except the up-to-5 architecture-action sub-issues in step (7).
- NEVER mention the CEO (d9f942b9-e245-4e28-99eb-8f12fbebc2c3) in any comment — assignment alone is the trigger.
- NEVER mention any agent in a wrap-up or thank-you. Only mention an agent on dispatch sub-issues, and only if assignment alone is insufficient.
- NEVER touch DEV-36 (the workspace-operations dialog).
- Read each issue's metadata before pinning anything; do not log run state.

REVIEW WINDOW:
- `since = first day of previous calendar month, 00:00 Asia/Kuwait` → `now`. Use RFC3339 UTC for any CLI/API filter.

INPUTS TO PULL (continue on per-source failure — log "skipped <source>: <reason>" to stdout):
- All ADRs in `00 - Factory Brain` (title prefix "ADR-" or label "adr"). `multica issue list --project 1a1c2fb3-41ee-4b99-b820-d10f1c564052 --output json`.
- All apps shipped or in-flight in the window (projects whose titles start with "APP —").
- Default stack ground-truth: scan `multica skill list --output json` plus the workspace CLAUDE.md content surfaced in your runtime brief.
- Per-runtime cost / quota notes: latest "Workspace Upgrade Weekly Loop" issue + comments for the trailing month (project 00 - Factory Brain).
- Per-integration health: upstream release notes via `gh` CLI / public RSS / vendor changelogs. Never use `curl`/`wget` against Multica.
- Open CVEs: GitHub Security Advisories (`gh api /advisories?ecosystem=...`) for Node, Go, Postgres, Next.js, Expo, plus declared SDKs.

STEPS:

(1) ADR audit
   - List every ADR-* issue (any status).
   - For each, classify: still-load-bearing | superseded (cite successor) | contradicted (cite the shipped app / decision that diverged) | stale.
   - Cross-reference each shipped app's PRD / schema / API contract to detect contradictions.
   - Output as a table.

(2) Default tech stack
   - Restate the current default stack per layer (frontend, backend, DB, auth, deploy, mobile, payments, messaging, analytics).
   - For each layer: (a) what matured in the past 30 days (releases, GA milestones), (b) any alternative now worth a re-look, (c) recommendation: hold | watch | re-evaluate.

(3) Per-runtime delta
   - Runtimes in scope: Claude Code, Codex, Opencode, Openclaw, Hermes.
   - For each: pricing / quota changes, new capabilities, deprecations, observed failure rate this month (cite any `agent-self-healing-policy` retry_log surfaced on issues).

(4) Per-integration delta
   - Integrations: Supabase, Vercel, KNet, MyFatoorah, Meta (FB/IG/WhatsApp Graph), Google (Maps/OAuth/Workspace), Expo.
   - For each: pricing changes, breaking API changes, new quotas / rate limits, deprecation notices. One bullet per integration. If nothing landed, write "no changes".

(5) Security posture
   - New CVE classes affecting our stack.
   - RLS / secret-handling gaps surfaced this month (cross-reference any `security-review-checklist` failures in `06 - QA Security Performance`).
   - One-paragraph posture summary + bulleted gaps.

(6) Top 5 architecture changes to consider
   - Derive from steps (1)–(5). Rank by impact × urgency. For each: title, rationale (1–2 lines), owner (squad / agent), effort (S/M/L), risk if skipped.
   - List fewer than 5 if fewer are warranted — do NOT invent fillers.
   - If the month is genuinely quiet, list 0 actions and post the comment marker "no changes — green".

(7) Auto-dispatch the Top 5 (or fewer) as sub-issues
   - For each action, create a sub-issue:
     - Title: "ARCH ACTION: <one-line>"
     - Parent: this autopilot's issue id
     - Project: 00 - Factory Brain (1a1c2fb3-41ee-4b99-b820-d10f1c564052)
     - Priority: high for security / CVE; medium for stack or runtime drift; low for "watch" items
     - Status: todo
     - Assignee: solution-architect (77da9a0d-924e-4087-9278-59ba1182b599) by default; database items → database-architect (89c4ed8b-e38b-48c4-9029-19fd7007a255); API contract items → api-architect (614bc86d-6ef1-4f1e-8b3c-b393b43f46d0); integration items → integration-architect (4d62192f-7508-4ed2-99f5-db8b3dabbd9c); security items → security-auditor (17759d29-f9bb-4c4c-910c-b4476723db87).
     - Description includes: rationale, evidence (links to ADR / app / CVE / release notes), Acceptance Criteria, DoD, suggested effort.
   - If the month is "green" (0 actions), skip dispatch but still complete steps (8)–(10).

(8) Post the audit report as ONE comment on this autopilot's created issue. Use this exact shape (HEREDOC via `multica issue comment add <this-issue-id> --content-stdin`):

```
# Monthly Architecture & Tool-stack Review — <YYYY-MM>

**Window:** <since> → <now> (Asia/Kuwait)
**Apps reviewed:** <N> shipped, <N> in-flight
**ADRs reviewed:** <N>

## ADR audit
| ADR | Verdict | Evidence |
| --- | --- | --- |
| ADR-XXX <title> | still-load-bearing \| superseded \| contradicted \| stale | <link> |

## Default tech stack
- Frontend: hold|watch|re-evaluate — <one-line reason>
- Backend: …
- DB: …
- Auth: …
- Deploy: …
- Mobile: …
- Payments: …
- Messaging: …
- Analytics: …

## Per-runtime
- Claude Code: <delta or "no changes">
- Codex: …
- Opencode: …
- Openclaw: …
- Hermes: …

## Per-integration
- Supabase: …
- Vercel: …
- KNet: …
- MyFatoorah: …
- Meta: …
- Google: …
- Expo: …

## Security posture
<one paragraph + bulleted gaps, or "no new CVE classes; no RLS/secret gaps surfaced this month">

## Top 5 architecture changes
1. **<title>** — owner: <agent/squad> | effort: S/M/L | risk-if-skipped: <one line>
2. …

(If the month is quiet: "no changes — green")

## Dispatched sub-issues
- DEV-NN — <ARCH ACTION title>
- …
```

Do NOT include any `mention://agent/...` link in this comment.

(9) Pin metadata on this issue ONLY when materially useful for future runs. Recommended keys:
   - `review_window_end` (RFC3339)
   - `adrs_reviewed` (number)
   - `apps_reviewed` (number)
   - `actions_dispatched` (number, 0–5)
   - `posture` (string: green | yellow | red)
   Use `multica issue metadata set` once each; skip any key whose value matches what `metadata list` already shows.

(10) Flip this issue's status to `in_review` (`multica issue status <this-issue-id> in_review`). Do NOT close it — the CEO Command Squad confirms Architecture Squad has actioned the dispatched sub-issues. Sub-issues run on their own assignees.

OUTPUT STDOUT (one line only, no extra comment):
`Monthly Arch Review @ <RFC3339> | adrs=N | apps=N | actions=N | posture=<green|yellow|red>`

OPERATING RULES:
- Never block on a single CLI / `gh` / HTTP failure. Log "skipped <source>: <reason>" and continue.
- Even an empty month gets a "no changes — green" comment — never silent.
- Cap dispatch at 5 sub-issues hard.
- Read metadata before pinning. Only update keys that changed since last review.
- All comments go on the auto-created issue or on the dispatch sub-issues this run spawned. Never comment on DEV-36 or any unrelated issue.
```
