---
id: 03-04-07
title: "Performance, dtypes and When to Leave Pandas"
level: advanced
prereqs: ["03-04-01", "03-02-07"]
estimated_minutes: 90
tags: [pandas, performance, dtypes, memory, category, numpy, sqlite]
---

# Performance, dtypes and When to Leave Pandas

Sooner or later a table stops being small. A million-event catalogue, a decade of
daily data from a few hundred stations, or a gridded product flattened into rows
will exhaust the comfortable regime, and the response has to be measured rather
than guessed. This lesson is about the three levers that actually move: **dtype**,
**vectorisation**, and **choosing the right tool**.

It is also a lesson in scepticism. The folklore — "NumPy is faster than pandas",
"the `.str` accessor beats `apply`" — is true often enough to be repeated and
false often enough to be dangerous. Two of the measurements below contradict it,
on this machine, with this pandas build, and they are included precisely because
a rule you cannot falsify is not a rule.

> The table is **SYNTHETIC** — 600,000 rows generated in-code with the same
> columns and the same statistical rules as the 400-row catalogue used by the
> other lessons (`code/synthetic_catalog.py`). It is not the USGS catalogue and
> not an observation of the Earth.
>
> **All timings below are one run on one machine and vary with load, cache state
> and CPU.** The *ratios* are the content; the milliseconds are not, and no timing
> here should be quoted as a property of pandas.

## Learning objectives

By the end of this lesson you will be able to:

1. **Measure** memory with `memory_usage(deep=True)` and say which columns
   dominate an object-heavy table.
2. **Convert** a low-cardinality text column to `category` and report the
   measured saving and the fixed-label cost.
3. **Decide** whether a float downcast is acceptable by measuring the largest
   change it makes and whether equality survives.
4. **Replace** a per-element Python loop with a vectorised expression and
   quantify the difference.
5. **Explain** why the naive NumPy approach to a moving average can be slower
   than the pandas one, in terms of algorithmic complexity rather than library
   quality.
6. **State** the three conditions under which leaving pandas is the right call,
   and the conditions under which it is not.
7. **Time** an operation with a best-of-N harness rather than a single run.
8. **Justify** a dtype choice as a statement about the resolution the measurement
   supports.

## Prerequisites

- [03-04-01 Series, DataFrame and the Labeled-Data Model](./01-series-dataframe.md)
  — dtypes, and what a column actually stores.
- [03-02-07 Memory Layout, Strides and Cache-Aware Performance](../02-numpy/07-memory-performance.md)
  — contiguity and cache behaviour, which explain why vectorised code wins.

## 1. Measure first

Three commands cover almost all diagnosis:

```python
df.memory_usage(deep=True)     # per column, including the objects they point to
df.info(memory_usage="deep")   # dtypes, non-null counts, total
# and a timing harness, because a single time.perf_counter() measures the cache
def best_of(fn, repeats=3):
    times = []
    for _ in range(repeats):
        t0 = time.perf_counter(); result = fn(); times.append(time.perf_counter() - t0)
    return min(times), result
```

`best_of` is not a profiler and does not need to be. It removes the worst source
of noise in this kind of measurement — the first-run cost of touching cold
memory — and it returns the result alongside the time so you can check the two
arms computed the same thing. That second property matters more than the timing:
an optimisation that changed the answer is not an optimisation.

## 2. Memory, and where it goes

### 2.1 The measurement

On the 600,000-row synthetic table:

| Column | MB | share |
|---|---|---|
| event_id | 33.6 | 22.8 % |
| region | 34.5 | 23.4 % |
| agency | 34.2 | 23.2 % |
| mag_type | 30.6 | 20.8 % |
| mw | 4.8 | 3.3 % |
| depth_km | 4.8 | 3.3 % |
| n_stations | 4.8 | 3.3 % |

Total: 147.3 MB. Four text columns hold ninety per cent of it, and three of those
four have two, two and four distinct values. The mechanism is worth stating
precisely: a text column in pandas 3 stores a Python string object per row (or an
arrow/pointer structure, depending on storage), so the cost is proportional to
the **number of rows**, not to the number of distinct values. 600,000 copies of
"Northvale" and 600,000 copies of "Eastmere" cost the same.

