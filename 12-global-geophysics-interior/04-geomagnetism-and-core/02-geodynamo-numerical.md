---
id: 12-04-02
title: "Numerical Geodynamo Models"
level: research
prereqs: ["08-01-05", "12-04-01", "12-02-04"]
tags: [global-geophysics, earth-interior, geodynamo, mhd, numerical-modelling, reversals]
---

# Numerical Geodynamo Models

**All models and data in this module are SYNTHETIC.** The control parameters are
adopted values, the low-order truncation is an invented teaching model, and no
published simulation, run name, code or output field is referred to. Every number
is printed by
[`code/geodynamo_numerical_demo.py`](./code/geodynamo_numerical_demo.py).

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** the Boussinesq magnetohydrodynamic system that a numerical dynamo
   solves, and **identify** which equation carries the magnetic field.
2. **Define** the Ekman, Rayleigh, Rossby, magnetic Prandtl and magnetic Reynolds
   numbers and **compute** each for an adopted parameter set.
3. **Explain** the two dimensionless numbers — $E \sim 10^{-15}$ and
   $Pm \sim 10^{-6}$ — that put the Earth's core out of reach of direct
   simulation, and **convert** the second into a grid-size requirement.
4. **Derive** the critical dynamo number of a two-mode $\alpha$–$\Omega$ model
   and **verify** its growth rate and its saturation amplitude against the
   analytic values.
5. **Interpret** a three-mode truncation's reversal statistics, and **state**
   why an individual reversal chronology is not reproducible while a rate is.
6. **Compute** the Elsasser number and **use** it to say whether a model is in
   the magnetostrophic regime that the Earth occupies.
7. **List** what verifies a dynamo model and what cannot verify it.

## Prerequisites

- [08-01-05 The Geodynamo: Mechanism and Evidence](../../08-geomagnetism-electromagnetism/01-earth-magnetic-field/05-dynamo-theory.md) —
  the induction equation, Cowling's theorem, the saturation argument and the
  energy budget. This lesson uses those results and does not re-derive them.
- [01 Observations of the Core Field and Secular Variation](01-core-field-observations.md) —
  the free-decay eigenvalue problem and the magnetic Reynolds number.
- [12-02-04 Core Composition, Light Elements and the Geodynamo](../02-composition-and-mineral-physics/04-core-composition.md) —
  the transport properties that set the dimensionless numbers.

## 1. The system that is actually solved

A numerical dynamo integrates, in a spherical shell between an inner and an outer
radius rotating at $\Omega$, four coupled equations. In the Boussinesq
approximation, with $\mathbf{u}$ the velocity, $\mathbf{B}$ the magnetic field,
$\Theta$ the temperature perturbation and $P$ the modified pressure:

$$\frac{\partial \mathbf{u}}{\partial t}
+ (\mathbf{u}\cdot\nabla)\mathbf{u}
+ 2\,\boldsymbol{\Omega}\times\mathbf{u}
= -\nabla P + Ra\,\Theta\,\hat{\mathbf{r}}
+ \frac{1}{Pm\,E}\left(\nabla\times\mathbf{B}\right)\times\mathbf{B}
+ \nabla^2\mathbf{u},$$

$$\frac{\partial \mathbf{B}}{\partial t}
= \nabla\times\left(\mathbf{u}\times\mathbf{B}\right)
+ \frac{1}{Pm}\nabla^2\mathbf{B},\qquad
\nabla\cdot\mathbf{u} = \nabla\cdot\mathbf{B} = 0,$$

$$\frac{\partial \Theta}{\partial t} + (\mathbf{u}\cdot\nabla)\Theta = q\nabla^2\Theta .$$

The second equation is the induction equation and only it can create field from
motion. Its two terms are, in order, **advection** and **diffusion**, and their
ratio is the magnetic Reynolds number $Rm = UL/\eta$ that
[01](01-core-field-observations.md) §6 measured to be about $2\times10^3$ for the
core. Every dynamo model is an attempt to sustain the first term against the
second on a grid small enough to resolve the structures that do it.

## 2. The dimensionless numbers, computed

