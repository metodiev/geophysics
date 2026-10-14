---
id: 06-01-06
title: "Interface Waves, Head Waves and the Total Wavefield"
level: doctoral
prereqs: ["06-01-04", "06-02-02", "06-02-05"]
tags: [seismology, interface-waves, head-waves, stoneley, total-wavefield, refraction]
---

# Interface Waves, Head Waves and the Total Wavefield

Everything so far in this module has named a wave and then computed it: a P
wave, an S wave, a Rayleigh wave, a reflection coefficient. This lesson is built
around the observation that the named arrivals are not the wavefield. They are
the *parts of an integral* that happen to be large at a particular offset, and
the honest statement of what a seismogram contains is a sum over contributions —
some discrete, some continuous — that no single ray name covers.

Two families are examined here because they expose the problem from opposite
sides.

- The **head wave** (the refracted arrival used by every refraction survey) is
  a body-wave arrival that exists only because the interface extends far enough
  to be "run along". It is not a ray that a ray-tracing program finds by
  shooting; it is a contribution from the slowness integral whose stationary
  phase is not on the real ray-parameter axis.
- The **interface wave** at a welded contact (a Stoneley wave) is a trapped mode
  that exists *only* for certain contrasts. Whether it exists at all is a
  property of the two media, and it is a measurement, not a definition.

The central honest difficulty of this lesson is that a seismogram can be fully
explained by the total field while every named arrival in it is a
partial-truth approximation. Both the head wave and the interface wave are
best understood by asking what is left over after they are removed.

All models and data in this module are **SYNTHETIC**. Every number quoted below
is printed by `code/interface_waves_demo.py`, or is an exact constant stated
with its units. No real station, event or waveform is used, and no measured
Earth property is quoted.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the critical angle, the head-wave intercept time and the crossover
   distance for a two-layer model from Snell's law alone, and **state** the
   condition on the velocity contrast under which the head wave exists.
2. **Explain** why the head wave's apparent velocity along the interface equals
   the velocity of the *lower* medium, and why that makes it a measurement of
   that medium rather than of the interface.
3. **Assemble** the four boundary conditions of a welded solid-solid contact as
   a $4\times4$ homogeneous system, and **derive** the existence condition
   $0 < c < \min(v_{s1}, v_{s2})$ for a trapped interface mode.
4. **Distinguish** contributions of pole, branch-point and stationary-phase type
   in the slowness integral, and **state** which named arrival each produces.
5. **Quantify** the discretisation error of an independent first-arrival
   calculation, and **state** the measured order of convergence rather than
   assuming it.
6. **Interpret** a measured existence boundary for trapped modes as a statement
   about the *contrast*, and **explain** why no existence criterion should be
   quoted from memory.

## Prerequisites

- [06-01-04 Reflected, Refracted and Converted Body Waves](04-body-wave-arrivals.md) —
  Snell's law in layered media and the Zoeppritz system whose boundary
  conditions are reused here.
