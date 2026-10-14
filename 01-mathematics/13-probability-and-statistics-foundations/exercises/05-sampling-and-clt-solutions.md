# Solutions — 01-13-05 Sampling Distributions, Law of Large Numbers and CLT

> **Read this after attempting the exercises, not before.**
>
> Numbers were computed. For every limit-theorem invocation the hypothesis being
> used is named, because the whole lesson is about the difference between the
> theorem and its hypotheses.

---

## ★1 — Chebyshev against the Gaussian value

**(a)** $\operatorname{Var}(\bar X) = \sigma^{2}/n = 4/100 = 0.04$. Chebyshev gives

$$P\left(\left|\bar X - \mu\right| \ge \varepsilon\right)
\le \frac{\sigma^{2}}{n\varepsilon^{2}} = \frac{4}{100 \times 0.25} =
\boxed{0.16}.$$

**(b)** If the observations are Gaussian then $\bar X$ is exactly Gaussian with
standard error $0.2$, so

$$P\left(\left|\bar X - \mu\right| > 0.5\right) = 2\left[1 - \Phi(2.5)\right]
= 2(1 - 0.993790) = \boxed{0.012419}.$$

**The ratio** is $0.16/0.012419 = 12.9$. The bound is nearly thirteen times the true
value, and that is expected: Chebyshev is distribution-free and must therefore cover
the worst case, which is attained by a two-point distribution placing mass at the
extremes. The bound's value is that it establishes convergence with no assumption
beyond finite variance; its cost is that it is useless for numeric error bars.

---

## ★2 — Standard errors

$$\operatorname{se}(\bar X) = \frac{3}{\sqrt{36}} = \boxed{0.5}.$$

For a target standard error of $0.1$,

$$\frac{3}{\sqrt n} = 0.1 \ \Longrightarrow\ \sqrt n = 30
\ \Longrightarrow\ n = \boxed{900}.$$

**The pattern worth internalising.** Going from a standard error of $0.5$ to $0.1$ is
a factor of five in precision and a factor of $25$ in sample size. Uncertainty
budgets in geophysics are dominated by this quadratic cost, which is why the cheapest
way to improve a survey is usually to reduce the single-measurement standard deviation
rather than to add stations.

---

## ★3 — Standardising

$$z = \frac{\bar X - \mu_0}{\sigma/\sqrt n} = \frac{52 - 50}{6/3} =
\frac{2}{2} = \boxed{1.0}.$$

A $z$ of $1.0$ corresponds to a two-sided p-value of $0.3173$: the observation is
entirely compatible with the null hypothesis. Note how the sample size enters: with
the same sample mean and a sample of $n = 900$ instead of $9$ the standard error
would be $0.2$ and $z$ would be $10$, and the same difference of two units would be
overwhelming. **A mean difference means nothing without the sample size.**

---

## ★4 — Which laws apply

| Parent | LLN | Classical CLT |
|---|---|---|
| (a) $\text{Uniform}(0,1)$ | yes (finite mean, and finite variance) | yes |
| (b) $\text{Exp}(1)$ | yes | yes (variance $= 1$) |
| (c) Pareto $\alpha = 1.5$ | yes ($\alpha > 1$ so the mean exists) | **no** (variance infinite) |
| (d) Pareto $\alpha = 2.5$ | yes | yes (variance $\alpha x_{\min}^{2}/((\alpha-1)^{2}(\alpha-2))$ is finite) |
| (e) standard Cauchy | **no** (no mean) | no |

**The point of the table.** (c) is the case that catches people out: the law of large
numbers holds, so the sample mean converges and its running value looks stable over
short stretches, yet the CLT fails and no Gaussian error bar is available. The
distinction is between the first moment, needed for convergence, and the second,
needed for a Gaussian limit and for a finite standard error.

---

## ★5 — The Berry–Esseen bound in practice

The bound is

$$\sup_z\left|P(Z_n \le z) - \Phi(z)\right| \le
\frac{C\,E|X-\mu|^{3}}{\sigma^{3}\sqrt n}
= \frac{0.4748 \times 2.414553}{\sqrt n} = \frac{1.146430}{\sqrt n}.$$

At $n = 100$: $\boxed{0.114643}$. At $n = 300$: $\boxed{0.066189}$.

