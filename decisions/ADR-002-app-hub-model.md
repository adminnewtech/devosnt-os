# ADR-002 — App Hub Model

**Status:** Accepted (DEV-37)
**Date:** 2026-05-25
**Owners:** CEO Command Squad

## Context
Before this ADR, every app's artifacts (PRD, schema, build sub-issues, QA reports, deploy plan, runbook) were scattered across the workspace's pipeline projects (`01 - App Requests`, `02 - Product Specs`, etc.) and the parent `APP — *` issue.

This made it hard to:
- See "everything about app X" in one place.
- Hand the app off to a customer or to a maintenance crew.
- Refresh the codegraph baseline for a specific repo.

## Decision
Every new app gets its own **App Hub project** at intake:

- Project name: `APP — <App Name>`
- Project description: brief, GitHub repo URL, lifecycle phase
- Project lead: the assigned squad agent
- Every artifact about the app lives in that project (PRD, schema, build sub-issues, QA, deploy, runbook).
- Closes when the app is shipped.

A matching GitHub repo is created under `adminnewtech/<app-name>` by the `app-hub-bootstrap` skill. The repo URL is pinned to the parent issue metadata as `github_repo_url`.

## Lifecycle phases (parent metadata `lifecycle_phase`)
1. `intake` — App Hub project just created, brief in progress
2. `plan` — PRD / schema / API contract / role matrix being produced
3. `build` — Build sub-issues running in parallel
4. `integrate` — All build children done, Knowledge Graph Squad refreshing codegraph + impact analysis
5. `deploy` — DevOps Launch Squad executing deployment-checklist
6. `done` — App live, Skill Factory Squad runs post-build extraction

## Deploy gate
Parent advances `integrate → deploy` only when `deploy_gate=green` is pinned. No bypass.

## Consequences
- Factory Pulse v3 reads `lifecycle_phase` to decide the next squad.
- Skill extraction is automatically triggered when a parent reaches `done`.
- Customer handover = one project link, not a workspace scavenger hunt.

## Related
- Skill: `app-hub-bootstrap`
- Autopilot: `Factory Pulse — Auto-route & Unblock`
- Squad: `Knowledge Graph Squad`
