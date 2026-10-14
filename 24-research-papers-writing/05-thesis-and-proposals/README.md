# Module 24-05 — Theses, Proposals and Career Documents

**Stages:** advanced → research · **Prerequisites:** modules
[24-02](../02-scientific-writing/README.md),
[24-03](../03-research-methods-and-rigour/README.md) and, for the proposal lesson,
[24-04](../04-presentation-and-communication/README.md).

This module covers the documents that are not papers: the proposal that asks for
money, the thesis that delivers it, the funding arithmetic that decides, and the CV
and research statement that carry a career forward. Each is scored against a scheme,
and each lesson therefore starts from the scheme rather than from the prose. What
emerges is a consistent picture: weights are the specification, the decision boundary
is noisy, and the two actions with the largest measured returns are clearing the
boundary rather than topping the ranking, and revising rather than rewriting.

The organising thread is **traceability between promise and evidence**. A proposal
promises; a thesis must show that each claimed contribution is supported by words
somewhere and is not merely a chapter result; a funding record is evidence about
feasibility; a CV summarises a distribution that a single index conceals. The module's
lessons each build one link in that chain, and each measures the link's strength: the
score margin at a funding line, the fraction of a thesis that repeats itself, the band
of panel decisions that are closer to a coin toss than to a judgement, and the
insensitivity of the h-index to the work that identifies a researcher.

All numbers in this module are **SYNTHETIC**, produced by seeded demonstrations with
chosen parameters. No proposal, panel, thesis, publication record or hiring process
was measured or queried. Where a lesson refers to a published convention — page and
word norms, funding-rate arithmetic, citation-based indices — it does so as a stated
definition and states plainly which parts are teaching values.

## Learning objectives

By the end of this module you will be able to:

1. **Read** a scoring scheme and **compute** the weighted score and the marginal value
   of a point on each criterion.
2. **Measure** the margin at a funding line and **compare** it with the shift produced
   by a change of weighting.
3. **Allocate** chapter budgets against a page limit and **remove** redundancy by
   reference rather than by deletion.
4. **Test** each claimed contribution for supporting words and **narrow** the claims
   that fail.
5. **Compute** a panel-mean standard error, the uncertain band around a boundary, and
   the cost of halving it.
6. **Compute** expected submissions per award and **justify** revision and triage from
   it.
7. **Summarise** a publication record with a distribution rather than an index, and
   **demonstrate** what the index ignores.
8. **Map** evidence to a hiring rubric and **write** a research statement whose future
   is proportionate to its past.

## Prerequisites

- [24-03-01 Formulating Answerable Research Questions](../03-research-methods-and-rigour/01-research-questions.md) —
  the question every proposal promises.
- [24-03-03 Designing Observational, Experimental and Modelling Studies](../03-research-methods-and-rigour/03-study-design.md) —
  the design that makes a plan credible.
- [24-02-02 Paper Structure: IMRaD and Its Variants](../02-scientific-writing/02-paper-structure.md) —
  the argument structure a thesis chapter inherits.
- [24-04-03 Seminars, Qualifying Exams and Thesis Defence](../04-presentation-and-communication/03-seminar-and-defence.md) —
  the examination the thesis leads to.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Writing a Compelling Research Proposal](01-research-proposal.md) | doctoral | The scheme shift is $5.19\times$ the margin at the line; a point on feasibility is worth $2.5$ points on team |
| 02 | [Thesis Structure, Chapters and the Contribution Statement](02-thesis-structure.md) | research | $12$ pages over the limit; $14.6\%$ redundancy is the cheapest cut; two of six claims are really chapter results |
| 03 | [Understanding Grant Funding and Review Criteria](03-grant-funding.md) | research | $\pm 0.26$-point band holds $21.8\%$ of applications; $5.0$ submissions per award; $100$ person-days per funded project |
| 04 | [Academic CVs, Research Statements and Career Paths](04-cv-and-career.md) | advanced | Mean/median citations $2.18$; Gini $0.562$; $h$ unchanged by the peak; a rubric change moves $7$ of $12$ candidates |

