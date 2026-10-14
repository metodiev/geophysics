---
id: 18-05-08
title: "Trans-Dimensional and Reversible-Jump MCMC"
level: research
prereqs: ["18-05-07", "18-05-04"]
tags: [inverse-problems, bayesian, uncertainty-quantification, reversible-jump, trans-dimensional, model-selection]
---

# Trans-Dimensional and Reversible-Jump MCMC

All models and data in this module are **SYNTHETIC**. The polynomial family, the
prior width and the noise level below are chosen teaching values; the trans-D
chain is deliberately kept small so that it mixes in under a second. Every number
quoted is printed by
[`code/trans_dimensional_demo.py`](./code/trans_dimensional_demo.py).

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** why a posterior over models of different dimension is not a
   posterior over a fixed parameter vector, and what the trans-dimensional
   formulation changes.
2. **Derive** the reversible-jump acceptance ratio, including the
   dimension-matching map, its Jacobian, the proposal-probability ratio, and the
   prior density of the created or deleted parameter.
3. **Implement** birth, death and within-model moves, and **show** by measurement
   that dropping any one of the ratio's factors biases the posterior.
4. **Verify** a reversible-jump implementation against an independent route to the
   same model probabilities.
5. **Diagnose** a trans-D chain using acceptance rates per move, the
   autocorrelation time of the model index, effective sample size and split
   $\hat R$.
6. **Quantify** the Monte Carlo error of a posterior model probability, including
   the case of a rarely visited model.
7. **State** when a trans-D formulation is preferable to the two-stage route of
   computing evidences for each model separately.

## Prerequisites

- [18-05-07 Bayesian Evidence and Model Selection](07-evidence-and-model-selection.md)
  — the model probabilities that a trans-D chain estimates without ever computing
  an integral.
- [18-05-04 Markov Chain Monte Carlo: Metropolis-Hastings and Gibbs](04-mcmc.md)
  — detailed balance, acceptance ratios, $\tau$, ESS and $\hat R$.
- [18-04-04 Global Search: Monte Carlo, Simulated Annealing, Genetic Algorithms](../04-nonlinear-inversion/04-global-search.md)
  — the search-side view of a variable-dimension model space.

## 1. Intuition: the model is part of the unknown

In lesson [07](07-evidence-and-model-selection.md) the number of layers, terms or
basis functions was fixed, and each model was compared by computing an integral.
That works when the candidate list is short and the integration is cheap. In a
real inversion the number of unknowns is itself unknown: how many layers is the
velocity profile, how many sources are in the field, how many discontinuities
does the receiver function require? Enumerating all of them and integrating each
is possible only for small families.

The trans-dimensional formulation makes the model index $k$ one of the unknowns.
The state of the chain is $(k, c_k)$ — a model order and the parameters that order
needs — and the target is

$$
p(k, c_k \mid d) \propto p(d \mid k,c_k)\,p(c_k\mid k)\,p(k).
$$

A chain on this space reports $p(k\mid d)$ directly, as the fraction of iterations
spent in each order, and it does so *without* computing any evidence integral.
That is the attraction. The complication is that the chain must move between
spaces of different dimension, and a Metropolis proposal cannot do that without
being told how to match the dimensions. Reversible-jump MCMC is the construction
that makes such moves satisfy detailed balance.

## 2. Dimension matching