### 2.2 `category`

A categorical column stores each distinct label once — the *dictionary* — and a
small integer code per row. Measured on the synthetic table:

| Column | before | after | saving |
|---|---|---|---|
| region | 34.5 MB | 0.6 MB | 98.3 % |
| agency | 34.2 MB | 0.6 MB | 98.2 % |
| mag_type | 30.6 MB | 0.6 MB | 98.0 % |
| event_id | 33.6 MB | 33.6 MB | 0.0 % |

Total: 147.3 MB → 49.8 MB, a factor of 2.96. The codes and dictionary are
visible afterwards:

```
0    2
1    3
2    2
3    0
4    1
  categories of region: ['Eastmere', 'Northvale', 'Southgate', 'Westhold']
```

Two consequences to state whenever you use it:

- **The label set is fixed at conversion time.** A new label arriving later
  either raises on assignment (when it is not a category) or must be added with
  `.cat.add_categories()`. That rigidity is a feature for a QC flag and an
  inconvenience for a free-text field.
- **`event_id` gains nothing.** It has 600,000 distinct values, so the dictionary
  is as large as the column. Categorising a high-cardinality identifier is a
  common and expensive mistake; the rule of thumb is that `category` pays when
  the distinct count is a small fraction of the row count.

Note the pandas 3 detail: text is stored as the dedicated `str` dtype
(`StringDtype(storage='python', na_value=nan)`), not `object`. A memory
calculation based on "an object column costs 8 bytes per pointer plus the
objects" still describes it, but code that tests `dtype == object` will not see it.

### 2.3 Downcasting, and what it costs

The numeric columns are already cheap here, but the general trade is worth
measuring. Casting `mw` and `depth_km` to `float32`:

```
           dtype_before dtype_after  before_MB  after_MB
depth_km        float64     float32        4.8       2.4
mw              float64     float32        4.8       2.4
  total: 147.3 MB -> 142.5 MB  (1.03x smaller)
```

A 3 per cent saving on the whole frame, because the text dominates. On the
columns themselves it is 50 per cent. The important part is the price:

```
    largest absolute change   : 4.578e-07 magnitudes
    rows changed at all       : 575,550 of 600,000
    exact equality preserved  : False
```

`float32` carries about seven significant decimal digits, so a magnitude rounded
to 0.1 is represented with an error of order 10⁻⁷. That is irrelevant for
plotting and fatal for code that groups by exact float equality — 575,550 of
600,000 rows no longer compare equal to their earlier selves. Downcast, then
re-check every comparison and every grouping key. On an integer column the
analogous move is `int64 → int32`, which is exact as long as the values fit; the
risk there is silent wraparound, not rounding.

## 3. Where the time actually goes

### 3.1 Per-element Python versus vectorised

Summing depths above 30 km over 600,000 rows:

| Approach | Time | Ratio |
|---|---|---|
| Python loop over the array | 15.86 ms | 31.4× |
| pandas boolean mask + `.sum()` | 0.51 ms | 1× |

The two results are equal to about fifteen significant figures and **not
bit-for-bit identical**:

```
    absolute difference : 1.863e-09
    relative difference : 4.962e-16
```

That is floating-point addition being non-associative: the loop adds one number
at a time, the mask sums in a different order. The relative difference of
5 × 10⁻¹⁶ is at the limit of double precision, so it is not an error in either
arm — but it is the reason comparisons of computed floats use a tolerance.

### 3.2 Accessors, measured rather than assumed

Inside pandas, the specialised accessor usually wins because its loop is compiled
rather than re-entering Python per element:

| Operation | Time |
|---|---|
| `Series.apply(len)` | 33.19 ms |
| `Series.str.len()` | 13.91 ms |
| ratio | 2.39× |

with identical results. But the honest counter-example belongs right beside it:
in the same run, `.str.upper()` was **slower** than `.apply(str.upper)` for these
short repeated labels, because `upper()` has to allocate a new string either way
and the accessor adds a layer. Measure the operation you have. The rule "prefer
the accessor" is a prior, not a law.

