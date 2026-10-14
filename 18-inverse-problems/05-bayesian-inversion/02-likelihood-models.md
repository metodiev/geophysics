---
id: 18-05-02
title: "Constructing Likelihoods and Error Models"
level: research
prereqs: ["18-05-01", "18-02-06"]
tags: [inverse-problems, bayesian, uncertainty-quantification, likelihood, error-models, robustness]
---

# Constructing Likelihoods and Error Models

All models and data in this module are **SYNTHETIC**. Every number quoted below
is printed by [`code/likelihood_models_demo.py`](./code/likelihood_models_demo.py)
on the line-shaped teaching data set described in Section 4; none is a
measurement. The module README states the same.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** a likelihood from a stated noise process, and state explicitly which
   physical assumptions each step imports.
2. **Construct** the generalised least-squares likelihood for correlated errors
   and **quantify** the error made by ignoring the correlation.
3. **Derive** the variance inflation factor for the sample mean under an AR(1)
   error process, and use it to predict the direction of the mistake.
4. **Distinguish** Gaussian, Laplace and Student-$t$ likelihoods by their
   influence on a single outlier, and **measure** that influence rather than
   assert it.
5. **Estimate** an unknown noise scale inside the inversion, and explain why the
   resulting likelihood is hierarchical.
6. **Choose** between robust and correlated error models for a stated data type,
   and list the diagnostics that would decide between them.
7. **State** when a likelihood is not identifiable from the data at hand.

## Prerequisites

