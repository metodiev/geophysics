# Exercises — 25-06-02 Capstone: Proposal, Literature Review and Methods Plan

Attempt these before reading the
[solutions](./02-capstone-proposal-solutions.md). The lesson is
[02 Capstone Proposal](../02-capstone-proposal.md); all numbers are **SYNTHETIC**
planning figures printed by
[`code/capstone_proposal_demo.py`](../code/capstone_proposal_demo.py):

| Quantity | Value |
|---|---|
| work breakdown | 12 tasks, PERT estimates $E = (o+4m+p)/6$, $\mathrm{sd} = (p-o)/6$ |
| sum of expected durations | 33.7 weeks |
| deterministic critical path | 8 tasks, 24.50 weeks |
| slack | data QC 0.83; sensitivity analysis 1.00; code release 11.33; defence prep 0.00; other critical tasks 0.00 |
| Monte Carlo | mean 25.31, sd 1.38; P10 23.55, P50 25.30, P80 26.48, P90 27.12, P95 27.62 |
| $P(\le 24$ weeks$)$ | 17.3% |
| drivers (corr. with finish) | manuscript draft 0.453, processing pipeline 0.452, inversion runs 0.447 |
| repair A | trim the three longest tasks by 25%: 22.31 weeks, 92.1% |
| repair B | start the method test in week 0: 24.56 weeks, 36.0% |

## ★ Foundational

**★1.** Compute the PERT expected duration and standard deviation for a task with
$o = 2$, $m = 3$, $p = 7$ weeks, and state what the standard deviation describes.

**★2.** For the three-task chain A (3 weeks) → B (4 weeks) → C (2 weeks), compute the
project duration and the slack of each task. Then add a parallel task D (2 weeks) that
also starts after A and must finish before a closing task E (1 week) that follows both
B and D; recompute the duration and each task's slack.

**★3.** State why the sum of the expected durations (33.7 weeks) exceeds the
deterministic critical path (24.50 weeks), and by what percentage.

## ★★ Applied

**★★4.** Reproduce the deterministic critical path from the task table, and verify the
slack of "data request and QC" (0.83 weeks) and of "code release and docs" (11.33
weeks) with a forward and backward pass.

**★★5.** Interpret the Monte Carlo percentiles for a project manager: what completion
date would you promise for an 80% confidence, and what is the probability of meeting the
24-week budget? Then state the mean and compare it with the deterministic path, and
explain the difference.

**★★6.** Compare the two repairs: compute the probability gain of each, and estimate
the effort each requires. State which repair should be taken first and why the answer
does not depend on the exact effort numbers.

**★★7.** The finish-date correlations are 0.453 (manuscript draft), 0.452 (processing
pipeline), 0.447 (inversion runs), 0.294 (literature review), 0.289 (figures). Two
tasks have identical expected durations (4.17 weeks) yet different correlations with
the finish. Explain how that is possible and state what a risk register should
therefore be built from.

**★★8.** A slip: the processing pipeline turns out to need $o = 5$, $m = 6$, $p = 8$
weeks (two weeks more than planned). Recompute the deterministic path and the deadline
probability (the answers are in the solutions), then state the two cheapest protections
and what they restore.

## ★★★ Research-oriented

**★★★9.** Write the scheduling half of a capstone proposal for the design brief you
produced in [25-06-01](./01-capstone-design-exercises.md): a 10–14 task work breakdown
with dependencies and three-point estimates, the forward and backward passes, the
critical path and slack table, a deadline probability, the finish-date drivers, and at
least one dependency repair you have identified as free. Your answer must include the
**assumption** behind each $p$ (what would have to go wrong), and it must state which
single milestone the schedule is designed to protect. A schedule whose estimates have no
stated assumptions is a guess with a table around it.
