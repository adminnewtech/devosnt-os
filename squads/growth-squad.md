# Squad — Growth Squad

- **ID:** `3ff01911-bb76-4e3b-8eb9-ffbee295803a`
- **Members:** 7
- **Leader:** `634be4c5-858b-4b2d-9a01-ad169f0a1db4`

## Description

Launch readiness: landing page, SEO, onboarding, analytics events, conversion checklist, launch comms. Sits between Knowledge Graph and DevOps in the lifecycle.

## Members (preview)

- [`growth-lead`](../agents/growth-lead.md) — leader
- [`seo-specialist`](../agents/seo-specialist.md) — member
- [`content-writer-ar-en`](../agents/content-writer-ar-en.md) — member

## Operating Manual

```markdown
# Growth Squad — Operating Manual

## Mission
Make every shipped app launch-ready before it reaches DevOps. The factory builds the binary; the Growth Squad turns it into a product people can find, sign up for, and adopt. Nothing flips `lifecycle_phase=deploy` until this squad has signed `growth_gate=green`.

## Members
- **growth-lead** (leader) — Owns the launch plan, growth gate, and the Growth → DevOps handoff. Runs `growth-launch-plan` on every parent.
- **seo-specialist** — Sitemap, robots, per-route meta, OG/Twitter cards, JSON-LD, starter keyword map. Owns `seo-baseline-setup`.
- **content-writer-ar-en** — Bilingual launch copy (Arabic-Kuwaiti default for NewTech): landing page, onboarding micro-copy, emails, social, app-store listing.
- **analytics-lead** — Event taxonomy, conversion funnel, KPI dashboard, pre-launch baseline. Owns `analytics-tracking-setup`.
- **onboarding-designer** — First-run experience: signup → verify → setup → first value. Owns `onboarding-flow-builder` and the activation target.
- **arabic-rtl-experience-agent** (shared with Product UX) — RTL mirroring + Arabic-Kuwaiti review on bilingual launches.
- **frontend-engineer** (shared with Build) — Production wiring for landing page + onboarding flow.

## Trigger
- Factory Pulse autopilot reassigns the parent to Growth Squad when `lifecycle_phase=integrate` AND `deploy_gate=green`.
- On entry, growth-lead flips parent metadata `lifecycle_phase=growth` and runs `growth-launch-plan`.
- `growth-launch-plan` fans out 5 sub-issues in parallel:
  - `landing-page-builder` → frontend-engineer + content-writer-ar-en + seo-specialist (joint owners)
  - `seo-baseline-setup` → seo-specialist
  - `onboarding-flow-builder` → onboarding-designer + content-writer-ar-en
  - `analytics-tracking-setup` → analytics-lead
  - Launch-day comms bundle → content-writer-ar-en
- When all 5 land in `done`, growth-lead flips `growth_gate=green`. The next Factory Pulse run hands the parent to DevOps Launch Squad.

## Definition of "Growth ready"
- Landing page live with primary CTA above the fold (URL pinned to parent metadata `landing_url`).
- SEO baseline applied: sitemap.xml, robots.txt, per-page meta + OG + JSON-LD, 10-keyword starter map.
- Onboarding flow shipped end-to-end with the activation event firing (default target: 60% of signups reach `FirstValueReached` in session).
- Analytics events instrumented in client + server, conversion funnel report shows non-zero data, KPI dashboard URL pinned (`analytics_dashboard_url`).
- Launch-day comms drafted: welcome email + 3 social posts + in-app announcement (bilingual when PRD is bilingual).
- Growth conversion checklist signed off by growth-lead.
- Arabic-Kuwaiti review passed (when bilingual) — arabic-rtl-experience-agent must sign off on copy + RTL layout.

## Handoff to DevOps
Hand off only when `growth_gate=green` is pinned and every sub-issue is `done` or `cancelled` with a reason. DevOps cannot start deploy until growth-lead's signoff comment lands on the parent. The parent metadata at handoff carries: `landing_url`, `analytics_dashboard_url`, `growth_gate=green`, `launch_date`.

## Quality gates owned
- Block any parent moving to `lifecycle_phase=deploy` if any growth artifact is missing.
- Block any landing page that ships without analytics OR without SEO baseline.
- Block any bilingual project whose Arabic copy has not been reviewed.
- Block any onboarding flow that lacks an instrumented activation event.
- Veto a DevOps deploy attempt if `growth_gate` is anything but `green`.

## Output discipline
- Launch plan goes in the parent as a `growth-launch-plan` comment, with 5 sub-issue links.
- Each artifact ships as its own sub-issue in the parent's project (or `05 - Parallel Build` when the artifact requires production wiring).
- Pin only re-readable facts on parent metadata: `landing_url`, `analytics_dashboard_url`, `growth_gate`, `launch_date`, `waiting_on`. Never log run state.
- Never mention an agent in a wrap-up — squad dispatch and Factory Pulse advance work without re-pinging anyone.

## Skills owned
`growth-launch-plan`, `landing-page-builder`, `seo-baseline-setup`, `onboarding-flow-builder`, `analytics-tracking-setup`, `ab-testing-framework`. Shared: `app-store-listing-optimizer` (with Product UX), `content-style-guide-ar-en` (with arabic-rtl-experience-agent).

## Escalation
Escalate to CEO Command Squad when: scope of launch expands beyond the PRD, two channels disagree on launch copy, paid acquisition is requested, or external integrations (Mailchimp, PostHog, GA4, app-store accounts) need credentials. Escalate to workspace owner only after CEO Command Squad cannot resolve internally.
```
