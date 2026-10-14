---
id: 04-06-04
title: "Aquifer Types and Groundwater Occurrence"
level: intermediate
prereqs: ["04-01-05", "04-05-03"]
estimated_minutes: 75
tags: [aquifer, groundwater, darcy, transmissivity, storativity, theis, archie, crim, saline-intrusion]
---

# Aquifer Types and Groundwater Occurrence

An aquifer is a rock that both stores and transmits water. Those are two
different properties, and the distinction is the whole subject: a clay has high
porosity and no permeability, so it stores water and yields none; a fractured
granite has almost no porosity and a high permeability along its fractures, so it
yields water from a void fraction of a per cent. The **aquifer type** is a
statement about which of the two properties is present and how it is organised in
space — and that organisation is what geophysics maps.

This lesson covers the four families (porous, fractured, karstic, and the
transitional case of a layered alluvial system), the two storage regimes
(confined and unconfined), the well hydraulics that a pumping test measures, the
recharge estimation that a water balance needs, and — the geophysical core — the
**property contrasts** by which each is detected.

## Learning objectives

By the end of this lesson you will be able to:

1. **Distinguish** an aquifer from an aquitard and an aquiclude in terms of porosity
   and permeability, and give an example of a rock that is one without the other.
2. **Classify** aquifers as porous, fractured or karstic, and as confined or
   unconfined, and say which classification decides the response to pumping.
3. **Apply** Darcy's law and compute a transmissivity from a conductivity and a
   saturated thickness.
4. **Distinguish** specific storage from specific yield and compute both, and
   explain why the same transmissivity can give very different responses.
5. **Compute** a Theis drawdown, a specific capacity and a radius of influence,
   and state the convention each depends on.
6. **Estimate** recharge from water-table fluctuation and state why it is a
   consistency check rather than a measurement.
7. **Compute** a formation factor from Archie's law and an effective permittivity
   from CRIM, and explain which physical property each geophysical method is
   actually measuring.
8. **Explain** why a saline intrusion is the easiest groundwater target and a
   fractured granite the hardest.

## Prerequisites

- [04-01-05 Density, Porosity, Permeability and Elastic Properties](../01-earth-structure/05-rock-physics-basics.md)
  — porosity, permeability and the density relations used throughout.
- [04-05-03 Fluvial, Coastal and Aeolian Systems](../05-geomorphology-and-quaternary/03-fluvial-coastal.md)
  — the depositional architecture that determines aquifer connectivity.

---

## 1. Aquifer types

| Type | Storage | Conduction | Yield character |
|---|---|---|---|
| Porous (intergranular) | Pore volume | Pore throats | High and predictable; large volumes |
| Fractured | Fracture volume (small) | Fracture network | Variable; found by intersection |
| Karstic | Conduits and cavities | Conduits | Very high but extremely local |
| Layered alluvial | Interbedded aquifers and aquitards | Channel sands | Governed by connectivity, not total sand |

The classification that matters for the *response to pumping* is:

- **Unconfined (water-table) aquifer.** The water surface is the water table, at
  atmospheric pressure. Pumping lowers the water table and the water released
  comes from **drainage of pores** — the specific yield.
- **Confined (artesian) aquifer.** The aquifer is bounded above by an aquitard and
  the water is under pressure. Pumping does not dewater the rock; it reduces the
  pressure and the water released comes from **compression of the rock and
  expansion of the water** — the specific storage.
- **Leaky and perched** are the intermediate cases, and most real aquifers are one
  of them.

## 2. Darcy's law, conductivity and transmissivity

The fundamental relation is Darcy's law, in the form used in hydrogeology:

$$
Q = K\,i\,A,
$$

with $Q$ the volumetric flow rate [m³ s⁻¹], $K$ the **hydraulic conductivity**
[m s⁻¹], $i$ the hydraulic gradient (dimensionless) and $A$ the cross-sectional
area [m²]. The **transmissivity** is the depth-integrated conductivity,

$$
T = K\,b,
$$

with $b$ the saturated thickness [m], giving $T$ in m² s⁻¹ (or, in practice,
m² day⁻¹).

**Physical reasoning.** $K$ is not a property of the fluid alone nor of the rock
alone; it combines both, through the permeability $k$ [m²]:
$K = k\rho_w g/\mu$. A rock therefore has *different* hydraulic conductivities for
water at 10 °C and at 100 °C, and by a factor of two or more. This is one reason a
geothermal reservoir and a cold aquifer of identical rock behave differently, and
it is a common source of confusion when comparing a geology paper with a
hydrogeology paper.

