---
id: 21-06-07
title: "ML for Climate Downscaling and Emulation"
level: research
prereqs: ["21-06-01", "21-04-02", "16-05-04"]
estimated_minutes: 60
tags: [machine-learning, climate, downscaling, emulation, teaching]
---

# ML for Climate Downscaling and Emulation

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** statistical downscaling and emulation, and state what each one
   takes as input and asserts about the relationship it learns.
2. **Construct** a lapse-rate downscaling model as a linear regression on coarse
   temperature and elevation anomaly, and **state** the physics the coefficients
   carry.
3. **Design** four evaluation blocks — interpolation, later period, other region,
   both shifts — and **explain** what each one tests.
4. **Measure** the dominance of a spatial transfer failure over a temporal one and
   **explain** the mechanism in terms of a mis-specified response rather than a
   bias.
5. **Diagnose** an over-parameterised emulator from its in-sample and
   out-of-sample errors and **predict** which split will expose it.
6. **Distinguish** a distributional difference (a warmer period) from a structural
   difference (a different regime), and **state** why only the second breaks a
   correctly specified model.
7. **Specify** the report of a downscaling or emulation study: the input product,
   the training region and period, the transfer tested, the elevation dataset, and
   the metric's units.

Every field, temperature and error below is **SYNTHETIC**, produced by
[`code/climate_ml_demo.py`](./code/climate_ml_demo.py). No reanalysis product,
climate model output or station record is read or quoted.

## Prerequisites

- [21-06-01 ML for Seismic Detection, Picking and Classification](./01-seismic-ml.md) —
  the metric and prior discipline.
- [21-04-02 Bias-Variance Trade-Off, Underfitting and Overfitting](../../21-statistics-bayesian-ml/04-machine-learning-fundamentals/02-bias-variance.md) —
  the overfitting mechanism that the quadratic emulator exhibits here.
- [16-05-04 Downscaling: Statistical and Dynamical](../../16-atmosphere-climate/05-climate-models/04-downscaling.md) —
  the climate-science framing and the dynamical alternative.
- [21-04-03 Cross-Validation, Metrics and the Danger of Leakage](../../21-statistics-bayesian-ml/04-machine-learning-fundamentals/03-model-assessment.md) —
  the split vocabulary applied to space and time.

## 1. Intuition: two questions, one model

Downscaling and emulation are often the same code answering different questions.

- **Downscaling** asks: given a coarse field, what does the fine field look like
  *for the same situation*? The training and test data come from the same climate;
  the model learns a spatial relationship (elevation, land use, coastal
  gradients).
- **Emulation** asks: given a change in forcing, what is the response? The test
  situation is *outside* the training distribution by construction, because the
  point of an emulator is to predict a climate that has not happened.

Both are fitted by minimising error on the available period, and both are
evaluated by hold-out. The difference is which hold-out matters, and a study can
pass every validation it runs while failing the question it was asked. The
demonstration makes that concrete: an emulator that looks excellent under a
temporal split can lose a factor of three under a spatial transfer.

## 2. The synthetic problem

| Property | Value |
|---|---|
| coarse grid | 6 × 6 cells |
| fine grid | 18 × 18 cells (3 × 3 per coarse cell) |
| time | 200 monthly means |
| coarse temperature | $12.0 - 0.6\,\text{lat} + 3.0\sin(2\pi t/12) + 0.03t + \mathrm{AR}(1)$ [K] |
| elevation | 0–927 m, deterministic, fine-scale relief included |
| lapse rate | 6.5 K/km west of $x = 0.5$, 3.0 K/km east of it |
| fine truth | coarse value − lapse$(x)\times$ elevation anomaly $+ 0.8\tanh((T_c-15\ \mathrm{K})/4\ \mathrm{K}) + 0.15$ K noise |
| mean coarse temperature | 13.88 K (months 1–150), 17.20 K (months 151–200) |

The two halves of the domain differ in the **elevation response** — 6.5 K/km
versus 3.0 K/km — which is the structural difference; the second half of the
record is simply warmer by 3.32 K, which is the distributional difference. The
model is fitted on the western half and the first 150 months only (24 300
fine-cell-months), and the two emulators are:

$$\hat y = \beta_0 + \beta_1 T_c + \beta_2 \Delta z \quad\text{(linear)},$$

$$\hat y = \beta_0 + \beta_1 T_c + \beta_2 \Delta z + \beta_3 T_c^2
+ \beta_4 T_c\Delta z \quad\text{(quadratic)},$$

with fitted standardised-free coefficients
$(\beta_0,\beta_1,\beta_2) = (-2.21876,\ +1.14830,\ -0.00647)$ for the linear
model: the elevation coefficient is $-6.47\times10^{-3}$ K/m, i.e. **6.47 K/km**,
which is the western lapse rate recovered to within 0.5%. That is the check that
the model has learned physics rather than a correlation.

