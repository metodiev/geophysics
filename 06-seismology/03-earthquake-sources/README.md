# Module 06-03 — Earthquake Sources

**Stages:** advanced → doctoral · **Prerequisites:** modules 06-01 and 06-02;
single-variable calculus, linear algebra and NumPy proficiency.

This module answers a deceptively simple question: *what did the earthquake
actually do?* A seismogram is a filtered, delayed, direction-dependent record of
a source, and the job of source theory is to invert that record into a few
numbers — a moment, a mechanism, a stress drop, a duration — and to say honestly
how much of each number is measurement and how much is model. The module starts
from the elastic rebound cycle and ends at a monitoring discriminant, so that
every abstraction has a use by the time it appears.

The central honest difficulty is that **almost every source quantity is a
product of a measurement and an assumption, and the assumption is usually
invisible**. A depth is conditional on a velocity ratio. A stress drop is a
moment times a corner frequency cubed, divided by a model constant that nobody
measures. A moment magnitude depends on which offset the author used. A
final slip from a rupture integration can fall short of its asymptote because the
integration window ended, not because the fault arrested. Every lesson in this
module contains at least one of these trade-offs worked out arithmetically, and
several contain a place where the intended narrative had to be corrected against
what the code actually printed.

All models and data in this module are **SYNTHETIC**. No real earthquake,
catalogue, station, waveform, measured constant or published number is quoted.
Every numeric value in the lessons and exercises is either printed by one of the
seven demonstrations in [`code/`](code) or is an exact standard constant stated
with its units. The model *constants* that enter — the Brune constant $k$, the
Eshelby factor $16/7$, the friction law — are labelled as choices wherever they
appear, because that labelling is the point.

## Learning objectives

By the end of this module you will be able to:

1. Derive the loading rate, recurrence interval, slip, seismic moment and moment
   rate of a fault from a block-slider model, and state which inputs are
   measured, nominal or chosen.
2. Construct a moment tensor from fault geometry, derive the four-lobe radiation
   pattern, and identify the conventions under which $P$ and $T$ labels are
   defined.
3. Decompose any moment tensor into isotropic, double-couple and CLVD parts, and
   state what a non-zero CLVD does and does not mean.
4. Derive the emission-time distribution of a propagating rupture, compute the
   directivity contrast, and distinguish the moment-rate duration from the
   apparent duration.
5. Measure a corner frequency, invert it for stress drop, and quantify how a
   model constant propagates — cubed — into the answer.
6. Build the energy budget of a dynamic rupture, verify the radiated-energy
   identity, and recognise a truncated integration from the numbers alone.
7. Explain and quantify two explosion/earthquake discriminants, and state why
   two band amplitudes bound a source rather than identify it.

## Prerequisites

- [06-01 Elastic Wave Propagation](../01-elastic-wave-propagation/README.md) —
  P and S waves, potentials and the representation theorem.
- [06-02 Ray Theory and Travel Times](../02-ray-theory-and-travel-times/README.md) —
  the ray parameter, travel times and the far-field approximation.
- [05-04 Rock Physics](../../05-core-geophysics/04-rock-physics/README.md) —
  elastic moduli and their relation to rock properties.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Faulting, Slip and the Elastic Rebound Cycle](01-faulting-and-slip.md) | advanced | $\dot\tau = \mu V/W$ gives $T = \Delta\tau W/(\mu V)$; the moment *rate* is set by area and plate rate, not by event size |
| 02 | [The Double-Couple Source and Radiation Patterns](02-double-couple.md) | graduate | $A(\hat r) = (\hat r\cdot\hat n)(\hat r\cdot\hat s)$ — four lobes, half the sphere compressional, and a fault-plane ambiguity |
| 03 | [Moment Tensors, Decomposition and Physical Meaning](03-moment-tensors.md) | doctoral | $M = M_{\text{iso}} + M^{\text{dc}} + M^{\text{clvd}}$ is an identity; reading the parts physically is a model |
| 04 | [Source Time Functions, Rupture Kinematics and Directivity](04-source-time-function.md) | doctoral | $\sigma^2 = \sigma_w^2+\sigma_d^2$ is an incoherent bound; the same event has different durations at different azimuths |
| 05 | [Source Spectra, Corner Frequency and Stress Drop](05-source-spectra.md) | graduate | The plateau measures $M_0$; $f_c$ gives $\Delta\sigma$ only through a model constant, cubed |
| 06 | [Rupture Dynamics, Fracture Energy and Scaling Laws](06-rupture-dynamics.md) | doctoral | $M_0\propto f_c^{-3}$ until the seismogenic width saturates; radiated energy is the residual after the fracture bill |
| 07 | [Discriminating Explosions from Earthquakes](07-nuclear-explosion-sources.md) | graduate | An explosion cannot radiate dilatation; two band amplitudes bound a source but do not identify it |

## Suggested path

