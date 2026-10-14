---
id: 03-04-05
title: "Merging, Joining and Aligning Irregular Time Series"
level: intermediate
prereqs: ["03-04-02", "03-04-04"]
estimated_minutes: 90
tags: [pandas, merge, join, time-series, alignment, merge-asof, resampling]
---

# Merging, Joining and Aligning Irregular Time Series

Real geophysical data arrive in pieces that are keyed differently. The events
have a `region`; the stations have a `region`, a latitude and an elevation; the
groundwater logger writes a level every couple of days and the detector writes
an event count every day, and the two do not share a single timestamp.

Two operations cover almost all of this: **merging**, which combines tables on a
key, and **alignment**, which puts two series on a common index. The first has a
failure mode that is silent and multiplicative — a join on a non-unique key
multiplies rows, and every total computed afterwards is inflated by the
multiplication — and the second has a failure mode that is invisible — the wrong
alignment choice quietly changes how many rows are usable.

> The events, the station metadata and both time series are **SYNTHETIC** (see
> `code/synthetic_catalog.py`). The stations are not real stations, the regions
> are invented names, and no number below is an observation of the Earth.

## Learning objectives

By the end of this lesson you will be able to:

1. **Choose** `how=` for a join from the question being asked, and predict which
   unmatched keys survive and where `NaN` appears.
2. **Predict** the row count of a join from the cardinality of the key on each
   side, and detect an unintended many-to-many multiplication before it reaches a
   total.
3. **Use** `validate=` to turn a cardinality assumption into an assertion.
4. **Repair** a non-unique-key join by joining on a unique key or by aggregating
   before the join.
5. **Explain** why an outer join keeps a key with no match and reports `NaN`,
   and why an inner join's silence is the more dangerous option.
6. **Align** two irregular series with an explicit `reindex` on the union of
   timestamps, and state the resulting missing counts.
7. **Resample** onto a regular calendar period with the aggregation appropriate
   to what the number means.
8. **Use** `merge_asof` for a nearest-preceding match, justify `direction=` and
   always supply a `tolerance=`.

## Prerequisites

- [03-04-02 Indexing, Selection, loc/iloc and Boolean Masks](./02-indexing-selection.md)
  — masks and label addressing.
- [03-04-04 Group-By, Aggregation and Reshaping](./04-groupby-aggregation.md)
  — aggregating before a join is the standard repair for a bad key.

## 1. What a join is, in one paragraph

A merge takes two tables, a key column (or several), and produces a table
containing combinations of rows that share key values. Everything else follows
from *how many* rows share a key value on each side:

| left key count | right key count | rows produced (per key value) |
|---|---|---|
| 1 | 1 | 1 — a one-to-one join |
| many | 1 | as many as the left has — many-to-one |
| 1 | many | as many as the right has — one-to-many |
| many | many | the **product** — many-to-many |

Only the last row is dangerous, and it is the one that happens by default when
both tables are keyed on the same descriptive attribute.

## 2. A join on a unique key

The events carry a `region` name. A lookup table maps each region to a code and a
tectonic class, with exactly one row per region:

```python
lookup = pd.DataFrame({
    "region": ["Northvale", "Eastmere", "Southgate", "Westhold"],
    "region_code": ["R1", "R2", "R3", "R4"],
    "tectonic_class": ["transitional", "subduction", "strike-slip", "extensional"],
})
merged = df.merge(lookup, on="region", how="left", validate="many_to_one")
```

`validate="many_to_one"` asserts that the right-hand key is unique. It is not
decoration: if the lookup ever acquires a duplicate region row, the merge raises
`MergeError` instead of quietly duplicating events. Every merge in production
code should carry a `validate=` that states what you believe about the key. It
costs one string and turns the most expensive class of bug in tabular work into a
crash.

The demo confirms the row count is unchanged — 391 events in, 391 rows out —
which is what a many-to-one join on a complete lookup should do.

## 3. A join on a non-unique key, and the damage it does

Now join the events to the station table on `region`. There are fourteen stations
across four regions, so `region` is unique in neither table.

```
  events  : 391 rows
  stations: 14 rows
  naive merge result: 1219 rows (= sum over regions of events x stations)
```

1219 rows from 391 events and 14 stations. Every event now appears once per
station in its region — between two and four times:

```
    rows per event: min = 2, max = 4
```

The catastrophic part is what happens to a total:

```
    total energy, events alone        : 6.8871e+11 J
    total energy, after the bad merge : 2.1454e+12 J
    inflation factor                  : 3.1152
```

