---
id: 11-04-01
title: "Geophysical Signatures of Geothermal Reservoirs"
level: doctoral
prereqs: ["05-09-01", "05-09-03", "04-06-03", "11-01-02"]
tags: [exploration-geophysics, geothermal, heat-flow, convection, non-uniqueness]
---

# Geophysical Signatures of Geothermal Reservoirs

**All models and data in this module are SYNTHETIC.** The geotherms, reservoir
geometries, fluid properties and anomalies below are chosen teaching values, not
measurements from any field. No well, field, operator or published resource
figure is described. Mineral, fluid and physical constants are quoted as
standard values with units.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the conductive geotherm with radiogenic heat production and
   **compute** the surface heat flow it implies.
2. **Invert** the heat-flow requirement: compute the heat flow needed for a
   stated temperature at a stated depth, and **state** the role of conductivity
   in that answer.
3. **Compute** heat in place and the sustained thermal power it implies, and
   **explain** why the answer is not a resource estimate.
4. **Derive** the porous-medium Rayleigh number and **compute** the permeability
   needed for convection, with its assumptions stated.
5. **Quantify** the resistivity signature of a clay cap and of hot water, and
   **explain** why the two are difficult to separate.
6. **Compute** the gravity anomaly of a buried body and **derive** the
   half-width depth rule.
7. **Demonstrate** the source-strength/source-depth trade-off in a heat-flow
   anomaly and **state** what breaks it.

## Prerequisites

- [05-09-01 Measuring Terrestrial Heat Flow](../../05-core-geophysics/09-geothermal-and-heat-flow-methods/01-heat-flow-measurement.md) —
  the measurement this lesson interprets.
- [05-09-03 Geothermal Exploration Geophysics](../../05-core-geophysics/09-geothermal-and-heat-flow-methods/03-geothermal-exploration.md) —
  the method-level survey treatment; this lesson is the physics and the
  non-uniqueness behind it.
- [04-06-03 Geothermal Systems, Heat Flow and Resource Assessment](../../04-earth-science-geology/06-petroleum-and-mineral-systems/03-geothermal-systems.md) —
  the geological system: heat source, permeability, fluid, caprock.
- [11-01-02 Targeting Strategy and Method Selection](../01-exploration-workflow/02-targeting-and-strategy.md) —
  how a geothermal prospect is screened before any survey.

## 1. What a geothermal system is, and what geophysics can see

A geothermal system needs four things: a **heat source**, a **permeable
reservoir**, **fluid** to carry the heat, and a **caprock** that keeps the fluid
circulating near the surface. The exploration question is which of these is
present and where — and the honest hierarchy is:

| element | best geophysical constraint | what it actually measures |
|---|---|---|
| heat flux | heat-flow / geothermometry | temperature gradient and conductivity |
| heat source | gravity, magnetics | density and magnetisation contrasts |
| reservoir permeability | **nothing directly** | fracture intensity proxies, seismicity |
| fluid | MT/EM, gravity | conductance, density |
| caprock | MT/EM, seismic | resistivity, acoustic contrast |

**Permeability — the single quantity that decides whether a geothermal prospect
produces — is not measured by any surface method.** Every surface survey
measures a proxy, and the proxy-to-permeability step is a model. That statement
organises the whole module, and it is the reason this lesson spends as much
space on non-uniqueness as on signals.

## 2. Conduction: the geotherm and the surface heat flow

Fourier's law in one dimension gives the heat flux

$$q = -k\,\frac{\mathrm{d}T}{\mathrm{d}z},$$

with $k$ the thermal conductivity in $\mathrm{W\,m^{-1}\,K^{-1}}$. With a
uniform radiogenic heat production $A$ (W m⁻³), steady state gives

$$\frac{\mathrm{d}}{\mathrm{d}z}\left(k\frac{\mathrm{d}T}{\mathrm{d}z}\right)
= -A
\qquad\Longrightarrow\qquad
q(z) = q_m + A z,
\qquad
T(z) = T_0 + \frac{q_m z + \tfrac12 A z^{2}}{k},$$

where $q_m$ is the reduced (mantle) heat flow, $T_0$ the surface temperature and
$k$ assumed constant. The surface heat flow is $q(0) = q_m + A h$ for a
producing layer of thickness $h$.

