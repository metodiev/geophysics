---
id: 17-06-02
title: "Hydrological and Watershed Analysis in GIS"
level: doctoral
prereqs: ["17-06-01", "17-05-03", "14-02-02"]
tags: [gis, geospatial, remote-sensing, geospatial-analysis-advanced, hydrology, watershed, drainage, wetness-index]
---

# Hydrological and Watershed Analysis in GIS

A watershed boundary is not drawn; it is *computed* from a flow rule applied to a
digital elevation model. That sentence contains the whole content of this lesson.
Everything in hydrological GIS — a basin boundary, a stream network, a drainage
density, a wetness index, a flow accumulation — is an exact consequence of three
choices that the terrain cannot make: the flow rule, the cell size and the
extraction threshold. This lesson makes each choice explicit, verifies each
result against an independent route where one exists, and then measures how much
the answers move when the elevation data are perturbed by an amount far smaller
than the vertical accuracy of a global DEM.

All models and data in this module are **SYNTHETIC**. The terrain, the basins,
the networks and every statistic below are generated in memory from a fixed
seed. No real catchment, gauge, river or coordinate is used.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** a D8 flow network from a filled DEM and **state** the two
   implementation details (the fill epsilon and the receiver convention) that
   decide whether it works at all.
2. **Delineate** a watershed by reverse traversal from a pour point, and
   **verify** it against the flow accumulation at that point.
3. **Explain** why a stream network begins with a threshold rather than with a
   channel, and **quantify** how the threshold propagates into drainage density,
   stream counts and network order.
4. **Compute** Strahler orders and the bifurcation ratio, and **state** what the
   ratio does and does not measure.
5. **Fit** a Hack's-law exponent and **demonstrate** that the fit is dominated by
   the extraction recipe rather than by the terrain.
6. **Derive** the topographic wetness index, and **measure** its resolution
   dependence, its floor convention and its ranking instability.
7. **Compute** a hypsometric curve and integral and **contrast** their stability
   with that of slope-derived metrics.
8. **Quantify** the sensitivity of a delineation to DEM error, and **explain**
   why the sensitivity depends on relief rather than on the algorithm.

## Prerequisites

- [01 Terrain Analysis: Slope, Aspect, Curvature, Flow Accumulation](01-terrain-analysis.md) —
  the DEM, the fill and the D8 rule used here.
- [03 Raster Data Model, Resolution and Resampling](../05-gis-fundamentals/03-raster-data-model.md) —
  cell area, coarsening and the resampling statistic.
- [14-01-01 The Hydrologic Cycle](../../14-hydrology-hydrogeophysics/01-hydrology-fundamentals/01-hydrologic-cycle.md) —
  the water balance that flow accumulation approximates.

## 1. From a DEM to a flow network

Three steps, in this order, and each one changes the answer:

1. **Fill** the depressions. A closed depression has no outlet computing rule, so
   D8 assigns it no receiver. Priority flood (see
   [01 Terrain Analysis](01-terrain-analysis.md) §5) raises each cell to the
   level of its lowest path to the boundary, with a small epsilon so the filled
   surface has a strictly monotone path. Measured on the synthetic terrain:
   16 364 of 54 000 cells raised (30.30 %), maximum raise 204.41 m.
2. **Route** flow. D8 gives each cell the neighbour with the steepest descent,
   with the diagonal step divided by $\sqrt 2$ so that slope, not step count, is
   compared.
3. **Accumulate**. Process cells in decreasing filled elevation and push each
   cell's total to its receiver. The result is the number of upstream cells,
   which becomes an area when multiplied by the cell area.

The filled surface had 18 cells with no receiver — the domain edge plus a few
ties. The largest accumulation is 17 973 cells = 718.92 km².

## 2. Watershed delineation and its internal check

A watershed is the set of cells that drain to a chosen point. It is computed by
reversing the receiver graph (a traversal of children rather than parents) and
then verified against the accumulation:

| quantity | value |
|---|---|
| pour point (row, col) | (31, 299) |
| accumulation at the pour point | 17 973 cells |
| cells found by reverse traversal | 17 973 |
| agreement (topological check) | True |
| basin area | 718.920 km² (33.28 % of the DEM) |
| basin relief | 121.17 – 597.91 m (476.74 m relief) |
| second basin | 7 530 cells (301.200 km²) |
| overlap between the two basins | 0 cells |
| combined area | 1 020.120 km² (47.23 % of the DEM) |

$$
\underbrace{\left|\text{basin}(p)\right|}_{\text{reverse traversal}}
= \underbrace{\text{acc}(p)}_{\text{forward count}}
\qquad\text{exactly.}
$$

That equality is the only internal check a delineation has, and it is worth
running every time: it catches a broken receiver graph, a stale accumulation
array and an off-by-one in the traversal. It says **nothing** about whether the
chosen pour point is the outlet the hydrologist intended, which is a decision
about the problem rather than about the data.

