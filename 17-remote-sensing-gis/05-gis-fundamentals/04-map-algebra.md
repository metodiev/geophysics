---
id: 17-05-04
title: "Map Algebra and Raster Analysis"
level: advanced
prereqs: ["17-05-03", "17-05-02"]
tags: [gis, geospatial, remote-sensing, gis-fundamentals, map-algebra, focal-operators, slope, zonal-statistics]
---

# Map Algebra and Raster Analysis

Every raster calculation — a band ratio, a slope map, a moving average, a zonal
summary — is one of four operations: **local**, **focal**, **zonal** or
**global**. The classification is not taxonomy for its own sake. Each class has
its own error behaviour, its own dependence on the georeference, and its own way
of producing a plausible wrong number: local operators propagate noise
non-linearly, focal operators change the *support* of the measurement, zonal
operators depend on a weighting choice, and global statistics depend on a mask.

All models and data in this module are **SYNTHETIC**. The DEM, the temperature
surface, the reflectance bands and the zone map below are generated in memory
from a fixed seed. No real terrain, image or shapefile is used, and every number
is printed by the demonstration.

## Learning objectives

By the end of this lesson you will be able to:

1. **Classify** any raster expression as local, focal, zonal or global, and
   **state** which of the four georeference quantities it depends on.
2. **Propagate** measurement uncertainty through a ratio index analytically, and
   **verify** the result by Monte Carlo simulation.
3. **Explain** why a constant per-band noise level becomes a spatially varying
   noise level in every normalised difference index, and **locate** the worst
   pixels.
4. **Quantify** what a focal filter removes, and **state** the condition under
   which "smoothing reduces noise" is a measurement rather than a slogan.
5. **Choose** an edge policy for a focal operator and **measure** the artefact it
   introduces.
6. **Verify** a focal derivative operator against an analytically known
   surface, and **explain** the finite-difference attenuation factor $\mathrm{sinc}(d/L)$
   that makes a slope map scale-dependent.
7. **Compute** a zonal statistic with and without area weighting, and **state**
   the difference as a reporting decision.

## Prerequisites

- [03 Raster Data Model, Resolution and Resampling](03-raster-data-model.md) —
  the georeference, cell area and resampling.
- [02 Vector Data Model and Attribute Operations](02-vector-data-model.md) —
  zonal statistics are a vector/raster join.
- [02-01-02 Measurement Uncertainty](../../02-physics/01-measurement-and-physical-reasoning/02-measurement-uncertainty.md) —
  the error-propagation rule used in §2.

## 1. The four operator classes

| class | expression | example | depends on |
|---|---|---|---|
| local | $f(\text{in}_1[i,j], \text{in}_2[i,j], \dots)$ | band ratio, reclass | cell values only |
| focal | $f(\text{in}[i-k:i+k,\, j-k:j+k])$ | slope, smooth, filter | cell values and window shape |
| zonal | $f(\text{in}[\text{zone} = z])$ | mean elevation per basin | cell values, zone map, **cell areas** |
| global | $f(\text{in}[\text{all cells}])$ | basin mean, histogram | the mask |

The demonstration builds a synthetic raster set: a $180 \times 240$ grid of
200 m cells (48 km × 36 km), a DEM from 294.2 m to 961.8 m, a surface
temperature from 8.75 °C to 13.09 °C with a 6.5 K/km lapse rate, two reflectance
bands (NIR 0.260–0.396, red 0.110–0.178) and a three-zone map.

A practical rule for reading someone else's raster expression: name the class of
each term. A "local" formula that secretly contains a focal term (a smoothed
band, a filtered DEM) has a support larger than one cell, and every subsequent
statistic inherits it.

## 2. Local operators: uncertainty propagates through a ratio

The normalised difference vegetation index is a local operator:

$$
\text{NDVI} = \frac{\text{NIR} - \text{red}}{\text{NIR} + \text{red}},
\qquad
\frac{\partial \text{NDVI}}{\partial \text{NIR}} = \frac{2\,\text{red}}{(\text{NIR}+\text{red})^2},
\qquad
\frac{\partial \text{NDVI}}{\partial \text{red}} = -\frac{2\,\text{NIR}}{(\text{NIR}+\text{red})^2}.
$$

