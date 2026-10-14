---
id: 02-11-04
title: "Atmospheric Structure, Hydrostatic Balance and Lapse Rates"
level: advanced
prereqs: ["02-06-01", "02-11-01", "02-05-01"]
estimated_minutes: 90
tags: [hydrostatic-balance, scale-height, lapse-rate, atmospheric-stability]
---

# Atmospheric Structure, Hydrostatic Balance and Lapse Rates

Everything that governs the interior of the Earth — a **density gradient set by
self-compression**, a pressure that is the integral of that gradient, a
temperature that follows an adiabat — governs the atmosphere too, and it governs
it with the *same two equations*. This lesson is the deliberate mirror of lesson
[01](./01-pressure-density-depth.md), and the contrast between the two cases is
the point.

$$\frac{\mathrm{d}P}{\mathrm{d}z} = -\rho g \quad\text{in both cases},$$

but in the Earth's interior the density is a nearly fixed material property and
the pressure rises to $10^{11}$ Pa over 6371 km, whereas in the atmosphere the
density is set by the ideal-gas law and the *whole* atmosphere is a thin shell:
98.8 per cent of its mass lies within 30 km, which is 0.47 per cent of the Earth's
radius. The atmosphere is a two-dimensional skin on a three-dimensional body, and
that geometric fact is why its physics looks so different despite sharing an
equation.

Four quantities organise the whole subject, and this lesson derives each of them:

$$H = \frac{RT}{g}\ \text{(scale height)}, \qquad
\Gamma_d = \frac{g}{c_p}\ \text{(dry adiabatic lapse rate)},$$

$$\theta = T\left(\frac{p_0}{p}\right)^{R/c_p}\ \text{(potential temperature)},
\qquad
N^2 = \frac{g}{T}\left(\Gamma_d - \Gamma\right)\ \text{(buoyancy frequency)}.$$

The first two are computed in §1 and §2, the third and fourth in §2.3–§2.4, and
§3 checks the whole apparatus against the standard atmosphere's defined
temperature profile — a case where the answer is known in advance and the
integration can be verified rather than merely believed.

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** hydrostatic balance for a compressible gas, close the system with
   the ideal-gas law, and derive the isothermal exponential atmosphere.
2. **Compute** the scale height $H = RT/g$ and state what fraction of the
   atmosphere's mass lies within one, two and three scale heights.
3. **Derive** the dry adiabatic lapse rate $\Gamma_d = g/c_p$ from the first law
   and hydrostatic balance, and verify it a second way from
   $(\gamma-1)g/(\gamma R)$.
4. **Derive** the power-law solution $p = p_0(T/T_0)^{g/(\Gamma R)}$ for a
   constant lapse rate, and verify a numerical integration against it.
5. **Define** potential temperature and buoyancy frequency, and use them to
   explain why the stratosphere is almost immune to vertical mixing.
6. **Integrate** hydrostatic balance through the standard atmosphere's defined
   temperature profile and reproduce its pressures.
7. **Explain** why the observed tropospheric lapse rate (6.5 K/km) is shallower
   than the dry adiabat (9.8 K/km), and what would change if it were not.
8. **Estimate** the atmosphere's total mass from surface pressure alone.

## Prerequisites

- [02-06-01 Fluid Statics, Pressure and Buoyancy](../06-fluid-mechanics/01-fluid-statics.md)
  — hydrostatic balance in a fluid, and the buoyancy principle used in §2.4.
- [02-11-01 Pressure, Density and Gravity Inside the Earth](./01-pressure-density-depth.md)
  — the same equation in a self-gravitating incompressible body; the contrast is
  the substance of this lesson.
- [02-05-01 Temperature, Heat, Internal Energy and Specific Heat](../05-thermodynamics/01-temperature-and-heat.md)
  — enthalpy, $c_p$ and why an adiabatic process is isentropic.
- [26-02-03 Physical Constants and Earth Parameters](../../26-reference-library/02-symbols-and-units/03-constant-handbook.md)
  — §1 for the exact value of the standard atmosphere, §3.6 for the properties
  of air.

## 1. Hydrostatic balance in a compressible gas

### 1.1 The same equation

Consider a slab of air of unit horizontal area and thickness $\mathrm{d}z$. Its
weight is $\rho g\,\mathrm{d}z$, and the pressure difference across it is
$\mathrm{d}P$. Equilibrium requires

$$\frac{\mathrm{d}P}{\mathrm{d}z} = -\rho g, \qquad (1)$$

which is identical to lesson [01](./01-pressure-density-depth.md) equation (1)
with $z$ measured upward. Two differences from the interior case matter.

**There is no self-gravity.** The atmosphere's mass is
$5.27\times10^{18}$ kg — one millionth of the Earth's — so $g$ is constant to
within a part in $10^3$ over the whole atmosphere. We may treat $g$ as fixed
and, for most purposes, the atmosphere as plane-parallel.

