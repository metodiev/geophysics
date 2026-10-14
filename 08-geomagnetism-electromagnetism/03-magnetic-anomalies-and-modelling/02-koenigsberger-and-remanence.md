---
id: 08-03-02
title: "Koenigsberger Ratio and Remanence Dominance"
level: graduate
prereqs: ["08-03-01", "08-01-06"]
tags: [geomagnetism, electromagnetism, remanence, koenigsberger, magnetisation, palaeomagnetism]
---

# Koenigsberger Ratio and Remanence Dominance

Lesson 01 treated a magnetised body as if the present field decided everything.
It does not. A rock carries a **natural remanent magnetisation** acquired in the
past, and in many rocks that remanence is larger than the magnetisation the
present field induces. The ratio of the two is the **Koenigsberger ratio** $Q$,
and this lesson is about what happens when it exceeds one: the body's
magnetisation stops pointing along the field, an induced-only interpretation
returns a wrong susceptibility, and the anomaly can invert its sign.

> All models and data in this module are **SYNTHETIC**.

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** the Koenigsberger ratio $Q$ and **compute** it from a
   susceptibility, a remanence and an ambient field.
2. **Add** induced and remanent magnetisation as vectors and **compute** the
   magnitude and direction of the resultant.
3. **Derive** the anomaly of a body with an arbitrary magnetisation direction and
   **compute** how the anomaly amplitude varies with the angle between
   $\mathbf{M}$ and the ambient field.
4. **Predict** the sign and magnitude of the anomaly over a remanence-dominated
   body, and **identify** the configuration that reverses it.
5. **Quantify** the error made by an induced-only interpretation of a
   remanence-dominated anomaly.
6. **Explain** why $Q$ is a property of the rock *and* the latitude.
7. **State** which additional measurements could resolve the ambiguity, and what
   each would require.

## Prerequisites

- [08-03-01 Magnetic Anomaly Physics](01-magnetic-anomaly-basics.md) — the dipole
  field, $\Delta T = \hat f\cdot\mathbf{B}_a$ and the depth–moment trade-off.
- [08-01-06 Palaeomagnetism, Reversals and Magnetostratigraphy](../01-earth-magnetic-field/06-palaeomagnetism.md) —
  where remanence comes from and why its direction is geologically meaningful.

## 1. The ratio, defined

Write the induced and remanent magnetisations as vectors and add them:

$$\mathbf{M} = \underbrace{\chi\mathbf{H}_0}_{\mathbf{M}_i} + \underbrace{\mathbf{M}_r}_{\text{NRM}}, \qquad
Q \equiv \frac{\left|\mathbf{M}_r\right|}{\left|\mathbf{M}_i\right|}
= \frac{\left|\mathbf{M}_r\right|}{\chi H_0}.$$

Three statements follow directly from the definition and are worth separating:

- $Q$ is **dimensionless** but **not** a property of the rock alone: it contains
  $H_0$, which varies by more than a factor of two between the equator and the
  poles.
- $Q$ says nothing about the *direction* of the remanence, only about its
  magnitude. Two rocks with the same $Q$ and different remanence directions have
  different resultant magnetisations.
- The relevant comparison for the *anomaly* is not $Q$ but the vector sum; $Q$ is
  the convenient summary.

Rocks span a wide range of $Q$. Using synthetic teaching values at
$B_0 = 50.0\ \mu$T ($H_0 = 39.79\ \mathrm{A\,m^{-1}}$):

| Synthetic rock | $\chi$ | $M_i$ (A m$^{-1}$) | $M_r$ (A m$^{-1}$) | $Q$ |
|---|---|---|---|---|
| weakly magnetic sediment | $1.0\times10^{-4}$ | 0.0040 | 0.0002 | 0.050 |
| magnetite-bearing granite | $1.0\times10^{-2}$ | 0.3979 | 0.0500 | 0.126 |
| magnetite skarn | 0.2000 | 7.9577 | 2.0000 | 0.251 |
| basalt with a strong NRM | 0.0300 | 1.1937 | 5.0000 | 4.189 |
| banded iron formation | 0.5000 | 19.8944 | 20.0000 | 1.005 |

The basalt is the important row: a *modest* susceptibility and a modest
remanence make $Q > 4$. Basalts, in particular, are often remanence-dominated.

## 2. The vector sum, and why direction is the whole story

