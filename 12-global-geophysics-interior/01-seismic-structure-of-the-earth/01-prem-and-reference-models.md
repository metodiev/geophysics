---
id: 12-01-01
title: "PREM, IASP91 and Reference Earth Models"
level: graduate
prereqs: ["06-02-02", "02-11-01", "02-11-03", "02-04-05"]
tags: [global-geophysics, earth-interior, reference-models, prem, iasp91, travel-times, radial-structure]
---

# PREM, IASP91 and Reference Earth Models

> **All models and data in this module are SYNTHETIC.** The radial velocity and
> density profile used throughout this lesson is a teaching model chosen by us.
> It is *not* PREM, *not* IASP91, and no number in the tables below is a
> published measurement. Names such as "Moho at 24.4 km" or "CMB at 2891 km" are
> used as **conventional interface labels**, in the same way a map uses named
> towns: they tell you where to look, not what we measured.

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** what a reference Earth model is a model *of*, and state which
   quantities it takes as fixed inputs rather than predictions.
2. **Describe** the layered parametrisation of a radial model and name the
   conventional interfaces that organise it.
3. **Derive** the spherical-Earth ray integrals for $\Delta(p)$ and $T(p)$ from
   the conservation of $U = r\sin i / v$, and **verify** them against a
   homogeneous sphere where both have closed forms.
4. **Compute** vertical travel times, a travel-time branch, the core-grazing
   limit and the shadow gap of a given model, reporting each with units.
5. **Check** the internal consistency relation $\mathrm{d}T/\mathrm{d}\Delta = p$
   and **quantify** the finite-difference error of that check.
6. **Compute** the mass and moment of inertia of a radial density profile, and
   **explain** what $C/MR^2$ alone can and cannot constrain.
7. **State** the non-uniqueness of the model: why a travel-time curve constrains
   integrals of slowness rather than velocities, and what else is needed.

## Prerequisites

