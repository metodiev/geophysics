# Solutions — 01-13-02 Random Variables, PMFs, PDFs and CDFs

> **Read this after attempting the exercises, not before.**
>
> Numeric answers were computed, not estimated. Where a probability is given to six
> decimal places, the rounding is stated. Every continuous answer says whether the
> quantity is a probability or a density, because that distinction is the point of
> several of these problems.

---

## ★1 — Poisson PMF

**(a)** With $\lambda = 2.5$,

$$p(k) = \frac{2.5^{k}e^{-2.5}}{k!}.$$

| $k$ | $p(k)$ |
|---|---|
| 0 | 0.082085 |
| 1 | 0.205212 |
| 2 | 0.256516 |
| 3 | 0.213763 |

**(b)** Consistency checks. The probabilities decrease past the mode at $k = 2 =
\lfloor \lambda \rfloor$, and they sum to $1$ over all $k$; more usefully, compute
the mean and second moment from the four listed terms plus the tail:

$$\sum_k k\,p(k) = 2.500000, \qquad \sum_k k^{2}p(k) - \left(\sum_k k\,p(k)\right)^{2}
= 2.500000,$$

both equal to $\lambda$. For the Poisson family the mean and the variance are the
same number, and finding them equal is a check that the PMF has been written with
the right normalisation and the right parameter. A practical consequence: count data
whose sample variance substantially exceeds the sample mean are **not** Poisson, and
the ratio is a standard over-dispersion diagnostic.

---

## ★2 — Exponential waiting time

**(a)** The density is

$$f(x) = 2e^{-2x}, \qquad x \ge 0, \quad [f] = \mathrm{yr^{-1}},$$

a **density**, not a probability. At $x = 0.5$ yr,

$$f(0.5) = 2e^{-1} = 0.735759\ \mathrm{yr^{-1}}.$$

The value exceeds $1$; that is permitted, because it is probability per unit time.
The probability of an interval of width $0.01$ yr around $0.5$ yr is approximately
$0.00736$.

**(b)**

$$P(X < 0.5) = 1 - e^{-1} = 0.632121, \qquad P(X > 1) = e^{-2} = 0.135335.$$

**(c)** The median solves $1 - e^{-2m} = 1/2$, so $e^{-2m} = 1/2$ and

$$m = \frac{\ln 2}{2} = 0.346574\ \mathrm{yr}.$$

The median is smaller than the mean $1/\lambda = 0.5$ yr, as it must be for a
right-skewed distribution. Note also how much easier the median is to compute than
the mean: no integration is required, only the survival function.

---

## ★3 — Using the CDF

$$P(1 < X < 4) = F(4) - F(1) = e^{-1/3} - e^{-4/3}
= 0.716531 - 0.263597 = \boxed{0.452934}.$$

For the conditional probability, use the definition and the memorylessness that this
family possesses:

$$P(X > 6 \mid X > 3) = \frac{P(X > 6)}{P(X > 3)}
= \frac{e^{-2}}{e^{-1}} = e^{-1} = \boxed{0.367879}.$$

The answer equals $P(X > 3)$, which is the memoryless property: the process does not
remember the first three units of time. Compare with the Weibull of ★8, where the
corresponding answer is larger, because the hazard there is increasing.

---

## ★4 — Discrete CDF and quantiles

| $x$ | $p(x)$ | $F(x)$ |
|---|---|---|
| 1 | 0.2 | 0.2 |
| 2 | 0.5 | 0.7 |
| 3 | 0.3 | 1.0 |

The smallest $x$ with $F(x) \ge 0.7$ is $\boxed{x = 2}$, since $F(2) = 0.7$ exactly.

**Two remarks.** First, the quantile function of a discrete variable is not the
inverse of the CDF in the strict sense; the general definition is
$Q(u) = \min\{x : F(x) \ge u\}$, which is what was used here. Second, the boundary
case $u = 0.7$ matters: the convention above returns $2$, and the opposite convention
("strictly greater") would return $3$. Both conventions appear in software, and a
simulation that uses the quantile function must use the same convention as the
validation test.

