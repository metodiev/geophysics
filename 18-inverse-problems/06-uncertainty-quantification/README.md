# Module 18-06 — Uncertainty Quantification

**Stages:** graduate → research · **Prerequisites:** module 18-05; basic
probability and numerical computing.

This module takes the posterior of 18-05 and asks what it is *for*. An inversion
that produces a distribution has not yet reported an uncertainty: it has produced an
object that must be split into components with different remedies, propagated through
a forward model that may be nonlinear, attributed to the inputs that drive it,
summarised and displayed without over-claiming, and finally converted into a decision.
Each lesson takes one of those steps and measures it.

The module's honesty point is that the components are not interchangeable and the
remedies are not universal. Adding stations lowers the epistemic term by a measured
factor and leaves the aleatory and structural terms untouched. A Monte Carlo mean
converges at a measured $N^{-1/2}$ while a tail probability converges far more
slowly. A sensitivity index estimated from $8192$ base samples has a standard error
of roughly $0.0007$, and a local derivative at a nominal point can rank the most
influential parameter last. A $95\%$ band that is correct pointwise covers a whole
curve only $74\%$ of the time. Information is worth exactly nothing when it cannot
change a decision, and most when the decision is marginal. Every one of those
statements is printed by a demonstration in `code/`, and every lesson quotes the
measurement rather than asserting the principle.

All models and data in this module are **SYNTHETIC**. No real data set, station,
survey or published measurement is used. Every number printed in a lesson is produced
by the demonstration that accompanies it, or is an exact mathematical constant or a
derived analytic result.

## Learning objectives

By the end of this module you will be able to:

1. **Separate** prediction uncertainty into aleatory, epistemic and structural
   components, and **state** which remedy reaches each.
2. **Propagate** an uncertain input distribution through a nonlinear forward model by
   Monte Carlo, **measure** the convergence rate, and **report** the standard error
   and the effective sample size.
3. **Apply** antithetic variates and importance sampling, and **measure** the
   variance reduction rather than assume it.
4. **Compute** first-order and total Sobol' sensitivity indices with the
   Saltelli/Jansen estimators, and **demonstrate** with a measured example that a
   local derivative analysis can invert the ranking.
5. **Build** a polynomial-chaos surrogate in a basis orthonormal for the input
   measure, read the moments and indices off its coefficients, and **validate** it on
   held-out points.
6. **Distinguish** pointwise from simultaneous credible bands, and **compute** the
   widening required to convert one into the other.
7. **Demonstrate** that overlapping credible bands are not evidence that two models
   agree, by measuring overlap and a Bayes factor on the same data.
8. **Compute** the expected value of perfect and sample information, and **explain**
   why the value is zero when the information cannot change the action.

## Prerequisites

- [18-05 Bayesian Inversion and Inference](../05-bayesian-inversion/README.md) — the
  posterior, its likelihood and its summary statistics.
- [18-05-06 Posterior Summaries](../05-bayesian-inversion/06-posterior-summary.md) —
  the intervals this module displays and decides from.
- [03-02-06 The Random Module in NumPy](../../03-scientific-computing/02-numpy/06-random-module.md)
  — reproducible sampling, used by every demonstration.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Taxonomy of Uncertainty: Aleatory, Epistemic, Structural](01-uncertainty-taxonomy.md) | doctoral | Three components, three remedies; one separating datum cut the worst-direction epistemic s.d. by a factor of 284 |
| 02 | [Monte Carlo Propagation and Its Convergence](02-monte-carlo-uq.md) | graduate | Measured $N^{-1/2}$ convergence; antithetic variates gave $21\times$ variance reduction; importance sampling found a $3.6\times10^{-5}$ probability with $11\%$ ESS of its $200\,000$ draws |
| 03 | [Sensitivity Analysis: Local, Global, Sobol Indices](03-sensitivity-analysis.md) | research | Exact indices verified by QMC; a local derivative of exactly zero for the parameter carrying $84\%$ of the variance |
| 04 | [Surrogate Models and Polynomial Chaos for UQ](04-surrogate-uq.md) | research | Degree-2 exactness for a polynomial model; a degree-1 surrogate inverts the ranking; a measured $19.5\times$ saving in forward evaluations |
| 05 | [Visualising and Communicating Uncertainty](05-uncertainty-visualisation.md) | doctoral | A $95\%$ pointwise band covered the whole curve $74\%$ of the time; a mean $\pm 2\sigma$ bar reached $-0.29$ s |
| 06 | [Decision-Making Under Uncertainty and Value of Information](06-decision-under-uncertainty.md) | research | EVPI rises as the decision becomes marginal; the same survey is worth $0$ or $8.9$ depending on the decision |

## Suggested path