## 3. Stream extraction: a threshold, not a channel

A raster has no channels. What a "stream network" means in raster hydrology is:
cells whose upstream area exceeds a stated threshold. The threshold is therefore
a decision, and it propagates into every downstream statistic:

| threshold (cells) | area above (km²) | stream cells | first-order streams | max Strahler | drainage density (km/km²) |
|---|---|---|---|---|---|
| 50 | 2.0000 | 2 681 | 1 220 | 4 | 0.2482 |
| 200 | 8.0000 | 1 931 | 1 451 | 3 | 0.1788 |
| 800 | 32.0000 | 1 383 | 1 094 | 3 | 0.1281 |
| 3200 | 128.0000 | 574 | 407 | 2 | 0.0531 |

The drainage density falls by a factor of 4.7 between the lowest and the highest
threshold, and the maximum order falls from 4 to 2. **None of the terrain
changed.** A published drainage density without its threshold and its cell size
is not a measurement of the landscape; it is a statement about the extraction
recipe. The conventional value for a real catchment is quoted at a stated
threshold for exactly this reason.

### 3.1 Strahler ordering and the bifurcation ratio

Stream order is assigned from the leaves upwards: a headwater segment is order 1,
and a junction takes the maximum order of its tributaries, plus one if two
tributaries of equal maximum order meet.

At a 200-cell threshold the order counts are $[1451, 389, 91]$ for orders
1, 2, 3, giving bifurcation ratios

$$
\frac{N_1}{N_2} = 3.730,\qquad \frac{N_2}{N_3} = 4.275,
\qquad \overline{R_B} = 4.002 .
$$

The classical value for natural drainage networks is close to 4, so the number is
a useful **implementation check**: an error in the junction rule or in the
receiver graph moves it immediately. It is not evidence about a landscape, and
here the landscape is explicitly synthetic. Note also that the ratio depends on
the threshold: reporting a bifurcation ratio means reporting the rule that built
the network it describes.

## 4. Hack's law, fitted and found wanting

Hack's law states that the length $L$ of a stream is a power of its basin area,

$$
L = k A^{h},
$$

with $h \approx 0.6$ for natural networks. The natural unit of a stream here is a
**Strahler segment**: a maximal chain of constant order, measured from the source
of the segment to its downstream junction. Fitting each threshold separately:

| threshold (cells) | segments | fitted $h$ | $R^2$ |
|---|---|---|---|
| 100 | 58 | 0.6472 | 0.424 |
| 200 | 43 | 0.9927 | 0.564 |
| 400 | 33 | 0.9295 | 0.409 |
| 800 | 21 | 1.2418 | 0.695 |

The exponent varies from 0.65 to 1.24 and the fits are poor. This is a **negative
result** and a useful one:

* A segment's length is quantised in cell and diagonal steps (200 m and 283 m)
  while its area varies continuously, so at lengths of a few cells the relation
  cannot be smooth.
* The number of segments is small (21–58), so sampling error is large.
* The threshold decides which cells are streams, and therefore both the segments
  and their areas.

The honest conclusion is not that Hack's law is false but that **a power law can
be fitted to almost any network, and a fit is not evidence for a law.** Reporting
an exponent requires the threshold, the cell size and the length definition
(straight-line distance to the outlet, path length along D8, or length of the
main channel), without which the number is comparable with nothing.

## 5. Topographic wetness index

The topographic wetness index is

$$
\text{TWI} = \ln\frac{a}{\tan\beta},
\qquad a = \frac{\text{acc} \cdot \Delta^2}{\Delta}\ \left[\mathrm{m^2\,m^{-1}}\right],
$$

where $a$ is the specific catchment area (accumulated area per unit contour
width) and $\beta$ is the local slope. Measured on the synthetic filled DEM:

| quantity | value |
|---|---|
| $a$ range | 200 to 3 594 600 m² m⁻¹ |
| $\tan\beta$ range | $1.0\times10^{-4}$ (the floor) to 0.1598 |
| TWI mean / sd / range | 11.870 / 3.500 / [7.492, 23.450] |
| TWI deciles (10, 50, 90 %) | 8.957, 9.997, 17.342 |

Three decisions are hidden in that table:

1. **The slope floor.** Flat cells give $\tan\beta = 0$ and TWI diverges, so a
   floor is applied — here $10^{-4}$. The floor is a choice, and it sets the
   upper tail of the TWI distribution.
2. **The definition of $a$.** Dividing the accumulated *area* by the cell width
   assumes the contour width equals the cell size. For D8 with diagonals the
   effective width varies, and some implementations divide by the number of
   contributing neighbours instead.
3. **The resolution.** Coarsening the same filled surface to 800 m gives

