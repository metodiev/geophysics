---
id: 02-05-01
title: "Temperature, Heat, Internal Energy and Specific Heat"
level: beginner
prereqs: ["02-01-01", "02-01-04"]
estimated_minutes: 90
tags: [temperature, heat-capacity, latent-heat, magma]
---

# Temperature, Heat, Internal Energy and Specific Heat

Three words are used interchangeably in ordinary speech and must be separated
before any thermodynamics can be done. **Temperature** is a property of a body
at an instant: it says how fast its atoms are jostling and it is *intensive*—two
litres of water at 20 °C have the same temperature as one litre. **Internal
energy** is the total microscopic energy the body contains: it is *extensive*, so
two litres at 20 °C hold twice as much as one. **Heat** is not a property of a
body at all; it is energy *in transit* because of a temperature difference, and a
body that is not exchanging energy has no heat, only internal energy.

Getting this wrong is not pedantry. The reason a magma body can sit at
1200 °C for millennia while a cup of coffee at 80 °C is undrinkable in minutes is
that the two differ by a factor of 10¹⁴ in *internal energy*, not by 1100 °C in
temperature.

## Learning objectives

By the end of this lesson you will be able to:

1. **Distinguish** temperature, internal energy and heat, and classify each as
   intensive or extensive.
2. **Compute** the heat content of a rock volume from its volumetric heat
   capacity $\rho c_p$, and compare it with water and air.
3. **Explain** why $c_p \approx c_v$ for crystalline rock and when the
   difference matters, using $c_p - c_v = \alpha^2 T K_T/\rho$.
4. **Estimate** the specific heat of a mineral from the Dulong–Petit
   high-temperature limit, and state when that limit fails.
5. **Separate** sensible from latent heat, and compute the latent fraction for a
   crystallising magma and the total energy content of a magma body.
6. **Convert** between stored energy and the power or time required to move it.

## Prerequisites

- [02-01-01 Physical Quantities, SI Units and Dimensional Homogeneity](../01-measurement-and-physical-reasoning/01-physical-quantities.md)
  — the unit conventions used throughout.
- [02-01-04 Conservation Laws as the Engine of Physical Modelling](../01-measurement-and-physical-reasoning/04-conservation-laws.md)
  — why energy accounting works at all.

## 1. The three quantities, defined

### 1.1 Temperature

Temperature is the state variable that decides the direction of heat flow between
two bodies in contact: energy goes from the higher temperature to the lower.
Thermodynamically it is defined by

$$\frac{1}{T} = \left(\frac{\partial S}{\partial U}\right)_{V,N} ,$$

where $S$ is entropy and $U$ internal energy. That definition is the subject of
lesson [03](./03-second-law.md); for now the operational meaning is what a
thermometer measures. Temperature is intensive and has no additive property: it
makes no sense to add the temperatures of two samples.

### 1.2 Internal energy

Internal energy is the sum of the kinetic energy of the atoms' thermal motion
and the potential energy of their interactions. For a solid at moderate
temperature the only mode that matters is lattice vibration; for a gas there is
also translation and rotation; for a melt there is also configurational
disorder. Internal energy is extensive and is defined only up to an additive
constant, because only *changes* are measurable.

### 1.3 Heat

Heat is energy transferred across a boundary because of a temperature
difference. It is a verb wearing a noun's clothes. Two consequences:

- There is no such thing as "the heat in a body", only its internal energy.
- Heat is one of two ways to change internal energy; the other is work. The
  relation between the three is the first law, lesson [02](./02-first-law.md).

## 2. How much energy a rock stores

### 2.1 Volumetric heat capacity

For a substance whose volume is held fixed, the energy needed to raise its
temperature by $\Delta T$ is

$$Q = m c_v \Delta T = \rho V c_v \Delta T , \tag{1}$$

and if the pressure is held fixed instead, $c_p$ replaces $c_v$. For a rock, the
two are nearly equal (§3.2), so the working formula is

$$Q = \rho\, c_p\, V\, \Delta T . \tag{2}$$

The product

$$C_V \equiv \rho c_p \qquad [\mathrm{J\,m^{-3}\,K^{-1}}] \tag{3}$$

