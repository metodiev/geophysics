---
id: 08-01-03
title: "Spherical Harmonic Analysis of the Magnetic Field"
level: doctoral
prereqs: ["08-01-02", "02-08-03", "02-08-02", "02-08-06"]
tags: [geomagnetism, spherical-harmonics, gauss-coefficients, power-spectrum, continuation, non-uniqueness]
---

# Spherical Harmonic Analysis of the Magnetic Field

Spherical harmonic analysis is the only framework in geomagnetism that lets a
handful of numbers describe a field everywhere outside its source region. That
is a strong claim, and it is worth being precise about what makes it true: the
field is a potential field in a source-free region, the region is (nearly) a
spherical shell, and Laplace's equation separates in spherical coordinates. Every
convenience of the method — the coefficients, the power spectrum, upward
continuation — is a corollary. Every limitation — truncation, downward
continuation, internal/external ambiguity — is the same three facts read in
reverse.

**All models and data in this module are SYNTHETIC.** The Gauss coefficients
below are invented teaching values, not IGRF or WMM coefficients, and no
published field model, spectrum or observation is reproduced. Standard values
used are $\mu_0 = 4\pi\times10^{-7}\ \mathrm{H\,m^{-1}}$, $a = 6371\ \mathrm{km}$
and the $11.5^{\circ}$ dipole tilt.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the general internal-source solution of Laplace's equation as a
   spherical harmonic series, and state the boundary conditions that select it.
2. **Evaluate** Schmidt semi-normalised associated Legendre functions and verify
   their orthogonality integral $2(2-\delta_{m0})/(2n+1)$.
3. **Forward-compute** the field from a set of Gauss coefficients, and check the
   degree-1 and degree-2 terms against hand algebra.
4. **Derive** the Mauersberger–Lowes degree power
   $R_n = (n+1)\sum_m\left[(g_n^m)^2+(h_n^m)^2\right]$ from the mean square of
   the field over a sphere.
5. **Measure** truncation error as a function of maximum degree and decide what
   degree a task requires.
6. **Quantify** upward and downward continuation by degree, and explain why
   downward continuation is ill-posed.
7. **State** the non-uniqueness that survives even with perfect, complete data
   at one radius, and the extra information that removes it.

## Prerequisites

- [08-01-02 The Geocentric Dipole, IGRF and WMM Models](02-dipole-and-igrf.md) —
  the degree-1 case and the definition of a Gauss coefficient.
- [02-08-03 Spherical Harmonics and Multipole Expansions](../../02-physics/08-potential-theory/03-spherical-harmonics.md)
  — the mathematical machinery.
