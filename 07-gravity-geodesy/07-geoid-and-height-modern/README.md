# Module 07-07 — The Geoid and Modern Height Determination

**Stages:** doctoral → research · **Prerequisites:** modules 07-01, 07-04 and
07-05; the inverse-problem vocabulary of folder 18.

This module is where the geoid stops being a concept and becomes a number with an
error budget. The geoid is the equipotential surface that best fits mean sea
level, and it is used every day to turn a GNSS ellipsoidal height into a height
above sea level. It is also the one geodetic product that cannot be measured
directly: it is computed, from gravity, and every metre of it is a statement
about a model.

The organising difficulty is the same one that runs through the whole folder, in
its sharpest form: **the geoid is a long-wavelength quantity computed from a
short-wavelength measurement.** In this module's synthetic field, 98.2% of the
geoid variance sits in harmonic degrees 2–10, while the gravity anomaly's power is
spread across the spectrum. Stokes' integral converts one into the other with a
kernel that does not decay, so a regional survey — however dense — inherits its
geoid's long wavelengths from a global model. Every lesson here therefore reports
a *three-part* answer: the reference model and its error, the data region and its
resolution, and the method used to combine them.

The three lessons follow the product through its three lives: how the geoid is
computed (01), how it becomes a national vertical datum and a choice of origin
(02), and how it is subtracted from a measured sea surface to expose the ocean's
circulation (03). Each lesson's demonstration measures the thing that normally
goes unmeasured: the propagation of a reference-model error into a geoid, the
crossover length at which GNSS plus a geoid beats spirit levelling, and the
wavelength at which a geoid error swamps an ocean current.

All models and data in this module are **SYNTHETIC**. The coefficient spectrum,
the reference model, the levelling line, the heights, the geoid, the sea-surface
topography, the jet and every error level are teaching values. No measured
gravity field, geoid model, national datum, tide gauge or ocean current is used.

## Learning objectives

By the end of this module you will be able to:

1. **State** the geodetic boundary-value problem and **derive** Stokes' integral
   from the $(l-1)$ relation between the gravity anomaly and the disturbing
   potential.
2. **Describe** the Stokes kernel's $1/\psi$ singularity and its vanishing
   integral, and **explain** what each implies for a numerical implementation.
3. **Quantify** what a regional gravity data set can determine, by comparing the
   spectra of the geoid and the gravity anomaly.
4. **Apply** remove–restore and **measure** the geoid error a reference model's
   coefficient error produces.
5. **Derive** the least-squares collocation estimator and **state** the sense in
   which it is optimal only under an assumed covariance.
6. **Derive** a geopotential number from levelling and **compute** dynamic,
   orthometric and normal heights from it.
7. **Distinguish** a datum offset from a height-system difference, and **state**
   which affects differences and which does not.
8. **Build** the error budget of a GNSS-plus-geoid height and **compute** the
   baseline length at which it beats levelling.
9. **Define** the mean dynamic topography, **compute** the geostrophic velocity it
   implies, and **quantify** the velocity error from a stated geoid error.
10. **Find** the wavelength at which a geoid-error spectrum swamps an
    oceanographic signal, and **name** the independent data that validate a
    circulation product.

## Prerequisites

- [07-01 Gravity Fundamentals](../01-gravity-fundamentals/README.md) — the
  potential, Bruns' formula and the gravity reductions.
- [07-04 Geodesy and Reference Frames](../04-geodesy-reference-frames/README.md) —
  height systems, datums and GNSS.
- [07-05 Satellite Gravimetry](../05-satellite-gravimetry/README.md) — where the
  long-wavelength coefficients come from.
- [18 Inverse Problems](../../18-inverse-problems/README.md) — covariance,
  regularisation and conditioning, used in lesson 01.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Determining the Geoid: Stokes, Remove-Restore, Kriging](01-geoid-determination.md) | research | 98% of the geoid is long-wavelength and unobservable locally; the reference model is the answer |