## Suggested path

**If you are writing your first proposal:** 01, then 03. Read the scheme, compute the
weights, then read the funding arithmetic so that a rejection arrives with a context
rather than as a verdict.

**If you are finishing a thesis:** 02, then 04 §5. The contribution-support test and
the redundancy audit between them settle what the synthesis chapter must do and where
the page cut comes from.

**If you are applying for jobs:** 04, then 01 §5. Write the research statement as a
proposal with a shorter horizon, and map it to the department's published criteria.

**If you supervise:** 01 §4 (marginal value of a point) and 02 §3 (contribution
support) are the two exercises to run with a student, because both convert a vague
draft into a list of decisions.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-research-proposal.md`](01-research-proposal.md) | Lesson 01 |
| [`02-thesis-structure.md`](02-thesis-structure.md) | Lesson 02 |
| [`03-grant-funding.md`](03-grant-funding.md) | Lesson 03 |
| [`04-cv-and-career.md`](04-cv-and-career.md) | Lesson 04 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Four runnable demonstrations |

| Script | What it measures |
|---|---|
| [`code/research_proposal_demo.py`](code/research_proposal_demo.py) | Weighted scores under two schemes, funding-line flips, margin versus scheme shift, marginal value of a point |
| [`code/thesis_structure_demo.py`](code/thesis_structure_demo.py) | Chapter budget against a page limit, redundancy, contribution support, writing time |
| [`code/grant_funding_demo.py`](code/grant_funding_demo.py) | Boundary, panel-mean standard error, uncertain band, expected submissions, cost per award |
| [`code/cv_and_career_demo.py`](code/cv_and_career_demo.py) | Citation distribution and Gini, h-index insensitivity, career-length growth, rubric sensitivity |

## How to run the demos

```bash
cd 24-research-papers-writing/05-thesis-and-proposals/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python research_proposal_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python thesis_structure_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python grant_funding_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python cv_and_career_demo.py
```

All four scripts are print-only, read no files, use no network and finish in under a
second.

## Mastery checkpoint

1. Tabulate the weights of a target scheme and compute your proposal's weighted score
   under it and under a plausible alternative.
2. Compute your thesis's page total, estimate its redundancy, and list your claimed
   contributions with their supporting words.
3. Compute the standard error of a panel mean for a scheme you know and the number of
   applications inside its band.
4. Compute your expected submissions per award at the scheme's rate.
5. Write your CV's record as a distribution, and your research statement with a
   proportionate future.

## Common pitfalls across this module

1. **Writing before reading the scheme.** Weights decide what a week is worth.
2. **Optimising the total instead of clearing the line.** Near the boundary, the
   scheme decides.
3. **Cutting a thesis evenly.** Cut redundancy first; refer rather than repeat.
4. **Padding the synthesis chapter.** It does not create support for a claim.
5. **Reading a rejection as a verdict.** The band of uncertain decisions is
   measurable and wide.
6. **Writing new proposals instead of revising.** The expected-submissions arithmetic
   is decisive.
7. **Leading a CV with an index.** It ignores the work that identifies you.
8. **Quoting these synthetic numbers as institutional norms.** Every table describes a
   teaching generator.

## Related modules

- [24-03 Research Methods and Scientific Rigour](../03-research-methods-and-rigour/README.md) —
  designing the work a proposal promises and a thesis reports.
- [24-04 Presentation and Science Communication](../04-presentation-and-communication/README.md) —
  the talks, defences and public messages that accompany these documents.
- [24-06 Reproducible Publication and Open Data](../06-reproducible-publication/README.md) —
  the artefacts that make a thesis and a proposal's promises verifiable.
- [22-05 Collaboration and Project Management](../../22-data-engineering-reproducibility/05-collaboration-and-project-management/README.md) —
  data management plans and project structure for the funded project.
- [26-04 Textbook Bibliography](../../26-reference-library/04-textbook-bibliography/README.md) —
  where the literature these documents cite is catalogued.
