---
id: 25-06-02
title: "Capstone: Proposal, Literature Review and Methods Plan"
level: research
prereqs: ["25-06-01", "22-05-01", "22-01-04", "25-05-05"]
estimated_minutes: 260
tags: [capstone, research-proposal, project-management, literature-review, research]
---

# Capstone: Proposal, Literature Review and Methods Plan

## Learning objectives

By the end of this lesson you will be able to:

1. **Turn** a design brief into a proposal with a work breakdown, a methods plan and a
   risk register.
2. **Schedule** the work with three-point estimates and **compute** the critical path,
   the total slack of every task and the expected duration.
3. **Show** why the sum of the task durations is not the project duration, and why the
   difference is the whole content of a schedule.
4. **Sample** the schedule to obtain the probability of meeting a deadline and the
   tasks that actually drive the finish date.
5. **Evaluate** a proposed schedule repair on the same simulated schedules and
   **choose** the repair with the best return per unit of effort.
6. **Write** a literature review that produces four outputs: the gap, the numbers you
   will reuse, the methods you will not use and why, and the comparison your result
   will be tested against.
7. **Specify** a methods plan whose validation step precedes the production run.

## Prerequisites

- [25-06-01 Capstone: Designing an Original Research Study](./01-capstone-design.md) —
  the brief this lesson turns into a plan.
- [22-05-01 Structuring a Research Project](../../22-data-engineering-reproducibility/05-collaboration-and-project-management/01-project-structure.md) —
  the repository practices a plan is implemented with.
- [22-01-04 Writing Documentation for Research Code](../../22-data-engineering-reproducibility/01-research-software-engineering/04-documentation.md) —
  where the methods plan lives after the proposal is accepted.
- [25-05-05 Project: Reproducing a Published Result](../05-doctoral-projects/05-reproduce-published-result.md) —
  how to read a paper for the numbers you will reuse.

## 1. The question

*Will the study finish, and does the proposal say what will be done before it is done?*

A proposal is judged on two things that are usually missing from student proposals: a
**schedule with a critical path** and a **methods plan whose validation step comes
first**. The demonstration writes a 12-task work breakdown for the ambient-noise study
of [25-06-01](./01-capstone-design.md) and analyses it:

| measure | value |
|---|---|
| sum of the expected task durations | 33.7 weeks |
| **critical path** (deterministic) | 8 tasks, 24.50 weeks |
| Monte Carlo mean | 25.31 weeks (sd 1.38) |
| P50 / P80 / P90 | 25.30 / 26.48 / 27.12 weeks |
| P(finish within the 24-week budget) | **17.3%** |
| best repair found | trim the three longest tasks by 25%: 22.31 weeks, 92.1% |

Two results carry the lesson. First, **the sum of the task durations (33.7 weeks) is
38% longer than the schedule (24.5 weeks)**: tasks run in parallel, and only the
longest path through the dependency graph determines the finish date. A proposal that
adds up its task list has not scheduled anything. Second, **the deterministic critical
path is exactly at the budget (24.50 weeks) while the realistic plan has a 17.3%
chance of meeting it** — because path lengths fluctuate and the critical path switches.

## 2. Three-point estimates and the critical path

Each task gets an optimistic $o$, a most likely $m$ and a pessimistic $p$, giving

$$E = \frac{o + 4m + p}{6},\qquad \mathrm{sd} = \frac{p-o}{6},$$

the PERT conventions. The demo's estimates:

| # | task | predecessors | $o$ | $m$ | $p$ | $E$ | sd |
|---|---|---|---|---|---|---|---|
| 1 | literature review | — | 2 | 3 | 4 | 3.00 | 0.33 |
| 2 | data request and QC | 1 | 1 | 2 | 4 | 2.17 | 0.50 |
| 3 | method test on synthetic | 1 | 2 | 3 | 4 | 3.00 | 0.33 |
| 4 | processing pipeline | 2, 3 | 3 | 4 | 6 | 4.17 | 0.50 |
| 5 | inversion runs | 4 | 2 | 3 | 5 | 3.17 | 0.50 |
| 6 | sensitivity analysis | 5 | 1 | 2 | 3 | 2.00 | 0.33 |
| 7 | uncertainty quantification | 5 | 2 | 3 | 4 | 3.00 | 0.33 |
| 8 | figures | 6, 7 | 1 | 2 | 3 | 2.00 | 0.33 |
| 9 | manuscript draft | 8 | 3 | 4 | 6 | 4.17 | 0.50 |
| 10 | internal review and revision | 9 | 1 | 2 | 3 | 2.00 | 0.33 |
| 11 | code release and docs | 4 | 2 | 3 | 4 | 3.00 | 0.33 |
| 12 | defence preparation | 9 | 1 | 2 | 3 | 2.00 | 0.33 |

