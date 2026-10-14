---
id: 04-06-01
title: "Source, Reservoir, Seal and Trap: The Petroleum System"
level: intermediate
prereqs: ["04-03-04", "04-01-05", "02-05-06"]
estimated_minutes: 75
tags: [petroleum-system, source-rock, maturation, reservoir, seal, trap, bright-spot]
---

# Source, Reservoir, Seal and Trap: The Petroleum System

A petroleum accumulation is not a rock type; it is a **system** in which five
elements must coincide in space and in time: a **source rock** rich enough in
organic matter to generate hydrocarbons, a **migration pathway**, a **reservoir**
with both porosity and permeability, a **seal** with a capillary entry pressure
high enough to hold the buoyant column, and a **trap** — a geometric closure in
which the hydrocarbon can collect. Remove any one of the five and there is no
accumulation, however favourable the others.

The word *system* is doing real work here. It means that the interesting
questions are about **timing and coincidence**: did generation start after the
trap formed, and did the seal survive the burial that followed? It also means
that the geophysical contribution is not a search for "oil" but a measurement of
each element separately — because no geophysical method detects hydrocarbons
directly at depth. What is measured is a *property contrast* associated with an
element: a temperature (source maturity), a density and velocity (reservoir), a
resistivity (fluid type), an impedance contrast (geometry and, indirectly, fluid).

## Learning objectives

By the end of this lesson you will be able to:

1. **Name and distinguish** the five elements of a petroleum system, and state
   what makes each one adequate rather than merely present.
2. **Explain** why the "oil window" is a temperature interval and why its depth
   therefore moves with the geothermal gradient.
3. **Compute** a first-order Arrhenius conversion and explain why the temperature
   at which a given conversion is reached depends on the **heating rate**.
4. **Compute** porosity, bulk density and vertical effective stress with depth
   from a compaction law, and explain why effective stress rather than depth is
   the physical variable behind velocity trends.
5. **Compute** the buoyant column height a seal can support from a capillary
   entry pressure, and state which input dominates the uncertainty.
6. **Compute** acoustic impedances and reflection coefficients for a shale over a
   brine sand and over a gas sand, and explain why the gas case is larger.
7. **State** which physical property carries the signature of each element, and
   therefore which method could see it.

## Prerequisites

- [04-03-04 Sedimentary Basins: Formation, Fill and Subsidence](../03-geologic-time-and-stratigraphy/04-sedimentary-basins.md)
  — the subsidence history that drives maturation, and the geometry that makes a
  trap.
- [04-01-05 Density, Porosity, Permeability and Elastic Properties](../01-earth-structure/05-rock-physics-basics.md)
  — the porosity–density–velocity relations used throughout.
