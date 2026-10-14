# Module 13-05 — Geodynamic Modelling Practice

**Stages:** research · **Prerequisites:** modules
[13-01](../01-geodynamic-principles/README.md) and
[13-02](../02-mantle-convection/README.md); numerical methods
([19-03](../../19-numerical-modeling-hpc/03-finite-element-and-volume/README.md)),
inverse problems ([18-01](../../18-inverse-problems/01-inverse-problem-foundations/README.md))
and scientific Python ([03-02](../../03-scientific-computing/02-numpy/README.md),
[03-03](../../03-scientific-computing/03-scipy/README.md)).

This module is about the machinery, and about the honest reporting of what the
machinery can and cannot do. A geodynamic code solves the balance laws of module
13-01 for a rheology of module 13-01 in a geometry of module 13-03; the question
this module answers is *how much of the answer is the physics and how much is the
discretisation*. Every lesson measures its own error rather than asserting that it
is small: element pairs are tested against the inf-sup condition, advection
schemes are tested against an exact operator identity, the Nusselt number is
tested against the analytic critical Rayleigh number, and an adjoint gradient is
tested against finite differences.

The organising principle is that **verification is possible and validation is
not**. Every model here has an exact target — a manufactured solution, an analytic
growth rate, the critical Rayleigh number $8\pi^4$, an operator identity, a
quarter-of-a-million-mode Picard plot — and the measured error against that
target is the evidence. What cannot be done from synthetic models is to show that
the equations describe the Earth, and the module says so in each lesson instead
of leaving it implicit.

All models and data in this module are **SYNTHETIC**. The parameters are chosen
teaching values with units, no number is quoted from a published benchmark, and
every printed number is produced by the demonstration in the lesson that uses it.

## Learning objectives

By the end of this module you will be able to:

1. **Derive** the weak form of a boundary-value problem and **measure** the order
   of accuracy of a discretisation by grid refinement.
2. **Compute** the discrete inf-sup constant of a Stokes element pair and
   **decide**, from its behaviour under refinement, whether the pair is stable.
3. **Derive** and **verify** the upwind numerical diffusivity $|u|h/2$ and the
   cell-Péclet monotonicity threshold.
4. **Non-dimensionalise** the Boussinesq Stokes system and **compute** the
   Rayleigh number.
5. **Derive** the linear growth rate $\sigma(k,l)$ and the critical Rayleigh
   number of a convection cell, and **measure** both.
6. **Quantify** the grid, scheme and diagnostic-definition error in a reported
   Nusselt number and **combine** them into an uncertainty statement.
7. **Compute** a Grid Convergence Index and **state** what it excludes.
8. **Derive** and **verify** the adjoint of a time-stepping forward model.
9. **Interpret** a singular-value spectrum as a statement about which initial
   conditions are recoverable.
10. **Estimate** the ensemble size needed for a spread-based uncertainty and
    **state** its sampling error.

## Prerequisites

- [13-01-01 Momentum, Mass and Energy Balances](../01-geodynamic-principles/01-momentum-mass-energy.md) —
  the equations being discretised.
- [13-02-01 Rayleigh-Bénard Convection Applied to the Mantle](../02-mantle-convection/01-rayleigh-benard-mantle.md) —
  the convection problem used as a test case.
- [19-03 Finite Element and Finite Volume Methods](../../19-numerical-modeling-hpc/03-finite-element-and-volume/README.md) —
  the general theory of the discretisations.
- [19-01 Numerical Foundations for Simulation](../../19-numerical-modeling-hpc/01-numerical-foundations/README.md) —
  consistency, stability, convergence.
- [18-01 Inverse Problem Foundations](../../18-inverse-problems/01-inverse-problem-foundations/README.md) —
  the framework for the assimilation lesson.
- [03-02 NumPy](../../03-scientific-computing/02-numpy/README.md) and
  [03-03 SciPy](../../03-scientific-computing/03-scipy/README.md) —
  the tools every demonstration uses.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Finite Element and Finite Volume Methods in Geodynamics](01-finite-element-geodynamics.md) | research | The inf-sup constant is measured, not asserted; upwinding is an exact operator identity, and it has a price |
