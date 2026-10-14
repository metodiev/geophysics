# Module 25-03 — Advanced Projects

**Stages:** advanced · **Prerequisites:** modules
[25-01](../01-beginner-projects/README.md) and
[25-02](../02-intermediate-projects/README.md), plus the method modules named
in each lesson.

This module adds the last ingredient a project needs before it becomes research:
**an assessment of what the model resolves**. Every lesson here fits a model and
then measures three things that a fit alone does not give — a statistical
uncertainty, a systematic or bias term, and a statement of the set of models the
data cannot distinguish. The measures are not decorative. A magnetic depth from a
skewed anomaly is biased by $+14.8\%$ unless the analytic signal is used, and the
analytic signal itself carries a $+4.5\%$ bias from the smoothing. A two-layer
resistivity sounding recovers its half-space resistivity $15.5\%$ high at a
chi-square of $1.07$ per datum, because the thickness and the resistivity trade
against each other at a correlation of $+0.83$. A gravity inversion with 32
parameters resolves the equivalent of $21.4$ of them and returns a mean
uncertainty, $15.09\ \mathrm{kg\,m^{-3}}$, that is $1.6$ times smaller than its
actual error.

The organising idea is therefore **the deliverable is a set, not a number**. Each
project ends with an object that describes a family: a trade-off curve for the
resistivity, a principal-axis interval for strain, an equivalence class for the
density model, a measured false-positive rate for a climate trend. Where the
module quotes a single best-fit value — and it does, in every lesson — the
accompanying text states which measurement makes that value conditional and how
large the condition is. This is the habit that separates a report a reviewer
accepts from one that is returned.

Provenance is stated per lesson. Real data are named where the project genuinely
needs them — the IGRF coefficients for magnetics, the NOAA global gravity
database, the NOAA land-based station archive, the EarthScope/UNAVCO facility for
GNSS — and every number in the prose comes from a **SYNTHETIC** demonstration that
runs without a network. Each demonstration is print-only, seeded with
`np.random.default_rng(20261014)`, runs in under a second and exits 0.

## Learning objectives

By the end of this module you will be able to:

1. **Derive** the Hilbert relation for a 2-D potential field and **use** the
   analytic signal to estimate a magnetic source's depth independently of its
   magnetisation direction.
2. **Quantify** the bias a regional trend and a smoothing filter introduce, and
   **separate** it from the statistical uncertainty.
3. **Invert** a resistivity sounding and **measure** its equivalence class by
   profile likelihood, comparing it with the linearised interval.
4. **Estimate** a depth of investigation from a model's sensitivity to its
   deepest parameter.
5. **Build and judge** a reflection processing flow: velocity resolution, NMO
   residual moveout, NMO stretch mute and measured stacking gain.
6. **Estimate** a climate trend with an autocorrelation-corrected error bar and
   **measure** the test's false-positive rate on surrogates.
7. **Compute** a strain-rate tensor from a GNSS velocity field, with principal
   axes, uncertainties and an explicit aperture.
8. **Report** a gravity inversion with a covariance, a resolution trace and a
   sampled equivalence class.

## Prerequisites

- [25-02-02 Project: Gravity Anomaly of Simple Bodies](../02-intermediate-projects/02-simple-gravity-model.md) —
  the closed-form bodies that projects 01 and 06 extend.
- [25-02-04 Project: Interpreting a Refraction Survey](../02-intermediate-projects/04-refraction-interpretation.md) —
  the inverse-problem conditioning that project 02 develops.
- [01-10-06 Hilbert Transform, Analytic Signal and Instantaneous Phase](../../01-mathematics/10-fourier-analysis/06-hilbert-transform.md) —
  the transform behind project 01.
- [18-02-04 SVD Analysis: Model Resolution and Data Importance](../../18-inverse-problems/02-linear-inverse-problems/04-svd-analysis-inverse.md)
  and
  [18-03-02 Tikhonov Regularisation and the Smoothing Trade-Off](../../18-inverse-problems/03-regularization/02-tikhonov.md) —
  the machinery of projects 02 and 06.
- [20-05-01 Stochastic Processes, Stationarity and Ergodicity](../../20-signal-processing/05-noise-and-random-signals/01-stochastic-processes.md) —
  the integrated time that inflates project 04's error bars.
- [06-09-03 Velocity Analysis and Moveout Interpretation](../../06-seismology/09-reflection-seismology/03-velocity-analysis.md) —
  the methods of project 03.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Project: Magnetic Anomaly Modelling and Depth Estimation](01-mag-anomaly-modelling.md) | advanced | The analytic signal gives 4.160 km where the skewed anomaly's half-width gives 4.594 km; the residual bias is $+4.5\%$ |
| 02 | [Project: ERT Inversion with Resolution Assessment](02-ert-inversion-project.md) | advanced | $+15.5\%$ on $\rho_2$ at $\chi^2 = 1.07$ per datum, with a $+0.834$ correlation against thickness |
| 03 | [Project: Seismic Reflection Processing Flow](03-seismic-processing-project.md) | advanced | A $5\%$ velocity error is $0.70$ of a wavelet period; the stack gain of 8.88 is $\sqrt{N}$, and 11.16 is interpolation |
| 04 | [Project: Climate Data Analysis and Trend Attribution](04-climate-data-analysis-project.md) | advanced | A naive trend test fires on $43.8\%$ of no-trend surrogates; the corrected test on $7.8\%$ |
| 05 | [Project: GNSS Strain Rate Estimation](05-gnss-strain-project.md) | advanced | $e_1 = +24.889$ nanostrain yr⁻¹ over 200 km, $+20.714$ over the inner half with $2.5\times$ the error |
| 06 | [Project: Gravity Inversion with Uncertainty Quantification](06-gravity-inversion-uq.md) | advanced | 21.42 of 32 parameters resolved; the uncertainty is $1.6\times$ smaller than the error |

