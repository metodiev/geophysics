---
id: 05-01-02
title: "Taxonomy of Methods: Active/Passive, Source/Receiver Geometry"
level: intermediate
prereqs: ["05-01-01"]
tags: [method-taxonomy, acquisition, active-passive, survey-geometry]
---

# Taxonomy of Methods: Active/Passive, Source/Receiver Geometry

## Learning objectives

1. **Classify** any geophysical method by four independent axes: energy source,
   field type, measurement domain, and target property.
2. **Explain** why the active/passive distinction is not the same as the
   natural/controlled-source distinction.
3. **Describe** the four canonical source–receiver geometries and the
   resolution each delivers.
4. **Derive** the relationship between acquisition geometry and the spatial
   wavelengths of the earth structure that are recoverable.
5. **Choose** a method family from a stated target and contrast.

## Prerequisites

- [05-01-01 The Central Idea](./01-physical-property-contrast.md) — contrasts
  and detectability.

## 1. Intuition: four questions, not one

Survey methods are usually taught as a list, which hides their structure. Ask
four questions and the list sorts itself:

1. **Where does the energy come from?** Natural (the Earth's own fields and
   seismic sources) or controlled (a hammer, a vibrator, a transmitter, a
   laser).
2. **What is the field?** Potential (gravity, magnetics: governed by elliptic
   equations, smooth, no focusing) or wave/diffusive (seismic, GPR, EM:
   governed by hyperbolic or parabolic equations, with phase and travel time).
3. **Where is the measurement?** Surface, airborne, borehole, marine, or
   satellite — this sets the accessible geometry.
4. **What property is targeted?** Density, magnetisation, conductivity,
   permittivity, elastic moduli, temperature.

Only the fourth question determines what you are looking for. The first three
determine what you *can* resolve.

## 2. Precise definitions

**Active method.** A method in which the operator introduces energy of known
character (position, time, amplitude, spectrum) and observes its interaction
with the subsurface. Examples: reflection and refraction seismics, GPR, DC
resistivity, controlled-source EM, induced polarisation.

**Passive method.** A method that observes a field whose source is not
controlled. Examples: gravity, magnetics, magnetotellurics, microseismic
monitoring, self-potential.

**Source–receiver geometry.** The arrangement of sources and receivers; the
single most important design choice after the method itself.

| Geometry | Source | Receiver | What it measures | Typical resolution |
|---|---|---|---|---|
| Common-offset profiling | fixed source, moved with receivers | towed/rolled | lateral variation on one surface | lateral only |
| Common-midpoint (CMP) sounding | multiple offsets | multiple offsets | vertical variation | depth-dependent |
| Wide-aperture / refraction | large offsets | linear array | velocity structure | smooth, large-scale |
| Tomographic (cross-hole, ERT) | many positions | many positions | full 2-D/3-D distribution | best, most expensive |

**Dimension of the model.** 1-D (layered), 2-D (a profile), 2.5-D (2-D with
3-D sources), 3-D. The model dimension, not the method, usually sets the cost.

## 3. Derivation: geometry fixes the recoverable wavelengths

Consider a surface line of receivers spaced $\Delta x$ apart. A field pattern of
spatial wavelength $\lambda_x$ is sampled without ambiguity only if $\Delta x <
\lambda_x/2$ (Nyquist). Therefore the *shortest* structure a survey can resolve
laterally is $\lambda_\text{min} = 2\Delta x$.

The *longest* structure is set by the aperture $L$ (the total spread of
sources and receivers): roughly $\lambda_\text{max} \approx L$. A survey with
$L = 1000$ m and $\Delta x = 10$ m therefore samples spatial wavelengths from
20 m to about 1000 m — a factor of 50 in wavelength, or 1.7 decades. This ratio
is the survey's *bandwidth*, and it is fixed **before** any processing, because
processing cannot create wavenumbers that were never sampled.

For an active source, the temporal bandwidth $B$ and the target velocity $v$
give a vertical resolution limit (the Rayleigh quarter-wavelength criterion)

$$\Delta z_\text{res} \approx \frac{v}{4B}.$$

Dimensional check: $[\mathrm{m\,s^{-1}}]/[\mathrm{s^{-1}}] = \mathrm{m}$. A
source with $B = 40$ Hz in material at $v = 2000$ m/s gives
$\Delta z_\text{res} = 2000/(4\cdot 40) = 12.5$ m.

This is the essential asymmetry: **active methods earn resolution by spending
bandwidth; potential-field methods have no bandwidth to spend**, because their
fields are solutions of Laplace's equation and are therefore smooth away from
sources.

## 4. Units and dimensional analysis

| Quantity | Symbol | SI unit | Typical field expression |
|---|---|---|---|
| Receiver spacing | $\Delta x$ | m | 5–50 m in shallow surveys |
| Aperture | $L$ | m | 10²–10⁴ m |
| Temporal bandwidth | $B$ | Hz (s⁻¹) | 10–200 Hz for crustal seismics |
| Dominant frequency | $f_0$ | Hz | 1–100 Hz |
| Resolution | $\Delta z$ | m | from $v/(4B)$ |
| Maximum unambiguous wavenumber | $k_N$ | rad m⁻¹ | $\pi/\Delta x$ |

Note that $f_0$ and $B$ are different numbers: a source can have a high
dominant frequency and a narrow band. Resolution depends on the *band*, not the
peak.

## 5. Assumptions

1. **Uniform receiver spacing along a line.** Irregular spacing makes the
   Nyquist argument local, not global.
