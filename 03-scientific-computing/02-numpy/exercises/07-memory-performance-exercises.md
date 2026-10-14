# Exercises — 03-02-07 Memory Layout, Strides and Cache-Aware Performance

Attempt these **closed-book** before opening the
[solutions](./07-memory-performance-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/memory_performance_demo.py`](../code/memory_performance_demo.py) require
you to run it and report its actual output:

```
.venv/bin/python 03-scientific-computing/02-numpy/code/memory_performance_demo.py
```

**Every timing you report must be accompanied by the element count and the
machine.** Every performance claim must be checked with a correctness check. The
machine used for the reference numbers reports a 128-byte cache line
(`sysctl -n hw.cachelinesize`), a 64 KiB L1 data cache and a 6 MiB L2.

---

## ★ Foundational

**★1.** A `float64` array has shape `(4000, 4000)`.

(a) Give its memory and its C-order strides.
(b) Compute the number of 128-byte cache lines it occupies.
(c) State how many useful elements a traversal along axis 1 obtains per cache
line, and how many a traversal along axis 0 obtains.
(d) Compute the two numbers if the array were `float32` instead.

---

**★2.** Explain in one or two sentences each.

(a) Why a *reduction* along axis 0 of a C-ordered array need not be slower than
along axis 1, while an *elementwise* traversal along axis 0 is much slower.
(b) What `np.asfortranarray` does and what it costs.
(c) When making an array contiguous pays for itself.
(d) Why a matrix product is less sensitive to layout than an elementwise
operation.

---

**★3.** For a `(6000,)` `float64` vector $x$:

(a) Compute the number of bytes read by `(x * x).sum()`.
(b) Compute the number of bytes read by `np.dot(x, x)`.
(c) State the ratio and the reason for it.
(d) State which one is *faster* and which one is *cheaper*, and whether they can
differ.

---

**★4.** State whether each operation is memory-bandwidth-bound or
compute-bound, and why:

(a) `a + b` for two 100 MB arrays.
(b) `np.dot(A, B)` for two $1000 \times 1000$ arrays.
(c) `np.sort(x)` for a 100 MB vector.
(d) `np.exp(x)` for a 100 MB vector.

---

## ★★ Applied

**★★5.** Run the demo. Report, quoting its output:

(a) The C-order and F-order strides of the `(4, 5)` array, and `a.itemsize`.
(b) The three reduction timings and the `axis0/axis1` ratio.
(c) The two strided-view shapes and strides, the two timings and the ratio.
(d) The two traversal-loop timings and the ratio, plus the stated iteration and
addition counts.
(e) The `ascontiguousarray` timings, the copy size, and the per-million-element
copy cost.
(f) The matrix-product timings and ratio.

---

**★★6.** For the demo's strided case:

```
arr[:, ::16].shape = (3000, 188), strides = (24000, 128)
row-subset     (contiguous)   :    0.095 ms
column-strided (stride 128 B) :    2.270 ms
```

(a) Compute the penalty per pass, in milliseconds.
(b) Compute the cost of one full contiguity copy of `arr`, from the demo's
per-million-element figure ($1.32$ ms per $10^6$ elements; the array has
$9 \times 10^6$ elements).
(c) Compute the break-even number of passes.
(d) State the decision for a loop that performs 3 passes, and for one that
performs 50.

---

**★★7.** A finite-difference solver keeps five `(500, 500, 500)` `float64`
arrays (one model, four wavefields) and updates the fields in place each step.

(a) Compute the total memory.
(b) Compute the bytes touched per update step, assuming every element of every
field is read and written.
(c) Given a memory bandwidth of about 100 GB s⁻¹ (a representative modern
figure; measure yours before quoting it), compute the minimum time per step.
(d) State which single change gives the largest speed-up if the solver is
bandwidth-bound and the physics tolerates it.

---

## ★★★ Research-oriented

**★★★8.** A stack of 2048 seismic traces, each 4096 samples of `float32`, is
stored as `(ntrace, nsample)`.

(a) Compute the memory.
(b) A processing step requires the *median across traces at each sample*. State
the axis, the result shape and the memory traffic of the naive implementation,
which sorts along the axis.
(c) State why sorting along axis 0 of a C-ordered array is worse than sorting
along axis 1 and by roughly what factor, using the cache-line arithmetic of ★1.
(d) Propose the layout change that removes the penalty, and state its one-off
cost and the resulting traffic per pass.
(e) State the condition under which the layout change is *not* worth it.

---

**★★★9.** Design a benchmark for a stencil operation on a `(1024, 1024, 1024)`
`float32` grid, comparing row-major and column-major update order, such that the
result is trustworthy. State:

(a) the correctness check that must accompany the timing;
(b) the number of repetitions and the statistic you would report;
(c) the two machine properties you would measure and report alongside the time,
and why they are needed to interpret it;
(d) the reason a benchmark on a smaller grid can give the wrong answer, with the
criterion for "large enough".
