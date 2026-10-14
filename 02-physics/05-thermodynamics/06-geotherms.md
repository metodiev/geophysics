---
id: 02-05-06
title: "Geotherms, Heat Flow and the Earth's Thermal Budget"
level: graduate
prereqs: ["02-05-04", "02-05-05"]
estimated_minutes: 90
tags: [geotherm, heat-flow, radiogenic-heat, thermal-budget]
---

# Geotherms, Heat Flow and the Earth's Thermal Budget

A **geotherm** is a temperature–depth profile. It is the single most useful
thermal object in solid-earth geophysics, because almost everything else is
derived from it: seismic velocity, rheology, metamorphic grade, hydrocarbon
maturity, and the depth to the brittle–ductile transition all depend on
temperature, and temperature at depth is otherwise inaccessible.

Constructing one requires a transport model (conduction, convection, or both), a
heat source distribution, and boundary conditions. This lesson builds the
standard continental conductive geotherm with exponentially distributed
radiogenic heat production, derives the partition of surface heat flow into its
mantle and crustal components, treats the oceanic lithosphere as a cooling
half-space, and then adds the whole planet up: how much heat it loses, how much
it generates, and how fast it is therefore cooling.

**One warning that governs the entire lesson.** Heat flow varies strongly by
province. Continental heat flow is typically 40–100 mW m⁻² and oceanic heat flow
typically 50–150 mW m⁻² depending on age, with local values outside both ranges.
Every number here is a *nominal* value for a province class, not a measurement at
a place, and the global mean is a summary — it is not what a drill hole sees.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the steady conductive geotherm for an exponentially distributed
   heat source, and identify each term.
2. **Derive** the partition $q_{\text{surface}} = q_{\text{mantle}} +
   A_0 h$ and explain why no crustal radiogenic heat escapes downward in a
   steady 1-D model.
3. **Construct** geotherms for three continental provinces from a single measured
   input each, and compute the thermal lithosphere thickness by two criteria.
4. **Apply** the half-space cooling model to the oceanic lithosphere, compute
   heat flow and plate thickness against age, and state the model's two
   well-known failures.
5. **Estimate** the global heat loss, the radiogenic inventory of crust and
   mantle, and the residual, and convert the residual into a secular cooling
   rate with its assumptions stated.
6. **Explain** why a purely conductive mantle is impossible and what replaces it.
7. **State** which parts of a thermal budget are measured, which are computed and
   which are assumed.

## Prerequisites

