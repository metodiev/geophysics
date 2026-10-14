# Solutions — 01-13-04 Common Distributions and Their Earth-Science Roles

> **Read this after attempting the exercises, not before.**
>
> Every number was computed. Where a distribution is named, the mechanism is named
> as well, because the mechanism is what makes the choice defensible rather than
> convenient.

---

## ★1 — Matching distributions to mechanisms

| | Family | Mechanism |
|---|---|---|
| (a) | **Gaussian** | additive: many small independent error contributions sum, and the CLT makes the sum normal |
| (b) | **exponential** (gaps) and **Poisson** (counts) | constant hazard: the probability of an event in the next instant does not depend on elapsed time |
| (c) | **lognormal** | multiplicative: a product of positive factors is lognormal because the sum of their logs is normal |
| (d) | **power law / Pareto** | scale-invariant fragmentation: breaking a fragment produces pieces drawn from the same size process |
| (e) | **Gumbel** (or the wider generalised extreme value family) | extreme of a large sample from a light-tailed parent |

**A caution on (e).** The Gumbel is the appropriate limit for a parent with
exponentially decaying tails. A parent with a power-law tail gives a Fréchet-type
limit and a parent with bounded support gives a Weibull-type limit; all three are
members of the generalised extreme value family, distinguished by a shape
parameter. Choosing the Gumbel without checking the parent's tail is a decision, not
a default.

---

## ★2 — Poisson counts

With $\lambda = 4$ per year,

$$P(N = 0) = e^{-4} = \boxed{0.018316},$$

$$P(N \ge 1) = 1 - e^{-4} = \boxed{0.981684},$$

$$P(N = 3) = \frac{4^{3}e^{-4}}{3!} = \frac{64 \times 0.0183156}{6}
= \boxed{0.195367}.$$

**Checks.** The three answers are consistent with the PMF: $p(0) + p(1) + p(2) +
p(3)$ plus the tail accounts for the whole unit mass, and the value $3$ is below the
mode at $\lfloor 4 \rfloor = 4$, so it should be just short of the maximum mass —
which it is, since $p(4) = 0.195367 \times 4/4 = 0.195367$ as well, an exact tie for
integer $\lambda$.

**A practical warning.** The Poisson assumption of a constant rate fails whenever
events cluster. For a real catalogue the variance of the annual count exceeds the
mean, and the difference is a usable diagnostic: fit the mean, compare with the
variance, and if the ratio is substantially above one, do not report a Poisson
uncertainty.

---

## ★3 — Waiting times

A mean waiting time of $0.25$ yr implies a rate

$$\lambda = \frac{1}{0.25} = 4\ \mathrm{yr^{-1}}.$$

The gap is exponential, so

$$P(\text{gap} > 1) = e^{-\lambda \times 1} = e^{-4} = \boxed{0.018316}.$$

The number coincides with the probability of zero events in a year from ★2, and it
should: "no event in the next year" and "the next gap exceeds one year" are the same
event for a Poisson process. Recognising such coincidences is a good check that the
two views of the process have been connected correctly.

---

## ★4 — Lognormal summary

With $\mu = 0$, $\sigma = 1$:

$$\text{median} = e^{\mu} = e^{0} = \boxed{1}, \qquad
\text{mean} = e^{\mu + \sigma^{2}/2} = e^{0.5} = \boxed{1.648721}, \qquad
\text{mode} = e^{\mu - \sigma^{2}} = e^{-1} = \boxed{0.367879}.$$

The ordering mode $<$ median $<$ mean is the signature of a lognormal.

The fraction above the mean is

$$P(X > E[X]) = 1 - \Phi\left(\frac{\sigma}{2}\right) = 1 - \Phi(0.5)
= 1 - 0.691462 = \boxed{0.308538}.$$

So fewer than one third of the samples exceed the arithmetic mean, and the mean sits
between the $69$th and the $70$th percentile of the distribution. **This is the
single most important practical fact about lognormal quantities**: reporting the
mean as a "typical" value describes a region that the majority of the data never
reaches.

---

