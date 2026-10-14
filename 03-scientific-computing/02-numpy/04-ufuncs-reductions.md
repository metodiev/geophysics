---
id: 03-02-04
title: "Universal Functions, Reductions and Axis Semantics"
level: intermediate
prereqs: ["03-02-03"]
estimated_minutes: 75
tags: [numpy, ufunc, reduction, axis, nan]
---

# Universal Functions, Reductions and Axis Semantics

A **ufunc** (universal function) is a NumPy function that operates
element-by-element with broadcasting, is implemented in compiled code, and has
four methods — `reduce`, `accumulate`, `reduceat`, `outer` — that turn it into a
reduction. Almost every arithmetic operator is a ufunc: `np.add`, `np.multiply`,
`np.sqrt`, `np.maximum`. Almost every statistical summary is a *reduction* over
one of them: `np.sum` is `np.add.reduce`, `np.max` is `np.maximum.reduce`.

The reason this lesson is long is the `axis` argument. `axis=k` means "remove
axis $k$", and the result keeps every other axis in order. Getting it wrong
produces a plausible number of the right magnitude, because a mean of a gravity
grid over stations is still a gravity value in mGal. The demonstration in §2
prints two such answers, both about 1000, one of which is the mean over north
stations and one the mean over east stations. There is no exception, no warning,
and no visual clue. Only an assertion against the coordinate array catches it,
and that is what this lesson trains.

## Learning objectives

By the end of this lesson you will be able to:

1. **State** what `axis=k` removes, and **write down** the result shape of a
   reduction over any axis or tuple of axes of a 3-D array without running the
   code.
2. **Reproduce** the classic axis mix-up on an `(north, east)` grid and
   **explain** why the wrong answer is numerically plausible.
3. **Guard** a reduction with a shape assertion against the coordinate array it
   must match.
4. **Use** `keepdims=True` to make a reduction broadcast back onto its input.
5. **Distinguish** reductions that propagate `nan` from the `nan`-aware variants,
   and **choose** correctly.
6. **Use** cumulative and locating reductions (`cumsum`, `argmax`,
   `unravel_index`, `percentile`) and convert a flat index back to physical
   indices.
7. **Recognise** that `np.add.reduce` *is* `np.sum`, and use the ufunc-method
   forms `reduce`, `accumulate` and `outer` where they are the natural tool.
8. **Justify** the replacement of a Python loop by a reduction in terms of
   operation counts, not only in terms of a timing.

## Prerequisites

- [03 Broadcasting Rules and Vectorised Thinking](./03-broadcasting.md) — the
  shape rules that `keepdims` exists to satisfy.
- [03-01-03 Conditionals, Loops and Loop-Invariant Reasoning](../01-python-fundamentals/03-control-flow.md)
  — the loop that a reduction replaces.

## 1. What `axis` means

The rule is short. For an array of shape `(s0, s1, ..., sn)`:

- `axis=k` collapses axis $k$ and keeps the rest, in their original relative
  order.
- `axis=(k, l)` collapses both at once.
- With no `axis`, everything is collapsed and the result is a scalar (a 0-d
  array, to be exact).

The demo's cube has shape `(8, 10, 12)` — depth, north, east — and gives

```
  cube.sum(axis=0        ) -> shape (10, 12)     sum = 118680.0000
  cube.sum(axis=1        ) -> shape (8, 12)      sum = 118680.0000
  cube.sum(axis=2        ) -> shape (8, 10)      sum = 118680.0000
  cube.sum(axis=(0, 1)   ) -> shape (12,)        sum = 118680.0000
  cube.sum(axis=(0, 2)   ) -> shape (10,)        sum = 118680.0000
  cube.sum(axis=(1, 2)   ) -> shape (8,)         sum = 118680.0000
  cube.sum(axis=(0, 1, 2)) -> shape ()           sum = 118680.0000
```

Notice that every route ends at the same total 118 680. That is a property of
*summation* (the result is independent of the order of the collapsed axes), not a
property of reductions in general — `min`, `max` and `prod` share it, but a
reduction that is not commutative, or one whose intermediate values are rounded,
does not. As the demo notes, each intermediate result is not order-independent
even when the total is.

The check you should adopt when a reduction's output is supposed to align with a
coordinate array is an assertion:

```python
profile = gravity.mean(axis=1)
assert profile.shape == north.shape, (profile.shape, north.shape)
```

which the demo runs and reports as passing.

## 2. The mix-up, and why it survives

