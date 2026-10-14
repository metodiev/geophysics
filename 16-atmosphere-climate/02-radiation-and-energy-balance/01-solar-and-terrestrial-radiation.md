---
id: 16-02-01
title: "Solar and Terrestrial Radiation, Blackbody Laws"
level: intermediate
prereqs: ["16-01-01", "02-05-05"]
tags: [atmosphere, climate, radiation, blackbody, planck, stefan-boltzmann, wien, insolation]
---

# Solar and Terrestrial Radiation, Blackbody Laws

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** radiance, irradiance (flux density) and exitance, and **convert**
   between them with the correct factor of $\pi$ for a Lambertian surface.
2. **Derive** Wien's displacement law and the Stefan–Boltzmann law from the Planck
   function, and **compute** the constants $b = hc/(xk_B)$ and
   $\sigma = 2\pi^5k_B^4/(15h^3c^2)$ from $h$, $c$ and $k_B$.
3. **Derive** the solar effective temperature from the solar constant, the
   astronomical unit and the nominal solar radius, and **explain** why that
   derivation requires no knowledge of the Sun's interior.
4. **Compute** the global-mean top-of-atmosphere insolation, the absorbed fraction
   for a stated albedo, and the corresponding effective radiating temperature.
5. **Quantify** the spectral separation of solar and terrestrial radiation and
   **explain** why it is the prerequisite for any greenhouse effect.
6. **Compute** a brightness temperature from a flux and **state** the conditions
   under which it equals a kinetic temperature.
7. **Compute** the daily-mean top-of-atmosphere insolation as a function of
   latitude and season, and **explain** why the summer pole receives more than the
   equator.

## Prerequisites

- [16-01-01 Atmospheric Composition and Vertical Structure](../01-atmospheric-structure-and-thermodynamics/01-atmospheric-composition.md) —
  the atmospheric state variables used to describe the receiving body.
- [02-05-05 Convection, Radiation and Combined Heat Transfer](../../02-physics/05-thermodynamics/05-convection-radiation.md) —
  radiation as one of three heat-transfer modes, and the Stefan–Boltzmann law in
  its general form.

The thermodynamics of the atmosphere itself is
[16-01 Atmospheric Structure and Thermodynamics](../01-atmospheric-structure-and-thermodynamics/README.md)
and is not repeated here. The microscopic origin of spectral lines (why real gases
absorb at particular wavelengths) is
[02-09-03 Radiation Interaction](../../02-physics/09-radiation-and-atomic-physics/03-radiation-interaction.md).

> **All models and data in this module are SYNTHETIC.** The physical constants
> ($h$, $c$, $k_B$, $\sigma$, the solar constant, the astronomical unit, the
> nominal solar radius) are standard constants and are listed with their values
> wherever they are used. The albedo and the planetary temperature below are
> chosen teaching values, printed by the demonstration. No measured spectrum,
> satellite record or published figure is used or quoted.

## 1. Intuition: everything radiates, and the two spectra barely overlap

Any body with a temperature above absolute zero emits electromagnetic radiation.
For a perfect absorber and emitter — a **blackbody** — the spectrum is fixed by one
number, the temperature, through the Planck function. Two consequences organise
this entire module.

**Wien's law: the peak wavelength is inversely proportional to temperature.**
The demonstration derives the displacement constant $b = hc/(xk_B)$ from the
fundamental constants by solving $x = 5(1-e^{-x})$, obtaining
$x = 4.965114232$ and $b = 2.897771955\times10^{-3}\ \mathrm{m\,K}$ — matching the
tabulated value to a relative difference of $6.4\times10^{-11}$. Applied to the
Sun and the Earth:

$$\lambda_{\max}^{\text{Sun}} = \frac{2.8978\times10^{-3}}{5772} = 502\ \mathrm{nm}
\quad\text{(green light)},$$

$$\lambda_{\max}^{\text{Earth}} = \frac{2.8978\times10^{-3}}{254.6}
= 11.4\ \mu\mathrm{m} \quad\text{(thermal infrared)}.$$

