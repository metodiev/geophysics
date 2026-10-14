---
id: 05-09-03
title: "Geothermal Exploration Geophysics"
level: graduate
prereqs: ["05-09-01", "05-09-02", "11-04-01"]
tags: [geothermal, exploration, clay-cap, fault, mt, heat-in-place, permeability, resource]
---

# Geothermal Exploration Geophysics

## Learning objectives

By the end of this lesson you will be able to:

1. **State** what a geothermal exploration programme is actually looking for, and
   why almost none of it is the heat.
2. **Distinguish** a convective (volcanic or fault-hosted) system from a conductive
   (sedimentary basin) system, and name the geophysical signature of each.
3. **Explain** the clay-cap model and why it makes resistivity the primary
   exploration method in high-temperature systems.
4. **Compute** a heat-in-place estimate and state what it is *not*.
5. **Derive** the mantle heat flow and the thermal boundary layer from a geotherm
   and a stated convective scaling, and state the scaling's limits.
6. **State** which quantities the geophysics cannot measure — permeability above
   all — and what measurement does.

## Prerequisites

- [05-09-01 Measuring Terrestrial Heat Flow](./01-heat-flow-measurement.md)
  — the heat-flow measurement and the geotherm.
- [05-09-02 Thermal Conductivity Measurement and Corrections](./02-thermal-conductivity.md)
  — the conductivity that converts a gradient into a heat flow.
- [11-04-01 Geophysical Signatures of Geothermal Reservoirs](../../11-exploration-geophysics/04-geothermal-exploration-geophysics/01-geothermal-signatures.md)
  — the method-by-method signatures this lesson builds on.

## 1. Intuition: exploring for permeability, using heat as the locator

A geothermal resource needs three things: **heat**, **fluid**, and **permeability**.
Geophysics is good at one of them, moderate at another, and essentially blind to the
third:

| Requirement | What it is | What measures it |
|---|---|---|
| Heat | Elevated temperature at accessible depth | Temperature logs in wells; heat-flow maps; the geotherm |
| Fluid | Water (or steam) in the rock | Inferred from resistivity, from seismics, from wells |
| Permeability | Connected pathways that let the fluid flow | **Nothing remotely.** Wells, flow tests, microseismicity as a proxy, and structural inference |

The exploration problem is therefore not "where is it hot" — heat is the *easy*
part, and in many systems its surface expression (hot springs, fumaroles,
hydrothermal alteration) has already located the system. The problem is **where the
heat can be extracted**, which is a permeability question, and permeability is
inferred from structure and from proxies rather than measured.

That is why geothermal exploration is methodologically different from petroleum
exploration. In petroleum the target (a trap full of hydrocarbons) has a
characteristic geometry that seismic images directly. In geothermal the target is a
*plumbing system*, and the geophysics maps its alteration footprint, its structure
and its fluid, then infers the plumbing.

## 2. Precise definitions

### 2.1 Convective and conductive systems

- **Convective system.** Fluid circulates, carrying heat from depth. Found in
  volcanic terrains (magmatic heat) and in fault-hosted systems in extending or
  transtensional crust. The surface heat flow is *higher* than the conductive
  geotherm implies, locally by an order of magnitude.
- **Conductive system.** Heat conducts through a sedimentary sequence; the
  temperature at depth is set by $q/k$ with the basin's conductivity. Lower grade,
  but far more widespread and often co-produced with oil and gas.

The distinction matters because the geophysical targets differ: fractured basement
and volcanic rocks in the first case; aquifer geometry and depth in the second.

### 2.2 The clay-cap model

In a high-temperature convective system, hot fluids ascending along fractures alter
the rock: smectite and other clays form in a zone above the reservoir, where
temperatures are in the smectite stability range, and these clays are
**electrically conductive**. Below the cap, higher-temperature alteration forms
illite, chlorite and epidote, which are **resistive**. The result is a
characteristic **conductive cap over a resistive reservoir**, and it is the single
most useful exploration signature in the subject:

- **MT/CSEM** maps the cap and the resistive reservoir beneath it.
- The cap's base is often equated with the top of the reservoir, which is an
  *association*, not a measurement.
- The resistive zone is a *necessary* condition for a productive reservoir in this
  play type, not a sufficient one: it says the alteration happened, not that
  permeability is present.

### 2.3 Heat in place

The stored thermal energy above a reference temperature:

$$H = \int_V \rho c_p \left(T - T_{\text{ref}}\right)\mathrm{d}V . \tag{1}$$

It is a *physical* quantity and it is **not** a resource. Recovery depends on
permeability, fluid, well design, reinjection and economics; no geothermal resource
statement may be derived from equation (1) alone. The discipline of
[04-06-03 Geothermal Systems](../../04-earth-science-geology/06-petroleum-and-mineral-systems/03-geothermal-systems.md)
applies: compute the physics, leave the recovery factor symbolic.

### 2.4 Mantle heat flow and the thermal boundary layer

From the geotherm of
[05-09-01 §2.4](./01-heat-flow-measurement.md), $q_m = q_0 - Ah$ with $A$ the
radiogenic heat production in a layer of thickness $h$. For a convecting layer of
depth $d$ with Nusselt number $Nu$, the **thermal boundary layer** has thickness

$$\delta \sim \frac{d}{Nu}, \qquad
q \sim k\frac{\Delta T}{d}\,Nu . \tag{2}$$

$Nu = 1$ is pure conduction and $Nu \gg 1$ is vigorous convection.

## 3. Derivations

### 3.1 Heat in place, and why it is not a resource

For a reservoir of area $A$, thickness $h$, porosity $\phi$, fluid-filled fraction
$S$, density $\rho$, heat capacity $c_p$ and a temperature rise
$\Delta T = T - T_{\text{ref}}$:

$$H = \rho c_p A h \phi S\,\Delta T
\;\Longrightarrow\;
\frac{H}{A} = \rho c_p h \phi S \,\Delta T . \tag{3}$$

Evaluated per unit area for a SYNTHETIC case — $\rho c_p = 2.6\times10^{6}$
J m⁻³ K⁻¹, $h = 300$ m, $\phi S = 0.05$ (an effective fluid fraction), and
$\Delta T = 200$ K:

$$\frac{H}{A} = (2.6\times10^{6})(300)(0.05)(200)
= 7.8\times10^{9}\ \mathrm{J\,m^{-2}} . \tag{4}$$

At a 30-year extraction period that is an average power of
$7.8\times10^{9}/(30\times3.156\times10^{7}) = 8.2$ W m⁻² — a number that looks
encouraging until one notes that it assumes *all* the stored heat is produced, which
is exactly what recovery factor means and exactly what is not known. **Report the
heat in place, state the recovery factor symbolically, and state that permeability
sets it.**

### 3.2 The geotherm and the partition

For $T_0 = 10$ °C, $k = 2.5$ W m⁻¹ K⁻¹, $q_0 = 65$ mW m⁻², $h = 20$ km, the
demonstration measures:

| $A$ (µW m⁻³) | $q_m$ (mW m⁻²) | radiogenic share | $T$ @20 km | $T$ @50 km | $T$ @100 km |
|---|---|---|---|---|---|
| 0.4 | 57.0 | 12 % | 498.0 °C | 1182.0 °C | 2322.0 °C |
| 0.8 | 49.0 | 25 % | 466.0 °C | 1054.0 °C | 2034.0 °C |
| 1.2 | 41.0 | 37 % | 434.0 °C | 926.0 °C | 1746.0 °C |
| 1.6 | 33.0 | 49 % | 402.0 °C | 798.0 °C | 1458.0 °C |

Three things follow. First, **the mantle heat flow falls by nearly half as the
radiogenic production rises** over this range, so a shallow geothermal gradient
cannot be interpreted without the heat production. Second, the temperature at
100 km is the most sensitive to $A$, which is why lithospheric thickness inferred
from geotherms carries the largest model uncertainty. Third, all four rows use a
*constant* conductivity; a depth-dependent $k$ would change the curvature as much
as $A$ does, and the two are not separable from a temperature profile alone.

