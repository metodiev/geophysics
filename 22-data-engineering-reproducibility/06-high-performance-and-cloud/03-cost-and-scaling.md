---
id: 22-06-03
title: "Cost, Scaling and Practical Efficiency"
level: research
prereqs: ["22-06-02", "22-06-01"]
estimated_minutes: 55
tags: [cost-model, weak-scaling, break-even, budgeting, efficiency]
---

# Cost, Scaling and Practical Efficiency

## Learning objectives

By the end of this lesson you will be able to:

1. **Build** a three-part cost model for a computational result — compute, storage and
   data movement — and **state** which part dominates for a data-heavy project.
2. **Compute** the cost per unit of work under weak scaling, and **state** why it rises
   even when the wall time barely changes.
3. **Find** the break-even core count for a deadline, and **state** the serial floor below
   which no number of cores reaches it.
4. **Forecast** a project's annual bill by item, and **identify** the items that compute
   optimisation cannot touch.
5. **Choose** between spending on cores and spending on storage, egress or recomputation,
   with the measurement that decides each.
6. **State** what a cost figure does and does not tell you about a result's value.

Every cost, rate and volume in this lesson is **SYNTHETIC**: chosen teaching values in
arbitrary units, not a provider's price list, and not a benchmark of a real system. Prices
change, regional pricing differs, and the only reliable authority is the provider's
current documentation.

## Prerequisites

- [22-06-02 Cloud Computing for Geophysical Computation](./02-cloud-computing-research.md) —
  the speedup model behind the deadline arithmetic.
- [22-06-01 Running Jobs on HPC Clusters and Schedulers](./01-cluster-jobs.md) —
  the allocation-based alternative to a bill.

## 1. Intuition: the solver is a line item

Ask a modeller what a simulation costs and the answer is the runtime. Ask a computing
centre and the answer is compute, storage, transfer and staff time — and in data-heavy
geoscience the compute is frequently the smallest of them. The reason is asymmetry:
compute is consumed once and can be right-sized, while data is *kept* and *moved*
repeatedly, and both are billed per unit per month or per transferred unit. A 12-hour
64-core run that produces two terabytes has, in the demonstration's SYNTHETIC model, a
total cost of 698.4 units of which **95 % is the storage and the egress** and 5 % is the
compute. Optimising the solver would improve the smaller half.

This is not an argument against efficiency. It is an argument for measuring all three
terms before choosing where to optimise.

## 2. The cost model

For one result, the three terms are

$$C_{\text{compute}} = n\,T(n)\,c_{h}, \qquad
C_{\text{storage}} = V\,m\,c_{s}, \qquad
C_{\text{egress}} = V_{\text{out}}\,c_{e},$$

where $n$ is the core (or instance) count, $T(n)$ the wall time in hours, $c_h$ the cost
per core-hour, $V$ the stored volume, $m$ the number of months kept, $c_s$ the cost per
volume-month and $c_e$ the cost per unit transferred. Three consequences follow directly.

1. **Compute scales with core-hours, not cores.** Doubling the cores to halve the wall
   time leaves the compute cost unchanged *only if* the parallel efficiency stays at
   100 %; it never does, so it rises.
2. **Storage scales with *time kept*.** A result kept for ten years pays for itself ten
   times over, which makes retention a decision rather than a default.
3. **Egress is a *read* pattern cost.** It is charged on the way out, so it is produced by
   the analysis reading data, not by the analysis producing it.

In the demonstration's example: $64 \times 12 \times 0.05 = 38.4$ units of compute,
$2 \times 12 \times 20 = 480$ units of storage for twelve months, and
$2 \times 90 = 180$ units of egress — total 698.4 units.

## 3. Weak scaling: the cost of the same work

Strong scaling asks "how much faster with more cores?". Weak scaling asks "what does the
*same work* cost when the problem is larger and spread over proportionally more cores?".
Efficiency falls with size — communication, load imbalance and I/O contention all grow —
so the cost per unit of work rises even though the wall time stays roughly constant.

The demonstration assumes a 2 % efficiency loss per doubling of cores, starting from
12 h at 64 cores:

| problem size | cores | wall (h) | core-hours | cost | cost per unit |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 64 | 12.00 | 768 | 38.4 | 38.40 |
| 8 | 512 | 12.73 | 6 520 | 326.0 | 40.75 |
| 64 | 4 096 | 13.51 | 55 353 | 2 767.7 | 43.24 |
| 512 | 32 768 | 14.34 | 469 930 | 23 496.5 | 45.89 |

The wall time grows by 20 % across a 512-fold increase in problem size; the cost per unit
of work grows by 19.5 %. Two sentences of practical value: *a run that "still takes
thirteen hours" is not a run that costs the same*, and *a 2 % per-doubling inefficiency is
the difference between 45.89 and 38.40 units per unit of work at the top of the range*.

## 4. The break-even core count

