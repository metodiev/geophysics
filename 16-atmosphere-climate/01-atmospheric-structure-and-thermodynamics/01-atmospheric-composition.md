---
id: 16-01-01
title: "Atmospheric Composition and Vertical Structure"
level: beginner
prereqs: ["02-01-01", "02-05-01"]
tags: [atmosphere, climate, composition, hydrostatic-balance, scale-height, thermodynamics]
---

# Atmospheric Composition and Vertical Structure

## Learning objectives

By the end of this lesson you will be able to:

1. **Convert** between mole fraction, mass mixing ratio and partial pressure for a
   dry-air mixture, and **compute** the mean molar mass of air from a table of
   species.
2. **Derive** the specific gas constant $R_d$ and the specific heats $c_p$, $c_v$
   of dry air from the molar gas constant and a chosen composition, and **verify**
   the Mayer relation $c_p - c_v = R_d$.
3. **Derive** the hydrostatic pressure profile for an isothermal atmosphere and
   for an atmosphere with a constant lapse rate, and **state** the scale height
   $H = R_d T / g$.
4. **Integrate** the hydrostatic equation numerically and **quantify** the
   disagreement with the analytic solutions to better than $0.01\%$.
5. **Compute** the total mass of the atmosphere and the mass of its column per
   unit area from surface pressure alone.
6. **Explain** why moist air is lighter than dry air at the same pressure and
   temperature, and **use** the virtual temperature.
7. **State** which numbers in this lesson are model inputs, which are measured,
   and which are inferred.

## Prerequisites

- [02-01-01 Physical Quantities, SI Units and Dimensional Homogeneity](../../02-physics/01-measurement-and-physical-reasoning/01-physical-quantities.md) —
  the unit discipline used in every equation below.
- [02-05-01 Temperature, Heat, Internal Energy and Specific Heat](../../02-physics/05-thermodynamics/01-temperature-and-heat.md) —
  what $c_p$ and $c_v$ mean before they are used here.

The hydrostatic balance that produces the pressure profiles is derived properly
in [02 Hydrostatic Balance and Pressure-Height Relations](02-hydrostatic-balance.md);
this lesson uses it and checks it numerically. The general thermodynamics of
mixing and of the first law is
[02-05 Thermodynamics and Heat Transfer](../../02-physics/05-thermodynamics/README.md)
and is not repeated.

> **All models and data in this module are SYNTHETIC.** The atmosphere below is a
> teaching model with chosen inputs. Nothing in it is a measurement made by this
> repository, and no number here should be cited for any location or date.

## 1. Intuition: an ocean of gas with a very short memory

Stand on a beach and the atmosphere feels weightless. It is not. A column of air
one metre square down to the ground has a mass of about
$10^4\ \mathrm{kg}$ (Section 5), which is the weight of roughly two loaded
lorries. The reason we do not notice is that the same pressure pushes up as down.

Two facts make the atmosphere tractable as physics.

**It is thin and dilute.** Ninety-nine per cent of its mass sits below about
$30\ \mathrm{km}$, and below the tropopause ($11\ \mathrm{km}$ in the model of
this lesson) sits $77.7\%$ of the mass. Air behaves as an ideal gas to better than
$0.1\%$ at these pressures and temperatures, so one equation of state is enough.

**It mixes fast.** Molecules at $288\ \mathrm{K}$ move at a root-mean-square
speed of $506\ \mathrm{m\,s^{-1}}$ (Section 2), some fifty times faster than a
typical wind. A parcel of air therefore comes into thermal equilibrium with its
surroundings long before it has been carried far. That is the licence to treat
the atmosphere as a *continuum with a local temperature* — the assumption on
which almost everything in folders 16 and 17 rests.

The composition is the starting point because it fixes the constants. Nitrogen
and oxygen together are $99.03\%$ of dry air by mole fraction; everything else,
including the carbon dioxide that dominates the public discussion of climate,
makes up the remaining $1\%$ by mole but a much smaller share by mass. The gas
constant of air, and therefore every pressure, density and scale height in this
module, is a weighted average of the behaviour of that mixture.

## 2. Precise definitions

### 2.1 Composition variables

For a mixture of species $i$ with molecular counts $n_i$:

$$x_i = \frac{n_i}{\sum_j n_j} \quad \text{(mole fraction, dimensionless)},$$

$$w_i = \frac{n_i M_i}{\sum_j n_j M_j} \quad \text{(mass fraction, dimensionless)},$$

where $M_i$ is the molar mass of species $i$ in $\mathrm{kg\,mol^{-1}}$.
Meteorology uses a third variable, the **mass mixing ratio**
$r_i = m_i/m_{\text{dry air}}$ (dimensionless, often quoted in
$\mathrm{g\,kg^{-1}}$). The three are related through molar masses and are not
interchangeable: for water vapour in air at $10\ \mathrm{g\,kg^{-1}}$,
$r = 0.010$ but the mole fraction is only $0.0162$.

The mean molar mass of the mixture, by definition a mole-fraction-weighted
average, is

$$\boxed{\;M_d = \sum_i x_i M_i\;}$$

and is the *only* place composition enters the ideal-gas law for air.

### 2.2 The equation of state and the derived constants

$$\boxed{\;p = \rho R_d T\;} \qquad R_d = \frac{R^{*}}{M_d},$$

with $R^{*} = 8.314462618\ \mathrm{J\,mol^{-1}\,K^{-1}}$ (a standard constant, the
exact SI value of the molar gas constant) and $R_d$ the **specific gas constant
for dry air**. For a diatomic gas the equipartition theorem gives
$\gamma \equiv c_p/c_v = 7/5$, so

$$c_p = \frac{\gamma}{\gamma-1}R_d, \qquad c_v = \frac{R_d}{\gamma-1}, \qquad
c_p - c_v = R_d .$$

