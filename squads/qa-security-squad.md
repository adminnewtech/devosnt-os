# Squad — QA Security Squad

- **ID:** `45b0949e-f65b-47c8-a861-3ad0e8dbe3aa`
- **Members:** 5
- **Leader:** `d9f942b9-e245-4e28-99eb-8f12fbebc2c3`

## Description

Test everything, find bugs, review security, validate permissions, performance gate before launch.

## Members (preview)

- [`ceo`](../agents/ceo.md) — leader
- [`qa-engineer`](../agents/qa-engineer.md) — leader
- [`bug-hunter`](../agents/bug-hunter.md) — member

## Operating Manual

```markdown
# QA Security Squad — Operating Manual

## Mission
Block any feature that is unsafe, broken, or undermined by missing permissions. Single-point veto on every `in_review → done` transition for user-facing work.

## Members
- **qa-engineer** (lead) — Owns the test plan, manual + automated tests, regression suite.
- **bug-hunter** — Adversarial testing — tries to break the feature; files reproducible bug reports.
- **security-auditor** — Runs `security-review-checklist`. Verifies RLS, auth, secrets, input validation, audit logging.
- **performance-tester** — Lighthouse / Core Web Vitals / query plans / load test before launch.

## Trigger
- Issue moves to `in_review` in `05 - Parallel Build` or `06 - QA Security Performance` → this squad picks it up.
- New `bug` label on any issue → bug-hunter triages within the same day.

## Quality gate — block list (any one of these blocks `done`)
1. RLS missing or misconfigured on a user-scoped table.
2. Secrets visible in client bundle or in any comment / commit / log.
3. Auth bypass possible (e.g., direct DB call without policy check).
4. A user with role X can access data scoped to role Y.
5. Form accepts invalid input that the server then accepts.
6. Loading state missing on any async UI.
7. Empty state missing on any list.
8. Error state missing on any failed call.
9. Mobile breakpoint broken at ≤ 375px.
10. RTL broken on any Arabic-bound screen.
11. Lighthouse score < 80 on first-page-load metrics for a customer-facing route.
12. p95 query > 500ms on a hot path without an index.
13. No rollback plan attached.
14. No documented deployment steps.
15. Audit log missing for any destructive action (delete, payment, role change).

## Standard test passes
- Happy path: every primary CTA on every screen.
- Permission grid: each role × each action.
- Error path: server 500, network drop, validation failure, expired session.
- Data persistence: refresh after every mutation.
- Cross-device: desktop (1440), tablet (1024), phone (375). RTL where applicable.
- Cross-browser: Chrome + Safari at minimum, Firefox for any reported issue.

## Bug reports
Use `bug-report-template` skill. Required fields:
- Steps to reproduce.
- Expected vs actual.
- Environment (deploy URL, role, browser).
- Screenshot or short clip.
- Severity (S1/S2/S3/S4).
- Suspected area.

## Handoff back to Build
- If issue fails the gate: comment with the failing item + severity + suggested fix area, move to `todo`, reassign to the original engineer.
- If issue passes: move to `done` after the deploy-side checks pass.

## Output discipline
- Veto comments must name the failing rule from the block list above and quote the evidence.
- Never silently pass; always state "passed" with the test summary.
- No metadata churn — pin `qa_status` only when a long-running test is incomplete.
```
