---
id: 15-02-02
title: "Multibeam Bathymetry and Swath Mapping"
level: advanced
prereqs: ["15-01-01", "15-02-01", "05-05-04"]
tags: [oceanography, marine-geophysics, multibeam, swath, bathymetry, footprint, sound-speed, attitude]
---

# Multibeam Bathymetry and Swath Mapping

> **All models and data in this module are SYNTHETIC.** The sonar parameters,
> depths and attitudes used here are chosen teaching values, printed by the
> demonstration in `code/`. No survey, vessel, chart or acquisition specification
> is reproduced, and no published accuracy standard is quoted.

A multibeam echo sounder measures the seafloor by timing acoustic pulses in many
directions at once. The measurement per beam is trivial — a two-way travel time
and an angle — and everything difficult lies in converting those two numbers into
a position on the seafloor. That conversion needs a sound speed, an attitude, a
position, and a timing; **each of those comes with an error, and the depth error
scales with the depth.**

That gives the method a property no amount of care removes: a multibeam system's
*resolution* varies by a factor of four across a single swath, and its *depth
accuracy* is a fraction of the depth rather than a fixed length. This lesson
derives both, and shows that the errors that dominate depend on whether the
survey is shallow (attitude-limited) or deep (sound-speed-limited).

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the swath width $2z\tan\theta_{\max}$ and **state** why the
   width-to-depth ratio is a property of the beam angle alone.
2. **Derive** the across-track footprint $z\,\Delta\theta/\cos^{2}\theta$ and the
   along-track footprint $R\,\Delta\phi$, and **quantify** the factor by which
   resolution degrades at the swath edge.
3. **Show** that a fractional sound-speed error is an equal fractional *range*
   error, and **compute** the resulting depth error at a stated depth.
4. **Convert** a roll, pitch or heave error into a cross-track or vertical
   displacement, and **state** which of these is not distinguishable from real
   bathymetry.
5. **Compute** a sounding density and choose a grid cell from the across-track
   beam spacing, **stating** the trade-off that choice makes.
6. **Assemble** a depth-error budget in quadrature and **identify** which term
   dominates in shallow and in deep water.
7. **Distinguish** a scale error (which moves a whole swath coherently) from a
   geometry error (which grows toward the swath edges).

## Prerequisites

- [15-01-01 Seawater Properties: Temperature, Salinity, Density](../01-physical-oceanography/01-seawater-properties.md) —
  the sound speed that the whole conversion depends on.
- [15-02-01 Marine Seismic Reflection: Airguns, Streamers, Processing](01-marine-seismic-reflection.md) —
  the same travel-time geometry in reflection profiling.
- [05-05-04 Positioning, GNSS and Navigation](../../05-core-geophysics/05-survey-design-and-acquisition/04-positioning-gnss.md) —
  the position that turns ranges and angles into soundings.

## 1. What a swath sounder measures

A multibeam system transmits a fan of acoustic energy across the track and
receives it on an array that resolves the returning energy into many beams. Per
beam it obtains

- a **two-way travel time** $t$, from which a **slant range** $R = ct/2$ is
  computed with an assumed sound speed $c$;
- a **beam angle** $\theta$ from vertical, from the arrival direction across the
  receive array.

From $(R,\theta)$ and the vessel's attitude and position, the sounding's position
and depth follow by trigonometry. Three consequences are immediate and are the
substance of the lesson:

- the conversion contains an assumed $c$, and $c$ varies by $5.9\,\%$ across the
  real ocean (Lesson 15-01-01, Section 5);
- the geometry degrades as $\theta$ grows, so a swath does not have one
  resolution;
- the depth that comes out is a fraction of the *depth*, so accuracy
  specifications are naturally written as percentages and hide their own
  depth dependence.

## 2. Swath geometry

A beam at the extreme angle $\theta_{\max}$ reaches the seafloor at horizontal
distance $z\tan\theta_{\max}$ from the nadir, for a flat seafloor at depth $z$.
Two symmetric sides give the **swath width**

$$W = 2 z \tan\theta_{\max} .$$

With $\theta_{\max} = 60^\circ$:

| depth $z$ (m) | swath width (m) | width/depth | outer-beam slant range (m) |
|---|---|---|---|
| 50 | 173 | 3.464 | 100 |
| 200 | 693 | 3.464 | 400 |
| 1000 | 3464 | 3.464 | 2000 |
| 2000 | 6928 | 3.464 | 4000 |
| 4000 | 13856 | 3.464 | 8000 |