**The magnitude range is enormous.** Gravel to clay spans five orders of
magnitude in $K$, and the same factor appears in the yield. This is why the
question "how much water?" cannot be answered by mapping geometry alone: it needs
a pumping test, and geophysics supplies the geometry that makes the pumping test
interpretable.

## 3. Storage: two different mechanisms

**Confined aquifer.** The specific storage is

$$
S_s = \rho_w g\left(\alpha + \phi\beta\right),
$$

with $\alpha$ the compressibility of the solid matrix [Pa⁻¹] and $\beta$ the
compressibility of water [Pa⁻¹], and the dimensionless storativity is
$S = S_s b$. With $\alpha = 10^{-10}$ Pa⁻¹, $\beta = 4.4\times10^{-10}$ Pa⁻¹ and
$\phi = 0.2$, $S_s = 1.84\times10^{-6}$ m⁻¹, so a 50 m aquifer has
$S = 9.2\times10^{-5}$ — of order $10^{-4}$.

**Unconfined aquifer.** The water released per unit area per unit head change is
the **specific yield** $S_y$, which is the drainable porosity: 0.15–0.25 for
sand and gravel, 0.05 for silt, 0.02 for clay. The ratio $S_y/S$ for a 50 m
confined aquifer is of order $10^{3}$ — a thousand-fold difference in the water
released by one metre of head change.

**Consequence.** Two aquifers with identical transmissivity respond completely
differently to a drought: the unconfined one drains and its water table falls,
the confined one depressurises with almost no change in stored volume. Any
water-balance statement must say which regime it refers to.

## 4. Well hydraulics

For a confined aquifer pumped at a constant rate $Q$ from a fully penetrating
well, the **Theis solution** gives the drawdown

$$
s(r,t) = \frac{Q}{4\pi T}\,W(u),
\qquad
u = \frac{r^{2}S}{4Tt},
$$