- [02-05-04 Heat Conduction, Fourier's Law and Thermal Diffusivity](./04-heat-conduction.md)
  — the transport law and the half-space solution.
- [02-05-05 Convection, Radiation and Combined Heat Transfer](./05-convection-radiation.md)
  — the convective flux that supplies the mantle contribution.

## 1. What a geotherm is, and what it is not

A geotherm is a *model* temperature profile, defined by three choices:

1. **A transport mechanism.** Conduction, or convection, or a conductive lid over
   a convective interior. The mechanism sets the functional form.
2. **A heat-source distribution.** Radiogenic production in the crust and mantle,
   latent heat at phase boundaries, and heat from the core.
3. **Boundary conditions.** Surface temperature and heat flow, and a condition at
   the base (a fixed temperature, a fixed flux, or an adiabat).

Different choices give different geotherms from the same data, which is why
published geotherms for the same region differ by tens of degrees. The honest way
to write one down is to state all three choices.

A geotherm is **not** an equilibrium temperature field except in the steady limit,
and steady requires a time much longer than $L^2/\kappa$. For the whole
lithosphere that is $10^8$ yr, so a geotherm beneath a young rift is a transient
object and must be modelled as one.

## 2. Derivations

### 2.1 Steady conduction with an exponentially distributed source

Take $z$ downward, constant $k$, surface temperature $T_0$ and surface heat flux
$q_0$ (positive upward). Radiogenic heat production decays with depth as

$$A(z) = A_0 e^{-z/h} \tag{1}$$

with $A_0$ the surface production and $h$ the characteristic depth scale
(a nominal 10 km for continental crust). The steady heat equation
(lesson [04](./04-heat-conduction.md) equation (4)) with $z$ downward is

$$k\frac{\mathrm{d}^2T}{\mathrm{d}z^2} = -A(z) . \tag{2}$$

Integrating once,

$$\frac{\mathrm{d}T}{\mathrm{d}z} = \frac{A_0 h}{k}e^{-z/h} + C , \qquad
C = \frac{q_0 - A_0 h}{k} \quad\text{(from the surface condition)}
\tag{3}$$

and integrating again with $T(0) = T_0$:

$$\boxed{\ T(z) = T_0 + \frac{q_0 - A_0 h}{k}z
+ \frac{A_0 h^2}{k}\left(1 - e^{-z/h}\right)\ } \tag{4}$$

with the corresponding upward heat flow

$$q(z) = k\frac{\mathrm{d}T}{\mathrm{d}z} = q_0 - A_0 h\left(1 - e^{-z/h}\right)
\;\xrightarrow[z\gg h]{}\; q_0 - A_0 h . \tag{5}$$

### 2.2 The partition of surface heat flow

Equation (5) at great depth carries the central result of this section:

$$q_{\text{mantle}} = q_0 - A_0 h , \qquad\text{equivalently}\qquad
q_0 = q_{\text{mantle}} + A_0 h . \tag{6}$$

The term $A_0 h$ is the total heat production in the radiogenic layer,
$\int_0^\infty A(z)\,\mathrm{d}z = A_0 h$. So **the surface heat flow is the
mantle contribution plus all of the crustal production**, and in a steady 1-D
model none of the crustal heat escapes downward. That is a consequence of the
1-D steady assumption, not a general truth: in two dimensions, some crustal heat
can flow sideways into a basin or a ridge.

Two checks on equation (6):

- **It is a partition, not a measurement.** Both $q_0$ and $A_0$ are measured;
  their difference, $q_{\text{mantle}}$, is derived and inherits both
  uncertainties. Since $A_0$ is uncertain by a factor of several in real rocks,
  the mantle heat flow is the least well determined number in any geotherm.
- **The ratio $A_0 h/q_0$ is the radiogenic fraction.** For $A_0 = 1$ µW m⁻³,
  $h = 10$ km and $q_0 = 40$, 60 and 85 mW m⁻², it is 25, 17 and 12 per cent —
  small exactly where the heat flow is large. Old, cold provinces have a
  *larger* radiogenic fraction of their surface flux than young, hot ones.

### 2.3 The thermal lithosphere

The conductive geotherm of equation (4) cannot continue downward: it would
exceed the solidus within about 100 km. The mantle below the lithosphere is
convective and its temperature follows an adiabat, $T_{\text{ad}} = T_p + 0.4z$
with $T_p$ the potential temperature and the slope in K km⁻¹ (lesson
[02](./02-first-law.md) §2.2). The base of the thermal lithosphere is where the
two curves meet. Two equivalent criteria are used in practice: the depth where the
geotherm reaches a fixed isotherm (commonly 1300 °C, the nominal
brittle–ductile transition temperature), and the depth where it intersects the
adiabat. They differ by only a few per cent for realistic parameters, as the demo
shows; and **neither is a measurement**. Both are constructions, and the meaning
of "lithosphere thickness" therefore depends on which criterion the author used.

### 2.4 Oceanic lithosphere as a cooling half-space

New oceanic lithosphere is created hot at a ridge and cools by conduction into
the ocean above. If the plate is treated as a semi-infinite half-space with
surface temperature fixed and initial temperature $T_m$, then the surface heat
flow is equation (11) of lesson [04](./04-heat-conduction.md):

$$q(t) = \frac{k\,\Delta T}{\sqrt{\pi\kappa t}} \propto t^{-1/2},
\qquad\text{with}\qquad
d(t) = 2\sqrt{\kappa t} \tag{7}$$

the thermal boundary layer thickness. Two structural features:

- **Heat flow is a stopwatch.** Because $q \propto t^{-1/2}$ with a known
  coefficient, a heat-flow measurement determines the age of the sea floor. That
  inference, made before ocean drilling, was a decisive early test of sea-floor
  spreading.
- **The invariant $q\sqrt{t} = k\Delta T/\sqrt{\pi\kappa}$ is a constant.** Any
  deviation from a constant in the $q\sqrt t$ column of a table means an
  arithmetic error, and the demo reports that column for exactly this reason.

With nominal values $k = 3.2$ W m⁻¹ K⁻¹, $\rho = 3300$ kg m⁻³,
$c_p = 1250$ J kg⁻¹ K⁻¹ (so $\kappa = 7.76\times10^{-7}$ m² s⁻¹) and
$\Delta T = 1300$ K:

| Age (Ma) | $q$ (mW m⁻²) | $d$ (km) |
|---|---|---|
| 1 | 474.4 | 9.9 |
| 5 | 212.1 | 22.1 |
| 10 | 150.0 | 31.3 |
| 25 | 94.9 | 49.5 |
| 50 | 67.1 | 70.0 |
| 100 | 47.4 | 99.0 |

**The model's two failures are as informative as its successes.**

1. *Young crust:* the model overpredicts. At 1 Ma it gives 474 mW m⁻²; measured
   values near ridge axes are far lower, because seawater circulates through the
   fractured basalt and removes heat by advection — a Péclet-number effect
   (lesson [05](./05-convection-radiation.md) §3.7).
2. *Old crust:* the model underpredicts. Beyond about 70 Ma the observed heat
   flow flattens instead of continuing to fall as $t^{-1/2}$, because the plate is
   not semi-infinite: its thermal boundary layer has reached a finite, roughly
   constant thickness. A plate model with a fixed base temperature is required for
   old lithosphere.

## 3. Computed cases

### 3.1 Continental geotherms by province

With $T_0 = 283.15$ K, $A_0 = 1.0$ µW m⁻³, $h = 10$ km and
$k = 2.5$ W m⁻¹ K⁻¹ — and *only* $q_0$ differing between rows:

| Province | $q_0$ (mW m⁻²) | $q_{\text{mantle}}$ (mW m⁻²) | radiogenic % | $T$ @20 km (°C) | $T$ @50 km (°C) | lithosphere (km) |
|---|---|---|---|---|---|---|
| Craton | 40 | 30 | 25.0 | 285 | 650 | 104.2 |
| Stable platform | 60 | 50 | 16.7 | 445 | 1050 | 62.5 |
| Extensional basin | 85 | 75 | 11.8 | 645 | 1550 | 41.7 |

The craton lithosphere is more than twice as thick as the extensional one, from
the same equations and one measured input. That is the quantitative form of the
statement that heat flow varies strongly by province.

The table also contains a **reductio**. Extrapolated to 150 km the geotherms give
1850 °C, 3050 °C and 4550 °C. A purely conductive mantle would exceed the dry
peridotite solidus within about 100 km everywhere and the whole mantle would be
molten. It is not. Therefore the mantle does not conduct; it convects, and the
conductive geotherm is valid only down to the lithosphere base. That argument is
from thermodynamics, not from a model fit, and it is what established mantle
convection.

### 3.2 Global heat loss

With continental heat flow 65 mW m⁻² over 29 per cent of the surface and oceanic
heat flow 100 mW m⁻² over 71 per cent (all nominal), and a surface area of
5.10 × 10¹⁴ m² (nominal, derived from the mean radius):

$$\bar q = 0.29(65) + 0.71(100) = 89.85\ \mathrm{mW\,m^{-2}}, \qquad
\dot Q_{\text{loss}} = 0.08985\times5.10\times10^{14}
= 4.58\times10^{13}\ \text{W} = 45.8\ \text{TW} . \tag{8}$$

The sensitivity to the global mean is substantial, and should always be quoted:

| Mean $q$ (mW m⁻²) | Total loss (TW) |
|---|---|
| 65 | 33.2 |
| 80 | 40.8 |
| 89.9 | 45.8 |
| 100 | 51.0 |

### 3.3 The radiogenic inventory

Radiogenic heating comes from the decay of ²³⁸U, ²³⁵U, ²³²Th and ⁴⁰K, in
roughly that order of importance per unit mass. Because the concentrations are
measured by geochemistry, not by geophysics, the inventory is an *assumption*
about composition applied to a *measured* volume. With nominal values:

| Reservoir | $A$ (µW m⁻³) | Volume basis | Power (TW) |
|---|---|---|---|
| Continental crust | 1.0 | 1.479 × 10¹⁴ m² × 35 km | 5.18 |
| Oceanic crust | 0.2 | 3.621 × 10¹⁴ m² × 7 km | 0.51 |
| Mantle | 0.01 | 8.889 × 10²⁰ m³ | 8.89 |
| **Total** | | | **14.57** |

**The mantle concentration is the weakest link.** 0.01 µW m⁻³ is the least
constrained number in the whole calculation: published estimates of the bulk
silicate Earth's U, Th and K content differ by enough to move the mantle term by a
factor of two or more, and the continental crustal value by similar amounts. This
is why estimates of the present-day radiogenic power span roughly 10–25 TW in the
literature. The honest statement is an order of magnitude with the assumptions
displayed, which is what the table above does.

### 3.4 The residual and secular cooling

$$\dot Q_{\text{deficit}} = \dot Q_{\text{loss}} - \dot Q_{\text{radiogenic}}
= 45.8 - 14.6 = 31.2\ \text{TW} . \tag{9}$$

If the whole deficit cooled the mantle, with $M = 4.004\times10^{24}$ kg
(Earth minus core minus crust) and $c_p = 1250$ J kg⁻¹ K⁻¹,

$$\frac{\mathrm{d}T}{\mathrm{d}t} = \frac{\dot Q_{\text{deficit}}}{Mc_p}
= 6.24\times10^{-15}\ \mathrm{K\,s^{-1}} = 197\ \mathrm{K\ per\ 10^9\ yr} .
\tag{10}$$

**Two caveats that must travel with that number.**

1. The mantle concentration of 0.01 µW m⁻³ is uncertain by a factor of two, and
   the deficit moves by tens of per cent with it.
2. Part of the surface heat loss is balanced not by mantle cooling but by cooling
   of the core and by the latent heat released as the inner core grows (lesson
   [07](./07-phase-equilibria.md) §3.5 computes a present-day latent power of
   about 1.9 TW for an adopted growth rate). Equation (10) is therefore an
   **upper bound** on the mantle cooling rate.

Published estimates of present-day secular cooling span roughly tens to about
100 K per 10⁹ yr. Equation (10) lands at the high end of that range because of the
adopted inventory. The defensible statement is that the Earth is losing more heat
than it generates by a factor of about three, and is therefore cooling on a
timescale of order 10⁹ yr — which is the statement that matters for the thermal
evolution of the planet.

## 4. Physical interpretation

**A geotherm is the arithmetic of two numbers you do not know well.** Heat flow
and heat production are both measured with substantial uncertainty, and the
temperature at depth is obtained by integrating their difference twice. Small
errors in $q_0$ become large errors in $T$ at 100 km: a 5 mW m⁻² heat-flow change
at 20 K km⁻¹ is 25 K per 100 km. Always carry the uncertainty.

**The mantle heat flow is a difference, and a difference of two uncertain numbers
is uncertain.** $q_{\text{mantle}} = q_0 - A_0h$. When $q_0$ is 40 and $A_0h$ is
10, a 50 per cent error in $A_0h$ is a 12 per cent error in the mantle
contribution; when $q_0$ is 85, the same error is 7 per cent. Cold provinces are
where the partition is hardest to determine.

**The oceanic half-space model is a calibration, not just a model.** Because $q$
depends only on age, it converts a heat-flow map into an age map. That is why
sea-floor age is known globally to better accuracy than almost any other
geological quantity.

**Every global budget is a bookkeeping exercise with one leg missing.** The heat
loss is measured (sum a map); the radiogenic production is assumed (from
composition); and the difference is attributed to cooling. If the assumed
inventory were wrong at the factor-of-two level, half the "secular cooling" would
disappear. A budget whose residual is a third of its largest term is only as good
as its weakest assumption, and the discipline is to say which one that is.

## 5. Assumptions and regime of validity

| Approximation | Statement | What breaks outside it |
|---|---|---|
| Steady state | Equations (4)–(6) | Any thermal event younger than $L^2/\kappa$; rifting, underplating, magma emplacement |
| 1-D conduction | No lateral heat flow | Basins, ridges, intrusions, and any province boundary |
| Constant $k$ | Analytic integration | $k$ varies with $T$ and lithology by a factor of 2 |
| Exponential $A(z)$ | One scale height | Real crust has layers: the upper crust is far more radiogenic than the lower |
| No advection | No fluid flow | Any basin with groundwater moving faster than ~4 cm yr⁻¹ |
| Constant surface temperature | Boundary condition | Glacial cycles and land-use change perturb the top hundred metres (lesson 04) |
| Complete partition, no downward heat loss | $q_0 = q_m + A_0h$ | 2-D geometry, where crustal heat can flow sideways |
| Half-space cooling | Equations (7) | Hydrothermal circulation on young crust; finite plate thickness on old crust |
| Uniform mantle heat production | $A = 0.01$ µW m⁻³ | Real mantle production is heterogeneous and concentrated in enriched reservoirs |
| Whole deficit cools the mantle | Equation (10) | Core cooling and inner-core latent heat take part |

## 6. Units and dimensional analysis

- Every term in equation (4) must be in K. Check the second:
  $\mathrm{W\,m^{-2}}\cdot\mathrm{m}/(\mathrm{W\,m^{-1}K^{-1}}) = \mathrm{K}$ ✓.
  The third: $\mathrm{W\,m^{-3}}\cdot\mathrm{m^2}/(\mathrm{W\,m^{-1}K^{-1}})
  = \mathrm K$ ✓. Both are dimensionally identical to $q_0 h/k$; the
  exponential term is the correction for the source's decay with depth.
- $A_0 h$: $\mathrm{W\,m^{-3}}\cdot\mathrm{m} = \mathrm{W\,m^{-2}}$ ✓, a heat
  flow. This is why the partition works: a production times a length is a flux.
- $q\sqrt t$: $\mathrm{W\,m^{-2}\,s^{1/2}}$; the invariant is awkward to quote
  but it is the correct form, and it is constant only if the model is exactly
  right.
- Equation (10): $\mathrm{W}/(\mathrm{kg}\cdot\mathrm{J\,kg^{-1}K^{-1}})
  = \mathrm{W/(J\,K^{-1})} = \mathrm{K\,s^{-1}}$ ✓.
- **Useful anchors**: a continental geotherm is 10–40 K km⁻¹; a craton's thermal
  lithosphere is ~100 km and an extensional province's ~40 km; global heat loss
  is ~45 TW; radiogenic production is ~15 TW; the radiogenic fraction of surface
  heat flow is 10–25 per cent in continental crust. Any computed continental
  geotherm sloping at 1 K km⁻¹ or at 100 K km⁻¹ is wrong before it is compared
  with data.

## 7. Python demonstration

[`code/geotherms_demo.py`](./code/geotherms_demo.py) builds the province
geotherms, finds the thermal lithosphere by two criteria, applies the half-space
cooling model, and closes the global budget. Observed output:

```text
province              q0 (mW/m2)  q_mantle radiogenic %    T@20km (C)    T@50km (C)   T@100km (C)   T@150km (C)
craton                      40.0      30.0         25.0         284.6         649.7        1250.0        1850.0
stable platform             60.0      50.0         16.7         444.6        1049.7        2050.0        3050.0
extensional basin           85.0      75.0         11.8         644.6        1549.7        3050.0        4550.0

  Thermal lithosphere thickness (depth where the geotherm reaches
  1300 C, a nominal definition):
    craton                 104.2 km
    stable platform         62.5 km
    extensional basin       41.7 km

  Cross-check against a mantle adiabat (potential temperature
  1550 K, slope 0.4 K/km):
    craton                 105.8 km
    stable platform         62.6 km
    extensional basin       41.5 km
```

```text
  Invariant: q sqrt(t) = k dT/sqrt(pi kappa) = 2664743.3162 W m^-2 s^0.5
 age (Ma)    q (mW/m2)    d (km)    q*sqrt(t)
       1.0        474.4       9.9 2664743.3162
       5.0        212.1      22.1 2664743.3162
      10.0        150.0      31.3 2664743.3162
      25.0         94.9      49.5 2664743.3162
      50.0         67.1      70.0 2664743.3162
     100.0         47.4      99.0 2664743.3162
```

```text
  global mean heat flow = 89.85 mW/m2
  total heat loss = 0.0898 W/m2 x 5.10e+14 m2 = 4.5823e+13 W = 45.82 TW

   continental crust: 1.00 uW/m3 x 1.479e+14 m2 x 35 km = 5.18 TW
  oceanic crust:     0.20 uW/m3 x 3.621e+14 m2 x 7 km = 0.51 TW
  mantle:            0.01 uW/m3 x 8.889e+20 m3 = 8.89 TW
  total radiogenic  = 14.57 TW

  Deficit (loss - production) = 31.25 TW
  Mantle mass (Earth - core - crust) = 4.0040e+24 kg
  Implied cooling rate dT/dt = deficit/(M c_p) = 6.2439e-15 K/s
                             = 197.0 K per 10^9 yr
```

### What to observe

| Observation | Consequence |
|---|---|
| `q_mantle` falls from 75 to 30 mW m⁻² as `q0` falls from 85 to 40 | The mantle contribution is the *larger* term in every province |
| Radiogenic % rises as $q_0$ falls | Cold provinces are proportionally more self-heating |
| Lithosphere 104.2 km (craton) versus 41.7 km (extensional) | A factor of 2.5 from one input, the same equations |
| The two lithosphere criteria agree to a few per cent | The definition is robust; the absolute value is construction-dependent |
| $q\sqrt t$ constant to ten digits | The half-space solution was implemented correctly; this is the arithmetic check |
| $q$ falls by 10 from 1 Ma to 100 Ma | Exactly $t^{-1/2}$; heat flow as an age chronometer |
| Loss 45.8 TW against production 14.6 TW | The planet is losing three times what it generates |
| Cooling 197 K per 10⁹ yr | An order-of-magnitude statement, dominated by the assumed mantle inventory |

> **Breaking exercise.** Set the mantle heat production to 0.02 µW m⁻³ (double)
> and predict, before running, the new deficit and cooling rate. Then explain why
> doubling the *mantle* concentration changes the radiogenic total by 60 per cent
> while doubling the *crustal* concentration changes it by 35 per cent, and what
> that says about where the uncertainty actually lives.

## 8. Common mistakes

1. **Quoting a geotherm without its assumptions.** Transport mechanism, source
   distribution and boundary conditions must all be stated.
2. **Treating the mantle heat flow as measured.** It is a difference of two
   uncertain quantities; in a cold province it is the most uncertain number in the
   problem.
3. **Forgetting that the crustal radiogenic heat appears in the surface flux.**
   Omitting $A_0h$ from equation (6) makes the mantle contribution too large by
   12–25 per cent.
4. **Extrapolating a conductive geotherm below the lithosphere.** It gives
   thousands of degrees and is not an approximation but a contradiction.
5. **Using a global mean heat flow as a local value.** Province-to-province
   variation is a factor of three; the mean is a summary statistic.
6. **Applying half-space cooling to old lithosphere.** The $t^{-1/2}$ law fails
   beyond about 70 Ma for a dynamical reason, not a measurement reason.
7. **Ignoring hydrothermal circulation on young oceanic crust.** It is why the
   modelled heat flow at 1 Ma is 474 mW m⁻² while satellite-derived estimates near
   ridges are far lower.
8. **Quoting a secular cooling rate to three digits.** The radiogenic inventory is
   uncertain by a factor of two; the derived rate inherits that.
9. **Attributing the entire heat-loss deficit to mantle cooling.** Core cooling
   and inner-core latent heat contribute.
10. **Assuming the mantle heat flow is uniform.** It varies with lithospheric age
    and with the presence of mantle plumes; a single value is a global average.

## 9. Real-world applications

- **Geothermal exploration.** The resource temperature at depth is read from a
  geotherm built on local heat flow and conductivity; the province-level
  differences of §3.1 are the first-order exploration criterion
  ([05-09/03](../../05-core-geophysics/09-geothermal-and-heat-flow-methods/03-geothermal-exploration.md)).
- **Hydrocarbon maturity.** The time–temperature history of a sedimentary basin,
  which controls whether organic matter has matured to oil or gas, is a geotherm
  plus a subsidence history; the same heat-flow data serve both.
- **Lithosphere rheology.** The depth to the brittle–ductile transition is an
  isotherm, and the geotherm therefore sets the strength of the lithosphere and
  the maximum depth of seismicity.
- **Sea-floor age and plate kinematics.** Half-space cooling converts heat flow to
  age, which is the global chronometer for oceanic crust.
- **Thermal evolution of the Earth.** The budget of §3.3–§3.4 is the initial
  condition for every thermal-evolution model
  ([12-03/03](../../12-global-geophysics-interior/03-geotherms-and-heat-budget/03-thermal-evolution.md)).
- **Global heat-flow databases.** Every interpretation starts from a map of $q$
  with each measurement's corrections recorded: topographic, palaeoclimatic,
  sedimentary and advective
  ([12-03/02](../../12-global-geophysics-interior/03-geotherms-and-heat-budget/02-heat-flow-global.md)).
- **Geoneutrino detection.** Measuring the radiogenic power directly, rather than
  assuming it, is the aim of geoneutrino experiments — a rare case of the
  inventory becoming measurable.

## 10. Further reading

- **Jaupart, C., & Mareschal, J.-C. *Heat Generation and Transport in the Earth*
  (Cambridge University Press, 2011).** The definitive modern treatment of
  continental geotherms, the heat-flow partition and the radiogenic inventory.
  Level: graduate.
- **Turcotte, D. L., & Schubert, G. *Geodynamics* (3rd ed., Cambridge University
  Press, 2014).** Half-space cooling, plate models, and the thermal budget of the
  Earth. Level: graduate.
- **Fowler, C. M. R. *The Solid Earth* (2nd ed., Cambridge University Press,
  2005).** A compact account of the global heat budget that connects this lesson
  to mantle convection. Level: intermediate to graduate.
- **Stüwe, K. *Geodynamics of the Lithosphere* (2nd ed., Springer, 2007).**
  Geotherm construction for the lithosphere, with worked examples of the
  application to metamorphism and seismicity. Level: intermediate.
- **Anderson, D. L. *Theory of the Earth* (Blackwell, 1989).** The geochemical
  constraints on the radiogenic inventory, and the geophysical consequences of
  getting them wrong. Level: graduate.
- **Dziewonski, A. M., & Anderson, D. L. (1981). Preliminary reference Earth
  model. *Physics of the Earth and Planetary Interiors*, 25(4), 297–356.** The
  reference model whose radial structure underpins the depths and volumes used in
  §3.3. Level: graduate.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 11. Related lessons

- [04 Heat Conduction, Fourier's Law and Thermal Diffusivity](./04-heat-conduction.md)
  — the transport law and the half-space solution used in §2.4.
- [05 Convection, Radiation and Combined Heat Transfer](./05-convection-radiation.md)
  — why the mantle contribution is convective.
- [07 Thermodynamic Phase Equilibria and Mantle Mineralogy](./07-phase-equilibria.md)
  — where the geotherm crosses phase boundaries, and the core's thermal state.
- [02-11-01 Pressure, Density and Gravity Inside the Earth](../11-physics-of-earths-interior-and-atmosphere/01-pressure-density-depth.md)
  — the pressures at which the geotherm is evaluated.
- [12-global-geophysics-interior/03 Geotherms and Heat Budget](../../12-global-geophysics-interior/03-geotherms-and-heat-budget/01-radiogenic-heat.md)
  — the global treatment in full.
- [05-core-geophysics/09 Geothermal and Heat-Flow Methods](../../05-core-geophysics/09-geothermal-and-heat-flow-methods/README.md)
  — how the inputs are measured.
- [13-geodynamics-tectonics/01 Momentum, Mass and Energy Balances in the Solid Earth](../../13-geodynamics-tectonics/01-geodynamic-principles/01-momentum-mass-energy.md)
  — the coupled balances.

Exercises:
[`exercises/06-geotherms-exercises.md`](./exercises/06-geotherms-exercises.md)
and
[`exercises/06-geotherms-solutions.md`](./exercises/06-geotherms-solutions.md).

## Self-assessment checklist

- [ ] I can derive the exponentially heated geotherm and identify each term.
      (§2.1)
- [ ] I can derive $q_0 = q_{\text{mantle}} + A_0h$ and explain the 1-D steady
      assumption it rests on. (§2.2)
- [ ] I can build a geotherm for a province from $q_0$ and state every other input
      I used. (§3.1)
- [ ] I can compute the thermal lithosphere thickness by two criteria and explain
      why they differ. (§2.3, §7)
- [ ] I can explain why a conductive mantle is impossible, using an extrapolated
      geotherm. (§3.1)
- [ ] I can apply half-space cooling, verify the $q\sqrt t$ invariant, and state
      the model's two failures. (§2.4, §7)
- [ ] I can estimate the global heat loss and the radiogenic inventory, and say
      which of the two is measured and which is assumed. (§3.2, §3.3)
- [ ] I can convert a heat-loss deficit into a secular cooling rate and state the
      caveats that bound it. (§3.4)
- [ ] I can explain why heat flow varies strongly by province and why a global
      mean is not a local value. (§3.1, §8)
