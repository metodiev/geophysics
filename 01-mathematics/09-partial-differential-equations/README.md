# Module 01-09 — Partial Differential Equations

**Stage:** advanced → doctoral · **Prerequisites:**
[06 Multivariable and Vector Calculus](../06-multivariable-calculus/README.md)
(partial derivatives, the integral theorems, Green's identities, potential
theory), [05 Single-Variable Calculus](../05-single-variable-calculus/README.md)
(ordinary differential equations, Fourier series),
[07 Linear Algebra](../07-linear-algebra/README.md) (eigenvalues, orthogonality,
symmetric positive definite systems).

This module is where the mathematics of geophysics stops being a description of
fields and becomes a description of *processes*. The single most useful
organising idea in the whole subject is here, and it is one line long:

> **The three canonical PDEs are the three families of geophysical measurement.**

| Class | Prototype | Geophysical family | What the data can see |
|---|---|---|---|
| Elliptic | $\nabla^2V = -4\pi G\rho$ | gravity, magnetics, DC resistivity, self-potential, steady groundwater flow | amplitudes of a smooth, non-unique functional of the source |
| Parabolic | $u_t = \kappa\nabla^2u$ | heat flow, palaeoclimate, pore pressure, induced seismicity, aquifer response, EM induction | decay and depth, with $\tau \sim L^2/\kappa$ and no arrival times |
| Hyperbolic | $u_{tt} = c^2\nabla^2u$ | seismic body and surface waves, GPR, acoustic logging, normal modes | travel times, phases and amplitudes — sharp, invertible constraints |

Every lesson derives its mathematics from a physical conservation statement,
verifies its solutions by substitution, and then measures something numerically
against an exact solution. Nothing is presented as an abstract exercise: the
diffusive timescale *is* the reason a 100 km lithosphere cannot have equilibrated
in 100 Myr, the CFL condition *is* the reason a seismic modelling job either runs
or explodes, and the uniqueness theorem for the Dirichlet problem *is* the reason
potential-field inversion has a null space.

## Learning objectives

By the end of this module you will be able to:

1. **Classify** a second-order linear PDE from its principal part, and say which
   data it requires, how informative those data can be, and what the numerical
   method must therefore be.
2. **Derive** the diffusion and wave equations from conservation plus a
   constitutive law, obtaining the diffusivity and the wave speed from material
   parameters, and state the assumption each derivation rests on.
3. **Compute** diffusive timescales $\tau \sim L^2/\kappa$ and electromagnetic
   skin depths $\delta = \sqrt{2/(\omega\mu\sigma)}$ for real survey parameters,
   and use them to design or critique an experiment.
4. **Verify** a proposed solution by substitution, and verify a numerical scheme
   against an exact solution by reporting an observed convergence order.
5. **Derive** the CFL condition from both the domain of dependence and a von
   Neumann analysis, and predict the growth rate when it is violated.
6. **State and use** the properties of harmonic functions, the uniqueness theorems
   for the elliptic boundary-value problems, and the precise sense in which
   potential-field inversion is nevertheless non-unique.
7. **Solve** initial-boundary value problems by separation of variables and by
   characteristics, including the breaking of a nonlinear wave into a shock.
8. **Formulate** a problem weakly, assemble and solve it by Galerkin methods,
   derive an adjoint with its boundary terms, and explain the ill-posedness of
   derivative-based inversion and what regularisation assumes in its place.

## Lessons

| # | Lesson | Level | Key idea |
|---|---|---|---|
| 01 | [Classification of PDEs: Elliptic, Parabolic, Hyperbolic](./01-classification.md) | advanced | The discriminant of the principal part sorts every geophysical measurement into three families |
| 02 | [The Diffusion/Heat Equation and Diffusive Timescales](./02-heat-equation.md) | advanced | One equation, four subdisciplines, and the timescale $\tau \sim L^2/\kappa$ |
| 03 | [The Wave Equation and Its Physical Content](./03-wave-equation.md) | advanced | Finite speed, d'Alembert's two families, and the CFL condition that the grid must respect |
| 04 | [Laplace and Poisson Equations in Earth Systems](./04-laplace-poisson.md) | advanced | Harmonic functions make the problem rigid, and that rigidity is what makes inversion ambiguous |
| 05 | [Separation of Variables and Boundary Conditions](./05-separation-of-variables.md) | advanced | Eigenvalues from the boundary conditions; amplitudes from the data |
| 06 | [Method of Characteristics and First-Order PDEs](./06-characteristics.md) | graduate | Information travels along one family; nonlinearity makes it break |
| 07 | [Boundary and Initial-Boundary Value Problems](./07-boundary-value-problems.md) | graduate | Well posed or not — counting conditions, proving stability, and failing the third Hadamard test |
| 08 | [Weak Solutions, Variational Forms and Well-Posedness](./08-weak-solutions.md) | doctoral | Ask for less and get more: Galerkin methods, Lax–Milgram, adjoints and regularisation |

## How to work through the module