**The forward pass.** Earliest finish $\mathrm{EF}_i = \max_{j \in
\text{pred}(i)} \mathrm{EF}_j + E_i$; the project duration is
$\max_i \mathrm{EF}_i$. **The backward pass** gives the latest finish
$\mathrm{LF}_i = \min_{j \in \text{succ}(i)} (\mathrm{LF}_j - E_j)$, and
**total slack** $= \mathrm{LF}_i - \mathrm{EF}_i$. The demo's result:

| task | earliest finish | total slack | on the path? |
|---|---|---|---|
| literature review | 3.00 | 0.00 | critical |
| data request and QC | 5.17 | 0.83 | |
| method test on synthetic | 6.00 | 0.00 | critical |
| processing pipeline | 10.17 | 0.00 | critical |
| inversion runs | 13.33 | 0.00 | critical |
| sensitivity analysis | 15.33 | 1.00 | |
| uncertainty quantification | 16.33 | 0.00 | critical |
| figures | 18.33 | 0.00 | critical |
| manuscript draft | 22.50 | 0.00 | critical |
| internal review and revision | 24.50 | 0.00 | critical |
| code release and docs | 13.17 | 11.33 | |
| defence preparation | 24.50 | 0.00 | critical |

Total slack is the delay a task can absorb without moving the finish date, and it is
the only number in a schedule that tells you where to spend attention. **Data request
and QC has 0.83 weeks of slack** — it must not slip more than four working days, and
it is *not* obviously on the "important" path to the reader who looks at the task
list. Sensitivity analysis has 1.00 week; code release has 11.33. The critical tasks
are the eight above plus defence preparation: everything else can be late, and
almost-nothing-else can.

**Why the path, not the sum.** The sum (33.7 weeks) counts tasks that share calendar
time: the code release runs alongside the inversions, and the sensitivity analysis runs
alongside the uncertainty quantification. The critical path (24.5 weeks) is the longest
chain of dependencies, and it is the only quantity that propagates to the deadline.
A proposal whose schedule is the sum of its parts is a proposal that has allocated
38% more time than it needs — or that has not noticed its own parallelism.

## 3. The schedule is a distribution, not a date

Sampling every task from its triangular distribution and recomputing the longest path
$20\,000$ times gives

| percentile | weeks |
|---|---|
| P10 | 23.55 |
| P50 | 25.30 |
| P80 | 26.48 |
| P90 | 27.12 |
| P95 | 27.62 |

with mean $25.31$ and sd $1.38$, and $P(\le 24\ \text{weeks}) = 17.3\%$. The
deterministic critical path was 24.50 weeks — **so the "expected" plan has a 17% chance
of hitting its own deadline.** Two mechanisms cause this:

1. **Path switching.** When the pipeline or the draft takes a pessimistic draw, the
   critical path moves through a different chain; the expected longest path is longer
   than the longest path of the expected durations. The Monte Carlo mean exceeds the
   deterministic path by $0.81$ weeks, and the gap grows with the number of
   near-critical parallel paths.
2. **The distribution is skewed.** The PERT mean already sits above the mode, and the
   right tail is long, so the P80 and P90 are further out than the sd alone suggests.

**The driver analysis** is what a risk register should be built from, not from
imagination. The correlation of each task's duration with the project finish is

| task | correlation with finish | on critical path |
|---|---|---|
| manuscript draft | $0.453$ | 100% |
| processing pipeline | $0.452$ | 100% |
| inversion runs | $0.447$ | 100% |
| literature review | $0.294$ | 100% |
| figures | $0.289$ | 100% |

All five are on the critical path in every simulated schedule, and the draft and the
pipeline are almost equally important. **The task with the highest correlation is not
necessarily the one with the largest estimate** (the draft and the pipeline both
estimate 4.17 weeks; the review at 2.33 weeks matters less), and a risk register that
lists only the largest tasks has missed the mechanism.

