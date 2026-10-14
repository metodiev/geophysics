# Solutions — 12-04-03 Palaeomagnetic Record and Reversal Frequency

> Read after attempting the [exercises](./03-palaeomagnetic-record-exercises.md).
> Lesson: [03 Palaeomagnetic Record and Reversal Frequency](../03-palaeomagnetic-record.md).
> Numbers computed. All models **SYNTHETIC**.

---

## ★1 — Mean interval and rate

$$\bar{\Delta t} = \frac{200\ \mathrm{Myr}}{500} = 0.400\ \mathrm{Myr},
\qquad \lambda = \frac{1}{\bar{\Delta t}} = 2.50\ \mathrm{Myr^{-1}} .$$

Units: the interval in Myr; the rate in reversals per Myr. Note that the rate is
**not** the mean of the point-wise rates when the record is non-stationary; it is
the count divided by the duration, which is why it must be reported with its
window.

---

## ★2 — Median of an exponential

$$P(\Delta t > m) = e^{-m/\bar{\Delta t}} = \tfrac12
\;\Longrightarrow\;
m = \bar{\Delta t}\ln 2 = 0.6931\,\bar{\Delta t}.$$

For $\bar{\Delta t} = 0.380$ Myr: $m = 0.263$ Myr. The demonstration observed a
median of 0.215 Myr, a mean/median ratio of $0.380/0.215 = 1.77$, above the
exponential value of $1/0.6931 = 1.44$. The excess is the signature of a
time-varying rate (a mixture of exponentials is over-dispersed), and it appears
before any formal test.

---

## ★3 — Probability of a long gap

$$P(\Delta t \ge 10) = e^{-5.0\times10} = e^{-50} = 1.93\times10^{-22}.$$

In decimal orders of magnitude, $\log_{10} = -21.7$. A gap of 20 Myr would be
$e^{-100} = 3.7\times10^{-44}$, and each additional 10 Myr multiplies the
probability by another $e^{-50} \approx 2\times10^{-22}$.

---

## ★4 — A 25-Myr gap

Mean interval 0.400 Myr gives a mean rate $\lambda = 2.50\ \mathrm{Myr^{-1}}$.

$$P(\Delta t \ge 25) = e^{-2.5\times25} = e^{-62.5} = 7.2\times10^{-28}.$$

For the gap to be a 5% fluctuation,

$$\lambda_{5\%} = \frac{\ln(1/0.05)}{25} = \frac{2.996}{25}
= 0.1198\ \mathrm{Myr^{-1}},$$

$$\frac{\lambda_{5\%}}{\lambda} = \frac{0.1198}{2.50} = 0.048,$$

i.e. the rate would have to be **21 times lower** than the record's mean. The
gap is therefore not a fluctuation of the observed process; it marks a different
process.

---

## ★★5 — The sampling bias at 0.5 Myr

At $\lambda = 5\ \mathrm{Myr^{-1}}$ the interval distribution is exponential with
mean 0.2 Myr. The fraction of intervals shorter than 0.5 Myr is

$$P(\Delta t < 0.5) = 1 - e^{-5\times0.5} = 1 - e^{-2.5} = 0.918,$$

so **92% of intervals are shorter than the resolution** and will be merged into
their neighbours.

The bias is one-sided because merging can only remove polarity changes: a
sampling grid that misses an odd number of reversals inside one cell records no
change where a change occurred, and there is no mechanism by which a cell records
a change that did not happen. Any count from a finite-resolution section is
therefore a lower bound on the true count, and the shortfall is largest where the
rate is highest.

---

## ★★6 — Threshold bias

From the demonstration's table, thresholds at 0.4 and 0.6 of the adopted median
($3.20\times10^{22}$ and $4.80\times10^{22}\ \mathrm{A\,m^2}$) give biases of
+1.6% and +7.8% on a synthetic sample of 400. A threshold at
$0.8\times$ the median ($6.4\times10^{22}$) gives **+19.0%** with 281 of 400
retained.

Averaging more determinations does not remove the bias, because the bias is in
the *selection* rather than in the sampling: every added determination is
subject to the same threshold, so the sample mean converges to the mean of the
truncated distribution, not to the mean of the true distribution. Removing the
bias requires modelling the selection function — the probability that a
determination of a given true strength is accepted — and inverting it.

---

## ★★★7 — Stationarity test for 200 reversals

**Statistic.** With 200 reversals a binning of 20-Myr windows is too coarse; use
either the interval CV (expected 1 under the null with standard error
$\approx\sqrt{1/(2N)} = 0.05$ for $N = 200$) or a slope fitted to counts in
windows sized to hold at least 10 expected reversals each.

**Null.** A stationary Poisson process at the record's mean rate. Generate it by
drawing the same number of reversals uniformly over the record length — this
preserves the mean rate exactly and removes the rate structure.

**Power.** For a factor-of-two rate change across the record, the count in the
first half differs from the second half by a factor of two. With 100 reversals
per half, the difference has a standard error of
$\sqrt{100 + 50} \approx 12$ against a difference of 50 — a $4\sigma$ effect, so
the test has high power for that effect size. For a 20% change the difference is
20 with the same standard error, a $1.7\sigma$ effect: **not detectable**.

**Confound.** Long-range correlations (a slowly varying sedimentation rate, or
clustering of reversals in time) inflate the variance of any count statistic, so
a nominal $4\sigma$ result can be a $2\sigma$ result. The conservative remedy is
to bootstrap the null from *blocks* of the record rather than from uniform draws.

---

## ★★★8 — Stationary versus smoothly varying nulls

If the null uses a smoothly varying rate (for example the fitted rate curve), the
null already contains the trend being tested, so the test statistic is compared
against a distribution that includes the effect. The measured slope then falls
close to the centre of the null distribution and the $p$-value becomes large —
the demonstration's own earlier version gave $p = 0.355$ by exactly this route.

That version is **more conservative in the wrong direction**: it does not protect
against a real trend, it simply fails to look for one. A null containing the
effect can only ever fail to reject.

Which null is appropriate depends on the question:

- To ask **"is the rate stationary?"**, the null must be stationary, and the
  fitted varying rate must not enter it.
- To ask **"did the dynamo's regime change?"**, one wants a null that contains
  *adiabatic* rate variations (slow changes caused by the cooling of the core, as
  in [12-03-03](../../03-geotherms-and-heat-budget/03-thermal-evolution.md)) but not
  a discrete switch. The appropriate null is then a physically parameterised
  cooling model, and the test becomes a comparison of two models rather than of a
  model against stationarity.

---

## What a good answer looks like

Every statistical claim came with its power, every interval statistic came with
its sampling resolution, and no test was reported without stating the null it was
tested against.
