---
id: 02-11-01
title: "Pressure, Density and Gravity Inside the Earth"
level: advanced
prereqs: ["02-06-01", "02-08-01", "01-06-04"]
estimated_minutes: 90
tags: [hydrostatic-equilibrium, prem, core-mantle-boundary, adams-williamson]
---

# Pressure, Density and Gravity Inside the Earth

The Earth's centre is 6371 km below your feet, at about 360 GPa and a few
thousand kelvin, and nobody has been there. Everything this lesson states about
it is an inference from two things that *are* measured at the surface: the mass
(to about five significant figures, through $GM_\oplus$) and the moment of
inertia. Everything else follows from one equation of physics and one assumption
about how the interior is arranged.

The equation is hydrostatic balance,

$$\frac{\mathrm{d}P}{\mathrm{d}r} = -\rho(r)\,g(r),$$

and the assumption is that the interior is spherically symmetric and close
enough to hydrostatic equilibrium that no shell of it is accelerating
appreciably. Those two statements, integrated over a density profile, generate
the pressure, gravity and density profiles of the whole planet — and they also
generate a *test*: if the density profile you assume implies the right mass and
the right moment of inertia, and if the resulting seismic velocities match the
ones observed, then the profile is admissible. That test is the entire method of
deep-Earth geophysics, and this lesson is its worked example.

Two warnings before starting, because they govern every number below.

**First, the numbers are model output, not measurements.** The densities used
here are the rounded characteristic values tabulated in
[26-02-03 Physical Constants and Earth Parameters](../../26-reference-library/02-symbols-and-units/03-constant-handbook.md)
§3.3. They are nominal anchors for a reference model. They are not samples, they
carry no uncertainty statement in the usual sense, and the precise values at a
specific depth require the reference model itself. The primary description of the
Preliminary Reference Earth Model (PREM) is Dziewonski, A. M., & Anderson, D. L.
(1981), *Physics of the Earth and Planetary Interiors* **25**, 297–356.

**Second, every number in this lesson is computed and checked.** The
hydrostatic integration in
[`code/interior_pressure_demo.py`](./code/interior_pressure_demo.py) is verified
against two cases that can be solved in closed form: a uniform sphere and a
two-layer sphere. Both close to within $3\times10^{-4}$ relative, and the
discrepancies are quoted in §8. Nothing here is asserted that has not either been
computed or been taken from the constant handbook.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** $\mathrm{d}P/\mathrm{d}r = -\rho g$ from the force balance on a
   spherical shell, and state precisely what is being assumed about the shell.
2. **Derive** $g(r) = GM(r)/r^2$ from the shell theorem, and explain why only the
   mass inside $r$ contributes to the field at $r$.
3. **Scale** the central pressure as $GM^2/R^4$ before doing any integral, and
   evaluate the coefficient for a uniform sphere.
4. **Construct** a layered reference model from rounded density characteristics,
   and integrate the coupled equations for $M(r)$, $g(r)$ and $P(r)$.
5. **Verify** that integration against exact solutions for a uniform sphere and a
   two-layer sphere, and report the measured discrepancy.
6. **Explain** the density jump at the core–mantle boundary as a change of
   composition, using the opposite-signed jumps in $\rho$ and $v_p$.
7. **Apply** the Adams–Williamson relation $\mathrm{d}\rho/\mathrm{d}z = \rho g/\phi$
   and interpret where it succeeds and where it fails.
8. **Check** a model against the two surface observables that constrain it: total
   mass and $C/(MR^2)$.

## Prerequisites

- [02-06-01 Fluid Statics, Pressure and Buoyancy](../06-fluid-mechanics/01-fluid-statics.md)
  — the hydrostatic equation in a constant-density fluid, which is the starting
  point of §2 and the limit that fails in the deep Earth.
- [02-08-01 Newtonian Gravitational Potential and Field](../08-potential-theory/01-gravitational-potential.md)
  — the shell theorem and $g = -\nabla\Phi$.
- [01-06-04 Divergence, Curl and Physical Meaning](../../01-mathematics/06-multivariable-calculus/04-divergence-and-curl.md)
  — the divergence theorem, used in §2.2 to relate the flux of $\mathbf g$ to the
  enclosed mass.
- [26-02-03 Physical Constants and Earth Parameters](../../26-reference-library/02-symbols-and-units/03-constant-handbook.md)
  — §3.2 for the Earth's mass, radius and how they are classified, and §3.3 for
  the interior characteristics used throughout this lesson.

## 1. Why the interior is a hydrostatic problem

