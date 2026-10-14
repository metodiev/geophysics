---
id: 08-02-06
title: "Magnetic Survey Design, Diurnal Correction and Levelling"
level: advanced
prereqs: ["08-02-02", "08-01-04", "08-02-05"]
tags: [geomagnetism, surveys, diurnal-correction, levelling, base-station, error-budget, qc]
---

# Magnetic Survey Design, Diurnal Correction and Levelling

A magnetic survey produces a grid of anomalies, and the path from a sensor
reading to that grid is a sequence of subtractions, each with its own time
constant and its own spatial signature: remove the instrument's offset, remove the
diurnal variation, remove the main field, remove the line-to-line level errors.
This lesson treats that chain as an error-budget problem. Every step is quantified
with a synthetic example, and the lesson's conclusion is the one that matters in
practice: the largest term in the budget is almost never the instrument.

**All models and data in this module are SYNTHETIC.** The diurnal signal, survey
geometry, drift, noise, geology and error terms are chosen teaching values. The
only standard value used is the Earth radius $6371\ \mathrm{km}$, with the
synthetic axial dipole coefficient of module 08-01.

## Learning objectives

By the end of this lesson you will be able to:

1. **Construct** a diurnal correction from a base station and **compute** the
   residual left by a timing lag.
2. **Compute** the main field's spatial gradient from a dipole model and quantify
   what an epoch error does to a survey — and what it does not do.
3. **Set up** a tie-line levelling adjustment, read its residuals, and state what
   a levelling solution determines and what it assumes.
4. **Apply** the quarter-wavelength rule to line spacing and along-line sampling.
5. **Check** repeatability and compare it with the expected noise.
6. **Build** an error budget in quadrature and identify the dominant term.

## Prerequisites

- [08-02-02 Proton Precession and Overhauser Magnetometers](02-proton-overhauser.md) —
  the scalar readings the chain starts from.
- [08-01-04 Secular Variation, Jerks and Core Dynamics](../01-earth-magnetic-field/04-secular-variation.md) —
  the time dependence that the epoch error refers to.
- [08-02-05 Airborne Magnetic Surveys and Compensation](05-airborne-magnetic-surveys.md) —
  the airborne instance of the same processing chain.

## 1. The measurement chain

Starting from a sensor reading $R(t)$ at position $\mathbf{x}$:

$$R(t) = \underbrace{B_{\text{main}}(\mathbf{x},t)}_{\text{model}}
+ \underbrace{D(t)}_{\text{diurnal}}
+ \underbrace{A(\mathbf{x})}_{\text{anomaly}}
+ \underbrace{\epsilon}_{\text{noise and error}},$$

and the survey wants $A$. Every term on the right must be either modelled,
measured elsewhere, or made small:

| step | removes | how | typical instrument |
|---|---|---|---|
| instrument offset and drift | $\epsilon$ | repeat readings, calibration | reference reading |
| diurnal correction | $D(t)$ | a base station recording simultaneously | magnetometer at a quiet site |
| main-field removal | $B_{\text{main}}$ | a reference field model at the right epoch and position | Gauss coefficients |
| levelling | line-to-line level errors | tie lines and a least-squares adjustment | the survey itself |
| sampling | aliasing | the quarter-wavelength rule | design |

The rest of the lesson takes them in turn.

## 2. Diurnal correction, and the cost of a timing lag

The external field's daily variation is of order tens of nanotesla — thousands of
times the resolution of a modern sensor. It cannot be removed by the sensor, so it
is **measured** at a base station and subtracted from the field readings. The
correction is

$$A(\mathbf{x},t) = R(\mathbf{x},t) - B_{\text{main}} - D_{\text{base}}(t),$$

which is exact only if the base station's variation is the same as the field
site's — an assumption about spatial uniformity — and only if the two are
**synchronised**.

The demonstration's SYNTHETIC diurnal signal (an $18\ \mathrm{nT}$ daily wave plus
a $4.5\ \mathrm{nT}$ semi-diurnal wave) spans $23.413\ \mathrm{nT}$ over an
8-hour survey. Correcting with a base reading taken at a lag:

