---
id: 03-04-04
title: "Group-By, Aggregation and Reshaping"
level: intermediate
prereqs: ["03-04-02"]
estimated_minutes: 90
tags: [pandas, groupby, aggregation, pivot, melt, reshaping, tidy-data]
---

# Group-By, Aggregation and Reshaping

Most geophysical questions are not about individual measurements. "Events per
region per year", "median depth by tectonic class", "energy released per year" —
each is a summary of a *group* of rows. The group-by is the operation that
expresses them, and reshaping is the operation that turns the answer into the
table the next step wants.

The shape of the output is a decision, and it is worth making deliberately.
Statements in the *split-apply-combine* idiom are the ones that scale; a loop
with a dictionary accumulator is the same computation with the parallelism
thrown away.

> The catalogue is **SYNTHETIC** (see `code/synthetic_catalog.py`), generated
> in-code from a fixed seed; it is not the USGS catalogue. Regional differences
> quoted here are properties of the generator and are never interpreted as
> tectonics.

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the split-apply-combine pattern and identify the split key, the
   applied function and the combining step in a given computation.
2. **Distinguish** `size()` from `count()` and predict where the two differ on a
   column with gaps.
3. **Write** a named aggregation whose output columns are self-documenting, and
   explain what it improves over `agg(["count", "mean"])`.
4. **Group** by two keys, keep the result in long form, and say why long form is
   the form to aggregate, filter and plot in.
5. **Reshape** long to wide with `unstack` and `pivot_table`, and back with
   `melt`, and verify the round trip.
6. **Predict** the output *shape* of `agg` (one row per group) versus `transform`
   (one row per input row) and choose accordingly.
7. **Explain** why aggregating a derived, non-linear quantity is not the same as
   aggregating its input, using radiated energy as the example.
8. **Recognise** when a group-by result's index is non-unique and what that means
   for a later `.loc`.

## Prerequisites

- [03-04-02 Indexing, Selection, loc/iloc and Boolean Masks](./02-indexing-selection.md)
  — masks select rows; group-by splits them.
- [03-04-01 Series, DataFrame and the Labeled-Data Model](./01-series-dataframe.md)
  — the grouped key becomes the index, so index semantics matter.

## 1. Split-apply-combine

`df.groupby(key)[value].func()` performs three steps:

1. **Split** the rows into one sub-frame per distinct value of `key`.
2. **Apply** `func` to the `value` column of each sub-frame independently.
3. **Combine** the results into one object indexed by the group keys.

The `[value]` slot is optional but recommended. `df.groupby("region").mean()` on
the full frame computes the mean of *every* numeric column, including columns
where a mean is meaningless. Selecting the column first keeps the computation and
the intent the same size.

The result's index is the group key. That is why `df.groupby("region")["mw"].mean()`
prints as a column of four numbers with region names on the left, and why
`.loc["Northvale"]` works on it afterwards — the key is the index.

A `GroupBy` object is **lazy**: `df.groupby("region")` performs no work at all
until a reduction is requested, which is why it can be built speculatively on a
large frame. Iterating it yields `(key, sub_frame)` pairs, which is occasionally
useful for debugging a single group and is a common performance trap when used
instead of an aggregation — a Python loop over groups pays interpreter overhead
once per group, and the built-in aggregations do not. When you find yourself
writing `for key, group in df.groupby(...)`, ask whether `agg`, `transform` or
`filter` expresses the same thing; it usually does, and it is faster.

## 2. `size()` versus `count()`

These look interchangeable and are not.

- `size()` counts **rows** in each group, ignoring values entirely.
- `count()` counts **non-missing values** in the selected column.

On a column with no gaps they agree, so a mistake stays invisible until the data
acquire a gap. The demo makes the distinction unavoidable by punching forty
magnitudes out of a clean frame:

| Region | `size()` | `count()` on `mw` |
|---|---|---|
| Eastmere | 108 | 98 |
| Northvale | 134 | 121 |
| Southgate | 87 | 78 |
| Westhold | 62 | 54 |

Row counts 108/134/87/62 are unchanged; magnitude counts fall by 10/13/9/8 — the
forty holes, distributed by region. A "number of events" column built with
`count()` on a mostly-complete column is right most of the time, which is the
worst kind of wrong.

Use `size()` when the question is "how many events" and `count()` only when the
question really is "how many of them have a magnitude recorded".

## 3. Named aggregation

```python
summary = df.groupby("region").agg(
    n_events=("event_id", "count"),
    mean_mw=("mw", "mean"),
    max_mw=("mw", "max"),
    median_depth_km=("depth_km", "median"),
)
```