| 02 | [Vertical Datum Modernisation and National Height Systems](02-vertical-datum-modernisation.md) | doctoral | A height is a geopotential divided by a gravity; a datum offset is a choice and cancels in differences |
| 03 | [Sea Surface Topography and the Marine Geoid](03-sea-surface-topography.md) | doctoral | The ocean's signal is 1% of the geoid, and the geostrophic balance differentiates the error |

## Suggested path

**If you are new to geoid computation:** lesson 01 in full, running the
demonstration. Take the band table in §3 seriously — it is the reason the rest of
the lesson exists. Then 02 §1–3 for how the geoid becomes a height.

**If you are here for height systems:** 02 in full, after 01 §4 (remove–restore
and the reference-model error). The height-system arithmetic of 02 §1–2 is
self-contained.

**If you are here for the ocean:** 03 in full, after 01 §3–4. The geostrophic
argument of 03 §2–4 is self-contained, but the geoid-error spectrum it uses comes
from 01.

**If you are preparing a research project:** 01 §4–5 (the reference-model error
and the conditioning of collocation), 02 §5–6 (error budgets and the
verifiability of a datum change) and 03 §4–5 (spectral comparison and the limits
of validation), plus the ★★★ exercises in all three lessons.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-geoid-determination.md`](01-geoid-determination.md) | Lesson 01 |
| [`02-vertical-datum-modernisation.md`](02-vertical-datum-modernisation.md) | Lesson 02 |
| [`03-sea-surface-topography.md`](03-sea-surface-topography.md) | Lesson 03 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Three runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
pandas (SciPy is used for Legendre functions and one-dimensional quadrature):

```bash
cd 07-gravity-geodesy/07-geoid-and-height-modern/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python geoid_determination_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python vertical_datum_modernisation_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python sea_surface_topography_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), requires no network access, and exits 0.
Each runs in under a second.

## Mastery checkpoint

Complete this without notes:

> A national agency has a synthetic gravity data set covering a region, a
> satellite-only reference model with a 0.2% relative coefficient error at
> degrees 2–20, a levelling network with a 1 mm/√km standard, and a GNSS service
> with a 1.5 cm vertical error. **(a)** Compute the geoid error the reference model
> contributes. **(b)** State whether the region's own gravity data can fix it, and
> why. **(c)** Estimate the geoid's accuracy requirement for a 1 cm height target,
> and state whether it is met. **(d)** Compute the levelling/GNSS+geoid crossover
> for absolute heights with a 2 cm geoid error. **(e)** State which of the
> following a datum change must publish: the height system, the datum offset, the
> geoid model, checkpoints in both systems — and which single item makes the
> transformation verifiable.

A worked version of (a), (d) and (e) appears in the lesson-01 and lesson-02
solutions; the point of the checkpoint is the error accounting.

## Common pitfalls across this module

1. **A geoid accuracy without a reference model and a band.** Both are part of
   the number.
2. **Believing regional gravity determines a geoid.** It determines the residual
   geoid; the long wavelengths are a model.
3. **A height without a height system.** Orthometric, normal and dynamic heights
   of the same point differ by decimetres.
4. **Confusing a datum offset with a height-system difference.** One cancels in
   differences; the other does not.
5. **Assuming the new method is always better.** Compute the crossover.
6. **Using the geoid and the ocean to check each other.** A geoid error looks
   exactly like a plausible current.

## Related modules

- [07-01 Gravity Fundamentals](../01-gravity-fundamentals/README.md) — the
  potential, Bruns' formula and the reductions.
- [07-04 Geodesy and Reference Frames](../04-geodesy-reference-frames/README.md) —
  datums, height systems and GNSS, which this module supplies a geoid for.
- [07-05 Satellite Gravimetry](../05-satellite-gravimetry/README.md) — the
  long-wavelength coefficients that make a modern geoid possible.
- [07-06 Earth Tides and Rotation](../06-earth-tides-and-rotation/README.md) —
  corrections and frames that a geoid computation inherits.
- [15 Oceanography and Marine Geophysics](../../15-oceanography-marine/README.md) —
  the user of the marine geoid and the MDT.
- [18 Inverse Problems](../../18-inverse-problems/README.md) and
  [26 Reference Library](../../26-reference-library/README.md).