Using $T(n) = T_{64}\,\bigl(p + (1-p)\,64/n\bigr)$ with $p = 0.05$ from a 64-core,
12-hour base, the demonstration solves for the cores each deadline requires:

| deadline (h) | cores needed | wall (h) | core-hours | cost | feasible |
| ---: | ---: | ---: | ---: | ---: | :--- |
| 12.0 | 64 | 12.00 | 768 | 38.4 | yes |
| 6.0 | 256 | 3.45 | 883 | 44.2 | yes |
| 3.0 | 512 | 2.03 | 1 037 | 51.8 | yes |
| 1.5 | 1 024 | 1.31 | 1 344 | 67.2 | yes |
| 0.5 | — | 0.60 | — | — | **no** |

The serial floor is $12 \times 0.05 = 0.60$ h; no core count reaches the half-hour
deadline, and the "cores needed" column would have to be infinite. Note the shape of the
cost column: the *first* halving of the deadline costs 15 % more, the second 17 %, the
third 30 %. The marginal cost of squeezing the wall time rises precisely where the
efficiency is lowest — that is the practical meaning of the asymptote.

Notice also that these are **best cases** for the parallelism: they assume the only
inefficiency is the serial fraction. Communication, load imbalance and file contention
add to the wall time and therefore to the core-hours.

## 5. Where the cost actually goes

A data-heavy project's annual bill, in the demonstration's SYNTHETIC decomposition:

| item | share of annual cost |
| :--- | ---: |
| compute for analysis | 35.0 % |
| storage of raw data | 25.0 % |
| storage of derived products | 10.0 % |
| data egress | 20.0 % |
| recomputation after failures | 10.0 % |
| **not compute** | **65 %** |

Each line has a different fix, and only the first is a solver issue.

- **Raw-data storage** is fixed by retention policy and by not keeping re-downloadable
  archives: keep the identifier and the recipe, not necessarily the bytes.
- **Derived-product storage** is fixed by deleting regenerable intermediates and by a
  format that is not larger than it needs to be
  ([22-03-01](../03-data-formats-and-engineering/01-file-formats-scientific.md)).
- **Egress** is fixed by placing compute next to data and by reading only the window the
  analysis needs ([22-04-05](../04-databases-and-large-data/05-cloud-native-geoscience.md)).
- **Recomputation after failures** is fixed by checkpointing and by completion tracking
  ([22-02-03](../02-reproducible-workflows/03-workflow-managers.md) §5).

Sixty-five per cent of the bill lies in items that a faster solver does not touch, and
every one of them is a design decision made before the solver ran.

## 6. Practice: forecasting a project

A defensible forecast has five lines and one uncertainty statement.

1. **Work units.** State the number of independent units (realisations, events, tiles,
   stations-years) and the cost per unit, from a pilot rather than a guess.
2. **Compute line.** Units × core-hours per unit × $c_h$, plus the setup and merge work.
3. **Storage lines.** Raw, intermediate and published volumes, each with its retention
   in months, separated because they have different retention policies.
4. **Movement line.** Egress per pass × number of passes, and the number of passes
   should be one — every extra pass is a redesign opportunity.
5. **Failure line.** Expected recomputation volume = failure rate × unit cost × retry
   depth; a forecast without it is a forecast that will be exceeded.
6. **Uncertainty.** State which line is least certain and what measurement would narrow
   it; in practice this is almost always the per-unit cost, which is why the pilot is
   mandatory.

Then compare the forecast against a *recorded* bill after the first production run, and
revise. A forecast that is never compared to an invoice is a document, not a model.

## 7. Worked example: the run nobody objected to

A group runs a 32-core, 6-hour job weekly. The compute is modest; the job writes a 400 GB
intermediate to shared storage, which is read back by a visualisation service in a
different region. Nobody objects until the annual review, where the intermediate's storage
months and the cross-region reads are most of the project's infrastructure line, and 20
of the 52 weekly runs were rerun after interrupted transfers — the recomputation term. The
fixes are three sentences, none involving the solver: delete the intermediate after the
published product is built, run the visualisation where the data is, and write to a
durable location before transferring. The lesson is not that the group was careless; it is
that the compute number was visible in every meeting and the other three were not.

## Assumptions and regime of validity

- **Chosen unit prices.** All rates are teaching values; nothing here is a price quote and
  no provider's current prices are asserted.
- **Linear cost in time.** Storage billed per volume-month and compute per core-hour are
  linear; tiered, committed-use and spot pricing are not, and change the break-even.
- **The 2 % per-doubling efficiency loss is a model.** Real losses depend on the
  algorithm and the machine; the conclusion (cost per unit of work rises with size) is
  robust, the specific 19.5 % is not.
- **The serial fraction is measured on a pilot problem size.** It does not transfer
  unchanged to a different size ([22-06-02](./02-cloud-computing-research.md) §2).
- **Cost is not value.** A cheap result that is wrong, unused or unreproducible has no
  value; the cost model allocates resources, it does not judge the science.

