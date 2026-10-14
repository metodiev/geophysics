---
id: 04-05-02
title: "Glacial and Periglacial Landforms and Sediments"
level: intermediate
prereqs: ["04-05-01", "04-01-05"]
estimated_minutes: 75
tags: [glacial, periglacial, till, ice-flow, glen-flow-law, isostasy, gpr-ice]
---

# Glacial and Periglacial Landforms and Sediments

Ice has two properties that make it a different geomorphic agent from water. It
is a **solid that deforms**, so it erodes by abrasion and quarrying over its whole
bed rather than by traction along a single thread; and it is **buoyant and
viscous**, so it can transport any grain size from clay to boulders without
sorting them. The result is a landform assemblage that is unmistakable in shape
and, for the geophysicist, unusually favourable: tills and gravels are soft,
porous and low-velocity against the bedrock they overlie, and ice is a
low-loss dielectric that radar penetrates for kilometres.

This lesson develops the flow mechanics that produce the shapes, the
sedimentology of the deposits, the periglacial processes that act at the margins,
and the property contrasts that make each element detectable. It is the lesson
in this folder that is closest to the practice of near-surface geophysics: the
everything-over-till setting of a glaciated shield or a mountain valley is the
standard survey environment for shallow seismic, surface-wave, GPR and
refraction work.

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** a glacier mass balance, the equilibrium-line altitude, and the
   accumulation–ablation area ratio, and say how each is measured.
2. **Compute** the basal driving stress and the depth-averaged internal
   deformation velocity of an ice mass from Glen's flow law, and state the
   temperature and stress dependence of the flow-law coefficient.
3. **Use** the perfect-plasticity model to estimate ice thickness from surface
   slope, and say why that model is quantitatively wrong but qualitatively
   useful.
4. **Distinguish** the landforms of glacial erosion from those of glacial
   deposition, and name the sediment type that forms each.
5. **State** the property contrasts of till, glaciofluvial sand and gravel, and
   ice against bedrock, and choose a method that can see each contact.
6. **Compute** the Airy isostatic depression and the relaxation time of a
   viscous mantle, and explain post-glacial rebound as a measurement of
   viscosity.
7. **Compute** the Stefan active-layer depth and the frost-heave magnitude, and
   state the assumptions of each.
8. **Explain** why glacial sediments are both the most common shallow aquifer in
   glaciated terrain and a persistent geotechnical hazard.

## Prerequisites

- [04-05-01 Landform Processes and Shapes](./01-landforms.md) — the mass balance
  frame and the transport laws that ice replaces here.
- [04-01-05 Density, Porosity, Permeability and Elastic Properties](../01-earth-structure/05-rock-physics-basics.md)
  — the petrophysics used in §6.

---

## 1. The glacier as a system

A glacier is a body of ice with a **mass balance**: accumulation (snowfall,
avalanche, refreezing) minus ablation (melt, sublimation, calving). The
**equilibrium-line altitude** (ELA) is the elevation where the two are equal; it
is a *climatic* quantity and the single number that a palaeoclimate
reconstruction from glacial landforms tries to recover.

Above the ELA the ice is cold and the surface is in accumulation; below it the ice
is at the pressure melting point in summer and the surface is lowering. Mass
balance is measured by stake networks and repeat altimetry today, and inferred
from trimlines, moraine positions and lake sediments in the past. Every such
inference is a model, because the ELA that produced a moraine is not directly
observable.

Ice flows because of its own weight. What matters for the landforms is the pair
(velocity, discharge), where the ice flux per unit width is $q = \bar{u}H$.

## 2. Ice flow: driving stress, Glen's law and thickness

The **basal driving stress** of a glacier is the downslope component of its own
weight:

$$
\tau_b = \rho_i g H \sin\alpha,
$$

with $\rho_i \approx 917$ kg m⁻³ the density of ice, $g = 9.81$ m s⁻²,
$H$ the thickness [m] and $\alpha$ the surface slope. For
$H = 1000$ m and $\alpha = 1^\circ$ this is $1.57\times10^{5}$ Pa — of the order of
$10^{5}$ Pa, which is the observed range for real glaciers and the reason a
yield-stress model works at all.

Ice deforms by creep, described by **Glen's flow law**, a power law with exponent
$n \approx 3$:

$$
\dot{\varepsilon} = A\,\tau^{n}, \qquad
A(T) = A_0 \exp\!\left[\frac{Q}{R}\left(\frac{1}{T_0} - \frac{1}{T}\right)\right].
$$

Integrating $\dot{\varepsilon}$ over depth with a shear stress that decreases
linearly to zero at the surface gives the depth-averaged velocity contribution
from internal deformation:

$$
\bar{u}_d = \frac{2A}{n+1}\,\tau_b^{n} H .
$$

Two structural facts follow immediately and are worth memorising:

- Velocity is **linear in $A$**, so a 10 K cooling cuts the deformation rate by
  roughly a factor of 3 — a large, well-documented effect.
- Velocity depends on the driving stress **cubed**, so a 10 per cent error in
  thickness is a 33 per cent error in velocity.

Sliding at the bed is a separate, additive term that depends on effective
pressure and on the subglacial drainage system. It is *not* derived here; the
demo treats it as an explicitly flagged multiplier so that its effect can be seen
without pretending it is computed from first principles.

### Perfect plasticity: a useful wrong model

If the bed is assumed to yield at a constant stress $\tau_0$, then $H = \tau_0 /
(\rho_i g \sin\alpha)$. The result — thickness inversely proportional to the sine
of the slope — is qualitatively right (ice sheets are kilometres thick on plains)
and quantitatively wrong near the margin where sliding, not yield, sets the
profile.

## 3. Landforms of glacial erosion

| Landform | Shape | Dominant process |
|---|---|---|
| Cirque (corrie, cwm) | Armchair hollow with a steep headwall | Headwall freeze–thaw plus rotational flow drawdown |
| Arête and pyramidal peak | Narrow ridge, sharp summit | Headward erosion of two or three cirques |
| U-shaped valley / trough | Parabolic cross-section, hanging tributaries | Lateral abrasion by a thick, sliding glacier |
| Roche moutonnée | Asymmetric bedrock boss, gentle up-ice | Abrasion on the stoss side, quarrying on the lee |
| Striations, chatter marks | Lineations on bedrock | Abrasion by entrained clasts |
| Overdeepening, rock basin | Closed basin below sea level | Selective quarrying under fast flow |
| Fjord, finger lake | Long, deep, straight trough | Trough excavation extended by glacial retreat |

The geophysical relevance of the erosional suite is that it is **bedrock
geometry**, so it is expressed as a density or velocity contrast against whatever
fills the hollow. An overdeepening filled with water or with unconsolidated
sediment is one of the largest shallow density contrasts available, and is mapped
by gravity, seismic refraction and, in freshwater, by GPR.

## 4. Landforms of glacial deposition, and the sediments that make them

Glacial sediments are classified by where they were deposited relative to the
ice, because that controls sorting and therefore porosity and permeability:

- **Till (diamicton).** Unsorted, matrix-supported; deposited directly at the base
  or from the surface of the ice. Low permeability where the matrix is clay-rich.
- **Glaciofluvial sand and gravel.** Sorted by meltwater, high permeability, the
  productive aquifer unit.
- **Glaciolacustrine silt and clay.** Varved, very low permeability, the classic
  aquitard and the classic slope-stability problem.
- **Glaciomarine clay.** Often overconsolidated to a depth set by later erosion;
  its strength profile controls the geotechnical behaviour.

| Landform | Architecture | Sediment |
|---|---|---|
| Ground moraine / till sheet | Sheet of diamicton, metres to tens of metres | Till |
| Terminal and lateral moraine | Ridge, boulder-rich, cross-valley or along flank | Till, often ablation-dominated |
| Drumlin | Streamlined oval hill, long axis parallel to flow | Till, sometimes with a stratified core |
| Esker | Sinuous ridge, sinuous and steep-sided | Sorted glaciofluvial gravel |
| Kame and kettle | Hummocky mounds and closed hollows | Sorted sand and gravel, buried ice blocks |
| Outwash plain (sandur) | Broad sheet with braided channels | Sorted sand and gravel |

### Why glacial deposits matter for near-surface geophysics

Glaciated terrain is the single most common setting for shallow geophysical
surveys in Europe and North America, and the reason is a set of large, systematic
property contrasts:

| Material | Density (kg m⁻³) | $v_P$ (m s⁻¹) | Resistivity (Ω m) | Susceptibility (SI) |
|---|---|---|---|---|
| Till, saturated, soft | 1900–2100 | 1400–1800 | 10–100 | $10^{-4}$–$10^{-2}$ |
| Till, compacted, dry | 1800–2000 | 700–1200 | $10^{2}$–$10^{3}$ | $10^{-4}$–$10^{-2}$ |
| Glaciofluvial sand and gravel | 1800–2100 | 1500–1800 | $10^{2}$–$10^{3}$ | $10^{-5}$–$10^{-3}$ |
| Glaciolacustrine clay | 1700–2000 | 1500–1800 | 5–50 | $10^{-5}$–$10^{-4}$ |
| Crystalline bedrock | 2600–2800 | 4500–6200 | $10^{3}$–$10^{5}$ | $10^{-3}$–$10^{-1}$ |
| Limestone bedrock | 2500–2700 | 4000–6000 | $10^{2}$–$10^{4}$ | $10^{-5}$–$10^{-4}$ |
| Ice (cold) | 917 | 3400–4000 | $10^{6}$–$10^{8}$ (dielectric) | 0 |

All values are **nominal literature ranges**, not measurements of any site:
density and velocity vary by ranges between rocks and by moisture and
compaction within one, not by percentages. Three consequences:

1. **Sediment over bedrock is a large seismic contrast.** Both density and
   velocity step up, so the normal-incidence reflection coefficient is a few
   tenths, not a few per cent.
2. **Dry versus saturated sediment is a large contrast in the *same* sediment.**
   The water table is therefore the strongest shallow reflector in the section.
3. **The internal contrasts within tills are small.** Mapping the internal
   architecture of a till sheet needs a method sensitive to something else —
   conductivity (clay content), permittivity (water content), or the shear
   modulus (stiffness) — rather than P-wave impedance.

## 5. Periglacial processes

Periglacial refers to the cold, non-glacial environments at the margins and in
the forefields: permafrost, seasonal freezing, and the landforms that freezing and
thawing produce.

- **Active layer.** The seasonally thawed layer above permafrost. Its thickness
  sets the depth of seasonal mechanical and geochemical activity and is the
  first-order indicator of permafrost state.
- **Patterned ground.** Sorted circles, polygons and stripes, produced by frost
  heave and by lateral sorting of clasts. Their size scales with the active-layer
  depth, which makes them a proxy for palaeoclimate.
- **Solifluction lobes.** Slow downslope flow of water-saturated soil, the
  periglacial analogue of a creep law with a much larger effective diffusivity.
- **Ice wedges and their casts.** Polygonal networks filled with ice, or, after
  melting, with sand; they are both a geohazard and a palaeoclimate indicator.
- **The Stefan problem.** Where latent heat dominates and the surface temperature
  is taken as a step, the freezing (or thawing) front advances as
  $X = \sqrt{2k\Delta T t / (L\rho_w)}$.

Frost heave follows from the ~9 per cent volume expansion of water on freezing,
but the observed heave of a wet soil is usually much smaller than that, because
water drains and refreezes rather than freezing in place. Any number quoted for
heave is an upper bound unless the drainage and segregation ice are modelled.

## 6. Quantitative treatment with units

| Quantity | Symbol | Unit | Value used here (MODELLED) |
|---|---|---|---|
| Ice density | $\rho_i$ | kg m⁻³ | 917 |
| Driving stress | $\tau_b$ | Pa | computed |
| Flow-law coefficient (0 °C) | $A_0$ | Pa⁻³ s⁻¹ | $2.4\times10^{-24}$ |
| Flow-law exponent | $n$ | – | 3 |
| Creep activation energy | $Q$ | J mol⁻¹ | $6.0\times10^{4}$ |
| Plastic yield stress | $\tau_0$ | Pa | $1.0\times10^{5}$ |
| Mantle viscosity | $\eta$ | Pa s | $1\times10^{21}$ |
| Ice permittivity | $\varepsilon_r$ | – | 3.17 |
| Latent heat of fusion | $L$ | J kg⁻¹ | $3.34\times10^{5}$ |

