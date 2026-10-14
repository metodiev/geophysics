# Module 19-01 — Numerical Foundations for Simulation

**Stages:** graduate → research · **Prerequisites:**
[01-12 Numerical Methods for Mathematical Problems](../../01-mathematics/12-numerical-methods/README.md),
[03-12 Building Numerical Simulation Code in Python](../../03-scientific-computing/12-numerical-simulation-python/README.md),
[03-02 NumPy and Array Computing](../../03-scientific-computing/02-numpy/README.md).

This module answers the question that every later modelling module assumes:
**when a continuous problem is replaced by a finite set of numbers, what exactly
have you changed, and how would you know?** It builds the vocabulary — grid,
node, cell, degree of freedom, storage convention — and then quantifies the
consequences: a material contrast stored in the wrong place produces a flux error
that refinement does not remove; a discrete norm is not the norm of the field;
the discretisation error of a scheme is a number you can predict before writing
the solver; and refining the grid improves accuracy while making the linear
algebra worse in a precisely measurable way.

The central honest difficulty is that **convergence is not accuracy**. A scheme
can be consistent and stable — and therefore convergent by Lax equivalence — and
still deliver a wave that travels at the wrong speed, arrives with the wrong
amplitude, and prefers the grid's diagonal to the geology's. Every lesson here
either derives a quantity in closed form and then measures it, or measures a
quantity and then explains it; where a demo contradicts an expectation, the
lesson reports the measurement.

**All models and data in this module are SYNTHETIC.** Every number quoted in
these lessons is printed by a demo in `code/`, or is an exact constant (a Taylor
coefficient, an eigenvalue formula, an asymptotic order). No dataset, station or
published measurement is used anywhere in this module.

## Learning objectives

By the end of this module you will be able to:

1. **Count** the degrees of freedom of node-centred and cell-centred
   discretisations in one, two and three dimensions, and **size** a run's memory
   before writing it.
2. **Explain** why the harmonic mean reproduces a material interface exactly and
   the arithmetic mean does not, with the measured flux error attached.
3. **Derive** a truncation constant from the moments of a stencil and
   **measure** the observed order of accuracy from solutions alone.
4. **Compute** a Richardson-extrapolated value and a grid-convergence index, and
   **state** what each bounds.
5. **Predict** the step size at which truncation and round-off balance, and
   **explain** why further refinement makes a result worse.
6. **Perform** a von Neumann stability analysis, **measure** the growth rate of
   an unstable run, and **state** the Lax equivalence theorem with its
   hypotheses.
7. **Derive** a discrete dispersion relation, **measure** the phase and group
   velocities of a pulse, and **quantify** numerical dissipation and grid
   anisotropy.

## Prerequisites

- [01-12 Numerical Methods for Mathematical Problems](../../01-mathematics/12-numerical-methods/README.md) —
  root finding, interpolation, differentiation, quadrature, linear and ODE
  solvers, PDE discretisation.
- [03-12 Building Numerical Simulation Code in Python](../../03-scientific-computing/12-numerical-simulation-python/README.md) —
  a first finite-difference solver, CFL conditions, verification practice.
- [03-02 NumPy and Array Computing](../../03-scientific-computing/02-numpy/README.md) —
  arrays, strides, memory layout and vectorisation.
- [01-09 Partial Differential Equations](../../01-mathematics/09-partial-differential-equations/README.md) —
  the classification this folder discretises.

## Lesson map

| # | Lesson | Level | The honest difficulty it addresses |
|---|---|---|---|
| 01 | [Discretisation: Grids, Nodes, Cells and Degrees of Freedom](01-discretisation-concepts.md) | graduate | Where the unknowns live decides the answer: a $2.8\,\%$ flux error from an averaging choice, and a discrete norm that is not the norm you meant |
| 02 | [Truncation Error, Order of Accuracy and Convergence Rates](02-convergence-and-error.md) | doctoral | Order without a constant is not a number; measured orders on three grids, and the round-off floor that ends refinement |
| 03 | [Consistency, Stability and the Lax Equivalence Theorem](03-consistency-stability.md) | research | Consistency and stability are independent; higher spatial order can be *unconditionally unstable* |
| 04 | [Numerical Dispersion, Dissipation and Grid Anisotropy](04-numerical-dispersion-diffusion.md) | research | A stable, convergent scheme still moves waves at the wrong speed, in the wrong direction, with the wrong amplitude |

