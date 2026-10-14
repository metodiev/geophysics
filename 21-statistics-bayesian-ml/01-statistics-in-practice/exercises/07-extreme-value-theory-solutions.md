# Solutions — 21-01-07 Extreme Value Theory for Geohazards

> Read after attempting. Lesson:
> [07 Extreme Value Theory](../07-extreme-value-theory.md). Numbers quoted from
> the demonstration reproduce its output.

---

## ★1 — Classifying the shape parameter

| $\hat\xi$ | case | domain of attraction | tail |
|---|---|---|---|
| $+0.63$ | Fréchet | power-law tail, $1-G(z)\sim z^{-1/\xi}$ | heaviest; $\mathbb E[X] $ may diverge for $\xi \ge 1$ |
| $-0.12$ | Weibull | bounded above at $\mu - \sigma/\xi$ | no exceedance beyond a hard maximum |
| $-0.001$ | Gumbel (indistinguishable from $\xi = 0$) | exponential decay | light-tailed, unbounded |

The last case is the one that must be reported as "consistent with Gumbel": a
$\hat\xi$ whose interval contains $0$ does not support a bounded-tail claim even
though its sign is negative.

---

## ★2 — Gumbel return levels

$$z_T = \mu - \sigma\ln\!\big(-\ln(1 - 1/T)\big), \qquad \mu = 0,\ \ \sigma = 1 .$$

- $T = 10$: $-\ln(0.9) = 0.10536$, $\ln(0.10536) = -2.2504$, so
  $z_{10} = 0 + 2.2504 = 2.2504$.
- $T = 100$: $-\ln(0.99) = 0.010050$, $\ln = -4.60015$, so
  $z_{100} = 4.6002$.

The levels are in units of $\sigma$. Doubling the return period adds only a
constant multiple of $\sigma$ in the Gumbel case — the growth is logarithmic,
which is why light-tailed bodies rarely produce alarming long-period levels.

---

## ★3 — Exceedance probability over the return period

$$P(\text{at least one exceedance in } T \text{ blocks})
= 1 - \Big(1 - \frac1T\Big)^{T} .$$

- $T = 10$: $(0.9)^{10} = 0.34868$, so $P = 0.6513$.
- $T = 100$: $(0.99)^{100} = 0.36603$, so $P = 0.6340$.

Both are about $1 - e^{-1} = 0.6321$, independent of $T$ for large $T$. A
"$100$-block return level" is therefore exceeded with probability $63\ \%$ in any
$100$ blocks — it is a rate statement, not a safe bound, and reporting it as an
upper limit is a category error.

---

## ★★4 — GEV return level from the fitted parameters

$$z_T = \mu + \frac{\sigma}{\xi}\Big[\big(-\ln(1 - 1/T)\big)^{-\xi} - 1\Big].$$

**$T = 100$:** $-\ln(0.99) = 0.0100503$; $\ln(0.0100503) = -4.60015$;
$(-4.60015)(-0.6297) = +2.89671$; $e^{2.89671} = 18.116$; minus one is
$17.116$; $\sigma/\xi = 4.9415/0.6297 = 7.8473$;

$$z_{100} = 7.6615 + 7.8473 \times 17.116 = 7.6615 + 134.30 = 141.96 .$$

Matches the printed $141.957$ ✔.

**$T = 10$:** $-\ln(0.9) = 0.10536$; $\ln = -2.25037$; times $-0.6297$ gives
$+1.41693$; $e^{1.41693} = 4.1249$; minus one is $3.1249$;
$7.8473\times3.1249 = 24.52$; $z_{10} = 7.6615 + 24.52 = 32.18$ ✔, matching the
printed $32.184$.

---

## ★★5 — Threshold-model return level

With $u = 7.664$, $\beta = 5.1507$, $\xi = 0.5831$ and $\lambda_u = 1.0$
exceedance per block:

$$(T\lambda_u)^{\xi} = 100^{0.5831} = e^{0.5831\times4.60517} = e^{2.68554}
= 14.666,$$

$$z_{100} = 7.664 + \frac{5.1507}{0.5831}(14.666 - 1)
= 7.664 + 8.8324 \times 13.666 = 7.664 + 120.72 = 128.38 .$$

The GEV gives $141.96$, so the threshold model is **$9.6\ \%$ lower**.

