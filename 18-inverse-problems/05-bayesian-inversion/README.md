# Module 18-05 — Bayesian Inversion and Inference

**Stages:** doctoral → research · **Prerequisites:** modules 18-01, 18-02 and 18-03;
basic probability.

This module reformulates the inverse problem as a question about probability. A
model is not a fixed unknown to be found; it is a random variable, and the answer
to the inversion is its conditional distribution given the data. That single change
does three things at once. It makes every ingredient that a traditional inversion
inserts by hand — damping, smoothness, bounds, initialisation — explicit as a
probability statement. It replaces a number with a distribution, so that the answer
carries its own uncertainty. And it makes the regularisation parameter of
Tikhonov inversion a *derived* quantity: $\lambda^2 = \sigma_d^2/s_0^2$, the ratio
of noise variance to prior variance, which the analyst must justify rather than
tune.

The honest difficulty of the module is that the posterior is conditional — on the
likelihood and on the prior — and both are choices with consequences that are
computable. Lesson 02 measures what a wrong error model does to an interval;
lesson 03 measures how much of an answer came from the prior rather than the data;
lesson 06 measures the coverage of a Bayesian interval under a prior that disagrees
with the truth. Where a claim cannot be verified analytically, the lesson says so
and supplies an independent numerical route instead. Every demos prints the
diagnostics — acceptance rates, autocorrelation times, effective sample sizes,
split R-hat, divergence counts — that the claims rest on, because a sampler that
has not been diagnosed has not produced a result.

All models and data in this module are **SYNTHETIC**. No real data set, station,
event or published measurement is used, and no number is quoted from a published
source. Every number printed in a lesson is produced by the demonstration in
`code/` that accompanies it, or is an exact mathematical constant.

## Learning objectives

By the end of this module you will be able to:

1. **Derive** the posterior for a linear-Gaussian inverse problem, and show that
   the maximum a posteriori estimate is exactly the Tikhonov solution with
   $\lambda^2=\sigma_d^2/s_0^2$.
2. **Construct** a likelihood from a stated noise process, including correlated and
   heavy-tailed models, and **measure** the bias and the interval error produced by
   assuming independence when the noise is correlated.
3. **Quantify** the influence of a prior on the posterior, including the prior
   share of the posterior precision, prior-data conflict, and the boundary mass a
   hard constraint produces.
4. **Implement** random-walk Metropolis and Gibbs samplers, and **report** the
   integrated autocorrelation time, effective sample size and split R-hat that make
   the result auditable.
5. **Implement** Hamiltonian Monte Carlo, **measure** the second-order energy error
   of the leapfrog integrator, and **quantify** the gain from a
   covariance-matched mass matrix.
6. **Summarise** a posterior with marginals, equal-tailed and highest-posterior-density
   intervals, and independent credible regions, and **distinguish** a credible from
   a confidence statement by measuring coverage.
7. **Compute** an evidence analytically where possible, decompose it into a
   best-fit likelihood and an Occam factor, and **demonstrate** why a Bayes factor
   is conditional on the prior width.
8. **Implement** a reversible-jump sampler over models of different dimension, and
   **verify** it against an independent route to the same model probabilities.

## Prerequisites

- [18-01 Foundations of Inverse Problems](../01-inverse-problem-foundations/README.md)
  — model space, data space, and Hadamard's conditions.
- [18-02 Linear Inverse Problems](../02-linear-inverse-problems/README.md) — least
  squares, minimum norm, the generalised inverse, weighting and covariance.
- [18-03 Regularisation and Stabilisation](../03-regularization/README.md) —
  Tikhonov damping and the choice of the trade-off parameter.
- [21-03 Bayesian Inference](../../21-statistics-bayesian-ml/03-bayesian-inference/README.md)
  — the general statistical framework this module specialises to inverse problems.
- [03-02-06 The Random Module in NumPy](../../03-scientific-computing/02-numpy/06-random-module.md)
  — generators and seeding, which every demo uses.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Bayes' Theorem as an Inverse-Problem Formulation](01-bayes-inverse-formulation.md) | doctoral | The posterior is prior × likelihood; MAP is Tikhonov with $\lambda$ named; a null direction returns to the prior |
| 02 | [Constructing Likelihoods and Error Models](02-likelihood-models.md) | research | The likelihood is a claim about residuals; ignoring correlation narrows the interval by 21% and a Gaussian likelihood lets one outlier move the slope without limit |
| 03 | [Priors: Informative, Reference and Their Influence](03-priors.md) | research | A prior carries a measurable share of the information; the Jeffreys scale prior is the flat prior on $\log\sigma$; bounds produce boundary mass |
| 04 | [Markov Chain Monte Carlo: Metropolis-Hastings and Gibbs](04-mcmc.md) | research | Detailed balance; the best ESS is not at the highest acceptance; $\hat R$ detects some failures and cannot see an unvisited mode |
| 05 | [Hamiltonian Monte Carlo and Modern Samplers](05-hmc-and-modern-samplers.md) | research | Gradients replace guesswork; the leapfrog error is $\mathcal{O}(\varepsilon^2)$; the mass matrix is worth a factor of about 96 on a stiff target |
| 06 | [Posterior Summaries](06-posterior-summary.md) | doctoral | Mean, median, mode and two credible intervals all differ in a skew; a 95% credible interval covered the truth 23.5% of the time under a conflicting prior |
| 07 | [Bayesian Evidence and Model Selection](07-evidence-and-model-selection.md) | research | The evidence is an average over the prior; Occam's razor is the volume ratio; the Bayes factor moves by a factor of 68.8 across prior widths |
| 08 | [Trans-Dimensional and Reversible-Jump MCMC](08-trans-dimensional.md) | research | The model index becomes an unknown; the acceptance ratio fails silently, so a second route to $P(k\mid d)$ is mandatory |