**The spectra are almost disjoint.** Of the Sun's blackbody flux, $99.0\%$ lies
below $4\ \mu\mathrm{m}$; of the Earth's, $99.96\%$ lies above it (the
demonstration's numbers are $0.990241$ and $0.999597$). This single fact is what
makes a greenhouse effect possible: an atmosphere can be nearly transparent in one
band and nearly opaque in the other, and that asymmetry — not any property of the
gases taken alone — is the mechanism. It also explains the practical shape of
climate physics: solar radiation is a *source* that can be measured geometrically,
while terrestrial radiation is a *response* that must be computed through
absorption.

The other organising number is the **factor four**. The Earth intercepts sunlight
on a disc of area $\pi R^2$ and must radiate it away from a sphere of area
$4\pi R^2$, so the global-mean insolation is the solar constant divided by four:
$1361/4 = 340.25\ \mathrm{W\,m^{-2}}$. With a planetary albedo of $0.30$, the
absorbed flux is $238.17\ \mathrm{W\,m^{-2}}$, which a blackbody radiates at
$254.58\ \mathrm{K}$. That number is *not* the surface temperature; the gap between
it and the observed surface temperature is the greenhouse effect, and it is
quantified in [03](03-greenhouse-effect.md).

## 2. Precise definitions

### 2.1 Radiometric quantities

| quantity | symbol | unit | meaning |
|---|---|---|---|
| Radiance | $B$ (or $L$) | $\mathrm{W\,m^{-2}\,sr^{-1}}$ | power per unit area per unit solid angle, per unit wavelength or per unit frequency |
| Irradiance / flux density | $F$, $E$ | $\mathrm{W\,m^{-2}}$ | power through a surface |
| Exitance (emitted flux density) | $M$ | $\mathrm{W\,m^{-2}}$ | power leaving a surface |

For a **Lambertian** surface (radiance independent of direction),

$$M = \pi B .$$

**This factor of $\pi$ is the source of more errors than any other in the
subject**, and the demonstration makes it explicit: integrating the Planck
function over wavelength gives $\sigma T^4/\pi$, and only after multiplying by
$\pi$ does it give $\sigma T^4$. It is also why the Stefan–Boltzmann constant
contains $\pi^5$ rather than $\pi^4$:

$$\int_0^\infty B_\lambda\,\mathrm{d}\lambda = \frac{2\pi^4k_B^4}{15h^3c^2}T^4,
\qquad
\sigma = \pi\int_0^\infty B_\lambda\,\mathrm{d}\lambda
= \frac{2\pi^5k_B^4}{15h^3c^2}.$$

### 2.2 The Planck function

$$B_\lambda(T) = \frac{2hc^2}{\lambda^5}\,
\frac{1}{\exp\!\left(\dfrac{hc}{\lambda k_BT}\right) - 1}
\qquad \mathrm{(W\,m^{-2}\,sr^{-1}\,m^{-1})}.$$

### 2.3 Emissivity, absorptivity and Kirchhoff's law

Real surfaces emit a fraction $\varepsilon_\lambda \in [0,1]$ of the blackbody
value. **Kirchhoff's law** states that for a body in local thermodynamic
equilibrium,

$$\varepsilon_\lambda = a_\lambda ,$$

where $a_\lambda$ is the spectral absorptivity. A good absorber at a wavelength is
a good emitter at that wavelength — and, crucially, *only* at that wavelength.
This is the thermodynamic fact that makes the greenhouse effect consistent: a gas
that absorbs strongly in the infrared must also emit strongly there.

### 2.4 Brightness temperature

Given a measured spectral radiance, the **brightness temperature** $T_B$ is the
temperature of the blackbody with the same radiance. If a measured flux density
$F$ is emitted by an isothermal blackbody surface, $F = \sigma T^4$, so

$$T_B = \left(\frac{F}{\sigma}\right)^{1/4}.$$

$T_B$ equals the kinetic temperature only if the surface is black and nothing
intervenes between it and the instrument. For a grey surface, $T_B = \varepsilon^{1/4}T$;
for an atmosphere with absorption, $T_B$ is generally *lower* than the surface
temperature and the deficit measures the intervening absorption.

## 3. Derivations

### 3.1 Wien's displacement law

Maximise $B_\lambda$ with respect to $\lambda$. Write $x = hc/(\lambda k_BT)$; then
$B_\lambda \propto x^5/(e^x-1)$ (up to constants), and

