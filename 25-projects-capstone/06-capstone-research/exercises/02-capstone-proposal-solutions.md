# Solutions — 25-06-02 Capstone: Proposal, Literature Review and Methods Plan

Reference solutions. Numbers marked "printed" come from
[`code/capstone_proposal_demo.py`](../code/capstone_proposal_demo.py); the slip and
repair-combination values were obtained by re-running the same analysis with the
modified estimates. All planning figures are **SYNTHETIC**.

## ★1. PERT for one task

$$E = \frac{o + 4m + p}{6} = \frac{2 + 12 + 7}{6} = 3.5\ \text{weeks},\qquad
\mathrm{sd} = \frac{p - o}{6} = \frac{5}{6} = 0.83\ \text{weeks}.$$

$E$ is the mean of a distribution whose shape puts half its weight on the most likely
value and a quarter on each extreme; the standard deviation measures the *breadth* of
that distribution, i.e. how much the task's duration varies from attempt to attempt.
Its size is the reason a three-point estimate is worth more than a single number: a
0.83-week sd on a 3.5-week task is what makes a 24-week plan a distribution rather
than a date.

## ★2. A chain and a diamond

*Chain A→B→C:* duration $3+4+2 = 9$ weeks, and **every task has zero slack** — in a
pure chain, any delay propagates directly to the finish. This is worth stating
explicitly because it explains why the demo's eight critical tasks have zero slack even
though several look small.

*Diamond,* with D (2 weeks) starting after A and E (1 week) after both B and D:

| task | duration | earliest finish | latest finish | slack |
|---|---|---|---|---|
| A | 3 | 3 | 3 | 0 |
| B | 4 | 7 | 8 | 1 |
| D | 2 | 5 | 8 | 3 |
| E | 1 | 9 | 9 | 0 |

Duration $= 3 + \max(4, 2) + 1 = 9$ weeks, and the slack belongs entirely to the
shorter branch: D has 3 weeks, B has 1. **Slack is created by parallelism, not by
shortness** — D could take five weeks instead of two without delaying anything, while
B cannot take five.

## ★3. Sum versus path

The sum (33.7 weeks) counts every task as if it were executed in series. The network
runs several tasks concurrently: the code release and documentation (3.00 weeks)
overlaps the inversion series, the sensitivity analysis (2.00) overlaps the uncertainty
quantification (3.00), and the defence preparation (2.00) overlaps the internal review
and revision (2.00). The critical path is the longest *chain of dependencies*, 24.50
weeks, and the excess of the sum over it is

$$\frac{33.7}{24.50} = 1.376 \quad\Longrightarrow\quad 37.6\% .$$

So a proposal that reports the sum has over-allocated by 38%, or has failed to notice
that its own plan contains parallelism. The reverse error — assuming parallelism that
one person cannot deliver — is worse, and the test is to ask of every pair of
concurrent tasks which person executes each.

## ★★4. Reproducing the critical path and the slack

Forward pass (earliest finish):

| task | preds | $E$ | EF |
|---|---|---|---|
| 1 literature review | — | 3.00 | 3.00 |
| 2 data request and QC | 1 | 2.17 | 5.17 |
| 3 method test on synthetic | 1 | 3.00 | 6.00 |
| 4 processing pipeline | 2, 3 | 4.17 | $\max(5.17,6.00)+4.17 = 10.17$ |
| 5 inversion runs | 4 | 3.17 | 13.33 |
| 6 sensitivity analysis | 5 | 2.00 | 15.33 |
| 7 uncertainty quantification | 5 | 3.00 | 16.33 |
| 8 figures | 6, 7 | 2.00 | $\max(15.33,16.33)+2.00 = 18.33$ |
| 9 manuscript draft | 8 | 4.17 | 22.50 |
| 10 internal review and revision | 9 | 2.00 | 24.50 |
| 11 code release and docs | 4 | 3.00 | 13.17 |
| 12 defence preparation | 9 | 2.00 | 24.50 |

Project duration $= \max \mathrm{EF} = 24.50$ weeks (tasks 10 and 12 both end there).

Backward pass: $\mathrm{LF}_i = \min_{j \in \text{succ}(i)}(\mathrm{LF}_j - E_j)$,
starting from $\mathrm{LF}_{10} = \mathrm{LF}_{12} = 24.50$.

- Task 2: successor 4, so $\mathrm{LF}_2 = \mathrm{LS}_4 = 10.17 - 4.17 = 6.00$, and
  slack $= 6.00 - 5.17 = \mathbf{0.83}$ weeks — four working days, as printed.
  Task 2 must not slip more than that even though it is not on the path.
- Task 11: no successors, so $\mathrm{LF}_{11} = 24.50$,
  slack $= 24.50 - 13.17 = \mathbf{11.33}$ weeks — the code release can be delivered
  nearly three months late without moving the finish.
- Task 7: successor 8, $\mathrm{LF}_7 = \mathrm{LS}_8 = 18.33 - 2.00 = 16.33$,
  slack 0.00 — critical, because the figures wait on the *later* of tasks 6 and 7.

**The slack table is the schedule's real product**: it says where attention is
required (tasks 2 and 6 have 0.83 and 1.00 weeks) and where it is not (task 11 has
11.33).

## ★★5. Interpreting the percentiles

- P80 $= 26.48$ weeks, so a date promised with 80% confidence is **week 27** (rounding
  up, never down, since the distribution is right-skewed).