## Suggested path

**If you are new to Bayesian inversion:** lessons 01–03 in order, running each
demonstration. Lesson 01 is the only one that must be understood before the rest;
02 and 03 can be read in either order.

**If you already know linear inverse theory:** read 01 §3–4 (the Tikhonov
equivalence), then 04 §4–5 (why the acceptance rate is not a quality measure) and
06 §5 (credible versus confidence) — the two claims most often reported without
evidence.

**If you are preparing a research project:** 02 (error models), 05 (samplers and
their diagnostics), 07 (model selection and its prior dependence) and 08 (models of
unknown dimension), plus the exercises at ★★★ level.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-bayes-inverse-formulation.md`](01-bayes-inverse-formulation.md) | Lesson 01 |
| [`02-likelihood-models.md`](02-likelihood-models.md) | Lesson 02 |
| [`03-priors.md`](03-priors.md) | Lesson 03 |
| [`04-mcmc.md`](04-mcmc.md) | Lesson 04 |
| [`05-hmc-and-modern-samplers.md`](05-hmc-and-modern-samplers.md) | Lesson 05 |
| [`06-posterior-summary.md`](06-posterior-summary.md) | Lesson 06 |
| [`07-evidence-and-model-selection.md`](07-evidence-and-model-selection.md) | Lesson 07 |
| [`08-trans-dimensional.md`](08-trans-dimensional.md) | Lesson 08 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Eight runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
SymPy:

```bash
cd 18-inverse-problems/05-bayesian-inversion/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python bayes_inverse_formulation_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python likelihood_models_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python priors_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python mcmc_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python hmc_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python posterior_summary_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python evidence_and_model_selection_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python trans_dimensional_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), makes no plots and needs no network access.
The longest, `hmc_demo.py`, runs in about four seconds; the rest finish in under a
second. Each exits with status $0$.

## Mastery checkpoint

Complete this without notes:

> A SYNTHETIC two-parameter inversion has
> $G = \begin{bmatrix}1&0\\0&1\\1&1\end{bmatrix}$, $\sigma_d = 0.5$, a prior
> $\mathcal{N}(0, 2^2I)$ and data $d = (1.7645,\,-0.7691,\,0.5949)$. **(a)** Write
> the posterior covariance and compute the posterior mean. **(b)** State $\lambda$
> for the equivalent Tikhonov problem and explain why it is not a free parameter.
> **(c)** The operator is replaced by $G_{\text{bad}}$ with parallel columns; state
> what happens to the posterior along $(1,-1)/\sqrt2$ and give the number. **(d)** A
> colleague reports a $95\%$ credible interval and calls it a $95\%$ confidence
> interval; state what the second claim requires and why it can fail.

A worked version of (a)–(c) appears in the lesson-01
[solutions](exercises/01-bayes-inverse-formulation-solutions.md).

## Common pitfalls across this module

1. **Reporting a posterior mean as the answer.** A distribution summarised by one
   number has lost the reason for the exercise.
2. **Assuming independence because the data are ordered.** The measured interval
   error at $\rho = 0.9$ is $21\%$ too narrow.
3. **Treating the prior as a formality.** In the measured table a prior of width
   $0.3$ carries $55\%$ of the posterior precision.
4. **Reading a credible interval as a frequency.** Under a conflicting prior the
   measured coverage was $23.5\%$ for a $95\%$ interval.
5. **Tuning a sampler by acceptance rate.** The measured optimum ESS occurred at
   acceptance $0.199$; a chain at $0.947$ acceptance had an ESS $117$ times smaller.
6. **Claiming convergence from $\hat R$.** A reversible-jump chain with a wrong
   acceptance ratio reported $\hat R = 1.001$ and model probabilities off by a
   factor of $25$ in the rare state.
7. **Quoting a Bayes factor without the prior width.** Measured to move by a factor
   of about $69$ across the plausible range.
8. **Forgetting to report the effective sample size.** The chain length is not the
   sample size, and the difference is often a factor of $20$ or more.

## Related modules

- [18-01 Foundations of Inverse Problems](../01-inverse-problem-foundations/README.md)
  and [18-02 Linear Inverse Problems](../02-linear-inverse-problems/README.md) — the
  deterministic formulations this module subsumes.
- [18-03 Regularisation and Stabilisation](../03-regularization/README.md) — the
  damping that reappears as a prior precision.
- [18-04 Nonlinear Inversion and Optimisation](../04-nonlinear-inversion/README.md) —
  gradients and convergence, used directly by lesson 05.
- [18-06 Uncertainty Quantification](../06-uncertainty-quantification/README.md) —
  what to do with a posterior: propagation, sensitivity, surrogate models and
  decisions.
- [18-07 Joint and Multi-Physics Inversion](../07-joint-and-multi-physics-inversion/README.md)
  — combining posteriors from different data types.
- [18-08 Practical Inversion Workflow](../08-practical-inversion-workflow/README.md)
  — synthetic testing, model assessment and responsible reporting.
- [21-03 Bayesian Inference](../../21-statistics-bayesian-ml/03-bayesian-inference/README.md)
  and [21-04 Machine Learning Fundamentals](../../21-statistics-bayesian-ml/04-machine-learning-fundamentals/README.md)
  — the statistics and learning background.
- [06-seismology/11 Earthquake Statistics and Hazard](../../06-seismology/11-earthquake-statistics-and-hazard/README.md)
  — a domain where probabilistic reasoning and credible intervals are used in
  practice.
