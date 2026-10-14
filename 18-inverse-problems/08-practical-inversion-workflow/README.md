# Module 18-08 — Practical Inversion Workflow

**Stages:** graduate → research · **Prerequisites:** modules 18-01 and 18-02;
basic regularisation (18-03).

This module is the procedural half of the folder: what to do, in order, before
and after an inversion is run. Its organising claim is that most inversion
failures are decided before the solver starts (the parameterisation), or after
it finishes (the assessment and the report), and not in the solver at all. The
four lessons correspond to the four stages of that claim: set the problem up so
that it is solvable, test it on synthetics that the production processing would
also recover, assess the produced model for resolution and artifacts, and report
it with the numbers that make it auditable.

The recurring difficulty is that an inversion always returns a picture. Every
lesson here therefore measures something a picture cannot show: the effective
number of resolved parameters, the resolution length, the admitted range of the
model at each depth, and the misfit against a noise level stated in advance. The
honest difficulty of the module is that these four quantities are exactly the
ones most often omitted, and each of them can overturn an interpretation that the
picture suggests.

All models and data in this module are **SYNTHETIC**. The operators, grids,
noise levels and weights are chosen teaching ingredients, and no number is quoted
from a real survey.

## Learning objectives

By the end of this module you will be able to:

1. **Translate** a physical question into a data count, a stated noise level and
   a parameterisation, and **justify** the parameterisation with resolution
   numbers.
2. **Compute** resolution matrices, effective parameter counts and point-spread
   functions for competing discretisations, and **choose** between them.
3. **Design** and **run** synthetic tests (spike, checkerboard, shifted pattern)
   and **report** a recovery curve rather than a picture.
4. **Assess** a produced model by the five-item protocol: misfit, complexity,
   resolution, admissibility and alternatives.
5. **Choose** a regularisation weight from a stated noise level by the
   discrepancy principle, and **state** the assumptions that choice carries.
6. **Report** a model with per-depth admitted ranges, a resolution length and a
   chi value, and **rewrite** unsupported claims into supported ones.
7. **State** the reproducibility requirements (weights, noise levels, seeds,
   code) that make an inversion auditable by a reader who never sees the data.

## Prerequisites

- [18-01-04 Discretisation, Parameterisation and Model Choice](../01-inverse-problem-foundations/04-discretisation-reality.md).
- [18-02-05 Resolution and Information Matrices in Interpretation](../02-linear-inverse-problems/05-resolution-matrices.md).
- [18-03-03 Choosing the Trade-Off: L-Curve, GCV, Discrepancy Principle](../03-regularization/03-parameter-choice.md).
- [18-06-05 Visualising and Communicating Uncertainty](../06-uncertainty-quantification/05-uncertainty-visualisation.md).

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Setting Up a Solvable Inverse Problem](01-problem-setup.md) | graduate | The grid is a choice; a cell must move the data more than the noise to be a parameter |
| 02 | [Synthetic Testing, Checkerboards and Recovery Tests](02-synthetic-testing.md) | research | Recovery is a curve, and the worst alignment is the honest number |
| 03 | [Assessing a Model: Resolution, Artifacts, Alternatives](03-model-assessment.md) | research | Five items, each a number; a feature thinner than the PSF is not a layer |
| 04 | [Reporting Inversion Results Responsibly](04-reporting-inversion.md) | doctoral | The misfit is not the objective; the admitted range is part of the model |

## Suggested path

**If you are about to run your first inversion:** lessons 01 → 03, running each
demo. Lesson 01 decides the grid; lesson 03 tells you what you may claim.

**If you are writing up a result:** lesson 04 after 03. The eight-line template
in §4 is the checklist; the three forbidden sentences in §5 are the audit.

**If you are reviewing an inversion:** lesson 04 §5–6 and lesson 03 §3. The four
questions in the lesson-04 exercises are a workable review protocol.

**If you are preparing a research project:** 02 §3 (the alignment trap), 03 §3–4
(perturbation test and admitted range), and the ★★★ exercises of 02 and 04.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-problem-setup.md`](01-problem-setup.md) | Lesson 01 |
| [`02-synthetic-testing.md`](02-synthetic-testing.md) | Lesson 02 |
| [`03-model-assessment.md`](03-model-assessment.md) | Lesson 03 |
| [`04-reporting-inversion.md`](04-reporting-inversion.md) | Lesson 04 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Four runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
SymPy:

```bash
cd 18-inverse-problems/08-practical-inversion-workflow/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python problem_setup_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python synthetic_testing_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python model_assessment_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python reporting_inversion_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), requires no network access and exits 0. All
four run in under a second.

## Mastery checkpoint

Complete this without notes:

> A 40-cell inversion of 15 observations with $\sigma = 0.25$ produces a model
> with chi per datum 0.94 and $\operatorname{tr}R = 4.94$. **(a)** State how many
> independent numbers the data supported and why the 40-cell grid was still
> legitimate. **(b)** The model shows an anomaly 1 km wide at 6.25 km where the
> PSF half-width is 4.00 km; state what you may and may not claim. **(c)** At
> 12.25 km the model value is 0.2241 with a 95% admitted range 0.0448–0.4034;
> write one supported sentence. **(d)** Name the regularisation weight choice you
> would use on real data, and the number it needs.

A worked version of (a)–(c) appears in the lesson-03 and lesson-04
[solutions](exercises/04-reporting-inversion-solutions.md).

## Common pitfalls across this module

1. **Choosing the grid last.** The parameterisation is the first decision, not
   the last.
2. **Reporting the misfit as a quality measure.** The minimum misfit can have the
   largest error.
3. **Showing a checkerboard as a picture.** Report the curve and the worst
   alignment.
4. **Quoting a model value with no admitted range.** The range is the measurement.
5. **Omitting the noise level or the weight.** Without them, nothing in the
   report can be checked.

## Related modules

- [01 Inverse Problem Foundations](../01-inverse-problem-foundations/README.md).
- [02 Linear Inverse Problems](../02-linear-inverse-problems/README.md).
- [03 Regularisation and Stabilisation](../03-regularization/README.md).
- [07 Joint and Multi-Physics Inversion](../07-joint-and-multi-physics-inversion/README.md) —
  the workflow applied to more than one data set.
- [09 Machine Learning Approaches to Inversion](../09-machine-learning-inversion/README.md) —
  the same workflow questions for learned inverses.
- [24 Research Papers and Writing](../../24-research-papers-writing/README.md) —
  the publication context for reporting conventions.
