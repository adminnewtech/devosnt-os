# Autopilot — Factory Pulse — Auto-route & Unblock

- **ID:** `b7f20bdc-5e6d-4089-8e92-f2476846dd61`
- **Status:** `active`
- **Execution mode:** `run_only`
- **Assignee:** `ebd03ec3-2a72-433f-b89f-bf4d35573a3d` (agent)
- **Last run:** 2026-06-05T08:00:12Z
- **Created:** 2026-05-25T17:20:18Z

## Description / Steps

```markdown
Factory Pulse v3 — App Hub model + lifecycle_phase + deploy_gate enforcement + Growth-before-Deploy gate. Run every 15 minutes. Mode=run_only. Do NOT create new issues.

CRITICAL EXCLUSIONS: NEVER touch DEV-36 (the workspace-operations dialog with the workspace owner). NEVER touch any issue whose creator is a member AND whose title contains "تابع" or "مراجعة" or whose project is the CEO/ops project. These are conversations, not work items.

Steps:

(1) QA dispatch — list every issue with status=in_review whose parent_issue_id is NOT null (children only — never parents). For each: if assignee is NOT the QA Security Squad (id 45b0949e-f65b-47c8-a861-3ad0e8dbe3aa), reassign via `multica issue update <id> --assignee-id 45b0949e-f65b-47c8-a861-3ad0e8dbe3aa`. The squad leader fans out. Skip if already on QA squad.

(2) Build dispatch — list issues with status=todo whose parent is not null. If assignee is a build-engineer name (mobile-engineer, frontend-engineer, backend-engineer, full-stack-engineer), leave it. Otherwise reassign to Build Squad (a51cdb63-a37d-4e54-80cf-a0534ff416f7). Cap at 6 per pulse.

(3) Backlog promotion — list backlog issues. If parent in_progress AND all sibling prerequisites done/cancelled, flip to todo + comment "Promoted — prereqs landed."

(4) Stall detection — any in_progress issue updated_at >90min ago with no new comment since updated_at. Reassign to same agent (re-fires the run). Track retry_log metadata; cap at 3 attempts then set status=blocked.

(5) Parent advance — for every parent (in_review or in_progress) where ALL children are done/cancelled: read parent metadata. Decide next destination by `lifecycle_phase`:
   - If `lifecycle_phase=build` OR unset → flip metadata `lifecycle_phase=integrate` and reassign parent to **Knowledge Graph Squad (981c8c82-88ca-4940-a2cb-20e1893707b7)** for codegraph refresh + impact analysis + integration-branch verification. Comment: "All build children landed — dispatching Knowledge Graph Squad for integrate phase."
   - If `lifecycle_phase=integrate` AND `deploy_gate=green` → flip metadata `lifecycle_phase=growth` and reassign parent to **Growth Squad (3ff01911-bb76-4e3b-8eb9-ffbee295803a)** to run growth-launch-plan (landing page, SEO baseline, onboarding flow, analytics events, launch comms). Comment: "Integration green — dispatching Growth Squad for launch readiness." DevOps is NOT dispatched until Growth signs the gate.
   - If `lifecycle_phase=integrate` AND `deploy_gate!=green` (missing, red, or pending) → DO NOT dispatch. Comment once: "Holding parent in integrate — deploy_gate not green." Skip further pulses until gate flips.
   - If `lifecycle_phase=growth` AND `growth_gate=green` → reassign parent to **DevOps Launch Squad (d097f96a-2467-4c3c-b6e3-4c8a13517d17)** + flip `lifecycle_phase=deploy`. Comment: "Growth ready — dispatching DevOps Launch Squad."
   - If `lifecycle_phase=growth` AND `growth_gate!=green` (missing, red, or pending) → DO NOT dispatch. Comment once: "Holding parent in growth — growth_gate not green." Skip further pulses until gate flips.
   - If `lifecycle_phase=deploy` AND parent done → step (6) handles skill extraction.
   Do NOT mention CEO — squad dispatch replaces CEO re-entry.

(6) Skill extraction trigger — when a parent moves to done, reassign a copy-of-issue to Skill Factory Squad (925a3e48-37f2-4620-870c-b57fe9003981) for cross-project-pattern-extractor + reusable-template-extractor.

(7) Model audit — fix any agent with empty model (set claude-sonnet-4-6 + runtime 6af6eb94-a120-43e6-b6de-5e1503c2f1e3).

(8) App Hub bootstrap watch — any parent issue with title prefix "APP — " or label "app-request" and missing metadata key `app_project_id`: reassign to ceo (d9f942b9-e245-4e28-99eb-8f12fbebc2c3) with comment "App Hub bootstrap needed — run app-hub-bootstrap skill." Cap 2 per pulse.

(9) Output — one-line summary printed (no comment, no new issue). Format: "Pulse @ HH:MM | QA: N | Build: N | Promoted: N | Stalls: N | Parents→KG: N | Parents→Growth: N | Parents→DevOps: N | Held(deploy_gate): N | Held(growth_gate): N | Skills extracted: N | Agents fixed: N". If all zero: print "Pulse @ HH:MM | quiet".

Operating rules:
- Never block on a single CLI failure. Log and continue.
- Use --output json everywhere.
- NEVER mention CEO (d9f942b9-e245-4e28-99eb-8f12fbebc2c3) — squad dispatch handles all advance.
- Read metadata before pinning. Only update keys that changed.
- This autopilot is run_only; never create new issues.
- Hard skip rules: DEV-36, any issue with creator_type=member AND status=in_progress (those are active human conversations).
- `deploy_gate=green` only authorizes Growth dispatch (integrate→growth). `growth_gate=green` is the ONLY signal that authorizes DevOps dispatch (growth→deploy). No bypass.
```
