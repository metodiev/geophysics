# 06 — Seismology

**Stages:** intermediate → research

Seismology is the highest-resolution probe we have of the solid Earth. It is
also the discipline in which the gap between what we *measure* and what we
*report* is widest, and most of this folder exists to keep that gap visible. What
a seismometer records is ground motion as a function of time at a point. What a
seismologist reports is a **source** (a moment tensor, a depth, a rupture
history), a **structure** (a P- and S-wave speed field, a discontinuity, an
attenuation field), and an **uncertainty**. Every one of those is inferred, and
each inference imports assumptions — about the source, about the wavelet, about
the velocity model used to locate the event, about the Earth being layered —
that the data alone cannot check.

The organising principle of the folder is therefore a single question asked in
thirteen different ways: **what does this measurement actually constrain, and
what does it leave free?** A first-motion focal mechanism constrains two of the
moment-tensor degrees of freedom and leaves the rest to the waveform. A single
Ps delay time constrains a curve of (depth, velocity-ratio) pairs, not a depth.
A travel-time tomography model constrains the data coverage, not the Earth. A
magnitude saturates because the quantity it was designed to measure stops being
the quantity the instrument sees. These are not caveats appended to the physics;
in this folder they *are* the physics, and the lessons are written so that each
result arrives with its non-uniqueness attached.

Three distinctions recur often enough to state once:

- **The forward problem versus the inverse problem.** Seismology is mostly an
  inverse problem, but it is only ever solved through a forward model: you cannot
  interpret a record without a theory that predicts one. Every module here
  develops a forward model *first*, verifies it against something computable
  independently, and only then inverts it. When an inversion is presented, so is
  the way its answer was tested.
- **Kinematics versus dynamics.** Travel times, moveouts and ray paths describe
  *where and when* energy went; moment tensors, rupture dynamics and scattering
  describe *why*. The folder moves from waves (modules 01–02), through sources
  (03) and their location and size (04), into the structure they sample
  (05–07), the geometry they are collected in (08–10), and the hazard and
  societal questions they answer (11–12).
- **Resolution versus detection.** A thin layer, a weak conversion or a slow
  velocity change can be *detected* long after it has become *unresolvable*.
  Reporting one as the other is the commonest overclaim in the subject, and
  several lessons measure the difference explicitly.

## Learning objectives for the folder

By the end of this folder you will be able to:

1. **Derive** the elastodynamic wave equation from Hooke's law and Newton's law,
   obtain the P and S speeds from the elastic moduli and density, and obtain the
   Rayleigh and Love dispersion relations.
2. **Compute** ray paths, travel times and amplitudes in a layered or laterally
   varying Earth using the ray parameter, Snell's law, the $\tau(p)$ formalism and
   ray tracing.
3. **Represent** an earthquake source as a moment tensor, decompose it into
   isotropic, double-couple and compensated-linear-vector-dipole parts, and
   predict the radiation pattern it produces.
4. **Locate** an earthquake from arrival times, quantify the location uncertainty
   from the velocity model and station geometry, and improve it by relative
   location methods.
5. **Distinguish** the magnitude scales, explain why they saturate, and compute a
   moment magnitude and a radiated energy from an appropriate measurement.
6. **Measure** attenuation by at least two independent methods, separate intrinsic
   from scattering attenuation, and interpret an attenuation image in terms of
   temperature and state.
7. **Formulate** a tomographic inverse problem, state its parametrisation, and
   read a resolution and null-space analysis instead of a picture.
8. **Retrieve** an empirical Green's function from ambient noise and use it for
   tomography and for monitoring a velocity change with coda-wave interferometry.
9. **Extract** a receiver function, measure crustal thickness and the
   $v_p/v_s$ ratio by H-k stacking, and state the trade-off that limits each.
10. **Process** a reflection section — deconvolution, velocity analysis, NMO,
    stack, migration — and interpret an AVO response with its assumptions made
    explicit.
11. **Estimate** a $b$-value, decluster a catalogue, and carry out and criticise a
    probabilistic seismic-hazard analysis.
