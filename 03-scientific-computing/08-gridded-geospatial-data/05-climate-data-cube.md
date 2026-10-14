---
id: 03-08-05
title: "Case Study: Analysing a Climate Data Cube"
level: advanced
prereqs: ["03-08-03", "03-08-04", "03-08-01"]
tags: [climate, case-study, anomalies, trend, area-weighting, regression-map, enso]
---

# Case Study: Analysing a Climate Data Cube

This lesson runs one analysis end to end, on data whose truth is known because it
was imposed. That is the only way to check an analysis pipeline rigorously: build
a field with a trend, a seasonal cycle and an oscillation of stated amplitude,
then ask whether the pipeline recovers them.

> **Every number below is measured output from
> `code/climate_data_cube_demo.py`.** The cube is SYNTHETIC and generated with
> `np.random.default_rng(20260806)`. Nothing is downloaded, and no observation of
> the Earth appears in this lesson.

## Learning objectives

By the end of this lesson you will be able to:

1. **Build** a labelled 480-month cube with an imposed trend, seasonal cycle,
   meridional profile and amplitude-modulated oscillation, and state each imposed
   amplitude.
2. **Compute** anomalies against a stated baseline and say what the baseline
   choice does to the residual mean.
3. **Recover** an imposed trend to within a stated tolerance, and report the
   residual rms alongside the slope.
4. **Show** that a naive grid mean and an area-weighted mean can agree on a slope
   while disagreeing by two orders of magnitude on the residuals.
5. **Demonstrate** that subsampling months biases a trend, with the measured
   number.
6. **Produce** a regression map of the field against an index, and predict the
   peak correlation from the imposed amplitudes before measuring it.
7. **Read** a lag-correlation profile and explain why it decays rather than
   oscillating.
8. **State** what a real dataset would add that this synthetic cube cannot show.

## Prerequisites

- [03-08-03 Dataset, Alignment, Broadcasting and GroupBy](./03-xarray-dataset.md)
  — weights, `groupby`, and the ellipsoidal area facts used here.
- [03-08-04 Chunking with Dask for Out-of-Core Analysis](./04-dask-chunking.md)
  — the technique this cube would need at 0.25° resolution.
- [03-08-01 netCDF/HDF5 Formats and Self-Describing Data](./01-netcdf-and-hdf5.md)
  — the storage conventions a real product follows.

## 1. The cube, and the ground truth it encodes

```
dims = {'time': 480, 'lat': 36, 'lon': 72}, dtype = float64, nbytes = 9,953,280
time: 1985-01-01 .. 2024-12-01 (480 monthly steps)
lat: -87.5 .. 87.5 deg, spacing 5.0 deg
lon: -177.5 .. 177.5 deg, spacing 5.0 deg
values: -33.88 .. 33.05 K
IMPOSED: trend 0.20 K/decade, seasonal amplitude 3.00 K, ENSO amplitude 1.40 K
grid cells = 2,592; grid spacing is UNIFORM in longitude and latitude,
  so cells are NOT equal-area
```

Five ingredients, each with a stated amplitude:

| Term | Form | Purpose |
|---|---|---|
| meridional profile | $28 - 0.30|\phi| - 0.004\phi^{2}$ | a strong latitude gradient, so weighting matters |
| seasonal cycle | $3\cos(2\pi t/12)$ | a signal that must be removed before a trend |
| warming trend | $0.20 \times (t/120)$ | the quantity to recover, in K/decade |
| oscillation | $1.4\, f(t)\cos 2\phi$ | an amplitude-modulated signal at 4-year period |
| noise | $\mathcal{N}(0, 0.35)$ | an irreducible floor of 0.35 K |

Two engineering notes are worth recording because they were bugs first.

**Broadcasting aligns trailing axes.** The oscillation was initially written as
`enso * cos(2*lat)` with shapes `(480,)` and `(1, 36, 1)`. NumPy treats the
1-D array as `(1, 1, 480)` — padding on the *left* — so the "time" variation was
placed along longitude and the regression map came out at |r| = 0.10 instead of
0.83. The fix is to state every shape explicitly:
`enso[:, None, None] * pattern[None, :, None]`. This is the same trap as
[03-02-03 Broadcasting](../02-numpy/03-broadcasting.md), and the detection method
here was the *regression map itself*: the imposed pattern is `cos 2φ`, so a peak
at a latitude of 7.5° instead of ~0° is a signature of a scrambled forecast.

**Grid spacing uniform in degrees is not uniform in area.** 36 rows over 175° of
latitude and 72 columns over 355° of longitude. Cell area ∝ cos φ, which spans
0.044 at 87.5° to 0.999 at 0°, a factor of 23 within this grid alone.

