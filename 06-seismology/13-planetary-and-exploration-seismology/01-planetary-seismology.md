---
id: 06-13-01
title: "Planetary Seismology: InSight and Lunar Seismic Experiments"
level: doctoral
prereqs: ["06-01-02", "06-02-02", "04-08-03"]
tags: [seismology, planetary-seismology, single-station, polarisation, location, InSight, Moon]
---

# Planetary Seismology: InSight and Lunar Seismic Experiments

Planetary seismology asks the questions terrestrial seismology asks — where did
the event occur, what is the structure, how large was it — with one instrument,
no permanent network, and no ability to deploy a second station where the
physics would most like one. The missions that motivate this lesson (the Apollo
lunar seismic experiments and the InSight lander) are the reason the subject
exists; **this module quotes no numbers from them**. Everything below is a
synthetic straight-ray model, and its purpose is to establish what a single
three-component seismometer can and cannot determine, on any planet.

The honest difficulty is a counting argument that turns into a statement about
bias. A single station records an arrival time, an S−P time, and a polarisation.
Those three observations are not three locations. One of them constrains a
*range* (and a range is a curve in the map of possible hypocentres), and the
polarisation constrains a *direction* only in combination with an assumed
velocity model. With no velocity model at all there is a one-parameter family of
exact fits, and its spread is a factor of more than two in epicentral distance.
That is the central point: **single-station location is an inference conditional
on a model, not a measurement.**

All models and data in this module are **SYNTHETIC**. No real station, event,
waveform or planetary dataset is used.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the relation between the S−P time and the slant range, and
   **explain** why a time difference constrains a range rather than a position.
2. **Derive** the polarisation incidence relation $\Delta = h\tan i$ and
   **compute** how a polarisation error propagates into the epicentral distance.
3. **Quantify** the velocity-model dependence of a single-station location, and
   **show** that the effect of a 1% velocity error exceeds the effect of a
   realistic pick error.
4. **Count** observations and unknowns to determine whether a single station can
   locate an event, and **construct** the family of models that fit the record
   exactly when it cannot.
5. **Compute** the fractional sensitivity $\mathrm{d}\ln\Delta/\mathrm{d}i =
   2/\sin 2i$ and **identify** the geometries in which polarisation is strong
   and where it carries no information at all.
6. **Explain** why a second station collapses the trade-off through geometry
   rather than through station count, and **compute** the perpendicular
   uncertainty from a baseline.
7. **State** which quantities a single station does determine well, and design a
   monitoring rule around them.

## Prerequisites

- [06-01-02 P and S Waves](../01-elastic-wave-propagation/02-p-and-s-waves.md) —
  P and S polarisations, and why a three-component station can separate them.
