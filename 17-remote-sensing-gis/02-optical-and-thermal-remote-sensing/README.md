# Module 17-02 — Optical and Thermal Remote Sensing

**Stages:** advanced → doctoral · **Prerequisites:** module
[17-01 Remote Sensing Physics](../01-remote-sensing-physics/README.md) and
[21-04 Machine Learning Fundamentals](../../21-statistics-bayesian-ml/04-machine-learning-fundamentals/README.md)
(for the accuracy-assessment material).

This module takes the radiometry of 17-01 and does the things remote sensing is
actually used for: reduce a reflectance spectrum to a few numbers that mean
something, separate a pixel into materials, measure a surface temperature and a
heat flow, assign labels, detect change, and find a mineral or an anomaly. Every
lesson is built the same way: derive the estimator, measure what it does to a
synthetic scene, and report the failure mode with a number attached.

The organising idea is that **each estimator is an invariance statement with a
residual**. A band ratio cancels a multiplicative gain exactly and an additive
haze not at all. A spectral index saturates, so above a certain biomass its
inversion is a prior rather than a measurement. An unmixing solution is physical
only after projection onto the simplex, and that projection biases small
fractions toward zero. A thermal retrieval is a two-unknowns-one-equation problem
in which emissivity and temperature are degenerate, so a brightness temperature is
not a surface temperature. A classifier's single accuracy figure conceals the one
class pair that matters. A change image detects illumination, misregistration and
instrument drift before it detects the surface. A band-depth ratio cancels
brightness exactly, slope partially, and nothing at all when the material lacks
the denominator feature.

A second theme is **assessment**. Every lesson states what should be reported
alongside the answer: the operating point of a change map, the confusion matrix of
a classification, the emissivity source of a temperature product, the continuum
rule of a band depth, the endmember provenance of an abundance map, and the
false-alarm rate of a geobotanical anomaly. None of these is administrative; each
is the difference between a measurement and an assertion.

All models and data in this module are **SYNTHETIC**. No real scene, sensor,
mission, product, material, mineral or dataset is used. The demonstrations
generate their scenes, spectra and series in code with a fixed random seed
(`np.random.default_rng(20261014)`), read no files, need no network access, print
labelled results with units, and exit 0. Where a measurement contradicted an
intended statement during writing, the lesson was changed to match the
measurement.

## Learning objectives

By the end of this module you will be able to:

1. **Prove** the invariance of a band ratio to a multiplicative gain, **derive**
   the residual error from an additive offset, and **compute** the propagated
   uncertainty of an index from per-band noise.
2. **Derive** the sensitivity of a saturating index–property relation and
   **state** the point beyond which its inversion is unbounded.
3. **Derive** the soil-adjustment tuning condition for a linear soil line and
   **show** invariance to soil brightness along it.
4. **Solve** the linear mixing model unconstrained, sum-to-one constrained and
   fully constrained, and **quantify** the conditioning, the noise propagation and
   the boundary bias of each.
5. **Convert** a thermal radiance to a brightness temperature, an emissivity and a
   surface temperature, and **quantify** the temperature–emissivity degeneracy.
6. **Derive** the thermal skin depth, damping and phase lag, and **convert** a
   surface temperature anomaly to a heat-flow anomaly with a stated thickness and
   conductivity.
7. **Derive** the quadratic Gaussian discriminant, **compute** a confusion matrix,
   Cohen's $\kappa$ and a Mahalanobis separability, and **demonstrate** the Hughes
   phenomenon and the accuracy paradox with numbers.
8. **Compute** difference, ratio and change-vector change images, **derive** their
   noise, and **quantify** the cost of misregistration and of an uncorrected gain
   drift.
9. **Derive** the breakdown point of a robust slope estimator and **measure** the
   false-positive rate of a trend test under four assumption violations.
10. **Perform** continuum removal, **compute** band depths and depth ratios, and
    **compare** estimators at equal false-alarm rate.
11. **Quantify** the false-alarm budget of a geobotanical inference and **state**
    the independent evidence a mineralisation claim requires.

## Prerequisites

- [17-01-02 Reflectance, Emissivity and Spectral Signatures](../01-remote-sensing-physics/02-reflectance-and-emissivity.md)
  — the surface quantities every estimator here operates on.
- [17-01-03 Atmospheric Attenuation, Scattering and Correction](../01-remote-sensing-physics/03-atmospheric-effects.md)
  — the correction that must precede any of these estimators.
- [17-01-04 Spatial, Spectral, Temporal and Radiometric Resolution](../01-remote-sensing-physics/04-resolution-concepts.md)
  — the sampling and noise floor the estimators fight against.
- [21-04-03 Cross-Validation, Metrics and the Danger of Leakage](../../21-statistics-bayesian-ml/04-machine-learning-fundamentals/03-model-assessment.md)
  — the assessment framework used in lessons 04–05.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Multispectral Imaging, Band Ratios and Indices](01-multispectral-imaging.md) | advanced | A ratio cancels a multiplicative gain exactly and an additive haze not at all; indices saturate and have a null space |
