---
id: 05-03-04
title: "Numerical Forward Modelling and Discretisation"
level: graduate
prereqs: ["05-03-01", "05-03-03"]
tags: [discretisation, finite-difference, convergence, manufactured-solution, numerics]
---

# Numerical Forward Modelling and Discretisation

## Learning objectives

1. **Distinguish** the three sources of error in a numerical forward model:
   modelling, discretisation and round-off.
2. **Derive** the second-order truncation error of the 5-point Laplacian and
   **measure** the convergence order of a solver.
3. **Use** the method of manufactured solutions to validate a PDE solver.
4. **Choose** a discretisation and state its cost and its error budget.
5. **Report** a numerical result so that another person can reproduce and
   falsify it.

## Prerequisites

- [05-03-01 The Forward Problem](./01-forward-problem.md)
- [01-09-04 Laplace and Poisson Equations](../../01-mathematics/09-partial-differential-equations/04-laplace-poisson.md)

## 1. Intuition

Analytical solutions exist for a handful of shapes. Everything else is
numerical, and every numerical answer contains an error that you chose. The
skill is not writing the solver; it is knowing which of the three error sources
dominates, and demonstrating that it is small compared with the physical
question.

## 2. Precise definitions

**Modelling error.** The difference between the physical system and its
mathematical statement (e.g. assuming a homogeneous half-space when the Earth is
layered). You cannot reduce it by refining a grid.

**Discretisation error.** The difference between the exact solution of the
mathematical statement and the computed solution. Reduced by refinement.

**Round-off error.** The difference caused by finite-precision arithmetic.
Increases as the grid is refined past a crossover point, because more
operations accumulate more error.

**Convergence order $p$.** If the error behaves as $E(h) = Ch^p$ for grid
spacing $h$, then $p = \log(E_1/E_2)/\log(h_1/h_2)$ measured between two
refinements.

## 3. Derivations

### 3.1 Truncation error of the 5-point Laplacian

Taylor expand $u$ about $(x_i,y_j)$:

$$u_{i\pm1,j} = u \pm h u_x + \frac{h^2}{2}u_{xx} \pm \frac{h^3}{6}u_{xxx}
+ \frac{h^4}{24}u_{xxxx} + O(h^5).$$

Adding the four neighbours and subtracting $4u$:

$$u_{i+1,j}+u_{i-1,j}+u_{i,j+1}+u_{i,j-1}-4u = h^2\nabla^2u
+ \frac{h^4}{12}\left(u_{xxxx}+u_{yyyy}\right) + O(h^6),$$

so

$$\nabla^2u = \frac{u_{i+1,j}+u_{i-1,j}+u_{i,j+1}+u_{i,j-1}-4u}{h^2}
- \frac{h^2}{12}\left(u_{xxxx}+u_{yyyy}\right) + O(h^4).$$

The scheme is **second order**: the local truncation error is $O(h^2)$.

### 3.2 Measuring the order

Halving $h$ multiplies a second-order error by 4. So the *order* is measurable:

$$p = \frac{\log(E(h_1)/E(h_2))}{\log(h_1/h_2)}.$$

This is the single most useful diagnostic in numerical geophysics: it tells you
whether your implementation matches your intention.

### 3.3 Method of manufactured solutions

Choose a solution $u$ with the properties you need (here
$u = \sin\pi x\sin\pi y$, which vanishes on the unit-square boundary). Compute
the source term $b = -\nabla^2u$ analytically. Solve the discrete problem with
$b$ and the exact boundary data, and compare with $u$. Any defect in the
implementation — a wrong coefficient, a wrong stencil, an assembly bug — shows
up as an error that does not converge at the expected order.

## 4. Units and dimensional analysis

| Symbol | Meaning | Unit |
|---|---|---|
| $h$ | grid spacing | m |
| $u$ | field being solved for | m² s⁻² (potential) |
| $b$ | source term | m² s⁻² m⁻² = s⁻² |
| $E$ | error norm | depends on $u$ |
| $p$ | convergence order | dimensionless |

