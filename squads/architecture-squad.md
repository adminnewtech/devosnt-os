# Squad — Architecture Squad

- **ID:** `b85344f7-9de0-4670-952f-9eabf4966697`
- **Members:** 5
- **Leader:** `d9f942b9-e245-4e28-99eb-8f12fbebc2c3`

## Description

Tech stack, database schemas, API contracts, auth, permissions, integrations. Outputs implementation-ready architecture.

## Members (preview)

- [`ceo`](../agents/ceo.md) — leader
- [`solution-architect`](../agents/solution-architect.md) — leader
- [`database-architect`](../agents/database-architect.md) — member

## Operating Manual

```markdown
# Architecture Squad — Operating Manual

## Mission
Take an approved PRD + role matrix and produce implementation-ready architecture: stack, database schema, API contracts, auth model, integrations, and security posture. Build cannot start until this squad has signed off.

## Members
- **solution-architect** (lead) — Stack choice, system boundaries, scaling story, ADRs.
- **database-architect** — Relational schema, RLS-first policies, migrations, indexes, seed data.
- **api-architect** — HTTP API contract, OpenAPI 3.1 document, error model, pagination, versioning.
- **integration-architect** — Third-party integrations (Supabase, Stripe, KNet, MyFatoorah, Shopify, Zoho, WhatsApp Cloud, Meta, Google).

## Trigger
- New issue in `04 - Architecture Database API` → run `database-schema-designer` + `api-contract-designer` + `auth-permission-matrix` in parallel.
- Output of these three is the Architecture pack the Build Squad implements against.

## Definition of "Architecture ready"
- ADR-001: stack choice, with rejected alternatives and the reason.
- Schema: ER diagram + Postgres DDL + RLS policies per table + seed data plan.
- API contract: OpenAPI 3.1 doc with every endpoint, request/response shape, status codes, error model.
- Auth model: provider, token flow, session strategy, refresh strategy, RBAC rules wired to the role matrix.
- Integrations: per-integration brief — purpose, auth, rate limits, failure mode, idempotency, retry policy.
- Security model: secret storage, PII inventory, retention, audit log requirement, threat model summary.
- Cost note: estimated monthly cost at 100, 1k, 10k users for the chosen stack.

## Default tech stack (deviate only with CEO approval)
- Web: Next.js + React + TypeScript + Tailwind CSS.
- Backend: Supabase (Postgres + Auth + Storage + Edge Functions) OR Node.js/TypeScript API when Supabase doesn't fit.
- Mobile: React Native + Expo.
- DB: Postgres. Always RLS-first. Always migrations.
- Deploy: Vercel (web), Supabase (db), Expo EAS (mobile).
- Payments: KNet + MyFatoorah for Kuwait, Stripe for global.
- Messaging: Meta WhatsApp Cloud API.

## Quality gates owned
- Block Build if RLS is missing on any user-scoped table.
- Block Build if API contract has endpoints with no error model.
- Block Build if integrations have no documented failure mode.
- Block Build if secrets management is undefined.

## Handoff to Build
Once Architecture pack is approved, post a single comment on the parent project issue with:
1. Link to schema migration files / ADR.
2. Link to OpenAPI doc.
3. Link to permission matrix.
4. List of integrations and their owner agent.
5. List of env vars needed.
Then CEO promotes Build sub-issues from `backlog → todo`.

## Output discipline
- ADRs live in `00 - Factory Brain` (workspace standards) or `04 - Architecture Database API` (project-specific).
- Schemas and API contracts live in `04 - Architecture Database API`.
- Every architecture decision must name the rejected alternative.
```
