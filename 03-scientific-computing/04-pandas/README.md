# Module 03-04 — Pandas and Tabular Geophysical Data

**Stages:** beginner → advanced · **Prerequisites:**
[03-01-05 Lists, Tuples, Dictionaries, Sets and Complexity](../01-python-fundamentals/05-data-structures.md)
for the dictionary model the `DataFrame` is built on, and
[03-02-01 ndarray Creation, dtypes, Shapes and Strides](../02-numpy/01-ndarray-basics.md)
for the dtypes and shapes every column carries. The performance lesson also
assumes [03-02-07 Memory Layout, Strides and Cache-Aware Performance](../02-numpy/07-memory-performance.md).

Most geophysical data are tables. An earthquake catalogue has one row per event;
a station archive has one row per station-day; a survey has one row per station;
a model evaluation has one row per parameter combination. NumPy gives you a
rectangular block of numbers and an index of integers. pandas gives you the same
block of numbers with **axes that have names**, and that single addition removes a
whole class of bug — the one where a column is silently paired with the wrong
rows because two tables were sorted differently.

Two features distinguish this module from a general pandas tutorial:

- **One running example, cleaned honestly.** Every lesson works on the same
  synthetic earthquake catalogue: a real depth column with missing values, real
  duplicated reports, and real sentinel values where a solver gave up. The
  cleaning lesson states a policy, applies it, and reports how many rows each
  step removed, because that count is what makes the result auditable.
- **Every number in every lesson is a measured demo output.** The scripts in
  `code/` are run, their output is quoted, and where a measurement contradicts
  the folklore — as two do in lesson [07](./07-performance-pandas.md) — the
  contradiction is printed rather than smoothed over.

