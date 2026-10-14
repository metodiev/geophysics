# Solutions — 03-04-03 Cleaning: Missing Values, Duplicates and Outliers

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output. The catalogue is SYNTHETIC; nothing here is a
> claim about the Earth.

---

## ★1 — Triage counts

**(a)** **20** `depth_km` values are missing (408 − 388 non-null).

**(b)** **7** `mw` values are missing (408 − 401 non-null).

**(c)** **8** rows carry a duplicated `event_id`.

**(d)** **2** rows: the values `999.0` km (event S0001) and `-3.0` km (event
S0002). Neither is a depth; the first is a sentinel code and the second is a
negative value produced by a solver that ran off the end of its allowed range.

---

## ★2 — Robust location and scale

**(a)** Mean `= 135/9 = 15.0`; median `= 10.0` (the fifth of nine sorted values).

**(b)** Deviations from the median: `[5, 3, 2, 1, 0, 1, 2, 3, 50]`. Sorted:
`[0, 1, 1, 2, 2, 3, 3, 5, 50]`, and the median of those is `2.0`. So
MAD `= 2.0`.

**(c)** For 60: `0.6745 × 50 / 2 = 16.86`. For 5:
`0.6745 × (−5) / 2 = −1.69`.

---

## ★3 — The non-robust score on the same data

**(a)** Mean `= 15.0`; sample standard deviation `= 17.059` (with `ddof=1`, which
is what pandas uses).

**(b)** `z(60) = (60 − 15)/17.059 = 2.638`.

**(c)** No. The robust score is 16.86, far above 3.5; the mean/std score is 2.64,
**below** 3.5. A sigma-clipping rule at 3.5σ would keep a value that is 8 MAD
from the median.

---

## ★4 — `dropna` and `fillna`

**(a)** 3 values.

**(b)** 3 rows — `subset` restricts the test to the named column, so a row is
dropped only when *that* column is missing.

**(c)** 0 rows, if any other column also has a missing value; at most 3. Bare
`dropna()` drops a row when **any** column is missing, which is almost never the
intended rule and is the commonest over-cleaning mistake.

**(d)** It asserts that those two earthquakes occurred at exactly 0 km depth. That
is a measurement claim that the data do not support, and it will propagate into
every mean, histogram and depth-profile computed afterwards.

---

## ★5 — The mean of a contaminated column

**(a)** `mean = 23.94` km, `median = 14.83` km.

**(b)** `21.48` km.

**(c)** **2.46 km**. Two rows out of 408 moved the mean by more than fifteen per
cent of the median; the median did not move at all.

**(d)** The median, with the count, **after** the two impossible values are
removed. The order matters: robustness is a stopgap for a contaminated column,
whereas removal is the repair. Reporting a robust statistic while leaving a
sentinel in the data leaves the sentinel to contaminate everything else.

---

## ★6 — Robust versus non-robust outlier detection

**(a)** `median = 14.83` km, `MAD = 8.02` km.

**(b)** **19** rows at `|z| > 3.5`: the 999 km sentinel plus eighteen Eastmere
events. All nineteen flagged values have a robust deviation of more than 3.5 MAD
from the median, which is the stated criterion.

**(c)** **1** row; the sentinel scores **18.68** on that scale.

**(d)** The mean/std score divides by the standard deviation, and the standard
deviation is computed *from the same column that contains the outlier*. The 999 km
value inflates σ so much that it drags its own z-score down towards the
threshold, and it simultaneously raises the threshold's effective size for every
other value: the deep Eastmere events at 57–77 km are 5–8 MAD out but only ~2.5σ
out. The estimator is contaminated by the observation it is supposed to flag —
this is masking, and it is why scale estimates used for outlier detection are
robust ones.

---

## ★7 — Before and after

**(a)** 408 rows raw, 391 cleaned, **17 removed**.

**(b)** duplicate `event_id`: **8**; impossible depth: **2**; missing magnitude:
**7**; magnitude below M 2.0: **1**. Sum **18**.

**(c)** Because one row can carry two defects at once. Here one duplicate report
also had a missing magnitude, so it is counted under two reasons but removed once.
Counting reasons and counting rows answer different questions; only the row count
says how much data was lost.

