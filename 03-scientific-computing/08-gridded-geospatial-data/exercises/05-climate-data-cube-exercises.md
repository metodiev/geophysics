# Exercises — 03-08-05 Case Study: Analysing a Climate Data Cube

Attempt these **closed-book** before opening the
[solutions](./05-climate-data-cube-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems that say "run the demo" refer to
[`../code/climate_data_cube_demo.py`](../code/climate_data_cube_demo.py); report
its **actual** output. The cube is **SYNTHETIC** (480 months, 36 latitudes, 72
longitudes) with an imposed trend, seasonal cycle, oscillation and noise. No real
dataset is read and nothing is downloaded.

---

## ★ Foundational

**★1.** State the five terms the synthetic cube is built from and the imposed
amplitude of each.

**★2.** A series has a linear trend of 0.20 K/decade. A baseline is centred 5 years
before the record's centre. What is the mean anomaly of the record, and why?

**★3.** Explain in one sentence why a complete annual mean of a monthly series does
not need to be deseasonalised, and what "complete" means.

**★4.** Define a regression map and say what the correlation coefficient means at a
single grid point.

---

## ★★ Applied

**★★5.** Run the demo, Sections 2 and 3.
(a) Report the whole-record anomaly mean, the baseline anomaly mean and the
baseline residual standard deviation.
(b) The imposed noise is 0.35 K. Compute the signal standard deviation in
quadrature and state what contributes it.
(c) Report the recovered trend under both weightings, the imposed value, and both
percentage errors.

**★★6.** Run the demo, Section 3.
(a) Report the residual rms under the naive and weighted means.
(b) Give the cancellation arithmetic for $\cos 2\phi$ on a 36-row uniform latitude
grid (unweighted and weighted).
(c) State why the naive mean's smoother residual is *not* evidence of a better
analysis.

**★★7.** Run the demo, Section 4.
(a) Report the raw annual trend and the January+July-only trend.
(b) Compute the percentage bias of the subsampled trend.
(c) Explain the mechanism in terms of the seasonal phase.

**★★8.** Run the demo, Section 5.
(a) Report the measured peak |r|, its location, and the two band maxima.
(b) Reproduce the a-priori prediction ($\sigma_{\text{index}} = 0.3958$ K, local
signal $= 1.4|\cos 2\phi|\sigma$, noise 0.35 K) and give the predicted r.
(c) State the agreement between prediction and measurement.

---

## ★★★ Research-oriented

**★★★9.** Reproduce the demonstration's cube with a **non-uniform** latitude grid
(for example Gaussian, dense at the equator) and re-run the trend recovery under
both weightings. Report both trends, both residual rms values and the naive-versus-
weighted trend gap. Then explain, in terms of the weighting kernel and the imposed
$\cos 2\phi$ pattern, why the gap changes.

**★★★10.** The lag correlation decays monotonically from +0.2917 to +0.0003 over
12 months. Replace the Gaussian-envelope oscillation with a pure 48-month sinusoid
of the same amplitude and re-measure the lag profile at lags 0, 6, 12, 18, 24. Then
state which observable distinguishes "an amplitude-modulated signal" from "a
stationary periodic signal" in a lag-correlation table, and why that distinction
matters for a claim that a signal "propagates".

**★★★11.** Write a 350–500 word critical appraisal of the sentence: *"The global
temperature anomaly trend is 0.20 K/decade."* Address at least: the baseline
choice, the weighting, the mask, the record length, the spatial coverage, and the
difference between the trend and its uncertainty. Use the measured numbers from the
demo wherever they bear on the point, and mark clearly where you are reasoning
rather than measuring.
