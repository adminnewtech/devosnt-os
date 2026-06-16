# Integration Audit Report

_Generated: 2026-06-16T14:02:08.067588+00:00_

## Health Summary

| Metric | Count |
|---|---|
| agents_without_model | 0 |
| orphan_skills | 12 |
| agents_without_skills | 0 |
| empty_squads | 0 |
| squads_without_leader | 0 |
| inactive_autopilots | 0 |
| missing_required_autopilots | 0 |
| missing_projects | 0 |
| blocked_issues | 2 |
| in_review_parent_count | 7 |
| agents_outside_squad_preview | 18 |

## Coverage Matrix

- **Agents:** 41 (with skills: 41, without: 0)
- **Skills:** 146 (owned: 134, orphan: 12)
- **Squads:** 10 (active members: 10)
- **Projects:** 11 (pipeline gaps: 0)
- **Autopilots:** 9 (active: 9)

## Verdict: YELLOW ⚠️ — 14 warnings, no blockers

## Findings

| Severity | Area | Detail | Remediation |
|---|---|---|---|
| 🟡 WARN | `issue.blocked` | DEV-264 blocked: Factory Health Audit — 2026-06-15 | Review blocker — autopilot caps at 3 retries |
| 🟡 WARN | `issue.blocked` | DEV-257 blocked: QA Gate: DEV-187 — BENCHMARK ACTION: Pre-build Research Gate | Review blocker — autopilot caps at 3 retries |
| 🟡 WARN | `skill.orphan` | Skill `ab-test-analysis` has no agent owner | Assign to the most relevant agent, or archive if obsolete |
| 🟡 WARN | `skill.orphan` | Skill `growth-loop-designer` has no agent owner | Assign to the most relevant agent, or archive if obsolete |
| 🟡 WARN | `skill.orphan` | Skill `hipaa-compliance-checklist` has no agent owner | Assign to the most relevant agent, or archive if obsolete |
| 🟡 WARN | `skill.orphan` | Skill `pre-build-research-gate` has no agent owner | Assign to the most relevant agent, or archive if obsolete |
| 🟡 WARN | `skill.orphan` | Skill `pre-deploy-scan` has no agent owner | Assign to the most relevant agent, or archive if obsolete |
| 🟡 WARN | `skill.orphan` | Skill `sandbox-process-runner` has no agent owner | Assign to the most relevant agent, or archive if obsolete |
| 🟡 WARN | `skill.orphan` | Skill `seo-audit-checklist` has no agent owner | Assign to the most relevant agent, or archive if obsolete |
| 🟡 WARN | `skill.orphan` | Skill `supabase-mcp-setup` has no agent owner | Assign to the most relevant agent, or archive if obsolete |
| 🟡 WARN | `skill.orphan` | Skill `supabase-postgres-best-practices` has no agent owner | Assign to the most relevant agent, or archive if obsolete |
| 🟡 WARN | `skill.orphan` | Skill `universal-connector-install` has no agent owner | Assign to the most relevant agent, or archive if obsolete |
| 🟡 WARN | `skill.orphan` | Skill `user-skill-creation-wizard` has no agent owner | Assign to the most relevant agent, or archive if obsolete |
| 🟡 WARN | `skill.orphan` | Skill `weekly-status-email` has no agent owner | Assign to the most relevant agent, or archive if obsolete |
| 🔵 INFO | `agent.no_squad` | Agent `workspace-operations-manager` not in member_preview of any squad | May still be member; member_preview shows top 3 only — confirm with squad detail |
| 🔵 INFO | `agent.no_squad` | Agent `ui-designer` not in member_preview of any squad | May still be member; member_preview shows top 3 only — confirm with squad detail |
| 🔵 INFO | `agent.no_squad` | Agent `arabic-rtl-experience-agent` not in member_preview of any squad | May still be member; member_preview shows top 3 only — confirm with squad detail |
| 🔵 INFO | `agent.no_squad` | Agent `api-architect` not in member_preview of any squad | May still be member; member_preview shows top 3 only — confirm with squad detail |
| 🔵 INFO | `agent.no_squad` | Agent `integration-architect` not in member_preview of any squad | May still be member; member_preview shows top 3 only — confirm with squad detail |
| 🔵 INFO | `agent.no_squad` | Agent `backend-engineer` not in member_preview of any squad | May still be member; member_preview shows top 3 only — confirm with squad detail |
| 🔵 INFO | `agent.no_squad` | Agent `full-stack-engineer` not in member_preview of any squad | May still be member; member_preview shows top 3 only — confirm with squad detail |
| 🔵 INFO | `agent.no_squad` | Agent `mobile-engineer` not in member_preview of any squad | May still be member; member_preview shows top 3 only — confirm with squad detail |
| 🔵 INFO | `agent.no_squad` | Agent `security-auditor` not in member_preview of any squad | May still be member; member_preview shows top 3 only — confirm with squad detail |
| 🔵 INFO | `agent.no_squad` | Agent `performance-tester` not in member_preview of any squad | May still be member; member_preview shows top 3 only — confirm with squad detail |
| 🔵 INFO | `agent.no_squad` | Agent `release-manager` not in member_preview of any squad | May still be member; member_preview shows top 3 only — confirm with squad detail |
| 🔵 INFO | `agent.no_squad` | Agent `documentation-agent` not in member_preview of any squad | May still be member; member_preview shows top 3 only — confirm with squad detail |
| 🔵 INFO | `agent.no_squad` | Agent `prompt-optimizer` not in member_preview of any squad | May still be member; member_preview shows top 3 only — confirm with squad detail |
| 🔵 INFO | `agent.no_squad` | Agent `memory-curator` not in member_preview of any squad | May still be member; member_preview shows top 3 only — confirm with squad detail |
| 🔵 INFO | `agent.no_squad` | Agent `docs-analyst` not in member_preview of any squad | May still be member; member_preview shows top 3 only — confirm with squad detail |
| 🔵 INFO | `agent.no_squad` | Agent `tool-evaluator` not in member_preview of any squad | May still be member; member_preview shows top 3 only — confirm with squad detail |
| 🔵 INFO | `agent.no_squad` | Agent `analytics-lead` not in member_preview of any squad | May still be member; member_preview shows top 3 only — confirm with squad detail |
| 🔵 INFO | `agent.no_squad` | Agent `onboarding-designer` not in member_preview of any squad | May still be member; member_preview shows top 3 only — confirm with squad detail |

