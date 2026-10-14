---
id: 04-01-05
title: "Density, Porosity, Permeability and Elastic Properties"
level: intermediate
prereqs: ["04-01-04", "02-04-04"]
estimated_minutes: 90
tags: [rock-physics, porosity, permeability, gassmann, archie, elastic-moduli]
---

# Density, Porosity, Permeability and Elastic Properties

This lesson is where the Earth science stops describing rocks and starts
predicting numbers that a measurement can be compared with. Four properties
carry almost all of the load:

| Property | Symbol | Serves |
|---|---|---|
| Density | $\rho$ | Gravity, seismic impedance, density logging |
| Elastic moduli | $K$, $G$ (through $v_p$, $v_s$) | Seismic and sonic, seismology |
| Porosity | $\phi$ | Resistivity, neutron, NMR, density log |
| Permeability | $k$ | Hydrology, well tests, NMR free-fluid index |

The reason this lesson sits at the end of the module is that each property is a
*mixture*: a rock is a mineral framework plus a pore space plus a fluid, and
every one of the four properties above is a statement about how the three
combine. The mixture laws are where the physics is, and the assumptions they
carry are where the errors are.

Two calculations in this lesson are the ones a working geophysicist performs
most often:

- **Gassmann fluid substitution**, which predicts the velocity change when the
  pore fluid changes. It is the calculation behind time-lapse seismic
  monitoring of a reservoir, and its most useful feature is that it predicts the
  *signs* of the changes rather than only their size.
- **The velocity–porosity and porosity–permeability relations**, which are what
  allow a measured velocity or a measured conductivity to be turned into a
  porosity and a permeability — the step that makes a geophysical survey an
  aquifer or a reservoir characterisation rather than a picture.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** a bulk density from a grain density, a porosity and a pore
   fluid, for dry and saturated states.
2. **Compute** the Voigt, Reuss and Hill average moduli of a mineral mixture
   and interpret the width of the bound as a measure of ignorance.
3. **Convert** moduli to velocities and back, and explain which direction
   amplifies a measurement error and why.
4. **Apply** Gassmann fluid substitution to compute the velocity change for a
   fluid change, and explain why $v_p$ falls while $v_s$ rises when brine is
   replaced by gas.
5. **Compute** a permeability from porosity and grain size with the
   Kozeny–Carman relation, and state the two scalings that dominate it.
6. **Apply** Archie's law and the time-average equation and explain why they
   disagree about what "porosity" means.
7. **State** the regime of validity of each mixture law and the failure mode
   outside it.
8. **Map** each property to the geophysical method that measures it, and say
   which property a given survey is really mapping.

## Prerequisites

- [04-01-04 Igneous, Sedimentary and Metamorphic Rocks](./04-rock-types.md) —
  the rock classes and their property ranges.
- [02-04-04 Young's Modulus, Poisson's Ratio and the Elastic Constants](../../02-physics/04-elasticity-and-continuum-mechanics/04-elastic-moduli.md)
  — the moduli, their relations and their physical meaning.

## 1. Density: the mixture that gravity measures

$$\rho_\text{bulk} = (1-\phi)\rho_\text{grain} + \phi\,\rho_\text{fluid}.$$

The demo tabulates it for a quartz framework:

```text
     phi    fluid   rho (kg/m^3)   density contrast vs grain
    0.00    brine         2650.0                        0.0%
    0.20    brine         2320.0                      -12.5%
    0.20      gas         2140.0                      -19.2%
    0.30    brine         2155.0                      -18.7%
    0.30      gas         1885.0                      -28.9%
```

Two sources of contrast in one equation, and a single density measurement cannot
separate them. A gas-filled sand at 20 per cent porosity is 180 kg/m³ lighter
than the same sand full of brine, which moves the contrast from $-12.5$ to
$-19.2$ per cent. That difference, appearing over years as a reservoir is
produced, is the signal a time-lapse gravity or seismic survey looks for.

