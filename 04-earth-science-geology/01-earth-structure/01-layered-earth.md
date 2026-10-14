---
id: 04-01-01
title: "Crust, Mantle, Core: Seismological and Geochemical Evidence"
level: beginner
prereqs: ["00-04-01", "02-11-01", "01-01-03"]
estimated_minutes: 75
tags: [earth-structure, moho, core-mantle-boundary, prem, seismology, geochemistry]
---

# Crust, Mantle, Core: Seismological and Geochemical Evidence

Nobody has been deeper than about 12 km into the Earth. Everything below that
is inferred, and the inference is what this lesson is about. The Earth is
divided into crust, mantle and core, and the divisions are established by four
*kinds* of evidence that were gathered independently and that agree:

1. **Seismology.** Compressional (P) and shear (S) waves travel through the
   interior, and the travel times of thousands of earthquakes, recorded at
   thousands of stations, are inverted for velocity as a function of depth.
   Sharp changes in velocity mark the boundaries.
2. **The shadow zones.** Some paths through the Earth have no arrivals at all,
   and the geometry of those gaps constrains the velocities on both sides of a
   boundary. Lesson §3 shows the argument in full, and it is the most direct
   seismological statement about the outer core that exists.
3. **Geochemistry and petrology.** Meteorites of different classes, mantle
   xenoliths carried up by volcanoes, and the composition of the crust, when
   put together with the cosmochemical abundances of the elements, give a
   *compositional* model of the interior that has to be consistent with the
   seismic velocities and densities.
4. **Mineral physics.** Once the pressure and temperature at depth are known,
   the velocity of a candidate mineral assemblage can be computed in the
   laboratory and compared with the seismic profile. A compositional model
   survives only if its minerals have the right velocities at the right
   pressures.

The result is a layered model that reproduces four independent sets of numbers:
the Earth's mass, its moment of inertia, the pressure at the core–mantle
boundary, and the position of the seismic shadow zones. That agreement is
what makes the model credible, and the demo in §8 computes all four.

## Learning objectives

By the end of this lesson you will be able to:

1. **Name** the compositional layers — crust, mantle, outer core, inner core —
   and state the depth and the characteristic density and velocity of each.
2. **Explain** the S-wave shadow zone as evidence that the outer core is
   liquid, and explain why the *absence* of arrivals is stronger evidence than
   a low velocity would be.
3. **Derive** the P-wave shadow zone's existence from the fact that the P
   velocity *decreases* at the core–mantle boundary, and say what a velocity
   increase there would do instead.
4. **Compute** the Earth's mass, surface gravity and moment-of-inertia factor
   from a layered density model, and explain why the moment of inertia is the
   sharpest of the three as a test of radial structure.
5. **Compute** a hydrostatic pressure profile and state why pressure, not
   depth, is the variable that controls which minerals are stable.
6. **State** the geochemical argument that the core is iron-rich, and the
   mineral-physical test that a proposed mantle mineral assemblage has to pass.
7. **Explain** what "PREM" is, and why it is a *reference model* with stated
   assumptions rather than a measurement.
8. **Distinguish** an observation from an inference at every step of the
   argument, and say which of the four evidence types constrains each boundary.

## Prerequisites

- [00-04-01 What Geophysics Is: Physics of the Earth by Remote Measurement](../../00-orientation/04-orientation-geophysics/01-what-is-geophysics.md)
  — the idea that a measurement at the surface constrains the interior.
- [02-11-01 Pressure, Density and Gravity Inside the Earth](../../02-physics/11-physics-of-earths-interior-and-atmosphere/01-pressure-density-depth.md)
  — hydrostatic equilibrium and the gravity inside a spherically symmetric body.
- [01-01-03 Units, SI Conventions and Dimensional Analysis](../../01-mathematics/01-arithmetic/03-units-and-dimensional-analysis.md)
  — GPa, km/s and kg/m³, and why a dimensional check catches most errors.

## 1. The layers, and what defines each one