**Density is a variable, not a material property.** In the mantle, $\rho$ is set
by mineralogy and compression and changes by a factor of 5 over 6371 km. In the
atmosphere, $\rho$ is set by the ideal-gas law and changes by a factor of
$\sim10^3$ over 50 km. So equation (1) is not a relationship between pressure and
a known density; it is one equation in two unknowns, and a *closure* is
required.

### 1.2 The closure: the ideal-gas law

For air, $p = \rho R_{\text{air}} T$ with the specific gas constant

$$R_{\text{air}} = \frac{R}{M_{\text{air}}}
= \frac{8.314\,462\,618\,153\,24}{0.028\,9644}
= 287.058\ \text{J kg}^{-1}\text{K}^{-1}.$$

Here $R = N_Ak_B$ is exact (both $N_A$ and $k_B$ are SI defining constants), and
$M_{\text{air}} = 0.028\,9644$ kg mol⁻¹ is the **nominal** molar mass of dry air —
a representative value for a mixture whose composition varies slightly. The
specific gas constant is therefore a nominal quantity built on an exact one.

Eliminating $\rho$ from equation (1):

$$\frac{\mathrm{d}P}{P} = -\frac{g}{R_{\text{air}}T}\,\mathrm{d}z. \qquad (2)$$

Every atmospheric equilibrium structure emerges from integrating equation (2)
under an assumption about $T(z)$, and the whole structure of this lesson is the
choice of that assumption.

### 1.3 The scale height

If $T$ is constant, equation (2) integrates at once:

$$P = P_0\exp\!\left(-\frac{z}{H}\right), \qquad
H \equiv \frac{R_{\text{air}}T}{g}. \qquad (3)$$

$H$ is the **pressure scale height**: the height over which the pressure falls by
a factor of $e$. With $T = 288.15$ K (the standard atmosphere's definition of
15 °C) and $g = 9.806\,65$ m/s² (exact by definition):

$$H = \frac{287.058\times288.15}{9.80665} = 8434.7\ \text{m} \approx 8.435\ \text{km}.$$

The atmosphere's pressure therefore halves every $H\ln 2 = 5.85$ km in an
isothermal model, and 63, 86 and 95 per cent of its mass lie within one, two and
three scale heights — the last being 25.3 km. That is the number to carry around:
**the atmosphere is a 25 km skin.**

Note how $H$ behaves: it grows with temperature and falls with gravity. Two
consequences will be used in lesson [05](./05-planetary-physics.md): a hot
atmosphere is a *thick* atmosphere at fixed pressure, and a high-gravity body has
a compressed one at the same temperature.

The ocean provides the contrast that proves the point. Water is essentially
incompressible, so its pressure gradient is $\rho g = 9.79$ kPa m⁻¹ and one
atmosphere is 10.3 m of water. There is no scale height for an incompressible
fluid; equation (3) requires an ideal gas, and applying it to water is a category
error even though the numbers can be computed.

## 2. The dry adiabatic lapse rate

### 2.1 Derivation from the first law

A parcel of air that rises without exchanging heat with its surroundings obeys
$\mathrm{d}h = v\,\mathrm{d}P$ (the first law with $\mathrm{d}q = 0$, where $h$
is specific enthalpy and $v = 1/\rho$). For an ideal gas,
$\mathrm{d}h = c_p\,\mathrm{d}T$, and hydrostatic balance in the environment
gives $\mathrm{d}P = -\rho g\,\mathrm{d}z$. Therefore

$$c_p\,\mathrm{d}T = \frac{1}{\rho}(-\rho g\,\mathrm{d}z) = -g\,\mathrm{d}z,$$

$$\boxed{\ \Gamma_d \equiv -\frac{\mathrm{d}T}{\mathrm{d}z} = \frac{g}{c_p}\ }
\qquad (4)$$

The four assumptions are worth naming, because each of them can be violated:
adiabatic (no heat exchange), reversible (no dissipation), hydrostatic
equilibrium in the environment, and an ideal gas with constant $c_p$.

With $c_p = 1005$ J kg⁻¹ K⁻¹ (nominal for air near 15 °C):

$$\Gamma_d = \frac{9.806\,65}{1005} = 9.758\times10^{-3}\ \text{K m}^{-1}
= 9.758\ \text{K km}^{-1}.$$

**A second derivation, as a check.** For an ideal gas with constant $\gamma =
c_p/c_v$, $c_p = \gamma R/(\gamma-1)$, so

$$\Gamma_d = \frac{g}{c_p} = \frac{\gamma-1}{\gamma}\cdot\frac{g}{R}
= \frac{0.4}{1.4}\times\frac{9.806\,65}{287.058} = 9.760\ \text{K km}^{-1},$$

agreeing to 0.02 per cent — the residual being the difference between the nominal
$c_p = 1005$ and the value implied by $\gamma = 1.4$ and $R_{\text{air}}$. Two
routes, one answer; that is the level of checking expected of a derived constant.

### 2.2 The observed profile, and why it differs

