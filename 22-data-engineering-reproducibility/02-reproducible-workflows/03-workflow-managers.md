---
id: 22-02-03
title: "Workflow Managers: Snakemake, Make, Dask, Prefect"
level: research
prereqs: ["22-02-02", "22-02-01"]
estimated_minutes: 50
tags: [workflows, scheduling, caching, snakemake, make, dask, research-practice]
---

# Workflow Managers: Snakemake, Make, Dask, Prefect

## Learning objectives

By the end of this lesson you will be able to:

1. **Represent** an analysis as a directed acyclic graph of rules with declared
   inputs and outputs, and **explain** why declaration is the enabling mechanism.
2. **Compute** a workflow's serial cost, critical path and maximum available
   speedup, and **interpret** each.
3. **Predict** the makespan of a DAG on a given number of workers, and **explain**
   why efficiency falls with worker count even when the graph is embarrassingly
   parallel in parts.
4. **Apply** a dependency-aware invalidation rule and **compute** the fraction of
   a workflow that re-runs when an input changes.
5. **Choose** between a file-based rule engine, a dataflow framework and a
   task-orchestration service for a stated requirement, and **justify** the choice
   by the failure it prevents.
6. **Separate** the cost of a workflow from its speed, and **report** core-hours
   alongside wall time.

All workflow numbers in this lesson are **SYNTHETIC**: the task graph, durations
and input sets are generated with chosen parameters, and the scheduler is a
greedy list scheduler implemented in the demonstration. No workflow engine was run
and no benchmark of a real system is quoted.

## Prerequisites

- [22-02-02 Pinning Environments and Managing Dependencies](./02-environment-pinning.md) —
  what each rule executes inside.
- [22-02-01 The Reproducibility Problem in the Computational Sciences](./01-reproducibility-crisis.md) —
  manual steps as a failure category.

## 1. Intuition: the workflow manager's job is invalidation

A human running an analysis by hand makes two decisions repeatedly: *what to run
next* and *what can be skipped*. The second is the hard one, and it is where
errors enter. A workflow manager exists to make it automatic and correct: each
piece of work declares what it consumes and what it produces, and the tool decides
what is out of date.

That reframes the tool choice. Engines differ in syntax, in language support and
in where they run, but they all answer the same question — *is this output
consistent with its declared inputs?* The answer is only as good as the
declarations. A rule that reads a file it did not declare **will not be re-run**
when that file changes, and the workflow will silently produce a stale result with
no error. This single failure mode is the reason declaration discipline, not
engine features, is the skill being taught here.

## 2. The model: rules, targets and a DAG

A workflow is a set of **rules**. Each rule has a name, declared inputs, declared
outputs, a command, and optionally resources (threads, memory, wall time). A
target is an output someone asked for; the engine resolves it backwards through
the rules to build a DAG, then executes it in dependency order.

The properties that follow from this design, and that matter in practice:

- **Partial execution.** Asking for one figure runs only its ancestors.
- **Parallelism.** Tasks with no path between them can run at the same time; the
  engine schedules them, not the user.
- **Invalidation.** An output is stale if its inputs changed, or if the rule
  changed, or if the output is missing.
- **Retries and logs.** A failure is attributed to one rule, and its log is the
  unit of diagnosis.
- **Idempotence requirement.** A rule must behave the same whether or not its
  previous output exists; a rule that appends to a file violates this and produces
  different results on a re-run.

## 3. Choosing among the families

| Family | Examples | Fits when | Characteristic failure |
|---|---|---|---|
| File-based rule engines | Make, Snakemake, Nextflow | the analysis is a set of files derived from files | a rule with an undeclared input silently does not re-run |
| Dataflow / array frameworks | Dask, Spark-like engines | one operation applies to a large collection, out of core | a task graph larger than the scheduler's memory, or a hidden shuffle |
| Orchestration services | Prefect, Airflow, workflow schedulers | heterogeneous steps, retries, schedules, external systems | the same code produces different results because the service's environment is not the analysis's environment |

The three families are not ranked: a Dask graph cannot express "this figure
depends on that parameter file" as naturally as a rule engine, and a rule engine
is a poor way to express a 10 TB array reduction. The lesson's measurements below
are properties of the **file-based rule** model, which is what most geophysical
pipelines are.

