# Solutions — 03-04-05 Merging, Joining and Aligning Irregular Time Series

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output. All tables are SYNTHETIC; no number below is an
> observation of the Earth.

---

## ★1 — Cardinality and an `validate=` assertion

**(a)** **Unique**: 10 rows, 10 distinct `k` values, one row each.

**(b)** **100 rows**. Each left row matches exactly one right row, so the left
cardinality is preserved.

**(c)** `validate="many_to_one"` — many left rows to one right row.

**(d)** Every left row with that `k` would match two right rows, doubling the row
count for that key. With `validate="many_to_one"` pandas raises `MergeError`
before producing a result; without it, the duplication is silent and any total
computed afterwards is inflated.

---

## ★2 — One-to-many

**(a)** **5 rows** — one for each right row.

**(b)** A **one-to-many** join (from the left table's point of view).

**(c)** The left table's columns are repeated across all five output rows; the
right table's columns vary.

---

## ★3 — `concat(axis=1)`

**(a)** They are aligned on the **index**.

**(b)** A label present in one frame and not the other is kept (the index is the
union) and receives `NaN` in the missing frame's columns.

**(c)** An **outer join** on the index. `join="inner"` would restrict to the
intersection instead.

---

## ★4 — Alignment arithmetic

**(a)** 691 timestamps — the demo prints this for the same pair of series.

**(b)** `691 − 221 = 470` timestamps are in exactly one series.

**(c)**

```python
union = a.index.union(b.index)
combined = pd.DataFrame({"a": a.reindex(union), "b": b.reindex(union)})
```

---

## ★5 — The row explosion

**(a)** 391 events, 14 stations, and a merge result of **1219 rows**.

**(b)** Minimum **2**, maximum **4** rows per event — exactly the number of
stations in the event's region.

**(c)** `6.8871e+11` J before, `2.1454e+12` J after, inflation factor
**3.1152**.

**(d)** Because the operation performed is a sum of each event's energy once per
matching station row — a well-defined arithmetic operation on the merged table,
producing a positive number in joules to full floating-point precision. Nothing
about the value is arithmetically wrong; it answers "sum of energy over the
merged rows", which is a different question from "sum of energy over events". The
units and the significant figures come from the input data, not from the
question, which is why they do not expose the error.

---

## ★6 — The aggregation repair

**(a)**

```python
summary = (df.groupby("region")["event_id"].count()
             .rename("n_events").reset_index())
both = stations.merge(summary, on="region", how="left")
```

**(b)** **14 rows** in, 14 rows out — the demo prints "station table enriched with
region aggregates: 14 rows (still one per station)".

**(c)** The assumption is that a regional aggregate is the right attribute for a
station: that every station in a region is described by that region's event
count. That is true for a regional summary and false for anything station-specific
(a station-level detection threshold, say) — hence the distinction between the
two repairs in the lesson. For the region-level question the repair is exact,
because it *replaces* a join with a lookup.

---

## ★7 — Outer versus inner

**(a)**

| region | n_events | n_stations | events_per_station |
|---|---|---|---|
| Eastmere | 108.0 | 4 | 27.000000 |
| Northvale | 134.0 | 3 | 44.666667 |
| Southgate | 87.0 | 3 | 29.000000 |
| Westhold | 62.0 | 2 | 31.000000 |
| Outerisle | NaN | 2 | NaN |

**(b)** `Outerisle` has two stations and no events, so `n_events` is `NaN` and the
ratio of an undefined numerator to a defined denominator is `NaN`. Dividing by
zero events is undefined, not infinite, and `NaN` is pandas reporting that
honestly.

**(c)** `how="inner"` would keep **4** regions and drop `Outerisle` silently —
no error, no warning, and no record in the output that a station group existed
at all.

---

## ★8 — `merge_asof`

**(a)** **672** rows (the left length), of which **668** carry a level inside the
five-day tolerance.

**(b)** The first groundwater value appears on **2014-01-05** (`10.921` m). The
four preceding rows — 2014-01-01 to 2014-01-04 — carry `NaN`, because there is no
prior measurement inside the tolerance.

**(c)** Without `tolerance`, the four leading rows would be paired with whatever
the earliest right-hand record is, producing a value that looks measured but
comes from outside the window, possibly days or months away. The tolerance exists
because a measurement has a **correlation time**: a groundwater level three weeks
old is not the level today, and the tolerance is where that physical judgement is
recorded. It converts "nearest sample, however far" into "nearest sample, if it is
close enough to be representative".

---

## ★9 — Attaching station metadata to events

**(a)** Because the merged table would claim that each event is associated with
every station in its region — the 1219-row explosion of Section 3. The column
names would be right and the association would be wrong, which is the worst
combination: nothing downstream can detect the problem from the schema.

**(b)** The two questions are: *what is the join key, and is it unique on each
side?* and *which single station does an event belong to?* The first is a
cardinality question and can be checked mechanically (`is_unique`, `validate=`).
The second is a scientific decision — nearest station, nearest station within a
distance limit, the station that recorded the event, or a station-weighted
average — and the correct answer depends on what the correction is for. No pandas
feature answers it.

**(c)** Compute the distance to every station, keep the nearest, and require it
to be within 50 km:

```python
# cross join on a constant key, then distance, then one row per event
pairs = events.assign(_k=0).merge(stations.assign(_k=0), on="_k")
pairs["dist_km"] = haversine(pairs)          # your distance function
near = pairs[pairs["dist_km"] <= 50.0]
nearest = (near.sort_values("dist_km")
                .drop_duplicates("event_id", keep="first"))
joined = events.merge(nearest, on="event_id", how="left", validate="one_to_one")
```

Events with no station within 50 km receive `NaN` in every station column,
because `how="left"` keeps them and the station fields are genuinely absent. The
number of such events must be reported — it is a data-coverage statement.

**(d)**

```python
assert len(joined) == len(events)
assert joined["event_id"].is_unique
```

The first asserts the row count was preserved, which is the property that the
region join destroyed. The second asserts that no event was duplicated by
matching more than one station, which is the other half of the same guarantee.

---

## ★10 — Estimating the cost before running it

**(a)** For each of the 50 shared key values: the left contributes 40,000 rows
and the right 5,000, so the product is `40,000 × 5,000 = 2 × 10⁸` rows. Across
50 values: **10¹⁰ rows** — ten billion.

**(b)** `10¹⁰ × 200 bytes = 2 × 10¹² bytes = 2 TB`. It does not fit in 16 GB; it
does not fit in any machine you are likely to have.

**(c)** Aggregate before joining. If the downstream question is a per-key summary,
`left.groupby("k")` reduces 2,000,000 rows to 50 and the join becomes trivial. If
the question genuinely needs the cross product, generate it *per key* and consume
it streaming — loop over the 50 key values, materialise one `2 × 10⁸`-row block at
a time (`2 × 10⁸ × 200 B = 40 GB`, still too large, so aggregate inside the loop
as well), or push the computation into a database where the engine can stream the
join without materialising it.

**(d)** A join is the wrong tool whenever you cannot state the row count of the
result *before* running it. If you cannot say "this join is many-to-one and
preserves the left cardinality", you are not joining; you are generating
combinations, and the size of the generation should be estimated first. The
estimate is a one-line calculation from the key cardinalities, and it is far
cheaper than a failed allocation.
