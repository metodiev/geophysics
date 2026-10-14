---
id: 08-01-02
title: "The Geocentric Dipole, IGRF and WMM Models"
level: advanced
prereqs: ["08-01-01", "02-08-03", "02-08-01"]
tags: [geomagnetism, dipole, igrf, wmm, gauss-coefficients, reference-models]
---

# The Geocentric Dipole, IGRF and WMM Models

A compass needle behaves, to a first approximation, as if the Earth contained a
single bar magnet near its centre. That approximation explains the sign of
inclination in each hemisphere, the growth of dip with latitude, and the
existence of a magnetic equator; it fails by a few per cent, and the way it fails
is the subject of the rest of the module. This lesson derives the dipole field
from a potential, defines the Gauss coefficients that generalise it, and
describes what a reference model such as IGRF or WMM actually is: a
finite-degree, time-dependent polynomial fit, valid over a stated interval, and
nothing more.

**All models and data in this module are SYNTHETIC.** The coefficients used here
are invented teaching values; they are **not** IGRF or WMM coefficients, and no
published model is reproduced. The standard values used are $\mu_0$, the mean
Earth radius $6371\ \mathrm{km}$, the dipole tilt $11.5^{\circ}$ and the
Boltzmann-type constants of no other kind.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the field of a centred dipole from a scalar potential and obtain
   $B_r = 2(\mu_0 m/4\pi r^3)\cos\theta$,
   $B_\theta = (\mu_0 m/4\pi r^3)\sin\theta$.
2. **Derive** the geomagnetic relation $\tan I = 2\tan\lambda$ and use it to
   convert between inclination and geomagnetic latitude.
3. **Reproduce** the radial decay $(a/r)^3$ and explain why natural attenuation
   with altitude is a consequence of Laplace's equation rather than a separate
   fact.
4. **Define** a Gauss coefficient and compute the number of coefficients needed
   for a given maximum degree.
5. **Recover** Gauss coefficients from synthetic field values by least squares,
   and explain why a truncated fit absorbs nothing when the basis is orthogonal
   over a complete sphere but does bias a fit to scattered points.
6. **State** what an IGRF- or WMM-class model is, what its maximum degree means,
   and what limits its validity in time and in space.

## Prerequisites

- [08-01-01 Describing the Main Field](01-main-field-description.md) — the
  elements and the frame.
- [02-08-03 Spherical Harmonics and Multipole Expansions](../../02-physics/08-potential-theory/03-spherical-harmonics.md)
  — Legendre functions and the multipole expansion.
- [02-08-01 Newtonian Gravitational Potential and Field](../../02-physics/08-potential-theory/01-gravitational-potential.md)
  — the same mathematics for a different field, which is the fastest way to see
  what is generic here.

## 1. From a potential to the dipole field

The magnetic field of a current-free region is curl-free, so it can be written as
the gradient of a **scalar potential**:

$$\mathbf{B} = -\nabla V, \qquad \nabla^2 V = 0 \ \text{where there is no source}.$$

Inside a spherical shell containing no current, the general solution of Laplace's
equation that vanishes at infinity is

$$V(r,\theta,\phi) = a\sum_{n=1}^{\infty}
\left(\frac{a}{r}\right)^{n+1}
\sum_{m=0}^{n}\left[g_n^m\cos(m\phi) + h_n^m\sin(m\phi)\right]P_n^m(\cos\theta),$$

with $a$ the reference radius, $\theta$ colatitude, $\phi$ east longitude,
$P_n^m$ the Schmidt semi-normalised associated Legendre functions, and $g_n^m$,
$h_n^m$ the **Gauss coefficients**. Everything that follows is this one equation
specialised and truncated.

### 1.1 Degree 1: the geocentric dipole

Keep only $n = 1$. With $P_1^0 = \cos\theta$ and $P_1^1 = \sin\theta$, and
writing $S_1 = g_1^0\cos\theta + (g_1^1\cos\phi + h_1^1\sin\phi)\sin\theta$,