```
gravity = cube.sum(axis=0)            # (10, 12), the depth-collapsed map
mean over north stations (axis=0) -> shape (12,): [ 958.  960.  962.  964. 1014. 1016. 1018. 1020. 1022.  976.  978.  980.]
mean over east stations  (axis=1) -> shape (10,): [ 951.  955.  959. 1013. 1017. 1021. 1025.  979.  983.  987.]
```

Both vectors are around 1000, both are monotone over part of their range, and
both could plausibly be a profile of the synthetic anomaly. Only the shapes
distinguish them: `(12,)` matches the east axis and `(10,)` matches the north
axis. Comparing them directly raises

```
ValueError: operands could not be broadcast together with shapes (12,) (10,)
```

which is the *good* outcome — the two vectors cannot even be compared, so the
mistake becomes visible the moment anything downstream tries to use them
together. The dangerous case is a square grid, where both answers have the same
length and every downstream operation succeeds.

The reduction with the wrong axis is not a small error. It is a coherent
statement about a different quantity, computed correctly.

## 3. `keepdims`: reductions that broadcast back

Subtracting the map mean from the cube — the anomaly relative to the average
depth slice — requires the reduction to keep the collapsed axis:

```
cube.mean(axis=0).shape              = (10, 12)
cube.mean(axis=0, keepdims=True).shape = (1, 10, 12)
cube - kept.shape                    = (8, 10, 12)
anomaly.mean(axis=0).max()           = 0.000e+00
```

Without `keepdims`, `cube - plain` raises, because `(8, 10, 12)` and `(10, 12)`
align from the right as `12` vs `12` and `10` vs `10` and then `8` vs *missing*
— which is fine — actually that succeeds, broadcasting the `(10, 12)` map across
all 8 depth slices. That is exactly the danger: it succeeds and gives an anomaly
per (depth, north, east) cell. With `keepdims=True` the expression is explicit
about which axis was collapsed, and the intent is readable.

Two reasons to prefer `keepdims`:

- **Readability.** The shape of the result states which axis was reduced.
- **Correctness under broadcasting.** When the reduced array is combined with the
  original, the length-1 axis from `keepdims` cannot be aligned wrongly — the
  alignment is pinned.

## 4. `nan`, and the `nan`-aware reductions

A single missing value contaminates a reduction:

```
a = [[ 1.  2. nan]
     [ 4. nan  6.]]
np.sum(a)            = nan
np.mean(a)           = nan
np.nansum(a)         = 13.0
np.nanmean(a)        = 3.25
np.nanmax(a)         = 6.0
np.all(np.isnan(a).sum(axis=1) > 0) = True
np.isnan(a).any()    = True
```

The `nan`-aware variants skip missing values. The choice between them is a
statement about the data, not a matter of taste:

- **`np.nansum` is right when `nan` means "no measurement".** A station that was
  not occupied should not contribute zero to a sum; it should be ignored.
- **`np.sum` is right when you want to know that there is a hole.** If any `nan`
  appears, the answer should be `nan`, because the total is genuinely unknown.
  This is the safer default in a pipeline, and it is why `np.sum` is not
  `nan`-skipping.
- **`nan` is not a substitute for a mask.** `np.isnan(a).sum(axis=1)` gives the
  count of missing values per row, which is the diagnostic that tells you whether
  a `nanmean` is computed from 3 values or 3000. A `nanmean` over one value is
  meaningless and will not warn you.

The demo's suggestion `np.all(np.isnan(a).sum(axis=1) > 0)` returning `True` is
the check "every row has at least one missing value" — a summary you should
compute before deciding to skip.

## 5. Cumulative and locating reductions

Not every reduction collapses an axis to one number. `cumsum` keeps the shape and
replaces each element by the total up to that point:

```
depth profile (mean over the map) = [103.625 108.625 120.292 125.292 130.292 128.625 133.625 138.625]
cumulative sum                    = [103.625 212.25  332.542 457.833 588.125 716.75  850.375 989.   ]
np.trapezoid-free total (cum[-1]) = 989.000000   equals profile.sum(): True
```

The last element of the cumulative sum is the total; every earlier element is a
running total, which is what a cumulative heat-flow, cumulative mass or
cumulative moment curve needs.

The **locating** reductions return indices rather than values, and the index
space is the flattened array unless `axis` is given:

```
cube.ravel().shape = (960,)
argmax (flat index) = 560, value = 165.0000
unravel_index -> (depth, north, east) = (4, 6, 8)
cube[4, 6, 8] = 165.0   (same value)
np.argmax(cube, axis=0).shape = (10, 12)  -> the depth of the maximum at every map cell
np.percentile(depth_profile, [0, 50, 100]) = [103.625      126.95833333 138.625     ]
```

