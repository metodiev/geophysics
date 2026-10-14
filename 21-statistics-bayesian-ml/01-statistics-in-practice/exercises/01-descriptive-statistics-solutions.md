# Solutions — 21-01-01 Descriptive Statistics, Robust Measures and Outliers

> Read after attempting. Lesson:
> [01 Descriptive Statistics](../01-descriptive-statistics.md). Numbers taken
> from the demonstration are exact reproductions of its output.

---

## ★1 — Three location estimates

Sample: $4.1, 4.8, 4.9, 5.0, 5.2, 5.3, 120.0$ (sorted), $n = 7$.

(a) Mean $= (4.1+5.2+4.8+5.0+5.3+4.9+120.0)/7 = 149.3/7 = 21.329\ \%$. This
estimates the **mean** of the process and is pulled by the $120.0$ value.

(b) The $4$th order statistic is the median: $\tilde x = 5.0\ \%$. This
estimates the **median** of the process; the $120.0$ value enters only through
its rank.

(c) Trim $g = 1$ from each end: mean of $\{4.8, 4.9, 5.0, 5.2, 5.3\}$ is
$25.2/5 = 5.04\ \%$. This estimates a trimmed mean, which equals the process
**mean** when the tails are symmetric and is otherwise between the mean and the
median.

---

## ★2 — Two robust scales

Mean $= 21.3286$, so the deviations from the mean are $-17.2286, -16.1286,
-16.5286, -16.3286, -16.0286, -16.4286, +98.6714$.

$$\sum (x_i-\bar x)^2 = 296.82 + 260.13 + 273.19 + 266.62 + 256.92 + 269.90 +
9736.05 = 11359.6 .$$

$$s = \sqrt{11359.6/6} = \sqrt{1893.3} = 43.512\ \% .$$

Sorted absolute deviations from the median $5.0$: $0.0, 0.1, 0.2, 0.2, 0.3,
0.9, 115.0$. The MAD is the $4$th of these: $0.2\ \%$. Gaussian scale
$0.2/0.6745 = 0.2965\ \%$.

With the median-of-halves convention, $Q_1 = 4.8$ and $Q_3 = 5.3$, so
$\mathrm{IQR} = 0.5\ \%$ and $\mathrm{IQR}/1.349 = 0.3707\ \%$.

The two robust scales ($0.2965$ and $0.3707$) differ by a factor of $1.25$ and
both are tiny, because the bulk of the sample spans only $1.2\ \%$. The standard
deviation is $43.512\ \%$ — about **$147$ times** the MAD-based scale. That
factor is the price of the single value at $120.0$.

---

## ★3 — Is the median's departure sampling error?

$$\text{SE}(\bar x) = \frac{s}{\sqrt n} = \frac{9.866}{\sqrt{200}}
= \frac{9.866}{14.142} = 0.6977\ \% .$$

The median departs from $50\ \%$ by $|49.060 - 50| = 0.940\ \% = 1.35$ standard
errors. A $1.35\sigma$ excursion happens by chance roughly $9\ \%$ of the time
(two-sided), so it is **consistent with sampling error** — the clean sample was
drawn from exactly $\mathcal N(50, 10^2)$, so any discrepancy is noise by
construction.

---

## ★4 — Exact shift of the mean, and the median's insensitivity

Replacing $x_1,\dots,x_k$ by $c$ changes the mean by

$$\Delta \bar x = \frac{k c - \sum_{i=1}^{k} x_i}{n}.$$

With $k = 10$, $c = 200\ \%$, $n = 200$ and $\sum_{i=1}^{10} x_i = 10 \times 200
- 200 \times 7.325 = 2000 - 1465 = 535.0\ \%$,

$$\Delta \bar x = \frac{2000 - 535.0}{200} = \frac{1465}{200} = +7.325\ \% ,$$

which is the demonstration's observed shift exactly, since the shift is
deterministic given the sample.

For the median, $\tilde x$ is the middle order statistic. As long as $k < n/2$,
the middle order statistic is still drawn from the *clean* values, so
$\Delta \tilde x$ depends only on how many values changed rank — never on $c$.
The demonstration reports $+0.574\ \%$ there, which is the shift of the 100th
order statistic caused by removing $10$ values below it; doubling $c$ would
leave it unchanged.

---

## ★5 — Masking arithmetic

With clean mean $\approx 49 \%$ and standard deviation $10\ \%$, a spike at
$120\ \%$ has

$$z = \frac{120 - 49}{10} = 7.1 > 3.5,$$

so it is flagged. Adding one value at $2000\ \%$ to a sample of $200$ gives