| Layer | Depth range | $\rho$ (kg/m³) | $v_p$ (km/s) | $v_s$ (km/s) |
|---|---|---|---|---|
| Continental crust | 0 – ~35 km | 2 600 – 2 900 | 5.8 – 6.5 | 3.2 – 3.7 |
| Oceanic crust | 0 – ~7 km | 2 800 – 3 000 | 6.5 – 7.0 | 3.5 – 3.8 |
| Uppermost mantle | below the Moho | ~3 300 | ~8.1 | ~4.5 |
| Transition zone | 410 – 660 km | 3 600 – 4 400 | 9.1 – 10.3 | 5.0 – 5.6 |
| Lower mantle | 660 – 2 891 km | 4 400 – 5 570 | 10.3 – 13.7 | 5.6 – 7.3 |
| Outer core (liquid) | 2 891 – 5 153 km | 9 900 – 12 200 | 8.0 – 10.3 | 0 |
| Inner core (solid) | 5 153 – 6 371 km | 12 800 – 13 100 | 11.0 – 11.3 | 3.5 – 3.7 |

These are the **rounded characteristic values** of the Preliminary Reference
Earth Model (PREM) as collected in
[26-02-03 Physical Constants and Earth Parameters with Sources](../../26-reference-library/02-symbols-and-units/03-constant-handbook.md);
they are *nominal*, not exact, and different reference models differ in the
third figure. Read the table for its structure rather than its digits.

Three features of the table carry the physics.

**The Moho.** The boundary between crust and mantle is a velocity
discontinuity at which $v_p$ jumps from about 6.5 to about 8.1 km/s. It was
found in 1909 by Andrija Mohorovičić from the arrival times of earthquakes
recorded at increasing distance from their epicentre: beyond a certain
distance a *second* wave arrives earlier than the direct one, which is only
possible if it has travelled through a faster layer below a sharp boundary.
That is the whole method — a discontinuity is discovered because a faster path
through a deeper layer overtakes a slower path through a shallower one.

**The core–mantle boundary.** At 2 891 km depth the density jumps by a factor
of about two while $v_p$ *falls* from 13.7 to 8.0 km/s. A discontinuity that
moves different properties in different directions is not a change of state; it
is a change of **composition**. A phase transition changes density and velocity
in the *same* sense, because a denser phase is generally also stiffer. The
core–mantle boundary therefore marks a change of material, and the material
below it must be much denser, which points to metal.

**The inner core.** $v_s$ is zero in the outer core and rises to about
3.5 km/s in the inner core. The outer core cannot transmit a shear wave; the
inner core can. The outer core is liquid and the inner core is solid, and the
inner core is *hotter* than the outer core. That apparent paradox is the
thermodynamics lesson: pressure raises the melting temperature faster than the
geotherm rises with depth, so the deepest material is solid even though it is
the hottest. See
[02-05 Thermodynamics](../../02-physics/05-thermodynamics/README.md).

## 2. How a flat Earth becomes a spherically symmetric inversion

The quantity a seismologist measures is a **travel time**, $T$, and an arrival
time is measured to a precision of a fraction of a second on a path that may
take twenty minutes. Turning that into a velocity at a depth is an inverse
problem with a long history, and the key is Snell's law in spherical geometry.

For a spherically symmetric model with velocity $v(r)$, every ray obeys

$$p = \frac{r \sin\theta}{v(r)} = \text{constant along the ray},$$

where $\theta$ is the angle between the ray and the radial direction and $p$ is
the **ray parameter**, in seconds. The epicentral distance $\Delta$ and the
travel time are then integrals from the turning point $r_{\min}$ (where
$r/v = p$) to the surface:

$$\Delta(p) = 2\int_{r_{\min}}^{R} \frac{p}{r\sqrt{r^2/v^2 - p^2}}\,\mathrm{d}r, \qquad
T(p) = 2\int_{r_{\min}}^{R} \frac{r}{v^2\sqrt{r^2/v^2 - p^2}}\,\mathrm{d}r.$$