## 3. Four evaluation blocks

| Block | Cells and months | What it tests |
|---|---|---|
| in-sample | west, months 1–150 | nothing about generalisation |
| later period | west, months 151–200 | distributional shift (warmer) |
| other region | east, months 1–150 | structural shift (different lapse regime) |
| both shifts | east, months 151–200 | the deployment case for a regional application |

RMSE in K, with the mean error in parentheses:

| method | in-sample | later period | other region | both shifts |
|---|---|---|---|---|
| bilinear interpolation | 1.169 (+0.160) | 1.186 (−0.296) | 0.754 (+0.158) | 0.781 (−0.296) |
| linear lapse-rate emulator | 0.166 (−0.000) | 0.193 (+0.036) | 0.558 (−0.001) | 0.564 (+0.037) |
| quadratic emulator | 0.160 (−0.000) | 0.277 (+0.096) | 0.556 (−0.001) | 0.597 (+0.097) |

Three results.

1. **The temporal transfer is nearly free.** The linear emulator's error grows
   from 0.166 K to 0.193 K when the climate warms by 3.32 K. A correctly specified
   response extrapolates through a distributional shift.
2. **The spatial transfer costs a factor of 3.2.** On the eastern half the same
   model's RMSE is 0.558 K, and the error is not a constant bias — the mean error
   is $-0.001$ K. It is the mis-specified elevation response: the western
   6.5 K/km is imposed where the truth is 3.0 K/km, so the error is proportional
   to the elevation anomaly and averages to zero over the domain while reaching
   about 1 K at the extremes.
3. **Interpolation is not a substitute for a response model.** Bilinear
   interpolation has no elevation term at all and never beats 0.75 K, but it is
   *better* in the east (0.754 K) than in the west (1.169 K) — precisely because
   the east's true lapse rate is weaker, so ignoring elevation costs less there.
   A method with no physics can look relatively better where the physics matters
   less.

## 4. Over-parameterisation shows up under the *easier* extrapolation

The quadratic emulator beats the linear one in-sample (0.160 versus 0.166 K) by
fitting the seasonal curvature of the $\tanh$ term. It then performs **worse**
under the temporal transfer (0.277 versus 0.193 K) and slightly worse again in
the combined case (0.597 versus 0.564 K).

The mechanism is the one in
[21-04-02](../../21-statistics-bayesian-ml/04-machine-learning-fundamentals/02-bias-variance.md):
the extra coefficient reduces bias inside the training range and increases
variance outside it, and the variance term is what a warmer period exercises. Note
that the *spatial* transfer does not expose it — both models score 0.556 and
0.558 K there, because the lapse-rate misspecification dominates everything else.
A study that validates only by region, or only by period, sees one of the two
failures and not the other. Both blocks are needed, and the difference between
them is the reason.

## 5. Assumptions and regime of validity

1. **The relationship is stationary in time.** A downscaling model fitted on one
   period assumes the fine-to-coarse relation holds in another; the demonstration
   shows this is generous when the relation is correctly specified and the shift
   is purely distributional.
2. **The relationship is transferable in space.** This is the assumption that
   fails here, and it fails because a physical parameter (the lapse rate) differs.
   No amount of local validation detects it.
3. **Elevation is known on the fine grid.** The evidence is that the fine
   elevation dataset is authoritative; a different digital elevation model moves
   the answer at the metric's own scale.
4. **The coarse field is unbiased.** A reanalysis product carries its own
   biases; a learned correction fitted on a biased input inherits them.
5. **The fine-scale residual is white.** Real residuals are spatially correlated
   and heteroscedastic, which changes the meaning of the RMSE but not the ranking
   of methods.
6. **The metric is temperature, not impact.** RMSE in K says nothing about
   precipitation extremes, which are the quantities most applications care about.

## The honest summary

On a synthetic 6 × 6 to 18 × 18 downscaling problem with a known lapse rate, a
linear emulator recovers the western lapse rate as 6.47 K/km against a true
6.5 K/km, holds 0.193 K RMSE through a 3.32 K warming, and fails at 0.558 K — a
factor of 3.2 — when applied to a region whose lapse rate is 3.0 K/km. The error
is not a bias but a wrong response, invisible to local validation and to any
temporal split. A quadratic emulator that wins in-sample (0.160 versus 0.166 K)
loses under warming (0.277 versus 0.193 K). The transferable conclusions:
recover a physical coefficient where one is identifiable; test the transfer that
matches the deployment question; expect over-parameterisation to appear under the
easier extrapolation, not the harder one; and compare against interpolation,
which is a real baseline that can look better where the physics happens to matter
less.