With an adopted $\nu = 10^{-6}\ \mathrm{m^2\,s^{-1}}$,
$\sigma = 10^{6}\ \mathrm{S\,m^{-1}}$, $L = R_{\text{core}} = 3.48\times10^6\
\mathrm{m}$, $\Omega = 7.292\times10^{-5}\ \mathrm{s^{-1}}$ and
$U = 5\times10^{-4}\ \mathrm{m\,s^{-1}}$:

| Number | Definition | Value |
|---|---|---|
| Ekman | $E = \nu/(\Omega L^2)$ | $1.13\times10^{-15}$ |
| magnetic Prandtl | $Pm = \nu/\eta$ | $1.26\times10^{-6}$ |
| Rayleigh | $Ra = \alpha g\Delta T L^3/(\kappa\nu)$ | $6.20\times10^{30}$ |
| Rossby | $Ro = U/(\Omega L)$ | $1.97\times10^{-6}$ |
| magnetic Reynolds | $Rm = UL/\eta$ | 2187 |

Read the first two together, because they are the reason the problem is hard.

- $E \sim 10^{-15}$ means the viscous boundary layers are of thickness
  $\sqrt{\nu/\Omega} \sim 4$ m inside a 3480-km body — five orders of magnitude
  thinner than the shell. No global simulation resolves them.
- $Pm \sim 10^{-6}$ means momentum diffuses a million times faster than the field.
  At equal time the magnetic diffusion length exceeds the viscous one by
  $\sqrt{\eta/\nu} = \sqrt{1/Pm} = 892$, so a grid that resolves both needs of
  order $892^3 = 7.1\times10^{8}$ points — and that is before the small-scale
  flow structures are considered.

The practical consequence is that every published dynamo runs at
$Pm \sim 0.1$–$10$ and $E \sim 10^{-4}$–$10^{-8}$, i.e. **nine orders of
magnitude away from the core in $Pm$**. The adopted $Ra$, computed from molecular
diffusivities, is meaningless as a "value for the core"; it is quoted to show how
far outside the resolved regime the planet sits.

## 3. What a low-order truncation can and cannot show

A full simulation is not needed to see the *mechanism*, and a truncation makes
the mathematics checkable, which is its whole value.

### 3.1 Two modes: the critical dynamo number

Take one poloidal amplitude $P$ and one toroidal amplitude $T$:

$$\frac{\mathrm{d}P}{\mathrm{d}t} = \alpha T - \kappa P,\qquad
\frac{\mathrm{d}T}{\mathrm{d}t} = \omega P - \kappa T .$$

This is the smallest system that contains both the $\alpha$-effect (poloidal
field made from toroidal) and the $\Omega$-effect (toroidal from poloidal). Its
matrix is $\begin{pmatrix}-\kappa & \alpha\\ \omega & -\kappa\end{pmatrix}$, so
the growth rates are

$$\sigma = -\kappa \pm \sqrt{\alpha\omega},\qquad
\text{onset when}\quad D \equiv \frac{\alpha\omega}{\kappa^2} \ge 1 .$$

The demonstration measures $\sigma$ by integrating the linear system and fitting
an exponential, and compares with the closed form:

| $D$ | $\sigma$ analytic | $\sigma$ measured | behaviour |
|---|---|---|---|
| 0.50 | −0.292893 | −0.292893 | decay |
| 0.90 | −0.051317 | −0.051317 | decay |
| 1.00 | 0.000000 | 0.000000 | neutral |
| 1.21 | 0.100000 | 0.100000 | growth |
| 1.50 | 0.224745 | 0.224745 | growth |
| 2.00 | 0.414214 | 0.414214 | growth |

The agreement is to all printed digits. The critical dynamo number is therefore
a *measured* property of the truncation and a *derived* property of the algebra,
which is what makes the truncation useful as a testbed: any error in the
implementation of the $\alpha$- or $\Omega$-term shows up immediately.

### 3.2 Saturation as a prediction, not a fit

A linear dynamo grows without bound, so real dynamos need a saturation
mechanism. The standard one is $\alpha$-quenching: the helical motion that
generates the poloidal field is itself impeded by the field it makes,

$$\alpha = \frac{\alpha_0}{1 + (P^2 + T^2)/B_{\text{sat}}^2}.$$

At saturation both derivatives vanish, giving $P = \alpha T$, $T = \omega P$, and
then $\alpha_0/(1 + A^2)\cdot\omega = \kappa$, i.e.

$$A^2 = D - 1,\qquad A = \sqrt{D - 1}.$$