---

## ★5 — A quadratic transformation

**(a)** With $X \sim \text{Uniform}(0,2)$ the density is $f_X(x) = 1/2$ on $(0,2)$.
The map $g(x) = x^{2}$ is strictly increasing on the support, so $g^{-1}(y) =
\sqrt y$ and

$$\frac{d g^{-1}}{dy} = \frac{1}{2\sqrt y}.$$

Hence

$$f_Y(y) = f_X(\sqrt y)\left|\frac{d g^{-1}}{dy}\right|
= \frac{1}{2}\cdot\frac{1}{2\sqrt y} = \frac{1}{4\sqrt y},
\qquad 0 < y < 4.$$

The units are $[\text{unit of } X]^{-2}$, as they must be, since $Y$ is a squared
quantity.

**(b)** Verify normalisation:

$$\int_0^{4}\frac{1}{4\sqrt y}\,dy = \frac{1}{2}\left[\sqrt y\right]_0^{4}
= \frac{1}{2}(2 - 0) = 1. \quad \checkmark$$

**(c)** From the density,

$$P(Y > 1) = \int_1^{4}\frac{1}{4\sqrt y}\,dy
= \frac{1}{2}\left[2 - 1\right] = \frac{1}{2}.$$

Directly from $X$: $Y > 1 \iff X > 1$, and $P(X > 1) = 1 - F_X(1) = 1 - 1/2 = 1/2$.
The two agree, as they must.

**What the exercise teaches.** The transform $Y = X^{2}$ concentrates probability at
small $y$: the density $1/(4\sqrt y)$ diverges as $y \to 0^{+}$, even though $X$ had
a perfectly flat density. A nonlinear transformation can create a singularity, and
it does so at the point where the inverse map's derivative blows up (here
$dx/dy \to \infty$ as $y \to 0$). This is the mechanism by which transformations of
ordinary variables produce heavy-tailed and singular densities, and it is the reason
the jacobian factor is not optional.

---

## ★6 — Magnitude to energy with $\lambda = 2.0$

**(a)** With $f_M(m) = \lambda e^{-\lambda m}$ and $Y = 10^{1.5M}$, the inverse is
$m = \log_{10}(y)/1.5$ and $dm/dy = 1/(1.5\ln 10 \cdot y)$. Therefore

$$f_Y(y) = \frac{\lambda}{1.5\ln 10}\,y^{-\alpha-1}, \qquad
\alpha = \frac{\lambda}{1.5\ln 10}
= \frac{2.0}{1.5 \times 2.302585} = \frac{2.0}{3.453877} = \boxed{0.579059}.$$

**(b)** Median. The median magnitude is $\ln 2/\lambda = 0.346574$; since $10^{1.5m}$
is increasing, the median of $Y$ is the transform of the median of $M$:

$$Y_{\text{med}} = 10^{1.5 \times 0.693147/2} = 10^{0.519860} = \boxed{3.310247}.$$

**(c)** $E[Y]$ exists only if $\alpha > 1$. Here $\alpha = 0.579059 < 1$, so **the
mean does not exist** for this choice of parameters. The reason is structural, not
numerical: the tail probability decays as $y^{-0.58}$, slower than $y^{-1}$, so
$\int y\,f_Y(y)\,dy$ diverges. Raising $\lambda$ until $\alpha > 1$, that is
$\lambda > 1.5\ln 10 = 3.453877$, would make the mean finite.

**(d)**

$$P(Y > 100) = 100^{-\alpha} = 10^{-2 \times 0.579059} = 10^{-1.158118} =
\boxed{0.069483}.$$

**The lesson.** The median (3.31) is a perfectly well defined and easily computed
number while the mean does not exist. That is not a paradox: the median is defined by
an inversion $\{F(x) = 1/2\}$, which requires nothing of any moment, while the mean
is an integral against the tail. Reporting a "typical" energy for such a distribution
by averaging samples will produce a number that grows without bound as the sample
grows, exactly as measured in the lesson.

---

## ★7 — A valid CDF and its quantile function

