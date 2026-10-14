# Solutions — 03-02-03 Broadcasting Rules and Vectorised Thinking

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output on the project interpreter (NumPy 2.5.4).

---

## ★1 — Result shapes

Align from the right; an axis pair is compatible if equal or if one is 1.

| pair | result | reasoning |
|---|---|---|
| (a) `(64, 1) + (1, 32)` | `(64, 32)` | both axes stretched |
| (b) `(64, 32) + (64,)` | raises | trailing axes are 32 vs 64 |
| (c) `(64, 32) + (32,)` | `(64, 32)` | the `(32,)` is treated as `(1, 32)` |
| (d) `(3, 1, 5) * (1, 4, 1)` | `(3, 4, 5)` | every axis stretched |
| (e) `(8,) - (8, 1)` | `(8, 8)` | `(8,)` → `(1, 8)`; axes 8 vs 1 and 1 vs 8 |
| (f) `(10, 20, 30) + (30,)` | `(10, 20, 30)` | the `(30,)` aligns with the last axis |

Case (e) is the trap of §9 in the lesson: an outer-product-shaped result from two
1-D arrays of equal length, with no error.

---

## ★2 — Per-channel scaling

**(a)**

```python
scaled = data / np.abs(offsets)[:, None]
```

**(b)** The intermediate produced by the broadcast of `offsets[:, None]` against
`data` is conceptually `(48, 2000)`, but no such array is *allocated*: broadcasting
does not materialise the stretched operand. The only allocation is the
`(48, 2000)` **result** (the quotient), which is $768\,000$ bytes $= 0.768$ MB in
`float64`.

**(c)**

```python
out = np.empty_like(data)
for i in range(data.shape[0]):
    out[i] = data[i] / abs(offsets[i])
```

The loop avoids the `(48, 1)` temporary for the reshaped offsets, but not the
result. The memory saving is negligible here (the offset array is 384 bytes); the
loop's real cost is 48 interpreted iterations. Blocking is the technique that
actually matters, and it applies when the *kernel* is large, not when a vector is.

**(d)** For a `(nsample, nchannel)` array the channel axis is last, so the
reshaped offsets must be `(1, nchannel)`, i.e. `np.abs(offsets)[None, :]`.

---

## ★3 — Distance matrix memory

**(a)**

```python
dx = xy[:, None, 0] - xy[None, :, 0]
dy = xy[:, None, 1] - xy[None, :, 1]
d = np.hypot(dx, dy)
```

**(b)** $500 \times 500 \times 8 = 2 \times 10^6$ bytes $= 2$ MB.

**(c)** $n = 5000$: $5000^2 \times 8 = 2 \times 10^8$ bytes $= 200$ MB.
$n = 50\,000$: $50\,000^2 \times 8 = 2 \times 10^{10}$ bytes $= 20$ GB.

**(d)** $n^2$ evaluations in each case — $250\,000$, $2.5 \times 10^7$ and
$2.5 \times 10^9$. The number of *independent* pairs is $n(n-1)/2$, so the
computed count is a factor of about **2** larger than necessary (the diagonal is
zero by construction and the matrix is symmetric). Exploiting that symmetry halves
the work; exploiting a spatial index removes most of it.

---

## ★4 — One-sentence explanations

**(a)** A station mean has one value *per row*, so the axis that must line up with
rows is the trailing axis of a `(nsta, 1)` array; a sample mean has one value per
column, so it must be `(1, nsamp)`. Broadcasting aligns trailing axes.

**(b)** `np.tile` *materialises* the repeated data, so it is still needed when the
repetition must be a real array — for example when it is passed to a library that
requires matching shapes, or when the repeated operand is not the small one.

**(c)** Because the element $(i, j)$ of the product is $a_i b_j$: the outer product
of two vectors, written without the index arithmetic.

**(d)** Because both operands count where the vector is, so element $k$ pairs with
element $k$; an outer product requires one operand to vary along rows and the
other along columns, which is what `None` supplies.

---

## ★5 — Reporting the demo

**(a)**

```
ValueError: operands could not be broadcast together with shapes (12,500) (12,) 
max |station mean after| = 3.268e-16 (float rounding only)
```

**(b)** `broadcast == loop   = True`, `max |bcast - loop|  = 0.0`,
`diagonal is zero     = True` (and `matrix is symmetric  = True`).

**(c)** `n =   2000: distance matrix would need    0.03 GB` and
`n =  20000: distance matrix would need    3.20 GB`.

**(d)**

```
(4000, 1) + (1, 4000)                           (4000, 4000)     128.0
(4000, 1, 1) * (1, 2000, 4000)                (4000, 2000, 4000)  256000.0
gravity forward: (nobs, 1) - (1, nsrc)         (20000, 5000)     800.0
```

The largest case has shape `(4000, 2000, 4000)`.

**(e)** `` `mean[:, None]` costs 96 bytes; the broadcast result costs 48000 bytes.``
$96 = 12 \times 8$ and $48\,000 = 12 \times 500 \times 8$.

---

## ★★6 — A blocked gravity forward model

