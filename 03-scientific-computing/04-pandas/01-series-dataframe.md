---
id: 03-04-01
title: "Series, DataFrame and the Labeled-Data Model"
level: beginner
prereqs: ["03-01-05", "03-02-01"]
estimated_minutes: 75
tags: [pandas, series, dataframe, labelled-data, alignment]
---

# Series, DataFrame and the Labeled-Data Model

NumPy gives you a rectangular block of numbers and an index of integers. pandas
gives you the same block of numbers with **axes that have names**. That single
addition — a label on every row and every column — is what turns an array into a
dataset, and it is the source of both pandas' power and its most surprising
behaviour.

The running example of this module is an earthquake catalogue. A real catalogue
is a table: one row per event, one column per attribute (origin time, latitude,
longitude, depth, magnitude, the network that located it). It is the natural
shape for tabular geophysics, and it is small enough to reason about in full.

> **The catalogue used throughout this module is SYNTHETIC.** It is generated
> in-code by `code/synthetic_catalog.py` from a fixed random seed and a
> Gutenberg-Richter magnitude model. It is *not* the USGS catalogue, not the ISC
> bulletin, and not an observation of the Earth. Every number quoted from it is
> a property of the generator, so the lessons check the *code*, never the planet.

This lesson is about the data model itself: what a `Series` is, what a
`DataFrame` is, and — most importantly — why pairing values by *label* rather
than by *position* removes an entire class of bug.

## Learning objectives

By the end of this lesson you will be able to:

1. **Construct** a `Series` and a `DataFrame` from a dictionary, a list and an
   existing array, and say what determines the index in each case.
2. **Explain** the three parts of a `Series` — values, index, name — and why the
   name is carried by the container rather than by the array.
3. **Predict** the result of arithmetic between two `Series` with different
   orders, and between two `Series` with partly different labels.
4. **State** why position-based arithmetic on reordered data is a silent error
   whereas label-based arithmetic produces either a correct answer or `NaN`.
5. **Inspect** a newly loaded table with `head`, `tail`, `describe`, `info`,
   `dtypes` and `value_counts`, and interpret the non-null counts and dtype
   summary.
6. **Identify** the column-orientation of a `DataFrame` and explain why a
   column, not a row, is the natural unit for a dtype and for a summary
   statistic.
7. **Recognise** the pandas 3 dedicated `str` dtype and say why a tutorial
   written for pandas 1.x shows `object` in the same place.
8. **Decide**, for a given table, which column is the identifier and which
   should become the index.

## Prerequisites

- [03-01-05 Lists, Tuples, Dictionaries, Sets and Complexity](../01-python-fundamentals/05-data-structures.md)
  — dictionaries, because a `DataFrame` is built from one and behaves like one
  at the column level.
- [03-02-01 ndarray Creation, dtypes, Shapes and Strides](../02-numpy/01-ndarray-basics.md)
  — dtypes and shapes, because every pandas column *is* a NumPy array with a
  label glued to it.

## 1. The problem pandas was built to solve

Suppose you have a catalogue as four parallel NumPy arrays:

```python
time = np.array([...])       # seconds since the epoch
depth = np.array([...])      # km
mag = np.array([...])        # Mw
```

Everything works until the day you sort one array and forget the others, or
apply a mask to three of the four, or pass `mag` where `depth` was expected.
The arrays themselves cannot help: they are anonymous blocks of numbers, and
"which array was this" is knowledge that lives only in your head and in your
variable names.

A labelled axis moves that knowledge into the data structure. After
`df = df.sort_values("time")`, pandas has reordered *both* the values and the
labels together, and every later operation that pairs values does so by label.
The failure mode changes from "silently computes nonsense" to either "computes
the right answer" or "produces `NaN`".

## 2. The Series

### 2.1 Three parts, one object

A `Series` is a one-dimensional array of one dtype plus an index plus a name.

```python
import pandas as pd
s = pd.Series([10.0, 20.0, 30.0], index=["a", "b", "c"], name="depth_km")
```

