---
id: 16-08-04
title: "Analysing Climate Data in Python: xarray and CDO"
level: graduate
prereqs: ["16-08-03", "03-08-02", "03-02-01", "21-01-01"]
tags: [atmosphere, climate, xarray, cdo, data-analysis, area-weighting, regridding]
---

# Analysing Climate Data in Python: xarray and CDO

> **All models and data in this module are SYNTHETIC.** The gridded field in
> `code/climate_data_python_demo.py` is generated from a chosen formula. No real
> dataset, reanalysis, station, model output or published value is used.

A climate data file is an array with **labelled axes**, and almost every error in
applied climate analysis is a mistake about those labels: a latitude mean taken
without area weights, an anomaly formed against an unstated reference period, an
annual mean labelled at the wrong end of the year, a data gap silently
re-weighting a spatial mean, a regridding that does not conserve the quantity it
moves. None of these mistakes throws an error. They all produce a plausible
number.

This lesson is about doing the mechanics correctly, in `xarray`, with the
corresponding `CDO`-style operators named so that a reader who works on the command
line can map one to the other. The demonstrations are deliberately simple — one
synthetic field, a handful of operations — because the point is the bookkeeping,
not the physics. Each operation is accompanied by the measured size of the error
you get by doing it the naive way: $5.06\ \mathrm{K}$ from ignoring area weights,
$+17.1\%$ on a trend from the same omission, $2.62\ \mathrm{K}$ from a data gap
averaged without weights, $2.77\ \mathrm{K}$ in a high-latitude block from a
non-conservative coarse-graining.

## Learning objectives

By the end of this lesson you will be able to:

1. **Describe** a gridded climate dataset as labelled arrays, and **state** the
   coordinate and unit conventions that must be checked first.
2. **Derive** the area element on a latitude–longitude grid and **explain** why
   $\cos(\mathrm{lat})$ weighting is required for any zonal or global mean.
3. **Measure** the error introduced by an unweighted spatial mean, for both a mean
   value and a trend.
4. **Form** climatologies and anomalies with an explicitly stated reference
   period, and **explain** what does and does not change when the period changes.
5. **Handle** time correctly: resampling labels, partial bins, rolling windows and
   their lost endpoints.
6. **Handle** missing data by renormalising weights, and **measure** the error of
   not doing so.
7. **Coarse-grain conservatively** and **measure** the error of a plain block mean.
8. **Map** the common `CDO` operators onto their `xarray` equivalents and **state**
   the three habits that prevent most of these mistakes.

## Prerequisites

- [16-08-03 Homogenisation, Bias Adjustment and Uncertainty](03-climate-data-homogenisation.md) —
  what the data have already been through before you open them.
- [03-08-02 xarray DataArray, Coordinates and Labeled Dimensions](../../03-scientific-computing/08-gridded-geospatial-data/02-xarray-dataarray.md) —
  the labelled-array model used throughout this lesson.
- [03-02-01 ndarray Creation, dtypes, Shapes and Strides](../../03-scientific-computing/02-numpy/01-ndarray-basics.md) —
  the array semantics underneath xarray.
- [21-01-01 Descriptive Statistics, Robust Measures and Outliers](../../21-statistics-bayesian-ml/01-statistics-in-practice/01-descriptive-statistics.md) —
  means, trends and weighting.

## 1. What a climate dataset is

A climate dataset is an array with names for its axes. In `xarray` a
`DataArray` carries:

- **dimensions** (`time`, `lat`, `lon`, `lev`, …) — the axes;
- **coordinates** — the label value at each index along each axis;
- **attributes** — at minimum `units`, and ideally the provenance and the
  processing history.

Three checks come before any calculation, and they catch a large fraction of real
mistakes:

1. **Units.** $\mathrm{K}$ or $^\circ\mathrm{C}$? Per second or per day? A single
   field with mixed units silently produces nonsense.
2. **Coordinate semantics.** Are `lat` values *point* coordinates (the centre of
   each grid cell) or *bounds*? For weights and for regridding this matters: the
   area of a cell is set by its **edges**, not its centre.
3. **Calendar and time convention.** Standard, no-leap, 360-day calendars differ;
   month lengths differ; and a monthly mean's timestamp may sit at the start, the
   middle or the end of the month.

The demonstration's synthetic field has shape $(18, 36, 288)$ — 18 latitudes from
$-85^\circ$ to $+85^\circ$, 36 longitudes, 288 months — and its `lat` coordinate
holds point values, which is exactly the situation in which naive area weighting
goes wrong.

