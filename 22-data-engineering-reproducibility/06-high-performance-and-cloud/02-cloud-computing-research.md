---
id: 22-06-02
title: "Cloud Computing for Geophysical Computation"
level: research
prereqs: ["22-06-01", "22-02-06"]
estimated_minutes: 50
tags: [cloud-computing, scaling, amdahl, preemptible, research-computing]
---

# Cloud Computing for Geophysical Computation

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** strong-scaling speedup and efficiency from a serial fraction, and
   **state** the asymptote it imposes.
2. **Choose** a worker count from a wall-time requirement and the efficiency curve,
   and **compute** the instance-hours each choice consumes.
3. **Compute** the interruption probability of a preemptible fleet, and **choose** a
   checkpoint interval from the work a restart would lose.
4. **Separate** what the cloud changes (elastic capacity, per-task machine types,
   separated storage) from what it does not (the serial fraction, licences,
   correctness).
5. **Design** a cloud job for a stated deadline, with the request, the checkpointing
   and the cost accounting stated.
6. **Diagnose** three cloud-specific failures: a fleet that cannot finish because of
   one serial stage, a checkpoint interval longer than the interruption interval, and
   an egress charge larger than the compute.

All parallel fractions, interruption rates and costs in this lesson are **SYNTHETIC**
with chosen values in arbitrary units. No cloud service was used, no provider price or
limit is quoted, and no benchmark of a real system is reported; those change and must be
read from the provider's current documentation.

## Prerequisites

- [22-06-01 Running Jobs on HPC Clusters and Schedulers](./01-cluster-jobs.md) —
  the request-and-queue arithmetic that a cloud replaces with a price.
- [22-02-06 Containers for Computational Reproducibility](../02-reproducible-workflows/06-containers-reproducibility.md) —
  the artefact that makes a cloud instance reproducible.

## 1. Intuition: elastic capacity, unchanged physics

The cloud's offer is simple: obtain machines on demand, pay by the hour, and release
them when the work is done. That changes the *cost curve* of capacity — no queue, no
allocation, no waiting for a maintenance window — and it changes nothing about the
algorithm. A serial fraction of 5 % still caps the speedup at 20×; a wrong unit is still
wrong; a licence that forbids commercial use still forbids it. The first skill is
therefore to know which quantity the cloud can move.

## 2. Strong scaling and its ceiling

Amdahl's law gives the speedup from $n$ workers with a serial fraction $p$:

$$S(n) = \frac{1}{p + \dfrac{1-p}{n}}, \qquad
\lim_{n \to \infty} S(n) = \frac{1}{p}.$$

For $p = 0.05$ the demonstration measures:

| Workers | Speedup | Efficiency |
|---|---|---|
| 1 | 1.00 | 100.0 % |
| 4 | 3.48 | 87.0 % |
| 16 | 9.14 | 57.1 % |
| 64 | 15.42 | 24.1 % |
| 256 | 18.62 | 7.3 % |
| 1 024 | 19.64 | 1.9 % |

The asymptote is **20×**, and it is approached slowly: 64 workers give 15.4×, and the
next sixteen-fold increase in capacity adds 27 %. Efficiency collapses while speedup
crawls — at 1 024 workers, 98 % of the capacity is spent waiting for the serial part.
The practical conclusion: **find and shrink the serial fraction** (I/O, a per-file
read, a global reduction, a single-threaded setup stage) before buying more workers,
because the ceiling is a property of the code.

## 3. Cost: the deadline is the requirement

Instance-hours rise monotonically while wall time falls:

| Workers | Wall time (h) | Instance-hours | Cost (units) |
|---|---|---|---|
| 1 | 24.00 | 24.0 | 24.0 |
| 16 | 2.62 | 42.0 | 42.0 |
| 64 | 1.56 | 99.6 | 99.6 |
| 256 | 1.29 | 330.0 | 330.0 |

Going from 1 to 16 workers costs 75 % more instance-hours to save 21 hours; going from
64 to 256 costs 3.3× more to save 16 minutes. The honest framing is that the *deadline*
is the requirement and the cost is its price: state the wall time you need, then choose
the smallest worker count that meets it. Without a deadline, the cost-minimising answer
is one worker — which is why a project without a stated wall-time requirement cannot
justify its cloud bill.

## 4. Preemptible capacity and checkpointing

Cheaper capacity is often interruptible: an instance can be reclaimed, and the job must
restart. With a per-instance-hour interruption probability of 0.02, the probability of an
interruption within a checkpoint interval of $m$ minutes is

$$P = 1 - e^{-0.02\,m/60},$$

