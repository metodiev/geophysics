---
id: 04-08-02
title: "Planetary Interiors and Magnetic Fields"
level: advanced
prereqs: ["04-08-01", "04-01-01", "07-01-01"]
estimated_minutes: 75
tags: [planetary-interiors, hydrostatic-equilibrium, moment-of-inertia, dynamo, induction]
---

# Planetary Interiors and Magnetic Fields

Nobody has been inside a planet. Every statement about a planetary interior is an
inference from something measured from outside — a radius, a mass, a gravity
field, a magnetic field, a seismic travel time, or the way the body wobbles — and
the inference always requires a model that is more elaborate than the observation.
This lesson is about that chain, and it is deliberately built so that the
*arithmetic is checkable against itself* even though the interiors are not.

The lesson does three things. It integrates the equations of hydrostatic
equilibrium to show how a central pressure is obtained — and that it is a
property of a model rather than of a planet. It derives the moment-of-inertia
factor and inverts the geodetic value for a core density, in an inversion that
**fails informatively** and therefore teaches more than a successful one. And it
treats planetary magnetic fields: what a dynamo requires, how a dipole moment is
obtained from a measured surface field, and how a time-varying external field
probes the interior conductivity of a body through the skin depth — which is how
a subsurface ocean is detected from outside a moon.

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** the equations of hydrostatic equilibrium for a spherically symmetric
   body and state which of them contains the physics and which the geometry.
2. **Compute** a central pressure from a density profile, verify the numerical
   integration against the analytic uniform-sphere result, and explain why a
   central pressure is a model output rather than a measurement.
3. **Derive** the moment-of-inertia factor of a uniform sphere and of a layered
   body, and use it to distinguish a centrally condensed body from a homogeneous
   one.
4. **Invert** a geodetic moment-of-inertia factor for a core density at a fixed
   core radius, and explain what the failure of the inversion reveals about the
   model.
5. **Compute** the magnetic Reynolds number and the magnetic diffusion time for a
   conducting fluid, and state the three requirements a dynamo imposes on a body.
6. **Compute** a dipole moment from an equatorial surface field, and explain why
   the argument for a dynamo is the field's variability and the temperature of
   the core rather than the amplitude.
7. **Compute** a skin depth and use it to explain how a time-varying external
   field detects a conducting layer inside a body that cannot be visited.
8. **State**, for each inference in this lesson, which part is measured and which
   is assumed.

## Prerequisites

- [04-08-01 Solar System Architecture and Formation](./01-solar-system.md) —
  masses, radii and the density-implies-composition argument that this lesson
  turns into an interior structure.
- [04-01-01 Crust, Mantle, Core: Seismological and Geochemical Evidence](../01-earth-structure/01-layered-earth.md)
  — the Earth's interior as the calibration case, including how its layering is
  established.
- [07-01-01 Newtonian Gravitation, Field and Acceleration](../../07-gravity-geodesy/01-gravity-fundamentals/01-newtonian-gravity.md)
  — the field of a spherically symmetric mass distribution, which is what makes
  $g(r) = GM(r)/r^2$ usable inside a body.

## 1. Three equations, and where the uncertainty lives

For a spherically symmetric body in hydrostatic equilibrium, the interior is
determined by three relations:

$$\frac{\mathrm{d}M}{\mathrm{d}r} = 4\pi r^2\rho(r), \qquad
g(r) = \frac{GM(r)}{r^2}, \qquad
\frac{\mathrm{d}P}{\mathrm{d}r} = -\rho(r)g(r) , \tag{1}$$

with the boundary conditions $M(0) = 0$ and $P(R) = 0$. The first is geometry,
the second is Newton's theorem that only the mass inside $r$ contributes, and
the third is the balance of forces on a shell. Together they are exact for a
hydrostatic, spherically symmetric body.

