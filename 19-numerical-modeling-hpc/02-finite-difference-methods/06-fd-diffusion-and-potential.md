---
id: 19-02-06
title: "FD for Diffusion, Laplace and Poisson Problems"
level: doctoral
prereqs: ["19-02-01", "19-01-02", "19-02-04"]
tags: [numerical-modelling, hpc, poisson, laplace, diffusion, solvers, conditioning]
---

# FD for Diffusion, Laplace and Poisson Problems

Diffusion and potential problems are where finite differences meet numerical
linear algebra: the discretisation is short, and the difficulty moves into the
solver, the conditioning and the scaling with dimension. This lesson solves a
two-dimensional Poisson problem with a closed-form solution, checks the observed
order *and* the exact error constant, measures how the iteration count of two
solvers grows with resolution, and closes the loop with time-dependent diffusion
by recovering the analytic decay rate of the fundamental mode from a run. **All
models and data in this module are SYNTHETIC.** Every number quoted here is
printed by `code/fd_diffusion_and_potential_demo.py`.

## Learning objectives

By the end of this lesson you will be able to:

1. **Assemble** the five-point Laplacian in two dimensions and **solve** a Poisson
   problem whose exact solution is known.
2. **Predict** the constant in the $h^{2}$ error term from the truncation
   analysis of the stencil, and **verify** it against measured errors.
3. **Measure** the iteration counts of conjugate gradients and Jacobi against
   resolution and **explain** the exponents in terms of the condition number.
4. **Count** the unknowns, memory and step count of a three-dimensional problem
   before solving it, and **state** the resulting cost law.
5. **Recover** the diffusive timescale $1/(2\pi^{2}\alpha)$ of a mode from a
   time-dependent run and **identify** the bias that a first-order-in-time scheme
   adds.
6. **Decide** whether a diffusion problem is grid limited or timescale limited,
   and choose the scheme accordingly.

## Prerequisites

- [19-02-01 Deriving Finite-Difference Operators via Taylor Expansion](01-fd-derivation.md) —
  the second-derivative stencil and its truncation constant.
- [19-01-02 Truncation Error, Order of Accuracy and Convergence Rates](../01-numerical-foundations/02-convergence-and-error.md) —
  measured order and the constant that must be reported with it.
- [19-02-04 Explicit vs Implicit Time Stepping and Stability Limits](04-fd-time-stepping.md) —
  the time discretisation used in the last section.

## 1. Intuition: the stencil is the easy part

A Poisson solver is three lines of discretisation and a linear solve. The
interesting numbers are all in the solve:

- **Conditioning.** The five-point Laplacian has eigenvalues
  $\lambda_{jk} = -4h^{-2}[\sin^{2}(j\pi h/2)+\sin^{2}(k\pi h/2)]$, so its
  condition number grows as $h^{-2}$. Refining from $h = 1/32$ to $1/64$
  multiplies $\kappa$ by four.
- **Iteration count.** Conjugate gradients needs $O(\sqrt\kappa) = O(h^{-1})$
  iterations; Jacobi needs $O(\kappa) = O(h^{-2})$. Both were measured here, and
  the ratio of iteration counts grows with resolution in a way that no stencil
  improvement can change.
- **Dimension.** The step limit of an explicit diffusion scheme grows as
  $h^{2}/(2\alpha d)$, so a three-dimensional refinement costs $n^{5}$ overall.

The lesson's work is therefore mostly about *when* the solver becomes the
problem, measured rather than asserted.

## 2. Precise definitions

**Poisson problem (Dirichlet).** $-\nabla^{2}u = f$ in $\Omega$,
$u = g$ on $\partial\Omega$.

**Five-point Laplacian.** On a uniform 2-D grid with spacing $h$,

$$\nabla^{2}u \approx \frac{u_{i+1,j}+u_{i-1,j}+u_{i,j+1}+u_{i,j-1}-4u_{i,j}}{h^{2}},
\qquad \text{truncation } \frac{h^{2}}{12}\left(u_{xxxx}+u_{yyyy}\right)+O(h^{4}).$$

**Condition number.** $\kappa(A) = \lambda_{\max}/\lambda_{\min}$ for symmetric
positive definite $A$; it bounds the relative error amplification of the linear
solve and drives the cost of iterative methods.

**Jacobi iteration.** $x^{k+1} = x^{k} + D^{-1}(b - Ax^{k})$, with $D$ the
diagonal of $A$. Converges linearly with a rate governed by
$\kappa$.