**(a)** $8000 \times 8000 = 6.4 \times 10^7$ kernel values; in `float64`,
$6.4 \times 10^7 \times 8 = 512$ MB.

**(b)** With a block of 500 observations the largest kernel is
$500 \times 8000 = 4 \times 10^6$ values $= 32$ MB. The number of blocks is
$8000 / 500 = 16$.

**(c)** Both forms evaluate $6.4 \times 10^7$ kernel values — the block form simply
processes them in 16 chunks. The work is identical because blocking changes the
*order* of the loops, not the set of pairs visited. What changes is the memory
high-water mark (512 MB against 32 MB) and the cache behaviour of each chunk.

**(d)** The kernel decays as $1/r^2$, so a source further than some distance
contributes less than the noise level divided by the number of sources: truncating
the sum where $G m / r^2 < \epsilon_{\text{needed}}/n_{\text{src}}$ is a defensible
approximation, provided the *aggregate* truncation error is bounded. In practice
one uses a spatial index (KD-tree or octree) to visit only nearby sources, which
lowers the cost to $O(n \log n)$ for a roughly uniform source distribution. The
wavelet-based and multipole expansions are the rigorous versions of this idea.

---

## ★★7 — Four spellings

Let `data` be `(12, 500)` and `mean` be `(12,)`.

| expression | intermediate | result |
|---|---|---|
| (a) `data - mean[:, None]` | none materialised for `mean`; output `(12, 500)` | new array (copy) |
| (b) `mean.reshape(-1, 1)` | same | new array (copy) |
| (c) `np.expand_dims(mean, 1)` | same | new array (copy) |
| (d) `data -= mean[:, None]` | same | **no new array**: `data` is modified in place |

The demo verifies that the three non-in-place spellings produce identical arrays
(`newaxis, reshape and expand_dims agree: True`). Form (d) is the one to use when
`data` is a large working array and the original values are no longer needed; it
halves the peak memory. It is also the form that silently corrupts a caller's
array if `data` is a function argument (lesson
[02](../02-indexing-slicing.md)).

---

## ★★★8 — What "station mean" assumes

The model is $\text{data}_{ij} = s_{ij} + c_i + \epsilon_{ij}$ with $c_i$ the
station's DC offset, $s_{ij}$ the signal, $\epsilon$ zero-mean noise.

**(a)** The estimator is the sample mean over samples:
$\hat{c}_i = \frac{1}{J}\sum_j \text{data}_{ij}$, and the subtraction removes it.

**(b)** It is unbiased for $c_i$ only if the sample mean of the *signal* is zero
over the averaging window: $\frac{1}{J}\sum_j s_{ij} = 0$. Equivalently, the signal
must have no DC component, or the window must contain a whole number of signal
cycles.

**(c)** Any low-frequency signal: a long-period surface wave, a regional field in a
potential-field survey, or a secular trend in a time series. A window shorter than
the signal period biases the estimate; a window containing a partial signal cycle
leaves a residual and removes part of the signal. This is why DC removal in
processing is done with respect to a *reference window* known to contain
background only, or with an explicit high-pass filter whose corner frequency is
justified.

**(d)** A linear drift needs two parameters per station. The broadcast form is

```python
t = np.arange(nsample, dtype=float)
base = np.column_stack([np.ones_like(t), t])            # (nsample, 2)
coef = np.linalg.lstsq(base, data.T, rcond=None)[0]     # (2, nsta)
drift = (coef.T @ base.T)                               # (nsta, nsample)
corrected = data - drift
```

The shapes are `(nsample, 2)` for the design matrix, `(2, nsta)` for the fitted
coefficients, and the product `coef.T @ base.T` broadcasts back to
`(nsta, nsample)`.

---

## ★★★9 — Same shape, different meaning

```python
rng = np.random.default_rng(20261014)
a = rng.normal(size=(100, 100))
u = np.linspace(-1.0, 1.0, 100)

by_row    = a - u[:, None]     # subtracts a ramp along rows
by_column = a - u[None, :]     # subtracts a ramp along columns
same_shape = by_row.shape == by_column.shape        # True, (100, 100)
different  = not np.allclose(by_row, by_column)     # True
```

Both results are `(100, 100)` and both are smooth; a plot of either looks like a
detrended field. The distinguishing test is **not** a shape assertion — it must be
a check against a *known* property of the coordinates. Two workable checks:

1. **A functional check.**
   `assert np.allclose(by_row.mean(axis=1), a.mean(axis=1) - u)` — the row means
   must differ from the original row means by exactly `u`. If the subtraction was
   along the wrong axis, this fails.
2. **A coordinate check.** Assert the shape against the coordinate array it must
   match *and* assert one known element:
   `assert by_row[0, 0] == a[0, 0] - u[0]`.

The invariant that makes the difference meaningful is that the subtracted quantity
`u` is indexed by the *same physical variable as the axis along which it varies*:
if `u` is a function of sampling time it must vary along the time axis, and if it
is a function of station it must vary along the station axis. That correspondence
between a physical variable and an array axis is the thing a shape assertion
cannot check, and the thing that must be written down.