$$\frac{\mathrm{d}}{\mathrm{d}x}\left(\frac{x^5}{e^x-1}\right) = 0
\;\Longrightarrow\;
\frac{5x^4(e^x-1) - x^5e^x}{(e^x-1)^2} = 0
\;\Longrightarrow\;
5(e^x-1) = xe^x,$$

$$x = 5\left(1-e^{-x}\right).$$

The nontrivial root is $x = 4.965114232$ (Newton's method, as in the
demonstration), giving

$$\boxed{\;\lambda_{\max}T = \frac{hc}{xk_B} = b = 2.897771955\times10^{-3}\
\mathrm{m\,K}\;}$$

The constant is *derived*, not fitted: it contains $h$, $c$, $k_B$ and the root of
a transcendental equation.

### 3.2 The Stefan–Boltzmann law

Integrate the Planck function over all wavelengths. Substituting
$x = hc/(\lambda k_BT)$:

$$\int_0^\infty B_\lambda\,\mathrm{d}\lambda
= \frac{2k_B^4T^4}{h^3c^2}\int_0^\infty\frac{x^3}{e^x-1}\,\mathrm{d}x
= \frac{2k_B^4T^4}{h^3c^2}\cdot\frac{\pi^4}{15},$$

using $\int_0^\infty x^3/(e^x-1)\,\mathrm{d}x = \Gamma(4)\zeta(4) = \pi^4/15$.
Multiplying by $\pi$ for the hemispheric geometry:

$$\boxed{\;F = \sigma T^4, \qquad \sigma = \frac{2\pi^5k_B^4}{15h^3c^2}
= 5.670374419\times10^{-8}\ \mathrm{W\,m^{-2}\,K^{-4}}\;}$$

The demonstration verifies both halves numerically: the integral
$\int x^3/(e^x-1)\,\mathrm{d}x$ comes out as $6.493939402$ against $\pi^4/15 =
6.493939402$ (relative difference $2.0\times10^{-11}$), and $\sigma$ computed from
the constants agrees with the tabulated value to $3.3\times10^{-11}$. **The
agreement is a check on the arithmetic and on the numerical quadrature, not a
measurement** — no experiment is involved.

### 3.3 The solar effective temperature from the solar constant

The solar constant $S = 1361\ \mathrm{W\,m^{-2}}$ is the flux density at $1\
\mathrm{AU} = 1.495978707\times10^{11}\ \mathrm{m}$. The Sun's luminosity is
therefore

$$L_\odot = S \times 4\pi\,(1\ \mathrm{AU})^2
= 1361 \times 4\pi \times 2.23796\times10^{22} = 3.8275\times10^{26}\ \mathrm{W}.$$

If the Sun radiates as a blackbody of radius $R_\odot = 6.957\times10^{8}\
\mathrm{m}$, then $L_\odot = 4\pi R_\odot^2\sigma T_{\text{eff}}^4$, so

$$\boxed{\;T_{\text{eff}} = \left(\frac{L_\odot}{4\pi R_\odot^2\sigma}\right)^{1/4}
= \left(\frac{S\,(1\,\mathrm{AU})^2}{R_\odot^2\sigma}\right)^{1/4}
= 5771.8\ \mathrm{K}\;}$$

checked by Wien: $b/T_{\text{eff}} = 502\ \mathrm{nm}$, in the visible. **The
argument uses no knowledge of the Sun's interior.** Three measured or defined
numbers — the solar constant, the distance, and the radius — plus the blackbody
laws give the photospheric temperature. That is the strongest possible
demonstration that the blackbody model is doing real work.

### 3.4 Global-mean insolation and the factor four

The Earth intercepts sunlight over $\pi R_E^2$ and distributes it over
$4\pi R_E^2$:

$$F_{\text{mean}} = \frac{S\,\pi R_E^2}{4\pi R_E^2} = \frac{S}{4}
= \frac{1361}{4} = 340.25\ \mathrm{W\,m^{-2}}.$$

With planetary albedo $a$, the absorbed flux is $S(1-a)/4$; the equilibrium
condition for a blackbody is

