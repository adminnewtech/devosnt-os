# Squad — DevOps Launch Squad

- **ID:** `d097f96a-2467-4c3c-b6e3-4c8a13517d17`
- **Members:** 5
- **Leader:** `d9f942b9-e245-4e28-99eb-8f12fbebc2c3`

## Description

Deployment, environments, CI/CD, rollback, documentation, release notes, customer handover.

## Members (preview)

- [`ceo`](../agents/ceo.md) — leader
- [`deployment-engineer`](../agents/deployment-engineer.md) — leader
- [`environment-manager`](../agents/environment-manager.md) — member

## Operating Manual

```markdown
# DevOps Launch Squad — Operating Manual

## Mission
Take a QA-approved feature or product to production safely, with rollback ready and customer + admin docs in hand. Owns the moment between "QA passed" and "customer is using it".

## Members
- **deployment-engineer** (lead) — CI/CD pipelines, build, deploy, env hygiene.
- **environment-manager** — Env vars, secrets rotation, dev/staging/prod isolation.
- **release-manager** — Release notes, version tags, change log, customer comms.
- **documentation-agent** — README, ARCHITECTURE, RUNBOOK, user guide, admin guide.

## Trigger
- Issue in `07 - Deploy Documentation Handover` with `--status todo`.
- QA Security squad has signed off on the parent feature.

## Pre-deploy checklist (must be 100% green before any production push)
- All env vars listed and present in target environment.
- Migrations dry-runned against a staging DB snapshot.
- Feature flag wired up if rollout is gradual.
- Rollback plan written by `rollback-plan-generator` and reviewed.
- Release notes drafted via `release-manager`.
- User guide + admin guide updated (`user-guide-generator`, `admin-guide-generator`).
- Smoke test plan defined (3-5 critical user journeys).
- On-call agent / human identified for the launch window.
- Customer comms drafted if user-visible (Arabic-KW + English).

## Post-deploy checklist (must run within 30 min of cutover)
- Smoke tests executed on production.
- Error rate monitored for 30 min — must remain at or below baseline.
- p95 latency monitored — must remain at or below baseline.
- Auth flows verified with a real test account in each role.
- Payment flow verified with a sandbox transaction if payment was touched.
- Rollback path tested at least once in staging within the last 7 days.

## Rollback authority
- Deployment Engineer may roll back without approval if error rate > 2× baseline for 5 min.
- All other rollbacks require CEO approval; comment the reason.

## Handover artifacts (required for every shipped project)
- `README.md` — what the app is, how to run it, env vars list.
- `ARCHITECTURE.md` — stack, schema, API, auth, integrations, decisions.
- `RUNBOOK.md` — common incidents and how to fix them.
- `USER_GUIDE.md` — top journeys for the end user (bilingual if Arabic-bound).
- `ADMIN_GUIDE.md` — top journeys for the admin (bilingual if Arabic-bound).
- `ROLLBACK.md` — exact steps to undo the last deploy.

## Quality gates owned
- Cannot deploy without all pre-deploy items green.
- Cannot close a `07` issue without all handover artifacts checked in.

## Output discipline
- Pin `deploy_url`, `release_tag`, `rollback_tested_at` to the issue.
- Customer-facing release notes in Arabic-KW for NewTech projects unless told otherwise.
- Engineer-facing notes always English.
```
