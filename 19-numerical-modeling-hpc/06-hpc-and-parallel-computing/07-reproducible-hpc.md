---
id: 19-06-07
title: "Reproducibility and Provenance in HPC Workflows"
level: research
prereqs: ["19-06-02", "19-06-03", "19-06-06"]
tags: [numerical-modelling, hpc, reproducibility, provenance, floating-point, manifests]
---

# Reproducibility and Provenance in HPC Workflows

## Learning objectives

By the end of this lesson you will be able to:

1. **Demonstrate** that a reduction's bits depend on its order, and **quantify**
   the difference in units of the last place.
2. **Show** that an exactly-rounded sum removes the order dependence, and state
   what it costs.
3. **Specify** a reproducibility test that a reviewer can run, and name the
   quantity it must hold fixed.
4. **Construct** a canonical provenance manifest, hash it, and explain what the
   hash answers and what it does not.
5. **Measure** what a text round trip does to a floating-point state, and choose
   a serialisation accordingly.
6. **Write** a reproducibility claim that is falsifiable.

## Prerequisites

- [19-06-02 Shared-Memory Parallelism: OpenMP and Threading](02-shared-memory-parallelism.md) —
  the pool-size experiment this lesson generalises.
- [19-06-03 Distributed-Memory Parallelism with MPI](03-mpi-distributed.md) —
  collectives, where the reduction order is a communicator property.
- [19-06-06 Parallel I/O, Checkpointing and Job Management](06-hpc-io-and-checkpointing.md) —
  the state that must be hashable and restorable.

All numbers are **measurements of IEEE-754 double arithmetic** on the machine that
ran the demo, printed by `code/reproducible_hpc_demo.py`; IEEE-754 double
arithmetic is what makes them reproducible elsewhere. The arrays, chunk counts
and parameter dictionary are **SYNTHETIC** teaching values. Every file the demo
writes is deleted before it exits, and it starts only short-lived bounded thread
pools with explicit joins.

All models and data in this module are **SYNTHETIC**.

## 1. The same numbers, added differently, are different numbers

Floating-point addition is not associative: for doubles,
$(a+b)+c \neq a+(b+c)$ in general. A reduction is therefore a *specified* object
only when its order is specified. Measured on a fixed array of
$1\,048\,576$ doubles:

| decomposition | value | digest | difference from numpy, in ulp |
|---|---|---|---|
| 1 chunk | $-604.9947385276926$ | `2480f3b8d7fc37e1` | $+0.0$ |
| 4 chunks | $-604.9947385276926$ | `2480f3b8d7fc37e1` | $+0.0$ |
| 8 chunks | $-604.9947385276923$ | `deb0615c619b32fb` | $+2.0$ |
| 16 chunks | $-604.9947385276924$ | `e9bc265096c50b55` | $+1.0$ |
| 64 chunks | $-604.9947385276924$ | `e9bc265096c50b55` | $+1.0$ |

Three distinct digests across six decompositions, and a spread of $2$ ulp. Two
further measured facts make the scale concrete:

- a naive Python for-loop accumulation of the first $200\,000$ values differs from
  numpy's pairwise sum of the same values by $-63.0$ ulp, i.e. about
  $7.2\times10^{-12}$ in absolute terms;
- the differences above are *not monotone* in the chunk count: $4$ chunks happens
  to round to the same value as $1$ chunk, and $8$ does not.

That last point is the practical one. **You cannot tell by looking which
decomposition changes the last bits.** The claim must be tested, not reasoned
about — which is why the test in Section 3 is the deliverable of this lesson.

### 1.1 Three different words, three different tests

The words are used interchangeably in practice and should not be, because each has
a different test and a different strength:

| term | claim | test | measured evidence in this module |
|---|---|---|---|
| **repeatability** | the same code, same inputs, same machine gives the same answer | run twice, compare digests | trivially true here: a fixed seed and identical arithmetic |
| **bitwise reproducibility** | the same result **across a controlled change** — pool size, machine size, rank count — with the decomposition held fixed | fix the decomposition, vary the workers, compare digests | one digest across pool sizes $1\ldots8$, four across chunk counts |
| **replicability** | an *independent* implementation, or the same code on different hardware or a different backend, agrees to a stated tolerance | two implementations, one comparison, a stated tolerance | not measured here; it needs a second implementation |

Only the middle row is a claim this module can support with its own numbers, and
the row above it is nearly free while the row below it is the expensive one. A
paper that says "reproducible" without saying which row it means is making a claim
whose test is unknown — and, as Section 2 showed, the *decomposition* is the
quantity that separates the first two rows.

Note what the table also implies about tolerance: a replicability claim needs a
number attached, and the natural number is the one the arithmetic can deliver. For
a $10^{6}$-term double reduction, $10^{-15}$ relative is achievable and $10^{-16}$
is not, so a claim of agreement "to within $10^{-15}$" is the kind that can pass.
Among the failures this module's own demos produced, the sign error in the
fast-multipole expansion was an $O(1)$ disagreement — three orders of magnitude
outside any tolerance — and it was caught by exactly the comparison the table's
third row describes.

## 2. Order independence has a price, and it is purchasable

`math.fsum` is exactly rounded: its result is the correctly rounded value of the
exact sum, so it cannot depend on the order in which terms arrive. Six
decompositions of the same $200\,000$ values:

| chunks | `math.fsum` value | digest |
|---|---|---|
| 1 | $-556.489231889989$ | `1c22e0923955a191` |
| 2 | $-556.489231889989$ | `1c22e0923955a191` |
| 4 | $-556.489231889989$ | `1c22e0923955a191` |
| 8 | $-556.489231889989$ | `1c22e0923955a191` |
| 16 | $-556.489231889989$ | `1c22e0923955a191` |

**One digest for every decomposition.** Exact rounding converts "reproducible if
you use the same decomposition" into "reproducible", which is a strictly stronger
and much more useful statement. It costs time and memory, so it belongs on
reductions whose bits matter — residuals, norms, energy budgets, and the
quantities a paper will quote — and not on every inner loop.

The same idea in parallel form: a fixed pairwise tree with a stated merge order
gives the same digest for any number of workers, as
[02 §6](02-shared-memory-parallelism.md) measured, because the *tree* is fixed
even though the assignment of chunks to workers is not.

## 3. A reproducibility test someone else can run

The measured statement, from [02 §6](02-shared-memory-parallelism.md):

| experiment | digests |
|---|---|
| 8 chunks, pool size $1,2,4,8$ | **1 distinct** |
| chunk counts $1,3,8,16$ | **4 distinct** |

The test that follows from it:

> **Same decomposition, different machine size, same digest.**

Concretely: fix the chunk boundaries (and, in a distributed code, the reduction
tree), run the same input at $1$ worker and at $8$, and compare cryptographic
digests of the result. That test asserts something true and it fails loudly when
the code changes the arithmetic between the two runs.

A test that varies the decomposition asserts something **false**, and a code that
passes it is not being checked. This distinction is the difference between a
reproducibility claim and a reproducibility slogan.

## 4. Provenance: a canonical manifest, hashed

A run is identified by its inputs and its environment. Canonicalise and hash:

```json
{"byte_order":"little","cpu_count":10,"decomposition":{"layout":"bands","ranks":4},
 "dt_s":0.004,"float64_eps":2.220446049250313e-16,"grid":[256,256],
 "numpy":"2.5.4","python":"3.14.8",
 "reduction_order":"chunked, chunks=8, sequential merge","scipy":"1.18.1",
 "sweeps":200,"sympy":"1.14.0","velocity_km_s":3.5}
```