**3.12 times too large.** The number is positive, the units are joules, it has
five significant figures, and it is wrong by a factor of three. Nothing raised a
warning. A row count would have.

This is the reason Section 1's table is worth memorising. The failure is not in
the join machinery; it is in the assumption that a shared descriptive column is a
key. `region` is a *category*, not an *identifier*.

### 3.1 Two correct repairs

**Repair a — join on a unique key.** Derive or use an identifier. The station
table has `station_id`; a region table has `region_code`. Joining events to a
one-row-per-region table and events to stations are then two separate, correct
joins.

**Repair b — aggregate before joining.** If the intent was "give every station
its region's event count", compute the count per region first and join the
*summary*:

```python
summary = df.groupby("region")["event_id"].count().rename("n_events").reset_index()
both = stations.merge(summary, on="region", how="left")
```

Fourteen rows in, fourteen rows out, each station carrying its region's count. The
demo prints exactly that, and the station table is still one row per station.

The choice between the repairs is a modelling decision: a station-level analysis
wants repair (b); an event-level analysis that needs station metadata wants
repair (a) plus a stated rule for *which* station's metadata applies to a
regional event, which is itself a substantive decision and not a pandas one.

## 4. `how=` and what survives

| `how=` | Keys kept | Unmatched side |
|---|---|---|
| `"inner"` | only keys present in both | rows disappear silently |
| `"left"` | all left keys | right columns become `NaN` |
| `"right"` | all right keys | left columns become `NaN` |
| `"outer"` | union of keys | `NaN` on whichever side is missing |

`concat(axis=1)` on two Series is an outer join on the index, which is the
cleanest way to see the semantics. Combining a per-region event count with a
per-region station count gives:

| region | n_events | n_stations | events_per_station |
|---|---|---|---|
| Eastmere | 108.0 | 4 | 27.0 |
| Northvale | 134.0 | 3 | 44.67 |
| Southgate | 87.0 | 3 | 29.0 |
| Westhold | 62.0 | 2 | 31.0 |
| Outerisle | NaN | 2 | NaN |

`Outerisle` has stations and no events. The outer join keeps it and reports
`NaN`; the ratio is `NaN`, because a ratio with an undefined denominator is
undefined, and `NaN` says so. An inner join would have returned four rows and
dropped Outerisle **silently** — no error, no warning, no trace.

The general principle: **an outer join reports its unmatched keys; an inner join
hides them.** Use `inner` when a missing key means the row is genuinely not part
of the question, and check the row count against both inputs when you do.

## 5. Aligning two irregular time series

Alignment is a different problem from merging. There is no key column here; the
timestamps *are* the keys, and they do not match.

The two synthetic series:

- daily event counts: 672 observations from 2014-01-01 to 2015-12-31, with about
  8 per cent of calendar days absent (an outage, a holiday, a logger restart);
- groundwater level: 240 observations, sampled every two to four days.

Overlap and union, as measured:

```
  timestamps in both series       : 221
  timestamps in the union         : 691
  union timestamps missing from one series or the other: 470
```

221 shared timestamps out of a union of 691. There is no way to lay these two
series side by side without a decision, and the decision is one of:

**Option A — reindex onto the union.** Every timestamp that appears in either
series becomes a row, and absent values become `NaN`:

```python
union = counts.index.union(heads.index)
combined = pd.DataFrame({"n_events": counts.reindex(union),
                         "head_m":   heads.reindex(union)})
```

The demo reports 19 missing event-count days and 451 missing head days out of
691 rows. That is a very sparse frame, and the sparsity is honest: the logger
really did not record on those days.

**Option B — resample onto a regular calendar.** Both series are reduced to
month-end:

```python
monthly = pd.concat([counts.resample("ME").sum().rename("n_events"),
                     heads.resample("ME").mean().rename("head_m_mean")], axis=1)
```

24 rows, one per month. The aggregation is not the same for the two series and
must not be: a **count** resampled with `sum()` is still a count (23 events in
January 2014); a **level** resampled with `sum()` would be a meaningless "total
metres", so it takes `mean()`. Choosing the aggregation from what the number
means is the content of this step.

Option A preserves the question "what happened on this day"; Option B answers
"what happened this month". Neither is more correct. The mistake is picking one
without noticing that the row count and the missing-value pattern changed.

## 6. `merge_asof`: the nearest preceding observation

Neither of the options above answers a common question: "for each event-count
day, what was the groundwater level **at that time**?" The level was not measured
that day, so the correct answer is the most recent measurement before it —
provided the gap is small.

