---
id: 15-02-05
title: "Marine Gravity and Magnetic Surveys"
level: graduate
prereqs: ["07-01-04", "07-02-05", "08-03-01"]
tags: [oceanography, marine-geophysics, marine-gravity, magnetics, eotvos, free-air, bouguer, dipole]
---

# Marine Gravity and Magnetic Surveys

> **All models and data in this module are SYNTHETIC.** The densities, dipole
> moment and body geometry are chosen teaching values, printed by the
> demonstration in `code/`. No survey, chart, satellite model, magnetic model or
> published anomaly is reproduced. The constants used ($G$, $\Omega$, $R$,
> $\mu_0$, the knot) are standard values with units.

Potential-field methods measure the Earth's field *from a platform in motion*.
That is the defining difficulty of both, and it is why a marine gravity survey
spends as much effort on the platform's acceleration as on the gravimeter, and
why an airborne magnetic survey is more often limited by how well the aircraft's
position and attitude are known than by the magnetometer's noise.

This lesson derives the two corrections that make a moving-platform measurement
usable — the **Eötvös correction** for gravity and the **free-air and Bouguer
reductions** for the depth — and then the dipole field that underlies the
magnetic method. Both derivations use only standard constants, which is the point:
the coefficients that appear in survey practice are not magic numbers but
arithmetic on $\Omega$, $R$, $G$ and $\mu_0$.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the Eötvös correction
   $\Delta g = 2\Omega V\cos\phi\sin\alpha + V^{2}/R$ from the centrifugal and
   curvature accelerations of a moving platform, and **compute** both coefficients
   in mGal per knot.
2. **Compute** the free-air gradient $-2g/R$ and the Bouguer slab attraction
   $2\pi G\rho h$, and **state** which of the two requires a known depth and which
   requires a known density.
3. **Reduce** a synthetic station to a free-air and a Bouguer anomaly, and
   **state** the sign conventions.
4. **Assemble** a marine gravity error budget and **identify** which term
   dominates.
5. **Derive** the geocentric dipole field
   $B = B_0\sqrt{1+3\sin^{2}\lambda}$ and the inclination relation
   $\tan I = 2\tan\lambda$, and **state** what they do and do not represent.
6. **Compute** the anomaly of a vertical dipole body, **locate** its zero
   crossing, and **explain** why an inclined magnetisation skews the pattern and
   why reduction to the pole needs the magnetisation direction.
7. **Distinguish** a modelled field from a measured one in writing.

## Prerequisites

- [07-01-04 Gravity Corrections and Reductions](../../07-gravity-geodesy/01-gravity-fundamentals/04-gravity-reduction.md) —
  the drift, latitude, free-air and Bouguer corrections on land.
- [07-02-05 Airborne and Marine Gravity](../../07-gravity-geodesy/02-gravity-instruments-and-surveys/05-airborne-marine-gravity.md) —
  the instruments and their moving-platform behaviour.
- [08-03-01 Magnetic Anomalies: The Basics](../../08-geomagnetism-electromagnetism/03-magnetic-anomalies-and-modelling/01-magnetic-anomaly-basics.md) —
  the field, the anomaly and the reduction to the pole.

## 1. The Eötvös correction, derived

A gravimeter measures the magnitude of the *measured* acceleration, which on a
moving platform is gravity plus two kinematic accelerations:

- the change in centrifugal acceleration caused by the platform's eastward
  velocity component $u$: this contributes an upward (radially outward)
  acceleration $2\Omega\cos\phi\,u$, so the measured $g$ is *reduced* by it;
- the curvature acceleration of the platform's path, $V^{2}/R$, also radially
  outward.

Writing $u = V\sin\alpha$ with $\alpha$ the heading measured from north:

$$\boxed{\;\Delta g = -\left[2\Omega\cos\phi\,V\sin\alpha + \frac{V^{2}}{R}\right],\;}$$

and converting to the units of practice — mGal ($10^{-5}\ \mathrm{m\,s^{-2}}$)
and knots ($1\ \mathrm{kn} = 0.514444\ \mathrm{m\,s^{-1}}$):

$$E = 7.503\,V\cos\phi\sin\alpha + 0.004154\,V^{2}\ \mathrm{mGal}
\qquad (V \text{ in knots}).$$