## 4. Serial cost, critical path and the speedup ceiling

For a DAG with task durations $d_i$, two quantities bound the wall time:

$$C_{\text{serial}} = \sum_i d_i, \qquad
C_{\text{crit}} = \text{longest path} \sum_{i \in P} d_i.$$

$C_{\text{serial}}$ is the time on one core with no parallelism; $C_{\text{crit}}$
is the floor for any number of workers, because the tasks on the critical path
cannot overlap. Their ratio is the **maximum available speedup**:

$$S_{\max} = \frac{C_{\text{serial}}}{C_{\text{crit}}}.$$

For the demonstration's SYNTHETIC workflow — 24 tasks, 40 dependencies, durations
drawn uniformly in $[2,25]$ minutes — the measurements are

$$C_{\text{serial}} = 383.4\ \text{min}, \qquad
C_{\text{crit}} = 137.4\ \text{min}, \qquad S_{\max} = 2.79.$$

So no amount of parallelism makes this workflow run faster than 2.79 times its
serial time, and that ceiling is a property of the analysis, not of the cluster.
Extending a pipeline with a chain of dependent steps lowers $S_{\max}$; splitting a
long step into independent pieces raises it.

## 5. Scheduling: what workers actually buy

With $W$ workers and a greedy list schedule (largest task first among those whose
dependencies are complete, each task starting when both its predecessors and a
worker are free), the demonstration measures

| Workers | Makespan (min) | Speedup | Efficiency |
|---|---|---|---|
| 1 | 383.4 | 1.00 | 1.00 |
| 2 | 203.8 | 1.88 | 0.94 |
| 4 | 162.2 | 2.36 | 0.59 |
| 8 | 137.4 | 2.79 | 0.35 |

Three observations. First, the makespan at 8 workers is exactly the critical path
(137.4 min) and exactly the ceiling $S_{\max} = 2.79$: for this graph, more than
eight workers cannot shorten the run at all, and the 4-worker row already reaches
2.36 of the available 2.79. Second, efficiency falls steeply — 0.94 at two workers,
0.35 at eight — because the schedule is bounded by a chain that most workers must
wait behind. Third, the practical worker count for this workflow is two or four;
the correct number is the one where the wall time still falls meaningfully, not
the largest the cluster will give you.

## 6. Caching: the fraction that re-runs

The value of a workflow manager in daily work is not the parallel speedup; it is
that an edit re-runs a small part of the pipeline. With a dependency-aware rule —
a task re-runs if any of its declared inputs changed, and every descendant of a
re-run task re-runs — the demonstration's SYNTHETIC model (24 tasks, each reading
one to three of six inputs, averaged over 200 draws) measures:

| Inputs changed | Tasks re-run (mean) | Fraction of the workflow |
|---|---|---|
| 1 of 6 | 15.0 | 62 % |
| 2 of 6 | 19.7 | 82 % |
| 3 of 6 | 21.9 | 91 % |
| 6 of 6 | 24.0 | 100 % |

Read that table as a warning about **fan-out of inputs**: in this graph a single
changed input forces 62 % of the tasks to re-run, because the input feeds a task
near the root and everything downstream depends on it. The measured numbers are
properties of the generated graph's shape, and the design lesson generalises:
caching pays when the graph is *wide near the target* and *narrow near the
inputs*, so a change to an input touches a small downstream cone. A pipeline that
reads every input into one giant first step has a cache that invalidates
everything, and its wall time on an edit is the full serial cost.

## 7. Cost is not speed

Scheduling faster can cost more. For the demonstration's workflow on 4 workers:

$$C_{\text{core-time}} = \frac{383.4}{60} = 6.39\ \text{core-hours}, \qquad
\text{wall} = \frac{162.2}{60} = 2.70\ \text{h},$$

and the idle allocation is

$$4 \times 2.70 - 6.39 = 4.41\ \text{core-hours} = 41\ \%\ \text{of the allocation}.$$

