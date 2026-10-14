# Module 19-05 — Integral Equation and Boundary Methods

**Stages:** research · **Prerequisites:** modules 19-01 and 19-02; the Poisson
and Laplace equations; acquaintance with an inverse problem.

This module reformulates a field problem as an integral over sources. The
motivation is practical rather than aesthetic: an integral formulation needs no
artificial outer boundary for an unbounded domain, reduces a 2-D area integral to
a 1-D boundary integral, and represents localised or sheet-like targets with
sources on a surface rather than nodes in a volume. The price is a **dense**
operator, and often an **ill-conditioned** one, and both of those are properties
of the equation rather than of the code.

All models and data in this module are **SYNTHETIC**. The bodies, boundaries,
kernels and test fields are chosen teaching values. Nothing here is a measurement
of the Earth, and no published benchmark value is quoted.

The module is organised around one discipline: **a representation is accepted
only when an independent evaluation agrees with it.** A Poisson-equation residual,
a Richardson extrapolation checked against a second extrapolation, an FFT inverse
checked against a sparse solve, a tree code checked against a direct sum — every
lesson ships the measurement that would have caught the mistake. Two of them did:
the Green's function demo's lumped-source error and the tree code's alternating
sign were both found this way, and both are kept in the shipped code with their
measured consequences printed.

## Learning objectives

By the end of this module you will be able to:

1. **Derive** a volume-integral representation of a potential field and verify it
   against the Poisson equation by numerical differentiation.
2. **Reduce** an area integral to a boundary integral with the divergence theorem
   and **measure** the accuracy per unknown that it buys, and does not buy.
3. **Assemble** and solve a constant-panel boundary integral equation, recover the
   free term from the discrete row sums, and handle the exterior problem.
4. **Classify** a Fredholm equation as first or second kind and **predict** its
   conditioning, then confirm it with a refinement table.
5. **Construct** numerical Green's functions by inverting a discrete operator and
   **quantify** the relation between them and the closed-form kernels.
6. **Build** a hierarchical far-field expansion and **measure** its geometric
   convergence, its interaction counts and its implementation cost.

## Prerequisites

- [19-01-01 Discretisation: Grids, Nodes, Cells and Degrees of Freedom](../01-numerical-foundations/01-discretisation-concepts.md) —
  what it means to choose unknowns.
- [19-01-02 Truncation Error, Order of Accuracy and Convergence Rates](../01-numerical-foundations/02-convergence-and-error.md) —
  the refinement table is the only accepted evidence of order in this module.
- [19-02-06 FD for Diffusion, Laplace and Poisson Problems](../02-finite-difference-methods/06-fd-diffusion-and-potential.md) —
  the differential formulation every integral formulation is compared against.
- [03-12 Building Numerical Simulation Code in Python](../../03-scientific-computing/12-numerical-simulation-python/README.md) —
  the measurement habit and the tooling this module inherits.
- [01-12 Numerical Methods](../../01-mathematics/12-numerical-methods/README.md) —
  quadrature, root finding and linear algebra at the level used here.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Volume and Surface Integral Equations](01-integral-equations.md) | research | A representation is verified against the equation it came from; first-kind systems are ill-posed before you discretise them |