A fluid — and over geological time a solid, too, if its viscosity is low enough —
arranges itself so that no interior surface of constant density is out of
mechanical balance. If a shell of material at radius $r$ were to feel a net
upward force, it would rise; a net downward force and it would sink. The
timescale for that rearrangement is a viscous relaxation time, and for the mantle
it is short compared with the age of the Earth. So to an excellent approximation
the Earth is in hydrostatic equilibrium at every radius, and that is the single
assumption that lets us compute the pressure everywhere without knowing anything
about the material.

The second assumption is spherical symmetry, which is a statement about the
*mean* structure. The Earth is flattened by about 1 part in 298, has continents
and slabs, and is not a sphere. But the deviations are small perturbations on the
mean state, and the mean state is what a reference model describes. Everything
below is a mean radial structure, and its formal name is a **spherically
symmetric, hydrostatic, radially layered model**.

## 2. Derivation of the hydrostatic and gravity equations

### 2.1 Force balance on a thin shell

Take a shell of radius $r$, thickness $\mathrm{d}r$, and unit cross-sectional
area. Its mass per unit area is $\rho\,\mathrm{d}r$. Three forces act on it:

- gravity, $-\rho g\,\mathrm{d}r$ per unit area, directed inward;
- the pressure difference across it, $P(r) - P(r+\mathrm{d}r) = -\mathrm{d}P$,
  which is the net upward push;
- and, by assumption, no acceleration.

Equilibrium gives $-\mathrm{d}P - \rho g\,\mathrm{d}r = 0$, that is

$$\boxed{\ \frac{\mathrm{d}P}{\mathrm{d}r} = -\rho(r)\,g(r)\ } \qquad (1)$$

The pressure must decrease outward — the gradient is negative because gravity
points inward and the pressure must support the weight above. The single
boundary condition is $P(R) = 0$, because the surface of the Earth is not under
an imposed pressure (the atmosphere contributes $10^5$ Pa, which is $10^{-6}$ of
the central pressure and is neglected). This is the crucial structural point:
$\mathrm{d}P/\mathrm{d}r = -\rho g$ is a *first-order* equation, so exactly one
boundary condition is needed and only one is available. Pressure is therefore
*never* independently measurable in the deep interior; it is always a derived
quantity. No experiment measures 135 GPa at the CMB; the number is the integral
of $\rho g$ over the whole column above it.

### 2.2 The shell theorem and $g(r)$

The gravitational field inside a spherically symmetric body is produced only by
the mass inside the sphere of radius $r$. The mass outside, being spherically
distributed, exerts no net force at $r$. This follows from the divergence
theorem applied to $\mathbf g$:

$$\oint \mathbf g\cdot\mathrm{d}\mathbf A = -4\pi GM_{\text{enc}}
\qquad\Longrightarrow\qquad -4\pi r^2 g(r) = -4\pi G M(r),$$

so

$$\boxed{\ g(r) = \frac{G M(r)}{r^2}\ } \qquad (2)$$

with the enclosed mass

$$M(r) = \int_0^r 4\pi r'^2\rho(r')\,\mathrm{d}r'. \qquad (3)$$

Equations (1)–(3) are a closed system *if* $\rho(r)$ is known. They are not an
equation that determines $\rho$; density is an input, supplied by a reference
model, and the equations then tell you what $g$ and $P$ must be. The deep insight
is that this is an **over-determined** problem in the other direction: given
$\rho(r)$ you get $M$, $g$, $P$, and you can compare the implied $M$, $C$ and
$v_p$ against observation. Each comparison is a test of the assumed $\rho$.

### 2.3 Scaling before integrating

Before integrating anything, note that $P_c$ can only be built from $G$, $M$ and
$R$. Dimensional analysis forces

$$P_c \sim \frac{GM^2}{R^4},$$

and the numerical coefficient is a property of the density distribution alone.
For a uniform sphere it can be integrated at once. With
$\rho = M/(\tfrac{4}{3}\pi R^3)$ and $M(r) = Mr^3/R^3$,

$$P_c = \int_0^R \rho\frac{GM(r)}{r^2}\,\mathrm{d}r
= \frac{3GM^2}{8\pi R^4} = 0.1194\,\frac{GM^2}{R^4}. \qquad (4)$$

Evaluating with $G = 6.674\,30\times10^{-11}$ m³ kg⁻¹ s⁻² (CODATA, a **measured**
constant), $M = 5.972\times10^{24}$ kg (a **nominal** value derived from the
defining $GM_\oplus$ and the measured $G$) and $R = 6.371\times10^6$ m (nominal):
$P_c = 172.5$ GPa.

That is a *lower bound*. Any concentration of mass toward the centre puts more
weight in the outer part of the column, where $g$ is larger and the lever arm is
longer, and the same can be shown to raise $P_c$. The real Earth's 356.7 GPa —
twice the uniform value — is therefore direct evidence of a centrally condensed
planet, obtained without any seismology at all.