$$\frac{S(1-a)}{4} = \sigma T_e^4
\;\Longrightarrow\;
T_e = \left(\frac{S(1-a)}{4\sigma}\right)^{1/4}
= \left(\frac{1361\times0.70}{4\times5.670374419\times10^{-8}}\right)^{1/4}
= 254.58\ \mathrm{K}.$$

Three remarks that matter later:

- **This is not a surface temperature.** A blackbody with no atmosphere would have
  this *surface* temperature; the real Earth has a warmer surface and a colder
  effective radiating temperature, and the difference is a *vertical* statement
  about where the atmosphere radiates from ([03](03-greenhouse-effect.md)).
- **The albedo is an input, not a prediction.** $a = 0.30$ is a chosen teaching
  value here. Reflectivity depends on clouds, ice and surface type, and its
  response to warming is one of the largest uncertainties in climate science
  ([04-02](../04-climate-system-and-feedbacks/02-climate-feedbacks.md)).
- **The factor four is geometry, not physics.** It assumes uniform absorption over
  the sphere, which is exact for an annual mean and wrong for any instant or
  latitude band.

### 3.5 Daily-mean insolation versus latitude

For a planet with obliquity, the daily-mean top-of-atmosphere insolation at
latitude $\phi$ with solar declination $\delta$ is

$$\bar F(\phi,\delta) = \frac{S}{\pi}\left[
h_0\sin\phi\sin\delta + \cos\phi\cos\delta\sin h_0\right],
\qquad
h_0 = \arccos\left(-\tan\phi\tan\delta\right),$$

with $h_0$ the half-day length in radians. At the equinox ($\delta = 0$),
$h_0 = \pi/2$ and $\bar F = (S/\pi)\cos\phi$; at the pole in summer,
$h_0 = \pi$ and $\bar F = S\sin\delta$.

The demonstration tabulates it:

| $\phi$ | equinox ($\delta=0$) | June solstice ($\delta = 23.44^\circ$) |
|---|---|---|
| 0° | 433.2 | 397.5 |
| 30° | 375.2 | 490.4 |
| 45° | 306.3 | 499.3 |
| 60° | 216.6 | 492.4 |
| 90° | 0.0 | 541.4 |

**The summer pole receives more than the equator.** At $90^\circ$ latitude in June
the Sun never sets, and $S\sin 23.44^\circ = 541.4\ \mathrm{W\,m^{-2}}$ exceeds the
equatorial daily mean of $397.5\ \mathrm{W\,m^{-2}}$. That inversion is what
reverses the pole-to-equator temperature gradient, and through the thermal wind of
[16-01-05](../01-atmospheric-structure-and-thermodynamics/05-atmospheric-dynamics-basics.md)
it reverses the sign of the zonal wind — the stratospheric sudden warmings and the
monsoonal reversals both trace back to this single line of arithmetic.

## 4. Physical interpretation

- **Temperature is a wavelength.** Wien's law means that a change in temperature is
  a change in where the energy appears, and instruments are therefore designed
  band by band rather than as "thermometers".
- **Blackbody radiation is a limit, not a description.** The Sun is close to it in
  the visible continuum; the Earth's surface is close to it in the infrared (with
  $\varepsilon \approx 0.95$–$1.0$ for water and rock); the atmosphere is emphatically
  *not* a blackbody, because it absorbs and emits in narrow bands.
- **Kirchhoff's law is the consistency requirement.** Without it, one could
  postulate an atmosphere transparent to outgoing radiation but opaque to incoming
  — which would violate the second law in a closed system. The greenhouse effect is
  not a radiation trap; it is a change in the *altitude* from which the planet
  effectively radiates, and it depends on $\varepsilon_\lambda$ being the same for
  emission and absorption at each wavelength.
- **The factor $\pi$ is a geometry statement about the hemisphere.** It appears
  whenever a radiance is converted to a flux from a flat surface, and it disappears
  from ratios.
- **The solar constant is measured, not derived.** Its value, and its small
  variation with solar activity, is an observational result; the *blackbody* use of
  it above is a model that the derivation of $T_{\text{eff}}$ then tests for
  self-consistency.

## 5. Worked numerical examples

**Example 1 — the factor of $\pi$, demonstrated.**

At $T = 255\ \mathrm{K}$, numerically integrating the Planck function from
$1\ \mathrm{nm}$ to $3\ \mathrm{cm}$ on a geometric grid gives

