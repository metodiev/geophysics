---
id: 25-05-03
title: "Project: Geodynamic Model-Data Comparison"
level: doctoral
prereqs: ["13-03-04", "13-05-03", "18-03-03", "25-04-01"]
estimated_minutes: 240
tags: [projects, geodynamics, model-data-comparison, inverse-problems, doctoral]
---

# Project: Geodynamic Model-Data Comparison

## Learning objectives

By the end of this project you will be able to:

1. **Derive** the subsidence of a cooling half-space and of a cooling plate from the
   depth-integrated temperature deficit.
2. **Fit** both models to bathymetry and heat flow by weighted least squares and
   **report** every parameter with its uncertainty.
3. **Reject** a model on a misfit statistic rather than on a plot, and **use** the
   *structure* of the residual as evidence for the physics that is missing.
4. **Separate** model error from noise by fitting the same model to noiseless
   synthetic data over the same range.
5. **Explain** the trade-off between a ridge offset and a subsidence rate, and why
   the age range of the data decides which of the two is resolved.
6. **State** which combination of physical parameters each observable measures, and
   refuse to report a single parameter that the data only determine as a product.
7. **Write** a model–data comparison that reports the region of validity of each
   model alongside its parameters.

All data in this project are **SYNTHETIC**: a plate model with a stated thickness is
sampled to produce bathymetry and heat flow in
[`code/geodynamic_model_demo.py`](./code/geodynamic_model_demo.py). For the project
itself, seafloor age and depth grids are available from the open archives cited in
`tools/verified_links.tsv` (NOAA/NGDC and the Global Multi-Resolution Topography
compilations), and the model–data workflow is unchanged when they are used.

## Prerequisites

- [13-03-04 Basin Geodynamics and Thermal Subsidence](../../13-geodynamics-tectonics/03-plate-tectonics-quantitative/04-basin-geodynamics.md) —
  the same thermal-subsidence physics applied to sedimentary basins.
- [13-05-03 Benchmarking Geodynamic Models](../../13-geodynamics-tectonics/05-geodynamic-modelling/03-benchmarking-geodynamics.md) —
  how a forward model's validity range is established.
- [18-03-03 Choosing the Regularisation Parameter](../../18-inverse-problems/03-regularization/03-parameter-choice.md) —
  discrepancy arguments and what "the data are fitted" means.
- [25-04-01 Project: Finite-Difference Wave Propagation](../04-graduate-projects/01-fd-wave-propagation-project.md) —
  the numerical-forward-model skills this project assumes.

## 1. The question

*Over what age range is the half-space cooling model of the oceanic lithosphere
adequate, and what does the failure of the model outside that range tell us?*

The half-space model predicts seafloor depth $d = d_\text{ridge} + a\sqrt{t}$ and
heat flow $q = C/\sqrt{t}$ — two one-parameter laws fitted to thousands of kilometres
of seafloor. The demonstration shows what happens when they are fitted outside their
region of validity: to bathymetry generated from a plate model with a 95 km base, the
half-space fit returns $a = 161.7$ against a theoretical $359.4\
\mathrm{m\,Myr^{-1/2}}$, with a ridge depth of $3426$ m against a true $2500$ m, a
residual rms of $236.5$ m against $100$ m of noise ($\chi^2/\text{dof} = 5.59$), and
a residual that is *systematic*. Restricting the fit to the young seafloor and
fitting the plate model both recover the physics: the plate model returns $L = 94.0$
km against a true $95$ km with $\chi^2/\text{dof} = 1.04$. **A geodynamic model is
defined by its range of validity, and the data decide where that range ends.**

## 2. The two forward models

**Half-space cooling.** With $T(z,t) = T_m\,\mathrm{erf}\!\left(z/2\sqrt{\kappa
t}\right)$, the depth-integrated temperature deficit is
$\int_0^\infty (T_m - T)\,dz = 2T_m\sqrt{\kappa t/\pi}$, and thermal contraction
gives

$$d(t) = d_\text{ridge} + a\sqrt{t},\qquad
a = \frac{2\rho_m\alpha T_m}{\rho_m-\rho_w}\sqrt{\frac{\kappa}{\pi}}\,\sqrt{t_\text{Myr}}
= 359.4\ \mathrm{m\,Myr^{-1/2}},$$

$$q(t) = \frac{C}{\sqrt{t}},\qquad
C = \frac{kT_m}{\sqrt{\pi\kappa t_\text{Myr}}} = 417.8\
\mathrm{mW\,m^{-2}\,Myr^{1/2}},$$

