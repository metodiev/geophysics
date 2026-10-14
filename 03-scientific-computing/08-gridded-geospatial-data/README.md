# Module 03-08 — Gridded and Geospatial Data

**Stages:** intermediate → graduate · **Prerequisites:**
[03-01-06 Files, Paths and I/O](../01-python-fundamentals/06-files-and-io.md) for
reading bytes off disk, [03-02-01 ndarray Creation, dtypes, Shapes and
Strides](../02-numpy/01-ndarray-basics.md) for the arrays underneath every format
here, and [03-04-01 Series, DataFrame and the Labeled-Data
Model](../04-pandas/01-series-dataframe.md) for the labelled-data idea that xarray
extends to $N$ dimensions. The chunking lesson also assumes
[03-02-07 Memory Layout, Strides and Cache-Aware
NumPy](../02-numpy/07-memory-performance.md).

## Scope

Geophysics measures fields, and the fields live on grids: gravity and magnetics on
a survey lattice, climate on a space–time cube, topography on a raster, seismic and
radar on three-dimensional arrays. This module covers the four things you must know
to work with them responsibly.

1. **What the container is.** netCDF-4 and HDF5 store labelled multidimensional
   arrays with metadata that survives being emailed to a colleague: dimensions,
   coordinate variables, units, and the `scale_factor`/`add_offset`/`_FillValue`
   machinery that decides what the numbers mean. Lesson 01 reads the file at the
   level of its bytes and its conventions.
2. **How to compute on labelled axes.** xarray gives every axis a name and every
   position a coordinate, which changes indexing, arithmetic and reduction from
   positional operations into labelled ones — and introduces the alignment
   behaviour that silently discards or NaN-fills data. Lessons 02 and 03.
3. **How to compute on data that do not fit in memory.** Dask describes the whole
   array and evaluates it a chunk at a time, so a 512 MB field can be reduced on a
   laptop. Lesson 04 measures what chunking costs and where it changes the answer.
4. **How to work with physical coordinates.** A grid with a CRS has a metric
   meaning that a grid without one does not; the raster's affine transform is the
   six numbers that connect `(row, col)` to `(x, y)`. Lessons 05 and 06.

The through-line is **measurement over assertion**. Every numerical claim in the
lessons was produced by running the demo in `code/`, and several of the lessons
correct a claim that the measurement contradicted.

## Module map

| # | Lesson | Level | What it establishes |
|---|---|---|---|
| 01 | [netCDF/HDF5 Formats and Self-Describing Data](./01-netcdf-and-hdf5.md) | intermediate | the data model, packing, `_FillValue`, chunking and compression |
| 02 | [xarray DataArray, Coordinates and Labeled Dimensions](./02-xarray-dataarray.md) | intermediate | labelled indexing, alignment, broadcasting, interpolation |
| 03 | [Dataset, Alignment, Broadcasting and GroupBy](./03-xarray-dataset.md) | advanced | multi-variable containers, area weighting, groupby, ellipsoidal band areas |
| 04 | [Chunking with Dask for Out-of-Core Analysis](./04-dask-chunking.md) | graduate | task graphs, chunk layout, halos, precision trade-offs |
| 05 | [Case Study: Analysing a Climate Data Cube](./05-climate-data-cube.md) | advanced | a full analysis on a synthetic cube with known ground truth |
| 06 | [rasterio: Rasters, Windows, Masks and Reprojection](./06-rasterio-rasters.md) | advanced | affine transforms, half-pixel convention, masks, reprojection |

Each lesson has a paired problem set in `exercises/` (`*-exercises.md`) and a fully
worked solution file quoting the measured numbers (`*-solutions.md`).

## How to run the demonstrations

Every script is offline, seeded, and writes only into a throw-away directory inside
this module that it deletes on exit. Use the project interpreter, which carries the
scientific stack:

```bash
cd /Users/miroslav/Documents/workspace/geophysics

# 01 netCDF/HDF5
.venv/bin/python 03-scientific-computing/08-gridded-geospatial-data/code/netcdf_hdf5_demo.py

# 02 DataArray
.venv/bin/python 03-scientific-computing/08-gridded-geospatial-data/code/xarray_dataarray_demo.py

# 03 Dataset
.venv/bin/python 03-scientific-computing/08-gridded-geospatial-data/code/xarray_dataset_demo.py

# 04 dask chunking
.venv/bin/python 03-scientific-computing/08-gridded-geospatial-data/code/dask_chunking_demo.py

# 05 climate data cube
.venv/bin/python 03-scientific-computing/08-gridded-geospatial-data/code/climate_data_cube_demo.py

# 06 rasterio
.venv/bin/python 03-scientific-computing/08-gridded-geospatial-data/code/rasterio_rasters_demo.py
```

Requirements are those of `requirements.txt`: numpy, netCDF4, h5py, xarray, dask,
rasterio, pyproj and (for one geodesic comparison) shapely. All are declared in the
manifest; install with

```bash
pip install -r requirements.txt
```

## Data policy

**No real dataset is read by any demonstration, and none is committed to this
repository.** The grids are synthesised in code from a seeded generator and are
labelled `SYNTHETIC` in the output and in the prose:

| Demo | Synthetic field |
|---|---|
| 01 | a Gaussian gravity anomaly plus a linear trend and seeded noise, 161 × 121 × 24 |
| 02 | the same Gaussian on a lon/lat grid, at two resolutions |
| 03 | a global 3° grid with a Gaussian, a meridional term and seeded noise, plus 36 months of temperature |
| 04 | a 512 MB field built lazily from coordinate arrays, never materialised |
| 05 | a 480-month cube with an imposed 0.20 K/decade trend, a 3 K seasonal cycle, a 1.4 K oscillation and 0.35 K noise |
| 06 | a tilted plane plus a Gaussian hill and a ripple on a 30 m grid, with known analytic gradients |

Real products are named only in prose, with a verified URL, and are never fetched by
a demonstration. Where a lesson needs to describe a real archive it says so and
points at the source, for example the Copernicus Climate Data Store
(<https://cds.climate.copernicus.eu>) for monthly reanalysis.

Two consequences of the synthetic-data policy are worth stating. First, a
synthetic field lets every derived quantity be checked against an imposed value —
which is how the lessons can report that a trend of 0.20 K/decade is recovered to
0.16 %, or that a packing scheme's rms error is exactly `scale_factor / sqrt(12)`.
Second, a synthetic field cannot show what a real one would: masks, quality flags,
changing instrument mixes and incomplete coverage are absent, and each lesson says
what its cube omits.

## What this module does not cover

- **Writing efficient geospatial file formats at the byte level.** Lesson 01 reads
  the structure; it does not implement a writer beyond what `netCDF4` and `h5py`
  provide.
- **Vector data.** Geometries, CRSs on features and spatial joins are module
  [03-09 Geospatial Python](../09-geospatial-python/README.md).
- **Cartographic design.** Colormaps, typography and figure layout are module
  [03-05 Plotting, Visualisation and Scientific Figures](../05-plotting-and-visualisation/README.md).
- **Inversion and modelling on grids.** Solvers, adjoints and mesh generation are
  module [19 Numerical Modeling and HPC](../../19-numerical-modeling-hpc/README.md).
