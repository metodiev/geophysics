---
id: 04-08-04
title: "Exoplanets, Habitability and Observational Constraints"
level: graduate
prereqs: ["04-08-01", "04-08-02", "16-02-01"]
estimated_minutes: 75
tags: [exoplanets, habitability, planet-detection, mass-radius, error-propagation]
---

# Exoplanets, Habitability and Observational Constraints

An exoplanet is a body that has never been seen as an object. It is inferred from
a periodic dip in a star's brightness, or a periodic wobble in a star's spectrum,
and everything else — its radius, its mass, its density, its temperature, its
atmosphere, its habitability — is a further inference from that. This makes
exoplanetary science the purest case of a theme that runs through this whole
module: **the measurement is small, the model is large, and the honest result
carries the model with it.**

The lesson is therefore built as an error-propagation exercise. It derives the
four relations that turn a light curve and a spectrum into a radius and a mass,
computes the uncertainties that propagate through them, and then asks what
habitability claims can be supported by a radius, an incident flux and a mass.
The answer is a specific and useful one: a radius and a flux are consistent with a
range of compositions and atmospheres, and a habitability claim is a statement
about that range, not about the planet. One section is deliberately a
demonstration of a *correct* piece of physics giving a *wrong* answer because its
regime of validity was not checked, because that is the characteristic failure
mode of a field in which every quantity is an inference.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the transit depth from geometry and compute it in parts per million
   for a given planet-to-star radius ratio.
2. **Derive** the geometric transit probability and the transit duration for a
   circular orbit, and explain how the two weight the observed catalogue.
3. **Derive** the radial-velocity semi-amplitude from Kepler's third law and
   conservation of momentum, and compute it for an Earth-mass planet.
4. **Compute** the minimum mass, the exact averages $\mathrm{E}[\sin i] = \pi/4$
   and $\mathrm{E}[1/\sin i] = \pi/2$, and the Jensen-inequality error of using
   one for the other.
5. **Propagate** the stellar radius uncertainty into a planet radius and therefore
   into a density, and state which uncertainty dominates.
6. **Compute** an equilibrium temperature, recover the Earth's greenhouse
   increment as a residual, and demonstrate explicitly that a habitable-zone edge
   is an atmosphere-dependent model output.
7. **Derive** the mass–radius relations of a constant-density body, a
   self-compressed solid body and a fully degenerate gas, and state the regime in
   which the degenerate relation fails for real giant planets.
8. **State** what a radius, a flux and a mass can and cannot establish about
   habitability, and write the sentence that reports the inference honestly.

## Prerequisites

- [04-08-01 Solar System Architecture and Formation](./01-solar-system.md) —
  Kepler's third law, equilibrium temperature, and the density-implies-
  composition argument that this lesson applies to systems we cannot visit.
- [04-08-02 Planetary Interiors and Magnetic Fields](./02-planetary-interiors.md)
  — hydrostatic equilibrium and the equation of state needed to turn a mass and a
  radius into an interior.
- [16-02-01 Solar and Terrestrial Radiation, Blackbody Laws](../../16-atmosphere-climate/02-radiation-and-energy-balance/01-solar-and-terrestrial-radiation.md)
  — the radiative balance on which the equilibrium temperature and the habitable
  zone rest.

## 1. What is actually measured, and what follows

Two techniques supply almost all of the data, and each measures one geometric
quantity.

**Transit photometry** measures the fractional dimming of a star when a planet
crosses its disk. The observable is a *ratio of areas*, and it therefore gives
the planet's radius in units of the star's radius.

**Radial velocity** measures the periodic Doppler shift of the star's spectral
lines as it orbits the star–planet barycentre. The observable is a *line-of-sight
velocity*, and it gives the planet's mass times $\sin i$, where $i$ is the
unknown orbital inclination.

Everything else is derived, and the derivation chain is worth stating once,
because it is where the uncertainties accumulate:

| Quantity | From | Depends on |
|---|---|---|
| Planet radius | transit depth | the **stellar radius**, which is itself an inference |
| Orbital period | either | nothing else |
| Orbit size | Kepler's third law | the stellar mass |
| Minimum mass | RV amplitude | the stellar mass, and $\sin i$ |
| Density | mass and radius | both of the above, cubed in the radius |
| Incident flux | orbit size | the stellar luminosity and the distance |
| Temperature | flux and albedo | the **albedo**, which is assumed |
| Composition | density | an equation of state and a core fraction |

