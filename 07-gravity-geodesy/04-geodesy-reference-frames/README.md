# Module 07-04 — Geodesy and Reference Frames

**Stages:** advanced → doctoral · **Prerequisites:** modules 07-01 and 07-03;
linear algebra; basic statistics.

This module is about the framework that makes a measurement a position and a
height. Its central claim is deflationary and useful: **a coordinate is not a
measurement, it is a definition plus a measurement.** An ellipsoid is chosen, a
frame is realised by a set of stations at an epoch, a height system is selected,
and only then does a number mean something. Every lesson is organised around one
consequence of that claim. Changing the ellipsoid without transforming the datum
moves points by hundreds of metres. Mixing orthometric and ellipsoidal heights
imports a metre of geoid gradient into a levelling line. A frame rotation of a few
tenths of a milliarcsecond per year is indistinguishable from a plate rotation. A
velocity uncertainty computed under a white-noise assumption is optimistic by a
factor of eight or more, and that factor — not the receiver — is what limits what
a geodetic network can resolve.

The module therefore spends as much effort on error structure as on geometry.
Lesson 01 builds the ellipsoid and the transformations, with the round-trip and
limit tests that make an implementation trustworthy. Lesson 02 works in
geopotential numbers, where the four height systems separate cleanly and the
"ignoring gravity" error turns out to be a covariance rather than a magnitude.
Lesson 03 develops the observation equations of satellite positioning, verifies
the DOP prediction by simulation, and shows the collapse of integer ambiguity
resolution as the noise approaches half a cycle. Lesson 04 measures how correlated
noise inflates velocity errors, how a three-station rosette cannot separate strain
from rotation, and how large the land-motion term is in a sea-level budget.
Lesson 05 closes the circle with Euler poles, frame rotations and the
fourteen-parameter transformation of positions and velocities.

All models and data in this module are **SYNTHETIC**. The stations, ellipsoids
(other than the WGS 84 constants used to evaluate normal gravity), datum shifts,
transformations, constellations, baselines, delays, poles, plates and sea-level
records are chosen teaching values. No real station, network, mission, gauge,
plate model or published pole is referenced or quoted.

## Learning objectives

By the end of this module you will be able to:

1. Compute ellipsoid parameters and curvature radii, convert between geodetic and
   Cartesian coordinates, and test the inverse to round-off.
2. Apply and invert a seven-parameter Helmert transformation and quantify the
   coordinate change from reinterpreting coordinates on a new ellipsoid.
3. Compute geopotential numbers and all four height systems, and explain why
   gravity-free levelling errs only through the covariance of gravity and terrain.
4. Interpret a loop misclosure by its scaling with the number of setups, and
   assemble $h = H + N$ with a geoid model's gradient taken into account.
5. Write the pseudorange and phase observation equations, build a geometry matrix,
   compute the DOP quartet, and verify the position covariance by Monte Carlo.
6. Resolve integer ambiguities, measure the fix-rate collapse with noise, and state
   the tests that prevent accepting a wrong fix.
7. Fit trends and seasonal terms to position time series, and quantify the
   inflation of the formal error under correlated noise.
8. Compute strain rates with correct error propagation, and demonstrate the
   strain-rotation ambiguity of a small array.
9. Convert tide-gauge trends to absolute sea level with collocated vertical land
   motion and a defensible uncertainty.
10. Convert Euler poles to velocity fields, invert a velocity field for the Euler
    vector, and quantify the effect of an unmodelled frame rotation.

## Prerequisites

- [07-01-03 Reference Ellipsoid, Normal Gravity and Clairaut's Theorem](../01-gravity-fundamentals/03-normal-gravity.md) —
  the ellipsoid as the surface on which normal gravity is defined.
- [07-01-04 Gravity Reductions: Free-Air, Bouguer, Isostatic and Terrain](../01-gravity-fundamentals/04-gravity-reduction.md) —
  why heights enter every gravity reduction.
- [07-03-04 Gravity Inversion and Its Severe Non-Uniqueness](../03-gravity-anomalies-and-modelling/04-inversion-gravity.md) —
  the aperture and resolution arguments reused in lessons 04 and 05.
- [21-01-02 Choosing Probability Models for Earth Data](../../21-statistics-bayesian-ml/01-statistics-in-practice/02-probability-models-earth.md) —
  the Gaussian and power-law error models used throughout.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Geodetic Datums, Ellipsoids and Coordinate Frames](01-geodetic-datums.md) | advanced | A coordinate is a definition plus a measurement; a datum change moves points by hundreds of metres |
