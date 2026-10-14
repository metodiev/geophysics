# Solutions — 07-02-03 Survey Procedures: Loops, Drift, Repeatability and Ties

> **Read after attempting the exercises.** Numbers were computed, not estimated.

Lesson: [03 Survey Procedures: Loops, Drift, Repeatability and Ties](../03-survey-procedures.md).

---

## ★1 — From readings to an anomaly

The observation equation is
$R = g + D(t) + \epsilon$, so with the base defining $g = 0$:

$$g_{\text{station}} = \left(R_{\text{station}} - R_{\text{base}}\right)
- \left[D\left(t_{\text{station}}\right) - D\left(t_{\text{base}}\right)\right].$$

With a linear drift $D = \alpha t$:

$$g_{\text{station}} = \left(14.0 - 2.5\right) - 12\ \mathrm{\mu Gal\,h^{-1}}
\times0.50\ \mathrm{h} = 11.5 - 6.0 = 5.5\ \mathrm{\mu Gal}.$$

**If the drift rate were not known,** the only defensible answer would be the
difference $11.5\ \mathrm{\mu Gal}$ **plus an unknown drift contribution**; the
uncertainty would be the drift rate's uncertainty times $0.5\ \mathrm{h}$ (in
practice obtained from the base occupations), and it would usually dominate. This is
the reason the base is bracketed around the stations: the bracket supplies
$D(t)$ rather than assuming it.

---

## ★2 — Closure and its expected size

$$\text{expected closure rms} = \sqrt{N}\,\sigma
= \sqrt{8}\times2.0 = 5.657\ \mathrm{\mu Gal}.$$

Observed $7.2\ \mathrm{\mu Gal}$ gives

$$\frac{7.2}{5.657} = 1.27,$$

i.e. $27\%$ above the expectation — comfortably consistent with a single draw from a
Gaussian of unit variance (a $1.27\sigma$ excursion has probability about $20\%$).
**Conclusion:** the loop's closure shows no evidence of drift or an event beyond
noise.

**Why this is the right comparison.** The closure is a sum of $N$ independent reading
noises (plus any drift model error), so its rms is $\sqrt{N}\sigma$, not $\sigma$.
Comparing a closure with the per-reading noise instead of $\sqrt{N}\sigma$ would
make every loop look broken.

---

## ★3 — Repeats and the standard error of the mean

$$\text{SEM}(n) = \frac{\sigma}{\sqrt{n}} = \frac{2.5}{\sqrt{n}}\ \mathrm{\mu Gal}:$$

| $n$ | SEM (µGal) |
|---|---|
| 1 | 2.50 |
| 4 | 1.25 |
| 25 | 0.50 |

$$\text{repeats for } 0.5\ \mathrm{\mu Gal}:\quad
n = \left(\frac{2.5}{0.5}\right)^{2} = 25.$$

**Caution.** This is a *repeatability* of $0.5\ \mathrm{\mu Gal}$, not an accuracy:
drift, the calibration scale and the tie are untouched. If any of those terms exceeds
$0.5\ \mathrm{\mu Gal}$ — and in a typical survey at least one does — the 25 repeats
have bought nothing beyond about the fifth.

---

## ★★4 — A step seen as an apparent drift rate

**Derivation.** The single bracket estimates the slope from the first and last base
occupations:

$$\widehat{\alpha} = \frac{D(T) - D(0)}{T}
= \alpha_{\text{true}} + \frac{S}{T},$$

because the step adds $S$ to the numerator and nothing to the denominator. Hence

$$\widehat{\alpha} - \alpha_{\text{true}} = \frac{S}{T}.$$

**(a)** $S = 20\ \mathrm{\mu Gal}$, $T = 2.0\ \mathrm{h}$:
$20/2.0 = 10.0\ \mathrm{\mu Gal\,h^{-1}}$.