| 02 | [Boundary Element Methods for Potential Fields](02-boundary-element.md) | research | The free term is measurable from the row sums, the sign of it decides interior from exterior, and in 2-D the volume grid is often the better tool |
| 03 | [Numerical Green's Functions and Their Computation](03-greens-function-numerics.md) | research | Where the delta goes decides between roundoff and first-order error; a kernel on a periodic grid is a sum over images |
| 04 | [Fast Multipole and Hierarchical Acceleration](04-fast-multipole.md) | research | Moments, an admissibility test, geometric convergence — and a measured reminder that counts are not timings |

## Suggested path

**If you are new to integral methods:** lessons 01 and 02 in order, running both
demos. Lesson 01 §3 is where the boundary reduction is derived and measured;
lesson 02 §5 is where the boundary method is shown *not* to win in 2-D.

**If you already know boundary elements:** read 01 §4–5 (Fredholm classes and
conditioning), then 03 §3 (where the delta goes) and 04.

**If you are preparing a research project:** 02 §7 (assumptions), 03 §4–5
(periodic images and the additive constant), and 04 §5 (what counts do and do not
predict), plus the ★★★ exercises.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-integral-equations.md`](01-integral-equations.md) | Lesson 01 |
| [`02-boundary-element.md`](02-boundary-element.md) | Lesson 02 |
| [`03-greens-function-numerics.md`](03-greens-function-numerics.md) | Lesson 03 |
| [`04-fast-multipole.md`](04-fast-multipole.md) | Lesson 04 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Four runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
SymPy:

```bash
cd 19-numerical-modeling-hpc/05-integral-equation-and-boundary-methods/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python integral_equations_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python boundary_element_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python greens_function_numerics_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python fast_multipole_demo.py
```

Every demo prints labelled results with units, uses the fixed seed
`np.random.default_rng(20261014)`, requires no network access, starts no
subprocess and no long-lived thread pool, and exits 0. The slowest of the four
runs in about eight seconds.

## Mastery checkpoint

Complete this without notes:

> A uniform 2-D rectangle $12\ \mathrm{km}\times6\ \mathrm{km}$ with
> $\rho = 2600\ \mathrm{kg\,m^{-3}}$ has a monopole strength
> $2G\rho A = 2.498858\times10^{1}\ \mathrm{m^{2}\,s^{-2}}$, and its field at
> $30$ km is measured as $8.413406\times10^{-4}\ \mathrm{m\,s^{-2}}$ against a
> monopole estimate of $8.329526\times10^{-4}\ \mathrm{m\,s^{-2}}$. **(a)** State
> what the $1.007$ ratio measures and how it decays with distance. **(b)** The
> same kernel is used in a first-kind equation whose condition number grows with
> $n$; state what happens to the solution error and why refining is not a remedy.
> **(c)** A boundary-element code reports a row sum of $-0.48437500$; state how
> many panels it has and which free term its assembly implies.

A worked version of (a)–(c) appears in the lesson-01 and lesson-02
[solutions](exercises/02-boundary-element-solutions.md).

## Common pitfalls across this module

1. **Quoting agreement without naming what limited it.** Every comparison in this
   module states which of the two routes set the residual.
2. **Discretising a first-kind equation more finely.** It makes the conditioning
   worse; the data residual can fall while the solution error grows.
3. **Fixing a sign convention by memory.** The $2\pi$, the $4\pi$ and the factor
   $2$ in the 2-D log potential are one consistent set, and the free term's sign
   decides interior from exterior.
4. **Putting the delta wherever it is convenient.** Site, hat and lumped
   representations differ by roundoff against first order.
5. **Treating a periodic kernel as a free-space kernel.** Whether the images
   matter is a question of $\kappa L$, and the demonstration measures both
   regimes.
6. **Reporting an interaction count as a speedup.** The counts show an algorithm;
   the times show an implementation, and in the shipped demo they disagree.

## Related modules

- [19-01 Numerical Foundations for Simulation](../01-numerical-foundations/README.md) —
  discretisation, order and stability, the vocabulary this module assumes.
- [19-02 Finite-Difference Methods](../02-finite-difference-methods/README.md) —
  the differential counterpart and the volume-grid comparison.
- [19-03 Finite Element and Finite Volume Methods](../03-finite-element-and-volume/README.md) —
  the weak-form route to the same boundary term.
- [19-06 High-Performance and Parallel Computing](../06-hpc-and-parallel-computing/README.md) —
  the dense operator as a performance problem.
- [18-inverse-problems](../../18-inverse-problems/README.md) — regularisation of
  the first-kind systems met in lesson 01.
