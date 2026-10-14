# Exercises — 03-04-03 Cleaning: Missing Values, Duplicates and Outliers

Attempt these **closed-book** before opening the
[solutions](./03-cleaning-data-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems that say "run the demo" refer to
[`../code/cleaning_data_demo.py`](../code/cleaning_data_demo.py); report its
**actual** output. The catalogue is **SYNTHETIC**
([`../code/synthetic_catalog.py`](../code/synthetic_catalog.py)) and is not the
USGS catalogue.

Every answer that involves a decision must state the decision **and** the count of
rows it affects.

---

## ★ Foundational

**★1.** On the synthetic catalogue (408 raw rows):

(a) How many `depth_km` values are missing?
(b) How many `mw` values are missing?
(c) How many rows have a duplicated `event_id`?
(d) How many rows contain a depth outside the physically admissible range
`[0, 700]` km, and what are the two values?

---

**★2.** A nine-value depth column is
`[5, 7, 8, 9, 10, 11, 12, 13, 60]`.

(a) Compute the mean and the median.
(b) Compute the median absolute deviation (MAD).
(c) Compute the robust z-score `0.6745 (x - median) / MAD` for the value 60 and
for the value 5.

---

**★3.** For the same nine values:

(a) Compute the mean and the sample standard deviation (`ddof=1`).
(b) Compute the mean/std z-score of the value 60.
(c) Is either score above the common threshold of 3.5?

---

**★4.** A five-row frame has `depth_km` non-null in three rows. State the result
of each:

(a) `df["depth_km"].dropna()` — how many values?
(b) `df.dropna(subset=["depth_km"])` — how many rows?
(c) `df.dropna()` — how many rows, and what additional assumption does it make?
(d) `df["depth_km"].fillna(0)` — what claim does it make about the two missing
rows?

---

## ★★ Applied

**★★5.** Run the demo, Section 1.

(a) Report the mean and the median depth.
(b) Report the mean depth after excluding the two impossible values.
(c) By how much did two rows out of 408 move the mean?
(d) State which of the two statistics you would report for this column and why.

---

**★★6.** Run the demo, Section 4.

(a) Report the median and the MAD.
(b) How many rows does the robust score flag at `|z| > 3.5`, and how many of them
are in the Eastmere region?
(c) How many rows does a mean/std z-score flag at the same threshold, and what
does the sentinel score?
(d) Explain the result of (c) in terms of the quantity the two scores divide by.

---

**★★7.** Run the demo, Section 5.

(a) Report the row counts before and after cleaning, and the number removed.
(b) Report the four row-level reason counts and their sum.
(c) Why can the reasons sum to more than the rows removed?
(d) Report the `N(M >= 2.0)` count before and after, and explain why
`N(M >= 3.0)` is unchanged.

---

**★★8.** A three-event frame is

| event_id | depth_km | agency |
|---|---|---|
| S1 | 10.0 | N1 |
| S1 | 10.4 | N2 |
| S2 | 20.0 | N1 |

(a) How many duplicate `event_id` values are there?
(b) Which row survives `drop_duplicates("event_id")`, and which depth does it
carry?
(c) Which row survives if the rule is "prefer N2", and how do you implement that
rule?
(d) State, in one sentence, why a rule is better than `keep="first"` alone.

---

## ★★★ Research-oriented

**★★★9.** A new defect class appears: a `depth_km` column where `0.0` is used to
mean "no depth determined", because an upstream integer column could not hold
`NaN`.

(a) Why is this worse than a `NaN`?
(b) Write the triage step that detects it, without assuming which value is the
sentinel.
(c) State a policy that recovers the information, and its cost.
(d) State one thing you could check afterwards to confirm the policy did not
destroy real data.

---

**★★★10.** You clean a 400-row catalogue in two ways: policy A removes the 20
missing depths, policy B imputes them with the regional median. Everything else
is identical.

(a) How many rows does each policy return?
(b) Which policy would you use for an estimate of mean depth by region, and
which for a magnitude-frequency fit, and why?
(c) Design the reported sentence that makes either choice auditable, including
the counts.
(d) A reviewer asks whether the imputed rows changed the answer. Describe the
test you would run, in one or two sentences, and what result would be
concerning.
