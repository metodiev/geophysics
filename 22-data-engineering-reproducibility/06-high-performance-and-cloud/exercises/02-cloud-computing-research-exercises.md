# Exercises — 22-06-02 Cloud Computing for Geophysical Computation

Attempt these before reading the
[solutions](./02-cloud-computing-research-solutions.md). The lesson is
[02 Cloud Computing for Geophysical Computation](../02-cloud-computing-research.md).
Numbers refer to the **SYNTHETIC** model of `code/cloud_computing_research_demo.py`:
serial fraction 0.05, a 24-hour base run, a per-instance-hour interruption probability of
0.02, and chosen costs in arbitrary units.

## ★ Foundational

**★1.** Write Amdahl's law and its asymptote, and state what the "serial fraction" is in
a geophysical analysis (give three examples).

**★2.** For $p = 0.05$: (a) compute $S(4)$, $S(16)$ and $S(64)$; (b) compute the efficiency
at each; (c) state the asymptote and what it means for a 1 024-instance fleet.

**★3.** State three things the cloud changes and three it does not change.

## ★★ Applied

**★★4.** An analysis takes 20 hours on one worker with a serial fraction of 0.08.

(a) Compute the speedup and efficiency at 8, 32 and 128 workers. (b) Compute the wall time
at each. (c) Choose the smallest worker count bringing the run under 3 hours, and compute
its instance-hours.

**★★5.** The same run uses interruptible instances at 0.03 interruptions per
instance-hour.

(a) Compute the interruption probability within a 20-minute checkpoint interval.
(b) Compute the probability that at least one of 32 instances is interrupted over a
2-hour run. (c) Choose a checkpoint interval and state the trade-off you are making.

**★★6.** A group's fleet of 64 instances runs a 1.5-hour job and reports "no speedup
beyond 16 instances".

(a) State the two candidate explanations and the measurement that distinguishes them.
(b) Compute the efficiency at 16 and 64 instances for $p = 0.05$ and state whether the
observation is consistent with the serial fraction alone. (c) State the change that would
move the ceiling.

## ★★★ Research-oriented

**★★★7.** Design a cloud execution plan for a 5 000-realisations ensemble that must
complete within 24 hours, using containers and interruptible capacity. State the
per-realisations work, the worker count and instance type reasoning, the checkpointing
strategy, the completion tracking, the data placement (co-located with compute), and the
cost accounting. State the one failure your plan cannot prevent.

**★★★8.** Design a measurement of a real workload's serial fraction: state the
experiments (a scaling series at several worker counts), the fit or estimate, the
confounders (I/O, contention, warm caches) and how you would separate them. State what
the estimate cannot tell you about a different problem size.

**★★★9.** A group's cloud bill is dominated by egress. Analyse the problem: state the
access pattern that produces it, the three redesigns available (co-location, caching,
layout change), the measurement for each, and the risk each introduces. State what you
would need to know about the provider's charging model to choose.
