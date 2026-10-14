# Solutions — 03-04-06 Case Study: Earthquake Catalogue Wrangling

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.
>
> **The catalogue is SYNTHETIC**: generated in-code with input b-value 1.05 and
> completeness at M 2.0. **No b-value below is a geophysical result.** Each is an
> illustration of the calculation and a check that the code recovers a known
> input on data whose answer is known by construction.

---

## ★1 — The relation

The cumulative form is

$$N(\ge M) = a\,10^{-bM}, \qquad \log_{10} N(\ge M) = a - bM .$$

**(a)** The b-value is the coefficient `b` in the exponent, equivalently the
negative of the slope of `log10 N` against `M`.

**(b)** `log10 391 = 2.592177`; `log10 48 = 1.681241`; `log10 2 = 0.301030`.

**(c)** Each one-unit increase in magnitude divides the number of events at or
above that magnitude by `10^b`. For `b ≈ 1` the count drops by a factor of ten
per magnitude unit: a catalogue with 10,000 events above M 3 has about 1,000 above
M 4 and about 100 above M 5.

---

## ★2 — The Aki-Utsu estimator inverted

**(a)** `Mc − ΔM/2 = 3.0 − 0.05 = 2.95`.

**(b)** From `b = log10(e)/(M̄ − 2.95)`, rearranging gives
`M̄ = 2.95 + log10(e)/b = 2.95 + 0.434294/1.1581 = 2.95 + 0.37500 = 3.325`. The
mean of the 48 magnitudes at or above M 3.0 is **3.325**, which the demo also
prints directly.

**(c)** Because magnitudes are **rounded** to 0.1 before they are recorded. A
magnitude reported as 3.0 lies somewhere in `[2.95, 3.05)`, so the expected value
of the recorded number is the bin centre minus a half-bin offset from the true
threshold. Subtracting `ΔM/2` from `Mc` moves the threshold to the *lower edge*
of the bin, which is what makes the estimator consistent rather than biased by
half a bin width.

---

## ★3 — One decade is not an estimate

**(a)** `(1.681241 − 2.592177)/(3.0 − 2.0) = −0.910936`, so the implied
`b ≈ 0.91`.

**(b)** `(0.301030 − 1.681241)/(4.0 − 3.0) = −1.380211`, so `b ≈ 1.38`.

**(c)** Because a two-point slope is a single ratio subject to counting noise at
both ends. The lower decade is depressed by incompleteness near the detection
threshold, and the upper decade contains only two events, so its `log10 N` has an
uncertainty of order `1/(√N ln 10) = 1/(1.41 × 2.30) ≈ 0.3` — comparable with the
0.48 difference being measured across that decade. A fit needs many magnitude levels, each with a stated count, and the
*scatter* of the levels around the line is the only honest indication of whether
the relation holds.

---

## ★4 — Completeness

**(a)** The magnitude of completeness `Mc` is the lowest magnitude at which the
network records essentially every event above it in space and time. Below it,
the recorded rate is the product of the true rate and a detection probability
that rises with magnitude, so the observed curve steepens — the fit then measures
where the instruments stopped seeing, not how the earthquakes were distributed.

**(b)** Because the estimator is a formula with one unknown (the slope) applied to
the subset you choose, whereas `Mc` determines *which events enter the formula*.
The demo measures the effect: the same catalogue yields `b` from **1.0186** at
`Mc = 2.5` to **2.0437** at `Mc = 3.5`, a range of 1.03 — six times the formal
error at a fixed `Mc`. No estimator choice moves the answer that far.

---

## ★5 — Least squares on part of the curve

**(a)** Through `M = 3.0` and `M = 3.5`:
`(1.204120 − 1.681241)/(3.5 − 3.0) = −0.954243`, so **`b ≈ 0.954`**.

**(b)** `0.954` against the demo's full-fit `1.5033` — the difference is entirely
which levels are included. The full fit uses every level from `M = 3.0` upward at
0.1 spacing, so it includes the sparse high-magnitude levels where `log10 N` is
1 or 0 and the straight-line assumption fails; those levels drag the fitted slope
steeper because the counts fall faster than the relation predicts as `N`
approaches single digits. Using only the well-populated lower levels gives a
value closer to the MLE.

**(c)** `b = 2.0437` at `Mc = 3.5`, with 16 events. Raising the threshold to 3.5
discards almost all the data that constrains the slope — 32 of the 48 events are
between M 3.0 and M 3.5 — and leaves a small, truncated sample in which the mean
magnitude is close to the threshold. The estimator's denominator
(`M̄ − 2.95`) then becomes small and unstable, and `b` inflates. This is not a
better estimate of anything; it is a demonstration that an estimator applied to a
sample that cannot constrain it will still return a number.

---

## ★6 — Formal error versus real uncertainty

**(a)** At `Mc = 3.0`: `1.1581/√48 = 1.1581/6.9282 = 0.1672`. At `Mc = 2.5`:
`1.0186/√148 = 1.0186/12.1655 = 0.0837`.

**(b)** The `Mc = 2.5` value is smaller because it uses three times as many
events, and `σ_b` shrinks as `1/√N`. It does not mean the answer is more
trustworthy, because the smaller formal error is *conditional on* a completeness
claim that is more questionable at M 2.5. Formally tighter and physically less
defensible is a common and dangerous combination — the error bar excludes exactly
the uncertainty that matters.

