---
id: 16-08-01
title: "Surface, Radiosonde and Satellite Climate Records"
level: advanced
prereqs: ["16-02-01", "16-04-04", "21-01-01"]
tags: [atmosphere, climate, observations, homogeneity, satellite, radiosonde, data-products]
---

# Surface, Radiosonde and Satellite Climate Records

> **All models and data in this module are SYNTHETIC.** The stations, radiosondes
> and satellite series in `code/observation_records_demo.py` are chosen teaching
> constructions around a known synthetic truth. No real station, instrument,
> mission or published temperature record is used, and no published warming rate
> is quoted.

A climate record is not a measurement. It is a **product**: an observational time
series plus a processing chain, and the processing chain decides how much of the
trend in the product is in the climate. This lesson is about that gap. Three
observing systems are used to make the point — surface thermometers, radiosondes,
and satellite sounders — because they fail in *different* ways, and the failures
teach the same lesson: **the biases that matter are the ones that change in
time**, because only those survive as trends.

The lesson is deliberately about method rather than about places or missions. It
builds one known synthetic truth, observes it with three synthetic systems that
carry three different defects, and measures how much trend each defect
manufactures. Every spurious trend in the lesson is printed by the demonstration.

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** a climate data record as a product and **distinguish** a
   fundamental observation, a thematic product and a climate data record.
2. **Explain** why a time-constant bias cancels in anomalies while a
   time-varying bias does not, and **measure** the trend it produces.
3. **Quantify** the trend error introduced by an uncorrected instrument step and
   by a slow siting drift, and **state** what an inhomogeneity is.
4. **Explain** how changes in network composition manufacture a trend and how an
   anomaly-based index removes the leading part of it.
5. **Explain** the satellite diurnal-drift problem and **measure** the spurious
   trend an uncorrected drift produces.
6. **Distinguish** random from structural uncertainty and **state** why the latter
   does not shrink as $1/\sqrt{n}$.
7. **Write** the processing-chain statement a defensible climate record needs.

## Prerequisites

- [16-02-01 Solar and Terrestrial Radiation, Blackbody Laws](../02-radiation-and-energy-balance/01-solar-and-terrestrial-radiation.md) —
  the radiances satellite sounders invert.
- [16-04-04 Natural Variability: ENSO, NAO, PDO, Solar and Volcanic](../04-climate-system-and-feedbacks/04-natural-variability.md) —
  the variability a record is trying to resolve.
- [21-01-01 Descriptive Statistics, Robust Measures and Outliers](../../21-statistics-bayesian-ml/01-statistics-in-practice/01-descriptive-statistics.md) —
  trends and their standard errors.

## 1. Observations, products and the processing chain

The World Meteorological Organization's data-system vocabulary distinguishes three
levels, and the distinction is the subject of this lesson:

- a **fundamental observation** — the raw instrument reading with its calibration
  and metadata (a thermometer voltage, a radiance, a radiosonde report);
- a **thematic product** — derived for a purpose (a daily mean, a gridded field, a
  reanalysis);
- a **climate data record** — a series intended for long-term change detection,
  with documented processing, homogenisation and a quantified uncertainty.

The last level is where climate trends live. Nothing about a fundamental
observation lets you compute a 50-year trend; that computation happens in the
product. Two consequences:

1. **A product cannot be more certain than its processing.** If the adjustment for
   an instrument change is wrong by $0.1\ \mathrm{K}$, that error enters the trend
   directly.
2. **A product's uncertainty is not only statistical.** Part of it is
   *structural*: it comes from choices (which stations, which adjustment method,
   which reference series) and it does not shrink as $1/\sqrt{n}$, because adding
   more stations that share the same unadjusted bias does not remove the bias.

## 2. Why a constant bias cancels and a changing bias does not

Let a station measure truth $T(t)$ with an additive bias $b(t)$:
$y(t) = T(t) + b(t)$. Form anomalies relative to a reference period when the bias
is $b_{\text{ref}}$:

$$y'(t) = y(t) - \overline{y} = T'(t) + \left[b(t) - b_{\text{ref}}\right].$$

