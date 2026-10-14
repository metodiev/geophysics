---
id: 05-06-01
title: "The Processing Pipeline: Editing, Correction, Enhancement"
level: intermediate
prereqs: ["05-02-03", "05-02-04"]
tags: [processing, pipeline, filters, transfer-function, editing, levelling]
---

# The Processing Pipeline: Editing, Correction, Enhancement

## Learning objectives

By the end of this lesson you will be able to:

1. **Name** the stages of the universal processing chain and state, for each, what it
   assumes and what it destroys.
2. **Describe** a filter as a linear operator with a transfer function, and explain
   why filtering is never free.
3. **Order** a processing sequence correctly and explain why a different order gives
   a different result.
4. **Measure** the cost of each stage against a known truth, rather than judging a
   step by whether the output "looks better".
5. **Estimate** a robust noise scale from data containing spikes, and explain why
   the naive estimator fails.
6. **Choose** a filter cutoff from data rather than habit, and show the criterion.

## Prerequisites

- [05-02-03 Noise, Drift, Tides and Instrument Bias in Field Data](../02-geophysical-fields-and-observables/03-noise-and-drift.md)
  — what the pipeline is trying to remove.
- [05-02-04 Reduction of Observations to Anomalies](../02-geophysical-fields-and-observables/04-reduction-of-observations.md)
  — the corrections that must be applied before any enhancement.
- [01-10-03 Convolution, Filtering and the Convolution Theorem](../../01-mathematics/10-fourier-analysis/03-convolution.md)
  — the linear-operator view developed in Section 3.

## 1. Intuition: a pipeline is a sequence of irreversible decisions

Every processing step is a transformation that is applied to the data and cannot be
undone without loss, because the data are finite and no step is exactly invertible in
practice. The useful mental model is therefore not "cleaning the data" but a
**sequence of decisions, each of which removes something**:

| stage | typical operations | what it assumes | what it destroys |
|---|---|---|---|
| **1. edit / QC** | despike, kill bad traces, remove obvious glitches | spikes are rare, isolated and unrepresentative | the samples it removes, and the ability to prove they were wrong |
| **2. tie / level** | remove instrument drift, tie to a base, level lines to a datum | the drift and the mismatch are longer-wavelength than the signal of interest | long-wavelength signal, unavoidably |
| **3. filter** | band-pass, notch, f–k, spatial arrays | signal and noise occupy different parts of the spectrum | the amplitude and phase in the rejected band, plus part of the signal |
| **4. transform** | derivatives, analytic signal, continuation | a physical model of how the field behaves | nothing in principle, but the noise is amplified |
| **5. correct** | statics, NMO, free-air/Bouguer, terrain, Eötvös | a physical model, with stated parameters | the ability to reinterpret without re-doing the correction |
| **6. grid** | nearest, spline, kriging, minimum curvature | smoothness between samples | the honest admission of where data end and invention begins |
| **7. visualise** | contouring, colour stretch, illumination | nothing physical | the reader's ability to see anything outside the chosen scale |

The right question about any step is not "does the output look better?" but **"what
did I remove, and can I show that I did not need it?"** Sections 4–6 answer that
question numerically for a synthetic dataset whose answer is known.

## 2. Precise definitions

### 2.1 The general linear operator

Most of stages 2–5 are, or approximate, a **linear shift-invariant operator**

$$y(x) = \int h(x - x')\,d(x')\,\mathrm{d}x' = (h * d)(x) ,
\tag{1}$$

whose Fourier transform is a multiplication:

$$\hat y(k) = H(k)\,\hat d(k), \qquad H(k) = \frac{\hat y(k)}{\hat d(k)} ,
\tag{2}$$

where $H$ is the **transfer function**. Equation (2) is the operational definition
of a filter, and it is also the honest definition: a filter is *whatever it does to
the spectrum*, not the name on the processing menu.

### 2.2 Zero-phase and phase-shifting operators