The measured value at $n = 300$ was $0.013241$, so the bound is about five times the
observed discrepancy. This is typical: the sharp Berry–Esseen constant is a
worst-case constant over all distributions with a given third absolute moment, and
the true discrepancy depends on the whole shape of the parent, including the
symmetry of the correction terms. The bound's use is to tell you the *rate*
($n^{-1/2}$) and the *scaling variable* ($E|X-\mu|^{3}/\sigma^{3}$, i.e. skewness),
not to provide a numeric error bar.

**Practical consequence.** Do not use the Berry–Esseen bound to justify "n is large
enough". Use it to know that the error falls as $n^{-1/2}$ and is proportional to a
standardised third moment, then verify normality empirically — with a quantile plot
of the standardised means, as the demonstration does.

---

## ★6 — Monte Carlo draws for a probability

For an estimated proportion $\hat p$ from $N$ independent Bernoulli draws, the
standard error is $\sqrt{p(1-p)/N}$. Setting this equal to $0.001$ with $p = 0.1$:

$$N = \frac{p(1-p)}{(0.001)^{2}} = \frac{0.09}{10^{-6}} = \boxed{90\,000}.$$

**Remarks.** (i) The formula uses the worst-case $p = 0.5$ only when the probability
is unknown; here $p \approx 0.1$ is known, and using $0.5$ would have given
$250\,000$ draws and wasted most of them. (ii) If the target precision were relative,
$\pm 1\%$ rather than $\pm 0.001$ absolute, the required $N$ would be
$(1-p)/(p r^{2}) = 0.9/(0.1 \times 10^{-4}) = 90\,000$ as well — a coincidence of the
numbers chosen. (iii) The rule assumes a fixed $N$ decided in advance; stopping when
the estimate looks precise enough is a form of the optional-stopping problem of
[01-13-08](../08-hypothesis-testing.md) Section 6.

---

## ★7 — Sample size for $\alpha = 2.5$

The fluctuation of the mean scales as

$$\sigma_{\bar X} \propto n^{-(1-1/\alpha)} = n^{-(1 - 0.4)} = n^{-0.6}.$$

To halve $\sigma_{\bar X}$ requires

$$\left(\frac{n_2}{n_1}\right)^{0.6} = 2 \ \Longrightarrow\
\frac{n_2}{n_1} = 2^{1/0.6} = 2^{1.666667} = \boxed{3.1748}.$$

So a $3.17$-fold increase in sample size halves the precision of the mean, against
the fourfold increase required when the variance is finite.

**A caveat about the exponent.** For $1 < \alpha < 2$ this is the leading
asymptotic scaling. The convergence to it is slow, because the terms that dominate
are rare events, and the effective exponent measured over a finite range of $n$ can
differ from the asymptotic value — the lesson measured $0.3161$ where the asymptotic
value is $0.3333$, on a range from $n = 100$ to $n = 10\,000$.

---

## ★8 — The same question for $\alpha = 1.5$

$$\sigma_{\bar X} \propto n^{-(1-1/1.5)} = n^{-1/3},$$

so

$$\left(\frac{n_2}{n_1}\right)^{1/3} = 2 \ \Longrightarrow\
\frac{n_2}{n_1} = 2^{3} = \boxed{8}.$$

Comparing the two: $\boxed{3.17}$ for $\alpha = 2.5$ against $\boxed{8}$ for
$\alpha = 1.5$. A smaller tail exponent means a heavier tail, therefore a more
variable largest observation, therefore a sample mean whose value is set by that
observation rather than by the bulk; and because the largest of $n$ draws grows only
slowly, more data are needed before the mean settles.

---

## ★9 — Proof of the weak law under finite variance

**Chebyshev's inequality.** For any random variable $Y$ with finite mean and variance
and any $\varepsilon > 0$,

$$P\left(\left|Y - E[Y]\right| \ge \varepsilon\right) \le
\frac{\operatorname{Var}(Y)}{\varepsilon^{2}}.$$

*Proof.* On the event $\{|Y - E[Y]| \ge \varepsilon\}$ we have $(Y -
E[Y])^{2}/\varepsilon^{2} \ge 1$, so

$$\operatorname{Var}(Y) = E\left[(Y-E[Y])^{2}\right] \ge
\varepsilon^{2}P\left(\left|Y - E[Y]\right| \ge \varepsilon\right),
\qquad \blacksquare$$

**Application.** Let $X_1, X_2, \dots$ be i.i.d. with $E[X_i] = \mu$ and
$\operatorname{Var}(X_i) = \sigma^{2} < \infty$. Independence gives
$\operatorname{Var}(\bar X_n) = \sigma^{2}/n$ and linearity gives
$E[\bar X_n] = \mu$. Applying Chebyshev to $Y = \bar X_n$:

$$P\left(\left|\bar X_n - \mu\right| \ge \varepsilon\right)
\le \frac{\sigma^{2}}{n\varepsilon^{2}} \xrightarrow[n\to\infty]{} 0
\quad \text{for every } \varepsilon > 0. \qquad \blacksquare$$

**The hypotheses used, in order.** Finite first moment to define $\mu$; finite second
moments and independence to compute $\operatorname{Var}(\bar X_n) = \sigma^{2}/n$;
and finite variance again (through Chebyshev) to convert the variance bound into a
concentration statement. Drop the finite variance and the proof collapses — which is
not merely a limitation of the proof, since for $\alpha \le 1$ the conclusion itself
is false.

---

## ★10 — Why the scaling is $n^{-(1-1/\alpha)}$

**The argument.** Let $X_1, \dots, X_n$ be i.i.d. Pareto$(\alpha)$ with
$1 < \alpha < 2$, so $E[X]$ is finite but $E[X^{2}]$ is not. The largest observation
satisfies $X_{(n)} \approx n^{1/\alpha}$ in the following sense: the probability that
a given observation exceeds $x$ is $x^{-\alpha}$, so the number of observations
exceeding $x$ has mean $n x^{-\alpha}$, which is of order one when
$x \approx n^{1/\alpha}$. Depending on the realisation, the largest value is
sometimes a little above and sometimes below that scale, so $X_{(n)} =
n^{1/\alpha} \cdot O_p(1)$.

Now consider the sample mean. Its fluctuation about $\mu$ is dominated by the largest
few terms, because the bulk contributes $O(n^{-1/2})$ in units of $\sigma$ but the
second moment does not exist, so the bulk's contribution cannot be bounded by a
finite variance. Approximating the mean by its largest term,

$$\bar X_n - \mu \approx \frac{X_{(n)}}{n} = O_p\left(\frac{n^{1/\alpha}}{n}\right)
= O_p\left(n^{-(1 - 1/\alpha)}\right).$$

Since $1 - 1/\alpha < 1/2$ for $\alpha < 2$, this fluctuation is *larger* than
$n^{-1/2}$ and decays more slowly. $\blacksquare$

**Checks on the argument.** As $\alpha \to 2^{-}$ the exponent
$1 - 1/\alpha \to 1/2$, recovering the finite-variance rate in the limit. As
$\alpha \to 1^{+}$ the exponent tends to $0$: at the boundary where the mean is about
to become infinite, the sample mean barely converges at all. Both limits are correct,
which is the main evidence that the scaling argument has the right form.

---

## ★11 — A Monte Carlo precision statement with $\alpha = 1.7$

**(a) Why $s/\sqrt N$ may not apply.** The rule estimates the standard error of the
ensemble mean as the sample standard deviation divided by $\sqrt N$, and its validity
rests on the CLT, which requires a finite variance. With $\alpha = 1.7$ the variance
does not exist, so the sample standard deviation does not converge, the ensemble mean
does not converge normally, and the reported precision would improve roughly as
$N^{-(1-1/1.7)} = N^{-0.412}$ rather than $N^{-0.5}$ — and erratically even then.

**(b) A diagnostic.** Re-run the ensemble with increasing $N$ and record the running
estimates of the mean and of the standard deviation. If the mean is stable to the
quoted precision but the standard deviation keeps climbing, a missing second moment is
the cause. A complementary diagnostic is to plot the empirical survival function of
the simulated output on log–log axes: a straight line over a substantial range is the
signature of a power-law tail, and its slope estimates $\alpha$. A third is to
compare the ensemble quantiles at two different $N$: quantiles stabilise even when
moments do not, so agreement in the quantiles with disagreement in the mean is
diagnostic.

**(c) What to report instead.** Report the median and a quantile range (for example
the $2.5$th and $97.5$th percentiles), together with the number of draws and a
statement of their Monte Carlo uncertainty computed from the quantiles' own standard
errors, $\sqrt{p(1-p)/N}/f(q_p)$. Report the estimated tail exponent and the range of
values over which the power-law form is supported. State explicitly that the mean and
standard deviation are not reported because the corresponding moments do not exist,
and if a mean-like summary is required, report the mean of the *truncated*
distribution with the truncation level stated.
