# Module 17-03 — Radar Remote Sensing

**Stages:** graduate → research (via doctoral) · **Prerequisites:** modules
17-01 and 17-02; the wave and polarisation vocabulary of folder 02; basic linear
algebra.

This module is about the one remote-sensing technique that supplies its own
illumination and measures *phase*. That single fact produces everything here: an
image that works at night and through cloud, a range measurement precise to a
fraction of the wavelength, and a dataset whose dominant error sources are
geometry and weather rather than detector noise.

The module is built as one chain, and each lesson states which limit binds.
Lesson 01 establishes the geometry and the budget — range resolution from
bandwidth, azimuth resolution from antenna length, and the pulse-repetition
window that ties them together. Lessons 02 to 05 handle the phase: what it
measures, why it is only known modulo half a wavelength, how a network of pairs
replaces one fragile unwrapping, what the atmosphere and the orbit add, and what
the four great application families can and cannot conclude. Lessons 06 and 07
break the geometry in the two remaining directions: polarimetry asks *what* is
scattering, and altimetry looks straight down and lets the pulse set the
resolution.

All models and data in this module are **SYNTHETIC**. The carrier frequencies are
teaching values chosen inside the conventional band designations, the orbit,
antenna, baselines, coherence values, deformation fields, screens, slips,
densities and repeat cycles are teaching values chosen so the arithmetic can be
followed with a pencil, and the only external numbers used are exact or standard
constants (the speed of light, Boltzmann's constant, Earth's gravitational
parameter, standard gravity, the rotation rate) plus the stated band ranges and
the standard M2 tidal period. No real mission, sensor, scene, station or measured
displacement appears anywhere in the module.

## Learning objectives

By the end of this module you will be able to:

1. **Derive** the slant- and ground-range resolution of a radar and **explain**
   why a synthetic aperture gives an azimuth resolution of $L/2$ independently of
   range, **verifying** it by matched filtering a simulated chirp.
2. **Derive** the pulse-repetition-frequency window from the azimuth Doppler
   bandwidth and the swath, and **state** which ambiguity each bound prevents.
3. **Derive** the interferometric phase from the two-way path, **demonstrate** the
   $\lambda/2$ ambiguity explicitly, and **state** what additional observation
   removes it.
4. **Derive** the height sensitivity and ambiguity height, **verify** the
   linearisation against the exact geometry, and **measure** the baseline
   decorrelation that limits it.
5. **Assemble** a phase network, **compute** its rank and null space from the pair
   graph, and **distinguish** what a disconnected network leaves undetermined from
   what noise limits.
6. **Quantify** the atmospheric and orbital error budget: the delay-to-
   displacement identity, the stratified and turbulent structure, the aliasing
   budget, and what stacking can and cannot average away.
7. **Interpret** a fringe pattern for an earthquake, a volcano, a subsidence field
   and a landslide, **stating** the projection, the model and the aliasing limit
   that each interpretation depends on.
8. **Decompose** a coherency matrix into entropy, anisotropy and mean scattering
   angle, and **state** which of those parameters are invariant when the matrix is
   degenerate.
9. **Convert** an altimetric round-trip time into a height and a wave height, and
   **compute** the geostrophic current, the tidal alias and the ice thickness that
   follow from it.

## Prerequisites

- [17-01 Remote Sensing Physics](../01-remote-sensing-physics/README.md) —
  the spectrum, sensing windows, reflectance and resolution concepts.
- [17-02 Optical and Thermal Remote Sensing](../02-optical-and-thermal-remote-sensing/README.md) —
  the radiometric framing and the surface-property vocabulary.
- [02-07-05 Electromagnetic Waves, Impedance and Polarisation](../../02-physics/07-electromagnetism/05-em-waves.md) —
  the wave description used for polarimetry and backscatter.
- [01-07-07 Orthogonality, Projections and Least Squares](../../01-mathematics/07-linear-algebra/07-orthogonality.md) —
  the Hermitian eigen-decomposition behind the polarimetric parameters.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [SAR Principles: Geometry, Polarisation, Backscatter](01-sar-principles.md) | graduate | Resolution comes from bandwidth and antenna length; the PRF window ties them together |
| 02 | [InSAR: Interferometric Phase and Deformation Measurement](02-insar.md) | research | The phase measures range modulo $\lambda/2$; coherence sets how well it is known |
| 03 | [InSAR Time Series: PS-InSAR and SBAS](03-insar-time-series.md) | research | Many short baselines convert one fragile unwrapping into a checkable inversion |
| 04 | [Atmospheric and Orbital Error Correction in InSAR](04-insar-atmospheric-correction.md) | research | A delay is indistinguishable from a displacement in one pair |
| 05 | [InSAR for Earthquakes, Volcanoes, Subsidence and Landslides](05-insar-applications.md) | research | Four targets, four different binding limits |
| 06 | [SAR Polarimetry and Polarimetric Decomposition](06-polarimetry.md) | research | Three Pauli channels separate surface, double bounce and volume — within what the model allows |
| 07 | [Radar Altimetry and Sea/Ice Surface Height](07-radar-altimetry.md) | doctoral | Nadir geometry inverts the SAR design: the pulse sets the footprint |

## Suggested path

**If you are new to radar:** 01 in full, then 02 (the ambiguity is the whole
subject), running every demonstration. Stop there if you only need to read a
radar image intelligently.

