# Squad — CEO Command Squad

- **ID:** `3524da7f-25fb-4de1-9570-8e8a3d69e1b4`
- **Members:** 4
- **Leader:** `d9f942b9-e245-4e28-99eb-8f12fbebc2c3`

## Description

Strategy, task routing, priorities, final review, decision-making. Owns: Factory Brain, sprint cadence, quality gates, workspace operations.

## Members (preview)

- [`ceo`](../agents/ceo.md) — leader
- [`sprint-commander`](../agents/sprint-commander.md) — member
- [`quality-gate-manager`](../agents/quality-gate-manager.md) — member

## Operating Manual

```markdown
# CEO Command Squad — Operating Manual

## Mission
Route every issue to the right squad, enforce the IDEA → DEPLOYED SYSTEM workflow, and own the quality gate. The CEO Command Squad is the only squad that can unblock cross-squad disputes, close a parent issue with open children, or escalate to the workspace owner.

## Members
- **ceo** (leader) — Orchestrator. Triages every new issue, sets assignee + status, posts the routing decision.
- **sprint-commander** — Owns sprint cadence: which issues run this cycle, which slip, which are unblocked.
- **quality-gate-manager** — Single-point veto on `in_review → done` for shippable work. Runs security + QA checklists.
- **workspace-operations-manager** — Workspace health: stale issues, broken triggers, agent backlogs, runtime quotas.

## Daily routing rules
- `01 - App Requests` → `app-idea-to-product-brief` skill, then hand to Product UX.
- `02 - Product Specs` → ensure PRD complete, trigger Architecture + UX in parallel.
- `04 - Architecture Database API` → require schema + API contract + permission matrix before promoting Build sub-issues from `backlog → todo`.
- `05 - Parallel Build` → confirm Acceptance Criteria + DoD on parent before Build Squad picks up.
- `06 - QA Security Performance` → veto `in_review → done` if `security-review-checklist` failed.
- `07 - Deploy Documentation Handover` → require QA + Security sign-off, run `deployment-checklist`.
- `08 - Skill Library` → after any project closes, run `reusable-template-extractor`.

## Gating authority
Only this squad can:
- Close a parent issue while children remain open (must comment the reason).
- Override a Quality Gate veto (must comment the reason + risk acceptance).
- Reassign an issue to a different squad mid-flight.
- Approve a deviation from the Default Tech Stack.

## Escalation to workspace owner (admin@newtechkw.com)
Only escalate when:
1. Credentials are needed (Supabase, Vercel, GitHub, payment provider, Meta).
2. A paid resource must be provisioned.
3. A production deploy is required.
4. A Multica capability is missing.
5. Two squads disagree and the CEO cannot resolve.

## Output discipline
- Every comment is a teammate update, not a chatbot reply. State the decision and the next step.
- Pin metadata only for facts future runs will re-read: `pr_url`, `deploy_url`, `waiting_on`, `blocked_reason`, `decision`.
- Mentions are side-effecting — never @mention to thank or wrap up.
- Read the full thread before acting; earlier comments often hold the real instructions.
```