Each argument is `output_name=("column", "function")`. The output is a tidy table
with usable column names, rather than a `MultiIndex` of `("mw", "mean")` pairs
that has to be flattened before plotting. The measured table on the synthetic
catalogue:

| Region | n_events | mean_mw | max_mw | median_depth_km |
|---|---|---|---|---|
| Eastmere | 108 | 2.421 | 4.0 | 41.280 |
| Northvale | 134 | 2.451 | 4.3 | 7.835 |
| Southgate | 87 | 2.444 | 3.7 | 11.725 |
| Westhold | 62 | 2.453 | 3.7 | 22.205 |

Two things to read from it. The mean magnitudes are all within 0.03 of each
other, so the generator gave every region the same magnitude distribution. The
median depths differ by a factor of five, which is the per-region depth model of
the generator and the only strong regional signal in the table. Reporting the mean
magnitude and calling the regions "different" would be reading noise; reporting
the median depth and calling them different is reading the model.

## 4. Two keys, and the long form

```python
long = df.groupby(["region", "year"])["event_id"].count().rename("n_events")
```

Forty rows: four regions times ten years. This is the **long** (or *tidy*) form —
one row per observation of the *summary*, with the keys as ordinary columns
(before grouping) or as a `MultiIndex` (after). It is the form to work in
because:

- filtering is a mask on a column rather than an index manipulation;
- adding a third key (`["region", "year", "mag_type"]`) changes nothing
  structurally;
- most plotting libraries and most model-fitting functions want it.

The **wide** form has the keys spread across the axes. It is the form to *read*
and to paste into a report.

## 5. Reshaping: long to wide and back

Two routes, same result:

```python
wide = long.unstack(fill_value=0)          # after grouping: keys -> columns
wide = df.pivot_table(index="region", columns="year",
                      values="depth_km", aggfunc="median")   # one step
```

`unstack` moves the innermost index level into the columns. `pivot_table` is
`groupby` plus `unstack` in one call, and it takes an `aggfunc` because a pivot
of repeated (region, year) pairs is an aggregation whether you call it one or
not. `fill_value=0` is right for a *count* — a year with no events really has
zero — and wrong for a *level* or a *depth*, where zero is a claim. Use
`pivot_table`'s default `NaN` there.

The measured `pivot_table` of median depth shows the Eastmere depths sitting at
37-54 km in every year while Northvale stays near 8 km — a structure that is
invisible in the four-row summary and obvious in the ten-column one. Reshaping is
how structure becomes visible.

Going back:

```python
back = wide.reset_index().melt(id_vars="region", var_name="year",
                               value_name="n_events")
```

`melt` gathers columns into rows; `reset_index` first lifts the row index back
into a column so it is preserved as an identifier. The demo verifies the round
trip rather than assuming it:

```
  wide shape (4, 10) -> melted shape (40, 3)
    long -> wide -> long reproduces the original counts: True
    rows compared: 40
```

A round-trip check is the cheapest possible test of a reshape. It catches the
lost index, the off-by-one, and the column that silently became the index.

### 5.1 `pivot` raises, `pivot_table` aggregates — pick deliberately

`pivot` requires that each (index, column) pair be unique and raises
`ValueError: Index contains duplicate entries, cannot reshape` when it is not.
`pivot_table` accepts duplicates and resolves them with its `aggfunc`. The two
are therefore not alternatives; they encode different assumptions:

- Use `pivot` when a duplicate would be a **bug** — one magnitude per station per
  phase, say — and you want the error.
- Use `pivot_table` when a duplicate is **expected** and an aggregation is the
  right resolution — many events per region per year.

Trying to pivot the full catalogue on `(region, year)` fails for exactly that
reason: there are many events in each cell. Grouping first and then unstacking,
or calling `pivot_table`, both work because both state the aggregation. Reaching
for `pivot_table` out of habit hides the case where the duplicates signalled a
problem.

## 6. `transform`: same grouping, different output shape

`agg` reduces each group to one number. `transform` applies the same function
but **broadcasts the result back to every row of the group**, so the output has
the same length and index as the input.

```python
df["region_median_mw"] = df.groupby("region")["mw"].transform("median")
df["mw_anomaly"] = df["mw"] - df["region_median_mw"]
```

This is the pipeline pattern for a group-wise anomaly: subtract the group's
central value from every member. The demo cross-checks the broadcast against an
explicit `map`:

```
    max |df minus hand-written map()| = 0.0
```

and reports the three largest positive anomalies — events that stand out from
their own region's magnitude distribution:

| event_id | region | mw | region median | anomaly |
|---|---|---|---|---|
| S0065 | Northvale | 4.3 | 2.3 | 2.0 |
| S0281 | Eastmere | 4.0 | 2.3 | 1.7 |
| S0298 | Northvale | 3.7 | 2.3 | 1.4 |

