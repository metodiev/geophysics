# Module 19-03 — Finite Element and Finite Volume Methods

**Stages:** research · **Prerequisites:** modules 19-01 and 19-02, the
PDE sequence in 01-09, and 03-12.

**All models and data in this module are SYNTHETIC.** Every coefficient, mesh,
manufactured solution and reference value is a chosen teaching model or an exact
closed form, and every number quoted in the lessons is printed by the
demonstration named in that lesson. No external finite-element package is used:
the element matrices, quadrature rules and assembled systems are built with NumPy
and SciPy so that the reader can inspect every line that produces a number.

This module is about the two discretisation families that dominate geophysical
forward modelling once the geometry stops being a rectangle. Finite elements
build the discrete equations from a **weak form** — an integral statement of the
problem — and choose a space of piecewise polynomials to represent the solution
in. Finite volumes build them from a **flux balance** over cells. The two views
answer different questions, and the interesting content of the module is the
comparison: a weak form handles a variable coefficient without any special
treatment and is optimal in the energy norm, while a flux form conserves a total
*exactly* and forces the modeller to decide what happens at a face. Several
lessons measure both and report which property each method actually delivers.

Three ideas recur, and each is measured rather than asserted. First, **order of
accuracy is a measurement, not a label**: every convergence table in this module
prints per-step orders beside the fitted one, because the first refinement always
underestimates the asymptote. Second, **the error norm is part of the
experiment**: a method can be nodally exact and second order in $\mathrm{L}^2$
while its gradient error is only first order, and a report that quotes one number
has silently chosen a question. Third, **the linear algebra is part of the
method**: the assembled matrix is sparse with $O(\mathrm{ndof})$ non-zeros, but
its condition number grows as $h^{-2}$ and the cost of solving it — iterations,
fill-in, ordering — is where most of the practical effort goes.

## Learning objectives

By the end of this module you will be able to:

1. **Convert** a classical boundary-value problem into a weak form, **classify**
   its boundary conditions as essential or natural, and **state** what each
   classification costs.
2. **Derive** the element stiffness and mass matrices of linear, quadratic and
   bilinear elements, **choose** a quadrature rule from the element order and the
   coefficient degree, and **measurably verify** both.
3. **Measure** the $\mathrm{L}^2$ and $\mathrm{H}^1$ convergence orders of
   Lagrange elements of order $p = 1, 2, 3$ and **explain** the $p+1$ and $p$
   pattern with a Taylor argument.
4. **Assemble** a two-dimensional system, **verify** it against an independent
   construction, and **quantify** its sparsity, conditioning, Krylov iteration
   count and factorisation fill-in.
5. **Derive** the conservative finite-volume update, **prove** its exact
   conservation by telescoping, and **measure** both the numerical diffusion of
   the upwind flux ($a\Delta x(1-C)/2$) and the boundary-speed error of a
   non-conservative discretisation of Burgers' equation.
6. **Choose** between harmonic and arithmetic face coefficients, and **state** the
   measured consequence of getting it wrong across a discontinuity.
7. **Apply** the same machinery to a magnetotelluric, a Stokes and a
   seismic site-response problem, and **verify** each against an exact closed
   form rather than against another code.

## Prerequisites

- [19-01 Numerical Foundations for Simulation](../01-numerical-foundations/README.md) —
  grids, degrees of freedom, truncation error and the meaning of "order".
- [19-02 Finite-Difference Methods](../02-finite-difference-methods/README.md) —
  the stencil view of the same operators, and the boundary conditions this module
  contrasts with.
- [01-09 Partial Differential Equations](../../01-mathematics/09-partial-differential-equations/README.md) —
  the equations being discretised, including the weak/variational setting.
- [03-12 Building Numerical Simulation Code in Python](../../03-scientific-computing/12-numerical-simulation-python/README.md) —
  the refinement-study practice used in every measurement here.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Weak Formulation and the Galerkin Method](01-fem-weak-form.md) | research | Integration by parts moves the derivative onto the test function; "leaving a node free" is a flux condition, and harmonic face coupling is exact where the arithmetic mean is first order |
| 02 | [Element Types, Shape Functions and Quadrature](02-fem-element-types.md) | research | The basis is determined by its nodes; quadrature is chosen by degree count; measured orders are $p+1$ and $p$, and one quadrature point can make an element singular |
| 03 | [Assembly, Sparsity and Linear System Structure](03-fem-assembly.md) | research | The assembled matrix is sparse but ill-conditioned; $\mathrm{cond} = O(h^{-2})$, CG iterations grow as $h^{-1}$, and ordering changes the factorisation |
| 04 | [Finite Volume Methods and Conservative Discretisation](04-finite-volume.md) | research | One flux per face conserves the total exactly; upwind is dissipative by a measured amount, Lax–Wendroff is dispersive, and only the flux form gets a shock speed right |
| 05 | [FEM in Geophysics: EM, Geodynamics and Seismology](05-fem-geophysics.md) | research | The same elements solve a diffusive, a viscous and an elastic problem, each verified against an exact closed form and a conservation identity |

