# Solutions — 19-06-01 Computer Architecture, Memory Hierarchy and Roofline Thinking

> **Read after attempting the exercises.** Numbers are computed from the printed
> demonstration outputs; timings are machine-dependent and vary between runs.

Lesson: [01 Computer Architecture, Memory Hierarchy and Roofline Thinking](../01-hpc-architecture.md).

---

## ★1 — Two intensities for one kernel

- **(a) three-array model:** read $x$, read $y$, write $y$: $24$ bytes; flops $2$;
  $I = 2/24 = 0.0833$ flop/byte.
- **(b) five-pass model:** read $x$, write temporary, read temporary, read $y$,
  write $y$: $40$ bytes; flops $2$; $I = 2/40 = 0.05$ flop/byte.

The two differ by $1.67\times$, which is why a GB/s figure is meaningless without
the traffic model attached. The demonstration uses (b) because that is the traffic
numpy's expression actually generates.

---

## ★2 — Where $100$ GB/s is first exceeded

From the table: $85.49$ GB/s at $64$ KB per array, then $117.38$ GB/s at
$512$ KB. So the first size above $100$ GB/s is **$512$ KB per array**
($65\,536$ elements). The smallest size, $8$ KB per array, gives **$44.72$ GB/s**.

---

## ★3 — Which regime

At $8$ KB, one pass touches $1024$ elements in about $0.9\ \mu\mathrm{s}$ — the
same order as the fixed cost of a single ufunc call measured at
$0.37\ \mu\mathrm{s}$ in [04 §3](../04-gpu-computing.md). The rate is therefore
set by **per-call overhead**, not by memory: the array is far too small to
saturate a memory system whose plateau is an order of magnitude higher.

---

## ★4 — Predicting the scale kernel from the copy kernel

Copy: $16$ bytes per element at $115.45$ GB/s, so
$t = 16 \times 8\,388\,608/115.45\times10^{9} = 1.162\times10^{-3}$ s
$= 1.162$ ms.

Scale: also $16$ bytes per element (one read, one write), so the prediction is the
same $1.162$ ms, i.e.

$$\text{bandwidth prediction} = 115.45\ \text{GB/s},$$

against a measured $105.48$ GB/s — a $9.4\%$ shortfall. The shortfall is real and
worth naming: the scale kernel performs one multiply per element and its `out=`
target is the same array it reads, so read and write are to the same location and
the store-to-load behaviour differs slightly from a pure copy. Within $10\%$, the
prediction from an independent kernel holds, which is the point.

---

## ★5 — Compute or memory bound?

Memory-bound ceiling: $I\times B = (20/24)\times108 = 90$ GFLOP/s.
Compute-bound requirement is irrelevant here because no compute peak was
measured — and that is the honest answer: **with only a bandwidth measurement,
the kernel is memory bound unless a compute-bound kernel is also measured**. The
crossover intensity at which a hypothetical compute peak $F$ would take over is
$I^{*} = F/108$, so without an $F$ the question cannot be closed. The kernel
moves $24$ bytes per element and needs $20$ flops, so it has
$I = 0.833$ flop/byte — high enough that a real machine's FLOP peak would need to
exceed $90$ GFLOP/s for the kernel to become compute bound.

---

## ★6 — The stencil ratio and the two explanations

$$8.305/4.061 = 2.045 .$$

The two candidate explanations, as the lesson lists them:

- **row-slice strides:** the five shifted reads are non-contiguous rows of a
  $2048^{2}$ array, so each contributes partial-line traffic;
- **per-call overhead:** the naive expression issues about ten ufunc calls, each
  with a fixed cost; at $0.37\ \mu\mathrm{s}$ each, ten calls are
  $3.7\ \mu\mathrm{s}$, which is negligible against $8.3$ ms and therefore **not**
  the explanation here.

The measurement already discriminates: per-call overhead accounts for $0.04\%$ of
the time, so the stride is the candidate. Exercise ★★★7 designs the confirming
experiment.

---

## ★7 — Separating stride from overhead

Two experiments, each with its own observable.

- **Stride:** run the same stencil on a grid whose rows are padded so that each
  row starts on a cache-line boundary, and on one where they are offset. If the
  time changes, the row-start alignment matters, which is a stride effect.
  Observable: time versus row length modulo the assumed $8$-double line.
- **Overhead:** measure the stencil on a small grid (say $64^{2}$) where the
  arithmetic is negligible and the call count is unchanged. If the time is
  $O(\text{number of calls})$, the ratio is overhead-limited. Observable: time per
  ufunc call at fixed array size.

The measured $0.04\%$ overhead share at $2048^{2}$ settles it for this size: the
stride explanation is the only one that can produce a factor $2.045$.

---

## ★8 — What is wrong with transferring $210$ GB/s

The number came from a copy kernel at a working-set size near the cache-resident
peak ($131$ GB/s was measured in the sweep, and $117-120$ GB/s in the
$512$ KB–$2$ MB range). Using it as a *peak* for a $2048^{2}$ stencil is wrong in
two ways:

- the stencil's working set ($2048^{2}$ doubles $= 33.6$ MB per array) is far
  outside any cache, so the relevant bandwidth is the **plateau** ($\sim108$ GB/s
  here), not the cache-resident peak;
- the stencil's own measured rate is $24.20$ GB/s of ideal bytes, i.e. it does not
  even reach the plateau, because of its strided access.

The measurement to make instead: run the *stencil* at the production grid size and
report its own rate, then compare it with the plateau measured by the same kernel
family. Anything else compares a cache-resident copy with a memory-bound stencil
and calls the difference a deficiency of the machine.
