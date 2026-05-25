# One-time Setup — Make the repo self-syncing

The repo runs three GitHub Actions:

| Workflow | Trigger | What it does |
|---|---|---|
| `validate` | every push / PR | Re-renders docs from snapshots; PR fails if drift |
| `sync-from-multica` | daily 04:00 UTC + manual | Pulls fresh JSON from Multica → re-renders → commits drift |
| `weekly-improvement-digest` | Monday 06:00 UTC + manual | Builds week-over-week diff report |

`validate` works out of the box.

`sync-from-multica` needs Multica credentials wired as repo secrets. **One-time setup:**

```bash
# Multica server URL (e.g. https://api.multica.dev)
gh secret set MULTICA_SERVER_URL --repo adminnewtech/devosnt-os

# Multica API token with read access to the devosnt workspace
gh secret set MULTICA_TOKEN --repo adminnewtech/devosnt-os
```

Without these secrets, the workflow gracefully skips the snapshot step and only re-renders from the last committed snapshots (so it never errors out).

## Enable the native Projects v2 board

```bash
gh auth refresh -s project,read:project
gh project create --owner adminnewtech --title "devosnt — App Factory Pipeline"
```

Then add columns: `App Requests` → `Product Specs` → `UX` → `Architecture` → `Build` → `QA` → `Deploy`. The sync workflow can be extended to push open Multica issues into the board automatically.

## Force a manual sync right now

```bash
gh workflow run sync-from-multica.yml --repo adminnewtech/devosnt-os
```

## Re-render locally

```bash
python3 scripts/render_kb.py
python3 scripts/audit_integration.py
```

## Trust model

- **Multica is source of truth.** Don't hand-edit `agents/`, `skills/`, `squads/`, `projects/`, `autopilots/`, `snapshots/`.
- **The repo is mirror + audit + history.** Hand-edit only `README.md`, `PIPELINE.md`, `SETUP.md`, `workspace/`, `decisions/`, and scripts.
- **PRs auto-fail on hand-edited generated files** — the `validate` workflow re-runs the renderer and blocks drift.