> ## The catalogue is SYNTHETIC
>
> Every event, station and time series in this module is **generated in-code**
> by [`code/synthetic_catalog.py`](./code/synthetic_catalog.py) from a fixed
> random seed, using a Gutenberg-Richter magnitude model.
>
> It is **not** the USGS catalogue, not the ISC bulletin, and not an observation
> of the Earth. The regions (Northvale, Eastmere, Southgate, Westhold) and the
> networks (SYN-NET1, SYN-NET2) are invented names.
>
> In particular, the b-value computed in lesson
> [06](./06-earthquake-catalog-pandas.md) is an **illustration of the
> calculation** and a check that the code recovers the generator's known input
> (b = 1.05). It is not a geophysical result, and no b-value from this module may
> be quoted as one. If you want real earthquakes, query the
> [USGS FDSN event service](https://earthquake.usgs.gov/fdsnws/event/1/).

The distinction that causes the most wasted time in tabular work is between a
**label** and a **position**. `.loc` addresses labels, `.iloc` addresses
positions, a boolean mask selects rows by condition, and every arithmetic
operation between two Series aligns on labels. Lesson [02](./02-indexing-selection.md)
makes the distinction unavoidable, including the chained-assignment trap that
pandas 3 reports as `ChainedAssignmentError` — a write that is silently discarded,
which is worse than an exception.

## Learning objectives

By the end of this module you will be able to:

1. **Explain** the labelled-data model — `Series`, `DataFrame`, index, dtype — and
   predict when an operation aligns by label and when it multiplies rows.
2. **Select** rows and columns with masks, `.loc` and `.iloc`, combine conditions
   correctly, and assign in one step so that no write is silently lost.
3. **Clean** a table with a stated, justified policy for missing values,
   duplicates and outliers, and **report the count of rows each step removed**.
4. **Aggregate** with `groupby`, split the statistics correctly between `agg` and
   `transform`, and reshape between long and wide forms with a verified round
   trip.
5. **Join** two tables with a stated cardinality, detect a non-unique-key row
   explosion before it reaches a total, and align irregular time series with an
   explicit choice between `reindex`, `resample` and `merge_asof`.
6. **Estimate** a magnitude-frequency relation as a worked pipeline, and state
   the estimator, completeness, sample size and sensitivity that a reported
   b-value requires.
7. **Choose** dtypes deliberately — including `category` for low-cardinality
   labels — measure the memory and speed consequences, and decide when NumPy, a
   database or a chunked reader is the right tool instead of pandas.

## Lessons

| # | Lesson | Level | Key idea |
|---|---|---|---|
| 01 | [Series, DataFrame and the Labeled-Data Model](./01-series-dataframe.md) | beginner | Labels turn an array into a dataset, and prevent the "which column was this" bug |
| 02 | [Indexing, Selection, loc/iloc and Boolean Masks](./02-indexing-selection.md) | beginner | `.loc` is labels, `.iloc` is positions, and a chained assignment writes nowhere |
| 03 | [Cleaning: Missing Values, Duplicates and Outliers](./03-cleaning-data.md) | intermediate | Every policy is a decision; report the rows it removed |
| 04 | [Group-By, Aggregation and Reshaping](./04-groupby-aggregation.md) | intermediate | Split-apply-combine, `size` vs `count`, and long ↔ wide |
| 05 | [Merging, Joining and Aligning Irregular Time Series](./05-merging-time-series.md) | intermediate | A non-unique key multiplies rows and inflates every total |
| 06 | [Case Study: Earthquake Catalogue Wrangling](./06-earthquake-catalog-pandas.md) | intermediate | **The mastery lesson**: the magnitude-frequency relation, end to end |
| 07 | [Performance, dtypes and When to Leave Pandas](./07-performance-pandas.md) | advanced | Memory, vectorisation, and the measurement that contradicts the folklore |

## Suggested path

**If you are working through the computing folder in order:** lessons 01–07 in
numeric order. Nothing here depends on the plotting module, but lesson
[05](./05-merging-time-series.md) is the natural bridge to
[03-06 Jupyter and Notebooks](../06-jupyter-and-notebooks/README.md) for keeping a
cleaning pipeline visible.

**If you have used pandas before and want the science:** start with
[03](./03-cleaning-data.md) §2 and §4 (the policy and the robust score), then
[05](./05-merging-time-series.md) §3 (the row explosion), then
[06](./06-earthquake-catalog-pandas.md) in full. Those three sections are where
experience does not help and measurement does.

**If you are here for seismology or hazard work:** read
[03](./03-cleaning-data.md), [04](./04-groupby-aggregation.md),
[05](./05-merging-time-series.md) and [06](./06-earthquake-catalog-pandas.md) in
full, then [03-10 ObsPy and Seismic Data](../10-obspy-and-seismic-data/README.md)
for reading real waveform and catalogue formats, and
[21-statistics-bayesian-ml](../../21-statistics-bayesian-ml/README.md) for the
inference that follows.

**If you are here for geospatial or gridded data:** read
[01](./01-series-dataframe.md) and [04](./04-groupby-aggregation.md), then
[03-08 Gridded and Geospatial Data](../08-gridded-geospatial-data/README.md) and
[03-09 Geospatial Python](../09-geospatial-python/README.md), which extend the
column-and-index model to coordinates and coordinate reference systems.

**If you are here for performance or production:** read
[07](./07-performance-pandas.md) in full, then
[03-13 Testing, Profiling and Packaging](../13-testing-profiling-packaging/README.md)
for turning a notebook pipeline into something that can be run again.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-series-dataframe.md`](./01-series-dataframe.md) … [`07-performance-pandas.md`](./07-performance-pandas.md) | The seven lessons |
| [`code/synthetic_catalog.py`](./code/synthetic_catalog.py) | The **SYNTHETIC** catalogue, station table and irregular series used by every demo |
| [`code/series_dataframe_demo.py`](./code/series_dataframe_demo.py) | Series anatomy, alignment, the positional-versus-label comparison, first inspection |
| [`code/indexing_selection_demo.py`](./code/indexing_selection_demo.py) | Masks, `loc`/`iloc`, and the chained-assignment warning as pandas 3 actually raises it |
| [`code/cleaning_data_demo.py`](./code/cleaning_data_demo.py) | Triage, missing-value policy, duplicate reports, robust versus non-robust outlier scores |
| [`code/groupby_aggregation_demo.py`](./code/groupby_aggregation_demo.py) | `size` vs `count`, named aggregation, `unstack`, `pivot_table`, `melt`, `transform` |
| [`code/merging_time_series_demo.py`](./code/merging_time_series_demo.py) | Unique and non-unique joins, the 391 → 1219 row explosion, `reindex`, `resample`, `merge_asof` |
| [`code/earthquake_catalog_demo.py`](./code/earthquake_catalog_demo.py) | The case study: histogram, cumulative counts, two b-estimators, completeness sensitivity |
| [`code/performance_dtypes_demo.py`](./code/performance_dtypes_demo.py) | Deep memory, `category`, downcast precision, loop versus mask, the three-way moving average, SQLite |
| [`exercises/01-…`](./exercises) … [`exercises/07-…`](./exercises) | Exercises and full worked solutions for every lesson |

Every script needs pandas, which is installed in the project virtual
environment. Run them; do not read them:

```
.venv/bin/python 03-scientific-computing/04-pandas/code/series_dataframe_demo.py
```

All timings printed by the performance demo are machine-dependent. The ratios are
the lesson; the milliseconds are not.

## Mastery checkpoint

Complete this without notes, from a clean interpreter.

> Using the cleaned synthetic catalogue of 391 events:
>
> **(a)** State the dtype of the `region` column in pandas 3 and say why a
> pandas 1.x tutorial prints something else.
> **(b)** Write a single expression selecting events with `mw >= 3.5` and
> `depth_km < 20`, and say whether `.loc` or `.iloc` is required.
> **(c)** A colleague runs `df[df["depth_km"] > 60]["agency"] = "DEEP"` and the
> column does not change. Explain what happened and give the repair.
> **(d)** The station table has fourteen rows sharing four region names. Predict
> the row count of `events.merge(stations, on="region")` and explain why a total
> computed afterwards is inflated by the same factor.
> **(e)** Compute `N(M >= 3.0)` and `N(M >= 4.0)` from the cumulative table
> (391, 148, 48, 16, 2 at magnitudes 2.0, 2.5, 3.0, 3.5, 4.0), and say what the
> ratio implies about `b` — and then say why that implication is not a result
> about the Earth.

Parts (a)–(c) are lesson [02](./02-indexing-selection.md); part (d) is lesson
[05](./05-merging-time-series.md) §3; part (e) is lesson
[06](./06-earthquake-catalog-pandas.md) §5.

**Worked answer for (d) and (e):**

The join produces `Σ_regions (n_events × n_stations) = 108×4 + 134×3 + 87×3 +
62×2 = 432 + 402 + 261 + 124 = 1219` rows. Every event is replicated once per
station in its region, so a per-event quantity summed after the merge counts each
event 2 to 4 times; the demo measures the inflation factor on radiated energy as
**3.1152**. A row count, checked before any total, is the guard.

For (e), `N(M >= 3.0) = 48` and `N(M >= 4.0) = 2`, a ratio of 24 against an
expected `10^b ≈ 11` for `b = 1.05`. That is not evidence for a large `b`: two
events in the upper decade means the ratio's uncertainty is of order 100 per
cent, and the generator's input — the only quantity it can legitimately be
compared against — is 1.05. Anything stronger must be stated as a statement about
the code, never about the Earth.

## Common pitfalls across this module

1. **Positional arithmetic on reordered data.** `a.to_numpy() - b.to_numpy()` is
   only correct if the two arrays are in the same order, and nothing enforces
   that.
2. **Unparenthesised comparisons.** `df[df.a > 1 & df.b < 2]` is a `TypeError`;
   the parenthesised form is the only correct one.
3. **Chained assignment.** `df[mask]["col"] = x` writes to a temporary and is
   discarded. pandas 3 raises `ChainedAssignmentError` as a warning and keeps
   going, which is exactly why it must be fixed rather than tolerated.
4. **`count()` when you meant `size()`.** Invisible until a column acquires a
   gap, at which point a rate is quietly wrong by up to about 13 per cent on this
   catalogue.
5. **Joining on a descriptive column.** A region name is a category, not an
   identifier; the row count multiplies and every total with it.
6. **`how="inner"` by habit.** It deletes unmatched keys silently; an outer join
   reports them.
7. **`merge_asof` without `tolerance`.** Early rows get paired with a measurement
   from outside any sensible window.
8. **`fillna(0)` for a quantity that cannot be zero.** Depth, magnitude, station
   count. Zero is a claim, not a convenience.
9. **Removing statistical outliers by default.** The robust score flags the deep
   regional structure; deleting it deletes the signal.
10. **Quoting a b-value without estimator, completeness, sample size and
    sensitivity.** Four things, or the number is not comparable with any other.
11. **Optimising without measuring.** Two of lesson [07](./07-performance-pandas.md)'s
    measurements contradict the folklore, on the same machine, in the same run.
12. **Treating a timing as portable.** Report ratios and the machine; the
    milliseconds belong to the run that produced them.

## Related folders

- [03-scientific-computing/02 NumPy and Array Computing](../02-numpy/README.md)
  — the array layer pandas columns are built on, and the dtypes they inherit.
- [03-scientific-computing/05 Plotting, Visualisation and Scientific Figures](../05-plotting-and-visualisation/README.md)
  — where a cleaned table becomes a figure, and a wrong dtype becomes a wrong axis.
- [03-scientific-computing/06 Jupyter, Notebooks and Literate Computing](../06-jupyter-and-notebooks/README.md)
  — restart-and-run-all is the only reliable detector of a silently dropped write.
- [03-scientific-computing/08 Gridded and Geospatial Data](../08-gridded-geospatial-data/README.md)
  and [09 Geospatial Python](../09-geospatial-python/README.md) — the same model
  with coordinates, CRSs and spatial joins.
- [03-scientific-computing/10 ObsPy and Seismic Data](../10-obspy-and-seismic-data/README.md)
  — reading real event and waveform formats into exactly these structures.
- [06-seismology/README.md](../../06-seismology/README.md) — the science that the
  catalogue statistics of lesson [06](./06-earthquake-catalog-pandas.md) serve.
- [21-statistics-bayesian-ml/README.md](../../21-statistics-bayesian-ml/README.md)
  — estimation, uncertainty and the completeness problem treated statistically.
- [26-reference-library/README.md](../../26-reference-library/README.md) — the
  open-datasets catalogue, for the real tables to point these tools at next.
