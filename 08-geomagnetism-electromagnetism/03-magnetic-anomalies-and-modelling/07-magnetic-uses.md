---
id: 08-03-07
title: "Applications: Mineral Exploration, Unexploded Ordnance, Archaeology"
level: advanced
prereqs: ["08-03-01", "08-03-04", "08-02-05"]
tags: [geomagnetism, electromagnetism, applications, unexploded-ordnance, archaeology, mineral-exploration, gradiometry]
---

# Applications: Mineral Exploration, Unexploded Ordnance, Archaeology

The physics of this module was built for three very different customers. A
mineral explorer wants a magnetite-rich body a kilometre down; a clearance team
wants a shell 30 cm down; an archaeologist wants a ditch 50 cm down. The physics
is identical, but the survey design, the sensor and the interpretation are set by
the **scale of the target**, and getting that scale right is most of the
practical skill. This lesson works through the three cases with the same
equations, and makes one point repeatedly: detectability is a ratio between a
signal and a noise, and both halves of that ratio have to be known.

> All models and data in this module are **SYNTHETIC**. The targets,
> susceptibilities and noise levels are chosen teaching values, and no survey or
> site is described.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the induced moment of a compact ferrous target including the
   demagnetising factor, and **state** the saturation limit of a sphere.
2. **Compute** the anomaly of a compact target at a given range and **derive**
   the maximum detection range for a stated noise level.
3. **Explain** the $r^{-3}$ scaling in terms of target moment and **use** it to
   rank targets by size.
4. **Quantify** the loss of recorded peak amplitude caused by a coarse station
   spacing, and **relate** the required spacing to the target depth.
5. **Compare** total-field and vertical-gradient surveys for resolving nearby
   targets and for rejecting a smooth regional field.
6. **Explain** why a deep large body and a shallow small body are
   indistinguishable from their anomaly and **state** the consequences for
   exploration and for clearance.
7. **State** for each of the three applications which physical property is
   measured, what the target-to-noise ratio is, and what the main failure mode
   is.

## Prerequisites

- [08-03-01 Magnetic Anomaly Physics](01-magnetic-anomaly-basics.md) — the dipole
  field, magnetisation, susceptibility.
- [08-03-04 Magnetic Forward Modelling](04-magnetic-forward-modelling.md) —
  where the dipole approximation is valid and where it is not.
- [08-02-05 Airborne Magnetic Surveys and Compensation](../02-magnetic-instruments-and-surveys/05-airborne-magnetic-surveys.md) —
  the sensors and platforms these applications use.

## 1. The induced moment of a compact target, with demagnetisation

For a compact **ferrous** target the susceptibility is large — of order $10^{2}$
for steel — and the internal field is reduced by the target's own shape. For a
sphere in a uniform field the internal field is uniform and, in SI,

$$\mathbf{H}_{\text{int}} = \frac{3}{3+\chi}\,\mathbf{H}_0,\qquad
\mathbf{M} = \chi\mathbf{H}_{\text{int}} = \frac{3\chi}{3+\chi}H_0\,\hat h_0,\qquad
m = M V = \frac{3\chi}{3+\chi}H_0 V .$$

The factor $3\chi/(3+\chi)$ is the **demagnetising factor** of a sphere. It
saturates: as $\chi \to \infty$, $M \to 3H_0$ whatever the target's composition.
For $\chi = 100$ the fraction is $3(100)/103 = 2.913$, so $M = 2.913 H_0$:
already $97\%$ of the saturation value. **Making the steel better motivated
buys almost nothing; only volume does.**

*Numerical check (SYNTHETIC).* A steel sphere of radius $5.0$ cm has
$V = \left(4/3\right)\pi a^{3} = 5.236\times10^{-4}$ m$^3$. With $\chi = 100$ and
$H_0 = 40.0$ A m$^{-1}$ (a synthetic ambient field of $50.0\ \mu$T),

$$m = 2.913 \times 40.0 \times 5.236\times10^{-4} = 6.100\times10^{-2}\ \mathrm{A\,m^{2}},
\qquad M = 116.5\ \mathrm{A\,m^{-1}}$$

