---
id: 07-03-06
title: "Microgravity for Cavities, Tunnels and Archaeology"
level: advanced
prereqs: ["07-03-01", "07-02-02"]
tags: [gravity, geodesy, microgravity, cavities, archaeology, engineering]
---

# Microgravity for Cavities, Tunnels and Archaeology

All models and data in this module are SYNTHETIC. The void sizes, depths, density
contrasts, instrument resolution and noise levels used below are chosen teaching
values; no real site, instrument or survey is referenced.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the anomaly of a spherical void and of a long tunnel, in microgal,
   and **state** which one a given target resembles.
2. **Derive** the detectability limit — the depth at which a void's signal equals
   a stated instrument resolution — and **show** how it scales with radius.
3. **Apply** the half-width depth rules at metre scale, and **quantify** how
   station spacing limits them.
4. **Remove** a regional trend by least squares using the flanks of the profile,
   and **explain** why the flanks and not the whole line.
5. **Distinguish** a density contrast from a void: air-filled versus water-filled.
6. **Estimate** the depth uncertainty from the noise, and **state** the
   assumptions about geology, topography and instrument drift.
7. **Decide** whether a survey can answer a given engineering question before it
   is acquired.

## Prerequisites

- [01 Interpreting Anomalies: Geometry, Depth and Amplitude Rules](01-anomaly-interpretation.md) —
  the half-width rules used at engineering scale.
- [07-02-02 Relative Gravimeters: Springs, LaCoste-Romberg, Scintrex](../02-gravity-instruments-and-surveys/02-relative-gravimeters.md) —
  what a relative gravimeter measures and the size of its drift and noise.

## 1. The scale of the problem

Engineering microgravity looks for voids: karst cavities, mine workings, tunnels,
crypts, cellars, unmarked graves. The targets are metres across and metres deep,
and the signals are tens of microgal — a millionth of the Earth's field. Two
consequences follow immediately. First, the *geological* noise (variable soil
thickness, topography, buried walls, filled ground) is usually larger than the
target signal, so the survey design and the residual analysis matter more than
the instrument. Second, the anomaly is small enough that a relative gravimeter's
drift, the tides, and the local elevation of the station all matter.

The unit of the trade is the **microgal**:

$$1\ \mu\mathrm{Gal} = 10^{-8}\ \mathrm{m\,s^{-2}} = 10^{-3}\ \mathrm{mGal}.$$

## 2. The two model shapes

### 2.1 A cavity as a sphere

A void of radius $R$ at depth $z$ (to the centre) has a density contrast
$\Delta\rho = \rho_{\text{void}} - \rho_{\text{rock}}$, which is negative for an
air-filled cavity in rock:

$$\Delta\rho \approx -2000\ \mathrm{kg\,m^{-3}}\ \text{(air)},\qquad
\Delta\rho \approx -1000\ \mathrm{kg\,m^{-3}}\ \text{(water-filled)}.$$

Its anomaly is that of a sphere:

$$g_z(0) = \frac{G M}{z^{2}},\qquad M = \tfrac{4}{3}\pi R^{3}\Delta\rho .$$

The demonstration prints, for $\Delta\rho = -2000\ \mathrm{kg\,m^{-3}}$:

| $R$ (m) | $z$ (m) | peak anomaly ($\mu$Gal) |
|---|---|---|
| 1 | 2 | 13.98 |
| 1 | 5 | 2.24 |
| 2 | 5 | 17.89 |
| 4 | 2 | 894.63 |
| 4 | 10 | 35.79 |

The $R^{3}$ scaling is brutal: doubling the radius multiplies the signal by
eight, so a survey designed for a $2\ \mathrm{m}$ void sees a $4\ \mathrm{m}$ one
far beyond its nominal depth range.

### 2.2 A tunnel as a horizontal cylinder

A tunnel long compared with its depth is a 2-D body:

$$g_z(0) = \frac{2G\lambda}{z}, \qquad \lambda = \pi R^{2}\Delta\rho .$$

The demonstration measures the half-width of this profile numerically at
$0.25\ \mathrm{m}$ spacing and recovers the depth exactly for
$z = 3, 5, 10, 20\ \mathrm{m}$: the half-width **is** the depth to the axis. The
peak values are $111.83$, $67.10$, $33.55$ and $16.77\ \mu$Gal for
$R = 2\ \mathrm{m}$, $\Delta\rho = -2000\ \mathrm{kg\,m^{-3}}$.

