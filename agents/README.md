# Agents

Total agents in `devosnt`: **41**

| Name | Model | Runtime | Skills | Description |
|---|---|---|---|---|
| [analytics-lead](./analytics-lead.md) | `claude-sonnet-4-6` | `local` | 3 | Analytics event plan + conversion funnel + dashboards. Wires PostHog / Plausible |
| [api-architect](./api-architect.md) | `claude-sonnet-4-6` | `local` | 5 | Complete OpenAPI 3.1 contract before any endpoint is implemented. |
| [arabic-rtl-experience-agent](./arabic-rtl-experience-agent.md) | `claude-sonnet-4-6` | `local` | 3 | RTL UI + Kuwaiti-Arabic copy. Native, not machine-translated. |
| [backend-engineer](./backend-engineer.md) | `claude-sonnet-4-6` | `local` | 9 | API endpoints, DB access, jobs, webhooks. Codex runtime. |
| [bug-hunter](./bug-hunter.md) | `claude-sonnet-4-6` | `local` | 4 | Hunts edge-case defects QA didn't cover. Thinks like a power user/attacker. |
| [ceo](./ceo.md) | `claude-sonnet-4-6` | `local` | 19 | CEO Orchestrator — founding agent. Routes every issue, enforces the IDEA → DEPLO |
| [claude-code-lead-developer](./claude-code-lead-developer.md) | `claude-sonnet-4-6` | `local` | 8 | Orchestrates Build Squad. Decomposes parents, assigns engineers, unblocks. |
| [codebase-cartographer](./codebase-cartographer.md) | `claude-sonnet-4-6` | `local` | 1 | Owns the human-readable architecture overview per app: docs/ARCHITECTURE.md, gui |
| [codegraph-indexer](./codegraph-indexer.md) | `claude-sonnet-4-6` | `local` | 1 | Builds + refreshes the per-app codegraph index (SQLite + tree-sitter) and the Un |
| [content-writer-ar-en](./content-writer-ar-en.md) | `claude-sonnet-4-6` | `local` | 2 | Bilingual launch copy: landing page, email, social, in-app. Default to Arabic-Ku |
| [database-architect](./database-architect.md) | `claude-sonnet-4-6` | `local` | 8 | RLS-first PostgreSQL schema with indexes, audit, money + timezone hygiene. |
| [deployment-engineer](./deployment-engineer.md) | `claude-sonnet-4-6` | `local` | 7 | Production deploys + rollback plans. Confirms before pushing prod. |
| [docs-analyst](./docs-analyst.md) | `claude-sonnet-4-6` | `local` | 3 | Reads vendor docs + changelogs. Alerts on breaking changes. |
| [documentation-agent](./documentation-agent.md) | `claude-sonnet-4-6` | `local` | 4 | Keeps dev docs + admin/user guides current. EN + AR-KW where needed. |
| [environment-manager](./environment-manager.md) | `claude-sonnet-4-6` | `local` | 5 | Env vars, secrets, feature flags across local/preview/staging/prod. |
| [frontend-engineer](./frontend-engineer.md) | `claude-sonnet-4-6` | `local` | 12 | Next.js + TS + Tailwind frontend implementation with accessibility + responsive. |
| [full-stack-engineer](./full-stack-engineer.md) | `claude-sonnet-4-6` | `local` | 10 | Small end-to-end features (UI + API + migration) in one PR. Opencode runtime. |
| [github-analyst](./github-analyst.md) | `claude-sonnet-4-6` | `local` | 2 | Owner of github-research-workflow. Prior-art research for any non-trivial build. |
| [growth-lead](./growth-lead.md) | `claude-sonnet-4-6` | `local` | 6 | Growth Squad leader. Owns launch readiness, growth plan, conversion goals, and G |
| [impact-analyst](./impact-analyst.md) | `claude-sonnet-4-6` | `local` | 1 | On every Build sub-issue, runs codegraph_impact against the proposed change scop |
| [integration-architect](./integration-architect.md) | `claude-sonnet-4-6` | `local` | 8 | Plans every external integration (payments, Shopify, Zoho, WhatsApp). |
| [memory-curator](./memory-curator.md) | `claude-sonnet-4-6` | `local` | 4 | Audits workspace memory + pinned metadata for staleness. |
| [mobile-engineer](./mobile-engineer.md) | `claude-sonnet-4-6` | `local` | 6 | React Native (Expo) mobile apps. Claude runtime (swapped from Openclaw→Codex→Cla |
| [onboarding-designer](./onboarding-designer.md) | `claude-sonnet-4-6` | `local` | 2 | First-run experience: signup → verify → workspace setup → first value. Owns acti |
| [performance-tester](./performance-tester.md) | `claude-sonnet-4-6` | `local` | 3 | Runs performance-review-checklist with prod-like data volume. |
| [product-manager](./product-manager.md) | `claude-sonnet-4-6` | `local` | 11 | Idea → PRD → user stories → MVP scope cut. Hands off to UX + Architecture. |
| [prompt-optimizer](./prompt-optimizer.md) | `claude-sonnet-4-6` | `local` | 2 | Improves agent prompts via prompt-improvement-review. |
| [qa-engineer](./qa-engineer.md) | `claude-sonnet-4-6` | `local` | 6 | Writes + executes QA test plans. Pass/fail every shippable feature. |
| [quality-gate-manager](./quality-gate-manager.md) | `claude-sonnet-4-6` | `local` | 8 | Gates in_review→done. Runs agent-output-quality-review. Veto power. |
| [release-manager](./release-manager.md) | `claude-sonnet-4-6` | `local` | 6 | Release notes, customer comms, post-deploy verification. |
| [research-scout](./research-scout.md) | `claude-sonnet-4-6` | `local` | 4 | Weekly frontier scan: AI tools, SaaS competitors, patterns. |
| [security-auditor](./security-auditor.md) | `claude-sonnet-4-6` | `local` | 7 | Runs security-review-checklist. Veto on fail. |
| [seo-specialist](./seo-specialist.md) | `claude-sonnet-4-6` | `local` | 3 | SEO baseline + content discoverability. Owns sitemap, robots, meta, OG, JSON-LD, |
| [skill-builder](./skill-builder.md) | `claude-sonnet-4-6` | `local` | 4 | Lifts 3x-repeated workflows into reusable skills. |
| [solution-architect](./solution-architect.md) | `claude-sonnet-4-6` | `local` | 26 | Tech stack + ADRs + build graph. Default Next.js + Supabase + Vercel. |
| [sprint-commander](./sprint-commander.md) | `claude-sonnet-4-6` | `local` | 3 | Sprint cadence + parallel WIP enforcement across all squads. |
| [template-builder](./template-builder.md) | `claude-sonnet-4-6` | `local` | 3 | Turns shipped apps into reusable code templates + seed repos. |
| [tool-evaluator](./tool-evaluator.md) | `claude-sonnet-4-6` | `local` | 2 | Runs tool-comparison-workflow for any new tool/service decision. |
| [ui-designer](./ui-designer.md) | `claude-sonnet-4-6` | `local` | 6 | Design tokens, primitives, composed screens (LTR + RTL). |
| [ux-architect](./ux-architect.md) | `claude-sonnet-4-6` | `local` | 7 | PRD → sitemap → user flows → screen list with states + role visibility. |
| [workspace-operations-manager](./workspace-operations-manager.md) | `claude-sonnet-4-6` | `local` | 4 | Owns workspace settings, agent lifecycle, runtime health, quarterly upgrade. |
