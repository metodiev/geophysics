# Exercises — 20-07-01 Sparse and L1 Deconvolution

Attempt these before reading the
[solutions](./01-sparse-deconvolution-solutions.md). The lesson is
[01 Sparse and L1 Deconvolution](../01-sparse-deconvolution.md). All models are
**SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Evaluate $\operatorname{prox}_{t\lvert\cdot\rvert}(x)$ for
$(x, t) = (3.0, 0.5)$, $(-0.2, 0.5)$, $(0.4, 0.5)$ and $(0.4, 1.0)$. State in
one sentence which of these is a "sparse" outcome and why.

**★2.** The demonstration reports $\lVert W \rVert_2^{2} = 11.961$ from the SVD
and 11.934 from 200 power iterations. Compute the step size $1/L$ used by ISTA
in each case, and the relative difference between them.

**★3.** A colleague runs ISTA with $L = 8.0$ on this operator and the iterates
diverge. Explain why, using the definition of $L$ and the quantity measured in
★2.

## ★★ Applied

**★★4.** Using the penalty table of the lesson (residual, nonzero count and
amplitude ratio for $\lambda \in \{0.01, 0.05, 0.1, 0.3, 1.0\}$), choose a
$\lambda$ for a study that must report amplitudes to within 15 % and must keep
the residual below 12 %. Justify the choice with the two numbers and state what
you give up.

**★★5.** The damping search found $\mu = 2.256\times10^{-1}$ gives an L2
solution with residual 9.54 %, against 9.62 % for the L1 solution at
$\lambda = 0.10$. Count the samples: L1 has 19 above $10^{-3}$; L2 has 351 above
$10^{-3}$, 73 above 10 % of its peak and 13 above 50 % of its peak. Compute the
ratio of "effectively nonzero" samples and explain why the comparison at matched
residual is the only fair one.

**★★6.** The kurtosis of the true reflectivity is 45.961, of the data 13.114, of
the L1 solution at $\lambda = 0.1$ it is 49.190, and of the L2 solution 15.314.
For a Gaussian variable the kurtosis is 3. Explain what the four numbers measure
and why the L1 solution's value is *closer to the truth than the data's own*.

## ★★★ Research-oriented

**★★★7.** Design an experiment that measures the shrinkage bias of the L1
solution as a function of the local signal-to-noise ratio. Specify: the
generator, the metric, the sweep, the number of trials per cell, and the
prediction you would test. Include a debiasing variant and state where it should
help and where it should hurt.

**★★★8.** The subgradient check reports $\max\lvert W^{T}(Wr-d) +
\lambda\operatorname{sign}(r)\rvert = 1.739\times10^{-7}$ on the support and
$0.000$ for $\max(0, \lvert W^{T}(Wr-d)\rvert - \lambda)$ off it. Explain why
these two numbers are not of the same order, and what each would look like if
the iteration had been stopped after 20 steps instead of 800.