### 3.3 Group-by is compiled

`groupby(...).agg(...)` runs a C-level hash-table pass. Reimplementing it as a
Python loop over `df.groupby(...)` pays interpreter overhead per group and
produces the same numbers. The lesson-[04](./04-groupby-aggregation.md) advice
applies with a performance reason attached: when you write
`for key, group in df.groupby(...)`, first ask whether `agg`, `transform` or
`filter` expresses the same computation.

## 4. When to leave pandas

### 4.1 NumPy — and the measurement that contradicts the folklore

A 200-point moving average of 600,000 depths, three ways:

| Approach | Time | Complexity |
|---|---|---|
| `Series.rolling(200).mean()` | 2.76 ms | O(n) running sum |
| `np.convolve(depths, ones(200)/200)` | 11.28 ms | O(n × window) |
| `np.cumsum` difference | 1.42 ms | O(n) running sum |

The naive NumPy route is the **slowest of the three**, four times slower than the
pandas call it was supposed to beat. `convolve` evaluates a 200-point dot product
at each of 600,000 positions — about 0.12 G multiply-adds — while `rolling`
maintains a running sum and adds one value and removes one per position. Matching
the running-sum algorithm in NumPy with a cumulative sum is then the fastest of
all three, and it agrees with `rolling` to 1.7 × 10⁻¹⁰ km.

The lesson is not "NumPy is slower" or "NumPy is faster". It is that **the
algorithm dominates and the library is second order**. Dropping to NumPy does not
change complexity; choosing the right recurrence does.

The same measurement boundary tells you when *not* to leave: `rolling` carries an
index, a window object, NaN handling and edge semantics. Reimplementing those in
NumPy is where the bugs live, so leave only when the output is a raw array and
the index is genuinely not part of the question.

### 4.2 A database

The last boundary is the one that is not about speed at all. A filtered aggregate
run in pandas, then in SQLite:

```
    pandas mask + groupby  :     7.20 ms
    SQL GROUP BY (fetch)   :    23.67 ms
```

SQL is three times slower here, on 600,000 rows, in an in-memory database, with
the data already loaded. That is not the point. The argument for the database is
that **the filter and the aggregate happen inside the engine**:

- a table of 10⁹ rows never has to be brought into memory;
- a query touches only the columns it names, so a columnar engine reads a
  fraction of the bytes;
- the query is a string that can be reviewed, logged and version-controlled.

When the data no longer fit in RAM, that is the moment pandas stops being the
right tool — not a moment earlier. Between the two lies the chunked or
columnar reader (`read_csv(chunksize=...)`, Parquet, Zarr), which keeps the
pandas API while never holding the whole table.

## 5. dtype reference

| dtype | Use for | Watch out for |
|---|---|---|
| `float64` | measurements, coordinates | default; 8 bytes |
| `float32` | large arrays where 7 digits suffice | breaks exact equality |
| `int64` | counts, identifiers that are numbers | cannot hold `NaN`; upcasts to float |
| `Int64` (nullable) | counts that can be missing | not a NumPy dtype; some ops differ |
| `bool` | flags | 1 byte per row |
| `str` / `object` | free text, identifiers | the memory problem; O(rows) cost |
| `category` | low-cardinality labels, QC flags | fixed label set |
| `datetime64[ns]` | timestamps | timezone-naive by default; resolution limits |
| `timedelta64[ns]` | durations, residuals | — |

## 6. Worked code

```python
import pandas as pd, numpy as np, time

def best_of(fn, repeats=3):
    times, result = [], None
    for _ in range(repeats):
        t0 = time.perf_counter(); result = fn(); times.append(time.perf_counter() - t0)
    return min(times), result

df = build()                                   # SYNTHETIC, 600,000 rows

# memory, with the objects counted
print(df.memory_usage(deep=True) / 1e6)

# categorical labels, after checking cardinality
for col in ("region", "agency", "mag_type"):
    assert df[col].nunique() < 0.01 * len(df)
    df[col] = df[col].astype("category")

# a downcast, with its precision cost measured rather than assumed
small = df.astype({"mw": "float32"})
assert (small["mw"] == df["mw"]).all(), "float32 changed the values"
```

