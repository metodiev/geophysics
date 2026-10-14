# Solutions — 18-05-06 Posterior Summaries: Marginals, Credible Intervals, Correlations

> Read after attempting the exercises. Numbers were computed, not estimated.
> Lesson: [06 Posterior Summaries](../06-posterior-summary.md).

---

## ★1 — Loss minimisation

$$
f(a) = \mathbb{E}[(m-a)^2] = \mathbb{E}[m^2] - 2a\,\mathbb{E}[m] + a^2,
\qquad
f'(a) = -2\mathbb{E}[m] + 2a = 0 \ \Rightarrow\ a = \mathbb{E}[m].
$$

Since $f''(a) = 2 > 0$ this is the unique minimum. The **median** minimises the
absolute-error loss $\mathbb{E}[\lvert m-a\rvert]$; the **mode** minimises the
zero-one loss.

---

## ★2 — Two interval definitions

**Equal-tailed:** $[q_{0.025},q_{0.975}]$ from the posterior CDF, with $2.5\%$ of
the probability in each tail.

**HPD:** the shortest interval whose posterior probability is $0.95$; for a unimodal
density its endpoints have equal density.

Measured for the demonstration's inverse-gamma posterior: equal-tailed
$[0.6321,2.7979]$, width $2.1658$; HPD $[0.5264,2.4318]$, width $1.9054$. The HPD
is $1.137$ times shorter. The HPD moves mass out of the left tail
($0.025 \to 0.003$) into the right tail ($0.025 \to 0.047$), because the density
is higher on the left; the short interval spends its probability budget where the
density is large.

---

## ★3 — Credible is not confidence

A credible interval is **conditional on the observed data and the stated prior**:
it says the parameter lies in the interval with posterior probability $0.95$ under
that pair. A confidence interval is a statement about repeated sampling from the
data-generating process: it says that intervals so constructed would contain the
true parameter in $95\%$ of replications. Because the first conditions on the data
and averages over the parameter, and the second averages over data at a fixed
parameter, there is no theorem linking them, and the measured coverage table
demonstrates the gap.

---

## ★★4 — Marginal and conditional widths

$$
\sigma_{\text{marginal}} = 1.0000, \qquad
\sigma_{\text{conditional}} = \sqrt{1-\rho^2} = \sqrt{0.19} = 0.435890,
$$

$$
\frac{\sigma_{\text{marginal}}}{\sigma_{\text{conditional}}}
= \frac{1}{\sqrt{1-\rho^2}} = 2.2942 .
$$

---

## ★★5 — Two coverage numbers

Under the weak prior $\mathcal{N}(1.0, 20^2)$ the prior contributes
$1/400 = 0.0025$ to a precision while the six data contribute
$N/\sigma^2 = 6$; the prior share is $0.04\%$, so the posterior interval is
essentially the likelihood interval, and both coincide at
$0.953$ — a Monte Carlo estimate of the nominal $0.95$ with $4000$ replicates
(standard error $\sqrt{0.95\cdot0.05/4000} = 0.0034$, so $0.953$ is $0.9$ standard
errors from $0.95$).

Under the conflicting prior $\mathcal{N}(3.0,0.5^2)$ the prior contributes $4$ to
the precision against the data's $6$; the prior share is $40\%$, and the posterior
is centred near a value the data do not support. The interval covers the truth in
$23.5\%$ of replicates.

Neither is "wrong". The second interval correctly reports what follows from the
model — data model plus prior — and the model is wrong about the prior. What is
wrong is any claim that the number $0.95$ describes repeated-sampling coverage
unless the prior happens to be well calibrated.

---

## ★★6 — Transforming a quantity of interest

Because $g(\sigma) = 1/\sigma$ is strictly decreasing, the quantiles transform
by reversing:

$$
\sigma \in [0.6321,\ 2.7979]
\ \Rightarrow\
g \in \left[\frac{1}{2.7979},\ \frac{1}{0.6321}\right] = [0.357411,\ 1.581967].
$$

The mean does **not** transform this way. The $95\%$ upper limit of $g$,
$1.5820$, is far above $1/\mathbb{E}[\sigma] = 1/1.2871 = 0.776939$, because the
distribution of $1/\sigma$ has a long upper tail: small values of $\sigma$ are
possible and they produce very large values of $g$. Formally
$\mathbb{E}[1/\sigma] \neq 1/\mathbb{E}[\sigma]$ by Jensen's inequality, and the
interval $[0.3574,1.5820]$ is not symmetric about $1/\mathbb{E}[\sigma]$ — or about
anything. Report the interval, not the reciprocal of the mean.

---

## ★★7 — Credible volume versus the product of marginals

From the measured table: the $95\%$ region area is $2.6553$ at $\rho = 0.99$ and
$18.8227$ at $\rho = 0$, so

$$
\frac{2.6553}{18.8227} = 0.1411 .
$$

The region shrinks by a factor of $7.09$. The product of the marginal interval
widths is constant, so its ratio is $1.0000$. The consequence: quoting one interval
per parameter and treating their product as the admitted volume overstates the
region by $5.79$ times at $\rho = 0.99$. Joint statements require the joint
region — a covariance, a sample, or a contour — not the collection of marginal
intervals.

---

## ★★8 — Coverage study design

- **Generating process:** a synthetic model with a known true parameter vector; the
  data generated exactly from the assumed likelihood, then, in a second arm, with a
  deliberate misspecification (heavy tails, or correlated errors).
- **Interval construction:** for each replicate, run the inversion and form the
  $95\%$ equal-tailed credible interval from the posterior sample.
- **Replicates:** for a standard error of $0.005$ on a coverage near $0.95$,
  $n = 0.95\cdot0.05/0.005^2 = 1900$; use $2000$ to be safe.
- **Interpretation:** a measured coverage of $0.90$ means the intervals contain the
  truth in $90\%$ of replications under a construction that claims $95\%$. Under a
  correctly specified likelihood and a well-calibrated prior this should not
  happen, so the diagnosis is a **likelihood or prior misspecification** — too
  narrow a likelihood (unmodelled correlation, as measured in lesson
  [02](../02-likelihood-models.md)), or a prior that is confidently wrong (as
  measured in this lesson). It is not evidence that the sampler is broken: a
  biased sampler usually distorts the interval only modestly, whereas a
  misspecified likelihood distorts it systematically, and the two can be separated
  by re-running on data generated from the *assumed* likelihood, where coverage
  should return to $0.95$.
