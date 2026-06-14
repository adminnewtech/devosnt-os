# Autopilot — Factory Health Daily Audit

- **ID:** `0cf43035-4ef9-4b41-b99a-9f84a4ec9872`
- **Status:** `active`
- **Execution mode:** `create_issue`
- **Assignee:** `f3a68587-4383-43b1-8f03-16b12ee95797` (agent)
- **Last run:** 2026-06-14T03:00:14Z
- **Created:** 2026-05-25T15:56:10Z

## Description / Steps

```markdown
Run the daily factory health audit. Cover: (1) runtime health (multica runtime list) — alert if any offline >5m; (2) WIP discipline — flag any agent with >3 in_progress or any squad with >6; (3) stale issues — list any in_progress issue >24h with no comments; (4) orphan/zero-skill check — every skill assigned to ≥1 agent; every agent has ≥1 skill; (5) metadata hygiene — sample 10 done issues and flag any with stale waiting_on / blocked_reason; (6) cost — pull the current month spend per project and compare to budget (cost-budget-tracker); (7) error budget — pull yesterday's Sentry error rate, latency p95, uptime % per shipped app and alert on SLO burn. Post one consolidated comment on the created issue with: GREEN/YELLOW/RED status, the top 5 issues found, and one-line remediation per issue. Status the issue 'done' if all green; 'in_review' if YELLOW; 'blocked' if RED. Do not silently ignore failures.
```
