# Solutions — 16-09-02 Geodesy for Sea Level, Ice Mass and Water Storage

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand; the arithmetic is shown.

Lesson: [02 Geodesy for Sea Level, Ice Mass and Water Storage](../02-geodesy-climate.md).

---


## ★ Foundational

## ★1 — Closure and its uncertainty

$$\text{residual} = 3.50 - 2.10 - 1.30 = +0.10\ \mathrm{mm\,yr^{-1}}.$$

$$\sigma = \sqrt{0.40^{2}+0.20^{2}+0.30^{2}} = \sqrt{0.16+0.04+0.09}
= \sqrt{0.29} = 0.539\ \mathrm{mm\,yr^{-1}}.$$

$$\frac{\text{residual}}{\sigma} = \frac{0.10}{0.539} = +0.19.$$

The budget **closes** at this precision: a residual less than a fifth of a
standard deviation is entirely consistent with the measurement errors. The
statement "the budget closes" is a statement about the *ratio*, not about the
number $0.10$.

---

## ★2 — Rates to totals

Total: $3.3\ \mathrm{mm\,yr^{-1}} \times 30\ \mathrm{yr}
= 99\ \mathrm{mm} \approx 0.099\ \mathrm{m}$.

Gauge: $4.5 \times 30 = 135\ \mathrm{mm} = 0.135\ \mathrm{m}$.

The $1.2\ \mathrm{mm\,yr^{-1}}$ difference is $36\ \mathrm{mm}$ over the period —
comparable to the total change from a decade of the absolute trend, which is why
the land-motion correction cannot be treated as a rounding term.

---

## ★3 — A GIA correction on the mass term

$$\text{corrected} = 1.70 + 0.60 = \mathbf{2.30\ \mathrm{mm\,yr^{-1}}},
\qquad \frac{0.60}{1.70} = \mathbf{+35\%}.$$

A correction equal to a third of the quantity being corrected is not a
refinement; it is a first-order term that must be reported with its own
uncertainty.

---

## ★★ Applied

## ★★4 — Absolute trend and its uncertainty

$$\text{absolute} = 4.50 - 1.50 = \mathbf{3.00\ \mathrm{mm\,yr^{-1}}}.$$

The uncertainty has two contributions: the tide-gauge trend's own uncertainty (here
unspecified, so treat it as a separate term in a full budget) and the land-motion
uncertainty $\pm0.30\ \mathrm{mm\,yr^{-1}}$. Treating the land motion as the
dominant extra term, the absolute trend is

$$3.00 \pm 0.30\ \mathrm{mm\,yr^{-1}}$$

**from the land motion alone**, which is $10\%$ of the value. The point is that a
$10\%$ uncertainty can come from a correction that involves no sea-level
measurement at all, and it enters the budget's closure test directly.

---

## ★★5 — Variance contribution of a correction

$$\text{fraction of variance} = \frac{0.25^{2}}{0.867^{2}}
= \frac{0.0625}{0.7517} = \mathbf{0.083}\ (8.3\%).$$

If the GIA uncertainty were halved to $0.125\ \mathrm{mm\,yr^{-1}}$, its variance
falls by a factor of four, to $0.015625$, and the new budget variance is
$0.7517 - 0.0625 + 0.0156 = 0.7048$, so the fraction becomes
$0.0156/0.7048 = 2.2\%$ and the budget standard error falls from $0.867$ to
$0.840\ \mathrm{mm\,yr^{-1}}$ — a $3\%$ reduction.

The consequence to state: **halving a correction's assumed uncertainty barely
changes the total budget error here**, because it was already a minority term.
Deciding where to invest effort requires knowing which term dominates, and that
is the purpose of the variance decomposition.

---

## ★★6 — How the trend's standard error scales

Observed ratio: $1.734/0.434 = 4.00$.

$n^{-3/2}$ prediction for $n$ from $10$ to $30$:
$(30/10)^{3/2} = 3^{1.5} = 5.196$.

