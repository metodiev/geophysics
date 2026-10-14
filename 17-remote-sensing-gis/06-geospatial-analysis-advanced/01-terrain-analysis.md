---
id: 17-06-01
title: "Terrain Analysis: Slope, Aspect, Curvature, Flow Accumulation"
level: graduate
prereqs: ["17-05-03", "17-05-04", "03-03-07"]
tags: [gis, geospatial, remote-sensing, geospatial-analysis-advanced, terrain, dem, slope, flow-accumulation]
---

# Terrain Analysis: Slope, Aspect, Curvature, Flow Accumulation

A digital elevation model is a *sampling* of a surface, and every terrain
attribute — slope, aspect, curvature, flow accumulation — is a property of the
sampling as much as of the ground. This lesson treats each of them as a
derivative operator with a stated support, verifies each against an analytically
known surface where one exists, and measures what a change of cell size does to
the answer. Two results organise the whole lesson: a focal operator cannot
represent a field that varies faster than its window, and a map of any
difference-based metric is a statement about the processing chain.

All models and data in this module are **SYNTHETIC**. The terrain, the cone, the
paraboloid and every statistic below are generated in memory from a fixed seed.
No real DEM, catchment or coordinate is used.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** slope and aspect from Horn's 3×3 weights and **state** the sign
   convention that makes aspect correct on a north-up grid.
2. **Verify** a derivative operator against a cone and a paraboloid where the
   answer is analytic, and **state** the tolerance achieved.
3. **Explain** why aspect is a circular quantity and **compute** the circular
   mean and spread instead of the arithmetic mean.
4. **Diagnose** which part of a curvature or slope field is noise by comparing a
   measured field with the analytic value of a known surface.
5. **Explain** priority-flood filling, **measure** the volume it adds, and
   **state** why every flow-accumulation map is a map of the filled surface.
6. **Verify** a D8 flow-accumulation field by conservation, and **state** what
   that check does and does not test.
7. **Quantify** the resolution dependence of slope, ruggedness and hypsometry,
   and **choose** a metric whose stability matches the comparison being made.

## Prerequisites

- [03 Raster Data Model, Resolution and Resampling](../05-gis-fundamentals/03-raster-data-model.md) —
  the georeference and the cell size every derivative depends on.
- [04 Map Algebra and Raster Analysis](../05-gis-fundamentals/04-map-algebra.md) —
  focal operators, the edge policy and the $\mathrm{sinc}$ attenuation that this
  lesson extends.
- [03-03-07 ndimage and Linear Algebra](../../03-scientific-computing/03-scipy/07-ndimage-linalg.md) —
  the smoothing and array machinery used by the demonstration.

## 1. Slope and aspect from a 3×3 window

The standard terrain derivatives use Horn's weighted differences over the eight
neighbours:

$$
\left.\frac{\partial z}{\partial x}\right|_{i,j} =
\frac{(z_3 + 2z_6 + z_9) - (z_1 + 2z_4 + z_7)}{8\,\Delta},
\qquad
\left.\frac{\partial z}{\partial y}\right|_{i,j} =
\frac{(z_1 + 2z_2 + z_3) - (z_7 + 2z_8 + z_9)}{8\,\Delta},
$$

where $\Delta$ is the cell size and the indices run around the block. Then

$$
\text{slope} = \arctan\!\sqrt{g_x^2 + g_y^2},
\qquad
\text{aspect} = \operatorname{atan2}\!\left(-g_x,\,-g_y\right) \bmod 360°,
$$

with aspect measured as a compass azimuth (0° = north, increasing clockwise)
pointing **downslope**.

The sign convention is worth stating explicitly because it fails silently. Row
index increases *southwards*, so the north-up derivative takes the **north row
minus the south row**. Getting this wrong leaves the slope map unchanged — slope
is a magnitude — and reverses every aspect by 180°. The demonstration makes the
point by construction: with the sign corrected, the aspect error on a synthetic
cone is 0.0009° on average; with the sign reversed it is 179.999°.

