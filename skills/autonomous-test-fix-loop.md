# Skill — autonomous-test-fix-loop

- **ID:** `622391e4-2b94-4a93-a858-305148e2344b`
- **Created:** 2026-05-26T17:04:18Z

## Description

After a build issue goes in_review, runs the QA test plan against the preview URL, creates a fix sub-issue on failure, and loops until all green or the 3-cycle retry cap triggers escalation.

## Owned by

- [`qa-engineer`](../agents/qa-engineer.md)
- [`bug-hunter`](../agents/bug-hunter.md)

## Config

```json
{}
```