digest `dc1e910e295d7663e7025b24c472679d17649d244e7b2132bfff98410227350c`. Change
one parameter in its fourth significant digit, `dt_s` from $0.004$ to $0.0041$,
and the digest becomes `c908aec969c13e7e19250813d381125ae7caa199a542b535d6bb24c9188edc37`.
Sorted keys and no whitespace are what make two manifests comparable at all: a
canonical form is a prerequisite for a hash that means anything.

Three entries in that manifest deserve comment, because they are the ones
routinely omitted:

- **`reduction_order`**, because Section 1 showed that the decomposition is part
  of the arithmetic;
- **`float64_eps` and `byte_order`**, because they are what make the last-bit
  claim portable or not;
- **library versions**, because a change of BLAS or of numpy's pairwise summation
  threshold changes results without changing the code.

What the hash **does not** do: it does not prove the run was correct, it does not
record the *output*, and it does not fail if the input file changed but the
manifest did not. It answers one question — "is this the same run?" — quickly and
unambiguously.

## 5. Serialisation: the state is not a picture

Writing and reading back a $1000$-element array:

| form | identical bits | $\max$ difference |
|---|---|---|
| `.npy` binary | **True** | $0.000$ |
| text, $17$ significant digits | **True** | $0.000$ |
| text, $6$ significant digits | False | $4.999\times10^{-7}$ |

The six-digit round trip has a largest absolute error of $4.999\times10^{-7}$,
which is $4.8\times10^{-7}$ of the array's RMS — good enough to plot and nowhere
near good enough to restart from. Seventeen significant digits is the number that
round-trips a double **in this format**; the binary form always round-trips and is
smaller. Both are legitimate choices; silently writing six digits into a
checkpoint is not.

The general rule: **serialise state losslessly, serialise diagnostics however you
like, and label which is which.** A checkpoint, a restart file and a
"sensitivity matrix" that will be re-read later are all state. A plot's data
table usually is not.

## 6. Writing a claim that can fail

Compare three sentences.

- *"The code is reproducible."* Unfalsifiable, and therefore worth nothing.
- *"The code is bitwise reproducible on the same platform for a fixed
  decomposition and a fixed reduction order."* Falsifiable, and the test in
  Section 3 is its check.
- *"On this machine, with numpy 2.5.4 and a fixed 8-chunk decomposition, the run
  reproduces bitwise across pool sizes 1–8 and the manifest hash of each run is
  `dc1e910e…`."* A claim a reader can try to break, with the information needed
  to try.

The third sentence is the target. It names the platform, the decomposition, the
software and the observable — and if any of those changes, the claim is withdrawn
rather than weakened.

## 7. Assumptions and regime of validity

1. **IEEE-754 double arithmetic.** Every ulp statement depends on it; a
   fast-math flag, an extended-precision register or a different rounding mode
   changes the results and must be recorded.
2. **CPython and the measured numpy version.** numpy's `np.sum` uses pairwise
   summation above a size threshold; a version change can move that threshold and
   change results with no code change.
3. **No competing load.** The timings in this module move with machine load; the
   ulp differences do not, which is why this lesson's evidence is digests rather
   than times.
4. **A single process for the digest experiment.** The digest invariance was
   measured across *pool sizes* in one process; cross-machine invariance requires
   the same hardware behaviour (denormals, FMA contraction) and is a stronger
   claim than anything measured here.
5. **A canonical manifest format.** Sorting keys, fixing separators and fixing
   the number formatting are what make two manifests comparable; a manifest
   generated by `repr` of a dictionary is not canonical.
6. **Hashes are not signatures.** They detect change, not tampering or error. A
   provenance system that must resist forgery needs more than a hash.

## 8. A fully worked example

Take the six-chunk decomposition table from Section 1 and work out what it means
for a paper's table of results.

- **Spread:** the six values span $-604.9947385276926$ to
  $-604.9947385276923$, a difference of $3\times10^{-13}$, i.e. about $2$ ulp of a
  value near $605$.