- [06-02-02 Snell's Law and Layered Media](../02-ray-theory-and-travel-times/02-snell-and-layering.md) —
  ray geometry; this lesson uses the straight-ray limit of it.
- [04-08-03 Planetary Geophysics from Orbiters and Landers](../../04-earth-science-geology/08-planetary-science/03-planetary-geophysics-missions.md) —
  what a lander can carry, and why the instrument count is what it is.

## 1. What one station records

A three-component station at the surface records six numbers for each event: a
detection, an S−P time difference, an azimuth, and an incidence angle (from the
ratio of vertical to horizontal motion). The synthetic model of this lesson —
chosen for transparency, not for realism — is straight rays in a homogeneous
half-space:

$$t_P = \frac{R}{V_p}, \qquad t_S = \frac{R}{V_s}, \qquad
R = \sqrt{\Delta^{2} + h^{2}}, \qquad \tan i = \frac{\Delta}{h},$$

where $\Delta$ is the epicentral distance, $h$ the source depth, $R$ the slant
range and $i$ the incidence angle from the vertical measured at the source.
Subtracting the first two,

$$\boxed{\;t_S - t_P = R\left(\frac{1}{V_s} - \frac{1}{V_p}\right)
= R\,\frac{V_p - V_s}{V_p V_s}\;}$$

so the S−P time is a **range** measurement with a sensitivity set entirely by the
two velocities. Two consequences follow immediately, and they are the ones that
survive into layered models:

- the range depends on $V_p$ and $V_s$ through the *difference of reciprocals*,
  so it is controlled by $V_p/V_s$ rather than by either velocity alone;
- a source at depth $h$ and a source at epicentral distance $\Delta$ that give
  the same $R$ are indistinguishable to the S−P time. **Depth and distance are
  inseparable from this observable**, whatever the pick quality.

*SYNTHETIC example.* With $V_p = 6.00\ \mathrm{km\,s^{-1}}$,
$V_s = 3.46\ \mathrm{km\,s^{-1}}$, $\Delta = 40.0\ \mathrm{km}$,
$h = 10.0\ \mathrm{km}$:

$$R = \sqrt{40.0^{2} + 10.0^{2}} = \sqrt{1700} = 41.2311\ \mathrm{km},$$
$$t_P = \frac{41.2311}{6.00} = 6.8718\ \mathrm{s}, \qquad
t_S = \frac{41.2311}{3.46} = 11.9165\ \mathrm{s}, \qquad
t_S - t_P = 5.0446\ \mathrm{s},$$
$$\tan i = \frac{40.0}{10.0} = 4.0 \;\Rightarrow\;
i = 75.9638^{\circ}.$$

Every one of those numbers is printed by
[`code/planetary_single_station_demo.py`](code/planetary_single_station_demo.py).

## 2. The range–depth trade-off

Invert the S−P relation: for a measured $t_S - t_P$ and a *fixed* depth $h$, the
epicentral distance is determined. But if $h$ is unknown, the measurement only
pins down $R$, and the locus of $({\Delta}, h)$ with
$\sqrt{\Delta^{2}+h^{2}} = R$ is a circle in the $\Delta$–$h$ plane. The
demonstration tabulates the pairs that fit one measured $t_S - t_P$ to within a
$50\ \mathrm{ms}$ pick uncertainty:

| $\Delta$ (km) | $h$ required (km) to match $t_S - t_P$ |
|---|---|
| 5.0 | 40.515 |
| 10.0 | 39.579 |
| 20.0 | 35.587 |
| 40.0 | 8.153 |
| 60.0 | 0.000 |
| 80.0+ | 0.000 |

Read the table twice. First, it is a *curve*: many physically different sources
reproduce the measured time difference to within the pick error, including a
source $40\ \mathrm{km}$ away at $8\ \mathrm{km}$ depth and a source
$10\ \mathrm{km}$ away at nearly $40\ \mathrm{km}$ depth. Second, the same
$50\ \mathrm{ms}$ pick uncertainty is a **$0.99\%$ constraint on the range**:
the admissible range interval is $40.822$–$41.640\ \mathrm{km}$ around a true
value of $41.231\ \mathrm{km}$. A $1\%$ distance constraint sounds excellent
until it is remembered that the distance is only one coordinate of the answer,
and that the *other* coordinate (depth) is what the same data leave almost free.

## 3. Adding polarisation: what collapses, and what it costs

Add the observed incidence angle. With the velocity model assumed, the pair
$(\Delta, h)$ is then over-determined and collapses onto a point: the
demonstration recovers $\Delta = 40.0000\ \mathrm{km}$,
$h = 10.0000\ \mathrm{km}$ exactly when it is given the true velocities.

The words "with the velocity model assumed" are doing all the work. Perturb the
model while keeping both observations fixed, and the answer moves:

| $V_p/V_s$ error | $\Delta$ recovered (km) | $h$ recovered (km) | $\mathrm{d}\Delta$ |
|---|---|---|---|
| $-10\%$ | 52.3711 | 13.0928 | $+30.93\%$ |
| $-5\%$ | 45.3571 | 11.3393 | $+13.39\%$ |
| $-1\%$ | 40.9677 | 10.2419 | $+2.42\%$ |
| $0\%$ | 40.0000 | 10.0000 | $0.00\%$ |
| $+1\%$ | 39.0769 | 9.7692 | $-2.31\%$ |
| $+5\%$ | 35.7746 | 8.9437 | $-10.56\%$ |
| $+10\%$ | 32.3567 | 8.0892 | $-19.11\%$ |

**A $1\%$ error in $V_p/V_s$ moves the epicentral distance by $2.31\%$ — at
$40\ \mathrm{km}$ that is hundreds of metres, and the sign of the error is not
knowable from the record.** Compare the $50\ \mathrm{ms}$ pick error, which
produced a $0.99\%$ range constraint: in a planetary setting the velocity model
is the dominant error term, not the picking.

## 4. Counting observations and unknowns

Make the model uncertainty explicit by counting:

| quantity | count |
|---|---|
| unknowns: $\Delta$, $h$, $V_p$, $V_s$ | 4 |
| observations: $t_P$, $t_S - t_P$, incidence angle | 3 |
| degrees of freedom | 1 |

One degree of freedom remains, so the solution set is a **curve**, not a point.
The demonstration constructs it by assuming a series of velocities:

| assumed $V_p$ ($\mathrm{km\,s^{-1}}$) | implied $V_s$ | $\Delta$ (km) | $h$ (km) | implied $t_P$ (s) |
|---|---|---|---|---|
| 3.00 | 1.73 | 20.00 | 5.00 | 6.8718 |
| 4.00 | 2.31 | 26.67 | 6.67 | 6.8718 |
| 5.00 | 2.88 | 33.33 | 8.33 | 6.8718 |
| 6.00 | 3.46 | 40.00 | 10.00 | 6.8718 |
| 7.00 | 4.04 | 46.67 | 11.67 | 6.8718 |
| 8.00 | 4.61 | 53.33 | 13.33 | 6.8718 |

Every row reproduces the entire record — including the P arrival time, which is
why the family is a curve parameterised by the velocity rather than a plane.
Over a plausible $V_p$ span of $3$–$8\ \mathrm{km\,s^{-1}}$ the epicentral
distance ranges from $20.0$ to $53.3\ \mathrm{km}$, **a factor of $2.67$**, with
no observational discriminant anywhere in the record. This is the quantitative
statement of "single-station location is a modelling problem".

## 5. Where polarisation is strong, and where it is useless

Differentiate the geometry. From $\Delta = h\tan i$,

$$\frac{\mathrm{d}\Delta}{\mathrm{d}i} = h\sec^{2} i
\qquad\text{(absolute, depends on } h\text{)},$$

$$\frac{\mathrm{d}\ln \Delta}{\mathrm{d}i} = \frac{2}{\sin 2i}
\qquad\text{(fractional, independent of } h\text{)}.$$

The fractional form is the useful one: it says how much a polarisation error
costs, as a fraction of the answer, with no reference to the scale of the
problem. It is **minimised at $i = 45^{\circ}$** ($\sin 2i = 1$) and grows toward
both the near-vertical and the near-horizontal limits. Measured on the
demonstration's grid:

| $\Delta/h$ | $i$ (deg) | $\mathrm{d}\Delta/\mathrm{d}i$ (km/deg) | $\mathrm{d}\ln\Delta/\mathrm{d}i$ (%/deg) |
|---|---|---|---|
| 0.25 | 14.04 | 2.967 | 7.42 |
| 0.50 | 26.57 | 1.745 | 4.36 |
| 0.75 | 36.87 | 1.454 | 3.64 |
| 1.00 | 45.00 | 1.396 | 3.49 |
| 1.50 | 56.31 | 1.513 | 3.78 |
| 2.00 | 63.43 | 1.745 | 4.36 |
| 5.00 | 78.69 | 3.630 | 9.08 |
| 10.00 | 84.29 | 7.051 | 17.63 |

Two honest readings, both printed by the demonstration:

- **For an event at $\Delta \sim h$** ($i \approx 45^{\circ}$) a $1^{\circ}$
  polarisation error costs about **$3.5\%$ of the distance** — the best case
  available. A polarisation measured to $5^{\circ}$ therefore already limits a
  single-station distance to $\sim 17\%$.
- **For a near-horizontal ray** ($\Delta \gg h$) the cost rises to $17.6\%$ per
  degree, and **for a near-vertical ray** the distance is barely determined at
  all, because $\Delta = h\tan i$ is then almost independent of $h$: a deep event
  almost directly beneath the station moves the incidence angle very little when
  it moves horizontally.

The widely repeated claim that polarisation makes a single station sufficient is
true only in a band of geometries around $i = 45^{\circ}$, and it is *always*
conditional on the velocity model of §3.

## 6. A second station is geometry, not count

A $50\ \mathrm{ms}$ pick uncertainty on $t_S - t_P$ is a range uncertainty of

$$\sigma_R = \frac{\sigma_t}{1/V_s - 1/V_p}
= \frac{0.050}{0.289017 - 0.166667}
= \frac{0.050}{0.122351} = 408.7\ \mathrm{m}.$$

Two stations separated by a baseline $b$ provide two ranges. For a source at
perpendicular distance $d$ from the baseline, the two ranges differ by an amount
whose sensitivity to $d$ is $d/r$ (with $r$ the half-baseline-to-source
distance), so the perpendicular uncertainty is

$$\sigma_d \approx \sigma_R\,\frac{r}{d}.$$

Measured:

| $b$ (km) | $d$ (km) | $r$ (km) | $\sigma_d$ (m) | $\sigma_d/b$ |
|---|---|---|---|---|
| 10.0 | 0.5 | 5.02 | 4107.0 | 0.4107 |
| 10.0 | 1.0 | 5.10 | 2083.8 | 0.2084 |
| 10.0 | 5.0 | 7.07 | 577.9 | 0.0578 |
| 10.0 | 20.0 | 20.62 | 421.2 | 0.0421 |
| 50.0 | 5.0 | 25.50 | 2083.8 | 0.0417 |
| 50.0 | 20.0 | 32.02 | 654.2 | 0.0131 |
| 50.0 | 100.0 | 103.08 | 421.2 | 0.0084 |

A source near the baseline is very poorly located perpendicular to it —
$\sigma_d/b = 0.41$ for $b = 10\ \mathrm{km}$, $d = 0.5\ \mathrm{km}$ — **no
matter how good the picks are**, because the two ranges differ by too little to
locate the source's offset. Adding stations along the *same* line does not fix
this: azimuthal **coverage** fixes it. That is why planetary single-station
experiments are supplemented by an independent constraint on $R$ (a velocity
model, a second phase such as a surface reflection, or a known source depth)
rather than by a better sensor.

## 7. What a single station does determine well

Two things, and both are worth designing a mission around:

- **Back-azimuth.** The horizontal polarisation gives the direction of the ray
  from the station, and it is not coupled to the velocity model (it is a
  direction, not a distance). Measured azimuth scatter versus per-component
  signal-to-noise:

| S/N per horizontal component | azimuth s.d. (deg) | 90th percentile error (deg) |
|---|---|---|
| 2.0 | 20.166 | 33.095 |
| 5.0 | 8.012 | 13.129 |
| 10.0 | 4.040 | 6.687 |
| 50.0 | 0.804 | 1.328 |
| 200.0 | 0.204 | 0.335 |

  The azimuth is a **back-azimuth**: it is the direction from which the energy
  came, not a source location, and it is the one geometric quantity a single
  station gives cheaply.

- **Detection and relative timing.** With a known velocity model, a
  single station still yields ranges and hence a radial distance; with several
  events it yields structure along many ray paths. Most of the scientific return
  of a single-station experiment comes from these *relative* measurements, not
  from absolute locations.

A practical statement of the same result: if the mission goal is hypocentres,
the design requirement is not "a good three-component sensor" but "a velocity
model good enough that a $1\%$ error moves the distance by less than the
scientific target", or "a second observing geometry".

## 8. Worked numeric examples

### Example 1 — the range and its uncertainty

For $\Delta = 25.0\ \mathrm{km}$, $h = 15.0\ \mathrm{km}$,
$V_p = 5.80\ \mathrm{km\,s^{-1}}$, $V_s = 3.30\ \mathrm{km\,s^{-1}}$:

$$R = \sqrt{25.0^{2} + 15.0^{2}} = \sqrt{850} = 29.1548\ \mathrm{km},$$
$$t_S - t_P = 29.1548\left(\frac{1}{3.30} - \frac{1}{5.80}\right)
= 29.1548 \times (0.303030 - 0.172414) = 29.1548 \times 0.130616
= 3.808\ \mathrm{s}.$$

A $40\ \mathrm{ms}$ pick error maps to

$$\sigma_R = \frac{0.040}{0.130616} = 306.2\ \mathrm{m} =
0.31\ \mathrm{km},$$

a $1.05\%$ range constraint — the same structure as the demonstration's
$0.99\%$, as it must be, since both are $\sigma_t$ divided by the reciprocal
difference.

### Example 2 — the cost of a velocity error

The same event is located with $V_s$ overestimated by $3\%$
($V_s' = 3.399\ \mathrm{km\,s^{-1}}$), keeping the measured $t_S - t_P$. The new
reciprocal difference is $1/3.399 - 1/5.80 = 0.294204 - 0.172414 = 0.121790$, so

$$R' = \frac{3.808}{0.121790} = 31.267\ \mathrm{km},$$

an error of $+2.11\ \mathrm{km}$, or $+7.25\%$ in range. **A $3\%$ velocity error
produces a $7\%$ distance error** — 20 times larger than the pick error of
Example 1. The amplification factor here, $7.25/3 = 2.4$, is the ratio of the
velocity change to the change in the reciprocal difference; it is always of order
unity or larger, and its sign is not recoverable from the record.

### Example 3 — polarisation sensitivity at two geometries

Take $h = 8\ \mathrm{km}$. For $\Delta = 8\ \mathrm{km}$ ($i = 45^{\circ}$),
$\mathrm{d}\ln\Delta/\mathrm{d}i = 2/\sin 90^{\circ} = 2.00$ per radian
$= 2.00/57.296 = 3.49\%$ per degree, matching the table. For
$\Delta = 80\ \mathrm{km}$ ($\Delta/h = 10$, $i = 84.289^{\circ}$),
$\mathrm{d}\ln\Delta/\mathrm{d}i = 2/\sin(168.578^{\circ})
= 2/0.198014 = 10.100$ per radian $= 17.63\%$ per degree. The polarisation
measurement is five times more valuable for the near event than for the far one,
at the same station and the same pick precision.

## 9. Assumptions and regime of validity

1. **Straight rays in a homogeneous half-space.** Valid only at distances small
   enough that the ray curvature is negligible; at regional distances a layered
   model and converted phases are required, and the incidence angle no longer
   maps onto $\Delta/h$ in the simple way used here.
2. **A known, correct velocity model** wherever a location is quoted. §3 and §4
   are the quantification of what "assumed" costs.
3. **No free-surface conversion.** A real vertical component contains P, SV and
   the free-surface response; the synthetic polarisation here is the incident-ray
   value.
4. **A point source with an isotropic radiation pattern.** Real sources radiate
   directionally, which biases both amplitude and apparent polarisation.
5. **Polarisation measured at source incidence, not at the sensor.** In a
   layered structure the ray bends between source and receiver, so the measured
   surface incidence is not the source incidence; using one for the other is a
   systematic error of the same order as the velocity error of §3.
6. **One event.** Multi-event joint location with an unknown common structure is
   a different (and weaker-constrained) problem, and does not remove the
   degeneracy of §4 by itself.

## 10. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| epicentral distance | $\Delta$ | km | |
| depth | $h$ | km | |
| slant range | $R$ | km | $\sqrt{\mathrm{km^{2}}}$ |
| travel time | $t$ | s | $\mathrm{km}/(\mathrm{km\,s^{-1}})$ |
| reciprocal difference | $1/V_s - 1/V_p$ | $\mathrm{s\,km^{-1}}$ | |
| range uncertainty | $\sigma_R$ | km | $\mathrm{s}/\mathrm{s\,km^{-1}}$ |
| incidence | $i$ | rad or deg | from $\arctan(\Delta/h)$ |
| fractional sensitivity | $\mathrm{d}\ln\Delta/\mathrm{d}i$ | $\mathrm{rad^{-1}}$ | $2/\sin 2i$ |

The check that matters: the S−P time is a range divided by a velocity
*difference*, so a large $V_p - V_s$ makes the observable sensitive to distance
and a small one makes it insensitive. For a Poisson solid with $V_p/V_s = \sqrt{3}$
the reciprocal difference is
$1/V_s - 1/V_p = (1 - V_s/V_p)/V_s = 0.42265/V_s$; if a medium approached
$V_p = V_s$ the observable would vanish, which is why an S−P time is useless in a
fluid.

## 11. Python demonstration

[`code/planetary_single_station_demo.py`](code/planetary_single_station_demo.py)
implements the whole lesson. Section A is the range–depth trade-off curve;
section B adds polarisation and then perturbs the velocity model; section C
removes the velocity model entirely and exhibits the one-parameter family;
section D measures the fractional polarisation sensitivity against $\Delta/h$;
section E computes the two-station perpendicular uncertainty and shows that
geometry, not station count, is the constraint; section F measures the azimuth
error versus signal-to-noise. Its closing summary lists every number quoted in
this lesson.

Full sets with worked solutions are in
[`exercises/01-planetary-seismology-exercises.md`](exercises/01-planetary-seismology-exercises.md)
and
[`exercises/01-planetary-seismology-solutions.md`](exercises/01-planetary-seismology-solutions.md).

## Mastery checkpoint

Without notes:

> A single station on a planetary surface records an S−P time of
> $4.20\ \mathrm{s}$ and an incidence angle of $60^{\circ}$, with
> $V_p = 5.50\ \mathrm{km\,s^{-1}}$ and $V_s = 3.20\ \mathrm{km\,s^{-1}}$ and a
> pick uncertainty of $\sigma_t = 0.06\ \mathrm{s}$. **(a)** Compute the slant
> range and its uncertainty with units. **(b)** Compute $\Delta$ and $h$.
> **(c)** Recompute $\Delta$ if $V_p/V_s$ is $2\%$ too large, and compare the
> change with the range uncertainty from (a). **(d)** How many degrees of
> freedom remain if the velocity model is also unknown, and what does that
> imply for a quoted single-station hypocentre? **(e)** State two measurements
> that would break the degeneracy and the assumption each one carries.

A worked version appears in the
[solutions](exercises/01-planetary-seismology-solutions.md).

## Common pitfalls

1. **Quoting a single-station hypocentre without the velocity model.** The model
   is part of the result.
2. **Treating the S−P time as a location.** It is a range (§1).
3. **Believing polarisation removes the trade-off.** It removes it *given* the
   velocity model, and at a cost of $\sim 3.5\%$ per degree in the best case
   (§5).
4. **Adding stations along one line.** Coverage, not count (§6).
5. **Using surface incidence as source incidence.** They differ by the ray
   bending (§9).
6. **Forgetting that a deep source beneath the station is the worst case for
   polarisation**, not the best (§5).
7. **Reporting an azimuth as a location.** It is a back-azimuth (§7).

## Related modules

- [06-04 Earthquake Location and Magnitude](../04-earthquake-location-and-magnitude/README.md) —
  the multi-station version of this problem, and the geometry that makes it work.
- [06-02 Ray Theory and Travel Times](../02-ray-theory-and-travel-times/README.md) —
  the ray geometry this lesson uses in its straight-ray limit.
- [06-13 Planetary and Applied Seismology Frontiers](README.md) — this module.
- [04-08 Planetary Science and Comparative Planetology](../../04-earth-science-geology/08-planetary-science/README.md) —
  the bodies and missions whose interiors the method is applied to.

## Self-assessment checklist

- [ ] I can derive $t_S - t_P = R(1/V_s - 1/V_p)$ and invert it.
- [ ] I can compute $\sigma_R$ from a pick uncertainty with units.
- [ ] I can construct the $(\Delta, h)$ family that fits one measurement.
- [ ] I can propagate a $V_p/V_s$ error into a distance error.
- [ ] I can derive and evaluate $2/\sin 2i$ and say where it is worst.
- [ ] I can compute a two-station perpendicular uncertainty from a baseline.
- [ ] I can state the two quantities a single station determines well.
