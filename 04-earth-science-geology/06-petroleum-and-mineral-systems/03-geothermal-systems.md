---
id: 04-06-03
title: "Geothermal Systems, Heat Flow and Resource Assessment"
level: advanced
prereqs: ["02-05-06", "04-01-05", "04-06-01"]
estimated_minutes: 75
tags: [geothermal, heat-flow, conduction, convection, rayleigh, magnetotellurics, skin-depth, resource-assessment]
---

# Geothermal Systems, Heat Flow and Resource Assessment

A geothermal system is a **petroleum system with heat instead of hydrocarbon**,
and the analogy is exact enough to be useful: a heat source in place of a source
rock, a permeable reservoir, a fluid that carries the energy, and a
low-permeability caprock that stops it escaping. The differences are equally
instructive. The "resource" is not a substance that can be assayed but a
**continuous flux** through a volume of rock; the temperature that matters is
measured in a borehole rather than inferred from a maturity model; and the
quantity that a resource estimate depends on most — the recovery factor — is an
engineering parameter with a large uncertainty, not a physical constant.

This lesson develops the physics that a geothermal assessment rests on:
Fourier's law for conduction, the Rayleigh criterion for the onset of convection,
the magnetotelluric (MT) response that actually locates a geothermal field, and
the heat-in-place arithmetic that marks the boundary between physics and
engineering.

## Learning objectives

By the end of this lesson you will be able to:

1. **Name** the five elements of a geothermal system and the play types they
   describe.
2. **Compute** a conductive heat flow from a gradient and a conductivity, and a
   temperature profile that includes a radiogenic source term.
3. **Compute** the Rayleigh number for a saturated porous layer and decide, using
   the critical value $4\pi^{2}$, whether convection is expected.
4. **Compute** a magnetotelluric skin depth and the apparent resistivity of a
   layered section, and explain why apparent resistivity is not a true
   resistivity.
5. **Explain** why a conductive clay cap over a resistive reservoir is the
   standard geothermal exploration target, and which property MT measures.
6. **Compute** the heat in place in a rock volume and state precisely where the
   physics ends and the engineering begins.
7. **Compute** the temperature excess that an anomalous heat flow produces at a
   given depth, and describe the observation that it would take to detect it.
8. **State** the assumptions of each calculation and the conditions under which
   it fails.

## Prerequisites