The **observed mean tropospheric lapse rate, as defined in the standard
atmosphere, is 6.5 K km⁻¹** — a factor of 1.50 smaller than the dry adiabat.
Three effects account for the difference.

- **Latent heat.** Rising air that is saturated condenses water, releasing latent
  heat and warming the parcel as it rises. That reduces the lapse rate. This is
  the *moist* adiabatic lapse rate, and because it depends on the saturation
  specific humidity — hence on temperature and pressure through the
  Clausius–Clapeyron relation — it is not a constant. It is always shallower than
  the dry adiabat, and the difference grows with temperature and humidity. The
  full treatment is
  [16-atmosphere-climate/01-03](../../16-atmosphere-climate/01-atmospheric-structure-and-thermodynamics/03-thermodynamic-processes.md).
- **Radiative constraint.** The outgoing longwave flux must balance the absorbed
  solar flux, and the profile that does so in radiative equilibrium is
  *steeper* than the dry adiabat — it would be convectively unstable. The
  atmosphere therefore convects until the profile is marginally stable against
  the operative (moist) adiabat, and the observed profile is the result.
- **Horizontal heat transport.** The mean profile is not a single adiabat at all;
  it is an average over tropical deep convection, mid-latitude baroclinic eddies
  and polar radiative cooling, all at different latitudes and seasons.

The observed 6.5 K km⁻¹ is a *defined characteristic of the standard atmosphere*,
not a measurement of a particular place or day. Actual tropospheric lapse rates
range from near-dry-adiabatic over deserts and in descending föhn winds to well
below 6.5 K/km in the moist tropics, and the tropopause height varies from about
8 km in polar winter to about 16 km in the tropics.

**The sharpest way to see what the lapse rate means.** It sits *between* the two
extremes: it is shallower than the dry adiabat and steeper than isothermal. A
profile steeper than 9.758 K/km would be convectively unstable and would overturn
in minutes; one shallower than zero (isothermal) would suppress convection
entirely. The actual value being 1.5 times shallower than the dry adiabat is the
quantitative content of "the troposphere is a moist-convecting layer".

### 2.3 Potential temperature

Define the **potential temperature**

$$\theta \equiv T\left(\frac{p_0}{p}\right)^{R/c_p}, \qquad p_0 = 101\,325\ \text{Pa}. \qquad (5)$$

The physical meaning: $\theta$ is the temperature a parcel would have if moved
adiabatically to the reference pressure $p_0$. Differentiating along an adiabat
gives $\mathrm{d}\theta = 0$, so **an adiabatic process is a line of constant
$\theta$**, and any *increase* of $\theta$ with height means the stratification
is stable — a parcel displaced upward finds itself denser than its surroundings
and sinks back.

From the integrated form of equation (2) with a constant lapse rate
$\Gamma = -\mathrm{d}T/\mathrm{d}z$,

$$\ln\frac{p}{p_0} = \frac{g}{R\Gamma}\ln\frac{T}{T_0}
\qquad\Longrightarrow\qquad
p = p_0\left(\frac{T}{T_0}\right)^{g/(R\Gamma)}, \qquad (6)$$

which is the *power law* that replaces the exponential when the lapse rate is
non-zero. For the standard troposphere, $g/(R\Gamma) = 9.80665/(0.287058\times6.5)
= 5.256$ — the familiar exponent of the tropospheric barometric formula. Two
extreme cases are worth holding in mind: $\Gamma = 0$ recovers equation (3), and
$\Gamma = \Gamma_d$ gives an atmosphere that is neutrally stable to dry
convection.

### 2.4 The buoyancy frequency

Let a parcel be displaced upward by $\delta z$ adiabatically. Its internal
temperature change is $-\Gamma_d\,\delta z$; the environment's is
$-\Gamma\,\delta z$. The parcel's relative buoyancy is therefore proportional to
$(\Gamma_d - \Gamma)\delta z$, and Newton's second law gives simple harmonic motion
with

$$N^2 = \frac{g}{\theta}\frac{\mathrm{d}\theta}{\mathrm{d}z}
= \frac{g}{T}\left(\Gamma_d - \Gamma\right). \qquad (7)$$

$N$ is the **Brunt–Väisälä frequency**, the frequency at which a displaced parcel
oscillates. The consequences are immediate and complete:

- $N^2 > 0$: **stable**. The parcel oscillates; the timescale is $2\pi/N$.
- $N^2 = 0$: **neutral**. The parcel stays where it is put.
- $N^2 < 0$: **unstable**. The parcel accelerates away and convection follows.
  This is the Schwarzschild criterion for the interior of a star and the
  Rayleigh–Bénard criterion's local ancestor for the atmosphere.

Equation (7) is *the* single number that decides whether a layer mixes, and it is
why $N$ appears in every atmospheric and oceanic-dynamics model downstream.

## 3. The real temperature profile

### 3.1 The layers

The standard atmosphere is defined by a piecewise-linear temperature profile: a
list of geopotential heights at which the lapse rate changes, with
$T_0 = 288.15$ K and $p_0 = 101\,325$ Pa at sea level. Both of those are exact
defining values of the standard; the layer structure is:

| Base height (km) | Lapse rate (K/km) | Temperature at the top (K) | Layer |
|---|---|---|---|
| 0 | $-6.5$ | 288.15 | Troposphere |
| 11 | $0$ | 216.65 | Tropopause / lower stratosphere |
| 20 | $+1.0$ | 228.65 | Upper stratosphere |
| 32 | $+2.8$ | 270.65 | Stratopause |
| 47 | $0$ | 270.65 | Lower mesosphere |
| 51 | $-2.8$ | 214.65 | Upper mesosphere |
| 71 | $-2.0$ | 186.95 | Mesopause (at 84.852 km) |

Read the signs. The temperature **falls** through the troposphere because
convection carries heat up and the adiabat requires a decrease; it is **constant**
at the tropopause; it **rises** through the stratosphere because ozone absorbs
ultraviolet radiation in place; it **falls** again through the mesosphere because
there is essentially nothing left to absorb; and above the mesopause it rises
steeply in the thermosphere as extreme-ultraviolet radiation is absorbed by the
remaining, extremely tenuous gas. In the thermosphere the "temperature" is a
measure of the kinetic energy of a very thin gas and not of a large heat content —
a temperature of 1000 K there corresponds to a much smaller thermal energy per
unit volume than 300 K at sea level.

The names are worth having: **tropopause** at ~11 km (the standard's defined
value; 8–16 km in reality, depending on latitude and season), **stratopause**
near 47–51 km, **mesopause** near 85 km.

### 3.2 Integrating through the profile

Within a layer of constant lapse rate, equation (2) integrates in closed form:

$$p = p_{\text{base}}\left(\frac{T}{T_{\text{base}}}\right)^{g/(R\Gamma)}
\quad (\Gamma \ne 0), \qquad
p = p_{\text{base}}\exp\!\left[-\frac{g\,\Delta z}{RT_{\text{base}}}\right]
\quad (\Gamma = 0). \qquad (8)$$

Applying equation (8) layer by layer from $p_0 = 101\,325$ Pa gives the standard
atmosphere's pressures:

| Height (km) | $T$ (K) | $\Gamma$ (K/km) | $p$ (Pa) | $p$ (hPa) |
|---|---|---|---|---|
| 0 | 288.15 | $-6.5$ | 101 325.0 | 1013.25 |
| 11 | 216.65 | $0$ | 22 632.6 | 226.33 |
| 20 | 216.65 | $+1.0$ | 5 475.2 | 54.75 |
| 32 | 228.65 | $+2.8$ | 868.1 | 8.68 |
| 47 | 270.65 | $0$ | 110.9 | 1.11 |
| 51 | 270.65 | $-2.8$ | 66.9 | 0.67 |
| 71 | 214.65 | $-2.0$ | 4.0 | 0.04 |
| 84.852 | 186.95 | — | 0.4 | 0.004 |

**And the verification.** Inside the troposphere the constant lapse rate makes
the power law (6) an *exact* solution of the same differential equation, so a
numerical integration should reproduce it to round-off, not merely to a few per
cent:

$$\text{relative difference at }11\ \text{km} = 3.21\times10^{-16}.$$

That is double-precision round-off. It is the correct result when the integration
scheme reproduces the exact solution of the equation being integrated, and it is
the counterpart of the closed-form checks in lesson
[01](./01-pressure-density-depth.md) §8. Anything much larger than this would
indicate either a coding error or a mismatch between the profile used in the
integration and the one used in the analytic form — a subtle bug that a
"looks-plausible" output would hide.

### 3.3 Potential temperature and stability through the real profile

Evaluating equations (5) and (7) through the same profile:

| $z$ (km) | $T$ (K) | $p$ (hPa) | $\theta$ (K) | $N$ (s⁻¹) | Period (min) |
|---|---|---|---|---|---|
| 0 | 288.15 | 1013.25 | 288.15 | 0.01053 | 9.9 |
| 2 | 275.15 | 794.96 | 294.90 | 0.01078 | 9.7 |
| 5 | 255.65 | 540.20 | 305.96 | 0.01118 | 9.4 |
| 8 | 236.15 | 356.00 | 318.37 | 0.01163 | 9.0 |
| 11 | 216.65 | 226.33 | 332.43 | 0.02102 | 5.0 |
| 20 | 216.65 | 54.75 | 498.59 | 0.02207 | 4.7 |
| 47 | 270.65 | 1.11 | 1897.03 | 0.01880 | 5.6 |

Two results.

**$\theta$ rises monotonically everywhere**, so the whole 0–47 km column is
statically stable, including the troposphere. That is not a paradox: the
troposphere looks "overturned" only against an isothermal reference. Against the
*adiabatic* reference — which is what $\theta$ measures — it is stable, because
6.5 < 9.758. If the observed lapse rate ever exceeded 9.758 K/km, $\theta$ would
decrease with height and the layer would convect.