## 2. Verification on a cone

A cone $z = 500 - m r$ with $m = 0.25$ has $|\nabla z| = 0.25$ everywhere except
at the apex, so

$$
\text{slope} = \arctan(0.25) = 14.0362434679°\ \text{exactly.}
$$

The demonstration measures, over the 52 963 cells with $r > 5$ cells:

| quantity | value |
|---|---|
| mean measured slope | 14.0352855720° |
| max deviation from the analytic slope | 0.1212° |
| mean aspect error | 0.000854° |
| median aspect error | 0.000239° |
| max aspect error | 0.1146° |
| cells with aspect error > 1° | 0 of 52 963 |
| the 29 cells within 3 cells of the apex | mean 6.33°, max 180.00° |

Both statistics are effectively exact away from the apex, and the failures are
**localised at the apex**, where the true azimuth sweeps through 360° inside a
single 3×3 window. That is the general statement about focal operators: they
cannot represent a field that varies faster than the window, and where the
field violates the assumption the error is large and structured, not random.

## 3. Aspect is a circular quantity

A compass direction lives on a circle, and the arithmetic mean of circular data
is not defined. Two synthetic headings of 1° and 359° have:

| statistic | value | interpretation |
|---|---|---|
| arithmetic mean | 180.000° | points **south** — wrong |
| circular mean | 360.000° | points north — right |

On the synthetic terrain, the 53 043 cells steeper than 5° give an arithmetic
mean aspect of 180.001° (an artefact of the bipolar distribution) and a circular
mean of 323.626°, with a circular spread $1-R = 0.9946$ where $R$ is the
resultant length. A spread near 1 means the aspects are close to uniformly
distributed, which the octant histogram confirms:

```
octant counts (N, NE, E, SE, S, SW, W, NW): [4025, 9236, 9256, 3916, 3933, 9267, 9405, 4005]
```

The substitute for a "mean and standard deviation of aspect" is the resultant
length $R$ plus a histogram or a rose diagram, and every circular statistic has
to be computed that way. A t-test on aspect, or a regression of aspect on
elevation, is undefined; the same questions have to be posed on $\sin$ and
$\cos$ of the direction, or on the fold of the circle that is physically
meaningful.

## 4. Curvature: an exact operator, and a noisy product

The five-point discrete Laplacian of a paraboloid
$z = 50\left((x-\bar x)/1000\right)^2$ m is

$$
\nabla^2 z = \frac{z_{i+1,j} + z_{i-1,j} + z_{i,j+1} + z_{i,j-1} - 4z_{i,j}}{\Delta^2}
\to 2 \times \frac{50}{1000^2} = 1.0 \times 10^{-4}\ \mathrm{m^{-1}},
$$

and the measurement gives $1.000000 \times 10^{-4}$ with an error of
$2.41 \times 10^{-18}$ m⁻¹ on the interior. That is a **verification**: the
operator is implemented correctly.

On the synthetic terrain, the comparison with the analytic Laplacian of the
noise-free surface is more informative:

| quantity | value |
|---|---|
| analytic Laplacian, RMS | 2.158544 × 10⁻⁴ m⁻¹ |
| measured on the noise-free DEM | 2.137450 × 10⁻⁴ m⁻¹ |
| measured on the noisy DEM (σ = 1 m, one-cell correlated) | 2.138869 × 10⁻⁴ m⁻¹ |
| excess attributable to the noise | 7.79 × 10⁻⁶ m⁻¹ |
| white-noise prediction $\sigma \, \sqrt{20}/\Delta^2$ | 5.0 × 10⁻⁵ m⁻¹ |
| after a 3-cell smoothing of the noisy DEM | 1.271464 × 10⁻⁴ m⁻¹ (59.4 % of raw) |

Three readings, all measured:

1. The noise excess is small (0.4 % of the RMS) **because the synthetic noise is
   correlated over one cell**; the white-noise prediction is more than six times
   larger. A noise field's spectrum, not its standard deviation, decides how much
   curvature it contributes — the same statement as the focal-filter result in
   [04 Map Algebra](../05-gis-fundamentals/04-map-algebra.md).
2. Curvature amplifies short wavelengths by $k^2$, so the raw curvature map is
   dominated by whatever the DEM carries at the cell scale.
3. A 3-cell smoothing removes 41 % of the curvature RMS — and that removed part
   is **terrain** curvature, not noise (the noise contribution is 0.4 %).
   Smoothing changes the answer, so a curvature map is a statement about the
   processing as much as about the ground, and its radius of support must be
   reported with it.

## 5. Priority-flood pit filling

Hydrological analysis cannot proceed on a surface with closed depressions: a cell
with no lower neighbour has no flow direction, and the accumulation stops there.
The standard fix is a **priority flood** (Barnes et al., 2014): grow a water
surface outwards from the domain edges, always expanding from the lowest frontier
cell, raising each interior cell to at most the level of the lowest path to the
boundary.

Two details matter in the implementation and both are visible in the numbers:

* **An epsilon is added at each step.** Without it, filled areas are *exactly
  flat*, and a D8 rule that requires a strictly lower neighbour finds no
  direction at all: the demonstration's first attempt left 15 190 cells with no
  downslope neighbour. With $\varepsilon = 10^{-3}$ m the filled surface has a
  strictly monotone path to the outlet and only 28 cells (the domain edge and a
  few ties) remain.
* **The fill is large and it is an artefact.** Measured: 15 185 of 54 000 cells
  raised (28.12 %), maximum raise 317.73 m, mean raise where raised 86.27 m,
  total volume added $5.24 \times 10^{10}$ m³. The synthetic surface has no real
  depressions; the fill is removing interpolation noise between samples of a
  3.5 km-wavelength surface at 200 m spacing. Every flow-accumulation map is a
  map of the *filled* surface, so this volume is a systematic component of every
  downstream discharge.

## 6. D8 flow accumulation and a conservation check

D8 gives every cell one receiver: the neighbour with the steepest descent.
Accumulation is then a topological count, computed by processing cells in
decreasing filled elevation and pushing each cell's total to its receiver. On the
synthetic DEM:

| quantity | value |
|---|---|
| maximum accumulation | 12 385 cells (495.40 km²) |
| cells with accumulation > 1 | 46 246 (85.64 %) |
| cells with a downslope receiver | 53 972 (99.95 %) |
| outlets (no receiver) | 28 |
| headwater cells | 7 726 |
| sum of accumulation at the outlets | 54 000 cells |
| conservation residual | 0.0 cells (0.000000 %) |

The check is exact and it costs nothing:

$$
\sum_{\text{outlets}} \text{acc}
= \sum_{\text{all cells}} 1 = n_{\text{cells}},
$$

because each cell contributes exactly 1 and drains to exactly one outlet. It
catches the two standard D8 bugs — a direction that points uphill, and a receiver
that is its own source (a cycle) — either of which breaks the sum by a visible
amount. What it does **not** test: with 200 m cells and a monotone fill the
drainage net is a tree, while real channels bifurcate and rejoin; and the count
is an *area*, not a discharge, until it is multiplied by an effective rainfall.

## 7. Scale dependence: the same terrain at four cell sizes

Coarsening the DEM by averaging and recomputing the slope statistics:

| cell (m) | cells | mean slope (°) | sd (°) | fraction > 5° | fraction > 10° |
|---|---|---|---|---|---|
| 200 | 54 000 | 6.885 | 3.523 | 64.7 % | 20.8 % |
| 400 | 13 500 | 6.463 | 3.306 | 59.5 % | 14.8 % |
| 800 | 3 375 | 5.078 | 2.587 | 46.9 % | 3.3 % |
| 1600 | 814 | 2.595 | 0.900 | 0.0 % | 0.0 % |