If $b$ is **constant**, $b(t) - b_{\text{ref}} = 0$ and the anomaly is unbiased —
which is why absolute accuracy matters less than stability for trend work. If $b$
**changes**, the change enters the anomaly and, if it is gradual or stepped, it
appears as a trend. A change in $b$ that is unrelated to climate is called an
**inhomogeneity**, and removing it is **homogenisation**
([16-08-03](03-climate-data-homogenisation.md)).

The demonstration's three synthetic stations are designed to isolate this:

| Station | defect (chosen) | fitted trend (K/yr) | true (K/yr) |
|---|---|---|---|
| A | step of $+0.40\ \mathrm{K}$ at year 40 (instrument change) | $+0.0191 \pm 0.0006$ | $+0.0150$ |
| B | linear siting drift $+0.002\ \mathrm{K\,yr^{-1}}$ | $+0.0165 \pm 0.0005$ | $+0.0150$ |
| C | none, but only available before year 60 | $+0.0147 \pm 0.0005$ | $+0.0150$ |

Station C recovers the trend because its only error is random; A is high by
$27\%$ and B by $10\%$, and both are *within* small formal standard errors of
their own biased values. **The standard error measures the noise, not the bias**,
which is the single most important sentence in this lesson.

## 3. Averaging does not fix a changing bias

The naive mean of the three raw records gives $+0.0168 \pm 0.0005\
\mathrm{K\,yr^{-1}}$ against a true $+0.0150$, a trend error of
$+0.0018\ \mathrm{K\,yr^{-1}}$ ($+12\%$). After the step and drift adjustments,
the mean gives $+0.0146 \pm 0.0005\ \mathrm{K\,yr^{-1}}$, a residual error of
$-0.0004\ \mathrm{K\,yr^{-1}}$.

The arithmetic is a warning about what averaging does. Random errors average down
as $1/\sqrt{n}$; **systematic errors average up, or not at all**, because the
average of $n$ copies of the same bias is the same bias. In a network where
instruments were changed in a particular decade, the bias is shared, and no
amount of additional stations in that decade removes it.

## 4. Network composition: the bias that lives in the index

A climate index is an average over a *changing set* of observations. If the set
changes in a way correlated with the quantity being averaged — stations drop out
in cold regions, new stations appear in warm ones, ocean routes shift — the index
acquires a trend that is not in the climate.

The demonstration builds such a case: reliable sites contribute before year 60,
and after year 60 they are replaced by sites with a chosen $+0.8\ \mathrm{K}$ mean
offset. The composite fits a trend of $+0.0246 \pm 0.0007\ \mathrm{K\,yr^{-1}}$
against the true $+0.0150$ — an inflation of $+0.0096\ \mathrm{K\,yr^{-1}}$, more
than half the true signal. The $+0.8\ \mathrm{K}$ discontinuity is larger than the
entire true change over the record ($120 \times 0.015 = 1.8\ \mathrm{K}$ — the
same order).

Two defences are standard. Working in **anomalies** rather than absolutes removes
the time-constant part of any site's offset. And **reducing the index to a common
network** — computing the anomaly of each site relative to its own climatology and
then averaging, or using a pairwise difference network — makes the index
insensitive to which sites are present, to the extent that the sites' anomaly
series are interchangeable. Neither defence is perfect: an offset that changes
*within* a site's record cannot be removed by anomaly formation.

## 5. Radiosondes: a vertical record with a changing heritage

Radiosondes add a dimension and a class of problems. A sonde drifts with the wind
as it ascends, so the reported profile is a slanted sample, not a column; the
radiation correction for the temperature sensor depends on daylight and on the
solar angle, which introduces a **day–night difference**; sensor types, balloon
burst heights and ground-station processing have all changed over the decades; and
the number of stations and their launch times is not constant. Each of these is a
potential inhomogeneity in a time series of, say, mid-tropospheric temperature.

The consequence for practice is that radiosonde-based records are constructed from
*differences between neighbouring stations and between launch times* rather than
from raw reports, precisely because the shared errors cancel in a difference while
the climate signal does not.

## 6. Satellites: a changing observing geometry

Satellite sounders infer layer temperatures from radiances, and their problems are
geometric rather than instrumental in the ordinary sense:

- **Orbit and local observation time.** A sun-synchronous satellite crosses the
  equator at an approximately fixed local time, but that time **drifts** as the
  orbit precesses. Because the diurnal cycle has a large amplitude, an
  uncorrected drift mixes a diurnal signal into the climate record.
- **Inter-satellite calibration.** A long record is a concatenation of
  overlapping satellites; offsets between them must be removed, and the removal
  method affects the trend.
- **Layer weighting.** A radiance is a weighted average over an altitude range;
  the *derived* temperature is a retrieval, with its own error, and a shift in
  the weighting function is not a temperature change.

The demonstration measures the first of these with an exaggerated drift. With a
synthetic diurnal amplitude of $1.5\ \mathrm{K}$ and $6.0$ hours of local-time
drift over $120$ years, the uncorrected series fits $+0.0057 \pm 0.0006\
\mathrm{K\,yr^{-1}}$ against the true $+0.0150$; the drift has removed
$-0.0093\ \mathrm{K\,yr^{-1}}$, or $62\%$ of the signal. Removing the known
diurnal term exactly restores $+0.0148 \pm 0.0005\ \mathrm{K\,yr^{-1}}$. *A few
hours of uncorrected drift is enough to halve a multi-decade trend* — the drift
here is exaggerated relative to a real mission, but the mechanism and the
sensitivity are real.

## 7. Combining records, and what the combination adds

Different systems sample different things (surface air temperature, layer
temperature, sea-surface temperature), so combining them is not averaging
commensurate numbers. What combination adds is **different structural errors**: a
trend that survives independently-processed surface, radiosonde and satellite
records is more credible than one from any single product, because it is harder
for three unrelated processing chains to manufacture the same artefact. What it
does *not* add is a rigorous uncertainty: combining series with shared climate
signals and different biases requires a careful error model, and simply averaging
the three trends and quoting the scatter understates the uncertainty.

## 8. Worked example — reading a trend table

Suppose a product reports the trend over a 120-year record with a formal standard
error of $0.0005\ \mathrm{K\,yr^{-1}}$ but an adjustment-related uncertainty of
$\pm 0.1\ \mathrm{K}$ in a step applied at year 60. A step enters the fitted trend
exactly through the ordinary-least-squares slope,

$$\delta(\text{trend}) = \delta_{\text{step}}\,
\frac{\sum_{t \ge t_0}\left(t-\bar t\right)}{\sum_t \left(t-\bar t\right)^{2}}.$$

For years $t = 0,\dots,119$, $\bar t = 59.5$ and
$\sum_t (t-\bar t)^{2} = 143{,}990$. A step beginning at $t_0 = 60$ gives
$\sum_{t\ge60}(t-\bar t) = 60 \times (89.5-59.5) = 1800$, so the lever factor is
$1800/143{,}990 = 0.01250\ \mathrm{yr^{-1}}$ and

$$\delta(\text{trend}) = 0.1 \times 0.01250 = 0.00125\ \mathrm{K\,yr^{-1}},$$

**$2.5$ times the formal standard error.** A step at the record *centre* has the
largest lever factor (the extreme values $t_0=0$ and $t_0=L$ give zero and
$0.0111\ \mathrm{yr^{-1}}$ respectively for $L=120$), so the adjustment
uncertainty is worst exactly where a mid-record instrument change actually occurs.

This is the lesson's central arithmetic: for long trends, the uncertainty is
dominated by what you did to the data, not by how much data you had. The
demonstration makes the same point with a step of $0.40\ \mathrm{K}$ at year 40,
which shifts the fitted slope by
$0.40 \times 1600/143{,}990 = +0.0044\ \mathrm{K\,yr^{-1}}$ — most of the
$+0.0045$ discrepancy between station A and the truth.

## 9. Assumptions and regime of validity

1. **The anomaly reference period does not overlap with a large bias change.**
   Choosing a reference window that contains the step corrupts every anomaly.
2. **Adjustments are unbiased.** The demonstration adjusts by the *known* bias; a
   real chain must *estimate* it, and estimation error enters the trend.
3. **The known-truth construction used here is a teaching device.** Real
   observational uncertainty has no ground truth to compare against, so it must be
   estimated by comparing independent products and by propagating the adjustment
   uncertainty.