**(b)** $S = 40\ \mathrm{\mu Gal}$, $T = 4.0\ \mathrm{h}$:
$40/4.0 = 10.0\ \mathrm{\mu Gal\,h^{-1}}$.

**What they have in common:** the same apparent rate error, and identical station
errors, because the error depends only on $S/T$. **Implication:** a fitted rate
cannot distinguish a small step soon after the base occupation from a larger step
earlier, nor either of them from a genuine change in the drift rate — the two
explanations are *degenerate* in the single-bracket model. Breaking the degeneracy
requires more base occupations (so that the segment slopes can be compared) or a
repeat station inside the loop. This is the algebraic version of the lesson's
measured $34.79$ against $15.0\ \mathrm{\mu Gal\,h^{-1}}$.

---

## ★★5 — Designing the base-occupation interval

The model error is taken as $8\%$ of the drift accumulated over the interval
$\tau$: $\text{error} = 0.08\,\alpha\,\tau$. Setting it equal to the target:

$$\tau = \frac{\text{target}}{0.08\,\alpha}.$$

**Target $2\ \mathrm{\mu Gal}$, $\alpha = 30\ \mathrm{\mu Gal\,h^{-1}}$:**

$$\tau = \frac{2}{0.08\times30} = 0.833\ \mathrm{h} = 50\ \mathrm{minutes}.$$

**Target $5\ \mathrm{\mu Gal}$:** $\tau = 5/(0.08\times30) = 2.083\
\mathrm{h} = 125$ minutes.

**With a $20\%$ model-error fraction instead of $8\%$:**
$\tau = 2/(0.20\times30) = 0.333\ \mathrm{h} = 20$ minutes — the interval shrinks by
a factor of $2.5$, i.e. linearly in the assumed model-error fraction.

**Reading of the result.** The interval depends on three things: the drift rate
(measured), the target (chosen) and the model-error fraction (assumed, and usually
unknown until the base-occupation series is examined). The design should therefore
state the fraction, and the survey should *verify* it by looking at the segment
slopes; if they scatter more than the fraction allows, the interval must be shortened
or the drift model improved.

---

## ★★6 — Correlated and independent terms

**(a) Absolute value of one station.** All terms contribute:

$$\sigma_{\text{abs}} = \sqrt{4.0^{2} + 1.5^{2} + 3.0^{2} + 1.0^{2}}
= \sqrt{16 + 2.25 + 9 + 1} = \sqrt{28.25} = 5.315\ \mathrm{\mu Gal}.$$

**(b) Difference between two stations in the same survey.** The two stations share
the tie and the calibration scale, so those terms cancel *exactly*:

$$\sigma_{\text{diff}} = \sqrt{1.5^{2} + 3.0^{2} + 2\times1.0^{2}}
= \sqrt{2.25 + 9 + 2} = \sqrt{13.25} = 3.640\ \mathrm{\mu Gal}.$$

(The reading-noise term is doubled because two independent readings are involved.
The calibration term is *not* doubled, because it is fully correlated: including it
at its full size in a difference is conservative. Strictly, a scale error affects a
difference in proportion to the difference rather than to the reading, so with
readings of $\sim5\ \mathrm{mGal}$ and differences of $\sim1\ \mathrm{mGal}$ its
contribution to a difference is about a fifth of $1.5\ \mathrm{\mu Gal}$, i.e.
$0.3\ \mathrm{\mu Gal}$, and the difference budget is closer to $3.2\mathrm{\mu Gal}$.)

**Why the two answers differ.** Correlated errors add linearly *to the value* and
cancel *in differences*. The absolute value inherits the full tie error; an anomaly
within the map does not. So the same survey supports a
$3.6\ \mathrm{\mu Gal}$ *anomaly* interpretation and a $5.3\ \mathrm{\mu Gal}$
*absolute* statement, and quoting the wrong one is a common over- or under-claim.
The stricter treatment — weighting the calibration term by the span of the
difference rather than by the reading magnitude — gives an even smaller
$\sigma_{\text{diff}}$ and should be used when the difference is much smaller than
the readings.

