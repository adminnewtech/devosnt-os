# Autopilot — Weekly Benchmark Sweep

- **ID:** `5c4d2248-77af-47f6-bb1c-54578b8b0952`
- **Status:** `active`
- **Execution mode:** `create_issue`
- **Assignee:** `606dde5b-1e4b-481a-8cf4-0f6aa0dd37c7` (agent)
- **Last run:** 2026-06-29T06:00:02Z
- **Created:** 2026-05-26T16:47:40Z

## Description / Steps

```markdown
Weekly Benchmark Sweep — refresh the six-vendor competitive brief every Monday and route the top action into the Skill Factory. Mode=create_issue. Runs every Monday 09:00 Asia/Kuwait (GMT+3). Project: 09 - Research Intelligence (e977793d-b825-448a-a3f1-bb8f59cc1266). Source skill: `benchmark-vendor-tracker` (DEV-50). Seed data: DEV-62 (first six-vendor sweep).

CRITICAL SAFETY RULES:
- Mode is create_issue. Do not create additional issues except the up-to-3 sub-issues for Skill Factory dispatch in step (6).
- NEVER mention the CEO (d9f942b9-e245-4e28-99eb-8f12fbebc2c3) in any comment — assignment is the trigger.
- NEVER mention any agent in a wrap-up or thank-you. Only mention an agent on a fresh dispatch sub-issue, and only if assignment alone is insufficient.
- NEVER touch DEV-36 (the workspace-operations dialog) or any unrelated issue.
- Read each issue's metadata before pinning anything; do not log run state. Stay within the issue this autopilot creates and the dispatch sub-issues it spawns.
- All comments go ONLY on the issue this autopilot creates and the dispatch sub-issues spawned this run. Never comment on DEV-36, DEV-50, DEV-60, or any other issue.
- Use `--output json` on every Multica CLI call. Continue on single-call failure (log "skipped <vendor|step>: <reason>" to stdout and proceed).
- Never use curl/wget against Multica resources — only against vendor public sites/docs.

VENDORS COVERED EVERY WEEK (six, in this order):
1. Lovable           — https://lovable.dev
2. Bolt.new          — https://bolt.new
3. Cursor (agent)    — https://www.cursor.com
4. Replit Agent      — https://replit.com/agent
5. Antigravity 2.0   — https://antigravity.dev (or current official URL)
6. Atoms.dev         — https://atoms.dev

STEPS:

(1) Scope. Treat `since = now - 7 days` (RFC3339, UTC) as the diff window. Locate the prior sweep's report comment for diffing: list this project's issues created by this autopilot in the past 14 days (title starts with "Weekly Benchmark Sweep —"); pick the most recent one whose status is `done` or `in_review` and that is NOT the issue this autopilot just created. If no prior sweep is found, fall back to DEV-62 (RESEARCH: Six-vendor benchmark sweep, id c289d731-eaf9-4747-814f-c122f1ed08cd) as the baseline. If neither is available, mark the diff section "No baseline — first sweep" and proceed.

(2) Per vendor (all six, in order), invoke the `benchmark-vendor-tracker` skill to produce a fresh one-page brief. The skill's required output shape (per DEV-50) is: vendor name, run date, 3-sentence description, onboarding flow note, pricing as of run date, 3 strengths (with source links), 3 weaknesses, patterns to copy (named), patterns to beat (named, with our differentiated approach), decision verdict (import / adapt / recreate / study only / reject). If the `benchmark-vendor-tracker` skill is not yet published, use this inline fallback rubric and add a one-line note to the final report: "benchmark-vendor-tracker skill not yet published — used inline rubric." Capture every claim with a source URL — landing page, pricing page, changelog, release notes, blog post, or YouTube demo. No hand-wavy claims.

   Source-of-truth checklist per vendor (best effort; skip any that 404 or block):
   - Landing page (current copy + above-the-fold positioning)
   - Pricing page (capture tier names, prices, and any "new in <date>" badges)
   - Changelog / release notes / "What's new" page
   - Public blog or product update feed (last 30 days)
   - YouTube / X / public demo for any flow change announced in the window
   Continue on per-source failure. Cap vendor research at ~10 minutes wall time each.

(3) Diff vs last week. For each vendor, compare this week's brief to the baseline brief (from step 1). Material diff categories:
   - new_features (named, with source link)
   - pricing_changes (tier added/removed, price up/down, free-tier change)
   - new_flows (onboarding, agent UX, deployment surface, integration surface)
   - removed_or_deprecated (anything quietly dropped)
   - positioning_shift (the headline copy changed in a way that signals strategy)
   If a vendor genuinely shipped nothing material, write "No material change since <baseline date>." Do NOT pad — empty diffs are signal, not failure.

(4) Score the cross-vendor pattern set. Aggregate every "pattern to copy" across the six briefs and rank by:
   - frequency (how many of the six vendors do this)
   - impact (1–5: how much would importing this move our win rate vs Lovable/Bolt/Cursor)
   - effort (S | M | L)
   - readiness (do we already have an adjacent skill we can extend, or is this net-new)
   Final score = (frequency × impact) / effort. Pick the Top 3 "actions to consider."

(5) Compose the sweep report. Post ONE comment on this autopilot's created issue with this exact shape (parseable for the next sweep's diff step):

```
# Weekly Benchmark Sweep — <YYYY-MM-DD>

