# 📱 APP — Android Attendance

- **ID:** `09e6cfd3-d45e-4225-a494-2e3400b6983c`
- **Status:** `in_progress`
- **Issues:** 16 (done: 4)

## Description

App Hub for the Android Attendance app (parent: DEV-25). Per the App Hub Model (ADR-002): every artifact for this app lives here — PRD, schema, build sub-issues, QA reports, deploy plan, runbook. Closes when the app is shipped. GitHub repo: pending admin provisioning (newtechkw/attendance-app). Lifecycle phase tracked on the parent issue metadata.

## Open Issues (snapshot)

| ID | Title | Status | Priority |
|---|---|---|---|
| DEV-348 | BUILD: Implement Postgres schema + RLS + audit trigger — Android Attendance | `in_review` | medium |
| DEV-349 | BUILD: Implement Supabase Edge Functions (punch, sync, reports, FCM) — Android A | `in_review` | medium |
| DEV-350 | BUILD: Next.js admin web frontend shell (RTL Arabic) — Android Attendance | `in_review` | medium |
| DEV-351 | BUILD: Supabase Auth integration — JWT custom claims hook + session management — | `in_review` | medium |
| DEV-352 | BUILD: React Native Expo mobile app shell (Android, RTL Arabic) — Android Attend | `blocked` | medium |
| DEV-356 | FIX: punch_rate_limit RLS — confirm tenant isolation (blocker for DEV-348) | `in_review` | high |
| DEV-360 | QA Gate: DEV-349 — BUILD: Implement Supabase Edge Functions (punch, sync, report | `in_progress` | none |
| DEV-361 | Emulator QA: DEV-352 — run 7 screens, offline sync test, attach screenshots | `blocked` | medium |
| DEV-365 | QA Gate 2: DEV-350 — Verify revision (loading states + component library) | `in_review` | medium |
| DEV-366 | REVISE: Confirm/add Zod validation on /employees, /offices, /shifts CRUD modals | `in_review` | medium |
| DEV-367 | QA Gate 3: DEV-350 — Verify CRUD Zod validation (Gate 3 of 3, forecast ACCEPT) | `in_progress` | medium |

## Recent Done

- DEV-362 — REVISE: Confirm loading/empty/error states + shadcn/ui — DEV-350 Next.js admin s
- DEV-358 — QA Gate: DEV-350 — BUILD: Next.js admin web frontend shell (RTL Arabic) — Androi
- DEV-359 — QA Gate: DEV-352 — BUILD: React Native Expo mobile app shell (Android, RTL Arabi
- DEV-355 — QA Gate: DEV-351 — BUILD: Supabase Auth integration — JWT custom claims hook + s
