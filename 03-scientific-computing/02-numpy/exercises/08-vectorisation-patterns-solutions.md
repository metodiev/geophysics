# Solutions — 03-02-08 Replacing Loops: Vectorisation Patterns and Traps

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output. Reference machine: Apple M5 (arm64), 16 GB RAM,
> NumPy 2.5.4, CPython 3.14. Timings are machine-dependent; the operation and
> element counts are not.

---

## ★1 — Fused or materialised

| form | verdict | full-size passes |
|---|---|---|
| (a) `(x * x).sum()` | **materialises** a temporary | 3 (read `x`, write temp, read temp) |
| (b) `np.dot(x, x)` | **fused** in BLAS | 1 (read `x`) |
| (c) `np.sum(np.abs(x))` | materialises the `abs` | 3 |
| (d) `np.add(x, y, out=z)` | **fused**, no temporary | 3 (read `x`, read `y`, write `z`) — but no *extra* allocation |
| (e) `np.where(x > 0, x, 0.0).sum()` | materialises the `where` result (and the mask) | 5+ |

Note (d): the number of passes is unchanged; what `out=` removes is the
*allocation* of a new array, and therefore the peak memory. That is often the
binding constraint.

---

## ★2 — Growth in a loop

**(a)** $1 + 2 + \cdots + m = m(m+1)/2$ element copies, because each `np.append`
allocates a buffer of length $k+1$ and copies the existing $k$ values.

**(b)** $20\,000 \times 20\,001 / 2 = 2.00 \times 10^8$ copies — the demo prints
`200010000`, about `200.0100e6`, against the 20 000 copies a preallocated fill
performs.

**(c)** (i) Preallocate with `np.empty(m)` and fill by index when the final length
is known. (ii) Collect into a Python list and call `np.concatenate` once, which
grows amortised-constant and copies once at the end.

**(d)** Quadratic in the number of iterations, $O(m^2)$, so it is unusable beyond a
few thousand iterations and merely wasteful below that.

---

## ★3 — One or two sentences

**(a)** Because it calls the Python function once per element, so it merely hides a
loop behind the broadcasting interface; it cannot compile or parallelise the
function. The demo measures it 107.8× slower than the array expression on
$10^6$ elements, and the reproducible reason is the $10^6$ Python calls.

**(b)** Because the broadcast materialises an intermediate proportional to
$n^2$ (or to the product of the broadcast axes), and once that intermediate
exceeds the cache the cost of writing and reading it can exceed the loop overhead
it saved. The demo measures a 384 MB intermediate against a 0.2 MB one for the
same result.

**(c)** "Vectorised" means the loop runs in compiled code; "fused" means the chain
of operations is performed in a single pass with no materialised intermediate.
A composition of two vectorised operations is vectorised but not fused — that is
exactly case ★1(a).

**(d)** Because the fastest way to compute the wrong answer is to compute it
vectorised: broadcasting with the wrong axis, an overflowed integer dtype, or a
`nan`-contaminated reduction all produce plausible arrays at full speed. The
demo's §1 checks the broadcast against the loop to $10^{-14}$ mGal before quoting
a speed-up.

---

## ★4 — Dedicated kernels