---

## ★★★7 — A $3\ \mathrm{\mu Gal}$ survey design (specification)

**Choices.** Instrument: $0.5\ \mathrm{\mu Gal}$ per reading, drift
$20\ \mathrm{\mu Gal\,h^{-1}}$ (SYNTHETIC); area $30\ \mathrm{km^{2}}$, station
spacing $250\ \mathrm{m}$ gives about 500 stations; occupation 3 minutes per station
including travel inside a star pattern from a central base; absolute tie
$4\ \mathrm{\mu Gal}$; calibration scale $0.02\%$ over the survey's $8\ \mathrm{mGal}$
gravity span, i.e. $1.6\ \mathrm{\mu Gal}$.

**Budget.**

| term | value (µGal) | how reduced |
|---|---|---|
| absolute tie (correlated) | 4.00 | better absolute datum; cancels in anomalies |
| calibration scale (correlated) | 1.60 | calibration line over a wide span |
| drift model | 24 min interval $\Rightarrow 0.08\times20\times0.4 = 0.64$ | denser base occupations |
| reading noise, 4 samples | 0.25 | more samples |
| **total (absolute value)** | $\sqrt{16+2.56+0.41+0.06} = 4.36$ | |
| **total (anomaly within survey)** | $\sqrt{2.56+0.41+0.06} = 1.74$ | |

The anomaly target ($3\ \mathrm{\mu Gal}$) is met with margin; the absolute-value
error ($4.4\ \mathrm{\mu Gal}$) is dominated by the tie and is *not* the quantity the
science question needs. State which one the survey claims.

**Cheapest improvements.** (1) Denser base occupations: the drift term is the
largest survey-controlled term, and halving the interval halves it. (2) Four samples
per station instead of one: this costs seconds and removes the reading noise from
the budget. What would *not* help: repeating station readings beyond four samples
(already below the drift term), or buying a more precise instrument (the tie and the
calibration dominate the absolute budget).

**Falsification.** Re-occupy 10% of the stations on a second day and compare;
differences should be consistent with the *difference* budget
($\sim2\ \mathrm{\mu Gal}$). Also check the base-occupation residuals against the
assumed $8\%$ model-error fraction: if they exceed it, the interval is too long and
the claim fails.

---

## ★★★8 — Distinguishing drift from a step (specification)

**Data.** A base-occupation series $R_{k}$ at times $t_{k}$, $k = 1\dots B$, with
reading noise $\sigma$ ($2$–$3\ \mathrm{\mu Gal}$ in the lesson's SYNTHETIC
examples). $B \ge 6$ is a practical minimum: three parameters of a general
piecewise model (level, slope before, slope after) must be estimated with at least a
few degrees of freedom left for the test.

**Two nested models.**

- $M_{1}$: $R_{k} = a + b\,t_{k} + \epsilon_{k}$ (pure linear drift; 2 parameters).
- $M_{2}$: $R_{k} = a + b\,t_{k} + S\,\left[t_{k} > t_{s}\right] + \epsilon_{k}$
  (linear drift plus a step at a *fitted* or *scanned* time $t_{s}$; 3 parameters, or
  more if $t_{s}$ is scanned).

**Test statistic.** With $B - 2$ and $B - 3$ residual degrees of freedom,

$$F = \frac{\left(\chi^{2}_{1} - \chi^{2}_{2}\right)/1}
{\chi^{2}_{2}/\left(B-3\right)},
\qquad
\chi^{2}_{i} = \sum_{k}\frac{\left(R_{k} - \text{model}_{i}\right)^{2}}{\sigma^{2}},$$

and reject $M_{1}$ at the $5\%$ level when $F > F_{0.95}\left(1, B-3\right)$ — which
fixes the false-alarm rate at $5\%$ by construction. Because $t_{s}$ is scanned, the
*look-elsewhere* effect must be accounted for: with $N_{s}$ candidate times the
effective threshold rises, so either use the Bonferroni-corrected threshold or, better,
fix $t_{s}$ from an external event (a transport, a temperature excursion) and test
with one degree of freedom.

