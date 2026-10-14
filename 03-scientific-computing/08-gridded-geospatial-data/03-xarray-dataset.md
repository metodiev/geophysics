---
id: 03-08-03
title: "Dataset, Alignment, Broadcasting and GroupBy"
level: advanced
prereqs: ["03-08-02", "03-04-04"]
tags: [xarray, dataset, weights, area-weighting, groupby, geodesy]
---

# Dataset, Alignment, Broadcasting and GroupBy

Real gridded data are never one array. A gravity compilation ships an anomaly, an
elevation, a Bouguer correction and a quality mask on the same grid; a climate
product ships temperature, wind and humidity on a shared space–time lattice. The
`Dataset` is xarray's container for that family of arrays, and the whole reason
to use it is that the members are guaranteed to share their coordinates.

> **Every quantity below is measured output from
> `code/xarray_dataset_demo.py`**, which builds a SYNTHETIC global cube. Nothing
> is downloaded.

This lesson also contains the single most consequential calculation in the whole
module: the difference between a naive grid mean and an area-weighted mean, and
the precise sense in which `cos(latitude)` is the right weight.

## Learning objectives

By the end of this lesson you will be able to:

1. **Build** a `Dataset` from variables that share dimensions, and say what
   `data_vars` and `coords` guarantee.
2. **Distinguish** the merge default join (`outer`) from the arithmetic default
   (`inner`), and predict the NaN footprint of each.
3. **Compute** an area-weighted mean with `ds.weighted(w).mean(...)` and show
   algebraically that it equals $\sum w x / \sum w$.
4. **Quantify** the error of a naive grid mean, in absolute units and in per
   cent, for a field with a meridional gradient — globally and inside a small
   box.
5. **Derive** the exact area of a latitude band on an ellipsoid, verify the
   formula against the closed-form total surface area, and bound the error of the
   `cos(lat_mid)` shortcut.
6. **Use** `groupby` and `groupby_bins` correctly, including the fact that equal
   cell counts do not mean equal areas.
7. **Explain** why the area of a "lat–lon box" is ambiguous at the 0.25 % level.
8. **Predict** where `rolling` and `shift` introduce NaN, and how many.

## Prerequisites

- [03-08-02 xarray DataArray, Coordinates and Labeled Dimensions](./02-xarray-dataarray.md)
  — labels, alignment and broadcasting.
- [03-04-04 Group-By, Aggregation and Reshaping](../04-pandas/04-groupby-aggregation.md)
  — the tabular version of `groupby`, including the split–apply–combine contract.

## 1. Intuition: why a container, not a convention

A directory of eight NetCDF files on the same grid is a contract enforced by
nothing. Rename a dimension, shift one file's longitudes by half a cell, or load
them with a different chunking, and the analysis still runs.

A `Dataset` enforces the contract structurally:

```python
ds = xr.Dataset({"anomaly": anomaly, "elevation": elevation, "t2m": temperature},
                attrs={"title": "SYNTHETIC dataset", "Conventions": "CF-1.11"})
```

Measured: `data_vars = ['anomaly', 'elevation', 't2m']`,
`coords = ['lat', 'lon', 'time']`, `dims = {'lat': 60, 'lon': 120, 'time': 36}`,
`anomaly` shape `(60, 120)`, `t2m` shape `(36, 60, 120)`. The `t2m` variable is
three-dimensional and the anomaly is two-dimensional; they are consistent because
they name the same `lat` and `lon` dims. Selecting a point returns all three
variables at once — measured `anomaly = 19.0538 mGal`,
`elevation = 2091.0 m`, and `t2m` with all 36 time steps — which is what makes a
joint analysis possible without keeping a private index mapping in your head.

## 2. Alignment inside a Dataset

### 2.1 The merge default is the union

Merging a fine grid with a coarse one is the archetypal compilation step.
Measured:

```
coarse grid (30, 60) with lat spacing 6.0 deg
xr.merge default join='outer' -> {'lat': 90, 'lon': 180},
  NaN in the coarse variable = 14,400 (88.9 % of the union grid)
join='inner' -> {'lat': 0, 'lon': 0}, NaN = 0
```

The union grid has $90 \times 180 = 16{,}200$ cells, of which the coarse variable
covers only $30 \times 60 = 1{,}800$: the missing fraction is
$1 - 1800/16200 = 88.9$ %, exactly as printed. An inner join keeps only the 1,800
labels that exist in both — but "both" is false here, because the two grids share
no labels at all when one is a 6° subsampling by *coarsening*; hence the empty
result. **The default for merging is deliberately conservative (keep everything,
fill with NaN), while the default for arithmetic is deliberately narrow (keep
only the overlap).** Both defaults assume you are paying attention.

### 2.2 Selecting does not touch the other variables

`ds.sel(lon=slice(-120.0, -100.0), lat=slice(30.0, 45.0))` returns a `Dataset` in
which every variable was subset consistently — measured: `anomaly` becomes
`(5, 7)` = 35 of 7,200 cells, 0.5 % of the grid, and `t2m` is subset on the same
`lat`/`lon` labels without being mentioned. This is the structural guarantee in
action.

One measured trap: `ds.sel(lon=-110.0)` raises `KeyError` on the demonstration's
3° grid, because −110.0 is not a label. The 3° grid runs −180.0, −177.0, …, so
−111.0 is present and −110.0 is not. Label addressing is exact, and exactness is
a feature until the day it is an inconvenience; then use `method="nearest"` and
say so in the log.

## 3. Area weighting: the calculation that decides global numbers

### 3.1 The problem in one line

Rows of a lon/lat grid are not equal areas. The demonstration's latitudes run
−88.5° to 88.5° at 3° spacing, so the weight $\cos\phi$ ranges from 0.0262 to
0.9997 — a factor of 38 between the outermost and central rows. Averaging rows
equally is therefore averaging *cells*, and the cells near the poles are tiny.

### 3.2 The measured difference

| Field | Naive grid mean | `cos(lat)`-weighted | Difference |
|---|---|---|---|
| anomaly (mGal) | 4.1389 | 2.3563 | 1.7827 (75.66 %) |
| elevation (m) | 1273.4702 | 1570.7231 | 297.2529 (18.92 %) |

Inside a small box (30–45°N, 120–100°W) the same comparison gives 2.7649 versus
2.7378 mGal — a **0.99 %** difference. Two conclusions, both quantitative:

- Over a wide range of latitude, weighting is not a refinement, it is the
  difference between a number and a number that is 76 % wrong.
- Inside a small box the error is about 1 %, which is the regime where people
  acquire the habit of ignoring it — and then apply the unweighted code to a
  global grid.

### 3.3 The weight, derived

On a sphere of radius $R$, the area of a cell spanning $d\lambda$ and $d\phi$ at
latitude $\phi$ is

$$dA = R^{2}\cos\phi\; d\phi\, d\lambda .$$

A weighted mean of a field $x(\phi,\lambda)$ over the globe is therefore

$$\bar{x} = \frac{\iint x \cos\phi\, d\phi\, d\lambda}
  {\iint \cos\phi\, d\phi\, d\lambda},$$

