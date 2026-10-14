---
id: 13-05-04
title: "Data Assimilation and Adjoint Geodynamics"
level: research
prereqs: ["13-05-03", "18-02-04", "18-04-02"]
tags: [geodynamics, tectonophysics, adjoint, data-assimilation, inverse-problems, uncertainty]
---

# Data Assimilation and Adjoint Geodynamics

> **All models and data in this module are SYNTHETIC.** The forward model is a
> chosen one-dimensional diffusion problem; the "data" are generated from a known
> truth with added noise. Every number is printed by
> [`code/data_assimilation_geodynamics_demo.py`](code/data_assimilation_geodynamics_demo.py).

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the adjoint of a time-stepping forward model and **verify** the
   resulting gradient against central finite differences.
2. **Measure** the singular-value (Picard) spectrum of a diffusive forward map
   and **state** how many modes a given noise level admits.
3. **Explain** why a diffusion forward map has a genuine null space and
   **demonstrate** it by two initial conditions that produce the same observable.
4. **Quantify** the cost advantage of the adjoint over finite differences as a
   function of the number of parameters, and **say** when the advantage does not
   matter.
5. **Estimate** how many ensemble members are needed for a spread-based
   uncertainty to be reliable, from a measured $N^{-1/2}$ sampling error.
6. **State** the difference between a data-constrained component and a component
   suppressed by regularisation.

## Prerequisites

- [13-05-03 Benchmarking Geodynamic Codes](03-benchmarking-geodynamics.md) —
  verification discipline, applied here to a gradient.
- [18-02-04 SVD Analysis of Inverse Problems](../../18-inverse-problems/02-linear-inverse-problems/04-svd-analysis-inverse.md) —
  singular values, the Picard condition and the null space.
- [18-04-02 Gradient and Newton Methods](../../18-inverse-problems/04-nonlinear-inversion/02-gradient-and-newton.md) —
  the optimisation setting in which the adjoint gradient is used.
- [18-06-01 Uncertainty Taxonomy](../../18-inverse-problems/06-uncertainty-quantification/01-uncertainty-taxonomy.md) —
  where ensemble-based uncertainties come from.

## 1. Why assimilation is unavoidable in geodynamics

A geodynamic model is never observed directly. What is observed is a present-day
state — seismic velocities, gravity, heat flow, surface velocities, topography —
and the model is a history that produced it. The inference therefore runs
*backwards in time*, and the forward map that must be inverted is a
time-integration of diffusion, advection and creep. Such maps are strongly
smoothing, and this lesson quantifies exactly what that costs: how much of the
initial condition can come back, how expensive the gradient is, and what a
"recovered" model means when part of it is invisible.

The demonstration uses the smallest model that has all the relevant features:

$$\frac{\partial\theta}{\partial t} = \kappa\frac{\partial^2\theta}{\partial z^2},
\qquad \theta(0,t) = \theta(L,t) = 0,$$

discretised by explicit finite differences with diffusion number
$\nu = \kappa\,\Delta t/h^2 = 0.40$ on $N = 64$ interior nodes ($h = 0.01538$) for
$N_{\text{step}} = 120$ steps, so the total time is
$T = 120\,\kappa\Delta t = 0.011361$ in units of $L^2/\kappa$. The observable is
the final state $\boldsymbol{d} = M\boldsymbol{m}$, where $\boldsymbol{m}$ is the
initial condition and the matrix $M = (I + \nu L)^{120}$ with $L$ the second-
difference operator.

## 2. The Picard spectrum: what diffusion destroys

The singular values of $M$ are the amplification factors the model applies to
each mode of the initial condition. Measured:

| index | singular value | above $10^{-3}$? | above $10^{-6}$? |
|---|---|---|---|
| 0 | $8.939\times10^{-1}$ | yes | yes |
| 1 | $6.383\times10^{-1}$ | yes | yes |
| 2 | $3.636\times10^{-1}$ | yes | yes |
| 4 | $5.946\times10^{-2}$ | yes | yes |
| 8 | $9.229\times10^{-5}$ | no | yes |
| 16 | $4.367\times10^{-16}$ | no | no |
| 32 | $1.541\times10^{-17}$ | no | no |
| 48 | $5.678\times10^{-18}$ | no | no |
| 63 | $2.393\times10^{-20}$ | no | no |

