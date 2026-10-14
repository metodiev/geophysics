---
id: 05-07-04
title: "Ground Truthing: Boreholes, Outcrop and Drill Core"
level: advanced
prereqs: ["05-07-02", "05-07-03", "05-08-01"]
tags: [ground-truth, borehole, core, validation, prediction-test, scale]
---

# Ground Truthing: Boreholes, Outcrop and Drill Core

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** ground truthing as a *prediction test* on data the model was not
   fitted to, and distinguish it from calibrating a model to the well.
2. **Derive** the prediction residual statistic and the level at which a model
   should be judged successful.
3. **Quantify** the scale gap between a borehole (decimetres to metres) and an
   anomaly footprint (hundreds of metres to kilometres) and explain why it limits
   what a single well can prove.
4. **Derive** the depth error introduced by a wrong average velocity when tying a
   well to a seismic section or a potential-field depth estimate.
5. **Explain** what core, cuttings, wireline logs and downhole measurements each
   measure, and what they do *not*.
6. **State** honestly when a borehole has falsified a model, when it has merely
   failed to confirm one, and when the two are indistinguishable at the available
   precision.

## Prerequisites

- [05-07-02 Quantitative Interpretation and Depth Estimation](./02-quantitative-interpretation.md)
  — the fitted model, its covariance, and the fact that its residual is not a
  validation.
- [05-07-03 Integrating Multiple Methods and Constraints](./03-multi-method-integration.md)
  — the prediction test in its abstract form; this lesson carries it out.
- [05-08-01 The Borehole Environment and Invasion Profiles](../08-geophysical-logging/01-borehole-environment.md)
  — what a log actually measures, and why the borehole is not the formation.

## 1. Intuition: a model is a prediction, and a well is a test

There is a difference between *fitting* a model to a well log and *testing* a
model with a well. If you include the borehole in the inversion — for example by
using its measured density as a constraint — the resulting model will agree with
the borehole by construction, and the agreement is worth nothing. The test only
has content when the model is fixed *before* the well data are seen, and then
used to predict something the well measures.

That is the entire content of ground truthing, and it is why a drilling programme
must be designed as an experiment. The questions to answer before drilling are:

1. **What will the model predict?** A depth interval, a density, a seismic
   two-way time, a temperature.
2. **At what precision must the prediction be tested?** The well's own
   measurement precision and the scale mismatch of Section 3.3.
3. **What result would falsify the model?** If no result would, the well is not a
   test.

There is also a scale problem that is frequently glossed over. A borehole is a
line in a volume. The property it measures is a property of a rock volume a few
decimetres across, at one horizontal location. A geophysical anomaly integrates
the property over a footprint of hundreds of metres and a depth range of
hundreds of metres. **Agreement between them is a statement about a spatial
average, not about a point**, and disagreement is often the more informative
outcome because it means the model's spatial distribution is wrong even if its
average is right.

## 2. Precise definitions

### 2.1 Ground truth

**Ground truth** is an independent measurement of the quantity the model claims
to predict. Independence requires (i) that the measurement was not used in
constructing the model, and (ii) that its errors are not correlated with the
model's. A density log run in the well that provided the inversion's starting
model fails requirement (i).

### 2.2 Core, cuttings, and log

- **Core** is a cylinder of rock, typically a few centimetres to ~10 cm in
  diameter, recovered to surface. It is the only sample of the rock *in situ* and
  it is damaged, wetted, depressurised and (in weak rocks) partially lost; a
  recovery figure below 100 per cent biases any average computed from it.
- **Cuttings** are chips returned by the drilling fluid, depth-lagged by the
  circulation time and mixed over an interval. They are a lithological indicator,
  not a property measurement.
- **Wireline logs** measure formation properties *in situ* over a volume of
  investigation of order a few decimetres to a metre, with borehole effects
  (Section 4.2 of [05-08-01](../08-geophysical-logging/01-borehole-environment.md))
  and environmental corrections that must be applied.

