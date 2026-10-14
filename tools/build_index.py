"""Generate CURRICULUM.md and the per-folder progress report from the plan.

The generator reconciles the declared plan (``tools/curriculum_plan.py``) with
what actually exists on disk, so coverage figures are never optimistic.

Usage
-----
    python3 tools/build_index.py            # rewrite CURRICULUM.md
    python3 tools/build_index.py --check    # exit 1 if CURRICULUM.md is stale
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import curriculum_plan as plan  # noqa: E402
from frontmatter import FrontmatterError, read_lesson  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT = REPO_ROOT / "CURRICULUM.md"

LEVEL_BADGE = {
    "beginner": "B",
    "intermediate": "I",
    "advanced": "A",
    "graduate": "G",
    "doctoral": "D",
    "research": "R",
}


def status_of(rel_path: str) -> str:
    return "written" if (REPO_ROOT / rel_path).exists() else "planned"


def render() -> str:
    counts = plan.summary()
    cov = plan.coverage()
    lessons = plan.all_lessons()
    written = [lesson for lesson in lessons if (REPO_ROOT / lesson["path"]).exists()]
    # A lesson only counts as written if it is substantive, not a stub.
    substantive = []
    for lesson in written:
        try:
            meta = read_lesson(REPO_ROOT / lesson["path"])
            substantive.append(meta)
        except FrontmatterError:
            continue

    pct = (len(written) / counts["lessons"] * 100) if counts["lessons"] else 0.0

    lines: list[str] = []
    add = lines.append

    add("# Master Curriculum Index\n")
    add(
        "This file is **generated** by `python3 tools/build_index.py`. Do not edit it by "
        "hand; edit [`tools/curriculum_plan.py`](./tools/curriculum_plan.py) and regenerate.\n"
    )
    add("Legend: **B** beginner · **I** intermediate · **A** advanced · **G** graduate · "
        "**D** doctoral · **R** research professional. "
        "A check mark means the lesson file exists; a dot means it is planned and not yet written.\n")

    add("## Coverage at a glance\n")
    add("| Metric | Value |")
    add("|---|---|")
    add(f"| Folders | {counts['folders']} |")
    add(f"| Modules | {counts['modules']} |")
    add(f"| Lessons planned | {counts['lessons']} |")
    add(f"| Lessons written | {len(written)} |")
    add(f"| Lessons with valid frontmatter | {len(substantive)} |")
    add(f"| Exercise/solution companions written | {cov['companions_present']} / "
        f"{cov['companions_planned']} |")
    add(f"| Completion | {pct:.1f}% |")
    add("")
    add("> Companion files are the conventional `exercises/<lesson>-exercises.md` and "
        "`<lesson>-solutions.md` pairs. Lessons in `00-orientation` and "
        "`26-reference-library` are process material and reference pages, so they "
        "carry no companions by design.\n")

    add("## The six learning stages\n")
    add("| Stage | Entry requirement | Mastery checkpoint |")
    add("|---|---|---|")
    for _key, name, entry, checkpoint in plan.STAGES:
        add(f"| **{name}** | {entry} | {checkpoint} |")
    add("")

    add("## Contents\n")
    for folder in plan.PLAN:
        folder_ref = folder["reference"]
        folder_written = (REPO_ROOT / folder_ref).exists()
        mark = "x" if folder_written else " "
        add(f"- [{mark}] [{folder['title']}](./{folder_ref}) — "
            f"`{folder['slug']}` · stages: {folder['stage']}")

    add("\n---\n")

    for folder in plan.PLAN:
        lesson_paths = [lesson["path"] for module in folder["modules"] for lesson in module["lessons"]]
        done = sum(1 for path in lesson_paths if (REPO_ROOT / path).exists())
        total = len(lesson_paths)
        add(f"## {folder['title']}\n")
        add(f"`{folder['slug']}` — **{len(folder['modules'])} modules**, "
            f"**{done}/{total} lessons written**\n")
        add(f"[Folder index](./{folder['reference']})\n")

        for module in folder["modules"]:
            module_written = (REPO_ROOT / module["path"]).exists()
            module_done = sum(1 for lesson in module["lessons"]
                              if (REPO_ROOT / lesson["path"]).exists())
            module_total = len(module["lessons"])
            flag = "x" if module_written else " "
            add(f"### [{flag}] {module['title']} "
                f"({module_done}/{module_total})\n")
            add(f"Module index: [`{module['dir']}/README.md`](./{module['path']})\n")
            add("| | Lesson | Level |")
            add("|---|---|---|")
            for lesson in module["lessons"]:
                mark = "✓" if (REPO_ROOT / lesson["path"]).exists() else "·"
                add(f"| {mark} | [{lesson['title']}](./{lesson['path']}) | "
                    f"{LEVEL_BADGE[lesson['level']]} |")
            add("")

    add("---\n")
    add("## How to use this index\n")
    add("1. Pick a stage from the table above and read the matching "
        "[study roadmap](./00-orientation/01-study-roadmap/README.md).")
    add("2. Follow the [dependency graph](./00-orientation/02-curriculum-map/README.md) "
        "rather than the numbering alone.")
    add("3. After finishing any lesson, complete its exercises and tick the mastery "
        "checkpoint in the roadmap.")
    add("")

    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="exit non-zero if the generated file would change")
    args = parser.parse_args(argv)

    content = render()
    if args.check:
        existing = OUTPUT.read_text(encoding="utf-8") if OUTPUT.exists() else ""
        if existing != content:
            print("CURRICULUM.md is out of date. Run: python3 tools/build_index.py")
            return 1
        print("CURRICULUM.md is up to date.")
        return 0

    OUTPUT.write_text(content, encoding="utf-8")
    counts = plan.summary()
    written = sum(1 for lesson in plan.all_lessons()
                  if (REPO_ROOT / lesson["path"]).exists())
    print(f"Wrote {OUTPUT.relative_to(REPO_ROOT)}: "
          f"{written}/{counts['lessons']} lessons present.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
