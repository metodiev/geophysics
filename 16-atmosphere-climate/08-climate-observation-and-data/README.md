# Module 16-08 — Climate Observations and Data Products

**Stages:** advanced → research · **Prerequisites:** modules 16-02 and 16-04;
the gridded-data handling of module 03-08.

This module is about the evidence. Every statement in folders 16 and 17 rests on
a time series, and every time series is a **product**: an observational record plus
a processing chain. The chain decides how much of the variation in the product is
in the climate. A thermometer changes, a station moves, a satellite's orbit
precesses, a network thins out over mountains and oceans, a reanalysis fills the
gaps with a model — and each of these leaves a signature that is indistinguishable
from a trend once a trend model is imposed on it. This module makes that
signature quantitative and then teaches the handling discipline that keeps it out
of the analysis.

The organising question is the one the whole folder keeps returning to: **what
does this number actually constrain, and what did the processing put there?** A
station series is a set of raw reports plus a homogenisation, and its trend is
conditional on the adjustments. A reanalysis is a model constrained by
observations, and in a data-sparse decade it reports the model. A bias-adjusted
projection is a transfer function applied to model output, and the choice of
transfer function decides whether a trend survives. A gridded field's global mean
is an area-weighted integral, and an unweighted mean of the same array is a
different quantity. None of these is a nuisance to be patched; each is the
physics of the measurement.

The module is deliberately practical, and it measures its own errors rather than
asserting them. The lessons show an unadjusted station change manufacturing
$+0.0018\ \mathrm{K\,yr^{-1}}$ of spurious trend, a change in network composition
manufacturing $+0.0096\ \mathrm{K\,yr^{-1}}$, an uncorrected satellite local-time
drift removing $62\%$ of a trend, an observing-system change producing a
$+0.0062\ \mathrm{K\,yr^{-1}}$ artefact in a toy reanalysis where the truth has no
trend, two quantile-mapping procedures that differ by $1.90\ \mathrm{K}$ in the
change they report, and an unweighted global mean that is $5.06\ \mathrm{K}$ from
the area-weighted one. Every one of those numbers is printed by the demonstration
in this module's `code/` directory.

**All models and data in this module are SYNTHETIC.** The stations, radiosondes,
satellite series, assimilation system, step changes and gridded fields are chosen
teaching constructions around a known synthetic truth. No real station, network,
reanalysis product, mission, instrument or published record is used, and no
published trend, adjustment or anomaly is quoted.

## Learning objectives

By the end of this module you will be able to:

1. **Define** a climate data record as a product, and **distinguish** a fundamental
   observation, a thematic product and a climate data record.
2. **Explain** why a time-constant bias cancels in anomalies while a time-varying
   bias does not, and **compute** the trend an instrument step or siting drift
   produces from the exact ordinary-least-squares leverage.
3. **Quantify** the trend manufactured by a change in network composition, and
   **state** why an anomaly-based index removes only part of it.
4. **Explain** the satellite diurnal-drift problem and **measure** the spurious
   trend an uncorrected drift produces.
5. **Describe** a reanalysis as a model constrained by observations, **derive** the
   analysis update, and **demonstrate** that in the model-dominated limit the
   product reports the model's climate.
6. **Compute** the trend a level discontinuity produces in a fitted slope, and
   **state** why a reanalysis is not homogenised for climate trends.
7. **Distinguish** a product's internal spread from its error against reality, and
   **name** the component of the error the spread omits.
8. **Construct** a neighbour-difference series, **detect** a breakpoint with a
   split-mean $t$-statistic scan, and **quantify** the scan's false-positive rate.
9. **Measure** the residual trend error after a correct adjustment, and **state**
   it as the homogenisation uncertainty.
10. **Distinguish** delta-change from quantile-mapping bias adjustment, and
    **demonstrate** a mapping that removes a climate change signal.
11. **Derive** the $\cos(\mathrm{lat})$ area weight, and **compute** area-weighted
    means, climatologies, anomalies and conservative regriddings correctly.
