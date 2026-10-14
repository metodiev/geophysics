---
id: 02-06-05
title: "Flow in Porous Media: Darcy's Law and Permeability"
level: advanced
prereqs: ["02-06-03", "02-06-01"]
estimated_minutes: 90
tags: [darcy-law, permeability, porous-media, pore-pressure]
---

# Flow in Porous Media: Darcy's Law and Permeability

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** specific discharge, porosity, permeability and hydraulic
   conductivity precisely, and convert between the hydraulic and intrinsic
   descriptions without ambiguity.
2. **Derive** Darcy's law from the Stokes limit of the Navier–Stokes equation,
   by averaging over a representative elementary volume, and show where the
   permeability comes from in a bundle-of-tubes and in a fracture.
3. **State** the range of validity of Darcy's law in terms of a pore-scale
   Reynolds number, and compute the discharge at which it fails for a given
   grain size.
4. **Solve** one-dimensional and radial steady-flow problems, including the
   Thiem solution for a pumped well, and verify the solution numerically.
5. **Derive** the pore-pressure diffusion equation, compute the hydraulic
   diffusivity, and estimate the distance a pressure disturbance travels in a
   given time.
6. **Explain** why permeability is a measured, not a calculated, property of a
   rock, and why the Kozeny–Carman relation is empirical.
7. **Connect** the mathematics to hydrogeology and to reservoir-induced
   seismicity, and state which quantities in each application are measured.

## Prerequisites

- [02-06-03 Viscous Flow, Reynolds Number and Boundary Layers](./03-viscous-flow.md)
  — Poiseuille flow and the cubic law, from which Darcy's law is derived here.
- [02-06-01 Fluid Statics, Pressure and Buoyancy](./01-fluid-statics.md) —
  hydrostatic pressure and head, the driving variable.

## 1. Why a separate law is needed

The Navier–Stokes equation is valid inside a pore, but it cannot be solved for
every pore of an aquifer, and it would be the wrong description anyway: what a
hydrogeologist needs is the discharge through a *volume* of rock, not the
velocity at a point inside a grain gap. So we average.

The result of that averaging is Darcy's law, and it has a peculiar status worth
stating at the outset. It is:

- **not a conservation law**, but an empirical constitutive relation — it was
  found experimentally by Darcy in 1856 and only later derived from
  Navier–Stokes;
- **valid only in a range**: it is the creeping-flow limit of a porous medium,
  and it fails at high discharge;
- **mesoscale**: it relates volume-averaged quantities over a representative
  elementary volume (REV) — a volume large compared with the pores and small
  compared with the formation;
- **the foundation of hydrogeology**, petroleum reservoir engineering, soil
  physics, geothermal reservoir modelling and poroelasticity.

Everything that follows is an elaboration of those four points.

## 2. Precise definitions

**Porosity $\phi$.** The fraction of the bulk volume occupied by connected pore
space that can transmit fluid (the *effective* porosity). Distinguish it from
total porosity, which includes isolated pores.

**Specific discharge (Darcy velocity) $\mathbf{q}$.** The volume flow rate per
unit *bulk* area, with units m s⁻¹. It is not the speed of the fluid: the **pore
velocity** is $\mathbf{v} = \mathbf{q}/\phi$, which is larger because the fluid
occupies only a fraction $\phi$ of the area.

**Intrinsic permeability $k$.** A property of the *medium* alone, with units m²
(equivalently, the darcy, $1\ \mathrm{darcy} = 0.9869\times10^{-12}\ \mathrm{m^2}$).
It does not depend on the fluid.

**Hydraulic conductivity $K$.** A property of the medium *and the fluid*:

$$K = \frac{k\rho g}{\mu}, \qquad [K] = \mathrm{m\,s^{-1}}. \tag{1}$$

The distinction matters: the same sandstone has $K$ differing by a factor of
about 50 between water and a light oil, because $\mu$ differs. Confusing $k$ with
$K$ is the most common error in the subject.