- **Relative spread:** $3\times10^{-13}/605 = 5\times10^{-16}$, which is half the
  unit roundoff $\epsilon = 2.22\times10^{-16}$ times a modest number of
  roundings — exactly what a different summation order produces.
- **What this does to a reported number:** a quantity quoted to $4$ significant
  figures is unchanged; a quantity quoted to $15$ is not, and any claim of
  *bitwise* agreement must name the decomposition.
- **What a reviewer can check:** given the seed, the array size and the
  decomposition, the digest is either `deb0615c619b32fb` or it is not.

The size of the effect is the reason the rule is stated in terms of *claims*
rather than of *results*: the arithmetic is fine, the numbers are fine, and only
an over-specified claim is wrong.

## 9. Python demonstration

`code/reproducible_hpc_demo.py` measures the decomposition digests, the for-loop
against pairwise difference in ulp, the `math.fsum` invariance, the manifest
hashes, the three serialisations, and the worker-count invariance test.

```bash
cd 19-numerical-modeling-hpc/06-hpc-and-parallel-computing/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python reproducible_hpc_demo.py
```

## 10. Exercises

Full sets with worked solutions are in
[`exercises/07-reproducible-hpc-exercises.md`](./exercises/07-reproducible-hpc-exercises.md)
and [`exercises/07-reproducible-hpc-solutions.md`](./exercises/07-reproducible-hpc-solutions.md).

- **★** Convert the $2$ ulp spread of Section 1 into a relative difference.
- **★** State what `math.fsum` guarantees and what it does not.
- **★★** Design a digest test for a distributed reduction with a stated tree, and
  state what it must hold fixed.
- **★★** A checkpoint is written with six digits; state the consequence for a
  restart and how the demo's serialisation table proves it.
- **★★★** Write a reproducibility claim for a solver you know, and state the
  three ways you would try to falsify it.

## Mastery checkpoint

Without notes:

> A reduction gives digests `deb0615c619b32fb`, `e9bc265096c50b55` and
> `1c22e0923955a191` for three different chunk counts, and one digest for all
> pool sizes at a fixed chunk count. **(a)** State which quantity the digest
> depends on and which it does not. **(b)** State the test a reviewer should run.
> **(c)** A text round trip with six digits differs from the original by
> $4.999\times10^{-7}$; state whether that file may be used as a restart state
> and why.

A worked version appears in the lesson-07
[solutions](./exercises/07-reproducible-hpc-solutions.md).

## Common pitfalls

1. **Claiming reproducibility without naming the decomposition.** Measured here:
   four distinct digests across six chunk counts.
2. **Assuming a smaller difference is a better decomposition.** The differences
   are not monotone in the chunk count; only a test settles it.
3. **Hashing a non-canonical manifest.** Key order and whitespace change the
   hash without changing the run.
4. **Serialising state with six digits.** It is a picture, not a state.
5. **Believing a hash of the output proves the run's correctness.** It proves the
   bytes are the bytes.
6. **Leaving the reduction order implicit in a distributed code.** The
   communicator shape and the tree are part of the arithmetic; record them.

## Related modules

- [02 Shared-Memory Parallelism: OpenMP and Threading](02-shared-memory-parallelism.md) —
  the pool-size experiment.
- [03 Distributed-Memory Parallelism with MPI](03-mpi-distributed.md) —
  reductions whose order is a communicator property.
- [06 Parallel I/O, Checkpointing and Job Management](06-hpc-io-and-checkpointing.md) —
  the state that must round-trip losslessly.
- [22-data-engineering-reproducibility](../../22-data-engineering-reproducibility/README.md) —
  provenance, environment pinning and workflow managers as a discipline.
- [03-13 Testing, Profiling and Packaging](../../03-scientific-computing/13-testing-profiling-packaging/README.md) —
  the test suite that turns these claims into assertions.