**Everything uncertain is in $\rho(r)$.** The equations are the easy part; the
density profile is what no one measures directly. So a planetary interior model
is a statement about $\rho(r)$ that is required to (i) integrate to the measured
mass, (ii) produce the measured radius, (iii) satisfy an equation of state
measured in a laboratory or computed, and (iv) match whatever else is observed —
a seismic travel time, a moment of inertia, a gravitational harmonic. The
central pressure is the last thing out of that pipeline, and it inherits the
uncertainty of the profile.

**A worked example of the pipeline.** For a uniform density equal to the Earth's
mean, (1) integrates analytically:

$$P_\mathrm{centre} = \tfrac23\pi G\rho^2R^2
= \tfrac23\pi(6.6743\times10^{-11})(5513.4)^2(6.371\times10^6)^2
= 1.725\times10^{11}\ \mathrm{Pa} = 172.5\ \mathrm{GPa}. \tag{2}$$

A two-layer model with a core of 11000 kg m⁻³ inside 3480 km and a mantle of
4500 kg m⁻³ outside gives a mass of $6.02\times10^{24}$ kg — 0.8 per cent above
the tabulated Earth mass — and a central pressure of **330.4 GPa**. The
seismological value, from the preliminary reference Earth model and its
successors, is about **364 GPa**.

Three things follow. First, both models bracket the reference value without
being tuned to it, so the machinery works. Second, the reference value is not a
*measurement* either: it is the same integral performed on a density profile
inferred from seismic velocities, an equation of state and the mass. Third, the
demo shows that a two-parameter model can be tuned to give exactly 364 GPa while
its mass comes out 0.7 per cent low — **hitting one target while missing
another is what an under-determined model does**, and choosing the parameters to
hit the target you care about is not a validation.

## 2. The moment of inertia, and what it measures

The moment of inertia about the rotation axis is

$$C = \frac{8\pi}{3}\int_0^R\rho(r)\,r^4\,\mathrm{d}r , \tag{3}$$

the factor $\tfrac23$ coming from the perpendicular distance of a shell from the
axis. For a uniform sphere this gives $C = \tfrac25MR^2$, so

$$\alpha \equiv \frac{C}{MR^2} = 0.4 \tag{4}$$

**whatever the density**. Central condensation lowers $\alpha$, so $\alpha$ is a
measure of how concentrated the mass is toward the centre, and it is
dimensionless — which is what makes it comparable between bodies.

Equation (4) is also the reason $\alpha$ matters: it is the one interior quantity
that is determined by *dynamics* rather than by seismology. The Earth's $\alpha$
is inferred from its precession constant (measured by very long baseline
interferometry) together with its gravitational harmonic $J_2$, through the
Darwin–Radau relation, which assumes the body is in hydrostatic equilibrium. The
tabulated value is about **0.3308**, and both the value and the assumption are
inferences rather than measurements.

**An inversion that fails, informatively.** Two layers, a core of radius
$R_c = 3480$ km (a seismological input), a uniform mantle of 4500 kg m⁻³, and an
unknown core density. Bisecting for the core density that reproduces
$\alpha = 0.3308$ gives

$$\rho_c = 13\,538\ \mathrm{kg\,m^{-3}},
\qquad M = 6.47\times10^{24}\ \mathrm{kg}. \tag{5}$$

Seismology puts the outer core near 10 to 12 thousand kg m⁻³ and the inner core a
little above 13 thousand, so the required *average* core density is far too high,
and the mass it implies is 8 per cent too large. The two-layer model is
therefore **wrong, not merely imprecise**: no choice of the two densities and the
fixed core radius reproduces both the mass and $\alpha$, because a uniform mantle
cannot be centrally condensed enough. The real mantle's density increases with
depth.

The lesson from the failure is worth stating explicitly, because it generalises:
**an inversion that returns an impossible value has told you that the model is
inadequate, which is more useful than a plausible value it cannot defend.**
A two-layer fit that had returned $\rho_c = 10\,500$ kg m⁻³ would have looked
like a success and would have been a false one.

## 3. Magnetic fields: what a dynamo requires