**(a)** Three checks:

- $F$ is non-decreasing: $F'(x) = 1/(1+x)^{2} > 0$.
- $F(0) = 0$ and $\lim_{x\to\infty} x/(1+x) = 1$, so the limits are correct.
- $F$ is right-continuous, being a ratio of continuous functions with a denominator
  bounded away from zero on the support.

Hence $F$ is a valid CDF.

**(b)** Solve $F(x) = u$: $x = u(1+x)$, so $x(1-u) = u$ and

$$F^{-1}(u) = \frac{u}{1-u}, \qquad 0 \le u < 1.$$

**(c)** Draw $10^{6}$ independent uniform values $u_i$ on $[0,1)$ and return
$x_i = u_i/(1-u_i)$ for each. This is the **inverse-transform** method: by the
probability integral transform, $F^{-1}(U)$ has CDF $F$.

**(d)** At $u = 1/2$, $x = (1/2)/(1/2) = \boxed{1}$.

**A practical warning.** The distribution is heavy-tailed: $F^{-1}(u) \sim 1/(1-u)$
as $u \to 1$, so the tail decays like $x^{-1}$, and the mean $\int x f(x)\,dx$ with
$f(x) = 1/(1+x)^{2}$ is divergent. Simulating it is straightforward, and summarising
it by a mean is not. Also note that the largest sampled value from $10^{6}$ draws will
be of order $10^{6}$, because the tail is that heavy — a useful reminder of why
empirical means for such distributions are dominated by the largest few samples.

---

## ★8 — Weibull hazard

**(a)** With $F(x) = 1 - e^{-(x/\lambda)^{k}}$, the survival function is
$S(x) = e^{-(x/\lambda)^{k}}$ and the density is
$f(x) = (k/\lambda)(x/\lambda)^{k-1}S(x)$. Hence

$$h(x) = \frac{f(x)}{S(x)} = \frac{k}{\lambda}\left(\frac{x}{\lambda}\right)^{k-1}
= \frac{2}{10}\left(\frac{x}{10}\right) = 0.02x.$$

**(b)** Increasing, since $dh/dx = 0.02 > 0$. Physically, the hazard grows with
elapsed time: a component or a fault that has survived longer is *more* likely to
fail in the next instant, which is the signature of accumulating damage. This is the
opposite of the exponential, and it is why a Weibull model with $k > 1$ is used for
wear-out, for the size-dependence of fracture spacing, and for quantities whose
failure is triggered by a threshold on a growing quantity.

**(c)**

$$P(X > 12 \mid X > 10) = \frac{S(12)}{S(10)}
= \frac{e^{-(1.2)^{2}}}{e^{-(1.0)^{2}}} = e^{-1.44 + 1.00} = e^{-0.44} =
\boxed{0.644036}.$$

The memoryless value, from an exponential with the same scale $\lambda = 10$, would
be $P(X > 12 \mid X > 10) = e^{-2/10} = e^{-0.2} = 0.818731$. Here the conditional
probability is *lower* than the memoryless value, because the hazard rises
with age, so surviving to ten years leaves you closer to failure, not further from it.
This contrast is the practical content of the hazard-rate concept.

---

## ★9 — Lognormal moments

**(a)** Since $\ln X = Z \sim \mathcal{N}(\mu, \sigma^{2})$ and $X = e^{Z}$:

- **Median.** The exponential is increasing, so the median of $X$ is the exponential
  of the median of $Z$: $e^{\mu}$.
- **Mean.** Using the moment generating function of the normal,
  $E[e^{tZ}] = e^{t\mu + t^{2}\sigma^{2}/2}$, evaluated at $t = 1$:

  $$E[X] = e^{\mu + \sigma^{2}/2}.$$