```python
joined = pd.merge_asof(left, right, on="date", direction="backward",
                       tolerance=pd.Timedelta("5D"))
```

Three requirements and one safeguard:

- **Both frames sorted on the key.** `merge_asof` does not sort; unsorted input
  gives wrong pairings. The demo checks `is_monotonic_increasing` on both sides
  and prints `True` for each.
- **`direction=`** is `"backward"`, `"forward"` or `"nearest"`. Backward means
  "at or before this date". `"nearest"` can select a measurement taken *after*
  the row's timestamp, which is a look-ahead error in anything forecast-like.
- **`tolerance=`** refuses to pair a day with a measurement from months earlier.
  Without it, the first days of the record are silently paired with the first
  measurement whenever it happened.

Measured result: 672 rows out (the left length — a backward asof never creates
rows), and 668 of the 672 carry a level inside the five-day tolerance. The four
`NaN`s are the first days, before the first groundwater reading; the tolerance
boundary is visible in the output at 2014-01-05, where the level 10.921 first
appears.

## 7. Worked code

```python
import pandas as pd, synthetic_catalog as sc

df = sc.clean_catalog()
df["energy_j"] = sc.mag_to_energy_j(df["mw"])

lookup = pd.DataFrame({...})                                  # unique key
merged = df.merge(lookup, on="region", how="left", validate="many_to_one")

stations = sc.station_table()                                 # non-unique key
bad = df.merge(stations, on="region", how="inner")            # 391 -> 1219 rows
assert len(bad) == len(df), "join changed the row count"      # the guard you write

summary = df.groupby("region")["event_id"].count().rename("n_events").reset_index()
good = stations.merge(summary, on="region", how="left")       # 14 -> 14 rows
```

The `assert` is the whole lesson in one line. A join that was supposed to
preserve the row count should assert that it did.

## 8. Physical interpretation

A join is an assertion about the world: *these two records describe the same
thing.* When the assertion is "these two records share a region", the join is
saying something weaker than it looks — and the row explosion is pandas
reporting, in row counts, that a category is not an identifier.

Alignment has a physical reading too. Reindexing onto a union asserts that the
absent timestamps mean "not observed" rather than "zero". Resampling asserts that
the monthly aggregate is a meaningful description of the interval. `merge_asof`
with a tolerance asserts that a measurement stays representative for at most a
few days — an assumption about the physical process's correlation time, not about
the file. A groundwater level three weeks old is a different measurement from one
taken yesterday, and the tolerance is where that judgement is recorded.

## 9. Assumptions and limits

- **`merge` does not check cardinality unless you ask.** `validate=` is opt-in.
- **Column name collisions get suffixed.** `_x` and `_y` appear without warning;
  rename before merging if the tables share generic names like `latitude`.
- **Joins are performed in memory.** A many-to-many join on a large table can
  exhaust memory before the row count post-mortem ever runs. Estimate
  `len(left) * len(right) / n_keys` first.
- **`concat(axis=1)` aligns on the index, not on values.** If the two frames have
  different index types (a `RangeIndex` and a `DatetimeIndex`) the result is a
  disaster: pandas will not align them at all, and you get `NaN` everywhere.
- **`reindex` introduces `NaN`; `asfreq` does the same for a regular grid.** Both
  are honest about absence and neither fills.
- **Downstream aggregations skip `NaN` by default**, so a table that is 65 per
  cent missing in one column still yields a mean. Pair an alignment step with a
  count of usable rows.
- **`merge_asof` performs no interpolation.** It copies the preceding value
  forward, which is exactly right for a step-like quantity and wrong for a
  smoothly varying one where the difference across the gap is comparable to the
  signal.
- **Resampling changes what the observations mean.** A monthly mean of a
  fortnightly-sampled level has an irregular sampling weight; if that matters,
  keep the count per month as a column.

## 10. Python demonstration

```
.venv/bin/python 03-scientific-computing/04-pandas/code/merging_time_series_demo.py
```

**A unique key preserves the row count:**

```
  events   : 391 rows, key 'region' unique in the lookup? True
  merged   : 391 rows (unchanged)
```

**A non-unique key does not:**

```
  naive merge result: 1219 rows (= sum over regions of events x stations)
    rows per event: min = 2, max = 4
    total energy, events alone        : 6.8871e+11 J
    total energy, after the bad merge : 2.1454e+12 J
    inflation factor                  : 3.1152
```

