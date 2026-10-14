---
id: 02-05-03
title: "Second Law, Entropy and Irreversibility"
level: advanced
prereqs: ["02-05-02", "01-05-05"]
estimated_minutes: 90
tags: [entropy, second-law, irreversibility, carnot]
---

# Second Law, Entropy and Irreversibility

The first law says that energy is conserved. It is silent about direction: it
permits a lukewarm cup of coffee to separate spontaneously into a hot half and a
cold half, or heat to flow from a cold fault zone into a hot magma chamber. Both
of those conserve energy perfectly. Neither ever happens. The second law supplies
the missing arrow, and it does so through a quantity — entropy — that is
generated, never destroyed, in any real process.

This lesson is where thermodynamics becomes a geophysical instrument. The
direction of natural processes is not a philosophical matter: it is why the
geotherm runs downhill, why convection proceeds at all, why a geothermal plant
cannot approach unity efficiency whatever the engineer does, and why the Earth
exports entropy to space at a rate four orders of magnitude larger than the rate
at which its interior generates it.

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the second law in the entropy-production form
   $\mathrm{d}S = \delta Q/T + \delta S_{\text{gen}}$, with
   $\delta S_{\text{gen}} \ge 0$, and explain how it forbids the reverse of an
   observed process.
2. **Compute** the entropy change associated with a heat transfer and show that
   the same heat delivered at a lower temperature changes entropy more.
3. **Derive** the local entropy-production rate for conduction,
   $\sigma = k|\nabla T|^2/T^2$, and integrate it down a conductive geotherm to
   obtain $kG(1/T_0 - 1/T_H)$ per unit area.
4. **Show** that reversing the direction of heat flow in a conductor gives
   $\sigma < 0$, which is the formal statement that heat flows down the geotherm
   and never up.
5. **Apply** the Carnot bound to geothermal conversion and explain the gap
   between it and real plant efficiency as irreversibility.
6. **Account** for the Earth's entropy budget: interior conduction, secular
   cooling, and the degradation of solar radiation to terrestrial infrared.

## Prerequisites

- [02-05-02 First Law, Work and Energy Balances](./02-first-law.md) — the energy
  bookkeeping that entropy supplements.
- [01-05-05 Integration Techniques and Definite Integrals](../../01-mathematics/05-single-variable-calculus/05-integration.md)
  — the integrals of §3.2.

## 1. Definitions and statements

### 1.1 The entropy function

For a reversible transfer of heat $\delta Q_{\text{rev}}$ at temperature $T$,

$$\mathrm{d}S \equiv \frac{\delta Q_{\text{rev}}}{T} . \tag{1}$$

$S$ is a state function: it depends only on the state of the system, not on the
path taken to reach it. For a real (irreversible) process,

$$\mathrm{d}S = \frac{\delta Q}{T_{\text{boundary}}} + \delta S_{\text{gen}},
\qquad \delta S_{\text{gen}} \ge 0 , \tag{2}$$

where $T_{\text{boundary}}$ is the temperature *at the boundary where the heat
crosses*. For an isolated system ($\delta Q = 0$),

$$\mathrm{d}S \ge 0 \quad\text{and}\quad S\ \text{is maximal at equilibrium.}
\tag{3}$$

This is the form that matters. Entropy is not "disorder" in any rigorous sense;
it is the log of the number of microscopic states consistent with the
macroscopic state, $S = k_B \ln \Omega$ with $k_B$ the Boltzmann constant
(exact: $1.380\,649\times10^{-23}$ J K⁻¹), and the second law is the statement
that a system explores the states available to it rather than the ones that are
not.

### 1.2 The classical statements, and their geophysical readings