is the **volumetric heat capacity**: the energy stored per cubic metre per
kelvin. This, not $\rho$ and not $c_p$ separately, is what controls every
transient thermal problem in the solid Earth, because heat is stored in volume
and, as lesson [04](./04-heat-conduction.md) shows, it enters the diffusion
equation as the ratio $\kappa = k/(\rho c_p)$.

### 2.2 The numbers

Nominal values (representative of the class of material, not measurements of any
sample; see the [constant handbook](../../26-reference-library/02-symbols-and-units/03-constant-handbook.md)):

| Material | $\rho$ (kg m⁻³) | $c_p$ (J kg⁻¹ K⁻¹) | $\rho c_p$ (J m⁻³ K⁻¹) |
|---|---|---|---|
| Granite | 2700 | 790 | 2.133 × 10⁶ |
| Basalt | 2900 | 840 | 2.436 × 10⁶ |
| Mantle rock | 3300 | 1250 | 4.125 × 10⁶ |
| Water | 1000 | 4186 | 4.186 × 10⁶ |
| Air (sea level) | 1.2 | 1005 | 1.23 × 10³ |
| Iron | 7870 | 450 | 3.542 × 10⁶ |

Three observations follow immediately, and each has a geophysical consequence.

1. **Water stores about twice as much heat per cubic metre as granite** (4.186
   against 2.133 MJ m⁻³ K⁻¹). This is why a water-filled aquifer is a far better
   thermal buffer than dry rock, and why porous rock's heat capacity must be
   computed with a mixture rule rather than from the mineral grain.
2. **Air stores 1700 times less per cubic metre than rock.** The atmosphere is
   thermally thin; it changes temperature readily and cannot damp anything. Any
   statement about "the atmosphere storing heat" refers to the ocean, not the air.
3. **All rocks fall within a factor of two of each other.** The mineralogy that
   changes seismic velocity by 40 per cent changes heat capacity by 20 per cent.
   Conductivity is the more variable thermal property, and it is covered in
   lesson [04](./04-heat-conduction.md).

### 2.3 Per unit of energy, in units people use

One cubic metre of granite warmed by 1 K takes 2.133 × 10⁶ J = 0.593 kWh. One
cubic kilometre (10⁹ m³) warmed by 1 K takes 2.133 × 10¹⁵ J. Because that is
still an awkward number, work out the *time*: at a geothermal extraction rate of
10 MW, cooling 1 km³ of rock by 100 K releases 2.133 × 10¹⁷ J, which lasts
6.8 × 10² years. Every enhanced-geothermal scheme is ultimately a calculation of
this kind, with the uncertainty living in how fast the heat can be replenished by
conduction from the surrounding rock.

## 3. Derivations

### 3.1 Why $c_p$ and $c_v$ differ, and by how much

For any substance,

$$c_p - c_v = \frac{\alpha^2 T K_T}{\rho} , \tag{4}$$

where $\alpha = (1/V)(\partial V/\partial T)_p$ is the volumetric thermal
expansion coefficient and $K_T$ is the isothermal bulk modulus. Equation (4) is
a standard thermodynamic identity; it can be derived from the definition of
enthalpy and the Maxwell relations, and it is worth understanding rather than
memorising because it explains the pattern:

- For **solids**, $\alpha$ is small (10⁻⁵ to 10⁻⁴ K⁻¹), so $c_p - c_v$ is a small
  fraction of $c_p$: 0.04 per cent for granite at 300 K, 4.5 per cent for mantle
  rock at 1600 K. Rock physics uses $c_p$ throughout without apology.
- For **water**, $\alpha$ is large near 4 °C (where it passes through zero) and
  the difference is per-cent-level.
- For an **ideal gas**, $\alpha = 1/T$ exactly, so $c_p - c_v = K_T/\rho = R/M$:
  the difference is tens of per cent, which is why the atmosphere cannot ignore
  it ([16-01](../../16-atmosphere-climate/01-atmospheric-structure-and-thermodynamics/README.md)).

**Regime of validity.** Equation (4) is exact for a homogeneous single-phase
material in local equilibrium. It fails for a two-phase mixture, where a
"pressure change" can also change the phase fractions, and for a material whose
relaxation time is comparable to the timescale of the measurement — notably
water near 4 °C and any material near a phase transition.

### 3.2 Why rock specific heat is about 800–1250 J kg⁻¹ K⁻¹

