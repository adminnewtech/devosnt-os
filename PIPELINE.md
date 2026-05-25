# Factory Pipeline — Live Board

The pipeline mirrors the 8 numbered Multica projects. Click any stage for the open work + recent done items.

| # | Stage | Live link |
|---|---|---|
| 00 | 🧠 Factory Brain | [projects/00 - Factory Brain](./projects/00---factory-brain.md) |
| 01 | 💡 App Requests | [projects/01 - App Requests](./projects/01---app-requests.md) |
| 02 | 📐 Product Specs | [projects/02 - Product Specs](./projects/02---product-specs.md) |
| 03 | 🎨 UX UI Design System | [projects/03 - UX UI Design System](./projects/03---ux-ui-design-system.md) |
| 04 | 🏗️ Architecture | [projects/04 - Architecture Database API](./projects/04---architecture-database-api.md) |
| 05 | ⚙️ Parallel Build | [projects/05 - Parallel Build](./projects/05---parallel-build.md) |
| 06 | 🛡️ QA / Security | [projects/06 - QA Security Performance](./projects/06---qa-security-performance.md) |
| 07 | 🚀 Deploy & Handover | [projects/07 - Deploy Documentation Handover](./projects/07---deploy-documentation-handover.md) |
| 08 | 📚 Skill Library | [projects/08 - Skill Library](./projects/08---skill-library.md) |
| 09 | 🔬 Research Intelligence | [projects/09 - Research Intelligence](./projects/09---research-intelligence.md) |

## Active App Hubs

| Hub | Lifecycle phase | Snapshot |
|---|---|---|
| 📱 APP — Android Attendance | _check parent metadata_ | [project page](./projects/app-android-attendance.md) |

## Add the native GitHub Projects v2 board (optional)

Projects v2 needs the `project` scope on the GitHub token. One-time setup:

```bash
gh auth refresh -s project,read:project
gh project create --owner adminnewtech --title "devosnt — App Factory Pipeline"
# Then add the seven pipeline columns: App Requests, Product Specs, UX, Architecture, Build, QA, Deploy
```

After that, the daily sync workflow can also sync open Multica issues into the board.

The markdown pipeline above is the source-of-truth view; the Projects v2 board is a presentation layer.