**$N$ nearly doubles across the tropopause**, from 0.0105 to 0.0210 s⁻¹, and the
buoyancy period halves from 9.9 to 5.0 minutes. The reason is visible in equation
(7): above the tropopause, $\Gamma = 0$, so $\Gamma_d-\Gamma$ is the *full*
9.758 K/km rather than the 3.26 K/km excess of the troposphere. A larger restoring
force per unit displacement, a stiffer oscillation. This factor-of-two jump in
$N$ is the quantitative statement of "the stratosphere is almost immune to
vertical mixing": a displaced parcel there oscillates rather than convects, and
the same displacement in the troposphere would be carried away by the convection
already present.

A nominal $N\approx0.01$ s⁻¹ gives a buoyancy period of about 10 minutes, which
is the timescale of a mountain lee wave and of a convective plume's oscillation.

### 3.4 The mass of the atmosphere

A one-line consequence of hydrostatic balance. Integrating equation (1) over the
whole atmosphere gives $\int_0^\infty\rho\,\mathrm{d}z = p_0/g$, so the total mass
is the surface pressure times the surface area divided by $g$:

$$M_{\text{atm}} = \frac{4\pi R^2 p_0}{g}
= \frac{4\pi(6.371\times10^6)^2\times101\,325}{9.806\,65}
= 5.27\times10^{18}\ \text{kg}. \qquad (9)$$

That is $8.83\times10^{-7}$ of the Earth's mass — about one millionth, and
comparable to the mass of a small icy moon rather than to nothing. Because
$p_0 = 101\,325$ Pa is exact by definition, the estimate carries no uncertainty in
the pressure; the assumptions of a spherical Earth and of sea-level pressure
everywhere are what limit it, and the second biases the answer slightly high
because much of the land surface lies above sea level.

## 4. Physical interpretation

**The same equation, two completely different regimes, because of geometry.** In
the Earth the pressure reaches $3.6\times10^{11}$ Pa over a distance comparable to
the body's radius, and the density varies by a factor of 5 because minerals
compress. In the atmosphere the pressure reaches $10^5$ Pa over 0.13 per cent of
the radius, and the density varies by $10^3$ because a gas expands. One equation,
two powers of ten in the answer.

**Lapse rate is a statement about stability, not about heating.** The daily
temperature cycle heats the ground, not the air; the troposphere is cold on top
because convection *carries* it there. When you see the dry adiabatic lapse rate
quoted as a property of air, remember that it is a property of the *process*: it
is what an adiabatic parcel does, and the actual profile is what the atmosphere
decides when it can convect.

**The tropopause is where the convection stops.** Its 11 km in the standard
atmosphere is a defined value; the physical definition is the level at which
convective updraughts can no longer penetrate, which is where the temperature of
a rising moist parcel falls to that of the environment. That is why the
tropopause is higher in the tropics (warm, moist surface ⇒ deeper convection).
The standard atmosphere's 11 km is a mid-latitude average.

**Potential temperature is the coordinate in which "hot" means "rises".** It is
worth noticing that the entire subject of atmospheric stability is organised
around one change of variable, equation (5), which removes the adiabatic
temperature change and leaves only the part that does work. The same move is made
in the ocean (potential density) and in the mantle (the adiabat of lesson
[02](./02-equations-of-state.md) §4.4), for the same reason.

## 5. Assumptions and regime of validity

| Assumption | Where used | Regime of validity | What breaks it |
|---|---|---|---|
| Hydrostatic balance | Throughout | Excellent: vertical accelerations are $10^{-3}g$ except in strong convection and tornadoes | Severe convection, gravity waves, and any strong updraught |
| Ideal gas | §1.2 | Air is nearly ideal at atmospheric temperatures and pressures | Condensation (which removes vapour), and real-gas corrections at high $p$ |
| Constant $g$ | Throughout | $g$ falls by ~3 per cent across 100 km | Only matters for the thermosphere and escape calculations |
| Dry adiabatic lapse rate | §2.1 | The correct rate for unsaturated air | Any saturated ascent; then the moist adiabat applies and it is not a constant |
| $c_p$ constant | §2.1 | $c_p$ varies by ~1 per cent over the troposphere | Large vertical extent; use tabulated $c_p(T)$ |
| Constant lapse rate within a layer | §3.2 | The definition of the standard atmosphere | The real atmosphere has curved profiles; a single lapse rate per layer is a convention |
| The standard atmosphere is the real atmosphere | §3 | It is a *defined* climatological profile | Any particular place or time; seasonal and latitude variation exceed the difference between layers |
| $\mathrm{d}\theta/\mathrm{d}z > 0$ is sufficient for stability | §2.4 | True for a dry adiabat | For moist air, stability is assessed against the moist adiabat, and conditional instability is the interesting case |
| Sea-level pressure applied everywhere | Equation (9) | Gives a slight overestimate | Topography; the true mean surface pressure is lower |

## 6. Units and dimensional analysis

