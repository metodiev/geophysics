# Module 24-01 — Reading the Research Literature

**Stages:** intermediate → doctoral · **Prerequisites:** none inside this folder;
[00-01-03 Self-Assessment](../../00-orientation/01-study-roadmap/03-self-assessment.md)
and [02-01-02 Measurement Uncertainty](../../02-physics/01-measurement-and-physical-reasoning/02-measurement-uncertainty.md)
are the two habits this module assumes.

This module is about the half of research that happens before you write anything:
finding the papers that matter, reading them at the right depth, and judging them
without either credulity or cynicism. Its organising idea is that **reading is a
measurement problem**. A triage rule has a precision and a recall; a query has a
recall and an hour cost; a literal reading of a paper is a claim about the state
of the literature that can be wrong in two directions. Once reading is described
that way, the choices become arithmetic instead of taste.

The module's five lessons move from the object (what a paper is made of) to the
instruments (how to screen, search and monitor). Lesson 01 measures the shape of
the IMRaD argument — sections, word budgets, citation placement, the hourglass —
so that a reader knows which sentence can be checked where. Lessons 02 and 03
separate the cheap passes from the expensive ones: a skim produces a label, a map
produces a structure, a deep read produces a reproduction, and a critique
separates reproducibility from data adequacy from inferential validity. Lessons
04 and 05 treat the corpus itself as a filtering problem, with a documented
protocol for the one-off search and a budget for the continual stream.

All models, corpora and measurements in this module are **SYNTHETIC**. Each
demonstration generates its own corpus from a seeded random generator with chosen
teaching parameters; no published paper was measured, no database was queried and
no bibliometric figure is quoted from a real survey. Where a number describes a
plausible literature rather than a specific one, the lesson says so. The one
external convention used — journal-partitioned IMRaD structure and the
Introduction's "niche" move — is attributed to its published source in the text
and is not reproduced here.

## Learning objectives

By the end of this module you will be able to:

1. **Name** the functional blocks of a research paper and **state** what each one
   licenses, distinguishing what a section can support from what it may assert.
2. **Measure** a paper's sectional word budget and reference density and
   **compare** it with the synthetic corpus distribution.
3. **Run** the four reading passes — skim, map, deep-read, critique — and
   **state** the output and cost of each.
4. **Compute** precision, recall, $F_1$ and the number needed to screen for a
   triage rule or a search query, and **interpret** each in working hours.
5. **Audit** a paper's reporting against a checklist, **compute** joint compliance
   and **explain** why it is governed by the weakest required item.
6. **Design** and **document** a systematic search protocol, including its yield
   accounting and its de-duplication threshold with both error rates.
7. **Model** an alert stream as volume, filter and cap, and **quantify** the
   relevant items that attention limits forgo.
8. **Write** a critique that names the axis that failed, the evidence, the
   consequence, the test and the reviewer's own uncertainty.

## Prerequisites

- [00-01-03 Self-Assessment and Reflection](../../00-orientation/01-study-roadmap/03-self-assessment.md) —
  the practice of stating what you know with what confidence.
- [00-01-04 Effective Study Habits](../../00-orientation/01-study-roadmap/04-study-habits.md) —
  the attention budget this module allocates.
- [00-03-01 Navigating This Repository](../../00-orientation/03-how-to-use-this-repo/01-navigation.md) —
  how the curriculum's collections are addressed.
- [02-01-02 Measurement Uncertainty](../../02-physics/01-measurement-and-physical-reasoning/02-measurement-uncertainty.md) —
  what an error bar asserts, needed for the critique lesson.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Anatomy of a Research Paper](01-anatomy-of-a-paper.md) | intermediate | The hourglass argument; $20.1/29.6/24.1/26.2\%$ sectional budget; $69.5\%$ of citations in $46.5\%$ of words |
| 02 | [Reading Strategies: Skim, Map, Deep-Read, Critique](02-reading-strategies.md) | intermediate | Four passes, four outputs; two-pass reading recovers $67\%$ of the content in $42\%$ of the time |
| 03 | [Critiquing Methods, Data and Inference](03-critiquing-methods.md) | doctoral | Three axes; joint compliance $10.7\%$ against a $13.1\%$ independence prediction; $65\%$ of modelled defects leave no textual trace |
| 04 | [Systematic Literature Search and Reference Management](04-literature-search.md) | intermediate | A broad keyword finds $55\%$ of the corpus at $9.2\%$ precision; a Boolean AND finds $16.7\%$ at $37.0\%$ |
| 05 | [Keeping Up: Journals, Preprints, Societies, Alerts](05-keeping-up-with-literature.md) | intermediate | Six sources = $34.9\ \mathrm{h/week}$; filtering buys $11\times$ for a $21\%$ miss rate; the cap binds |