**Hydraulic head $h$.** $h = z + p/(\rho g)$ with $z$ measured upward. The head
is what drives flow; a fluid flows from high head to low head, not necessarily
from high pressure to low pressure. In a variable-density system the distinction
is essential and gets a separate treatment (variable-density flow).

**Representative elementary volume (REV).** The smallest volume over which an
average is stable to further doubling. Darcy's law is defined at scales larger
than the REV. There is no REV for a single fracture, which is why fracture flow
is treated with the cubic law of lesson 03 rather than with Darcy's law.

**Darcy's law.**

$$\mathbf{q} = -\frac{k}{\mu}\left(\nabla p - \rho\mathbf{g}\right) =
-K\nabla h . \tag{2}$$

Both forms are the same statement; the first is the one to use in a
variable-density problem, the second in constant-density hydrogeology.

## 3. Derivations

### 3.1 Darcy's law from Stokes flow

Start from the Stokes limit of the momentum equation — inertia dropped, valid
when the pore-scale Reynolds number is small:

$$0 = -\nabla p + \mu\nabla^2\mathbf{u} + \rho\mathbf{g}. \tag{3}$$

The equation is linear, so its solution in a fixed geometry is a linear map from
the driving force $(\nabla p - \rho\mathbf{g})$ to the velocity field, and hence
to the volume-averaged flux. Averaging over an REV,

$$\overline{\mathbf{u}} = \mathbf{q} = -\frac{1}{\mu}\mathbf{D}\left(\nabla p -
\rho\mathbf{g}\right), \tag{4}$$

where $\mathbf{D}$ is a tensor with units m² that depends only on the pore
geometry. For an isotropic medium, $\mathbf{D} = k\mathbf{I}$ and equation (4) is
Darcy's law. This derivation has a clean consequence: **Darcy's law inherits the
validity conditions of Stokes flow**, and its coefficient $k$ inherits the
geometry of the medium — which is why $k$ cannot be computed from a porosity
alone.

### 3.2 Permeability of a bundle of tubes and of a fracture

For a bundle of straight tubes of radius $r$, with $N$ tubes per unit area,

$$\mathbf{q} = N\frac{\pi r^4}{8\mu}\left(-\nabla p\right) =
\phi\frac{r^2}{8\mu}\left(-\nabla p\right)
\;\Longrightarrow\;
k = \frac{\phi r^2}{8}, \tag{5}$$

using $N = \phi/(\pi r^2)$. For a fracture of aperture $b$, lesson 03 gave

$$k = \frac{b^2}{12}. \tag{6}$$

Equations (5) and (6) are the two building blocks of every estimate of
permeability from geometry. Both are exact for their idealised geometry. Neither
applies to a real rock without a great deal of further argument, because a real
rock is not a bundle of tubes and a real fracture is not smooth.

### 3.3 Radial flow to a well: the Thiem solution

For steady, radial, confined flow to a well, Darcy's law in radial coordinates
gives $q_r = -K\,\mathrm{d}h/\mathrm{d}r$ and continuity requires the total
discharge $Q = 2\pi r D q_r$ to be the same at every radius. Hence

$$\frac{\mathrm{d}h}{\mathrm{d}r} = -\frac{Q}{2\pi T r}, \qquad T = KD, \tag{7}$$

where $T$ is the transmissivity (m² s⁻¹) and $D$ the aquifer thickness.
Integrating between two radii,

$$Q = \frac{2\pi T\,(h_2-h_1)}{\ln(r_2/r_1)}. \tag{8}$$

Two consequences are worth naming. First, the head profile is **logarithmic**, not
linear, because the area through which the flow passes grows with $r$. Second,
equation (8) is only valid with the well in a steady state. A real well takes
time to reach anything like it, and in a confined aquifer true steady state is
never reached — the drawdown continues to grow, slowly, forever. The Thiem
solution is therefore a *late-time approximation*, and its regime of validity is
explicitly stated rather than assumed.

