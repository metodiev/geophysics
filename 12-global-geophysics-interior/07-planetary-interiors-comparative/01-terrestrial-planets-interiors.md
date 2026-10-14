---
id: 12-07-01
title: "Interiors of Mars, Venus, Mercury and the Moon"
level: doctoral
prereqs: ["12-01-02", "12-06-01", "04-08-02"]
tags: [global-geophysics, earth-interior, planetary-interiors, comparative-planetology, scaling, moment-of-inertia]
---

# Interiors of Mars, Venus, Mercury and the Moon

> All models and data in this module are **SYNTHETIC**. The bodies here are
> dimensionless teaching bodies obtained by scaling one interior structure; they
> are *not* Mars, Venus, Mercury or the Moon, and no number below is a
> measurement of any of them. Externally quoted quantities are the exact
> constant $G$ and exact mathematical results.

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** why comparative interior studies are organised around
   dimensionless numbers rather than around absolute pressures or temperatures.
2. **Derive** the central pressure of a uniform self-gravitating sphere and
   **obtain** it for layered bodies by quadrature, verifying both against each
   other.
3. **Form** the dimensionless central pressure $\Pi = P_{c}R^{4}/(GM^{2})$,
   **show** that it is invariant under a change of scale for a fixed interior
   structure, and **measure** the exponents in the mass and the radius.
4. **Invert** an adopted moment-of-inertia factor into a family of (core size,
   density contrast) models, and **state** precisely what the family assumption
   contributes to the answer.
5. **Add** a figure observable and **show** how a second observable narrows the
   family, and **identify** which ambiguity is left over (the parameterisation).
6. **Scale** the surface-to-volume ratio and the compression parameter
   $P_{c}/K$, and **state** the size at which the constant-density scaling
   argument stops being respectable.
7. **Compare** two bodies in the dimensionless numbers, and **say** which
   differences are physics and which are size.

## Prerequisites

- [12-01-02 Crustal Structure and Continental vs Oceanic Crust](../01-seismic-structure-of-the-earth/02-crustal-structure.md) —
  the shell that dominates the moment of inertia of a small body.
- [12-06-01 Moment of Inertia, Figure and Interior Constraints](../06-geodesy-constraints-interior/01-moment-of-inertia.md) —
  the inertia functional, the two-layer ridge, and the figure solver used here.
- [04-08-02 Planetary Interiors and Magnetic Fields](../../04-earth-science-geology/08-planetary-science/02-planetary-interiors.md) —
  the descriptive counterpart: what is known about each body and how.

## 1. Why comparison is a method

A planet is not an experiment. There is no way to hold one body's mass fixed
while varying its rotation, and no way to repeat a formation history. What a
comparative study does instead is to use the *scaling* of interior physics to
separate effects that are otherwise entangled:

- effects that depend on **size** (pressure, gravity, surface-to-volume ratio,
  cooling time);
- effects that depend on **composition** (density, equation of state, melting
  point);
- effects that depend on **history** (the figure, the internal temperature,
  whether a dynamo still runs).

The method has a sharp requirement: the comparison must be made in numbers that
have no units, because a body twice as massive and twice as large has four times
the central *pressure* while being in an arguably similar *state*. This lesson
builds those numbers from scratch and shows where they stop being reliable.

Two rules follow, and they are the honest content of the lesson:

1. **Scale before comparing.** If two bodies differ in the dimensionless numbers
   of §3, the difference is physics; if they agree, the difference is size.
2. **State the family.** Every inversion below is performed inside a
   parameterised family of structures. The parameterisation is an assumption,
   and §4 and §5 measure what it is worth.

## 2. The interior as a differential equation

Static hydrostatic equilibrium of a spherically symmetric body is

$$
\frac{\mathrm{d}P}{\mathrm{d}r} = -\rho(r)\,\frac{GM(r)}{r^{2}},
\qquad
\frac{\mathrm{d}M}{\mathrm{d}r} = 4\pi r^{2}\rho(r).
$$

For **uniform** density this integrates in closed form. With
$M(r) = \tfrac43\pi\rho r^{3}$,

$$
\frac{\mathrm{d}P}{\mathrm{d}r} = -\frac{4\pi G\rho^{2}}{3}r
\qquad\Longrightarrow\qquad
P_{c} = \frac{4\pi G\rho^{2}}{3}\int_{0}^{R}r\,\mathrm{d}r
= \frac{2}{3}\pi G\rho^{2}R^{2},
$$