The two numbers answer different questions: 2.70 h is what the user waits, 6.39
core-hours is what the project buys. Here the 4-worker allocation is idle for
41 % of its time, because the critical path forces three of the four workers to
wait; the same wall time is achievable on two workers with a much better
allocation. On a shared cluster the core-hours are the quantity that has to be
justified, and a workflow with $S_{\max} = 2.79$ cannot use more than about three
cores productively no matter how many are requested. Report both numbers, and
state the wall-time constraint that motivated the request.

## 8. Practice: what makes a workflow trustworthy

1. **Declare every input.** A read of an undeclared file is an invisible
   dependency; if the engine cannot see it, it cannot invalidate on it.
2. **One rule, one transformation.** A rule that both filters and inverts cannot
   be re-used and cannot be tested in isolation.
3. **Make rules idempotent.** Overwrite outputs rather than appending; a re-run
   must produce the same file.
4. **Pin the environment per rule.** The rule's interpreter, library versions and
   container are part of the rule: see
   [22-02-02](02-environment-pinning.md).
5. **Record seeds as parameters.** Randomness in a rule is an input; an unrecorded
   seed makes the rule a different function on every run.
6. **Run `--dry-run` before submitting.** It is the cheapest check that the graph
   resolves and that the targets are what you think.
7. **Keep provenance with the outputs.** Log the rule, the inputs, the environment
   and the exit status alongside each artefact; a workflow that cannot say what
   produced a file has only moved the ambiguity.

## 9. Worked example: halving a 6-hour pipeline

A group's pipeline takes 6 hours on one core and they want 1 hour. Work through
the arithmetic before requesting hardware:

1. **Measure the critical path.** If the chain of dependent steps totals 5 h,
   $S_{\max} = 6/5 = 1.2$ and the target is unreachable by any cluster: the
   analysis must be restructured, for example by running four profiles as
   independent rules instead of one sequential loop.
2. **Check the input fan-out.** If every rule reads the merged catalogue, an edit
   to the catalogue re-runs 100 % of the workflow; splitting the catalogue by
   region restores partial invalidation.
3. **Choose the worker count from the makespan curve.** Add workers while the
   wall time still falls meaningfully; the demonstration's graph gains 1.9$\times$
   from 4 to 8 workers and would gain far less beyond that.
4. **Report the cost.** Six core-hours on one core versus, say, 2 h wall on four
   cores at 8 core-hours of allocation: the wall-time gain costs extra allocation,
   and a group that asks for 40 cores for the same graph buys a long queue and
   almost no wall-time gain.

The order matters: restructuring the graph changes $S_{\max}$, which is the
quantity that decides whether more workers can help at all.

## Assumptions and regime of validity

1. **Known, static durations.** The model uses fixed task durations; real tasks
   vary with input size and contention, and a scheduler that plans on estimates
   is only as good as those estimates.
2. **A greedy list schedule.** Makespans are for largest-first list scheduling,
   which is a good heuristic and not optimal; a different scheduler changes the
   numbers by a few per cent.
3. **Unlimited memory and no queueing.** The model has no cluster queue, no memory
   ceiling and no failure; a real cluster's wait time can dominate the makespan.
4. **Exact invalidation.** The caching table assumes the invalidation rule is
   correct and complete; a rule with an undeclared input re-runs *less* than the
   table and is silently wrong instead.
5. **Uniform input fan-out.** The measured re-run fractions are properties of the
   generated graph; a graph with a different shape has different fractions, and the
   lesson reports the shape, not a universal constant.

## The honest summary

A workflow manager is an invalidation engine: it re-runs what changed and skips
what did not. Its ceiling is the critical path, not the cluster — 383.4 minutes of
serial work with a 137.4-minute critical path caps the speedup at 2.79 for the
demonstration's graph — and the measured schedule reaches speedups of 1.88, 2.36
and 2.79 on 2, 4 and 8 workers at efficiencies of 0.94, 0.59 and 0.35, hitting the
ceiling exactly at eight workers. Its daily value is partial re-execution, which in
the modelled graph re-runs 62 % of the workflow when one of six inputs changes, a
number set by input fan-out rather than by the engine. And its cost is core-hours,
reported separately from wall time: 2.70 h at 6.39 core-hours with 41 % of a
four-worker allocation left idle. The skill is in the declarations: a workflow is
only as correct as the inputs its rules admit to reading.

## Python demonstration