- **$H = RT/g$.** $\mathrm{J\,kg^{-1}K^{-1}}\cdot\mathrm{K}/(\mathrm{m\,s^{-2}})
  = \mathrm{J\,kg^{-1}}/(\mathrm{m\,s^{-2}}) = \mathrm{m^2\,s^{-2}}/(\mathrm{m\,s^{-2}})
  = \mathrm{m}$ ✓.
- **$\Gamma_d = g/c_p$.** $\mathrm{m\,s^{-2}}/(\mathrm{J\,kg^{-1}K^{-1}})
  = \mathrm{m\,s^{-2}\,kg\,K\,J^{-1}} = \mathrm{K\,m^{-1}}$ ✓ (using
  $\mathrm{J} = \mathrm{kg\,m^2\,s^{-2}}$). Reported as 9.758 K/km.
- **The exponent $g/(R\Gamma)$.** Dimensionless:
  $\mathrm{m\,s^{-2}}/(\mathrm{m^2\,s^{-2}K^{-1}}\cdot\mathrm{K\,m^{-1}}) = 1$ ✓.
  Its value, 5.256, is a useful thing to know.
- **Potential temperature.** $T$ times a dimensionless power, so K ✓.
- **$N$.** $g/T$ has units $\mathrm{m\,s^{-2}K^{-1}}$ and
  $\Gamma_d-\Gamma$ has $\mathrm{K\,m^{-1}}$, so the product is
  $\mathrm{s^{-2}}$, and $N$ is in s⁻¹ ✓ — a frequency, as it must be.
- **Atmospheric mass (9).** $\mathrm{m^2}\cdot\mathrm{Pa}/(\mathrm{m\,s^{-2}})
  = \mathrm{m^2}\cdot\mathrm{kg\,m^{-1}\,s^{-2}}/(\mathrm{m\,s^{-2}}) = \mathrm{kg}$ ✓.
- **Useful anchors.** $H\approx8.4$ km; $\Gamma_d\approx9.8$ K/km;
  observed $\Gamma\approx6.5$ K/km; $p$ halves every ~5.5 km in the real
  troposphere (5.85 km isothermal); 90 per cent of the mass is below ~16 km; one
  atmosphere is 10.3 m of water.

## 7. Python demonstration

[`code/atmospheric_structure_demo.py`](./code/atmospheric_structure_demo.py)
derives the lapse rate, computes the scale height, integrates the standard
atmosphere, and evaluates $\theta$ and $N$. The blocks below are the script's
actual output, **abridged by omission** where a block would otherwise repeat rows
already tabulated above; every line shown is reproduced verbatim.

```text
  Gamma_d = 9.80665 / 1005 = 9.758 K/km
  Observed mean tropospheric lapse rate (defined in the standard
  atmosphere) = 6.5 K/km, i.e. 1.50 times smaller than dry adiabatic.
```

```text
  R_specific(air) = R/M = 8.31446262 / 0.0289644 = 287.058 J kg^-1 K^-1
  H = R T / g at sea level, 288.15 K    = 8.435 km
  H = R T / g at 250 K                  = 7.318 km
  H = R T / g at tropopause, 216.65 K   = 6.342 km
  For an isothermal 288.15 K atmosphere, p falls by a factor e every
  8.43 km (5.24 miles) and halves every 5.85 km.
```

```text
  z (km)    T (K)  L (K/km)      p (Pa)   p (hPa)  analytic p   rel diff
    0.00   288.15      -6.5    101325.0   1013.25    101325.0   0.00e+00
   11.00   216.65       0.0     22632.6    226.33     22632.6   3.21e-16
   20.00   216.65       1.0      5475.2     54.75         nan        n/a
   32.00   228.65       2.8       868.1      8.68         nan        n/a
   47.00   270.65       0.0       110.9      1.11         nan        n/a
   51.00   270.65      -2.8        66.9      0.67         nan        n/a
   71.00   214.65      -2.0         4.0      0.04         nan        n/a
   84.85   186.95       0.0         0.4      0.00         nan        n/a
```

```text
  z (km)    T (K)   p (hPa)   theta (K)   N (1/s)  period (min)
    0.00   288.15   1013.25      288.15   0.01053           9.9
    2.00   275.15    794.96      294.90   0.01078           9.7
    5.00   255.65    540.20      305.96   0.01118           9.4
    8.00   236.15    356.00      318.37   0.01163           9.0
   11.00   216.65    226.33      332.43   0.02102           5.0
   20.00   216.65     54.75      498.59   0.02207           4.7
   47.00   270.65      1.11     1897.03   0.01880           5.6
```

```text
  M = 4 pi R^2 p0 / g = 4 pi (6.371e+06)^2 x 101325 / 9.80665
    = 5.2701e+18 kg
  That is 8.825e-07 of the nominal Earth mass, i.e. about
  one millionth. The sea-level pressure of 101325 Pa is an exact
  defining value, so this estimate carries no uncertainty in p0; the
  assumptions of a spherical Earth and of sea-level pressure
  everywhere are what limit it, and the second one biases the answer
  slightly high because much of the land surface lies above sea level.
```

