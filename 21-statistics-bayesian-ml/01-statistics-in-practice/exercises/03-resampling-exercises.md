# Exercises — 21-01-03 Resampling: Bootstrap, Jackknife, Permutation Tests

Attempt these before reading the
[solutions](./03-resampling-solutions.md). The lesson is
[03 Resampling](../03-resampling.md). All samples are **SYNTHETIC**; numbers
quoted from the demonstration reproduce its output.

## ★ Foundational

**★1.** A sample of five densities is $\{2.60, 2.72, 2.68, 2.75, 3.40\}$ in
$\mathrm{g/cm^3}$. Compute the leave-one-out means $\hat\theta_{(i)}$ and the
jackknife bias estimate. Explain the result.

**★2.** A bootstrap percentile interval for a mean is
$[1.1688, 1.7151]$ a.u. with point estimate $1.4339$ a.u. State (a) what
population this is an interval for, (b) what fraction of bootstrap replicates
fall below the lower endpoint, and (c) whether the interval is symmetric about
the point estimate.

**★3.** In a two-sample comparison the observed difference of means is
$-0.5086$ a.u., and $240$ of $5000$ shuffles produce an absolute difference at
least as large. Compute the permutation $p$-value with the $+1$ correction.

## ★★ Applied

**★★4.** Derive the jackknife variance of the sample mean and show that it
equals $s^2/n$ exactly, where $s^2$ is the unbiased sample variance. Then check
it against the demonstration's mean values: jackknife standard error $0.1412$
and bootstrap standard error $0.1404$.

**★★5.** The bootstrap atom at the sample maximum is $1-(1-1/n)^n$. Compute it
for $n = 50$ and $n = 100$, and compare with the demonstration's measured
fraction $0.6346$ of bootstrap maxima equal to the sample maximum.

**★★6.** The percentile endpoint of a bootstrap interval has Monte-Carlo
standard error $\sqrt{p(1-p)/B}\,/\,f(q_p)$, where $f$ is the bootstrap density
at the $p$-quantile. Using a Gaussian approximation with the median's bootstrap
standard error $0.1478$ a.u. and $B = 10^4$, estimate the endpoint error at
$p = 0.025$ and compare it with the interval width $0.5231$ a.u.

## ★★★ Research-oriented

**★★★7.** Specify a **moving-block bootstrap** for a stationary time series of
$n = 1000$ daily GNSS positions with an estimated integrated autocorrelation
time of $\tau_{\text{int}} = 8$ days. State the block length, the number of
blocks per resample, the statistic, and the diagnostic that shows the block
length is adequate. Give the specification, not a discussion.

**★★★8.** Design a **coverage study** that measures the actual coverage of the
percentile bootstrap interval for the median of a skewed sample, as a function
of $n \in \{10, 20, 50, 100, 500\}$. State the replicate count needed to resolve
coverage departures of $2\ \%$, the nominal level, and the predicted direction of
the error at small $n$.