| Statement | Content | Geophysical reading |
|---|---|---|
| Clausius | Heat never flows spontaneously from cold to hot | The geotherm runs downhill; a hot body cannot be warmed by a colder one |
| Kelvin–Planck | No cyclic device converts heat entirely into work | Geothermal efficiency is bounded by Carnot, never unity |
| Entropy | $\mathrm{d}S_{\text{universe}} \ge 0$ | Every irreversible process leaves a permanent trace in the entropy books |
| Carathéodory | Every state has adiabatically inaccessible neighbours | The existence of a temperature function at all |

The four are equivalent. The entropy statement is the one that can be
*differentiated* and applied pointwise in a continuum, which is why it is the
working form in geophysics.

## 2. Derivations

### 2.1 Entropy production in a temperature difference

Heat $Q$ crossing from a hot boundary at $T_h$ to a cold boundary at $T_c$ causes
the hot reservoir to lose entropy $Q/T_h$ and the cold one to gain $Q/T_c$.
Because $T_c < T_h$,

$$\sigma = Q\left(\frac{1}{T_c} - \frac{1}{T_h}\right) \ge 0 . \tag{4}$$

Equation (4) is the whole of the second law in its simplest form. Three readings:

- The entropy produced per unit heat transferred is zero only when
  $T_h = T_c$, i.e. in the limit of a vanishing gradient, in which case the
  flux also vanishes. **All real heat transport produces entropy.**
- The production is *larger* for a bigger temperature drop. A given heat flux
  down a steep gradient is more irreversible than the same flux down a shallow
  one.
- The production is zero at $T_h = T_c$ but the second law does not forbid a
  finite flux at a finite $\Delta T$; it only forbids a negative one.

### 2.2 Local entropy production for conduction

The continuum version of equation (4). The heat flux density is
$\mathbf{q} = -k\nabla T$, and the entropy flux density is $\mathbf{q}/T$. The
entropy balance for a volume element with no internal entropy source other than
irreversibility is

$$\rho\frac{\partial s}{\partial t} + \nabla\cdot\left(\frac{\mathbf{q}}{T}\right)
= \sigma , \qquad \sigma \ge 0 , \tag{5}$$

with $s$ the specific entropy. Substituting $\mathbf{q} = -k\nabla T$ and using
$\nabla\cdot(k\nabla T) = \rho c_p\,\partial T/\partial t$ for constant $k$:

$$\sigma = k\frac{|\nabla T|^2}{T^2} . \tag{6}$$

Note three properties:

- $\sigma \ge 0$ automatically, and it vanishes only when $\nabla T = 0$ — the
  same limit in which the flux vanishes. Reversing the flux direction does not
  change $|\nabla T|^2$, which is why the naive reversal argument must be made
  using equation (4), where the *sign* of the heat matters.
- $\sigma$ scales as the square of the gradient but only as $1/T^2$: a steep
  gradient in cold rock produces far more entropy than the same gradient in hot
  rock.
- Viscous dissipation adds a term $\tau_{ij}\dot\varepsilon_{ij}/T$, which is
  negligible in the lithosphere and dominant in a shear zone; magnetic and
  chemical irreversibilities add analogous terms, and each has the same structure
  (flux × conjugate force / $T$).

### 2.3 Integrating down a conductive geotherm

Take a linear geotherm $T(z) = T_0 + Gz$ over a column of thickness $H$ with
constant $k$. Then $|\nabla T| = G$ and

$$\Sigma = \int_0^H \sigma\,\mathrm{d}z = kG^2\int_0^H
\frac{\mathrm{d}z}{(T_0 + Gz)^2}
= kG^2\cdot\frac{1}{G}\left(\frac{1}{T_0} - \frac{1}{T_H}\right), \tag{7}$$

using $\int \mathrm{d}z/(T_0+Gz)^2 = -(1/G)/(T_0+Gz)$. So

$$\boxed{\ \Sigma = kG\left(\frac{1}{T_0} - \frac{1}{T_H}\right)\ }
\qquad [\mathrm{W\,m^{-2}\,K^{-1}}] . \tag{8}$$