(a) `np.bincount(idx, weights=w, minlength=n)`
(b) `np.add.reduceat(a, starts)`
(c) `np.add.at(dest, idx, values)`
(d) `np.einsum("ij,jk,kl->il", ...)` with `optimize=True`
(e) `np.multiply(a, b, out=c)` (or any ufunc's `out=` parameter)

---

## ★5 — Reporting the demo

**(a)**

```
nobs = 400, nsrc = 400, pairs = 160000
triple loop (1 run)   :     87.75 ms
broadcast  (best of 3):      0.42 ms
speedup               :     216.0x   (machine dependent)
max |loop - vector|   : 3.253e-19 m/s^2 (3.253e-14 mGal)
agreement (rel 1e-10) : True
```

**(b)**

```
(x * x).sum()  :     5.56 ms, peak traced memory    160.0 MB
np.dot(x, x)   :     1.87 ms, peak traced memory      0.0 MB
```

**(c)**

```
Python list comprehension :    102.63 ms
array expression a*a-2*a+1:      0.59 ms
np.vectorize(lambda ...)  :     63.63 ms
np.vectorize / array expr =     107.8x   (machine dependent)
```

**(d)** `np.append in a loop :     46.21 ms`,
`preallocated fill   :      0.68 ms`, `ratio = 68x`, and the copy count
`1 + 2 + ... + 20000 = 200010000 element copies`.

**(e)**

```
full 4000x4000 broadcast : run 1  0.041 s, run 2  0.033 s, peak traced   384.0 MB
row-wise loop            : run 1  0.045 s, run 2  0.045 s, peak traced     0.2 MB
time ratios full/row     : 0.90x then 0.70x   (machine dependent, unstable)
peak memory ratio = 2392x   (this is the robust result)
```

---

## ★★6 — A delayed receiver matrix

**(a)** $12\,000^2 \times 4 = 5.76 \times 10^8$ bytes $= 576$ MB in `float32`.

**(b)** $1.44 \times 10^8$ elements; independent pairs number
$n(n-1)/2 = 7.2 \times 10^7$, so the matrix contains about **two times** as many
elements as independent pairs — and it stores the diagonal (zero by construction)
as well.

**(c)** With $B = 500$ the largest intermediate is
$500 \times 12\,000 = 6 \times 10^6$ elements $= 24$ MB in `float32`; the number
of blocks is $12\,000/500 = 24$.

**(d)** $1.44 \times 10^8$ delay evaluations in both forms. Blocking reorders the
loop; it does not change which pairs are visited. It changes the working set from
576 MB to 24 MB, which is what turns a memory-bound thrash into a cache-resident
computation. (If the matrix is symmetric in the physical problem, the unused half
is also skipped, which *does* halve the work: $7.2 \times 10^7$ evaluations.)

**(e)** When the matrix is not going to be used in full — for example when only
delays below a threshold matter, or only receivers within a few wavelengths
interact. Then the correct tool is a spatial index (KD-tree or ball tree) or a
neighbour list, which visits $O(n \log n)$ (or $O(n)$ for a bounded interaction
radius) pairs and never materialises the matrix.

---

## ★★7 — Binning weighted samples

**(a)**

```python
# 1. masked accumulation -- WRONG with duplicate indices
acc = np.zeros(nbins)
acc[idx] += w                       # duplicates are silently dropped

# 2. unbuffered scatter-accumulate -- correct
acc = np.zeros(nbins)
np.add.at(acc, idx, w)

# 3. dedicated histogram kernel -- correct
acc = np.bincount(idx, weights=w, minlength=nbins)
```

**(b)** Implementation 1. `acc[idx] += w` is
`acc.__setitem__(idx, acc.__getitem__(idx) + w)`: the gather copies, the add acts
on the copy, and the scatter writes each destination index once — so where two
samples share a bin, only one contributes. This is lesson
[02](../02-indexing-slicing.md) §4 in a numerical-processing costume, and it is the
most common silent bug in gridding code.

**(c)** `np.bincount` has a dedicated kernel for exactly this reduction. Using it
states the intent — "histogram these values" — with no ambiguity about duplicate
handling, and it is the form a reader can verify at a glance.

**(d)** Because the demo's measurement (0.57 ms for `np.add.at` against 0.98 ms for
`np.bincount` on a one-million-sample problem with 1000 bins) shows `np.add.at`
slightly *faster*; the choice is therefore made on **correctness and clarity**, not
speed. Performance criteria are machine- and version-dependent; semantic criteria
are not.

---

## ★★★8 — Convolution

**(a)** $60\,000 \times 1000 = 6 \times 10^7$ multiply-adds, i.e.
$1.2 \times 10^8$ flops.