which in terms of the mass is the exact constant

$$
P_{c} = \frac{3}{8\pi}\frac{GM^{2}}{R^{4}}
\qquad\Longrightarrow\qquad
\Pi_{\text{uniform}} = \frac{P_{c}R^{4}}{GM^{2}} = \frac{3}{8\pi} = 0.119366 .
$$

The demonstration verifies the closed form against a quadrature of
$\mathrm{d}P/\mathrm{d}r$:

```text
  SYNTHETIC uniform body: rho = 4000 kg/m^3, R = 3.0e+06 m, M = 4.524e+23 kg
     closed form 2.0129e+10 Pa
     integration 2.0136e+10 Pa   (difference 0.035 %)
     in GPa: 20.13 GPa
```

and reproduces the constant:

```text
     3/(8 pi) = 0.119366   quadrature gives 0.119408
```

The quadrature is a discrete sum over shells, so a $3\times10^{-4}$ relative
error is expected and is reported rather than hidden. For a layered body no
closed form exists, and the quadrature is the tool for everything that follows.

## 3. The dimensionless interior

Define

$$
\Pi \equiv \frac{P_{c}R^{4}}{GM^{2}} .
$$

For a fixed interior *structure* — a fixed set of structure numbers such as the
core radius fraction and the density contrast — $\Pi$ is a pure number independent
of the mass and the radius. The demonstration tests this directly by scaling one
two-layer structure to four very different bodies:

```text
   M (kg)      R (m)     P_c (Pa)      Pi = P_c R^4/(G M^2)
   3.00e+23   2.40e+06     3.4179e+10         0.188778
   6.00e+23   3.00e+06     5.5998e+10         0.188778
   6.00e+24   6.00e+06     3.4999e+11         0.188778
   6.00e+25   9.50e+06     5.5688e+12         0.188778
```

The invariance is exact to the printed digits, and it is the whole basis of
comparative work: the *state* of a body with a given structure is a pure number,
and only $GM^{2}/R^{4}$ sets the magnitudes. Measured exponents confirm the
dependence:

```text
     d ln P_c / d ln M =  2.000   (two)
     d ln P_c / d ln R = -4.000   (minus four)
```

which is exactly $P_{c}\propto GM^{2}/R^{4}$. A body twice as massive and twice
as large has the same $\Pi$ and one quarter of the central pressure.

*Worked example.* Compare a body with $M = 4.0\times10^{23}$ kg,
$R = 3.0\times10^{6}$ m, $x_{\text{core}} = 0.4$, $\alpha = 1.8$ with a body of
ten times the mass and twice the radius, holding the structure fixed.
The first has $\Pi = 0.1888$ (from the table above at the nearest structure).
For the second, $P_{c} = \Pi\,GM^{2}/R^{4} = 0.1888\times6.674\times10^{-11}
\times(4\times10^{24})^{2}/(6\times10^{6})^{4}$, i.e.
$P_{c} = 0.1888 \times 6.674\times10^{-11}\times1.6\times10^{49}/1.296\times10^{27}
= 1.56\times10^{11}$ Pa. The measured scaling $P_{c}\propto M^{2}R^{-4}$ predicts
the ratio $(10)^{2}/(2)^{4} = 100/16 = 6.25$; the first body's
$2.33\times10^{10}$ Pa times 6.25 is $1.46\times10^{11}$ Pa. The two estimates
differ by about 6% because the structures are not identical (the first body has
$x_{\text{core}} = 0.4$, $\alpha = 1.8$; the table's $\Pi$ belongs to
$x_{\text{core}} = 0.5$, $\alpha = 2.0$). The lesson: **the exponents are exact
for a fixed structure; the constant is not.**

## 4. The inverse problem: an inertia factor is a curve

Adopt the synthetic constraint $C/MR^{2} = 0.3350$ for a body with
$M = 4.0\times10^{23}$ kg and $R = 3.0\times10^{6}$ m, and solve for the density
contrast at each core size:

```text
   x_core    alpha required   core rho (kg/m^3)   mean rho (kg/m^3)
    0.10         197.3746          583487.7             3536.8
    0.20          26.4702           77772.2             3536.8
    0.30           9.0515           26296.6             3536.8
    0.40           4.7477           13543.2             3536.8
    0.50           3.2128            8900.9             3536.8
    0.60           2.5755            6796.2             3536.8
```