## Suggested path

**If you are working through the folder in order:** 01 → 02 → 03 → 04 → 05 → 06.
Project 01 establishes the bias-versus-scatter accounting that all five later
projects reuse.

**If you are a potential-fields geophysicist:** 01 and 06, in that order, with
[25-02-02](../02-intermediate-projects/02-simple-gravity-model.md) as the
refresher. The pair covers depth estimation and inversion, which are the two
halves of the discipline.

**If you use time series:** 04, then
[25-02-03](../02-intermediate-projects/03-fourier-analysis-signals.md) for the
spectral side, then the geodetic series ideas of
[20-08-03](../../20-signal-processing/08-timeseries-analysis-geophysics/03-geodetic-time-series.md).

**If you are preparing a research project:** 02 §5 and 06 §6–7 are the two
templates to copy — an equivalence class measured by profile likelihood and one
sampled from a posterior. Both are transferable to any inversion you will run.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-mag-anomaly-modelling.md`](01-mag-anomaly-modelling.md) | Project 01 |
| [`02-ert-inversion-project.md`](02-ert-inversion-project.md) | Project 02 |
| [`03-seismic-processing-project.md`](03-seismic-processing-project.md) | Project 03 |
| [`04-climate-data-analysis-project.md`](04-climate-data-analysis-project.md) | Project 04 |
| [`05-gnss-strain-project.md`](05-gnss-strain-project.md) | Project 05 |
| [`06-gravity-inversion-uq.md`](06-gravity-inversion-uq.md) | Project 06 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every project |
| [`code/`](code) | Six runnable demonstrations |

| Script | What it prints |
|---|---|
| [`code/mag_anomaly_modelling_demo.py`](code/mag_anomaly_modelling_demo.py) | Skewed anomaly geometry, Hilbert-relation check, analytic-signal Lorentzian fit, trend bias sweep, Monte Carlo depth |
| [`code/ert_inversion_demo.py`](code/ert_inversion_demo.py) | Wenner sounding, regularised inversion, correlation matrix, profile likelihood, depth of investigation |
| [`code/seismic_processing_demo.py`](code/seismic_processing_demo.py) | Semblance velocity picks with bandwidths, NMO residual moveout, stretch mute, measured stacking gains |
| [`code/climate_trend_demo.py`](code/climate_trend_demo.py) | Trend with naive and corrected errors, measured false-positive rates, annual-mean comparison |
| [`code/gnss_strain_demo.py`](code/gnss_strain_demo.py) | Velocity gradient, strain/rotation/dilatation, principal axes, aperture table, outlier test |
| [`code/gravity_inversion_uq.py`](code/gravity_inversion_uq.py) | Kernel check, $\chi^2$ scan, covariance and resolution, posterior equivalence class |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
pandas:

```bash
cd 25-projects-capstone/03-advanced-projects/code

/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python mag_anomaly_modelling_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python ert_inversion_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python seismic_processing_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python climate_trend_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gnss_strain_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gravity_inversion_uq.py
```

Each script prints labelled results with units, states its **SYNTHETIC**
provenance, reads no files, uses no network, draws no plots and exits 0. Each runs
in under a second.

## Mastery checkpoint

Produce one resolution assessment for a model you have fitted:

> **(a)** State the forward model, its parameters and its data. **(b)** Fit it and
> report each parameter with a statistical uncertainty. **(c)** Measure the
> **equivalence class**: profile-likelihood the parameter you care about, or sample
> the posterior, and report the range that fits within the data's own precision.
> **(d)** Measure the **bias**: refit under a deliberately wrong assumption
> (a trend left in, a wrong matrix, a wrong velocity, a wrong prior) and report
> how far the answer moves. **(e)** Compare (b), (c) and (d) and state which
> dominates. **(f)** State the one additional observation that would shrink the
> dominant term, with its mechanism. Templates: the profile likelihood of
> [02 §5](./02-ert-inversion-project.md), the posterior ensemble of
> [06 §7](./06-gravity-inversion-uq.md), and the wrong-assumption test of
> [01 §7](./01-mag-anomaly-modelling.md).

## Common pitfalls across this module

1. **Reporting a best-fit value as the answer.** Every lesson here measures how
   large the class of equally good models is, and in every case it is large.
2. **Quoting a statistical error while a systematic term dominates** — the
   $+14.8\%$ magnetisation bias, the $+12.9\%$ trend bias, the $+2.92\ \mathrm{p.u.}$
   matrix bias of module 25-02.
3. **Choosing a regularisation or processing parameter by taste.** The discrepancy
   principle and the mute threshold are both stated choices with measured
   consequences.
4. **Assuming a test is calibrated because the formula says 5%.** The naive
   climate trend test fired on $43.8\%$ of surrogate records.
5. **Forgetting the aperture or the averaging length.** A strain rate, a stacked
   section and a smooth model each average over a scale that belongs in the
   report.

## Related modules

- [25-02 Intermediate Projects](../02-intermediate-projects/README.md) — the
  conditional-parameter accounting this module extends into full resolution
  assessment.
- [25-04 Graduate Projects](../04-graduate-projects/README.md) — non-linear
  inversions, time series and joint problems that reuse these measures.
- [18 Inverse Problems](../../18-inverse-problems/README.md) — the theory behind
  every covariance, resolution matrix and equivalence class used here.
- [21 Statistics and Bayesian ML](../../21-statistics-bayesian-ml/README.md) —
  the resampling, regression and error-rate machinery of project 04.
- [22 Data Engineering and Reproducibility](../../22-data-engineering-reproducibility/01-research-software-engineering/README.md) —
  how the flows and ensembles of this module become reproducible pipelines.