Both coefficients are **derived** in the demonstration:

$$2\Omega \times 10^{5} \times 0.514444
= 2(7.292115\times10^{-5})(10^{5})(0.514444) = 7.5028\ \mathrm{mGal\,kn^{-1}},$$

$$\frac{10^{5}(0.514444)^{2}}{6.371\times10^{6}} = 0.004154\
\mathrm{mGal\,kn^{-2}},$$

and they agree with the conventional values quoted in practice to $3\times10^{-3}$
and $<10^{-6}$ respectively — the residual being the rounded constants used here.

| speed (kn) | heading (deg) | latitude (deg) | $E$ (mGal) |
|---|---|---|---|
| 6 | 0 | 30 | $+0.15$ |
| 6 | 45 | 30 | $+27.72$ |
| 6 | 90 | 30 | $+39.14$ |
| 6 | 270 | 30 | $-38.84$ |
| 10 | 90 | 30 | $+65.39$ |
| 10 | 270 | 30 | $-64.56$ |

Two structural properties matter. The **$V^{2}$ term is always positive** (the
platform is pushed outward, so it reads less gravity), independent of heading and
latitude. The **linear term vanishes on north–south headings and reverses between
east and west** — which is exactly why a survey is steered on reciprocal headings
so that the term cancels along a line and its residual, not its magnitude, is what
enters the error budget.

## 2. Free-air and Bouguer reductions

$$g(h) \approx g(0)\left(1 - \frac{2h}{R}\right)
\;\Longrightarrow\;
\frac{\mathrm{d}g}{\mathrm{d}h} = -\frac{2g}{R}
= -\frac{2(9.80665)}{6.371\times10^{6}} = -0.30785\
\mathrm{mGal\,m^{-1}},$$

$$g_{\text{slab}} = 2\pi G\rho h .$$

| $h$ (m) | $2\pi G\rho h$ at $\rho = 2500\ \mathrm{kg\,m^{-3}}$ (mGal) |
|---|---|
| 10 | 1.0483 |
| 50 | 5.2417 |
| 100 | 10.4835 |
| 500 | 52.4175 |

**Which needs what.** The free-air correction needs the **depth** (or height), and
nothing else; the Bouguer correction needs the depth *and* a **density**, and the
density is the quantity the survey is usually trying to determine. That asymmetry
is the source of the standard caveat that a Bouguer anomaly is only as good as its
assumed density.

A worked reduction with $g_{\text{ref}} = 981\,000.000$ mGal at sea level, a
station in $1200\ \mathrm{m}$ of water, a density contrast of $2500 - 1030\
\mathrm{kg\,m^{-3}}$, and a synthetic crustal anomaly of $+20.0$ mGal:

| step | value |
|---|---|
| observed $g$ | $980\,650.5767$ mGal |
| free-air correction | $+369.4233$ mGal |
| **free-air anomaly** | $+20.0000$ mGal — the crustal signal, recovered exactly |
| Bouguer correction | $73.9715$ mGal |
| **simple Bouguer anomaly** | $-53.9715$ mGal |

The free-air reduction removes the whole of the 1200 m of missing rock and returns
the crustal signal **provided the depth is known**. The Bouguer reduction then
removes the attraction of the rock between the station and the datum using the
assumed density contrast. Note the conservative convention: in the marine case the
water is *already* there, so the density contrast is between rock and water, not
rock and air.

## 3. An error budget for a marine gravity survey

| term | contribution (mGal) |
|---|---|
| gravimeter reading noise | 0.200 |
| Eötvös, speed error $0.1$ kn at 10 kn | 0.539 |
| Eötvös, heading error $1^\circ$ on an east–west line at $45^\circ$N | 0.926 |
| depth error 0.5 m through the free-air gradient | 0.154 |
| datum and drift | 0.300 |
| tide and ocean-loading model | 0.100 |
| **total (quadrature)** | **1.145** |

**The Eötvös terms dominate.** The heading term alone (0.926 mGal) exceeds the
instrument noise (0.200 mGal) by a factor 4.6, and the total is 1.145 mGal — so
improving the gravimeter beyond about 1.13 mGal would buy nothing at all. This is
the characteristic shape of a moving-platform error budget and the reason modern
systems invest in GNSS-derived acceleration and attitude rather than in quieter
sensors.

