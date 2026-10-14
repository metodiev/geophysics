# Module 00-03 — How to Use This Repository

**Stage:** beginner → intermediate · **Prerequisites:** [00-02 curriculum map](../02-curriculum-map/README.md)

This module is the **operator's manual**. It covers where files live and how they
are named, how to install the scientific stack without breaking reproducibility,
how the automated quality gate works and what it does not check, and the batch
workflow used to add lessons and projects.

You can start reading lessons before finishing this module — the gate needs
nothing installed — but you will save time by at least skimming
[environment setup](./02-environment-setup.md) before your first Python lesson.

## Learning objectives

By the end of this module you will be able to:

1. Navigate from a folder to a lesson to its frontmatter, and decode a lesson
   `id` in either direction.
2. Create and verify an isolated Python environment containing only the tiers of
   `requirements.txt` your chosen track needs.
3. Run `check_all.py`, `build_index.py` and `verify_links.py`, interpret their
   output, and repair each class of failure they report.
4. Add a lesson or a project using the plan → write → validate contract, and
   review it with a checklist that separates mechanical from scientific checks.

## Lessons

| # | Lesson | Level |
|---|---|---|
| 01 | [Repository Navigation and File Naming Conventions](./01-navigation.md) | beginner |
| 02 | [Setting Up the Python Environment and Tooling](./02-environment-setup.md) | beginner |
| 03 | [Running the Link, Formula and Duplication Checks](./03-quality-gate.md) | intermediate |
| 04 | [Batch Workflow for Adding Lessons and Projects](./04-contribution-workflow.md) | intermediate |

## The three commands worth memorising

```bash
python3 tools/check_all.py       # structure, relative links, LaTeX, duplicates
python3 tools/build_index.py     # regenerate CURRICULUM.md from the plan and disk
python3 tools/verify_links.py    # audit cited URLs against tools/verified_links.tsv
```

All three run on the Python standard library alone. Nothing needs to be installed
to validate the repository, which is what allows the quality gate to run in any
environment, including continuous integration.

## Honesty rules that the tooling enforces

- **Every external URL is registered** in `tools/verified_links.tsv` with an
  observed HTTP status. `verify_links.py` fails the audit if a cited URL is not
  registered, so an invented link cannot survive.
- **Every relative link resolves**, or points at a path the plan declares.
- **Every lesson's `id`, `title` and `level` match the plan** character for
  character.
- **Datasets carry a provenance label** — `SYNTHETIC`, `OBSERVED` or
  `ILLUSTRATIVE` — so a reader knows what weight the numbers can carry.

No tool can enforce the deeper rule, which is stated in the root
[README](../../README.md): where a fact could not be verified, the text says so
rather than guessing.

## Mastery checkpoint

You have completed this module when you can, unaided:

- [ ] Clone the repository, run the quality gate on a bare interpreter, and
      explain what each of the four checks verifies.
- [ ] Create a virtual environment, install `requirements.txt`, and demonstrate
      that a lesson's Python code runs inside it.
- [ ] Add a lesson: declare it in `tools/curriculum_plan.py`, create the file with
      matching frontmatter, pass `check_all.py`, and regenerate `CURRICULUM.md`.
- [ ] State three things the quality gate does not check, and how you would catch
      each of them.

## Related modules

- [02-curriculum-map](../02-curriculum-map/README.md) — what to study, once you
  know how the repository works.
- [04-orientation-geophysics](../04-orientation-geophysics/README.md) — the
  subject itself, if you have not yet met it.
- [22-data-engineering-reproducibility](../../22-data-engineering-reproducibility/README.md) —
  where the environment and workflow habits here are developed into
  research-grade practice.
