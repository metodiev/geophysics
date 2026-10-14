---
id: 25-04-03
title: "Project: InSAR Deformation Time Series Analysis"
level: graduate
prereqs: ["25-04-04", "17-03-02", "20-08-01", "18-02-01"]
estimated_minutes: 200
tags: [projects, insar, geodesy, time-series, deformation, teaching]
---

# Project: InSAR Deformation Time Series Analysis

## Learning objectives

By the end of this project you will be able to:

1. **Fit** a displacement time series with a linear rate, a seasonal term and a
   coseismic step in one design matrix, and **report** each with its uncertainty.
2. **Measure** the bias that omitting the seasonal term induces in the rate, and
   **explain** why the misfit does not flag it.
3. **Measure** the bias from omitting a step, and **state** why the step's own
   uncertainty is usually large.
4. **Demonstrate** the window dependence of a linear rate in the presence of a
   decaying transient, and **state** the observation span a rate requires.
5. **Convert** a line-of-sight rate into a statement about horizontal motion, and
   **state** what the conversion needs.
6. **Grade** an InSAR velocity map by whether it carries its reference frame, its
   look geometry and its error correlation length.
7. **Diagnose** the four InSAR time-series failure modes: a seasonal term absorbed
   into a rate, a step explained as a trend, a transient aliased into a rate, and a
   formal error quoted where correlated errors dominate.

All series in this project are **SYNTHETIC**: generated from chosen deformation
components with chosen noise by
[`code/insar_timeseries_demo.py`](./code/insar_timeseries_demo.py). Sentinel-1
interferograms are distributed through the Copernicus Data Space Ecosystem at
<https://dataspace.copernicus.eu/>; no number below comes from it.

## Prerequisites

- [25-04-04 Project: Earthquake Catalogue Statistics and Hazard Inputs](./04-earthquake-catalog-analysis.md) —
  the tectonic setting the deformation is compared against.
- [17-03-02 InSAR: Interferometric Phase and Deformation Measurement](../../17-remote-sensing-gis/03-radar-remote-sensing/02-insar.md) —
  how the phase becomes a line-of-sight displacement.
- [20-08-01 Detrending, Deseasonalising and Anomalies](../../20-signal-processing/08-timeseries-analysis-geophysics/01-detrending-seasonality.md) —
  the decomposition this project fits jointly instead of sequentially.
- [18-02-01 Overdetermined Problems and Least Squares](../../18-inverse-problems/02-linear-inverse-problems/01-overdetermined.md) —
  the estimator and its covariance.

## 1. The question

*What is the deformation rate, and how much of it is an artefact of the model's
omissions?*

InSAR time series are fitted, not read. A rate comes out of a design matrix that
contains (or omits) a seasonal cycle, a step for a coseismic jump, and a functional
form for any transient; and each omission leaks into the rate. The demonstration
measures two of those leaks directly: leaving the seasonal term out of a
step-free series moves the rate by $-1.64\ \mathrm{mm\,yr^{-1}}$ and inflates its
error bar by a factor of $2.2$, and leaving the 10 mm step out moves the rate by
$+3.47\ \mathrm{mm\,yr^{-1}}$. **Neither leak is flagged by the misfit**, because
both omissions produce a model that still fits acceptably.

## 2. The data

**Synthetic series (SYNTHETIC).** 60 epochs at an 18-day repeat, spanning
$2.95\ \mathrm{yr}$, built from $12.0\ \mathrm{mm\,yr^{-1}}$ of linear
displacement, an $8.0\ \mathrm{mm}$ annual sinusoid, a $10.0\ \mathrm{mm}$ step at
$1.95\ \mathrm{yr}$, and $3.0\ \mathrm{mm}$ of Gaussian noise per epoch. The
resulting series runs from $-4.64$ to $+47.63\ \mathrm{mm}$. A second series
replaces the step with a $-15\ \mathrm{mm}$ transient decaying with a
$0.3\ \mathrm{yr}$ time constant.

**Provenance.** SYNTHETIC. The components are chosen; the deformation is not a
measured one, and no atmospheric or orbital error is simulated.

## 3. The project specification

**Steps.**

1. State the series: epochs, repeat interval, span, and the components you are
   putting in and testing for.
2. Fit four models — rate only; rate plus season; rate plus season plus step; and
   the same on the transient series — by weighted least squares, and tabulate each
   rate with its formal uncertainty and the residual rms.
3. Measure the bias from each omission, in $\mathrm{mm\,yr^{-1}}$ and in units of
   the omitted model's own error bar.
4. Fit the transient series over three windows of different start times and report
   the rate in each; state the window over which the transient dominates.
5. State what the rate means physically: a line-of-sight projection, to be
   converted with the incidence angle and, for a horizontal velocity, a second
   look geometry.
6. Write the report: the model, the fitted parameters with errors, the omission
   biases, the window dependence, and the error-correlation caveat.

**Deliverable.** The fitted table, the two omission-bias measurements, the window
table, and the caveat paragraph.

