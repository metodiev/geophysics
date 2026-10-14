# Solutions — 19-06-03 Distributed-Memory Parallelism with MPI

> **Read after attempting the exercises.** Numbers are computed from the printed
> demonstration outputs; the interconnect parameters are **assumed model inputs**.

Lesson: [03 Distributed-Memory Parallelism with MPI](../03-mpi-distributed.md).

---

## ★1 — Halo fractions

For bands of height $b = 512/p$ and width $n = 512$, the halo fraction is
$2n/(nb) = 2/b$:

- $p = 16$: $b = 32$, fraction $= 2/32 = 6.25\%$ (matching the lesson-05 table);
- $p = 64$: $b = 8$, fraction $= 2/8 = 25.00\%$.

---

## ★2 — Why the bits agree

Every interior point is updated as
$u^{\text{new}} = 0.25(u_{\text{up}} + u_{\text{down}} + u_{\text{left}} +
u_{\text{right}})$ from the **previous** sweep's values. In the banded version
those four values are the same four numbers: two come from the rank's own interior
and two from the halo rows, which were copied verbatim from the neighbouring
ranks' interior rows. Same operands, same order of operations, same result —
hence the measured $0.000$ at every $p$, not merely a small difference.

---

## ★3 — Messages and bytes at $p = 8$

$2(p-1) = 14$ messages per sweep. Each message is one row of $512$ doubles
$= 4096$ bytes. Each rank sends two messages ($2\times4096 = 8192$ bytes, i.e.
$8$ kB) and, with a balanced ring, receives two. The total across ranks in one
sweep is $14 \times 4096 = 57\,344$ bytes $\approx 56$ kB.

---

## ★4 — Reproducing the ratio

$$c(p) = \frac{2(p-1)\alpha + 2(p-1)\cdot4096/\beta}{t_{\text{sweep}}} .$$

- $p = 4$: numerator $= 6(5\times10^{-6}) + 6(4096/10^{10})
  = 3.0\times10^{-5} + 2.46\times10^{-6} = 3.246\times10^{-5}$ s; dividing by
  $4.61\times10^{-4}$ s gives $c = 0.0704$ (printed $0.0723$; the difference is
  the rounding of the printed sweep time).
- $p = 16$: numerator $= 30(5\times10^{-6}) + 30(4.096\times10^{-7})
  = 1.5\times10^{-4} + 1.23\times10^{-5} = 1.623\times10^{-4}$ s, so
  $c = 0.3521$ (printed $0.3542$).

Both reproduce the table to about $1\%$, which is the arithmetic's own accuracy
given the printed rounding.

---

## ★5 — Where the ratio reaches one

Solve $2(p-1)(\alpha + 4096/\beta) = t_{\text{sweep}}$. With
$\alpha + 4096/\beta = 5\times10^{-6} + 4.096\times10^{-7} = 5.410\times10^{-6}$ s,

$$p - 1 = \frac{4.61\times10^{-4}}{2(5.410\times10^{-6})} = 42.6
\;\Rightarrow\; p \approx 43.6 .$$

So the model predicts $c = 1$ near $p \approx 44$. The model is **not credible
there**: at that $p$ a band is $512/44 \approx 12$ rows tall, the halo fraction is
$2/12 = 17\%$, and the assumption that a sweep is compute-limited by its interior
points while communication is a small perturbation has failed. The model's useful
range is the one where $c \ll 1$, and extrapolating it to $c = 1$ describes a
regime it was never fitted in.

---

## ★6 — The collective difference in ulp

The result is $-1.6100468382312125$; the difference is $2.22\times10^{-16}$. The
spacing of doubles near $1.61$ is $2^{-52}\times2^{0} = 2.22\times10^{-16}$, so the
difference is **1 ulp**.

Implication: an `Allreduce` result is only specified once the reduction order is
specified. Two codes that "both compute the sum" can disagree in the last bit, so
a reproducibility claim must name the reduction tree — and a test that changes the
communicator shape and expects the same digest is asserting something false.

---

## ★7 — Weak scaling

**Held constant:** work per rank, i.e. the global grid grows as $p$ so that each
rank keeps its band height (say $64$ rows). Then the halo fraction per rank is
constant at $2/64 = 3.1\%$, the messages per rank stay $2$, and the bytes per rank
stay $8192$ — all independent of $p$.

**Prediction:** $c$ is constant, so the modelled efficiency is constant too,
$1/(1+c)$ with $c = 0.187$ from the lesson's worked example, i.e. about $84\%$ at
every $p$ — as long as no global operation grows with $p$ (a global reduction,
whose cost grows as $\log p$, is the usual term that breaks weak scaling).

**Difference from the strong table:** strong scaling degrades with $p$ (from
$95.5\%$ to $57.1\%$ across $p = 2\ldots32$) because the halo fraction grows;
weak scaling is flat. That is why campaigns prefer weak scaling and why strong
scaling curves must state the fixed problem size.

---

## ★8 — Hang in a blocking ring

The two candidate causes:

- **Deadlock:** each rank sends to its right neighbour before posting the receive
  from its left one, and the sends cannot complete because no matching receives
  are posted — a cyclic wait. Observable: the hang is *reproducible* and the job
  never progresses at all (no output after the first step).
- **Convoying / buffer exhaustion:** the sends do complete for a while but consume
  the available buffers, so the code serialises internally, or it deadlocks only
  for particular message sizes and topologies. Observable: the code runs for many
  steps at small message sizes and hangs when a parameter crosses a threshold —
  intermittency that correlates with message size or rank count rather than with
  the code path.

The separating observable is **reproducibility with respect to message size**:
a true cyclic-wait deadlock hangs the same way regardless of size; a
buffer-related failure changes behaviour when the message size or the number of
eager-only messages changes.