The two entries in bold are the ones that dominate the error budget and that are
themselves model-dependent. A planet's density is limited by the *star*, not by
the planet's own measurement; a planet's temperature is limited by an albedo
nobody has measured.

## 2. Transits

**Depth.** The planet blocks a fraction of the stellar disk equal to the ratio of
their areas, so

$$\delta = \frac{\Delta F}{F} = \left(\frac{R_p}{R_*}\right)^2 . \tag{1}$$

An Earth-sized planet in front of a Sun-sized star gives
$(6.371\times10^6/6.957\times10^8)^2 = 8.39\times10^{-5}$, i.e. **84 parts per
million**. That number explains the history of the field: it is a space-instrument
problem because the stellar variability, not the detector noise, is usually the
limiting term.

**Probability.** A transit occurs if the planet's impact parameter falls within
$R_* + R_p$ of the line of sight, so for randomly oriented orbits

$$p = \frac{R_* + R_p}{a} \approx \frac{R_*}{a} \quad (R_p \ll R_*) . \tag{2}$$

For a Sun-like star this is 9.3 per cent at 0.05 au, 2.3 per cent at 0.2 au and
0.465 per cent at 1 au — **one in 215**. Combined with the shorter period at small
$a$, which multiplies the number of transits per unit time, (2) is the reason the
catalogue is dominated by close-in planets before any instrument is mentioned.
The observed distribution is the product of the true distribution and this
geometric and cadence weighting; removing the weighting is what turns a catalogue
into a population.

**Duration.** For a circular orbit the transit lasts

$$t = \frac{P}{\pi}\arcsin\!\left(\frac{R_*+R_p}{a}\right)
\approx \frac{PR_*}{\pi a} , \tag{3}$$

which for an Earth-analogue is 13.0 h. The duration is also what makes a
grazing transit diagnosable: a planet whose impact parameter is close to $R_*$
produces a shallow, V-shaped and short transit, and the impact parameter is
recoverable from the shape — which is why a light curve provides $R_p/R_*$,
$a/R_*$ and $i$ from one measurement.

## 3. Radial velocity

**The semi-amplitude, derived.** The star and planet orbit their barycentre, so
$a_* = (m_p/M)a$ with $M = M_* + m_p$, and the star's orbital speed is
$v_* = 2\pi a_*/P$. Kepler's third law,
$a^3 = GMP^2/(4\pi^2)$, removes $a$:

$$v_* = \frac{2\pi}{P}\frac{m_p}{M}a
= \left(\frac{2\pi G}{P}\right)^{1/3}\frac{m_p}{M^{2/3}} , \tag{4}$$

and the observed semi-amplitude is this times $\sin i$ and an eccentricity factor:

$$K = \left(\frac{2\pi G}{P}\right)^{1/3}
\frac{m_p\sin i}{M^{2/3}}\frac{1}{\sqrt{1-e^2}} . \tag{5}$$

The eccentric factor is exact, not an approximation. For an Earth-mass planet at
1 au around a Sun-like star, (5) gives $K = 0.0894$ m s⁻¹ = **8.9 cm s⁻¹**, which
is two orders of magnitude below the Sun's own granulation noise. That single
number is why terrestrial-mass planets are found from space, in the infrared, and
around small quiet stars.

**The minimum mass, and the two averages.** Radial velocity measures
$m_p\sin i$, so every mass is a *minimum*. For isotropically oriented orbits
$\cos i$ is uniform on $[0,1]$, so $i$ has density $\sin i$ and

$$\mathrm{E}[\sin i] = \int_0^{\pi/2}\sin^2i\,\mathrm{d}i = \frac{\pi}{4} = 0.7854,
\qquad
\mathrm{E}\!\left[\frac{1}{\sin i}\right]
= \int_0^{\pi/2}\sin i\,\frac{1}{\sin i}\,\mathrm{d}i = \frac{\pi}{2} = 1.5708 . \tag{6}$$

The consequences are opposite in direction and matter for population statistics:

- The mean *true mass* of a population is $\pi/2 = 1.571$ times the mean *minimum*
  mass, because $m_\mathrm{true} = m_\mathrm{min}/\sin i$.
- Using $1/\mathrm{E}[\sin i] = 4/\pi = 1.273$ instead is wrong by **23 per
  cent**, and the error is Jensen's inequality: the reciprocal of a mean is not
  the mean of the reciprocal.

A Monte Carlo with two million random orientations reproduces both averages to
better than 0.5 per cent, and the fraction of orbits with $\sin i < 0.5$ comes out
0.1336 against the analytic $1-\sqrt3/2 = 0.1340$.

## 4. Error propagation: the star matters more than the planet

**Radius.** Inverting (1) gives $R_p = R_*\sqrt\delta$, so a fractional error in
the stellar radius passes through unchanged:

$$\frac{\delta R_p}{R_p} = \frac{\delta R_*}{R_*} . \tag{7}$$

**Density.** With $\rho \propto M/R^3$,

$$\left(\frac{\delta\rho}{\rho}\right)^2
= \left(\frac{\delta M}{M}\right)^2 + 9\left(\frac{\delta R_*}{R_*}\right)^2 , \tag{8}$$

so a 5 per cent stellar radius error is a **15 per cent density error** — larger
than the radial-velocity mass error for most systems. The dominant systematic in
a planet's density is therefore the star, and a density quoted without the
stellar radius uncertainty is quoted with an unstated error of the same order as
the quantity itself.

**Mass.** When both a transit and an RV are available, the transit fixes $\sin i$
through the impact parameter and the density of the star (the transit of a
*known* star gives $\sin i$ directly), so the mass is no longer a minimum. This is
the reason that the transit-plus-RV pair is the productive combination: each
measurement supplies what the other cannot determine.

## 5. Temperature, and the habitable zone as a model output

The equilibrium temperature of an airless body follows from the same flux balance
as in lesson 01:

$$T_\mathrm{eq} = \left[\frac{(1-A)L}{16\pi\sigma a^2}\right]^{1/4} . \tag{9}$$

With $A = 0.3$ this gives 254.6 K at 1 au, and the Earth's measured mean surface
temperature of about 288 K then implies a greenhouse increment of **33.4 K**,
obtained as a residual rather than asserted. The temperature depends on the
albedo, on the star's luminosity and on the distance — and only the second of the
three is measured well.

**A naive habitable zone** is the set of distances at which an airless body with
$A = 0.3$ lies between the freezing and boiling points of water: 0.870 au to
0.466 au from (9). That is not the conventional habitable zone, and the
difference is instructive. Adding the Earth's 33 K of greenhouse warming moves the
freezing boundary from 0.870 au to 1.125 au — **outward by 29 per cent**, for one
assumed atmosphere. A different atmosphere moves it somewhere else again, and a
runaway greenhouse, a carbonate–silicate thermostat, clouds, tidal locking and
the stellar spectrum all enter.

**The honest statement.** The conventional habitable zone is defined by
empirically calibrated flux limits derived from one-dimensional climate models,
and its edges are model outputs with published uncertainties. A planet inside the
zone is **a candidate for surface liquid water**, not a detection of it. No
arithmetic in this lesson changes that, and any sentence that reports a
habitability claim must name the atmosphere model it assumes. This is a graduate
lesson partly for that reason: the physics is straightforward and the epistemic
discipline is the hard part.

## 6. Mass, radius and what a density can mean

**The uncompressed limit.** For a body that cannot compress,
$R = (3M/4\pi\rho)^{1/3}$, so $R \propto M^{1/3}$.

**A self-compressed solid body.** Model the compression with a Murnaghan equation
of state, $\rho = \rho_0(1 + K_0'P/K_0)^{1/K_0'}$, with $K_0' \approx 4$ for
silicates, and integrate the hydrostatic equations. The result is a mass–radius
relation whose local slope sits between two analytic limits:

- uncompressed: $R \propto M^{1/3}$ (exponent 0.333);
- strongly compressed: with $\rho \propto P^{1/4}$ and $P \sim GM^2/R^4$,
  $M \sim G^{1/4}M^{1/2}R^2$ gives $R \propto M^{1/4}$ (exponent 0.250).

