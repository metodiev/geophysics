# Solutions — 18-06-02 Monte Carlo Propagation and Its Convergence

> Read after attempting the exercises. Numbers were computed, not estimated.
> Lesson: [02 Monte Carlo Propagation and Its Convergence](../02-monte-carlo-uq.md).

---

## ★1 — Sample size for a target relative error

$$
\hat\mu_N = \frac1N\sum_i g(X_i), \qquad
\text{s.e.}(\hat\mu_N) = \frac{\hat\sigma_g}{\sqrt N}.
$$

The relative error is $\text{CV}/\sqrt N$ with CV the coefficient of variation of the
output. For CV $= 0.10$ and a relative error of $0.005$:

$$
\frac{0.10}{\sqrt N} = 0.005 \ \Rightarrow\ \sqrt N = 20 \ \Rightarrow\ N = 400 .
$$

---

## ★2 — Linearised versus Monte Carlo variance

$$
\text{relative discrepancy} = \frac{0.0157 - 0.0152}{0.0157} = 0.031847 = 3.18\% .
$$

The standard deviation is itself a random quantity with relative standard error
$\approx 1/\sqrt{2N}$, so at $N = 2\times10^{6}$,

$$
\frac{1}{\sqrt{2N}} = \frac{1}{\sqrt{4\times10^{6}}} = 5.0\times10^{-4} = 0.05\% .
$$

The $3.18\%$ discrepancy is $64$ times larger than the Monte Carlo error, so it is
**not** explained by sampling: the linearised propagation is genuinely $3.2\%$ low,
because the sphere anomaly is nonlinear in $R$ over the $\pm8\%$ input spread.

---

## ★3 — Why the sample count is not precision

The precision of a Monte Carlo mean is $\sigma_g/\sqrt N$, so it depends on the
output variance as well as on the sample count: two studies with the same $N$ can
differ in precision by orders of magnitude. A run that reports draws without a
standard error gives the reader no way to tell a converged answer from a noisy one.

---

## ★★4 — Antithetic variance reduction and when it fails

A variance reduction factor of $20.99$ means the antithetic estimator with $N$
evaluations has the same variance as a plain estimator with $20.99N$ evaluations.
At $N = 2000$ that is

$$
2000 \times 20.99 = 41\,980 \approx 4.2\times10^{4}
$$

plain evaluations for the same precision.

The condition under which it fails: the reduction relies on $g(Z)$ and $g(-Z)$
being negatively correlated, which holds when $g$ is monotone in the inputs. For a
non-monotone or oscillatory $g$ the pair can be positively correlated, and the
antithetic estimator then has a *larger* variance than plain Monte Carlo. The
sphere anomaly is increasing in $R$ and $\rho$ and decreasing in $z$, which is why
the reduction is so large here.

---

## ★★5 — Rare events

**(a)** For a probability $p$, the relative standard error of the counting estimator
is $\sqrt{(1-p)/(pN)} \approx 1/\sqrt{pN}$, so a $10\%$ relative error needs

$$
N \approx \frac{1}{p\,(0.10)^2} = \frac{100}{p} = \frac{100}{3.570\times10^{-5}}
= 2.8\times10^{6} .
$$

**(b)** The effective sample size was $21\,954$ of $200\,000$, i.e. $10.98\%$. The
weights are therefore reasonably balanced: not dominated by a handful of draws,
which is the failure mode that makes an importance-sampling estimate unusable.

**(c)** Report the importance-sampling estimate: it used ten times fewer forward
evaluations and has a smaller standard error ($1.1\times10^{-6}$ against
$4.3\times10^{-6}$). The plain estimate is consistent with it (difference $0.42$
standard errors) but rests on $75$ events and has an $11.5\%$ relative error. State
both, and state the effective sample size, because the importance-sampling estimate
would be untrustworthy if that number were small.

---

## ★★6 — Why a quantile is harder than a mean

The mean is an average of every sample, so every draw contributes. A quantile is
determined by the local density near that quantile: the standard error of the
$q$-quantile is approximately

$$
\text{s.e.}(\hat q) \approx \frac{\sqrt{q(1-q)/N}}{f(q)},
$$

which depends on the density $f$ at the quantile. In a tail the density is small, so
the standard error is a much larger fraction of the quantity itself — hence the
convergence of tail estimates is slower than the mean's, and the demonstration's
rare-event section is the extreme case.

**Practical consequence.** A decision with a threshold in the tail of a predicted
distribution — a detection threshold, a safety factor — is driven by a quantity that
a simulation reports with the least accuracy. Quote the standard error of the
quantile, or carry out enough samples that it is small relative to the margin
between the prediction and the threshold.

---

## ★★7 — Measuring variance reduction

- **Metric:** the ratio of the empirical variance of the estimate over $R$
  independent replicates, for the plain and reduced estimators at equal evaluation
  budget; report the ratio with its own standard error.
- **Replicates:** $R \ge 400$ so that the twentieth percentile of the variance ratio
  is resolvable; the demonstration uses $400$ and obtains
  $0.000353/0.000077 = 4.58$ in standard deviations, i.e. a variance ratio of
  $20.99$.
- **Decision rule:** accept the reduction only if the measured ratio is significantly
  above $1$ at two standard errors, and re-measure it whenever the model or the input
  distributions change, because the reduction is a property of the integrand.

---

## ★★8 — Budget allocation for an expensive forward solve

- **Sampling:** one Latin-hypercube or quasi-random design of $200$–$500$ forward
  solves for surrogate training, plus $2000$–$5000$ surrogate evaluations (free) with
  a validation set of $100$–$200$ *actual* forward solves held out.
- **Surrogate construction:** the fitting cost is negligible; the cost is the
  training solves, about $500$ hours at one hour per solve.
- **Validation:** the held-out forward solves, about $200$ hours.
- **Remainder:** direct Monte Carlo on the surrogate for the tail quantities, whose
  standard error is estimated from the surrogate ensemble and then propagated
  through the surrogate's own validation error.
- **Diagnostic to report:** the held-out RMSE of the surrogate against the target
  accuracy of the UQ quantity, plus a comparison of the surrogate-based mean and
  variance against a smaller direct Monte Carlo run (say $200$ solves) with its own
  standard error. If the surrogate error is not small compared with the UQ error,
  the allocation must shift towards validation, not towards more sampling.