## Suggested path

**If you are new to numerical modelling:** lessons 01–02 in order, running each
demo and checking the printed numbers against the predictions in the text. The
counting exercises in lesson 01 are the fastest way to build intuition about
cost.

**If you already write solvers:** start at 01 §3.2 (the interface averaging
result), then read 02 §3.2–3.4 (observed order, Richardson, GCI) and 03 in full.
Those three sections cover the failures most often seen in production codes.

**If you are preparing a research project:** 03 and 04 are the two lessons that
decide whether a wavefield means what it appears to mean; pair them with the
★★★ exercises, which ask for measured protocols rather than opinions.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-discretisation-concepts.md`](01-discretisation-concepts.md) | Lesson 01 |
| [`02-convergence-and-error.md`](02-convergence-and-error.md) | Lesson 02 |
| [`03-consistency-stability.md`](03-consistency-stability.md) | Lesson 03 |
| [`04-numerical-dispersion-diffusion.md`](04-numerical-dispersion-diffusion.md) | Lesson 04 |
| [`exercises/`](exercises) | One exercise set and one worked solution set per lesson |
| [`code/`](code) | Four runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
SymPy:

```bash
cd 19-numerical-modeling-hpc/01-numerical-foundations/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python discretisation_concepts_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python convergence_and_error_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python consistency_stability_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python numerical_dispersion_diffusion_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), runs in well under a second, requires no
network access and exits 0.

## Mastery checkpoint

Complete this without notes:

> A 1-D advection problem is discretised with upwind differencing at $C = 0.4$
> on a periodic grid of 200 cells with $h = 25$ m. **(a)** Compute the truncation
> residual's leading coefficient and state the order. **(b)** State whether the
> scheme is stable and what Lax equivalence then allows you to conclude.
> **(c)** A mode of 10 cells per wavelength is present: predict its phase error
> with the scheme of lesson 04 and decide whether it matters. **(d)** The grid is
> refined to $h = 12.5$ m at fixed $C$: state what happens to the truncation
> error, to the phase error of that mode, and to the conditioning of any
> implicit solve you might add.

Parts (a)–(c) are worked in the lesson solutions listed under each lesson.

## Common pitfalls across this module

1. **Quoting an order without the constant.** The constant decides the
   resolution you need.
2. **Assuming consistency implies stability, or stability implies accuracy.**
   Lesson 03 measures both failure modes.
3. **Reporting a discrete norm as a physical quantity.** It carries an
   $O(h^{2})$ bias of its own.
4. **Refining past the round-off floor.** The optimal step is predictable and
   measurable.
5. **Trusting "ten points per wavelength" without the scheme and the Courant
   number.** It corresponds to a $1.9\,\%$ phase error at $C = 0.5$ and to exact
   propagation at $C = 1$.
6. **Forgetting anisotropy.** The grid has a preferred direction even when the
   medium does not.

## Related modules

- [19-02 Finite-Difference Methods](../02-finite-difference-methods/README.md) —
  the stencils, boundaries and schemes built on these foundations.
- [19-07 Verification, Validation and Numerical Uncertainty](../07-verification-validation-uncertainty/README.md) —
  the formal practice of the measurements performed here.
- [01-12 Numerical Methods for Mathematical Problems](../../01-mathematics/12-numerical-methods/README.md) —
  the mathematical-methods counterpart of this module.
- [18-01 Foundations of Inverse Problems](../../18-inverse-problems/01-inverse-problem-foundations/README.md) —
  the same discretisation choices seen from the inversion side.
