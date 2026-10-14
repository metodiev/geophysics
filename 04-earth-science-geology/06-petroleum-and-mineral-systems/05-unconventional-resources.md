---
id: 04-06-05
title: "Unconventional Resources: Shale, Tight Gas, Hydrates"
level: advanced
prereqs: ["04-06-01", "04-01-05", "04-05-04"]
estimated_minutes: 75
tags: [shale-gas, tight-gas, gas-hydrate, gassmann, fizz-gas, brittleness, klinkenberg, bsr]
---

# Unconventional Resources: Shale, Tight Gas, Hydrates

"Unconventional" is a statement about **permeability and about where the
hydrocarbon sits**, not about the hydrocarbon itself. A conventional play has a
source rock, a migration pathway and a permeable reservoir with a seal; an
unconventional play has the hydrocarbon still where it formed, in a rock whose
matrix permeability is so low that the fluid does not flow unless the rock is
fractured. Three families are usually distinguished: **shale** (the source is the
reservoir, and the hydrocarbon is adsorbed and in micropores), **tight gas** (a
low-permeability conventional-looking reservoir), and **gas hydrate** (a solid
clathrate whose stability is a phase-boundary problem rather than a trap
problem).

This lesson develops the rock physics that each family requires — fluid
substitution and the fizz-gas problem, brittleness and closure stress, the
Klinkenberg correction, and the hydrate stability field — and then draws a line
that the previous lessons have already drawn once: **the physics ends at the
permeability, the moduli and the stability field; recovery factors, estimated
ultimate recovery and reserves are engineering, economic and regulatory
quantities and are not derived here.**

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** what makes a resource unconventional, in terms of permeability and
   of the relationship between source, reservoir and seal.
2. **Apply** Gassmann's equation to compute saturated bulk moduli, P- and S-wave
   velocities, and the $v_P/v_S$ ratio for a range of water saturations.
3. **Explain and quantify** the fizz-gas effect: why a small free-gas saturation
   lowers $v_P$ more than a large one, and why $v_S$ is the discriminator.
4. **Compute** Poisson's ratio and Young's modulus from velocities and a density,
   and explain why a brittleness index built from them is a convention rather
   than a physical property.
5. **Compute** the base of the gas-hydrate stability field from a hydrostatic
   pressure profile, a geotherm and a stated phase boundary, and state the
   sensitivity to bottom-water temperature and to the geothermal gradient.
6. **Explain** the bottom-simulating reflector as an impedance contrast, including
   its polarity.
7. **Compute** a Klinkenberg-corrected permeability and a uniaxial-strain closure
   stress, and state which quantities in each are model inputs.
8. **State** precisely which quantities in an unconventional assessment are
   physical and which are engineering or economic.

## Prerequisites

- [04-06-01 Source, Reservoir, Seal and Trap: The Petroleum System](./01-petroleum-system.md)
  — the system framework, and the derivation of the fluid effect on impedance.
- [04-01-05 Density, Porosity, Permeability and Elastic Properties](../01-earth-structure/05-rock-physics-basics.md)
  — porosity, permeability, and the elastic moduli.
- [04-05-04 Quaternary Climate Change and Landscape Records](../05-geomorphology-and-quaternary/04-quaternary-climate.md)
  — the thermal and sea-level history that sets where hydrates are stable today.

---

## 1. What "unconventional" means

| Property | Conventional | Unconventional |
|---|---|---|
| Permeability | millidarcy to darcy | nano- to microdarcy |
| Source and reservoir | Separate | Commonly the same rock |
| Seal | Required | Not required for the resource to exist |
| Migration | Essential | Minimal or absent |
| Flow mechanism | Matrix flow | Fracture flow after stimulation |
| Trap geometry | Essential | Not required |

The consequence for geophysics is a change of target. In a conventional play the
geophysical question is *where is the fluid* — geometry and fluid type. In an
unconventional play the questions are *where is the rock that can be fractured*,
*where is the rock rich in organic matter*, and *how is the stress oriented*.
Those are rock-mechanics and petrophysical questions, which is why
unconventional geophysics is dominated by seismic inversion, azimuthal anisotropy,
microseismic monitoring and borehole geomechanics rather than by fluid
indicators.

## 2. Shale: the source is the reservoir

**Where the gas is.** Adsorbed on organic matter and on clay surfaces, and free in
micropores and natural fractures. Organic richness (measured as total organic
carbon) and thermal maturity together determine how much is there; the *physics*
of the rock determines whether it will flow.