The lesson to carry away: **a density anomaly is a statement about bulk
density, and bulk density is a three-part mixture.** The mineral framework, the
pore volume and the pore fluid all contribute, and a survey with one density
number cannot tell them apart without a second, differently weighted
measurement.

## 2. Quantitative treatment: effective moduli and the bounds

A rock is a composite, and there is no exact formula for the effective elastic
moduli of a general composite. There are **bounds**, and the bounds are
themselves the useful result. For a two-mineral mixture with volume fractions
$f_1 + f_2 = 1$:

$$M_V = f_1M_1 + f_2M_2 \quad\text{(Voigt, iso-strain, upper bound)},$$

$$\frac{1}{M_R} = \frac{f_1}{M_1} + \frac{f_2}{M_2}
\quad\text{(Reuss, iso-stress, lower bound)},$$

$$M_H = \tfrac12(M_V + M_R) \quad\text{(Hill average)}.$$

The demo applies them to a quartz–calcite mixture:

```text
   f_calcite     K_V     K_R     K_H     G_V     G_R     G_H  VRH spread
        0.25    46.5    42.4    44.4    40.5    39.4    40.0          9%
        0.50    56.0    49.6    52.8    37.0    35.7    36.3         12%
        0.75    65.5    59.7    62.6    33.5    32.6    33.0          9%
```

The spread is an honest measure of ignorance. Knowing only the mineral
fractions, the bulk modulus of a 50/50 mixture lies somewhere in a 12 per cent
band, and the calculation cannot say where. Everything that narrows the band —
pore geometry, crack density, cementation, saturation, grain contacts — is
information that has to come from somewhere other than the mineralogy. That is
why rock physics is a subject rather than a formula, and why the Hill average
has to be quoted as a model rather than as a measurement.

The bound is wider for the bulk modulus than for the shear modulus here, because
quartz and calcite differ by a factor of 2.0 in $K$ (37 against 75 GPa) and only
1.5 in $G$ (44 against 30 GPa). The wider the contrast between the end members,
the wider the ignorance. A rock whose minerals are very different is the rock
whose properties are least predictable from its mineralogy.

## 3. Quantitative treatment: moduli and velocities, both directions

$$v_p = \sqrt{\frac{K + \frac{4}{3}G}{\rho}}, \qquad v_s = \sqrt{\frac{G}{\rho}},
\qquad
G = \rho v_s^2, \qquad K = \rho\!\left(v_p^2 - \tfrac{4}{3}v_s^2\right).$$

The forward direction is what a rock-physics model produces; the inverse
direction is what a seismic interpreter works in. The demo does both and checks
the round trip:

```text
    rho (kg/m^3)   K (GPa)   G (GPa)  Vp (m/s)  Vs (m/s)   Vp/Vs      nu
  quartzite, compact          2650      37.0      44.0      6008      4075    1.47   0.074
  limestone, compact          2710      75.0      30.0      6514      3327    1.96   0.324
  sandstone, 20% phi          2320      15.0       6.9      3230      1725    1.87   0.301
  shale, 15% phi              2450      20.0       6.0      3381      1565    2.16   0.364

  label                K (GPa)   G (GPa)      nu     error
  quartzite, compact     37.00     44.00   0.074  7.68e-16
  limestone, compact     75.00     30.00   0.324  2.37e-16
  sandstone, 20% phi     15.00      6.90   0.301  1.29e-16
  shale, 15% phi         20.00      6.00   0.364  0.00e+00
```

The round trip is exact to floating-point precision, which is the *algebra*
being consistent and nothing more. What matters in practice is the error
amplification, which the demo also computes — a one per cent error in each
velocity, propagated separately:

```text
  label                dK/K for 1% in Vp   dK/K for 1% in Vs
  quartzite, compact                5.2%               -3.2%
  limestone, compact                3.1%               -1.1%
  sandstone, 20% phi                3.2%               -1.2%
  shale, 15% phi                    2.8%               -0.8%
```