The demonstration uses $T_0 = 10$ °C, $k = 2.5\ \mathrm{W\,m^{-1}\,K^{-1}}$,
$q_m = 60\ \mathrm{mW\,m^{-2}}$, $A = 1.5\ \mathrm{\mu W\,m^{-3}}$ over 10 km:

$$q_{\text{surface}} = 60 + 1.5\times10^{-6}\times10^{4}\times10^{3}
= 75\ \mathrm{mW\,m^{-2}},$$

| depth (km) | $T$ (°C) | $\mathrm{d}T/\mathrm{d}z$ (°C/km) |
|---|---|---|
| 1 | 34 | 24.6 |
| 2 | 59 | 25.2 |
| 3 | 85 | 25.8 |
| 5 | 138 | 27.0 |
| 8 | 221 | 28.8 |

Two points. First, the gradient **steepens with depth** because production adds
to the flux from below: a single "geothermal gradient" is already a model, and
extrapolating a shallow gradient to depth under-estimates temperature. Second,
the surface heat flow is a *direct measurement*
([05-09-01](../../05-core-geophysics/09-geothermal-and-heat-flow-methods/01-heat-flow-measurement.md)) —
the one quantity in this table that does not require an inversion, only a
conductivity.

### 2.1 Inverting the requirement

For a screening question — "what heat flow do we need for 250 °C at 3 km?" — the
answer is $q = k(T-T_0)/z$:

| target $T$ (°C) | depth (km) | $k = 2.0$ | $k = 2.5$ | $k = 3.0$ (mW m⁻²) |
|---|---|---|---|---|
| 150 | 4 | 70 | 88 | 105 |
| 200 | 3 | 127 | 158 | 190 |
| 250 | 3 | 160 | 200 | 240 |
| 250 | 4 | 120 | 150 | 180 |

A 250 °C resource at 3 km needs roughly **200 mW/m²** — between two and three
times the global average. This is why heat flow is the first-order screening
criterion: it is cheap, it is direct, and the answer is a factor of two, not a
factor of two *in the model*.

## 3. Heat in place and sustained thermal power

The heat stored above a reference temperature is

$$H = \left[(1-\phi)\rho_r c_r + \phi\rho_w c_w\right] V \left(T_{\text{res}} -
T_{\text{ref}}\right),$$

where the bracketed term is the volumetric heat capacity of the saturated rock.
Using $\rho_r = 2700\ \mathrm{kg\,m^{-3}}$, $c_r = 900\
\mathrm{J\,kg^{-1}\,K^{-1}}$, $\rho_w = 1000$, $c_w = 4180$ and $\phi = 0.08$:

$$\rho c = 0.92(2.43\times10^{6}) + 0.08(4.18\times10^{6})
= 2.57\times10^{6}\ \mathrm{J\,m^{-3}\,K^{-1}}.$$

For a $2\times2$ km, 300 m thick reservoir at 250 °C with a 60 °C reference,
$V = 1.2\times10^{9}\ \mathrm{m^{3}}$:

$$H = 2.57\times10^{6}\times1.2\times10^{9}\times190
= 5.86\times10^{17}\ \mathrm{J} = 0.59\ \mathrm{EJ}.$$

Spread over 30 years ($9.467\times10^{8}$ s) that is $619\ \mathrm{MW}$ of
thermal power — if **all** of it were produced, which it is not. Reporting only
what a recovery fraction would give:

| recovery fraction | sustained thermal power (MW) |
|---|---|
| 0.02 | 12 |
| 0.05 | 31 |
| 0.10 | 62 |
| 0.25 | 155 |

**The arithmetic is physics; the fraction is engineering and economics** — it
depends on permeability, well configuration, pressure management and heat
exchange area, all of which change with technology. This is exactly the
discipline imposed in
[04-06-03](../../04-earth-science-geology/06-petroleum-and-mineral-systems/03-geothermal-systems.md)
for heat in place and in
[04-06-01](../../04-earth-science-geology/06-petroleum-and-mineral-systems/01-petroleum-system.md)
for hydrocarbon volumes: compute the physical quantity, and leave the recovery
factor symbolic.

## 4. Convection: why permeability decides everything

A geothermal system is interesting precisely because it **convects**: fluid
transports heat far faster than conduction. The criterion for the onset of
convection in a horizontal porous layer heated from below is a critical
Rayleigh number, and for the idealised free-free (constant-temperature)
boundaries it is exactly

