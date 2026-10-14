---
id: 18-05-04
title: "Markov Chain Monte Carlo: Metropolis-Hastings and Gibbs"
level: research
prereqs: ["18-05-01", "18-05-02", "03-02-06"]
tags: [inverse-problems, bayesian, uncertainty-quantification, mcmc, metropolis-hastings, gibbs, convergence-diagnostics]
---

# Markov Chain Monte Carlo: Metropolis-Hastings and Gibbs

All models in this module are **SYNTHETIC**. The target of this lesson is a
deliberately simple correlated Gaussian whose moments are known in closed form,
so that every diagnostic can be checked against an exact answer. Every number
quoted is printed by [`code/mcmc_demo.py`](./code/mcmc_demo.py).

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the Metropolis-Hastings acceptance probability from detailed
   balance, and state the symmetry assumption that reduces it to the Metropolis
   rule.
2. **Construct** a random-walk proposal and **tune** its scale using a measured
   acceptance-rate/efficiency curve rather than a rule of thumb.
3. **Estimate** the integrated autocorrelation time and the effective sample
   size, and **explain** why the acceptance rate alone is not a quality measure.
4. **Compute** the split $\hat R$ diagnostic over several chains and state
   precisely what it rules out and what it cannot detect.
5. **Derive** the Gibbs sampler as a special case of Metropolis-Hastings with
   acceptance probability one, and state the condition under which it exists.
6. **Diagnose** a chain that has failed to converge using at least three
   independent pieces of evidence.
7. **Report** an MCMC result with the diagnostic quantities that make it
   auditable.

## Prerequisites

