# Exercises — 20-08-04 Change-Point Detection and Regime Shifts

Attempt these before reading the
[solutions](./04-change-point-and-detection-solutions.md). The lesson is
[04 Change-Point Detection and Regime Shifts](../04-change-point-and-detection.md).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Write the piecewise-constant mean model and the penalised objective.
Explain in one sentence why the fit term alone has a degenerate minimiser.

**★2.** For $n = 500$, compute $\log n$ and the penalties $2\log n$ and
$4\log n$ to two decimal places. State the change-point count detected at each
from the lesson table.

**★3.** State the segment cost $\mathrm{SSE}(i,j)$ in words and explain why the
dynamic program needs it for every pair $(i, j)$.

## ★★ Applied

**★★4.** A detector at $\beta = 2.0$ returns 11 change points for a series whose
truth is 2. Using the cost objective, explain the trade-off the fit term is
exploiting and why each of the 9 extra points reduces the objective.

**★★5.** Using the false-positive table, choose a penalty for a study in which a
false regime shift costs a research programme a year of work, and state the
measured error rate you accept. Then say what you would give up in detection
power, using the ramp table as evidence.

**★★6.** The variance-only series produced 6 mean change points, none at the true
epoch 250, with segment standard deviations 1.33, 2.75, 2.07, 2.86, 2.29, 3.10.
Explain what those six numbers are telling you about the mechanism of the false
detections.

## ★★★ Research-oriented

**★★★7.** Design a change-point analysis for a series with autocorrelated
(AR(1)) noise. Specify how the cost function changes, how you would calibrate the
penalty, and the prediction for whether the calibrated penalty is larger or
smaller than for white noise at the same per-series error rate. Include the
diagnostic you would report to show the calibration worked.

**★★★8.** The lesson shows that a single ramp is represented by four steps at
$\beta = 12.42$ and by two steps at $\beta = 49.68$. Design an experiment that
would let you *decide* whether the true process is a ramp or a sequence of
steps: state the two model families, the comparison criterion, and the smallest
number of detectable steps for which the two families are distinguishable at a
stated record length.