The observed ratio (4.00) is smaller than the asymptotic prediction (5.20), which
is expected: the $n^{-3/2}$ law is asymptotic in the persistence model, and at
$n = 10$ with $\varphi = 0.70$ the estimate is not yet in the asymptotic regime.

**Doubling the noise sd.** The trend standard error is proportional to the noise
sd, so doubling it doubles $\mathrm{SE}$. To keep
$|\text{trend}|/\mathrm{SE}$ constant one must increase the record length so that
$\mathrm{SE}$ falls by a factor of two. Since $\mathrm{SE} \propto n^{-3/2}$,
$n_{\text{new}} = n_{\text{old}} \times 2^{2/3} = n_{\text{old}} \times 1.587$.
For a baseline of $30$ years, $n_{\text{new}} \approx \mathbf{48\ years}$.

The general and useful rule: **trend precision improves as $n^{3/2}$, so noise
increases are cheap to absorb by extending the record and expensive to absorb any
other way** — which is exactly why the longest instrumental records are the most
valuable.

---

## ★★★ Research-oriented

## ★★★7 — Validating a mass-change partition

**The two corrections most likely to change it:**

1. **GIA.** The live correction differs between an ice-covered margin and its
   forebulge, and its uncertainty is regional. A wrong GIA field redistributes
   mass between the "ice" and "groundwater" buckets without changing the total
   trend.
   *Diagnostic:* repeat the partition with several independent GIA models
   (or several Earth-viscosity profiles) and report the spread of the ice
   fraction. If the ice fraction moves by more than its quoted uncertainty, the
   partition is model-limited.

2. **Leakage and filtering.** Gravity solutions are filtered and smoothed, so mass
   anomalies leak between adjacent regions. A coastal ice-loss signal leaks
   inland and can be mistaken for groundwater depletion.
   *Diagnostic:* apply the forward-modelled leakage operator to *synthetic*
   mass-change patterns that mimic each candidate scenario and check whether the
   observed pattern uniquely selects one. If two distinct truth patterns map to
   statistically indistinguishable filtered fields, the partition is not
   identified by the data.

**Additional requirement:** an independent constraint on one term (well records or
a terrestrial water budget for groundwater; altimetry or a surface mass-balance
model for ice), so that the partition is over-determined rather than merely
modelled.

Report format: *"the ice fraction is $X \pm Y$ from the measurement error and moves
within $[X_{\min}, X_{\max}]$ across the GIA and leakage choices; the total mass
trend is robust, the partition is not."*

---

## ★★★8 — GIA tolerance for a two-term partition (design)

**Generator.** A synthetic regional mass-change field constructed as a sum of two
known patterns: an ice-loss pattern $I$ frozen at a chosen amplitude and a
groundwater-depletion pattern $W$ with a chosen amplitude, such that the total is
fixed, $I + W = T$. Two truth scenarios are generated: (a) all of $T$ from $I$,
(b) a stated split, e.g. $60\%$ $I$ and $40\%$ $W$.

**Forward operator.** Apply a leakage/filtering operator to each synthetic field,
then add a GIA correction with a randomly drawn error of standard deviation
$\sigma_{\text{GIA}}$ from a set of candidate viscoelastic models, and finally add
measurement noise.

**Estimator.** Fit the two amplitudes by least squares to the filtered field
(i.e. attempt the partition), and construct the confidence region for the ice
fraction.

**Decision rule.** For each $\sigma_{\text{GIA}}$, compute the probability that the
two truth scenarios are distinguished: define the rule as "scenario (a) is
rejected if the $95\%$ interval for the ice fraction excludes $100\%$", and
measure the rejection rate over realisations.

**Tolerance.** The tolerated uncertainty is the largest
$\sigma_{\text{GIA}}$ for which the rejection rate at the chosen confidence level
remains above a stated power (e.g. $80\%$). Reporting *that value as a function of
the scenario separation* — rather than a single pass/fail — is the deliverable: it
states how much correction uncertainty the partition can absorb, and therefore how
much modelling effort the problem deserves.