**If you already know InSAR:** read 01 §3.1–3.4 for the budget, then 02 §3.4–3.6
for the coherence statistics, then 03 for the network, 04 for the errors and 05
for the interpretation. The measured tables are the content; the prose is the
argument around them.

**If you are preparing a research project:** 03 §3.1–3.4 (rank, null space and
what is determined), 04 §3.3–3.6 (the errors that dominate every result) and the
★★★ exercises in each lesson. Lesson 05 is the worked interpretation.

**If you are working in polarimetry:** 01 §3.5 first (the three mechanisms),
then 06 in full, with attention to §3.3 (single-look entropy) and §3.5 (what is
invariant in a decomposition).

## Materials in this module

| Path | Contents |
|---|---|
| [`01-sar-principles.md`](01-sar-principles.md) | Lesson 01 — geometry, resolution, the PRF window, the SNR budget |
| [`02-insar.md`](02-insar.md) | Lesson 02 — the phase, the ambiguity, coherence, speckle, projection |
| [`03-insar-time-series.md`](03-insar-time-series.md) | Lesson 03 — the network, rank, min-norm, PS and SBAS screening |
| [`04-insar-atmospheric-correction.md`](04-insar-atmospheric-correction.md) | Lesson 04 — delay, turbulence, ramps, stacking |
| [`05-insar-applications.md`](05-insar-applications.md) | Lesson 05 — earthquakes, volcanoes, subsidence, landslides |
| [`06-polarimetry.md`](06-polarimetry.md) | Lesson 06 — Pauli basis, coherency matrix, decompositions |
| [`07-radar-altimetry.md`](07-radar-altimetry.md) | Lesson 07 — range, footprint, wave height, geostrophy, aliasing |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Seven runnable demonstrations, one per lesson |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
pandas:

```bash
cd 17-remote-sensing-gis/03-radar-remote-sensing/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python sar_principles_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python insar_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python insar_time_series_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python insar_atmospheric_correction_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python insar_applications_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python polarimetry_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python radar_altimetry_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), requires no network access and exits 0. Each
one verifies at least one of its own claims numerically — a matched-filtered
chirp, a coherence estimator measured against a known truth, a structure-function
exponent, an eigenvector rotation that leaves the observable matrix unchanged —
so the numbers in the lessons are measurements from these scripts rather than
assertions copied into prose.

## Mastery checkpoint

Complete this without notes:

> An interferometric pair with $\lambda = 5.6565\ \mathrm{cm}$,
> $\theta = 35^\circ$, $B_{\perp} = 100\ \mathrm{m}$ and $L = 16$ looks shows a
> wrapped phase change of $+3$ fringes with coherence $0.6$.
> **(a)** Convert the fringe count to a line-of-sight displacement and state the
> displacements that would produce the same observation. **(b)** Compute the
> height ambiguity and say what a $200\ \mathrm{m}$ of relief would do to the
> fringe count. **(c)** Give the phase uncertainty implied by the coherence and the
> look count, and convert it to millimetres of displacement. **(d)** State two
> reasons the answer might be atmospheric rather than deformation, and one
> observation that would settle it.

A worked version of (a)–(c) appears in the lesson-02
[solutions](exercises/02-insar-solutions.md).

## Common pitfalls across this module

1. **Quoting a resolution without the geometry.** Ground-range resolution depends
   on incidence; azimuth resolution depends on the antenna length.
2. **Treating the wrapped phase as a displacement.** It is a displacement modulo
   $\lambda/2$ and it has a sign ambiguity.
3. **Reporting coherence or entropy without the look count.** Both are degenerate
   at one look.
4. **Believing a network determines an absolute level.** Only differences within a
   connected component are determined.
5. **Assuming the atmosphere averages away.** Only the part that is independent
   between acquisitions does.
6. **Reading a projection as a physical motion.** A factor of seven between east
   and north hides in the look vector.
7. **Presenting a decomposition as a measurement.** The number of mechanisms is a
   model decision.
8. **Forgetting the reference surface.** A height without its ellipsoid, geoid or
   mean sea surface is not a height.

## Related modules

- [17-01 Remote Sensing Physics](../01-remote-sensing-physics/README.md) — the
  optical and radiometric foundations.
- [17-04 Satellite Geodesy Techniques](../04-satellite-geodesy-techniques/README.md) —
  the other half of satellite geophysics: GNSS, gravimetry and the tracking
  techniques that also provide the orbits radar needs.
- [17-08 Remote Sensing Applications in Geophysics](../08-remote-sensing-applications-geophysics/README.md) —
  where these measurements are turned into geophysical products.
- [07-05 Satellite Gravimetry](../../07-gravity-geodesy/05-satellite-gravimetry/README.md) —
  the geoid whose error limits every altimetric height.
- [13-04 Tectonophysics and Deformation](../../13-geodynamics-tectonics/04-tectonophysics-deformation/README.md) —
  the earthquake-cycle framework for the deformation measured in lesson 05.
- [18 Inverse Problems](../../18-inverse-problems/README.md) — unwrapping,
  time-series estimation and source inversion as inverse problems with stated
  regularisation.
- [20 Signal Processing](../../20-signal-processing/README.md) — matched
  filtering, sampling and aliasing, the tools used in every lesson here.
