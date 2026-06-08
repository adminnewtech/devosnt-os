# Autopilot — Skill Improvement Weekly Loop

- **ID:** `656afad6-c9eb-40b3-8fb3-26ef3676f859`
- **Status:** `active`
- **Execution mode:** `create_issue`
- **Assignee:** `5822179b-4e9e-40ea-bca2-70f4c80d2a19` (agent)
- **Last run:** 2026-06-08T04:00:03Z
- **Created:** 2026-05-25T15:56:16Z

## Description / Steps

```markdown
Run the weekly skill improvement loop. (1) Pull all retry_log metadata across issues touched in the past 7 days — find the top 5 most-failed skills; (2) Run cross-project-pattern-extractor across the past week's closed issues; (3) For each repeated failure pattern (≥3 occurrences) propose: a prompt fix, a missing default, or a new skill; (4) Run prompt-improvement-review on the top 3 failed skills; (5) Run workspace-upgrade-report scan; (6) Post a ranked action list as a comment on the created issue — top 5 actions with: rationale, source issues, effort estimate, owner agent. Memory Curator and Prompt Optimizer pick up the top 3 immediately. Never skip a week — silent skip is itself a finding.
```