- **Mode.** Differentiate the density
  $f(x) = \frac{1}{x\sigma\sqrt{2\pi}}\exp\left(-\frac{(\ln x - \mu)^{2}}{2\sigma^{2}}\right)$
  and set the derivative to zero. Writing $L = \ln x$,

  $$\frac{d}{dx}\ln f = -\frac{1}{x} - \frac{L - \mu}{x\sigma^{2}} = 0
  \ \Longrightarrow\ \sigma^{2} + L - \mu = 0
  \ \Longrightarrow\ L = \mu - \sigma^{2},$$

  so the mode is $e^{\mu - \sigma^{2}}$.

**(b)** Since $\sigma^{2} > 0$, $\mu - \sigma^{2} < \mu < \mu + \sigma^{2}/2$, and
$e^{\cdot}$ is increasing, so mode $<$ median $<$ mean. The gap between the median
and the mean grows with $\sigma^{2}$.

**(c)**

$$P(X < E[X]) = P\left(e^{Z} < e^{\mu + \sigma^{2}/2}\right)
= P\left(Z < \mu + \frac{\sigma^{2}}{2}\right)
= \Phi\left(\frac{\sigma}{2}\right).$$

For $\sigma = 1$ this is $\Phi(0.5) = 0.691462$, so the fraction **above** the mean
is $1 - 0.691462 = 0.308538$. The lesson's simulation reported $0.307670$ from
$300\,000$ draws; the difference of $0.00087$ is about $1.8$ standard errors for a
proportion near $0.31$ with that sample size, so the simulation and the exact value
agree.

**Two further values, for calibration:** $\Phi(0.25) = 0.598706$ at $\sigma = 0.5$,
and $\Phi(1) = 0.841345$ at $\sigma = 2$. The fraction of the distribution below the
mean rises from $60\%$ to $84\%$ as $\sigma$ doubles, which is a vivid statement of
how unrepresentative the arithmetic mean becomes for a lognormal quantity with large
spread.

---

## ★10 — General magnitude-to-energy transformation

**(a)** With $Y = 10^{aM}$, the inverse is $M = \ln Y/(a\ln 10)$ and

$$\frac{dM}{dY} = \frac{1}{a\ln 10 \cdot Y}.$$

Therefore

$$f_Y(y) = \lambda e^{-\lambda M}\frac{1}{a\ln 10 \cdot y}
= \frac{\lambda}{a\ln 10}\,y^{-\alpha - 1}, \qquad
\alpha = \frac{\lambda}{a\ln 10}, \quad y \ge 1,$$

which is a Pareto density with lower limit $1$ and tail exponent $\alpha$.
$\blacksquare$

**(b)** For any $\alpha > 0$,

$$\int_1^{\infty} y^{-\alpha-1}\,dy = \left[-\frac{y^{-\alpha}}{\alpha}
\right]_1^{\infty} = \frac{1}{\alpha},$$

so

$$\int_1^\infty f_Y(y)\,dy = \frac{\lambda}{a\ln 10}\cdot\frac{1}{\alpha}
= \alpha \cdot \frac{1}{\alpha} = 1. \quad \checkmark$$

Normalisation holds for every positive $\alpha$, with no condition on $\lambda$.

**(c)** The mean is

$$E[Y] = \int_1^\infty y\,f_Y(y)\,dy = \alpha\int_1^\infty y^{-\alpha}\,dy
= \frac{\alpha}{\alpha - 1},$$

finite if and only if $\alpha > 1$, that is if and only if

$$\lambda > a\ln 10.$$

For the lesson's parameterisation $\lambda = b\ln 10$, this becomes $b > a$. With
$a = 1.5$ and $b = 1$ we have $\alpha = 1/1.5 = 0.6667 < 1$, so the mean diverges,
which is the statement made in the lesson.

**(d)** Normalisation is a statement about the *area* under the density, which is an
integral of $y^{-\alpha-1}$. The mean is a statement about the *first moment*, which
is an integral of $y^{-\alpha}$. The first converges for every $\alpha > 0$; the
second needs $\alpha > 1$. So a density can be perfectly proper — integrating to
exactly one, sampling from it straightforward — while its mean, its variance, or any
higher moment fails to exist. This is why "the distribution is well defined" and "the
mean is well defined" are different sentences, and why quantile-based summaries are
the safe default for heavy-tailed quantities.