The width-to-depth ratio is constant at $2\tan 60^\circ = 3.464$. **Coverage is a
property of the beam angle, not of the depth.** One consequence worth following
through: for a system with a fixed number of beams and fixed angular spacing, the
across-track *sounding spacing* on the seafloor grows linearly with depth, so
resolution falls linearly with depth. A deeper survey is a coarser survey with the
same instrument.

For a flat seafloor the outer-beam slant range is $z/\cos\theta_{\max} = 2z$ at
$60^\circ$: **exactly twice the depth.** That factor of two reappears in every
error term that scales with slant range.

## 3. Beam footprint

A real beam has an angular width $\Delta\theta$ across-track and $\Delta\phi$
along-track. At slant range $R = z/\cos\theta$,

- the across-track footprint is the arc $R\,\Delta\theta$ projected onto the
  seafloor, which divides by another $\cos\theta$:
  $$\ell_{\text{across}} = \frac{R\,\Delta\theta}{\cos\theta}
  = \frac{z\,\Delta\theta}{\cos^{2}\theta};$$
- the along-track footprint is $R\,\Delta\phi$, with no projection factor, because
  the along-track direction is not tilted relative to the seafloor.
  $$\ell_{\text{along}} = R\,\Delta\phi .$$

The $1/\cos^{2}\theta$ in the first expression is the single most important
geometric fact about swath sonar. With $z = 2000\ \mathrm{m}$ and
$\Delta\theta = 1^\circ = 0.017453\ \mathrm{rad}$:

| $\theta$ (deg) | slant range (m) | across-track footprint (m) | growth vs nadir |
|---|---|---|---|
| 0 | 2000 | 34.9 | 1.000 |
| 15 | 2071 | 37.4 | 1.072 |
| 30 | 2309 | 46.5 | 1.333 |
| 45 | 2828 | 69.8 | 2.000 |
| 55 | 3487 | 106.1 | 3.040 |
| 60 | 4000 | 139.6 | 4.000 |

**The outer beams resolve a patch of seafloor four times longer than the nadir
beams**, and the along-track footprint at the outer beam is
$R\,\Delta\phi = 4000 \times 0.017453 = 69.8\ \mathrm{m}$ — a factor of two, not
four, because there is no projection factor in that direction. A swath's
resolution is therefore *anisotropic* as well as variable: the footprint at
$60^\circ$ is $139.6\ \mathrm{m}$ across-track by $69.8\ \mathrm{m}$ along-track.

## 4. Sound-speed error is a scale error

The system computes a slant range from the measured two-way time using an assumed
sound speed:

$$R = \frac{c_{\text{assumed}}\,t}{2} .$$

If the true path-averaged speed is $c_{\text{true}}$, then

$$\frac{\delta R}{R} = \frac{c_{\text{assumed}} - c_{\text{true}}}{c_{\text{true}}}
\equiv \epsilon,$$

exactly; there is no approximation. Since the depth is proportional to the slant
range at fixed angle, $\delta z/z = \epsilon$ as well:

| $c$ error | depth error at 200 m | at 2000 m | at 4000 m |
|---|---|---|---|
| 0.1 % | 0.20 m | 2.00 m | 4.00 m |
| 0.5 % | 1.00 m | 10.00 m | 20.00 m |
| 1.0 % | 2.00 m | 20.00 m | 40.00 m |
| 2.0 % | 4.00 m | 40.00 m | 80.00 m |
| 5.0 % | 10.00 m | 100.00 m | 200.00 m |

Three points deserve emphasis.

- **A $1\,\%$ sound-speed error is $20\ \mathrm{m}$ of depth error at
  $2\ \mathrm{km}$.** That is larger than most survey specifications, and it is
  the reason sound-speed profiles are measured rather than assumed.
- **The error is a *scale* error.** It multiplies the bathymetry by a constant, so
  the result is a perfectly plausible seafloor that is uniformly too deep or too
  shallow. Nothing in the data looks wrong. Only an independent depth (a
  bar check, a cross-line tie, or a measured profile) can detect it.
- **Shallow water is insensitive to it.** The same $0.5\,\%$ error is $0.5\
  \mathrm{m}$ at $200\ \mathrm{m}$ and $20\ \mathrm{m}$ at $4000\ \mathrm{m}$.
  Sound-speed accuracy matters *with depth*.

## 5. Attitude, heave, and the outer-beam penalty

Roll mis-points the beams. At slant range $R$, an attitude error $\delta\theta$
displaces the sounding across-track by

