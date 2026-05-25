#!/usr/bin/env python3
"""Render Multica JSON snapshots into a browsable markdown knowledge base.

Inputs:  snapshots/raw/*.json
Outputs: agents/*.md, skills/*.md, squads/*.md, projects/*.md, autopilots/*.md,
         workspace/_index.md, snapshots/SNAPSHOT.md
"""
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "snapshots" / "raw"

# Workspace ID for filtering (devosnt)
DEVOSNT_WS = "6ab51ea8-1c35-46e7-a387-961e2877f3cf"


def load(name):
    path = RAW / f"{name}.json"
    if not path.exists():
        return []
    with path.open() as f:
        data = json.load(f)
    if isinstance(data, dict):
        for key in ("issues", "items", "autopilots", "data"):
            if key in data and isinstance(data[key], list):
                return data[key]
        return [data]
    return data


def slugify(name):
    s = re.sub(r"[^a-zA-Z0-9_-]+", "-", name.lower()).strip("-")
    return s or "unnamed"


def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


def in_ws(item):
    return item.get("workspace_id") == DEVOSNT_WS


# ---------------- AGENTS ----------------
def render_agents(agents, skills_by_id):
    out_dir = ROOT / "agents"
    out_dir.mkdir(exist_ok=True)
    index = ["# Agents\n",
             "Total agents in `devosnt`: **{}**\n".format(sum(1 for a in agents if in_ws(a))),
             "| Name | Model | Runtime | Skills | Description |",
             "|---|---|---|---|---|"]
    for a in sorted(agents, key=lambda x: x["name"]):
        if not in_ws(a):
            continue
        slug = slugify(a["name"])
        skill_count = len(a.get("skills", []) or [])
        index.append(
            f"| [{a['name']}](./{slug}.md) | `{a.get('model','-') or '-'}` "
            f"| `{a.get('runtime_mode','-')}` | {skill_count} | {a.get('description','')[:80]} |"
        )
        body = [
            f"# Agent — {a['name']}\n",
            f"- **ID:** `{a['id']}`",
            f"- **Model:** `{a.get('model','-') or '-'}`",
            f"- **Runtime mode:** `{a.get('runtime_mode','-')}`",
            f"- **Runtime ID:** `{a.get('runtime_id','-')}`",
            f"- **Max concurrent tasks:** {a.get('max_concurrent_tasks','-')}",
            f"- **Created:** {a.get('created_at','')}",
            "",
            "## Description",
            "",
            a.get("description") or "_(no description)_",
            "",
            "## Skills",
            "",
        ]
        skill_list = a.get("skills") or []
        if skill_list:
            for s in sorted(skill_list, key=lambda x: x["name"]):
                body.append(f"- [`{s['name']}`](../skills/{slugify(s['name'])}.md) — {s.get('description','')}")
        else:
            body.append("_(no skills assigned)_")
        body += ["", "## Instructions", "", "```markdown",
                 a.get("instructions") or "(none)", "```", ""]
        write(out_dir / f"{slug}.md", "\n".join(body))
    write(out_dir / "README.md", "\n".join(index) + "\n")


# ---------------- SKILLS ----------------
def render_skills(skills, agents):
    out_dir = ROOT / "skills"
    out_dir.mkdir(exist_ok=True)
    # Build skill→agents reverse index
    skill_to_agents = {}
    for a in agents:
        if not in_ws(a):
            continue
        for s in (a.get("skills") or []):
            skill_to_agents.setdefault(s["id"], []).append(a["name"])

    index = ["# Skills\n",
             "Total skills in `devosnt`: **{}**\n".format(sum(1 for s in skills if in_ws(s))),
             "| Skill | Owners | Description |",
             "|---|---|---|"]
    for s in sorted(skills, key=lambda x: x["name"]):
        if not in_ws(s):
            continue
        slug = slugify(s["name"])
        owners = skill_to_agents.get(s["id"], [])
        owners_str = ", ".join(f"`{o}`" for o in owners) if owners else "_(unowned)_"
        index.append(f"| [{s['name']}](./{slug}.md) | {owners_str} | {s.get('description','')[:90]} |")
        body = [
            f"# Skill — {s['name']}\n",
            f"- **ID:** `{s['id']}`",
            f"- **Created:** {s.get('created_at','')}",
            "",
            "## Description",
            "",
            s.get("description") or "_(no description)_",
            "",
            "## Owned by",
            "",
        ]
        if owners:
            for o in owners:
                body.append(f"- [`{o}`](../agents/{slugify(o)}.md)")
        else:
            body.append("_⚠️ No agent owns this skill — orphan_")
        body += ["", "## Config", "", "```json",
                 json.dumps(s.get("config") or {}, indent=2), "```", ""]
        write(out_dir / f"{slug}.md", "\n".join(body))
    write(out_dir / "README.md", "\n".join(index) + "\n")