Coarsening by 8× removes 62 % of the mean gradient and **all** of the cells
steeper than 10°. The terrain did not change. This is the same
$\mathrm{sinc}(d/L) = \sin(\pi d/L)/(\pi d/L)$ attenuation measured in
[04 Map Algebra](../05-gis-fundamentals/04-map-algebra.md), applied by averaging
instead of by a wider window, and it is why a "mean slope of the region" is
meaningless without a stated cell size. A slope threshold crossed by changing
the cell size is a property of the grid, not of the ground — and hazard or
suitability maps built on such a threshold inherit the grid's decision.

## 8. Ruggedness versus hypsometry: which metric is portable

| cell (m) | hypsometric integral | mean slope (°) | mean terrain ruggedness index (m/m) |
|---|---|---|---|
| 200 | 0.5005 | 6.885 | 0.11078 |
| 400 | 0.4969 | 6.463 | 0.10766 |
| 800 | 0.4857 | 5.078 | 0.09580 |
| 1600 | 0.4888 | 2.595 | 0.06351 |

Across a 64-fold change in cell count the hypsometric integral moves by 2.3 %
while the slope-derived ruggedness index falls by 43 %. Metrics built from
*differences between neighbouring cells* are resolution-dependent; metrics built
from *elevation distributions* much less so. A comparison of ruggedness between
two regions therefore requires one stated cell size, and a comparison of
hypsometry nearly does not. The choice of metric is part of the hypothesis, not a
presentational preference.

## 9. Worked example: is a slope threshold real?

A synthetic study reports that 64.7 % of a region is steeper than 5°, from a
200 m DEM.

1. **Reproduce the number.** Horn's 3×3 weights, the stated cell size and the
   stated edge policy are needed; with all three, the number is reproducible.
2. **Test its stability.** At 800 m the same terrain gives 46.9 % and at 1600 m
   0.0 %. So the claim "64.7 % is steeper than 5°" is a claim about a *200 m*
   DEM.
3. **Quantify the arithmetic part.** The analytic mean slope of the synthetic
   surface is 7.0018° against the measured 6.8854° — a 1.7 % deficit from the
   finite difference alone at 200 m. At 800 m the $\mathrm{sinc}$ factor at the
   dominant 3.5 km wavelength is $\sin(\pi \cdot 800/3500)/(\pi \cdot 800/3500)
   = 0.935$; the measured mean slope ratio is $5.078/7.002 = 0.725$, the
   remainder being further smoothing by 4×4 block averaging.
4. **Statement.** "At 200 m cells, 64.7 % of the synthetic region has Horn slope
   above 5°; the fraction falls to 46.9 % at 800 m and 0.0 % at 1600 m, so the
   threshold applies to the 200 m product." That is reviewable. "64.7 % is
   steep" is not, because *steep* has no cell size.

## Assumptions and regime of validity

1. **The DEM is a faithful sample of the surface at the cell scale.** Every
   derivative assumes the sampling interval resolves the terrain; §7 measures
   what happens when it does not.
2. **The surface is $C^2$ at the window scale.** A cliff, a quarry face or a
   road cut violates it, and Horn's weights then return an average of two
   different slopes.
3. **The edge policy is stated.** A focal operator loses $k/2$ cells on each
   side, or invents them; the collar is a systematic region, not a random one.
4. **The fill is accepted as part of the model.** It changes the surface by tens
   of metres here (§5), and it is not optional for D8.
5. **The flow rule is declared.** D8 sends all flow to one neighbour; D-infinity
   or multiple-flow-direction algorithms spread it, and they give different
   accumulation fields on the same DEM.
6. **The vertical datum is a single surface.** A DEM mosaicked from two sources
   with a datum offset produces spurious slopes at the seam, and the artefact
   looks like a linear feature.
7. **Noise is characterised.** The demonstration *knows* its noise (σ = 1 m,
   correlated over one cell) and can therefore separate signal from noise in §4;
   on a real DEM the same separation requires an independent error model.

## Python demonstration