Consider a move from order $k$ to order $k+1$. The current coefficient vector
$c$ has $k+1$ entries; the target vector $c'$ has $k+2$. Something must supply the
extra number. The device is a **dimension-matching map**: generate an auxiliary
variable $u$ with density $q(u)$ and set $(c', u) = g(c,u)$ where $g$ is a
bijection between the two augmented spaces. Then the acceptance ratio carries the
Jacobian of $g$:

$$
\alpha = \min\!\left(1,\
\frac{p(k+1,c')\,q'_{\text{reverse}}(u')}{p(k,c)\,q_{\text{forward}}(u)}
\,\Bigl\lvert\frac{\partial g}{\partial(c,u)}\Bigr\rvert\right).
$$

Here $q'_{\text{reverse}}$ is the density of the reverse move. Every factor is
present for a reason, and dropping any one of them is the commonest way to build
a chain that runs, looks plausible and reports the wrong probabilities.

For the polynomial family used throughout this module the construction is the
simplest possible one: the coefficient vector is *extended*, $c' = (c, u)$, with
$u$ drawn from a proposal density $q(u)$ chosen by the analyst. The map has a unit
Jacobian, so no Jacobian factor appears, but the proposal density and the prior
density of the new coefficient do not cancel unless $q$ *is* the prior.

## 3. The acceptance ratios used here

The demonstration uses birth, death and within-model moves with the proposal
probabilities

$$
(\pi_{\text{move}},\pi_{\text{birth}},\pi_{\text{death}}) =
\begin{cases}
(0.5,\,0.5,\,0.0) & k = 0\\
(0.5,\,0.25,\,0.25) & 0 < k < K\\
(0.5,\,0.0,\,0.5) & k = K,
\end{cases}
$$

so the boundary orders have only one direction available.

**Birth**, $k \to k+1$, drawing $u \sim \mathcal{N}(0,s^2)$ and setting
$c' = (c,u)$:

$$
\ln\alpha_{\text{birth}} =
\ln\frac{\mathcal{L}(k+1,c')}{\mathcal{L}(k,c)}
+ \ln\frac{p(c'\mid k+1)}{p(c\mid k)}
+ \ln\frac{\pi_{\text{death}}(k+1)}{\pi_{\text{birth}}(k)}
- \ln q(u).
$$

The second term is the prior density of the created coefficient,
$\mathcal{N}(u;0,\tau^2)$. It **cancels** against $q(u)$ only if
$s = \tau$. The demonstration deliberately uses $s = 0.3$ while $\tau = 1.0$,
so the two do not cancel and the ratio
$\mathcal{N}(u;0,\tau^2)/\mathcal{N}(u;0,s^2)$ is what keeps the chain correct.
This is worth stressing because proposing from a tighter-than-prior distribution
is the standard way to make births acceptable; the correction is the price.

**Death**, $k \to k-1$, deleting the last coefficient $u = c_k$:

$$
\ln\alpha_{\text{death}} =
\ln\frac{\mathcal{L}(k-1,c'')}{\mathcal{L}(k,c)}
+ \ln\frac{p(c''\mid k-1)}{p(c\mid k)}
+ \ln\frac{\pi_{\text{birth}}(k-1)}{\pi_{\text{death}}(k)}
+ \ln q(u).
$$

Writing the prior ratio explicitly,
$p(c''\mid k-1)/p(c\mid k) = 1/\mathcal{N}(u;0,\tau^2)$, and the last term is the
reverse birth proposal density $\mathcal{N}(u;0,s^2)$ evaluated at the coefficient
being deleted. The built-in implementation computes the prior ratio as
$\ln p(c'') - \ln p(c)$ and then multiplies by $q(u)$; the two are algebraically
identical, and the fact that both forms appear in the literature is a reliable
source of sign errors.

### 3.1 A deliberately honest note on debugging

The demonstration's first working version had the death ratio with the two normal
densities exchanged. The chain ran, produced a posterior over $k$, and reported
$P(k) = (0.057, 0.457, 0.486)$ against an analytic
$(0.002, 0.357, 0.641)$ — a discrepancy in the rare state of a factor of $25$,
far outside the Monte Carlo error. Nothing in the $\hat R$ diagnostic flagged it:
$\hat R$ was $1.001$. Only the independent route in Section 6 exposed it. This is
the single most useful thing to know about reversible-jump code: **it fails
silently**, and a second route to the same probabilities is not optional.

## 4. Worked example: the model probabilities

The SYNTHETIC data are $12$ points on $x\in[-1,1]$ from $y = 0.5+x$ with
$\sigma = 0.5$; the family is polynomials of orders $k = 0,1,2$ with
$\mathcal{N}(0,1^2)$ coefficients and a uniform prior over the three orders. The
exact evidences from lesson [07](07-evidence-and-model-selection.md) give

$$
\ln p(d\mid k) = (-20.4768,\ -15.3904,\ -14.8061)
\;\Longrightarrow\;
P(k\mid d) = (0.0022,\ 0.3571,\ 0.6406).
$$

The reversible-jump chain ($60\,000$ iterations, $5\,000$ discarded, started at
$k = 0$) reports

| $k$ | iterations spent there | measured $P(k)$ | analytic $P(k)$ | difference |
|---|---|---|---|---|
| 0 | 184 | 0.0033 | 0.0022 | $+0.0011$ |
| 1 | 19 050 | 0.3464 | 0.3571 | $-0.0108$ |
| 2 | 35 766 | 0.6503 | 0.6406 | $+0.0096$ |

**Monte Carlo error for a rarely visited state.** The naive binomial standard
error for $P(0)$ from $55\,000$ correlated draws is
$\sqrt{0.0033\times0.9967/55\,000} = 2.4\times10^{-4}$, which is far too small
because the draws are not independent. The model index changes only when a birth
or death is accepted: $3112$ accepted births and $3111$ accepted deaths, i.e.
$6223$ transitions in $55\,000$ retained iterations. Using that as the effective
sample size for the occupancy gives
$\sqrt{0.0033\times0.9967/6223} = 7.3\times10^{-4}$, so the observed difference of
$0.0011$ is about $1.5$ standard errors — a plausible draw. **A rare model's
probability is limited by the number of transitions into it, which is why the
acceptance rate for births and deaths is a first-class diagnostic.**

## 5. Mixing diagnostics for a trans-dimensional chain

The demonstration reports, for the same run:

$$
\text{move: } 17\,094/29\,800 = 0.574, \quad
\text{birth: } 3112/5343 = 0.582, \quad
\text{death: } 3111/24\,763 = 0.126 .
$$

The asymmetry is the interesting part. Births were proposed rarely (only from
$k<2$ states) and accepted often ($0.582$); deaths were proposed often (from any
$k>0$) and accepted rarely ($0.126$), because the chain spends most of its time at
$k=2$, where a death proposal must delete a coefficient that the likelihood
actually needs. A chain that spends all its time in one model because it cannot
leave is the characteristic trans-D failure, and it shows up here as a low death
acceptance.

The model index is itself a chain:

$$
\tau_{\text{index}} = 53.4, \qquad
\text{ESS} = \frac{55\,000}{53.4} = 1030 \ (1.87\%).
$$

Over four chains of $10\,000$ retained draws started in different orders, the
split diagnostic gives $\hat R = 1.0063$, comfortably below the conventional
threshold of $1.01$, with pooled
$P(k) = (0.0016,\ 0.3560,\ 0.6424)$, close to the analytic values. As lesson
[04](04-mcmc.md) insists, $\hat R$ here is a weak instrument: a discrete index can
sit in one model for thousands of iterations in every chain simultaneously, giving
a low $\hat R$ and a very wrong $P(k)$. It must be read together with the
per-move acceptance rates and the ESS of the index.

## 6. Verification against an independent route

The model probabilities can be obtained without any MCMC, by quadrature on the
coefficient space:

| $k$ | grid points | quadrature $p(d\mid k)$ | analytic $p(d\mid k)$ | relative error |
|---|---|---|---|---|
| 0 | 121 | $1.279535\times10^{-9}$ | $1.279535\times10^{-9}$ | $6.4\times10^{-15}$ |
| 1 | 14 641 | $2.070210\times10^{-7}$ | $2.070210\times10^{-7}$ | $6.7\times10^{-15}$ |
| 2 | 226 981 | $3.713519\times10^{-7}$ | $3.713519\times10^{-7}$ | $1.4\times10^{-10}$ |

giving $P(k)_{\text{quad}} = (0.0022,\ 0.3571,\ 0.6406)$, which agrees with the
analytic values to the grid error and with the trans-D chain to the Monte Carlo
error. Three independent routes, one answer.

This triple agreement is the check that the reversible-jump acceptance ratios are
implemented correctly. It costs nothing extra here because the family is tiny; in
a real problem the independent route is usually a synthetic recovery test — inject
a known model order, invert, and confirm that the posterior concentrates on it —
which is the workflow of
[18-08-02](../08-practical-inversion-workflow/02-synthetic-testing.md).

## 7. Trans-D or two-stage evidence?

Both routes report $p(k\mid d)$ for a fixed candidate family. The choice is
practical.

| | trans-D chain | compute evidence per model |
|---|---|---|
| Cost | one chain | one inversion per model |
| Handles many models | yes, cost is roughly independent of the number | cost grows with the family |
| Reports parameter posteriors | per model, as a by-product | separately |
| Diagnoses | mixing between models is the difficulty | the difficulty is the integral |
| Failure mode | silent bias from a wrong acceptance ratio | a badly approximated integral |

The most common practical recommendation follows from the failure modes: if the
candidate family is small and each integral is cheap, use lesson
[07](07-evidence-and-model-selection.md)'s route and verify with quadrature. Use
trans-D when the family is genuinely large or when the number of unknowns is
unbounded *a priori* — the classic case being a 1-D profile represented as an
unknown number of layers, where the trans-D posterior over the number of layers is
itself the deliverable. In geophysics this is how layer-count posteriors,
source-count posteriors in microseismic monitoring, and the number of
discontinuities in a receiver-function inversion are reported.

## 8. Assumptions and regime of validity

1. **The Jacobian must be computed, not assumed to be one.** Here the
   dimension-matching map is a vector extension and the block is the identity;
   for a map such as $\theta' = \log\theta$ the Jacobian is $1/\theta'$ and matters.
2. **The prior on the extra parameter must be proper.** An improper prior makes
   the birth acceptance ratio undefined; trans-D requires proper, normalisable
   priors on every coefficient.
3. **Model priors must be explicit.** With a uniform prior over $k$, an
   unbounded family has infinitely many models and no normalisation; trans-D
   always uses a truncated family $0\le k\le K$, and $K$ must be stated.
4. **Birth and death must be exact reverses.** Any asymmetry between them —
   a different coefficient ordering, a different distribution — breaks detailed
   balance and biases $P(k)$.
5. **Mixing is the bottleneck.** Report per-move acceptance rates and the ESS of
   the model index. A high within-model ESS with a low index ESS still gives a
   well-determined set of parameters *conditional on a poorly determined model*.
6. **Extrapolation beyond the family is impossible.** If the truth lies outside
   the candidate orders, the posterior over $k$ piles up at the boundary $K$; that
   pile-up is the diagnostic, and it means the family, not the sampler, is wrong.
7. **The likelihood must be comparable across models.** If the data are summarised
   differently for different orders — different numbers of samples, different
   bands — the comparison is meaningless. This is the same trap as a hand-built
   Bayes factor.

## 9. Demonstration and exercises

[`code/trans_dimensional_demo.py`](./code/trans_dimensional_demo.py) implements
birth, death and within-model moves with the acceptance ratios above, prints the
per-move acceptance rates, the occupancy table, the index autocorrelation time,
split $\hat R$ over four chains, and the three-way verification against analytics
and quadrature. It exits $0$ in under a second. Exercises and solutions:
[`exercises/08-trans-dimensional-exercises.md`](./exercises/08-trans-dimensional-exercises.md),
[`exercises/08-trans-dimensional-solutions.md`](./exercises/08-trans-dimensional-solutions.md).

## Mastery checkpoint

**(a)** Write the birth acceptance ratio for a proposal $u\sim\mathcal{N}(0,s^2)$
and state what happens to it when $s = \tau$.
**(b)** A trans-D run spends $200$ of $100\,000$ iterations in $k=0$, with $9000$
accepted model transitions in total. Estimate $P(0)$ and give an honest standard
error.
**(c)** The posterior over $k$ piles up on the largest order in the family. State
the two interpretations and how to distinguish them.
**(d)** Explain in two sentences why a Bayes factor computed with an improper
prior on a model-specific parameter is meaningless, and how trans-D avoids the
problem.

## Common pitfalls

1. **Dropping the proposal-density ratio when $s \neq \tau$.** It biases the
   posterior, silently, as the debugging note in Section 3.1 records.
2. **Exchanging the prior and proposal densities in the death ratio.** The
   commonest sign error in reversible-jump code.
3. **Reading $\hat R$ alone.** It was $1.001$ in the buggy version.
4. **Ignoring per-move acceptance rates.** A death rate of $0.126$ means the chain
   is spending its time in the largest model whether or not that is justified.
5. **Using an improper prior on the extra parameter.** The ratio is undefined.
6. **Forgetting that the family is truncated.** The upper bound $K$ is a model
   choice, and boundary pile-up is a statement about the family.
7. **Comparing models through different data summaries.** The evidence is then not
   comparable.

## Further reading

- **Green, P. J. (1995). Reversible jump Markov chain Monte Carlo computation and
  Bayesian model determination. *Biometrika*, 82(4), 711–732.** Level: research.
  The original construction, including the Jacobian of the dimension-matching map.
- **Sambridge, M., Gallagher, K., Jackson, A., & Rickwood, P. (2006).
  Trans-dimensional inverse problems, model comparison and the evidence.
  *Geophysical Journal International*, 167(2), 528–542.** Level: research. The
  trans-D formulation in a geophysical idiom, with the evidence as a by-product.
- **Bodin, T., & Sambridge, M. (2009). Seismic tomography with the reversible jump
  algorithm. *Geophysical Journal International*, 178(3), 1411–1436.** Level:
  research. A large-scale trans-D inversion, useful for seeing where the mixing
  difficulty actually lies.
- **Gelman, A., Carlin, J. B., Stern, H. S., Dunson, D. B., Vehtari, A., &
  Rubin, D. B. (2013). *Bayesian Data Analysis* (3rd ed.). CRC Press.**
  Level: research. Chapter-level treatment of model determination and its
  diagnostics.

## Related modules

- [07 Bayesian Evidence and Model Selection](07-evidence-and-model-selection.md) —
  the analytic route this lesson reproduces without integration.
- [04 Markov Chain Monte Carlo](04-mcmc.md) and
  [05 Hamiltonian Monte Carlo and Modern Samplers](05-hmc-and-modern-samplers.md)
  — the within-model machinery.
- [18-08-02 Synthetic Testing, Checkerboards and Recovery Tests](../08-practical-inversion-workflow/02-synthetic-testing.md)
  — the verification route when no analytic evidence exists.
- [18-08-03 Assessing a Model: Resolution, Artifacts, Alternatives](../08-practical-inversion-workflow/03-model-assessment.md)
  — what to do with a posterior that piles up at a model boundary.
- [18-06-06 Decision-Making Under Uncertainty and Value of Information](../06-uncertainty-quantification/06-decision-under-uncertainty.md)
  — turning $P(k\mid d)$ into a decision.