### What to observe

| Observation | Consequence |
|---|---|
| $\Gamma_d = 9.758$ K/km against an observed 6.5 | The factor 1.50 is latent heat and radiative-convective equilibrium, not error |
| $H = 8.435$ km at 288.15 K, 6.342 km at 216.65 K | The scale height is proportional to $T$; the tropopause is a *thin* atmosphere |
| $p$ halves every 5.85 km isothermally, ~5.5 km in the real troposphere | A lapse rate makes the atmosphere compress *faster* than exponential |
| Relative difference $3.21\times10^{-16}$ at 11 km | The integration reproduces the exact power law to round-off |
| $p$ = 226.33 hPa at 11 km, 1.11 hPa at 47 km | Two-thirds of the mass is in the troposphere; 0.1 per cent above 47 km |
| $\theta$ rises from 288.15 to 332.43 K across the troposphere | The troposphere is stable in the coordinate that matters |
| $N$ jumps 0.0105 → 0.0210 s⁻¹ at the tropopause | Stability doubles because $\Gamma_d-\Gamma$ doubles; the buoyancy period halves |
| $\theta = 1897$ K at 47 km | The stratosphere and mesosphere are extremely stably stratified |
| $M_{\text{atm}} = 5.27\times10^{18}$ kg | A millionth of the Earth's mass, and a one-line result |

> **Breaking exercise.** Change the tropospheric lapse rate in the demo from
> $-6.5$ to $-9.758$ K/km (the dry adiabat) and predict, before running, (i) the
> new tropopause temperature at 11 km, (ii) whether $N$ becomes zero or negative
> throughout the layer, and (iii) the new surface pressure at 11 km. Then answer
> the physical question the result raises: a dry-adiabatic troposphere has
> $\mathrm{d}\theta/\mathrm{d}z = 0$ and is *neutrally* stable, so it convects on
> the slightest push. What, in the real atmosphere, prevents the lapse rate from
> reaching 9.758 K/km everywhere?

## 8. Common mistakes

1. **Using the dry adiabatic lapse rate for a moist atmosphere.** 9.758 against
   6.5 is a 50 per cent error, and it is the error that makes a student's
   convective-cloud calculation give the wrong cloud base.
2. **Forgetting that the scale height depends on temperature.** Quoting a single
   "8 km" for the whole atmosphere; it is 8.4 km at the surface and 6.3 km at the
   tropopause of the same profile.
3. **Sign errors in the lapse rate.** $\Gamma$ is defined here as
   $-\mathrm{d}T/\mathrm{d}z$, so it is positive when temperature decreases
   upward. A negative $\Gamma$ in the stratosphere is correct and not a mistake.
4. **Applying the exponential atmosphere where the lapse rate is not zero.**
   Equation (3) requires isothermal conditions; use equation (8) otherwise.
5. **Treating the standard atmosphere as data.** It is a *definition*; the real
   profile at a place and time differs by more than the difference between its
   own layers.
6. **Concluding that the troposphere is unstable because temperature falls with
   height.** Stability is measured against the adiabat, not against zero. The
   correct test is $\mathrm{d}\theta/\mathrm{d}z$, or $N^2 > 0$.
7. **Using the isothermal scale height for the ocean.** $H = RT/g$ requires an
   ideal gas; water is incompressible and its pressure gradient is $\rho g$.
8. **Confusing the tropopause height with a constant.** 11 km in the standard is
   a mid-latitude average; the real range is roughly 8–16 km.
9. **Reporting the thermosphere's temperature as comparable to a surface
   temperature.** It measures the kinetic energy of an extremely tenuous gas, not
   an energy content.
10. **Ignoring the factor of $g$ in the atmospheric mass.** $p_0/g$ is the mass per
    unit area only if $g$ is the surface value; the result is exact for a
    spherical non-rotating body with uniform surface pressure.

## 9. Real-world applications

- **Weather forecasting and numerical weather prediction.** Hydrostatic balance
  is the vertical equation of every hydrostatic model; the hydrostatic
  approximation is abandoned only in non-hydrostatic cloud-resolving models.
- **Aviation.** The standard atmosphere defines the pressure altitude that
  altimeters read and the temperature profile used for aircraft performance. The
  fact that it is a *standard* and not the actual atmosphere is why a local
  pressure setting is required.
- **Balloon and sounding analysis.** A radiosonde returns $T$, $p$ and humidity;
  the derived $\theta(z)$ and $N(z)$ are what the forecaster reads to judge
  convective potential.
- **Air quality and dispersion.** The height of the stable layer and the value of
  $N$ set the depth of the mixed layer and hence pollutant concentration.
- **Remote sensing of temperature.** Nadir sounders retrieve $T(p)$ from
  radiances; the retrieval is anchored by hydrostatic balance, which is why the
  pressure coordinate is the natural one in atmospheric science.
- **Palaeoclimate and ice cores.** The lapse rate determines the relationship
  between surface temperature and the temperature at the top of an ice sheet,
  which is what an ice-core isotope record measures.