| cell | TWI mean | TWI sd | 10–90 % |
|---|---|---|---|
| 200 m | 11.870 | 3.500 | 8.957 – 17.342 |
| 800 m | 11.889 | 2.726 | 9.601 – 16.621 |

The mean shifts by only 0.16 %, but the **spread changes by 22 %**, and the
ranking changes more than that: the top-10 % TWI mask at 800 m overlaps the
200 m mask with a Jaccard index of only 0.2593, so about 74 % of the selected
area changes when only the cell size changes. Part of that is the block
structure of the upsampled coarse field, and the part that matters is that the
*selected area*, not only the values, depends on the cell size. Because TWI is a
difference of two logs whose terms scale differently with resolution
(accumulation with the cell count, slope by $\mathrm{sinc}$ attenuation), its
absolute values are not comparable between DEMs and only the ranking within one
grid is meaningful — and a wetland mask drawn from that ranking inherits the
grid's decision.

## 6. Hypsometry: the portable basin metric

The hypsometric curve of the delineated basin gives the fraction of area above
each relative height; the hypsometric integral is the mean relative height:

| quantity | value |
|---|---|
| basin cells | 17 973 |
| relief | 121.17 – 597.91 m |
| hypsometric integral | 0.4231 |
| the highest 10 % of the area accounts for | 0.6 % of the basin |
| the highest 50 % of the area accounts for | 34.8 % of the basin |
| the highest 90 % of the area accounts for | 96.6 % of the basin |

The integral is an *area* statistic and it is stable: in
[01 Terrain Analysis](01-terrain-analysis.md) the same terrain's integral moved
by 2.3 % across a 64-fold change in cell count, while the slope-derived
ruggedness fell by 43 %. By the rule of §8 of that lesson, hypsometry is the
metric to use when two basins from different DEMs must be compared, and slope or
drainage density is the metric that must be recomputed on a common grid first.

## 7. Sensitivity: how far a 1 m error moves the boundary

The decisive experiment is not the algorithm but its input. Two synthetic
landscapes, the same 1 m elevation error, 12 independent noise realisations each:

| landscape | reference basin (cells) | area spread | Jaccard overlap with the reference | boundary change | outlet displacement (mean / max) |
|---|---|---|---|---|---|
| full relief | 17 962 | 0.38 % | 0.9966 (min 0.9945) | 0.34 % | 0.00 / 0.00 km |
| 15 % relief | 19 671 | 32.27 % | 0.4870 (min 0.3645) | 51.30 % | 0.65 / 3.20 km |

The two rows are the lesson:

* Where the divides follow large systematic slopes, a 1 m error changes the basin
  by a third of a per cent and the outlet not at all. The "algorithm" is
  irrelevant: the terrain decides.
* Where the relief is small compared with the error, the same input perturbation
  halves the basin, changes half of its area, and moves the detected outlet by
  kilometres — because near a flat divide the flow direction is decided by the
  noise.

A 1 m vertical error is well below the vertical accuracy of most global DEMs
(typically 2–10 m and worse under vegetation), so the second row, not the first,
is the realistic case for low-relief ground. The honest remedy is exactly the
experiment above: **repeat the delineation from perturbed DEMs and report the
spread** — a basin boundary with a stated uncertainty rather than a single line.

## 8. Worked example: is this basin 719 km²?

A synthetic delineation reports 718.920 km² at a pour point on a 200 m DEM.

1. **Internal consistency.** Reverse traversal equals forward accumulation
   (17 973 cells), so the graph is sound. ✔
2. **Cell area.** $200\,\mathrm m \times 200\,\mathrm m = 0.04\ \mathrm{km^2}$;
   $17\,973 \times 0.04 = 718.92\ \mathrm{km^2}$. ✔ (Area is counting, so it is
   exact given the grid.)
3. **Projection.** If the grid is a projected CRS in metres over 60 km, the area
   distortion is small; if it were a geographic grid the "cell area" would vary
   with latitude and the count would not be an area.
4. **DEM uncertainty.** At full relief the spread is 0.38 % → ±2.7 km²; at 15 %
   relief it is 32 % → ±230 km². The number to publish is
   "719 ± 3 km² (full relief)" or "787 km² with a 32 % spread under 1 m
   elevation error", not "718.920 km²".
5. **Definition.** "Basin of the pour point at (31, 299)" is a different object
   from "basin of the gauge", which is a decision about which cell represents a
   measuring station — and the DEM cell containing a gauge is not automatically
   the right pour point.

## Assumptions and regime of validity

1. **Flow converges to one neighbour (D8).** Diverging flow, alluvial fans and
   floodplains are misrepresented; D-infinity or multiple-flow-direction
   algorithms exist and give different accumulation fields.
2. **The fill is physically meaningful.** Any closed depression, real or
   artefactual, is destroyed. In karst or glaciated terrain the fill can remove
   the features of interest.