A planetary magnetic field is either **remanent** (frozen into magnetised rock
when it cooled through its Curie temperature) or **generated** (sustained by
motions in a conducting fluid). The distinction is not academic: a remanent field
records the past, a generated one reports the present.

**What a dynamo requires.** Three conditions, and a body that fails any of them
has no intrinsic field:

1. A **conducting fluid region** — a liquid metal core, or a salty ocean, or a
   metallic hydrogen interior.
2. A **source of kinetic energy** in that region — convection, driven by thermal
   or compositional buoyancy, or by precession and tides.
3. **Sufficient electrical conductivity** and a large enough scale, quantified by
   the magnetic Reynolds number

$$R_m = \mu_0\sigma U L , \tag{6}$$

where $U$ is a flow speed and $L$ a length scale. A dynamo sustains a field only
if $R_m$ exceeds a critical value, which numerical experiments place somewhere
between about 10 and 100 depending on the flow geometry — an order of magnitude,
not a constant. For a core with $\sigma = 3\times10^5$ S m⁻¹,
$U = 5\times10^{-4}$ m s⁻¹ and $L = 2\times10^6$ m, $R_m = 377$, comfortably
above any plausible threshold.

**The diffusion time** is the other side of the same coin:

$$\tau_\eta = \mu_0\sigma L^2 . \tag{7}$$

For the same numbers $\tau_\eta = 1.51\times10^{12}$ s $\approx 48\,000$ years.
This is how long the field would persist if the flow stopped, and it is why the
field's *existence at one instant* does not require a dynamo while its
*persistence over billions of years* does. It also explains why geomagnetic
reversals take thousands of years rather than days: they are diffusive
reorganisations of a large conductor.

**A dipole moment from a surface field.** A centred dipole has

$$B_r = \frac{\mu_0}{4\pi}\frac{2m\cos\theta}{r^3}, \qquad
B_\theta = \frac{\mu_0}{4\pi}\frac{m\sin\theta}{r^3} , \tag{8}$$

so at the equator, $B_\mathrm{eq} = (\mu_0/4\pi)\,m/R^3$ and

$$m = \frac{4\pi}{\mu_0}B_\mathrm{eq}R^3 . \tag{9}$$

With $B_\mathrm{eq} = 3.1\times10^{-5}$ T and $R = 6.371\times10^6$ m this gives
$m = 8.02\times10^{22}$ A m², against a tabulated value from geomagnetic field
models of a little under $8\times10^{22}$ A m². The few per cent difference is the
non-dipole part of the field — which is itself informative, since it is the
signature of the flow that generates it.

**Why a dynamo and not a fossil.** The required magnetisation, if the moment were
remanent and spread uniformly through the core, is
$M = m/V_\mathrm{core} = 8.02\times10^{22}/1.77\times10^{20} = 454$ A m⁻¹, which
is small compared with the saturation magnetisation of iron (of order
$10^6$ A m⁻¹). **So the amplitude is easy and the amplitude is not the argument.**
The argument is twofold: the field changes on a human timescale, which a fossil
cannot do, and the core is far above the Curie temperature of iron (near 1043 K),
so ferromagnetic ordering cannot persist there at all.

## 4. Induction: probing an interior with a varying field

If a body sits in a time-varying external magnetic field — because it orbits
inside a planetary magnetosphere — the field diffuses into any conductor it
contains, and the induced currents produce their own field, which is measured
from outside. The relevant length scale is the **skin depth**:

$$\delta = \sqrt{\frac{2}{\mu_0\sigma\omega}} , \tag{10}$$

which follows from the diffusion equation for the field in a good conductor. If a
conducting layer is thin compared with $\delta$, the induction is weak and the
induced field is small; if the layer is thick compared with $\delta$, it responds
nearly as a perfect conductor and the induced dipole is large. The amplitude of
the induced field therefore measures the product of the conductivity and the
thickness — not the thickness alone.

