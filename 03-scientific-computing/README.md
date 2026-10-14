# 03 — Scientific Computing and Python

**Stages:** beginner → graduate (with advanced and doctoral modules)

Geophysics is a computational science. A measurement is not a result until it
has been read, cleaned, reduced, modelled, inverted, plotted and stored — and
Python is the language in which essentially all of that happens today, in
research and in industry alike. This folder builds the computational skill the
rest of the curriculum assumes, and it does so in **dependency order**: nothing
here uses a library that a later module has not introduced.

The organising principle is that **a program is a scientific instrument**. An
instrument has a specification (what it claims to measure), a calibration (does
it return the right number on a known input?), a precision (how many digits
survive?), a failure mode (what does it do on bad data?) and a cost (how long,
how much memory?). Every lesson in this folder asks those five questions of the
code it teaches. A syntax tour asks none of them.

Two consequences follow, and they are the folder's two rules:

1. **Every container, dtype and control structure is justified by a measurement
   problem.** A dictionary is taught because a 10⁵-station lookup cannot be a
   list scan; a generator is taught because a 10 GB waveform file does not fit in
   memory; `float64` is taught because a gravity survey resolves part in 10⁹.
2. **Every number in a lesson is computed.** The demos in each module's `code/`
   directory are runnable, and the lessons quote their real output. Where a
   quantity is a nominal rock property or a synthetic data set, the text says so
   in the same sentence.

## Learning objectives for the folder

By the end of this folder you will be able to:

1. Write correct, readable Python that solves a geophysical problem from a
   description, using only the standard library where that is sufficient and a
   library where it is genuinely better.
2. Choose the right data structure for a task on the evidence of its complexity,
   and explain in one sentence why a quadratic algorithm is a scaling error and
   not a micro-optimisation.
3. Read, validate and clean real tabular and gridded geophysical data, including
   its encodings, missing values, units and metadata.
4. Vectorise numeric work with NumPy, and state when vectorisation is *not* the
   answer — because the problem is I/O-bound, or because the kernel is not
   elementwise.
5. Assemble an end-to-end pipeline: a survey or catalogue in a file, a physical
   reduction, an uncertainty estimate, a publication-shaped figure and a
   reproducible script.
6. Handle the formats the discipline actually uses: CSV and columnar text,
   netCDF and xarray grids, GeoJSON and shapefiles, miniSEED and stationXML.
7. Write tests, profile the result, and package it so that another person can
   install and reproduce it.

## Modules

Modules are in dependency order. Module numbers are *not* difficulty labels: the
first five are beginner material, but module 12 depends on all of them.

| # | Module | Focus | Why it matters downstream |
|---|---|---|---|
| 01 | [Python Programming Fundamentals](./01-python-fundamentals/README.md) | Types, control flow, functions, containers, I/O, exceptions, classes, generators, decorators | The instrument itself; everything else is a library on top of it |
| 02 | [NumPy and Array Computing](./02-numpy/README.md) | ndarray, dtypes, slicing, broadcasting, ufuncs, linear algebra, reproducibility | The array model that SciPy, pandas, xarray and ObsPy all share |
| 03 | [SciPy for Scientific Computing](./03-scipy/README.md) | Quadrature, ODE integration, optimisation, interpolation, signal, sparse, ndimage | The numerical methods of the curriculum, already written and tested |
| 04 | [Pandas and Tabular Geophysical Data](./04-pandas/README.md) | Series, DataFrame, indexing, cleaning, group-by, joins on irregular time | Earthquake catalogues, station lists, well logs, survey sheets |
| 05 | [Plotting, Visualisation and Scientific Figures](./05-plotting-and-visualisation/README.md) | Matplotlib object model, error bars, colour, maps, figures for publication | A result nobody can read is not a result; also the figure ethics of geophysics |
| 06 | [Jupyter, Notebooks and Literate Computing](./06-jupyter-and-notebooks/README.md) | Notebook execution model, hidden state, literate analysis, export | Reproducible exploration, and the discipline that keeps it reproducible |
| 07 | [SymPy and Symbolic Computation](./07-sympy/README.md) | Symbolic algebra, calculus, equation solving, code generation | Deriving the formulas the numeric modules then implement |
| 08 | [xarray, netCDF, and Gridded Earth Data](./08-gridded-geospatial-data/README.md) | Labelled N-dimensional arrays, netCDF, chunking, time coordinates | Every climate, gravity, magnetic and bathymetry grid |
| 09 | [GeoPandas and Geospatial Python](./09-geospatial-python/README.md) | Geometries, CRS and reprojection, spatial joins, raster/vector overlay | Site selection, station geometry, anomaly maps, land/sea masks |
| 10 | [ObsPy and Seismological Data Handling](./10-obspy-and-seismic-data/README.md) | miniSEED/StationXML, inventories, instrument response, preprocessing | The entry point to all observational seismology |
| 11 | [PyGMT and Professional Mapping](./11-pygmt-and-mapping/README.md) | Cartographic projections, shaded relief, colour palettes, map annotation | Maps that a journal and a reader will accept |
| 12 | [Building Numerical Simulation Code in Python](./12-numerical-simulation-python/README.md) | Stencils, boundary conditions, stability, verification, structure of a solver | The bridge from this folder to the modelling and inversion folders |
| 13 | [Testing, Profiling, and Packaging](./13-testing-profiling-packaging/README.md) | pytest, assertions and floating-point comparison, profiling, environments, packaging | What makes code trustworthy to someone who is not you |

