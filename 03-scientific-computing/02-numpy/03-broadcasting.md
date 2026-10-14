---
id: 03-02-03
title: "Broadcasting Rules and Vectorised Thinking"
level: intermediate
prereqs: ["03-02-02"]
estimated_minutes: 75
tags: [numpy, broadcasting, vectorisation, distance-matrix]
---

# Broadcasting Rules and Vectorised Thinking

Broadcasting is the mechanism that lets NumPy combine arrays of *different*
shapes without writing a loop, by conceptually repeating an array along an axis
of length 1 until the shapes match. It is what makes `traces - mean[:, None]`
subtract one number per station from a whole station's worth of samples, and
what makes a distance matrix a single line of code.

It is also the source of the quietest class of bug in numerical Python, because
the *successful* cases are silent. `(12,) - (12, 500)` raises a `ValueError` and
tells you exactly what is wrong. `(12, 1) - (12, 500)` gives the answer you
wanted. And `(500,) - (500,)` gives a *scalar* when you may have meant an outer
product — no error, no warning, no clue. This lesson gives the rules, then the
patterns, then the sizes at which broadcasting stops being free.

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the broadcasting rules (align from the right; each axis pair must
   be equal or one of them must be 1; missing leading axes count as 1) and
   **apply** them to predict any result shape.
2. **Subtract** a per-station mean from a 2-D trace array using `mean[:, None]`,
   and explain why the naive `data - mean` raises and what its message says.
3. **Build** an $n \times n$ distance matrix in one expression, verify it against
   a double loop, and **compute** the memory it needs for $n = 2\,000$ and
   $n = 20\,000$.
4. **Use** the outer-product idiom `a[:, None] * b[None, :]` and recognise where
   `np.outer` is the clearer alternative.
5. **Compute** the size of the intermediate array a broadcast expression will
   allocate, *before* running it.
6. **Explain** why broadcasting removes the loop but not the $O(n^2)$ memory,
   and name the two remedies (tiling and spatial indexing).

## Prerequisites

- [02 Indexing, Slicing, Views vs Copies and Fancy Indexing](./02-indexing-slicing.md)
  — `None`/`newaxis` is an indexing operation and produces a view.
- [01-07-02 Matrices, Matrix Multiplication and Linear Maps](../../01-mathematics/07-linear-algebra/02-matrices-and-operations.md)
  — the outer product and matrix-vector product being broadcast here.

## 1. The rules

Broadcasting compares the shapes element-wise **from the trailing (rightmost)
axis backwards**. Two axes are compatible if they are equal or if one of them
has length 1. The result takes the larger length. Any axis present in one shape
but not the other counts as length 1. If any axis pair is incompatible, NumPy
raises `ValueError`.

The demo exercises six pairs:

```
  (3, 4)       + (4,)         : ok -> (3, 4)
  (3, 4)       + (3, 1)       : ok -> (3, 4)
  (3, 1)       + (1, 4)       : ok -> (3, 4)
  (5, 1, 3)    + (4, 1)       : ok -> (5, 4, 3)
  (2, 3, 4)    + (3, 1)       : ok -> (2, 3, 4)
  (2, 3, 4)    + (4, 3)       : ValueError: operands could not be broadcast together with shapes (2,3,4) (4,3)
```

Work through the fourth by hand. `(5, 1, 3)` and `(4, 1)` align from the right as
`(5, 1, 3)` and `(_, 4, 1)`; axis 2 is `3` against `1` → `3`; axis 1 is `1`
against `4` → `4`; axis 0 is `5` against missing → `5`. Result `(5, 4, 3)`. The
sixth fails because the trailing axes are `4` against `3`.

Note that broadcasting never *materialises* the repeated array. `data - mean[:,
None]` does not build a `(12, 500)` copy of `mean`; the subtraction reads the
single scalar belonging to the row. The demo states the accounting:

```
`mean[:, None]` costs 96 bytes; the broadcast result costs 48000 bytes.
```

The 48 000 bytes are the *output*, which is unavoidable. The input expansion is
free. That is the entire efficiency argument for broadcasting over
`np.tile`/`np.repeat`.

## 2. The canonical operation: remove a per-station offset

