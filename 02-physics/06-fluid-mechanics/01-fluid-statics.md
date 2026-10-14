---
id: 02-06-01
title: "Fluid Statics, Pressure and Buoyancy"
level: intermediate
prereqs: ["02-02-02", "02-02-03", "02-01-01"]
estimated_minutes: 90
tags: [fluid-statics, pressure, buoyancy, isostasy]
---

# Fluid Statics, Pressure and Buoyancy

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** pressure as an isotropic surface traction and derive the
   hydrostatic relation $\nabla p = \rho\mathbf{g}$ from the balance of forces on
   a fluid parcel.
2. **Integrate** the hydrostatic relation through a layered medium and state
   precisely what the single-density approximation assumes and what it costs.
3. **Derive** Archimedes' principle from the pressure field, rather than
   asserting it, and use the equivalent statement that the net force on a
   submerged body per unit volume is $(\rho_{\text{host}}-\rho_{\text{body}})
   \mathbf{g}$.
4. **Compute** the buoyancy pressure available to drive magma ascent and state
   which other forces (viscous resistance, tensile strength of the host rock)
   must be overcome for the magma to reach the surface.
5. **Formulate** isostasy as a hydrostatic balance at depth, solve the Airy and
   Pratt models, and explain why surface gravity alone does not determine the
   compensating mass.
6. **Check** every one of these numerically, including a finite-difference test
   of $\partial p/\partial z = \rho g$.

## Prerequisites