**Worked check.** With $H = 1000$ m and $\alpha = 1^\circ$:
$\tau_b = 917 \times 9.81 \times 1000 \times 0.017452 = 1.570\times10^{5}$ Pa, and
$\bar{u}_d = \frac{2 \times 2.4\times10^{-24}}{4}(1.570\times10^{5})^{3}(1000)
= 4.64\times10^{-6}$ m s⁻¹ $= 146.5$ m yr⁻¹.

That velocity is high for a valley glacier and is entirely plausible for a fast
outlet of an ice sheet with a 1° surface. It is also a warning: because the
stress enters as the cube, the same formula gives 53.7 m yr⁻¹ at $-10$ °C and
5.6 m yr⁻¹ at $-30$ °C, so a quoted ice velocity is meaningless without a stated
temperature and thickness.

**Isostasy and rebound.** Airy local isostasy gives an immediate depression
$\Delta h = (\rho_i/\rho_m)H$, i.e. 27.8 per cent of the ice thickness, for
$\rho_m \approx 3300$ kg m⁻³. The relaxation time of a viscous half space loaded
at wavelength $\lambda$ is

$$
\tau = \frac{2\eta k}{\rho_m g}, \qquad k = \frac{2\pi}{\lambda},
$$

so $\tau$ is **linear in the wavelength**: 123 kyr at 100 km, 12.3 kyr at
1000 km, 4.1 kyr at 3000 km, for $\eta = 10^{21}$ Pa s. This is why rebound is a
useful constraint on viscosity: the observed wavelength dependence of the
present-day uplift rate is a measurement of $\eta$, and the geodetic data are the
observable (see the GNSS and gravity references in §10).

## 7. Assumptions and regime of validity

1. **Glen's law integration** assumes a uniform slope, a stress that varies
   linearly with depth, no longitudinal coupling, and no sliding. It is therefore
   an *internal deformation* velocity only.
2. **$A$ is not a constant.** It depends strongly on temperature, on impurity
   content and on fabric; the Arrhenius form is a parameterisation with a stated
   activation energy, not a derivation.
3. **Perfect plasticity** ignores sliding, longitudinal stresses and the
   thermodynamic coupling at the margin. Use it for order-of-magnitude only.
4. **Airy isostasy** assumes no flexural rigidity. For loads narrower than the
   elastic thickness it overestimates depression considerably.
5. **The relaxation-time formula** assumes a uniform viscous half space and a
   single Fourier wavelength; real relaxation involves a layered, non-Newtonian
   mantle.
6. **The Stefan solution** assumes latent heat dominates, constant properties,
   and a step surface temperature. It over-predicts where the soil is dry or the
   winter temperature oscillates (which is always).
7. **Property ranges are nominal.** Any survey must measure, not assume, the
   density and velocity of its own materials.

## 8. Python demonstration

[`code/glacial_landforms_demo.py`](./code/glacial_landforms_demo.py) computes
the driving stress and the deformation velocity, its temperature and thickness
sensitivity, the perfect-plasticity thickness, an explicitly flagged sliding
sensitivity, the Airy depression and relaxation time, the seismic reflection
coefficients of the sediment–bedrock contacts, the GPR velocity and travel time
in ice, and the periglacial active-layer and frost-heave numbers.

```text
  COMPUTED driving stress tau_b = rho g H sin(alpha) = 1.5700e+05 Pa
  COMPUTED depth-averaged deformation velocity
    u_d = 2A/(n+1) tau_b^n H = 4.6437e-06 m/s = 146.54 m/yr
    T =    0.0 degC: A = 2.400e-24 Pa^-3 s^-1 (100.0 per cent of A(0)), u_d =  146.543 m/yr
    T =  -10.0 degC: A = 8.794e-25 Pa^-3 s^-1 ( 36.6 per cent of A(0)), u_d =   53.698 m/yr
    slope  0.50 deg: H =   1273.9 m, tau_b = 1.0e+05 Pa
    slope  1.00 deg: H =    637.0 m, tau_b = 1.0e+05 Pa
    ice thickness   2000 m: Airy depression =  555.76 m (27.79 per cent of the load)
    lambda =   1000 km: tau = 3.8817e+11 s =     12301 yr =  12.30 kyr
    till over shale bedrock       : R = +0.3701  (37.01 per cent of the amplitude)
    till over granite bedrock     : R = +0.6231  (62.31 per cent of the amplitude)
  COMPUTED the same till dry vs saturated, a pure fluid effect:
    R = +0.3035 for the water table inside the till.
    depth     500 m: two-way travel time =    5.939 us
  COMPUTED at 100 MHz the wavelength is 1.684 m, so the
  quarter-wavelength vertical resolution is about 0.421 m.
  COMPUTED Stefan depth X = sqrt(2 k dT t / (L rho_w)) = 1.4580 m
```

