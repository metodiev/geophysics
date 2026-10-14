---
id: 02-11-05
title: "Comparative Planetary Physics and Interiors"
level: doctoral
prereqs: ["02-11-01", "02-11-03", "02-11-04"]
estimated_minutes: 90
tags: [planetary-interiors, moment-of-inertia, geodynamo, atmospheric-escape]
---

# Comparative Planetary Physics and Interiors

The previous four lessons built a description of one planet, and they did it with
three instruments that were all Earth-specific: a layered density model, a
seismological velocity model, and a standard atmosphere. On any other body at
least two of the three are unavailable. This lesson is about what remains.

Three diagnostics transfer, and each has a different shape.

**The moment of inertia factor $k = C/(MR^2)$** is a single dimensionless number
between 0 and 0.4 that measures central condensation. It can be measured from a
body's gravity field and rotation, it requires no seismology, and lesson
[01](./01-pressure-density-depth.md) §3.4 already computed the Earth's value as
0.3326 against a nominal 0.33. For every other body in the solar system it is
the primary structural constraint. §1 works the inversion in closed form and
establishes both what it proves and where it is degenerate.

**The magnetic Reynolds number** $Rm = \mu_0\sigma UL$ decides whether a
conducting, moving fluid can sustain a magnetic field. It is a dimensionless
number built from three properties that can be estimated well enough to be
useful, and it organises the observed pattern of which bodies have magnetic
fields. §3 derives it and computes the associated timescales for the Earth.

**The Jeans escape parameter** $\lambda = GMm/(kTr)$ decides which atmospheric
constituents a body can retain. It explains in one formula why the giant planets
hold hydrogen and helium and the terrestrial planets do not. §4 derives and
evaluates it.

Two closing cautions. First, the diagnostics are *necessary* and not
*sufficient*: a low $k$ shows that a body has dense material toward its centre,
not that it has an iron core. Second, **this lesson deliberately does not quote
magnetic field strengths, core radii or compositions for individual planets**,
because those numbers require mission-specific sources, they are revised as
missions return data, and an unsourced value in a teaching text is worse than no
value at all. Where a number appears below it is either an Earth number from the
[constant handbook](../../26-reference-library/02-symbols-and-units/03-constant-handbook.md),
or a computed quantity from the demo. For other bodies, use the current NASA and
ESA mission archives.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** $C/(MR^2) = 0.4$ for a homogeneous sphere and $0$ for a point mass,
   and derive the two-layer formula
   $k = 0.4(f^5\alpha+1-f^5)/(f^3\alpha+1-f^3)$.
2. **Invert** the Earth's $k$ with its seismological core radius to obtain the
   density contrast and mean core density implied by a two-layer model.
3. **Explain** the degeneracy that leaves $k$ alone unable to give both core size
   and core density, and name the measurements that break it.
4. **Derive** the induction equation's two terms, define the magnetic Reynolds
   number and the magnetic diffusion time, and evaluate both for the Earth.
5. **Compare** the magnetic diffusion time with the thermal diffusion time across
   the same core, and explain why that comparison requires convection.
6. **Name** the three requirements for a dynamo and use them to account for which
   bodies have intrinsic magnetic fields.
7. **Derive** the Jeans escape parameter and the scale height, evaluate them for
   several molecular species, and explain selective atmospheric loss.
8. **State** what each diagnostic does *not* determine, and why the mass–radius
   degeneracy is the fundamental limitation of exoplanet interior modelling.

## Prerequisites

- [02-11-01 Pressure, Density and Gravity Inside the Earth](./01-pressure-density-depth.md)
  — the moment-of-inertia integral, and the reference model used as the Earth
  case throughout.
- [02-11-03 Seismic Velocities, Elastic Moduli and Mineralogy](./03-seismic-parameter-relations.md)
  — the composition inference that is available for the Earth and unavailable
  elsewhere.
- [02-11-04 Atmospheric Structure](./04-atmospheric-structure.md) — the scale
  height and hydrostatic balance used in §4.
- [02-07-04 Faraday's Law, Induction and Eddy Currents](../07-electromagnetism/04-em-induction.md)
  — the induction equation and magnetic diffusivity.
- [02-06-06 Mantle Convection](../06-fluid-mechanics/06-mantle-convection.md) —
  the convection criterion that the dynamo and the surface heat flow share.

## 1. The moment of inertia as the primary diagnostic

### 1.1 The quantity and its limits

For a spherically symmetric body of radius $R$ and mass $M$, the polar moment of
inertia is

$$C = \frac{8\pi}{3}\int_0^R \rho(r)\,r^4\,\mathrm{d}r, \qquad k \equiv \frac{C}{MR^2}. \qquad (1)$$

Two values are fixed by geometry, whatever the body:

- **Homogeneous sphere.** $\rho$ constant gives $C = \tfrac25MR^2$, so
  $k = 0.400$. This is the maximum.
- **Point mass at the centre.** $C\to0$, so $k\to0$. This is the minimum.

Everything real lies between. The Earth's nominal $k = 0.33$ (computed as 0.3326
in lesson [01](./01-pressure-density-depth.md) §3.4 from the layered model) is a
statement that the Earth's mass is *partly* de-leveraged, and the whole art of
using $k$ is deciding how much of that is a dense core and how much is ordinary
self-compression of a material whose density rises with pressure. The two effects
are not separable from $k$ alone, and §1.4 says what separates them.