$$\int_0^\infty B_\lambda\,\mathrm{d}\lambda
= 7.631723\times10^{1}\ \mathrm{W\,m^{-2}\,sr^{-1}},$$

while

$$\frac{\sigma T^4}{\pi} = \frac{5.670374419\times10^{-8}\times255^4}{\pi}
= \frac{239.7576}{3.14159} = 76.3172\ \mathrm{W\,m^{-2}\,sr^{-1}},$$

$$\pi \times 76.3172 = 239.7576 = \sigma T^4 = 2.397576\times10^{2}\ \mathrm{W\,m^{-2}}.\;\checkmark$$

The ratio $\int B\,\mathrm{d}\lambda/(\sigma T^4) = 0.31831 = 1/\pi$ at *every*
temperature — $255$, $288$ and $5772\ \mathrm{K}$ all give $0.31831$ — which is
the signature of a missing steradian rather than a numerical error.

**Example 2 — the Sun, from the solar constant.**

$L_\odot = 3.8275\times10^{26}\ \mathrm{W}$; $R_\odot = 6.957\times10^{8}\
\mathrm{m}$, so $4\pi R_\odot^2 = 6.0821\times10^{18}\ \mathrm{m^2}$;

$$\sigma T_{\text{eff}}^4 = \frac{3.8275\times10^{26}}{6.0821\times10^{18}}
= 6.2930\times10^{7}\ \mathrm{W\,m^{-2}},$$

$$T_{\text{eff}} = \left(\frac{6.2930\times10^{7}}{5.670374419\times10^{-8}}
\right)^{1/4} = (1.1098\times10^{15})^{1/4} = 5771.8\ \mathrm{K}.$$

Cross-check with Wien: $\lambda_{\max} = 2.897772\times10^{-3}/5771.8
= 5.021\times10^{-7}\ \mathrm{m} = 502.1\ \mathrm{nm}$ — green light, as it must
be for a star whose visual magnitude is what it is.

**Example 3 — the two spectra, in numbers.**

| $T$ (K) | fraction of flux below $4\ \mu\mathrm{m}$ | above |
|---|---|---|
| 5772 (photosphere) | 0.990241 | 0.009759 |
| 288 (surface) | 0.001448 | 0.998552 |
| 255 (effective radiating) | 0.000403 | 0.999597 |

So the overlap region — where an atmospheric constituent could be simultaneously
important for sunlight and for terrestrial radiation — carries under $1\%$ of the
solar energy and under $0.05\%$ of the terrestrial energy. A molecule absorbing at
$4\ \mu\mathrm{m}$ or longer is therefore radiatively irrelevant to the incoming
beam by construction. This is why the greenhouse effect can be described with a
single "infrared opacity" and why the same molecules barely perturb the solar
budget.

The demonstration also computes that $97.87\%$ of the Sun's blackbody flux arrives
below $3\ \mu\mathrm{m}$.

## 6. Assumptions and regime of validity

| Assumption | Where used | What breaks it |
|---|---|---|
| Blackbody emission | all of §3 | Real surfaces have $\varepsilon_\lambda < 1$ and vary with wavelength (water $\approx0.98$ in the thermal infrared, deserts lower in the "window") |
| Local thermodynamic equilibrium | Kirchhoff's law | Fails in the upper atmosphere and in the solar corona, where the source function decouples from the local temperature; emission becomes non-local and can be in emission lines |
| Spherical, uniform absorption of sunlight | the factor four | Exact only as an annual, global mean; instantaneous and zonal values differ by up to a factor of two |
| A single, constant albedo | $T_e$ | Albedo depends on cloud amount, cloud phase, sea ice and surface type, and it changes with climate |
| No atmosphere for $T_e$ | §3.4 | The real Earth has one; the $254.6\ \mathrm{K}$ is a reference state, not a prediction |
| Solar constant constant | §3.3 | It varies by about $0.1\%$ over the solar cycle, and by $6.8\%$ over the year because the orbit is eccentric — the demonstration uses the mean value |
| Wien's law locates the *spectral radiance* peak | §3.1 | In frequency space the peak is at a different wavelength; both are correct for different arguments |
| Radiative equilibrium | the whole energy-balance picture | Advection and latent heat move energy as well; the top-of-atmosphere balance is radiative, but the surface balance is not |