**(b)** Use the convolution theorem:
$\mathcal{F}(w * x) = \mathcal{F}(w)\,\mathcal{F}(x)$, so convolve by transforming
both, multiplying pointwise and transforming back. With a transform length of
65536 ($2^{16}$, the next power of two above $60\,000 + 1000$), each FFT costs
about $5 N \log_2 N$ flops:

$$5 \times 65536 \times 16 = 5.24 \times 10^6 \text{ flops per transform},$$

three transforms plus $65536$ complex multiplies (6 flops each) give about
$1.6 \times 10^7$ flops — roughly an order of magnitude fewer than the direct
form, and the gap grows as the wavelet gets shorter.

**(c)** Two complex `float64` arrays of length 65536 are
$2 \times 65536 \times 16 = 2.1$ MB, plus the real output. The direct form needs no
storage beyond the input and output (the wavelet is 1000 samples), so the transform
trades about 2 MB of memory for an order of magnitude of time. On a modern machine
2 MB is negligible; on a memory-constrained device it is not, which is why
overlap-add/overlap-save split the transform into segments.

**(d)** The transform wins when $5N\log_2 N$ (times three transforms) is less than
$N_{\text{trace}} N_{\text{wavelet}}$. With $N_{\text{trace}} = 60\,000$ and
$N = 65536$ the transform term is about $2.5 \times 10^7$ against the direct
$6 \times 10^7$; the crossover for a transform of this length is a wavelet of about
250 samples. Shorter wavelets than that favour the transform strongly; longer
ones narrow the gap and eventually favour the direct form for a short trace.

**(e)** The transform exploits **translation invariance**: the operator is a
convolution, so its eigenvectors are complex exponentials and it is diagonal in the
Fourier basis. It does *not* hold when the operator is space- or time-variant — for
example a Q-filter whose attenuation depends on the travel time already elapsed, or
a depth-dependent deconvolution in a medium where the wavelet changes with depth.
Those require a direct, position-dependent computation (or a set of locally valid
transforms, which is the standard *time-variant* deconvolution in practice).

---

## ★★★9 — Judging a "40×" claim

**(a)** A reviewer needs:

1. **The arrays and dtypes involved**, so the element counts and byte counts can be
   checked.
2. **The absolute times** (or time per element), not only the ratio.
3. **The number of repetitions and the statistic reported** (best of $n$? mean of
   $n$? a single run?).
4. **The machine and the library build** (CPU, cache sizes, RAM, NumPy version,
   BLAS vendor and thread count), because BLAS-backed operations may be
   multithreaded.
5. **The correctness check** showing the two implementations agree, with the
   tolerance and the scale it is judged against.

**(b)** A speed-up on a **small** problem usually overestimates the gain for the
real one, because the interpreter overhead that vectorisation removes is a fixed
per-iteration cost: on a small array it dominates, while on a large array the
memory traffic does. A "40×" measured on an array that fits in cache is a statement
about loop overhead; the same code on a 100× larger array may show 2×, because both
versions are then bandwidth-bound.

**(c)** The two independent measurements are (i) the **peak memory allocation** (via
`tracemalloc`, or the process high-water mark) and (ii) the **bytes touched per
operation**, computed from the array shapes and dtypes. If the peak allocation is
unchanged, no intermediate was removed, so the gain is CPU-side. If the bytes
touched are unchanged but the time fell, the gain is CPU-side; if the bytes fell too,
it is memory-side. For a large array, a gain is far more likely to be memory-side,
because bandwidth is the binding constraint.

**(d)** The reproducible criterion is the **operation count and the element count**
per unit of work, together with the peak allocation — these are properties of the
algorithm and the machine architecture, and they are reproducible on any machine.
The achievable criterion when the timing itself cannot be reproduced is a
statement of the form: "the vectorised form performs 1 pass over 160 MB where the
composed form performs 3 passes over the same data, on the same machine, with a
measured peak allocation of 0 MB against 160 MB." That claim survives a change of
CPU; the "40×" does not.