The error is *amplified* everywhere, and most for the rock with the lowest
Poisson's ratio. The reason is that $K = \rho(v_p^2 - \frac43v_s^2)$ is a
difference of two comparable terms, and cancellation amplifies a relative error.
Bulk modulus is therefore the least well determined elastic constant recovered
from a velocity measurement — a statement about the arithmetic, not about the
rock.

A note on the Poisson's-ratio column: 0.074 for the pure-quartz rock is
genuinely low, because quartz itself has a low ratio
([04-01-03](./03-mineralogy.md)). Real sandstones and quartzites sit at 0.10 to
0.20 once feldspar, clay and cement are present, and most crustal rocks fall
between 0.2 and 0.3. A measured 0.35 or above is evidence of soft, clay-rich or
overpressured material rather than of a different mineralogy.

## 4. Physical reasoning: Gassmann fluid substitution

The velocity of a fluid-saturated rock depends on the fluid, but a fluid has no
shear modulus, so the way it enters is not obvious. Gassmann's relation
separates the two:

$$K_\text{sat} = K_\text{dry} + \frac{\left(1 - K_\text{dry}/K_\text{min}\right)^2}
{\dfrac{\phi}{K_\text{fl}} + \dfrac{1-\phi}{K_\text{min}} - \dfrac{K_\text{dry}}{K_\text{min}^2}},
\qquad G_\text{sat} = G_\text{dry}.$$

The shear modulus is unchanged by the fluid — exactly, not approximately — and
that single fact produces the most useful diagnostic in reservoir geophysics.

The demo applies it to a 20 per cent porosity sandstone whose dry-rock moduli
are $K_\text{dry} = 9.92$ GPa and $G_\text{dry} = 6.87$ GPa, computed from
$v_p = 3000$ m/s and $v_s = 1800$ m/s at the dry density:

```text
     fluid   K_fl (GPa)   K_sat (GPa)   rho (kg/m^3)  Vp (m/s)  Vs (m/s)
     brine         2.20         15.01           2320      3228      1721
       oil         1.00         12.42           2280      3076      1736
       gas         0.02          9.98           2140      2990      1792

    Vp falls from 3228 to 2990 m/s, a change of -7.4 per cent.
    Vs rises from 1721 to 1792 m/s, +4.1 per cent.
```

Both signs follow from the physics.

- **$v_p$ falls** because the saturating fluid's bulk modulus falls: gas at
  0.02 GPa is far more compressible than brine at 2.2 GPa, so $K_\text{sat}$
  drops and $v_p$ drops with it.
- **$v_s$ rises** even though $G$ does not change, because $v_s = \sqrt{G/\rho}$
  and the density falls by more than nothing. The rock gets lighter without
  getting weaker in shear.

That pair of opposing signs is why a reservoir study uses $(v_p, v_s)$ rather
than $v_p$ alone: the two velocities separate "the rock changed" from "the fluid
changed". A drop in $v_p$ with a *rise* in $v_s$ is a fluid substitution. A drop
in both is a change of rock or of pressure, and a change in neither is a change
that the seismic method cannot see.

## 5. Quantitative treatment: permeability, Archie and the time average

**Permeability from porosity and grain size.** The Kozeny–Carman relation
idealises the pore space as a bundle of capillary tubes:

$$k = \frac{d^2\phi^3}{180(1-\phi)^2}.$$

```text
    d (mm)    phi       k (m^2)       k (D)
      0.05   0.25     3.858e-13        0.39
      0.10   0.25     1.543e-12        1.56
      0.20   0.25     6.173e-12        6.25
      0.50   0.25     3.858e-11       39.09
```

Two scalings. The grain-size dependence is **quadratic**, so a ten-fold coarser
sand is a hundred-fold more permeable at the same porosity: sand and silt are
not two points on a continuum for a hydrologist, they are an aquifer and an
aquitard. The porosity dependence is **steeper than cubic** at low porosity,
because the $(1-\phi)^2$ in the denominator grows as the pores close as well —
the demo computes that losing five porosity points from 0.25 to 0.20 costs
55 per cent of the permeability, and the same loss from 0.15 to 0.10 costs
74 per cent.

