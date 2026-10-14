# Exercises — 22-07-04 Benchmarking, Performance Tracking and Documentation Tests

Attempt these before reading the
[solutions](./04-benchmarking-and-docs-solutions.md). The lesson is
[04 Benchmarking, Performance Tracking and Documentation Tests](../04-benchmarking-and-docs.md).
Numbers refer to the **SYNTHETIC** simulation of `code/benchmarking_and_docs_demo.py`.

Use $n = [(z_{0.95} + z_{0.80})\,\sigma/\Delta]^2$ with
$z_{0.95} = 1.645$ and $z_{0.80} = 0.842$, and round up.

## ★ Foundational

**★1.** Name the three quantities that a benchmark comparison needs, and state which one is
usually left unmeasured.

**★2.** A benchmark has 6 % run-to-run noise.

(a) Compute the repeats needed to detect a 10 % change at 95 % confidence with 80 % power.
(b) Compute the repeats for a 3 % change. (c) State the effect on both numbers of halving the
noise.

**★3.** State four things that a documentation example test catches and three things it
cannot catch.

## ★★ Applied

**★★4.** A team measures a benchmark once per push, 18 pushes a day for 230 working days,
and alerts on a 4 % slowdown. Run-to-run noise is 7 %.

(a) Compute the probability of a false alarm per comparison and the expected number of false
alarms per year. (b) Compute the expected number of alarms a year if they take the median of
9 runs instead. (c) State the change in the alert rule that reduces alarms without making the
test insensitive, and its effect.

**★★5.** A kernel's operation counts are 2.00e6, 4.30e6 and 9.20e6 for problem sizes
$n = 10^4, 2\times10^4, 4\times10^4$.

(a) Fit the log-log slope and state the empirical complexity. (b) State the slope a quadratic
kernel would show. (c) Compute the repeats needed to detect the same change from timing alone
at 8 % noise, and state why the count is the better instrument here.

**★★6.** A team switches its benchmark estimator from best-of-5 to best-of-20 to "reduce
noise".

(a) Compute the expected bias of each estimator relative to a single run for
$\sigma = 0.10$, given that the minimum of $N$ standard normals has expectation
$-1.163$ ($N=5$) and $-2.060$ ($N=20$). (b) State the trend-line artefact the switch
produces. (c) State what you would record to make the change defensible.

## ★★★ Research-oriented

**★★★7.** Design the performance-tracking system for a library with 12 numerical kernels
that runs on a shared cluster with variable load.

State: the machine and environment control, the estimator and $N$ per kernel, the effect size
you will track, the thresholds and the alert rule (with the expected false-alarm rate), what
is recorded per run, what counts as a discontinuity, how a kernel addition is handled, and the
one situation in which you would deliberately *not* alert.

**★★★8.** A paper claims "our method is 30 % faster than the baseline".

Design the evidence you would require: the benchmark specification, the machine and
environment, the estimator and repeats, the effect size and its confidence interval, the
operation counts, the input sizes, the code and container identifiers, and the statistical
comparison the claim implies. State the three ways the claim could be false despite a
correct measurement.

**★★★9.** A group's documentation is generated automatically from docstrings and reports
"100 % of the public API documented".

Analyse what that statement verifies: state what the generator proves, the four things it
cannot prove, the documentation tests you would add (with their cost), and how you would
measure whether the documentation is *usable* rather than present. State the one measurement
that would settle whether the documentation helps anyone.