The largest is $8.939\times10^{-1}$ and the smallest $2.393\times10^{-20}$: a
ratio of $2.7\times10^{-20}$, i.e. below double precision. **Seven of the 64
modes carry a singular value above $10^{-3}$; ten above $10^{-6}$.** Everything
else has been damped below any realistic data noise by the time the observation
is taken.

Two consequences, both of which are properties of the physics rather than of the
algorithm:

- The number of recoverable modes is set by the product of the noise level and
  the time $T$: doubling $T$ halves the number of modes roughly as
  $\sqrt{\ln(1/\epsilon)}$.
- Increasing the number of grid points does not increase the number of
  recoverable modes. It increases the resolution of the *forward* problem while
  leaving the *inverse* problem exactly as underdetermined as it was.

## 3. The adjoint gradient, and how to know it is right

For a misfit $J(\boldsymbol{m}) = \tfrac12\|M\boldsymbol{m}-\boldsymbol{d}\|^2$
the gradient is $\nabla J = M^{\mathsf{T}}(M\boldsymbol{m}-\boldsymbol{d})$, and
for a time-stepping forward model the transpose application is the *adjoint
integration run backwards*. The demonstration applies the transpose explicitly
and compares with central finite differences with step $\epsilon = 10^{-7}$:

| quantity | value |
|---|---|
| $\|\nabla J\|$ from the adjoint | 1.193857 |
| $\|\nabla J\|$ from finite differences | 1.193857 |
| maximum componentwise relative difference | $1.030\times10^{-8}$ |
| overall relative difference | $5.727\times10^{-9}$ |

The gradient is verified. The residual is not round-off but the accuracy of the
difference quotient itself: with $\epsilon = 10^{-7}$ in double precision, the
central difference carries a relative error of order $\epsilon^{2/3} \approx
2.2\times10^{-5}$, so agreement at the $10^{-9}$ level is *better* than the
finite-difference test can resolve. That is the general rule: a gradient test
verifies the adjoint only down to the accuracy of the difference quotient, and a
test that disagrees at $10^{-3}$ is a real bug while one that agrees at $10^{-9}$
means the test has run out of resolution, not that the adjoint is perfect.

## 4. Worked example: recovering an initial condition

*Problem.* Invert noiseless data generated by a Gaussian initial condition
$m_{\text{true}}(x) = \exp[-(x-0.5)^2/(2\cdot0.08^2)]$ by gradient descent with
step $1/L_{\max}^2 = 1.2515$.

1. After 4000 iterations the misfit falls to $J = 1.487\times10^{-6}$: the data
   are matched.
2. The recovered field still differs from the truth by
   $\|\hat m - m_{\text{true}}\|_\infty/\|m_{\text{true}}\|_\infty = 0.1197$ —
   about 12%, on *noiseless* data.
3. Why: decompose both fields in sine modes and compare. The Gaussian is
   symmetric about the centre, so only odd modes are populated:

| mode | amplitude of $m_{\text{true}}$ | amplitude of the recovered error |
|---|---|---|
| 1 | 2.215315 | 0.000000 |
| 3 | 1.720702 | 0.000000 |
| 9 | 0.177067 | 0.177060 |
| 13 | 0.010993 | 0.010993 |
| 21 | 0.000002 | 0.000002 |

Modes 1 and 3 come back exactly; from mode 9 onward the entire amplitude is
missing. The recovered field is a *low-pass* version of the truth, and its
residual error is concentrated in exactly the modes that Section 2 says are
invisible.

*Answer.* A time-integration inverse problem returns the resolvable part of the
initial condition. The right way to report it is as a filtered reconstruction
with a stated cut-off, not as "the initial condition".

## 5. The null space, measured two ways

Take $\boldsymbol{m}_1$ as the leading singular vector scaled to 3, and
$\boldsymbol{m}_2 = \boldsymbol{m}_1 + \tfrac12\boldsymbol{v}_{\text{null}}$
where $\boldsymbol{v}_{\text{null}}$ is the trailing singular vector — the
direction the model damps hardest. Measured:

- relative difference of the initial conditions:
  $\|\boldsymbol{m}_2-\boldsymbol{m}_1\|/\|\boldsymbol{m}_1\| = \mathbf{0.1667}$
  (a 16.7% change);
- relative difference of the observables:
  $\mathbf{1.304\times10^{-16}}$ — below double-precision round-off;
- amplification ratio: $7.826\times10^{-16}$.

So a 16.7% change of the initial state is *invisible*. On noisy data the two
hypotheses are equally acceptable:

| quantity | value |
|---|---|
| $J(\boldsymbol{m}_1)$ | $2.8851492418\times10^{-6}$ |
| $J(\boldsymbol{m}_2)$ | $2.8851492418\times10^{-6}$ |
| difference | $1.05\times10^{-19}$ |

and inverting data generated from each (with a different noise realisation) by
gradient descent from zero gives

- from $\boldsymbol{m}_1$: error 0.0033, and $\|\hat m\|/\|m_{\text{true}}\| = 1.0001$;
- from $\boldsymbol{m}_2$: error 0.1646, and $\|\hat m\|/\|m_{\text{true}}\| = 0.9865$;
- the **two recovered fields differ by only 1.14%**, although the two truths
  differ by 16.7%.

This is the operational meaning of a null space: a zero-start (minimum-norm)
inversion returns essentially the same answer for two very different truths, and
the component it misses is exactly the one its regularisation suppresses. The
minimum-norm choice is a *choice* — a modelling decision that must be stated,
because the data do not make it.

## 6. Cost: one adjoint against $2p$ forward runs

Gradients can also be computed by finite differences: one perturbed forward run
per parameter per side. Measured cost, averaged over 100 applications:

| operation | measured time |
|---|---|
| one forward application $M\boldsymbol{m}$ | 0.0027 ms |
| one forward-plus-adjoint pair $M^{\mathsf{T}}(M\boldsymbol{m})$ | 0.0116 ms |
| finite-difference gradient over all 64 parameters (128 forward runs) | 0.35 ms |
| adjoint gradient (2 applications) | 0.0116 ms |

The measured speed-up is **30× for 64 parameters**, and it grows linearly with
the number of parameters. For a geodynamic inverse problem with $10^5$–$10^6$
discretised parameters, the finite-difference gradient is not merely slow but
impossible, and the adjoint is the only route. The caveat is equally important:
for a *handful* of parameters (a scalar viscosity, an interface depth), finite
differences are simpler, use one forward code rather than two, and the adjoint's
advantage is negligible. The demonstration's own Section 4 inverts a *one*-
parameter family; the adjoint is the wrong tool there.

## 7. Uncertainty from an ensemble, and how many members

An ensemble assimilation estimates an uncertainty from the spread of the members.
The sampling error of a standard deviation estimated from $N$ independent
realisations falls as $N^{-1/2}$. The demonstration estimates the amplitude of a
fixed spatial pattern from 2000 independent noisy realisations, uses the full set
as the reference, and measures the error of a shorter ensemble:

| $N$ realisations | std estimate | error against the reference |
|---|---|---|
| 10 | $1.574\times10^{-4}$ | 2.11% |
| 30 | $1.282\times10^{-4}$ | 20.24% |
| 100 | $1.476\times10^{-4}$ | 8.19% |
| 300 | $1.556\times10^{-4}$ | 3.22% |
| 1000 | $1.590\times10^{-4}$ | 1.14% |
| 2000 | $1.608\times10^{-4}$ | 0.00% |

The fitted exponent over $N = 30\ldots1000$ is $-0.822$. The ideal sampling error
of a standard deviation is $N^{-1/2}$; the measured exponent is steeper here
because a single sequence of realisations is used and the small-ensemble entries
are the erratic ones. What the measurement establishes is the *scale* of the
problem: at 30 members this single sequence is out by 20%, so an ensemble
assimilation that reports a spread from a few tens of members is reporting a
number with tens of per cent of sampling noise *before* any model error is added.
And in geodynamics model error is never zero.