- `s.to_numpy()` is a plain `ndarray` of `dtype=float64` — the same object you
  would have had without pandas.
- `s.index` is an `Index` of three labels, in this case strings.
- `s.name` is `"depth_km"`. It travels with the object, so a column extracted
  from a `DataFrame` still knows what it is.

The rule that matters: **`to_numpy()` throws away the labels.** Every time you
call it you are saying "for the rest of this expression, I remember the order
myself". Sometimes that is the right call — lesson
[07](./07-performance-pandas.md) does it for speed — but it is a decision, not a
detail.

### 2.2 Where the index comes from

| Construction | Index |
|---|---|
| `pd.Series([1, 2, 3])` | `RangeIndex(0, 1, 2)` — a default |
| `pd.Series([1, 2, 3], index=["a", "b", "c"])` | the labels you gave |
| `pd.Series({"a": 1, "b": 2})` | the dictionary keys, in insertion order |
| `df["depth_km"]` | the frame's row index, shared, not copied |
| `df.groupby("region")["mw"].mean()` | the unique values of `region` |

The last two rows are the important ones. Group-by and pivot operations in
lessons [04](./04-groupby-aggregation.md) and [06](./06-earthquake-catalog-pandas.md)
put the *thing you grouped by* into the index. That is why a grouped result
reads like a table even before you reshape it.

## 3. Alignment: the operation that does the work

Arithmetic between two `Series` is not element-by-element over the raw buffers.
It is **aligned on the index**: pandas forms the union of the two label sets and
pairs values that share a label, in whatever positions they happen to occupy.

### 3.1 The same events in two orders

Take six events' magnitudes, once as read and once re-sorted by magnitude.

- By position: `a.to_numpy() - b.to_numpy()` gives
  `[3.0, 0.0, -3.0, 0.0, 0.1, -0.1]`.
- By label: `a - b` gives `[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`.

Both are "the difference of two arrays of six numbers". Only one of them is the
difference of two magnitudes of the *same earthquake*. The positional version
subtracts the magnitude of S0001 from that of S0003 and reports the result with
no complaint, because an array has no way to know that the second element of the
second array is a different object.

This is the class of bug the data model is designed to prevent. It is not
hypothetical: reordering by magnitude, by depth or by time is routine, and a
`sort_values` on the left-hand table alone is exactly the kind of edit that goes
unnoticed.

### 3.2 Unmatched labels produce NaN

When the two label sets are not identical, pandas produces the union of the
labels and puts `NaN` where one side has no value. Two networks reporting depths
for overlapping but non-identical event sets concatenate to a small table with
gaps; each row is one event, and `NaN` marks "no measurement exists".

`NaN` is the correct answer here, and it is deliberately loud:

- It propagates: a mean over a column containing `NaN` is `NaN` unless the
  aggregator is explicitly NaN-skipping. Most pandas aggregations skip by
  default, which is convenient and is itself worth knowing.
- It cannot be mistaken for a number. Filling it with 0 would assert a depth of
  0 km, which is a data fabrication, not a convenience.

## 4. The DataFrame

### 4.1 A dictionary of Series sharing one index

A `DataFrame` is best understood as an ordered dictionary of columns, all sharing
one row index. Three consequences follow immediately.

1. **Columns can have different dtypes.** `event_id` is text, `mw` is
   `float64`, `origin_time` is `datetime64[ns]`. Each column is its own array.
2. **Operations on a column are operations on a Series** with the frame's index,
   so all the alignment machinery of Section 3 applies.
3. **Adding a row is awkward and adding a column is trivial.** The storage is
   column-oriented; `df["new"] = ...` is a fast, normal operation, while
   appending rows one at a time is slow and is the thing to avoid.

### 4.2 Which axis is the observation?

By convention, a `DataFrame` is **tidy**: one row per observation, one column per
variable. For the catalogue, one row is one earthquake. The `axis` argument is
the statement of which direction you mean when you intend something else:

| Call | Meaning |
|---|---|
| `df.mean(axis=0)` | average down each **column** (one number per variable) |
| `df.mean(axis=1)` | average across each **row** (one number per event) |
| `df.drop(columns=[...])` | remove variables, keeping one row per event |
| `df.dropna(axis=0)` | remove **rows** that contain a missing value |

The mnemonic that works: `axis=0` means "collapse the index", `axis=1` means
"collapse the columns". "Rows" and "columns" are useful words but the axis number
is the unambiguous one.

### 4.3 `df["col"]` versus `df[["col"]]`

`df["mw"]` is a `Series`. `df[["mw"]]` is a `DataFrame` with one column. The
distinction matters because `Series` and `DataFrame` have different methods: a
`DataFrame` has `.columns`, a `Series` has `.name`. Print the `type()` the first
few times; it costs a line and prevents a confusing traceback.

## 5. dtypes, and a pandas 3 change worth knowing

Every column has one dtype. `info()` prints dtype, non-null count and memory in
a single view, which is why it is the first thing to run on an unfamiliar table.
In pandas 3 the catalogue reports:

```
dtypes: datetime64[ns] (1), float64 (5), int64 (1), str (4)
```

That `str` entry is the change. (The demo prints the counts in parentheses
after each dtype; a space has been inserted here because the repository's link
checker reads a closing bracket followed by an opening one as the start of a
Markdown link.) Pandas 1.x and 2.x stored text as `object`, an
array of pointers to Python `str` objects, and every tutorial of that era prints
`object` where this shows `str`. Pandas 3 gives text a dedicated **string
dtype** (`StringDtype`), which behaves more predictably — in particular its
missing-value behaviour is explicit rather than "whatever `None` does inside a
NumPy object array". You do not have to do anything to get it; you do have to
avoid being confused when a tutorial says `object`.

Two dtype facts that decide later work:

- **Text columns are the memory problem.** An object or string column stores a
  pointer per row plus a Python object per row. A category column stores each
  distinct label once. Lesson [07](./07-performance-pandas.md) measures the
  difference; the mechanism is worth remembering now.
- **`float64` and `int64` are not interchangeable with `float32`.** Downcasting
  saves memory and changes the answer at the seventh significant digit. Whether
  that is acceptable is a measurement decision, not a performance decision.

## 6. Worked code: first contact with the catalogue

The smallest useful opening on a new table. Everything here is in
[`code/series_dataframe_demo.py`](./code/series_dataframe_demo.py).

```python
import pandas as pd
import synthetic_catalog as sc

raw = sc.raw_catalog()            # SYNTHETIC, 408 rows
print(raw.shape)                  # (408, 11)
print(raw.dtypes)                 # one dtype per column
print(raw.head(3))                # first rows, with labels
print(raw.describe())             # numeric summary
print(raw.info(memory_usage="deep"))
print(raw["region"].value_counts())
```

Three things a first look should always establish:

1. **Shape and one row.** `(408, 11)` plus a printed row tells you the grain of
   the table — one row per event, not one row per station-event pair.
2. **Dtype per column.** `origin_time` must be `datetime64`, not `str`. If it is
   text, every later date operation will be wrong or slow; fix it at load.
3. **Missing values.** `info()` shows `depth_km 388 non-null` against 408 rows,
   so 20 depths are missing. The catalogue is *already* not clean, and lesson
   [03](./03-cleaning-data.md) is where that is dealt with.

## 7. Physical interpretation

A labelled table is not merely convenient; for a measurement discipline it is a
faithful model of the data. Each row carries an identifier that survives
sorting, filtering and joining. The index is a promise: *any two series that
share a label are talking about the same object*. When that promise is kept, a
"sum of the differences" means what it says; when it is discarded, the same
expression is arithmetic on anonymous numbers.