## The honest summary

1. Compute the three terms — compute, storage, movement — before optimising any of them;
   in data-heavy work the compute is often the smallest.
2. Cost per unit of work rises with problem size even when the wall time does not;
   report both.
3. The break-even core count is set by the deadline and bounded by the serial floor; the
   marginal cost of the last halving is the largest.
4. Roughly two thirds of a data-heavy bill can be storage, movement and recomputation,
   and every one of those is a design decision.
5. A forecast must have a failure line and be compared against an invoice.
6. State the unit prices you assumed; the arithmetic is only as good as they are.

## Python demonstration

[`code/cost_and_scaling_demo.py`](./code/cost_and_scaling_demo.py) prints, with
`np.random.default_rng(20261014)`:

1. the three cost terms for a 64-core, 12-hour, 2 TB run — 38.4 + 480 + 180 = 698.4
   units, with storage and egress at 95 %;
2. the weak-scaling table above, with cost per unit of work rising from 38.40 to 45.89;
3. the deadline/cores break-even table, including the infeasible half-hour deadline and
   the 0.60 h serial floor;
4. the annual cost-share table, with 65 % of the bill outside compute.

```bash
cd 22-data-engineering-reproducibility/06-high-performance-and-cloud/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python cost_and_scaling_demo.py
```

## Exercises

Graded problems and worked solutions are in
[`exercises/03-cost-and-scaling-exercises.md`](./exercises/03-cost-and-scaling-exercises.md)
and
[`exercises/03-cost-and-scaling-solutions.md`](./exercises/03-cost-and-scaling-solutions.md).

## Mastery checkpoint

Without notes: a run takes 12 h on 64 cores, produces 2 TB, and the storage is kept one
year. Chosen rates: 0.05 per core-hour, 20 per TB-month, 90 per TB egress.

1. Compute the three cost terms and the total, and state the dominant one.
2. Compute the cost per unit of work if the same work is spread over 4 096 cores with a
   2 % efficiency loss per doubling.
3. Find the cores needed for a 3-hour deadline at $p = 0.05$, and the serial floor.
4. Name three cost lines that a faster solver does not reduce.

## Common pitfalls

1. **Forecasting compute only.** The 95 % figure above is the demonstration's answer to
   this habit.
2. **Keeping everything forever.** Retention is a decision; storage is billed per month.
3. **Reading data across regions in an inner loop.** It converts compute cost into egress
   cost and wall time.
4. **Assuming weak scaling is free.** The same work costs 19.5 % more at 32 768 cores than
   at 64 in the demonstration's model.
5. **Chasing a deadline below the serial floor.** No budget reaches it; change the
   algorithm or the deadline.
6. **Quoting a price without a date and a region.** Provider prices change; a cost slide
   without them is not defensible.
7. **No failure line in the forecast.** A 20-of-52 rerun record is not unusual and is
   exactly the term most forecasts omit.

## Where this is used

- **Allocation and grant requests** — the cost of the requested compute and storage,
  itemised: see
  [22-05-04 Research Data Management Plans](../05-collaboration-and-project-management/04-research-data-management-plan.md).
- **Choosing between a cluster and the cloud** — the same work costed both ways:
  see [22-06-01 Running Jobs on HPC Clusters and Schedulers](./01-cluster-jobs.md) and
  [22-06-02 Cloud Computing for Geophysical Computation](./02-cloud-computing-research.md).
- **Data architecture decisions** — retention, layout and co-location chosen on cost
  evidence: see
  [22-04-05 Cloud-Native Geoscience Data Access](../04-databases-and-large-data/05-cloud-native-geoscience.md).
- **Ensemble and Monte Carlo planning** — the cost of the next ensemble predicted from the
  last one: see
  [22-03-03 Data Pipelines and Provenance](../03-data-formats-and-engineering/03-data-pipelines.md).

## Related lessons

- [22-06-01 Running Jobs on HPC Clusters and Schedulers](./01-cluster-jobs.md) —
  utilization and the queue instead of a bill.
- [22-06-02 Cloud Computing for Geophysical Computation](./02-cloud-computing-research.md) —
  the speedup model this lesson prices.
- [22-03-02 Format Design and Trade-offs](../03-data-formats-and-engineering/02-format-design-tradeoffs.md) —
  format choice as a storage and I/O cost decision.
- [19-06 HPC and Parallel Computing](../../19-numerical-modeling-hpc/06-hpc-and-parallel-computing/README.md) —
  the algorithms that set the serial fraction.

## Self-assessment checklist

- [ ] I can write the three-term cost model and compute each term.
- [ ] I can compute the cost per unit of work under weak scaling.
- [ ] I can find the break-even core count and the serial floor.
- [ ] I can forecast a project's bill by item, with a failure line.
- [ ] I can name the cost lines that compute optimisation does not reduce.
- [ ] I can state the assumptions and the date/region limitation of any cost figure.