## 3. Integrating the equations over a layered reference model

### 3.1 The model

We adopt six layers whose density ranges are exactly the rounded handbook
characteristics, linearly interpolated in depth within each layer.

| Layer | Depth range (km) | $\rho$ (kg/m³) |
|---|---|---|
| Crust | 0–35 | 2600 → 2900 |
| Upper mantle | 35–410 | 3300 → 3600 |
| Transition zone | 410–660 | 3600 → 4400 |
| Lower mantle | 660–2891 | 4400 → 5570 |
| Outer core | 2891–5153 | 9900 → 12200 |
| Inner core | 5153–6371 | 12800 → 13100 |

Three features of this table deserve comment, because they are choices and not
facts.

**The density is continuous at 410 km and 660 km.** The handbook gives the
transition zone as 3600–4400 kg m⁻³ and the lower mantle as 4400–5570, so its
ranges join continuously. A real reference model has small density steps at both
discontinuities — a few per cent at 410 km, more at 660 km. Smearing them out is
a deliberate simplification whose consequence is quantified in §4.

**The jumps are at the Moho and at the core–mantle boundary.** The Moho step is
2900 → 3300 kg m⁻³ (13 per cent) and the CMB step is 5570 → 9900 kg m⁻³ (78 per
cent). Those two are the structural facts this lesson is about.

**Velocities are interpolated across the handbook ranges too**, so that
$\phi = v_p^2 - \tfrac{4}{3}v_s^2$ and $K = \rho\phi$ can be computed at any
depth. At the base of the lower mantle this uses $v_p = 13.7$ km/s, and at the
centre $v_p = 11.3$ km/s. Those are the handbook's own endpoints, so the $K$
values below are internally consistent with the density and velocity ranges —
they are still nominal anchors, not measurements.

### 3.2 The integration

Equations (1)–(3) are integrated on a 500 m radial grid by walking outward for
the mass,

$$M_i = M_{i-1} + 4\pi r_i^2\rho_i\,\Delta r,$$

and then inward for the pressure using the tabulated $g$,

$$P_i = P_{i-1} + \rho_i\,g_i\,\Delta r, \qquad P(R) = 0.$$

Two details matter. The mass loop starts at the centre and accumulates outward,
so $M(r)$ is the enclosed mass by construction. The pressure loop starts at the
surface and accumulates inward, so $P$ is the weight of everything above. Getting
these directions the wrong way round is the single commonest error in writing
this integrator; the symptom is a pressure that is maximum at the surface.

### 3.3 Results

Selected values from the demo, at grid points nearest the stated depths:

| Depth (km) | $\rho$ (kg/m³) | $g$ (m/s²) | $P$ (GPa) | $\phi$ (km²/s²) | $K = \rho\phi$ (GPa) |
|---|---|---|---|---|---|
| 0 | 2600 | 9.786 | 0.01 | 19.99 | 52.0 |
| 35 | 3300 | 9.813 | 0.96 | 38.61 | 127.4 |
| 410 | 3600 | 9.933 | 13.73 | 49.48 | 178.1 |
| 660 | 4400 | 9.947 | 23.69 | 64.28 | 282.8 |
| 2000 | 5103 | 9.882 | 86.50 | 93.88 | 479.0 |
| 2891 (just below CMB) | 9900 | 10.510 | 134.63 | 64.00 | 633.6 |
| 5153 | 12800 | 4.387 | 322.01 | 104.67 | 1339.7 |
| 6370 | 13100 | 0.007 | 356.69 | 109.43 | 1433.5 |

Four things to read off.

**$g$ barely changes through the mantle.** It is 9.79 m/s² at the surface and
10.51 m/s² at the core–mantle boundary, a rise of only 7 per cent across 2891 km.
The reason is a near-cancellation: as $r$ decreases, $1/r^2$ grows, but $M(r)$
shrinks; through the mantle the two effects almost balance. This is characteristic
of a body with most of its mass in a shell, and it is why a naive
"$g$ falls with depth" expectation is wrong.

**$g$ falls steeply through the outer core**, from 10.51 to 4.39 m/s², and to
zero at the centre. Inside a shell of nearly uniform density $M(r) \propto r^3$,
so $g \propto r$: almost linear, exactly as observed.

**The pressure at 410 km is 13.73 GPa**, against the 13.67 GPa that the
uniform-density estimate in
[02-05-07 Phase Equilibria](../05-thermodynamics/07-phase-equilibria.md) §4
produces. Two independent models agreeing to 0.4 per cent at that depth is
reassuring for both.

**The central pressure is 356.7 GPa.** The value obtained from published
reference models is of order 360 GPa; the exact number is set by the density
profile assumed, and the demo's own two-layer check in §8 shows how sensitive it
is to the shape of the profile.

