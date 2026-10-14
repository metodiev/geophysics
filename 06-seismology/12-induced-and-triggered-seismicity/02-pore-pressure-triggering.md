---
id: 06-12-02
title: "Pore-Pressure Diffusion and Triggering Mechanisms"
level: doctoral
prereqs: ["06-12-01", "02-06-01"]
tags: [pore-pressure-diffusion, triggering-front, diffusivity, poroelasticity, migration]
---

# Pore-Pressure Diffusion and Triggering Mechanisms

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the pore-pressure diffusion equation from mass conservation,
   Darcy's law and linearised fluid and pore compressibility, and identify the
   hydraulic diffusivity $D$ with its units.
2. **Derive** the exponential-integral Green's function for a constant-rate line
   source, and from it the **triggering front** $r_c(t) = \sqrt{4Dtx_c}$.
3. **Derive** the naive form $r \propto \sqrt{Dt}$ and state precisely which
   quantity a front position does and does not constrain.
4. **Measure** the migration exponent from a simulation and quote the observed
   accuracy of that measurement.
5. **Quantify** the degeneracy between the inferred diffusivity and the assumed
   triggering threshold, and between the inferred diffusivity and the hypocentral
   location error.
6. **State** at least two alternative migration laws that can fit the same short
   observational record, and say what extra data would discriminate them.

## Prerequisites

- [06-12-01 Causes of Induced Seismicity](./01-induced-seismicity-causes.md)
  — the Coulomb failure function and the role of $\Delta p$ in it.
- [02-06-01 Fluid Statics, Pressure and Buoyancy](../../02-physics/06-fluid-mechanics/01-fluid-statics.md)
  — pressure, gradients and the continuum description of a fluid.
- [01-08-01 First-Order Ordinary Differential Equations](../../01-mathematics/08-ordinary-differential-equations/01-first-order-odes.md)
  — the technique used for the Green's function.

## 1. Intuition: why a front, and why it is not a diffusivity measurement

Inject fluid at a point and the pressure disturbance spreads outwards. Seismic
events are triggered where and when the disturbance arrives. So the migrating
outer edge of an induced sequence — its "front" — looks like a direct
measurement of how fast pressure moves, and therefore of the hydraulic
diffusivity.

That inference is real but much weaker than it looks, for two reasons that this
lesson makes quantitative.

The first is that **the front is a contour, not a particle**. A contour is
defined by a threshold, and the threshold is a modelling choice. Move the
threshold and the contour moves; the *shape* of the migration does not change,
but the number you read off from it does.

The second is that **$r \propto \sqrt{Dt}$ means the diffusivity goes as $r^2$**.
Errors in the radius are doubled in $D$, and an error of two in $D$ is nothing
next to the three or four orders of magnitude spanned by rock permeability.

The result, measured below, is a clean separation: the **migration exponent** is
a robust measurement (0.499902 against an exact 0.5 in the demonstration), while
the **absolute diffusivity** recovered from the same front spans a factor of 267
across defensible threshold assumptions.

## 2. Precise definitions

### 2.1 Hydraulic diffusivity

For a fluid of dynamic viscosity $\eta$ (Pa·s) in a porous medium of intrinsic
permeability $k$ (m²) and porosity $\phi$ (dimensionless), the **hydraulic
diffusivity** is

$$D = \frac{k}{\eta\,S},
\qquad S = \phi\left(c_f + c_p\right)\ \ \text{[Pa}^{-1}\text{]},$$

where $S$ is the storage coefficient (dimension 1/Pa), $c_f$ the fluid
compressibility and $c_p$ the pore compressibility.

$$[D] = \frac{\mathrm{m^2}}{\mathrm{Pa\,s}\times\mathrm{Pa}^{-1}}
= \frac{\mathrm{m^2}}{\mathrm{s}}\ \ \checkmark$$

### 2.2 The pressure change field

$\Delta p(\mathbf{x},t)$ is the change from the pre-operational value. Because
the equation is linear, superposition applies: many wells give the sum of many
$\Delta p$ fields.

### 2.3 The triggering front

Given a threshold $\Delta p_c$ above which the Coulomb function is taken to be
changed enough to matter, the **triggering front** is

$$r_c(t) = \max\{r : \Delta p(r,t) \ge \Delta p_c\}.$$