**Sensitivity.** The smallest detectable step is roughly

$$S_{\min} \approx z\,\sigma\,\sqrt{\frac{2\left(B-1\right)}{B}}
\;\;\text{for a known } t_{s},$$

with $z \approx 2$ for a $5\%$ two-sided test. For $\sigma = 3\
\mathrm{\mu Gal}$ and $B = 8$ this is about $6\ \mathrm{\mu Gal}$; for $B = 20$ it is
about $5.4\ \mathrm{\mu Gal}$ — the statistical sensitivity saturates, because what
limits detection is the *noise on one reading*, not the number of occupations. More
occupations reduce the *false-alarm* risk and the uncertainty of the estimated step,
but the smallest detectable step improves only slowly.

**Practical consequence.** A step of $5\ \mathrm{\mu Gal}$ at the desired
$3\ \mathrm{\mu Gal}$ accuracy cannot be detected from a single base series with
$3\ \mathrm{\mu Gal}$ readings. The remedy is not more statistics but more
information: repeat a *station* inside the loop (the repeat difference is free of the
drift model), or use the closure structure of a network rather than a single loop.

---

## ★★★9 — A repeat survey with a different tie (specification)

**Data.** Two surveys $A$ and $B$ of a subset of 15% of the stations, different
instruments, different absolute ties, two months apart.

**Model.** For a station measured in both,

$$\Delta_{i} = g^{B}_{i} - g^{A}_{i} = \delta_{\text{datum}} + s\left(x_{i},
y_{i}\right) + e_{i},$$

where $\delta_{\text{datum}}$ is a constant offset (the tie difference plus any
survey-wide bias), $s$ is a smooth spatial field (a survey-wide systematic such as a
density or elevation-model difference), and $e_{i}$ is the station-specific
difference (noise plus genuine time-variable gravity, e.g. a subsidence or a
groundwater signal).

**Signatures on a map of $\Delta$.**

1. **A constant offset** appears as a uniform shift with no spatial pattern:
   diagnosed by the mean of $\Delta$ and its standard error. With $n$ repeat
   stations, the mean's uncertainty is $\sigma_{\Delta}/\sqrt{n}$; a significant
   non-zero mean is a datum difference. This is the *only* signature that can be
   removed by a single number.
2. **A survey-wide field** $s$ appears as a smooth, large-scale gradient or
   warp that grows towards the survey's edges and correlates with terrain,
   latitude or the reduction inputs (elevation error, density choice, terrain-model
   truncation). The diagnosis is a regression of $\Delta$ on those covariates;
   a significant slope identifies the cause and removes it as a *modelled* term
   rather than as a constant.
3. **A station-specific difference** appears as a local, spatially incoherent
   anomaly — possibly a real time-variable signal, possibly a bad measurement.
   Distinguish them with a third occupation: a repeatable local anomaly is
   time-variable gravity (a subsidence bowl, a water-table change); a non-repeatable
   one is a measurement error. The lesson's repeatability for one occupation
   ($2.5$–$3.5\ \mathrm{\mu Gal}$) sets the threshold.

**Order of operations.** Estimate and remove $\delta_{\text{datum}}$ first (one
parameter from $n$ stations), then fit $s$ on the covariates, then examine the
residuals for local structure. Doing it in the other order lets a datum offset
contaminate the covariate regression, since a constant term is the first column of
any such fit.

**What cannot be separated.** A systematic shared by both surveys, at the same
stations, with the same covariate dependence (for example both using the same
elevation model) cancels in $\Delta$ and is invisible. The only defence is an
independent data set (levelling, GNSS heights, in-situ density) or a change of
procedure between the two surveys, so that the shared systematic becomes an
unshared one and therefore visible.