**Conjugate gradients (CG).** Krylov method for symmetric positive definite
systems, converging in at most $n$ steps in exact arithmetic and in
$O(\sqrt\kappa)$ steps to a given tolerance in practice.

## 3. Derivations

### 3.1 The exact error constant of the five-point scheme

Take $\Omega = (0,1)^{2}$, $u = \sin(\pi x)\sin(\pi y)$, so
$f = 2\pi^{2}\sin(\pi x)\sin(\pi y)$ and $\nabla^{2}u = -2\pi^{2}u$. Apply the
five-point operator to the exact solution:

$$\mathsf L_h u = \nabla^{2}u + \frac{h^{2}}{12}\left(u_{xxxx}+u_{yyyy}\right)
+ O(h^{4}) = -2\pi^{2}u + \frac{h^{2}\pi^{4}}{6}u + O(h^{4}),$$

using $u_{xxxx}+u_{yyyy} = 2\pi^{4}u$. With $e = u - u_h$ and
$\mathsf L_h u_h = -f = -2\pi^{2}u_h$,

$$\mathsf L_h e = \frac{h^{2}\pi^{4}}{6}u + O(h^{4}).$$

Because both $u$ and $e$ are proportional to the same eigenmode,
$\mathsf L_h e \approx -2\pi^{2}e$, so

$$e \approx -\frac{h^{2}\pi^{2}}{12}u
\qquad\Longrightarrow\qquad
\max|e| \approx \frac{\pi^{2}}{12}h^{2} = 0.822467\,h^{2}.$$

This is an exact prediction. The demonstration solves the system with a sparse
direct solver for $n = 16, 32, 64, 128$:

| $n$ | $h$ | unknowns | $\max\lvert e\rvert$ | $\max\lvert e\rvert/h^{2}$ | observed order |
|---|---|---|---|---|---|
| 16 | 0.058824 | 256 | $2.826503\times10^{-3}$ | 0.816859 | — |
| 32 | 0.030303 | 1024 | $7.538815\times10^{-4}$ | 0.820977 | 1.90661 |
| 64 | 0.015385 | 4096 | $1.945758\times10^{-4}$ | 0.822083 | 1.95401 |
| 128 | 0.007752 | 16384 | $4.941827\times10^{-5}$ | 0.822369 | 1.97722 |

The constant column walks towards $0.822467$ from below while the observed order
walks towards 2 from below — the same behaviour seen in the one-dimensional
manufactured problem of
[19-01-02](../01-numerical-foundations/02-convergence-and-error.md), because it
is the same truncation term. An observed order of $1.977$ at $n = 128$ is not a
defect; it is what a second-order scheme looks like one decade away from the
asymptote.

### 3.2 Solver scaling, measured

Same grids, same operator, a Gaussian right-hand side (a single sine mode would
be an eigenvector and CG would solve it in one iteration, measuring nothing).
Iterations to a relative residual of $10^{-10}$:

| $n$ | unknowns | non-zeros | CG iterations | Jacobi iterations |
|---|---|---|---|---|
| 16 | 256 | 1 216 | 28 | 1 338 |
| 32 | 1 024 | 4 992 | 54 | 5 062 |
| 64 | 4 096 | 20 224 | 109 | 19 662 |

Measured growth exponents per halving of $h$: **CG 1.013**, **Jacobi 1.957**.
Both match the theory ($O(h^{-1}) = O(\sqrt\kappa)$ and $O(h^{-2}) = O(\kappa)$)
and the practical reading is stark. At $n = 64$ Jacobi needs $19\,662$ iterations
against CG's $109$; at $n = 256$ the extrapolated counts are $\sim3\times10^{5}$
against $\sim430$. The stencil is the same in both runs — **the solver decides
the run time**, and the cheapest improvement to a production code is usually the
one that changes the linear algebra rather than the discretisation.

### 3.3 Three dimensions: count first

The five-point stencil in $d$ dimensions has an explicit diffusion limit
$dt \le h^{2}/(2\alpha d)$. For a unit cube with $n$ cells per side:

| $n$ | unknowns | float64 field (MiB) | explicit steps to $t = 1$ |
|---|---|---|---|
| 50 | 125 000 | 1.0 | 31 212 |
| 100 | 1 000 000 | 7.6 | 122 412 |
| 200 | 8 000 000 | 61.0 | 484 812 |