$k$ is measured, in practice, from a body's degree-2 gravity coefficient and its
rotation — the same data that give the flattening — because a rotating body's
flattening and its moment of inertia are linked through the Darwin–Radau
relation. Precession and nutation provide second and third routes; see
[12-global-geophysics-interior/06-01](../../12-global-geophysics-interior/06-geodesy-constraints-interior/01-moment-of-inertia.md).

### 1.2 The two-layer inversion, in closed form

Consider a body with a core of radius fraction $f = r_c/R$ and a core density
$\alpha$ times the mantle density $\rho_m$. Then

$$M = \tfrac43\pi R^3\rho_m\left[f^3\alpha + 1 - f^3\right], \qquad
C = \tfrac{8}{15}\pi R^5\rho_m\left[f^5\alpha + 1 - f^5\right],$$

and dividing,

$$k = 0.4\,\frac{f^5\alpha + 1 - f^5}{f^3\alpha + 1 - f^3}. \qquad (2)$$

The $0.4$ is the homogeneous value; the fraction is the central condensation. For
the Earth, take $f = 3480/6371 = 0.5462$ from the handbook's core depths, and
solve equation (2) for $\alpha$:

$$k = 0.33 \quad\Longrightarrow\quad
\alpha = \frac{0.4(1-f^5) - k(1-f^3)}{k\,f^3 - 0.4\,f^5} = 3.039.$$

Then $M = 5.972\times10^{24}$ kg fixes the absolute scale:
$\rho_m = 4138$ kg m⁻³, hence a **mean core density of 12 576 kg m⁻³.**

Two things about that result.

**It lands where the seismological model puts it, independently.** The handbook's
outer core is 9900–12 200 kg m⁻³ and its inner core 12 800–13 100 kg m⁻³. A
two-parameter fit driven only by total mass, radius, moment of inertia and a
seismological core radius returns a mean core density of 12 576 kg m⁻³. That is
the classical argument for a dense core, and the fact that the *magnitude* comes
out right from completely different data is the reason it is believed.

**It is still a two-layer cartoon.** The real core is 9900 kg m⁻³ at its top and
13100 at its centre; the real mantle varies likewise. The 12 576 figure is a mean,
and lesson [01](./01-pressure-density-depth.md) §3.3 showed what a mean-density
core does to the central pressure — it over-predicts it by 9 per cent. So this
inversion constrains the *amount* of dense material, not its distribution.

### 1.3 The degeneracy, on a grid

Evaluating equation (2) over a range of $(f,\alpha)$ shows the structure of the
problem without any assumptions about which planet you are discussing:

| $f$ | $\alpha=1.0$ | $\alpha=1.5$ | $\alpha=2.0$ | $\alpha=3.0$ | $\alpha=4.0$ |
|---|---|---|---|---|---|
| 0.00 | 0.4000 | 0.4000 | 0.4000 | 0.4000 | 0.4000 |
| 0.20 | 0.4000 | 0.3985 | 0.3970 | 0.3940 | 0.3910 |
| 0.40 | 0.4000 | 0.3896 | 0.3798 | 0.3619 | 0.3459 |
| 0.50 | 0.4000 | 0.3824 | 0.3667 | 0.3400 | 0.3182 |
| 0.55 | 0.4000 | 0.3786 | 0.3602 | 0.3303 | 0.3071 |
| 0.60 | 0.4000 | 0.3750 | 0.3545 | 0.3228 | 0.2993 |
| 0.70 | 0.4000 | 0.3701 | 0.3479 | 0.3170 | 0.2965 |
| 0.80 | 0.4000 | 0.3706 | 0.3512 | 0.3271 | 0.3128 |

The $\alpha = 1$ column is flat at 0.4000 (a homogeneous body, however the layers
are labelled) and the $f = 0$ row is flat (a core of zero radius does nothing).
Between those limits $k$ falls as the core grows *or* as the density contrast
grows, so a measured $k$ fixes a **curve** in the $(f,\alpha)$ plane, not a point.
A body with $k = 0.33$ could have a large core with a modest contrast or a
smaller core with a large one. The last row shows a further subtlety: beyond
$f\approx0.7$ the curves turn over, because a large enough core starts to
displace mantle material outward faster than it concentrates mass.

### 1.4 What breaks the degeneracy

In increasing order of strength:

- **A seismologically or geodetically determined core radius**, which is what
  let us solve for $\alpha$ rather than a curve. Available for the Earth, and in
  a weaker form for the Moon and Mars through geodetic and seismic data.
