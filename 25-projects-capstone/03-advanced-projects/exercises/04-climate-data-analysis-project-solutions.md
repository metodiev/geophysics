# Solutions — 25-03-04 Project: Climate Data Analysis and Trend Attribution

> Read after attempting. Lesson:
> [04 Climate Data Analysis](../04-climate-data-analysis-project.md). All values
> are **SYNTHETIC** teaching numbers printed by
> [`code/climate_trend_demo.py`](../code/climate_trend_demo.py).

---

## ★1 — Integrated time and inflation

$$\tau_\text{int} = \Delta t\,\frac{1+\rho}{1-\rho}
= 0.25 \times \frac{1.50}{0.50} = 0.25 \times 3.00 = 0.75\ \mathrm{yr},$$

$$\text{inflation} = \sqrt{\frac{\tau_\text{int}}{\Delta t}}
= \sqrt{\frac{0.75}{0.25}} = \sqrt{3} = 1.732.$$

Unit of $\tau_\text{int}$: **years**, i.e. the same unit as $\Delta t$ and as the
time axis, because $\rho$ is dimensionless. A $\tau_\text{int}$ in samples means a
factor of $\Delta t$ has been forgotten.

Interpretation: adjacent quarterly samples are worth about $1/3$ of an independent
sample each, so a 40-year quarterly record has
$N_\text{eff} = 160/3 = 53$ effective samples rather than 160.

---

## ★2 — Trend in per-decade units

$$b = 0.023746\ \mathrm{^\circ C\,yr^{-1}} = 0.23746\
\mathrm{^\circ C\,decade^{-1}},$$

$$t_\text{naive} = \frac{0.023746}{0.001936} = 12.27, \qquad
t_\text{corrected} = \frac{0.023746}{0.004366} = 5.44.$$

Corrected standard error in per-decade units:

$$\sigma_b = 0.004366 \times 10 = 0.04366\ \mathrm{^\circ C\,decade^{-1}}.$$

So the trend is $+0.237 \pm 0.044\ \mathrm{^\circ C\,decade^{-1}}$
(autocorrelation-corrected), against the imposed
$+0.200\ \mathrm{^\circ C\,decade^{-1}}$. The estimate is $0.037\
\mathrm{^\circ C\,decade^{-1}}$ above the truth — $0.85\sigma$ of the corrected
error, comfortably consistent, and far outside the naive bar which would have made
this a $3.4\sigma$ "discrepancy".

---

## ★3 — Why the naive error is too small

The least-squares formula $\hat\sigma^{2}(A^{\mathsf T}A)^{-1}$ assumes the
residuals are independent, so it counts $N$ samples as $N$ pieces of information;
with positively autocorrelated residuals the record contains only
$N_\text{eff} \approx T/\tau_\text{int}$ independent pieces, and the standard error
is too small by $\sqrt{\tau_\text{int}/\Delta t}$. The quantity that fixes it is
the **integrated autocorrelation time** $\tau_\text{int}$, measured from the
residuals, or equivalently the effective sample count $N_\text{eff} = T/\tau_\text{int}$.

---

## ★★4 — Measured error rates

$$\text{naive rate} = \frac{219}{500} = 0.438 = 43.8\%, \qquad
\text{corrected rate} = \frac{39}{500} = 0.078 = 7.8\%,$$

$$\text{ratio} = \frac{0.438}{0.078} = 5.62.$$

Binomial standard errors, $\sqrt{p(1-p)/M}$ with $M = 500$:

$$\sigma_\text{naive} = \sqrt{\frac{0.438\times0.562}{500}} = \sqrt{4.92\times10^{-4}}
= 2.22\%,$$

$$\sigma_\text{corrected} = \sqrt{\frac{0.078\times0.922}{500}} = \sqrt{1.438\times10^{-4}}
= 1.20\%.$$

**Consistency with the nominal 5%:**

$$\frac{0.078 - 0.050}{0.0120} = 2.34\sigma.$$

The corrected rate is **outside** the nominal value at roughly $2.3\sigma$, so at a
$2\sigma$ criterion the correction is not consistent with a perfectly calibrated
test: it **under-corrects**. The reason is that the lag-1-based inflation ignores
the higher-lag correlation and the effect of the seasonal design, both of which
inflate the trend estimator slightly more than
$\sqrt{(1+\rho)/(1-\rho)}$ predicts.

This is precisely why the honest report quotes the **measured** rate ($7.8\%$)
rather than the nominal one ($5\%$), and why the surrogate experiment belongs in
the deliverable.

---

## ★★5 — What annual averaging did

$$\frac{\text{annual corrected SE}}{\text{monthly corrected SE}}
= \frac{0.004445}{0.004366} = 1.018.$$