With independent per-band noise of standard deviation $\sigma$ on each band,

$$
\sigma_{\text{NDVI}}^2 =
\left(\frac{\partial \text{NDVI}}{\partial \text{NIR}}\right)^2 \sigma^2 +
\left(\frac{\partial \text{NDVI}}{\partial \text{red}}\right)^2 \sigma^2 .
$$

The synthetic field gives NDVI in $[0.3479, 0.4455]$ with mean 0.3897. Setting
$\sigma = 0.005$ (a 5-part-in-1000 reflectance error) the demonstration reports:

| quantity | value |
|---|---|
| analytic $\sigma_{\text{NDVI}}$, mean over the raster | 0.01622 |
| analytic $\sigma_{\text{NDVI}}$, maximum (row 116, col 0) | 0.02013 |
| pooled check $\sqrt{\overline{\mathrm{var}}}$ | 0.01630 |
| Monte Carlo standard deviation of the NDVI error, 20 000 draws | 0.01629 |
| agreement of the pooled pair | 0.056 % |
| worst cell: analytic vs Monte Carlo | 0.02013 vs 0.01998 (0.733 %) |
| mean amplification | 3.245 × the band noise |
| amplification at the darkest pixel | 4.03 × the band noise |

Two exact consequences follow from the derivatives, not from the simulation:

* The index is **least reliable in dark pixels**, because both derivatives carry
  $(\text{NIR}+\text{red})^{-2}$. The sensitivity is a property of the
  *reflectances*, not of the index's definition.
* A **constant** per-band noise level becomes a **spatially varying** noise level
  in every ratio index. No figure of the index shows this, and a classification
  threshold applied to the index inherits it: the same threshold is a different
  number of standard deviations in different parts of the image.

This is the general lesson for local operators: they are cheap, and the price is
that their uncertainty is a *field*, not a number.

## 3. Focal operators: what a filter actually removes

A $k \times k$ focal mean is a low-pass filter. The demonstration measures the
surviving standard deviation for the smooth synthetic DEM and for a white-noise
raster with the same grid:

| window | DEM sd (m) | retained | noise sd (m) | retained | exact $1/k$ |
|---|---|---|---|---|---|
| 3 | 148.967 | 99.9 % | 3.347 | 33.3 % | 33.3 % |
| 5 | 148.729 | 99.8 % | 2.015 | 20.0 % | 20.0 % |
| 11 | 147.556 | 99.0 % | 0.937 | 9.3 % | 9.1 % |
| 21 | 145.538 | 97.6 % | 0.493 | 4.9 % | 4.8 % |

For a white-noise field the surviving standard deviation is **exactly** $1/k$ —
an exact analytic result, reproduced here to within rounding — while for the
smooth DEM the same operator removes under 3 % of the standard deviation. Both
numbers are correct, and together they are the honest statement of "smoothing
reduces noise": the filter removes only the variance it can average out, which
means the variance at wavelengths **shorter than the window**. A DEM whose
variance sits at 6–8 km wavelengths is untouched by a $5 \times 5$ filter at
200 m spacing.

Two further properties:

* **Filtering is irreversible.** The removed variance cannot be recovered by any
  later operation. Every downstream statistic is a statistic of the filtered
  field.
* **A focal mean creates a new measurement support.** The output cell is an
  average over $k^2$ input cells, so its effective resolution is coarser. A slope
  computed from a $21 \times 21$ smoothed DEM is a slope over roughly 4 km, not
  over 200 m (§6).

### 3.1 Edge policies

Four policies, measured on the same $5\times5$ filter (the 2-cell collar is 1664
of 43 200 cells):