**Climate-claim discipline.** This lesson supplies three things of very different
status:

1. **The blackbody laws** are physics, verified here to $10^{-11}$ against the
   constants that define them.
2. **$T_e = 254.58\ \mathrm{K}$ for $a = 0.30$** is a *model*: a single-layer,
   zero-dimensional, blackbody, albedo-fixed calculation. It is the reference
   against which the greenhouse effect is measured, and it is not a prediction of
   any real temperature.
3. **The solar constant $S = 1361\ \mathrm{W\,m^{-2}}$** is a *measured* standard
   value; its small variability is an observational result.

Confusing (2) with an observation is the commonest error in informal discussions of
the greenhouse effect: "the Earth should be $-18.6\ \mathrm{^\circ C}$" is a
statement about a *model*, not about the Earth. What is observed is the surface
temperature, and the fact that it is about $33\ \mathrm{K}$ higher is the
phenomenon to be explained — a job for
[02 Radiative Transfer in the Atmosphere](02-radiative-transfer-atmosphere.md) and
[03 The Greenhouse Effect](03-greenhouse-effect.md).

## 7. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| Wavelength | $\lambda$ | m (nm, µm) | |
| Spectral radiance | $B_\lambda$ | $\mathrm{W\,m^{-2}\,sr^{-1}\,m^{-1}}$ | |
| Flux density / irradiance | $F$ | $\mathrm{W\,m^{-2}}$ | |
| Stefan–Boltzmann constant | $\sigma$ | $\mathrm{W\,m^{-2}\,K^{-4}}$ | $F = \sigma T^4$ ✔ |
| Wien constant | $b$ | m K | $\lambda_{\max}T$ ✔ |
| Solar constant | $S$ | $\mathrm{W\,m^{-2}}$ | |
| Brightness temperature | $T_B$ | K | $T_B = (F/\sigma)^{1/4}$ ✔ |
| Solid angle | $\Omega$ | sr | $M = \pi B$: sr⁻¹ × sr = dimensionless ✔ |

The dimensional check that catches the factor-of-$\pi$ error: an exitance must be
$\mathrm{W\,m^{-2}}$ and a radiance $\mathrm{W\,m^{-2}\,sr^{-1}}$, so *something*
must multiply by a solid angle. In the blackbody case that something is
$\pi\ \mathrm{sr}$, and if a computed $\sigma$ comes out $1/\pi$ too small, the
hemispheric integral was omitted.

## 8. Python demonstration

[`code/solar_and_terrestrial_radiation_demo.py`](code/solar_and_terrestrial_radiation_demo.py)
prints every number quoted above. It:

1. states the Planck function and both of its limits;
2. solves $x = 5(1-e^{-x})$ by Newton's method and derives
   $b = 2.897771955\times10^{-3}\ \mathrm{m\,K}$, agreeing with the tabulated value
   to $6.4\times10^{-11}$;
3. evaluates $\int_0^\infty x^3/(e^x-1)\,\mathrm{d}x$ numerically and compares it
   with $\pi^4/15$ (agreement $2.0\times10^{-11}$), then computes $\sigma$ from
   $h$, $c$ and $k_B$ and compares it with the tabulated constant
   ($3.3\times10^{-11}$);
4. integrates the Planck function directly and shows explicitly that the radiance
   integral is $\sigma T^4/\pi$ while $\pi$ times it is $\sigma T^4$;
5. derives the solar luminosity ($3.8275\times10^{26}\ \mathrm{W}$) and effective
   temperature ($5771.8\ \mathrm{K}$) from the solar constant, the AU and the
   nominal solar radius;
6. computes the global-mean insolation, the absorbed flux and the effective
   radiating temperature ($254.58\ \mathrm{K}$);
7. tabulates the band fractions at three temperatures, and the fraction of the
   solar flux below $3\ \mu\mathrm{m}$;
8. tabulates brightness temperatures for five fluxes;
9. tabulates the daily-mean insolation versus latitude for two declinations.

```bash
cd 16-atmosphere-climate/02-radiation-and-energy-balance/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python solar_and_terrestrial_radiation_demo.py
```