- [02-05-06 Geotherms, Heat Flow and the Earth's Thermal Budget](../../02-physics/05-thermodynamics/06-geotherms.md)
  — the conduction equation and the definition of heat flow.
- [04-01-05 Density, Porosity, Permeability and Elastic Properties](../01-earth-structure/05-rock-physics-basics.md)
  — porosity and permeability, which set the convective possibility.
- [04-06-01 Source, Reservoir, Seal and Trap: The Petroleum System](./01-petroleum-system.md)
  — the system framework this lesson mirrors.

---

## 1. The geothermal system, and the play types

| Element | Role | Observable |
|---|---|---|
| Heat source | Elevated flux: a young intrusion, an extended crust, or a thick radiogenic crust | Heat flow, geotherm |
| Reservoir | Permeable rock carrying the fluid | Permeability; from structure, fracture mapping and well tests |
| Fluid | The carrier of energy | Temperature, salinity, chemistry |
| Caprock | Low-permeability layer preventing convective escape | Clay alteration, low resistivity |
| Recharge | Supply of water to sustain the system | Hydrology, isotope chemistry |

Four play types are usually distinguished:

1. **Volcanic / magmatic.** A young intrusion supplies heat at shallow depth.
   High temperature, high gradient, and a strong clay-cap MT signature.
2. **Sedimentary basin.** A deep permeable aquifer in a basin with a normal or
   slightly elevated gradient. Lower temperature, but large volumes and long
   production histories.
3. **Fault- and fracture-controlled.** Permeability is structural; the system is
   a few hundred metres wide and kilometres long, so it is a *structure* target
   as much as a conductivity target.
4. **Engineered (enhanced) systems.** The rock is hot but tight; permeability is
   created by stimulation. Here geophysics supplies the stress state, the
   temperature and the microseismic monitoring, and the permeability is
   manufactured rather than found.

## 2. Conduction: Fourier's law and the geotherm

In steady state with no convection and no source,

$$
q = -k\frac{\mathrm{d}T}{\mathrm{d}z},
$$

with $q$ the heat flux [W m⁻²] and $k$ the thermal conductivity [W m⁻¹ K⁻¹].
Solving for the profile gives $T(z) = T_0 + qz/k$, and adding a distributed
radiogenic source $A$ [W m⁻³] gives

$$
T(z) = T_0 + \frac{q_0 z}{k} + \frac{A z^{2}}{2k}.
$$

The quadratic source term is why a heat-producing granite is warmer at depth than
a simple linear gradient predicts: 2 $\mu$W m⁻³ adds 10 K at 5 km, which is
large against the resolution of most thermal models.

**Units.** $q$ is conventionally reported in mW m⁻²; $k$ in W m⁻¹ K⁻¹; the
gradient in K km⁻¹. The product $k \times (\text{K km}^{-1}) \times 10^{-3}$ is
mW m⁻², and the factor of $10^{3}$ is the commonest arithmetic error.

## 3. Convection: the Rayleigh criterion

A permeable layer with a temperature contrast across it becomes unstable to
convection above a critical Rayleigh number. For a saturated porous layer the
Rayleigh number is

$$
\mathrm{Ra} = \frac{k_\mathrm{perm}\,\rho_w^{2} c_p\, g\,\alpha\,\Delta T\,H}
{\mu\,\lambda},
$$

with $k_\mathrm{perm}$ the permeability [m²], $\alpha$ the thermal expansion
coefficient [K⁻¹], $\Delta T$ the temperature contrast, $H$ the layer thickness,
$\mu$ the dynamic viscosity and $\lambda$ the saturated thermal conductivity.
The critical value for a horizontal layer with impermeable isothermal boundaries
is

$$
\mathrm{Ra}_c = 4\pi^{2} \approx 39.5 .
$$

**Physical reasoning.** Ra is proportional to the product $H\,\Delta T$, so a
thin layer with a large contrast and a thick layer with a small one are not
equivalent: what sets the instability is the product, together with the
permeability and viscosity, which both enter to the first power and both vary by
orders of magnitude in real rock. This is why a real field cannot be classified
as "convective" or "conductive" from first principles, and why drilling the
temperature profile is still the decisive measurement.

The practical significance is large. Convection is a much more efficient heat
transport mechanism than conduction, so a convective system has an almost
isothermal reservoir and a **steep gradient in the caprock** above it. A measured
temperature log that is nearly straight is a conductive system; one with a sharp
break is a convective reservoir under a cap.

## 4. Heat flow measurement, in one paragraph

A heat flow is the product of two measured fields: a **temperature gradient**,
from a temperature log or a series of measurements in a borehole, and a
**thermal conductivity**, from a divided-bar or needle-probe measurement on cores
or from a borehole conductivity log. Both are local and both vary with
lithology, so a heat-flow map is the product of two noisy fields. Two corrections
dominate: **topography and palaeoclimate** (the transient of
[04-05-04](../05-geomorphology-and-quaternary/04-quaternary-climate.md) §6), and
**advection** by groundwater, which is not a correction but a change of regime.

## 5. The magnetotelluric signature, and why it is the workhorse

Geothermal exploration is not primarily a temperature-measuring exercise; it is a
**conductivity**-measuring one. The reason is alteration: hot fluid reacting with
rock converts feldspars and volcanic glass into clay, and clay is conductive by
several orders of magnitude relative to fresh rock. The result is a layered
section in which the **clay cap is conductive and the hot reservoir below is
relatively resistive**, and that contrast is what MT measures.

**Skin depth.** For a uniform half-space of resistivity $\rho$ [Ω m] and a period
$T$ [s],

$$
\delta = \sqrt{\frac{2\rho}{\omega\mu_0}} \approx 503\sqrt{\rho T}\ \text{m}.
$$

Sounding depth is therefore **set by the period**, which is why an MT site is a
depth profile rather than a single number.

**Apparent resistivity.** The measured response is converted into an apparent
resistivity using the Cagniard relation
$\rho_a = |Z|^{2}/(\omega\mu_0)$, which is exact only for a uniform half-space.
Over a layered earth it is a *weighted average* of the resistivities within the
sounding depth, and it is not the resistivity of any particular layer. Reading
$\rho_a$ as a true resistivity is a standard and expensive error.

**What MT does *not* measure.** Temperature. A conductive clay cap indicates
alteration and therefore past fluid flow; the temperature comes from a measured
gradient, from geology, and from the exhumation and heat-flow history.

## 6. Resource assessment: where the physics stops

The **heat in place** in a rock volume $V$ with temperature excess $\Delta T$ is

$$
Q = \rho\,c\,V\,\Delta T,
$$

which is a physical quantity: given a volume, a density, a heat capacity and a
temperature contrast, $Q$ follows. For 1 km³ of rock with
$\rho c = 2.43\times10^{6}$ J m⁻³ K⁻¹ and $\Delta T = 100$ K this is
$2.43\times10^{17}$ J $= 243$ PJ.

What follows is **not** physics:

$$
Q_{\text{recoverable}} = R\,Q,
\qquad
P = \dot m\,c\,\Delta T,
$$

where $R$ is a recovery factor and $\dot m$ a mass flow rate. Both depend on
permeability, well pattern, reinjection temperature, project lifetime, drilling
cost, energy price and regulation. The correct treatment — and the one this
lesson and its demo adopt — is to **state the physical quantity, leave the
engineering factors symbolic, and show how the answer depends on them**:
$\partial Q/\partial R = Q$, so a factor of two in $R$ is a factor of two in the
result, and no additional geophysics removes that dependence.

This is the same discipline that
[lesson 05](./05-unconventional-resources.md) applies to recovery factors in
unconventional hydrocarbon plays, and it exists for the same reason: a reserve is
a legal and economic category, not a measurement.

## 7. Assumptions and regime of validity

**Conduction.**

1. Steady state. A system still equilibrating after a magmatic intrusion, or one
   perturbed by erosion or a palaeoclimate transient, is not steady.
2. One-dimensional heat flow. Topography, lateral conductivity contrasts and
   dipping structure all break it.
3. No advection. Groundwater flow changes the equation, not just the answer.
4. Constant $k$ and $A$. Both vary with lithology; $A$ varies with the
   radiogenic element content mapped in module 02-09.

**Convection.**

1. The Rayleigh criterion assumes a homogeneous, isotropic permeable layer with
   impermeable boundaries and small perturbations. A fractured reservoir is
   anisotropic, often fault-bounded, and not a layer.
2. Permeability and viscosity are the two least-known inputs and both enter
   linearly.
3. Above the onset, Ra says that convection occurs but not how strongly; that
   needs a Nusselt-number relation, which is another parameterisation.

**Magnetotellurics.**

1. The Cagniard relation assumes a plane wave and a one-dimensional earth.
   Three-dimensional structure, topography and cultural noise all distort it.
2. Static shift from near-surface inhomogeneity offsets the whole curve by a
   constant factor and is not removed by 1-D modelling.
3. The method measures conductivity, which is only *indirectly* related to
   temperature.

## 8. Quantitative treatment with units

| Quantity | Symbol | Unit | Value used here (MODELLED) |
|---|---|---|---|
| Thermal conductivity | $k$ | W m⁻¹ K⁻¹ | 2.5 |
| Geothermal gradient | – | K m⁻¹ | $25\times10^{-3}$ |
| Heat production | $A$ | W m⁻³ | $2\times10^{-6}$ |
| Permeability | $k_\mathrm{perm}$ | m² | $10^{-14}$ |
| Thermal expansion of water | $\alpha$ | K⁻¹ | $5\times10^{-4}$ |
| Viscosity of water at 130 °C | $\mu$ | Pa s | $2.5\times10^{-4}$ |
| Bulk density × heat capacity | $\rho c$ | J m⁻³ K⁻¹ | $2.43\times10^{6}$ |

**Worked check 1.** $q = k\,\mathrm{d}T/\mathrm{d}z = 2.5 \times 25\times10^{-3}
= 62.5$ mW m⁻², the order of magnitude of continental heat flow.

**Worked check 2.** With $H = 1000$ m and $\Delta T = 100$ K,

$$
\mathrm{Ra} = \frac{(10^{-14})(10^{3})^{2}(4186)(9.81)(5\times10^{-4})(100)(10^{3})}
{(2.5\times10^{-4})(2.0)} = 41.1,
$$

which is $1.04\,\mathrm{Ra}_c$: marginally convective. The demo's point is not
that this is the answer for a particular field, but that a *plausible* set of
inputs lands within a few per cent of critical — so the regime is genuinely
ambiguous and must be measured, not asserted.

## 9. Python demonstration

[`code/geothermal_systems_demo.py`](./code/geothermal_systems_demo.py) computes
heat flow and geotherms with a source term, the Rayleigh number against the
Horton–Rogers–Lapwood criterion, the heat in place with the engineering factors
kept symbolic, the MT skin depth and the Cagniard apparent resistivity of layered
sections, and the temperature excess of an anomalous heat flow.

```text
   conductivity (W/m/K)   gradient (K/km)   q (mW/m^2)
                   2.5              25.0       62.50
       1.0                35.0              35.4       0.40
       5.0               135.0             145.0      10.00
      500        50       10.27      0.260   conductive
     1000       100       41.06      1.040   convecting
    V =    1.0 km^3, dT =   100 K: Q = 2.430e+17 J = 243.000 PJ
    m_dot =    50 kg/s, dT =   100 K: P =    20.9 MW_th
                   5.0       1125.4       3558.8      11254.0
       0.01                      100.00                        5.00                        5.00
     100.00                      100.00                      220.82                       38.93
   10000.00                      100.00                      457.94                       48.75
     0.5                  2.00                  6.00                 12.00
```

### What to observe

- Sixty-two and a half milliwatts per square metre from $2.5$ W m⁻¹ K⁻¹ at
  25 K km⁻¹: the arithmetic is trivial and the difficulty is entirely in
  measuring both factors.
- The radiogenic source term adds $0.40$ K at 1 km and $10.0$ K at 5 km. A
  quadratic term that is negligible at shallow depth and dominant at the base of
  a heat-flow section is exactly the kind of error that a linear model conceals.
- The Rayleigh number crosses $\mathrm{Ra}_c$ between the 500 m/50 K case
  ($\mathrm{Ra}/\mathrm{Ra}_c = 0.26$) and the 1000 m/100 K case ($1.04$). The
  regime is decided by the *product* $H\Delta T$, and it is decided marginally.
- The MT table verifies the recursion: a 100 Ω m half-space returns exactly
  100.00 Ω m at every period. The 500 m clay cap over 500 Ω m reads 5.00 Ω m at
  0.01 s, 11.16 Ω m at 1 s and 220.82 Ω m at 100 s, and is still climbing at
  10 000 s (457.94 Ω m). **That is the practical content of the method**: the
  period range needed to see the reservoir, and the fact that an intermediate
  period reports neither the cap nor the reservoir.
- A 30 mW m⁻² anomaly at 1 km produces 12 K. That is the honest detection
  statement: not an instrument specification, but a comparison between the
  temperature step the target produces and the uncertainty of the thermal model
  used to interpret it.

## 10. Common mistakes

1. **Forgetting the $10^{3}$ in mW m⁻².** A units slip of a factor of 1000 in a
   heat-flow map looks like a real anomaly.
2. **Treating a heat-flow map as a measurement.** It is a product of two measured
   fields, each with its own uncertainty.
3. **Applying a conduction solution where groundwater flows.** Advection is a
   different regime, not a correction.
4. **Ignoring the palaeoclimate transient.** A several-per-cent systematic bias
   with a spatial pattern (see
   [04-05-04](../05-geomorphology-and-quaternary/04-quaternary-climate.md) §6).
5. **Asserting a convective or conductive regime from Ra alone.** The inputs are
   too uncertain, and the answer is often marginal.
6. **Reading an apparent resistivity as a true resistivity.** Over a layered
   earth it is a weighted average, and the error can exceed a factor of ten.
7. **Ignoring static shift in MT.** It offsets the whole curve and survives 1-D
   inversion.
8. **Treating the clay cap as the reservoir.** The cap is the *seal and the
   alteration halo*; the reservoir is the resistive zone beneath it.
9. **Quoting a recovery factor or a capacity as if it were a resource.** One is
   an engineering assumption and the other an economic statement.
10. **Assuming that a temperature log needs no model.** The inference from
   measured temperature to heat flow requires a conductivity profile and a
   surface-history assumption.

## 11. Real-world applications

- **Geothermal exploration.** MT and gravity for structure and alteration,
  microseismics for fracture permeability, and a temperature gradient hole for the
  decisive measurement
  ([11-04-01 Geothermal Signatures](../../11-exploration-geophysics/04-geothermal-exploration-geophysics/01-geothermal-signatures.md)).
- **Heat-flow mapping.** Continental and oceanic heat-flow datasets constrain
  tectonics and the thermal state of the lithosphere
  ([12 Global Geophysics and the Earth's Interior](../../12-global-geophysics-interior/README.md)).
- **Direct-use and district heating.** Lower-temperature resources in sedimentary
  basins, where the reservoir is an aquifer and the assessment is a
  hydrogeological one ([04-06-04 Aquifer Types and Groundwater Occurrence](./04-groundwater-aquifers.md)).
- **Enhanced (engineered) geothermal systems.** Where permeability is created:
  the geophysical problem becomes the stress state, the induced microseismicity
  and the time-lapse monitoring of the created volume
  ([10-06 Near-Surface Monitoring](../../10-gpr-near-surface/06-nearsurface-monitoring/README.md)).
- **Borehole palaeoclimatology.** The same conduction equation run in reverse to
  recover a surface-temperature history
  ([04-05-04](../05-geomorphology-and-quaternary/04-quaternary-climate.md)).
- **Basin thermal history.** Heat flow and conductivity through the basin fill as
  the boundary condition for the maturation models of
  [lesson 01](./01-petroleum-system.md).
- **Hydrothermal mineral systems.** The same fluid-and-heat engine that makes a
  geothermal field makes an epithermal deposit
  ([lesson 02](./02-mineral-deposits.md)).

## 12. Further reading

- **Beardsmore, G. R., & Cull, J. P. *Crustal Heat Flow: A Guide to Measurement
  and Modelling* (Cambridge).** The measurement of both factors in §4. Level:
  graduate.
- **Turcotte, D. L., & Schubert, G. *Geodynamics* (Cambridge).** Conduction,
  convection and the Rayleigh criterion in the same notation as §2 and §3.
  Level: graduate textbook.
- **Nield, D. A., & Bejan, A. *Convection in Porous Media* (Springer).** The
  Horton–Rogers–Lapwood problem, the critical Rayleigh number and the
  Nusselt-number relations beyond it. Level: graduate.
- **Simpson, F., & Bahr, K. *Practical Magnetotellurics* (Cambridge).** The MT
  response, static shift and 3-D effects. Level: graduate.
- **Chave, A. D., & Jones, A. G. (eds) *The Magnetotelluric Method: Theory and
  Practice* (Cambridge).** The definitive reference for §5. Level: reference.
- **Rybach, L., & Muffler, L. J. P. (eds) *Geothermal Systems: Principles and
  Case Histories* (Wiley).** The play-type classification of §1. Level:
  professional.
- **Muffler, P., & Cataldi, R. (1978). Methods for regional assessment of
  geothermal resources.** *Geothermics*. The origin of the heat-in-place
  approach of §6, and of the recovery-factor discussion. Level: advanced.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 13. Related lessons

- [01 Source, Reservoir, Seal and Trap: The Petroleum System](./01-petroleum-system.md)
  — the same system logic, and where the basin thermal history is used.
- [02 Mineral Deposit Types and Their Geophysical Signatures](./02-mineral-deposits.md)
  — alteration mineralogy, which is what makes the clay cap.
- [04 Aquifer Types and Groundwater Occurrence](./04-groundwater-aquifers.md)
  — the fluid flow, without which there is no convective system.
- [05 Unconventional Resources: Shale, Tight Gas, Hydrates](./05-unconventional-resources.md)
  — where the same caution about recovery factors is applied.
- [02-05-06 Geotherms, Heat Flow and the Earth's Thermal Budget](../../02-physics/05-thermodynamics/06-geotherms.md)
  — the physics this lesson applies.
- [04-05-04 Quaternary Climate Change and Landscape Records](../05-geomorphology-and-quaternary/04-quaternary-climate.md)
  — the thermal transient that is a signal in one application and a bias in the
  other.
- [05-09 Geothermal and Heat-Flow Methods](../../05-core-geophysics/09-geothermal-and-heat-flow-methods/README.md)
  — the measurement side, in method form.

Exercises:
[`exercises/03-geothermal-systems-exercises.md`](./exercises/03-geothermal-systems-exercises.md)
and
[`exercises/03-geothermal-systems-solutions.md`](./exercises/03-geothermal-systems-solutions.md).

## Self-assessment checklist

- [ ] I can name the five elements of a geothermal system and four play types.
      (§1)
- [ ] I can compute a heat flow from a gradient and a conductivity, with the
      units right. (§2)
- [ ] I can compute a temperature profile with a radiogenic source term and say
      where the quadratic term matters. (§2, §9)
- [ ] I can write the porous-media Rayleigh number and compare it with
      $4\pi^{2}$. (§3)
- [ ] I can explain why the convective and conductive cases have different
      temperature-log shapes. (§3)
- [ ] I can compute an MT skin depth for a given resistivity and period. (§5)
- [ ] I can compute a layered apparent resistivity and explain why it is not a
      true resistivity. (§5, §9)
- [ ] I can explain why a clay cap is conductive and why it is the exploration
      target. (§5)
- [ ] I can compute the heat in place and state where the engineering begins.
      (§6)
- [ ] I can state four assumptions of the conduction model and three of the MT
      interpretation. (§7)