**Always check the units of a result like this.** $kG(1/T_0 - 1/T_H)$:
$\mathrm{W\,m^{-1}K^{-1}}\cdot\mathrm{K\,m^{-1}}\cdot\mathrm{K^{-1}} =
\mathrm{W\,m^{-2}K^{-1}}$ ✓, an entropy production *per unit area* of column.

With $T_0 = 283$ K, $T_H = 1600$ K, $H = 150$ km and $k = 3.0$ W m⁻¹ K⁻¹:
$G = 8.78$ K km⁻¹ and

$$\Sigma = 3.0\times8.78\times10^{-3}\left(\frac{1}{283} -
\frac{1}{1600}\right) = 7.66\times10^{-5}\ \mathrm{W\,m^{-2}\,K^{-1}}
= 7.66\times10^{-5}\ \mathrm{W\,m^{-2}\,K^{-1}} . \tag{9}$$

Multiplied by the Earth's surface area (5.10 × 10¹⁴ m², nominal) this gives
3.9 × 10¹⁰ W K⁻¹. Hold that number; it is four orders of magnitude smaller than
the radiative figure in §3.4.

### 2.4 Carnot efficiency, and why it is not achievable

For any device operating between reservoirs at $T_h$ and $T_c$, reversibility
gives the maximum work fraction

$$\eta_{\text{Carnot}} = 1 - \frac{T_c}{T_h} , \tag{10}$$

and no real device can exceed it. For a geothermal resource at 200 °C and a
25 °C sink, $\eta_{\text{Carnot}} = 1 - 323.15/473.15 = 0.370$. Real flash plants
achieve roughly 12 per cent, and binary plants 8–10 per cent — 40 to 60 per cent
of the bound. The gap is entirely irreversibility: finite-rate heat exchangers,
turbine friction, pressure drops, and the fact that the reservoir itself
depressurises during production.

Two structural consequences for geothermal energy:

- **Low temperature is the fundamental constraint.** A resource at 90 °C has
  $\eta_{\text{Carnot}} = 0.179$; no engineering can lift it to the flash-plant
  range.
- **Efficiency and power trade off.** Driving a plant harder to extract more
  power lowers the outlet temperature and reduces efficiency; the optimum is a
  second-law problem, not a reservoir-size problem.

## 3. Applications

### 3.1 The same heat at different temperatures

One megajoule delivered at 300 K changes entropy by 3333 J K⁻¹; the same
megajoule at 3000 K changes it by 333 J K⁻¹. **Low-temperature heat is
entropy-rich and work-poor.** This single inequality explains why domestic space
heating is cheap and electricity is expensive, and why a geothermal resource's
*value* depends on its temperature far more sharply than on its flow rate.

### 3.2 Entropy of fusion

Crystallising basalt releases $L = 4\times10^5$ J kg⁻¹ at about $T_m = 1500$ K,
so the entropy change is

$$\Delta s_{\text{fus}} = \frac{L}{T_m} = \frac{4\times10^5}{1500}
= 267\ \mathrm{J\,kg^{-1}\,K^{-1}} . \tag{11}$$

Rate this against the entropy tied up in simply heating the rock: over 1200 K at
$c_p = 840$ J kg⁻¹ K⁻¹, $\Delta s = c_p \ln(T_2/T_1) = 840\ln(1500/300) = 1352$
J kg⁻¹ K⁻¹ — a ratio of 0.20 against the sensible part alone, or about one sixth
of the *total* $\Delta s$ of $267/(267+1352) = 0.165$. Either way, the front
is where a disproportionate share of the entropy production is concentrated. This is why crystallisation releases its heat at nearly constant
temperature: the process is entropy-limited, not energy-limited, at that step.

### 3.3 Secular cooling

The Earth loses more heat than it generates (lesson [06](./06-geotherms.md)),
so the interior is cooling. The entropy production associated with the deficit is
of order

