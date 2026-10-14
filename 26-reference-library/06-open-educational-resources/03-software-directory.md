---
id: 26-06-03
title: "Software Directory: Open-Source Geophysics Tools"
level: advanced
prereqs: []
estimated_minutes: 25
tags: [reference, software, open-source, tools]
---

# Software Directory: Open-Source Geophysics Tools

A directory of the open-source software used across this curriculum and its
neighbours: data access, processing, forward modelling, inversion, geospatial
handling, plotting and reproducible computation. Each project is named with its
access point, its usual licence position and an honest statement of what it is
and is not.

## How to use this page

Choose by task, not by reputation. The table format deliberately gives "not for"
for every project, because the most common software failure in geophysics is
using an excellent tool outside the problem class it was designed for. Where a
project's licence is stated, it is the licence the project publishes; **verify it
in the repository before redistribution**, because projects relicense.

All access points here are registered in
[`tools/verified_links.tsv`](../../tools/verified_links.tsv) with the HTTP status
observed when last checked.

*Provenance of this page:* a software directory. No code is reproduced or
redistributed by this repository.

## Seismological data access and processing

| Project | Access point | Typical licence | Use it for | Not for |
|---|---|---|---|---|
| ObsPy | [obspy.org](https://www.obspy.org), [docs](https://docs.obspy.org), [source](https://github.com/obspy/obspy) | LGPL-3 | Reading MiniSEED/SAC/StationXML, FDSN client access, instrument deconvolution, filtering, beamforming, TauP integration | Large-scale seismic imaging; it is a processing toolkit, not an imaging package |
| ObsPy FDSN client | [Client API](https://docs.obspy.org/packages/autogen/obspy.clients.fdsn.client.Client.html) | LGPL-3 | Querying station, dataselect and event services portably | Anything requiring a service that does not implement the FDSN contract |
| ObsPy Trace and Stream | [Trace](https://docs.obspy.org/packages/autogen/obspy.core.trace.Trace.html), [Stream](https://docs.obspy.org/packages/autogen/obspy.core.stream.Stream.html) | LGPL-3 | The core containers and their methods | — |
| ObsPy array analysis | [array_processing](https://docs.obspy.org/packages/autogen/obspy.signal.array_analysis.array_processing.html) | LGPL-3 | Beamforming and f–k analysis of arrays | Array design; you must supply a sensible geometry |
| ObsPy TauP | [obspy.taup](https://docs.obspy.org/packages/obspy.taup.html) | LGPL-3 | Travel times, ray paths and phase identification from 1-D models | Any 3-D structure |
| TauP | [seis.sc.edu/taup/](https://seis.sc.edu/taup/) | Open (Java reference implementation) | Independent cross-checking of travel times and phase names | Being the last word on Earth structure |
| Pyrocko | [pyrocko.org](https://pyrocko.org) | GPL-3 | Earthquake source studies, waveform databases, synthetic seismograms | General-purpose GIS |
| SAC (Seismic Analysis Code) | [IRIS/EarthScope software downloads](https://ds.iris.edu/ds/nodes/dmc/software/downloads/) | Distributed by the data centre; check terms | Classic interactive seismogram analysis; still standard in observatory work | Automated, scriptable large-scale processing |

## Potential fields, EM, and inversion frameworks

| Project | Access point | Typical licence | Use it for | Not for |
|---|---|---|---|---|
| SimPEG | [simpeg.xyz](https://simpeg.xyz) | MIT | Simulation and gradient-based inversion across EM, potential fields and flow; excellent documentation | Interactive teaching at first-year level |
| PyGIMLi | [pygimli.org](https://www.pygimli.org) | GPL-3 (check current terms) | Geophysical inversion and modelling with a strong geoelectrics and hydrogeophysics tradition | Very large 3-D problems |
| Fatiando a Terra | [fatiando.org](https://www.fatiando.org) | BSD-3 | Modular forward modelling, gravity/magnetic processing and inversion building blocks | A single integrated application |
| Madagascar | [ahay.org](https://www.ahay.org) | GPL (as published by the project) | Reproducible seismic processing through scripts with provenance | Interactive interpretation |
| SeisUnix | [seismic-unix.org](https://seismic-unix.org) | GPL as stated by the project | The classic Unix seismic processing suite: sorting, velocity analysis, migration | Modern Python interoperability, though it exists |
| ASPECT | [aspect.geodynamics.org](https://aspect.geodynamics.org) | GPL-2+ as stated by the project | Mantle convection and lithospheric deformation modelling with adaptive meshes | Short-timescale seismology |
| CIG software collection | [geodynamics.org](https://geodynamics.org) | Varies by code | Community modelling codes for geodynamics, seismology and tectonics | One-size-fits-all workflows |

## Geospatial data handling, formats and plotting

| Project | Access point | Typical licence | Use it for | Not for |
|---|---|---|---|---|
| GDAL | [gdal.org](https://gdal.org) | MIT/X | Reading and writing essentially every raster and vector format | Analysis; it is a translation layer |
| PROJ | [proj.org](https://proj.org) | MIT/X | Coordinate transformations | Deciding which transformation is right; the registry does that |
| pyproj | [pyproj4.github.io/pyproj/](https://pyproj4.github.io/pyproj/) | MIT | Python access to PROJ | — |
| GeoPandas | [geopandas.org](https://geopandas.org) | BSD-3 | Vector dataframes, spatial joins, attribute analysis | Raster processing |
| Shapely | [shapely.readthedocs.io](https://shapely.readthedocs.io) | BSD-3 | Planar geometry operations | Geodesic (spherical) geometry, which needs different tools |
| Cartopy | [cartopy.readthedocs.io](https://cartopy.readthedocs.io) | LGPL-3 | Publication-quality map projections for Matplotlib figures | Large-scale image processing |
| PyGMT | [pygmt.org](https://pygmt.org) | BSD-3 (binding), LGPL-3 (GMT) | GMT-quality maps and grid operations from Python | Interactive editing |
| GMT | [generic-mapping-tools.org](https://www.generic-mapping-tools.org), [documentation](https://docs.generic-mapping-tools.org) | LGPL-3 | Map production and grid processing at research quality | Being a GIS |
| segyio | [segyio.readthedocs.io](https://segyio.readthedocs.io) | LGPL-3 | Reading and writing SEG-Y seismic files | Interpretation |
| lasio | [lasio.readthedocs.io](https://lasio.readthedocs.io) | MIT | Reading borehole LAS well-log files | Log interpretation |
| Natural Earth | [naturalearthdata.com](https://www.naturalearthdata.com) | Public domain | Base maps for cartography | Measurement (see module 26-05) |

## Numerics, arrays, data and documentation

| Project | Access point | Typical licence | Use it for | Not for |
|---|---|---|---|---|
| NumPy | [numpy.org](https://numpy.org) | BSD-3 | Arrays, linear algebra, FFT, random generators | Symbolic mathematics |
| NumPy random generators | [Generator API](https://numpy.org/doc/stable/reference/random/generator.html) | BSD-3 | Reproducible random draws with explicit seeds | Cryptographic randomness |
| SciPy | [scipy.org](https://scipy.org), [docs](https://docs.scipy.org/doc/scipy/) | BSD-3 | Optimisation, signal processing, statistics, special functions, integration | Replacing domain-specific geophysical codes |
| pandas | [pandas.pydata.org](https://pandas.pydata.org) | BSD-3 | Tabular data and time series | Very large array data, where Xarray or Dask fit better |
| Xarray | [xarray.dev](https://xarray.dev), [docs](https://docs.xarray.dev) | Apache-2.0 | Labelled n-dimensional arrays with coordinates | Non-gridded data, which needs GeoPandas |
| cf-xarray | [cf-xarray.readthedocs.io](https://cf-xarray.readthedocs.io) | Apache-2.0 | CF-aware accessors for Xarray | Files that do not follow CF |
| netCDF4-python | [unidata.github.io/netcdf4-python/](https://unidata.github.io/netcdf4-python/) | MIT-style (Unidata) | Low-level NetCDF I/O | High-level analysis |
| Zarr | [zarr.readthedocs.io](https://zarr.readthedocs.io) | MIT | Chunked, cloud-friendly array storage | Archival formats required by agencies |
| Dask | [docs.dask.org](https://docs.dask.org) | BSD-3 | Parallel and out-of-core computation over large arrays | Real-time processing |
| HDF5 (via h5py) and NetCDF | see project documentation | BSD-style | Container formats for large gridded data | — |
| Matplotlib | [matplotlib.org](https://matplotlib.org) | BSD-style | Publication figures | Interactive GIS-style exploration |
| Jupyter | [jupyter.org](https://jupyter.org) | BSD-3 | Notebooks for teaching and exploratory analysis | Long-running production pipelines |
| Jupyter Book | [jupyterbook.org](https://jupyterbook.org) | BSD-3 | Building books and course material from notebooks and Markdown | A general-purpose web framework |
| pytest | [pytest documentation](https://docs.pytest.org/en/stable/) | MIT | Tests for numerical code, including `approx` for floating-point comparisons | — |
| scikit-learn | [scikit-learn.org](https://scikit-learn.org) | BSD-3 | Classical machine learning with solid validation tooling | Deep-learning architectures |
| TensorFlow | [tensorflow.org](https://www.tensorflow.org) | Apache-2.0 | Deep learning at scale | Problems better served by a smaller model |
| PyTorch | [pytorch.org](https://pytorch.org), [install selector](https://pytorch.org/get-started/locally/) | BSD-3 | Research-grade deep learning, including differentiable geophysical modelling | — |

## Choosing a licence-aware workflow

| Practice | Why it matters |
|---|---|
| Record the version of every tool | Results change between releases, especially in coordinate transformation and optimisation defaults |
| Record the licence alongside the tool | Redistribution of a derived product can inherit the tool's terms |
| Prefer a package manager and an environment file | Reproducibility per [22-data-engineering-reproducibility](../../22-data-engineering-reproducibility/README.md) |
| Test the pipeline on synthetic data with a known answer | Catches the wrong-parameter and wrong-convention errors that unit tests miss |
| Cite the software in publications | Many projects publish a citable paper as well as a repository |

## Caveats

- **"Open source" is not "open data".** A tool's licence governs the code; the
  data it reads have their own licences.
- **GPL-family licences have distribution consequences** for combined works;
  check before shipping a derived product.
- **Project activity varies.** A repository with no commits for several years may
  still be the best tool for its niche — but pin the version you tested.
- **Documentation is not validation.** A well-documented wrong parameter choice
  still gives a wrong answer; validate on synthetic cases with known answers.
- **This directory is not exhaustive**, and it is a snapshot: verify the licence
  and the current version at the project site before relying on either.

## Related pages

- [OER: Mathematics, Physics and Computing](./01-oer-mathematics.md)
- [OER: Geophysics, Seismology and Earth Science Courses](./02-oer-geophysics.md)
- [Data Licensing, Attribution and Reuse Policy](./04-data-policy-and-licences.md)
- [Synthetic Data Generators for Learning and Testing](../05-open-datasets-catalogue/06-datasets-synthetic.md)
- [03-scientific-computing folder overview](../../03-scientific-computing/README.md)
