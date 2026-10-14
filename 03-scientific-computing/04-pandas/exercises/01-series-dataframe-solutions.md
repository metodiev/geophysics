# Solutions — 03-04-01 Series, DataFrame and the Labeled-Data Model

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output. The catalogue is SYNTHETIC and no statement
> below is a claim about the Earth.

---

## ★1 — Series anatomy

**(a)** `float64`. All three values are written with a decimal point, so the
array is floating point.

**(b)** `type(s.index)` is `pandas.core.indexes.base.Index`, and its values are
`['E1', 'E2', 'E3']` — the labels you supplied, not integers.

**(c)** `s.name` is `'depth_km'`. It lives on the **container** (`Series`), not on
the values: `s.to_numpy()` has no name attribute, which is why extracting the
array and losing the label happens as one silent step.

**(d)** `.to_numpy()`. You lose the index, the name, and every guarantee that a
later operation pairs values by label rather than by position. It is the right
call when handing the buffer to a function that only accepts arrays, and the
wrong call before an arithmetic operation on two tables that may be ordered
differently.

---

## ★2 — Positional versus label arithmetic

**(a)** `a.to_numpy() - b.to_numpy()` gives `[0.9, 1.8, -2.7]`. These are
differences between *different events*: position 0 is S1 in `a` and S3 in `b`.

**(b)** `a - b` gives `[0.0, 0.0, 0.0]`. The two Series carry the same three
labels, and pandas pairs them by label: S1 with S1, S2 with S2, S3 with S3. Each
pair is the same measurement, so each difference is zero.

**(c)** `a - b`. Only the labelled expression guarantees that each difference is
between the two determinations of one event; the positional version computes
three plausible, unit-correct and meaningless numbers.

---

## ★3 — Unmatched labels

**(a)** Three entries: the labels are the **union** `{S1, S2, S9}`.

**(b)** `S1` has the value `5.0 + 1.0 = 6.0`.

**(c)** `NaN` at `S2` (missing from the left) and at `S9` (missing from the
right).

**(d)** Because `NaN` says "no measurement exists", whereas `0` would assert a
magnitude of zero — a value that cannot occur and that would silently enter any
sum, mean or count computed afterwards. The gap is informative; the zero would
be a fabrication.

---

## ★4 — Counts and coverage

**(a)** `408 - 401 = 7` magnitudes are missing.

**(b)** `408 - 388 = 20` depths are missing.

**(c)** 388. The default aggregator skips `NaN`, so the mean is over the values
present.

**(d)** It is the right default *arithmetically* and a decision that must be
owned: the mean is then a mean over the well-measured events, which are not a
random subset of all events. Skipping is fine; reporting the count or an
uncertainty alongside it is what makes the choice visible.

---

## ★5 — Reading the demo

**(a)** `(408, 11)` — 408 rows and 11 columns, as printed by Section 4.

**(b)** The dtype is `str`. A pandas 1.x tutorial would print `object`, because
before pandas 3 text was stored as a NumPy array of Python objects. Pandas 3
gives text a dedicated string dtype (`StringDtype`), so a check written as
`dtype == object` no longer matches.

**(c)** `region` has 4 unique values and `agency` has 2, as printed at the end of
Section 5.

**(d)** The three `count` values are 388 (`depth_km`), 401 (`mw`) and 408
(`n_stations`). They differ because `describe()` reports non-null counts, and the
first two columns have missing entries while `n_stations` has none.

---

## ★6 — The alignment trap, deliberately inverted

**(a)** `events["depth_rank"]` is `0.0` for every row. `sort_values` returns a new
frame that shares the **same index labels** as `events`, so subtracting the two
Series aligns them by label and each row is subtracted from itself.

**(b)** After `reset_index(drop=True)` and a sort, `by_matrix` carries a
`RangeIndex` 0..407 that is unrelated to which event is which. Subtracting it from
`events["depth_km"]` (also 0..407 after a reset) now pairs values **by position**,
so each row is subtracted from a depth belonging to a different event. The result
is a column of numbers of the right size and units and of no meaning.