The honest caveat is that $k$ is controlled by the pore **throats**, not the
pores, and throat size depends on diagenesis, clay content and stress. A core
measurement can differ from the reservoir-scale value by orders of magnitude,
which is why permeability is the property that is almost always calibrated
rather than predicted.

**Archie's law** connects the water saturation to the rock's resistivity:

$$S_w = \left(\frac{aR_w}{\phi^m R_t}\right)^{1/n}.$$

With $a = 1$, $m = 2$, $n = 2$ and $R_w = 0.1$ Ω·m, the demo returns
$S_w = 0.943$ at $\phi = 0.15$, $R_t = 5$ Ω·m, and $S_w = 2.108$ at
$R_t = 1$ Ω·m. The second value is impossible — a saturation cannot exceed 1 —
and that is instructive rather than embarrassing: the formula is being used
outside the domain where its parameters describe the rock, and a printed $S_w$
above 1 is a warning that the model, not the rock, has failed.

**The time-average equation** connects the velocity to the porosity:

$$\frac{1}{v_p} = \frac{\phi}{v_\text{fluid}} + \frac{1-\phi}{v_\text{matrix}}.$$

With $v_\text{fluid} = 1500$ and $v_\text{matrix} = 5500$ m/s it gives 3587 m/s
at $\phi = 0.20$. A Gassmann calculation for the same rock gave 3228 m/s. The
two disagree by 11 per cent, and the reason is that they are not measuring the
same porosity: Archie's law reports the connected, brine-filled volume
fraction, while the time average responds to however much soft material the
rock contains, including isolated pores, soft grains and cracks. When a report
quotes "porosity" it has to say which measurement produced the number and which
model converted it. The neutron log measures hydrogen, the density log measures
electrons, the sonic log measures travel time and Archie measures conductivity:
four different porosities in the same rock.

## 6. Assumptions and regime of validity

| Assumption | Where it holds | What breaks without it |
|---|---|---|
| Bulk density is a volume-weighted mixture | Exactly; it is a definition | Nothing — but it cannot separate its own terms |
| Voigt/Reuss bounds bracket the true modulus | Always, for a two-phase mixture | They do not predict the value inside the bound |
| Hill average is the value | Sometimes | It is a model; the true modulus can be anywhere in the bound |
| Gassmann's relation | Isotropic rock, single fluid, low frequency, no chemical interaction | Anisotropic or fractured rock, patchy saturation, and ultrasonic frequencies all violate it |
| Kozeny–Carman permeability | Clean, well-sorted sands | Clay, diagenesis and stress make it unreliable by orders of magnitude |
| Archie's law | Clean, water-wet sandstones with a connected brine phase | Shaly sands, carbonates with vugs, and hydrocarbon-wet rocks all fail it |
| The time-average equation | Compressible pore fluid, stiff matrix | Gas-saturated rocks (the fluid term becomes negligible) and soft matrices |

Two rows are the ones most often violated in practice. Gassmann assumes a
**single fluid** filling the pore space in a uniform way; a rock with patches of
gas and patches of brine violates the uniform-saturation assumption, and the
errors can exceed 20 per cent in $v_p$. And Archie's law assumes a **connected
brine phase**; a carbonate with vugs can hold hydrocarbons in the vugs while the
matrix stays fully brine-saturated, and the conductivity then reports a
saturation the volume calculation does not agree with. Both failures are
detectable, with a second measurement, and both are invisible to the model
alone.

## 7. Units and dimensional analysis

| Quantity | Unit | Check |
|---|---|---|
| Density | kg/m³ | 1 g/cm³ = 1000 kg/m³ |
| Modulus | Pa, GPa | $[\rho v^2]$ |
| Velocity | m/s | Use SI in every modulus calculation |
| Porosity $\phi$ | dimensionless, 0 – 1 | Reported as per cent by geologists, as a fraction in every formula |
| Permeability $k$ | m², or darcy | 1 D = $9.869\times10^{-13}$ m² |
| Resistivity $R$ | Ω·m | $R_t$, $R_w$; $R_w$ is the formation-water resistivity |
| Saturation $S_w$ | dimensionless, 0 – 1 | Must satisfy $0 \le S_w \le 1$ |