The integration over 0.5 to 10 Earth masses gives an exponent of **0.294**,
between the two limits and close to the empirical slope of the observed
rocky-planet population. That is a satisfying result, and it is worth being clear
about why it is satisfying: the exponent was not fitted, it emerged from the
integration, and it interpolates between two limits that were derived separately.

The model is not a prediction of any particular planet. With one composition, one
constant $K_0'$, no iron core and no phase transitions it gives about 7000 km for
an Earth-mass body against the Earth's 6371 km, and the difference is mostly the
core. **A measured radius therefore constrains a range of compositions, not a
composition**, and a radius is not a composition.

**A degenerate limit, and a regime failure.** For a non-relativistic degenerate
electron gas the Fermi pressure is $P = K\rho^{5/3}$ with

$$K = \tfrac15\hbar^2(3\pi^2)^{2/3}/\left(m_e(\mu_e m_u)^{5/3}\right) , \tag{10}$$

which is derived by weighting the filled Fermi sphere and contains no fitted
constant. Combining it with hydrostatic support gives

$$GM^2/R^4 \sim K(M/R^3)^{5/3}
\quad\Longrightarrow\quad
R \sim \frac{K}{G}M^{-1/3} . \tag{11}$$

The scaling is a genuine piece of physics and it predicts that a **more massive**
degenerate body is **smaller**, because gravity compresses a body whose pressure
rises only as $\rho^{5/3}$.

Calibrated on one Jupiter mass (which fixes the unknown dimensionless constant of
the hydrostatic estimate), (11) predicts 0.794, 0.585 and 0.464 Jupiter radii for
2, 5 and 10 Jupiter masses. The observed mass–radius relation for giant planets is
much flatter than that: across the range where such planets are measured, radii
stay within a factor of about two of one Jupiter radius and do not shrink with
mass.

**This is a regime failure, and the lesson is worth more than the formula.** The
degenerate scaling applies to a *cold, fully degenerate* body. A giant planet of a
few Jupiter masses is neither: its interior is only partly degenerate and its
thermal content and formation history keep it inflated. The physics of the Fermi
pressure is correct and the conclusion drawn from it is wrong, because the regime
was not checked. It is the characteristic error of this field, and it is why every
inference in this lesson is stated with its model.

## 7. What habitability would require

A habitable-zone membership is one condition out of several, and the others are
not measured at all. To claim that a planet *could* support surface liquid water,
one needs at least: a surface and a pressure sufficient to keep water liquid; an
energy source — for a known system, stellar flux, though tidal and radiogenic
heating matter for a moon or an ice-covered body; a volatile inventory and a
delivery mechanism; a chemistry that supplies the elements biology uses; and
*stability* over the timescale on which life would have to arise.

Of these, a transit gives the radius (hence, with a mass, a *bulk* density that
excludes a very low-density atmosphere only in the crudest sense); a radial
velocity gives the mass; and the combination gives a bulk composition. The
incident flux gives an equilibrium temperature, and the temperature is where the
atmosphere enters, because a greenhouse can move the surface temperature by tens
of kelvin. **What a radius, a flux and a mass cannot do is distinguish an
Earth-like planet from a Venus-like one, or from an airless one with the same
bulk density.** That distinction requires a spectrum.

The corresponding honest sentence has a specific form. Not "the planet is
habitable", and not "the planet is in the habitable zone, therefore it has liquid
water", but: *"the planet's radius and mass are consistent with a rock–iron
composition, its incident flux places it within the model-dependent habitable
zone of its star as defined by a stated set of climate models, and a spectrum
would be needed to establish whether it has an atmosphere at all."* That sentence
can be reviewed. The others cannot.

## 8. Physical interpretation

- **Two observables, many inferences.** A transit gives a radius ratio, an RV
  gives a mass times $\sin i$, and everything else is a model.
- **The star is the limiting factor for a radius and a density.** A 5 per cent
  stellar radius error is a 15 per cent density error, which is larger than the
  mass error in most systems.
- **The $1/\sin i$ correction is not the reciprocal of the $\sin i$ average.**
  Population statistics that confuse them are biased by 23 per cent.
- **A habitable-zone edge is a model output.** Moving one assumed atmosphere
  shifts the freezing boundary by 29 per cent.
