---
id: 22-05-01
title: "Project Directory Structure and Conventions"
level: intermediate
prereqs: ["22-02-02", "22-01-01"]
estimated_minutes: 45
tags: [project-structure, conventions, portability, collaboration]
---

# Project Directory Structure and Conventions

## Learning objectives

By the end of this lesson you will be able to:

1. **Distinguish** code, data, outputs and configuration in a project tree, and
   **state** the failure each boundary prevents.
2. **Measure** a project's path portability, and **identify** the references that
   break when it moves.
3. **Choose** between a flat and a package layout, and **state** the import and
   testing consequences of each.
4. **Compute** a portability score from checks a reviewer can run, and **name** the
   two changes that raise it most.
5. **Write** the conventions a newcomer needs — entry points, naming, data
   locations, output locations — where they will be read.
6. **Diagnose** the four structural failures: a path that breaks on a move, an
   output written into the source tree, a configuration buried in code, and a
   checkout that shadows an installed library.

The project tree and the reference counts in this lesson are **SYNTHETIC** with
chosen proportions; no real repository was inspected. The categories, the arithmetic
and the checks are the transferable part.

## Prerequisites

- [22-02-02 Pinning Environments and Managing Dependencies](../02-reproducible-workflows/02-environment-pinning.md) —
  the dependency side of a portable project.
- [22-01-01 Designing Software for Scientific Research](../01-research-software-engineering/01-software-design-science.md) —
  why a change reaches further than the file it touches.

## 1. Intuition: the tree is an interface

A project's directory structure is the first thing a newcomer reads and the last
thing anyone documents. It answers four questions before any code runs: where the
code is, where the data are, where the outputs go, and what to run first. When those
answers are implicit, every reader reconstructs them from the scripts, and every
assumption of the original author — a personal directory, a working directory, a
filename with `FINAL` in it — becomes a defect that appears only when someone else
tries.

The organising rule is that **the tree should make the wrong thing hard**. Data are
read-only and live in one place; outputs are written and never read by hand;
configuration is a file; and code is one importable unit. Each boundary removes a
class of accidents.

## 2. The four regions

| Region | Contents | Rule | Accident it prevents |
|---|---|---|---|
| `src/` or the package | importable code | installed or importable, no I/O at import time | a script importing by working directory |
| `data/` (or an identifier) | inputs, read-only | never written by the project; versioned by identifier | an analysis that depends on a locally patched input |
| `results/`, `figures/` | outputs | regenerable, never edited by hand | a figure that cannot be reproduced |
| `config/` | parameters and paths | the only place paths appear | a constant edited in five scripts |

The demonstration's **SYNTHETIC** project has 60 scripts, 40 data files and 8
documented entry points. That ratio is the point: most files are internals, a
handful are interfaces, and the README's job is to name the handful.

## 3. Path portability: the cheapest test

Path references divide into four kinds, and two of them survive a move:

| Reference kind | Scripts (of 60) | Breaks if the project moves? |
|---|---|---|
| absolute (`/home/…/data.csv`) | 9 | yes |
| relative to the project root | 27 | no |
| depends on the working directory (`data.csv`) | 20 | yes |
| read from a configuration file | 4 | no |

**29 of 60 scripts (48 %)** break when the project is moved, and moving a project is
the cheapest portability test in existence: copy the tree to a different path, run
the documented entry point, and observe. The two failing kinds have different
remedies — absolute paths become a configured root, and working-directory dependence
becomes an explicit import or path — but the diagnostic is the same, and it is free.

The deeper reason to prefer "paths appear in one place" is not portability alone: a
path is a **parameter**, and parameters belong where a reader can see and change
them. A path hard-coded in a script is a parameter hidden in an implementation.

## 4. Flat tree or package

A flat tree puts every module in one directory; a package layout puts the code under
a single importable package (conventionally `src/<package>/`) with an installed
distribution.

