# Exercises — 18-03-03 Choosing the Trade-Off: L-Curve, GCV, Discrepancy Principle

Attempt these before reading the
[solutions](./03-parameter-choice-solutions.md). The lesson is
[03 Choosing the Trade-Off: L-Curve, GCV, Discrepancy Principle](../03-parameter-choice.md).
All models are **SYNTHETIC**. Reference values from the demonstration:
$\kappa_2 = 1.163\times10^{6}$, noise $1.1063\ \mathrm{mGal}$ ($0.50\%$ of the
peak), $n\sigma_e^2 = 6.6178\times10^{-5}$ in standard-form units, 400 $\alpha$
values from $10^{-12}$ to $10^{1}$.

## ★ Foundational

**★1.** At the selected $\alpha$ the residual satisfies
$\|Km_\alpha-d\|^2 = 0.4\,n\sigma_e^2$. State whether the parameter should be
increased or decreased, and give the reason in terms of what is being fitted.

**★2.** Compute the GCV function at $\alpha = 10^{-6}$ from
$\|Km_\alpha-d\|^2 = 2.7155\times10^{-5}$ and $\sum_i f_i = 31.291$ with
$n = 64$, and compare with the curve value $1.627\times10^{-6}$ printed by the
demonstration.

**★3.** The L-curve corner sits at $\alpha = 2.673\times10^{-5}$ with residual
$0.507\,n\sigma_e^2$. State in one sentence what is wrong with that solution and
which test revealed it.

## ★★ Applied

**★★4.** The GCV minimum is flat: 32 of 400 grid points lie within $5\%$ of it,
spanning $\alpha = 1.62\times10^{-4}$ to $1.66\times10^{-3}$. Compute the ratio
of the endpoints and state how many significant figures of $\alpha$ the data can
support.

**★★5.** Using the failure-mode table, compute the error ratio
$E(0.25)/E(1.00)$ for the discrepancy principle when $\sigma_e$ is
underestimated by a factor of four, and express the result as an order of
magnitude. Then do the same for overestimating by a factor of four, and explain
the asymmetry using the shape of the trade-off curve.

**★★6.** The Monte Carlo gives an interquartile range of $0.15$ decades in
$\log_{10}\alpha$ for the discrepancy rule and $0.39$ for the L-curve. Convert
both to multiplicative factors on $\alpha$, and state which of the two rules you
would trust to reproduce a colleague's result.

## ★★★ Research-oriented

**★★★7.** Write the GCV function for the case $L = D$ (a first-difference
penalty) in terms of the generalised singular values of $(K,D)$. State what
changes in the denominator and why GCV's "effective number of parameters" is no
longer $\sum_i f_i$ with $f_i$ from the unpenalised SVD.

**★★★8.** Design a Monte Carlo study that measures the bias of the L-curve rule
as a function of the fitted decay $q \in \{1.6, 3.2, 6.3\}$ at fixed noise level,
specify the statistic (median error divided by the oracle error), the number of
realisations needed for a stated precision, and the prediction. State what result
would show that the L-curve is *not* systematically biased.