## Top skills by adoption

- `aegis-method-pack` — 9 owner(s): claude-code-lead-developer, frontend-engineer, backend-engineer, full-stack-engineer, mobile-engineer, qa-engineer, bug-hunter, security-auditor, performance-tester
- `systematic-debugging` — 9 owner(s): claude-code-lead-developer, frontend-engineer, backend-engineer, full-stack-engineer, mobile-engineer, qa-engineer, bug-hunter, security-auditor, performance-tester
- `verification-before-completion` — 9 owner(s): claude-code-lead-developer, frontend-engineer, backend-engineer, full-stack-engineer, mobile-engineer, qa-engineer, bug-hunter, security-auditor, performance-tester
- `delivery-comment-checklist` — 8 owner(s): ceo, quality-gate-manager, claude-code-lead-developer, frontend-engineer, backend-engineer, full-stack-engineer, mobile-engineer, skill-builder
- `establishing-project-context` — 6 owner(s): solution-architect, database-architect, api-architect, integration-architect, claude-code-lead-developer, codebase-cartographer
- `agent-self-healing-policy` — 5 owner(s): ceo, sprint-commander, claude-code-lead-developer, skill-builder, prompt-optimizer
- `wcag-accessibility-checklist` — 5 owner(s): quality-gate-manager, ux-architect, ui-designer, frontend-engineer, qa-engineer
- `onboarding-flow-builder` — 5 owner(s): product-manager, ux-architect, growth-lead, content-writer-ar-en, onboarding-designer
- `i18n-multilang-setup` — 5 owner(s): ux-architect, ui-designer, arabic-rtl-experience-agent, frontend-engineer, mobile-engineer
- `agentic-codegen-loop` — 5 owner(s): claude-code-lead-developer, frontend-engineer, backend-engineer, full-stack-engineer, mobile-engineer

## Self-improvement loop status

1. **Factory Pulse v3** — runs every 15 min, routes work, no human in loop ✅
2. **Factory Health Daily Audit** — flags stale/cost/SLO issues daily ✅
3. **Skill Improvement Weekly Loop** — mines retry_log, proposes prompt fixes + new skills ✅
4. **cross-project-pattern-extractor skill** — runs on every project close ✅
5. **reusable-template-extractor skill** — promotes 3x-repeated patterns to skills ✅
6. **prompt-improvement-review skill** — audits agent prompts, owned by `prompt-optimizer` ✅

The loop is: **failure → retry_log → weekly mining → fix proposal → prompt-optimizer applies**.
