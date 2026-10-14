---
id: 22-05-02
title: "Issue Tracking, Milestones and Kanban for Research"
level: intermediate
prereqs: ["22-05-01", "22-02-03"]
estimated_minutes: 45
tags: [project-management, kanban, queueing, collaboration]
---

# Issue Tracking, Milestones and Kanban for Research

## Learning objectives

By the end of this lesson you will be able to:

1. **Apply** Little's law to a research queue, and **compute** the lead time implied
   by a work-in-progress level and an arrival rate.
2. **Measure** a cycle-time distribution, and **explain** why the mean misleads when
   the distribution has a tail.
3. **Separate** work time from queueing time, and **compute** how a WIP limit moves
   the lead-time percentile people plan with.
4. **State** what a WIP limit cannot do — create capacity — and **compute** the
   backlog growth when demand exceeds capacity.
5. **Design** an issue tracker's fields so that progress is measurable, and **name**
   the fields that turn a tracker into a report.
6. **Measure** where cycle time goes, and **identify** the waits that a milestone
   should record.

The arrival rate, service times and congestion model in this lesson are
**SYNTHETIC** with chosen parameters. No issue tracker was read and no team was
observed; the queueing arithmetic is exact for the stated model.

## Prerequisites

- [22-05-01 Project Directory Structure and Conventions](./01-project-structure.md) —
  the artefact the work produces.
- [22-02-03 Workflow Managers: Snakemake, Make, Dask, Prefect](../02-reproducible-workflows/03-workflow-managers.md) —
  the same queueing logic applied to tasks instead of people.

## 1. Intuition: a research queue is a queue

Research work is often described as unmeasurable, and individual creativity is; the
*flow* of work is not. Items arrive (questions, data requests, review tasks), they
wait, they are worked on, and they finish. That structure is a queue, and queueing
theory applies with one modification: the service times are heavy-tailed, because a
task can be a two-hour fix or a six-month modelling effort.

Two quantities decide what people experience: **how many items are in progress** and
**how fast items arrive**. Neither is a moral judgement, and together they determine
the lead time.

## 2. Little's law and the implied lead time

For a stable system,

$$\text{WIP} = \text{throughput} \times \text{lead time},$$

so with a fixed arrival rate the lead time is proportional to the work in progress.
The demonstration's **SYNTHETIC** team receives 6 issues per week (1.2 per working
day):

| WIP (items in progress) | Implied lead time (days) |
|---|---|
| 2 | 1.7 |
| 6 | 5.0 |
| 12 | 10.0 |
| 24 | 20.0 |

The law explains a familiar complaint: the work did not get slower, there is simply
more of it open at once. It also makes the WIP limit the primary control: capping the
number of open items shortens *every* item's wait, whereas adding people does not
change the arrival rate.

## 3. The work distribution, and why the mean misleads

The second component is the work itself. The demonstration models 5 000 issues with a
lognormal work time (median 9 days):

| Percentile of work time | Days |
|---|---|
| 50th | 8.9 |
| 75th | 18.8 |
| 90th | 36.4 |
| 99th | 106.3 |
| mean | 16.1 |
| maximum | 694.7 |

The mean (16.1 days) is **1.8× the median**, and the 99th percentile is twelve times
the median. Consequences for planning and for reporting:

- a plan built on the median will be met by half the items and missed by the other
  half; a plan built on the mean still misses the tail that people remember;
- **the tail is where the reputation lives**: a single six-month item defines the
  collaboration's memory of the project;
- the tracker's report should therefore quote a percentile (the 85th or 90th), not a
  mean, because the percentile is what a user of the queue experiences.

## 4. Lead time as work plus queueing

Combining the two components gives the quantity a user actually experiences:

$$\text{lead time} = \text{work time} + \frac{\text{WIP}}{\text{throughput}} .$$

| WIP | Queueing (days) | Median lead (days) | 90th percentile lead (days) |
|---|---|---|---|
| 2 | 1.7 | 10.5 | 38.1 |
| 6 | 5.0 | 13.9 | 41.4 |
| 12 | 10.0 | 18.9 | 46.4 |
| 24 | 20.0 | 28.9 | 56.4 |

