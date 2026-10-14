---
id: 21-01-02
title: "Choosing Probability Models for Earth Data"
level: doctoral
prereqs: ["01-13-04", "01-13-06"]
estimated_minutes: 60
tags: [statistics, probability-models, lognormal, heavy-tails, model-selection, extreme-values]
---

# Choosing Probability Models for Earth Data

## Learning objectives

By the end of this lesson you will be able to:

1. **Distinguish** a parametric family from the data it describes, and
   **state** what a fitted parameter does and does not constrain.
2. **Derive** the mean, variance and skewness of the lognormal distribution and
   **explain** the mean-median gap as a function of the log-scale spread.
3. **Compare** competing families by maximised likelihood, AIC and the
   Kolmogorov-Smirnov distance, and **state** what each criterion rewards.
4. **Compute** a tail probability from two models fitted to the same sample and
   **quantify** how far they disagree beyond the largest observation.
5. **Derive** the block-maxima limit and **fit** a generalised extreme value
   distribution to block maxima.
6. **Decide** when a heavy-tailed family is justified and when it is an artefact
   of too few samples.

Every model and data set in this lesson is **SYNTHETIC**. The "permeability"
values are drawn from a lognormal law with stated parameters and the block
maxima from a standard Gaussian; no measured value is used and no number here
constrains real rock.

## Prerequisites

- [01-13-04 Common Distributions and Their Earth-Science Roles](../../01-mathematics/13-probability-and-statistics-foundations/04-distributions.md) —
  the families whose tails are compared here.
- [01-13-06 Point Estimation, Bias, Consistency and Efficiency](../../01-mathematics/13-probability-and-statistics-foundations/06-estimation-theory.md) —
  maximum likelihood, which produces every fitted parameter below.
- [21-01-01 Descriptive Statistics, Robust Measures and Outliers](01-descriptive-statistics.md) —
  the summaries that motivate a skewed family.

## 1. Intuition: the model is a claim about the tail

A probability model is not a description of your data. It is a claim about what
values you have **not** seen, extrapolated from what you have. Two families that
fit the body of a sample equally well can disagree by orders of magnitude about
the probability of exceeding the largest observation, and that disagreement is
the entire content of the model choice.

Earth data make this concrete. Petrophysical properties are positive, multiply
rather than add, and are bounded below by zero; the lognormal is the natural
first guess. Hazard quantities are maxima over a season, and their theory is the
extreme-value family, not the Gaussian. The Gaussian is the default only because
it is convenient, and a model choice made for convenience must be defended by a
diagnostic — not asserted by habit.

## 2. Likelihood, selection and what each criterion rewards

For an i.i.d. sample $\{x_i\}$ and a family with density $f(x;\theta)$, the
log-likelihood is $\ell(\theta) = \sum_i \ln f(x_i;\theta)$, and the maximum
likelihood estimate is $\hat\theta = \arg\max_\theta \ell(\theta)$. The
**Akaike information criterion** is

$$\mathrm{AIC} = 2k - 2\ell(\hat\theta),$$

where $k$ is the number of free parameters. The first term charges for
flexibility; the second rewards fit. Comparing families with a different $k$ by
the raw likelihood alone always favours the larger family, which is why $2k$ is
there.

A **goodness-of-fit** statistic answers a different question. The
Kolmogorov-Smirnov distance

$$D = \sup_x \big| \hat F_n(x) - F(x;\hat\theta) \big|$$

measures the largest gap between the empirical and fitted CDFs. It is a
diagnostic of absolute fit, not a comparison between two families, and its
$p$-value is not valid when $\hat\theta$ is estimated from the same sample — the
demonstration therefore quotes $D$, not a KS $p$-value.

## 3. The Gaussian and its tail

The Gaussian density is $f(x) = (2\pi\sigma^2)^{-1/2}\exp(-(x-\mu)^2/2\sigma^2)$,
with the far tail $P(X > x) \approx \phi(z)/z$ for $z = (x-\mu)/\sigma$. The
failure that matters in geophysics is not the symmetry; it is the decay. The
hazard function of the Gaussian *increases* without bound, so the Gaussian
understates the chance of large values for any quantity whose tail is genuinely
heavier.

## 4. The lognormal family

If $Y = \ln X \sim \mathcal N(\mu_{\ln}, \sigma_{\ln}^2)$ then $X$ is lognormal
with median $e^{\mu_{\ln}}$ and closed-form moments

$$\mathbb E[X] = e^{\mu_{\ln} + \sigma_{\ln}^2/2}, \qquad
\operatorname{Var}(X) = \big(e^{\sigma_{\ln}^2}-1\big)e^{2\mu_{\ln}+\sigma_{\ln}^2},$$

$$\text{skewness}(X) = \big(e^{\sigma_{\ln}^2}+2\big)\sqrt{e^{\sigma_{\ln}^2}-1}.$$

