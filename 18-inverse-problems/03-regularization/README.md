# Module 18-03 — Regularisation and Stabilisation

**Stages:** graduate → research · **Prerequisites:** modules 18-01 and 18-02;
[05-03 Forward Modelling Principles](../../05-core-geophysics/03-forward-modelling-principles/README.md).

This module answers the question that lessons 18-01 and 18-02 leave open: if the
unregularised solution of a discretised first-kind problem is dominated by noise
amplification, what exactly should replace it, and what does the replacement
cost? Each lesson takes one family of penalties, derives it, and then *measures*
its bias, its resolution and its failure modes on the same synthetic
potential-field problem, so that the comparisons are between objectives and not
between solvers.

The organising idea is that **regularisation is a model choice, not a numerical
setting**. A penalty asserts something about the Earth — that the property field
is smooth, or sparse, or piecewise constant, or non-negative — and the assertion
is imposed whether or not it is true. Every lesson therefore carries three
things: a derivation, a measurement of the trade-off the penalty buys, and a
measurement of what happens when the prior is wrong. The measurements include the
exact bias–variance decomposition of Tikhonov, the closed-form amplitude bias of
$\ell_1$, the annihilation threshold of total variation, the residual cost of a
false bound, and the equivalence class of models that fit a nonlinear problem
equally well.

All models and data in this module are **SYNTHETIC**. The forward physics is the
exact 2-D line-mass gravity formula, so the kernel is a real forward operator,
but the density distributions, station grids, target depths and noise are chosen
teaching values. No measured data, no published spectrum and no instrument noise
level is used anywhere; every number quoted in a lesson is printed by a
demonstration in [`code/`](code) or is an exact standard constant.

## Learning objectives

By the end of this module you will be able to:

1. Explain why an unregularised solution of a first-kind problem is unusable with
   noise, and quantify the amplification from the singular-value spectrum and the
   discrete Picard condition.
2. Derive the Tikhonov estimator, its filter factors and its exact bias and
   variance, and compute the $\alpha$ that minimises their sum.
3. Choose a regularisation parameter by the L-curve, GCV or the discrepancy
   principle, state each rule's assumption, and measure how it fails when the
   assumption is violated.
4. Derive the optimality conditions of $\ell_1$ regularisation, the exact
   critical parameter $\alpha_{\max} = \|A^{\mathsf T}d\|_\infty$ and the
   closed-form shrinkage, and measure the support-recovery phase transition and
   the coherence limit.
5. Explain the piecewise-constant prior of total variation, measure an
   edge-preserving advantage and the staircase artefact that comes with it.
6. Formulate constraints as convex feasible sets, derive the KKT conditions, and
   measure the bias, the misfit and the active set they produce.
7. Regularise a nonlinear problem, measure the convergence order and the
   equivalence class of equally acceptable models, and state the parameters that
   must accompany a reported solution.

## Prerequisites

- [18-01-02 Hadamard's Conditions: Existence, Uniqueness, Stability](../01-inverse-problem-foundations/02-hadamard-well-posedness.md) —
  what "ill-posed" means before it is fixed.
- [18-02-04 SVD Analysis: Model Resolution and Data Importance](../02-linear-inverse-problems/04-svd-analysis-inverse.md) —
  the singular-value coordinates every lesson uses.
- [18-02-06 Data Weighting and Error Covariance Specification](../02-linear-inverse-problems/06-weighting-and-covariance.md) —
  what $\chi^2$ means, and why every measurement here is quoted against
  $n\sigma^2$.
- [05-03-01 The Forward Problem: From Model to Data](../../05-core-geophysics/03-forward-modelling-principles/01-forward-problem.md) —
  how the kernel is built.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Why Regularisation Is Physically and Statistically Justified](01-why-regularize.md) | graduate | Exact data inverts to $10^{-10}$; $0.5\%$ noise gives $10^{3}$; the Picard plot says which components survive |
| 02 | [Tikhonov Regularisation and the Smoothing Trade-Off](02-tikhonov.md) | doctoral | Filter factors, an exact bias–variance sum, and an oracle $\alpha$ that costs 3.6× more variance than bias |
| 03 | [Choosing the Trade-Off: L-Curve, GCV, Discrepancy Principle](03-parameter-choice.md) | research | Three rules, their assumptions, and measured biases of 1.25× to 7.6× the oracle |
| 04 | [L1 Regularisation, Sparsity and Compressive Sensing](04-sparsity.md) | research | Exact zeros, an exact $\alpha_{\max}$, an exact $\mathcal O(\alpha)$ bias, and a coherence limit |
| 05 | [Total Variation and Edge-Preserving Inversion](05-total-variation.md) | research | Edges three times sharper than the data support — and 15 invented steps on a smooth model |
| 06 | [Physical Constraints, Bounds and Feasible Model Sets](06-constraints.md) | graduate | A false bound costs 9× the error and 1100× the residual; an inactive bound costs nothing |
| 07 | [Regularisation of Nonlinear Problems](07-nonlinear-regularization.md) | research | Linear convergence, a 22% biased minimum, and an equivalence class 0.65 km wide |

## Suggested path

**If you are new to regularisation:** lessons 01 → 02 → 06, running each
demonstration. Lesson 02 contains the exact decomposition that makes the rest
readable; lesson 06 is the shortest route to seeing a prior change an answer.

**If you have used Tikhonov before:** read 01 §3 and §4 (the measurements), then
02 §4 (the exact bias–variance) and 03 (what happens when the truth is unknown).

**If you are here for sparse or edge-preserving methods:** 04 and 05, in that
order, then 03 §6–7 on failure modes; the phase transition and the coherence
failure in 04 are the two results most often missing from applied papers.