## 2. Anomalies and the baseline

```
baseline 1985-2014 has 360 months; climatology {'month': 12, 'lat': 36, 'lon': 72}
global mean over the baseline = 12.3419 K
monthly anomalies: shape (480, 36, 72), mean over the WHOLE record = +0.1000 K
baseline anomaly mean = +0.000000 K; std = 0.5488 K
```

An anomaly is a difference from a stated reference, so the baseline is part of the
definition, not a preprocessing detail. Three facts follow from the numbers:

1. The whole-record anomaly mean is **+0.1000 K** even though the baseline mean is
   0.000000 by construction. The trend guarantees it: the record is centred on
   2005 and the baseline on 2000, so the mean anomaly is
   $0.20\ \text{K/decade} \times 0.5\ \text{decade} = 0.10$ K — exactly the
   measured value. If someone asks "has it warmed?", the baseline choice is the
   first thing to check, and here it is a 0.1 K effect.
2. The residual standard deviation is **0.5488 K**. The imposed noise is 0.35 K, so
   the oscillation contributes in quadrature:
   $\sqrt{0.5488^{2} - 0.35^{2}} = 0.423$ K of regional signal. Nothing mysterious —
   but if you had assumed the residual was pure noise, you would have
   overestimated the noise by 57 %.
3. The climatology is a 12-member group on the `month` axis, so it is a
   *composite* over 30 years. During a warming trend, a composite over 30 years
   smears the trend into the climatology by about 0.03 K per decade of baseline
   length. A 10-year baseline would smear less and be noisier; a 50-year baseline
   would smooth more and bias the trend. **The baseline is an analysis choice with
   a quantifiable consequence.**

## 3. Trend recovery: the central measurement

Both weightings recover the imposed trend, and they differ in a much more
instructive way than "one is right".

```
naive    first/last = -0.2928 / +0.4925 K
weighted first/last = -0.2947 / +0.4718 K
naive    trend = +0.2002 K/decade (residual rms 1.72 mK)
weighted trend = +0.1997 K/decade (residual rms 165.78 mK)
IMPOSED trend = +0.2000 K/decade
  naive error    = +0.0002 K/decade (+0.08 %)
  weighted error = -0.0003 K/decade (-0.16 %)
  the two weightings differ by 0.49 mK/decade
```

Read the residual column carefully, because it is the lesson. The **unweighted**
mean has a residual rms of 1.72 mK; the **weighted** mean has 165.78 mK, a factor
of 96 larger. Neither number is an error. The explanation is that the imposed
oscillation has a pattern $\cos 2\phi$, and a uniform average over the
uniformly spaced latitude rows of $\cos 2\phi$ nearly vanishes:

$$\frac{1}{36}\sum_{i=1}^{36}\cos 2\phi_i = -1.9\times10^{-17},\qquad
\frac{\sum_i \cos\phi_i \cos 2\phi_i}{\sum_i \cos\phi_i} = 0.333,$$

so the oscillation cancels in the unweighted mean and does not cancel under
$\cos\phi$ weighting, which emphasises the low latitudes where $\cos 2\phi = +1$.
The unweighted series is therefore *smoother* — and it is smoother because it has
destroyed a real signal, not because it is better.

Three conclusions:

- **A trend can be recovered correctly by a computation that is wrong in other
  respects.** If the report contains only the trend, the unweighted pipeline looks
  superior. If the report contains the variability, it does not.
- **Agreement between two methods is not validation** unless the methods are
  expected to differ. Here they differ by 0.49 mK/decade, which is tiny, and by
  165 mK in residual rms, which is not.
- **The cancellation is a coincidence of $\cos 2\phi$.** For a pattern like
  $\cos\phi$ (the physically realistic polar amplification) the unweighted mean
  does not cancel it, and the trend is biased instead.

### 3.1 The trend must be linear, and the series must be complete

```
annual means of the RAW field: first = 12.047 K, last = 12.814 K
measured trend = +0.1997 K/decade (difference from the anomaly trend 0.00 mK/decade)
January+July only (80 samples): trend = +0.1446 K/decade
```

Two measured results with opposite signs of reassurance:

- **Complete annual means do not need deseasonalising.** Every annual mean
  averages exactly 12 months, so the seasonal cycle cancels to 0.00 mK/decade
  difference against the anomaly series. It is legitimate to fit the raw annual
  means — *provided every year has all twelve months*.
