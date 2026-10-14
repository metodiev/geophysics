# Module 09-06 — Borehole Electrical and EM Methods

**Stages:** graduate → doctoral · **Prerequisites:** modules 09-01 and 09-02;
basic potential theory and linear algebra.

This module takes the electrical and electromagnetic methods underground, where
the geometric factors can be computed exactly and the answer can be checked
against a closed form. It is built around one honest difficulty, repeated in three
regimes: **what the measurement can resolve is set by geometry, not by the
instrument.** A cross-hole DC survey measures a diffuse, sign-changing sensitivity
distribution rather than a ray, and its inversion admits whole families of models
that fit the data equally well. A cross-hole radar survey measures travel times
along nearly parallel paths, so its ray matrix is rank-deficient and a model
perturbation larger than the target is invisible to the data. An induction log
averages the formation over a window set by the coil spacing, so a thin bed can
never read its own conductivity and the apparent bias grows as the square root of
conductivity.

Each lesson therefore does two things: it derives the forward model and verifies
it against something computable independently, and then it *measures* the
non-uniqueness — a null-space model, an equivalent model, a shoulder-effect
deficit — rather than listing it as a caveat. The tools that make this possible are
deliberately modest: a whole-space Green's function, an exact image series, a
closed-form induction response, and a straight-ray matrix. Every one of them has a
limit that can be stated, and every lesson states it.

All models and data in this module are **SYNTHETIC**. No real borehole, site,
instrument or published number is used.

## Learning objectives

By the end of this module you will be able to:

1. Derive the whole-space Green's function and use it to compute geometric factors,
   transfer resistances and apparent resistivities that pass a forward check.
2. Derive the adjoint sensitivity kernel of a four-electrode measurement and
   verify it against the exact uniform-perturbation response.
3. Build a tomographic Jacobian, read its singular spectrum and resolution
   diagonal, and state what fraction of an anomaly the inversion can recover.
4. Construct an equivalent model that fits the data as well as the inversion
   result and quantify how much further from the truth it is.
5. Compute dielectric velocities, wavelengths and low-loss attenuation, and check
   the loss-tangent condition that makes the wave treatment valid.
6. Explain why a single-hole reflection gives range but not azimuth, and quantify
   what a directional antenna or a second geometry contributes.
7. Measure the numerical rank and null space of a cross-hole ray geometry and
   demonstrate a model perturbation that changes the data by
   $10^{-13}$ of the picking error.
8. Derive the skin depth and the induction number, and relate them to the
   resolution and calibration of a downhole EM tool.
9. Derive the exact homogeneous two-coil induction response, separate its in-phase
   and quadrature channels, and quantify the skin-effect bias of a quadrature
   calibration.
10. Derive Doll's geometric factor from the ring-flux identity and use it to
    compute the vertical resolution and the shoulder effect of a sonde.

## Prerequisites

- [09-01 Electrical Properties of Earth Materials](../01-electrical-properties-of-earth/README.md) —
  conductivity, Archie's law and clay conduction.
- [09-02 DC Resistivity Methods](../02-dc-resistivity/README.md) — arrays,
  geometric factors, forward modelling and inversion.
- [09-05 Applied Electromagnetic Methods](../05-em-methods-applications/README.md) —
  apparent conductivity in the surface geometry.
- [05-08 Geophysical Logging](../../05-core-geophysics/08-geophysical-logging/README.md) —
  the borehole environment and the multi-log interpretation context.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Cross-Hole and Borehole-to-Surface Tomography](01-cross-hole-tomography.md) | doctoral | The sensitivity is a signed diffuse kernel, not a ray; equivalent models fit equally well |
| 02 | [Borehole Radar and Directional Probing](02-borehole-radar.md) | doctoral | Range without azimuth; a rank-deficient ray matrix; damping decides the image |
| 03 | [Downhole EM Logging and Induction Tools](03-downhole-em-logging.md) | graduate | Conductivity is a volume average; the calibration bias grows as $\sqrt{\sigma}$ |

## Suggested path