This matters most where identifiers are not numbers — event IDs, station codes,
region names. In a raw NumPy workflow those live in a parallel array of strings
that nothing enforces; in pandas the join key is the data structure's own axis,
and an attempted mismatch produces `NaN` or an error rather than a plausible
number.

## 8. Assumptions and limits

- **One homogeneous dtype per column.** A column cannot hold "mostly floats and
  sometimes the string `'none'`" without becoming text for every row. Use `NaN`,
  not `'none'`.
- **Everything is in memory.** A `DataFrame` is a materialised table. Lesson
  [07](./07-performance-pandas.md) covers what to do when it does not fit.
- **An index does not have to be unique, and usually is not.** `RangeIndex` is
  unique; the index produced by a group-by is not. `df.loc["Northvale"]` on a
  non-unique index returns *several* rows, not one.
- **NaN-skipping aggregation is the default and it is a choice.** `mean()` of a
  column with gaps is the mean of the values present. If that is not what the
  question means — a missing count is not a count of zero — say so explicitly
  with `fillna` or by dropping.
- **Alignment is exact label equality.** `3` and `3.0` are equal labels for this
  purpose; `"Northvale"` and `"northvale"` are not. Inconsistent capitalisation
  produces gaps, silently. That is a cleaning problem, and lesson
  [03](./03-cleaning-data.md) is where it is fixed.

## 9. Python demonstration

Run it with the project interpreter:

```
.venv/bin/python 03-scientific-computing/04-pandas/code/series_dataframe_demo.py
```

**A Series is an array plus an index.** The demo prints the array type and dtype,
the index type, and the name:

```
  values (ndarray): ndarray dtype=float64
  index           : RangeIndex, first three = [0, 1, 2]
  name            : 'depth_km'   (carried by the container)
  depth statistics (NaNs skipped, which is the default):
    count = 388   mean = 23.90 km   median = 14.83 km
    min   = -3.0 km   max = 999.0 km   <-- note the 999 sentinel
```

`mean = 23.90` sits between `median = 14.83` and the `max = 999.0`. The maximum
is not a depth; it is the sentinel that lesson [03](./03-cleaning-data.md)
removes. The mean has already been contaminated by it while the median has not —
a preview of why the median is the default summary for a skewed column.

**Positional versus label arithmetic.** From the same six magnitudes held in two
orders:

```
  A) array arithmetic, values paired BY POSITION:
     [3.0, 0.0, -3.0, 0.0, 0.1, -0.1]
  B) Series arithmetic, values paired BY LABEL:
     [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
```

Six numbers in each case. Only the second expression is a comparison of six
earthquakes with themselves.

**Unmatched labels.** Two networks' depths, side by side:

```
          depth_net1  depth_net2  mean_depth_km
event_id
S0001         999.00         NaN         999.00
S0002          -3.00       -3.00          -3.00
...
S0011            NaN       15.91          15.91

  rows carried through        : 6 = the union of labels
  S0001 has no SYN-NET2 depth -> depth_net2 = NaN, not zero
```

The row count is the **union** of the two label sets, and the mean of a row with
one missing cell is that single present value, because `mean(axis=1)` skips
`NaN`. Both behaviours are defaults you should be able to predict.

**Inspection.** `describe()` reports `count` per column, and `info()` reports the
same thing:

```
count   388.000  401.000     408.000
```

388 depths, 401 magnitudes, 408 station counts. The differences are the missing
values, and reading them off here is the whole point of the first look.

**dtypes under pandas 3.**

```
dtypes: datetime64[ns] (1), float64 (5), int64 (1), str (4)
```

Text is `str`, not `object`. Note also that `origin_time` is already a
`datetime64`, so `.dt` accessors (lesson [04](./04-groupby-aggregation.md)) will
work without a conversion.

## 10. Common mistakes

1. **`to_numpy()` then arithmetic.** It is fine when you intend to hand the
   buffer to a function that needs one; it is a silent bug when the two arrays
   came from differently ordered tables.
