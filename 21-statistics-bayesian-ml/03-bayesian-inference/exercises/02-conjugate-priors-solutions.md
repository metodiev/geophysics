# Solutions — 21-03-02 Conjugate Priors and Analytic Posteriors

> Read after attempting. Lesson:
> [02 Conjugate Priors](../02-conjugate-priors.md). Numbers quoted from the
> demonstration reproduce its output.

---

## ★1 — Beta(1,3) updated with 4 of 16

$$\mathrm{Beta}(1 + 4,\ 3 + 16 - 4) = \mathrm{Beta}(5, 15).$$

$$\text{mean} = \frac{5}{20} = 0.250000, \qquad
\text{mode} = \frac{5-1}{20-2} = \frac{4}{18} = 0.222222,$$

$$\text{variance} = \frac{5\times15}{20^{2}\times21} = \frac{75}{8400}
= 0.008929 .$$

The maximum-likelihood estimate is $4/16 = 0.25$, and the prior mean is
$1/4 = 0.25$: the two agree, so the posterior mean coincides with both. The
prior-equivalent sample size is $a+b-2 = 2$, giving a posterior that is very
close to the data.

---

## ★2 — Normal-Normal update

$$\frac{1}{\tau_1^{2}} = \frac{1}{\tau^{2}} + \frac{n}{\sigma^{2}}
= \frac{1}{1} + \frac{25}{4} = 1 + 6.25 = 7.25
\;\Longrightarrow\;
\tau_1^{2} = \frac{1}{7.25} = 0.137931, \quad \tau_1 = 0.371392 .$$

$$\mu_1 = \tau_1^{2}\Big(\frac{\mu_0}{\tau^{2}} + \frac{n\bar y}{\sigma^{2}}\Big)
= \frac{3 + 6.25\times3.5}{7.25} = \frac{3 + 21.875}{7.25}
= \frac{24.875}{7.25} = 3.431034 .$$

**Data weight.**

$$w = \frac{n/\sigma^{2}}{1/\tau^{2} + n/\sigma^{2}} = \frac{6.25}{7.25}
= 0.862069 .$$

**Shrinkage.** $\mu_1 - \bar y = 3.431034 - 3.5 = -0.068966$, i.e. the estimate
is pulled towards the prior mean $3$ by $6.9\ \%$ of the $0.5$ gap between the
sample mean and the prior. In standard-error units the posterior is
$(3.431 - 3)/0.371 = 1.16$ from the prior mean and $(3.5 - 3.431)/0.371 = 0.19$
from the data — both plausible, and the posterior sits between them as the
precision weighting requires.

---

## ★3 — Gamma-Poisson update

$$\lambda \mid y \sim \mathrm{Gamma}(3 + 8,\ \text{rate } 2 + 4)
= \mathrm{Gamma}(11, \text{rate } 6).$$

$$\text{mean} = \frac{11}{6} = 1.833333, \qquad
\text{sd} = \frac{\sqrt{11}}{6} = \frac{3.316625}{6} = 0.552771 .$$

The maximum-likelihood estimate is $8/4 = 2.000$, so the prior pulls the estimate
**down** by $8.3\ \%$. The prior acts like $3$ prior events over $2$ prior
intervals of exposure; with only four observed intervals that pseudo-data is
still a substantial fraction of the evidence.

---

## ★★4 — Deriving the Normal-Normal posterior

With $\mu \sim \mathcal N(\mu_0,\tau^{2})$ and
$\bar y \sim \mathcal N(\mu, \sigma^{2}/n)$, the log posterior is

$$-2\ln p(\mu\mid\bar y) = \frac{(\mu - \mu_0)^{2}}{\tau^{2}}
+ \frac{(\bar y - \mu)^{2}}{\sigma^{2}/n} + \text{const}.$$

Expand and collect the terms in $\mu$:

$$= \mu^{2}\Big(\frac{1}{\tau^{2}} + \frac{n}{\sigma^{2}}\Big)
- 2\mu\Big(\frac{\mu_0}{\tau^{2}} + \frac{n\bar y}{\sigma^{2}}\Big)
+ \text{const}.$$

This is a quadratic in $\mu$ with coefficient
$P = 1/\tau^{2} + n/\sigma^{2}$ on $\mu^{2}$ and $-2Q$ on $\mu$, so the
posterior is Gaussian with

$$\frac{1}{\tau_1^{2}} = P = \frac{1}{\tau^{2}} + \frac{n}{\sigma^{2}},
\qquad
\mu_1 = \frac{Q}{P}
= \frac{\mu_0/\tau^{2} + n\bar y/\sigma^{2}}{1/\tau^{2} +
n/\sigma^{2}} .$$

Completing the square is the whole derivation: the posterior precision is the
sum of the precisions, and the posterior mean is the precision-weighted average.
No integration is needed because the quadratic form is self-normalising.

---

## ★★5 — Limits of the update

