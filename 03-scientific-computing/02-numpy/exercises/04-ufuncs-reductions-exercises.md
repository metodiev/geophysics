# Exercises — 03-02-04 Universal Functions, Reductions and Axis Semantics

Attempt these **closed-book** before opening the
[solutions](./04-ufuncs-reductions-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/ufuncs_reductions_demo.py`](../code/ufuncs_reductions_demo.py) require
you to run it and report its actual output:

```
.venv/bin/python 03-scientific-computing/02-numpy/code/ufuncs_reductions_demo.py
```

Every axis question must be answered with the **result shape** and the **physical
meaning** of the surviving axes.

---

## ★ Foundational

**★1.** For an array of shape `(8, 10, 12)` standing for
`(depth, north, east)`, give the result shape and the meaning of each element for:

(a) `.sum(axis=0)`
(b) `.mean(axis=2)`
(c) `.max(axis=(1, 2))`
(d) `.mean(axis=(0, 2))`
(e) `.sum()` and `.sum(axis=(0, 1, 2))` — how do the two differ?

---

**★2.** A gravity map `g` of shape `(north, east)` and coordinate vectors
`north`, `east`.

(a) Write the expression for the profile averaged over north.
(b) Write the assertion that proves the result matches the coordinate vector it
belongs to.
(c) Explain what goes wrong if the two coordinates happen to have the same length.

---

**★3.** For `a = np.array([[1.0, 2.0, np.nan], [4.0, np.nan, 6.0]])`, give the
value of each:

(a) `np.sum(a)`
(b) `np.nansum(a)`
(c) `np.nanmean(a)`
(d) `np.isnan(a).sum(axis=1)`
(e) State the danger of using `np.nansum` on a slice that is entirely `nan`.

---

**★4.** Write, in one line each:

(a) The depth profile of a `(depth, north, east)` cube averaged over the map.
(b) The cumulative depth profile of (a).
(c) The depth index of the maximum of (a).
(d) The physical depth of that maximum, given `z0 = 0.0` m and `dz = 25.0` m.

---

## ★★ Applied

**★★5.** Run the demo. Report, quoting its output:

(a) The seven `cube.sum(axis=...)` shapes.
(b) The two `mean` vectors and their shapes, and the `ValueError` raised when they
are compared.
(c) The four `nan`-aware results and the two propagating ones.
(d) The flat `argmax`, the `unravel_index` triple, and the check
`cube[4, 6, 8]`.
(e) The timing for `np.sum` and the Python loop at $n = 4 \times 10^6$, and the
statement of agreement between them.

---

**★★6.** A seismogram has 40 000 samples at 100 Hz.

(a) Compute the sample index and time of the maximum amplitude using `argmax`.
(b) The trace is windowed into consecutive 0.5 s windows. Compute the number of
windows and write the reshape-plus-reduction that gives the mean amplitude per
window.
(c) State what happens to the last window if the length is not a multiple of the
window size, and give the two standard treatments.
(d) Explain why `np.add.reduceat` is preferable to the reshape when the windows
have unequal lengths.

---

**★★7.** A `(nsample, nchannel)` array `x` holds 1 000 000 samples from 24
channels.

(a) Compute the shape, and the mean of each channel, and state the axis.
(b) Compute the *global* mean in two ways — as a mean over both axes and as a
weighted mean of the channel means — and state when the two differ.
(c) Compute the variance per channel using `ddof=0` and `ddof=1`, and give the
relative difference for $N = 1\,000\,000$.
(d) Write the check that the mean over both axes is the average of the channel
means for equal-length channels, and state why it would fail for unequal lengths.

---

## ★★★ Research-oriented

**★★★8.** The reduction of a trace over a time axis is a sum, but the *physical*
quantity is usually an integral. Derive the relation
$\int x(t)\,\mathrm{d}t \approx \Delta t \sum_k x_k$ (rectangle rule), state its
error term in terms of $\Delta t$ and the second derivative, and give the
corresponding trapezoid rule. Then:

(a) Explain the units of `np.sum(x)` against the units of the integral.
(b) Compute the relative error of the rectangle rule for a sinusoid of period
$T$ sampled at $N$ points per period, to leading order in $1/N$.
(c) State which rule NumPy's `np.trapezoid` implements and why it is the default
for irregularly sampled data only if it is given the coordinate vector.

---

**★★★9.** A colleague reports that "`np.nanmean` fixed the NaNs". Interrogate that
claim:

(a) Give the two distinct meanings of a `nan` in a field dataset and say which
one `nanmean` is appropriate for.
(b) Design a diagnostic that reports, for every reduction, the number of valid
values that entered it.
(c) State what `np.nanmean` returns for an all-`nan` slice and why that is a silent
failure.
(d) Give the array-level fix that makes the number of valid values part of the
returned result rather than an afterthought.