- [06-02-02 Snell's Law, Layered Media and the Travel-Time Curve](../../06-seismology/02-ray-theory-and-travel-times/02-snell-and-layering.md) —
  the ray parameter as a conserved quantity in a stack of layers.
- [02-11-01 Pressure, Density and Gravity Inside the Earth](../../02-physics/11-physics-of-earths-interior-and-atmosphere/01-pressure-density-depth.md) —
  how pressure and gravity vary with radius.
- [02-11-03 Seismic Velocities, Elastic Moduli and Mineralogy](../../02-physics/11-physics-of-earths-interior-and-atmosphere/03-seismic-parameter-relations.md) —
  where $v_p$ and $v_s$ come from in terms of $K$, $G$ and $\rho$.
- [02-04-05 Elastodynamic Equation of Motion and Wave Speeds](../../02-physics/04-elasticity-and-continuum-mechanics/05-elastodynamics.md) —
  the wave equation whose speeds a reference model stores.

## 1. What a reference Earth model is

A **reference Earth model** is a one-dimensional (radially symmetric) table of
$v_p(r)$, $v_s(r)$ and $\rho(r)$ that is intended to represent the *average*
Earth, together with the interface depths at which those functions jump. Its
purpose is not to describe any particular place. It is to provide:

- a **travel-time baseline**: predicted arrival times as a function of distance,
  against which real arrivals are compared;
- a **depth baseline**: the reference frame in which a tomographic anomaly of
  $+1\,\%$ or a discontinuity displaced by $-10\ \mathrm{km}$ means something;
- a **boundary-condition set** for normal-mode, geodetic and geodynamic
  calculations that need a plausible starting Earth.

Three things follow immediately from that definition, and they organise this
whole module.

**First, a reference model is a *model*, so it is built by fitting.** The
functions $v_p$, $v_s$, $\rho$ are not measured continuously with depth; they are
constrained by finite collections of observables (travel times, dispersion
curves, free-oscillation periods, the mass and the moment of inertia) and the
"model" is a smooth parametrisation chosen to fit them. The parametrisation is
part of the model.

**Second, velocities can be measured where density cannot.** Seismic waves give
$v_p$ and $v_s$ directly. Density is far harder, and it is usually obtained by
imposing an additional physical assumption — most often that the mantle is in
hydrostatic equilibrium under self-gravitation, which turns $v_p$, $v_s$ and the
Adams–Williamson relation into a differential equation for $\rho$. A reference
model's density profile is therefore *more model-dependent* than its velocity
profiles, and this is worth saying out loud whenever a density is used in an
argument.

**Third, a reference model is not unique.** Many different profiles reproduce the
same travel times within their uncertainties. Any statement of the form "the
velocity at 2000 km depth is $x$" is really "within the family of models
consistent with these data, $x$ is a good summary". Lesson
[04 Lower-Mantle Heterogeneity and LLSVPs](04-lower-mantle-heterogeneity.md)
shows what happens when you try to test that statement locally.

### 1.1 Two conventions you will see immediately

- **Radius or depth.** Functions may be tabulated against radius $r$ (0 at the
  centre) or depth $z = R - r$ (0 at the surface). The two are related by the
  Earth radius. We use the standard mean Earth radius $R = 6371\ \mathrm{km}$.
- **Layer boundaries are *named*, and the names are used as shorthand for a
  depth.** "The 410" means the discontinuity conventionally placed at about
  410 km depth; "the CMB" means the core–mantle boundary, conventionally at
  2891 km depth, i.e. radius $3480\ \mathrm{km}$. These are labels. This lesson's
  model uses them, with the numerical values quoted as conventions rather than
  as measured results.

## 2. The layered parametrisation

The model used in the demonstration is piecewise linear in depth. Within each
layer the velocity and density interpolate linearly between the top and bottom
values:

$$v(r) = v_{\text{top}} + \frac{r_{\text{top}} - r}{r_{\text{top}} - r_{\text{bot}}}
\left(v_{\text{bot}} - v_{\text{top}}\right),$$

so that a layer is specified by five numbers per elastic property. The chosen
(SYNTHETIC) profile is:

| depth range (km) | $v_p$ (km s$^{-1}$) | $v_s$ (km s$^{-1}$) | $\rho$ (g cm$^{-3}$) |
|---|---|---|---|
| 0 – 24.4 | 5.80 → 6.50 | 3.20 → 3.70 | 2.60 → 2.90 |
| 24.4 – 180 | 8.10 → 8.10 | 4.49 → 4.45 | 3.38 → 3.36 |
| 180 – 400 | 8.08 → 8.55 | 4.42 → 4.66 | 3.35 → 3.54 |
| 400 – 670 | 8.90 → 10.15 | 4.80 → 5.55 | 3.65 → 3.99 |
| 670 – 2891 | 10.75 → 13.72 | 5.85 → 7.26 | 4.01 → 5.57 |
| 2891 – 5149.5 | 8.06 → 10.29 | 0 | 9.90 → 12.17 |
| 5149.5 – 6371 | 11.03 → 11.26 | 3.50 → 3.67 | 12.76 → 13.09 |

The features that make this look like an Earth, and that any model of this kind
must reproduce, are:

- a thin, slow **crust** above a faster **lid** (the Moho step at 24.4 km);
- a **low-velocity zone** between roughly 180 and 400 km where $v_s$ *decreases*
  downwards;
- a **transition zone** between 400 and 670 km in which both velocities increase
  quickly, bounded by two jumps;
- a **lower mantle** in which velocities and density rise smoothly;
- a first-order **drop** in $v_p$ and a **loss of $v_s$** at the CMB: the outer
  core cannot support shear, so a fluid outer core is a conclusion drawn from
  seismology, not an assumption;
- a **jump up** again at the ICB, which is the core's own evidence that the inner
  core is solid.

The last two bullets are the important ones conceptually. A layered model is not
a smooth guess: it is a statement about *where the functions jump*, and each jump
is a physical claim.

## 3. From the velocity profile to travel times

### 3.1 The conserved quantity

In a spherically symmetric Earth, Snell's law in the form

$$U(r) \equiv \frac{r \sin i(r)}{v(r)} = \text{constant} \equiv p$$

holds along a ray, where $i$ is the angle between the ray and the **vertical**
(radial) direction. The conserved $p$ is the **ray parameter**. Note its units
carefully: $r$ has units of km and $v$ of km s$^{-1}$, so $p$ has units of
**seconds per radian**, not s km$^{-1}$. In a flat-layered Earth the conserved
quantity is $\sin i / v$ with units s km$^{-1}$; in a sphere it is the
radius-weighted version. Mixing the two conventions is a classic error, so we
will always convert explicitly:

$$p_{\mathrm{s\,deg^{-1}}} = \frac{p_{\mathrm{s\,rad^{-1}}}}{57.2958}.$$

### 3.2 The turning point

Along a ray $U(r)$ decreases as $r$ decreases (for a monotonically increasing
$v(r)$ it decreases faster than $r$). The ray can penetrate until
$U(r_{tp}) = p$, i.e. until $\sin i = 1$ and the ray becomes horizontal at the
**turning radius** $r_{tp}$. Below that radius no real angle $i$ exists: the
solution is evanescent. Setting $U(r_{tp}) = p$ is the equation that defines the
ray's deepest point.

### 3.3 The integrals

Summing the horizontal and vertical legs of a ray that turns at $r_{tp}$ and
returns to the surface gives the standard pair

$$\boxed{\;\Delta(p) = 2p\int_{r_{tp}}^{R} \frac{\mathrm{d}r}
{r\sqrt{U^2(r) - p^2}},\qquad
T(p) = 2\int_{r_{tp}}^{R} \frac{\left(r/v^2(r)\right)\mathrm{d}r}
{\sqrt{U^2(r) - p^2}}.\;}$$

The dimensions check: $p\,\mathrm{d}r/(r\sqrt{U^2-p^2})$ is
$(\mathrm{s})(\mathrm{km})/(\mathrm{km}\cdot\mathrm{s})$, i.e. radians. The time
kernel is $(\mathrm{km}\,\mathrm{s}^2\mathrm{km}^{-2})(\mathrm{km})/\mathrm{s}
= \mathrm{s}$. The product $r/v^2$ is the *slowness-weighted* radius whose
integral produces a time, while the $2p/(r)$ factor produces an angle. Nothing
else can be dimensionally right, which is why the same two integrands reappear in
every spherically symmetric travel-time code.

For a ray that crosses a first-order discontinuity, the integral is split at the
discontinuity and the **local** velocity is used in each shell:
$\Delta = 2\left[\int_{\text{mantle}} + \int_{\text{core}}\right]$, with $U=r/v_p$
in the mantle above the CMB and $U = r/v_p$ with the core's own $v_p$ below it.
The ray parameter itself does not change across the boundary — that is the
content of the conserved $U$ — and that is exactly why a ray can be *refracted
into* a slow outer core rather than reflected off it.

### 3.4 The slowness identity

Because $T$ is a function of $\Delta$ along a branch, and because the two
integrals above are both functions of the same single parameter $p$, the branch
satisfies

$$\frac{\mathrm{d}T}{\mathrm{d}\Delta} = p,$$

with $\Delta$ in radians. This is the differential form of the fact that $\tau(p)
= T - p\Delta$ is stationary. It is the single most useful internal check a
travel-time calculation can have, and the demonstration measures it numerically.

## 4. What the model predicts

### 4.1 Vertical travel times

Setting $p = 0$ removes the horizontal leg, and the integrals collapse to a pure
radial integral:

$$T_\text{vert} = \int_{r_1}^{r_2} \frac{\mathrm{d}r}{v(r)}.$$

The demonstration integrates the SYNTHETIC profile and prints:

| path | $T_\text{vert}$ (s) | effective $v$ (km s$^{-1}$) |
|---|---|---|
| surface → CMB (2891.0 km of mantle) | 260.486 | 11.0985 |
| surface → ICB (5149.5 km) | 507.818 | 10.1404 |
| surface → centre (6371 km) | 617.471 | 10.3179 |
| centre → ICB (1221.5 km, inner core only) | 109.559 | 11.1492 |

The "effective velocity" is just distance divided by time. It is a **harmonic
mean**, not an arithmetic mean: $T = \int \mathrm{d}r/v$ weights slow material
more heavily than fast material. Any hand-estimate that averages $v_p$
arithmetically on this path will come out *too fast*, and therefore give a
travel time that is too short.

### 4.2 A travel-time branch

Sampling turning radii from the surface downwards gives the P branch. Selected
rows from the demonstration (thinning out the deep end where the branch
flattens):

| $r_{tp}$ (km) | $p$ (s rad$^{-1}$) | $p$ (s deg$^{-1}$) | $\Delta$ (deg) | $T$ (s) |
|---|---|---|---|---|
| 6100 | 737.213 | 12.8668 | 21.615 | 299.43 |
| 5800 | 598.452 | 10.4450 | 23.605 | 319.13 |
| 5100 | 441.418 | 7.7042 | 52.286 | 564.76 |
| 4200 | 329.226 | 5.7461 | 75.249 | 719.44 |
| 3700 | 275.589 | 4.8099 | 86.404 | 778.27 |
| 3481 | 253.742 | 4.4286 | 91.158 | 800.22 |

Two features are worth staring at. Between $r_{tp} = 6100$ and 5800 km the
distance *scarcely grows* (21.6° → 23.6°) while the time grows by 20 s: that is
the low-velocity zone, which traps rays and packs them into a small distance
range. At the deep end, the branch **terminates** at the core-grazing ray
($p = 253.742\ \mathrm{s\,rad^{-1}}$, $\Delta = 91.158°$ in this model) because no
mantle ray can turn below the CMB.

### 4.3 The shadow gap and the core branches

Rays with $p$ smaller than $U$ at the bottom of the mantle penetrate the core.
The demonstration scans them and finds:

| branch | turning in | $\Delta$ range (deg) | comment |
|---|---|---|---|
| mantle P | mantle | up to 91.16 | ends at the core-grazing ray |
| outer-core branch | outer core | 144.00 – 148.72 | **folds**: the caustic is at 144.00° |
| inner-core branch | inner core | 112.13 – 177.52 | reaches inward to 112.13° |

The outer-core branch is a fold of the travel-time curve: $\Delta$ passes through
a minimum (here 144.00° at $r_{tp} = 1781\ \mathrm{km}$) and then increases again,
so two different rays with different times arrive at the same distance. That fold
is the **caustic**, and it is why amplitudes concentrate and then vanish near it.

Between the end of the mantle branch and the inward end of the inner-core branch
there is a range of $p$ — from $U$ just above the ICB in the outer core
(118.71 s rad$^{-1}$) up to $U$ at the bottom of the mantle
(253.742 s rad$^{-1}$) — for which **no ray turns anywhere in the model**. Their
epicentral distances fill the gap from 91.2° to 112.1°. This is the model's
**P shadow zone**. The classical observed limits for the real Earth are about
103° and 143°; the difference is a property of the core radius and gradients
chosen here, so the model demonstrates the *mechanism* and not the numbers. In
particular, the real P shadow is not "empty": weak core-penetrating arrivals
exist within it, which is precisely how the inner core was detected.

## 5. Two independent checks

A travel-time calculation that has not been checked is a plot, not a result. The
demonstration performs two checks that cost four lines of code each.

### 5.1 A homogeneous sphere

For constant $v$ the rays are straight chords and the integrals have closed
forms. With turning radius $r_{tp}$ in a sphere of radius $R$:

$$\Delta = 2\arccos\!\left(\frac{r_{tp}}{R}\right),\qquad
T = \frac{2\sqrt{R^2 - r_{tp}^2}}{v}.$$

Numerically integrating the general formulae instead, with $v = 8.00\
\mathrm{km\,s^{-1}}$ and $r_{tp} = 3000\ \mathrm{km}$:

| quantity | analytic | numerical | relative error |
|---|---|---|---|
| $\Delta$ | 123.816652° | 123.816652° | $2.1\times10^{-11}$ |
| $T$ | 1405.116565 s | 1405.116565 s | $1.2\times10^{-11}$ |

Agreement at the $10^{-11}$ level means the quadrature and the singularity
treatment (the substitution $r = r_{tp} + s^2$) are both correct. If the same
code gives agreement only to $10^{-4}$, the fault is in the quadrature, not in
the physics.

### 5.2 The slowness identity

Comparing the finite-difference slope of the branch with the mean ray parameter
over the same interval:

| interval (deg) | measured $\mathrm{d}T/\mathrm{d}\Delta$ (s deg$^{-1}$) | mean $p$ (s deg$^{-1}$) | error |
|---|---|---|---|
| 37.69 → 52.29 | 8.2386 | 8.2080 | +0.37 % |
| 75.25 → 82.01 | 5.4582 | 5.4595 | −0.02 % |
| 86.40 → 89.67 | 4.6780 | 4.6785 | −0.01 % |

The residual is not physics: over a finite interval the measured slope
approximates $\bar{p}$, and the curvature of $T(\Delta)$ makes the approximation
second-order accurate at best. The large-interval row shows the largest error
(+0.37 %) exactly as expected.

## 6. Mass, moment of inertia, and what geodesy constrains

The same density profile gives two more numbers, both computable from the 1-D
model:

$$M = \int_0^R 4\pi r^2 \rho(r)\,\mathrm{d}r, \qquad
C = \int_0^R \frac{8}{3}\pi r^4 \rho(r)\,\mathrm{d}r .$$

The second integral is the polar moment of inertia of a spherical shell; the
factor $8\pi/3$ comes from integrating $\rho\,(r\sin\theta)^2$ over the sphere.
The demonstration reports

| quantity | value |
|---|---|
| model mass $M$ | $5.7904\times10^{24}$ kg (ratio 0.9696 to the standard 5.9722×10²⁴ kg) |
| model $C$ | $7.7479\times10^{37}$ kg m² |
| model $C/MR^2$ | 0.3297 |

The exact reference is a **uniform** sphere: $C/MR^2 = 2/5 = 0.4$ for any
density, uniformly distributed. Since this model concentrates mass towards the
centre, its value must be *below* 0.4, and it is. The value conventionally
adopted for the Earth is $C/MR^2 = 0.3307$; the model lands within 0.4 % of it
because it was built to mimic that shape — which is a warning about
"agreement", not evidence of anything.

The useful exercise is the reverse direction. Consider the simplest possible
Earth: a uniform core of density $\rho_c$ and radius $a = qR$, plus a uniform
mantle of density $\rho_m$. Then

$$\frac{C}{MR^2} = \frac{2}{5}\,
\frac{\rho_c q^5 + \rho_m (1-q^5)}{\rho_c q^3 + \rho_m (1-q^3)},$$

because $M \propto \rho_c q^3 + \rho_m(1-q^3)$ and $C \propto \rho_c q^5 +
\rho_m(1-q^5)$ with the same prefactors up to $R^3$ and $R^5$. With
$\rho_c = 10.50$, $\rho_m = 4.90\ \mathrm{g\,cm^{-3}}$ and $q = 3480/6371 =
0.5462$, the demonstration evaluates this to **0.3559** — still far above 0.3307.
Sweeping $q$ over the whole interval $0 < q < 1$, the smallest ratio any such
two-layer Earth can reach is **0.3424**, at $q = 0.7166$ (a core of radius
4566 km). No choice of a two-layer structure with these densities can reproduce
0.3307.

That is a real constraint, obtained from a number that geodesy can measure to
high precision: **the density must increase with depth within the mantle or the
core** (or both). Seismology says where the jumps are; $C/MR^2$ says that smooth
uniform layers are not enough. Neither statement alone determines the profile,
and that is the honest summary of what a reference model is.

## 7. Non-uniqueness: what the travel times do not fix

A travel-time curve is one number per distance, and each number is an integral of
slowness along a path. The map from a velocity profile to a travel-time curve is
therefore **many-to-one**, for three distinct reasons:

1. **Null-space directions.** A perturbation $\delta v(r)$ that leaves
   $\int \delta u\,\mathrm{d}s$ unchanged along every ray is invisible. In
   practice these are oscillatory perturbations whose depth scale is smaller than
   the ray spacing, plus the classical depth–velocity trade-off: pushing a
   discontinuity deeper and making the material above it faster can leave
   $\Delta(p)$ unchanged while changing $T(p)$ by less than typical picking
   errors.
2. **Discretisation choice.** The number of layers is chosen by the analyst, and
   a 30-layer model and a 200-layer model fitted to the same data will disagree
   in the layers, however closely they agree in travel time.
3. **Data coverage.** Rays sample some depths and distances densely and others
   barely. The shadow gap of Section 4.3 is a coverage hole: nothing samples the
   core's top region on the direct P branch, and the core-penetrating phases that
   do are weak and arrive late.

Later lessons in this module attack all three: [02](02-crustal-structure.md) asks
what local crustal structure does to a global model, [03](03-upper-mantle-discontinuities.md)
uses the *slopes* of discontinuities as an independent constraint,
[04](04-lower-mantle-heterogeneity.md) replaces the 1-D assumption with a
damped inverse problem and studies its resolution, and
[05](05-core-mantle-boundary.md) and [06](06-outer-and-inner-core.md) work in the
region where the data are weakest and the models most contested.

## 8. Assumptions and regime of validity

Everything in this lesson rests on the following, and each one has an identifiable
failure mode:

1. **Spherical symmetry.** Velocities depend on $r$ alone. Failure mode: 3-D
   structure (lesson 04) perturbs arrivals by up to several seconds, which is the
   same size as the signals we interpret.
2. **Isotropy.** One $v$ per phase per radius. Failure mode: mantle anisotropy of
   a few per cent changes travel times measurably along different azimuths
   (lessons 03 and 06).
3. **Perfect elasticity at seismic frequencies.** No attenuation, so the
   travel-time integrals are real. Failure mode: attenuation makes velocities
   frequency-dependent (physical dispersion), so "the" velocity is a
   band-limited quantity; the effect is small but systematic.
4. **Geometric (ray) theory.** The integrals assume an infinitely thin ray.
   Validity requires the structure to vary slowly over a wavelength; near a
   caustic (Section 4.3) ray amplitudes are unbounded and the method fails
   qualitatively, not just quantitatively.
5. **First-order interfaces.** Jumps in the table are treated as true
   discontinuities. Failure mode: a real transition over tens of km changes both
   amplitudes and apparent depths.
6. **Hydrostatic equilibrium** if the density is derived rather than fitted. A
   large part of the lower mantle may not be in hydrostatic equilibrium at the
   precision claimed.
7. **Small $p$ expansion.** Not used here, but any quick estimate of the form
   $\Delta t \approx \ldots$ has a regime of validity, usually
   $p \lesssim 0.08\ \mathrm{s\,km^{-1}}$.

## 9. Worked examples

### Example 1 — the vertical time as an effective velocity

The demonstration gives $T_\text{vert} = 260.486\ \mathrm{s}$ from the surface to
the CMB over 2891.0 km. The implied effective velocity is

$$v_\text{eff} = \frac{2891.0}{260.486} = 11.0985\ \mathrm{km\,s^{-1}}.$$

A colleague estimates instead by arithmetic mean, noting that $v_p$ rises from
10.75 to 13.72 km s$^{-1}$ across the lower mantle and using a midpoint value
$11.4\ \mathrm{km\,s^{-1}}$ for the 2221 km of lower mantle plus the transition
zone. Their time is $\approx 2891/11.4 = 253.6\ \mathrm{s}$, some **7 s too
short**. The reason is structural, not arithmetic: $1/v$ is what integrates, and
the slow upper mantle occupies a large fraction of the path. Always take the
harmonic mean when a path average is needed.

### Example 2 — the core-grazing ray parameter

At the bottom of the mantle the model has $v_p = 13.72\ \mathrm{km\,s^{-1}}$ at
$r = 3480\ \mathrm{km}$. The largest ray parameter that just fails to enter the
core is

$$p = \frac{U(r_\text{CMB})}{1} = \frac{3480}{13.72}
= 253.64\ \mathrm{s\,rad^{-1}} = 4.4266\ \mathrm{s\,deg^{-1}},$$

where the conversion uses $1\ \mathrm{rad} = 57.2958°$. The demonstration, which
evaluates the profile 1 km above the interface, obtains
$253.742\ \mathrm{s\,rad^{-1}}$; the difference (0.04 %) is the velocity gradient
over that kilometre and is a useful reminder that "the velocity at the CMB" is
ambiguous by construction.

A ray with $p = 4.43\ \mathrm{s\,deg^{-1}}$ therefore grazes the core, and the
whole mantle P branch lives at $p \ge 4.43$. Rays with $4.43 > p >
U_\text{ICB}$ cannot turn at all (Section 4.3), which is why the P shadow exists.

### Example 3 — a two-layer moment of inertia

Take a uniform mantle with $\rho_m = 4.90$ and a uniform core with
$\rho_c = 10.50\ \mathrm{g\,cm^{-3}}$, with $q = a/R = 0.5462$. Then

$$q^3 = 0.16297,\quad q^5 = 0.04862,$$
$$\rho_c q^3 + \rho_m(1-q^3) = 1.71120 + 4.10149 = 5.81269,$$
$$\rho_c q^5 + \rho_m(1-q^5) = 0.51051 + 4.66176 = 5.17227,$$
$$\frac{C}{MR^2} = \frac{2}{5}\cdot\frac{5.17227}{5.81269}
= 0.4 \times 0.88983 = 0.35593.$$

This is 7.7 % above the conventional 0.3307, and — as Section 6 shows — no
two-layer model with these densities gets closer than 0.3424. The data therefore
demand radial structure *within* a layer, not merely a subdivision into layers.

### Example 4 — reading a travel-time table like a slowness measurement

From the branch table, $T = 660.97\ \mathrm{s}$ at $\Delta = 65.753°$ and
$T = 719.44\ \mathrm{s}$ at $\Delta = 75.249°$. The average slowness is

$$\frac{719.44 - 660.97}{75.249 - 65.753} = \frac{58.47}{9.496}
= 6.157\ \mathrm{s\,deg^{-1}},$$

which should lie between the endpoint ray parameters $6.5687$ and
$5.7461\ \mathrm{s\,deg^{-1}}$; it does, and it is within 0.4 % of their mean
$6.1574$. This is the slowness identity used as a *measurement*: the local slope
of a travel-time curve is a direct measurement of the ray parameter, and hence of
$r/v$ at the turning depth. Every 1-D velocity inversion is a formalisation of
this observation.

## 10. Python demonstration

`code/prem_and_reference_models_demo.py` performs the whole calculation with
numpy only. It:

1. builds the SYNTHETIC profile and prints the layer table;
2. integrates the vertical travel time over the mantle and the whole Earth;
3. **validates** the ray integrals against a homogeneous sphere, where $\Delta$
   and $T$ are known in closed form (agreement to $2.1\times10^{-11}$);
4. scans the mantle P branch, printing $p$, $\Delta$, $T$ and the measured
   $\mathrm{d}T/\mathrm{d}\Delta$, and checks the slowness identity;
5. scans the core branches, locating the fold of the outer-core branch (caustic
   at 144.00°) and the inward end of the inner-core branch (112.13°);
6. integrates the density profile for $M$ and $C$, evaluates the closed-form
   two-layer $C/MR^2$, and shows that no two-layer model reaches the conventional
   value.

Run it with

```bash
cd 12-global-geophysics-interior/01-seismic-structure-of-the-earth/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python prem_and_reference_models_demo.py
```

It prints labelled results with units, uses the fixed seed
`np.random.default_rng(20261014)`, needs no network, and takes under a second.

## 11. Exercises

Full sets with worked solutions are in
[`exercises/01-prem-and-reference-models-exercises.md`](exercises/01-prem-and-reference-models-exercises.md)
and
[`exercises/01-prem-and-reference-models-solutions.md`](exercises/01-prem-and-reference-models-solutions.md).

- **★** Convert $p$ between s km$^{-1}$, s rad$^{-1}$ and s deg$^{-1}$; state the
  regime in which the spherical and flat forms coincide.
- **★★** Reproduce the homogeneous-sphere check by hand for one ray.
- **★★** Use the branch table to estimate the depth of the 410 and 670 jumps.
- **★★★** Derive the null-space direction of a two-layer perturbation that leaves
  $T(\Delta)$ unchanged to first order, and quantify it.

## Mastery checkpoint

Without notes, and showing your arithmetic:

> A reference model has a discontinuity at 24.4 km depth where $v_p$ steps from
> 6.50 to 8.10 km s$^{-1}$, and a mean Earth radius of 6371 km.
> **(a)** Compute the ray parameter (in s rad$^{-1}$ and s deg$^{-1}$) of the ray
> that turns exactly at that interface.
> **(b)** A station at $\Delta = 60°$ records a first arrival 1.5 s earlier than
> the model predicts. State two *different* modifications of the model that would
> explain the residual, and say which of them the travel time of a single station
> cannot distinguish.
> **(c)** Compute the vertical travel time through a 24.4 km crust of uniform
> $v_p = 6.20\ \mathrm{km\,s^{-1}}$ and explain why the answer is not simply
> $24.4/6.20$ for a real crust.
> **(d)** State one observable, other than a travel time, that would break the
> ambiguity in (b).

A worked version of (a) and (c) appears in the lesson-01
[solutions](exercises/01-prem-and-reference-models-solutions.md).

## Common pitfalls

1. **Mixing the flat and spherical ray parameters.** $p$ in s km$^{-1}$ is
   $\sin i/v$; $p$ in s rad$^{-1}$ is $r\sin i/v$. In this lesson the second is
   used throughout, and the conversion factor is 57.2958.
2. **Reading the layer table as a measurement.** A table of numbers with units is
   not evidence. Attributing a value to "the Earth" because it is in a model's
   table is the single most common overclaim in this subject.
3. **Taking an arithmetic mean where a harmonic mean is required.** Section 9,
   Example 1, quantifies the error at 7 s on a 260 s path.
4. **Treating the shadow zone as empty.** It is empty of rays with turning points
   in this model, not of arrivals. Weak core-penetrating phases travel into it.
5. **Forgetting that density is the soft part.** Velocities come from seismic
   observations; density typically comes from an equilibrium assumption. A
   density disagreement is therefore a test of the assumption first.
6. **Comparing a model to itself.** The model in this lesson "agrees" with the
   conventional $C/MR^2$ because it was constructed to mimic that shape. Agreement
   obtained by construction is not a validation; the homogeneous-sphere
   comparison in Section 5.1 is, because the analytic answer was never an input.

## 13. Related modules

- [02 Crustal Structure and Continental vs Oceanic Crust](02-crustal-structure.md) —
  the top 40 km, where the 1-D assumption fails hardest.
- [03 Upper-Mantle Discontinuities at 410 and 660 km](03-upper-mantle-discontinuities.md) —
  using the *depth* of the interfaces as a thermometer.
- [04 Lower-Mantle Heterogeneity and LLSVPs](04-lower-mantle-heterogeneity.md) —
  what damped inversion of the same data really recovers.
- [05 Core-Mantle Boundary: ULVZ, D'' and Post-Perovskite](05-core-mantle-boundary.md)
  and [06 Outer Core, Inner Core Anisotropy and Rotation](06-outer-and-inner-core.md) —
  the deep branches and their caustics.
- [Module 02 Composition and Mineral Physics](../02-composition-and-mineral-physics/README.md) —
  whether the profile is mineralogically possible.
- [06-06-06 Global Mantle Tomography and Its Geodynamic Interpretation](../../06-seismology/06-seismic-tomography/06-global-mantle-tomography.md) —
  the same data used to look sideways instead of downwards.
- [07-05-03 Spherical Harmonic Solutions and Coefficient Interpretation](../../07-gravity-geodesy/05-satellite-gravimetry/03-spherical-harmonic-solutions.md) —
  $C_{20}$ and the figure of the Earth as an independent radial constraint.

## Self-assessment checklist

- [ ] I can state what a reference Earth model is for and what it is not.
- [ ] I can convert between the flat and spherical ray parameters and give the
      units of each.
- [ ] I can write the two ray integrals from memory and check them dimensionally.
- [ ] I can explain what the turning radius is and why the branch terminates at
      the core-grazing ray.
- [ ] I can validate a travel-time code against a homogeneous sphere.
- [ ] I can say what the measured $\mathrm{d}T/\mathrm{d}\Delta$ is equal to, and
      why the finite-difference version is only second-order accurate.
- [ ] I can compute $C/MR^2$ for a two-layer model and say what its value forbids.
- [ ] I can name three distinct reasons a travel-time curve does not determine a
      velocity profile.