The last relation (Mayer's relation) is not an observation about air; it follows
from the ideal-gas law and is a useful arithmetic check.

### 2.3 Hydrostatic balance

For a fluid at rest with no horizontal pressure gradient,

$$\frac{\mathrm{d}p}{\mathrm{d}z} = -\rho g ,$$

derived from [02-06-01 Fluid Statics, Pressure and Buoyancy](../../02-physics/06-fluid-mechanics/01-fluid-statics.md).
This is one of the few exact statements in meteorology, and it is the engine of
the pressure profiles below. It contains no approximation about temperature: it
holds whatever $T(z)$ is.

## 3. Derivations

### 3.1 Mean molar mass and $R_d$ from a composition table

The demonstration takes the following dry-air mole fractions as *chosen inputs*
of the teaching model (they are printed by the code, and they are normalised by
their sum, which is not exactly unity):

| species | $M_i$ (g mol⁻¹) | $x_i$ |
|---|---|---|
| N₂ | 28.0134 | 0.780840 |
| O₂ | 31.9988 | 0.209476 |
| Ar | 39.9480 | 0.009340 |
| CO₂ | 44.0095 | 0.000420 |
| Ne | 20.1797 | 0.00001818 |
| He | 4.002602 | 0.00000524 |
| CH₄ | 16.0425 | 0.00000190 |
| Kr | 83.7980 | 0.00000114 |
| H₂ | 2.01588 | 0.00000055 |
| N₂O | 44.0128 | 0.00000033 |
| **sum** | | **1.00010334** |

Evaluating $M_d = \sum_i x_i M_i$ after normalising by that sum gives

$$M_d = 28.9661\ \mathrm{g\,mol^{-1}} = 2.89661\times10^{-2}\ \mathrm{kg\,mol^{-1}},$$

$$R_d = \frac{8.314462618}{2.89661\times10^{-2}}
= 287.041\ \mathrm{J\,kg^{-1}\,K^{-1}},$$

$$c_p = \frac{1.4}{0.4}\times 287.041 = 1004.64\ \mathrm{J\,kg^{-1}\,K^{-1}},
\qquad c_v = \frac{287.041}{0.4} = 717.60\ \mathrm{J\,kg^{-1}\,K^{-1}},$$

and $c_p - c_v = 287.041 = R_d$ exactly, as Mayer's relation requires. These are
*derived* numbers in this module, not quoted constants: change the CO₂ fraction
and $R_d$ changes in the sixth figure.

**Sensitivity.** Adding $100\ \mathrm{ppm}$ of CO₂ (from 420 to
$520\ \mathrm{\mu mol\,mol^{-1}}$) raises $M_d$ by
$100\times10^{-6}\times(44.0095-28.9661) = 1.50\times10^{-3}\
\mathrm{g\,mol^{-1}}$, i.e. by $5.2\times10^{-5}$ relative — and lowers $R_d$ by
the same fraction, $0.015\ \mathrm{J\,kg^{-1}\,K^{-1}}$. Composition changes
matter for $R_d$ only at the $10^{-5}$ level; they matter for *radiative transfer*
in [16-02](../02-radiation-and-energy-balance/README.md) at a level eight orders
of magnitude larger. That contrast is the reason the same molecule can be
irrelevant to the dynamics and central to the energy budget.

### 3.2 Scale height for an isothermal atmosphere

Substitute $\rho = p/(R_d T)$ into the hydrostatic equation:

$$\frac{\mathrm{d}p}{\mathrm{d}z} = -\frac{g}{R_d T}\,p .$$

If $T$ were independent of $z$ this integrates at once:

$$\boxed{\;p(z) = p_0 \exp\!\left(-\frac{z}{H}\right), \qquad
H \equiv \frac{R_d T}{g}.}$$

$H$ is the **scale height**: the height over which pressure falls by a factor
$e$. With the sea-level temperature of the model, $T_0 = 288.15\ \mathrm{K}$ and
$g = 9.80665\ \mathrm{m\,s^{-2}}$ (standard gravity),

$$H = \frac{287.041 \times 288.15}{9.80665} = 8.4342\times10^{3}\ \mathrm{m}
= 8.4342\ \mathrm{km}.$$

So the isothermal model predicts $p(1\ \mathrm{km}) = 0.8882\,p_0$,
$p(5\ \mathrm{km}) = 0.5528\,p_0$ and $p(10\ \mathrm{km}) = 0.3055\,p_0$. Keep
those three numbers: Section 3.3 shows the real (lapse-rate) atmosphere deviates
from them by an amount that grows with height, and Section 5 measures it.

### 3.3 The polytropic solution for a constant lapse rate

The troposphere is not isothermal. Adopt the conventional lapse rate
$\Gamma = 6.5\ \mathrm{K\,km^{-1}} = 6.5\times10^{-3}\ \mathrm{K\,m^{-1}}$
(a stated convention of the standard atmosphere, not a measurement of this
module), so that $T(z) = T_0 - \Gamma z$ up to the tropopause at
$z_t = 11\ \mathrm{km}$; above it the model is isothermal at $216.65\ \mathrm{K}$
to $20\ \mathrm{km}$. Then

$$\int_{p_0}^{p}\frac{\mathrm{d}p'}{p'}
= -\frac{g}{R_d}\int_0^{z}\frac{\mathrm{d}z'}{T_0-\Gamma z'},$$

$$p(z) = p_0\left(\frac{T(z)}{T_0}\right)^{\!\frac{g}{R_d \Gamma}}
= p_0\left(1-\frac{\Gamma z}{T_0}\right)^{\!\frac{g}{R_d\Gamma}},$$

with the **polytropic exponent**

$$\frac{g}{R_d \Gamma} = \frac{9.80665}{287.041 \times 6.5\times10^{-3}}
= 5.2561 .$$

Above the tropopause the isothermal solution resumes from $p(z_t)$:

$$p(z) = p(z_t)\exp\!\left(-\frac{(z-z_t)g}{R_d T_t}\right),
\qquad T_t = 216.65\ \mathrm{K}.$$

Note the arithmetic identity worth remembering: writing the exponent as
$g/(R_d\Gamma) = (g/H)(1/\Gamma)$ shows that the polytropic profile is the
isothermal profile with an *effective* scale height $H\gamma_{\text{eff}}$
growing with height, because the air is cooling as you rise.

### 3.4 Total mass of the atmosphere

Integrate hydrostatic balance over the whole column and use $p(\infty)=0$:

$$\int_0^\infty \rho g\,\mathrm{d}z = p_0 \;\Longrightarrow\;
\frac{m}{A} = \frac{p_0}{g},$$

so the column mass per unit area depends **only** on surface pressure. Multiplying
by the Earth's surface area $A = 4\pi R_E^2$ gives the total mass as a pure
surface measurement:

$$M_{\text{atm}} = \frac{p_0}{g}\,4\pi R_E^2 .$$

With $p_0 = 101325\ \mathrm{Pa}$ (standard sea-level pressure, a definition),
$g = 9.80665\ \mathrm{m\,s^{-2}}$ and the conventional mean radius
$R_E = 6.371\times10^{6}\ \mathrm{m}$:

$$\frac{m}{A} = \frac{101325}{9.80665} = 10332.27\ \mathrm{kg\,m^{-2}},
\qquad
M_{\text{atm}} = 10332.27 \times 5.1006\times10^{14}
= 5.2701\times10^{18}\ \mathrm{kg}.$$

For scale, that is $8.8\times10^{-7}$ of the Earth's mass. The **uncertainty** in
this number is dominated not by $p_0$ (known to a few parts in $10^4$ as a *local*
pressure, but atmospheric pressure varies by $\pm 3\%$ in time and by more with
altitude) but by the choice of $p_0$ itself: it is a definition of a standard
state, and the real global mean surface pressure is different in the third
figure. Quoting $5.27\times10^{18}\ \mathrm{kg}$ to four figures is therefore a
statement about the standard atmosphere, not a measurement of the Earth.

### 3.5 Why moist air is lighter

Air is a mixture, and the ideal-gas law applies to each component separately:
$p = p_d + e$, with $p_d = \rho_d R_d T$ for dry air and $e = \rho_v R_v T$ for
water vapour, where $M_w = 18.0153\ \mathrm{g\,mol^{-1}}$ gives
$R_v = 8.314462618/1.80153\times10^{-2} = 461.5\ \mathrm{J\,kg^{-1}\,K^{-1}}$.
Eliminating the partial pressures gives

$$\rho = \frac{p}{R_d T}\left[1 - \frac{e}{p}\left(1-\varepsilon\right)\right],
\qquad \varepsilon \equiv \frac{R_d}{R_v} = \frac{M_w}{M_d} = 0.622 .$$

Introduce the **virtual temperature** $T_v$ by requiring
$\rho = p/(R_d T_v)$:

$$T_v = \frac{T}{1 - \dfrac{e}{p}(1-\varepsilon)}
= T\left(1 + 0.608\,q + \cdots\right),$$

where $q$ is the specific humidity (the $\cdots$ are terms of order
$q^2$). The name is literal: moist air at temperature $T$ behaves
dynamically like dry air at the slightly higher temperature $T_v$. A water
molecule is lighter than the nitrogen or oxygen molecule it displaces, so adding
vapour at *fixed pressure* lowers the density.

## 4. Physical interpretation

- **Composition sets the constants, not the weather.** $R_d = 287.041\
  \mathrm{J\,kg^{-1}\,K^{-1}}$ and $c_p = 1004.64\ \mathrm{J\,kg^{-1}\,K^{-1}}$
  are properties of the mixture. Every temperature, pressure and stability
  calculation in this module reuses them.
- **The scale height is the natural ruler.** At $8.43\ \mathrm{km}$ it is close
  to the height of the highest mountains divided by one. Saying "the pressure
  halves every $5.8\ \mathrm{km}$" (since $\ln 2 \times H = 0.693 \times 8.434 =
  5.85\ \mathrm{km}$) is a better intuition pump than any formula.
