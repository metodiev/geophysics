# Solutions — 17-07-04 Satellite Time Series and Trend Analysis

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> All values are **SYNTHETIC** teaching numbers.

Lesson: [04 Satellite Time Series and Trend Analysis](../04-time-series-satellite.md).

---

## ★1 — Inflation and effective $n$

$$
\gamma = \sqrt{\frac{1.5}{0.5}} = \sqrt{3} = 1.732, \qquad
n_{\text{eff}} = 200 \times \frac{0.5}{1.5} = 66.7.
$$

Two hundred observations carry the information of about sixty-seven.

---

## ★2 — Corrected standard error

$$
\gamma = \sqrt{\frac{1.25}{0.75}} = \sqrt{1.\overline{6}} = 1.291, \qquad
\mathrm{SE}_{\text{corr}} = 0.002 \times 1.291 = 0.00258\ \text{per year}.
$$

---

## ★3 — Nyquist limit

The largest sampling interval is half the period:
$365.25/2 = 182.6$ days. This is the **Nyquist** condition
($\Delta < T/2$). Sampling more slowly than this folds the annual cycle onto a
lower frequency.

---

## ★4 — Corrected interval

$$
\gamma = \sqrt{\frac{1.5159}{0.4841}} = 1.769, \qquad
\mathrm{SE}_{\text{corr}} = 0.0018 \times 1.769 = 0.00318\ \text{per year}.
$$

$$
0.0184 \pm 1.96 \times 0.00318 = 0.0184 \pm 0.00624
= [\,0.0122,\; 0.0246\,]\ \text{per year},
$$

matching the lesson's corrected interval and about twice the width of the naive
one.

---

## ★5 — Aliasing

The sampling interval of $400$ days exceeds the $182.6$-day Nyquist limit for an
annual cycle, so the cycle is not resolved but *folded* onto a lower frequency.
The five samples land at different phases of the sinusoid, and their slow drift
in phase with time mimics a linear trend — the fitted slope is $+0.0162$ per
year from a signal with no trend at all. The effect is **aliasing**.

---

## ★6 — Variance reduction

$$
\mathrm{Var}_{\text{no step}} = 0.0314^{2} = 9.86\times10^{-4}, \qquad
\mathrm{Var}_{\text{step}} = 0.0276^{2} = 7.62\times10^{-4}.
$$

$$
\text{reduction} = \frac{9.86 - 7.62}{9.86} = 0.227,\ \text{i.e. } 22.7\%.
$$

A quarter of the residual variance was the step being mis-modelled as noise.

---

## ★7 — Design to detect a $0.005$/yr trend (specification)

- **Target.** Detect $\beta_1 = 0.005$ per year at the $95\%$ level with the
  corrected standard error, under $\rho = 0.5$, noise sd $0.03$, an annual
  harmonic in the model, and a revisit of $16$ days.
- **Quantity that sets significance.** The corrected standard error
  $\mathrm{SE}_{\text{corr}} \approx \mathrm{SE}_{\text{naive}}\gamma$; with
  $\gamma = 1.732$, achieving $\mathrm{SE}_{\text{corr}} \lesssim 0.005/1.96
  = 0.00255$ requires the naive error to be $\lesssim 0.00147$, which sets the
  required record length $n$ through
  $\mathrm{SE}_{\text{naive}} \propto 1/(\sigma_t\sqrt{n})$.
- **Assumptions to state.** The trend is linear; one annual harmonic suffices;
  the residual is stationary AR(1) with the stated $\rho$; there is no break or
  product-version change; the index is comparable across the whole record.
- **Honesty.** Because the corrected error dominates the design, lengthening the
  record — not sharpening the estimator — is what buys the detection.

---

## ★8 — A reprocessing is not a trend

A constant offset in the second half of the record is a **step** at the
processing date, not a change in the surface. A single-trend fit smears that
step across the record, producing a spurious secular slope whose size depends on
where the break falls relative to the record centre. The test is in the
residuals: fit trend + seasonal, then plot (or regress) the residuals against
time; a break shows as a coherent block of same-sign residuals before and after
the date. Fitting an explicit step term (or splitting the record) recovers the
offset. The practical safeguard is to align the candidate break with the
**product's version timeline** — if the break coincides with a reprocessing, it
is a processing artefact, and the series should be harmonised or truncated
rather than interpreted.