- **A subsampled series does.** Restricting to January and July — a real practice,
  if the other months are missing or snow-contaminated — gives **+0.1446 K/decade**,
  a **27.7 % underestimate** of the imposed 0.20. The residual seasonal term
  (in this synthetic, the two months fall at $t = 0$ and $t = 6$, where the cosine
  is $+1$ and $-1$, i.e. a non-constant offset when the sampling is aligned with a
  12-month cycle only at one phase) interacts with the linear fit.

The general rule, stated as arithmetic: fitting $y = a + bt$ to a series that also
contains $c\cos(\omega t + \psi)$ gives a slope biased by a term proportional to
$c\cos\psi$ unless $\psi$ is unknown-but-random across the record. Sampling two
months out of twelve fixes $\psi$ and removes the randomisation.

## 4. Spatial structure

```
time-mean zonal anomaly by latitude (K):
  -77.5 deg: +0.1279    -47.5 deg: +0.1009    -17.5 deg: +0.0751
   +7.5 deg: +0.0686    +32.5 deg: +0.0876    +62.5 deg: +0.1197
  +82.5 deg: +0.1319
5 S-5 N  trend: +0.1970 K/decade (error -3.03 mK/decade)
60-90 N  trend: +0.2016 K/decade (error +1.56 mK/decade)
```

The imposed trend is uniform in space, and both bands recover it to within
**3.03 mK/decade** (1.5 % of the imposed value, and about 2 % of the *signal*
each band contains).
The latitude dependence of the time-mean anomaly (+0.0686 to +0.1319 K) comes
from the oscillation, not the trend: the oscillation's $\cos 2\phi$ pattern is
positive at the equator and at the poles, negative at 45°, and its time mean over
a 4-year carrier inside a 20-year envelope is not zero over a 40-year record.

A correctly designed case study has both: a spatially uniform trend, so that
spatial biases in the trend estimator show up as departures from 0.20, and a
spatially structured oscillation, so that spatial weighting matters for
everything else.

## 5. A regression map, and a prediction that can be checked

The analysis question: which pixels follow the oscillation index? The measured
answer:

```
correlation of the monthly anomaly with the ENSO index:
  global maximum |r| = 0.8276 at lat 7.5, lon -102.5
  equatorial band (|lat| < 10 deg): max |r| = 0.8276
  mid-latitude band 40-60 N: max |r| = 0.5662
  prediction from the imposed amplitudes: deseasonalised index std = 0.3958 K,
  so the local signal std is 0.5352 K against 0.35 K of noise -> r = 0.8369
```

The prediction is elementary. At latitude $\phi$, the oscillation has local
standard deviation $1.4 \times |\cos 2\phi| \times \sigma_{\text{index}} =
1.4 \times 0.966 \times 0.3958 = 0.5352$ K. The noise is 0.35 K, uncorrelated with
the index, so

$$r = \frac{\sigma_{\text{signal}}}
  {\sqrt{\sigma_{\text{signal}}^{2} + \sigma_{\text{noise}}^{2}}}
= \frac{0.5352}{\sqrt{0.5352^{2} + 0.35^{2}}} = 0.8369,$$

against a measured 0.8276. **A 1.1 % agreement between an a-priori prediction and
a map maximum.** That is the standard this module asks of an analysis: the result
should be predictable from the model, and the measurement should confirm it.

It also explains why the mid-latitude maximum is 0.5662. At 45°, $\cos 2\phi$
passes through zero, so the correlation map changes sign; the largest |r| in the
40–60° band occurs at its edges, not at 45°.

### 5.1 Lag structure

```
lag + 0 months: area-weighted mean correlation = +0.2917
lag + 2 months: +0.2821      lag + 4 months: +0.2528
lag + 6 months: +0.2062      lag + 9 months: +0.1112
lag +12 months: +0.0003
```

The decay is monotone over about 9 months, not oscillatory, even though the index
contains a 4-year carrier. The reason is the **envelope**: the index is
$f(t)\sin(2\pi t/48)$ with a Gaussian packet of 20-year separation, so its
autocorrelation is that of a narrow-band but amplitude-modulated process — it
decorrelates as the packet turns over, not once per carrier period. A pure
sinusoid would show the oscillating lag structure; this index does not, and
observing which one you have is the diagnostic that distinguishes "the signal
propagated" from "the signal is periodic".

The `+12` value of 0.0003 is the arithmetic check: a 48-month carrier at a 12-month
lag is a quarter period, i.e. $\cos(\pi/2) = 0$.

## 6. Units and dimensional analysis

Climate analysis is unusually exposed to unit errors because anomalies,
temperatures and rates all carry different units for the same numbers.

