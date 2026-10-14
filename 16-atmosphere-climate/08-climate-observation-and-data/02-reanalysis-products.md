---
id: 16-08-02
title: "Reanalysis: ERA5, MERRA, JRA and Their Caveats"
level: doctoral
prereqs: ["16-08-01", "16-05-02", "18-01-01"]
tags: [atmosphere, climate, reanalysis, data-assimilation, uncertainty, observations]
---

# Reanalysis: ERA5, MERRA, JRA and Their Caveats

> **All models and data in this module are SYNTHETIC.** The truth, the
> observations and the assimilating model in `code/reanalysis_demo.py` are a
> chosen scalar system with a deliberately large climate bias. No reanalysis
> product, numerical model, satellite, observing system or published value is
> used, and no numerical value is quoted from any published reanalysis.
> Different reanalysis families are named only as families that exist.

A **reanalysis** is a numerical weather-prediction model run over a historical
period while being continuously pulled toward observations by a data-assimilation
system. It is the most convenient object in climate science: complete in space and
time, physically consistent, with every variable present at every grid point. It
is also the most easily misread, because everything about that convenience comes
from the model, and the model is not the climate.

This lesson is about the gap between what a reanalysis *is* (an analysis:
observations plus a model, weighted by their stated uncertainties) and what it is
often *used as* (an observational record). The demonstration reduces the whole
system to one scalar state variable so that the mechanism is visible: a model with
a biased climate, an observing system whose density changes at a known year, and
an analysis that shows a trend where the truth has none. The mechanism is not a
simplification artefact; it is why reanalyses carry "caveats" as a permanent
feature rather than as a growing pain.

## Learning objectives

By the end of this lesson you will be able to:

1. **Describe** a reanalysis as a model constrained by observations, and
   **state** which properties are inherited from the model.
2. **Derive** the scalar analysis update from the least-squares/Bayes formulation,
   and **define** the background and observation error covariances.
3. **Demonstrate** that in the model-dominated limit the analysis reports the
   model's climate, including its bias.
4. **Quantify** how a change in observing-system density manufactures a
   discontinuity and therefore a trend, and **estimate** the trend from the
   discontinuity.
5. **Distinguish** a product's internal spread from its error against reality, and
   **explain** which component of the error the spread misses.
6. **State** when a reanalysis trend is defensible and when it is a hypothesis.
7. **Design** a validation that would distinguish a model artefact from a
   response to forcing.

## Prerequisites

- [16-08-01 Surface, Radiosonde and Satellite Climate Records](01-surface-and-satellite-records.md) —
  the observing systems whose changes drive the artefacts here.
- [16-05-02 GCMs, Resolution and Parameterisation](../05-climate-models/02-gcms-and-parameterisation.md) —
  the models that supply the background.
- [18-01-01 Forward vs Inverse Problems and the Practical Asymmetry](../../18-inverse-problems/01-inverse-problem-foundations/01-forward-and-inverse.md) —
  the estimation framing of the analysis step.

## 1. What a reanalysis is, precisely

Let $\mathbf{x}$ be the model state (temperature, wind, humidity, pressure at every
grid point and level). The system cycles through time:

1. **Background (forecast)**: advance the previous analysis with the model,
   $\mathbf{x}^{b}_t = \mathcal{M}\left(\mathbf{x}^{a}_{t-1}\right)$, with
   background error covariance $\mathbf{B}$.
2. **Observations**: all observations in the time window, related to the state by
   an observation operator $\mathbf{H}$, with error covariance $\mathbf{R}$.
3. **Analysis**: combine them,
   $$\mathbf{x}^{a}_t = \mathbf{x}^{b}_t
   + \mathbf{K}\left(\mathbf{y}_t - \mathbf{H}\mathbf{x}^{b}_t\right),
   \qquad \mathbf{K} = \mathbf{B}\mathbf{H}^{\mathsf{T}}
   \left(\mathbf{H}\mathbf{B}\mathbf{H}^{\mathsf{T}}+\mathbf{R}\right)^{-1}.$$

The quantity in brackets is the **innovation**: the part of the observation not
already explained by the background. The gain $\mathbf{K}$ decides how much of it
to believe.

