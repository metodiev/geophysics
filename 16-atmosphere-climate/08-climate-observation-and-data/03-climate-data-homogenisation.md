---
id: 16-08-03
title: "Homogenisation, Bias Adjustment and Uncertainty"
level: research
prereqs: ["16-08-01", "21-01-03", "21-01-01"]
tags: [atmosphere, climate, homogenisation, bias-adjustment, breakpoint, uncertainty, data-products]
---

# Homogenisation, Bias Adjustment and Uncertainty

> **All models and data in this module are SYNTHETIC.** The stations, the step
> change, the reference series and the model/observation pairs in
> `code/homogenisation_demo.py` are chosen teaching constructions. No real
> station, network, dataset or published adjustment is used, and no published
> number is quoted.

Two different operations are called "correcting the data", and confusing them is
one of the commonest errors in applied climate work. **Homogenisation** removes
*artificial* changes from an observational record — the fingerprints of instrument
changes, station moves and siting — and it is legitimate precisely because the
artefact is not climate. **Bias adjustment** adapts a *model's* output to an
observed distribution, and it is not a data correction at all: it is a mapping
between two statistical descriptions, and the mapping chosen decides whether a
climate change signal survives.

This lesson treats both, quantitatively. The homogenisation half measures how
large a step is detectable, what a false alarm costs, and what residual trend
error remains after a perfect detection. The bias-adjustment half shows two
procedures that are both called quantile mapping and that differ by $1.90\
\mathrm{K}$ in the change they report. The unifying idea is that **every adjustment
is a transfer function, and the transfer function is a modelling choice that must
be stated and tested.**

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** an inhomogeneity, and **distinguish** a metadata-based from a
   statistical detection of a breakpoint.
2. **Construct** a neighbour-difference series and **detect** a breakpoint with a
   split-mean $t$-statistic scan.
3. **Explain** the multiplicity problem in a scan and **quantify** the
   false-positive rate of a stated threshold.
4. **Measure** how much a step biases a trend, and **measure** the residual trend
   error after adjustment.
5. **Derive** the trend error contributed by a break-year or step-size error.
6. **Distinguish** delta-change and quantile-mapping bias adjustment, and
   **demonstrate** a mapping that removes a climate change signal.
7. **State** the homogenisation and adjustment uncertainty a defensible product
   must report.

## Prerequisites

- [16-08-01 Surface, Radiosonde and Satellite Climate Records](01-surface-and-satellite-records.md) —
  where inhomogeneities come from and why they matter.
- [21-01-03 Resampling: Bootstrap, Jackknife, Permutation Tests](../../21-statistics-bayesian-ml/01-statistics-in-practice/03-resampling.md) —
  the resampling machinery used to calibrate a detection rule.
- [21-01-01 Descriptive Statistics, Robust Measures and Outliers](../../21-statistics-bayesian-ml/01-statistics-in-practice/01-descriptive-statistics.md) —
  trends and their standard errors.

## 1. What an inhomogeneity is, and two ways to find it

Write a station's anomaly as $\varepsilon(t) = \text{climate}(t) + b(t) + n(t)$,
with $b$ a non-climatic bias and $n$ random error. An **inhomogeneity** is a
change in $b$: a step at an instrument change, a ramp from gradual urbanisation, a
change in observation time. Only the *change* in $b$ matters for a trend
([16-08-01 §2](01-surface-and-satellite-records.md)), so detection is about
changes.

There are two independent routes:

- **Metadata.** Station histories record moves, instrument changes, screen
  changes and observation-time changes. Metadata tells you *when to look*; it
  rarely gives the size of the change, and it is often incomplete.
- **Statistical detection.** Compare the candidate station with one or more
  neighbours that should share the climate signal. Under the null of a homogeneous
  candidate, the difference has no break.

The two are complementary, and a defensible product uses both: metadata to
generate candidate dates, statistics to estimate and confirm.

## 2. The neighbour-difference test

Let $C(t)$ be the candidate and $R(t)$ a reference formed from neighbours, with
the station's annual anomalies both expressed relative to a common reference
period. Define

$$D(t) = C(t) - R(t).$$

The regional climate signal cancels between the two (to the extent that the
stations sample the same climate), so under a homogeneous candidate $D$ is
zero-mean noise. A step in $b_C$ at year $t_0$ appears as a step in $D$. For a
candidate break year $t_0$ the test statistic is the split-mean $t$-statistic