[`code/workflow_managers_demo.py`](./code/workflow_managers_demo.py) generates the
24-task graph with `np.random.default_rng(20261014)` and prints, under four
numbered banners:

1. serial cost (383.4 min), critical path (137.4 min) and the 2.79$\times$ ceiling;
2. the makespan, speedup and efficiency table for 1, 2, 4 and 8 workers;
3. the re-run fraction after 1, 2, 3 and 6 of 6 inputs change (62 %, 82 %, 91 %,
   100 %, averaged over 200 draws);
4. core-hours versus wall time, with the idle share of the allocation (41 %).

```bash
cd 22-data-engineering-reproducibility/02-reproducible-workflows/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python workflow_managers_demo.py
```

## Exercises

Graded problems and worked solutions are in
[`exercises/03-workflow-managers-exercises.md`](./exercises/03-workflow-managers-exercises.md)
and
[`exercises/03-workflow-managers-solutions.md`](./exercises/03-workflow-managers-solutions.md).

## Mastery checkpoint

Without notes: a workflow has five rules, $A \to B \to C$ with durations 10, 20
and 30 minutes, plus $D$ (15 min) and $E$ (40 min) independent of them.

1. Compute the serial cost, the critical path and the maximum speedup.
2. Compute the makespan on 2 workers by hand, and state whether the efficiency is
   above or below the demonstration's 2-worker value of 0.94.
3. A change to $A$'s input affects $B$ and $C$ but not $D$ or $E$. State the
   fraction of the workflow that re-runs and how a designer could have made it
   smaller.
4. State what a rule engine cannot tell you about the analysis it runs.

## Common pitfalls

1. **Undeclared inputs.** The engine cannot invalidate on a dependency it cannot
   see, and the failure is a stale result with no error message.
2. **Adding workers past the critical path.** Beyond $S_{\max}$ the only effect is
   a larger allocation.
3. **Sampling every rule from one giant node.** A single root input makes the
   cache useless: 62 % of the modelled workflow re-runs on a one-input edit.
4. **Reporting wall time only.** Core-hours are the resource a cluster bills;
   1.73 h at 6.39 core-hours with 8 % idle is the honest report.
5. **Orchestrating with a service whose environment differs from the analysis.**
   The engine records success while the numbers come from a different environment.
6. **Non-idempotent rules.** A rule that appends produces a different result on a
   re-run, which breaks both caching and repeatability.

## Where this is used

- **Standard geophysical processing chains** — read, quality-control, filter,
  invert, plot — are file-to-file DAGs by nature.
- **Ensemble and inversion studies** — one rule per realisation is the difference
  between a re-runnable study and a shell loop.
- **Cluster and cloud submission** — schedulers consume the DAG and the resource
  declarations: see
  [22-06-01 Running Jobs on HPC Clusters and Schedulers](../06-high-performance-and-cloud/01-cluster-jobs.md).
- **Continuous integration of an analysis** — running the DAG on a reduced input
  is how a change is validated end to end: see
  [22-07-02 Continuous Integration for Research Software](../07-software-testing-quality/02-continuous-integration.md).

## Related lessons

- [22-02-04 Notebooks vs Pipelines: Choosing the Right Tool](./04-notebooks-vs-pipelines.md) —
  when the ordering should be fixed by a tool and when exploration justifies a
  session.
- [22-02-05 Data Versioning and Provenance Tracking](./05-data-versioning.md) —
  the identifiers the rules consume and record.
- [19-06 HPC and Parallel Computing](../../19-numerical-modeling-hpc/06-hpc-and-parallel-computing/README.md) —
  the parallel algorithms and their scaling laws.
- [22-06-03 Cost, Scaling and Practical Efficiency](../06-high-performance-and-cloud/03-cost-and-scaling.md) —
  the same core-hours arithmetic at the level of a project budget.

## Self-assessment checklist

- [ ] I can express an analysis as rules with declared inputs and outputs.
- [ ] I can compute serial cost, critical path and maximum speedup.
- [ ] I can predict a makespan on $W$ workers for simple graphs.
- [ ] I can apply a dependency-aware invalidation rule.
- [ ] I can choose a workflow family for a stated requirement.
- [ ] I can report core-hours and wall time separately.