- **A mass–radius relation is a family of compositions.** It is a diagnostic of
  the *plausible* interior, and the word plausible belongs in the sentence.
- **A correct scaling outside its regime gives a wrong answer.** The degenerate
  $R \propto M^{-1/3}$ result is the demonstration.

## 9. Units and dimensional analysis

| Quantity | Expression | Units |
|---|---|---|
| Transit depth | $(R_p/R_*)^2$ | dimensionless |
| Transit probability | $(R_*+R_p)/a$ | dimensionless |
| Transit duration | $(P/\pi)\arcsin[(R_*+R_p)/a]$ | s |
| RV semi-amplitude | $(2\pi G/P)^{1/3}m_p\sin i/M^{2/3}$ | (m³ s⁻²/s)$^{1/3}$ × kg/kg$^{2/3}$ = m s⁻¹ |
| Density error | $\sqrt{(\delta M/M)^2 + 9(\delta R/R)^2}$ | dimensionless |
| Equilibrium temperature | $[(1-A)L/(16\pi\sigma a^2)]^{1/4}$ | K |
| Degenerate pressure coefficient | $\tfrac15\hbar^2(3\pi^2)^{2/3}/[m_e(\mu_em_u)^{5/3}]$ | (J s)² kg⁻¹ m⁻⁶ ... = Pa (kg m⁻³)$^{-5/3}$ |

The last row is the one worth doing carefully, because it is where a units error
hides: $K$ must be in Pa divided by $(\mathrm{kg\,m^{-3}})^{5/3}$ for
$P = K\rho^{5/3}$ to be dimensionally consistent, which is
$\mathrm{kg\,m^{-1}\,s^{-2}}\times(\mathrm{kg\,m^{-3}})^{-5/3}$. If a
calculation of a degenerate radius is off by a factor of 10, the exponent on
$\rho$ or the $5/3$ power of the composition factor is the first thing to check.

## 10. Assumptions and regime of validity

1. **A circular orbit** in (2) and (3) and a **background-free light curve** in
   (1). A transit of a grazing or eccentric planet needs the full geometry, and
   stellar limb darkening changes the shape of the dip without changing its
   depth.
2. **Random orbit orientation** for the geometric probabilities in §2 and §3. A
   system that is dynamically aligned or measured in a biased sample does not
   obey them.
3. **Isotropic inclination distribution** for $\mathrm{E}[\sin i]$ in (6). A
   transit-detected subsample is *not* isotropic — its inclinations are near
   $90^\circ$ — so (6) applies to an RV-only sample and not to a transit sample.
4. **A single-planet system** in (5). Additional planets contribute their own
   reflex motion, and a multi-planet fit is a joint inversion.
5. **A known stellar mass and radius** throughout. Both are inferences from a
   spectrum, a parallax and a stellar model, and they propagate directly into
   every planet quantity.
6. **An albedo, for the temperature.** The equilibrium temperature is defined for
   an airless body; a real planet's albedo depends on its atmosphere, which is
   what one is trying to determine.
7. **Hydrostatic equilibrium and a single equation of state** in §6. A planet with
   a thick atmosphere, a hot interior, phase transitions or a strong thermal
   gradient does not follow the relation computed here, and the observed spread of
   radii at fixed mass is largely due to exactly those effects.
8. **The degenerate limit only for a cold, fully degenerate body** in (11). See
   §6: this is the regime check that the giant-planet comparison fails.

## 11. Python demonstration

[`code/exoplanets_demo.py`](./code/exoplanets_demo.py) derives all six relations,
propagates the errors and runs the two averages numerically. No exoplanet, star,
mass, radius or discovery is quoted anywhere in it.

The two observables, including why the amplitude is so small:

```text
     R_p/R_earth   delta (ppm)   delta (per cent)
            1.0         83.86           0.0084
           11.2      10519.79           1.0520
```

```text
     a (au)   p (per cent)   one in ...
      0.05        9.3009          10.8
      1.00        0.4650         215.0
```

```text
     a (au)   P (yr)   K for 1 M_earth (m/s)   mass for K = 1 m/s (M_earth)
      1.00    0.9999                   0.0894                        11.18
```

