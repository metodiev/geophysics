# Solutions — 25-04-04 Project: Earthquake Catalogue Statistics and Hazard Inputs

> Read after attempting. Lesson:
> [04 Catalogue Statistics](../04-earthquake-catalog-analysis.md). All values are
> **SYNTHETIC** teaching numbers printed by
> [`code/catalogue_hazard_demo.py`](../code/catalogue_hazard_demo.py).

---

## ★1 — The b-value

$$\hat b = \frac{\log_{10}e}{\overline{M} - (M_c - \Delta M/2)}
= \frac{0.434294}{3.42 - (3.0 - 0.05)} = \frac{0.434294}{0.47} = 0.9240,$$

$$\sigma_b = \frac{\hat b}{\sqrt{N}} = \frac{0.9240}{\sqrt{4000}}
= \frac{0.9240}{63.25} = 0.0146.$$

Unit: **dimensionless** (magnitudes are logarithmic, and the numerator and
denominator are both in magnitude units). $b = 0.92 \pm 0.01$ is close to the
fiducial 1.0 and entirely ordinary.

---

## ★2 — Extrapolated rates

$$\lambda(M \ge 6) = 10^{\,a - bM_0} = 10^{-2.0 - 0.9\times6} = 10^{-7.4}
= 3.981\times10^{-8}\ \mathrm{yr^{-1}},$$

$$\lambda(M \ge 7) = 10^{-2.0-6.3} = 10^{-8.3} = 5.012\times10^{-9}\ \mathrm{yr^{-1}},$$

$$\frac{\lambda(M\ge6)}{\lambda(M\ge7)} = 10^{\,b} = 10^{0.9} = 7.943.$$

**The ratio depends only on $b$** — the standard result that each unit of magnitude
costs a factor $10^{b}$ in rate, independent of $a$ and of the threshold. This is
why $b$ is the parameter that controls the *shape* of a hazard curve while $a$
controls its overall level.

---

## ★3 — Poisson probabilities with an interval

$$P(\ge1,\ 30\ \mathrm{yr}) = 1 - e^{-0.03409 \times 30}
= 1 - e^{-1.0227} = 0.6404,$$

$$P(\ge1,\ 50\ \mathrm{yr}) = 1 - e^{-0.03409 \times 50}
= 1 - e^{-1.7045} = 0.8182,$$

matching the demonstration. **Interval from $\sigma_\lambda$ alone:**

| exposure | lower ($\lambda - \sigma$) | upper ($\lambda + \sigma$) |
|---|---|---|
| 30 yr | $1-e^{-(0.02662)(30)} = 0.5501$ | $1-e^{-(0.04156)(30)} = 0.7126$ |
| 50 yr | $1-e^{-(0.02662)(50)} = 0.7359$ | $1-e^{-(0.04156)(50)} = 0.8748$ |

The interval spans a quarter of the central value, and it includes **only** the
$b$-value's statistical uncertainty: not the $M_c$ choice (§6 of the lesson moves
the rate by $40\%$), not the declustering rule (which moves it by a factor of
$2.9$), and not the omission of a maximum magnitude.

---

## ★★4 — Is the change in b significant?

$$\frac{0.8947 - 0.8369}{\sqrt{0.0069^{2} + 0.0136^{2}}}
= \frac{0.0578}{0.01525} = 3.79\sigma.$$

The declustering has changed $b$ by $3.8$ standard errors — a **significant** change,
not a fluctuation. That is the point of the item: the naive expectation is that
declustering leaves $b$ alone (aftershocks obey the same GR law), and the
measurement contradicts it, because the *filter* is magnitude-dependent: it deletes
the small members of each cluster and the mainshock survives. The bias is a
property of the algorithm, not of the seismicity, and it means that a declustered
$b$-value must not be compared with a raw one without stating the rule.

---

## ★★5 — Rate against retention

$$\text{rate ratio} = \frac{0.68690}{0.23416} = 2.93,
\qquad
\text{fraction removed} = 1 - \frac{3794}{16589} = 0.7713.$$