## ★5 — Hill estimator

The Hill estimator for the $k$ largest values with threshold $X_{(n-k)}$ is

$$\hat\alpha = \left[\frac{1}{k}\sum_{i=1}^{k}
\ln\frac{X_{(n-k+i)}}{X_{(n-k)}}\right]^{-1}.$$

With threshold $20$ and the values $100, 50, 40, 30, 20$, the ratios are
$5, 2.5, 2, 1.5, 1$ and their logarithms are $1.609438$, $0.916291$, $0.693147$,
$0.405465$, $0.000000$. The mean logarithm is

$$\frac{1.609438 + 0.916291 + 0.693147 + 0.405465 + 0}{5} = \frac{3.624341}{5}
= 0.724868,$$

so

$$\hat\alpha = \frac{1}{0.724868} = \boxed{1.3796}.$$

**Why this is only an estimate.** Five order statistics is a very small window, and
the estimator is sensitive to it: using only the top three values would give
$\hat\alpha = 3/(1.609438 + 0.916291 + 0.693147) = 3/3.218876 = 0.932$ — a change of
$32\%$ from the five-value answer. In practice $\hat\alpha$ is plotted against the
window size $k$ on a log axis, and the estimate is taken from the region where the
plot is flat. Reporting a single number without that plot hides the dependence that
governs its reliability.

---

## ★6 — The maximum of $100$ exponentials

**(a) Exact.**

$$P(M_{100} \le 5) = \left[P(X \le 5)\right]^{100}
= \left(1 - e^{-5}\right)^{100} = (0.993262)^{100} = \boxed{0.508609}.$$

**(b) Gumbel approximation.** With $n = 100$, $\ln n = 4.605170$ and
$y = 5 - 4.605170 = 0.394830$,

$$P(M_n - \ln n \le y) \approx \exp\left(-e^{-y}\right)
= \exp(-0.673794) = \boxed{0.509770}.$$

The two differ by $0.00116$ in probability, or $0.23\%$ relative — the approximation
is already excellent at $n = 100$.

**Why the shift.** The maximum of $n$ exponentials grows like $\ln n$, because the
typical largest value sits where the survival function is about $1/n$, that is where
$e^{-x} \approx 1/n$. Subtracting $\ln n$ removes that growth so that the
distribution converges to a fixed limit. Without the shift there is no limit: the
distribution slides to the right forever.

---

## ★7 — Pareto moments

For a Pareto variable with $P(X > x) = (x/x_{\min})^{-\alpha}$ on $x \ge x_{\min}$,

$$E[X] = \frac{\alpha\,x_{\min}}{\alpha - 1} = \frac{3 \times 2}{2} =
\boxed{3},$$

$$\operatorname{Var}(X) = \frac{\alpha\,x_{\min}^{2}}{(\alpha-1)^{2}(\alpha-2)}
= \frac{3 \times 4}{4 \times 1} = \boxed{3}.$$

The $k$-th moment exists if and only if $\alpha > k$, so with $\alpha = 3$ the
highest existing moment is the **third**, and the fourth moment (and hence the
kurtosis, and the sampling variance of a sample variance) does not exist.

**What that means in practice.** A sample variance from this distribution is unbiased
in expectation but converges very slowly and is right-skewed, so a single sample
variance typically sits well below $3$. The lesson's simulation measured exactly this
for $\alpha = 2.5$: $78.5\%$ of samples of size $10\,000$ understated the true
variance. For $\alpha = 3$ the bias would be smaller but still substantial. The
median and other quantiles are unaffected by the missing moments and should be
preferred for reporting.

---

## ★8 — Bias in tail estimation

Two reasons the estimate of $\hat\alpha = 2.4$ may be biased:

1. **Threshold bias.** The power law holds only above some lower limit. If the
   window includes values below it, the fitted exponent is pulled toward the
   exponent of whatever distribution describes the bulk — and if the bulk is
   lognormal or exponential, the estimate can move in either direction depending on
   where the window starts. This is the dominant source of systematic error in
   practice, and it is why the estimate depends on the window size.