| lag (min) | residual rms (nT) | residual peak (nT) |
|---|---|---|
| 0 | 0.0000 | 0.0000 |
| 1 | 0.0081 | 0.0638 |
| 5 | 0.0406 | 0.3192 |
| 15 | 0.1235 | 0.9572 |
| 30 | 0.2511 | 1.9124 |

Three points:

- **The residual is the time derivative of the diurnal signal times the lag.**
  For a harmonic of angular frequency $\omega$ and amplitude $\alpha$, the
  residual is $\alpha\,2\sin(\omega\delta/2) \approx \alpha\omega\delta$: linear
  in the lag. The table shows exactly that scaling up to 15 minutes
  ($0.0406 \to 0.1235$ for $5 \to 15$ minutes).
- **Zero lag is exact by construction**, and the correction's quality is therefore
  a *clock* question, not a magnetometer question. A GPS-disciplined clock is the
  cheapest component in the chain and one of the most important.
- **A residual of $0.96\ \mathrm{nT}$ at the worst moment is not noise**: it is
  smooth in time, so along a line it appears as a ramp, indistinguishable from a
  geological gradient over a few hundred metres. That is why the base station's
  clock and the interpolated correction matter more than its sensor's resolution.

**What makes a good base site.** Magnetically quiet (no nearby sources, no
cultural noise), geologically uninteresting, and within the region where the
diurnal variation may be assumed uniform — which is a statement about the
*external* field's spatial scale (thousands of kilometres), not about the geology.
A second base station is the standard check: if the two disagree beyond their
noise, the assumption is failing and the region is too large for a single-station
correction.

## 3. Main-field removal: the gradient, and the epoch error

The main field varies across a survey. From the synthetic axial dipole,
$F(\lambda) = |g_1^0|\sqrt{1+3\sin^{2}\lambda}$, so

$$\frac{\mathrm{d}F}{\mathrm{d}\lambda}
= |g_1^0|\frac{3\sin\lambda\cos\lambda}{\sqrt{1+3\sin^{2}\lambda}}.$$

The demonstration evaluates this:

| latitude (°) | $F$ (nT) | north–south gradient (nT/km) |
|---|---|---|
| 0 | 30000.00 | 0.0000 |
| 30 | 39686.27 | 4.6240 |
| 45 | 47434.16 | 4.4672 |
| 60 | 54083.27 | 3.3931 |

At $45^{\circ}$ the gradient is $4.47\ \mathrm{nT\,km^{-1}}$, so a 20 km
north–south survey spans **89.3 nT** of main field — larger than most targets.
The removal therefore cannot be omitted, and its accuracy matters as much as the
sensor's.

### 3.1 What an epoch error does, and what it does not

Suppose the model is applied 5 years out of date with a secular variation of
$-34\ \mathrm{nT\,yr^{-1}}$: the error in $g_1^0$ is

$$\Delta g_1^0 = -34\times5 = -170\ \mathrm{nT}.$$

The resulting field error across the survey is $\Delta g_1^0$ times the *shape
factor* $\sqrt{1+3\sin^{2}\lambda}$, which the demonstration finds changes by
**0.1883%** over the $0.18^{\circ}$ of latitude spanned by 20 km. So the error
varies by only

$$170\times0.001883 = 0.320\ \mathrm{nT}$$

across the area: **an epoch error is a uniform offset over a survey area.** Two
consequences that are easy to get wrong:

- **A uniform offset is absorbed by levelling** and does not distort the anomaly,
  so an out-of-date epoch does not wreck a local anomaly map.
- **What does distort a map is a non-uniform model error**: a wrong datum
  (mis-referenced coordinates), a model applied outside its validity in
  *position*, or a truncated model whose omitted terms vary across the area. Those
  produce gradients, and levelling cannot distinguish them from geology.

The distinction is worth stating as a rule: **offsets are levelling problems,
gradients are model problems.**

## 4. Levelling

Levelling determines and removes a constant offset per flight line (or per survey
day) by using **tie lines** that cross the survey lines. At each crossing the two
lines should agree after the geology is accounted for; the disagreement is a
**mistie**.

