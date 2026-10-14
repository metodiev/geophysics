# Solutions — 21-01-03 Resampling: Bootstrap, Jackknife, Permutation Tests

> Read after attempting. Lesson:
> [03 Resampling](../03-resampling.md). Numbers quoted from the demonstration
> reproduce its output.

---

## ★1 — Leave-one-out means and the jackknife bias

Sample $\{2.60, 2.72, 2.68, 2.75, 3.40\}$, $n = 5$, sum $S = 14.15$,
$\bar x = 2.83$.

Omitting $i$, $\hat\theta_{(i)} = (S - x_i)/4$:

| omitted | $\hat\theta_{(i)}$ (g/cm³) |
|---|---|
| 2.60 | 11.55/4 = 2.8875 |
| 2.72 | 11.43/4 = 2.8575 |
| 2.68 | 11.47/4 = 2.8675 |
| 2.75 | 11.40/4 = 2.8500 |
| 3.40 | 10.75/4 = 2.6875 |

$\bar\theta_{(\cdot)} = (2.8875+2.8575+2.8675+2.8500+2.6875)/5 = 14.150/5 = 2.8300$.

$$\widehat{\text{bias}} = (n-1)(\bar\theta_{(\cdot)} - \bar x)
= 4(2.8300 - 2.8300) = 0 .$$

The result is **exactly zero**, and it had to be: the sample mean is a linear
functional of the data, so the leave-one-out average reproduces the full-sample
mean identically. The jackknife can only detect non-linear bias.

---

## ★2 — Reading the percentile interval

(a) It is an interval for the **mean of the population from which the sample was
drawn**, under the plug-in assumption that the empirical distribution stands in
for that population. It is an interval for the sampling distribution of the
**mean**, not for the data and not for the next observation.

(b) By construction, $2.5\ \%$ of bootstrap replicates fall below the lower
endpoint and $97.5\ \%$ below the upper endpoint.

(c) It is not symmetric: $1.4339 - 1.1688 = 0.2651$ below and
$1.7151 - 1.4339 = 0.2812$ above. The $5.7\ \%$ asymmetry is the small
$+0.111$ skewness of the bootstrap distribution showing up in the endpoints.

---

## ★3 — Permutation $p$-value

$$p = \frac{1 + 240}{1 + 5000} = \frac{241}{5001} = 0.04819 \approx 0.048 .$$

The $+1$ guarantees $p > 0$; it is the resolution limit of a $B$-shuffle test.
Here $B = 5000$ gives a resolution of $1/5001 = 0.0002$, ample for a reported
value of $0.048$.

---

## ★4 — Jackknife variance of the mean

With $S = \sum_j x_j$ and $\hat\theta_{(i)} = (S - x_i)/(n-1)$,

$$\hat\theta_{(i)} - \bar x
= \frac{S - x_i}{n-1} - \frac{S}{n}
= \frac{n(S-x_i) - (n-1)S}{n(n-1)}
= \frac{S - n x_i}{n(n-1)}
= \frac{\bar x - x_i}{n-1}.$$

Therefore

$$\sum_i \big(\hat\theta_{(i)} - \bar x\big)^2
= \frac{1}{(n-1)^2}\sum_i (x_i - \bar x)^2
= \frac{(n-1)s^2}{(n-1)^2} = \frac{s^2}{n-1},$$

and the mean of the leave-one-out values equals $\bar x$, so

$$\widehat{\mathrm{se}}_{\text{jack}}^2
= \frac{n-1}{n}\cdot\frac{s^2}{n-1} = \frac{s^2}{n}
\quad\Longrightarrow\quad
\widehat{\mathrm{se}}_{\text{jack}} = s/\sqrt n .$$

The jackknife reproduces the textbook standard error exactly. Checking against
the demonstration: jackknife $0.1412$ versus bootstrap $0.1404$ differ by
$(0.1412-0.1404)/0.1404 = +0.57\ \%$ — the bootstrap's own Monte-Carlo scatter at
$B = 10^4$ is a few tenths of a per cent, so the two agree as expected.

---

## ★5 — The atom at the sample maximum

$$p_{\max} = 1 - \Big(1 - \frac1n\Big)^{n}.$$