Two properties follow immediately and they are the lesson. First, **where
observations are absent, $\mathbf{H}\mathbf{x}^{b} = \mathbf{y}$ trivially or the
innovation is undefined, and the analysis *is* the background** — a model
simulation. Second, **where observations are dense and accurate, the analysis is
close to the observations**, and the model's role is to fill and to smooth. A
change in observation density therefore changes *which* of the two the product
most resembles, and that change is not in the climate.

## 2. The scalar version, solved

For one state variable the recursion is exact and the numbers are transparent.
Write $B$ for the background variance, $R$ for the observation error variance, and
$K = B/(B+R)$. Then

$$x^{a} = x^{b} + K\left(y - x^{b}\right), \qquad
B^{a} = (1-K)B, \qquad B^{b}_{t+1} = \varphi^{2}B^{a} + Q,$$

with persistence $\varphi$ and process-noise variance $Q$. The **steady-state**
background variance is $B^{b}_{\infty} = Q/(1-\varphi^{2})$ in the absence of
observations, and the gain rises with $B$ and falls with $R$: the system trusts
the observations when the model is uncertain and the observations are good.

Two limits worth memorising:

- $R \to \infty$ (useless observations): $K \to 0$ and the analysis is the model.
- $B \to 0$ (a model believed to be perfect): $K \to 0$ and again the analysis is
  the model. **Believing your model too much and having no observations are the
  same failure.**

## 3. Worked example — a biased model and a changing observing system

The demonstration uses the scalar system with $\varphi = 0.70$, process-noise
standard deviation $0.05\ \mathrm{K}$, a *truth* forcing term of
$+0.050\ \mathrm{K\,step^{-1}}$ and a *model* forcing term of
$-0.100\ \mathrm{K\,step^{-1}}$. The corresponding climate means are

$$\bar x_{\text{truth}} = \frac{0.050}{1-0.70} = +0.167\ \mathrm{K}, \qquad
\bar x_{\text{model}} = \frac{-0.100}{1-0.70} = -0.333\ \mathrm{K},$$

a difference of $0.500\ \mathrm{K}$, deliberately large so the mechanism is
visible. The observation error standard deviation is $0.03\ \mathrm{K}$, and
observations are available with probability $0.05$ before year 30 and $0.80$
after it. The truth has **no trend**.

The assimilated product behaves exactly as the two limits predict:

| era | observations ingested | rms error (K) | mean error (K) | fitted trend (K/yr) |
|---|---|---|---|---|
| sparse (years 0–29) | 2 | 0.376 | $-0.350$ | $-0.0033$ |
| dense (years 30–59) | 25 | 0.113 | $-0.081$ | $+0.0017$ |

The truth fits $+0.0007\ \mathrm{K\,yr^{-1}}$; the analysis over the whole record
fits $+0.0070\ \mathrm{K\,yr^{-1}}$, an artefact of $+0.0062\
\mathrm{K\,yr^{-1}}$. **The product manufactures a trend where the climate has
none**, because the sparse-era analysis sits at the model's climate
($-0.333\ \mathrm{K}$) and the dense-era analysis sits near the observed one
($+0.167\ \mathrm{K}$). The change in bias at the transition is $+0.269\
\mathrm{K}$.

The arithmetic is worth doing explicitly, because it is the same arithmetic as
the step-leverage calculation in
[16-08-01 §8](01-surface-and-satellite-records.md). For a record of $L = 60$ years
with $t_0 = 30$,

$$\delta(\text{trend}) = \delta_{\text{jump}}\, \frac{\sum_{t\ge t_0}(t-\bar t)}{\sum_t (t-\bar t)^{2}}
= 0.269 \times \frac{450}{17{,}995} = 0.0067\ \mathrm{K\,yr^{-1}},$$

which reproduces the measured artefact $+0.0062\ \mathrm{K\,yr^{-1}}$ to within
the difference between the fitted jump and the era-mean difference. **A pure level
discontinuity is indistinguishable from a trend once a trend model is imposed on
it** — that is the whole of the reanalysis trend problem in one line.

## 4. The model-only limit, and why it looks credible

Setting observation availability to zero makes the product a free-running
simulation. In the demonstration its statistics are:

- rms difference from truth: $0.484\ \mathrm{K}$;
- mean difference (the climate bias): $-0.471\ \mathrm{K}$;
- standard deviation: $0.057\ \mathrm{K}$ against the truth's $0.073\
  \mathrm{K}$;
- fitted trend: $-0.0017\ \mathrm{K\,yr^{-1}}$.

So the free-running model has roughly the right variability and no spurious trend,
but the wrong mean level. A sparse-era reanalysis inherits that level, and because
the wrongness is a *constant offset plus the model's own internal variability*, the
result looks like a perfectly ordinary climate record. **Nothing in the appearance
of a reanalysis reveals which parts of it are model and which are observation**;
only the innovation statistics and the observing-system history do.

## 5. The spread is not the error

Ensemble reanalyses have a spread, and it is natural to read that spread as an
uncertainty. It is not, in one specific and important sense: the spread is
generated by the assimilation system's own error model, so it covers the errors
the system *knows about*. In the demonstration:

| era | mean background sd (K) | actual rms error (K) | ratio |
|---|---|---|---|
| sparse | 0.106 | 0.376 | 0.283 |
| dense | 0.056 | 0.113 | 0.491 |

In the sparse era the product's internal spread is less than one third of its
actual error, because the missing part — the model's climate bias — is not in the
spread at all. This is a structural property of assimilation, not a tuning
failure: the system is centred on the model's climate, and it is self-consistent
within that.

## 6. Naming the products, and what their differences mean

Several reanalysis families exist — for example ERA5, MERRA and JRA, produced by
different agencies with different models and different assimilation systems. Their
differences are the most practical uncertainty information a user has, and they
are informative precisely because the systems differ in their models, their
observation handling and their bias-correction choices.

But a difference between products is not an error bar:
the products share much of the same observing system, so their errors are partly
correlated, and they share the same physical model class, so their biases can
agree. Agreement between reanalyses is therefore **weaker evidence than it looks**,
and disagreement is a *lower bound* on the structural uncertainty. Rigorous
uncertainty estimates for reanalysis-derived trends come from error models and
from comparisons with independent, homogenised observational products — not from
the spread across a handful of families.

## 7. What a reanalysis is good for

- **Process studies and composites.** Composites of events require complete
  fields; the model's physical consistency is a feature, and the artefacts are
  largely common to the composite members and partly cancel in a difference.
- **Dynamical consistency.** Budgets (moisture, energy, momentum) close in a
  reanalysis by construction, which makes it the natural tool for budget
  calculations — with the caveat that closure is a property of the model, not of
  the atmosphere.
- **Drivers for other models.** Surface fluxes, winds and radiation fields are
  used to force ocean, wave, hydrology or dispersion models, where errors partly
  cancel in the response.

## 8. When a reanalysis trend is defensible

A reanalysis trend is defensible when:

1. the trend is **large compared with the spread across reanalysis families**;
2. it is **stable when the analysis is restricted to a period of stable, dense
   observing coverage**;
3. it is **reproduced by independent homogenised observational products**;
4. the **innovation statistics do not show a trend**, i.e. the model is not
   progressively drifting away from (or being pulled toward) the observations;
5. the trend is **not confined to the era boundary** of an observing-system
   change.

If any of those fails, the trend is a hypothesis about the product, not a result
about the climate.

## 9. Assumptions and regime of validity

1. **$\mathbf{B}$ and $\mathbf{R}$ describe the actual errors.** If $\mathbf{B}$
   is too small the analysis ignores the observations; if $\mathbf{R}$ is too
   small the observations are over-trusted and the analysis inherits their biases.
2. **The observation operator and bias corrections are right.** Satellite
   radiance bias correction is a large, model-dependent component of every modern
   reanalysis, and its choices leave fingerprints in the products.
3. **The model's climate is unbiased, or its bias is corrected.** The demonstration
   shows what happens when it is not: the sparse era reports the model.
4. **The observing system's changes are documented.** Otherwise a product
   discontinuity cannot even be attributed to a cause.
5. **Homogeneity is not provided by construction.** A reanalysis is not a
   climate data record; a trend must be tested against the observation and model
   changes that produced it.

