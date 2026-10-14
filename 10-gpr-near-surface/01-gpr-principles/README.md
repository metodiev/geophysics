# Module 10-01 — GPR Principles

**Stages:** intermediate → graduate · **Prerequisites:** basic electromagnetism
(Maxwell's equations, plane waves and impedance), wave reflection and simple
dimensional analysis.

This module builds the physics of ground-penetrating radar from one question:
what does a recorded time actually constrain? A GPR system measures a voltage
against time at a point. Everything a practitioner draws — a depth, a layer
thickness, a water content, the position of a buried pipe — is an inference that
runs through a wave speed, and the wave speed is not measured. The module is
arranged so that each result arrives with the assumption that produced it
attached, and so that every non-uniqueness is quantified rather than mentioned.

The five lessons follow the geometry of a single measurement. Lesson 01 derives
the speed and the reflection coefficient from Maxwell's equations in the low-loss
limit and states exactly where that limit stops being valid. Lesson 02 asks how
the speed is obtained in practice — from the air and ground waves, from the
curvature of a diffraction hyperbola, or from the moveout of a multi-offset
gather — and measures what a constant-velocity correction leaves behind. Lesson
03 is about energy: which loss mechanisms set the penetration, why conduction
loss is frequency-independent in this regime, and how $\alpha$ and $Q$ are
measured from two reflections. Lesson 04 leaves the medium and describes the
antenna: its medium-dependent resonance, its broad radiation pattern, the
critical angle that traps energy in the ground, and the offset-imposed blind zone
$d_{\min} = x/2$. Lesson 05 closes the loop with resolution — vertical,
horizontal, and the spatial sampling that decides which apparent dips are
geology.

**All models and data in this module are SYNTHETIC.** The permittivities,
conductivities, quality factors, layer models and noise levels are chosen
teaching values; no field site, instrument model, measured travel time or
published number is quoted. Every number in the lessons is printed by a
demonstration in [`code/`](./code), and the demonstrations are the source of the
numbers rather than an illustration of them.

## Learning objectives

By the end of this module you will be able to:

1. **Derive** $v = c/\sqrt{\varepsilon_r}$ and $\alpha = (\sigma/2)\sqrt{\mu/
   \varepsilon}$ from a damped wave equation, and **compute** the loss tangent
   that decides whether they may be used.
2. **Compute** normal-incidence reflection and transmission coefficients and
   **verify** the energy budget at a dielectric interface.
3. **Convert** measured two-way times to depths with a stated velocity, and
   **quantify** the depth error from a velocity error, a time-zero error and a
   single-velocity approximation in a layered medium.
4. **Estimate** a velocity from air-wave and ground-wave arrival times, from a
   diffraction hyperbola fit, and from CMP moveout with Dix inversion, and
   **state** the aperture each method needs.
5. **Compute** conduction and constant-$Q$ attenuation, **build** a two-way
   amplitude budget, and **solve** for the depth at which a stated dynamic range
   is exhausted.
6. **Measure** $\alpha$ and $Q$ from a spectral ratio, **state** its fitting band,
   and **explain** when the spectral-centroid estimator fails.
7. **Compute** the critical angle, the surface footprint and the polarisation
   coupling of a dipole antenna, and **derive** the near-surface blind zone
   $d_{\min} = x/2$.
8. **Quantify** vertical resolution against a stated criterion, **derive** the
   Fresnel zone radius with its convention, **measure** migrated lateral
   resolution, and **predict** the apparent dip an under-sampled grid produces.

## Prerequisites

- [02-07-03 Maxwell's Equations and Their Physical Meaning](../../02-physics/07-electromagnetism/03-maxwell-equations.md) —
  the four equations and the displacement and conduction currents.
- [02-07-05 Electromagnetic Waves, Impedance and Polarisation](../../02-physics/07-electromagnetism/05-em-waves.md) —
  plane waves, refractive index and wave impedance.
- [02-03-08 Reflection, Refraction and Snell's Law for Waves](../../02-physics/03-oscillations-and-waves/08-reflection-refraction.md).
- [02-03-09 Diffraction, Scattering and Resolution Limits](../../02-physics/03-oscillations-and-waves/09-diffraction.md) —
  the wave-physics background to the resolution lesson.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [GPR Physics: EM Pulses, Dielectric Permittivity and Reflection](01-gpr-physics.md) | intermediate | $v = c/\sqrt{\varepsilon_r}$ and $R = (\sqrt{\varepsilon_1}-\sqrt{\varepsilon_2})/(\sqrt{\varepsilon_1}+\sqrt{\varepsilon_2})$ hold only while $\tan\delta \ll 1$ |
| 02 | [Velocity Estimation and Depth Conversion in GPR](02-gpr-velocity-and-depth.md) | advanced | Depth is a family indexed by velocity; the hyperbola's curvature is the measurement |
| 03 | [Attenuation, Penetration Depth and Frequency Trade-Offs](03-gpr-attenuation-penetration.md) | advanced | Conduction loss is frequency independent; penetration is a dynamic-range question |
| 04 | [Antennas: Frequency, Shielding, Polarisation and Offsets](04-gpr-antennas.md) | graduate | The antenna is medium-loaded, wide-angle, polarisation-sensitive, and blind above $x/2$ |
| 05 | [Vertical and Horizontal Resolution Limits](05-gpr-resolution.md) | advanced | Resolution needs its criterion, its aperture and its band; detection is not resolution |

## Suggested path

**If you are new to GPR:** lessons 01–03 in order, running each demonstration
before reading the arithmetic in the lesson. Lesson 02 is where the depth
non-uniqueness first bites.

**If you already know the radar equation:** read 01 §4 (regime of validity) and
§6 (what a nominal frequency is), then 03 and 05 — the two ends of the frequency
decision.

**If you are preparing a field survey or a research project:** 02 §4 (Dix and its
error amplification), 04 (offsets, blind zone, polarisation), and 05 §4–5
(aperture-limited resolution and aliasing), then the ★★★ exercises.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-gpr-physics.md`](01-gpr-physics.md) | Lesson 01 |
| [`02-gpr-velocity-and-depth.md`](02-gpr-velocity-and-depth.md) | Lesson 02 |
| [`03-gpr-attenuation-penetration.md`](03-gpr-attenuation-penetration.md) | Lesson 03 |
| [`04-gpr-antennas.md`](04-gpr-antennas.md) | Lesson 04 |
| [`05-gpr-resolution.md`](05-gpr-resolution.md) | Lesson 05 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Five runnable, print-only demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy and SymPy:

```bash
cd 10-gpr-near-surface/01-gpr-principles/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gpr_physics_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gpr_velocity_and_depth_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gpr_attenuation_penetration_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gpr_antennas_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gpr_resolution_demo.py
```

Every demonstration prints labelled results with units, uses the fixed seed
`np.random.default_rng(20261014)`, requires no network access, and exits 0.
None of them opens a window or a file: the output is the result.

## Mastery checkpoint

Complete this without notes:

> A $200\ \mathrm{MHz}$ survey with antennas $0.30\ \mathrm{m}$ apart images a
> reflector at $t = 40.0\ \mathrm{ns}$ in ground whose $\varepsilon_r$ is believed
> to be $9$ with $\sigma = 1\times10^{-3}\ \mathrm{S\,m^{-1}}$.
> **(a)** Compute $\tan\delta$ and decide whether $v = c/\sqrt{\varepsilon_r}$
> applies.
> **(b)** Convert the pick to a depth and state the error for a $10\%$ velocity
> error.
> **(c)** Compute the shallowest depth that can be separated from the ground
> wave, and the two-way time of a reflector at half that depth.
> **(d)** Compute the two-way attenuation loss at the reflector in dB, and the
> attenuation length $1/(2\alpha)$.
> **(e)** Compute $\lambda$, the Rayleigh-type vertical resolution limit, and the
> first Fresnel diameter at the reflector depth.
> **(f)** State one additional measurement that would remove most of the depth
> ambiguity.

Parts (a)–(e) are worked, with the numbers, across the five lesson solution files
in [`exercises/`](./exercises).

## Common pitfalls across this module

1. **Quoting a depth without the velocity that produced it.** The trade-off is the
   physics, not a caveat appended to it.
2. **Using the low-loss formulas in a lossy medium.** Compute the loss tangent
   first; it costs one line.
3. **Confusing detection with resolution.** In the SYNTHETIC model of lesson 05 a
   $2.3\ \mathrm{mm}$ bed is detectable and utterly unresolvable.
4. **Believing that lower frequency always penetrates deeper.** Conduction loss is
   frequency independent, and the relaxation term saturates against it.
5. **Reading an "antenna frequency" as a bandwidth.** The medium sets the
   resonance; the recorded spectrum is the only evidence.
6. **Quoting a resolution number without its criterion, aperture and band.**
   Reasonable criteria differ by a third.
7. **Trusting an aliased dip.** At $\Delta x = \lambda/2$ a $45^\circ$ event
   appears to dip the other way.

## Related modules

- [10-02 GPR Acquisition and Processing](../02-gpr-acquisition-and-processing/README.md) —
  the geometry and the processing that this module's physics assumes.
- [08-04 Electromagnetic Induction](../../08-geomagnetism-electromagnetism/README.md) —
  the diffusive regime of the same equations.
- [09-01 Electrical Properties of Earth Materials](../../09-electrical-em-methods/01-electrical-properties-of-earth/README.md) —
  what measured permittivity and conductivity actually look like.
- [06-10 Refraction and Near-Surface Seismology](../../06-seismology/10-refraction-and-near-surface-seismology/README.md) —
  the complementary method at the same depth range.
- [05-05 Survey Design and Data Acquisition Principles](../../05-core-geophysics/05-survey-design-and-acquisition/README.md) —
  the general design framework this module specialises to radar.
