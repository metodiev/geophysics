---
id: 03-04-06
title: "Case Study: Earthquake Catalogue Wrangling"
level: intermediate
prereqs: ["03-04-03", "03-04-04", "03-04-05"]
estimated_minutes: 90
tags: [pandas, case-study, seismicity, magnitude-frequency, gutenberg-richter, completeness]
---

# Case Study: Earthquake Catalogue Wrangling

This lesson runs the whole pipeline on the running example: triage, clean, bin,
aggregate, estimate, and report with the caveats attached. The scientific object
is the **magnitude-frequency relation** — the observation that small earthquakes
outnumber large ones by a nearly constant ratio — and the standard description of
it is the Gutenberg-Richter law, whose slope is the b-value. Estimating a
b-value from a catalogue is one of the most-repeated computations in observational
seismology, and it is almost entirely a pandas exercise: bin, count cumulatively,
fit, and check the sensitivity to the one assumption that dominates everything
else.

> ## The catalogue is SYNTHETIC
>
> Every event in this lesson is generated in-code by `code/synthetic_catalog.py`
> from a fixed random seed, using a Gutenberg-Richter magnitude model with
> b-value 1.05 and completeness at M 2.0. It is **not** the USGS catalogue, not
> the ISC bulletin, and not an observation of the Earth.
>
> The consequence for this lesson is direct and must be stated: **any b-value
> computed below is an illustration of the calculation and a check that pandas
> recovers the generator's known input. It is not a geophysical result and must
> never be quoted as one.** The *methods* transfer to real catalogues; the
> *numbers* do not.

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the Gutenberg-Richter relation in both its cumulative and its
   differential form, and say what the b-value is the slope of.
2. **Build** a binned magnitude histogram with `pd.cut` and a cumulative
   frequency count with a boolean mask, without writing a loop.
3. **Estimate** b by maximum likelihood (the Aki-Utsu estimator) and by least
   squares on cumulative counts, and explain why the two disagree.
4. **Explain** why the choice of the magnitude of completeness dominates the
   uncertainty of the estimate, and demonstrate the sensitivity instead of
   asserting it.
5. **Report** a b-value with the estimator, the completeness assumption, the
   sample size and the sensitivity range — and **refuse** to report one from
   data that cannot support it.
6. **Justify** which events were dropped in cleaning and how many rows each
   policy step removed.
7. **Read** a catalogue summary (rate per year, energy share, largest event) and
   say what each column is and is not evidence for.
8. **Use** an in-memory CSV round trip and state what a CSV does and does not
   preserve.

## Prerequisites

- [03-04-03 Cleaning: Missing Values, Duplicates and Outliers](./03-cleaning-data.md)
  — the policy applied in Section 2.
- [03-04-04 Group-By, Aggregation and Reshaping](./04-groupby-aggregation.md)
  — the cumulative count is an aggregation.
- [03-04-05 Merging, Joining and Aligning Irregular Time Series](./05-merging-time-series.md)
  — only needed if you extend the study to station metadata.

## 1. The question, and the data

The question is: *how does the rate of earthquakes depend on magnitude?* The data
are a catalogue with one row per event and columns for origin time, position,
depth, magnitude and the network that located it. The synthetic table has 400
base events plus 8 duplicate reports, with missing values and sentinels injected.

Nothing here requires a physical model beyond the magnitude-frequency law itself,
which is why it is a good pandas case study: the difficulty is entirely in the
bookkeeping, and every bookkeeping decision changes the answer.

## 2. Magnitude-frequency and the Gutenberg-Richter relation

The empirical law, in cumulative form, is

$$N(\ge M) = a\,10^{-bM}, \qquad \log_{10} N(\ge M) = a - bM , \tag{1}$$

where $N(\ge M)$ is the number of events with magnitude at least $M$. The slope
$b$ is the **b-value**, and its meaning is a ratio: increasing $M$ by one unit
divides the rate by $10^{b}$. The usual geophysical range is roughly
$0.7 \lesssim b \lesssim 1.3$, with the vicinity of 1.0 the most common; this is
the one sentence in the lesson that belongs to real seismology, and it is a
statement about published catalogues, not about the synthetic table.

The differential (non-cumulative) form follows from equation (1): the number in a
unit magnitude interval is proportional to $10^{-bM}$ up to a factor of
$b\ln 10$. That factor is why the cumulative form is preferred for fitting — it
needs no bin-width correction — and why the modal bin of a histogram and the
cumulative fit do not sit on top of each other.

