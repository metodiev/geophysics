---
id: 11-03-01
title: "Reflection Seismic in Exploration: From 2-D to 3-D"
level: graduate
prereqs: ["06-09-01", "06-09-02", "05-05-02", "11-01-02"]
tags: [exploration-geophysics, seismic-reflection, survey-design, resolution, acquisition]
---

# Reflection Seismic in Exploration: From 2-D to 3-D

**All models and data in this module are SYNTHETIC.** The acquisition
geometries, velocities, target depths and noise levels used here are chosen
teaching values, not measurements from any survey. No field, well, company or
basin is described.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the vertical resolution limit $\lambda/4$ from the interference of
   two reflections and **state** the assumption about wavelet bandwidth that it
   hides.
2. **Compute** the first Fresnel zone radius $\sqrt{\lambda z/2}$ and **explain**
   why migration, not processing effort, is what reduces it.
3. **Derive** the trace-density expression for 3-D fold from the
   source–receiver midpoint mapping, and **count** the discretisation
   correction on a synthetic acquisition grid.
4. **Predict** the stacking gain $\sqrt{N}$ for uncorrelated noise and
   **measure** it.
5. **Compute** the alias frequency $f_{\max} = v/(4\Delta x \sin\theta)$ for a
   dipping event and **choose** a bin size from it.
6. **Quantify** the 2-D side-swipe (apparent-depth) error and **decide** what
   a 2-D line can and cannot be used for.
7. **Design** a 3-D acquisition for a stated target, reporting resolution,
   fold and the assumptions behind both.

## Prerequisites

- [06-09-01 Acoustic Impedance, Reflection Coefficients and the Convolution Model](../../06-seismology/09-reflection-seismology/01-reflection-principle.md) —
  what a reflection is, derived.
- [06-09-02 Reflection Processing Flow](../../06-seismology/09-reflection-seismology/02-processing-flow.md) —
  deconvolution, NMO, stack and migration, which this lesson assumes rather
  than re-derives.
- [05-05-02 Array Geometry, Fold, Offsets and Spatial Sampling](../../05-core-geophysics/05-survey-design-and-acquisition/02-geometry-and-coverage.md) —
  the acquisition vocabulary.
- [11-01-02 Targeting Strategy and Method Selection](../01-exploration-workflow/02-targeting-and-strategy.md) —
  why a seismic survey is chosen at all rather than, say, gravity.

## 1. What a seismic survey delivers, and what it does not

An exploration seismic survey delivers a **grid of reflection amplitudes indexed
by two-way travel time**. It is not a picture of rock and it is not a picture of
hydrocarbons. In the play language of
[04-06-01 Source, Reservoir, Seal and Trap](../../04-earth-science-geology/06-petroleum-and-mineral-systems/01-petroleum-system.md),
seismic constrains the **trap geometry**, the **seal/reservoir contrast**, and —
through amplitudes and inversion — a **bulk average** of the reservoir
interval. It measures no fluid, no porosity and no permeability directly.

That leaves three questions that decide whether a target is visible at all, and
they are all answered before a line is shot:

1. **Vertical resolution**: how thick is the thinnest bed whose thickness and
   amplitude can be read separately? Controlled by bandwidth, not by effort.
2. **Horizontal resolution**: how large an area is summed into one trace?
   Controlled by the Fresnel zone during acquisition and by migration
   afterwards.
3. **Sampling**: how many times is each subsurface point measured, and how
   finely is the wavefield sampled in space? Controlled by the geometry.

The rest of this lesson makes those three quantitative, and shows what a 3-D
survey buys over a 2-D one.

## 2. Vertical resolution: the $\lambda/4$ limit

A reflection is a contrast in acoustic impedance $Z = \rho v$; for two
half-spaces, $R = (Z_2-Z_1)/(Z_2+Z_1)$
([06-09-01](../../06-seismology/09-reflection-seismology/01-reflection-principle.md)).
A thin bed is therefore two reflectors of opposite sign separated by the
two-way travel time

$$\Delta t = \frac{2h}{v},$$

where $h$ is the bed thickness. The measured trace is the convolution of the
two spikes with the source wavelet $w(t)$:

$$d(t) = R\left[w(t) - w(t-\Delta t)\right].$$

When $\Delta t$ is small compared with the wavelet's own duration, the two
terms interfere and $d$ is no longer two separable events. The classical rule is
that resolution stops at

$$h_{\lambda/4} = \frac{\lambda}{4} = \frac{v}{4f},$$

and it is worth being explicit about why: $\lambda/2$ in two-way time is the
separation at which the negative lobe of the first event begins to leave the
main lobe of the second. It is a rule of thumb calibrated on a symmetric
wavelet, and this lesson's demonstration measures both the coefficient and its
wavelet dependence.

