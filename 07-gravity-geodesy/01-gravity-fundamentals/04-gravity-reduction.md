---
id: 07-01-04
title: "Gravity Reductions: Free-Air, Bouguer, Isostatic and Terrain"
level: advanced
prereqs: ["07-01-03", "05-02-04", "05-06-03"]
tags: [gravity, geodesy, free-air, bouguer, terrain-correction, reduction, gravity-anomaly]
---

# Gravity Reductions: Free-Air, Bouguer, Isostatic and Terrain

**All models and data in this module are SYNTHETIC.** The hill, the valley, the
station, the densities, the profile and the reading are chosen teaching values. No
survey, station or dataset is reproduced. The only exact quantities used are
$G = 6.67430\times10^{-11}\ \mathrm{m^{3}\,kg^{-1}\,s^{-2}}$, the unit relation
$1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$, and the four WGS84 defining
constants used to build normal gravity.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the free-air correction from the gradient of normal gravity, and
   **explain** why the coefficient depends on latitude and on the adopted radius.
2. **Derive** the Bouguer slab correction $2\pi G\rho h$ from the attraction of an
   infinite plate, and **quantify** how a finite body approaches it.
3. **Compute** terrain corrections for a hill and for a valley from the ring
   formula, and **verify** the closed forms numerically.
4. **Derive** the observed gravity gradient over a uniform-density surface,
   $-\mathrm{d}\gamma/\mathrm{d}h + 2\pi G\rho$, and **explain** what it implies
   for the elevation dependence of free-air and Bouguer anomalies.
5. **Apply** a Nettleton-type scan to choose a Bouguer density, and **measure**
   how the choice is biased when the geology correlates with the terrain.
6. **Assemble** a complete reduction for a station and **rank** the errors
   contributed by elevation, latitude, terrain and assumed density.
7. **State** precisely which parts of the reduction are measurements, which are
   model assumptions, and which are conventions.

## Prerequisites