Take a synthetic body with $\chi = 0.0100$ (so $M_i = 0.3979$ A m$^{-1}$ along
the field, at $60^\circ$ inclination and $0^\circ$ declination) and a remanence
of $0.200$ A m$^{-1}$ at $30^\circ$ inclination with varying declination. Adding
the vectors:

| $M_r$ declination | $\left|\mathbf{M}\right|$ (A m$^{-1}$) | declination of $\mathbf{M}$ | inclination of $\mathbf{M}$ | $Q$ |
|---|---|---|---|---|
| $0^\circ$ | 0.5798 | $0.0^\circ$ | $50.1^\circ$ | 0.50 |
| $45^\circ$ | 0.5621 | $20.9^\circ$ | $52.3^\circ$ | 0.50 |
| $90^\circ$ | 0.5169 | $41.0^\circ$ | $59.3^\circ$ | 0.50 |
| $135^\circ$ | 0.4674 | $58.0^\circ$ | $72.0^\circ$ | 0.50 |
| $180^\circ$ | 0.4453 | $0.0^\circ$ | $86.7^\circ$ | 0.50 |

$Q$ is constant down the table because the *magnitudes* did not change; the
resultant direction swings through $87^\circ$ of inclination and up to $58^\circ$
of declination. An interpreter who assumes $\mathbf{M}\parallel\mathbf{B}_0$ is
therefore assuming a direction the rock need not share, and the error is not a
few per cent — it can be tens of degrees.

### 2.1 The algebra of the sum

Because $\mathbf{M}_i$ is parallel to $\hat f$, the vector sum can be written
with the law of cosines. Let $\gamma$ be the angle between $\mathbf{M}_r$ and
$\hat f$ and write $M_r = Q M_i$. Then

$$\left|\mathbf{M}\right| = M_i\sqrt{1 + Q^{2} + 2Q\cos\gamma},$$

and the component of $\mathbf{M}$ along the ambient field direction is

$$\mathbf{M}\cdot\hat f = M_i\left(1 + Q\cos\gamma\right).$$

Two consequences are immediate and useful. First, the projection on the field
vanishes when $\cos\gamma = -1/Q$, which for $Q > 1$ is an accessible
configuration: a strong enough remanence can null the *along-field* component
entirely. Second, the maximum of $|\mathbf{M}|$ is at $\gamma = 0$
($|\mathbf{M}| = M_i(1+Q)$) and the minimum at $\gamma = 180^\circ$
($|\mathbf{M}| = M_i|1-Q|$).

*Numerical check (SYNTHETIC).* With $M_i = 0.3979$ A m$^{-1}$, $M_r = 0.200$
A m$^{-1}$ so $Q = 0.5027$, and a remanence at $30^\circ$ inclination,
$45^\circ$ declination, the angle $\gamma$ between $\mathbf{M}_r$ and
$\hat f$ follows from $\cos\gamma = \cos30^\circ\cos45^\circ\cos60^\circ +
\sin30^\circ\sin60^\circ = 0.3062 + 0.4330 = 0.7392$, so $\gamma = 42.3^\circ$.
Then

$$\left|\mathbf{M}\right| = 0.3979\sqrt{1 + 0.5027^{2} + 2(0.5027)(0.7392)}
= 0.3979\sqrt{1.9958} = 0.3979\times1.4127 = 0.5621\ \mathrm{A\,m^{-1}},$$

which is exactly the demonstration's entry for that row. Note what the check
requires: getting $\gamma$ right in three dimensions. Reading the table's
declination difference instead of $\gamma$ is the commonest arithmetic error in
this calculation, and here it would have given $45^\circ$ and $0.5566$
A m$^{-1}$.

### 2.2 The amplitude as a function of the angle

With $\theta$ the angle between $\mathbf{M}$ and $\hat f$, and the body observed
directly above its centre with $\hat r$ vertical,

$$\Delta T(\theta) = \frac{\mu_0}{4\pi}\frac{M V}{z^{3}}
\left[3\cos(I)\cos(\text{angle between }\hat m\text{ and }\hat z)
- \cos\theta\right],$$

so for a fixed $|\mathbf{M}|$ the anomaly is a **linear** function of the
projection factors and passes through zero. For the demonstration's body
($M = 0.5169$ A m$^{-1}$, $V = 1$ km$^3$, $z = 2$ km) rotating $\mathbf{M}$ away
from $\hat f$ in the vertical plane containing $\hat f$:

| $\theta$ | $\Delta T$ (nT) | $\Delta T/\Delta T(\theta=0)$ |
|---|---|---|
| $0^\circ$ | 9.06 | 1.000 |
| $30^\circ$ | 3.14 | 0.346 |
| $60^\circ$ | $-3.62$ | $-0.400$ |
| $90^\circ$ | $-9.41$ | $-1.039$ |
| $120^\circ$ | $-12.68$ | $-1.400$ |
| $150^\circ$ | $-12.55$ | $-1.386$ |
| $180^\circ$ | $-9.06$ | $-1.000$ |

Three features deserve attention. The anomaly changes sign between $30^\circ$ and
$60^\circ$ while the magnetisation magnitude is unchanged. The largest anomaly is
at $\theta \approx 120^\circ$, *not* at $\theta = 0$: for a body magnetised
partly across the field, the projection factor can be larger. And the curve is
not monotonic, because the bracket mixes two different cosines.

## 3. Worked example: a remanence-dominated body

Take $\chi = 0.020$ ($M_i = 0.796\ \mathrm{A\,m^{-1}}$) and
$M_r = 5.00\ \mathrm{A\,m^{-1}}$ so that $Q = 6.28$. The body is the same
$1$ km$^3$ at $2$ km depth, and the induced-only anomaly is $12.43$ nT.

| Remanence direction (inclination/declination) | $\Delta T$ over the centre (nT) |
|---|---|
| $60^\circ / 0^\circ$ (along the field) | 90.56 |
| $60^\circ / 90^\circ$ (across the field) | 106.18 |
| $-60^\circ / 0^\circ$ (against the field) | $-96.94$ |
| $-30^\circ / 180^\circ$ | $-14.63$ |

The first row is $7.3\times$ the induced-only value; the third is negative with
almost the same magnitude. **The same rock, the same depth, the same surveying,
produces an anomaly either positive or negative depending on a magnetisation the
survey never measured.**

## 4. The cost of assuming induced magnetisation

A synthetic body with $M_i = 0.50$ A m$^{-1}$, $M_r = 5.00$ A m$^{-1}$
($Q = 10.0$) and a remanence at $60^\circ$ inclination, $45^\circ$ declination
gives a resultant

$$\mathbf{M} = 0.50\hat f + 5.00\,\hat m_r, \qquad
\left|\mathbf{M}\right| = 5.467\ \mathrm{A\,m^{-1}},
\qquad \mathbf{M}\text{ at }41.2^\circ\text{ decl, }60.6^\circ\text{ incl}.$$

The angle between $\mathbf{M}$ and $\mathbf{B}_0$ is $20.1^\circ$, and the anomaly
over the centre is $90.51$ nT.

An interpreter who assumes induced magnetisation places $\mathbf{M}$ along
$\hat f$ and asks what magnitude reproduces $90.51$ nT. Because the anomaly is
linear in $\mathbf{M}$, the required magnitude follows by scaling, giving

$$\left|\mathbf{M}_{\text{assumed}}\right| = 5.793\ \mathrm{A\,m^{-1}},
\qquad \chi_{\text{app}} = \frac{5.793}{39.79} = 0.1456.$$

The true susceptibility is $0.0126$. The induced-only interpretation is wrong by
a factor of **11.6**, and the residual is not noise: it is a physically
unmodelled magnetisation. Note also the direction of the error — the
susceptibility is *inflated*, because the interpreter has to explain a strong
anomaly with a mechanism that is partially cancelling itself.

## 5. What can be done about it

Nothing in a single total-field profile determines $\mathbf{M}$'s direction. The
available remedies, in increasing order of cost, are:

1. **Measure the rock.** Oriented samples give the NRM direction and the
   susceptibility directly, so $\mathbf{Q}$ and the resultant direction can be
   computed rather than assumed. This is the standard route in mineral
   exploration.
2. **Use the anomaly shape.** The direction of $\mathbf{M}$ affects not only the
   amplitude but the *asymmetry* of the anomaly; a body magnetised across the
   field has a different shape from one magnetised along it. This is close to
   inversion and subject to exactly the non-uniqueness of
   [06 Magnetic Inversion](06-magnetic-inversion.md).
3. **Use several bodies.** If a survey covers many bodies and one of them can be
   sampled, the sampled direction can be tested against the others.
4. **Use the magnetic gradient tensor** or borehole vector data, which fix
   $\mathbf{M}$ more directly than a scalar total field.