Distinguishing these matters because a "core density" and a "log density" differ
systematically, and comparing a model to the wrong one produces a false
validation.

### 2.3 Prediction residual

If a model predicts $p$ with stated uncertainty $\sigma_p$ and the well measures
$d$ with uncertainty $\sigma_d$, the **standardised prediction residual** is

$$r = \frac{d - p}{\sqrt{\sigma_d^2 + \sigma_p^2}}. \tag{1}$$

The model passes the test at the $1-\alpha$ level if $|r| < z_{1-\alpha/2}$. For
a single well and $\alpha = 0.05$, that is $|r| < 1.96$. The uncertainty in the
denominator must include the model's uncertainty, or the test is unfair to the
model.

### 2.4 Depth reference and tie

A **tie** is the mapping between a geophysical depth (or two-way time) and the
borehole's measured depth. It requires a velocity or time–depth relationship, and
it is where most apparent disagreements originate.

## 3. Derivations

### 3.1 Why a good residual is not a validation

Let the true field be $\mathbf{d} = \mathcal{F}[\mathbf{m}_{\text{true}}] +
\boldsymbol{\epsilon}$. Any model $\hat{\mathbf{m}}$ in the feasible set gives

$$\|\mathbf{d} - \mathcal{F}[\hat{\mathbf{m}}]\|^2 \approx
\|\boldsymbol{\epsilon}\|^2,$$

which is the *same* for every feasible model. The demonstration of
[05-07-02 §4.1](./02-quantitative-interpretation.md) shows two models with
residuals 0.0202 and 0.0204 mGal and depths differing by 128 m; the surface
groundtruthing demonstration shows two cases with residuals 0.0184 and
0.0188 mGal whose downhole predictions differ by a factor of 37. **The residual
is a property of the noise, not of the model.** Only the prediction test of
equation (1) discriminates.

### 3.2 Depth error from a velocity error

If a depth is obtained from a two-way time $t$ and an average velocity $v$,
$z = vt/2$. With $v$ uncertain but $t$ measured,

$$\frac{\delta z}{z} = \frac{\delta v}{v}. \tag{2}$$

So a 5 per cent velocity error gives a 5 per cent depth error: **40 m at 800 m**,
which is often larger than the target's own thickness. This is why a synthetic
seismogram is built from the well and not the other way round: the tie is a
*calibration of the velocity model*, and any depth comparison made before the tie
is made is comparing two different depth scales.

### 3.3 The scale gap, quantified

Consider a compact body of radius $R = 120$ m at 300 m depth and a borehole that
intersects it over $2R = 240$ m of core. The gravity anomaly's half-width is
$0.766R$-scale-free in the body's *depth*, not its radius; for a compact body the
anomaly footprint (say, the width at 10 per cent of peak) is roughly
$4z = 1.2$ km. The core sample is 0.1 m across. The ratio of sampled linear
scales is about $10^{4}$.

Three consequences follow, and each is a limitation of ground truthing:

1. **A single well proves a point, and the model predicts a volume.** If the body
   is heterogeneous, the well may sample a barren zone inside a productive body,
   or a productive zone inside a barren body.
2. **A well that misses the target is still informative**, provided the model's
   prediction of the target location is written down first. A miss with a stated
   geometry is a measurement of the model's error; a miss without one is an
   anecdote.
3. **Agreement in the mean does not imply agreement in the distribution.** The
   demonstration's case A shows 783.6 kg m⁻³ implied against 800.0 kg m⁻³
   measured — 2 per cent — and case B, with the same surface fit quality, shows
   1268.6 against 800.0, i.e. 59 per cent.

### 3.4 The property-inversion step, and where the error enters

From a fitted compact body with mass $M$ and a borehole that gives a radius $R$,

$$\Delta\rho_{\text{implied}} = \frac{M}{\tfrac{4}{3}\pi R^3}. \tag{3}$$

Two error sources enter, and $R$ enters **cubed**:

$$\left|\frac{\delta(\Delta\rho)}{\Delta\rho}\right| =
\left|\frac{\delta M}{M}\right| + 3\left|\frac{\delta R}{R}\right|. \tag{4}$$

A 10 per cent error in the borehole-derived radius becomes a 30 per cent error in
density. In case B the mass itself is wrong (9.18 × 10⁹ kg recovered against
1.35 × 10¹⁰ kg present, because a deep body was absorbed into the single-body
fit), which is why the implied density is 59 per cent high even though the radius
is correct — see the demonstration in Section 7.

### 3.5 What "the well disagrees with the model" means

Work through the possibilities explicitly, because reporting the wrong one is a
common failure:

| Well result | Model result | Interpretation |
|---|---|---|
| Rock present, correct density | Body predicted there | Pass; the model is supported in that direction (not proved) |
| Barren rock | Body predicted there | The model's geometry, property, or both are wrong. Which one depends on the anomaly's remaining mass balance |
| Rock present | No body predicted | The model's null space was larger than assumed, or the anomaly was interpreted wrongly |
| Rock present, different density | Body predicted there | The prediction of *mass* may be right (the amplitude fitted) while the *property* is wrong — the classic smearing failure |
| Well did not reach the target | — | No test. Report "not tested", not "consistent" |

The fourth row is exactly the demonstration's case B, and it is the most common
real outcome.

## 4. Worked examples

### 4.1 A prediction test that passes, and one that fails

**Setup.** A compact ore body of radius 120 m, density contrast 800 kg m⁻³, centre
at 300 m. Surface gravity on a 17 × 17 grid with 0.02 mGal noise. The single-body
fit gives $M = 5.672\times10^{9}$ kg at $z = 308.8 \pm 10.9$ m, RMS 0.0184 mGal.

*Case A test.* The hole at $x = 10$ m is logged below the ore, from 500 to
1300 m. The model predicts the downhole gravity profile; the mismatch is
0.1167 mGal maximum and 0.0315 mGal RMS, i.e. **1.6 times the station noise**,
and the implied density is 783.6 kg m⁻³ against 800.0 measured, i.e. **an
$r$ of about 0.5** by equation (1) if the core's uncertainty is 30 kg m⁻³. Pass.

*Case B test.* Add a second, deeper body: radius 270 m, contrast 100 kg m⁻³,
centre 900 m. The surface fit now gives $M = 9.182\times10^{9}$ kg at
$z = 380.3 \pm 11.5$ m with RMS 0.0188 mGal — indistinguishable from case A.
The downhole mismatch is 3.6646 mGal maximum and **1.1655 mGal RMS, 58 times the
station noise**. The implied density is 1268.6 kg m⁻³ against 800.0 measured.
Fail, decisively.

*What was learned.* The surface data alone could not have told you which case you
were in. The borehole could, in one pass, at a depth range where nothing was
being "discovered".

### 4.2 Designing the well so that it is a test

**Problem.** You have a gravity anomaly with a feasible depth range of 250–400 m
and a mass of $(9 \pm 1)\times10^{9}$ kg. Design a borehole that will test the
model.

*Step 1 — choose a falsifiable prediction.* "Between 250 and 400 m the hole will
intersect rock of density at least 400 kg m⁻³ above the local host."

*Step 2 — compute the required precision.* Equation (4): the density is what the
mass and the intersection geometry imply, so the hole must give the radius to
better than 10 per cent if 30 per cent on density is acceptable.

*Step 3 — choose the location deliberately.** Place the hole at the predicted
centre; if it is off-centre by design, the predicted intersection length changes
and the test becomes ambiguous.

*Step 4 — state the falsification condition in advance.* "Barren rock over the
entire 250–400 m interval falsifies the model." That sentence must be in the
drilling proposal, not written afterwards.

### 4.3 The temperature-well analogue

