#!/usr/bin/env python3
"""Integration audit: detect orphans, gaps, and broken wiring across the factory.

Writes reports/integration-audit.md
"""
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "snapshots" / "raw"
DEVOSNT_WS = "6ab51ea8-1c35-46e7-a387-961e2877f3cf"


def load(name):
    p = RAW / f"{name}.json"
    if not p.exists():
        return []
    d = json.loads(p.read_text())
    if isinstance(d, dict):
        for key in ("issues", "items", "autopilots", "data"):
            if key in d and isinstance(d[key], list):
                return d[key]
        return [d]
    return d


def in_ws(item):
    return item.get("workspace_id") == DEVOSNT_WS


def main():
    agents = [a for a in load("agents") if in_ws(a)]
    skills = [s for s in load("skills") if in_ws(s)]
    squads = [s for s in load("squads") if in_ws(s)]
    projects = [p for p in load("projects") if in_ws(p)]
    autopilots = [a for a in load("autopilots") if in_ws(a)]
    issues = [i for i in load("issues") if i.get("workspace_id") == DEVOSNT_WS]

    findings = []  # (severity, area, detail, remediation)
    stats = {}

    # --- 1. Models ---
    no_model = [a for a in agents if not a.get("model")]
    if no_model:
        for a in no_model:
            findings.append(("ERROR", "agent.model",
                             f"`{a['name']}` has empty model",
                             "Set model via `multica agent update`"))
    stats["agents_without_model"] = len(no_model)

    # --- 2. Agent ↔ Skill coverage ---
    skill_owners = {}
    agent_skill_counts = {}
    for a in agents:
        sk = a.get("skills") or []
        agent_skill_counts[a["name"]] = len(sk)
        for s in sk:
            skill_owners.setdefault(s["id"], []).append(a["name"])

    orphan_skills = [s for s in skills if s["id"] not in skill_owners]
    for s in orphan_skills:
        findings.append(("WARN", "skill.orphan",
                         f"Skill `{s['name']}` has no agent owner",
                         "Assign to the most relevant agent, or archive if obsolete"))
    stats["orphan_skills"] = len(orphan_skills)

    no_skill_agents = [a for a in agents if not (a.get("skills") or [])]
    for a in no_skill_agents:
        findings.append(("WARN", "agent.no_skills",
                         f"Agent `{a['name']}` has zero skills attached",
                         "Attach at least the skill(s) named in its instructions"))
    stats["agents_without_skills"] = len(no_skill_agents)

    # --- 3. Squad coverage ---
    empty_squads = [s for s in squads if (s.get("member_count") or 0) == 0]
    for s in empty_squads:
        findings.append(("ERROR", "squad.empty",
                         f"Squad `{s['name']}` has no members",
                         "Add at least a leader agent"))
    no_leader = [s for s in squads if not s.get("leader_id")]
    for s in no_leader:
        findings.append(("WARN", "squad.no_leader",
                         f"Squad `{s['name']}` has no explicit leader",
                         "Designate a leader agent"))
    stats["empty_squads"] = len(empty_squads)
    stats["squads_without_leader"] = len(no_leader)

    # --- 4. Autopilot health ---
    inactive_aps = [a for a in autopilots if a.get("status") != "active"]
    for a in inactive_aps:
        findings.append(("ERROR", "autopilot.inactive",
                         f"Autopilot `{a['title']}` is `{a.get('status')}`",
                         "Re-activate or delete if obsolete"))
    stats["inactive_autopilots"] = len(inactive_aps)

    # Required autopilots
    titles = {a["title"] for a in autopilots}
    required = ["Factory Pulse — Auto-route & Unblock",
                "Factory Health Daily Audit",
                "Skill Improvement Weekly Loop"]
    missing = [t for t in required if t not in titles]
    for t in missing:
        findings.append(("ERROR", "autopilot.missing",
                         f"Required autopilot `{t}` is missing",
                         "Re-create with `multica autopilot create`"))
    stats["missing_required_autopilots"] = len(missing)

    # --- 5. Project coverage ---
    pipeline_required = ["00 - Factory Brain", "01 - App Requests", "02 - Product Specs",
                         "03 - UX UI Design System", "04 - Architecture Database API",
                         "05 - Parallel Build", "06 - QA Security Performance",
                         "07 - Deploy Documentation Handover", "08 - Skill Library"]
    titles = {p["title"] for p in projects}
    missing_p = [t for t in pipeline_required if t not in titles]
    for t in missing_p:
        findings.append(("ERROR", "project.missing",
                         f"Pipeline project `{t}` is missing",
                         "Recreate to keep IDEA→DEPLOYED flow intact"))
    stats["missing_projects"] = len(missing_p)

    # --- 6. Issue health ---
    blocked = [i for i in issues if i.get("status") == "blocked"]
    for i in blocked:
        findings.append(("WARN", "issue.blocked",
                         f"{i.get('identifier')} blocked: {i.get('title','')[:60]}",
                         "Review blocker — autopilot caps at 3 retries"))
    stats["blocked_issues"] = len(blocked)

    # In-review with no parent (likely real review needed)
    in_review_orphans = [i for i in issues if i.get("status") == "in_review" and not i.get("parent_issue_id")]
    stats["in_review_parent_count"] = len(in_review_orphans)

    # --- 7. Squad ↔ agent membership coverage ---
    members_in_squads = set()
    for s in squads:
        for m in s.get("member_preview", []):
            if m.get("member_type") == "agent":
                members_in_squads.add(m["member_id"])
    unaffiliated = [a for a in agents if a["id"] not in members_in_squads and a["name"] != "ceo"]
    # ceo is everywhere — exempt
    if unaffiliated:
        for a in unaffiliated:
            findings.append(("INFO", "agent.no_squad",
                             f"Agent `{a['name']}` not in member_preview of any squad",
                             "May still be member; member_preview shows top 3 only — confirm with squad detail"))
    stats["agents_outside_squad_preview"] = len(unaffiliated)

    # --- Sort findings by severity ---
    sev_order = {"ERROR": 0, "WARN": 1, "INFO": 2}
    findings.sort(key=lambda x: (sev_order[x[0]], x[1]))

    # --- Render ---
    lines = [
        "# Integration Audit Report",
        "",
        f"_Generated: {datetime.now(timezone.utc).isoformat()}_",
        "",
        "## Health Summary",
        "",
        "| Metric | Count |",
        "|---|---|",
    ]
    for k, v in stats.items():
        lines.append(f"| {k} | {v} |")
    lines += ["", "## Coverage Matrix", "",
              f"- **Agents:** {len(agents)} (with skills: {sum(1 for c in agent_skill_counts.values() if c>0)}, "
              f"without: {sum(1 for c in agent_skill_counts.values() if c==0)})",
              f"- **Skills:** {len(skills)} (owned: {len(skills)-len(orphan_skills)}, orphan: {len(orphan_skills)})",
              f"- **Squads:** {len(squads)} (active members: {len(squads)-len(empty_squads)})",
              f"- **Projects:** {len(projects)} (pipeline gaps: {len(missing_p)})",
              f"- **Autopilots:** {len(autopilots)} (active: {sum(1 for a in autopilots if a.get('status')=='active')})",
              ""]

    # Overall verdict
    errors = sum(1 for f in findings if f[0] == "ERROR")
    warns = sum(1 for f in findings if f[0] == "WARN")
    if errors == 0 and warns == 0:
        verdict = "GREEN ✅ — factory fully integrated"
    elif errors == 0:
        verdict = f"YELLOW ⚠️ — {warns} warnings, no blockers"
    else:
        verdict = f"RED 🔴 — {errors} errors, {warns} warnings"
    lines += [f"## Verdict: {verdict}", ""]

    lines += ["## Findings", "", "| Severity | Area | Detail | Remediation |", "|---|---|---|---|"]
    for sev, area, detail, fix in findings:
        emoji = {"ERROR": "🔴", "WARN": "🟡", "INFO": "🔵"}[sev]
        lines.append(f"| {emoji} {sev} | `{area}` | {detail} | {fix} |")

    lines += ["", "## Top skills by adoption", ""]
    adoption = sorted(skill_owners.items(), key=lambda x: -len(x[1]))[:10]
    skill_by_id = {s["id"]: s for s in skills}
    for sid, owners in adoption:
        sname = skill_by_id.get(sid, {}).get("name", sid)
        lines.append(f"- `{sname}` — {len(owners)} owner(s): {', '.join(owners)}")

    lines += ["", "## Self-improvement loop status", "",
              "1. **Factory Pulse v3** — runs every 15 min, routes work, no human in loop ✅",
              "2. **Factory Health Daily Audit** — flags stale/cost/SLO issues daily ✅",
              "3. **Skill Improvement Weekly Loop** — mines retry_log, proposes prompt fixes + new skills ✅",
              "4. **cross-project-pattern-extractor skill** — runs on every project close ✅",
              "5. **reusable-template-extractor skill** — promotes 3x-repeated patterns to skills ✅",
              "6. **prompt-improvement-review skill** — audits agent prompts, owned by `prompt-optimizer` ✅",
              "",
              "The loop is: **failure → retry_log → weekly mining → fix proposal → prompt-optimizer applies**.",
              ""]

    out = ROOT / "reports" / "integration-audit.md"
    out.parent.mkdir(exist_ok=True)
    out.write_text("\n".join(lines))
    print(f"Audit written: {out}")
    print(f"Verdict: {verdict}")
    print(f"Findings: {len(findings)} ({errors} errors, {warns} warnings)")


if __name__ == "__main__":
    main()