`transform` is the answer to "how do I use a group statistic in a per-row
computation without writing a join?" It is exactly a join on the group key, done
internally and correctly.

## 7. Aggregating a derived quantity

Magnitude is logarithmic; radiated energy is not. The relation
$\log_{10} E = 1.5M + 4.8$ (joules) means that summing energy and summing
magnitude are different aggregations of the same events, and they give different
regional pictures:

| Region | n_events | event share | energy share |
|---|---|---|---|
| Eastmere | 108 | 0.2762 | 0.2456 |
| Northvale | 134 | 0.3427 | 0.4722 |
| Southgate | 87 | 0.2225 | 0.1517 |
| Westhold | 62 | 0.1586 | 0.1305 |

Northvale holds 34 per cent of the events and 47 per cent of the energy, because
it contains the largest event; Eastmere holds the largest share of events and a
smaller share of energy. Neither column is more true than the other. The choice
of aggregation statistic is a statement about what the question means: "how much
activity" and "how much energy" are different questions.

The general rule: **a non-linear transform and an aggregation do not commute.**
Aggregating first and transforming second gives a different answer from
transforming first and aggregating second, and the order must be chosen to match
the question.

## 8. Worked code

```python
import pandas as pd, synthetic_catalog as sc

df = sc.clean_catalog()                                   # SYNTHETIC
df = df.assign(year=df["origin_time"].dt.year,
               energy_j=sc.mag_to_energy_j(df["mw"]))

by_region = df.groupby("region", observed=True).agg(
    n_events=("event_id", "count"),
    mean_mw=("mw", "mean"),
    median_depth_km=("depth_km", "median"),
    max_mw=("mw", "max"),
    total_energy_j=("energy_j", "sum"),
)

per_year = (df.groupby(["region", "year"], observed=True)["event_id"]
              .count().rename("n_events"))
wide = per_year.unstack(fill_value=0)
```

Note `observed=True`. Etymologically it is about categorical groupers — it
returns only the categories present in the data, and it becomes the default
behaviour in modern pandas. Passing it explicitly is harmless for text keys and
documents that you know the flag exists.

## 9. Physical interpretation

Aggregation is where a table becomes a claim about the Earth. "Mean magnitude by
region" is a claim that the regions differ in seismicity; "events per region per
year" is a claim about rates; "energy share" is a claim about which region does
the work. Each is a statistic, so each carries the statistic's caveats —
sensitivity to a few large events, dependence on the chosen central value, and
the fact that a mean over a small group has a large standard error.

Two habits follow. First, always report the group size with the group statistic;
a mean magnitude over 3 events and over 300 events are different claims. Second,
prefer the median alongside the mean for skewness-prone quantities. Magnitude is
roughly exponential (heavy right tail), so the mean magnitude is dominated by the
few large events — as the energy comparison in Section 7 shows from the other
direction.

## 10. Assumptions and limits

- **Group keys become the index.** The result of a group-by is not a normal
  table; it is a table with a meaningful index. `reset_index()` when you want it
  to behave like one, and remember `.loc` on a group index returns rows, not a
  scalar.
- **`agg` on many columns is not free.** `df.groupby(k).mean()` over twenty
  numeric columns costs twenty passes. Name the columns.
- **`pivot_table` silently aggregates.** If you expected one row per (region,
  year) and there are several, the pivot picks an `aggfunc` (mean by default) and
  gives you a number without complaining. Use `pivot_table` when you intend an
  aggregation and `pivot` when you want an error on duplicates.
- **`fill_value=0` is only right for counts.** For a level, a depth or a
  temperature, an absent group is not a zero.
- **Group-wise statistics inherit small-sample problems.** With four groups and
  ~100 events each, the standard error of the mean magnitude is about 0.045, so
  the 0.03 spread across regions in Section 3 is not distinguishable from noise.
  Say so rather than tabulating it as a finding.
- **`transform` requires a broadcastable result.** A function returning a
  different length raises; that is the check that the operation you asked for is
  the one you wanted.

## 11. Python demonstration

```
.venv/bin/python 03-scientific-computing/04-pandas/code/groupby_aggregation_demo.py
```

**Split-apply-combine.** `df.groupby("region")["mw"].mean()` returns, in one
line, four means with region names as labels:

```
region
Eastmere     2.4213
Northvale    2.4507
Southgate    2.4437
Westhold     2.4532
```

**`size` versus `count`, measured on a deliberately holed frame:**

```
           size()  count() on mw
region
Eastmere      108             98
Northvale     134            121
Southgate      87             78
Westhold       62             54
```

**Named aggregation, with the derived energy column:**