- **Hydrostatic balance is exact; the profiles are models.** The pressure at a
  point is determined by the mass of the air above it, full stop. What the
  isothermal and polytropic formulae add is an assumption about $T(z)$.
- **The atmosphere is not in radiative equilibrium.** Its temperature profile
  falls in the troposphere and rises in the stratosphere. Hydrostatic balance
  does not explain either feature, and Section 6 states plainly what would have
  to be added. The explanation is radiative plus dynamical, and it is the subject
  of [16-02](../02-radiation-and-energy-balance/README.md) and
  [16-03](../03-atmospheric-circulation/README.md).
- **A thin shell.** With $H \ll R_E$ the atmosphere is a shell of relative
  thickness $8.4/6371 = 1.3\times10^{-3}$; the plane-parallel approximation used
  throughout folder 16 and in radiative transfer is therefore excellent for local
  problems and fails only for the large-scale geometry of sunlight.

## 5. Worked numerical example

**Example 1 — pressure at 3 km, isothermal versus lapse-rate.**

*Isothermal*, using $H = 8.4342\ \mathrm{km}$ from the demonstration:

$$p = 1013.25\,\mathrm{hPa}\,\times\exp\!\left(-\frac{3.000}{8.4342}\right)
= 1013.25 \times e^{-0.355694} = 1013.25 \times 0.700627
= 709.97\ \mathrm{hPa}.$$