12. **Handle** resampling labels, partial bins, rolling windows and data gaps
    without introducing artefacts, and **map** the common `CDO` operators onto
    their `xarray` equivalents.

## Prerequisites

- [16-02 Radiation and Energy Balance](../02-radiation-and-energy-balance/README.md) —
  the radiances satellite sounders invert.
- [16-04 The Climate System and Feedbacks](../04-climate-system-and-feedbacks/README.md) —
  the variability a record has to resolve before a trend means anything.
- [03-08 xarray, netCDF and Gridded Earth Data](../../03-scientific-computing/08-gridded-geospatial-data/README.md) —
  the labelled-array and file-format practice the last lesson assumes.
- [21-01 Statistics in Practice](../../21-statistics-bayesian-ml/01-statistics-in-practice/README.md) —
  trends, resampling and the calibration of a detection rule.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Surface, Radiosonde and Satellite Climate Records](01-surface-and-satellite-records.md) | advanced | A record is a product; only biases that change in time survive as trends, and the standard error cannot see them |
| 02 | [Reanalysis: ERA5, MERRA, JRA and Their Caveats](02-reanalysis-products.md) | doctoral | A reanalysis is a model constrained by observations; where data are sparse it reports the model, and a change in observing density manufactures a trend |
| 03 | [Homogenisation, Bias Adjustment and Uncertainty](03-climate-data-homogenisation.md) | research | Homogenisation removes an artefact; bias adjustment maps a distribution, and the transfer function decides whether a climate signal survives |
| 04 | [Analysing Climate Data in Python: xarray and CDO](04-climate-data-analysis-python.md) | graduate | Every error here is a mistake about labels: weights, reference periods, bin edges, gaps and regridding |

## Suggested path

**If you are new to observational climate data:** lessons 01 and 04 first — the
failure modes and the handling discipline — then 02 and 03. Lesson 01 is where
the artefacts appear; lesson 04 is where most of them are either avoided or
introduced in practice.

**If you already work with gridded products:** read 01 §2–4 (why changing biases
matter), then 02 §4–5 (the observing-system discontinuity and the spread-versus-
error distinction), then 03 in full.

**If you are preparing a research project or a data paper:** 03 §2–4 (detection
limits and the multiplicity of a scan), 03 §5–6 (the two quantile mappings),
04 §2–6 (weights, labels, gaps, conservative regridding), plus the ★★★ exercises.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-surface-and-satellite-records.md`](01-surface-and-satellite-records.md) | Lesson 01 — demo [`code/observation_records_demo.py`](code/observation_records_demo.py) |
| [`02-reanalysis-products.md`](02-reanalysis-products.md) | Lesson 02 — demo [`code/reanalysis_demo.py`](code/reanalysis_demo.py) |
| [`03-climate-data-homogenisation.md`](03-climate-data-homogenisation.md) | Lesson 03 — demo [`code/homogenisation_demo.py`](code/homogenisation_demo.py) |
| [`04-climate-data-analysis-python.md`](04-climate-data-analysis-python.md) | Lesson 04 — demo [`code/climate_data_python_demo.py`](code/climate_data_python_demo.py) |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Four runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib,
pandas and xarray:

```bash
cd 16-atmosphere-climate/08-climate-observation-and-data/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python observation_records_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python reanalysis_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python homogenisation_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python climate_data_python_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), is print-only, requires no network access and
exits 0. The slowest runs in about two seconds.

## Mastery checkpoint

Complete this without notes:

> A synthetic record of a known trend is observed by a station carrying a
> $+0.40\ \mathrm{K}$ instrument step at year 40 of 120 years, and a network whose
> composition changes at year 60 with a $+0.80\ \mathrm{K}$ mean offset in the
> replacement sites. **(a)** Compute the step's contribution to the fitted trend
> using $\sum_{t\ge40}(t-\bar t) = 1600$ and $\sum_t(t-\bar t)^2 = 143{,}990$, and
> compare it with the measured discrepancy of $+0.0045\
> \mathrm{K\,yr^{-1}}$. **(b)** Explain why the station's own standard error
> ($0.0006\ \mathrm{K\,yr^{-1}}$) does not reveal the error. **(c)** State the
> trend artefact the network-composition change produces and one defence against
> it. **(d)** An adjustment step with an uncertainty of $\pm0.1\ \mathrm{K}$ is
> applied at year 60; compute the trend error it contributes and compare it with a
> formal standard error of $0.0005\ \mathrm{K\,yr^{-1}}$. **(e)** A toy reanalysis
> in a data-sparse era sits $0.35\ \mathrm{K}$ below the truth and corrects to
> $-0.08\ \mathrm{K}$ once observations are dense: state the trend artefact this
> produces and why the ensemble spread misses it. **(f)** Two quantile-mapping
> procedures report changes of $+1.89$ and $-0.01\ \mathrm{K}$ for the same model
> output: state which is correct and why.

Parts (a) and (d) use the step-leverage algebra worked in the lesson-01
[solutions](exercises/01-surface-and-satellite-records-solutions.md) (★★4 and the
lesson §8 example); (e) is the discontinuity-to-trend calculation of the lesson-02
[solutions](exercises/02-reanalysis-products-solutions.md) (★★5); (f) is the
quantile-mapping contrast of the lesson-03
[solutions](exercises/03-climate-data-homogenisation-solutions.md) (★★6).

## Common pitfalls

1. **Reading a small standard error as small uncertainty.** The formal error
   measures noise, not bias, and it cannot see an unadjusted step: the station's
   $0.0006\ \mathrm{K\,yr^{-1}}$ sat on a $+0.0045\ \mathrm{K\,yr^{-1}}$ error.
2. **Assuming more stations means less error.** Shared systematic errors do not
   average down.
3. **Comparing absolute values across a changing network.** Use anomalies and a
   common network, and accept that neither is perfect.
4. **Treating a reanalysis as an observational record.** In sparse periods it is a
   model, and its detail is not information.
5. **Reading the ensemble spread as the total uncertainty.** It omits the model's
   climate bias — a factor of $3.5$ understatement in the demonstration's sparse
   era.
6. **Fitting trends across an observing-system change.** A $0.27\ \mathrm{K}$ level
   discontinuity produced a $+0.0062\ \mathrm{K\,yr^{-1}}$ apparent trend.
7. **Calling a bias adjustment a data correction.** Quantile mapping maps a model
   distribution onto an observed one; the wrong transfer function removes the
   signal entirely.
8. **Ignoring the multiplicity of a breakpoint scan.** A nominal $|t|>3$ rule fired
   on $12\%$ of no-break realisations.
9. **Unweighted spatial means.** $5.06\ \mathrm{K}$ of offset and $+17.1\%$ of
   trend error in the demonstration.
10. **Unstated reference periods and label conventions.** Anomalies and rolling
    means change meaning without them; a "YE" bin of a July-start record held six
    months, not twelve.

## Related modules

- [16-04 The Climate System and Feedbacks](../04-climate-system-and-feedbacks/README.md) —
  the variability every trend here must be tested against.
- [16-05 Climate Models and Simulation](../05-climate-models/README.md) — where the
  model half of a reanalysis and the bias-adjusted output of lesson 03 come from.
- [16-07 Extremes, Impacts and Attribution](../07-climate-extremes-and-attribution/README.md) —
  the consumer of these records: an attribution statement inherits their
  homogeneity and their coverage.
- [16-09 Geophysics Applied to Climate Science](../09-geophysics-and-climate/README.md) —
  the geophysical instruments that supply the same kind of product, with the same
  obligation to state the detection threshold.
- [03-08 xarray, netCDF and Gridded Earth Data](../../03-scientific-computing/08-gridded-geospatial-data/README.md) —
  the labelled-array practice lesson 04 applies.
- [17-01 Remote Sensing Physics](../../17-remote-sensing-gis/01-remote-sensing-physics/README.md) —
  the radiative-transfer background behind satellite sounding.
- [21-01 Statistics in Practice](../../21-statistics-bayesian-ml/01-statistics-in-practice/README.md) —
  the trend, resampling and detection theory used here.
