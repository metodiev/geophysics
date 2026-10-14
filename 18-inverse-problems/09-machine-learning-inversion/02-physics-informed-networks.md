---
id: 18-09-02
title: "Physics-Informed Neural Networks"
level: research
prereqs: ["18-09-01", "18-04-01"]
tags: [inverse-problems, machine-learning, pinn, physics-informed, boundary-value-problem]
---

# Physics-Informed Neural Networks

> All models and data in this module are **SYNTHETIC**. The equation, its source
> term and its exact solution are chosen teaching ingredients; no number below is
> a measurement of the Earth. Training is deliberately tiny: one hidden layer and
> a few hundred optimiser iterations, finishing in about half a second.

## Learning objectives

By the end of this lesson you will be able to:

1. **Formulate** the physics-informed loss as a residual of the governing
   equation plus boundary conditions, and **state** what information it uses
   instead of interior data.
2. **Compute** the analytic second derivative of a one-hidden-layer
   $\tanh$ network and **use** it to evaluate a PDE residual exactly.
3. **Measure** the accuracy of a physics-only fit, a data-only fit, and a
   combined fit against an exact solution.
4. **Diagnose** a data-only fit by its physics residual and boundary error rather
   than by its data misfit.
5. **Measure** the failure under mis-specified physics and **state** why no
   internal diagnostic can detect it.
6. **State** when a physics-informed network is a reformulation of a classical
   solver and when it is genuinely a different method.

## Prerequisites

- [18-09-01 Learned Inversion: Direct and Iterative Networks](01-learned-inversion.md) —
  the empirical-risk view, and why the prior matters.
- [18-04-01 Local Linearisation, Jacobians and Iteration](../04-nonlinear-inversion/01-local-linearization.md) —
  the optimisation vocabulary used here.

## 1. The physics-informed loss

Rather than learning from data alone, a physics-informed network (PINN)
minimises the **residual of the governing equation** at collocation points,
subject to boundary conditions. For a boundary-value problem
$\mathcal{L}[u] = f$, $u|_{\partial\Omega} = g$:

$$\Phi(\theta) = \frac{1}{N_c}\sum_{i=1}^{N_c}
\left|\mathcal{L}[u_\theta](\mathbf{x}_i) - f(\mathbf{x}_i)\right|^2
+ \beta\,\frac{1}{N_b}\sum_{j=1}^{N_b}\left|u_\theta(\mathbf{x}_j) - g(\mathbf{x}_j)\right|^2 .$$

No solution values are used. The information comes from the **equation**, and for
a well-posed problem the equation plus the boundary data determine the solution —
which is why a physics-only PINN can succeed where a data-only network with five
measurements cannot.

This connection is worth stating plainly: for a well-posed linear problem the PINN
is a **least-squares collocation solver** for the PDE, expressed in a neural
basis. Modern deep-learning terminology does not change the approximation theory
underneath.

## 2. Worked example: a BVP with a known solution

`code/physics_informed_demo.py` solves

$$-u''(z) = f(z) = \pi^2\sin(\pi z), \quad z\in(0,1),\qquad u(0)=u(1)=0,
\qquad u(z)=\sin(\pi z),$$

with a one-hidden-layer network $u(z) = \mathbf{W}_2\cdot\tanh(\mathbf{W}_1 z +
\mathbf{b}_1) + b_2$ (16 units, 65 parameters), 200 collocation points,
$\beta = 100$ and L-BFGS-B.

The second derivative is available in closed form. With
$h_j = \tanh(W_{1j}z + b_{1j})$,

$$\frac{\mathrm{d}^2 u}{\mathrm{d} z^2} = \sum_{j=1}^{16} W_{2j}
\left[-2h_j\left(1-h_j^2\right)W_{1j}^2\right],$$

so no automatic differentiation is needed and the residual is exact to round-off.

| fit | error vs exact $u$ (L2 rms) | physics residual (rms) | boundary error (max) |
|---|---|---|---|
| physics only, no interior data | $2.40\times10^{-5}$ | $4.275\times10^{-3}$ | $6.629\times10^{-5}$ |
| data only, 5 noisy points | $0.0626$ | $4.220$ | $0.240$ |
| physics + data | $2\times10^{-4}$ | — | — |

The physics-only fit is accurate to better than one part in a thousand with **no
interior measurements at all**: the equation and the boundary conditions supply
essentially all the information. The network is a representation, not a source of
information.

## 3. Why the data-only fit is misleading