$$\dot S_{\text{secular}} \approx \dot Q\left(\frac{1}{T_{\text{cold}}} -
\frac{1}{T_{\text{hot}}}\right) . \tag{12}$$

With a 31 TW deficit, $T_{\text{cold}} = 283$ K and $T_{\text{hot}} = 1600$ K,
this is 9.0 × 10¹⁰ W K⁻¹, larger than conduction but still small on the scale of
§3.4. The implied whole-mantle cooling rate at that deficit is
$\dot Q/(Mc_p) = 6.2\times10^{-15}$ K s⁻¹ $= 196$ K per 10⁹ yr for
$M = 4.0\times10^{24}$ kg and $c_p = 1250$ J kg⁻¹ K⁻¹ — a nominal figure with a
stated inventory, not a measurement.

### 3.4 The Earth's dominant entropy production

The Earth absorbs sunlight at the photospheric temperature and re-emits it at its
own much lower effective temperature. With an adopted solar constant
$S = 1361$ W m⁻² and albedo 0.30 (both nominal), the absorbed flux per unit area
is $S(1-a)/4 = 238.175$ W m⁻², giving

$$T_e = \left(\frac{S(1-a)}{4\sigma}\right)^{1/4} = 254.578\ \text{K}
= -18.57\ ^\circ\text{C} \tag{13}$$

with $\sigma = 5.670\,374\,419\times10^{-8}$ W m⁻² K⁻⁴ (exact). At steady state
the climate system's internal entropy is constant, so the entropy it produces
equals the entropy it exports:

$$\dot\Sigma_{\text{rad}} = F_{\text{abs}}\left(\frac{1}{T_e} -
\frac{1}{T_\odot}\right) = 238.175\left(\frac{1}{254.578} -
\frac{1}{5772}\right) = 0.8943\ \mathrm{W\,m^{-2}\,K^{-1}} . \tag{14}$$

Globally that is **4.56 × 10¹⁴ W K⁻¹**, which is

$$\frac{4.56\times10^{14}}{3.9\times10^{10}} \approx 1.2\times10^{4} \tag{15}$$

times the solid Earth's conductive entropy production. Both are second-law
statements and both are quantitative, which is the point: the planet's internal
heat engine is enormous in energy and small in entropy production, while its
radiation budget is the reverse. Anyone who claims that the Earth's internal
heat "drives the climate" is claiming the wrong engine by four orders of
magnitude.

## 4. Physical interpretation

**Entropy production is the tax on every real process.** Equation (4) says the
tax rate is set by the temperature contrast. A process that runs on a small
contrast pays little per unit of heat but moves little heat; a process that moves
a lot of heat across a large contrast pays a lot. There is no configuration that
moves heat at a finite rate with zero tax.

**The direction of the geotherm is not an assumption.** It follows from
equation (4). If the Earth's interior were colder than its surface, heat would
have to flow inward, the entropy production would be negative, and the state
would be impossible. Every thermal model that runs the geotherm uphill is
therefore wrong before any data are considered, which is a much stronger check
than comparing with observations.

**Reversibility is a limit, not a mode of operation.** A reversible process is a
sequence of states each infinitesimally displaced from equilibrium. It carries no
flux, takes infinite time, and never occurs. It is a boundary that real
efficiencies approach from below, and it is useful only as a bound.

**Irreversibility is where the interesting geophysics lives.** The entropy
produced by mantle convection, by viscous dissipation in a shear zone, by
chemical diffusion and by the degradation of solar photons is the quantitative
measure of how far from equilibrium the Earth is — and therefore of how much work
the system can do.

## 5. Assumptions and regime of validity

