---
id: 25-05-04
title: "Project: Trans-Dimensional Bayesian Inversion"
level: doctoral
prereqs: ["18-05-01", "18-05-08", "21-03-04", "25-04-01"]
estimated_minutes: 260
tags: [projects, bayesian, rjmcmc, model-selection, trans-dimensional, doctoral]
---

# Project: Trans-Dimensional Bayesian Inversion

## Learning objectives

By the end of this project you will be able to:

1. **Write** the joint posterior over a model space of *variable dimension*, with an
   explicit prior on the number of parameters.
2. **Derive** the reversible-jump acceptance ratio for a birth/death move, including
   the proposal densities, the prior ratio and the Jacobian.
3. **Compute** the marginal likelihood of a linear-Gaussian model analytically and
   **use** it to obtain an exact reference posterior for a small model space.
4. **Show** that the posterior over the layer count is a model-selection result, and
   **decompose** it into an Occam factor and a prior factor.
5. **Diagnose** poor mixing in a trans-dimensional sampler from acceptance rates and
   from the disagreement between chains, and **distinguish** a bias from Monte Carlo
   variance.
6. **Report** uncertainty that includes the structural component, and **state** what
   portion of it comes from the layer count rather than from the values.
7. **Design** a validation protocol for a trans-dimensional inversion of a problem
   whose exact answer is unknown.

All data in this project are **SYNTHETIC**: a three-layer velocity profile measured
by 20 samples in [`code/transdimensional_demo.py`](./code/transdimensional_demo.py).
The demonstration also computes the *exact* posterior by enumerating every model with
up to five layers and integrating the layer values analytically, which is only
possible because the model space is small — and that is the point of the project.

## Prerequisites

- [18-05-01 The Bayesian Formulation of Inverse Problems](../../18-inverse-problems/05-bayesian-inversion/01-bayes-inverse-formulation.md) —
  the posterior and the evidence.
- [21-03-04 Markov Chain Monte Carlo in Practice](../../21-statistics-bayesian-ml/03-bayesian-inference/04-mcmc-practice.md) —
  acceptance ratios, burn-in and convergence diagnosis.
- [18-04-01 Local Linearisation, Jacobians and Iteration](../../18-inverse-problems/04-nonlinear-inversion/01-local-linearization.md) —
  the fixed-dimension inversion this project generalises.
- [25-04-01 Project: Finite-Difference Wave Propagation](../04-graduate-projects/01-fd-wave-propagation-project.md) —
  the forward-modelling skills the project assumes.

## 1. The question

*How many layers does the data support, and what does the answer do to the
uncertainty of the profile?*

A fixed-parameterisation inversion answers "what are the values?" and silently
assumes the answer to "how many?". Trans-dimensional sampling treats the number of
layers as an unknown and returns its posterior. The demonstration, on a synthetic
three-layer profile with 20 noisy samples, gives

$$P(k=3) = 0.9318,\quad P(k=4) = 0.0675,\quad P(k=5) = 0.0007,$$

computed **exactly** by enumerating all 5036 models with up to five layers and
integrating the layer values analytically — out of $2^{19} = 524288$ possible
boundary sets. The posterior mean profile lies $0.046\ \mathrm{km\,s^{-1}}$ rms from
the truth, and the layer-count uncertainty contributes to its error bars: with the
layer count fixed at three the profile uncertainty would be understated.

## 2. The model space and the posterior

**Parameterisation.** $k$ layers on 20 cells, $k-1$ internal boundaries chosen from
the 19 possible positions, and $k$ layer values.

**Prior.** $k$ uniform on $\{1,\dots,K_{\max}=5\}$; given $k$, boundaries uniform over
the $\binom{19}{k-1}$ subsets; layer values i.i.d. $N(0, \sigma_m^2)$ with
$\sigma_m = 1.5\ \mathrm{km\,s^{-1}}$ — deliberately vague, allowing 2–9 km/s.

**Likelihood.** $\mathbf d = \mathbf G\mathbf m + \boldsymbol\epsilon$ with
$\boldsymbol\epsilon \sim N(0, \sigma_d^2\mathbf I)$, $\sigma_d = 0.15\
\mathrm{km\,s^{-1}}$, and $\mathbf G$ a Gaussian averaging kernel of one-cell
half-width, so that adjacent samples are correlated and the boundaries are not
individually identifiable from a single datum.

