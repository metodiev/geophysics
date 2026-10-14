# Solutions — 03-02-04 Universal Functions, Reductions and Axis Semantics

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output on the project interpreter (NumPy 2.5.4).

---

## ★1 — Result shapes for `(8, 10, 12)` = (depth, north, east)

| expression | result shape | meaning of each element |
|---|---|---|
| (a) `.sum(axis=0)` | `(10, 12)` | depth-integrated value at each (north, east) cell |
| (b) `.mean(axis=2)` | `(8, 10)` | mean over east at each (depth, north) |
| (c) `.max(axis=(1, 2))` | `(8,)` | map maximum of each depth slice |
| (d) `.mean(axis=(0, 2))` | `(10,)` | mean over depth and east: a north profile |
| (e) `.sum()` and `.sum(axis=(0, 1, 2))` | both `()` | identical values |

(e) The two differ only in interface: `np.sum(a)` is `np.add.reduce(a)` with
`axis=None`, and `axis=(0, 1, 2)` is the explicit spelling of "all axes". Both
return a 0-d array; the total is the same, and both are `np.float64` scalars, not
Python floats.

Note (b): the mean over east of a *value* is a value, which is why the wrong-axis
result is impossible to spot by magnitude.

---

## ★2 — Profile and its assertion

**(a)** `profile = g.mean(axis=1)` — the mean over the north axis leaves east.

**(b)**

```python
profile = g.mean(axis=1)
assert profile.shape == east.shape, (profile.shape, east.shape)
```

**(c)** If `north.size == east.size`, both `g.mean(axis=0)` and `g.mean(axis=1)`
have the same length, so the assertion passes for the wrong reduction. The values
are then reversed relative to the coordinates, and a plot of `profile` against
`east` shows a profile with a plausible shape and the wrong orientation — or, in a
tomographic inversion, a model that is transposed in a way no residual check
detects. The remedy is to test on non-square grids and to assert a *value*
(e.g. `assert np.isclose(profile[0], g[:, 0].mean())`), not only a shape.

---

## ★3 — `nan` behaviour

**(a)** `np.sum(a) = nan`
**(b)** `np.nansum(a) = 13.0`
**(c)** `np.nanmean(a) = 3.25` ($13/4$)
**(d)** `np.isnan(a).sum(axis=1)` → `array([1, 1])`
**(e)** `np.nansum` of an all-`nan` slice is **0.0** — indistinguishable from a
genuine zero. A station that failed completely therefore contributes a plausible
zero to a map, and no downstream check flags it. Always pair `nansum` with a count
of valid values, as in (d), and mask where the count is zero.

---

## ★4 — One-line reductions

Given a cube `cube` of shape `(depth, north, east)` and `z0 = 0.0`, `dz = 25.0`:

**(a)** `profile = cube.mean(axis=(1, 2))`
**(b)** `cum = np.cumsum(profile)`
**(c)** `k = np.argmax(profile)`
**(d)** `z_max = z0 + dz * k`

The demo performs exactly this chain and reports
`argmax (flat index) = 560, value = 165.0000` for the *flattened cube* and
`unravel_index -> (depth, north, east) = (4, 6, 8)`; for the reduced profile the
index would be the depth index directly, which is why reducing first is the safer
route when only the depth of the maximum is wanted.

---

## ★5 — Reporting the demo

**(a)**

```
  cube.sum(axis=0        ) -> shape (10, 12)     sum = 118680.0000
  cube.sum(axis=1        ) -> shape (8, 12)      sum = 118680.0000
  cube.sum(axis=2        ) -> shape (8, 10)      sum = 118680.0000
  cube.sum(axis=(0, 1)   ) -> shape (12,)        sum = 118680.0000
  cube.sum(axis=(0, 2)   ) -> shape (10,)        sum = 118680.0000
  cube.sum(axis=(1, 2)   ) -> shape (8,)         sum = 118680.0000
  cube.sum(axis=(0, 1, 2)) -> shape ()           sum = 118680.0000
```

**(b)**

```
mean over north stations (axis=0) -> shape (12,): [ 958.  960.  962.  964. 1014. 1016. 1018. 1020. 1022.  976.  978.  980.]
mean over east stations  (axis=1) -> shape (10,): [ 951.  955.  959. 1013. 1017. 1021. 1025.  979.  983.  987.]
```

and `ValueError: operands could not be broadcast together with shapes (12,) (10,)`.

**(c)** `np.nansum(a) = 13.0`, `np.nanmean(a) = 3.25`, `np.nanmax(a) = 6.0`, and
`np.all(np.isnan(a).sum(axis=1) > 0) = True`; the propagating ones are
`np.sum(a) = nan` and `np.mean(a) = nan`.

**(d)** `argmax (flat index) = 560, value = 165.0000`;
`unravel_index -> (depth, north, east) = (4, 6, 8)`; `cube[4, 6, 8] = 165.0`.

**(e)** `np.sum : np.float64(7999998000000.0) in    0.443 ms` and
`Python for-loop : 7999998000000.0 in  105.798 ms`, with
`both results agree exactly: True` and `ratio (loop/numpy) = 239.0x`.

The exactness is a property of this particular number: $8 \times 10^{12}$ is
exactly representable in `float64`, and the values are integers, so no rounding
occurs in either summation order. Do not generalise it.

---

## ★★6 — Seismogram windows

**(a)** `k = int(np.argmax(np.abs(trace)))`, and
`t = k / fs = k / 100` s. (Using `np.abs` matters: the largest *amplitude* is the
largest absolute value, and `argmax` on the signed trace finds the largest
positive excursion instead.)

**(b)** $40\,000 / 50 = 800$ windows of 50 samples. With
`w = trace.reshape(800, 50)`, the per-window mean is `w.mean(axis=1)`.