## 4. The geocentric dipole field

The field of a centred dipole of moment $m$ is, in magnitude,

$$\boxed{\;B(\lambda) = \frac{\mu_0 m}{4\pi R^{3}}\sqrt{1 + 3\sin^{2}\lambda},\;}$$

with $\lambda$ the magnetic latitude, and the inclination $I$ satisfies

$$\tan I = 2\tan\lambda .$$

With the demonstration's chosen synthetic moment $m = 8.0\times10^{22}\
\mathrm{A\,m^{2}}$:

| latitude | $B$ (nT) | inclination (deg) |
|---|---|---|
| $0^\circ$ | 30936.2 | 0.00 |
| $15^\circ$ | 33902.5 | 28.19 |
| $30^\circ$ | 40924.8 | 49.11 |
| $45^\circ$ | 48914.5 | 63.43 |
| $60^\circ$ | 55771.1 | 73.90 |
| $75^\circ$ | 60298.2 | 82.37 |
| $90^\circ$ | 61872.4 | 90.00 |

Three facts follow from the closed form and are worth testing because they are the
properties actually used:

- **the polar field is exactly twice the equatorial field** ($61872.4$ against
  $30936.2$ nT) — a direct consequence of $\sqrt{1+3\sin^{2}\lambda}$;
- **the inclination sweeps $0^\circ$ to $90^\circ$** with $\tan I = 2\tan\lambda$:
  this is the relation that lets a *palaeolatitude* be read from a fossil
  magnetisation direction;
- **both are properties of the dipole assumption, not of the field.** A real field
  contains a non-dipole part that is a large fraction of the total and is obtained
  from a spherical-harmonic model. Nothing in this section substitutes for such a
  model, and no number here should be compared with a real measurement.

## 5. A magnetic anomaly over a dipole body

For a vertical dipole of moment $m$ at depth $d$, the vertical-component anomaly
along a profile at offset $x$ is

$$B_a(x) = \frac{\mu_0 m}{4\pi}\frac{2d^{2} - x^{2}}{(x^{2}+d^{2})^{5/2}} .$$

With $m = 6.0\times10^{10}\ \mathrm{A\,m^{2}}$ and $d = 3000$ m:

| $x$ (m) | $B_a$ (nT) | | $x$ (m) | $B_a$ (nT) |
|---|---|---|---|---|
| $-6000$ | $-7.95$ | | $0$ | $+444.44$ |
| $-4000$ | $+3.84$ | | $2000$ | $+137.85$ |
| $-3000$ | $+39.28$ | | $3000$ | $+39.28$ |
| $-2000$ | $+137.85$ | | $4000$ | $+3.84$ |

Peak positive anomaly $444.44$ nT at the epicentre; the anomaly is **symmetric**
about $x = 0$ and crosses zero where $x^{2} = 2d^{2}$, i.e. at
$|x| = \sqrt{2}\,d = 4243$ m. Both are testable consequences of the formula rather
than properties of the body.

**What a real survey sees.** A vertical dipole anomaly is symmetric and bipolar
with the positive lobe over the body. An *inclined* magnetisation — which is the
normal case away from the magnetic poles, because the inducing field is inclined —
rotates and skews that pattern, shifting the positive lobe and adding a negative
one asymmetrically. **Reduction to the pole** transforms the observed anomaly into
what it would look like under a vertical field, and it requires the magnetisation
direction as an input. If that direction is assumed rather than known — the usual
situation, because it depends on the rock's remanence — the reduced anomaly is a
model output presented as data.

## 6. Assumptions and regime of validity

1. **A spherical, non-rotating reference for the reduction.** The Eötvös
   derivation treats the platform's path as circular of radius $R$; the true path
   is an ellipsoid, which changes the $V^{2}$ coefficient by a fraction of a per
   cent — comparable to the effect being corrected.
2. **A point measurement.** A ship's gravimeter averages over its beam and over
   the swell-induced motion; the "station" is a smoothed quantity.