A useful sanity check on a Poisson solver for gravity: $b = 4\pi G\rho$ has
units $\mathrm{m^3kg^{-1}s^{-2}\cdot kg\,m^{-3}} = \mathrm{s^{-2}}$, matching
$\nabla^2\Phi$ with $[\Phi] = \mathrm{m^2s^{-2}}$ divided by $\mathrm{m^2}$. ✓

## 5. Assumptions

1. **Sufficient regularity** of the solution for the Taylor expansion. A
   discontinuous density field reduces the local order.
2. **Convergence to the correct solution**, not merely to *a* solution. The
   manufactured-solution test confirms this; refinemente alone does not (a
   consistent but wrongly-scaled scheme can converge to the wrong answer).
3. **Stability.** For time-dependent schemes, the time step must satisfy the
   stability limit (e.g. $dt \le h^2/(2D)$ for explicit diffusion).
4. **Round-off is below the discretisation error** for the grids used.

## 6. Worked examples (measured)

From `code/validation_benchmarks.py`, manufactured solution
$u = \sin\pi x\sin\pi y$ on the unit square with a sparse direct solve:

| $n$ | $h$ | $\max\lvert u_\text{num}-u_\text{exact}\rvert$ | measured order |
|---|---|---|---|
| 21 | 0.05 | $2.0587\times10^{-3}$ | — |
| 41 | 0.025 | $5.1420\times10^{-4}$ | 2.0013 |
| 81 | 0.0125 | $1.2852\times10^{-4}$ | 2.0003 |
| 161 | 0.00625 | $3.2128\times10^{-5}$ | 2.0001 |

Fitted log–log slope over all four grids: **2.000559**. The implementation is
second order, as intended, and the measurement says so.

**A test that cannot fail is not a test.** In Section 4 of the demo a deliberate
2% scaling error is injected into the prism kernel: the correct code passes a
$10^{-6}$ tolerance with a relative error of $3.98\times10^{-15}$, while the
buggy code fails with $2.000\times10^{-2}$. Inject a known error and confirm the
test rejects it.

**Round-off floor.** Gauss-Legendre quadrature of the prism integral gives
relative errors of $1.19\times10^{-2}$ at $n=4$, $1.51\times10^{-4}$ at 8,
$3.55\times10^{-8}$ at 16, then $8.5\times10^{-15}$ and $4.0\times10^{-15}$ at
32 and 64: it has hit the round-off floor near $10^{-15}$, and further refinement
buys nothing. **Set tolerances above the measured floor.**

## 7. Python demonstration

Run `code/validation_benchmarks.py`. It performs all three checks above (order
measurement, quadrature convergence, closed-form versus independent integral),
plus the deliberate-bug test, and prints the measured numbers. Predict the order
before running, then break the stencil (change the coefficient 4 to 4.01) and
confirm that the measured order collapses.

## 8. Exercises, mistakes, applications

Exercises: [`exercises/04-numerical-forward-modelling-exercises.md`](./exercises/04-numerical-forward-modelling-exercises.md).

**Common mistakes.** (1) Refining the grid and calling the change "convergence"
without measuring an order. (2) Attributing discretisation error to the physics.
(3) Using a tolerance below the round-off floor. (4) Forgetting that an
inconsistent scheme converges to the wrong answer. (5) Reporting a result with
no grid, no tolerance and no measured error.

**Applications.** Finite-difference and finite-element gravity/magnetic
modelling in complex 3-D geometry; finite-difference seismic wave propagation;
finite-element EM; all share this error taxonomy.

## Extended worked example: a second convergence study, in a different equation

The manufactured-solution test exercises an elliptic solver. A second study, on
the parabolic diffusion equation, confirms that the same discipline transfers to
time-dependent problems — and it exposes a different failure mode.

