# Solutions — 22-05-02 Issue Tracking, Milestones and Kanban for Research

> Read after attempting. Numbers are computed here and match the demonstration's printed
> output. Lesson:
> [02 Issue Tracking, Milestones and Kanban for Research](../02-issue-tracking.md).

---

## ★1 — Little's law

$$\text{WIP} = \text{throughput} \times \text{lead time},$$

where **WIP** is the number of items started and not finished, **throughput** is the
rate at which items are finished in a steady state (equal to the arrival rate if the
system is stable), and **lead time** is the average time from starting (or arriving) to
finishing. Applied to a research queue, the law's value is that any two terms determine
the third: a group that knows its arrival rate and its open-item count knows the wait it
is imposing.

## ★2 — The demonstration's queue

(a) Throughput $= 6/5 = 1.20$ issues per working day.

(b) WIP 2: $2/1.20 = 1.7$ days. WIP 24: $24/1.20 = 20.0$ days. Both match the printed
table.

(c) The difference is the *entire* experience of the queue for the same work: the same
issues take 20 days of waiting at WIP 24 against 1.7 at WIP 2, and nothing about the work
itself changed.

## ★3 — The work distribution

Median 8.9 days; 90th percentile 36.4 days; mean 16.1 days; maximum 694.7 days (all
printed). The mean exceeds the median because the distribution is right-skewed: a
lognormal with $\sigma = 1.1$ has a long upper tail whose few large values pull the mean
up, while the median is set by the bulk. The practical consequence is that the mean
describes a value that most items never reach — a classic property of queueing and
service-time data.

## ★★4 — A 10-arrival team

(a) Throughput $= 10/5 = 2.0$ issues per working day.

(b) Queueing wait $= \text{WIP}/\text{throughput}$: WIP 3 → 1.5 days; WIP 15 → 7.5 days.

(c) Scaling the demonstration's shape: with a median work time of 12 days, the 90th
percentile is $12 \times (36.4/8.9) = 49.1$ days. Lead times:

| WIP | Queueing | Median lead | 90th percentile lead |
|---|---|---|---|
| 3 | 1.5 | 13.5 | 50.6 |
| 15 | 7.5 | 19.5 | 56.6 |

So a five-fold difference in WIP moves the median lead time by 44 % and the 90th
percentile by 12 % — the limit helps most at the centre of the distribution, and the tail
is dominated by the work distribution itself. That is the honest quantitative answer to
"will a WIP limit fix our slowest items?": mostly no.

## ★★5 — Arrivals exceeding capacity

(a) Growth $= 20 - 12 = 8$ per week, $8 \times 50 = 400$ per year (counting 50 working
weeks).

(b) Responses:

1. **Reduce arrivals**: triage into "not now" with a documented reason (a policy decision
   the group makes once, rather than each member's private queue), and batch recurring
   requests into a single periodic job.
2. **Increase capacity**: automate the recurring items (scripts, templates, a checklist),
   or hire/schedule dedicated time; the tracker's blocked-reason report tells you which
   items are repetitive enough to automate.
3. **Accept the backlog deliberately**: publish the current wait (from the percentiles)
   so requesters can plan, and set a service level ("reviewed within three weeks") that
   the group can actually meet.

(c) A WIP limit of 4 achieves **visibility**: the backlog grows by 8 items a week in a
list everyone can see, instead of being absorbed invisibly into four in-progress items.
It does not change throughput; it changes whether the shortage is a decision.

## ★★6 — An open/closed tracker

(a) The measurements not available: (i) cycle time and its distribution, because there is
no record of when work started; (ii) the work-in-progress count at any time, because
"open" merges the backlog with in-progress; (iii) the blocked-reason distribution, because
the reason lives in unstructured prose.

(b) Two field changes: a **state** field with an enforced small vocabulary (backlog, in
progress, blocked, review, done) and **transition timestamps** (entry and exit per state);
optionally a controlled **block reason** field.

(c) The weekly report:

```text
Queue: 34 open (12 in progress, 4 blocked), oldest 61 days
Cycle time last 8 weeks: median 14 d, 85th percentile 42 d
Blocked reasons: access 3, decision 1 (unchanged from last week)
```

Those three lines are what a supervisor, a student and a funder can each act on, and
none of them required more than two fields.

## ★★★7 — A supervision and reporting system for eight people

**States and fields.** States: backlog → in progress → (blocked) → review → done.
Fields: owner (one person), type (analysis, code, manuscript, data request, admin),
entry/exit timestamps per state, block reason (controlled vocabulary), definition of done
(an artefact: a merged change, a released figure, an archived dataset), and links to the
artefact and to the milestone.

**WIP policy.** A per-person limit of two or three in-progress items (one if supervision
time is scarce), enforced by the tool where possible; exceeding it requires closing or
deferring something, which is the conversation the policy exists to force.

**Weekly review (30 minutes, fixed agenda).** (i) The blocked items and their reasons (the
longest part of the meeting); (ii) the oldest three items, with a decision each: push,
split, drop; (iii) the WIP count per person against the limit; (iv) one number — the
trailing four-week median and 85th percentile cycle time.

**Milestone arithmetic.** A milestone is a set of issues with a date; the count must be
within the group's capacity until that date *after* subtracting the recurring work
(reviews, teaching, service). Compute the capacity in person-weeks, then check the
milestone's estimated effort against it — a milestone whose effort exceeds capacity is a
plan to miss it, and the review's job is to remove items early rather than at the
deadline.

**Reports.** For the group: the weekly three lines of ★★6(c). For a funder: the milestone
progress against the plan, the number of deliverables completed with their artefacts, and
the blocked-reason distribution as evidence of a systemic constraint (data access,
decisions).

**The metric I would not publish.** *Per-person throughput or cycle time.* Queue
statistics are properties of the system; publishing them per person converts the tracker
into an evaluation instrument, which produces optimised bookkeeping (small items, early
re-labelling) rather than faster research. The public metrics are the system's: lead-time
percentiles, blocked reasons, milestone progress.

## ★★★8 — Measuring a real queue's cycle time

**Data.** The tracker's transition history: for each issue, the timestamp of each state
change (and the actor, for audit). If the tracker only retains the final state, the
history is unavailable and the measurement cannot be made retrospectively — which is the
argument for capturing transitions from the start.

**Statistic.** Cycle time (start → done) and lead time (arrival → done) as **percentiles
by issue type** (analysis, code, manuscript, data request) and by month or quarter. Report
the sample size alongside each percentile: a 90th percentile from nine items is an
anecdote with a decimal point.

**Confounders and their handling.** (i) **Re-opened issues**: count the re-openings and
report the time to *final* completion, or treat each opening as a cycle and report the
number of cycles; (ii) **split issues**: sum the parts' work and attribute the lead time
to the original arrival, so a split does not look like a new fast task; (iii) **issues
never intended to finish** (parking-lot ideas, wish-list notes): exclude them by type
rather than by omission, and state the exclusion rule.

**What the measurement cannot tell you.** Whether the work was *good*: a queue can have
excellent cycle-time percentiles and produce wrong analyses, and a slow item may be the
most valuable work in the project. The queue's statistics are about flow and are
complementary to a scientific review, not a substitute for it.

## ★★★9 — A burst of 30 issues

**Assumptions.** Capacity 12 per week (2.4 per working day), arrivals return to 6 per
week after the burst week, and the service remains at capacity while the backlog exists.

**Recovery time.** The burst adds 30 issues; the steady-state arrivals (6/week) are below
capacity (12/week), so the system drains the extra backlog at
$12 - 6 = 6$ issues per week. The burst's excess over the normal weekly arrival of 6 is
$30 - 6 = 24$ issues, so recovery takes $24/6 = 4$ weeks — during which the lead time for
*new* items includes a queueing component of up to $24/2.4 \approx 10$ working days at the
start of the drain.

**The assumption that makes recovery possible.** That capacity is **elastic and
sustained**: the team can actually work at 12 issues/week (not merely 12 on paper), and
the burst does not permanently consume capacity (review fatigue, a follow-on project).
If capacity is 8 rather than 12, the drain rate is 2 issues/week and recovery takes
12 weeks; at a capacity of 6 (equal to arrivals) the backlog never clears.

**What the burst reveals about the WIP policy.** A WIP limit does not protect against a
burst — the burst's items queue regardless — but it determines *where* they queue and
whether the group sees them: with a limit of 4, four items are in progress and 20 sit
visibly in the backlog with a computed wait; without a limit, all 24 appear "in progress"
and everyone's attention is spread over them, which lengthens even the short items. The
policy question the burst raises is not "how do we work faster" but "which of these 30
issues are we prepared to say no to", and the blocked/backlog visibility is what makes
that question unavoidable.
