---
id: 19-06-06
title: "Parallel I/O, Checkpointing and Job Management"
level: research
prereqs: ["19-06-03", "19-06-05", "19-06-01"]
tags: [numerical-modelling, hpc, parallel-io, checkpointing, job-management, fault-tolerance]
---

# Parallel I/O, Checkpointing and Job Management

## Learning objectives

By the end of this lesson you will be able to:

1. **Verify** that a checkpoint and restart reproduces an uninterrupted run
   exactly, and state the property that makes that possible.
2. **Measure** the cost of one file per rank against one aggregated file, and
   interpret the ratio as per-file overhead.
3. **Demonstrate** the two failure modes of a write — a torn file and a destroyed
   previous checkpoint — and the rename that prevents them.
4. **Verify** integrity with a hash, and state what a hash does and does not
   prove.
5. **Compute** an optimal checkpoint interval from a measured write cost and an
   assumed failure rate, and state which input is which.
6. **State** the job-management facts that decide whether a checkpoint is useful
   at all.

## Prerequisites

- [19-06-03 Distributed-Memory Parallelism with MPI](03-mpi-distributed.md) —
  why a parallel job has many writers.
- [19-06-05 Domain Decomposition and Load Balancing](05-domain-decomposition.md) —
  the per-rank data layout that shapes the I/O pattern.
- [19-06-01 Computer Architecture, Memory Hierarchy and Roofline Thinking](01-hpc-architecture.md) —
  the bandwidth-thinking this lesson applies to a filesystem.

All models and data in this module are **SYNTHETIC**. All numbers are
**measurements of a local filesystem** on the machine that ran
the demo, printed by `code/hpc_io_and_checkpointing_demo.py`. Array sizes, the
payload size used in the interval model and the machine **mean time between
failures are chosen teaching values**; the MTBF is an **assumed model input** and
is labelled as such in the output. The demo writes a few small files into the
directory it is run from and **deletes every one of them before exiting**; no
process, subprocess, MPI rank or network operation is used.

## 1. Checkpoint and restart: an exact test

Integrate a $256^{2}$ field for $24$ steps and compare two paths:

- **uninterrupted:** $24$ steps in one run;
- **restart:** $12$ steps, write a checkpoint, load it, run $12$ more steps.

| quantity | measured |
|---|---|
| $\max|u_{\text{restart}} - u_{\text{uninterrupted}}|$ | **0.000** |
| checkpoint size on disk | $524\,416$ bytes for $524\,288$ bytes of payload |

Bitwise identical. The checkpoint stores the state **exactly** — a `.npy` file
holds the array's bytes and dtype — and the arithmetic after the restart is the
same arithmetic in the same order. Any difference here would be a serialisation
bug, not rounding: the state was parked, not approximated. The extra $128$ bytes
on disk are the header, and a reader who has ever looked at a checkpoint and
wondered why it is never exactly divisible by the element size now knows.

**The design rule this test enforces:** a checkpoint must contain *everything the
next step reads*, and nothing inferred. If the restart reconstructs a derived
quantity from a rounded parameter, the trajectory will diverge — and it will
diverge slowly, which is the worst way for a bug to behave.

## 2. One file per rank against one aggregated file

$8$ ranks, $250\,000$ doubles each ($2$ MB per rank, $16$ MB total):

| pattern | time | throughput |
|---|---|---|
| one file per rank | 3.011 ms | 5.31 GB/s |
| one aggregated file | 3.179 ms | 5.03 GB/s |
| ratio per-rank/aggregated | **0.947** | |

Eight files were marginally faster than one on this filesystem, because the files
are large relative to the metadata cost of creating them and this machine's
filesystem parallelises the writes. On a parallel filesystem with many clients
the aggregated pattern usually wins, and on a distributed filesystem with a
metadata bottleneck the per-rank pattern usually wins — which is why the number
above is presented as a measurement of *this* filesystem, not as a rule.