so $w(\phi) = \cos\phi$ and no normalisation of the *latitudes* is needed as long
as the denominator uses the same weights. Normalising $w$ to have mean 1 (as the
demonstration's `area_weights` helper does) changes nothing, because the ratio is
invariant to a common scale factor. What is *not* invariant is dropping the
weight: then $w \equiv 1$ and the denominator becomes the number of cells.

### 3.4 `weighted` is a normalised sum, and nothing else

The demonstration checks the API against the definition:

```
numerator   sum(w*x) = 10801.553348 (mGal x dimensionless)
denominator sum(w)   = 4584.186002 (dimensionless: 60 rows x 120 columns)
manual sum(w*x)/sum(w) = 2.3562641970 mGal
ds.weighted(w).mean()  = 2.3562641970 mGal
difference = 1.155e-14 mGal
```

Agreement at the 10⁻¹⁴ level is floating-point closure, not similarity. Note the
units carefully: the weight is dimensionless (a cosine), so the weighted mean
carries exactly the units of the field. That is why a *cell-area* weight works
too — area in m² divided by area in m² is dimensionless — and why mixing a
cosine weight with an area weight gives the same answer only if the areas are
proportional to the cosines.

## 4. The exact area of a latitude band, and the cost of `cos(lat)`

The `cos(lat)` weight is exact on a sphere. The Earth is an ellipsoid, and the
distinction has a measurable size.

### 4.1 The formula

For a latitude band from $\phi_1$ to $\phi_2$ spanning $\Delta\lambda$ of
longitude, the exact ellipsoidal area is

$$A = \frac{\Delta\lambda}{2}\,a^{2}(1-e^{2})\Big[F(\phi)\Big]_{\phi_1}^{\phi_2},
\qquad
F(\phi) = \frac{\sin\phi}{1 - e^{2}\sin^{2}\phi}
  + \frac{1}{2e}\ln\frac{1 + e\sin\phi}{1 - e\sin\phi},$$

with $a$ the semi-major axis and $e$ the first eccentricity. Verified against the
closed-form total surface area of the ellipsoid,
$2\pi a^{2}\big(1 + \frac{1-e^{2}}{e}\operatorname{artanh} e\big)$:

```
validation: sum of bands = 5.100656e+14 m^2, closed form = 5.100656e+14 m^2,
            relative difference = 2.45e-16
```

That is machine precision, so the implementation is right and the numbers below
are trustworthy.

### 4.2 How wrong is `cos(lat_mid)`?

The `cos` weight is a differential statement: it is exact for an infinitesimal
band. For a finite band the exact spherical weight is
$\sin\phi_2 - \sin\phi_1$, and the ellipsoid adds its own correction. Measured
errors of the rule `A ≈ cos(φ_mid) · 2πR²Δφ` with $R = 6{,}371$ km:

| Band | `cos(lat_mid)` rule (km²) | Ellipsoid exact (km²) | Error |
|---|---|---|---|
| 0–5°N | 22,234,578 | 22,128,969 | +0.477 % |
| 30–35°N | 18,770,318 | 18,752,921 | +0.093 % |
| 60–65°N | 10,276,567 | 10,335,814 | −0.573 % |
| 75–80°N | 4,817,028 | 4,855,639 | −0.795 % |

So: **the `cos(lat_mid)` rule carries an error of up to ~0.8 % for 5° bands, and
the error changes sign near 45°.** That is a useful bound to quote. If a
calculation needs better, use the `sin` difference for the sphere and the $F$
formula for the ellipsoid.

Note also the sphere-versus-ellipsoid comparison at the whole-Earth level:
WGS 84's surface is 510.066 × 10⁶ km² and a sphere of $R = 6{,}371$ km is
510.064 × 10⁶ km², a relative difference of −0.0004 %. A mean radius is an
excellent global approximation and a poor regional one.

### 4.3 The ambiguity of "the area of a lat–lon box"

There is a genuine definitional trap here. A box bounded by two **parallels** and
two **meridians** — the ordinary rectangular selection in lon/lat — has the area
given by the band formula. A box whose four edges are **geodesics** has a
different area, because a geodesic between two points at the same latitude bows
poleward of the parallel. Measured for a 10° × 10° box at the equator:

```
area bounded by GEODESICS = 1,227,877.2 km^2
area bounded by PARALLELS = 1,224,832.3 km^2   (+0.249 %)
```

A quarter of a per cent. This is the scale of the disagreement between two
software packages that both compute "the area of the box" correctly. When a
result must reconcile across tools, specify the boundary convention, not just the
coordinates.

## 5. Grouping

### 5.1 By month: climatology

```
groupby('time.month').mean() -> {'month': 12, 'lat': 60, 'lon': 120}
samples per month: [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
zonal-mean temperature at 43.5 N: January -7.084 degC, July -15.103 degC,
  difference -8.019 K
the imposed seasonal term is 4.0*cos(2*pi*i/12) K, so the expected
half-amplitude is 4.000 K; measured 4.010 K
```

The recovery of an imposed 4.000 K half-amplitude to within 0.010 K (0.25 %) is
the check that the calendar arithmetic is right: the synthetic series was built
on real monthly timestamps (`freq="MS"`), so no month drifts. Had the timestamps
been 30-day steps, the same code would have produced a phase-shifted climatology
and a much larger discrepancy — the failure mode seen in the DataArray lesson's
trend fit. **Grouping is only meaningful if the time axis is physically regular.**

### 5.2 By latitude bins: equal counts, unequal areas

```
groupby_bins('lat', 15 deg) -> 12 bins; first (-90.0, -75.0], last (75.0, 90.0]
cells per bin (summed over longitude) = [600, 600, 600, 600, 600, 600, 600, 600, 600, 600, 600, 600]
but the 0-15 N band covers 65,731,954.8 km^2 and the 75-90 N band
only 8,764,211.3 km^2: equal cell counts, 7.50x different areas
```

This is the trap in one picture. A `groupby_bins("lat")` reduction weights every
bin equally by *cell count*; the polar bins are 7.50× smaller in the physical
quantity that matters. Any per-bin statistic that will later be averaged across
bins must carry the bin area with it. Note also the inclusive upper edge in the
printed bin labels: `(-90.0, -75.0]` includes −75.0, so a grid point exactly on a
bin edge is assigned to the bin below. Off-by-one-bin errors at the poles are
usually this.

### 5.3 The mechanics of `groupby` on a Dataset

`ds.groupby("time.month").mean()` splits on the `time` coordinate, applies
`mean` to every variable, and concatenates along a new `month` dimension. Three
consequences worth stating:

1. The grouping key must be a coordinate or a derived one
   (`"time.month"`, `"time.season"`, `"time.dt.year"`), not an array.
2. Variables that do not have the grouped dimension are carried through unchanged
   — a land mask in a `Dataset` grouped over time stays a land mask.
3. Unequal group sizes are *not* reported. `ds.groupby(...).count()` is the audit
   that tells you whether your groups are balanced; run it.

## 6. Rolling and shifting

```
monthly series: 36 steps; rolling(12, center=True) -> 11 NaN ends
mean of the rolled series = -11.9990 degC vs unrolled -11.9991 degC (0.0002 K)
shift(time=1) -> 1 NaN, and it moves the series in the LABEL direction
correlation at lag +1 month = 0.8595
```

A centred window of length 12 removes 11 samples — 5 at each end plus the centre
sample's own window arithmetic — and `shift` moves values *along the labelled
axis*, so the sign of the lag is something you must decide and document.
Correlation at lag +1 being 0.8595 with an imposed 4.0 K annual cycle and 0.2 K
of noise is consistent: what is being correlated is a smoothed seasonal cycle.

The statistical caveat is the important one: `rolling(...).mean()` is a
*smoothing filter*, and a 12-month centred mean of a monthly series is not a
12-month climatology. It suppresses everything with a period near 12 months,
which includes the annual cycle you probably want to keep.

## 7. Reshaping: stack and unstack

```
stack(('lat','lon') -> 'cell') -> (7200,) with a MultiIndex of 2 levels
first label (-88.5, -180.0), last label (88.5, 177.0)
unstack returns (60, 120) and identical values: True
```

Stacking is how a 2-D field becomes an input to a 1-D algorithm — a scatter
plot, a regression against a covariate, a nearest-neighbour search. The
`MultiIndex` keeps the latitude and longitude as *labels*, so unstacking restores
the original grid (measured: identical values) rather than depending on row
order. The last label is `(88.5, 177.0)`: with 120 longitudes from −177.5 at 3°
spacing, the last is +177.5, and the stacked order runs latitude-major.

## 8. Python demonstration

The full script is
[`code/xarray_dataset_demo.py`](./code/xarray_dataset_demo.py):

```bash
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python \
    03-scientific-computing/08-gridded-geospatial-data/code/xarray_dataset_demo.py
```

It writes one NetCDF file into a throw-away directory inside the module and
deletes it on exit. pyproj supplies the ellipsoidal band areas and the geodesic
box areas.

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| merge default is `outer`, arithmetic default is `inner` | two defaults, opposite instincts, both silent |
| global naive vs weighted anomaly differs by 75.66 % | an unweighted global mean is not a small error |
| the same comparison in a 15° × 20° box differs by 0.99 % | regional work hides the habit that breaks global work |
| `weighted` equals $\sum wx/\sum w$ to 10⁻¹⁴ | the API is a definition, not a heuristic |
| the band-area formula matches the closed form to 2.45 × 10⁻¹⁶ | the ellipsoidal numbers can be trusted |
| `cos(lat_mid)` is off by up to 0.795 % for 5° bands | quote the shortcut's error, do not hide it |
| geodesic vs parallel box areas differ by 0.249 % | "the area of the box" needs a convention |
| 12 latitude bins have equal cell counts and 7.50× different areas | bin counts are not physical weights |
| `(ds * 1e6)` keeps the original `attrs['units']` | attribute propagation is copy-paste |
| the round trip writes float64 unless asked otherwise | the file keeps the precision you give it |

> **Breaking exercise.** Change the demonstration's latitude grid to a Gaussian
> one that is dense at the equator, and predict whether the naive-versus-weighted
> gap grows or shrinks. Then measure it.

## 9. Units and dimensional analysis

Area weighting is where units do the most work in this module, so fix the
bookkeeping explicitly:

- The field $x$ has units $[x]$; the weight is dimensionless; therefore
  $\bar{x}$ has units $[x]$. Measured numerator 10,801.553348 has units
  mGal × dimensionless, denominator 4,584.186002 is dimensionless, quotient
  2.3562641970 mGal.
- A weight built from areas has units m², and the quotient is again dimensionless
  in area. What is forbidden is a weight built from *unconverted degrees*, which
  has units that vary with latitude and therefore is not a weight at all.
- $\cos\phi$ is defined only for $\phi$ in radians. `np.cos(np.deg2rad(lat))` is
  the only defensible spelling; `np.cos(lat)` with degrees in `lat` is a
  quantity with no name.
- A latitude *bin* label such as `(75.0, 90.0]` is a range in degrees; the
  corresponding area is in km². Keeping the two in separate columns prevents a
  7.5× error from becoming a 7.5× error in a published table.

## 10. Common mistakes

1. **Averaging a global grid without weights.** Measured cost: 75.66 % on the
   demonstration's anomaly, 18.92 % on elevation, and it can be any size.
2. **Assuming the merge default drops data.** It does not; it fills with NaN.
   The NaN fraction is predictable: 88.9 % in the demonstration.
3. **Treating `groupby_bins` counts as physical weights.** Equal counts, 7.50×
   area ratio.
4. **Forgetting `keep_attrs` semantics differ across versions.** Check
   `xr.get_options()` rather than trusting a tutorial.
5. **Comparing areas from two tools without agreeing on the boundary.**
   Parallel-bounded and geodesic-bounded boxes differ by 0.249 % for a 10° box.
6. **Using a centred rolling mean as a climatology.** It removes the annual cycle.
7. **Concluding that a trend is robust because the noise is small.** In the
   climate cube lesson the same series gives 0.2002 and 0.1997 K/decade under two
   weightings but residual rms values of 1.72 mK and 165.78 mK: the *residuals*
   differ by two orders of magnitude because the unweighted mean cancels a
   $\cos 2\phi$ pattern that the weighted mean keeps. Agreement of a slope is not
   evidence that the two series are the same.

## 11. Real-world applications

- **Gravity compilations.** Merging surveys on different grids and averaging to a
  common cell size is an alignment problem with a NaN footprint that must be
  reported, not just produced.
- **Global climate indicators.** Every "global mean temperature anomaly" number in
  the literature depends on the weighting and the mask; the difference between
  76 % and 1 % error is the difference between a global and a regional claim.
- **Satellite gravimetry.** GRACE equivalent-water-height fields are unequal-area
  by construction (equal-area in terms of the spherical harmonic basis), so
  converting them to a lat/lon grid and then averaging without weights is a
  common and avoidable error.
- **Ice-sheet mass balance.** Ice-sheet areas are computed on polar stereographic
  grids and then compared with global products; geodesic-versus-parallel
  boundary conventions matter at the 0.1 % level, which is a few tens of Gt.
- **Ocean heat content.** Basin integrals are weighted by cell volume, not cell
  area, and the bathymetry mask changes the weight; a merged `Dataset` with the
  mask as a variable is the structure that keeps this straight.

## 12. Further reading

- **Xarray, *Computation* and *GroupBy* user-guide sections.** Level:
  intermediate. <https://docs.xarray.dev> — the reference for
  `weighted`, `groupby`, `resample` and `rolling`.
- **CF Conventions Committee, *CF Conventions*.** Level: reference.
  <https://cfconventions.org> — cell measures and cell methods, the standard way
  to state a weighting inside a file.
- **cf-xarray, *CF convention aware accessors*.** Level: intermediate.
  <https://cf-xarray.readthedocs.io> — reads `cell_area`, `standard_name` and
  coordinate metadata so your code does not have to guess.
- **Hoyer, S. and Hamman, J. (2017). xarray: N-D labeled arrays and datasets in
  Python. *Journal of Open Research Software*, 5(1), 10.** Level: intermediate.
  The design rationale for shared dimensions.
- **Karney, C. F. F. (2013). Algorithms for geodesics. *Journal of Geodesy*,
  87(1), 43–55.** Level: advanced. The algorithms behind the geodesic
  computations used here to define the "true" areas; useful when you need to know
  what `Geod.geometry_area_perimeter` is actually doing.

> Note on citations: bibliographic details are given so you can locate these
> works. This repository does not host or reproduce copyrighted text.

## 13. Related lessons

- [01 netCDF/HDF5 Formats and Self-Describing Data](./01-netcdf-and-hdf5.md) —
  where the `Dataset` came from.
- [02 xarray DataArray, Coordinates and Labeled Dimensions](./02-xarray-dataarray.md)
  — alignment and broadcasting in one array.
- [04 Chunking with Dask for Out-of-Core Analysis](./04-dask-chunking.md) —
  the same `Dataset` with lazy, chunked storage.
- [05 Case Study: Analysing a Climate Data Cube](./05-climate-data-cube.md) —
  weighting, trends and regression maps on a 480-month cube.
- [03-04-04 Group-By, Aggregation and Reshaping](../04-pandas/04-groupby-aggregation.md)
  — the tabular ancestor of Section 5.

## Exercises

[`exercises/03-xarray-dataset-exercises.md`](./exercises/03-xarray-dataset-exercises.md),
with full worked answers in
[`exercises/03-xarray-dataset-solutions.md`](./exercises/03-xarray-dataset-solutions.md).

## Self-assessment checklist

- [ ] I can build a `Dataset` whose members share dimensions, and explain what
      that guarantees.
- [ ] I can predict the NaN footprint of an `outer` merge given the two label
      sets.
- [ ] I can compute a weighted mean by hand and show it equals
      `ds.weighted(w).mean()`.
- [ ] I can state the measured naive-versus-weighted gap globally and inside a
      small box.
- [ ] I can write down the exact ellipsoidal area of a latitude band and say what
      the `cos(lat_mid)` rule costs.
- [ ] I know that a geodesic-bounded box differs from a parallel-bounded box by
      0.25 % for a 10° box.
- [ ] I can explain why 12 equal-count latitude bins are not equal weights.
- [ ] I can say how many NaN a centred 12-point rolling mean introduces.
