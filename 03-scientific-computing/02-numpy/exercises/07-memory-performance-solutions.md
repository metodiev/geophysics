# Solutions — 03-02-07 Memory Layout, Strides and Cache-Aware Performance

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output. The reference machine is an Apple M5 (arm64),
> 16 GB RAM, 128-byte cache line, 64 KiB L1 data, 6 MiB L2, NumPy 2.5.4.

---

## ★1 — Lines and useful elements

**(a)** $4000 \times 4000 \times 8 = 1.28 \times 10^8$ bytes $= 128$ MB.
Strides $(4000 \times 8,\ 8) = (32000, 8)$ bytes.

**(b)** $1.28 \times 10^8 / 128 = 10^6$ cache lines.

**(c)** Along axis 1 the stride is 8 bytes, so a 128-byte line yields
$128/8 = 16$ useful `float64` values. Along axis 0 the stride is 32000 bytes,
which is 250 lines, so each access lands on a fresh line and yields **1** useful
element per line.

**(d)** With `float32` the itemsize halves: strides $(16000, 4)$, and a line
yields $128/4 = 32$ useful values along axis 1 and still 1 along axis 0. The
penalty ratio *doubles* to 32 because the line can hold twice as many values
*and* the axis-0 case is unchanged. This is a useful counter to the intuition that
smaller dtypes are always better: they increase the *relative* cost of a strided
access even though they reduce the absolute traffic.

---

## ★2 — Explanations

**(a)** A reduction kernel chooses its own loop order, which is sequential over
memory for either axis: it streams rows into a small accumulator. An elementwise
kernel touches each element at its own address, so the stride *is* the access
pattern and a large stride wastes most of every cache line.

**(b)** `np.asfortranarray` returns an array with the same logical contents stored
column-major, allocating and copying if the input was C-ordered. The cost is one
read plus one write of the whole array — comparable to a single in-place pass.

**(c)** When the number of subsequent traversals exceeds the break-even point,
which is the copy cost divided by the per-pass penalty. The demo's numbers give
about **4 passes** (§ ★★6).

**(d)** Because BLAS is written as a cache-blocked algorithm with internal
transposes and vectorised inner kernels, so either layout can be consumed
efficiently. What it cannot absorb for free is a *mismatch* between its operands,
which forces an internal copy.

---

## ★3 — Bytes for $x^{\top}x$

**(a)** `(x * x)` allocates and writes a 6000-element temporary, then `sum` reads
it: reads $2 \times 6000 \times 8 = 96\,000$ bytes of `x` and of the temporary,
writes $48\,000$ — about **144 kB** of traffic for one number.

**(b)** `np.dot(x, x)` reads `x` once: $6000 \times 8 = 48\,000$ bytes, and writes
nothing.

**(c)** Ratio 3:1. The composition has a materialised intermediate; the fused kernel
does not (the demo measures the peak traced allocation as 160.0 MB against
0.0 MB at $n = 2 \times 10^7$).

**(d)** In the demo, `np.dot` was faster (1.87 ms against 5.56 ms) *and* cheaper.
They can differ: a fused kernel can be slower if it is single-threaded while the
composed version's kernels are multithreaded, or if the fused kernel has poor
vectorisation. The measurement decides, and both quantities must be reported.

---

## ★4 — Bandwidth or compute

**(a)** Bandwidth-bound: one add per element read-and-write, i.e. about
$1/24$ flop per byte.

**(b)** Compute-bound for $n = 1000$: $2 \times 10^9$ flops on $8$ MB of data is
$250$ flops per byte, far above the machine's ratio, so BLAS keeps the operands in
cache and the arithmetic is the limit.