The **Dulong–Petit law** states that in the high-temperature limit the molar
heat capacity of a solid is $3nR$ per mole, where $n$ is the number of atoms per
formula unit and $R$ is the molar gas constant (exact: 8.314 462 618… J mol⁻¹ K⁻¹
from $N_A k_B$). Dividing by molar mass gives the specific heat:

| Mineral | $n$ | $M$ (g mol⁻¹) | $3nR$ (J mol⁻¹ K⁻¹) | $c_v$ (J kg⁻¹ K⁻¹) |
|---|---|---|---|---|
| Periclase MgO | 2 | 40.30 | 49.89 | 1238 |
| Bridgmanite MgSiO₃ | 5 | 100.39 | 124.72 | 1242 |
| Quartz SiO₂ | 3 | 60.08 | 74.83 | 1245 |

Every silicate lands within one per cent of 1240 J kg⁻¹ K⁻¹, because the limit
is $3R$ per *atom* and almost all rock-forming oxides carry about 20 g of mass
per atom. The nominal mantle value of ~1250 J kg⁻¹ K⁻¹ is therefore a
theoretical result, not a coincidence.

**Regime of validity, and why the crustal number is lower.** Dulong–Petit is the
*high-temperature* limit. It is reached only well above the Debye temperature of
each vibrational mode, which for most minerals is 300–500 K. A room-temperature
measurement of granite gives ~790 J kg⁻¹ K⁻¹, below the limit, because not all
modes are excited. At low temperature $c$ falls towards zero as $T^3$. So:
mantle heat capacities are classical and predictable; crustal and cryospheric
ones are not.

### 3.3 Sensible and latent heat

Cooling a body from $T_1$ to $T_2$ releases **sensible** heat
$\rho c_p (T_1 - T_2)$. Crystallising it releases **latent** heat $\rho L$, where
$L$ is the latent heat of fusion, at essentially constant temperature. For
basalt with $L \approx 4\times10^5$ J kg⁻¹ (nominal; $L$ for silicates is
poorly known and varies with composition and pressure):

$$Q_{\text{sensible}} = 2900 \times 840 \times 1200 = 2.92\times10^9\
\text{J m}^{-3}, \qquad
Q_{\text{latent}} = 2900 \times 4\times10^5 = 1.16\times10^9\
\text{J m}^{-3}. \tag{5}$$

The latent heat is **28.4 per cent** of the total released between 1500 K and
300 K. Two consequences:

- The cooling curve of a magma body has a pronounced plateau. If crystallisation
  spans ~150 K, the heat released per kelvin of cooling *inside* the interval is
  $1.16\times10^9/150 = 7.7\times10^6$ J m⁻³ K⁻¹, a factor of **3.2** more than
  the sensible rate of $2.4\times10^6$ J m⁻³ K⁻¹ outside it. The body stalls.
- Any thermal model of a magma chamber that omits latent heat will overestimate
  the cooling rate during crystallisation by a factor of several, which
  translates into a wrong solidification time.

### 3.4 The energy content of a magma body

A 1 km³ body (10⁹ m³) cooling from 1500 K to 300 K releases

$$E = (2.92\times10^9 + 1.16\times10^9)\times10^9 = 4.08\times10^{18}\ \text{J}.
\tag{6}$$

Since 1 kW-year $= 1000 \times 3.155\,76\times10^7 = 3.1558\times10^{10}$ J,
this is $1.29\times10^8$ kW-years $= 129$ GW-years.

**Read that as energy, not power.** 129 GW-years delivered over 10 000 years is
13 MW. The *power* of a magma body is not a property of the magma; it is a
property of the path the heat takes to get out, which is lesson
[04](./04-heat-conduction.md). This distinction between stored energy and
delivered power is the single most common source of confusion in geothermal
assessments.

## 4. Physical interpretation

**Heat capacity is the price of a temperature change.** Every thermal calculation
in geophysics is a struggle between an energy source and this price. Rock is
expensive to heat: 2 MJ m⁻³ K⁻¹, so warming the top 100 m of the crust by 1 K
takes 2.1 × 10¹¹ J per km².

**Water is the expensive one.** Its high volumetric heat capacity, arising from
hydrogen bonding rather than density, makes liquid water the best thermal ballast
on the planet's surface. This is why the ocean moderates climate on
multi-decadal to millennial timescales and why the solid Earth cannot.