- [18-05-01 Bayes' Theorem as an Inverse-Problem Formulation](01-bayes-inverse-formulation.md)
  — the posterior as prior times likelihood.
- [18-02-06 Data Weighting and Error Covariance Specification](../02-linear-inverse-problems/06-weighting-and-covariance.md)
  — the weighting matrix $C_d^{-1}$ and what goes into it.
- [18-06-01 Taxonomy of Uncertainty: Aleatory, Epistemic, Structural](../06-uncertainty-quantification/01-uncertainty-taxonomy.md)
  — where the likelihood's randomness sits in a wider taxonomy.

## 1. Intuition: the likelihood is a claim about the residuals

A likelihood is not a formality appended to a forward model; it is the statement
of what the residuals $r_i = d_i - g_i(m)$ would look like if the model were
right. Three questions define it:

- **Scale** — how large are the residuals? (a variance, possibly varying by datum)
- **Shape** — how are they distributed? (Gaussian tails, or heavier?)
- **Dependence** — are they independent between data points? (usually not)

A traditional inversion answers all three by assuming zero-mean, independent,
equal-variance Gaussian noise, which is the same as minimising $\|d-Gm\|^2$. That
is a *choice*, and this lesson measures what it costs when the choice is wrong.
The point is not that the Gaussian assumption is bad; it is that its consequences
are computable, so it can be checked.

## 2. From residual to likelihood

For data $d \in \mathbb{R}^N$, model prediction $g(m)$, and a residual vector
$r(m) = d - g(m)$, a general multivariate Gaussian likelihood is

$$
p(d\mid m) = (2\pi)^{-N/2}\,\lvert C_d\rvert^{-1/2}
\exp\!\left[-\tfrac12 r(m)^{\top} C_d^{-1} r(m)\right].
$$

Everything that matters is in $C_d$: its diagonal sets the per-datum weights, its
off-diagonal elements set the dependence. Two special cases will be used
throughout the module.

**Isotropic.** $C_d = \sigma^2 I$, giving
$-\ln p = \frac{1}{2\sigma^2}\|r\|^2 + \text{const}$ — ordinary least squares.

**Correlated.** $C_d = \sigma^2 R$ with a correlation matrix $R$, giving
generalised least squares with the residual weighted by $R^{-1}$.

### 2.1 Deriving the AR(1) covariance

The simplest useful model of dependence is first-order autoregression: the error
at index $i$ remembers a fraction $\rho$ of the previous one plus an innovation,

$$
e_i = \rho\,e_{i-1} + \eta_i, \qquad \eta_i \sim \mathcal{N}(0,\ \sigma^2(1-\rho^2)),
$$

started from the stationary distribution $e_1 \sim \mathcal{N}(0,\sigma^2)$. Then
$\operatorname{Var}(e_i) = \sigma^2$ for every $i$ and

$$
\operatorname{Cov}(e_i,e_j) = \sigma^2 \rho^{\lvert i-j\rvert}
\quad\Longrightarrow\quad
R_{ij} = \rho^{\lvert i-j\rvert}.
$$

This is the model the demonstration calls `ar1` with $\rho = 0.9$ and
$\sigma = 0.20$. The correlation matrix is banded and strongly non-diagonal:
neighbouring data points share about $81\%$ of their variance. Treating them as
independent is not a small approximation.

### 2.2 Exact variance of a mean under AR(1)

The penalty for that approximation is computable. For the sample mean of $n$
observations with stationary AR(1) errors,

$$
\operatorname{Var}(\bar e) = \frac{\sigma^2}{n^2}\sum_{i=1}^{n}\sum_{j=1}^{n}
\rho^{\lvert i-j\rvert}
= \frac{\sigma^2}{n}\left[1 + 2\sum_{k=1}^{n-1}\left(1-\frac{k}{n}\right)\rho^{k}\right]
\;\xrightarrow[\;n\to\infty\;]{}\;
\frac{\sigma^2}{n}\cdot\frac{1+\rho}{1-\rho}.
$$

At $\rho = 0.9$ the asymptotic inflation factor is $(1+0.9)/(1-0.9) = 19$. The
independent-noise formula $\sigma^2/n$ therefore understates the variance of the
mean by a factor of $19$ in the large-sample limit — a standard error that is
$\sqrt{19} \approx 4.4$ times too small. For a fitted slope over a finite,
non-uniform design the factor is smaller; the demonstration measures it below.

## 3. Heavy tails and robustness

A Gaussian likelihood penalises a residual quadratically. A residual of ten
standard deviations therefore contributes $50$ to $-\ln p$ — large, but the
*derivative* of the penalty with respect to the parameter continues to grow, so a
single bad datum can pull the estimate without limit. Heavy-tailed likelihoods
remove that property.

**Laplace (double exponential).**
$-\ln p = \sum_i \lvert r_i\rvert/\sigma + \text{const}$ — absolute-value
penalty, the $L_1$ misfit of
[18-03-04 Sparsity](../03-regularization/04-sparsity.md), with an influence that
saturates instead of diverging.

**Student-$t$ with $\nu$ degrees of freedom.**
$$
-\ln p = \frac{\nu+1}{2}\sum_i \ln\!\left(1 + \frac{r_i^2}{\nu\sigma^2}\right)
+ \text{const}.
$$
For large $r_i$ the penalty grows only logarithmically. It is the Gaussian mixture

$$
t_\nu(0,\sigma^2) = \int \mathcal{N}(0,\sigma^2/s)\,\mathrm{Gamma}(s;\nu/2,\nu/2)\,
\mathrm{d}s,
$$

which is the standard hierarchical way to write a robust likelihood: each datum
gets its own unknown scale. That structure is what makes it a *model* and not
merely a nonlinear penalty.

## 4. Worked example: three noise processes, three likelihoods

The demonstration fits a straight line $y = a + bx$ to $12$ SYNTHETIC points at
$x = 0,1,\dots,11$ generated from $y = 1.0 + 0.5x$ with three different noise
processes, and integrates the posterior over a $241\times241$ grid in $(a,b)$
under a flat prior. The realised residuals about the truth are already
informative:

| data set | noise process | rms residual about truth |
|---|---|---|
| `iid` | independent Gaussian, $\sigma = 0.20$ | $0.2444$ |
| `ar1` | AR(1), $\rho = 0.90$, $\sigma = 0.20$ | $0.3358$ |
| `outlier` | independent Gaussian plus two $1.2$-unit outliers | $0.5780$ |

The fitted slope and its reported posterior standard deviation under each
likelihood are:

| data set | Gaussian | Laplace | Student-$t$ ($\nu=4$) |
|---|---|---|---|
| `iid` | $0.4895 \pm 0.0167$ | $0.4964 \pm 0.0254$ | $0.4941 \pm 0.0230$ |
| `ar1` | $0.5240 \pm 0.0167$ | $0.5227 \pm 0.0148$ | $0.5236 \pm 0.0168$ |
| `outlier` | $0.4192 \pm 0.0167$ | $0.4579 \pm 0.0208$ | $0.4616 \pm 0.0206$ |

Three things are worth extracting from this table.

**On clean data all three agree, and the Gaussian is the most efficient.** For the
`iid` set the Gaussian slope is $0.4895$ with a standard deviation of $0.0167$;
the robust fits give a slightly different estimate with a *larger* standard
deviation ($0.0254$ and $0.0230$). Robustness is not free: under exactly the
assumed Gaussian model the robust likelihood is the less efficient one. That is
the honest statement of the trade.

**On contaminated data the robust fits are less biased.** The true slope is
$0.5$. The Gaussian likelihood returns $0.4192$, an error of $-0.0808$ — about
five of its own reported standard deviations. Laplace returns $0.4579$ (error
$-0.0421$) and Student-$t$ returns $0.4616$ (error $-0.0384$), halving the bias.
They pay for it with a wider reported interval, $0.0208$ and $0.0206$ against
$0.0167$, which is the correct response: the data are less informative than a
Gaussian likelihood believes.

**The wrong independence assumption is a failure of the interval, not of the
point estimate.** For the `ar1` set, fitting with an independent Gaussian gives
$0.5240 \pm 0.0167$. Fitting the same data with the exact AR(1) covariance
(generalised least squares) gives $0.5340 \pm 0.0213$. The point estimate moves
by $0.010$; the reported uncertainty is understated by a factor of
$\sqrt{0.0213^2/0.0167^2} = 1.27$, i.e. the Gaussian interval is $21\%$ too
narrow. The point estimate and the interval are separate deliverables, and only
the second is broken by an unmodelled correlation.

### 4.1 Measuring influence instead of asserting it

To show what "robust" means quantitatively, the demonstration perturbs a single
datum at $x = 3$ by $\delta$ standard deviations and reports the shift in the
posterior-mean slope, $\Delta b = b(\delta) - b(\delta = 0)$:

| $\delta/\sigma$ | Gaussian $\Delta b$ | Laplace $\Delta b$ | Student-$t$ $\Delta b$ |
|---|---|---|---|
| 1 | $-0.0035$ | $-0.0023$ | $-0.0028$ |
| 2 | $-0.0070$ | $-0.0057$ | $-0.0064$ |
| 4 | $-0.0140$ | $-0.0064$ | $-0.0092$ |
| 8 | $-0.0280$ | $-0.0064$ | $-0.0071$ |
| 16 | $-0.0559$ | $-0.0064$ | $-0.0056$ |

The Gaussian column is proportional to $\delta$: its influence is unbounded, and
doubling the outlier doubles the damage. The robust columns saturate: between
$\delta = 4$ and $\delta = 16$ the Laplace shift does not change at all
($-0.0064$) and the Student-$t$ shift is essentially flat. This is the property
that justifies the word *robust*, and it is a measured curve rather than a
claim. It is also a warning: a robust likelihood "fixes" the outlier by
discarding its information, so if the extreme datum is real structure rather than
a blunder, a robust likelihood will suppress a genuine signal.

## 5. Estimating the noise scale

In practice $\sigma$ is unknown. Treating it as a parameter is not an
afterthought; it makes the likelihood hierarchical:

$$
\sigma \sim \pi(\sigma), \qquad d \mid m,\sigma \sim \mathcal{N}(Gm, \sigma^2 I)
\quad\Longrightarrow\quad
p(m,\sigma\mid d) \propto \frac{1}{\sigma^{N}}\exp\!\left[-\frac{\|d-Gm\|^2}{2\sigma^2}\right]\pi(m)\pi(\sigma).
$$

Note that the usual $1/\sqrt{2\pi\sigma^2}$ factors have become $\sigma^{-N}$,
which is why the prior on a scale parameter matters more than the prior on a
location. With the reference prior $\pi(\sigma)\propto 1/\sigma$ (derived in
[03](03-priors.md)) the SYNTHETIC `iid` data give

$$
\hat\sigma = \sqrt{\text{rss}/N} = 0.2417, \qquad
\mathbb{E}[\sigma\mid d] = 0.2581 \pm 0.0577,
$$

against an injected $\sigma = 0.20$. The posterior mean exceeds the maximum
likelihood value and the injected value exceeds neither: with $N = 12$ the scale
is poorly determined, and the posterior for $\sigma$ is skewed upward. Reporting
the slope with $\sigma$ *fixed* at its maximum-likelihood value would understate
the total uncertainty by ignoring this spread. Propagating it is the subject of
[18-06-02 Monte Carlo Propagation](../06-uncertainty-quantification/02-monte-carlo-uq.md).

### 5.1 Diagnostics that discriminate between error models

The demonstration's three data sets were *chosen*; in real work they must be
diagnosed. The useful tests, in order of increasing strength:

1. **Residual-versus-index plot.** Trend or runs indicate correlation. This is the
   test the `ar1` set fails and the `iid` set passes.
2. **Empirical autocorrelation of residuals.** Compare with the $\pm 1.96/\sqrt N$
   band; lag-1 autocorrelation near $\rho$ is diagnostic.
3. **Residual quantile plot against a normal.** Heavy tails or points far off the
   line indicate a robust likelihood is needed.
4. **Posterior predictive check.** Simulate data from the fitted model and compare
   a chosen statistic — here the rms residual itself — with the observed value. A
   statistic more extreme than $95\%$ of the replicated values falsifies the
   likelihood, not the forward model.

## 6. Worked example: the cost of ignoring correlation, computed

Take the AR(1) model with $\rho = 0.9$. A naive analysis assumes
$\operatorname{Var}(\bar e) = \sigma^2/n$ and reports a standard error of the form
$\sigma/\sqrt{n}$. Using the exact finite-sample expression of Section 2.2 with
$n = 12$ and $\rho = 0.9$:

$$
\sum_{k=1}^{11}\left(1-\frac{k}{12}\right)0.9^{k}
= 0.9(0.9167) + 0.81(0.8333) + 0.729(0.75) + 0.6561(0.6667) + \cdots
\approx 2.36,
$$

so the inflation factor is $1 + 2(2.36) = 5.72$ for the mean. The measured slope
example above gave a factor of only $1.27^2 = 1.61$, because a slope is a
*difference* of observations and differencing removes much of a slowly varying
correlation. That contrast is the practical lesson: correlation inflates the
uncertainty of a mean far more than that of a slope, so the inspection of a
residual sequence must be paired with the quantity actually reported.

## 7. Assumptions and regime of validity

1. **The forward model is unbiased.** A likelihood describes residuals, not
   systematic error. If $g(m)$ is wrong in a structured way, no choice of
   likelihood repairs it; that is model discrepancy, treated in
   [18-06-01](../06-uncertainty-quantification/01-uncertainty-taxonomy.md).
2. **Errors are additive and independent of the model.** A multiplicative error
   model, $d = g(m)\,(1+\epsilon)$, is a different likelihood and would be fitted
   in the log domain.
3. **$C_d$ is positive definite.** A covariance built by hand from an
   autocorrelation function must be checked; the demonstration's AR(1) matrix is
   positive definite for $\lvert\rho\rvert<1$.
4. **The scale is identifiable.** With one datum, $\sigma$ and $m$ cannot both be
   determined; the posterior is then a ridge and only a ratio is meaningful.
5. **Robustness is a statement about influence, not about correctness.** A
   heavy-tailed likelihood down-weights extremes; if the extremes are signal, it
   will discard them.
6. **Gaussianity of the *posterior* is not implied.** Any of these likelihoods
   with a uniform-density prior on $(a,b)$ gives an exactly computable posterior,
   but not a Gaussian one, and its mean and mode differ.

## 8. Demonstration and exercises

[`code/likelihood_models_demo.py`](./code/likelihood_models_demo.py) generates the
three noise realisations, evaluates three likelihoods on a parameter grid, prints
the influence table and the scale inference, and exits $0$ in well under a second.
Exercises and solutions:
[`exercises/02-likelihood-models-exercises.md`](./exercises/02-likelihood-models-exercises.md),
[`exercises/02-likelihood-models-solutions.md`](./exercises/02-likelihood-models-solutions.md).

## Mastery checkpoint

**(a)** Write the likelihood for data with a known variance that grows linearly
with datum index, $C_d = \sigma_0^2\operatorname{diag}(1,2,\dots,N)$. What does
this do to the relative weight of the last datum?
**(b)** For AR(1) errors with $\rho = 0.5$ and $n = 100$, compute the asymptotic
inflation factor of the sample-mean variance.
**(c)** State two measured consequences of fitting an AR(1) data set with an
independent Gaussian likelihood.
**(d)** Give the influence-function behaviour of a Gaussian and a Student-$t$
likelihood as $\lvert r\rvert\to\infty$, and name one risk of using the robust
form.

## Common pitfalls

1. **Assuming independence because the data are sorted.** Ordering is exactly the
   structure that creates correlation.
2. **Reading a small residual as a good likelihood.** A likelihood is judged by
   its calibration, not by the size of the residuals it produces.
3. **Reporting a robust estimate with the Gaussian interval.** The interval must
   come from the same likelihood as the estimate.
4. **Fixing $\sigma$ at its maximum-likelihood value.** This discards the
   uncertainty in $\sigma$ and narrows the posterior on the parameters.
5. **Treating an outlier as noise by default.** Extreme values are sometimes the
   only evidence of a second population.
6. **Optimising a likelihood with a free scale without a prior.** With
   $\pi(\sigma)\propto 1$ (improper) the posterior may be improper; use a
   reference or proper prior and say which.

## Further reading

- **Tarantola, A. (2005). *Inverse Problem Theory and Methods for Model Parameter
  Estimation*. SIAM.** Level: research. Error models and their construction.
- **Gelman, A., Carlin, J. B., Stern, H. S., Dunson, D. B., Vehtari, A., &
  Rubin, D. B. (2013). *Bayesian Data Analysis* (3rd ed.). CRC Press.**
  Level: research. Hierarchical and robust likelihoods, and posterior predictive
  checks.
- **Huber, P. J. (1964). Robust estimation of a location parameter. *Annals of
  Mathematical Statistics*, 35(1), 73–101.** Level: research. The origin of the
  influence-function language used in Section 4.1.

## Related modules

- [01 Bayes' Theorem as an Inverse-Problem Formulation](01-bayes-inverse-formulation.md).
- [03 Priors: Informative, Reference and Their Influence](03-priors.md) — the
  priors on $m$ and on $\sigma$ used here.
- [04 Markov Chain Monte Carlo](04-mcmc.md) — how to sample a posterior when the
  likelihood is non-Gaussian.
- [18-02-06 Data Weighting and Error Covariance Specification](../02-linear-inverse-problems/06-weighting-and-covariance.md).
- [18-06-01 Taxonomy of Uncertainty](../06-uncertainty-quantification/01-uncertainty-taxonomy.md)
  — separating the noise you can model from the structure you cannot.
- [19-07-03 Model Validation](../../19-numerical-modeling-hpc/07-verification-validation-uncertainty/03-model-validation.md)
  — where model discrepancy sits in a simulation code.
