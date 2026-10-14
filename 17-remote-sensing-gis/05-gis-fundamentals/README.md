# Module 17-05 — Geographic Information Systems

**Stages:** beginner → graduate · **Prerequisites:** basic Python and NumPy;
an introductory pandas course (module 03-04) or equivalent.

This module is the part of the curriculum where a measurement acquires a
*place*. Every technique in the remote-sensing folder produces numbers attached
to positions, and a GIS is the machinery that decides what those positions mean:
which reference frame they are in, which unit a distance carries, which polygon
a point belongs to, which cell a value is an average over. This module builds
that machinery from the two data models — vector and raster — and treats the
decisions hidden inside it as the subject rather than the housekeeping.

The organising difficulty is that **two of the most consequential choices in a
GIS are invisible in the result**. The first is the coordinate reference system:
a layer in the wrong frame is a plausible-looking map displaced by kilometres,
and every area computed in a geographic frame is not an area at all. The second
is topology and support: a coverage with slivers and overlaps has an area that is
not additive, a join that was meant to be one-to-one can silently multiply rows,
a focal filter quietly changes the size of the region each cell represents, and a
kriged map inherits the smoothness of a variogram that the data cannot pin down.
In this module each of those failures is *measured*, in metres, square kilometres
or per cent, so that it can be recognised the next time it appears without a
warning.

Three ideas recur, and each is quantified rather than asserted. The first is
**units**: a degree is not a length, a cell area is a property of the projection,
and a 1 m digitising tolerance becomes a measurable area error. The second is
**support**: an interpolated grid cell and a buffered polygon are not
measurements of a point, and comparing products with different support is the
commonest quantitative error in the field. The third is **non-uniqueness**: a
variogram, a smoothing parameter, an edge policy and a normalisation range are
all inferred or chosen, and the module shows two defensible choices producing
maps that differ by a third of the field's range.

All models and data in this module are **SYNTHETIC**. Every polygon, raster,
attribute table, variogram and validation number is constructed in memory from a
fixed seed for teaching purposes. No real dataset, satellite image, coordinate or
place is used, and no number is quoted from a published measurement.

## Learning objectives

By the end of this module you will be able to:

1. **Describe** a GIS layer as a table plus a geometry column, and **state** which
   operations preserve, destroy or duplicate that geometry.
2. **Read** an affine geotransform and a CRS, and **derive** cell area, extent,
   cell centres and the units of any distance or area.
3. **Test** a coverage for topology errors using area additivity and the Euler
   count, and **quantify** the overlap and gap terms separately.
4. **Compute** the row-count and bias consequences of an attribute or spatial
   join, and **predict** them before running the join.
5. **Choose** a resampling statistic for a stated purpose, and **explain** the
   information a coarsening destroys — including the minority class and the
   aliased wavelength.
6. **Classify** any raster expression as local, focal, zonal or global, and
   **propagate** uncertainty through a ratio index and a focal filter.
7. **Verify** a derivative operator against an analytically known surface, and
   **measure** the finite-difference attenuation that makes a slope map
   scale-dependent.
8. **Fit** a variogram, **demonstrate** its parameter valley, and **explain** why
   two equally defensible models give maps that differ by a large fraction of the
   field's range.
9. **Assemble** an ordinary-kriging system, **verify** its unbiasedness and
   exactness, and **interpret** its variance as a model statement.
10. **Design** a pipeline that is a pure function of its inputs, with a canonical
    output encoding, stated numeric tolerances, fixed iteration order, guards and
    a provenance record.

## Prerequisites

- [03-04 pandas](../../03-scientific-computing/04-pandas/README.md) — group-by,
  merge and indexing, which are the tabular half of every vector operation.
- [03-09 Geospatial Python](../../03-scientific-computing/09-geospatial-python/README.md) —
  Shapely, GeoPandas and cartopy at library level.
- [03-08 Gridded Geospatial Data](../../03-scientific-computing/08-gridded-geospatial-data/README.md) —
  rasterio, xarray and NetCDF, the tools behind the raster lessons here.
- [02-01 Measurement and Physical Reasoning](../../02-physics/01-measurement-and-physical-reasoning/README.md) —
  units, dimensions and uncertainty propagation.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [GIS Concepts: Layers, Attributes and Topology](01-gis-concepts.md) | beginner | A layer is a table plus geometry; a coverage's area residual diagnoses its topology |
| 02 | [Vector Data Model and Attribute Operations](02-vector-data-model.md) | intermediate | Joins multiply rows, predicates select answers, and validity is asserted not assumed |
| 03 | [Raster Data Model, Resolution and Resampling](03-raster-data-model.md) | intermediate | Area is counting; a coarse cell is a model; aliasing relocates a wavelength |
| 04 | [Map Algebra and Raster Analysis](04-map-algebra.md) | advanced | Four operator classes, each with its own error behaviour and support |
| 05 | [Spatial Interpolation: IDW, Kriging, Splines](05-spatial-interpolation-gis.md) | graduate | Every interpolator is a model, and the validation metric is the arbiter |
| 06 | [Reproducible Geospatial Workflows (QGIS, Python)](06-geospatial-workflows.md) | graduate | Reproducibility is engineering: pure functions, canonical encoding, manifest |