*Numbers from the demonstration (chosen $v = 3.00\ \mathrm{km\,s^{-1}}$):*

| $f$ (Hz) | $\lambda$ (m) | $\lambda/4$ (m) | period (ms) |
|---|---|---|---|
| 15 | 200.0 | 50.0 | 67 |
| 20 | 150.0 | 37.5 | 50 |
| 30 | 100.0 | 25.0 | 33 |
| 40 | 75.0 | 18.8 | 25 |
| 60 | 50.0 | 12.5 | 17 |

Two lessons follow immediately. First, resolution is bought with **frequency**,
and frequency is lost to absorption with depth, so resolution is always a
function of depth even at constant rock. Second, a target 15 m thick needs
roughly 50 Hz at that velocity — a real acquisition constraint, and the reason
high-frequency sources and long offsets are specified per target rather than by
habit.

The measurement also shows that $\lambda/4$ is a *rule of thumb*, not a
physical constant. With a 30 Hz Ricker wavelet, the composite amplitude of a
wedged bed reaches its maximum at $19.5\ \mathrm{m}$, i.e.
$0.195\,v/f_0$, and the read-off thickness becomes accurate to 10% at
$16.95\ \mathrm{m}$ or $0.17\,v/f_0$. Both are *below* $\lambda/4 = 25\ \mathrm{m}$.
The coefficient is a property of the wavelet, which is
[11-03-02](02-seismic-stratigraphy.md)'s subject.

## 3. Horizontal resolution: the Fresnel zone

For a zero-offset reflection from a plane at depth $z$, the energy that arrives
within half a period of the specular arrival comes from a disc whose radius is
the **first Fresnel zone radius**

$$r_f = \sqrt{\frac{\lambda z}{2}}.$$

*Derivation sketch.* The path difference to a point at horizontal offset $x$ is
$\sqrt{z^2+x^2}-z \approx x^2/(2z)$; setting that equal to $\lambda/4$ (a
half-period of travel time in the two-way sense) gives $x^2 = \lambda z/2$.

*Numbers from the demonstration* ($f = 30\ \mathrm{Hz}$, $\lambda = 100\ \mathrm{m}$):

| depth (m) | two-way time (s) | Fresnel radius (m) | in wavelengths |
|---|---|---|---|
| 1000 | 0.667 | 223.6 | 2.2 |
| 2000 | 1.333 | 316.2 | 3.2 |
| 3000 | 2.000 | 387.3 | 3.9 |
| 4000 | 2.667 | 447.2 | 4.5 |

Two features are worth naming. The Fresnel radius grows only as $\sqrt{z}$, so
it is the *least* restrictive of the resolution limits. And it is an
acquisition-geometry quantity in the sense that it bounds what migration can
recover: pre-stack migration can, in principle, collapse the Fresnel zone to
something close to the resolution limit, but only if the wavefield is sampled
finely enough to record the angles involved. That is the link to §5.

## 4. 3-D fold from trace density

**Fold** is the average number of times a subsurface midpoint is measured. It
governs the signal-to-noise ratio of the stack. The clean derivation is a
density argument.

Let $\sigma_s$ be the source density (sources per km²) and $\sigma_r$ the
receiver density. A pair $(s,r)$ maps to a midpoint $m = (s+r)/2$ and an offset
$h = r-s$ with unit Jacobian:

$$\left|\frac{\partial(s,r)}{\partial(m,h)}\right| = 1 .$$

So the density of $(m,h)$ pairs is $\sigma_s\sigma_r$, and integrating over the
offset window $|h_x| \le h_x^{\max},\ |h_y| \le h_y^{\max}$ gives the **trace
density**:

$$\text{fold} = \sigma_s\,\sigma_r\,\Delta A_{\text{bin}}\,
(2h_x^{\max})(2h_y^{\max}).$$

Equivalently, in a form that survives discretisation:

$$\boxed{\ \text{fold} = \sigma_s\,T\,\Delta A_{\text{bin}}\ }, \qquad
T = \sigma_r\,(2h_x^{\max})(2h_y^{\max}),$$

where $T$ is the number of live traces each source contributes inside the offset
window.