### What to observe

- The perfect-plasticity thickness halves as the slope doubles: 1274 m at 0.5°,
  637 m at 1°, 318 m at 2°. That inverse-sine behaviour is the model's only
  robust prediction.
- The reflection coefficient for till over bedrock is 0.37 to 0.62, which is
  roughly 25 to 40 times larger in energy than a typical deep crustal reflection.
  Shallow sediment mapping is easy for the same reason that deep exploration is
  hard: the contrasts are large and the targets are close.
- Till over ice gives only 0.04, because ice and water-saturated sediment have
  nearly the same acoustic impedance. This is why the ice-bed contact is mapped
  by radar rather than by seismic reflection: radar sees the *dielectric*
  contrast, which is very large.
- The active-layer depth is 1.46 m for these parameters and scales as the square
  root of both the season length and the surface offset, so a 60 per cent longer
  winter deepens it by 26 per cent, not 60 per cent.

## 9. Common mistakes

1. **Quoting an ice velocity without a thickness and a temperature.** With
   $\bar u \propto A H^{4}$ in the stress-dominated regime, the number is
   meaningless without both.
2. **Treating till as a single material.** Dry, saturated, overconsolidated and
   clay-rich tills differ by a factor of two in velocity and by an order of
   magnitude in resistivity.
3. **Assuming the sub-till surface is bedrock.** Buried valleys, overdeepenings
   and stacked till sheets are the rule in glaciated terrain, not the exception.
4. **Using a P-wave survey to find a sand-and-gravel aquifer beneath clay.** Both
   have similar velocities; the contrast is in conductivity and in shear modulus.
5. **Reading a moraine ridge as a purely depositional feature.** Many are
   ice-marginal push structures, so their internal geometry is deformed.
6. **Ignoring rebound in a levelling or GNSS dataset.** Present-day uplift of a
   few mm yr⁻¹ is a real signal and a real bias for any subsidence measurement in
   the same region.
7. **Applying Airy isostasy to a 20 km load.** Flexural rigidity supports narrow
   loads, and the local model overestimates the depression by a large factor.
8. **Taking an active-layer thickness as a permafrost depth.** The active layer
   *is* the thawed layer; the permafrost is below it and its base is a different
   and much less certain horizon.
9. **Assuming the ice-bed interface is uniformly reflective.** A deformable
   till bed is acoustically transparent and a hard bed is not; the two strata
   look completely different in a radar record.
10. **Stating a glacial chronology from a landform alone.** A moraine gives a
    position, not an age; the age comes from a dated sample, with its own
    assumptions.

## 10. Real-world applications

- **Groundwater in glaciated basins.** Buried valleys and outwash aquifers supply
  a large fraction of the drinking water in northern Europe and North America,
  and their geometry is mapped by a combination of seismic refraction,
  transient electromagnetics and boreholes
  ([14-01-02 Aquifer Types and Properties](../../14-hydrology-hydrogeophysics/01-hydrology-fundamentals/02-aquifer-types-and-properties.md)).
- **GPR on glaciers and ice sheets.** Radar is the standard tool for ice
  thickness, internal layers, the bed and subglacial lakes, because cold ice is a
  very low-loss dielectric ([10-03-02 GPR Glaciology](../../10-gpr-near-surface/03-gpr-applications/02-gpr-glaciology.md)).
- **Geotechnical site investigation.** Till thickness, buried channels and
  glaciomarine clay are the three things a foundation, tunnel or road project in
  glaciated terrain needs before anything is built
  ([11-06-01 Site Investigation](../../11-exploration-geophysics/06-geotechnical-and-engineering/01-site-investigation.md)).
- **Post-glacial rebound and sea level.** GNSS and gravity observations of
  rebound supply the viscosity constraints used in every glacial isostatic
  adjustment model ([07 Gravity and Geodesy](../../07-gravity-geodesy/README.md)).
