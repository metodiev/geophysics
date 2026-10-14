# Exercises — 18-09-04 Uncertainty in Learned Inversion: Pitfalls and Calibration

Attempt these before reading the
[solutions](./04-uncertainty-in-learned-inversion-solutions.md). The lesson is
[04 Uncertainty in Learned Inversion: Pitfalls and Calibration](../04-uncertainty-in-learned-inversion.md).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Name the three kinds of uncertainty in a learned inverse and state which
one an ensemble of networks measures.

**★2.** For a nominal 95.4% interval, state the empirical coverage observed in
distribution and out of distribution (spike family), and the shortfall factor in
each case.

**★3.** Define the ratio error/$\sigma$ and state its value for a perfectly
calibrated Gaussian estimator.

## ★★ Applied

**★★4.** The in-distribution mean $\sigma$ is 0.0105 and the mean error is 0.0451.
Compute the factor by which the intervals must be widened to be calibrated in the
mean-absolute sense (target ratio $\sqrt{2/\pi}\approx0.80$), and state whether a
single global factor would fix the out-of-distribution case.

**★★5.** Coverage falls from 30.3% to 13.4% under shift while $\sigma$ stays near
0.01. Explain in two sentences why the ensemble cannot detect this, using the
words "correlated" and "lower bound".

**★★6.** The linear posterior reference over-covers at 100%. State one operational
consequence of over-coverage and one of under-coverage, and say which is more
dangerous for a drilling or excavation decision.

## ★★★ Research-oriented

**★★★7.** Design a calibration-and-shift-test protocol that a practitioner could
run before deploying a learned inverse, using only data available in production.
Specify the held-out sets, the metrics and the acceptance thresholds. A
specification that could not be executed is a failed answer.

**★★★8.** Construct an ensemble that is well calibrated in distribution and badly
miscalibrated on a shifted family, and then construct a second ensemble that is
worse in distribution but *better* on the shifted family. Explain what design
choice causes the trade-off and how you would decide between them for a stated
application.
