---
id: 17-05-03
title: "Raster Data Model, Resolution and Resampling"
level: intermediate
prereqs: ["17-05-01", "03-08-06"]
tags: [gis, geospatial, remote-sensing, gis-fundamentals, raster, resampling, aliasing]
---

# Raster Data Model, Resolution and Resampling

A raster is an array plus a georeference. The array is cheap — arithmetic on it
is index arithmetic — and that cheapness is the entire reason remote sensing
works at planetary scale. The georeference is where the honesty lives: a raster
does not store where its cells are, it stores a six-number rule that generates
their positions, and every question of area, resolution and reprojection is a
question about that rule rather than about the data.

This lesson builds synthetic rasters, measures what resampling does to a signal,
and separates three errors that are routinely conflated: the area error of a
projection, the information loss of coarsening, and the aliasing that relocates
a wavelength instead of removing it.

All models and data in this module are **SYNTHETIC**. Every raster below is
generated in memory from a fixed seed. No satellite image, DEM or shapefile is
read, and no coordinate refers to a real place.

## Learning objectives

By the end of this lesson you will be able to:

1. **Read** an affine geotransform and **derive** cell centres, corners, extent
   and cell area from it.
2. **Verify** cell-area accounting ($n_{\text{cells}} \times A_{\text{cell}}$
   against the extent area) and **explain** why a regular grid makes area exact
   while the shape remains approximate.
3. **Choose** a resampling statistic for a stated purpose, and **measure** the
   error of block mean, nearest neighbour and block maximum against a fine grid.
4. **Convert** a categorical raster between resolutions without inventing values,
   and **quantify** the loss of a minority class.
5. **Apply** the Nyquist criterion, **predict** the alias of a sampled
   wavelength, and **demonstrate** that the alias is an equally valid signal for
   the samples.
6. **Quantify** the area error of a hard edge decision and **compare** it with a
   sub-pixel fractional estimate.
7. **Compute** how cell area varies with latitude on a geographic grid, and
   **explain** what a reprojection does to the geometry of the grid.

## Prerequisites

- [01 GIS Concepts: Layers, Attributes and Topology](01-gis-concepts.md) —
  layers, CRS and units.
- [03-08-06 Rasterio Rasters](../../03-scientific-computing/08-gridded-geospatial-data/06-rasterio-rasters.md) —
  reading a raster, the `transform` object and nodata with a library.
- [02-03-07 Dispersion](../../02-physics/03-oscillations-and-waves/07-dispersion.md) —
  waves, wavelengths and the idea of a limiting scale; used here for aliasing.

## 1. The georeference

A raster dataset is an array plus an **affine transform** that maps *(column,
row)* to *(x, y)*:

$$
\begin{pmatrix} x \\ y \end{pmatrix} =
\begin{pmatrix} a & b \\ d & e \end{pmatrix}
\begin{pmatrix} \text{col} \\ \text{row} \end{pmatrix} +
\begin{pmatrix} c \\ f \end{pmatrix}.
$$

The demonstration prints, for a synthetic $160 \times 240$ raster of 250 m
cells:

| quantity | value |
|---|---|
| array shape | 160 rows × 240 cols = 38 400 cells |
| dtype | float64 → 0.307 MB uncompressed |
| transform (a, b, c, d, e, f) | (250.0, 0.0, 400000.0, 0.0, −250.0, 5600000.0) |
| upper-left corner | (400000.0, 5600000.0) m |
| centre of cell (row, col) = (0, 0) | (400125.0, 5599875.0) m |
| lower-right corner | (460000.0, 5560000.0) m |
| extent | 60.0 km × 40.0 km |

Three facts that cost people days when they are missed:

* **$e$ is negative.** Row 0 is the *north* edge, so the y scale is $-250$ m.
  Dropping that sign flips the raster vertically with no error message.
* **The transform maps corners, not centres.** `transform * (0.5, 0.5)` is the
  centre of the top-left cell, exactly half a cell in from both edges.