Three things the law is **not**. It is not a statement that earthquakes are
random in time; it is not valid below the completeness magnitude; and it does not
fit the largest events in a small sample, where a few events scatter around the
line and a least-squares fit is dominated by the poor counting statistics at low
$N$. All three caveats shape the rest of the lesson.

## 3. Completeness: the assumption that dominates

Below some magnitude $M_c$, a network does not detect or locate every event, so
the observed rate is a fraction of the true rate and the slope steepens. Any fit
that includes those events is fitting the detection curve, not the earthquake
population. Choosing $M_c$ is therefore the most consequential decision in the
whole computation, and it is a *choice* — informed by methodology, but never
measured exactly.

Two cheap diagnostics, neither of which settles the question:

- **The modal bin** of the differential histogram, used by the *maximum
  curvature* method. On the synthetic catalogue the modal bin is
  $[2.2, 2.3)$, which would suggest $M_c \approx 2.2$. The method is known to
  underestimate $M_c$, so it is reported as a diagnostic, never adopted as the
  answer.
- **The shape of the cumulative curve.** A straight line in
  $\log_{10} N$ against $M$ is the sign that the completeness range has been
  reached; a concave-upward bend at the low end is where the misfit lives.

The demonstration below proceeds with a *stated* $M_c = 3.0$ and then measures
how much the answer moves when it is changed. That measurement, not the point
estimate, is the scientific content of the section.

## 4. Building the relation with pandas

Nothing here needs a loop.

```python
import numpy as np, pandas as pd
import synthetic_catalog as sc

clean = sc.clean_catalog()
mags = clean["mw"]

# differential histogram: one pd.cut plus one value_counts
edges = np.arange(sc.M_MIN, 5.0 + 0.1, 0.1)
counts = pd.cut(mags, bins=edges, right=False).value_counts().sort_index()

# cumulative counts: a mask per grid magnitude
grid = np.round(np.arange(2.0, mags.max() + 0.05, 0.5), 2)
cumulative = pd.DataFrame({
    "mc_geq": grid,
    "n_geq": [int((mags >= g).sum()) for g in grid],
}).assign(log10_n=lambda d: np.log10(d["n_geq"]))
```

Two points about the code:

- `right=False` makes the bins half-open `[lo, hi)`, which matters because a
  magnitude of exactly 3.0 must belong to one bin and not two. Without it, a
  magnitude on a bin edge is counted in the bin below and the histogram sums to
  more than the number of events.
- The cumulative count uses a mask per grid point rather than a running total.
  It is $O(n \cdot k)$ for $n$ events and $k$ grid points, which is trivially
  fast at catalogue sizes, and it cannot accumulate the off-by-one errors a manual
  running sum invites. At $10^8$ events you would cumulate a sorted array
  instead; at $10^3$–$10^6$ this is the clearer expression.

The measured cumulative table for the synthetic catalogue:

| `mc_geq` | `n_geq` | `log10_n` |
|---|---|---|
| 2.0 | 391 | 2.592177 |
| 2.5 | 148 | 2.170262 |
| 3.0 | 48 | 1.681241 |
| 3.5 | 16 | 1.204120 |
| 4.0 | 2 | 0.301030 |

The fall from 391 to 2 across two magnitude units is the relation itself. If the
catalogue were complete at M 2.0 with $b = 1.05$, the expected ratios would be
about 11 per magnitude unit; the observed ratios are 8.1 over 2.0 to 3.0 and 24
over 3.0 to 4.0. The first is a little low and the second is high because only
two events sit above M 4.0 — counting noise at the far tail, not a change in
physics.

## 5. Two estimators, and why they disagree

**Maximum likelihood (Aki-Utsu).** For magnitudes above a known completeness
threshold and rounded to bin width $\Delta M$,

$$b = \frac{\log_{10} e}{\bar{M} - \left(M_c - \frac{\Delta M}{2}\right)} , \tag{2}$$

where $\bar{M}$ is the mean of the magnitudes at or above $M_c$. The
$\Delta M/2$ term corrects for the binning: a magnitude reported as 3.0 is
somewhere in $[2.95, 3.05)$, and using the bin centre keeps the estimator
unbiased.

**Least squares on the cumulative curve.** Fit a straight line to
$\log_{10} N(\ge M)$ against $M$ for $M \ge M_c$ and take the slope's negative.
This is the intuitive route, and it is the one that gets used when people fit by
hand in a spreadsheet.

On the synthetic catalogue with $M_c = 3.0$ and 48 events used:

| Estimator | b |
|---|---|
| maximum likelihood (Aki-Utsu) | 1.1581 |
| least squares on $\log_{10} N(\ge M)$ | 1.5033 |
| difference | 0.3452 |

They differ by 0.35 — far more than either estimator's formal error. This is not
a bug in either. The two answer different questions:

- The likelihood weights **each event equally**, which is the statistically
  efficient thing to do and is why it is the standard estimator.
- Least squares weights **each magnitude level equally**, and the levels are
  equally spaced while their counts are not; the high-magnitude levels with one
  or two events therefore carry the same influence as the low-magnitude level
  with 48. The tail, where counting noise is worst, is over-weighted, and the
  fitted line is dragged towards the steep tail.

The lesson is not "use MLE". It is that *which estimator you used must be
reported*, because another reader choosing the other one will get a substantially
different number from the same catalogue.

## 6. The uncertainty that matters

The formal standard error of the maximum-likelihood estimator is approximately

$$\sigma_b \approx \frac{b}{\sqrt{N}} , \tag{3}$$

which for $b = 1.1581$ and $N = 48$ is 0.1672. That is the number most often
quoted after a b-value. The demo then measures a different number, by re-estimating
$b$ at five completeness thresholds:

| $M_c$ | events used | b (MLE) | $\sigma_b$ |
|---|---|---|---|
| 2.5 | 148 | 1.0186 | 0.0837 |
| 2.8 | 75 | 1.0875 | 0.1256 |
| 3.0 | 48 | 1.1581 | 0.1672 |
| 3.2 | 30 | 1.2528 | 0.2287 |
| 3.5 | 16 | 2.0437 | 0.5109 |

The range of b across that span is **1.0251**, six times the formal error at a
fixed $M_c$. So the honest error bar is not $\pm 0.17$; it is "somewhere between
1.0 and 2.0 depending on where you believe the catalogue is complete", unless
$M_c$ is established independently, for example by comparing catalogues or by
network detection modelling.

Note also the estimates near the generator's true completeness: at
$M_c = 2.5$ the MLE gives 1.0186 and at 2.8 it gives 1.0875, bracketing the
generator's input 1.05. That agreement is the software check — the code does what
it claims on data whose answer is known. **It is not evidence about any real
region, and the 2.04 at $M_c = 3.5$ shows how easily a plausible-looking number
can be produced by a defensible-looking choice.** Declining to report a b-value
from data that cannot constrain it is the correct professional outcome, and it is
the outcome this section is designed to make you comfortable reaching.

## 7. What a CSV round trip does and does not carry

Catalogues are exchanged as CSV, so the round trip is part of the workflow:

```python
import io
buf = io.StringIO()
tidy.to_csv(buf, index=False)
back = pd.read_csv(io.StringIO(buf.getvalue()), parse_dates=["origin_time"])
```

Two properties to remember. First, a CSV carries values and column names but no
dtypes — the round trip is faithful only because `parse_dates` was supplied, and
without it `origin_time` returns as text and every later date operation breaks.
Second, a CSV is an interchange format and not a storage format: it has no notion
of a categorical dtype, no compression, and no schema, so a column of Python
objects serialises as their `repr`. Use it to move data between tools; do not use
it as the archive.

## 8. Worked code: the whole pipeline

```python
import numpy as np, pandas as pd, io
import synthetic_catalog as sc

# 1. clean, reporting the row counts (lesson 03's policy)
raw, clean = sc.raw_catalog(), sc.clean_catalog()
print(len(raw), "->", len(clean))                 # 408 -> 391

# 2. bin and cumulate
mags = clean["mw"]
edges = np.arange(sc.M_MIN, 5.0 + 0.1, 0.1)
hist = pd.cut(mags, bins=edges, right=False).value_counts().sort_index()

# 3. estimate b two ways at a stated Mc
mc, dm = 3.0, 0.1
m = mags[mags >= mc]
b_mle = np.log10(np.e) / (m.mean() - (mc - dm / 2))
grid = np.round(np.arange(mc, mags.max() + 0.05, 0.1), 2)
n_geq = np.array([int((mags >= g).sum()) for g in grid], float)
keep = n_geq > 0
b_ls = -np.polyfit(grid[keep], np.log10(n_geq[keep]), 1)[0]

# 4. report the sensitivity, not just the point estimate
sensitivity = {mc_i: b_aki_utsu(mags, mc_i) for mc_i in (2.5, 2.8, 3.0, 3.2, 3.5)}
```

