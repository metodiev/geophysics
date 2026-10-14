# Module 15-02 — Marine Geophysical Methods

**Stages:** advanced → research · **Prerequisites:** modules 15-01 (physical
oceanography), 02-03 (oscillations and waves), 02-06 (fluid mechanics) and 09-01
(electrical properties of the Earth); comfort with Fourier transforms,
convolution and with units.

> **All models and data in this module are SYNTHETIC.** Every source wavelet,
> sound-speed profile, seafloor roughness field, sediment reflectivity,
> density contrast, magnetic moment and resistivity model in these lessons is a
> chosen teaching value, printed by a demonstration in `code/`. No survey line,
> cruise, vessel, station, well, prospect, basin or published measurement or
> citation is reproduced. Physical constants ($g$, $\Omega$, $c$ in seawater,
> $\mu_0$, $G$, $\rho_{\text{sw}}$) and exact conventional constants (the Eötvös
> coefficients, the M2 period, $1\ \mathrm{kn} = 0.514444\ \mathrm{m\,s^{-1}}$,
> $1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$) are stated with units.

Marine geophysics has a structural problem that land geophysics does not: the
measurement is made from a moving platform, and everything the surveyor needs to
know about the geometry has to be reconstructed from the same data that carry the
signal. A multibeam system measures depth from a travel time and an assumed sound
speed, so a one-per-cent error in the sound speed is a one-per-cent error in the
depth — and the sound-speed profile is itself measured, with its own uncertainty.
A marine gravity meter measures a difference from a moving reference, so its
largest error term is the platform's velocity, through the Eötvös correction. A
seismic streamer is towed behind the source, so its actual positions are estimated
by a network of compasses and acoustics that the processing has to trust.

The second theme is that **resolution and penetration are the same trade seen
twice**. Every method in this module is a probe whose resolving power is set by
its bandwidth and whose reach is set by attenuation, and the lesson in each case
is to compute both rather than to quote a system specification. The module
therefore measures the trade-offs: the tuning thickness of a 30 Hz wavelet at
$50.4\ \mathrm{m}$ and the $\lambda/4$ limit at $12.6\ \mathrm{m}$; the
$4.0\times$ degradation of a $1^\circ$ beam footprint between nadir and
$60^\circ$; the factor $68.6$ by which a 20 ms continuous-wave pulse is worse than
a 20 ms chirp; the factor $410$ by which frequency-dependent compliance removal
beats a single scalar; the up-to-$99\,\%$ deviation that refutes the
transverse-resistance rule of thumb in the wrong geometry.

The third discipline is that **every result is stated in the geometry it was
derived for**. A migration aperture, a demultiple operator, an Eötvös
correction, a compliance transfer function and a skin depth are all conditional:
change the water depth, the velocity or the source geometry and the number
changes. Where a lesson crosses from a derivation to a survey decision, it says
which assumption is doing the work.

## Learning objectives

By the end of this module you will be able to:

1. **Compute** a water-bottom reflection coefficient, an incidence angle from a
   streamer offset, and the moveout that a stacking velocity must correct, and
   **quantify** a stacking loss from a stated velocity error.
2. **Derive** the swath width and footprint of a beam-forming sonar, and
   **assemble an error budget** for a depth measurement, identifying the
   dominant term.
3. **Compute** side-scan across-track and along-track resolution from the grazing
   angle, the pulse length and the altitude, and **evaluate** a sonar equation for
   the maximum range.
4. **Design** a chirp waveform for a stated resolution, and **measure** the
   compression, the side-lobe level and the penetration/resolution trade from the
   matched-filter output.
5. **Derive** the Eötvös correction and the free-air and Bouguer gradients, and
   **reduce** a synthetic gravity reading to an anomaly with a stated budget.
6. **Compute** the water-layer multiple period, a receiver-function delay and the
   compliance-removal residual, and **evaluate** the clock, tilt, coupling and
   noise requirements of an ocean-bottom deployment.
7. **Derive** the skin depth, **evaluate** a layered electromagnetic response, and
   **demonstrate** with numbers why a plane-wave seafloor measurement is
   water-dominated and what the controlled-source geometry does instead.