In a real catalogue the events are discrete, so "the front" is usually taken to
be the largest epicentral distance among events in a time bin, or a fitted
percentile of that distance. **These two definitions give different numbers from
the same catalogue**, and which one is used must be stated.

### 2.4 What is *not* being assumed

Diffusion of pore pressure is not the only mechanism that can produce a migrating
front of seismicity. Aseismic slip can propagate along a fault and trigger events
as it goes, and a poroelastic strain front can propagate faster than the pressure
front. Each of these has a different $r(t)$. This lesson derives the diffusive
one and says what the alternatives look like; it does not claim that diffusion is
what any particular sequence is doing.

## 3. Derivations

### 3.1 From mass conservation to the diffusion equation

**Step 1 — mass conservation.** For a fluid of density $\rho$ and Darcy
velocity $\mathbf{q}$ (volume flux per unit area, m/s),

$$\frac{\partial(\phi\rho)}{\partial t} + \nabla\cdot(\rho\mathbf{q}) = Q,$$

with $Q$ a source term (kg m⁻³ s⁻¹).

**Step 2 — Darcy's law.**
$$\mathbf{q} = -\frac{k}{\eta}\left(\nabla p - \rho g\hat z\right).$$

**Step 3 — assume small perturbations** about a static state, so that $\rho$,
$\phi$, $k$ and $\eta$ are constant to first order and the gravity term is
absorbed into the static field. Then linearising the left-hand side,

$$\rho\left(\phi c_f + c_p\right)\frac{\partial p}{\partial t}
= \rho\frac{k}{\eta}\nabla^2 p + Q,$$

**Step 4 — divide by $\rho S$** with $S = \phi c_f + c_p$:

$$\boxed{\ \frac{\partial p}{\partial t} = D\nabla^2 p + \frac{Q}{\rho S}\ },
\qquad D = \frac{k}{\eta S}.$$

This is the same parabolic equation as heat conduction, with one difference worth
naming: heat diffuses through the *solid*, whereas pressure diffuses through the
*connected pore network*. Thermal diffusivity of rock is roughly
$10^{-6}\ \mathrm{m^2/s}$ and varies little; hydraulic diffusivity spans many
orders of magnitude because permeability does. Quoting a "typical" hydraulic
diffusivity without saying what the permeability range is would be exactly the
error this curriculum forbids.

**Step 5 — what sets the scale.** For a disturbance that has spread to radius
$r$ in time $t$, dimensional analysis of (Step 4) gives

$$r^2 \sim D t \qquad\Longrightarrow\qquad r \sim \sqrt{Dt}.$$

The rest of this lesson is about the constants hidden in "$\sim$".

### 3.2 The Green's function for a constant-rate line source

Take a 2-D problem (a long horizontal well or a line of wells, so that $p$ depends
only on the radial distance $r$ in the horizontal plane) with a source of strength
$Q$ switched on at $t = 0$ and held constant. Then

$$\frac{\partial p}{\partial t}
= D\left(\frac{\partial^2 p}{\partial r^2} + \frac{1}{r}\frac{\partial p}{\partial r}\right),
\qquad p(r,0)=0 .$$

**Step 1 — look for a similarity solution in $u = r^2/(4Dt)$** (a standard change
of variable for this equation, chosen so that the diffusion operator becomes an
ordinary differential equation). Substituting gives

$$u\frac{\mathrm{d}^2 f}{\mathrm{d}u^2} + (1+u)\frac{\mathrm{d}f}{\mathrm{d}u} = 0
\qquad\text{with } p = f(u).$$

**Step 2 — solve.** Let $g = \mathrm{d}f/\mathrm{d}u$; then
$\mathrm{d}g/g = -(1+u)/u\,\mathrm{d}u = -(1/u + 1)\mathrm{d}u$, so

$$g = \frac{C_1 e^{-u}}{u}.$$

**Step 3 — integrate once more.** $\int_u^\infty e^{-s}/s\,\mathrm{d}s = E_1(u)$,
the exponential integral. Requiring $p \to 0$ as $u \to \infty$:

$$p(r,t) = C\,E_1\!\left(\frac{r^2}{4Dt}\right).$$

**Step 4 — fix the constant from the source strength.** The total injected
"pressure-volume" rate per unit length is $Q$; integrating the flux through a
circle of radius $r$ as $r \to 0$ gives $C = Q/(4\pi D)$. Hence

