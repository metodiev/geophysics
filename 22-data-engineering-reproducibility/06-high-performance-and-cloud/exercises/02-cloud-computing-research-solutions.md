# Solutions — 22-06-02 Cloud Computing for Geophysical Computation

> Read after attempting. Numbers are computed here and match the demonstration's printed
> output. Lesson:
> [02 Cloud Computing for Geophysical Computation](../02-cloud-computing-research.md).

---

## ★1 — Amdahl's law

$$S(n) = \frac{1}{p + (1-p)/n}, \qquad \lim_{n\to\infty} S(n) = \frac{1}{p}.$$

The **serial fraction** $p$ is the part of the runtime that cannot be parallelised. In a
geophysical analysis it is typically: reading and parsing an input file; a setup stage that
builds a mesh or a matrix; a global reduction or a final merge of partial results; a
single-threaded library call; or the output write. Any of these caps the speedup at
$1/p$ no matter how many workers are used.

## ★2 — Speedup and efficiency at $p = 0.05$

(a) $S(4) = 1/(0.05 + 0.2375) = 3.48$; $S(16) = 1/(0.05 + 0.0594) = 9.14$;
$S(64) = 1/(0.05 + 0.0148) = 15.42$. All match the printed table.

(b) Efficiencies: $3.48/4 = 87.0\ \%$; $9.14/16 = 57.1\ \%$; $15.42/64 = 24.1\ \%$.

(c) The asymptote is $1/0.05 = 20\times$. At 1 024 workers the measured
speedup is 19.64 — within 2 % of the ceiling — at an efficiency of 1.9 %, so 98 % of the
fleet's capacity is spent waiting for the serial 5 %.

## ★3 — What the cloud changes

**Changes**: capacity is elastic and billed by the hour; a different machine type can be
used per task; storage and compute are separate services (so the network becomes a
first-class resource and the failure mode is a bill rather than a queue position).
**Does not change**: the serial fraction of the algorithm; the licences of the
dependencies and data; the correctness of the result.

## ★★4 — A 20-hour analysis at $p = 0.08$

(a) $S(8) = 1/(0.08 + 0.115) = 5.13$, efficiency 64.1 %;
$S(32) = 1/(0.08 + 0.02875) = 9.20$, efficiency 28.7 %;
$S(128) = 1/(0.08 + 0.00719) = 11.47$, efficiency 9.0 %.

(b) Wall time: $20/5.13 = 3.90$ h; $20/9.20 = 2.17$ h; $20/11.47 = 1.74$ h.

(c) Under 3 hours: 8 workers give 3.90 h (not enough), 16 workers give
$S(16) = 1/(0.08+0.0575) = 7.27 \to 2.75$ h (enough). So **16 workers**, consuming
$16 \times 2.75 = 44$ instance-hours. Note that requesting 128 instead buys 1.74 h for
$128 \times 1.74 = 223$ instance-hours — five times the cost for a 37 % shorter run.

## ★★5 — Interruptible capacity

(a) $P = 1 - e^{-0.03 \times 20/60} = 1 - e^{-0.01} = 0.00995 \approx 1.0\ \%$.

(b) Over a 2-hour run with 32 instances, the instance-hours are $64$, so
$P(\text{any}) = 1 - e^{-0.03 \times 64} = 1 - e^{-1.92} = 0.8536$.

(c) A 20-minute interval loses at most 20 minutes (10 on average) per interruption, and
the table's checkpoints cost time themselves. With $P(\text{any}) = 0.854$ over the run,
the expected loss is $0.854 \times 10$ minutes $\approx 8.5$ minutes if every instance
restarts from its last checkpoint — acceptable if the checkpoint write takes well under a
minute, and the trade is that a shorter interval reduces the loss but adds checkpoint
writes. Choose the interval where the checkpoint cost per interval is smaller than the
expected loss it prevents.

## ★★6 — "No speedup beyond 16 instances"

