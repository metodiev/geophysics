# Solutions — 19-06-04 GPU Computing: CUDA, OpenCL and Portability Layers

> **Read after attempting the exercises.** Numbers are computed from the printed
> demonstration outputs. No GPU is used or timed anywhere.

Lesson: [04 GPU Computing: CUDA, OpenCL and Portability Layers](../04-gpu-computing.md).

---

## ★1 — Sectors for a stride-3 access

Lane $i$ accesses double index $3i$, i.e. byte offset $24i$. Sectors are
$32$ bytes, so lane $i$ touches sector $\lfloor 24i/32\rfloor$. For
$i = 0$: sector $0$; $i = 1$: byte $24$ → sector $0$; $i = 2$: byte $48$ →
sector $1$; $i = 3$: byte $72$ → sector $2$; and so on.

Distinct sectors touched over $i = 0\ldots31$:
$\lfloor 24 \times 31/32\rfloor = 23$, and the distinct values run from $0$ to
$23$, so **24 sectors** for $32$ values, i.e. $0.75$ useful doubles per sector.
That is worse than contiguous ($4$ per sector) and better than stride 8
($1$ per sector), which is exactly what the byte-offset argument predicts.

---

## ★2 — The crossover

$$\frac{0.37\times10^{-6}\ \text{s}}{0.1848\times10^{-9}\ \text{s per element}}
= 2002 \approx 2029 \text{ elements}.$$

(The printed $2029$ uses the rounded printed values; both are the same statement.)
Below about two thousand elements per call, the fixed cost dominates.

---

## ★3 — The gather/slice comparison

The two quantities are **time**, $4.708$ ms for the index-gather form and
$1.646$ ms for the shifted-slice form on a $1024^{2}$ grid, and their **agreement**
in the interior, which is $0.000$ exactly. The agreement is what makes the timing
comparison meaningful: the two forms compute the same field.

---

## ★4 — Per-element cost and a long run

- Gather: $4.708\times10^{-3}/1\,048\,576 = 4.49$ ns per element.
- Slice: $1.646\times10^{-3}/1\,048\,576 = 1.57$ ns per element.
- Ratio: $2.86$.

For $10^{5}$ steps: gather $= 10^{5}\times4.708\times10^{-3} = 470.8$ s;
slice $= 10^{5}\times1.646\times10^{-3} = 164.6$ s. The saving is $306$ s, or
$65\%$ of the run, for identical answers — decided entirely by the expression,
before any device choice.

---

## ★5 — Choosing a precision

Measured relative errors: float32 $8.025\times10^{-7}$, float64
$3.848\times10^{-16}$, i.e. a ratio of $2.1\times10^{9}$.

- A target of $10^{-8}$ **cannot** be met in float32 by this pairwise
  accumulation: the measured error already exceeds the target by $80\times$.
- Float64 has $3.8\times10^{-16}$, which is four orders of magnitude better than
  the target.

So: accumulate in **float64**. This does not forbid float32 kernels — the
elementwise work can be single precision, and only the accumulator and the
partial sums need double, which is the standard mixed-precision arrangement and
the reason "keep reductions in double" is a rule rather than a preference.

---

## ★6 — Why the CPU penalty is smaller than the sector count

A stride-8 sweep touches $32$ sectors per warp against $8$ for contiguous, a
factor of $4$ in *transactions*. The measured CPU penalty is $1.11\times$ per
element, for three reasons:

- a CPU core fetches whole cache lines (typically $64$ bytes $= 8$ doubles), so
  the eight doubles of a line are all in the same line as one stride-8 element —
  the access is line-aligned by construction and the "wasted" doubles cost
  bandwidth but not extra transactions;
- hardware prefetchers detect strided patterns and fetch ahead;
- out-of-order execution overlaps the fetches with arithmetic.

The sector count therefore bounds the *traffic*, not the *time*, on a device with
prefetching and a deep cache hierarchy. The lesson's phrasing is deliberate: it is
a transaction count, not a timing model.

---

## ★7 — Indexing arithmetic or memory transactions?

- **Indexing arithmetic:** the gather performs four 64-bit loads from the index
  table per element. Observable: cost scales with the *size of the index table*
  (e.g. $4$ columns against $1$), not with the memory pattern of `u`.
- **Memory transactions:** the gathered loads are scattered. Observable: if the
  index table is sorted so that the four neighbours are contiguous
  ($\text{nei}[i] = 4i + 0\ldots3$), the gather becomes a structured access, and
  the cost should drop towards the slice form's.

The experiment: three kernels on the same grid — (a) the true gather, (b) a
gather with a sorted, sequential index table, (c) the slice form. If (b) is close
to (a), the index table's size is the cost; if (b) is close to (c), the memory
pattern is the cost. The measured ratio of (a) to (c) is $2.86$, and the
distinction between (a) and (b) is the observation that settles which mechanism
dominates.

---

## ★8 — What a portability layer does not guarantee

| not guaranteed | test that detects it |
|---|---|
| identical floating-point results (reduction orders, reassociation, fused multiply-add) | hash the output bytes of the same run on both devices |
| identical performance (memory geometry, occupancy, cache behaviour) | time the same kernel on both devices at the production size; report both |
| identical numerical behaviour at the edges (boundary modes, fast-math flags) | compare against an analytic solution near the boundary, not only in the interior |

The layer guarantees the *expression* of one model on several devices. Every
claim about results or speed must be re-measured per device, and the digest test
in the first row is the same test the reproducibility lesson specifies — which is
why [07 Reproducibility and Provenance](../07-reproducible-hpc.md) treats the
device and backend as part of a run's identity.
