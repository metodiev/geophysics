# Module 04-08 — Planetary Science and Comparative Planetology

**Stages:** beginner → graduate · **Prerequisites:**
[01-03-01 Angles, Triangles and the Unit Circle](../../01-mathematics/03-trigonometry/01-angles-and-triangles.md)
and
[02-01-01 Physical Quantities, SI Units and Dimensional Homogeneity](../../02-physics/01-measurement-and-physical-reasoning/01-physical-quantities.md)
for the geometry and the units discipline that make these calculations checkable,
and
[04-01-01 Crust, Mantle, Core: Seismological and Geochemical Evidence](../01-earth-structure/01-layered-earth.md)
for the Earth as the calibration case — the one body whose interior is genuinely
known, and the reference against which every other body is described.

This module is the one place in the curriculum where "the Earth" is a special
case rather than the subject. It exists for three reasons, and they are not the
ones a popular account would give.

First, **the solar system is the only laboratory in which planetary-scale physics
can be tested.** The Earth is one realisation of a set of processes —
differentiation, convection, dynamo action, atmospheric escape, volatile
delivery — and a sample of one cannot separate the essential from the accidental.
Mars has no dynamo and the Earth has one; Venus has a runaway greenhouse and the
Earth does not; a body with a radius of a few hundred kilometres cannot retain an
atmosphere at all. Each of those is a controlled comparison, and each constrains a
mechanism that a terrestrial-only view has to take for granted.

Second, **planetary science is where the inference chain is visible.** Nowhere
else in geophysics is the gap between a measurement and a conclusion so wide, and
nowhere else is it so well documented. A planet's radius comes from a dip in a
light curve; its mass from a Doppler shift; its interior from a moment of inertia
inferred from a precession constant through a relation that assumes hydrostatic
equilibrium; its habitability from a climate model. This module makes that chain
the explicit subject, which is why the *epistemic* content of the lessons is
quantitative rather than decorative: an error propagation, an inclination
average, a regime check and a Bayesian posterior are all computed.

Third, **every quantity here is provisional.** Planetary values are
mission-derived and are revised — a radius from an occultation, a gravitational
parameter from a tracking campaign, a dipole moment from a magnetic field model.
A planetary scientist is therefore obliged to quote a value with its source and
its epoch, and the demos in this module label every input as NOMINAL or
TABULATED for exactly that reason. This is a habit that transfers directly to any
other data set that is still being collected.

## Learning objectives

By the end of this module you will be able to:

1. **Derive** Kepler's third law from the force balance and use it as a
   measurement of a gravitational parameter, including the interpretation of a
   residual against a tabulated value.
2. **Compute** an equilibrium temperature from a flux balance, recover a
   greenhouse increment as a residual, and compute the distance at which a
   volatile is stable.
3. **Compute** an orbital angular momentum, state the angular-momentum problem of
   solar-system formation, and distinguish the robust part of the result from the
   part that depends on an unknown.
4. **Compute** a Jeans escape parameter and use it to predict which gases a body
   retains — and name a case in which the criterion fails and why.
5. **Integrate** the equations of hydrostatic equilibrium, verify the integration
   against an analytic case, and explain why a central pressure is a property of a
   model rather than of a planet.
6. **Derive** a moment-of-inertia factor, invert a geodetic value for a core
   density, and interpret the failure of that inversion as a statement about the
   model.
7. **Compute** a magnetic Reynolds number, a diffusion time, a dipole moment from
   a surface field and a skin depth, and state the three requirements a dynamo
   imposes and what an induction measurement actually determines.
8. **Compute** the sensitivity of a lander seismometer, a radio-tracking system, a
   radar sounder and an orbiting magnetometer, and identify what limits each one —
   which is, in no case, the instrument.
9. **Derive** the transit and radial-velocity relations for an exoplanet, propagate
   the uncertainties through them, and state the inclination averages and the
   Jensen-inequality error of confusing them.