$$\delta x \approx R\,\delta\theta .$$

With the outer beam at $R = 4000\ \mathrm{m}$ ($z = 2000\ \mathrm{m}$,
$\theta = 60^\circ$):

| roll error | cross-track shift (m) |
|---|---|
| 0.02° | 1.40 |
| 0.05° | 3.49 |
| 0.10° | 6.98 |
| 0.50° | 34.91 |
| 1.00° | 69.81 |

**A $0.1^\circ$ roll error shifts the outer beam by $7.0\ \mathrm{m}$, comparable
to the across-track footprint itself.** Attitude accuracy is not a secondary
concern; it competes directly with resolution.

The same arithmetic applies to pitch (along-track) and, more seriously, to
**heave**: a vertical motion of the vessel moves the whole swath vertically and is
*not distinguishable from real bathymetry*. Heave must be measured — by an
accelerometer, corrected by a GNSS-derived vertical — not inferred. And note that
roll and pitch errors grow with slant range, so their effect is concentrated at
the swath edges, whereas a sound-speed error is coherent across the whole swath.
That difference matters when the errors are later inverted for: they have
different spatial signatures.

## 6. Sounding density and grid resolution

With a vessel speed $v$, ping rate $f_p$ and beam spacing $\Delta\theta$, the
sounding spacing is

$$\text{along-track} = \frac{v}{f_p}, \qquad
\text{across-track} \approx z\,\Delta\theta .$$

For $v = 8.0\ \mathrm{kn} = 4.116\ \mathrm{m\,s^{-1}}$, $f_p = 10\ \mathrm{Hz}$,
$\Delta\theta = 0.3^\circ = 5.236\times10^{-3}\ \mathrm{rad}$:

| depth (m) | swath width (m) | soundings per m$^{2}$ at nadir | across-track spacing (m) |
|---|---|---|---|
| 100 | 346 | 4.641 | 0.52 |
| 500 | 1732 | 0.928 | 2.62 |
| 2000 | 6928 | 0.232 | 10.47 |
| 4000 | 13856 | 0.116 | 20.94 |

Two decisions follow, and both are judgement calls rather than measurements.

- **Grid cell size.** A defensible choice is the *nadir* across-track spacing
  ($10.5\ \mathrm{m}$ at $2000\ \mathrm{m}$ depth): finer would interpolate,
  coarser would discard data. A different defensible choice is the outer-beam
  footprint ($139.6\ \mathrm{m}$ at the same depth), which produces a smooth,
  conservative product. **The same soundings therefore yield bathymetric grids
  with different resolutions depending on the analyst's choice**, and the choice
  must be stated. The demonstration prints the nadir choice.
- **Along-track decimation.** The along-track spacing here ($0.41\ \mathrm{m}$) is
  25 times finer than the across-track spacing at $2000\ \mathrm{m}$. Storing all
  of it is wasteful; decimating to the across-track spacing is standard, and it
  discards 96 % of the soundings while changing nothing visible.

## 7. The depth-error budget

Combine the terms in quadrature. At $z = 2000\ \mathrm{m}$ with the demonstration's
chosen values:

| term | contribution (m) |
|---|---|
| sound speed, $0.5\,\%$ of depth | 10.000 |
| time measurement, $0.05\ \mathrm{ms}$ of travel time | 0.040 |
| roll, $0.05^\circ$ at $4000\ \mathrm{m}$ slant range | 3.491 |
| heave residuals, $0.10\ \mathrm{m}$ | 0.100 |
| beam-angle calibration, $0.02^\circ$ | 1.396 |
| **total (quadrature)** | **10.684** |

The total is $10.68\ \mathrm{m}$, i.e. $0.534\,\%$ of the depth. The dominant term
is the **acoustic** one, and it is a *scale* error proportional to depth; the
attitude terms scale with slant range and only reach $3.5\ \mathrm{m}$ at the
outer beam. The two classes therefore trade places with depth: a
$200\ \mathrm{m}$ survey has a $1\ \mathrm{m}$ sound-speed term and a
$3.5\ \mathrm{m}$ roll term (attitude-limited), while a $4000\ \mathrm{m}$ survey
has a $20\ \mathrm{m}$ sound-speed term and the same $3.5\ \mathrm{m}$ roll term
(sound-speed-limited). **"The" depth accuracy is therefore a function of depth,
and a single percentage is a summary, not a specification.**

## 8. Assumptions and regime of validity

