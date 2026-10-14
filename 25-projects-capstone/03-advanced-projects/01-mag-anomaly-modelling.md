---
id: 25-03-01
title: "Project: Magnetic Anomaly Modelling and Depth Estimation"
level: advanced
prereqs: ["25-02-02", "08-01-02", "08-03-06", "01-10-06"]
estimated_minutes: 180
tags: [projects, magnetics, potential-fields, analytic-signal, depth, teaching]
---

# Project: Magnetic Anomaly Modelling and Depth Estimation

## Learning objectives

1. **Write** the total-field anomaly of a 2-D dipole line and **show** how remanence skews it in
 position and amplitude.
2. **Derive** the Hilbert-transform relation between the horizontal and vertical derivatives of
 a 2-D potential field, and **use** it to compute the analytic signal amplitude from one
 profile.
3. **Show** analytically that the analytic signal of a line source is a Lorentzian whose half-
 width is the source depth.
4. **Invert** the analytic signal for position and depth by a linear fit of $1/|\mathrm{AS}|$ to
 a parabola, and **report** both quantities with uncertainties.
5. **Measure** the bias that a linear regional trend introduces, and **show** that a constant
 regional level introduces none.
6. **Estimate** the depth uncertainty by Monte Carlo over the noise, and **distinguish** it from
 the systematic bias from smoothing and trend absorption.

## Prerequisites

- [25-02-02 Project: Gravity Anomaly of Simple Bodies](../02-intermediate-projects/02-simple-gravity-model.md) —
  the half-width depth logic that this project transfers to a skewed field.
- [08-01-02 The Geocentric Dipole, IGRF and WMM Models](../../08-geomagnetism-electromagnetism/01-earth-magnetic-field/02-dipole-and-igrf.md) —
  the core field that must be removed before an anomaly exists.
- [08-03-06 Magnetic Inversion and Its Non-Uniqueness](../../08-geomagnetism-electromagnetism/03-magnetic-anomalies-and-modelling/06-magnetic-inversion.md) —
  what the inverted model does and does not represent.
- [01-10-06 Hilbert Transform, Analytic Signal and Instantaneous Phase](../../01-mathematics/10-fourier-analysis/06-hilbert-transform.md) —
  the transform used to obtain the vertical derivative.

## 1. The question

*How deep is the magnetic source, when the direction of its magnetisation is
unknown?*

Magnetic interpretation has one difficulty that gravity does not: the anomaly
depends on the **direction** of magnetisation as well as its magnitude. Induced
magnetisation in a mid-latitude survey is not vertical, and remanent
magnetisation can point anywhere, so the anomaly of a compact body is neither
symmetric nor centred above it. Any depth rule based on the anomaly's own shape
therefore returns a *biased* depth. The project's answer is the **analytic
signal**, which is independent of magnetisation direction for a 2-D source, and
its measured superiority over the anomaly's own half-width.

## 2. The data

**Synthetic sources.** Two 2-D dipole lines at 4.0 km depth with a strength of
$1000\ \mathrm{nT\,km}$: body A at $x = -8.0\ \mathrm{km}$ with zero skew
(induced, symmetric) and body B at $x = +8.0\ \mathrm{km}$ with a $40°$ skew
(remanence). The profile runs from $-40$ to $+40\ \mathrm{km}$ at 0.2 km sampling
(401 samples), with a $60\ \mathrm{nT}$ constant regional level, a trend of
$1.5$–$8.0\ \mathrm{nT\,km^{-1}}$ and $0.5\ \mathrm{nT}$ of measurement noise.

**Real data for the project itself.** Aeromagnetic and ship-track data are
distributed by national geological surveys and compiled by the NOAA National
Geophysical Data Center; the anomalies must first be reduced to a common
datum and have the IGRF core field removed using the coefficients published at
<https://www.ngdc.noaa.gov/IAGA/vmod/igrf.html>.