**(c)** In (a) the property being used is label alignment on a shared index, which
is exactly what a labelled axis is for. In (b) that property has been destroyed by
discarding the index, and the arithmetic silently reverts to positional — which is
why `reset_index(drop=True)` early in a pipeline is worth being suspicious of.

---

## ★7 — Axis semantics

**(a)** `frame.mean(axis=0)` gives `mw = 3.5` and `depth_km = 20.0` — one value
per **column**, i.e. per variable.

**(b)** `frame.mean(axis=1)` gives `S1 = 6.25`, `S2 = 11.75`, `S3 = 17.25` — one
value per **row**, i.e. per event. (Mean of a magnitude and a depth is
dimensionally meaningless; the exercise is about the axis, and this is the
sentence that says so.)

**(c)** `axis=0` collapses the index and therefore summarises each variable;
`axis=1` collapses the columns and therefore summarises each observation.

---

## ★8 — The mean and the median of a contaminated column

**(a)** From the demo: `count = 388`, `mean = 23.90` km, `median = 14.83` km,
`min = -3.0` km, `max = 999.0` km.

**(b)** The column contains the sentinel `999.0` km, which is not a depth. The
mean is sensitive to that single value (pulling it about 2.4 km above the mean of
the physically admissible values), while the median depends only on the ordering
of values, and one extreme value does not move the middle.

**(c)** The median, with the count, and with the outliers identified and removed
before *either* is reported. More precisely: the sentinel is a data-quality
defect, and the correct action is to remove it (lesson
[03](../03-cleaning-data.md)) rather than to choose a robust statistic to hide
it. The median is the right *default summary*; removal is the right *repair*.

---

## ★9 — Reproducibility and a "random" catalogue

**(a)** The generator uses `numpy.random.default_rng(SEED)` — a pseudo-random
number generator initialised from a fixed integer. The sequence is deterministic
given the seed, so the same seed reproduces the same catalogue exactly on any
machine with the same NumPy version. "Random" here means "drawn from a
distribution", not "unpredictable".

**(b)** Not a bug. A mean over a finite sample has a sampling distribution with
standard deviation `sigma / sqrt(n)`. With a magnitude standard deviation near
0.45 and ~390 events, the standard error is about 0.023, so a difference of 0.01
between two independent draws is well inside one standard error. The number to
check is not "is it different" but "is it different by more than the sampling
error".

**(c)** Compare the inputs, not the outputs: hash the generated table and compare
the digest across runs,

```python
assert pd.util.hash_pandas_object(df).sum() == expected_digest
```

or simply assert that the first row and the shape match. Comparing a *derived*
statistic to a tolerance conflates generator non-reproducibility with numerical
tolerance, and hides whichever changed.

---

## ★10 — Choosing an index

**(a)** The **event** table: index `event_id`, unique, one row per event. The
**arrival** table: no unique single index; if a `MultiIndex` is used at all it is
`(event_id, station_id, phase)`, with the columns still present for convenience.
The **station** table: index `station_id`, unique.

**(b)** Because arrivals are one-to-many from events and many-to-one to stations:
`event_id` repeats many times in the arrival table, so it is not unique. A
non-unique index is legal, and `.loc` on it returns several rows, but a *unique*
key would let a join detect duplicates and error on them (lesson
[05](../05-merging-time-series.md)), which a composite key with a repeating
component cannot do as cleanly.

**(c)** `arrivals.loc[event_id]` returns a `DataFrame` (several rows, because the
index value is not unique). With 62,000 arrivals across 391 events the average is
about 158 rows per event, with a long right tail — the largest events have far
more arrivals than the smallest.

**(d)** A unique single key makes "one row per event" assertions possible: after
a merge you can call `validate="many_to_one"` and be told if the key is ever
duplicated. With a composite key whose components repeat, that assertion is
weaker and the corresponding bug is a silent row multiplication.