- [06-02-02 Snell's Law and Layered Media](../02-ray-theory-and-travel-times/02-snell-and-layering.md) —
  the ray parameter as a conserved horizontal slowness.
- [06-02-05 Shadow Zones and Diffractions](../02-ray-theory-and-travel-times/05-shadow-zones.md) —
  what happens when no real ray reaches a receiver, which is the regime the head
  wave and the interface wave both live in.

## 1. Intuition: what a "ray" is a name for

Write the exact response of a layered medium to a point source as an integral
over horizontal slowness $p$ (the Sommerfeld–Weyl / Cagniard–de Hoop form):

$$u(\mathbf{x},t) = \int_{\mathcal{C}} \frac{A(p)}{\text{(geometry)}}
\, e^{\,\mathrm{i}\omega\left(t - p\,x - q(p)\,z\right)}\;\mathrm{d}p .$$

Everything we call an arrival comes from a **critical point** of that integral:

| Type of critical point | Named arrival |
|---|---|
| Stationary phase at a real saddle $p^{*}$ | direct, reflected, transmitted body waves |
| Pole of $A(p)$, at a real slowness slower than every body-wave speed | surface wave (Rayleigh, Love), trapped interface mode (Stoneley) |
| Branch-point contribution, i.e. the branch-line integral | **head wave**, and diffraction from a shadow boundary |
| The rest of the contour | the "continuous field": near-field, evanescent, scattered |

Two consequences follow immediately and they are the reason this lesson exists.
First, the list is a classification of *mathematics*, not of rock: the same
physics, evaluated at a different offset, changes which critical point
dominates. Second, when a receiver sits in a shadow zone there is no real
stationary point at all, and the field is carried entirely by the last three
rows — a situation no collection of named rays can describe.

## 2. Precise definitions

**Head wave.** In a two-layer model with $v_2 > v_1$, a ray in the lower medium
travelling parallel to the interface has horizontal slowness $1/v_2$. Because
$1/v_2 < 1/v_1$, that slowness is *not* attainable by a real ray in the upper
medium; the corresponding disturbance in the upper medium is evanescent, and the
energy that shows up at the surface is radiated from the interface along the
critical direction. The resulting arrival is the head (or refracting) wave.

**Apparent velocity.** The velocity inferred from the slope of a travel-time
curve, $v_{\text{app}} = \mathrm{d}x/\mathrm{d}t$. For the head wave it is $v_2$;
for a direct wave it is $v_1$.

**Critical angle.** The incidence angle $\theta_c$ in medium 1 at which the
transmitted ray is parallel to the interface. From Snell's law,
$\sin\theta_c/v_1 = 1/v_2$, so $\sin\theta_c = v_1/v_2$. It exists only when
$v_2 > v_1$.

**Interface (Stoneley) wave.** A solution of the elastodynamic equations that is
attached to a welded contact between two solid half-spaces and decays away from
it on both sides. It carries no length scale, so its speed $c$ does not depend on
frequency: it is *non-dispersive*, unlike the Rayleigh wave in a layer over a
half space.

**Total wavefield.** The complete solution, including all contributions of every
type in §1, without selecting a "first arrival".

## 3. Derivation: the head wave, from Snell's law to a travel-time curve

### 3.1 Geometry

Let a source and receiver lie on the free surface of a layer of thickness $H$
and speed $v_1$, over a half space of speed $v_2 > v_1$. The head-wave path is:

1. down from the source to the interface at angle $\theta_c$,
2. along the interface at speed $v_2$,
3. up from the interface to the receiver at angle $\theta_c$.

The two inclined legs each have length $H/\cos\theta_c$ and are traversed at
speed $v_1$; the interface leg has length $x - 2H\tan\theta_c$ and is traversed at
speed $v_2$. Hence

$$
t_{\text{head}}(x)
= \frac{2H}{v_1\cos\theta_c}
+ \frac{x - 2H\tan\theta_c}{v_2}.
$$

Using $\cos\theta_c = \sqrt{1 - (v_1/v_2)^2}$ and $\sin\theta_c = v_1/v_2$, the
$x$-dependent terms combine and the expression collapses to the standard linear
form

$$
\boxed{\;t_{\text{head}}(x) = \frac{x}{v_2} + t_i,
\qquad
t_i = \frac{2H\cos\theta_c}{v_1} = \frac{2H\sqrt{v_2^2 - v_1^2}}{v_1 v_2}.\;}
$$

The quantity $t_i$ is the **intercept time**: the extrapolation of the head-wave
line back to $x = 0$. The slope is $1/v_2$, so a refraction profile measures the
*lower* velocity, scaled by a thickness through $t_i$.

### 3.2 Crossover distance

The direct arrival is $t_{\text{direct}} = x/v_1$. The first arrival switches from
direct to head when the two times are equal:

$$\frac{x}{v_1} = \frac{x}{v_2} + t_i
\quad\Longrightarrow\quad
x_{\text{cross}} = t_i\left(\frac{1}{v_1} - \frac{1}{v_2}\right)^{-1}
= \frac{t_i\,v_1 v_2}{v_2 - v_1}.$$

Two properties of this expression matter in practice. It grows linearly with $H$,
so a thick layer hides the head wave to large offsets; and it grows as the
contrast shrinks, so a weak contrast requires long offsets. Both are statements
about *geometry*, not about rock type, and neither can be escaped by better
instrumentation.

### 3.3 Numerical check (SYNTHETIC model of the demonstration)

$v_1 = 1500\ \mathrm{m\,s^{-1}}$, $v_2 = 3000\ \mathrm{m\,s^{-1}}$,
$H = 20\ \mathrm{m}$:

$$\sin\theta_c = 1500/3000 = 0.5 \;\Longrightarrow\;
\theta_c = 30.000000^\circ,\qquad \cos\theta_c = \tfrac{\sqrt3}{2} = 0.8660254,$$

$$t_i = \frac{2(20)(0.8660254)}{1500}
= \frac{34.641016}{1500}\ \mathrm{s}
= 0.023094011\ \mathrm{s} = 23.094011\ \mathrm{ms},$$

$$x_{\text{cross}} = \frac{(0.023094011)(1500)(3000)}{1500}
= 69.2820\ \mathrm{m}.$$

These are exactly the numbers the demonstration prints, and the apparent
velocity it reports along the interface is $v_2 = 3000\ \mathrm{m\,s^{-1}}$.

## 4. Derivation: why the head wave needs $v_2 > v_1$

Snell's law is $\sin\theta_2 = (v_2/v_1)\sin\theta_1$. A transmitted angle
$\theta_2 = 90^\circ$ requires $\sin\theta_1 = v_1/v_2 \le 1$. If $v_2 < v_1$
there is no incidence angle that produces a ray travelling along the interface,
the branch-point contribution moves off the real slowness axis, and no head wave
exists. The condition is therefore

$$v_2 > v_1 \quad\text{(the lower medium must be faster)},$$

which is why a refraction survey is impossible over a velocity *inversion* — the
classic hidden-layer problem. Note that the head wave is also not "the ray that
grazes the interface": a grazing ray exists in both cases, but only with a
faster lower medium does the branch-line integral contribute a distinct arrival
with the slope $1/v_2$.

## 5. Derivation: the trapped interface mode at a welded contact

### 5.1 Potentials and decay

Take two homogeneous isotropic half-spaces in welded contact at $z = 0$, with
$z<0$ medium 1 and $z>0$ medium 2, and look for a wave that propagates along
$+x$ and decays with $|z|$. Write, as in
[05 Wavefield Potentials](05-wavefield-potentials.md), the displacement as the
gradient of a P potential plus the curl of an S potential, with

$$\phi = A\,e^{\,\mathrm{i}k(x - ct)}\,e^{\alpha z},\qquad
\psi = B\,e^{\,\mathrm{i}k(x - ct)}\,e^{\beta z},$$

and the decay conditions $\alpha^2 = k^2\left(1 - c^2/\alpha_{v}^2\right) > 0$,
$\beta^2 = k^2\left(1 - c^2/\beta_{v}^2\right) > 0$, where $\alpha_v,\beta_v$ are
the P and S speeds. "Decays on both sides" therefore requires

$$c < \alpha_{v1},\ \beta_{v1},\ \alpha_{v2},\ \beta_{v2}
\qquad\Longrightarrow\qquad
0 < c < \min(\beta_{v1}, \beta_{v2}),$$

since the S speed is always the smaller of the two in each medium. This single
inequality is the entire existence bound: a trapped welded-interface mode can
only be slower than the slower shear speed of the two media.

### 5.2 The four boundary conditions

A welded contact transmits traction and displacement. Continuity of the two
displacement components and of the two traction components gives, at $z = 0$,

$$u_x^{(1)} = u_x^{(2)},\qquad u_z^{(1)} = u_z^{(2)},\qquad
\sigma_{zz}^{(1)} = \sigma_{zz}^{(2)},\qquad
\sigma_{xz}^{(1)} = \sigma_{xz}^{(2)}.$$

Substituting the potential forms turns these into a homogeneous linear system

$$\mathbf{M}(c)\,\mathbf{v} = \mathbf{0},
\qquad \mathbf{v} = (A_1, B_1, A_2, B_2)^{\!\top},$$

and a nonzero solution exists if and only if $\det\mathbf{M}(c) = 0$. Because the
only lengths in the problem are $1/k$ and the half-space is infinite, $k$
cancels from every entry: the condition is a function of $c$ alone, and the
resulting mode is **non-dispersive**. That is the structural reason a Stoneley
wave has a single speed while a Rayleigh wave in a layer has a dispersion curve.

The demonstration builds $\mathbf{M}$ from the *same potential coefficients*
verified by the Zoeppritz solution in
[04 Body-Wave Arrivals](04-body-wave-arrivals.md), scans
$0 < c < \min(v_{s1}, v_{s2})$ for a sign change of the determinant, and then
checks that the matrix actually loses rank at the root rather than merely
changing sign.

### 5.3 What the measurement says

The fixed medium 1 is $v_p = 5000\ \mathrm{m\,s^{-1}}$,
$v_s = 2900\ \mathrm{m\,s^{-1}}$, $\rho = 2600\ \mathrm{kg\,m^{-3}}$, whose
free-surface Rayleigh speed the demonstration computes as
$2664.6114\ \mathrm{m\,s^{-1}}$. Sweeping the shear-ratio $v_{s2}/v_{s1}$ and the
density ratio $\rho_2/\rho_1$ over a $10\times5$ grid (50 combinations), the
demonstration finds **roots in 8 of the 50 combinations**, every root has a
shear-velocity ratio in the interval $[0.90, 1.10]$, and every root satisfies
$c/\min(v_s) \ge 0.980676$. In other words, the trapped mode travels at *almost*
the slower shear speed of the pair — within about 2% of it over this grid — which
is why a trapped interface wave is difficult to separate from a direct S arrival
on a record at finite offset.

Outside that contrast band the determinant does not change sign anywhere on the
admissible interval, and no trapped welded-interface mode exists in this model
class. Existence is therefore a statement about the *pair of media*, not a
general property of interfaces — the numerical form of the familiar observation
that the Stoneley mode requires the two solids to be similar.

Two consistency checks distinguish a genuine mode from a near-miss:

| Quantity | Value printed by the demo |
|---|---|
| Model | $v_{s2}/v_{s1} = 1.00$, $\rho_2/\rho_1 = 0.60$ |
| Root speed | $c = 2894.2775\ \mathrm{m\,s^{-1}}$ |
| Smallest/largest singular value of the row-normalised matrix at the root | $5.916\times10^{-16}$ |
| Same ratio 5% away from the root ($c = 3038.9914\ \mathrm{m\,s^{-1}}$) | $1.542\times10^{-1}$ |

A rank-deficient matrix at the root and a well-conditioned matrix 5% away is the
numerical statement that the mode is a true null vector of the boundary
conditions. No existence criterion is quoted from memory here: the boundary
located above is the one the scan resolved for this model class.

## 6. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| layer thickness | $H$ | m | |
| body-wave speed | $v_1, v_2, v_p, v_s$ | $\mathrm{m\,s^{-1}}$ | |
| critical angle | $\theta_c$ | rad (or deg) | $\sin\theta_c = v_1/v_2$ is dimensionless |
| ray parameter | $p$ | $\mathrm{s\,m^{-1}}$ | $\sin i / v$ |
| vertical slowness | $q$ | $\mathrm{s\,m^{-1}}$ | $\sqrt{v^{-2}-p^{2}}$ |
| intercept time | $t_i$ | s | $\mathrm{m}\times\mathrm{s\,m^{-1}}$: $\dfrac{2H\cos\theta_c}{v_1}$ |
| crossover distance | $x_{\text{cross}}$ | m | $\mathrm{s}\times\mathrm{m\,s^{-1}}$: $t_iv_1v_2/(v_2-v_1)$ |
| interface-wave speed | $c$ | $\mathrm{m\,s^{-1}}$ | root of a determinant in $c$ alone |
| density | $\rho$ | $\mathrm{kg\,m^{-3}}$ | enters only through ratios |

Two structural points are worth extracting from the table. First, the head-wave
intercept time is the *only* combination of $H$, $\theta_c$ and $v_1$ that can
produce a time, and it must: a length times a slowness is a time. If a computation
of $t_i$ comes out in $\mathrm{m^2\,s^{-1}}$ or in $\mathrm{s^{-1}}$, a factor of a
velocity has been misplaced. Second, the trapped-mode condition is homogeneous in
$c$: the determinant carries no length, no time and no mass, so its root $c$ is a
speed built from the two media's speeds alone (through their ratios) — which is the
dimensional reason the mode is non-dispersive.

## 7. The total wavefield: what is left over

It is worth stating the bookkeeping explicitly, because it is the conceptual
content of the lesson.

1. The exact response is an integral over slowness (§1).
2. Every named phase is one critical-point contribution to that integral: body
   waves from real saddles, surface waves from poles, the head wave from a
   branch line.
3. The *sum of all named contributions* is not the field. Whatever is not
   captured is a continuous contribution with no name, and it is not small near
   the source (where the near field dominates), in shadow zones (where no real
   saddle exists), and immediately behind a wavefront.
4. Therefore two statements are compatible and both true: "the first arrival at
   long offset is the head wave, $t = x/v_2 + t_i$", and "a refraction profile
   is an inversion for $v_2$ and $H$ that assumes the total field can be
   represented by two named arrivals". The second statement is where the
   approximation lives, and it must be reported.

## 8. Assumptions and regime of validity

1. **Two homogeneous isotropic half-spaces, welded.** A fluid lower medium
   replaces the welded conditions with purely normal traction and slip, giving
   the Scholte (or Stoneley–Scholte) interface wave instead; that case is not
   solved here.
2. **Plane strain in the $x$–$z$ plane.** Out-of-plane (SH) motion decouples and
   cannot form the mode considered; this is the same decoupling used for Love
   waves in [03 Surface Waves](03-surface-waves.md).
3. **No attenuation.** Interface waves are strongly affected by anelasticity and
   by a thin low-velocity layer, neither of which is in the model.
4. **A laterally infinite, perfectly sharp interface** for the head wave. A
   finite refractor, a dip, or a gradational transition changes both $t_i$ and
   the amplitude behaviour.
5. **Head-wave amplitudes are not computed here.** The demonstration computes
   arrival *times*; the amplitude decay of the head wave is an asymptotic result
   that this lesson does not derive, and no amplitude number is quoted.
6. **The grid calculation assumes an 8-neighbour stencil.** Its systematic error
   is a property of that stencil (see §9.2) and would differ for a 16-neighbour
   or eikonal solver.

## 9. Worked examples

### 9.1 Head-wave travel times, by hand

With $v_1 = 1500$, $v_2 = 3000\ \mathrm{m\,s^{-1}}$, $H = 20\ \mathrm{m}$,
$t_i = 23.094\ \mathrm{ms}$:

| $x$ (m) | $t_{\text{direct}} = x/v_1$ (ms) | $t_{\text{head}} = x/v_2 + t_i$ (ms) | first arrival (ms) |
|---|---|---|---|
| 30 | 20.000 | 33.094 | 20.000 (direct) |
| 60 | 40.000 | 43.094 | 40.000 (direct) |
| 100 | 66.667 | 56.427 | 56.427 (head) |
| 200 | 133.333 | 89.761 | 89.761 (head) |
| 400 | 266.667 | 156.427 | 156.427 (head) |

The demonstration's independent grid calculation returns $20.000$, $40.000$,
$56.427$, $89.761$ and $156.427\ \mathrm{ms}$ at $\Delta x = 1\ \mathrm{m}$ for
the head-wave branch, and the switch between the two branches happens exactly at
$x_{\text{cross}} = 69.282\ \mathrm{m}$.

### 9.2 Discretisation error of the independent calculation

The same arrivals are computed on a graph by Dijkstra's algorithm, with the same
two media and an interface at depth $H$. Comparing with the closed form:

| $\Delta x$ (m) | $x$ (m) | analytic (ms) | grid (ms) | relative difference |
|---|---|---|---|---|
| 4.0 | 100 | 56.427344 | 60.702549 | $7.576\times10^{-2}$ |
| 4.0 | 400 | 156.427344 | 160.702549 | $2.733\times10^{-2}$ |
| 2.0 | 100 | 56.427344 | 59.207455 | $4.927\times10^{-2}$ |
| 1.0 | 100 | 56.427344 | 58.459909 | $3.602\times10^{-2}$ |
| 1.0 | 400 | 156.427344 | 158.459909 | $1.299\times10^{-2}$ |

The grid is systematically **late**, because an 8-neighbour graph measures a
staircase approximation to the inclined leg and therefore overestimates its
length. Halving $\Delta x$ from 4 m to 1 m reduces the error at $x = 400\ \mathrm{m}$
from $2.733\times10^{-2}$ to $1.299\times10^{-2}$, a factor of $2.10$ for a
factor of 4 in $\Delta x$. Taking the printed consecutive ratios,
$2.733/1.777 = 1.538$ and $1.777/1.299 = 1.368$ per halving, the *measured*
order of convergence is

$$\frac{\ln 1.538}{\ln 2} = 0.62,\qquad
\frac{\ln 1.368}{\ln 2} = 0.45,$$

i.e. of order $0.5$, not 2. A second-order scheme would reduce the error by 4 per
halving; the stencil, not the arithmetic, is the limitation. This is a useful
reminder that agreement between two independent methods must be *quantified*,
and that the observed convergence order is a measurement.

### 9.3 Existence of the trapped mode, summarised from the sweep

From the 50-point sweep of §5.3 the demonstration reports:

- roots in 8 of 50 combinations;
- every root with $v_{s2}/v_{s1} \in [0.90, 1.10]$;
- every root with $c/\min(v_s) \ge 0.980676$;
- a rank-deficient condition matrix at the root ($5.916\times10^{-16}$) and a
  well-conditioned one 5% away ($1.542\times10^{-1}$).

The correct reading of that table is a statement about a *contrast range*, not a
formula to be quoted. Any general existence criterion would have to be derived
for the specific symmetry and contact type at hand; the honest output of this
model is the measured boundary.

## 10. Python demonstration

[`code/interface_waves_demo.py`](./code/interface_waves_demo.py) performs both
halves of the lesson:

1. builds the head-wave times analytically from Snell's law and the geometry of
   §3, computes $t_i$ and $x_{\text{cross}}$, and compares with a grid
   first-arrival calculation at three grid spacings;
2. assembles the $4\times4$ welded-contact system, scans for trapped-mode roots
   over a grid of shear- and density-contrast pairs, reports the existence
   boundary, and checks the null-vector property at one root.

It is print-only, uses the fixed seed `np.random.default_rng(20261014)`, and
exits 0:

```bash
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python \
    06-seismology/01-elastic-wave-propagation/code/interface_waves_demo.py
```

## 11. Exercises

Full sets with worked solutions are in
[`exercises/06-interface-waves-exercises.md`](./exercises/06-interface-waves-exercises.md)
and
[`exercises/06-interface-waves-solutions.md`](./exercises/06-interface-waves-solutions.md).
They include a hand computation of $t_i$ and $x_{\text{cross}}$, a contrast
inversion from two apparent velocities, a convergence-order measurement, and a
research-level question on why the head wave's amplitude requires an asymptotic
treatment that this lesson deliberately omits.

## Mastery checkpoint

Without notes, and using only the SYNTHETIC model
$v_1 = 1500\ \mathrm{m\,s^{-1}}$, $v_2 = 3000\ \mathrm{m\,s^{-1}}$,
$H = 20\ \mathrm{m}$:

**(a)** State $\theta_c$, compute $t_i$ and $x_{\text{cross}}$, and give the unit
of each.
**(b)** Write the head-wave arrival time at $x = 250\ \mathrm{m}$ and say whether
it is the first arrival there.
**(c)** Explain in three sentences why the head-wave slope measures $v_2$ and not
the interface.
**(d)** Write the four welded-contact boundary conditions and derive the
bound on $c$ for a trapped mode.
**(e)** The demonstration finds no trapped mode for $v_{s2}/v_{s1} = 0.60$ at any
density ratio it tries. State precisely what that does *not* prove.

A worked version of (a)–(d) appears in
[`exercises/06-interface-waves-solutions.md`](./exercises/06-interface-waves-solutions.md).

## Common pitfalls

1. **Treating the head wave as a ray a tracer can shoot.** The grazing ray and
   the head wave have the same geometry but different amplitudes and different
   existence conditions; the head wave comes from a branch line, not from a real
   saddle.
2. **Quoting an interface-wave existence criterion from memory.** Existence
   depends on the contact type and the contrast; measure it for the model at
   hand, as §9.3 does.
3. **Confusing non-dispersive with trivial.** The Stoneley speed is
   frequency-independent because the problem has no length scale; a thin layer,
   attenuation or a fluid contact destroys that property.
4. **Reporting agreement between two solvers as validation.** Two methods that
   share a discretisation assumption validate each other's arithmetic, not the
   physics. The grid here agrees to about 1.3% at $\Delta x = 1\ \mathrm{m}$,
   with a measured order of about 0.5.
5. **Forgetting that the ray sum is incomplete.** Reporting only named phases
   near the source, in a shadow, or just behind a wavefront is a statement about
   the approximation, not about the Earth.

## Self-assessment checklist

- [ ] I can derive $t_i = 2H\cos\theta_c/v_1$ and $x_{\text{cross}}$ without notes.
- [ ] I can state the existence condition $v_2 > v_1$ and explain it with Snell's law.
- [ ] I can write the four welded-contact boundary conditions and explain why they give a $4\times4$ determinant.
- [ ] I can derive the trapped-mode bound $0 < c < \min(v_{s1},v_{s2})$ from the decay constants.
- [ ] I can explain why the trapped mode is non-dispersive but the Rayleigh wave in a layer is dispersive.
- [ ] I can classify a named arrival by the type of critical point that produces it.
- [ ] I can measure the convergence order of a numerical first-arrival calculation and state it as a number.

## Related modules

- [06-02 Ray Theory and Travel Times](../02-ray-theory-and-travel-times/README.md) —
  the ray picture this lesson shows to be incomplete, and the tau-p or Radon
  domain in which the missing contributions are natural.
- [06-05 Attenuation and Anelasticity](../05-attenuation-and-anelasticity/README.md) —
  why measured interface- and surface-wave amplitudes need a scattering term.
- [06-09 Reflection Seismology](../09-reflection-seismology/README.md) — the
  same welded-contact conditions used to build a reflection-coefficient
  inversion.
- [06-10 Refraction and Near-Surface Seismology](../10-refraction-and-near-surface-seismology/README.md) —
  the head wave as a working method, with the hidden-layer failure mode of §4.
- [06-11 Earthquake Statistics and Hazard](../11-earthquake-statistics-and-hazard/README.md) —
  the classification of critical points reappears as the classification of
  waveform attributes.