| Property | Flat tree | Package layout |
|---|---|---|
| Import resolution | depends on the working directory | one root, fixed at install |
| Tests | may import the checkout by accident | import the installed package |
| Name collisions with installed libraries | possible by file name | confined to the package namespace |
| Entry points | discovered by reading the tree | declared in the distribution metadata |
| Cost | none | one extra directory and a packaging file |

The demonstration's 24 modules in a flat layout carry a modelled collision risk of one
name; the number is a teaching value, but the mechanism is real: a file called
`types.py` or `random.py` in the working directory shadows the standard library for
every script in it, and the resulting error is confusing precisely because the file
looks harmless.

## 5. A portability score with checkable items

A score is useful only if each item maps to a check someone can run. The
demonstration uses five:

| Check | Coverage |
|---|---|
| paths are relative to the project root | 45 % |
| data and outputs are separate from code | 80 % |
| a package layout with one import root | 100 % |
| configuration is a file, not a constant | 10 % |
| the README names the entry points | 50 % |

Mean coverage: **0.570**. The two changes that raise it most are the two weakest
items — move the constants into a configuration file, and make paths relative or
configured. That ordering is the value of scoring: it converts "we should tidy the
project" into a ranked list of two tasks with a measurable effect.

## 6. Conventions worth writing down

1. **One README, one entry point.** State the command that produces the main result;
   a newcomer should not have to read the tree.
2. **Data by identifier, not by path.** The project points at a dataset version, not
   at `data/catalogue_v2_FINAL.csv`
   ([22-02-05](../02-reproducible-workflows/05-data-versioning.md)).
3. **Outputs never enter the source tree, and are never committed** unless they are
   regression fixtures, which live in a named test directory.
4. **Names describe roles**: `prepare_catalogue.py`, `invert_1d.py`, not
   `script1.py`, `test2_final.py`, `new_new.py`.
5. **The convention is enforced by a check**, not by a paragraph: a path check in
   continuous integration catches the regression that documentation cannot.
6. **One project, one purpose.** A directory that holds three projects has no
   structure; separate them.

## 7. Worked example: adopting a project whose author left

A group inherits a project with 60 scripts in one directory, data in two personal
directories, outputs mixed with sources, and a README that is a chronology of the
research.

1. **Run the portability test.** Copy the tree elsewhere, try the documented entry
   point. In the demonstration's proportions, expect about half the scripts to fail
   (9 absolute and 20 working-directory references of 60).
2. **Establish the four regions first.** Move inputs to a data area referenced by
   identifier, outputs to a results area, parameters to a configuration file. The
   scripts then fail in a *diagnosable* way — a missing configuration key rather
   than a wrong number.
3. **Make the code importable.** Move the modules into a package and add the
   packaging file, so tests import the installed code and the results no longer
   depend on where the shell was.
4. **Name the entry points.** Two or three, documented in the README, with the
   others marked as internal. The 8 documented entry points of the demonstration's
   model is a plausible target; every one of them should be runnable from a clean
   checkout.
5. **Add the check.** A CI job that runs the portability test and the entry points on
   a fresh clone. That is the step that keeps the structure from decaying, because
   structural decay is a regression like any other.

## Assumptions and regime of validity

1. **Chosen proportions.** The 9/27/20/4 split of reference kinds and the coverage
   percentages are teaching values; the categories and the arithmetic are what
   generalise.
2. **A single-project repository.** Monorepos, notebooks-only projects and
   collaborative writing repositories have different structures; the four regions
   apply, the packaging advice may not.
3. **A file-based data store.** Projects whose data live in a database or an object
   store replace the `data/` region with an identifier and a fetch step, and the
   region's rule (read-only, versioned) is unchanged.
4. **A score is not a measure of quality.** It measures convention coverage; a
   project can score 1.0 and be scientifically wrong.
5. **Conventions need enforcement.** A documented convention without a check decays;
   the lesson's recommendation is to encode each rule as a check, which is possible
   for every item in §5 except the README's quality.

## The honest summary

