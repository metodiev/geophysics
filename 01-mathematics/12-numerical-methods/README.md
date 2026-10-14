# Module 01-12 — Numerical Methods for Mathematical Problems

**Stage:** intermediate → graduate · **Prerequisites:**
[07 Linear Algebra](../07-linear-algebra/README.md) (elimination, conditioning,
eigenvalues, sparse structure), [09 Partial Differential Equations](../09-partial-differential-equations/README.md)
(consistency, stability and the CFL condition as subjects),
[05 Single-Variable Calculus](../05-single-variable-calculus/README.md) (Taylor
series, integration), [06 Multivariable and Vector Calculus](../06-multivariable-calculus/README.md)
(partial derivatives and multiple integrals) and
[08 Ordinary Differential Equations](../08-ordinary-differential-equations/README.md)
(stiff systems).

Every earlier module in this folder answers the question *what is the
mathematics of geophysics?* This one answers the question that actually decides
whether a project succeeds: **when the mathematics cannot be evaluated in closed
form, what do you compute instead, and how do you know the answer is right?**

The organising idea is that the whole of numerical analysis reduces to two
questions, asked of every algorithm:

> **Is it consistent, and is it stable?** Consistency says the algorithm
> approximates the right equation. Stability says the error does not grow.
> Together they imply convergence — but only for a linear problem, and only when
> both are checked.

| Lesson | The question it answers | The number that decides |
|---|---|---|
| 01 Root finding | Where is the zero of this function? | convergence order: 1, 1.618 or 2 |
| 02 Interpolation | What is the field between the samples? | node distribution and spline order |
| 03 Differentiation | How do I get a derivative from samples? | optimal step $h^\* \sim u^{1/2}$ or $u^{1/3}$ |
| 04 Integration | How do I integrate a function with no antiderivative? | quadrature order and node placement |
| 05 Linear solvers | How do I solve the system an inversion produces? | $\kappa$, and $\sqrt{\kappa}$ for CG |
| 06 ODE solvers | How do I march a forward model in time? | order, and the stability limit $2/\lambda$ |
| 07 PDE discretisation | Does my scheme converge at all? | the CFL condition and the amplification factor |
| 08 Eigenvalue problems | What are the principal axes and modes? | the ratio $\lambda_2/\lambda_1$ |

Each lesson states which model or geometry a formula assumes before applying it,
and every numerical claim in the module was produced by a script in `code/` that
uses the Python standard library only. Where a scheme was verified, the observed
convergence order is reported next to the error, because an error without an
order is not evidence.

## Learning objectives

By the end of this module you will be able to:

1. **Choose** a root-finding method from the information available — a bracket,
   a derivative, or neither — and predict its convergence order before running
   it, including the failure modes of Newton's method.
2. **Interpolate** irregularly sampled field data without inventing structure,
   selecting the node distribution and the interpolant for the job, and stating
   which orders apply to which window.
3. **Differentiate** numerical data while accounting for the three separate
   error sources — truncation, round-off and observation noise — and predict the
   optimal step from the order of the leading truncation term.
4. **Integrate** the anomaly of an arbitrary body by quadrature, choose between
   Newton–Cotes, Gauss and adaptive rules from the integrand's behaviour, and
   validate the result against a closed form or a limit.
5. **Distinguish** direct from iterative linear solvers, estimate the cost of
   each from the sparsity and the condition number, and say when
   preconditioning is the only remaining option.
6. **Implement** forward models as ODEs or PDEs with the right scheme for the
   problem's stiffness, and diagnose instability from the amplification factor
   rather than from the output.
7. **State and use** the Lax equivalence theorem: check consistency, check
   stability, then claim convergence — and know which of the three the CFL
   condition controls.
8. **Compute** a handful of eigenpairs of a large sparse operator with the
   power method, Lanczos or Arnoldi, and explain the loss of orthogonality that
   forces reorthogonalisation.

## Lessons

| # | Lesson | Level | Key idea |
|---|---|---|---|
| 01 | [Root Finding: Bisection, Newton, Secant and Robust Hybrids](./01-root-finding.md) | intermediate | A bracket buys certainty, a derivative buys order, and hybrids buy both |
| 02 | [Interpolation, Splines and Approximation Theory](./02-interpolation.md) | intermediate | Node distribution matters more than degree; the order you quote depends on the window |
| 03 | [Numerical Differentiation and Finite-Difference Stencils](./03-numerical-differentiation.md) | advanced | Truncation wants a small step, round-off wants a large one, and the optimum scales as $u^{1/2}$ or $u^{1/3}$ |
| 04 | [Numerical Integration: Trapezoid, Simpson, Gauss Quadrature](./04-numerical-integration.md) | advanced | The only way to validate a quadrature rule on a real body is a closed form or a limit |
| 05 | [Direct vs Iterative Linear Solvers and Convergence](./05-linear-solvers.md) | graduate | Sparsity is the structure; exploiting it is the whole game |
| 06 | [Numerical ODE Solvers: Euler, Runge-Kutta, Implicit and Adaptive](./06-ode-solvers.md) | graduate | Order and stability are different properties, and stiffness breaks both intuition and error estimators |
| 07 | [Discretising PDEs: Consistency, Stability, Convergence](./07-pde-discretisation.md) | graduate | Consistent plus stable means convergent; the CFL condition is the price of an explicit scheme |
| 08 | [Numerical Eigenvalue Problems (Power, Lanczos, Arnoldi)](./08-matrix-eigen-solvers.md) | graduate | Principal axes, normal modes and convergence rates are all one computation |