- $P(\le 24) = 17.3\%$: the budget is met about one time in six.
- Mean $= 25.31$ weeks against a deterministic critical path of 24.50 weeks, a
  difference of $0.81$ weeks.

The difference exists because the deterministic pass uses each task's *mean* duration,
while the Monte Carlo takes the longest path of each sampled realization. When two
paths are nearly equal (here the chain through tasks 6 and 7 differ by only 1.00 week
at the figures node), the realized longest path alternates between them, and the mean
of the maximum exceeds the maximum of the means — the same convexity argument that makes
$E[\max(X,Y)] > \max(E[X],E[Y])$. The gap grows with the number of near-critical
parallel paths, which is precisely the situation a busy capstone is in.

## ★★6. Comparing the repairs

| repair | mean finish | $P(\le 24)$ | gain | effort |
|---|---|---|---|---|
| baseline | 25.31 | 17.3% | — | — |
| A: trim the three longest by 25% | 22.31 | 92.1% | $+74.8$ points | 25% off 11.51 weeks of task time $\approx 2.9$ weeks |
| B: start the method test in week 0 | 24.56 | 36.0% | $+18.7$ points | **none** |

A buys four times the probability for a real cost; B buys 18.7 points for nothing. The
return per unit of effort — 26 points per week of effort for A, unbounded for B — makes
B the first repair regardless of how the effort is priced, and this conclusion does not
depend on the exact effort numbers because B's cost is zero. **The schedule's cheapest
improvement is always a dependency that does not need to exist**, and the analysis that
finds it is the backward pass: task 3's predecessor list, not its duration, was the
problem.

## ★★7. Equal durations, different correlations

The correlation of a task's duration with the finish date measures how much of the
*finish-date variance* passes through that task — it depends on the path from the task
to the end, not on the task's own size. Two tasks of 4.17 weeks differ because:

- one lies on the critical path in **every** realization (correlation $0.45$), so any
  draw of its duration shifts the finish almost one-for-one;
- the other may sit on a path that is absorbed by slack in some realizations, so part
  of its variation is absorbed (a lower correlation).

A risk register should therefore be built from (i) the finish-date correlations, (ii)
the critical-path frequency of each task, and (iii) the slack table — not from the task
list sorted by size. A task that is large but never on the critical path (the code
release, 3.00 weeks, slack 11.33) is not a schedule risk at all; a task that is small
and always critical (the internal review, 2.00 weeks, slack 0.00) is.

## ★★8. The slip

With the pipeline at $o = 5$, $m = 6$, $p = 8$ weeks ($E = 6.17$, two weeks more than
planned):

| quantity | baseline | after the slip |
|---|---|---|
| deterministic path | 24.50 | **26.50** weeks |
| Monte Carlo mean | 25.31 | **27.31** weeks |
| P80 | 26.48 | **28.48** weeks |
| $P(\le 24$ weeks$)$ | 17.3% | **0.68%** |

The deadline is effectively lost — 0.68% is not a plan. The two cheapest protections,
evaluated on the same schedules:

| protection | mean finish | $P(\le 24)$ | cost |
|---|---|---|---|
| B: method test starts in week 0 | 26.56 | 3.73% | none |
| A: trim the three longest tasks by 25% | 23.81 | 56.27% | real effort |
| A and B together | 23.06 | **76.52%** | real effort |

The free repair recovers only the equivalent of its 0.75 weeks (0.68% $\to$ 3.73%):
**slack cannot be manufactured by moving a dependency when a two-week overrun has
consumed it.** Restoring a defensible plan requires the real trim (56.27%), and the
combination of both gives 76.52%. The honest proposal then states one of two things:
"the deadline is met with 77% probability on a trimmed scope", or "the study is
re-planned for 28 weeks". What it must not do is report the original 24-week plan with
a two-week overrun hidden inside it.

## ★★★9. The scheduling half of a proposal

The structure required is exactly the demo's, applied to your own design brief:

1. **Work breakdown**, 10–14 tasks, each with predecessors, $o$, $m$, $p$, and — the
   part the demo does not print — the *assumption behind $p$*: "6 weeks rather than 4
   if the rotation/deconvolution has to be re-derived for the three-component data",
   "8 weeks rather than 6 if the first two inversions fail to converge and the
   parameterisation has to be reduced". A pessimistic estimate without a stated failure
   is an arbitrary number, and an arbitrary $p$ propagates straight into the deadline
   probability.
2. **Forward and backward passes**, with the slack table, and at least one sentence
   identifying the tasks with less than a week of slack.
3. **Deadline probability** from at least 10 000 samples, with the P50/P80/P90 quoted
   and the $P(\le$ budget$)$ stated as a percentage rather than a hope.
4. **Drivers**: the finish-date correlations and the critical-path frequency, from which
   the risk register is written (two or three risks, each with an expected impact in
   weeks and a mitigation that changes the *schedule*, not just the mood).
5. **A dependency repair** demonstrated to be free, and its measured probability gain.
6. **The protected milestone.** For a capstone built on the brief of
   [25-06-01](./01-capstone-design-exercises.md), the milestone the schedule must
   protect is the one that verifies the estimator against synthetic data with a known
   answer. Everything downstream is a function of it, a failure there invalidates the
   headline number rather than delaying it, and it is the only step whose failure
   cannot be absorbed by working faster later. A schedule that puts it in the middle —
   after the data processing, before the inversions — with adequate slack *in front of
   it* is the deliverable.
