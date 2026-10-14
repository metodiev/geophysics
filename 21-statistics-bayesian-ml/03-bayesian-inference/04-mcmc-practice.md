---
id: 21-03-04
title: "MCMC in Practice: Diagnostics, Burn-In, Convergence"
level: research
prereqs: ["21-03-02", "21-03-01"]
estimated_minutes: 75
tags: [bayesian, mcmc, metropolis-hastings, convergence-diagnostics, effective-sample-size]
---

# MCMC in Practice: Diagnostics, Burn-In, Convergence

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** the Metropolis-Hastings acceptance probability and **state** the
   condition on the proposal for it to be valid.
2. **Explain** why a random-walk sampler on a transformed parameter is
   preferable to one on the raw parameter, and **demonstrate** the Jacobian term
   that a missing transform introduces.
3. **Compute** the acceptance rate, the integrated autocorrelation time and the
   effective sample size of a chain.
4. **Compute** split-$\hat R$ across chains and **state** the threshold at which
   convergence is declared.
5. **Diagnose** burn-in, poor mixing and pseudo-convergence, and **state** what
   each looks like in a trace.
6. **State** what MCMC diagnostics can and cannot detect.

The target in this lesson is a **SYNTHETIC** conjugate posterior for a Poisson
rate with a stated prior, so the exact answer is known and every diagnostic can
be checked. No measured value is used.

## Prerequisites

- [21-03-02 Conjugate Priors and Analytic Posteriors](02-conjugate-priors.md) —
  the exact posterior used to validate the sampler.
- [21-03-01 The Bayesian Paradigm and Subjective Probability](01-bayesian-paradigm.md) —
  the posterior the chain is meant to sample.
- [21-01-03 Resampling: Bootstrap, Jackknife, Permutation Tests](../01-statistics-in-practice/03-resampling.md) —
  Monte-Carlo error, which is what an effective sample size measures.

## 1. Intuition: a random walk that visits the posterior

Markov-chain Monte Carlo builds a sequence of parameter values whose long-run
distribution is the posterior. The workhorse is **Metropolis-Hastings**: propose
a move, accept it with a probability that depends on the ratio of the target
densities, and repeat. Nothing is integrated and nothing is normalised — only
ratios of the target density are needed, which is why MCMC works for posteriors
whose normalising constant is unknown.

The price is that the samples are **correlated**. A chain that moves in small
steps produces many nearly identical samples, so the *effective* sample size is
far below the number of iterations. All the diagnostics in this lesson measure
that gap, and all of them are checks on the *sampler*, not on the *model*.

## 2. The algorithm and its validity

For a target density $\pi(\theta)$ and a proposal density $q(\theta' \mid
\theta)$, the Metropolis-Hastings step accepts the proposal $\theta'$ with
probability

$$\alpha = \min\!\left(1,\
\frac{\pi(\theta')\,q(\theta \mid \theta')}{\pi(\theta)\,q(\theta' \mid
\theta)}\right).$$