$$P = \frac{1}{\tau^{2}} + \frac{n}{\sigma^{2}}
\;\Longrightarrow\;
\tau_1^{2} = \frac{1}{P} = \frac{\tau^{2}\sigma^{2}}{\sigma^{2} + n\tau^{2}} .$$

As $n \to \infty$, $\tau_1^{2} \to \sigma^{2}/n$ and
$\mu_1 \to \bar y$: with enough data the prior is irrelevant. But the convergence
is at the rate $1/n$ in precision, so a prior with precision $1/\tau^{2}$
contributes an equivalent of $\sigma^{2}/\tau^{2}$ observations. In the
demonstration's case ($\sigma^{2} = 1$, $\tau^{2} = 1$) the prior is worth one
observation and is negligible at $n = 10$; a prior with $\tau = 0.1$ would be
worth $100$ observations and would dominate at $n = 10$.

The practical statement: **a prior of finite precision is never forgotten, only
outvoted**, and the number of observations needed to outvote it is
$\sigma^{2}/\tau^{2}$.

---

## ★★6 — Predictive distributions

**One future observation.** The predictive variance is the posterior variance
plus the sampling variance:

$$\operatorname{Var}(\tilde y) = \tau_1^{2} + \sigma^{2} = 0.090909 + 1.0
= 1.090909, \qquad \text{sd} = 1.044465 .$$

**The mean of ten future observations.** Each has sampling variance
$\sigma^{2}/10 = 0.1$ around the same $\mu$, so

$$\operatorname{Var}(\bar{\tilde y}_{10}) = \tau_1^{2} + \frac{\sigma^{2}}{10}
= 0.090909 + 0.1 = 0.190909, \qquad \text{sd} = 0.436934 .$$

The single-observation predictive is wider by a factor
$1.044465/0.436934 = 2.39$, and both are wider than the posterior standard
deviation $0.301511$. The predictive answers "what will I observe?"; the
posterior answers "what is the parameter?". Reporting the posterior where a
forecast is required understates the spread by a factor of $3.5$ for one
observation, which is the largest single source of over-confidence in Bayesian
forecasting.

---

## ★★★7 — Unknown variance and the widening of the interval

**Prior.** $\mu \mid \sigma^{2} \sim \mathcal N(\mu_0, \sigma^{2}/\kappa_0)$ and
$\sigma^{2} \sim \mathrm{InvGamma}(\alpha_0, \beta_0)$ — the Normal-inverse-gamma
conjugate prior — with weakly informative settings
$\kappa_0 = 1$, $\alpha_0 = \beta_0 = 0.01$.

**Marginal posterior.** Integrating out $\sigma^{2}$ gives a **Student-t** for
$\mu$ with $\nu = 2\alpha_0 + n$ degrees of freedom, scale
$\sqrt{\beta_n/(\alpha_n\kappa_n)}$ and centre $\mu_n$. The credible interval is
$\mu_n \pm t_{0.975,\nu}\times\text{scale}$.

**Design.** Sample sizes $n \in \{5, 10, 20, 50, 100\}$; $M = 2000$ synthetic
data sets per size with unit true variance; compare the width of the
$95\ \%$ credible interval under the known-variance update with that under the
Normal-inverse-gamma update.

**Prediction.** At $n = 5$ the unknown-variance interval is wider by a factor of
about **$1.6$**, because $t_{0.975, 5} = 2.571$ against the normal $1.960$ and
the scale also carries the variance uncertainty. At $n = 100$ the factor falls to
about **$1.02$**, since $t_{0.975,100} = 1.984$ against $1.960$. The headline is
the widening factor as a function of $n$: pretending the variance is known is a
material over-confidence at small $n$, and the honest model uses the $t$
distribution.

---

## ★★★8 — Simulation-based calibration

**Model.** The Beta-Binomial: $\theta \sim \mathrm{Beta}(2,2)$, then
$k \sim \mathrm{Binomial}(n = 20, \theta)$.

**Procedure.** For $L = 1000$ replicates: draw $\theta^{(\ell)}$ from the prior;
draw $k^{(\ell)}$; draw $S = 500$ samples from the posterior
$\mathrm{Beta}(2+k^{(\ell)}, 22-k^{(\ell)})$; compute the rank
$r^{(\ell)} = \#\{s : \theta^{(\ell)}_s < \theta^{(\ell)}\}$.

**Metric.** The histogram of the $L$ ranks, each divided by $S+1$.

**Prediction under a correct posterior.** The ranks are **uniformly
distributed** on $\{0,\dots,S\}$ — a flat histogram, since by construction the
prior draw is exchangeable with the posterior draws. A systematic excess of
low ranks means the posterior is too **narrow** (over-confident); an excess of
high ranks means too **wide**. With $L\times S = 500\,000$ comparisons, a
departure of $2\ \%$ from flatness is resolved at about $3\sigma$, so $L = 1000$
is ample. Uniformity of ranks is the sharpest available check that a posterior
sampler and its normalisation are mutually consistent.