The data-only network fits the five points to $2.36\times10^{-6}$ rms — a
spectacular fit — and has L2 error 0.0626 against the exact solution, a physics
residual of 4.220 and a boundary error of 0.240. It is an interpolation with 65
parameters and 5 constraints: accurate where it was trained, meaningless between
the points, and not a solution of any equation.

The diagnostic order matters. The data misfit cannot distinguish the two fits;
the **physics residual and the boundary error** can, and they require no solution
values.

## 4. Failure mode: mis-specified physics

Solve the same problem with $f_{\text{wrong}} = 1.20\,f$:

| quantity | value |
|---|---|
| physics residual at the solution (rms) | $2.969\times10^{-2}$ |
| error against the **true** $u$ | $0.1411$ |
| recovered amplitude / true amplitude | $1.200$ |

The amplitude ratio is exactly 1.200, as the linearity of the equation requires.
The answer is smooth, satisfies the boundary conditions, and solves a well-posed
problem — **the wrong one**. Every internal diagnostic looks healthy, because the
network was asked to satisfy the wrong equation and did so.

A physics-informed network cannot detect a mis-specified equation. The only
defence is to test the physics against data it did not generate — a held-out
experiment, a different method, or a synthetic test with the *measured* source
term — which is exactly the discipline an empirical inversion already requires.

## 5. When is a PINN genuinely different?

- **As a forward solver** for a well-posed PDE, it is a collocation method in a
  neural basis: competitive or not depending on the problem, but not a different
  kind of information.
- **As an inverse method** it is most useful when the unknown is a *field*
  (a conductivity, a velocity, a source term) and the data are sparse or noisy:
  the equation then regularises the field, and the PINN shares that role with the
  classical PDE-constrained formulations.
- **It is different in cost profile**: training replaces a linear solve, and a
  new source term or boundary condition normally requires retraining.

## 6. Numeric demonstration

```bash
cd 18-inverse-problems/09-machine-learning-inversion/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python physics_informed_demo.py
```

Five sections: the BVP; the physics-only fit; the data-only fit; the combined
fit; the mis-specified-physics failure. Print-only, seeded, exits 0 in about two
seconds.

## 7. Assumptions and regime of validity

1. **The equation is right.** Section 4 is a measurement of what happens when it
   is not, and no internal diagnostic detects it.
2. **Collocation points cover the domain.** A PINN can satisfy a residual on a
   finite point set while violating the PDE between points; refine or randomise
   the points and check the residual is stable.
3. **The network can represent the solution.** A one-hidden-layer tanh network
   with 16 units is chosen here for speed; larger or stiffer problems need larger
   networks and, typically, domain decomposition.
4. **Boundary conditions are weighted.** $\beta$ is a weight, and an over-weighted
   boundary term hides interior error while an under-weighted one lets the
   solution drift. Report the boundary error separately.
5. **The cost profile differs.** Training must be repeated when the equation,
   source term or domain changes.

## Mastery checkpoint

Without notes: **(a)** Write the PINN loss for $-u''=f$ with Dirichlet
conditions and identify the weight $\beta$. **(b)** Derive the closed-form
second derivative of the one-hidden-layer network. **(c)** Given the three rows
of the comparison table, state which diagnostic separates the data-only fit from
the physics-only fit, and why the misfit does not. **(d)** Explain why a 20%
error in $f$ produces an amplitude ratio of exactly 1.200.

## Common pitfalls

1. **Reporting the physics residual as accuracy.** A small residual on a wrong
   equation is confidently wrong.
2. **Judging a fit by its data misfit.** Section 3.
3. **Under-weighting the boundary conditions.** The solution drifts and the
   interior residual can still look small.
4. **Claiming the method "needs no data" without stating the physics
   assumptions.** The equation is an input, with an error bar.
5. **Confusing a forward solver with an inverse method.** The information source
   is different; the terminology is not.

## Related modules

- [Learned Inversion: Direct and Iterative Networks](01-learned-inversion.md).
- [Generative Priors: GANs, VAEs, Diffusion Models](03-generative-models-inversion.md).
- [Uncertainty in Learned Inversion: Pitfalls and Calibration](04-uncertainty-in-learned-inversion.md).
- [18-04-01 Local Linearisation, Jacobians and Iteration](../04-nonlinear-inversion/01-local-linearization.md).

Code: [`code/physics_informed_demo.py`](code/physics_informed_demo.py).
Exercises: [`exercises/02-physics-informed-networks-exercises.md`](exercises/02-physics-informed-networks-exercises.md).