So the catalogue shrank by a factor of $4.4$ while the $M \ge 6$ rate fell by only
$2.9$. The reason is the **magnitude dependence of the retention**: 17 of 19 events
at $M \ge 6$ survive the filter (89.5%) against 22.9% overall. The events that
declustering removes are overwhelmingly small, so the rate of *large* events falls
much less than the total count. This is the quantitative reason that "declustering
reduced the catalogue by a factor of four, so it reduced the hazard by four" is
wrong: the large-event rate is far more robust to declustering than the total rate,
and only the large-event rate enters the hazard.

---

## ★★6 — Which of a and b dominates the Mc sensitivity

From the demonstration's $M_c$ sweep for the declustered catalogue:

| $M_c$ | $\hat b$ | $a = \log_{10}(N/T) + bM_c$ | $\lambda(M \ge 6)$ |
|---|---|---|---|
| 3.0 | $0.8369$ | $\log_{10}75.88 + 2.511 = 1.880 + 2.511 = 4.391$ | $0.23416$ |
| 4.0 | $0.7034$ | $\log_{10}8.36 + 2.814 = 0.922 + 2.814 = 3.736$ | $0.32758$ |

$$\text{change} = \frac{0.32758}{0.23416} - 1 = +39.9\%.$$

Both terms move: $a$ falls by $0.655$ (which alone would reduce $\lambda$ by a
factor of $4.5$) while $b$ falls by $0.1335$ and multiplies $M_0 = 6$, raising
$\log_{10}\lambda$ by $+0.801$ (a factor of $6.3$). The $b$ term wins, and it does so
**because the threshold is large**: the effect of $b$ on the extrapolated rate is
amplified by $M_0$, so an $M_c$ error matters more for a hazard study at
$M \ge 7$ than at $M \ge 6$. This amplification is the reason a high-threshold
hazard calculation is the most sensitive to completeness, and why $M_c$ must be
established before, not after, a rate is quoted.

---

## ★★★7 — An $M_c$ estimation procedure and its validation

**Estimators to compare.**

1. **Maximum curvature**, with a correction for the binned histogram: simple,
   biased when the detection fall-off is gradual.
2. **Goodness-of-fit (GFT)**: the $M_c$ above which the observed and
   GR-predicted cumulative distributions do not differ by more than a stated
   tolerance; robust to a gradual onset.
3. **$b$-value stability (MBS)**: the $M_c$ above which $\hat b$ stops varying
   systematically with the threshold — the most informative single diagnostic,
   because a rising or falling $\hat b$ with $M_c$ is direct evidence of
   incompleteness at the lower threshold.
4. **Entire-magnitude-range (EMR)** methods, which fit $a$, $b$ and a detection
   function jointly — the current default when the fall-off is gradual.

**Report all of them together.** Agreement between four estimators is evidence; a
single number is not. Where they disagree by more than the bin width, take the
largest $M_c$ as the conservative choice and propagate the range as an uncertainty.

**Detecting a time-varying $M_c$.** Split the catalogue into decades (or into
periods separated by network changes, which should be documented separately) and
estimate $M_c$ per window. A downward step in $M_c$ coincident with a network
upgrade is a detection change, not a rate change. The complementary diagnostic is
the **cumulative-count curve**: a rate change from detection appears as a jump in
$N(\ge M_c)$ at the change date, while a genuinely accelerating rate appears as a
smooth change in slope.

**Propagating the $M_c$ uncertainty into a rate.** Compute $\lambda(M \ge M_0)$
for each candidate $M_c$ and report the **range**, since $M_c$ enters both $a$ and
$b$ (§★6) and the two effects are large and opposite. Alternatively, treat $M_c$ as
a nuisance parameter with a prior set by the estimator spread and marginalise over
it — the Bayesian form of the same calculation, which is what the
trans-dimensional project of 25-05-04 does for a full model.

**The test that would show the estimate is wrong.** Synthetic recovery: generate
catalogues from a *known* $M_c$ with a realistic gradual detection function, run
the whole procedure, and check that the estimator recovers the generating value
within its stated interval. An estimator validated only on the real catalogue, for
which no true $M_c$ exists, has never been shown to work. A second, cheaper test is
to add a known sequence of synthetic small events below the assumed $M_c$ and
verify that the estimate does not move.