That last `assert` is the one that fires in the demo — and it *should* fire, or
be replaced by a tolerance check with the tolerance justified.

## 7. Physical interpretation

A dtype is a claim about the resolution a measurement supports. A magnitude
recorded to 0.1 cannot be distinguished from its neighbour by a `float32`
representation error of 10⁻⁷, so the downcast is physically harmless. A depth
differenced between two stations 100 m apart can lose meaning in `float32` when
the depths are kilometres — the subtraction is exact in `float64` and lossy in
`float32`. A count stored as `int32` is exact until it silently wraps; a count
stored as `float64` is exact until it exceeds 2⁵³.

None of these are computing problems in origin. They are statements about the
precision of the *measurement* and about the arithmetic that will be done to it.
"Just use float64" is the safe answer and a poor one on a 10⁸-row table; "use
float32 to halve memory" is a good answer and a bad one if the next step is a
small difference of large numbers. Decide with the measurement and the arithmetic
in view.

## 8. Assumptions and limits

- **Timings are environment-dependent.** Everything above is one run on one
  machine; treat the ratios as indicative and re-measure on yours.
- **`memory_usage(deep=True)` is not exact for every dtype.** It approximates the
  cost of PyArrow-backed columns; for planning purposes that is enough.
- **Categorical comparisons can be slower** in some operations, and reordering
  categories changes sort order. Speed is not guaranteed to improve, only memory.
- **Vectorised code is memory-hungry.** A double-precision temporary for a
  million-row expression is 8 MB; a chain of five is 40 MB of peak overhead. On a
  tight-memory machine, an in-place operation or a chunked approach may be the
  only option that fits, even at the same total work.
- **`groupby` with many groups allocates a hash table per grouping.** Grouping on
  a high-cardinality key (region × year × mag_type × event_id) is closer to
  sorting than to aggregating.
- **Leaving pandas has a maintenance cost.** A NumPy implementation of a window
  function has to reimplement edge handling and NaN semantics, and it is the part
  most likely to be wrong. Take the exit only when the win is measured.

## 9. Python demonstration

```
.venv/bin/python 03-scientific-computing/04-pandas/code/performance_dtypes_demo.py
```

**Memory anatomy.** 147.3 MB for 600,000 rows, with the four text columns
accounting for 113 MB of it (22.8 %, 23.4 %, 23.2 %, 20.8 %) against 3.3 % each
for the numeric columns.

**Categorical conversion.** 147.3 MB → 49.8 MB, a factor of 2.96, with per-column
savings of 98.3 %, 98.2 % and 98.0 % for the three low-cardinality columns and
0.0 % for the high-cardinality identifier. The dictionary and codes are printed,
and the pandas 3 `str` dtype is named explicitly:
`<StringDtype(storage='python', na_value=nan)>`.

**Downcast cost.** 147.3 MB → 142.5 MB overall, 50 % on the two float columns,
with a largest absolute change of 4.578 × 10⁻⁷ magnitudes, 575,550 of 600,000
rows changed, and `exact equality preserved: False`.

**Loop versus mask.** 15.86 ms against 0.51 ms, a ratio of 31.4×, agreeing to a
relative difference of 4.96 × 10⁻¹⁶.

**Accessor measurements.** `.str.len()` beats `.apply(len)` by 2.39×, and the
demo also reports that `.str.upper()` was *slower* than `.apply(str.upper)` in
the same run — deliberately included so the section cannot be read as a blanket
endorsement.

**Moving average, three ways.** `rolling` 2.76 ms, `convolve` 11.28 ms, `cumsum`
1.42 ms, with the first and third agreeing to 1.7 × 10⁻¹⁰ km over 599,801
windows. The naive NumPy route is the slowest.

**Filtered aggregate, pandas versus SQLite.** 7.20 ms against 23.67 ms on
600,000 rows in memory, with both returning count 19343 / 19605 / 19543 / 19431
and identical means. The demo prints the honest conclusion: on a table this size
the database is not faster, and the argument for it is that the work happens in
the engine.

