---
id: 25-04-01
title: "Project: Finite-Difference Wave Propagation and Convergence Testing"
level: graduate
prereqs: ["19-01-02", "19-01-03", "19-02-04", "19-02-05"]
estimated_minutes: 210
tags: [projects, numerics, finite-difference, convergence, stability, teaching]
---

# Project: Finite-Difference Wave Propagation and Convergence Testing

## Learning objectives

By the end of this project you will be able to:

1. **Discretise** the scalar wave equation with second-order centred differences
   and **write** the update explicitly, identifying every grid quantity.
2. **Measure** the order of convergence against a closed-form solution, and
   **fit** the order from the error sequence.
3. **Demonstrate** that an $\mathcal O(\Delta t)$ error in the *initialisation*
   destroys a second-order scheme's observed convergence, and **explain** why.
4. **Measure** the error against points per wavelength and **state** the accuracy
   a stated grid density buys.
5. **Locate** the CFL stability limit by experiment and **distinguish** a growing
   solution from a bounded one.
6. **State** the difference between consistency, stability and convergence, and
   **identify** which of the three each measurement here tests.
7. **Report** a numerical experiment as a convergence table with a fitted order, a
   resolution study and a stability margin — not as a single solution.

All results in this project are **SYNTHETIC**: a scalar wave problem with a
closed-form solution, computed by
[`code/fd_wave_demo.py`](./code/fd_wave_demo.py). No field seismogram, no
benchmark model and no published dispersion curve is used.

## Prerequisites

- [19-01-02 Truncation Error, Order of Accuracy and Convergence Rates](../../19-numerical-modeling-hpc/01-numerical-foundations/02-convergence-and-error.md) —
  the definition of order that this project measures.
- [19-01-03 Consistency, Stability and the Lax Equivalence Theorem](../../19-numerical-modeling-hpc/01-numerical-foundations/03-consistency-stability.md) —
  the theorem behind §7.
- [19-02-04 Explicit vs Implicit Time Stepping and Stability Limits](../../19-numerical-modeling-hpc/02-finite-difference-methods/04-fd-time-stepping.md) —
  the CFL condition derived, here measured.
- [19-02-05 Finite-Difference Acoustic and Elastic Wave Propagation](../../19-numerical-modeling-hpc/02-finite-difference-methods/05-fd-wave-propagation.md) —
  the scheme and its geophysical context.

## 1. The question

*Does the code solve the equation it claims to, and how accurately?*

A wave-propagation code that runs and produces a plausible-looking wavefield has
demonstrated almost nothing. The question is answerable only by comparison with a
known solution, and the structure of the answer is a **convergence table**: the
error at successively finer grids, and the rate at which it falls. This project
does exactly that on a problem with a closed-form solution, and then shows the
trap that catches most first attempts — the scheme is second order, and the
*initialisation* is first order, so a naive convergence test measures the
initialisation.

## 2. The problem and the data (SYNTHETIC)

$$u_{tt} = c^{2}u_{xx}, \qquad 0 \le x \le L = 1.0\ \mathrm{km},
\qquad c = 2.5\ \mathrm{km\,s^{-1}},$$

with Dirichlet boundaries and the initial state
$u(x,0) = \sin(\pi x/L)$, $u_t(x,0) = 0$. The exact solution is a standing wave,

$$u(x,t) = \sin\!\left(\frac{\pi x}{L}\right)\cos\!\left(\frac{\pi c t}{L}\right),
\qquad T_\text{period} = \frac{2L}{c} = 0.800\ \mathrm{s},$$

integrated to $t = 0.55\ \mathrm{s} = 0.688$ of a period. Integrating for less
than a period keeps the solution away from the exact zeros of the cosine, where a
relative error would be meaningless.

**Provenance.** SYNTHETIC. The solution is analytic, the grid is the only
approximation, and there is no source, no absorbing boundary and no heterogeneity
to introduce a second error mechanism.

## 3. The project specification

**Steps.**

1. Write the update $u^{n+1}_i = 2u^{n}_i - u^{n-1}_i + r^{2}(u^n_{i+1} -
   2u^{n}_i + u^n_{i-1})$ with $r = c\Delta t/\Delta x$, and state its truncation
   error.
2. Run the scheme at $N = 50, 100, 200, 400$ interior points with
   $r = 0.5$ fixed, **adjusting $\Delta t$ so every run ends at exactly the same
   time**, and tabulate the rms error against the exact solution.