*Polytropic*, using the exponent $5.2561$:

$$T(3\ \mathrm{km}) = 288.15 - 6.5\times3 = 268.65\ \mathrm{K},$$

$$\frac{T}{T_0} = 0.932328, \qquad
p = 1013.25 \times 0.932328^{5.2561}
= 1013.25 \times 0.691854 = 701.08\ \mathrm{hPa}.$$

The isothermal model overestimates the pressure at $3\ \mathrm{km}$ by
$8.89\ \mathrm{hPa}$ ($1.27\%$). At $5\ \mathrm{km}$ the gap is
$540.19$ vs $560.09\ \mathrm{hPa}$, i.e. $19.90\ \mathrm{hPa}$ ($3.7\%$), and at
$8\ \mathrm{km}$ it is $355.98$ vs $392.44\ \mathrm{hPa}$, i.e.
$36.46\ \mathrm{hPa}$ ($10.2\%$). **The isothermal approximation degrades upward
and the sign of the error is systematic, not random** — cold air aloft is dense,
so pressure falls faster than an isothermal model predicts. This is exactly the
kind of assumption failure the exercises ask you to quantify.

**Example 2 — how much of the atmosphere is below the tropopause?**

Hydrostatic balance at $z_t$ gives the fraction of the mass above, which is just
$p(z_t)/p_0$:

$$\frac{p(11\ \mathrm{km})}{p_0} = \left(\frac{216.65}{288.15}\right)^{5.2561}
= 0.751865^{5.2561} = 0.2233
\;\Longrightarrow\; f_{\text{below}} = 1 - 0.2233 = 0.7767 .$$

So $77.7\%$ of the atmospheric mass — and essentially all of the water vapour and
weather — lies in the lowest $1.7\ \times10^{-3}$ of the Earth's radius. Observing
the atmosphere from above is therefore mostly a measurement of a very thin layer.

**Example 3 — mass of a trace constituent, and the per-ppm weight.**

The mass mixing ratio of CO₂ in this model's dry air is

$$w_{\mathrm{CO_2}} = x\frac{M_{\mathrm{CO_2}}}{M_d}
= 4.20\times10^{-4}\times\frac{44.0095}{28.9661} = 6.381\times10^{-4}\
\mathrm{kg\,kg^{-1}},$$

so the total CO₂ mass implied by the model composition is
$5.2701\times10^{18} \times 6.381\times10^{-4} = 3.36\times10^{15}\ \mathrm{kg}$.
One mole fraction of $1\ \mathrm{\mu mol\,mol^{-1}}$ (1 ppm) corresponds to
$10332.27\ \mathrm{kg\,m^{-2}} \times 1.519\times10^{-6} = 1.57\times10^{-2}\
\mathrm{kg\,m^{-2}}$ of CO₂, or $8.01\times10^{12}\ \mathrm{kg}$ over the Earth.

Note carefully what this calculation is: **arithmetic on a chosen composition
input**. It is not a measurement of the atmosphere's CO₂ content, this repository
does not track the current value, and the model's $420\ \times10^{-6}$ is an
illustrative number chosen so the tables are concrete. The *method* — convert a
mole fraction to a mass and multiply by $p_0 A/g$ — is the transferable result.

## 6. Assumptions and regime of validity