### 3.4 Pore-pressure diffusion

Combine Darcy's law with conservation of mass and a constitutive relation for the
storage of the porous medium. For a slightly compressible fluid and a
compressible matrix, the linearised result is a diffusion equation for the
pressure (or head):

$$\frac{\partial p}{\partial t} = \kappa_h\nabla^2 p, \qquad
\kappa_h = \frac{k\rho g}{\mu S_s}, \tag{9}$$

with $S_s$ the specific storage (m⁻¹). The hydraulic diffusivity $\kappa_h$ has
units m² s⁻¹ and sets the length $L \sim \sqrt{\kappa_h t}$ over which a pressure
disturbance propagates in time $t$. This is the equation that connects
hydrogeology to induced seismicity: a pore-pressure change diffuses outwards from
an injection well (or from a reservoir) and changes the effective stress on
nearby faults, which is what triggers slip. The handbook quotes crustal hydraulic
diffusivity as $10^{-2}$ to $10^0\ \mathrm{m^2\,s^{-1}}$ for fractured rock
(nominal, Sec. 3.4); for intact rock the values are far lower, and the range is
the reason earthquake-triggering distances are hard to predict.

### 3.5 Validity: pore-scale Reynolds number

Define

$$Re_p = \frac{\rho\,q\,d}{\mu}, \tag{10}$$

with $d$ a characteristic pore or grain diameter and $q$ the specific discharge.
Some authors use the pore velocity $v = q/\phi$ instead, which makes $Re_p$
larger by $1/\phi$ (a factor of 3–5 for typical porosities); the definition in
use must always be stated. The convention in this module is equation (10).

Darcy's law is accepted while $Re_p \lesssim 1$–$10$; above that the inertia term
matters, the response becomes nonlinear, and the standard correction is the
Forchheimer term,

$$-\nabla p = \frac{\mu}{k}\mathbf{q} + \rho\frac{\beta}{k^{1/2}}|\mathbf{q}|
\mathbf{q}, \tag{11}$$

with $\beta$ a second, also empirical, coefficient. Note that $Re_p$ depends on
the *grain* scale; using a formation-scale length would give a Reynolds number
small by many orders of magnitude and would wrongly suggest that Darcy's law is
always safe.

## 4. Physical interpretation

**Permeability is a measured quantity.** Equations (5) and (6) show how it
*scales*, not what it *is*. Real rocks are consolidated, cemented, fractured and
anisotropic. The relation

$$k \approx \frac{d^2\phi^3}{180(1-\phi)^2} \quad\text{(Kozeny–Carman)} \tag{12}$$

is a widely used estimate, and it is empirical: the constant 180 is fitted, and
real rocks scatter around the prediction by an order of magnitude or more. It is
a starting guess. In practice permeability is measured by a flow test — a pumping
test in an aquifer, a core-flood in a laboratory, a well test in a reservoir.

**A single open fracture can dominate a rock mass.** $k = b^2/12$ gives
$84\,000$ darcy for a 1 mm aperture, against $10^{-3}$–$10^{-1}$ darcy for a
tight sandstone. That ratio of a million is why crystalline rock with open
fractures can be a viable aquifer, and why stress changes that close fractures
change the permeability drastically (lesson 03, ★★5).

**Why Darcy's law is so robust in hydrogeology.** The demo computes
$Re_p = 1$ at a specific discharge of $5\times10^{-3}$ m s⁻¹ for 0.2 mm sand,
i.e. about 432 m per day. Ordinary groundwater moves at 0.1–1 m per day, three
orders of magnitude below the limit. This is the numerical reason a linear law
suffices for most of hydrogeology — and why it fails near a gravel-packed well, in
a karst conduit or in a gravel aquifer, where both the grain scale and the
velocity jump up.

## 5. Assumptions and regime of validity