**If you are new to uncertainty quantification:** lessons 01, 02 and 05 in order,
running each demonstration. Lesson 01 sets the vocabulary, lesson 02 the arithmetic,
and lesson 05 the reporting.

**If you already propagate uncertainties:** read 02 §3–4 (variance reduction and
importance sampling), then 03 and 04 — the sensitivity question and the surrogate
answer.

**If you are preparing a research project:** 01 §4 (design and identifiability),
03 §5 (why local sensitivities mislead), 04 §5–6 (surrogate error and cost), and 06
§4 (value of information), plus the exercises at ★★★ level.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-uncertainty-taxonomy.md`](01-uncertainty-taxonomy.md) | Lesson 01 |
| [`02-monte-carlo-uq.md`](02-monte-carlo-uq.md) | Lesson 02 |
| [`03-sensitivity-analysis.md`](03-sensitivity-analysis.md) | Lesson 03 |
| [`04-surrogate-uq.md`](04-surrogate-uq.md) | Lesson 04 |
| [`05-uncertainty-visualisation.md`](05-uncertainty-visualisation.md) | Lesson 05 |
| [`06-decision-under-uncertainty.md`](06-decision-under-uncertainty.md) | Lesson 06 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Six runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
SymPy:

```bash
cd 18-inverse-problems/06-uncertainty-quantification/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python uncertainty_taxonomy_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python monte_carlo_uq_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python sensitivity_analysis_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python surrogate_uq_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python uncertainty_visualisation_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python decision_under_uncertainty_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), produces no plots — the visualisation lesson
prints the numbers a figure caption would need instead — and needs no network access.
Each exits with status $0$; the longest runs in about two seconds.

## Mastery checkpoint

Complete this without notes:

> A prediction carries a structural bias of $0.18$ data units, an epistemic standard
> deviation of $0.084$ and an aleatory standard deviation of $0.20$, at a location
> $x^* = 6$ km. **(a)** Compute the total RMSE and the share contributed by the bias.
> **(b)** State which component responds to more stations at the same aperture, and
> by what law. **(c)** A $95\%$ credible band is drawn with $120$ depth samples; state
> the difference between its pointwise and simultaneous coverage and give the measured
> numbers for a synthetic ensemble. **(d)** A survey would halve the epistemic term.
> State what else must be known before its value can be assessed.

A worked version of (a)–(b) appears in the lesson-01
[solutions](exercises/01-uncertainty-taxonomy-solutions.md).

## Common pitfalls across this module

1. **Calling a bias "noise".** Measured: the structural term reached $88.4\%$ of the
   mean square error at $x^* = 12$ km and no amount of data reduced it.
2. **Reporting draws without a standard error or an effective sample size.** The
   plain Monte Carlo rare-event estimate rested on $75$ events with an $11.5\%$
   relative error; the importance-sampling estimate had $11.0\%$ ESS and a $3.0\%$
   relative error.
3. **Assuming a variance-reduction scheme helps.** It is a property of the integrand
   and must be measured.
4. **Quoting first-order sensitivity indices as "the" sensitivity.** Measured
   interaction shares of $0.10$ on the largest parameter.
5. **Trusting a surrogate because its training error is small.** An underdetermined
   fit with $35$ coefficients and $20$ points had a held-out RMSE of $1.03$.
6. **Drawing a symmetric band for a skewed posterior.** The measured lower edge was
   $-0.2918\ \mathrm{s}$ for a quantity that cannot be negative.
7. **Reading overlapping bands as agreement.** Measured: $100\%$ overlap with a
   $\log_{10}$ Bayes factor of $3.86$ against one of the two models.
8. **Valuing information without a decision.** Measured: EVSI exactly zero when the
   action cannot change.

## Related modules

- [18-05 Bayesian Inversion and Inference](../05-bayesian-inversion/README.md) — the
  posterior this module quantifies.
- [18-07 Joint and Multi-Physics Inversion](../07-joint-and-multi-physics-inversion/README.md)
  — where the uncertainty of several data types is combined.
- [18-08 Practical Inversion Workflow](../08-practical-inversion-workflow/README.md)
  — synthetic testing, model assessment and responsible reporting.
- [19-07 Verification, Validation and Uncertainty Quantification](../../19-numerical-modeling-hpc/07-verification-validation-uncertainty/README.md)
  — the same concepts in a simulation-code setting.
- [21-03 Bayesian Inference](../../21-statistics-bayesian-ml/03-bayesian-inference/README.md)
  — the statistical background.
- [06-seismology/11 Earthquake Statistics and Hazard](../../06-seismology/11-earthquake-statistics-and-hazard/README.md)
  and [11-01 The Exploration Workflow](../../11-exploration-geophysics/01-exploration-workflow/README.md)
  — two domains where these decisions are taken in practice.