`b_aki_utsu` is the two-line function defined in the demo module
([`code/earthquake_catalog_demo.py`](./code/earthquake_catalog_demo.py)); it is
equation (2) with `dm = 0.1`.

The order matters and is the point of the lesson: clean, then choose completeness,
then estimate, then **quantify the sensitivity of the estimate to the choice**.

## 9. Physical interpretation

For a real catalogue, a b-value near 1.0 is a robust observation about the size
distribution of brittle failure across a huge range of scales, and deviations
from it are interesting: they correlate with stress state, with faulting style,
with the depth range sampled, and with the incompleteness of the catalogue
itself. That is why the completeness choice matters so much — a b-value that has
absorbed a detection artefact looks exactly like a b-value that has absorbed a
physical difference.

**None of that applies to the numbers in this lesson.** The synthetic catalogue's
b-value is 1.05 *by construction*. If you find yourself writing "the b-value of
1.16 indicates...", stop: it indicates that the estimator and its assumptions
were applied to data generated with b = 1.05. The transferable content is the
pipeline and the reporting discipline.

The pipeline itself transfers, and the reporting discipline is usually the part
missing in published work: an estimator named, a completeness assumption stated
and justified, a sample size quoted, and a sensitivity range shown. A reader who
has those four things can judge the number. A reader given only "b = 1.16" cannot.

## 10. Assumptions and limits

- **Completeness is assumed, not derived, in this lesson.** Maximum curvature is
  used only as a diagnostic and it underestimates.
- **The catalogue is a sample.** 391 events is small; the formal error at
  $M_c = 3.0$ is 0.17 and the tail is dominated by two events. Any statement about
  the tail from this sample would be a statement about those two events.
- **Independence is assumed.** Earthquakes cluster in aftershock sequences;
  a declustering step is standard practice before estimating a b-value, and it
  is absent here because the synthetic events are independent by construction.
  On a real catalogue its absence is a defect.
- **The magnitude scale is assumed homogeneous.** Mixing `Mw`, `mb` and `ML`
  without conversion biases the estimate; lesson [03](./03-cleaning-data.md)'s
  `mag_type` column exists to make that visible.
- **Depth is not used.** The relation is one-dimensional in magnitude; any depth
  dependence would need to be tested by conditioning, which is a group-by and a
  decision about bin sizes.
- **The least-squares fit is not weighted.** A weighted fit with Poisson errors
  would be better and would not change the lesson's point that the estimator
  choice must be reported.
- **A CSV round trip is not a schema.** `parse_dates` is a manual repair of a
  lossy format.

## 11. Python demonstration

```
.venv/bin/python 03-scientific-computing/04-pandas/code/earthquake_catalog_demo.py
```

The demo prints the synthetic-data disclaimer above every result. Cleaning
reports 408 → 391 rows with the row-level reasons summing to 18 against 17 rows
removed, because one duplicate report also had a missing magnitude.

**The histogram** (excerpt) falls from 46 events in `[2.0, 2.1)` through 93 in
the modal bin `[2.2, 2.3)` to 1 in `[3.9, 4.0)`. The demo prints the implied
slope from two decades:

```
  N(M>=2.0)/N(M>=3.0) = 391/48 = 8.1   -> implied b ~ 0.91
  N(M>=3.0)/N(M>=4.0) = 48/2 = 24.0   -> implied b ~ 1.38
```

8.1 and 24.0 bracket the generated 1.05 ratio (about 11 per unit) as expected:
the first ratio is depressed by the incompleteness below the effective threshold,
the second is inflated by having only two events in the upper decade. **Both are
displays of counting statistics, not of the Earth's seismicity.**

**The two estimators:**

```
  (a) maximum likelihood (Aki-Utsu, 0.1 binning) : b = 1.1581
  (b) least squares on log10 N(>=M)              : b = 1.5033
      difference                                 : 0.3452
  Approximate standard error of the MLE, b/sqrt(N): 0.1672  (N = 48)
```

**The sensitivity table** of Section 6, with a range of 1.0251 against a formal
error of 0.1672, and the demo's own conclusion printed: the completeness choice
"moves the answer by far more than the formal error at a fixed Mc".

**Rate and energy.** Yearly counts from 34 to 49 events (mean 39.1 per year), and
regional totals with Northvale's 4.3 event dominating its energy column. The
largest synthetic event is **M 4.3 on 2011-08-14 in Northvale** — a property of
the generator's seed, quoted here only so you can confirm the demo ran.

