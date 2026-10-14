# Module 21-03 — Bayesian Inference

**Stages:** doctoral → research · **Prerequisites:**
[21-01 Statistics in Geophysical Practice](../01-statistics-in-practice/README.md)
and [01-13 Probability and Statistics Foundations](../../01-mathematics/13-probability-and-statistics-foundations/README.md).

Bayesian inference is the branch of statistics that treats a parameter as a
random variable and a probability as a degree of belief. Its appeal in
geophysics is immediate: the quantities we want — a slip rate, a permeability
field, the depth of a interface — are unknown to us by definition, and the
question "what is the probability it lies in this range?" is exactly the question
a Bayesian posterior answers directly. This module builds that apparatus in
order: the paradigm and the meaning of a prior, the families whose posteriors are
exact, the hierarchical models that let groups borrow strength, the samplers that
handle everything else, the approximations that make it scale, and the workflow
that checks the whole construction.

The organising idea is that **the prior is a model, and its influence is a
measurable quantity**. Every lesson reports the prior-equivalent sample size or
its analogue: a $\mathrm{Beta}(20,20)$ prior carries $38$ observations' worth of
information and moved a posterior mean by $0.136$ on a sample of $30$; a
mean-field approximation that ignores a correlation of $-0.8955$ reports
$44.5\ \%$ of the true posterior standard deviation; a prior whose mean is
comparable to a plug-in estimate produced a prior predictive range that excluded
half the observed data. None of these is a defect of the method; each is a number
that belongs in the report.

A second thread is **what each diagnostic can and cannot see**. MCMC's
$\hat R = 1.00012$ and an effective sample size of $3918$ from $19\,000$ draws
certify the sampler and say nothing about the model. A missing Jacobian shifted
the posterior mean by $3.3\ \%$ while every diagnostic looked excellent. Only a
comparison against a known answer — which is why this module uses conjugate
targets throughout — can catch a wrong target. The workflow lesson turns that
into a sequence of explicit checks, each of which can fail.

All models and data in this module are **SYNTHETIC**. Every posterior is either
known in closed form or sampled from a target the code defines; no measured
value enters. The demonstrations are print-only, seeded with
`np.random.default_rng(20261014)`, need no network, create no files, and each
runs in well under ten seconds.

## Learning objectives

By the end of this module you will be able to:

1. **Write** Bayes' theorem for a parameter and **justify** a prior through
   exchangeability rather than convenience.
2. **Distinguish** credible from confidence intervals and **state** what each
   claims.
3. **Derive** the Beta-Binomial, Normal-Normal and Gamma-Poisson updates and
   **verify** them numerically.
4. **Fit** a hierarchical model, **compute** the shrinkage factor, and **explain**
   why partial pooling wins on mean squared error.
5. **Run** an MCMC sampler, **compute** $\tau_{\text{int}}$, $N_{\text{eff}}$ and
   split-$\hat R$, and **detect** a burn-in transient.
6. **Derive** the ELBO, **implement** mean-field CAVI, and **quantify** the
   variance under-estimate it produces.
7. **Run** prior predictive, posterior predictive and predictive-comparison checks
   and **report** their outcomes, including ties.
8. **State** for each result which assumption it rests on and what a wrong
   assumption would change.

## Prerequisites