The honest summary is that the anomaly gives $|\mathbf{M}|$ and $\mathbf{M}$'s
projection on $\hat f$, and the rest is prior information.

## 6. Assumptions and regime of validity

1. **Uniform magnetisation of each body.** As in
   [01](01-magnetic-anomaly-basics.md); good for weak magnetisation, questionable
   for the strongly magnetic bodies where $Q$ is often large.
2. **A single remanence component.** Rocks can carry several superimposed
   components, acquired at different times. What is measured is their sum.
3. **No viscous or chemical remagnetisation since acquisition.** Laboratory
   demagnetisation is how this is tested palaeomagnetically, and a survey cannot
   test it at all.
4. **The ambient field direction is known and uniform.** In practice it is
   modelled from a main-field model, with an error of order a fraction of a
   degree; that translates into a small error in the projection factors.
5. **$Q$ is treated as constant over the body.** It is not, if the body contains
   more than one lithology; the "body" in the model is then an average.

## 7. Python demonstration

`code/koenigsberger_and_remanence_demo.py` prints every number in this lesson:

1. $Q$ for five synthetic rock types;
2. the vector sum, including the resultant declination and inclination as the
   remanence azimuth is varied at fixed $Q$;
3. the anomaly as a function of the angle between $\mathbf{M}$ and the field,
   including the sign change and the maximum near $\theta = 120^\circ$;
4. a remanence-dominated body producing $+90.56$ nT and $-96.94$ nT from the
   same rock;
5. the induced-only interpretation bias, a factor of $11.59$ in apparent
   susceptibility.

```bash
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python koenigsberger_and_remanence_demo.py
```

Fixed seed, print-only, exits 0.

## 8. Exercises

[`exercises/02-koenigsberger-and-remanence-exercises.md`](./exercises/02-koenigsberger-and-remanence-exercises.md)
and
[`exercises/02-koenigsberger-and-remanence-solutions.md`](./exercises/02-koenigsberger-and-remanence-solutions.md).

## Mastery checkpoint

Without notes:

> A **synthetic** basalt body has $\chi = 0.040$ and
> $M_r = 6.0$ A m$^{-1}$ at $45^\circ$ inclination, $200^\circ$ declination. The
> ambient field is $48\ \mu$T at $55^\circ$ inclination, $0^\circ$ declination.
> **(a)** Compute $H_0$, $M_i$ and $Q$. **(b)** Compute $\left|\mathbf{M}\right|$
> and the angle between $\mathbf{M}$ and $\mathbf{B}_0$. **(c)** The body is
> $0.5$ km$^3$ at $1.0$ km depth; compute the anomaly over its centre.
> **(d)** Compute the susceptibility an induced-only interpreter would report.
> **(e)** State two measurements that would remove the ambiguity and what each
> requires.

## Common pitfalls

1. **Adding magnitudes instead of vectors.** $|\mathbf{M}| \neq M_i + M_r$ except
   when the two are parallel.
2. **Quoting $Q$ as a rock constant.** It contains $H_0$; a basalt that is
   remanence-dominated in one country can be induced-dominated in another.
3. **Assuming the largest anomaly means the largest magnetisation.** The
   projection factor can peak at an intermediate angle (Section 2.1).
4. **Reading a negative anomaly as a reversed-polarity body.** A body magnetised
   against the field and a body with reversed polarity produce the same total
   field anomaly, and neither is distinguishable from an induced body in a
   different field inclination without more information.
5. **Ignoring the depth trade-off when using amplitude to infer $M$.** A factor
   of two in depth is a factor of eight in moment.
6. **Trusting a single solution from an inversion that assumed a
   magnetisation direction.** The assumed direction is an input, not a result.

## Related modules

- [01 The Earth's Magnetic Field](../01-earth-magnetic-field/README.md) —
  palaeomagnetic directions and reversals.
- [01 Magnetic Anomaly Physics](01-magnetic-anomaly-basics.md) — the forward
  model this lesson extends.
- [03 Reduction to the Pole](03-reduction-to-pole.md) — what one does about an
  unknown magnetisation direction when interpreting a map.
- [06 Magnetic Inversion](06-magnetic-inversion.md) — the systematic treatment of
  what a data set can and cannot determine.
- [04-01 Earth Structure](../../04-earth-science-geology/01-earth-structure/README.md) —
  the rock types whose magnetic properties are being contrasted.