* **The array alone does not know where it is.** Six numbers carry the whole
  georeference, and they are metadata that travel separately from the numbers in
  most file formats.

### 1.1 cell area is counting, not geometry

$$
n_{\text{cells}} A_{\text{cell}} = 38\,400 \times (0.25\ \mathrm{km})^2
= 38\,400 \times 0.0625\ \mathrm{km^2} = 2400.000\ \mathrm{km^2},
$$

and the extent area is $60 \times 40 = 2400.000\ \mathrm{km^2}$. The agreement is
*exact* — this is arithmetic, not measurement. A vector coverage of the same
region needs every boundary vertex and still only approximates the area. On a
grid the area is exact and the *shape* is the approximation; in a coverage the
shape is (nearly) exact and the area is computed from it. Each model is honest
about a different thing.

## 2. Resampling a continuous field

Coarsening by a factor $k$ replaces a $k \times k$ block of cells by one cell.
What that cell *means* is a decision:

| intended meaning of the coarse cell | statistic |
|---|---|
| estimate of the integral over the block | mean (or sum, with $A_{\text{cell}}$) |
| the value at the cell centre | nearest neighbour |
| a picture that looks like the original | any smooth interpolation |
| an extreme that must not be missed | max/min (a decision, not an average) |

The demonstration coarsens a smooth synthetic field by $4\times4$ (a 1 km grid)
and compares each product, upsampled back to the fine grid, with the truth:

| method | RMSE vs fine grid | bias | max abs error |
|---|---|---|---|
| block mean | 0.5875 | +0.0000 | 1.5336 |
| nearest (every $k$-th cell) | 0.9801 | −0.0066 | 3.0112 |
| offset subsample (every $k$-th + 1) | 0.6482 | +0.0011 | 1.9636 |
| block maximum | 1.2022 | +0.9990 | 3.0127 |

The block mean wins on both RMSE and bias — unsurprisingly, since the block mean
*is* the definition of the coarse cell's value. The block maximum has a bias of
almost exactly $+1$ on a field running from about 5 to 17: it is not an average
of the field at all. A single RMSE does not rank these products; what ranks them
is the question the coarse cell is supposed to answer. Reporting the method is
therefore part of the result, not a footnote.

### 2.1 Categorical rasters: mode survives, mean invents

For a class raster, the same choice is sharper. Coarsening three synthetic
classes by $4\times4$:

| statistic | result |
|---|---|
| fine class proportions | 50.00 %, 37.50 %, 12.50 % |
| mode (`4x4` plurality, ties to the smallest code) | 50.00 %, 49.42 %, **0.58 %** |
| mean of class codes | range 0.000–1.688, 1193 of 2400 cells **not an integer class** |

A mean of class codes produces a number that is not a class. Rounding it later
is an undeclared decision; keeping it makes the layer non-categorical and every
later lookup ("is this cell forest?") has to answer for it. Mode is the honest
reduction — and it still destroys the minority class, which falls from 12.50 % of
cells to 0.58 %. **A rare class does not survive coarsening**, and no choice of
statistic changes that; it is the same information-loss statement as §2, applied
to a discrete field.

## 3. Aliasing: a wavelength is relocated, not blurred

A grid of spacing $h$ can represent wavelengths longer than $2h$ — the **Nyquist
wavelength**. Anything shorter is *not removed*; it appears at a longer
wavelength that the samples cannot distinguish from it. For a true spatial
frequency $f = 1/L$ sampled at spacing $h$, the observed alias frequency is

$$
f_{\text{alias}} = \left| f - \frac{k}{h} \right|
\quad\text{for the integer } k \text{ that minimises it.}
$$

The demonstration samples a synthetic 4000 m sinusoid at six spacings, fits a
single sinusoid to the samples by least squares, and compares the fit with the
prediction:

