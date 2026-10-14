# Module 17-01 — Remote Sensing Physics

**Stages:** beginner → graduate · **Prerequisites:** [02-10 Radiative Transfer,
Blackbody Radiation and Kirchhoff's Law](../../02-physics/10-optics-and-photometry/03-radiative-transfer.md)
and [16-02 Solar and Terrestrial
Radiation](../../16-atmosphere-climate/02-radiation-and-energy-balance/01-solar-and-terrestrial-radiation.md);
basic calculus and dimensional analysis.

This module establishes what a remote-sensing measurement physically is before any
of the later modules use one. It follows a single photon path: the spectrum and
the atmospheric windows decide which wavelengths are available at all; the
surface decides what fraction of the arriving radiation is reflected, absorbed or
emitted; the atmosphere on the return path adds, removes and re-emits; and the
instrument decides how finely, how often and how precisely the result can be
recorded. Each of the four lessons takes one stage of that path and quantifies
its consequences.

The organising idea is that **every remote-sensing quantity is an inference with
a stated error budget**. A reflectance is not measured, it is retrieved: the
sensor measures radiance, and reflectance comes out of a model with a path
radiance, two transmittances and an illumination term, each of which contributes
error. A surface temperature is not measured either — it depends on an emissivity
assumption and an atmospheric correction whose errors in the thermal infrared are
of the *same magnitude* and can partly cancel, so a retrieval can appear accurate
for the wrong reason. Rather than list these as caveats, the module derives each
error propagation and measures it in a demonstration, so that the numbers arrive
with the claim.

The module is deliberately numerical. Every lesson contains a fully worked
example, every claimed figure is printed by a runnable demonstration in `code/`,
and the demonstrations are print-only: they generate their synthetic scenes,
spectra and instrument geometries in code with a fixed random seed and require no
network access. Where a demonstration's measurement contradicted an intended
statement during writing, the lesson was changed to match the measurement.

All models and data in this module are **SYNTHETIC**. No real station, sensor,
mission, dataset or atmospheric measurement is used. The physical constants
quoted (the Planck constant, the speed of light, the Boltzmann and
Stefan-Boltzmann constants, Wien's displacement constant, the solar constant and
the mean Earth radius) are exact or standard values and are labelled as such;
every other number is output of a demonstration in this module.

## Learning objectives

By the end of this module you will be able to:

1. **Convert** between wavelength, frequency and photon energy, and **decide**
   which wavelengths can reach a surface sensor through an atmosphere.
2. **Derive** Wien's displacement law and the Stefan-Boltzmann law from the Planck
   function, and **compute** the solar and terrestrial emission regimes.
3. **Convert** a measured radiance to a reflectance through a Lambertian model,
   and **state** where the Lambertian assumption fails and by how much.
4. **Apply** energy conservation and Kirchhoff's law to obtain emissivity from
   reflectance, and **quantify** the surface-temperature error a wrong emissivity
   produces.
5. **Separate** path radiance, transmittance and surface signal in a sensor
   radiance, and **compute** the reflectance error from mishandling each term.
6. **Propagate** an atmospheric-parameter uncertainty to a retrieved reflectance
   by linearisation and by Monte Carlo, and **explain** the small positive bias
   of a noisy multiplicative correction.
7. **Compute** the ground sample distance, the diffraction limit, the sampling
   Nyquist frequency and the system MTF, and **decide** whether a design is
   aperture-limited, detector-limited or aliased.
8. **Compute** a spectral resolving power, a revisit time and a noise-equivalent
   temperature difference, and **quantify** the spatial/spectral/radiometric
   trade.
9. **State** the non-uniqueness of a single-band mixed-pixel measurement and
   **parametrise** its null space.

## Prerequisites

- [02-10-03 Radiative Transfer, Blackbody Radiation and Kirchhoff's Law](../../02-physics/10-optics-and-photometry/03-radiative-transfer.md)
  — the Planck function and radiative-transfer vocabulary.
- [02-10-04 Spectroscopy Principles for Remote Sensing](../../02-physics/10-optics-and-photometry/04-spectroscopy.md)
  — absorption features and band-depth measurement.
- [16-02-01 Solar and Terrestrial Radiation, Blackbody Laws](../../16-atmosphere-climate/02-radiation-and-energy-balance/01-solar-and-terrestrial-radiation.md)
  — the top-of-atmosphere energy balance.
- [16-02-02 Radiative Transfer in the Atmosphere](../../16-atmosphere-climate/02-radiation-and-energy-balance/02-radiative-transfer-atmosphere.md)
  — the atmospheric radiative-transfer equation.
- [20-01-05 Sampling, Nyquist and Reconstruction](../../20-signal-processing/01-signals-and-systems/05-sampling-theory.md)
  — the sampling theorem behind the aliasing criterion.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [The Electromagnetic Spectrum and Sensing Windows](01-em-spectrum-remote-sensing.md) | beginner | Wien and Stefan-Boltzmann fix the two emission regimes; windows are a property of the atmosphere, not the instrument |
| 02 | [Reflectance, Emissivity and Spectral Signatures](02-reflectance-and-emissivity.md) | advanced | $\rho$ and $\varepsilon$ are one measurement through Kirchhoff; a signature is a shape with a weight, not a value |
| 03 | [Atmospheric Attenuation, Scattering and Correction](03-atmospheric-effects.md) | graduate | Correction is an inversion: path radiance, transmittance and scattering each carry their own error budget |
| 04 | [Spatial, Spectral, Temporal and Radiometric Resolution](04-resolution-concepts.md) | intermediate | Four resolutions trade against one budget; a GSD is a sampling interval, not a resolution |

## Suggested path

**If you are new to remote sensing:** lessons 01 → 02 → 04, running each
demonstration. Lesson 03 is the graduate-level step and is easiest after the
first three.

**If you come from physics or signal processing:** read 01 §3 and 02 §3 quickly,
then 03 and 04 in full — the correction error budget and the resolution trade are
where the remote-sensing content is.

**If you are preparing a research project:** 02 §3.4 (emissivity-to-temperature
sensitivity), 03 §3.4–3.6 (error propagation and convexity), and 04 §3.7 with the
exercises at ★★★ level.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-em-spectrum-remote-sensing.md`](01-em-spectrum-remote-sensing.md) | Lesson 01 |
| [`02-reflectance-and-emissivity.md`](02-reflectance-and-emissivity.md) | Lesson 02 |
| [`03-atmospheric-effects.md`](03-atmospheric-effects.md) | Lesson 03 |
| [`04-resolution-concepts.md`](04-resolution-concepts.md) | Lesson 04 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Four runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
pandas:

```bash
cd 17-remote-sensing-gis/01-remote-sensing-physics/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python em_spectrum_remote_sensing_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python reflectance_emissivity_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python atmospheric_correction_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python resolution_concepts_demo.py
```

Every demo prints labelled results with units, uses the fixed seed
`np.random.default_rng(20261014)`, reads no files, needs no network access, and
exits 0.

## Mastery checkpoint

Complete this without notes:

> A sensor at $700\ \mathrm{km}$ with a $0.30\ \mathrm{m}$ aperture and a
> $12\ \mathrm{\mu m}$-equivalent ground pitch is observing a surface at
> $300\ \mathrm{K}$ with $\varepsilon = 0.95$ under a synthetic atmosphere with
> $\tau_{\rm vert}(0.55\,\mathrm{\mu m}) = 0.250$, and the Sun is at $30°$ zenith.
> **(a)** Compute the surface radiance in the $10.8\ \mathrm{\mu m}$ band and the
> temperature retrieved if the atmosphere is ignored. **(b)** Compute the
> reflectance error at $0.66\ \mathrm{\mu m}$ if path radiance is ignored
> entirely. **(c)** Decide whether the visible band is aliased and what the
> thermal band's effective resolution is. **(d)** State which single additional
> measurement would most improve (a) and why.

A worked version of (a)–(c) appears in the lesson-03 and lesson-04
[exercises](exercises).

## Common pitfalls

1. **Reporting reflectance without an uncertainty.** The demonstration's
   atmospheric errors alone are worth $2\%$–$40\%$ depending on which term is
   mishandled.
2. **Treating brightness temperature as surface temperature.** With
   $\varepsilon = 0.86$ that is a $9.8\ \mathrm{K}$ error before any atmospheric
   term.
3. **Applying Kirchhoff's law as $\varepsilon = 1-\rho$ to a translucent
   surface.** The transmittance term is not optional.
4. **Subtracting path radiance and stopping.** Transmittance and illumination
   still carry their own errors, multiplicative and amplified by the air mass.
5. **Assuming correction noise averages away.** A noisy multiplicative
   correction is convex and biases a composite high.
6. **Reading a GSD as a resolution.** The aperture, not the detector, may be the
   limit; in this module's synthetic thermal band it is by a factor of $4.4$.
7. **Inverting a mixed pixel with one band.** The solution is a curve, not a
   point.

## Related modules

- [02-10 Optics and Photometry](../../02-physics/10-optics-and-photometry/README.md)
  — the radiative-transfer and diffraction physics this module applies.
- [16-02 Radiation and Energy Balance](../../16-atmosphere-climate/02-radiation-and-energy-balance/README.md)
  — the atmospheric radiative transfer in a climate context.
- [20-01 Signals and Systems](../../20-signal-processing/01-signals-and-systems/README.md)
  — sampling, aliasing and reconstruction.
- [17-02 Optical and Thermal Remote Sensing](../02-optical-and-thermal-remote-sensing/README.md)
  — the applications this physics supports.
- [18-inverse-problems](../../18-inverse-problems/README.md) — the general
  treatment of the retrievals built here.