| Approximation | Statement | What breaks outside it |
|---|---|---|
| Local thermodynamic equilibrium | Each element has a temperature and entropy | Extremely fast transients and rarefied gases; not relevant in the solid Earth below ~100 km altitude |
| Continuum description | $\sigma$ is a density, defined at a point | Fracture and grain-scale heterogeneity smaller than the averaging volume |
| Constant $k$ in equation (8) | Analytic integration is possible | Real conductivities vary with temperature by a factor of 2 across the lithosphere; integrate numerically |
| Linear geotherm | Valid for §3.2 only | The real geotherm is curved by heat production (lesson 06) |
| Steady state | Equation (14) treats the Earth's entropy as constant | On glacial–interglacial timescales the planetary heat content changes and there is a storage term |
| Blackbody radiation | Equation (14) treats the Earth as an opaque emitter | The atmosphere is partially transparent; the real budget needs radiative transfer |
| Single-component phase change | $\Delta s = L/T_m$ | Multi-component crystallisation releases $L$ over an interval; integrate instead |

## 6. Units and dimensional analysis

- $S$: J K⁻¹. Specific entropy $s$: J kg⁻¹ K⁻¹. $\Delta S = Q/T$:
  $\mathrm{J/K}$ ✓ — note that entropy has the same units as heat capacity, which
  is not a coincidence but frequently causes confusion.
- $\sigma$ in equation (6): $k|\nabla T|^2/T^2$ is
  $\mathrm{W\,m^{-1}K^{-1}}\cdot\mathrm{K^2m^{-2}}\cdot\mathrm{K^{-2}} =
  \mathrm{W\,m^{-3}}$, a volumetric entropy production rate. Integrating over
  depth gives $\mathrm{W\,m^{-2}K^{-1}}$ ✓ as in equation (8).
- $\eta_{\text{Carnot}}$: dimensionless, and **must be computed in kelvin**.
  Using 200 and 25 in °C gives 0.875 instead of 0.370 — a catastrophic error that
  is easy to make and produces an over-optimistic design.
- $\mathrm{d}T_e/\mathrm{d}S = T_e/(4S) = 0.0468$ K per W m⁻² for the adopted
  solar constant, so a 1 per cent change in $S$ moves $T_e$ by 0.64 K. The
  fourth power is what makes the surface temperature stable against modest
  forcing changes and catastrophic against large ones.
- **A useful anchor**: entropy production in the solid Earth is of order
  10¹⁰ W K⁻¹; the radiation budget is of order 10¹⁴ W K⁻¹. Any computed
  interior entropy production above 10¹² W K⁻¹ is a unit or a factor-of-$T$ error.

## 7. Python demonstration

[`code/second_law_demo.py`](./code/second_law_demo.py) computes entropy changes,
the entropy production of conduction, the integral (8), Carnot limits and the
Earth's entropy budget. Observed output:

```text
       Q (J)     T (K)        dS (J/K)
   1.000e+06       300    3.333333e+03
   1.000e+06      1000    1.000000e+03
   1.000e+06      3000    3.333333e+02
   4.080e+18      1500    2.720000e+15
```

```text
   T_h (K)   T_c (K)    q (W/m2)    sigma (W/m2/K)
    1600.0     283.0      0.0650      1.890570e-04
     800.0     283.0      0.0650      1.484320e-04
     373.0     283.0      0.0650      5.541924e-05
    1600.0    1600.0      0.0650      0.000000e+00
```

```text
  G = 8.7800 K/km
  sigma = k G (1/T0 - 1/T_H) = 7.661170e-05 W m^-2 K^-1
  globally: 3.9072e+10 W/K
```

```text
   T_h (C)   T_c (C)   T_h (K)   T_c (K)   eta_Carnot  eta_real (nominal)
     200.0      25.0    473.15    298.15       0.3699                0.12
     150.0      25.0    423.15    298.15       0.2954                0.10
     300.0      25.0    573.15    298.15       0.4798                0.20
      90.0      25.0    363.15    298.15       0.1790                0.06
```