evaluated with $\kappa = 10^{-6}\ \mathrm{m^2\,s^{-1}}$, $\alpha = 3.0\times10^{-5}\
\mathrm{K^{-1}}$, $T_m = 1300\ ^\circ\mathrm{C}$, $\rho_m = 3300$,
$\rho_w = 1030\ \mathrm{kg\,m^{-3}}$, $k = 3.2\ \mathrm{W\,m^{-1}\,K^{-1}}$.

**Plate model.** The same cooling, but with the base held at $T_m$ at depth $L$:

$$T(z,t) = T_m\left[\frac{z}{L} + \frac{2}{\pi}\sum_{n=1,3,5,\dots}
\frac{1}{n}\sin\frac{n\pi z}{L}\,e^{-(n\pi/L)^2\kappa t}\right],$$

so the subsidence saturates at

$$d_\text{sat} = \frac{\rho_m\alpha T_m L/2}{\rho_m-\rho_w} = 2693\ \mathrm{m}$$

for $L = 95$ km. The plateau at old ages is the whole content of the model: it is
what the half-space model cannot produce.

## 3. The data and the fits (all SYNTHETIC)

Bathymetry at 60 ages from 2 to 160 Myr, depths 2961 to 5284 m, with 100 m rms
noise; heat flow at the same ages, 279.7 down to 40.4 mW m$^{-2}$, with 5%
multiplicative noise.

| fit | parameters | residual rms | $\chi^2/\text{dof}$ | verdict |
|---|---|---|---|---|
| half-space, 2–160 Myr | $d_\text{ridge} = 3426 \pm 39$ m, $a = 161.7 \pm 4.4$ | 236.5 m | 5.59 | rejected |
| plate model, 2–160 Myr | $L = 94.0$ km ($1\sigma$: 92.0–97.0), $d_\text{ridge} = 2485$ m, $d_\text{sat} = 2695$ m | 102.0 m | 1.04 | accepted |
| half-space, 2–39 Myr | $d_\text{ridge} = 2612$ m, $a = 323.8 \pm 18.1$ | 131.4 m | 1.72 | marginal |
| half-space, 2–39 Myr, noiseless | $a = 336.8 \pm 18.1$ | 22.8 m | — | model error isolated |
| half-space heat flow | $C = 420.7$ (expected 417.8) | 5.45 mW m$^{-2}$ | 5.44 | rejected |
| plate-model heat flow, $L$ free | $L = 94.0$ km | — | 0.76 | accepted |

Four doctoral-level readings:

1. **One model can be wrong and still fit the amplitudes.** The half-space heat-flow
   coefficient is recovered to $0.7\%$ ($420.7$ against $417.8$) while the model is
   rejected at $\chi^2/\text{dof} = 5.44$. The *amplitude* is right and the *shape* is
   wrong, which is why a plot of a fit and a table of parameters are not evidence.
2. **The failure is systematic, and the pattern names the missing physics.** The
   half-space depth residuals (observed minus fitted) average $-192$, $+205$ and
   $-233$ m over the youngest, middle and oldest thirds of the age range: the fitted
   line runs *below* the observations at young and old ages and *above* them in the
   middle, the signature of a $\sqrt{t}$ curve pivoting about the middle of the range
   to accommodate a curve that flattens — the saturation the plate model supplies.
   The remaining bias is the missing plateau, and the fitted intercept
   ($3426$ m against a true $2500$ m) is where most of it went.
3. **Restricting the range removes most of the bias and exposes the rest.** Fitting
   the same half-space model to 2–39 Myr gives $a = 336.8$ noiselessly against the
   theoretical $359.4$: the remaining $23\ \mathrm{m\,Myr^{-1/2}}$ is the plate
   model's own departure from $\sqrt{t}$ inside the (nominally valid) young range.
   The noisy fit gives $323.8$, $13$ below the noiseless one — that $13$ is the
   noise, and the two contributions are separated only by running the fit on data
   generated by the model itself.
4. **The plate thickness is recovered, and the recovery has a precision.** $L = 94.0$
   km against a true 95, with a $1\sigma$ interval of $[92.0, 97.0]$ km from
   $\Delta\chi^2 = 1$ — so $\pm 2.5$ km, **not** the $1$ km grid step, which limits
   only the search. The heat flow gives $L = 94.0$ km too, from an entirely different
   observable; that agreement is the strongest evidence in the demonstration and it
   exists because heat flow and bathymetry respond to the same $L$ through different
   physics. Both fits recover the thickness because the *plateau* is what the data
   contain, and the plateau exists only if the plate has a base.

