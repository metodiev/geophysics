# Module 17-07 — Earth Observation Data and Platforms

**Stages:** intermediate → doctoral · **Prerequisites:** modules 17-01 and 17-05;
basic Python and array handling.

This module is about the *data* side of Earth observation: where a product comes
from, what its numbers mean, where it is served from, how it is found, and how a
stack of observations becomes a time series. It is built around one honest
difficulty: **an Earth-observation product is a computation frozen at a chosen
step.** A digital number becomes a radiance through calibration coefficients,
a radiance becomes a reflectance through solar geometry, a reflectance becomes a
surface reflectance through an atmospheric model, and a stack becomes a
composite through a cloud mask and a reducer. Every one of those steps is a model
or a choice, and the file you download records only some of them.

The four lessons move along that chain. Lesson 01 is the calibration and index
chain, and its central result is that a ratio index is robust to a *multiplicative*
gain error but not to an offset, and that aggregation is nonlinear. Lesson 02
moves the computation to the archive: the reducer becomes part of the method, a
cloud mask has false negatives, and a version change shifts the answer. Lesson 03
is discovery, framed as a detection problem over metadata that is itself a
measurement with error — and licensing as three independent permissions, not one.
Lesson 04 turns a cube into a trend and shows that the standard error is wrong
unless the autocorrelation is accounted for, that sampling can invent a trend,
and that a break is not a trend.

All models and data in this module are **SYNTHETIC**. No real archive, scene,
station or time series is used, and no number is quoted from a published
measurement. Three platform families are named (Google Earth Engine, the
Copernicus services and NASA Earthdata) as canonical examples of an
archive-plus-compute service; no specification of any of them is quoted.

## Learning objectives

By the end of this module you will be able to:

1. **Convert** a digital number to radiance and to top-of-atmosphere reflectance
   with units, and **distinguish** the four levels of an optical observation.
2. **Compute** a normalised band index and **state** the conditions under which
   it is invariant to a calibration error.
3. **Demonstrate** the saturation of an index and the nonlinearity of
   aggregation, and **state** the consequence for a coarse product.
4. **Explain** the compute-at-source model, **compute** an egress ratio, and
   **state** why the reducer is part of the method.
5. **Measure** the bias of a compositing method with and without a cloud mask,
   and **state** why a median is not a cure.
6. **Measure** a discovery query with precision and recall, and **explain** why
   metadata error degrades both.
7. **Distinguish** access, redistribution and derivative rights, and **state**
   which a given use requires.
8. **Estimate** a trend with a corrected standard error, **demonstrate** aliasing,
   and **distinguish** a break from a trend.

## Prerequisites

- [17-05-03 Raster Data Model, Resolution and Resampling](../05-gis-fundamentals/03-raster-data-model.md)
  — grids, cells and resampling.
- [17-01-04 Spatial, Spectral, Temporal and Radiometric Resolution](../01-remote-sensing-physics/04-resolution-concepts.md)
  — the four resolutions.
- [03-08-02 xarray DataArray](../../03-scientific-computing/08-gridded-geospatial-data/02-xarray-dataarray.md)
  — the labelled array a gridded product is held in.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Landsat, Sentinel and MODIS Data Products](01-landsat-sentinel.md) | intermediate | A product is a calibration chain; a ratio index cancels a multiplicative error, not an offset; aggregation is nonlinear |
| 02 | [Cloud Platforms: GEE, Copernicus, NASA Earthdata](02-cloud-platforms.md) | advanced | The reducer is part of the method; a cloud mask has blind spots; the version is part of the answer |
| 03 | [Data Discovery, Access and Licensing](03-data-discovery.md) | intermediate | Discovery is detection over metadata with error; access is not redistribution |
| 04 | [Satellite Time Series and Trend Analysis](04-time-series-satellite.md) | doctoral | The naive error is wrong; sampling can invent a trend; a break is not a trend |

## Suggested path

**If you are new to Earth observation:** lessons 01 and 03 in order, running each
demonstration. Lesson 01 is the calibration you cannot skip; lesson 03 is where
you will spend most of your real time.

**If you already use a cloud platform:** read 02 §3–§5 (masking and versions),
then 04 — the two places where a platform's convenience becomes a
reproducibility risk.

**If you are preparing a research project:** 01 §5–§6 (index limits and
aggregation), 02 §5 (versioning) and all of 04, plus the ★★★ exercises.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-landsat-sentinel.md`](01-landsat-sentinel.md) | Lesson 01 |
| [`02-cloud-platforms.md`](02-cloud-platforms.md) | Lesson 02 |
| [`03-data-discovery.md`](03-data-discovery.md) | Lesson 03 |
| [`04-time-series-satellite.md`](04-time-series-satellite.md) | Lesson 04 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Four runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib,
pandas, xarray and the geospatial stack:

```bash
cd 17-remote-sensing-gis/07-earth-observation-data/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python landsat_sentinel_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python cloud_platforms_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python data_discovery_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python time_series_satellite_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), reads and writes no files, and exits 0. They
require no network access.

## Mastery checkpoint

Complete this without notes:

> A band with $g = 0.020$, $o = -1.00$, $E_s = 1900\ \mathrm{W\,m^{-2}\,\mu m^{-1}}$
> and $\theta = 40^\circ$ records $DN = 4500$. **(a)** Compute the radiance and
> the reflectance with units. **(b)** A second band ($E_s = 1700$) records
> $DN = 6500$; compute the NDVI of the pair. **(c)** A cloud platform returns a
> masked median for that pixel with a flagged clear count of $40$ of $60$; state
> how the count depends on the mask and why it must be reported. **(d)** A trend
> fitted to five years of the resulting index has a naive standard error of
> $0.003$ and $\rho = 0.5$; compute the corrected error and state whether the
> detection survives.

The calibration and NDVI arithmetic of (a)–(b) follows the worked examples in
[lesson 01](01-landsat-sentinel.md); the corrected-error arithmetic of (d) is
developed in [lesson 04](04-time-series-satellite.md).

## Common pitfalls across this module

1. **Treating a product as raw data.** Every level adds a model.
2. **Reading a ratio index as a measurement.** It saturates and it is not linear.
3. **Averaging an index to a coarser grid.** The Jensen gap is real.
4. **Trusting a cloud mask.** It has false negatives; report the count.
5. **Citing a collection without a version.** Reprocessing changes the number.
6. **Confusing access with redistribution.** They are different permissions.
7. **Dividing a trend by a naive standard error.** Autocorrelation inflates it.

## Related modules

- [17-01 Remote Sensing Physics](../01-remote-sensing-physics/README.md) — the
  physics the calibration chain encodes.
- [17-02 Optical and Thermal Remote Sensing](../02-optical-and-thermal-remote-sensing/README.md)
  — the indices and retrievals built on these products.
- [22-02 Reproducible Research Workflows](../../22-data-engineering-reproducibility/02-reproducible-workflows/README.md)
  — versioning and provenance as general practice.
- [21-07 Time-Series Modelling and Forecasting](../../21-statistics-bayesian-ml/07-time-series-and-forecasting/README.md)
  — the statistical home of lesson 04.