Unknowns grow as $n^{3}$, steps as $n^{2}$, so a $4\times$ refinement costs
$4^{5} = 1024$ times the work. The memory column is exact arithmetic on the array
size and is the cheapest experiment available: a single float64 field at
$n = 200$ is already $61$ MiB, and an explicit scheme needs several copies. A
$400^{3}$ model is $488$ MiB per field and $3.9\times10^{6}$ steps — which is why
three-dimensional potential-field and thermal models are solved by multigrid or
implicitly, not by explicit marching.

### 3.4 Diffusion as a time-dependent problem

For $u_t = \alpha\nabla^{2}u$ with Dirichlet zeros the modes decay
independently: the fundamental mode $u = \sin(\pi x)\sin(\pi y)$ decays as
$e^{-2\pi^{2}\alpha t}$, with timescale

$$\tau = \frac{1}{2\pi^{2}\alpha} = 0.050661\ \text{s}\quad(\alpha = 1).$$

Marching with backward Euler at $dt = 10^{-3}$ s on a $32\times32$ grid and
measuring the maximum amplitude:

| $t$ | measured amplitude | exact $e^{-2\pi^{2}t}$ | ratio |
|---|---|---|---|
| 0.020 | $6.750877\times10^{-1}$ | $6.738255\times10^{-1}$ | 1.00187 |
| 0.040 | $4.567776\times10^{-1}$ | $4.540407\times10^{-1}$ | 1.00603 |
| 0.100 | $1.414942\times10^{-1}$ | $1.389111\times10^{-1}$ | 1.01859 |
| 0.200 | $2.006603\times10^{-2}$ | $1.929630\times10^{-2}$ | 1.03989 |

The decay rate is recovered, and the ratio drifts *upwards* — the measured
amplitude is larger than exact because backward Euler under-damps: its mode
amplification $1/(1+dt\lambda)$ exceeds $e^{-dt\lambda}$ for every $dt>0$, and
the gap is first order in $dt$. That is the same $O(dt)$ bias whose order was
measured in [19-02-04](04-fd-time-stepping.md), expressed this time as an
amplitude error at a fixed time. Two readings follow: the timescale recovered
here is a property of the *physics* and of the boundary conditions, not of the
scheme; and a one-per-cent amplitude error after four timescales is the price of
a first-order-in-time method on a problem whose exact answer is a pure
exponential.

## 4. Worked example: a steady geothermal problem, sized end to end

*A steady heat-conduction model over a $20\ \mathrm{km}\times20\ \mathrm{km}$
area with a conductivity of $2.5\ \mathrm{W\,m^{-1}\,K^{-1}}$, solved on a grid
with $h = 250$ m, Dirichlet temperatures on the boundaries. How long does the
solve take, and what limits the accuracy?*

1. Unknowns: $80\times80 = 6400$; the five-point matrix has
   $\mathrm{nnz} = 5n^{2} - 4n = 5(6400) - 4(80) = 31\,680$ non-zeros, against
   $4.1\times10^{7}$ for a dense matrix of the same size.
2. Conditioning: $\kappa \sim \pi^{-2}(2/h^{2}) = 2\times(250)^{-2}/9.87$ in the
   model units — with $L = 20$ km and $h = 0.25$ km this gives
   $\kappa \sim 3.2\times10^{5}$, which for CG predicts
   $O(\sqrt\kappa)\approx570$ iterations.
3. Method: with $\kappa = 3\times10^{5}$ a direct sparse solve is entirely
   feasible on this grid; CG with an incomplete-Cholesky preconditioner is the
   alternative if the grid grows by a factor of ten in each direction.
4. Accuracy: the truncation constant is $\pi^{2}/12$ in the unit-square scaling,
   so on this domain the relative error at $h = 0.25$ km is
   $O(0.82\,(h/20)^{2}) = 1.3\times10^{-4}$ — well below the uncertainty of the
   conductivity, which is the real limit.
5. The honest conclusion: on this problem the discretisation error is not the
   limiting factor, the rock properties are. Reporting a four-digit temperature
   from a model whose conductivity is known to $20\,\%$ is a false precision, and
   recognising it here costs nothing.

## 5. Assumptions and regime of validity

1. **Uniform grid, isotropic operator, Dirichlet boundaries.** Neumann conditions
   change the smallest eigenvalue and lower $\kappa$; anisotropy of the medium
   raises it; both change the iteration counts measured here.
