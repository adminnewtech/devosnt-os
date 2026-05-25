# Squad — Product UX Squad

- **ID:** `0cb607aa-2bcc-430a-a050-1a18ce6767df`
- **Members:** 5
- **Leader:** `d9f942b9-e245-4e28-99eb-8f12fbebc2c3`

## Description

Turn ideas into products, screens, workflows, and user experiences. Owns PRDs, sitemaps, screen lists, UX flows, RTL/Arabic rules.

## Members (preview)

- [`ceo`](../agents/ceo.md) — leader
- [`product-manager`](../agents/product-manager.md) — leader
- [`ux-architect`](../agents/ux-architect.md) — member

## Operating Manual

```markdown
# Product UX Squad — Operating Manual

## Mission
Turn raw app ideas into implementation-ready product specs and UI flows. Every project enters the factory through this squad. Nothing reaches Build until this squad has signed off on the PRD, user stories, screen list, and role matrix.

## Members
- **product-manager** (lead) — Owns brief, PRD, MVP vs Production scope, acceptance criteria.
- **ux-architect** — Sitemap, user flows, navigation, state machines, empty/loading/error states.
- **ui-designer** — Screen-level layout, component selection, design tokens, dashboard shells.
- **arabic-rtl-experience-agent** — Arabic Kuwaiti copy, RTL mirroring, locale-aware date/number/currency rules.

## Trigger
- New issue in `01 - App Requests` → run `app-idea-to-product-brief` skill → produce one-page brief.
- Approved brief → run `product-brief-to-prd` → produce PRD in `02 - Product Specs`.
- Approved PRD → run `prd-to-user-stories` + `dashboard-screen-planner` + `auth-permission-matrix` in parallel.
- Approved stories → run `user-stories-to-issues` to generate Build issues in `05 - Parallel Build` as `--status backlog` (CEO promotes when Architecture is ready).

## Definition of "PRD ready"
- Business goal in one sentence.
- Named user personas with their top 3 jobs-to-be-done.
- MVP scope explicit + Production scope explicit + non-goals.
- Role matrix (who can see / do what).
- Top 10 user stories with acceptance criteria.
- Screen list with empty/loading/error states called out.
- Localization decision (English-only, Arabic-only, bilingual + RTL).
- Open questions block — anything that needs the user before Architecture starts.

## Definition of "UX ready"
- Sitemap shows every reachable screen.
- Per-screen spec: purpose, key components, primary CTA, secondary actions, data shown, permission gate, empty/loading/error variants.
- Mobile layout described for any screen that will be used on phones.
- RTL variant noted for any Arabic-bound screen.

## Handoff to Architecture
Hand off when PRD + screen list + role matrix are approved. Architecture cannot start the schema until the role matrix is final — otherwise RLS gets rewritten twice.

## Quality gates owned
- Block any project that lacks a Role Matrix.
- Block any user-visible screen that lacks empty/loading/error variants.
- Block Arabic-bound projects that lack an RTL plan.

## Output discipline
- Briefs and PRDs go in `02 - Product Specs` as issues, not comments.
- Screen lists go in `03 - UX UI Design System` as issues.
- Always link back to the originating App Request.
- Use [[mention://issue/<id>]] to link related artifacts.
```
