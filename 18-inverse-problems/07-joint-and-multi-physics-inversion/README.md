# Module 18-07 — Joint and Multi-Physics Inversion

**Stages:** advanced → research · **Prerequisites:** modules 18-01 and 18-02;
the Tikhonov material of 18-03.

This module is about the one honest reason to invert two data sets together
instead of separately: the two forward operators have different **null spaces**,
so each sees directions the other leaves free. Everything the module claims is
bounded by that sentence. Combining data sets cannot create information; it can
only apply the constraints of one operator to the directions the other cannot
reach, and it does so through an assumption — the same parameters, the same
geometry, or a rock-physics relation — which is a statement about the Earth and
is therefore testable and falsifiable.

The organising difficulty is that a joint inversion always produces a picture.
The coupling term is a regulariser with a weight, and a weight can be raised
until the answer looks like the assumption rather than the data. Every lesson
therefore measures the coupling: the rank and resolution it adds (lesson 01),
the misfit it costs (lesson 02), the bias it imposes when the relation is wrong
(lesson 03), the uncertainty it silently mis-states when a workflow's prior is
not the posterior it claims (lesson 04), and the three failure modes together,
with the chi table that exposes all of them (lesson 05).

All models and data in this module are **SYNTHETIC**. No real survey, station,
well or rock-physics compilation is used, and no number is quoted from a
published study.

## Learning objectives

By the end of this module you will be able to:

1. **State** what joint inversion can and cannot add, in terms of the null spaces
   and model-space spans of the operators involved.
2. **Quantify** complementarity from singular values, rank and the model
   resolution matrix, and **report** the gain in resolution rather than a picture.
3. **Derive** the cross-gradient coupling term, its gradient, and its scaling
   identity, and **explain** the flat-model loophole.
4. **Formulate** a petrophysical coupling and **measure** the optimal weight, the
   gain, and the bias from a wrong relation.
5. **Prove** that exact Gaussian sequential updating equals the simultaneous
   solution, and **identify** the three ways real workflows differ from it.
6. **Diagnose** weighting dominance, inconsistent physics and over-coupling from
   a chi table, a weight sweep and the separate inversions.
7. **Write** a joint-inversion report in which the weights, the noise levels, the
   chi values and the coupling assumption are all stated and checkable.

## Prerequisites

- [18-01-03 Null Space, Non-Uniqueness and Equivalence Classes](../01-inverse-problem-foundations/03-null-space.md) —
  the equivalence classes that make a second datum useful.
- [18-02-04 SVD Analysis: Model Resolution and Data Importance](../02-linear-inverse-problems/04-svd-analysis-inverse.md) —
  rank, resolution, effective parameters.
- [18-03-02 Tikhonov Regularisation and the Smoothing Trade-Off](../03-regularization/02-tikhonov.md) —
  the penalty/weight pattern the coupling extends.
- [18-05-01 Bayes' Theorem as an Inverse-Problem Formulation](../05-bayesian-inversion/01-bayes-inverse-formulation.md) —
  used in lesson 04.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Why Joint Inversion: Complementary Sensitivities](01-joint-inversion-concepts.md) | research | Joint rank 14 from ranks 6 and 10; one datum leaves a hyperbola, a second removes it; the gain depends on an error correlation you cannot measure |
| 02 | [Structural (Cross-Gradient) Coupling](02-structural-joint-inversion.md) | research | The penalty sees orientation, not amplitude; a constant model satisfies it exactly; a false hypothesis is a systematic bias |
| 03 | [Petrophysically Coupled Joint Inversion](03-petrophysical-joint-inversion.md) | research | A relation is information with a bias-variance optimum; a wrong relation is imposed just as effectively as a right one |
| 04 | [Sequential vs Simultaneous Inversion](04-sequential-vs-simultaneous.md) | research | The two-stage Gaussian update is the joint update; over-confident priors break it silently |
| 05 | [Pitfalls: Inconsistent Physics, Weighting, Over-Coupling](05-joint-inversion-pitfalls.md) | research | The chi table, the weight sweep and the separate inversions catch all three |

