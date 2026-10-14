# Exercises — 03-04-01 Series, DataFrame and the Labeled-Data Model

Attempt these **closed-book** before opening the
[solutions](./01-series-dataframe-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems that say "run the demo" refer to
[`../code/series_dataframe_demo.py`](../code/series_dataframe_demo.py); report its
**actual** output, not a remembered one. The catalogue is **SYNTHETIC**: it is
generated in-code by [`../code/synthetic_catalog.py`](../code/synthetic_catalog.py)
and is not the USGS catalogue.

Throughout, when a question asks for a *statement* about a table, give the number
and the unit, and say which column it came from.

---

## ★ Foundational

**★1.** A `Series` is constructed as

```python
s = pd.Series([12.0, 45.0, 33.0], index=["E1", "E2", "E3"], name="depth_km")
```

(a) What is `s.dtype`?
(b) What is `type(s.index)` and what are its values?
(c) What is `s.name`, and where does it live — on the values or on the container?
(d) What single call removes the labels, and what do you lose by calling it?

---

**★2.** Two `Series` describe the same three events' magnitudes in different
orders:

```python
a = pd.Series([3.1, 4.9, 2.2], index=["S1", "S2", "S3"])
b = pd.Series([2.2, 3.1, 4.9], index=["S3", "S1", "S2"])
```

(a) Compute `a.to_numpy() - b.to_numpy()` and write the three values.
(b) Compute `a - b` and write the three values.
(c) Explain in one sentence which expression answers "how much do the two
magnitude determinations differ, per event?".

---

**★3.** Two networks report magnitudes for partly overlapping event sets:

```python
c = pd.Series([5.0, 6.0], index=["S1", "S9"])
d = pd.Series([1.0, 2.0], index=["S1", "S2"])
```

(a) How many entries does `c + d` have?
(b) Which labels have a value, and what is it?
(c) What value appears at the other labels?
(d) State why this is a better outcome than a zero in those positions.

---

**★4.** A frame is 408 rows with `depth_km` non-null in 388 rows and `mw`
non-null in 401 rows.

(a) How many magnitudes are missing?
(b) How many depths are missing?
(c) If `df["depth_km"].mean()` is computed, how many values does it average?
(d) Is skipping missing values in a mean the right default here? One sentence.

---

## ★★ Applied

**★★5.** Run the demo, Section 4 and Section 5.

(a) Report `raw.shape`.
(b) Report the dtype of the `region` column and say why a pandas 1.x tutorial
would print something different.
(c) Report the unique counts of `region` and `agency`.
(d) Report the three `count` values printed by `describe()` and match each to the
column it belongs to.

---

**★★6.** A colleague writes:

```python
events = sc.raw_catalog()
by_matrix = events.sort_values("mw", ascending=False)
events["depth_rank"] = events["depth_km"] - by_matrix["depth_km"]
```

(a) What is `events["depth_rank"]` equal to for every row, given that both Series
carry the frame's original index? State the value.
(b) If the frame had been `reset_index(drop=True)` before the sort, what would
`by_matrix` carry as its index, and what would the subtraction now produce?
(c) Which property of the data model is being relied on in (a), and which is
being violated in (b)?

---

**★★7.** On the frame

```python
frame = pd.DataFrame({"mw": [2.5, 3.5, 4.5], "depth_km": [10.0, 20.0, 30.0]},
                     index=["S1", "S2", "S3"])
```

(a) Compute `frame.mean(axis=0)` and write both values.
(b) Compute `frame.mean(axis=1)` and write all three values.
(c) Explain in one sentence each which axis means "per variable" and which means
"per event".

---

**★★8.** Run the demo, Section 1.

(a) Report `count`, `mean`, `median`, `min` and `max` of `depth_km`.
(b) Explain why `mean` is much larger than `median` in terms of the specific
value in the column.
(c) Which of the two statistics would you report for this column, and why?

---

## ★★★ Research-oriented

**★★★9.** The demo constructs its catalogue from a seeded generator
(`SEED = 20261014` in `synthetic_catalog.py`).

(a) Explain why a "random" catalogue is nevertheless reproducible, and what
property of the generator provides that.
(b) A colleague removes the seed argument and reports a mean magnitude that
differs from the demo's by 0.01. Is that a bug? Justify in terms of the sampling
distribution of a mean.
(c) Design a one-line check that a two-run analysis produced identical inputs.

---

**★★★10.** You are given three tables: an *event* table keyed by `event_id`, an
*arrival* table keyed by `(event_id, station_id)`, and a *station* table keyed by
`station_id`.

(a) Which column of each table would you make the index, and which would you
leave as an ordinary column?
(b) For the arrival table, why is a single-column index the wrong choice?
(c) The event table has 391 rows and the arrival table 62,000 rows. If you set
the index of each to your choice from (a) and then call
`arrivals.loc[event_id]`, what type is the result and roughly how many rows does
it have on average?
(d) State one operation on the arrival table that a unique single key would make
possible and the composite key does not.