**If you are preparing a research project:** 03, 04 §5–6, 05 §4 and 07 §5, plus
the ★★★ exercises; each of those sections describes an experiment you can run on
your own problem.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-why-regularize.md`](01-why-regularize.md) | Lesson 01 |
| [`02-tikhonov.md`](02-tikhonov.md) | Lesson 02 |
| [`03-parameter-choice.md`](03-parameter-choice.md) | Lesson 03 |
| [`04-sparsity.md`](04-sparsity.md) | Lesson 04 |
| [`05-total-variation.md`](05-total-variation.md) | Lesson 05 |
| [`06-constraints.md`](06-constraints.md) | Lesson 06 |
| [`07-nonlinear-regularization.md`](07-nonlinear-regularization.md) | Lesson 07 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Seven runnable demonstrations |

| Script | What it measures |
|---|---|
| [`code/why_regularize_demo.py`](code/why_regularize_demo.py) | Singular-value decay, Picard condition, noise amplification, truncation optimum, second-kind control |
| [`code/tikhonov_demo.py`](code/tikhonov_demo.py) | Filter factors, exact bias–variance against Monte Carlo, point-spread width, $L=I$ versus $L=D$ |
| [`code/parameter_choice_demo.py`](code/parameter_choice_demo.py) | L-curve corner and its hidden smoothing, GCV, discrepancy principle, three failure modes |
| [`code/sparsity_demo.py`](code/sparsity_demo.py) | KKT check, exact $\alpha_{\max}$, closed-form bias, over-selection, phase transition, coherence |
| [`code/total_variation_demo.py`](code/total_variation_demo.py) | ADMM residuals, edge widths, staircase count, amplitude bias |
| [`code/constraints_demo.py`](code/constraints_demo.py) | Inactive bounds, false non-negativity, PAVA verification, POCS non-emptiness test |
| [`code/nonlinear_regularization_demo.py`](code/nonlinear_regularization_demo.py) | Jacobian verification, convergence rate, $\alpha$ sweep, equivalence class, IRLS |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
pandas:

```bash
cd 18-inverse-problems/03-regularization/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python why_regularize_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python tikhonov_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python parameter_choice_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python sparsity_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python total_variation_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python constraints_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python nonlinear_regularization_demo.py
```

Every demo prints labelled results with units, seeds its random numbers with
`np.random.default_rng(20261014)`, uses no network access and exits 0. The
longest, `total_variation_demo.py`, runs in about nine seconds.

## Mastery checkpoint

Complete this without notes, using the demonstrations only to check arithmetic:

> A colleague inverts the synthetic 64-station gravity profile of lesson 01 with
> $0.5\%$ noise. **(a)** They report an unregularised model with relative error
> $1.4\times10^{3}$ and a data misfit of $0.0000\%$. Explain in two sentences how
> both can be true, and state which of the two numbers is evidence of a problem.
> **(b)** They switch to Tikhonov with $L=I$ and $\alpha$ chosen by GCV, and
> report a residual of $0.62\,n\sigma^2$. State what that residual implies about
> $\alpha$ and what a sceptical reader should ask for. **(c)** They then impose a
> piecewise-constant prior and obtain a model with 12 sharp steps and
> $\chi^2/(n\sigma^2) = 0.8$. State the prior that was imposed, the two geologies
> for which it is appropriate, and the one measurement that would test it.
> **(d)** Finally they impose a hard bound $0 \le m \le 2$ while the truth peaks
> at $3.0$, and report $\chi^2/(n\sigma^2) = 1310$. State the two signatures of a
> wrong bound and which of them a reader can check without the truth.

Worked versions of (a)–(d) appear in the lesson solutions at ★★★ level.

## Common pitfalls across this module

1. **Judging an inversion by its residual.** In this module a misfit of
   $0.0000\%$ coexists with a model error of $10^{3}$, and three different priors
   all achieve $\chi^2 \approx n\sigma^2$ while differing in error by a factor of
   13.6.
2. **Quoting a regularisation parameter without its operator, normalisation and
   rule.** $\alpha$ for $L=I$ and for $L=D$ differ by two decades at equal error;
   the L-curve corner moves by a factor of 6.8 with the smoothing of the curve.
3. **Believing a biased method is a defect to be removed.** Every method in this
   module is biased by construction, the bias is computable, and the choice of
   bias is the analyst's.
4. **Assuming sparsity or edge preservation transfers from theory to
   geophysics.** Measured support recovery of the line-mass kernel is 0.00 at
   every sparsity tested, and TV invents 11–15 steps on a smooth model.
5. **Reporting a hard constraint as if it were data.** An active false bound
   inflates the error by a factor of 9 in the model and 1100 in $\chi^2$; the
   active set belongs in the report.

## Related modules

- [18-01 Inverse Problem Foundations](../01-inverse-problem-foundations/README.md) —
  ill-posedness, null spaces and the model–data mapping that this module fixes.
- [18-02 Linear Inverse Problems](../02-linear-inverse-problems/README.md) —
  least squares, the pseudo-inverse and resolution matrices.
- [18-04 Nonlinear Inversion and Optimisation](../04-nonlinear-inversion/README.md) —
  the local and global search methods that call the penalties of this module.
- [18-05 Bayesian Inversion and Inference](../05-bayesian-inversion/README.md) —
  the same priors expressed probabilistically, with uncertainty attached.
- [18-08 Practical Inversion Workflow](../08-practical-inversion-workflow/README.md) —
  how to set up, test and report an inversion in practice.
- [05-03 Forward Modelling Principles](../../05-core-geophysics/03-forward-modelling-principles/README.md) —
  the forward models being inverted.