**The outer join reports what the inner join would hide.** `Outerisle` appears
with `n_events = NaN` in the concatenated table, and `how='inner'` "would keep 4
regions and drop Outerisle silently".

**Alignment.** 221 shared timestamps, a union of 691, and 470 union timestamps
missing from one series or the other. Option A leaves 19 + 451 missing cells;
Option B gives 24 monthly rows with `n_events` summed and `head_m_mean`
averaged.

**`merge_asof`.** 672 rows out, 668 inside the 5-day tolerance, and the visible
boundary at 2014-01-05 where the first level appears.

## 11. Common mistakes

1. **Joining on a descriptive column and calling it a key.** The 3.12× energy
   inflation of Section 3.
2. **Not checking the row count after a join.** One `assert` or one `len()`.
3. **`how="inner"` by habit.** It deletes unmatched keys without recording the
   deletion.
4. **`concat(axis=1)` on compatible-looking but differently-indexed frames.**
   Check `df.index.equals(other.index)` first.
5. **`merge_asof` on unsorted frames.** Wrong pairings, no warning. Sort, or use
   `left.sort_values(key)` explicitly.
6. **`merge_asof` without `tolerance`.** The early rows get paired with whatever
   happens to be first.
7. **`direction="nearest"` in a forecasting context.** It can use future data.
8. **`resample(...).sum()` for a level.** "Total metres" of groundwater.
9. **Losing the sampling count when resampling.** A monthly mean of three
   readings and of thirty look the same afterwards.
10. **Assuming suffixed columns are named sensibly.** `depth_km_x` and
    `depth_km_y` require you to remember which table was which; rename instead.

## 12. Real-world applications

- **Catalogue and station metadata.** Every regional seismicity study joins
  events to network or station metadata; the key is usually an identifier, and a
  study that uses a region name instead produces the inflation this lesson
  measures.
- **Instrument time series.** Tide gauges, borehole levels, GNSS positions and
  meteorological stations all have outages; aligning them onto a common calendar
  is the first step of any comparison, and the gap policy is a published part of
  the method.
- **Satellite passes.** Altimetry and SAR acquisitions are irregular in time;
  pairing them with in-situ measurements is a `merge_asof` with a physically
  justified tolerance.
- **Model-data comparison.** A model run at fixed timesteps and an observation
  series at irregular times require an explicit choice between interpolation,
  nearest-sample and resampling; the choice is a stated part of the comparison.
- **Geodetic velocity fields.** Station solutions from different processing
  centres are merged on station code, and the code — not the station name — is
  the key precisely because names are not unique.

## 13. Further reading

- The pandas user guide sections *Merge, join, concatenate and compare* and
  *Time series / date functionality*, including the `merge_asof` and resampling
  documentation used above.
- [IRIS Data Services](https://ds.iris.edu) and its
  [DMC](https://ds.iris.edu/ds/nodes/dmc/) — the real archives whose station
  metadata tables have exactly the shape used here, and where station codes are
  the key for the reason this lesson gives.
- [USGS Earthquake Hazards Program](https://earthquake.usgs.gov) — the event
  service that supplies real catalogue columns.

## 14. Related lessons

- Previous: [04 Group-By, Aggregation and Reshaping](./04-groupby-aggregation.md).
- Next: [06 Case Study: Earthquake Catalogue Wrangling](./06-earthquake-catalog-pandas.md).
- [03-04-03 Cleaning: Missing Values, Duplicates and Outliers](./03-cleaning-data.md)
  — a duplicate key is the join problem seen from the other side.
- [03-01-05 Lists, Tuples, Dictionaries, Sets and Complexity](../01-python-fundamentals/05-data-structures.md)
  — dictionaries make the cost of a many-to-many join explicit.

## Exercises

[`exercises/05-merging-time-series-exercises.md`](./exercises/05-merging-time-series-exercises.md),
with full worked answers in
[`exercises/05-merging-time-series-solutions.md`](./exercises/05-merging-time-series-solutions.md).

## Self-assessment checklist

- [ ] I can predict the row count of a join from the key cardinalities.
- [ ] I use `validate=` whenever I believe a key is unique.
- [ ] I assert the row count after a join that was supposed to preserve it.
- [ ] I can name the two repairs for a non-unique-key join and say when each is
      right.
- [ ] I know that an outer join reports unmatched keys and an inner join hides
      them.
- [ ] I choose between `reindex` on the union and `resample` by asking what the
      number means.
- [ ] I can justify `direction=` and `tolerance=` in a `merge_asof` in physical
      terms, not just syntactically.