| cell (m) | Nyquist (m) | predicted alias (m) | fitted period (m) | fitted amplitude |
|---|---|---|---|---|
| 250 | 500 | 4000 | 4001.9 | 1.000 |
| 500 | 1000 | 4000 | 4001.9 | 1.000 |
| 1000 | 2000 | 4000 | 4001.9 | 1.000 |
| 2000 | 4000 | 4000 | 4001.9 | 1.000 |
| 3000 | 6000 | 12000 | 12003.7 | 1.000 |
| 4000 | 8000 | DC (infinite) | undefined | 0.000 |
| 5000 | 10000 | 20000 | 19995.5 | 1.000 |

At 3000 m spacing the samples are fitted *exactly* — residual at machine
precision, amplitude 1.000 — by a 12 km wavelength. At 4000 m spacing the samples
alias onto zero frequency: they cannot tell the sinusoid from a constant, which
is why the fitted amplitude collapses to 0.000 and the period is undefined.

The consequence is not a loss of sharpness. It is a **second, equally valid
Earth**: a 12 m landscape detail sampled by a 30 m instrument is not smeared, it
is *relocated*, and no amount of post-processing recovers which of the two is
true. This is why the standard remedy is to remove short wavelengths
*optically* or *in the sensor* before sampling, and why a coarse product is not a
blurred version of a fine one.

## 4. Hard edges versus fractional cover: the area error

A categorical map asks "which class is this cell?" — a question about a whole
cell, answered from a measurement that is often a fraction. The demonstration
tests a synthetic circular lake of exactly 100.0000 km² (radius 5.6419 km) on
grids from 250 m to 8 km:

| cell (m) | hard-classified area | error | sub-pixel estimate | error |
|---|---|---|---|---|
| 250 | 99.5000 km² | −0.5000 % | 100.0406 km² | +0.0406 % |
| 1000 | 96.0000 km² | −4.0000 % | 99.8400 km² | −0.1600 % |
| 2000 | 104.0000 km² | +4.0000 % | 99.8400 km² | −0.1600 % |
| 4000 | 96.0000 km² | −4.0000 % | 100.4800 km² | +0.4800 % |
| 8000 | 128.0000 km² | +28.0000 % | 99.8400 km² | −0.1600 % |

Two facts:

* The hard-edge error does **not** shrink monotonically with cell size and its
  *sign flips* from grid to grid. It is set by the perimeter times roughly half a
  cell, divided by the area, and it is variance rather than bias: the perimeter
  here is $2\pi r = 35.45$ km and the area is 100 km², so at 1 km cells a random
  half-cell edge offset is worth about $35.45 \times 0.5/100 \approx 18\%$ in the
  worst case and cancels to a few per cent on average.
* The sub-pixel estimate stays within a few tenths of a per cent at every
  resolution. Fractional cover is not a refinement, it is the difference between
  a defensible area and a coin flip.

Reporting a class area from hard cells as a measurement is the commonest
quantitative error in raster GIS. The `mean` of a probability or fraction layer
is the correct statistic; the `mode` is the right answer to a different question.

## 5. NoData

A raster has no way to represent "no measurement" except by a reserved value,
and the reserved value is an attribute of the file rather than of the number.
The demonstration masks 5.12 % of cells and measures three consequences:

| choice | mean | consequence |
|---|---|---|
| exclude NoData | 10.158322 | correct, but the denominator varies cell by cell |
| treat NoData as 0 | 9.638237 | a −0.520085 bias, **−5.120 %** of the mean |

Casting NoData to zero is the most damaging silent decision in raster
processing: a 5 % change to the denominator that looks like a data reduction.
Coarsening adds a second decision. With a $4\times4$ block, 1338 of 2400 coarse
cells (55.75 %) contain at least one missing fine cell, so the two policies
diverge:

* **ignore** — every coarse cell is an average over a different, smaller set of
  fine cells (2400 of 2400 cells usable);
* **propagate** — any coarse cell touching a missing value is itself missing
  (1062 of 2400 cells usable, 44.25 % retained).

Neither policy is wrong; five per cent missing at the fine scale becomes 56 %
missing at the coarse scale under propagation, which is a large and
non-obvious consequence. The pipeline must state the policy and carry the count
of excluded cells *next to* the statistic.

