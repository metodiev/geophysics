---
id: 13-05-03
title: "Benchmarking Geodynamic Codes"
level: research
prereqs: ["13-05-02", "19-07-01", "19-07-02"]
tags: [geodynamics, tectonophysics, benchmarking, verification, numerical-uncertainty]
---

# Benchmarking Geodynamic Codes

> **All models and data in this module are SYNTHETIC.** The convergence study,
> benchmark value and error budget below are computed from a chosen convection
> model with exact analytic targets, not from any published benchmark. Every
> number is printed by
> [`code/benchmarking_geodynamics_demo.py`](code/benchmarking_geodynamics_demo.py).

## Learning objectives

By the end of this lesson you will be able to:

1. **Distinguish** verification (does the code solve the stated equations?) from
   validation (do the equations describe the Earth?) and **state** which of the
   two is possible from synthetic models alone.
2. **Compute** a Grid Convergence Index from a three-grid study and **interpret**
   it as an uncertainty band rather than a decoration.
3. **Demonstrate** that two discretisations can agree on one integral diagnostic
   while disagreeing on the field that produces it.
4. **Show** that a benchmark value is resolution-dependent, by measuring the
   critical Rayleigh number at three grids and comparing with the exact
   $8\pi^4$.
5. **Build** an error budget for one reported number, sorted by the size of each
   contribution.
6. **Recognise** the failure mode in which a stopping criterion silently reports
   a number that is not a steady state.
7. **Write** a verification statement that names the target, the norm, the grid
   and the observed order.

## Prerequisites

- [13-05-02 Solving the Stokes Equations for Mantle Flow](02-stokes-flow-solvers.md) —
  the model and its exact targets used here.
- [19-07-01 Code Verification](../../19-numerical-modeling-hpc/07-verification-validation-uncertainty/01-code-verification.md) —
  the general methodology.
- [19-07-02 Solution Verification](../../19-numerical-modeling-hpc/07-verification-validation-uncertainty/02-solution-verification.md) —
  estimating the numerical error in a result.
- [19-01-02 Convergence and Error](../../19-numerical-modeling-hpc/01-numerical-foundations/02-convergence-and-error.md) —
  the order-of-accuracy framework.

## 1. What a benchmark is for

A benchmark is a problem with an answer that is known independently of the code
under test. There are exactly three kinds:

- an **analytic target**, such as the critical Rayleigh number $8\pi^4 = 779.27$
  for the unit-aspect free-slip box derived in
  [13-05-02](02-stokes-flow-solvers.md);
- a **manufactured solution**, where a source term is constructed so that a
  chosen function is the exact solution;
- a **cross-code comparison**, where two independently written codes solve the
  same problem and their answers are compared.

The third kind is the weakest and the most common. If the two codes share a
discretisation, a bug in that discretisation cancels in the comparison; if they
do not share it, the comparison constrains the *difference* between two
approximations but not either one's error. Sections 3–5 below quantify how weak
that evidence is.

Verification and validation are different questions. Verification asks whether
the code solves the stated equations correctly, and it is answerable here
because the targets are exact. Validation asks whether the stated equations
describe the Earth, and it is not answerable from synthetic models: it needs
observations, independent constraints and a statement of which observation
discriminates between two models that fit the data equally well. This curriculum
makes no validation claims, and the exercises ask for the *shape* of a validation
argument rather than a validation result.

## 2. Grid convergence and the Grid Convergence Index

If a discretisation has formal order $p$, the error of a smooth functional $F$ on
grid spacing $h$ behaves as $F(h) = F_0 + c\,h^p$. With three grids of uniform
refinement ratio $r$ the order follows from the solution values alone:

$$p \simeq \frac{\ln\left|\dfrac{F_1-F_2}{F_2-F_3}\right|}{\ln r} ,$$

and the extrapolated value and the uncertainty band — Roache's Grid Convergence
Index with safety factor $F_s$ — are