The demonstration builds a SYNTHETIC survey of 5 lines $\times$ 25 stations with
10 tie-line crossings, injecting line offsets of $0$, $+3.2$, $-1.7$, $+5.5$ and
$-2.4\ \mathrm{nT}$ (the kind of residual a diurnal correction leaves behind):

| quantity | value |
|---|---|
| rms mistie at the crossings, raw | 5.2222 nT |
| adjusted offsets | $-0.00$, $+4.28$, $-0.62$, $+7.38$, $-1.03$ nT |
| true minus adjusted | $0.00$, $-1.08$, $-1.08$, $-1.88$, $-1.37$ nT |
| rms mistie after adjustment | 0.5285 nT |

Reading the table:

- **The adjustment drives the misties to $0.53\ \mathrm{nT}$**, close to the
  tie-line reading noise. The *differences* between lines are therefore well
  determined.
- **The absolute offsets are recovered only to 1–2 nT.** With 10 crossings, five
  unknown offsets and one fixed datum, the network is barely over-determined; the
  absolute level is as good as the datum assumption, and the datum is a choice
  (usually "the first line is correct").
- **A levelling solution is a statement about relative levels**, and its residual
  is the honest measure of its quality. Reporting the adjusted offsets without
  the residual is reporting a fit without its misfit.

The demonstration's numbers also show why levelling *cannot* fix a per-line
gradient: the model being fitted is one constant per line, so any within-line
error (a diurnal ramp, a drape effect) survives the adjustment untouched. That is
why the diurnal correction of §2 must be done properly first.

## 5. Sampling

The rule is the same as for line spacing in
[08-02-05](05-airborne-magnetic-surveys.md) §6, applied in both directions:

| shortest target wavelength (m) | sample interval (m) | Nyquist wavelength (m) |
|---|---|---|
| 50 | 12.5 | 25 |
| 100 | 25 | 50 |
| 200 | 50 | 100 |
| 500 | 125 | 250 |

A 50 m target needs a $12.5\ \mathrm{m}$ sample interval — a walking survey.
From an aircraft, the same target cannot be resolved at any line spacing, and a
survey that claims it is claiming an interpolation. **The sampling rule is a
statement about what the survey can see, and it belongs in the report.**

## 6. Quality control: repeatability and the error budget

**Repeatability.** The demonstration's SYNTHETIC repeat measurement of 20 stations
gives

$$\text{mean difference} = -0.2539\ \mathrm{nT}, \qquad
\text{standard deviation} = 0.7722\ \mathrm{nT},$$

against the expected $0.7071\ \mathrm{nT}$ for two independent readings with
$0.5\ \mathrm{nT}$ noise each ($\sqrt{2}\times0.5$). The measured 0.77 is 9%
above expectation — consistent with the sample's own scatter ($1/\sqrt{2N} = 16\%$
for $N = 20$), so the instrument is behaving. **The test is a comparison, not a
number**: reproducibility above the noise model means an unmodelled effect
(diurnal residual, positioning error, sensor settling), and the comparison
identifies it.

**Error budget.** Combine contributions in quadrature (independent errors):

| contribution | standard uncertainty (nT) |
|---|---|
| instrument noise | 0.10 |
| orientation / levelling of the sensor | 0.50 |
| diurnal correction residual | 1.00 |
| main-field model removal | 0.50 |
| levelling and tie-line adjustment | 2.00 |
| **quadrature sum** | **2.35** |

The dominant term is the levelling adjustment at $2.00\ \mathrm{nT}$, and the
instrument contributes only $0.18\%$ of the variance:

$$\frac{0.10^{2}}{2.35^{2}} = 0.00181.$$

**This is the practical punchline of the module.** A survey that buys a
ten-times-better magnetometer and does not improve its levelling, its diurnal
correction or its tie-line network buys almost nothing. An error budget costs an
afternoon and tells you where to spend the rest of the project's money.

## 7. Assumptions and regime of validity

1. **The diurnal variation is uniform over the survey area.** True for the
   external part; a second base station is the test. Electrojet and coastline
   effects break it.
2. **The clocks are synchronised and the base record is interpolated.** Section 2
   prices the failure.