For $D = 4.0$ the demonstration measures $A = 1.732051$ against the prediction
$\sqrt{3} = 1.732051$, agreeing to $7.6\times10^{-12}$. **The saturation amplitude
is a prediction of the truncation, so a model that gets it wrong has a bug, not a
surprise.**

### 3.3 Three modes: reversals

A two-mode model cannot reverse: it saturates to a steady state or a single
oscillation. The transition to reversing behaviour needs nonlinearity of a
different kind — a triadic interaction, as in the classic three-mode truncation
that the dynamo literature shares with the Lorenz system:

$$\frac{\mathrm{d}X}{\mathrm{d}t} = -\sigma(X - Y),\qquad
\frac{\mathrm{d}Y}{\mathrm{d}t} = rX - Y - XZ,\qquad
\frac{\mathrm{d}Z}{\mathrm{d}t} = XY - bZ .$$

$X$ plays the role of the poloidal field and $r$ of the dynamo number. The
demonstration integrates it for 300 time units and measures sign changes of $X$
between 150 and 300:

| $r$ | reversals | rate (per unit time) | rms($X$) | mean($X$) |
|---|---|---|---|---|
| 14 | 0 | 0.000 | 5.888 | −5.888 |
| 22 | 0 | 0.000 | 7.483 | −7.483 |
| 26 | 60 | 0.400 | 7.634 | −0.744 |
| 32 | 98 | 0.653 | 8.567 | −1.217 |
| 50 | 140 | 0.933 | 10.990 | −0.040 |

The structure of the table is the physics: at low $r$ the field sits on a
non-trivial steady branch with $|X| = \sqrt{b(r-1)}$ — the demonstration verifies
that to $6\times10^{-10}$ — and never reverses; above $r \approx 24.7$ the field
wanders chaotically and reverses. **Reversals are a property of the nonlinear
regime, not of a persistent "field flip" mechanism.**

Three realisations at $r = 32$ give reversal rates 0.893, 0.820 and 0.887, a
spread of 4% — but the sweep's own realisation at the same $r$ gave 0.653 with a
25% smaller rms field. The same parameters support metastable states, so:

- a **rate** is a reproducible statistic, if the window is long enough;
- an **individual reversal chronology** is not reproducible at all.

That distinction is the single most transferable idea in this lesson. A model can
never predict *when* a reversal happens; it can only predict how often, and only
with an error bar that reflects the finite length of the record.

## 4. The Elsasser number, and the regime problem

The Elsasser number measures the Lorentz force against the Coriolis force,

$$\Lambda = \frac{B^2}{\mu_0\rho\eta\,\Omega}.$$

With an adopted $\rho = 1.1\times10^4\ \mathrm{kg\,m^{-3}}$:

| adopted $B$ | $\Lambda$ |
|---|---|
| 5.0 mT | 31.2 |
| 0.5 mT | 0.312 |

The Earth's core is believed to be in the regime $\Lambda \sim 1$–$10$
(magnetostrophic: rotation and magnetic forces comparable). Present-day
simulations, forced to run at much larger $Pm$ and much smaller $Ra$ than the
core, typically report $\Lambda \sim 0.1$: their fields are too weak relative to
rotation. This is the honest statement of the field's central limitation —

> **a numerical dynamo is not a scaled model of the Earth's core. It is a
> physically consistent solution of the same equations in a different corner of
> parameter space.**

Scaling studies convert one corner into another by power laws fitted to suites of
runs, and the *exponent* of those laws becomes the real result. Since the fitted
exponents depend on which runs are included, the uncertainty in an extrapolated
core field strength is dominated by systematic choices, not by numerical
precision.

## 5. What verifies a dynamo model, and what cannot

Verification, in the sense of "the code solves the equations", is done against:

1. **Analytic limits.** The free-decay eigenvalue problem of
   [01](01-core-field-observations.md) §6 has closed-form roots ($x = \pi$ for
   $l = 1$); the demonstration reproduces it to $2.2\times10^{-16}$. The
   two-mode dynamo's growth rate and saturation amplitude are closed-form; the
   demonstration reproduces both.
2. **Benchmarks.** The standard practice is to run a fixed parameter set agreed
   by several independent codes and compare a set of scalar diagnostics (mean
   field energy, ohmic dissipation, drift rate, Nusselt number). Agreement to a
   few per cent across codes is the strongest available statement about a
   simulation, because it tests the *discretisation*, not the physics.
