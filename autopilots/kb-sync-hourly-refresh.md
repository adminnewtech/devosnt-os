# Autopilot — KB Sync — Hourly Refresh

- **ID:** `47668345-3f72-4821-af88-c4233b4764cd`
- **Status:** `active`
- **Execution mode:** `run_only`
- **Assignee:** `f3a68587-4383-43b1-8f03-16b12ee95797` (agent)
- **Last run:** 2026-06-19T13:00:10Z
- **Created:** 2026-05-25T19:25:40Z

## Description / Steps

```markdown
KB Sync — Hourly Refresh. Runs every hour. Pull live workspace snapshots and refresh the devosnt-os knowledge base on GitHub so the audit and KB never drift more than 60 minutes from live state.

CRITICAL: This autopilot is run_only. Never create new issues. Do not change any issue status. Do not mention any agent. Stay quiet on success — only post a comment on DEV-36 (id e60d5be5-b9dd-48aa-b949-28286ea80f1b) if the audit verdict regresses (GREEN→YELLOW/RED).

Steps:

(1) Clone or update the KB repo:
    if [ -d /tmp/devosnt-os ]; then cd /tmp/devosnt-os && git pull --quiet; else cd /tmp && gh repo clone adminnewtech/devosnt-os --quiet; fi
    cd /tmp/devosnt-os

(2) Refresh raw snapshots (all 6 resource lists + 7 issue status lists). Use --output json on every call. Continue on any single failure:
    mkdir -p snapshots/raw
    for resource in agents skills squads projects autopilots workspaces; do multica $resource list --output json > snapshots/raw/$resource.json 2>/dev/null; done
    for status in done in_review in_progress backlog todo blocked cancelled; do multica issue list --output json --status $status > snapshots/raw/issues-$status.json 2>/dev/null; done
    multica issue list --output json > snapshots/raw/issues.json 2>/dev/null

(3) Re-render KB + run audit:
    python3 scripts/render_kb.py
    python3 scripts/audit_integration.py

(4) Detect drift. If git status --porcelain shows changes:
    - Commit with body: "chore: hourly KB sync — <COUNTS>" (counts from snapshots/SNAPSHOT.md)
    - Push to main
    - Update DEV-36 metadata key kb_sync_status to "<verdict>@<RFC3339-now>" (e.g. "green@2026-05-25T20:00Z") via: multica issue metadata set e60d5be5-b9dd-48aa-b949-28286ea80f1b --key kb_sync_status --value "..."
    - Update DEV-36 metadata key audit_verdict to the verdict from reports/integration-audit.md (GREEN, YELLOW, or RED)

(5) Verdict regression escalation. ONLY if the new verdict is YELLOW or RED (was GREEN before): post one comment on DEV-36 summarizing the new findings, parented to comment 9322ef81-1035-4f7a-832e-74c9a9d8f7da. No mentions.

(6) Output one-line summary to stdout: "KB Sync @ HH:MM | verdict=<G/Y/R> | drift=<yes/no> | issues=N agents=N skills=N". If git is clean and verdict is unchanged, say "KB Sync @ HH:MM | clean".

Operating rules:
- Never block on a single CLI failure. Log and continue.
- Run quietly. No issue comments unless verdict regresses.
- Never mention any agent.
- Use git config user.name "devosnt-os-bot" + user.email "bot@devosnt.local" before committing.
- Do not modify any issue status. Do not modify any non-metadata field on any issue.
```