The problem is $\partial B/\partial t = D\,\partial^2B/\partial z^2$ on a
semi-infinite domain, forced by $B(0,t) = B_0\cos\omega t$, with the closed-form
solution $B(z,t) = B_0e^{-z/\delta}\cos(\omega t - z/\delta)$ and
$\delta = \sqrt{2D/\omega}$. Take $D = 7.9577\times10^{5}$ m²/s (equivalent to
$\sigma = 1$ S/m), $T = 100$ s, so $\delta = 5032.9$ m.

An explicit scheme requires $dt \le dz^2/(2D)$ for stability. The demonstration
uses the conservative $dt = 0.4\,dz^2/D$ and marches five periods, recording the
last period for analysis. Measured decay length against grid refinement:

| $n_z$ | $dz/\delta$ | measured $\delta$ (m) | relative error | measured phase lag (rad) | predicted $z/\delta$ |
|---|---|---|---|---|---|
| 31 | 0.200 | 5057.4 | $4.87\times10^{-3}$ | 0.832 | 0.800 |
| 61 | 0.100 | 5040.6 | $1.53\times10^{-3}$ | 0.696 | 0.700 |
| 121 | 0.050 | 5036.4 | $6.99\times10^{-4}$ | 0.749 | 0.750 |

Both amplitude and phase converge toward the closed-form values, and the error
falls monotonically with refinement — the signature of discretisation error, not
modelling error. The observed error ratio per halving of $dz$ is about 3.2 then
2.2, i.e. between first and second order, which is what mixed time (first-order,
Euler) and space (second-order, centred) errors produce.

**An earlier version of this demonstration was wrong, and the way it was wrong is
instructive.** The first attempt used a domain extending only to $3\delta$ and
fitted the decay over $[0.2\delta, 1.5\delta]$. The measured decay length
settled at 4830–4841 m, a *systematic* 3.8% error that did not vanish with
refinement. The cause was not the scheme: it was the artificial zero-flux
boundary at $3\delta$, where the field has only decayed to $e^{-3} = 5\%$, so
that boundary reflects. The profile matched $e^{-z/\delta}$ to better than 0.5%
inside $z<\delta$ but diverged beyond it. Extending the domain to $6\delta$
(where $e^{-6} = 0.25\%$) and fitting within $1.2\delta$ reduced the error to
$4.9\times10^{-3}$ and made it converge.

**The lesson generalises.** A residual that does not shrink with refinement is
not a discretisation error — it is either a modelling error (a boundary
condition, a truncated domain, an inconsistent scheme) or a round-off floor.
Distinguishing them is done by the log-log slope: round-off is flat, a domain or
boundary error plateaus at a value set by the geometry, and a genuine
discretisation error decreases at the scheme's order. Report the slope, not just
the error.

## 9. Further reading

- **LeVeque, R. J. *Finite Difference Methods for Ordinary and Partial
  Differential Equations*.** Level: graduate. The canonical treatment of
  truncation error, stability and convergence.
- **Roache, P. J. *Verification and Validation in Computational Science and
  Engineering*.** Level: graduate. Manufactured solutions and grid-convergence
  indices.
- **Salari, K. & Knupp, P. (2000).** Code verification by the method of
  manufactured solutions. Sandia Report SAND2000-1444. Level: graduate.

## 10. Related lessons

- [05-03-05 Validating Forward Codes Against Analytic Benchmarks](./05-forward-model-validation.md)
- [03-03-02 scipy.integrate](../../03-scientific-computing/03-scipy/02-integrate.md)
- [19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md)

## Self-assessment checklist

- [ ] I can derive the second-order truncation error of the 5-point Laplacian.
- [ ] I can measure a convergence order from two grid refinements.
- [ ] I can set up a manufactured solution for a solver I use.
- [ ] I can identify the round-off floor in a refinement study.
- [ ] I can state the grid, the tolerance and the measured error for any
      numerical result I report.
