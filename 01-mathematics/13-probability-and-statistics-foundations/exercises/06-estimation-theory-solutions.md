# Solutions — 01-13-06 Point Estimation, Bias, Consistency and Efficiency

> **Read this after attempting the exercises, not before.**
>
> Numbers were computed. Where an estimator is compared with the Cramér–Rao bound,
> the regularity conditions are checked, because a bound applied outside its
> hypotheses is a source of confident errors.

---

## ★1 — Bessel's correction in numbers

$$E[s_n^{2}] = \frac{n-1}{n}\sigma^{2} = \frac{9}{10} \times 9 = \boxed{8.1}.$$

The bias is

$$\text{bias} = 8.1 - 9 = \boxed{-0.9}, \qquad
\frac{\text{bias}}{\sigma^{2}} = -\frac{1}{n} = \boxed{-0.10}.$$

A $10\%$ understatement at $n = 10$. The magnitude of the relative bias is exactly
$1/n$, so a hundred-station survey has a $1\%$ bias, which is why the correction
matters most in small surveys and in single-borehole datasets where $n$ may be five.

---

## ★2 — Relative efficiency

$$\text{relative efficiency} = \frac{\operatorname{Var}(\hat\theta_2)}
{\operatorname{Var}(\hat\theta_1)} = \frac{6}{4} = \boxed{1.5}.$$

The convention is that the ratio is stated with the more efficient estimator in the
numerator, so "the first estimator is $1.5$ times as efficient as the second", or
equivalently the second "has a relative efficiency of $67\%$". Because both are
unbiased, relative efficiency equals the ratio of mean squared errors, and stating
which convention is in use avoids the reciprocal confusion that plagues reports.

---

## ★3 — Poisson rate by maximum likelihood

The likelihood is $L(\lambda) = \prod_i \lambda^{x_i}e^{-\lambda}/x_i!$, so

$$\ell(\lambda) = \left(\sum_i x_i\right)\ln\lambda - n\lambda - \sum_i\ln x_i!,
\qquad \frac{d\ell}{d\lambda} = \frac{\sum_i x_i}{\lambda} - n = 0.$$

Hence

$$\hat\lambda = \bar x = \frac{3+5+2+4+6}{5} = \frac{20}{5} = \boxed{4}.$$

**Cramér–Rao bound.** The Fisher information for one Poisson observation is

$$I(\lambda) = E\left[\left(\frac{X - \lambda}{\lambda}\right)^{2}\right]
= \frac{\operatorname{Var}(X)}{\lambda^{2}} = \frac{\lambda}{\lambda^{2}} =
\frac{1}{\lambda},$$

using the score $\partial_\lambda \ln p = (X-\lambda)/\lambda$ and the Poisson
identity $\operatorname{Var}(X) = \lambda$. Therefore

$$\operatorname{Var}(\hat\lambda) \ge \frac{1}{nI(\lambda)} = \frac{\lambda}{n}
= \frac{4}{5} = \boxed{0.8},$$

with a standard error bound of $\sqrt{0.8} = 0.894$. The sample mean attains the
bound, so it is the efficient estimator here.

---

## ★4 — Exponential rate

With $n = 8$ and $\sum x_i = 4.0$,

$$\hat\lambda = \frac{n}{\sum_i x_i} = \frac{8}{4.0} = \boxed{2.0}.$$

**Exact bias.** $\bar X$ is gamma distributed with shape $n$ and mean $1/\lambda$, and
$E[1/\bar X] = n\lambda/(n-1)$ for $n > 1$:

$$E[\hat\lambda] = \frac{n\lambda}{n-1} = \frac{8 \times 2}{7} = 2.285714, \qquad
\text{bias} = +0.285714\ (+\tfrac{1}{7}).$$

**Exact variance.** For $\bar X \sim \text{Gamma}(n, \text{rate } n\lambda)$,

$$\operatorname{Var}\left(\frac{1}{\bar X}\right)
= \frac{n^{2}\lambda^{2}}{(n-1)^{2}(n-2)} = \frac{64 \times 4}{49 \times 6}
= \frac{256}{294} = 0.870748, \qquad \text{se} = 0.933139.$$

