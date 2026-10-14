# Exercises — 01-13-05 Sampling Distributions, Law of Large Numbers and CLT

Attempt these closed-book before reading
[the solutions](./05-sampling-and-clt-solutions.md). The lesson is
[01-13-05](../05-sampling-and-clt.md).

Marking: ★ foundational, ★★ applied, ★★★ research-oriented.

State the hypothesis you are using whenever you invoke a limit theorem.

---

## ★ Foundational

**★1.** For observations with standard deviation $\sigma = 2$, a sample of size
$n = 100$ and a tolerance $\varepsilon = 0.5$: compute (a) the Chebyshev bound on
$P(|\bar X - \mu| > \varepsilon)$ and (b) the exact value if the observations are
Gaussian. Comment on the ratio.

**★2.** For single-reading standard deviation $\sigma = 3$: compute the standard
error of the mean for $n = 36$, and the $n$ required for a standard error of $0.1$.

**★3.** A sample mean of $52$ is computed from $n = 9$ observations with known
$\sigma = 6$, under a null hypothesis of $\mu = 50$. Compute the standardised
statistic $z$.

**★4.** For each parent, state whether the law of large numbers holds and whether the
classical CLT applies: (a) $\text{Uniform}(0,1)$; (b) $\text{Exp}(1)$;
(c) Pareto with tail exponent $\alpha = 1.5$; (d) Pareto with $\alpha = 2.5$;
(e) standard Cauchy.

---

## ★★ Applied

**★★5.** For an $\text{Exp}(1)$ parent, the standardised third absolute moment is
$E|X-\mu|^{3}/\sigma^{3} = 2.414553$. Using the Berry–Esseen bound with the constant
$C = 0.4748$, compute the bound on the maximum CDF discrepancy at $n = 100$ and at
$n = 300$. The lesson measured $0.013241$ at $n = 300$. What does the comparison say
about the usefulness of the bound?

**★★6.** A Monte Carlo estimate of a probability near $0.1$ must be reported to
$\pm 0.001$. How many independent draws are required? State the formula you used.

**★★7.** For a parent with tail exponent $\alpha = 2.5$, the fluctuation of the
sample mean scales as $n^{-(1-1/\alpha)}$. By what factor must the sample size
increase to halve the precision of the mean?

**★★8.** Repeat ★7 for $\alpha = 1.5$ and compare the two factors. Explain in one
sentence why a smaller tail exponent makes the mean more expensive to estimate.

---

## ★★★ Research-oriented

**★★★9.** Prove the weak law of large numbers for i.i.d. variables with finite
variance, stating both the inequality you use and the hypothesis that makes it
applicable.

**★★★10.** Explain, with a scaling argument, why the fluctuation of the sample mean
of a Pareto$(\alpha)$ variable with $1 < \alpha < 2$ scales as
$n^{-(1-1/\alpha)}$ rather than as $n^{-1/2}$. Your argument should identify which
observation dominates the mean and how large it is.

**★★★11.** You are asked to state the precision of a Monte Carlo propagation result
for a quantity whose distribution is believed to have a power-law tail with
$\alpha = 1.7$.

(a) Explain why the usual $s/\sqrt N$ rule may not apply.
(b) State a diagnostic that would reveal the problem.
(c) State what you would report instead.