| Assumption | Valid when | Fails when | What breaks |
|---|---|---|---|
| Stokes limit inside the pores | $Re_p \lesssim 1$–$10$ | Gravel aquifers, karst, near-well flow | Forchheimer (quadratic) correction is needed |
| An REV exists | The medium is statistically homogeneous at a scale much larger than the pores | Single fractures, karst conduits, very heterogeneous media | Darcy's law is not defined; use cubic law or discrete-fracture models |
| $k$ is constant in time | The pore geometry does not change | Stress changes, dissolution, precipitation, fines migration, compaction | $k$ becomes a state variable; permeability evolution must be modelled |
| Isothermal, single-phase, Newtonian fluid | Ordinary groundwater | Geothermal systems, oil–water mixtures, non-Newtonian fluids | Additional physics required |
| Small pressure changes (linear storage) | $\Delta p \ll K_{\text{rock}}$ | Gas reservoirs, hydraulic fracturing | Nonlinear and two-phase flow |
| Homogeneous isotropy | Sandstones, unconsolidated sands | Shales, fractured rock, layered sequences | $k$ is a tensor; flow is not parallel to the driving gradient |

Two of these deserve emphasis for geophysics.

**Permeability is a state variable in coupled problems.** A pore-pressure change
alters the effective stress; the effective stress changes the aperture
distribution; the aperture distribution changes $k$. The coupling is
two-way, and it is the mechanism behind pressure-dependent aquifer response,
reservoir compaction, and the permeability enhancement or inhibition that makes
enhanced geothermal systems work. The coupling is the subject of poroelasticity
([02-04](../04-elasticity-and-continuum-mechanics/README.md) and
[14-hydrology-hydrogeophysics](../../14-hydrology-hydrogeophysics/README.md)).

**Where the REV does not exist, do not use Darcy.** In a granite with three open
fractures there is no representative elementary volume: the "permeability" of a
1 m³ sample and of a 1000 m³ block differ by orders of magnitude. The correct
treatment is a discrete fracture network, and the correct statement is that a
continuum permeability is a modelling choice with a scale attached.

## 6. Units and dimensional analysis

$$[k] = \mathrm{m^2}, \qquad [K] = \mathrm{m\,s^{-1}}, \qquad
[\kappa_h] = \mathrm{m^2\,s^{-1}}, \qquad
[\mathbf{q}] = \mathrm{m\,s^{-1}}. \tag{13}$$

Check equation (2): $[K\nabla h] = \mathrm{m\,s^{-1}}\times1 =
\mathrm{m\,s^{-1}} = [\mathbf{q}]$. Correct, and it is worth noticing that the
head is dimensionless in the sense that it is a length divided by a length.

Check equation (1): $[k\rho g/\mu] = \mathrm{m^2}\cdot\mathrm{kg\,m^{-3}}\cdot
\mathrm{m\,s^{-2}}/\mathrm{kg\,m^{-1}s^{-1}} = \mathrm{m\,s^{-1}}$. Correct.

Conversions worth memorising:

| Quantity | Relation | Typical values (nominal) |
|---|---|---|
| Specific discharge | $q = Q/A_{\text{bulk}}$ | $10^{-8}$–$10^{-5}$ m s⁻¹ in aquifers |
| Pore velocity | $v = q/\phi$ | 3–5× the specific discharge for $\phi = 0.2$–$0.3$ |
| Hydraulic conductivity $K$ | $k\rho g/\mu$ | $10^{-8}$ m s⁻¹ (silt) to $10^{-2}$ m s⁻¹ (gravel) |
| Transmissivity $T$ | $KD$ | $10^{-4}$ to $10^{-1}$ m² s⁻¹ |
| Storativity $S$ | $S_s D$ | $10^{-4}$–$10^{-2}$ (confined), 0.01–0.3 (unconfined) |

The storativity and specific storage entries are given as ranges because they are
measured, formation-specific quantities with the variability of natural
materials; they must not be quoted as single values.

## 7. Python demonstration