### 3.3 Nu and the boundary layer, as a scaling

With SYNTHETIC $k = 4.0$ W m⁻¹ K⁻¹, $d = 2900$ km, $\Delta T = 1300$ K and a
stated scaling $Nu = 0.18\,Ra^{1/3}$:

| $Ra$ | $Nu$ | $\delta = d/Nu$ (km) | conductive $q$ (mW m⁻²) | convective $q$ (mW m⁻²) |
|---|---|---|---|---|
| $10^{6}$ | 18.0 | 161 | 1.8 | 32.3 |
| $10^{7}$ | 38.8 | 75 | 1.8 | 69.5 |
| $10^{8}$ | 83.5 | 35 | 1.8 | 149.8 |
| $10^{9}$ | 180.0 | 16 | 1.8 | 322.8 |

The convective heat flows are of the right order for the Earth at
$Ra \sim 10^{6}$–$10^{7}$, with a boundary layer tens of kilometres thick. But the
**coefficient 0.18 and the exponent 1/3 are chosen**, and different regimes give
1/4 or 1/3; so this is an order-of-magnitude scaling, not a measurement.

What *is* measured, and measured here, are the critical Rayleigh numbers: the
demonstration solves the linear stability problem numerically and recovers

$$Ra_c^{\text{free}} = 657.5110 \quad (\text{closed form } 27\pi^4/4 = 657.5114),
\qquad
Ra_c^{\text{rigid}} = 1707.7616 \quad (\text{reference } 1707.762),$$

both to better than 0.001 per cent, with a stated caveat that at finer collocation
the eigenvalue *selection* degrades for the rigid case. These two numbers are quoted
in this repository only because they are re-derived in
`code/geothermal_demo.py`; the convection physics itself belongs to
[13-02-01 Rayleigh–Bénard Convection Applied to the Mantle](../../13-geodynamics-tectonics/02-mantle-convection/01-rayleigh-benard-mantle.md).

### 3.4 Why conductivity and heat flow both matter, and neither is the target

A conductive geothermal system's temperature at depth is

$$T(z) = T_0 + \int_0^z \frac{q(z')}{k(z')}\,\mathrm{d}z' . \tag{5}$$

So to predict the temperature at 2 km you need $q$ and $k$ — both *integrable*
quantities — and an error of 10 per cent in either is 10 per cent in $\Delta T$, i.e.
about 15 K for a 150 K rise. That is small compared with the permeability question,
which can be the difference between a 30 MW field and a dry hole. **The geophysics
that locates heat is not the geophysics that finds the resource.**

## 4. Worked examples

### 4.1 A high-temperature play: what each method contributes

**Problem.** A volcano-hosted prospect in an extensional setting. Which methods, and
what does each establish?

| Method | What it establishes | What it does not |
|---|---|---|
| MT / CSEM | The conductive clay cap and the resistive reservoir; the cap's geometry | Whether the reservoir is permeable |
| Gravity | Basin and caldera geometry, dense intrusions | Fluid or permeability |
| Microseismicity | Active fracture systems and fluid pathways as *movement* | Static permeability |
| Magnetics | Demagnetised (hydrothermally altered) zones | Temperature or permeability |
| Heat flow / temperature gradient holes | The heat, and the geotherm | The fluid's mobility |
| Structural geology from outcrop and seismic | Fault orientation and kinematics | Which faults are open at depth |
| **Wells and flow tests** | Permeability, fluid chemistry, temperature at depth | Field-wide distribution, without many wells |

The honest conclusion: the programme maps the *plumbing's* geological expression and
then the wells test it. Two to four exploration wells for a first substantiation are
typical because no surface method resolves the decisive variable.

### 4.2 A conductive play: basin temperatures

For a sedimentary basin, the target is an aquifer at depth with a useful
temperature. The calculation is equation (5) with a $q$ from regional heat-flow maps
and a $k$ from the lithology:

- $q = 60$ mW m⁻², $k = 1.8$ W m⁻¹ K⁻¹ (a shale-dominated section),
  $T_0 = 12$ °C: the gradient is 33 K km⁻¹, so 90 °C is reached at 2.4 km;
- the same $q$ with $k = 3.5$ (a sandstone section): 17 K km⁻¹, so 90 °C needs
  4.5 km.

**The conductivity matters more than the heat flow**, because it varies by a factor
of two between lithologies while $q$ varies by tens of per cent. This is why a
conductive-play assessment starts with a lithological column and a conductivity
model, and why the geophysics that helps most is the one that maps lithology (and
depth) — seismic and gravity — rather than the one that maps heat.

### 4.3 What cannot be inferred

Over a prospect, the following are frequently asserted and are not measured by any
of the geophysics:

1. **Permeability** at reservoir scale, in any direction.
2. **Fluid chemistry**, hence scaling and corrosion potential.
3. **Recharge**, hence sustainability.
4. **Whether the resistive zone is connected to the surface heat source.**
5. **The depth of the brittle–ductile transition**, which controls whether fractures
   remain open.

Each of these is a well test, a tracer test, or a modelling question with its own
assumptions. A geothermal prospect report that presents the MT anomaly as the
resource has made a category error; the correct statement is that the MT anomaly is
consistent with a clay cap over a possible reservoir, and that a well is required.

## 5. Assumptions

1. **The clay-cap association holds.** It is a strong empirical correlation in
   high-temperature systems and much weaker in low-temperature ones, and it fails
   where the cap is absent, thin, or masked by a conductive cover.
2. **A conductive geotherm above the reservoir.** Where vertical fluid flow occurs,
   the gradient is perturbed and equation (5) does not apply.
3. **Steady state**, over the diffusion time of the interval — which fails in young
   volcanic systems where the magmatic heat source is transient.
4. **A conductivity model** rather than a single number, with the anisotropy and
   saturation corrections of [05-09-02 §3.5](./02-thermal-conductivity.md).
5. **The heat-in-place volume is bounded** by the geometry the geophysics mapped,
   whose uncertainty is the dominant term in the result.
6. **No interference from other uses of the subsurface** — an engineering and
   regulatory assumption, not a physical one.

## 6. Units and dimensional analysis

- $H/A$: J m⁻² = (J m⁻³ K⁻¹)(m)(dimensionless)(K) ✓. To convert to a power,
  divide by a time in seconds and quote W m⁻²; to convert to energy, multiply by the
  area in m².
- $q$: mW m⁻². Temperature: °C or K, but $\Delta T$ must be in K for the physics
  and °C equals K for a *difference*.
- $\rho c_p$: J m⁻³ K⁻¹, of order $2$–$3\times10^{6}$ for rock, about
  $4.2\times10^{6}$ for water.
- $Nu$ and $Ra$ are dimensionless; $Ra = \alpha g \Delta T d^3/(\kappa\nu)$, so
  check which diffusivity and viscosity convention a quoted exponent pair assumes.
- $\delta$: m or km. A boundary layer of 100 km over a 2900 km layer implies
  $Nu \approx 29$.
- Resistivity: Ω m almost everywhere; a "conductive cap" is typically a few Ω m
  against tens of Ω m below. The ratio, not the absolute value, is the discriminator.

## 7. Python demonstration

`code/geothermal_demo.py` measures the critical Rayleigh numbers, computes geotherms
and evaluates the Nusselt scaling.

```python
a_c, ra_c = minimise_ra("rigid", 28, 2.4, 4.0)
print(a_c, ra_c)          # critical wavenumber and Rayleigh number
```

Measured output, abridged:

```
BC        N   critical a   Ra_c (measured)   closed form   difference
free-slip  24       2.2212          657.5112       657.511     -0.0000 per cent
free-slip  28       2.2212          657.5110       657.511     -0.0001 per cent
rigid      28       3.1162         1707.7616      1707.762     -0.0000 per cent

A (uW/m^3)   q_mantle (mW/m^2)   radiogenic share   T @20 km   T @50 km   T @100 km
        0.8              49.0               25 per cent      466.0     1054.0      2034.0

Ra          Nu        boundary layer (km)   conductive q (mW/m^2)   convective q (mW/m^2)
   1e+06      18.0                  161                    1.8                    32.3
   1e+07      38.8                   75                    1.8                    69.5
```

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| $Ra_c = 657.5110$ against $27\pi^4/4 = 657.5114$ | The stability solver is verified; the numbers may be quoted |
| $Ra_c = 1707.7616$ against 1707.762 for rigid | Both boundary conditions measured, both to 0.001 per cent |
| $q_m$ falls from 57 to 33 mW m⁻² as radiogenic $A$ rises 0.4 → 1.6 µW m⁻³ | A gradient cannot be interpreted without the heat production |
| The 100 km temperature spans 1458–2322 °C over that range | Lithospheric thickness from a geotherm is model-dominated |
| Convective $q$ spans 32–323 mW m⁻² across $Ra$ 10⁶–10⁹ | The scaling is order-of-magnitude only, and its coefficient is chosen |

> **Breaking exercise.** Change the scaling exponent from $1/3$ to $1/4$ and re-run
> Section 3. Predict which rows change most; then explain why the uncertainty in the
> exponent, not the coefficient, dominates the answer at large $Ra$.

## 8. Exercises

[`exercises/03-geothermal-exploration-exercises.md`](./exercises/03-geothermal-exploration-exercises.md)
and
[`exercises/03-geothermal-exploration-solutions.md`](./exercises/03-geothermal-exploration-solutions.md).

### ★ Foundational

**★1.** State the three requirements of a geothermal resource and which of them
geophysics measures.

**★2.** Explain the clay-cap model in three sentences, including what is conductive
and what is resistive.

**★3.** Compute $H/A$ for $\rho c_p = 2.4\times10^{6}$ J m⁻³ K⁻¹, $h = 200$ m,
$\phi S = 0.04$ and $\Delta T = 150$ K.

### ★★ Applied

**★★4.** Run `code/geothermal_demo.py` and report the geotherm table for
$A = 1.0$ µW m⁻³ (interpolate the table or recompute).

**★★5.** For $q = 75$ mW m⁻² and a lithological column with 40 per cent shale
(1.5 W m⁻¹ K⁻¹), 40 per cent sandstone (3.5) and 20 per cent limestone (2.8), compute
$k_\perp$ and the temperature at 2 km for a 12 °C surface.

**★★6.** A prospect has an MT conductive cap from 300 to 900 m and a resistive zone
below. State what that establishes, what it does not, and the two additional
measurements that would most reduce the risk.

### ★★★ Research-oriented

**★★★7.** Implement a simple conductive–convective model of a fault-hosted
geothermal system (a stated vertical conduit in a conductive half-space) and compute
the surface heat-flow anomaly and the temperature profile in a well 500 m from the
fault. Compare with a purely conductive profile and state the diagnostic that
distinguishes them in a temperature log.

**★★★8.** Design an exploration programme for a greenfield prospect: methods,
acquisition parameters, the interpretation chain, the decision points, and the
stated uncertainty in heat in place and in the probability of permeability. State
explicitly which decisions rest on geophysics and which require a well, and what the
first well must measure to be decisive.

## 9. Common mistakes

1. **Reporting heat in place as a resource.** Equation (1) is physics; recovery is
   not.
2. **Presenting an MT anomaly as the reservoir.** It is consistent with a clay cap
   over a possible reservoir.
3. **Interpreting a shallow gradient without the radiogenic heat production.**
   §3.2 quantifies the effect.
4. **Using a single conductivity when the lithology varies by a factor of two.**
   §4.2 shows it dominates the depth to a given temperature.
5. **Treating a Nusselt scaling as a measurement.** The coefficient and exponent are
   chosen (§3.3).
6. **Assuming the clay-cap association in a low-temperature system**, where it is
   much weaker.