- [18-05-01 Bayes' Theorem as an Inverse-Problem Formulation](01-bayes-inverse-formulation.md)
  — what is being sampled and why.
- [18-05-02 Constructing Likelihoods and Error Models](02-likelihood-models.md)
  — evaluating the target in practice.
- [03-02-06 The Random Module in NumPy](../../03-scientific-computing/02-numpy/06-random-module.md)
  — generators, seeding and reproducibility.
- [21-03-04 MCMC in Practice](../../21-statistics-bayesian-ml/03-bayesian-inference/04-mcmc-practice.md)
  — the general statistical workflow this lesson specialises.

## 1. Intuition: why we sample instead of integrating

The posterior answers every question of interest:

$$
\mathbb{E}[f(m)\mid d] = \int f(m)\,p(m\mid d)\,\mathrm{d}m,
\qquad
p(m_i\mid d) = \int p(m\mid d)\prod_{j\neq i}\mathrm{d}m_j .
$$

In one or two dimensions these integrals are done on a grid, as in lessons
[01](01-bayes-inverse-formulation.md) and [03](03-priors.md). In a hundred
dimensions a grid with 10 points per axis needs $10^{100}$ evaluations. A Markov
chain Monte Carlo method replaces the integral by an average over a sequence of
correlated draws whose limiting distribution is the posterior, so the cost grows
with the information required rather than with the dimension of the grid.

The price is that the draws are **correlated** and **sequential**. Every
diagnostic in this lesson exists to answer the single question: how much
information did those draws actually contain?

## 2. Markov chains and the target

A Markov chain is a sequence $x^{(1)}, x^{(2)},\dots$ where the next state depends
only on the current one, through a transition kernel $T(x'\mid x)$. If the target
$\pi(x)$ satisfies detailed balance,

$$
\pi(x)\,T(x'\mid x) = \pi(x')\,T(x\mid x'),
$$

then $\pi$ is a stationary distribution of the chain, and if the chain is
irreducible and aperiodic it converges to $\pi$ from any starting point. The
whole craft of MCMC is designing kernels that satisfy detailed balance for a
target that can only be evaluated up to a constant — which is exactly the
situation of a posterior $p(m\mid d)\propto p(d\mid m)p(m)$, where the
normalising constant $p(d)$ is unknown and possibly intractable.

## 3. Metropolis-Hastings

Propose $x' \sim q(\cdot\mid x)$ and accept with probability

$$
\alpha(x\to x') = \min\!\left(1,\
\frac{\pi(x')\,q(x\mid x')}{\pi(x)\,q(x'\mid x)}\right).
$$

*Why this works.* Detailed balance for the resulting kernel requires
$\pi(x)q(x'\mid x)\alpha(x\to x') = \pi(x')q(x\mid x')\alpha(x'\to x)$. Assume
without loss that the left acceptance is $1$ and the right is the ratio below
$1$; substituting gives $\pi(x)q(x'\mid x) = \pi(x')q(x\mid x')\cdot
\pi(x)q(x'\mid x)\big/\bigl(\pi(x')q(x\mid x')\bigr)$, an identity. Since
$\pi$ enters only through ratios, the unknown normalising constant cancels —
this is the single most important structural fact about MCMC.

For a **symmetric** proposal, $q(x'\mid x) = q(x\mid x')$, the rule reduces to the
Metropolis form

$$
\alpha(x\to x') = \min\!\left(1,\ \frac{\pi(x')}{\pi(x)}\right)
= \min\!\left(1,\ e^{\ln\pi(x') - \ln\pi(x)}\right),
$$

and the demonstration implements exactly this with
$q = \mathcal{N}(x,\ \text{step}^2 I)$. Working in log density throughout is
mandatory in practice: $\pi$ itself underflows for even moderately sized problems.

## 4. Tuning the proposal, measured

The proposal scale is the only user-facing parameter of a random walk. The
demonstration runs a SYNTHETIC target

$$
\pi = \mathcal{N}\!\left(\begin{bmatrix}1\\-2\end{bmatrix},
\begin{bmatrix}1.00&0.90\\0.90&1.00\end{bmatrix}\right),
$$

i.e. unit marginal standard deviations with correlation $+0.90$ and covariance
eigenvalues $0.1$ and $1.9$, for $40\,000$ steps with $2\,000$ discarded, and
reports the acceptance rate, the autocorrelation time of the slow direction and
the effective sample size:

| step | acceptance | $\tau$ (slow direction) | ESS of 38 000 draws |
|---|---|---|---|
| 0.10 | 0.893 | 559.3 | 68 |
| 0.30 | 0.700 | 134.5 | 282 |
| 0.70 | 0.431 | 37.9 | 1003 |
| **1.50** | **0.199** | **21.9** | **1736** |
| 3.00 | 0.072 | 30.6 | 1242 |
| 6.00 | 0.024 | 75.0 | 506 |

Two facts are visible. First, **the best ESS occurs at an acceptance rate near
$0.2$**, not near $1$. Second, the curve is smooth in both directions: too small a
step accepts almost always and moves nowhere; too large a step is rejected almost
always. The classical asymptotic result for a random walk in high dimension puts
the optimum near $0.234$; in one dimension it is nearer $0.44$; the measured
optimum here, in two strongly correlated dimensions, is $0.199$. The correct
reading is not that $0.2$ is a magic number but that **the optimum is
target-specific, so it must be found by measurement**.

### 4.1 Measuring the effective sample size

The autocorrelation function $\rho_k$ of the chain is estimated here with an FFT
and truncated at the first non-positive lag (the initial positive sequence rule).
For the step $1.50$ chain the demonstration reports

| lag | autocorrelation |
|---|---|
| 0 | $+1.0000$ |
| 1 | $+0.9113$ |
| 2 | $+0.8314$ |
| 5 | $+0.6313$ |
| 10 | $+0.4068$ |
| 20 | $+0.1793$ |
| 50 | $-0.0137$ |

and the integrated autocorrelation time is

$$
\tau = 1 + 2\sum_{k\ge 1}\rho_k \approx 21.9,
\qquad
\text{ESS} = \frac{n}{\tau} = \frac{38\,000}{21.9} = 1736 .
$$

**Only $4.6\%$ of the draws carry independent information.** Any statement about
the posterior that does not mention this number is unverifiable. The most extreme
illustration in the demonstration is the step $0.05$ chain: acceptance $0.947$,
$\tau = 2551.7$, ESS $= 16$ from $40\,000$ draws. A chain can look perfectly
healthy by acceptance rate and contain almost no information.

## 5. Convergence diagnostics

The chain converges to the target in the limit; in finite time it does not, and no
diagnostic can prove that it has. What diagnostics *can* do is detect failures.
The standard one compares several chains started from dispersed points.

For $m$ chains of length $n$, with within-chain variances $W$ and between-chain
variance $B$,

$$
W = \frac{1}{m}\sum_{j=1}^{m} s_j^2,
\qquad
B = n\,\operatorname{Var}(\bar x_j),
\qquad
\widehat{\operatorname{Var}} = \frac{n-1}{n}W + \frac{B}{n},
\qquad
\hat R = \sqrt{\frac{\widehat{\operatorname{Var}}}{W}} .
$$

Splitting each chain in half before computing $\hat R$ — the **split** $\hat R$
used here — catches a chain that is still drifting, because the two halves of a
drifting chain disagree. The demonstration runs four chains (split into eight
half-chains of $3500$ draws) at the chosen step, and reports

$$
\hat R = (1.0003,\ 1.0004), \qquad
\bar m = (1.0684,\ -1.9451), \qquad
\hat s = (0.9788,\ 0.9825),
$$

against exact values of $(1,-2)$ for the mean and $(1,1)$ for the standard
deviation. The agreement is within Monte Carlo error at $\text{ESS}\approx 1700$.

It is essential to be honest about what this buys:

- $\hat R \approx 1$ is **not** convergence. All chains can sit in the same wrong
  region, and $\hat R$ will be $1$.
- **Multimodal targets are invisible to $\hat R$.** If no chain ever visits a mode,
  nothing in the sample reveals its existence. Over-dispersed starting points and
  a target informed by physics are the practical defences.
- $\hat R$ near $1$ with a **tiny** ESS is still a poor result. Report both.
- Diagnostic thresholds (for instance $\hat R < 1.01$ and $\text{ESS} > 400$ for
  all reported quantities) should be stated in advance, not chosen after seeing
  the answer.

### 5.1 Where the draws come from matters

The four chains in the demonstration are started from dispersed points
$(0,0),(0.1,-0.1),(0.2,-0.2),(0.3,-0.3)$. Starting all chains at the same point
destroys the between-chain information that $\hat R$ uses, and makes the
diagnostic blind by construction. This is a common and invisible error.

## 6. Gibbs sampling

For a target with a natural partition $x = (u,v)$, the Gibbs sampler alternates

$$
u \sim \pi(u\mid v), \qquad v \sim \pi(v\mid u).
$$

*Why it is a Metropolis-Hastings special case.* Take the proposal
$q(u'\mid u,v) = \pi(u'\mid v)$, i.e. draw from the exact conditional. Then the
acceptance ratio is

$$
\frac{\pi(u',v)\,q(u\mid u',v)}{\pi(u,v)\,q(u'\mid u,v)}
= \frac{\pi(u'\mid v)\pi(v)\,\pi(u\mid v)}
{\pi(u\mid v)\pi(v)\,\pi(u'\mid v)} = 1,
$$

so every proposal is accepted. For the two-dimensional Gaussian the conditionals
are available in closed form: with correlation $\rho$ and unit variances,

$$
u\mid v \sim \mathcal{N}\!\left(\mu_u + \rho\,(v-\mu_v),\ 1-\rho^2\right),
$$

which is what the demonstration samples. The result is instructive:

| sampler | acceptance | $\tau$ | ESS of 18 000 draws |
|---|---|---|---|
| random-walk Metropolis, step 1.50 | 0.199 | 21.9 | 1736 of 38 000 |
| Gibbs | 1.000 | 9.1 | 1968 |

Gibbs has a smaller autocorrelation time **and** never rejects — but it requires
the conditional distributions to be samplable exactly. For a nonlinear forward
model, a robust likelihood, or a bounded prior that cuts across the parameter
blocking, they are not. That is why Metropolis-type samplers remain the default,
and why the next lesson turns to a sampler that uses gradient information instead
of guessing a proposal scale.

## 7. Worked example: from target to usable number

Assemble the chain of reasoning on the demonstration's target.

1. **Define the target.** $\ln\pi(m) = -\tfrac12 (m-\mu)^{\top}C^{-1}(m-\mu)$ with
   $\mu = (1,-2)$ and $C$ as in Section 4. The normalising constant is not needed.
2. **Propose** symmetrically, $m' = m + \text{step}\cdot z$,
   $z \sim \mathcal{N}(0,I)$.
3. **Accept** with probability $\min(1, \exp[\ln\pi(m') - \ln\pi(m)])$.
4. **Tune** the step by maximising the ESS, not the acceptance rate: choose
   $1.50$ from the measured table.
5. **Burn in** and discard: the demonstration discards the first $2000$ of
   $40\,000$ and states the number.
6. **Diagnose**: $\tau \approx 21.9$, $\text{ESS} \approx 1736$ on the slow
   direction, split $\hat R = (1.0003,1.0004)$ over four chains.
7. **Report**: posterior mean $(1.0684,-1.9451)$ and standard deviation
   $(0.9788,0.9825)$ from $38\,000$ draws with ESS $\approx 1736$; exact values
   $(1,-2)$ and $(1,1)$.

The measured mean differs from the exact mean by $0.068$ in the first component.
With $\text{ESS}\approx 1736$ the standard error of that mean is
$1/\sqrt{1736} = 0.024$; the discrepancy is $2.8$ standard errors, which is a
plausible draw and not a defect. But the point of reporting ESS is that this
*check* is possible: without it, a discrepancy of $0.068$ is uninterpretable.

## 8. Regime of validity

1. **Irreducibility and aperiodicity.** Any sampler with a hard rejection
   structure can be reducible in a symmetry-broken problem; a chain that never
   changes state is the symptom.
2. **Adaptation.** Tuning the step during the run breaks stationarity; adapt in
   warm-up only, then freeze, as the next lesson explains for mass matrices.
3. **Correlated parameters.** A random walk in a ridge mixes through the slow
   eigendirection, and its autocorrelation time scales as the condition number of
   the target covariance. The measured $\tau = 21.9$ against eigenvalues $0.1$ and
   $1.9$ is a mild case; in a real inversion the ratio is often $10^3$ or worse.
4. **Dimensionality.** A random walk diffuses; its efficiency degrades as the
   dimension grows, and the acceptance optimum drifts toward $0.234$. Beyond a few
   tens of parameters, gradient-based sampling is the practical route.
5. **Deterministic likelihood evaluation.** Every acceptance test costs a full
   forward solve. Chapter-level cost accounting — number of forward solves per
   effective sample — belongs in the report.
6. **The diagnostics are not a proof.** They can only detect failure. The only
   genuine check is an independent route to the same answer, as used in lessons
   [07](07-evidence-and-model-selection.md) and [08](08-trans-dimensional.md).

## 9. Demonstration and exercises

[`code/mcmc_demo.py`](./code/mcmc_demo.py) implements the random-walk sampler, the
autocorrelation estimator, the split $\hat R$ calculation and a Gibbs sampler on
the same target, prints all tables above with units, and exits $0$ in about a
second. Exercises and solutions:
[`exercises/04-mcmc-exercises.md`](./exercises/04-mcmc-exercises.md),
[`exercises/04-mcmc-solutions.md`](./exercises/04-mcmc-solutions.md).

## Mastery checkpoint

**(a)** Write the Metropolis-Hastings acceptance ratio for a non-symmetric
proposal and explain why the unknown evidence $p(d)$ never appears.
**(b)** A chain of $50\,000$ draws has $\tau = 250$. State the ESS and the
standard error of the posterior mean for a parameter with posterior standard
deviation $2$.
**(c)** Two chains started from the same point both report $\hat R = 1.000$.
Explain why this is uninformative and name a starting strategy that fixes it.
**(d)** For a Gaussian target with correlation $\rho = 0.99$, state whether a
random walk or a Gibbs sampler is preferable and why.

## Common pitfalls

1. **Tuning by acceptance rate.** The measured optimum in Section 4 is at
   $0.199$; a chain at $0.9$ acceptance had an ESS $25$ times smaller.
2. **Reporting the chain length as the sample size.** The sample size is the ESS.
3. **Claiming convergence from $\hat R$ alone.** It cannot see an unvisited mode.
4. **Starting all chains at the same place.** It disables the diagnostic.
5. **Adapting the proposal during production.** It breaks the detailed balance
   that the method relies on.
6. **Ignoring autocorrelation when quoting an interval.** A credible interval
   computed from correlated draws has a Monte Carlo error that grows with $\tau$.
7. **Using a thinning interval as a substitute for ESS.** Thinning reduces
   storage, not the number of forward solves.

## Further reading

- **Metropolis, N., Rosenbluth, A. W., Rosenbluth, M. N., Teller, A. H., &
  Teller, E. (1953). Equation of state calculations by fast computing machines.
  *Journal of Chemical Physics*, 21(6), 1087–1092.** Level: research. The
  original algorithm.
- **Hastings, W. K. (1970). Monte Carlo sampling methods using Markov chains and
  their applications. *Biometrika*, 57(1), 97–109.** Level: research. The
  non-symmetric generalisation derived in Section 3.
- **Gelfand, A. E., & Smith, A. F. M. (1990). Sampling-based approaches to
  calculating marginal densities. *Journal of the American Statistical
  Association*, 85(410), 398–409.** Level: research. Gibbs sampling as used in
  Section 6.
- **Robert, C. P., & Casella, G. (2004). *Monte Carlo Statistical Methods*
  (2nd ed.). Springer.** Level: research. Convergence theory and the asymptotically
  optimal scaling of random-walk Metropolis.
- **Vehtari, A., Gelman, A., Simpson, D., Carpenter, B., & Bürkner, P.-C. (2021).
  Rank-normalization, folding, and localization: An improved $\hat R$ for assessing
  convergence of MCMC. *Bayesian Analysis*, 16(2), 667–718.** Level: research. Why
  the classical $\hat R$ fails on heavy-tailed and multimodal targets, and what to
  use instead.

## Related modules

- [01 Bayes' Theorem as an Inverse-Problem Formulation](01-bayes-inverse-formulation.md).
- [05 Hamiltonian Monte Carlo and Modern Samplers](05-hmc-and-modern-samplers.md) —
  the gradient-based answer to the tuning problem measured here.
- [06 Posterior Summaries](06-posterior-summary.md) — turning draws into intervals.
- [07 Bayesian Evidence and Model Selection](07-evidence-and-model-selection.md).
- [18-04-01 Local Linearisation, Jacobians and Iteration](../04-nonlinear-inversion/01-local-linearization.md)
  — where the gradient used by the next lesson comes from.
- [18-04-07 Convergence Diagnosis and Local-Minimum Traps](../04-nonlinear-inversion/07-convergence-and-local-minima.md)
  — the deterministic analogue of Section 5.
- [18-06-02 Monte Carlo Propagation and Its Convergence](../06-uncertainty-quantification/02-monte-carlo-uq.md)
  — the same convergence arithmetic for independent samples.