```
           n_events  mean_mw  max_mw  median_depth_km
region
Eastmere        108    2.421     4.0           41.280
Northvale       134    2.451     4.3            7.835
...
  Total radiated energy by region (J, from 10^(1.5 M + 4.8)):
    Eastmere    1.692e+11
    Northvale   3.252e+11
    Southgate   1.045e+11
    Westhold    8.986e+10
```

**Two keys.** Forty rows in long form; `unstack(fill_value=0)` gives a
four-by-ten table of counts for years 2010-2019, and `pivot_table` with
`aggfunc="median"` gives the same shape for median depth.

**Round trip.** `(4, 10)` wide melts to `(40, 3)` long, and the demo verifies the
counts are reproduced exactly: `long -> wide -> long reproduces the original
counts: True`.

**`transform`.** The anomaly column agrees with an explicit `map`-based broadcast
to `0.0`, and the top three within-region magnitude excesses are listed — all
from the two regions that contain the catalogue's four largest events.

## 12. Common mistakes

1. **`count()` when you meant `size()`.** Invisible until a gap appears.
2. **Grouping the whole frame when you meant one column.** `groupby(k).mean()`
   averages every numeric column, including identifiers that happen to be
   numeric.
3. **Leaving a `MultiIndex` in place and getting `("mw", "mean")` later.** Named
   aggregation avoids it.
4. **`pivot_table` when you wanted `pivot`.** The former aggregates duplicates;
   the latter raises. If duplicates would be a bug, use the one that raises.
5. **`fill_value=0` for a level.** Zero metres of groundwater is a measurement;
   "no measurement" is not.
6. **Aggregating after a non-linear transform, or before, without deciding.**
   Section 7.
7. **Dropping the group size.** A mean without an n is not a summary.
8. **Comparing group means without an uncertainty.** Section 3's 0.03 spread is
   inside the noise for this sample size, and the table does not say so by
   itself.
9. **Forgetting that the grouped index is non-unique across keys.** `.loc` on it
   can return several rows.
10. **Reshaping without verifying the round trip.** One line, catches most
    reshape bugs.

## 13. Real-world applications

- **Seismic hazard.** Event rates per source zone per year are a group-by on two
  keys; the long form feeds the recurrence model directly.
- **Network operations.** Data availability per station per month is a count
  aggregate, and the wide form (stations by month) is the standard QC heat-map.
- **Catalogue QC.** Magnitude-of-completeness estimates are computed per
  (network, year, region) — a three-key group-by whose output shape decides how
  the completeness map is interpolated.
- **Geochemistry.** Mean and median of an oxide per lithological unit, with the
  sample count as a required column, is the standard summary table.
- **Model evaluation.** Bias and RMS misfit per station from a residual table is
  a group-by whose named-aggregation output can be plotted without relabelling.

## 14. Further reading

- The pandas user guide sections *Group by: split-apply-combine* and *Reshaping
  and pivot tables* — the reference for `agg`, `transform`, `apply`, `pivot`,
  `pivot_table`, `stack`/`unstack` and `melt`.
- Hadley Wickham's *Tidy Data* paper, for the long-form convention and its
  rationale (the paper this repository's table conventions follow).
- [USGS Earthquake Hazards Program](https://earthquake.usgs.gov) — real
  catalogues in exactly the long form used here.

## 15. Related lessons

- Previous: [03 Cleaning: Missing Values, Duplicates and Outliers](./03-cleaning-data.md).
- Next: [05 Merging, Joining and Aligning Irregular Time Series](./05-merging-time-series.md).
- [03-04-06 Case Study: Earthquake Catalogue Wrangling](./06-earthquake-catalog-pandas.md)
  — a magnitude-frequency relation is a cumulative group-by.
- [03-01-09 Iterators, Generators and Lazy Evaluation for Large Data](../01-python-fundamentals/09-iterators-generators.md)
  — the memory discipline that group-by replaces with a compiled pass.

## Exercises

[`exercises/04-groupby-aggregation-exercises.md`](./exercises/04-groupby-aggregation-exercises.md),
with full worked answers in
[`exercises/04-groupby-aggregation-solutions.md`](./exercises/04-groupby-aggregation-solutions.md).

## Self-assessment checklist

- [ ] I can name the split key and the applied function in a group-by I write.
- [ ] I know when `size()` and `count()` differ and which one answers "how many
      events".
- [ ] I write named aggregations so the output columns are self-documenting.
- [ ] I can reshape long to wide and back, and I verify the round trip.
- [ ] I can choose between `agg` and `transform` from the output shape I need.
- [ ] I can explain why aggregating energy and averaging magnitude are different
      pictures of the same events.
- [ ] I report an `n` with every group statistic.
- [ ] I check whether a group difference is larger than its uncertainty before
      calling it a difference.