## 9. Exercises

Graded problems with worked solutions:
[`exercises/01-solar-and-terrestrial-radiation-exercises.md`](exercises/01-solar-and-terrestrial-radiation-exercises.md)
and
[`exercises/01-solar-and-terrestrial-radiation-solutions.md`](exercises/01-solar-and-terrestrial-radiation-solutions.md).

## Mastery checkpoint

Without notes:

> A planet orbits at $2.0\ \mathrm{AU}$ with planetary albedo $0.20$ and radius
> $6.0\times10^{6}\ \mathrm{m}$. **(a)** Compute its global-mean insolation and its
> effective radiating temperature. **(b)** Compute the wavelength at which it emits
> most strongly and state which spectral region that is. **(c)** A satellite
> measures a flux density of $150\ \mathrm{W\,m^{-2}}$ emerging from the planet;
> compute the brightness temperature and state two reasons it might differ from
> your answer to (a). **(d)** Its star has radius $1.2$ solar radii and the planet
> receives $S = 340\ \mathrm{W\,m^{-2}}$; compute the star's effective temperature
> using only blackbody relations. **(e)** State which of (a)–(d) are measurements,
> which are model outputs, and which are definitions.

## Common pitfalls

1. **Forgetting the factor of $\pi$** between radiance and exitance. The
   demonstration's check — that $\int B_\lambda\,\mathrm{d}\lambda$ must be
   $\sigma T^4/\pi$, not $\sigma T^4$ — is the remedy.
2. **Using the solar constant directly as a mean surface flux.** The global mean is
   $S/4$; the $1361\ \mathrm{W\,m^{-2}}$ applies only perpendicular to the beam at
   the top of the atmosphere at $1\ \mathrm{AU}$.
3. **Treating the effective radiating temperature as the surface temperature.**
   They differ by the greenhouse effect, and for a real planet the difference is
   the thing being studied.
4. **Quoting a "blackbody" solar temperature without saying which temperature it
   is.** The *effective* temperature is a flux-weighted average; the *brightness*
   temperature at a given wavelength is not the same number.
5. **Applying Wien's law across coordinate changes.** The peak in $B_\lambda$ and
   the peak in $B_\nu$ occur at different wavelengths; both are correct.
6. **Assuming emissivity is one.** For real surfaces and, especially, for an
   atmosphere with narrow absorption bands it is very far from one.
7. **Believing the derived $T_e$ is a prediction.** It is a one-line model whose
   albedo was assumed.

## Related modules

- [16-01-01 Atmospheric Composition and Vertical Structure](../01-atmospheric-structure-and-thermodynamics/01-atmospheric-composition.md) —
  the state variables of the receiving atmosphere.
- [16-01-05 Atmospheric Dynamics: Coriolis, Geostrophic and Thermal Wind](../01-atmospheric-structure-and-thermodynamics/05-atmospheric-dynamics-basics.md) —
  the thermal wind whose seasonal reversal §3.5 explains.
- [02 Radiative Transfer in the Atmosphere](02-radiative-transfer-atmosphere.md) —
  what happens to the radiation as it crosses the atmosphere.
- [03 The Greenhouse Effect: Physics, Not Rhetoric](03-greenhouse-effect.md) —
  the difference between $254.6\ \mathrm{K}$ and the surface temperature.
- [04 Earth Energy Balance and Global Mean Temperature](04-earth-energy-balance.md) —
  the energy budget this lesson's radiation feeds into.
- [02-05-05 Convection, Radiation and Combined Heat Transfer](../../02-physics/05-thermodynamics/05-convection-radiation.md) —
  radiation in the general heat-transfer context.
- [02-10-03 Radiative Transfer](../../02-physics/10-optics-and-photometry/03-radiative-transfer.md) —
  the general transport equation.
- [01-12-04 Numerical Integration](../../01-mathematics/12-numerical-methods/04-numerical-integration.md) —
  the quadrature used to verify the two laws.
- [17-01-01 The Electromagnetic Spectrum in Remote Sensing](../../17-remote-sensing-gis/01-remote-sensing-physics/01-em-spectrum-remote-sensing.md) —
  where these bands are actually used to measure the planet.