## 10. Common mistakes

1. **Optimising without measuring.** The two contradictions in Section 4 exist
   because the folklore was believed.
2. **Timing once.** Cold cache, a background process, or a garbage collection can
   dominate a single run. Best-of-three, and compare results.
3. **Categorising a unique identifier.** 0.0 % saving and an oversized
   dictionary; see `event_id`.
4. **Downcasting without checking equality.** 575,550 rows changed.
5. **Using `object` where `category` belongs**, or the reverse for free text.
6. **Python loops over rows.** `iterrows` is the slowest way to do anything.
7. **Assuming NumPy is always faster.** The convolve result.
8. **Assuming the accessor is always faster.** The `str.upper` result.
9. **Leaving pandas to reimplement time-index semantics.** `rolling` on irregular
   timestamps is hard, and getting it subtly wrong is easy.
10. **Chaining many full-length temporaries** on a memory-constrained machine.
    The expression is fast and the peak memory is the problem.
11. **Forgetting that timings are not portable.** Quoting this lesson's
    milliseconds in a report.

## 11. Real-world applications

- **National catalogue services.** Millions of events; the region, network and
  magnitude-type columns are exactly the low-cardinality text columns that
  `category` exists for.
- **Continuous waveform archives.** Terabytes per station-year, which is why the
  archive is chunked and indexed rather than loaded.
- **GNSS position time series.** Dense enough that downcasting matters, and
  precise enough that float64 is not negotiable for the coordinates themselves.
- **Gridded model output.** large-array formats and chunked reads; the pandas
  boundary in this lesson is the same boundary those formats exist to cross.
- **Operational monitoring.** A real-time system budgets milliseconds; the
  best-of-N harness is how that budget is verified rather than assumed.

## 12. Further reading

- The pandas user guide sections *Categorical data*, *Scaling to large datasets*
  and *Enhancing performance*, including the `eval`/`query` performance notes.
- [NumPy](https://numpy.org) — the array layer and its memory model, and the
  documentation for `stride_tricks` and `convolve` behind Section 4.1.
- [SciPy](https://scipy.org) — the compiled implementations (`scipy.ndimage`,
  `scipy.signal`) that usually make a hand-written NumPy window unnecessary.
- [USGS Earthquake Hazards Program](https://earthquake.usgs.gov) — real
  catalogues at the scale where these decisions stop being hypothetical.

## 13. Related lessons

- Previous: [06 Case Study: Earthquake Catalogue Wrangling](./06-earthquake-catalog-pandas.md).
- [03-02-07 Memory Layout, Strides and Cache-Aware Performance](../02-numpy/07-memory-performance.md)
  — why contiguity and vectorisation win.
- [03-02-08 Replacing Loops: Vectorisation Patterns and Traps](../02-numpy/08-vectorisation-patterns.md)
  — the NumPy-side version of Section 3.
- [03-01-09 Iterators, Generators and Lazy Evaluation for Large Data](../01-python-fundamentals/09-iterators-generators.md)
  — chunked processing when nothing fits.
- [03-05-01 Matplotlib Figure/Axes Model and Anatomy of a Plot](../05-plotting-and-visualisation/01-matplotlib-basics.md)
  — where a downcast finally becomes visible, if it does.

## Exercises

[`exercises/07-performance-pandas-exercises.md`](./exercises/07-performance-pandas-exercises.md),
with full worked answers in
[`exercises/07-performance-pandas-solutions.md`](./exercises/07-performance-pandas-solutions.md).

## Self-assessment checklist

- [ ] I measure memory with `memory_usage(deep=True)` before optimising.
- [ ] I can say why a text column's memory scales with rows, not with distinct
      values.
- [ ] I categorise only columns whose distinct count is a small fraction of the
      rows, and I say the label set is then fixed.
- [ ] I check equality after any float downcast.
- [ ] I replace per-element loops with masks, and I time both arms.
- [ ] I can explain why the naive NumPy moving average lost, in terms of
      complexity.
- [ ] I can state the condition under which a database is the right tool.
- [ ] I use a best-of-N timing harness that returns the result as well as the time.
