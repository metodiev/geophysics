---
id: 16-05-02
title: "GCMs, Resolution and Parameterisation"
level: research
prereqs: ["16-05-01", "16-03-01", "01-12-07"]
tags: [atmosphere, climate, climate-models, gcm, resolution, parameterisation, numerical-diffusion]
---

# GCMs, Resolution and Parameterisation

> All models and data in this module are **SYNTHETIC**. Every number below was
> printed by
> [`code/gcms_and_parameterisation_demo.py`](code/gcms_and_parameterisation_demo.py).
> The column, the advection problem and the two convective closures are teaching
> constructions; the only standard constants used are the gravitational
> acceleration and the specific heat of dry air.

## Learning objectives

By the end of this lesson you will be able to:

1. **Distinguish** the resolved part of a general circulation model (the
   dynamical core) from the parameterised part (the physics package), and
   **name** the quantities each handles.
2. **Derive** the modified equation of the first-order upwind advection scheme
   and show that it is a diffusion equation with a numerical diffusivity
   $K_{\text{num}} = \tfrac{1}{2}u\,\Delta x(1-C)$.
3. **Measure** that diffusivity from a numerical experiment and **compare** it
   with the analytic value.
4. **Explain** why numerical diffusion is a resolution property, not a bug, and
   **quantify** how it scales with grid spacing.
5. **Construct** an energy-conserving convective adjustment and **demonstrate**
   that two such closures disagree on the final state.
6. **Define** effective resolution and **compare** it with the physical scale of
   convection, clouds, turbulence and gravity waves.
7. **State** the structural uncertainty that parameterisation introduces into a
   simulated climate, and why it does not vanish as resolution increases.

## Prerequisites

- [16-05-01 Model Hierarchy: EBMs, EMICs, GCMs, ESMs](01-climate-model-hierarchy.md) —
  what a model is defined by, and what a closure is.
- [16-03-01 Global Circulation](../03-atmospheric-circulation/01-global-circulation.md) —
  the circulation the dynamical core resolves.
- [01-12-07 PDE Discretisation](../../01-mathematics/12-numerical-methods/07-pde-discretisation.md) —
  finite differences, truncation error and stability.

## 1. Intuition: a grid that cannot see a cloud

A general circulation model solves approximations of the equations of motion,
mass continuity, thermodynamics and moisture on a grid covering the globe. The
grid spacing, not the physics, decides what the model can actually see. A
feature smaller than a few grid spacings is invisible; its net effect on the
resolved scales must nevertheless be present, or the model's energy and moisture
budgets will be wrong.

The response to that is a **parameterisation**: a rule that estimates the
sub-grid flux from resolved variables. Cloud microphysics, convection, boundary
layer turbulence, gravity-wave drag, radiative transfer through an unresolved
spectrum and land-surface exchange are all parameterised in every climate model
in routine use.

That sentence contains the whole difficulty of this lesson. A parameterisation
is a *closure* — an assumption about unresolved physics, written as a formula
with coefficients. It is not a measurement, and two closures consistent with the
same resolved budgets can produce different climates. Increasing resolution
moves the boundary between resolved and parameterised; it does not remove it.

## 2. Definitions

- **Dynamical core.** The solver for the resolved, adiabatic, large-scale flow
  (momentum, mass, thermodynamic energy). It carries state variables such as
  wind, temperature, pressure and moisture on the grid.
- **Physics package.** The set of parameterisations that supply the
  non-resolved sources and sinks to the dynamical core.
- **Grid spacing $\Delta x$.** The distance between adjacent state points.
- **Effective resolution.** The smallest feature a model represents
  acceptably. A common rule of thumb is four to seven grid spacings, because
  a feature must span several cells for the advection operator to move it at
  approximately the right speed.
- **Closure.** A formula expressing an unresolved flux in terms of resolved
  variables, plus the coefficients that formula needs.
- **Numerical diffusion.** The artificial smoothing produced by discretising
  advection. It is a truncation error, and (Section 3) it is predictable.

## 3. Derivation: discretising advection creates a diffusion

### 3.1 The modified equation

Take the linear advection equation with constant speed $u>0$,

$$\frac{\partial c}{\partial t} + u\frac{\partial c}{\partial x} = 0,$$

and discretise it with the first-order **upwind** scheme, which takes the
spatial derivative from the upwind side:

$$c_i^{n+1} = c_i^{n} - C\left(c_i^{n} - c_{i-1}^{n}\right),
\qquad C \equiv \frac{u\,\Delta t}{\Delta x}.$$