**(c)** Bandwidth-bound (and, for large arrays, dominated by cache misses within
the sort's own passes). Sorting is a data-movement operation.

**(d)** Bandwidth-bound for a vectorised `np.exp`, because the special-function
kernel evaluates a polynomial with a handful of operations per element, and
memory traffic dominates. (A scalar loop would be compute-bound on the
transcendental evaluation instead.)

---

## ★5 — Reporting the demo

**(a)** `C-order  shape (4, 5), strides (40, 8) bytes`,
`F-order  shape (4, 5), strides (8, 32) bytes`, `a.itemsize = 8 bytes`.

**(b)**

```
  arr.sum(axis=1)  (axis 1 contiguous)  :     2.36 ms
  arr.sum(axis=0)  (axis 0 strided)     :     1.39 ms
  arr.sum()        (both axes, one pass):     1.30 ms
  ratio axis0/axis1 = 0.59x   (machine dependent)
```

**(c)**

```
arr[:, ::16].shape = (3000, 188), strides = (24000, 128)
arr[::16, :].shape = (188, 3000), strides = (384000, 8)
  column-strided (stride 128 B) :    2.290 ms
  row-subset     (contiguous)   :    0.129 ms
  ratio strided/contiguous = 17.8x   (machine dependent)
```

**(d)**

```
row-wise  for i: a[i, :] += 1.0 :     1.91 ms
col-wise  for j: b[:, j] += 1.0 :     6.32 ms
ratio column/row = 3.30x   (machine dependent)
both loops perform 2000 iterations and 4000000 additions
```

**(e)** `np.ascontiguousarray(arr.T) :    8.77 ms  (copies 72.0 MB)`,
`np.ascontiguousarray(arr)   :     0.00 ms  (returns the same object: True)`,
`copying 9000000 elements costs 1.30 ms per 1e6 elements`.

**(f)** `A @ B   (both C order):    6.77 ms`,
`Af @ Bf (both F order):     6.81 ms`, `ratio = 1.006x`.

---

## ★★6 — Break-even

**(a)** $2.290 - 0.129 = 2.161$ ms per strided pass.

**(b)** $9 \times 0.97 = 8.73$ ms (the demo's measured full-copy time is
8.77 ms, so the per-million figure is consistent to within 0.5 per cent).

**(c)** $8.73 / 2.161 = 4.04$, so **about 4 passes**.

**(d)** With 3 passes, keep the strided view: $3 \times 2.161 = 6.5$ ms against
$8.73$ ms for the copy. With 50 passes, copy once: $8.73 + 50 \times 0.129 =
15.2$ ms against $50 \times 2.161 = 108.1$ ms. The decision reverses between the
two cases, which is why the count of passes is the quantity to establish before
optimising. Note also that the break-even count itself moves with the machine —
the earlier run of the same demo gave 5.5 passes — which is why the *method*, and
not the number, is what to carry away.

---

## ★★7 — A finite-difference solver

**(a)** $5 \times 500^3 \times 8 = 5 \times 10^9$ bytes $= 5.0$ GB. (One array is
$500^3 \times 8 = 1000$ MB.)

**(b)** Reading and writing each of the five arrays once per step touches
$2 \times 5 \times 10^9 = 10^{10}$ bytes $= 10$ GB per step.

**(c)** At 100 GB s⁻¹, $10^{10}/10^{11} = 0.1$ s per step minimum. A 1000-step
simulation therefore cannot run faster than 100 s no matter how fast the
arithmetic is — the arithmetic intensity of a second-order stencil is about 1 flop
per byte, far below the machine balance.

**(d)** **Switch the storage to `float32`**, which halves the traffic and
therefore halves the runtime, *provided* the scheme has been validated in
`float64` and the accumulated rounding over the integration has been shown
acceptable. The second-largest gain comes from fusing the five-array update into
fewer passes (reading each array once and writing once), and the third from
cache-blocking the stencil. In practice the dtype change is first because it is a
one-word edit and the gain is exactly a factor of two.

---

## ★★★8 — A trace stack

**(a)** $2048 \times 4096 \times 4 = 3.36 \times 10^7$ bytes $= 33.6$ MB.

**(b)** The reduction is over the trace axis, so with shape
`(ntrace, nsample)` the axis is **0** and the result has shape `(4096,)` — one
median per sample. A naive implementation copies the transposed view, sorts along
the axis, and takes the middle element of each column. The traffic is at least one
full read and write of 33.6 MB per pass, plus whatever the sort does internally
(typically several passes).

**(c)** Sorting along axis 0 of a C-ordered array touches elements 4096 `float32`
= 16 384 bytes apart, so each access is on a different cache line: 1 useful value
out of 32 per 128-byte line, a **32×** bandwidth penalty relative to a contiguous
pass. Sorting along axis 1 works row-by-row, contiguously.

**(d)** **Store the stack transposed**, as `(nsample, ntrace)`, so the trace axis
is the last and contiguous one. `np.asfortranarray` (or `.T.copy()`) costs one
read and one write of 33.6 MB — about 0.5 ms at 100 GB s⁻¹ — and thereafter every
trace-axis traversal is contiguous.

**(e)** It is **not** worth it when the trace-axis operation is performed only a
few times: the one-off copy is then comparable to the penalty it removes. Use the
same break-even arithmetic as ★★6: copy cost divided by per-pass penalty gives the
number of passes required. It is also not worth it when the array is small enough
to fit in L2, where the whole array is effectively contiguous anyway.

---

## ★★★9 — A trustworthy stencil benchmark

**(a)** The update must be checked against an independent implementation — an
analytic solution, a stored reference field, or the *same* stencil evaluated in
the other traversal order — with the difference reported as a maximum absolute and
a maximum relative value. A benchmark without this check measures the speed of an
unknown computation.

**(b)** Report the **best of at least 5 repetitions** after one discarded warm-up
run, and state the statistic explicitly. Use `time.perf_counter()`. Report each
result as seconds per grid-cell update, and print the raw times rather than only
the ratio, because the ratio hides the absolute cost that decides whether the
optimisation matters at all.

**(c)** Measure and report (i) the **memory bandwidth** (a large `a += b` on arrays
much larger than the last-level cache gives bytes/second) and (ii) the **cache
line size** (`sysctl -n hw.cachelinesize` on macOS, `getconf LEVEL1_DCACHE_LINESIZE`
on Linux). Both are needed: without the bandwidth you cannot tell whether a
"slow" kernel is close to the hardware limit, and without the line size you cannot
predict the penalty for a given stride, so you cannot tell whether the result
generalises.

**(d)** A small grid fits in cache, so both traversal orders stream from L1/L2 and
the memory-order difference vanishes — the benchmark then measures the compiler's
unrolling and the loop overhead, not the memory system. The criterion for "large
enough" is that the working set exceed the **last-level cache**, which for the
reference machine is the 6 MiB L2 that the OS reports but can be much larger; a
safe rule is a working set of at least $10\times$ the largest cache you can
measure, discarding results whose timing does not change when the grid is doubled.
The $1024^3$ `float32` grid in the question is 4 GB per field and satisfies it
easily, but it also exceeds the machine's RAM once a few temporaries are added —
which is itself a result worth reporting.
