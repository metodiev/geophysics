# Exercises — 18-07-05 Pitfalls: Inconsistent Physics, Weighting, Over-Coupling

Attempt these before reading the
[solutions](./05-joint-inversion-pitfalls-solutions.md). The lesson is
[05 Pitfalls: Inconsistent Physics, Weighting, Over-Coupling](../05-joint-inversion-pitfalls.md).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** For weights $w_1 = 10^{-3}$, $w_2 = 1$, state which data set the joint
solution effectively ignores and give the printed number that proves it.

**★2.** Define chi per datum and state the value expected when a model explains
data at its stated noise level.

**★3.** In the over-coupling table, list the $\mu$ values where both chi values
are below 2, and the $\mu$ values where the model error is below the uncoupled
error.

## ★★ Applied

**★★4.** From the weight sweep, find the $w_1$ that minimises the model error and
the $w_1$ that brings both chi values closest to 1. State whether they agree, and
what you would do if they did not.

**★★5.** The inconsistent-physics experiment gives separate-inversion chi values
of 0.82 and 0.48 but joint chi values of 7.24 and 5.87. Explain, using the
definition of the objective, why the separate inversions can both be at the noise
level while the joint cannot.

**★★6.** Over-coupling: at $\mu = 1$ the model error (0.0281) is *lower* than at
$\mu = 0$ (0.0371), yet chi 1 rises from 1.03 to 1.46. State the two
interpretations and explain which one you can test on real data.

## ★★★ Research-oriented

**★★★7.** A joint inversion is reported with a single image, a narrative, and no
chi values. Design the minimal numerical experiment you would run with the
authors' code (or with your own reproduction) to test whether the result is
dominated by weighting, inconsistency, or over-coupling. Specify the outputs and
the decision rule for each of the three hypotheses. A specification that could
not be executed is a failed answer.

**★★★8.** Weighting, coupling and the noise model are all priors of the same
formal kind. Construct a joint inversion in which the three are deliberately
mis-specified in compensating ways so that the chi table still looks acceptable,
and state the diagnostic that would still expose the compensation.
