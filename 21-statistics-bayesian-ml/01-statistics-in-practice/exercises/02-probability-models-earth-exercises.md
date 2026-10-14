# Exercises — 21-01-02 Choosing Probability Models for Earth Data

Attempt these before reading the
[solutions](./02-probability-models-earth-solutions.md). The lesson is
[02 Probability Models](../02-probability-models-earth.md). All samples are
**SYNTHETIC**; numbers quoted from the demonstration are reproduced exactly.

## ★ Foundational

**★1.** A lognormal permeability sample has $\hat\sigma_{\ln} = 1.0$ and median
$100\ \mathrm{mD}$. Compute the mean-median ratio and the distribution mean.
State the unit of each.

**★2.** The same sample is fitted with both a normal family ($k = 2$) and a
lognormal family ($k = 3$). Write down the AIC of each and compute the penalty
the lognormal pays for its extra parameter. Given
$\ell_{\text{normal}} = -27050.2$ and $\ell_{\text{lognormal}} = -24047.4$,
compute the likelihood gap $2(\ell_{\text{ln}} - \ell_{\text{n}})$ and the net
AIC difference.

**★3.** Compute the skewness of a lognormal with $\sigma_{\ln} = 1$ from the
closed form, and compare it with the sample skewness $6.527$.

## ★★ Applied

**★★4.** The fitted normal model has $\hat\mu = 162.26\ \mathrm{mD}$,
$\hat\sigma = 209.30\ \mathrm{mD}$. Compute $P(X > 1000\ \mathrm{mD})$ by
converting to a $z$-score, and compare it with the empirical value $0.00900$ and
the lognormal value $0.01015$. Express both ratios.

**★★5.** Repeat the calculation of ★1 for $\sigma_{\ln} = 0.5$ and
$\sigma_{\ln} = 2.0$. Tabulate the mean-median ratio and the skewness, and state
how the extrapolation risk scales with $\sigma_{\ln}$.

**★★6.** The GEV fit to the block maxima has $\hat\mu = 2.0285$,
$\hat\sigma = 0.4030$ and $\hat\xi = 0.1277$. Compute the *Gumbel* return level
$\mu - \sigma\ln(-\ln(1-1/T))$ for $T = 10, 100, 1000$ and compare each with the
fitted GEV values $2.8167$, $3.4306$ and $3.8782$. What does the comparison
show about mixing families?

## ★★★ Research-oriented

**★★★7.** Specify a Monte-Carlo study that measures the *sampling distribution*
of $\hat\sigma_{\ln}$ and of the GEV shape $\hat\xi$ as a function of sample size,
for data known to be lognormal and Gaussian respectively. State the estimator,
the metric, the sample sizes, and the prediction for the bias. The study must be
executable as described.

**★★★8.** A resource model reports a grade-tonnage curve that integrates a
lognormal above a cut-off. Design the sensitivity experiment that would show how
the tonnage above the cut-off depends on the family choice, and state the cut-off
beyond which the answer is dominated by the model rather than the data.