Expand each term about $(x_i,t_n)$ in a Taylor series. Writing $c$ for
$c(x_i,t_n)$, $\partial_x$ for the spatial derivative at the point and so on,

$$c_i^{n+1} = c + \Delta t\,c_t + \tfrac12\Delta t^{2}c_{tt} + \dots,$$

$$c_{i-1}^{n} = c - \Delta x\,c_x + \tfrac12\Delta x^{2}c_{xx} - \dots$$

Substituting and using $c_t = -u c_x$ (from the differential equation) to
eliminate the leading time derivatives from the truncation error gives the
**modified equation**:

$$\frac{\partial c}{\partial t} + u\frac{\partial c}{\partial x}
= \frac{u\,\Delta x}{2}(1-C)\,\frac{\partial^{2}c}{\partial x^{2}}
+ \mathcal{O}(\Delta x^{2}).$$

The right-hand side is a diffusion term:

$$\boxed{\;K_{\text{num}} = \tfrac{1}{2}\,u\,\Delta x\,(1-C)\;}$$

with the units of a diffusivity, $\mathrm{m^{2}\,s^{-1}}$. The scheme is said to
be *first-order accurate* because the leading error is $\mathcal{O}(\Delta x)$.

### 3.2 What this says

Three consequences follow immediately, and none of them is a defect of the code:

- **Halving the grid spacing halves the numerical diffusion.** Refining the grid
  is the only way to reduce it, and the reduction is linear, not quadratic,
  for a first-order scheme.
- **The Courant number matters.** At $C = 1$ the error vanishes; at the usual
  $C = 0.5$ the coefficient is $0.25\,u\,\Delta x$.
- **A first-order scheme damps extrema.** That damping is the diffusion above.
  Second-order schemes reduce it but introduce dispersion instead.

## 4. Measurement: the numerical diffusivity

The demonstration advects a Gaussian tracer of width $\sigma_{0} = 80\
\mathrm{km}$ around a $1000\ \mathrm{km}$ periodic channel with $u = 10\
\mathrm{m\,s^{-1}}$ and $C = 0.5$, for 24 hours, at four resolutions. It
measures the growth of the tracer variance and converts it into a diffusivity
through $\mathrm{Var}(t) = \mathrm{Var}(0) + 2Kt$:

| $N$ | $\Delta x$ (km) | $K_{\text{analytic}}$ (m²/s) | $K_{\text{measured}}$ (m²/s) | ratio |
|---|---|---|---|---|
| 64 | 15.625 | 39 062.5 | 39 059.6 | 1.000 |
| 128 | 7.812 | 19 531.2 | 19 531.2 | 1.000 |
| 256 | 3.906 | 9 765.6 | 9 765.6 | 1.000 |
| 512 | 1.953 | 4 882.8 | 4 882.8 | 1.000 |

The measured ratio $K(128)/K(512)$ is exactly $4.00$, as the formula predicts.
Agreement at the 0.1% level is the reward for measuring a truncation error
instead of assuming it.

Two details make the measurement honest. The tracer crosses the periodic
boundary during the run, so the mean and variance are computed with a periodic
estimator (the phase of the first Fourier coefficient and the shortest
distance). A naive first moment would split the blob between $x=0$ and $x=L$
and report a variance several times too large. The demonstration code does this
correctly; making the mistake first is instructive.

## 5. A sub-grid process and two closures for it

### 5.1 The problem

Consider a single column, $5\ \mathrm{km}$ deep, with 21 levels
($\Delta z = 250\ \mathrm{m}$), initialised with a surface temperature of
$300\ \mathrm{K}$ and a lapse rate of $10.50\ \mathrm{K\,km^{-1}}$. The dry
adiabatic lapse rate is a standard constant,

$$\Gamma_{d} = \frac{g}{c_p} = \frac{9.81\ \mathrm{m\,s^{-2}}}{1004\
\mathrm{J\,kg^{-1}\,K^{-1}}} = 9.77\times10^{-3}\ \mathrm{K\,m^{-1}}
= 9.77\ \mathrm{K\,km^{-1}},$$

so the column is **superadiabatic** and statically unstable. A real atmosphere
removes the instability by convection within minutes. A model column with no
convective parameterisation has no mechanism to remove it at all: the profile
simply remains unphysical.

### 5.2 An energy-conserving adjustment

