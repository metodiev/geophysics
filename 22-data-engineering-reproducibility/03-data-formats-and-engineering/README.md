# Module 22-03 — Data Formats and Engineering

**Stages:** intermediate → research · **Prerequisites:** module 22-02 (or equivalent
familiarity with environments, workflows and data versioning).

This module is about the data as an engineered artefact: how it is represented, how it
is laid out for the queries that will be asked of it, how it is fetched, how it is
checked, and how it is described. The organising idea is that **a format and a layout
are bets on access patterns**, and every bet can be priced. The lessons therefore pair
each design decision with a measurement: text costs 39.6× the parse time of binary at
six decimals; a windowed read of a $1024 \times 1024$ grid carries a $4.00\times$
amplification unless the chunks match the window; 13 monthly fetch requests cost 352 s
less over than 365 daily ones; the threshold of a naive $3\sigma$ flagging rule drifts
by 40 % depending on the contamination while a robust one stays within 10 %; and eight
metadata fields with per-field omission rates below 10 % leave 24 % of a catalogue
unusable.

The second thread is that **failures in this layer are silent**. A truncated response,
a lost record, a stale output, a zero-filled gap, a wrong unit declaration and an
unmapped vocabulary term all produce plausible values with no error anywhere. Each
lesson therefore ends with the check that would have caught its failure: a round trip
for a format conversion, a reconciliation count for a pipeline, a completeness gate for
a fetch, a confusion matrix for a QC rule, and a validating parser for metadata.

The third thread is cost accounting at the object level. Storage, request counts and
object counts are different resources: ten years of daily grid snapshots is only 1.9 GB
but 3650 objects, and a layout optimised on a laptop can be request-bound on an object
store. The lessons compute all three and make the trade-offs explicit, because the
choice of layout is usually made once, by whoever wrote the first file.

All measurements in this module are **SYNTHETIC** or **exact for a generated model**:
arrays, catalogues, service parameters, pipelines and QC records are produced by the
demonstrations with chosen parameters, and the compression ratios are measured with
zlib on synthetic fields. No real service, catalogue or file store was queried, no
published service limit or standard's text is quoted, and every number is a property of
the stated model.

## Learning objectives

By the end of this module you will be able to:

1. Choose a file representation from the size, precision and parse-cost requirements of
   the data, and verify a conversion with a round trip.
2. Design a chunking and partitioning scheme from the query shapes and the storage
   backend's request cost, and report compression as a measurement rather than an
   assumption.
3. Build a pipeline whose retries are safe, whose writes are idempotent, and whose
   losses are detected by reconciliation.
4. Plan and record a programmatic fetch so that it can be re-run or explained.
5. Evaluate a QC rule with a confusion matrix, handle gaps explicitly, and state the
   false-positive budget of every threshold.
6. Specify machine-checkable metadata: a schema, a versioned vocabulary, canonical
   units and validating parsers.

## Prerequisites

- [22-02-02 Pinning Environments and Managing Dependencies](../02-reproducible-workflows/02-environment-pinning.md) —
  the environment in which the formats are read.
- [22-02-05 Data Versioning and Provenance Tracking](../02-reproducible-workflows/05-data-versioning.md) —
  the identifiers and provenance that metadata completes.
- [03-08-01 netCDF/HDF5 Formats and Self-Describing Data](../../03-scientific-computing/08-gridded-geospatial-data/01-netcdf-and-hdf5.md) —
  library-level familiarity with the self-describing formats.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Scientific File Formats: CSV, Parquet, HDF5, netCDF, Zarr](01-file-formats-scientific.md) | advanced | Six decimals of text cost 1.19× the size of binary64 and 39.6× the parse time; 12 decimals still change bits for 19 998 of 20 000 values |
| 02 | [Format Trade-Offs: Access Patterns, Compression, Portability](02-format-design-tradeoffs.md) | research | A $256 \times 256$ window carries a $4.00\times$ amplification; the optimal chunk is 128 locally and 256 on a store; the same code compresses 76.29× or 1.08× |
| 03 | [Designing Robust Data Pipelines for Earth Data](03-data-pipelines.md) | research | Eight 98 % stages give 85.1 % end-to-end; retries reach 99.9999 % for 2.041 % extra work and produce 0.999 % duplicates and 0.997 % silent losses |
| 04 | [Programmatic Access to Earth Data (FDSN, Earthdata, Copernicus)](04-getting-earth-data.md) | graduate | The window cap is the plan's most valuable number: 30-day windows cost 2933 s against 3285 s; a 13-request fetch has a 48.7 % failure chance |
| 05 | [Automated Quality Control and Flagging](05-data-quality-control.md) | advanced | A $3\sigma$ rule spends a 0.27 % budget; masking moves the naive threshold 40 % and takes recall from 0.740 to 0.470; a 30 % zero fill shrinks $\sigma$ from 1.0069 to 0.8677 |
| 06 | [Metadata Standards and Controlled Vocabularies](06-metadata-standards.md) | research | Eight fields under 10 % missing leave 24 % of records unusable; 9 sensor terms collapse to 3 classes with 15 % unmapped; 76 % of units need a conversion |

## Suggested path

**If you are designing a data set:** read 01 for the representation and 06 for the
metadata, then 02 for the layout. Those three decide what the archive costs to keep and
what it costs a reader to use.

