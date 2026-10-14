---
id: 13-02-02
title: "Numerical Modelling of Mantle Convection"
level: research
prereqs: ["13-02-01", "03-12-01", "03-12-02"]
tags: [geodynamics, tectonophysics, mantle-convection, numerical-methods, verification, nusselt-number]
---

# Numerical Modelling of Mantle Convection

> All models and data in this module are **SYNTHETIC**. The solver below is a
> teaching model: every Rayleigh number, grid and perturbation is chosen, and
> every number quoted here is printed by
> `code/convection_numerical_demo.py`.

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** the Boussinesq convection equations in streamfunction–vorticity form
   and **explain** why that formulation removes the pressure and enforces
   incompressibility exactly.
2. **Implement** a Poisson solve that is spectral in one direction and
   tridiagonal in the other, and **verify** it against an analytic field.
3. **Verify** a convection code against linear theory by measuring the onset
   Rayleigh number and comparing it with $27\pi^{4}/4$.
4. **Measure** the Nusselt number as a function of $Ra$, **report** the local
   logarithmic slopes, and **state** why the global fit is not the asymptotic
   exponent.
5. **Quantify** the time-step error by extrapolating a measured growth rate to
   $\Delta t\to0$, and **state** why the *sign* of the growth rate is
   $\Delta t$-independent.
6. **Check** the energy balance of a solution with a heat-flux profile that must
   be constant in depth, and **interpret** the residual honestly.
7. **Assess** grid dependence and **list** the physical processes the model omits,
   with the order of magnitude each would change $Nu$.

## Prerequisites

- [13-02-01 Rayleigh-Benard Convection Applied to the Mantle](01-rayleigh-benard-mantle.md) —
  the dimensionless problem and $Ra_c$ that this solver verifies.
- [03-12-01 A 1-D Finite-Difference Solver from Scratch](../../03-scientific-computing/12-numerical-simulation-python/01-finite-difference-1d.md) —
  the discretisation vocabulary.
- [03-12-02 Numerical Stability, CFL Conditions and Convergence Testing](../../03-scientific-computing/12-numerical-simulation-python/02-stability-and-cfl.md) —
  the stability constraints used for the time step.
- [19-02-01 Finite-Difference Methods](../../19-numerical-modeling-hpc/02-finite-difference-methods/01-fd-derivation.md) —
  the systematic treatment of accuracy and stencils.

## 1. Intuition: a linear solve per time step

Two facts make mantle convection tractable numerically, and both come from
[13-01-01 §3](../01-geodynamic-principles/01-momentum-mass-energy.md).

First, because inertia is negligible, the velocity field is a *diagnostic*
function of the temperature field: at every instant the flow is the solution of a
linear Stokes problem with the buoyancy as its right-hand side. There is no
equation of motion to integrate.

Second, in two dimensions an incompressible flow has a streamfunction, and the
whole Stokes problem collapses to a single scalar equation:

$$\nabla^{4}\psi = -Ra\,\frac{\partial T}{\partial x}
\qquad\Longleftrightarrow\qquad
\nabla^{2}\omega = Ra\,\frac{\partial T}{\partial x},\quad
\nabla^{2}\psi = \omega .$$

So a time step of a convection code is: transform the temperature, solve two
Poisson problems, differentiate the streamfunction to get the velocity, and
advance the temperature. The difficulty is not conceptual but practical — the
same Poisson problem must be solved thousands of times, so it must be both fast
and accurate, and the advection must be stable without smearing the boundary
layers that carry all the physics.

## 2. The discretisation

### 2.1 Geometry, bases and boundary conditions

The demonstration uses a box $x\in[0,\,2\sqrt{2}]$ periodic in $x$, $z\in[0,1]$
with free-slip and isothermal boundaries, on a $49\times49$ grid. The width is the
critical wavelength of §[13-02-01 §3.2](01-rayleigh-benard-mantle.md), so the box
admits exactly one roll at onset and the comparison with linear theory is
unambiguous.

Two choices carry the accuracy:

- **Spectral in $x$.** A Fourier transform turns $\partial_x$ into a
  multiplication by $ik$ and $\partial_x^{2}$ into $-k^{2}$. The $x$-derivatives
  are then exact for the resolved modes, and the Poisson operator becomes
  mode-diagonal.
- **Tridiagonal in $z$.** For each wavenumber $k_m$, the equation
  $(D^{2} - k_m^{2})X = f$ with Dirichlet data is a tridiagonal linear system,
  solvable exactly by the Thomas algorithm. There is no iteration and no
  tolerance to choose, which removes an entire class of "did it converge?"
  questions.