**The rock physics.** Replacing brine with gas in a porous rock changes the bulk
modulus far more than the density, so $v_P$ falls sharply while $v_S$ is almost
unchanged. This is why a $v_P/v_S$ ratio is a *lithology-and-fluid* discriminator
and why a P-wave amplitude anomaly alone cannot be inverted for gas saturation.
Gassmann's equation makes the point quantitative:

$$
K_\mathrm{sat} = K_\mathrm{dry}
+ \frac{(1 - K_\mathrm{dry}/K_\mathrm{min})^{2}}
{\dfrac{\phi}{K_\mathrm{fl}} + \dfrac{1-\phi}{K_\mathrm{min}}
 - \dfrac{K_\mathrm{dry}}{K_\mathrm{min}^{2}}},
$$

with the fluid modulus from Wood's harmonic average,
$1/K_\mathrm{fl} = S_w/K_w + (1-S_w)/K_g$.

**The fizz-gas result.** Because $K_\mathrm{fl}$ collapses as soon as any free
gas appears while the density is still nearly that of brine, **a 10 per cent gas
saturation can lower $v_P$ more than a 100 per cent saturation**. The demo
computes 2803 m s⁻¹ at $S_w = 0.9$ against 2900 m s⁻¹ at $S_w = 0$, from a
brine-saturated 3113 m s⁻¹ — and $v_S$ moves by 0.6 per cent. This is the single
most important rock-physics fact in the lesson: it is why "bright spot = gas" is
a fallacy, and why quantitative interpretation needs the shear information or a
calibrated rock-physics model.

**Brittleness.** Whether a shale can be stimulated depends on its ability to fail
in a brittle manner rather than to deform ductilely. Quartz- and carbonate-rich
shales are brittle; clay-rich shales are ductile. The elastic proxies are
Young's modulus (higher = more brittle) and Poisson's ratio (lower = more
brittle), both computable from $v_P$, $v_S$ and $\rho$:

$$
\nu = \frac{v_P^{2} - 2v_S^{2}}{2(v_P^{2} - v_S^{2})},
\qquad
E = \rho v_S^{2}\frac{3v_P^{2} - 4v_S^{2}}{v_P^{2} - v_S^{2}} .
$$

A "brittleness index" is then a rescaling of $(E, \nu)$ onto a 0–1 scale using
**arbitrary bounds**. The pair $(E,\nu)$ is physical; the index is a convention
that differs between publications, and it should always be reported with its
bounds.

## 3. Tight gas: permeability, slip flow and stress

**The permeability problem.** A tight sandstone may have a gas permeability of a
few microdarcy to a few tens of microdarcy. Two corrections matter:

- **Gas slippage (Klinkenberg).** Because gas molecules slip along pore walls at
  low pressure, a gas permeability measured at low mean pressure *overestimates*
  the equivalent liquid permeability:

$$
k_g = k_L\left(1 + \frac{b}{p}\right),
$$

with $b$ the slip factor [Pa], which is rock specific. For
$k_L = 10^{-16}$ m², $b = 2\times10^{6}$ Pa, the reported permeability is 3.0 times
the liquid value at 1 MPa and 1.1 times at 20 MPa. The correction vanishes at high
pressure, which is why the measurement protocol states the pressure.

- **Stress sensitivity.** Permeability falls as effective stress rises, because
  pore throats close. A core measured at atmospheric conditions does not report
  the in-situ permeability.

**Closure stress.** A hydraulic fracture stays open only if the fluid pressure
exceeds the stress acting normal to it, and in a normal-faulting regime the
minimum horizontal stress is the closure stress. For uniaxial strain (zero lateral
strain), the poroelastic relation is

$$
\sigma_h = \frac{\nu}{1-\nu}\left(\sigma_v - \alpha p\right) + \alpha p,
$$

with $\alpha$ the Biot coefficient. With $\nu = 0.25$, $\sigma_v = 40$ MPa,
$\alpha = 0.8$ and $p = 16$ MPa, this gives $\sigma_h = 21.9$ MPa, a ratio
$\sigma_h/\sigma_v = 0.55$. The relation is *derived* from the assumed strain
state; the stress state itself is *modelled* — only a leak-off test or a fracture
calibration measures it.

## 4. Gas hydrate: a phase-boundary problem

A gas hydrate is an ice-like solid in which gas molecules occupy cages in a
water lattice. It is stable at **high pressure and low temperature**, so its
occurrence in the subsurface is a *phase-boundary* question:

1. Compute the hydrostatic pressure profile, $P(z) = \rho_w g z$ — an exact
   calculation given the density.
2. Take the **dissociation boundary** $T_\mathrm{diss}(P)$ from a laboratory
   compilation. This is a measured curve, and no general formula replaces it.
3. Intersect it with the geotherm. The intersection is the **base of the gas
   hydrate stability zone** (BGHSZ), and the interval between the seafloor and the
   BGHSZ is where hydrate *can* exist.

**The key structural insight** is that the depth of the intersection is controlled
by the **difference between the geotherm's slope and the phase boundary's slope**,
not by either alone. In the T–z plane the dissociation boundary rises at only
about 9 K km⁻¹ (because pressure grows with depth while the required temperature
rises slowly), while a geotherm rises at 25–40 K km⁻¹, so an intersection exists
and its depth is

$$
h = \frac{T_\mathrm{diss}(P_\mathrm{floor}) - T_\mathrm{floor}}
{G - (\mathrm{d}T_\mathrm{diss}/\mathrm{d}z)} .
$$

**Consequence.** A 2 K warming of the bottom water thins the stability zone from
478 m to 383 m in the demo's configuration — and this is why hydrate stability is
studied as a climate problem as much as a resource problem.

**The geophysical signature: the BSR.** The bottom-simulating reflector is a
seismic reflection that parallels the seafloor at the base of the stability zone.
Its physical cause is the **acoustic impedance contrast** between hydrate-bearing
sediment above and free gas below: the free gas sharply lowers $v_P$, so the
impedance drops and the reflection coefficient is **negative** — a trough, with
the polarity reversed relative to the seafloor. The demo computes
$R = -0.1304$.

Two cautions. The BSR marks the *base of the stability field*, which is a
temperature-and-pressure surface, not a hydrate concentration; and hydrate itself
has elastic properties close to those of the pore fluid it displaces, so the *top*
of the stability zone is usually invisible and the internal concentration is not
recoverable from the reflection alone.

## 5. The geophysical signature of each unconventional play

| Play | Property that differs | Method |
|---|---|---|
| Shale gas/oil | Organic richness (radioactivity, resistivity, density), brittleness ($E$, $\nu$), anisotropy | Seismic inversion, azimuthal seismic, logs, microseismics |
| Tight gas | Low permeability: no direct contrast; porosity texture, fracture density, stress | Seismic attributes, azimuthal anisotropy, microseismic monitoring |
| Coal-bed methane | Low density, low velocity, low resistivity; cleat anisotropy | Seismic, density and resistivity logs |
| Gas hydrate | Velocity increase where hydrate fills pores; free gas below the BGHSZ | Seismic reflection (BSR), velocity analysis, controlled-source EM |
| Any stimulated play | Microseismic events, time-lapse changes | Microseismic monitoring, time-lapse seismic |
| Overburden hazards | Shallow gas, overpressure | Shallow seismic, GPR, gravimetry |

**The common thread** is that unconventional geophysics mostly measures
**mechanical** properties — moduli, anisotropy, fracture density and orientation,
stress — because the resource is limited by flow rather than by the presence of
fluid. Fluid indicators exist and matter, but the discriminating measurement is
usually the one that constrains the rock's ability to be fractured and to keep a
fracture open.

## 6. Where the physics ends

This section is the lesson's most important content.

**Physical, computable, and stated here:** saturated elastic moduli from
Gassmann; $v_P$, $v_S$ and their ratio; Poisson's ratio and Young's modulus;
brittleness *given stated bounds*; hydrostatic pressure; the hydrate stability
depth given a stated phase boundary; reflection coefficients; the Klinkenberg
correction given a stated $b$; the closure-stress relation given a stress state.

**Not physical, not computed here:** the recovery factor; the estimated ultimate
recovery of a well; the drainage area of a fracture stage; the decline rate; the
resource and reserve volumes; the economics. These depend on completion design,
well spacing, operational practice, energy price, fiscal regime and regulation.
They change with technology and with markets, and they are not measurements.

The honest form of an unconventional statement is therefore conditional, for
example: "the rock physics is consistent with a gas-charged interval of the
following thickness and the following brittleness; how much of that gas is
recovered depends on parameters that are outside this analysis."

## 7. Assumptions and regime of validity

**Gassmann.**

1. The rock is isotropic, homogeneous, and macroscopically homogeneous; the pore
   fluid is mobile and the frequencies are low enough for the fluid pressure to
   equilibrate (the seismic band).