What the ratio does show is the structure of the decision: two patterns, one
measurement, and a difference that a specification sheet cannot predict. A
production choice is made by measuring both on the target filesystem, and the
demo's code is short enough to be the template.

### 2.1 Collective I/O and striping: a model, not a measurement

Two mechanisms sit between a parallel application and the disks, and neither can
be measured by this demo:

- **Striping.** A file is laid out across storage targets in fixed-size chunks, so
  two ranks writing adjacent regions land on different targets and proceed in
  parallel; two ranks writing the *same* stripe serialise. The observable that a
  user can control is the stripe size and the number of targets, and the quantity
  that matters is the number of ranks whose writes fall in one stripe.
- **Collective I/O.** Instead of every rank issuing its own writes, one (or a few)
  aggregators gather the requests and issue large, contiguous writes. The model is
  a two-stage handoff: an intra-node shuffle costing roughly $\text{bytes}/B_{\text{mem}}$
  and a per-target write costing roughly $\text{bytes}/B_{\text{disk}}$ with a
  fixed cost per request. It wins when the per-request cost dominates — i.e. for
  many small, strided writes from many ranks — and loses when the data already
  arrives contiguously and the handoff is pure overhead.

The reason this belongs in the lesson as a model rather than as advice: both
mechanisms have an optimum, and the optimum depends on the request size, the rank
count, the topology and the filesystem — four quantities that must be measured on
the target machine. The demo's two-pattern experiment (Section 2) is the smallest
version of that measurement, and it is deliberately reported as a property of
*this* filesystem.

## 3. Torn writes, and the rename that prevents them

A checkpoint is rewritten every interval. If the job dies during the rewrite, one
of two things happens:

| strategy | outcome of a crash mid-write |
|---|---|
| write directly over the checkpoint | previous checkpoint destroyed: the reload fails with `EOF: reading magic string, expected 8 bytes got 6` |
| write to a temporary name, then `os.replace` | previous checkpoint intact: $1000$ values, identical to the original |

The demonstration produces both, by raising an exception after writing a partial
header. The first case is not a lost new checkpoint; it is a **lost previous
checkpoint**, i.e. the loss of every step since the one before the interval — the
worst possible outcome, and the most common way a home-made checkpointing scheme
fails.

`os.replace` is atomic within a filesystem: a reader sees either the old file or
the new one, never a half-written one. The cost is one extra name in the
directory and one rename call. Two further rules, both cheap:

- **keep two generations** (`ckpt.npy` and `ckpt.prev.npy`), so that a corrupted
  file detected after the rename still leaves the previous state;
- **never write a checkpoint on a shared path without a per-job name**, or
  concurrent jobs will overwrite each other's state.

## 4. Integrity: what a hash proves

| quantity | measured |
|---|---|
| digest of the checkpoint | `b8d4d46d9e80dfa0525a6f3f0a049466…` |
| digest after flipping one bit | `9f741925b13eccc1c3d5f37f82a88c60…` |
| digests equal | `False` |
| arrays equal | `False` |
| elements differing | **1** |

One flipped bit in one mantissa changes one element by about $10^{-16}$ relative
and changes the digest completely. Three things follow:

- a **hash detects** any change to the bytes, which is what integrity checking
  needs;
- a hash does **not** tell you the file is correct — only that it is the file
  whose hash you recorded;
- therefore the hash must be **recorded somewhere else** (in the run manifest or
  the job log), and verified at restart. A checksum stored inside the file it
  protects proves nothing.

This is the same reasoning as
[07 Reproducibility and Provenance](07-reproducible-hpc.md) applies to results,
applied to state.

## 5. The checkpoint interval, with its inputs labelled

Model inputs, and which is which:

| input | value | source |
|---|---|---|
| measured write bandwidth | 5.03 GB/s | **measured** on this filesystem |
| payload | 512 MB | chosen |
| checkpoint write cost | 0.10 s | computed from the two above |
| machine MTBF | 1.0 year $= 3.156\times10^{7}$ s | **assumed model parameter** |

