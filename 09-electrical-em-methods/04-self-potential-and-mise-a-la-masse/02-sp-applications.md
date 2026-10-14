---
id: 09-04-02
title: "SP for Seepage, Dams, Landfills and Mineralisation"
level: advanced
prereqs: ["09-04-01", "09-01-02", "09-03-03", "01-13-09"]
tags: [electrical-methods, self-potential, seepage, monitoring, detection-limits, levelling, depth-estimation]
---

# SP for Seepage, Dams, Landfills and Mineralisation

## Learning objectives

By the end of this lesson you will be able to:

1. **Read** an SP profile as the surface expression of a current distribution,
   and **match** it against the four source geometries used here — a compact
   dipole, a vertical line, a shallow sheet and a point electrode.
2. **Derive** the matched-filter detection statistic for an SP anomaly and
   **compute** the source moment needed for a stated signal-to-noise ratio.
3. **Derive** why the required moment grows as $\text{depth}^{3/2}$ and check the
   exponent against a measured fit.
4. **Estimate** the depth of a source from a noisy profile, and **report** the
   Monte Carlo spread rather than the median alone.
5. **Decide**, from measured residuals, whether a profile can discriminate source
   *type*, and state what it cannot discriminate.
6. **Quantify** the bias produced by an unremoved drift, and explain why a
   symmetric trend is nearly harmless while an asymmetric one is not.
7. **Specify** an SP survey — station spacing, repeat measurements, levelling —
   that supports the interpretation being claimed.

## Prerequisites

- [09-04-01 Sources of Self-Potential: Electrokinetic, Electrochemical](01-self-potential-sources.md)
  — the mechanisms, the coupling coefficient and the width rules.