## 4. Trade-offs and what each observable measures

**The ridge-offset/subisidence-rate trade-off.** With basis functions $1$ and
$\sqrt{t}$, the correlation between the two parameter estimates is $-0.94$ over
2–160 Myr and $-0.95$ over 2–39 Myr. It does not disappear at any range: the two
columns of the design matrix are correlated over any finite interval, so an error in
the ridge depth is absorbed into the subsidence rate. The consequences are that
$d_\text{ridge}$ is meaningless without $a$ beside it, that extrapolating $a$ back to
$t=0$ is not a measurement of ridge depth, and that the *only* way to separate them
is to extend the age range — which is precisely why a global compilation agrees far
better than any single transect.

**The products.** Bathymetry measures $\alpha T_m$ and (with the plate model) $L$;
heat flow measures $kT_m/\sqrt{\pi\kappa}$ and $L$. Neither measures $T_m$,
$\alpha$, $k$ or $\kappa$ alone. Reporting "$T_m = 1300\ ^\circ\mathrm{C}$ from
seafloor depths" is a category error: the data constrain the product
$\alpha T_m$, and the split into $\alpha$ and $T_m$ requires another observable (a
petrological or seismic constraint on $T_m$, or a laboratory value of $\alpha$).
This is the normal condition of geodynamics, and the discipline it imposes is that
every reported parameter is accompanied by the combination the data actually
determine.

## 5. The project specification

**Steps.**

1. Choose a geodynamic forward model with a stated range of validity and state the
   observables it predicts (depth, heat flow, gravity anomaly, topography, uplift
   rate, …).
2. Derive the model's parameter dependence, and identify which combinations of
   physical parameters the data determine.
3. Build the synthetic or real dataset; state its noise level with a source for the
   estimate (`sigma` from the data, not from hope).
4. Fit each model by weighted least squares; report every parameter with its formal
   uncertainty and the parameter correlation matrix.
5. Report $\chi^2/\text{dof}$ for each fit and state the accept/reject decision and
   the criterion used.
6. Compare the same fit on noiseless synthetic data over the same range to separate
   model error from noise.
7. Examine the residual as a function of the independent variable; identify the
   systematic component and the physics it implies.
8. Repeat with the second observable, and compare the parameters shared between the
   two fits.
9. Write the comparison: model, range of validity, parameters with uncertainties,
   statistic, systematic residual, and the products the data determine.

**Deliverable.** Parameter tables with uncertainties for each model, the
$\chi^2/\text{dof}$ decisions, the residual-versus-age diagnosis, and a statement of
the resolved parameter combinations.

**Success criterion.** Every parameter is reported with an uncertainty; the model
choice is justified by a statistic and not by a plot; the systematic residual is
named with the physics it implies; the noiseless run separates model error from
noise; and no single parameter is reported where only a product is constrained.

## 6. Failure modes

1. **Fitting outside the range of validity and blaming the data.** $a = 161.7$
   against $359.4$ is the model being wrong, not the seafloor.
2. **Judging by the amplitude alone.** The heat-flow coefficient is recovered to
   $0.7\%$ by a rejected model.
3. **Reporting no uncertainty, or only the diagonal.** The parameter correlation is
   $-0.94$: the marginal errors understate the joint uncertainty severely.
4. **Assuming a known noise level without measuring it.** $\chi^2/\text{dof}$ is
   meaningless if $\sigma$ was chosen to make it equal to one.
5. **Ignoring the correction for sediment, thermal rejuvenation or hotspot swells**
   when using real bathymetry — they are of the same order as the residuals
   discussed here and must be modelled or masked.
6. **Reporting a physical parameter that is only determined as a product** ($T_m$,
   $\alpha$, $\kappa$, $k$).
7. **Extrapolating a fitted law back to the ridge** without noting that the
   correlation between the offset and the slope makes that extrapolation the least
   constrained part of the fit.

## 7. Rubric

| Criterion | Weight | Full marks |
|---|---|---|
| Forward model derived and its validity range stated | 15% | derivation shown, asymptotics identified |
| Weighted fits with uncertainties and correlations | 25% | full parameter table, correlation quoted |
| Model comparison by statistic | 20% | $\chi^2/\text{dof}$ for each model, decision and criterion |
| Residual diagnosis | 15% | systematic residual quantified and attributed to physics |
| Model-error versus noise separation | 15% | noiseless run over the same range |
| Resolved combinations stated | 10% | products named, no single-parameter claims |

