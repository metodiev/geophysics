# Solutions — 01-13-07 Confidence Intervals and Their Correct Interpretation

> **Read this after attempting the exercises, not before.**
>
> Numbers were computed. Where a statement about interpretation is assessed, the
> correct coverage language is given in full, because the misstatement is the point
> of the exercise.

---

## ★1 — A $z$ interval

With $z_{0.975} = 1.959964$, $\sigma = 4$ and $n = 25$:

$$\text{half-width} = 1.959964 \times \frac{4}{\sqrt{25}} = 1.959964 \times 0.8
= 1.567971.$$

The interval is

$$\bar X \pm 1.567971 = \boxed{[10.432029,\ 13.567971]},$$

with a full width of $\boxed{3.135942}$.

**Coverage statement.** Before the data were seen, the probability was $0.95$ that the
procedure would produce an interval containing $\mu$. After the data are in, either
this particular interval contains $\mu$ or it does not.

---

## ★2 — Sample size for a target half-width

$$n = \left(\frac{z_{0.975}\,\sigma}{w}\right)^{2}
= \left(\frac{1.959964 \times 4}{0.5}\right)^{2} = (15.679713)^{2}
= 245.853,$$

so $\boxed{n = 246}$ (rounded up, since a fractional observation is not available and
rounding down would miss the target). The $3.14$-fold increase over $n = 25$ for a
three-fold reduction in width is the $\sqrt n$ law: width scales as $n^{-1/2}$.

---

## ★3 — A $t$ interval

Degrees of freedom: $\mathrm{df} = n - 1 = 9$. The critical value is

$$t_{0.975,\,9} = 2.262157,$$

and the half-width is

$$t \times \frac{s}{\sqrt n} = 2.262157 \times \frac{3}{\sqrt{10}}
= 2.262157 \times 0.948683 = 2.146071.$$

The interval is

$$\boxed{[17.853929,\ 22.146071]},$$

with a width of $4.292142$.

**Comparison with the known-$\sigma$ interval.** Using $z = 1.959964$ instead of
$t = 2.262157$ would give a width of $3.718094$, so the $t$ interval is
$15.4\%$ wider. The penalty for having to estimate $\sigma$ from nine observations is
real but modest, and it falls quickly: at $\mathrm{df} = 30$ the ratio is $1.042$, and
at $\mathrm{df} = 100$ it is $1.012$.

---

## ★4 — True or false

**(a) False.** This is the misinterpretation. The realised interval is fixed and $\mu$
is fixed, so the probability that $\mu$ lies inside it is either $0$ or $1$. The
$95\%$ refers to the procedure's behaviour before the data were seen. The sentence
becomes correct only in a Bayesian formulation, where it describes a credible interval
and requires a prior on $\mu$.

**(b) True.** This is the definition of coverage, and it is the only guarantee a
confidence interval provides.

**(c) True.** A $99\%$ interval uses $z_{0.995} = 2.575829$ against
$z_{0.975} = 1.959964$, so it is $31.4\%$ wider. Higher confidence costs precision;
the two cannot be varied independently without changing the data.

**(d) False.** An interval that excludes zero is evidence against the null value *for
the parameter being estimated under the assumed model*. It does not establish absence,
because the parameter being intervalled may not be the physical effect of interest —
a systematic offset moves the interval without moving the truth, as ★5 shows.

---

## ★5 — Coverage with a systematic offset

The half-width is

$$w = \frac{1.959964 \times 1}{\sqrt{25}} = 0.391993.$$

The sample mean is $\bar X \sim \mathcal{N}(0.3, 1/25)$, so with
$\text{se} = 1/5 = 0.2$ the coverage is

$$P\left(|\bar X| \le w\right) = \Phi\left(\frac{w - 0.3}{0.2}\right)
- \Phi\left(\frac{-w - 0.3}{0.2}\right) = \Phi(0.459965) - \Phi(-3.459965).$$

The second term is $2.7\times10^{-4}$, so

$$\text{coverage} = 0.677282 - 0.000270 = \boxed{0.677}.$$

**Direction of the failure, and its growth with $n$.** Coverage is below nominal
because the interval is centred on $0.3$ rather than on $0$. As $n$ grows, $w$ shrinks
as $n^{-1/2}$ while the offset stays at $0.3$, so the argument
$(w - 0.3)/\text{se}$ becomes increasingly negative and the coverage falls toward
zero. The lesson measured exactly this: $0.529$ at $n = 16$ down to zero at
$n = 256$.

**What the interval is doing.** It is a valid interval for the mean of the *measured*
distribution, which is $0.3$, not $0$. No statistical procedure applied to these data
can detect the difference, because the data contain no information about it. The
remedy is external: calibration against a known standard, an inter-survey tie, or a
measurement by an independent method.