## 8. Assumptions and regime of validity

1. **The forward model is linear and the noise is Gaussian and known.** The
   Picard analysis and the closed-form scale solution both rely on linearity;
   with a nonlinear forward map the singular-value picture is local (a
   Jacobian), and the noise level is usually unknown.
2. **The data are the final state at one time.** More observation times, or a
   different observable (a gradient, an integral), change which modes are
   resolvable; the null space is a property of the *experiment*, not of diffusion
   alone.
3. **The gradient test is limited by the difference quotient.** Agreement at
   $10^{-9}$ with $\epsilon = 10^{-7}$ means the test is saturated, not that the
   adjoint is exact.
4. **The minimum-norm solution is a regularisation choice.** Starting from zero
   is convenient, not implied; a different prior gives a different null-space
   component.
5. **Ensemble uncertainties assume exchangeable members.** Real ensembles inherit
   correlated model error, which no $N$ can remove.
6. **Nothing here is calibrated to a real data set.** The "observation" is a
   forward-modelled final state with added noise.

## Mastery checkpoint

Without notes:

1. Write down the adjoint of one explicit diffusion step and explain why the
   adjoint integration runs backwards in time.
2. State the Picard condition in one sentence and use the measured spectrum to
   say how many modes a 0.1% noise level admits.
3. Given a forward map with singular values $\{1, 10^{-1}, 10^{-3}, 10^{-8}\}$ and
   a noise level $10^{-4}$, state which modes are recoverable and what the
   inversion will do with the others.
4. Explain why increasing the grid resolution does not increase the number of
   recoverable modes.
5. Estimate the cost ratio between an adjoint gradient and a finite-difference
   gradient for $p = 10$ and $p = 10^{5}$ parameters, and say which is preferable
   in each case, and why.
6. A colleague reports $\sigma = 0.5$ from a 40-member ensemble. What is the
   first question to ask about that number?

## Common pitfalls

1. **Reporting a recovered initial condition as if it were the truth.** The
   demonstration's noiseless inversion is 12% wrong.
2. **Testing a gradient with too large a step.** A difference quotient with
   $\epsilon = 10^{-3}$ cannot resolve better than $10^{-2}$ relative, so a
   $10^{-3}$ discrepancy proves nothing.
3. **Using the adjoint for a handful of parameters.** It is a 30× win at 64
   parameters and a complication at two.
4. **Treating the number of modes as a resolution question.** It is a
   noise-and-time question.
5. **Reporting an ensemble spread without its sampling error.** At 30 members
   that error is tens of per cent.
6. **Forgetting that the null-space component is a modelling choice.** The data
   are silent about it, so whatever was assumed must be stated.

## Related modules

- [13-05-03 Benchmarking Geodynamic Codes](03-benchmarking-geodynamics.md) —
  the verification habit that makes a gradient test meaningful.
- [18-02-04 SVD Analysis of Inverse Problems](../../18-inverse-problems/02-linear-inverse-problems/04-svd-analysis-inverse.md) —
  singular values, the Picard condition and the null space in general.
- [18-04-02 Gradient and Newton Methods](../../18-inverse-problems/04-nonlinear-inversion/02-gradient-and-newton.md) —
  how the adjoint gradient is used in an optimisation.
- [18-06 Uncertainty Quantification](../../18-inverse-problems/06-uncertainty-quantification/README.md) —
  sampling error, ensembles and decision-making.
- [13-02-02 Numerical Modelling of Mantle Convection](../02-mantle-convection/02-convection-numerical.md) —
  the models such assimilations are built on.

Companion exercises:
[`exercises/04-data-assimilation-geodynamics-exercises.md`](exercises/04-data-assimilation-geodynamics-exercises.md)
and
[`exercises/04-data-assimilation-geodynamics-solutions.md`](exercises/04-data-assimilation-geodynamics-solutions.md).
Run the demonstration with

```bash
cd 13-geodynamics-tectonics/05-geodynamic-modelling/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python data_assimilation_geodynamics_demo.py
```