- [07-01-03 Reference Ellipsoid, Normal Gravity and Clairaut's Theorem](03-normal-gravity.md)
  — normal gravity, the free-air gradient, and the latitude correction used here.
- [05-02-04 Reduction of Observations](../../05-core-geophysics/02-geophysical-fields-and-observables/04-reduction-of-observations.md)
  — the general idea of reducing a measurement to a common reference.
- [05-06-03 Static and Datum Corrections](../../05-core-geophysics/06-data-processing-principles/03-static-and-datum.md)
  — the processing-sequence framing that this lesson instantiates for gravity.

## 1. What a reduction is, and what it is not

A gravimeter returns a number at a place and a time. Everything between that
number and a statement about rocks is a **reduction**: a sequence of subtractions
and additions, each of which removes a known or modelled effect. The reductions in
this lesson are:

| step | removes | depends on |
|---|---|---|
| normal gravity $\gamma(\varphi)$ | the latitude and reference-ellipsoid effect | the adopted system |
| free air | the height of the station above the ellipsoid | $\mathrm{d}\gamma/\mathrm{d}h$ |
| Bouguer slab | the attraction of the rock between station and datum | an **assumed density** |
| terrain | the difference between the real topography and the slab | a digital elevation model and a density |
| isostasy | the deep compensation of topography | a **model** of compensation |

Three of the five inputs are models, not measurements. This is the honest core of
the lesson: **a gravity anomaly is a statement about a difference between a
measurement and a model**, so its value changes when the model changes, and no
amount of instrument precision removes that. The reduction does not create
information; it compares data with a hypothesis about everything that is *not* the
target.

## 2. The free-air correction

Normal gravity on the ellipsoid is $\gamma(\varphi)$. A station at height $h$ above
the ellipsoid measures a value reduced by the vertical gradient of *normal*
gravity — the part that has nothing to do with the rocks:

$$\mathrm{FA} = -\frac{\mathrm{d}\gamma}{\mathrm{d}h}\,h,
\qquad
\frac{\mathrm{d}\gamma}{\mathrm{d}h} = -\frac{2\gamma(\varphi)}{a}
\left(1 + f + m - 2f\sin^{2}\varphi\right).$$

The demonstration evaluates this for the reference constants

| latitude | $\mathrm{d}\gamma/\mathrm{d}h$ (mGal/m) |
|---|---|
| $0^\circ$ | $0.308769$ |
| $45^\circ$ | $0.308555$ |
| $90^\circ$ | $0.308339$ |

**Where does the familiar $0.3086$ come from?** Decompose it honestly:

- The spherical part $2\gamma/a$ at $45^\circ$ is $0.307494\
  \mathrm{mGal\,m^{-1}}$; the factor
  $(1 + f + m - 2f\sin^{2}\varphi)$ adds $+0.001061\ \mathrm{mGal\,m^{-1}}$
  ($+0.344\%$).
- A *spherical* model with $R = 6371\ \mathrm{km}$ and $g = 9.820250\
  \mathrm{m\,s^{-2}}$ gives $2g/R = 0.308280\ \mathrm{mGal\,m^{-1}}$.

So the difference between $0.3083$ and $0.3086$ is dominated by the choice of
reference radius and reference gravity, not by the flattening. Quoting a free-air
coefficient without those choices is quoting one member of a family. For the
station elevation used later:

| elevation $h$ (m) | free-air correction (mGal) |
|---|---|
| 100 | 30.855 |
| 1200 | 370.266 |
| 3000 | 925.665 |

At 1200 m the correction is already $0.038\%$ of the whole field, and it is far
larger than any target anomaly in a typical survey. Note also that the free-air
correction is *not* purely a correction for the station being further from the
Earth's centre: it lumps together the direct inverse-square effect and the
centrifugal and ellipsoidal geometry.

## 3. The Bouguer slab: $2\pi G\rho h$

Consider an infinite horizontal plate of uniform density $\rho$ and thickness $h$,
and an observation point on its upper surface. Every element has a vertical
attraction component; integrating over the plate gives

$$g_{\text{slab}} = 2\pi G\rho h,
\qquad 2\pi G\rho = 0.111969\ \mathrm{mGal\,m^{-1}}\ \text{for }
\rho = 2670\ \mathrm{kg\,m^{-3}}.$$

**Derivation.** For a ring at horizontal distance $s$ and a slab element at depth
$z$, the vertical component of the attraction is
$G\,\mathrm{d}M\,z/\left(s^{2}+z^{2}\right)^{3/2}$, and integrating over $s$ from
$0$ to $\infty$ and $z$ from $0$ to $h$ gives $2\pi G\rho h$ independent of $h$'s
position in space — which is why it is *the* slab formula. The Bouguer correction
is the negative of this: $\mathrm{BC} = -2\pi G\rho h$.

**How finite must the plate be?** The demonstration computes the attraction at the
centre of the top face of a cylinder of radius $R$ and height $h$, exactly:

$$g_{\text{cyl}} = 2\pi G\rho\left[h + R - \sqrt{R^{2}+h^{2}}\right],$$

and for a flat disk the same integral gives
$2\pi G\rho h\left(1 - h/\sqrt{R^{2}+h^{2}}\right)$. Measured for $h = 1200\ \mathrm{m}$:

| $R/h$ | cylinder (mGal) | fraction of the slab value | disk (mGal) |
|---|---|---|---|
| 1 | 78.7077 | 0.585786 | — |
| 3 | 112.5585 | 0.837722 | — |
| 10 | 127.6611 | 0.950124 | 120.9929 |
| 20 | 131.0055 | 0.975016 | 127.6528 |
| 50 | 133.0190 | 0.990001 | 131.6758 |

At $R/h = 10$ the cylinder is $5\%$ short of the slab value and the *thin* disk is
$10\%$ short; at $R/h = 50$ both are within $2\%$. The practical rule that follows
from the measured numbers: **the slab correction is a good approximation only where
the terrain extends at least several tens of times the station's height**, and the
number of heights required is a measurement, not a tradition.

## 4. Terrain corrections

Where the ground is not a flat plate, the difference between the real topography
and the plate must be restored. Two exactly solvable cases make the size of the
effect clear. Both are derived from the same ring integral

$$\mathrm{d}g = 2\pi G\rho\;\frac{s\,z}{\left(s^{2}+z^{2}\right)^{3/2}}\,
\mathrm{d}s\,\mathrm{d}z$$

that produced the slab, only with finite limits.

### 4.1 Station on a cylindrical hill

A station at the centre of the flat top of a cylinder of height $H$ and radius
$R$ measures $g_{\text{cyl}} = 2\pi G\rho\left[H + R - \sqrt{R^{2}+H^{2}}\right]$
from the cylinder, while the plate of thickness $H$ would have given
$2\pi G\rho H$. The terrain correction is the difference,

$$\boxed{\;T_{\text{hill}} = 2\pi G\rho\left[\sqrt{R^{2}+H^{2}} - R\right]
\;>\, 0.}$$

With the SYNTHETIC geometry $H = 60\ \mathrm{m}$, $R = 300\ \mathrm{m}$,
$\rho = 2670\ \mathrm{kg\,m^{-3}}$: $\sqrt{R^{2}+H^{2}} = 305.9412\ \mathrm{m}$, so
$\sqrt{R^{2}+H^{2}} - R = 5.9412\ \mathrm{m}$ and

$$T_{\text{hill}} = 0.111969 \times 5.9412 = 0.6652\ \mathrm{mGal}.$$

### 4.2 Station on the floor of a cylindrical valley

Now the surroundings are above the station, and the plate assumed mass in the
valley that is not there. The same integral gives

$$\boxed{\;T_{\text{valley}} = 2\pi G\rho\left[H + R - \sqrt{R^{2}+H^{2}}\right]
\;>\, 0,}$$

which for the same geometry is $0.111969 \times (60 + 300 - 305.9412) =
6.0529\ \mathrm{mGal}$ — an order of magnitude larger than the hill case. The
asymmetry is physical, not arithmetic: the missing mass in the valley is
*directly beneath* the station, where the vertical component of an attraction is
largest, while the hill's extra mass is off to the side.

### 4.3 Numerical verification

The demonstration integrates the ring formula directly for the hill case and
obtains $6.0493\ \mathrm{mGal}$ for the cylinder and therefore
$T = 6.7181 - 6.0493 = 0.6689\ \mathrm{mGal}$, against the closed form
$0.6652\ \mathrm{mGal}$: agreement to $0.0036\ \mathrm{mGal}$, which is the
quadrature error of a modest grid. **The terrain correction is always positive**,
it is a fraction of a milligal for gentle relief, and it becomes dominant in
rugged terrain where the station sits in a valley.

## 5. The observed gradient over a uniform surface

A useful composite that explains the shape of the reduced anomalies, and
do: over a surface of uniform density, moving the station up by $\mathrm{d}h$
removes the normal-gravity term and *adds* the attraction of the extra rock,

$$\frac{\mathrm{d}g_{\text{obs}}}{\mathrm{d}h}
= -\frac{\mathrm{d}\gamma}{\mathrm{d}h} + 2\pi G\rho
= -0.308555 + 0.111969 = -0.196586\ \mathrm{mGal\,m^{-1}}.$$

The consequences, measured:

| quantity | gradient (mGal/m) |
|---|---|
| observed $g$ over uniform rock | $-0.196586$ |
| free-air anomaly | $+0.111969$ |
| simple Bouguer anomaly | $0.000000$ |

Two readings of the same table:

- The free-air anomaly *mirrors elevation*: a plateau 1000 m high shows a
  $+112\ \mathrm{mGal}$ free-air anomaly with no geological signal at all. This is
  not an anomaly in the interpretable sense.
- The simple Bouguer anomaly is flat by construction, which is exactly what the
  slab correction was designed to achieve, and why the Bouguer anomaly is the
  interpretable quantity in the intermediate-wavelength band.

The residual elevation dependence of the *complete* Bouguer anomaly is therefore
not $0.1966\ \mathrm{mGal\,m^{-1}}$ — it is near zero for uniform rock and becomes
nonzero only through the density error, the terrain, and real geological or
isostatic variation. Getting this wrong is one of the standard confusions in the
subject, and the table settles it.

## 6. Choosing the Bouguer density

The reduction contains an assumed density, and the anomaly depends on it linearly:
at 1200 m a $300\ \mathrm{kg\,m^{-3}}$ error changes the anomaly by
$-15.0969\ \mathrm{mGal}$. The classical method for choosing it (Nettleton) is to
scan candidate densities and pick the one that makes the anomaly least correlated
with elevation, on the assumption that the *geology* is not controlled by the
topography.

The demonstration runs that experiment on SYNTHETIC data with a known density
$2750\ \mathrm{kg\,m^{-3}}$, 61 stations between 200 and 800 m, noise of
$0.051\ \mathrm{mGal}$, and two different geological signals:

| case | correlation of geology with elevation | recovered density | error |
|---|---|---|---|
| geology uncorrelated | $+0.052$ | $2775$ | $+25\ \mathrm{kg\,m^{-3}}$ |
| geology aligned with terrain | $+1.000$ | $2875$ | $+125\ \mathrm{kg\,m^{-3}}$ |

In the first case the scan recovers the truth to one grid step ($25\
\mathrm{kg\,m^{-3}}$) and the residual $|$correlation$|$ at the optimum is
$0.0022$. In the second case the optimum still has $|$correlation$| = 0.5984$ and
the density is biased by $+125\ \mathrm{kg\,m^{-3}}$: **the method fails in exactly
the situation it was invented for**, a geological signal that follows the
topography. Reporting the residual correlation therefore matters more than
reporting the density, because it is the diagnostic of whether the assumption held.

A second, independent handle is available in practice: where rock samples or a
borehole exist, the density is measured and the scan becomes a check rather than
the primary determination.

## 7. Worked example — one complete reduction

SYNTHETIC station: latitude $45^\circ$, elevation $1200\ \mathrm{m}$, reading
$979\,500.0000\ \mathrm{mGal}$ on top of the cylinder of Section 4.1, with the
deliberately wrong density $2450\ \mathrm{kg\,m^{-3}}$ so the density sensitivity
is visible.

| step | value (mGal) | note |
|---|---|---|
| observed reading | $979\,500.0000$ | measurement |
| minus normal gravity | $-980\,619.7769$ | $\gamma(45^\circ)$ from the closed form |
| plus free air | $+370.2659$ | $0.308555 \times 1200$ |
| plus Bouguer | $-123.2914$ | $-0.102743 \times 1200$ |
| plus terrain | $+0.6652$ | closed form of Section 4.1 |
| **complete Bouguer anomaly** | $\mathbf{-872.1373}$ | $\pm$ the errors below |

Error budget, each measured by the demonstration:

| error source | size | anomaly error (mGal) |
|---|---|---|
| 1 m of elevation | typical for a hand-held GNSS height | $\pm 0.1966$ |
| 10 m of elevation | no differential GNSS | $\pm 1.9659$ |
| $300\ \mathrm{kg\,m^{-3}}$ of density | plausible in unconsolidated cover | $\mp 15.0969$ |
| $0.1^\circ$ of latitude | $11\ \mathrm{km}$ of position error | $\pm 9.0512$ |
| terrain ignored | the SYNTHETIC hill | $\mp 0.6652$ |

The ranking is the lesson: **the assumed density and the latitude dominate, in
that order, and the terrain correction that everyone worries about is the smallest
term.** The instrument's own precision does not appear in the table, because it is
not the limiting factor.

## 8. Isostatic reduction, and its different logical status

The isostatic reduction removes the gravity effect of the *deep compensation* of
topography, which is why it belongs to a different category: it uses a model of
the subsurface, not a measurement of it. Two cases:

- Over a mountain with an Airy root, the Bouguer anomaly is negative by
  approximately $2\pi G(\rho_{m}-\rho_{c})t$, where $t$ is the root thickness.
  Lesson [06](06-isostasy.md) derives $t = h\rho_{c}/(\rho_{m}-\rho_{c})$ and
  computes this term; the reader should note that its magnitude (hundreds of
  milligal for a few kilometres of relief) is the largest term in the entire
  reduction after normal gravity and elevation.
- The **isostatic anomaly** is what remains after removing the modelled
  compensation. It is *not* an anomaly in the same sense as the Bouguer anomaly:
  it is a residual with respect to a hypothesis, and a nonzero isostatic anomaly
  is evidence about the hypothesis as much as about the rocks.

This is the honest ordering of the reductions by epistemic status:

1. normal gravity, free air — a convention plus a derived formula;
2. Bouguer slab, terrain — a definite approximation with a stated density;
3. isostatic — a model with free parameters and a contested history;
4. the residual — the only part that is a measurement of the target.

## 9. Assumptions and regime of validity

1. **Uniform slab density.** Real overburden varies with lithology and compaction;
   the single-density slab is an approximation whose error grows with the
   elevation range and the density range.
2. **The station's height is above the ellipsoid**, and the free-air coefficient
   applies to a *small* height. The $h^{2}$ term of lesson
   [03](03-normal-gravity.md) is $+3h^{2}/a^{2}$ relative: $+1.157\ \mathrm{mGal}$
   at 4 km, which matters for microgal work.
3. **The plate extends far enough.** Measured in Section 3: several tens of times
   the station height, or the terrain correction must absorb the difference.
4. **The terrain model is accurate.** The terrain correction is computed from a
   digital elevation model, so it inherits that model's errors, resolution and
   datum.
5. **The observations are on the physical surface**, not on a tower or a platform,
   unless the platform's height is carried in the free-air term.
6. **Latitude and longitude are known** to better than the anomaly's tolerance,
   because the latitude gradient is $0.8131\ \mathrm{mGal\,km^{-1}}$ at
   $45^\circ$: a 100 m positional error is already $0.08\ \mathrm{mGal}$.
7. **Horizontal accelerations are absent.** For a stationary station this is
   assumed, and for moving platforms it is the dominant problem (module
   [02](../02-gravity-instruments-and-surveys/README.md), lesson 5).
8. **The density is a model.** Section 6 measures the cost of getting it wrong.

## 10. Python demonstration

`code/gravity_reduction_demo.py` computes and prints, with units:

1. free-air coefficients at three latitudes, $0.308769$, $0.308555$,
   $0.308339\ \mathrm{mGal\,m^{-1}}$, and the decomposition of the familiar
   $0.3086$;
2. the slab coefficient $0.111969\ \mathrm{mGal\,m^{-1}}$ and the convergence of
   finite bodies, cylinder and disk;
3. terrain corrections for a hill ($0.6652\ \mathrm{mGal}$) and a valley
   ($6.0529\ \mathrm{mGal}$), verified by direct quadrature to
   $0.0036\ \mathrm{mGal}$;
4. the Nettleton scan in both a favourable and an unfavourable case;
5. the observed/anomaly gradients $-0.196586$, $+0.111969$ and $0.000000$
   $\mathrm{mGal\,m^{-1}}$;
6. a complete reduction with an error budget.

Exercises and solutions:
[`exercises/04-gravity-reduction-exercises.md`](exercises/04-gravity-reduction-exercises.md),
[`exercises/04-gravity-reduction-solutions.md`](exercises/04-gravity-reduction-solutions.md).

## Mastery checkpoint

Answer without notes.

> A SYNTHETIC station at $50^\circ$ latitude, elevation $2200\ \mathrm{m}$,
> reads $980\,651.000\ \mathrm{mGal}$; the Bouguer density is taken as
> $2600\ \mathrm{kg\,m^{-3}}$ and terrain is assumed negligible. **(a)** Compute
> the free-air and Bouguer corrections, using
> $\gamma(50^\circ) = 981\,070.2136\ \mathrm{mGal}$. **(b)** Compute the complete
> Bouguer anomaly. **(c)** State the three largest error sources and their sizes.
> **(d)** Explain in one sentence what a free-air anomaly of the same station would
> look like and why.

A worked version of (a)–(c) is in the
[solutions](exercises/04-gravity-reduction-solutions.md).

## Common pitfalls

1. **Applying $0.3086\ \mathrm{mGal\,m^{-1}}$ as if it were fundamental.** It
   depends on the adopted $a$, $\gamma$ and latitude; Section 2 measures the
   contributions.
2. **Sign errors in the free-air versus Bouguer corrections.** The free-air
   correction is added, the Bouguer correction is subtracted; mixing them changes
   the anomaly by twice the term.
3. **Thinking the Bouguer anomaly has a $0.1966\ \mathrm{mGal\,m^{-1}}$ elevation
   dependence.** Section 5 measures the three gradients and shows that this number
   belongs to the *observed* field, not to the reduced anomaly.
4. **Ignoring terrain because "it is small".** It is small in gentle relief and
   dominant for a station in a valley — the two cases differ by an order of
   magnitude at the same relief.
5. **Treating the Bouguer density as known.** It is the largest single source of
   anomaly error in the worked example.
6. **Forgetting that the terrain correction is always positive.** A negative
   computed value indicates a sign or geometry error.
7. **Confusing the isostatic anomaly with a data anomaly.** One is a residual
   against a model of the deep Earth.
8. **Mixing ellipsoidal with orthometric heights** in the free-air term; the
   difference is the geoid undulation, which is metres.

## Related modules

- [Module 01 — Gravity Fundamentals](README.md) — this module; lesson
  [03](03-normal-gravity.md) supplies normal gravity and lesson
  [06](06-isostasy.md) the isostatic reductions.
- [Module 02 — Gravity Instruments and Surveys](../02-gravity-instruments-and-surveys/README.md) —
  the acquisition side, including the practical processing sequence of lesson 4
  of that module.
- [05-02 Reduction of Observations](../../05-core-geophysics/02-geophysical-fields-and-observables/04-reduction-of-observations.md) —
  the same logic in other methods.
- [07-03-01 Interpreting Anomalies](../03-gravity-anomalies-and-modelling/01-anomaly-interpretation.md) —
  what to do with the reduced number.
- [Module 04 — Geodesy and Reference Frames](../04-geodesy-reference-frames/README.md) —
  height systems, without which the free-air term is ambiguous.
