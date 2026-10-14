---
id: 06-02-02
title: "Snell's Law, Layered Media and the Travel-Time Curve"
level: advanced
prereqs: ["06-02-01", "06-01-02", "01-03-01"]
tags: [seismology, snell, layered-media, head-waves, travel-time-curve, refraction]
---

# Snell's Law, Layered Media and the Travel-Time Curve

Almost every first-pass interpretation of a seismic record is a *layered*
interpretation. The crust is approximated by a stack of constant-velocity
layers, each interface produces a branch of arrivals, and the shape of the
travel-time curve — its slopes and intercepts — is inverted into thicknesses and
velocities. The whole method rests on one conservation law: in a stack of
horizontal layers the quantity

$$p = \frac{\sin i}{v}$$

is the same in every layer, where $i$ is the angle between the ray and the
vertical. This $p$ is the **ray parameter**, and it is the first integral of the
eikonal equation for a medium that depends on depth alone.

That single constant does a surprising amount of work. It fixes the geometry of
every ray, it is the *apparent slowness* measured on a record section, and — as
[03 The tau-p Transform and Intercept Time](03-tau-p.md) shows — it is the
natural variable in which the travel-time curve becomes a straight line. The
structure of this lesson follows the structure of the physics: derive the
conservation law, get the geometry from it, build the travel-time curve, then
measure what the finished curve can and cannot tell you.

The honest difficulty here is that a travel-time curve is an *incomplete* record
of the velocity structure. It sees only the arrivals that exist, and an interface
beneath a slower layer produces no arrival at all. A layered model is therefore
never uniquely recovered from first arrivals; the best a careful analyst can do
is report which parts of the structure the data constrain and which parts they
merely fail to contradict.

**All models and data in this module are SYNTHETIC.** The stack in this lesson
($6.00$, $6.50$, $7.00\ \mathrm{km\,s^{-1}}$ over an $8.00\ \mathrm{km\,s^{-1}}$
half space, with $5$, $10$ and $10$ km layers) is a chosen teaching model. Every
number quoted below is printed by `code/snell_and_layering_demo.py` when it runs;
none is taken from a published survey.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** $p = \sin i / v = \text{const}$ twice — from Fermat's principle and
   as the first integral of the ray equation for $v = v(z)$ — and **state** the
   assumption each derivation needs.
2. **Compute** the critical angle and the critical (minimum) offset of a head
   wave from the layer velocities and thicknesses.
3. **Construct** the travel-time curve of a layered stack from its branches, and
   **show** that each branch's slope is the reciprocal of the layer velocity it
   runs along.
4. **Derive** the intercept time $\tau = 2\sum_i h_i\cos\theta_i / v_i$ and
   **verify** it against the measured branch, including the identity
   $T - pX = \text{const}$.
5. **Identify** hidden (low-velocity) layers and **explain** why no arrival from
   them can appear in the first-arrival curve.
6. **Propagate** thickness and velocity uncertainties into an inverted depth, and
   **report** the depth with its conditional velocity assumption attached.
7. **Explain** why a grid method can miss a head wave that the closed-form
   branches contain.

## Prerequisites