### 2.3 Detectability

Setting the peak equal to a stated instrument resolution
$\Delta g_{\text{res}}$ gives the maximum depth at which a spherical void of
radius $R$ is detectable *in principle*:

$$z_{\max} = \sqrt{\frac{G\,(4/3)\pi R^{3}\left|\Delta\rho\right|}
{\Delta g_{\text{res}}}}.$$

With $\Delta g_{\text{res}} = 5\ \mu\mathrm{Gal}$ (a SYNTHETIC teaching value,
not a manufacturer's specification):

| $R$ (m) | $z_{\max}$ (m) |
|---|---|
| 0.5 | 1.2 |
| 1.0 | 3.3 |
| 2.0 | 9.5 |
| 5.0 | 37.4 |

Because $z_{\max} \propto R^{3/2}$, tripling the radius extends the reach by a
factor $5.2$, not $3$. **And instrument resolution is not the limit**: detection
requires the anomaly to exceed the *geological* noise, which is often several
times larger. Every practical detectability statement should carry the noise
level it assumed.

## 3. Worked example: a survey line with a regional trend

*A $2\ \mathrm{m}$ radius void at $3\ \mathrm{m}$ depth under a line of stations
$2\ \mathrm{m}$ apart, with a linear regional trend of
$2.00\ \mu\mathrm{Gal} + 0.0500\ \mu\mathrm{Gal\,m^{-1}}\cdot x$ and
$1.5\ \mu\mathrm{Gal}$ rms noise.*

1. **True anomaly.** From §2.1 the peak is
   $g = GM/z^{2} = (6.67430\times10^{-11})(4/3)\pi(8)(2000)/9
   = 4.97\times10^{-7}\ \mathrm{m\,s^{-2}} = 49.70\ \mu$Gal.
2. **Fit the regional on the flanks only** ($|x| \ge 20\ \mathrm{m}$), where the
   anomaly has died away. The demonstration obtains
   $2.110\ \mu\mathrm{Gal} + 0.0419\ \mu\mathrm{Gal\,m^{-1}}\,x$ against the true
   $2.000$ and $0.0500$ — close, and biased by the $1.5\ \mu$Gal noise.
3. **Subtract and measure.** The residual peak is $48.03\ \mu$Gal at $x = 0$,
   and the flank rms is $1.56\ \mu$Gal. The true peak is recovered to $3\%$.
4. **Convert to depth.** The residual half-width is $2.73\ \mathrm{m}$, so
   $z = 2.73/0.766421 = 3.56\ \mathrm{m}$ against a true $3.00\ \mathrm{m}$ — a
   $+19\%$ error caused by the $2\ \mathrm{m}$ station spacing, not by the noise.
   The half-width rule is only as sharp as the sampling it is measured from.
5. **Fitting the regional over the whole line** would have absorbed part of the
   anomaly and biased the depth shallow; the flanks are used precisely to avoid
   that.

## 4. Depth uncertainty from noise

Repeating the profile fit 300 times with fresh noise, with the regional
estimated on the flanks as above:

| noise rms ($\mu$Gal) | mean inferred depth (m) | scatter (m) |
|---|---|---|
| 0.0 | 3.16 | 0.00 |
| 0.5 | 3.15 | 0.07 |
| 1.0 | 3.15 | 0.15 |
| 2.0 | 3.12 | 0.31 |

The estimator is essentially unbiased (the $3.16\ \mathrm{m}$ offset at zero
noise is the sampling bias of §3, not a bias of the noise) and the scatter grows
roughly linearly with the noise. **Noise and anomaly size are interchangeable in
the error budget**: a target twice as large at the same depth is worth a factor
two in depth precision, and so is halving the noise.

## 5. What gravity can and cannot tell you

- **It measures a density contrast, never a void.** Filling the cavity with
  water halves the contrast ($-1000$ instead of $-2000\ \mathrm{kg\,m^{-3}}$) and
  therefore halves the anomaly: the demonstration prints a ratio of $0.500$ for
  both test cases. A water-filled cavity at $5\ \mathrm{m}$ is indistinguishable
  from an air-filled one at a larger depth.
- **It cannot separate size from depth** on the basis of amplitude alone; only
  the profile width adds that (see
  [01](01-anomaly-interpretation.md)).
- **It cannot see through a disturbed surface layer.** Made ground, a concrete
  slab or a variable soil cover adds a signal of the same order as the target.
- **It cannot locate a target horizontally better than the station spacing
  allows**, and the derivative method used for edges is a noise amplifier.

## 6. A field procedure that makes the numbers above achievable

The models in §1–§4 assume the anomaly is isolated. Real surveys have to earn
that. The following procedure is the minimum consistent with the noise levels
quoted in §4.

| step | requirement | why it matters at this scale |
|---|---|---|
| station positioning | $\le0.5\ \mathrm{m}$ horizontal, levelled to $\le5\ \mathrm{mm}$ | the free-air gradient $2g/R \approx 0.308\ \mathrm{mGal\,m^{-1}} = 0.031\ \mu\mathrm{Gal\,cm^{-1}}$ acts on every height error |
| gravity reading | repeat to $\le1\ \mu$Gal at each station | the target may be $10$–$50\ \mu$Gal |
| base station | re-occupied every $1$–$2\ \mathrm{h}$ and at closure | separates instrument drift from signal |
| tide | computed and removed | the solid-Earth tide is an order of magnitude larger than the target signal ([07-06-02](../06-earth-tides-and-rotation/02-tidal-corrections.md)) |
| terrain | corrected within a stated radius (e.g. $30\ \mathrm{m}$) | walls, steps and slabs are the same size as the target |
| datum | a repeat loop of $\ge10\%$ of stations | the drift model is tested, not assumed |
| regional | fitted on the flanks outside the target's footprint | the demonstration's tilt was $4\ \mu$Gal across the line |

With this protocol the residual noise level of the demonstration's synthetic line
($1.5\ \mu$Gal) is realistic, and the depth uncertainty quoted in §4 is
achievable. Without it, an anomaly of tens of microgal is indistinguishable from
the day's drift and the site's topography, and the survey answers a different
question from the one asked.

## 7. Assumptions and regime of validity

1. **Known density contrast.** The value used fixes the interpretation; report it
   as an assumption with a stated range.
2. **Compact, isolated target.** Overlapping voids and a target adjacent to a
   wall or a slope need forward modelling, not rules of thumb.
3. **Flat ground and no topographic relief**, or a terrain correction applied.
   At metre scale a $10\ \mathrm{cm}$ elevation error contributes
   $\approx 0.2\ \mu$Gal — small, but a sloping site accumulates.
4. **Tides, drift and instrument tilt removed.** The Earth tide is of order
   $100$–$200\ \mu$Gal — an order of magnitude larger than the target; it must be
   modelled and removed ([07-06-02 Tidal Corrections in Precise Measurements](../06-earth-tides-and-rotation/02-tidal-corrections.md)).
5. **Stable datum.** Relative gravimeters drift, so a repeat station and a
   closure protocol are mandatory
   ([07-02-03 Survey Procedures: Loops, Drift, Repeatability and Ties](../02-gravity-instruments-and-surveys/03-survey-procedures.md)).
6. **2-D interpretation only for tunnels long compared with their depth**, the
   condition demonstrated in
   [07-03-03](03-forward-modelling-2d3d.md).

## 8. Physical interpretation

- The signals are tiny because $G$ is tiny and the masses are small: a
  $2\ \mathrm{m}$ air-filled sphere displaces only about $6.7\times10^{4}\ \mathrm{kg}$
  of rock, a mass comparable to a small building. The survey is trying to weigh a
  house from the surface.
- The inverse-cube dependence of the kernel on distance means measurement
  *height* is as important as station position. The free-air gradient is
  $\mathrm{d}g/\mathrm{d}h = 2g/R \approx 0.308\ \mathrm{mGal\,m^{-1}}
  = 0.031\ \mu\mathrm{Gal\,cm^{-1}}$, so a $5\ \mathrm{cm}$ error in sensor height
  moves the anomaly by $0.15\ \mu$Gal and a $50\ \mathrm{cm}$ error by
  $1.5\ \mu$Gal — comparable with the target itself. That is why microgravity
  stations are levelled to millimetres.
- Because the anomaly's shape encodes depth and its amplitude encodes mass, the
  product of the two surveys (a line profile with good flanks and a repeat of a
  fixed base station) is what actually constrains a target.

## 9. Python demonstration

`code/microgravity_applications_demo.py` prints:

1. the cavity amplitude table against radius and depth;
2. the detectability table against a stated $5\ \mu$Gal resolution;
3. the tunnel profile with numerically measured half-widths;
4. the air-versus-water contrast table;
5. the regional-removal example, with the fitted regional, the residual peak and
   the recovered depth;
6. the depth-scatter study over 300 noise realisations.

Every number in this lesson is from that output; the script is print-only and
exits 0.

## 10. Exercises

See
[`exercises/06-microgravity-applications-exercises.md`](./exercises/06-microgravity-applications-exercises.md)
and
[`exercises/06-microgravity-applications-solutions.md`](./exercises/06-microgravity-applications-solutions.md).

- **★** Convert $25\ \mu$Gal to $\mathrm{m\,s^{-2}}$ and to mGal.
- **★** Compute the anomaly of a $1.5\ \mathrm{m}$ radius air-filled cavity at
  $4\ \mathrm{m}$ depth.
- **★★** A survey must detect a $1\ \mathrm{m}$ radius cavity under $4\ \mathrm{m}$
  of rock with $1\ \mu$Gal noise. Is it possible, and what contrast does it
  require?
- **★★** Show that the tunnel half-width equals the depth to the axis by
  differentiating the profile.
- **★★★** Design a survey that distinguishes a water-filled cavity at
  $3\ \mathrm{m}$ from an air-filled one at $3\sqrt{2}\ \mathrm{m}$, specifying
  the station spacing, the repeat protocol and the noise level you would need.

## Mastery checkpoint

Without notes:

> A microgravity line runs over a suspected tunnel. Residual peak
> $30\ \mu$Gal, half-width $6\ \mathrm{m}$, station spacing $2\ \mathrm{m}$,
> residual noise $1.5\ \mu$Gal.

**(a)** Compute the depth under the cylinder rule.
**(b)** Compute the line mass per metre of tunnel and the radius, assuming
$\Delta\rho = -2000\ \mathrm{kg\,m^{-3}}$.
**(c)** Give the depth uncertainty implied by the noise table, interpolating.
**(d)** State two reasons the true tunnel may be deeper than your answer, and one
measurement that would settle it.

## Common pitfalls

1. **Confusing microgal with mGal.** A factor of a thousand.
2. **Ignoring the Earth tide.** It is larger than the target signal.
3. **Reading a raw anomaly without removing the regional.** The demonstration's
   line has a $4\ \mu$Gal regional across it, comparable to a small target.
4. **Assuming the void is air-filled.** Water halves the anomaly; fill is the
   dominant ambiguity.
5. **Quoting a depth to the nearest centimetre.** Station spacing sets the limit,
   and here it produced $+19\%$.
6. **Forgetting elevation and terrain.** Free-air and Bouguer terms dwarf the
   target if station heights are wrong.

## 11. Applications

- **Engineering site investigation.** Void detection before construction; the
  same analysis applies to mine shafts, culverts and cavities.
- **Archaeology.** Buried walls, ditches, crypts and graves are density contrasts
  of a few hundred $\mathrm{kg\,m^{-3}}$; the same rules apply with smaller
  contrasts.
- **Glaciology and hydrology.** Cavities and conduits in karst aquifers, at metres
  to tens of metres — the same physics at a larger scale.
- **Quality control.** Repeat microgravity is used to monitor compaction, ground
  subsidence and storage integrity.

## Related modules

- [01 Interpreting Anomalies: Geometry, Depth and Amplitude Rules](01-anomaly-interpretation.md).
- [02 Analytical Formulas for Sphere, Cylinder, Sheet and Dyke](02-simple-body-formulas.md) —
  the closed forms used here.
- [04 Gravity Inversion and Its Severe Non-Uniqueness](04-inversion-gravity.md) —
  why a single anomaly cannot fix both size and depth.
- [07-02-04 Practical Correction Workflow and Processing Sequence](../02-gravity-instruments-and-surveys/04-corrections-workflow.md) —
  the corrections that make a microgal measurement meaningful.
- [07-06-02 Tidal Corrections in Precise Measurements](../06-earth-tides-and-rotation/02-tidal-corrections.md).

## 12. Self-assessment checklist

- [ ] I can compute a cavity anomaly in $\mu$Gal from radius and depth.
- [ ] I can derive and use the detectability limit and its $R^{3/2}$ scaling.
- [ ] I can apply both half-width rules at metre scale.
- [ ] I can remove a regional using the flanks and say why.
- [ ] I can convert noise to a depth uncertainty.
- [ ] I can list the corrections that must precede interpretation.