The median is $e^{\mu_{\ln}}$ regardless of $\sigma_{\ln}$, while the mean grows
like $e^{\sigma_{\ln}^2/2}$: the mean-median ratio is exactly
$e^{\sigma_{\ln}^2/2}$. The skewness depends only on $\sigma_{\ln}$ and is
$6.185$ at $\sigma_{\ln} = 1$.

## 5. Heavy tails and the extreme-value limit

Maxima do not follow the body's law. For i.i.d. $X_i$ with CDF $F$ and
$M_n = \max(X_1,\dots,X_n)$, if a non-degenerate limit for $(M_n - a_n)/b_n$
exists it is the **generalised extreme value** distribution

$$G(z) = \exp\!\left\{-\Big[1 + \xi\,\frac{z-\mu}{\sigma}\Big]^{-1/\xi}\right\},
\qquad 1 + \xi\frac{z-\mu}{\sigma} > 0,$$

with $\xi \to 0$ giving the Gumbel case $G(z) = \exp\{-e^{-(z-\mu)/\sigma}\}$.
The Gaussian $F$ is in the Gumbel domain ($\xi = 0$), so block maxima of Gaussian
data should fit a Gumbel law, and the return level for a $T$-block period solves
$G(z_T) = 1 - 1/T$. The scale of the limit is set by the normalising constant
$\sqrt{2\ln n}$ for Gaussian blocks. Fitting this family to block maxima is the
subject of [21-01-07 Extreme Value Theory](07-extreme-value-theory.md).

## 6. Worked example: two models on one skewed sample

The demonstration draws $n = 4000$ lognormal values with median
$100\ \mathrm{mD}$ and $\sigma_{\ln} = 1$.

**Moments.** The exact values are $\mathbb E[X] = e^{0.5} \times 100 = 164.87\
\mathrm{mD}$, $\sigma = 216.12\ \mathrm{mD}$ and skewness $6.185$. The sample
gives $162.26\ \mathrm{mD}$, $209.30\ \mathrm{mD}$ and $6.527$ — each within the
sampling scatter, since the standard error of the mean is
$\sigma/\sqrt n = 216.12/63.25 = 3.42\ \mathrm{mD}$.

**Selection.** The Gaussian fit has $\ell = -27050.2$, AIC $= 54104.5$ and
$D = 0.2262$. The lognormal fit has $\ell = -24047.4$, AIC $= 48100.8$ and
$D = 0.0092$, with $\hat\sigma_{\ln} = 0.996$ against the true $1.000$. The AIC
difference is $6003.6$ in favour of the lognormal — and the KS distance is
$0.2262/0.0092 = 24.6$ times smaller, which shows the two criteria agree here but
answer different questions.

**The tail.** The fraction of the sample above $1000\
\mathrm{mD}$ is $0.00900$ ($36$ of $4000$). The normal model predicts
$3.125\times10^{-5}$ — smaller than the empirical value by a factor of $288$, and
smaller than the lognormal prediction by $324.8$. Neither probability is
constrained by the data beyond the largest observation, $5199.7\ \mathrm{mD}$:
everything past that number is model.

**Block maxima.** Taking $1500$ blocks of $50$ standard normals gives block
maxima whose fitted GEV shape is $\hat\xi = +0.1277$. The Gumbel limit for
Gaussian blocks is $\xi = 0$, and the fitted value differs because a finite
sample of $1500$ maxima carries an uncertainty of order $0.05$ in $\xi$; the
point is that $\hat\xi$ is estimated, not asserted. The fitted return levels for
periods of $10$, $100$ and $1000$ blocks are $2.8167$, $3.4306$ and $3.8782$ in
standard-normal units, and the observed maximum over $75\,000$ values is
$4.5717$ against the asymptotic normaliser $\sqrt{2\ln n} = 4.7382$.

## Assumptions and regime of validity

1. **Independence.** Every likelihood and every AIC above assumes i.i.d.
   samples. Spatially or temporally correlated data inflate the effective
   sample size; the fit is then over-confident.
2. **The family must be physically admissible.** A lognormal asserts positivity
   and multiplicative structure; fitting it to a signed anomaly is a category
   error.
3. **AIC compares, it does not validate.** The best of two wrong families is
   still wrong; use the KS distance as a fit diagnostic alongside it.
4. **The tail is extrapolation.** The sample constrains probabilities only up
   to its largest observation. Beyond that, the model's shape decides, and the
   shape is the least well-estimated parameter.
5. **Block-maxima theory needs large blocks.** The GEV limit requires the block
   maximum to be an extreme; with $50$ blocks it is an approximation whose error
   is of the same order as $\hat\xi$ itself.

## The honest summary

