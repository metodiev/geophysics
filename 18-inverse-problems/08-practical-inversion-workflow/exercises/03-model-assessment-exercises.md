# Exercises — 18-08-03 Assessing a Model: Resolution, Artifacts, Alternatives

Attempt these before reading the
[solutions](./03-model-assessment-solutions.md). The lesson is
[03 Assessing a Model: Resolution, Artifacts, Alternatives](../03-model-assessment.md).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** List the five assessment items and the single quantity that represents
each.

**★2.** For a Gaussian posterior, a 95% admitted range is about how many
standard deviations wide? State the value and the assumption.

**★3.** From the table, state the PSF half-width at $z = 6.25$ km and whether a
0.5-km feature at that depth can be resolved.

## ★★ Applied

**★★4.** The perturbation test gives signature 0.953 and posterior norm 0.587 at
a width of 3 km. State the verdict under each criterion separately, and what to
do when the two criteria disagree.

**★★5.** The admitted range is 0.3402 at 2.25 km and 0.5468 at 19.75 km. Compute
the ratio and state two reasons the deep edge is worse.

**★★6.** A report claims "a 0.30 contrast at 6.25 km". The model value there is
0.3884 with an admitted 95% range of (0.2094, 0.5674). State whether the claim is
supported, and how you would rewrite it.

## ★★★ Research-oriented

**★★★7.** Design an assessment protocol for a nonlinear inversion (for example
full-waveform or a 2-D resistivity problem) in which the linear resolution
matrix is not available. Specify what replaces each of the five items and the
numerical cost of each. A specification that could not be executed is a failed
answer.

**★★★8.** The perturbation test uses the posterior covariance of a linearised
problem. Construct a case in which the posterior norm declares a perturbation
inadmissible but the perturbation is in fact consistent with the data (or vice
versa), and state what would have to be measured to detect it.