# ---------------- SQUADS ----------------
def render_squads(squads, agents_by_id):
    out_dir = ROOT / "squads"
    out_dir.mkdir(exist_ok=True)
    index = ["# Squads\n",
             "Total squads in `devosnt`: **{}**\n".format(sum(1 for s in squads if in_ws(s))),
             "| Squad | Members | Description |",
             "|---|---|---|"]
    for sq in sorted(squads, key=lambda x: x["name"]):
        if not in_ws(sq):
            continue
        slug = slugify(sq["name"])
        index.append(f"| [{sq['name']}](./{slug}.md) | {sq.get('member_count','?')} | {sq.get('description','')[:90]} |")
        body = [
            f"# Squad — {sq['name']}\n",
            f"- **ID:** `{sq['id']}`",
            f"- **Members:** {sq.get('member_count', 0)}",
            f"- **Leader:** `{sq.get('leader_id','-')}`",
            "",
            "## Description",
            "",
            sq.get("description") or "",
            "",
            "## Members (preview)",
            "",
        ]
        for m in sq.get("member_preview", []):
            mid = m.get("member_id")
            agent = agents_by_id.get(mid)
            if agent:
                body.append(f"- [`{agent['name']}`](../agents/{slugify(agent['name'])}.md) — {m.get('role','member')}")
            else:
                body.append(f"- `{mid}` — {m.get('role','member')}")
        body += ["", "## Operating Manual", "", "```markdown",
                 sq.get("instructions") or "(none)", "```", ""]
        write(out_dir / f"{slug}.md", "\n".join(body))
    write(out_dir / "README.md", "\n".join(index) + "\n")


# ---------------- PROJECTS ----------------
def render_projects(projects, all_issues):
    out_dir = ROOT / "projects"
    out_dir.mkdir(exist_ok=True)
    # Index issues by project_id
    issues_by_project = {}
    for i in all_issues:
        if i.get("workspace_id") != DEVOSNT_WS:
            continue
        issues_by_project.setdefault(i.get("project_id"), []).append(i)

    index = ["# Projects\n",
             "| Icon | Project | Issues | Done | Description |",
             "|---|---|---|---|---|"]
    for p in sorted(projects, key=lambda x: x.get("title", "")):
        if not in_ws(p):
            continue
        slug = slugify(p["title"])
        ic = p.get("icon", "") or ""
        index.append(f"| {ic} | [{p['title']}](./{slug}.md) | {p.get('issue_count',0)} | {p.get('done_count',0)} | {p.get('description','')[:80]} |")
        body = [
            f"# {ic} {p['title']}\n",
            f"- **ID:** `{p['id']}`",
            f"- **Status:** `{p.get('status','-')}`",
            f"- **Issues:** {p.get('issue_count',0)} (done: {p.get('done_count',0)})",
            "",
            "## Description",
            "",
            p.get("description") or "",
            "",
            "## Open Issues (snapshot)",
            "",
        ]
        project_issues = issues_by_project.get(p["id"], [])
        open_issues = [i for i in project_issues if i.get("status") not in ("done", "cancelled")]
        if open_issues:
            body.append("| ID | Title | Status | Priority |")
            body.append("|---|---|---|---|")
            for i in sorted(open_issues, key=lambda x: x.get("identifier", "")):
                body.append(f"| {i.get('identifier','?')} | {i.get('title','')[:80]} | `{i.get('status','-')}` | {i.get('priority','-')} |")
        else:
            body.append("_(no open issues)_")
        body += ["", "## Recent Done", ""]
        done_issues = sorted([i for i in project_issues if i.get("status") == "done"],
                             key=lambda x: x.get("updated_at", ""), reverse=True)[:10]
        if done_issues:
            for i in done_issues:
                body.append(f"- {i.get('identifier','?')} — {i.get('title','')[:80]}")
        else:
            body.append("_(none)_")
        write(out_dir / f"{slug}.md", "\n".join(body) + "\n")
    write(out_dir / "README.md", "\n".join(index) + "\n")


