---
id: 02-05-02
title: "First Law, Work and Energy Balances"
level: intermediate
prereqs: ["02-05-01", "02-02-03"]
estimated_minutes: 90
tags: [first-law, enthalpy, adiabat, geothermal-energy]
---

# First Law, Work and Energy Balances

The first law says that internal energy changes only by heat crossing the
boundary or work done at the boundary. Written that way it sounds like a
tautology, and in a sense it is: it defines heat as whatever energy transfer is
not work. Its power comes from the fact that the books must balance, so any
budget that does not close contains a flux you have not accounted for. In
practice, virtually every error in a geophysical thermal model — a geothermal
resource estimate, a magma-chamber cooling curve, a mantle potential
temperature — is an unclosed energy budget with one term missing.

This lesson fixes the sign convention, derives the two forms of the law that
geophysics actually uses (the enthalpy form for flowing systems and the
adiabatic gradient for convecting ones), and then applies them to a geothermal
power plant, a crystallising magma, and a descending slab.

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the first law in the geophysical sign convention and audit a closed
   cycle to show that $\Delta U$ vanishes.
2. **Distinguish** internal energy from enthalpy, and say which is conserved in
   a steady-flow device and which in a closed system.
3. **Derive** the adiabatic (isentropic) temperature gradient
   $\mathrm{d}T/\mathrm{d}P = \alpha T/(\rho c_p)$ and convert it into K km⁻¹
   for the mantle, the crust, the outer core and the atmosphere.
4. **Explain** why the mantle adiabat is a few tenths of a kelvin per kilometre
   while the dry atmospheric lapse rate is ~9.8 K km⁻¹, from the same formula.
5. **Close** the energy balance of a geothermal plant, including the work
   output and the rejected heat, and state which part is decided by the second
   law.
6. **Compute** the latent-heat fraction of a crystallising magma and the
   temperature change of a parcel descending adiabatically.

## Prerequisites

- [02-05-01 Temperature, Heat, Internal Energy and Specific Heat](./01-temperature-and-heat.md)
  — the three quantities the law relates.
- [02-02-03 Work, Energy, Power and Conservative Forces](../02-classical-mechanics/03-work-energy.md)
  — work as a line integral, and the mechanical energy budget.

## 1. The law and its sign convention

For a closed system (fixed mass, no material crossing the boundary),

$$\boxed{\ \mathrm{d}U = \delta Q - \delta W\ } \tag{1}$$

with the geophysical convention

| Symbol | Sign | Meaning |
|---|---|---|
| $\delta Q > 0$ | heat **into** the system | the system is being warmed from outside |
| $\delta W > 0$ | work done **by** the system | the system pushes its boundary outward |

This convention is the one used in most geophysics, and it is the opposite of the
one used in some chemistry texts. There is no "wrong" convention, but a model that
mixes two conventions produces energies wrong by a factor of the wrong sign, and
such errors are hard to see because the numbers still look plausible.

For a system that can only do work by expanding against pressure,
$\delta W = p\,\mathrm{d}V$, so

$$\mathrm{d}U = \delta Q - p\,\mathrm{d}V . \tag{2}$$

### 1.1 Why enthalpy exists

Geothermal systems are not closed: fluid enters, fluid leaves, and the work of
pushing fluid in and out is unavoidable. Adding it to the books defines

$$H \equiv U + pV , \qquad \mathrm{d}H = \delta Q + V\,\mathrm{d}p \quad
\text{(reversible)} . \tag{3}$$

For a steady-flow device with inlet enthalpy $h_1$ and outlet $h_2$ per unit
mass, no shaft work and negligible kinetic-energy change,

$$\dot m\,(h_2 - h_1) = \dot Q . \tag{4}$$

This is the form to use for a geothermal wellhead. It is *not* the form to use
for a closed parcel of mantle rock, where equation (2) is correct and $H$ would
introduce a spurious pressure term.

**Regime of validity.** Equations (2)–(4) assume a fixed-mass or
steady-flow system with no chemical reactions and no external field. The mantle
and core are in a gravitational field, so for a moving parcel the gravitational
potential energy must be carried separately (it is, in a convective calculation);
for local thermodynamics at a point it does not enter.