## 10. Python demonstration

[`code/reanalysis_demo.py`](code/reanalysis_demo.py) runs the scalar assimilation
experiment and prints labelled results with units. It:

1. states the synthetic truth, model bias and observing-system schedule;
2. assimilates with a scalar Kalman filter and reports the analysis error by era;
3. measures the model-only limit;
4. measures the discontinuity at the observing-system change and the trend it
   manufactures;
5. compares the product's internal spread with its actual error;
6. prints the honest reanalysis caveat.

Every number in this lesson is printed by that demonstration (except the model
and truth climate means, which are the exact values
$C/(1-\varphi)$ computed in Section 3).

## Mastery checkpoint

> In the demonstration the truth has no trend and the model's climate mean is
> $-0.333\ \mathrm{K}$ against a true $+0.167\ \mathrm{K}$.
>
> **(a)** Compute the two climate means from $C/(1-\varphi)$ and verify the
> $0.500\ \mathrm{K}$ difference.
> **(b)** Explain, using the analysis update, why the sparse-era analysis reports
> the model's level.
> **(c)** The bias changes by $+0.269\ \mathrm{K}$ at year 30 of a 60-year record.
> Using $\sum_{t\ge30}(t-\bar t) = 450$ and $\sum_t(t-\bar t)^2 = 17{,}995$,
> compute the trend the discontinuity produces and compare it with the measured
> $+0.0062\ \mathrm{K\,yr^{-1}}$.
> **(d)** The background spread in the sparse era is $0.106\ \mathrm{K}$ against
> an actual rms error of $0.376\ \mathrm{K}$. State which component of the error
> the spread misses and why.
> **(e)** A reanalysis shows a large trend in a region where the observing system
> was sparse before 1979 and dense afterwards. Name two checks that would
> distinguish a real trend from a product artefact.

## Common pitfalls

1. **Treating a reanalysis as an observational record.** It is a model
   constrained by observations; in sparse regions it is a model.
2. **Reading the ensemble spread as the total uncertainty.** It omits the model's
   climate bias (a factor of $3.5$ understatement in the demonstration's sparse
   era).
3. **Fitting trends across an observing-system change.** A level discontinuity of
   $0.269\ \mathrm{K}$ produced an apparent trend of $+0.0062\
   \mathrm{K\,yr^{-1}}$ where none exists.
4. **Assuming agreement between products is confirmation.** Products share
   observations and model structure, so their errors are correlated.
5. **Using physical consistency as a validation.** Budget closure is manufactured
   by the model.
6. **Assuming bias corrections are neutral.** Satellite bias correction is
   model-dependent and leaves fingerprints.
7. **Quoting reanalysis humidity or flux trends as observed.** These are among the
   most strongly model-dependent fields in any reanalysis.

## Related modules

- [16-08-01 Surface, Radiosonde and Satellite Climate Records](01-surface-and-satellite-records.md) —
  the observations and their changes, which are the input here.
- [16-08-03 Homogenisation, Bias Adjustment and Uncertainty](03-climate-data-homogenisation.md) —
  the step changes a reanalysis contains but does not correct.
- [16-08-04 Analysing Climate Data in Python: xarray and CDO](04-climate-data-analysis-python.md) —
  how these products are actually handled, in practice, without mistakes.
- [16-05-02 GCMs, Resolution and Parameterisation](../05-climate-models/02-gcms-and-parameterisation.md) —
  the model half of the analysis.
- [16-05-03 Model Evaluation, Skill and Benchmarking](../05-climate-models/03-model-evaluation.md) —
  how to test a model against observations without circularity.
- [18-01-01 Forward vs Inverse Problems and the Practical Asymmetry](../../18-inverse-problems/01-inverse-problem-foundations/01-forward-and-inverse.md) —
  the estimation framework behind the analysis step.

## Self-assessment checklist

- [ ] I can write the analysis update and identify the innovation.
- [ ] I can explain the two limits in which the analysis is the model.
- [ ] I can estimate the trend a level discontinuity produces in a fitted slope.
- [ ] I can explain which component of the error the ensemble spread misses.
- [ ] I can state two checks that would make a reanalysis trend credible.