The vertical velocity and vorticity vanish on free-slip boundaries
($\psi = \psi'' = 0$ implies $\omega = 0$), so both Poisson problems have
homogeneous Dirichlet data and the same operator — factor once, use twice.

### 2.2 Verification of the solver

Before any physics, verify the linear algebra against a field whose answer is
known. With $\psi = \sin(\pi z)\sin(kx)$ and $f = -(k^{2}+\pi^{2})\psi$, solving
the discrete problem gives

$$\max|\psi_{\text{numeric}} - \psi_{\text{exact}}|\big/
\max|\psi_{\text{exact}}| = 1.38\times10^{-4}.$$

That residual is not solver error: it is the difference between the discrete
Laplacian eigenvalue $2(1-\cos\pi\Delta z)/\Delta z^{2} = 9.872$ and the
continuum $\pi^{2} = 9.8696$, a relative difference of $2\times10^{-4}$ in the
operator, which propagates as $1.4\times10^{-4}$ into the solution. Recognising
this distinction is what separates verification from wishful thinking: a spectral
method can only be as good as its grid at representing the operator, and a
$1.4\times10^{-4}$ error is *expected* here, not tolerated.

### 2.3 Time stepping

The temperature equation is advanced with an implicit treatment of diffusion and
an explicit, first-order upwind treatment of advection:

$$\frac{T^{n+1} - T^{n}}{\Delta t} = \nabla^{2}T^{n+1}
- \mathbf{u}^{n}\cdot\nabla T^{n} .$$

Two consequences, both measured later:

- **Implicit diffusion removes the diffusive stability limit**, so the time step
  is set only by advection: $\Delta t \le \mathrm{CFL}\min(\Delta x,\Delta z)/|u|_{\max}$.
  The demonstration uses $\mathrm{CFL} = 0.7$.
- **Explicit advection introduces an $O(\Delta t)$ error in the growth rate**,
  which is why §4 extrapolates to $\Delta t \to 0$ rather than quoting a single
  number.

A detail of implementation that costs hours if missed: NumPy's `rfft` is
unnormalised, so the mean-mode coefficient of a uniform row of 1.0 is $N_x$, not
1. The inhomogeneous bottom boundary condition, when moved to the right-hand side
of the interior equations, must carry the same factor. Getting this wrong
produced a spurious interior cooling of exactly $1/N_x$ in an earlier version of
this code — a reminder that boundary conditions in transform space are where
implementation bugs hide.

## 3. Verification against linear theory: the onset

### 3.1 Measuring the growth rate

Start from the conducting state plus a random perturbation of rms
$10^{-6}$ and fit $\ln(\text{amplitude})$ against time over the samples that lie
inside an amplitude window around the initial value (so the fit sees only the
linear regime, and only after the non-fundamental modes seeded by the noise have
decayed). Measured at $\Delta t = 0.005$:

| $Ra$ | 500 | 620 | 680 | 700 | 800 | 1200 |
|---|---|---|---|---|---|---|
| $\sigma$ (per diffusive time) | $-3.4299$ | $-0.8521$ | $+0.4012$ | $+0.8171$ | $+2.8835$ | $+10.9396$ |
| $\sigma/\left[(Ra-Ra_c)/Ra_c\right]$ | — | — | 13.851 | 13.796 | 13.696 | 13.409 |

Bisecting on $\sigma(Ra) = 0$ gives the model's own critical value:

$$Ra_c^{\text{model}} = 660.86
\qquad\text{against}\qquad
27\pi^{4}/4 = 657.511,$$

a difference of **0.51%**, which is the spatial discretisation error of a
$49\times49$ grid — the same order as the $1.4\times10^{-4}$ operator error
amplified by the cubic sensitivity of $Ra_c$ to the vertical eigenvalue.

Two results are worth extracting.

- **The bifurcation is stationary and linear near onset.** The ratio
  $\sigma/[(Ra-Ra_c)/Ra_c]$ is 13.8, 13.8, 13.7, 13.4 across a fivefold range of
  distance from onset: $\sigma$ is proportional to the excess Rayleigh number, as
  the linearised theory predicts. The gentle downward drift at the largest
  distance is the expected nonlinear correction.