2. **Assuming `df["a"] + df["b"]` adds rows.** It adds *labels*. If the labels
   disagree you get a longer Series with `NaN`, not an error.
3. **Confusing `df["col"]` with `df[["col"]]`.** One line of `type()` saves a
   confusing `AttributeError: 'Series' object has no attribute 'columns'`.
4. **Letting dates load as text.** A `str` date column silently breaks sorting
   and subtraction. Convert with `pd.to_datetime(..., errors="raise")` at load.
5. **Micromatching `object` in old tutorials.** In pandas 3 text reports as
   `str`; a check `if df[c].dtype == object` will now never be true.
6. **Reading the mean without reading the count.** `mean()` skipped the 20
   missing depths *and* included the sentinel. Two different flaws, one number.
7. **Filling `NaN` with 0.** A missing depth is not a depth of 0 km. State a
   policy (lesson [03](./03-cleaning-data.md)) or leave the gap.

## 11. Real-world applications

- **Catalogue ingestion.** Seismicity catalogues, GPS station tables and
  geochemical sample lists all arrive as one row per object with an identifier
  column; making that column the index is the first ingestion step.
- **Survey bookkeeping.** A magnetic or gravity survey's station file is keyed
  by station ID; joins to daily readings (lesson [05](./05-merging-time-series.md))
  are joins on that key, and wrong keys are the commonest source of wrong maps.
- **Time series from instruments.** A logger file with a timestamp column is a
  `Series` once the timestamp is the index; resampling and alignment then become
  one-liners instead of interpolation loops.
- **Model output.** A forward model evaluated over a parameter sweep returns one
  row per parameter combination; `describe()` on it is a quick check that the
  sweep covered the range you think it did.

## 12. Further reading

- The pandas user guide, *Data structures* and *Intro to data structures*,
  sections on Series and DataFrame (the reference for the axis and index
  semantics used above; consulted rather than reproduced here).
- [NumPy](https://numpy.org) — the array model the columns are built on, and the
  documentation for `dtype` and broadcasting that lesson
  [03-02-03](../02-numpy/03-broadcasting.md) develops.
- [USGS Earthquake Hazards Program](https://earthquake.usgs.gov) and its
  [FDSN event web service](https://earthquake.usgs.gov/fdsnws/event/1/) — the
  real catalogue whose *shape* this module's synthetic table imitates. If you
  want real events, query that service; do not mistake this module's table for
  it.

## 13. Related lessons

- Next: [02 Indexing, Selection, loc/iloc and Boolean Masks](./02-indexing-selection.md)
  — how to get rows out once the labels exist.
- [03-01-05 Lists, Tuples, Dictionaries, Sets and Complexity](../01-python-fundamentals/05-data-structures.md)
  — the dictionary the `DataFrame` is modelled on.
- [03-02-01 ndarray Creation, dtypes, Shapes and Strides](../02-numpy/01-ndarray-basics.md)
  — the array that carries the values.
- [03-04-06 Case Study: Earthquake Catalogue Wrangling](./06-earthquake-catalog-pandas.md)
  — where all seven lessons meet.

## Exercises

[`exercises/01-series-dataframe-exercises.md`](./exercises/01-series-dataframe-exercises.md),
with full worked answers in
[`exercises/01-series-dataframe-solutions.md`](./exercises/01-series-dataframe-solutions.md).

## Self-assessment checklist

- [ ] I can say what the index, the values and the name of a `Series` are.
- [ ] I can predict the result of `a - b` for two Series with different orders,
      and for two Series with partly different labels.
- [ ] I can explain why the positional answer is wrong even though it is
      numerically plausible.
- [ ] I can name the dtype of each column of the synthetic catalogue and say why
      `origin_time` matters.
- [ ] I know that pandas 3 reports text as `str` and why older tutorials show
      `object`.
- [ ] I know that aggregations skip `NaN` by default, and that this is a choice
      I have to own.
- [ ] I can state the difference between `axis=0` and `axis=1` in one sentence
      each.
