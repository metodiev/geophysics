# Exercises — 16-05-05 CMIP, Model Intercomparison and Ensemble Design

Attempt these before reading the
[solutions](./05-coupled-model-intercomparison-solutions.md). Lesson:
[05 Model Intercomparison and Ensemble Design](../05-coupled-model-intercomparison.md).
All models and data are **SYNTHETIC**; no real model or ensemble size is used.
The demonstration is
[`../code/coupled_model_intercomparison_demo.py`](../code/coupled_model_intercomparison_demo.py).

## ★ Foundational

**★1.** Internal variability per member is $\sigma_i = 0.4\ \mathrm{K}$. How
many members are needed for the standard error of the ensemble mean to fall
below $0.05\ \mathrm{K}$?

**★2.** Three models respond to the same forcing with $1.5$, $2.5$ and
$5.0\ \mathrm{K}$. Compute the mean and the structural standard deviation (use
$N-1$ in the denominator).

**★3.** With the structural standard deviation from ★2 and $\sigma_i = 0.5\
\mathrm{K}$, compute the total spread with $25$ members per model.

## ★★ Applied

**★★4.** For the same three-model ensemble, tabulate the total spread for
$N = 1, 4, 16, 100, 10000$ members per model and state at what point the value
is within $1\%$ of the structural standard deviation.

**★★5.** An archive contains three models with $10$, $40$ and $50$ members and
ensemble means $2.0$, $3.0$ and $4.0\ \mathrm{K}$. Compute the member-weighted
and model-weighted means and state the difference.

**★★6.** Explain why inverse-variance weighting cannot be applied to a real
multi-model archive without additional assumptions, and name the assumption that
is most likely to fail.

## ★★★ Research-oriented

**★★★7.** Design an ensemble adequate to estimate the forced response of a
stated climate variable over a stated region, given a structural spread and an
internal variability measured from a pilot study. Specify the number of models,
the number of members per model, the weighting, and one assumption that your
design cannot test.

**★★★8.** A study reports the mean of eight models as "the" projection with a
standard error computed across the eight. Write a critique: state what the
standard error measures, what it omits, and one diagnostic that would reveal the
problem.
