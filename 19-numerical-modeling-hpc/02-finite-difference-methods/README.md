# Module 19-02 — Finite-Difference Methods

**Stages:** advanced → research · **Prerequisites:**
[19-01 Numerical Foundations for Simulation](../01-numerical-foundations/README.md),
[01-12 Numerical Methods for Mathematical Problems](../../01-mathematics/12-numerical-methods/README.md),
[03-12 Building Numerical Simulation Code in Python](../../03-scientific-computing/12-numerical-simulation-python/README.md).

This module builds finite-difference machinery one component at a time and
verifies each component against something derived rather than something
observed: stencils from the moment equations, boundary conditions whose order is
measured, time stepping whose stability limit is predicted in closed form, and a
two-dimensional wave solver whose phase speed is compared with the dispersion
relation of its own stencil. The ordering is deliberate — a solver with an
untested boundary is not a solver, and a wavefield whose dispersion has not been
measured is a picture, not a result.

The central honest difficulty is that **the discretisation is never the only
approximation**. A wave model carries four independent ones: the stencil (phase
error and anisotropy), the time step (CFL and temporal dispersion), the boundary
(spurious reflections), and the source (its bandwidth). Each is measurable, and
each has a different remedy. The lessons here measure all four in one place, so
that a modelling result can be attributed to one of them rather than to
"numerical error" in general.

**All models and data in this module are SYNTHETIC.** Every number quoted in
these lessons is printed by a demo in `code/`, or is an exact constant (a Taylor
coefficient, an impedance ratio, a von Neumann limit). No dataset, station,
seismic line or published measurement appears anywhere in this module.

## Learning objectives

By the end of this module you will be able to:

1. **Derive** any finite-difference stencil from its moment equations, including
   on non-uniform grids, and **state** its order and leading constant.
2. **Verify** a stencil by polynomial exactness and **measure** its convergence
   order on smooth data.
3. **Choose** between explicit, compact and staggered discretisations using
   measured resolving power rather than convention.
4. **Implement** Dirichlet, Neumann, one-way and sponge boundaries and
   **measure** the order and the reflection coefficient of each.
5. **Derive** the stability limit of an explicit scheme, **measure** it, and
   **separate** unconditional stability from accuracy.
6. **Assemble** a two-dimensional acoustic solver and **verify** its phase speed,
   anisotropy and reflection coefficients against independent predictions.
7. **Count** the unknowns, steps and iterations of a diffusive or potential
   problem before solving it, and **choose** between a direct and an iterative
   solve on that basis.

## Prerequisites

- [19-01 Numerical Foundations for Simulation](../01-numerical-foundations/README.md) —
  grids, degrees of freedom, truncation error, stability and dispersion; this
  module assumes all four.
- [01-12 Numerical Methods for Mathematical Problems](../../01-mathematics/12-numerical-methods/README.md) —
  differentiation, linear solvers, ODE and PDE discretisation.
- [03-12 Building Numerical Simulation Code in Python](../../03-scientific-computing/12-numerical-simulation-python/README.md) —
  a working 1-D solver and the habit of convergence testing.
- [02-04 Elasticity and Continuum Mechanics](../../02-physics/04-elasticity-and-continuum-mechanics/README.md) —
  the elastic equations the elastic examples approximate.

## Lesson map

| # | Lesson | Level | The honest difficulty it addresses |
|---|---|---|---|
| 01 | [Deriving Finite-Difference Operators via Taylor Expansion](01-fd-derivation.md) | advanced | Stencils are moment problems; a node assumed to be where it is not makes the scheme *inconsistent*, not merely inaccurate |
| 02 | [High-Order and Compact Stencils; Staggered Grids](02-fd-stencils.md) | doctoral | Resolving power, stencil width and round-off trade against each other; the staggered derivative buys a factor four for free |
| 03 | [Boundary Conditions: Dirichlet, Neumann, Absorbing, PML](03-fd-boundary-conditions.md) | research | One first-order boundary row fixes the order of the whole solution; a sponge has an optimum, and stronger is not better |
| 04 | [Explicit vs Implicit Time Stepping and Stability Limits](04-fd-time-stepping.md) | doctoral | Unconditional stability is not accuracy; measured growth rates on both sides of the CFL limit |
| 05 | [Finite-Difference Acoustic and Elastic Wave Propagation](05-fd-wave-propagation.md) | research | Phase speed, anisotropy, CFL and reflection measured in one model and compared with independent predictions |
| 06 | [FD for Diffusion, Laplace and Poisson Problems](06-fd-diffusion-and-potential.md) | doctoral | The stencil is the easy part: the solver, the conditioning and the dimension set the cost |