A real station-acquisition problem: each of 12 stations has a constant DC offset
(different instrument, different electrode contact), and you want the traces
without it. The synthetic version in the demo:

```python
rng = np.random.default_rng(SEED)
data = rng.normal(size=(12, 500))
data += np.linspace(-3.0, 3.0, 12)[:, None]     # station DC offsets
```

Output:

```
data.shape = (12, 500)  (station, sample)
station means (shape (12,)): [-3.0369 -2.5003 -1.9296 -1.3537 -0.7653 -0.3301  0.2858  0.8407  1.3514
  1.8734  2.4141  3.0302]
mean.shape = (12,) -> cannot broadcast directly against (12, 500)
ValueError: operands could not be broadcast together with shapes (12,500) (12,)
```

The error message is the fastest diagnostic in NumPy: it prints both shapes in
the order they were aligned. Here the trailing axes are `500` and `12`, which
disagree, and there is no axis of length 1 to stretch. The repair is to make the
station axis the *right* axis of a two-axis array:

```python
demeaned = data - mean[:, np.newaxis]        # (12, 1) against (12, 500)
```

Three spellings are equivalent and the demo verifies they agree exactly:
`mean[:, None]`, `mean.reshape(-1, 1)` and `np.expand_dims(mean, 1)`. The result

```
max |station mean after| = 3.268e-16 (float rounding only)
```

is zero to machine precision, which is the correct success criterion: not `== 0`
but "below the tolerance implied by the dtype". The measured station means
recover the offsets we put in (approximately $-3, -2.5, \ldots, +3$), which is the
sanity check that the subtraction was along the intended axis.

## 3. A distance matrix without a single Python loop

The second canonical operation. Given $n$ station positions as an `(n, 2)` array
of coordinates:

```python
dx = xy[:, None, 0] - xy[None, :, 0]     # (n, 1) - (1, n) -> (n, n)
dy = xy[:, None, 1] - xy[None, :, 1]
d = np.hypot(dx, dy)
```

The demo checks it against the explicit double loop:

```
xy.shape            = (200, 2)
dx.shape            = (200, 200)
d_bcast.nbytes      = 320000 bytes (0.3200 MB for n = 200)
broadcast == loop   = True
max |bcast - loop|  = 0.0
diagonal is zero     = True
matrix is symmetric  = True
```

Four independent checks: exact equality with the loop, exact zero diagonal,
exact symmetry, and the expected shape. Any of these failing means the axes were
indexed in the wrong order — the most common form of which is producing the
transpose, which is symmetric for distances and therefore invisible. For that
reason, when a quantity is *not* symmetric, always test it on an asymmetric case.
Reordering distances are the classic example in seismology.

The scaling warning follows:

```
  n =   2000: distance matrix would need    0.03 GB
  n =  20000: distance matrix would need    3.20 GB
```

$n^2$ memory. A 20 000-station survey is not a large survey, and the distance
matrix alone is 3.2 GB — before the residuals, the weights and the solver. The
remedies are (i) tile the computation over rows, computing one block of stations
at a time, or (ii) use a KD-tree or ball tree and visit only the pairs within a
range. Both are lesson
[08](./08-vectorisation-patterns.md)'s business; the point here is that the
one-liner's memory is predictable and must be predicted.

## 4. The outer-product idiom

The `[:, None]` and `[None, :]` pair is the general outer product:

```python
depth    = np.array([2.0, 4.0, 6.0, 8.0, 10.0])   # km
slowness = np.array([0.20, 0.15, 0.12, 0.10])     # s/km
t = depth[:, None] * slowness[None, :]            # (5, 4)
```

```
depth.shape (5,) x slowness.shape (4,) -> t.shape (5, 4)
travel-time matrix (s):
 [[0.4  0.3  0.24 0.2 ]
  [0.8  0.6  0.48 0.4 ]
  [1.2  0.9  0.72 0.6 ]
  [1.6  1.2  0.96 0.8 ]
  [2.   1.5  1.2  1.  ]]
np.outer agrees: True
```

`np.outer(depth, slowness)` is exactly this for 1-D inputs and is the clearer
choice when both are vectors of the same kind; the explicit `None` form is
necessary as soon as either operand is already multidimensional. Note that
`np.outer` flattens its arguments, so `np.outer(A, B)` on matrices does *not* do
what the elementwise `a[..., None] * b[..., None, :]` form does.