**Latent heat is the flat part of every thermal history.** Phase changes put a
large energy step at a nearly fixed temperature. The plateau in a cooling magma,
the flat segment in a borehole temperature profile crossing the permafrost base,
and the long pause in a numerical phase-change model are the same physics.

**Air is thermally irrelevant as a reservoir but decisive as a transport
medium.** Its volumetric heat capacity is 1700 times smaller than rock's, yet
atmospheric motion redistributes enormous energy because it moves fast. Capacity
and flux are different things, and this module is largely about keeping them
apart.

## 5. Assumptions and regime of validity

| Approximation | Statement | What breaks outside it |
|---|---|---|
| Constant $c_p$ over the temperature range | $Q = \rho c_p V \Delta T$ | Over hundreds of kelvin in a real rock, $c_p$ rises by 10–20 per cent; integrate instead |
| $c_p \approx c_v$ | Equation (4) gives a small difference | Gases, and any material near a phase transition or a $\lambda$ anomaly |
| Additivity of mixture heat capacities | $\rho c_p$ of a porous rock is the porosity-weighted average of the two phases | Fails when latent heat of pore-fluid vaporisation, or chemical reaction, is involved |
| Local thermal equilibrium | One temperature describes the rock and its pore fluid at every instant | Fails at high heating rate or low permeability; see the Gassmann-style frequency argument in lesson 02-04-04 |
| Latent heat released at a single temperature | The plateau is sharp | Real magmas crystallise over an interval and release $L$ along a liquidus-to-solidus path |
| Nominal values for real rocks | Order-of-magnitude estimates | A measurement of a specific rock can differ by ±30 per cent in $c_p$ and by a factor of 3 in $k$ |

## 6. Units and dimensional analysis

- $Q$: J. $c_p$: J kg⁻¹ K⁻¹. $\rho$: kg m⁻³. $\rho c_p$: J m⁻³ K⁻¹. Check
  equation (2): $\mathrm{kg\,m^{-3}}\cdot\mathrm{J\,kg^{-1}\,K^{-1}}\cdot
  \mathrm{m^3}\cdot\mathrm{K} = \mathrm{J}$ ✓.
- $\alpha$: K⁻¹. $K_T$: Pa = J m⁻³. Then $\alpha^2 T K_T/\rho$:
  $\mathrm{K^{-2}}\cdot\mathrm{K}\cdot\mathrm{J\,m^{-3}}\cdot\mathrm{m^3\,kg^{-1}}
  = \mathrm{J\,kg^{-1}\,K^{-1}}$ ✓, the same units as $c_p$. The identity (4) is
  dimensionally consistent, which is a genuine check because it is easy to
  misremember as $\alpha^2 T K_T$ per mole.
- $L$: J kg⁻¹, so $\rho L$: J m⁻³ ✓, the same as $\rho c_p \Delta T$.
- **A useful anchor**: any rock is within a factor of two of 2.5 MJ m⁻³ K⁻¹.
  If a thermal estimate comes out with a rock's volumetric heat capacity of
  10⁵ or 10⁸ J m⁻³ K⁻¹, the error is dimensional, not geological.

## 7. Python demonstration

[`code/temperature_heat_demo.py`](./code/temperature_heat_demo.py) tabulates
volumetric heat capacities, separates sensible from latent heat, computes the
energy content of a 1 km³ magma body, evaluates $c_p - c_v$ from equation (4),
and computes the Dulong–Petit limit for three minerals. Observed output:

```text
material        rho (kg/m3)  c_p (J/kg/K)   rho*c_p (J/m3/K)
granite              2700.0         790.0         2.1330e+06
basalt               2900.0         840.0         2.4360e+06
mantle rock          3300.0        1250.0         4.1250e+06
water                1000.0        4186.0         4.1860e+06
air                     1.2        1005.0         1.2311e+03
iron                 7870.0         450.0         3.5415e+06

  1 m^3 of granite warmed by 1 K takes 2.1330e+06 J = 0.5925 kWh
  1 km^3 of granite (1e9 m^3) warmed by 1 K takes 2.1330e+15 J
```