$$\text{Ra}_c = 4\pi^{2} \approx 39.5, \qquad
\text{Ra} = \frac{\rho_w c_w \,\beta\, g\,\Delta T\,H\,k_{\text{perm}}}
{\nu\, k_{\text{therm}}},$$

with $\beta$ the thermal expansion coefficient, $\Delta T$ the temperature
difference across the layer of thickness $H$, $k_{\text{perm}}$ the (Darcy)
permeability, $\nu$ the kinematic viscosity and $k_{\text{therm}}$ the thermal
conductivity of the saturated medium.

Setting $\text{Ra} = \text{Ra}_c$ and solving for permeability, with
$\beta = 5\times10^{-4}\ \mathrm{K^{-1}}$ (hot water),
$\nu = 3\times10^{-7}\ \mathrm{m^{2}\,s^{-1}}$,
$k_{\text{therm}} = 2.0\ \mathrm{W\,m^{-1}\,K^{-1}}$ and
$\rho_w c_w = 4.18\times10^{6}\ \mathrm{J\,m^{-3}\,K^{-1}}$:

| $H$ (m) | $\Delta T$ = 50 K | 100 K | 200 K |
|---|---|---|---|
| 100 | 0.23 D | 0.12 D | 0.06 D |
| 200 | 0.12 D | 0.06 D | 0.03 D |
| 500 | 0.05 D | 0.02 D | 0.01 D |

(1 D = $9.869\times10^{-13}\ \mathrm{m^{2}}$.) Three things follow.

1. **The threshold is low.** 0.01–0.23 darcy is within the range of fractured
   basement and volcanic rock — convection is not exotic.
2. **The requirement falls as $1/(H\Delta T)$.** A thick layer with a large
   temperature difference convects at permeability so low that no surface method
   could resolve it, which is why "no resistivity anomaly" is not evidence
   against a geothermal system.
3. **The criterion is idealised.** It assumes homogeneous, isotropic
   permeability, constant properties, a horizontal layer with idealised thermal
   boundaries, and no through-flow. Real systems are heterogeneous, and a single
   upward-flowing fault can convect with a regional permeability far below the
   homogeneous threshold. The number is a screen, not a prediction.

## 5. The property contrasts that a survey can see

### 5.1 Resistivity: the caprock and the temperature

Two effects coincide in a geothermal field. **Clay alteration** (smectite,
illite) around the upflow zone lowers resistivity; **hot water** is itself more
conductive. For water, a standard relation is

$$\rho_w(T) = \rho_w(25\ ^\circ\mathrm{C})\,
\frac{25+21.5}{T+21.5},$$

and Archie's law $\rho = a\,\rho_w/\phi^{m}$ converts it to rock resistivity.
With $a = 1$, $m = 2$, $\phi = 0.25$ and $\rho_w(25\ ^\circ\mathrm{C}) =
1\ \Omega\,\mathrm{m}$:

| $T$ (°C) | $\rho_w$ ($\Omega$ m) | cap resistivity ($\Omega$ m) |
|---|---|---|
| 25 | 1.000 | 16.00 |
| 100 | 0.383 | 6.12 |
| 200 | 0.210 | 3.36 |
| 250 | 0.171 | 2.74 |

Temperature alone lowers the water resistivity by a factor of 5.8 between 25 and
250 °C, and the cap resistivity follows. But mineral alteration can lower it by
another order of magnitude. **The two mechanisms produce the same signature**,
and magnetotellurics measures *conductance* (a product of conductivity and
thickness, [11-04-02](02-mt-for-geothermal.md)) rather than temperature. The
practitioner's rule is therefore: a low-resistivity anomaly is a *target*, and
mapping it is not the same as measuring temperature.

### 5.2 Density: gravity over a body

The gravity anomaly of a buried sphere of radius $a$, density contrast
$\Delta\rho$ and centre depth $z$ is

$$g(x) = \frac{4}{3}\pi G \Delta\rho \,a^{3}
\frac{z}{\left(z^{2}+x^{2}\right)^{3/2}},
\qquad
g_{\max} = \frac{4}{3}\pi G \Delta\rho\,\frac{a^{3}}{z^{2}} .$$

*Worked numbers* ($\Delta\rho = -200\ \mathrm{kg\,m^{-3}}$, $a = 500$ m — a
low-density altered caprock):

| depth $z$ (m) | $g_{\max}$ (mGal) | half-width (m) |
|---|---|---|
| 500 | 2.80 | 383 |
| 1000 | 0.70 | 766 |
| 1500 | 0.31 | 1149 |
| 2500 | 0.11 | 1915 |