4. **Spatial representativeness.** A point observation is being used for a grid
   box; the gap between them is a source of error that varies with station density
   and terrain.
5. **The trend model is linear.** A linear fit will distribute a step over the
   whole record; a non-linear or changepoint model gives a different answer.

## 10. Python demonstration

[`code/observation_records_demo.py`](code/observation_records_demo.py) builds the
synthetic truth and the three observing systems and prints labelled results with
units. It:

1. constructs a known truth with a stated trend and three defective synthetic
   stations;
2. fits trends to each station, to the naive mean, and to the adjusted mean;
3. measures the trend manufactured by a change in network composition;
4. measures the spurious trend from an uncorrected satellite-style diurnal drift;
5. prints the processing-chain statement a defensible product needs.

Every number in this lesson is printed by that demonstration.

## Mastery checkpoint

> The demonstration's synthetic truth has a trend of
> $+0.0150\ \mathrm{K\,yr^{-1}}$ over 120 years. Station A carries a
> $+0.40\ \mathrm{K}$ step at year 40; the naive mean of the raw stations fits
> $+0.0168 \pm 0.0005\ \mathrm{K\,yr^{-1}}$.
>
> **(a)** Explain why station C, which has no bias, still differs from the truth
> by $0.0003\ \mathrm{K\,yr^{-1}}$.
> **(b)** Compute the trend error of the naive mean and express it as a percentage
> of the true trend.
> **(c)** A colleague argues that more stations would reduce the error. Explain
> why that is wrong for a shared instrument change.
> **(d)** The network-composition experiment gives $+0.0246\
> \mathrm{K\,yr^{-1}}$. State the mechanism and one standard defence.
> **(e)** An adjustment step has an uncertainty of $\pm 0.1\ \mathrm{K}$ and is
> applied at year 60 of a 120-year record. Using
> $\sum_t (t-\bar t)^2 = 143{,}990$ and $\sum_{t\ge60}(t-\bar t) = 1800$, estimate
> the trend error it contributes and compare it with a formal standard error of
> $0.0005\ \mathrm{K\,yr^{-1}}$.

## Common pitfalls

1. **Reading a small standard error as small uncertainty.** The formal error
   measures noise, not bias; it cannot see an unadjusted step.
2. **Assuming more stations means less error.** Shared systematic errors do not
   average down.
3. **Comparing absolute temperatures across a changing network.** Use anomalies
   and a common network.
4. **Treating a retrieval as a measurement.** A satellite layer temperature is a
   derived quantity with a weighting function and an error model.
5. **Ignoring viewing geometry.** An uncorrected local-time drift removed $62\%$
   of the synthetic trend.
6. **Averaging trends from different systems as if commensurate.** Their errors
   are structural and partly shared.
7. **Choosing the anomaly reference period carelessly.** A reference window
   containing a bias change corrupts the whole series.

## Related modules

- [16-08-02 Reanalysis: ERA5, MERRA, JRA and Their Caveats](02-reanalysis-products.md) —
  what happens when observations are combined with a model, rather than with each
  other.
- [16-08-03 Homogenisation, Bias Adjustment and Uncertainty](03-climate-data-homogenisation.md) —
  the detection and removal of the inhomogeneities introduced here.
- [16-08-04 Analysing Climate Data in Python: xarray and CDO](04-climate-data-analysis-python.md) —
  the practical handling of the products this lesson describes.
- [16-04-04 Natural Variability: ENSO, NAO, PDO, Solar and Volcanic](../04-climate-system-and-feedbacks/04-natural-variability.md) —
  the signal a record must resolve before a trend means anything.
- [17-01 The Electromagnetic Spectrum and Sensing Windows](../../17-remote-sensing-gis/01-remote-sensing-physics/01-em-spectrum-remote-sensing.md) —
  the radiative-transfer background behind satellite sounding.

## Self-assessment checklist

- [ ] I can define a climate data record and say what makes it different from an
      observation.
- [ ] I can explain why a time-constant bias cancels in anomalies.
- [ ] I can estimate the trend error from a step adjustment and its lever arm.
- [ ] I can explain network-composition bias and one defence against it.
- [ ] I can explain the satellite diurnal-drift problem quantitatively.
- [ ] I can distinguish random from structural uncertainty.