1. **A flat seafloor.** Every formula uses $z = R\cos\theta$. On a slope the
   sounding is displaced and the depth error becomes a slope-dependent
   magnification, largest where the beam is most oblique to the slope.
2. **Straight-line ray paths.** Real rays refract in a layered ocean. The
   correction, called ray bending, is second-order in the sound-speed gradient and
   first-order in range; it is the reason a single "average" sound speed is not
   enough at long range, and profiles are applied in layers.
3. **A single assumed sound speed.** A real-time system applies a measured profile
   at the transducer and often a second estimate for the water column; the
   residual error is what Section 4 quantifies.
4. **No beam interference or side lobes.** Real systems have side-lobe returns
   from outside the steered beam, important on slopes and in shallow water.
5. **Known attitude at the instant of transmission.** Attitude is measured at a
   finite rate; interpolation between samples introduces an error that is largest
   in a seaway.
6. **No refraction by the sound-speed contrast at the seabed.** Trivial in
   practice, but worth noting: the seabed itself refracts and reflects.
7. **Soundings are independent.** Neighbouring soundings are correlated through the
   same beam footprint, so they are not independent measurements of the seafloor;
   averaging them reduces noise slower than $1/\sqrt{N}$.

## 9. Worked examples

### Example 1 — a swath in 300 m of water

$$W = 2(300)\tan 60^\circ = 600 \times 1.73205 = 1039\ \mathrm{m},$$

$$\ell_{\text{across}} \text{ at } 60^\circ = \frac{300 \times 0.017453}{\cos^{2}60^\circ}
= \frac{5.236}{0.25} = 20.94\ \mathrm{m},$$

$$\ell_{\text{along}} \text{ at } 60^\circ = \frac{300}{\cos 60^\circ}\times0.017453
= 600 \times 0.017453 = 10.47\ \mathrm{m}.$$

The footprint at the swath edge is $20.9\ \mathrm{m}$ across-track by
$10.5\ \mathrm{m}$ along-track. The nadir footprint would be
$300 \times 0.017453 = 5.24\ \mathrm{m}$.

### Example 2 — asking what sound-speed accuracy a specification demands

A survey in $1500\ \mathrm{m}$ of water is required to be accurate to
$\pm5\ \mathrm{m}$. Allowing the sound-speed term to consume half the budget
($2.5\ \mathrm{m}$):

$$\epsilon = \frac{2.5}{1500} = 1.67\times10^{-3} = 0.167\,\% .$$

Since $c \approx 1500\ \mathrm{m\,s^{-1}}$, that is
$\pm2.5\ \mathrm{m\,s^{-1}}$ on the path-averaged speed. Real deep-ocean sound
speeds vary by $90\ \mathrm{m\,s^{-1}}$ between the surface and $4\ \mathrm{km}$,
so this is a demanding but achievable requirement — and it is a requirement on
the *path average*, not on any single measurement of $c$.

### Example 3 — heave

A vessel in a swell of amplitude $1.5\ \mathrm{m}$ moves vertically by
$\pm1.5\ \mathrm{m}$. Without correction this appears directly as a bathymetric
error of $\pm1.5\ \mathrm{m}$. At $2000\ \mathrm{m}$ depth that is
$0.075\,\%$ — negligible against the $10\ \mathrm{m}$ sound-speed term — but at
$100\ \mathrm{m}$ depth it is $1.5\,\%$, larger than any acoustic term and
comparable to the whole swath's footprint. **Heave correction matters most exactly
where the swath is narrowest and the coverage most valuable.**

## 10. Python demonstration

`code/multibeam_bathymetry_demo.py` prints all the above with units:

1. swath width against depth, with the constant width-to-depth ratio;
2. the across-track and along-track footprints and the $1/\cos^{2}$ growth;
3. the depth error from a sound-speed error at three depths;
4. roll error against cross-track displacement at the outer beam;
5. sounding density and the grid-cell choice against depth;
6. a quadrature depth-error budget with the dominant term identified;
7. verification: the closed-form footprint against a direct difference of
   beam-edge ground ranges, and a unit check.

Run it with

```bash
cd 15-oceanography-marine/02-marine-geophysics-methods/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python multibeam_bathymetry_demo.py
```

Print-only, no network, fixed seed `np.random.default_rng(20261014)`, exit 0, in
under a second.

## 11. Exercises

Full sets with worked solutions are in
[`exercises/02-multibeam-bathymetry-exercises.md`](exercises/02-multibeam-bathymetry-exercises.md)
and
[`exercises/02-multibeam-bathymetry-solutions.md`](exercises/02-multibeam-bathymetry-solutions.md).

