# Autopilot — Daily Command Center Digest

- **ID:** `a0af1952-8173-4b21-bf8a-05940101fa4e`
- **Status:** `active`
- **Execution mode:** `create_issue`
- **Assignee:** `d9f942b9-e245-4e28-99eb-8f12fbebc2c3` (agent)
- **Last run:** 2026-06-08T04:00:06Z
- **Created:** 2026-05-26T16:42:03Z

## Description / Steps

```markdown
Daily Command Center Digest. Mode=create_issue. Runs every day 07:00 Asia/Kuwait (GMT+3). Produces ONE per-project status briefing comment on the dated issue this autopilot creates, so the CEO + workspace owner can see — at a glance — every project's state and what to push today.

CRITICAL SAFETY RULES:
- Mode is create_issue. Do not create additional issues. Do not change status on any other issue.
- NEVER mention any agent or member in the digest comment. Owner reads the dated issue directly; mentions would loop (Factory Pulse no-mention rule).
- NEVER touch DEV-36 (workspace-operations dialog) — exclude it from every list, count, and section.
- Quiet on green days: if NOTHING actionable changed since yesterday's digest (no new blockers, no stale in_review, no new approval ask, no project lifecycle_phase change, no new app-request), do NOT post any comment. Leave the auto-created issue body empty so it can be auto-cancelled by step (8).
- Use `--output json` on every CLI call. Continue on single-call failure (log to stdout and skip that signal).

STEPS:

(1) Snapshot the workspace.
    - `multica project list --output json` → all projects.
    - `multica issue list --output json` → all issues (paged if needed).
    - For each non-cancelled issue: record id, identifier, title, status, project_id, parent_issue_id, assignee_id, assignee_type, updated_at.
    - Exclude DEV-36 (id e60d5be5-b9dd-48aa-b949-28286ea80f1b) everywhere.
    - Build agent + squad name maps once: `multica agent list --output json` and `multica squad list --output json`. Used for assignee names; never for mention links.

(2) Detect "since yesterday" deltas. Treat `since = (now - 24h)` UTC.
    - new_blockers: issues that flipped to status=blocked in the window (updated_at >= since AND status=blocked).
    - cleared_blockers: issues that left blocked in the window (status != blocked AND prior blocked_reason metadata key present — best-effort).
    - new_approval_asks: any issue whose metadata gained `waiting_on=owner` or `waiting_on=admin` in the window, or whose body/comments contain a fresh "Approval needed" line written in the window (cheap heuristic: latest comment created_at >= since and contains "approval needed" case-insensitive).
    - stale_in_review_48h: any issue status=in_review with updated_at older than 48h.
    - lifecycle_phase changes: any parent issue whose metadata `lifecycle_phase` changed (compare to value from yesterday's pin — see step 7).
    - new_app_requests: any issue created_at >= since in project `01 - App Requests` (f3089a97-c608-4599-913c-f331335e1abe).
    If ALL six lists are empty AND there is no stale in_review and no current blocked anywhere → green day. Skip to step (8) without posting.

(3) Per-project section assembly. For each project (sorted by project title prefix `00 -`, `01 -`, … and then APP projects):
    - Skip the project entirely if it has zero open issues (status in {todo, in_progress, in_review, blocked}) AND no new_app_requests AND no lifecycle change.
    - Goal: 1 sentence from project.description (truncate to ~140 chars at the first sentence boundary).
    - lifecycle_phase: read from the project's "anchor" parent issue (heuristic: the parent issue with the most children in this project; if APP project, the parent whose title starts with "APP — "). Show the value of metadata `lifecycle_phase` or "—" if unset.
    - Active issues: counts by status — `todo=N in_progress=N in_review=N blocked=N` (exclude DEV-36).
    - Blockers + waiting_on: list every issue in this project with status=blocked OR metadata `waiting_on` set. Format: `DEV-NN <title> — waiting_on=<value> | blocked_reason=<value>`. Cap 5 per project; "+N more" if truncated.
    - Next action + owner: the single highest-priority issue in this project that is `todo` or `in_progress` and not blocked. Format: `DEV-NN <title> — owner=<agent-or-squad name>` (plain name, NO mention link).
    - Risk: 1 line — pick the most material risk: stale in_review item, oldest blocker, or "WIP imbalance: <name> has N in_progress" if any agent in this project has >=4 open issues. If nothing material, write "Risk: low — no stale or overloaded items.".
    - Approval needed: yes/no. If yes, quote the exact ask (one sentence from the requesting issue's body/comment). Format: `Approval needed: yes — DEV-NN: "<exact ask>"` or `Approval needed: no`.

(4) Compose the Top-3 block. Score every open issue across the workspace by:
    - urgency: blocked=4, stale_in_review_48h=3, has approval ask=3, deploy_gate=red=4, priority=urgent=4 / high=3 / medium=2 / low=1.
    - momentum: in_progress=2, in_review=1, todo=1, backlog=0.
    - age penalty: +1 per 24h since updated_at, cap +3.
    Final score = urgency + momentum + age_penalty. Pick the top 3 distinct issues (no two from the same parent unless nothing else qualifies).

(5) Render the digest comment using this exact shape (parseable by humans and future audits):

```
# Daily Command Center Digest — <YYYY-MM-DD KW>