- [02-08-02 Laplace's Equation and Harmonic Functions](../../02-physics/08-potential-theory/02-laplace-equation.md)
  — separation of variables and the radial solutions.
- [02-08-06 Uniqueness Theorems and Boundary Conditions](../../02-physics/08-potential-theory/06-uniqueness-theorems.md)
  — what "the solution is unique" precisely requires.

## 1. Setting up the expansion

Let $V$ be the magnetic scalar potential, so $\mathbf{B} = -\nabla V$. In a
region with no current density, Ampère's law gives $\nabla\times\mathbf{B} = 0$
and therefore $\nabla^2 V = 0$. Let the region be the annulus
$r_1 < r < r_2$ outside the core and inside the ionosphere. In spherical
coordinates $(r,\theta,\phi)$ Laplace's equation separates, and the radial
solutions are $r^{n}$ and $r^{-(n+1)}$. Demanding that $V\to0$ as $r\to\infty$
kills $r^{n}$, which is the field of **external** sources; what remains, written
in the conventional form with a reference radius $a$, is

$$V(r,\theta,\phi) = a\sum_{n=1}^{\infty}\left(\frac{a}{r}\right)^{n+1}
\sum_{m=0}^{n}\left[g_n^m\cos m\phi + h_n^m\sin m\phi\right]P_n^m(\cos\theta).$$

Three normalisation conventions circulate — Schmidt semi-normalised, Gauss
normalised, and fully normalised — and they differ by factorials. This module
uses **Schmidt semi-normalised** $P_n^m$, so that $P_1^0 = \cos\theta$,
$P_1^1 = \sin\theta$, and the Gauss coefficients are directly comparable with
the field in nT. Section 4 of
[08-01-02](02-dipole-and-igrf.md#4-from-the-dipole-to-a-real-reference-model)
counts the coefficients; section 5 of this lesson explains what they mean
physically.

Note the immediate corollary of the radial factor: **every degree has its own,
fixed radial power law** $(a/r)^{n+2}$ for the field. The expansion is therefore
simultaneously a description in space and a statement about how the description
must be transported in radius.

## 2. Legendre functions and orthogonality

The Schmidt functions satisfy

$$P_n^m(x) = \sqrt{\frac{(2-\delta_{m0})(n-m)!}{(n+m)!}}\;(1-x^2)^{m/2}
\frac{\mathrm{d}^m P_n(x)}{\mathrm{d}x^m}, \qquad x = \cos\theta,$$

with the Condon–Shortley phase removed. Evaluated at $\theta = 60^{\circ}$
the demonstration prints

| $n$ | $m$ | $P_n^m(\cos 60^{\circ})$ |
|---|---|---|
| 1 | 0 | +0.500000 |
| 1 | 1 | +0.866025 |
| 2 | 0 | −0.125000 |
| 2 | 1 | +0.750000 |
| 2 | 2 | +0.649519 |
| 3 | 0 | −0.437500 |
| 3 | 1 | +0.132583 |
| 3 | 2 | +0.726184 |
| 3 | 3 | +0.513490 |

Check two entries by hand: $P_1^0 = \cos 60^{\circ} = 0.5$ ✔ and
$P_1^1 = \sqrt{2\cdot0!/2!}\sin 60^{\circ} = 0.866025$ ✔.

### 2.1 The orthogonality integral, and why the whole method works

The associated Legendre functions are orthogonal in the sense

$$\int_0^{\pi}\left[P_n^m(\cos\theta)\right]^2\sin\theta\,\mathrm{d}\theta
= \frac{2(2-\delta_{m0})}{2n+1},$$

and cross terms with different $(n,m)$ integrate to zero. The demonstration
evaluates this integral by 40-point Gauss–Legendre quadrature and compares with
the closed form:

| $n$ | $m$ | computed | $2(2-\delta_{m0})/(2n+1)$ |
|---|---|---|---|
| 1 | 0 | 0.666667 | 0.666667 |
| 1 | 1 | 1.333333 | 1.333333 |
| 2 | 0 | 0.400000 | 0.400000 |
| 2 | 1 | 0.800000 | 0.800000 |
| 2 | 2 | 0.800000 | 0.800000 |
| 3 | 0 | 0.285714 | 0.285714 |
| 3 | 1 | 0.571429 | 0.571429 |
| 3 | 3 | 0.571429 | 0.571429 |

This single property is the reason coefficients can be recovered from field
values: multiplying the field by a basis function and integrating over the
sphere annihilates every other term. It is also why the demonstration's
degree-1 fit recovered $g_1^0$, $g_1^1$, $h_1^1$ **exactly** even though the
synthetic field contained degree 2 — and why the same fit on four scattered
points did not (see
[08-01-02](02-dipole-and-igrf.md) §4.2 and exercise ★★6).

## 3. Forward evaluation, checked by hand

The demonstration evaluates the series for a synthetic coefficient set spanning
degrees 1 to 4 and prints, at four sites, the components and the elements:

| site (lat, lon) | $X$ (nT) | $Y$ (nT) | $Z$ (nT) | $F$ (nT) | $D$ (°) | $I$ (°) |
|---|---|---|---|---|---|---|
| (60, 10) | 12516.58 | −5928.35 | 49430.42 | 51333.97 | −25.344 | 74.348 |
| (30, 100) | 23235.43 | −4097.13 | 24172.60 | 33778.49 | −10.000 | 45.694 |
| (0, 200) | 29647.84 | 8520.37 | 1758.44 | 30897.95 | 16.034 | 3.263 |
| (−45, 300) | 22868.40 | −98.47 | −39344.39 | 45507.74 | −0.247 | −59.833 |

Section 2b of the demonstration isolates two terms at $(0^{\circ}, 0^{\circ})$,
where the algebra is short enough to check on paper. With only
$g_1^0 = -30000\ \mathrm{nT}$:

$$X = 30000.0000\ \mathrm{nT}, \qquad Z = -0.0000\ \mathrm{nT}, \qquad
I = -0.0000^{\circ}.$$

Adding $g_2^0 = +1200\ \mathrm{nT}$ changes nothing about $X$ but adds a vertical
term:

$$X = 30000.0000\ \mathrm{nT}, \qquad Z = 1800.0000\ \mathrm{nT}, \qquad
I = 3.4336^{\circ}, \qquad F = 30053.94\ \mathrm{nT}.$$

The hand check: at the equator $\cos\theta = 0$, so $S_1 = 0$ and the dipole
contributes nothing to $B_r$; meanwhile
$S_2 = g_2^0 P_2^0 = 1200\times(-0.5) = -600\ \mathrm{nT}$ and
$Z = -(n+1)S_n = -3\times(-600) = +1800\ \mathrm{nT}$. The factor $(n+1)$ is the
$B_r = -(n+1)(a/r)^{n+2}S_n$ radial derivative, and it is why a quadrupole
produces, for equal coefficients, a vertical field three times larger than a
dipole's: **higher degrees have larger radial derivatives**. The $X$ component
is unchanged because $\mathrm{d}P_2^0/\mathrm{d}\theta \propto \sin\theta\cos\theta$
vanishes at the equator.

*Sign convention note.* $P_2^0(\cos 90^{\circ}) = -0.5$ with the Schmidt
convention and $g_2^0 = +1200$ therefore gives a **downward** contribution at
this equator point. A coefficient's sign does not tell you the sign of the field
at a particular point without the Legendre value.

## 4. Degree power: the Mauersberger–Lowes spectrum

Define the degree power

$$R_n = (n+1)\sum_{m=0}^{n}\left[\left(g_n^m\right)^2 + \left(h_n^m\right)^2\right].$$

### 4.1 Where the $(n+1)$ comes from

Integrate $|\mathbf{B}|^2$ over a sphere of radius $r$. Because the harmonics are
orthogonal on the sphere, only same-degree terms survive, and for degree $n$ the
radial and tangential parts contribute in the ratio
$\left[(n+1)^2 + n(n+1)\right] = (n+1)(2n+1)$ relative to the coefficient sum.
The sphere average of $|\mathbf{B}|^2$ at $r = a$ is therefore

$$\left\langle|\mathbf{B}|^2\right\rangle
= \sum_{n=1}^{\infty}(n+1)\sum_{m=0}^{n}\left[\left(g_n^m\right)^2
+ \left(h_n^m\right)^2\right] = \sum_n R_n,$$

so $R_n$ is exactly the mean-square field contributed by degree $n$. This is why
$R_n$ is additive and why a plot of $R_n$ against $n$ is a meaningful spectrum
even though the field is not periodic in space.

### 4.2 The synthetic spectrum

| $n$ | $R_n$ (nT²) | share of total | $R_n/R_1$ |
|---|---|---|---|
| 1 | $1.85256\times10^{9}$ | 98.629% | 1.00 |
| 2 | $1.605\times10^{7}$ | 0.854% | $8.66\times10^{-3}$ |
| 3 | $7.87\times10^{6}$ | 0.419% | $4.25\times10^{-3}$ |
| 4 | $1.838\times10^{6}$ | 0.098% | $9.92\times10^{-4}$ |

Total power: $1.878318\times10^{9}\ \mathrm{nT^2}$. The dipole carries 98.63% of
it. Two cautions follow immediately.

- **The spectrum is not a physical law.** The *slope* of $R_n$ against $n$ is a
  property of the coefficient set chosen here, and any claim about "the" slope of
  the geomagnetic spectrum is a claim about the Earth, not about the mathematics.
  What the mathematics guarantees is only the additivity of $R_n$.
- **A spectrum can hide spatial structure.** Two coefficient sets with identical
  $R_n$ can differ completely in pattern: $R_n$ averages over $m$ and over
  longitude, so it cannot distinguish a concentrated anomaly from a smooth one
  of the same power. Never interpret a spectrum as a map.

## 5. Truncation: choosing a maximum degree

The demonstration truncates the synthetic field at increasing maximum degree and
measures the rms vector residual over six sites:

| $N$ | rms residual (nT) | % of rms $|\mathbf{B}|$ |
|---|---|---|
| 1 | 4669.44 | 10.85% |
| 2 | 2728.33 | 6.34% |
| 3 | 1270.39 | 2.95% |
| 4 | 0.00 | 0.00% |

The residual is monotone because the basis is orthogonal: adding a degree can
only reduce the residual. That is a luxury of this synthetic demonstration. With
real, noisy, unevenly distributed data the residual first falls and then
*rises*, because beyond some degree the fit starts to absorb noise. Choosing $N$
is therefore a bias–variance decision, not a mathematical one.

Two scales constrain the choice:

- **Spatial.** A degree-$n$ harmonic has angular wavelength $2\pi/n$, so at
  radius $r$ the linear wavelength is $\Lambda = 2\pi r/n$. Inverting,
  $n = 2\pi r/\Lambda$: at the Earth's surface ($r = 6371\ \mathrm{km}$) a
  3000 km feature needs $n \ge 13.343$, i.e. degree 14.
- **Radial.** Section 6 shows that a measurement at altitude has already lost
  the higher degrees, so no choice of $N$ can recover what the geometry removed.

## 6. Upward and downward continuation

The field at radius $r$ is obtained from the surface field by scaling degree $n$
by $\left(a/r\right)^{n+2}$:

| $n$ | factor at 100 km | factor at 400 km |
|---|---|---|
| 1 | 0.954352 | 0.833037 |
| 2 | 0.939604 | 0.783825 |
| 4 | 0.910788 | 0.693951 |
| 10 | 0.829535 | 0.481568 |
| 13 | 0.791668 | 0.401164 |

At 400 km the dipole is reduced by 16.70% and degree 13 by 59.88%. Going the
other way, from 400 km to the surface, multiplies degree 1 by **1.2004** and
degree 13 by **2.4927**. That asymmetry is the whole story of continuation:

- **Upward continuation is a smoothing and a contraction.** Every factor is
  less than one, so errors cannot grow. It is numerically safe and physically
  lossy.
- **Downward continuation is a sharpening and an amplification.** The factors
  grow without bound with $n$, so a noise component at degree 13 is amplified
  2.49 times while the signal at degree 1 is amplified 1.20 times. The
  signal-to-noise ratio of the high degrees therefore *falls* by a factor of
  about 2.08 per step. This is why downward continuation is truncated or damped,
  and it is the same geometry that makes potential-field inversion non-unique
  ([18-03-01 Why Regularisation Is Physically and Statistically Necessary](../../18-inverse-problems/03-regularization/01-why-regularize.md)).

## 7. What is *not* determined, even with perfect data

An expansion is only as unique as its boundary conditions. Three distinct
non-uniquenesses operate here, and they should not be confused.

### 7.1 Internal versus external sources at one radius

An internal (core) source of degree $n$ has radial dependence
$(a/r)^{n+2}$; an external (ionospheric, magnetospheric) source has
$(r/a)^{n-1}$. Both are equal to the *same* surface value at $r = a$. The
demonstration evaluates the degree-2 case at $r = 0.95a$:

| model | radial factor at $0.95a$ |
|---|---|
| internal source | $(a/r)^{n+2} = 1.22774$ |
| external source | $(r/a)^{n-1} = 0.95000$ |
| ratio | 1.29236 |

Two models that are **identical in surface data** differ by 29.24% in the field
below the surface. No amount of surface data alone can separate them; data at a
second radius (satellite plus surface) does, and the conditioning of that
separation degrades as the radii approach each other. This is a null space in
the strict linear-algebra sense
([18-01-03 Null Space, Non-Uniqueness and Equivalence Classes](../../18-inverse-problems/01-inverse-problem-foundations/03-null-space.md)).

### 7.2 Source distribution versus source field

The potential outside the sources determines only the field there. Any two
magnetisation distributions inside the sphere that produce the same external
field are indistinguishable, and their difference is a "silent" or annihilating
distribution. A surface field is thus a constraint on a *set* of possible source
models, not on one.

### 7.3 Truncation versus measurement

Finally, the truncation of section 5 is itself a modelling choice with a
spatially organised signature. A degree-1 model of a degree-2 field leaves a
residual of 4.87% of the rms field (measured in
[08-01-02](02-dipole-and-igrf.md) §4.2), and the four field-space residuals
tabulated there (7.23%, 11.57%, 6.52%, 11.09%) are not noise: they are structure
that the model cannot hold.

## 8. Assumptions and regime of validity

1. **Source-free region.** The expansion describes the field *outside* the
   current system that generates it. Using it inside the core is a category
   error.
2. **Spherical reference surface and a stated radius.** $a = 6371\ \mathrm{km}$
   here; coefficients are meaningless without it.
3. **Internal sources only.** Section 7.1 quantifies what is lost if external
   sources are present — as they always are, to some degree.
4. **A stated normalisation and truncation degree.** Coefficient values change
   between conventions and between truncations.
5. **Complete, noise-free, global data** are needed for the orthogonality
   argument to deliver exact coefficients. Real data are none of those things,
   which is why real models are least-squares fits with a stated uncertainty,
   not quadrature results.
6. **Time.** Coefficients are epoch-dependent; the expansion says nothing about
   dynamics ([08-01-04](04-secular-variation.md)).

## 9. Python demonstration

`code/spherical_harmonic_magnetic_demo.py` prints, with units:

1. Schmidt Legendre values and their quadrature orthogonality integrals against
   the closed form $2(2-\delta_{m0})/(2n+1)$;
2. the forward field from a synthetic degree-1-to-4 coefficient set at four
   sites, with $D$ and $I$;
3. a hand-checkable degree-1 plus degree-2 evaluation at the equator;
4. the Mauersberger–Lowes spectrum with shares and ratios;
5. measured truncation residuals for $N = 1\ldots4$;
6. continuation factors by degree at 100 km and 400 km;
7. the internal/external ambiguity factors at $r = 0.95a$.

Exercises and solutions:
[`exercises/03-spherical-harmonic-magnetic-exercises.md`](./exercises/03-spherical-harmonic-magnetic-exercises.md),
[`exercises/03-spherical-harmonic-magnetic-solutions.md`](./exercises/03-spherical-harmonic-magnetic-solutions.md).

## Mastery checkpoint

1. State the two radial solutions of Laplace's equation at degree $n$ and say
   which belongs to an internal source.
2. Evaluate $P_2^1(\cos 90^{\circ})$ and explain why the equatorial field has no
   contribution from $g_2^1$.
3. From the table in §3.2, compute $R_1$ directly from the coefficients and
   check it against $1.85256\times10^{9}\ \mathrm{nT^2}$.
4. A model is truncated at degree 6. What is the shortest wavelength it can
   represent at the surface, and at 400 km altitude?
5. Explain in three sentences why downward continuation of a noisy satellite
   field to the core–mantle boundary is a regularised inverse problem and not an
   algebraic step.

## Common pitfalls

1. **Reading $R_n$ as a map.** The spectrum is an average over longitude; it
   cannot show where the power is.
2. **Comparing $R_n$ across models with different truncation.** A spectum from a
   degree-13 model is not comparable with one from a degree-10 model without
   stating both.
3. **Ignoring the $(n+1)$ factor.** It is the origin of the radial derivative
   and it changes the relative size of degrees in $R_n$.
4. **Continuing downward without damping.** Section 6 gives the amplification
   factors; they are the reason the operation needs regularisation.
5. **Assuming surface data determines the source depth.** Section 7.1 is a
   counterexample with an exact null space.
6. **Mixing normalisation conventions.** The coefficient values differ, and so
   does the apparent spectrum.

## Related modules

- [08-01-02 The Geocentric Dipole, IGRF and WMM Models](02-dipole-and-igrf.md) —
  the degree-1 case, coefficient counts and epochs.
- [08-01-04 Secular Variation, Jerks and Core Dynamics](04-secular-variation.md) —
  the time derivative of every coefficient used here.
- [08-01-05 The Geodynamo: Mechanism and Evidence](05-dynamo-theory.md) — the
  source of the coefficients.
- [02-08 Potential Theory](../../02-physics/08-potential-theory/README.md) —
  the mathematics in full generality.
- [18-inverse-problems](../../18-inverse-problems/README.md) — null spaces,
  regularisation and uncertainty.
- [12-04-01 Observations of the Core Field and Secular Variation](../../12-global-geophysics-interior/04-geomagnetism-and-core/01-core-field-observations.md) —
  the same coefficients as a core observable.

## Self-assessment checklist

- [ ] I can write the expansion and say what each symbol is.
- [ ] I can evaluate Legendre functions and check orthogonality.
- [ ] I can compute $R_n$ and state what it is the average of.
- [ ] I can choose a truncation degree from a wavelength requirement.
- [ ] I can quote the continuation factor by degree and say which direction is
      ill-posed.
- [ ] I can describe the internal/external ambiguity with numbers.