Young's first-order rule balances the two costs — writing more often costs more
write time, writing less often costs more recomputation:

$$\text{interval} = \sqrt{2\, t_{\text{ckpt}}\,\text{MTBF}}
= \sqrt{2(0.10)(3.156\times10^{7})} = 2.53\times10^{3}\ \text{s} = 0.70\ \text{h}.$$

At that interval the work lost per failure is about $1267$ s (half the interval);
without checkpointing it would be about $1.578\times10^{7}$ s (half the MTBF). The
interval moves as the **square root** of both inputs, so halving the MTBF shortens
it by only $1.41\times$ — a robustness worth knowing before agonising over a
factor of two in the failure rate.

Two honest qualifications. First, the MTBF is invented; a real number comes from
operational logs and is itself uncertain. Second, the formula assumes failures are
memoryless and that a checkpoint costs a fixed time, both of which are wrong in
detail at scale; the model is a first-order design rule, and its inputs are
visible in the two lines above.

## 6. Job management: the facts that decide whether it works

A checkpoint is only useful if the job can use it. The operational requirements
are as important as the code:

- **the wall-clock limit must exceed the checkpoint interval plus the time to
  reach the next checkpoint**, or the job dies repeatedly at the same point;
- **the restart must be a submission, not a manual recovery:** a script that
  detects a valid checkpoint, verifies its hash, and resumes from the recorded
  step is the difference between an unattended campaign and a babysat one;
- **the job must record its own identity:** run identifier, step number, wall
  time, and the manifest of
  [07 Reproducibility and Provenance](07-reproducible-hpc.md) — otherwise a
  restarted run cannot be compared with the original;
- **the queue's own limits matter:** checkpointing every interval to a scratch
  filesystem with a per-user quota fails at scale, and the failure is a write
  error in the middle of a campaign.

None of this is measurable in a demo, and it is stated as requirements rather
than dressed up as measurements.

## 7. Assumptions and regime of validity

1. **A local filesystem, one machine.** The measured 5.03 GB/s is a local-disk
   number. Parallel filesystems have different latency, metadata and sharing
   behaviour, and the per-rank-versus-aggregated ratio can invert.
2. **Small payloads.** The demo writes 16 MB in total; a real checkpoint may be
   terabytes, where stripe sizes and client counts dominate.
3. **A serial write.** The demo writes from one process; a genuinely parallel
   write (collective I/O) changes the cost structure entirely.
4. **An assumed MTBF.** Stated above. Every interval number inherits its
   uncertainty.
5. **A single-generation scheme would be fragile.** Section 3 shows why a
   temporary file plus rename is the minimum safe pattern, and two generations is
   safer.
6. **No atomicity across files.** `os.replace` is atomic per file. A checkpoint
   consisting of several files needs its own completion marker (write the marker
   last), or a restart can read a mix of generations.

## 8. A fully worked example

Checkpointing a run that costs $0.10$ s to write and that produces $12$ s of
useful work per interval:

- **Overhead fraction:** $0.10/12.10 = 0.83\%$ of wall time spent writing.
- **Work at risk:** on average half an interval, $6$ s, plus the checkpoint cost
  itself, $0.10$ s.
- **Expected loss rate** with MTBF $3.156\times10^{7}$ s: one failure per
  $3.156\times10^{7}$ s, each costing about $6.1$ s, so about
  $6.1/3.156\times10^{7} = 1.9\times10^{-7}$ of the wall time, i.e.
  $0.00002\%$.
- **Doubling the interval** to $24$ s halves the write overhead to $0.42\%$ and
  doubles the work at risk; at this MTBF the difference is negligible, which is
  why the optimum is flat and why a campaign does not need to tune it finely.

