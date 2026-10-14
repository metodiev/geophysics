# Exercises — 03-04-04 Group-By, Aggregation and Reshaping

Attempt these **closed-book** before opening the
[solutions](./04-groupby-aggregation-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems that say "run the demo" refer to
[`../code/groupby_aggregation_demo.py`](../code/groupby_aggregation_demo.py);
report its **actual** output. The catalogue is **SYNTHETIC**
([`../code/synthetic_catalog.py`](../code/synthetic_catalog.py)) and is not the
USGS catalogue. Regional differences below are properties of the generator, not
statements about tectonics.

The six-row frame used in the foundational problems is

```python
g = pd.DataFrame({
    "region": ["A", "A", "B", "B", "A", "B"],
    "year":   [2020, 2021, 2020, 2021, 2020, 2021],
    "mw":     [2.1, 3.2, 2.5, 3.6, 4.0, 2.8],
    "depth_km": [5.0, np.nan, 8.0, 9.0, 12.0, np.nan],
})
```

---

## ★ Foundational

**★1.** For the frame `g`:

(a) Compute `g.groupby("region")["mw"].mean()` and write both values.
(b) Compute the group sizes.
(c) Which region has the larger mean, and is the difference larger than the
standard error of either mean? (Use the group size and the magnitude spread.)

---

**★2.** For `g`:

(a) Compute `g.groupby("region")["depth_km"].size()`. Write both values.
(b) Compute `g.groupby("region")["depth_km"].count()`. Write both values.
(c) Explain the difference, and state which one answers "how many events are in
each region".

---

**★3.** For `g`:

(a) Compute the long-form count `g.groupby(["region", "year"])["mw"].count()`.
Write all four values.
(b) Reshape it with `unstack(fill_value=0)` and write the resulting table.
(c) Verify that the sum of the table equals the number of rows.

---

**★4.** For `g`:

(a) Compute the per-region median magnitude.
(b) Compute `g["mw"] - g.groupby("region")["mw"].transform("median")`.
(c) Explain why the result has six entries rather than two.

---

## ★★ Applied

**★★5.** Run the demo, Section 2.

(a) Report `n_events`, `mean_mw`, `max_mw` and `median_depth_km` for all four
regions.
(b) Report the total energy per region.
(c) The four mean magnitudes lie within 0.03 of each other. Using a magnitude
spread of about 0.45 and group sizes of 108, 134, 87 and 62, compute the standard
error of each mean and state whether the spread across regions is significant.
(d) Which column in the table is the strongest regional signal, and what is its
range?

---

**★★6.** Run the demo, Section 1.

(a) Report the `size()` and `count()` columns for the deliberately holed frame.
(b) How many magnitudes were knocked out, and how do the per-region differences
account for them?
(c) If a rate table had been built from `count()`, by how much would Northvale's
event count be understated, in per cent?

---

**★★7.** Run the demo, Section 7.

(a) Report the event share and the energy share for each region.
(b) Which region has the largest event share, and which the largest energy share?
(c) Explain the reversal in terms of the largest event in the catalogue.
(d) A colleague writes "region X is the most seismically active because it has
the most events". Give the two-sentence correction.

---

**★★8.** Run the demo, Section 5.

(a) Report the shapes of the wide and melted frames.
(b) Report the result of the round-trip check.
(c) State what the round trip would have caught if `reset_index()` had been
omitted before the `melt`.

---

## ★★★ Research-oriented

**★★★9.** A study tabulates event counts by `region`, `year` and `mag_type`, then
computes a rate per region-year by dividing each cell by the number of days in
that year.

(a) Write the group-by that produces the count table in long form.
(b) Explain why adding `mag_type` as a third key does not change the structure of
the code, and what it changes about the interpretation.
(c) The division is a broadcast from the year key to the (region, year) rows.
Write it with a join on a year table, and state why a join is safer than a
positional division.
(d) State one statistical problem with a rate per (region, year, mag_type) cell
from a catalogue of ~390 events.

---

**★★★10.** You are asked to decide whether two regions have "different"
seismicity, using mean magnitude, event rate and energy release.

(a) For each of the three statistics, state what a difference would mean
physically and what sampling effect could produce it without any physical
difference.
(b) State a decision rule that combines the three, written as an inequality
involving the difference and its uncertainty.
(c) Explain why reporting all three is better than reporting the one with the
largest difference.
(d) State one thing you would refuse to conclude from 390 synthetic events, and
why.
