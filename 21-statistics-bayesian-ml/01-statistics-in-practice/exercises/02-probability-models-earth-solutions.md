# Solutions — 21-01-02 Choosing Probability Models for Earth Data

> Read after attempting. Lesson:
> [02 Probability Models](../02-probability-models-earth.md). Numbers quoted from
> the demonstration reproduce its output.

---

## ★1 — Mean-median ratio

$$\frac{\mathbb E[X]}{\operatorname{median}(X)}
= e^{\sigma_{\ln}^2/2} = e^{0.5} = 1.6487 .$$

With median $100\ \mathrm{mD}$,

$$\mathbb E[X] = 100 \times 1.6487 = 164.87\ \mathrm{mD}.$$

The ratio is dimensionless; the mean carries $\mathrm{mD}$. The demonstration's
sample ratio is $162.26/98.88 = 1.641$, within sampling error of $1.6487$.

---

## ★2 — AIC accounting

$$\mathrm{AIC}_{\text{n}} = 2\times2 - 2(-27050.2) = 4 + 54100.4 = 54104.4 ,$$
$$\mathrm{AIC}_{\text{ln}} = 2\times3 - 2(-24047.4) = 6 + 48094.8 = 48100.8 .$$

The lognormal **pays** a penalty of $2$ AIC units (one extra parameter) and
**gains** a likelihood gap of

$$2(\ell_{\text{ln}} - \ell_{\text{n}}) = 2(-24047.4 + 27050.2) = 2\times3002.8
= 6005.6 .$$

Net AIC difference $= 6005.6 - 2 = 6003.6$, which is the demonstration's value.
The penalty is $0.03\ \%$ of the gap: it is decisive only when two families fit
almost equally well, which is exactly the case it was introduced for.

(Small rounding: the demonstration prints $54104.5$; the $0.1$ difference is
rounding of $\ell$ to one decimal.)

---

## ★3 — Lognormal skewness at $\sigma_{\ln} = 1$

$$\text{skew} = (e^{1}+2)\sqrt{e^{1}-1} = (4.71828)\times\sqrt{1.71828}
= 4.71828 \times 1.31082 = 6.1848 .$$

The sample value $6.527$ is $1.34$ in units of the sample's own skewness standard
error ($\sqrt{6/n} = \sqrt{6/4000} = 0.0387$ for a Gaussian reference — an
approximation here because the fourth moment is estimated poorly for a
heavy-tailed law). It is consistent with $\sigma_{\ln} = 1$ and, more
importantly, the closed form says skewness is a function of $\sigma_{\ln}$
alone: measuring $6.5$ pins $\sigma_{\ln} \approx 1.0$ without reference to the
median.

---

## ★4 — Tail probability from the Gaussian

$$z = \frac{1000 - 162.26}{209.30} = \frac{837.74}{209.30} = 4.0026 .$$

$$P(X > 1000) = 1 - \Phi(4.0026) = 3.13\times10^{-5},$$

the demonstration's $3.125\times10^{-5}$.

- Normal versus empirical: $0.00900 / 3.125\times10^{-5} = 288$ — the Gaussian
  understates the observed fraction by a factor of $288$.
- Normal versus lognormal: $0.01015 / 3.125\times10^{-5} = 324.8$.

Unit of the ratio: dimensionless. The Gaussian is not merely slightly off; it is
off by two-and-a-half orders of magnitude on a probability the sample can
actually see.

---

## ★5 — Scaling with $\sigma_{\ln}$

| $\sigma_{\ln}$ | mean-median ratio $e^{\sigma_{\ln}^2/2}$ | skewness |
|---|---|---|
| 0.5 | $e^{0.125} = 1.1331$ | $(e^{0.25}+2)\sqrt{e^{0.25}-1} = 3.284\times0.5335 = 1.752$ |
| 1.0 | $1.6487$ | $6.185$ |
| 2.0 | $e^{2} = 7.389$ | $(e^{4}+2)\sqrt{e^{4}-1} = 56.60\times7.321 = 414.4$ |

The mean-median ratio grows like $e^{\sigma_{\ln}^2/2}$ and the skewness like
$e^{3\sigma_{\ln}^2/2}$: both accelerate. At $\sigma_{\ln} = 2$ the mean sits at
$7.4\times$ the median and the distribution is so skewed that the sample mean is
a poor summary and any tail statement beyond the sample's observed range is
almost entirely model. The extrapolation risk therefore scales roughly with the
square of the log-scale spread.