### 3.4 The two checks that constrain the model

The model must reproduce the two observables it was not tuned to.

**Total mass.** The integration gives $5.9511\times10^{24}$ kg against the
nominal $5.972\times10^{24}$ kg, a ratio of **0.99650** — 0.35 per cent low. That
is a satisfying result rather than a coincidence: the handbook's density ranges
are rounded characteristics of the real Earth, so a model built from them should
recover the mass to a fraction of a per cent, and the residual measures how much
the rounding and the ignored density steps cost.

**Moment of inertia.** Computing

$$C = \frac{8\pi}{3}\int_0^R \rho(r)\,r^4\,\mathrm{d}r$$

gives $C/(MR^2) = \mathbf{0.3326}$, against the nominal Earth value of about
0.33. Again the agreement is close, and it is meaningful: the moment of inertia
is a much more sensitive probe of central condensation than the mass, because
$r^4$ weights the outer layers so heavily. A homogeneous sphere would give 0.4
and a point mass 0. The measured 0.33 is a statement that roughly a third of the
Earth's mass is deep enough to be de-leveraged, and lesson
[05](./05-planetary-physics.md) §1 turns that statement into a core density.

## 4. The density jump at the core–mantle boundary

### 4.1 What the profiles show

At 2891 km depth the model density jumps from 5570 to 9900 kg m⁻³ — a factor of
1.78 — while the seismic parameter $\phi$ *collapses* from 116.6 to 64.0 km² s⁻²,
because $v_p$ drops from 13.7 to 8.0 km/s across the same boundary. The pressure
is continuous to within the grid resolution (134.6 GPa on both sides).

That combination of signs is the whole argument. A change of *state* alone cannot
do it. Compressing a material raises its density and raises its elastic moduli,
so $\phi = K/\rho$ changes comparatively little and $v_p$ rises. A boundary at
which density nearly doubles while the compressional velocity drops by 40 per
cent requires a change of *material*.

### 4.2 What the material must be

Two candidate materials differ in the way the seismic parameter responds to
pressure. A silicate at 135 GPa has $K/\rho \approx 117$ km² s⁻². A metal-rich
material has a much lower $\phi$ for the same density: at the top of the outer
core, with $\rho = 9900$ kg m⁻³ and $v_p = 8.0$ km/s, $\phi = 64$ km² s⁻².

The physical reason is that $K$ depends on how strongly the electron density
resists compression, while $\rho$ depends on the mass of the atoms present. For a
given density, a higher mean atomic weight means fewer atoms per unit volume and
a lower velocity. Iron has a mean atomic weight near 56 against about 20 for
mantle silicates, so an iron-rich alloy at core density must have a lower $v_p$
than a silicate at the same density. The observation matches the prediction in
direction and roughly in magnitude, which is why the outer core is described as
iron-rich liquid rather than merely "dense".

Note what has and has not been shown. The physics below shows that the core is
*denser and more iron-rich in mean atomic weight* than the mantle. It does not by
itself give the exact iron fraction: the outer core is measurably less dense than
pure iron compressed to the same pressure, which requires light alloying
elements, and quantifying that deficit is a research problem in mineral physics
rather than a closed calculation (see
[12-global-geophysics-interior/02-04 Core Composition](../../12-global-geophysics-interior/02-composition-and-mineral-physics/04-core-composition.md)).

### 4.3 The Adams–Williamson test

There is a quantitative way to ask whether a given density gradient is just
self-compression or something more. If a layer is homogeneous and the compression
is adiabatic, then $\mathrm{d}\rho/\mathrm{d}P = \rho/K$, and combining that with
hydrostatic balance gives the **Adams–Williamson equation**:

$$\frac{\mathrm{d}\rho}{\mathrm{d}z} = \frac{\rho\,g}{\phi},
\qquad \phi \equiv v_p^2 - \tfrac{4}{3}v_s^2 = \frac{K}{\rho}, \qquad (5)$$

where $z$ increases downward. The demo compares this prediction with the model's
own density gradient at the middle of each layer:

| Region | $z$ (km) | $\rho$ | $g$ | $\phi$ | A–W $\mathrm{d}\rho/\mathrm{d}z$ | Model | ratio |
|---|---|---|---|---|---|---|---|
| Upper mantle | 222 | 3450 | 9.87 | 38.6 | 0.882 | 0.798 | 1.11 |
| Transition zone | 535 | 4000 | 9.96 | 56.6 | 0.703 | 3.187 | 0.22 |
| Lower mantle | 1776 | 4985 | 9.84 | 88.5 | 0.554 | 0.524 | 1.06 |
| Outer core | 4022 | 11050 | 7.68 | 83.7 | 1.014 | 1.016 | 1.00 |
| Inner core | 5762 | 12950 | 2.21 | 107.0 | 0.268 | 0.246 | 1.09 |