3. **A normal-gravity reference model.** Every anomaly is a difference from a
   reference field, and a change of reference changes every anomaly by a smooth
   function. The choice must be stated.
4. **An infinite-slab Bouguer correction.** Valid where the slab is wide relative
   to its thickness; a poor approximation over a narrow seamount or a steep slope.
5. **A density contrast.** The Bouguer anomaly is conditional on it.
6. **A centred dipole for the magnetic field.** No non-dipole terms, no secular
   variation, no crustal field.
7. **No remanence for the body.** The anomaly is computed for *induced*
   magnetisation in the ambient field; remanent magnetisation is common and can
   dominate, in which case the effective direction is not the ambient one.
8. **No self-demagnetisation, no magnetic viscosity, no anisotropy.** All are
   second-order for a first look.

## 7. Worked examples

### Example 1 — the Eötvös term on an east–west line

A survey at $60^\circ$N steaming east at 10 kn on a heading $\alpha = 90^\circ$:

$$E = 7.503(10)\cos 60^\circ \sin 90^\circ + 0.004154(100)
= 37.515 + 0.415 = 37.93\ \mathrm{mGal}.$$

On the reciprocal heading ($\alpha = 270^\circ$) it is $-37.10$ mGal. **Averaging
the two headings removes the linear term to first order and leaves $+0.415$ mGal**
— the $V^{2}$ term, which is why a survey line is normally flown or steamed in
both directions and the pair averaged.

### Example 2 — how deep is the body?

A symmetric magnetic anomaly's zero crossings are separated by $2\sqrt{2}\,d$. A
real survey reports crossings 8 km apart:

$$d = \frac{8000}{2\sqrt{2}} = 2828\ \mathrm{m} \approx 2.8\ \mathrm{km}.$$

This is the classic **half-width rule** in its cleanest form, and its limitation is
worth stating in the same breath: it is exact only for a vertical dipole, so it is
a *depth scale* rather than a depth, and for a body of finite extent it returns
something between the top and the centre of mass.

### Example 3 — the effect of getting the heading wrong

A $2^\circ$ heading error at 10 kn, $45^\circ$N:

$$E_{\text{err}} = 7.503(10)\cos 45^\circ \sin 2^\circ
= 53.06 \times 0.03490 = 1.852\ \mathrm{mGal}.$$

Against a total budget of 1.145 mGal, that single error would use the whole budget.
**The heading requirement is the binding constraint on a marine gravity survey**,
not the gravimeter.

## 8. Python demonstration

`code/marine_gravity_magnetics_demo.py` prints everything above with units:

1. the Eötvös correction derived from $\Omega$, $R$ and the knot, with the
   heading- and latitude-dependence tabulated;
2. the free-air gradient and the Bouguer slab table, then a full worked reduction
   that recovers an injected crustal anomaly exactly;
3. a six-term error budget, combined in quadrature;
4. the dipole field and inclination against latitude, with the polar/equatorial
   factor-of-two check;
5. the anomaly profile of a vertical dipole body, with its peak and its zero
   crossing at $\sqrt{2}d$;
6. verification: the derived coefficients against the conventional values
   ($0.003\,\%$ and $<10^{-6}$ agreement), the dipole field against its closed
   form, a unit check on the Eötvös term, and the symmetry of the anomaly.

Run it with

```bash
cd 15-oceanography-marine/02-marine-geophysics-methods/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python marine_gravity_magnetics_demo.py
```

Print-only, no network, fixed seed `np.random.default_rng(20261014)`, exit 0, in
under a second.

## 9. Exercises

Full sets with worked solutions are in
[`exercises/05-marine-gravity-magnetics-exercises.md`](exercises/05-marine-gravity-magnetics-exercises.md)
and
[`exercises/05-marine-gravity-magnetics-solutions.md`](exercises/05-marine-gravity-magnetics-solutions.md).

- ★ Derive the linear Eötvös coefficient and evaluate the correction for a 12 kn
  eastward line at $35^\circ$N.
- ★★ Compute the free-air and Bouguer corrections for a seabed station at
  $2500\ \mathrm{m}$ depth with a density contrast of $1800 - 1030\
  \mathrm{kg\,m^{-3}}$.