**If you are new to borehole methods:** read 03 first. It is the simplest geometry
(one hole, one coil pair) and it introduces skin depth, the induction number and
the geometric factor — all of which reappear in the two doctoral lessons.

**If you come from DC resistivity:** read 01, then 03 §4, then 02. The first two
share the geometric-factor language; the third changes the physics from diffusion
to propagation and shows where that change matters.

**If you are preparing a research project:** read 01 §5–7 (rank, resolution,
equivalence), 02 §4 (rank deficiency and the null space), and the ★★★ exercises of
both. Those three sections are the transferable content: they are the same
arguments that module 18 applies to every geophysical inverse problem.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-cross-hole-tomography.md`](01-cross-hole-tomography.md) | Lesson 01 |
| [`02-borehole-radar.md`](02-borehole-radar.md) | Lesson 02 |
| [`03-downhole-em-logging.md`](03-downhole-em-logging.md) | Lesson 03 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Three runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
SymPy:

```bash
cd 09-electrical-em-methods/06-borehole-electrical/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python cross_hole_tomography_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python borehole_radar_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python downhole_em_logging_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), needs no network access, and exits 0. The
three together run in about a second and a half.

## Mastery checkpoint

Complete this without notes.

> **(a)** Two boreholes 15 m apart are used for a whole-space cross-hole survey in
> a $50\ \Omega\,\mathrm{m}$ formation. Compute the geometric factor of the
> quadrupole $A=(0,0,5)$, $B=(0,0,7)$, $M=(15,0,5)$, $N=(15,0,7)$ and check the
> forward model. **(b)** State the sensitivity kernel, its units and the
> normalisation identity it must satisfy, and say what the identity does not test.
> **(c)** Your inversion of a $+50\%$ conductivity body returns $+27\%$. Give the
> two distinct reasons — one geometric, one numerical — why the amplitude is low.
> **(d)** A single-hole radar survey in the same hole measures a reflection at
> 82 ns and cannot place it in azimuth. Quantify the ambiguity and name two
> measurements that remove it. **(e)** A 1 m spacing, 20 kHz induction sonde is run
> in the same formation. Compute the skin depth, the induction number and the
> expected quadrature bias, and state whether the tool can resolve a $10\%$
> conductivity change.

A worked version of (a)–(c) appears in the lesson-01
[solutions](exercises/01-cross-hole-tomography-solutions.md); a worked version of
(e) appears in the lesson-03
[solutions](exercises/03-downhole-em-logging-solutions.md).

## Common pitfalls across this module

1. **Treating a sensitivity as a ray.** DC cross-hole sensitivity is diffuse,
   signed and maximal near the electrodes; ray language belongs to the
   high-frequency limit of lesson 02.
2. **Quoting a tomogram as a picture.** Report the resolution diagonal or the
   admissible set beside the image.
3. **Confusing coverage with resolution.** Many paths through a cell do not
   resolve it if they are parallel.
4. **Forgetting the $4\pi$ in the whole-space Green's function.** Always check
   that $K(\Delta V/I)$ returns the model resistivity.
5. **Assuming rather than checking low loss.** Compute $\sigma/(\omega\varepsilon)$.
6. **Reading a conductivity log as a lithology log.** Fluid, clay, geometry and
   metallic content all enter, and a single frequency does not separate them.

## Related modules

- [09-07 EM Data Processing, QC and Uncertainty](../07-em-data-processing-and-qc/README.md) —
  how the error budget of a borehole survey is assembled and reported.
- [09-01 Electrical Properties of Earth Materials](../01-electrical-properties-of-earth/README.md),
  [09-02 DC Resistivity Methods](../02-dc-resistivity/README.md),
  [09-05 Applied Electromagnetic Methods](../05-em-methods-applications/README.md) —
  the prerequisites in order.
- [05-08 Geophysical Logging](../../05-core-geophysics/08-geophysical-logging/README.md) —
  the borehole measurements this module quantifies.
- [18-inverse-problems](../../18-inverse-problems/README.md) — the systematic
  treatment of rank, null space and equivalence.
