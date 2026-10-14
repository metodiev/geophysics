# Module 17-06 — Advanced Geospatial Analysis

**Stages:** advanced → doctoral · **Prerequisites:** modules 17-05 (all lessons)
and 03-04; basic linear algebra.

This module takes the two data models of module 17-05 and asks what a raster or a
coverage *implies*. Terrain analysis turns a sampled surface into derivatives;
hydrology turns those derivatives into a flow network; network analysis turns a
friction surface into a graph and a route; spatial statistics asks whether a
pattern is distinguishable from its own autocorrelation; and multi-criteria
analysis turns a set of criteria into a decision. In each case the interesting
object is not the map but the **operator**, and each lesson therefore verifies its
operator against a surface whose answer is known analytically before applying it
to a surface whose answer is not.

The organising claim is that **every quantity in this module is a property of the
processing chain as much as of the ground**. Slope is a finite-difference
attenuation of the terrain's spectrum as well as a measure of steepness: the same
landscape yields 6.9° of mean slope at 200 m cells and 2.6° at 1600 m, and a
fraction of the terrain steeper than a threshold moves from 64.7 % to zero. A
watershed is the boundary of the *filled* DEM you supplied, and on a low-relief
landscape a 1 m elevation error changes half of its area. A least-cost route shares
only a quarter of its cells with the same route computed on a 5 % noisier friction
surface, while its cost changes by 0.7 %, so the optimum is geometrically
degenerate. A hotspot map drawn at an uncorrected 5 % level flags 3.5 % of a field
that contains no hotspots at all. None of these are defects of the software; they
are the arithmetic of sampling, resampling, graph construction and multiple
testing, and the module's purpose is to make each of them a measured number.

A second theme runs through the module because it is forced by the first: **verify
before you interpret**. Every lesson contains at least one exact check — Horn's
slope on a cone (error 0.0009°), the discrete Laplacian on a paraboloid (error
2.4 × 10⁻¹⁸ m⁻¹), the $\mathrm{sinc}$ attenuation of a centred difference (error
1.1 × 10⁻¹⁶), a D8 accumulation by conservation (residual exactly 0 cells),
an AHP eigenvector on a consistent matrix (error 5.6 × 10⁻¹⁷) — and then applies
the verified operator to a synthetic terrain whose truth is also known, so that
signal can be separated from processing artefact. The sequence *verify on an
analytic case, apply to a known synthetic case, report the uncertainty* is the
working method of the module.

All models and data in this module are **SYNTHETIC**. Every DEM, friction surface,
field, network, criterion raster and alternative is generated in memory from a
fixed seed. No real dataset, DEM, satellite image, catchment, route or coordinate
is used, and no number is quoted from a published measurement.

## Learning objectives

By the end of this module you will be able to:

1. **Compute** slope, aspect and curvature with Horn's weights and the correct
   north-up sign convention, and **verify** each against an analytic surface.
2. **Explain** why aspect is a circular quantity and **compute** circular
   statistics rather than arithmetic ones.
3. **Fill** depressions by priority flood with flat resolution, and **measure** the
   volume the fill adds to a DEM.
4. **Verify** a flow-accumulation field by conservation, and **delineate** a
   watershed by reverse traversal checked against forward accumulation.
5. **Quantify** how an extraction threshold propagates into drainage density,
   stream counts and network order, and **explain** why a fitted power law is not
   evidence for a law.
6. **Convert** a friction raster into a graph, **compute** a least-cost path, and
   **state** what two independent implementations do and do not establish.
7. **Demonstrate** when a graph must be directed, and **test** whether a
   cost-distance region is convex.
8. **Measure** the stability of a route and of a kriging or suitability product
   under a stated perturbation, and **report** the stable object rather than the
   point estimate.
9. **Compute** Moran's I, Geary's C, local Moran and Getis-Ord Gi*, with a
   permutation null and a multiplicity correction.
10. **Estimate** an effective sample size and **state** its consequence for a
    confidence interval.
