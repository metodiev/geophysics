---
id: 16-01-02
title: "Hydrostatic Balance and Pressure-Height Relations"
level: intermediate
prereqs: ["16-01-01", "02-06-01", "01-05-05"]
tags: [atmosphere, climate, hydrostatic-balance, hypsometric, geopotential, altimetry]
---

# Hydrostatic Balance and Pressure-Height Relations

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** hydrostatic balance from Newton's second law for a fluid element, and
   **state** precisely the regime in which it holds.
2. **Derive** the hypsometric equation from hydrostatic balance and the ideal-gas
   law, and **explain** that it is exact for an appropriately defined layer-mean
   temperature.
3. **Compute** a layer thickness from two pressure levels, and **invert** a
   measured thickness to a mean temperature.
4. **Quantify** the error made by using the arithmetic mean temperature instead of
   the $\ln p$-weighted mean, and by using the surface temperature.
5. **Convert** between geometric height and geopotential height, and **state** the
   size of the correction at $5$, $10$ and $20\ \mathrm{km}$.
6. **Build** a thickness-to-temperature error budget and **compute** the
   temperature accuracy needed for a given thickness accuracy.
7. **Estimate** the failure of hydrostatic balance from a vertical acceleration,
   and **say** whether it matters for a pressure profile.

## Prerequisites

- [01 Atmospheric Composition and Vertical Structure](01-atmospheric-composition.md) —
  the ideal-gas law, $R_d$, $c_p$ and the scale height.
- [02-06-01 Fluid Statics, Pressure and Buoyancy](../../02-physics/06-fluid-mechanics/01-fluid-statics.md) —
  pressure in a fluid at rest, and buoyancy.
- [01-05-05 Integration](../../01-mathematics/05-single-variable-calculus/05-integration.md) —
  the integrals used in §3 without comment.

## 1. Intuition: barometers weigh the sky

A barometer does not measure "pressure" in the abstract; it measures the weight of
the column of air above it. That single sentence is the content of this lesson.
Everything else is the algebra needed to turn it into numbers you can use.

Three consequences follow immediately, and each is worth holding on to:

- **Pressure must decrease upward**, because the column above you shrinks. It does:
  from about $1013\ \mathrm{hPa}$ at sea level to $500\ \mathrm{hPa}$ near
  $5.5\ \mathrm{km}$ to $226\ \mathrm{hPa}$ at the tropopause
  ([01](01-atmospheric-composition.md)).
- **A pressure difference measures a mass difference.** A $1\ \mathrm{hPa}$ fall
  in surface pressure is not a small number: over one square metre it is
  $0.1\ \mathrm{hPa} \times (1/9.80665) \approx 1.02\ \mathrm{kg\,m^{-2}}$, about
  a millimetre of water. Weather systems move masses of order $10^{5}\
  \mathrm{kg\,m^{-2}}$.
- **The height of a pressure surface is a temperature measurement.** Warm air is
  less dense, so a given pressure level sits higher above a warm column. This is
  why upper-air weather charts are drawn on pressure surfaces rather than at fixed
  heights: a "ridge" on a $500\ \mathrm{hPa}$ chart is a warm column, and a
  "trough" is a cold one. Section 3.3 shows exactly how many metres per kelvin.

## 2. Precise definitions

### 2.1 Hydrostatic balance

For a fluid at rest, the vertical component of the momentum equation reduces to

$$\boxed{\;\frac{\partial p}{\partial z} = -\rho g\;}$$

The **notation matters**: $\partial$, not $\mathrm{d}$. Balance is a statement about
the *vertical* gradient at a point; horizontal gradients are unconstrained and
are what drive the wind
([05](05-atmospheric-dynamics-basics.md)). The equation is a first-order ordinary
differential equation in $z$ for $p$, given $\rho(z)$.

### 2.2 Geopotential and geopotential height

Because $g$ varies with height and latitude, meteorology replaces $z$ by