$$V_1 = a\left(\frac{a}{r}\right)^{2} S_1.$$

The field components in spherical coordinates follow from
$B_r = -\partial V/\partial r$ and
$B_\theta = -(1/r)\,\partial V/\partial\theta$:

$$B_r = 2\left(\frac{a}{r}\right)^{3} S_1, \qquad
B_\theta = -\left(\frac{a}{r}\right)^{3}
\frac{\partial S_1}{\partial\theta}, \qquad
B_\phi = -\frac{1}{r\sin\theta}\frac{\partial V}{\partial\phi}.$$

For a purely **axial** dipole, $g_1^1 = h_1^1 = 0$ and $S_1 = g_1^0\cos\theta$, so

$$\boxed{\,B_r = 2 g_1^0 \left(\frac{a}{r}\right)^{3}\cos\theta, \qquad
B_\theta = g_1^0 \left(\frac{a}{r}\right)^{3}\sin\theta, \qquad B_\phi = 0.}$$

With $g_1^0 < 0$ this is a dipole whose north pole is in the south; the sign
convention is the Earth's, not a mistake. In the site frame,
$X = -B_\theta$ and $Z = -B_r$ (because $\theta$ increases southward and $r$
increases upward), so

$$X = -g_1^0\left(\frac{a}{r}\right)^3\sin\theta, \qquad
Z = -2g_1^0\left(\frac{a}{r}\right)^3\cos\theta.$$

### 1.2 The relation $\tan I = 2\tan\lambda$

Write $\lambda$ for latitude, so $\theta = 90^{\circ} - \lambda$ and
$\sin\theta = \cos\lambda$, $\cos\theta = \sin\lambda$. Then

$$H = |X| = |g_1^0|\left(\frac{a}{r}\right)^3\cos\lambda, \qquad
Z = 2|g_1^0|\left(\frac{a}{r}\right)^3\sin\lambda,$$

and dividing,

$$\tan I = \frac{Z}{H} = 2\tan\lambda.$$

This is the single most useful equation in the lesson. It says:

- $I = 0$ on the dipole equator and $I = \pm90^{\circ}$ at the dipole poles;
- the inclination is steeper than the latitude everywhere except at the equator
  and the pole;
- because the radial factor $(a/r)^3$ cancels, **the relation is independent of
  the dipole moment and of the observation radius** — it is pure geometry.

### 1.3 Worked example — the synthetic axial dipole table

Take the SYNTHETIC coefficient $g_1^0 = -30000\ \mathrm{nT}$ at $r = a$. The
demonstration tabulates:

| latitude (°) | $X$ (nT) | $Z$ (nT) | $I$ (°) | $\tan I/(2\tan\lambda)$ |
|---|---|---|---|---|
| 0 | 30000.0 | 0.0 | 0.0000 | — |
| 15 | 28977.8 | 15529.1 | 28.1868 | 1.000000 |
| 30 | 25980.8 | 30000.0 | 49.1066 | 1.000000 |
| 45 | 21213.2 | 42426.4 | 63.4349 | 1.000000 |
| 60 | 15000.0 | 51961.5 | 73.8979 | 1.000000 |
| 75 | 7764.6 | 57955.5 | 82.3693 | 1.000000 |
| 85 | 2614.7 | 59771.7 | 87.4952 | 1.000000 |

Check one row by hand. At $\lambda = 45^{\circ}$, $\theta = 45^{\circ}$:

$$X = -g_1^0\sin 45^{\circ} = 30000\times0.707107 = 21213.2\ \mathrm{nT},$$
$$Z = -2g_1^0\cos 45^{\circ} = 2\times30000\times0.707107
= 42426.4\ \mathrm{nT},$$
$$I = \arctan(2\tan 45^{\circ}) = \arctan 2 = 63.4349^{\circ}.$$

