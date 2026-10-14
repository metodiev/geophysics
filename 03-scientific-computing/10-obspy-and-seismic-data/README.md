# Module 03-10 — ObsPy and Seismological Data Handling

**Stages:** intermediate → advanced · **Prerequisites:**
[03-01-04 Functions, Scope, Modules and Packages](../01-python-fundamentals/04-functions-modules.md)
for how a package namespaces its functions,
[03-02-01 ndarray Creation, dtypes, Shapes and Strides](../02-numpy/01-ndarray-basics.md)
for the array model that every waveform is, and
[03-01-04](../01-python-fundamentals/04-functions-modules.md) for the module
and package mechanics. For the filtering material you also want
[03-03-05 scipy.signal: Filters, Windows and Spectral Estimation](../03-scipy/05-signal.md).

ObsPy is the reason observational seismology is done in Python. It reads every
format the archives use, it carries the metadata with the data, it implements
the processing operations that are standard in the discipline, and it bundles
the reference travel-time code with its standard Earth models. This module
teaches the library by measuring it: every number quoted in a lesson is printed
by a script in `code/`, and every convention — including two that contradict
the documentation — was verified against a synthetic case with a known answer.

## Scope

The module covers the whole path from a file on disk to a physical quantity:

1. the data model (`Trace`, `Stream`, `UTCDateTime`), and what a "count" is;
2. the two file formats that hold almost all waveform data, and their
   differences in precision, size and metadata;
3. the instrument response, and the deconvolution that turns counts into
   ground motion — including what the water level costs;
4. event catalogs, magnitudes, and the geodesy that joins events to stations;
5. preprocessing: detrend, taper, filter, decimate, in an order that can be
   defended;
6. travel times and phase naming, with a measured verification of the slowness
   identity;
7. cross-correlation, polarisation and array processing, with every convention
   measured;
8. FDSN web services: what to request, how to validate what arrives, and how to
   make a download reproducible.

## Two habits this module insists on

**Every routine is checked against a case whose answer is known.** A correlation
lag is measured on a synthetic delay; a back-azimuth on a synthetic arrival; a
beamformer against an independent implementation; a travel time against its own
derivative; a deconvolution against a forward model built from the same
response. Nothing is accepted because a docstring says so.

**Nothing is downloaded.** Every demonstration runs offline. Waveforms are
synthesised from `numpy` arrays with stated seeds, models come from ObsPy's
bundled `iasp91`, and the FDSN lesson prints the requests a reader would make
when online rather than pretending to have made them. Two measured
consequences of this discipline appear in the lessons: the docstring of
`array_processing` says the slowness column is in s/deg and the measurement
says s/km; and ObsPy 1.5.1 cannot represent a leap second, measured three ways.

## Prerequisites

- Python functions and modules; you will import from subpackages constantly.
- NumPy arrays, dtypes and slicing; `Trace.data` is an array and every
  processing operation is an array operation.
- Comfort with the frequency domain at the level of
  [03-03-05](../03-scipy/05-signal.md), because the response, the filters and
  the deconvolution all live there.
- No prior seismology. Phase names, magnitudes and the shadow zone are
  introduced here and developed in
  [06-seismology](../../06-seismology/README.md).

## Lesson map

| # | Lesson | Level | Key idea |
|---|---|---|---|
| 01 | [ObsPy Architecture and Data Models](./01-obspy-overview.md) | intermediate | `Trace` is an array plus checked metadata; counts are not a physical unit; ObsPy timestamps ignore leap seconds |
| 02 | [Reading MiniSEED/SAC: Trace and Stream](./02-reading-waveforms.md) | intermediate | Steim compression depends on the signal; SAC stores `float32`; gaps are not data |
| 03 | [StationXML Inventory, Response and Instrument Correction](./03-inventory-and-metadata.md) | advanced | Deconvolution needs a water level, and the clamp frequency must fall below the lowest frequency you keep |
| 04 | [Event Catalogs, QuakeML and Phase Metadata](./04-catalog-and-events.md) | intermediate | Depth is in metres; magnitude scales are different measurements; three definitions of distance |
| 05 | [Preprocessing: Detrend, Taper, Filter, Decimate](./05-filtering-detrending.md) | intermediate | Aliasing folds *into* the signal band; a causal filter shifts arrivals by 156 ms |
| 06 | [Travel Times with TauP and Phase Naming](./06-taup-travel-times.md) | intermediate | The ray parameter is `dT/dΔ`, verified numerically; the shadow zone is measured, not asserted |
| 07 | [Cross-Correlation, Polarisation and Array Processing](./07-obspy-advanced.md) | advanced | Measure the convention of every routine; two implementations agreeing is the only evidence |
| 08 | [Fetching Data from FDSN Web Services](./08-fdsn-clients.md) | intermediate | A query is a contract; validate what arrives; cache and record provenance |

## How to run the demos

All eight scripts run with the project virtual environment and need no network:

```
.venv/bin/python 03-scientific-computing/10-obspy-and-seismic-data/code/obspy_overview_demo.py
.venv/bin/python 03-scientific-computing/10-obspy-and-seismic-data/code/reading_waveforms_demo.py
.venv/bin/python 03-scientific-computing/10-obspy-and-seismic-data/code/inventory_and_metadata_demo.py
.venv/bin/python 03-scientific-computing/10-obspy-and-seismic-data/code/catalog_and_events_demo.py
.venv/bin/python 03-scientific-computing/10-obspy-and-seismic-data/code/filtering_detrending_demo.py
.venv/bin/python 03-scientific-computing/10-obspy-and-seismic-data/code/taup_travel_times_demo.py
.venv/bin/python 03-scientific-computing/10-obspy-and-seismic-data/code/obspy_advanced_demo.py
.venv/bin/python 03-scientific-computing/10-obspy-and-seismic-data/code/fdsn_clients_demo.py
```

Each script prints labelled sections with units, exits 0, and uses a fixed
`numpy.random.default_rng` seed so its output is reproducible. Scripts that
need scratch files create a directory inside `code/` and delete it before
exiting, so a run leaves the working tree clean.

## Companion exercises

Every lesson has paired exercise and solution files in [`exercises/`](./exercises/):
`NN-slug-exercises.md` and `NN-slug-solutions.md`, graded ★ (foundational),
★★ (applied) and ★★★ (research-oriented). Solutions quote the measured numbers
they rely on and, where a claim was corrected by measurement, say so.

## Where this module leads

- [06-seismology](../../06-seismology/README.md) uses these tools for real:
  ray theory, source parameters, location, tomography.
- [20-signal-processing](../../20-signal-processing/README.md) develops the
  filtering, deconvolution and array theory that this module uses.
- [22-data-engineering-reproducibility/03-data-formats](../../22-data-engineering-reproducibility/03-data-formats-and-engineering/01-file-formats-scientific.md)
  generalises the format and provenance questions to other data types.