- ★★ Compute the dipole field and inclination at $20^\circ$ and $70^\circ$ magnetic
  latitude with the demonstration's moment, and check the polar/equatorial ratio.
- ★★★ Design a gravity survey whose Eötvös error budget is below 0.5 mGal, stating
  the heading and speed tolerances and how you would achieve them.

## Mastery checkpoint

Without notes, and showing your arithmetic. Use $\Omega = 7.292115\times10^{-5}\
\mathrm{s^{-1}}$, $R = 6.371\times10^{6}$ m, $g = 9.80665\ \mathrm{m\,s^{-2}}$,
$G = 6.674\times10^{-11}$, $\mu_0 = 4\pi\times10^{-7}$, $1\ \mathrm{kn} =
0.514444\ \mathrm{m\,s^{-1}}$.

> A survey steams at 8 kn on a heading of $70^\circ$ from north at $50^\circ$N.
> **(a)** Compute the Eötvös correction in mGal, both terms separately.
> **(b)** Compute the Eötvös error produced by a $3^\circ$ heading error, and state
> whether it exceeds a 1 mGal budget.
> **(c)** Compute the free-air and Bouguer corrections for a seabed station at
> $800\ \mathrm{m}$ depth with a density contrast of $2200 - 1030\
> \mathrm{kg\,m^{-3}}$, and state which one needs the density.
> **(d)** A symmetric magnetic anomaly has zero crossings 6 km apart. Compute the
> dipole's depth and state one assumption that makes the number a depth *scale*
> rather than a depth.

A worked version of (a)–(d) is in the lesson-05
[solutions](exercises/05-marine-gravity-magnetics-solutions.md).

## Common pitfalls

1. **Ignoring the Eötvös correction or applying it with the wrong sign.** It
   subtracts; a platform moving east reads *less* gravity.
2. **Forgetting the $V^{2}$ term because it is heading-independent.** It is small
   at 6 kn (0.15 mGal) and not at 12 kn (0.60 mGal).
3. **Treating a Bouguer anomaly as data.** It depends on an assumed density.
4. **Comparing anomalies computed against different reference fields.** The
   difference is smooth, large and invisible in the anomalies themselves.
5. **Using a half-width rule as a depth measurement.** It is exact only for a
   vertical dipole and only for a point body.
6. **Reducing to the pole without knowing the magnetisation direction.** For a
   body with remanence, the reduced anomaly is a model output.
7. **Quoting a dipole field as "the Earth's field".** The non-dipole part is a
   large fraction of the total.

## Related modules

- [01 Marine Seismic Reflection: Airguns, Streamers, Processing](01-marine-seismic-reflection.md) —
  the method that images the *shape* of the bodies this lesson measures by their
  density and magnetisation.
- [02 Multibeam Bathymetry and Swath Mapping](02-multibeam-bathymetry.md) —
  the bathymetry that the free-air and Bouguer reductions require.
- [Module 15-03 Seafloor Tectonics and Structure](../03-seafloor-tectonics/README.md) —
  the crustal structure these fields are inverted for.
- [07-01-04 Gravity Corrections and Reductions](../../07-gravity-geodesy/01-gravity-fundamentals/04-gravity-reduction.md) —
  the land-based treatment of the same corrections.
- [07-05-01 GRACE and GRACE-FO](../../07-gravity-geodesy/05-satellite-gravimetry/01-grace-gracefo.md) —
  the satellite view of the same field, with the opposite resolution trade.
- [08-02-05 Airborne Magnetic Surveys](../../08-geomagnetism-electromagnetism/02-magnetic-instruments-and-surveys/05-airborne-magnetic-surveys.md) —
  the aeromagnetic version, where the altitude problem replaces the Eötvös one.

## Self-assessment checklist

- [ ] I can derive the Eötvös coefficients from $\Omega$, $R$ and the knot.
- [ ] I can state which term cancels on reciprocal headings and why.
- [ ] I can compute free-air and Bouguer corrections and state their inputs.
- [ ] I can assemble and read a marine gravity error budget.
- [ ] I can derive the dipole field and the inclination relation.
- [ ] I can compute a dipole anomaly and locate its zero crossing.
- [ ] I can state what reduction to the pole requires as an input.