- **The sign of $\sigma$ is $\Delta t$-independent.** The implicit-diffusion,
  explicit-advection scheme has zero growth exactly when $(1+\Delta t\,C) =
  (1+\lambda\Delta t)$, i.e. when the destabilising coupling $C$ equals the
  diffusive eigenvalue $\lambda$ — precisely the marginal condition of the
  continuum problem. So a bisection on $\sigma = 0$ measures the *spatial*
  discretisation error without contamination from the time step. That is a
  property of this scheme, not a general truth, and it is worth checking
  explicitly for any scheme before trusting such a test.

### 3.2 The time-step error, measured

The *magnitude* of $\sigma$ does depend on $\Delta t$, because advection is
explicit. The demonstration quantifies it at $Ra = 800$:

| $\Delta t$ | measured $\sigma$ | analytic $\sigma$ |
|---|---|---|
| 0.02 | 2.3486 | 3.2082 |
| 0.005 | 2.8831 | 3.2082 |
| 0.0025 | 2.9967 | 3.2082 |

A linear extrapolation to $\Delta t\to0$ gives $\sigma(0) = 3.0880$ against the
analytic single-mode value

$$\sigma = -(\pi^{2}+k_c^{2}) + \frac{Ra\,k_c^{2}}{(\pi^{2}+k_c^{2})^{2}}
= 3.2082 ,$$

an agreement of **3.7%**. Without the extrapolation, the coarsest run is 27% low
— and would have been reported as a 27% disagreement with theory. The lesson is
general: any explicit-advection measurement of a growth rate must carry its
$\Delta t$ dependence, and the cheapest honest fix is a two- or three-point
extrapolation.

## 4. The Nusselt number and its scaling

### 4.1 Measurement

$Nu$ is the surface heat flux in conductive units, $-\partial_z T|_{z=1}$. Each
run starts from the fundamental roll and is integrated until the flux is steady;
the spread over the second half of the run is reported as the convergence
measure.

| $Ra$ | $Nu$ | spread in the last half | $(Ra/Ra_c)^{1/3}$ | $Nu/\,\text{pred}$ |
|---|---|---|---|---|
| 1000 | 1.651 | $5.19\times10^{-3}$ | 1.150 | 1.435 |
| 3000 | 3.103 | $7.51\times10^{-5}$ | 1.659 | 1.871 |
| 10000 | 4.741 | $3.55\times10^{-4}$ | 2.478 | 1.914 |
| 20000 | 5.862 | $6.25\times10^{-4}$ | 3.122 | 1.878 |

The global fit over the range is

$$Nu = 0.099\,Ra^{0.418},$$

but the global exponent is *not* the interesting number. The local logarithmic
slopes are

| interval | local slope |
|---|---|
| 1000 → 3000 | 0.574 |
| 3000 → 10000 | 0.352 |
| 10000 → 20000 | 0.306 |

and the slope is decreasing towards the boundary-layer value $1/3$. The
interpretation is quantitative: near onset the weakly nonlinear term
($Nu-1\propto(Ra-Ra_c)/Ra_c$) dominates and steepens the apparent exponent,
while the asymptotic boundary-layer regime has not yet been reached at
$Ra = 2\times10^{4}$. A paper that fit $Nu\propto Ra^{0.42}$ over this range and
called it a scaling law would be reporting a crossover, not an asymptote. The
right way to present this measurement is as a *local* exponent that is still
evolving, with the range of $Ra$ stated.

The prefactor, 1.88 at the highest $Ra$, is the quantity that scaling theory
could not supply. Comparing with
[13-02-01 §4](01-rayleigh-benard-mantle.md): the exponent comes from a
boundary-layer balance, the coefficient requires solving the boundary layer, and
a numerical model is the cheapest way to do so. A prefactor of 1.9 rather than 1
is a genuine result about free-slip convection in a critical-wavelength box, not
an error.

### 4.2 Boundary-layer thickness

With equal top and bottom boundary layers the flux defines a thickness
$\delta = 1/(2Nu)$; the prediction is $(Ra_c/Ra)^{1/3}$:

| $Ra$ | $Nu$ | $\delta = 1/(2Nu)$ | $(Ra_c/Ra)^{1/3}$ | ratio |
|---|---|---|---|---|
| 1000 | 1.651 | 0.3029 | 0.8696 | 0.35 |
| 3000 | 3.103 | 0.1611 | 0.6029 | 0.27 |
| 10000 | 4.741 | 0.1055 | 0.4036 | 0.26 |
| 20000 | 5.862 | 0.0853 | 0.3203 | 0.27 |

