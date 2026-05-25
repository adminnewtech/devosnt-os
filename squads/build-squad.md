# Squad — Build Squad

- **ID:** `a51cdb63-a37d-4e54-80cf-a0534ff416f7`
- **Members:** 6
- **Leader:** `d9f942b9-e245-4e28-99eb-8f12fbebc2c3`

## Description

Builds the actual app fast. Lead Dev orchestrates Frontend/Backend/Full-Stack/Mobile engineers via Claude Code runtime.

## Members (preview)

- [`ceo`](../agents/ceo.md) — leader
- [`claude-code-lead-developer`](../agents/claude-code-lead-developer.md) — leader
- [`frontend-engineer`](../agents/frontend-engineer.md) — member

## Operating Manual

```markdown
# Build Squad — Operating Manual

## Mission
Build the actual app fast, with high quality, in parallel. This is where code is written. Every issue this squad picks up must have an approved Architecture pack behind it.

## Members
- **claude-code-lead-developer** (lead) — Orchestrates the squad, owns code quality, reviews PRs.
- **frontend-engineer** — Next.js / React / Tailwind. Components, pages, forms, state, validation.
- **backend-engineer** — API routes, server actions, Postgres, RLS, queries, jobs.
- **full-stack-engineer** — End-to-end features when frontend + backend should ship together.
- **mobile-engineer** — React Native / Expo. Screens, navigation, push, native integrations.

## Trigger
- Issue in `05 - Parallel Build` with `--status todo` and `assignee` = this squad or a member of it.
- Issue must reference: parent project issue, approved PRD, approved Architecture pack, the file/module in scope.

## Build standards (non-negotiable)
- TypeScript strict mode on. No `any` unchecked.
- Server-only secrets via env, never in client bundles.
- Every form: client-side validation + server-side validation.
- Every list: empty state + loading state + error state.
- Every mutation: optimistic UI when safe, with rollback on server error.
- Every user-scoped query: RLS-enforced at the DB, not just at the app layer.
- Every API endpoint: input validated (Zod), output typed, error shape uniform.
- Every PR: passes typecheck, lint, and the test suite locally.
- Never commit secrets. Never `git push --no-verify` unless CEO approves.

## Parallelization
- Independent build tasks run as sibling sub-issues in `--status todo`.
- Dependent steps are created as `--status backlog` and promoted by the lead when their input lands.
- Frontend + Backend split is fine; one engineer per file at a time.

## PR discipline
- One feature per PR. No drive-by refactors.
- PR description: what changed, why, screenshots if UI, test plan, env var changes if any.
- Pin `pr_url` to the issue metadata when the PR opens.
- Pin `pipeline_status` if CI is wired up.

## Quality gates owned
- Cannot move an issue to `in_review` until: code compiles, tests pass, RLS verified, screenshots attached for UI, env var list updated.
- Cannot self-promote to `done` — that requires QA Security squad.

## Handoff to QA Security
When the PR is open and CI is green, comment on the issue with:
1. PR link.
2. Preview deploy link (Vercel preview, Expo dev build).
3. Test credentials / role to use.
4. Areas of highest risk (where QA should look first).
Then move the issue to `in_review`.

## Output discipline
- All code goes in the project's Git repo, never in Multica comments.
- Comment the outcome on the issue, not the diff.
- Use plain language for status: "PR open, awaiting QA" beats "started ticket".
```