2. The shear modulus is independent of the fluid. This is exact for a
   homogeneous fluid at low frequency and is the reason $v_S$ is treated as a
   lithology indicator.
3. $K_\mathrm{dry}$, $K_\mathrm{min}$ and $\phi$ are known. They are the
   uncertainty, not the equation.
4. Wood's average assumes the fluids are mixed uniformly at a scale fine relative
   to the wavelength. Patchy saturation violates it and produces a different
   (higher) velocity for the same saturation.

**Brittleness and stress.**

1. The $(E,\nu)$ computation assumes isotropy; shales are strongly anisotropic,
   so a single $E$ and $\nu$ are approximations.
2. The closure-stress relation assumes uniaxial strain and linear poroelasticity.
   Tectonic strain, natural fractures and stress rotation all break it.
3. The brittleness index's bounds are arbitrary.

**Hydrate.**

1. Hydrostatic pressure is assumed. Overpressure and gas columns change it.
2. The phase boundary is taken from a compilation and is composition dependent:
   a methane-dominated gas and a gas with significant heavier components have
   different boundaries.
3. Salinity depresses the stability field and is often unknown.
4. The intersection gives the depth at which hydrate *can* exist; it says nothing
   about whether hydrate is present, and a BSR can be absent where hydrate exists
   and present where the gas column is thin.

**Klinkenberg.**

1. Valid for gas flow in a porous medium at pressures where slip matters; the
   slip factor $b$ is rock specific and is measured, not predicted.
2. It corrects for slip only; it does not correct for stress sensitivity, which
   must be measured separately.

## 8. Quantitative treatment with units

| Quantity | Symbol | Unit | Value used here (MODELLED) |
|---|---|---|---|
| Mineral bulk modulus | $K_\mathrm{min}$ | GPa | 36 |
| Fluid moduli | $K_w$, $K_g$ | GPa | 2.8, 0.05 |
| Dry-frame moduli | $K_\mathrm{dry}$, $\mu$ | GPa | 8, 6 |
| Porosity | $\phi$ | – | 0.30 |
| Densities | $\rho$ | kg m⁻³ | 2650 (grain), 1050 (water), 200 (gas) |
| Seabed pressure | $P_\mathrm{floor}$ | MPa | 15.16 at 1500 m water depth |
| Geothermal gradient | $G$ | K km⁻¹ | 30 |
| Klinkenberg slip factor | $b$ | Pa | $2.0\times10^{6}$ |
| Biot coefficient | $\alpha$ | – | 0.8 |

**Worked check (fizz gas).** With $K_\mathrm{dry} = 8$ GPa,
$K_\mathrm{min} = 36$ GPa, $\phi = 0.30$ and $K_w = 2.8$ GPa:

$$
K_\mathrm{sat} = 8 + \frac{(1-8/36)^{2}}{0.30/2.8 + 0.70/36 - 8/1296}
= 8 + \frac{0.6049}{0.120414} = 13.02\ \mathrm{GPa},
$$

and with $\rho = 2170$ kg m⁻³ the velocities are $v_P = 3113$ m s⁻¹ and
$v_S = 1663$ m s⁻¹. Replacing the fluid with a 90 per cent brine / 10 per cent gas
mixture gives $K_\mathrm{fl} = 0.431$ GPa and $K_\mathrm{sat} = 8.85$ GPa, so
$v_P = 2803$ m s⁻¹ — **lower than the fully gas-saturated 2900 m s⁻¹**.

## 9. Python demonstration

[`code/unconventional_resources_demo.py`](./code/unconventional_resources_demo.py)
computes the Gassmann fluid substitution and the fizz-gas effect, the elastic
moduli and a brittleness index with its bounds, the hydrate stability field and
its sensitivity, the BSR reflection coefficient, and the Klinkenberg correction
with the closure stress.

```text
   S_w    K_fl (GPa)  K_sat (GPa)  rho    vp      vs     Vp/Vs   nu
   1.00      2.8000      13.0238    2170    3113   1663   1.872  0.300
   0.90      0.4308       8.8524    2144    2803   1673   1.676  0.224
   0.00      0.0500       8.1006    1915    2900   1770   1.638  0.203
    fully brine-saturated: vp = 3113 m/s, vs = 1663 m/s
    90 per cent brine, 10 per cent free gas: vp = 2803 m/s (-9.9 per cent), vs = 1673 m/s (+0.6 per cent)
    fully gas-saturated: vp = 2900 m/s (-6.8 per cent), vs = 1770 m/s (+6.4 per cent)
    quartz-rich (brittle)    rho = 2650, vp = 3600, vs = 2100: E =  29.0 GPa, nu = 0.242
    quartz-rich (brittle)   : BI_E = 0.381, BI_nu = 0.789, BI = 0.585
  COMPUTED hydrostatic pressure at the seafloor P = rho g z = 15.156 MPa
  COMPUTED the boundary rises at 9.09 K/km in
  COMPUTED base of the stability zone at 478.3 m below the seafloor
                   2.0                30            478.3
                   4.0                30            382.7
  COMPUTED R = -0.1304, a *negative* coefficient.
                     1.0   3.0000e-16            3.000
                    20.0   1.1000e-16            1.100
     0.15           17.60                 0.440
     0.35           27.45                 0.686
```