$$T(t_0) = \frac{\overline{D}_{t\ge t_0} - \overline{D}_{t< t_0}}
{\sqrt{s^{2}_{t\ge t_0}/n_{\ge} + s^{2}_{t<t_0}/n_{<}}},$$

and the detected break is $\hat t_0 = \arg\max_{t_0}|T(t_0)|$. The estimated
adjustment is the mean jump, $\hat b = \overline{D}_{t\ge \hat t_0} -
\overline{D}_{t<\hat t_0}$, applied to the later segment.

**The multiplicity trap.** The scan evaluates $T$ at every candidate year, so the
nominal threshold is not the realised false-positive rate. In the demonstration
the scan covers about $70$ candidate years, and an unadjusted $|T| > 3$ rule fires
on $0.120$ of realisations that contain **no break at all** — twelve times the
nominal rate of a single test. A calibrated rule must control this multiplicity
(for example by a penalty on the number of candidates, by a permutation null
distribution of the maximum statistic, or by a Bayesian changepoint posterior).

## 3. Worked example — detection, adjustment and the trend

The demonstration builds a synthetic truth with trend $0.020\ \mathrm{K\,yr^{-1}}$
and AR(1) anomaly noise of standard deviation $0.50\ \mathrm{K}$ with
$\varphi = 0.40$; two stations add independent noise of $0.20\ \mathrm{K}$; the
candidate carries a step of $0.50\ \mathrm{K}$ from year 40.

*Before adjustment.* The candidate fits $+0.0250\ \mathrm{K\,yr^{-1}}$ against
the truth's $+0.0171\ \mathrm{K\,yr^{-1}}$ — a trend error of
$+0.0079\ \mathrm{K\,yr^{-1}}$. The step's contribution can be computed exactly
from the same leverage algebra as
[16-08-01 §8](01-surface-and-satellite-records.md): for $L = 80$ years,
$\sum_t(t-\bar t)^2 = 42{,}660$ and
$\sum_{t\ge40}(t-\bar t) = 800$, so

$$\delta(\text{trend}) = 0.50 \times \frac{800}{42{,}660}
= 0.0094\ \mathrm{K\,yr^{-1}},$$

which is the Monte Carlo mean unadjusted error in Section 4 (the fitted pair
differ by $0.0079$ only because this single realisation's truth has a
noise-shifted slope). A $0.5\ \mathrm{K}$ step produces nearly
$0.01\ \mathrm{K\,yr^{-1}}$ of spurious trend — half the true trend, from a single
instrument change.

*Detection.* The scan finds $\hat t_0 = 40$ exactly, with $|T| = 7.95$, and
estimates the adjustment as $+0.456\ \mathrm{K}$ against the true $0.50\
\mathrm{K}$ (the estimate is noisy, not biased in expectation). After adjustment
the trend is $+0.0165\ \mathrm{K\,yr^{-1}}$, a residual error of
$-0.0006\ \mathrm{K\,yr^{-1}}$ against the truth.

*Detection limits.* Repeating with different step sizes, requiring $|T|>3$ **and**
a break-year error within $\pm 3$ years:

| step (K) | detection rate | mean $\lvert T\rvert$ |
|---|---|---|
| 0.10 | 0.050 | 2.65 |
| 0.20 | 0.307 | 3.72 |
| 0.30 | 0.650 | 5.15 |
| 0.50 | 0.917 | 8.03 |
| 0.80 | 1.000 | 12.92 |
| 1.20 | 1.000 | 19.13 |

A step of $0.1\ \mathrm{K}$ — smaller than the station noise — is essentially
undetectable, and even a $0.2\ \mathrm{K}$ step is found less than a third of the
time. **Undetected inhomogeneities are the ones that matter**, because they are
not adjusted and they enter the network mean with their full trend bias.

## 4. The residual uncertainty after a correct adjustment

Over $300$ realisations with a $0.50\ \mathrm{K}$ step at year 40, the trend error
is:

| | mean | sd |
|---|---|---|
| unadjusted | $+0.0094\ \mathrm{K\,yr^{-1}}$ | $0.0010\ \mathrm{K\,yr^{-1}}$ |
| adjusted | $+0.0000\ \mathrm{K\,yr^{-1}}$ | $0.0012\ \mathrm{K\,yr^{-1}}$ |