$H(k)$ is in general complex, $H(k) = |H(k)|e^{\,i\phi(k)}$. A **zero-phase** operator
has $\phi \equiv 0$; it changes amplitudes but leaves every event at its recorded
time. A phase-shifting operator moves events, and the move is
frequency-dependent, which is why a causal filter applied "to make the data cleaner"
can shift and distort the very events it was meant to preserve.

### 2.3 Composition and order

Applying operators $A$ then $B$ gives $BA$ in the Fourier domain, i.e. a
multiplication of transfer functions. If $AB = BA$ the order does not matter; in
general it does, and the difference is a *different* processed dataset, not a
numerical subtlety. Section 7 measures the size of that difference.

## 3. Filters are not free

A filter with transfer function $H$ acts on signal **and** noise, and it acts on the
whole spectrum at once:

- **It distorts the signal** wherever $|H| \ne 1$, including inside the pass band.
  A Gaussian low-pass with cutoff $\lambda_c$ has
  $H(k) = \exp\!\left(-\tfrac12 (k/k_c)^{2}\right)$, so a signal component at
  $k = k_c$ is attenuated by a factor $e^{-1/2} = 0.607$ — 39 % of its amplitude
  removed at the nominal "cutoff".
- **It shifts phase** unless it is zero phase, moving events in time or space.
- **It correlates the noise.** Filtered noise is no longer independent between
  neighbouring stations; the effective number of independent samples falls, so a
  later $\sqrt{N}$ averaging gain is smaller than the count of samples suggests.
- **It changes the resolution.** Filtering to a longer wavelength is exactly the
  statement that the resolution is now that wavelength, whatever the station spacing.

The quantitative statement of the first point is the one to carry away: the
*amplitude loss* and the *noise reduction* are two numbers that must both be
reported, and Section 6 shows a dataset where a habitually chosen cutoff makes the
data worse.

## 4. A measured pipeline: what each stage costs

[`code/processing_pipeline_demo.py`](./code/processing_pipeline_demo.py) builds a
synthetic gravity profile whose truth is known: two buried spheres plus a smooth
regional trend, contaminated with three spikes, a linear drift and Gaussian noise
(*SYNTHETIC*: noise $\sigma = 0.008$ mGal, drift 0.02 mGal over the line, spikes
0.9, −0.7 and +1.4 mGal). The cumulative RMS error against the truth is the metric:

| stage | RMS error vs truth (mGal) |
|---|---|
| observed (raw) | 0.14377 |
| after edit (despike) | 0.05756 |
| after level (remove a straight line) | 0.01242 |
| after filter (best Gaussian low-pass) | 0.01177 |

That table is the shape of a good pipeline: a large improvement from the edit, a
larger one from levelling, and a small marginal one from filtering. It is also a
warning: the *filter* — the stage that field crews and processing reports emphasise —
contributed 5 % of the total improvement. Most of the value came from the two
unglamorous steps.

### 4.1 The edit stage, and a trap in the noise scale

The edit stage needs a scale to decide what is a spike. The naive choice is the
median absolute deviation (MAD) of the residual from a running median. The demo
measures that estimator and shows it fails:

| quantity | measured |
|---|---|
| difference-based $\hat\sigma$ | 0.01143 mGal (true input 0.00800) |
| naive running-median MAD scale | 0.00069 mGal — **17× too small** |
| samples a 4-sigma test on the naive scale would flag | 77 of 200 |
| samples flagged using the difference-based scale | 3 of 200, at indices 37, 121, 168 (the true spikes) |

The reason is structural, not a coding error: the residual from a running median is
**exactly zero whenever the sample happens to be the middle value of its own
window**, which occurs with probability $1/w$ for a window of $w$. A median-based
scale therefore sees a large point mass at zero and collapses. The robust remedy is
the successive-difference estimator

$$\hat\sigma = \frac{1.4826\,\operatorname{median}\lvert \Delta_i - \operatorname{median}(\Delta)\rvert}{\sqrt{2}},
\qquad \Delta_i = y_{i+1} - y_i ,
\tag{3}$$

which uses the fact that adjacent differences of white noise have standard deviation
$\sigma\sqrt{2}$. Equation (3) tolerates outliers in up to half the differences,
which is far more than any real survey needs.

