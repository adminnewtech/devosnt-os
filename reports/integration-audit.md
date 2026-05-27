# Integration Audit Report

_Generated: 2026-05-27T12:05:54.988628+00:00_

## Health Summary

| Metric | Count |
|---|---|
| agents_without_model | 41 |
| orphan_skills | 7 |
| agents_without_skills | 0 |
| empty_squads | 0 |
| squads_without_leader | 0 |
| inactive_autopilots | 0 |
| missing_required_autopilots | 0 |
| missing_projects | 0 |
| blocked_issues | 1 |
| in_review_parent_count | 2 |
| agents_outside_squad_preview | 18 |

## Coverage Matrix

- **Agents:** 41 (with skills: 41, without: 0)
- **Skills:** 120 (owned: 113, orphan: 7)
- **Squads:** 10 (active members: 10)
- **Projects:** 11 (pipeline gaps: 0)
- **Autopilots:** 9 (active: 9)

## Verdict: RED 🔴 — 41 errors, 8 warnings

## Findings

| Severity | Area | Detail | Remediation |
|---|---|---|---|
| 🔴 ERROR | `agent.model` | `ceo` has empty model | Set model via `multica agent update` |
| 🔴 ERROR | `agent.model` | `sprint-commander` has empty model | Set model via `multica agent update` |
| 🔴 ERROR | `agent.model` | `quality-gate-manager` has empty model | Set model via `multica agent update` |
| 🔴 ERROR | `agent.model` | `workspace-operations-manager` has empty model | Set model via `multica agent update` |
| 🔴 ERROR | `agent.model` | `product-manager` has empty model | Set model via `multica agent update` |
| 🔴 ERROR | `agent.model` | `ux-architect` has empty model | Set model via `multica agent update` |
| 🔴 ERROR | `agent.model` | `ui-designer` has empty model | Set model via `multica agent update` |
| 🔴 ERROR | `agent.model` | `arabic-rtl-experience-agent` has empty model | Set model via `multica agent update` |
| 🔴 ERROR | `agent.model` | `solution-architect` has empty model | Set model via `multica agent update` |
| 🔴 ERROR | `agent.model` | `database-architect` has empty model | Set model via `multica agent update` |
| 🔴 ERROR | `agent.model` | `api-architect` has empty model | Set model via `multica agent update` |
| 🔴 ERROR | `agent.model` | `integration-architect` has empty model | Set model via `multica agent update` |
| 🔴 ERROR | `agent.model` | `claude-code-lead-developer` has empty model | Set model via `multica agent update` |
| 🔴 ERROR | `agent.model` | `frontend-engineer` has empty model | Set model via `multica agent update` |
| 🔴 ERROR | `agent.model` | `backend-engineer` has empty model | Set model via `multica agent update` |
| 🔴 ERROR | `agent.model` | `full-stack-engineer` has empty model | Set model via `multica agent update` |
| 🔴 ERROR | `agent.model` | `mobile-engineer` has empty model | Set model via `multica agent update` |
| 🔴 ERROR | `agent.model` | `qa-engineer` has empty model | Set model via `multica agent update` |
| 🔴 ERROR | `agent.model` | `bug-hunter` has empty model | Set model via `multica agent update` |
| 🔴 ERROR | `agent.model` | `security-auditor` has empty model | Set model via `multica agent update` |
| 🔴 ERROR | `agent.model` | `performance-tester` has empty model | Set model via `multica agent update` |
| 🔴 ERROR | `agent.model` | `deployment-engineer` has empty model | Set model via `multica agent update` |
| 🔴 ERROR | `agent.model` | `environment-manager` has empty model | Set model via `multica agent update` |
| 🔴 ERROR | `agent.model` | `release-manager` has empty model | Set model via `multica agent update` |
| 🔴 ERROR | `agent.model` | `documentation-agent` has empty model | Set model via `multica agent update` |
| 🔴 ERROR | `agent.model` | `skill-builder` has empty model | Set model via `multica agent update` |
| 🔴 ERROR | `agent.model` | `template-builder` has empty model | Set model via `multica agent update` |
| 🔴 ERROR | `agent.model` | `prompt-optimizer` has empty model | Set model via `multica agent update` |
| 🔴 ERROR | `agent.model` | `memory-curator` has empty model | Set model via `multica agent update` |
| 🔴 ERROR | `agent.model` | `research-scout` has empty model | Set model via `multica agent update` |
| 🔴 ERROR | `agent.model` | `github-analyst` has empty model | Set model via `multica agent update` |
| 🔴 ERROR | `agent.model` | `docs-analyst` has empty model | Set model via `multica agent update` |
| 🔴 ERROR | `agent.model` | `tool-evaluator` has empty model | Set model via `multica agent update` |
| 🔴 ERROR | `agent.model` | `codegraph-indexer` has empty model | Set model via `multica agent update` |
| 🔴 ERROR | `agent.model` | `codebase-cartographer` has empty model | Set model via `multica agent update` |
| 🔴 ERROR | `agent.model` | `impact-analyst` has empty model | Set model via `multica agent update` |
| 🔴 ERROR | `agent.model` | `growth-lead` has empty model | Set model via `multica agent update` |
| 🔴 ERROR | `agent.model` | `seo-specialist` has empty model | Set model via `multica agent update` |
| 🔴 ERROR | `agent.model` | `content-writer-ar-en` has empty model | Set model via `multica agent update` |
| 🔴 ERROR | `agent.model` | `analytics-lead` has empty model | Set model via `multica agent update` |
| 🔴 ERROR | `agent.model` | `onboarding-designer` has empty model | Set model via `multica agent update` |
| 🟡 WARN | `issue.blocked` | DEV-126 blocked: OPS: Provision FIGMA_TOKEN + live smoke test for figma-to-ux | Review blocker — autopilot caps at 3 retries |
| 🟡 WARN | `skill.orphan` | Skill `benchmark-vendor-tracker` has no agent owner | Assign to the most relevant agent, or archive if obsolete |
| 🟡 WARN | `skill.orphan` | Skill `code-reviewer` has no agent owner | Assign to the most relevant agent, or archive if obsolete |
| 🟡 WARN | `skill.orphan` | Skill `multi-agent-coordinator` has no agent owner | Assign to the most relevant agent, or archive if obsolete |
| 🟡 WARN | `skill.orphan` | Skill `security-auditor` has no agent owner | Assign to the most relevant agent, or archive if obsolete |
| 🟡 WARN | `skill.orphan` | Skill `security-hardening-owasp` has no agent owner | Assign to the most relevant agent, or archive if obsolete |
| 🟡 WARN | `skill.orphan` | Skill `tdd-mastery` has no agent owner | Assign to the most relevant agent, or archive if obsolete |
| 🟡 WARN | `skill.orphan` | Skill `vendor-brief-changelog-verification` has no agent owner | Assign to the most relevant agent, or archive if obsolete |
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

