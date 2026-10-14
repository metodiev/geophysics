---
id: 12-03-01
title: "Radiogenic Heat Production and Mantle Geotherms"
level: doctoral
prereqs: ["02-05-04", "02-05-06", "02-09-02"]
tags: [global-geophysics, earth-interior, radiogenic-heat, geotherm, mantle, heat-flow]
---

# Radiogenic Heat Production and Mantle Geotherms

**All models and data in this module are SYNTHETIC.** The isotope inventory, the
rock compositions and the transport parameters used below are adopted inputs of
a teaching model, chosen to be representative. They are not measurements, and no
real sample, borehole or region appears anywhere in this lesson. Every number is
printed by
[`code/radiogenic_heat_demo.py`](./code/radiogenic_heat_demo.py).

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the specific heat production of a radioactive parent from its
   activity and its deposited energy per decay, and **state** why the neutrino
   fraction differs so much between the U and Th chains and K-40.
2. **Compute** the volumetric heat production $A$ of a rock from element
   concentrations, and **rank** the four isotopes actually responsible for the
   Earth's radiogenic heat.
3. **Partition** a provincial surface heat flow into its mantle and crustal
   components, and **explain** why the partition is a subtraction of two
   separately measured quantities.
4. **Integrate** the adiabatic temperature gradient exactly and **quantify** the
   error made by the constant-gradient approximation.
5. **Compute** the Rayleigh and Nusselt numbers for the whole mantle and
   **demonstrate** by numbers that a purely conductive mantle is impossible.
6. **Convert** a discontinuity depth anomaly into a temperature anomaly using a
   Clapeyron slope, and **state** the sense of the resulting transition-zone
   thickness proxy.
7. **State** which inputs of a mantle geotherm are measured, which are derived
   from other measurements, and which are pure assumption.

## Prerequisites

