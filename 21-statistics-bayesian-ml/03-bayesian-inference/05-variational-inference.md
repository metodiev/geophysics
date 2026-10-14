---
id: 21-03-05
title: "Variational Inference and Scalable Bayes"
level: research
prereqs: ["21-03-04", "21-03-02"]
estimated_minutes: 75
tags: [bayesian, variational-inference, elbo, mean-field, kl-divergence]
---

# Variational Inference and Scalable Bayes

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the variational objective and **derive** the evidence lower bound
   (ELBO) from the KL divergence.
2. **Write** the mean-field factorisation and the coordinate-ascent (CAVI)
   updates for a Gaussian approximation.
3. **Compute** the ELBO, verify it is a lower bound on the log evidence, and
   **report** the KL divergence to the true posterior.
4. **Explain** why a factorised approximation under-estimates posterior variance
   and **quantify** it with numbers.
5. **Compare** variational inference with MCMC on accuracy, cost and what each
   can and cannot deliver.
6. **Diagnose** the failure modes: variance collapse, mode seeking and an
   underestimated posterior used as if it were exact.

The problem in this lesson is **SYNTHETIC** and linear-Gaussian, so the exact
posterior is available and every approximation error can be measured. No measured
value is used.

## Prerequisites

- [21-03-04 MCMC in Practice: Diagnostics, Burn-In, Convergence](04-mcmc-practice.md) —
  the sampling alternative and its cost.
- [21-03-02 Conjugate Priors and Analytic Posteriors](02-conjugate-priors.md) —
  the Gaussian posterior used for validation here.
- [21-01-05 Nonparametric Statistics and Kernel Density Estimation](../01-statistics-in-practice/05-nonparametric-methods.md) —
  the bias-variance trade in an approximation, seen earlier for densities.

## 1. Intuition: turn integration into optimisation

MCMC is exact in the limit but slow: each sample costs a pass over the data, and
the samples are correlated. Variational inference replaces sampling with
optimisation. Choose a family of tractable distributions $q_\phi(\theta)$, and
find the member that is closest to the posterior in KL divergence. Inference
becomes an optimisation over $\phi$, which can be done by gradient descent, on
mini-batches, with the same machinery as deep learning.

The price is that the answer is only as good as the family. A factorised
$q(\theta) = \prod_i q_i(\theta_i)$ cannot represent correlations, so it returns
an answer that is confidently wrong in a specific, predictable way — it
under-estimates variance and can concentrate on one mode of a multi-modal
posterior. Knowing the direction of the error is what makes the method usable.

## 2. The ELBO

Minimising $\mathrm{KL}(q \,\|\, p(\cdot\mid y))$ over $q \in \mathcal Q$ is
equivalent to maximising the **evidence lower bound**

$$\mathcal L(q) = \mathbb E_q\big[\ln p(\theta, y)\big] -
\mathbb E_q\big[\ln q(\theta)\big]
= \mathbb E_q\big[\ln p(y\mid\theta)\big] +
\mathbb E_q\big[\ln p(\theta)\big] - \mathbb E_q\big[\ln q(\theta)\big],$$

because

$$\ln p(y) = \mathcal L(q) + \mathrm{KL}\big(q \,\|\, p(\cdot\mid y)\big)
\ge \mathcal L(q).$$

The gap between the ELBO and $\ln p(y)$ is exactly the KL divergence, so the ELBO
is both the objective and the diagnosis: if a closed-form $\ln p(y)$ is
available, the remaining error is known rather than assumed.

## 3. Mean-field CAVI

Take $\mathcal Q$ to be all products of independent factors. The optimal factor
for coordinate $i$ satisfies

$$\ln q_i^{*}(\theta_i) = \mathbb E_{-i}\big[\ln p(\theta, y)\big] + \text{const},$$

which is exact and self-consistent, so it can be iterated — **coordinate ascent
variational inference**, CAVI. For the linear-Gaussian model of this lesson,
$y = A\theta + e$ with $e \sim \mathcal N(0, \sigma^{2}I)$ and a
$\mathcal N(0, I)$ prior, the updates are

$$v_i \leftarrow \Big(1 + \frac{1}{\sigma^{2}}\sum_{\text{obs}}\sum_k A_{ki}^{2}
\Big)^{-1}, \qquad
m_i \leftarrow v_i\,\frac{1}{\sigma^{2}}\sum_{\text{obs}}\sum_k A_{ki}
\Big(y_k - \sum_{j \ne i} A_{kj} m_j\Big).$$