## 2. Derivations

### 2.1 The adiabatic gradient

Take a parcel of rock, displace it slowly enough that it stays in pressure
equilibrium with its surroundings and fast enough that it exchanges no heat. Then
$\delta Q = 0$, and equation (3) gives $\mathrm{d}h = V\,\mathrm{d}p$, i.e.

$$\left(\frac{\partial T}{\partial p}\right)_S
= \frac{T}{\rho c_p}\left(\frac{\partial V}{\partial T}\right)_p
= \frac{\alpha T}{\rho c_p} , \tag{5}$$

where the step in the middle uses one of the Maxwell relations and the last step
uses the definition of the volumetric expansion coefficient $\alpha$. Equation (5)
is exact for a single-phase material in local equilibrium under an isentropic
displacement. It is the gradient a parcel follows; it is not the gradient the
*environment* has, and confusing the two is a common error in convection.

### 2.2 From pressure to depth

The lithostatic relation $\mathrm{d}p/\mathrm{d}z = \rho g$ converts (5) into a
gradient in K m⁻¹:

$$\left(\frac{\mathrm{d}T}{\mathrm{d}z}\right)_S = \frac{\alpha T g}{c_p} . \tag{6}$$

For an ideal gas $\alpha = 1/T$ exactly, so the $T$ cancels and equation (6)
collapses to the **dry adiabatic lapse rate** $g/c_p$, independent of temperature
and pressure. With $g = 9.806\,65$ m s⁻² (exact, standard gravity) and
$c_p = 1005$ J kg⁻¹ K⁻¹:

$$\frac{\mathrm{d}T}{\mathrm{d}z}\bigg|_{\text{dry air}} = \frac{9.80665}{1005}
= 9.758\times10^{-3}\ \text{K m}^{-1} = 9.76\ \text{K km}^{-1}. \tag{7}$$

For a solid, $\alpha$ is not $1/T$ and equation (6) keeps its temperature and
pressure dependence. Using nominal values:

| System | $\alpha$ (K⁻¹) | $T$ (K) | $\rho$ (kg m⁻³) | $c_p$ (J kg⁻¹ K⁻¹) | $\mathrm{d}T/\mathrm{d}P$ (K GPa⁻¹) | $\mathrm{d}T/\mathrm{d}z$ (K km⁻¹) |
|---|---|---|---|---|---|---|
| Mantle | 3 × 10⁻⁵ | 1600 | 3300 | 1250 | 11.64 | 0.377 |
| Crust | 8 × 10⁻⁶ | 800 | 2700 | 800 | 2.96 | 0.079 |
| Outer core | 1 × 10⁻⁵ | 4000 | 11 000 | 700 | 5.19 | 0.560 |
| Dry air | $1/T$ | — | — | — | — | 9.758 |

**The two orders of magnitude that separate them are the whole point.** The mantle adiabat is
about 0.4 K km⁻¹; a conductive continental geotherm is 10–40 K km⁻¹; the dry
atmosphere is 9.8 K km⁻¹. A convective mantle is nearly isothermal, a conductive
lithosphere is not, and the atmosphere sits between them because a gas expands
enormously for a given temperature change while a solid does not.

### 2.3 Adiabatic compression of a descending parcel

A slab, or any mantle parcel, that descends 100 km with no heat exchange
experiences $\Delta p = \rho g \Delta z = 3300 \times 9.80665 \times 10^5
= 3.236\times10^9$ Pa, and therefore

$$\Delta T = \frac{\alpha T}{\rho c_p}\,\Delta p = 11.64 \times 3.236
= 37.7\ \text{K} \tag{8}$$

for the mantle parameters above. Thirty-eight kelvin per hundred kilometres.
This is why the mantle adiabat is nearly flat in temperature, why a ridge
geotherm and a plume geotherm differ by a few hundred kelvin across thousands of
kilometres, and why the excess temperature of a plume is a *carried* property
rather than something generated on the way up.

### 2.4 Internal heat sources