Convection is approximately a mixing process that conserves dry static energy
$s = c_pT + gz$. The **convective adjustment** algorithm is:

1. compute $s$ on all levels;
2. wherever $s_{i} > s_{i+1}$ (unstable), replace the pair with an average;
3. repeat until no unstable pair remains.

Averaging conserves the total $\sum_{i}s_{i}$, so the final profile has the
same column energy as the initial one, and the lapse rate becomes $\Gamma_{d}$ —
neutral. The demonstration verifies energy conservation to a relative
$2.96\times10^{-16}$, which is double-precision round-off.

### 5.3 Two closures, two climates

The adjustment rule is a choice. Relaxing fully to neutral and relaxing only
half-way are both energy-conserving closures, and they disagree:

| scheme | surface $T$ (K) | top $T$ (K) | lapse rate (K/km) |
|---|---|---|---|
| unadjusted (no closure) | 300.00 | 247.50 | 10.50 |
| full adjustment | 298.20 | 249.31 | 9.78 |
| half adjustment | 298.54 | 248.99 | 9.91 |

The difference in surface temperature is $0.34\ \mathrm{K}$ — from a closure
choice alone, on a single column, with both closures conserving energy exactly.
That is the structural uncertainty parameterisation introduces. It is not a
rounding error, and it does not average away with more grid points.

## 6. Resolution versus process scale

| grid spacing | features larger than about $4\Delta x$ |
|---|---|
| 100 km | 400 km |
| 25 km | 100 km |
| 10 km | 40 km |
| 1 km | 4 km |

Convective plumes (order 1 km), boundary-layer turbulence (well under 1 km),
clouds (0.1–10 km) and gravity waves (under 10 km) are smaller than the
effective resolution of every climate model in routine use, so all of them are
parameterised. A 1 km grid resolves 4 km features: it begins to represent the
largest convective systems explicitly, but individual plumes, turbulence and
microphysics remain sub-grid. Refining the grid shrinks the parameterised part;
it never eliminates it.

## 7. Worked example: how much diffusion does one gauge read?

*Problem.* A regional model uses a first-order upwind scheme with
$u = 10\ \mathrm{m\,s^{-1}}$, $\Delta x = 25\ \mathrm{km}$ and
$\Delta t = 600\ \mathrm{s}$. Compare its numerical diffusion with the molecular
diffusivity of air, $2\times10^{-5}\ \mathrm{m^{2}\,s^{-1}}$.

*Solution.*

1. $C = u\Delta t/\Delta x = (10)(600)/(2.5\times10^{4}) = 0.24$.
2. $K_{\text{num}} = \tfrac12u\Delta x(1-C)
   = 0.5\times10\times2.5\times10^{4}\times0.76
   = 9.5\times10^{4}\ \mathrm{m^{2}\,s^{-1}}$.
3. Ratio to molecular: $9.5\times10^{4}/2\times10^{-5} \approx 4.8\times10^{9}$.

*Interpretation.* The numerical diffusion is ten orders of magnitude larger than
molecular diffusion — the scheme's smoothing, not the fluid's, is what damps the
tracer. Compare with the demonstration's measured value at
$\Delta x = 15.625\ \mathrm{km}$ and $C = 0.5$: $K = 3.91\times10^{4}\
\mathrm{m^{2}\,s^{-1}}$. Reducing $\Delta x$ to 1 km at $C = 0.5$ would give
$2.5\times10^{3}\ \mathrm{m^{2}\,s^{-1}}$, still eight orders of magnitude above
molecular. Resolution buys accuracy in the numerical sense long before it
reaches the physical dissipation scale; that is why sub-grid dissipation in
climate models is a parameterisation and not a resolved process.

## 8. Assumptions and regime of validity

1. **The modified-equation result assumes constant $u$ and small $\Delta x$.**
   With variable velocity, on a sphere and near strong gradients the leading
   error still scales as $\Delta x$ but its coefficient varies in space.
2. **The convective adjustment assumes dry neutrality and instantaneous
   mixing.** Real convection is moist, entraining, and finite in duration; the
   moist adiabatic lapse rate is smaller than $\Gamma_{d}$, so the adjustment
   here is a dry idealisation.
3. **One column is not a climate.** The demonstration isolates convection; it
   says nothing about how the closure interacts with radiation, a large-scale
   circulation or the surface.
4. **$K_{\text{num}}$ is a truncation error, not a physical loss.** It is
   predictable and diagnosable, which is why it is worth measuring; but the
   modelled tracer is damped more than the real one.