**If you are following the mathematics folder in order:** all eight lessons, in
order, with the exercises. Lessons 01–04 are the core and take roughly 12–16
hours with the exercises. Lessons 05–07 add the solution techniques and take
another 10 hours. Lesson 08 is doctoral-level analysis and may be taken later;
it is required before [16 Functional Analysis](../16-functional-analysis/README.md)
and is the natural starting point for [18 Inverse Problems](../../18-inverse-problems/README.md).

**If you are here from a geophysics application:**

| You are working on | Read |
|---|---|
| Gravity, magnetics, DC resistivity, steady flow | [01](./01-classification.md) §4.1, [04](./04-laplace-poisson.md) in full, [08](./08-weak-solutions.md) §6–7 |
| Heat flow, palaeoclimate, geothermal | [01](./01-classification.md) §4.2, [02](./02-heat-equation.md) §4.1, [05](./05-separation-of-variables.md) §5 |
| Induced seismicity, reservoirs, hydrology | [02](./02-heat-equation.md) §4.2–4.3, [06](./06-characteristics.md) §6 |
| Seismology, GPR, acoustic methods | [01](./01-classification.md) §4.4, [03](./03-wave-equation.md) in full, [07](./07-boundary-value-problems.md) §7.3 |
| Modelling code development | [03](./03-wave-equation.md) §5, [07](./07-boundary-value-problems.md) §7, [08](./08-weak-solutions.md) §8 |
| Inversion and uncertainty | [04](./04-laplace-poisson.md) §5, [07](./07-boundary-value-problems.md) §6, [08](./08-weak-solutions.md) §6–7 |

**If you already solve PDEs numerically:** attempt ★★★9 of
[03](./03-wave-equation.md) and ★★★9 of [08](./08-weak-solutions.md) first. If
both come out cleanly, use the module as a reference and go directly to
[12 Numerical Methods](../12-numerical-methods/README.md) and
[18 Inverse Problems](../../18-inverse-problems/README.md).

## Mastery checkpoint

You have mastered this module when you can do all of the following unaided:

- [ ] Classify an unfamiliar second-order PDE, state which data it needs, and say
      whether its solution smooths, propagates or equilibrates.
- [ ] Derive the diffusion equation from conservation and Fourier's law, and
      derive $\tau \sim L^2/\kappa$ from the fundamental solution rather than
      quoting it.
- [ ] Compute a thermal, hydraulic and electromagnetic timescale or depth for a
      stated set of parameters, and say which of the three you are computing.
- [ ] Verify a solution by substitution and verify a scheme against an exact
      solution, reporting an observed convergence order and its significance.
- [ ] Derive the CFL condition for an explicit scheme and predict the growth rate
      above the limit.
- [ ] Prove uniqueness for the Dirichlet problem, and state exactly why that
      theorem does not make potential-field inversion unique.
- [ ] Solve an initial-boundary value problem by separation of variables, including
      a non-homogeneous boundary condition handled by steady-state subtraction.
- [ ] Solve a first-order transport problem by characteristics, and compute the
      breaking time and post-breaking gradient of a nonlinear conservation law.
- [ ] Count the boundary conditions each class requires from the characteristics,
      and implement a derivative condition to second order with a ghost node.
- [ ] Write a weak formulation, assemble it, and explain why a finite-element
      solution has one convergence order in $L^2$ and another in the energy norm.
- [ ] Derive an adjoint with its boundary terms and test the adjoint identity on a
      discretisation.
- [ ] Explain ill-posedness through the singular spectrum and say what a
      regularisation parameter assumes in place of missing information.

## A note on verification

Every numerical result quoted in this module was produced by the scripts in
`code/`, which use the Python standard library only and can be run directly
(`python3 code/<script>.py`) with no packages installed. Where a scheme was
verified, the observed convergence order is reported next to the error, because an
error without an order is not evidence. Where a claim could not be verified — because it depends on a parameter
that varies between sites, or on a value the author could not check — the lesson
says so rather than supplying a number.

## Related modules

- [06 Multivariable and Vector Calculus](../06-multivariable-calculus/README.md) —
  the prerequisite: gradients, the integral theorems, and the potential theory
  that this module generalises.
- [10 Fourier Analysis and Spectral Methods](../10-fourier-analysis/README.md) —
  the transform machinery behind the eigenfunction expansions of lesson 05.
- [11 Complex Analysis](../11-complex-analysis/README.md) — the Laplace transform
  for transient problems and dispersion relations for wave physics.
- [12 Numerical Methods for Mathematical Problems](../12-numerical-methods/README.md)
  — consistency, stability and convergence as a subject.
- [16 Functional Analysis for Inverse Problems](../16-functional-analysis/README.md)
  — the rigorous setting for weak solutions and ill-posedness.
- [18 Inverse Problems](../../18-inverse-problems/README.md) — what to do when the
  problem is not well posed.
- [19 Numerical Modeling and HPC](../../19-numerical-modeling-hpc/README.md) —
  these equations as they appear in production modelling codes.
- [02 Physics for Geophysics](../../02-physics/README.md) — the physical
  derivations of $c$, $\kappa$ and the boundary conditions.
- [06 Seismology](../../06-seismology/README.md) — the wave equation in its
  natural habitat.