### What to observe

- The fizz-gas table is the decisive output: $v_P$ falls 9.9 per cent at
  $S_w = 0.9$ but only 6.8 per cent at $S_w = 0$, while $v_S$ moves 0.6 per cent
  and 6.4 per cent respectively. The $v_S$ change at full gas saturation is a
  **density** effect, not a fluid-modulus one — worth separating, because it means
  $v_P/v_S$ is not a pure gas indicator either.
- The brittleness index gives 0.585 for the quartz-rich shale and 0.273 for the
  clay-rich one, and the ordering is robust while the numbers are not: change the
  bounds and both values change.
- The hydrate stability zone is 478 m thick for a 2 °C seabed and a 30 K km⁻¹
  gradient, and it thins to 383 m if the bottom water warms by 2 K. That is a
  20 per cent reduction from a 2 K change, and it is the whole reason hydrate is
  discussed in climate terms.
- The BSR reflection coefficient is $-0.1304$: negative, so a trough, with the
  polarity reversed relative to the seafloor.
- The Klinkenberg ratio is 3.0 at 1 MPa and 1.1 at 20 MPa. The measured
  permeability of a tight rock is a *pressure-dependent* number, and a report that
  omits the pressure omits the answer.

## 10. Common mistakes

1. **Reading a bright spot as gas saturation.** The fizz-gas effect makes the
   mapping non-unique from P-wave data alone.
2. **Assuming the shear modulus is fluid sensitive.** Gassmann says it is not, and
   that assumption is the basis of the $v_P/v_S$ discriminator.
3. **Using a brittleness index without its bounds.** Two papers with different
   bounds will disagree about the same rock.
4. **Treating an isotropic $E$ and $\nu$ as adequate for a shale.** Shales are
   strongly anisotropic, and the anisotropy is often the *target* (fracture
   orientation).
5. **Quoting a permeability without its pressure and stress state.** A core
   measurement is not an in-situ value.
6. **Assuming a BSR is a hydrate indicator.** It marks the base of the stability
   field; hydrate may be absent above it and gas may be absent below it.
7. **Taking the hydrate phase boundary from a general formula.** It is a measured
   curve and is composition and salinity dependent.
8. **Using hydrostatic pressure where there is a gas column.** A gas column
   reduces the pressure at a given depth, which shifts the stability field.
9. **Confusing a closure stress with a measured minimum horizontal stress.** The
   relation is derived from an assumed strain state.
10. **Quoting a recovery factor, an estimated ultimate recovery or a reserve.**
    These are engineering, economic and regulatory quantities, and none is
    computed or stated in this lesson.

## 11. Real-world applications

- **Unconventional play evaluation.** Organic richness and maturity from logs,
  brittleness and stress from seismic inversion, and sweet-spot delineation from
  the combination.
- **Fracture monitoring.** Microseismic event locations and time-lapse seismic
  for the geometry of the stimulated volume
  ([10-06 Near-Surface Monitoring](../../10-gpr-near-surface/06-nearsurface-monitoring/README.md)).
- **Hydrate assessment.** Seismic BSR mapping, velocity analysis, and
  controlled-source EM for the resistivity of a hydrate-bearing interval
  ([11-03-05 Unconventional Geophysics](../../11-exploration-geophysics/03-hydrocarbon-exploration/05-unconventional-geophysics.md)).
- **Geohazard and drilling safety.** Shallow gas, overpressure and hydrate
  dissociation during drilling are the same physics viewed from the operational
  side ([11-06-01 Site Investigation](../../11-exploration-geophysics/06-geotechnical-and-engineering/01-site-investigation.md)).
- **Carbon storage.** The same rock physics of fluid substitution and the same
  time-lapse monitoring problem, with CO₂ in place of hydrocarbon
  ([05-04 Rock Physics and Property Relations](../../05-core-geophysics/04-rock-physics/README.md)).