| policy | NaN cells | collar offset vs interior | change at the first corner cell |
|---|---|---|---|
| ignore (average what exists) | 0 | −0.056 m | +10.685 m |
| propagate (NaN if any input is NaN) | 1664 | +0.000 m | not defined (NaN) |
| reflect (mirror the interior) | 0 | −0.056 m | +12.822 m |
| constant (pad with 0) | 0 | −7.352 m | **−204.153 m** |

`ignore` keeps every cell but gives border cells a *smaller support*, so a
gradient computed across the collar mixes two window sizes. `propagate` keeps the
window honest and loses the whole collar. `reflect` invents interior values.
`constant` pads with zeros — and on a raster whose values are hundreds of metres,
a zero is not a mild approximation: it changes the first corner cell by more than
200 m. The edge policy is a choice, and **its size must be measured, not
assumed**; the collar offset of `ignore` (−0.056 m) is three orders of magnitude
smaller than the `constant` artefact, which is exactly the kind of thing that can
only be known by measuring.

## 4. Verifying a focal operator against a known answer

A slope map is computed from two focal derivatives. Horn's standard weights use
the eight neighbours with the pattern

$$
\left.\frac{\partial z}{\partial x}\right|_{i,j} =
\frac{(z_3 + 2z_6 + z_9) - (z_1 + 2z_4 + z_7)}{8\,\Delta},
\qquad
\left.\frac{\partial z}{\partial y}\right|_{i,j} =
\frac{(z_7 + 2z_8 + z_9) - (z_1 + 2z_2 + z_3)}{8\,\Delta},
$$

with $\Delta$ the cell size and the indices running around the $3\times3$ block.

The demonstration applies this to a synthetic plane whose gradient is known
exactly, $\partial z/\partial x = 0.05$, $\partial z/\partial y = 0.03$:

| quantity | value |
|---|---|
| exact slope | 3.3371107054° |
| mean Horn $\partial z/\partial x$ | 0.050000000000 (error 6.94 × 10⁻¹⁸) |
| mean Horn $\partial z/\partial y$ | 0.030000000000 (error 6.94 × 10⁻¹⁸) |
| mean Horn slope | 3.3371107054° (error 0.00°) |