- [01-13-01 Probability Axioms, Conditional Probability and Bayes' Rule](../../01-mathematics/13-probability-and-statistics-foundations/01-probability-axioms.md) —
  the theorem the module applies.
- [01-13-04 Common Distributions and Their Earth-Science Roles](../../01-mathematics/13-probability-and-statistics-foundations/04-distributions.md) —
  the families whose conjugacy is exploited in lesson 02.
- [21-01-02 Choosing Probability Models for Earth Data](../01-statistics-in-practice/02-probability-models-earth.md) —
  the likelihood side of every model here.
- [21-02-05 Geostatistics Combined with Geophysical Inversion](../02-geostatistics/05-geostatistics-inversion.md) —
  a linear Gaussian posterior worked out before this module.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [The Bayesian Paradigm and Subjective Probability](01-bayesian-paradigm.md) | doctoral | Three priors on one sample give posterior means of $0.2500$, $0.2647$ and $0.3857$; the sceptical prior carries $38$ observations |
| 02 | [Conjugate Priors and Analytic Posteriors](02-conjugate-priors.md) | research | The data weight is $0.909091$; precision adds, and the prior is a pseudo-observation |
| 03 | [Hierarchical Models and Exchangeability](03-hierarchical-models.md) | research | Partial pooling shrinks a group of three by $48\ \%$ and cuts the total error by $17\ \%$ while adding bias |
| 04 | [MCMC in Practice: Diagnostics, Burn-In, Convergence](04-mcmc-practice.md) | research | $19\,000$ correlated draws are worth $3918$; the missing Jacobian costs $3.3\ \%$ and no diagnostic notices |
| 05 | [Variational Inference and Scalable Bayes](05-variational-inference.md) | research | Mean field reports $44.5\ \%$ of the true posterior standard deviation, exactly $\sqrt{1-\rho^{2}}$ |
| 06 | [Bayesian Workflow and Principled Model Building](06-bayesian-workflow.md) | research | A model comparison returns a tie at $0.17\sigma$; predictive checks falsify but never confirm |

## Suggested path

**If you are new to Bayesian inference:** lessons 01 → 02 → 06, running every
demonstration. Lesson 01 fixes the meaning, lesson 02 gives the arithmetic, and
lesson 06 shows how the pieces are checked.

**If you have a hierarchical data set:** lesson 03 in full, then lesson 04 for
the sampling that unknown variance components require. The shrinkage table in
lesson 03 §6 is the result most often missing from applied work.

**If you are scaling to large data:** lesson 05, then lesson 06 §5 for how an
approximate posterior is reported. The calibration step in lesson 05 §4 is not
optional.

**If you are reviewing someone else's analysis:** lesson 06 §2 and §5, plus
lesson 01 §6 on prior sensitivity. Those three sections are the checklist.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-bayesian-paradigm.md`](01-bayesian-paradigm.md) | Lesson 01 |
| [`02-conjugate-priors.md`](02-conjugate-priors.md) | Lesson 02 |
| [`03-hierarchical-models.md`](03-hierarchical-models.md) | Lesson 03 |
| [`04-mcmc-practice.md`](04-mcmc-practice.md) | Lesson 04 |
| [`05-variational-inference.md`](05-variational-inference.md) | Lesson 05 |
| [`06-bayesian-workflow.md`](06-bayesian-workflow.md) | Lesson 06 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Six runnable demonstrations |

| Script | What it measures |
|---|---|
| [`code/bayesian_paradigm_demo.py`](code/bayesian_paradigm_demo.py) | Three grid posteriors, sequential versus batch updating, prior-equivalent sample size |
| [`code/conjugate_priors_demo.py`](code/conjugate_priors_demo.py) | Beta-Binomial, Normal-Normal and Gamma-Poisson posteriors with a numerical check |
| [`code/hierarchical_models_demo.py`](code/hierarchical_models_demo.py) | Three estimators, the shrinkage table, total error against the truth |
| [`code/mcmc_practice_demo.py`](code/mcmc_practice_demo.py) | Acceptance, autocorrelation time, $N_{\text{eff}}$, split-$\hat R$, burn-in |
| [`code/variational_inference_demo.py`](code/variational_inference_demo.py) | Mean-field CAVI, ELBO trajectory, exact KL, variance under-estimate |
| [`code/bayesian_workflow_demo.py`](code/bayesian_workflow_demo.py) | Prior predictive, exact LOO, WAIC, posterior predictive |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
pandas:

```bash
cd 21-statistics-bayesian-ml/03-bayesian-inference/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python bayesian_paradigm_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python conjugate_priors_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python hierarchical_models_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python mcmc_practice_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python variational_inference_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python bayesian_workflow_demo.py
```

Every demo prints labelled results with units, seeds its random numbers with
`np.random.default_rng(20261014)`, uses no network access, creates no files and
exits 0. All run in under a second; the longest,
`mcmc_practice_demo.py`, spends a half second on $80\,000$ Metropolis updates.

## Mastery checkpoint

Complete this without notes, using the demonstrations only to check arithmetic:

> A colleague estimates the recurrence rate of a fault from $30$ palaeoseismic
> observations. **(a)** They use a $\mathrm{Beta}(20,20)$-like prior carrying
> $38$ observations' worth of information and report a posterior mean that moves
> the estimate by $0.136$. State what you would ask them to report and why the
> analysis is prior-dominated. **(b)** They fit the model by MCMC, report
> $\hat R = 1.0001$ and stop. State two failures that diagnostic cannot detect.
> **(c)** They switch to variational inference to make it faster and report an
> interval half as wide as the MCMC one. State the likely cause and the
> calibration step they skipped. **(d)** Their model comparison gives an elpd
> difference of $0.4$ with a standard error of $1.1$ and they declare a winner.
> State the correct conclusion and what you would report instead. **(e)** They
> run no prior predictive check. State what that check would have caught and give
> one concrete prior it would have rejected.

Worked versions of (a)–(e) appear in the lesson solutions at ★★★ level.

## Common pitfalls across this module

1. **Hiding the prior.** Three priors on the same $30$ observations moved the
   posterior mean by $0.136$, comparable to the credible-interval width.
2. **Reading a credible interval as a confidence interval.** They answer
   different questions, and the Bayesian interval makes no guarantee when the
   prior is wrong.
3. **Reporting the posterior where the predictive is needed.** The predictive is
   wider by the sampling variance — a factor of $3.5$ for one observation.
4. **Treating shrinkage as a defect.** Partial pooling reduced the total error by
   $17\ \%$ while increasing the bias, which is the trade, not an accident.
5. **Trusting MCMC diagnostics as model checks.** They certified a sampler that
   was sampling a $3.3\ \%$ shifted target.
6. **Using a mean-field interval as if it were exact.** It reported $44.5\ \%$ of
   the true posterior standard deviation.
7. **Declaring a model comparison winner on a difference smaller than its
   standard error.** An elpd difference of $0.17\sigma$ is a tie.

## Related modules

- [21-01 Statistics in Geophysical Practice](../01-statistics-in-practice/README.md) —
  the frequentist tools this module is compared with.
- [21-02 Geostatistics](../02-geostatistics/README.md) — the linear Gaussian case
  of every construction here.
- [21-04 Machine Learning Fundamentals](../04-machine-learning-fundamentals/README.md) —
  where the ELBO becomes a training loss and shrinkage becomes regularisation.
- [18-05 Bayesian Inversion and Inference](../../18-inverse-problems/05-bayesian-inversion/README.md) —
  the same construction for inverse problems.
- [21-08 Causal Inference and Experimental Design](../08-causal-inference-and-design/README.md) —
  where posterior contrasts answer causal questions.
- [21-09 Ethical and Responsible Quantitative Practice](../09-ethical-and-responsible-analytics/README.md) —
  the reporting standards that a Bayesian workflow must meet.
