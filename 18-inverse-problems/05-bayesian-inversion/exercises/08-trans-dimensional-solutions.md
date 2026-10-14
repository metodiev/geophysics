# Solutions — 18-05-08 Trans-Dimensional and Reversible-Jump MCMC

> Read after attempting the exercises. Numbers were computed, not estimated.
> Lesson: [08 Trans-Dimensional and Reversible-Jump MCMC](../08-trans-dimensional.md).

---

## ★1 — Birth acceptance ratio

$$
\ln\alpha_{\text{birth}} =
\ln\frac{\mathcal{L}(k+1,c')}{\mathcal{L}(k,c)}
+ \ln\frac{p(c'\mid k+1)}{p(c\mid k)}
+ \ln\frac{\pi_{\text{death}}(k+1)}{\pi_{\text{birth}}(k)}
- \ln q(u),
$$

with $p(c'\mid k+1)/p(c\mid k) = \mathcal{N}(u;0,\tau^2)$ and
$q(u) = \mathcal{N}(u;0,s^2)$. When $s = \tau$ the last two terms cancel exactly,
and the ratio reduces to the likelihood ratio times the proposal-probability ratio.
When $s \ne \tau$ they do not cancel, and the surviving ratio is the correction for
proposing the new coefficient from a distribution other than the prior.

---

## ★2 — Occupancy and its standard error

$$
P(k=0) = \frac{200}{100\,000} = 0.0020 .
$$

The denominator for the standard error is **not** the number of retained iterations
($100\,000$), because the model index changes only on accepted birth-or-death
transitions. Using the $9000$ transitions as the effective sample size:

$$
\text{SE} = \sqrt{\frac{0.002\times0.998}{9000}} = 4.71\times10^{-4}.
$$

Using $100\,000$ would give $1.41\times10^{-4}$, an understatement by a factor of
$3.3$ — and the true error is still larger if the transitions are themselves
correlated in time.

---

## ★3 — The four factors

1. **Prior density of the created/deleted parameter** — accounts for the change in
   the dimension of the prior.
2. **Proposal density of the dimension-changing move** — the density from which the
   auxiliary variable is drawn (and its reverse).
3. **Proposal-probability ratio** — the probability of proposing the reverse move
   divided by the probability of proposing the forward move, given the current
   state.
4. **Jacobian of the dimension-matching map** — the volume change of the
   transformation between the augmented parameter spaces; equal to $1$ for a vector
   extension, and not equal to $1$ for a nonlinear map such as a log transform.

---

## ★★4 — Model probabilities from the evidences

With a uniform model prior,

$$
P(k\mid d) \propto e^{\ln p(d\mid k)} .
$$

Subtracting the largest value $-14.8061$:

$$
e^{-5.6707} = 0.003446,\qquad e^{-0.5843} = 0.557548,\qquad e^{0} = 1.000000 .
$$

Sum $= 1.560994$, hence

$$
P(k\mid d) = (0.002208,\ 0.357168,\ 0.640624) \approx (0.0022,\ 0.3572,\ 0.6406).
$$

This matches the demonstration's analytic column to four decimals, as it must: the
demonstration computes exactly this.

---

## ★★5 — Bayes factor for order 2 against order 1

$$
\ln B_{21} = -14.8061 - (-15.3904) = 0.5843
\ \Rightarrow\
B_{21} = e^{0.5843} = 1.7938,
\qquad \log_{10}B_{21} = 0.2538 .
$$

The expected log-odds is $\ln B_{21} = 0.5843$, which is **less than one**: the
evidence for order 2 over order 1 is about $1.8{:}1$, a mild preference, not a
decisive one. Reporting "the quadratic model is preferred" without the number $1.8$
overstates how much the data have settled the question — and Section 7 of the
lesson shows that with more data the same preference reverses.

---

## ★★6 — Birth/death asymmetry

Births are proposed only from states $k < K$, and they are accepted $0.582$ of the
time because the extra coefficient can usually improve the fit slightly. Deaths are
proposed from any $k > 0$, and the chain spends most of its time at $k = 2$, where a
death proposal must remove a coefficient the likelihood needs; hence the low
acceptance, $0.126$.

A death rate of $0.02$ would indicate that the chain is effectively **stuck** in the
largest model: it cannot leave $k = 2$, so $P(k)$ for the smaller orders is
estimated from a handful of visits, and the reported model probabilities are
dominated by the initial condition rather than by the data. The diagnostic response
is to increase the efficiency of the reverse move (propose the deleted coefficient
from a distribution closer to its posterior conditional, using the same correction
as in ★1) and to re-run, then check that the index ESS is large enough to report.

---

## ★★7 — Synthetic recovery test

- **Injected model:** a known number of layers, for example $k_{\text{true}} = 3$,
  with velocities and thicknesses drawn from the prior; data generated from the
  forward model with noise drawn from the stated likelihood.
- **Family and priors:** orders $0\le k\le 6$, coefficients $\mathcal{N}(0,\tau^2)$,
  uniform prior over $k$, with $\tau$ set to the values to be used in production.
- **Chains:** at least four, started in different orders including the maximum.
- **Diagnostics:** birth and death acceptance rates (both above $0.05$), index ESS
  above $400$, split $\hat R < 1.01$ for every parameter and for the model index.
- **Criterion for verified:** the posterior modes at $k_{\text{true}}$ and gives it
  at least $50\%$ of the mass; and the parameter posteriors bracket the injected
  values within their $95\%$ intervals. Repeat with $k_{\text{true}} = 1$ and
  $k_{\text{true}} = 5$ so that the test is not passing for one configuration only.

**What it cannot establish:** it cannot show the sampler is unbiased for all data.
A chain can be verified on a synthetic problem and still be wrong for real data if,
for example, the real likelihood has a region the moves cannot traverse. And a
passing recovery test cannot validate the *family*: if the truth lies outside the
candidate orders, the test with an injected member of the family cannot detect it.

---

## ★★8 — Mass at the largest order

1. **The truth genuinely needs that many layers**, or the data genuinely cannot
   distinguish the largest order from more. Experiment: extend the family to
   $k = K+2$ and re-run. If the pile-up moves to the new boundary, the family is
   still too small; if it stays at $K$, the data support order $K$.
2. **The prior on the extra coefficient is too tight**, so births are almost never
   accepted and the chain cannot leave the largest order it happened to reach.
   Experiment: widen $\tau$ (with the same correction ratios as ★1) and check
   whether the birth acceptance rate rises and the pile-up relaxes.

An **implementation error** is the third possibility and is distinguished by the
verification route of ★★7: a synthetic recovery test with an injected interior
model would fail, showing that the sampler, not the family, is the problem. Note
that a wrong Jacobian or a dropped proposal ratio can produce a *plausible-looking*
pile-up, which is exactly why the independent route is mandatory.