The 90th percentile of lead time is **1.5× larger at WIP 24 than at WIP 2**, while
the throughput is unchanged (the team is not the bottleneck). That is the honest
content of a WIP limit: it does not make the team faster, it makes the *queue* short
by refusing to start work that cannot be finished soon. The price is visible too —
items wait in a backlog instead of in progress — which is exactly the information a
research group usually lacks.

## 5. What a WIP limit cannot do

If arrivals exceed capacity, the backlog grows without bound and the lead time with
it. The demonstration's arithmetic (capacity 12 issues/week):

| Arrivals/week | Backlog change per week | Consequence |
|---|---|---|
| 6 | drains by 6 | a limit only shortens the queue |
| 12 | stable | a limit redistributes waiting, not capacity |
| 18 | grows by 6 (312/year) | lead time grows without bound; the limit makes it visible |

So a WIP limit is a **visibility and priority tool**, not a capacity tool. Above
capacity, the only options are to reduce the arrival rate (say no, defer, batch), to
increase capacity, or to accept a growing backlog — and the tracker's job is to make
that choice explicit rather than letting it hide inside everyone's in-progress list.

## 6. Tracker fields that make progress measurable

1. **State** with a small, enforced set of values (backlog, in progress, blocked,
   review, done) — the WIP count is then a query, not an estimate.
2. **Entry and exit timestamps** per state, so cycle and lead times are computable
   from history rather than remembered.
3. **Blocked reason** as a controlled vocabulary; the distribution of reasons is the
   most actionable report a research group can produce.
4. **Owner** (one person) and **reviewer** where relevant; two owners means none.
5. **Definition of done** in the issue, so completion is a fact about the artefact
   (a merged change, a released figure), not an opinion.
6. **A link to the artefact**: the pull request, the release tag, the dataset
   identifier. A closed issue should point at a thing.

Milestones, in this framing, are **batch release points** for a set of issues, and
their value is the conversation about what is *out* of the milestone, not the
countdown. A milestone with more items than the capacity until its date is a plan to
miss it.

## 7. Practice

1. **Cap the work in progress.** Choose the number from the team's capacity, not from
   ambition, and make exceeding it a visible decision.
2. **Report percentiles.** The 85th or 90th percentile of cycle time, plus the count
   of blocked items and the age of the oldest.
3. **Record the waits.** The distribution of blocked reasons (§6.3) identifies the
   fix: access, decisions, data, review.
4. **Review the queue weekly, briefly.** The queue's shape is visible only if someone
   looks; a ten-minute scan of the oldest items is enough.
5. **Separate the backlog from the sprint-like commitment.** A backlog is a wish
   list; work in progress is a promise. Conflating them is what makes lead time
   invisible.
6. **Do not measure individuals.** The queue's statistics are about the system; using
   them for individual evaluation converts the tracker into a source of bad data.

## Assumptions and regime of validity

1. **A constant arrival rate and a stable system.** Bursty arrivals (a grant deadline,
   a field campaign) make lead times worse than the steady-state formula for a while;
   the arithmetic bounds the steady state, not the transient.
2. **Chosen distributions.** The lognormal shape with median 9 days is a teaching
   value; the durable result is the gap between the mean and the median and the size
   of the tail.
3. **Queueing treated as Little's law.** Real queueing adds variability-driven delay
   on top; the model deliberately attributes all of it to the WIP term, which is the
   controllable part.
4. **Work is independent.** Items that share a data set, a collaborator or a decision
   correlate, and correlated items queue behind the same blockage.
5. **No measurement of a real team.** Nothing here describes any group's actual
   throughput, and no number should be quoted as an organisational norm.

## The honest summary