| 02 | [Height Systems: Ellipsoidal, Orthometric, Dynamic and Geoid Models](02-height-systems.md) | graduate | Height is a normalised potential; the four systems differ by millimetres to metres and must be named |
| 03 | [GNSS Positioning: Pseudorange, Carrier Phase and Ambiguity Resolution](03-gnss-positioning.md) | graduate | Geometry sets precision; phase gives millimetres but must be fixed as integers, and a bad fix is worse than none |
| 04 | [GNSS for Tectonics, Subsidence and Sea Level](04-gnss-geodesy-applications.md) | doctoral | Correlated noise, not the instrument, limits velocity; strain needs geometry as well as precision |
| 05 | [ITRF, Plate Motion Models and Frame Transformations](05-itrf-and-plate-models.md) | doctoral | A rigid rotation has three parameters and zero vertical motion; a frame rotation mimics a plate rotation |

## Suggested path

**If you are new to geodesy:** lessons 01, 02 and 03 in order, running each
demonstration. Lesson 02 is where heights stop being "just heights".

**If you already use GNSS positions:** read 01 §5–7 (datums and heights), then 03
§5 (ambiguity resolution) and 04 (noise and error budgets).

**If you are preparing a research project:** 04 and 05, plus the ★★★ exercises in
03 and 04 — the frame, the noise model and the geometry condition are what decide
whether a geophysical conclusion survives review.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-geodetic-datums.md`](01-geodetic-datums.md) | Lesson 01 |
| [`02-height-systems.md`](02-height-systems.md) | Lesson 02 |
| [`03-gnss-positioning.md`](03-gnss-positioning.md) | Lesson 03 |
| [`04-gnss-geodesy-applications.md`](04-gnss-geodesy-applications.md) | Lesson 04 |
| [`05-itrf-and-plate-models.md`](05-itrf-and-plate-models.md) | Lesson 05 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Five runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
pandas:

```bash
cd 07-gravity-geodesy/04-geodesy-reference-frames/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python geodetic_datums_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python height_systems_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gnss_positioning_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gnss_geodesy_applications_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python itrf_and_plate_models_demo.py
```

Every demo is print-only, prints labelled results with units, uses a fixed random
seed (`np.random.default_rng(20261014)`), runs in under a second, and exits 0. They
require no network access and no data files. **The numbers in the lessons are the
numbers these scripts print**; if a script is edited, the lesson text should be
checked against it.

## Mastery checkpoint

Complete this without notes:

> A coastal station has $\varphi = 45^{\circ}$, $\lambda = 15^{\circ}$,
> $h = 250\ \mathrm{m}$ on WGS 84, a collocated levelling benchmark with
> $H = 206.0\ \mathrm{m}$, and a five-year GNSS vertical rate of
> $-1.2\ \mathrm{mm\,yr^{-1}}$ with a white-noise formal error of
> $0.08\ \mathrm{mm\,yr^{-1}}$; the nearby tide gauge reads
> $+2.0\ \mathrm{mm\,yr^{-1}}$.
> **(a)** Compute $N$ from the heights and check it against the ellipsoid geometry.
> **(b)** State the height system each number belongs to.
> **(c)** Give a defensible uncertainty for the vertical rate and the resulting
> absolute sea-level rate with its uncertainty. **(d)** State whether the sign of
> the absolute rate is resolved.

Worked versions of (c) and (d) appear in the lesson-04
[solutions](exercises/04-gnss-geodesy-applications-solutions.md); the height
relations are in the lesson-02
[solutions](exercises/02-height-systems-solutions.md).

## Common pitfalls across this module

1. **Mixing datums.** A latitude or a height without its datum is not a coordinate.
2. **Confusing geodetic and geocentric latitude.** Up to $11.5\ \mathrm{arcmin}$ —
   21 km.
3. **Treating the geoid undulation as a constant.** The gradient, not the
   magnitude, is what ruins a levelling/ellipsoidal mix.
4. **Leaving gravity out of levelling.** The error is a covariance with terrain and
   is systematic.
5. **Reading a loop misclosure without its scaling with setup count.**
6. **Comparing horizontal and vertical GNSS errors directly.** One is a radial
   (2-D) error, the other a linear one.
7. **Accepting an ambiguity fix on rounding alone.** One wrong integer costs a
   whole wavelength.
8. **Quoting white-noise formal errors for station velocities.** They can
   understate the truth by more than an order of magnitude.
9. **Calling a three-station shear a strain rate.** Rotation and shear are
   entangled without enough independent directions.
10. **Comparing absolute and relative sea level** without the vertical land-motion
    term.

## Related modules

- [07-01 Gravity Fundamentals](../01-gravity-fundamentals/README.md) — normal
  gravity, the geoid and the reductions that use these heights.
- [07-03 Gravity Anomalies and Modelling](../03-gravity-anomalies-and-modelling/README.md) —
  the same resolution and non-uniqueness arguments in a potential-field setting.
- [07-06 Earth Tides and Rotation](../06-earth-tides-and-rotation/README.md) —
  rotation of the Earth itself, as opposed to a frame convention.
- [07-07 The Geoid and Modern Height Determination](../07-geoid-and-height-modern/README.md) —
  determining the surface that ties these height systems together.
- [21-statistics-bayesian-ml](../../21-statistics-bayesian-ml/README.md) — noise
  models, regression and uncertainty propagation.
