# Solutions — 03-08-05 Case Study: Analysing a Climate Data Cube

> **Read this after attempting the exercises, not before.** Every value attributed
> to "the demo" is its actual output. All data are SYNTHETIC; no number below is an
> observation of the Earth.

---

## ★1 — The five terms

| Term | Imposed amplitude |
|---|---|
| meridional profile $28 - 0.30|\phi| - 0.004\phi^{2}$ | 28 K at the equator falling to about 1.5 K at 87.5° |
| seasonal cycle $3\cos(2\pi t/12)$ | **3.00 K** amplitude |
| linear trend $0.20\,(t/120)$ | **0.20 K/decade** |
| oscillation $1.4 f(t)\cos 2\phi$ | **1.40 K** amplitude, 48-month carrier in a 20-year Gaussian envelope |
| noise $\mathcal{N}(0,0.35)$ | **0.35 K** standard deviation |

Measured cube: `dims = {'time': 480, 'lat': 36, 'lon': 72}`, values −33.88 to
33.05 K, 2,592 grid cells.

---

## ★2 — The baseline offset

The mean anomaly is $b(t_r - t_0) = 0.20 \times 0.5 = \mathbf{+0.10}$ K, and the
demo measures **+0.1000 K** for the whole-record mean against a baseline mean of
**0.000000 K**. The baseline is the reference point; the trend guarantees that a
record extending beyond it has a non-zero mean.

---

## ★3 — Complete annual means

An annual mean over exactly twelve consecutive months averages the seasonal term
over a full period, so its contribution is zero: measured in the demo as a
**0.00 mK/decade** difference between the raw annual trend and the anomaly trend.
"Complete" means **all twelve months present for every year**; a missing month
leaves a residual seasonal component, and *which* month is missing determines the
sign of the bias.

---

## ★4 — Regression map

A regression map is the field of a regression coefficient (or correlation) between
a time series at each grid point and a reference index. A correlation coefficient
at one grid point is the fraction of that point's temporal variance that is
linearly explained by the index, normalised to $[-1, 1]$; its square is the
variance fraction.

---

## ★5 — Anomalies and trends

**(a)** Measured: whole-record anomaly mean **+0.1000 K**; baseline anomaly mean
**+0.000000 K**; baseline residual standard deviation **0.5488 K**.

**(b)** $\sqrt{0.5488^{2} - 0.35^{2}} = 0.4229$ K. Contributors: the imposed
oscillation (1.4 K amplitude, modulated) plus the fact that the residual includes
the 2015–2024 part of the record beyond the baseline.

**(c)** Naive **+0.2002 K/decade** (**+0.08 %**), weighted **+0.1997 K/decade**
(**−0.16 %**), imposed **+0.2000 K/decade**. Their mutual difference is
0.49 mK/decade.

---

## ★6 — The residual lesson

**(a)** Naive residual rms **1.72 mK**; weighted residual rms **165.78 mK** — a
factor of 96.

**(b)** On the demo's 36-row uniform grid:

$$\frac{1}{36}\sum_{i=1}^{36}\cos 2\phi_i = -1.9\times10^{-17},
\qquad
\frac{\sum_i \cos\phi_i \cos 2\phi_i}{\sum_i \cos\phi_i} = 0.333.$$

The unweighted sum cancels the pattern to machine precision; the weighted sum
retains a third of it.

**(c)** The naive series is smoother because it has **destroyed a real signal**,
not because it has estimated it better. The oscillation is a physical part of the
field; an area mean must retain it. Reporting only the trend hides the difference,
which is exactly how a wrong pipeline survives peer review.

---

## ★7 — Subsampling

**(a)** Raw annual trend **+0.1997 K/decade**; January+July only (80 samples)
**+0.1446 K/decade**.

**(b)** Bias $= (0.1446 - 0.2000)/0.2000 = \mathbf{-27.7\ \%}$.

**(c)** Fitting $y = a + bt$ to a series containing $c\cos(\omega t + \psi)$ biases
the slope by a term proportional to $c\cos\psi$. When two specific months are kept,
$\psi$ is *fixed* rather than randomised over the record, so the bias does not
average out. January and July are the extremes of a 12-month cycle, which is the
worst possible pair for a slope estimate that assumes the offset to be constant.

---

## ★8 — The regression map

**(a)** Measured: global maximum |r| = **0.8276 at latitude 7.5°, longitude
−102.5°**; equatorial band (|φ| < 10°) maximum **0.8276**; mid-latitude band
40–60°N maximum **0.5662**.

**(b)** At 7.5°N,
$\sigma_{\text{signal}} = 1.4 \times |\cos 15°| \times 0.3958 = 0.5352$ K, and

$$r = \frac{0.5352}{\sqrt{0.5352^{2} + 0.35^{2}}} = \mathbf{0.8369}.$$

**(c)** Measured 0.8276 against predicted 0.8369: a **1.1 %** agreement. That is the
standard to aim for — an a-priori prediction from the imposed parameters that the
measurement confirms, rather than a number reported because it was computed.

The mid-latitude maximum is smaller because $\cos 2\phi$ passes through zero at
45°, so the largest |r| in the 40–60° band occurs at its edges.

---

## ★9 — A non-uniform latitude grid

A complete answer reports the numbers and then explains them; the explanation is
the graded part because the numbers depend on the chosen grid.

Construction: replace `lat = np.linspace(-87.5, 87.5, 36)` with a grid whose
spacing shrinks toward the equator, e.g. a sine-spaced or Gaussian-spaced
distribution, and keep everything else identical.

What changes:

