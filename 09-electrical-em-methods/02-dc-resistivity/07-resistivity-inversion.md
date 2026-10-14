---
id: 09-02-07
title: "Resistivity Inversion: Smoothness, Robustness, Constraints"
level: research
prereqs: ["09-02-06", "18-02-01", "18-03-02"]
tags: [electrical-methods, inversion, tikhonov, l-curve, robust, covariance, non-uniqueness]
---

# Resistivity Inversion: Smoothness, Robustness, Constraints

Inversion is the step where a set of voltages becomes a picture, and it is the
step where most of the information is quietly discarded. This lesson builds a
complete one-dimensional inversion — Gauss–Newton on log-resistivities with a
smoothness penalty — and then spends most of its effort on the three questions
that decide whether the answer is meaningful: how the trade-off parameter is
chosen, what the model covariance says, and how a single bad datum changes the
result.

**All models and data in this module are SYNTHETIC.** The true model, the noise
and the starting models are chosen teaching values; no field data are used.

## Learning objectives

By the end of this lesson you will be able to:

1. **Formulate** a damped Gauss–Newton inversion with a roughness penalty in log
   space and **explain** why log parameters are used.
2. **Choose** the trade-off parameter from a linearised L-curve using the
   discrepancy principle, and **state** the convention used to define it.
3. **Explain** why a model bound is part of the formulation, not a refinement,
   and what happens without one.
4. **Compute** a model covariance and interpret neighbouring-layer
   correlations.
5. **Test** a converged solution with multi-start and report what the test does
   and does not prove.
6. **Detect** an outlier from residuals and **quantify** what robust reweighting
   recovers and what it cannot.
7. **Report** an inversion with the admitted family, the covariance and the
   regularisation bias, instead of a single number.

## Prerequisites

- [09-02-06 Forward Modelling Resistivity Data](06-resistivity-forward-modelling.md) —
  the forward model, its verification and its null space.
- [18-02-01 Overdetermined Problems and Least Squares](../../18-inverse-problems/02-linear-inverse-problems/01-overdetermined.md).
- [18-03-02 Tikhonov Regularisation and the Smoothing Trade-Off](../../18-inverse-problems/03-regularization/02-tikhonov.md).

## 1. The formulation

Data are log-apparent resistivities at eight Wenner spacings,
$d_i = \ln\rho_a(a_i)$, with an assumed relative error
$\sigma = 2\%$ in the log domain. The model is
$m_j = \ln\rho_j$ for four resistivities with fixed layer boundaries. Minimise

$$\Phi(m) = \left\|\frac{d - f(m)}{\sigma}\right\|^{2}
+ \lambda\left\|Dm\right\|^{2}, \qquad
D_{ij} = -1\ (i=j),\ +1\ (j=i+1),$$

solved by Gauss–Newton: with $J = \partial f/\partial m$ evaluated at $m^{(k)}$,

$$\left(J^{\mathsf{T}}J + \lambda D^{\mathsf{T}}D\right)\delta m =
J^{\mathsf{T}}r, \qquad r_i = \frac{d_i - f_i(m)}{\sigma},
\qquad m^{(k+1)} = m^{(k)} + \delta m.$$

Three choices deserve comment.

- **Log parameters.** Resistivity spans decades; in linear space a single deep
  layer with a large value dominates the Jacobian and the inversion wastes its
  effort there.
- **Roughness penalty.** The null space of [09-02-06](06-resistivity-forward-modelling.md)
  means the data cannot determine the model alone; the penalty selects the
  smoothest member of the equivalence class, which is a *stated choice*.
- **Bounds.** The model is clipped to $1\ \Omega\,\mathrm{m} \le \rho \le
  10^{5}\ \Omega\,\mathrm{m}$, the range of the SYNTHETIC teaching catalogue of
  [09-01-01](../01-electrical-properties-of-earth/01-resistivity-conductivity.md).
  This is not cosmetic: without a bound the basement resistivity has no finite
  best fit at all, because the data are essentially insensitive to it and the
  quadratic misfit does not grow as it runs away.

## 2. Convergence, and what the model looks like

The demo's SYNTHETIC truth is $\rho = (200, 30, 8, 800)\ \Omega\,\mathrm{m}$ with
boundaries at 2, 6 and 18 m; the data carry 2% noise (a fixed
seed) and the fit starts from a uniform $100\ \Omega\,\mathrm{m}$:

| iteration | 0 | 1 | 2 | 3 | 4 | 6 | 8 | 10 | 14 |
|---|---|---|---|---|---|---|---|---|---|
| $\chi^{2}$ per datum | 311.215 | 33.323 | 2.184 | 1.146 | 0.999 | 0.955 | 0.941 | 0.933 | 0.926 |
| roughness $\|Dm\|$ | 0.8463 | 1.4559 | 1.9975 | 2.2572 | 2.4294 | 2.6523 | 2.8023 | 2.9163 | 3.0864 |