### 4.1 Rank-1 updates and the design matrix

Two patterns recur often enough to be worth naming, because both are outer
products in disguise.

**A rank-1 update** changes a matrix by an outer product of the form
$M \to M + u v^{\top}$:

```python
M += np.outer(u, v)          # one column-scaled addition per row
```

In geophysics this is the update of a cross-correlation matrix by one new
observation, the accumulation of a ray's contribution into a sensitivity matrix,
and the update of a covariance estimate by one sample. Written as a nested loop it
is $O(n m)$ Python operations; written as an outer product it is one compiled
broadcast, and the only memory it adds beyond the increment is the $n \times m$
result of `np.outer`, which can be avoided entirely with `M += u[:, None] * v`.

**A design matrix** is a column stack of basis functions evaluated at the
observations. The demo's least-squares example builds a parabola with

```python
A = np.column_stack([np.ones_like(x), x, x ** 2])
```

but the broadcasting form makes the structure explicit and generalises to any
number of terms:

```python
exponents = np.arange(4)                    # (4,)  -> constant, x, x^2, x^3
A = x[:, None] ** exponents                 # (n, 4)
```

One line, any polynomial order, and the column $k$ is $x^k$ by construction. The
same idiom builds a Fourier design matrix
(`np.sin(2 * np.pi * f * t[:, None])` for a vector of frequencies `f`), a
travel-time tomography matrix, and the design for a fit of an anomaly profile to a
set of analytic source shapes. Two cautions apply: the columns grow in magnitude
with the exponent, which is exactly the scaling problem that lessons
[05](./05-linear-algebra-numpy.md) treats with the condition number; and the
broadcast allocates the full $(n, n_{\text{terms}})$ matrix, which is the
deliberate cost of forming the design.

A third pattern, the **distance-to-sources matrix**, is the one that needs
blocking:

```python
for start in range(0, nobs, block):
    chunk = obs[start:start + block]            # (block, 2)
    d = np.hypot(chunk[:, None, 0] - src[:, 0],  # (block, nsrc)
                 chunk[:, None, 1] - src[:, 1])
    ...
```

The outer broadcast is over the *survey* axis, and the block size is chosen so
that the `(block, nsrc)` intermediate fits comfortably in cache. This is the
structure that makes the difference between §5's fatal allocation and a working
forward model.

## 5. What broadcasting costs, in advance

The demo tabulates the intermediate sizes:

```
operation                                       result shape        MB
(4000, 1) + (1, 4000)                           (4000, 4000)     128.0
(4000, 1, 1) * (1, 2000, 4000)                (4000, 2000, 4000)  256000.0
gravity forward: (nobs, 1) - (1, nsrc)         (20000, 5000)     800.0
```

The second row is the one to remember: a three-axis broadcast where all three
lengths are large creates a 256 GB array. NumPy will attempt it and the process
will be killed by the operating system, not by a friendly error. The habit that
prevents this is to compute `np.broadcast_shapes(a.shape, b.shape)`, multiply the
entries, and multiply by the itemsize — before running the expression. The last
row shows the ordinary cost of a gravity forward model: 20 000 observations by
5 000 sources is 800 MB of intermediates, which is why real codes loop over
observation blocks and vectorise the source axis.

## 6. Physical interpretation

Broadcasting is the array-level statement of a very common physical structure:
**the same operator applied along a shared axis.** A station has a DC offset; a
charge has a $1/r$ falloff; a source contributes to every observation with a
weight $G/(r^2)$. In each case one index ranges over the observations and another
over the causes, and the physics is a product over the *pair*, not the sets.

Written as a double loop, this structure is explicit and slow. Written as
broadcasting, it is implicit, fast, and only as correct as the axes are. The
discipline that keeps it correct is to name the axes in your head (or in a
comment) as `(observation, source)` and to assert the result shape against the
coordinate array it must match — exactly the discipline lesson
[04](./04-ufuncs-reductions.md) applies to reductions.

## 7. Assumptions and regime of validity