against the saturation value $3H_0 = 120.0$ A m$^{-1}$. The demonstration
discretises the same sphere into 7208 cubes, sums their dipole fields, and
compares with the exact single-dipole field of that moment: the ratio is
$0.9961$ at three radii, $0.9959$ at five and $0.9958$ at ten. The $0.4\%$ deficit
is the discretisation (a staircase sphere), not a physical effect — which is
itself the point: a uniformly magnetised sphere's external field *is* a dipole
exactly, so a good integrator must reproduce one.

## 2. Detection depth

A compact target observed at range $r$ on the axis of its moment gives, in the
pole configuration,

$$\Delta T = \frac{\mu_0}{4\pi}\,\frac{2m}{r^{3}}.$$

Setting $\Delta T$ equal to a detection threshold
$\tau = 3\sigma_n$ and solving for the range gives the **maximum detection
depth** (below a sensor at the surface, and treating the range as the depth for a
target whose moment points along the field):

$$r_{\max} = \left(\frac{2\left(\mu_0/4\pi\right)m}{\tau}\right)^{1/3}.$$

With $\sigma_n = 0.10$ nT and $\tau = 0.30$ nT:

| Synthetic target | $m$ (A m$^2$) | $\Delta T$ at 1 m (nT) | Maximum range (m) |
|---|---|---|---|
| steel sphere, $r = 2$ cm | $3.90\times10^{-3}$ | 0.78 | 1.38 |
| steel sphere, $r = 5$ cm | $6.10\times10^{-2}$ | 12.20 | 3.44 |
| steel sphere, $r = 10$ cm | $4.88\times10^{-1}$ | 97.60 | 6.88 |
| iron cylinder, 0.3 m $\times$ 0.3 m | 2.47 | 494.11 | 11.81 |

The range grows as the **cube root** of the moment, which is the same statement
as the $r^{-3}$ law read backwards: to detect a target twice as deep you need
eight times the moment. A survey's specification is therefore set by the
*smallest* target it must find, and it is the small targets, not the large ones,
that decide the line spacing, the sensor height and the noise budget.

## 3. Sampling: what the station spacing does

The anomaly half-width is the only length scale the survey has to beat. For the
pole-configuration dipole profile,
$\Delta T \propto \left(2z^{2}-\rho^{2}\right)/\left(\rho^{2}+z^{2}\right)^{5/2}$,
whose half-width at half-maximum is $\sqrt{2}\,z$. For the 5 cm sphere at
$z = 0.5$ m that is $\sqrt{2}\times0.5 = 0.71$ m.

A survey cannot choose where its stations fall, so the demonstration averages the
recorded peak over 50 offsets drawn uniformly within one station spacing and
reports the worst case too:

| Spacing (m) | Samples over the anomaly | Mean loss (%) | Worst loss (%) |
|---|---|---|---|
| 0.05 | 28.3 | 0.26 | 0.74 |
| 0.10 | 14.1 | 1.06 | 2.68 |
| 0.25 | 5.7 | 5.90 | 16.42 |
| 0.50 | 2.8 | 20.71 | 48.19 |
| 0.75 | 1.9 | 35.95 | 75.57 |
| 1.00 | 1.4 | 50.62 | 90.09 |
| 2.00 | 0.7 | 82.49 | 100.05 |

Two lessons are in the table. The mean loss grows smoothly once the spacing
approaches the half-width — by 0.5 m spacing (2.8 samples per half-width) a fifth
of the peak is already gone, and by 2 m spacing the anomaly is missed entirely
about as often as it is found. And the worst case is much worse than the mean:
at 0.25 m spacing the expected loss is 5.9% but an unlucky survey loses 16.4%.
**An anomaly's amplitude is partly a property of where the stations fell**, which
is why a detection claim needs a spacing argument, not just a contour map.

## 4. Gradiometry

A **gradiometer** measures the difference between two sensors a fixed short
distance apart and therefore approximates a component of the field gradient. Two
things follow.

### 4.1 Resolution of nearby targets

Two **synthetic** dipoles of $m = 0.020$ A m$^2$ at $0.80$ m depth, separated by
a varying distance, with the metric "value halfway between the targets divided by
the largest value" (smaller is better separated):