**Provenance.** SYNTHETIC. The bodies are idealised lines, the "remanence" is a
chosen rotation of the magnetisation vector, and no number below is a property of
any real magnetic source.

## 3. The project specification

**Steps.**

1. Generate the profile for a symmetric and a skewed source; report each peak,
   its position and its half-width.
2. Compute $\partial T/\partial x$ by a short moving-average-then-difference
   derivative, and $\partial T/\partial z$ as minus its Hilbert transform;
   verify the pair numerically.
3. Form $|\mathrm{AS}| = \sqrt{(\partial T/\partial x)^{2} + (\partial T/\partial z)^{2}}$
   and locate its peak.
4. Fit $1/|\mathrm{AS}|$ to a parabola over a window around the peak and convert
   the coefficients to $(k, x_0, z)$. Report $x_0$ and $z$ with their units.
5. Add a constant regional level, then a linear trend; estimate the depth with and
   without removing the trend, for two trend magnitudes.
6. Repeat the estimate over 200 noise realisations and report the mean and the
   scatter; compare the scatter with the residual bias.
7. Write the report: the profile, the two gradients, $|\mathrm{AS}|$, the fitted
   $(x_0, z)$, the bias budget and the validity range.

**Deliverable.** The profile and gradient pair, the $|\mathrm{AS}|$ curve with the
fitted Lorentzian, a table of the depth estimates under four conditions, and the
Monte Carlo uncertainty.

**Success criterion.** The depth is reported with (i) a statistical uncertainty
from the Monte Carlo, (ii) a systematic bias from the smoothing and the trend
treatment, and (iii) the statement that the estimate is for a 2-D source.

## 4. The anomaly of a 2-D source, and how skew spoils it

For a 2-D line of dipoles at depth $z$ and position $x_0$, with a magnetisation
direction making an angle $\theta$ with the vertical in the profile plane, the
total-field anomaly is

$$T(x) = k\,\frac{z\cos\theta + (x-x_0)\sin\theta}{(x-x_0)^{2}+z^{2}}.$$ At $\theta = 0$ this is a symmetric Lorentzian of half-width exactly $z$, so
$z = x_{1/2}$. At $\theta = 40°$ it is skewed: the demonstration's body B peaks at
$x = 9.40\ \mathrm{km}$ — displaced $+1.40\ \mathrm{km}$ from its true position —
reaches $-29.2\ \mathrm{nT}$ on its far side, and has a half-width of
$4.594\ \mathrm{km}$ against the true depth of $4.0\ \mathrm{km}$, a
**$+14.8\%$ depth bias** produced entirely by the magnetisation direction. The lesson is structural: **the anomaly's shape encodes the magnetisation
direction as well as the geometry**, and any method that reads the shape without
separating the two is biased by an amount that cannot be estimated from the
profile alone.

## 5. The analytic signal

A magnetic field outside its sources is harmonic in the half-space, so its
horizontal derivative $u = \partial T/\partial x$ and vertical derivative
$v = \partial T/\partial z$ satisfy the Cauchy–Riemann pair. In the Fourier
domain this gives

$$v = -\mathcal{H}(u),$$

with $\mathcal{H}$ the Hilbert transform. The **analytic signal amplitude** is

$$|\mathrm{AS}(x)| = \sqrt{u(x)^{2} + v(x)^{2}}
= \left|u(x) + i\,v(x)\right|.$$

For the line source above, both derivatives are available in closed form and the
result is a pure Lorentzian:

$$\left|\mathrm{AS}(x)\right| = \frac{k}{(x-x_0)^{2} + z^{2}},$$

**independent of $\theta$**. Its peak sits exactly over the source, and its
half-width is exactly the depth. For the demonstration's skewed body B:

| quantity | anomaly $T$ | $|\mathrm{AS}|$ |
|---|---|---|---|
| peak position (km) | 9.40 (true 8.00) | 8.00 (true 8.00) |
| half-width (km) | 4.594 | 4.160 |
| implied depth (km) | 4.594 ($+14.8\%$) | 4.160 ($+4.0\%$) |
| exact peak value ($\mathrm{nT\,km^{-1}}$) | — | $k/z^{2} = 62.5000$ |