12. **Explain** the mechanisms of induced seismicity, the logic of a traffic-light
    protocol, and the evidence from documented cases.

## Modules

Modules are in dependency order. Module numbers are *not* difficulty labels.

| # | Module | Focus | Why it matters downstream |
|---|---|---|---|
| 01 | [Elastic Wave Propagation](./01-elastic-wave-propagation/README.md) | The elastodynamic equation; P, S, Rayleigh and Love waves; interface waves, scattering and anisotropy | The wave physics every other module assumes |
| 02 | [Ray Theory and Travel Times](./02-ray-theory-and-travel-times/README.md) | The eikonal equation, Snell's law, $\tau(p)$, ray tracing, shadow zones, fast marching | The high-frequency limit used to locate events and image structure |
| 03 | [Earthquake Sources](./03-earthquake-sources/README.md) | Faulting and slip, the double couple, moment tensors, source time functions, spectra, rupture dynamics, explosion discrimination | Turns a seismogram into a physical source |
| 04 | [Earthquake Location and Magnitude](./04-earthquake-location-and-magnitude/README.md) | Hypocentre location, velocity-model dependence, relative location, magnitude scales and saturation, focal mechanisms | The basic catalogue quantities every regional study depends on |
| 05 | [Attenuation and Anelasticity](./05-attenuation-and-anelasticity/README.md) | Measuring $Q$, scattering versus intrinsic loss, Kramers-Kronig causality, attenuation tomography | The amplitude counterpart of travel-time structure; a probe of temperature |
| 06 | [Seismic Tomography](./06-seismic-tomography/README.md) | Path-integral data, travel-time and full-waveform inversion, the adjoint method, resolution and null space, global mantle models | The main route from travel times to a three-dimensional Earth |
| 07 | [Ambient Noise and Seismic Interferometry](./07-ambient-noise-and-interferometry/README.md) | Noise sources, Green's-function retrieval by cross-correlation, noise tomography, autocorrelation, coda monitoring | Structure and time-lapse change without an earthquake |
| 08 | [Receiver Functions and Crustal Structure](./08-receiver-functions-and-crustal-structure/README.md) | Ps conversions, H-k stacking, Moho depth and sharpness, anisotropy, joint inversion | The standard single-station crustal-image method |
| 09 | [Reflection Seismology](./09-reflection-seismology/README.md) | Impedance and the convolutional model, the processing flow, velocity analysis, migration, AVO, multiples, 4-D | The exploration industry's core method and the bridge to folder 11 |
| 10 | [Refraction and Near-Surface Seismology](./10-refraction-and-near-surface-seismology/README.md) | Refraction geometry, delay-time methods, refraction tomography, MASW/SASW, site characterisation | The shallowest and most applied branch; feeds engineering and hazard |
| 11 | [Earthquake Statistics and Hazard](./11-earthquake-statistics-and-hazard/README.md) | Gutenberg-Richter and $b$-value, aftershock statistics, the limits of prediction, PSHA, ground-motion models, hazard maps | Converts a catalogue into a societal decision, with its uncertainty |
| 12 | [Induced and Triggered Seismicity](./12-induced-and-triggered-seismicity/README.md) | Injection and extraction, pore-pressure diffusion, rate-and-state triggering, traffic-light protocols, case studies | Where seismology meets regulation and public consent |
| 13 | [Planetary and Applied Seismology Frontiers](./13-planetary-and-exploration-seismology/README.md) | Planetary seismology, glacial and volcano seismology, distributed acoustic sensing | Extends the toolkit to other bodies, other sources and new sensors |

## The dependency spine

```text
06-01 Elastic waves ──> 06-02 Rays & travel times ──> 06-04 Location & magnitude ──> 11 Hazard
      │                         │                             │
      │                         ├──> 06-06 Tomography ────────┤
      │                         │                             └──> 12 Global geophysics (interior)
      │                         └──> 06-10 Refraction / near-surface ──> 14 Hydrology, 23 Field methods
      │
      ├──> 06-03 Sources ──> 06-04 Location & magnitude
      ├──> 06-05 Attenuation ──> 06-06 Tomography
      ├──> 06-07 Ambient noise ──> 06-06 Tomography
      ├──> 06-08 Receiver functions ──> 12 Global geophysics (interior)
      └──> 06-09 Reflection ──> 11 Exploration, 04-06 Petroleum systems
```

