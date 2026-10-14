---
id: 03-04-03
title: "Cleaning: Missing Values, Duplicates and Outliers"
level: intermediate
prereqs: ["03-04-02"]
estimated_minutes: 90
tags: [pandas, missing-data, duplicates, outliers, data-quality, imputation]
---

# Cleaning: Missing Values, Duplicates and Outliers

A catalogue that arrives off the wire is never the table a tutorial shows you.
Depths are absent for some events because no depth solution was determined.
Some events appear twice because two networks located them and both reports were
merged in. A few "depths" are not depths at all but sentinel codes — `999`, or
`-3` — left by a program that had no better way to say "no value".

Cleaning is the process of deciding what to do about each of these, and the
decision is the scientific content. pandas will happily drop or fill anything;
it will not tell you which choice preserves the quantity you are about to
measure. This lesson supplies a policy, applies it, and — the part that is
usually skipped — **reports how many rows each step removed**, because that
count is what a reader needs in order to judge the result.

> The catalogue is **SYNTHETIC** (see `code/synthetic_catalog.py`), generated
> in-code from a fixed seed. It is not the USGS catalogue. The defects, however,
> are of the kinds real catalogues have, and the policy is the one you would
> apply to a real one.

## Learning objectives

By the end of this lesson you will be able to:

1. **Triage** an unfamiliar table with one pass of null counts, duplicate
   counts and range checks, before changing anything.
2. **Distinguish** a missing value (`NaN`) from a sentinel value (`999`) and
   explain why the second is more dangerous.
3. **State and justify** a policy for a missing value — drop, impute, or model —
   in terms of which variable is the analysis variable and which is supporting.
4. **Quantify** the cost of a policy by the number of rows removed or altered,
   and report it alongside the result.
5. **Detect** duplicate reports with `duplicated`, and choose `keep=` from a
   stated rule rather than from row order.
6. **Detect** outliers with a robust median/MAD score, and explain why a
   mean/standard-deviation score hides the largest outlier in a skewed column.
7. **Separate** two decisions that are often conflated: dropping *impossible*
   values, and keeping *unusual but possible* ones.
8. **Predict** how a cleaning choice propagates into a magnitude-frequency
   count, and verify the prediction.

## Prerequisites

- [03-04-02 Indexing, Selection, loc/iloc and Boolean Masks](./02-indexing-selection.md)
  — every cleaning step is a mask or a single-step assignment.
- [03-04-01 Series, DataFrame and the Labeled-Data Model](./01-series-dataframe.md)
  — `NaN` semantics and NaN-skipping aggregation.

## 1. Triage before treatment

Change nothing until you have looked. Five one-liners cover almost every table:

```python
raw.shape                        # rows, columns
raw.isna().sum()                 # missing per column
raw.duplicated("event_id").sum() # repeated keys
raw["depth_km"].describe()       # range, quartiles
raw.dtypes                       # is anything text that should be numeric?
```

On the synthetic catalogue this returns 408 rows; 20 missing depths, 7 missing
magnitudes, none missing elsewhere; 8 repeated event identifiers; and a
`depth_km` range of `-3.0` to `999.0`. Every defect the lesson addresses is
visible in five lines, and none of them required a plot.

The `describe()` range is the part people skip. A minimum of `-3.0` km and a
maximum of `999.0` km are both statements that something is wrong, and they are
the entry point to the outlier discussion in Section 4.

## 2. Missing values

### 2.1 What `NaN` is, and how it behaves

`NaN` is a floating-point value meaning "not a number". It has three properties
that matter:

- **It propagates.** Any arithmetic involving it gives `NaN`. `NaN + 1` is
  `NaN`, and `NaN > 0` is `False`.
- **It is skipped by default in aggregations.** `df["depth_km"].mean()` is the
  mean of the values present. This is convenient and it is a decision you are
  making implicitly every time.
- **It does not equal itself.** `NaN == NaN` is `False`. Test for missingness
  with `isna()`, never with `==`.