| Separation (m) | Field | Vertical gradient |
|---|---|---|
| 0.6 | 0.760 | 0.760 |
| 1.0 | 0.690 | 0.275 |
| 1.5 | 0.236 | 0.000 |
| 2.0 | 0.042 | 0.000 |

At separations comparable with the depth the gradient separates targets the
total field merges. Both methods fail at 0.6 m, where the two dipoles are less
than a depth apart.

### 4.2 Rejection of a smooth regional field

Adding a smooth regional field (a deep body plus a linear ramp) to the same
target pair, at a separation of 1.0 m:

| Quantity | Target only | With regional | Field after linear detrend | Gradient with regional |
|---|---|---|---|---|
| Field metric | 0.690 | 0.926 | 0.616 | — |
| Gradient metric | 0.275 | — | — | 0.273 |

The gradient is **unchanged** by the regional field, because differencing removes
a smooth background; the total field is degraded from 0.690 to 0.926 and needs a
trend removal that itself risks removing target signal. That insensitivity is why
gradiometers are standard in UXO and archaeological work. The price is stated in
[03](03-reduction-to-pole.md): differentiating multiplies high-wavenumber noise
by $\left|k\right|$, so a gradiometer's advantage is a noise-ratio argument that
has to be made for each survey.

## 5. The equivalence that governs exploration

Take a reference anomaly of 200 nT produced by $m = 1.0\times10^{9}$ A m$^2$ at
1.0 km. Because $\Delta T \propto m/z^{3}$, the same anomaly at other depths
requires:

| Depth (km) | Required moment (A m$^2$) | Required volume at 5 A m$^{-1}$ (km$^3$) |
|---|---|---|
| 0.5 | $1.25\times10^{8}$ | 0.025 |
| 1.0 | $1.00\times10^{9}$ | 0.200 |
| 2.0 | $8.00\times10^{9}$ | 1.600 |
| 4.0 | $6.40\times10^{10}$ | 12.800 |

A 0.025 km$^3$ body at 500 m and a 12.8 km$^3$ body at 4 km produce
indistinguishable anomalies. This is not a technical limitation to be engineered
away — it is the structure of the forward problem, and it is why
[06 Inversion](06-magnetic-inversion.md) reports families rather than bodies. In
exploration the practical response is to add independent information
(gravity, EM, drilling); in clearance the response is to *avoid* the ambiguity
entirely by keeping the survey shallow and densely sampled, so that the depth
range of interest is narrow.

## 6. An archaeological case, with its validity stated

**Synthetic example.** A pit or kiln of susceptibility contrast
$\Delta\chi = 1.0\times10^{-3}$ (SI), volume $V = \pi\left(1.0\right)^{2}(0.5) =
1.571$ m$^3$, top at $0.5$ m depth, with the sensor at $0.3$ m above the ground.
The induced moment is

$$m = \Delta\chi\,H_0\,V = 1.0\times10^{-3}\times40.0\times1.571
= 6.28\times10^{-2}\ \mathrm{A\,m^{2}},$$

and the dipole estimate at an effective range of $0.8$ m is

$$\Delta T = \frac{\mu_0}{4\pi}\frac{2m}{r^{3}} = 10^{-7}\times
\frac{2\times6.28\times10^{-2}}{\left(0.8\right)^{3}}
= 2.45\times10^{-8}\ \mathrm{T} = 24.5\ \mathrm{nT},$$

against a sensor noise of $0.10$ nT. The target-to-noise ratio is 245, so this
target is trivially detectable — *provided the survey is dense enough that a
station lands on it* (Section 3).

**The validity caveat, in numbers.** The pit is 2 m across and the range is 0.8 m:
the range is **0.4 of the body's width**, where the dipole approximation requires
several. Section 4.2 of
[04](04-magnetic-forward-modelling.md) measured the error of the dipole
approximation for a comparable geometry at a factor of 15. So the 24.5 nT above
is an order-of-magnitude estimate, useful for planning a survey and useless for
inverting a depth. A real archaeological interpretation models the pit as a
magnetised volume.