Convergence takes about four iterations to reach the noise level, after which
the model keeps *roughening* while the misfit improves by pennies: the trade-off
parameter, not the data, is now in control. At $\lambda = 1$ the recovered model
is $(197.7, 33.5, 10.2, 1374.8)$:

| layer | true ($\Omega\,\mathrm{m}$) | recovered | error |
|---|---|---|---|
| 1 | 200.0 | 197.7 | $-1.2\%$ |
| 2 | 30.0 | 33.5 | $+11.6\%$ |
| 3 | 8.0 | 10.2 | $+27.9\%$ |
| 4 | 800.0 | 1374.8 | $+71.9\%$ |

The first layer is recovered to about 1%; everything below the second is biased
by tens of per cent, with a sign and a size that come from the regularisation,
not from the physics. **The data constrain the deep structure weakly and the
smoothness prior fills the gap.**

## 3. Choosing the trade-off: the L-curve

The demo computes a *linearised* L-curve: one Jacobian at the converged model,
then for each $\lambda$ a single solve of the damped system and one forward
evaluation:

| $\lambda$ | $10^{-4}$ | $10^{-2}$ | 0.1 | 1.0 | 3.0 | 10 | 30 |
|---|---|---|---|---|---|---|---|
| $\chi^{2}$ per datum | 1.268 | 0.961 | 0.917 | 0.923 | 0.924 | 0.924 | 0.924 |
| roughness | 7.9212 | 5.1548 | 3.4150 | 3.1212 | 3.0980 | 3.0899 | 3.0875 |

Two features of this table are typical and worth naming. First, $\chi^{2}$ is
nearly flat for $\lambda \gtrsim 0.1$: the excess structure bought by a small
$\lambda$ does not improve the fit, it only fits noise. Second, roughness keeps
falling while $\chi^{2}$ rises only slightly — that flat region is the L-curve's
"foot" and it is why the criterion matters.

The demo uses the **discrepancy principle with an explicit convention**: the
smallest $\lambda$ whose linearised $\chi^{2}$ per datum still reaches 0.9.
Here that is $\lambda = 10^{-4}$, i.e. the roughest model consistent with the
assumed noise. Solving fully at that $\lambda$ gives
$(197.8, 33.5, 9.9, 10^{5})\ \Omega\,\mathrm{m}$ — and the basement has hit the
bound. **That is the honest answer: the sounding does not constrain the
basement, so the reported quantity is a bound, and the demo says so in the
output.** A different convention (say, the largest $\lambda$ with
$\chi^{2} \le 1$) would give a smoother model and, in this case, a basement near
the starting value — which would be an artefact of the starting model, not a
measurement.

## 4. Model covariance

At the chosen $\lambda$ the linearised model covariance is

$$\mathrm{Cov}(m) = \left(J^{\mathsf{T}}J + \lambda D^{\mathsf{T}}D\right)^{-1}
\quad\Rightarrow\quad \sigma_{m_j} = \sqrt{\mathrm{Cov}_{jj}},$$

in units of $\ln\rho$, so $\sigma_{m_j}$ is the fractional uncertainty in
$\rho_j$. The demo's table (with $\lambda = 10^{-4}$) is

| layer | $\rho$ ($\Omega\,\mathrm{m}$) | $1\sigma$ (%) | correlation with the next layer |
|---|---|---|---|
| 1 | 197.8 | 1.6 | $-0.786$ |
| 2 | 33.5 | 18.4 | $+0.394$ |
| 3 | 9.9 | 14.9 | $-0.275$ |
| 4 | $10^{5}$ (at the bound) | — | — |

Neighbouring-layer correlations are large and of *either* sign — the inversion
trades one layer against the next, exactly along the null direction of
[09-02-06](06-resistivity-forward-modelling.md). Where the data are
uninformative the correlation collapses while the individual uncertainty
explodes: the basement is limited only by the bound we imposed. **A covariance
that is small for a layer whose sensitivity is near zero is a lie; check the
Jacobian before believing an error bar.**

## 5. Multi-start: what a converged fit does and does not prove

The demo runs the same inversion from three starting models:

| starting model | $\chi^{2}$ | recovered $\rho$ ($\Omega\,\mathrm{m}$) |
|---|---|---|
| uniform 10 | 0.909 | 197.8, 33.5, 9.9, $10^{5}$ |
| uniform 1000 | 0.909 | 197.8, 33.5, 9.9, $10^{5}$ |
| decreasing 1000, 100, 10, 1 | 0.909 | 197.8, 33.5, 9.9, $10^{5}$ |