- **K versus °C.** A temperature is in K or °C; a temperature *difference* is in
  kelvin in both systems, because the offset cancels in a subtraction. The
  demonstration prints temperatures in degC and differences in K, which is the
  correct convention and looks like sloppiness until you write
  $\Delta(15\ \text{°C}) = 15\ \text{K}$ explicitly.
- **K/decade versus K/year.** The trend was imposed as 0.20 K/decade, which is
  0.02 K/year. A rate quoted in the wrong per-time unit is wrong by 10×, and the
  fit itself is dimensionally agnostic: it returns whatever slope corresponds to
  the time axis you supplied. The demonstration derives the time axis from
  `(series.time - series.time[0]) / (365.2425 days)`.
- **Dimensionless weights.** $\cos\phi$ is dimensionless, so
  `weighted(w).mean()` returns the field's own units, K. An *area* weight in m²
  also yields K. Mixing the two in one pipeline is consistent only if the areas
  are proportional to the cosines, which is true for the sphere and off by up to
  0.8 % for 5° ellipsoidal bands (measured in lesson 03).
- **Correlation is dimensionless.** $r = 0.8276$ has no units, which is why it can
  be compared across fields with different amplitudes. Its square, $r^{2} = 0.685$,
  is the fraction of variance explained — that is the quantity with a physical
  reading.

## 7. What a real dataset would add

The synthetic cube is deliberately clean, and the honest way to present a case
study is to list what it omits.

- **A land–sea mask and a sea-ice mask.** A sea-surface-temperature product has
  no values over land, and the mask changes the area weighting of every global
  mean. The demonstration's cube is defined everywhere, which no real product is.
- **Quality flags and bias adjustments.** Real series mix buoys, ships and
  satellites; the instrument mix changes over time, and an uncorrected change of
  mix is indistinguishable from a trend.
- **A non-uniform time axis.** Monthly means are not equally spaced in days
  (28–31), so a "monthly" series has a small varying dt. A regression in
  months-per-step silently assumes equal spacing, which is wrong at the 1 %
  level per leap year.
