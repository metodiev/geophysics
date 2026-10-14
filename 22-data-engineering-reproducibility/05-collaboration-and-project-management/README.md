# Module 22-05 — Collaboration and Project Management

**Stages:** intermediate → graduate · **Prerequisites:** modules 22-01 and 22-02 (or
equivalent familiarity with version control, environments and data versioning).

This module is about the human infrastructure that makes reproducible work possible: how a
project is laid out, how its work is tracked, how a manuscript is written by several people,
what a data management plan commits to, and what it means to release results openly. The
organising idea is that **collaboration decisions are measurable**, and that measuring them
converts arguments about practice into arithmetic. A project's paths break on a move in
48 % of the demonstration's scripts; four authors editing prose conflict with probability
0.846 at ten lines of separation under one formatting convention and 0.066 under another;
a research queue with 24 items in progress implies a 20-day wait at an arrival rate of 1.2
per working day; a ten-year retention horizon multiplies a five-year project's storage by
three.

The second thread is that **the artefacts are the interface**. A directory structure, an
issue's definition of done, a manuscript repository, a data management plan and an access
licence are all things another person reads and acts on. Each lesson therefore pairs a
practice with the artefact it produces and the check that keeps it true: a portability test
in CI, a block-reason vocabulary in the tracker, one sentence per line in the manuscript,
an identifier and landing page for the data, a named maintainer for a release.

The third thread is honesty about evidence. Several claims in this module are widely made
and weakly supported — that open data increases citations, that a work-in-progress limit
increases productivity, that a formatting convention is a matter of taste. The lessons
state which numbers are model outputs, which are conventions, and which require evidence
the group should collect itself; where a claim depends on a contested effect, the lesson
says what to measure instead.

All measurements in this module are **SYNTHETIC** with chosen parameters: project trees,
issue queues, manuscript line counts, storage forecasts and adoption curves are generated
by the demonstrations. No real repository, tracker, manuscript, plan or bibliometric
database was inspected, and no funder policy or measured effect of open practice is quoted.

## Learning objectives

By the end of this module you will be able to:

1. Lay out a project so that code, data, outputs and configuration are separated, and
   measure its portability with a move-and-run test.
2. Track work as a queue: apply Little's law, report cycle-time percentiles, and state what
   a WIP limit can and cannot change.
3. Run a collaborative manuscript repository with a formatting convention chosen for its
   merge behaviour, and make every figure regenerable.
4. Write a data management plan whose commitments have artefacts and numbers, with the
   storage and risk arithmetic attached.
5. Choose an access level per dataset and release artefacts in community formats, with the
   cost and the maintenance commitment budgeted.
6. Diagnose the collaboration failures of a project — broken paths, invisible queues,
   unreproducible figures, unaffordable retention, unreusable releases — from measurements.

## Prerequisites

- [22-05-01 Project Directory Structure and Conventions](01-project-structure.md) is the
  entry point; the later lessons assume its four-region vocabulary.
- [22-01-02 Version Control with Git](../01-research-software-engineering/02-version-control-git.md) —
  the merge machinery the writing lesson applies to prose.
- [22-02-05 Data Versioning and Provenance Tracking](../02-reproducible-workflows/05-data-versioning.md) —
  the identifiers that plans and releases commit to.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Project Directory Structure and Conventions](01-project-structure.md) | intermediate | 29 of 60 scripts break when a project moves; a five-item portability score reads 0.570 and ranks the fixes |
| 02 | [Issue Tracking, Milestones and Kanban for Research](02-issue-tracking.md) | intermediate | Little's law: WIP 24 implies a 20-day wait; the median cycle time is 8.9 days against a 36.4-day 90th percentile |
| 03 | [Collaborative Writing with LaTeX and Markdown](03-collaborative-writing.md) | advanced | 667 wrapped lines against 444 sentence-per-line lines; conflict probability 0.846 against 0.066 at ten lines |
| 04 | [Research Data Management Plans and FAIR Principles](04-research-data-management-plan.md) | advanced | 62.5 TB becomes 187.5 TB with ten-year retention; three copies cut loss risk from 0.02000 to 0.00001 |
| 05 | [Open Science Practice in the Geosciences](05-open-science-practice.md) | graduate | Adoption moves 14.8 % → 80.2 % between years 0 and 9; one release costs about 109 hours, maintenance included |

## Suggested path

**If you are starting a project:** read 01 for the tree and 04 for the plan; those two
decide what the project will be able to show at the end. Add 02 when the first queue
appears.

