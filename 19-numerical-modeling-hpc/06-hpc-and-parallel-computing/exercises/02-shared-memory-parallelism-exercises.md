# Exercises — 19-06-02 Shared-Memory Parallelism: OpenMP and Threading

Attempt these before reading the
[solutions](./02-shared-memory-parallelism-solutions.md). The lesson is
[02 Shared-Memory Parallelism: OpenMP and Threading](../02-shared-memory-parallelism.md).
All workloads are **SYNTHETIC**; every speedup quoted is measured.

## ★ Foundational

**★1.** Four threads on pure-Python work give a speedup of $0.930\times$. State
the mechanism that produces a number below one.

**★2.** Compute the parallel efficiency of the sort speedup $3.746\times$ on four
threads.

**★3.** State the difference between a race condition and a deadlock in one
sentence each.

## ★★ Applied

**★★4.** Model the bandwidth-bound kernel as
$t(P) = t_{\text{work}}/P + t_{\text{start}} + t_{\text{contention}}$ with
$t_{\text{work}} = 29.021$ ms, $t_{\text{start}} = 4$ ms, and predict the time at
$P = 4$ without contention. State the measured value and the ratio.

**★★5.** The static schedule's blocks carry $[21, 25, 29, 33]$ units against an
ideal of $27$. Compute the bound on the static makespan and compare with the
measured ratio $1.116$.

**★★6.** A reduction gives one digest across pool sizes $1\ldots8$ with a fixed
8-chunk decomposition, and four digests across chunk counts. State the rule the
measurement establishes and why the second experiment is not a valid
reproducibility test.

## ★★★ Research-oriented

**★★★7.** Design an experiment that decides whether the $0.303\times$ result for
the bandwidth-bound kernel is caused by GIL contention or by memory contention,
and state the observable that separates them.

**★★★8.** A stencil iteration costs $2.5$ ns per interior point and there are
$4\times10^{6}$ points. Decide between `schedule(static)` and `schedule(dynamic)`
with a number, and state the threshold you used.