Missing depths in the synthetic catalogue are 20 of 408 rows, or 4.9 per cent;
missing magnitudes are 7 rows, 1.7 per cent. Those fractions are small enough
that no policy is obviously wrong, which is exactly why the policy must be
stated rather than left to whatever the code happened to do.

### 2.2 Three policies

| Policy | When it is right | Cost |
|---|---|---|
| **Drop the row** | the missing variable is an analysis variable | loses the other variables in that row |
| **Impute** | the variable is supporting, and a stated imputation is defensible | imports an assumption into every statistic computed from it |
| **Model it** | the missingness is informative and the sample is large | complexity, and a model whose assumptions must be checked |

For this catalogue the split is clean and the reasoning is short.

- **Magnitude is dropped.** It is the analysis variable of the
  magnitude-frequency relation (lesson [06](./06-earthquake-catalog-pandas.md)).
  Imputing it would manufacture the distribution we are about to measure — the
  imputed values would be drawn from the very relation being fitted, so the fit
  would be partly a fit to its own assumption. Seven rows out of 408 is a cheap
  price for avoiding that.
- **Depth is imputed** with the median depth of the same region. Depth is
  supporting here: it is used to describe the population, not to compute the
  frequency law. A regional median preserves the regional structure (the
  synthetic Eastmere events really are deeper) and is robust to the sentinels —
  whereas a global mean would drag the sentinels into every gap.

### 2.3 The contrast worth remembering

`fillna(0)` is the default reflex and it is almost always wrong. On the depth
column the demo measures:

```
    mean after fillna(0) : 22.73 km   (asserts 0 km depth)
    mean after dropping  : 23.90 km
```

Neither number is a depth anyone measured. The first asserts that twenty
earthquakes occurred at exactly 0 km, which is not a thing. The difference
between the two is the imputation bias, made visible by computing both. Compute
the alternatives and show the spread; do not pick one and hope.

## 3. Duplicates

### 3.1 Exact duplicates and key duplicates

`.duplicated()` with no argument compares *whole rows*. That is rarely what you
want, because two reports of the same event differ in a decimal place or in the
station count. `duplicated("event_id")` compares the key, and on the synthetic
catalogue it finds exactly the eight planted repeat reports:

```
  events reported twice: 8 (S0004, S0035, S0077, S0134, S0139, S0176, S0232, S0275)
```

`duplicated(["origin_time", "latitude", "longitude"])` is the physical test —
same time, same place, same event — and it finds the same eight, which is the
cross-check that the key is being used consistently.

### 3.2 `keep=` is a rule, not a default

`.drop_duplicates("event_id")` keeps the first occurrence *in current row order*.
That makes the result depend on how the file happened to be sorted, which is the
kind of hidden dependency that changes an answer when a file is re-exported.

State the rule instead. For this catalogue the rule is jurisdictional: prefer the
network in a listed priority order.

```python
df["_prio"] = df["agency"].map({"SYN-NET1": 0, "SYN-NET2": 1}).fillna(2)
df = df.sort_values("_prio").drop_duplicates("event_id", keep="first")
```

Now `keep="first"` means "highest-priority network", which is a sentence you can
defend. The demo shows the two reports of event S0004:

```
event_id  depth_km  mw   agency
   S0004     36.36 NaN SYN-NET1
   S0004     34.38 NaN SYN-NET2
```

Two depths, a kilometre and a half apart. The cleaning step decides which one
the study will use, and that decision belongs in the methods section, not in
the ordering of an input file.

### 3.3 The cost of not doing it

Per-region counts, before and after removing the repeat reports:

| Region | with duplicates | one row per event | over-count |
|---|---|---|---|
| Eastmere | 116 | 112 | 4 |
| Northvale | 137 | 136 | 1 |
| Southgate | 89 | 88 | 1 |
| Westhold | 66 | 64 | 2 |

Eight duplicate rows inflate four regional rates. Rates feed hazard estimates
and b-value fits; an eight-row error on a 400-row catalogue is a 2 per cent
error on a count and a larger error on any statistic dominated by the duplicated
events.