The inclination distribution, checked analytically and by Monte Carlo:

```text
      E[sin i] = integral_0^(pi/2) sin^2 i di = pi/4 = 0.7854
      E[1/sin i] = integral_0^(pi/2) sin i (1/sin i) di = pi/2 = 1.5708
  ...
    sample mean sin i     = 0.78575   (pi/4 = 0.78540)
    sample mean 1/sin i   = 1.57304   (pi/2 = 1.57080)
    fraction with sin i < 0.5 = 0.13359   (analytic 1 - sqrt(3)/2 = 0.13397)
```

The habitable zone as a model output, and the mass–radius slope:

```text
     boundary            naive a (au)   with +33 K (au)
  freezing                     0.870               1.125
```

```text
     M (M_earth)   R model (km)   mean rho   R constant-density (km)
          0.50          5673.9       3903                   5883.7
         10.00         13686.4       5561                  15970.8

  The measured exponent across the table is R ~ M^0.294.
```

### What to observe

- The RV table is worth reading in full: a **1 m s⁻¹** signal requires
  11.2 Earth masses at 1 au, 5.0 at 0.2 au and 2.5 at 0.05 au. The sensitivity to
  mass is what drove the field toward close-in planets, and the geometric
  probability in §2 pushed in the same direction.
- The Monte Carlo reproduces $\pi/4$ and $\pi/2$ to 0.05 per cent and the
  $1-\sqrt3/2$ fraction to 0.3 per cent. The disagreements are the Monte Carlo
  error, and their size is the check — a "verification" that agreed to six
  figures with two million samples would indicate a coding error, not accuracy.
- The naive freezing boundary moves from 0.870 to 1.125 au when 33 K of greenhouse
  warming is added. That is a 29 per cent change in the *boundary of the
  habitable zone* from one assumed atmosphere, which is the quantitative version
  of "the habitable zone is a model".
- The measured mass–radius exponent is 0.294, between the derived limits of
  0.333 (uncompressed) and 0.250 (strongly compressed). The model was not told
  which regime it was in; it moved between them as the mass rose.
- The self-compressed model gives about 7000 km for an Earth-mass planet against
  the Earth's 6371 km. The difference is not an error to be tuned away — it is the
  iron core, and it is the reason a measured radius is a *constraint* rather than
  a composition.

## 12. Common mistakes

1. **Reporting a minimum mass as a mass.** Quote it as $m\sin i$ and apply the
   $\pi/2$ correction only for population statements, with the assumption of
   isotropy stated.
2. **Taking the reciprocal of the mean $\sin i$.** It is the mean of the
   reciprocal that converts minimum masses, and the two differ by 23 per cent.
3. **Quoting a density without the stellar radius uncertainty.** It is usually the
   dominant term.
4. **Treating a habitable-zone membership as a habitability claim.** The zone is a
   model output; the claim needs a spectrum.
5. **Using an equilibrium temperature as a surface temperature.** The difference
   is the greenhouse, 33 K on the Earth, and unknown on a planet without a
   measured atmosphere.
6. **Applying the isotropic $\mathrm{E}[\sin i]$ to a transit sample.** That
   sample's inclinations are near $90^\circ$ by selection.
7. **Claiming a composition from a density alone.** The same density admits a
   range of core fractions and, with an atmosphere, a range of envelope masses.
8. **Forgetting that the stellar mass enters every planet quantity.** An error in
   $M_*$ is an error in the orbit size, the mass and the flux.
9. **Using a degenerate mass–radius relation for a giant planet.** See §6: it
   predicts a shrinking radius and the observations are flat.
10. **Reporting a single value for a habitability-related quantity.** These are
    inferences with model dependence, and a range with the model named is the
    honest report.

## 13. Real-world applications

- **Survey design.** The transit probability times the number of transits per
  unit time is the detection yield, and it is why transit surveys stare at fields
  for years, and why their targets are bright, quiet, small stars.
- **Atmospheric characterisation.** Transmission and emission spectroscopy are
  the measurement that turns a candidate into an atmosphere, and the required
  precision sets the telescope
  ([17-01 Remote Sensing Physics](../../17-remote-sensing-gis/01-remote-sensing-physics/README.md)).