| Assumption | Where used | What breaks it |
|---|---|---|
| Ideal gas, $p=\rho R_d T$ | everywhere | Below about $50\ \mathrm{km}$ the error is $\lesssim0.1\%$; the non-ideal virial corrections become relevant in the thermosphere |
| Constant composition of "dry air" | $M_d$, $R_d$, $c_p$ | Water vapour varies from $0.1$ to $4\%$ near the surface; handled by $T_v$ (§3.5) not by changing $R_d$ |
| $\gamma = 1.4$ exactly | $c_p, c_v$ | Real air has $\gamma = 1.400$ to three figures; the neglected vibrational modes of CO₂ would move it in the fourth |
| Hydrostatic balance | all pressure profiles | Fails in vigorous convection where vertical accelerations are comparable to $g$; the failure is local and small away from thunderstorms |
| $T(z)$ linear with $\Gamma = 6.5\ \mathrm{K\,km^{-1}}$ | polytropic profile | The real lapse rate varies with season, surface and humidity; measured dry and moist adiabats are derived in [03 Adiabatic Processes, Lapse Rates and Stability](03-thermodynamic-processes.md) |
| Isothermal above $11\ \mathrm{km}$ | upper profile | The real stratosphere warms to about $270\ \mathrm{K}$ near $50\ \mathrm{km}$ because of ozone absorption — pure radiative physics, [16-02](../02-radiation-and-energy-balance/README.md) |
| Plane-parallel / thin shell | interpretation only | Curvature matters for solar geometry and for limb observations |
| Steady state | the profiles | A pressure profile is essentially instantaneous; the atmosphere adjusts to surface pressure changes in hours |

Two points about climate claims, made explicit here because this is the first
lesson of the folder:

1. **The pressure profile is not evidence about climate change.** It is a
   consequence of mass, gravity and temperature. The temperature profile is the
   thing that changes, and the interesting questions are about what sets it.
2. **The composition table is a model input.** The greenhouse effect of that CO₂
   is computed from measured absorption coefficients in
   [16-02-02](../02-radiation-and-energy-balance/02-radiative-transfer-atmosphere.md)
   and [16-02-03](../02-radiation-and-energy-balance/03-greenhouse-effect.md);
   those lessons will state exactly what is measured, what is modelled and what
   is inferred.

## 7. Units and dimensional analysis

| Quantity | Symbol | SI unit | Check |
|---|---|---|---|
| Pressure | $p$ | Pa = kg m⁻¹ s⁻² | force/area |
| Density | $\rho$ | kg m⁻³ | |
| Temperature | $T$ | K | |
| Specific gas constant | $R_d$ | J kg⁻¹ K⁻¹ | $(\mathrm{kg\,m^2\,s^{-2}})/(\mathrm{kg\,K})$ |
| Specific heat | $c_p, c_v$ | J kg⁻¹ K⁻¹ | same as $R_d$: Mayer's relation is a unit check |
| Lapse rate | $\Gamma$ | K m⁻¹ | K per km divided by 1000 |
| Scale height | $H = R_d T/g$ | m | $(\mathrm{J\,kg^{-1}\,K^{-1}})(\mathrm{K})/(\mathrm{m\,s^{-2}}) = \mathrm{m^2\,s^{-2}}/(\mathrm{m\,s^{-2}})=\mathrm{m}$ ✔ |
| Column mass | $p_0/g$ | kg m⁻² | $(\mathrm{kg\,m^{-1}\,s^{-2}})/(\mathrm{m\,s^{-2}})$ ✔ |
| Polytropic exponent | $g/(R_d\Gamma)$ | dimensionless | $(\mathrm{m\,s^{-2}})/((\mathrm{m^2\,s^{-2}\,K^{-1}})(\mathrm{K\,m^{-1}}))$ ✔ |

The two most common unit errors in this subject: quoting $\Gamma$ in
$\mathrm{K\,km^{-1}}$ inside the exponent, and quoting $R_d$ per mole rather than
per kilogram. The first changes the exponent by $10^3$; the second by a factor
$M_d \approx 29$.

## 8. Python demonstration

[`code/atmospheric_composition_demo.py`](code/atmospheric_composition_demo.py)
prints every number quoted above. It:

1. builds $M_d$ and $R_d$ from the composition table and checks the sum of the
   mole fractions;
2. derives $c_p$, $c_v$ and verifies $c_p - c_v = R_d$;
3. computes the rms molecular speed and the scale height;
4. integrates $\mathrm{d}p/\mathrm{d}z = -p g/(R_d T(z))$ with a fourth-order
   Runge–Kutta scheme and compares it with the analytic isothermal, polytropic
   and isothermal-above-the-tropopause solutions at $0,1,5,10,11,15$ and
   $20\ \mathrm{km}$. The agreement is better than $10^{-2}\ \mathrm{Pa}$
   everywhere — i.e. the analytic formulae and the numerics are the same physics,
   which is what a verification should show;