5. **Energy conservation does not imply correctness.** Both adjustment schemes
   conserve energy exactly and give different answers. Conservation constrains
   the closure; it does not determine it.

## 9. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| grid spacing | $\Delta x$ | m | |
| Courant number | $C$ | 1 | $u\Delta t/\Delta x$ |
| numerical diffusivity | $K_{\text{num}}$ | $\mathrm{m^{2}\,s^{-1}}$ | $(u\Delta x)$ has $\mathrm{m^{2}\,s^{-1}}$ |
| dry static energy | $s$ | $\mathrm{J\,kg^{-1}}$ | $c_pT$ and $gz$ have the same unit |
| lapse rate | $\Gamma$ | $\mathrm{K\,km^{-1}}$ | $g/c_p$ |

The last two rows are the useful checks in the convective calculation: adding
$c_pT$ and $gz$ is only meaningful because both are energies per unit mass, and
$g/c_p$ has units
$(\mathrm{m\,s^{-2}})/(\mathrm{J\,kg^{-1}\,K^{-1}}) = \mathrm{K\,m^{-1}}$.

## 10. Python demonstration

[`code/gcms_and_parameterisation_demo.py`](code/gcms_and_parameterisation_demo.py):

1. advects a Gaussian tracer at four resolutions, measures $K_{\text{num}}$ from
   the variance growth and compares it with $\tfrac12u\Delta x(1-C)$;
2. shows that $K_{\text{num}}\propto\Delta x$ by reporting the four-to-one ratio
   between the two finest resolutions;
3. builds a superadiabatic column, applies two energy-conserving convective
   adjustments and reports the temperature profiles and the disagreement;
4. verifies conservation of dry static energy to round-off;
5. tabulates effective resolution against process scale.

It is print-only, seeded with `np.random.default_rng(20261014)`, and exits 0.

## 11. Exercises

See [`exercises/02-gcms-and-parameterisation-exercises.md`](exercises/02-gcms-and-parameterisation-exercises.md)
and [`exercises/02-gcms-and-parameterisation-solutions.md`](exercises/02-gcms-and-parameterisation-solutions.md).

## Mastery checkpoint

> **(a)** Derive the boxed expression for $K_{\text{num}}$ from the modified
> equation, showing where the $\tfrac12$ and the $(1-C)$ come from.
> **(b)** A model with $\Delta x = 100\ \mathrm{km}$ and $C = 0.3$ has
> $u = 15\ \mathrm{m\,s^{-1}}$. Compute $K_{\text{num}}$ in
> $\mathrm{m^{2}\,s^{-1}}$ and state the effective resolution on the usual
> four-spacing rule.
> **(c)** The same model is refined to $\Delta x = 25\ \mathrm{km}$ with the same
> $C$. State the new $K_{\text{num}}$ and explain why the improvement is only
> linear.
> **(d)** Two convective closures both conserve dry static energy to round-off
> and differ by $0.34\ \mathrm{K}$ at the surface. State what extra evidence
> would let you choose between them, and why the choice cannot be made from the
> energy budget alone.

## Common pitfalls

1. **Calling numerical diffusion a bug.** It is a predictable truncation error;
   reduce it by refining $\Delta x$, not by adjusting the output.
2. **Assuming higher order removes the problem.** Second-order schemes lose the
   leading diffusion but gain dispersion, which appears as oscillations near
   sharp gradients.
3. **Thinking a finer grid means a parameterisation-free model.** Every finer
   grid has a new sub-grid scale and new closures.
4. **Treating a parameterisation as physics.** It is a closure with coefficients;
   report which one and with what values.
5. **Believing energy conservation settles the closure.** It constrains the
   column but does not select the mixing rule.

## Related modules

- [16-05 Climate Models](README.md) — the rest of this module.
- [16-05-06 Emulators and Surrogate Models](06-emulation-and-surrogates.md) —
  the cheap-model end of the same trade-off.
- [19-02 Finite-Difference Methods](../../19-numerical-modeling-hpc/02-finite-difference-methods/README.md) —
  schemes, stencils and stability in full.
- [19-01-03 Consistency, Stability and Convergence](../../19-numerical-modeling-hpc/01-numerical-foundations/03-consistency-stability.md) —
  the Lax-equivalence framework behind Section 3.
- [03-12 Building Numerical Simulation Code in Python](../../03-scientific-computing/12-numerical-simulation-python/02-stability-and-cfl.md) —
  the CFL condition in practice.
