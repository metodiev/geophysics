# Exercises — 18-08-02 Synthetic Testing, Checkerboards and Recovery Tests

Attempt these before reading the
[solutions](./02-synthetic-testing-solutions.md). The lesson is
[02 Synthetic Testing, Checkerboards and Recovery Tests](../02-synthetic-testing.md).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** State the three things a synthetic test fixes and the one thing it
varies with.

**★2.** From the recovery table, state the smallest period whose recovered
amplitude exceeds 0.9, and the largest period whose recovered amplitude is below
0.01.

**★3.** For the spike test, the recovered peak is 0.3222 and the PSF half-width is
3 cells. State what the recovered image would look like for a true pair of spikes
2 cells apart.

## ★★ Applied

**★★4.** A colleague shows a recovered checkerboard at period 8 with amplitude
0.9875 and concludes "the survey resolves 8-cell structure". State two additional
numbers the claim requires, and one reason the conclusion could still be wrong.

**★★5.** Using the alignment table, compute the worst-to-best ratio of recovered
amplitude for period 4 and state what you would report as the single number
describing period-4 recovery.

**★★6.** The PSF has a minimum of $-0.0531$. An interpreted section shows a
negative anomaly at the base of a positive one. Design the check that decides
whether the negative anomaly is real, stating the quantity you compute and the
threshold you apply.

## ★★★ Research-oriented

**★★★7.** Design a synthetic-test suite for a target family of your choice
(layered, blocky, or faulted) that would establish the resolution of a stated
experiment without relying on checkerboards. Specify the patterns, the metrics,
and the decision rule for "resolved to within X km". A specification that could
not be executed is a failed answer.

**★★★8.** The recovery for period 16 is 1.0004 — slightly above 1. Explain
mechanically how a linear inversion with a smoothness prior can recover an
amplitude larger than the truth, and state whether that argues for or against
using amplitude recovery as a resolution metric.