```text
  sensible heat  rho c_p delta T = 2.9232e+09 J per m^3
  latent heat    rho L           = 1.1600e+09 J per m^3 (L = 4.000e+05 J/kg, nominal)
  total                          = 4.0832e+09 J per m^3
  latent fraction of the total   = 0.2841
```

```text
  energy released cooling 1500 K -> 300 K = 4.0832e+18 J
  1 kW-year = 1000 W x 3.15576e+07 s = 3.1558e+10 J
  so the body's heat equals 1.2939e+08 kW-years,
  i.e. 129.39 GW-years,
```

```text
material         T (K)   alpha^2 T K_T/rho         c_p   (c_p-c_v)/c_p
granite            300              0.2844       790.0       3.601e-04
mantle rock       1600             56.7273      1250.0       4.538e-02
iron               300              0.9332       450.0       2.074e-03
water              300             26.4000      4186.0       6.307e-03
```

```text
mineral                 n   M (g/mol)   3nR (J/mol/K)   c_v (J/kg/K)
periclase MgO           2     40.3040          49.887         1237.8
bridgmanite MgSiO3      5    100.3875         124.717         1242.4
quartz SiO2             3     60.0835          74.830         1245.4
```

### What to observe

| Observation | Consequence |
|---|---|
| Water's $\rho c_p$ is 1.96× granite's | Pore fluid, not mineralogy, controls the heat capacity of a saturated rock |
| Air's $\rho c_p$ is 5.8 × 10⁻⁴ of granite's | The atmosphere is a transport medium, not a reservoir |
| Granite's $(c_p-c_v)/c_p$ is 3.6 × 10⁻⁴ | Rock physics uses $c_p$; the difference is negligible at crustal temperature |
| Mantle rock's is 4.5 × 10⁻² | At mantle temperature the difference reaches a few per cent and must be kept in precise adiabat calculations |
| Latent fraction 0.2841 | Nearly a third of a magma's heat is released at constant temperature |
| Every mineral gives ~1240 J kg⁻¹ K⁻¹ | Dulong–Petit is a real theory, not a table |

> **Breaking exercise.** Set `LATENT_FUSION["basalt"]` to 2.0e5 (the lower end of
> the plausible range) and predict, before running, the new latent fraction and
> the new plateau factor. Then explain why an uncertainty on $L$ of a factor of
> two changes the solidification *time* of a magma body by far less than a factor
> of two.

## 8. Common mistakes

1. **Saying "the heat of the rock".** Rock has internal energy. Heat is a
   transfer. The error is not just semantic: it leads people to add a heat flux
   to an energy content.
2. **Using $c_p$ in kg⁻¹ units with a volume.** $Q = \rho c_p V \Delta T$ has
   three factors on the right; omitting $\rho$ underestimates the energy of a
   rock volume by 2700.
3. **Comparing water and rock by specific heat instead of by volumetric heat
   capacity.** Water's $c_p$ is 5.3× granite's but its $\rho c_p$ is only 2×,
   because water is less dense. The volumetric quantity is the one that matters
   for storage.
4. **Forgetting the latent heat.** Omitting it underestimates a magma's heat
   release by 28 per cent and its time at temperature by far more.
5. **Confusing energy with power.** "This magma body contains 129 GW-years" is
   not a statement about 129 GW. Divide by the duration to get power.
6. **Extrapolating Dulong–Petit to low temperature.** It is the high-temperature
   limit; near 0 K the heat capacity goes to zero.
7. **Treating a nominal value as a measurement.** The conductivity of "granite"
   spans 2–4 W m⁻¹ K⁻¹; a thermal model built on the midpoint has an uncertainty
   that must be carried.
8. **Adding temperatures.** Averaging temperatures across a two-phase system
   without weighting by heat capacity, or summing °C values, gives nonsense.
   Weight by $\rho c_p V$.

## 9. Real-world applications

- **Geothermal energy assessment.** The recoverable energy of a reservoir is
  $\rho c_p V \Delta T$ times a recovery factor, and the *power* is that divided
  by the extraction lifetime. Both must be quoted
  ([05-09](../../05-core-geophysics/09-geothermal-and-heat-flow-methods/README.md)).