```text
  Entropy of fusion of basalt: L/T_m = 4.000e+05/1500 = 266.67 J kg^-1 K^-1
  Implied mantle cooling rate dT/dt = Q/(M c_p) = 6.2000e-15 K/s = 195.7 K per 10^9 yr

    absorbed flux S(1-a)/4 = 238.1750 W/m2
    effective radiating temperature = 254.5781 K = -18.57 C
    entropy produced per unit area = 0.894304 W m^-2 K^-1
    globally = 4.5609e+14 W/K
```

### What to observe

| Observation | Consequence |
|---|---|
| The same megajoule gives 3333 J K⁻¹ at 300 K and 333 J K⁻¹ at 3000 K | Temperature, not energy, sets the value of heat |
| The last conduction row gives exactly zero | Entropy production vanishes only when the flux does |
| 1.89 × 10⁻⁴ > 1.48 × 10⁻⁴ > 5.54 × 10⁻⁵ W m⁻² K⁻¹ | A steeper temperature drop produces more entropy for the same flux |
| Lithospheric conduction gives 3.9 × 10¹⁰ W K⁻¹ | The solid Earth's irreversible tax is modest |
| Radiation gives 4.56 × 10¹⁴ W K⁻¹ | The climate system dominates the planet's entropy production by four orders |
| Carnot 0.3699 against a realised 0.12 | Real conversion is at a third of the bound; the gap is irreversibility |

> **Breaking exercise.** Set the hot boundary in §2 of the demo to 290 K (just
> 7 K above the cold one) and predict, before running, the new entropy production.
> Then explain why the steady geotherm cannot have a small temperature difference
> at every depth — the flux would require a vanishing gradient, and a vanishing
> gradient cannot carry 65 mW m⁻² through rock.

## 8. Common mistakes

1. **Treating entropy as "disorder".** Entropy is a counting of microscopic
   states and a state function with units. The slogan is a metaphor, and it fails
   whenever it is used quantitatively.
2. **Using °C in the Carnot formula.** $\eta = 1 - T_c/T_h$ in kelvin, always.
3. **Reporting entropy production without saying where.** A rate per unit volume,
   per unit area and globally differ by many orders of magnitude; every figure in
   equations (6), (8) and (14) carries a different normalization.
4. **Assuming low-temperature heat is worthless.** It is entropy-rich and
   work-poor, but it is still energy: district heating is a legitimate use of a
   90 °C resource, and it is the *work* fraction that is small.
5. **Believing a heat pump violates the second law.** It does not: it moves heat
   uphill at the cost of work, and the relevant quantity is the coefficient of
   performance, which is bounded by $T_h/(T_h - T_c)$.
6. **Concluding that the second law forbids convection.** Convection is driven by
   a buoyancy force doing work; it *produces* entropy and is entirely legal. What
   is forbidden is a net spontaneous heat flux from cold to hot.
7. **Forgetting that equation (6) is quadratic in the gradient.** Doubling the
   gradient quadruples the entropy production, which is why lithospheric
   conduction is a larger entropy source than the much larger convective flux
   through the mantle.
8. **Using a reversible relation for an irreversible process.** $\mathrm{d}S =
   \delta Q/T$ is only valid for reversible heat transfer; the general statement
   is equation (2).

## 9. Real-world applications

- **Geothermal plant design.** The Carnot bound sets the resource's ceiling and
  the second law tells the engineer which irreversibilities to attack
  ([05-09/03](../../05-core-geophysics/09-geothermal-and-heat-flow-methods/03-geothermal-exploration.md)).
- **Heat pumps and district heating.** The coefficient of performance of a heat
  pump is a second-law quantity, and its limit is the reason ground-source
  systems are viable at all.
- **Chemical and petrological direction.** Which reactions proceed, in which
  order, and how far from equilibrium a metamorphic assemblage is are all
  entropy-production questions; they are the content of
  [02-05-07](./07-phase-equilibria.md).
- **Mantle convection and dissipation.** The entropy produced by viscous
  dissipation is the quantity that appears in the entropy budget of a convecting
  mantle and in the mechanical-to-thermal conversion that heats shear zones.