$$\boxed{\ p(r,t) = \frac{Q}{4\pi D}\,E_1\!\left(\frac{r^2}{4Dt}\right)\ }$$

with $E_1(x) = \int_x^\infty e^{-s}s^{-1}\mathrm{d}s$. In three dimensions the
corresponding result is $\mathrm{erfc}(r/\sqrt{4Dt})/r$, and for an instantaneous
pulse in 2-D it is the Gaussian $(A/4\pi Dt)\exp(-r^2/4Dt)$. All three have the
same self-similar argument $r^2/(4Dt)$, which is the origin of the
$\sqrt{Dt}$ scaling.

### 3.3 The front, exactly

Set $p(r_c,t) = \Delta p_c$ in the boxed result:

$$\frac{Q}{4\pi D}E_1\!\left(\frac{r_c^2}{4Dt}\right) = \Delta p_c
\ \Longrightarrow\
\frac{r_c^2}{4Dt} = x_c,
\qquad E_1(x_c) = \frac{4\pi D\,\Delta p_c}{Q}.$$

So

$$\boxed{\ r_c(t) = \sqrt{4D\,x_c\,t}\ }$$

and the migration exponent is **exactly $1/2$**, for every $D$, $Q$ and
$\Delta p_c$. The constant $x_c$ absorbs everything else.

This is the cleanest possible statement of the situation: the *exponent* is a
property of the mechanism, while the *prefactor* is a property of the mechanism
and of every assumption made about the source and the threshold.

### 3.4 Why $D$ is not recoverable from a front alone

Define the measured migration rate $a = r_c^2/t$, which is what a catalogue
gives you. Then

$$D_{\text{inferred}} = \frac{a}{4x_c},
\qquad\text{and}\qquad
x_c = x_c\!\left(\frac{\Delta p_c}{\Delta p_{\text{ref}}};\,t\right),$$

because the reference overpressure at a monitoring radius
$\Delta p_{\text{ref}}(t) = \dfrac{Q}{4\pi D}E_1\!\left(\dfrac{r_{\text{ref}}^2}{4Dt}\right)$
eliminates $Q$ and $D$ from the ratio. The measured $a$ fixes the *product*
$a = 4Dx_c$. Nothing in the seismicity fixes $x_c$ separately.

Quantitatively: $\Delta p_c/\Delta p_{\text{ref}}$ is the ratio of the
triggering threshold to the overpressure actually applied, and it is unknown to
within at least an order of magnitude. The demonstration below shows what that
does to $D_{\text{inferred}}$.

### 3.5 Alternative migration laws

| Migrating process | Expected $r(t)$ | Signature |
|---|---|---|
| Pressure diffusion | $\sqrt{4Dx_ct}$ | exponent 0.5, decelerating |
| Aseismic slip front | $v\,t$ | exponent 1, constant speed |
| Poroelastic strain relaxation | faster than pressure, $\propto\sqrt{D_u t}$ with $D_u > D$ | exponent 0.5, larger prefactor |
| Fluid-filled fracture propagation | $\propto t^{2/3}$ or $t^{1/2}$ depending on regime | exponent between 0.5 and 0.7 |

On a record spanning less than a decade in time, a factor-of-two difference in
exponent is hard to detect: the demonstration's own measurement of an exponent of
exactly 0.5 returns 0.4999, but that is with 150 perfect hypocentres in a
noise-free simulation. Real catalogues give exponents that scatter by $\pm 0.1$,
which spans all four models in the table.

## 4. Physical interpretation

The most useful way to read the derivation is as an *identification* statement:

- A migration with $r \propto \sqrt{t}$ **identifies the mechanism class as
  diffusive**. That is real information.
- The prefactor identifies $D x_c$, not $D$.
- Therefore an "observed diffusivity" quoted as a single number is a statement
  about $D$ *and* about the analyst's assumed threshold, mixed inseparably.

There is a second, subtler point. A front defined by the *outermost* triggered
event is a single extreme value of a noisy field, so it is the noisiest possible
estimator. A front defined by a fitted percentile of event distances is far
better behaved — but it is no longer the physical front, and it inherits the
event-count statistics. The measurement below quantifies both.

## 5. Assumptions and their consequences