The pair `argmax` plus `unravel_index` is the standard way to locate a feature in
a model cube: find the maximum in the flattened array, then convert the flat
index into `(depth, north, east)`. The conversion requires the array's shape and
its coordinate origin and spacing; getting that wrong shifts the located feature
by a whole cell, which is a common error when the coordinates start at a
non-zero value.

The demo prints the total through `cum[-1]` and calls it "`np.trapezoid-free`" to
make a distinction that matters: a **sum** over samples is not an **integral**
over a coordinate. `depth_profile.sum()` is in mGal (a sum of values), while a
trapezoidal integral over depth would be in mGal·m. Confusing the two is a
dimensional error, and lesson
[06](./06-random-module.md) is where the units of synthetic quantities are
pinned down.

## 6. ufunc methods

Every ufunc exposes the reduction as a method, and knowing this explains why
some operations have no dedicated function:

```
np.add.reduce(a)      = 10.0
np.add.accumulate(a)  = [ 1.  3.  6. 10.]
np.add.outer(a, b) =
[[11. 21. 31.]
 [12. 22. 32.]
 [13. 23. 33.]
 [14. 24. 34.]]
np.maximum.reduce([a, np.array([2.5, 1.0, 5.0, 3.0])]) = [2.5 2.  5.  4. ]
np.multiply.reduce(a) = 24.0 (factorial 4!)
```

So `np.sum(x)` and `np.add.reduce(x)` are the same call; `np.maximum.reduce` is
the elementwise maximum across the first axis of a stacked array, which is the
tool for "maximum of these fields" when a dedicated `np.max` would reduce over an
axis instead of across arrays; and `np.multiply.reduce` is a product, which is
why there is no separate `np.prod`-as-ufunc. The fourth method, `reduceat`, is
the segment reduction used for contiguous blocks; it is the fast path behind
"mean of each contiguous trace" and appears in lesson
[08](./08-vectorisation-patterns.md).

## 7. The speed argument, stated as an operation count

The demo times a reduction against an explicit Python loop:

```
n = 4000000 elements
np.sum          : np.float64(7999998000000.0) in    0.443 ms
Python for-loop : 7999998000000.0 in  105.798 ms
ratio (loop/numpy) = 239.0x   (machine dependent)
both results agree exactly: True
```

Note first that the two results agree **exactly** — both are the exact integer
sum represented in `float64`, because $8 \times 10^{12}$ is exactly
representable. This is not a general property; for non-representable sums the
pairwise order of `np.sum` and the sequential order of the loop give slightly
different results, and neither is "the" answer.

The reproducible claim is the operation count, not the ratio: the loop performs
$4 \times 10^6$ interpreted iterations and $4 \times 10^6$ Python-level
additions, while `np.sum` performs the same additions in compiled, pairwise
code. Wall-clock ratios of this kind vary with CPU, cache, the loop's overhead
per iteration and the NumPy build; the two runs recorded for this module on the
same machine gave **239×** and **122×**, so treat any single ratio as an
observation of the moment, not as a property of `np.sum`.
**Quote the count, not the ratio** when you report a speed-up in a paper or a
log, and additionally report the machine when you quote a time.

## 8. Physical interpretation

A reduction is a statement about what an axis *is*. Summing a cube over depth
gives a map because the depth axis is the one along which contributions
accumulate; averaging a map over north stations gives an east profile because the
north axis is the one along which stations are replicates of the same physics.
The physics does not enter the arithmetic at all — which is exactly why the
choice of axis is a *modelling* decision that must be justified, not an
implementation detail.

The classical geophysical reductions:

- **Stacking** is a mean over the trace axis, and its variance falls as $1/N$ —
  the array-level statement of the signal-to-noise argument.
- **Depth integration** (a sum over layers weighted by thickness) is a
  reduction over the depth axis of a product of two arrays.
- **Spectral averaging** is a mean over frequency bands, and requires the band
  edges to be the reduction's segment boundaries.
- **Grid statistics** (mean gravity over a survey block) are a mean over both
  map axes, `axis=(0, 1)`.

## 9. Assumptions and regime of validity

- **`axis` counting starts at 0 and follows the memory layout, not the physics.**
  The mapping from "depth" to 0 is a convention of your code.