**(c)** The demo's range is **1.0251**. Against the formal error at `Mc = 3.0`
(0.1672) the ratio is `1.0251/0.1672 ≈ 6.1`. The choice of completeness moves the
answer by six formal errors.

---

## ★7 — Why the estimators disagree

**(a)** The likelihood weights **each event equally**: an event contributes 1/N
to `M̄` regardless of its magnitude. Least squares weights **each magnitude level
equally** in `log10 N`, and the levels are equally spaced in magnitude while their
counts differ by orders of magnitude. The high-magnitude levels, where counting
noise is largest, therefore carry the same influence as the level with 48 events.

**(b)** The least-squares fit is dominated by the **high-magnitude tail** (few
events, large `log10 N` changes, hence strong leverage on the slope). The
likelihood fit is dominated by the **bulk of the events**, just above `Mc`.

**(c)** A methods sentence that states everything a reader needs:

> "The b-value was estimated by least squares on the cumulative magnitude-
> frequency distribution above a magnitude of completeness of 3.0 (`N = 48`),
> giving `b = 1.50`. A maximum-likelihood estimate on the same subset gives
> 1.16; the difference reflects the stronger influence of the sparse high-
> magnitude levels on an unweighted least-squares fit."

Reporting the second estimator alongside the first is what makes the choice
auditable rather than hidden.

---

## ★8 — The CSV round trip

**(a)** `origin_time`. A CSV stores values as text, so a timestamp column returns
as a string unless the reader is told its type. `parse_dates=["origin_time"]`
performs the conversion at load, and without it every later `.dt` operation fails
or, worse, sorting is lexicographic rather than chronological.

**(b)** A CSV preserves values and column names but not **dtypes**. Categories,
nullable integers, timezones and compression are all lost; the file has no
schema, so a column of Python objects serialises as its `repr` and comes back as
text.

**(c)** Every intermediate result becomes a source of type drift, and each load
becomes a place where a wrong `parse_dates` list silently restores text where
numbers are expected. A pipeline that must round-trip through disk should use a
typed format (Parquet, or a database table) and keep CSV for exchange at the
boundaries only.

---

## ★9 — Establishing completeness for a real catalogue

**(a)** At least two of:

- **Maximum curvature** — the mode of the differential magnitude histogram. Fast,
  and known to **underestimate** `Mc`; it assumes the detection curve turns over
  sharply and that the true distribution is smooth near the mode.
- **Goodness-of-fit (the `b-value stability` method)** — increase the trial `Mc`
  and watch the estimated `b`; take the value above which `b` is stable. It
  assumes that completeness produces a change in slope and that above `Mc` the
  relation is linear.
- **Comparison with a denser network or a different catalogue** in the same
  region. It assumes the reference catalogue is more complete — reasonable for a
  sparse regional network checked against a local one, and circular otherwise.
- **Detection modelling** — estimate `Mc` from the network's magnitude-distance
  detection capability. It assumes the detection model is correct, and it is the
  only method that gives a spatially varying `Mc`.

**(b)** Two independent checks: the cumulative magnitude-frequency curve should be
**straight** above `Mc` (a concave-up bend at the low end means `Mc` is still too
low), and the **rate should be stable** when the region is subdivided in time
(the same `Mc` should apply to the first half and the second half of the record —
if the earlier period needs a higher `Mc`, the network changed and a single
threshold is wrong).

**(c)** Aftershocks are triggered by their mainshock and are not independent
events, so including them inflates the count of small events relative to large
ones and biases the estimated `b` (and every rate) high at the low-magnitude end.
Declustering replaces one mainshock-plus-aftershocks count with a single
independent event, so the reported **rate** is a rate of independent events — a
different, and usually the intended, quantity.

**(d)** The four things: the **estimator** (maximum likelihood, Aki-Utsu, with the
bin width), the **completeness threshold and how it was established**, the
**sample size** (`N` events in the fit), and the **sensitivity** to the
completeness choice. Without all four the number cannot be compared with any
other study.

---

## ★10 — Twelve events

**(a)** `σ_b = 1.0/√12 = 0.2887`. A b-value quoted as `1.0 ± 0.29` covers
`0.71` to `1.29` at one sigma, and the entire plausible geophysical range
(`0.7`–`1.3`) at two.

**(b)** Twelve events cannot support the **linearity check**. The whole method
assumes that `log10 N` is a straight line above `Mc`, and with only a handful of
magnitude levels — most holding one event — the scatter is larger than the slope.
Without that check there is no evidence that the estimate is a b-value rather
than the slope of a curve that is not a line, and no evidence that `Mc` was chosen
correctly at all. The estimate is unverifiable, not merely imprecise.

**(c)** A paragraph that declines cleanly:

> "The regional catalogue contains twelve events at or above M 3.0, with the
> largest at M 4.2. This sample cannot constrain a b-value: the formal standard
> error at `N = 12` is about 0.29, and the sample does not span enough magnitude
> levels above any candidate completeness threshold to test the linearity that
> the estimate assumes. I therefore do not report a b-value. What the data do
> support is a statement of the observed count above M 3.0 over the catalogue
> period, with its Poisson uncertainty, and the maximum observed magnitude as an
> observation rather than an extrapolation. A b-value from these data would
> require a longer record, a lower detection threshold, or a regional pooling of
> data."

**(d)** A number with a large error bar invites exactly two errors: quoting the
central value without the bar, and averaging it with better estimates as if it
carried information. An explicit refusal states what the data can support and what
would be needed — which is the useful output — and it places the responsibility
for the missing estimate on the data rather than on the analyst's choice of
method.