## 4. Outliers

### 4.1 Sentinels are not outliers

The depth column contains `999.0` and `-3.0`. Those are not extreme
measurements; they are error codes. The distinction matters because the
treatment differs:

- **Sentinels** must be **removed** (or converted to `NaN`, which is the same
  thing done honestly). No statistical argument can rescue a value that means
  "unknown".
- **Outliers** are **kept unless there is a physical or instrumental reason to
  discard them**. A genuinely deep earthquake is a fact.

The diagnostic is the range check: a depth outside roughly `[0, 700]` km is not a
depth. `df["depth_km"].between(0, 700)` is the mask.

### 4.2 A robust score, and why the mean/std score fails

The robust score uses the median and the median absolute deviation:

```python
med = d.median()
mad = (d - med).abs().median()
z   = 0.6745 * (d - med) / mad        # Iglewicz-Hoban
```

The constant 0.6745 makes the score comparable to a standard deviation for
normally distributed data. The demo measures `median = 14.83` km and
`MAD = 8.02` km, and flags 19 rows at a threshold of 3.5 — one sentinel and
eighteen events from the deep Eastmere region.

Now the instructive part. A mean/standard-deviation score on the same column
flags **one** row:

```
    rows flagged at |z| > 3.5 : 1
    the 999 km sentinel scores: 18.68
```

The sentinel scores 18.7, so it is flagged — but the eight events at 57-77 km,
which are 5 to 8 MAD away from the median and are the very population a
"deep events" question is about, score below the threshold because the standard
deviation has been inflated by the same 999. The estimator and the outlier are
the same observation: the outlier enlarges the scale against which it is
measured. This is **masking**, and it is the reason robust statistics exist.

### 4.3 The decision

State the decision and its boundary:

- **Drop** depths outside `[0, 700]` km: two rows. A depth of 0 km and a depth of
  999 km are both errored values.
- **Keep** everything inside the range, including the eighteen flagged deep
  events. They are unusual, not impossible; the outliers flagged by the robust
  score are the regional structure, and deleting them would delete the signal. A
  cleaning step that removes real structure is worse than no cleaning.

That second decision is the one that is usually made silently and wrongly. A
pipeline that "removes outliers" with a sigma-clipping rule would have deleted
the Eastmere events and produced a catalogue with no deep seismicity, without
anything in the log to say so.

## 5. Worked code: the whole policy

The full policy is in `synthetic_catalog.clean_catalog()`, and the demo applies
it step by step. In order:

```python
# 1. drop impossible depths (sentinels)
df = df[df["depth_km"].isna() | df["depth_km"].between(0.0, 700.0)]
# 2. drop events with no magnitude (analysis variable)
df = df[df["mw"].notna()]
df = df[(df["mw"] >= 2.0) & (df["mw"] <= 9.0)]     # also removes the -1.0 code
# 3. impute missing depth from the regional median
for region, group in df.groupby("region"):
    df.loc[group.index[group["depth_km"].isna()], "depth_km"] = group["depth_km"].median()
# 4. one row per event, preferred network first
...
```

Result, as printed by the demo:

| Quantity | raw | cleaned |
|---|---|---|
| rows | 408 | 391 |
| missing `mw` | 7 | 0 |
| missing `depth_km` | 20 | 0 |
| duplicate `event_id` | 8 | 0 |
| depth outside 0..700 | 2 | 0 |
| `mw` < 2.0 | 1 | 0 |

**17 rows removed.** The demo also prints the row-level reasons, which sum to
**18** — one more than the rows removed, because a single row can carry two
defects. Counting reasons and counting rows are different operations, and only
the row count tells you how much data you lost.

Finally, the check that the cleaning did not move the quantity of interest:

```
         raw: N(M>=2.0) = 400   N(M>=3.0) = 48   N(M>=4.0) = 2
     cleaned: N(M>=2.0) = 391   N(M>=3.0) = 48   N(M>=4.0) = 2
```