## 6. Reprojection: a geographic grid is not an equal-area grid

Two things are true of a lon/lat grid, and both are quantitative.

**(i) A cell has no single area.** For a spherical Earth of radius
$a = 6\,378\,137$ m, a cell of $\Delta\phi$ in latitude and $\Delta\lambda$ in
longitude spans an area

$$
A = a^2 \Delta\lambda \left(\sin\phi_2 - \sin\phi_1\right).
$$

On the synthetic 60 × 40 grid of 0.05° cells centred at 40° N the demonstration
measures:

| row | cell area |
|---|---|
| southernmost | 24.4043 km² |
| middle | 24.0675 km² |
| northernmost | 23.7408 km² |
| ratio north/south | 0.97281 (−2.719 % over 2° of latitude) |

and for the same 0.05° cell elsewhere: 30.9801 km² at 0° N, 15.4783 km² at
60° N, a ratio of 0.49962 — which is $\cos 60° = 0.5$ to four digits, as the
small-angle limit requires. A per-cell mean used as a spatial mean is therefore
weighted wrongly, and the error is largest where the map is most distorted.

**(ii) A warp is a resampling.** Reprojecting that grid to UTM 31N gives a
56 × 48 grid of 4738.91 m cells, each exactly 22.457292 km² by construction:

| quantity | value |
|---|---|
| destination grid area | 60 365.201 km² |
| source nominal area | 57 770.105 km² |
| footprint growth | +4.492 % |
| destination cells outside the source footprint | 94 of 2688 (3.50 %) |
| value range after a nearest warp of a constant 1.0 source | [0.0, 1.0] |

The output grid is the bounding box of the warped footprint, so it necessarily
grows, and the extra cells are filled with nodata that **looks exactly like a
real zero** unless it is masked. The cell area of the output is a property of the
*projection*, chosen by the analyst, not of the measurement. Two consequences:
the destination is a new measurement rather than a re-expression of the old one,
and any area computed from it inherits the projection's area distortion.

## 7. Worked example: from a resolution to an area statement

A synthetic land-cover product has 30 m cells and a hard water class occupying
12 000 cells. The lake it represents is roughly 10 km² by an independent
estimate.

1. **Nominal area.** $12\,000 \times (0.030\ \mathrm{km})^2 = 12\,000 \times
   0.0009 = 10.800\ \mathrm{km^2}$.
2. **Perimeter term.** A 10 km² lake of compact shape has a perimeter of about
   11 km, so the hard-edge uncertainty is of order $P h / (2A) = 11 \times
   0.03/(2 \times 10.8) = 1.5\%$ — about $0.16\ \mathrm{km^2}$.
3. **Statement.** $10.80 \pm 0.16\ \mathrm{km^2}$, or 10.80 km² with a stated
   ±1.5 % edge term. Quoting 10.800 km² to four significant figures claims a
   precision 100× better than the geometry supports.
4. **What would tighten it.** Fractional cover in the boundary cells, or a
   finer-resolution product: the edge term scales as $h$, so a 10 m product
   reduces it to about 0.5 %.

## Assumptions and regime of validity

1. **The grid is regular and north-up.** An affine transform with non-zero `b`
   or `d` (rotation or shear) is legal but rare; every "row is a y value"
   shortcut fails on it.
2. **Cell values represent cell *interiors*.** A pixel-is-point raster stores
   values *at* nodes, not over areas, and the georeference convention differs.
   The demonstration measures the discrepancy as exactly half a cell: 125 m here,
   which is 6.25 m of positional bias for a 250 m product and 1.5 km for a 3 km
   product.
3. **Resampling is a model.** Every method above is an assumption about what
   happened between the samples. None is recoverable from the coarse product.
4. **The projection is the analyst's choice.** Areas and cell sizes in a
   projected raster are properties of that choice.
5. **NoData is metadata.** Its value, its meaning and the aggregation policy are
   all separate decisions.

## Python demonstration