The cube-root law is followed — the *shape* of the dependence is right — with a
nearly constant ratio of 0.26–0.27 (and 0.35 at the lowest $Ra$, where the
asymptotic law does not apply). The constant is the same $O(1)$ prefactor
appearing in $Nu$; it is the boundary-layer structure, not the exponent, that
the model actually computes.

## 5. Energy balance: a flat flux is a strong test

The exact Boussinesq solution has a heat flux that is independent of depth:

$$\overline{q}(z) = -\left\langle\frac{\partial T}{\partial z}\right\rangle
+ \langle wT\rangle = Nu \quad\text{for all } z ,$$

where the angle brackets are horizontal averages. This is a much stronger
statement than "the flux at the top equals the flux at the bottom", because it
constrains the interior too. Measured:

| $Ra$ | flux at top | flux at bottom | top–bottom | max deviation |
|---|---|---|---|---|
| 1000 | 1.6520 | 1.6526 | $3.6\times10^{-4}$ | $2.6\times10^{-2}$ |
| 3000 | 3.1028 | 3.1047 | $6.5\times10^{-4}$ | $8.9\times10^{-2}$ |
| 10000 | 4.7396 | 4.7591 | $4.6\times10^{-3}$ | $1.5\times10^{-1}$ |
| 20000 | 5.8597 | 5.9272 | $1.2\times10^{-2}$ | $2.0\times10^{-1}$ |

The global balance is satisfied to between 0.04% and 1.2% — good. The maximum
*local* deviation is 2.6% to 20%, and it grows with $Ra$. Where does it live?
Inside the boundary layers, where the first-order upwind scheme's numerical
diffusion is largest relative to the physical diffusion, and where the grid
resolves the gradient with the fewest points. Reporting both numbers, and
explaining the difference, is the difference between a conservation check and a
box-tick.

## 6. Resolution: measuring the discretisation error

Same physics, same $Ra = 3000$, two grids:

| grid | $\Delta z$ | $Nu$ | max flux deviation |
|---|---|---|---|
| $49\times49$ | 0.02083 | 3.103 | $8.9\times10^{-2}$ |
| $65\times65$ | 0.01562 | 3.132 | $6.7\times10^{-2}$ |

$Nu$ changes by 0.9% and the flux deviation falls by a quarter. First-order
upwind advection is diffusive, so the flux is *under*-predicted on the coarse
grid and converges upwards. Two conclusions:

- The measurement is grid-limited at the 1% level at $Ra = 3000$ on these grids,
  which is the honest error bar to attach to §4.1's numbers.
- Because the scheme's leading error is a numerical diffusion, its effect is to
  *smooth* boundary layers and to *reduce* the flux. A higher-order advection
  scheme would converge faster but can produce oscillations at sharp interfaces;
  the trade-off is a design decision that must be stated in any code comparison.

## 7. Assumptions and what the model leaves out

| omission | expected effect on $Nu$ |
|---|---|
| temperature-dependent viscosity | large: a stiff lid reduces flux by tens of per cent or more |
| internal heating | changes the exponent and the asymmetry of the boundary layers |
| a high-viscosity plate-like lid | suppresses surface motion; changes the planform |
| three dimensions | allows sheet-like downwellings; $Nu$ changes by tens of per cent |
| phase transitions, melting | local buoyancy and latent-heat terms modify $Ra$ locally |
| compressibility | modifies the adiabatic gradient and the buoyancy |

None of these is a small perturbation. That is why benchmarking against agreed
cases — the same problem solved by several codes with the same physics — is a
discipline of its own
([13-05-03](../05-geodynamic-modelling/03-benchmarking-geodynamics.md),
[19-07-01](../../19-numerical-modeling-hpc/07-verification-validation-uncertainty/01-code-verification.md)).
A convection code that has not been run against a benchmark has not been tested;
it has only been run.

## 8. Units, scaling and the practical checklist

| quantity | symbol | unit in the code | dimensional value |
|---|---|---|---|
| length | $z$ | 1 = $d$ | 2900 km |
| time | $t$ | $d^{2}/\kappa$ | 267 Gyr (!) |
| velocity | $\mathbf{u}$ | $\kappa/d = 3.45\times10^{-10}$ m s$^{-1}$ | — |
| temperature | $T$ | 1 = $\Delta T$ | 1300 K |
| flux | $Nu$ | 1 = $k\Delta T/d$ | $1.4\times10^{-3}$ W m$^{-2}$ |