The lesson generalises: **the estimate of the noise scale is itself a processing
decision with a measurable failure mode.** A pipeline that flags 77 of 200 samples as
spikes has replaced a third of the data with a smoothed version of itself, and it will
still produce a tidy-looking map.

### 4.2 The level stage, and the signal it removes

Levelling removes a straight line fitted to the quiet ends of the line:

| quantity | measured (mGal) |
|---|---|
| range of the removed straight line | 0.1162 |
| drift actually present in the data | 0.0995 |
| of the removed line, **true regional signal** removed as well | 0.0134 |

So levelling removed 17 % more than the drift: it took 0.0134 mGal of real
long-wavelength anomaly with it. That is unavoidable, and it is why the datum choice
is a scientific decision rather than a cosmetic one — the same argument, with
numbers, appears in
[05-06-03 Static Corrections, Datum and Elevation Effects](./03-static-and-datum.md).
The correct practice is to *report* the wavelength below which the data are no longer
trustworthy, not to pretend that levelling was free.

## 5. Choosing a filter cutoff from the data

The demo sweeps the cutoff wavelength of a zero-phase Gaussian low-pass over the
*levelled* profile and records both the noise on the quiet ends and the error against
the truth. Remember the convention: a **longer** cutoff wavelength is a **more
aggressive** filter, because it passes only wavelengths longer than $\lambda_c$.

| cutoff $\lambda_c$ (m) | noise on quiet ends (mGal) | anomaly peak (mGal) | peak error (%) | RMS vs truth (mGal) |
|---|---|---|---|---|
| none | 0.00814 | 1.2676 | −1.01 | 0.01242 |
| 20 | 0.00791 | 1.2673 | −1.03 | 0.01230 |
| 50 | 0.00697 | 1.2657 | −1.16 | 0.01183 |
| 100 | 0.00542 | 1.2608 | −1.54 | 0.01117 |
| **150** | **0.00439** | **1.2526** | **−2.18** | **0.01114** |
| 250 | 0.00301 | 1.2261 | −4.25 | 0.01309 |
| 400 | 0.00223 | 1.1693 | −8.69 | 0.02094 |
| 700 | 0.00240 | 1.0349 | −19.18 | 0.04591 |
| 1500 | 0.00427 | 0.7367 | −42.47 | 0.11346 |

Read the table three ways, because it contains three separate lessons.

1. **The error has a minimum at a mild cutoff (150 m here).** Below it the noise
   survives; above it the anomaly itself is removed. The criterion is measurable and
   the optimum is not a matter of taste.
2. **Aggressive filtering destroys the anomaly.** At $\lambda_c = 1500$ m the peak is
   down 42 % and the RMS error is nine times the unfiltered value. A filter chosen by
   habit rather than by spectrum makes the data worse, and the output still looks
   smooth and plausible.
3. **The "noise" column is not monotone.** Noise on the quiet ends *rises* again at
   the longest cutoffs (0.00223 at 400 m, then 0.00427 at 1500 m) because the
   Gaussian filter's own response at very long wavelengths is removing the regional
   trend, so what remains is no longer quiet. A noise estimate from a "quiet" part of
   a profile is only valid if the filter has not changed what is in it.

## 6. Transforms: the noise gain is not optional

Stage 4 (transform) is where a pipeline can silently destroy the data. The demo
measures the noise gain of a first derivative in the Fourier domain,
$\partial/\partial x \leftrightarrow i k$, on white noise, for several sample
spacings:

| $\Delta x$ (m) | measured gain | $\pi/(\Delta x\sqrt3)$ | $k_N$ (rad/m) |
|---|---|---|---|
| 10 | 0.18038 | 0.18138 | 0.31416 |
| 25 | 0.07263 | 0.07255 | 0.12566 |
| 50 | 0.03611 | 0.03628 | 0.06283 |
| 100 | 0.01810 | 0.01814 | 0.03142 |

The gain is the standard deviation of the differentiated noise divided by the
standard deviation of the input noise, and the prediction is derived in
[05-06-05](./05-merge-and-regularisation.md):