The same logic applies to heat flow. A borehole temperature profile can test a
conductivity-and-gradient model of heat flow, but only if (i) the model is stated
before the log is run, (ii) the hole has equilibrated (see
[05-09-01 Measuring Terrestrial Heat Flow](../09-geothermal-and-heat-flow-methods/01-heat-flow-measurement.md)),
and (iii) the conductivity used in the model is measured on the same rock, not
borrowed from a nearby well. A heat-flow model "validated" with a non-equilibrated
temperature log has been validated against the drilling mud.

## 5. Assumptions

1. **The model was fixed before the well data were seen.** Otherwise the test is
   circular; document the order of operations.
2. **The well measurement's uncertainty is known and includes its own borehole
   effects** (invasion, mudcake, hole size — Section 5 of
   [05-08-01](../08-geophysical-logging/01-borehole-environment.md)).
3. **The depth reference is common.** Both depth scales must be tied, with the
   tie's uncertainty carried (Section 3.2).
4. **The well is in the right place.** A well that misses the target tests
   nothing about the target; it tests the *target location* prediction.
5. **The property measured is the property modelled.** A bulk-density log is not
   a grain density; a P-wave slowness is not a porosity.
6. **One well is not the field.** Lateral heterogeneity at scales below the
   anomaly footprint is invisible to both the survey and the well.

## 6. Units and dimensional analysis

- Equation (1) is dimensionless: $d$, $p$, $\sigma_d$, $\sigma_p$ must all be in
  the same unit. Converting one gravity value to mGal and leaving another in
  m s⁻² is a factor of $10^{5}$ error, and it silently makes every prediction
  "pass".
- Equation (3): kg/(kg m⁻³ × m³)... dimensionally
  $\mathrm{kg}/\mathrm{m^3} = \mathrm{kg\,m^{-3}}$ ✓. The $4\pi/3$ is exact and
  dimensionless.
- Equation (4): relative errors are dimensionless and the coefficients 1 and 3
  come from the linear and cubic dependence respectively.
- Downhole gravity is measured in mGal like surface gravity, but the downhole
  *gradient* (typically quoted in µGal m⁻¹ or mGal m⁻¹) is the more diagnostic
  quantity because it removes a datum offset. Mixing the two conventions is a
  common source of factor-of-10 errors.
- Depth: metres, with a stated datum. The difference between measured depth
  (along a deviated hole) and true vertical depth can exceed 10 per cent in a
  deviated well and must be stated.

## 7. Python demonstration

`code/groundtruth_demo.py` discretises the true spheres into point masses so the
downhole field is finite, inverts the surface data for a single compact body, and
runs the downhole prediction test in both cases. Predict each line before running.

```python
g_obs = gz_surface(xg, yg, masses) + rng.normal(0.0, sigma, xg.size)
popt, pcov = curve_fit(model_surface, (xg, yg), g_obs, p0=p0, maxfev=40000)
diff = (model_downhole(depths, *popt) - gz_downhole(depths, masses)) / MGAL
print(f"RMS |model - truth| = {np.sqrt(np.mean(diff ** 2)):.4f} mGal")
```

Measured output, abridged:

```
SYNTHETIC ore  : radius 120 m, contrast 800 kg/m^3, centre 300 m, mass 5.791e+09 kg
SYNTHETIC deep : radius 270 m, contrast 100 kg/m^3, centre 900 m, mass 8.245e+09 kg

CASE A (one body)
surface RMS residual     = 0.0184 mGal (0.9 x the station noise)
best single body         : m = 5.672e+09 kg, z0 =   308.8 +/- 10.9 m
  RMS |model - truth|    = 0.0315 mGal      ratio to station noise = 1.6
  density contrast implied by the model =     783.6 kg/m^3
  density contrast measured on core     =     800.0 kg/m^3   factor 0.98

CASE B (ore + deep body)
surface RMS residual     = 0.0188 mGal (0.9 x the station noise)
best single body         : m = 9.182e+09 kg, z0 =   380.3 +/- 11.5 m
  RMS |model - truth|    = 1.1655 mGal      ratio to station noise = 58.3
  density contrast implied by the model =    1268.6 kg/m^3
  density contrast measured on core     =     800.0 kg/m^3   factor 1.59
```

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| Both surface residuals are 0.018–0.019 mGal | The surface data cannot choose between the cases; residual is a noise property |
| Both recovered depths carry ±11 m statistical errors | The reported precision is an order of magnitude smaller than the actual error |
| Case A passes the downhole test at 1.6 × the noise | A prediction test is quantitative, not a yes/no gesture |
| Case B fails at 58 × the noise | A single well falsified a model that 289 stations could not |
| Implied density is 2 % wrong in A and 59 % wrong in B | Property inversion amplifies mass error through a cubed radius, §3.4 |