Apart from the mean-field term, this is the Gaussian conjugate update: the
precision of each coordinate is the prior precision plus the data precision,
and the mean solves the normal equations with the other coordinates held at
their current expectations.

## 4. What the factorisation costs

If the true posterior has correlation $\rho$ between two coordinates, a
factorised $q$ sets it to zero, and the KL divergence is minimised by shrinking
both variances. For a bivariate Gaussian the exact result is

$$v_{\text{MF}} = v_{\text{true}}\quad\text{only if }\rho = 0; \qquad
v_{\text{MF}} \to v_{\text{true}}(1-\rho^{2})\ \text{in the strong-correlation
limit},$$

so the mean-field variance is smaller than the true marginal variance by roughly
$1-\rho^{2}$ when the correlation is strong. The **mean is unbiased** (for a
Gaussian, factorisation does not move the mode), and the error appears entirely
in the variance — which is the worst possible place for a risk statement.

Two consequences worth stating together:

- **The approximation is not conservative.** It under-states uncertainty, so a
  decision based on it is over-confident, not merely imprecise.
- **The error is diagnosable if the truth is known.** Comparing the mean-field
  variance with an MCMC estimate on a small version of the problem is the
  standard calibration step before scaling up.

## 5. Worked example

The demonstration solves a two-parameter linear-Gaussian problem:
$y = A\theta + e$ with
$A = \begin{bmatrix}1 & 0.9\\ 0.9 & 1\end{bmatrix}$, five replicate
observations, $\sigma = 1$ and a $\mathcal N(0, I)$ prior. The design is strongly
correlated, which is the case that exposes mean field.

**The exact posterior.** The precision matrix is
$\big(\begin{smallmatrix}10.05 & 9.00\\ 9.00 & 10.05\end{smallmatrix}\big)$,
so the posterior correlation is $-0.8955$ and the exact marginal standard
deviations are $0.70883$ and $0.70883$. The exact log evidence is
$\ln Z = -15.88319$.

**Mean-field CAVI.** The update converges to means $[+0.13293, +0.69066]$ —
identical to the exact posterior means to the printed precision — and standard
deviations $0.31544$ and $0.31544$. The ratio to the truth is

$$\frac{\sigma_{\text{MF}}}{\sigma_{\text{true}}}
= \frac{0.31544}{0.70883} = 0.44502,$$

so the mean-field approximation reports **$44.5\ \%$** of the true posterior
standard deviation. With a correlation of $-0.8955$, the predicted factor
$\sqrt{1-\rho^{2}} = \sqrt{1-0.802} = 0.445$ matches the measured ratio to three
decimal places — the theory of §4 is exact here.

**The ELBO.** The bound rises from $-17.07352$ after the first sweep to
$-16.70000$ after ten, and converges to $-16.69283$. The exact log evidence is
$-15.88319$, so

$$\mathrm{KL}\big(q \,\|\, p(\cdot\mid y)\big) = \ln Z - \mathcal L
= -15.88319 + 16.69283 = 0.80964,$$

a strictly positive number, as it must be. The optimiser reduced the KL to
$0.81$ nats and stopped, because the factorised family contains nothing closer.
A full-covariance Gaussian would have achieved $\mathrm{KL} = 0$; the residual is
entirely the cost of the independence assumption.

## Assumptions and regime of validity

1. **The family must contain a good approximation.** A factorised Gaussian cannot
   represent skew, bounds or multi-modality; the answer is the best member of a
   family that may not fit.
2. **The ELBO must be computable or estimable with low variance.** High-variance
   gradient estimates need variance reduction (reparameterisation, control
   variates).
3. **Mode seeking is not mode finding.** Optimisation converges to one
   configuration; a multi-modal posterior yields one mode and a falsely narrow
   interval.
4. **The variance is biased low.** Quantify it against a sampler before relying
   on a credible interval.
5. **The mean is usually fine.** For unimodal exponential-family posteriors the
   mean-field mean is a good point estimate; the failure is in the spread.
6. **Scaling is the point.** Mini-batch stochastic gradients are what make
   variational inference feasible on data too large for MCMC, and the
   approximation error is the price.

## The honest summary