- ★ Compute the swath width and the outer-beam slant range for
  $z = 800\ \mathrm{m}$ and $\theta_{\max} = 65^\circ$.
- ★★ Derive $\ell_{\text{across}} = z\Delta\theta/\cos^{2}\theta$ and evaluate it
  at $\theta = 0$, $45^\circ$, $65^\circ$ for $z = 800\ \mathrm{m}$,
  $\Delta\theta = 1^\circ$.
- ★★ A survey must be accurate to $\pm3\ \mathrm{m}$ in $1200\ \mathrm{m}$ of
  water. What sound-speed accuracy does that require if the acoustic term gets
  half the budget?
- ★★★ Design a survey that would detect and quantify the scale error of
  Section 4 in a deep-water bathymetric grid, and state the independent reference
  the test requires.

## Mastery checkpoint

Without notes, and showing your arithmetic.

> A multibeam system with $\theta_{\max} = 60^\circ$, $\Delta\theta = 1^\circ$,
> $f_p = 8\ \mathrm{Hz}$ surveys at $5\ \mathrm{kn}$ in water $2500\ \mathrm{m}$
> deep. Use $1\ \mathrm{kn} = 0.514444\ \mathrm{m\,s^{-1}}$.
> **(a)** Compute the swath width, the outer-beam slant range and the
> across-track footprint at nadir and at the outer beam.
> **(b)** Compute the across-track soundings and the along-track ping spacing, and
> state which direction is oversampled and by how much.
> **(c)** The path-averaged sound speed is $1520\ \mathrm{m\,s^{-1}}$ but the
> system assumed $1500\ \mathrm{m\,s^{-1}}$. Compute the depth error, state its
> sign, and say whether it is detectable from the swath's own internal
> consistency.
> **(d)** A roll bias of $0.08^\circ$ is present. Compute the cross-track
> displacement of the outer beam and compare it with the outer-beam footprint.

A worked version of (a)–(d) is in the lesson-02
[solutions](exercises/02-multibeam-bathymetry-solutions.md).

## Common pitfalls

1. **Quoting one resolution for a swath.** The footprint varies by a factor 4
   between nadir and the outer beam, and it is anisotropic.
2. **Treating a sound-speed error as random noise.** It is a coherent *scale*
   error, invisible in the data and not reduced by averaging.
3. **Assuming attitude errors are small.** At $0.1^\circ$ roll the outer beam is
   displaced by more than the nadir footprint.
4. **Forgetting heave.** Vertical vessel motion is indistinguishable from
   bathymetry and must be measured.
5. **Gridding to the worst footprint, or to the best.** Both discards information;
   state and justify the choice.
6. **Averaging neighbouring soundings as if independent.** They share a footprint,
   so the noise reduction is slower than $1/\sqrt{N}$.
7. **Applying one sound speed over a long range.** Ray bending is second-order in
   the gradient but first-order in range and is not removed by averaging.

## Related modules

- [01 Marine Seismic Reflection: Airguns, Streamers, Processing](01-marine-seismic-reflection.md) —
  the same travel-time physics and the same $\lambda/4$ resolution logic.
- [03 Side-Scan Sonar and Seafloor Imaging](03-side-scan-sonar.md) —
  the same swath geometry used for backscatter instead of depth.
- [05 Marine Gravity and Magnetic Surveys](05-marine-gravity-magnetics.md) —
  the potential-field methods that see the seabed's shape from a distance.
- [Module 15-02 README](README.md) — how the methods in this module fit together.
- [Module 15-04 Seafloor Mapping and Habitat Characterisation](../04-seafloor-mapping-and-habitats/README.md) —
  what the bathymetry this lesson produces is used for.
- [17 Remote Sensing and GIS](../../17-remote-sensing-gis/README.md) —
  the gridding and terrain-analysis stage downstream of a bathymetric product.

## Self-assessment checklist

- [ ] I can derive and evaluate the swath width and its width-to-depth ratio.
- [ ] I can derive the $1/\cos^{2}\theta$ footprint law and locate its effect.
- [ ] I can convert a sound-speed error into a depth error and say why it is
      invisible.
- [ ] I can convert a roll, pitch or heave error into a displacement.
- [ ] I can compute a sounding density and justify a grid cell.
- [ ] I can build a depth-error budget and name the dominant term at two depths.
- [ ] I can distinguish a scale error from a geometry error.