7. **Ignoring that microseismicity measures movement, not permeability.**

## 10. Real-world applications

- **Volcanic and fault-hosted geothermal exploration.** The clay-cap/MT workflow of
  §2.2, with gravity and microseismics for structure and activity.
- **Sedimentary basin geothermal and co-produced heat.** A conductive play, where
  the lithology and the depth — mapped by seismic and gravity — dominate the
  assessment (§4.2).
- **Direct-use and district heating.** Shallower targets where the same physics
  applies over smaller depths.
- **Enhanced geothermal systems.** Where permeability is engineered rather than
  found, and where microseismic monitoring is both a tool and a regulatory
  requirement
  ([06-12-01 Induced and Triggered Seismicity](../../06-seismology/12-induced-and-triggered-seismicity/README.md)).
- **Global assessment.** Heat-flow maps and geotherms set the theoretical ceiling on
  the resource
  ([12-03-02 Global Heat Flow and Its Distribution](../../12-global-geophysics-interior/03-geotherms-and-heat-budget/02-heat-flow-global.md)).

## 11. Further reading

- **Rybach, L. & Muffler, L. J. P. (eds.) (1981). *Geothermal Systems: Principles
  and Case Histories*. Wiley.** Level: intermediate to advanced. The classical
  framework, with the clay-cap association.
- **Bödvarsson, G. S. & Witherspoon, P. A. (1989). Geothermal reservoir
  engineering. *Geothermics*, 18(3).** Level: advanced. Reservoir physics, and why
  permeability is decisive.
- **Cumming, W. (2009). Geothermal resource conceptual models using surface
  exploration data. *Proceedings, Thirty-Fourth Workshop on Geothermal Reservoir
  Engineering*, Stanford.** Level: advanced. How to build a conceptual model from
  surface data honestly.
- **Jaupart, C. & Mareschal, J.-C. (2011). *Heat Generation and Transport in the
  Earth*. Cambridge University Press.** Level: advanced. The geotherm, the
  radiogenic partition and the boundary-layer framework of §3.
- **Kuper, T. (2020) and the broader literature on MT for geothermal exploration.**
  Level: advanced. For method-specific acquisition and inversion, follow
  [11-04-02 Magnetotellurics for Geothermal Resource Assessment](../../11-exploration-geophysics/04-geothermal-exploration-geophysics/02-mt-for-geothermal.md).

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text.

## 12. Related lessons

- [05-09-01 Measuring Terrestrial Heat Flow](./01-heat-flow-measurement.md)
  — the measurement behind every heat-flow statement in this lesson.
- [05-09-02 Thermal Conductivity Measurement and Corrections](./02-thermal-conductivity.md)
  — the other input to the temperature-at-depth calculation.
- [13-02-01 Rayleigh–Bénard Convection Applied to the Mantle](../../13-geodynamics-tectonics/02-mantle-convection/01-rayleigh-benard-mantle.md)
  — where the critical Rayleigh numbers of §3.3 belong.
- [05-07-05 Reporting Geophysical Results with Honest Uncertainty](../07-interpretation-and-integration/05-reporting-results.md)
  — the reporting discipline for a resource statement.
- [11-04-01 Geophysical Signatures of Geothermal Reservoirs](../../11-exploration-geophysics/04-geothermal-exploration-geophysics/01-geothermal-signatures.md)
  — the method-by-method detail.

## Self-assessment checklist

- [ ] I can state the three resource requirements and which one geophysics cannot
      measure. (§1)
- [ ] I can distinguish convective from conductive systems and name the targets.
      (§2.1)
- [ ] I can explain the clay-cap model and its limits. (§2.2)
- [ ] I can compute a heat in place and state what it is not. (§3.1)
- [ ] I can compute a geotherm, the mantle heat flow and the radiogenic share. (§3.2)
- [ ] I can quote the critical Rayleigh numbers because I have re-derived them, and
      state the limits of a Nusselt scaling. (§3.3)
- [ ] I can run the demonstration and explain every printed number. (§7)