2. **Single-scattering / ray theory** for the resolution formulas. Full-wave
   effects, and especially migration, can beat the quarter-wavelength estimate
   laterally, but not by orders of magnitude.
3. **The target contrast is strong enough to be measured within the bandwidth.**
   Resolution is not detectability: a thin bed can be *located* far more
   precisely than $v/(4B)$ if it is strong, and a thick weak one not at all.
4. **No aliasing in the source array.** Source spacing must also obey Nyquist
   during processing that treats sources as a wavefield (e.g. migration).

## 6. Worked examples

**6.1 Sampling design.** A shallow target at 30 m depth needs a lateral
resolution of 5 m. With a fixed-offset GPR profile, $\Delta x < 2.5$ m is
required. Over a 500 m line that is at least 200 traces.

**6.2 Trade-off between the two ends of the band.** Doubling the aperture $L$
extends the longest recoverable wavelength but leaves the shortest unchanged,
so it improves the *imaging of broad structure* only. Halving $\Delta x$
sharpens the image but does nothing for regional trends. A survey that is short
and dense, or long and sparse, is therefore good at one thing and useless at
the other.

**6.3 Active versus passive resolution.** A passive seismic array of aperture
$L$ has resolution set by $L$ alone; it cannot buy bandwidth because the
source spectrum is not under control. This is why microseismic locations are
an order of magnitude coarser than reflection images, and why the comparison
"seismic is high resolution" is method-specific, not universal.

## 7. Python demonstration

The module demonstration `code/resolution_depth_demo.py` quantifies the
difference between potential-field and wave methods. It measures the
half-width of a point-mass anomaly as a function of depth and reports the
log–log slope; the measured value is:

```
   depth(m)   half-width(m)   hw/depth
        100         153.200    1.53200
       1600        2451.200    1.53200
measured log-log slope d(log hw)/d(log depth) = 1.000000
closed form: g(x)/g(0) = 1/2  =>  hw = 1.532842 * depth
```

The width is *exactly* proportional to depth, so resolution degrades linearly —
you cannot fix it with a better sensor, only with a shallower target. Compare
this with a wave method, where a broader band genuinely improves resolution.
Section 3 gives the closed form $2\sqrt{2^{2/3}-1} = 1.532842$; the measured
$1.532$ differs by $5.5\times10^{-4}$ because of the finite sampling grid, and
that residual is exactly the kind of discretisation error that
[05-03-05](../03-forward-modelling-principles/05-forward-model-validation.md)
teaches you to report.

## 8. Exercises, mistakes, applications

Exercises: [`exercises/02-method-taxonomy-exercises.md`](./exercises/02-method-taxonomy-exercises.md).
Solutions: the companion solutions file.

**Common mistakes.**

1. **Equating "active" with "better".** Passive MT reaches tens of kilometres
   where active EM reaches hundreds of metres; the source does not decide the
   depth range, the physics does.
2. **Believing processing can restore resolution.** It cannot add wavenumbers.
3. **Ignoring the aperture.** A dense but short survey maps shallow detail and
   aliases regional structure into false detail.
4. **Confusing resolution with accuracy.** A poorly positioned, well-sampled
   survey is precisely wrong.
5. **Forgetting that a survey must be designed for a *specific* contrast.**
   Geometry tuned for a weak target wastes money on a strong one.

**Real-world applications.**

- **Mineral and groundwater surveys** use dense, short-aperture arrays because
  the targets are shallow ([04-06-02 Mineral Deposits](../../04-earth-science-geology/06-petroleum-and-mineral-systems/02-mineral-deposits.md)).
- **Crustal imaging** uses long-offset, wide-aperture acquisition
  ([06-seismology](../../06-seismology/README.md)).
- **Geothermal exploration** combines passive MT with active seismic because
  neither contrast alone is diagnostic.
- **Airborne magnetics** trade resolution for coverage, then use the
  line-spacing argument in Section 3 to state what was lost.

## 9. Further reading

- **Sheriff, R. E. & Geldart, L. P. (1995). *Exploration Seismology* (2nd ed.).**
  Chapters 1–3. Level: intermediate. The clearest statement of source–receiver
  geometry and the CMP concept.
- **Telford, Geldart & Sheriff (1990). *Applied Geophysics*.** Chapters 1 and
  4–7. Level: intermediate. Method-by-method acquisition practice.
- **Kearey, P., Brooks, M. & Hill, I. (2002). *An Introduction to Geophysical
  Exploration* (3rd ed.).** Level: beginner to intermediate. A readable
  classification of methods.

## 10. Related lessons

- [05-01-03 Resolution, Penetration Depth and the Fundamental Trade-Off](./03-resolution-depth-tradeoff.md)
- [05-01-05 Choosing a Method: A Decision Framework](./05-choosing-a-method.md)
- [05-05-01 Survey Planning: Objectives, Target Resolution, Budget](../05-survey-design-and-acquisition/01-survey-planning.md)
- [03-03-05 scipy.signal](../../03-scientific-computing/03-scipy/05-signal.md)

## Self-assessment checklist

- [ ] I can classify a method on all four axes.
- [ ] I can compute $\Delta z_\text{res} = v/(4B)$ and state its assumptions.
- [ ] I can explain what the aperture and the receiver spacing each control.
- [ ] I can state why potential-field resolution is not improvable by
      instrumentation.
- [ ] I can name the geometry that gives the best resolution and say what it
      costs.