Data counts: $N = 600$ monthly samples, $N = 50$ annual means — a factor of 12.

Decompose each corrected error as
$\text{SE} = \text{SE}_\text{naive}\times\text{inflation}$:

| | naive SE | inflation | corrected SE |
|---|---|---|---|
| monthly | $0.001936$ | $2.255$ | $0.004366$ |
| annual | $0.003792$ | $1.172$ | $0.004445$ |
| ratio (annual/monthly) | $1.958$ | $0.520$ | $1.018$ |

The two factors move in **opposite directions by almost the same factor**: the
naive error grows by $1.96$ because there are twelve times fewer numbers and
because the residual scatter of an annual mean is larger than
$1/\sqrt{12}$ of the monthly scatter (consecutive months are correlated, so twelve
months carry only about three independent pieces of information), while the
inflation falls by $0.52$. Their product is $1.02$.

**Conclusion.** Averaging does not buy precision in a trend: it converts
twelve correlated numbers into one less-correlated number, and the effective
information is the same. What it buys is comparability and interpretability, and
that is a legitimate reason to use annual means — provided the error bar is not
presented as an improvement.

---

## ★★6 — Correcting a colleague's interval

The colleague's interval: $0.004 = 2\sigma_\text{naive}$, so
$\sigma_\text{naive} = 0.002$, matching the demonstration's $0.001936$.

**Corrected 95% interval:**

$$\sigma_\text{corrected} = 0.001936 \times 2.255 = 0.004366\ \mathrm{^\circ C\,yr^{-1}},$$

$$b = 0.02375 \pm 0.00873\ \mathrm{^\circ C\,yr^{-1}}
\quad\text{i.e.}\quad [+0.01501,\ +0.03248]\ \mathrm{^\circ C\,yr^{-1}}.$$

**How much wider:**

$$\frac{0.00873}{0.00400} = 2.18.$$

The true interval is **$2.18$ times wider** than the quoted one — a factor that
makes the difference between "a precisely known trend" and "a trend known to
$\pm 37\%$ of its own value".

**Two items missing.** (i) The **noise model**: the interval is only valid for
white residuals, and the residuals here have $\rho = 0.6713$; the colleague should
quote $\rho$, $\tau_\text{int}$ and the corrected interval. (ii) The
**scope**: a trend interval is a statement about detectability, not about
attribution; without a spatial pattern test and a physical fingerprint, the
interval does not support any causal claim.

---

## ★★★7 — A regional detection-and-attribution test

**Null model.** Trends are not tested against white noise but against a null that
reproduces the observed space-time structure. Build the null from **surrogate
data**: (i) an AR(1) or, better, a fitted **power-law (long-memory)** time-series
model per station; and (ii) a **spatial correlation model** — either a fitted
covariance function or, more robustly, **block resampling of the station field**
(block bootstrap over stations and over years) so that spatial coherence is
preserved. A per-station white-noise null is the mistake measured in §5 of the
lesson, exaggerated by the number of stations.

**The estimator.** The standard pattern-correlation approach: project the
observed field of trends onto a **fingerprint** $g(\text{lat},\text{lon},\text{month})$
obtained from a physical model's response to a specific forcing, and test the
projection's amplitude. The fingerprint is what converts a magnitude comparison
into a pattern comparison, and it is the reason a single regional mean trend is
not an attribution.

**Spatial correlation and multiplicity.** Because the stations are correlated, the
number of *independent* spatial degrees of freedom is far smaller than the station
count: estimate it from the **empirical orthogonal functions** of the trend field
(or from the correlation length), and use that number, not the station count, in
any multiplicity adjustment. State the number of hypotheses searched — the number
of EOF patterns retained — and adjust the threshold accordingly, or calibrate the
threshold so the **measured** false-positive rate on the block-bootstrapped null
equals the target. The measured rate is the deliverable.

**Independent data that turn detection into attribution.** A fingerprint test
establishes that the observed *pattern* is consistent with the modelled response to
a candidate forcing and inconsistent with the null. That is stronger than a
detection but still a consistency argument; the additional evidence is:

1. **an independent period of record** (a different century, a different region)
   where the same fingerprint appears;
2. **an independent variable** — for a temperature attribution, the ocean heat
   content, the stratospheric cooling pattern, or the seasonal-cycle amplitude —
   whose response the same physical model predicts and which is not used to build
   the fingerprint;
3. **a competing-forcing test**: the pattern must *distinguish* the candidate from
   the plausible alternative (solar, volcanic, aerosol), which the model must be
   able to separate.

A design that reports only the significance of a regional trend has produced a
detection at best, and a detection with an uncalibrated threshold at worst.