For a continuous medium with a distributed source of power per unit volume
$A$ (radiogenic heating, latent heat). the steady heat equation acquires the
source term

$$\nabla\cdot(k\nabla T) + A = 0 , \tag{9}$$

and the transient law is

$$\rho c_p \frac{\partial T}{\partial t} = \nabla\cdot(k\nabla T) + A . \tag{10}$$

Equation (10) *is* the first law applied to a continuum element: the left side is
the rate of change of stored internal energy, the first term on the right is the
net heat conducted in, and $A$ is the heat generated internally. Lessons
[04](./04-heat-conduction.md) and [06](./06-geotherms.md) work both terms.

## 3. Applications

### 3.1 A geothermal plant

Take a flash plant with 100 kg s⁻¹ of water dropping from 200 °C to 50 °C and
$c_p = 4186$ J kg⁻¹ K⁻¹ (nominal). The advected enthalpy drop is

$$\dot Q = \dot m c_p \Delta T = 100 \times 4186 \times 150 = 6.28\times10^7\
\text{W} = 62.8\ \text{MW}_{th}. \tag{11}$$

At a conversion efficiency of 12 per cent the electrical output is 7.53 MW and
55.26 MW is rejected to cooling. The books balance: 7.53 + 55.26 = 62.79 MW.

**The first law does not choose the efficiency.** Any value of $\eta$ between 0
and 1 balances. What limits $\eta$ is the second law, which for these
temperatures gives a Carnot ceiling of $1 - 323.15/473.15 = 0.3170$; a real plant
gets 40–60 per cent of that. So the division of labour is clean: the first law
tells you how much energy there is, and the second law tells you how much of it
can be turned into work.

### 3.2 A crystallising magma

Latent heat is an internal source term of the type in equation (10). For basalt
with $\rho = 2900$ kg m⁻³, $c_p = 840$ J kg⁻¹ K⁻¹ and $L = 4\times10^5$
J kg⁻¹ (nominal), cooling from 1500 K to 300 K releases 2.92 × 10⁹ J m⁻³ of
sensible heat and 1.16 × 10⁹ J m⁻³ of latent heat — 28.4 per cent of the total.

The consequence is quantitative. If crystallisation spans 150 K, the apparent heat
capacity inside that interval is

$$(\rho c_p)_{\text{eff}} = \rho c_p + \frac{\rho L}{\Delta T_{\text{xtal}}}
= 2.436\times10^6 + \frac{1.16\times10^9}{150} = 1.017\times10^7\
\text{J m}^{-3}\,\text{K}^{-1}, \tag{12}$$

a factor of 3.2 larger than outside it. A thermal model that ignores this factor
predicts a magma chamber crystallising three times too fast.

### 3.3 Convective versus conductive heat transport, by energy balance

Consider the whole mantle. The rate at which it must deliver heat to the base of
the lithosphere is the surface heat flow minus the crustal contribution. In a
convective interior the transport is by advection of enthalpy, and the
first law applied to a rising limb gives

$$\dot Q \approx \rho c_p\, \bar v\, A\, \Delta T_{\text{excess}} , \tag{13}$$

with $\bar v$ the mean upwelling velocity. Putting numbers to it — the boundary
between conduction and convection is a first-law bookkeeping statement before it
is anything else — is lesson [05](./05-convection-radiation.md), and the
instability that decides which mode operates is the Rayleigh number there.

## 4. Physical interpretation

**The adiabatic gradient is the temperature gradient of a *moving* fluid.** A
system at rest has a temperature gradient set by how heat gets in and out. A
system in vigorous motion has a gradient set by how much it can compress. The
mantle is the second kind; the lithosphere is the first. The two meet at the
lithosphere base, and their intersection is the definition of that boundary.

**$c_p$ versus $c_v$ is the same distinction in miniature.** Heating at constant
pressure does work against expansion; heating at constant volume does not. In a
solid the expansion is negligible, so the two costs are nearly equal. In a gas
they differ by a factor of 1.4, and in the atmosphere the difference is the
difference between the dry adiabat and the isothermal atmosphere.