The **half-width** — the horizontal distance at which the anomaly falls to half
its maximum — follows from setting $(1+x^2/z^2)^{-3/2} = 1/2$:

$$\left(\frac{x_{1/2}}{z}\right)^{2} = 2^{2/3}-1 = 0.5874
\qquad\Longrightarrow\qquad
x_{1/2} = 0.766\,z .$$

So the half-width gives the depth *for the assumed shape*. A 0.3 mGal anomaly
from this body at 1.5 km is measurable with good field practice; the depth from
its half-width is conditional on the sphere. Depth, density contrast and radius
trade off — the standard potential-field ambiguity treated in
[07-03-02](../../07-gravity-geodesy/03-gravity-anomalies-and-modelling/02-simple-body-formulas.md).

### 5.3 The other contrasts, briefly

- **Magnetics**: hydrothermal alteration destroys magnetite, so an upflow zone
  commonly appears as a magnetic **low** within a magnetically quiet area. The
  interpretation is a *destruction of magnetisation* model, and it must be
  distinguished from a change of source depth or of rock type; the modelling
  tools are those of
  [08-03 Magnetic Anomalies and Modelling](../../08-geomagnetism-electromagnetism/03-magnetic-anomalies-and-modelling/README.md).
- **Seismic velocity**: temperature changes $v_p$ and $v_s$ by only a few per
  cent over the range of interest, and porosity/alteration changes dominate.
  Seismic therefore contributes **structure** — faults, the top of the
  reservoir, the geometry of a volcanic unit — rather than a temperature proxy.
  Passive seismic and microseismicity contribute the fracture-permeability
  proxy ([11-04-03](03-microseismic-geothermal.md)).
- **Density from the same elastic data**: the reservoir fluid expansion with
  temperature changes $\rho$ slightly, and this is generally below the
  potential-field detection threshold for the body sizes involved.

## 6. Non-uniqueness: what the anomaly amplitudes do not say

### 6.1 Heat-flow amplitude cannot separate source strength from depth

For a point source of thermal power $Q$ at depth $z$ in a half-space at steady
state, the surface heat flux above it is

$$q = \frac{Q}{2\pi z^{2}} .$$

| surface anomaly (mW m⁻²) | $Q$ at 1 km | $Q$ at 2 km | $Q$ at 3 km |
|---|---|---|---|
| 20 | 0.1 MW | 0.5 MW | 1.1 MW |
| 50 | 0.3 MW | 1.3 MW | 2.8 MW |
| 100 | 0.6 MW | 2.5 MW | 5.7 MW |

A 50 mW/m² anomaly is consistent with a 0.3 MW source at 1 km or a 2.8 MW
source at 3 km. **The amplitude gives $Q/z^{2}$; the anomaly's *width* is what
separates them**, exactly as the half-width does for gravity. This is why a
single heat-flow value is a screening datum and not an interpretation, and why
the *pattern* of many values — a bullseye, a linear anomaly along a fault, a
broad region — is the interpretable observation.

### 6.2 Everything else

The three ambiguities below are developed quantitatively in their own lessons or
modules, and are listed here as the reason this module reports ranges:

| ambiguity | what trades with what |
|---|---|
| conductance equivalence in MT | layer thickness × conductivity ([11-04-02](02-mt-for-geothermal.md)) |
| potential fields | depth × density contrast × radius ([07-03-02](../../07-gravity-geodesy/03-gravity-anomalies-and-modelling/02-simple-body-formulas.md)) |
| microseismic source | moment × stress drop × rupture area ([11-04-03](03-microseismic-geothermal.md)) |

## 7. Worked examples

### Example 1 — a geotherm with production

$T_0 = 10$ °C, $k = 2.5\ \mathrm{W\,m^{-1}\,K^{-1}}$,
$q_m = 60\ \mathrm{mW\,m^{-2}}$, $A = 1.5\ \mathrm{\mu W\,m^{-3}}$. At 3 km:

1. Flux: $q = 0.060 + 1.5\times10^{-6}\times3000 = 0.0645\
   \mathrm{W\,m^{-2}}$.
2. Conductive term: $q_m z/k = 0.060\times3000/2.5 = 72$ K.
3. Production term: $Az^2/(2k) = 1.5\times10^{-6}\times9\times10^{6}/(2\times2.5)
   = 13.5/5 = 2.7$ K.