## Python demonstration

[`code/climate_ml_demo.py`](./code/climate_ml_demo.py) prints every number quoted
above. It:

1. generates the coarse field, the fine elevation grid and the regime-dependent
   lapse rate, and prints the training and test temperature means;
2. fits the linear and quadratic emulators on the west half and months 1–150 and
   prints all coefficients, so the lapse-rate coefficient can be compared with
   the truth;
3. prints a 3 × 4 table of RMSE and bias over the four evaluation blocks;
4. prints the west-versus-east RMSE for every method and the structural warnings
   about transferability, under a `SYNTHETIC` provenance line.

Run it with the project virtual environment:

```bash
cd 21-statistics-bayesian-ml/06-ml-in-geophysics/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python climate_ml_demo.py
```

It runs in under 0.2 s (closed-form least squares only), reads no files, uses no
network and exits 0.

## Exercises

Graded problems and worked solutions are in
[`exercises/07-climate-ml-exercises.md`](./exercises/07-climate-ml-exercises.md)
and [`exercises/07-climate-ml-solutions.md`](./exercises/07-climate-ml-solutions.md).

## Mastery checkpoint

Without notes:

1. The fitted elevation coefficient is $-6.47\times10^{-3}$ K/m. State the true
   value in the training half and the percentage error, then state why that check
   is possible here and usually is not in a real study.
2. The linear emulator's RMSE goes from 0.166 K to 0.193 K under a 3.32 K warming,
   and to 0.558 K under a change of region. Explain in two sentences why one
   transfer is nearly free and the other is not.
3. The quadratic emulator wins in-sample and loses under warming. State the
   mechanism and the split that exposes it.
4. A colleague validates a downscaling model with five random cells held out.
   State what their number measures and the one transfer test you would add.

## Common pitfalls

1. **Validating by geography when the question is time.** The spatial transfer
   here hides the overfitting; the temporal one exposes it.
2. **Validating by time when the question is space.** The temporal transfer here
   gives 0.193 K to a model that costs 0.558 K where it will be used.
3. **Reporting an RMSE without the transfer it belongs to.** One model, four
   numbers spanning 0.166–0.597 K.
4. **Treating interpolation as the baseline.** It is a *different* model (no
   elevation response) and can beat a physics-aware model in a region where its
   missing term matters less.
5. **Assuming a warmer period tests extrapolation.** A distributional shift is
   benign for a correctly specified model; a change in a physical parameter is
   not.
6. **Quoting K without saying where.** RMSE in K over a domain with 900 m of
   relief is dominated by whether elevation was modelled at all.

## Where this is used

- **Impact assessment**, where downscaled fields drive hydrological, agricultural
  and energy models.
- **Emulation of expensive climate models**, where a surrogate is fitted to
  simulations and used to explore forcing scenarios
  ([16-05-06](../../16-atmosphere-climate/05-climate-models/06-emulation-and-surrogates.md)).
- **Bias correction of forecasts**, a downscaling problem with a temporal
  transfer question, where the demonstration's asymmetry is the central risk.
- **Geohazard projection**, where downscaled precipitation or temperature feeds
  slope-stability and permafrost models
  ([16-09-05](../../16-atmosphere-climate/09-geophysics-and-climate/05-climate-geohazards.md)).
- **Satellite product fusion**, where a coarse resolution sensor is calibrated
  against a fine one using exactly the elevation-and-regime regression used here.

## Related lessons

- [21-06-08 ML for Remote Sensing Classification](./08-remote-sensing-ml.md) —
  the classification counterpart, with the same transfer problem.
- [21-06-09 Pitfalls: Spurious Correlations, Non-Stationarity, Extrapolation](./09-ml-pitfalls-geophysics.md) —
  the general statement of the failures measured here.
- [21-04-02 Bias-Variance Trade-Off, Underfitting and Overfitting](../04-machine-learning-fundamentals/02-bias-variance.md) —
  the mechanism behind the quadratic emulator's loss.
- [21-04-06 Feature Engineering for Earth Data](../04-machine-learning-fundamentals/06-feature-engineering.md) —
  elevation anomalies, ratios and other transferable features.
- [16-05-04 Downscaling: Statistical and Dynamical](../../16-atmosphere-climate/05-climate-models/04-downscaling.md) —
  the climate-science context and the dynamical alternative.

## Self-assessment checklist

- [ ] I can state the difference between downscaling and emulation.
- [ ] I can write the lapse-rate model and interpret each coefficient.
- [ ] I can design four evaluation blocks and say what each tests.
- [ ] I can distinguish a distributional from a structural transfer.
- [ ] I can predict which transfer exposes over-parameterisation.
- [ ] I can list the five items a downscaling report must contain.