(All gradients in kg m⁻³ km⁻¹.)

**The lower mantle and the outer core pass.** Ratios of 1.06 and 1.00 mean that
the observed density gradient is what adiabatic self-compression of a homogeneous
layer would produce. That is the observation which justifies treating the lower
mantle and the outer core as convecting, well-mixed layers with their density
structure set by compression rather than by layering. The outer-core agreement at
1.00 is the sharpest single result in the demo.

**The transition zone fails, by a factor of 4.5.** Its gradient is far too steep
to be compression. The extra density comes from mineral phase changes — the
olivine-to-wadsleyite transition near 410 km and the
ringwoodite-to-bridgmanite-plus-ferropericlase decomposition near 660 km — each
of which packs the same atoms into less volume. That is exactly the regime in
which the Adams–Williamson assumption of a homogeneous layer breaks, and the
break is the signal.
[02-05-07](../05-thermodynamics/07-phase-equilibria.md) supplies the
thermodynamics of those transitions.

**The inner core ratio of 1.09** is a mild excess. It says the model's inner-core
gradient is slightly less than adiabatic self-compression requires, which is
within the resolution of the rounded densities and is not a claim about physics.

## 5. Physical interpretation

Three statements are worth carrying out of this lesson.

**Pressure is an integral, never a measurement.** Every pressure in the deep
Earth, including the 135 GPa at the core–mantle boundary that is quoted as though
it were a property, is the accumulated weight of the column above it computed
from an assumed density profile. When you see "the pressure at the inner core
boundary is 329 GPa", the correct reading is "the reference model's density
profile, integrated, gives 329 GPa there". That is why a revision to the density
model propagates into a revision of every pressure quoted downstream.

**Gravity inside a planet is not monotonic in an obvious way, and the reason is
a cancellation.** From the surface to the CMB, $g$ rises by 7 per cent; through
the core it falls by more than a factor of two. Both follow from
$g = GM(r)/r^2$ and the shape of $\rho(r)$. Anyone who expects interior gravity
to fall steadily with depth has not done the integral, and the integral is three
lines of code.

**The core–mantle boundary is where the physics of the Earth changes kind.** Above
it, the material is a silicate whose density gradient is compression plus phase
changes. Below it, it is a metal whose density gradient is almost purely
adiabatic compression. That is why a reference model is built in two halves, and
why a mineral-physics equation of state (lesson [02](./02-equations-of-state.md))
is calibrated separately for each.

## 6. Assumptions and regime of validity

| Assumption | Where used | Regime of validity | What breaks it |
|---|---|---|---|
| Hydrostatic equilibrium | Throughout | Valid when the viscous relaxation time is short compared with the timescale of the perturbation | Glacial isostatic adjustment, post-seismic relaxation, and any actively convecting region depart at the level of a few per cent or more |
| Spherical symmetry | Throughout | The Earth's flattening is 1/298; lateral heterogeneity in the mantle is of order 1 per cent in velocity | Subduction, plumes, the degree-2 structure of the lower mantle, and the low-velocity provinces |
| $\rho$ depends on $r$ only | Equations (1)–(3) | Definition of a reference model | Real lateral density variations; the reference model is a mean |
| $P(R) = 0$ | Boundary condition | The atmosphere is $10^5$ Pa against $10^{11}$ Pa | Only matters for its own sake; neglected here |
| Density continuous within a layer | The layered model | A modelling choice | The real 410 km and 660 km discontinuities have density steps of a few per cent |
| Adams–Williamson: homogeneous, adiabatic | §4.3 | Valid for a well-mixed convecting layer | Mineral phase changes (the transition zone) and compositional layering |
| Rigid-body moment of inertia | §3.4 | The Earth is not perfectly rigid, but the fluid Love number correction is small | Tidal and rotational deformation; treated in [12-global-geophysics-interior/06](../../12-global-geophysics-interior/06-geodesy-constraints-interior/01-moment-of-inertia.md) |

## 7. Units and dimensional analysis

- $\mathrm{d}P/\mathrm{d}r$: Pa m⁻¹. Check equation (1): $[\rho][g] =
  \mathrm{kg\,m^{-3}}\cdot\mathrm{m\,s^{-2}} = \mathrm{kg\,m^{-2}\,s^{-2}}
  = \mathrm{Pa\,m^{-1}}$ ✓.
- Integrating: Pa m⁻¹ × m = Pa ✓. Reporting GPa is a convenience: 356.7 GPa
  $= 3.567\times10^{11}$ Pa.