- [06-02-01 Eikonal Equation, Rays and Fermat's Principle](01-eikonal-and-rays.md)
  — the eikonal equation and the ray equations used in Section 1.
- [06-01-02 P and S Waves: Particle Motion, Speeds and Polarisation](../01-elastic-wave-propagation/02-p-and-s-waves.md)
  — the speeds that enter every layer.
- [01-03-01 Angles, Triangles and the Unit Circle](../../01-mathematics/03-trigonometry/01-angles-and-triangles.md)
  — the trigonometry of the ray geometry.

## 1. Two derivations of the same conservation law

### 1.1 From Fermat's principle

Put two half spaces in contact at $z = 0$, with speeds $v_1$ above and $v_2$
below, and let a ray go from a point $A$ at height $h_1$ in the upper medium to a
point $B$ at depth $h_2$ in the lower one, crossing the interface at horizontal
position $x$. The travel time is

$$T(x) = \frac{\sqrt{x^{2} + h_1^{2}}}{v_1}
+ \frac{\sqrt{(X - x)^{2} + h_2^{2}}}{v_2},$$

where $X$ is the horizontal separation of $A$ and $B$. Fermat's principle says
the actual path has $\mathrm{d}T/\mathrm{d}x = 0$:

$$\frac{x}{v_1\sqrt{x^{2}+h_1^{2}}} = \frac{X - x}{v_2\sqrt{(X-x)^{2}+h_2^{2}}}.$$

The left side is $\sin i_1 / v_1$ and the right side is $\sin i_2 / v_2$, where
both angles are measured from the vertical. Therefore

$$\boxed{\;\frac{\sin i_1}{v_1} = \frac{\sin i_2}{v_2} \equiv p\;}$$

which is Snell's law, and $p$ has the units of slowness:
$\mathrm{s\,km^{-1}}$ (or $\mathrm{s\,m^{-1}}$), because $\sin i$ is
dimensionless.

### 1.2 As the first integral of the ray equation

For $v = v(z)$ the ray equation from
[01](01-eikonal-and-rays.md) reduces to a conservation law. Let $i(z)$ be the
angle from the vertical. Differentiating $\sin i = p v$ with respect to arc
length and using the ray equation gives $\mathrm{d}p/\mathrm{d}s = 0$: with
depth as the only coordinate, $p$ cannot change along the ray. Physically this is
a statement about translation symmetry — the medium does not change horizontally,
so the horizontal component of the slowness is conserved, exactly as a component
of momentum is conserved when a potential depends on only one coordinate.

The geometric content is worth stating once, because it is used constantly. If a
ray crosses a layer of thickness $h$ at angle $i$ from the vertical, then

$$\text{vertical slowness} \quad \eta \equiv \frac{\cos i}{v}
= \sqrt{\frac{1}{v^{2}} - p^{2}},
\qquad
\text{travel time across the layer} = h\,\eta,
\qquad
\text{horizontal advance} = h\tan i = \frac{h\,p}{\eta}.$$

All three follow from $\sin i = pv$ and $\cos i = \sqrt{1 - p^{2}v^{2}}$. For a
ray to exist in a layer at all, $p \le 1/v$ must hold: a ray parameter larger
than a layer's slowness is evanescent there, which is the seed of the shadow
zones of [05](05-shadow-zones.md).

## 2. Head waves and the moment a branch is born

Suppose $v_2 > v_1$. As the incidence angle $i_1$ increases, $i_2$ increases
faster, and at

$$\sin i_{c} = \frac{v_1}{v_2}$$

the transmitted ray is horizontal ($i_2 = 90^\circ$). Beyond that, the interface
responds by launching a disturbance that travels *along* it at speed $v_2$ and
radiates back into the upper medium at $i_c$: this is the **head wave** (the
"refraction" of exploration seismology). For the demonstration's first interface,
$v_1 = 6.00$ and $v_2 = 6.50\ \mathrm{km\,s^{-1}}$ give
$i_c = 67.380^\circ$.

Two numbers define the branch:

- the **critical offset**, the surface separation at which the head wave first
  returns,
  $$X_c = 2\sum_{i < k} h_i \tan\theta_i,$$
  the horizontal distance travelled down and up at the critical angle;
- the **intercept time**, the surface-separation-independent part of its arrival
  time,
  $$\tau = 2\sum_{i < k} h_i\,\eta_i = 2\sum_{i<k}\frac{h_i\cos\theta_i}{v_i}.$$

Along the branch, the arrival time is

$$T(X) = \frac{X}{v_k} + \tau ,$$

so the branch is a straight line of slope $1/v_k$. That is the central practical
fact of refraction interpretation: **the slope of a branch measures the speed of
the layer the ray runs along**, and the intercept measures the material above it.

Every branch also obeys $T - pX = \tau$ with $p = 1/v_k$ constant along the
branch, which is the identity taken up in [03](03-tau-p.md).

## 3. The travel-time curve of a stack

Sort all arrivals at each surface offset and keep the earliest: that is the
**first-arrival travel-time curve** of the model. Near the source the direct wave
through layer 1 wins; beyond the crossover distance the first head-wave branch
takes over, and each deeper interface can in principle produce a later crossover.
The demonstration builds exactly this curve from the closed-form branches and
prints the branch parameters:

| interface | $v$ along (km s⁻¹) | critical offset $X_c$ (km) | intercept $\tau$ (s) | slope $1/v$ (s km⁻¹) | measured slope (s km⁻¹) |
|---|---|---|---|---|---|
| 1 | 6.5000 | 24.0000 | 0.641026 | 0.153846 | 0.153846 |
| 2 | 7.0000 | 66.6780 | 2.000476 | 0.142857 | 0.142857 |
| 3 | 8.0000 | 75.3617 | 4.279331 | 0.125000 | 0.125000 |

Both the intercepts and the slopes are *measured* from the constructed curve by
the demonstration, then compared with the closed forms above. The measured slope
of every branch equals $1/v_k$ to six decimals, and the intercepts agree with
$2\sum h_i\cos\theta_i/v_i$ exactly — for interface 2,
$0.858465 + 1.142011 = 2.000476$ s. Snell's law has been used, and this table is
the list of its consequences.

For interface 2 the demonstration also reports $T - pX$ over the whole branch:
its minimum and maximum are both $2.0004761109$ s and its difference from the
constructed intercept is $1.332\times10^{-15}$ s — machine precision. The
quantity that the construction calls "intercept time" is literally the
$p$-invariant of the branch.

**The crossover distance.** Between the direct wave $T = X/v_1$ and the
interface-1 head wave $T = X/v_2 + \tau_1$, the crossover solves

$$X\left(\frac{1}{v_1} - \frac{1}{v_2}\right) = \tau_1
\quad\Longrightarrow\quad
X = 2h_1\sqrt{\frac{v_2 + v_1}{v_2 - v_1}} ,$$

which for $h_1 = 5$ km, $v_1 = 6.00$, $v_2 = 6.50\ \mathrm{km\,s^{-1}}$ is exactly
$2(5)\sqrt{12.5/0.5} = 50.0$ km. Beyond 50 km the head wave is the first arrival,
which is why crustal refraction surveys are laid out at tens of kilometres of
offset — and why the geometry of the survey, not the physics, decides which
layers are seen.

## 4. Hidden layers, and the asymmetry of non-detection

If $v_2 < v_1$ the head wave from interface 1 does not exist: the critical angle
has no real solution, because $\sin i_c = v_1/v_2 > 1$. No ray can run along the
interface, no arrival is generated, and the interface is **hidden**. The direct
wave remains the fastest arrival from that depth range no matter what offset is
used. Adding a further, faster layer does not rescue the hidden one: the deeper
branch carries information about the *total* thickness above it, not about how
that thickness is partitioned.

The demonstration makes this concrete with a synthetic low-velocity stack
($6.00\ \mathrm{km\,s^{-1}}$ for 10 km, then $5.70\ \mathrm{km\,s^{-1}}$ for 10 km,
then $6.50\ \mathrm{km\,s^{-1}}$, over a $7.50\ \mathrm{km\,s^{-1}}$ half space):
interface 1 produces `nan` for both critical offset and intercept, while
interfaces 2 and 3 produce offsets of $84.4905$ and $84.7980$ km and intercepts of
$2.968475$ and $5.815471$ s. The word `nan` in the table is the physics, not a
numerical failure — it is the statement that the wave family does not exist.

This is the asymmetry that makes layered inversion an *interpretation*: the
presence of a branch proves a velocity increase; its absence proves nothing at
all, because it is equally consistent with no interface, with a small velocity
decrease, and with a large one.

## 5. Worked examples

### Example 1 — intercept time and critical offset for interface 2, by hand

With $p = 1/v_3 = 1/7.00 = 0.142857\ \mathrm{s\,km^{-1}}$:

1. **Layer 1:** $\sin\theta_1 = p v_1 = 0.142857 \times 6.00 = 0.857143$, so
   $\theta_1 = 58.9973^\circ$ and $\cos\theta_1 = 0.515079$. Contribution to
   $\tau$: $2(5.00)(0.515079)/6.00 = 0.858465$ s.
2. **Layer 2:** $\sin\theta_2 = 0.142857 \times 6.50 = 0.928571$, so
   $\theta_2 = 68.2132^\circ$ and $\cos\theta_2 = 0.371154$. Contribution:
   $2(10.00)(0.371154)/6.50 = 1.142011$ s.
3. $\tau_2 = 0.858465 + 1.142011 = 2.000476$ s — the number in the table.
4. Critical offset: the legs are $h_1\tan\theta_1 = 8.3205$ km and
   $h_2\tan\theta_2 = 25.0185$ km, so
   $X_c = 2(8.3205 + 25.0185) = 66.6780$ km, matching the table.

The same geometry is computed a second way in the demonstration, from the ray
angles rather than from the slowness integral, for interface 3 with
$p = 1.250000\times10^{-4}\ \mathrm{s\,m^{-1}}$: the layer angles are
$48.590378^\circ$, $54.340912^\circ$ and $61.044976^\circ$, the one-way legs are
$5.669467$, $13.937463$ and $18.073922$ km, and twice their sum is $75.361705$ km,
identical to the critical offset from the slowness integral to
$1.455\times10^{-14}$ km. Two routes, one geometry.

### Example 2 — inverting a measured branch

A branch on a record section is fitted as $T = X/7.05 + 2.0005$ s with $X$ in
kilometres. The slope gives $v_3 = 7.05\ \mathrm{km\,s^{-1}}$, but the intercept
does not by itself give two thicknesses: it gives $2h_1\cos\theta_1/v_1 +
2h_2\cos\theta_2/v_2$ with $\theta_1$, $\theta_2$ depending on $p = 1/7.05$, and
$h_1$ and $h_2$ entering only through that combination. Unless $v_1$ and $v_2$
are known from other branches, one measured intercept constrains one *sum*, not
the individual depths. Layered refraction is a chain: each branch is inverted
using the velocities obtained from all shallower branches, so an error in the
shallowest velocity propagates into every depth below.

### Example 3 — how thickness and velocity uncertainty reach a depth

The demonstration puts stated uncertainties on the first interface
($h_1 = 5.00$ km, $v_1 = 6.00\ \mathrm{km\,s^{-1}}$, $v_{\text{along}} = 6.50\
\mathrm{km\,s^{-1}}$, true intercept $0.641026$ s) and runs 4000 realisations with
$\sigma_h = 0.25$ km and $\sigma_v = 0.10\ \mathrm{km\,s^{-1}}$ (1.67 % of $v_1$):

- modelled intercept: $0.639342 \pm 79.349$ ms;
- depth recovered by inverting with the *nominal* $v_1$:
  $4.9869 \pm 0.6189$ km against a true 5.00 km;
- the velocity error alone moves the inverted depth from 5.000 km to 4.416 km
  ($-0.584$ km), while the thickness error alone contributes 0.250 km;
- the combined scatter, $0.6189$ km, is $2.48$ times the thickness error that was
  put in.

The two contributions add in quadrature, and the *smaller relative* input — a
1.67 % velocity error — produces the *larger* depth error. A depth obtained from
a travel time is never better determined than the velocity model used to convert
the time into a distance. This is the same trade-off, in a different setting,
that the receiver-function module confronts in
[06-08 Receiver Functions and Crustal Structure](../08-receiver-functions-and-crustal-structure/README.md).

## 6. Assumptions and the regime of validity

1. **Flat, parallel, horizontal interfaces.** Dipping layering changes both the
   apparent velocities and the geometry: on a dip line, the slope of a branch
   gives $1/v$ only if the dip is known or removed by shooting in opposite
   directions.
2. **Constant velocity within each layer.** A real layer with a gradient will
   produce a curved, not straight, branch — the curve is information, but it
   cannot be read with the straight-line formulas above. Gradients must be
   handled by integrating $\eta(z)$, as in [04](04-ray-tracing.md).
3. **Ray theory's high-frequency limit.** The head wave is an interference
   phenomenon; the ray construction describes its *arrival time* correctly but
   not its amplitude, and the construction fails outright when the layer is thin
   compared with a wavelength.
4. **Two-dimensional geometry (a line), isotropic velocities.** Out-of-plane
   offsets and anisotropy both break the relation $p = \sin i / v$.
5. **Only first arrivals are inverted.** As Section 4 shows, this is a
   *selection* effect, and its consequence is that low-velocity layers are
   invisible to the method.

## 7. A grid method sees the same model differently

The demonstration also solves the same layered model on a fine grid with a
Dijkstra-style first-arrival calculation and compares it with the branches.

On the direct branch the two agree to machine precision (relative differences
$10^{-15}$ to $10^{-14}$), which is a check that both are computing the same
$X/v_1$. At 60 km they disagree by $1.299\times10^{-2}$: the branches return the
head wave at $9.871795$ s while the grid returns the direct arrival at $10.000000$ s
and has *missed* the head wave entirely.

The cause is measurable and worth understanding. The head-wave leg descends the
5 km first layer at the critical angle $67.38^\circ$, i.e. over about 12 km of
horizontal offset. An eight-neighbour grid can only realise that trajectory as a
staircase of axis-aligned steps, which over-estimates the leg by **30.5 %**;
twice that penalty exceeds the 0.129 s advantage the head wave holds over the
direct arrival at 60 km, so the coarse grid loses it. Grid methods have a
resolution-dependent bias that is largest for arrivals travelling at a shallow
angle to an interface — exactly the arrivals refraction methods depend on. For a
layered model, the closed-form branches are exact and should be used instead.

## 8. Python demonstration

`code/snell_and_layering_demo.py` prints five labelled sections with units:

1. **Snell's law and the head-wave branches** — the table of Section 3, with
   measured slopes and intercepts against their closed forms.
2. **The intercept time is the tau-p intercept** — the $T - pX$ invariance of a
   branch ($1.332\times10^{-15}$ s).
3. **Ray geometry rebuilt from the angles** — the angles and legs of Example 1.
4. **The first arrival against a grid calculation** — machine-precision agreement
   on the direct branch, and the lost head wave at 60 km.
5. **How thickness and velocity uncertainty reach the depth** — the Monte Carlo
   of Example 3.

```bash
cd 06-seismology/02-ray-theory-and-travel-times/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python snell_and_layering_demo.py
```

## Mastery checkpoint

Complete this without notes:

> A three-layer model has $v_1 = 5.60$, $v_2 = 6.20$, $v_3 = 6.90\
> \mathrm{km\,s^{-1}}$ with $h_1 = 2.0$ km, $h_2 = 8.0$ km. **(a)** Compute the
> critical angle at interface 1 and state whether a head wave exists there.
> **(b)** Compute the intercept time of the interface-1 branch. **(c)** At what
> offset does it become the first arrival? **(d)** A colleague reports the same
> intercept for interface 1 but suggests $v_1 = 6.20\ \mathrm{km\,s^{-1}}$;
> recompute the implied $h_1$ and state the percentage change. **(e)** Explain in
> one sentence why no branch from a hypothetical $5.2\ \mathrm{km\,s^{-1}}$ layer
> between 2 and 10 km could appear on the record.

A worked version of (a)–(c) appears in the lesson
[solutions](exercises/02-snell-and-layering-solutions.md).

## Common pitfalls

1. **Reading a depth from an intercept without stating the velocities above it.**
   The intercept fixes a sum weighted by angles that depend on $p$; it is not a
   depth.
2. **Using the straight-line branch formulas on a gradient.** A gradient gives a
   curved branch; forcing a line through it produces a fictitious layer.
3. **Interpreting the absence of a branch as the absence of an interface.** It is
   a one-sided constraint, and a low-velocity layer produces exactly this silence.
4. **Forgetting that the slope gives the velocity along the refractor, not in it.**
   The refractor's own velocity is what the branch slope measures; the layers
   above only contribute to the intercept.
5. **Trusting a grid solution for shallow-angle arrivals.** As Section 7 shows,
   the staircase bias is worst exactly there; use the closed forms for layered
   models.
6. **Quoting a depth to three digits when the velocity above it is uncertain by
   two.** Example 3 is the arithmetic of that mistake.

## Related modules

- [06-01 Elastic Wave Propagation](../01-elastic-wave-propagation/README.md) —
  the wave physics behind the head wave, and the reflection and transmission
  coefficients this lesson deliberately avoids needing.
- [01 Eikonal Equation, Rays and Fermat's Principle](01-eikonal-and-rays.md) —
  the parent theory; this lesson is its layered special case.
- [03 The tau-p Transform and Intercept Time](03-tau-p.md) — the same branches
  turned into intercept functions and inverted by regression.
- [05 Shadow Zones, Triplications and the Low-Velocity Zone](05-shadow-zones.md) —
  the hidden-layer mechanism at the scale of the whole Earth.
- [06-10 Refraction and Near-Surface Seismology](../10-refraction-and-near-surface-seismology/README.md) —
  the same mathematics applied to engineering-scale surveys.
- [06-04 Earthquake Location and Magnitude](../04-earthquake-location-and-magnitude/README.md) —
  where these travel-time curves are used to locate events.

## Exercises

Full sets with worked solutions are in
[`exercises/02-snell-and-layering-exercises.md`](./exercises/02-snell-and-layering-exercises.md)
and
[`exercises/02-snell-and-layering-solutions.md`](./exercises/02-snell-and-layering-solutions.md).