- [02-02-02 Newton's Laws of Motion](../02-classical-mechanics/02-newtons-laws.md)
  — force balances, which is all that fluid statics is.
- [02-02-03 Work, Energy and Conservation Laws](../02-classical-mechanics/03-work-energy.md)
  — the potential-energy reading of buoyancy and floating.
- [02-01-01 Physical Quantities, Units and Dimensions](../01-measurement-and-physical-reasoning/01-physical-quantities.md)
  — units and prefixes, used throughout the units section.

## 1. Why start with the fluid at rest

Almost every quantity in fluid geophysics — the pressure at the base of an
aquifer, the overburden on a fault, the driving force of a volcano, the support
of a mountain range — is a *static* balance. The reason is not that the fluids
are motionless. It is that over the timescales on which the questions are posed,
the acceleration term is negligible compared with the pressure and gravity terms.

A mantle plume rises for tens of millions of years at centimetres per year; the
pressure work it does in one year is enormous compared with the change in its
kinetic energy in that year. A water table adjusts to recharge over days to
decades while the pressure field around it is essentially in hydrostatic balance
from second to second. Fluid statics is therefore not a special case that we
leave behind: it is the leading-order description of most of the Earth, and the
dynamical corrections in later lessons are corrections *to it*.

Two consequences follow, and they organise this lesson:

- **Pressure is what keeps a fluid from collapsing into a surface.** In a static
  fluid the pressure gradient balances gravity exactly. Remove that balance and
  the fluid moves — that is the subject of lesson 02.
- **Pressure depends on depth, not on shape.** A consequence of the balance is
  that the pressure at a given depth in a connected static fluid is the same
  whatever the geometry above it. Pascal's paradox, the hydrostatic balance of a
  mountain root, and the behaviour of connected aquifers all follow from this.

## 2. Precise definitions

**Pressure.** In a fluid at rest, the traction on any plane is normal to it and
independent of its orientation; the magnitude per unit area is the pressure $p$.
Equivalently, the stress tensor is $\sigma_{ij} = -p\delta_{ij}$ (with the
solid-mechanics tension-positive convention). Units: pascal, 1 Pa = 1 N m⁻².

**Hydrostatic equilibrium.** The state in which every fluid element has zero
acceleration, so the pressure gradient exactly balances the body force:

$$\nabla p = \rho\mathbf{g}. \tag{1}$$

**Absolute and gauge pressure.** Absolute pressure is measured from vacuum; gauge
pressure is measured from local atmospheric pressure. Borehole and aquifer
practices usually quote gauge pressure or head; state which.

**Pressure head.** For a fluid of density $\rho$, the height of a column that
produces a pressure $p$ is $h = p/(\rho g)$. Head is pressure expressed as a
length and is the natural variable in hydrogeology (lesson 05).

**Buoyancy force.** The net pressure force on the surface of a submerged body.
By equation (1), for a uniform host density it equals the weight of the
displaced fluid, directed upwards (Archimedes' principle).

**Isostasy.** The statement that below some depth (the *compensation depth*) the
pressure is laterally uniform, so that lateral variations in the mass above are
balanced by lateral variations in the density or thickness below. It is a
hydrostatic balance condition, not a separate law of physics.

## 3. Derivations

### 3.1 Pressure is isotropic in a static fluid

Take a small wedge of fluid at rest. There is no shear traction, because a fluid
at rest cannot support shear, and no acceleration. Balancing forces on the two
inclined faces and taking the size to zero shows that the normal traction per
unit area is the same on every face. That common value is $p$, and the stress
tensor reduces to $-p\delta_{ij}$. This is a *definition* of a fluid at rest, and
it is the reason a pressure gauge reads the same whatever its orientation — a
fact we use without thinking every time we read a tire pressure.

### 3.2 The hydrostatic equation

Consider a small rectangular parcel with cross-section $A$ and vertical extent
$\delta z$. The pressure force on its underside is $p(z)A$ upwards; on its top,
$p(z+\delta z)A$ downwards; its weight is $\rho g A\,\delta z$ downwards. Zero
net force gives

$$p(z) - p(z+\delta z) - \rho g\,\delta z = 0
\;\Longrightarrow\; \frac{dp}{dz} = -\rho g , \tag{2}$$

with $z$ measured upwards. In the geophysical convention with depth $d$
measured downwards, the same statement is

$$\frac{dp}{dd} = +\rho g . \tag{3}$$

Integrating from the surface:

$$p(d) = p_0 + g\int_0^{d}\rho(d')\,dd' . \tag{4}$$

Two features of equation (4) deserve emphasis. First, the term $p_0$ is the
surface pressure — about 101 325 Pa (the standard atmosphere, exact by
definition in the handbook's classification). Second, and more important, the
*only* quantity needed is the density profile. Pressure does not care about the
shape of the container, the path taken by the fluid, or the horizontal extent of
the layer. This is the geometric content of Pascal's principle.

### 3.3 Buoyancy from the pressure field

The net pressure force on a closed surface $S$ enclosing a volume $V$ is

$$\mathbf{F} = -\oint_S p\,\mathbf{n}\,dS = -\int_V \nabla p\,dV
= -\int_V \rho_{\text{host}}\mathbf{g}\,dV , \tag{5}$$

using the divergence theorem and equation (1). For a body of volume $V$ and mass
$m_{\text{body}}$, the net force is

$$\mathbf{F}_{\text{net}} = -\int_V \rho_{\text{host}}\mathbf{g}\,dV
+ m_{\text{body}}\mathbf{g} , \tag{6}$$

which for uniform densities becomes the familiar

$$F_{\text{net}} = (\rho_{\text{host}} - \rho_{\text{body}})\,gV . \tag{7}$$

Equation (7) is the form to remember: **the buoyancy force per unit volume is
$(\rho_{\text{host}}-\rho_{\text{body}})g$**, and it is the *contrast* in density,
not the density itself, that does the work. A floating body displaces its own
mass, so its submerged fraction is exactly $\rho_{\text{body}}/\rho_{\text{host}}$.

### 3.4 Isostasy as a buoyancy balance

Consider a crustal column of density $\rho_c$ standing a height $h$ above the
reference level, supported by a root of thickness $r$ extending into mantle of
density $\rho_m$. Requiring that the pressure at the compensation depth be the
same under the mountain as under the reference column gives the Airy balance

$$\rho_c h = (\rho_m - \rho_c)\,r
\qquad\Longrightarrow\qquad
r = \frac{\rho_c}{\rho_m-\rho_c}\,h . \tag{8}$$

The Pratt alternative keeps the base of the crust flat and reduces the column
density instead: $\rho(D+h) = \rho_0 D$ at compensation depth $D$. The two
models impose the same physics — hydrostatic pressure equal at depth — and differ
only in where they put the compensation. Equation (8) shows the amplification
factor $\rho_c/(\rho_m-\rho_c)$: for $\rho_c = 2700$ and $\rho_m = 3300\
\mathrm{kg\,m^{-3}}$ it is $4.5$, so a 1 km mountain needs a 4.5 km root.

## 4. Physical interpretation

**Magma ascent.** Basaltic magma is less dense than the crust it intrudes. With
the nominal densities $\rho_{\text{magma}} = 2500$ and $\rho_{\text{crust}} =
2700\ \mathrm{kg\,m^{-3}}$, the driving pressure per metre of column is
$(\rho_c-\rho_m)g \approx 1962$ Pa m⁻¹, so a 1 km column of magma supplies about
2 MPa of buoyancy pressure at its base. Whether the magma reaches the surface is
a competition between this and the viscous resistance of the conduit and the
tensile strength of the host rock, which is of order megapascals to tens of
megapascals. Buoyancy alone is *necessary and not sufficient*: it explains why
melt rises at all, not why any particular eruption occurs.

**Isostasy.** The 4.5 amplification factor of equation (8) is why mountain roots
are deep: the Alps and Tibet are supported by roots tens of kilometres thick,
and the compensation is why the free-air gravity anomaly over a large mountain
range is nearly zero. The same physics explains post-glacial rebound, where
removing an ice load unloads the crust and it rises — a slow buoyancy response
whose timescale is set by mantle viscosity (lesson 06).

**Ocean and crustal pressure.** In the ocean the pressure gradient is
$\rho_w g \approx 10.1\ \mathrm{kPa\,m^{-1}}$, so the rule of thumb "about 1 MPa
per 100 m" overestimates by about 1 per cent for seawater and by about 2 per cent
for fresh water. In the continental crust, $\rho_c g \approx 26.5\
\mathrm{MPa\,km^{-1}}$; that number, the *lithostatic gradient*, is the starting
point of every in-situ stress and borehole-stability calculation.

## 5. Assumptions and regime of validity

Every result above rests on assumptions. Each is stated here with its regime and
with the observation that would falsify it.

| Assumption | Valid when | Fails when | What breaks |
|---|---|---|---|
| The fluid is at rest | Accelerations are negligible over the timescale of interest | Rapid flows, seismic shaking, tides in a narrow channel | Pressure is no longer determined by depth alone; the momentum equation is needed |
| No shear stress | Always, for a fluid at rest | Any motion | Stress tensor acquires off-diagonal parts |
| $g$ is constant | Over the height of the problem, to the accuracy quoted | Heights of hundreds of kilometres | $g$ falls with radius; integrate properly |
| The density profile is known | It is measured or modelled | Undersaturated or overpressured pore fluids in the crust | The pressure gradient in the pores need not be $\rho_w g$ |
| Isostatic equilibrium holds | Loads older than the relaxation time, typically $10^4$–$10^5$ yr | Young loads, active tectonics, mantle of low viscosity | Pressure is not yet laterally uniform at depth; there is a dynamic support term |
| Airy/Pratt compensation | Loads are broad compared with the elastic thickness | Narrow loads | The lithosphere flexes and supports part of the load elastically |

The most consequential of these for geophysics is the last one. Isostasy is a
*limit* of an elastic plate on a fluid foundation. Narrow loads — a seamount
rather than a mountain belt — are supported by flexure, and the observed gravity
anomaly records the flexural rigidity, which is the subject of
[02-04 Elasticity](../04-elasticity-and-continuum-mechanics/README.md) and
[07-gravity-geodesy](../../07-gravity-geodesy/README.md).

## 6. Units and dimensional analysis

Pressure has dimensions of force per area:

$$[p] = \mathrm{M\,L^{-1}T^{-2}} = \mathrm{kg\,m^{-1}\,s^{-2}} =
\mathrm{Pa}. \tag{9}$$

Check equation (3): $[\rho g] = \mathrm{kg\,m^{-3}}\cdot\mathrm{m\,s^{-2}} =
\mathrm{kg\,m^{-2}s^{-2}} = \mathrm{Pa\,m^{-1}}$. Dimensionally consistent.

Useful conversions, all exact arithmetic from the definitions:

| Quantity | Value | Note |
|---|---|---|
| 1 bar | $10^5$ Pa | Not SI; still common in geophysics |
| 1 atm (standard) | 101 325 Pa | Exact by definition (handbook, Sec. 1) |
| 1 kbar | $10^8$ Pa = 100 MPa | Convenient for mantle pressures |
| 1 MPa | 10 bar | The natural unit for rock mechanics |
| 1 head metre of water | 9.81 kPa × (ρ/1000) | From $p = \rho g h$ |

Two dimensionless groups do the work in this lesson:

- **The density contrast ratio** $(\rho_{\text{host}}-\rho_{\text{body}})/
  \rho_{\text{host}}$, which sets how strongly buoyancy acts. It is 0.074 for
  basalt magma in crust and 0.11 for an iceberg in seawater.
- **The compensated-load ratio** $r/h = \rho_c/(\rho_m-\rho_c)$ from equation
  (8), a pure number that depends only on the densities.

Dimensional analysis warns us about one common error: do not mix gauge and
absolute pressure. Adding $p_0$ to a head calculation changes nothing in a
buoyancy problem (it cancels in the pressure difference), but it changes
everything if the quantity is a boiling point or a gas solubility.

## 7. Python demonstration

The demo [`code/fluid_statics_demo.py`](./code/fluid_statics_demo.py) builds a
layered hydrostatic profile, checks the gradient numerically, and works through
buoyancy and isostasy. Run it with `python3 fluid_statics_demo.py`. Its actual
output includes:

```text
 z (km)    p (MPa)   dp/dz (MPa/km)   rho*g (MPa/km)
    1.0     26.487        26.487000        26.487000
   30.0    794.610        26.487000        26.487000
  the two columns agree by construction: dp/dz = rho g = 26.487000 MPa/km
```

```text
       layer  top (km)  base (km)     rho  p_top (MPa)  p_base (MPa)
    sediment       0.0        2.0    2200        0.000        43.164
 upper crust       2.0       15.0    2650       43.164       381.118
 lower crust      15.0       35.0    2900      381.118       950.098

finite-difference check of dp/dz (h = 0.05 km), samples well inside a layer:
  max |finite-difference - rho*g| over 695 interior samples = 2.183e-08 Pa/m

  layered p(35 km)              =   950.098 MPa
  single-density 2700 estimate  =   927.045 MPa
  relative difference           = +2.49 %
```

```text
                  body  rho_body  rho_host  d(rho*g) (Pa/m)  over 5 km (MPa)
basaltic magma in crust      2500      2700          1962.00            9.810
granitic melt in crust      2400      2700          2943.00           14.715
mantle plume vs mantle      3250      3300           490.50            2.453
   iceberg in seawater       917      1030          1108.53            5.543
  dense block in crust      3000      2700         -2943.00          -14.715
```

```text
Airy balance: rho_c * h = (rho_m - rho_c) * r
  h (km)   root r (km)      r/h   topo load (MPa)   root buoy. (MPa)   residual
     1.0          4.50     4.50            26.487             26.487  +0.00e+00
     5.0         22.50     4.50           132.435            132.435  +0.00e+00

Pratt model at compensation depth D = 30 km: rho * (D + h) = rho_0 * D
  h =  2.0 km  ->  required density  2531.2 kg/m^3  (deficit 168.8)
```

### What to observe

| Observation | Consequence |
|---|---|
| The finite-difference gradient matches $\rho g$ to $2\times10^{-8}$ Pa m⁻¹ over 695 interior samples | The discrete differentiation is correct; a large residual would indicate an indexing or step-size error |
| The three-layer pressure at 35 km, 950 MPa, exceeds the single-density estimate by 2.5 per cent | Density structure matters: a constant-density model is a choice, not a law. The layered result requires no new physics |
| Every density-contrast row scales linearly with the density difference, and the dense block is negative | Buoyancy responds to the *contrast*; a body denser than its host sinks with the same coefficient |
| The Airy residual is exactly zero in the table | Equation (8) is an identity once the balance is imposed; the residual tests the arithmetic, not the physics |
| The iceberg's submerged fraction is 0.890 | For $917$ and $1030\ \mathrm{kg\,m^{-3}}$ the familiar "nine-tenths below water" is confirmed to a per cent |
| The Pratt model needs a density deficit of 169 kg m⁻³ for a 2 km plateau at 30 km compensation | Compensation by density rather than by root thickness requires a large anomaly; both models fit the same gravity data, which is why gravity alone is non-unique |

> **Breaking exercise.** Halve the density of the sediment layer and predict,
> before running, the change in $p(35\ \mathrm{km})$; then change the surface
> pressure $p_0$ and predict the change in the *buoyancy* answers of section 2.
> The second prediction should be "none".

## 8. Common mistakes

1. **Using the total pressure where a pressure difference is needed.** Buoyancy
   and isostasy involve differences; the atmospheric term cancels.
2. **Assuming a single density.** The lithostatic gradient $26.5\
   \mathrm{MPa\,km^{-1}}$ assumes $2700\ \mathrm{kg\,m^{-3}}$ everywhere. Real
   crust is layered, and the error at 35 km reached 2.5 per cent in the demo.
3. **Confusing pressure with force.** Pressure acts on a surface; a force needs
   the area. "The pressure on the fault" is a traction.
4. **Treating isostasy as a law.** It is a limit of hydrostatic equilibrium at
   depth, valid for broad loads and old enough to have relaxed.
5. **Forgetting that the buoyancy of a sinking body is upward.** The sign of
   $(\rho_{\text{host}}-\rho_{\text{body}})$ handles it; do not add a minus sign
   from intuition.
6. **Quoting a magma density as a fact.** The density of a specific magma
   depends on composition, temperature, pressure and volatile content; it is a
   measured quantity with a range of several hundred kg m⁻³. The values here are
   nominal.
7. **Assuming pore pressure is hydrostatic.** Overpressure and underpressure are
   common, and the effective stress (lesson 04 of the mechanics module) is what
   matters for failure.
8. **Ignoring that $g$ varies.** Over 30 km, $g$ changes by about 1 per cent; over
   the whole mantle it changes by 10 per cent or more.

## 9. Real-world applications

- **Aquifer pressure and well design.** The hydrostatic gradient $\rho_w g$ sets
  the pressure at the base of a borehole and therefore the mud weight needed to
  keep it stable. See [14-hydrology-hydrogeophysics](../../14-hydrology-hydrogeophysics/README.md).
- **Volcanic hazard.** The buoyancy pressure of a magma column, minus the
  viscous and elastic resistance, is the first term in any ascent model; it is
  why dense magmas stall and why volatile exsolution can trigger an eruption.
- **Isostasy and geoid.** The Airy and Pratt models are the reference against
  which gravity and geoid anomalies are interpreted; the residuals are the
  signal. See [07-gravity-geodesy](../../07-gravity-geodesy/README.md).
- **Post-glacial rebound.** The relaxation of the crust to the removal of ice is
  a buoyancy problem whose timescale measures mantle viscosity. See
  [13-geodynamics-tectonics](../../13-geodynamics-tectonics/README.md).
- **Reservoir pressure depletion.** Compaction and subsidence follow from the
  change in effective stress as pore pressure falls.
- **Ocean pressure and sea-level height.** Satellite altimetry measures sea
  surface height to centimetres; converting that to a geostrophic current is
  lesson 07 of this module.

## 10. Further reading

- **Batchelor, G. K. *An Introduction to Fluid Dynamics* (Cambridge University
  Press).** The classic derivation of hydrostatic equilibrium and buoyancy, with
  careful attention to the assumptions. Level: advanced.
- **Turcotte, D. L., & Schubert, G. *Geodynamics* (Cambridge University Press).**
  Isostasy, flexure and mantle convection in one consistent treatment; the
  standard reference for the material of this module. Level: advanced.
- **Watts, A. B. *Isostasy and Flexure of the Lithosphere* (Cambridge University
  Press).** Everything about compensation, including why Airy and Pratt are
  limits and how flexure replaces them. Level: graduate.
- **Jaeger, J. C., Cook, N. G. W., & Zimmerman, R. W. *Fundamentals of Rock
  Mechanics* (Blackwell).** Lithostatic and pore pressure, effective stress, and
  the measurement of in-situ stress. Level: advanced.
- **Sleep, N. H., & Fujita, K. *Principles of Geophysics* (Blackwell).**
  Buoyancy, isostasy and the thermal state of the Earth in a single volume.
  Level: intermediate.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 11. Related lessons

- [02 Continuity and Momentum Equations; Navier–Stokes](./02-conservation-fluid.md)
  — what happens when the static balance is broken.
- [05 Flow in Porous Media: Darcy's Law and Permeability](./05-porous-media-flow.md)
  — hydrostatic head as the driving variable of groundwater flow.
- [06 Mantle Convection and Rayleigh–Bénard Instability](./06-mantle-convection.md)
  — buoyancy as the engine of convection.
- [07 Rotating Fluids, Coriolis Effect and Geostrophic Balance](./07-geophysical-fluids.md)
  — the pressure field when rotation joins the balance.
- [02-04-01 Stress](../04-elasticity-and-continuum-mechanics/01-stress.md) — the
  continuum form of the same pressure field, and effective stress.
- [26-reference-library constants handbook](../../26-reference-library/02-symbols-and-units/03-constant-handbook.md)
  — the classification of exact, measured and nominal values used here.

Exercises:
[`exercises/01-fluid-statics-exercises.md`](./exercises/01-fluid-statics-exercises.md)
and [`exercises/01-fluid-statics-solutions.md`](./exercises/01-fluid-statics-solutions.md).

## Self-assessment checklist

- [ ] I can derive $\nabla p = \rho\mathbf{g}$ from a force balance on a parcel.
      (Section 3.2)
- [ ] I can integrate it through a layered density profile and say what the
      constant-density approximation costs. (Sections 3.2, 7)
- [ ] I can derive Archimedes' principle from the pressure field rather than
      quoting it. (Section 3.3)
- [ ] I can compute the buoyancy pressure available to a magma column and say
      why it is not sufficient for ascent. (Section 4)
- [ ] I can solve the Airy and Pratt isostasy problems and explain the
      amplification factor. (Section 3.4)
- [ ] I can state the regime of validity of isostasy and name the observation
      that falsifies it for narrow loads. (Section 5)
- [ ] I can convert between Pa, bar, atm and head, and check a hydrostatic
      gradient dimensionally. (Section 6)
- [ ] I can state which numbers in this lesson are nominal rather than measured.
      (Sections 4, 8)