- **Permafrost monitoring.** Electrical resistivity and seismic refraction track
  the active layer and the thaw front, and the time-lapse signal is the
  measurement ([10-06 Near-Surface Monitoring](../../10-gpr-near-surface/06-nearsurface-monitoring/README.md)).
- **Palaeoclimate from glacial geology.** Moraine positions, trimlines and
  equilibrium-line reconstructions constrain past temperature and precipitation,
  and are the land-based counterpart of the records in
  [lesson 04](./04-quaternary-climate.md).
- **Aggregate resources.** Eskers and outwash plains are the primary sand and
  gravel sources in glaciated regions, and their internal structure is a seismic
  and GPR problem.

## 11. Further reading

- **Paterson, W. S. B. *The Physics of Glaciers* (Elsevier).** The standard
  reference for §2, the flow law, its temperature dependence and its measured
  coefficients. Level: graduate.
- **Cuffey, K. M., & Paterson, W. S. B. *The Physics of Glaciers* (4th ed.).**
  The current edition of the same work, with updated coefficient values. Level:
  graduate.
- **Benn, D. I., & Evans, D. J. A. *Glaciers and Glaciation* (Routledge).** The
  landform and sedimentology reference for §3 and §4. Level: undergraduate to
  graduate.
- **Boulton, G. S., & others on subglacial deformation.** The literature that
  changed the interpretation of tills from lodgement to deformation. Level:
  advanced.
- **French, H. M. *The Periglacial Environment* (Wiley).** Permafrost, active
  layer, patterned ground and the geotechnical consequences. Level: advanced.
- **Sugden, D. E., & John, B. S. *Glaciers and Landscape* (Arnold).** Classic
  treatment of the landform assemblage as a process signature. Level:
  undergraduate.
- **Anderson, R. S., & Anderson, S. P. *Geomorphology* (Cambridge).** Chapters on
  glacial and periglacial processes that put §2 in the same notation as
  [lesson 01](./01-landforms.md). Level: undergraduate to graduate.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 12. Related lessons

- [01 Landform Processes and Shapes](./01-landforms.md) — the transport laws that
  ice replaces.
- [03 Fluvial, Coastal and Aeolian Systems](./03-fluvial-coastal.md) — the
  meltwater and outwash side of the same sediment system.
- [04 Quaternary Climate Change and Landscape Records](./04-quaternary-climate.md)
  — the climate that set the ELA and the ice volume.
- [04-01-05 Density, Porosity, Permeability and Elastic Properties](../01-earth-structure/05-rock-physics-basics.md)
  — where the property table of §4 comes from.
- [04-04-04 Fractures, Joints and Their Geophysical Signature](../04-structural-geology/04-fractures-joints.md)
  — fracturing in the bedrock beneath the till sheet.
- [10-01 GPR Principles](../../10-gpr-near-surface/01-gpr-principles/README.md)
  — the method behind the ice and sand-and-gravel examples.
- [10-03-02 GPR Glaciology](../../10-gpr-near-surface/03-gpr-applications/02-gpr-glaciology.md)
  — radar on ice in practice.

Exercises:
[`exercises/02-glacial-landforms-exercises.md`](./exercises/02-glacial-landforms-exercises.md)
and
[`exercises/02-glacial-landforms-solutions.md`](./exercises/02-glacial-landforms-solutions.md).

## Self-assessment checklist

- [ ] I can define mass balance and the equilibrium-line altitude, and say how
      each is measured. (§1)
- [ ] I can compute a driving stress from thickness and slope. (§2)
- [ ] I can write Glen's flow law and the integrated deformation velocity, and
      state the temperature dependence of $A$. (§2)
- [ ] I can explain why thickness matters through the fourth power and
      temperature only linearly in the stress-dominated regime. (§6)
- [ ] I can estimate a thickness from a slope with the perfect-plasticity model
      and say why it is wrong in detail. (§2, §7)
- [ ] I can list the erosional landforms and the depositional landforms with
      their sediments. (§3, §4)
- [ ] I can name the property contrast that makes sediment-over-bedrock visible
      to P-wave reflection, and the one that makes the water table visible. (§4)
- [ ] I can compute an Airy depression and a viscous relaxation time. (§6)
- [ ] I can compute a Stefan active-layer depth and state its assumptions. (§5, §7)
- [ ] I can say why radar rather than seismic reflection images an ice bed. (§8)