[`code/darcy_flow_demo.py`](./code/darcy_flow_demo.py) derives and verifies the
permeability of a tube bundle, converts permeability to conductivity, verifies
the Thiem solution, tests the Darcy validity range and solves the
pressure-diffusion equation. Its actual output includes:

```text
numerical check for r = 5.0 um, phi = 0.2, A = 1 m^2:
  number of tubes in the cross-section = 2546479089
  total flux  = 6.250000e-05 m^3/s
  k from total flux   = 6.250000e-13 m^2
  k from phi r^2 / 8  = 6.250000e-13 m^2   relative difference 1.85e-10
```

```text
     k (m^2)    k (darcy)         material (nominal)     K (m/s)   K (m/day)
   1.000e-09    1.013e+03               clean gravel   9.810e-03   8.476e+02
   1.000e-13    1.013e-01                 silty sand   9.810e-07   8.476e-02
   1.000e-17    1.013e-05     shale / intact granite   9.810e-11   8.476e-06
   8.300e-08    8.410e+04         1 mm open fracture   8.142e-01   7.035e+04
```

```text
  Thiem: |Q| = 2 pi T (h2 - h1)/ln(r2/r1) = 1.447379e-03 m^3/s = 125.05 m^3/day
  numerical |Q| from 2 pi r (-T dh/dr) over 200000 radial steps: max ||Q_num| - |Q|| = 7.351e-08 m^3/s
  relative difference = 5.08e-05
```

```text
                       setting     d (m)    q (m/s)    Re_pore      verdict
                  sand aquifer  2.00e-04   1.00e-05  2.000e-03     Darcy ok
            sand aquifer, fast  2.00e-04   1.00e-03  2.000e-01     Darcy ok
                gravel aquifer  1.00e-02   1.00e-02  1.000e+02 Darcy invalid
                 1 mm fracture  1.00e-03   1.00e-02  1.000e+01 Darcy invalid
               borehole-scale flow  1.00e-01   1.00e+00  1.000e+05 Darcy invalid

  critical specific discharge at Re_pore = 1 (q* = mu/(rho d)):
    d = 2.0e-04 m  ->  q* = 5.000e-03 m/s = 4.320e+02 m/day
```

```text
    k (m^2)   S_s (1/m)  kappa_h (m^2/s)   L in 1 day (m)   L in 1 yr (m)
  1.000e-15     1.0e-05       9.8100e-04             9.21           175.9

explicit finite-difference solution of the diffusion equation versus erfc:
  grid: N = 501, dx = 0.2000 m, dt = 8.0000e+00 s, t_end = 1.6001e+05 s
  max |numerical - erfc| at t_end = 2.595e-03 (peak value is 0.5)
```

### What to observe

| Observation | Consequence |
|---|---|
| The tube-bundle permeability from a summed Poiseuille flux matches $\phi r^2/8$ to $1.9\times10^{-10}$ | The derivation is exact for the idealised geometry; the idealisation is what is being tested, not the algebra |
| A 1 mm open fracture has $K = 0.814$ m s⁻¹, roughly $10^{7}$ times intact granite | One fracture dominates a rock mass; this is why crystalline aquifers exist and why they are so heterogeneous |
| The numerical radial flux matches the Thiem result to $5\times10^{-5}$ relative | The logarithmic profile is correct; the residual is the finite-difference truncation at the first radial interval |
| $Re_p = 0.002$ for an ordinary sand aquifer but $100$ for a gravel aquifer at the same order of specific discharge | Darcy validity is a property of the *grain scale*: coarser material fails sooner |
| $q^\ast = 5\times10^{-3}$ m s⁻¹ $= 432$ m per day for 0.2 mm sand | Ordinary groundwater ($0.1$–$1$ m per day) is two to three orders below the limit: this is why Darcy's law is robust |
| The finite-difference and error-function solutions differ by at most $2.6\times10^{-3}$ against a peak of 0.5, i.e. 0.5 per cent | The diffusion equation and its analytic solution are consistent; the difference is the scheme's truncation error |
| $\kappa_h = 9.8\times10^{-4}$ m² s⁻¹ gives a diffusion length of 9.2 m in one day and 176 m in one year | A pressure disturbance travels metres per day in this rock: months to years to reach a fault hundreds of metres away, which is the timescale that matters for reservoir triggering |