- **Broadcasting assumes the axes are semantically aligned.** The rule is
  positional, so `(12, 1)` against `(12, 500)` is accepted only because the
  trailing axis of the first is 1. If your station axis were the *last* axis of
  the data, the identical expression would produce a silent outer product.
- **No expansion is materialised for the *inputs*, but the *output* always is.**
  The saving is on the small operand.
- **Length-1 axes are indistinguishable from broadcast axes after the fact.**
  If you need to know how an array was created, keep the labels in the variable
  names (`mean_per_station` rather than `m`).
- **`(n,)` against `(n,)` is a dot product, not an outer product.** The demo's
  `(3, 4) + (4,)` succeeds because the trailing axes match. If you meant an
  outer product, you must write `[:, None]`.
- **Very large broadcasts are not just slow, they are fatal.** The process dies
  on allocation. There is no "memory-efficient broadcasting" mode; you must
  restructure the computation.
- **Broadcasting does not avoid the arithmetic.** The operation count is the
  same as the loop's; only the interpreter overhead and (sometimes) the
  vectorisation of the inner loop change.
- **`np.broadcast_shapes` is the cheap predictor** and is available as a public
  function since NumPy 1.20.

## 8. Python demonstration

The script is [`code/broadcasting_demo.py`](./code/broadcasting_demo.py):

```
.venv/bin/python 03-scientific-computing/02-numpy/code/broadcasting_demo.py
```

All data is SYNTHETIC. The traces are drawn from
`np.random.default_rng(20261014)`, the station coordinates are a seeded uniform
sample on a synthetic 5 km × 5 km square, and the depths and slownesses of the
travel-time table are hand-chosen numbers. No dataset is read.

Key output (this machine, NumPy 2.5.4):

```
mean.shape = (12,) -> cannot broadcast directly against (12, 500)
ValueError: operands could not be broadcast together with shapes (12,500) (12,) 
mean[:, None].shape = (12, 1)
demeaned.shape      = (12, 500)
max |station mean after| = 3.268e-16 (float rounding only)
newaxis, reshape and expand_dims agree: True
```

```
broadcast == loop   = True
max |bcast - loop|  = 0.0
diagonal is zero     = True
matrix is symmetric  = True
```

```
  n =   2000: distance matrix would need    0.03 GB
  n =  20000: distance matrix would need    3.20 GB
```

```
(4000, 1, 1) * (1, 2000, 4000)                (4000, 2000, 4000)  256000.0
```

### What to observe

1. The `ValueError` for `data - mean` is raised at the first element, before any
   arithmetic happens. Broadcasting validation is a shape check, which is why it
   is cheap and why it is worth triggering deliberately while developing.
2. The residual station mean is `3.268e-16`, roughly $1.5\,\epsilon$ for `float64`
   scaled by the data magnitude. Reporting a mean of "0" here would be wrong;
   reporting `3.3e-16` shows the subtraction was exact modulo rounding.
3. The distance matrix is `0.32 MB` at $n = 200$ and would be 10 000 times larger
   at $n = 20\,000$ — the $n^2$ scaling is not a rounding detail, it is the
   engineering constraint.
4. The 256 000 MB row is deliberately absurd and is *accepted* by the shape
   checker: `np.broadcast_shapes` returned a valid shape, and only the allocator
   would stop it. This is why the shape prediction must be paired with a byte
   prediction.

## 9. Common mistakes

1. **Forgetting `[:, None]`** on a per-station statistic, producing either a
   `ValueError` (lucky) or an outer product (unlucky).
2. **Using `[None, :]` where `[:, None]` was meant.** On a `(500,)` vector the two
   give `(1, 500)` and `(500, 1)` — same memory, different meaning, no error.
3. **Broadcasting a `(n,)` index against an `(n, m)` grid.** The trailing axes
   decide, so the row index must usually be `[:, None]`.
4. **Assuming a broadcast allocates nothing.** The output allocates, and so do
   any temporaries in the expression.
5. **Building an $n \times n$ matrix when a row-wise loop would do.** Section 5 of
   lesson [08](./08-vectorisation-patterns.md) measures the case where the loop
   wins.
6. **Reducing before broadcasting.** `data.mean(axis=0) - mean[:, None]` mixes a
   map-shaped array with a station-shaped one; get the axes consistent first,
   then broadcast.