3. Fit the observed order from successive error ratios and compare with the
   predicted value.
4. Repeat step 2 with the second time level initialised naively
   ($u^{-1} = u^{0}$) and with the exact value, and explain the difference.
5. Measure the error against points per wavelength over a factor of 16 in grid
   density.
6. Sweep the CFL number through 1 and report the amplitude of a fixed-duration run
   at each value; identify the stability limit.
7. Write the report: the scheme, the convergence table with the fitted order, the
   resolution table and the stability margin.

**Deliverable.** The update, two convergence tables, a resolution table, a CFL
sweep, and a statement of what the numbers do and do not establish.

**Success criterion.** Every error is measured against a stated exact solution at
the *same* time; the order is fitted, not asserted; the initialisation's effect is
measured; the stability limit is bracketed by experiment.

## 4. The scheme and its truncation error

With $r = c\Delta t/\Delta x$ the explicit scheme is

$$u^{n+1}_i = 2u^{n}_i - u^{n-1}_i
+ r^{2}\left(u^{n}_{i+1} - 2u^{n}_i + u^{n}_{i-1}\right),$$

and a Taylor expansion gives the modified equation

$$u_{tt} - c^{2}u_{xx}
= \frac{c^{2}\Delta x^{2}}{12}\left(r^{2}-1\right)u_{xxxx}
+ \mathcal O(\Delta x^{4}),$$

so the scheme is **second order** in space and time, with a leading error term that
vanishes at $r = 1$. That explains both why $r$ is usually chosen close to 1 in
production codes and why the CFL limit is at $r = 1$: the scheme is most accurate
exactly where it is about to become unstable.

## 5. Measuring the order, and the initialisation trap

With the time step adjusted so that every run ends at $t = 0.55\ \mathrm{s}$:

| $N$ | $\Delta x$ (m) | rms error, naive start | fitted order | rms error, exact start | fitted order |
|---|---|---|---|---|---|
| 50 | 20.00 | $9.776\times10^{-3}$ | — | $3.480\times10^{-4}$ | — |
| 100 | 10.00 | $5.018\times10^{-3}$ | $0.96$ | $8.692\times10^{-5}$ | $2.00$ |
| 200 | 5.00 | $2.537\times10^{-3}$ | $0.98$ | $2.174\times10^{-5}$ | $2.00$ |
| 400 | 2.50 | $1.276\times10^{-3}$ | $0.99$ | $5.438\times10^{-6}$ | $2.00$ |

**The scheme is second order; the naive run is first order.** Starting the
leapfrog with $u^{-1} = u^{0}$ sets the initial velocity to zero only to
$\mathcal O(\Delta t)$ accuracy: the implied velocity is
$(u^{1}-u^{-1})/(2\Delta t) \approx \tfrac{1}{4}\Delta t\,c^{2}u_{xx}$. That
$\mathcal O(\Delta t)$ error in the initial *data* propagates as an
$\mathcal O(\Delta t)$ error in the solution, and since $\Delta t \propto \Delta x$
at fixed $r$, it dominates the $\mathcal O(\Delta x^{2})$ truncation error and
flattens the fitted order to 1. The exact initialisation removes it and the fitted
order is $2.00$ at every refinement — a factor of $28$ smaller error at $N = 50$
than the naive start.

Three consequences for practice:

1. **A convergence test measures the whole algorithm**, including its start-up.
   Reporting order 2 from a scheme whose initialisation is order 1 is a claim about
   the code, not about the stencil.
2. **The error is not always where the textbooks put it.** A new source term, a
   boundary condition, an interpolation at a receiver, or a tapered source wavelet
   can each be the first-order term.
3. **The value of a convergence test is the fitted order, not the error.** A small
   error on a coarse grid means nothing if the order is wrong.

## 6. Resolution: points per wavelength

| $N$ | points per wavelength | rms error |
|---|---|---|
| 20 | 40.0 | $2.161\times10^{-3}$ |
| 40 | 80.0 | $5.421\times10^{-4}$ |
| 80 | 160.0 | $1.358\times10^{-4}$ |
| 160 | 320.0 | $3.397\times10^{-5}$ |
| 320 | 640.0 | $8.496\times10^{-6}$ |