- **Self-compression, constrained by an equation of state.** A body's own weight
  compresses it, so $k$ falls with mass even at fixed composition (lesson
  [02](./02-equations-of-state.md) §4). This is not a nuisance but a *signal*: it
  means a low $k$ can be produced by size alone, and accounting for it correctly
  is what turns $k$ into a compositional statement.
- **The degree-3 or higher gravity coefficients and the rotation rate**, which
  pin the flattening and hence the radial density distribution more tightly than
  $k$ alone.
- **For the Earth, seismology in full.** That is why the Earth is the only body
  whose interior is known in detail, and why every other planet's structure is
  reported as a family of models rather than a profile.

## 2. Interiors without seismology

### 2.1 The inference loop

On a body with no seismology, the loop of lesson
[02](./02-equations-of-state.md) §5 shortens to three steps.

1. **Measure** $M$, $R$, $k$, the rotation rate and the gravity field.
2. **Assume** a composition and a thermal state, hence an equation of state.
3. **Compute** the hydrostatic structure and compare the predicted $M$, $R$ and
   $k$ with the measured ones. Adjust until they match — or, better, map out the
   full set of models that match within the uncertainties.

Step 3 is the whole content. The output is never a single answer; it is a
*degeneracy curve* or a region in parameter space, and reporting it as a single
model is the commonest error in planetary interior papers.

### 2.2 The fundamental limitation

Two numbers, $M$ and $R$, with one or two more constraints, against an unknown
composition, an unknown core size, an unknown thermal state, and an unknown
distribution of light elements. The degeneracy is severe, and it is intrinsic:
for a given $M$ and $R$ a body can trade a larger iron core against a hotter
interior, or a lighter mantle against a denser core, and remain within the data.

The standard demonstrations of an interior structure — the moment of inertia from
a passing spacecraft, the tidal Love number $k_2$ from a repeated flyby, the
libration amplitude from a lander's radio tracking — each add one constraint.
This is why planetary missions are designed around specific measurements rather
than around "visiting", and why a single well-chosen measurement (a moment of
inertia, a Love number) can be worth more than a large volume of lower-precision
data.

### 2.3 What the Earth contributes

The Earth is the calibration point for all of this. Its $k$, its core radius, its
core density, its adiabat and its equation of state were discussed in lessons
[01](./01-pressure-density-depth.md)–[03](./03-seismic-parameter-relations.md),
and every one of those numbers is used as a prior when interpreting another body.
The honest statement of the Earth's role is this: **the Earth tells us what a
one-solar-mass, rocky, differentiated body looks like when you can measure it in
detail, and everything about other bodies is an extrapolation of that template
into different mass, temperature and composition regimes.** The extrapolation is
where the difficulty lies, and it is a difficulty of equations of state
(lesson [02](./02-equations-of-state.md) §6) rather than of gravity.

## 3. Magnetic fields and the dynamo criteria

### 3.1 The induction equation and $Rm$

In a moving conductor, the magnetic field obeys the induction equation:

$$\frac{\partial \mathbf B}{\partial t}
= \underbrace{\nabla\times(\mathbf u\times\mathbf B)}_{\text{advection}}
+ \underbrace{\eta\nabla^2\mathbf B}_{\text{diffusion}},
\qquad \eta = \frac{1}{\mu_0\sigma}. \qquad (3)$$

Non-dimensionalise by a flow speed $U$ and a length scale $L$. The ratio of the
advection term to the diffusion term defines the **magnetic Reynolds number**

$$Rm = \frac{UL}{\eta} = \mu_0\sigma UL. \qquad (4)$$

- $Rm \ll 1$: diffusion wins, any field decays, and the field is enslaved to the
  flow (this is the regime of every geophysical electromagnetic method, where the
  relevant $Rm$ is tiny).
- $Rm \gg 1$: advection wins, field lines are frozen into the fluid and are
  stretched, folded and amplified by the flow. This is the regime in which a
  self-sustaining dynamo is possible.

The threshold is not exactly 1. Dynamo action requires $Rm$ above a value of order
tens, because the amplification has to outrun diffusion in a geometry that also
has to close on itself, and the exact critical value depends on the flow geometry.
But the *order of magnitude* is what makes the criterion useful.

For the Earth's outer core, with nominal values $\sigma = 10^6$ S m⁻¹ (liquid iron
alloy), $U = 3\times10^{-4}$ m s⁻¹ (0.3 mm/s, the core-flow speed inferred from
secular variation) and $L = 2\times10^6$ m:

$$Rm = 1.2566\times10^{-6}\times10^6\times3\times10^{-4}\times2\times10^6
= 754.$$

Comfortably above threshold. Every ingredient here is nominal — the conductivity
of iron at core conditions is itself an active research topic — but the value is
three orders of magnitude clear of the boundary, so the conclusion is robust to
factor-of-two errors in any of the three.

### 3.2 Diffusion times

The diffusion time is the time over which a field would decay if the motion
stopped:

$$\tau_\eta = \frac{L^2}{\eta} = \mu_0\sigma L^2
= 1.2566\times10^{-6}\times10^6\times(2\times10^6)^2
= 5.03\times10^{12}\ \text{s} = 1.59\times10^{5}\ \text{yr}.$$

A field with no dynamo decays in about $10^5$ years. Palaeomagnetic evidence for
a field spanning billions of years is therefore direct evidence that the dynamo
has operated for that long: the field cannot have been a fossil. That single
comparison — $10^5$ yr of possible memory against $4.5\times10^9$ yr of observed
field — is the reason the geodynamo is not optional.

### 3.3 Why convection is required

A second timescale makes the energy requirement explicit. Thermal diffusion across
the same length with a nominal thermal diffusivity $\kappa = 10^{-5}$ m² s⁻¹ for
liquid iron gives

$$\tau_\kappa = \frac{L^2}{\kappa} = 4.0\times10^{17}\ \text{s}
= 1.27\times10^{10}\ \text{yr},$$

which is **nearly three times the age of the Earth.** A core that could remove its
heat only by conduction would still be almost isothermal after 4.5 Gyr; its
heat would effectively be trapped. Two consequences:

- **The core must convect**, because conduction is too slow to carry the heat
  out, and the heat must go somewhere.
- **The same convection is what the dynamo needs.** The thermally driven buoyancy
  and the compositional buoyancy released as the inner core grows both drive the
  flow that $Rm \gg 1$ requires.

The two requirements have one mechanism, and that is the reason the geodynamo is
robust rather than delicate.

### 3.4 Three ingredients, and the comparative pattern

A dynamo needs, all three at once:

1. **a conducting fluid region** — the iron-alloy outer core on the Earth;
2. **an energy source driving convection** in that region;
3. **rotation** to organise the flow into a large-scale, coherent field.

The observed pattern of intrinsic planetary magnetic fields is organised by how
many of the three are present, and the pattern is qualitative and
mission-derived, so it is stated here without numbers.

