---
id: 04-08-01
title: "Solar System Architecture and Formation"
level: beginner
prereqs: ["01-03-01", "02-01-01"]
estimated_minutes: 75
tags: [solar-system, planetary-formation, kepler, ice-line, escape-velocity]
---

# Solar System Architecture and Formation

Look at the solar system and three numbers stand out. The four inner planets are
small, dense and nearly airless. The four outer planets are large, light and
enormously gaseous. And between them, at a distance of two to four times the
Earth's from the Sun, there is almost nothing at all — a ring of rock and a belt
of ice where a planet should be.

This lesson is about the physics behind those three facts. The architecture of
the solar system is not an accident of history: it is what a disk of gas and dust
around a young star does when it cools, when the volatile compounds cross from
gas to solid, and when the leftover small bodies are gradually removed. Only one
of the four relations derived here needs any planetary data at all. The rest
follow from the Sun's mass, the Sun's luminosity and the laws of mechanics — which
means you can check every one of them with a calculator and a table of
constants.

## Learning objectives

By the end of this lesson you will be able to:

1. **Describe** the architecture of the solar system in terms of mass, size,
   density and composition as functions of heliocentric distance.
2. **Derive** Kepler's third law from Newton's law of gravitation and use it to
   measure the Sun's gravitational parameter from the Earth's orbit.
3. **Compute** the equilibrium temperature of a body at any heliocentric distance
   from a flux balance, and identify the factor of 4 that comes from the geometry
   of a sphere.
4. **Compute** the distance at which water ice is stable and explain why that
   distance, rather than any property of the planets, separates the terrestrial
   from the giant planets.
5. **Compute** the orbital angular momentum of a planet, compare it with the
   Sun's rotational angular momentum, and state the angular-momentum problem of
   solar-system formation in one sentence.
6. **Compute** the Jeans escape parameter for a gas on a given body and use it to
   explain which bodies retain which gases — and to identify the case where it
   fails.
7. **Compute** the density of a two-component mixture and invert it for a
   composition, stating why the inversion requires an *uncompressed* density.

## Prerequisites

- [01-03-01 Angles, Triangles and the Unit Circle](../../01-mathematics/03-trigonometry/01-angles-and-triangles.md)
  — the geometry of orbits and the small-angle approximations used throughout.
- [02-01-01 Physical Quantities, SI Units and Dimensional Homogeneity](../../02-physics/01-measurement-and-physical-reasoning/01-physical-quantities.md)
  — the units discipline that makes an astronomical calculation checkable, and
  the distinction between a defined and a measured constant that the whole lesson
  rests on.

## 1. The architecture, in four numbers

Four quantities summarise the system:

| Quantity | Inner region | Outer region |
|---|---|---|
| Mass | $< 0.5$ per cent of the system | $> 99$ per cent, mostly Jupiter and Saturn |
| Mean density | 3900 to 5500 kg m⁻³ | 700 to 1600 kg m⁻³ |
| Dominant volatiles | rock, metal, CO₂ | H₂, He, ices |
| Number of bodies | 4 planets | 4 planets, many moons, two belts |

**Density is the first diagnostic.** A mean density of 5500 kg m⁻³ for the Earth
is impossible for a body of hydrogen and helium at any modest pressure, so the
inner planets are made of rock and metal. A mean density of 1330 kg m⁻³ for
Jupiter is impossible for rock, so it is mostly hydrogen. The mean density of a
body therefore constrains its bulk composition before any spectroscopy is done —
and a mean density is a *measured* quantity whenever a mass and a radius are
known, which for solar-system bodies they usually are.

**The belt structure is the second diagnostic.** The asteroid belt occupies
2.1 to 3.3 au and contains a total mass far below that of any planet; the
Kuiper belt extends beyond 30 au. Both are leftovers. Their existence is itself a
datum: it says that the accretion process was efficient where planets are and
inefficient where belts are.

## 2. Formation in outline