Each doubling of the point count quarters the error — the $\mathcal O((\Delta
x/\lambda)^{2})$ grid-dispersion error of a second-order scheme. Extrapolating the
usual rules of thumb: about 10 points per wavelength buys of order $1\%$ accuracy
and 20 points about $0.25\%$, which is why production acoustic codes use 5–10
points per *shortest* wavelength as a minimum and 20 when amplitudes matter.

The table also makes clear why "5 points per wavelength" is a statement about
*phase* error, not about amplitude: a second-order scheme at 5 points per
wavelength has a phase error of several percent per wavelength traversed, so over
50 wavelengths the accumulated timing error is of order a period.

## 7. Consistency, stability and convergence

The three words are related by the Lax equivalence theorem — for a consistent
linear scheme, **stability is equivalent to convergence** — and the project
measures each in a different way.

- **Consistency** is a property of the stencil alone: does the truncation error
  vanish as $\Delta x, \Delta t \to 0$? §4 is the statement; §5 is the check that
  the scheme's order survives contact with the rest of the algorithm.
- **Stability** is a property of the *time step*: does the norm of the solution
  stay bounded? The CFL sweep measures it directly.
- **Convergence** is a property of the pair: does the numerical solution approach
  the exact one? §6 is the measurement.

The CFL sweep, at $N = 100$ and the same physical end time:

| CFL number | $\Delta t$ (ms) | final amplitude | verdict |
|---|---|---|---|
| 0.25 | 1.0000 | $3.7921\times10^{-1}$ | stable |
| 0.50 | 2.0000 | $3.7555\times10^{-1}$ | stable |
| 0.90 | 3.6000 | $3.6381\times10^{-1}$ | stable |
| 1.00 | 4.0000 | $3.5352\times10^{-1}$ | stable (exactly at the limit) |
| 1.01 | 4.0400 | $3.0767$ | **growing** (8× the initial amplitude) |
| 1.10 | 4.4000 | $1.1542\times10^{32}$ | **unstable** (overflowed) |

The boundary is **sharp**: at $r = 1.00$ the run is bounded, at $r = 1.01$ it has
already grown eightfold, and at $r = 1.10$ it has overflowed double precision. An
explicit scheme does not degrade gracefully when its stability condition is
violated — a fact worth pausing on, because the alternative failure mode, a slowly
growing solution that looks physical for a few hundred steps, is the one that
reaches a published figure.

**Why $r = 1$.** The von Neumann analysis gives the amplification factor
$|g|^{2} = 1 - r^{2}\sin^{2}\theta$ for this scheme, which is bounded only for
$r \le 1$. The measured boundary matches the analysis exactly, and the accuracy
analysis of §4 shows that the leading error term also vanishes at $r = 1$: the
scheme is most accurate and least stable at the same point.

## 8. Assumptions and regime of validity

1. **A homogeneous medium.** Heterogeneity requires the elastic or acoustic
   variable-density form and introduces impedance-related errors not present here.
2. **Dirichlet boundaries.** Real problems need absorbing boundaries or a PML; a
   reflecting boundary would invalidate the error measurement entirely.
3. **A single mode.** The standing-wave solution is one spatial frequency, so this
   test measures dispersion at one $(k, \Delta x)$; a broadband test would show the
   frequency dependence of the error.
4. **A uniform grid.** Variable grids change the local CFL condition and introduce
   an interpolation error that is frequently the dominant one.
5. **Second-order accuracy is an assumption of the test.** A fourth-order scheme
   needs a fourth-order-convergent exact comparison; with an order-1
   initialisation, a fourth-order stencil would also measure order 1.

## The honest summary

The project's product is a table and a trap. The scheme is second order in
space and time, with a leading error term proportional to $(\Delta x^{2}/12)
(r^{2}-1)u_{xxxx}$, and it measures order $2.00$ at every refinement *when the
second time level is initialised from the exact solution* — errors falling
$3.480\times10^{-4} \to 5.438\times10^{-6}$ between $N = 50$ and $N = 400$.
Initialising naively with $u^{-1} = u^{0}$ collapses the fitted order to $0.96$–$0.99$
and inflates the error by a factor of $28$, because the implied initial velocity
carries an $\mathcal O(\Delta t)$ error that dominates the $\mathcal O(\Delta x^{2})$
truncation term. The CFL limit is at $r = 1$ and is sharp: bounded at $1.00$,
growing at $1.01$, overflowed at $1.10$. What transfers to a production code is
the practice of measuring the fitted order on the *whole* algorithm, and of
treating a scheme's advertised accuracy as a hypothesis rather than a property.