Exactly as in
[12-06-01](../06-geodesy-constraints-interior/01-moment-of-inertia.md): the observable is a curve, not a point. Two
details are specific to the comparative setting.

- The **mean density is the same in every row**, because mass and radius are
  fixed. The mean density is a *measured* quantity for a body with a known mass
  and radius; the core density is not.
- The required core density becomes absurd for small cores (a core of one tenth
  of the radius needs a density two orders of magnitude above the mean). This is
  how a *physically admissible* range replaces an arbitrary one, and it is the
  only place where mineral physics enters the inversion: it says what densities
  are available.

## 5. Adding the figure: two observables, and what is left

A hydrostatic body also has a figure, and the fluid Love number
$k_{f} = 3J_{2}/q$ is a second functional of the same profile. The demonstration
computes both along the ridge and then uses $k_{f}$ as a second data point:

```text
   x_core    alpha required    C/MR^2     J2/q      k_f
    0.20           26.4702    0.3350    0.3307     0.9922
    0.30            9.0515    0.3350    0.3265     0.9794
    0.40            4.7477    0.3350    0.3231     0.9694
    0.50            3.2128    0.3350    0.3212     0.9636
    0.60            2.5755    0.3350    0.3202     0.9607
  SYNTHETIC measured k_f = 0.9888.  Closest models on the ridge:
     x_core = 0.20  k_f = 0.9922   |k_f - measured| = 0.0034   <-- closest
     x_core = 0.30  k_f = 0.9794   |k_f - measured| = 0.0094
```

The pair $(C/MR^{2}, k_{f})$ selects one row inside the two-layer family. That is
genuine progress, and the demonstration also shows the *check* that makes it
believable: the same solver returns $C/MR^{2} = 0.4000$, $J_{2}/q = 0.4979$ and
$k_{f} = 1.4938$ for a homogeneous body against the exact small-rotation values
$0.4$, $0.5$ and $1.5$. Without that calibration the ridge inversion would be
unverifiable.

The residual ambiguity is no longer in the data: it is in the assumption that
the body consists of two uniform layers. A graded envelope, a density
discontinuity elsewhere, or a light layer at the top all reproduce two numbers
and differ in what they imply about composition.

## 6. Thermal and compression scaling, and where scaling stops

Two dimensionless arguments dominate comparative thermal discussions.

**Surface-to-volume.** For a given heat production per unit mass, the cooling
rate scales with $S/V = 3/R$:

```text
   R (m)        S/V (1/m)     ratio to R = 6.4e6 m
   6.40e+06     4.6875e-07             1.00
   3.00e+06     1.0000e-06             2.13
   1.70e+06     1.7647e-06             3.76
   1.00e+06     3.0000e-06             6.40
```

A body half the size loses heat twice as fast per unit mass, all else equal.
That is the scaling behind the qualitative statement that small bodies cool and
die while large ones stay active — but "all else equal" is doing the work, and
radiogenic inventory, insulation and tidal heating are not equal.

**Compression.** The relevant dimensionless measure is the central pressure over
a relevant elastic modulus, $P_{c}/K$:

```text
   R (m)      M (kg)      P_c (Pa)     P_c/K
   3.00e+06   4.00e+23     2.3264e+10     0.1790
   6.00e+06   4.00e+24     1.4540e+11     1.1185
```

With a synthetic $K = 1.3\times10^{11}$ Pa, the larger body is compressed by
more than a factor of one at its centre: a constant-density scaling is no longer
respectable for it, and the dimensionless numbers of §3 drift with the interior
as the equation of state takes over. **This is the boundary of the method in this
lesson**: the scaling arguments are exact statements about structure, and they
degrade continuously as self-compression becomes important.

## 7. Assumptions and regime of validity

| Assumption | Where it enters | Failure mode |
|---|---|---|
| Spherical symmetry and hydrostatic equilibrium | §§2–3 | A fossil figure or a large lateral heterogeneity |
| Piecewise-uniform layers | §4, §5 | Graded structures: the ridge becomes a wider family |
| Two observables, two parameters | §5 | With three parameters the answer is a curve again |
| Hydrostatic figure ($k_{f}$ usable) | §5 | A body whose figure is partly fossil |
| Constant density for the scaling arguments | §6 | Bodies large enough that $P_{c}/K \gtrsim 0.1$ |
| One equation of state for all depths | §2 | Real bodies have phase transitions, which appear as density jumps *not* put in by hand |