10. **Derive** the mass–radius relations of an uncompressed, a self-compressed and
    a fully degenerate body, and state the regime in which the degenerate relation
    gives a wrong answer.
11. **Write** the honest sentence that reports a planetary or exoplanetary
    inference with its model attached, and recognise when a result is conditional
    on an assumption that has been dressed up as a number.

## Lessons

| # | Lesson | Level | Key idea |
|---|---|---|---|
| 01 | [Solar System Architecture and Formation](./01-solar-system.md) | beginner | Kepler's law as a measurement, the ice line from a flux balance, the angular-momentum problem, and the escape parameter that decides which gases a body keeps |
| 02 | [Planetary Interiors and Magnetic Fields](./02-planetary-interiors.md) | advanced | **The inference lesson**: hydrostatic equilibrium integrates a model, a failed inversion diagnoses it, and a field's variability — not its amplitude — is what shows it is generated |
| 03 | [Planetary Geophysics from Orbiters and Landers](./03-planetary-geophysics-missions.md) | advanced | Four techniques, four different limiting factors, none of them the instrument: one station, one pass, one chance |
| 04 | [Exoplanets, Habitability and Observational Constraints](./04-exoplanets-habitability.md) | graduate | **The epistemic lesson**: two observables, many inferences, one worked example of correct physics giving a wrong answer outside its regime |

Lesson 02 is the module's **mastery lesson** for a geophysicist: if you can state
what a central pressure, a moment of inertia and a magnetic Reynolds number do
and do not determine, you have the habit that the rest of planetary geophysics
requires. Lesson 04 is the mastery lesson for anyone who has to communicate a
result that rests on a model.

## Suggested path

**If you are working through the folder in order:** lessons 01 to 04 in numeric
order. Lesson 01 is written at beginner level and needs only algebra and the
geometry of a circle; lesson 04 is written at graduate level and expects the error
propagation to be routine.

**If you are here from seismology:** read
[03](./03-planetary-geophysics-missions.md) §2 first, then
[02](./02-planetary-interiors.md) §1 and §3, then
[06-13 Planetary and Applied Seismology Frontiers](../../06-seismology/13-planetary-and-exploration-seismology/README.md)
and
[06-08-02 H-K Stacking and Crustal Thickness Estimation](../../06-seismology/08-receiver-functions-and-crustal-structure/02-h-k-stacking.md)
for the multi-station versions of the single-station problems.

**If you are here from gravity and geodesy:** read
[02](./02-planetary-interiors.md) §2 (the moment of inertia) and
[03](./03-planetary-geophysics-missions.md) §3 (Doppler tracking), then
[07-05 Satellite Gravimetry](../../07-gravity-geodesy/05-satellite-gravimetry/README.md)
and
[12-06 Geodetic Constraints on the Interior](../../12-global-geophysics-interior/06-geodesy-constraints-interior/README.md).

**If you are here for geomagnetism:** read
[02](./02-planetary-interiors.md) §3 and §4 in full, then
[12-04 Geomagnetic Field and Core Dynamics](../../12-global-geophysics-interior/04-geomagnetism-and-core/README.md)
for the terrestrial case and
[12-07 Comparative Planetary Interiors](../../12-global-geophysics-interior/07-planetary-interiors-comparative/README.md)
for the comparison.

**If you are here for habitability or astrobiology:** read
[01](./01-solar-system.md) §4 and §6, then
[04](./04-exoplanets-habitability.md) in full, then
[16-04 The Climate System and Feedbacks](../../16-atmosphere-climate/04-climate-system-and-feedbacks/README.md)
for the climate physics the habitable zone rests on.