- [02-05-04 Heat Conduction, Fourier's Law and Thermal Diffusivity](../../02-physics/05-thermodynamics/04-heat-conduction.md) —
  Fourier's law and the steady conductive equation.
- [02-05-06 Geotherms, Heat Flow and the Earth's Thermal Budget](../../02-physics/05-thermodynamics/06-geotherms.md) —
  the conductive geotherm with an exponentially distributed source and the
  oceanic half-space model. This lesson does not re-derive those; it uses them.
- [02-09-02 Radioactive Decay, Half-Life and Dating](../../02-physics/09-radiation-and-atomic-physics/02-radioactive-decay.md) —
  activity $\lambda N$ and the decay constant.

## 1. Why the interior has a temperature at all

The Earth's surface loses heat at a rate that can be measured directly. That heat
has to come from somewhere, and there are only three candidates:

1. **Radiogenic heat**, released by the decay of long-lived isotopes in the crust
   and mantle.
2. **Secular cooling**, released by the interior getting colder with time.
3. **Core cooling and latent heat**, released at the inner-core boundary as the
   liquid outer core freezes and the whole core cools.

This lesson is about the first of the three, because it is the only one whose
size is fixed by *inventory and nuclear physics* rather than by a thermal model.
If you know how much uranium, thorium and potassium a rock contains, you know its
heat production without knowing anything about the Earth's temperature. That
makes radiogenic heat the anchor of every thermal budget in the subject — and it
makes the *uncertainty* in the trace-element inventory the dominant uncertainty
in the budget.

The second half of the lesson builds an actual mantle geotherm. The point of the
exercise is not the curve: it is that the curve is a *model output* whose
sensitivity to its inputs can be computed, and that two of the inputs (the mantle
adiabat and the convective transport efficiency) are the ones that actually
matter.

## 2. Precise definitions

### 2.1 Activity and specific heat production

A mass $m$ of a parent isotope with molar mass $M$ contains
$N = m N_A / M$ atoms, where $N_A$ is the Avogadro constant. With decay constant
$\lambda = \ln 2 / T_{1/2}$, its activity is

$$R = \lambda N = \frac{\ln 2}{T_{1/2}}\,\frac{m\,N_A}{M}
\qquad (\text{decays per second, Bq}).$$

Each decay chain releases an energy $Q_{\text{tot}}$, of which a fraction
$f_\nu$ leaves the Earth in neutrinos and never becomes heat. The specific heat
production of that parent is therefore

$$\boxed{\;H = \frac{\ln 2}{T_{1/2}}\,\frac{N_A}{M}\,
Q_{\text{tot}}\left(1 - f_\nu\right)\;}\qquad (\mathrm{W\,kg^{-1}}).$$

Note what $H$ is *not*: it is not a property of the rock. It is a property of the
isotope, with units of power per unit mass **of that isotope**.

### 2.2 Volumetric heat production

For a rock of density $\rho$ containing mass fractions $C_i$ of the natural
elements, the volumetric production is the sum over parents,

$$A = \rho \sum_i C_i f_i H_i \qquad (\mathrm{W\,m^{-3}}),$$

where $f_i$ is the isotopic fraction of the natural element (for example
$f(\mathrm{^{238}U}) = 0.9927$ of natural uranium; the two U parents share a
single element concentration).

### 2.3 The heat-flow partition

In a steady, one-dimensional conductive crust with production decaying as
$A(z) = A_0 e^{-z/h}$ (derived in
[02-05-06](../../02-physics/05-thermodynamics/06-geotherms.md) §2.1), the surface
heat flow $q_0$ and the flow entering the mantle lithosphere satisfy

$$q_{\text{mantle}} = q_0 - A_0 h .$$

$A_0 h$ is the whole column integral of the production, $\int_0^\infty A\,dz$ —
that is why the depth scale $h$ and not the crustal thickness appears. The
quantity $A_0 h / q_0$ is the **radiogenic fraction** of the surface flux.

## 3. Derivations

### 3.1 The isotope inventory, computed rather than quoted

The demonstration adopts four parents with half-lives and chain energies, and
computes $H$ from equation (2.1). It prints, in µW per kg of the pure parent:

| Parent | $T_{1/2}$ (Gyr) | $Q_{\text{tot}}$ (MeV) | $f_\nu$ | $H$ (µW kg⁻¹) |
|---|---|---|---|---|
| ²³⁸U | 4.468 | 51.7 | 0.053 | 97.56 |
| ²³⁵U | 0.704 | 46.4 | 0.041 | 570.07 |
| ²³²Th | 14.05 | 42.6 | 0.065 | 25.89 |
| ⁴⁰K | 1.248 | 1.31 | 0.30 | 38.97 |

Two features of that table drive the whole subject.

- **²³⁵U is by far the most productive per kilogram** — it is six times more
  productive than ²³⁸U — but it is only $0.72\%$ of natural uranium, so its
  contribution to a rock is small.
- **⁴⁰K deposits only $0.92\ \mathrm{MeV}$ per decay**, because 30% of its
  $1.31\ \mathrm{MeV}$ escapes as a neutrino and the remaining electron energy is
  shared with the emitted antineutrino. Its specific production is $2.5$ times
  smaller than ²³⁸U's, not hundreds of times smaller as the tiny isotopic
  abundance ($1.17\times10^{-4}$) might suggest: abundance enters only through
  the element concentration times $f_i$.

*Worked example — from a specific production to a rock.* A synthetic rock
contains $2.0\ \mathrm{ppm}$ of U by mass. Then

$$H_{\text{U in rock}} = 2.0\times10^{-6} \left(0.9927 \times 97.56
+ 0.0072 \times 570.07\right) = 2.0\times10^{-6} \times 100.97
= 2.019\times10^{-4}\ \mathrm{W\,kg^{-1}}.$$

Multiplying by $\rho = 2700\ \mathrm{kg\,m^{-3}}$ gives
$0.545\ \mathrm{\mu W\,m^{-3}}$ from uranium alone. Verify against the
demonstration's per-isotope table: $0.5230 + 0.0222 = 0.5452$. ✔

### 3.2 A synthetic crust and a synthetic mantle

The demonstration's adopted compositions give

$$A_{\text{continental crust}} = 1.351\ \mathrm{\mu W\,m^{-3}}, \qquad
A_{\text{depleted mantle}} = 0.005\ \mathrm{\mu W\,m^{-3}},$$

with the crustal value split as ²³⁸U 0.5230, ²³²Th 0.5593, ⁴⁰K 0.2462 and
²³⁵U 0.0222 µW m⁻³. Thorium, not uranium, is the largest single contributor,
because the adopted Th concentration is four times the U concentration and the
two specific productions are within a factor of four.

The mantle number is three orders of magnitude smaller, and this is the single
most consequential fact in the Earth's thermal budget. Integrating the depleted
composition over the whole mantle column gives

$$A_{\text{mantle}} \times d = 0.005\ \mathrm{\mu W\,m^{-3}} \times 2891\
\mathrm{km} = 15.8\ \mathrm{mW\,m^{-2}},$$

which is only $24\%$ of the adopted continental surface flux of
$65\ \mathrm{mW\,m^{-2}}$. **A depleted mantle cannot pay for the heat the Earth
loses.** Something else must be paying: the crust (which is enriched by a factor
of several hundred relative to the mantle) and secular cooling. That imbalance is
the subject of [03 Thermal Evolution and Secular Cooling](03-thermal-evolution.md).

### 3.3 Provincial geotherms and the partition

Three synthetic provinces, each defined by its surface heat flow $q_0$, its
surface production $A_0$ and its depth scale $h$:

| Province | $q_0$ (mW m⁻²) | $A_0$ (µW m⁻³) | $h$ (km) | $A_0h$ (mW m⁻²) | $q_{\text{mantle}}$ | $T(40\ \mathrm{km})$ (°C) |
|---|---|---|---|---|---|---|
| cold craton | 45.0 | 0.60 | 10.0 | 6.00 | 39.00 | 657.6 |
| average crust | 65.0 | 1.00 | 10.0 | 10.00 | 55.00 | 929.3 |
| extended crust | 90.0 | 1.80 | 8.0 | 14.40 | 75.60 | 1265.4 |

Two readings of the table matter.

- **The radiogenic fractions are 0.133, 0.154 and 0.160** — not monotonic in
  $q_0$, because $A_0$ also changes. If instead $A_0 h$ is held fixed at
  $10\ \mathrm{mW\,m^{-2}}$ and only $q_0$ is varied, the fractions are $0.222$,
  $0.154$ and $0.111$: they *fall* as the flux rises. The reason is arithmetic,
  not geology: the same crustal production is a bigger share of a smaller
  budget. A common error is to use this monotonic version of the statement while
  varying both quantities at once.
- **$q_{\text{mantle}}$ is a difference.** Both $q_0$ and $A_0 h$ carry
  uncertainties of tens of per cent in real provinces, so
  $q_{\text{mantle}} = q_0 - A_0h$ is the *worst determined* number in the
  table. It is not a measurement and cannot be one: no instrument sees the
  mantle heat flow directly.

### 3.4 The mantle adiabat, integrated exactly

In a convecting, well-mixed mantle the temperature follows an adiabat, and the
adiabatic gradient is a thermodynamic identity,

$$\frac{\mathrm{d}T}{\mathrm{d}z} = \frac{\alpha g T}{c_p},$$

with $\alpha$ the thermal expansivity, $g$ gravity and $c_p$ the specific heat.
This is not a small parameter problem in disguise: for the adopted values
$\alpha = 3\times10^{-5}\ \mathrm{K^{-1}}$, $g = 9.81\ \mathrm{m\,s^{-2}}$,
$c_p = 1250\ \mathrm{J\,kg^{-1}\,K^{-1}}$ and $T = 1600\ \mathrm{K}$,

$$\frac{\mathrm{d}T}{\mathrm{d}z}\bigg|_{1600} =
\frac{3\times10^{-5}\times9.81\times1600}{1250}\times10^{3}
= 0.377\ \mathrm{K\,km^{-1}}.$$

Because $T$ appears on the right-hand side, the correct integration is
exponential:

$$T(z) = T_p \exp\!\left(\frac{\alpha g z}{c_p}\right).$$

Over the whole mantle, $\alpha g d/c_p = 0.681$, so the exponential factor is
$e^{0.681} = 1.98$. The demonstration prints

$$T_{\text{exact}}(2891\ \mathrm{km}) = 3160.3\ \mathrm{K}, \qquad
T_{\text{linear}}(2891\ \mathrm{km}) = 2689.1\ \mathrm{K},$$

a difference of **471.2 K, or 14.9%**. The constant-gradient approximation is
conservative — it always under-predicts the temperature — and for a
2000-km-thick mantle it is not a rounding error. When a thermal model quotes a
"potential temperature" of 1600 K and a CMB temperature of 2800 K, the 1200 K
difference is mostly this exponential adiabat, not an exotic heat source.

### 3.5 Convective transport: why conduction cannot work

Parameterise convection by Rayleigh number and Nusselt number:

$$Ra = \frac{\rho \alpha g \Delta T d^{3}}{\kappa \eta}, \qquad
Nu = \left(\frac{Ra}{Ra_c}\right)^{\beta},
\qquad \beta = \tfrac13,$$

with $d$ the layer depth, $\kappa$ the thermal diffusivity and $\eta$ the
viscosity. The conducted flux is $q_{\text{cond}} = k\Delta T/d$ and the
convective flux is $Nu$ times that.

With the adopted values ($\Delta T = 2500\ \mathrm{K}$, $d = 2891\ \mathrm{km}$,
$\kappa = 10^{-6}\ \mathrm{m^2\,s^{-1}}$, $\eta = 10^{21}\ \mathrm{Pa\,s}$,
$Ra_c = 1100$),

$$Ra = 5.87\times10^{7}, \qquad Nu = 37.6, \qquad
q_{\text{cond}} = 3.89\ \mathrm{mW\,m^{-2}}, \qquad
q_{\text{conv}} = 146.5\ \mathrm{mW\,m^{-2}}.$$

A conducting mantle can carry **$3.9\ \mathrm{mW\,m^{-2}}$**; the Earth actually
loses roughly $65$–$100\ \mathrm{mW\,m^{-2}}$. Conduction is short by more than
a factor of 15, and no adjustment of the conductivity closes the gap.

The same conclusion follows from a temperature argument that needs no Rayleigh
number at all. A conductive mantle carrying $80\ \mathrm{mW\,m^{-2}}$ has
$\mathrm{d}T/\mathrm{d}z = q/k = 17.78\ \mathrm{K\,km^{-1}}$. Against an adopted
solidus $T_{\text{sol}} = 1400 + 3z$ (K, $z$ in km) the geotherm crosses the
solidus at **94.1 km**; against the bare 1600 K isotherm it crosses at
**89.4 km**. Either way the mantle below about 100 km would be molten. It is not,
therefore it convects. That is the entire argument, and it is worth memorising in
this form: *the mantle is solid and loses more heat than conduction allows, so it
must be convecting.*

The demonstration also inverts the exercise: to obtain
$q = 80\ \mathrm{mW\,m^{-2}}$ from the adopted $Ra$–$Nu$ law requires
$\eta = 6.1\times10^{21}\ \mathrm{Pa\,s}$, six times the adopted
$10^{21}\ \mathrm{Pa\,s}$. **The scaling law does not reproduce the flux with
independent inputs.** That discrepancy is not an error to hide; it is the honest
statement that a one-parameter $Nu(Ra)$ law calibrated on laboratory convection
is an approximation to a mantle whose viscosity varies by orders of magnitude in
space and time.

### 3.6 A discontinuity depth as a thermometer

A phase transition with Clapeyron slope $m = \mathrm{d}P/\mathrm{d}T$ sits where
the geotherm crosses the phase boundary. Since $P = \rho g z$ to first order, a
temperature anomaly $\Delta T$ displaces the transition by

$$\boxed{\;\Delta z = \frac{m\,\Delta T}{\rho g}\;}$$

*Worked example.* For a cold anomaly $\Delta T = -100\ \mathrm{K}$ with
$\rho = 3800\ \mathrm{kg\,m^{-3}}$ and $g = 9.81\ \mathrm{m\,s^{-2}}$:

- a **410-type** transition with $m = +2.5\ \mathrm{MPa\,K^{-1}}$:
  $\Delta z = 2.5\times10^{6}\times(-100)/(3800\times9.81) = -6.7\ \mathrm{km}$,
  i.e. **shallower**;
- a **660-type** transition with $m = -2.0\ \mathrm{MPa\,K^{-1}}$:
  $\Delta z = +5.4\ \mathrm{km}$, i.e. **deeper**.

The separation between the two transitions therefore **increases by 12.1 km** in
a cold region. That is exactly the sense in which transition-zone thickness is a
temperature proxy. Note carefully what the number is: a *difference of two model
depths*. It is not a temperature measurement. Converting 12.1 km into kelvin
requires the two Clapeyron slopes and the density, and an error of 20% in either
slope is a 20% error in the inferred anomaly — with no error bar visible in the
depth.

## 4. Assumptions and regime of validity

This is the section that must be read before any number above is reused.

1. **The isotope table is adopted, not measured.** Half-lives, chain energies and
   neutrino fractions are inputs of the teaching model. Different adopted values
   change $H$ by a few per cent, and change the rock-scale $A$ by the same few
   per cent.
2. **The compositions are single values.** Real crustal heat production varies by
   more than an order of magnitude within a province; a single $A_0$ is an
   average whose spread is the dominant uncertainty in $q_{\text{mantle}}$.
3. **The geotherms are steady and one-dimensional.** Steady requires
   $t \gg L^2/\kappa \approx 30\ \mathrm{Myr}$ for a 30-km crust: true for a
   craton, false beneath an active rift. One-dimensional neglects lateral
   conduction, which matters near basins and ridges.
4. **The adiabat is a well-mixed limit.** It holds where convection is vigorous
   and the boundary layers are thin. It does not hold in the thermal boundary
   layers, which is why the geotherm is conductive in the lid and adiabatic
   below.
5. **The $Nu(Ra)$ law is a parameterisation, not physics.** It is calibrated on
   isoviscous convection and applied to a strongly temperature-dependent
   rheology; the 6× viscosity discrepancy computed above is the price.
6. **$P = \rho g z$ is a first-order approximation.** $\rho$ and $g$ both vary
   appreciably through the transition zone, so the Clapeyron thermometer has a
   systematic error of order 10% in $g$.

## 5. Worked example: a full mantle geotherm from the inputs

Build the potential-temperature profile for the adopted model.

1. **Adiabat.** $T(z) = 1600\exp(0.681 z/d)$ with $z$ measured downward from the
   top of the adiabatic region. At $z = d$ (2891 km), $T = 3160.3\ \mathrm{K}$.
2. **Lid.** In the conductive lid the gradient is $q_0/k$; for the average
   province, $65\ \mathrm{mW\,m^{-2}}/2.5\ \mathrm{W\,m^{-1}\,K^{-1}}
   = 26.0\ \mathrm{K\,km^{-1}}$, giving 657.6 K at 25 km and 929.3 K at 40 km
   (the earlier table's value, including the radiogenic curvature).
3. **Matching.** The lid meets the adiabat where the two curves cross; for the
   adopted numbers that is within a few tens of kilometres of 100 km, consistent
   with the solidus-crossing depth of 94.1 km found in §3.5. The fact that two
   quite different criteria (solidus crossing, lid–adiabat intersection) give
   similar depths is a consistency check on the model, not a measurement of the
   lithosphere thickness.
4. **Sensitivity.** A $10\ \mathrm{K}$ change in potential temperature moves the
   surface flux by $d q/dT$; for the adopted model in
   [03](03-thermal-evolution.md) that slope is
   $0.31\ \mathrm{mW\,m^{-2}\,K^{-1}}$, so a 10 K error is a 5.7% flux error.
   Conversely, fitting the flux to 5% pins the potential temperature to about
   9 K — *within the model*.

## 6. Verification in the demonstration

The demonstration does not take the closed-form geotherm on trust. It integrates
$\mathrm{d}T/\mathrm{d}z = q(z)/k$ numerically, where $q(z)$ is the *measured*
flux minus the accumulated production, and compares with the closed form of
[02-05-06](../../02-physics/05-thermodynamics/06-geotherms.md):

$$\max\left|T_{\text{analytic}} - T_{\text{quadrature}}\right|
= 1.24\times10^{-7}\ \mathrm{K}$$

over the range 1–39 km. The residual is at the level of the quadrature tolerance.

The significance of that agreement is often missed: it shows that the *partition*
$q_{\text{mantle}} = q_0 - A_0h$ is not an extra assumption bolted onto the
solution. It is the same statement as the differential equation, integrated. An
analyst who treats the partition as a physical law and the ODE as a separate
result has counted one model twice.

## 7. Python demonstration

[`code/radiogenic_heat_demo.py`](./code/radiogenic_heat_demo.py) prints, in seven
labelled sections: the four specific heat productions and the neutrino check; two
rock compositions with the per-isotope split; the three provincial geotherms with
their partitions and radiogenic fractions; the exact and linear adiabats; the
Rayleigh/Nusselt calculation, the conductive-versus-convective comparison and the
solidus crossing; the Clapeyron-slope thermometer for both transition types; and
the quadrature verification. It exits 0 in under a second.

```bash
cd 12-global-geophysics-interior/03-geotherms-and-heat-budget/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python radiogenic_heat_demo.py
```

## 8. Exercises

Full sets with worked solutions are in
[`exercises/01-radiogenic-heat-exercises.md`](./exercises/01-radiogenic-heat-exercises.md)
and
[`exercises/01-radiogenic-heat-solutions.md`](./exercises/01-radiogenic-heat-solutions.md).

- **★** Compute $H$ for an adopted parent with $T_{1/2} = 10\ \mathrm{Gyr}$,
  $M = 200\ \mathrm{g\,mol^{-1}}$, $Q_{\text{tot}} = 40\ \mathrm{MeV}$ and
  $f_\nu = 0.05$, and state the units at each step.
- **★★** A province has $q_0 = 70 \pm 7\ \mathrm{mW\,m^{-2}}$ and
  $A_0h = 12 \pm 4\ \mathrm{mW\,m^{-2}}$. Give $q_{\text{mantle}}$ with its
  uncertainty and comment on which input dominates.
- **★★** Show that the radiogenic fraction $A_0h/q_0$ falls monotonically as
  $q_0$ rises when $A_0h$ is fixed, and give the value of $q_0$ at which the
  fraction is $0.20$.
- **★★★** Repeat the Clapeyron calculation with $g$ varying between the surface
  value and the value at the CMB, and bound the systematic error in $\Delta T$.

## 9. Mastery checkpoint

Without notes:

> A synthetic crust has $\rho = 2700\ \mathrm{kg\,m^{-3}}$, $2.0\ \mathrm{ppm}$ U,
> $8.0\ \mathrm{ppm}$ Th and $2.0\ \mathrm{wt\%}$ K, an adopted depth scale
> $h = 10\ \mathrm{km}$ and a measured surface flux $q_0 = 65\ \mathrm{mW\,m^{-2}}$.
> **(a)** Compute $A_0$ and $q_{\text{mantle}}$. **(b)** State the two assumptions
> that make $A_0 h$ the correct column integral. **(c)** Compute the mantle
> adiabat temperature at 2891 km from $T_p = 1600\ \mathrm{K}$ and compare with
> the linear approximation. **(d)** Compute the Rayleigh number for
> $\eta = 10^{22}\ \mathrm{Pa\,s}$ and decide whether the mantle would convect
> with that viscosity. **(e)** Name the one input in your chain of reasoning that
> is a pure assumption rather than a measurement or a derived quantity.

## 10. Common pitfalls

1. **Treating $H$ as a rock property.** It is per kilogram of *parent*. The rock
   value requires the element concentration and the isotopic fraction.
2. **Forgetting the neutrino fraction.** For K-40 it removes 30% of the energy;
   ignoring it biases the potassium contribution upward by nearly half.
3. **Using the constant-gradient adiabat over 2000 km.** The error is 15% and it
   is systematic, not random.
4. **Quoting $q_{\text{mantle}}$ as a measurement.** It is a difference of two
   measured numbers and carries the larger of the two relative uncertainties.
5. **Assuming the radiogenic fraction falls with heat flow.** That is true when
   $A_0$ is fixed; provinces with high $A_0$ can have high fractions *and* high
   heat flow, as the synthetic provinces here show.
6. **Reading a transition-zone thickness as a temperature.** It is a pair of
   depths and two Clapeyron slopes away from a temperature.

## 11. Related modules

- [03 Geotherms and the Earth's Heat Budget](README.md) — the module
  introduction, with the lesson map and the suggested reading paths.
- [02 Heat Flow and Its Distribution](02-heat-flow-global.md) — the same
  production, observed as a global flux.
- [03 Thermal Evolution and Secular Cooling](03-thermal-evolution.md) — what a
  radiogenic shortfall does to the planet over 4.5 Gyr.
- [12-02 Composition and Mineral Physics](../02-composition-and-mineral-physics/README.md) —
  where the mantle's trace-element budget and phase boundaries come from.
- [02-physics 05 Thermodynamics](../../02-physics/05-thermodynamics/README.md) —
  the transport equations used but not derived here.
- [05-09 Geothermal and Heat-Flow Methods](../../05-core-geophysics/09-geothermal-and-heat-flow-methods/01-heat-flow-measurement.md) —
  how $q_0$ is actually measured and what its error bars are.