| Assumption | Consequence if violated |
|---|---|
| Single-phase, constant-viscosity fluid | Two-phase flow changes $S$ and the front speed by a factor depending on saturation |
| Homogeneous, isotropic permeability | Layering and faults channel flow; a front can be strongly non-circular |
| Constant $\phi$, $c_f$, $c_p$ | Real storage varies with effective stress, so $D$ changes as $p$ changes |
| Darcy flow | Near a wellbore, or in a fracture, flow is not Darcian and the near-field is wrong |
| Constant injection rate and no leak-off | Precludes finite-volume injection; the pulse case has a different prefactor |
| Threshold $\Delta p_c$ constant in space | Real fault populations have variable strength, so triggering is a stochastic threshold |
| Point/line source | Violated near the injection interval, which is where the largest $\Delta p$ is |
| Negligible stress coupling | In a real reservoir, pressure and stress change together; §3.5's alternatives apply |

## 6. Units and dimensional analysis

| Quantity | Symbol | SI unit |
|---|---|---|
| Permeability | $k$ | m² |
| Dynamic viscosity | $\eta$ | Pa·s |
| Storage coefficient | $S$ | Pa⁻¹ |
| Diffusivity | $D$ | m²/s |
| Pressure change | $\Delta p$ | Pa |
| Migration rate $r^2/t$ | $a$ | m²/s |
| Source strength (per unit length) | $Q$ | Pa·m²/s |
| Exponential integral argument | $x$ | dimensionless |

Two checks:

- $[k/(\eta S)] = \mathrm{m^2}/(\mathrm{Pa\,s}\times\mathrm{Pa^{-1}}) =
  \mathrm{m^2\,s^{-1}}$ ✓.
- $E_1$ takes a dimensionless argument, so $r^2/(4Dt)$ must be dimensionless:
  $\mathrm{m^2}/(\mathrm{m^2\,s^{-1}}\times\mathrm{s})$ ✓. A common error is to
  write $E_1(r^2/Dt)$ with $t$ in days, which is dimensionally fine but
  numerically wrong by $\sqrt{86400}$.

**Numerical anchor for scale conversion.** $D = 0.1\ \mathrm{m^2/s}$ gives
$\sqrt{4Dt} = 3.55$ km at $t = 1$ year ($3.156\times10^7$ s). Because the front
goes as $\sqrt{D}$, changing $D$ by a factor of 100 changes the front by a factor
of 10.

## 7. Worked examples

### 7.1 The front at one year, by hand

**Problem.** $D = 0.1\ \mathrm{m^2/s}$, $x_c = 1.2$, $t = 1$ yr. Find $r_c$.

**Step 1 — convert the time.** $t = 365.25 \times 86400 = 3.1558\times10^7$ s.

**Step 2 — assemble.** $r_c = \sqrt{4 \times 0.1 \times 3.1558\times10^7 \times 1.2}
= \sqrt{1.5148\times10^7} = 3892\ \mathrm{m} \approx 3.9$ km.

The demonstration computes 3888.2 m for the same inputs (it uses
$x_c = 1.1977$), which is a 0.1 % difference traceable to the third decimal of
$x_c$. Agreement of this kind is the point of doing the arithmetic by hand.

### 7.2 What a factor-of-two radius error does to $D$

**Problem.** A catalogue's front is measured at 3 km, then re-measured with a
better velocity model at 4 km, at the same time. What happens to $D$?

**Step 1 — the scaling.** $D \propto r^2$, so
$$\frac{D_2}{D_1} = \left(\frac{4}{3}\right)^2 = 1.778.$$

**Step 2 — interpretation.** A 33 % radius change moves the inferred diffusivity
by 78 %. Since the radius is the quantity with the largest systematic uncertainty
(velocity model, station geometry, magnitude-of-completeness), this is the
dominant term in the error budget — larger than the location-error term, because
a velocity-model error is *systematic* and scales every event's distance the same
way.

### 7.3 The demonstration's measured numbers

Run

```text
<repo>/.venv/bin/python code/diffusion_front_demo.py
```

Model inputs (all labelled MODEL in the script): $D = 0.10\ \mathrm{m^2/s}$,
reference overpressure 5.0 MPa at $r_{\text{ref}} = 50$ m after one year,
threshold $\Delta p_c = 0.10$ MPa, a $30\ \mathrm{km}$ domain at
$\mathrm{d}r = 50$ m, and two years of injection.

