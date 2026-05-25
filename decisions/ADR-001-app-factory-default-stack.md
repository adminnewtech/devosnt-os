# ADR-001 — Default Tech Stack

**Status:** Accepted
**Date:** 2026-05-25
**Owners:** Architecture Squad

## Decision
Default tech stack for every app produced by the factory:

| Layer | Tool | Why |
|---|---|---|
| Web | Next.js + React + TypeScript + Tailwind | Vercel-first, server components, mature ecosystem |
| Backend | Supabase (Postgres + Auth + Storage + Edge Functions) | RLS-first multitenancy, fastest path to prod, free tier covers MVP |
| Mobile | React Native + Expo | Code sharing with web, OTA updates |
| DB | Postgres | Single SQL dialect across all apps, JSONB escape hatch |
| Deploy | Vercel (web), Supabase (db), Expo EAS (mobile) | Zero infra for the factory to manage |
| Payments KW | KNet + MyFatoorah | Local rails Kuwaiti customers expect |
| Payments global | Stripe | The only global default that works |
| Messaging | Meta WhatsApp Cloud API | What customers in KW actually open |

## Deviation policy
Deviate only with explicit CEO Command Squad approval. The deviation must name:
1. The default that was rejected.
2. The reason no preset stack can solve the problem.
3. The added operational cost (extra runbook, extra runtime, extra agent).

## Consequences
- New build issues default to this stack without architecture re-debate.
- Every preset skill (`crm-system-builder`, `hr-system-builder`, etc.) assumes this stack.
- Cost is predictable: Vercel + Supabase free tier covers MVPs up to ~1k users.