11. **Assemble** AHP weights, verify them on a consistent matrix, and **interpret**
    the consistency ratio as a check on the analyst rather than on the data.
12. **Measure** compensation, rank reversal and weight sensitivity in a
    multi-criteria suitability rule.

## Prerequisites

- [17-05-03 Raster Data Model, Resolution and Resampling](../05-gis-fundamentals/03-raster-data-model.md) —
  the georeference and the cell size every metric here depends on.
- [17-05-04 Map Algebra and Raster Analysis](../05-gis-fundamentals/04-map-algebra.md) —
  focal operators, their edge policies and the $\mathrm{sinc}$ attenuation.
- [17-05-05 Spatial Interpolation: IDW, Kriging, Splines](../05-gis-fundamentals/05-spatial-interpolation-gis.md) —
  variograms and non-uniqueness, the vocabulary of lesson 04.
- [03-03 SciPy](../../03-scientific-computing/03-scipy/README.md) — sparse
  matrices, graph algorithms and array machinery.
- [03-04 pandas](../../03-scientific-computing/04-pandas/README.md) — the tabular
  half of every aggregation used here.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Terrain Analysis: Slope, Aspect, Curvature, Flow Accumulation](01-terrain-analysis.md) | graduate | Every derivative is a focal operator with a support; verify it on a known surface |
| 02 | [Hydrological and Watershed Analysis in GIS](02-hydrological-gis.md) | doctoral | The boundary is the boundary of the filled DEM you supplied, and it inherits the DEM's error |
| 03 | [Network Analysis and Least-Cost Paths](03-network-analysis.md) | advanced | The cost of the optimum is stable and the line is not; a route is a model output |
| 04 | [Spatial Statistics, Autocorrelation and Hotspot Analysis](04-spatial-statistics.md) | doctoral | Weights, null and multiplicity decide the answer; an uncorrected map invents hotspots |
| 05 | [Multi-Criteria Decision Analysis for Suitability Mapping](05-multicriteria-decision.md) | doctoral | A suitability map is a decision rule; report the class, the rank range and the sensitivity |

## Suggested path

**If you are new to terrain and hydrology:** lessons 01 and 02 in order, running
each demonstration. Lesson 01 establishes the verification method; lesson 02
applies it to a boundary that is computed rather than drawn.

**If your work is routing or accessibility:** lesson 03, then lesson 01 §7 on the
scale dependence of slope, because most movement costs are built from it.

**If your work involves patterns, anomalies or hotspot maps:** lesson 04 before
anything else. It is the lesson whose omission is most costly, because the failure
mode (a map of p-values with no multiplicity control) looks like a result.

**If your work is suitability mapping, site selection or land-use planning:**
lesson 05, with lesson 04 §6 (effective sample size) attached to it, since scores
over autocorrelated cells do not carry the independent evidence they appear to.

