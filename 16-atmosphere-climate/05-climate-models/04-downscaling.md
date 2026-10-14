---
id: 16-05-04
title: "Downscaling: Statistical and Dynamical"
level: research
prereqs: ["16-05-03", "16-02-05", "16-08-01"]
tags: [atmosphere, climate, climate-models, downscaling, statistical-downscaling, orography]
---

# Downscaling: Statistical and Dynamical

> All models and data in this module are **SYNTHETIC**. Every number below was
> printed by [`code/downscaling_demo.py`](code/downscaling_demo.py). The
> orography is a generated profile, the temperatures come from a chosen lapse
> rate, and no real model output or station record is used.

## Learning objectives

By the end of this lesson you will be able to:

1. **Distinguish** dynamical from statistical downscaling by what each one
   actually adds to the information already present in the coarse field.
2. **Derive** the lapse-rate correction
   $\Delta T = \Gamma\,(h_{\text{coarse}} - h_{\text{fine}})$ and **state** the
   units of each term.
3. **Compute** the variance removed by a deterministic fine-scale predictor and
   **interpret** the residual as the information no predictor carries.
4. **Measure** the error of four downscaling methods and **rank** them with
   stated metrics.
5. **Explain** why a statistically downscaled product implicitly assumes
   stationarity of the training relationship, and **demonstrate** the bias that
   appears when it fails.
6. **Distinguish** bias from scatter in a downscaled product, and **state** why
   bias is the more dangerous error.
7. **Design** a downscaling evaluation with a held-out period and a stated
   predictor set.

## Prerequisites

- [16-05-03 Model Evaluation, Skill and Benchmarking](03-model-evaluation.md) —
  the metrics used to compare the methods below.
- [16-02-05 Zero- and One-Dimensional Energy Balance Models](../02-radiation-and-energy-balance/05-energy-balance-models.md) —
  the energy balance that makes a lapse rate the first-order control on
  elevation-dependent temperature.
- [16-08-01 Surface, Radiosonde and Satellite Climate Records](../08-climate-observation-and-data/01-surface-and-satellite-records.md) —
  where the station data used to calibrate a statistical downscaling come from.

## 1. Intuition: what is being added?

A climate model run at 100 km does not resolve a valley. A user wants a valley
temperature. "Downscaling" is the family of methods that produce fine-scale
structure from coarse output. The first question to ask is not *which method*,
but *what information does the method add?*

There are exactly two honest answers:

- **A deterministic fine-scale predictor is used.** Orography is known at any
  resolution. Because surface temperature falls with height at roughly the
  environmental lapse rate, elevation is a predictor that is genuinely finer
  than the model. A lapse-rate correction therefore adds real information.
- **A statistical relationship is applied.** Regression maps coarse variables
  onto fine ones. This can remove a mean bias and can redistribute variance, but
  it cannot create structure that no predictor contains. Its skill is bounded by
  the correlation between the predictors and the target.

Dynamical downscaling (a limited-area model nested in the coarse field) is a
third route: it resolves processes the coarse model parameterised. It is more
expensive and its added value is a research question, not a guarantee, because
the boundary conditions still come from the coarse model.

## 2. Definitions

- **Statistical downscaling.** A calibrated mapping from large-scale predictors
  to local variables, fitted on a training period and applied to a target
  period.
- **Dynamical downscaling.** A higher-resolution model driven at its lateral
  boundaries by the coarse solution.
- **Delta-change (perturbation) method.** A simple statistical method that adds
  the coarse model's *change* to an observed fine baseline; it inherits the
  observed fine structure but assumes the change is spatially uniform.
- **Perfect-prognosis assumption.** The predictors are assumed to be available
  and skillfully predicted at the target time.
- **Stationarity assumption.** The fitted relationship is assumed to hold in the
  target period (often a different climate).
- **Added value.** Demonstrated improvement of the downscaled product over the
  raw coarse output, measured against independent fine-scale observations.

## 3. Derivation: the information argument

### 3.1 Setting

