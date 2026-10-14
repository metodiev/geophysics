---
id: 07-01-03
title: "Reference Ellipsoid, Normal Gravity and Clairaut's Theorem"
level: graduate
prereqs: ["07-01-02", "02-08-05", "02-08-03"]
tags: [gravity, geodesy, normal-gravity, reference-ellipsoid, clairaut, somigliana, j2]
---

# Reference Ellipsoid, Normal Gravity and Clairaut's Theorem

**All models and data in this module are SYNTHETIC.** The only exact quantities
used here are the four WGS84 defining constants
($a = 6\,378\,137\ \mathrm{m}$, $f = 1/298.257223563$,
$GM = 3.986004418\times10^{14}\ \mathrm{m^{3}\,s^{-2}}$,
$\omega = 7.292115\times10^{-5}\ \mathrm{rad\,s^{-1}}$) and
$G = 6.67430\times10^{-11}\ \mathrm{m^{3}\,kg^{-1}\,s^{-2}}$. Every gravity value
in this lesson is *computed* from those four numbers by the formulas derived
below.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the ellipsoid parameters $b$, $e^{2}$, $e'^{2}$ and the rotation
   parameter $m$ from the four defining constants of a reference ellipsoid.
2. **Derive** the first-order relations between the flattening $f$, the dynamic
   form factor $J_2$ and $m$ by imposing that the ellipsoid is a level surface,
   and **state** at what order that derivation breaks down.
3. **Distinguish** the *normal potential* (a mathematical construction with an
   exactly ellipsoidal level surface) from the real gravity field, and explain
   why "normal" and "anomaly" are always defined as a pair.
4. **Compute** normal gravity at the equator and the pole from the closed forms
   involving $q_0$ and $q_0'$, and **evaluate** Somigliana's formula at any
   latitude.
5. **State and verify** Clairaut's theorem $\beta + f = \tfrac52 m$, and
   **quantify** the error of the first-order theory it belongs to.
6. **Compute** the latitude correction in $\mathrm{mGal\,km^{-1}}$ and the
   free-air gradient in $\mathrm{mGal\,m^{-1}}$, and **explain** why the
   latitude dependence of the free-air coefficient is small but not zero.
7. **State** the regime of validity of the normal field, including the
   hydrostatic assumption and the meaning of a "conventional" gravity formula.

## Prerequisites

- [07-01-02 Gravitational Potential, Equipotentials and the Geoid](02-gravity-potential.md)
  — the gravity potential $W$, level surfaces, the rotation parameter $m$ and the
  first-order flattening relations used here.
- [02-08-05 Equipotentials](../../02-physics/08-potential-theory/05-equipotentials.md)
  — why a fluid surface must be an equipotential.
- [02-08-03 Spherical Harmonics](../../02-physics/08-potential-theory/03-spherical-harmonics.md)
  — the $P_{2}$ Legendre polynomial and the coefficient $J_2$.

## 1. Why a reference field is needed

An anomaly is a difference. Before it can be computed, someone must decide what
to subtract, and the reference must be (i) computable everywhere, (ii) smooth, and
(iii) as close as possible to the real field so that the residual stays small.
The construction that satisfies all three is the **normal field**: the gravity
field of a rotating, homogeneous-in-shape *level ellipsoid* with a specified mass,
rotation rate and dynamical flattening.

The word **normal** is doing two jobs at once, and both matter.

- *Normal* as in *perpendicular*: at every point of the ellipsoid the normal field
  is exactly perpendicular to the ellipsoid, because the ellipsoid is one of its
  level surfaces by construction. This is what makes ellipsoidal coordinates and
  height systems tractable (module [04](../04-geodesy-reference-frames/README.md)).
- *Normal* as in *standard*: the normal field is a **convention**. Two countries
  can adopt different ellipsoids and obtain different anomalies from the same
  measurements. The anomaly is a difference of two fields, so it inherits the
  arbitrariness of the reference — a point the exercises test directly.