The two should agree asymptotically — they estimate the same tail index — but
not exactly in a finite sample: (i) the GPD used $1000$ exceedances above the
$95$th percentile while the GEV used $1000$ block maxima, i.e. different extreme
sets; (ii) $\hat\xi$ differs between them ($0.5831$ vs $0.6297$); (iii) the
threshold-model return-level formula assumes the Poisson-GPD limit exactly,
including the declared rate $\lambda_u$. A $10\ \%$ gap at $T = 100$ is a
reasonable representation of how much the answer depends on the extreme-value
*route* as well as on the data, and is one reason a study should report both.

---

## ★★6 — Inverting a mean-excess slope

For a GPD, $\dfrac{\mathrm de}{\mathrm du} = \dfrac{\xi}{1-\xi}$, so

$$\xi = \frac{\text{slope}}{1 + \text{slope}} = \frac{1.2010}{2.2010} = 0.5457 .$$

The fitted maximum-likelihood value is $\hat\xi = 0.5831$, and the true value is
$0.6667$. The slope estimate is $1.4$ percentage points closer to the truth than
the fit here, but that is luck: the slope is a **first difference of two
heavy-tailed sample means**, each based on a different number of exceedances
(about $1000$ and $600$ respectively). Its standard error therefore shrinks only
as the *square root of the number of exceedances*, and the two means are highly
correlated, which makes the difference noisier than it looks. The
maximum-likelihood fit uses every exceedance jointly and is the more efficient
estimator; the mean-excess plot is a diagnostic, not an estimator.

---

## ★★★7 — Threshold-selection study

**Design.** Draw $N = 50\,000$ i.i.d. Fréchet values with $\alpha = 1.5$
($\xi = 0.6667$). For exceedance fractions
$\phi \in \{0.20, 0.10, 0.05, 0.02, 0.01, 0.005, 0.002\}$ set
$u = $ the corresponding quantile, fit the GPD by maximum likelihood, and record
$\hat\xi$. Repeat with $M = 1000$ independent samples.

**Metrics.** Bias $= \overline{\hat\xi} - 0.6667$ with its standard error
$\mathrm{sd}(\hat\xi)/\sqrt M$; the estimator's spread $\mathrm{sd}(\hat\xi)$; and
the realised number of exceedances $N\phi$.

**Data-based diagnostics.** (i) The mean-excess plot: linearity above $u$.
(ii) The parameter-stability plot: $\hat\xi$ and the modified scale
$\beta - \xi u$ constant above $u$. (iii) The number of exceedances, which must be
large enough that the asymptotics bite.

**Predictions.** At low $\phi$ (few exceedances) the estimator is **noisy**, with
$\mathrm{sd}(\hat\xi)$ growing like $1/\sqrt{N\phi}$; at high $\phi$ (low
threshold) the estimator is **biased low**, because the body is not yet in the
GPD's asymptotic regime and the excess distribution is not Pareto. The
stability plot shows this as a downward drift of $\hat\xi$ as $u$ falls. The
study's headline is the threshold window — neither too low nor too high — in
which both bias and spread are acceptable, which for $\alpha = 1.5$ and
$N = 50\,000$ is typically $\phi \in [0.005, 0.05]$.

---

## ★★★8 — Declustering study

**Cluster identification.** Build a synthetic series as a Poisson process of
cluster onsets with rate $\lambda_c$ per block; within each cluster, place
$K \sim \mathrm{Geometric}(\theta)$ events whose magnitudes decay with a
Markov-like dependence, so that the extremal index is $\theta \approx 1 -
\overline{1/K}$.

**Declustering runs parameter.** Separate runs of exceedances by the
**runs method**: declare an exceedance part of the current cluster until $r$
consecutive observations fall below $u$; take the cluster maximum. Sweep
$r \in \{1, 2, 3, 5, 10\}$ blocks.

**Quantity rescaled by the extremal index.** $\theta$ is the factor by which the
rate of independent exceedances is reduced by clustering: the exceedance rate of
the **declustered** series is $\theta \lambda_u$, so the threshold return level
becomes

$$z_T = u + \frac{\beta}{\xi}\Big[\big(T\,\theta\,\lambda_u\big)^{\xi} - 1\Big].$$

**Verification that the declustered series is i.i.d.** After extracting cluster
maxima, test (i) the autocorrelation function of the cluster-maximum series for
values significantly different from zero at lags $1$–$10$, and (ii) a
dispersion-index / runs test on their exceedance pattern. The study's headline is
the $r$ at which these diagnostics stop changing — beyond it, raising $r$
discards data for no gain in independence, and the fitted $\hat\theta$ has
stabilised.