- **Reductions with `axis=None` return a 0-d array, not a Python scalar.** It
  behaves like a scalar in almost all contexts, but `type(np.sum(x))` is
  `np.float64`, and `isinstance(..., float)` is `True` for `np.float64` — but not
  for every NumPy scalar type. Cast with `float(...)` at API boundaries.
- **`np.sum` on integers promotes to the platform default integer** and can
  overflow for `int32` inputs; pass `dtype=np.int64`.
- **Float summation is not associative**, so `np.sum` (pairwise) and a loop
  (sequential) can differ in the last digits — and so can `np.sum` over an array
  and over its transpose.
- **`nan` propagates through `sum`, `mean`, `min`, `max`, `std`** but not through
  `argmax` or comparison, where it behaves as a large value in some environments;
  do not rely on `argmax` semantics in the presence of `nan` without testing.
- **`np.percentile` interpolates** by default (`method="linear"`), so a median
  can be a value not present in the data.
- **`np.nansum` of an all-`nan` slice is 0.0**, which is indistinguishable from a
  genuine zero. Guard with a count of valid values.
- **The ufunc `out=` parameter** writes into a preallocated array and is how a
  reduction is fused into a larger computation without temporaries; forgetting
  it is why vectorised code sometimes allocates more than the loop.

## 10. Python demonstration

The script is [`code/ufuncs_reductions_demo.py`](./code/ufuncs_reductions_demo.py):

```
.venv/bin/python 03-scientific-computing/02-numpy/code/ufuncs_reductions_demo.py
```

The cube is SYNTHETIC and deterministic: a linear trend in depth, north and east
plus a $40$-unit block of $3 \times 4 \times 5$ cells, built by arithmetic on the
index arrays. No random numbers and no data file are involved, so every value
printed below is reproducible exactly.

Key output (this machine, NumPy 2.5.4):

```
cube.shape = (8, 10, 12)  (depth, north, east)
  cube.sum(axis=0        ) -> shape (10, 12)     sum = 118680.0000
  ...
  cube.sum(axis=(0, 1, 2)) -> shape ()           sum = 118680.0000
```

```
mean over north stations (axis=0) -> shape (12,): [ 958.  960.  962.  964. 1014. 1016. 1018. 1020. 1022.  976.  978.  980.]
mean over east stations  (axis=1) -> shape (10,): [ 951.  955.  959. 1013. 1017. 1021. 1025.  979.  983.  987.]
the two answers have different shapes: (12,) vs (10,)
comparing them raises ValueError: operands could not be broadcast together with shapes (12,) (10,) 
first 10 entries of `correct` vs `wrong` are different: True
```

```
np.nansum(a)         = 13.0
np.nanmean(a)        = 3.25
```

```
argmax (flat index) = 560, value = 165.0000
unravel_index -> (depth, north, east) = (4, 6, 8)
cube[4, 6, 8] = 165.0   (same value)
```

```
np.sum          : np.float64(7999998000000.0) in    0.443 ms
Python for-loop : 7999998000000.0 in  105.798 ms
```

### What to observe

1. The grand total is the same by all seven routes, which is a property of
   summation and not a licence to be careless about the axis: the *intermediate*
   arrays differ in shape and meaning at every step.
2. The two means are both near 1000 mGal and both plausible; only the shapes tie
   them to the coordinates. This is the whole reason for the assertion in §1.
3. `np.nanmean` of the demo array is `3.25 = 13/4`: the four non-`nan` values
   averaged. Had one row contained the only valid values, the "mean" would still
   have been printed, with no indication of how many samples it used.
4. `unravel_index(560, (8, 10, 12))` giving `(4, 6, 8)` is worth checking by hand:
   $4 \cdot 120 + 6 \cdot 12 + 8 = 480 + 72 + 8 = 560$. That arithmetic is the C
   order of the array, and it is the same arithmetic as the strides.
5. Both sums agree exactly, and the 239× ratio is a machine- and load-dependent
   observation (a second run of the same script gave 122×); the counted work
   (4 million interpreted iterations) is not.

## 11. Common mistakes

1. **Using `axis=0` where the physics says "stations".** The axis number must be
   derived from the array's construction, not from habit.
2. **Averaging a map over the wrong axis** on a square grid, where nothing raises
   and the answer is plausible.
3. **Forgetting `keepdims`** when the reduction is subtracted from its input.
4. **Using `np.mean` on data with `nan`** and getting `nan` for the whole survey
   because one station failed.
5. **Using `np.nanmean` without counting the valid values** and reporting a mean
   over three samples with the confidence of one over three thousand.