Three checks worth doing every time.

**The porosity unit check.** Porosity is a *fraction* in every formula and a
*percentage* in every log display. A porosity entered as 20 instead of 0.20
gives a time-average velocity of 75 m/s, which is slower than water and
therefore obviously wrong — but an Archie calculation with the same error gives
a saturation that looks plausible. State the unit.

**The permeability unit check.** $[d^2] = \text{m}^2$, so Kozeny–Carman returns
m². One darcy is $9.869\times10^{-13}$ m², so a value of $10^{-12}$ m² is about
1 D, which is a good aquifer. Mixing m² and darcy is a factor of $10^{12}$.

**The modulus unit check.** $\rho v_s^2$ with $\rho$ in kg/m³ and $v_s$ in m/s
gives Pa. A velocity in km/s and a density in g/cm³ gives
$10^{-3} \times 10^{6} = 10^{3}$ times the correct answer in Pa and
$10^{-6}$ times it if the result is read as GPa — the reason the demo converts
everything to SI before computing.

## 8. Python demonstration

[`code/rock_physics_basics_demo.py`](./code/rock_physics_basics_demo.py)
implements the density mixture, the Voigt–Reuss–Hill bounds, the
forward and inverse velocity–modulus relations with an error-propagation table,
Gassmann fluid substitution for three fluids, the Kozeny–Carman permeability,
Archie's law and the time-average equation.

Sections §1 to §5 above are quoted directly from its output. Three points about
what the demo demonstrates, rather than merely prints:

- **The bounds section shows what cannot be known.** It is a demonstration of
  the *limit* of a mineralogical calculation, and printing the spread as a
  percentage is what makes that limit usable.
- **The error-propagation section shows what a measurement costs.**
  A 1 per cent velocity error becomes a 3 to 5 per cent bulk-modulus error, and
  the amplification factor depends on the rock. That is a number a survey
  designer needs and almost never computes.
- **The Gassmann section shows why a *pair* of velocities is used.** The
  opposing signs of the $v_p$ and $v_s$ changes are the diagnostic, and the demo
  computes them rather than asserting them.

The exercise set asks for the same calculations at different porosities and
saturations, and for the sensitivity of each result to its inputs. The habit to
acquire is that of the demo: every model output is printed next to an
independent check, or next to a statement of what it would take to check it.

## 9. Common mistakes

1. **Mixing porosity as a fraction and as a percentage.** The single most
   common arithmetic error in this subject.
2. **Quoting a Hill average as if it were measured.** It is the midpoint of a
   bound, and the true value can be anywhere inside it.
3. **Forgetting that Gassmann leaves $G$ unchanged.** A change in $v_s$ with a
   fluid change is a *density* effect, not a stiffness effect.
4. **Applying Gassmann to patchy saturation.** The uniform-saturation
   assumption is violated by a real reservoir, and the error can exceed 20 per
   cent in $v_p$.
5. **Using Kozeny–Carman as a prediction.** It overestimates $k$ in real rocks
   and is unreliable in the presence of clay.
6. **Accepting a saturation above 1 from Archie's law.** It means the assumed
   parameters do not describe the rock.
7. **Treating the four "porosities" as the same quantity.** Neutron, density,
   sonic and resistivity porosities measure different things and agree only in
   an ideal rock.
8. **Reporting $K$ from velocities without an uncertainty.** It is a difference
   of comparable terms and the least well determined modulus.

## 10. Real-world applications

- **Time-lapse seismic reservoir monitoring.** Gassmann fluid substitution is
  the forward model that turns a saturation change into a predicted velocity
  change, which is what a 4-D survey is tested against.