## Suggested path

**If you are following the mathematics folder in order:** lessons 01–04 form the
intermediate core and take roughly 12 hours with the exercises. Lesson 05 is the
bridge to everything numerical that follows and should not be skipped. Lessons
06–08 are graduate material and take another 14 hours. The whole module is
required before [19 Numerical Modeling and HPC](../../19-numerical-modeling-hpc/README.md)
and before the practical parts of [18 Inverse Problems](../../18-inverse-problems/README.md).

**If you are here from a geophysics application:**

| You are working on | Read |
|---|---|
| Hypocentre location and travel-time inversion | [01](./01-root-finding.md) §5, [05](./05-linear-solvers.md) §6 |
| Potential-field interpretation and field regularisation | [02](./02-interpolation.md) in full, [04](./04-numerical-integration.md) §6 |
| Gravity gradients, strain rates, edge detection | [03](./03-numerical-differentiation.md) in full |
| Anomalies of arbitrary bodies, terrain corrections | [04](./04-numerical-integration.md) in full |
| Inversion, tomography and solver performance | [05](./05-linear-solvers.md) in full, [08](./08-matrix-eigen-solvers.md) §5 |
| Thermal, hydrological and geodynamic forward models | [06](./06-ode-solvers.md) in full, [07](./07-pde-discretisation.md) §2 |
| Seismic, GPR and electromagnetic wave modelling | [07](./07-pde-discretisation.md) §3–4 |
| Stress tensors, normal modes, stability analysis | [08](./08-matrix-eigen-solvers.md) §5 |
| Scientific-computing practice | [03 Scientific Computing](../../03-scientific-computing/README.md) |

**If you already solve these problems numerically:** attempt ★★★9 of
[03](./03-numerical-differentiation.md) and ★★★9 of
[07](./07-pde-discretisation.md). If both come out cleanly, use the module as a
reference and go to [18 Inverse Problems](../../18-inverse-problems/README.md)
and [19 Numerical Modeling and HPC](../../19-numerical-modeling-hpc/README.md).

## Materials in this module

| Path | Contents |
|---|---|
| [`01-root-finding.md`](./01-root-finding.md) … [`08-matrix-eigen-solvers.md`](./08-matrix-eigen-solvers.md) | The eight lessons |
| [`exercises/`](./exercises) | One exercise set and one worked solution set per lesson |
| [`code/root_finding.py`](./code/root_finding.py) | Bisection, Newton, secant and a safeguarded hybrid; measured orders; Newton's two-cycle; a Murnaghan equation of state; hypocentre location from four arrival times |
| [`code/interpolation.py`](./code/interpolation.py) | Lagrange versus Newton forms; the Runge phenomenon on equispaced versus Chebyshev nodes; natural and clamped cubic splines with measured orders; a spline overshooting a step |
| [`code/numerical_differentiation.py`](./code/numerical_differentiation.py) | Stencil design orders; the truncation/round-off trade-off; the *measured* optimal-step exponents $u^{1/2}$ and $u^{1/3}$; Richardson extrapolation; a gravity gradient with and without noise |
| [`code/numerical_integration.py`](./code/numerical_integration.py) | Newton–Cotes orders; Gauss–Legendre exactness and convergence; Romberg columns; adaptive Simpson on a kink and its failure on an unsampled spike; the gravity of a sphere by 3-D quadrature |
| [`code/linear_solvers.py`](./code/linear_solvers.py) | LU with and without pivoting against exact rational arithmetic; Cholesky; Thomas versus dense cost; condition number of the Poisson matrix; Jacobi, SOR and CG iteration counts against theory |
| [`code/ode_solvers.py`](./code/ode_solvers.py) | Measured orders 1, 2, 4; the stability limit $2/\lambda$; A-stability and L-stability; adaptive step doubling that works and the stiff case where it fails; decay, cooling and a damped oscillator |
| [`code/pde_discretisation.py`](./code/pde_discretisation.py) | Von Neumann factors measured for FTCS heat, the leapfrog wave scheme and advection; the CFL limit; convergence orders; the central-difference instability |
| [`code/matrix_eigen_solvers.py`](./code/matrix_eigen_solvers.py) | Power iteration and its all-ones trap; Rayleigh quotient iteration and deflation; Jacobi rotations; Lanczos with and without reorthogonalisation; Arnoldi; stress axes, normal modes and a Jacobi spectral radius |

Every script runs with `python3 code/<script>.py` and imports nothing outside the
standard library. The numbers quoted in the lessons are the outputs of these
scripts.