> **Breaking exercise.** Using $\kappa_h = 9.8\times10^{-4}\ \mathrm{m^2\,s^{-1}}$,
> estimate how long a pressure front takes to reach 1 km, and then repeat with
> the largest handbook value, $10^0\ \mathrm{m^2\,s^{-1}}$ for fractured rock.
> Predict the ratio of the two times before computing. It should be 1000, and it
> is the width of the range in which a triggering distance must be stated as a
> range rather than as a number.

## 8. Common mistakes

1. **Confusing permeability with hydraulic conductivity.** $k$ is a property of
   the medium (m²); $K$ includes the fluid (m s⁻¹). They differ by $\rho g/\mu$,
   a factor of about $10^{7}$ for water in SI units.
2. **Using Darcy's law for a single open fracture or a karst conduit.** Those are
   conduits with no REV; use the cubic law or a proper conduit description.
3. **Reporting a formation-scale Reynolds number.** $Re_p$ uses the grain scale.
   A formation-scale $Re$ is always tiny and proves nothing.
4. **Treating the Kozeny–Carman constant as universal.** The 180 is fitted;
   real rocks scatter by an order of magnitude or more.
5. **Forgetting that $q$ is not the fluid velocity.** The pore velocity is
   $q/\phi$, three to five times larger for a typical porosity.
6. **Applying the Thiem solution as though it were exact at early time.** It is a
   steady-state result; the drawdown of a real well grows slowly forever, so the
   "steady" value is a late-time approximation.
7. **Using a constant $\kappa_h$ over a range of stress.** Permeability depends
   on effective stress and can change by orders of magnitude as pressure changes.
8. **Confusing pressure-driven and head-driven flow in a variable-density
   system.** A dense brine at low pressure can flow down a head gradient; the
   $\rho\mathbf{g}$ term in (2) is not optional.
9. **Quoting a permeability without saying how it was measured and at what
   scale.** A core permeability and a well-test permeability are not the same
   quantity.

## 9. Real-world applications

- **Aquifer characterisation and well design.** Transmissivity, storativity and
  the Thiem/drawdown relations are the working tools of hydrogeology; the
  quantities are measured by pumping tests and interpreted with equation (8) and
  its transient counterparts. See
  [14-hydrology-hydrogeophysics](../../14-hydrology-hydrogeophysics/README.md).
- **Induced and triggered seismicity.** Pore-pressure diffusion, equation (9),
  changes the effective normal stress on a fault and can trigger slip at
  distances that grow as $\sqrt{\kappa_h t}$. This is the physical basis of
  reservoir-triggered and injection-induced earthquakes; the key seismological
  questions are the fault's stress state and the orientation of its slip
  tendency relative to the regional stress. See
  [06-seismology/12 Induced and Triggered Seismicity](../../06-seismology/12-induced-and-triggered-seismicity/README.md).
- **Geothermal reservoirs.** Flow through a fracture network, with
  pressure-dependent permeability and coupled heat transport, is the core
  modelling problem of enhanced geothermal systems.
- **Petroleum reservoir engineering.** Darcy's law in its multi-phase form, with
  relative permeability functions that are again measured, underpins production
  forecasting.
- **Groundwater contamination and remediation.** The pore velocity $q/\phi$, not
  the specific discharge, is the advective transport speed; the difference
  between them determines when a contaminant arrives.
- **Poroelastic coupling.** Subsidence from fluid withdrawal and the stress
  changes from injection are two-way coupled problems whose fluid side is
  equation (2) and whose solid side is elasticity.