The last column of the table is 1.000000 at every latitude, which is the
numerical statement of section 1.2. The horizontal intensity at the dipole
equator is $30000.0\ \mathrm{nT}$ and it approaches $2.7\times10^{-5}\
\mathrm{nT}$ near the dipole pole: $H$ collapses because $X \propto \cos\lambda$.

## 2. Radial decay, and why it is not an extra assumption

Laplace's equation has no radial derivative structure of its own; it merely
requires the sum of the radial and tangential second derivatives to vanish. The
consequence is that each degree carries a fixed radial power law,
$(a/r)^{n+2}$ for the field. For degree 1 that is $(a/r)^3$:

| $r$ (km) | altitude (km) | $(a/r)^3$ | $F$ at the dipole equator (nT) |
|---|---|---|---|
| 6371.0 | 0.0 | 1.00000 | 30000.00 |
| 6471.0 | 100.0 | 0.95435 | 28630.56 |
| 6771.0 | 400.0 | 0.83304 | 24991.11 |
| 7371.0 | 1000.0 | 0.64572 | 19371.57 |

Four hundred kilometres of altitude multiplies the dipole field by $0.83304$,
removing $16.70\%$ of its amplitude. Two things follow that this module will use
repeatedly:

- **A measurement at altitude can be continued to the surface by dividing by
  $(a/r)^{n+2}$ per degree.** The shape of the anomaly does not change with
  height; only the amplitude does.
- **The inverse operation is ill-posed.** Continuation *downward* multiplies
  high degrees by $(r/a)^{n+2}$, which grows without bound with $n$: noise at
  degree 13 is amplified more than the signal at degree 1. That is why
  downward continuation must be truncated or damped, and it is the same
  mechanism that makes gravity and magnetic inversion non-unique
  ([18-01-03 Null Space, Non-Uniqueness and Equivalence Classes](../../18-inverse-problems/01-inverse-problem-foundations/03-null-space.md)).

## 3. The dipole is tilted, and nothing in the data says it should not be

The best-fitting dipole axis is tilted by $11.5^{\circ}$ from the rotation axis
(standard value). Geomagnetic latitude is the latitude measured from that axis.
For a site at geographic colatitude $\theta$ and longitude $\phi$, with the
dipole axis tilted in the $\phi = 0$ plane,

$$\cos\theta_{\text{gm}} = \cos\theta\cos(11.5^{\circ})
+ \sin\theta\sin(11.5^{\circ})\cos\phi.$$

The demonstration evaluates this at synthetic sites:

| site lat (°) | site lon (°) | geomagnetic lat (°) | difference (°) |
|---|---|---|---|
| 45.0 | 0.0 | 56.5000 | +11.5000 |
| 45.0 | 90.0 | 43.8610 | −1.1390 |
| 45.0 | 180.0 | 33.5000 | −11.5000 |
| 60.0 | 90.0 | 58.0640 | −1.9360 |
| 0.0 | 0.0 | 11.5000 | +11.5000 |
| −30.0 | 90.0 | −29.3381 | +0.6619 |

The difference never exceeds the tilt itself, and is largest where the site
longitude aligns with the tilt plane. The physical point is that the tilt is a
*model parameter*, not an observable: any data set can be fitted by a dipole with
some axis and moment, and the residual after doing so is the non-dipole field.
There is no measurement that "sees" the axis.

## 4. From the dipole to a real reference model

### 4.1 Counting coefficients

Retaining all degrees up to $N$ requires

$$\sum_{n=1}^{N}(2n+1) = N(N+2) \ \text{coefficients},$$

counting $g$ and $h$ together. The demonstration prints 3, 8, 15, 120 and 195
for $N = 1, 2, 3, 10, 13$. Modern IGRF- and WMM-class models are truncated
somewhere around $N = 13$; the exact truncation is a model choice traded against
the data coverage, the noise level and the intended epoch.

### 4.2 Recovering coefficients from field values

Because the spherical harmonics are orthogonal over a complete sphere, the
coefficients can be recovered by projection, or equivalently by least squares on
a grid that integrates them correctly. The demonstration does the latter with
Gauss–Legendre nodes in colatitude and a uniform longitude grid:

- fitting **degree 1 only** to a field that also contains degree 2 recovers
  $g_1^0 = -30000.00$, $g_1^1 = -1800.00$, $h_1^1 = 4800.00\ \mathrm{nT}$ — the
  true values exactly — and leaves an rms residual of **4.87% of the rms field**.
- fitting **degrees 1 and 2** recovers all eight coefficients to better than
  $4\times10^{-11}\ \mathrm{nT}$, with an rms residual of
  $2.9\times10^{-11}\ \mathrm{nT}$, i.e. machine precision.

This is a precise and slightly counter-intuitive result: **truncation does not
bias the coefficients you keep — it appears entirely as a residual field.** The
reason is orthogonality. Bias appears only when a truncated model is fitted to a
scattered, non-global set of points, where the omitted harmonics are correlated
with the retained ones over that particular sampling. That distinction is
worth remembering whenever someone says "the dipole term is contaminated by
higher degrees": on a global orthogonal grid it is not contaminated, and on a
local survey it certainly is.

### 4.3 What a truncation leaves behind, in field space

| site lat (°) | site lon (°) | degree-1 $F$ (nT) | full $F$ (nT) | residual (nT) | % of $F$ |
|---|---|---|---|---|---|
| 20 | 30 | 34573.59 | 34070.53 | 2461.91 | 7.23 |
| 45 | 120 | 43122.10 | 39152.27 | 4528.60 | 11.57 |
| −60 | 250 | 51566.28 | 54786.59 | 3573.34 | 6.52 |
| 10 | 300 | 35181.82 | 37997.21 | 4213.69 | 11.09 |

The residual is a vector difference, not a difference of magnitudes, which is why
it can exceed the difference of the $F$ columns. With the synthetic coefficients
chosen for this demonstration the non-dipole part reaches roughly a tenth of the
field; a real Earth is somewhat better approximated by a dipole than that, but
the teaching point is the *structure* of the residual: it is spatially
organised, it is not noise, and it is what the higher degrees describe.

### 4.4 Time: the model has an epoch

A Gauss coefficient is a number for a date. The demonstration carries a synthetic
secular variation of $g_1^0$ of $-40\ \mathrm{nT\,yr^{-1}}$ and reports:

| extrapolation | $g_1^0$ (nT) | change (nT) | change (%) |
|---|---|---|---|
| 0 yr | −30000.00 | 0.0 | 0.00 |
| 2 yr | −30080.00 | −80.0 | +0.27 |
| 5 yr | −30200.00 | −200.0 | +0.67 |
| 10 yr | −30400.00 | −400.0 | +1.33 |

Extrapolation error is not a rounding issue: it is a physical error that grows
with the interval, and unlike the truncation error it does **not** average out
of a survey. Lesson [08-01-04](04-secular-variation.md) quantifies it properly;
here the point is that a model without an epoch is not a model.

## 5. Assumptions and regime of validity

1. **No current flows in the region where $V$ is expanded.** The potential
   representation is valid in the insulating atmosphere and crust between the
   source region and the observation point; it fails inside the core, where the
   field is generated.
2. **The source is internal.** A surface data set can be fitted equally well by
   an internal and an external source of the same degree; only data at two radii
   (satellite plus surface) or a physical argument distinguishes them. This is
   the classical internal/external ambiguity, and it is the subject of
   [08-01-03](03-spherical-harmonic-magnetic.md).
3. **The reference radius is stated.** $a = 6371\ \mathrm{km}$ is used
   throughout this module.
4. **Schmidt semi-normalisation.** Coefficient values are convention-dependent.
   Comparing $g_1^0$ from two sources requires the same normalisation; the
   Schmidt convention used here is the geomagnetic standard.
5. **The truncation degree is part of the answer.** A degree-13 model and a
   degree-1 model are not the same object measured at different precisions; they
   are different models, and the difference has spatial structure.
