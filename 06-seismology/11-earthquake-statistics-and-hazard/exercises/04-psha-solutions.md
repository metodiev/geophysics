# Solutions — 06-11-04 Probabilistic Seismic Hazard Analysis (PSHA) and Its Logic

> Read after attempting the exercises. Numbers were computed with the formulas of
> the lesson. All values are **SYNTHETIC**.

Lesson: [04 PSHA](../04-psha.md).

---

## ★1 — probability to return period

$$T = -\frac{t}{\ln(1-P)}.$$

**(a)** 5% in 50 yr: $T = -50/\ln(0.95) = 50/0.0512933 = 974.8$ yr. The small-$P$
approximation gives $50/0.05 = 1000$ yr, an overestimate of 2.6%.

**(b)** 1% in 100 yr: $T = -100/\ln(0.99) = 100/0.010050 = 9950.5$ yr against the
approximation $100/0.01 = 10\,000$ yr, an overestimate of 0.5%.

The approximation $T \approx t/P$ is accurate when $P$ is small; for the 10%-in-50-yr
case the exact value 474.6 yr already differs from 500 yr by 5%.

---

## ★2 — magnitude rates

The cumulative rate above $m$ is

$$\nu(m) = 0.05\,\frac{10^{-(m-4.5)} - 10^{-3}}{1 - 10^{-3}}.$$

Above $M6.0$: $10^{-1.5} = 0.0316228$, so
$\nu = 0.05\,(0.0316228 - 0.001)/0.999 = 0.05\times0.030654 = 1.5327\times10^{-3}
\ \mathrm{yr^{-1}}$ (return period 652 yr).

Above $M6.5$: $10^{-2} = 0.01$, so
$\nu = 0.05\,(0.01 - 0.001)/0.999 = 0.05\times0.0090090 = 4.5045\times10^{-4}
\ \mathrm{yr^{-1}}$ (return period 2220 yr).

Bin $6.0$–$6.5$: the difference,
$1.5327\times10^{-3} - 4.5045\times10^{-4} = 1.0823\times10^{-3}\ \mathrm{yr^{-1}}$.

Note the ratio $\nu(6.0)/\nu(6.5) = 3.40$ rather than the $10^{0.5} = 3.16$ of a
pure exponential: the truncation at $M7.5$ removes mass from the upper end and
steepens the effective slope near it.

---

## ★3 — conditional exceedance probability

Median PGA at $M6.5$, $R = 15$ km:

$$\ln \hat z = 1.411 + 1.00\times0.5 - 1.30\ln(20)
= 1.911 - 1.30\times2.9957 = 1.911 - 3.8944 = -1.9834,$$
$$\hat z = e^{-1.9834} = 0.1375\ \mathrm{g}.$$

