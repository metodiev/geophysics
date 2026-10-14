---
id: 18-05-01
title: "Bayes' Theorem as an Inverse-Problem Formulation"
level: doctoral
prereqs: ["18-01-05", "18-02-01", "18-03-02"]
tags: [inverse-problems, bayesian, uncertainty-quantification, posterior, map, tikhonov]
---

# Bayes' Theorem as an Inverse-Problem Formulation

All models and data in this module are **SYNTHETIC**. No number in this lesson is
a measurement; every figure quoted in the text is printed by
[`code/bayes_inverse_formulation_demo.py`](./code/bayes_inverse_formulation_demo.py),
which you should run as you read.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the posterior density from Bayes' theorem, naming the three
   ingredients (prior, likelihood, normalising constant) and stating which part
   of the inverse problem each one encodes.
2. **Construct** the posterior for a linear-Gaussian inverse problem in closed
   form, and **show** that its mean and covariance are the prior and likelihood
   precisions added.
3. **Demonstrate** that the Bayesian maximum a posteriori estimate is exactly the
   Tikhonov-regularised solution, with a regularisation parameter that the
   statistical model supplies rather than the analyst.
4. **Evaluate** whether a given data set is more informative than a given prior
   by comparing precisions, and state the answer as a fraction of the posterior.
5. **Explain** why a null-space direction is left at the prior, not set to zero,
   and **quantify** the posterior variance along that direction.
6. **Distinguish** maximising a posterior from averaging under it, and state the
   single condition under which the two coincide.
7. **State** the assumptions under which a Gaussian posterior is the correct one,
   and the diagnostics that would show they fail.

## Prerequisites

- [18-01-05 Model Space, Data Space and Mappings Between Them](../01-inverse-problem-foundations/05-model-space-data-space.md)
  — what $m$ and $d$ are, and what $G$ does to one to produce the other.
- [18-02-01 Overdetermined Problems and Least Squares](../02-linear-inverse-problems/01-overdetermined.md)
  — the least-squares solution this lesson generalises.
- [18-03-02 Tikhonov Regularisation and the Smoothing Trade-Off](../03-regularization/02-tikhonov.md)
  — the damping term that reappears here as a prior precision.
- [21-03-01 The Bayesian Paradigm](../../21-statistics-bayesian-ml/03-bayesian-inference/01-bayesian-paradigm.md)
  — the general Bayesian workflow this module specialises to inverse problems.

## 1. Intuition: an inverse problem is a question about probability

