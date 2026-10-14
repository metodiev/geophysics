# Exercises — 03-04-06 Case Study: Earthquake Catalogue Wrangling

Attempt these **closed-book** before opening the
[solutions](./06-earthquake-catalog-pandas-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

> **The catalogue is SYNTHETIC.** It is generated in-code
> ([`../code/synthetic_catalog.py`](../code/synthetic_catalog.py)) from a
> Gutenberg-Richter model with input b-value **1.05** and completeness at
> **M 2.0**. It is not the USGS catalogue and not an observation of the Earth.
> Any b-value computed in these exercises is an illustration of the calculation
> and a check of the code — **never a geophysical result**. Several answers below
> require you to say exactly that.

Problems that say "run the demo" refer to
[`../code/earthquake_catalog_demo.py`](../code/earthquake_catalog_demo.py).

Useful constants from the demo: the cleaned catalogue has 391 events, and the
cumulative counts are

| `M >=` | 2.0 | 2.5 | 3.0 | 3.5 | 4.0 |
|---|---|---|---|---|---|
| `N` | 391 | 148 | 48 | 16 | 2 |

---

## ★ Foundational

**★1.** Write the cumulative Gutenberg-Richter relation and

(a) state which symbol is the b-value;
(b) compute `log10 N` for `N = 391`, `N = 48` and `N = 2`;
(c) explain what "the rate falls by a factor of `10^b` per unit magnitude"
means in words.

---

**★2.** The Aki-Utsu maximum-likelihood estimator, for magnitude bin width
`ΔM = 0.1` and completeness `Mc = 3.0`, is

$$b = \frac{\log_{10} e}{\bar M - (M_c - \Delta M/2)} .$$

(a) Compute the denominator for `Mc = 3.0`, `ΔM = 0.1`.
(b) Given the demo's answer `b = 1.1581`, work backwards to `M̄`, the mean of the
48 magnitudes at or above M 3.0.
(c) Why is the `ΔM/2` term present?

---

**★3.** Using the cumulative table:

(a) Compute the two-point slope of `log10 N` against `M` between M 2.0 and
M 3.0, and the implied `b`.
(b) Do the same between M 3.0 and M 4.0.
(c) Explain why one decade is not an estimate of `b`.

---

**★4.** In two or three sentences each:

(a) What is the magnitude of completeness, and why does a fit that includes
events below it describe detection rather than seismicity?
(b) Why is the choice of `Mc` more consequential than the choice of estimator?

---

## ★★ Applied

**★★5.** Using the cumulative table and `Mc = 3.0`:

(a) Fit a least-squares line to `log10 N` against `M` at `M = 3.0` and `M = 3.5`
only, and report the slope's negative as `b`.
(b) Compare it with the demo's full least-squares value of `1.5033` and explain
the difference in terms of which levels are included.
(c) Compute the MLE `b` at `Mc = 3.5` from the demo's sensitivity table and
explain why it is so much larger than the value at `Mc = 2.5`.

---

**★★6.** The formal standard error of the MLE is approximately `σ_b = b/√N`.

(a) Compute `σ_b` at `Mc = 3.0` (`b = 1.1581`, `N = 48`) and at `Mc = 2.5`
(`b = 1.0186`, `N = 148`).
(b) Which is smaller, and why does that not mean the `Mc = 2.5` answer is more
trustworthy?
(c) Report the demo's range of `b` across `Mc = 2.5 … 3.5` and compute its ratio
to the formal error at `Mc = 3.0`.

---

**★★7.** The demo reports `b = 1.1581` by maximum likelihood and `b = 1.5033` by
least squares.

(a) Explain, in terms of weighting, why the two differ.
(b) Which level of the cumulative curve dominates each fit?
(c) Write the sentence you would put in a methods section if you used the
least-squares value.

---

**★★8.** The demo ends with an in-memory CSV round trip.

(a) Which column required `parse_dates`, and why?
(b) What does a CSV not preserve that a pandas DataFrame does?
(c) State one consequence for a pipeline that saves intermediate results as CSV.

---

## ★★★ Research-oriented

**★★★9.** You are handed a real catalogue of 200,000 events and asked to
estimate a b-value with a defensible uncertainty.

(a) Describe the procedure you would use to establish `Mc`, naming at least two
methods and saying what each assumes.
(b) State two independent checks that the catalogue is complete above your
chosen `Mc`.
(c) State why you would decluster, and what declustering changes about the
reported rate.
(d) List the four things your reported b-value would include.

---

**★★★10.** A colleague hands you a regional catalogue with twelve events above
M 3.0 and the largest at M 4.2, and asks for the b-value.

(a) Compute the formal standard error for `b ≈ 1.0` and `N = 12`.
(b) State one additional check that twelve events cannot support, and why it
matters for the validity of the estimate.
(c) Write the paragraph you would return, including what you decline to state.
(d) Explain why "no b-value is reported because the catalogue cannot constrain
one" is a stronger scientific output than a number with a large error bar.