6. **Summing integer arrays without specifying `dtype`** and overflowing.
7. **Confusing a sum with an integral.** `arr.sum()` has the units of the values;
   an integral over a coordinate carries the coordinate's unit too.
8. **Reading `argmax` on a flattened array and reporting the flat index as a
   coordinate.** Convert with `unravel_index`, then apply the origin and spacing.
9. **Quoting a timing ratio from one machine as if it were a property of NumPy.**
   Quote the operation count.

## 12. Real-world applications

- **Seismic stacking.** `gather.mean(axis=0)` stacks traces; the axis choice *is*
  the stacking geometry, and a wrong axis produces a section that looks like
  coherent noise.
- **Bouguer and terrain corrections.** The mean elevation and mean density over a
  gravity station's template are reductions over (radius, azimuth) of a polar
  grid; the axis order must match `meshgrid`'s.
- **Spectral estimation.** Welch's method is a mean over segment periods, plus a
  mean over the taper dimension; the `nanpoling` of missing samples is handled by
  the `nan`-aware mean.
- **Heat flow.** A borehole's total heat flow is a depth integral of conductivity
  times gradient — a reduction over depth of a product, with the sign convention
  of lesson 02-05-04 to respect.
- **Satellite gravity time series.** The monthly solution is reduced over
  latitude and longitude to a Stokes coefficient; the reduction axis order is
  defined by the product grid.
- **Machine learning.** Loss reduction over a batch is a mean over axis 0; the
  reduction must ignore padding, which is where `nan`-aware or masked reduction
  enters.

## 13. Further reading

- **NumPy documentation, "Universal functions (ufunc)" and "Reduction
  operations".** [https://numpy.org](https://numpy.org) — the normative list of
  methods (`reduce`, `accumulate`, `reduceat`, `outer`) and the `axis` parameter
  semantics. Level: beginner to intermediate.
- **NumPy documentation, `numpy.nansum`, `numpy.nanmean`, `numpy.argmax`,
  `numpy.unravel_index`.** [https://numpy.org](https://numpy.org) — the exact
  behaviour of the `nan`-aware and locating reductions used here. Level:
  beginner.
- **Higham, N. J. *Accuracy and Stability of Numerical Algorithms* (2nd ed.,
  SIAM, 2002).** The error analysis of summation, including the pairwise scheme
  NumPy uses, and why order-independence of *results* is not order-independence
  of *rounding*. Level: graduate.
- **Harris, C. R., et al. "Array programming with NumPy." *Nature* 585, 357–362
  (2020).** DOI 10.1038/s41586-020-2649-2. Level: intermediate.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 14. Related lessons

- [03 Broadcasting Rules and Vectorised Thinking](./03-broadcasting.md) — the
  shape rules that make `keepdims` necessary.
- [06 Random Number Generation and Reproducible Seeds](./06-random-module.md) —
  where the units and provenance of synthetic quantities are pinned down.
- [08 Replacing Loops: Vectorisation Patterns and Traps](./08-vectorisation-patterns.md)
  — the cases where a reduction is not the fastest tool.
- [21-statistics-bayesian-ml/…](../../21-statistics-bayesian-ml/README.md) — the
  inferential use of means and variances.
- [05-core-geophysics/09 Geothermal and Heat-Flow Methods](../../05-core-geophysics/09-geothermal-and-heat-flow-methods/README.md)
  — depth integrals with physical units.

Exercises:
[`exercises/04-ufuncs-reductions-exercises.md`](./exercises/04-ufuncs-reductions-exercises.md)
and
[`exercises/04-ufuncs-reductions-solutions.md`](./exercises/04-ufuncs-reductions-solutions.md).

## Self-assessment checklist

- [ ] I can write the result shape of any reduction of an `(8, 10, 12)` array
      without running it. (§1)
- [ ] I can state why the wrong-axis mean is dangerous rather than obviously
      wrong, and write the assertion that catches it. (§2)
- [ ] I can explain when to use `keepdims=True` and what breaks without it. (§3)
- [ ] I can choose between `np.sum` and `np.nansum` and justify the choice from
      the meaning of the missing value. (§4)
- [ ] I can convert a flat `argmax` index to `(depth, north, east)` by hand.
      (§5)
- [ ] I can name the four ufunc methods and give one use for each. (§6)
- [ ] I can state a speed-up as an operation count rather than a wall-clock
      ratio, and say why. (§7)
- [ ] I can give an example from my own work where a sum and an integral differ
      in units. (§8)