Two consequences of these equations are used constantly in the interpretation
of the interior, and both are demonstrated numerically in §8:

- **A ray turns where $r/v = p$.** A velocity that increases with depth makes
  $r/v$ decrease with depth, so a ray launched downward eventually reaches a
  depth where $r/v = p$ and is bent back to the surface. The depth of that
  turning point is what a travel-time curve samples.
- **A velocity discontinuity splits a ray.** At a boundary the ray parameter is
  continuous, but the ray's direction changes because the velocity changes.
  Whether change is a refraction or a total reflection depends on the sign.

## 3. Physical reasoning: the shadow zones, from the sign of a jump

The Earth has two celebrated absences of arrivals, and they are the most
direct evidence about the core that exists.

**The S-wave shadow.** S waves are observed out to an epicentral distance of
about 103° and then not at all, until much larger distances where waves that
have travelled as P outside the core and converted back to S appear. If the
outer core had merely a *low* shear velocity, rays would still turn in it and S
would be observed inside the shadow. No S is observed because there is no shear
modulus below the core–mantle boundary at all. The core is liquid, and the
distinction between "slow in shear" and "cannot carry shear" is the whole
content of the observation.

**The P-wave shadow.** Direct P is strong out to about 103°, absent from about
103° to about 143°, and then returns as a much larger-amplitude arrival. This
gap exists because the P velocity *decreases* at the core–mantle boundary.

Here is the argument, which §8 computes. Take the ray parameter that just
grazes the core–mantle boundary,

$$p_\text{grazing} = \frac{r_\text{CMB}}{v_p(\text{bottom of mantle})} = \frac{3480}{13.7} = 254\ \text{s}.$$

A ray with a slightly larger ray parameter turns inside the mantle and never
reaches the core, so the *largest* distance reached by a mantle-only ray is
$\Delta(p_\text{grazing})$. A ray with this same $p$ that is *transmitted* into
the core must satisfy Snell's law on the other side,

$$\sin\theta_\text{core} = \frac{p\, v_\text{core}}{r_\text{CMB}},$$

and because $v_\text{core}$ is smaller than $v_\text{mantle}$, the transmitted
ray continues downward at a steep angle and turns deep inside the core. It
therefore re-emerges at a distance *larger* than the grazing distance. Between
the two there is no arrival: that is the shadow.

The sign of the jump is what creates the gap. If the velocity *increased* at
the core–mantle boundary, the transmitted ray would be refracted toward the
boundary, emerge at a distance smaller than the grazing ray's, and the shadow
would close. So the existence of the P shadow is a measurement of the sign of
the velocity jump, and it is a measurement that could have come out the other
way.

## 4. Quantitative treatment: mass, gravity, moment of inertia and pressure

Given a density profile $\rho(r)$, four quantities follow by integration over
the sphere, and each is an independent test of the profile.

**Mass.** With $R$ the surface radius,

$$M = 4\pi\int_0^{R}\rho(r)\,r^2\,\mathrm{d}r .$$

**Gravity inside the Earth** follows from the mass enclosed:

$$g(r) = \frac{G M(r)}{r^2}, \qquad M(r) = 4\pi\int_0^{r}\rho(r')\,r'^2\,\mathrm{d}r'.$$

**Moment of inertia.** For a spherically symmetric body,

$$I = \frac{8\pi}{3}\int_0^{R}\rho(r)\,r^4\,\mathrm{d}r,
\qquad \frac{I}{MR^2} = \text{the mass-weighted mean of } (r/R)^2 .$$

**Hydrostatic pressure.** Below the crust, where the material cannot support a
deviatoric stress over geological time, pressure satisfies

$$\frac{\mathrm{d}P}{\mathrm{d}r} = -\rho(r)\,g(r), \qquad P(R) = 0 .$$

Why the moment of inertia is the sharp test: a model can be tuned to produce
the right mass *or* the right surface gravity while putting the density at the
wrong radius. $I/(MR^2)$ measures *where* the mass is, so it cannot be fixed by
that kind of tuning. For a uniform sphere it is exactly $2/5 = 0.4000$; the
observed value is about 0.3307, and that single number is the quantitative
statement that the Earth is strongly concentrated toward its centre. A model
that matches the mass and the surface gravity but not the moment of inertia has
the right amount of mass in the wrong place.

Pressure is the variable that matters for mineralogy. The pressure at 30 km is
about 0.8 GPa and at the core–mantle boundary about 136 GPa, and the same
silicate mineral has completely different elastic properties at the two. This
is why a mineral-physical test of a compositional model needs a pressure and
temperature for every depth, and why
[02-11-02 Equations of State and High-Pressure Mineral Physics](../../02-physics/11-physics-of-earths-interior-and-atmosphere/02-equations-of-state.md)
comes before any claim about which minerals are down there.

## 5. Physical reasoning: the geochemical and mineral-physical arguments

Seismology gives velocities and densities. It does not give a chemical formula.
The composition comes from three sources, and each carries its own uncertainty.

**Meteorites.** Chondritic meteorites are undifferentiated samples of the early
solar system, and their elemental abundances provide a starting composition for
the bulk Earth. Iron meteorites are samples of differentiated metallic cores of
smaller bodies, and they are direct evidence that metallic iron–nickel liquid
separates from silicate melt. The Earth's core is iron-rich because (a) iron is
the most abundant heavy element in the cosmochemical inventory, (b) metal and
silicate separate under the conditions of planetary accretion, and (c) the core
density, around 10 000 to 12 000 kg/m³, requires a dense metal, with a light
element such as sulfur, oxygen, silicon or carbon mixed in to explain why the
core is slightly *less* dense than pure iron at those pressures.

**Mantle xenoliths.** Peridotite nodules carried up in alkali basalts and
kimberlites are actual mantle rock, sampled from depths of tens to a couple of
hundred kilometres. Their mineralogy — olivine, orthopyroxene, clinopyroxene
and an aluminous phase — defines the composition of the uppermost mantle, and
their elastic properties at pressure and temperature either match the seismic
velocities or they do not.

**Mineral physics.** For each candidate assemblage, the elastic moduli are
measured or computed at the relevant pressure and temperature and converted
into velocities:

$$v_p = \sqrt{\frac{K + \frac{4}{3}G}{\rho}}, \qquad v_s = \sqrt{\frac{G}{\rho}}.$$

The phase transitions at 410 km and 660 km are the sharpest example of this
test succeeding. Both discontinuities are now identified with specific
reactions — olivine to wadsleyite at 410 km, and ringwoodite to bridgmanite
plus ferropericlase at 660 km — and the predicted velocity and density jumps at
those reactions match the seismological discontinuities. That is a prediction
made before the seismology was precise enough to test it, which is the
strongest kind of agreement available in this subject.

## 6. Assumptions and regime of validity

| Assumption | Where it holds | What breaks without it |
|---|---|---|
| Spherical symmetry, $v = v(r)$ | Global average to a few kilometres of travel time | Lateral heterogeneity (subducting slabs, LLSVPs) perturbs travel times by seconds |
| Hydrostatic pressure | Below the seismogenic crust, over geological time | The upper few tens of km support shear stress; sedimentary basins are not hydrostatic |
| Radial density depends only on composition and phase | Everywhere except boundary layers and plumes | Thermal boundary layers at the top and bottom of the mantle have their own density structure |
| The outer core is liquid | Established by the S shadow | Nothing in this lesson survives without it |
| A reference model is a *reference* | As a baseline for anomalies | A 1-D model is not the Earth. PREM has no slabs, no plumes and no lateral variation |

The last row is important enough to state separately. PREM is a **reference
model**: a one-dimensional, spherically symmetric, transversely isotropic
average whose purpose is to be subtracted from observations so that the
interesting three-dimensional structure can be seen. Treating a reference model
as a description of the Earth is the most common category error in this
subject. The 410 km and 660 km discontinuities are *nominal* depths that vary
by tens of kilometres laterally, and that variation is part of the signal, not
noise.

## 7. Units and dimensional analysis

| Quantity | Unit | Check |
|---|---|---|
| Depth $z$ | km (crust and mantle), km | 1 GPa ≈ 33 – 36 km in the crust |
| Density $\rho$ | kg/m³ | 1 g/cm³ = 1000 kg/m³ |
| Velocity $v_p, v_s$ | km/s (or m/s) | $\sqrt{\text{Pa}/(\text{kg/m}^3)} = \text{m/s}$ |
| Pressure $P$ | GPa | $[\rho g z] = (\text{kg/m}^3)(\text{m/s}^2)(\text{m}) = \text{Pa}$ |
| Gravity $g$ | m/s² | $[GM/r^2]$ |
| Moment of inertia factor | dimensionless | A ratio; must lie in $(0, 0.4)$ |
| Ray parameter $p$ | s | $[r/v] = \text{m}/(\text{m/s})$ |

Two checks worth doing every time.

**The velocity-unit check.** $K/\rho$ has units $\text{Pa}/(\text{kg/m}^3) =
(\text{kg m}^{-1}\text{s}^{-2})/(\text{kg m}^{-3}) = \text{m}^2\text{s}^{-2}$,
so $\sqrt{K/\rho}$ is in m/s. A velocity quoted in km/s is a factor of 1000
smaller than the same velocity in SI, and mixing the two is the most common
arithmetic error in a hand calculation of this material — a $v_p$ of 8000
against a density of 3300 gives a nonsense modulus if the 8000 is read as km/s.

**The pressure check.** $\rho g z$ with $\rho = 2800$ kg/m³ and $z = 30$ km
gives $2800 \times 9.81 \times 3\times10^4 = 8.2\times10^8$ Pa ≈ 0.8 GPa. The
rule "1 GPa per 33 km in the crust" follows immediately, and so does the fact
that the rule fails in the mantle where $\rho$ is larger and the pressure
gradient is correspondingly steeper.

## 8. Python demonstration

[`code/layered_earth_demo.py`](./code/layered_earth_demo.py) builds a
seven-layer model from the rounded PREM values in the table of §1 and computes
the mass, surface gravity, moment-of-inertia factor, hydrostatic pressure
profile and the two shadow boundaries. It labels the comparison values
`TABULATED` and the computed values separately, so the two can never be
confused.

The mass, gravity and moment of inertia:

```text
  model mass                        = 5.9528e+24 kg
  TABULATED Earth mass              = 5.9722e+24 kg
  relative difference               = -0.3 %

  model surface gravity g(R)        = 9.7884 m/s^2
  TABULATED standard gravity        = 9.80665 m/s^2
  relative difference               = -0.2 %

  model moment-of-inertia factor    = 0.3327
  TABULATED I/(M R^2)               = 0.3307

  gravity at the core-mantle boundary (r = 3480 km) = 10.508 m/s^2
```

Three independent observables reproduced from one seven-layer density profile.
The moment-of-inertia factor agrees to half a per cent, which — as §4 argued —
is the agreement that actually constrains the radial structure. The computed
gravity at the core–mantle boundary, 10.51 m/s², is *larger* than at the
surface, because the dense core below contributes outward attraction while the
light mantle above contributes little inward attraction at that radius. A
homogeneous body would have $g$ falling linearly to zero at the centre.

The pressure profile:

```text
  core-mantle boundary   model   134.6 GPa   TABULATED  136.0 GPa   (-1.0 %)
  inner-core boundary    model   322.0 GPa   TABULATED  329.0 GPa   (-2.1 %)
  centre                 model   356.6 GPa
```

The small systematic underestimate is the coarse model's crust: it uses one
24 km "average" crust, so the mass of the light upper layers is wrong in
detail, and the pressure carries that error at every greater depth.

The shadow zones:

```text
  S waves.  The mantle ray that just grazes the core-mantle boundary:
    ray parameter   p = r_CMB / v_S = 3480 / 7.30 = 476.71 s
    distance        Delta = 90.4 deg
    TABULATED S-shadow entry = ~103 deg

  P waves.  The same ray parameter, p = r_CMB / v_P(bottom of mantle)
    = 254.01 s, gives two distances for the nominal model:
      mantle ray grazing the CMB   Delta =   89.1 deg,  T = 13.14 min
      same ray transmitted into the core, turning at r = 2329 km
                                   Delta =  172.0 deg,  T = 22.02 min
    TABULATED P-shadow zone = ~103 to ~143 deg
```

Both boundaries are within the right order and neither is exact, and the demo
says why rather than hiding it. The boundaries depend on the *shape* of the
mantle velocity gradient, not only on the ray parameter, so the demo sweeps a
one-parameter family of gradients and tabulates the result:

```text
       alpha   v_top (km/s)   Delta_S (deg)   Delta_P (deg)
      LAYERS           4.50            90.4            89.1   <- nominal model
        0.50           4.50            60.4            58.6
        1.00           4.50            85.8            84.4
        2.00           4.50           102.9           102.3
        4.00           4.50           108.8           108.5
        8.00           4.50           111.3           111.1
```

The observed value of about 103° sits between the rows at $\alpha = 2$ and
$\alpha = 4$, so the measured shadow boundary is itself a measurement of the
mantle velocity gradient. That is the general shape of the argument in this
subject: the interior is not observed directly, it is constrained, and every
observation constrains a *combination* of model parameters rather than one of
them in isolation.

The counterfactual test in the same section is the direct evidence for a liquid
outer core. Give the outer core a finite shear velocity of 4.0 km/s and the
grazing ray refracts into it and turns, so S arrivals would appear inside the
shadow; they do not. The demo then does the same for the P shadow in reverse:
increase the velocity at the core–mantle boundary to 16 km/s and
$\sin\theta_\text{core} = 1.168 > 1$, which has no solution, so the ray cannot
enter the core at all and the shadow closes.

## 9. Common mistakes

1. **Reading a reference model as the Earth.** PREM is a 1-D average. Quoting
   "the" depth of the 410 km discontinuity without a range turns a nominal
   value into a false measurement.
2. **Confusing the compositional and rheological divisions.** Crust/mantle/core
   is composition. Lithosphere/asthenosphere is rheology. They do not share
   boundaries, and
   [04-01-02](./02-lithosphere-asthenosphere.md) exists because of it.
3. **Thinking the S shadow means the outer core is slow.** It means the outer
   core has *no* shear modulus. A fluid with a small but finite $v_s$ would put
   arrivals inside the shadow.
4. **Quoting a density jump and a velocity jump as if they must agree.** At the
   core–mantle boundary they disagree in sign, and that disagreement is the
   evidence for a compositional change.
5. **Using the depth–pressure rule outside its range.** 1 GPa ≈ 33 km is a
   crustal rule at $\rho = 2800$ kg/m³; at the base of the mantle the gradient
   is about five times steeper.
6. **Assuming the mantle is homogeneous.** Xenoliths, seismic tomography and
   the discontinuities themselves all say otherwise.
7. **Treating the inner core as "the hottest part, therefore liquid".** The
   inner core is solid because pressure raises the melting point faster than
   the geotherm rises.
8. **Taking a velocity to be a composition.** A velocity constrains a
   *combination* of composition, temperature and phase; inverting it for one
   of those requires the other two.

## 10. Real-world applications

- **Global seismology and tomography.** Every earthquake location uses a
  reference velocity model, and every tomographic image is a perturbation away
  from one ([12-01 Seismic Structure of the Earth](../../12-global-geophysics-interior/01-seismic-structure-of-the-earth/README.md)).
- **Nuclear test monitoring.** Discrimination between an explosion and an
  earthquake uses the P/S amplitude ratio, which requires knowing how the waves
  travel through the real, laterally varying Earth.
- **Mineral exploration at depth.** The depth to the Moho, and the density
  contrast across it, is the background against which a crustal-scale gravity
  or seismic survey is interpreted.
- **Geothermal and basin studies.** The pressure and temperature at depth set
  the fluid properties, and the layered velocity model converts a seismic
  reflection time into a depth.
- **Planetary science.** The same four evidence types are applied to Mars, the
  Moon and Mercury, and the comparison is how we know which of the Earth's
  features are universal
  ([04-08 Planetary Science](../08-planetary-science/README.md)).

## 11. Further reading

- **Dziewonski, A. M., & Anderson, D. L. (1981). Preliminary reference Earth
  model. *Physics of the Earth and Planetary Interiors* 25, 297–356.** The
  paper that defines PREM; the source of the table in §1. Level: advanced.
- **Anderson, D. L. *Theory of the Earth* (Blackwell).** A textbook built
  around the argument of this lesson, from seismology to composition.
  Level: advanced.
- **Shearer, P. M. *Introduction to Seismology* (Cambridge University Press).**
  Chapters on travel times and the ray parameter give §2 and §3 in full
  detail. Level: intermediate.
- **Poirier, J.-P. *Introduction to the Physics of the Earth's Interior*
  (Cambridge University Press).** The mineral-physics side: equations of
  state, phase transitions and the elasticity of mantle minerals.
  Level: graduate.
- **Irvine, G. J., et al., *PREM* digital model availability.** Reference-model
  coefficients are distributed as tabulated files; confirm the current
  distribution point before citing a table.
- **Meteoritical Society, *Meteoritical Bulletin Database*.** The
  authoritative inventory for chondrite and iron-meteorite compositions used
  in the geochemical argument of §5.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 12. Related lessons

- [04-01-02 Lithosphere, Asthenosphere and the Rheological Definition](./02-lithosphere-asthenosphere.md)
  — the other, non-compositional way of dividing the outer Earth.
- [04-01-05 Density, Porosity, Permeability and Elastic Properties](./05-rock-physics-basics.md)
  — the crustal and upper-mantle property relations that a survey measures.
- [04-02-01 Continental Drift to Plate Tectonics: The Evidence Trail](../02-plate-tectonics/01-tectonic-theory.md)
  — what happens when the interior is put in motion.
- [02-11 Physics of the Earth's Interior and Atmosphere](../../02-physics/11-physics-of-earths-interior-and-atmosphere/README.md)
  — the physics behind §4 and §5 in full.
- [12-01-01 PREM, IASP91 and Reference Earth Models](../../12-global-geophysics-interior/01-seismic-structure-of-the-earth/01-prem-and-reference-models.md)
  — what a reference model is used for, and its three-dimensional successors.

Exercises:
[`exercises/01-layered-earth-exercises.md`](./exercises/01-layered-earth-exercises.md)
and
[`exercises/01-layered-earth-solutions.md`](./exercises/01-layered-earth-solutions.md).

## Self-assessment checklist

- [ ] I can name the compositional layers with a depth and a characteristic
      density and velocity for each. (§1)
- [ ] I can explain the Moho as the discovery of a faster deeper path. (§1)
- [ ] I can explain why a density jump with a velocity drop implies a change of
      composition rather than a change of state. (§1)
- [ ] I can derive the S-wave shadow from $p = r\sin\theta/v$ and explain why
      no arrival is stronger evidence than a slow arrival. (§3, §8)
- [ ] I can explain why the P shadow requires a velocity *decrease* at the
      core–mantle boundary. (§3, §8)
- [ ] I can compute the mass, surface gravity and moment-of-inertia factor from
      a layered density profile. (§4, §8)
- [ ] I can explain why the moment of inertia is the sharpest test of radial
      structure. (§4)
- [ ] I can compute a hydrostatic pressure profile and give the crustal depth
      that corresponds to 1 GPa. (§4, §7)
- [ ] I can state the geochemical argument for an iron core and the
      mineral-physical test of a mantle assemblage. (§5)
- [ ] I can state what a reference model is and what it is not. (§6)
- [ ] I can say which of the four evidence types constrains each boundary.
      (§1–§5)