**Comparison with the bound.** The Cramér–Rao bound is $\lambda^{2}/n = 4/8 = 0.5$.
The MLE's finite-sample variance of $0.8707$ is $74\%$ above the bound at $n = 8$, and
its bias is $14\%$ of $\lambda$. Both discrepancies shrink as $n$ grows — the bias as
$1/n$ and the inefficiency as $1/n$ at leading order — which is the standard pattern:
maximum likelihood is asymptotically efficient and finitely biased, and the bias must
be reported when $n$ is small enough for it to matter.

---

## ★5 — Poisson Cramér–Rao bound

From ★3, $I(\lambda) = 1/\lambda$, so with $\lambda = 4$ and $n = 25$:

$$I(\lambda) = \frac{1}{4} = 0.25, \qquad
\operatorname{Var}(\hat\lambda) \ge \frac{\lambda}{n} = \frac{4}{25} =
\boxed{0.16}, \qquad \text{se} \ge \boxed{0.4}.$$

**A note on the scaling.** The bound decreases as $1/n$ and grows linearly in
$\lambda$: relative precision $\text{se}/\lambda = 1/\sqrt{n\lambda}$ improves only as
the square root of the expected total count $n\lambda$. To halve the relative
uncertainty of a rate estimate you need four times the total observation time, which
is the reason rate estimates from short catalogues carry large uncertainties even
when the rate itself is high.

---

## ★6 — Laplace model, and the cost of using the mean

**(a)** The log-density is $\ln f(x) = -\ln(2b) - |x-\mu|/b$, whose derivative with
respect to $\mu$ (valid for $x \ne \mu$) is $\operatorname{sgn}(x-\mu)/b$. Hence

$$I(\mu) = E\left[\frac{\operatorname{sgn}(X-\mu)^{2}}{b^{2}}\right]
= \frac{1}{b^{2}}.$$

**(b)** For $n$ independent observations,

$$\operatorname{Var}(\hat\mu) \ge \frac{1}{nI(\mu)} = \boxed{\frac{b^{2}}{n}}.$$

**(c)** The Laplace variance is $2b^{2}$, so the sample mean has

$$\operatorname{Var}(\bar X) = \frac{2b^{2}}{n}.$$

**(d)** The sample median attains the bound asymptotically, since for any density
$\sqrt n(\tilde X - \mu) \to \mathcal{N}(0, 1/(4f(\mu)^{2}))$ and here
$f(\mu) = 1/(2b)$, giving variance $b^{2}/n$. Therefore

$$\text{relative efficiency of the mean} = \frac{b^{2}/n}{2b^{2}/n} =
\boxed{0.5}.$$

The mean wastes exactly half the information in the data. **The interpretation to
carry away:** "efficient" is not a property of the mean; it is a property of the mean
*under a stated model*. Under a Gaussian model the mean is efficient; under a Laplace
model the median is, and the mean is half as good.

---

## ★7 — Consistency of a biased estimator

The estimator has bias $2/n$ and variance $1.5^{2}/n = 2.25/n$.

**Consistency.** Both conditions hold: the bias tends to $0$, and the variance tends
to $0$. Hence the estimator is consistent by the sufficient condition
$$\text{Var} \to 0 \text{ and } \text{bias} \to 0
\ \Longrightarrow\ \text{consistency.}$$

**Mean squared error at $n = 4$.**

$$\text{MSE} = \operatorname{Var} + \text{bias}^{2} = \frac{2.25}{4} +
\left(\frac{2}{4}\right)^{2} = 0.5625 + 0.25 = \boxed{0.8125}.$$

At $n = 100$ the same expression gives $0.0225 + 0.0004 = 0.0229$, so the bias
contributes under $2\%$ of the MSE. **The general lesson:** bias is a property of a
fixed $n$ and consistency is a property of the limit; an estimator can be badly biased
in a small sample and effectively unbiased in a large one, and both statements are
true at once.

---

## ★8 — Biased and unbiased variance estimators, and their MSEs

$$\hat\sigma^{2}_{\text{MLE}} = \frac{1}{n}\sum(x_i - \bar x)^{2}, \qquad
E[\hat\sigma^{2}_{\text{MLE}}] = \frac{n-1}{n}\sigma^{2}.$$