- **A real fetch step.** Production code opens the cube from a NetCDF or Zarr
  store, often chunked and often only partly complete. The honest source for the
  real thing is the Copernicus Climate Data Store
  (<https://cds.climate.copernicus.eu>), ERA5 monthly reanalysis; this lesson
  never touches the network.
- **A file's own reproducibility record.** The imposed parameters here are in the
  script, one `default_rng(20260806)` away from being reproducible. A published
  cube needs a version, a DOI and a processing trace.

## 8. Python demonstration

The full script is
[`code/climate_data_cube_demo.py`](./code/climate_data_cube_demo.py):

```bash
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python \
    03-scientific-computing/08-gridded-geospatial-data/code/climate_data_cube_demo.py
```

It needs no disk write and no network. Every printed number is a measurement of
the cube it just built.

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| whole-record anomaly mean is +0.1000 K | the baseline is an analysis choice worth 0.1 K here |
| residual std 0.5488 K vs 0.35 K noise | assume the difference is signal, then verify |
| both weightings recover 0.20 K/decade to ≤0.16 % | a 40-year record is what buys that precision |
| residual rms 1.72 mK (naive) vs 165.78 mK (weighted) | the naive mean destroyed the oscillation |
| complete annual means need no deseasonalising | measured 0.00 mK/decade difference |
| Jan+Jul only gives 0.1446 K/decade | subsampling biased the trend by 27.7 % |
| measured max |r| = 0.8276 vs predicted 0.8369 | the pipeline is validated against its own model |
| lag correlation decays to 0.0003 at 12 months | the envelope, not the carrier, sets the memory |

> **Breaking exercise.** Change `SEASONAL_K` to 0.5 K and predict the new
> Jan+Jul-only trend bias before running. Then change the imposed trend to
> 0.40 K/decade and predict whether the baseline smear doubles.

## 9. Common mistakes

1. **Reporting a global mean without saying what was weighted.** Measured
   difference between two defensible global means: 0.49 mK/decade in the trend,
   165 mK in residual rms.
2. **Fitting a trend to a series that still contains a seasonal term.** Measured
   bias from a two-month subsample: 27.7 %.
3. **Assuming the residual is noise.** The residual is 0.5488 K against a 0.35 K
   noise floor; the oscillation accounts for the rest.
4. **Treating a 4-year carrier as the whole story.** The lag profile decays
   monotonically because the amplitude is modulated.
5. **Broadcasting a 1-D array against a 3-D array without checking the axis
   order.** It silently moved the time variation to longitude and produced
   |r| = 0.10 instead of 0.83.
6. **Comparing a correlation map's maximum to a model without stating the model.**
   The prediction here is two lines of arithmetic, which is what makes 0.8276
   against 0.8369 a validation rather than a coincidence.
7. **Quoting a trend from a grid whose cells are not equal-area** and whose
   weighting is unstated. Both numbers in Section 3 are defensible; only one is
   usually the one you meant.
8. **Forgetting that a monthly composite is a mean over an unequal number of
   month lengths.** The dates matter, not just the count.

## 10. Real-world applications

- **Global temperature series.** Every published global-mean anomaly depends on
  area weighting, the land–sea mask, the baseline and the interpolation of
  sparse coverage; the analysis in Section 3 is a miniature of that machinery.
- **ENSO and teleconnections.** Regression maps of a field onto an index are the
  standard diagnostic, and the two-line prediction in Section 5 is how a
  teleconnection claim is checked for plausibility.
- **Ocean heat content.** Weighted by cell volume rather than area, with a
  bathymetric mask; the weighting choice changes multi-decadal trends by tens of
  per cent.
- **Ice-sheet and glacier mass balance.** Area-weighted integrals over
  catchments whose boundaries are vector features — the vector–raster zonal
  statistics of [04 Vector-Raster Integration and Zonal Statistics](../09-geospatial-python/04-vector-raster-ops.md).
- **Model–observation comparison.** Regridding a model cube onto an observational
  grid, with a stated interpolation method, is where cubic-versus-linear becomes
  a scientific decision rather than a library default.

## 11. Further reading

- **Copernicus Climate Change Service, *Climate Data Store*.** Level:
  intermediate. <https://cds.climate.copernicus.eu> — the ERA5 monthly
  reanalysis this case study imitates; a real fetch requires registering for an
  API key.
- **Xarray, *Computation* and *GroupBy* user-guide sections.** Level:
  intermediate. <https://docs.xarray.dev> — `groupby("time.month")`,
  `resample`, and `weighted`.
- **CF Conventions Committee, *CF Conventions*.** Level: reference.
  <https://cfconventions.org> — the `cell_measures` and `cell_methods`
  attributes that state a weighting inside a file, so that it survives being
  passed to a colleague.
- **NOAA NCEI, *products and data pages*.** Level: intermediate.
  <https://www.ncei.noaa.gov> — long temperature and ocean datasets with real
  masks, real baselines and real quality flags.
- **Storch, H. von and Zwiers, F. W. (1999). *Statistical Analysis in Climate
  Research*. Cambridge University Press.** Level: advanced. Trend estimation,
  decorrelation, and the statistics of a finite record; Chapter 3 is the
  background for Section 3.

> Note on citations: bibliographic details are given so you can locate these
> works. This repository does not host or reproduce copyrighted text.

## 12. Related lessons

- [03 Dataset, Alignment, Broadcasting and GroupBy](./03-xarray-dataset.md) —
  the weighting and grouping machinery used here.
- [04 Chunking with Dask for Out-of-Core Analysis](./04-dask-chunking.md) —
  what a 0.25° version of this cube requires.
- [01 netCDF/HDF5 Formats and Self-Describing Data](./01-netcdf-and-hdf5.md) —
  how a real cube reaches you.
- [06 rasterio: Rasters, Windows, Masks and Reprojection](./06-rasterio-rasters.md)
  — the same ideas on a grid with a projected CRS.
- [03-04-06 Case Study: Earthquake Catalogue Wrangling](../04-pandas/06-earthquake-catalog-pandas.md)
  — the tabular case study in this folder.

## Exercises

[`exercises/05-climate-data-cube-exercises.md`](./exercises/05-climate-data-cube-exercises.md),
with full worked answers in
[`exercises/05-climate-data-cube-solutions.md`](./exercises/05-climate-data-cube-solutions.md).

## Self-assessment checklist

- [ ] I can state the five ingredients of the synthetic cube and their imposed
      amplitudes.
- [ ] I can explain why the whole-record anomaly mean is +0.1000 K.
- [ ] I can quote the recovered trend under both weightings and say which is
      closer to the imposed 0.20 K/decade.
- [ ] I can explain the 1.72 mK versus 165.78 mK residual difference.
- [ ] I can say when complete annual means can skip deseasonalising, and what
      happens when they are incomplete.
- [ ] I can predict a regression map's peak correlation from amplitudes and noise.
- [ ] I can explain why the lag correlation decays instead of oscillating.
- [ ] I can list four things a real cube would add that this one omits.