## 2. The reference ellipsoid in four numbers

A rotating ellipsoid of revolution that is a level surface of its own gravity
potential is fixed by **four** constants. Any convenient set works; the WGS84 set is

$$a,\qquad f,\qquad GM,\qquad \omega,$$

where $a$ is the semi-major axis, $f$ the flattening, $GM$ the geocentric
gravitational constant and $\omega$ the angular rotation rate. From these, in the
demonstration's arithmetic:

$$b = a(1-f) = 6\,356\,752.314\ \mathrm{m},$$

$$e^{2} = f(2-f) = 6.694379990\times10^{-3},$$

$$e'^{2} = \frac{e^{2}}{1-e^{2}} = 6.739496742\times10^{-3}
\qquad\text{(second eccentricity squared)},$$

$$m \equiv \frac{\omega^{2}a^{2}b}{GM} = 3.449786507\times10^{-3}
\qquad\text{(rotation parameter)}.$$

Note what is *not* in the list: $J_2$ is **derived**, not defining. In the system
of four constants above, $J_2$ follows from the requirement that the ellipsoid be
a level surface, and the closed form is

$$J_2 = \frac{e^{2}}{3}\left(1 - \frac{2}{15}\frac{m\,e'}{q_0}\right),
\qquad q_0 = \frac12\left[\left(1 + \frac{3}{e'^{2}}\right)\arctan e'
- \frac{3}{e'}\right],$$

which evaluates to $J_2 = 1.082629821\times10^{-3}$. The demonstration also
computes a *second*, independent closed-form constant,

$$q_0' = 3\left(1 + \frac{1}{e'^{2}}\right)
\left(1 - \frac{\arctan e'}{e'}\right) - 1 = 2.688041300\times10^{-3},$$

which appears in the surface-gravity expressions of Section 4. The functions
$q_0$ and $q_0'$ are not arbitrary: they are the values of the auxiliary function

$$q(u) = \frac12\left[\left(1 + \frac{3u^{2}}{E^{2}}\right)
\arctan\frac{E}{u} - \frac{3u}{E}\right]$$

and its derivative at the ellipsoid surface, and they arise from integrating the
potential of an ellipsoidal shell. The honest summary: **the closed form exists,
it is algebra, and it is what makes the normal field computable to nine digits.**

## 3. The normal potential and its level surfaces

Write the geodetic potential of the rotating normal body as

$$W(r,\varphi) = \frac{GM}{r}\left[1 - J_2\left(\frac{a}{r}\right)^{2}
P_2(\sin\varphi) - J_4\left(\frac{a}{r}\right)^{4}P_4(\sin\varphi) - \cdots
\right] + \tfrac12\omega^{2}r^{2}\cos^{2}\varphi,$$

with $P_2$ the Legendre polynomial. The normal potential is defined as the
potential whose *external* field is exactly that of the level ellipsoid, which is
available in a closed form (the Pizzetti–Somigliana expression) rather than as a
truncated series; the series above is its harmonic expansion, and even in principle
it has infinitely many terms. Lesson [02](02-gravity-potential.md) measured what
truncation costs: retaining only $J_2$ leaves a level-surface residual of
$3.46\times10^{-3}$ of $W$ on the ellipsoid — the same order as $f$. Since $J_4$
is of order $f^{2}$ relative, the practical rule is:

$$J_{2k} = O(f^{k}) \quad\text{in relative size,}$$

so a field accurate to $10^{-9}$ relative (a microgal) needs harmonics out to
$k = 3$ in the series, or the closed form.

### 3.1 The level-surface condition to first order

Impose $W = \text{const}$ on the surface $r(\varphi) = a\left(1 - f\sin^{2}\varphi
\right)$, keeping terms to first order in $f$, $m$ and $J_2$. Expanding
$1/r \approx (1/a)\left(1 + f\sin^{2}\varphi\right)$ and
$\left(a/r\right)^{2} \approx 1 + 2f\sin^{2}\varphi$, and using
$P_2(\sin\varphi) = \tfrac12\left(3\sin^{2}\varphi - 1\right)$ and
$\cos^{2}\varphi = 1 - \sin^{2}\varphi$, the terms of the potential that are not
constant combine into

$$\frac{GM}{a}\Big[f - \tfrac{3}{2}J_2\Big]\sin^{2}\varphi
- \tfrac12\omega^{2}a^{2}\sin^{2}\varphi + \text{(constant)} = 0 .$$

For this to hold at every latitude the coefficient of $\sin^{2}\varphi$ must
vanish:

$$\boxed{\;f = \tfrac{3}{2}J_2 + \tfrac{1}{2}m
\qquad\Longleftrightarrow\qquad
J_2 = \tfrac{2}{3}f - \tfrac{1}{3}m\;}$$

where $m \approx \omega^{2}a^{2}/GM$ to the same order. Numerically:
$\tfrac32 J_2 + \tfrac12 m = 3.348837985\times10^{-3}$ against the defining
$f = 3.352810665\times10^{-3}$, a relative difference of $-1.18\times10^{-3}$ —
that residual is the size of the second-order terms, and it is *larger* than
1 microgal, so the first-order relation is a consistency check and not a
substitute for the closed form.

Physically the condition says: **shape, rotation and mass distribution are not
independent**. A planet that rotates faster must either flatten more or
concentrate its mass, and the two responses are different in kind. The
demonstration's rotating-planet exercise shows what happens when the assumption
fails.

## 4. Normal gravity at the equator and the pole

Differentiating $W$ and evaluating at the ellipsoid surface gives the surface
gravity. Keeping first order in $f$, $J_2$ and $m$:

$$\gamma_{e} \approx \frac{GM}{a^{2}}\left(1 + \frac{3}{2}J_2 - m\right),
\qquad
\gamma_{p} \approx \frac{GM}{a^{2}}\left(1 + 2f - 3J_2\right).$$

Inserting numbers (with $J_2$ from the first-order relation) predicts
$\gamma_{e} = 9.780434286\ \mathrm{m\,s^{-2}}$ and
$\gamma_{p} = 9.832087472\ \mathrm{m\,s^{-2}}$. The exact closed forms are

$$\gamma_{e} = \frac{GM}{ab}\left(1 - m - \frac{m\,e'q_0'}{6q_0}\right)
= 9.780325336\ \mathrm{m\,s^{-2}},$$

$$\gamma_{p} = \frac{GM}{a^{2}}\left(1 + \frac{m\,e'q_0'}{3q_0}\right)
= 9.832184938\ \mathrm{m\,s^{-2}}.$$

**Measured accuracy of the first-order theory.** The demonstration computes the
difference term by term:

| quantity | closed form ($\mathrm{m\,s^{-2}}$) | first order ($\mathrm{m\,s^{-2}}$) | difference |
|---|---|---|---|
| $\gamma_{e}$ | 9.780325336 | 9.780434286 | $+10.90\ \mathrm{mGal}$ |
| $\gamma_{p}$, first-order $J_2$ | 9.832184938 | 9.832087472 | $-9.75\ \mathrm{mGal}$ |
| $\gamma_{p}$, exact $J_2$ | 9.832184938 | 9.832165323 | $-1.96\ \mathrm{mGal}$ |

Two lessons follow. First, a first-order formula is not good enough for a
*definition*: 10 mGal is far above any survey precision. Second, using the exact
$J_2$ instead of the first-order one improves the pole by $7.79\ \mathrm{mGal}$,
which shows that the dominant error in the naive expansion is the coefficient,
not the algebra. This is why the international gravity formula is specified in the
Somigliana form below, and not as a truncated series.

## 5. Somigliana's formula

Given the two surface values $\gamma_{e}$ and $\gamma_{p}$, the surface gravity of
the level ellipsoid at geodetic latitude $\varphi$ is

$$\boxed{\;
\gamma(\varphi) = \frac{a\,\gamma_{e}\cos^{2}\varphi
+ b\,\gamma_{p}\sin^{2}\varphi}
{\sqrt{a^{2}\cos^{2}\varphi + b^{2}\sin^{2}\varphi}}\;}$$

This is exact (not a series) for the level ellipsoid, and it is the practical
definition of normal gravity everywhere in geodesy. Check the limits: at
$\varphi = 0$ the numerator is $a\gamma_{e}$ and the denominator $a$, so
$\gamma = \gamma_{e}$; at $\varphi = 90^\circ$ both numerator and denominator
pick out $b$, so $\gamma = \gamma_{p}$. The demonstration evaluates it at seven
latitudes:

| latitude | $\gamma$ ($\mathrm{m\,s^{-2}}$) | $\gamma$ (mGal) | difference from $45^\circ$ ($\mathrm{m\,s^{-2}}$) |
|---|---|---|---|
| $0^\circ$ | 9.780325336 | 978032.5336 | $-0.025872$ |
| $15^\circ$ | 9.783784962 | 978378.4962 | $-0.022413$ |
| $30^\circ$ | 9.793247269 | 979324.7269 | $-0.012951$ |
| $45^\circ$ | 9.806197769 | 980619.7769 | $0$ |
| $60^\circ$ | 9.819176953 | 981917.6953 | $+0.012979$ |
| $75^\circ$ | 9.828696627 | 982869.6627 | $+0.022499$ |
| $90^\circ$ | 9.832184938 | 983218.4938 | $+0.025987$ |

The total latitude range is $0.051860\ \mathrm{m\,s^{-2}} = 5186.0\ \mathrm{mGal}$,
about $0.53\%$ of the field.

### 5.1 What the series coefficients mean

Fitting $\gamma(\varphi)/\gamma_{e} - 1$ by $\beta\sin^{2}\varphi +
\beta_1\sin^{4}\varphi$ over all latitudes gives, as the demonstration measures,

| terms | $\beta$ | $\beta_1$ | max residual |
|---|---|---|---|
| 1 | $5.298557102\times10^{-3}$ | — | 0.408130 mGal |
| 2 | $5.278986840\times10^{-3}$ | $2.344982986\times10^{-5}$ | 0.000505 mGal |
| 3 | $5.279042787\times10^{-3}$ | $2.327096736\times10^{-5}$ | $0.000001$ mGal |

The pole-to-equator *difference* is
$\beta_{\text{pole}} = 5.302441399\times10^{-3}$, which is **not** the
coefficient of $\sin^{2}\varphi$ in the two-term fit: the two differ by $0.44\%$
because the difference is the sum of all the series coefficients. A quoted
"gravity coefficient" is meaningless until the series it belongs to is named, and
the fit residual is the evidence that the series reproduces the formula. This is a
general rule for this folder: **state the representation, not just the number.**

## 6. Clairaut's theorem

Clairaut's theorem relates the *dynamical* flattening of gravity to the geometric
flattening and the rotation parameter:

$$\boxed{\;\beta + f = \tfrac{5}{2}m, \qquad
\beta \equiv \frac{\gamma_{p} - \gamma_{e}}{\gamma_{e}}\;}$$

**Derivation (first order).** From Section 4,

$$\gamma_{p} - \gamma_{e}
\approx \frac{GM}{a^{2}}\big[2f - \tfrac92 J_2 + m\big]
\;\;\overset{J_2 = \frac23 f - \frac13 m}{=}\;\;
\frac{GM}{a^{2}}\big[2f - 3f + \tfrac32 m + m\big]
= \frac{GM}{a^{2}}\big[\tfrac52 m - f\big],$$

and dividing by $\gamma_{e} \approx (GM/a^{2})\left(1 + f - \tfrac32 m\right)$
gives $\beta \approx \tfrac52 m - f$ to first order. The theorem states that the
two ways the field can be non-spherical — the geometry ($f$) and the rotation
($m$) — are linked through the measured gravity difference alone, with no
knowledge of the internal density distribution.

**Numerical check (measured).**

$$\beta = 5.302441399\times10^{-3}, \qquad
\tfrac52 m - f = 5.271655602\times10^{-3},$$

$$\frac{\beta - \left(\tfrac52 m - f\right)}{\tfrac52 m - f}
= +0.5840\%, \qquad \text{absolute residual } +3.078580\times10^{-5}.$$

Clairaut's theorem is therefore verified **to the accuracy its derivation
claims** — first order in $f$ and $m$ — and not to the accuracy of the closed
form. Presenting the $0.58\%$ discrepancy as a failure would be wrong; presenting
the relation as exact would be worse. The second-order theory (Darwin's
continuation) is what makes $\gamma_{e}$ itself a derived rather than an adopted
constant.

**What breaks the theorem.** Clairaut's theorem assumes the body is in
hydrostatic equilibrium. A body with a fossil bulge, a rigid lithosphere or
lateral density variations has a $\beta$ and an $f$ that do not satisfy it, and the
*size* of the failure is a measurement of the departure from hydrostatic
equilibrium — one of the few direct handles on the deep interior.

## 7. Corrections that follow directly

### 7.1 The latitude correction

Differentiating Somigliana's formula gives the change of normal gravity with
latitude. Measured at 45° the slope is
$90.5115\ \mathrm{mGal\,deg^{-1}}$, which converts, with $1^\circ$ of latitude
$\approx 111.32\ \mathrm{km}$ of meridian arc, to

$$\frac{\mathrm{d}\gamma}{\mathrm{d}(\text{arc})}\bigg|_{45^\circ}
= \frac{90.5115}{111.32} = 0.8131\ \mathrm{mGal\,km^{-1}}.$$

At other latitudes the demonstration measures $0.4050\ \mathrm{mGal\,km^{-1}}$ at
$15^\circ$, $0.7026$ at $30^\circ$, $0.7057$ at $60^\circ$ and
$0.4081$ at $75^\circ$, and exactly zero at the equator and the poles. The reason
is that $\mathrm{d}\gamma/\mathrm{d}\varphi \propto \sin 2\varphi$: the correction
**vanishes at the equator**, where the formula has a maximum, and is largest at
$45^\circ$. Confusing the derivative with the function is the commonest latitude
error, and the measured shape is what settles it.

### 7.2 Normal gravity at height

For a station at height $h$ above the ellipsoid,

$$\gamma(h) = \gamma(\varphi)\left[1
- \frac{2}{a}\left(1 + f + m - 2f\sin^{2}\varphi\right)h
+ \frac{3h^{2}}{a^{2}}\right].$$

The **free-air gradient** is the linear coefficient:
$-0.3088\ \mathrm{mGal\,m^{-1}}$ at the equator,
$-0.3086$ at $45^\circ$ and $-0.3083$ at the pole as the demonstration measures.
Note how close these are to the spherical value $-0.308280\
\mathrm{mGal\,m^{-1}}$ derived in [lesson 01](01-newtonian-gravity.md) from
$-2g/r$: the ellipsoidal refinement appears in the fourth decimal. In practice
the coefficient $0.3086$ is applied for all latitudes, and the latitude-dependent
part is absorbed into the latitude correction.

The **$h^{2}$ term** is $+3h^{2}/a^{2}$ relative, which the demonstration measures
as $+0.072\ \mathrm{mGal}$ at $h = 1000\ \mathrm{m}$ and
$+1.157\ \mathrm{mGal}$ at $h = 4000\ \mathrm{m}$. A purely linear free-air
reduction therefore leaves a systematic error of about 1 mGal at 4 km of
elevation. Lesson [04](04-gravity-reduction.md) carries this term explicitly.

## 8. Worked examples

### Example 1 — anomaly of a station from normal gravity

A SYNTHETIC station at latitude $60^\circ$, on the ellipsoid, reads
$g = 981\,920.00\ \mathrm{mGal}$. Compute the gravity anomaly relative to the
normal field, and then the same anomaly for a station at latitude $45^\circ$,
same reading.

1. Normal gravity at $60^\circ$: $\gamma(60^\circ) =
   981\,917.6953\ \mathrm{mGal}$ (from the table).
2. Anomaly: $981\,920.00 - 981\,917.6953 = +2.3047\ \mathrm{mGal}$.
3. Normal gravity at $45^\circ$: $\gamma(45^\circ) =
   980\,619.7769\ \mathrm{mGal}$.
4. Anomaly at $45^\circ$: $981\,920.00 - 980\,619.7769 =
   +1300.2231\ \mathrm{mGal}$.

The same reading gives anomalies differing by $1298\ \mathrm{mGal}$, which is
larger than any real anomaly on Earth for a single station: this is the arithmetic
reminder that **the latitude correction is not optional**. It also shows that
"anomaly" without a stated reference is not a number.

### Example 2 — how much of the anomaly is latitude, for a survey

A SYNTHETIC survey line runs $40\ \mathrm{km}$ due north at $45^\circ$ latitude.

1. Latitude change: $40/111.32 = 0.3593^\circ$.
2. Latitude correction: $90.5115 \times 0.3593 = 32.52\ \mathrm{mGal}$ over the
   line, i.e. $0.8131\ \mathrm{mGal\,km^{-1}} \times 40 = 32.52\ \mathrm{mGal}$.
3. If the stations also rise $400\ \mathrm{m}$ along the line, the free-air term
   contributes $-0.3086 \times 400 = -123.44\ \mathrm{mGal}$, about four times
   the latitude term and of opposite sign.
4. A target producing $2\ \mathrm{mGal}$ is therefore invisible unless both terms
   are removed to better than $5\%$: $5\%$ of $123\ \mathrm{mGal}$ is
   $6\ \mathrm{mGal}$.

## 9. Assumptions and regime of validity

1. **Hydrostatic equilibrium.** The level-ellipsoid construction assumes the body
   is a rotating fluid in equilibrium. The real Earth departs from it, and the
   departure is *measured* (Section 6).
2. **Axisymmetry.** The normal field has no longitude dependence. Non-zonal terms
   ($J_{2,2}$, sectorial harmonics) are part of the actual field and are part of
   the anomaly.
3. **First order in $f$ and $m$** for every relation labelled first order. The
   measured residuals ($0.584\%$ in Clairaut, 10 mGal in $\gamma_{e}$) are the
   price, and they are larger than modern survey precision.
4. **The four constants are conventions.** A different ellipsoid (a different
   set of defining constants) gives different normal gravity and therefore a
   different anomaly from the same reading. Published anomalies must state their
   reference system.
5. **The normal field contains no density information.** $GM$ and $J_2$ are
   integrals of the density; the field does not invert uniquely to $\rho$, as
   [lesson 02](02-gravity-potential.md) shows.
6. **$GM$ is not $G$ times $M$.** $GM$ is the measured product; $G$ is known far
   less precisely than $GM$, so the Earth's mass is the uncertain factor. This is
   why defining constants are given as $GM$.
7. **Height.** $\gamma(h)$ above requires $h$ above the *ellipsoid*, not above sea
   level; mixing orthometric and ellipsoidal heights here is a real error source
   treated in module [04](../04-geodesy-reference-frames/README.md).

## 10. Python demonstration

`code/normal_gravity_demo.py` computes, from the four defining constants only:

1. the derived parameters $b = 6\,356\,752.314\ \mathrm{m}$,
   $e'^{2} = 6.739496742\times10^{-3}$, $m = 3.449786507\times10^{-3}$;
2. $\gamma_{e} = 9.780325336$ and $\gamma_{p} = 9.832184938\
   \mathrm{m\,s^{-2}}$, and the first-order comparison (differences
   $+10.90$, $-9.75$ and $-1.96\ \mathrm{mGal}$);
3. Somigliana's formula at seven latitudes, with the limits checked;
4. the series fits and their residuals, and the $0.44\%$ gap between the fitted
   $\beta$ and the pole-to-equator difference;
5. Clairaut's relation and its $0.5840\%$ residual;
6. the latitude correction, $0.8131\ \mathrm{mGal\,km^{-1}}$ at $45^\circ$ and
   zero at the equator;
7. the free-air gradient at three latitudes and the $h^{2}$ term at 1 and 4 km.

Exercises and solutions:
[`exercises/03-normal-gravity-exercises.md`](exercises/03-normal-gravity-exercises.md),
[`exercises/03-normal-gravity-solutions.md`](exercises/03-normal-gravity-solutions.md).

## Mastery checkpoint

Answer without notes.

> A SYNTHETIC station at latitude $30^\circ$ reads $g = 979\,400.00\
> \mathrm{mGal}$ on the ellipsoid. **(a)** Compute the anomaly against the normal
> field. **(b)** The station's position is later corrected to latitude
> $30^\circ\!.05$ north; compute the change in normal gravity and in the anomaly.
> **(c)** State what happens to the anomaly if a different reference ellipsoid is
> adopted. **(d)** Compute the free-air and $h^{2}$ contributions if the station is
> actually $3000\ \mathrm{m}$ above the ellipsoid.

A worked version of (a)–(b) is in the
[solutions](exercises/03-normal-gravity-solutions.md).

## Common pitfalls

1. **Confusing the ellipsoid with the geoid.** The ellipsoid is the reference
   *surface of the normal field*; the geoid is a level surface of the *real*
   field. They differ by the geoid undulation.
2. **Treating $J_2$ as a defining constant.** With $(a, f, GM, \omega)$ it is
   derived; with $(a, GM, J_2, \omega)$ the flattening is derived. State which set
   is in use.
3. **Applying latitude correction as a function rather than a derivative.** It
   vanishes at the equator, not at $45^\circ$.
4. **Quoting a gravity formula coefficient without its series.** Section 5.1
   measures a $0.44\%$ difference between two legitimate-looking "beta" values.
5. **Trusting a first-order formula at microgal level.** The measured errors are
   10 mGal in $\gamma_{e}$ and $0.58\%$ in Clairaut.
6. **Assuming the free-air coefficient is exactly constant.** It varies with
   latitude in the fourth decimal and with height through the $h^{2}$ term.
7. **Forgetting that normal gravity is hydrostatic.** A body out of hydrostatic
   equilibrium has no "normal gravity" in this sense at all.

## Related modules

- [Module 01 — Gravity Fundamentals](README.md) — this module; lesson
  [02](02-gravity-potential.md) supplies the potential and the level-surface
  condition, and lesson [04](04-gravity-reduction.md) uses the corrections derived
  here.
- [02-08 Potential Theory](../../02-physics/08-potential-theory/README.md) —
  harmonic functions, spherical harmonics and uniqueness.
- [Module 04 — Geodesy and Reference Frames](../04-geodesy-reference-frames/README.md) —
  where the ellipsoid, datum and height systems are used in practice.
- [Module 12 — Global Geophysics and the Earth's Interior](../../12-global-geophysics-interior/README.md) —
  what $J_2$ and $f$ imply about the density distribution.
- [07-03-01 Interpreting Anomalies](../03-gravity-anomalies-and-modelling/01-anomaly-interpretation.md) —
  what to do with the number this lesson produces.