## 7. Assumptions and regime of validity

1. **Uniformity of susceptibility within a target** and between targets. A single
   piece of steel is uniform enough; a landfill is not.
2. **A dipole target.** Requires the range to be several target widths — safe for
   a shell seen from a metre, unsafe for a pit seen from 0.8 m.
3. **A known, constant ambient field** for computing induced moments. A survey's
   own field varies by hundreds of nanoteslas across a country and by tens of
   nanoteslas diurnally; both must be removed (see
   [08-02-06 Survey Procedures](../02-magnetic-instruments-and-surveys/06-magnetic-survey-procedures.md)).
4. **Sensor noise known and stationary.** Every detection range in this lesson is
   a ratio to it.
5. **No overlapping targets.** Two shells in the same footprint produce a
   composite anomaly that is not the sum of two dipoles in any simple sense.
6. **Line spacing matched to the target depth.** Quantified in Section 3; this is
   the most common cause of a "missed" target that was in the ground.

## 8. Python demonstration

`code/magnetic_uses_demo.py`:

1. computes the demagnetisation-limited moment of a sphere and verifies the exact
   dipole field by a 7208-cube volume sum ($0.4\%$ discretisation deficit);
2. tabulates $\Delta T$ at 1 m and the maximum detection range for four synthetic
   targets at 0.10 nT noise;
3. measures the mean and worst recorded-peak loss against station spacing;
4. compares field and vertical-gradient resolution of two nearby dipoles, and the
   rejection of a smooth regional field;
5. tabulates the depth–moment equivalence;
6. computes an archaeological estimate and states its geometric validity limit.

```bash
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python magnetic_uses_demo.py
```

Fixed seed, print-only, exits 0.

## 9. Exercises

[`exercises/07-magnetic-uses-exercises.md`](./exercises/07-magnetic-uses-exercises.md)
and
[`exercises/07-magnetic-uses-solutions.md`](./exercises/07-magnetic-uses-solutions.md).

## Mastery checkpoint

Without notes:

> A **synthetic** clearance survey must find a steel sphere of radius 3 cm at
> depths up to 1.5 m. **(a)** Compute its induced moment for $\chi = 100$ and
> $H_0 = 40$ A m$^{-1}$, and the saturation-limited value it approaches as
> $\chi\to\infty$. **(b)** Compute the anomaly at 1.5 m and decide the maximum
> sensor noise that still gives a $3\sigma$ detection. **(c)** Choose a station
> spacing, using the half-width rule, and justify it with a number from the
> sampling table. **(d)** State one advantage of a gradiometer for this survey and
> one cost. **(e)** State what the survey cannot determine about the target, and
> why.

## Common pitfalls

1. **Assuming the target's susceptibility is what limits detectability.** It
   saturates within a factor of 1.03; volume and range do the work.
2. **Using the dipole formula at a range comparable with the target size.**
   Measured error: a factor of 15 in the demonstration of
   [04](04-magnetic-forward-modelling.md).
3. **Reporting a detection depth without the noise level.** Every range in
   Section 2 is a ratio to $\sigma_n$.
4. **Sampling more coarsely than the half-width.** The mean loss is 20% at 2.8
   samples per half-width and 82% at 0.7.
5. **Treating a deep anomaly as a large deposit.** Depth and volume trade
   exactly (Section 5).
6. **Believing a gradiometer is immune to noise.** It is immune to *smooth*
   fields, and it amplifies high-wavenumber noise.

## Related modules

- [01 Magnetic Anomaly Physics](01-magnetic-anomaly-basics.md) — the equations
  reused here.
- [04 Magnetic Forward Modelling](04-magnetic-forward-modelling.md) — the
  validity limit of the dipole approximation used throughout.
- [05 Magnetic Depth Estimation](05-magnetic-depth-estimation.md) — what can be
  said about the depth of these targets.
- [06 Magnetic Inversion](06-magnetic-inversion.md) — the deep-large versus
  shallow-small equivalence in general form.
- [05-05 Survey Design and Acquisition](../../05-core-geophysics/05-survey-design-and-acquisition/README.md) —
  line spacing, sampling theory and coverage as general design problems.