A probability model is a wager about unobserved values, and the wager is paid in
the tail. On the synthetic sample above, a Gaussian and a lognormal fitted to the
same $4000$ values disagree by a factor of $325$ about a probability that the
data can barely see. Model choice therefore must be argued from the physics of
the generating process and reported with a diagnostic; a single number — a mean,
a quantile, a return level — inherits the model's tail assumption whether the
analyst states it or not. What the numbers here do **not** constrain is the tail
of any real permeability distribution: that requires a sample large enough to
observe the tail, which the demonstration deliberately does not provide.

## Python demonstration

[`code/probability_models_earth_demo.py`](./code/probability_models_earth_demo.py)
prints every number quoted above. It:

1. compares sample moments with the lognormal closed forms;
2. fits the normal and the lognormal and prints log-likelihood, AIC and KS;
3. prints the tail probability above $1000\ \mathrm{mD}$ from each model;
4. generates block maxima and fits a GEV, printing $\hat\xi$ and three return
   levels.

```bash
cd 21-statistics-bayesian-ml/01-statistics-in-practice/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python probability_models_earth_demo.py
```

It runs in about half a second and prints only text.

## Exercises

Graded problems are in
[`exercises/02-probability-models-earth-exercises.md`](./exercises/02-probability-models-earth-exercises.md)
with worked solutions in
[`exercises/02-probability-models-earth-solutions.md`](./exercises/02-probability-models-earth-solutions.md).
The ★★★ problems ask you to design the model-selection experiment.

## Mastery checkpoint

Without notes, a sample of $4000$ permeability values has sample mean
$162.3\ \mathrm{mD}$, median $98.9\ \mathrm{mD}$ and skewness $6.53$.

1. Compute the implied $\sigma_{\ln}$ from the mean-median ratio and from the
   skewness, and state whether the two agree.
2. Compute the lognormal theoretical mean and standard deviation for that
   $\sigma_{\ln}$, and compare them with the sample values.
3. State the AIC penalty the Gaussian pays for having one fewer parameter, and
   explain why it does not change the conclusion here.
4. Your colleague reports $P(X > 3000\ \mathrm{mD}) = 10^{-4}$ from the fitted
   lognormal. What must accompany that number?

## Common pitfalls

1. **Fitting a Gaussian because it is convenient.** On positive, multiplicative
   data the Gaussian misstates the tail by orders of magnitude.
2. **Comparing likelihoods without the parameter penalty.** A larger family
   always fits better in-sample; that is not evidence.
3. **Reporting a KS $p$-value after estimating parameters.** The standard
   $p$-value assumes a fully specified null and is anti-conservative here.
4. **Quoting a tail probability as if it were observed.** Above the largest
   observation it is an extrapolation, and the extrapolation is model-driven.
5. **Reading $\hat\xi$ as physics.** For Gaussian blocks the truth is $\xi = 0$;
   a finite-sample estimate near $0.13$ shows the estimator's noise, not a new
   mechanism.
6. **Mixing a body model with a hazard question.** A return level is a
   block-maxima quantity; fitting the body distribution and transforming is
   wrong unless the transformation is derived.

## Where this is used

- **Petrophysics**: permeability and porosity distributions, and the choice of
  a lognormal or a mixture.
- **Geochemistry**: lognormal element concentrations and the detection limits
  that truncate them.
- **Hydrology**: flood and rainfall frequency analysis uses GEV and generalised
  Pareto families directly.
- **Seismology**: magnitude-frequency relations and ground-motion models
  specify a family for the tail.
- **Geodesy**: error models for GNSS residuals choose between Gaussian and
  heavy-tailed laws.
- **Resource estimation**: grade-tonnage curves are integrals against an
  assumed grade distribution.

## Related lessons

- [21-01-01 Descriptive Statistics, Robust Measures and Outliers](01-descriptive-statistics.md) —
  the summaries the model must reproduce.
- [21-01-07 Extreme Value Theory for Geohazards](07-extreme-value-theory.md) —
  the full treatment of the block-maxima and threshold-exceedance families.
- [21-01-05 Nonparametric Statistics and Kernel Density Estimation](05-nonparametric-methods.md) —
  what to do when no family is defensible.
- [21-02-01 Regionalised Variables and Spatial Continuity](../02-geostatistics/01-regionalized-variables.md) —
  the spatial version of the same distributional assumptions.
- [01-13-04 Common Distributions and Their Earth-Science Roles](../../01-mathematics/13-probability-and-statistics-foundations/04-distributions.md) —
  the catalogue these models are drawn from.

## Self-assessment checklist

- [ ] I can write the lognormal moments and the mean-median ratio.
- [ ] I can compare two families by AIC and by a fit diagnostic.
- [ ] I can state what the KS distance does and does not test.
- [ ] I can fit a GEV to block maxima and interpret the shape parameter.
- [ ] I can say which region of the sample a reported tail probability is
      extrapolating into.
- [ ] I can name the assumption that makes a fitted tail credible.