3. **The DEM resolves the channels.** If a channel is narrower than a cell, the
   accumulation is a property of the interpolation, not of the channel.
4. **The threshold is the network definition.** All stream statistics inherit it.
5. **Rainfall is uniform.** Accumulation is an area; a discharge requires an
   effective rainfall field, and a catchment comparison therefore requires either
   a runoff model or a stated uniformity assumption.
6. **The grid is projected in metres.** A geographic grid makes cell area
   latitude-dependent and TWI's $a$ ill-defined.
7. **The vertical datum is consistent.** Seams between DEM sources appear as
   spurious divides.

## Python demonstration

[`code/hydrological_gis_demo.py`](code/hydrological_gis_demo.py) builds the whole
chain in memory. It:

1. assembles a synthetic terrain with two catchments, fills it and drains it;
2. delineates a basin by reverse traversal and verifies it against the forward
   accumulation, then delineates a second basin and checks the overlap;
3. extracts streams at four thresholds and reports stream cells, first-order
   counts, maximum order and drainage density;
4. computes Strahler orders and bifurcation ratios;
5. fits Hack's law per threshold on Strahler segments and reports the exponent,
   the $R^2$ and the threshold dependence;
6. computes TWI, measures its resolution dependence and the overlap of the top
   10 % mask between resolutions;
7. computes the hypsometric curve and integral of the basin;
8. re-runs the whole delineation on 12 independent noise realisations at two
   reliefs and reports the Jaccard overlap, the area spread and the outlet
   displacement.

```bash
cd 17-remote-sensing-gis/06-geospatial-analysis-advanced/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python hydrological_gis_demo.py
```

Print-only, no files, no network, exits 0.

## Exercises

[`exercises/02-hydrological-gis-exercises.md`](exercises/02-hydrological-gis-exercises.md)
and the
[solutions](exercises/02-hydrological-gis-solutions.md):

- **★** Compute the cell area, basin area and relief of a stated delineation.
- **★★** Derive how the drainage density scales with the extraction threshold.
- **★★★** Design an uncertainty statement for a watershed boundary and specify
  the experiment that produces it.

## Mastery checkpoint

Without notes:

> A synthetic 250 m DEM covers 40 km × 30 km. **(a)** State the cell count and the
> cell area, and the area of a basin of 9 000 cells. **(b)** The extraction
> threshold is raised from 100 to 400 cells. State three statistics that change
> and the direction of each. **(c)** Give the two routes that must agree for a
> delineation to be internally valid, and say what the agreement does not test.
> **(d)** The region's relief is 30 m and the DEM's vertical error is 3 m. Explain
> what that implies for the watershed boundary and describe the experiment you
> would run to quantify it.

A worked version of (a)–(c) is in the
[solutions](exercises/02-hydrological-gis-solutions.md).

## Common pitfalls

1. **Reporting a drainage density without a threshold.** It moves by a factor of
   five between defensible thresholds.
2. **Quoting basin area to four significant figures.** The DEM uncertainty is
   the limit, not the cell count.
3. **Treating a filled depression as terrain.** The fill removes karst sinks,
   quarries and glacial hollows along with the artefacts.
4. **Comparing stream statistics between DEMs.** The network is a function of the
   grid and the threshold.
5. **Fitting a power law and reporting the $R^2$.** A poor fit with a plausible
   exponent is a warning, not a result.
6. **Using TWI across resolutions.** Its absolute values are not comparable, and
   a threshold on it selects different ground.
7. **Assuming an outlet is the gauge.** The pour point is a decision.
8. **Treating a single delineation as the boundary.** It is the boundary of the
   DEM supplied; perturb the DEM and measure.

## Related modules

- [01 Terrain Analysis: Slope, Aspect, Curvature, Flow Accumulation](01-terrain-analysis.md).
- [03 Network Analysis and Least-Cost Paths](03-network-analysis.md) — the same
  graph machinery applied to movement rather than to water.
- [04 Spatial Statistics, Autocorrelation and Hotspot Analysis](04-spatial-statistics.md) —
  how to test a claim made about a basin.
- [06-geospatial-analysis-advanced README](README.md).
- [14 Hydrology and Hydrogeophysics](../../14-hydrology-hydrogeophysics/README.md) —
  the physics that turns an accumulation into a discharge.

## Self-assessment checklist

- [ ] I can list the three decisions a raster stream network depends on.
- [ ] I can verify a delineation by two independent routes.
- [ ] I can compute a bifurcation ratio and say what it tests.
- [ ] I can fit Hack's law and explain why a fit is not a law.
- [ ] I can write TWI and name its two hidden conventions.
- [ ] I can choose between hypsometry and ruggedness for a comparison.
- [ ] I can design an uncertainty experiment for a watershed boundary.