**(d)** `N(M >= 2.0)` is 400 before and **391** after. `N(M >= 3.0)` is **48** in
both, because the two inadmissible magnitudes (`−1.0`) and the seven missing ones
were never eligible for `M >= 3.0`. The cleaning removed defects rather than
signal — which is the check that makes the policy defensible, and it is worth
running every time a cleaning step is added.

---

## ★8 — Duplicate reports

**(a)** **1** duplicate (the second S1 row), i.e. `duplicated("event_id").sum()`
is 1.

**(b)** The first row in current order: `S1` with `depth_km = 10.0`. `keep="first"`
is defined by row order, and row order is a property of the file.

**(c)** Sort by a stated priority so that N2 comes first, then keep the first:

```python
prio = {"N2": 0, "N1": 1}
df["_p"] = df["agency"].map(prio)
df = df.sort_values("_p").drop_duplicates("event_id", keep="first")
```

which keeps `S1` with `depth_km = 10.4`.

**(d)** A rule is reproducible and reviewable: "prefer network N2 because it is
the regional authority" can be checked, argued with and cited, whereas "keep the
first" silently encodes whatever order the ingestion happened to produce, and
changes when the file is re-exported.

---

## ★9 — A sentinel disguised as a measurement

**(a)** A `NaN` is *self-announcing*: `isna()` finds it, aggregations skip it,
and a plot leaves a gap. A `0.0` is indistinguishable from a legitimate
measurement of a shallow event at the surface, so nothing in the table flags it.
Every mean, histogram and depth-section that follows silently includes it, and no
statistic computed downstream can recover the distinction.

**(b)** Triage without assuming the sentinel value:

```python
d = df["depth_km"]
print(d.value_counts().head(10))         # does one value dominate?
print((d == 0.0).mean())                 # is an improbable value common?
print(d.quantile([0.0, 0.001, 0.01, 0.5]))   # a spike at the minimum
```

A large, round-valued mode at a physically implausible value — or a spike at the
very bottom of the range while the rest of the distribution is centred higher —
is the signature. Comparing against the neighbouring depth distribution, or
against the fraction expected at that depth, confirms it.

**(c)** Policy: convert `0.0` to `NaN`, then apply the missing-depth policy.
Cost: legitimate surface events (depth genuinely 0.0 km, which for a
crustal catalogue is rare but possible) are destroyed or imputed. The cost is
paid to avoid contaminating everything else; where surface events matter, the
distinction has to be recovered from another column (a depth-fixed flag, the
solver's status code) and the policy must say so.

**(d)** Two checks. First, the depth **histogram** before and after: the spike
should disappear and the rest of the distribution should be unchanged shape.
Second, the **event count** as a function of depth band: if converting the zeros
to `NaN` removes an implausible share of a depth band you believe should be
populated, then some of those zeros were real. A concerning result is a *change
in the shape* of the distribution elsewhere, which would mean the sentinel was
not confined to the value you assumed.

---

## ★10 — Two cleaning policies

**(a)** Policy A returns **380** rows (400 minus the 20 missing depths). Policy B
returns **400** rows, because every missing depth is filled.

**(b)** For the **mean depth by region**, policy B is defensible *provided the
imputed count is reported*, because the mean is a summary of the population and
the imputation is a stated model of the missing rows; but policy A is cleaner if
the missing rows differ systematically (they usually do — a missing depth means a
poorly constrained hypocentre, which correlates with magnitude and station
coverage). For the **magnitude-frequency fit**, the depth policy is irrelevant to
the count above a magnitude threshold, so use policy A and avoid the imputation
entirely: never impute a variable the study does not need.

**(c)** A sentence that carries the counts:

> "Missing depth values (20 of 400 rows, 5.0 %) were imputed with the median
> depth of the event's region; the 8 duplicate reports were resolved by network
> priority (SYN-NET1 over SYN-NET2); 2 depths outside [0, 700] km were removed
> as invalid. 17 rows were removed in total."

**(d)** Recompute the headline statistic with and without the imputed rows, and
compare. The test:

```python
with_imputed = stat(clean_imputed)
without     = stat(clean_imputed.drop(index=imputed_index))
```

A difference **larger than the statistic's own uncertainty** is the concerning
result, because it means the conclusion depends on the imputation rather than on
the measurements. A difference inside the uncertainty is acceptable *and must
still be reported*, since "we checked and it does not matter" is a stronger
statement than silence.