**If you are preparing a research project:** 01 §4 (curvature and noise), 02 §7
(delineation sensitivity), 03 §6 (route degeneracy), 04 §5–6 (multiplicity and
effective sample size) and 05 §6–7 (sensitivity and rank reversal), plus the ★★★
exercises throughout.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-terrain-analysis.md`](01-terrain-analysis.md) | Lesson 01 |
| [`02-hydrological-gis.md`](02-hydrological-gis.md) | Lesson 02 |
| [`03-network-analysis.md`](03-network-analysis.md) | Lesson 03 |
| [`04-spatial-statistics.md`](04-spatial-statistics.md) | Lesson 04 |
| [`05-multicriteria-decision.md`](05-multicriteria-decision.md) | Lesson 05 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for all five lessons |
| [`code/`](code) | Five runnable demonstrations, one per lesson |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib,
pandas, GeoPandas, Shapely, Rasterio and pyproj:

```bash
cd 17-remote-sensing-gis/06-geospatial-analysis-advanced/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python terrain_analysis_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python hydrological_gis_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python network_analysis_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python spatial_statistics_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python multicriteria_decision_demo.py
```

Every demo is print-only — no figures, no files, no network — uses a fixed random
seed (`np.random.default_rng(20261014)`), prints labelled results with units and
exits 0. The hydrological demo implements its own priority-flood fill and D8
routing, so it has no dependency beyond NumPy and SciPy; the network demo uses
`scipy.sparse.csgraph` for one of its two shortest-path implementations and a
hand-written Dijkstra for the other.

## Mastery checkpoint

Complete this without notes:

> A synthetic 250 m DEM covers 40 km × 30 km and contains a basin of 9 000 cells.
> **(a)** State the cell area, the basin area, and why the area is exact while the
> boundary is not. **(b)** The region's relief is 30 m and the DEM's vertical
> accuracy is 3 m. State what that implies for the delineated boundary and name
> the experiment that quantifies it. **(c)** A slope map from this DEM reports
> that 45 % of the basin exceeds 8°. Give two reasons the number changes at 1 km
> cells and state the direction of each. **(d)** A least-cost route across the
> basin is computed and has the lowest possible cost; a colleague reports it as
> the route. Give the two checks you would run, and state what you would publish
> instead.

A worked version of (a)–(c) is in
[02-hydrological-gis-solutions.md](exercises/02-hydrological-gis-solutions.md) and
[01-terrain-analysis-solutions.md](exercises/01-terrain-analysis-solutions.md).

## Common pitfalls across this module

1. **Reading a derivative map as the terrain.** Slope, aspect and curvature carry
   the window size, the edge policy and the DEM's noise spectrum.
2. **Comparing metrics computed at different supports.** The arithmetic difference
   is usually larger than the geomorphological one.
3. **Reversing the north-up sign**, which leaves slope looking correct and reverses
   every aspect by 180°.
4. **Averaging a circular quantity.** Aspect, azimuth and phase have no arithmetic
   mean.
5. **Treating the fill as preprocessing.** It changes the surface by tens of metres
   and every discharge inherits it.
6. **Quoting a basin area or a drainage density without its DEM, threshold and
   flow rule.**
7. **Presenting a single least-cost line** when the optimum is degenerate and a
   corridor is the honest product.
8. **Reporting Moran's I without its weights, or a hotspot map without a
   multiplicity correction.**
9. **Using the cell count as the sample size** on an autocorrelated field.
10. **Reading a suitability score as a probability or a feasibility**, and quoting
    the top cell when it changes in a third of plausible weight perturbations.

## Related modules

- [17-05 Geographic Information Systems](../05-gis-fundamentals/README.md) — the
  prerequisite module: layers, raster model, map algebra, interpolation and
  reproducible workflows.
- [17-01 Remote Sensing Physics](../01-remote-sensing-physics/README.md) — where
  the rasters being analysed come from.
- [17-02 Optical and Thermal Remote Sensing](../02-optical-and-thermal-remote-sensing/README.md) —
  classification, change detection and the fractional-cover products used here.
- [17-03 Radar Remote Sensing](../03-radar-remote-sensing/README.md) — InSAR digital
  elevation models and their specific error structure.
- [17-07 Earth Observation Data and Platforms](../07-earth-observation-data/README.md) —
  obtaining the DEMs and imagery these workflows consume.
- [17-08 Remote Sensing Applications in Geophysics](../08-remote-sensing-applications-geophysics/README.md) —
  where these methods are applied to geological and hydrological targets.
- [14 Hydrology and Hydrogeophysics](../../14-hydrology-hydrogeophysics/README.md) —
  the physics behind the hydrological indices.
- [18 Inverse Problems](../../18-inverse-problems/README.md) — the general theory of
  the non-uniqueness and sensitivity measured concretely here.
- [21-02 Geostatistics](../../21-statistics-bayesian-ml/02-geostatistics/README.md) —
  variograms, kriging and conditional simulation as a statistical discipline.
- [21-03 Bayesian Inference](../../21-statistics-bayesian-ml/03-bayesian-inference/README.md) —
  the formal frame for the decision rules of lesson 05.