$$F_0 \simeq F_3 + \frac{F_3-F_2}{r^p - 1}, \qquad
\mathrm{GCI} = F_s\,\frac{|F_3-F_2|/F_3}{r^p-1} .$$

The GCI is a *statement about the numerical solution*, not about the physics: it
says how much of a reported number you should not trust because of the mesh.

Measured, for the Nusselt number of the constant-viscosity free-slip unit-aspect
cell at $Ra = 10^4$:

| $N$ | $h$ | $Nu$ (bottom flux) | $Nu$ (volume average) | steps to steady state |
|---|---|---|---|---|
| 16 | 0.058824 | 5.31066 | 4.18571 | 1600 |
| 32 | 0.030303 | 4.97829 | 4.51225 | 2600 |
| 48 | 0.020408 | 4.90191 | 4.63216 | 5000 |

with the refinement ratio $h_1/h_2 = 1.941$ (not exactly 2, because $h = 1/(N+1)$
and the meshes were chosen at round numbers — a complication that must be stated,
since the classic three-grid formula assumes a uniform ratio and the *ratios here
are not uniform*). The demonstration reports

- observed order $p = 2.217$,
- Richardson extrapolation $Nu(h\to0) = 4.84745$,
- GCI with $F_s = 1.25$: **1.389%** of $Nu$,
- the finest grid's own error, $|Nu(48)-Nu_0|/Nu_0 = 1.12\%$.

Two cautions follow from reading the arithmetic rather than the answer. First,
the measured order 2.217 exceeds the formal order 2 — a reminder that a fitted
order from three grids is a noisy quantity, not a measurement of $p$. Second,
the two definitions of the same diagnostic differ far more than the GCI:
$4.90191$ from the bottom flux against $4.63216$ from
$1+\langle wT\rangle$, a **5.50%** difference. The reported uncertainty is
dominated not by the grid but by which question was asked.

## 3. What agreement between two grids proves, and what it does not

The Nusselt number is an integral of the bottom heat flux; errors partly cancel
in an integral, which is why it is the quantity two grids agree on first.
Compare the *field* that produced it. Interpolating the $N=32$ horizontally
averaged temperature onto the $N=48$ profile gives

- rms difference: **0.938%** of the total temperature drop,
- maximum difference: **4.532%**,

against a 1.558% difference in $Nu$. The interior temperature field — which is
what a seismic velocity conversion, a geoid interpretation or a metamorphic
assemblage would actually read — agrees 3 to 5 times less well than the single
number usually quoted.

The practical consequence is the following. A benchmark that specifies only
"$Nu$ within 1%" can be passed by two codes whose interior fields differ by
several per cent, and the comparison has then verified almost nothing. The
benchmark to design is one that constrains the field: pointwise interior values,
a boundary-layer thickness, the rms velocity, or the planform. The module
[19-07-04 Benchmark Problems](../../19-numerical-modeling-hpc/07-verification-validation-uncertainty/04-benchmark-problems.md)
develops the design side of this argument.

## 4. A benchmark value depends on the resolution

The critical Rayleigh number of the configuration has the exact value
$8\pi^4 = 779.27$. Measuring it — as in
[13-05-02](02-stokes-flow-solvers.md), by extrapolating the growth rate of the
first mode to zero — gives

| $N$ | $h$ | $Ra_c$ measured | error against $8\pi^4$ |
|---|---|---|---|
| 24 | 0.040000 | 813.65 | $+4.41\%$ |
| 40 | 0.024390 | 799.39 | $+2.58\%$ |
| 64 | 0.015385 | 791.69 | $+1.59\%$ |

The measured value decreases monotonically toward the exact one as $h$ shrinks,
which is precisely what a correct code with a consistent discretisation must do.
Two conclusions:

- **A benchmark comparison is meaningless without the grid.** "Code A gives
  779.3 and code B gives 792" says nothing until both grids are quoted; the
  second could be the more trustworthy result at a coarser resolution or the
  less trustworthy one at the same resolution.
- **The measured drift is itself the verification evidence.** A code that
  reproduced $779.27$ exactly on a coarse mesh would be suspicious, and a code
  whose error grew with refinement would be wrong.

## 5. An error budget for one reported number

Take $Nu = 4.90191$ at $N=48$ with the stopping tolerance $10^{-6}$ as the
reference, and vary one choice at a time:

| source of change | $Nu$ | deviation from the reference |
|---|---|---|
| grid coarsened to $N=32$ | 4.97829 | 1.558% |
| grid coarsened to $N=16$ | 5.31066 | 8.338% |
| diagnostic redefined as $1+\langle wT\rangle$ | 4.63216 | 5.503% |
| stopping tolerance loosened to $10^{-5}$ | 4.97828 | 0.000% (same grid) |

The ordering is the point. The definition of the diagnostic is the largest single
entry, then the grid; the stopping criterion is negligible for this quantity
once it is tight enough to be met at all. An honest report quotes the definition,
the grid and the measured grid error, and says that the stopping error was
checked.

The fourth row is compared with the same grid at tolerance $10^{-6}$, so it
isolates the stopping error; the comparison is apples to apples only because the
reference in that row is the $N=32$ run at the tighter tolerance.

## 6. The failure that is not small at all

The same demonstration runs the first-order upwind energy equation at $N=32$,
$Ra = 10^4$, and samples $Nu$ every 1000 steps:

$$3.138,\ 3.927,\ 2.343,\ 1.428,\ 3.375,\ 1.674$$

The values wander by a factor of three. The stopping rule used everywhere else in
this lesson — "stop when $Nu$ changes by less than a tolerance between two checks
200 steps apart" — is satisfied at some times and violated at others, so it can
return a number that is not a steady state at all, and it will do so silently.

This is the most dangerous failure in computational geodynamics because it
produces a plausible number. The remedy is procedural, not numerical: monitor the
diagnostic over a window much longer than the stopping interval, plot it, and
state the amplitude of the residual variation in the result. A steady-state claim
is a hypothesis with evidence, not an assumption.

## 7. Worked example: writing a verification statement

*Problem.* Write a defensible verification paragraph for the claim "$Nu = 4.9$ at
$Ra = 10^4$ in the unit-aspect free-slip box".

*Answer, with the arithmetic from Sections 2–5:*

1. **Target.** The problem is the constant-viscosity Boussinesq convection
   problem in a unit square with free-slip boundaries, adiabatic side walls and
   fixed temperatures; the discretisation is the stream-function/vorticity scheme
   of [13-05-02](02-stokes-flow-solvers.md) with central differences.
2. **Independent verification.** The same code reproduces the analytic critical
   Rayleigh number $8\pi^4 = 779.27$ to $+4.41\%$ at $N=24$ and $+1.59\%$ at
   $N=64$, with the error decreasing monotonically with refinement — the
   strongest statement available here.
3. **Solution verification.** $Nu = 5.31066$, $4.97829$, $4.90191$ at $N = 16,\
   32,\ 48$; observed order $2.217$; Richardson limit $4.84745$; GCI 1.389%.
4. **The claim.** $Nu = 4.90 \pm 0.07$ (the GCI band), with the definition
   (bottom flux) stated.
5. **Residual risk.** The definition of $Nu$ changes the number by 5.5%, and the
   total is quoted to 1.4%; the dominant uncertainty is therefore not the mesh
   but the diagnostic. The interior temperature field is resolved only to a few
   per cent.

Note what is missing: no statement about the Earth. The paragraph verifies a
code and quantifies its numerical error, and stops there. That boundary is the
subject of the next section.

## 8. Assumptions and regime of validity