Variational inference converts a sampling problem into an optimisation problem
and returns an answer that is fast, deterministic and systematically
over-confident. The demonstration measured that bias exactly: a mean-field
Gaussian reproduced the posterior means to the printed precision while
delivering only $44.5\ \%$ of the true posterior standard deviation, with a KL
gap of $0.81$ nats that no amount of optimisation within the factorised family
could remove. The compensation is cost: the CAVI run is a few hundred matrix
operations, where MCMC would need thousands of correlated draws. What the method
does **not** provide is a warning — the ELBO is a bound, and without a known
truth or an independent sampler to compare against, an over-confident answer
looks exactly like a confident one.

## Python demonstration

[`code/variational_inference_demo.py`](./code/variational_inference_demo.py)
prints every number quoted above. It:

1. computes the exact Gaussian posterior and its log evidence;
2. runs mean-field CAVI and prints the ELBO trajectory;
3. compares the mean-field and exact standard deviations and reports the KL gap.

```bash
cd 21-statistics-bayesian-ml/03-bayesian-inference/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python variational_inference_demo.py
```

It runs in well under a second and prints only text.

## Exercises

Graded problems are in
[`exercises/05-variational-inference-exercises.md`](./exercises/05-variational-inference-exercises.md)
with worked solutions in
[`exercises/05-variational-inference-solutions.md`](./exercises/05-variational-inference-solutions.md).
The ★★★ problems ask you to design the calibration and family-comparison studies.

## Mastery checkpoint

Without notes, a mean-field approximation gives standard deviations
$0.31544$ where the exact posterior has $0.70883$, with an exact correlation of
$-0.8955$ and $\ln Z = -15.88319$ against a converged ELBO of $-16.69283$.

1. Compute the ratio of the standard deviations and compare it with
   $\sqrt{1-\rho^{2}}$.
2. Compute the KL divergence and state why it must be positive.
3. State what the ELBO value would be if the family contained the true posterior.
4. A colleague reports a $95\ \%$ credible interval from the mean-field
   approximation and calls it conservative. State the error.

## Common pitfalls

1. **Reporting a mean-field interval as if it were exact.** It is typically far
   too narrow, by $1-\rho^{2}$ in the strong-correlation limit.
2. **Reading the ELBO as a goodness-of-fit.** It bounds the evidence; a large gap
   means a poor family, not a poor model.
3. **Assuming optimisation found the global optimum of the KL.** CAVI converges to
   a local optimum; over-dispersed restarts are the check.
4. **Ignoring the variance of a stochastic ELBO gradient.** Biased gradients bias
   the answer.
5. **Using a Gaussian family for a bounded parameter.** The interval can extend
   into impossible values.
6. **Skipping calibration.** Without a comparison to a sampler or a known truth,
   the under-statement is invisible.

## Where this is used

- **Large-scale Bayesian inference**: latent-variable models with millions of
  observations.
- **Variational autoencoders**: the ELBO is the training objective.
- **Seismic and geodetic inversions**: fast approximate posteriors for
  operational decisions.
- **Spatial statistics**: variational approximations for Gaussian processes that
  would otherwise be cubic in the number of sites.
- **Probabilistic programming**: automatic differentiation variational inference
  packages.

## Related lessons

- [21-03-04 MCMC in Practice: Diagnostics, Burn-In, Convergence](04-mcmc-practice.md) —
  the accurate but slow alternative.
- [21-03-02 Conjugate Priors and Analytic Posteriors](02-conjugate-priors.md) —
  the exact posteriors that CAVI generalises.
- [21-03-06 Bayesian Workflow and Principled Model Building](06-bayesian-workflow.md) —
  where an approximation error belongs in the report.
- [21-05-05 Autoencoders for Compression and Denoising](../05-deep-learning/05-autoencoders.md) —
  the ELBO as a training loss.
- [18-06 Uncertainty Quantification](../../18-inverse-problems/06-uncertainty-quantification/README.md) —
  the same approximations in inverse problems.

## Self-assessment checklist

- [ ] I can derive the ELBO and state its relation to the KL divergence.
- [ ] I can write the mean-field update for a Gaussian coordinate.
- [ ] I can compute the ELBO gap against a known evidence.
- [ ] I can predict the variance under-estimate from a correlation.
- [ ] I can compare variational inference with MCMC on cost and accuracy.
- [ ] I can name the failure modes that no internal diagnostic reveals.