## 2. Area weighting, derived

On a sphere of radius $R$, the area element in spherical coordinates is

$$\mathrm{d}A = R^{2}\cos\varphi\;\mathrm{d}\varphi\,\mathrm{d}\lambda,$$

where $\varphi$ is latitude and $\lambda$ longitude. For a regular
latitude–longitude grid the longitude spacing $2\pi/N_{\lambda}$ is constant, so
**the area of a grid cell is proportional to $\cos\varphi$** and a global mean is

$$\overline{X} = \frac{\sum_{j,k} X(\varphi_j,\lambda_k)\cos\varphi_j}
{\sum_{j,k}\cos\varphi_j}.$$

Why it matters numerically: at $85^\circ$ a cell covers
$\cos 85^\circ = 0.0872$ of an equatorial cell's area, so an unweighted mean gives
it $11.5$ times its correct influence. For a field that varies with latitude —
every climate field — the error is first-order, not a refinement.

The demonstration measures it. For the synthetic field:

| quantity | unweighted | $\cos(\mathrm{lat})$-weighted | difference |
|---|---|---|---|
| global mean, first month (K) | 275.0249 | 280.0804 | $-5.0555$ |
| fitted trend (K/yr) | $+0.0472$ | $+0.0403$ | $+0.0069$ ($+17.1\%$) |

The field warms faster at high latitudes by construction, so the unweighted mean
over-weights the fast-warming polar points and inflates the trend by $17\%$ — an
error of the same order as the trend itself. `xarray` performs the weighted mean
with `da.weighted(weights).mean(dim)`, which **renormalises by the sum of the
weights actually used**; a plain `da.mean(dim)` does not weight at all.

## 3. Climatology, anomalies and the reference period

An **anomaly** is a deviation from a **climatology**, and a climatology is defined
over a stated **reference period**. For a monthly climatology,

$$A(t) = X(t) - \overline{X}_{\text{month}(t)},$$

where $\overline{X}_m$ is the mean of all values in month $m$ within the reference
period. Three consequences:

- Changing the reference period shifts **every** anomaly by the change in the
  period mean, so the *level* of an anomaly series is a choice.
- Differences of anomalies, and trends, are **not** affected by a uniform shift —
  which is why anomaly-based comparisons are robust to a common offset but not to
  a change in the period *within* the series.
- A seasonal cycle computed from a short period is noisy; the same cycle computed
  in different decades differs, and that difference is not climate change until it
  is tested.

In the demonstration the area-weighted global-mean seasonal cycle has range
$4.379\ \mathrm{K}$ (months 1, 4, 7, 10 give $280.544$, $282.730$, $284.923$,
$282.730\ \mathrm{K}$), much smaller than the local seasonal amplitude of
$6.0\ \mathrm{K}$, because the cycle is latitude-dependent and partly cancels in a
global mean. The anomaly field has standard deviation $0.844\ \mathrm{K}$, which is
the internal variability the trend must be detected against.

## 4. Time: resampling, labels and windows

`xarray`'s `resample(time=...)` bins a time series the way `pandas` does, and the
**label convention is part of the result**:

- `resample(time="YE")` labels each bin by its **last** day (`2000-12-31` for the
  first bin of a January-start record);
- `resample(time="YS")` labels each bin by its **first** day (`2000-01-01`).

For a record that starts in January the *values* are identical — the demonstration
verifies this — and only the labels differ, by $365$ days. For a record that starts
in July the difference is not cosmetic: the first `"YE"` bin contains **6 months**,
so it is not an annual mean at all. The demonstration prints exactly that
(6 months, not 12). **An annual mean that is not a 12-month mean is a different
statistic**, and it will appear in a map as an artefact.