## Suggested path

**If you are new to finite elements:** lessons 01–02 in order, running each
demonstration. Lesson 01, Section 6 is where the finite-volume idea first
appears, and it is the natural bridge to lesson 04.

**If you already use a finite-element package:** read lesson 01 §3 (Céa and
nodal exactness, and why the second does not survive in 2-D), then lesson 03 §5–8
for the cost structure, then lesson 04 for the conservation comparison.

**If you are preparing a research project:** lessons 01 §6, 04 §1–5 and 05 in
full, plus the ★★★ exercises, which ask for measurement designs rather than
calculations.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-fem-weak-form.md`](01-fem-weak-form.md) | Lesson 01 |
| [`02-fem-element-types.md`](02-fem-element-types.md) | Lesson 02 |
| [`03-fem-assembly.md`](03-fem-assembly.md) | Lesson 03 |
| [`04-finite-volume.md`](04-finite-volume.md) | Lesson 04 |
| [`05-fem-geophysics.md`](05-fem-geophysics.md) | Lesson 05 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Five runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy and SciPy:

```bash
cd 19-numerical-modeling-hpc/03-finite-element-and-volume/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python fem_weak_form_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python fem_element_types_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python fem_assembly_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python finite_volume_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python fem_geophysics_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), exits 0, and takes well under 20 s on a
laptop. They are print-only: no plots, no files, no network.

## Mastery checkpoint

Complete this without notes:

> A two-dimensional Q1 model of a unit square uses $n = 64$ cells per side with
> homogeneous Dirichlet data. **(a)** State the number of unknowns and the number
> of non-zeros. **(b)** State the measured condition-number law and predict
> $\mathrm{cond}$ at $n = 128$. **(c)** Predict how the unpreconditioned CG
> iteration count changes, and explain why Jacobi preconditioning does nothing
> here. **(d)** A separate one-dimensional calculation has a coefficient of 1 for
> $x<1/2$ and $10^6$ for $x>1/2$, with the interface on a face; state which face
> coefficient is exact and give the measured error of the other. **(e)** State
> which of the two methods in this module conserves its discrete total exactly,
> and why.

A worked version of (a)–(c) appears in the
[lesson-03 solutions](exercises/03-fem-assembly-solutions.md); (d) is in the
[lesson-01 solutions](exercises/01-fem-weak-form-solutions.md).

## Common pitfalls across this module

1. **Treating a free boundary node as "no condition".** It is a flux condition,
   and the measured consequence is a solution differing by $\pi x$.
2. **Quoting an order against the wrong norm.** Nodal, $\mathrm{L}^2$ and
   $\mathrm{H}^1$ errors differ by a whole order on the same run.
3. **Under-integrating an element.** A single quadrature point makes the
   quadratic element matrix *singular*, and a partially degenerate rule returns a
   plausible wrong answer instead of an error.
4. **Assuming the assembly is right because it is symmetric.** Symmetry and
   positive definiteness survive a transposed node ordering; an independent
   construction does not.
5. **Preconditioning by reflex.** Jacobi on a uniform Q1 mesh is exactly the
   identity operation.
6. **Averaging transport coefficients at faces.** Arithmetic averaging gives a
   first-order error that refining cannot remove.
7. **Discretising a conservation law in advective form.** The measured outcome is
   43% of the mass deleted in 200 steps and a Burgers shock that does not move.
8. **Reporting a manufactured-solution agreement as validation.** It verifies the
   code, not the physics.

## Related modules

- [19-04 Spectral and Pseudospectral Methods](../04-spectral-and-pseudospectral/README.md) —
  the other way to raise the order of a scheme.
- [19-05 Integral Equation and Boundary Methods](../05-integral-equation-and-boundary-methods/README.md) —
  what to do when the operator of interest is dense by nature.
- [19-06 High-Performance and Parallel Computing](../06-hpc-and-parallel-computing/README.md) —
  how the assembled matrix is partitioned and solved at scale.
- [19-07 Verification, Validation and Numerical Uncertainty](../07-verification-validation-uncertainty/README.md) —
  the systematic version of the checks used throughout this module.
- [19-08 Geophysical Simulation Case Studies](../08-geophysical-simulation-case-studies/README.md) —
  where these elements are used on production problems.
- [13-05 Geodynamic Modelling Practice](../../13-geodynamics-tectonics/05-geodynamic-modelling/README.md) —
  finite elements in their geodynamical setting.
- [01-16 Functional Analysis for Inverse Problems](../../01-mathematics/16-functional-analysis/README.md) —
  the theory behind the weak form and Céa's lemma.