- $g = GM/r^2$: $\mathrm{m^3\,kg^{-1}\,s^{-2}}\cdot\mathrm{kg\,m^{-2}} =
  \mathrm{m\,s^{-2}}$ ✓.
- The central-pressure scale $GM^2/R^4$:
  $\mathrm{m^3\,kg^{-1}\,s^{-2}}\cdot\mathrm{kg^2\,m^{-4}} =
  \mathrm{kg\,m^{-1}\,s^{-2}} = \mathrm{Pa}$ ✓.
- **Useful anchors.** Mean density $M/(\tfrac43\pi R^3) = 5513$ kg m⁻³. Surface
  $g$ from the model is 9.786 m/s² against the standard gravity of 9.806 65 m/s²,
  which is exact by definition; the 0.2 per cent difference is the model's own
  mass shortfall, and it is a useful self-consistency check.
- **A trap in the $\phi$ column.** $\phi$ in km² s⁻² must be multiplied by
  $10^6$ before multiplying by $\rho$ in kg m⁻³ to get $K$ in Pa. Getting this
  wrong gives $K$ six orders of magnitude too small, i.e. a crustal bulk modulus
  for the inner core.

## 8. Python demonstration

[`code/interior_pressure_demo.py`](./code/interior_pressure_demo.py) builds the
layered model, integrates the hydrostatic and gravity equations, and performs
five checks and comparisons. This is the module's verification script. The blocks
below are the script's actual output, **abridged by omission** where a block would
otherwise repeat rows already tabulated above; every line shown is reproduced
verbatim, and running the script produces the full output.

```text
1. Layered reference model (rounded handbook characteristics)
layer                 depth range (km)         rho (kg/m3)
crust                             0-35           2600-2900
upper mantle                    35-410           3300-3600
transition zone                410-660           3600-4400
lower mantle                  660-2891           4400-5570
outer core                   2891-5153          9900-12200
inner core                   5153-6371         12800-13100
```

```text
 depth (km)  rho (kg/m3)   g (m/s2)   P (GPa)   phi (km2/s2)   K=rho*phi (GPa)
          0         2600      9.786      0.01          19.99              52.0
         35         3300      9.813      0.96          38.61             127.4
        410         3600      9.933     13.73          49.48             178.1
        660         4400      9.947     23.69          64.28             282.8
       2891         9900     10.510    134.63          64.00             633.6
       5153        12800      4.387    322.01         104.67            1339.7
       6370        13100      0.007    356.69         109.43            1433.5
```

```text
  model mass          = 5.9511e+24 kg
  nominal Earth mass  = 5.9720e+24 kg
  ratio               = 0.99650
  model C/(M R^2)     = 0.3326   (nominal Earth value ~0.33)
  model centre pressure = 356.7 GPa
  core-mantle boundary  at 2891 km: P = 134.6 GPa, g = 10.51 m/s2
  inner-core boundary   at 5153 km: P = 322.0 GPa, g = 4.39 m/s2
  surface gravity       g = 9.7856 m/s2   (standard gravity 9.80665 m/s2)
  g at 3000 km depth    = 10.261 m/s2
```

```text
region            z mid    rho      g    phi     A-W   model  ratio
upper mantle        222   3450   9.87   38.6   0.882   0.798   1.11
transition zone     535   4000   9.96   56.6   0.703   3.187   0.22
lower mantle       1776   4985   9.84   88.5   0.554   0.524   1.06
outer core         4022  11050   7.68   83.7   1.014   1.016   1.00
inner core         5762  12950   2.21  107.0   0.268   0.246   1.09
```

```text
  (a) Uniform sphere, exact P_c = 3 G M^2 / (8 pi R^4):
      rho = 5513.3 kg/m3  (mean density)
      numerical P_c = 172.5173 GPa
      exact     P_c = 172.4631 GPa
      relative difference = 3.140e-04
  (b) Two-layer planet, core radius 3480 km, rho_core 12576 kg/m3,
      rho_mantle 4138 kg/m3. Analytic P_c by integrating the two
      shells separately:
      numerical P_c = 389.6465 GPa
      exact     P_c = 389.5479 GPa
      relative difference = 2.531e-04
```

### What to observe