- **Earth.** All three. The strongest and most dipole-dominated field among the
  terrestrial planets, with the dipole inclined a few degrees to the rotation axis
  (about 10° in the handbook's nominal figure, and time-varying).
- **Mercury.** All three, but with a small, slowly convecting core: a weak field
  with a substantially offset and tilted dipole.
- **Jupiter and Saturn.** All three, in a hydrogen-metallic interior rather than
  an iron core, and with far larger energy sources: fields much stronger than the
  Earth's. Rotation dominates the field geometry, so both have nearly
  axisymmetric dipoles.
- **Uranus and Neptune.** All three, but the fields are strongly tilted and
  strongly offset from the centre, which is not what a dynamo acting in a thin
  outer shell of a known geometry would produce. The accepted explanation is that
  the dynamo acts in a deep, thick conducting shell, and the geometry of that
  shell — not the flow — sets the field's structure.
- **Venus.** No present-day intrinsic field. The dynamo criterion is therefore
  being violated in one of its three requirements, and the candidates are all
  about energy: a stagnant-lid planet has no efficient mechanism for removing
  core heat, and a slow rotation rate weakens the organising effect. Which of
  these dominates is an open question, and it is a good example of a comparative
  argument that the observations constrain but do not yet settle.
- **Mars.** No present-day global dynamo field, but strong *crustal remanent*
  magnetization — rocks magnetised by a field that existed early in its history.
  This is a strictly stronger statement than "no field today": the dynamo
  operated once and then stopped, and the reason is that a small body cools and
  its core either solidifies or becomes stably stratified, killing convection.
  Mars is the clearest natural experiment on dynamo *cessation*.
- **The Moon.** Remanent magnetization but no global field today: the same story
  with an earlier shutdown.
- **Ganymede.** The only moon with an intrinsic field at present, which is
  notable because it shows that the three ingredients are not limited to planets.

## 4. Atmospheres: scale height and escape

### 4.1 The scale height, revisited

From lesson [04](./04-atmospheric-structure.md) §1.3, the pressure scale height
of an isothermal atmosphere is

$$H = \frac{R_{\text{specific}}T}{g} = \frac{k_BT}{mg}, \qquad (5)$$

where the second form makes the composition dependence explicit through the mean
molecular mass $m$. Two structural consequences transfer immediately to any
body: **a hotter atmosphere is a puffier one at the same pressure**, and **a
higher surface gravity compresses it**. Escape, however, depends on something
else.

### 4.2 The Jeans escape parameter

A molecule at the top of an atmosphere escapes if its kinetic energy exceeds the
gravitational binding energy at that radius $r$:

$$\tfrac12 mv^2 > \frac{GMm}{r}.$$

The ratio of the two, evaluated for the thermal population, is the **Jeans escape
parameter**

$$\lambda = \frac{GMm}{k_BTr} = \frac{v_{\text{esc}}^2m}{2k_BT},
\qquad v_{\text{esc}} = \sqrt{\frac{2GM}{r}}. \qquad (6)$$

$\lambda$ is roughly the ratio of gravitational to thermal energy for one
molecule. It is proportional to the molecular mass, so **escape is selective**:
the lightest species go first, and the same exosphere that retains nitrogen
loses hydrogen.

A body retains a species over billions of years when $\lambda$ is of order a few
tens. Below about 10 the escape is fast; between 10 and 30 it is slow but
significant over geological time. The threshold depends on the species and on the
age, and the formula is a hydrostatic-thermodynamic estimate rather than a full
kinetic calculation — non-thermal escape mechanisms (charge exchange, pick-up,
photodissociation-driven blow-off, and hydrodynamic escape) matter for hydrogen
and for any body with a strong stellar wind.

Evaluating equation (6) for the Earth, with an exobase at 500 km altitude, an
exobase radius of 6871 km and a nominal exospheric temperature of 1000 K (the
temperature varies by a factor of two with solar activity, so this is an anchor):

| Species | $m$ (u) | $H$ (km) | $\lambda$ | Retained? |
|---|---|---|---|---|
| H₂ | 2.016 | 488.5 | 14.1 | Slowly lost |
| He | 4.003 | 246.0 | 27.9 | Slowly lost |
| N₂ | 28.014 | 35.2 | 195.5 | Retained |
| O₂ | 31.998 | 30.8 | 223.3 | Retained |
| CO₂ | 44.010 | 22.4 | 307.1 | Retained |

($v_{\text{esc}}$ at the exobase is 10.77 km/s.)

Read the two columns together. **The scale height falls with molecular mass and
the Jeans parameter rises with it**, so heavy species both occupy a thin layer
and are hard to remove, while light species extend far out and leak. That is the
whole mechanism of selective escape, and it accounts for the composition of
every terrestrial-planet atmosphere: hydrogen and helium were lost from the inner
solar system, and nitrogen, oxygen and carbon dioxide were retained.

### 4.3 Comparative consequences, without numbers

Three qualitative rules follow directly from equations (5) and (6) and organise
every atmosphere in the solar system.

**Mass matters.** $\lambda \propto M/r$ (approximately, since $r\approx R$ for
a thin atmosphere), so a more massive body of similar size retains more. This is
the primary reason the giant planets kept their hydrogen and helium envelopes
while the terrestrial planets did not, and it is a statement about $M$, not about
distance from the Sun.

**Temperature matters, and inversely.** A hot exosphere is an escaping exosphere,
because $\lambda \propto 1/T$. This is why the same species that a body retains
when it is quiet it can lose when its star is active, and why escape rates vary
with the stellar cycle.

**Distance matters through temperature, not directly.** A body further out is
colder, its exosphere is cooler, and $\lambda$ is larger at the same mass and
radius. This is a statement about the temperature, and it is the reason the
"habitable zone" is not simply a distance.

The three effects compete, which is why the atmospheric inventories of the bodies
in the solar system are so varied. The physics of §4 is a *framework*; assigning
the observed inventories to the framework requires per-body data.

## 5. Physical interpretation: what differs, and why

**Mass sets the compression, and compression sets the structure.** A larger body
of the same composition compresses more under its own gravity, so its central
density is higher and its $k$ lower, with no compositional change at all. This is
the reason $k$ cannot be read as "iron content" without an equation of state, and
it is why the largest rocky bodies require the most careful interior modelling.

**Rotation sets the field geometry, and geometry sets the field shape.** The
Earth, Jupiter and Saturn have nearly axisymmetric dipoles because rotation
dominates their dynamo flows. Uranus and Neptune do not, which is the strongest
single observational argument that their dynamos act in thick shells with a
geometry unlike the Earth's. Field *geometry* is therefore a probe of the dynamo
region's shape, not just of its existence.

**Composition sets the equation of state, and the equation of state sets
everything else.** An iron core, a hydrogen-metallic envelope and an ice mantle
are three completely different materials at the same pressure, and they are
described by different equations of state with different behaviours under
compression. Most of the difference between planetary interiors is a difference
of material rather than of gravity.

**Loss processes are selective, which is why atmospheres are not simply scaled
versions of each other.** Equation (6) is a statement about one species at a
time. A body does not lose its atmosphere; it loses its lightest constituents
first, and the residual composition records the history.

## 6. Assumptions and regime of validity

| Assumption | Where used | Regime of validity | What breaks it |
|---|---|---|---|
| Spherical symmetry and no rotation for $k$ | §1 | The moment of inertia is defined for a rotating body; the spheroidal correction is what makes $k$ measurable | Rapidly rotating bodies, where the Darwin–Radau relation and the flattening must be used jointly |
| Two-layer model | §1.2 | A cartoon that separates core from mantle | Continua; the real core has its own density gradient |
| Composition is uniform within a layer | §1–§2 | A modelling choice to make the problem finite | Compositional gradients, which are precisely what the measurements are used to detect |
| Hydrostatic equilibrium | §1–§2 | Excellent for slowly rotating bodies | Rapidly rotating and tidally distorted bodies, where the figure equations replace it |
| $\sigma$, $U$ and $L$ are known in the core | §3.1 | Nominal estimates, good to a factor of about two | The electrical conductivity of iron at core conditions is itself uncertain |
| The dynamo threshold is "of order tens" | §3.1 | Correct to an order of magnitude | The precise critical $Rm$ depends on the flow; kinematic dynamo studies give a range |
| Thermal diffusivity of the core is $10^{-5}$ m² s⁻¹ | §3.3 | A nominal value; published estimates span a factor of a few | The same conductivity uncertainty as above |
| Jeans escape is the dominant loss mechanism | §4.2 | Adequate for a first assessment | Non-thermal escape, hydrodynamic escape, and impact erosion, all of which matter for light species and for young systems |
| Exobase at a fixed radius and temperature | §4.2 | A convenient idealisation | Exobase height and temperature both vary strongly with solar activity |
| Bodies are not observed to change | §1–§4 | All the diagnostics are snapshots | Thermal evolution changes every one of them over billions of years |

## 7. Units and dimensional analysis

- **$k = C/(MR^2)$.** $\mathrm{kg\,m^2}/(\mathrm{kg\,m^2})$, dimensionless ✓.
  Values lie in $(0, 0.4]$.
- **$C$ from the density integral.** $\mathrm{kg\,m^{-3}}\cdot\mathrm{m^4}\cdot
  \mathrm{m} = \mathrm{kg\,m^2}$ ✓.
- **$\eta = 1/(\mu_0\sigma)$.** $1/(\mathrm{N\,A^{-2}}\cdot\mathrm{S\,m^{-1}})
  = 1/(\mathrm{kg\,m\,s^{-2}A^{-2}}\cdot\mathrm{A^2\,s^3\,kg^{-1}m^{-3}})
  = \mathrm{m^2\,s^{-1}}$ ✓ — a diffusivity, as it must be.
- **$Rm = \mu_0\sigma UL$.**
  $\mathrm{N\,A^{-2}}\cdot\mathrm{A^2\,s^3\,kg^{-1}m^{-3}}\cdot\mathrm{m\,s^{-1}}
  \cdot\mathrm{m} = 1$ ✓.
- **$\tau_\eta = \mu_0\sigma L^2$.** $\mathrm{m^2\,s^{-1}}\cdot\mathrm{m^2}
  = \mathrm{s}$ ✓, since diffusive timescales are $L^2/\eta$.
- **Jeans parameter.** $GMm/(k_BTr)$:
  $\mathrm{m^3\,s^{-2}}\cdot\mathrm{kg}/(\mathrm{J}\cdot\mathrm{m})
  = \mathrm{m^2\,s^{-2}\,kg}/(\mathrm{kg\,m^2\,s^{-2}}) = 1$ ✓.
- **Escape velocity.** $\sqrt{2GM/r}$: $\sqrt{\mathrm{m^2\,s^{-2}}}
  = \mathrm{m\,s^{-1}}$ ✓.
- **Useful anchors.** $R_{\text{gas}}T/g$ in km for an Earth-like $g$ is
  $\approx2.9\,T/1000$; a Jeans parameter of 30 corresponds to $(v_{\text{esc}}/v_{\text{thermal}})^2
  \approx30$, i.e. an escape speed about 5.5 times the thermal speed.

## 8. Python demonstration

[`code/planetary_physics_demo.py`](./code/planetary_physics_demo.py) performs the
two-layer inversion, tabulates $k$, evaluates the dynamo diagnostics, and computes
the Jeans parameters. The blocks below are the script's actual output, **abridged
by omission** where a block would otherwise repeat rows already tabulated above;
every line shown is reproduced verbatim.

```text
  Homogeneous sphere:  C/(M R^2) = 2/5 = 0.400
  Point mass at the centre:        C/(M R^2) -> 0
  Earth (nominal, rounded):        C/(M R^2) = 0.33

    f = 0.5462 (core radius 3480 km / mean radius 6371 km)
    alpha = rho_core / rho_mantle = 3.039
    mean mantle density implied = 4138 kg/m3
    mean core density implied   = 12576 kg/m3
```

```text
     f  alpha=1.0  alpha=1.5  alpha=2.0  alpha=3.0  alpha=4.0
  0.00     0.4000     0.4000     0.4000     0.4000     0.4000
  0.20     0.4000     0.3985     0.3970     0.3940     0.3910
  0.40     0.4000     0.3896     0.3798     0.3619     0.3459
  0.50     0.4000     0.3824     0.3667     0.3400     0.3182
  0.55     0.4000     0.3786     0.3602     0.3303     0.3071
  0.60     0.4000     0.3750     0.3545     0.3228     0.2993
  0.70     0.4000     0.3701     0.3479     0.3170     0.2965
  0.80     0.4000     0.3706     0.3512     0.3271     0.3128
```

```text
  Rm        = 754.0
  tau_eta   = 5.027e+12 s = 1.593e+05 yr
  For comparison, the thermal diffusion time over the same length
  with a nominal thermal diffusivity of 1e-05 m2/s is
    tau_th = 4.000e+17 s = 1.268e+10 yr,
```

```text
species      m (u)   H (km)   v_esc   lambda   kept?
H2           2.016   488.49   10.77     14.1    slow
He           4.003   246.02   10.77     27.9    slow
N2          28.014    35.15   10.77    195.5     yes
O2          31.998    30.78   10.77    223.3     yes
CO2         44.010    22.38   10.77    307.1     yes
```

### What to observe

| Observation | Consequence |
|---|---|
| $k$ = 0.4000 for every $\alpha$ at $f=0$, and for every $f$ at $\alpha=1$ | The two limits are geometric, not physical |
| $\alpha = 3.039$ and $\rho_c = 12\,576$ kg m⁻³ from $M$, $R$, $k$ and $f$ alone | The dense-core inference does not require seismology, only one seismological length |
| The grid's rows turn over beyond $f\approx0.7$ | A very large core displaces mantle outward faster than it concentrates mass |
| $Rm = 754$ against a threshold of tens | The conclusion is robust to a factor-of-two error in every input |
| $\tau_\eta = 1.59\times10^5$ yr against an observed field age of $4.5\times10^9$ yr | The geodynamo must be operating, not decaying |
| $\tau_\kappa = 1.27\times10^{10}$ yr, exceeding the age of the Earth | Conduction alone could not cool the core; convection is required |
| $H$ falls 488 → 22 km from H₂ to CO₂ | Heavy species occupy a thin layer |
| $\lambda$ rises 14.1 → 307.1 over the same sequence | Escape is selective, and the selectivity is proportional to molecular mass |
| $v_{\text{esc}}$ at the exobase is 10.77 km/s | Escape requires a molecule above about 5.5 times the thermal speed |

> **Breaking exercise.** The Earth's $k$ is quoted here as 0.33, and the actual
> value is about 0.3308. Before running anything, predict how much $\alpha$ and
> $\rho_c$ change when the input is 0.3308 instead of 0.33. Then answer the
> question the answer raises: the inversion is *very* sensitive to $k$, so what is
> the dominant uncertainty in the two-layer core density — $k$, $f$, or the
> model? (Hint: differentiate equation (2) with respect to each.) This sensitivity
> is why planetary papers report a *range* of core sizes, and why the honest
> output of the inference loop is a region and not a number.

## 9. Common mistakes

1. **Reading $k$ as a composition indicator.** Self-compression lowers $k$ with no
   compositional change, so a low $k$ means "dense material toward the centre",
   not "iron".
2. **Reporting one interior model when the data admit a family.** The degeneracy
   of §1.3 is not a defect of the method; it is the answer.
3. **Comparing $k$ between bodies of different masses without an equation of
   state.** The larger body's $k$ is lower for the same composition.
4. **Treating $Rm$ as a threshold at exactly 1.** Dynamo action needs $Rm$ of
   order tens; the criterion is a scaling argument, not an equality.
5. **Assuming a body's magnetic field must be dipole-like.** Uranus and Neptune
   demonstrate otherwise, and the geometry is informative.
6. **Inferring a dynamo from remanent magnetization.** Crustal remanence is
   evidence of a *past* dynamo; the two are different claims, and conflating them
   is how the Mars result is most often misstated.
7. **Using the Jeans parameter as a rate.** $\lambda$ is an energy ratio; it
   tells you whether escape is possible, not how fast it is. A full rate needs
   the exobase density and the kinetic flux.
8. **Using the isothermal scale height for a strongly non-isothermal
   thermosphere.** The thermosphere's temperature rises by an order of magnitude
   with height; $H$ is a local quantity there.
9. **Quoting field strengths or core sizes for other bodies without a source.**
   These are mission-derived and revised. Cite the mission.
10. **Forgetting that all these are snapshots.** Thermal evolution changes $k$
    slightly, field strength substantially, and atmospheric composition
    completely over the age of a body.

## 10. Real-world applications

- **Spacecraft mission design.** A moment of inertia, a Love number or a
  libration amplitude each add exactly one constraint, so instrument selection is
  interior-structure design. This is why subsurface radar, gravity gradiometry and
  radio science are standard payload elements.
- **Exoplanet characterisation.** Mass and radius from transit and radial velocity
  are matched against grids of interior models; the output is a probability
  distribution over composition, and the degeneracy of §2.2 is the dominant
  uncertainty.
- **Palaeomagnetism and the history of the geodynamo.** The field's longevity,
  reversals and intensity variations are the observational record the $Rm$ and
  $\tau_\eta$ arguments are tested against.
- **Planetary habitability.** Whether a body retains an atmosphere is set by
  equations (5) and (6), and the same mathematics applied to a planet around
  another star is the "atmospheric escape" problem in exoplanet science.
- **Comparative geodynamics.** Why one body has plate tectonics and another a
  stagnant lid is a question about the convective regime, and the criteria are
  those of lesson [02-06-06](../06-fluid-mechanics/06-mantle-convection.md)
  applied with different parameters.
- **Icy moons and subsurface oceans.** The same induction physics that powers the
  geodynamo is used in reverse: an induced magnetic response to a varying
  external field is the primary evidence for a conducting salty ocean beneath an
  ice shell.

## 11. Further reading

- **Schubert, G., Turcotte, D. L., & Olson, P. *Mantle Convection in the Earth
  and Planets* (Cambridge University Press, 2001).** The comparative-geodynamics
  reference, including the moment-of-inertia and Darwin–Radau machinery of §1.
  Level: graduate.
- **Merrill, R. T., McElhinny, M. W., & McFadden, P. L. *The Magnetic Field of
  the Earth: Paleomagnetism, the Core and the Deep Mantle* (Academic Press,
  1998).** The palaeomagnetic evidence and the dynamo framework of §3. Level:
  graduate.
- **Roberts, P. H., & King, E. M. (2013).** "On the genesis of the Earth's
  magnetism." *Reports on Progress in Physics* **76**, 096801. A modern review of
  the dynamo criteria and the parameters that enter them.
- **Stevenson, D. J.** "Interior structure of the giant planets" and related
  reviews in *Annual Review of Earth and Planetary Sciences*. The equations of
  state of planetary interiors beyond rock and iron.
- **Catling, D. C., & Kasting, J. F. *Atmospheric Evolution on Inhabited and
  Lifeless Worlds* (Cambridge University Press, 2017).** Atmospheric escape in
  full, including the non-thermal mechanisms that §4.2 sets aside.
- **Lissauer, J. J., & de Pater, I. *Fundamental Planetary Science* (Cambridge
  University Press, 2013).** The observational basis for every qualitative
  statement in §3.4 and §4.3, with current numbers and their sources.
- **Valencia, D., et al.** Papers on the mass–radius–composition relation for
  small exoplanets, which is the direct descendant of the inference loop of §2.
  Search current literature rather than relying on any single reference here.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.
> For planetary field strengths, core sizes and atmospheric inventories, use the
> current NASA and ESA mission archives rather than any secondary source,
> including this one.

## 12. Related lessons

- [01 Pressure, Density and Gravity Inside the Earth](./01-pressure-density-depth.md)
  — the Earth as the worked example, including the moment-of-inertia computation.
- [02 Equations of State and High-Pressure Mineral Physics](./02-equations-of-state.md)
  — the equation of state that the inference loop of §2 assumes.
- [03 Seismic Velocities, Elastic Moduli and Mineralogy](./03-seismic-parameter-relations.md)
  — the composition inference that is available for the Earth and unavailable
  elsewhere.
- [04 Atmospheric Structure](./04-atmospheric-structure.md) — the scale height
  and hydrostatic balance underlying §4.
- [02-07-04 Faraday's Law and Induction](../07-electromagnetism/04-em-induction.md)
  — the induction equation of §3.1.
- [02-06-06 Mantle Convection](../06-fluid-mechanics/06-mantle-convection.md)
  — the convection criterion that the dynamo and the heat flow share.
- [12-global-geophysics-interior/07 Planetary Interiors](../../12-global-geophysics-interior/07-planetary-interiors-comparative/01-terrestrial-planets-interiors.md)
  — the observational detail this lesson deliberately omits.
- [12-global-geophysics-interior/04-02 The Geodynamo](../../12-global-geophysics-interior/04-geomagnetism-and-core/02-geodynamo-numerical.md)
  — dynamo modelling in full.

Exercises:
[`exercises/05-planetary-physics-exercises.md`](./exercises/05-planetary-physics-exercises.md)
and
[`exercises/05-planetary-physics-solutions.md`](./exercises/05-planetary-physics-solutions.md).

## Self-assessment checklist

- [ ] I can derive $k = 0.4$ for a homogeneous sphere and $k\to0$ for a point
      mass. (§1.1)
- [ ] I can derive the two-layer formula (2) and invert it for $\alpha$. (§1.2)
- [ ] I can explain why $k$ alone leaves $(f,\alpha)$ on a curve, and name three
      measurements that break the degeneracy. (§1.3–§1.4)
- [ ] I can state why $k$ is not an iron-content indicator. (§1.4, §5)
- [ ] I can write the induction equation and identify the two terms. (§3.1)
- [ ] I can compute $Rm$, $\tau_\eta$ and $\tau_\kappa$ and compare the last with
      the age of the Earth. (§3.1–§3.3)
- [ ] I can name the three dynamo ingredients and account for the observed
      pattern of planetary fields. (§3.4)
- [ ] I can derive the Jeans parameter from the energy balance and evaluate it
      for two species. (§4.2)
- [ ] I can explain selective escape from the $m$-dependence of $H$ and
      $\lambda$. (§4.2–§4.3)
- [ ] I can state the mass–radius degeneracy and why mission design is
      interior-structure design. (§2.2)