**If you are new to source theory:** lessons 01, 02 and 05 in order, running each
demonstration. These three carry the definitions used everywhere else (slip,
moment, radiation pattern, corner frequency).

**If you already know moment tensors:** read 03 §3.4–3.5 (the decomposition and
its orthogonality) and 04 §3.2–3.4 (the quadrature bound and the truncation
artefact), then 06.

**If you are preparing a research project:** 03 (decomposition conventions), 04
(directivity), 05 §3.4–3.5 (model-constant sensitivity), 06 §3.3–3.5 (energy
budget and integration discipline), plus the ★★★ exercises.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-faulting-and-slip.md`](01-faulting-and-slip.md) | Lesson 01 |
| [`02-double-couple.md`](02-double-couple.md) | Lesson 02 |
| [`03-moment-tensors.md`](03-moment-tensors.md) | Lesson 03 |
| [`04-source-time-function.md`](04-source-time-function.md) | Lesson 04 |
| [`05-source-spectra.md`](05-source-spectra.md) | Lesson 05 |
| [`06-rupture-dynamics.md`](06-rupture-dynamics.md) | Lesson 06 |
| [`07-nuclear-explosion-sources.md`](07-nuclear-explosion-sources.md) | Lesson 07 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Seven runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
ObsPy:

```bash
cd 06-seismology/03-earthquake-sources/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python faulting_and_slip_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python double_couple_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python moment_tensor_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python source_time_function_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python source_spectra_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python rupture_dynamics_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python nuclear_explosion_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)` where randomness is used), writes no files,
draws no plots and exits 0. They require no network access.

## Mastery checkpoint

Complete this without notes.

> A SYNTHETIC strike-slip fault has $\mu = 3.0\times10^{10}\ \mathrm{Pa}$,
> brittle width $W = 12\ \mathrm{km}$, plate rate $V = 35\ \mathrm{mm\,a^{-1}}$
> and mean stress drop $\Delta\tau = 3.0\ \mathrm{MPa}$. **(a)** Compute the
> loading rate, the mean recurrence interval, the coseismic slip and $M_0$ for a
> $40\ \mathrm{km}\times12\ \mathrm{km}$ rupture. **(b)** State which of those
> four numbers depend on the assumed $\Delta\tau$ and which do not. **(c)** Give
> one reason each for the recurrence interval being a *mean* and for the depth
> being a *conditional* number. **(d)** A corner frequency of
> $0.246\ \mathrm{Hz}$ is measured for the event; with $k = 0.37$ and
> $\beta = 3500\ \mathrm{m\,s^{-1}}$, compute the equivalent radius, explain why
> the answer depends on $k$, and state what changes if $k = 0.50$ is used.
> **(e)** Compute the $M_0$–$f_c$ exponent implied by constant stress drop and
> state the one assumption behind it. **(f)** Name the observable that would
> separate a shallow isotropic source from this event and say why it is decisive.

Worked versions of parts of (a)–(e) appear in the lesson-01, 05 and 06
[solutions](exercises/).

## Common pitfalls across this module

1. **Quoting a derived quantity without its model input.** Depths need a
   velocity ratio; stress drops need $k$; magnitudes need an offset and a unit.
2. **Reading a decomposition as a measurement.** $M_{\text{iso}}$,
   $M^{\text{dc}}$ and $\varepsilon$ are all computed from an inverted tensor.
3. **Treating an incoherent sum rule as exact.** The quadrature duration
   $\sqrt{\sigma_w^2+\sigma_d^2}$ is an upper bound.
4. **Ignoring directivity.** Durations, corner frequencies and stress drops are
   azimuth-dependent, and the stress drop inherits the error cubed.
5. **Assuming one scaling exponent.** Self-similarity ends at the seismogenic
   width.
6. **Trusting a number a demo prints for a narrative.** Check whether a
   discrepancy is uniform across rows — a constant fractional offset is a
   computation, not physics.
7. **Assuming station independence.** A source-level probability is an upper
   bound on a network's discriminant power.

## Related modules

- [06-01 Elastic Wave Propagation](../01-elastic-wave-propagation/README.md) —
  the wave physics that carries the source signal.
- [06-04 Earthquake Location and Magnitude](../04-earthquake-location-and-magnitude/README.md) —
  how the source parameters of this module become reported locations and
  magnitudes.
- [06-05 Attenuation and Anelasticity](../05-attenuation-and-anelasticity/README.md) —
  the path effect that must be removed before any spectrum is called a source
  spectrum.
- [06-11 Earthquake Statistics and Hazard](../11-earthquake-statistics-and-hazard/README.md) —
  how the moment rate and scaling branches of this module become hazard.
- [06-12 Induced and Triggered Seismicity](../12-induced-and-triggered-seismicity/README.md) —
  the Coulomb criterion and non-double-couple sources in practice.
- [18-inverse-problems](../../18-inverse-problems/README.md) — the systematic
  treatment of non-uniqueness and regularisation used throughout.
