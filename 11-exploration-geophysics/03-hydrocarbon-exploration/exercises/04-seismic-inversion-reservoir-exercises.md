# Exercises — 11-03-04 Seismic Inversion for Reservoir Properties

Attempt these before reading the
[solutions](./04-seismic-inversion-reservoir-solutions.md). The lesson is
[04 Seismic Inversion for Reservoir Properties](../04-seismic-inversion-reservoir.md).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Two layers have impedances 6.60 and 7.40 MRayl. Compute the reflection
coefficient exactly and with the approximation $r \approx \tfrac12\Delta\ln Z$;
report the difference as a percentage of the exact value.

**★2.** Write the convolutional forward model for log-impedance inversion, the
Tikhonov objective function and the resulting normal equations. State the units
of each symbol.

**★3.** A 35 Hz Ricker has negligible energy below 8 Hz and above 60 Hz. State
which frequency band of the impedance is (a) recoverable from the trace and
(b) invisible to it, in one sentence each.

## ★★ Applied

**★★4.** The inversion of a trace with 3% noise returns an impedance error of
4.3% when the background is correct. Using the demonstration's measured
sensitivity, estimate the error if the background level is 4% too low, and state
which term dominates the total error budget.

**★★5.** From the demonstration's thin-bed table, report the recovered contrast
and the RMS width for a 12 ms bed, and state the two systematic errors and their
approximate sizes. Then state whether an interpreter could infer the bed
thickness from the impedance result alone.

**★★6.** The trace has 3% noise and the relative data residual for a well-fit
model is therefore about 0.03. Using the demonstration's table, choose
$(\lambda,\mu)$ and justify the choice. Explain what happens at
$\mu = 10^{-1}$ and why that is diagnosable.

## ★★★ Research-oriented

**★★★7.** Design a sensitivity study that separates the noise-driven and
model-driven parts of the impedance uncertainty, with a stated number of
realisations, a stated set of background perturbations, and a stated metric.
Predict the ordering of the two contributions and the experiment's failure mode.

**★★★8.** Quantify the error of the linearisation $r \approx \tfrac12\Delta\ln Z$
for reflection coefficients of 0.05, 0.10 and 0.25, and state the coefficient
magnitude above which a full (non-linear) inversion is required for a 1%
amplitude accuracy.