## Python demonstration

[`code/fd_wave_demo.py`](./code/fd_wave_demo.py) prints every number quoted above.
It:

1. states the problem, the exact solution and the period;
2. runs the convergence test twice — naive and exact initialisation — fitting the
   order from successive error ratios ($0.96$–$0.99$ against $2.00$);
3. sweeps the grid from 40 to 640 points per wavelength and prints the
   quartering error;
4. sweeps the CFL number from $0.25$ to $1.10$ and prints the final amplitude and
   the verdict for each, locating the stability limit between $1.00$ and $1.01$.

Run it with the project virtual environment:

```bash
cd 25-projects-capstone/04-graduate-projects/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python fd_wave_demo.py
```

The script prints only, writes no files, uses no network and exits 0. It runs in
under a second.

## Exercises

Graded problems and worked solutions are in
[`exercises/01-fd-wave-propagation-project-exercises.md`](./exercises/01-fd-wave-propagation-project-exercises.md)
and
[`exercises/01-fd-wave-propagation-project-solutions.md`](./exercises/01-fd-wave-propagation-project-solutions.md).
The ★★★ item asks you to design a verification suite for a heterogeneous elastic
code, not to rerun the homogeneous test.

## Mastery checkpoint

Without notes:

1. Write the update and its truncation error, and state at which $r$ the leading
   term vanishes.
2. Explain in two sentences why a first-order initialisation gives an order-1
   convergence measurement on a second-order scheme.
3. A colleague reports "the code is second order" from a run at a single grid
   density. State what that claim requires.
4. The CFL sweep shows a bounded run at $r = 1.00$ and growth at $1.01$. State the
   theorem that relates this to convergence.

## Common pitfalls

1. **Measuring the order at a single grid.** An order is a slope, and a slope needs
   two or more points.
2. **Comparing at different times.** If the runs do not end at the same time, the
   measurement carries an $\mathcal O(\Delta t)$ contamination; this project had to
   fix exactly that before the order came out right.
3. **Reporting an error without the exact solution behind it.** "Small residual"
   is not a convergence statement.
4. **Running at $r$ far below 1 "for safety".** The leading error term grows as
   $r^{2}-1$; a smaller $r$ is *less* accurate, not more.
5. **Assuming a slowly growing solution is physical.** Check the norm against the
   initial amplitude, as the CFL table does.

## Where this is used

The verification practice here is the foundation of every wave-modelling project
that follows: the full-waveform inversion of
[25-05-02](../05-doctoral-projects/02-full-waveform-inversion-project.md) inverts a
model whose forward operator has to be verified first, and the migration step of
[25-03-03](../03-advanced-projects/03-seismic-processing-project.md) relies on the
same dispersion properties. In professional practice the convergence table is the
first appendix of any modelling paper, and a code without one is treated as
unverified.

## Related lessons

- [19-01-04 Numerical Dispersion, Dissipation and Grid Anisotropy](../../19-numerical-modeling-hpc/01-numerical-foundations/04-numerical-dispersion-diffusion.md) —
  the grid-dispersion error measured in §6.
- [19-02-02 High-Order and Compact Stencils; Staggered Grids](../../19-numerical-modeling-hpc/02-finite-difference-methods/02-fd-stencils.md) —
  what changes when the stencil is raised to fourth order.
- [19-02-03 Boundary Conditions: Dirichlet, Neumann, Absorbing, PML](../../19-numerical-modeling-hpc/02-finite-difference-methods/03-fd-boundary-conditions.md) —
  the boundary error that would otherwise dominate §5.
- [25-05-02 Project: A Small-Scale Full-Waveform Inversion](../05-doctoral-projects/02-full-waveform-inversion-project.md) —
  where the verified forward operator is inverted.

## Self-assessment checklist

- [ ] I can write the second-order scheme and its modified equation.
- [ ] I can measure and fit an order of convergence.
- [ ] I can explain and demonstrate the initialisation trap.
- [ ] I can convert a grid density to an accuracy expectation.
- [ ] I can locate a stability limit by experiment.
- [ ] I can state which measurement tests consistency, stability and convergence.
