# Exercises — 01-13-06 Point Estimation, Bias, Consistency and Efficiency

Attempt these closed-book before reading
[the solutions](./06-estimation-theory-solutions.md). The lesson is
[01-13-06](../06-estimation-theory.md).

Marking: ★ foundational, ★★ applied, ★★★ research-oriented.

For every claim about an estimator, say whether it is a statement about the estimator
or about a particular estimate.

---

## ★ Foundational

**★1.** A sample of $n = 10$ observations comes from a population with variance
$\sigma^{2} = 9$. Compute $E[s_n^{2}]$, the bias of $s_n^{2}$, and the relative bias.

**★2.** Two unbiased estimators of the same parameter have variances $4$ and $6$.
Compute the relative efficiency of the first with respect to the second.

**★3.** Counts of events in five equal intervals are $3, 5, 2, 4, 6$. Compute the
maximum likelihood estimate of the Poisson rate and the Cramér–Rao standard error
bound.

**★4.** Waiting times with an exponential distribution give a sample of $n = 8$ with
total $\sum x_i = 4.0$. Compute the maximum likelihood estimate of the rate, its
exact bias for this $n$, and its exact variance.

---

## ★★ Applied

**★★5.** For a Poisson$(\lambda)$ sample of size $n = 25$ with $\lambda = 4$, compute
the Fisher information for one observation, the Cramér–Rao lower bound on the variance
of any unbiased estimator of $\lambda$, and the corresponding standard error.

**★★6.** For a Laplace density $f(x) = \frac{1}{2b}e^{-|x-\mu|/b}$:

(a) compute the Fisher information for $\mu$;
(b) state the Cramér–Rao bound for a sample of $n$;
(c) compute the variance of the sample mean;
(d) hence compute the relative efficiency of the sample mean against the sample median.

**★★7.** An estimator has bias $2/n$ and variance $\sigma^{2}/n$ with
$\sigma = 1.5$. Is it consistent? Justify with the two sufficient conditions, and
compute its mean squared error at $n = 4$.

**★★8.** The maximum likelihood estimator of a Gaussian variance is
$\hat\sigma^{2} = \frac{1}{n}\sum(x_i - \bar x)^{2}$. State its expectation, and
calculate both its bias and the mean squared error of the two variance estimators
when $\sigma^{2} = 9$ and $n = 10$. Which has the smaller MSE?

---

## ★★★ Research-oriented

**★★★9.** Derive $E[s_n^{2}] = \frac{n-1}{n}\sigma^{2}$ starting from

$$\sum_{i=1}^{n}(x_i - \bar x)^{2} = \sum_{i=1}^{n}(x_i - \mu)^{2}
- n(\bar x - \mu)^{2},$$

stating what is assumed about the $x_i$ and where the independence enters.

**★★★10.** Consider a contaminated population: with probability $0.9$ a value is drawn
from $\mathcal{N}(0,1)$ and with probability $0.1$ from $\mathcal{N}(0,10^{2})$.

(a) Compute the population variance.
(b) Compute the variance of the sample mean for $n = 25$.
(c) Using the asymptotic result $\operatorname{Var}(\tilde X) \approx
1/(4nf(\mu)^{2})$ for the sample median, compute the median's variance for $n = 25$.
(d) Compute the ratio and explain why the mean loses so badly, in a sentence that
names the mechanism.

**★★★11.** For a $\text{Uniform}(0,\theta)$ sample, the maximum likelihood estimator
of $\theta$ is $\hat\theta = X_{(n)}$, the largest observation.

(a) State precisely why the Cramér–Rao bound does not apply to this family, and derive
$\operatorname{Var}(\hat\theta) = \theta^{2}n/[(n+1)^{2}(n+2)]$. Compare its order in
$n$ with the $1/(nI)$ bound one would obtain by differentiating the density anyway.
(b) A colleague proposes the midrange $(X_{(1)} + X_{(n)})/2$ as a location estimator
for general data because it is unbiased and efficient for the uniform family. Explain
why it becomes unreliable for a heavy-tailed distribution, naming the robustness
concept that quantifies the failure.