- `agent-self-healing-policy` — 5 owner(s): ceo, sprint-commander, claude-code-lead-developer, skill-builder, prompt-optimizer
- `wcag-accessibility-checklist` — 5 owner(s): quality-gate-manager, ux-architect, ui-designer, frontend-engineer, qa-engineer
- `onboarding-flow-builder` — 5 owner(s): product-manager, ux-architect, growth-lead, content-writer-ar-en, onboarding-designer
- `i18n-multilang-setup` — 5 owner(s): ux-architect, ui-designer, arabic-rtl-experience-agent, frontend-engineer, mobile-engineer
- `agentic-codegen-loop` — 5 owner(s): claude-code-lead-developer, frontend-engineer, backend-engineer, full-stack-engineer, mobile-engineer
- `analytics-tracking-setup` — 5 owner(s): frontend-engineer, growth-lead, seo-specialist, analytics-lead, onboarding-designer
- `api-contract-designer` — 4 owner(s): ceo, solution-architect, api-architect, backend-engineer
- `auth-permission-matrix` — 4 owner(s): ceo, solution-architect, database-architect, security-auditor
- `cross-project-pattern-extractor` — 4 owner(s): ceo, skill-builder, memory-curator, research-scout
- `deployment-checklist` — 4 owner(s): ceo, deployment-engineer, environment-manager, release-manager

## Self-improvement loop status

1. **Factory Pulse v3** — runs every 15 min, routes work, no human in loop ✅
2. **Factory Health Daily Audit** — flags stale/cost/SLO issues daily ✅
3. **Skill Improvement Weekly Loop** — mines retry_log, proposes prompt fixes + new skills ✅
4. **cross-project-pattern-extractor skill** — runs on every project close ✅
5. **reusable-template-extractor skill** — promotes 3x-repeated patterns to skills ✅
6. **prompt-improvement-review skill** — audits agent prompts, owned by `prompt-optimizer` ✅

The loop is: **failure → retry_log → weekly mining → fix proposal → prompt-optimizer applies**.