| Observation | Consequence |
|---|---|
| $g$ rises from 9.786 to 10.510 m/s² across 2891 km | $1/r^2$ and $M(r)$ almost balance through the mantle; interior gravity is not simply decreasing |
| $g = 4.387$ m/s² at 5153 km and 0 at the centre | Inside a nearly uniform core $M(r)\propto r^3$ and $g\propto r$ |
| $P$ = 134.6 GPa at the CMB, 322.0 GPa at the ICB | Pressure is the integrated weight of the column; 63 per cent of the central pressure is already reached at the CMB |
| Mass ratio 0.99650 against the nominal value | The rounded handbook densities are good to a fraction of a per cent |
| $C/(MR^2) = 0.3326$ against a nominal 0.33 | The model's central condensation matches; this is the constraint that eventually yields a core density |
| $\phi$ collapses from 116.6 to 64.0 km² s⁻² across the CMB | Density and velocity jump in opposite directions: composition, not compression |
| A–W ratio 0.22 in the transition zone | Phase changes, not self-compression, set the gradient there |
| A–W ratio 1.00 in the outer core | The outer core is adiabatic and homogeneous to within the model's resolution |
| Uniform-sphere error $3.1\times10^{-4}$ | The integrator reproduces an exact solution to the accuracy of the 500 m step |

> **Breaking exercise.** Change the radial step `DR` from 500 m to 2000 m and to
> 125 m, and predict *before running* how the uniform-sphere relative difference
> should change. It is a first-order (rectangle-rule) scheme for the mass and
> pressure integrals, so you should expect the error to halve when the step
> halves. Then answer the harder question: the uniform-sphere error is
> $3.1\times10^{-4}$ at $\Delta r = 500$ m, which is *far* smaller than a
> first-order scheme with $10^4$ steps has any right to be. Explain why. (Hint:
> think about which part of the integral the error accumulates in, and about the
> fact that the pressure integrand is a smooth quadratic in $r$ for the uniform
> sphere, so the rectangle rule is not first-order for *that* integrand.)

## 9. Common mistakes

1. **Integrating the pressure outward.** $P(R)$ is the only boundary condition
   and it is at the surface, so the accumulation must run inward. An outward
   integration has no boundary condition at all and gives an arbitrary answer
   that happens to look plausible after normalisation.
2. **Using the surface $g$ throughout.** $g$ is 9.79 m/s² at the surface and
   10.51 at the CMB. Using 9.8 for the whole column underpredicts the central
   pressure by about 8 per cent, which is larger than most of the effects you are
   trying to resolve.
3. **Forgetting that $\rho(r)$ is an input.** Equations (1)–(3) do not determine
   the density. A model is a hypothesis; the observations that test it are the
   mass, the moment of inertia and the seismic velocities.
4. **Quoting "the pressure at the core–mantle boundary" as if it were measured.**
   It is the integral of an assumed density profile. Report the model with the
   number.
5. **Treating the rounded handbook ranges as data.** They are nominal anchors.
   A value such as "3300 kg m⁻³ for the uppermost mantle" is a representative
   number for a quantity that varies laterally.
6. **Applying Adams–Williamson to the transition zone.** Its failure there is the
   information; the assumption of homogeneity is what breaks.
7. **Confusing the mean density with the central density.** The mean is 5513
   kg m⁻³; the centre is in the region of 13 000 kg m⁻³ by the handbook's own
   rounded range. They differ by a factor of 2.4, and the difference is the
   entire content of the moment-of-inertia constraint.
8. **Assuming the density jump at the CMB implies a similar velocity jump.**
   It implies the opposite, and the opposite is what makes the CMB a weak
   normal-incidence P reflector (lesson [03](./03-seismic-parameter-relations.md) §5).
9. **Reporting $g$ inside the Earth without saying which interior it belongs
   to.** Without a stated reference model, an interior $g$ is undefined.
10. **Believing that hydrostatic equilibrium is exact.** It is an approximation
    whose error is a few per cent in convecting regions, and that error is
    precisely what mantle dynamics is about.

## 10. Real-world applications

- **Reference Earth models.** Every seismological study that reports a depth
  refers to a reference model, and the model's density profile is what makes a
  depth-to-pressure conversion possible. Change the model and the pressure at
  which a phase transition is placed changes with it.
- **Mineral-physics experiments.** A diamond-anvil cell reaches mantle pressures;
  knowing which pressure corresponds to which depth is exactly this
  integration ([12-global-geophysics-interior/02-02](../../12-global-geophysics-interior/02-composition-and-mineral-physics/02-high-pressure-experiments.md)).
- **Geodesy and the moment of inertia.** $C/(MR^2)$ and the gravity
  coefficients are the surface observables that constrain core size, and they are
  measured by satellites
  ([12-global-geophysics-interior/06-01](../../12-global-geophysics-interior/06-geodesy-constraints-interior/01-moment-of-inertia.md)).
- **Planetary interiors.** The same integration, with a different mass, radius
  and equation of state, is how the cores of other bodies are inferred; see
  lesson [05](./05-planetary-physics.md).
- **Isostasy and lithospheric buoyancy.** The hydrostatic equation applied to the
  outer few tens of kilometres is the basis of every isostatic model, and the
  deviation from a perfect hydrostatic state is the load.