4. $T = 10 + 72 + 2.7 = 84.7$ °C.

The demonstration prints 85 °C at 3 km (rounding of the same arithmetic). Note
the production contributes 2.7 K of 75 K — small in this model, and much larger
in a granite with high heat production, which is why the term must not be
dropped blind.

### Example 2 — the convection screen, by hand

$H = 300$ m, $\Delta T = 150$ K, $k_{\text{therm}} = 2.0$,
$\beta = 5\times10^{-4}$, $\nu = 3\times10^{-7}$:

$$\text{Ra} = \frac{(4.18\times10^{6})(5\times10^{-4})(9.81)(150)(300)
k_{\text{perm}}}{3\times10^{-7}\times2.0}
= \frac{9.23\times10^{8}\,k_{\text{perm}}}{6\times10^{-7}}
= 1.54\times10^{15}\,k_{\text{perm}}.$$

Setting $\text{Ra} = 39.5$ gives $k_{\text{perm}} = 2.6\times10^{-14}\
\mathrm{m^{2}} = 0.026$ D, consistent with the table's 0.03 D at $H = 200$ m,
$\Delta T = 200$ K. A 300 m thick layer with a 150 K contrast convects above
about 26 millidarcy. If the target is to *rule out* convection, the measurement
required is permeability to a precision of tens of millidarcy — which no
surface method delivers.

### Example 3 — heat in place with a different reservoir

Same geometry but $\phi = 0.02$ (fractured basement):

$$\rho c = 0.98(2.43\times10^{6}) + 0.02(4.18\times10^{6})
= 2.465\times10^{6}\ \mathrm{J\,m^{-3}\,K^{-1}},$$

and $H = 2.465\times10^{6}\times1.2\times10^{9}\times190 = 5.62\times10^{17}$
J = 0.56 EJ, i.e. 96% of the $\phi = 0.08$ value. **Heat in place depends
almost entirely on the rock, not on the pore fluid**, because the rock carries
most of the heat capacity. The porosity matters for *deliverability*, not for
the inventory — a distinction that is often blurred in resource reporting.

## 8. Assumptions and regime of validity

1. **Steady-state conduction.** The geotherm expressions assume steady state; a
   recent thermal event (young volcanism, an intrusion) violates it, and
   palaeoclimate perturbs the top few hundred metres
   ([05-09-02](../../05-core-geophysics/09-geothermal-and-heat-flow-methods/02-thermal-conductivity.md)).
2. **A single conductivity.** Real sections vary by a factor of two between
   shale, sand and volcanic rock; the geotherm must be computed in layers.
3. **Uniform heat production.** $A$ varies by lithology and is often measured
   only at the surface.
4. **The Rayleigh criterion is idealised.** Homogeneous, isotropic,
   constant-property layer, idealised boundaries, no through-flow; the real
   criterion is heterogeneous and system-specific.
5. **Archie's law is empirical** and fails in clay-rich and fractured rocks —
   which are precisely the rocks of interest here; clay conduction is
   volumetric and not captured by $\phi^{-m}$.
6. **The temperature coefficient of $\rho_w$ is an empirical correlation**, not
   a thermodynamic identity, and its constants are fit over a limited range.
7. **Sphere and point-source formulas assume isolated, homogeneous bodies.** Real
   sources are irregular and the anomaly is a superposition.
8. **No method measures permeability or temperature at depth directly.** Every
   statement about either is a model, and the model's non-uniqueness should be
   quoted alongside the answer.

## 9. Units and dimensional consistency

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| heat flux | $q$ | W m⁻² | $k\,\mathrm{d}T/\mathrm{d}z$ |
| conductivity | $k$ | W m⁻¹ K⁻¹ | |
| heat production | $A$ | W m⁻³ | flux/distance |
| volumetric heat capacity | $\rho c$ | J m⁻³ K⁻¹ | |
| heat in place | $H$ | J | J m⁻³ K⁻¹ × m³ × K |
| permeability | $k_{\text{perm}}$ | m² | 1 D = $9.869\times10^{-13}$ m² |
| gravity anomaly | $g$ | m s⁻² | 1 mGal = $10^{-5}$ m s⁻² |

Two conversions cause most errors in this subject: **mW/m² vs W/m²** (a factor
of 1000) and **darcy vs m²** (a factor of $9.87\times10^{-13}$). Both appear in
every real dataset.