## Prerequisites

- [15-01 Physical Oceanography](../01-physical-oceanography/README.md) —
  the sound speed, stratification and wave physics every method here assumes.
- [02-03 Oscillations and Waves](../../02-physics/03-oscillations-and-waves/README.md) —
  dispersion, superposition and the bandwidth of a pulse.
- [02-06 Fluid Mechanics](../../02-physics/06-fluid-mechanics/README.md) —
  the continuum description of water and sediment.
- [09-01 Resistivity, Conductivity and Conduction Mechanisms](../../09-electrical-em-methods/01-electrical-properties-of-earth/01-resistivity-conductivity.md) —
  the property the last lesson measures.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Marine Seismic Reflection: Airguns, Streamers, Processing](01-marine-seismic-reflection.md) | graduate | A reflection coefficient of 0.39 is the largest signal in marine seismics, and it is the one you spend the most effort removing |
| 02 | [Multibeam Bathymetry and Swath Mapping](02-multibeam-bathymetry.md) | advanced | Depth is a travel time divided by an assumed sound speed, so the error budget is dominated by the assumption, not the instrument |
| 03 | [Side-Scan Sonar and Seafloor Imaging](03-side-scan-sonar.md) | advanced | Backscatter is amplitude, so the interpretable quantity is the grazing-angle dependence, and the resolution collapses at the far range |
| 04 | [Sub-Bottom Profiling and Chirp Systems](04-sub-bottom-profiling.md) | graduate | Bandwidth buys resolution and attenuation takes it back; the compressed pulse is a matched filter's output, not a transmitted wavelet |
| 05 | [Marine Gravity and Magnetic Surveys](05-marine-gravity-magnetics.md) | graduate | The largest correction is the platform's own velocity; the Eötvös term is 7.5 mGal per knot |
| 06 | [Ocean-Bottom Seismology and OBS Networks](06-obn-ocean-bottom-seismology.md) | doctoral | The water layer is both the method's finest ruler and its worst generator of coherent noise |
| 07 | [Marine CSEM and EM for Gas Hydrates](07-marine-csem-em.md) | research | The ocean is five skin depths thick, so the geometry must avoid the screening rather than correct it |

## Suggested path

**If you are new to marine geophysics:** lessons 02 and 03 in order, then 05. They
share one framework — a travel time or a field difference, an assumed constant,
and an error budget — and they are the three whose numbers you can verify from a
harbour wall.

**If you come from exploration seismics:** read 01, then 04 and 06. Lesson 04 is
where the resolution/penetration trade becomes arithmetic; lesson 06 is where the
water layer stops being a nuisance and becomes the experiment.

**If you are preparing a research project:** 04 §4–6 (matched filter, gain and
penetration law), 06 §3–6 (compliance, clock, tilt) and 07 §5 (the
resistivity–thickness trade), plus the ★★★ exercises in each companion set, which
are written as survey designs rather than as algebra.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-marine-seismic-reflection.md`](01-marine-seismic-reflection.md) | Lesson 01 |
| [`02-multibeam-bathymetry.md`](02-multibeam-bathymetry.md) | Lesson 02 |
| [`03-side-scan-sonar.md`](03-side-scan-sonar.md) | Lesson 03 |
| [`04-sub-bottom-profiling.md`](04-sub-bottom-profiling.md) | Lesson 04 |
| [`05-marine-gravity-magnetics.md`](05-marine-gravity-magnetics.md) | Lesson 05 |
| [`06-obn-ocean-bottom-seismology.md`](06-obn-ocean-bottom-seismology.md) | Lesson 06 |
| [`07-marine-csem-em.md`](07-marine-csem-em.md) | Lesson 07 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Seven runnable demonstrations, one per lesson |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
ObsPy:

```bash
cd 15-oceanography-marine/02-marine-geophysics-methods/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python marine_seismic_reflection_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python multibeam_bathymetry_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python side_scan_sonar_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python sub_bottom_profiling_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python marine_gravity_magnetics_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python obn_ocean_bottom_seismology_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python marine_csem_em_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), requires no network access and exits 0. They
are print-only — no plots are produced — so the output can be compared line by
line with the tables in the lessons. Every demo runs in under ten seconds; the
sub-bottom and OBS demos are the slowest because they transform and correlate
records of several thousand samples.