All three converge to the same model, with a layer-wise spread of 0.0% for the
first three layers and a spread limited only by the bound for the fourth. So
**for this data set the misfit surface is effectively unimodal**, and the demo
says exactly that rather than claiming a general uniqueness. The uncertainty is
not in multiple minima here; it is in the covariance of Section 4 and in the
equivalence classes of [09-02-03](03-apparent-resistivity.md). This is the
honest use of a multi-start test: it can find a second minimum, and a single
convergence is evidence about *this* data set only.

## 6. Robustness: one bad datum

Corrupt the $a = 6$ m datum with $+20\%$ and keep the assumed 2% error model:

| model | $\chi^{2}$ | $\rho_1$ | $\rho_2$ | $\rho_3$ | $\rho_4$ |
|---|---|---|---|---|---|
| true | — | 200.0 | 30.0 | 8.0 | 800.0 |
| least squares | 9.728 | 191.7 | 67.9 | 10.9 | $10^{5}$ |
| Huber reweighted, 3 sweeps | 3.659 | 195.6 | 48.7 | 10.3 | $10^{5}$ |

Units: $\Omega\,\mathrm{m}$. The weights come from residual ratios
$|r_i/\sigma|$: a datum with a ratio below 2 keeps weight 1, above it is
down-weighted as $2/|r_i/\sigma|$ (Huber). Reweighting brings layer 2 from 67.9
back to 48.7 $\Omega\,\mathrm{m}$ against a true 30 — it *reduces the damage
without undoing it* — and three of the eight data end up down-weighted. The
lesson is not "use a robust norm"; it is:

1. A single 20% error against a 2% error model is a serious error, and no
   weighting scheme fully recovers from it.
2. The residual expressed in units of the *assumed* error is the diagnostic;
   computing it is mandatory, not optional.
3. Reporting $\chi^{2} = 9.7$ on the least-squares answer and stopping would have
   hidden the fact that the fit is being driven by one datum.

## 7. Regime of validity

1. **Fixed layer boundaries.** Thicknesses are not inverted here; inverting them
   adds exactly the null directions of
   [09-02-06](06-resistivity-forward-modelling.md).
2. **Gaussian, independent errors.** The covariance and the discrepancy
   principle both assume it; correlated errors inflate the true uncertainty.
3. **Local linearisation.** The covariance is a linearised object; the admitted
   family must be explored with the nonlinear model when a null direction is
   present (Section 6 of [09-02-06](06-resistivity-forward-modelling.md)).
4. **The smoothness penalty is a choice.** A different norm (total variation,
   minimum-structure, sparsity in a transform domain) gives a different model
   with the same misfit.
5. **One-dimensional here; two- and three-dimensional ERT adds lateral
   smoothing and a much larger null space** (module 09-02-05 and 09-02-08).

## 8. Mastery checkpoint

1. Write the damped normal equations and explain each term.
2. Given the L-curve table, state which $\lambda$ you would choose under the
   convention "$\chi^{2}$ per datum = 1", and what the choice does to the deep
   layer.
3. Explain why a bound on the model is part of the *formulation* rather than a
   numerical safeguard.
4. From the covariance table, state which layer resistivities the data actually
   determine and which are set by the prior.
5. A datum has a residual of $5\sigma$. Give the two actions you would take
   before deleting anything.

## 9. Common pitfalls

1. **Reporting a model without $\chi^{2}$.** A fit that misses the noise level
   is not a fit.
2. **Deleting outliers.** Reweight, or report them; deleting changes the data
   set silently.
3. **Believing small error bars for insensitive parameters.** The basement in
   Section 4 is the example.
4. **Using a multi-start test as a uniqueness proof.** It is a search, not a
   theorem.
5. **Choosing $\lambda$ by taste.** State the criterion and the convention.
6. **Forgetting that the *picture* is a penalty's choice.** Change the norm and
   the picture changes with the misfit unchanged.

## 10. Related modules

- [09-02-06 Forward Modelling Resistivity Data](06-resistivity-forward-modelling.md).
- [09-02-08 ERT Applications](08-ert-applications.md).
- [18-03-03 Choosing the Trade-Off: L-Curve, GCV, Discrepancy Principle](../../18-inverse-problems/03-regularization/03-parameter-choice.md).
- [18-03-06 Physical Constraints, Bounds and Feasible Model Sets](../../18-inverse-problems/03-regularization/06-constraints.md).
- [18-06 Uncertainty Quantification](../../18-inverse-problems/06-uncertainty-quantification/README.md).
- [09-02 Resistivity Methods](README.md).

## 11. Demonstration and exercises

- [`code/resistivity_inversion_demo.py`](code/resistivity_inversion_demo.py)
  prints the synthetic data, the iteration history, the L-curve, the covariance,
  the multi-start test and the robust-reweighting comparison.
- [Exercises](exercises/07-resistivity-inversion-exercises.md) and
  [worked solutions](exercises/07-resistivity-inversion-solutions.md).