**If you already have the physics:** attempt ★★★8 of
[01](./01-solar-system.md), ★★★8 and ★★★9 of
[02](./02-planetary-interiors.md), ★★★8 of
[03](./03-planetary-geophysics-missions.md) and ★★★8 and ★★★9 of
[04](./04-exoplanets-habitability.md). They are the problems that require a
judgement about what the model cannot support, and they mirror the way results are
actually reported.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-solar-system.md`](./01-solar-system.md) … [`04-exoplanets-habitability.md`](./04-exoplanets-habitability.md) | The four lessons |
| [`exercises/01-solar-system-exercises.md`](./exercises/01-solar-system-exercises.md) and [`-solutions.md`](./exercises/01-solar-system-solutions.md) | Kepler as a measurement, temperatures, the ice line, escape, mixture densities |
| [`exercises/02-planetary-interiors-exercises.md`](./exercises/02-planetary-interiors-exercises.md) and [`-solutions.md`](./exercises/02-planetary-interiors-solutions.md) | **The mastery lesson's problem set**, including the moment-of-inertia degeneracy |
| [`exercises/03-planetary-geophysics-missions-exercises.md`](./exercises/03-planetary-geophysics-missions-exercises.md) and [`-solutions.md`](./exercises/03-planetary-geophysics-missions-solutions.md) | Single-station seismology, Doppler sensitivity, radar budgets, magnetic depth from two altitudes |
| [`exercises/04-exoplanets-habitability-exercises.md`](./exercises/04-exoplanets-habitability-exercises.md) and [`-solutions.md`](./exercises/04-exoplanets-habitability-solutions.md) | Transits, radial velocities, inclination statistics, error propagation, mass–radius limits |
| [`code/solar_system_demo.py`](./code/solar_system_demo.py) | Kepler as a measurement with the residual explained, the greenhouse increment, the angular-momentum budget, the Jeans parameter |
| [`code/planetary_interiors_demo.py`](./code/planetary_interiors_demo.py) | Hydrostatic integration checked against the analytic uniform case, the moment-of-inertia inversion, dynamo and skin-depth relations |
| [`code/planetary_geophysics_missions_demo.py`](./code/planetary_geophysics_missions_demo.py) | Sensitivity of lander seismology, radio tracking, radar sounding and magnetometry, from assumed instrument performance |
| [`code/exoplanets_demo.py`](./code/exoplanets_demo.py) | Two observables, the inclination averages by analysis and Monte Carlo, the habitable zone as a model, the mass–radius exponent from an integration |

Every script prints its own numbers, labels every NOMINAL and TABULATED input, and
names the one relation in the module that fails its regime check. Run them with
the repository's environment, which supplies NumPy:

```bash
cd 04-earth-science-geology/08-planetary-science/code
../../../.venv/bin/python planetary_interiors_demo.py
```

## Mastery checkpoint

Complete this without notes, with a calculator and no code.

> **(a)** A body orbits the Sun at 4 au. Compute its period and its orbital speed,
> and state which input to the calculation is measured and which is defined.
> **(b)** Compute the equilibrium temperature at 4 au for an albedo of 0.3, and
> the distance at which a body with that albedo reaches 170 K. **(c)** A body has
> $GM = 4.28\times10^{13}$ m³ s⁻² and a radius of $3.39\times10^6$ m. Compute its
> escape speed, the thermal speed of CO₂ at 250 K, and the Jeans parameter, and
> state whether CO₂ is retained. **(d)** A body has a mean density of
> $5500$ kg m⁻³ and a uniform-density model would give $\alpha = 0.4$. State
> whether the real $\alpha$ is larger or smaller and why. **(e)** A conducting
> layer has $\sigma = 1$ S m⁻¹ and is 50 km thick inside a body in a field varying
> with a 12-hour period. Compute the skin depth and state whether the layer's
> induction response is strong or weak. **(f)** An Earth-sized planet transits a
> Sun-sized star. Compute the depth in ppm and the geometric probability at 1 au.
> **(g)** An RV survey reports a minimum mass of $2\ M_\oplus$. State the mean
> true mass of such a population and the assumption behind the correction.

**Worked answer for (c) and (g).**

(c) $v_\mathrm{esc} = \sqrt{2(4.28\times10^{13})/3.39\times10^6}
= \sqrt{2.525\times10^7} = 5025$ m s⁻¹. For CO₂ (44.009 u) at 250 K,

$$v_\mathrm{th} = \sqrt{\frac{3(1.380\,649\times10^{-23})(250)}
{44.009\times1.6605\times10^{-27}}} = \sqrt{1.418\times10^5} = 376.5\ \mathrm{m\,s^{-1}},$$

so $\lambda = (5025/376.5)^2 = 178$, well above 25: **CO₂ is retained**. These are
the parameters of Mars, and the conclusion is consistent with Mars having a
CO₂ atmosphere — though the criterion says nothing about how much of it remains,
which is why the escape parameter is a threshold and not a theory.

(g) The mean true mass is $\mathrm{E}[1/\sin i] = \pi/2$ times the mean minimum
mass, i.e. $2\times1.5708 = 3.14\ M_\oplus$, under the assumption that the orbits
are oriented **isotropically**. Using $1/\mathrm{E}[\sin i] = 4/\pi$ would give
2.55 instead — a 19 per cent error, and an example of Jensen's inequality.

Parts (a), (b) and (c) are lesson [01](./01-solar-system.md) §3, §4 and §6;
part (d) is lesson [02](./02-planetary-interiors.md) §2; part (e) is lesson
[02](./02-planetary-interiors.md) §4; parts (f) and (g) are lesson
[04](./04-exoplanets-habitability.md) §2 and §3.

## Common pitfalls across this module

1. **Treating a model output as a measurement.** A central pressure, an interior
   structure and a habitable-zone edge are all model results, and the sentence
   that reports them must say so.
2. **Quoting a planetary value without its source and epoch.** These are revised;
   a radius or a field strength from an old paper is a systematic error.
3. **Confusing a compressed density with an uncompressed one.** A measured mean
   density is compressed, and the composition inference needs the uncompressed
   value, which requires an interior model.
4. **Using a scaling outside its regime.** The degenerate $R \propto M^{-1/3}$
   relation is the module's worked example, and the lesson is that a correct
   formula can give a wrong answer.
5. **Taking the reciprocal of an average.** $\mathrm{E}[1/\sin i] \neq
   1/\mathrm{E}[\sin i]$, and the difference is 23 per cent.
6. **Ignoring the star.** In exoplanet work the host star is usually the dominant
   error term in a planet's radius and density.
7. **Assuming that a detected field implies a dynamo, or that no detected field
   implies no dynamo.** Crustal remanence and detection thresholds both
   intervene.
8. **Quoting a radar or seismological range without the material property that
   sets it.** A loss tangent and a velocity model are inputs, and they are
   measured or they are guesses.
9. **Expecting a single measurement to determine a structure.** A radius, a
   moment of inertia or a conversion delay each constrain a *family* of models,
   and it is the variety of independent constraints that determines an interior.
10. **Writing a conclusion that cannot be reviewed.** If the sentence does not
    name the model, the assumption or the data set, it cannot be checked, and a
    result that cannot be checked is not a result.

## Related lessons in other folders

- [06-13 Planetary and Applied Seismology Frontiers](../../06-seismology/13-planetary-and-exploration-seismology/README.md)
  — the seismological methods of lesson 03 in full.
- [12-07 Comparative Planetary Interiors](../../12-global-geophysics-interior/07-planetary-interiors-comparative/README.md)
  — the interior comparison that lesson 02 sets up.
- [07-05 Satellite Gravimetry](../../07-gravity-geodesy/05-satellite-gravimetry/README.md)
  — how a gravity field is measured from orbit, on the Earth and elsewhere.
- [17-03 Radar Remote Sensing](../../17-remote-sensing-gis/03-radar-remote-sensing/README.md)
  — the radar systems of lesson 03 applied from a remote-sensing perspective.
- [16-04 The Climate System and Feedbacks](../../16-atmosphere-climate/04-climate-system-and-feedbacks/README.md)
  — the climate physics behind the habitable zone.
- [26 Reference Library](../../26-reference-library/README.md) — where the
  constants and tabulated values used across this module are collected with their
  sources.