The measured $|\mathrm{AS}|$ peak is $61.1388\ \mathrm{nT\,km^{-1}}$ against the
exact $62.5000$; the deficit is the finite-difference and smoothing loss, and it
is the origin of the residual $+4\%$ bias.

## 6. Inverting the analytic signal

Because $|\mathrm{AS}|$ is a Lorentzian, its reciprocal is a **parabola**:

$$\frac{1}{|\mathrm{AS}(x)|} = \frac{(x-x_0)^{2}+z^{2}}{k}
= \frac{1}{k}x^{2} - \frac{2x_0}{k}x + \frac{x_0^{2}+z^{2}}{k},$$

so a weighted least-squares fit of $1/|\mathrm{AS}|$ to
$ax^{2}+bx+c$ gives

$$k = \frac{1}{a}, \qquad x_0 = -\frac{b}{2a}, \qquad
z^{2} = \frac{c}{a} - x_0^{2}.$$

Weights are $|\mathrm{AS}|^{4}$ at each sample, because
$\sigma(1/|\mathrm{AS}|) \propto \sigma_{\mathrm{AS}}/|\mathrm{AS}|^{2}$.
The fit is **linear**, so there is no starting model and no local minimum — which
is why this estimator is preferred to a non-linear inversion of the same curve. Applied to body B over a $\pm 12\ \mathrm{km}$ window, the fit gives
$x_0 = 7.944\ \mathrm{km}$ and $z = 4.137\ \mathrm{km}$ against the true
$8.0$ and $4.0\ \mathrm{km}$.

## 7. Regional fields: what survives a derivative and what does not

A **constant** regional level vanishes when the profile is differentiated, so it
costs the depth estimate nothing. A **linear** trend does not: it contributes a
constant $c = \mathrm{d}T_\text{reg}/\mathrm{d}x$ to $\partial T/\partial x$,
which enters $|\mathrm{AS}|$ as $\sqrt{(u+c)^{2} + \mathcal{H}(u+c)^{2}}$ and
distorts the Lorentzian shape.

The demonstration measures this directly, with the same noise realisation:

| trend (nT km⁻¹) | $z$ without removal (km) | $z$ after removal (km) | bias, raw |
|---|---|---|---|
| 1.5 | 4.201 | 4.195 | $+5.0\%$ |
| 8.0 | 4.515 | 4.195 | $+12.9\%$ |

Removing the trend reduces the bias to $+4.9\%$, which is the residual from the
short smoothing filter; leaving it in costs $12.9\%$ at
$8\ \mathrm{nT\,km^{-1}}$. **The trend must be removed before the analytic signal
is computed**, and the removal is a modelling choice that absorbs part of the
anomaly's own long-wavelength tail — which is why the profile should extend
several source depths beyond the anomaly. Note also that de-trending does not recover the *positions*: the Monte Carlo
gives $x_0 = -8.121 \pm 0.009\ \mathrm{km}$ against a true $-8.0\ \mathrm{km}$, a
bias of $-0.121\ \mathrm{km}$ that is thirteen times its own scatter. Both biases
are systematic, and both come from the same cause: the derivative is computed on
sampled, smoothed data.

## 8. The uncertainty: statistical against systematic

Over 200 noise realisations of the same model, with the trend removed each time:

$$z = 4.181 \pm 0.017\ \mathrm{km}\ (\text{true } 4.0),
\qquad
\text{bias } +4.5\%,$$

$$x_0 = -8.121 \pm 0.009\ \mathrm{km}\ (\text{true } -8.0),
\qquad
\text{bias } -0.121\ \mathrm{km}.$$