A plane has zero second derivative, so the central-difference truncation term of
order $\Delta^2 z'''$ vanishes identically and only float64 round-off remains.
An operator that cannot reproduce an exactly known answer has no business being
applied to an unknown one — this is the *verification* step of
[19-07 Verification and Validation](../../19-numerical-modeling-hpc/07-verification-validation-uncertainty/README.md),
available here for free because the answer is analytic.

The same check on a paraboloid $z = 50\left((x-\bar{x})/1000\right)^2$ m, whose
Laplacian is exactly $2 \times 50/1000^2 = 1.0 \times 10^{-4}\ \mathrm{m^{-1}}$,
gives a five-point discrete Laplacian of $1.000000\times10^{-4}$ with an error of
$1.36 \times 10^{-20}$ on the interior. Curvature is a second derivative, so it
amplifies short wavelengths by $k^2$: the window that estimates a smooth
hillslope well will produce a curvature map dominated by whatever high-frequency
noise survives the DEM. The demonstration's near-exact agreement is a statement
about the *synthetic* surface — a real DEM's curvature is dominated by its noise,
and that is the useful warning, not the 20-digit agreement.

## 5. Scale dependence of slope

Because a centred difference is a finite-difference approximation, it attenuates
the gradient of a sinusoid. For a difference taken over a total spacing $d$
(i.e. sampling at $x \pm d/2$), the exact factor is

$$
\text{attenuation} = \mathrm{sinc}\!\left(\frac{d}{L}\right) =
\frac{\sin(\pi d/L)}{\pi d/L},
$$

where $\mathrm{sinc}$ is the normalised sinc. The demonstration verifies this on
a pure 6000 m sinusoid:

| total spacing $d$ (m) | measured attenuation | $\mathrm{sinc}(d/L)$ | difference |
|---|---|---|---|
| 400 | 0.9927051996 | 0.992705 | 1.11 × 10⁻¹⁶ |
| 800 | 0.9710122092 | 0.971012 | 1.11 × 10⁻¹⁶ |
| 1600 | 0.8870637931 | 0.887064 | 2.22 × 10⁻¹⁶ |
| 3200 | 0.5935615337 | 0.593562 | 1.11 × 10⁻¹⁶ |

Then it applies the same operator to the mixed synthetic terrain, whose analytic
mean gradient is 0.031660:

| window | spacing $d$ (m) | mean $|\nabla|$ | ratio to analytic | $\mathrm{sinc}(d/6000)$ | $\mathrm{sinc}(d/8000)$ | mean slope (°) | fraction above 2° |
|---|---|---|---|---|---|---|---|
| 3 | 400 | 0.031325 | 0.9894 | 0.99271 | 0.99589 | 1.794 | 35.1 % |
| 5 | 800 | 0.030625 | 0.9673 | 0.97101 | 0.98363 | 1.754 | 34.1 % |
| 9 | 1600 | 0.028251 | 0.8923 | 0.88706 | 0.93549 | 1.618 | 29.3 % |
| 17 | 3200 | 0.020800 | 0.6570 | 0.59356 | 0.75683 | 1.191 | 10.3 % |

The analytic field's own statistics are a mean of 1.813°, a standard deviation of
0.765°, a maximum of 3.287° and 36.4 % of cells above 2°.

Read the table as a warning about a common report: **the fraction of the
terrain steeper than 2° is 35.1 % at a 3-cell window and 10.3 % at a 17-cell
window.** The terrain did not change. A slope threshold crossed by changing the
window size is a property of the window, not of the ground, and the two
$\mathrm{sinc}$ columns bracket the measured ratio at every window because the
synthetic terrain is a mixture of a 6 km and an 8 km component. At the 3-cell
window the measured ratio sits 0.3 % below both factors — a centred difference
also shifts the phase of each component, and $|\nabla|$ is a nonlinear function
of the two shifted components, so the ratio is not a convex combination of the
two factors.

## 6. Zonal statistics: the weighting choice

A zonal statistic is a per-zone aggregation of a raster, restricted to the cells
whose zone identifier matches. For three synthetic zones:

| zone | n cells | area (km²) | mean elevation (m) |
|---|---|---|---|
| 1 | 21 600 | 864.000 | 585.404 |
| 2 | 10 800 | 432.000 | 551.874 |
| 3 | 10 800 | 432.000 | 791.874 |

* unweighted mean of the zone means: **643.050639 m**
* area-weighted mean: **628.638889 m**
* global mean of all cells: **628.638889 m**

The area-weighted mean equals the global cell mean here because every cell has
the same area. The unweighted mean of means is 2.2925 % higher, and it is the
number a summary table usually reports. The difference is a reporting choice, not
an error:

$$
\bar z_{\text{unweighted}} - \bar z_{\text{weighted}} = \text{a term proportional to
the covariance between zone size and zone mean},
$$

which is precisely the quantity a reader needs: if the small zones are also the
high ones (a summit zone, a narrow valley), the unweighted mean will
systematically misrepresent the region.

Three further decisions are hidden in a zonal statistic:

1. **Cell assignment at zone boundaries.** A cell whose centre falls in the zone
   counts fully; a cell that straddles the boundary is split in the cell-centre
   convention and assigned whole in the majority convention. The difference is
   the same edge term as §4 of
   [03 Raster Data Model](03-raster-data-model.md).
2. **NoData policy.** Whether a zone's statistic uses cells that are missing in
   the *value* raster but present in the zone raster.
3. **Area weighting.** Every cell is not equal-area if the raster is geographic
   (§6 of [03](03-raster-data-model.md)).

## 7. Global statistics, masks and thresholds

A global statistic is global *over the mask*. The demonstration thresholds the
DEM at its 60th percentile (676.222 m), which by construction selects
40.00 % of cells, and then perturbs the threshold:

| threshold (m) | shift | masked fraction | mean of the subset (m) |
|---|---|---|---|
| 666.222 | −10.0 | 42.13 % | 775.002 |
| 675.222 | −1.0 | 40.24 % | 779.912 |
| 676.222 | 0.0 | 40.00 % | 780.527 |
| 677.222 | +1.0 | 39.80 % | 781.046 |
| 686.222 | +10.0 | 37.98 % | 785.810 |

A threshold converts a continuous field into a binary map with a **step
response**, and the reported mean of the selected subset moves by 0.8 % for a
1.5 % change in the mask. A threshold chosen as a *percentile* is
self-normalising: it always selects exactly the stated fraction, whatever the
data, which is convenient and also a way of hiding the fact that the physical
threshold moved between two epochs. A threshold chosen in physical units is
reproducible across epochs, and that is usually what a change study needs.

## 8. Worked example: a weighted overlay, and why it is not a measurement

Take three synthetic inputs — DEM, surface temperature (reversed so that warmer
is better) and NDVI — and combine them with fixed weights
$\mathbf{w} = (0.5, 0.3, 0.2)$, $\sum w_i = 1$. Two defensible normalisations:

* **min–max over the study area**: $\tilde z_i = (z_i - \min z_i)/(\max z_i - \min z_i)$;
* **a fixed physical range**: $\tilde z_i = \mathrm{clip}((z_i - l_i)/(h_i - l_i), 0, 1)$
  with stated $(l_i, h_i)$.

Both give a score in $[0,1]$ and the weights are identical. The demonstration
reports:

| quantity | value |
|---|---|
| min–max score range | 0.2306 – 0.7291 |
| physical-range score range | 0.2808 – 0.7245 |
| Pearson correlation of the two score rasters | 0.769723 |
| fraction of cells in the same score decile | 23.083 % |
| argmax under min–max | row 160, col 218 (score 0.7291) |
| argmax under physical range | row 160, col 190 (score 0.7245) |
| distance between the two best cells | 5.600 km |

The correlation is 0.77, so the two maps agree broadly; the best cell moves
5.6 km, so they disagree where it matters. The reason is structural: a min–max
normalisation rescales each input by whatever range the study area happens to
contain, so **adding one extreme pixel to the study area changes every score in
the map**. A physical range is arbitrary but *fixed*, and therefore reproducible,
reviewable and falsifiable.

This is the honest core of map algebra in decision-making: a weighted overlay is
a decision rule, not a measurement. It must carry its normalisation, its ranges
and its weights, or it cannot be reviewed — and the weights themselves are the
subject of
[05 Multi-Criteria Decision Analysis](../06-geospatial-analysis-advanced/05-multicriteria-decision.md).

## Assumptions and regime of validity

1. **The grid is regular and north-up.** Every focal and zonal statement above
   assumes the transform of §1 of [03 Raster Data Model](03-raster-data-model.md).
2. **Cells are equal-area.** Zonal area weighting is only meaningful after
   checking the CRS; on a geographic raster the weighting is latitude-dependent.
3. **Inputs are independent.** The error propagation in §2 assumes uncorrelated
   band noise; correlated errors (atmospheric over-correction is spatially
   correlated) violate it, and the true uncertainty is larger.
4. **Noise is stationary.** A constant per-band $\sigma$ is a modelling choice.
   Real sensors have signal-dependent noise, which changes the amplification
   field.
5. **The DEM is the terrain.** A focal slope is a slope *of the DEM*, including
   its sampling, its interpolation and its noise. The verification in §4 is
   against an analytic surface, not against a real one.
6. **The mask is exogenous.** A global statistic is conditional on a mask that
   is usually chosen by the analyst; the mask choice moves the number (§7).

## Python demonstration

[`code/map_algebra_demo.py`](code/map_algebra_demo.py) builds every raster above
in memory with NumPy. It:

1. assembles the synthetic raster set and prints the four operator classes on
   it;
2. computes NDVI, its analytic uncertainty field, a Monte Carlo check, and the
   amplification factor at the mean and worst cells;
3. measures the variance removed by $3\times3$ to $21\times21$ focal means on
   the DEM and on white noise, and tests the exact $1/k$ result;
4. measures four edge policies for a $5\times5$ filter including the corner-cell
   artefact of zero padding;
5. verifies Horn's gradients against an analytic plane and a five-point
   Laplacian against an analytic paraboloid;
6. verifies the $\mathrm{sinc}(d/L)$ attenuation exactly, then measures the
   scale dependence of slope on the synthetic terrain at four window sizes;
7. computes zonal means and the area-weighted versus unweighted difference;
8. measures the threshold sensitivity of a masked global mean;
9. compares two normalisations of the same weighted overlay and reports the
   correlation, the decile agreement and the displacement of the best cell.

```bash
cd 17-remote-sensing-gis/05-gis-fundamentals/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python map_algebra_demo.py
```

Print-only, no files, no network, exits 0.

## Exercises

[`exercises/04-map-algebra-exercises.md`](exercises/04-map-algebra-exercises.md)
and the
[solutions](exercises/04-map-algebra-solutions.md):

- **★** Propagate a stated band uncertainty through a normalised difference.
- **★★** Derive the focal-filter variance reduction for white noise and check it
  against the measured table.
- **★★★** Design a slope product with a stated support and demonstrate its
  stability under a change of window.

## Mastery checkpoint

Without notes:

> A study computes NDVI from two synthetic bands and a slope map from a synthetic
> DEM. **(a)** With per-band $\sigma = 0.004$ at NIR $= 0.30$ and red $= 0.10$,
> compute $\sigma_{\text{NDVI}}$ analytically. **(b)** The same NDVI is computed
> at NIR $= 0.10$, red $= 0.03$. Compute the amplification and state in one
> sentence why a single NDVI threshold cannot have one uncertainty. **(c)** A
> colleague smooths the DEM with a $9\times9$ filter at 200 m spacing and reports
> the slope map as unchanged. Using the $\mathrm{sinc}$ factor, state what the
> filter does to a 6 km wavelength and what it does to a 400 m one. **(d)** The
> zonal mean for one zone is 0.4 % different under area weighting. Give the two
> mechanisms that could produce that difference.

A worked version of (a)–(c) is in the
[solutions](exercises/04-map-algebra-solutions.md).

## Common pitfalls

1. **Quoting a single uncertainty for a ratio index.** It is a field.
2. **Smoothing to "reduce noise" without checking the noise's wavelengths.**
3. **Leaving the edge policy unstated.** It is a decision with a measurable size.
4. **Comparing slope maps computed with different windows.** The difference is
   arithmetic, not geology.
5. **Reporting an unweighted mean of zone means as the regional mean.**
6. **Choosing a threshold by percentile and comparing it across epochs.**
7. **Presenting a weighted overlay as a measurement.** It is a decision rule;
   report its normalisation and ranges.
8. **Forgetting that curvature amplifies short-wavelength noise by $k^2$.**

## Related modules

- [03 Raster Data Model, Resolution and Resampling](03-raster-data-model.md).
- [05 Spatial Interpolation: IDW, Kriging, Splines](05-spatial-interpolation-gis.md) —
  what to do when the raster is not a regular grid.
- [06-gis-fundamentals README](README.md).
- [21-01-06 Spatial Statistics](../../21-statistics-bayesian-ml/01-statistics-in-practice/06-spatial-statistics-geo.md) —
  the inferential machinery behind zonal comparisons.
- [Advanced Geospatial Analysis](../06-geospatial-analysis-advanced/README.md) —
  terrain, hydrology and multi-criteria analysis built on these operators.

## Self-assessment checklist

- [ ] I can classify any raster expression into the four operator classes.
- [ ] I can propagate band uncertainty through a ratio analytically and check it
      by simulation.
- [ ] I can predict how much variance a focal mean removes for a given input
      spectrum.
- [ ] I can verify a derivative operator against a known surface.
- [ ] I can compute the $\mathrm{sinc}$ attenuation of a slope with window size.
- [ ] I can compute a zonal statistic with and without area weighting.
- [ ] I can state the normalisation and ranges of a weighted overlay.