7. **Trusting a symmetric test as a check.** Transposed distance matrices are
   symmetric. Test with an asymmetric quantity.
8. **Forgetting that `np.hypot(dx, dy)` is a ufunc** and writing
   `np.sqrt(dx**2 + dy**2)`, which allocates two extra arrays of the full size.

## 10. Real-world applications

- **Seismic processing.** Removing a per-channel instrument response, applying a
  per-trace scalar gain, and computing a per-sample time vector for all traces
  at once are all `(nchannel, 1)` or `(1, nsample)` broadcasts.
- **Potential-field forward modelling.** Gravity and magnetic kernels are
  products over (observation, source) pairs; the whole modelling literature is
  written in the broadcasting idiom, and the memory budget is the (nobs, nsrc)
  intermediate.
- **Receiver functions and array seismology.** Time-shifting a record section,
  computing cross-correlation matrices and stacking along moveout curves are
  broadcasts over (trace, time) and (trace, trace).
- **Interferometric synthetic aperture radar.** The phase difference between two
  acquisitions is a broadcast of a per-date scalar over a (line, pixel) grid.
- **Inversion regularisation.** A first-difference roughening operator applied to
  a model is a broadcast of a per-axis weight over the model grid.
- **Machine learning.** Normalisation statistics are computed per channel and
  broadcast over (batch, channel, sample); the memory of the broadcast determines
  the batch size.

## 11. Further reading

- **NumPy documentation, "Broadcasting".** [https://numpy.org](https://numpy.org)
  — the normative rules, including the `np.broadcast_shapes` and
  `np.broadcast_arrays` helpers used here. Level: beginner to intermediate.
- **NumPy documentation, "Universal functions (ufunc) — broadcasting".**
  [https://numpy.org](https://numpy.org) — how the rules interact with ufunc
  loops and the `out=` argument. Level: intermediate.
- **Harris, C. R., et al. "Array programming with NumPy." *Nature* 585, 357–362
  (2020).** DOI 10.1038/s41586-020-2649-2. Level: intermediate.
- **Golub, G. H., & Van Loan, C. F. *Matrix Computations* (4th ed., Johns Hopkins
  University Press, 2013).** The BLAS-2/BLAS-3 view of the outer product and
  rank-1 update, which is what a broadcast over a shared axis computes. Level:
  graduate.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 12. Related lessons

- [04 Universal Functions, Reductions and Axis Semantics](./04-ufuncs-reductions.md)
  — the axis conventions that broadcasting depends on.
- [08 Replacing Loops: Vectorisation Patterns and Traps](./08-vectorisation-patterns.md)
  — where broadcasting is slower than the loop it replaced.
- [07 Memory Layout, Strides and Cache-Aware Performance](./07-memory-performance.md)
  — why the intermediate's *layout* matters as well as its size.
- [01-07-07 Orthogonality, Projections and Least Squares](../../01-mathematics/07-linear-algebra/07-orthogonality.md)
  — the design-matrix construction that broadcasting builds in one line.
- [05-plotting-and-visualisation/04 3-D Plots, Surfaces and Voxel Rendering](../05-plotting-and-visualisation/04-3d-and-surfaces.md)
  — how a broadcast grid becomes a surface.

Exercises:
[`exercises/03-broadcasting-exercises.md`](./exercises/03-broadcasting-exercises.md)
and
[`exercises/03-broadcasting-solutions.md`](./exercises/03-broadcasting-solutions.md).

## Self-assessment checklist

- [ ] I can predict the result shape of any two broadcastable shapes by hand.
      (§1)
- [ ] I can write the station-mean subtraction three ways and say which I
      prefer. (§2)
- [ ] I can compute the bytes of an $n \times n$ distance matrix for a stated
      $n$ before running the code. (§3)
- [ ] I can write the outer-product idiom and say when `np.outer` is clearer.
      (§4)
- [ ] I can predict the size of a three-axis broadcast and explain why it is
      fatal rather than merely slow. (§5)
- [ ] I can state the tolerance I use instead of `== 0` after a broadcast
      subtraction, and why. (§2, §8)
- [ ] I can name two cases where broadcasting is the wrong tool. (§7, §9)