(this is the demonstration's scenario median of 0.1376 g to three figures.)

$$P(PGA > 0.30) = 1 - \Phi\!\left(\frac{\ln(0.30/0.1375)}{0.60}\right)
= 1 - \Phi\!\left(\frac{0.7802}{0.60}\right) = 1 - \Phi(1.3003).$$

$\Phi(1.3003) = 0.9033$, so

$$P = 0.0967 \approx 9.7\%.$$

Roughly one event in ten of this size and distance exceeds $0.30\ \mathrm{g}$ — the
consequence of a lognormal tail, not of the median exceeding the threshold.

---

## ★4 — why the total-rate check works

For the least likely cell, the magnitude bin centred on 4.625 at $R = 48.75$ km:

$$\ln \hat z = 1.411 + 1.00(4.625-6) - 1.30\ln(53.75)
= 1.411 - 1.375 - 1.30\times3.9844 = 0.036 - 5.1797 = -5.1437,$$
$$\hat z = e^{-5.1437} = 5.83\times10^{-3}\ \mathrm{g}.$$

$$P(PGA > 0.001) = 1 - \Phi\!\left(\frac{\ln(0.001/0.00583)}{0.60}\right)
= 1 - \Phi\!\left(\frac{-1.7635}{0.60}\right) = 1 - \Phi(-2.939) = 0.99835.$$

So even the least likely cell exceeds the threshold 99.8% of the time. The grid's
smallest median is $5.8\times10^{-3}\ \mathrm{g}$, more than five times the check
threshold, which is why the integral returns $0.04999\ \mathrm{yr^{-1}}$ against
the source rate $0.05000\ \mathrm{yr^{-1}}$: **the small deficit is exactly these
sub-1% tail cells.**

The check works because it tests the *bookkeeping* of the mixture (rates and
weights summing to the input rate) at a threshold where the physics is trivial. A
bookkeeping error of 25% — for example, computing bin rates from bin centres
without the truncation normalisation — would show up immediately.

---

## ★5 — one deaggregation cell

**Bin rate.** $\nu(6.00) = 1.5327\times10^{-3}$ from ★2;
$\nu(6.25) = 0.05\,(10^{-1.75} - 10^{-3})/0.999 = 0.05\,(0.0177828 - 0.001)/0.999
= 8.3998\times10^{-4}$. The bin rate is the difference,
$6.927\times10^{-4}\ \mathrm{yr^{-1}}$.

**Median PGA** at $M6.125$, $R = 6.25$ km:

$$\ln \hat z = 1.411 + 0.125 - 1.30\ln(11.25) = 1.536 - 3.1465 = -1.6105,
\qquad \hat z = 0.1998\ \mathrm{g}.$$

**Conditional probability** at $0.2\ \mathrm{g}$:

$$P = 1 - \Phi\!\left(\frac{\ln(0.2/0.1998)}{0.60}\right)
= 1 - \Phi(0.00167) = 0.4993,$$

essentially one half, as expected for a threshold equal to the median.

**Contribution:**

$$6.927\times10^{-4}\times\frac{1}{18}\times0.4993 = 1.92\times10^{-5}
\ \mathrm{yr^{-1}},$$

which is $1.92\times10^{-5}/4.3\times10^{-4} = 4.5\%$ of the total rate at
$0.2\ \mathrm{g}$. The entire deaggregation table is the same calculation repeated
on a grid, which is why the percentages sum to 100.

---

## ★6 — the effect of $\sigma$ on the design amplitude

$$\frac{0.00026}{0.00003} = 8.7.$$

A designer who reduced $\sigma$ from 0.90 to 0.30 — perhaps by "tightening" the
ground-motion model with more records — would see the rate at $0.4\ \mathrm{g}$
fall by a factor of 8.7, and would therefore read the 2%-in-50-yr amplitude from a
much flatter curve and design for a smaller motion.

**Why:** for a threshold $z$ above the median, the exceedance probability is
$1 - \Phi(\ln(z/\hat z)/\sigma)$, an increasing function of $\sigma$ because the
argument decreases. Quantitatively for $z = 2\hat z$, going from $\sigma = 0.30$ to
$0.60$ multiplies the exceedance probability by about 12 (the calculation in
[lesson 05](../05-ground-motion-models.md)). More scatter means more frequent
extreme shaking; a smaller $\sigma$ is not evidence of a safer site but of a
tighter model — and if the true $\sigma$ were larger, the design would be
unconservative.

---

## ★7 — a four-branch logic tree

$$\mathbb E[\lambda] = 0.15(0.00008) + 0.35(0.00012) + 0.35(0.00016)
+ 0.15(0.00031).$$

Term by term:
$1.20\times10^{-5} + 4.20\times10^{-5} + 5.60\times10^{-5} + 4.65\times10^{-5}
= 1.565\times10^{-4}\ \mathrm{yr^{-1}}$.

The mean, $1.57\times10^{-4}$, is **below** the reference branch's
$1.60\times10^{-4}$ and well above the lowest branch. Note three properties:

- the mean of the branches is not the best-estimate branch, because the weights are
  not concentrated on it;
- the mean is pulled by the high-rate branch ($0.15\times0.00031 = 4.65\times10^{-5}$
  contributes 30% of the total from one branch);
- reporting only the reference branch would understate the epistemic spread by a
  factor of 4 across the branches, which usually exceeds the difference between two
  hazard models.

Good practice reports fractiles of the branch distribution (for example the 5th,
50th and 95th percentiles of the weighted branch values), not just the mean,
because a design decision is usually about the upper tail.

---

## ★8 — study specification (calibrating epistemic spread)

**Observable.** For a set of test sites, the *observed* number of exceedances of a
threshold IM over a stated period, compared with the rates predicted by each model
branch. The observable is a count per site-period, which has Poisson scatter for
small rates — the dominant noise source, and one that must be modelled rather than
ignored.

**Aggregation level.** Aggregate over many sites and periods to get enough
exceedances; the aggregation rule (which sites, which magnitude-distance
separation, which IM) must be fixed in advance, and sites within the same source
region are correlated so an effective sample size smaller than the site count must
be used.

**Score.** For each site-period compute the probability integral transform of the
observation under each branch's predicted rate. Under a calibrated model these are
uniform. Then test:
(i) uniformity of the PIT values (a Kolmogorov-type test) — tests the centre of the
distribution; and
(ii) the fraction of observations inside the model's stated 5–95% branch interval —
tests the spread.
Report both, with a pre-declared pass/fail threshold.

**Failure mode invisible to one site.** A model whose *median* is biased and whose
*spread* is too wide can look calibrated at any single site (the wide spread
absorbs the bias) while failing the uniformity test in the ensemble. Conversely a
model with the right median and too narrow a spread passes at single sites but
fails the interval-coverage test.

**Honest limitation.** The Earth provides only one realisation of the future, and
the test treats spatial and temporal samples as exchangeable; if the catalogue's
completeness or the network changed during the test period, the observed counts
inherit those changes and the test measures the catalogue as much as the model.
