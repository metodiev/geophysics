# Exercises — 21-01-05 Nonparametric Statistics and Kernel Density Estimation

Attempt these before reading the
[solutions](./05-nonparametric-methods-solutions.md). The lesson is
[05 Nonparametric Methods](../05-nonparametric-methods.md). All samples are
**SYNTHETIC**; numbers quoted from the demonstration reproduce its output.

## ★ Foundational

**★1.** An ECDF is estimated from $n = 200$ independent values at a point where
the true CDF equals $F = 0.4$. Compute $\operatorname{Var}\hat F_n$ and its
square root, and state the width of the DKW band at $n = 200$ for confidence
$1 - 2e^{-2}$.

**★2.** Two groups of $n_1 = n_2 = 40$ give $U = 678.0$. Compute
$\mathbb E[U]$, $\operatorname{sd}(U)$ and the normal $z$, then the two-sided
$p$-value, and compare with the demonstration's permutation-free value
$0.2423$.

**★3.** In a paired experiment $15$ of $30$ differences are positive. Compute
the exact two-sided sign-test $p$-value using the binomial distribution with
$p = 1/2$ and compare with the demonstration's $1.0000$.

## ★★ Applied

**★★4.** For $n = 30$ paired differences the Wilcoxon signed-rank statistic is
$W^{+} = 226.0$. Compute $\mathbb E[W^{+}]$, $\operatorname{Var}(W^{+})$ and the
normal $z$, then the two-sided $p$-value, and compare with the demonstration's
$0.9032$.

**★★5.** For the demonstration's density sample, $s = 1.663$ and $n = 200$.
Compute Silverman's and Scott's bandwidths from the formulas and compare with
the printed $0.6108$ and $0.5762$. Explain which term of the $\min$ was
selected.

**★★6.** Starting from
$\mathrm{MISE}(h) \approx \frac{h^{4}}{4}(\int u^{2}K)^{2}\int(f'')^{2}
+ \frac{1}{nh}\int K^{2}$, derive the optimal bandwidth and show that it scales
as $n^{-1/5}$. State the constant for the Gaussian kernel, for which
$\int u^{2}K\,\mathrm du = 1$ and $\int K^{2}\,\mathrm du = (4\pi)^{-1/2}$.

## ★★★ Research-oriented

**★★★7.** Specify a **power study** comparing Welch's $t$ test, Mann-Whitney
and a permutation test, as a function of contamination fraction
$f \in [0, 0.3]$ and true shift $\delta \in [0, 1]\sigma$. State the group sizes,
the replicate count needed to resolve a $5\ \%$ power difference, and the
prediction for each test at $f = 0$ and at $f = 0.3$. A specification that could
not be executed is a failed answer.

**★★★8.** Design a **cross-validated bandwidth selector** for the density of a
bimodal sample and state the diagnostic that shows it has selected a bandwidth
that under-smooths the trough. Give the statistic, the search grid, the
selection criterion, and the way you would detect the failure.