The events carrying an error-code magnitude and the events with no magnitude
were never eligible for `N(M >= 3.0)`, so the counts above M 2 and above M 3 are
unchanged. That is the
right shape of answer: the cleaning removed defects, not signal. Had the
duplicate removal changed `N(M >= 3.0)`, the duplicates would have been events
above M 3 and the report would need to say so.

## 6. Physical interpretation

Cleaning is where measurement uncertainty enters a table. Every choice in this
lesson is a statement about the instrument or the network:

- **A missing magnitude** means the event was detected but not sized. Dropping it
  biases the catalogue towards better-recorded events — usually the larger ones,
  near stations. That bias is real and is the reason magnitude of completeness is
  estimated (lesson [06](./06-earthquake-catalog-pandas.md)) rather than assumed.
- **A missing depth** means the hypocentre was poorly constrained, which happens
  for small or poorly recorded events. Imputing the regional median assumes those
  events are distributed like the well-located ones, which is an assumption, and
  it is the reason the imputation count (20 rows) is reported.
- **Duplicate reports** are a statement about networks, not about the Earth. Two
  solutions for one earthquake are two estimates of one hypocentre, and choosing
  between them is choosing an estimator.
- **The 999 sentinel** is a software artefact that has been mistaken for data in
  published catalogues. Its presence is a fact about the processing chain.

## 7. Assumptions and limits