1. **The reported order requires a uniform refinement ratio.** With $h_1/h_2 \ne
   h_2/h_3$ the three-grid formula is only indicative, as in the $1.941$ ratio
   used above.
2. **The Richardson limit assumes one dominant error term.** Mixed orders (a
   second-order interior and a first-order boundary treatment) produce a fitted
   order that is neither, and an extrapolation that is biased.
3. **The GCI is a band on the numerical solution, not on the physics.** It does
   not include model error, parameter error or the diagnostic definition.
4. **The measured $Ra_c$ is a property of the discretised linearised problem.**
   It converges to $8\pi^4$ for this scheme; other schemes converge to the same
   value at their own rates.
5. **The stopping failure is demonstrated for one scheme at one Rayleigh
   number.** Its general lesson — check that a steady state exists — is what
   carries over, not the specific numbers.
6. **All of this is verification.** No number in this lesson is a measurement of
   the Earth, and none is a validation.

## Mastery checkpoint

Without notes:

1. State the difference between verification and validation, and say which is
   possible with synthetic models.
2. Given three Nusselt numbers on uniformly refined grids, compute the observed
   order, the Richardson limit and a GCI with $F_s = 1.25$.
3. Explain why two codes agreeing on $Nu$ to 1% may have interior temperature
   fields that differ by several per cent, and design one extra benchmark
   quantity that would catch it.
4. Explain why the measured $Ra_c$ decreasing toward $8\pi^4$ is evidence of
   correctness while a measured value of exactly $8\pi^4$ on a coarse grid would
   be suspicious.
5. Sort the following by expected size for a convection diagnostic: grid error,
   diagnostic definition, stopping tolerance, advection scheme.
6. Describe the procedure you would use to detect that a reported steady state is
   not one.

## Common pitfalls

1. **Quoting a benchmark value without the grid, the norm and the diagnostic
   definition.** Every one of those changes the number by more than the
   comparison tolerance usually claimed.
2. **Treating cross-code agreement as verification.** Shared discretisations
   share errors.
3. **Assuming a fitted order equals the formal order.** The measured 2.217
   against a formal 2 shows the noise; the boundary-layer case in
   [13-05-01](01-finite-element-geodynamics.md) shows a case where both schemes
   return $\approx 0.9$.
4. **Trusting a stopping criterion.** The upwind run wanders by a factor of three
   while satisfying it.
5. **Reporting a GCI as the total uncertainty.** It excludes the diagnostic
   definition, the parameters and the model.
6. **Letting verification slide into validation.** A code that reproduces an
   analytic target has not been shown to describe the mantle.

## Related modules

- [13-05-01 Finite Element and Finite Volume Methods](01-finite-element-geodynamics.md) —
  the schemes whose orders are measured.
- [13-05-02 Solving the Stokes Equations for Mantle Flow](02-stokes-flow-solvers.md) —
  the model, the analytic targets and the diagnostics.
- [19-07 Verification, Validation and Numerical Uncertainty](../../19-numerical-modeling-hpc/07-verification-validation-uncertainty/README.md) —
  the general methodology, including manufactured solutions and benchmark design.
- [13-02-02 Numerical Modelling of Mantle Convection](../02-mantle-convection/02-convection-numerical.md) —
  the modelling context in which these diagnostics are used.
- [13-01-02 Rheology: Elastic, Viscous, Plastic and Power-Law Creep](../01-geodynamic-principles/02-rheology-of-earth.md) —
  the constitutive choice a benchmark never tests.

Companion exercises:
[`exercises/03-benchmarking-geodynamics-exercises.md`](exercises/03-benchmarking-geodynamics-exercises.md)
and
[`exercises/03-benchmarking-geodynamics-solutions.md`](exercises/03-benchmarking-geodynamics-solutions.md).
Run the demonstration with

```bash
cd 13-geodynamics-tectonics/05-geodynamic-modelling/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python benchmarking_geodynamics_demo.py
```