- The **weighted** result should change only slightly: the cos-weight already
  corrects for cell area, so refining where the cells were small (the poles) or
  large (the equator) mostly adds resolution, not bias. Expect the weighted trend
  to stay within a few mK/decade of +0.1997.
- The **naive** result changes a lot, because the naive mean's implicit weight is
  "one per row", and the row distribution has changed. The measured cancellation of
  $\cos 2\phi$ over a *uniform* grid (−1.9 × 10⁻¹⁷) becomes a partial cancellation:
  the sum
  $\frac{1}{n}\sum_i \cos 2\phi_i$ is now the mean of $\cos 2\phi$ under a different
  measure, and it is no longer zero. Expect the naive residual rms to rise from
  1.72 mK (it will no longer cancel the oscillation) and the naive/weighted trend
  gap to widen from 0.49 mK/decade.

The mechanism in one sentence: **the naive mean's implicit weights are the row
densities, so changing the grid changes the estimate; the cos-weighted mean's
weights are the cell areas, so changing the grid changes only the sampling.**

A good answer also comments on the direction of the change: a grid dense at the
*equator* over-represents the equatorial band, and $\cos 2\phi = +1$ there, so the
naive mean will move *toward* the equatorial anomaly — which is precisely the
regime in which the two estimates now disagree in the trend rather than only in the
residuals.

---

## ★10 — Distinguishing a modulated signal from a periodic one

Replace `enso = sin(2π t/48) * exp(-((t % 240 - 120)/60)²)` with
`enso = sin(2π t/48)` and re-measure.

| Lag (months) | Gaussian envelope (measured) | Pure 48-month sinusoid (measured) |
|---|---|---|
| 0 | +0.2917 | +0.3420 |
| 6 | +0.2062 | +0.2403 |
| 12 | +0.0003 | −0.0061 |
| 18 | not sampled (see below) | −0.2541 |
| 24 | not sampled (see below) | −0.3563 |
| 36 | not sampled (see below) | −0.0203 |

The envelope column is the demonstration's output at its five sampled lags; the
sinusoid column was obtained by replacing the envelope with `sin(2π t/48)` and
re-running the same lag computation. The demo samples lags 0, 2, 4, 6, 9, 12 only,
so its negative branch is never shown — which is itself a lesson about choosing
lags.

A pure 48-month carrier produces a **cosine-shaped lag profile** with period 48
months: **+0.3420 at lag 0, −0.0061 at 12, −0.3563 at 24, −0.0203 at 36** —
measured. The envelope produces a **monotone decay** with no negative branch,
because the autocorrelation of an amplitude-modulated process is governed by the
envelope's width (20 years) rather than by the carrier's period.

The observable that distinguishes them is therefore **the sign structure of the lag
profile**: a negative branch at half the carrier period means a stationary
oscillation; monotone decay means the amplitude itself is non-stationary.

Why it matters: "the signal propagates" is a claim about a *phase-shifted*
response at different locations, which can only be diagnosed from a lag structure
that is stable across the record. If the amplitude is non-stationary, then a lag
that fits the 1998 event will not fit the 2015 event, and the propagation claim is
an artefact of a single event rather than a property of the system. The
demonstration's monotone decay to 0.0003 at 12 months is the signature that says:
**measure the propagation with a windowed analysis, and report the window.**

---

## ★11 — Appraising a trend sentence

A complete appraisal contains the following points; the reasoning is marked.

**Baseline.** The number is a rate and is baseline-independent, but the *anomaly
series* the rate came from is not. The demo measures a whole-record mean of
+0.1000 K against a 30-year baseline centred 5 years before the record, purely from
the trend. Any statement of "how much it has warmed" needs a baseline; a rate
needs the baseline only to the extent that the baseline choice affects the
seasonal removal and the trend estimator. (Measured: the 0.1000 K offset;
reasoned: the rate's insensitivity.)

**Weighting.** Measured: 0.2002 vs 0.1997 K/decade for naive and cos-weighted means
of the same synthetic field — a 0.49 mK/decade difference, i.e. 0.25 %. So for
*this* field the weighting barely matters for the rate, and matters enormously for
the residuals (1.72 vs 165.78 mK). The sentence must therefore state the weighting
because it determines everything else that can be computed from the series, even
where it barely changes the rate.

**Mask.** The demonstration's cube is defined everywhere, which no real product is.
A land–sea mask changes the area weighting; a sea-ice mask removes a seasonally
varying fraction of the high latitudes, which is correlated with the signal and
therefore biases a trend. (Reasoned; the synthetic cube cannot show it.)

**Record length and uncertainty.** The demo recovers an imposed 0.20 to within
0.16 % over 40 years, with residual rms values of 1.72 mK and 165.78 mK. Two
consequences: (i) a 40-year record is what makes a 0.2 K/decade rate precise to a
few mK; (ii) the *residual* size is not the trend's uncertainty. A trend is
reported with a standard error that depends on the residual autocorrelation, which
the sentence omits entirely.

**Spatial coverage.** The demo's cube is complete and the trend is spatially
uniform by construction. Real coverage is sparse and changes over time; the
coverage change is usually the dominant uncertainty in a global rate, and it is
invisible in a single number.

**Trend versus uncertainty.** "0.20 K/decade" is a point estimate. A defensible
sentence is of the form "0.20 ± 0.03 K/decade over 1985–2024, area-weighted, with a
1985–2014 baseline and a stated mask", which states the estimator, the period, the
weighting, the baseline and the uncertainty. The demonstration can supply four of
those five from measurement; the uncertainty requires an autocorrelation model and
is where the reasoning starts.