## The dependency spine

Three chains carry most of the weight downstream:

```text
03-01 Fundamentals ──> 03-02 NumPy ──┬──> 03-03 SciPy ──────────> 19 Numerical Modelling, 18 Inverse Problems
                                     ├──> 03-04 pandas ─────────> 21 Statistics & ML, 22 Data Engineering
                                     ├──> 03-08 xarray/netCDF ──> 16 Climate, 12 Global Geophysics
                                     └──> 03-10 ObsPy ──────────> 06 Seismology, 20 Signal Processing

03-01 Fundamentals ──> 03-05 Plotting ──> 03-11 PyGMT ──> 24 Papers & Writing
03-01 Fundamentals ──> 03-13 Testing/Profiling/Packaging ──> every project in 25 Projects
03-01 Fundamentals ──┬──> 03-06 Notebooks
                     └──> 03-07 SymPy ──> derivation support for 01 Mathematics and 02 Physics
03-02 NumPy + 03-04 pandas ──> 03-09 GeoPandas ──> 17 Remote Sensing & GIS, 11 Exploration Geophysics
```

**Three rules of thumb that follow from this map:**

1. **Module 01 and 02 are load-bearing.** Reading a trace, fitting a curve,
   inverting a travel-time curve and inverting a gravity profile all reduce to
   array arithmetic and an explicit loop over stations. If the fundamentals are
   shaky, every later module is slower than it needs to be.
2. **Module 12 is where programming becomes geophysics.** It is the first module
   in the folder whose correctness criterion is physical (does the numerical
   solution converge to the analytic one?) rather than syntactic.
3. **Module 13 pays for itself the first time you re-run an experiment.** Version
   control, a test suite and a pinned environment are what turn "it worked on my
   laptop in March" into a result.

## Suggested path

**If you are new to programming (beginner path).** Work the thirteen modules in
numeric order,
and do not skip module 01. Expect module 01 to take the longest per lesson and
module 06 the shortest. Type every demo rather than reading it — the standard
library demos in module 01 are deliberately small enough to retype. Stop at the
end of module 05 and build something of your own from a data set you care about
before continuing; the remaining modules are much easier once you have one
complete pipeline behind you.

**If you already program (experienced path), in Python or another language.** Read
[01-python-fundamentals](./01-python-fundamentals/README.md) as a reference and
diagnostic: attempt the ★★★ problems of its exercises, and read only the lessons
whose problems you cannot close. Then take modules **02, 03, 04, 05, 13** in that
order, because that is the working core for almost every task in later folders.
Treat **08, 09, 10, 11** as format modules: read the one whose data you have in
front of you. If you come from MATLAB, module 02 is the one that matters most —
the shift is from a mutable global workspace to explicit arrays and functions.

**If you are here for a specific later folder.** The mapping is direct:

| Later folder | Take these modules |
|---|---|
| 06 Seismology | 01, 02, 03, 05, 10, 20 |
| 07 Gravity & Geodesy | 01, 02, 03, 05, 08, 09 |
| 08 Geomagnetism & EM | 01, 02, 03, 05, 08 |
| 10 GPR & Near-Surface | 01, 02, 03, 05, 09 |
| 11 Exploration Geophysics | 01, 02, 03, 04, 05, 09, 11 |
| 14 Hydrology & Hydrogeophysics | 01, 02, 03, 04, 08, 09 |
| 16 Atmosphere & Climate | 01, 02, 03, 08, 04 |
| 17 Remote Sensing & GIS | 01, 02, 08, 09, 11 |
| 18 Inverse Problems | 01, 02, 03, 12, 13 |
| 19 Numerical Modelling & HPC | 01, 02, 03, 12, 13 |
| 21 Statistics, Bayesian & ML | 01, 02, 04, 05, 13 |
| 22 Data Engineering & Reproducibility | 01, 04, 08, 13 |
| 25 Projects & Capstone | all of them |

## Mastery checkpoint for the folder

Produce one integrated artefact, in a directory with a README:

> **Take a real (or clearly labelled synthetic) geophysical data set, and turn it
> into a checked, reproducible result.** Specifically: read it from its actual
> on-disk format; validate it and *report* what you had to discard and why;
> reduce it with a formula you can derive and whose units you can state; compute
> the answer *with* an uncertainty; produce one publication-shaped figure and one
> machine-readable output file; and leave behind a script, a test suite, and a
> pinned environment that another person can run to obtain the same numbers.
> Then write one page answering: which container did you choose and why, which
> dtype, what was the complexity of the expensive step, and which of your
> assumptions would break first on a different data set?

This single artefact exercises modules 01, 02, 03, 04, 05 and 13 at once, and it
is exactly the deliverable that
[22-data-engineering-reproducibility](../22-data-engineering-reproducibility/README.md)
and [25-projects-capstone](../25-projects-capstone/README.md) then build on.

## A caution about libraries

The scientific Python ecosystem moves. Functions are renamed, defaults change,
and a routine that was fast in one release is a compatibility shim in the next.
Two habits keep a code base alive for a decade:

- **Pin what you depend on.** `environment.yml` and `requirements.txt` exist in
  this repository for that reason. Record versions with the results.
- **Know what the library is doing.** The difference between a correct and an
  incorrect use of a library function is almost always an assumption the
  documentation states and the tutorial skips — a periodic versus non-periodic
  boundary condition, an axes argument, a one-sided derivative at an endpoint.
  This folder teaches the *method* alongside the call, so that the failure is
  visible when it happens.

The reverse also matters: do not reimplement what is already correct and tested.
Write your own quadrature only to learn quadrature, then use
[SciPy](https://scipy.org). Write your own FFT never.

## Conventions used throughout

| Convention | Meaning here |
|---|---|
| `ENVIRONMENT` | The pinned interpreter and packages in [`environment.yml`](../environment.yml) |
| Nominal property | A typical value for teaching, not a measurement of a named sample |
| SYNTHETIC | Data generated by the code itself, with a fixed seed, and labelled as such in its own header |
| `float64` | IEEE-754 double, the default real type in Python and NumPy |
| Stdlib-only | The demo imports nothing outside the Python standard library |
| Unit in the name | `depth_km`, `velocity_m_s`, `anomaly_mgal` — units travel with the variable |

Numeric constants used across the folder come from the standards bodies, not from
memory: the CODATA fundamental constants from
[NIST](https://physics.nist.gov/cuu/Constants/), earthquake catalogue queries
from the [USGS FDSN event service](https://earthquake.usgs.gov/fdsnws/event/1/),
waveforms from [EarthScope/IRIS Data Services](https://ds.iris.edu/ds/nodes/dmc/),
and coordinate systems from [EPSG](https://epsg.org).

## Related folders

- [01-mathematics](../01-mathematics/README.md) — numerical methods, floating
  point, linear algebra and probability; module 01 here is the *implementation*
  of what that folder proves.
- [02-physics](../02-physics/README.md) — the models this folder computes.
- [05-core-geophysics](../05-core-geophysics/README.md) — the first folder that
  consumes these tools wholesale.
- [22-data-engineering-reproducibility](../22-data-engineering-reproducibility/README.md)
  — where module 13's practices become a workflow.
- [26-reference-library](../26-reference-library/README.md) — symbols, units and
  constants used in every listing here.