With $\sigma^{2} = 9$ and $n = 10$:

$$E[\hat\sigma^{2}_{\text{MLE}}] = 8.1, \qquad \text{bias} = -0.9, \qquad
\text{bias}^{2} = 0.81.$$

**Variances.** For Gaussian data,
$\operatorname{Var}(s_{n-1}^{2}) = 2\sigma^{4}/(n-1)$ and
$\operatorname{Var}(s_{n}^{2}) = 2\sigma^{4}(n-1)/n^{2}$:

$$\operatorname{Var}(s_{n-1}^{2}) = \frac{2 \times 81}{9} = 18, \qquad
\operatorname{Var}(s_{n}^{2}) = \frac{2 \times 81 \times 9}{100} = 14.58.$$

**Mean squared errors.**

| Estimator | Variance | bias² | MSE |
|---|---|---|---|
| $s_{n}^{2} = \frac{1}{n}\sum(x-\bar x)^{2}$ | 14.58 | 0.81 | **15.39** |
| $s_{n-1}^{2} = \frac{1}{n-1}\sum(x-\bar x)^{2}$ | 18.00 | 0.00 | **18.00** |

The **biased** estimator has the smaller mean squared error, by $14.5\%$. For Gaussian
data the ratio is $2(n-1)/n^{2} + 1/n^{2}$ divided by $2/(n-1)$, which is less than one
for every $n > 1$, so this is not an accident of the numbers chosen: dividing by $n$
beats dividing by $n-1$ in the MSE sense at every sample size, for Gaussian data.

**What not to conclude.** Bessel's correction remains the right default, because
unbiasedness is what makes an estimator average correctly across independent problems
and because the MSE advantage is small. The exercise's purpose is to make the point
that "unbiased" and "accurate" are different words, and that choosing between
estimators requires stating the loss function first.

---

## ★9 — Deriving the expectation of $s_n^{2}$

**Assumptions.** $x_1, \dots, x_n$ are independent and identically distributed with
mean $\mu$ and variance $\sigma^{2} < \infty$.

**Algebraic identity.** Expand $\sum_i (x_i - \mu)^{2}$ about $\bar x$:

$$\sum_{i=1}^{n}(x_i - \mu)^{2} = \sum_{i=1}^{n}\left[(x_i - \bar x) + (\bar x -
\mu)\right]^{2}
= \sum_i (x_i - \bar x)^{2} + 2(\bar x - \mu)\underbrace{\sum_i(x_i - \bar x)}_{=0}
+ n(\bar x - \mu)^{2}.$$

Therefore

$$\sum_{i=1}^{n}(x_i - \bar x)^{2} = \sum_{i=1}^{n}(x_i - \mu)^{2}
- n(\bar x - \mu)^{2}.$$

**Taking expectations.** By linearity,

$$E\left[\sum_i(x_i - \bar x)^{2}\right] = \sum_i E\left[(x_i - \mu)^{2}\right]
- nE\left[(\bar x - \mu)^{2}\right] = n\sigma^{2} - n\cdot\frac{\sigma^{2}}{n}
= (n-1)\sigma^{2}.$$

The last steps use $E[(x_i - \mu)^{2}] = \sigma^{2}$ and
$\operatorname{Var}(\bar x) = \sigma^{2}/n$. Hence

$$E[s_n^{2}] = \frac{n-1}{n}\sigma^{2}. \qquad \blacksquare$$

**Where independence enters.** Only in $\operatorname{Var}(\bar x) = \sigma^{2}/n$,
which requires the cross-covariances to vanish. With correlated observations the
identity still holds but the second term becomes
$n\operatorname{Var}(\bar x) > \sigma^{2}$, so the expectation of $s_n^{2}$ is
*smaller* than $(n-1)\sigma^{2}/n$ — the sample variance understates the population
variance by an extra factor that grows with the correlation. This is the
variance-estimation counterpart of the standard-error inflation of
[01-13-03](../03-expectation-variance.md) Section 8.

---

## ★10 — Contaminated normal: mean against median

**(a)** For a mixture with weights $0.9$ and $0.1$ of variances $1$ and $100$:

$$\sigma^{2} = 0.9(1) + 0.1(100) = 0.9 + 10 = \boxed{10.9}.$$

**(b)** The variance of the sample mean for $n = 25$:

$$\operatorname{Var}(\bar X) = \frac{10.9}{25} = \boxed{0.436}.$$

**(c)** The asymptotic variance of the median needs the density at the centre:

$$f(0) = 0.9\,\phi(0) + 0.1\,\frac{\phi(0)}{10}
= 0.9(0.398942) + 0.1(0.039894) = 0.359048 + 0.003989 = 0.363037,$$

so

$$\operatorname{Var}(\tilde X) \approx \frac{1}{4n f(0)^{2}}
= \frac{1}{100 \times (0.363037)^{2}} = \frac{1}{13.180} = \boxed{0.075875}.$$

**(d)** The ratio is $0.436/0.075875 = \boxed{5.75}$: the mean's variance is more than
five times the median's.

**The mechanism.** The contaminated component contributes $10$ to the population
variance while contributing only $0.004$ to the density at the centre. The variance
is an integral against the *tail* of the distribution, so a rare component with a
large spread dominates it; the median's asymptotic variance depends on the density at
a *point*, so the same rare component barely moves it. Any estimator whose influence
function is unbounded — and the mean's is linear — inherits the tail's variability,
while an estimator with a bounded influence function, such as the median, does not.
This is the argument for robust estimation, and it is why a single gross error in a
small geophysical dataset can move a mean arbitrarily while leaving a median
essentially unchanged.

---

## ★11 — The uniform family and the midrange

**(a) Why Cramér–Rao does not apply.** The uniform density on $(0,\theta)$ is
$1/\theta$ on a support whose boundary depends on the parameter. The regularity
conditions for the Cramér–Rao bound require that the support not depend on $\theta$
and that differentiation under the integral sign be permitted. Neither holds: the
"score" $\partial_\theta \ln(1/\theta) = -1/\theta$ is not a function of the data at
all, and its mean square $1/\theta^{2}$ gives a spurious bound of $\theta^{2}/n$.

**Exact variance of the MLE.** The maximum $X_{(n)}$ has density
$f(x) = n x^{n-1}/\theta^{n}$ on $(0,\theta)$, so $E[X_{(n)}] = \theta n/(n+1)$ and
$E[X_{(n)}^{2}] = \theta^{2}n/(n+2)$. Hence

$$\operatorname{Var}(X_{(n)}) = \theta^{2}\left(\frac{n}{n+2} -
\frac{n^{2}}{(n+1)^{2}}\right)
= \theta^{2}\frac{n(n+1)^{2} - n^{2}(n+2)}{(n+2)(n+1)^{2}}
= \frac{\theta^{2}n}{(n+1)^{2}(n+2)}. \qquad \blacksquare$$

This is $O(\theta^{2}/n^{2})$, not $O(\theta^{2}/n)$: the error falls as $n^{-1}$ in
the *standard deviation* rather than $n^{-1/2}$, an order-of-magnitude better than any
regular estimator could achieve. The maximum of the sample converges to $\theta$
because it is bounded by it and gets close to it; the rate is faster because the
extreme order statistic carries direct information about the boundary rather than
diffuse information about the centre.

**(b) Why the midrange fails for heavy tails.** The midrange is built from the two
extreme order statistics. For a uniform parent those extremes are the most informative
observations about the range; for a heavy-tailed parent they are the *least*
informative about the centre and the most variable. The lesson's simulation measured
the consequence: for a Laplace parent with $n = 25$ the midrange had a mean squared
error of $0.828$ against $0.054$ for the median, a factor of fifteen.

The relevant concept is the **breakdown point**: the smallest fraction of
contaminated observations that can make the estimator arbitrarily wrong. The midrange
has breakdown point $1/n$ — a single arbitrarily large observation moves it without
bound — the mean has $0$, and the median has $0.5$. A related concept is the
**influence function**, the derivative of the estimator with respect to one
observation: bounded for the median, unbounded for the mean and the midrange.
Reporting a location estimate without saying how much contamination it tolerates is
reporting half an answer.