- **Soil and vadose-zone physics.** Unsaturated flow generalises $K$ to a
  function of water content, $K(\theta)$, which is another measured relation.

## 10. Further reading

- **Bear, J. *Dynamics of Fluids in Porous Media* (Dover).** The standard
  reference: the volume-averaging derivation, Darcy's law's validity and the
  Forchheimer correction. Level: graduate.
- **Freeze, R. A., & Cherry, J. A. *Groundwater* (Prentice-Hall).** The
  hydrogeological companion, with the field methods that measure the parameters.
  Level: intermediate.
- **de Marsily, G. *Quantitative Hydrogeology* (Academic Press).** Rigorous and
  well organised, strong on the averaging and on heterogeneity. Level: graduate.
- **Wang, H. F. *Theory of Linear Poroelasticity* (Princeton University Press).**
  Connects Darcy's law to the elasticity of the matrix, which is the physics of
  both subsidence and triggered seismicity. Level: graduate.
- **Dullien, F. A. L. *Porous Media: Fluid Transport and Pore Structure*
  (Academic Press).** How pore geometry controls permeability, and why the
  geometry-based estimates are idealisations. Level: graduate.
- **Ingebritsen, S. E., Sanford, W. E., & Neuzil, C. E. *Groundwater in Geologic
  Processes* (Cambridge University Press).** Applies Darcy's law to crustal
  processes, with field-scale values. Level: graduate.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 11. Related lessons

- [03 Viscous Flow, Reynolds Number and Boundary Layers](./03-viscous-flow.md) —
  Poiseuille flow, the cubic law and the source of $k = b^2/12$.
- [01 Fluid Statics, Pressure and Buoyancy](./01-fluid-statics.md) — head and
  hydrostatic pressure, the driving variable of equation (2).
- [04 Turbulence, Mixing and Eddy Diffusivity](./04-turbulence.md) — the other
  great volume-averaged closure, with the same requirement of honesty about the
  parameterisation.
- [06 Mantle Convection and Rayleigh–Bénard Instability](./06-mantle-convection.md)
  — the same physics at the scale of the whole mantle, where none of Darcy's
  assumptions hold.
- [14-hydrology-hydrogeophysics](../../14-hydrology-hydrogeophysics/README.md) —
  the discipline built on this law.
- [06-seismology/12 Induced and Triggered Seismicity](../../06-seismology/12-induced-and-triggered-seismicity/README.md)
  — where pore-pressure diffusion meets fault mechanics.
- [02-05-06 Geotherms, Heat Flow and the Earth's Thermal Budget](../05-thermodynamics/06-geotherms.md)
  — heat transport through the same pore space, and why the crust is not in
  thermal equilibrium.

Exercises:
[`exercises/05-porous-media-flow-exercises.md`](./exercises/05-porous-media-flow-exercises.md)
and
[`exercises/05-porous-media-flow-solutions.md`](./exercises/05-porous-media-flow-solutions.md).

## Self-assessment checklist

- [ ] I can define $q$, $\phi$, $k$, $K$, $T$ and $S$ without ambiguity and
      convert between the hydraulic and intrinsic descriptions. (Sections 2, 6)
- [ ] I can derive Darcy's law from Stokes flow by volume averaging. (Section 3.1)
- [ ] I can derive $k = \phi r^2/8$ and $k = b^2/12$ and say why neither is a
      property of a real rock. (Section 3.2)
- [ ] I can state the validity range in terms of $Re_p$ and compute the discharge
      at which it fails. (Sections 3.5, 7)
- [ ] I can solve the Thiem problem and state its regime of validity.
      (Section 3.3)
- [ ] I can derive the pressure-diffusion equation and estimate a diffusion
      length. (Section 3.4)
- [ ] I can explain why permeability is measured, and give the measurement that
      each application uses. (Sections 4, 9)
- [ ] I can explain how pore-pressure diffusion couples to fault slip and what
      controls the triggering distance. (Sections 3.4, 9)