2. **The error constant belongs to this eigenmode.** For a general right-hand
   side the error is still $O(h^{2})$ but the constant varies with the local
   derivatives; only for the single-mode problem is it a clean number.
3. **CG assumes symmetric positive definiteness.** A nonsymmetric advection
   operator (or a strongly variable coefficient discretised asymmetrically) needs
   GMRES or BiCGStab, and the $O(\sqrt\kappa)$ law is then only indicative.
4. **Iteration counts depend on the tolerance and the preconditioner.** The
   numbers above are for unpreconditioned methods at $10^{-10}$; a good
   preconditioner can change them by an order of magnitude and reduce the
   exponent.
5. **The diffusion timescale is set by the domain and the mode.** $\tau =
   1/(2\pi^{2}\alpha)$ is for a unit square with Dirichlet zeros and the
   fundamental mode; a different geometry or a Neumann boundary changes both the
   constant and the slowest mode, and the slowest mode is what a thermal model
   must be run to.
6. **Explicit step counts assume $d$-dimensional isotropy.** On a stretched grid
   (small $h$ in one direction, large in another) the limit is set by the
   *smallest* spacing, so the step count can be far worse than the $n^{2}$ law
   suggests.

## 6. Python demonstration

`code/fd_diffusion_and_potential_demo.py` prints:

1. the two-dimensional Poisson convergence table with the measured constant
   approaching $\pi^{2}/12 = 0.822467$;
2. CG against Jacobi iteration counts with the measured growth exponents 1.013
   and 1.957;
3. the three-dimensional storage and step-count arithmetic;
4. the backward-Euler march of a diffusing mode against its exact exponential,
   with the measured first-order damping bias.

```bash
cd 19-numerical-modeling-hpc/02-finite-difference-methods/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python fd_diffusion_and_potential_demo.py
```

## Mastery checkpoint

Without notes:

> A 2-D steady potential problem is solved on a $200\times200$ grid with the
> five-point Laplacian. **(a)** State the truncation order and the constant for
> the single-mode test problem. **(b)** Estimate the condition number and the
> number of CG iterations for a $10^{-10}$ residual, and compare with Jacobi.
> **(c)** A colleague halves $h$ in both directions and reports that the run takes
> ten times longer: state the expected total cost factor and suggest where they
> went wrong. **(d)** State one circumstance in which refining this grid would
> not improve the answer.

Parts (a)–(c) are worked in
[`exercises/06-fd-diffusion-and-potential-solutions.md`](exercises/06-fd-diffusion-and-potential-solutions.md).

## Common pitfalls

1. **Reporting the order without the constant.** Here the constant is
   $\pi^{2}/12$ exactly, and it is what tells you the resolution you need.
2. **Choosing the stencil and ignoring the solver.** Iteration counts differ by
   two orders of magnitude at $n = 64$ for the same matrix.
3. **Benchmarking CG on a single eigenmode.** One mode is solved in one
   iteration; use a right-hand side with a broad spectrum.
4. **Assuming $O(n^{3})$ is the whole cost in 3-D.** The step count adds $n^{2}$,
   and memory adds a hard ceiling.
5. **Trusting a first-order-in-time decay.** Backward Euler under-damps by
   $1\,\%$ after four timescales at $dt = 10^{-3}$ here; the bias is systematic,
   not noise.
6. **Confusing the diffusive timescale with the run time.** The timescale is
   physics; the run time is a scheme-and-hardware question.

## Related modules

- [19-02-05 Finite-Difference Acoustic and Elastic Wave Propagation](05-fd-wave-propagation.md) —
  the wave counterpart of the same discretisations.
- [19-01-02 Truncation Error, Order of Accuracy and Convergence Rates](../01-numerical-foundations/02-convergence-and-error.md) —
  the manufactured-problem technique used in §3.1.
- [01-12-05 Direct vs Iterative Linear Solvers and Convergence](../../01-mathematics/12-numerical-methods/05-linear-solvers.md) —
  the solver theory behind the measured exponents.
- [01-09-04 Laplace and Poisson Equations in Earth Systems](../../01-mathematics/09-partial-differential-equations/04-laplace-poisson.md).
- [Module 19-02 Finite-Difference Methods](README.md).

Exercises and worked solutions:
[`exercises/06-fd-diffusion-and-potential-exercises.md`](exercises/06-fd-diffusion-and-potential-exercises.md)
and
[`exercises/06-fd-diffusion-and-potential-solutions.md`](exercises/06-fd-diffusion-and-potential-solutions.md).