Four rules of thumb follow:

1. **Waves before everything.** Modules 01 and 02 are the vocabulary. A moment
   tensor, a tomographic kernel and an AVO gradient are all statements about
   waves, and none of them can be read by someone who has not derived the wave
   equation and the ray parameter.
2. **Sources before location.** You cannot assess a hypocentre without knowing
   what initiated the wave; the origin time, the depth and the mechanism are
   entangled, and module 03 is what disentangles them.
3. **Structure is an inverse problem; treat it as one.** Modules 05–07 all end in
   an image, and in all three the resolution analysis is part of the result, not
   an appendix. Read module 06's resolution lesson before believing any
   tomographic picture.
4. **Modules 09 and 10 are the same physics in different geometries.** Reflection
   and refraction share the wave equation of module 01 and the rays of module 02;
   what differs is the target depth, the acquisition and the processing. Learn to
   move between them, and note where both meet folder 11.

## Which modules do you actually need?

| Goal | Minimum path |
|---|---|
| Understand how seismic waves travel and are recorded | 01, 02 |
| Work on earthquake sources or seismotectonics | 01, 02, 03, 04 |
| Work on Earth structure or global tomography | 01, 02, 05, 06 |
| Work on crustal structure from passive data | 01, 02, 07, 08 |
| Work in exploration, reservoir or petroleum seismology | 01, 02, 09 |
| Work in engineering, near-surface or hydrogeophysics | 01, 02, 10 |
| Work in earthquake hazard or catastrophe risk | 01, 02, 04, 11 |
| Work on induced seismicity or regulation | 01, 02, 04, 11, 12 |
| Work on planetary or volcano seismology | 01, 02, 03, 13 |

## Suggested paths

**If you are new to seismology:** read modules 01 and 02 in full, in order, running
each demonstration and doing the exercises. They are the two modules on which the
rest of the folder stands. Then take modules 03 and 04 together — a source is only
meaningful with a location and a size — and only then choose among the imaging
modules (05–09).

**If you come from physics or mathematics and want the geophysics:** read
[01-01](./01-elastic-wave-propagation/01-wave-equation-elastic.md) for the
elastodynamic equation, [02-01](./02-ray-theory-and-travel-times/01-eikonal-and-rays.md)
for the high-frequency limit, and then
[03-03](./03-earthquake-sources/03-moment-tensors.md) for the moment tensor.
Those three carry the formal content that the remaining modules apply. Skim
modules 01 and 02's descriptive sections for vocabulary and go straight to the
inverse-problem modules 05–07.

**If you already know travel-time seismology and want the modern methods:** read
[06-04](./06-seismic-tomography/04-full-waveform-inversion.md) and
[06-05](./06-seismic-tomography/05-adjoint-methods.md) for full-waveform and
adjoint inversion,
[07-02](./07-ambient-noise-and-interferometry/02-cross-correlation-green.md) for
noise interferometry, and
[13-04](./13-planetary-and-exploration-seismology/04-distributed-acoustic-sensing.md)
for distributed acoustic sensing — the three developments that have most changed
the subject since the classical textbooks.

**If you are preparing a research project:** read the resolution and null-space
lesson [06-03](./06-seismic-tomography/03-resolution-and-nullspace.md), the
attenuation separation lesson
[05-02](./05-attenuation-and-anelasticity/02-scattering-vs-intrinsic.md), and the
hazard critique [11-04](./11-earthquake-statistics-and-hazard/04-psha.md). Each is
a worked example of stating what a data set does *not* determine.

## Mastery checkpoint for the folder

Produce one integrated artefact:

> **From arrivals to a defensible source-and-structure statement.** Given a small
> synthetic data set of three-component records from a local array (which you may
> generate yourself, using the forward-modelling code of modules 01–02): (a) pick
> P and S arrivals and locate the event, reporting an error ellipse and the
> velocity model you assumed; (b) invert the first motions and the waveforms for a
> moment tensor and decompose it; (c) estimate a magnitude on two scales and
> explain any disagreement; (d) from the same event, measure an attenuation
> operator and state whether it is intrinsic or scattering; (e) state, for each of
> (a)–(d), which quantity you have measured and which you have inferred, and name
> one additional observation that would most reduce the largest remaining
> uncertainty. A worked version of the location and magnitude steps appears in the
> module 04 exercises; the point of the checkpoint is the uncertainty accounting,
> not the numbers.

This single exercise links modules 01, 02, 03, 04 and 05, and it is the reasoning
that [12-global-geophysics-interior](../12-global-geophysics-interior/README.md)
and [11-exploration-geophysics](../11-exploration-geophysics/README.md) will
assume you can already do.

## Conventions used throughout

| Symbol | Meaning | Typical unit |
|---|---|---|
| $u_i$ | Particle displacement (component $i$) | m, or nm s |
| $v_p, v_s$ | P- and S-wave speeds | km/s (crustal) or m/s (near-surface) |
| $\lambda, \mu$ | Lamé parameters (shear modulus $\mu$) | Pa |
| $\rho$ | Mass density | kg/m³ |
| $p$ | Ray parameter, $p = \sin\theta / v$ | s/km, or s/° |
| $\tau$ | Intercept time, $\tau = t - p\,\Delta$ | s |
| $t$ | Travel time | s |
| $\Delta$ | Epicentral distance | ° or km |
| $M_0$ | Seismic moment | N·m |
| $M_w$ | Moment magnitude | dimensionless |
| $Q$ | Quality factor (attenuation) | dimensionless |
| $M_{ij}$ | Moment-tensor components | N·m |
| $k = v_p/v_s$ | Velocity ratio | dimensionless |
| $b$ | Gutenberg-Richter $b$-value | dimensionless |

Full definitions are in the
[symbol handbook](../26-reference-library/02-symbols-and-units/01-symbol-handbook.md);
the rounded Earth and source values this folder uses as nominal anchors are in
[26-02-03 Physical Constants and Earth Parameters with Sources](../26-reference-library/02-symbols-and-units/03-constant-handbook.md).

## A caution about numbers in this folder

Crustal velocities, Moho depths, $Q$ values, $b$-values, corner frequencies and
ground-motion amplitudes **vary** — between regions, between events, and between
analysts of the same data. Where this folder gives a number it gives a *teaching
value* with its units and its provenance (a synthetic model, or a named standard
constant), never an unsourced figure with the authority of a measurement. Every
demonstration is reproducible from the code in its module's `code/` directory, is
print-only, uses a fixed random seed (`np.random.default_rng(20261014)`), and
requires no network access. Unless a lesson explicitly says otherwise, **all
models and data in this folder are SYNTHETIC**.

## How to use the code

Every module carries a `code/` directory of self-contained demonstrations and an
`exercises/` directory of graded problems with worked solutions. Run a module's
demos with the project virtual environment, from the module's `code/` directory;
each module README lists its own commands. For example:

```bash
cd 06-seismology/01-elastic-wave-propagation/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python wave_equation_demo.py
```

The repository-wide quality gate, which checks structure, frontmatter, links and
LaTeX, is documented in
[03-quality-gate](../00-orientation/03-how-to-use-this-repo/03-quality-gate.md).

## Where this folder sits

Seismology sits between the Earth-context folders and the applied and
mathematical folders. It assumes
[04-earth-science-geology](../04-earth-science-geology/README.md) for what the
Earth is made of and
[05-core-geophysics](../05-core-geophysics/README.md) for what a geophysical
measurement is. It supplies
[11-exploration-geophysics](../11-exploration-geophysics/README.md),
[12-global-geophysics-interior](../12-global-geophysics-interior/README.md) and
[13-geodynamics-tectonics](../13-geodynamics-tectonics/README.md) with their
primary observable, and it depends on
[18-inverse-problems](../18-inverse-problems/README.md) and
[20-signal-processing](../20-signal-processing/README.md) for the general theory
of the inversions and filters it uses.
