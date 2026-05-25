# Squad — Skill Factory Squad

- **ID:** `925a3e48-37f2-4620-870c-b57fe9003981`
- **Members:** 5
- **Leader:** `d9f942b9-e245-4e28-99eb-8f12fbebc2c3`

## Description

Converts repeated successful workflows into reusable skills, templates, and memory. Compounds workspace velocity over time.

## Members (preview)

- [`ceo`](../agents/ceo.md) — leader
- [`skill-builder`](../agents/skill-builder.md) — leader
- [`template-builder`](../agents/template-builder.md) — member

## Operating Manual

```markdown
# Skill Factory Squad — Operating Manual

## Mission
Compound workspace velocity. Anything done well three times becomes a skill or template the rest of the factory can reuse. This is the squad that makes the next project faster than the last.

## Members
- **skill-builder** (lead) — Promotes a 3-times-repeated workflow into a Multica skill.
- **template-builder** — Promotes a shipped app into a starter template (Next.js + Supabase boilerplate, RTL dashboard shell, etc.).
- **prompt-optimizer** — Audits agent prompts, finds drift, proposes targeted edits.
- **memory-curator** — Owns the workspace memory: which lessons stick, which get pruned, what new patterns emerge.

## Trigger
- Issue in `08 - Skill Library` with `--status todo`.
- Post-project: CEO routes the project's `reusable-template-extractor` run here.
- Quarterly: `workspace-upgrade-report` skill runs, producing a self-audit.

## When to create a skill
- A workflow has been executed cleanly 3+ times across projects.
- An agent has produced a near-identical artifact 3+ times — promote the template.
- The workspace owner explicitly asks for one.
- A new external tool / API is integrated and the integration steps are repeatable.

## Skill anatomy (every new skill must define)
- Name (kebab-case).
- Purpose — one sentence on what it produces.
- Trigger — when an agent should run it.
- Required input.
- Step-by-step procedure.
- Output shape.
- Quality checklist — what good output looks like.
- Failure handling — what to do if a step fails.
- Improvement rule — when to update the skill itself.

## When to create a template instead
- A shipped app's full repo + schema + env is reusable as a starter.
- A common UI shell (dashboard, mobile, marketing) is a starting point for 3+ projects.
- A deployment recipe (Vercel + Supabase + custom domain) is repeatable.

## Prompt drift checks (monthly)
- Sample 5 recent runs per agent.
- Score against `agent-output-quality-review`.
- If score < 4/5, run `prompt-improvement-review` and propose targeted edits.
- All prompt edits require CEO approval before going live.

## Memory rules
- Save user role + preferences as `user` memory.
- Save corrections + validated approaches as `feedback` memory.
- Save initiative / deadline context as `project` memory.
- Save external system pointers as `reference` memory.
- Do NOT save code patterns (derivable from repo), ephemeral state, or runtime logs.

## Output discipline
- Every new skill is announced via a comment on the project that triggered it.
- Skills go through CEO review before being marked usable workspace-wide.
- Pin `skill_name`, `promoted_from_issues` on the skill creation issue.
```