*Worked example (the demonstration's small grid).* Sources every 100 m on lines
every 200 m give $\sigma_s = 50\ \mathrm{km^{-2}}$; receivers every 50 m on lines
every 200 m give $\sigma_r = 100\ \mathrm{km^{-2}}$; offsets are limited to
$\pm400\ \mathrm{m}$ in both directions; the bin is 25 m.

- continuum: $T = 100 \times 0.8 \times 0.8 = 64$,
  $\text{fold} = 50 \times 64 \times 0.000625 = 2.00$;
- discrete count: 17 receiver positions in the $x$ window and 5 lines in the
  $y$ window give $T = 85$, so $\text{fold} = 2.66$;
- **measured** by counting midpoints of the synthetic grid over a central
  $20\times20$ block: **2.76**.

The measured value agrees with the discrete count to 4% and exceeds the
continuum rule by 38% — because the offset window is only a few line spacings
wide, so counting whole lines (the "fencepost") is not a small correction. This
is a general warning: continuum design formulas are asymptotically right and
locally wrong.

*Realistic template (design numbers).* Receivers 25 m along line, lines every
300 m, 9 lines, offsets $|h_x| \le 3000$ m and $|h_y| \le 1200$ m give
$\sigma_r = 133.3\ \mathrm{km^{-2}}$ and $T = 1920$; sources every 50 m on lines
every 300 m give $\sigma_s = 66.7\ \mathrm{km^{-2}}$ and **fold 80**, or **40**
if the source lines are 600 m apart. Fold is a statement about sampling, and
halving the source lines halves it.

**Why fold matters.** For uncorrelated noise, stacking $N$ traces multiplies
the signal-to-noise ratio by $\sqrt{N}$ if amplitudes are preserved. The
demonstration measures this on 4000-sample noise realisations:

| fold | measured gain | $\sqrt{N}$ |
|---|---|---|
| 1 | 1.00× | 1.00× |
| 6 | 2.39× | 2.45× |
| 12 | 3.46× | 3.46× |
| 30 | 5.59× | 5.48× |
| 60 | 7.00× | 7.75× |
| 120 | 11.94× | 10.95× |

The scatter around $\sqrt{N}$ is the sampling noise of a finite realisation, not
a departure from theory. Note what the result does *not* say: fold improves
random noise only. Coherent noise — multiples, side-swipe, ground roll —
is not attenuated by $\sqrt{N}$ at all, which is why 3-D acquisition exists.

## 5. Spatial sampling and alias frequency

A dipping event has a two-way moveout $p = \mathrm{d}t/\mathrm{d}x$. At
frequency $f$ its spatial frequency (wavenumber) is $k = f p$, and the spatial
Nyquist wavenumber for a trace interval $\Delta x$ is $k_N = 1/(2\Delta x)$.
Aliasing is avoided while $k \le k_N$, i.e.

$$f_{\max} = \frac{1}{2\Delta x\,p}
= \frac{v}{4\Delta x \sin\theta},$$

where $\theta$ is the true dip and $p = 2\sin\theta/v$ for a two-way time
section.

*Numbers from the demonstration* ($v = 3.00\ \mathrm{km\,s^{-1}}$), $f_{\max}$ in Hz:

| $\Delta x$ (m) | dip 10° | dip 20° | dip 30° |
|---|---|---|---|
| 12.5 | 345.5 | 175.4 | 120.0 |
| 25.0 | 172.8 | 87.7 | 60.0 |
| 50.0 | 86.4 | 43.9 | 30.0 |
| 100.0 | 43.2 | 21.9 | 15.0 |

The steep dips alias first, and the 30 Hz signal is preserved at every trace
interval in the table — which is exactly why a survey designed for 30 Hz content
can still be shot on a 50 m grid and still fail on a steep flank after
migration has steepened the apparent dips.

## 6. Why 2-D is not a slice of 3-D

A 2-D line records only in-plane offsets. Energy arriving from a reflector at
horizontal distance $y$ out of the plane is recorded at the time it arrives, and
migration along the line cannot move it out of the plane. A point diffractor at
true depth $z$ therefore images at the **apparent depth**

$$z_{\text{app}} = \sqrt{z^2+y^2}.$$

*Numbers from the demonstration:*

| true depth (m) | off-line distance (m) | apparent depth (m) | error |
|---|---|---|---|
| 2000 | 250 | 2016 | +0.8% |
| 2000 | 500 | 2062 | +3.1% |
| 2000 | 1000 | 2236 | +11.8% |
| 2000 | 1500 | 2500 | +25.0% |
| 2500 | 1500 | 2915 | +16.6% |

Two kinds of damage follow. The first is a depth error, which is bounded and in
principle predictable. The second is worse: the apparent position *moves with
the line location*, so a 2-D grid of lines produces a set of events whose
positions are mutually inconsistent. Interpretation cannot fix this — only
acquisition can. This is the geophysical reason why a modern prospect is shot in
3-D: not better resolution, but a wavefield sampled in two horizontal directions
so that migration has somewhere to put the out-of-plane energy.

## 7. Worked design example

**Statement.** Target: a reservoir at 2.5 km depth with $v_{\text{rms}} = 3.0\
\mathrm{km\,s^{-1}}$; a 25 m thick reservoir; steepest dip 25°; a random-noise
fold target of 40; the deepest event of interest has a period of 0.05 s.

1. **Wavelength and vertical resolution.** At 30 Hz, $\lambda = 3.0/0.030 =
   100\ \mathrm{m}$ and $\lambda/4 = 25\ \mathrm{m}$. The reservoir is exactly at
   the resolution limit: its thickness will be *readable* only with a favourable
   wavelet, and its amplitude will be thickness-dependent. State this to the
   interpreter before acquisition, not after.
2. **Fresnel zone.** $r_f = \sqrt{100\times2500/2} = 353.6\ \mathrm{m}$. A
   channel 100 m wide cannot be mapped on a zero-offset stack; it will require
   migration with sampled offsets and probably attributes
   ([06-09-07](../../06-seismology/09-reflection-seismology/07-seismic-attributes.md)).
3. **Bin size from alias.** For 25° dip: $f_{\max} = 3.0/(4\Delta x \sin25°)$.
   Requiring $f_{\max} \ge 50\ \mathrm{Hz}$ gives $\Delta x \le 3.0/(4\times50\
   \times0.4226) = 35.5\ \mathrm{m}$. Choose 25 m: a half-offset bin of 12.5 m
   with 25 m group interval is standard and leaves margin.
4. **Fold.** With $\sigma_s = 66.7\ \mathrm{km^{-2}}$ (sources every 50 m on
   300 m lines) and $T = 1920$ (25 m group interval, 9 receiver lines, 300 m
   line spacing, $\pm3$ km inline and $\pm1.2$ km crossline offsets), the
   demonstration's expression gives $\text{fold} = 66.7\times1920\times0.000625 =
   80$. To reach the target of 40, source lines can be doubled to 600 m spacing.
5. **What the fold buys.** $\sqrt{40} = 6.3$ in signal-to-noise for random
   noise. If the target event is 1.5× the noise floor on a single trace, the
   stack should put it at about 9.5× — visible, and still not a fluid
   indicator.
6. **Check against the alternatives.** Gravity and magnetics constrain the
   structure and basement depth at a fraction of the cost
   ([07-03-02](../../07-gravity-geodesy/03-gravity-anomalies-and-modelling/02-simple-body-formulas.md))
   and should be acquired first: if the trap is defined by a basement
   high, potential fields may answer the screening question without seismic. The
   seismic survey then buys the seal, the reservoir and the amplitude
   information that the potential fields cannot supply.

## 8. Assumptions and regime of validity

1. **Constant velocity for the resolution estimates.** $\lambda = v/f$ and
   $r_f = \sqrt{\lambda z/2}$ assume a single velocity. In a layered or
   strongly compacting earth, use the local interval velocity at the target,
   and expect the lateral variation to matter more than the vertical one.
2. **$\lambda/4$ assumes a broad-band, symmetric wavelet.** The demonstration
   measures $0.195\,v/f_0$ for the tuning maximum of a Ricker wavelet, so the
   rule is a scaling, not a constant. Quote the wavelet when quoting the
   resolution.
3. **$\sqrt{N}$ assumes uncorrelated, zero-mean noise and preserved
   amplitudes.** True-amplitude processing
   ([05-06-04](../../05-core-geophysics/06-data-processing-principles/04-gain-and-amplitude.md))
   is a prerequisite, and coherent noise violates the assumption outright.
4. **Fold is a midpoint-density statement.** It says nothing about the
   *distribution* of offsets in a bin: a bin with ±3 km offsets and one with
   ±300 m can have the same fold and completely different value for velocity
   analysis and AVO.
5. **Fresnel zone assumes a specular reflection from a plane.** For a
   diffractor or a rough surface, the relevant scale is the resolution of the
   migration, not the Fresnel radius.
6. **The alias formula assumes a linear event.** Curved events alias at
   different frequencies across the section; the formula is a sufficient
   condition at the steepest point.
7. **2-D side-swipe assumes an isolated diffractor.** Continuous out-of-plane
   structure produces a superposition that no single number describes.

## 9. Units and dimensional consistency

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| wavelength | $\lambda$ | m | $v/f$ = (m/s)/Hz |
| Fresnel radius | $r_f$ | m | $\sqrt{\mathrm{m}\cdot\mathrm{m}}$ |
| source density | $\sigma_s$ | km⁻² | per unit area |
| live traces per source | $T$ | 1 | dimensionless count |
| bin area | $\Delta A$ | km² | |
| fold | | 1 | km⁻² × 1 × km² |
| alias frequency | $f_{\max}$ | Hz | (m/s)/(m) |

The only combination that can produce a fold is a density times an area: if your
fold comes out with units of km² or s⁻¹, an area or a count has been misplaced.
Likewise the alias formula must return Hz; $v/(4\Delta x \sin\theta)$ has units
(m/s)/m = s⁻¹.

## 10. Python demonstration

`code/seismic_in_exploration_demo.py` prints, with units and labels:

1. the resolution table ($\lambda$, $\lambda/4$, period) at five frequencies;
2. the Fresnel radius at four depths;
3. the fold: continuum rule, discrete count and the value **measured** by
   counting midpoints of a synthetic acquisition grid;
4. the measured stacking gain against $\sqrt{N}$;
5. the alias-frequency table;
6. the 2-D apparent-depth (side-swipe) error table.

It is print-only, uses `np.random.default_rng(20261014)` and exits 0. Every
number quoted in this lesson is a number it prints.

## 11. Exercises

Full sets with worked solutions:

- [`exercises/01-seismic-in-exploration-exercises.md`](exercises/01-seismic-in-exploration-exercises.md)
- [`exercises/01-seismic-in-exploration-solutions.md`](exercises/01-seismic-in-exploration-solutions.md)

## Mastery checkpoint

Without notes:

> A 30 Hz Ricker wavelet, a rock velocity of $3.0\ \mathrm{km\,s^{-1}}$, a target
> at 2.0 km depth and a source grid of 50 m shots on 300 m lines with 25 m
> receivers on nine 300 m receiver lines, offsets limited to $\pm3$ km inline and
> $\pm1.2$ km crossline, bin $25\times25$ m. **(a)** Compute $\lambda$,
> $\lambda/4$ and the Fresnel radius at the target. **(b)** Compute the fold and
> the random-noise gain. **(c)** State the largest dip that is unaliased at
> 40 Hz. **(d)** A 600 m wide, 20 m thick channel is the target: state which of
> resolution, Fresnel zone and fold is the binding limit, and why.

## Common pitfalls

1. **Quoting a resolution without a velocity and a wavelet.** $\lambda/4$ is a
   scaling: it needs $v$ and $f$, and its coefficient is wavelet-dependent.
2. **Expecting fold to fix coherent noise.** Fold buys $\sqrt{N}$ against
   random noise and nothing against multiples or side-swipe.
3. **Confusing fold with offset distribution.** Two bins with the same fold can
   differ by an order of magnitude in maximum offset.
4. **Using a 2-D line as if it were a slice of 3-D.** The apparent depth error
   is $z(\sqrt{1+(y/z)^2}-1)$ and it moves with the line position.
5. **Designing bins from habit rather than from the alias relation.** The
   steepest dip of interest, not the shallowest, sets $\Delta x$.
6. **Treating the continuum fold rule as exact.** On grids where the offset
   window spans only a few line spacings, the fencepost term is tens of per
   cent.

## Related modules

- [06-09 Reflection Seismology](../../06-seismology/09-reflection-seismology/README.md) —
  the theory this lesson applies: reflection coefficients, processing,
  velocities, migration, AVO, multiples, attributes.
- [05-05 Survey Design and Acquisition](../../05-core-geophysics/05-survey-design-and-acquisition/README.md) —
  the general design principles and spatial sampling theory.
- [04-06 Petroleum, Mineral and Geothermal Systems](../../04-earth-science-geology/06-petroleum-and-mineral-systems/README.md) —
  the play elements that the seismic data are used to constrain.
- [11-03-02 Seismic Stratigraphy and Sequence Interpretation](02-seismic-stratigraphy.md) —
  what the interpreter does with the volume this lesson designs.
- [11-02 Mineral Exploration Geophysics](../02-mineral-exploration/README.md) —
  the same design logic applied to hard-rock targets.

## Further reading

- Telford, W. M., Geldart, L. P., & Sheriff, R. E. (1990). *Applied
  Geophysics* (2nd ed.). Cambridge University Press. Level: textbook. The
  seismic field-methods and resolution chapters.
- Sheriff, R. E., & Geldart, L. P. (1995). *Exploration Seismology* (2nd ed.).
  Cambridge University Press. Level: textbook. Acquisition geometry, fold and
  resolution, with the classical figures.
- Yilmaz, Ö. (2001). *Seismic Data Analysis*. Society of Exploration
  Geophysicists. Level: reference. The processing and migration reference used
  throughout folders 06 and 11.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.