[`code/terrain_analysis_demo.py`](code/terrain_analysis_demo.py) builds
everything above in memory. It:

1. assembles the synthetic terrain, reports its statistics and counts its pits;
2. verifies Horn slope and aspect on an analytic cone and localises the failure
   at the apex;
3. demonstrates the circular nature of aspect with a two-value example and on the
   terrain;
4. verifies the discrete Laplacian on a paraboloid, then separates signal from
   noise in the terrain curvature;
5. implements priority-flood filling with flat resolution and measures the volume
   it adds;
6. computes D8 accumulation and verifies it by conservation;
7. measures the resolution dependence of slope at four cell sizes;
8. compares the stability of hypsometry and ruggedness.

```bash
cd 17-remote-sensing-gis/06-geospatial-analysis-advanced/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python terrain_analysis_demo.py
```

Print-only, no files, no network, exits 0.

## Exercises

[`exercises/01-terrain-analysis-exercises.md`](exercises/01-terrain-analysis-exercises.md)
and the
[solutions](exercises/01-terrain-analysis-solutions.md):

- **★** Compute the Horn gradient and slope at a stated 3×3 block.
- **★★** Derive the $\mathrm{sinc}$ attenuation of a slope for a stated cell
  size and wavelength, and predict the measured fall.
- **★★★** Design a noise-robust curvature product with a stated support and
  justify the smoothing by the noise spectrum.

## Mastery checkpoint

Without notes:

> A synthetic 30 m DEM covers 20 km × 10 km. **(a)** Give the cell count, the cell
> area and the total area. **(b)** A slope map from it reports that 30 % of the
> region exceeds 15°. State two checks you would run before believing the number,
> and predict the direction of the change in each. **(c)** The DEM contains a
> 1 m-deep closed depression of 20 cells. State what the D8 algorithm does with
> it, what the fill does, and what volume the fill adds. **(d)** An aspect map
> from the same DEM has a mean of 179°. Explain why that number is not a
> statistic about the terrain.

A worked version of (a)–(c) is in the
[solutions](exercises/01-terrain-analysis-solutions.md).

## Common pitfalls

1. **Ignoring the y sign convention.** Slope survives, aspect is reversed.
2. **Averaging aspect arithmetically.** Use the resultant length and a rose.
3. **Reading a raw curvature map as geology.** Curvature amplifies cell-scale
   noise by $k^2$.
4. **Forgetting the fill in a flow-accumulation result.** The map is of the
   filled surface.
5. **Reporting accumulation as a discharge.** It is an area.
6. **Comparing slopes from different cell sizes.** The difference is arithmetic.
7. **Using a slope threshold across resolutions.** The fraction crossing it is a
   property of the grid.
8. **Comparing ruggedness from two DEMs of different resolution** — and then
   drawing a tectonic conclusion from the difference.

## Related modules

- [03 Raster Data Model, Resolution and Resampling](../05-gis-fundamentals/03-raster-data-model.md).
- [04 Map Algebra and Raster Analysis](../05-gis-fundamentals/04-map-algebra.md) —
  the operator classes and the $\mathrm{sinc}$ attenuation used throughout.
- [02 Hydrological and Watershed Analysis in GIS](02-hydrological-gis.md) — what
  comes next: watersheds, stream networks and the wetness index.
- [06-geospatial-analysis-advanced README](README.md).
- [14 Hydrology and Hydrogeophysics](../../14-hydrology-hydrogeophysics/README.md) —
  the physical processes the terrain indices approximate.

## Self-assessment checklist

- [ ] I can write Horn's weights and the aspect convention from memory.
- [ ] I can verify a derivative operator on a surface with a known answer.
- [ ] I can explain why aspect needs circular statistics.
- [ ] I can measure how much of a curvature field is noise.
- [ ] I can describe priority flood and why the epsilon is needed.
- [ ] I can verify an accumulation field by conservation.
- [ ] I can state the resolution dependence of slope and of hypsometry.