---

## ★6 — Pareto with $\alpha = 2.5$ and the fourth moment

The variance exists, since $\alpha = 2.5 > 2$, so a sample standard deviation is a
legitimate estimator of a finite quantity and a $t$-style interval is not formally
undefined. However, the **fourth** moment does not exist (it requires
$\alpha > 4$), and the sampling variance of the sample variance depends on the fourth
moment. Consequently:

- The sample standard deviation converges very slowly and its distribution is strongly
  right-skewed, so a typical sample understates the population standard deviation (the
  lesson measured $78.5\%$ of samples of size $10\,000$ understating the true variance
  at $\alpha = 2.5$).
- The interval's *width* is therefore itself highly variable, and the nominal coverage
  is not achieved reliably even though the population variance exists.

**Recommendation.** Report an interval for the median or another quantile, obtained
from a quantile-based standard error, and state the sample size. If an interval for the
mean is required, use the bootstrap but check its coverage on synthetic data first, and
be explicit that the interval's width is sensitive to the largest few observations.

---

## ★7 — Two intervals, a difference, and the eye test

The intervals are $[9.0, 11.0]$ and $[11.0, 13.0]$: they **touch** at $11.0$ and
otherwise do not overlap.

Each $95\%$ interval has half-width $1.0$, so each standard error is
$1.0/1.959964 = 0.510213$. The standard error of the difference, for independent
experiments, is

$$\text{se}(B - A) = \sqrt{0.510213^{2} + 0.510213^{2}} = 0.721551,$$

and the $95\%$ interval for the difference is

$$(12.0 - 10.0) \pm 1.959964(0.721551) = 2.0 \pm 1.414214
= \boxed{[0.585786,\ 3.414214]}.$$

The interval excludes zero, so the difference of $2.0$ is significant at the $5\%$
level.

**The lesson.** Two intervals that overlap only at a single point perfectly illustrate
why the eye test fails: a reader comparing them would describe the result as marginal,
while the formal test of the difference is clear. The reverse error also occurs —
intervals can overlap substantially while the difference is significant, when the
correlation between the two estimates is negative. The rule is: **to test a difference,
compute the interval for the difference.**

---

## ★8 — Depth from velocity and travel time

$$d = \frac{vT}{2} = \frac{3000 \times 0.500}{2} = 750.0000\ \mathrm{m}.$$

Relative uncertainty by the product rule:

$$\frac{\sigma_d}{d} = \sqrt{\left(\frac{100}{3000}\right)^{2} +
\left(\frac{0.005}{0.500}\right)^{2}} = \sqrt{0.0011111 + 0.0001} = 0.034801.$$

Hence

$$\sigma_d = 750.0000 \times 0.034801 = 26.100766\ \mathrm{m},$$

and the approximate $95\%$ interval is

$$750.00 \pm 1.959964(26.100766) = 750.00 \pm 51.157 \quad
\boxed{[698.84,\ 801.16]\ \mathrm{m}}.$$

**Reading the budget.** The velocity term contributes $3.333\%$ and the timing term
$1.000\%$; removing the timing uncertainty entirely would leave $3.333\%$, reducing
$\sigma_d$ from $26.10$ m to $25.00$ m — a gain of $4.2\%$. Halving the velocity
uncertainty to $50$ m/s would give $14.58$ m, a gain of $44\%$. The budget, not the
interval, tells you where to spend the next measurement.

---

## ★9 — Coverage as a function of the offset

**(a)** With $\bar X \sim \mathcal{N}(\mu + \delta, \sigma^{2}/n)$ and half-width
$w = z_{1-\alpha/2}\sigma/\sqrt n$:

$$C(\delta) = P\left(\left|\bar X - \mu\right| \le w\right)
= \Phi\left(\frac{w - \delta}{\sigma/\sqrt n}\right)
- \Phi\left(\frac{-w - \delta}{\sigma/\sqrt n}\right).$$

**(b)** Write $s = \sigma/\sqrt n$ and $w = z s$. Then

$$C(\delta) = \Phi\left(z - \frac{\delta\sqrt n}{\sigma}\right)
- \Phi\left(-z - \frac{\delta\sqrt n}{\sigma}\right).$$

For fixed $\delta \ne 0$ the argument $z - \delta\sqrt n/\sigma \to -\infty$ and the
second argument also tends to $-\infty$; both terms tend to $0$, so
$C(\delta) \to 0$. $\blacksquare$

**(c)** Differentiate with respect to $\delta$, letting $\phi$ denote the standard
normal density:

$$C'(\delta) = -\frac{\sqrt n}{\sigma}\phi\left(z - \frac{\delta\sqrt n}{\sigma}\right)
+ \frac{\sqrt n}{\sigma}\phi\left(-z - \frac{\delta\sqrt n}{\sigma}\right).$$

For $\delta > 0$ the first density is evaluated nearer the centre than the second
(because $z - \delta\sqrt n/\sigma < -z - \delta\sqrt n/\sigma$ whenever
$z > 0$), so the first term dominates and $C'(\delta) < 0$. By symmetry $C$ is
increasing for $\delta < 0$. Hence $C$ is decreasing in $|\delta|$, and $C(0) =
1-\alpha$ is its maximum. $\blacksquare$

**(d)** More data cannot recover a systematic error, and it actively makes the coverage
worse: the interval narrows as $n^{-1/2}$ while $\delta$ is fixed, so the interval
converges on the wrong value and its coverage decays to zero. The only remedies are
external to the dataset — calibration, ties between surveys, or an independent
measurement — and the practical implication is that effort spent on more data is
wasted, or worse, until the systematic error has been bounded.

---

## ★10 — Replications for a coverage measurement

The estimated coverage is a proportion $\hat C$ from $N$ independent replications,
with standard error $\sqrt{C(1-C)/N}$. Setting this to $0.002$ and using
$C \approx 0.95$:

$$N = \frac{C(1-C)}{(0.002)^{2}} = \frac{0.95 \times 0.05}{4 \times 10^{-6}}
= \frac{0.0475}{4\times10^{-6}} = \boxed{11\,875}.$$

**Why the number depends on the coverage being measured.** The binomial variance
$C(1-C)$ is maximal at $C = 0.5$ and much smaller near $0$ or $1$. Using $C = 0.95$
gives $N = 11\,875$; using the worst case $C = 0.5$ would give $N = 62\,500$. So a
design aimed at measuring a coverage near $0.95$ can use fewer replications than one
aimed at a coverage that might be anywhere — but the design must state which regime it
assumed, and if the measured coverage turns out to be far from $0.95$ the standard
error must be recomputed from the observed value rather than from the design value.

---

## ★11 — A ratio, and why symmetry fails

**(a)** $R = 100/10 = 10$. By the delta method with independent numerator and
denominator,

$$\frac{\sigma_R}{R} \approx \sqrt{\left(\frac{\sigma_A}{A}\right)^{2}
+ \left(\frac{\sigma_B}{B}\right)^{2}}
= \sqrt{(0.02)^{2} + (0.2)^{2}} = \sqrt{0.0004 + 0.04} = 0.200998,$$

so

$$\sigma_R \approx 10 \times 0.200998 = 2.009975,$$

and the symmetric interval is

$$10 \pm 1.959964(2.009975) = 10 \pm \mathbf{3.9395}
= \boxed{[6.0609,\ 13.9391]}.$$

**(b)** $1/B$ is convex, so the distribution of $R$ is right-skewed: the upper tail is
stretched and the lower tail compressed relative to a Gaussian. A symmetric interval
built from a single standard deviation therefore places too little probability above
the point estimate and too much below it, and its true coverage is not $95\%$. The
severity grows with the relative uncertainty of the denominator — here $20\%$, which
is enough to matter, and much more than enough once $\sigma_B/B$ exceeds about a third.

**(c)** Construct the interval from the **quantiles of the ratio's sampling
distribution**, obtained either by Monte Carlo propagation through $\hat A$ and
$\hat B$ or by Fieller's method. Simulating $400\,000$ pairs with
$\hat A \sim \mathcal{N}(100, 2^{2})$ and $\hat B \sim \mathcal{N}(10, 2^{2})$ and
taking the quantiles of $A/B$ gives

| Quantity | Value |
|---|---|
| $2.5$th percentile | $7.168$ |
| median | $10.005$ |
| $97.5$th percentile | $16.449$ |
| mean | $10.461$ |

So the correct interval is approximately $[7.17, 16.45]$, against the symmetric
$[6.06, 13.94]$. The upper limit is understated by $2.5$ units — an error of $18\%$ —
and the interval is visibly asymmetric about the median, with the upper arm three
times the length of the lower.

**A diagnostic.** Compare the mean and the median of the simulated ratio: here
$10.461$ against $10.005$, a separation of about $0.23$ standard errors of the median,
which flags the skewness directly. A second diagnostic is to compare the two arms of
the interval, $q_{0.975} - q_{0.5} = 6.44$ against $q_{0.5} - q_{0.025} = 2.84$; a
ratio of more than about $1.2$ says the symmetric interval is not appropriate.