## 4. Repairing the schedule

Two candidate repairs, evaluated on the same $20\,000$ schedules:

| repair | mean finish | $P(\le 24$ weeks$)$ | cost |
|---|---|---|---|
| baseline | 25.31 | 17.3% | — |
| A: trim the three longest tasks by 25% | 22.31 | 92.1% | real effort |
| B: start the synthetic method test at week 0 (remove the dependency) | 24.56 | 36.0% | **none** |

Repair B is free: the method test does not actually need the literature review to be
finished, and starting it at week 0 removes $0.75$ weeks from the expected finish
without any additional work. It is worth $18.7$ percentage points of deadline
probability for no cost. Repair A buys $74.8$ points and costs a quarter of the effort
of the three biggest tasks — probably out of reach, which is exactly why B should be
found first. **The cheapest schedule improvement is usually a dependency that need not
exist, and the analysis that finds it is the backward pass, not goodwill.**

This is the sense in which a schedule is a research product: it identifies the
specific claim in the plan ("the processing pipeline cannot start until the data are
cleaned") that is doing the damage, and it quantifies what removing it is worth.

## 5. The literature review, defined by its outputs

A literature review is not a summary; it is four deliverables:

1. **The gap**, stated as the specific missing number, model or test — not "few
   studies have examined X" but "no published dispersion curve exists for this basin
   below 4 s period, so the shallow $V_s$ is unconstrained".
2. **The numbers you will reuse**, each with its source and its definition of
   uncertainty. A scatter taken from a paper as "$0.3$" is useless unless you know
   whether it is a standard deviation, a standard error, a 95% interval or a range; the
   power calculation of [25-06-01](./01-capstone-design.md) turns on that distinction.
3. **The methods you will not use, with the reason** — a paragraph that saves a
   referee's question and your own weeks. "Full-waveform inversion is not attempted
   because the source wavelet is unknown and the survey is a single 2-D line."
4. **The comparison your result will be tested against**: the published value, its
   uncertainty, and the reason your study's precision is different. Without this, the
   write-up cannot distinguish agreement from a coincidence.

Two habits keep the review honest: read the *figures and methods* before the abstract
(the abstract's numbers often come from a different model run), and record every
number you intend to reuse in a file with its provenance as you read, not afterwards.

## 6. The methods plan

Numbered, in execution order, with the validation step **before** the production run:

1. **Data acquisition and QC** — query, filters, thresholds, resulting count, and the
   completeness or detection-time check.
2. **Forward model / synthetic validation** — the method run on a synthetic dataset
   with a known answer, with the acceptance criterion stated *before* it is run
   ("recovers the input within one standard error", "gradient matches finite
   differences to $10^{-6}$"). This is the step that fails early and cheaply.
3. **Processing pipeline**, with the parameters that are not determined by the data
   listed and given a default and a sensitivity range.
4. **Inversion or estimation**, with the objective, the regularisation and its rule.
5. **Sensitivity and uncertainty analysis** — at minimum, the response of the headline
   number to each choice made in steps 2–4.
6. **Comparison with the literature** — the number from the review's output (4), in its
   own uncertainty units.
7. **Deliverables** — the artefact, its resolution or uncertainty, and the code release.

Each step ends in a **milestone** with a binary state (done or not), because a plan
whose milestones are "mostly complete" has no milestones. The two milestones that
matter most are "synthetic validation passes" and "headline number obtained": if the
first slips, the rest is speculation, and it is the one step the schedule must protect.

## 7. Failure modes

1. **A schedule that is the sum of the tasks.** $33.7$ vs $24.5$ weeks on this
   breakdown; the difference is the proposal's credibility.
2. **A single-date deadline with no distribution.** The deterministic path meets the
   24-week budget exactly and delivers a $17.3\%$ chance of success.
3. **A risk register built from the largest tasks** rather than from the finish-date
   correlations.
4. **Parallelism assumed but not scheduled.** If two tasks are "done in parallel" by
   one person, they are on the same path and the schedule must say so.
5. **A literature review that cites rather than quantifies** — no gap, no reusable
   numbers, no rejected methods, no comparison value.
6. **A methods plan whose validation step is last.** Then the discovery that the method
   does not work arrives when there is no time to change it.
7. **Slack not reported.** A task with $0.83$ weeks of slack and a task with $11.33$
   weeks look identical in a task list.

## 8. Rubric

| Criterion | Weight | Full marks |
|---|---|---|
| Work breakdown with dependencies and three-point estimates | 20% | every task has o/m/p and its predecessors |
| Schedule analysis | 25% | critical path, slack per task, and the sum-versus-path point made |
| Deadline probability and drivers | 20% | Monte Carlo percentile table and finish-date correlations |
| Repairs evaluated | 15% | at least one free dependency repair, quantified |
| Literature review outputs | 10% | gap, reusable numbers with uncertainty definitions, rejected methods, comparison value |
| Methods plan with validation first | 10% | numbered steps, validation before production, milestones binary |

## 9. The honest summary

The product of this lesson is a plan whose arithmetic is visible: a 12-task breakdown
whose sum is 33.7 weeks and whose critical path is 24.5 weeks, a deadline met in
17.3% of simulated schedules, a finish date driven by the manuscript draft and the
processing pipeline (correlations $0.45$), and a free repair — removing one dependency
— worth $18.7$ percentage points. The transferable results are that a proposal's
schedule is a distribution and not a date, that the cheapest improvement is usually a
dependency that need not exist, and that a literature review earns its place by
producing four specific outputs, none of which is a summary.

## Python demonstration

[`code/capstone_proposal_demo.py`](./code/capstone_proposal_demo.py) prints every number
above: the breakdown with PERT estimates, the forward and backward passes with slack,
the Monte Carlo percentiles and deadline probability, the finish-date correlations, and
the two evaluated repairs.

```bash
cd 25-projects-capstone/06-capstone-research/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python capstone_proposal_demo.py
```

Print-only, seeded with `np.random.default_rng(20261014)`, no network, no files, no
plots, exits 0, runs in about $1$ s.

## Exercises

Graded problems and worked solutions are in
[`exercises/02-capstone-proposal-exercises.md`](./exercises/02-capstone-proposal-exercises.md)
and
[`exercises/02-capstone-proposal-solutions.md`](./exercises/02-capstone-proposal-solutions.md).
The ★★★ item asks you to re-plan a slip: a single task overruns and you must find the
cheapest way to protect the deadline.

## Mastery checkpoint

Without notes:

1. Compute the PERT expected duration and sd for $o = 2$, $m = 3$, $p = 7$.
2. Perform a forward and backward pass on a three-task chain and state each task's
   slack.
3. Explain why the Monte Carlo mean exceeds the deterministic critical path.
4. State why the sum of the task durations is not the project duration.
5. Name the four outputs of a literature review.

## Common pitfalls

1. Reporting a schedule as a list of durations with no dependency graph.
2. Assuming a person can execute two parallel tasks at once.
3. Estimating $p$ as the "worst case" without asking what the worst case really is.
4. Scheduling the validation step last.
5. Treating slack as unimportant because the task looks small.

## Where this is used

Every remaining capstone lesson works from this plan: the
[execution](./03-capstone-execution.md) tracks it, the
[write-up](./04-capstone-writeup.md) reports against it, and the
[defence](./05-capstone-defence.md) asks what slipped and why. The scheduling
arithmetic itself is the standard project-management tool of any research programme,
from a field campaign to a multi-year consortium: the tasks change, the critical path
does not.

## Related lessons

- [22-05-01 Structuring a Research Project](../../22-data-engineering-reproducibility/05-collaboration-and-project-management/01-project-structure.md) —
  the repository in which the plan becomes issues and milestones.
- [25-06-01 Capstone: Designing an Original Research Study](./01-capstone-design.md) —
  the brief and the power calculation the plan must deliver.
- [25-05-05 Project: Reproducing a Published Result](../05-doctoral-projects/05-reproduce-published-result.md) —
  reading a paper for its numbers, uncertainties and method choices.
- [25-06-03 Capstone: Data, Modelling and Uncertainty Analysis](./03-capstone-execution.md) —
  executing the methods plan, with the verification steps it specifies.

## Self-assessment checklist

- [ ] I can build a work breakdown with dependencies and three-point estimates.
- [ ] I can compute the critical path and each task's total slack.
- [ ] I can simulate a schedule and report the deadline probability.
- [ ] I can identify the finish-date drivers rather than the largest tasks.
- [ ] I can find and quantify a free dependency repair.
- [ ] I can state the four outputs of my literature review.