**Window:** <since> → <now> (UTC)
**Baseline brief:** DEV-NN (<date>) | **Vendors covered:** 6/6 (skipped: <list with reasons or "none">)

## Per-Vendor Brief

### 1. Lovable
- **One-liner:** <3 sentences>
- **Pricing (this week):** <tier names + prices>
- **Strengths:** <3 with source links>
- **Weaknesses:** <3>
- **Patterns to copy:** <named items, each with implementation note>
- **Patterns to beat:** <named items, each with our differentiated approach>
- **Verdict:** <import | adapt | recreate | study only | reject> — <one-line reason>
- **Sources:** <link>, <link>, <link>
- **Diff vs <baseline date>:** new_features=<list or "—"> | pricing_changes=<list or "—"> | new_flows=<list or "—"> | removed=<list or "—"> | positioning=<note or "—">

### 2. Bolt.new
… (same shape)

### 3. Cursor (agent mode)
… (same shape)

### 4. Replit Agent
… (same shape)

### 5. Antigravity 2.0
… (same shape)

### 6. Atoms.dev
… (same shape)

## Top 3 Actions to Consider
1. **<short action title>** — frequency=<n>/6 | impact=<1-5> | effort=<S|M|L> | score=<n>
   - Rationale: <one sentence, cite the vendors>
   - Proposed Multica artifact: <skill name | template | prompt patch>
2. **<short action title>** — frequency=<n>/6 | impact=<1-5> | effort=<S|M|L> | score=<n>
   - Rationale: <one sentence>
   - Proposed Multica artifact: <…>
3. **<short action title>** — frequency=<n>/6 | impact=<1-5> | effort=<S|M|L> | score=<n>
   - Rationale: <one sentence>
   - Proposed Multica artifact: <…>

## Top action → routed to Skill Factory
- DEV-NN — <action #1 title>  (sub-issue dispatched this run)

## Next sweep window
<next-monday-09:00-Asia/Kuwait RFC3339>
```

Post via: `multica issue comment add <this-issue-id> --content-stdin` (HEREDOC the body in). Do NOT include any `mention://agent/...` link in this comment.

(6) Auto-dispatch the #1 action as a sub-issue to the Skill Factory Squad. Selection rule: the single highest-scoring action from the Top 3 (the acceptance criterion only requires the top action; only escalate the #2 and #3 if they are tied-on-score and equally well-formed — never invent fillers). The dispatch sub-issue:
   - Title: "BENCHMARK ACTION: <short action title>"
   - Parent: this autopilot's issue id
   - Project: 09 - Research Intelligence (e977793d-b825-448a-a3f1-bb8f59cc1266)
   - Priority: high
   - Status: todo (fires immediately — the action is already scored and rationalized)
   - Assignee: Skill Factory Squad (925a3e48-37f2-4620-870c-b57fe9003981)
   - Description must include: Input (the pattern observed + which vendors ship it), Expected Output (concrete artifact: new skill / template / prompt patch), Acceptance Criteria, Dependencies, Risk, Definition of Done.
   The squad leader fans out internally. Do NOT @mention any agent in the sub-issue body — assignment alone is the trigger.

(7) Pin metadata on this issue ONLY when materially useful for future runs. Recommended keys:
   - `sweep_window_end` (RFC3339)
   - `baseline_brief_id` (DEV-NN of the prior sweep used for diffing)
   - `vendors_covered` (number, expect 6)
   - `vendors_skipped` (string, comma-separated, only if non-empty)
   - `dispatched_count` (number, expect 1; rarely 2–3 if ties)
   - `material_change_vendors` (string, comma-separated list of vendors whose diff was non-empty)
   Use `multica issue metadata set` once each. Skip any key whose value matches what `metadata list` already shows.

(8) Flip this issue's status to `in_review` (`multica issue status <this-issue-id> in_review`) so the CEO Command Squad can verify the week-over-week delta. Do NOT close it — CEO verifies and closes. The dispatched sub-issue stays `todo` for Skill Factory.

(9) Output to stdout (one line only, no comment): `Benchmark Sweep @ <RFC3339> | vendors=<covered>/6 | material_changes=<n> | top3=<n> | dispatched=<n>`.

OPERATING RULES:
- Never block on a single CLI/HTTP failure. Log "skipped <vendor|source>: <reason>" and continue.
- Cap dispatch at 1 sub-issue (acceptance criterion: "Auto-routes top action to Skill Factory Squad"). Only escalate to 2–3 when scores tie and both items are PR-ready specs.
- Read metadata before pinning. Only update keys whose values changed.
- All comments go on the auto-created issue or on the dispatch sub-issue this run spawned. Never comment on DEV-36, DEV-50, DEV-60, or any other unrelated issue.
- Diff section must be non-empty (or explicitly say "No material change since <baseline date>") for every vendor — that is the acceptance criterion.
- Every claim must have a source URL — no hand-wavy assertions.
- The created issue MUST land in `in_review`, never `done` — CEO verifies week-over-week trend.
```