# ---------------- AUTOPILOTS ----------------
def render_autopilots(autopilots):
    out_dir = ROOT / "autopilots"
    out_dir.mkdir(exist_ok=True)
    index = ["# Autopilots\n",
             "Scheduled / triggered automations that keep the factory running without manual intervention.\n",
             "| Autopilot | Status | Mode | Last Run | Assignee |",
             "|---|---|---|---|---|"]
    for ap in sorted(autopilots, key=lambda x: x["title"]):
        if not in_ws(ap):
            continue
        slug = slugify(ap["title"])
        index.append(f"| [{ap['title']}](./{slug}.md) | `{ap.get('status','-')}` | `{ap.get('execution_mode','-')}` | {ap.get('last_run_at','never')} | `{ap.get('assignee_id','-')[:8]}…` |")
        body = [
            f"# Autopilot — {ap['title']}\n",
            f"- **ID:** `{ap['id']}`",
            f"- **Status:** `{ap.get('status','-')}`",
            f"- **Execution mode:** `{ap.get('execution_mode','-')}`",
            f"- **Assignee:** `{ap.get('assignee_id','-')}` ({ap.get('assignee_type','-')})",
            f"- **Last run:** {ap.get('last_run_at','never')}",
            f"- **Created:** {ap.get('created_at','')}",
            "",
            "## Description / Steps",
            "",
            "```markdown",
            ap.get("description") or "",
            "```",
            "",
        ]
        write(out_dir / f"{slug}.md", "\n".join(body))
    write(out_dir / "README.md", "\n".join(index) + "\n")


# ---------------- SNAPSHOT METADATA ----------------
def render_snapshot_meta(counts):
    body = [
        "# Snapshot",
        "",
        f"- **Generated at:** {datetime.now(timezone.utc).isoformat()}",
        f"- **Workspace ID:** `{DEVOSNT_WS}`",
        "",
        "## Counts",
        "",
        "| Resource | Count |",
        "|---|---|",
    ]
    for k, v in counts.items():
        body.append(f"| {k} | {v} |")
    write(ROOT / "snapshots" / "SNAPSHOT.md", "\n".join(body) + "\n")


def main():
    agents = load("agents")
    skills = load("skills")
    squads = load("squads")
    projects = load("projects")
    autopilots = load("autopilots")
    all_issues = load("issues")

    agents_by_id = {a["id"]: a for a in agents}
    skills_by_id = {s["id"]: s for s in skills}

    render_agents(agents, skills_by_id)
    render_skills(skills, agents)
    render_squads(squads, agents_by_id)
    render_projects(projects, all_issues)
    render_autopilots(autopilots)

    counts = {
        "agents":   sum(1 for a in agents if in_ws(a)),
        "skills":   sum(1 for s in skills if in_ws(s)),
        "squads":   sum(1 for s in squads if in_ws(s)),
        "projects": sum(1 for p in projects if in_ws(p)),
        "autopilots": sum(1 for a in autopilots if in_ws(a)),
        "issues_total": sum(1 for i in all_issues if i.get("workspace_id") == DEVOSNT_WS),
    }
    render_snapshot_meta(counts)
    print("Render complete:", counts)


if __name__ == "__main__":
    main()