5. computes the column mass and the total atmospheric mass, and the fraction of
   mass below the tropopause;
6. computes the virtual temperature and the density change from
   $q = 10\ \mathrm{g\,kg^{-1}}$;
7. converts an illustrative column water vapour of $25\ \mathrm{kg\,m^{-2}}$ to
   latent heat and expresses it as a temperature increment over the whole column,
   $6.02\ \mathrm{K}$.

Run it from the module's `code/` directory:

```bash
cd 16-atmosphere-climate/01-atmospheric-structure-and-thermodynamics/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python atmospheric_composition_demo.py
```

## 9. Exercises

Graded problems with worked solutions:
[`exercises/01-atmospheric-composition-exercises.md`](exercises/01-atmospheric-composition-exercises.md)
and
[`exercises/01-atmospheric-composition-solutions.md`](exercises/01-atmospheric-composition-solutions.md).

## Mastery checkpoint

Without notes:

> An exoplanet's atmosphere is modelled as dry air with $M_d = 28.97\
> \mathrm{g\,mol^{-1}}$ and a surface pressure of $2.00\times10^5\ \mathrm{Pa}$ at
> $T_0 = 300\ \mathrm{K}$, with a constant lapse rate of
> $5.0\ \mathrm{K\,km^{-1}}$. **(a)** Compute $R_d$, $c_p$ and the scale height.
> **(b)** Compute the pressure at $4\ \mathrm{km}$ with the isothermal and the
> polytropic models and state the percentage difference. **(c)** Compute the
> column mass per unit area and, for a planet of radius $7.0\times10^{6}\
> \mathrm{m}$, the total atmosphere mass. **(d)** State one assumption of the
> polytropic model that this planet would violate, and say how you would detect
> the violation in a measured $T(z)$ profile.

## Common pitfalls

1. **Confusing mole fraction and mass fraction.** For CO₂ in air they differ by a
   factor $44.0/28.97 = 1.52$; for water vapour by a factor $0.62$ in the
   opposite sense.
2. **Using $\Gamma$ in $\mathrm{K\,km^{-1}}$ in the exponent.** The exponent is
   dimensionless and needs metres.
3. **Quoting $5.27\times10^{18}\ \mathrm{kg}$ as a measured mass.** It is a
   recomputation of a *standard* surface pressure; the real column mass varies.
4. **Treating $c_p$ as a constant of nature.** It is a property of the chosen
   mixture: change the composition and it moves.
5. **Believing the isothermal model at altitude.** Its error reaches $10\%$ by
   $8\ \mathrm{km}$, and it has the wrong sign of curvature everywhere in the
   troposphere.
6. **Using the dry gas constant for moist air instead of $T_v$.** The density
   error at $q=10\ \mathrm{g\,kg^{-1}}$ is $0.6\%$ — small, but systematic, and
   larger than many of the effects this folder later claims to detect.

## Related modules

- [02 Hydrostatic Balance and Pressure-Height Relations](02-hydrostatic-balance.md) —
  the same balance derived from first principles, with the altimetry applications.
- [03 Adiabatic Processes, Lapse Rates and Stability](03-thermodynamic-processes.md) —
  where the lapse rate comes from and when a parcel rises.
- [04 Moisture, Humidity Variables and Cloud Formation](04-moisture-and-clouds.md) —
  the humidity variables used in §3.5.
- [05 Atmospheric Dynamics: Coriolis, Geostrophic and Thermal Wind](05-atmospheric-dynamics-basics.md) —
  what happens once the atmosphere is not at rest.
- [02-05 Thermodynamics and Heat Transfer](../../02-physics/05-thermodynamics/README.md) —
  the general thermodynamics used but not duplicated here.
- [02-11-04 Atmospheric Structure, Hydrostatic Balance and Lapse Rates](../../02-physics/11-physics-of-earths-interior-and-atmosphere/04-atmospheric-structure.md) —
  the same physics stated for the general planetary case.
- [Module 16-02 — Radiation and Energy Balance](../02-radiation-and-energy-balance/README.md) —
  what actually sets the temperature profile used here as an input.