---

## ★6 — Gumbel versus GEV return levels

Gumbel quantile at the GEV's fitted $\hat\mu$, $\hat\sigma$:

$$z_T = \hat\mu - \hat\sigma\ln\!\big(-\ln(1 - 1/T)\big).$$

- $T = 10$: $-\ln(1-1/10) = 0.10536$, $\ln(0.10536) = -2.2504$, so
  $z_{10} = 2.0285 + 0.4030\times2.2504 = 2.0285 + 0.9069 = 2.9354$.
- $T = 100$: $-\ln(0.99) = 0.010050$, $\ln = -4.6002$, so
  $z_{100} = 2.0285 + 1.8539 = 3.8824$.
- $T = 1000$: $-\ln(0.999) = 0.0010005$, $\ln = -6.9075$, so
  $z_{1000} = 2.0285 + 2.7837 = 4.8122$.

Fitted GEV values: $2.8167$, $3.4306$, $3.8782$. The Gumbel extrapolation is
higher at every period and diverges with $T$ (difference $+0.119$, $+0.452$,
$+0.934$). The fitted $\hat\xi = +0.1277$ bends the upper tail relative to the
Gumbel case, so **evaluating one family's formula at another family's
parameters is not the same as fitting that family**. Report the family and the
parameters together, always.

---

## ★★★7 — Sampling distribution of $\hat\sigma_{\ln}$ and $\hat\xi$

**Estimators.** (i) $\hat\sigma_{\ln}$, the standard deviation of $\ln x$ after
maximum-likelihood fitting. (ii) $\hat\xi$, the shape from
`scipy.stats.genextreme.fit` on block maxima.

**Design.** For sample sizes $n \in \{50, 100, 200, 500, 1000, 5000, 20000\}$
and $M = 2000$ replicates: (i) draw $n$ lognormal values with $\sigma_{\ln}=1$,
compute $\hat\sigma_{\ln}$; (ii) draw $n$ standard normals in blocks of
$\lceil n^{1/3}\rceil$, fit the GEV to the maxima, record $\hat\xi$.

**Metric.** Bias $= \overline{\hat\theta} - \theta$, its own standard error
$\mathrm{sd}(\hat\theta)/\sqrt M$, and the standard deviation of $\hat\theta$
(the estimator's spread).

**Predictions.** $\hat\sigma_{\ln}$ is nearly unbiased at all sizes, with spread
$\approx \sigma_{\ln}/\sqrt{2n}$ — at $n = 50$ that is $0.10$, a $10\ \%$ relative
error. $\hat\xi$ is strongly **biased low** at small block counts (typically
$-0.10$ to $-0.05$ below the true $0$ for fewer than $\sim50$ blocks) and
converges slowly, so a reported $\hat\xi$ below about $0.1$ in absolute value is
indistinguishable from the Gumbel case unless the number of blocks is stated.
This prediction is exactly what the demonstration's $\hat\xi = +0.1277$ from
$1500$ blocks illustrates: large enough to be visible, small enough to be
noise.

---

## ★★★8 — Sensitivity of a grade-tonnage curve to the family

**Design.** Fit a lognormal and, as the alternative, a two-component mixture to
the same assay sample. Compute tonnage above cut-off $c$,
$T(c) = V\!\int_c^{\infty} g(x)\,\mathrm{d}x$, for
$c \in \{0.5, 1, 2, 5, 10, 20\}\times$ the sample median, under each family. Plot
$T_{\text{mix}}(c)/T_{\text{ln}}(c)$ against $c$.

**Prediction.** The ratio is $\approx 1$ for $c$ below the $95$th percentile and
then fans out; the two families agree on the body and disagree increasingly in
the tail.

**Where the model dominates.** The ratio departs from $1$ by more than the
sampling error of $T(c)$ once $c$ exceeds the largest observed grade. Beyond
that point the answer is a property of the fitted tail, not of the data: no
additional sampling from the same population would change it, only a better
(physically justified) family or more samples in the tail. The experiment
must therefore report the cut-off at which the family ratio first exceeds, say,
$1.5$, and treat every tonnage computed above it as a model statement.