**Enthalpy is the bookkeeper of a flow.** Any system that has material entering
and leaving — a hydrothermal system, a magma conduit, a geothermal well — is
described by $h$, not $u$, and the difference is real: the $pV$ term accounts for
the work the flow does on the surrounding fluid to make room for itself.

## 5. Assumptions and regime of validity

| Approximation | Statement | What breaks outside it |
|---|---|---|
| Reversible displacement | A parcel stays in pressure equilibrium; no dissipation | Fast ascent (explosive volcanism) is irreversible and heats the parcel |
| $\delta Q = 0$ for the adiabat | The parcel exchanges no heat | Exchange is significant for small parcels or slow motion; the mantle is not strictly adiabatic |
| Single phase | $\alpha$, $c_p$ are those of one material | Melting, dehydration, or a phase transition absorbs latent heat and flattens the gradient |
| Ideal-gas $\alpha = 1/T$ | The dry adiabat is $g/c_p$ | Moist air releases latent heat; the saturated lapse rate is much smaller |
| Negligible kinetic energy | $h_2 - h_1$ is the energy change of the flow | High-velocity wellbore flow and volcanic jets need the kinetic term |
| Steady flow | Equation (4) has no storage term | Start-up, shut-in and pressure-transient tests are transient by construction |
| Distributed source $A$ is known | Equation (10) can be integrated | Radiogenic heat production of a real rock varies by a factor of 3 |

## 6. Units and dimensional analysis

- $\mathrm{d}U$, $Q$, $W$, $H$: all J ✓. Equation (1) is dimensionally trivial;
  the risk is not units but sign.
- $pV$: $\mathrm{Pa}\cdot\mathrm{m^3} = \mathrm{J}$ ✓ — enthalpy is measured in
  joules, not joules per mole, in the form used here.
- $\alpha T/\rho c_p$: $\mathrm{K^{-1}\cdot K\cdot m^3\,kg^{-1}\cdot kg\,K\,J^{-1}}
  = \mathrm{m^3\,K\,J^{-1}} = \mathrm{K\,Pa^{-1}}$ ✓ since
  $\mathrm{J\,m^{-3}} = \mathrm{Pa}$. So equation (5) has units K Pa⁻¹, and
  multiplying by $\rho g$ [Pa m⁻¹] gives K m⁻¹ ✓.
- $A$: W m⁻³. Then $A/(\rho c_p)$: $\mathrm{W\,m^{-3}}/(\mathrm{J\,m^{-3}K^{-1}})
  = \mathrm{K\,s^{-1}}$ ✓, a heating rate, as required by equation (10).
- **A useful anchor**: the mantle adiabat is ~0.4 K km⁻¹ and the crustal
  conductive gradient is ~25 K km⁻¹. Any computed mantle adiabat of 25 K km⁻¹
  or any computed crustal adiabat of 9 K km⁻¹ indicates a substituted $\alpha$
  or a confused $c_p$.

## 7. Python demonstration

[`code/first_law_demo.py`](./code/first_law_demo.py) audits a closed cycle,
tabulates equation (5) for four systems, closes a geothermal plant balance,
computes the latent-heat plateau, and computes the adiabatic heating of a
descending parcel. Observed output:

```text
  dU = Q - W with Q > 0 into the system, W > 0 done by the system
  Step 1: Q = +5.0e+06 J, W = +2.0e+06 J  ->  dU = 3.0e+06 J (internal energy rises)
  Step 2: Q = -1.0e6 J, W = +2.0e6 J  ->  dU = -3.0e+06 J
  Cycle total dU = 0.0e+00 J  (must be 0 for a closed cycle)
```

```text
system                        dT/dP (K/GPa)   rho*g (Pa/m)   dT/dz (K/km)
mantle (alpha=3e-5/T)               11.6364        32361.9         0.3766
crust (alpha=8e-6/T)                 2.9630        26478.0         0.0785
outer core (alpha=1.0e-5/T)          5.1948       107873.1         0.5604
dry atmosphere (g/c_p)                                             9.7579
```