Let $T_f(i)$ be the fine-grid truth at fine point $i$, and let $B(i)$ denote the
coarse box containing $i$. The coarse model provides only the box mean

$$T_c(B) = \frac{1}{|B|}\sum_{i\in B} T_f(i)
\qquad\text{(exactly, if the model conserves the mean)}.$$

Define the predictor set $\mathbf{x}(i)$ available at fine scale — possibly
including $T_c(B(i))$, fine orography $h_f(i)$, and anything else.

### 3.2 What regression can and cannot do

The best possible predictor is the conditional mean
$\mathbb{E}[T_f \mid \mathbf{x}]$, which minimises mean squared error. Its
residual variance is

$$\mathrm{Var}\bigl[T_f - \mathbb{E}[T_f|\mathbf{x}]\bigr]
= \mathrm{Var}[T_f]\bigl(1-\rho^{2}\bigr),$$

where $\rho$ is the multiple correlation between the target and the predictors.
Two consequences:

- **No method can beat $\rho$.** If the only predictor is the box mean
  $T_c(B(i))$, then within a box that predictor is *constant*, so
  $\rho^{2}$ is exactly the fraction of fine variance explained by the box
  means, and the residual cannot be reduced by any statistical transformation of
  $T_c$.
- **Adding a genuinely fine predictor reduces the residual.** Fine orography is
  constant within a box? No — the *coarse* orography is constant within a box,
  but the fine orography varies, which is precisely why it carries information.

### 3.3 The lapse-rate correction

If temperature falls with height at rate $\Gamma$ (positive, $\mathrm{K\,km^{-1}}$),
then a point at height $h_f$ in a box whose mean height is $h_c$ has

$$\boxed{\;T_{\text{lapse}}(i) = T_c(B(i)) + \Gamma\bigl[h_c(B(i)) - h_f(i)\bigr].}$$