[`code/raster_data_model_demo.py`](code/raster_data_model_demo.py) constructs
everything above in memory. It:

1. prints the affine transform, cell centres and corners, extent and cell-area
   accounting;
2. coarsens a smooth field four ways and measures RMSE, bias and maximum error
   against the fine grid;
3. coarsens a categorical field by mode and by mean and counts the invented
   values;
4. tests the alias prediction at seven spacings by least-squares fitting;
5. measures hard-edge and sub-pixel areas for a synthetic lake at five
   resolutions;
6. quantifies the pixel-is-area/pixel-is-point half-cell offset;
7. measures the NoData bias and the usable-cell loss under two aggregation
   policies;
8. reprojects a synthetic lon/lat raster with `rasterio` in an in-memory
   `MemoryFile` and reports cell areas, footprint growth and nodata fill.

```bash
cd 17-remote-sensing-gis/05-gis-fundamentals/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python raster_data_model_demo.py
```

Print-only, RAM-backed (no file is written), no network, exits 0.

## Exercises

[`exercises/03-raster-data-model-exercises.md`](exercises/03-raster-data-model-exercises.md)
and the
[solutions](exercises/03-raster-data-model-solutions.md):

- **★** Compute cell area, extent and a cell centre from a transform.
- **★★** Predict the alias of a stated wavelength at a stated spacing.
- **★★★** Design a coarsening recipe that preserves a rare class, and estimate
  the resolution at which it fails.

## Mastery checkpoint

Without notes:

> A 1000 × 1000 raster has 10 m cells and a transform with $e = -10$. **(a)**
> State its extent in km and its total area, and explain why the answer is exact.
> **(b)** You coarsen it to 100 m by taking the mean. A class occupying 4 % of the
> fine cells is worth how much of a coarse cell on average, and what do you expect
> its reported proportion to be after coarsening? **(c)** You then reproject it to
> another CRS. State two things that change and one thing that does not. **(d)** A
> colleague reports the same class as 6.5 % of the area from the reprojected hard
> raster. Give two mechanisms that could produce the difference.

A worked version of (a)–(c) is in the
[solutions](exercises/03-raster-data-model-solutions.md).

## Common pitfalls

1. **Forgetting the negative y scale.** The raster flips and looks plausible.
2. **Mixing corner and centre conventions.** A half-cell bias that survives every
   subsequent analysis.
3. **Comparing products with different resampling methods as if the difference
   were signal.** The methods differ by more than the change being studied.
4. **Coarsening a class raster with a mean.** It invents classes.
5. **Reporting a class area from hard cells.** The error is variance, not bias,
   and its sign changes between grids.
6. **Treating NoData as zero.** A silent percentage-point bias.
7. **Believing a warp is lossless.** It resamples, and it grows the footprint.

## Related modules

- [01 GIS Concepts: Layers, Attributes and Topology](01-gis-concepts.md).
- [02 Vector Data Model and Attribute Operations](02-vector-data-model.md) —
  the other data model, and why raster wins at scale.
- [04 Map Algebra and Raster Analysis](04-map-algebra.md) — operators on the
  arrays this lesson teaches you to georeference.
- [06-gis-fundamentals README](README.md).
- [03-08 Gridded Geospatial Data](../../03-scientific-computing/08-gridded-geospatial-data/README.md) —
  xarray, NetCDF and chunked arrays for larger rasters.
- [17-01-04 Resolution Concepts](../01-remote-sensing-physics/04-resolution-concepts.md) —
  spatial, spectral, temporal and radiometric resolution in the sensing chain.

## Self-assessment checklist

- [ ] I can write the affine mapping and find a centre and a corner.
- [ ] I can state the cell area, the extent area and why they agree exactly.
- [ ] I can choose a resampling statistic for a stated purpose.
- [ ] I can compute the alias of a wavelength at a given spacing.
- [ ] I can estimate the area error of a hard classification from a perimeter.
- [ ] I can state both NoData aggregation policies and their costs.
- [ ] I can explain what a reprojection preserves and what it changes.