A research queue obeys Little's law: with 1.2 issues arriving per working day, a WIP
of 2 implies a 1.7-day wait, and a WIP of 24 implies 20 days. The work itself is
heavy-tailed — median 8.9 days, 90th percentile 36.4, maximum 694.7 in the
demonstration's model — so the lead time a user sees is the sum of a work distribution
and a queueing term, and capping the WIP moves the 90th percentile by 1.5× without
changing throughput. What a limit cannot do is create capacity: with 18 arrivals a
week against a capacity of 12, the backlog grows by 312 items a year and no WIP policy
changes that. The tracker's value is therefore in making the queue visible — states,
timestamps, block reasons, percentiles — so that the choice between reducing arrivals
and accepting a backlog is made on purpose.

## Python demonstration

[`code/issue_tracking_demo.py`](./code/issue_tracking_demo.py) prints, with
`np.random.default_rng(20261014)`:

1. Little's law for four WIP levels (1.7 to 20.0 days);
2. the cycle-time distribution (median 8.9, 90th percentile 36.4, mean 16.1, maximum
   694.7 days);
3. lead time as work plus queueing for the same four levels, and the 1.5× spread in
   the 90th percentile;
4. the backlog arithmetic when demand exceeds capacity (312 items/year).

```bash
cd 22-data-engineering-reproducibility/05-collaboration-and-project-management/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python issue_tracking_demo.py
```

## Exercises

Graded problems and worked solutions are in
[`exercises/02-issue-tracking-exercises.md`](./exercises/02-issue-tracking-exercises.md)
and
[`exercises/02-issue-tracking-solutions.md`](./exercises/02-issue-tracking-solutions.md).

## Mastery checkpoint

Without notes: a group's tracker receives 10 issues per week, the capacity is 15 per
week, and the median work time is 12 days with a lognormal tail.

1. Compute the throughput in issues per working day and the lead time implied by WIP
   levels of 3 and 15.
2. State which percentile you would report and why the mean is not it.
3. State what a WIP limit of 5 does to the lead-time distribution, and what it does to
   throughput.
4. Arrivals rise to 20 per week. Compute the yearly backlog growth and state the three
   available responses.

## Common pitfalls

1. **Reporting a mean cycle time.** The demonstration's mean is 1.8× its median and the
   tail is twelve times it.
2. **Treating a WIP limit as a productivity measure.** It changes the queue, not the
   capacity.
3. **Letting the backlog and the in-progress list merge.** The lead time becomes
   invisible and the queue's growth is noticed only at the deadline.
4. **Measuring individuals from queue statistics.** It converts the tracker into bad
   data, because people optimise what is measured.
5. **Milestones without capacity arithmetic.** A milestone whose items exceed the
   capacity until its date is a plan to miss it.
6. **No blocked-reason vocabulary.** The most actionable statistic in a research queue
   is why items are not moving.

## Where this is used

- **Supervision of students and small teams** — the queue is the supervision
  conversation, and percentiles make it short.
- **Grant and reporting cycles** — the milestone view is what a report needs, with the
  capacity arithmetic attached.
- **Research software maintenance** — issue trackers hold the work that keeps a code
  usable ([22-01-01](../01-research-software-engineering/01-software-design-science.md) §6).
- **Data access and review queues** — a data request queue behaves the same way, and
  the blocked-reason distribution is the evidence for a policy change.

## Related lessons

- [22-05-01 Project Directory Structure and Conventions](./01-project-structure.md) —
  the artefacts the issues produce.
- [22-05-03 Collaborative Writing with LaTeX and Markdown](./03-collaborative-writing.md) —
  the review work that a tracker's states make visible.
- [22-02-03 Workflow Managers: Snakemake, Make, Dask, Prefect](../02-reproducible-workflows/03-workflow-managers.md) —
  the same scheduling logic for machines.
- [22-01-03 Code Review and Collaborative Development](../01-research-software-engineering/03-code-review.md) —
  the review stage that a tracker's cycle time includes.

## Self-assessment checklist

- [ ] I can apply Little's law to a research queue.
- [ ] I can measure and report a cycle-time distribution.
- [ ] I can separate work time from queueing time.
- [ ] I can state what a WIP limit does and does not change.
- [ ] I can design tracker fields that make progress measurable.
- [ ] I can compute backlog growth when demand exceeds capacity.