## Suggested path

**If you are new to finite differences:** lessons 01 and 02 in order, running both
demos. Lesson 01 §3.2 (polynomial exactness) is the fastest verification habit to
acquire.

**If you already write wave codes:** 03 (boundaries) and 04 (time stepping) are
where production bugs live; then 05 shows all four error sources measured in one
model, which is the report structure a modelling study should copy.

**If your interest is potential fields or heat flow:** 06 is self-contained given
01, and its §3.2 solver-scaling measurements are the ones that set run times in
practice.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-fd-derivation.md`](01-fd-derivation.md) | Lesson 01 |
| [`02-fd-stencils.md`](02-fd-stencils.md) | Lesson 02 |
| [`03-fd-boundary-conditions.md`](03-fd-boundary-conditions.md) | Lesson 03 |
| [`04-fd-time-stepping.md`](04-fd-time-stepping.md) | Lesson 04 |
| [`05-fd-wave-propagation.md`](05-fd-wave-propagation.md) | Lesson 05 |
| [`06-fd-diffusion-and-potential.md`](06-fd-diffusion-and-potential.md) | Lesson 06 |
| [`exercises/`](exercises) | One exercise set and one worked solution set per lesson |
| [`code/`](code) | Six runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
SymPy:

```bash
cd 19-numerical-modeling-hpc/02-finite-difference-methods/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python fd_derivation_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python fd_stencils_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python fd_boundary_conditions_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python fd_time_stepping_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python fd_wave_propagation_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python fd_diffusion_and_potential_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), needs no network access, and exits 0. The
slowest (the two-dimensional wave demo) runs in about seven seconds.

## Mastery checkpoint

Complete this without notes:

> A 2-D acoustic model uses the fourth-order-in-space, second-order-in-time
> scheme, with $c = 2500\ \mathrm{m\,s^{-1}}$, $h = 12.5$ m and a 20 Hz source.
> **(a)** Compute the wavelength, the points per wavelength, and the CFL limit.
> **(b)** State the phase error and anisotropy you expect, and which of the two
> dominates a diagonal travel time. **(c)** Choose a boundary treatment for a
> free surface and for the absorbing edges, and state the measured order of each.
> **(d)** If the run must produce reflection amplitudes accurate to $2\,\%$,
> decide whether the planned resolution suffices, and state the measurement that
> settles it.

Parts (a)–(c) are worked in the lesson solutions listed under each lesson.

## Common pitfalls across this module

1. **Recalling stencil weights instead of deriving them**, then using them on a
   grid that is not the one they were derived for.
2. **A first-order boundary condition**, which silently sets the order of the
   entire solution.
3. **Working at the stability limit** ($r = 1/2$ or $C = 1$), where the highest
   mode is neutral and never leaves.
4. **Assuming an implicit scheme is cheaper or more accurate.** It removes a
   stability limit; it does not remove the accuracy requirement.
5. **Reporting a wavefield without stating the stencil, the Courant number and
   the boundary treatment** — the three quantities that determine what the
   picture means.
6. **Choosing a stencil and ignoring the solver.** Measured: two orders of
   magnitude difference in iteration count on the same matrix.

## Related modules

- [19-01 Numerical Foundations for Simulation](../01-numerical-foundations/README.md) —
  the foundations this module builds on.
- [19-03 Finite Element and Finite Volume Methods](../03-finite-element-and-volume/README.md) —
  the alternative discretisation families for the same problems.
- [19-06 High-Performance and Parallel Computing](../06-hpc-and-parallel-computing/README.md) —
  what the measured step counts and bandwidths cost on real hardware.
- [19-08 Geophysical Simulation Case Studies](../08-geophysical-simulation-case-studies/README.md) —
  the full models these components assemble into.
- [06-01 Elastic Wave Propagation](../../06-seismology/01-elastic-wave-propagation/README.md) —
  the physics the elastic examples approximate.