- **Climate energetics.** The greenhouse effect is a radiative-transfer problem,
  but the planetary energy and entropy budgets of §3.4 are the framework that
  makes "radiative forcing" an energy statement
  ([16-02/03](../../16-atmosphere-climate/02-radiation-and-energy-balance/03-greenhouse-effect.md)).
- **Irreversible seismology.** The anelastic attenuation of seismic waves is
  entropy production, and the quality factor $Q$ is its quantitative measure
  ([02-03-10](../03-oscillations-and-waves/10-attenuation.md)).

## 10. Further reading

- **Fermi, E. *Thermodynamics* (Dover reprint).** The most compact rigorous
  derivation of the Carnot bound and the entropy inequality. Level: beginner.
- **Callen, H. B. *Thermodynamics and an Introduction to Thermostatistics*
  (2nd ed., Wiley).** Entropy as a fundamental relation, the Legendre transforms,
  and local equilibrium in a continuum. Level: intermediate to advanced.
- **Prigogine, I. *Introduction to Thermodynamics of Irreversible Processes*
  (Interscience).** The derivation of $\sigma = k|\nabla T|^2/T^2$ and its
  general flux–force structure; the source of the formalism in §2.2. Level:
  advanced.
- **de Groot, S. R., & Mazur, P. *Non-Equilibrium Thermodynamics* (Dover).** The
  systematic treatment of coupled irreversible processes, including
  thermodiffusion, which matters in magma and groundwater. Level: advanced.
- **Turcotte, D. L., & Schubert, G. *Geodynamics* (3rd ed., Cambridge University
  Press, 2014).** Mantle convection as an entropy-producing process, and the
  thermal-evolution context of §3.3. Level: graduate.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 11. Related lessons

- [02 First Law, Work and Energy Balances](./02-first-law.md) — the conservation
  law that the second law supplements.
- [04 Heat Conduction, Fourier's Law and Thermal Diffusivity](./04-heat-conduction.md)
  — the transport law whose irreversibility is quantified here.
- [05 Convection, Radiation and Combined Heat Transfer](./05-convection-radiation.md)
  — the transport that dominates the Earth's interior and its radiation budget.
- [02-03-10 Attenuation, Absorption and the Quality Factor Q](../03-oscillations-and-waves/10-attenuation.md)
  — entropy production in a seismic wave.
- [02-10-03 Radiative Transfer, Blackbody Radiation and Kirchhoff's Law](../10-optics-and-photometry/03-radiative-transfer.md)
  — the physics behind equation (14).
- [16-atmosphere-climate/02 Radiation and Energy Balance](../../16-atmosphere-climate/02-radiation-and-energy-balance/README.md)
  — the planetary budget in full.

Exercises:
[`exercises/03-second-law-exercises.md`](./exercises/03-second-law-exercises.md)
and
[`exercises/03-second-law-solutions.md`](./exercises/03-second-law-solutions.md).

## Self-assessment checklist

- [ ] I can write the entropy-production form of the second law and say what the
      inequality means. (§1.1)
- [ ] I can state the four classical formulations and use the entropy one
      quantitatively. (§1.2)
- [ ] I can compute the entropy produced when heat crosses a temperature
      difference, including its sign. (§2.1)
- [ ] I can derive $\sigma = k|\nabla T|^2/T^2$ and integrate it down a linear
      geotherm to get $kG(1/T_0 - 1/T_H)$. (§2.2, §2.3)
- [ ] I can construct the argument that heat cannot flow up the geotherm,
      using the sign of the entropy production. (§2.1, §4)
- [ ] I can compute a Carnot bound in kelvin and compare it with real plant
      performance. (§2.4, §7)
- [ ] I can compute the entropy of fusion of a rock and rate it against the
      sensible entropy change. (§3.2)
- [ ] I can account for the Earth's entropy budget across conduction, secular
      cooling and radiation, and explain which dominates. (§3.3, §3.4)