| Checkpoint every (min) | $P$ (interruption in the interval) | Expected work lost (h) |
|---|---|---|
| 60 | 0.0198 | 0.010 |
| 30 | 0.0100 | 0.002 |
| 10 | 0.0033 | 0.000 |
| 5 | 0.0017 | 0.000 |

and over a whole run the probability that *some* instance is interrupted is:

$$P(\text{any}) = 1 - e^{-\lambda\,(\text{instance-hours})},$$

which is **0.864** for a 64-instance run and **0.999** for a 256-instance run. At fleet
scale an interruption is not a risk but a certainty, so the design question becomes how
much work a restart costs: a checkpoint interval of 30 minutes bounds the loss to 15
minutes on average, and the checkpoint's own cost must be smaller than that (which is
why checkpointing a 20-minute stage every 5 minutes is counterproductive).

## 5. What the cloud changes, and what it does not

| Changes | Does not change |
|---|---|
| capacity is elastic and billed by the hour | the serial fraction of the algorithm |
| a different machine type per task | the licence of your dependencies or data |
| storage and compute are separate services, with a network between them | whether the result is correct |
| the failure mode shifts from a queue to a bill | the need for provenance and versioning |

Two consequences deserve emphasis. First, **storage and compute are separated**, so the
network becomes a first-class resource: a job that reads its data across the network pays
in wall time and in egress charges, which is why
[22-04-05](../04-databases-and-large-data/05-cloud-native-geoscience.md) argues for
chunked layouts and computation near the data. Second, the **failure mode is the bill**:
an inefficient request produces a charge rather than a queue position, so the accounting
of [22-06-03](03-cost-and-scaling.md) applies from the first run rather than at the end.

## 6. Practice: a cloud job that behaves

1. **State the deadline before choosing workers.** The efficiency curve then has a target,
   and the cost is defensible.
2. **Shrink the serial fraction first.** Profile the setup, the global reduction and the
   I/O; each of them caps the speedup whatever the fleet size.
3. **Use containers, pinned by digest.** The instance is ephemeral, so the environment
   must travel with the work ([22-02-06](../02-reproducible-workflows/06-containers-reproducibility.md)).
4. **Checkpoint to durable storage**, not to the instance's disk, and verify the
   checkpoint's contents rather than its existence.
5. **Treat the fleet as unreliable:** idempotent tasks that can be restarted, a manifest
   of completed work, and a supervisor that resubmits what did not complete
   ([22-03-03](../03-data-formats-and-engineering/03-data-pipelines.md) §5).
6. **Fetch data once, in the region where it lives**, and record the identifier rather
   than the URL ([22-03-04](../03-data-formats-and-engineering/04-getting-earth-data.md) §5).
7. **Tag every instance with the run's identifier**, so a bill can be attributed to a
   result — the cloud analogue of the scheduler's job identifier.

## 7. Worked example: a fleet that runs no faster than the laptop

A group moves a 24-hour analysis to 256 instances and measures 1.4 hours — barely better
than the 16-instance run's 2.6 hours.

1. **Compute the ceiling.** With $p = 0.05$ the asymptote is 20×, so the best possible
   wall time is 1.2 hours. At 1.29 hours the group is already at 93 % of the achievable
   speedup: the fleet is not the problem.
2. **Find the serial part.** Profile the run: setup, reading a configuration, a
   single-threaded merge at the end, or a global reduction. Each caps the speedup at
   1/p and, in the demonstration's model, a 5 % serial fraction caps it at 20×.
3. **Decide the response.** If the merge is the serial part and it can be partitioned,
   the ceiling moves; if it cannot, the deadline must be renegotiated or the algorithm
   changed. Buying 1 024 instances would buy 1.9 % efficiency (the measured row) — a
   large bill for a 4 % wall-time gain.
4. **Report the numbers.** Serial fraction, speedup, efficiency, wall time, instance-hours
   and cost per run — the six quantities that make the fleet's behaviour auditable.

## Assumptions and regime of validity

1. **Chosen serial fraction and rates.** The 5 % serial fraction and 0.02 per-hour
   interruption rate are teaching values; both must be measured for a real workload.
2. **Amdahl's law as the model.** It assumes a fixed problem size and no parallel
   overheads (communication, contention, scheduling); measured speedups are usually worse
   than Amdahl predicts, never better.
3. **Independent interruptions.** Instances in a fleet fail independently in the model;
   a provider-wide event correlates them, and a single-region design is a single failure
   domain.
4. **Homogeneous instances.** Mixed machine types, spot-price variation and network
   contention change the arithmetic.