(a) Two explanations: (i) the serial fraction caps the speedup (the algorithm's ceiling);
(ii) the work is not actually being distributed — a scheduling or partitioning defect, so
the extra instances are idle or duplicating work. The distinguishing measurement is the
**per-instance activity**: if all 64 instances are busy and the wall time is flat, the
ceiling is algorithmic; if most are idle, the distribution is the problem.

(b) Efficiencies at $p = 0.05$: 57.1 % at 16 and 24.1 % at 64 — the *speedup* however
still rises from 9.14 to 15.42 (a 69 % improvement), so a fleet with a genuine 5 % serial
fraction does get faster from 16 to 64 workers. A flat wall time therefore points to the
second explanation (distribution), not to Amdahl alone; that is the value of having the
numbers.

(c) The change that moves the ceiling: reduce the serial fraction (parallelise the I/O,
the setup or the merge) — buying more instances does not.

## ★★★7 — A 5 000-realisations ensemble in 24 hours

**Per-realisations work.** Suppose each realisation takes 2 core-hours at 4 cores
(30 minutes) and 6 GB of memory, with a 10-minute setup per instance if the setup is not
shared.

**Worker count and type.** To finish in 24 hours with 30-minute tasks, one instance per
realisation is far more than needed: a **4-core instance running roughly 40 realisations
per day** finishes 5 000 realisations in about 125 instance-days, which is
5 000 × 0.5 h / 24 h = 104 instance-slots of 24 hours — around 105 instances if each runs
continuously, or fewer with better packing. Choose **128 instances of 4 cores** for a
margin, plan a two-hour setup stage once per instance rather than per realisation (a shared
read-only mount or a prebuilt container), and use the same instance type throughout so the
timing is comparable.

**Checkpointing.** Each realisation is short (30 minutes), so the checkpoint is the
realisation's own output: write it to durable storage and record completion; on a
per-realisations basis, no intra-task checkpointing is needed, and the restart granularity
is one realisation (30 minutes — acceptable). If realisations were longer than the
interruption interval, checkpoint inside them.

**Completion tracking.** A manifest of the 5 000 identifiers with a completion flag,
updated by the tasks; a supervisor loop resubmits the unfinished ones and stops when the
manifest is complete — the pattern of
[22-03-03](../../03-data-formats-and-engineering/03-data-pipelines.md) §5.

**Data placement.** Data and compute in the same region, with the input read once into a
shared read-only store; the container image pinned by digest
([22-02-06](../../02-reproducible-workflows/06-containers-reproducibility.md)) and pulled once
per instance.

**Cost accounting.** Record instance-hours per stage and per realisation (tagged), the
egress volume, and the storage months; compute the cost per realisation, which is the
number that makes the next ensemble's budget predictable
([22-06-03](../03-cost-and-scaling.md)).

**The failure it cannot prevent.** A systematic error in the *ensemble setup* (a wrong
parameter, a units error, a bad seed policy) that invalidates all 5 000 realisations after
they are paid for — which is why a 10-realisations pilot with known answers runs first,
and why the rate of completed realisations is monitored during the run.

## ★★★8 — Measuring a serial fraction

**Experiments.** Run the workload at several worker counts (1, 2, 4, 8, 16, 32, 64) with
the same problem size and inputs, recording wall time. Fit
$T(n) = T_1\,(p + (1-p)/n)$ by least squares on $1/T$ versus $1/n$ (a linear relation:
$1/T(n) = [p + (1-p)/n]/T_1$), which yields $p$ and $T_1$.

**Confounders and separation.**

1. **I/O and network**: if the input read does not scale with $n$, it behaves like a serial
   fraction. Repeat the series with the input cached locally and compare $p$.
2. **Contention**: on a shared machine, more workers mean more competition for memory
   bandwidth and the network. Repeat at low occupancy, or on a dedicated allocation.
3. **Warm caches**: the first run of a series is slower. Randomise the order of worker
   counts and repeat each point three times, reporting the spread.
4. **Overheads of the parallel framework**: startup and communication grow with $n$; they
   appear as a *negative* efficiency effect that the two-parameter model attributes to
   $p$, so also inspect the per-worker activity.

**What the estimate cannot tell you.** How the serial fraction behaves at a *different
problem size*: I/O and setup fractions usually fall as the problem grows (Amdahl's
"scaled" version), while communication fractions rise. A fraction measured on the pilot
problem is a hypothesis for the production problem, and the honest report states the
problem size it was measured on.

## ★★★9 — A bill dominated by egress

**The access pattern that produces it.** A fleet reading its data from an object store in
one region while running in another (or a group downloading archives to an institutional
cluster every run) — the classic misplacement that turns a compute problem into a transfer
problem.

**Three redesigns.**

1. **Co-locate**: run the compute in the same region as the data, so intra-region traffic
   replaces egress. *Measurement*: egress volume before and after, and wall time (network
   latency usually falls as well). *Risk*: lock-in to a region's instance availability, and
   a migration of the code's environment to that region.
2. **Cache**: keep a local, versioned copy of the region or period the analysis repeatedly
   reads, keyed by the data identifier so a change invalidates it. *Measurement*: cache
   hit rate and bytes fetched. *Risk*: a stale copy if the key is a name rather than an
   identifier — the same hazard as
   [22-04-05](../../04-databases-and-large-data/05-cloud-native-geoscience.md) §7.
3. **Change the layout**: chunked, tiled, columnar storage read by *range* so only the
   window the analysis needs crosses the network. *Measurement*: bytes fetched against
   bytes used (the amplification of
   [22-03-02](../../03-data-formats-and-engineering/02-format-design-tradeoffs.md) §2).
   *Risk*: a rewriting effort and a layout that suits one access pattern and not others.

**What you need to know about the charging model.** Which directions and destinations are
charged, whether traffic within a provider's network is free, whether requests themselves
are billed (and at what granularity), and whether the charge depends on the region pair.
Those details decide whether co-location removes the charge entirely or merely reduces it,
and the provider's current documentation is the only reliable source.