**Exact evidence.** For a fixed boundary set $b$, conditioning on $\mathbf m$ gives

$$\mathbf d \sim N\bigl(\mathbf 0,\ \mathbf G\,\mathbf S_b\,\mathbf G^{\mathsf T}
+ \sigma_d^2\mathbf I\bigr),\qquad
\mathbf S_b = \sigma_m^2\,\mathbf P_b\mathbf P_b^{\mathsf T},$$

where $\mathbf P_b$ assigns each cell to its layer. The evidence is then a Gaussian
density evaluated at $\mathbf d$, with the layer values integrated out. Enumerating
all 5036 subsets took $0.15$ s, and the posterior is the normalised product of
evidence and prior.

| $k$ | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| $P(k)$ exact | $0.0000$ | $0.0000$ | $0.9318$ | $0.0675$ | $0.0007$ |
| $P(k)$ rjMCMC | $0.0000$ | $0.0000$ | $0.9834$ | $0.0165$ | $0.0001$ |

The most probable single model is $k=3$ with boundaries at cells 6 and 13 — the truth
— with $P = 0.9306$.

## 3. The reversible-jump acceptance ratio

For a birth that splits one layer with value $v$ into two with values $v-u$ and
$v+u$, $u \sim N(0,\sigma_u^2)$, at an empty boundary position chosen uniformly:

$$\alpha_\text{birth} = \min\Bigl(1,\ \frac{L'}{L}\,
\underbrace{\frac{N(v-u)\,N(v+u)}{N(v)}}_{\text{value prior ratio}}\,
\underbrace{\frac{\binom{19}{k-1}}{\binom{19}{k}}}_{\text{boundary prior ratio}}\,
\underbrace{\frac{p_d(k+1)}{p_b(k)}}_{\text{move probabilities}}\,
\underbrace{\frac{N_e}{k}}_{\text{position choices}}\,
\frac{1}{q(u)}\,\underbrace{2}_{|J|}\Bigr),$$

with $N_e = 20-k$ the number of empty positions and the death move the exact inverse
(merge $v = (v_L+v_R)/2$, $|J| = 1/2$). Every factor has a mechanical interpretation:
the likelihood ratio, the change in parameter prior, the change in the prior on the
number of parameters and their positions, the asymmetry of the proposal, and the
Jacobian of the change of variables. A birth that adds a value drawn from the prior
instead of splitting an existing one is a valid alternative, but then the proposal
density of that value replaces the value-prior factor — and the acceptance rate
collapses, because a prior-drawn value almost never fits sharply peaked data.

**This is where the project's difficulty lives.** The demonstration's acceptance
rates are

| move | acceptance |
|---|---|
| value perturbation ($\sigma = 0.2$) | $0.354$ |
| boundary displacement ($\pm1$ cell) | $0.004$ |
| birth (split) | $0.007$ |
| death (merge) | $0.007$ |

The data are precise enough ($\sigma_d = 0.15$ against a 1.6 km/s velocity contrast)
that moving a boundary by one cell without re-optimising the values changes the
misfit enormously. The sampler therefore enters the four-layer models rarely, and
the consequence is visible in the table of §2: **P(k=4) is underestimated by a factor
of about three**, while the posterior *mean profile* is accurate
($0.017\ \mathrm{km\,s^{-1}}$ rms against the exact posterior mean; $0.036$ against
the truth). Three chains from three different starting models ($k=3$, $k=1$ and
$k=5$), all ending at the true boundaries, give total-variation distances from the
exact posterior of $0.0516$, $0.0489$ and $0.0506$ — **they agree with each other
and they are all biased in the same direction**, because they share the same
proposal. Agreement between chains is not evidence of correctness; a shared poor
proposal produces a shared bias.

## 4. The project specification

**Steps.**

1. Define the model space: what varies dimensionally (layer count, boundary
   positions, number of sources, polynomial order, …), and the prior on the number
   of parameters and on the positions.
2. Write the forward operator and the likelihood; state the noise level and its
   source.
3. Derive the reversible-jump acceptance ratios for every move type, with the
   Jacobians.
4. Build a small version of the problem whose evidence can be computed **exactly**
   (analytic marginal likelihood, enumerable model space) and obtain the reference
   posterior.
5. Run three or more chains from dispersed starting models; report the posterior on
   the model dimension, the posterior mean profile with its uncertainty, and all
   acceptance rates.
6. Compare the chains with the exact reference; quantity the bias, if any, and
   distinguish it from Monte Carlo error by repeating with a longer run.
7. Decompose the posterior odds for two model dimensions into a prior factor and an
   evidence (Occam) factor.
8. Propose and test at least one proposal improvement, and demonstrate the
   improvement **against the exact reference**.
9. Report the uncertainty with the structural component identified.

**Deliverable.** An exact reference posterior for a small model space, a
trans-dimensional sampler validated against it, the posterior over the model
dimension, and an explicit statement of the sampler's demonstrated accuracy.

**Success criterion.** The sampler is validated against an exactly known answer
before it is applied to anything else; the model-dimension posterior is reported with
its demonstrated bias; acceptance rates are given; the uncertainty is decomposed into
value and structural parts; and no claim is made from a run whose mixing has not been
demonstrated.

## 5. What the data support, quantitatively

The odds against an extra layer decompose cleanly. From the table of §2:

$$\frac{P(4)}{P(3)} = \frac{0.0675}{0.9318} = \frac{1}{13.8},\qquad
\text{prior factor} = \frac{\binom{19}{2}}{\binom{19}{3}} = \frac{171}{969}
= \frac{1}{5.7},$$

so the Bayes factor — the evidence ratio with the layer-count prior removed — is

$$\mathrm{BF}_{43} = \frac{1/13.8}{1/5.7} = 0.41,$$

i.e. the data alone disfavour four layers by a factor $2.4$, and the prior on the
number of boundaries does the rest. Both factors are the standard Occam argument, and
reporting only the total hides that a change of prior on $k$ would move the answer
substantially. This is why the project asks for the decomposition: **the layer count
is a prior-dependent quantity and the report must say so.**

## 6. Failure modes

1. **Applying a trans-dimensional sampler without a validated reference.** The
   demonstration's own sampler is biased at $k=4$ while its profile estimate is
   excellent; without the exact reference that bias would be invisible.
2. **Reading chain agreement as convergence.** Shared-proposal bias survives
   agreement, and the standard $\hat R$ diagnostic cannot detect it.
3. **Poorly chosen birth proposals.** Drawing a new value from the wide prior, or
   splitting with a $\sigma_u$ mismatched to the data precision, gives acceptance
   rates of $10^{-3}$ and a posterior that is effectively that of the starting model.
4. **Confusing the evidence with the best-fitting likelihood.** The posterior over
   $k$ is an integral over all values and boundaries, not a maximum-likelihood
   comparison.
5. **Reporting the posterior mean profile without the structural uncertainty**, which
   understates the error bars exactly where the layer count is uncertain.
6. **Omitting the acceptance rates and the number of trans-dimensional jumps.** They
   are as necessary in a Bayesian inversion report as a residual is in a least-squares
   one.
7. **A prior on $k$ that silently encodes the answer** (e.g. $K_{\max} = 3$ when the
   question is whether four layers are supported).

## 7. Rubric

| Criterion | Weight | Full marks |
|---|---|---|
| Model space and prior fully specified | 15% | dimension, positions and values, with the effect of each prior stated |
| Acceptance ratios derived | 20% | every factor and the Jacobian present for birth and death |
| Exact reference posterior | 20% | analytic evidence, enumerated space, reference table |
| Sampler validated against it | 20% | acceptance rates, chain comparison, bias quantified |
| Odds decomposition | 15% | prior factor and Bayes factor separately |
| Structural uncertainty reported | 10% | value and structural components identified |

## 8. The honest summary

The product is a posterior over a *model space* rather than over a single model, plus
an explicit measurement of how well that posterior was computed. Exactly, the data
give $P(k=3) = 0.9318$, $P(4) = 0.0675$ and $P(5) = 0.0007$, with a posterior mean
profile $0.046\ \mathrm{km\,s^{-1}}$ from the truth; the reversible-jump chains
reproduce the profile to $0.017\ \mathrm{km\,s^{-1}}$ but underestimate $P(4)$ by a
factor of about three at a trans-dimensional acceptance rate of $0.007$, and they do
so consistently from three different starting models. The transferable results are
that the number of parameters is an inferable quantity with its own prior dependence,
that a Bayesian inversion's credibility rests on validating the sampler against a
case with a known answer, and that agreement between chains is not that validation.

## Python demonstration

[`code/transdimensional_demo.py`](./code/transdimensional_demo.py) prints every number
above: the synthetic dataset and prior, the exact enumerated posterior, three
reversible-jump chains with their acceptance rates and total-variation distances, and
the profile comparison.

```bash
cd 25-projects-capstone/05-doctoral-projects/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python transdimensional_demo.py
```

Print-only, seeded with `np.random.default_rng(20261014)`, no network, no files, no
plots, exits 0, runs in about $2.5$ s.

## Exercises

Graded problems and worked solutions are in
[`exercises/04-bayesian-inversion-project-exercises.md`](./exercises/04-bayesian-inversion-project-exercises.md)
and
[`exercises/04-bayesian-inversion-project-solutions.md`](./exercises/04-bayesian-inversion-project-solutions.md).
The ★★★ item asks you to design and justify a validation protocol for a
trans-dimensional inversion whose exact answer is unknown.

## Mastery checkpoint

Without notes:

1. Write the joint posterior over a variable-dimension model space.
2. Write the birth acceptance ratio and name each factor.
3. State why a prior-drawn new value gives an unusable acceptance rate.
4. Compute the Bayes factor from the posterior odds and the prior odds.
5. State two diagnostics that a shared-proposal bias defeats.

## Common pitfalls

1. Treating the layer count as a hyperparameter to be tuned rather than inferred.
2. Judging a trans-dimensional run by its profile alone.
3. Ignoring the Jacobian of the split/merge transformation.
4. Comparing $\chi^2$ instead of evidence when the dimension differs.
5. Reporting a posterior mean that silently averages over a poorly sampled model
   space.

## Where this is used

Trans-dimensional sampling is the standard tool for problems whose complexity is
itself unknown: the number of layers in a 1-D Earth model, the number of
discontinuities in a receiver-function inversion
([25-04-06](../04-graduate-projects/06-receiver-function-project.md)), the number of
sources in a seismicity model, the number of basis functions in a gravity or
magnetotelluric inversion ([25-04-02](../04-graduate-projects/02-mt-1d-2d-inversion.md)).
The same posterior-over-model-space logic underlies the model-comparison decisions
made by hand in [25-05-03](./03-geodynamic-model-data.md), and the validation
protocol it demands is the same discipline that
[25-05-05](./05-reproduce-published-result.md) applies to a published result.

## Related lessons

- [18-05-08 Trans-Dimensional and Reversible-Jump MCMC](../../18-inverse-problems/05-bayesian-inversion/08-trans-dimensional.md) —
  the derivation in full generality.
- [21-03-04 Markov Chain Monte Carlo in Practice](../../21-statistics-bayesian-ml/03-bayesian-inference/04-mcmc-practice.md) —
  diagnostics, autocorrelation and effective sample size.
- [18-06-02 Monte Carlo Uncertainty Propagation](../../18-inverse-problems/06-uncertainty-quantification/02-monte-carlo-uq.md) —
  propagating a sampled posterior into a decision.
- [25-05-03 Project: Geodynamic Model-Data Comparison](./03-geodynamic-model-data.md) —
  the same accept/reject decision made with $\chi^2/\text{dof}$ instead of evidence.

## Self-assessment checklist

- [ ] I can specify a prior on a variable-dimension model space.
- [ ] I can derive a reversible-jump acceptance ratio with its Jacobian.
- [ ] I can compute an analytic evidence for a linear-Gaussian model.
- [ ] I can validate a sampler against an exact reference posterior.
- [ ] I can diagnose poor mixing from acceptance rates and chain behaviour.
- [ ] I can decompose posterior odds into prior and Occam factors.