Rolling windows have the same issue at the ends. A centred 12-month rolling mean of
a 288-month series leaves $277$ valid values (the demonstration's count), losing
six months at each end; a trailing window loses eleven at the start only. The
first and last valid labels in the demonstration are `2000-07-01` and
`2023-07-01`. State which window you used, and never compare a rolling-mean series
with a raw one over the periods where the window is incomplete.

## 5. Missing data and weight renormalisation

Data gaps are not missing at random. A satellite's coverage changes with its orbit;
a station network thins out over mountains and oceans; a quality-control flag
removes one region more than another. What you do with the gap is therefore a
modelling decision.

The demonstration removes every point north of $60^\circ\mathrm{N}$ for two years
($108$ points at one time step) and compares the two ways of coping:

| quantity | complete field (K) | with the gap (K) | error (K) |
|---|---|---|---|
| plain mean over grid points | 275.276 | 277.898 | $+2.622$ |
| $\cos(\mathrm{lat})$-weighted mean | 280.318 | 281.426 | $+1.107$ |

Both estimates change, because the removed region has its own temperature; the
point is that they change **differently**. `weighted()` renormalises the weights
over the valid points, so the weighted mean remains an area-weighted mean *of the
available area* — a well-defined quantity, though not the same quantity as before
the gap. A plain `skipna` mean re-weights the grid by how many points happen to be
present, which corresponds to no physical area at all. When the gap's *pattern*
changes with time, the second error changes with time and becomes a trend: a
coverage change entering the record as a climate signal.

**Practice:** form the product of field and weights, count the valid weights,
divide, and report the coverage fraction alongside the mean.

## 6. Regridding: conservative versus convenient

Two arrays on different grids must be brought onto a common grid, and the operation
is not neutral. On a latitude–longitude grid, a plain block average of a
$3\times3$ block weights each contributing cell equally, while a **conservative**
regridder weights each by its area. The demonstration coarse-grains the synthetic
field from $18\times36$ to $6\times12$ and compares, in one column:

| latitude | plain block mean (K) | $\cos(\mathrm{lat})$-weighted (K) | difference (K) |
|---|---|---|---|
| $+75^\circ$ | 261.839 | 264.606 | $-2.767$ |
| $+45^\circ$ | 277.459 | 277.960 | $-0.502$ |
| $+15^\circ$ | 285.572 | 285.627 | $-0.055$ |
| $-15^\circ$ | 286.128 | 286.192 | $-0.065$ |

The mean absolute difference between the two coarse-grainings is $1.079\
\mathrm{K}$. The error is concentrated at high latitudes, where the cells within a
block differ most in area — exactly the physics the naive method discards. For a
**conservative** quantity (mass, energy, a tracer budget) a non-conservative
regridder is not merely inaccurate; it changes the total, and totals are usually
what the study is about.

## 7. The `xarray` / `CDO` correspondence

The command-line world and the Python world implement the same operations. The
pairs below are the ones you will meet most often:

| `CDO` operator | `xarray` equivalent |
|---|---|
| `cdo fldmean` | `da.weighted(coslat).mean(["lat", "lon"])` |
| `cdo timmean` | `da.mean("time")` |
| `cdo monmean` | `da.groupby("time.month").mean("time")` |
| `cdo ymonmean` | monthly climatology (12 values) |
| `cdo sub` with `timmean` | `da.groupby("time.month") - clim` (anomaly) |
| `cdo remapcon` | conservative regridding (area-weighted) |
| `cdo setmissval` | `da.where(mask)` plus explicit renormalisation |

Three habits prevent most mistakes in either world:

1. **Inspect before computing.** Print the `dims`, the coordinate ranges, the units
   and the time span. Most errors are visible at this step.
2. **Weight by $\cos(\mathrm{lat})$ for every zonal or global mean**, and pass the
   weights explicitly; never rely on a default.
3. **Write the reference period and the label convention next to every anomaly,
   mean and rolling statistic.** A number without them is not reproducible.

## 8. Assumptions and regime of validity

1. **A regular latitude–longitude grid.** The $\cos\varphi$ weight is exact only
   for a regular grid in spherical coordinates. On a curvilinear, Gaussian,
   reduced or unstructured grid the weights are the actual cell areas, and
   `cos(lat)` is an approximation — usually a good one, never an identity.
2. **Point coordinates treated as cell centres.** The weight uses the cell's
   latitude, so the label must be the centre, not an edge; mixing the two is a
   systematic offset.
3. **The climatology's period is representative.** A 10-year climatology of a
   variable with a 20-year cycle is a biased reference.
4. **Gaps are ignorable or the coverage is reported.** If the coverage trend is
   comparable to the signal, the estimate is contaminated by the coverage.
5. **The regridding is conservative for the quantity's budget.** Conservative
   remapping preserves the integral; for diagnosed quantities that are not
   integrals (a maximum, a threshold count) conservation does not preserve the
   right statistic.
6. **Linear statistics commute with averaging; non-linear ones do not.** A mean of
   means is a mean only with equal weights; a variance of means is not a variance.

## 9. Python demonstration

[`code/climate_data_python_demo.py`](code/climate_data_python_demo.py) builds the
synthetic field and runs the whole analysis, printing labelled results with units.
It:

1. constructs an `xarray.DataArray` with `time`, `lat` and `lon` coordinates;
2. compares plain and $\cos(\mathrm{lat})$-weighted global means and trends;
3. forms a monthly climatology and anomalies and measures the seasonal range;
4. demonstrates the resampling label convention and a partial bin;
5. measures the error of `skipna` averaging across a data gap;
6. compares simple and conservative coarse-graining;
7. prints the `xarray`/`CDO` operator correspondence and the three habits.

Every number in this lesson is printed by that demonstration.

## Mastery checkpoint

> The demonstration's synthetic field warms at $0.030\ \mathrm{K\,yr^{-1}}$ in the
> global mean, with a polar amplification factor $1 + 1.5(|\mathrm{lat}|/90)^{2}$.
>
> **(a)** Write the area element on a sphere and explain why $\cos\varphi$ appears.
> **(b)** The unweighted trend is $+0.0472\ \mathrm{K\,yr^{-1}}$ and the weighted
> trend $+0.0403\ \mathrm{K\,yr^{-1}}$. Explain the sign and approximate size of
> the difference using the polar amplification factor.
> **(c)** A 24-year record starting in January is annualised with `resample("YE")`
> and `resample("YS")`. State what differs and, for a July-start record, what is
> wrong with the first bin.
> **(d)** Removing a region for two years changes the weighted global mean by
> $+1.107\ \mathrm{K}$ and the unweighted mean by $+2.622\ \mathrm{K}$. Explain why
> the two differ, and which is the better-defined quantity.
> **(e)** A $3\times3$ block coarse-graining differs from a conservative one by
> $2.767\ \mathrm{K}$ at $+75^\circ$. Explain why the error is concentrated there.
> **(f)** State the three habits that would have caught the errors in (b)–(e).

## Common pitfalls

1. **Unweighted spatial means.** $5.06\ \mathrm{K}$ of offset and $+17.1\%$ of
   trend error in the demonstration.
2. **A default weighting that is not the physics.** Check what your library does
   when a weight is missing; renormalisation is a choice.
3. **Unstated reference period.** Anomaly levels move; differences of anomalies do
   not.
4. **Mislabelled annual means.** A `"YE"` bin of a mid-year-start record held six
   months.
5. **Comparing rolling means over incomplete windows.** Six months are lost at each
   end of a centred 12-month window.
6. **`skipna` without weights.** A gap changes the effective area, and a changing
   coverage becomes a trend.
7. **Non-conservative regridding of a budget.** $1.079\ \mathrm{K}$ mean absolute
   difference in the demonstration, concentrated at high latitude.
8. **Assuming `lat`/`lon` labels are cell edges.** They are usually centres; cell
   area comes from the edges.

## Related modules

- [16-08-01 Surface, Radiosonde and Satellite Climate Records](01-surface-and-satellite-records.md) —
  what the numbers in a file are, before they reach your array.
- [16-08-02 Reanalysis: ERA5, MERRA, JRA and Their Caveats](02-reanalysis-products.md) —
  the most common gridded products, and what their completeness means.
- [16-08-03 Homogenisation, Bias Adjustment and Uncertainty](03-climate-data-homogenisation.md) —
  the adjustments the data have already been through.
- [17-05-03 Raster Data Model, Resolution and Resampling](../../17-remote-sensing-gis/05-gis-fundamentals/03-raster-data-model.md) —
  grids, resolution and resampling in the geospatial context.
- [03-08-05 Case Study: Analysing a Climate Data Cube](../../03-scientific-computing/08-gridded-geospatial-data/05-climate-data-cube.md) —
  the same operations applied end-to-end to a realistic climate dataset.
- [03-02-04 Universal Functions, Reductions and Axis Semantics](../../03-scientific-computing/02-numpy/04-ufuncs-reductions.md) —
  the axis and reduction semantics underneath `mean(dim=...)`.
- [22-02 Reproducible Workflows](../../22-data-engineering-reproducibility/02-reproducible-workflows/README.md) —
  storing, versioning and documenting the processing chain.

## Self-assessment checklist

- [ ] I can state the coordinate, unit and calendar checks I perform first.
- [ ] I can derive the $\cos\varphi$ area weight and apply it explicitly.
- [ ] I can form an anomaly with a stated reference period.
- [ ] I can explain the resampling label convention and a partial bin.
- [ ] I can handle a gap by renormalising weights and reporting coverage.
- [ ] I can choose conservative regridding and say why.
- [ ] I can map a `CDO` command to its `xarray` equivalent.