> **Breaking exercise.** Move the deep body from 900 m to 2000 m and re-run. Predict
> whether case B now passes the downhole test. Then explain, in terms of the
> sensitivity kernel, why the well's *depth range* determines which bodies it can
> detect.

## 8. Exercises

[`exercises/04-ground-truthing-exercises.md`](./exercises/04-ground-truthing-exercises.md)
and
[`exercises/04-ground-truthing-solutions.md`](./exercises/04-ground-truthing-solutions.md).

### ★ Foundational

**★1.** A model predicts a body at $300 \pm 40$ m; the well finds it at
$310 \pm 5$ m. Compute the standardised residual of equation (1) and state
whether the model passes at the 5 per cent level.

**★2.** A seismic average velocity is 5 per cent too high. A reflector is picked
at 2.0 s two-way time. Compute the depth error and state the sign.

**★3.** Explain in three sentences why using a well log as a constraint in the
inversion destroys its value as a test.

### ★★ Applied

**★★4.** Run `code/groundtruth_demo.py`. Report the implied density in both
cases and verify equation (4) numerically by perturbing the assumed radius by
±10 per cent.

**★★5.** Design a prediction test for the Section 4.2 scenario: state the
prediction, the required precision, the falsification condition, and the number
of wells needed to distinguish "wrong location" from "wrong property".

**★★6.** For the case-B model, compute the additional mass the deep body
contributes to the surface anomaly and show that it is below the 0.02 mGal noise
at 900 m depth. Then find the depth at which it would become detectable.

### ★★★ Research-oriented

**★★★7.** Replace the single-well test with a *tomographic* test: suppose three
holes are drilled in a triangle of 600 m side. Using the same forward model,
compute the smallest body each hole could detect, and show how the joint test
constrains the model better than any one hole. Report the reduction in the
feasible set and discuss whether it is worth the cost.

**★★★8.** The demonstration discretises each sphere into 257 point masses.
Investigate the sensitivity of the downhole prediction to that discretisation,
and report the number of points at which the RMS changes by less than 1 per cent.
Then state the discretisation error you would quote for the test.

## 9. Common mistakes

1. **Calibrating then validating with the same well.** Circular, and it is the
   most common form of false confirmation in exploration.
2. **Comparing a core density to a log density without correction.** They differ
   systematically; the log's volume of investigation is not the core's.
3. **Ignoring the depth tie.** A 5 per cent velocity error is 40 m at 800 m; most
   "discrepancies" are ties, not geology.
4. **Reporting a well that missed the target as "consistent with the model".**
   Not tested is not the same as confirmed.
5. **Treating one well as a field-wide calibration.** Lateral heterogeneity below
   the anomaly footprint is invisible to both.
6. **Using the model's own residual as evidence.** Section 3.1: the residual is
   the noise.
7. **Forgetting that a borehole samples a line.** The model predicts a volume; the
   ratio of scales is $10^{4}$, and the property it measures averages over
   decimetres.

## 10. Real-world applications

- **Mineral exploration drilling.** Every drilling programme is (or should be) a
  prediction test of the geophysical model; the value of the geophysics is
  measured by its hit rate against stated predictions
  ([04-06-02 Mineral Deposits](../../04-earth-science-geology/06-petroleum-and-mineral-systems/02-mineral-deposits.md)).