- **Aquifer and groundwater characterisation.** Porosity and permeability are
  the two numbers a hydrogeological model needs, and both are estimated from
  geophysics through the relations in this lesson
  ([14-03-04 Building Geophysical Proxies](../../14-hydrology-hydrogeophysics/03-petrophysics-hydrology/04-geophysical-proxy-relations.md)).
- **CO$_2$ storage monitoring.** The density and velocity changes caused by
  replacing brine with supercritical CO$_2$ are computed with Gassmann before a
  monitoring survey is designed.
- **Geothermal reservoir assessment.** Porosity and permeability control the
  fluid flow that a geothermal system depends on, and the same relations apply
  at higher temperature and pressure.
- **Engineering site investigation.** The porosity and stiffness of the
  near-surface material determine its response to ground motion, and both are
  measured by seismic and electrical methods.

## 11. Further reading

- **Mavko, G., Mukerji, T., & Dvorkin, J. *The Rock Physics Handbook*
  (Cambridge University Press).** The reference for every relation in this
  lesson, with its assumptions stated for each. Level: advanced.
- **Gassmann, F. (1951). Über die Elastizität poröser Medien. *Vierteljahrsschrift
  der Naturforschenden Gesellschaft in Zürich* 96, 1–23.** The original
  derivation. Level: graduate.
- **Archie, G. E. (1942). The electrical resistivity log as an aid in
  determining some reservoir characteristics. *Transactions of the AIME* 146,
  54–62.** The origin of $S_w$ and the cementation exponent. Level: advanced.
- **Schön, J. H. *Physical Properties of Rocks: Fundamentals and Principles of
  Petrophysics* (Elsevier).** A systematic handbook of measured rock
  properties and their variability. Level: advanced.
- **Tiab, D., & Donaldson, E. C. *Petrophysics* (Elsevier).** Where these
  relations are used in practice, with the log interpretation workflow.
  Level: intermediate.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 12. Related lessons

- [04-01-03 Rock-Forming Minerals and Their Physical Properties](./03-mineralogy.md)
  — the mineral moduli that the bounds are built from.
- [04-01-04 Igneous, Sedimentary and Metamorphic Rocks](./04-rock-types.md) —
  where the property ranges and the sorting statistics come from.
- [04-02-02 Divergent, Convergent and Transform Boundaries](../02-plate-tectonics/02-plate-boundaries.md)
  — the boundary types whose rock types and property ranges this lesson
  predicts.
- [05-04 Rock Physics and Property Relations](../../05-core-geophysics/04-rock-physics/README.md)
  — the same relations developed further: Hashin–Shtrikman bounds, Gassmann's
  derivation, and the velocity–porosity–clay models.
- [14-03 Petrophysics for Hydrology](../../14-hydrology-hydrogeophysics/03-petrophysics-hydrology/README.md)
  — the porosity–permeability relations in their hydrological setting.

Exercises:
[`exercises/05-rock-physics-basics-exercises.md`](./exercises/05-rock-physics-basics-exercises.md)
and
[`exercises/05-rock-physics-basics-solutions.md`](./exercises/05-rock-physics-basics-solutions.md).

## Self-assessment checklist

- [ ] I can compute a bulk density for dry and saturated states. (§1)
- [ ] I can compute Voigt, Reuss and Hill moduli and interpret the bound width.
      (§2)
- [ ] I can convert between moduli and velocities in both directions. (§3, §8)
- [ ] I can explain why a 1 per cent velocity error gives a larger bulk-modulus
      error, and why the factor depends on the rock. (§3)
- [ ] I can apply Gassmann substitution and reproduce the signs of the $v_p$ and
      $v_s$ changes. (§4)
- [ ] I can compute a Kozeny–Carman permeability and state its two scalings.
      (§5)
- [ ] I can apply Archie's law, recognise an out-of-domain result, and explain
      the difference between Archie and velocity porosity. (§5)
- [ ] I can state the regime of validity of Gassmann, Archie and Kozeny–Carman.
      (§6)
- [ ] I can check porosity, permeability and modulus units. (§7)
- [ ] I can map each property to the method that measures it. (§1, §10)