A project's tree is its first interface, and the failures it prevents are specific:
paths that break on a move (48 % of the demonstration's scripts), outputs mixed with
sources, configuration buried in code, and name collisions from a flat layout. The
measurements are cheap — move the project and run the entry point — and the fixes are
ranked by scoring five checkable items, where the weakest two (configuration in a
file, paths relative or configured) are also the cheapest to change. The structure
worth writing down is four regions — code, data, outputs, configuration — plus one
documented entry point per result and a CI check that keeps all of it true.

## Python demonstration

[`code/project_structure_demo.py`](./code/project_structure_demo.py) prints, with
`np.random.default_rng(20261014)`:

1. a synthetic flat tree and its missing boundaries;
2. the reference-kind table and the 29 of 60 (48 %) that break on a move;
3. the flat-versus-package comparison and the collision mechanism;
4. the five-item portability score (0.570) and the two changes that raise it most.

```bash
cd 22-data-engineering-reproducibility/05-collaboration-and-project-management/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python project_structure_demo.py
```

## Exercises

Graded problems and worked solutions are in
[`exercises/01-project-structure-exercises.md`](./exercises/01-project-structure-exercises.md)
and
[`exercises/01-project-structure-solutions.md`](./exercises/01-project-structure-solutions.md).

## Mastery checkpoint

Without notes: a project has 40 scripts, of which 12 use absolute paths, 18 are
working-directory dependent, 8 use root-relative paths and 2 read a configuration
file.

1. Compute the fraction of scripts that break when the project moves.
2. State the remedy for each failing kind, and which one requires a code change.
3. State the four regions and one rule for each.
4. Name the two items of the portability score you would fix first for this project
   and why.

## Common pitfalls

1. **Working-directory dependence.** The most common failure and the hardest to see,
   because the script works when run from the directory it was written in.
2. **Data inside the source tree.** It mixes read-only inputs with regenerable
   outputs, and one `rm -r` becomes irreversible.
3. **Constants in code.** A parameter hidden in an implementation is a change nobody
   can find later.
4. **A flat tree with common names.** `types.py` or `random.py` silently shadows a
   library.
5. **Conventions in prose only.** Structural decay is a regression; it needs a check.
6. **Six entry points that are "documented" but not runnable from a clean clone.**
   The portability test is what makes the claim true.

## Where this is used

- **Handing a project to a student** — the tree and the README are the onboarding.
- **Publishing an artefact** — a reviewer's first action is to clone and run, and the
  structure decides whether that succeeds:
  see [24-06 Reproducible Publication](../../24-research-papers-writing/06-reproducible-publication/README.md).
- **Long-lived codes** — the boundaries are what allow a component to be replaced
  ([22-01-01](../01-research-software-engineering/01-software-design-science.md) §6).
- **Data management planning** — the storage regions a plan describes are the
  project's directories: see
  [22-05-04 Research Data Management Plans and FAIR Principles](04-research-data-management-plan.md).

## Related lessons

- [22-05-02 Issue Tracking, Milestones and Kanban for Research](02-issue-tracking.md) —
  the work that the structure must accommodate.
- [22-01-04 Documentation, Docstrings and READMEs That Work](../01-research-software-engineering/04-documentation.md) —
  where the conventions are written.
- [22-02-02 Pinning Environments and Managing Dependencies](../02-reproducible-workflows/02-environment-pinning.md) —
  the environment side of portability.
- [22-03-03 Designing Robust Data Pipelines for Earth Data](../03-data-formats-and-engineering/03-data-pipelines.md) —
  the pipeline that reads the data region and writes the results region.

## Self-assessment checklist

- [ ] I can name the four regions and the accident each prevents.
- [ ] I can measure the fraction of path references that break on a move.
- [ ] I can choose flat or package layout with a stated reason.
- [ ] I can score five checkable structural items.
- [ ] I can write the conventions a newcomer needs.
- [ ] I can diagnose the four structural failures.
