# Solutions — 03-02-01 ndarray Creation, dtypes, Shapes and Strides

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output on the project interpreter (NumPy 2.5.4).

---

## ★1 — Grid memory

**(a)** Shape `(3000, 2000)` — north first, because the module's convention is
`(north, east)` so that `gravity.mean(axis=1)` is an east profile.

**(b)** $\text{size} = 3000 \times 2000 = 6 \times 10^6$ elements;
$\text{nbytes} = 6 \times 10^6 \times 8 = 48 \times 10^6$ bytes = **48 MB**.

**(c)** In `float32`, itemsize 4:
$6 \times 10^6 \times 4 = 24 \times 10^6$ bytes = **24 MB**.

**(d)** In `int16`, itemsize 2: $12 \times 10^6$ bytes = **12 MB**. It is *not*
appropriate for a processed gravity field: a processed value is a real number in
mGal with a fractional part and a sign, while `int16` holds integers in
$[-32768, 32767]$ — a range of only 65536 counts, which cannot represent a small
anomaly on a large regional field without a scale-and-offset convention that must
then be carried with the data. Use `int16` for raw counts with a recorded scale
factor, not for derived values.

---

## ★2 — Strides by hand

**(a)** `(100, 80)` `float64`: moving one column right steps 8 bytes; moving one
row down steps $80 \times 8 = 640$ bytes. Strides `(640, 8)`. Axis **1** is
contiguous. (This is exactly the demo's `gz.strides`.)

**(b)** `(5, 4, 3)` `int16`, itemsize 2: strides
$(4 \times 3 \times 2,\ 3 \times 2,\ 2) = (24, 6, 2)$ bytes. Axis **2** is
contiguous.

**(c)** `(40, 60, 60)` `float32`, itemsize 4: strides
$(60 \times 60 \times 4,\ 60 \times 4,\ 4) = (14400, 240, 4)$ bytes. Axis **2**
(east) is contiguous. (Matches the demo.)

**(d)** In all three C-ordered cases the **last** axis is the contiguous one,
because C order stores the last index varying fastest.

---

## ★3 — A survey's storage

**(a)** $2 \times 10^3 \times 3 \times 10^3 \times 4096 =
2.458 \times 10^{10}$ values.

**(b)** `float64`: $2.458 \times 10^{10} \times 8 = 196.6$ GB.
`float32`: $98.3$ GB. `int16`: $49.2$ GB.

**(c)** Acquired data: `int16` (or `int32` if the digitiser is 24-bit), because it
halves or quarters the storage of the raw archive and preserves the exact counts
the instrument produced. Final processed stack: `float32`, because the processing
itself is floating-point and the result must be a real amplitude. The transition
from counts to physical units happens once, at the head of the processing
sequence, with the scale factor recorded.

**(d)** $\log_{10}(1/1.192 \times 10^{-7}) = \log_{10}(8.39 \times 10^6) = 6.92$
decimal digits. NumPy's `np.finfo(np.float32).precision` reports 6, which is the
conservative count of digits that survive a rounding.

---

## ★4 — `float32` accumulation

**(a)** $10^8 \times 0.1 = 10^7$ exactly.

**(b)** $0.1$ in binary is $0.0001100110011\ldots_2$, a repeating fraction, so the
stored value is $0.1(1 + \delta)$ with $|\delta| \le \epsilon_{32}/2 \approx
6 \times 10^{-8}$. Multiplying by $10^8$ amplifies that to an absolute error of
order $10^8 \times 0.1 \times 6 \times 10^{-8} = 0.6$ at worst, and the
accumulation adds its own rounding.

**(c)** `np.sum(x, dtype=np.float64)`. The array stays in `float32` (100 MB
instead of 200 MB) and the accumulator is double precision.

**(d)** `np.int64`. NumPy promotes integer reductions to the platform default
integer regardless of the input dtype, which prevents the sum of `int8` values
from overflowing at 127; the promotion does *not* protect a sum of `int64`
values from overflowing, which is the caller's responsibility.

---

## ★5 — Reporting the demo

**(a)** `gz.nbytes = 64000 bytes = 0.0640 MB`, `gz.strides = (640, 8) bytes`.

**(b)** `cube.size = 144000`, `cube.nbytes = 576000 bytes = 0.576000 MB`,
`cube.strides = (14400, 240, 4) bytes`.

**(c)** `float32 eps = 1.192e-07 (precision 6 digits)`,
`float64 eps = 2.220e-16 (precision 15 digits)`.

**(d)** C order `(40, 8)`, F order `(8, 32)`.

**(e)** `sum(float32) = 1000000.125` (error `0.125`);
`sum(float32, dtype=f8) = 1000000.0149011612` (error `0.0149012`);
`sum(float64) = 1000000.0` (error `0`).

Note that the `dtype=float64` accumulator is *not* exact: the input values are
already rounded to `float32`, so $0.0149$ of the error is irreducible without
recomputing the input in double precision. The accumulator fixes the *summation*
error, not the *representation* error.

---

## ★6 — `meshgrid` conventions

**(a)**

```python
east = 1000.0 + 50.0 * np.arange(20)      # 1000 .. 1950 m
north = 2000.0 + 50.0 * np.arange(10)     # 2000 .. 2450 m
E, N = np.meshgrid(east, north, indexing="xy")
```

`E.shape == (10, 20)`.

**(b)** `E[0, :3] = [1000. 1050. 1100.]` and `N[:3, 0] = [2000. 2050. 2100.]` —
both verified directly.

**(c)** With `indexing="ij"` the shape becomes `(20, 10)`, `E` varies along axis 0
and `N` along axis 1: the arrays are transposed relative to (b).

**(d)** For a square grid both conventions give the same shape, so an assertion on
shape passes; only the *values* are transposed, and any field built from the
coordinates is silently transposed too. The remedy is to use non-square grids in
tests and to assert a coordinate value, not only a shape.

---

## ★7 — Model memory budget

**(a)** $600 \times 600 \times 400 = 1.44 \times 10^8$ cells.
`float32`: $1.44 \times 10^8 \times 4 = 576$ MB. `float64`: $1152$ MB.

**(b)** Model (576 MB `float32`) plus four `float64` wavefields:
$4 \times 1152 = 4608$ MB. Peak $\approx 5.18$ GB.

**(c)** Velocities in the Earth span 1500–8000 m s⁻¹ and are known to about
$\pm 50$ m s⁻¹, i.e. a relative precision of $5 \times 10^{-3}$ near 10000 m s⁻¹.
`float32` carries $\sim 7$ decimal digits, so the storage is not the limiting
factor for the model. For the wavefields, however, time stepping accumulates
rounding over $10^4$–$10^5$ steps, and the loss of significance in a small
difference of large numbers is severe; use `float64` for the wavefields unless
the scheme has been validated in `float32` against an analytic solution.

**(d)** Available $16 - 2 - 5.18 = 8.82$ GB. One `float32`
$1000^3$ model is $4$ GB. So **two** fit, with 0.82 GB to spare. Note that this is
the kind of arithmetic that decides whether a `float64` model is affordable at
all: the same three models in `float64` would be 24 GB and do not fit.

---

## ★★8 — A dtype-selection rule

The rule must quantify three things.

1. **Measurement precision.** The relative precision required of the output is
   $r = \Delta x / x$, where $\Delta x$ is the physical uncertainty of a reading.
   The storage dtype must satisfy $\epsilon_{\text{stored}} \ll r$.
2. **Accumulated rounding.** For $N$ sequential operations with relative error
   bounded by $u$ per operation, a first-order bound is
   $N u$ (a random-walk argument gives the more realistic $\sqrt{N} u$). So
   require $\sqrt{N}\,\epsilon \ll r$.
3. **Memory.** $n_{\text{cells}} \times \text{itemsize} \times n_{\text{arrays}}
   \le$ budget.

Applying it: $r \approx 5 \times 10^{-3}$ from part ★7(c). With $N = 10^5$ steps,
$\sqrt{N} = 316$, so the requirement is $316\,\epsilon \ll 5 \times 10^{-3}$, i.e.
$\epsilon \ll 1.6 \times 10^{-5}$. `float32` has $\epsilon = 1.19 \times 10^{-7}$,
which satisfies the bound with two orders of magnitude to spare *if* the scheme is
stable and the error does not grow. A growing (unstable) error invalidates the
$\sqrt{N}$ estimate entirely, which is why the honest form of the rule is:

> Use `float32` when $\sqrt{N}\epsilon_{\text{32}} \ll r$ **and** the numerical
> scheme has been shown to be stable, and validate once in `float64` against an
> analytic solution.

The rule is checkable: $N$ is known, $r$ is measured, $\epsilon$ is a constant,
and the stability claim is a separate testable proposition.

---

## ★★9 — Endianness

**(a)** A NumPy dtype string carries a byte-order character: `'<'` little-endian,
`'>'` big-endian, `'='` native. So `'<i2'` and `'>i2'` are both 16-bit signed
integers with opposite byte order.

**(b)**

```python
raw = np.fromfile("legacy.bin", dtype=">i2")
native = raw.astype("<i2")          # or raw.astype(raw.dtype.newbyteorder("="))
```

`astype` performs the byte swap and produces a native-order array.

**(c)** `arr.byteswap()` returns an array of the *same dtype* whose bytes are
swapped: interpreting it still uses the original dtype, so the values are the
byte-swapped numbers, not the intended ones. The dtype must be changed as well, as
in

```python
swapped = arr.byteswap().view(arr.dtype.newbyteorder())
```

which is what `astype` does for you.

**(d)** The check is physical: a seismogram's first sample should be near the
pre-event noise floor and successive samples should be *smooth*. If the byte order
is wrong, consecutive samples differ by $\sim 2^{16}$ in magnitude and the trace
looks like white noise at full scale. Equivalently: compute
$\max_t |x_{t+1} - x_t|$ — for correct order it is a few counts, for wrong order it
is tens of thousands of counts. Never guess from the file size alone.