**Success criterion.** Every fitted parameter has a unit and an uncertainty; every
omission bias is quantified; the reference frame, the look geometry and the error
model are stated.

## 4. The model and why omissions leak into the rate

With $t$ in years the design matrix is

$$d(t) = a + b\,t + c\cos 2\pi t + e\sin 2\pi t + f\,H(t - t_s),$$

whose coefficients are the offset, the **rate** $b$, the seasonal amplitudes and
the **step**. The parameters are estimated by weighted least squares with
covariance $\sigma^{2}(A^{\mathsf T}WA)^{-1}$, so each carries a formal uncertainty.
The demonstration's full fit recovers the step as
$7.1133 \pm 4.7237\ \mathrm{mm}$ against a true $10.0\ \mathrm{mm}$: the estimate
is $0.6\sigma$ low and the uncertainty is large because a single step at
$t_s = 1.95\ \mathrm{yr}$ in a $2.95\ \mathrm{yr}$ record is supported by only one
third of the data on one side.

Measured omission biases:

| omitted term | rate (mm yr⁻¹) | formal 1σ | rms (mm) | bias from the full model |
|---|---|---|---|---|
| season (step-free series) | $10.3834$ | $2.6966$ | $5.9276$ | $-1.6373$ |
| season included | $12.0207$ | $1.2355$ | $2.5760$ | — |
| step ($10\ \mathrm{mm}$) omitted | $16.7561$ | $1.6209$ | $3.3796$ | $+3.4656$ |
| step included | $13.2905$ | $2.6921$ | $2.8863$ | — |

Two features are worth stating explicitly. First, the biases are **larger than the
error bars** they are measured against — $-1.64\ \mathrm{mm\,yr^{-1}}$ is $1.33$
times the correct model's own error bar ($1.2355\ \mathrm{mm\,yr^{-1}}$), and
$+3.47\ \mathrm{mm\,yr^{-1}}$ is $2.1$ times the omitted model's own error. A
systematic bias of twice your error bar is a wrong answer with a confident
uncertainty.

Second, **the residual rms does not diagnose either omission**: $2.88$ mm for the
full model against $3.38$ mm for the step-omitting model is a factor of $1.17$,
within the scatter of a 60-epoch series. The misfit is a weak detector of a
missing term when the missing term is smooth over the record.

## 5. Window dependence: a transient aliased into a rate

A decaying transient cannot be distinguished from a fast rate over a window shorter
than its decay time. The demonstration's second series is
$12.0\ \mathrm{mm\,yr^{-1}} - 15\exp(-t/0.3)\ \mathrm{mm}$ plus noise:

| window | fitted rate (mm yr⁻¹) | formal 1σ |
|---|---|---|
| epochs 0–1.0 yr | $23.0487$ | $7.8911$ |
| epochs 0.25–3.0 yr | $14.2215$ | $1.6153$ |
| epochs 1.5–3.0 yr | $14.1207$ | $4.3579$ |

The early window returns nearly **twice** the true rate, and the misfit is good:
over that window the exponential is almost linear. Windows that exclude the
transient return $14.1 \pm 1.6$ and $14.1 \pm 4.4\ \mathrm{mm\,yr^{-1}}$, both
consistent with the true 12 at their own precision, though the short late window's
error is large because it uses half the epochs.

The rule that follows: **a rate is meaningful only with its window**, and a rate
fitted over a span shorter than the timescale of the slowest process in the signal
is a property of the window, not of the site. For post-seismic, volcanic or
permafrost studies the transient's timescale must be estimated and either modelled
or excluded explicitly.

## 6. What a rate is and is not

1. **It is a line-of-sight projection.** The measurement is the component of
   displacement along the radar look vector, so the rate is $b_\text{LOS} =
   \hat{\mathbf{l}}\cdot\mathbf{v}$ with $\hat{\mathbf{l}}$ set by the incidence and
   heading angles. Recovering a horizontal velocity requires **two look
   geometries** — ascending and descending — and even then only the
   east–west and vertical components are separable; north–south motion is nearly
   invisible to Sentinel-1's near-polar orbit.
2. **It is relative.** The interferometric phase gives displacements relative to a
   **reference point**, and no network of interferograms determines the absolute
   motion; a rate is always "with respect to" something that must be stated.
3. **Its uncertainty is correlated.** Atmospheric delay and orbit error are
   spatially and temporally correlated, so the formal least-squares error
   understates the true uncertainty of a *regional* rate by a factor that is itself
   estimated from the residuals' correlation structure.
4. **It is not a trend over a longer period.** Three years of data constrain a
   three-year rate; extrapolating it is a model statement.

## 7. Assumptions and regime of validity

1. **A linear rate.** Non-linear inter-seismic deformation, a slowing landslide or
   a deflating reservoir all violate it; residual plots by epoch are the check.
2. **A pure annual sinusoid for the season.** Snow load, groundwater and
   thermoclastic effects are not exactly annual; a two-harmonic or
   data-driven seasonal basis is often needed.