The nondimensional time unit is worth pausing on: one unit is 267 Gyr, so the
$t_{\text{end}} = 1$ integrations in §4 are not "short" in any physical sense —
they are longer than the age of the Universe in the pure diffusive scaling. That
is a statement about how useless the diffusive timescale is as a clock for the
mantle, and it is why the convective (overturn) time is the relevant unit.

**Checklist before believing a convection number.** State (1) the nondimensional
form and the definition of $Nu$; (2) the boundary conditions; (3) the grid and
the advection scheme; (4) the time step and its CFL number; (5) the convergence
measure and its value; (6) the energy-balance residual; and (7) at least one
independent verification, such as the onset $Ra_c$ compared with $27\pi^{4}/4$.

## 9. The demonstration

`code/convection_numerical_demo.py` is a complete, self-contained solver:

```bash
cd 13-geodynamics-tectonics/02-mantle-convection/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python convection_numerical_demo.py
```

It prints the discretisation and the verified Poisson error; measures the onset
of convection by bisection on the growth rate and compares with $27\pi^{4}/4$;
extrapolates the growth rate to $\Delta t\to0$; measures $Nu(Ra)$ with local
slopes and boundary-layer thicknesses; checks the flux-profile energy balance;
runs a two-grid resolution study; and lists the omitted physics. Runtime is about
15 s, it is print-only, uses a fixed seed, needs no network, and exits 0.

Exercises:
[`exercises/02-convection-numerical-exercises.md`](exercises/02-convection-numerical-exercises.md)
and
[`exercises/02-convection-numerical-solutions.md`](exercises/02-convection-numerical-solutions.md).

## Mastery checkpoint

Complete this without notes.

> You inherit a 2-D convection code that reports $Nu = 12.4$ at $Ra = 10^{6}$ in a
> $2.83\times1$ box with free-slip boundaries, using first-order upwind advection
> on a $65\times65$ grid with $\mathrm{CFL} = 0.9$ and a single run to
> $t_{\text{end}} = 0.5$.
> **(a)** List the four checks you would run before believing the number, in
> order, and say what each would reveal. **(b)** The code's onset test gives
> $Ra_c = 690$. Is that a bug? Justify with a number from this lesson.
> **(c)** Explain why the sign of the measured growth rate is a more robust
> diagnostic than its magnitude. **(d)** State one piece of physics whose
> omission could plausibly account for a factor-of-two error in $Nu$, and how you
> would test the claim.

A worked version appears in the
[solutions](exercises/02-convection-numerical-solutions.md).

## Common pitfalls

1. **Reporting $Nu$ without a convergence measure.** Without the spread you
   cannot tell a steady state from a slowly drifting one.
2. **Fitting a single exponent over a crossover.** The local slopes here range
   from 0.57 to 0.31; there is no single exponent.
3. **Quoting a growth rate at one $\Delta t$.** Explicit advection gives an
   $O(\Delta t)$ error; extrapolate.
4. **Forgetting the FFT normalisation for boundary terms.** It produces an
   interior drift of exactly $1/N$.
5. **Confusing a flux *balance* check with a *profile* check.** The top–bottom
   agreement can be excellent while the interior profile deviates by 20%.
6. **Comparing $Nu$ across codes with different $Nu$ definitions.** Is $Nu$ the
   surface flux, the volume-averaged dissipation, or the boundary-layer
   estimate? They differ by the $O(1)$ coefficients.
7. **Treating a small grid dependence as proof of convergence.** A 1% change
   between two grids is consistent with a first-order error whose remaining
   contribution is 1%; it does not demonstrate the error is small.

## Related modules

- [13-02-01 Rayleigh-Benard Convection Applied to the Mantle](01-rayleigh-benard-mantle.md) —
  the theory this code verifies and extends.
- [13-02-03 Mantle Plumes, Hotspots and Large Igneous Provinces](03-mantle-plumes.md) —
  what happens when the instability is discrete rather than a layer.
- [13-02-04 Subduction Dynamics, Slab Geometry and Slab Pull](04-subduction-dynamics.md) —
  the other half of the convective cycle.
- [13-05-02 Solving the Stokes Equations for Mantle Flow](../05-geodynamic-modelling/02-stokes-flow-solvers.md) —
  how the linear solve is generalised to variable viscosity and 3-D.
- [19-03-01 Finite Element and Finite Volume Methods](../../19-numerical-modeling-hpc/03-finite-element-and-volume/01-fem-weak-form.md) —
  the alternative discretisation families.