The Monte Carlo uncertainty of $\pm 0.017\ \mathrm{km}$ is **25 times smaller**
than the $+0.181\ \mathrm{km}$ bias. Reporting "$z = 4.18 \pm 0.02\ \mathrm{km}$"
would therefore be wrong in the way that matters: the dominant error is the
estimator's, not the data's, and only a better derivative, a longer profile, or a
2-D rather than profile-based treatment reduces it.

## 9. Failure modes and how to detect them

1. **A depth from the anomaly's own half-width.** *Detect:* compare with the
   $|\mathrm{AS}|$ half-width; the demonstration's gap is $4.594$ against $4.160\
   \mathrm{km}$.
2. **An unremoved linear trend.** *Detect:* refit the trend and the depth
   together; the demonstration's $8\ \mathrm{nT\,km^{-1}}$ case moves from $4.515$
   to $4.195\ \mathrm{km}$.
3. **An over-smoothed derivative.** *Detect:* halve the smoothing length and
   compare; a depth that moves by more than its stated uncertainty is
   smoothing-limited.
4. **A profile shorter than a few source depths.** *Detect:* compare the profile
   half-length with $3z$; the demonstration's $40\ \mathrm{km}$ spans ten source
   depths, but a $10\ \mathrm{km}$ profile would not define the Lorentzian's wings
   and the fit's $a$ coefficient would be unstable.
5. **Treating a 3-D source as 2-D.** *Detect:* the Hilbert relation used here is
   exact only for profiles perpendicular to a strike-infinite source; a compact
   body has a different signature, and a map-based 3-D approach is required.
6. **Reporting $k$ as a magnetisation.** $k$ is an amplitude with units of
   $\mathrm{nT\,km}$ per unit profile; converting it to a magnetisation requires a
   source geometry, which is what the inversion assumed in the first place.

## 10. Rubric

| Criterion | 4 — exemplary | 3 — competent | 2 — developing | 1 — incomplete |
|---|---|---|---|---|
| Gradients | Both computed, Hilbert relation verified | Both computed | Horizontal only | Numerical gradient of $T$ |
| $|\mathrm{AS}|$ | Peak located, units of nT/km | Curve plotted | Mentioned | Absent |
| Fit | Linear fit with weights, $(x_0,z)$ and units | Fit | Peak-to-half-width | Eyeballed |
| Trend | Bias measured at two trend magnitudes, both treatments | Trend removed | Trend mentioned | Ignored |
| Uncertainty | Monte Carlo plus a separate systematic term | Monte Carlo | Stated | Absent |

## 11. Assumptions and regime of validity

1. **A 2-D source.** The Hilbert relation is exact only for a field independent of
   the strike direction; a compact body breaks it and the recovered depth becomes
   a shape-dependent average.
2. **A dipole line.** A finite-width body has a different $\mathrm{AS}$ shape once
   the profile distance is comparable to its width, and the depth returned is then
   the depth to the top edge rather than to the centre.
3. **One source in the window.** Overlapping anomalies superpose their
   analytic signals non-linearly, so the fit window must isolate one body.
4. **No data gaps or levelling errors.** The Hilbert transform uses the whole
   profile; a flight-line mis-tie appears as a spurious $\mathrm{AS}$ spike.
5. **The vertical derivative is derived, not measured.** Any error in
   $\partial T/\partial x$ — noise, smoothing, gridding — propagates into
   $\partial T/\partial z$ with equal weight.

## The honest summary

One estimator and three measurements. The analytic signal recovers the position
($8.00\ \mathrm{km}$) and the depth ($4.160\ \mathrm{km}$) of a body whose anomaly
is skewed by $40°$, where the anomaly's own half-width returns
$4.594\ \mathrm{km}$ against a true depth of $4.0\ \mathrm{km}$ — a $+14.8\%$
bias against the analytic signal's $+4.0\%$. The
method's power is its invariance; its price is that it needs a
**de-trended profile** (an $8\ \mathrm{nT\,km^{-1}}$ trend otherwise costs
$+12.9\%$), a derivative computed on smoothed data ($+4.9\%$), and a profile
several source depths long. The Monte Carlo uncertainty of $\pm 0.017\ \mathrm{km}$
is 25 times smaller than the residual bias, so the honest report is a depth with a
systematic error bar, not a precise number.