For a conductivity of 1 S m⁻¹ (a salty ocean; the salinity of any particular ocean
is an assumption), (10) gives $\delta = 101$ km at an 11.2-hour period and 279 km
at a 3.55-day period. The short period is the discriminating one: at 3.55 days
even a very thick conductor is thin compared with $\delta$, so the response is
weak whatever is there. **Induction therefore measures a conductance (the product
$\sigma t$), and reporting it as an ocean thickness requires a model that fixes
the salinity and the conductivity of everything above and below.**

This is the same logic as the skin depth in terrestrial electromagnetic methods,
where it is the basis of the method; the planetary application is that the
external field is supplied by the parent planet rather than by a coil, and the
receiver is a magnetometer on a spacecraft rather than an induction coil on the
ground ([08-03 Planetary Geophysics from Orbiters and Landers](./03-planetary-geophysics-missions.md)
and, for the terrestrial version,
[09 Electrical and EM Methods](../../09-electrical-em-methods/README.md)).

## 5. Physical interpretation

- `Hydrostatic equilibrium' is a *constraint*, not a solution: it says what any
  interior must satisfy, and the physics is in choosing $\rho(r)$.
- A **central pressure is the integral of a model**. It is meaningful and useful,
  and it is not observed.
- The **moment-of-inertia factor** is the one interior quantity that comes from
  dynamics, and it discriminates between a homogeneous and a centrally
  condensed body with no seismic data at all.
- A **failed inversion is a result**. When the inversion in §2 demanded a core
  density that seismology excludes, the correct conclusion was about the model,
  and the arithmetic that produced it was right.
- A magnetic field's **amplitude is easy to explain and its variability is hard**,
  which is exactly why the variability is what shows the field is being
  generated.
- **Induction measures a conductance**, so a claim about an ocean's thickness is
  a model output with the salinity inside it.

## 6. Units and dimensional analysis

| Quantity | Expression | Units |
|---|---|---|
| Mass continuity | $4\pi r^2\rho$ | m² × kg m⁻³ = kg m⁻¹ |
| Gravity inside a body | $GM(r)/r^2$ | m³ s⁻² / m² = m s⁻² |
| Pressure gradient | $-\rho g$ | kg m⁻³ × m s⁻² = Pa m⁻¹ |
| Central pressure | $\tfrac23\pi G\rho^2R^2$ | m³ s⁻² kg⁻¹ × kg² m⁻⁶ × m² = Pa |
| Moment of inertia | $\tfrac83\pi\int\rho r^4\mathrm{d}r$ | kg m⁻³ × m⁵ = kg m² |
| Moment-of-inertia factor | $C/(MR^2)$ | kg m²/(kg m²) = dimensionless |
| Magnetic Reynolds number | $\mu_0\sigma UL$ | N A⁻² × S m⁻¹ × m s⁻¹ × m = dimensionless |
| Diffusion time | $\mu_0\sigma L^2$ | N A⁻² × S m⁻¹ × m² = s |
| Dipole moment | $(4\pi/\mu_0)B_\mathrm{eq}R^3$ | T m³/(N A⁻²) = A m² |
| Skin depth | $\sqrt{2/(\mu_0\sigma\omega)}$ | (N A⁻² S m⁻¹ s)$^{1/2}$ = m |

Two of these are worth checking by hand. The magnetic Reynolds number must be
dimensionless, and the check is that $\mu_0$ has the units N A⁻² and
$\sigma UL$ has A² N⁻¹ m s⁻¹, so the product cancels — which is the reason
conductivity is quoted in S m⁻¹ in this context and in ohmm in others. And
$\tfrac23\pi G\rho^2R^2$ comes out in pascals, with no numerical factor of $4\pi$
left over: the uniform-sphere central pressure is $\tfrac23\pi G\rho^2R^2$, a
formula containing $\pi$ and nothing else, which is a useful thing to have
memorised as an order-of-magnitude estimate.

## 7. Assumptions and regime of validity

1. **Spherical symmetry and hydrostatic equilibrium** in (1). A rapidly rotating
   body is oblate, and the flattening changes the surface boundary condition;
   a body with a rigid lithosphere can support deviatoric stress and need not be
   hydrostatic at all, which is why the flattening of a small body can reveal a
   fossil shape rather than a fluid one.
2. **A specified density profile** in §1 and §2. Every conclusion inherits the
   profile's uncertainty, and different profiles can satisfy the same mass and
   radius.
3. **Hydrostatic equilibrium for the Darwin–Radau relation** in §2. The Earth's
   $\alpha$ is only as hydrostatic as the Earth is, and departures from
   hydrostaticity are a real contributor to the uncertainty.
4. **A two-layer model** in §2. Real interiors are graded and differenced; the
   failure of the inversion is the demonstration.
5. **A dipolar field** in (8) and (9). The geodetic dipole is a fit to a field
   with higher harmonics, so it is a summary of the observations rather than a
   measured quantity, and its value depends on the epoch.
6. **Steady dynamo theory at a critical $R_m$** in §3. The critical value depends
   on the flow geometry and on the boundary conditions, and laboratory dynamo
   experiments and numerical models disagree about it by a factor of several.
7. **A uniform conductor** in (10). A layered conductor has a frequency-dependent
   response, and inverting it requires a transfer function measured at several
   periods, not one skin depth.
8. **A dipole source field** in §4. A non-dipolar external field couples to
   higher harmonics of the internal structure, and the induced field is then a
   richer function of the interior — which is an advantage if you have the
   models, and a trap if you do not.

## 8. Python demonstration

[`code/planetary_interiors_demo.py`](./code/planetary_interiors_demo.py)
integrates the hydrostatic equations for two models, computes and inverts the
moment-of-inertia factor, and evaluates the dynamo and induction relations.
Every density is labelled NOMINAL; the seismological pressure, the geodetic
$\alpha$ and the dipole moment are labelled TABULATED inferences.

The integration, checked against the analytic uniform-sphere result:

```text
  Model A: uniform density at the mean density of the Earth.
    rho_mean = M/(4/3 pi R^3) = 5513.4 kg/m^3
    P_centre = (2/3) pi G rho^2 R^2 = 172.5 GPa   (analytic)
    the same quantity from the numerical integration = 172.5 GPa
  Model B: two layers, NOMINAL densities and a core radius.
    mass from the profile   = 6.0219e+24 kg
    tabulated Earth mass    = 5.9722e+24 kg   (difference 0.83 per cent)
    central pressure        = 330.4 GPa