- **Hydrocarbon well ties.** Synthetic seismograms, check shots and VSPs are the
  standard ground-truthing chain for seismic depth conversion
  ([05-08-06 Vertical Seismic Profiling and Check Shots](../08-geophysical-logging/06-seismic-while-drilling.md)).
- **Geothermal wells.** Temperature logs, flow tests and core conductivity
  validate the heat-flow model and the MT/gravity structure
  ([05-09-03 Geothermal Exploration Geophysics](../09-geothermal-and-heat-flow-methods/03-geothermal-exploration.md)).
- **Groundwater and geotechnical boreholes.** Logs and cores test the ERT or
  seismic model of an aquifer or a hazard, and the scale gap is often the
  limiting factor.
- **Scientific drilling.** The classic case where the borehole is the experiment
  and the geophysics is the hypothesis generator; the same discipline applies at
  exploration scale.

## 11. Further reading

- **Parker, R. L. (1994). *Geophysical Inverse Theory*. Princeton University
  Press.** Chapter 1 and §5.04. Level: graduate. The formal account of why a
  residual is a property of the noise and of how to test a model against unused
  data.
- **Ellis, D. V. & Singer, J. M. (2007). *Well Logging for Earth Scientists*
  (2nd ed.). Springer.** Chapters 1–4. Level: intermediate to advanced. What the
  borehole measurements actually measure, and their environmental corrections.
- **Hearst, J. R., Nelson, P. H. & Paillet, F. L. (2000). *Well Logging for
  Physical Properties*. Wiley.** Level: advanced. Borehole gravimetry and
  downhole measurement design, relevant to §3.3.
- **Tarantola, A. (2005). *Inverse Problem Theory and Methods for Model Parameter
  Estimation*. SIAM.** Chapter 1. Level: graduate. Model testing, prediction and
  the role of independent data.
- **Box, G. E. P. (1976). Science and statistics. *Journal of the American
  Statistical Association*, 71(356), 791–799.** Level: intermediate. The source
  of "all models are wrong, but some are useful", and a short, bracing read on
  what validation can and cannot mean.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text.

## 12. Related lessons

- [05-07-03 Integrating Multiple Methods and Constraints](./03-multi-method-integration.md)
  — the same prediction test in the context of a joint feasible set.
- [05-07-05 Reporting Geophysical Results with Honest Uncertainty](./05-reporting-results.md)
  — how to report a failed test, which is more valuable than a passed one.
- [05-08-07 Log Interpretation, Petrophysics and Uncertainty](../08-geophysical-logging/07-log-interpretation.md)
  — turning logs into properties, with the uncertainty that a prediction test
  needs in its denominator.
- [05-09-01 Measuring Terrestrial Heat Flow](../09-geothermal-and-heat-flow-methods/01-heat-flow-measurement.md)
  — the temperature-log case of §4.3, where equilibration is the ground-truthing
  problem.
- [18-06-06 Decision-Making Under Uncertainty and Value of Information](../../18-inverse-problems/06-uncertainty-quantification/06-decision-under-uncertainty.md)
  — what a well is worth before you drill it.

## Self-assessment checklist

- [ ] I can state the two independence conditions for ground truth and check them
      for a given dataset. (§2.1)
- [ ] I can compute a standardised prediction residual with both measurement and
      model uncertainty in the denominator. (§2.3, §4.1)
- [ ] I can explain why a good residual is not a validation. (§3.1)
- [ ] I can compute the depth error from a velocity error and state its sign.
      (§3.2)
- [ ] I can quantify the scale gap between a borehole and an anomaly footprint.
      (§3.3)
- [ ] I can propagate a radius error into a density error using the cubed
      dependence. (§3.4)
- [ ] I can list the six interpretations of "the well disagrees with the model"
      and choose the right one. (§3.5)
- [ ] I can run the demonstration and explain why case B fails while its residual
      looks identical to case A's. (§7)