- **Planetary atmospheres.** The same equations with different $g$, $R$ and
  composition organise the structure of every atmosphere in the solar system;
  see lesson [05](./05-planetary-physics.md) §4.

## 10. Further reading

- **Wallace, J. M., & Hobbs, P. V. *Atmospheric Science: An Introductory Survey*
  (2nd ed., Academic Press, 2006).** The standard reference for the static
  stability analysis of §2.3–§2.4, and the source of the standard-atmosphere
  conventions. Level: intermediate to graduate.
- **Holton, J. R., & Hakim, G. J. *An Introduction to Dynamic Meteorology* (5th
  ed., Academic Press, 2013).** Hydrostatic balance, the buoyancy frequency and
  the thermodynamic equation, developed into the full dynamics. Level: graduate.
- **Andrews, D. G. *An Introduction to Atmospheric Physics* (2nd ed., Cambridge
  University Press, 2010).** The radiation-and-temperature view of why the
  stratosphere inverts, complementary to the dynamical treatment. Level:
  intermediate.
- **Salby, M. L. *Fundamentals of Atmospheric Physics* (Academic Press, 1996).**
  Thorough on the thermodynamic structure and the radiative-convective balance
  that sets the observed lapse rate. Level: graduate.
- **Chapman, S., & Lindzen, R. S. *Atmospheric Tides* (Reidel, 1970).** The upper
  atmosphere's structure and the buoyancy oscillations of §2.4, in full.
- **Vallis, G. K. *Atmospheric and Oceanic Fluid Dynamics* (2nd ed., Cambridge
  University Press, 2017).** The unified treatment of $N$ in both fluids, and the
  origin of that unification in potential-temperature coordinates. Level: graduate.
- **U.S. Standard Atmosphere (1976), published jointly by NOAA, NASA and the U.S.
  Air Force.** The definition used for the profile in §3. Confirm the current
  revision before using its numerical tables in any application.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 11. Related lessons

- [01 Pressure, Density and Gravity Inside the Earth](./01-pressure-density-depth.md)
  — the same equation in a self-gravitating incompressible body.
- [05 Comparative Planetary Physics and Interiors](./05-planetary-physics.md)
  — scale heights and atmospheric escape on other bodies.
- [02-06-01 Fluid Statics](../06-fluid-mechanics/01-fluid-statics.md) — buoyancy
  and the pressure gradient in a fluid at rest.
- [02-05-01 Temperature, Heat and Specific Heat](../05-thermodynamics/01-temperature-and-heat.md)
  — enthalpy and the adiabatic relation.
- [02-05-02 First Law, Work and Energy Balances](../05-thermodynamics/02-first-law.md)
  — the adiabat $pV^\gamma =$ const and its derivation.
- [16-atmosphere-climate/01-02 Hydrostatic Balance](../../16-atmosphere-climate/01-atmospheric-structure-and-thermodynamics/02-hydrostatic-balance.md)
  and [01-03 Thermodynamic Processes](../../16-atmosphere-climate/01-atmospheric-structure-and-thermodynamics/03-thermodynamic-processes.md)
  — the meteorological development, including the moist adiabat.
- [16-atmosphere-climate/02-01 Solar and Terrestrial Radiation](../../16-atmosphere-climate/02-radiation-and-energy-balance/01-solar-and-terrestrial-radiation.md)
  — the radiative balance that sets the radiative-equilibrium profile.

Exercises:
[`exercises/04-atmospheric-structure-exercises.md`](./exercises/04-atmospheric-structure-exercises.md)
and
[`exercises/04-atmospheric-structure-solutions.md`](./exercises/04-atmospheric-structure-solutions.md).

## Self-assessment checklist

- [ ] I can write hydrostatic balance for a gas and close it with the ideal-gas
      law. (§1.1–§1.2)
- [ ] I can derive $P = P_0e^{-z/H}$ and compute $H = RT/g$. (§1.3)
- [ ] I can derive $\Gamma_d = g/c_p$ from the first law and check it via
      $(\gamma-1)g/(\gamma R)$. (§2.1)
- [ ] I can explain the factor of 1.50 between the dry adiabat and the observed
      6.5 K/km. (§2.2)
- [ ] I can derive the power law $p = p_0(T/T_0)^{g/(R\Gamma)}$ and evaluate the
      exponent 5.256 for the troposphere. (§2.3)
- [ ] I can define potential temperature and say why $\mathrm{d}\theta/\mathrm{d}z>0$
      means stable. (§2.3)
- [ ] I can derive $N^2 = (g/T)(\Gamma_d-\Gamma)$ and interpret its sign. (§2.4)
- [ ] I can integrate hydrostatic balance through the standard atmosphere and
      verify against the analytic tropospheric solution. (§3.2)
- [ ] I can name the four layers and explain the sign of the lapse rate in each.
      (§3.1)
- [ ] I can derive the atmosphere's mass from $p_0$ and $g$. (§3.4)