## 10. Python demonstration

`code/geothermal_signatures_demo.py` prints:

1. the geotherm and gradient at five depths, with the surface heat flow;
2. the required-heat-flow table for four temperature/depth targets and three
   conductivities;
3. heat in place, the 30-year-sustained power, and four recovery scenarios;
4. the Rayleigh criterion table: permeability required for convection versus
   layer thickness and temperature difference;
5. water and clay-cap resistivity versus temperature;
6. the gravity anomaly and half-width for four depths, with the derivation of
   the 0.766 coefficient;
7. the source-strength/source-depth table for a heat-flow anomaly.

Print-only, seeded with `np.random.default_rng(20261014)`, exits 0.

## 11. Exercises

- [`exercises/01-geothermal-signatures-exercises.md`](exercises/01-geothermal-signatures-exercises.md)
- [`exercises/01-geothermal-signatures-solutions.md`](exercises/01-geothermal-signatures-solutions.md)

## Mastery checkpoint

> A prospect has $T_0 = 12$ °C, $k = 2.2\ \mathrm{W\,m^{-1}\,K^{-1}}$,
> $q_m = 65\ \mathrm{mW\,m^{-2}}$ and $A = 2.0\ \mathrm{\mu W\,m^{-3}}$.
> **(a)** Compute $T$ at 3 km, including the production term, and the surface
> heat flow. **(b)** State the heat flow needed for 220 °C at 3.5 km with no
> production. **(c)** For a 250 m thick layer with $\Delta T = 120$ K,
> $k_{\text{therm}} = 2.2\ \mathrm{W\,m^{-1}\,K^{-1}}$,
> $\beta = 5\times10^{-4}$, $\nu = 3\times10^{-7}$: compute the permeability
> required for convection. **(d)** A 40 mW/m² heat-flow anomaly is mapped with a
> 4 km width: state the two interpretations it admits and what additional
> measurement would separate them.

## Common pitfalls

1. **Extrapolating a shallow gradient.** Production steepens the geotherm;
   extrapolation under-estimates temperature.
2. **Reading a resistivity anomaly as temperature.** Hot water and clay
   alteration give the same signature, and MT measures conductance.
3. **Reporting heat in place as a resource.** The recovery fraction is
   engineering, not physics.
4. **Assuming the homogeneous Rayleigh threshold.** A single fault can convect
   where a homogeneous layer could not.
5. **Treating a heat-flow value as an interpretation.** Amplitude gives
   $Q/z^2$; the pattern and width carry the rest.
6. **Using Archie's law uncritically in clay-rich or fractured rock**, which is
   the rock type geothermal exploration is usually looking at.

## Related modules

- [05-09 Geothermal and Heat-Flow Methods](../../05-core-geophysics/09-geothermal-and-heat-flow-methods/README.md) —
  heat-flow measurement and method-level exploration practice.
- [04-06-03 Geothermal Systems, Heat Flow and Resource Assessment](../../04-earth-science-geology/06-petroleum-and-mineral-systems/03-geothermal-systems.md) —
  the geological system in full.
- [11-04-02 Magnetotellurics for Geothermal Resource Assessment](02-mt-for-geothermal.md) —
  the resistivity method that chases the cap and the conductor.
- [11-04-03 Microseismic Monitoring of Geothermal Fields](03-microseismic-geothermal.md) —
  the permeability proxy that actually responds to fluid flow.
- [07-03 Gravity Anomalies and Modelling](../../07-gravity-geodesy/03-gravity-anomalies-and-modelling/README.md) —
  the potential-field toolbox used in §5.2.
- [11-07-03 Case Study: Geothermal Field Development](../07-exploration-case-studies/03-case-study-geothermal.md) —
  how these signatures are combined in practice.

## Further reading

- Telford, W. M., Geldart, L. P., & Sheriff, R. E. (1990). *Applied
  Geophysics* (2nd ed.). Cambridge University Press. Level: textbook. The
  geothermal and heat-flow sections, and the potential-field formulas.
- Sheriff, R. E., & Geldart, L. P. (1995). *Exploration Seismology* (2nd ed.).
  Cambridge University Press. Level: textbook. Gravity and magnetic
  interpretation used in §5.
- Kearey, P., Brooks, M., & Hill, I. (2002). *An Introduction to Geophysical
  Exploration* (3rd ed.). Blackwell. Level: textbook. Survey-method selection,
  including the geothermal case.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.