## Mastery checkpoint

Complete this without notes:

> A synthetic survey in $1500\ \mathrm{m}$ of water ($c = 1500\
> \mathrm{m\,s^{-1}}$, $\rho = 1025\ \mathrm{kg\,m^{-3}}$ over
> $\rho = 1900\ \mathrm{kg\,m^{-3}}$, $v_p = 1600\ \mathrm{m\,s^{-1}}$) uses a
> 30 Hz wavelet, a $1^\circ$ beam sonar, and a 20 ms, 2–6 kHz chirp.
> **(a)** Compute the water-bottom reflection coefficient at normal incidence and
> the $\lambda/4$ resolution limit. **(b)** Compute the multibeam footprint at
> nadir and at $60^\circ$ incidence at a 2000 m slant range. **(c)** Compute the
> compressed pulse length and the range resolution of the chirp.
> **(d)** Compute the two-way water attenuation at $0.1\ \mathrm{Hz}$ for the
> electromagnetic measurement of the same seafloor.

Worked versions of (a)–(b) appear in the lesson-01 and lesson-02 solutions
([01](exercises/01-marine-seismic-reflection-solutions.md),
[02](exercises/02-multibeam-bathymetry-solutions.md)); (c) is in
[04](exercises/04-sub-bottom-profiling-solutions.md) and (d) in
[07](exercises/07-marine-csem-em-solutions.md).

## Common pitfalls across this module

1. **Quoting a depth without its sound speed.** Every acoustic depth in this
   module is a travel time multiplied by an assumed velocity, and the percentage
   errors are equal.
2. **Using a survey's processing velocity as a physical velocity.** Stacking
   velocities are fitted to moveout and are not $v_p$ of the rock.
3. **Confusing resolution with accuracy.** A system can resolve 12 m features and
   be systematically 20 m wrong; both numbers belong in the same sentence.
4. **Treating backscatter amplitude as reflectivity.** Sonar amplitude is
   geometry, gain, absorption and calibration as well as the seafloor.
5. **Forgetting that a matched filter outputs a wavelet, not a pulse.** The
   compressed peak width is set by the bandwidth, and the side lobes are set by
   the window.
6. **Differencing two gravity readings as if the platform were still.** The
   Eötvös correction is the largest term for a ship, and the free-air gradient is
   $0.30785\ \mathrm{mGal\,m^{-1}}$.
7. **Applying the transverse-resistance rule to a plane-wave sounding.** Lesson
   07 measures deviations of up to $99\,\%$ for models with equal $\rho h$.
8. **Exporting a model's numbers to a real survey.** Every model here is
   synthetic; only the *structure* — the trade-offs, the budgets, the
   non-uniqueness — transfers.

## Related modules

- [Module 15-01 Physical Oceanography](../01-physical-oceanography/README.md) —
  the water column and its sound speed, which every instrument in this module
  either measures or assumes.
- [Module 15-03 Seafloor Tectonics and Structure](../03-seafloor-tectonics/README.md) —
  what the reflection and refraction measurements are used to interpret.
- [Module 15-04 Seafloor Mapping and Habitat Characterisation](../04-seafloor-mapping-and-habitats/README.md) —
  where bathymetry, backscatter and sub-bottom data become a map and a habitat.
- [06-08 Receiver Functions and Crustal Structure](../../06-seismology/08-receiver-functions-and-crustal-structure/README.md) —
  the land version of the ocean-bottom conversion work in lesson 06.
- [09-05 EM Methods and Applications](../../09-electrical-em-methods/05-em-methods-applications/README.md) —
  the controlled-source method that lesson 07 applies at the seafloor.
- [20-01 Signals and Systems](../../20-signal-processing/01-signals-and-systems/README.md) —
  convolution, transfer functions and the matched filter used throughout.