The last row deserves emphasis: in a real body the density discontinuities are
*outputs* of mineral physics, not free parameters. A comparative study that
treats the core radius as a free parameter is therefore exploring a family that
mineral physics may already have excluded — and the excluded part is the part
with the small dense cores that the ridge of §4 requires at small $x$.

## 8. Python demonstration

[`code/terrestrial_planets_interiors_demo.py`](code/terrestrial_planets_interiors_demo.py):

1. central pressure: closed form for a uniform sphere against quadrature;
2. $\Pi$ invariance under scaling, with the mass and radius exponents measured;
3. the moment-of-inertia ridge;
4. the figure observable $k_{f} = 3J_{2}/q$ along the ridge, and the two-observable
   selection;
5. the surface-to-volume and compression scalings.

```bash
cd 12-global-geophysics-interior/07-planetary-interiors-comparative/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python terrestrial_planets_interiors_demo.py
```

## 9. Exercises

[`exercises/01-terrestrial-planets-interiors-exercises.md`](exercises/01-terrestrial-planets-interiors-exercises.md)
and the worked
[`exercises/01-terrestrial-planets-interiors-solutions.md`](exercises/01-terrestrial-planets-interiors-solutions.md).

## Mastery checkpoint

Without notes:

> **(a)** A body has $M = 2.0\times10^{23}$ kg and $R = 2.4\times10^{6}$ m.
> Using $\Pi = 0.1888$ for its structure class, compute its central pressure.
> **(b)** Give the central pressure of a body with the same structure, twice the
> mass and 1.5 times the radius, and state which of the two is more compressed
> for the same $K$.
> **(c)** An adopted $C/MR^{2} = 0.3400$ is matched by $x_{\text{core}} = 0.4$
> with some $\alpha$. Explain why $x_{\text{core}} = 0.2$ also works, and state
> one physical requirement that would exclude it.
> **(d)** You are given $M$, $R$, $C/MR^{2}$ and $k_{f}$ with 1% errors. State
> what is determined, what remains a family, and why.

A worked version of (a)–(b) appears in the lesson-01
[solutions](exercises/01-terrestrial-planets-interiors-solutions.md).

## Common pitfalls

1. **Comparing absolute pressures between bodies of different size.** Convert
   to $\Pi$ first; otherwise size is mistaken for composition.
2. **Using the exponents as constants.** $P_{c}\propto M^{2}R^{-4}$ holds at
   fixed structure; the dimensionless constant changes with the structure.
3. **Quoting a core density from an inertia factor.** §4 produces a curve, and
   only mineral physics narrows it.
4. **Treating $k_{f}$ as a measurement when the figure may not be hydrostatic.**
   A fossil figure contaminates the second observable as well.
5. **Forgetting the calibration.** A figure solver that never reproduces the
   homogeneous values $0.4$, $0.5$, $1.5$ is not a verified solver.
6. **Applying a scaling argument where the body is self-compressed.** Check
   $P_{c}/K$ before using constant-density reasoning.

## Related modules

- [04-08-02 Planetary Interiors and Magnetic Fields](../../04-earth-science-geology/08-planetary-science/02-planetary-interiors.md) —
  the descriptive account of what each body is like; this lesson supplies the
  scaling tools it assumes.
- [06-13-01 Planetary Seismology: InSight and Lunar Seismic Experiments](../../06-seismology/13-planetary-and-exploration-seismology/01-planetary-seismology.md) —
  the observation that removes the last ambiguity of §4: a seismic radius of a
  core is a direct measurement of $x$.
- [12-07-02 Icy Moons, Subsurface Oceans and Induction Studies](02-icy-moons.md) —
  the same comparative logic applied to a layer that gravity cannot see.
- [12-07-03 Giant Planet Interiors and Magnetic Fields](03-giant-planets.md) —
  where the compression of §6 becomes the dominant physics rather than a
  correction.
- [12-06-01 Moment of Inertia, Figure and Interior Constraints](../06-geodesy-constraints-interior/01-moment-of-inertia.md) —
  the machinery this lesson compares.