**Solver verification.** The same finite-difference update is first applied to an
exactly solvable pulse problem. Measured: maximum relative error
$2.717\times10^{-3}$, and total mass conserved to $3.4\times10^{-13}$ per cent
over $5.05\times10^4$ steps. The residual error is set by the initial condition's
width (200 m, 4 cells), not by the scheme.

**Migration exponent.** Front radii measured at 30, 60, 120, 240, 365.25, 500 and
730.5 days give

$$\ln r = -0.3662 + 0.499902\,\ln t ,
\qquad r/\sqrt{t} = 0.6933\ \mathrm{m\,s^{-1/2}}\ \ \text{to}\ \pm0.0004 .$$

The measured exponent is **0.499902** against an exact 0.5, and the numerical
front position matches the exponential-integral solution to 0.0 % at the printed
precision. So the exponent is measurable to about 0.02 % **in a noise-free
simulation**; the observational scatter in real catalogues is far larger.

**The threshold degeneracy.** Holding the measured $a = 0.4792\ \mathrm{m^2/s}$
fixed and varying the assumed threshold ratio $\Delta p_c/\Delta
p_{\text{ref}}$:

| Assumed $\Delta p_c/\Delta p_{\text{ref}}$ | $x_c$ | $D_{\text{inferred}}$ (m²/s) | ratio to true $D$ |
|---|---|---|---|
| 0.5 | 0.0107 | 11.2411 | 112.4 |
| 0.2 | 0.1298 | 0.9226 | 9.23 |
| 0.1 | 0.3496 | 0.3426 | 3.43 |
| 0.05 | 0.6679 | 0.1794 | 1.79 |
| **0.02 (true)** | **1.1977** | **0.1000** | **1.00** |
| 0.01 | 1.6565 | 0.0723 | 0.72 |
| 0.005 | 2.1510 | 0.0557 | 0.56 |
| 0.002 | 2.8454 | 0.0421 | 0.42 |

Over the stated range the inferred diffusivity spans **0.0421 to 11.2411 m²/s —
a factor of 267 — while the migration exponent is 0.5 in every case.** This is
the single most important number in the lesson.

**Location error.** Adding Gaussian hypocentre errors to the 150-event synthetic
sequence and refitting $D$:

| Estimator | median $D$ (m²/s) | p10 | p90 | p90/p10 |
|---|---|---|---|---|
| all 150 events, $\sigma = 1$ km | 0.1049 | 0.0993 | 0.1108 | 1.12 |
| 5 outermost events, $\sigma = 1$ km | 0.1031 | 0.0831 | 0.1252 | 1.51 |
| outermost event only, $\sigma = 1$ km | 0.0990 | 0.0586 | 0.1492 | 2.55 |

Two conclusions, and the second contradicts a common assumption:

1. **Random location error averages out.** With 150 events the spread is
   only 12 %; the fit is dominated by the well-located outer events and the
   errors partly cancel. Discarding events, or using the outermost event alone,
   makes it much worse (spread 2.55).
2. **Systematic location error does not average out.** Multiplying every
   hypocentral distance by $(1+b)$ scales $D$ by $(1+b)^2$ exactly, for any
   number of events: measured $D/D_{\text{true}} = 1.103$, 1.210 and 1.440 for
   $b = 0.05$, 0.10 and 0.20. A velocity model that is 10 % wrong is a 21 %
   diffusivity error that no amount of extra events will reduce.

## 8. Python demonstration

`code/diffusion_front_demo.py`:

1. solves $\partial_tp = D(1/r)\partial_r(r\partial_rp)$ with a source term on a
   cell-centred radial grid, using an explicit scheme with diffusion number 0.025
   (stability limit 0.5);
2. **validates the operator** on an exactly solvable pulse problem, reporting the
   maximum relative error and the mass budget;
3. measures the front by linear interpolation of the threshold crossing, so the
   front is not quantised to the 50 m grid;
4. fits the migration exponent by least squares in log-log space;
5. sweeps the assumed threshold ratio to map the degeneracy;
6. refits $D$ under random and systematic location errors.

Exercises against the output: change `DR` to 100 m and check whether the exponent
degrades; change `P_C` to 0.3 MPa and predict the sign of the change in
$D_{\text{inferred}}$ before running.

