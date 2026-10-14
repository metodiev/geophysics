# Exercises — 20-08-05 Climate Time-Series Analysis and Modes of Variability

Attempt these before reading the
[solutions](./05-climate-timeseries-solutions.md). The lesson is
[05 Climate Time-Series Analysis and Modes of Variability](../05-climate-timeseries.md).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Write the one-sided AR(1) spectrum. For $\rho = 0.7$ and $\sigma = 1$,
compute $S(0)$ and $S(1/2)$ and their ratio.

**★2.** State the pointwise 95 % level of a raw periodogram in terms of
$S(f)$ and compute the numerical multiplier.

**★3.** For 200 frequency bins, compute the corrected multiplier
$-\log(0.05/200)$ and the ratio to the pointwise multiplier. State what the ratio
means.

## ★★ Applied

**★★4.** From the measured counts (22 bins above the white-noise level, 12 above
the red-noise level), compute the expected number of false exceedances at the
pointwise 5 % level for a white-noise series with 300 bins, and say why 12 is
still not evidence of 12 oscillations.

**★★5.** The injected oscillation has a variance of $A^{2}/2$ with $A = 0.35$.
Compute it, compare with the red-noise level at that frequency (29.680), and
state the signal-to-noise ratio in spectral terms. Then explain why the
oscillation was declared against the white-noise null.

**★★6.** Two independent realisations of the same two-mode generator gave EOF 1
with 14.34 % and 12.64 % of the variance, and a pattern correlation of 0.970.
Compute the relative difference in explained variance and state what you would
report as the uncertainty on the fraction.

## ★★★ Research-oriented

**★★★7.** Design a test for a spectral peak that accounts for the fact that the
period, amplitude and phase are all estimated from the data. Specify the null,
the test statistic, the calibration procedure via surrogate data, and the way you
would report the peak's significance alongside its fitted parameters. State why
a phase-randomised surrogate is the right null for this purpose.

**★★★8.** The lesson's multiplicity correction is the simple Bonferroni form.
Design an experiment that measures, for a red-noise series of $n = 600$ monthly
samples, the *true* family-wise error rate of the peak search for a range of
threshold multipliers between 2.996 and 12, and compare it with the Bonferroni
prediction. Predict whether Bonferroni is conservative or anti-conservative here
and why.