The **nebular hypothesis** holds that the Sun and the planets formed from a
single collapsing cloud of gas and dust, and it survives because it predicts the
three observations in the introduction rather than explaining them one at a time.

The sequence, in the order that matters for the physics:

1. **Collapse and flattening.** A rotating cloud that collapses conserves angular
   momentum, so it spins up and flattens into a disk. The disk is the reason the
   planets orbit in nearly the same plane and in the same direction, which is an
   observation no other formation mechanism explains naturally.
2. **Condensation.** As the disk cools, different compounds cross from vapour to
   solid at different temperatures. Metals and silicates condense above about
   1300 K; water ice below about 150 to 170 K; methane and ammonia below about
   50 to 100 K depending on the pressure.
3. **Accretion.** Dust grains collide and stick, growing into planetesimals and
   then into planetary embryos. Beyond a certain mass, an embryo can capture gas
   from the disk directly.
4. **Clearing.** The remaining gas is dispersed by the young star's radiation and
   wind, and the remaining planetesimals are ejected or absorbed.

The **frost line** (or snow line) is the distance at which the temperature falls
below the condensation temperature of water. Its importance is not that ice is
present beyond it, but that ice is *abundant*: water is one of the most common
compounds in a cosmic-composition gas, so a disk with ice available has far more
condensable mass, builds larger cores faster, and those cores can then capture
hydrogen and helium before the gas disappears. **The giant planets exist where
they do because the frost line let them grow large enough, quickly enough, to
hold onto gas** — which is a statement about a temperature and a timescale, and
both of them are computable.

## 3. Kepler's third law, derived from Newton

Three assumptions: the orbit is circular, the planet's mass is negligible
compared with the Sun's, and gravity supplies the centripetal force. Then

$$\frac{mv^2}{a} = \frac{GMm}{a^2}
\quad\Longrightarrow\quad
v^2 = \frac{GM}{a} . \tag{1}$$

The orbital period is $T = 2\pi a/v$, so

$$T^2 = \frac{(2\pi a)^2}{v^2} = \frac{4\pi^2a^2}{GMa}
\quad\Longrightarrow\quad
\frac{T^2}{a^3} = \frac{4\pi^2}{GM} , \tag{2}$$

which is Kepler's third law, with the proportionality constant obtained from
gravity rather than fitted. It is the most useful relation in the lesson because
it can be run backwards: **measure $a$ and $T$ for one body and you have measured
$GM$ for the central object.**

The astronomical unit is *defined* (its value in metres is exact by convention)
and the sidereal year is measured, so (2) gives a measurement of the Sun's
gravitational parameter from two numbers:

$$GM = \frac{4\pi^2(1.495\,978\,707\times10^{11})^3}
{(3.155\,815\times10^7)^2}
= 1.327\,13\times10^{20}\ \mathrm{m^3\,s^{-2}} . \tag{3}$$

The commonly quoted value is $1.327\,124\times10^{20}$ m³ s⁻², and the derived
value is **2.9 parts per million high**. That residual is not an error: the
Earth does not orbit the Sun, it orbits the Earth–Moon barycentre, and the
barycentre's orbit responds to the Sun *plus* the Earth–Moon system. The mass of
the Earth and Moon in solar masses is $3.04\times10^{-6}$, which is exactly the
residual — so the calculation has measured the Earth as well as the Sun, and
recognising this is a good example of a discrepancy with a physical explanation
that can be checked rather than argued about.

Two other results follow immediately from (1): the orbital speed of the Earth,
$v = 2\pi a/T = 29.79$ km s⁻¹, and the fact that $v \propto 1/\sqrt a$, so a body
at 4 au orbits at half the Earth's speed and takes eight times as long.

## 4. Equilibrium temperature and the ice line

A body at heliocentric distance $a$ intercepts sunlight over its cross section
$\pi R^2$ and re-radiates from its whole surface $4\pi R^2$. With albedo $A$ and
solar luminosity $L$,