The bracket is the departure of the point from the box mean elevation; with
$\Gamma = 6.5\ \mathrm{K\,km^{-1}}$ and a $0.146\ \mathrm{km}$ within-box
standard deviation of orography (the demonstration's measured value), the
typical correction is of order $0.95\ \mathrm{K}$ — larger than the raw error of
the coarse model, which is why neglecting it matters.

## 4. Measurement: four methods

The demonstration uses a synthetic transect: 80 fine points, 20 coarse boxes of
4 points, fine orography from 0.000 to $1.215\ \mathrm{km}$ (coarse range 0.000
to $0.972\ \mathrm{km}$), a chosen true lapse rate of
$6.5\ \mathrm{K\,km^{-1}}$, and fine temperatures with standard deviation
$2.504\ \mathrm{K}$. Methods are fitted on the first half and scored on the
second half.

| method | RMSE (K) | bias (K) |
|---|---|---|
| raw coarse (box mean repeated) | 1.056 | 0.000 |
| lapse-rate correction (true $\Gamma$) | 0.229 | 0.000 |
| statistical, predictor $=$ coarse $T$ only | 1.056 | 0.000 |
| statistical, predictors $=$ coarse $T$ and fine orography | 0.294 | 0.086 |

Three observations:

- **The lapse correction reduces RMSE by a factor of $4.6$** ($1.056 \to 0.229$).
  This is real added value, because fine orography is known independently of the
  coarse model.
- **Statistical downscaling with the coarse temperature alone changes nothing.**
  Its fitted coefficients are an intercept of $-0.000\ \mathrm{K}$ and a slope of
  $1.0000$: it recovered the identity, because the box-mean predictor is
  constant within a box and the box means already equal the fine means. RMSE is
  identical to the raw output, to three decimals.
- **The hybrid (coarse $T$ plus fine orography) recovers the lapse relation from
  data.** Its fitted orography coefficient is $-6.880\ \mathrm{K\,km^{-1}}$
  against a true $-6.500\ \mathrm{K\,km^{-1}}$, an error of
  $0.380\ \mathrm{K\,km^{-1}}$; its RMSE, $0.294\ \mathrm{K}$, is slightly worse
  than the analytic correction because it also fits noise.

The variance accounting tells the same story in one number:

| quantity | value (K²) |
|---|---|
| total fine-scale variance | 6.3487 |
| variance left by the raw coarse output | 1.5100 |
| variance left after the lapse correction | 0.0697 |
| fraction of the raw residual variance removed | 0.9538 |

So $95.4\%$ of the fine-scale variance left by the coarse field is correlated
with fine orography. What remains ($0.0697\ \mathrm{K^{2}}$, a standard
deviation of $0.264\ \mathrm{K}$) is the noise the demonstration injected
($0.30\ \mathrm{K}$) plus the imperfection of the fit. **No statistical method
can reduce that part**, because no predictor contains it.

## 5. The stationarity failure

Now change the true lapse rate in the target half from $6.5$ to
$8.5\ \mathrm{K\,km^{-1}}$ — a physical change of regime, as would occur if the
relationship between circulation and local temperature changed.

| method | RMSE (K) | bias (K) |
|---|---|---|
| raw coarse | 1.367 | 0.000 |
| lapse-rate correction using the old $\Gamma$ | 0.386 | 0.000 |
| statistical, coarse $T$ only | 1.367 | 0.000 |
| statistical, coarse $T$ and fine orography | 1.117 | **$+0.794$** |

The statistical model trained on the old regime acquires a systematic error of
$+0.794\ \mathrm{K}$ — nearly a kelvin of bias, not scatter. The lapse method
with a frozen $\Gamma$ also degrades ($0.229 \to 0.386\ \mathrm{K}$), for the
same reason: it too assumed a constant.

This is the central caveat of statistical downscaling. It is not a defect of the
regression; it is the regression doing what it was told. **A statistically
downscaled product carries an implicit claim that the training relationship
holds in the target period.** When the claim fails, the error appears as a bias,
and a bias is invisible to an uncertainty estimate built only from the residual
scatter of the training fit.

## 6. Worked example: the lapse correction, by hand

*Problem.* A coarse box has mean elevation $h_c = 0.55\ \mathrm{km}$ and mean
temperature $T_c = 285.00\ \mathrm{K}$. Two fine points in the box have
elevations $0.20\ \mathrm{km}$ and $1.10\ \mathrm{km}$. Using
$\Gamma = 6.5\ \mathrm{K\,km^{-1}}$, downscale.

*Solution.*

1. Point A: $T = 285.00 + 6.5(0.55-0.20) = 285.00 + 2.275
   = 287.28\ \mathrm{K}$.
2. Point B: $T = 285.00 + 6.5(0.55-1.10) = 285.00 - 3.575
   = 281.43\ \mathrm{K}$.
3. The within-box spread produced is $287.28 - 281.43 = 5.85\ \mathrm{K}$,
   entirely from the orography term.

*Interpretation.* The correction is proportional to the elevation departure, so
its error is proportional to the error in $\Gamma$. A $10\%$ error in $\Gamma$
($6.5 \to 5.85\ \mathrm{K\,km^{-1}}$) changes point B by
$-3.575 \times 0.90 = -3.218\ \mathrm{K}$ instead, i.e. by
$+0.357\ \mathrm{K}$ — larger than the hybrid method's total RMSE in Section 4.
Choosing $\Gamma$ is therefore the dominant modelling decision in an
orography-based downscaling, and it should be reported either with its
uncertainty or as a fitted coefficient (as the hybrid does).

## 7. Assumptions and regime of validity

1. **The coarse model conserves the box mean.** The demonstration assumes
   $T_c(B)$ equals the box mean of the fine truth. Real coarse grids do not
   satisfy this exactly, which adds an error the method cannot see.
2. **The lapse rate is a single constant.** It varies with season, humidity and
   stability. A single $\Gamma$ is a first-order closure.
3. **Statistical downscaling assumes stationarity.** Section 5 quantifies the
   penalty when it fails; the penalty appears as bias.
4. **Perfect prognosis.** The predictors are assumed skillfully available at the
   target time. In a projection, the coarse $T$ is itself a model output with
   its own error, which propagates into the downscaled product.
5. **Point-scale validity.** A statistical fit at station points does not
   generalise to an unobserved grid cell without assuming spatial homogeneity of
   the relationship.
6. **Added value must be demonstrated, not asserted.** The correct test is
   whether the downscaled product beats the raw coarse output against
   independent fine observations; the demonstration does exactly this on a
   held-out half of the transect.

## 8. Units and dimensional analysis

| quantity | symbol | unit | check |
|---|---|---|---|
| elevation | $h$ | km | |
| lapse rate | $\Gamma$ | $\mathrm{K\,km^{-1}}$ | |
| correction | $\Gamma(h_c-h_f)$ | K | $\mathrm{K\,km^{-1}}\times\mathrm{km}$ |
| residual variance | | $\mathrm{K^{2}}$ | square of a temperature |

A common unit error is to fit orography in metres while using $\Gamma$ in
$\mathrm{K\,km^{-1}}$, which inflates the correction by $10^{3}$. Check the
product's unit before trusting the coefficient.

## 9. Python demonstration

[`code/downscaling_demo.py`](code/downscaling_demo.py):

1. generates a fine orography and its coarse box means, and reports the
   within-box orography standard deviation;
2. builds fine and coarse temperatures from a chosen lapse rate;
3. fits and scores raw, lapse-rate, statistical and hybrid downscaling on a
   held-out half;
4. repeats the comparison after changing the true lapse rate, isolating the
   non-stationarity bias;
5. decomposes the fine-scale variance into the part a fine predictor removes and
   the part no predictor contains.

It is print-only, seeded with `np.random.default_rng(20261014)`, and exits 0.

## 10. Exercises

See [`exercises/04-downscaling-exercises.md`](exercises/04-downscaling-exercises.md)
and [`exercises/04-downscaling-solutions.md`](exercises/04-downscaling-solutions.md).

## Mastery checkpoint

> **(a)** A coarse box has $T_c = 288.0\ \mathrm{K}$, $h_c = 0.30\ \mathrm{km}$.
> Downscale to fine points at $0.05\ \mathrm{km}$ and $0.90\ \mathrm{km}$ with
> $\Gamma = 6.0\ \mathrm{K\,km^{-1}}$.
> **(b)** Regress the two resulting temperatures on fine orography and recover
> the fitted coefficients; state why the intercept is not $288.0\
> \mathrm{K}$.
> **(c)** Explain in one sentence why adding the coarse temperature as a
> predictor alongside fine orography helps, and why adding the coarse
> temperature alone does not.
> **(d)** A downscaled product has a training RMSE of $0.3\ \mathrm{K}$ and, in a
> warmer target decade, a mean error of $1.0\ \mathrm{K}$. State which
> assumption failed and how you would detect it without knowing the truth.

## Common pitfalls

1. **Confusing downscaling with forecasting.** Downscaling refines a field; it
   does not create predictive information.
2. **Assuming a regression can add fine structure.** It is bounded by the
   predictors' correlation with the target; a within-box-constant predictor adds
   nothing.
3. **Ignoring non-stationarity.** The bias it produces is invisible to residual
   based uncertainty estimates.
4. **Reporting only scatter.** Biases are the errors that matter for impacts and
   adaptation; they must be measured against an independent record.
5. **Forgetting that $\Gamma$ is a choice.** Its uncertainty propagates linearly
   into the correction.
6. **Declaring added value without a held-out comparison.** The right test is
   against independent fine-scale observations.

## Related modules

- [16-05 Climate Models](README.md).
- [16-05-03 Model Evaluation, Skill and Benchmarking](03-model-evaluation.md) —
  the metrics used here.
- [16-08 Climate Observations and Data](../08-climate-observation-and-data/README.md) —
  where the observed fine-scale record comes from.
- [16-07-04 Impacts, Vulnerability and Risk Assessment](../07-climate-extremes-and-attribution/04-impacts-and-risk.md) —
  the user side that makes downscaled products necessary.
- [21-07 Time-Series Modelling and Forecasting](../../21-statistics-bayesian-ml/07-time-series-and-forecasting/README.md) —
  regression and stationarity in general.