- **Borehole and reservoir pressure.** The same equation with a pore fluid gives
  the pore-pressure gradient, which is 9.8 MPa km⁻¹ for water and about
  23 MPa km⁻¹ for the rock overburden — the ratio is the basis of every
  fracture-gradient calculation in drilling.

## 11. Further reading

- **Dziewonski, A. M., & Anderson, D. L. (1981).** "Preliminary reference Earth
  model." *Physics of the Earth and Planetary Interiors* **25**, 297–356. The
  primary source for the reference model this lesson approximates. Level:
  graduate.
- **Turcotte, D. L., & Schubert, G. *Geodynamics* (3rd ed., Cambridge University
  Press, 2014).** Hydrostatic equilibrium, the Adams–Williamson equation and the
  moment of inertia, with the geophysical motivation. Level: graduate.
- **Fowler, C. M. R. *The Solid Earth* (2nd ed., Cambridge University Press,
  2005).** The most compact treatment of the density and pressure structure of
  the Earth, and the natural companion to this lesson. Level: intermediate to
  graduate.
- **Stacey, F. D., & Davis, P. M. *Physics of the Earth* (4th ed., Cambridge
  University Press, 2008).** The physics of the interior from first principles,
  including the thermodynamics of the core. Level: graduate.
- **Anderson, D. L. *Theory of the Earth* (Blackwell, 1989).** Freely available
  from the author's academic pages; the fullest development of the inference of
  composition from the reference model. Level: graduate.
- **Lowrie, W. *Fundamentals of Geophysics* (2nd ed., Cambridge University
  Press, 2007).** A gentler entry to the same material, with the observational
  context. Level: intermediate.
- **Boehler, R. (ed.) *High-Pressure Research: Application to Earth and
  Planetary Sciences* (AGU, 1992).** The conference volume that formed the
  modern mineral-physics literature; useful for the origins of the EOS forms in
  lesson [02](./02-equations-of-state.md).

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 12. Related lessons

- [02 Equations of State and High-Pressure Mineral Physics](./02-equations-of-state.md)
  — what supplies $\rho(P)$ and $\rho(T)$ in the first place.
- [03 Seismic Velocities, Elastic Moduli and Mineralogy](./03-seismic-parameter-relations.md)
  — how $v_p$, $v_s$ and $\rho$ together constrain composition.
- [05 Comparative Planetary Physics and Interiors](./05-planetary-physics.md)
  — the moment of inertia used as a core-size diagnostic.
- [02-06-01 Fluid Statics](../06-fluid-mechanics/01-fluid-statics.md) — the
  constant-density limit and where it stops being useful.
- [02-08-01 Newtonian Potential](../08-potential-theory/01-gravitational-potential.md)
  — the shell theorem in full.
- [02-05-07 Phase Equilibria and Mantle Mineralogy](../05-thermodynamics/07-phase-equilibria.md)
  — why the transition zone breaks Adams–Williamson.
- [12-global-geophysics-interior/01-01 PREM and Reference Models](../../12-global-geophysics-interior/01-seismic-structure-of-the-earth/01-prem-and-reference-models.md)
  — how such models are actually built and what they contain.

Exercises:
[`exercises/01-pressure-density-depth-exercises.md`](./exercises/01-pressure-density-depth-exercises.md)
and
[`exercises/01-pressure-density-depth-solutions.md`](./exercises/01-pressure-density-depth-solutions.md).

## Self-assessment checklist

- [ ] I can derive $\mathrm{d}P/\mathrm{d}r = -\rho g$ from a force balance on a
      shell and state the one boundary condition. (§2.1)
- [ ] I can derive $g(r) = GM(r)/r^2$ and say why only the enclosed mass
      contributes. (§2.2)
- [ ] I can scale the central pressure as $GM^2/R^4$ and evaluate the uniform
      coefficient 0.1194. (§2.3)
- [ ] I can build a layered model from rounded densities and integrate $M$, $g$
      and $P$ in the correct directions. (§3.2)
- [ ] I can verify the integrator against the uniform-sphere and two-layer exact
      solutions and report the discrepancies. (§8)
- [ ] I can check a model against the mass and $C/(MR^2)$ and interpret the
      residuals. (§3.4)
- [ ] I can explain the CMB density jump as a composition change using the
      opposite-signed $\rho$ and $v_p$ jumps. (§4.1–§4.2)
- [ ] I can state and apply the Adams–Williamson relation and interpret the
      ratios 1.00 and 0.22. (§4.3)
- [ ] I can list three assumptions of §6 with their regimes and what breaks them.
- [ ] I can explain why $g$ is nearly constant through the mantle and nearly
      linear in $r$ through the core. (§5)