## 9. Exercises

### ★ Foundational

**★1.** Compute $D$ for $k = 10^{-14}\ \mathrm{m^2}$, $\eta = 10^{-3}$ Pa·s and
$S = 10^{-10}\ \mathrm{Pa^{-1}}$. Then compute it for $k = 10^{-12}\ \mathrm{m^2}$
with the same $\eta$ and $S$, and state the ratio.

**★2.** Compute $r_c$ at $t = 1$ yr for $D = 0.5\ \mathrm{m^2/s}$ and
$x_c = 1.0$, and at $t = 4$ yr for the same parameters. Confirm that quadrupling
the time doubles the front.

**★3.** State the dimensions of $D$, $S$, $Q$ and $x_c$, and verify that
$Q/(4\pi D)$ in $p = (Q/4\pi D)E_1(r^2/4Dt)$ has pressure units.

### ★★ Applied

**★★4.** A catalogue gives a front at 2.5 km after 100 days and 4.0 km after
400 days. Compute $a = r^2/t$ for both and comment on whether the two are
consistent with a single $D x_c$.

**★★5.** On a $\log r$ against $\log t$ plot a sequence has slope 0.62. State
which models from the table in §3.5 remain viable, and what additional data would
discriminate them.

**★★6.** Using the demonstration's threshold table, state the threshold ratio at
which $D_{\text{inferred}}$ is within a factor of two of the true value, and
translate that into a statement about how well the injection overpressure must be
known.

**★★7.** A colleague reports $D = 0.4\ \mathrm{m^2/s}$ from a front migration and
notes the front was measured with a velocity model later revised by 8 %. Using
the systematic-bias result, give the revised $D$ and its uncertainty from that
single effect.

### ★★★ Research

**★★★8.** Derive the 3-D Green's function for a constant-rate point source,
$p = (Q/4\pi D r)\,\mathrm{erfc}(r/\sqrt{4Dt})$, and show that its large-$t$
limit is the steady-state solution. Then derive the front radius in that case and
compare its $t$-dependence with the 2-D result.