5. **No provider specifics.** Prices, interruption rates, instance types and data-transfer
   costs differ by provider, region and time; the lesson's units are arbitrary, and a real
   design must read the current price list.

## The honest summary

The cloud supplies capacity on demand and changes nothing about the algorithm: with a
5 % serial fraction the speedup asymptote is 20×, reached as 15.4× at 64 workers and
19.6× at 1 024 workers where efficiency has fallen to 1.9 %, so the serial fraction — not
the fleet — is the ceiling to fix first. Cost rises monotonically with worker count
(24.0 to 330.0 units for 24.0 to 1.29 hours), which makes the stated deadline the
requirement and the cost its price, and interruption is a certainty at fleet scale
(0.999 for a 256-instance run), which makes the checkpoint interval the design variable
rather than the risk of interruption. What remains unchanged is the part that decides
whether the work was worth doing: the algorithm's structure, the licences, and the
correctness of the result.

## Python demonstration

[`code/cloud_computing_research_demo.py`](./code/cloud_computing_research_demo.py)
prints, with `np.random.default_rng(20261014)`:

1. the Amdahl table from 1 to 1 024 workers, with the 20× asymptote;
2. wall time, instance-hours and cost for four worker counts;
3. the checkpoint-interval table and the fleet interruption probabilities (0.864 and
   0.999);
4. the table of what the cloud changes and what it does not.

```bash
cd 22-data-engineering-reproducibility/06-high-performance-and-cloud/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python cloud_computing_research_demo.py
```

## Exercises

Graded problems and worked solutions are in
[`exercises/02-cloud-computing-research-exercises.md`](./exercises/02-cloud-computing-research-exercises.md)
and
[`exercises/02-cloud-computing-research-solutions.md`](./exercises/02-cloud-computing-research-solutions.md).

## Mastery checkpoint

Without notes: an analysis takes 20 hours on one worker with a serial fraction of 0.08.

1. Compute the speedup and efficiency at 8, 32 and 128 workers, and the asymptote.
2. Choose the smallest worker count that brings the run under 3 hours, and compute the
   instance-hours it consumes.
3. State the interruption probability for a 32-instance run with a per-hour rate of 0.03,
   and the checkpoint interval you would use.
4. State three things the migration to the cloud does not change.

## Common pitfalls

1. **Buying workers to fix a serial fraction.** 1 024 workers at 1.9 % efficiency is the
   demonstration's measured outcome.
2. **No stated deadline.** Without one, the cost-minimising answer is one worker and no
   cloud bill can be justified.
3. **Checkpointing less often than interruptions occur.** At fleet scale some instance is
   always interrupted.
4. **Reading data across the network in the inner loop.** It converts compute cost into
   egress cost and wall time.
5. **Ephemeral instances holding the only copy.** Durable storage for outputs and
   checkpoints, always.
6. **Untagged instances.** A bill that cannot be attributed to a result is a bill nobody
   can defend.

## Where this is used

- **Elastic analysis of large archives** — the workload that suits the cloud best, when
   data and compute are co-located:
  see [22-04-05 Cloud-Native Geoscience Data Access](../04-databases-and-large-data/05-cloud-native-geoscience.md).
- **Deadline-driven simulations** — where the wall-time requirement justifies the cost.
- **Teaching and workshops** — ephemeral, identically configured environments:
  see [22-02-06 Containers for Computational Reproducibility](../02-reproducible-workflows/06-containers-reproducibility.md).
- **Cost accounting** — the bill as the feedback signal:
  see [22-06-03 Cost, Scaling and Practical Efficiency](./03-cost-and-scaling.md).

## Related lessons

- [22-06-01 Running Jobs on HPC Clusters and Schedulers](./01-cluster-jobs.md) —
  the cluster alternative to elastic capacity.
- [22-06-03 Cost, Scaling and Practical Efficiency](./03-cost-and-scaling.md) —
  the cost model this lesson's numbers feed.
- [19-06 HPC and Parallel Computing](../../19-numerical-modeling-hpc/06-hpc-and-parallel-computing/README.md) —
  the algorithms behind the serial fraction.
- [22-02-06 Containers for Computational Reproducibility](../02-reproducible-workflows/06-containers-reproducibility.md) —
  what makes an ephemeral instance reproducible.

## Self-assessment checklist

- [ ] I can compute speedup, efficiency and the asymptote from a serial fraction.
- [ ] I can choose a worker count from a deadline.
- [ ] I can compute an interruption probability and choose a checkpoint interval.
- [ ] I can state what the cloud changes and what it does not.
- [ ] I can design a cloud job with checkpointing and completion tracking.
- [ ] I can name the three cloud-specific failures and their detectors.