- [09-01-02 Archie's Law, Porosity and Saturation](../01-electrical-properties-of-earth/02-archies-law.md)
  — why a seepage path or a leachate plume changes the conductivity as well as
  the SP source.
- [09-03-03 IP Acquisition, Chargeability and Phase Units](../03-induced-polarisation/03-ip-acquisition.md)
  — electrode behaviour and the noise environment of a small-potential
  measurement.
- [01-13-09 Error and Uncertainty Propagation](../../01-mathematics/13-probability-and-statistics-foundations/09-error-propagation.md)
  — how a per-station noise becomes an uncertainty on a fitted depth.

**All models and data in this module are SYNTHETIC.** Depths, source strengths,
station spacing, noise levels and drift sizes are chosen teaching values. Nothing
here is a model of a particular dam, landfill, mine or aquifer, and no field
value is quoted.

---

## 1. Intuition: an SP survey is a pattern, and its limits are geometric

An SP survey produces one number per station: a voltage between a roving electrode
and a fixed (or previously occupied) reference. The interpretation is a *pattern*,
and three facts about patterns set every practical limit.

- **Amplitude falls rapidly with distance from the source.** For a compact
  source the surface field falls as $1/h^{2}$ in the source depth, so the anomaly
  from a deep source is small and easily buried in noise.
- **Width grows with distance.** The full width at half maximum of the anomaly is
  proportional to the depth, with a constant that depends on the source geometry
  ($3.464\,h$ for a point electrode, $1.533\,h$ for a compact dipole;
  lesson 01 §3.5). Depth information therefore lives in the *shape*, and it is
  the only depth information there is.
- **A trend can be indistinguishable from a source.** A long-wavelength drift
  over the profile has the same shape as a deep, broad source. Whether that
  matters depends on the symmetry of the trend relative to the anomaly, and this
  lesson measures it.

The practical consequence is a survey design that is dominated by two questions:
*how many stations across the anomaly* (which controls the depth uncertainty) and
*how well can the trend be removed* (which controls the systematic error). Neither
is answered by a bigger instrument.

## 2. Precise definitions

### 2.1 The measurement

An SP reading at station $i$ is
$V_i = V_{\text{true}}(x_i) - V_{\text{ref}} + e_i$, with $e_i$ the
per-station error (electrode noise, contact potentials, reading error) and
$V_{\text{ref}}$ a reference potential that may itself drift with time. Levelling
is the operation of removing a smooth function of position (and sometimes of
time) from $\{V_i\}$; **the levelling function is part of the model and must be
reported**.

### 2.2 Anomaly metrics

| Metric | Definition | What it constrains |
|---|---|---|
| amplitude | maximum departure from the levelled background | source moment $\times$ $1/h^{2}$ |
| FWHM | full width at half maximum of a single lobe | depth, given a geometry |
| peak-to-trough separation | for bipolar anomalies | depth and source length |
| sign pattern | single lobe, bipolar, or reversed | mechanism and geometry |

### 2.3 Detection

With the anomaly $v(x_i)$ as a *template* and white noise of rms $\sigma_n$ per
station, the matched-filter signal-to-noise ratio is

$$\mathrm{SNR} = \frac{\left\langle \mathbf{v}, \mathbf{b}\right\rangle}
{\sigma_n \lVert \mathbf{b}\rVert}, \qquad
\mathbf{b} = \frac{\mathbf{v}}{\text{moment}},$$

where $\mathbf{b}$ is the unit-moment template. Detection at $\mathrm{SNR} = 3$
is the threshold used throughout this lesson.

### 2.4 The source models

Four synthetic models are compared: a compact vertical dipole (a polarised body
with two ends), a vertical line of current balanced by a sink below (a seepage
path or a long body), a shallow horizontal sheet balanced by a sink a few metres
below (a diffuse source such as a landfill base), and a point electrode (a
strongly polarised compact body). All are computed by the half-space image method
of lesson 01 §3.4.

## 3. Derivations

### 3.1 The measured profiles

For $I = 0.100$ A in a host of $\sigma = 0.010$ S/m over $41$ stations spanning
$400$ m, the demonstration prints:

| source model | peak (mV) | value at the profile edge (mV) | FWHM (m) | shape |
|---|---|---|---|---|
| vertical dipole, $d = 40$ m, $L = 20$ m | 21.221 | 0.150 | 40.0 | single-signed |
| vertical line, $z = 20$–$60$ m | 16.311 | 0.179 | 60.0 | single-signed |
| horizontal sheet, $z = 10$ m, half-length $60$ m | 10.286 | 0.015 | 120.0 | single-signed |

All three are single-signed positive lobes, and their widths increase as the
source becomes deeper or more distributed. **A wide, weak anomaly is therefore
the signature of a shallow broad source; a narrow, strong one of a compact
deeper source** — and the pair (width, amplitude) is exactly the pair that
Section 3.4 shows to be non-unique in the strongest sense.

### 3.2 Detection: how strong a source must be

For a compact vertical dipole of length $4$ m, with $\sigma_n = 1\ \mu$V per
station, the moment $IL$ that reaches $\mathrm{SNR} = 3$ is:

| depth (m) | $IL$ for SNR = 3 (A m) | corresponding peak anomaly ($\mu$V) |
|---|---|---|
| 10 | $1.622\times10^{-5}$ | 2.689 |
| 20 | $4.882\times10^{-5}$ | 1.962 |
| 40 | $1.387\times10^{-4}$ | 1.384 |
| 80 | $3.933\times10^{-4}$ | 0.979 |
| 160 | $1.131\times10^{-3}$ | 0.704 |
| 320 | $3.540\times10^{-3}$ | 0.550 |

The fitted power law is

$$IL_{\text{required}} \propto \text{depth}^{1.542},$$

and the exponent is not a coincidence. Write the dipole surface field as
$v(x) \approx \frac{\rho IL}{2\pi}\cdot\frac{h}{\left(x^{2}+h^{2}\right)^{3/2}}$
so that $\lVert\mathbf{v}\rVert^{2} \propto (IL)^{2}\displaystyle\int
\frac{h^{2}\,\mathrm{d}x}{\left(x^{2}+h^{2}\right)^{3}} \propto
\frac{(IL)^{2}}{h^{3}}$ over a profile that extends well beyond $h$ on both
sides. Hence

$$\lVert\mathbf{v}\rVert \propto \frac{IL}{h^{3/2}}
\;\Longrightarrow\;
IL_{\text{required}} \propto h^{3/2},$$

and the measured $1.542$ exceeds $1.5$ by $2.8\%$, the residual being the finite
$400$ m extent of the profile at the shallower depths. A factor $32$ in depth
therefore costs a factor $218$ in moment (measured), not $32$.

Two consequences follow for survey design. First, the depth range of an SP
survey is set by the *noise*, and a factor-two improvement in noise buys a factor
$2^{2/3} = 1.59$ in depth. Second, the peak anomaly needed shrinks with depth
(2.689 $\mu$V at 10 m against 0.550 $\mu$V at 320 m) because a broader template
collects more signal: **the anomaly can be smaller than the per-station noise and
still be detected**, which is what a matched filter is for and why station
spacing across the anomaly matters more than absolute precision.

### 3.3 Depth from a noisy profile

Fitting the depth on a $1$ m grid with the current solved linearly, and repeating
$120$ times per noise level, the demonstration measures:

| noise (% of peak) | median depth (m) | 16–84% spread (m) | bias (m) |
|---|---|---|---|
| 0.5 | 40.0 | 0.0 | $+0.0$ |
| 2.0 | 40.0 | 2.0 | $+0.0$ |
| 5.0 | 40.0 | 3.0 | $+0.0$ |
| 20.0 | 40.0 | 14.0 | $+0.0$ |

The estimator is essentially unbiased under the correct model family, and its
**spread grows with the noise** — from unresolved at $0.5\%$ noise to $14$ m
(35% of the depth) at $20\%$ noise. Under an incorrect family the bias reappears,
as Section 3.4 shows. The reportable number is the spread; the median alone
overstates what the profile supports.

### 3.4 Source type, source parameters, and what a profile can separate

Fitting four candidate shapes to one synthetic profile (truth: dipole, $40$ m,
$20$ m long, $2\%$ noise), each with its scale solved linearly:

| candidate | peak (mV) | rms residual (mV) | in units of the noise |
|---|---|---|---|
| dipole $d = 40$ m, $L = 20$ m (truth) | 21.273 | 0.443 | 1.04 |
| dipole $d = 44$ m, $L = 30$ m | 20.792 | 0.504 | 1.19 |
| vertical line, $z = 20$–$60$ m | 20.617 | 0.613 | 1.45 |
| horizontal sheet at $10$ m | 12.371 | 2.943 | 6.93 |

So a single profile at this noise and spacing **does** separate a deep compact
source from a shallow broad one (the sheet is rejected at $6.93$ noise units) but
**does not** distinguish a dipole from a short vertical line ($1.04$ versus
$1.45$) — they have the same surface shape over this aperture. And within the
dipole family, lesson 01 §3.6 measured the ridge of admitted
$(\text{depth},\ \text{length})$ pairs with a correlation of $+0.854$.

The three statements must be kept apart:

1. the *family* is constrained (a sheet is rejected);
2. the *parameters within the family* are not (a ridge is admitted);
3. the *depth* depends on which family is assumed at all (the factor $2.26$
   between the two width constants of lesson 01 Example 2).

### 3.5 Drift: which trends bias the answer

Adding trends of $1.70$ mV across the $400$ m profile to a $21.22$ mV anomaly and
refitting:

| trend added | recovered depth (m) | recovered current (A) |
|---|---|---|
| none | 40.0 | 0.1002 |
| linear ramp | 40.0 | 0.1002 |
| quadratic | 40.0 | 0.1004 |
| linear ramp over one half of the profile | 41.0 | 0.1048 |
| exponential decay from one end | 40.0 | 0.1008 |

The symmetric trends change nothing, and there is an exact reason: the symmetric
anomaly template $\mathbf{b}$ is **orthogonal** to any odd function of $x$, so
$\left\langle\mathbf{b}, \text{linear ramp}\right\rangle = 0$ and the linear
trend cannot bias a single-lobe symmetric fit. The quadratic trend has a small
projection on the template's own breadth, giving a $0.2\%$ change in amplitude.

The asymmetric trends do bias the answer: the one-sided ramp moves the depth by
$+1.0$ m and the current by $+4.6\%$, because the fit trades a long-wavelength
ramp against a deeper, stronger source. The exponential trend, whose curvature
falls mostly in the wings where the template is small, moves the current by only
$+0.6\%$. **The size of the bias depends on where the trend's curvature falls
relative to the anomaly**, which is why the check — refit with and without the
trend removed and compare — is mandatory rather than optional, and why the
levelling function must be reported.

## 4. Physical interpretation

- **Width is depth; amplitude is moment over depth squared.** Both are needed,
  and both are affected by the unknown conductivity, which enters the amplitude
  directly ($V \propto \rho I$). Without an independent resistivity model, an
  amplitude anomaly is not interpretable in absolute terms.
- **Detection is a matched-filter problem, not a threshold problem.** The
  $\text{depth}^{3/2}$ law is the whole depth penalty; it is beaten by narrower
  station spacing and by more stations across the anomaly, which raise the
  template norm.
- **Source type is separable; source parameters within a type are not.** This is
  the practical content of Section 3.4 and it is the honest form of the claim
  "SP locates seepage": it constrains the geometry class and the footprint, not
  a unique body.
- **Trends matter in proportion to their asymmetry.** A linear regional trend is
  a non-issue for a symmetric anomaly; a step or a one-sided ramp is a real
  error, and its detection is the refit comparison of Section 3.5.

## 5. Assumptions and regime of validity

1. **A single dominant source mechanism** per anomaly. Mixed electrokinetic and
   electrochemical sources add, and separating them requires the additional
   evidence listed in lesson 01 §4.
2. **A homogeneous host** in every forward model. In reality a conductivity
   boundary refracts the current, distorts the anomaly and can produce a
   long-wavelength pattern that mimics drift. Every interpretation of Section 3
   is therefore *conditional on the conductivity model*.
3. **White, stationary, independent per-station noise** for the matched filter
   and the Monte Carlo. Correlated noise (a drifting reference) invalidates both;
   that is exactly why the drift case is treated separately in Section 3.5.
4. **The template geometry is known** in Section 3.3. When it is not, the
   admitted range is wider, as lesson 01 §3.6 measured.
5. **The profile extends beyond the anomaly** so that the template norm
   converges; a profile truncated inside the anomaly inflates the fitted depth.
6. **No time-lapse effects within a survey.** Rainfall infiltration and tidal
   pumping change SP during acquisition; repeated stations are the only check.
7. **Two-dimensionality.** A profile is treated as a section through a
   two-dimensional source, which is appropriate for a line-like body and wrong
   for a compact one; the sheet model of Section 3.1 exists to make that
   difference visible.

## 6. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| potential | $V$ | V (reported mV) | $\rho I/(2\pi r)$ |
| current | $I$ | A | |
| conductivity | $\sigma$ | S/m | |
| depth, length, spacing | $h$, $L$, $\Delta x$ | m | |
| noise | $\sigma_n$ | V per station | same unit as $V$ |
| template norm | $\lVert\mathbf{v}\rVert$ | V (with stations as a count) | sum of squares of volts, square-rooted |
| moment | $IL$ | A m | $I$ times a length |

Check the $\text{depth}^{3/2}$ law dimensionally: $v \propto \rho IL/h^{2}$ at the
peak, so $\lVert v\rVert^{2} \propto (\rho IL)^{2}/h^{3}$ times a length
integrated over the profile — the extra length cancels against the $h$ in the
integration measure, leaving $\lVert v\rVert \propto IL/h^{3/2}$ ✓. If a
computation gives a different exponent, the template has probably been
truncated or the distance measure has been mixed up with a station count.

## 7. Worked examples

### Example 1 — a depth from a measured width, with its model dependence

A synthetic profile has $\mathrm{FWHM} = 120.0$ m (the sheet model of
Section 3.1). Interpret it first as a point electrode:

$$h = \frac{120.0}{3.4641} = 34.6\ \mathrm{m},$$

and then as a compact dipole:

$$h = \frac{120.0}{1.5328} = 78.3\ \mathrm{m}.$$

A factor $2.26$ apart, from the same measurement. The sheet model used here has
its source at $10$ m depth but is *distributed*, which is why its width does not
fit either constant: the demonstration's sheet gives FWHM $120.0$ m for a
$120$ m long source at $10$ m depth. **A distributed source has a width set by
its own extent, not by its depth**, and no single-depth conversion applies. The
additional measurement that discriminates is station spacing fine enough to see
the flanks of the anomaly, plus an independent conductivity model.

### Example 2 — the moment a target of a stated depth requires

A $40$ m deep compact dipole must be detected at $\mathrm{SNR} = 3$ with
$\sigma_n = 1\ \mu$V per station. From the measured table the required moment is
$IL = 1.387\times10^{-4}$ A m. For a $4$ m long body that is
$I = 3.47\times10^{-5}$ A of equivalent source current — a physically tiny
current, which is the point: SP detects current, not voltage, and the currents
are microamps.

Check the peak anomaly: with that moment the model gives
$1.384\ \mu$V at the central station, i.e. slightly *above* the per-station
noise. The detection works because the matched filter sums the anomaly across
$41$ stations, adding signal coherently and noise incoherently.

### Example 3 — the cost of a drift

Suppose a $4.6\%$ error in the recovered source current is unacceptable, and the
survey uses a levelling function that can only remove a straight line. From
Section 3.5 the one-sided ramp gives $+4.6\%$ of bias; a straight-line removal
would not touch it (the ramp is not linear over the whole profile in that case).
The remedy is either a longer profile that contains both ends of the ramp, or
repeated base-station readings that document the drift in time. Quantitatively:
the drift is $1.70$ mV across $400$ m, i.e. $0.0042$ mV/m, and the anomaly is
$21.22$ mV wide by $40$ m — so the drift is $3.4\%$ of the anomaly amplitude but
presents itself as a *long-wavelength* shape that the fit can trade against
depth. That trade is the bias.

## 8. Python demonstration

`code/sp_applications_demo.py` prints every number in this lesson. It:

1. builds and compares three synthetic source geometries with their amplitudes
   and widths;
2. computes the matched-filter detection moment over a factor $32$ in depth,
   fits the power law (measured exponent $1.542$) and derives the $3/2$
   exponent;
3. runs a $120$-realisation Monte Carlo of the depth estimator at four noise
   levels and reports the median, the 16–84% spread and the bias;
4. fits four candidate source types to one noisy profile and reports the
   residuals in noise units;
5. refits the profile with five different trends added and reports the recovered
   depth and current for each.

Run it with the project virtual environment:

```bash
cd 09-electrical-em-methods/04-self-potential-and-mise-a-la-masse/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python sp_applications_demo.py
```

## 9. Exercises

Full sets with worked solutions are in
[`exercises/02-sp-applications-exercises.md`](./exercises/02-sp-applications-exercises.md)
and
[`exercises/02-sp-applications-solutions.md`](./exercises/02-sp-applications-solutions.md).

- **★** A profile has a single-signed lobe with FWHM $80$ m. Give the depth under
  the point-electrode and the compact-dipole assumptions.
- **★** Using the measured table, what moment is needed to detect a $160$ m deep
  compact dipole at SNR $= 3$ with $1\ \mu$V noise, and what peak anomaly does
  that produce?
- **★★** Derive $\lVert\mathbf{v}\rVert \propto IL/h^{3/2}$ for the dipole
  template and state the two assumptions used.
- **★★** A survey has $2\%$ noise and reports a depth of $40$ m without a spread.
  Using the Monte Carlo table, state what spread should have been quoted.
- **★★★** Design an SP survey to distinguish a $60$ m deep compact body from a
  $10$ m deep distributed sheet, both of which produce a $10$ mV, $120$ m wide
  anomaly: choose the station spacing, the profile length, the repeat policy and
  the levelling, and state the statistic that decides.

## 10. Common mistakes

1. **Quoting a depth without the source family.** The same FWHM gives depths a
   factor $2.26$ apart under two standard families.
2. **Treating an amplitude anomaly as a target strength.** The amplitude carries
   $\rho$, which is unknown; the width carries the geometry.
3. **Reporting a median without a spread.** At $20\%$ noise the 16–84% spread is
   $14$ m on a $40$ m source.
4. **Levelling with a function that can absorb the anomaly.** A one-sided ramp
   biases the recovery by $+4.6\%$ in current and $+1$ m in depth.
5. **Assuming white noise.** The matched-filter gain and the Monte Carlo spreads
   both assume it; a drifting reference is neither white nor independent.
6. **Ignoring conductivity structure.** A conductivity boundary refracts current
   and mimics a source; SP alone cannot separate them.
7. **Truncating the profile inside the anomaly.** The template norm then
   underestimates the signal and inflates the fitted depth.

## 11. Real-world applications

- **Dam and levee seepage.** An SP profile across an embankment is used to locate
  preferential seepage paths; the interpretation is the *line* geometry of
  Section 3.1, and the detection limit is the moment table of Section 3.2.
- **Landfill and waste-site characterisation.** A shallow distributed source,
  modelled here as a sheet, is the typical signature of leachate-related redox
  activity at a waste boundary.
- **Mineral exploration.** The classical compact anomaly over sulphide bodies is
  the dipole/electrode family of Section 3.1, and the confusion between a deep
  compact body and a shallow distributed one is the ambiguity of Section 3.4.
- **Monitoring.** Repeated surveys along fixed lines with permanent electrodes
  turn the amplitude into a time series; the detectability of a change is then
  set by the same $1/h^{3/2}$ law applied to the change, not to the absolute
  anomaly.

## 12. Further reading

- **Revil, A., & Jardani, A., *The Self-Potential Method: Theory and
  Applications in Environmental Geosciences* (Cambridge University Press).**
  Level: research monograph. The seepage and environmental applications, with
  the source models used here in their rigorous form.
- **Reynolds, J. M., *An Introduction to Applied and Environmental
  Geophysics* (2nd ed., Wiley-Blackwell).** Level: textbook. Field procedure,
  non-polarisable electrodes, and the practical problem of drift.
- **Telford, W. M., Geldart, L. P., & Sheriff, R. E., *Applied Geophysics*
  (2nd ed., Cambridge University Press).** Level: textbook. Anomaly shapes for
  the classical source geometries.
- **Fitterman, D. V., & Corwin, R. F., "Inversion of self-potential data from
  the Cerro Prieto geothermal field, Mexico", *Geophysics* 47 (1982).**
  Level: research. An early quantitative inversion of SP profiles; useful as a
  demonstration that the inverse problem was understood as non-unique from the
  start.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text. **No number in this lesson is
> quoted from any of them**: every figure is printed by
> [`code/sp_applications_demo.py`](./code/sp_applications_demo.py), apart from
> the exact constants $3.4641 = 2\sqrt{3}$ and $1.5328 = 2\sqrt{2^{2/3}-1}$
> derived in lesson 01.

## 13. Related lessons

- [01 Sources of Self-Potential: Electrokinetic, Electrochemical](01-self-potential-sources.md) —
  the mechanisms and the width rules used throughout.
- [03 Mise-à-la-Masse and Induced Polarisation Mapping](03-mise-a-la-masse.md) —
  the active-current counterpart of the passive measurement.
- [09-02-05 ERT Acquisition and Design](../02-dc-resistivity/05-ert-tomography.md) —
  the conductivity model that SP interpretation is conditional on.
- [09-03-04 IP for Sulphides, Clays, Contaminants and Permafrost](../03-induced-polarisation/04-ip-applications.md) —
  the polarisation signature that distinguishes a clay-rich from a saline
  conductor, a distinction SP cannot make.
- [09-07-01 EM Noise, Coupling and Cultural Effects](../07-em-data-processing-and-qc/01-em-noise-and-coupling.md) —
  the noise environment shared by every electrical method.

## 14. Self-assessment checklist

- [ ] I can match a measured profile width to a source geometry class.
- [ ] I can compute a detection moment from a template and a noise level.
- [ ] I can derive the $3/2$ exponent of the detection law.
- [ ] I can report a depth with the spread its noise level implies.
- [ ] I can say which source types are separable from one profile and which are
      not, quoting measured residuals.
- [ ] I can explain why a linear trend is harmless and a one-sided ramp is not.
- [ ] I can write an SP acquisition specification with its levelling policy.