$$s' \approx \sqrt{\frac{(2000-59)^2 + 199 \times 100}{199}} \approx 138.6\ \%,$$

the demonstration's $138.55\ \%$; the new mean is $\approx 59\ \%$. The same
$120\ \%$ spike now has

$$z' = \frac{120 - 59}{138.55} = 0.44 < 3.5,$$

so it is **masked**. The modified $z$-score uses the median ($\approx 49.5\ \%$)
and the MAD ($\approx 7.1\ \%$), both unchanged by the gross spike:

$$M = \frac{0.6745\,(120 - 49.5)}{7.1} = \frac{47.55}{7.1} = 6.7 > 3.5,$$

so the moderate spike is still found. This is the mechanism behind the
demonstration's "finds 1 of 5" versus "finds 5 of 5".

---

## ★6 — Measured versus theoretical scatter

$$\text{theory (mean)} = \frac{10}{\sqrt{200}} = 0.7071\ \%,$$

measured $0.7267\ \%$ — high by $+2.8\ \%$.

$$\text{theory (median)} = \sqrt{\frac{\pi}{2}}\cdot\frac{10}{\sqrt{200}}
= 1.2533 \times 0.7071 = 0.8862\ \%,$$

measured $0.8886\ \%$ — high by $+0.27\ \%$.

The **median** discrepancy is the smaller here, but that is luck of the ensemble
and not a general rule: both are estimates from $M = 3000$ ensembles, whose own
relative standard error is $1/\sqrt{2M} = 1.3\ \%$. Both measurements are within
about $2$ of those units; no physics is being missed. The relevant comparison is
between the two estimators, and the demonstration's relative efficiency
$(0.7267/0.8886)^2 = 0.6688$ sits within the ensemble scatter of the theoretical
$2/\pi = 0.6366$.

---

## ★★★7 — Efficiency of a trimmed mean across contamination

**Design.** For each contamination fraction $f \in \{0, 0.05, 0.10, 0.15, 0.20,
0.30, 0.40\}$ and each outlier magnitude $c/\sigma \in \{0, 1, 3, 10, 30\}$,
generate $n = 200$ values: $(1-f)n$ from $\mathcal N(0,1)$ and $fn$ equal to $c$.
For each configuration run $M = 20\,000$ ensembles and record the sample standard
deviation of each estimator across ensembles.

**Metric.** Efficiency of estimator $T$ relative to the mean,
$\mathrm{Eff}(T) = \mathrm{Var}(\bar x)/\mathrm{Var}(T)$, evaluated from the
ensemble variances.

**Resolution.** The relative standard error of an ensemble variance is
$\sqrt{2/M} = 1.0\ \%$ at $M = 20\,000$; an efficiency difference is claimed only
when it exceeds $2\sqrt{2}\times1.0\ \% \approx 2.8\ \%$.

**Prediction at $f = 0$.** All three estimators are unbiased; the trimmed mean
loses a little efficiency (about $2$–$5\ \%$ at $\alpha = 0.1$) and the median
loses $2/\pi = 36.3\ \%$. As $f$ grows the ordering reverses: the mean's variance
grows without bound $\propto f c^2$, while the trimmed mean and the median
saturate. The predicted crossing for $c/\sigma = 10$ is between $f = 0.05$ and
$f = 0.10$, and the experiment measures exactly where.

---

## ★★★8 — Revealing a $2\ \%$ dilution

**Diagnostic.** Plot the spacing of consecutive order statistics near the upper
tail (a QQ plot against the fitted lognormal, or the ratio of the 99th percentile
to the 90th). A $2\ \%$ fraction of diluted samples forms a cluster at a fixed
multiple of the true value; a QQ plot shows a step, not a smooth tail.

**What moves, and by how much.** With a dilution factor $d$ applied to a
fraction $f = 0.02$:

- the **mean** shifts by $f(d-1)\mu_{\text{clean}}$, i.e. $0.02\,(d-1)$ in units
  of the clean mean — for $d = 0.5$ that is $1\ \%$ of the mean, well below the
  standard error $\sigma/\sqrt n$ unless $n$ is very large;
- the **standard deviation** grows by approximately $f(d-1)\sigma$ to first
  order, again a sub-percent effect;
- the **$2$nd and $99$th percentiles** move discontinuously at the transition
  point, which is the sensitive statistic.

**What it cannot conclude.** A single sample cannot distinguish a $2\ \%$
dilution from a genuine second population, a laboratory batch effect, or a
mixture of two rock types. The diagnostic constrains the *fraction and multiple*
only if the analyst knows a priori that the contamination is a dilution of a
single clean population; otherwise the test must be repeated on a control
material.