$$\Phi(z) = \int_0^z g(z')\,\mathrm{d}z', \qquad
Z \equiv \frac{\Phi}{g_0},$$

with $g_0 = 9.80665\ \mathrm{m\,s^{-2}}$ the standard gravity. $Z$ is the
**geopotential height**, and its unit, the geopotential metre, is numerically
identical to the SI metre. The point of the substitution is that
$-\partial p/\partial Z = -\rho g_0$ exactly, so the equation of motion becomes
linear in the new coordinate.

### 2.3 Thickness and layer-mean temperature

The **thickness** of a layer is the geopotential height difference between two
pressure surfaces, $Z(p_1) - Z(p_2)$. The **hypsometric equation** relates it to a
mean temperature:

$$\boxed{\;Z_2 - Z_1 = \frac{R_d \bar{T}}{g_0}\ln\frac{p_1}{p_2}\;}$$

where $\bar{T}$ is *defined* by

$$\bar{T} = \frac{\displaystyle\int_{p_2}^{p_1} T\,\mathrm{d}\ln p}
{\displaystyle\int_{p_2}^{p_1}\mathrm{d}\ln p}
= \frac{1}{\ln(p_1/p_2)}\int_{p_2}^{p_1} T\,\mathrm{d}\ln p .$$

$\bar{T}$ is therefore not the arithmetic mean of the temperature of the layer.
Using the wrong mean is a real and measurable error, quantified in §5.

## 3. Derivations

### 3.1 Hydrostatic balance from Newton's second law

Take a slab of fluid of horizontal area $A$ and vertical extent
$\mathrm{d}z$ at height $z$ (Figure-free argument; the geometry is all it needs).
Three vertical forces act:

- pressure on the lower face, $p(z)A$, upward;
- pressure on the upper face, $p(z+\mathrm{d}z)A$, downward;
- weight, $\rho g A\,\mathrm{d}z$, downward.

Newton's second law for the slab, with vertical acceleration $a_z$:

$$\rho A\,\mathrm{d}z\,a_z = p(z)A - p(z+\mathrm{d}z)A - \rho g A\,\mathrm{d}z,$$

$$a_z = -\frac{1}{\rho}\frac{\partial p}{\partial z} - g .$$

Setting $a_z = 0$ gives $\partial p/\partial z = -\rho g$. Note what the derivation
does *not* assume: not that the fluid is incompressible, not that $T$ is constant,
and not that there is no motion — only that the vertical acceleration is
negligible. §6 measures how large it can get.

### 3.2 The hypsometric equation

Substitute the ideal-gas law $\rho = p/(R_d T)$ into hydrostatic balance and
divide by $p$:

$$\frac{\mathrm{d}p}{p} = -\frac{g}{R_d T}\,\mathrm{d}z
\quad\Longleftrightarrow\quad
\mathrm{d}z = -\frac{R_d T}{g}\,\mathrm{d}(\ln p).$$

Integrating between two pressure levels $p_1 > p_2$ with heights $z_1 < z_2$:

$$z_2 - z_1 = \frac{R_d}{g}\int_{p_2}^{p_1} T\,\mathrm{d}\ln p
= \frac{R_d \bar{T}}{g}\ln\frac{p_1}{p_2},$$

which is the hypsometric equation with the $\ln p$-weighted mean of §2.3. **The
equation is exact**: it is not a linearisation, and the only assumption is
hydrostatic balance plus the ideal-gas law. What is *not* exact is any claim that
$\bar{T}$ is a temperature you happen to have measured.

### 3.3 The layer-mean temperature of a polytropic layer

For the model atmosphere $T = T_0(p/p_0)^{\kappa}$ with
$\kappa \equiv R_d\Gamma/g_0$ (derived in
[01 §3.3](01-atmospheric-composition.md)), the weighted mean is

$$\bar{T} = \frac{T_0}{\ln(p_1/p_2)}\int_{p_2}^{p_1}(p/p_0)^{\kappa}\,\mathrm{d}\ln p
= \frac{T_0\,(p_1^{\kappa} - p_2^{\kappa})}
{\kappa\,p_0^{\kappa}\,\ln(p_1/p_2)} .$$

This is what the demonstration evaluates, and it is the number that makes the
hypsometric equation exact for the 1000–500 hPa layer.

### 3.4 Thickness sensitivity to temperature

Differentiate the hypsometric equation at fixed $p_1, p_2$:

$$\boxed{\;\frac{\delta(Z_2-Z_1)}{Z_2 - Z_1} = \frac{\delta \bar{T}}{\bar{T}}\;}
\qquad\Longrightarrow\qquad
\delta(Z_2-Z_1) = \frac{R_d}{g_0}\ln\frac{p_1}{p_2}\;\delta\bar T .$$

The coefficient $K \equiv (R_d/g_0)\ln(p_1/p_2)$ has units of metres per kelvin and
is the *only* thing you need to size an error budget. For the 1000–500 hPa layer

$$K = \frac{287.041}{9.80665}\times 0.693147 = 29.272 \times 0.693147
= 20.288\ \mathrm{m\,K^{-1}}.$$

### 3.5 Geopotential: how big is the correction?

With $g(z) = g_0\left(R_E/(R_E+z)\right)^2$ (an inverse-square field, exact for a
spherical Earth outside its mass),

$$\Phi(z) = g_0\int_0^z\left(\frac{R_E}{R_E+z'}\right)^{2}\mathrm{d}z'
= g_0\,\frac{R_E\,z}{R_E+z},
\qquad
Z = z\,\frac{R_E}{R_E+z}.$$

Therefore
$$Z - z = -\frac{z^2}{R_E+z} \approx -\frac{z^2}{R_E}.$$

The correction is quadratic: $z^2/R_E = 3.9\ \mathrm{m}$ at $5\ \mathrm{km}$,
$15.7\ \mathrm{m}$ at $10\ \mathrm{km}$ and $62.6\ \mathrm{m}$ at $20\ \mathrm{km}$ —
matching the demonstration. It is *worth applying* only because the thickness
errors of §5 are of the same few-metre size; a $1\%$ error in temperature would
swamp it.

### 3.6 Inverting the hypsometric equation

Solved for the mean temperature, the equation is the basis of a temperature
measurement:

$$\bar{T} = \frac{g_0\,(Z_2-Z_1)}{R_d \ln(p_1/p_2)} .$$

A radiosonde (or, historically, a radar altimeter measurement of layer thickness)
gives $Z_2 - Z_1$ directly; the constant $g_0/(R_d\ln(p_1/p_2))$ converts metres to
kelvin. For the 1000–500 hPa layer that constant is
$1/20.288\ \mathrm{m\,K^{-1}} = 0.04929\ \mathrm{K\,m^{-1}}$: about
**one kelvin per $20\ \mathrm{m}$ of thickness**.

**What is measured and what is inferred.** The *heights* are measured (by radar or
by hypsometry of pressure). The *temperature* is inferred, conditional on the
ideal-gas law and hydrostatic balance. In a moist atmosphere the layer-mean
temperature retrieved this way is a *virtual* temperature, because the air is
lighter than dry air at the same $T$ — the correction is derived in
[01 §3.5](01-atmospheric-composition.md) and used in
[04](04-moisture-and-clouds.md).

## 4. Physical interpretation

- **Pressure is a mass coordinate.** Because horizontal pressure gradients
  accelerate air but vertical ones merely weigh it, the surface $p = \text{const}$
  is a natural vertical coordinate. In this coordinate the hydrostatic equation
  becomes $\partial \Phi/\partial p = -1/\rho$: *geopotential is the integral of
  specific volume over pressure*. Pressure coordinates are the reason weather
  charts look the way they do.
- **Thickness is a thermometer.** A $1000\text{–}500\ \mathrm{hPa}$ thickness of
  $5462\ \mathrm{m}$ in the model means $\bar T = 269.28\ \mathrm{K} = -3.9\
  \mathrm{^\circ C}$. The common shorthand "$20\ \mathrm{m}$ per degree" is
  Section 3.4, and it is accurate to about $0.1\%$ over this layer.
- **The vertical coordinate is nearly inertial.** The demonstration shows that an
  acceleration of $0.1\ \mathrm{m\,s^{-2}}$ — a strong updraught — perturbs the
  pressure by only $1.0\%$ of $g$. That is why hydrostatic models can predict
  weather successfully without resolving convective motions; the vertical
  momentum equation is diagnostically weak. Note carefully that this is a claim
  about *pressure profiles*, not about the vertical velocity, which is essential
  for precipitation.
- **The relevant failure is at small scales, not at large ones.** The non-hydrostatic
  fraction scales as $a_z/g$; large-scale vertical accelerations are
  $\sim10^{-5}\ \mathrm{m\,s^{-2}}$ and utterly negligible, while thunderstorm
  updraughts and mountain waves, at a few tenths of a $\mathrm{m\,s^{-2}}$, are
  where the approximation must be dropped.
- **Altimetry is an inverse problem with a known degeneracy.** A pressure
  measurement alone does not determine a height: the same surface pressure occurs
  at different heights depending on the mean temperature of the column below. This
  is exactly the degeneracy of
  [06-08-01 receiver functions](../../06-seismology/08-receiver-functions-and-crustal-structure/01-receiver-function-principle.md)
  in a different guise: one measurement, two unknowns, so a second measurement (a
  thermometer, or a surface-pressure reference) must break it.

## 5. Worked numerical examples

**Example 1 — thickness and its two common errors.**

Model inputs: $p_0 = 101325\ \mathrm{Pa}$, $T_0 = 288.15\ \mathrm{K}$,
$\Gamma = 6.5\ \mathrm{K\,km^{-1}}$. The demonstration locates the pressure
surfaces by inverting the polytropic profile:

$$z(1000\ \mathrm{hPa}) = 110.88\ \mathrm{m}, \qquad
z(500\ \mathrm{hPa}) = 5574.22\ \mathrm{m},$$

so the exact thickness is $5463.34\ \mathrm{m}$ (in geometric height; the
geopotential correction of §3.5 is $O(10\ \mathrm{m})$ over this layer and is
applied separately).

| choice of $\bar T$ | $\bar T$ (K) | thickness (m) | error (m) | error (%) |
|---|---|---|---|---|
| surface temperature $287.429\ \mathrm{K}$ | 287.429 | 5831.49 | $+368.15$ | $+6.74$ |
| arithmetic mean of the layer | 269.673 | 5471.25 | $+7.92$ | $+0.145$ |
| $\ln p$-weighted mean (defined by the equation) | 269.283 | 5463.34 | $0.00$ | $0.000$ |

The arithmetic mean is **biased warm** by $0.390\ \mathrm{K}$ here, because
$\ln p$ spends more of its range in the upper, colder part of the layer. The
resulting thickness error, $7.9\ \mathrm{m}$, is $0.145\%$ — smaller than a
typical radiosonde's absolute accuracy, but systematic: it does not average out
over many soundings. Using the surface temperature gives a $6.7\%$ error, which is
why "thickness" is never estimated from a surface thermometer alone.

**Example 2 — the altimetry error budget.**

From §3.4 the thickness is $20.288\ \mathrm{m}$ per kelvin for this layer, so:

| $\delta\bar T$ (K) | $\delta(\text{thickness})$ (m) | % of $5463.34\ \mathrm{m}$ |
|---|---|---|
| 0.5 | 10.14 | 0.186 |
| 1.0 | 20.29 | 0.371 |
| 2.0 | 40.58 | 0.743 |
| 5.0 | 101.44 | 1.857 |

To hold the thickness error below $10\ \mathrm{m}$ the layer-mean temperature must
be known to $10/20.288 = 0.493\ \mathrm{K}$. This is the reason humidity
corrections matter (a $10\ \mathrm{g\,kg^{-1}}$ virtual-temperature correction is
$1.75\ \mathrm{K}$, Section 5.5 of [01](01-atmospheric-composition.md)) and the
reason radiative bias in a temperature sensor is a serious matter: **the
sensitivity is linear and it does not cancel in an average.**

**Example 3 — how wrong would non-hydrostatic balance have to be?**

The fractional departure from hydrostatic balance is $|a_z|/g$:

| $a_z$ (m s⁻²) | $|a_z|/g$ | surface-pressure perturbation (Pa) |
|---|---|---|
| 0.01 | 0.102% | 103 |
| 0.10 | 1.020% | 1033 |
| 1.00 | 10.197% | 10332 |

The surface-pressure column in the table is $(|a_z|/g)p_0$, the pressure offset a
uniform vertical acceleration would imply. Even an acceleration of an entire
$1\ \mathrm{m\,s^{-2}}$ — a tenth of gravity, far beyond any real sustained
updraught — moves the column pressure by only $103\ \mathrm{hPa}$, and real
sustained accelerations are two orders of magnitude smaller. **Hydrostatic balance
is an excellent approximation for pressure, and a poor one for vertical motion**;
the two statements are not in tension.

## 6. Assumptions and regime of validity

| Assumption | Where used | Failure mode and size |
|---|---|---|
| Vertical acceleration negligible | $\partial p/\partial z=-\rho g$ | Thunderstorms and mountain waves: $|a_z|/g \sim 10^{-2}$ locally; negligible for the mean profile and for large-scale flow |
| Ideal gas | $\rho = p/(R_d T)$ | $<0.1\%$ below $50\ \mathrm{km}$ |
| Spherically symmetric, inverse-square $g$ | §3.5 | The oblateness and terrain perturb $g$ by $\sim0.5\%$; small for thickness but not for absolute altimetry |
| Hydrostatic "steady state" | profile interpretation | Vertical adjustment takes $\sim N^{-1}$ (a few minutes), so a pressure profile is essentially instantaneous; no approximation needed |
| Horizontally uniform layer | hypsometric inversion of a *layer* | Fails where a front crosses the layer: the retrieved $\bar T$ is then a horizontal average, not a local temperature |
| $\bar T$ known | any thickness-to-temperature step | The dominant error; see Example 2 |
| Dry air constant $R_d$ | all of §3 | Moist air requires $T_v$; error $\sim0.5\%$ in density at $10\ \mathrm{g\,kg^{-1}}$ |

**Climate-claim discipline for this lesson.** The hypsometric equation is
thermodynamics, not evidence about climate. What it *does* provide is the
measurement chain: thickness changes are among the most directly observed records
of atmospheric warming, because they integrate temperature over a deep layer and
are less sensitive to local site effects than surface thermometers. Turning that
into an attribution statement requires the statistical machinery of
[16-07](../07-climate-extremes-and-attribution/README.md) and the
homogenisation of [16-08](../08-climate-observation-and-data/README.md); this
lesson only establishes the physics of the conversion.

## 7. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| Pressure | $p$ | Pa | |
| Geopotential | $\Phi$ | m² s⁻² | $g\times z$ |
| Geopotential height | $Z$ | m (gpm) | $\Phi/g_0$ |
| Layer-mean temperature | $\bar T$ | K | $\ln p$ weighted |
| Sensitivity coefficient | $(R_d/g_0)\ln(p_1/p_2)$ | m K⁻¹ | $(\mathrm{m^2\,s^{-2}\,K^{-1}})/(\mathrm{m\,s^{-2}})$ |
| Pressure-coordinate analogue | $\partial\Phi/\partial p = -1/\rho$ | m² s⁻² Pa⁻¹ | $(\mathrm{m^2\,s^{-2}})/(\mathrm{kg\,m^{-1}\,s^{-2}})$ |

The clean identity to remember is
$\delta Z / \delta \bar T = R_d \ln(p_1/p_2)/g_0$: a length per kelvin. Any
expression for thickness sensitivity that does not come out in m K⁻¹ has a
velocity or a mass in the wrong place.

## 8. Python demonstration

[`code/hydrostatic_balance_demo.py`](code/hydrostatic_balance_demo.py) prints all
of the numbers above. It:

1. computes the exact geometric heights of the 1000 and 500 hPa surfaces by
   inverting the polytropic profile;
2. computes the hypsometric thickness with three different choices of $\bar T$ and
   tabulates the errors — the `ln p`-weighted mean reproduces the exact value to
   $0.000\ \mathrm{m}$;
3. inverts the equation to recover $\bar T$ from the thickness;
4. tabulates the geopotential correction $Z-z$ from the analytic expression
   $\Phi = g_0 R_E z/(R_E+z)$, finding $-3.92$, $-15.67$ and $-62.59\
   \mathrm{m}$ at $5$, $10$ and $20\ \mathrm{km}$;
5. builds the thickness-to-temperature table and the $10\ \mathrm{m} \Rightarrow
   0.493\ \mathrm{K}$ requirement;
6. tabulates the non-hydrostatic fraction for three accelerations;
7. verifies with two independent routes — an RK4 integration of
   $\mathrm{d}p/\mathrm{d}z$ reproduces the analytic $500\ \mathrm{hPa}$ height to
   $0.000000\ \mathrm{Pa}$, and the hypsometric equation reproduces a
   $900\text{–}600\ \mathrm{hPa}$ thickness to $4.6\times10^{-12}\ \mathrm{m}$.

That last pair is the point of a *verification*: two independent computations of
the same quantity must agree, and their disagreement bounds the numerical error
rather than the physical uncertainty.

```bash
cd 16-atmosphere-climate/01-atmospheric-structure-and-thermodynamics/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python hydrostatic_balance_demo.py
```

## 9. Exercises

Graded problems with worked solutions:
[`exercises/02-hydrostatic-balance-exercises.md`](exercises/02-hydrostatic-balance-exercises.md)
and
[`exercises/02-hydrostatic-balance-solutions.md`](exercises/02-hydrostatic-balance-solutions.md).

## Mastery checkpoint

Without notes:

> A synthetic sounding gives $p = 1000\ \mathrm{hPa}$ at $Z = 111\ \mathrm{m}$ and
> $p = 300\ \mathrm{hPa}$ at $Z = 9160\ \mathrm{m}$. **(a)** Compute $\bar T$ for
> the layer. **(b)** Compute the thickness sensitivity coefficient and state the
> thickness error produced by a $1.5\ \mathrm{K}$ error in $\bar T$. **(c)** You
> later learn that the layer contains $6\ \mathrm{g\,kg^{-1}}$ of water vapour on
> average; state whether the true temperature is higher or lower than your answer
> to (a) and by roughly how much. **(d)** State two assumptions of your
> calculation and, for each, an observation that would falsify it.

## Common pitfalls

1. **Using the arithmetic mean temperature.** It is biased warm for a
   normal-lapse layer by $0.39\ \mathrm{K}$ in the model here — a $7.9\
   \mathrm{m}$ thickness bias that looks like noise and is not.
2. **Using the surface temperature as the layer mean.** A $6.7\%$ thickness
   error; see Example 1.
3. **Mixing up $z$ and $Z$.** They differ by up to $16\ \mathrm{m}$ at
   $10\ \mathrm{km}$; use $Z$ for thickness and be explicit.
4. **Confusing hydrostatic balance with "no vertical motion".** Balance says the
   *acceleration* is negligible, not the velocity. A slowly rising parcel is
   perfectly hydrostatic.
5. **Applying the hypsometric equation across a front.** The retrieved $\bar T$ is
   then a horizontal average over two different air masses.
6. **Believing altimetry is unambiguous.** A pressure measurement cannot separate
   height from column temperature; that degeneracy is the reason aircraft carry
   barometric altimeters *and* a reference pressure.
7. **Quoting $g$ to four figures where it varies by $0.5\%$.** Use
   $g_0$ deliberately and say so.

## Related modules

- [01 Atmospheric Composition and Vertical Structure](01-atmospheric-composition.md) —
  the constants and the pressure profiles used here.
- [03 Adiabatic Processes, Lapse Rates and Stability](03-thermodynamic-processes.md) —
  why $\Gamma$ has the value it does and what replaces it when a parcel rises.
- [04 Moisture, Humidity Variables and Cloud Formation](04-moisture-and-clouds.md) —
  the virtual-temperature correction to $\bar T$.
- [05 Atmospheric Dynamics: Coriolis, Geostrophic and Thermal Wind](05-atmospheric-dynamics-basics.md) —
  what thickness gradients do once the flow is in motion.
- [02-06-01 Fluid Statics, Pressure and Buoyancy](../../02-physics/06-fluid-mechanics/01-fluid-statics.md) —
  the general fluid-statics result derived here in the atmospheric case.
- [02-11-01 Pressure, Density and Gravity Inside the Earth](../../02-physics/11-physics-of-earths-interior-and-atmosphere/01-pressure-density-depth.md) —
  the same balance applied to the solid Earth, where $\rho$ is not given by a gas law.
- [16-03 Atmospheric Circulation](../03-atmospheric-circulation/README.md) —
  where thickness gradients drive the jet streams.