where $W(u) = E_1(u)$ is the exponential integral (equivalently, the "well
function"). Its limiting behaviour is worth memorising:

- For small $u$ (late time or near the well), $W(u) \approx -\gamma - \ln u$,
  where $\gamma = 0.5772$ is the Euler–Mascheroni constant, so the drawdown grows
  **logarithmically** with time and decreases logarithmically with radius.
- The **specific capacity** $Q/s$ is what a pumping test reports; it depends on
  $T$, $S$, the well radius and the pumping duration, and is therefore not a pure
  aquifer property.
- The **radius of influence** is not a physical boundary. It is the radius at
  which the drawdown falls below whatever threshold the analyst chooses, and it
  must be quoted with that convention. Reporting it without one is the standard
  error.

## 5. Recharge from water-table fluctuation

For an unconfined aquifer with no pumping, inflow or evapotranspiration during the
period of rise, the recharge is

$$
R = S_y\,\frac{\Delta h}{\Delta t},
$$

with $\Delta h$ the water-table rise over the interval. The answer is **linear in
$S_y$**, which is estimated from grain size or from a pumping test, so a factor of
two in $S_y$ is a factor of two in the recharge. The method is therefore a
consistency check on a water balance rather than an independent measurement, and
it fails completely where the water table is pumped, drained by a river or sealed
by a paved surface.

## 6. The geophysical signature of an aquifer

This is the section that connects the hydrogeology to the measurement. No method
sees "water"; each sees a property that the water changes.

| Property | How water changes it | Method |
|---|---|---|
| Electrical resistivity | Pore fluid conductivity dominates: brine lowers it, fresh water raises it | ERT, electromagnetic induction, TEM |
| Dielectric permittivity | Water has $\varepsilon_r \approx 81$, air 1, minerals 4–6 | GPR |
| Density | Saturation and porosity change bulk density | Microgravity, borehole gravimetry |
| P-wave velocity | Saturating a dry sediment raises $v_P$ sharply at the water table | Seismic refraction and reflection |
| Shear modulus | Stiffness of the skeleton, not the fluid | Surface-wave and downhole seismic |
| Nuclear magnetic resonance | Directly sensitive to pore water and to pore size | Surface and borehole NMR |
| Natural gamma | Clay content, not water | Gamma logging |

**The two quantitative relations used most.**

*Archie's law.* The formation factor is $F = a/\phi^{m}$ and the saturated rock
resistivity is $\rho_0 = F\rho_w$, with a partial-saturation form
$\rho_t = \rho_0/S_w^{n}$. All three exponents ($a$, $m$, $n$) are **empirically
fitted** and lithology-dependent, and converting $\rho_w$ to a salinity or a total
dissolved solids is a *further* empirical step.

*CRIM.* The complex refractive index model for the effective permittivity,

$$
\sqrt{\varepsilon_\mathrm{eff}} = \theta\sqrt{\varepsilon_w}
+ (1-\phi)\sqrt{\varepsilon_s} + (\phi-\theta)\sqrt{\varepsilon_a},
$$

is a **derived** mixing model with declared end-member permittivities, and it
gives a radar velocity $v = c/\sqrt{\varepsilon_\mathrm{eff}}$. Because water has
$\varepsilon_r \approx 81$ and air 1, the water table is one of the strongest radar
reflectors in the shallow subsurface.

**Saline intrusion.** Where seawater meets fresh groundwater, the pore-fluid
conductivity changes by two to three orders of magnitude over a transition zone.
That is the largest contrast in the list and it is in the *fluid*, so it is
essentially independent of the rock: a saline wedge is detectable by EM and ERT
almost anywhere, which is why it is the easiest groundwater target in the table.

**Fractured rock.** The hardest. The target is a void fraction of order 1 per
cent, distributed in apertures of tens of micrometres, whose **connectivity**
controls the yield. No method images fractures at that scale from the surface;
what works is a combination of structural mapping, azimuthal resistivity or
seismic anisotropy, and borehole imaging.

## 7. Assumptions and regime of validity

**Darcy and Theis.**

1. Darcy's law is valid for laminar flow through a porous medium. It fails in
   karst conduits and in turbulent flow near a well, where a well-loss term must
   be added.
2. The Theis solution assumes a homogeneous, isotropic, infinite, confined
   aquifer of constant thickness, a fully penetrating well, and constant pumping
   from time zero. Real aquifers violate most of these.
3. The Theis solution contains no leakage, no recharge boundary and no river
   boundary; the deviations are diagnosed from the shape of the
   drawdown–time curve, which is why a pumping test is analysed as a curve family
   rather than a single number.

**Archie and CRIM.**

1. Archie assumes a clean (clay-free) granular rock, with the clay-free condition
   the one most often violated. A shaly sand needs a shaly-sand relation.
2. CRIM is a mixing model; it assumes that the phases are mixed at a scale small
   compared with the wavelength, and it ignores interfacial polarisation.
3. Both relate a *bulk* property to a volume fraction under an assumed geometry,
   and neither is a measurement of water content.

**Recharge.**

1. No pumping, no evapotranspiration and no surface sealing during the interval of
   rise.
2. $S_y$ is known. It usually is not, to better than a factor of two.

## 8. Quantitative treatment with units

| Quantity | Symbol | Unit | Value used here (MODELLED) |
|---|---|---|---|
| Hydraulic conductivity | $K$ | m s⁻¹ | $10^{-5}$–$10^{-2}$ |
| Saturated thickness | $b$ | m | 5–30 |
| Transmissivity | $T$ | m² s⁻¹ | $Kb$ |
| Specific storage | $S_s$ | m⁻¹ | $1.84\times10^{-6}$ |
| Specific yield | $S_y$ | – | 0.02–0.20 |
| Pumping rate | $Q$ | m³ s⁻¹ | 0.05 |
| Water resistivity | $\rho_w$ | Ω m | 10 |
| Water permittivity | $\varepsilon_w$ | – | 81 |

**Worked check 1 (Darcy).** $K = 10^{-4}$ m s⁻¹ = 8.64 m day⁻¹; with
$i = 0.002$ and $A = 1000$ m², $Q = 1.728\times10^{-4}$ m³ s⁻¹
$= 17.3$ m³ day⁻¹. And $T = Kb = 10^{-4} \times 20 =
2\times10^{-3}$ m² s⁻¹ $= 172.8$ m² day⁻¹.

**Worked check 2 (Theis).** With $Q = 0.05$ m³ s⁻¹, $T = 0.01$ m² s⁻¹,
$S = 10^{-4}$, $r = 100$ m and $t = 1$ day:
$u = (10^{4})(10^{-4})/(4 \times 0.01 \times 86400) = 2.89\times10^{-4}$, and
$W(u) = E_1(u) = 7.57$, so $s = 0.05/(4\pi \times 0.01) \times 7.57 = 3.01$ m.

## 9. Python demonstration

[`code/groundwater_aquifers_demo.py`](./code/groundwater_aquifers_demo.py)
computes Darcy flow and transmissivity, the confined and unconfined storage
coefficients, the Theis drawdown with the exponential integral evaluated from its
own series and integral, the recharge estimate, Archie's formation factor and
partial-saturation resistivity, and the CRIM permittivity with GPR velocities and
the water-table reflection coefficient.

```text
   K (m/s)    K (m/day)   Q (m^3/day)   b (m)   T (m^2/day)
     1.0e-05        0.86          1.73      10            8.6
     1.0e-02      864.00        1728.00      30        25920.0
  COMPUTED S_s = 1.8443e-06 1/m
    b =    50 m: S = S_s b = 9.2214e-05 (dimensionless)
  COMPUTED ratio S_y / S for b = 50 m: 1627 times more water released per metre of
  CHECK E1(1) = 0.2193839344 (reference 0.2193839344)
   time (d)     s at 50 m   s at 100 m   s at 500 m   u at 500 m
        1.0       3.564        3.012        1.734    7.234e-03
      100.0       5.396        4.845        3.564    7.234e-05
    T = 0.010 m^2/s, S = 1e-04: s =   8.187 m, Q/s =     527.7 m^3/day per metre
    R = 0.1 x 0.8 / 1.0 = 80.0 mm/yr
    0.30    11.11      111.111
    0.10   100.00     1000.000
    phi = 0.30, Sw = 0.5: rho_t =    444.44 ohm m
    1.0    0.30     18.19      0.0703          111.1
    0.2    0.06      5.50      0.1278         2777.8
    R = -0.2904 (29.0 per cent of amplitude)
```

### What to observe

- The specific storage gives a dimensionless storativity of
  $9.2\times10^{-5}$ for a 50 m aquifer, against a specific yield of 0.15: a factor
  of **1627**. Every statement about water availability depends on which regime is
  meant.
- The exponential integral is verified against its tabulated value at $u = 1$
  (0.2193839344 to ten figures), which is the check that the well function is
  right — the same discipline of validating a numerical routine against a known
  value that the rest of the repository applies.
- Drawdown at 50 m grows from 3.56 m at 1 day to 5.40 m at 100 days — a
  logarithmic growth of only 1.8 m for a hundredfold increase in time. That slow
  growth is why a confined aquifer appears to stabilise, and why an apparent
  "steady state" in a pumping test is usually not one.
- Archie's law gives 111 Ω m at $\phi = 0.30$ and 1000 Ω m at $\phi = 0.10$ with
  a 10 Ω m water, and the partial-saturation form raises it to 444 Ω m at
  $S_w = 0.5$. A dry sand's resistivity is therefore *higher* than a saturated
  one by a factor that depends on both porosity and saturation — which is why
  resistivity alone cannot separate the two.
- CRIM gives $v = 0.0703$ m/ns fully saturated and $0.1278$ m/ns at
  $S_w = 0.2$, and a water-table reflection coefficient of $-0.2904$: 29 per cent
  of amplitude, one of the strongest shallow reflections available.

## 10. Common mistakes

1. **Confusing porosity with permeability.** Clay is the standard counterexample.
2. **Quoting a hydraulic conductivity without the fluid.** $K$ contains the
   viscosity, so it is temperature dependent.
3. **Treating the radius of influence as a physical boundary.** It is a
   convention.
4. **Analysing a pumping test with a single solution.** The curve shape is the
   diagnostic; leakage, boundaries and well loss all show in it.
5. **Comparing storativity between a confined and an unconfined aquifer.** They
   are different quantities with different magnitudes.
6. **Reading a resistivity as a water content.** Archie needs porosity, a
   cementation exponent and a water resistivity.
7. **Assuming Archie for a shaly sand.** The clay-free condition is the one most
   often violated.
8. **Converting a water resistivity to a salinity without a temperature
   correction.** The conversion coefficient is temperature dependent.
9. **Treating a fractured-rock target as a volume target.** Connectivity controls
   the yield, and it is not imaged from the surface.
10. **Quoting a recharge or a safe yield as a measurement.** One is a model
    result, the other a regulatory statement.

## 11. Real-world applications

- **Water supply.** Site selection, well-field design and aquifer delineation, using
  ERT and EM for geometry and a pumping test for the parameters
  ([14-01-02 Aquifer Types and Properties](../../14-hydrology-hydrogeophysics/01-hydrology-fundamentals/02-aquifer-types-and-properties.md)).
- **Saline intrusion and coastal management.** EM and ERT are the standard
  methods, because the contrast is in the pore fluid
  ([14-02-02 EM for Hydrology](../../14-hydrology-hydrogeophysics/02-hydrogeophysics-methods/02-em-for-hydrology.md)).
- **Soil moisture and the unsaturated zone.** GPR and EMI at the metre scale, with
  the permittivity contrast as the observable
  ([14-02-04 GPR for Soil Moisture](../../14-hydrology-hydrogeophysics/02-hydrogeophysics-methods/04-gpr-for-soil-moisture.md)).
- **Hydrological monitoring.** Time-lapse ERT and gravity for storage change, and
  the time-lapse signal *is* the measurement
  ([10-06 Near-Surface Monitoring](../../10-gpr-near-surface/06-nearsurface-monitoring/README.md)).
- **Contaminant and landfill studies.** Where the target is a change in pore-fluid
  conductivity rather than water itself
  ([14-04 Contaminant and Environmental Geophysics](../../14-hydrology-hydrogeophysics/04-contaminant-and-environmental/README.md)).
- **Engineered and agricultural recharge.** Mapping where infiltrated water goes,
  with the same contrasts and the same caveats.
- **Geothermal aquifers.** Where the same rock has a different hydraulic
  conductivity because the water is hot
  ([lesson 03](./03-geothermal-systems.md)).

## 12. Further reading

- **Freeze, R. A., & Cherry, J. A. *Groundwater* (Prentice-Hall).** The standard
  reference for §1–§3, including the storage mechanics in full. Level: graduate
  textbook.
- **Fetter, C. W. *Applied Hydrogeology* (Waveland).** Well hydraulics and
  pumping-test analysis, §4. Level: undergraduate to graduate textbook.
- **Theis, C. V. (1935). The relation between the lowering of the piezometric
  surface and the rate and duration of discharge of a well.** *Transactions
  AGU*. The original solution. Level: classic paper.
- **Archie, G. E. (1942). The electrical resistivity log as an aid in determining
  some reservoir characteristics.** *Transactions AIME*. The origin of §6's
  formation factor. Level: classic paper.
- **Rubin, Y., & Hubbard, S. S. (eds) *Hydrogeophysics* (Springer).** The
  geophysical methods applied to aquifers, with their resolution and their
  limits. Level: graduate.
- **Binley, A., & Kemna, A. on ERT in hydrogeology.** The method, its sensitivity
  and its inversion. Level: advanced.
- **Kirsch, R. (ed.) *Groundwater Geophysics* (Springer).** A method-by-method
  treatment with field examples. Level: professional.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 13. Related lessons

- [01 Source, Reservoir, Seal and Trap: The Petroleum System](./01-petroleum-system.md)
  — where the same fluid physics acts at depth and over geological time.
- [03 Geothermal Systems, Heat Flow and Resource Assessment](./03-geothermal-systems.md)
  — the hot end of the same aquifer system.
- [05 Unconventional Resources: Shale, Tight Gas, Hydrates](./05-unconventional-resources.md)
  — where low permeability is the defining property.
- [04-05-03 Fluvial, Coastal and Aeolian Systems](../05-geomorphology-and-quaternary/03-fluvial-coastal.md)
  — the depositional architecture that decides connectivity.
- [04-01-05 Density, Porosity, Permeability and Elastic Properties](../01-earth-structure/05-rock-physics-basics.md)
  — the rock properties behind §2 and §6.
- [14-01-03 Hydraulic Head and Darcy's Law](../../14-hydrology-hydrogeophysics/01-hydrology-fundamentals/03-hydraulic-head-darcy.md)
  — the hydrogeological treatment of §2 in more depth.
- [14-03-02 Archie and Saturation](../../14-hydrology-hydrogeophysics/03-petrophysics-hydrology/02-archie-and-saturation.md)
  — the petrophysical relations of §6.

Exercises:
[`exercises/04-groundwater-aquifers-exercises.md`](./exercises/04-groundwater-aquifers-exercises.md)
and
[`exercises/04-groundwater-aquifers-solutions.md`](./exercises/04-groundwater-aquifers-solutions.md).

## Self-assessment checklist

- [ ] I can give an example of a rock with high porosity and low permeability.
      (§2)
- [ ] I can classify an aquifer by type and by confinement, and say which decides
      the pumping response. (§1)
- [ ] I can apply Darcy's law and compute a transmissivity with units. (§2)
- [ ] I can compute a specific storage and a specific yield and compare them.
      (§3, §9)
- [ ] I can compute a Theis drawdown and explain the logarithmic behaviour. (§4)
- [ ] I can state why the radius of influence needs a convention. (§4)
- [ ] I can estimate recharge from water-table fluctuation and state its main
      weakness. (§5)
- [ ] I can compute a formation factor and explain what Archie's exponents are.
      (§6)
- [ ] I can compute an effective permittivity with CRIM and a radar velocity from
      it. (§6, §9)
- [ ] I can explain why a saline wedge is an easier target than a fractured
      granite. (§6)