```text
  advected enthalpy drop  m_dot c_p dT = 6.2790e+07 W = 62.79 MW thermal
  electric output at eta = 0.12      = 7.5348e+06 W = 7.53 MWe
  heat rejected to cooling    = 5.5255e+07 W = 55.26 MW
  closure check: electric + rejected = 62.79 MW  (equals thermal input)

  The first law is satisfied for ANY eta. Choosing eta is the job of
  the second law (lesson 02-05-03): the Carnot bound for these
  temperatures is 1 - 323.15/473.15 = 0.3170.
```

```text
    rho L / 150 K = 7.7333e+06 J m^-3 K^-1
  against the sensible rate of 2.4360e+06 J m^-3 K^-1 — a factor
    3.17
  greater heat release per kelvin of cooling inside the interval
```

```text
  dP over 100 km = rho g dz = 3.2362e+09 Pa = 3.2362 GPa
  dT = (alpha T / rho c_p) dP = 37.658 K
```

### What to observe

| Observation | Consequence |
|---|---|
| The cycle closes to exactly 0 J | The sign convention is being applied consistently; a non-zero total would be a sign error, not physics |
| Mantle adiabat 0.377 K km⁻¹ against crustal 0.079 K km⁻¹ | The crustal value is *smaller*, because $\alpha$ is three times smaller and $T$ is half |
| Atmosphere 9.76 K km⁻¹, two orders above the mantle | The same formula covers both; the difference is entirely in $\alpha = 1/T$ |
| Electric + rejected = thermal input exactly | The first law closes for any $\eta$; it does not choose $\eta$ |
| Plateau factor 3.17 | Latent heat is a source term of the same magnitude class as sensible heat |
| 37.7 K per 100 km of descent | Adiabatic heating is real but small; it cannot generate a hot plume |

> **Breaking exercise.** Change the mantle $\alpha$ from 3 × 10⁻⁵ to 3 × 10⁻⁶ K⁻¹
> and predict, before running, the new mantle adiabat. Then explain why the real
> mantle's $\alpha$ rises with temperature and falls with pressure, and what that
> does to the shape of the adiabat.

## 8. Common mistakes

1. **Mixing sign conventions.** Using $\mathrm{d}U = \delta Q + \delta W$ in one
   place and $\mathrm{d}U = \delta Q - \delta W$ in another. Pick the geophysical
   convention and state it.
2. **Using the adiabat as the environment's gradient.** The adiabat is what a
   parcel follows. A region is unstable only if the *environmental* gradient
   exceeds it — that condition is the basis of convective instability.
3. **Forgetting that the mantle adiabat is not zero.** "The mantle is isothermal"
   is wrong by 0.4 K km⁻¹, which is 1200 K across the mantle — larger than most
   of the temperature differences being discussed.
4. **Applying the dry adiabat to moist air.** Latent heat release in a rising
   saturated parcel gives a saturated lapse rate of roughly 5–6 K km⁻¹, not 9.8.
5. **Omitting latent heat from a magma cooling model.** Factor 3.2 on the
   effective heat capacity during crystallisation.
6. **Assuming the first law sets an efficiency.** It does not; it only closes the
   books. Efficiency is a second-law question.
7. **Ignoring the $pV$ term in a flowing system.** Using $u$ instead of $h$ in
   equation (4) for a wellbore introduces an error of order $pV/m$, which for
   water at 20 MPa is ~20 kJ kg⁻¹ against $\Delta h$ of hundreds of kJ kg⁻¹ —
   several per cent.
8. **Adding kinetic energy when it does not matter, and omitting it when it
   does.** In a geothermal well flow at metre-per-second velocities the kinetic
   term is negligible; in a volcanic jet it is not.

## 9. Real-world applications

- **Geothermal reservoir assessment.** The recoverable power of a field is an
  enthalpy balance, and the choice of flash, binary or dry-steam plant follows
  from the enthalpy of the produced fluid
  ([05-09](../../05-core-geophysics/09-geothermal-and-heat-flow-methods/README.md)).
- **Magma chamber and lava lake thermal models.** Equation (10) with a
  temperature-dependent effective heat capacity including latent heat is the
  standard tool for predicting solidification
  ([13-06](../../13-geodynamics-tectonics/06-crustal-and-lithospheric-dynamics/README.md)).