3. **Conservation and symmetry.** $\nabla\cdot\mathbf{B} = 0$ must hold to
   machine accuracy; the Nusselt number must equal the total heat flux minus the
   conductive part; the solution must respect the symmetries of the forcing.

What cannot verify a dynamo model is a match to the Earth's observable field.
A model with the wrong $Pm$ can be tuned to produce a dipole of the right
strength, the right tilt and even a realistic reversal rate, because the
observable set has far fewer independent constraints than the model has
parameters. **The Earth is the target, not the test.**

## 6. Assumptions and regime of validity

1. **Boussinesq.** Density variations are neglected except in the buoyancy term.
   For a 3480-km liquid shell with a real density contrast this is a
   simplification; anelastic approximations are used to relax it.
2. **The relevant diffusivities are molecular.** A turbulent simulation would
   need to resolve the turbulence; instead, larger-than-real $\nu$ and $\kappa$
   are adopted, which is precisely the $Pm$ problem of §2.
3. **Low-order truncations are qualitative.** The two- and three-mode systems
   used here contain the mechanism and none of the geometry. Their coefficients
   are *chosen*; only their behaviour is physics.
4. **The Elsasser number comparison assumes uniform $B$ and $\sigma$.** Both vary
   with radius in a real core.
5. **Reversal rates from a truncation are not transferable.** The demonstration's
   rates depend on the adopted $r$, on the window length and on the initial
   condition — all three of which are choices.
6. **The demos are not simulations.** They solve small ODE systems exactly and
   cheaply; they are checkable, and the price of that checkability is that they
   say nothing quantitative about the core.

## 7. Mastery checkpoint

Without notes:

> A two-mode dynamo has $\kappa = 1$, $\alpha = 2.0$ and $\omega = 2.0$ at onset
> parameters, with $\alpha$-quenching of amplitude $B_{\text{sat}} = 1$.
> **(a)** Compute $D$ and the linear growth rate. **(b)** State whether the system
> grows and by what factor over ten time units. **(c)** Compute the saturation
> amplitude analytically. **(d)** Explain in one sentence why the model cannot
> reverse. **(e)** Compute the Elsasser number for $B = 1\ \mathrm{mT}$ with the
> adopted core properties and say whether the model is in the Earth's regime.

## 8. Common pitfalls

1. **Treating a simulation's parameters as the core's.** $E$ and $Pm$ differ by
   orders of magnitude, and that difference is the field's main limitation.
2. **Fitting $Pm$ by raising resolution.** The requirement scales as $Pm^{-3/2}$
   in three dimensions; a factor of ten in $Pm$ is a factor of $10^{1.5} = 32$ in
   grid points per direction, and much more in cost.
3. **Reporting a reversal rate without the window.** Rates converge slowly and
   metastable states are real; a single window is a sample, not a rate.
4. **Confusing a benchmark with a validation.** Cross-code agreement tests the
   discretisation; matching the Earth tests nothing if the parameters are wrong.
5. **Reading a low-order model's coefficients as physical.** They are chosen to
   produce the right qualitative behaviour.
6. **Assuming a strong-field dynamo.** Whether the saturated state is
   magnetostrophic ($\Lambda \gtrsim 1$) or weak-field is an outcome of the
   simulation, not an input.

## 9. Related modules

- [01 Observations of the Core Field and Secular Variation](01-core-field-observations.md) —
  the observational constraints, the free-decay problem and the $Rm$ argument.
- [03 Palaeomagnetic Record and Reversal Frequency](03-palaeomagnetic-record.md) —
  what the reversal statistics of the real field look like.
- [08-01 The Earth's Magnetic Field](../../08-geomagnetism-electromagnetism/01-earth-magnetic-field/README.md) —
  the induction equation and the geodynamo's energy budget.
- [12-02 Composition and Mineral Physics](../02-composition-and-mineral-physics/README.md) —
  the transport properties and the core's thermal state.
- [12-03 Geotherms and the Earth's Heat Budget](../03-geotherms-and-heat-budget/README.md) —
  the heat flow that drives the convection.
- [19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md) — the
  solvers, stiffness and parallelisation that a real dynamo needs.