When $q$ is symmetric — a random walk, $q(\theta'\mid\theta) = \mathcal N(\theta,
s^{2})$ — the proposal ratio cancels and $\alpha = \min(1,
\pi(\theta')/\pi(\theta))$, the **Metropolis** rule. The chain has $\pi$ as its
stationary distribution, so after a transient its samples are distributed as the
posterior. Two practical consequences follow immediately:

- **Sample on a transformed scale when the parameter is positive.** Sampling on
  $\log\theta$ needs the Jacobian: the target for $\log\theta$ is
  $\pi(\theta)\,\theta$, so the log-density must be augmented by $\log\theta$.
  Omitting it silently samples a *different* distribution — in this lesson's
  case $\mathrm{Gamma}(\alpha-1, \beta)$ instead of
  $\mathrm{Gamma}(\alpha, \beta)$, a mean shift of $3.3\ \%$.
- **Tune the proposal scale.** Too small and the chain crawls with a high
  acceptance rate; too large and it rejects almost always.

## 3. Diagnostics that matter

**Acceptance rate.** Informative but not a target in itself. For a one-dimensional
random walk on a transformed parameter, a rate near $0.4$–$0.5$ is efficient; the
famous $0.234$ figure is the asymptotic optimum for high-dimensional targets.

**Autocorrelation time.** With $\rho_k$ the autocorrelation of the chain at lag
$k$,

$$\tau_{\text{int}} = 1 + 2\sum_{k\ge1}\rho_k, \qquad
N_{\text{eff}} = \frac{N_{\text{steps}}}{\tau_{\text{int}}} .$$

Truncating the sum at the first non-positive $\rho_k$ (the initial-positive
sequence rule) gives the estimate used in the demonstration.

**$\hat R$.** Run $m$ chains from dispersed starting points and compare the
between-chain and within-chain variances:

$$\hat R = \sqrt{\frac{W\,(L-1)/L + B/L}{W}}$$

with $W$ the mean within-chain variance and $B = L\,\operatorname{var}(\bar
\theta_c)$ the between-chain variance. $\hat R \to 1$ as the chains mix;
$\hat R < 1.01$ is the conventional threshold, and it is a statement about
**all** the chains agreeing, not about any one of them.

**Burn-in.** The initial transient, discarded before inference. Judge it by
comparing the first segment's mean with the rest and, better, by starting chains
from over-dispersed points and checking that they agree: if a chain started far
from the mode converges to the same place, the transient is over.

## 4. What diagnostics cannot see

$\hat R$ and $\tau_{\text{int}}$ compare chains and lags within the model. They
cannot detect

- **a multi-modal posterior** explored by one mode only, when all chains start in
  the same basin;
- **an incorrect target**, such as the missing Jacobian above, because all chains
  agree on the wrong answer;
- **a mis-specified model**, because the posterior is exactly the model's
  posterior.

The remedy for the first is over-dispersed starts plus a prior that does not
forbid the other mode; for the second, a correctness test against a known
distribution — which is exactly why this lesson uses a conjugate target.

## 5. Worked example

The demonstration samples the posterior for a Poisson rate given $28$ events in
$10$ intervals, a $\mathrm{Gamma}(2, \text{rate }1)$ prior, so the exact
posterior is $\mathrm{Gamma}(30, \text{rate }11)$ with mean $2.727273$ and
standard deviation $0.497930$.

Four chains of $20\,000$ steps start at $\lambda = 0.05$, $0.5$, $3.0$ and $8.0$,
with a random-walk proposal of standard deviation $0.35$ on $\log\lambda$.

| quantity | measured |
|---|---|
| acceptance rates | $0.5272$, $0.5230$, $0.5178$, $0.5122$ |
| lag-1 autocorrelation | $0.6413$ |
| integrated autocorrelation time | $4.8$ steps |
| effective sample size (chain 1, after burn-in) | $3918.3$ of $19000$ |
| Monte-Carlo standard error of the mean | $0.007936$ |
| split-$\hat R$ | $1.00012$ |
| worst chain-mean error against the exact mean | $0.0105$ |

Every diagnostic agrees with the exact answer. The acceptance rate is a healthy
$0.51$–$0.53$, the autocorrelation time of $4.8$ steps means each chain of
$19\,000$ post-burn-in samples is worth about $3918$ independent draws, and the
resulting Monte-Carlo error of the mean, $0.0079$, is $1.6\ \%$ of the posterior
standard deviation. $\hat R = 1.00012$ is far below the $1.01$ threshold.

**Burn-in.** The chains started as far as $8.0$ from a posterior mean of
$2.7273$ — more than ten posterior standard deviations away. Comparing the first
$500$ steps with the next $500$ shows the transient: chain 1's first-segment mean
is $2.5990$ against $2.7853$ for the second, a difference of $0.19$. After
$5000$ steps the worst chain-mean error is $0.0099$, essentially the Monte-Carlo
error of $0.0079$, and no longer falls with more burn-in. Burn-in worked: the
lesson is that it is detected by *disagreement between segments and chains*, not
by a fixed fraction of the run.

## Assumptions and regime of validity

1. **The target is the intended posterior.** A sampler samples what it is given;
   a missing Jacobian or a mis-coded prior produces a confident wrong answer.
2. **$\hat R$ needs dispersed starts.** Chains started in one basin will agree and
   hide a second mode.
3. **$\tau_{\text{int}}$ needs a long chain.** The autocorrelation estimate is
   biased at short lags and noisy at long ones; report $N_{\text{eff}}$, not just
   $N$.
4. **Burn-in is a transient, not a guarantee.** A chain that has not mixed is not
   fixed by discarding more.
5. **Diagnostics are necessary, not sufficient.** Passing $\hat R$ and having a
   plausible trace do not make a wrong target right.
6. **Replications are cheap.** Independent chains with different seeds are the
   strongest single check available.

## The honest summary

MCMC turns integration into sampling, and pays for it with correlated draws whose
effective number must be measured. In this lesson every diagnostic was checked
against an exactly known posterior: the acceptance rate was $0.51$–$0.53$,
$\tau_{\text{int}} = 4.8$ steps reduced $19\,000$ draws to an effective $3918$,
$\hat R = 1.00012$ and the worst chain mean was within $0.0105$ of the truth.
The demonstration also makes the sampler's central hazard concrete: omitting the
$\log\lambda$ Jacobian when sampling on the log scale moves the posterior mean by
$3.3\ \%$ while every diagnostic still looks excellent. What diagnostics
**cannot** do is detect a wrong target — only a comparison with a known answer,
as here, can.

## Python demonstration

[`code/mcmc_practice_demo.py`](./code/mcmc_practice_demo.py) prints every number
quoted above. It:

1. runs four over-dispersed chains of $20\,000$ steps and prints the acceptance
   rates;
2. computes the lag-1 autocorrelation and the integrated autocorrelation time;
3. computes the effective sample size, the Monte-Carlo standard error and
   split-$\hat R$;
4. shows the burn-in transient and its removal.

```bash
cd 21-statistics-bayesian-ml/03-bayesian-inference/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python mcmc_practice_demo.py
```

It runs in about half a second and prints only text.

## Exercises

Graded problems are in
[`exercises/04-mcmc-practice-exercises.md`](./exercises/04-mcmc-practice-exercises.md)
with worked solutions in
[`exercises/04-mcmc-practice-solutions.md`](./exercises/04-mcmc-practice-solutions.md).
The ★★★ problems ask you to design the tuning and pseudo-convergence studies.

## Mastery checkpoint

Without notes, a chain of $19\,000$ post-burn-in samples has
$\tau_{\text{int}} = 4.8$, a posterior standard deviation of $0.497930$ and
split-$\hat R = 1.00012$.

1. Compute the effective sample size and the Monte-Carlo standard error.
2. Compute the acceptance rate you would expect if the proposal standard
   deviation were halved, and state the effect on $\tau_{\text{int}}$.
3. State what a $\hat R$ of $1.0001$ would mean if all four chains had been
   started at $\lambda = 2.7$.
4. State the one diagnostic that would have caught a missing Jacobian.

## Common pitfalls

1. **Omitting the Jacobian on a transformed scale.** It shifted the posterior
   mean by $3.3\ \%$ with no diagnostic complaint.
2. **Reporting the number of iterations as the sample size.** Report
   $N_{\text{eff}}$.
3. **Trusting $\hat R$ from chains started in one place.** They agree on the mode
   they found.
4. **Treating burn-in as a fixed fraction.** Detect the transient from
   segment-to-segment disagreement.
5. **Reading a smooth trace as convergence.** A slowly mixing chain looks smooth
   and is wrong.
6. **Confusing sampler error with model error.** No diagnostic tests the model.

## Where this is used

- **Hierarchical models**: the hyperparameters are rarely conjugate and are
  sampled.
- **Nonlinear inverse problems**: posteriors in tens to thousands of dimensions.
- **Geophysical tomography**: transdimensional samplers that also infer the
  number of parameters.
- **Hazard and source inversion**: posterior distributions for rates and
  mechanisms.
- **Machine learning**: Bayesian neural networks and probabilistic programming
  use the same samplers and the same diagnostics.

## Related lessons

- [21-03-02 Conjugate Priors and Analytic Posteriors](02-conjugate-priors.md) —
  the target used to validate the sampler here.
- [21-03-03 Hierarchical Models and Exchangeability](03-hierarchical-models.md) —
  the models for which sampling is usually required.
- [21-03-05 Variational Inference and Scalable Bayes](05-variational-inference.md) —
  the deterministic alternative to sampling.
- [21-03-06 Bayesian Workflow and Principled Model Building](06-bayesian-workflow.md) —
  where the diagnostics fit into a complete analysis.
- [18-06 Uncertainty Quantification](../../18-inverse-problems/06-uncertainty-quantification/README.md) —
  the inverse-problem setting for these samplers.

## Self-assessment checklist

- [ ] I can write the MH acceptance probability and its symmetric special case.
- [ ] I can state the Jacobian term for a log-scale sampler.
- [ ] I can compute $\tau_{\text{int}}$ and $N_{\text{eff}}$.
- [ ] I can compute split-$\hat R$ and interpret the threshold.
- [ ] I can detect a burn-in transient from the chain's own segments.
- [ ] I can state three failures no diagnostic can detect.