2. **Finite-sample bias of the Hill estimator.** Even in the exact power-law regime,
   the Hill estimator is biased low for moderate $k$ and its dispersion grows as $k$
   shrinks. With $5\%$ of $20\,000$ values the window contains $1000$ order
   statistics, which is adequate; with $10\%$ of $5000$ it contains $500$, which is
   still workable but noisier.

**The diagnostic** is a plot of $\hat\alpha(k)$ against $\ln k$ over a wide range of
$k$. A genuine power law produces a plateau in the estimate, and the size of the
plateau is a visual statement of how much of the data are consistent with the
power-law form. The absence of a plateau means there is no single exponent to report,
and the honest response is to say so. A second, independent diagnostic is to fit a
lognormal to the same window and compare the likelihoods: over two or three decades
the two models are often nearly indistinguishable, and reporting only the power law
hides that ambiguity.

---

## ★9 — Poisson as a binomial limit

**(a)** Let $N \sim \text{Binomial}(n, p)$ with $p = \lambda T/n$ held constant as
$n$ grows. Then for fixed $k$,

$$P(N = k) = \binom{n}{k}p^{k}(1-p)^{n-k}
= \frac{n(n-1)\cdots(n-k+1)}{k!}\left(\frac{\lambda T}{n}\right)^{k}
\left(1 - \frac{\lambda T}{n}\right)^{n-k}.$$

**(b)** Take the three factors in turn.

- The falling factorial: $n(n-1)\cdots(n-k+1)/n^{k} \to 1$ as $n \to \infty$, because
  there are $k$ factors each tending to $1$.
- The power: $(\lambda T/n)^{k}$ is unchanged, and the $k$ factors of $n$ in the
  falling factorial cancel those in the denominator.
- The last factor:
  $\left(1 - \frac{\lambda T}{n}\right)^{n-k} = \left(1 -
  \frac{\lambda T}{n}\right)^{n}\left(1 - \frac{\lambda T}{n}\right)^{-k}$,
  and using the standard limit $(1 - a/n)^{n} \to e^{-a}$ together with
  $\left(1 - \lambda T/n\right)^{-k} \to 1$, this tends to $e^{-\lambda T}$.

Collecting,

$$P(N = k) \to \frac{(\lambda T)^{k}}{k!}e^{-\lambda T},
\qquad \blacksquare$$

the Poisson PMF with mean $\lambda T$. The result is a proper PMF automatically,
because it is the limit of proper PMFs; this is why the normalisation in the lesson's
demonstration came out to $1$ to twelve decimal places.

**The physical assumption made explicit.** The limit $p = \lambda T/n \to 0$ with
$n \to \infty$ says that events are rare in any short interval and that the
probability of an event is proportional to the length of the interval. The second
part is the constant-hazard assumption, and it is that — not the algebra — which
fails for clustering seismicity, seasonal recharge and self-exciting processes.

---

## ★10 — Gumbel limit

**(a)** Independence gives

$$P(M_n \le x) = \prod_{i=1}^{n}P(X_i \le x) = \left(1 - e^{-x}\right)^{n}.$$

**(b)** Substitute $x = y + \ln n$ and take logarithms:

$$\ln P(M_n \le y + \ln n) = n\ln\left(1 - e^{-y - \ln n}\right)
= n\ln\left(1 - \frac{e^{-y}}{n}\right).$$

For large $n$ the argument $e^{-y}/n$ is small, so
$\ln(1 - u) = -u - u^{2}/2 - \cdots$ gives

$$n\ln\left(1 - \frac{e^{-y}}{n}\right) = -e^{-y} -
\frac{e^{-2y}}{2n} - \cdots \to -e^{-y}.$$

**(c)** Hence

$$P(M_n - \ln n \le y) \to \exp\left(-e^{-y}\right),$$

the **Gumbel** distribution. Its mean is the Euler–Mascheroni constant
$\gamma = 0.577216$ and its variance is $\pi^{2}/6 = 1.644934$.