- **Gas-hydrate and climate.** The stability field as a function of bottom-water
  temperature is the link from a seismic horizon to a climate question
  ([04-05-04 Quaternary Climate Change and Landscape Records](../05-geomorphology-and-quaternary/04-quaternary-climate.md)).
- **Geomechanics for geothermal and storage.** The closure-stress relation and
  the brittleness concept are the same in an enhanced geothermal system
  ([lesson 03](./03-geothermal-systems.md)).

## 12. Further reading

- **Mavko, G., Mukerji, T., & Dvorkin, J. *The Rock Physics Handbook*
  (Cambridge).** Gassmann's equation, Wood's average, and the limits of both.
  Level: reference.
- **Avseth, P., Mukerji, T., & Mavko, G. *Quantitative Seismic Interpretation*
  (Cambridge).** The fizz-gas problem and the workflow that addresses it.
  Level: graduate.
- **Zoback, M. D. *Reservoir Geomechanics* (Cambridge).** Stress state, closure
  stress, fracture mechanics and the measurement of each. Level: graduate.
- **Rickman, R., & others (2008). A practical use of shale petrophysics for
  stimulation design optimization.** *SPE*. The origin of the brittleness-index
  formulation, including its arbitrary bounds. Level: professional.
- **Klinkenberg, L. J. (1941). The permeability of porous media to liquids and
  gases.** *API Drilling and Production Practice*. The original slip correction.
  Level: classic paper.
- **Sloan, E. D., & Koh, C. A. *Clathrate Hydrates of Natural Gases* (CRC).** The
  phase behaviour behind §4. Level: graduate reference.
- **Kvenvolden, K. A. on gas hydrates in the geosphere.** The occurrence and the
  stability-field concept, including the caution that a BSR is not a resource
  estimate. Level: advanced review.
- **Boswell, R., & Collett, T. S. on hydrate resource assessment.** An explicit
  treatment of why a hydrate resource estimate is dominated by recovery
  assumptions. Level: professional.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 13. Related lessons

- [01 Source, Reservoir, Seal and Trap: The Petroleum System](./01-petroleum-system.md)
  — the conventional contrast, and the impedance consequence derived there.
- [03 Geothermal Systems, Heat Flow and Resource Assessment](./03-geothermal-systems.md)
  — the same discipline about recovery factors, in a different resource.
- [04 Aquifer Types and Groundwater Occurrence](./04-groundwater-aquifers.md)
  — permeability and fluid flow in the shallow subsurface.
- [02 Mineral Deposit Types and Their Geophysical Signatures](./02-mineral-deposits.md)
  — the property-contrast method applied to solids rather than fluids.
- [04-05-04 Quaternary Climate Change and Landscape Records](../05-geomorphology-and-quaternary/04-quaternary-climate.md)
  — the temperature history that sets the present hydrate stability field.
- [05-04 Rock Physics and Property Relations](../../05-core-geophysics/04-rock-physics/README.md)
  — effective-medium theory, Gassmann and anisotropy in full.
- [05-04-05 Anisotropy in Rock](../../05-core-geophysics/04-rock-physics/05-anisotropy-rock.md)
  — why a single $E$ and $\nu$ do not describe a shale.

Exercises:
[`exercises/05-unconventional-resources-exercises.md`](./exercises/05-unconventional-resources-exercises.md)
and
[`exercises/05-unconventional-resources-solutions.md`](./exercises/05-unconventional-resources-solutions.md).

## Self-assessment checklist

- [ ] I can define "unconventional" in terms of permeability and system
      geometry. (§1)
- [ ] I can write and apply Gassmann's equation with Wood's fluid average. (§2,
      §8)
- [ ] I can explain and quantify the fizz-gas effect. (§2, §9)
- [ ] I can compute Poisson's ratio and Young's modulus from $v_P$, $v_S$ and
      $\rho$. (§2)
- [ ] I can say why a brittleness index is a convention and not a property. (§2,
      §7)
- [ ] I can compute the base of the hydrate stability zone and its sensitivity to
      bottom-water temperature. (§4, §9)
- [ ] I can explain the BSR as an impedance contrast and state its polarity. (§4)
- [ ] I can apply the Klinkenberg correction and say what it does and does not
      correct. (§3)
- [ ] I can compute a uniaxial-strain closure stress and state what is measured
      and what is modelled. (§3)
- [ ] I can separate what is physical in an unconventional assessment from what is
      engineering or economic. (§6)