**★★★9.** Suppose the storage coefficient depends on effective stress as
$S = S_0\exp(-\beta\Delta\sigma')$. Show that the diffusion equation acquires a
nonlinear term, and estimate, for $\beta = 10^{-8}\ \mathrm{Pa^{-1}}$ and a 5 MPa
pressure change, the fractional change in $D$ between the near-well and far-field
regions. Does the front remain exactly $\sqrt{t}$?

**★★★10.** The demonstration finds that the front position is reproduced by the
exponential-integral solution to 0.0 %, yet a real catalogue never is. List, in
order of expected magnitude, the four physical effects that would break the
agreement, and design the observation that would distinguish the largest one.

## 10. Common mistakes

1. **Quoting a diffusivity from a front position without stating the threshold.**
   The measured span is a factor of 267.
2. **Reporting the exponent and the prefactor as if they had equal weight.** The
   exponent is robust; the prefactor is not.
3. **Using the outermost event as "the front".** Measured spread is 2.55 times
   worse than using all events.
4. **Assuming random location errors dominate.** They average out; a velocity
   model bias does not, and it enters as $(1+b)^2$.
5. **Forgetting the time unit inside $E_1$.** The argument is dimensionless.
6. **Treating a hydraulic diffusivity as a rock property.** It depends on the
   fluid's viscosity as well, so the same rock gives different $D$ for water and
   for brine or CO₂.
7. **Assuming the pressure front is the earthquake front.** The event front is
   set by a Coulomb threshold, which includes the stress term; the two differ.
8. **Ignoring aseismic slip.** A constant-speed $r \propto t$ front fits some
   sequences at least as well as $\sqrt{t}$.
9. **Extrapolating a front indefinitely.** $r = \sqrt{4Dx_ct}$ grows without
   bound, which is unphysical; finite injection volume and finite pressure
   ultimately bound it.
10. **Fitting a straight line to $\log r$ against $\log t$ over less than a
    decade.** The demonstration needs no noise at all to reach 0.02 % accuracy;
    real records are not that kind.

## 11. Real-world applications

- **Reservoir-scale monitoring.** Front migration is the standard first
  diagnostic of a triggered sequence, and the honest statement of it quotes the
  exponent and the threshold.
- **Hydraulic-fracturing diagnostics.** Microseismic clouds are used to infer
  stimulated volume; the same diffusion argument applies with the same caveats.
- **CO₂ storage.** Pressure monitoring in observation wells gives an independent
  constraint on $D$, which is exactly what the front cannot supply.
- **Groundwater hydrology.** Pumping tests measure $D$ directly, with a known
  forcing; the induced-seismicity problem is the inverse of this, with an unknown
  forcing.
- **Geothermal reservoirs.** Thermal and hydraulic fronts travel at different
  speeds, and the cooling front is what the thermoelastic mechanism follows.
- **Data sources.** Pressure histories from operators are the crucial independent
  measurement; seismic catalogues come from the
  [USGS FDSN event service](https://earthquake.usgs.gov/fdsnws/event/1/query),
  with service details at [fdsn.org](https://www.fdsn.org/webservices/) and the
  client documented at
  [ObsPy](https://docs.obspy.org/packages/autogen/obspy.clients.fdsn.client.Client.html).

## 12. Further reading

- **Carslaw, H. S., & Jaeger, J. C. *Conduction of Heat in Solids* (Oxford
  University Press).** The Green's functions and similarity solutions of §3.2,
  in a form that transfers directly; the mathematics is identical.
- **Wang, H. F. *Theory of Linear Poroelasticity* (Princeton University Press).**
  The constitutive framework behind $D$ and $S$, and the coupled stress and
  pressure fields that §3.5's alternatives come from.
- **Segall, P. *Earthquake and Volcano Deformation* (Princeton University
  Press).** Poroelastic sources and the seismicity response to them.
- **Jaeger, J. C., Cook, N. G. W., & Zimmerman, R. W. *Fundamentals of Rock
  Mechanics* (Blackwell).** Permeability, storage and the ranges these quantities
  actually occupy.
- **Shapiro, S. A. *Fluid-Induced Seismicity* (Cambridge University Press).** The
  migration-front argument in its original full form, including the
  three-dimensional and finite-volume cases.
- **USGS Earthquake Hazards Program at <https://earthquake.usgs.gov>.** Catalogues
  and magnitude conventions for the front measurements themselves.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 13. Related lessons

- [06-12-01 Causes of Induced Seismicity](./01-induced-seismicity-causes.md) —
  the Coulomb function whose $\Delta p$ term this lesson makes spatial.
- [06-12-03 Rate-and-State Friction and the Dieterich Seismicity Model](./03-rate-state-triggering.md)
  — the *time* domain counterpart: how a stress change becomes a rate change.
- [06-12-05 Documented Case Studies](./05-case-studies-induced.md) — where the
  front argument has been made, and how well it held up.
- [06-12-04 Traffic-Light Protocols, Monitoring and Mitigation](./04-monitoring-and-mitigation.md)
  — what an operator does with a front that is moving towards a fault.
- [02-06-02 Conservation Laws and the Navier–Stokes Equations](../../02-physics/06-fluid-mechanics/02-conservation-fluid.md)
  — the continuum framework behind Darcy's law.

Exercises:
[`exercises/02-pore-pressure-triggering-exercises.md`](./exercises/02-pore-pressure-triggering-exercises.md)
and
[`exercises/02-pore-pressure-triggering-solutions.md`](./exercises/02-pore-pressure-triggering-solutions.md).

## Self-assessment checklist

- [ ] I can derive $\partial_tp = D\nabla^2p$ from mass conservation and Darcy's
      law, and give the units of every symbol. (§3.1)
- [ ] I can derive $p = (Q/4\pi D)E_1(r^2/4Dt)$ by similarity. (§3.2)
- [ ] I can derive $r_c = \sqrt{4Dx_ct}$ and say which quantities $x_c$ absorbs.
      (§3.3)
- [ ] I can compute a front radius by hand and check it against the demo. (§7.1)
- [ ] I can state the measured migration exponent and its accuracy. (§7.3)
- [ ] I can quote the factor-of-267 degeneracy and explain its origin in one
      sentence. (§7.3, §3.4)
- [ ] I can say why random location error averages out and systematic error does
      not, with the measured numbers. (§7.3)
- [ ] I can name two alternative migration laws and what would discriminate
      them. (§3.5, §9 ★★5)
- [ ] I can list the assumptions of the diffusive front and a consequence of
      each. (§5)