**The physical meaning of $\ln n$.** The maximum of $n$ independent exponentials grows
logarithmically with the sample size, because the largest value typically sits where
the survival function is about $1/n$, i.e. at $x \approx \ln n$. In practice this
says that collecting ten times as much data raises the largest observable flood,
storm surge or ground motion by only a fixed increment, and the increment shrinks
with each further decade. This is why return-level estimation is a problem in the
tail form, not merely in the sample size.

---

## ★11 — Products of lognormals

**(a)** Let $X_i$ be independent with $\ln X_i \sim \mathcal{N}(\mu_i,
\sigma_i^{2})$. Then

$$\ln\left(\prod_{i=1}^{k}X_i\right) = \sum_{i=1}^{k}\ln X_i,$$

a sum of independent normal variables, which is normal with mean
$\sum_i\mu_i$ and variance $\sum_i\sigma_i^{2}$ (independence eliminates the
covariances). Therefore the product is lognormal with

$$\mu_{\text{prod}} = \sum_{i=1}^{k}\mu_i, \qquad
\sigma^{2}_{\text{prod}} = \sum_{i=1}^{k}\sigma_i^{2}.$$

**(b)** Three sentences.

Permeability arises from the product of many local multiplicative factors, so its
logarithm is a sum of independent contributions and the field is lognormal with the
arithmetic mean exceeding the median by the factor $e^{\sigma^{2}/2}$, which for
$\sigma_{\ln} = 1$ is $1.65$. A flow calculation in a layered or channelised medium
is controlled by the harmonic or the geometric mean of permeability rather than the
arithmetic mean, so using the arithmetic mean overstates the flow capacity, and using
it while also reporting it as "typical" misdescribes the distribution twice over. The
**geometric mean**, $e^{\mu}$, equal to the median, is the summary that respects the
multiplicative mechanism, and it is the quantity an analyst should report unless the
flow geometry specifically calls for a different average.

---

## ★12 — Extrapolating a power law

**(a)** With $\hat\alpha = 1.8$, the mean exists (needs $\alpha > 1$), the variance
does not (needs $\alpha > 2$), and neither does any higher moment. So the fit supports
a mean and quantiles, and nothing that depends on a second moment.

**(b)** The sample mean does not converge. Its fluctuation scales as
$n^{-(1-1/\alpha)} = n^{-0.444}$, much slower than the $n^{-1/2}$ of a finite-variance
variable, and the estimate is dominated by the largest observation. In practice the
running mean shows long plateaus interrupted by jumps as a new extreme value enters,
and it never settles — the behaviour measured for $\alpha = 1.5$ in
[01-13-05](../05-sampling-and-clt.md) Section 2.3.

**(c)** A return level at probability $p$ scales as $x_{\min}p^{-1/\alpha}$, so

$$\frac{d \ln x_p}{d\alpha} = \frac{\ln(1/p)}{\alpha^{2}}.$$

For a one-in-a-thousand-year event, $\ln(1/p) = 6.9$; with $\alpha = 1.8$ the
sensitivity is $6.9/3.24 = 2.13$, so a change of $0.1$ in $\alpha$ — about $6\%$ of
its value — moves $\ln x_p$ by $0.213$, that is it moves the return level by a factor
of $1.24$. But the *form* of the tail matters more, because a lognormal fitted to the same
data can have a tail that decays faster in the extrapolated region, giving a return
level lower by an order of magnitude, while fitting the observed range equally well.
The exponent is estimable; the form is not, from data that stop at the largest
observed event.

**(d)** Before accepting the extrapolation I would require: the window size $k$ used,
and a plot of $\hat\alpha(k)$ showing a plateau; a comparison fit of at least one
alternative heavy-tailed family (lognormal, generalised extreme value) with a
statement of how their extrapolated return levels differ; a statement of the
extrapolation distance in units of the observed range; a confidence interval for the
return level that includes the uncertainty in $\alpha$ (which is far wider than the
standard error of $\hat\alpha$ implies once the extrapolation is included); and an
independent argument, physical rather than statistical, for why the power-law form
should continue beyond the observed range. Without the last item the extrapolation is
an assumption reported as a number.
