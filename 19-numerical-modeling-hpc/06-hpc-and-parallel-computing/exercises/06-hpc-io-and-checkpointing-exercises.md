# Exercises — 19-06-06 Parallel I/O, Checkpointing and Job Management

Attempt these before reading the
[solutions](./06-hpc-io-and-checkpointing-solutions.md). The lesson is
[06 Parallel I/O, Checkpointing and Job Management](../06-hpc-io-and-checkpointing.md).
Sizes and the machine failure rate are **SYNTHETIC** teaching values; the
filesystem throughput is measured.

## ★ Foundational

**★1.** A restart test reports a maximum difference of $0.000$ after $24$ steps
with a checkpoint at step $12$. State the two numbers compared and the expected
outcome if the checkpoint were lossless.

**★2.** Compute the overhead fraction of a $0.10$ s checkpoint taken every
$60$ s of work.

**★3.** State the two failure modes the temporary-file-plus-rename pattern
prevents, in one sentence each.

## ★★ Applied

**★★4.** From the measured write throughput of $5.03$ GB/s, find the payload at
which a checkpoint costs $1\%$ of a $30$-minute interval.

**★★5.** With MTBF $= 3.156\times10^{7}$ s and a checkpoint cost of $0.10$ s,
compute the optimal interval and the work at risk per failure at that interval.

**★★6.** Compute the ratio of the same optimal interval if the MTBF is
$3.156\times10^{3}$ s, and state the stated robustness rule that explains the
ratio's size.

## ★★★ Research-oriented

**★★★7.** A checkpoint consists of four files written sequentially. Design a
restart protocol that is safe against a crash after any subset of the four, and
state the marker that makes it work.

**★★★8.** Design a measurement that decides whether the per-rank or the
aggregated I/O pattern is better on a given filesystem, and state the two
observables that would invert the measured $0.947$ ratio.