The adjustment removes the systematic part exactly, and leaves a residual of
standard deviation $0.0012\ \mathrm{K\,yr^{-1}}$ — about $6\%$ of the true trend —
because the break year and the step size are estimated, not known. **That residual
is the homogenisation uncertainty**, and it is of the same order as the sampling
error of the trend itself. Reporting a homogenised station trend without it
understates the uncertainty by roughly a factor of two.

## 5. Bias adjustment: a map, not a correction

Bias adjustment has a different logic. A climate model has its own climatology
with its own errors; to use its output in an impact model calibrated on
observations, the output is mapped to the observed distribution. Two standard
procedures:

- **Delta change.** Take the model's simulated *change* and add it to the observed
  series. The observed variability is preserved and the change is the model's.
- **Quantile mapping.** Build the transfer function
  $T(x) = F_{\text{obs}}^{-1}\!\left(F_{\text{model},\text{hist}}(x)\right)$ from
  the historical model–observation pair, then apply $T$ to the model's future
  values. This corrects the distribution, not just the mean.

Quantile mapping is the more informative method and the more dangerous one,
because the same name covers transfer functions built from different pairs.

## 6. Worked example — two quantile mappings, one trend

The demonstration uses synthetic model and observation samples: model historical
mean $10.04\ \mathrm{K}$, model future mean $11.95\ \mathrm{K}$ (a change of
$+1.91\ \mathrm{K}$), observed historical mean $11.00\ \mathrm{K}$, all with
standard deviation $2.0\ \mathrm{K}$.

- **Method A (correct).** Build the transfer function from the *historical*
  model–observation pair and apply it to the future model:
  $$T(x) = F_{\text{obs,hist}}^{-1}\!\left(F_{\text{model,hist}}(x)\right).$$
  The corrected future mean is $12.89\ \mathrm{K}$, a change of $+1.89\
  \mathrm{K}$ against the historical observed $11.00\ \mathrm{K}$. The model's
  climate change signal survives (the $0.02\ \mathrm{K}$ difference from $+1.91$
  is empirical-quantile discretisation).
- **Method B (wrong).** Map the future model directly onto the historical observed
  distribution, $T'(x) = F_{\text{obs,hist}}^{-1}\!\left(F_{\text{model,fut}}(x)\right)$.
  The corrected future mean is $10.99\ \mathrm{K}$, a change of $-0.01\
  \mathrm{K}$. **The climate change signal has been removed by construction**,
  because the future distribution has been mapped onto the historical one.

Both procedures are routinely described as "bias-corrected". They differ by
$1.90\ \mathrm{K}$ in the change they report. The lesson generalises: a bias
adjustment inherits whatever assumption its transfer function encodes, and a
transfer function fitted on the future period has already absorbed the signal you
are trying to report. When a period-by-period adjustment is unavoidable,
trend-preserving variants exist, but they trade the trend assumption for a
distributional assumption and must be tested against the unadjusted signal.

## 7. Assumptions and regime of validity

1. **The reference series is itself homogeneous.** If the neighbours share the
   candidate's break (a network-wide instrument change), the difference has no
   step and the detection fails.
2. **The candidate and the reference share the same climate signal.** Stations far
   apart in different climate regimes do not; the difference then contains real
   spatial variability that can be mistaken for a break.
3. **The network is dense enough.** Homogenisation needs neighbours; a sparse
   region cannot be homogenised statistically, and its trends carry an unquantified
   uncertainty.
4. **Detection and adjustment are separate steps.** A detection does not
   automatically give the right adjustment size, and the estimated jump inherits
   the reference's own noise.
5. **Bias adjustment does not create information.** It cannot recover a change
   that the model does not simulate; it can only map the model's statistics onto
   the observations'.
6. **Quantile mapping assumes the transfer function is stationary** unless a
   non-stationary variant is chosen deliberately and its assumption stated.
7. **Multiple breaks and gradual changes.** A ramp (urbanisation) is not a step;
   detecting it requires a different model, and a single-break method will place a
   spurious breakpoint in the middle of the ramp.

## 8. Python demonstration

[`code/homogenisation_demo.py`](code/homogenisation_demo.py) builds the synthetic
network and runs the whole analysis, printing labelled results with units. It:

1. constructs the truth, a reference station and a candidate with a step;
2. detects the breakpoint by a split-mean $t$-statistic scan and applies the
   adjustment;
3. measures detection rate versus step size and the false-positive rate of the
   rule;
4. measures the trend error before and after adjustment over $300$ realisations;
5. contrasts two quantile-mapping procedures that differ in the trend they
   report;
6. prints the statement a homogenisation report must contain.

Every number in this lesson is printed by that demonstration (except the
step-leverage arithmetic, which uses the exact sums given in Section 3).

## Mastery checkpoint

> The demonstration's synthetic candidate has a $0.50\ \mathrm{K}$ step at year 40
> of an 80-year record; the scan finds the break at year 40 with $|T| = 7.95$.
>
> **(a)** Compute the step's contribution to the fitted trend using
> $\sum_t(t-\bar t)^2 = 42{,}660$ and $\sum_{t\ge40}(t-\bar t) = 800$, and compare
> it with the Monte Carlo mean unadjusted error $+0.0094\ \mathrm{K\,yr^{-1}}$.
> **(b)** Explain why the unadjusted trend error of a *single* realisation
> ($+0.0079$) differs slightly from the expected value.
> **(c)** After a perfect detection and adjustment the residual trend error has sd
> $0.0012\ \mathrm{K\,yr^{-1}}$ against a true trend of $0.020\ \mathrm{K\,yr^{-1}}$.
> State what sets that residual.
> **(d)** The scan's nominal $|T|>3$ rule fires on $0.120$ of no-break
> realisations. Explain why, and name one way to calibrate the rule.
> **(e)** Two quantile-mapping procedures report changes of $+1.89\
> \mathrm{K}$ and $-0.01\ \mathrm{K}$ for the same model output. State which is
> correct and why, in terms of the transfer function's construction.

## Common pitfalls

1. **Calling a bias adjustment a data correction.** Quantile mapping maps a model's
   distribution onto an observed one; it is not homogenisation.
2. **Fitting the transfer function on the future period.** That absorbs the signal
   and reports a change of zero (Method B).
3. **Ignoring multiplicity in a breakpoint scan.** The scan's nominal threshold
   had a $0.120$ false-positive rate.
4. **Assuming the reference is homogeneous.** A shared break is invisible in a
   difference.
5. **Reporting a homogenised trend without the adjustment uncertainty.** The
   residual sd was $0.0012\ \mathrm{K\,yr^{-1}}$, comparable to the trend's own
   sampling error.
6. **Treating an undetected step as absent.** A $0.1\ \mathrm{K}$ step was detected
   in $5\%$ of realisations and biases the trend when missed.
7. **Using a single-break method on a gradual change.** The fitted breakpoint lands
   mid-ramp and the adjustment is wrong in both periods.

## Related modules

- [16-08-01 Surface, Radiosonde and Satellite Climate Records](01-surface-and-satellite-records.md) —
  the inhomogeneities this lesson detects and removes.
- [16-08-02 Reanalysis: ERA5, MERRA, JRA and Their Caveats](02-reanalysis-products.md) —
  the products that contain the same changes but are not adjusted for them.
- [16-08-04 Analysing Climate Data in Python: xarray and CDO](04-climate-data-analysis-python.md) —
  the practical handling of adjusted and unadjusted products.
- [16-05-04 Downscaling: Statistical and Dynamical](../05-climate-models/04-downscaling.md) —
  the main consumer of bias-adjusted model output.
- [21-01-03 Resampling: Bootstrap, Jackknife, Permutation Tests](../../21-statistics-bayesian-ml/01-statistics-in-practice/03-resampling.md) —
  how to build a calibrated null for a scan.
- [21-01-02 Choosing Probability Models for Earth Data](../../21-statistics-bayesian-ml/01-statistics-in-practice/02-probability-models-earth.md) —
  the distributional assumptions behind quantile mapping.

## Self-assessment checklist

- [ ] I can define an inhomogeneity and distinguish metadata from statistical
      detection.
- [ ] I can construct a neighbour difference and run a split-mean $t$ scan.
- [ ] I can compute the trend error a step produces from its leverage.
- [ ] I can quantify and control the multiplicity of a scan.
- [ ] I can distinguish delta change from quantile mapping.
- [ ] I can explain why one quantile mapping removes the climate signal.
- [ ] I can state the uncertainty a homogenisation report must carry.