## Suggested path

**If you are new to multi-physics work:** lessons 01 → 02 → 05, running each
demo. Lesson 05 is the one to keep; it is the checklist.

**If you come from a single-method background:** start at 01 §2–3 for the rank
and resolution arithmetic, then 03 if your target has a rock-physics relation,
otherwise 02.

**If you are preparing a research project:** 02 §4 (the flat-model loophole),
03 §5 (circularity of clustering), 04 §3–5 (the sequential failure modes), and
the ★★★ exercises of 05.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-joint-inversion-concepts.md`](01-joint-inversion-concepts.md) | Lesson 01 |
| [`02-structural-joint-inversion.md`](02-structural-joint-inversion.md) | Lesson 02 |
| [`03-petrophysical-joint-inversion.md`](03-petrophysical-joint-inversion.md) | Lesson 03 |
| [`04-sequential-vs-simultaneous.md`](04-sequential-vs-simultaneous.md) | Lesson 04 |
| [`05-joint-inversion-pitfalls.md`](05-joint-inversion-pitfalls.md) | Lesson 05 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Five runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
SymPy:

```bash
cd 18-inverse-problems/07-joint-and-multi-physics-inversion/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python joint_inversion_concepts_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python structural_cross_gradient_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python petrophysical_coupling_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python sequential_vs_simultaneous_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python joint_inversion_pitfalls_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), requires no network access, and exits 0. The
slowest runs in about five seconds.

## Mastery checkpoint

Complete this without notes:

> Two data sets are to be inverted jointly for one model. **(a)** You are told
> their operators have ranks 6 and 10 out of 40 cells; state the possible joint
> ranks and what determines where the truth lies. **(b)** You measure a
> vertical-gravity datum $H\Delta\rho = 1.2000$ with $\sigma = 0.020$ and a depth
> datum $H = 4.00$ km with $\sigma = 0.10$ km; compute the joint posterior
> standard deviations. **(c)** Your colleague adds a cross-gradient penalty and
> reports both model errors falling by 0.4%; state what else must be reported
> before that is a result. **(d)** The final chi values are 1.2 and 6.8; state
> what has happened and what you would do next.

A worked version of (b)–(d) appears in the lesson-01 and lesson-05
[solutions](exercises/01-joint-inversion-concepts-solutions.md).

## Common pitfalls across this module

1. **Quoting a joint model without the weights, the noise levels and the chi
   values.** Non-reproducible and unauditable.
2. **Raising a coupling weight until the picture looks right.** That is choosing
   the answer; the chi will eventually betray you.
3. **Assuming the coupling hypothesis rather than testing it.** Cross-gradient
   coupling and petrophysical relations are statements about the Earth.
4. **Treating the two-stage identity as a licence.** Sequential equals
   simultaneous only under stated conditions; the failures are in the prior.
5. **Believing that more data must give a better model at a specific truth.** The
   guarantee is prior-averaged; lesson 04 measures the difference.

## Related modules

- [01 Inverse Problem Foundations](../01-inverse-problem-foundations/README.md) —
  well-posedness and null spaces.
- [02 Linear Inverse Problems](../02-linear-inverse-problems/README.md) — the SVD
  and resolution machinery used throughout.
- [08 Practical Inversion Workflow](../08-practical-inversion-workflow/README.md) —
  how to test, assess and report the result.
- [09 Machine Learning Approaches to Inversion](../09-machine-learning-inversion/README.md) —
  what a learned surrogate or prior adds, and what it does not.
- [06 Uncertainty Quantification](../06-uncertainty-quantification/README.md) — the
  error model the joint gain depends on.
- [11 Exploration Geophysics](../../11-exploration-geophysics/README.md) — where
  multi-method surveys are designed and paid for.