6. **The epoch and the secular-variation term are part of the answer.** Outside
   the stated validity interval the model degrades monotonically with time.

## 6. Python demonstration

`code/dipole_and_igrf_demo.py` implements the potential of section 1 for an
arbitrary set of Gauss coefficients using Schmidt semi-normalised Legendre
functions, and prints:

1. the synthetic axial-dipole table with the $\tan I = 2\tan\lambda$ column;
2. the radial attenuation $(a/r)^3$ at 0, 100, 400 and 1000 km;
3. geomagnetic latitude under the standard $11.5^{\circ}$ tilt;
4. the least-squares recovery of coefficients at degree 1 and at degrees 1–2,
   with residuals;
5. the field-space residual left by a degree-1 truncation at four sites;
6. coefficient counts up to degree 13 and a synthetic secular-variation
   extrapolation.

Exercises and solutions:
[`exercises/02-dipole-and-igrf-exercises.md`](./exercises/02-dipole-and-igrf-exercises.md),
[`exercises/02-dipole-and-igrf-solutions.md`](./exercises/02-dipole-and-igrf-solutions.md).
The general theory of the expansion is developed in
[08-01-03](03-spherical-harmonic-magnetic.md).

## Mastery checkpoint

1. Derive $\tan I = 2\tan\lambda$ from $B_r$ and $B_\theta$ of an axial dipole,
   stating where each sign comes from.
2. At a site where $I = 55.0^{\circ}$, compute the geomagnetic latitude.
3. A satellite at 400 km measures a dipole field of $24991.11\ \mathrm{nT}$ at
   the dipole equator. Recover the coefficient $g_1^0$.
4. How many Gauss coefficients does a degree-6 model require? Derive the
   formula, do not recall it.
5. Explain in two sentences why a degree-1 fit to a global grid does not bias
   $g_1^0$ even when the true field contains degree 2.

## Common pitfalls

1. **Treating the magnetic pole as the dipole axis intersection with the
   surface of a *tilted* dipole and then using $a = 6371\ \mathrm{km}$.**
   The axis position and the surface location of vertical field differ; the
   dipole pole is a direction, the dip pole is a location.
2. **Supplying a coefficient set with the wrong normalisation.** Schmidt,
   Gauss and fully normalised conventions differ by factorials.
3. **Forgetting $(a/r)^{n+2}$.** A value at satellite altitude is not a value at
   the surface.
4. **Extrapolating without an epoch.** Section 4.4 quantifies the mistake.
5. **Calling the residual "noise".** It is organised structure; at degree 13 it
   is also partly unresolved noise, and the two cannot be separated by
   inspection alone.

## Related modules

- [08-01-03 Spherical Harmonic Analysis of the Magnetic Field](03-spherical-harmonic-magnetic.md) —
  the full machinery, including the ambiguity this lesson only flags.
- [08-01-04 Secular Variation, Jerks and Core Dynamics](04-secular-variation.md) —
  the time derivatives of the coefficients.
- [08-02 Magnetic Instruments and Surveys](../02-magnetic-instruments-and-surveys/README.md) —
  the instruments that measure the field whose model this lesson defines.
- [02-08 Potential Theory](../../02-physics/08-potential-theory/README.md) —
  Laplace's equation, multipoles and uniqueness.
- [12-04-01 Observations of the Core Field and Secular Variation](../../12-global-geophysics-interior/04-geomagnetism-and-core/01-core-field-observations.md) —
  the same field seen as a core-process observable.

## Self-assessment checklist

- [ ] I can derive the axial dipole field from the potential.
- [ ] I can convert between $I$ and geomagnetic latitude without notes.
- [ ] I can state the radial power law and justify it from Laplace's equation.
- [ ] I can count the coefficients a model of a given degree needs.
- [ ] I can recover a coefficient by least squares and state the residual.
- [ ] I can list the four things a reference model must state: normalisation,
      reference radius, truncation degree and epoch.