3. **The reference field model is applied at the right position and epoch.** §3.1
   distinguishes the two failure modes.
4. **Line offsets are constant along each line.** If they are not, their residual
   appears as a gradient and levelling cannot remove it.
5. **The tie-line network is rich enough.** Its geometry sets the conditioning of
   the adjustment, which §4 quantifies with a residual.
6. **Errors are independent and combine in quadrature.** Correlated errors (a
   mis-set heading, a wrong coordinate datum) do not, and must be modelled
   separately.
7. **Synthetic parameters.** Every number here is a teaching value.

## 8. Python demonstration

`code/magnetic_survey_procedures_demo.py` prints, with units:

1. the synthetic diurnal signal, its span, and the residual after correction with
   five different lags;
2. the main-field north–south gradient at four latitudes, the span over a 20 km
   survey, and the *variation* of an epoch error across the same distance;
3. a tie-line levelling adjustment with raw and adjusted misties and the residual
   offsets;
4. the sampling rule table;
5. a repeatability check against the expected noise;
6. an error budget in quadrature with the dominant term identified.

Exercises and solutions:
[`exercises/06-magnetic-survey-procedures-exercises.md`](./exercises/06-magnetic-survey-procedures-exercises.md),
[`exercises/06-magnetic-survey-procedures-solutions.md`](./exercises/06-magnetic-survey-procedures-solutions.md).

## Mastery checkpoint

1. A diurnal signal is a $20\ \mathrm{nT}$ sinusoid of 24-hour period. Compute
   the residual left by a 10-minute lag.
2. Compute the main-field gradient in nT/km at $40^{\circ}$ latitude for the
   synthetic dipole, and the span across a 30 km survey.
3. Distinguish, with numbers, an epoch error of 3 years at
   $-40\ \mathrm{nT\,yr^{-1}}$ from a wrong-position error of 1 km at
   $4.5\ \mathrm{nT\,km^{-1}}$.
4. A levelling adjustment of six lines leaves a residual mistie of
   $0.4\ \mathrm{nT}$. State what it does and does not determine.
5. An error budget has contributions 0.2, 0.8, 1.5 and 0.3 nT. Compute the
   quadrature sum and identify the dominant term's share of the variance.

## Common pitfalls

1. **Correcting for the diurnal variation with an un-synchronised base.** Section
   2 gives the cost per minute of lag.
2. **Blaming an anomaly on geology when it is a levelling residual.** If it
   repeats line-to-line, it is processing.
3. **Treating a model's epoch as cosmetic.** It is a $170\ \mathrm{nT}$ offset in
   the example — absorbed by levelling, but only if levelling is done.
4. **Reporting levelled data without the residual.** The residual is the
   uncertainty.
5. **Sampling at Nyquist.** It is the aliasing threshold, not a design target.
6. **Buying resolution.** §6's budget shows where the variance actually lives.

## Related modules

- [08-02-05 Airborne Magnetic Surveys and Compensation](05-airborne-magnetic-surveys.md) —
  the same chain with an aircraft in the loop.
- [08-02-02 Proton Precession and Overhauser Magnetometers](02-proton-overhauser.md) —
  the readings, and their noise.
- [08-01-02 The Geocentric Dipole, IGRF and WMM Models](../01-earth-magnetic-field/02-dipole-and-igrf.md) —
  the reference models and epochs that §3 removes.
- [05-05-05 Acquisition QC: Noise Tests, Repeatability, Metadata](../../05-core-geophysics/05-survey-design-and-acquisition/05-quality-control.md) —
  the general QC framework.
- [05-06-02 Noise Suppression and Processing Principles](../../05-core-geophysics/06-data-processing-principles/02-noise-suppression.md) —
  what comes after levelling.

## Self-assessment checklist

- [ ] I can build and price a diurnal correction.
- [ ] I can compute a main-field gradient and separate an offset error from a
      gradient error.
- [ ] I can set up and read a levelling adjustment.
- [ ] I can apply the sampling rule in both directions.
- [ ] I can run and interpret a repeatability check.
- [ ] I can build an error budget and say where the money should go.