## Suggested path

**If you are starting a literature review:** 01 → 04 → 02, then run the search
protocol on your own topic before touching a reference manager.

**If you are already reading a lot and feel behind:** 02 and 05, in that order.
The budget arithmetic in 05 explains why "reading more" is not a plan, and the
pass structure in 02 tells you what to read at which depth.

**If you are preparing to review manuscripts:** 01, then 03, then the review
practice in
[24-03-05 Peer Review Practice](../03-research-methods-and-rigour/05-peer-review-practice.md).
The three-axis separation in 03 is what turns a referee report from opinion into
evidence.

**If you are supervising students:** 02 §5 (the reading log) and 05 §5 (the policy
sentence) are the two artefacts worth requiring; both are short and both are
checkable.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-anatomy-of-a-paper.md`](01-anatomy-of-a-paper.md) | Lesson 01 |
| [`02-reading-strategies.md`](02-reading-strategies.md) | Lesson 02 |
| [`03-critiquing-methods.md`](03-critiquing-methods.md) | Lesson 03 |
| [`04-literature-search.md`](04-literature-search.md) | Lesson 04 |
| [`05-keeping-up-with-literature.md`](05-keeping-up-with-literature.md) | Lesson 05 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Five runnable demonstrations |

| Script | What it measures |
|---|---|
| [`code/anatomy_of_a_paper_demo.py`](code/anatomy_of_a_paper_demo.py) | Manuscript length, reference density, sectional budget, citation placement, hourglass widening |
| [`code/reading_strategies_demo.py`](code/reading_strategies_demo.py) | Triage confusion matrix, screening cost, three reading strategies, information yield per hour |
| [`code/critiquing_methods_demo.py`](code/critiquing_methods_demo.py) | Per-item reporting audit, joint compliance, weighted score, defect detectability |
| [`code/literature_search_demo.py`](code/literature_search_demo.py) | Precision/recall/F1 for five queries, union and intersection cost, de-duplication thresholds |
| [`code/keeping_up_demo.py`](code/keeping_up_demo.py) | Alert volume, filter performance, the cap model, annual budget and marginal cost |

## How to run the demos

```bash
cd 24-research-papers-writing/01-reading-research-literature/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python anatomy_of_a_paper_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python reading_strategies_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python critiquing_methods_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python literature_search_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python keeping_up_demo.py
```

Each script prints labelled sections, quotes no external data, needs no network and
finishes in well under a second.

## Mastery checkpoint

1. Take one paper, measure its sectional shares and reference densities, and state
   which sections you would have to read to check its central number.
2. State a triage rule of your own with its sensitivity and specificity, estimated
   from a labelled sample of at least $40$ records.
3. Audit three papers with a six-item checklist and report joint compliance.
4. Write a search protocol with a yield line, and estimate the screening hours.
5. Write your alert policy in the one-sentence form of lesson 05 §5.

## Common pitfalls across this module

1. **Treating reading volume as progress.** Skims are labels, not knowledge.
2. **Collapsing the three critique axes.** A reproducible paper can be wrong; a
   correct one can be irreproducible.
3. **Reporting mean compliance without its dispersion.** The tail is the finding.
4. **Chasing recall without a screening budget.** A union query is $38.6\
   \mathrm{h}$ of work in the demonstration, and that is the cheap case.
5. **De-duplicating by hand.** It is inconsistent, untraceable and it hides its own
   error rate.
6. **Assuming a filter is lossless.** Every filter has a recall, and an unmeasured
   one is usually worse than assumed.
7. **Quoting synthetic proportions as field norms.** Nothing in this module is a
   measurement of a real literature.

## Related modules

- [24-02 Scientific Writing](../02-scientific-writing/README.md) — the same
  anatomy from the writer's side.
- [24-03 Research Methods and Scientific Rigour](../03-research-methods-and-rigour/README.md) —
  what the critique lesson's axes become when you design your own study.
- [24-06 Reproducible Publication and Open Data](../06-reproducible-publication/README.md) —
  making the artefacts a reader needs actually available.
- [22-02 Reproducible Research Workflows](../../22-data-engineering-reproducibility/02-reproducible-workflows/README.md) —
  the tooling behind reproducible reading.
- [26-04 Textbook Bibliography](../../26-reference-library/04-textbook-bibliography/README.md) —
  where the works this module teaches you to read are catalogued.