- **Magma chamber thermal evolution.** Stored heat, latent heat and the
  latent-heat plateau set the duration of hydrothermal activity, contact
  metamorphism and ore-forming fluid circulation around an intrusion
  ([13-06](../../13-geodynamics-tectonics/06-crustal-and-lithospheric-dynamics/README.md)).
- **Seasonal thermal energy storage.** Aquifer thermal storage exploits the high
  volumetric heat capacity of water and the much larger capacity of the
  saturated rock it fills.
- **Borehole palaeoclimate.** The relevant rock property is again $\rho c_p$,
  entering through $\kappa = k/(\rho c_p)$ (lesson [04](./04-heat-conduction.md)).
- **Cryosphere.** The latent heat of fusion of ice (3.34 × 10⁵ J kg⁻¹, nominal)
  is why melting a glacier takes as much energy as warming it by 80 K, and why
  ice sheets are effective climate buffers.
- **Volcanic hazard.** The thermal energy budget of a magma body, not its
  temperature, determines how long it can drive an eruption or a hydrothermal
  system.

## 10. Further reading

- **Callen, H. B. *Thermodynamics and an Introduction to Thermostatistics*
  (2nd ed., Wiley).** The cleanest treatment of the state-variable versus
  process distinction and of equation (4). Level: beginner to advanced.
- **Fermi, E. *Thermodynamics* (Dover reprint).** A short, rigorous classic;
  Chapter 1 derives the first law from the same care about definitions used here.
  Level: beginner.
- **Turcotte, D. L., & Schubert, G. *Geodynamics* (3rd ed., Cambridge University
  Press, 2014).** Chapters on heat transfer, including the latent-heat treatment
  used in §3.3. Level: intermediate to graduate.
- **Incropera, F. P., & DeWitt, D. P. *Fundamentals of Heat and Mass Transfer*
  (Wiley).** The engineering reference for heat capacity, latent heat and
  combined transport. Level: intermediate.
- **Philpotts, A. R., & Ague, J. J. *Principles of Igneous and Metamorphic
  Petrology* (2nd ed., Cambridge University Press, 2009).** Magma thermal
  budgets, crystallisation intervals and why real cooling curves are not flat.
  Level: intermediate.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 11. Related lessons

- [02 First Law, Work and Energy Balances](./02-first-law.md) — what happens to
  the energy once stored.
- [04 Heat Conduction, Fourier's Law and Thermal Diffusivity](./04-heat-conduction.md)
  — how $\rho c_p$ enters the diffusion equation, and how fast stored heat moves.
- [02-01-03 Scaling Laws, Similarity and Dimensional Reasoning](../01-measurement-and-physical-reasoning/03-scaling-laws.md)
  — the dimensional discipline used throughout.
- [02-11-04 Atmospheric Structure, Hydrostatic Balance and Lapse Rates](../11-physics-of-earths-interior-and-atmosphere/04-atmospheric-structure.md)
  — where $c_p$ and $c_v$ must be kept apart.
- [05-core-geophysics/09 Geothermal and Heat-Flow Methods](../../05-core-geophysics/09-geothermal-and-heat-flow-methods/README.md)
  — the applied version of this lesson.

Exercises:
[`exercises/01-temperature-and-heat-exercises.md`](./exercises/01-temperature-and-heat-exercises.md)
and
[`exercises/01-temperature-and-heat-solutions.md`](./exercises/01-temperature-and-heat-solutions.md).

## Self-assessment checklist

- [ ] I can state which of temperature, internal energy and heat is intensive and
      which is extensive, and why heat is not a property of a body. (§1)
- [ ] I can compute the heat content of a rock volume and convert it into kWh or
      GW-years. (§2.3)
- [ ] I can explain why water stores twice as much heat per cubic metre as
      granite while air stores 1700 times less. (§2.2, §4)
- [ ] I can write and use $c_p - c_v = \alpha^2 T K_T/\rho$, and say when the
      difference matters. (§3.1)
- [ ] I can derive the specific heat of a silicate from Dulong–Petit and state
      the limit's regime of validity. (§3.2)
- [ ] I can compute the sensible and latent heat of a magma and the plateau
      factor they imply. (§3.3)
- [ ] I can compute the stored energy of a magma body and explain why that is not
      a power. (§3.4)
- [ ] I can state at least three approximations of this lesson with their regimes
      and what breaks outside them. (§5)