**If you are writing a paper with others:** read 03, then 01 §6 (conventions worth writing
down) and 05 §7 (the practice list). The manuscript repository is where all of it
converges.

**If you lead a group or supervise students:** read 02 in full — it is the queueing
arithmetic behind supervision — then 05 §6 on access levels.

**If you are preparing a proposal:** read 04 and 05 together; the plan's commitments and
the release's costs are the two sections that proposals usually under-cost.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-project-structure.md`](01-project-structure.md) | Lesson 01 |
| [`02-issue-tracking.md`](02-issue-tracking.md) | Lesson 02 |
| [`03-collaborative-writing.md`](03-collaborative-writing.md) | Lesson 03 |
| [`04-research-data-management-plan.md`](04-research-data-management-plan.md) | Lesson 04 |
| [`05-open-science-practice.md`](05-open-science-practice.md) | Lesson 05 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Five runnable demonstrations |

| Script | What it measures |
|---|---|
| [`code/project_structure_demo.py`](code/project_structure_demo.py) | Reference kinds, breakage on a move, layout comparison, portability score |
| [`code/issue_tracking_demo.py`](code/issue_tracking_demo.py) | Little's law, cycle-time percentiles, lead time versus WIP, backlog growth |
| [`code/collaborative_writing_demo.py`](code/collaborative_writing_demo.py) | Line counts and diff ratios, conflict probability by convention and separation, multi-editor probability |
| [`code/research_data_management_plan_demo.py`](code/research_data_management_plan_demo.py) | Storage forecast at two horizons, FAIR readiness, loss risk versus copies, cost of each phase |
| [`code/open_science_practice_demo.py`](code/open_science_practice_demo.py) | Logistic adoption, reuse totals, citation accrual with a stated multiplier, release effort |

## How to run the demos

```bash
cd 22-data-engineering-reproducibility/05-collaboration-and-project-management/code

/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python project_structure_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python issue_tracking_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python collaborative_writing_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python research_data_management_plan_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python open_science_practice_demo.py
```

Every demo prints labelled results with units, seeds its random numbers with
`np.random.default_rng(20261014)`, uses no network access, writes no files and exits 0.
Each runs in well under a second.

## Mastery checkpoint

Complete this without notes, using the demonstrations only to check arithmetic:

> A group of six (four students, one postdoc, one PI) is writing a paper from a two-year
> field campaign, with an instrument archive to be retained for ten years.
> **(a)** Their repository has 50 scripts, 20 of which use absolute paths and 15 are
> working-directory dependent; compute the breakage on a move and name the fix.
> **(b)** Their tracker receives 12 issues a week with a capacity of 15; compute the wait
> implied by ten items in progress and state the percentile they should report.
> **(c)** Their manuscript is 10 000 words; compute the line counts under hard-wrapped
> paragraphs and sentence-per-line, and state which convention reduces conflict.
> **(d)** The archive is 15 TB/year raw for two years plus 5 TB of derived products;
> compute the project total with a ten-year retention and state the multiplier.
> **(e)** State the copies and failure domains you would require, and the test that proves
> they work.
> **(f)** State the artefacts the paper's data availability statement should name, and the
> access level of each.

Worked versions of (a)–(f) appear in the lesson solutions at ★★ and ★★★ level.

## Common pitfalls across this module

1. **Working-directory dependence.** It breaks on a move and hides inside "it works for
   me"; the portability test is free.
2. **Reporting averages in a queue.** Cycle times are heavy-tailed: the demonstration's mean
   is 1.8× its median and its 90th percentile is 12× it.
3. **Reformatting with a content change.** The diff hides the science, and the merge
   geometry makes it worse.
4. **A plan without numbers.** Retention, volume, cost and responsibility are the items a
   reviewer can check; prose is not.
5. **Treating a second copy as a backup.** Independence means a different failure domain,
   and only a restore test proves it.
6. **Releasing without a maintainer.** The link rots, the metadata drifts, and the
   commitment outlives the project.

## Related modules

- [22-01 Research Software Engineering](../01-research-software-engineering/README.md) —
  the code-level conventions these practices frame.
- [22-02 Reproducible Research Workflows](../02-reproducible-workflows/README.md) —
  the environments and versioning that plans and releases depend on.
- [24-06 Reproducible Publication](../../24-research-papers-writing/06-reproducible-publication/README.md) —
  where the manuscript, the data statement and the release meet.
- [21-09 Ethical and Responsible Analytics](../../21-statistics-bayesian-ml/09-ethical-and-responsible-analytics/README.md) —
  the governance questions that decide what may be shared.