**If you are ingesting data:** read 03 and 04 in that order, then 05 for the checks that
catch what the pipeline cannot.

**If you are auditing someone else's archive:** read 06 §2–4 (is the metadata there and
machine-readable), 02 §2 (what does a query cost), and 03 §6 (what happens when a fetch
is partial). Those three questions find most of the problems.

**If you are here for the measurements:** every demo is self-contained and runs in
under a second; read each lesson's assumptions section before its results, and use the
★★★ exercises, which ask you to design a measurement rather than repeat one.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-file-formats-scientific.md`](01-file-formats-scientific.md) | Lesson 01 |
| [`02-format-design-tradeoffs.md`](02-format-design-tradeoffs.md) | Lesson 02 |
| [`03-data-pipelines.md`](03-data-pipelines.md) | Lesson 03 |
| [`04-getting-earth-data.md`](04-getting-earth-data.md) | Lesson 04 |
| [`05-data-quality-control.md`](05-data-quality-control.md) | Lesson 05 |
| [`06-metadata-standards.md`](06-metadata-standards.md) | Lesson 06 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Six runnable demonstrations |

| Script | What it measures |
|---|---|
| [`code/file_formats_scientific_demo.py`](code/file_formats_scientific_demo.py) | Representation sizes, round-trip precision at 3–12 decimals, parse cost, format capability table |
| [`code/format_design_tradeoffs_demo.py`](code/format_design_tradeoffs_demo.py) | Read amplification for four layouts, bytes-plus-requests cost on two backends, measured compression, storage and object counts |
| [`code/data_pipelines_demo.py`](code/data_pipelines_demo.py) | End-to-end success with and without retries, expected attempts, Monte Carlo duplicates and losses, idempotence table |
| [`code/getting_earth_data_demo.py`](code/getting_earth_data_demo.py) | Fetch plans at three window lengths, binding constraints, retry arithmetic, the five fields of a fetch record |
| [`code/data_quality_control_demo.py`](code/data_quality_control_demo.py) | Confusion matrices for three rules in two scenarios, threshold stability, gap-fill effects |
| [`code/metadata_standards_demo.py`](code/metadata_standards_demo.py) | Field and record completeness, vocabulary mapping and residue, unit conversions, ISO 8601 parsing |

## How to run the demos

```bash
cd 22-data-engineering-reproducibility/03-data-formats-and-engineering/code

/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python file_formats_scientific_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python format_design_tradeoffs_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python data_pipelines_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python getting_earth_data_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python data_quality_control_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python metadata_standards_demo.py
```

Every demo prints labelled results with units, seeds its random numbers with
`np.random.default_rng(20261014)`, uses no network access, writes no files and exits 0.
Each runs in well under a second.

## Mastery checkpoint

Complete this without notes, using the demonstrations only to check arithmetic:

> A group ingests a 12-million-row catalogue and a daily $2000 \times 2000$ gridded
> product from a public service, and publishes figures from both.
> **(a)** Compute the size of a $100 \times 100$ window read from the grid under
> chunks of 100 and of 400, and state which layout you would choose on an object store.
> **(b)** State the parse-time ratio of a text catalogue to a binary one, and what you
> would measure before converting.
> **(c)** Their ingest silently loses records about once a fortnight; name the failure,
> the gate that detects it, and why retries do not help.
> **(d)** State the five fields their fetch must record so a reprocessing at the service
> can be distinguished from their own error.
> **(e)** A $3\sigma$ QC rule removes 6 % of the grid's samples; state the
> false-positive budget at that threshold and two changes that make the removal
> auditable.
> **(f)** Their catalogue declares `unit = "gal"` for a column the analysis treats as
> m/s²; state the factor, the check that catches it, and the metadata change that
> prevents it.

Worked versions of (a)–(f) appear in the lesson solutions at ★★ and ★★★ level.

## Common pitfalls across this module

1. **Choosing a representation by habit.** Text at six decimals is larger than binary64
   and 39.6× slower to parse; the smallest file is not the readable one.
2. **Optimising the layout on the wrong backend.** The optimal chunk moves from 128 to
   256 when the request latency rises from 0.1 ms to 20 ms.
3. **Assuming a compression ratio.** 76.29× and 1.08× come from the same code on the
   same shape and dtype.
4. **Trusting a successful response.** Truncation, silent loss and partial coverage all
   look like success; only a reconciliation against the plan detects them.
5. **Deleting what QC flags.** Flag and keep, or the decision cannot be revisited.
6. **Writing metadata in prose.** A unit in a comment is not checkable; a unit in an
   attribute that a validator reads is.

## Related modules

- [22-02 Reproducible Research Workflows](../02-reproducible-workflows/README.md) —
  the environments, workflows and versioning that frame these data decisions.
- [22-04 Databases and Large Data Collections](../04-databases-and-large-data/README.md) —
  where the same data live at scale.
- [17-07 Earth Observation Data](../../17-remote-sensing-gis/07-earth-observation-data/README.md) —
  an application view of programmatic access.
- [03-08 Gridded Geospatial Data](../../03-scientific-computing/08-gridded-geospatial-data/README.md) —
  the library-level treatment of self-describing formats.