## Python demonstration

[`code/mag_anomaly_modelling_demo.py`](./code/mag_anomaly_modelling_demo.py) prints every number quoted above, writes no files,
uses no network and exits 0:

```bash
cd 25-projects-capstone/03-advanced-projects/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python mag_anomaly_modelling_demo.py
```

It is seeded with `np.random.default_rng(20261014)` and runs in under a second.
## Exercises

Graded problems and worked solutions are in
[`exercises/01-mag-anomaly-modelling-exercises.md`](./exercises/01-mag-anomaly-modelling-exercises.md)
and
[`exercises/01-mag-anomaly-modelling-solutions.md`](./exercises/01-mag-anomaly-modelling-solutions.md).
The ★★★ item asks you to design a joint depth-and-magnetisation estimate, not to
fit one more Lorentzian.

## Mastery checkpoint

Without notes:

1. Write the anomaly of a 2-D dipole line and identify which term carries the
   skew.
2. State the Hilbert relation between the horizontal and vertical derivatives and
   the condition under which it holds.
3. Show that $1/|\mathrm{AS}|$ is a parabola in $x$ and give the three formulas
   that recover $k$, $x_0$ and $z$.

## Common pitfalls

1. **Reading a depth from a skewed anomaly's half-width.** Remanence shifts the anomaly, so the half-width measures a mixture of depth and skew.
2. **Leaving a linear trend in before differentiating.** It enters the analytic signal as a constant offset and biases the depth; removal is a modelling choice that must be stated.
3. **Over-smoothing the derivative.** The filter width is a bias-variance trade and absorbs part of the anomaly's own curvature.
4. **Computing the analytic signal on a profile shorter than a few source depths.** The truncated long-wavelength tail is absorbed as if it were a trend.
5. **Quoting a depth uncertainty from noise alone.** The smoothing and trend-removal biases are systematic and larger.

## Where this is used

The analytic signal is the standard automatic depth-estimation step in
aeromagnetic processing, and it is the input to the magnetic inversion discussed
in [08-03-06](../../08-geomagnetism-electromagnetism/03-magnetic-anomalies-and-modelling/06-magnetic-inversion.md).
Its 3-D generalisation (the analytic signal of the full field magnitude) is used
for map-based estimates, and its failure for compact bodies is the reason
Euler deconvolution and Werner deconvolution are used alongside it. In
exploration practice the depth from this method is the first-pass constraint on
the top of a magnetic source, and the systematic bias measured here is the
tolerance attached to it.

## Related lessons

- [08-03-01 Magnetic Anomaly Physics and Remanent vs Induced Magnetisation](../../08-geomagnetism-electromagnetism/03-magnetic-anomalies-and-modelling/01-magnetic-anomaly-basics.md) —
  the anomaly itself and its units.
- [08-01-07 Rock Magnetism: Remanence, Susceptibility and Magnetic Mineralogy](../../08-geomagnetism-electromagnetism/01-earth-magnetic-field/07-rock-magnetism.md) —
  where the skew comes from physically.
- [08-03-05 Depth Estimation: Werner, Euler, Peters and Spectral Methods](../../08-geomagnetism-electromagnetism/03-magnetic-anomalies-and-modelling/05-magnetic-depth-estimation.md) —
  the alternative and complementary depth estimators, and why several are always
  run together.

## Self-assessment checklist

- [ ] I can write the anomaly of a 2-D dipole line and identify the skew term.
- [ ] I can derive and verify the Hilbert relation for a potential field.
- [ ] I can show that the analytic signal of a line source is a Lorentzian.
- [ ] I can invert $1/|\mathrm{AS}|$ linearly for position, depth and amplitude.
- [ ] I can measure the depth bias from an unremoved trend.