## 8. The honest summary

The product is a model that is accepted, a model that is rejected, and the reason.
The half-space model fitted over 160 Myr returns a subsidence rate a factor $2.2$ too
small and a residual $2.4$ times the noise level, with a systematic pattern; the same
model restricted to 39 Myr comes within $6\%$ of the theoretical coefficient
noiselessly; the plate model recovers a 94 km base from bathymetry and, independently,
from heat flow, with $\chi^2/\text{dof}$ of $1.04$ and $0.76$. The transferable
results are that the range of validity is part of the model, that a systematic
residual is the evidence for missing physics, and that geophysical data constrain
products of parameters, which the report must name.

## Python demonstration

[`code/geodynamic_model_demo.py`](./code/geodynamic_model_demo.py) prints every
number above: the theoretical coefficients, the two synthetic datasets, the
half-space and plate fits with uncertainties and $\chi^2/\text{dof}$, the
young-seafloor and noiseless comparison, and the heat-flow fits.

```bash
cd 25-projects-capstone/05-doctoral-projects/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python geodynamic_model_demo.py
```

Print-only, seeded with `np.random.default_rng(20261014)`, no network, no files, no
plots, exits 0, runs in about $0.2$ s.

## Exercises

Graded problems and worked solutions are in
[`exercises/03-geodynamic-model-data-exercises.md`](./exercises/03-geodynamic-model-data-exercises.md)
and
[`exercises/03-geodynamic-model-data-solutions.md`](./exercises/03-geodynamic-model-data-solutions.md).
The ★★★ item asks for a second observable and a joint inversion that separates two
parameters that a single observable can only determine as a product.

## Mastery checkpoint

Without notes:

1. Derive $a$ for half-space cooling from the depth-integrated temperature deficit.
2. Explain why the plate model saturates and at what depth.
3. State the accept/reject rule you would use and the two ways it can be misused.
4. Explain why $d_\text{ridge}$ and $a$ are correlated, and what removes the
   correlation.
5. Name two geodynamic parameters that are routinely reported but only constrained
   as products.

## Common pitfalls

1. Reporting a slope without its intercept's uncertainty.
2. Using a fixed, invented $\sigma$ to make $\chi^2/\text{dof} = 1$.
3. Ignoring the sign structure of the residual.
4. Treating the young-seafloor fit and the full-range fit as independent evidence
   when they share data.
5. Confusing the model's parameters with the physical constants they combine.

## Where this is used

Model–data comparison is the standard closing step of every geodynamic study: mantle
convection models against dynamic topography and the geoid, glacial-isostatic models
against uplift and gravity rates, and thermal models against heat flow, subsidence and
magnetotelluric structure — the last of these linking to
[25-04-02](../04-graduate-projects/02-mt-1d-2d-inversion.md), whose conductivity
profile is the same lithosphere sampled electrically. The same discipline appears in
the Bayesian treatment of [25-05-04](./04-bayesian-inversion-project.md), where the
model-choice decision of §3 becomes a posterior model probability.

## Related lessons

- [13-06-01 Isostasy and Flexure: Modelling Lithospheric Strength](../../13-geodynamics-tectonics/06-crustal-and-lithospheric-dynamics/01-isostasy-flexure-modelling.md) —
  the elastic-thickness analogue of the comparison made here.
- [18-06-02 Monte Carlo Uncertainty Propagation](../../18-inverse-problems/06-uncertainty-quantification/02-monte-carlo-uq.md) —
  how to propagate a measured $\sigma$ into a parameter uncertainty.
- [21-03-06 The Bayesian Workflow](../../21-statistics-bayesian-ml/03-bayesian-inference/06-bayesian-workflow.md) —
  the formal version of the accept/reject decision used in §3.
- [25-05-04 Project: Trans-Dimensional Bayesian Inversion](./04-bayesian-inversion-project.md) —
  what to do when the number of layers is itself unknown.

## Self-assessment checklist

- [ ] I can derive the half-space subsidence coefficient.
- [ ] I can fit two models and decide between them with a statistic.
- [ ] I can attribute a systematic residual to missing physics.
- [ ] I can separate model error from noise with a noiseless run.
- [ ] I can quote a full parameter uncertainty including correlations.
- [ ] I can name the products the data determine.