**(c)** If the length is not a multiple of the window size, `reshape` **raises**
(`cannot reshape array of size ...`). The two standard treatments are (i) truncate
to `nw * win` samples before reshaping, and (ii) pad to the next multiple with
zeros or `nan` and mask the padded window afterwards, using `nanmean` where the
padding is `nan`.

**(d)** `np.add.reduceat(trace, starts)` reduces contiguous segments of *arbitrary*
length given their start offsets. It therefore handles unequal windows — an
increasing window length for a constant-Q spectrogram, variable-length event
windows, offset bins of unequal population — with no reshape and no padding, and
it is a single compiled kernel.

---

## ★★7 — Channels

**(a)** Shape `(1000000, 24)`. The mean of each channel is over the sample axis,
so `axis=0`, giving 24 values: `x.mean(axis=0)`.

**(b)** Global mean: `x.mean()` (equivalently `x.mean(axis=(0, 1))`), or
`x.mean(axis=0).mean()` — the mean of the channel means. These agree **only when
every channel has the same number of samples**. With unequal lengths (a ragged
record, one channel truncated), the mean of means weights each channel equally
while the global mean weights each sample equally, which is the intended
definition in almost every physical context.

**(c)** `x.var(axis=0)` gives `ddof=0`;
`x.var(axis=0, ddof=1)` multiplies by $N/(N-1)$. For $N = 10^6$ the relative
difference is $1/(N-1) = 1.0 \times 10^{-6}$, i.e. 0.0001 per cent — invisible at
six significant figures. For $N = 200$ it is 0.5 per cent, which is why the
convention must be stated for small samples.

**(d)**

```python
assert np.allclose(x.mean(), x.mean(axis=0).mean())
```

For equal-length channels the identity holds exactly (up to rounding). For unequal
lengths each channel's mean contributes with weight $1/n_{\text{channel}}$ instead
of $n_i/\sum n_j$, so the identity fails — and its failure is the diagnostic that
the data are ragged.

---

## ★★★8 — Sum against integral

The rectangle (left-endpoint) rule on a uniform grid of spacing $\Delta t$ is

$$\int_a^b x(t)\,\mathrm{d}t \approx \Delta t \sum_{k=0}^{N-1} x_k ,$$

and its leading error is **first order**: a term proportional to
$\Delta t\,[x(b) - x(a)]$ — the difference of the endpoint values times the
spacing. The **trapezoid rule** is

$$\int_a^b x\,\mathrm{d}t \approx \Delta t\left(\frac{x_0}{2} + x_1 + \cdots +
x_{N-1} + \frac{x_N}{2}\right),$$

which cancels that first-order term exactly, leaving an error of order
$\Delta t^2$ proportional to the integral of the second derivative.

**(a)** `np.sum(x)` has the units of $x$; the integral has the units of
$x$ multiplied by the units of $t$. Summing a vertical-velocity seismogram in
m s⁻¹ gives m s⁻¹; integrating it gives m — a displacement, which is the physically
meaningful quantity. A factor of $\Delta t$ (in seconds) and a dimensional check
are both required.

**(b)** For $x = \sin(2\pi t/T)$ sampled at $N$ points per period and summed over a
whole number of periods, the rectangle-rule relative error is
$O\!\left((2\pi/N)^2\right) = O(N^{-2})$, because the first-derivative error term
vanishes when integrated over a full period, leaving the second-order term.

**(c)** `np.trapezoid(y, x)` implements the composite trapezoid rule and accepts
the coordinate vector `x`; when `x` is supplied it handles *non-uniform* spacing
correctly, and when it is omitted it assumes uniform spacing $\Delta x = 1$. That
default is the trap: omitting the coordinate silently gives the sum, not the
integral.

---

## ★★★9 — "`nanmean` fixed the NaNs"

**(a)** A `nan` in a field dataset means either (i) **no measurement was made** at
that location — a gap, a deleted bad trace, a masked area — or (ii) **a measurement
was made and failed a quality test**, so the value is unknown. `nanmean` is
appropriate for (i), where removing the value is a sampling statement, and
dangerous for (ii), where it silently favours the values that passed the test
(survivorship bias: the noisy samples are preferentially removed, and the mean
becomes optimistic).

**(b)**

```python
n_valid = np.isfinite(x).sum(axis=axis)
mean = np.nanmean(x, axis=axis)
```

and report `n_valid` alongside `mean` — as an array of the same shape, so a
downstream consumer can mask the cells where `n_valid` is below a threshold.

**(c)** `np.nanmean` of an all-`nan` slice returns `nan` **with a
`RuntimeWarning: Mean of empty slice`**, and `np.nansum` returns `0.0`. The
`nan`-returning case is a *loud* failure when warnings are enabled and a silent
one when they are not; the `0.0` case is silent always. The mitigation is to
configure warnings as errors in test suites
(`np.seterr(all="raise")` does **not** cover this; use `warnings.simplefilter("error")`)
and to gate the result on `n_valid`.

**(d)** Return a tuple, or use a masked array:

```python
def robust_mean(x, axis):
    valid = np.isfinite(x)
    n = valid.sum(axis=axis)
    total = np.where(valid, x, 0.0).sum(axis=axis)
    with np.errstate(invalid="ignore", divide="ignore"):
        mean = np.where(n > 0, total / np.maximum(n, 1), np.nan)
    return mean, n
```

The count is now part of the returned value, so it cannot be forgotten by a caller.
`np.ma.masked_array(x, mask=~valid).mean(axis=axis)` achieves the same thing with
the mask travelling alongside the data, which is the cleaner option for a pipeline
in which several statistics are computed on the same selection.