| 02 | [Hyperspectral Sensing and Spectral Unmixing](02-hyperspectral.md) | doctoral | Unconstrained least squares is unphysical, constraints buy admissibility and cost bias, and a small residual does not validate the model |
| 03 | [Thermal Infrared: Land Surface Temperature and Heat Flow](03-thermal-infrared.md) | graduate | Emissivity and temperature are degenerate; a temperature anomaly is a heat-flow anomaly only through a stated thermal resistance |
| 04 | [Land Cover Classification: Supervised and Unsupervised](04-land-cover-classification.md) | advanced | One accuracy number hides the error; more dimensions can make it worse; imbalance makes a useless map look accurate |
| 05 | [Change Detection and Time-Series Analysis](05-change-detection.md) | graduate | Differencing detects illumination, misregistration and instrument drift; robustness and significance both have measured limits |
| 06 | [Vegetation Indices, Geobotany and Mineral Alteration Mapping](06-vegetation-and-geobotany.md) | doctoral | A depth is defined relative to a continuum; a depth ratio cancels brightness, reduces slope bias, and fails when the denominator feature is absent |

## Suggested path

**If you are new to these methods:** lessons 01 → 04 → 05, running each
demonstration. Lessons 02 and 06 are the doctoral-level steps and are easiest after
01 and 04.

**If you work with thermal data:** 03 in full, plus 02 §3.5 for the conditioning
argument that reappears whenever several measurements constrain several unknowns.

**If you are preparing a research project:** 01 §3.2 (invariance and its residuals),
02 §3.5–3.7 (conditioning and model error), 04 §3.5–3.7 (dimension, imbalance),
05 §3.5–3.9 (robustness, testing, drift), and 06 §3.4–3.9 (depths and false-alarm
budgets), with the ★★★ exercises.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-multispectral-imaging.md`](01-multispectral-imaging.md) | Lesson 01 |
| [`02-hyperspectral.md`](02-hyperspectral.md) | Lesson 02 |
| [`03-thermal-infrared.md`](03-thermal-infrared.md) | Lesson 03 |
| [`04-land-cover-classification.md`](04-land-cover-classification.md) | Lesson 04 |
| [`05-change-detection.md`](05-change-detection.md) | Lesson 05 |
| [`06-vegetation-and-geobotany.md`](06-vegetation-and-geobotany.md) | Lesson 06 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Six runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
pandas:

```bash
cd 17-remote-sensing-gis/02-optical-and-thermal-remote-sensing/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python multispectral_imaging_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python hyperspectral_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python thermal_infrared_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python land_cover_classification_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python change_detection_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python vegetation_geobotany_demo.py
```

Every demo prints labelled results with units, uses the fixed seed
`np.random.default_rng(20261014)`, reads no files, needs no network access, and
exits 0.

## Mastery checkpoint

Complete this without notes:

> A synthetic four-band scene contains vegetation-like
> $(\rho_{\rm red}, \rho_{\rm NIR}) = (0.04, 0.48)$ over a soil background, and a
> second acquisition is brighter by $10\%$ with a
> $0.02$ additive haze term. **(a)** Compute the index change caused by the haze
> for the vegetation pixel. **(b)** State what a ratio would have done with the
> $10\%$ gain, and what it does with the haze. **(c)** A pixel measures
> $\rho_{\rm red} = 0.30$, $\rho_{\rm NIR} = 0.42$; compute the index and decide
> whether to call it vegetation. **(d)** State the one additional measurement that
> would settle (c).

A worked version of (a)–(c) appears in the lesson-01
[solutions](exercises/01-multispectral-imaging-solutions.md).

## Common pitfalls

1. **Reporting an index without its noise.** Per-band noise of $0.010$ gives
   $\sigma_{\rm NDVI} = 0.03563$ for the demonstration's vegetation spectrum.
2. **Inverting a saturated index.** Above $\mathrm{LAI}\approx5$ the upper limit is
   unbounded in the synthetic relation.
3. **Believing the simplex constraint makes an answer unbiased.** The FCLS
   projection pushes small true fractions to exactly zero.
4. **Quoting a depth without its continuum rule.** Endpoint choice alone moved a
   depth by $-61\%$.
5. **Treating a brightness temperature as a surface temperature.** With
   $\varepsilon = 0.90$ that is $3.65\ \mathrm{K}$ too low.
6. **Converting a temperature anomaly to a heat flow without a thickness and a
   conductivity.**
7. **Reporting one classification accuracy number.** The demonstration's map is
   $98.67\%$ accurate and misses $95\%$ of the target class.
8. **Differencing unregistered or unnormalised images.** One pixel of
   misregistration inflates apparent change by $1.25\times$; an uncorrected
   $0.02\%$ per-month drift creates a trend $0.22\times$ the true signal.
9. **Quoting a trend p-value without stating the autocorrelation and seasonal
   treatment.** The measured inflation under AR(1) noise is $6.3\times$.
10. **Calling a vegetation-stress anomaly a mineralisation anomaly** without an
    independent cause-separating measurement.

## Related modules

- [17-01 Remote Sensing Physics](../01-remote-sensing-physics/README.md) — the
  radiometry these estimators rest on.
- [17-05 GIS Fundamentals](../05-gis-fundamentals/README.md) — the data models and
  resampling that store and combine these products.
- [18-inverse-problems](../../18-inverse-problems/README.md) — the general
  treatment of unmixing, atmospheric correction and retrieval as inversions.
- [21-04 Machine Learning Fundamentals](../../21-statistics-bayesian-ml/04-machine-learning-fundamentals/README.md)
  — the assessment, regularisation and clustering theory behind lessons 02, 04 and
  05.
- [02-10 Optics and Photometry](../../02-physics/10-optics-and-photometry/README.md)
  — spectroscopy, radiative transfer and diffraction.