```

The moment of inertia, and the inversion that fails:

```text
  Model A (uniform):
    alpha = 0.400004   (the analytic limit is 0.4)
  Model B (two layers), core radius 3480 km:
        9000         4000    0.35251           5.2156
       11000         4500    0.34653           6.0220
       13000         5000    0.34196           6.8284

  Every plausible two-layer model above gives an alpha ABOVE the
  geodetic value ... Invert for the core density ...
    required rho_core = 13538 kg/m^3, giving alpha = 0.3308 and M = 6.470e24 kg
```

The dynamo, and the induction that detects an ocean:

```text
     sigma (S/m)   Rm        tau = mu_0 sigma L^2
       3.0e+05      376.99      47784.5 yr
       5.0e+05      628.32      79640.9 yr
```

```text
     sigma (S/m)   delta at 11.2 h (km)   delta at 3.55 d (km)
           0.1                  319.6                 881.4
           1.0                  101.1                 278.7
```

### What to observe

- The numerical integration reproduces the analytic value 172.5 GPa exactly,
  which validates the code; the *model* is then what is wrong, and the demo says
  so.
- The two-layer mass comes out 0.83 per cent high, so the model is not
  catastrophically wrong — and its central pressure of 330.4 GPa sits
  reassuringly near the reference 364 GPa. A model can be adequate for one
  purpose (an order-of-magnitude central pressure) and inadequate for another
  (the moment of inertia), and a single check does not transfer between them.
- The uniform-sphere $\alpha$ comes out 0.400004 rather than exactly 0.4, which
  is the discretisation error of a 100 000-point grid. Reporting the discrepancy
  is the point: it tells you the numerical resolution, and it is the only way to
  know that the grid is not doing something worse.
- The required core density of 13 538 kg m⁻³ is *higher* than the seismological
  range, and the mass it implies is 8 per cent too large. The inversion did not
  give an answer; it gave a diagnosis.

## 9. Common mistakes

1. **Treating a central pressure as a measurement.** It comes from integrating a
   model, and the model's profile is not observed.
2. **Validating a model on one quantity.** Matching the mass, or the central
   pressure, or $\alpha$, does not imply the others.
3. **Using the uniform-sphere $\alpha = 0.4$ for a real body.** Every
   differentiated body is below 0.4, and the departure is the information.
4. **Assuming a magnetic field implies a dynamo.** A crustal remanent field is
   common on small bodies that have no dynamo today; the test is the field's
   variability and the temperature of the source region.
5. **Assuming a dynamo implies a field we would recognise.** A dynamo produces
   whatever morphology the flow gives it, and a multipolar or time-varying field
   can be a dynamo's output without being a dipole.
6. **Quoting an ocean thickness from an induced field.** Induction measures a
   conductance; the thickness requires an assumed salinity and an assumed
   overlying conductivity.
7. **Using one period for an induction sounding.** The response is
   frequency-dependent, and a single period cannot separate a thin conductor
   from a thick one.
8. **Forgetting that $R_m$'s critical value is not a constant.** It depends on
   the flow, and quoting 40 or 100 without a source is quoting a model.
9. **Computing $\alpha$ with a grid too coarse for the integrand.** The $r^4$
   weighting means the outer few per cent of the body carries much of the moment
   of inertia, and a coarse grid biases it.
10. **Confusing the mean density with the interior density.** A mean density
    fixes one number; the interior requires a profile that also matches the mass,
    the radius and whatever else is measured.

## 10. Real-world applications

- **Spacecraft mission design.** A gravity field and a rotation state are the
  cheapest interior measurements, and they set what an orbiter is built to
  measure.
- **Magnetic field mapping.** The same planetological magnetometry that
  establishes a dynamo's presence is used to date crustal provinces from their
  remanent magnetisation.
- **Subsurface ocean detection.** Induction sounding is the primary evidence for
  liquid water inside icy moons, and it is an inverse problem with a stated
  degeneracy ([04-08-03 Planetary Geophysics from Orbiters and Landers](./03-planetary-geophysics-missions.md)).
- **Comparative planetology.** Why one body has a dynamo and another does not is
  a question about core size, composition and thermal evolution, all of which are
  inferred with the machinery of this lesson
  ([12-07 Comparative Planetary Interiors](../../12-global-geophysics-interior/07-planetary-interiors-comparative/README.md)).
- **Geomagnetism on Earth.** The same equations apply at home, where they can be
  tested against seismology and against a geological record of reversals
  ([12-04 Geomagnetic Field and Core Dynamics](../../12-global-geophysics-interior/04-geomagnetism-and-core/README.md)).
- **Planetary habitability.** An interior that supplies heat and volatiles, and a
  magnetic field that shields an atmosphere, both enter habitability arguments
  ([04-08-04 Exoplanets, Habitability and Observational Constraints](./04-exoplanets-habitability.md)).

## 11. Further reading

- **Chandrasekhar, S. *An Introduction to the Study of Stellar Structure*
  (Dover).** The classical treatment of hydrostatic equilibrium and polytropes,
  which is the machinery of §1 applied where the equation of state is better
  known. Level: graduate.
- **Dziewonski, A. M., & Anderson, D. L. (1981). "Preliminary reference Earth
  model." *Physics of the Earth and Planetary Interiors*.** The reference model
  whose central pressure is quoted here, and the standard example of an interior
  model built from many data types. Level: graduate.
- **Munk, W. H., & MacDonald, G. J. F. *The Rotation of the Earth* (Cambridge
  University Press).** Where the moment-of-inertia factor, the precession
  constant and the Darwin–Radau relation are derived together. Level: graduate.
- **Moffatt, H. K. *Magnetic Field Generation in Electrically Conducting Fluids*
  (Cambridge University Press).** The theory behind the dynamo requirements in
  §3, including why $R_m$ has a critical value. Level: doctoral.
- **Christensen, U. R., & Wicht, J., on dynamo scaling laws, and the
  (2003) *Philosophical Transactions* review literature.** The numerical
  experiments that supply the critical $R_m$ and the scaling of field strength
  with flow parameters. Level: doctoral.
- **NASA and ESA mission pages at <https://www.nasa.gov> and
  <https://www.esa.int>.** The current source for mission results, instrument
  descriptions and the corrections that follow a mission; planetary values are
  revised, so confirm them there rather than in a textbook. Level: reference.
- **International Association of Geomagnetism and Aeronomy, *International
  Geomagnetic Reference Field* and the NOAA magnetic field calculators at
  <https://www.ngdc.noaa.gov/IAGA/vmod/igrf.html> and
  <https://www.ngdc.noaa.gov/geomag/calculators/magcalc.shtml>.** The reference
  field whose dipole moment is quoted in §3, and a way to evaluate it. Level:
  reference.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 12. Related lessons

- [04-08-01 Solar System Architecture and Formation](./01-solar-system.md) — the
  masses, radii and compositions that these interiors have to explain.
- [04-08-03 Planetary Geophysics from Orbiters and Landers](./03-planetary-geophysics-missions.md)
  — the measurements that constrain these models.
- [04-08-04 Exoplanets, Habitability and Observational Constraints](./04-exoplanets-habitability.md)
  — what happens to interior inference when only a radius and a mass are known.
- [12-04 Geomagnetic Field and Core Dynamics](../../12-global-geophysics-interior/04-geomagnetism-and-core/README.md)
  — the terrestrial case, with far better data.
- [12-07 Comparative Planetary Interiors](../../12-global-geophysics-interior/07-planetary-interiors-comparative/README.md)
  — the comparison in full.
- [07-05 Satellite Gravimetry](../../07-gravity-geodesy/05-satellite-gravimetry/README.md)
  — how the gravity field that supplies $J_2$ is measured.
- [08-06 EM Fields in Conductors: Skin Depth and Diffusion](../../02-physics/07-electromagnetism/06-em-in-conductors.md)
  — the derivation of the skin depth used in §4.

Exercises:
[`exercises/02-planetary-interiors-exercises.md`](./exercises/02-planetary-interiors-exercises.md)
and
[`exercises/02-planetary-interiors-solutions.md`](./exercises/02-planetary-interiors-solutions.md).

## Self-assessment checklist

- [ ] I can write the three equations of hydrostatic equilibrium and say which
      contains the physics. (§1)
- [ ] I can compute a uniform-sphere central pressure analytically and verify a
      numerical integration against it. (§1)
- [ ] I can explain why a central pressure is a model output. (§1)
- [ ] I can derive $\alpha = 0.4$ for a uniform sphere and compute it for a
      layered body. (§2)
- [ ] I can invert a geodetic $\alpha$ for a core density and interpret a
      failure. (§2)
- [ ] I can compute $R_m$ and a diffusion time and state the three dynamo
      requirements. (§3)
- [ ] I can compute a dipole moment from a surface field and state why the
      dynamo argument is not about amplitude. (§3)
- [ ] I can compute a skin depth and explain induction sounding in terms of
      conductance. (§4)
- [ ] I can state three things a two-layer interior model cannot represent.
      (§7)
- [ ] I can name the quantity in this lesson that comes from dynamics rather than
      seismology. (§2)