- [02-05-06 Geotherms, Heat Flow and the Earth's Thermal Budget](../../02-physics/05-thermodynamics/06-geotherms.md)
  — the geothermal gradient, which converts the maturity window into a depth.

---

## 1. The five elements, and what "adequate" means

| Element | What it must provide | Quantified by |
|---|---|---|
| Source rock | Enough organic carbon, of the right type, heated into the generation window | TOC and its kinetics; temperature history |
| Migration | A pathway from source to trap | Permeability and the buoyancy pressure available |
| Reservoir | Porosity for storage **and** permeability for flow | $\phi$, $k$, and their geometry |
| Seal | A capillary entry pressure exceeding the buoyant pressure of the column | Pore-throat radius and interfacial tension |
| Trap | A closed geometric container | Closure geometry, from seismic and structure |
| **Timing** | Generation *after* the trap and seal existed | Burial history against trap formation |

The last row is not a sixth element; it is the constraint that makes the other
five a *system*. A perfect trap that filled before the seal was breached is
empty. This is why a petroleum system is always presented as a **time–event
chart** (mapped onto the time axis of the basin), and why the chart is an
interpretation, not a measurement.

## 2. Source rock and maturation

Organic matter (kerogen) converts to liquid and gaseous hydrocarbons over a
temperature interval that is conventionally divided into a **window** — roughly
$60$ to $120\ ^\circ$C for liquid hydrocarbons in the widely used convention,
with wet gas above it and dry gas higher still. The numbers are conventions, and
the mechanism is a set of parallel chemical reactions with a *distribution* of
activation energies, because kerogen is a mixture rather than a compound.

The simplest quantitative model is a first-order reaction with an Arrhenius rate
constant

$$
k(T) = A\exp\!\left(-\frac{E_a}{RT}\right),
\qquad
\frac{\mathrm{d}C}{\mathrm{d}t} = k(T)\,(1 - C),
$$

where $C$ is the conversion, $A$ the pre-exponential factor [s⁻¹] and $E_a$ the
activation energy [J mol⁻¹]. Because $E_a$ is large (of order $2\times10^{5}$
J mol⁻¹), $k$ changes by orders of magnitude over a few tens of kelvin, which is
the entire reason the window is narrow.

**Physical reasoning.** Heating a source rock is not like crossing a threshold; it
is like charging a capacitor whose leakage rate depends exponentially on
temperature. A rock that sits at $100\ ^\circ$C for a million years may convert
more than one that passes through $120\ ^\circ$C for ten thousand. That is why a
**burial history** and not a present-day depth is the quantity a basin model
predicts, and why the depth of the window moves with the gradient:

| Gradient | Top of window ($60\ ^\circ$C) | Base ($120\ ^\circ$C) |
|---|---|---|
| $20$ K km⁻¹ | 2.5 km | 5.5 km |
| $25$ K km⁻¹ | 2.0 km | 4.4 km |
| $40$ K km⁻¹ | 1.25 km | 2.75 km |

## 3. Migration and buoyancy

Hydrocarbons are less dense than water, so once a continuous hydrocarbon phase
exists it migrates **upward** under buoyancy: the driving pressure difference per
unit height is $\Delta\rho\, g$, with $\Delta\rho$ the density difference between
water and the hydrocarbon (of order $10^{2}$ kg m⁻³ for oil and $8\times10^{2}$
kg m⁻³ for gas at reservoir conditions).

Migration occurs along carriers — a permeable bed, a fault, an unconformity — and
stops where the buoyancy pressure can no longer overcome the capillary resistance
of the pore throats. That is the same balance that governs the seal (§5), so
migration and sealing are one physics seen at two scales.

## 4. Reservoir: compaction, density and effective stress

The porosity of a mudstone or sandstone decreases with burial, and a
widely used description is **Athy's law**,

$$
\phi(z) = \phi_0 \exp\!\left(-\frac{z}{c}\right),
$$

with $\phi_0$ the surface porosity and $c$ a length scale [m]. The bulk density
follows from a two-phase mixture, $\rho = \phi\rho_\mathrm{w}
+ (1-\phi)\rho_\mathrm{grain}$, and the vertical stress from integrating that
density. The quantity that actually controls compaction, velocity and pore
geometry is the **vertical effective stress**

$$
\sigma_v' = \sigma_v - p_\mathrm{pore},
$$

which is why a velocity–depth trend in an area of overpressure is wrong by tens of
per cent if it is calibrated on normally pressured wells: the same depth carries a
different effective stress.

**The fluid effect.** Replacing brine with gas in a reservoir changes the bulk
modulus much more than the density, so the P-wave velocity falls sharply while the
S-wave velocity barely changes. The acoustic impedance therefore falls, and the
top of a gas sand becomes a large, negative reflection coefficient — a *bright
spot*. Lesson [05](./05-unconventional-resources.md) derives this with Gassmann's
equation, and the demo here computes only the impedance consequence.

## 5. Seal and trap: the capillary entry pressure

A seal holds a hydrocarbon column by capillary resistance. The pressure needed to
force a non-wetting phase through a pore throat of radius $r$ is

$$
P_c = \frac{2\sigma\cos\theta}{r},
$$

with $\sigma$ the interfacial tension [N m⁻¹] and $\theta$ the contact angle. The
**column height** that this supports against buoyancy is

$$
h_{\max} = \frac{P_c}{\Delta\rho\, g}.
$$

Two consequences, both quantitatively important:

- $h_{\max} \propto 1/r$: the seal's capacity is a **pore-scale** property, so it
  is never a single number for a formation and is properly reported as a
  distribution.
- $h_{\max} \propto 1/\Delta\rho$: the same seal holds a much shorter *gas*
  column than *oil* column.

**Trap geometry** is the part that seismic data addresses directly: a
four-way dip closure, a fault-bounded block, a stratigraphic pinch-out or an
unconformity trap are all geometric objects, and their closure is measured in
time and converted to depth with a velocity model — which is a model, and is the
dominant uncertainty in the volume of the container.

## 6. The geophysical signature of each element

This is the bridge to folder 11. No method sees hydrocarbons; each sees a
property, and each element has its own.

| Element | Physical property that differs | Method that responds |
|---|---|---|
| Source rock | Radioactivity (uranium in organic-rich shale), resistivity, density | Gamma-ray spectrometry, resistivity logs, seismic inversion |
| Maturity | Temperature; and from it, a modelled density/velocity trend | Heat-flow and temperature data; basin modelling |
| Migration pathway | Porosity and permeability: resistivity, velocity, anisotropy | Seismic attributes, EM, well logging |
| Reservoir | Porosity, density, velocity, resistivity | Seismic reflection and inversion, EM, logs |
| Fluid type | P-wave velocity and density (impedance), resistivity | Seismic amplitude/Vp/Vs, CSEM, resistivity logs |
| Seal | High density, high velocity, high clay content, low resistivity | Seismic reflection, EM, logs |
| Trap geometry | Acoustic impedance contrasts at boundaries | Seismic reflection, gravity for large-scale structure |
| Overburden and hazards | Density, velocity, shallow gas | Shallow seismic, GPR, gravimetry |

Three cautions on that table, all of them the same caution:

1. An impedance anomaly is a **fluid-and-rock** effect, not a hydrocarbon
   indicator. A low-saturation "fizz" gas and a fully gas-charged sand can look
   similar in P-wave data (see
   [lesson 05](./05-unconventional-resources.md) §1).
2. Resistivity distinguishes brine from hydrocarbon, but only in a rock whose
   porosity and clay content are known; that knowledge comes from logs.
3. Gravity and magnetics contribute **structure** — the geometry of the trap and
   the depth of the basement — not fluids.

## 7. Assumptions and regime of validity

**Maturation.**

1. A single first-order reaction with one activation energy is a
   **parameterisation**. Real kinetic schemes use a distribution; the absolute
   temperatures differ, and the qualitative behaviour (strong temperature
   dependence, heating-rate dependence) does not.
2. The temperature history is a **model output** from a basin model calibrated
   against vitrinite reflectance, apatite fission tracks or well temperatures.
   Any "maturity" statement inherits that model's assumptions about
   palaeo-heat-flow and palaeo-surface temperature.
3. The window boundaries (60–120 °C) are conventions, not phase boundaries.

**Compaction and stress.**

1. Athy's law is empirical and exponential in form; it fits many mudstones and
   is not a mechanical law.
2. Hydrostatic pore pressure is assumed in the effective-stress calculation.
   Overpressure, which is common, changes the answer substantially.
3. Grain density is assumed constant with depth; mineralogical change during
   burial violates it.

**Seal and trap.**

1. $P_c = 2\sigma\cos\theta/r$ assumes a single cylindrical throat radius, a
   single interfacial tension and a constant contact angle. All three vary.
2. Column height computed this way is a *capacity*, not a prediction: it says
   what the seal could hold, not how much hydrocarbon is present.
3. Time is neglected: a seal can leak over geological time by diffusion and by
   episodic failure.

## 8. Quantitative treatment with units

| Quantity | Symbol | Unit | Value used here (MODELLED) |
|---|---|---|---|
| Surface temperature | $T_0$ | °C | 10 |
| Geothermal gradient | $G$ | K m⁻¹ | $25\times10^{-3}$ |
| Activation energy | $E_a$ | J mol⁻¹ | $2.0\times10^{5}$ |
| Pre-exponential factor | $A$ | s⁻¹ | $10^{13}$ |
| Surface porosity | $\phi_0$ | – | 0.50 |
| Athy length scale | $c$ | m | 2000 |
| Grain and water density | $\rho_g$, $\rho_w$ | kg m⁻³ | 2650, 1030 |
| Interfacial tension | $\sigma$ | N m⁻¹ | 0.030 (gas–water) |
| Pore-throat radius | $r$ | m | $0.20\times10^{-6}$ |
| Hydrocarbon density | $\rho_\mathrm{hc}$ | kg m⁻³ | 200 (gas), 800 (oil) |

**Worked check (seal).** $P_c = 2(0.030)/(0.20\times10^{-6}) = 3.0\times10^{5}$ Pa.
For gas, $\Delta\rho = 1030 - 200 = 830$ kg m⁻³, so
$h_{\max} = 3.0\times10^{5}/(830 \times 9.81) = 36.8$ m. For oil,
$\Delta\rho = 230$ kg m⁻³ and $h_{\max} = 110.8$ m. The same seal holds three
times the oil column it holds of gas, entirely through the density difference.

## 9. Python demonstration

[`code/petroleum_system_demo.py`](./code/petroleum_system_demo.py) computes the
geotherm and the window depths, the Arrhenius conversion isothermally and along
heating paths, the compaction and effective-stress profiles with the time–depth
conversion, the seal capacity for gas and oil, the acoustic impedances and
reflection coefficients, and the organic-carbon mass of a source rock.

```text
    z =  2.0 km: T =    60.0 degC
    z =  4.0 km: T =   110.0 degC
      60.0 degC ->  2.000 km
     120.0 degC ->  4.400 km
         100   1.009e-15   3.308e+06
         120   2.680e-14   1.246e+05
    beta (K/Myr)   T at 10 per cent (degC)
             1.0                97.1
            30.0               116.9
      500   0.3894        2019.2            9.49          4.44
     4000   0.0677        2540.4           90.34         49.92
    z =  4.0 km: v =   6300 m/s, one-way  1.196 s, TWT  2.392 s
    gas: d_rho =    830 kg/m^3, P_c = 3.000e+05 Pa, h_max =    36.84 m
    oil: d_rho =    230 kg/m^3, P_c = 2.500e+05 Pa, h_max =   110.80 m
    shale over brine sandstone : R = -0.0153
    shale over gas sandstone   : R = -0.1326
  COMPUTED amplitude ratio gas sand / brine sand = 8.66
       100 km^2 x    50 m at phi = 0.143: m_C = 4.836e+11 kg = 0.484 Gt
```

### What to observe

- The isothermal conversion time to 10 per cent falls from $3.3\times10^{6}$ yr at
  100 °C to $1.2\times10^{5}$ yr at 120 °C — a factor of 27 for 20 K. That is the
  reason a small change in the thermal history can change the prospect.
- The heating-rate table is the most important single result: a source heated at
  1 K per million years reaches 10 per cent conversion at 97 °C, and one heated at
  30 K per million years needs 117 °C. **The "temperature of generation" is not a
  property of the kerogen alone.**
- Bulk density rises from 1019 to 2540 kg m⁻³ between 500 m and 4 km, so the
  velocity trend that a time–depth conversion needs is not a straight line: the
  same 4 km is 2.392 s two-way at the modelled trend.
- The gas-sand reflection is 8.66 times the brine-sand one, and both are
  negative. Amplitude *and* polarity matter, and the ratio is the diagnostic.
- The organic-carbon calculation stops at the mass of carbon. The fraction
  converted, expelled and recovered are three separate questions; the demo states
  no number for any of them.

## 10. Common mistakes

1. **Treating the oil window as a fixed depth.** It is a temperature interval;
   its depth is the gradient inverted.
2. **Reading a present-day temperature as a maturity.** Conversion is a
   time–temperature integral, so a present-day temperature without a history says
   little.
3. **Assuming hydrostatic pore pressure** in an effective-stress calculation.
   Overpressure is common and changes the answer materially.
4. **Quoting a seal as a single number.** It is a distribution of pore-throat
   radii and therefore of capacities.
5. **Reading a bright spot as a hydrocarbon indicator.** It is an impedance
   anomaly; fizz gas, a tight streak and a tuning effect all produce them.
6. **Forgetting polarity.** The top of a gas sand is a trough, not a peak, and a
   display convention can invert the sign of the interpretation.
7. **Equating a structural closure with a trap.** A closure without a seal is a
   geometry, not a trap.
8. **Ignoring timing.** The chart of generation against trap formation is the
   system, and it is an interpretation.
9. **Treating a time map as a depth map.** Time-to-depth conversion is a model
   step, and it is where the largest volumetric error usually enters.
10. **Quoting a resource or recovery figure as if it were a measurement.** Those
    are engineering and economic quantities, and no such number appears in this
    lesson.

## 11. Real-world applications

- **Basin and play assessment.** The five-element framework is the standard
  structure of an exploration evaluation, and the event chart is its output.
- **Seismic interpretation for structure and fluid.** Reflection imaging of the
  trap and amplitude analysis for fluid, with the caveats of §6
  ([11-03-01 Seismic in Exploration](../../11-exploration-geophysics/03-hydrocarbon-exploration/01-seismic-in-exploration.md)).
- **Reservoir characterisation.** Porosity, saturation and net-to-gross from a
  combination of seismic inversion and well logs
  ([11-03-03 Reservoir Characterisation](../../11-exploration-geophysics/03-hydrocarbon-exploration/03-reservoir-characterisation.md)).
- **Borehole measurement.** Resistivity, density, neutron and sonic logs are what
  convert a geophysical anomaly into a rock with fluids
  ([05-08 Geophysical Logging](../../05-core-geophysics/08-geophysical-logging/README.md)).
- **Basin modelling.** The thermal and burial history that maturation depends on,
  calibrated against measured maturity indicators.
- **Geohazards and drilling safety.** Shallow gas, overpressure and weak seals are
  the same physics viewed from the drilling side
  ([11-06-01 Site Investigation](../../11-exploration-geophysics/06-geotechnical-and-engineering/01-site-investigation.md)).
- **Carbon storage.** The same five elements in reverse: a reservoir, a seal, a
  trap, and a monitoring problem in which time-lapse geophysics is the measurement
  ([10-06 Near-Surface Monitoring](../../10-gpr-near-surface/06-nearsurface-monitoring/README.md)).

## 12. Further reading

- **Magoon, L. B., & Dow, W. G. (eds) *The Petroleum System — From Source to
  Trap* (AAPG Memoir).** The origin of the system framework of §1. Level:
  professional reference.
- **Tissot, B. P., & Welte, D. H. *Petroleum Formation and Occurrence*
  (Springer).** The kinetics and the geochemistry of §2. Level: graduate.
- **Allen, P. A., & Allen, J. R. *Basin Analysis: Principles and Application to
  Petroleum Play Assessment* (Wiley).** Subsidence, thermal history and play
  assessment in one framework. Level: graduate textbook.
- **Batzle, M., & Wang, Z. (1992). Seismic properties of pore fluids.**
  *Geophysics*. The fluid properties behind any fluid-substitution calculation.
  Level: advanced.
- **Avseth, P., Mukerji, T., & Mavko, G. *Quantitative Seismic Interpretation*
  (Cambridge).** Rock physics, amplitude analysis and the fizz-gas problem.
  Level: graduate.
- **Mavko, G., Mukerji, T., & Dvorkin, J. *The Rock Physics Handbook*
  (Cambridge).** The relations, with their ranges and their assumptions. Level:
  reference.
- **Sclater, J. G., & Christie, P. A. F. (1980). Continental stretching.**
  *Journal of Geophysical Research*. The subsidence model that underlies most
  burial histories. Level: advanced.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 13. Related lessons

- [02 Mineral Deposit Types and Their Geophysical Signatures](./02-mineral-deposits.md)
  — the same property-contrast logic applied to metalliferous systems.
- [03 Geothermal Systems, Heat Flow and Resource Assessment](./03-geothermal-systems.md)
  — the thermal side of the same basin.
- [04 Aquifer Types and Groundwater Occurrence](./04-groundwater-aquifers.md)
  — the fluid-flow physics in the shallow subsurface, where it is measurable.
- [05 Unconventional Resources: Shale, Tight Gas, Hydrates](./05-unconventional-resources.md)
  — where the reservoir is also the source.
- [04-03-04 Sedimentary Basins](../03-geologic-time-and-stratigraphy/04-sedimentary-basins.md)
  — the geometry and subsidence that make a play.
- [04-05-03 Fluvial, Coastal and Aeolian Systems](../05-geomorphology-and-quaternary/03-fluvial-coastal.md)
  — the depositional architecture that becomes reservoir heterogeneity.
- [05-04 Rock Physics and Property Relations](../../05-core-geophysics/04-rock-physics/README.md)
  — porosity, density, velocity and fluid substitution in full.

Exercises:
[`exercises/01-petroleum-system-exercises.md`](./exercises/01-petroleum-system-exercises.md)
and
[`exercises/01-petroleum-system-solutions.md`](./exercises/01-petroleum-system-solutions.md).

## Self-assessment checklist

- [ ] I can name the five elements and say what "adequate" means for each. (§1)
- [ ] I can explain why the window is a temperature interval and compute its
      depth from a gradient. (§2, §8)
- [ ] I can write the Arrhenius rate law and explain the heating-rate effect.
      (§2, §9)
- [ ] I can compute a porosity, density and effective-stress profile. (§4)
- [ ] I can compute a capillary entry pressure and the column height it
      supports, for gas and for oil. (§5, §8)
- [ ] I can compute reflection coefficients for a shale over a brine sand and
      over a gas sand and explain the difference. (§4, §9)
- [ ] I can state which property carries each element's signature and which
      method responds. (§6)
- [ ] I can state four assumptions of a maturation model and four of a seal
      calculation. (§7)
- [ ] I can explain why an amplitude anomaly is not a hydrocarbon indicator.
      (§6, §10)