$$\text{gain} = \frac{k_N}{\sqrt{3}} = \frac{\pi}{\Delta x\sqrt3} .
\tag{4}$$

Measured and predicted agree to about 1 %. Two consequences:

- **The gain is independent of record length** and scales as $1/\Delta x$. Refining the
  grid does not make the derivative better; it multiplies the noise by a larger
  number.
- **Any transform must be band-limited first**, and the band limit is a stated
  wavelength that belongs in the processing report.

## 7. Order matters, and the difference is measurable

Operators do not commute in general, so the *sequence* is part of the processing.
The companion demo
[`code/processing_transparency_demo.py`](./code/processing_transparency_demo.py)
runs the same three steps in two orders and measures the difference: an RMS
difference of 0.007976 on a profile whose peak is 0.7765, i.e. **1.03 % of the
peak**, with a different output hash. The two results are different datasets. A
processing report that lists operations without their order has described a toolbox,
not a sequence.

The practical ordering rules follow from what each step assumes:

1. **Edit before anything that averages.** A spike inside a stack or a filter
   contaminates its neighbours; remove it while it is still local.
2. **Tie/level before filtering.** A trend is a long-wavelength term, and a filter
   that passes long wavelengths passes the trend too.
3. **Statics before stacking** (they must be, by definition of alignment).
4. **Filter before differentiating**, always.
5. **Grid last**, after all the corrections, because gridding is interpolation and
   interpolation of uncorrected data interpolates the errors too.

## 8. Assumptions

1. **Linearity and shift invariance** for equations (1)–(2). Time- or space-varying
   operators (a different filter per window, an f–k filter over a dipping event) are
   not described by a single $H(k)$ and must be documented window by window.
2. **The signal is band-limited below the noise-free region.** Filtering assumes
   signal and noise are separable in the transform domain. Where they overlap, the
   filter removes both.
3. **The truth is known here.** In the demo the RMS error against the truth is
   computable. In real data it is not, so the same reasoning must be applied through
   *forward modelling* and *repeatability*, not through visual smoothness.
4. **The noise is stationary.** A noise estimate from the quiet ends of a profile is
   applied everywhere in the sweep above; where the noise level varies across a map,
   the filter must vary too.
5. **Synthetic parameters are illustrative.** All numerical values in Sections 4–6 are
   from one synthetic dataset with stated parameters, not from a field survey.

## 9. Units and dimensional analysis

Transfer functions are dimensionless: $H = \hat y/\hat d$ with $y$ and $d$ in the same
unit. Operators that change the unit are *not* filters in this sense and must be
tracked:

$$\left[\frac{\partial}{\partial x}\right] = \mathrm{m^{-1}}, \qquad
\left[i k\right] = \mathrm{m^{-1}},$$

so a derivative's output is in the field unit per metre, and its noise gain in
equation (4) is in $\mathrm{m^{-1}}$ — which is why the numbers in the table have
units of per metre and why they change when $\Delta x$ changes. The RMS-error column
in Section 5 is in mGal, the same unit as the field, so it can be compared directly
with the anomaly peak.

## 10. Python demonstration

[`code/processing_pipeline_demo.py`](./code/processing_pipeline_demo.py) produces
every number in Sections 4–6. The robust scale and the zero-phase filter are short
enough to quote:

```python
def robust_sigma(y):                      # equation (3)
    d = np.diff(y)
    return 1.4826 * np.median(np.abs(d - np.median(d))) / np.sqrt(2.0)

def gaussian_lowpass(y, dx, cutoff_wavelength):
    k = 2 * np.pi * np.fft.rfftfreq(y.size, d=dx)
    kc = 2 * np.pi / cutoff_wavelength
    return np.fft.irfft(np.fft.rfft(y) * np.exp(-0.5 * (k / kc) ** 2), n=y.size)
```

`gaussian_lowpass` is real and symmetric, hence zero phase: it changes amplitudes and
does not move events.

## 11. Exercises, common mistakes, applications