**The CSV round trip** prints the first lines written, recovers five rows, and
reports `origin_time` as `datetime64[ns]` *because* `parse_dates` was supplied.

## 12. Common mistakes

1. **Fitting below the completeness magnitude.** The steepened low end then
   dominates the slope, and the fit describes detection.
2. **Quoting a b-value without the estimator.** 1.16 and 1.50 came from the same
   catalogue.
3. **Quoting a b-value without $M_c$.** The same catalogue gives 1.02 to 2.04.
4. **Quoting the formal error as if it were the uncertainty.** Section 6: the
   completeness range is six times larger.
5. **Mixing magnitude scales.** `Mw`, `mb` and `ML` are not interchangeable;
   filter on `mag_type` and say so.
6. **Not declustering.** Aftershocks violate independence and inflate the count
   at the low end of the range.
7. **Bin-edge double counting.** Use `right=False` (and check the histogram sums
   to the number of events).
8. **Reading the tail.** Two events above M 4.0 cannot support a statement about
   M 5 statistics.
9. **Trusting the CSV round trip without `parse_dates`.** Silent `str` dates.
10. **Presenting a synthetic b-value as a result.** The disclaimer at the top of
    this lesson exists because that mistake is easy and embarrassing.

## 13. Real-world applications

- **Probabilistic seismic hazard.** Recurrence models per source zone are
  magnitude-frequency fits; the completeness handling is a documented part of the
  hazard model.
- **Induced seismicity.** Regulatory frameworks compare b-values before, during
  and after injection; the estimator and completeness choices are contested
  precisely because the numbers are used for decisions.
- **Global seismicity statistics.** Comparing b-values between subduction and
  ridge environments requires per-region completeness maps, which makes this
  lesson's Section 6 a prerequisite rather than a caveat.
- **Aftershock forecasting.** Omori-Utsu and Gutenberg-Richter parameters are
  estimated from a declustered catalogue and combined into the forecast; both
  fits inherit the cleaning decisions of lesson [03](./03-cleaning-data.md).
- **Detection-network design.** The magnitude of completeness is the quantity a
  network upgrade is designed to lower, and it is estimated by exactly the kind
  of per-region, per-year aggregation used here.

## 14. Further reading

- The standard observational literature on magnitude-frequency statistics and on
  maximum-likelihood estimation of b-values (Aki 1965; Utsu 1965; and the modern
  treatments of the completeness problem) — read it before applying this
  pipeline to a real catalogue, because every assumption in Section 10 is
  discussed there in far more depth than a computing lesson can carry.
- [USGS Earthquake Hazards Program](https://earthquake.usgs.gov) and its
  [FDSN event web service](https://earthquake.usgs.gov/fdsnws/event/1/) — a real
  catalogue, downloadable with the quality flags this synthetic one imitates.
- [International Seismological Centre](https://www.isc.ac.uk) — the composite
  global bulletin, whose duplicate reports are the real-world version of this
  lesson's Section 2.

## 15. Related lessons

- Previous: [05 Merging, Joining and Aligning Irregular Time Series](./05-merging-time-series.md).
- Next: [07 Performance, dtypes and When to Leave Pandas](./07-performance-pandas.md).
- [03-04-03 Cleaning: Missing Values, Duplicates and Outliers](./03-cleaning-data.md)
  — the policy this lesson applies.
- [21-statistics-bayesian-ml](../../21-statistics-bayesian-ml) — maximum
  likelihood, uncertainty and model selection, in depth.

## Exercises

[`exercises/06-earthquake-catalog-pandas-exercises.md`](./exercises/06-earthquake-catalog-pandas-exercises.md),
with full worked answers in
[`exercises/06-earthquake-catalog-pandas-solutions.md`](./exercises/06-earthquake-catalog-pandas-solutions.md).

## Self-assessment checklist

- [ ] I can write the cumulative Gutenberg-Richter relation and say what the
      slope is.
- [ ] I can build a histogram with `pd.cut` and check that it sums to the number
      of events.
- [ ] I can compute both b-estimators and explain the difference between them.
- [ ] I can demonstrate the sensitivity of b to the completeness choice instead
      of asserting it.
- [ ] I can state the four things every reported b-value needs: estimator,
      completeness, sample size, sensitivity.
- [ ] I can say out loud what the b-value of a *synthetic* catalogue means, and
      it is "nothing about the Earth".
- [ ] I know why `parse_dates` is required after a CSV round trip.
