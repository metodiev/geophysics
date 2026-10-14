# Module 06-08 — Receiver Functions and Crustal Structure

**Stages:** advanced → research · **Prerequisites:** modules 06-01 and 06-02;
basic signal processing.

This module turns a single three-component seismogram into a measurement of
crustal structure. It is built around one honest difficulty: a P-to-S conversion
time depends on layer thickness *and* velocity ratio, so one measurement gives a
curve of possible Earths, not a number. Every lesson either derives that
non-uniqueness or shows how to reduce it with more data — and every lesson states
which of the two it is doing.

All models and data in this module are **SYNTHETIC**. No real station, event or
waveform is used, and no number is quoted from a published measurement.

## Learning objectives

By the end of this module you will be able to:

1. Derive the Ps delay time from ray geometry and explain why the down-going P
   leg is common to the direct and converted arrivals.
2. Quantify the depth–velocity-ratio trade-off from a single delay.
3. Explain and measure the resolution/noise trade-off of deconvolution, and
   choose a water level against a stated noise level.
4. Build and interpret an H-k stacking surface as a ridge, reporting admitted
   ranges rather than a single answer.
5. Separate a primary conversion from a multiple using moveout.
6. State the signature of anisotropy and the precise sense in which a single
   station cannot distinguish it from a dipping interface.
7. Combine receiver functions with surface-wave dispersion and quantify how much
   the joint constraint improves the answer.

## Prerequisites

- [06-01 Elastic Wave Propagation](../01-elastic-wave-propagation/README.md) —
  P and S waves, anisotropy.
- [06-02 Ray Theory and Travel Times](../02-ray-theory-and-travel-times/README.md) —
  the ray parameter and Snell's law.
- [03-10 ObsPy and Seismic Data](../../03-scientific-computing/10-obspy-and-seismic-data/README.md) —
  reading, filtering and handling waveforms.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Receiver Functions: Deconvolution and Ps Conversions](01-receiver-function-principle.md) | doctoral | Derive $\Delta t = H(q_s-q_p)$; deconvolution needs a water level; one delay is not two numbers |
| 02 | [H-K Stacking and Crustal Thickness Estimation](02-h-k-stacking.md) | graduate | The multiples break the trade-off; the answer is a ridge |
| 03 | [Moho Discontinuity Depth and Sharpness](03-moho-interface.md) | advanced | Depth is conditional on velocities; sharpness is stated relative to a frequency |
| 04 | [Anisotropy from Receiver Functions and Shear-Wave Splitting](04-anisotropy-receiver-functions.md) | doctoral | Transverse energy is not proof of anisotropy; it is a coverage problem |
| 05 | [Joint Inversion of Receiver Functions and Surface Waves](05-joint-inversion-rf.md) | research | Two different shadows intersect to give a peak |

## Suggested path

**If you are new to receiver functions:** lessons 01–03 in order, running each
demonstration. Lesson 03 is where the practical depth error appears.

**If you already know H-k stacking:** read 01 §3.2 (the trade-off), then 04 and
05 — the two routes to breaking it.

**If you are preparing a research project:** 01 §3.4–3.5 (deconvolution
stability), 04, 05, plus the exercises at ★★★ level.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-receiver-function-principle.md`](01-receiver-function-principle.md) | Lesson 01 |
| [`02-h-k-stacking.md`](02-h-k-stacking.md) | Lesson 02 |
| [`03-moho-interface.md`](03-moho-interface.md) | Lesson 03 |
| [`04-anisotropy-receiver-functions.md`](04-anisotropy-receiver-functions.md) | Lesson 04 |
| [`05-joint-inversion-rf.md`](05-joint-inversion-rf.md) | Lesson 05 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Five runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
ObsPy:

```bash
cd 06-seismology/08-receiver-functions-and-crustal-structure/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python rf_principle_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python hk_stacking_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python moho_interface_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python anisotropy_rf_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python joint_inversion_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), and exits 0. They require no network access.

## Mastery checkpoint

Complete this without notes:

> A station records a Ps delay of $4.10\ \mathrm{s}$ at
> $p = 0.060\ \mathrm{s\,km^{-1}}$, a second conversion at $4.9\ \mathrm{s}$, and
> a peak at $13.4\ \mathrm{s}$. **(a)** Convert the first delay to depth for
> $k = 1.72$ and $v_p = 6.30\ \mathrm{km\,s^{-1}}$, and state in one sentence why
> the answer is not unique. **(b)** Compute $\delta H$ for a $+0.008\
> \mathrm{s\,km^{-1}}$ reference-slowness error. **(c)** Decide which peaks are
> primaries and which are multiples, using moveout. **(d)** State what additional
> measurement would most tighten the depth.

A worked version of (a)–(c) appears in the lesson-03
[solutions](exercises/03-moho-interface-solutions.md).

## Common pitfalls across this module

1. **Quoting a depth without a velocity assumption.** The trade-off is the
   physics, not a caveat.
2. **Choosing a deconvolution water level by taste.** State the noise metric.
3. **Treating a ridge maximum as a point estimate.** Report the admitted set.
4. **Calling transverse energy "anisotropy".** Check the azimuthal coverage first.
5. **Confusing detection with resolution.** A thin or gradational Moho can be
   detected long after its width becomes unresolvable.

## Related modules

- [06-01 Elastic Wave Propagation](../01-elastic-wave-propagation/README.md).
- [06-02 Ray Theory and Travel Times](../02-ray-theory-and-travel-times/README.md).
- [06-09 Reflection Seismology](../09-reflection-seismology/README.md) — the same
  reflection-coefficient and resolution ideas in exploration geometry.
- [18-inverse-problems](../../18-inverse-problems/README.md) — the systematic
  treatment of non-uniqueness and regularisation.