**Window:** <since> → <now> (UTC) | **Projects scanned:** N | **Open issues:** N | **Blocked:** N | **Stale in_review (48h):** N | **Approval asks:** N

## Per-Project Status

### <project icon> <project title>
- **Goal:** <one sentence>
- **Phase:** <lifecycle_phase>
- **Active:** todo=<n> in_progress=<n> in_review=<n> blocked=<n>
- **Blockers / waiting_on:** <list or "none">
- **Next action:** <DEV-NN title — owner=name>
- **Risk:** <one line>
- **Approval needed:** <yes/no> [— "<exact ask>"]

### <next project>
… (same shape)

## Top 3 to Push Today

1. **DEV-NN** <title> — assignee=<name> | why: <one phrase>
2. **DEV-NN** <title> — assignee=<name> | why: <one phrase>
3. **DEV-NN** <title> — assignee=<name> | why: <one phrase>

## Deltas Since Yesterday
- New blockers: <DEV-NN list or "none">
- Cleared blockers: <DEV-NN list or "none">
- New approval asks: <DEV-NN list or "none">
- Stale in_review (48h+): <DEV-NN list or "none">
- New app requests: <DEV-NN list or "none">
- Lifecycle phase changes: <project: old→new or "none">
```

Post via: `multica issue comment add <this-issue-id> --content-stdin` (HEREDOC the body). NEVER include any `mention://agent/...` or `mention://member/...` link. Issue references should be plain `DEV-NN` text (no `mention://issue/...` either — keep the digest scannable).

(6) On a green day (step 2 short-circuited), do NOT post any comment. Skip to step (8).

(7) Pin metadata on THIS issue only if a value materially helps tomorrow's run:
    - `last_run_verdict` = "green" or "posted" (overwrite each run).
    - `last_window_end` = <RFC3339-now> (overwrite each run).
    - `lifecycle_phase_snapshot` = JSON map `{project_id: phase}` so step (2) can detect phase changes tomorrow.
    - `top3_count` = number (expect 0 on green days, 3 otherwise).
    Use `multica issue metadata set` once per changed key. Skip any key whose value is identical to what `metadata list` already shows.

(8) Status finalization.
    - If a digest was posted: flip THIS issue to `in_review` (`multica issue status <this-issue-id> in_review`). CEO + owner read it, then close.
    - If green day (no digest posted): flip THIS issue to `cancelled` with no comment so it stops cluttering the inbox.

(9) Output one line to stdout (only non-comment output): `Daily Digest @ <RFC3339> | verdict=<green|posted> | projects=N | top3=N | blocked=B stale=S approvals=A`.

OPERATING RULES:
- Never block on a single CLI failure. Log "skipped <signal>: <reason>" and continue with the remaining signals.
- All comments go ONLY on the issue this autopilot creates. Never comment on any other issue.
- Never mention any agent or member anywhere. Plain names only.
- Read this issue's existing metadata before pinning. Only update keys whose values changed.
- Do not create sub-issues, do not reassign any other issue, do not change any other issue's status.
- The created issue MUST land in `in_review` (when posted) or `cancelled` (green day) — never `done` (owner closes), never left in `todo`.
```