Now change the MTBF by four orders of magnitude — to $3.156\times10^{3}$ s
(about an hour), as in a large campaign on a machine with a real failure rate —
and the picture inverts: work at risk per failure is $6$ s against a failure
every hour, the interval optimum becomes
$\sqrt{2(0.10)(3.156\times10^{3})} = 25$ s, and checkpointing every $12$ s is
within a factor of two of optimal while $0.1$ s of the wall time is spent over
$12$ s. Both regimes use the same formula; only the imposed MTBF differs, and
**that is the number a campaign must learn from its logs rather than assume**.

## 9. Python demonstration

`code/hpc_io_and_checkpointing_demo.py` runs the restart test, the two I/O
patterns, both torn-write cases, the checksum exercise and the interval model,
deleting its files as it goes.

```bash
cd 19-numerical-modeling-hpc/06-hpc-and-parallel-computing/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python hpc_io_and_checkpointing_demo.py
```

## 10. Exercises

Full sets with worked solutions are in
[`exercises/06-hpc-io-and-checkpointing-exercises.md`](./exercises/06-hpc-io-and-checkpointing-exercises.md)
and [`exercises/06-hpc-io-and-checkpointing-solutions.md`](./exercises/06-hpc-io-and-checkpointing-solutions.md).

- **★** State the two numbers a restart test compares and the expected difference.
- **★** Compute the overhead fraction for a $0.10$ s checkpoint every $60$ s.
- **★★** From the measured write throughput, find the payload at which a
  checkpoint costs $1\%$ of a $30$-minute interval.
- **★★** Explain why `os.replace` makes a checkpoint safe while a direct
  overwrite does not.
- **★★★** Design a restart protocol for a checkpoint that consists of four
  files, and state the marker that makes it safe.

## Mastery checkpoint

Without notes:

> A restart test reports $\max|u_{\text{restart}} - u_{\text{uninterrupted}}| =
> 0.000$, a per-rank/aggregated write ratio of $0.947$, and an interval of
> $0.70$ h from a $5.03$ GB/s write of $512$ MB and an assumed MTBF of one year.
> **(a)** State which of the three inputs to the interval is measured and which
> is assumed. **(b)** State the failure mode that the temporary-file-plus-rename
> pattern prevents. **(c)** State what the checksum proves and where it must be
> stored.

A worked version appears in the lesson-06
[solutions](./exercises/06-hpc-io-and-checkpointing-solutions.md).

## Common pitfalls

1. **Overwriting a checkpoint in place.** A crash mid-write destroys the
   *previous* checkpoint, which is the expensive one.
2. **Storing the checksum inside the file it protects.** It proves nothing about
   the file's integrity against the run that wrote it.
3. **Inferring a parallel-filesystem rule from a local measurement.** The
   measured ratio is $0.947$ here and can invert elsewhere.
4. **Quoting an interval without its MTBF.** The square-root dependence means a
   wrong MTBF does not ruin the choice, but an unstated one makes the number
   meaningless.
5. **Leaving the restart manual.** If a human must decide which checkpoint to
   load, the campaign is not automated and the model above does not apply.
6. **Forgetting that a checkpoint must contain everything the next step reads.**
   Restart equality is the test, and it caught exactly this class of error in
   Section 1.

## Related modules

- [03 Distributed-Memory Parallelism with MPI](03-mpi-distributed.md) — the
  message patterns a checkpoint must be consistent with.
- [05 Domain Decomposition and Load Balancing](05-domain-decomposition.md) — the
  layout that determines the I/O pattern.
- [07 Reproducibility and Provenance in HPC Workflows](07-reproducible-hpc.md) —
  the manifest a restart must carry.
- [19-07 Verification, Validation and Numerical Uncertainty](../07-verification-validation-uncertainty/README.md) —
  what a resumed run is entitled to claim.
- [22-data-engineering-reproducibility](../../22-data-engineering-reproducibility/README.md) —
  provenance and workflow management as a discipline.
