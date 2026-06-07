# Autopilot — Workspace Upgrade Weekly Loop

- **ID:** `b1088844-cd4a-4139-b467-7afcd59591e1`
- **Status:** `active`
- **Execution mode:** `create_issue`
- **Assignee:** `d9f942b9-e245-4e28-99eb-8f12fbebc2c3` (agent)
- **Last run:** 2026-06-07T06:00:03Z
- **Created:** 2026-05-26T16:38:47Z

## Description / Steps

```markdown
Workspace Upgrade Weekly Loop — recursive workspace self-improvement. Mode=create_issue. Runs every Sunday 09:00 Asia/Kuwait (GMT+3).

Run the `workspace-upgrade-report` skill against the live workspace and post a single ranked action list as a comment on the issue this autopilot creates. Auto-dispatch the top 3 actions to skill-builder, prompt-optimizer, and memory-curator. Never skip a week — a silent skip is itself a finding.

CRITICAL SAFETY RULES:
- Mode is create_issue. Do not create additional issues except the three sub-issues for top-3 dispatch in step (6).
- NEVER mention CEO in any comment — CEO is the assignee and re-mentioning would loop (Factory Pulse v3 no-mention rule).
- NEVER mention any agent in a wrap-up. Only mention agents to delegate first-touch work on a fresh sub-issue.
- NEVER touch DEV-36 (the workspace-operations dialog).
- Read each issue's metadata before pinning anything; do not log run state. Stay within the issue this autopilot creates.

STEPS:

(1) Scope the scan window. Treat `since = now - 7 days` (RFC3339, UTC). Use `--output json` on every CLI call. Continue on single-call failure (log to stdout and skip that signal).

(2) Collect the five input signals:

   (a) retry_logs (last 7 days). Walk every issue updated in the past 7 days and pull metadata. Any `retry_log` key present is a failure signature. Aggregate by skill name / agent / failure_reason.
       - `multica issue list --output json --status in_progress` and `--status blocked` and `--status in_review` (paged if needed).
       - For each issue, `multica issue metadata list <id> --output json` — keep only entries with a `retry_log` key.

   (b) Blocked issues — every issue currently `status=blocked`:
       - `multica issue list --status blocked --output json`
       - For each: capture id, identifier, title, assignee, age (now - updated_at), and `blocked_reason` metadata.

   (c) Stale in_review (>48h) — every issue currently `status=in_review` whose `updated_at` is more than 48h ago:
       - `multica issue list --status in_review --output json`
       - Filter client-side by `updated_at`.

   (d) Agent WIP imbalance — for every agent in the workspace, count `in_progress` issues assigned to them. Flag any agent with WIP=0 (cold) or WIP≥4 (overloaded). Flag any squad whose total WIP ≥7.
       - `multica agent list --output json`
       - `multica issue list --status in_progress --output json` and group by `assignee_id`.

   (e) Skill orphans — every skill not assigned to any agent (`agent_count==0`), and every agent with zero skills attached.
       - `multica skill list --output json`
       - For each skill, attempt `multica skill get <id> --output json` (or inspect the skill→agent join if exposed). If the CLI exposes no join command, infer from agent definitions (`multica agent get <id> --output json` per agent) — cap the scan at 30 agents per run.

(3) Score and rank actions. For each candidate upgrade action, score on:
   - Impact (how many issues/agents this would unblock or accelerate; 1–5)
   - Effort (1=trivial, 5=multi-day)
   - Confidence (1=speculative, 5=clear pattern with ≥3 occurrences)
   Final score = (Impact × Confidence) / Effort. Surface the Top 5.

(4) Compose the upgrade report comment. Post ONE comment on this autopilot's created issue, using this exact shape so step (6) can parse it:

```
# Workspace Upgrade Report — <YYYY-MM-DD>

**Window:** <since> → <now> (UTC)
**Signals scanned:** retry_logs=N | blocked=N | stale_in_review_48h=N | wip_outliers=N | skill_orphans=N

## Top 5 Upgrade Actions

1. **<short title>** — owner=<agent-name> | effort=<S|M|L> | impact=<1-5> | score=<n>
   - Rationale: <one sentence, cite source issue identifiers like DEV-NN>
   - Expected impact: <one sentence>

2. … (same shape)
3. … (same shape)
4. … (same shape)
5. … (same shape)

## Signal Summary
- Retry log hotspots: <skill / agent / count> …
- Stale in_review: <DEV-NN list>
- Blocked: <DEV-NN list>
- WIP outliers: <agent: count> …
- Skill orphans: <skill names>

## Next Steps
- Top 3 actions auto-dispatched to skill-builder, prompt-optimizer, memory-curator (see linked sub-issues).
- Remaining actions parked on this issue for CEO triage.
```

Post via: `multica issue comment add <this-issue-id> --content-stdin` (HEREDOC the body in). Do NOT include any `mention://agent/...` link in this comment.

(5) Pin metadata on this issue ONLY if a value is materially needed by future runs. Recommended keys: `report_window_end` (RFC3339), `top_action_count` (number, expect 5), `dispatched_action_count` (number, expect 3). Use `multica issue metadata set` once each. Skip any key whose value is identical to what you already see in `metadata list`.

(6) Auto-dispatch top 3 actions. Each top-3 action gets its own sub-issue under this autopilot's created issue, assigned to the named owner. Owner mapping rules:
   - Owner agent named in the action header (skill-builder / prompt-optimizer / memory-curator) is the assignee.
   - If the top-3 already names a different agent (e.g. action #1 is a runtime fix that belongs elsewhere), still cap dispatch at exactly three sub-issues among {skill-builder, prompt-optimizer, memory-curator}. Pick the highest-scoring action that fits each agent's domain:
       * skill-builder → new skill, skill rewrite, skill orphan adoption
       * prompt-optimizer → agent prompt edit, prompt-improvement-review target, retry_log root-cause in prompts
       * memory-curator → memory cleanup, stale-fact removal, missing-default capture
   - If no candidate fits an agent's domain this week, comment on the parent: "No skill-builder/prompt-optimizer/memory-curator action this week — backlog empty for that lane." Do NOT mint a filler sub-issue.

   For each of the three dispatch sub-issues:
   - `multica issue create --title "Workspace Upgrade Action — <short title>" --project 1a1c2fb3-41ee-4b99-b820-d10f1c564052 --parent <this-issue-id> --status todo --priority high --assignee-id <agent-id> --description-stdin` with body that includes:
     * Input (the signal that triggered this)
     * Expected Output (concrete deliverable: prompt patch / new skill / memory entry)
     * Acceptance Criteria
     * Dependencies
     * Risk
     * Definition of Done
   - The sub-issue assignment fires the agent. Do not also `@mention` the agent in the sub-issue body — assignment is the trigger.

(7) Flip this issue's status to `in_review` so the CEO Command Squad can verify (`multica issue status <this-issue-id> in_review`). Do NOT close it. Top-3 sub-issues stay `todo` for the owner agents.

(8) Output to stdout: `Workspace Upgrade @ <RFC3339> | top5=5 | dispatched=N | blocked=B stale=S wip_out=W orphans=O retry=R`. This is the only non-comment output.

Operating rules:
- Never block on a single CLI failure. Log "skipped <signal>: <reason>" and continue with the remaining signals.
- All comments go on the auto-created issue. Never comment on DEV-36 or on issues you did not create.
- Do not use `multica issue update --status done` anywhere. The owners close their own sub-issues.
- Do not create more than 3 dispatch sub-issues. Cap is hard.
- The created issue MUST land in `in_review`, never `done` — CEO verifies week-over-week trend.
```