- **Potential temperature in mantle geochemistry and geodynamics.** The
  temperature a parcel would have if brought adiabatically to the surface is the
  standard way to compare melts from different depths; it is equation (5)
  integrated.
- **Atmospheric stability indices.** The dry and saturated adiabats of equation
  (7) and its moist analogue determine whether air parcels rise, which is the
  whole of convective weather
  ([16-01](../../16-atmosphere-climate/01-atmospheric-structure-and-thermodynamics/05-atmospheric-dynamics-basics.md)).
- **Contact metamorphism and ore genesis.** The energy balance of an intrusion
  against its host rock sets the duration of the hydrothermal circulation that
  concentrates metals.

## 10. Further reading

- **Fermi, E. *Thermodynamics* (Dover reprint).** The first law derived carefully,
  with the same insistence on the distinction between state functions and
  process quantities. Level: beginner.
- **Callen, H. B. *Thermodynamics and an Introduction to Thermostatistics*
  (2nd ed., Wiley).** Enthalpy, the Maxwell relations, and the derivation of
  equation (5). Level: intermediate to advanced.
- **Turcotte, D. L., & Schubert, G. *Geodynamics* (3rd ed., Cambridge University
  Press, 2014).** Mantle adiabats, the effect of phase transitions and latent
  heat on the adiabatic gradient, and convection treated as an energy balance.
  Level: graduate.
- **Stüwe, K. *Geodynamics of the Lithosphere* (2nd ed., Springer, 2007).**
  Adiabatic versus conductive gradients in the crust and lithosphere, with the
  geothermal applications. Level: intermediate.
- **Incropera, F. P., & DeWitt, D. P. *Fundamentals of Heat and Mass Transfer*
  (Wiley).** The steady-flow energy equation and the control-volume method in
  full generality. Level: intermediate.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 11. Related lessons

- [01 Temperature, Heat, Internal Energy and Specific Heat](./01-temperature-and-heat.md)
  — what is being conserved.
- [03 Second Law, Entropy and Irreversibility](./03-second-law.md) — which
  energy balances are achievable, and why efficiency is not a first-law question.
- [04 Heat Conduction, Fourier's Law and Thermal Diffusivity](./04-heat-conduction.md)
  — equations (9) and (10) in the conduction limit.
- [05 Convection, Radiation and Combined Heat Transfer](./05-convection-radiation.md)
  — advective transport and the Rayleigh number.
- [02-11-04 Atmospheric Structure, Hydrostatic Balance and Lapse Rates](../11-physics-of-earths-interior-and-atmosphere/04-atmospheric-structure.md)
  — the moist version of equation (7).
- [13-geodynamics-tectonics/01 Momentum, Mass and Energy Balances in the Solid Earth](../../13-geodynamics-tectonics/01-geodynamic-principles/01-momentum-mass-energy.md)
  — the same three balances, coupled.

Exercises:
[`exercises/02-first-law-exercises.md`](./exercises/02-first-law-exercises.md)
and
[`exercises/02-first-law-solutions.md`](./exercises/02-first-law-solutions.md).

## Self-assessment checklist

- [ ] I can state the first law with the geophysical sign convention and audit a
      cycle to zero. (§1, §7)
- [ ] I can explain why a flowing system is described by enthalpy rather than
      internal energy. (§1.1)
- [ ] I can derive $\partial T/\partial P|_S = \alpha T/(\rho c_p)$ and convert
      it to K km⁻¹. (§2.1, §2.2)
- [ ] I can explain the factor of 26 between the mantle and atmospheric
      adiabatic gradients. (§2.2)
- [ ] I can compute the adiabatic heating of a parcel descending a stated depth.
      (§2.3)
- [ ] I can write the transient heat equation with an internal source and say
      what each term is. (§2.4)
- [ ] I can close a geothermal energy balance and state which quantity the second
      law limits. (§3.1)
- [ ] I can compute the effective heat capacity of a crystallising magma and the
      plateau factor. (§3.2)
