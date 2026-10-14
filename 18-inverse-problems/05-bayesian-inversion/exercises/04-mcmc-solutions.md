# Solutions — 18-05-04 Markov Chain Monte Carlo: Metropolis-Hastings and Gibbs

> Read after attempting the exercises. Numbers were computed, not estimated.
> Lesson: [04 Markov Chain Monte Carlo: Metropolis-Hastings and Gibbs](../04-mcmc.md).

---

## ★1 — Detailed balance

$$
\pi(x)\,T(x'\mid x) = \pi(x')\,T(x\mid x')
\quad\text{for all } x, x' .
$$

For a symmetric proposal $q$ and the Metropolis rule
$\alpha(x\to x') = \min(1, \pi(x')/\pi(x))$, suppose $\pi(x')\le\pi(x)$ so that
$\alpha(x\to x') = \pi(x')/\pi(x)$ and $\alpha(x'\to x) = 1$. Then

$$
\pi(x)q(x'\mid x)\alpha(x\to x')
= \pi(x)q(x'\mid x)\frac{\pi(x')}{\pi(x)}
= \pi(x')q(x\mid x')\cdot 1
= \pi(x')q(x\mid x')\alpha(x'\to x),
$$

using $q(x'\mid x) = q(x\mid x')$. The other case is symmetric. Detailed balance
holds, so $\pi$ is stationary.

---

## ★2 — Effective sample size and standard error

$$
\text{ESS} = \frac{n}{\tau} = \frac{50\,000}{250} = 200,
\qquad
\text{SE}(\bar m) = \frac{s}{\sqrt{\text{ESS}}} = \frac{2}{\sqrt{200}} = 0.141421 .
$$

---

## ★3 — Acceptance probability

$$
\alpha = \min\!\left(1,\ e^{-2.5}\right) = e^{-2.5} = 0.082085 .
$$

Note that this is the acceptance probability **conditional on that proposal**; it
is not the average acceptance rate of the chain, which depends on how often such
moves are proposed.

---

## ★★4 — Split R-hat

With $m = 4$ chains of $n = 1000$, $W = 0.5$ and $B = 10$:

$$
\widehat{\operatorname{Var}} = \frac{n-1}{n}W + \frac{B}{n}
= \frac{999}{1000}(0.5) + \frac{10}{1000}
= 0.4995 + 0.0100 = 0.5095,
$$

$$
\hat R = \sqrt{\frac{0.5095}{0.5}} = \sqrt{1.019} = 1.009448 .
$$

The chains have not converged by the usual threshold $\hat R < 1.01$: $1.0094$ is
just below it, but the between-chain variance is $20$ times the within-chain
variance divided by $n$ **before** averaging, so the between-chain spread is
material. This is the situation where quoting the number is more informative than
quoting the verdict. Also check: the effective sample size of each parameter, the
starting points (were they dispersed?), the trace of each chain, and whether any
chain is stuck. $\hat R$ alone can be near 1 for a chain trapped in one of two
modes if all chains are trapped in the same one.

---

## ★★5 — Gibbs conditional

For a Gaussian with means $(\mu_1,\mu_2)$, unit variances and correlation $\rho$,

$$
m_1 \mid m_2 \sim \mathcal{N}\!\left(\mu_1 + \rho\,(m_2-\mu_2),\ 1-\rho^2\right)
\ \Rightarrow\ \sigma = \sqrt{1-0.81} = 0.435890 .
$$

The marginal standard deviation is $1.0000$. The ratio is
$1/\sqrt{1-\rho^2} = 2.2942$: knowing $m_2$ removes $81\%$ of the variance of
$m_1$, because the two are nearly the same number.

---

## ★★6 — ESS per thousand iterations

From the demonstration's table, the ESS values are over $38\,000$ retained draws,
so per $1000$ retained iterations:

| step | acceptance | ESS | ESS per $1000$ iterations |
|---|---|---|---|
| 0.10 | 0.893 | 68 | $1.79$ |
| **1.50** | **0.199** | 1736 | **$45.7$** |
| 3.00 | 0.072 | 1242 | $32.7$ |

Choose step $1.50$. Its ESS per iteration exceeds step $3.0$ by a factor
$1736/1242 = 1.398$ and step $0.1$ by a factor $1736/68 = 25.5$. The high
acceptance at step $0.1$ is precisely the problem: nearly every proposal is
accepted because nearly every proposal is indistinguishable from the current
state, so the chain barely moves and its autocorrelation time is $559.3$.

---

## ★★7 — Why continuous adaptation is invalid

Adapting the proposal from the past of the chain makes the kernel at step $t$
depend on the entire history $x^{(1..t-1)}$, not only on $x^{(t-1)}$. The sequence
is then not a Markov chain with a fixed kernel, detailed balance does not hold for
the adapted kernel, and the stationary distribution of the process need not be
$\pi$. The draws can be biased in a way that no within-chain diagnostic reveals,
and $\hat R$ across adapted chains is not calibrated.

Legitimate route: **adapt during warm-up only**, then freeze all tuning parameters
and start the sampling phase. Report the frozen values. Alternatively use an
adaptive scheme with a proven ergodicity result and cite it, and report the
adaptation window explicitly.

---

## ★★8 — Convergence study for a bimodal target

- **Chains:** at least $8$ independent chains.
- **Starting points:** dispersed, for example an over-dispersed sample from the
  prior, plus one chain started in the neighbourhood of each suspected mode. The
  point is that at least one chain must have a chance of finding the second mode.
- **Diagnostics:** split $\hat R$ per parameter; effective sample size; trace
  plots; rank-normalised $\hat R$ (which is sensitive to heavy tails); and the
  count of mode visits per chain, with the posterior mass assigned to each mode.
- **Thresholds, declared in advance:** $\hat R < 1.01$ after rank normalisation,
  $\text{ESS} > 400$ for every reported quantity, and every chain visiting every
  mode with at least $1\%$ of its draws.

**What the study cannot establish:** it cannot show that no unvisited mode exists.
If all chains miss a mode, every diagnostic will pass. The only genuine evidence
is an independent route — an analytic solution, a synthetic recovery test, or an
exhaustive search on a reduced problem — and even then the claim is limited to the
family searched.
