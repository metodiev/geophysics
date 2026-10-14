# Module 03-09 — Geospatial Python

**Stages:** intermediate → advanced · **Prerequisites:**
[03-04-01 Series, DataFrame and the Labeled-Data
Model](../04-pandas/01-series-dataframe.md) for the container a `GeoDataFrame`
extends, [03-04-02 Indexing, Selection, loc/iloc and Boolean
Masks](../04-pandas/02-indexing-selection.md) for mask-based selection,
[03-05-03 Maps, Cross-Sections and Geological
Symbology](../05-plotting-and-visualisation/03-maps-and-cross-sections.md) for map
figure construction, and — for the raster lessons — module
[03-08 Gridded and Geospatial Data](../08-gridded-geospatial-data/README.md).

## Scope

Vector data are how geophysics describes *places*: survey blocks, tenements,
catchments, flight lines, station inventories, fault traces. This module covers the
five things you must know to work with them.

1. **Geometry objects and planar operations.** Shapely gives you points, lines,
   polygons and the operations on them, in whatever units its coordinates are in —
   and it has no idea what a CRS is. Lesson 01.
2. **CRS handling on real features.** A `GeoDataFrame` attaches a CRS to a table of
   geometries, which makes area, distance and containment into metric questions with
   measurable answers. Lesson 02.
3. **Spatial indexing and joins at scale.** The naive point-in-polygon loop is
   $N \times M$; an R-tree makes it roughly $N$. Lesson 03 measures the reduction
   and, importantly, measures where it does *not* help.
4. **Raster–vector integration.** Zonal statistics, point sampling, masking and
   rasterisation are the bridge between a measurement on a grid and a region on a
   map. Lesson 04.
5. **Projections as a quantitative choice.** Cartopy plots in a projection, and
   `pyproj` tells you exactly how much that projection distorts at your latitude.
   Lesson 05.

The through-line is the same as the module's sibling: **distortion is a number, and
the number is available.** Every claim about degrees versus metres, wrong zones,
datums or Mercator inflation in these lessons is measured.

## Module map

| # | Lesson | Level | What it establishes |
|---|---|---|---|
| 01 | [Shapely Geometries and Planar Operations](./01-shapely-geometries.md) | intermediate | geometry types, units, buffers, validity, predicates, vectorisation |
| 02 | [GeoDataFrame, CRS Handling and Spatial Joins](./02-geopandas-basics.md) | intermediate | CRS arithmetic, area and distance errors, `sjoin`, boundary behaviour |
| 03 | [Spatial Indexing, Spatial Joins and Performance](./03-spatial-indexing.md) | advanced | STRtrees, candidate counting, cost models, when a grid beats an index |
| 04 | [Raster-Vector Integration and Zonal Statistics](./04-vector-raster-ops.md) | advanced | sampling, masking, rasterisation, resolution effects |
| 05 | [Cartopy: Map Projections and Geographic Plotting](./05-maps-cartopy.md) | intermediate | projection scale factors, datums, geodesic versus rhumb, plotting |

Each lesson has a paired problem set in `exercises/` (`*-exercises.md`) and a fully
worked solution file quoting the measured numbers (`*-solutions.md`).

## How to run the demonstrations

Every script is offline, seeded, and writes only into a throw-away directory inside
this module that it deletes on exit. Use the project interpreter:

```bash
cd /Users/miroslav/Documents/workspace/geophysics

# 01 shapely
.venv/bin/python 03-scientific-computing/09-geospatial-python/code/shapely_geometries_demo.py

# 02 geopandas
.venv/bin/python 03-scientific-computing/09-geospatial-python/code/geopandas_basics_demo.py

# 03 spatial indexing
.venv/bin/python 03-scientific-computing/09-geospatial-python/code/spatial_indexing_demo.py

# 04 vector-raster
.venv/bin/python 03-scientific-computing/09-geospatial-python/code/vector_raster_ops_demo.py

# 05 cartopy
.venv/bin/python 03-scientific-computing/09-geospatial-python/code/maps_cartopy_demo.py
```

Requirements are those of `requirements.txt`: shapely, pyproj, geopandas, rasterio,
numpy, pandas, matplotlib and cartopy. The Cartopy demo uses the `Agg` backend and
needs no display. Note that Cartopy's coastline, border, state and lake layers come
from Natural Earth via Cartopy's own data package and may be **downloaded on first
use** — the one network dependency in the module. Every other number comes from
`pyproj`, NumPy or a seeded generator, and runs offline.

## Data policy

**No real dataset is read by any demonstration, and none is committed to this
repository.** Geometry is built in code and labelled `SYNTHETIC`:

| Demo | Synthetic data |
|---|---|
| 01 | hand-built points, lines, polygons and a bow-tie ring |
| 02 | 600 seeded stations and six rectangular regions in the western USA |
| 03 | 2,000 seeded points against a 20 × 20 grid of 2 km cells in EPSG:32612 |
| 04 | a 30 m synthetic DEM (plane, ridge, basin, 90 m ripple) plus four survey blocks |
| 05 | a Gaussian anomaly on a global lon/lat grid, plotted on three projections |

Real products are named only in prose with a verified URL and are never fetched: for
example Natural Earth (<https://www.naturalearthdata.com>) for public-domain map
data, and EPSG.io (<https://epsg.io>) for CRS inspection.

## The three errors this module exists to prevent

1. **Computing a metric quantity in a geographic CRS.** `.area` in EPSG:4326 returns
   square degrees. Measured: a set of regions whose true total area is
   116,185.9791 km² reports as 12.000000 "square degrees", at ~9,682 km² per square
   degree.
2. **Using a projection outside its domain.** Measured: the same data in the wrong
   UTM zone gives an area error of **+0.8609 %** against **−0.0420 %** in the right
   one; a Quito–Tromsø straight line in Web Mercator is **+496 %** wrong.
3. **Guessing at the boundary convention.** Measured: a point exactly on a shared
   cell edge is matched by **0** cells under `within` and by **2** under
   `intersects`, and a polygon edge that misses the pixel grid by 17 m changes a
   block's pixel count by **401 cells (2.27 %)**.

## What this module does not cover

- **Gridded array containers.** netCDF, xarray, dask and rasters in their own right
  are module [03-08 Gridded and Geospatial Data](../08-gridded-geospatial-data/README.md).
- **Remote sensing and GIS practice.** Band algebra, indices and land-cover
  workflows are module [17 Remote Sensing and GIS](../../17-remote-sensing-gis/README.md).
- **Cartographic design.** Colormaps, typography and figure layout are module
  [03-05 Plotting, Visualisation and Scientific Figures](../05-plotting-and-visualisation/README.md).
- **Geodesy and reference frames.** Ellipsoids, geoids and datum realisation in
  their own right are modules [07 Gravity and Geodesy](../../07-gravity-geodesy/README.md)
  and [12 Global Geophysics and Earth Interior](../../12-global-geophysics-interior/README.md).