## Suggested path

**If you are new to GIS:** lessons 01–03 in order, running each demonstration.
Lesson 01 establishes the two silent failures; 02 and 03 build the two data
models and measure what each operation costs.

**If you already use GIS software:** read 01 §2–§4 (topology and predicates), 02
§3–§5 (joins and indexing) and 03 §3 (aliasing), then decide whether 04–06 apply
to your work. Most experienced users will find at least one measured number that
contradicts a habit.

**If you are preparing a research project:** 04 §2–§5 (uncertainty propagation
and scale dependence), 05 in full (variograms, non-uniqueness, kriging variance)
and 06 in full (the manifest that makes the result reviewable), plus the ★★★
exercises.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-gis-concepts.md`](01-gis-concepts.md) | Lesson 01 |
| [`02-vector-data-model.md`](02-vector-data-model.md) | Lesson 02 |
| [`03-raster-data-model.md`](03-raster-data-model.md) | Lesson 03 |
| [`04-map-algebra.md`](04-map-algebra.md) | Lesson 04 |
| [`05-spatial-interpolation-gis.md`](05-spatial-interpolation-gis.md) | Lesson 05 |
| [`06-geospatial-workflows.md`](06-geospatial-workflows.md) | Lesson 06 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for all six lessons |
| [`code/`](code) | Six runnable demonstrations, one per lesson |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib,
pandas, GeoPandas, Shapely, Rasterio and pyproj:

```bash
cd 17-remote-sensing-gis/05-gis-fundamentals/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gis_concepts_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python vector_data_model_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python raster_data_model_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python map_algebra_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python spatial_interpolation_gis_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python geospatial_workflows_demo.py
```

Every demo is print-only — no figures, no files, no network — uses a fixed random
seed (`np.random.default_rng(20261014)`), prints labelled results with units and
exits 0. The projection demo uses RAM-backed `rasterio` datasets, so nothing is
written to disk.

## Mastery checkpoint

Complete this without notes:

> A synthetic study area of 40 km × 25 km is covered by a 500 m raster and by a
> vector coverage of 12 polygons. **(a)** State the raster's cell count, its cell
> area and why its total area is exact while its boundary is approximate.
> **(b)** The vector coverage has a summed area 0.6 km² larger than its union.
> State what that means and give the two checks you would run next. **(c)** You
> resample the raster to 2 km. State what happens to a class occupying 3 % of the
> fine cells, and to a 4 km wavelength in the data. **(d)** You interpolate a
> 150-sample survey and report a variogram range of 6 km. State the two further
> pieces of information a reader needs before accepting that number.

A worked version of (a)–(c) is in the
[solutions](exercises/01-gis-concepts-solutions.md) and
[05](exercises/05-spatial-interpolation-gis-solutions.md).

## Common pitfalls across this module

1. **Doing metric arithmetic in a geographic CRS.** Degrees are not metres and
   squared degrees are not areas.
2. **Trusting a boundary that closes.** A 1 m tolerance is a real area error and
   a real adjacency change; snapping is a decision to be recorded.
3. **Letting a join change the unit of analysis.** A row-mean is not a site-mean.
4. **Comparing products with different support.** A focal filter, a coarsening and
   a reprojection all change what a cell represents.
5. **Treating a resampling choice as neutral.** The statistic defines the meaning
   of the coarse cell.
6. **Assuming validity.** No arithmetic operation will report an invalid geometry.
7. **Quoting a variogram parameter without its misfit valley.** The parameters are
   jointly non-unique.
8. **Reading the kriging variance as a map error.** It uses no measured values.
9. **Caching or diffing on raw bytes.** Row order, column order and the last
   digits of a projection are byte-visible and semantically irrelevant.
10. **Running a validation suite that cannot fail.**

## Related modules

- [17-01 Remote Sensing Physics](../01-remote-sensing-physics/README.md) —
  where the values that go into a GIS layer come from.
- [17-02 Optical and Thermal Remote Sensing](../02-optical-and-thermal-remote-sensing/README.md) —
  classification and change detection on the rasters built here.
- [17-03 Radar Remote Sensing](../03-radar-remote-sensing/README.md) —
  InSAR, whose phase-to-displacement conversion is a geospatial workflow in the
  sense of lesson 06.
- [17-04 Satellite Geodesy Techniques](../04-satellite-geodesy-techniques/README.md) —
  GNSS and satellite gravimetry, the reference frames underneath every CRS.
- [Advanced Geospatial Analysis](../06-geospatial-analysis-advanced/README.md) —
  terrain, hydrology, networks, spatial statistics and multi-criteria decisions
  built on this module.
- [17-07 Earth Observation Data and Platforms](../07-earth-observation-data/README.md) —
  how these layers are obtained, discovered and licensed.
- [17-08 Remote Sensing Applications in Geophysics](../08-remote-sensing-applications-geophysics/README.md) —
  where the module's cautions are applied to geological and hydrological targets.
- [03-09 Geospatial Python](../../03-scientific-computing/09-geospatial-python/README.md) —
  the library-level treatment this module deliberately does not duplicate.
- [22 Data Engineering and Reproducibility](../../22-data-engineering-reproducibility/README.md) —
  the wider reproducibility context of lesson 06.