$$(1-A)\,\frac{L}{4\pi a^2}\,\pi R^2 = 4\pi R^2\sigma T_\mathrm{eq}^4
\quad\Longrightarrow\quad
T_\mathrm{eq} = \left[\frac{(1-A)L}{16\pi\sigma a^2}\right]^{1/4} . \tag{4}$$

**The factor of 4 is the geometry** — a cross section intercepts and a surface
emits. There is no planetary property in (4) except the albedo, so it applies to
a rock, a comet or a spacecraft.

Evaluating (4) with $L = 3.828\times10^{26}$ W and $A = 0.3$ gives 254.6 K at
1 au, and the scaling $T_\mathrm{eq}\propto a^{-1/2}$ does the rest: 300 K at
0.72 au (close to Venus's distance), 206 K at 1.52 au (Mars's distance) and
111 K at 5.2 au (Jupiter's). The Earth's measured mean surface temperature is
about 288 K, and the difference from 254.6 K — **33.4 K** — is the greenhouse
effect of the atmosphere, recovered here as a residual rather than asserted.

The **ice line** is the distance at which $T_\mathrm{eq} = 273$ K, which (4)
places at **0.87 au**, and the distance at which $T_\mathrm{eq} = 200$ K, at
**1.62 au**. Water ice is stable against sublimation over geological times
somewhere in that range, and the giant planets are all well beyond it. The
boundary is not sharp — it depends on the albedo, on the disk's opacity and on
its radial temperature profile, which is steeper than the $a^{-1/2}$ of a
single irradiated body because the disk is also being heated from within — so
quote the ice line as a range and say what it depends on.

## 5. The angular-momentum budget

For a Kepler orbit the specific angular momentum is
$h = \sqrt{GMa(1-e^2)}$, so a planet's orbital angular momentum is

$$L = m\sqrt{GMa(1-e^2)} . \tag{5}$$

Summing (5) over the planets with tabulated masses and orbital elements gives
$3.13\times10^{43}$ kg m² s⁻¹, of which Jupiter holds 61.5 per cent, Saturn
25.0 per cent and Neptune 8.0 per cent; the four terrestrial planets together
hold 0.15 per cent.

The Sun's rotational angular momentum requires a moment of inertia, and the Sun
rotates differentially, so the value depends on the interior rotation profile.
Two coefficients bracket it: the uniform-sphere value $\tfrac25MR^2$ gives
$1.10\times10^{42}$ kg m² s⁻¹ (3.4 per cent of the system total), and a realistic
solar value of about $0.06\,MR^2$ gives $1.66\times10^{41}$ (0.5 per cent).

So the ordering is unambiguous even though the digits are not: **the Sun holds
99.87 per cent of the mass and between 0.5 and 3.4 per cent of the angular
momentum; the planets hold the rest of the angular momentum and 0.13 per cent of
the mass.** This is the **angular-momentum problem**: a rotating cloud that
collapses preserves angular momentum, so a naive account predicts a rapidly
rotating Sun, and the observed Sun is slow. Something transported angular
momentum outward — magnetic braking against the solar wind, or torques within
the disk — and identifying which is a live research question rather than a
settled one. The lesson to take from it is that the budget is a *constraint on
any formation model*, and it is computed from orbital elements, not assumed.

## 6. Escape and atmospheric retention

Whether a body keeps a gas depends on the competition between the thermal speed
of the molecules and the escape speed from the body.

$$v_\mathrm{esc} = \sqrt{\frac{2GM}{R}}, \qquad
v_\mathrm{th} = \sqrt{\frac{3kT}{m}}, \qquad
\lambda = \frac{v_\mathrm{esc}^2}{v_\mathrm{th}^2}
= \frac{2GMm}{3kTR} . \tag{6}$$

The **Jeans escape parameter** $\lambda$ is the ratio of the energy needed to
escape to the typical thermal energy, and escape is slow when $\lambda$ is large.
The conventional criterion is that a gas is retained over the age of the solar
system if $\lambda$ exceeds roughly 25, though the threshold is soft and depends
on the exosphere's structure.

Two numbers make the relation concrete. The Earth's escape speed is
$\sqrt{2(3.986\times10^{14})/6.371\times10^6} = 11.19$ km s⁻¹, and Mars's is
5.03 km s⁻¹ — a factor of 2.2, which enters $\lambda$ as a factor of 4.8. At an
assumed exospheric temperature of 1000 K the Earth gives $\lambda = 10.1$ for
H₂, 20.1 for He, 140 for N₂ and 221 for CO₂; at 250 K Mars gives 8.2, 16.2, 113
and 178. So the Earth retains nitrogen and carbon dioxide and loses hydrogen and
helium, which is what is observed; and Mars is predicted to retain N₂ and CO₂ as
well, which is *not* what its thin atmosphere suggests.

That failure is the most instructive part of the section. **Where the criterion
fails, it fails because escape is not a thermal problem.** Water on Mars is
photodissociated in the upper atmosphere and the hydrogen produced escapes; a
λ of 73 for H₂O at 250 K says "retained", and the answer is wrong because the
molecule is destroyed before it can escape as a molecule. Nitrogen loss involves
photochemical escape and ion pickup, which are non-thermal. So $\lambda$ is a
threshold, not a theory: use it to order the gases on a body, and do not use it
to conclude that a body with a high $\lambda$ has kept everything.

## 7. Densities and composition

The mean density of a body is a mass balance. For a two-component body with
components of density $\rho_1$ and $\rho_2$ and a mass fraction $f$ of component
2, the specific volumes add:

$$\frac{1}{\rho} = \frac{f}{\rho_2} + \frac{1-f}{\rho_1}
\quad\Longrightarrow\quad
f = \frac{1/\rho - 1/\rho_1}{1/\rho_2 - 1/\rho_1} . \tag{7}$$

This is an identity, not a model. For a rock (3500 kg m⁻³) and ice
(1000 kg m⁻³) mixture, $f = 0.3$ gives 2000 kg m⁻³ and $f = 0.5$ gives
1556 kg m⁻³; conversely a measured 2500 kg m⁻³ implies an ice mass fraction of
0.32.

The catch is in the word **measured**. The density a spacecraft determines from a
mass and a radius is a *compressed* density — the body's own weight raises its
interior density — and the zero-pressure or "uncompressed" density that (7)
wants is a model output. So a compositional inference from a density is
conditional on an interior model, and the same measured density corresponds to a
range of compositions. That theme — a measured number that becomes an inference
as soon as it is interpreted — runs through every lesson in this module, and
[04-08-02 Planetary Interiors and Magnetic Fields](./02-planetary-interiors.md)
takes it up directly.

## 8. Physical interpretation

- **The solar system is a temperature-ordered sequence.** Density, composition
  and volatile content all vary monotonically with distance, and the ordering
  variable is temperature, which is computable from the Sun's luminosity alone.
- **The belts are as informative as the planets.** A region where accretion
  stalled tells you about the mechanism that made it succeed elsewhere.
- **Kepler's third law is a measurement tool, not only a law.** It converts a
  period and a distance into a mass, which is how essentially every mass in
  astronomy outside the solar system is determined.
- **Angular momentum is a conservation law and an embarrassment.** A model that
  ignores it cannot explain a slow-rotating Sun.
- **Escape parameterises the possible, not the actual.** A high $\lambda$ means a
  gas *can* be retained; whether it was ever there and whether chemistry removed
  it are separate questions.

## 9. Units and dimensional analysis

| Quantity | Expression | Units |
|---|---|---|
| Gravitational parameter | $4\pi^2a^3/T^2$ | m³ s⁻² |
| Orbital speed | $\sqrt{GM/a}$ | m s⁻¹ |
| Equilibrium temperature | $[(1-A)L/(16\pi\sigma a^2)]^{1/4}$ | W m⁻² K⁻⁴ × W m⁻² → K |
| Orbital angular momentum | $m\sqrt{GMa(1-e^2)}$ | kg × (m³ s⁻² × m)$^{1/2}$ = kg m² s⁻¹ |
| Escape speed | $\sqrt{2GM/R}$ | m s⁻¹ |
| Jeans parameter | $2GMm/(3kTR)$ | dimensionless |
| Mixture density | $1/\rho = f/\rho_2 + (1-f)/\rho_1$ | kg m⁻³ |

Two of these are worth checking by hand. The gravitational parameter in the table
is m³ s⁻², which is an acceleration times an area, i.e. the units of $GM$ — and
it is *not* a mass, which is why it is measured directly rather than $M$ itself.
The Jeans parameter must be dimensionless: $GMm$ is an energy times a length
(J m), and $kTR$ is also an energy times a length, so the ratio is dimensionless,
which is the check that no factor of the body's radius has been omitted.

## 10. Assumptions and regime of validity

1. **Circular orbits and $m \ll M$** in §3. For the planets the eccentricities
   are below 0.21 (Mercury) and mostly below 0.06, so the circular form is good
   to a few per cent; for a planet of comparable mass to its star, or for a
   close binary, the general two-body form is needed.
2. **A single radiating body heated only by the star** in (4). A body with
   internal heat, an atmosphere, or a high albedo in one band and a low one in
   another does not have a single equilibrium temperature. The Earth's 33.4 K
   greenhouse increment is the measure of how far the model is from the real
   surface temperature.
3. **A slab-like disk temperature profile** in §4. Real protoplanetary disks are
   heated from within by accretion and are optically thick, so their temperature
   falls more steeply than $a^{-1/2}$ and the ice line is model-dependent.
4. **A uniform interior** in (7). Real bodies are differentiated, so the mean
   density is a mixture of a core and a mantle rather than a homogeneous mixture,
   and the inversion is degenerate.
5. **Jeans escape with a specified exospheric temperature** in (6). The exospheric
   temperature is a model output that depends on the stellar ultraviolet flux and
   on the atmosphere's composition, and $\lambda$ depends exponentially on it
   through the escape rate.
6. **A closed system** in §5. Comets, escaping atmospheres and the solar wind all
   remove angular momentum and mass, so the present budget is not the initial
   one.

## 11. Python demonstration

[`code/solar_system_demo.py`](./code/solar_system_demo.py) computes all five
relations from printed inputs. Every planetary mass, semimajor axis and
eccentricity is labelled TABULATED, and the demo says so in its own output,
because these values are revised as ephemerides improve.

Kepler's third law used as a measurement, with the residual explained:

```text
  a  = 1 au            = 1.495979e+11 m  (defined)
  T  = sidereal year   = 3.155815e+07 s  (TABULATED)
  GM = 4 pi^2 a^3/T^2  = 1.327128e+20 m^3/s^2   (derived)
  GM tabulated (IAU)   = 1.327124e+20 m^3/s^2
  relative difference  = 2.931e-06
  GM_earth + GM_moon   = 4.0351e+14 m^3/s^2, which is 3.040e-06
  of GM_sun.  The derived value exceeds the tabulated one by almost
  exactly that fraction, because the orbit measured is the
  Earth-Moon barycentre's ...
```

The equilibrium temperature and the greenhouse residual:

```text
  With A = 0.3 the Earth's equilibrium temperature is
  254.6 K = -18.6 C.  The measured mean surface
  temperature of the Earth is about 288 K, so the difference,
  33.4 K, is the greenhouse effect of the atmosphere —
  derived here as a residual, not asserted.

     T_eq (K)   a (au)
         200      1.620
         273      0.870
         300      0.720
```

The angular-momentum budget and the escape parameter:

```text
  total planetary orbital angular momentum = 3.1342e+43 kg m^2/s
  total planetary mass = 2.6676e+27 kg
    I = 0.40 M R^2 -> L_sun = 1.1033e+42 kg m^2/s = 3.400 per cent of the system total
    I = 0.06 M R^2 -> L_sun = 1.6550e+41 kg m^2/s = 0.525 per cent of the system total

  Mass share of the Sun = 99.8661 per cent.
```

```text
  Earth: GM = 3.9860e+14, R = 6.3710e+06 m, T_exo = 1000 K (assumed)
      v_esc = 11186.1 m/s
        gas     m (u)   v_th (m/s)   lambda   retained?
         H2     2.016       3517.5      10.1   no
         He     4.003       2496.2      20.1   no
         N2    28.014        943.6     140.5   yes
        CO2    44.009        752.8     220.8   yes
```

### What to observe

- The derived $GM$ is high by 2.93 ppm and the mass of the Earth–Moon system is
  3.04 ppm of the Sun's — the two numbers agree to better than 4 per cent of the
  residual itself. When a discrepancy has a name, a size and a sign, it stops
  being an error and becomes a measurement.
- The ice line at 0.870 au for $T_\mathrm{eq} = 273$ K and 1.620 au for 200 K
  bracket the region where water ice is stable. Note that neither number is
  anywhere near the asteroid belt's inner edge at 2.1 au: the belt is not at the
  ice line, and the reason for its existence is Jupiter's gravity rather than
  temperature, which is a reminder that a scaling gives you the *region* and
  dynamics gives you the *detail*.
- The angular-momentum share of the Sun is between 0.5 and 3.4 per cent
  depending only on the interior rotation profile, and the *conclusion* is
  unaffected. Distinguishing which parts of a result are robust from which depend
  on an unknown is a habit worth acquiring here.
- The Mars column in the escape table predicts retention of N₂ and CH₄, and Mars
  has a surface pressure two orders of magnitude below the Earth's. The
  criterion is not wrong; it is incomplete, and the demo says so explicitly.

## 12. Common mistakes

1. **Comparing densities without correcting for compression.** A measured mean
   density is a compressed density, and a large body is compressed more.
2. **Using the equilibrium temperature as a surface temperature.** The two differ
   by the greenhouse effect, 33 K for the Earth.
3. **Forgetting the factor of 4 in the flux balance.** It is the ratio of a
   sphere's surface to its cross section, and omitting it gives a temperature
   that is $4^{1/4} = 1.41$ times too high.
4. **Treating the ice line as a sharp boundary.** It is a range set by volatile
   condensation temperatures and by a disk model.
5. **Quoting $GM$ as a mass.** For the Sun, $GM$ is measured; the mass requires
   $G$, which is the least precisely known constant in the calculation.
6. **Assuming the Sun's rotation dominates the angular momentum.** It holds
   0.01 per cent of the mass's worth of rotational angular momentum against the
   planets' orbital budget; the comparison is the point of the calculation.
7. **Using an escape parameter as a prediction of an atmosphere.** It is a
   threshold for thermal escape, and non-thermal processes frequently dominate.
8. **Mixing tabulated values from different sources in one calculation.** Masses,
   radii and gravitational parameters are revised independently, and the
   differences are large enough to show up in a comparison.
9. **Assuming the planets formed where they are now.** Migration is a standard
   part of current formation theory, so present positions are not birth
   positions.
10. **Reporting an absolute plume, radius or temperature without its source.**
    Every planetary quantity in this module is mission-derived and revisable.

## 13. Real-world applications

- **Exoplanet mass determination.** Every exoplanet mass outside a transit-timing
  or microlensing measurement comes from (2) applied to the host star
  ([04-08-04 Exoplanets, Habitability and Observational Constraints](./04-exoplanets-habitability.md)).
- **Mission design.** The $a^{-1/2}$ temperature scaling sets the thermal
  environment of every spacecraft and the science case for every target.
- **Comparative planetology.** The ice line is the reference frame in which the
  compositions of other systems are discussed.
- **Asteroid and comet resources.** The density and volatile content of small
  bodies follow the same mixture arithmetic as (7).
- **Planetary protection.** Escape and atmospheric loss bear on which bodies can
  retain a biologically relevant atmosphere or surface liquid
  ([12-07 Comparative Planetary Interiors](../../12-global-geophysics-interior/07-planetary-interiors-comparative/README.md)).
- **Space weather.** Escape from a planet is driven by the star's ultraviolet
  flux and wind, which is the same physics as the Sun's own mass loss.

## 14. Further reading

- **Newton, I. *Philosophiæ Naturalis Principia Mathematica* (1687).** Book III
  contains the derivations of Kepler's laws from gravitation, which (2) is a
  one-line modern version of. Level: historical.
- **Chandrasekhar, S. *An Introduction to the Study of Stellar Structure*
  (Dover).** The origin of the polytropic and degenerate relations used in
  lessons 02 and 04 of this module. Level: graduate.
- **Taylor, S. R. *Solar System Evolution: A New Perspective* (Cambridge
  University Press).** A geochemical account of the architecture, complementary
  to the dynamical one. Level: advanced.
- **Lodders, K. (2003). "Solar system abundances and condensation temperatures of
  the elements." *The Astrophysical Journal*.** The reference for the
  condensation temperatures behind the ice line, and the source of the
  abundance ordering in §2. Level: graduate.
- **NASA planetary fact sheets and the JPL Solar System Dynamics pages, reached
  from <https://www.nasa.gov>.** The standard reference values for masses,
  radii and orbital elements used as inputs here; confirm the current revision
  before quoting a value. Level: reference.
- **ESA science pages at <https://www.esa.int>.** Mission context and the
  current status of solar-system measurements. Level: reference.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 15. Related lessons

- [04-08-02 Planetary Interiors and Magnetic Fields](./02-planetary-interiors.md)
  — what the interior of a body does with the mass and composition that this
  lesson's densities constrain.
- [04-08-03 Planetary Geophysics from Orbiters and Landers](./03-planetary-geophysics-missions.md)
  — how the numbers used here are actually measured.
- [04-08-04 Exoplanets, Habitability and Observational Constraints](./04-exoplanets-habitability.md)
  — the same relations applied to systems where almost nothing is measured
  directly.
- [12-07 Comparative Planetary Interiors](../../12-global-geophysics-interior/07-planetary-interiors-comparative/README.md)
  — the interior structure of the Earth compared with its neighbours.
- [02-08-01 Newtonian Gravitational Potential and Field](../../02-physics/08-potential-theory/01-gravitational-potential.md)
  — the potential theory behind (1) and (2).
- [16-02-01 Solar and Terrestrial Radiation, Blackbody Laws](../../16-atmosphere-climate/02-radiation-and-energy-balance/01-solar-and-terrestrial-radiation.md)
  — the radiative balance of (4), treated in full.

Exercises:
[`exercises/01-solar-system-exercises.md`](./exercises/01-solar-system-exercises.md)
and
[`exercises/01-solar-system-solutions.md`](./exercises/01-solar-system-solutions.md).

## Self-assessment checklist

- [ ] I can state the four numbers that summarise the architecture of the solar
      system. (§1)
- [ ] I can associate each stage of the nebular hypothesis with an observation
      it explains. (§2)
- [ ] I can derive Kepler's third law from the force balance and interpret the
      constant. (§3)
- [ ] I can compute a gravitational parameter from a period and a distance, and
      explain a residual against a tabulated value. (§3)
- [ ] I can derive and evaluate the equilibrium temperature and identify the
      factor of 4. (§4)
- [ ] I can compute the ice line and state what it depends on. (§4)
- [ ] I can compute an orbital angular momentum and state the
      angular-momentum problem. (§5)
- [ ] I can compute an escape speed and a Jeans parameter and use them to predict
      which gases a body retains. (§6)
- [ ] I can state a case where the Jeans criterion fails and why. (§6)
- [ ] I can invert a two-component density for a composition and state why the
      result needs an interior model. (§7)