- $n = 50$: $(0.98)^{50} = 0.36417$, so $p_{\max} = 0.63583$.
- $n = 100$: $(0.99)^{100} = 0.36603$, so $p_{\max} = 0.63397$.

The demonstration measures $0.6346$ at $n = 100$, within $0.1\ \%$ of the exact
$0.63397$ — the residual is the $1/\sqrt{B}$ Monte-Carlo error with
$B = 10^4$. Approximately $63\ \%$ of all bootstrap resamples contain the
original maximum, which is why the percentile upper endpoint is the sample
maximum itself and the interval cannot extend beyond it.

---

## ★6 — Monte-Carlo error of a percentile endpoint

For a Gaussian bootstrap with scale $\sigma_b = 0.1478$ a.u. and $B = 10^4$,
the standard error of the estimated $p$-quantile is

$$\mathrm{se}(q_p) \approx \frac{\sigma_b\sqrt{p(1-p)/B}}{\varphi(z_p)},$$

with $p = 0.025$, $z_{0.025} = -1.9600$ and $\varphi(z_{0.025}) = 0.05844$:

$$\sqrt{\frac{0.025\times0.975}{10^{4}}} = \sqrt{2.4375\times10^{-6}} = 0.0015614,$$

$$\mathrm{se}(q_{0.025}) \approx \frac{0.1478 \times 0.0015614}{0.05844}
= \frac{2.3077\times10^{-4}}{0.05844} = 3.95\times10^{-3}\ \text{a.u.}$$

So the endpoint is resolved to about $\pm 0.004$ a.u. against an interval width
of $0.5231$ a.u. — a $0.75\ \%$ contribution. The statistical uncertainty dwarfs
the Monte-Carlo error at $B = 10^4$, which is the criterion for choosing $B$:
pick $B$ so that this ratio is well below the precision you intend to report.

---

## ★★★7 — Moving-block bootstrap for a GNSS series

**Block length.** With an integrated autocorrelation time
$\tau_{\text{int}} = 8$ days, choose $L \approx 2\tau_{\text{int}} = 16$ days
(rounded to $20$ for safety). The moving-block bootstrap uses **overlapping**
blocks of length $L$.

**Resample construction.** With $n = 1000$ and $L = 20$, a resample is
$\lceil n/L \rceil = 50$ blocks drawn independently and uniformly from the
$n - L + 1 = 981$ possible start indices, concatenated and truncated to $1000$
points.

**Statistic.** The linear trend of the series in mm/yr; recompute it on each of
$B = 10^4$ resamples and form the percentile interval.

**Adequacy diagnostic.** Because the block bootstrap does not reproduce the
stationary variance of an AR-type process, inflate the resample's variance to
match the sample variance (the "stationary bootstrap" correction), or measure the
ratio of the bootstrap variance of the mean to the model-based value
$\sigma^2 \tau_{\text{int}}/T$. Require this ratio to lie within
$1 \pm 0.05$; raising $L$ until it does is the calibration. A block length that
fails this diagnostic understates the trend uncertainty.

---

## ★★★8 — Coverage study for the median

**Design.** For each $n \in \{10, 20, 50, 100, 500\}$ and $M = 10\,000$
replicates: draw $n$ lognormal values with $\sigma_{\ln} = 1$; form the
$95\ \%$ percentile bootstrap interval for the median with $B = 2000$; record
whether the true population median $e^{0} = 1$ lies inside.

**Resolution.** The standard error of an estimated coverage $c$ is
$\sqrt{c(1-c)/M}$; at $c = 0.95$ and $M = 10\,000$ that is $0.0022$, so a
$2\ \%$ departure from nominal is resolved at $9\sigma$. $M = 10\,000$ is
sufficient; $M = 2500$ is not.

**Nominal level.** $0.95$.

**Prediction.** At $n = 10$ the percentile interval **under-covers**, typically
to $0.85$–$0.90$, because the empirical distribution is too coarse to represent
the tail of the sampling distribution; the error shrinks toward nominal by
$n = 100$ and is negligible at $n = 500$. This is the finite-sample regime in
which the BCa or studentised intervals are worth their extra complexity.