## Mastery checkpoint

You have mastered this module when you can do all of the following unaided:

- [ ] State the convergence order of bisection, secant and Newton's method from
      memory and derive each from the Taylor expansion of the iteration.
- [ ] Describe a case where Newton's method cycles and explain what a bracketing
      safeguard does about it.
- [ ] Choose between linear interpolation, cubic splines and higher-degree
      polynomials for a given sampling pattern, and justify the choice from the
      node distribution rather than from habit.
- [ ] Predict the optimal step for a forward and a centred difference from the
      unit roundoff and the leading truncation term, and say which exponent
      belongs to which stencil.
- [ ] Derive the composite trapezoid and Simpson error terms from the Euler–Maclaurin
      expansion and state the degree of exactness of a Gauss rule.
- [ ] Estimate the condition number of a discretised operator from the grid
      spacing, and predict whether a direct or an iterative solver will be
      faster for a given problem size.
- [ ] Derive the amplification factor for a one-step scheme by substituting
      $u_i^n = G^n\mathrm{e}^{\mathrm{i}\theta i}$, and use it to state the
      stability condition.
- [ ] Explain why an explicit scheme for the heat equation forces
      $\Delta t \sim \Delta x^2$ while a leapfrog wave scheme only needs the
      Courant number bounded.
- [ ] Explain the difference between A-stability and L-stability, with the
      trapezoidal rule as the counterexample.
- [ ] Explain why the power method converges at $\lambda_2/\lambda_1$ for the
      eigenvector but at its square for the eigenvalue.
- [ ] Explain what the loss of orthogonality does to a Lanczos iteration and why
      reorthogonalisation is a requirement rather than a refinement.

## Common pitfalls across this module

1. **Quoting an error without an order.** "The error is $10^{-4}$" is not a
   verification; "the error falls as $h^{1.98}$" is. Every scheme in this module
   is validated by refining the grid and measuring the order.
2. **Refining a grid to fix an unstable scheme.** Stability is a property of the
   scheme and the step ratio, not of the step size alone. A central-difference
   advection scheme diverges for every step size.
3. **Conflating the two optimal-step exponents.** A forward difference has an
   optimal step proportional to $u^{1/2}$ and a centred difference to $u^{1/3}$,
   because the leading truncation terms are $O(h)$ and $O(h^2)$ respectively.
   Measured here as 0.48 and 0.33.
4. **Using a smooth interpolant on data that cannot be smooth.** A cubic spline
   overshoots a step by about 11% of the step, so porosity, concentration and
   monotone velocity logs need shape-preserving schemes.
5. **Believing that a small residual proves a small error.** The gap is the
   condition number, and for normal equations it is the *square* of the data
   condition number.
6. **Choosing an explicit method in a stiff regime.** The stability limit
   $h < 2/\lambda$ is not advisory; exceeding it produces growth at exactly
   $|1 - \lambda h|$ per step.
7. **Assuming an adaptive stepper always respects its tolerance.** Step doubling
   assumes a smooth local error model, and on a stiff transient the measured
   error exceeded the requested tolerance by factors of 45 to 4368, with the
   error falling only as $\mathrm{tol}^{0.5}$.
8. **Reading "unconditionally stable" as "unconditionally accurate".** Crank–Nicolson
   is stable at any step and second order, but a large step still leaves a large
   error, and it rings on stiff transients because it is not L-stable.
9. **Taking $\lambda_{\max}$ from a power iteration without checking the start
   vector.** An all-ones start on the Dirichlet Laplacian is orthogonal to every
   even mode and returns $\lambda_{n-1}$, not $\lambda_{\max}$.
10. **Trusting Lanczos without reorthogonalisation.** The basis loses
    orthogonality, converged Ritz values are reported several times, and the
    counting of the spectrum — not its extremes — is what fails.

## Related modules

- [07 Linear Algebra](../07-linear-algebra/README.md) — the prerequisite: the
  elimination, conditioning and eigen-analysis that this module turns into
  algorithms.
- [09 Partial Differential Equations](../09-partial-differential-equations/README.md)
  — the equations being discretised, and the first appearance of the CFL condition.
- [03 Scientific Computing](../../03-scientific-computing/README.md) — the
  practical setting for these algorithms: floating point, profiling and tests.
- [18 Inverse Problems](../../18-inverse-problems/README.md) — where the linear
  solvers and the condition number become the whole subject.
- [19 Numerical Modeling and HPC](../../19-numerical-modeling-hpc/README.md) —
  these schemes as they appear in production modelling codes, with parallel and
  domain-decomposition considerations.
- [14 Optimization](../14-optimization/README.md) — the same root-finding ideas
  generalised to minimisation.
- [21 Statistics and Bayesian ML](../../21-statistics-bayesian-ml/README.md) — the
  quadrature and sampling machinery applied to uncertainty propagation.
- [17 Remote Sensing and GIS](../../17-remote-sensing-gis/README.md) — the
  interpolation and resampling problems of lesson 02 in their data-science form.