Companion problem sets:
[`exercises/01-processing-pipeline-concept-exercises.md`](./exercises/01-processing-pipeline-concept-exercises.md)
and [`exercises/01-processing-pipeline-concept-solutions.md`](./exercises/01-processing-pipeline-concept-solutions.md).

### Common mistakes

1. **Judging a step by appearance.** A smoothed map that has lost 42 % of its anomaly
   peak still looks like a map.
2. **Reporting the noise reduction without the amplitude loss.** Both are consequences
   of the same transfer function.
3. **Using a median residual to estimate the noise scale.** Measured failure: 17× too
   small, 77 of 200 samples flagged.
4. **Levelling without recording what was removed.** The removed long-wavelength
   content is unavailable for later interpretation unless it is reported.
5. **Differentiating before band-limiting.** The measured $1/\Delta x$ gain of
   equation (4).
6. **Treating the order of steps as a presentation choice.** Measured difference
   1.03 % of the peak, and a different output hash.

### Real-world applications

- **Potential-field processing.** Reduction to a datum, levelling between survey
  lines and blocks, and derivative enhancement are the classical whole of the
  pipeline; each is one row of the table in Section 1.
- **Seismic processing.** The same seven stages exist with different names (edit,
  statics, deconvolution, NMO/stack, migration, display), and the same
  assumptions-versus-losses bookkeeping applies.
- **Airborne data.** Levelling between flight lines is stage 2, and it is usually the
  largest single manipulation of the data; its cost is the long-wavelength signal it
  removes.
- **Any reproducibility claim.** Once stages have an order and parameters, the
  sequence itself becomes a record that must be published — see
  [05-06-06](./06-processing-transparency.md).

## 12. Further reading

- **Blakely, R. J. (1995). *Potential Theory in Gravity and Magnetic Applications*.
  Cambridge University Press.** Chapters 8–10 on filters, continuation and
  derivatives as linear operators with stated transfer functions.
- **Yilmaz, Ö. (2001). *Seismic Data Analysis* (2nd ed.). SEG.** The canonical
  processing sequence, with each stage's assumptions stated. Level: advanced
  practitioner.
- **Telford, W. M., Geldart, L. P., & Sheriff, R. E. (1990). *Applied Geophysics*
  (2nd ed.). Cambridge University Press.** Chapters on data processing and
  enhancement in each method chapter.
- **Huber, P. J., & Ronchetti, E. M. (2009). *Robust Statistics* (2nd ed.). Wiley.**
  For robust scale estimators such as equation (3) and their breakdown behaviour.
  Level: advanced.
- **USGS, potential-fields processing notes** — <https://www.usgs.gov> — practical
  descriptions of levelling and gridding as applied in national programmes.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text, and you should
> confirm current availability and editions through your library before citing them.

## 13. Related lessons

- [05-06-02 Noise Suppression: Stacking, Filtering, Median, KL Transform](./02-noise-suppression.md) — the filter stage in detail.
- [05-06-03 Static Corrections, Datum and Elevation Effects](./03-static-and-datum.md) — the ordering constraint that statics impose.
- [05-06-05 Gridding, Merging and Levelling of Survey Data](./05-merge-and-regularisation.md) — the gridding stage and the derivative gain of equation (4).
- [05-06-06 Documenting Processing: Reproducibility in Practice](./06-processing-transparency.md) — recording the order and the parameters.
- [01-10-03 Convolution, Filtering and the Convolution Theorem](../../01-mathematics/10-fourier-analysis/03-convolution.md) — the mathematics of equations (1)–(2).

## 14. Self-assessment checklist

- [ ] I can name the seven stages and, for each, one assumption and one loss.
- [ ] I can explain why a filter is defined by its transfer function rather than by its name.
- [ ] I can state the amplitude loss at the cutoff of a Gaussian low-pass.
- [ ] I can compute a robust noise scale that survives spikes, and explain why the median residual does not.
- [ ] I can choose a cutoff from an RMS-versus-cutoff curve and justify the criterion.
- [ ] I can compute the noise gain of a first derivative and say how it scales with station spacing.
- [ ] I can give the ordering rules and the reason for each.
- [ ] I can state what my pipeline removes and how I would show that the removal was safe.