The classical inverse problem asks for the value of a model $m$ that produced a
data set $d$. It is ill-posed in the sense of
[18-01-02 Hadamard's Conditions](../01-inverse-problem-foundations/02-hadamard-well-posedness.md):
the answer may not exist, may not be unique, and may not depend continuously on
the data. Regularisation fixes the symptoms — it picks one answer out of the
admitted set — but the choice of the regularisation parameter is left dangling.
Where does that number come from?

The Bayesian reformulation answers that question by refusing to treat $m$ as a
fixed unknown. Instead $m$ is a random variable, the data are random too, and the
answer to the inverse problem is the **conditional distribution** of $m$ given
$d$. This is not a philosophical decoration. It converts a single number into a
distribution, and it makes every ingredient that a traditional inversion inserts
by hand — damping, smoothing, bounds, initialisation — explicit as a probability
statement whose consequences can be computed before the data arrive.

The trade is honest and must be stated up front: the posterior is conditional on
the likelihood **and** the prior. Change the prior and the posterior changes. A
Bayesian answer is not prior-free, and a report that hides the prior is
incomplete.

## 2. Formulation

### 2.1 Bayes' theorem

For a model vector $m \in \mathbb{R}^M$ and data $d \in \mathbb{R}^N$, Bayes'
theorem reads

$$
p(m \mid d) = \frac{p(d \mid m)\,p(m)}{p(d)},
\qquad
p(d) = \int p(d \mid m)\,p(m)\,\mathrm{d}m .
$$

The three ingredients map exactly onto the three questions of an inverse problem.

| Ingredient | Symbol | Inverse-problem role |
|---|---|---|
| Prior | $p(m)$ | What was admitted before the data: bounds, smoothness, plausible magnitude |
| Likelihood | $p(d \mid m)$ | The forward model **plus** the noise model; this is where physics enters |
| Evidence | $p(d)$ | The normalising constant; it makes the posterior integrate to one and is itself the model selection criterion of [07](07-evidence-and-model-selection.md) |

The posterior combines them by **multiplication in the exponent**. Taking
logarithms, with $\phi(m) = -\ln p(d\mid m)$ and $\psi(m) = -\ln p(m)$,

$$
-\ln p(m \mid d) = \phi(m) + \psi(m) + \text{const}.
$$

Every Bayesian inverse problem is therefore an optimisation of a sum of two
penalties — a data misfit and a prior penalty — unless one works with the whole
distribution, which is the point of the sampling lessons
[04](04-mcmc.md) and [05](05-hmc-and-modern-samplers.md).

### 2.2 The forward model is the likelihood

Suppose the physics can be written as a deterministic map $g$ and the observation
adds zero-mean noise $e$:

$$
d = g(m) + e, \qquad e \sim \mathcal{N}(0, C_d).
$$

Then $d \mid m \sim \mathcal{N}(g(m), C_d)$ and

$$
-\ln p(d \mid m) = \tfrac{1}{2}\bigl(d - g(m)\bigr)^{\!\top} C_d^{-1}
\bigl(d - g(m)\bigr) + \tfrac{1}{2}\ln|2\pi C_d| .
$$

The quadratic form is the same weighted misfit used by every least-squares
inversion; what has changed is that it is now interpreted as a density, so its
value can be compared with the prior and normalised.

## 3. The linear-Gaussian posterior, derived

Take $g(m) = Gm$ and a Gaussian prior $m \sim \mathcal{N}(m_0, C_M)$. Then

$$
-\ln p(m\mid d) = \tfrac{1}{2}(d-Gm)^{\top}C_d^{-1}(d-Gm)
+ \tfrac{1}{2}(m-m_0)^{\top}C_M^{-1}(m-m_0) + \text{const}.
$$

Expand the two quadratics in $m$, collect the quadratic form, and complete the
square. The term in $m^{\top}m$ is
$m^{\top}\!\left(G^{\top}C_d^{-1}G + C_M^{-1}\right)m$, so the posterior is
Gaussian with **posterior precision the sum of the two precisions**:

$$
C_{\text{post}} = \left(G^{\top}C_d^{-1}G + C_M^{-1}\right)^{-1},
\qquad
m_{\text{post}} = C_{\text{post}}\left(G^{\top}C_d^{-1}d + C_M^{-1}m_0\right).
$$

This is the central formula of the lesson. Read it as a statement about
information: precisions add. If $G^{\top}C_d^{-1}G$ is small in some direction,
that direction is dominated by $C_M^{-1}$ and the posterior there is the prior.

### 3.1 Numerical example: the two-parameter problem

The demonstration uses a SYNTHETIC problem with three data and two unknowns,

$$
G=\begin{bmatrix}1&0\\0&1\\1&1\end{bmatrix},\qquad
\sigma_d = 0.5,\qquad m_{\text{true}}=\begin{bmatrix}2\\-1\end{bmatrix},\qquad
m\sim\mathcal{N}(0,\,2^2 I).
$$

With the demonstration's noise realisation the data are
$d = (1.7645,\,-0.7691,\,0.5949)$. Then

$$
G^{\top}G=\begin{bmatrix}2&1\\1&2\end{bmatrix},\qquad
G^{\top}d = (2.3594,\,-0.1742),
$$

so the data precision is $G^{\top}C_d^{-1}G = 4\begin{bmatrix}2&1\\1&2\end{bmatrix}
= \begin{bmatrix}8&4\\4&8\end{bmatrix}$, the prior precision is
$\tfrac14 I$, and

$$
C_{\text{post}} = \begin{bmatrix}8.25&4\\4&8.25\end{bmatrix}^{-1}
= \begin{bmatrix}0.158472&-0.076830\\-0.076830&0.158472\end{bmatrix},
\qquad
m_{\text{post}} = \begin{bmatrix}1.5491\\-0.8355\end{bmatrix}.
$$

The posterior standard deviations are
$\sqrt{0.158472} = 0.3981$ for both parameters, and the correlation is
$-0.076830/0.158472 = -0.4848$. The demonstration prints exactly these values,
and also reproduces them by evaluating the posterior on a $401\times401$ grid:
the grid mean is $(1.5491,\,-0.8355)$ and the grid standard deviations are
$(0.3981,\,0.3981)$, agreeing with the analytics to the four decimals printed.
Two independent routes to the same posterior is the standard of evidence used
throughout this module.

## 4. Bayes' rule *is* Tikhonov regularisation

Written with isotropic covariances $C_d=\sigma_d^2 I$ and $C_M = s_0^2 I$, the
exponent of the posterior is

$$
-\ln p(m\mid d) = \frac{1}{2\sigma_d^2}\Bigl[
\bigl\|d-Gm\bigr\|^2 + \lambda^2\bigl\|m-m_0\bigr\|^2 \Bigr] + \text{const},
\qquad
\lambda^2 = \frac{\sigma_d^2}{s_0^2}.
$$

The minimiser is the damped least-squares solution of
[18-03-02](../03-regularization/02-tikhonov.md). The difference is interpretive
and it is not small: $\lambda$ is no longer a knob. It is the ratio of the noise
standard deviation to the prior standard deviation, so a weakly informative prior
*implies* a small $\lambda$ and a large posterior variance. The demonstration
prints the family for $\lambda \in \{0.05, 0.25, 1, 4\}$:

| $\lambda$ | damped solution $(m_1,m_2)$ | reading |
|---|---|---|
| 0.05 | $(1.6276,\,-0.8997)$ | prior nearly flat; close to least squares, wide posterior |
| **0.25** | $(\mathbf{1.5491},\,\mathbf{-0.8355})$ | the statistical value $\sigma_d/s_0$; the posterior mean |
| 1.00 | $(0.9066,\,-0.3602)$ | prior as strong as one datum; heavy shrinkage |
| 4.00 | $(0.1320,\,-0.0170)$ | prior dominant; the data barely move the answer |

## 5. Maximising versus averaging

The posterior mean $m_{\text{post}}$ and the maximum a posteriori estimate
$m_{\text{MAP}}$ are different operations: an expectation over the posterior
versus its mode. For the SYNTHETIC problem the demonstration reports

- the data misfit at the posterior mean, $\|d-Gm_{\text{post}}\| = 0.2548$;
- the data misfit at the least-squares fit, $\|d-Gm_{\text{LS}}\| = 0.2312$;
- the posterior objective $J(m) = \phi(m)+\psi(m)$ at the posterior mean,
  $0.517038$, and at a numerical minimiser, $0.517038$, whose coordinates are
  $(1.5491,\,-0.8355)$.

The posterior mean is **not** the best fit: it has a larger data misfit than the
least-squares solution, because it must also satisfy the prior. It *is* the
maximiser of the posterior, and it *is* the mean of the posterior, and the two
coincide because the posterior is Gaussian. Break the Gaussianity — a bounded
prior, a robust likelihood, a nonlinear forward model — and they separate; that
separation is the subject of [06](06-posterior-summary.md).

## 6. Rank deficiency: what the prior actually does

Replace $G$ by the SYNTHETIC rank-one operator

$$
G_{\text{bad}}=\begin{bmatrix}1&1\\2&2\\3&3\end{bmatrix},
$$

whose singular values the demonstration reports as $5.2915$ and $3.77\times
10^{-16}$ — the second is zero to machine precision. The direction
$v = (1,-1)/\sqrt2$ is in the null space: $G_{\text{bad}}v = 0$, so the data
contain no information about $m_1 - m_2$ at all. The posterior along $v$ is

$$
\sigma_{\text{post}}(v) = \sqrt{v^{\top}C_{\text{post}}\,v} = 2.0000
\ \text{in units of the model parameter},
$$

which is exactly the prior standard deviation $s_0 = 2$. The posterior has **not**
zeroed that direction; it has returned it to the prior. Reporting $m_{\text{post}}
= (0.4662,\,0.4662)$ as a unique answer hides the fact that any point on the line
$m_1+m_2 \approx$ const is equally consistent with the data. The honest report
is a posterior whose credible region is an unbounded-looking ridge — the subject
of [02](../02-linear-inverse-problems/01-overdetermined.md) and
[18-02-04 SVD Analysis](../02-linear-inverse-problems/04-svd-analysis-inverse.md).

## 7. The posterior as a normalised measure

It is worth checking that $p(m\mid d)$ really integrates to one, because that is
what makes it usable as a probability and not merely as a penalty. The
demonstration evaluates

$$
p(m\mid d)\ \propto\ \exp\!\left[-\frac{1}{2\sigma_d^{2}}\|d-Gm\|^{2}
-\frac{1}{2s_0^{2}}\|m-m_0\|^{2}\right]
$$

on a $401\times401$ grid with spacing $0.0275$, normalises the discrete masses,
and reports that the discrete mean, standard deviation and correlation match the
analytic ones. For a $2$-dimensional problem a grid is a perfectly good
integration rule; in ten or a hundred dimensions the same grid is unusable and a
sampler is required ([04](04-mcmc.md),
[05](05-hmc-and-modern-samplers.md)). That transition is why this module spends
five lessons on samplers.

## 8. Assumptions and regime of validity

1. **The noise model is the likelihood.** Everything downstream inherits it. If
   errors are correlated and treated as independent, the posterior is too narrow;
   [02](02-likelihood-models.md) measures how much.
2. **The prior is a choice, and it has consequences.** Informative priors shrink
   the answer; reference priors are not prior-free either; both are reported.
3. **Gaussianity of the posterior is a result, not an assumption.** It follows
   from a linear forward model with Gaussian noise and a Gaussian prior. Fail any
   one and the posterior mean, mode and credible limits separate.
4. **$C_d$ is known.** If it must be estimated from the data, the likelihood is
   hierarchical and the uncertainty in the noise parameters propagates into
   $C_{\text{post}}$.
5. **The model is complete.** All systematic error — model discrepancy,
   discretisation error, unit confusion — is treated as random here unless the
   likelihood is extended. Structural error is treated separately in
   [18-06-01 Uncertainty Taxonomy](../06-uncertainty-quantification/01-uncertainty-taxonomy.md).
6. **The forward map $G$ is exact.** If $G$ is itself approximate, the posterior
   understates the uncertainty; quantifying that gap is the work of
   [05-03 Forward-Model Validation](../../05-core-geophysics/03-forward-modelling-principles/05-forward-model-validation.md).

## 9. Demonstration and exercises

[`code/bayes_inverse_formulation_demo.py`](./code/bayes_inverse_formulation_demo.py)
computes all of the above and prints it with units; run it with the project venv
command in the [module README](./README.md). Graded problems with worked
solutions are in
[`exercises/01-bayes-inverse-formulation-exercises.md`](./exercises/01-bayes-inverse-formulation-exercises.md)
and
[`exercises/01-bayes-inverse-formulation-solutions.md`](./exercises/01-bayes-inverse-formulation-solutions.md).

## Mastery checkpoint

Without notes: a two-parameter problem has $G=\begin{bmatrix}1&1\\1&-1\end{bmatrix}$,
$\sigma_d = 0.4$, prior $m\sim\mathcal{N}((1,0),\,0.5^2I)$, and data
$d=(2.0,\,0.2)$. **(a)** Write down the posterior precision and invert it.
**(b)** Give the posterior mean. **(c)** State $\lambda$ for the equivalent
Tikhonov form. **(d)** A colleague computes the direction in which
$G^{\top}C_d^{-1}G$ vanishes and reports "the data determine $m_1+m_2$ exactly".
Say what is wrong with that sentence. **(e)** State one change to the
experiment that would shrink the posterior along that direction.

## Common pitfalls

1. **Reporting a posterior mean without the posterior.** It is a summary of a
   distribution; on its own it is a single number with no error bar.
2. **Treating $\lambda$ as free.** In a Bayesian formulation $\lambda$ is
   $\sigma_d/s_0$, both of which must be stated.
3. **Assuming the posterior is Gaussian because the *prior* is.** The forward map
   and the likelihood also have a say.
4. **Reading a null space as "zero".** A null direction is returned to the prior;
   its posterior width equals the prior width, as measured in Section 6.
5. **Confusing the evidence with a goodness-of-fit.** $p(d)$ is a normalising
   constant for one model and a model comparison criterion across models; it is
   never a measure of how well the model fits.
6. **Choosing a prior after seeing the answer.** Deciding the prior in the light
   of the posterior is a re-use of the data that invalidates the calibration.

## Further reading

- **Tarantola, A. (2005). *Inverse Problem Theory and Methods for Model Parameter
  Estimation*. SIAM.** Level: research. The fullest statement of the Bayesian
  view of inverse problems; the derivations in Section 3 follow its structure.
- **Sivia, D. S., & Skilling, J. (2006). *Data Analysis: A Bayesian Tutorial*
  (2nd ed.). Oxford University Press.** Level: advanced. The shortest honest route
  from Bayes' theorem to a working posterior.
- **Jaynes, E. T. (2003). *Probability Theory: The Logic of Science*. Cambridge
  University Press.** Level: research. Why a prior is unavoidable, argued from
  consistency rather than from convenience.
- **Gelman, A., Carlin, J. B., Stern, H. S., Dunson, D. B., Vehtari, A., &
  Rubin, D. B. (2013). *Bayesian Data Analysis* (3rd ed.). CRC Press.**
  Level: research. The reference for hierarchical likelihoods and prior
  sensitivity, used in lessons [02](02-likelihood-models.md) and
  [03](03-priors.md).

## Related modules

- [02 Constructing Likelihoods and Error Models](02-likelihood-models.md) — what
  happens when $C_d$ is wrong.
- [03 Priors: Informative, Reference and Their Influence](03-priors.md) — the
  other half of the product.
- [04 Markov Chain Monte Carlo: Metropolis-Hastings and Gibbs](04-mcmc.md) — how
  to work with the posterior when the analytic route is closed.
- [06 Posterior Summaries](06-posterior-summary.md) — how to report the
  distribution honestly.
- [07 Bayesian Evidence and Model Selection](07-evidence-and-model-selection.md) —
  what the normalising constant $p(d)$ is for.
- [18-02-01 Overdetermined Problems and Least Squares](../02-linear-inverse-problems/01-overdetermined.md)
  and [18-03-02 Tikhonov Regularisation](../03-regularization/02-tikhonov.md) —
  the deterministic forms that this lesson subsumes.
- [18-06-02 Monte Carlo Propagation and Its Convergence](../06-uncertainty-quantification/02-monte-carlo-uq.md)
  — what to do with a posterior once you have one.
