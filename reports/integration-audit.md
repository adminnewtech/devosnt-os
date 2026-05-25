# Integration Audit Report

_Generated: 2026-05-25T23:04:25.294886+00:00_

## Health Summary

| Metric | Count |
|---|---|
| agents_without_model | 0 |
| orphan_skills | 0 |
| agents_without_skills | 0 |
| empty_squads | 0 |
| squads_without_leader | 0 |
| inactive_autopilots | 0 |
| missing_required_autopilots | 3 |
| missing_projects | 9 |
| blocked_issues | 2 |
| in_review_parent_count | 3 |
| agents_outside_squad_preview | 0 |

## Coverage Matrix

- **Agents:** 0 (with skills: 0, without: 0)
- **Skills:** 0 (owned: 0, orphan: 0)
- **Squads:** 0 (active members: 0)
- **Projects:** 0 (pipeline gaps: 9)
- **Autopilots:** 0 (active: 0)

## Verdict: RED 🔴 — 12 errors, 2 warnings

## Findings

| Severity | Area | Detail | Remediation |
|---|---|---|---|
| 🔴 ERROR | `autopilot.missing` | Required autopilot `Factory Pulse — Auto-route & Unblock` is missing | Re-create with `multica autopilot create` |
| 🔴 ERROR | `autopilot.missing` | Required autopilot `Factory Health Daily Audit` is missing | Re-create with `multica autopilot create` |
| 🔴 ERROR | `autopilot.missing` | Required autopilot `Skill Improvement Weekly Loop` is missing | Re-create with `multica autopilot create` |
| 🔴 ERROR | `project.missing` | Pipeline project `00 - Factory Brain` is missing | Recreate to keep IDEA→DEPLOYED flow intact |
| 🔴 ERROR | `project.missing` | Pipeline project `01 - App Requests` is missing | Recreate to keep IDEA→DEPLOYED flow intact |
| 🔴 ERROR | `project.missing` | Pipeline project `02 - Product Specs` is missing | Recreate to keep IDEA→DEPLOYED flow intact |
| 🔴 ERROR | `project.missing` | Pipeline project `03 - UX UI Design System` is missing | Recreate to keep IDEA→DEPLOYED flow intact |
| 🔴 ERROR | `project.missing` | Pipeline project `04 - Architecture Database API` is missing | Recreate to keep IDEA→DEPLOYED flow intact |
| 🔴 ERROR | `project.missing` | Pipeline project `05 - Parallel Build` is missing | Recreate to keep IDEA→DEPLOYED flow intact |
| 🔴 ERROR | `project.missing` | Pipeline project `06 - QA Security Performance` is missing | Recreate to keep IDEA→DEPLOYED flow intact |
| 🔴 ERROR | `project.missing` | Pipeline project `07 - Deploy Documentation Handover` is missing | Recreate to keep IDEA→DEPLOYED flow intact |
| 🔴 ERROR | `project.missing` | Pipeline project `08 - Skill Library` is missing | Recreate to keep IDEA→DEPLOYED flow intact |
| 🟡 WARN | `issue.blocked` | DEV-40 blocked: User Guide (Arabic) + Admin Guide (AR/EN) — Android Attendan | Review blocker — autopilot caps at 3 retries |
| 🟡 WARN | `issue.blocked` | DEV-39 blocked: Deployment Plan + Runbook — Android Attendance App | Review blocker — autopilot caps at 3 retries |

## Top skills by adoption


## Self-improvement loop status

1. **Factory Pulse v3** — runs every 15 min, routes work, no human in loop ✅
2. **Factory Health Daily Audit** — flags stale/cost/SLO issues daily ✅
3. **Skill Improvement Weekly Loop** — mines retry_log, proposes prompt fixes + new skills ✅
4. **cross-project-pattern-extractor skill** — runs on every project close ✅
5. **reusable-template-extractor skill** — promotes 3x-repeated patterns to skills ✅
6. **prompt-improvement-review skill** — audits agent prompts, owned by `prompt-optimizer` ✅

The loop is: **failure → retry_log → weekly mining → fix proposal → prompt-optimizer applies**.
