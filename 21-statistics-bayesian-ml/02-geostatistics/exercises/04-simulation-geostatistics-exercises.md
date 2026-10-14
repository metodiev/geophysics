# Exercises — 21-02-04 Conditional Simulation and Uncertainty Realisations

Attempt these before reading the
[solutions](./04-simulation-geostatistics-solutions.md). The lesson is
[04 Conditional Simulation](../04-simulation-geostatistics.md). All fields are
**SYNTHETIC**; numbers quoted from the demonstration reproduce its output.

## ★ Foundational

**★1.** An ensemble has $L = 200$ realisations. Compute the relative standard
error of the ensemble variance and of the ensemble standard deviation. Then
compute both for $L = 1000$.

**★2.** The E-type estimate has spatial variance $0.3138$ while the mean
ensemble variance is $0.5022$. Compute their ratio and state what the ratio
measures.

**★3.** At a location, $30$ of $200$ realisations exceed a cut-off of
$2.0\ \mathrm{g/t}$. Compute the estimated exceedance probability and its
binomial standard error.

## ★★ Applied

**★★4.** Using the error-simulation identity
$Z_{cs} = Z_k + [Z_u - Z_{uk}]$, show that $Z_{cs}$ reproduces the data exactly
and that its conditional expectation given the data is the kriging estimate
$Z_k$.

**★★5.** A study needs the ensemble variance at each node to $2\ \%$ relative
precision. Using $\mathrm{RSE} = \sqrt{2/L}$, compute the required number of
realisations. State what changes if the target is a $95\ \%$ interval rather than
a variance.

**★★6.** Explain why the E-type estimate's spatial variance is smaller than the
mean realisation variance, and predict how the gap changes if the four
conditioning data are replaced by forty. Give the direction and the reasoning.

## ★★★ Research-oriented

**★★★7.** Specify a **connectivity study** that measures how the connected
volume above a threshold depends on the number of realisations and on the
variogram range. State the grid, the field construction, the connectivity metric,
the replicate count, and the prediction as the range increases. A specification
that could not be executed is a failed answer.

**★★★8.** Design a **convergence study** for a simulation algorithm: an
experiment that determines how many realisations are needed for the ensemble mean
to approximate the kriging estimate to a stated tolerance, as a function of the
number of conditioning data. State the metric, the tolerance, the replicate
count, and the predicted scaling with the number of realisations.
