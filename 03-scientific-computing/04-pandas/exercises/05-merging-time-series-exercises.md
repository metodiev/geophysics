# Exercises — 03-04-05 Merging, Joining and Aligning Irregular Time Series

Attempt these **closed-book** before opening the
[solutions](./05-merging-time-series-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems that say "run the demo" refer to
[`../code/merging_time_series_demo.py`](../code/merging_time_series_demo.py);
report its **actual** output. Every table is **SYNTHETIC**
([`../code/synthetic_catalog.py`](../code/synthetic_catalog.py)): the events are
generated, the stations are invented and the two time series are simulated.

Cardinality language used throughout: a key value is **unique** on a side if it
appears once there, and **repeated** if it appears more than once.

---

## ★ Foundational

**★1.** A left table has 100 rows keyed on `k`, of which 10 distinct values each
appear 10 times. A right table has 10 rows, one per distinct `k`.

(a) What is the cardinality of the right key?
(b) How many rows does `left.merge(right, on="k", how="left")` return?
(c) What `validate=` value states the assumption made about the right key?
(d) What happens if the right table accidentally contains a duplicated `k`?

---

**★2.** A right table has 5 rows and a left table has 1 row, keyed on `k` with a
single shared value.

(a) How many rows does a left join return?
(b) What is this cardinality called?
(c) Which table's columns are repeated across the output rows?

---

**★3.** Two frames are combined with `pd.concat([a, b], axis=1)`.

(a) On what are they aligned?
(b) What happens to labels present in one frame and not the other?
(c) What is this alignment equivalent to in join terms?

---

**★4.** A daily series has 672 observations over 730 calendar days; a second
series has 240 observations over the same period.

(a) How many timestamps are in the union of the two indexes?
(b) If they share 221 timestamps, how many are missing from exactly one series?
(c) State the one-line expression that puts both onto the union.

---

## ★★ Applied

**★★5.** Run the demo, Section 2.

(a) Report the number of events, the number of stations and the row count of the
naive merge.
(b) Report the minimum and maximum rows per event in the merged frame.
(c) Report the total energy before and after the merge and the inflation factor.
(d) Explain why the inflated total has plausible units and five significant
figures.

---

**★★6.** Run the demo, Section 2, part (b).

(a) Write the group-by-and-merge repair that enriches the station table with the
regional event count.
(b) Report the row count of the result and confirm it equals the station count.
(c) State the modelling assumption that makes this repair correct for the
question "how many events in this station's region".

---

**★★7.** Run the demo, Section 3.

(a) Report the outer-joined table, including `Outerisle`.
(b) Explain the `NaN` in the `events_per_station` column for `Outerisle`.
(c) Report how many regions `how="inner"` would keep, and what it would hide.

---

**★★8.** Run the demo, Section 5.

(a) Report the number of rows in the asof result and the number with a value
inside the 5-day tolerance.
(b) At which date does the first groundwater value appear, and what are the four
rows before it?
(c) State what changes if `tolerance` is removed, and give the physical reason
the tolerance exists.

---

## ★★★ Research-oriented

**★★★9.** You must attach station metadata (elevation, instrument, network) to
every event, so that a station correction can be applied.

(a) Explain why a direct merge on `region` is not the operation you want, even
though it produces a table with the right column names.
(b) State the two questions you must answer before writing any join, and why each
is a scientific decision rather than a pandas one.
(c) Write the join you would run, for the case where an event is assigned to the
nearest station within 50 km, and say what happens to events with no station in
range.
(d) State the check you would run after the join to prove the row count was
preserved.

---

**★★★10.** A left table has 2,000,000 rows keyed on `k` with 50 distinct values,
each appearing 40,000 times. A right table has 500,000 rows keyed on `k` with 100
distinct values, each appearing 5,000 times.

(a) Estimate the row count of a many-to-many merge on `k`, assuming all 50 of the
left's distinct values are among the right's 100.
(b) Estimate the peak memory of the result for a row of 200 bytes, and say whether
it fits in a 16 GB machine.
(c) Describe one change to the pipeline that avoids materialising that result.
(d) State the general rule for when a join is the wrong tool.