- **Stellar characterisation.** Since the star dominates the error budget for a
  planet radius, precision stellar spectroscopy and asteroseismology are
  planet-characterisation instruments.
- **Population statistics.** Occurrence rates require the geometric and selection
  weighting of §2 to be inverted, and the inclination corrections of §3 to be
  applied correctly.
- **Comparative planetology.** The solar system supplies the ground truth that
  exoplanet inferences lack, which is why
  [04-08-01](./01-solar-system.md) and [04-08-02](./02-planetary-interiors.md)
  come first in this module.
- **The limits of inference.** Every methodological caution in this lesson
  applies to any remote-sensing problem with one measurement and many unknowns,
  including subsurface geophysics.

## 14. Further reading

- **Seager, S. *Exoplanet Atmospheres* (Princeton University Press).** The
  standard text for the observable-to-inference chain, and rigorous about which
  quantities are model outputs. Level: graduate.
- **Murray, C. D., & Correia, A. C. M. *Exoplanets* (Princeton University Press)
  and the review literature on radial velocities.** The RV technique in full,
  including the instrumental and stellar-noise limitations. Level: graduate.
- **Winn, J. N., on transit geometry and spin–orbit alignment.** The derivations
  behind (1) to (3) with the eccentric and grazing cases in full. Level: graduate.
- **Kopparapu, R. K., et al., on habitable-zone limits.** The empirical flux
  limits and the climate models behind them; read it for the uncertainty on the
  edges, which is the point of §5. Level: graduate.
- **Chandrasekhar, S. *An Introduction to the Study of Stellar Structure*
  (Dover).** The derivation of the degenerate equation of state and the
  polytropic mass–radius relations behind (10) and (11). Level: graduate.
- **NASA Exoplanet Archive and the mission pages at <https://www.nasa.gov>.** The
  authoritative catalogue for any quoted planet parameter, including the
  revisions that follow new data; a parameter's reference and epoch should be part
  of every citation. Level: reference.
- **ESA science pages at <https://www.esa.int>.** Mission context and current
  results. Level: reference.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 15. Related lessons

- [04-08-01 Solar System Architecture and Formation](./01-solar-system.md) — the
  same relations applied where the data are far better.
- [04-08-02 Planetary Interiors and Magnetic Fields](./02-planetary-interiors.md)
  — why a mass and a radius do not determine an interior.
- [04-08-03 Planetary Geophysics from Orbiters and Landers](./03-planetary-geophysics-missions.md)
  — the measurements that are impossible for an exoplanet.
- [16-04 The Climate System and Feedbacks](../../16-atmosphere-climate/04-climate-system-and-feedbacks/README.md)
  — the climate physics behind the habitable-zone limits.
- [16-02-01 Solar and Terrestrial Radiation, Blackbody Laws](../../16-atmosphere-climate/02-radiation-and-energy-balance/01-solar-and-terrestrial-radiation.md)
  — the radiative balance of §5 in full.
- [21 Statistics and Bayesian Inference](../../21-statistics-bayesian-ml/README.md)
  — the population statistics and selection effects that §3's averages enter.

Exercises:
[`exercises/04-exoplanets-habitability-exercises.md`](./exercises/04-exoplanets-habitability-exercises.md)
and
[`exercises/04-exoplanets-habitability-solutions.md`](./exercises/04-exoplanets-habitability-solutions.md).

## Self-assessment checklist

- [ ] I can compute a transit depth and state what it depends on. (§2)
- [ ] I can derive the transit probability and the duration. (§2)
- [ ] I can derive the RV semi-amplitude and compute it for an Earth-mass planet.
      (§3)
- [ ] I can state the two inclination averages and the Jensen-inequality error of
      confusing them. (§3)
- [ ] I can propagate a stellar radius error into a planet radius and a density.
      (§4)
- [ ] I can compute an equilibrium temperature and recover a greenhouse increment
      as a residual. (§5)
- [ ] I can demonstrate that a habitable-zone edge is atmosphere-dependent. (§5)
- [ ] I can derive the uncompressed, the self-compressed and the degenerate
      mass–radius limits. (§6)
- [ ] I can name the regime in which the degenerate relation fails and why. (§6)
- [ ] I can write the honest sentence that reports a habitability-related
      inference. (§7)