| 02 | [Solving the Stokes Equations for Mantle Flow](02-stokes-flow-solvers.md) | research | $Ra_c = 8\pi^4$ is a target; the Nusselt-number exponent depends on the fitting range; it is contrast sharpness, not size, that breaks solvers |
| 03 | [Benchmarking Geodynamic Codes](03-benchmarking-geodynamics.md) | research | Agreement on one integral is not verification; the error budget is dominated by the diagnostic definition |
| 04 | [Data Assimilation and Adjoint Geodynamics](04-data-assimilation-geodynamics.md) | research | The adjoint is verified, the null space is real, and the minimum-norm answer is a choice |

## Suggested path

**If you are new to geodynamic modelling:** lessons 01 and 02 in order, running
each demonstration and reading its output line by line. Lesson 02 §3 (the analytic
growth rate and $Ra_c$) is the single most useful piece of algebra in the module.

**If you already run a geodynamic code:** lesson 03 in full, then lesson 04. The
error-budget table in 03 §5 is the template for reporting a number from any code.

**If you are preparing a research project:** 02 §7 (why solvers fail), 03 §3
(what cross-code agreement proves) and 04 §4–5 (what an inversion can and cannot
return), plus the ★★★ exercises.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-finite-element-geodynamics.md`](01-finite-element-geodynamics.md) | Lesson 01 |
| [`02-stokes-flow-solvers.md`](02-stokes-flow-solvers.md) | Lesson 02 |
| [`03-benchmarking-geodynamics.md`](03-benchmarking-geodynamics.md) | Lesson 03 |
| [`04-data-assimilation-geodynamics.md`](04-data-assimilation-geodynamics.md) | Lesson 04 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Four runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
SymPy:

```bash
cd 13-geodynamics-tectonics/05-geodynamic-modelling/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python finite_element_geodynamics_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python stokes_flow_solvers_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python benchmarking_geodynamics_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python data_assimilation_geodynamics_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), is print-only (no figures, no network) and
exits 0. The four take about 1 s, 9 s, 3 s and 0.3 s respectively.

## Mastery checkpoint

Complete this without notes:

> A convection code reports $Nu = 4.9$ at $Ra = 10^{4}$ on a $32\times32$ grid,
> with central-difference advection and a steady-state stopping tolerance of
> $10^{-6}$. **(a)** State which target you would use to verify the code and why
> it is an independent check. **(b)** Compute the grid error from
> $Nu = 5.0799$ ($N=24$), $4.9788$ ($N=32$) and $4.9015$ ($N=48$) under an
> $O(h^2)$ assumption. **(c)** State the three other contributions to the
> uncertainty and which is the largest. **(d)** Say which of (b) and (c) a better
> computer would reduce.

A worked version of (a)–(b) appears in the lesson-03
[solutions](exercises/03-benchmarking-geodynamics-solutions.md).

## Common pitfalls across this module

1. **Quoting an order of accuracy from one mesh pair.** The lesson's own
   estimates range from 2.22 to 0.9 depending on the problem.
2. **Asserting that an element pair is stable because the matrix inverted.**
   Measure the inf-sup constant under refinement.
3. **Blaming the viscosity contrast.** Smooth contrast was measured to be almost
   free; sharpness is the cost.
4. **Reporting a benchmark value without its grid, norm and diagnostic
   definition.** Each of the three changes the number by more than the usual
   comparison tolerance.
5. **Trusting a stopping rule.** Section 6 of lesson 03 exhibits a scheme that
   satisfies it while wandering by a factor of three.
6. **Treating the recovered initial condition as the truth.** The module's own
   noiseless inversion is 12% wrong.

## Related modules

- [13-01 Geodynamic Principles](../01-geodynamic-principles/README.md) and
  [13-02 Mantle Convection](../02-mantle-convection/README.md) — the physics this
  module discretises.
- [13-03 Quantitative Plate Tectonics](../03-plate-tectonics-quantitative/README.md)
  and [13-04 Tectonophysics and Deformation](../04-tectonophysics-deformation/README.md) —
  the geologies these methods are used on.
- [19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md) — the
  general numerical methods and the verification methodology.
- [18-inverse-problems](../../18-inverse-problems/README.md) — the general
  inversion theory behind lesson 04.