3. **A single step at a known time.** An unknown step time makes the problem
   non-linear; a step time inferred from the data needs its own uncertainty.
4. **Independent, equal-variance epochs.** Neither is true for interferograms; the
   weight matrix should reflect the correlation, and a variance factor should scale
   the formal errors to the residual scatter.
5. **A stable scatterer.** Decorrelation, a change in the scattering mechanism, or
   a phase unwrapping error on one interferogram propagates into every later epoch
   of a time-series chain.

## The honest summary

The project's result is a table of omissions. On a synthetic series with a
$12.0\ \mathrm{mm\,yr^{-1}}$ rate, omitting the seasonal term moves the rate to
$10.3834\ \mathrm{mm\,yr^{-1}}$ with an error bar inflated from $1.2355$ to
$2.6966$; omitting a $10\ \mathrm{mm}$ step moves it to
$16.7561\ \mathrm{mm\,yr^{-1}}$; and fitting a decaying transient over its own
decay window returns $23.05\ \mathrm{mm\,yr^{-1}}$ against a true 12. In every case
the residual rms remains acceptable, because a smooth omission is not a misfit
signal. The transferable practice is to state the model's terms, to quote every
rate with its window, and to treat an unmodelled smooth component as the most
likely source of a wrong rate — not as noise.

## Python demonstration

[`code/insar_timeseries_demo.py`](./code/insar_timeseries_demo.py) prints every
number quoted above. It:

1. builds the series and prints its components and range;
2. fits four models and prints each rate with its uncertainty and residual rms,
   plus both omission biases;
3. fits the transient series over three windows and prints the rates, showing the
   factor-of-two inflation in the early window;
4. prints the five things the analysis does not establish.

Run it with the project virtual environment:

```bash
cd 25-projects-capstone/04-graduate-projects/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python insar_timeseries_demo.py
```

The script prints only, writes no files, uses no network and exits 0. It runs in
under a second.

## Exercises

Graded problems and worked solutions are in
[`exercises/03-insar-deformation-project-exercises.md`](./exercises/03-insar-deformation-project-exercises.md)
and
[`exercises/03-insar-deformation-project-solutions.md`](./exercises/03-insar-deformation-project-solutions.md).
The ★★★ item asks you to design a time-series model for a stated target, not to
refit the demonstration.

## Mastery checkpoint

Without notes:

1. Write the design matrix for a rate, a season and a step, and state which
   coefficient is the rate.
2. The full model recovers the step as $7.1133 \pm 4.7237\ \mathrm{mm}$ against a
   true 10.0. State two reasons the uncertainty is so large.
3. A rate is fitted over 1.5 years and reported to $\pm 0.2\
   \mathrm{mm\,yr^{-1}}$. State the two things you would ask before believing it.
4. Name the four failure modes of §7 and the test for each.

## Common pitfalls

1. **Fitting a rate without a seasonal term.** The bias here is $-1.64\
   \mathrm{mm\,yr^{-1}}$, larger than the error bar.
2. **Fitting through a coseismic jump.** The step is a parameter, and its omission
   biases the rate by $+3.47\ \mathrm{mm\,yr^{-1}}$.
3. **Quoting a rate without its window.** The window is part of the result.
4. **Reporting a line-of-sight rate as a velocity.** The look geometry is required.
5. **Treating the formal error as the uncertainty.** Atmospheric and orbital errors
   are correlated over tens of kilometres and weeks.

## Where this is used

InSAR time series feed volcanic, seismic, landslide and subsidence monitoring, and
their rates are compared against the GNSS velocities of
[25-03-05](../03-advanced-projects/05-gnss-strain-project.md) and the seismicity of
[25-04-04](./04-earthquake-catalog-analysis.md). In professional practice the
report's first page states the reference point, the look geometry and the window,
and a rate without those three is not reviewed.

## Related lessons

- [17-03-03 InSAR Time Series: PS-InSAR and SBAS](../../17-remote-sensing-gis/03-radar-remote-sensing/03-insar-time-series.md) —
  the estimation and stacking strategies this project fits into.
- [13-04-03 Postseismic Relaxation and Viscoelastic Models](../../13-geodynamics-tectonics/04-tectonophysics-deformation/03-postseismic-viscoelastic.md) —
  the physical form of the transient of §5.
- [20-08-04 Change-Point Detection and Regime Shifts](../../20-signal-processing/08-timeseries-analysis-geophysics/04-change-point-and-detection.md) —
  how to find a step time rather than assume it.
- [25-03-04 Project: Climate Data Analysis and Trend Attribution](../03-advanced-projects/04-climate-data-analysis-project.md) —
  the same trend-and-error-rate discipline on a climate series.

## Self-assessment checklist

- [ ] I can fit rate, season and step in one design matrix.
- [ ] I can measure the bias from each omitted term.
- [ ] I can show that the misfit does not flag a smooth omission.
- [ ] I can demonstrate the window dependence of a rate.
- [ ] I can state what a line-of-sight rate does and does not determine.
- [ ] I can name the four failure modes of §7.
