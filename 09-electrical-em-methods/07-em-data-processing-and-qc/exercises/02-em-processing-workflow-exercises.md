# Exercises — 09-07-02 EM Processing Workflow and Data Editing

Attempt these before reading the
[solutions](./02-em-processing-workflow-solutions.md). The lesson is
[02 EM Processing Workflow and Data Editing](../02-em-processing-workflow.md).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** A synthetic decay is $V(t) = A(t+t_0)^{-p}$ with $A = 1.00$,
$t_0 = 1.00\times10^{-4}$ s and $p = 2.5$. Compute $V$ and the local timescale
$(t+t_0)/p$ at $t = 0.1$, $0.3$, $1.0$, $6.0$ and $20$ ms, and state the longest
low-pass filter (in milliseconds) that respects the rule "filter length
$\ll$ the fastest timescale" at each gate.

**★2.** The demonstration's record spans a factor $3.22\times10^{6}$ from first
sample to last. A constant offset that is $2\%$ of the first sample is what
fraction of the last sample? State the consequence for an interpreter who looks
only at the late-time gates.

**★3.** For a record with **additive, constant** noise (not multiplicative),
write down a despiking statistic and threshold, and explain why the *relative*
residual used in the lesson is the wrong choice for that record.

## ★★ Applied

**★4.** The demonstration's running median of length $k$ flags 481 samples at
$k=3$ with a global scale and 249 with a local scale, against 6 true spikes.
Explain where the false positives are concentrated, and why a *local* scale
reduces them.

**★5.** Using the drift table of the lesson, choose a drift-removal window for a
survey whose latest usable gate is 6 ms. State the assumption you rely on, the
mean gate error you accept, and one test that would falsify the assumption.

**★6.** Using the filtering table (measured gate-1 bias $+0.7244\%$ at $m=3$,
$+33.0756\%$ at $m=17$; 19.54 $\mu$s per sample) and the timescale of ★1 at
$t = 0.3$ ms, state the largest defensible filter length and compare it with the
measured boundary between the 7% and 33% bias regimes.

## ★★★ Research-oriented

**★★★7.** Write a processing log for the six-step chain of the lesson that
another analyst could reproduce without your code. It must contain, for each
step: the estimator, the parameter chosen, the measured noise reduction, the
measured bias on an ideal synthetic, and the parameters you rejected with the
number that made you reject them.

**★★★8.** The lesson's drift-removal error scales with the drift, not with the
noise, so a survey with an excellent receiver and a badly drifting instrument can
have a worse late-time result than a survey with a poor receiver and no drift.
Design a diagnostic that separates the two cases from the data alone, and state
the statistic and the decision rule. A specification that could not be executed
is a failed answer.