- **`NaN` is for float columns.** An integer column cannot hold `NaN`; pandas
  upcasts it to float, or (with pandas 3's nullable dtypes) you choose an
  `Int64` extension dtype. Watch for an `int64` column that has silently become
  `float64` because one value was missing.
- **The imputation is single-valued.** A regional median is a point estimate with
  no uncertainty. A study whose conclusions depend on the imputed depths must say
  so; the honest alternatives are multiple imputation or a robustness test with
  and without the imputed rows.
- **The outlier threshold is a choice.** 3.5 MAD is a common convention and not a
  law. Report the threshold, the median and the MAD, so a reader can apply
  another one.
- **Robustness does not make the decision for you.** The robust score correctly
  flagged the deep events; the *decision* to keep them came from the geology, not
  from the statistic.
- **Deduplication can hide disagreement.** After `drop_duplicates` there is one
  depth for each event and no record of the spread between networks. If that
  spread matters, aggregate it first (`std` per event) and keep it as a column.
- **Cleaning is not idempotent in the presence of judgement.** Running the
  pipeline twice is fine; running two *versions* of the pipeline and comparing
  the outputs silently is not.

## 8. Python demonstration

```
.venv/bin/python 03-scientific-computing/04-pandas/code/cleaning_data_demo.py
```

**Triage.** Missing counts (`depth_km 20`, `mw 7`), eight duplicate identifiers,
and the two impossible depths:

```
event_id   region  depth_km   agency
   S0001 Westhold     999.0 SYN-NET1
   S0002 Eastmere      -3.0 SYN-NET2
```

**The mean is contaminated, the median is not:**

```
    depth_km  mean   =    23.94 km   median =   14.83 km
    depth_km  mean excluding the two impossible values = 21.48 km
  Two impossible rows move the mean by 2.46 km and leave the
  median untouched.
```

Two rows out of 408 move the mean by 2.46 km. That is the sensitivity of a
non-robust statistic, measured rather than asserted.

**Duplicates and their cost.** Eight repeated events, and the over-count per
region (4, 1, 1, 2) shown in the table of Section 3.3.

**Robust versus non-robust outlier scores.** 19 rows flagged by median/MAD,
1 row by mean/std, with the sentinel scoring 18.68 — the masking failure of
Section 4.2, reproduced.

**Before and after.** 408 → 391 rows, 17 removed, 18 row-level reasons. And the
final check that the magnitude-frequency counts above M 2 and M 3 are unchanged.

## 9. Common mistakes

1. **`fillna(0)` for a physically positive quantity.** Depth, magnitude, station
   count, distance. Zero is a claim.
2. **`dropna()` with no arguments.** It drops every row containing any `NaN` in
   any column, which is usually far more than intended. Name the subset:
   `dropna(subset=["mw"])`.
3. **`duplicated()` with no arguments.** Whole-row comparison misses
   re-analysed duplicates, which differ in the digits.
4. **`drop_duplicates(keep="first")` without stating row order.** The result then
   depends on the source file's history.
5. **`drop_duplicates` on the wrong key.** Deduplicating on `origin_time` alone
   merges two genuinely distinct events with the same second-resolution
   timestamp.
6. **Removing statistical outliers by default.** As Section 4.3 shows, this
   deletes real structure. Remove the impossible; investigate the unusual.
7. **`mean`/`std` z-scores on a skewed column.** The sentinel inflates the scale
   that is supposed to expose it.
8. **Reporting the cleaned result without the removed-row count.** A reader cannot
   judge a policy they cannot see.
9. **Filling a `NaN` that means "not measured" with a value that means "measured
   as zero".** These are different states and the difference is often the
   scientific question.
10. **Assuming cleaning is documented because the code exists.** The policy
    belongs in the methods, in prose, with the counts.

## 10. Real-world applications

- **ISF/ISC bulletin merging.** Catalogs from different agencies are merged into
  a composite bulletin; de-duplication and priority rules are the core of that
  process, and the choices are published.
- **Magnitude of completeness.** Every b-value depends on where the catalogue is
  judged complete; how missing and duplicated events were handled changes that
  judgement.
- **Array processing QC.** A seismic array's automatic picks carry quality flags,
  and a station's data availability column has gaps that mean "offline", not
  "zero". The same `NaN`-versus-zero decision recurs.
- **Geochemical and geochronology tables.** Below-detection-limit values are
  conventionally reported as sentinels and are the classic case where treating a
  code as a number biases a regression.
- **Model-output archives.** A failed model run writes `-999` into a netCDF
  variable, and a naive annual mean then includes it. The sentinel is the same
  problem wearing different clothes.

## 11. Further reading

- The pandas user guide sections *Working with missing data* and *Duplicated
  values* — the semantics of `isna`, `dropna`, `fillna`, `duplicated` and
  `drop_duplicates` used above.
- The pandas user guide section on nullable dtypes, for integer columns that need
  to hold a genuine missing value.
- [USGS Earthquake Hazards Program](https://earthquake.usgs.gov) — the
  authoritative real catalogue, and its
  [FDSN event service](https://earthquake.usgs.gov/fdsnws/event/1/) for
  downloading data with quality flags rather than synthetic defects.

## 12. Related lessons

- Previous: [02 Indexing, Selection, loc/iloc and Boolean Masks](./02-indexing-selection.md).
- Next: [04 Group-By, Aggregation and Reshaping](./04-groupby-aggregation.md) —
  the regional medians used for imputation here are a group-by.
- [03-04-06 Case Study: Earthquake Catalogue Wrangling](./06-earthquake-catalog-pandas.md)
  — where the cleaned catalogue is used and the completeness problem is faced.
- [21-statistics-bayesian-ml](../../21-statistics-bayesian-ml/README.md) — for imputation
  as a statistical model rather than a single fill.

## Exercises

[`exercises/03-cleaning-data-exercises.md`](./exercises/03-cleaning-data-exercises.md),
with full worked answers in
[`exercises/03-cleaning-data-solutions.md`](./exercises/03-cleaning-data-solutions.md).

## Self-assessment checklist

- [ ] I run the five-line triage before changing anything.
- [ ] I can explain the difference between `NaN` and a sentinel value.
- [ ] I can state my missing-value policy and why the analysis variable is never
      imputed in a distributional study.
- [ ] I report the number of rows removed, and I know that reasons can outnumber
      rows.
- [ ] I choose `keep=` from a stated rule, not from row order.
- [ ] I can compute a median/MAD score and explain why a mean/std score masked
      the largest outlier.
- [ ] I distinguish "impossible" (remove) from "unusual" (keep, and investigate).
- [ ] I check that cleaning did not change the quantity I am about to report.
