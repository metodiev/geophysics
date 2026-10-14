# Module 02-10 — Optics and Photometry for Geophysical Sensing

**Stages:** intermediate → graduate · **Prerequisites:**
[02-01-01 Physical Quantities, SI Units and Dimensional Homogeneity](../01-measurement-and-physical-reasoning/01-physical-quantities.md)
for the unit discipline,
[02-03-08 Reflection, Refraction and Snell's Law for Waves](../03-oscillations-and-waves/08-reflection-refraction.md)
and
[02-03-09 Diffraction, Scattering and Resolution Limits](../03-oscillations-and-waves/09-diffraction.md)
for the wave foundations, and
[02-07-05 Electromagnetic Waves, Impedance and Polarisation](../07-electromagnetism/05-em-waves.md)
for the field description of light.

This module covers the optics that geophysics actually uses. It is not a general
optics course: every topic is here because an instrument depends on it, and every
number is computed rather than quoted.

The two applications that organise the module are **remote sensing** and
**fibre-optic sensing**, and they ask opposite questions of the same physics:

| | Remote sensing | Fibre sensing |
|---|---|---|
| What is measured | Radiance arriving from a distance | Optical phase inside a waveguide |
| Governing law | Radiative transfer | Interference and the strain-optic effect |
| The interface that matters | The air–surface boundary (Snell, Fresnel) | The core–cladding boundary (total internal reflection) |
| What sets the limit | Diffraction and detector sampling | Coherence, backscatter and the gauge length |
| Typical product | Surface temperature, reflectance, mineralogy | Strain, ground motion, temperature along a cable |

Three features distinguish this module from a standard optics treatment:

- **Every approximation carries its regime.** Geometrical optics assumes
  $\lambda/a\ll1$ — and the module computes the case where it fails (a
  single-mode fibre core, §3.3 of lesson 01). The Fraunhofer approximation
  assumes far-field observation, the greybody approximation assumes a
  wavelength-independent emissivity, the single-scattering approximation assumes
  an optically thin path: each is stated where it is used, with the observation
  that would falsify it.
- **Every number is computed.** The demos in [`code/`](./code) use the standard
  library only. The Planck function is verified against the Stefan-Boltzmann
  integral numerically ($\int x^3/(e^x-1)\,\mathrm dx$ against $\pi^4/15$, to
  $1.4\times10^{-13}$) and Wien's constant is recovered by two independent
  methods (to $6\times10^{-11}$). The Airy pattern is obtained by integrating the
  aperture, and its first zero is compared with the textbook 3.8317. The lessons
  quote the demos' actual output, including the errors the methods make.
- **Values that vary are given as ranges.** Emissivity, albedo, reflectance and
  mineral feature positions depend on composition, grain size, roughness,
  moisture and viewing geometry. They appear here as nominal ranges with a
  pointer to a spectral library, never as single facts. Constants that are exact
  by definition — $c$, $h$, $k_B$ and the derived $\sigma$, and $b$ from Wien's
  law — are the only quantities quoted to all their digits.

The distinction that causes more errors than any other in this subject is between
**resolution** and **sensitivity**. A wider aperture improves resolution and does
nothing for sensitivity; a longer integration improves sensitivity and does
nothing for resolution; a wider spectral band improves sensitivity and destroys
the narrow features that carry the compositional information. Lesson
[02](./02-interference-diffraction-optics.md) §3.1 makes the resolution trade
quantitative, lesson [04](./04-spectroscopy.md) §4 makes the spectral trade
quantitative, and the module's exercises test the confusion deliberately.

## Learning objectives

By the end of this module you will be able to:

1. Derive Snell's law from Fermat's principle, compute critical angles and
   Fresnel reflectances, and explain total internal reflection as a failure of
   phase matching. (Lesson 01)
2. Compute the numerical aperture, V number, mode count and single-mode cutoff of
   a step-index fibre, and explain why phase-based sensing requires single mode.
   (Lessons 01 and 05)
3. Apply the thin-lens equation to an instrument, compute the plate scale and the
   focus travel, and explain why a window in an optical train is never optically
   neutral. (Lesson 01)
4. Derive the two-slit fringe spacing and the Fraunhofer diffraction integral,
   obtain the Airy pattern from the circular aperture, and verify its zeros
   numerically. (Lesson 02)
5. Compute the resolution limit $1.2197\lambda/D$ for an aperture, convert it
   into a ground sample distance, and decide whether an instrument is
   diffraction-limited or pixel-limited. (Lesson 02)
6. Compute the reflectance of a thin-film coating, and the resolving power of a
   diffraction grating and of a Fabry–Perot etalon. (Lesson 02)
7. Write and manipulate the Planck function in both its wavelength and frequency
   forms, and verify the Stefan–Boltzmann and Wien laws numerically. (Lesson 03)
8. Derive the radiative transfer equation, solve it for a layer over a surface,
   and compute a brightness temperature with its inverse. (Lesson 03)
9. State Kirchhoff's law, convert between reflectance and emissivity, and
   quantify the error introduced by an emissivity assumption. (Lessons 03
   and 04)
10. Compute the band-integrated fraction of a blackbody spectrum and explain the
    role of the 8–14 µm atmospheric window. (Lesson 03)
11. Explain which photon–matter interactions fall in which wavelength region, and
    why mineral identification from reflectance works. (Lesson 04)
12. Measure a band depth and band centre with continuum removal, and quantify the
    depth loss and position error caused by finite resolution and by coarse
    sampling. (Lesson 04)
13. Compute the Rayleigh scattering loss and its $\lambda^{-4}$ scaling,
    the backscatter level and the spatial and temporal resolution limits of a
    distributed measurement. (Lesson 05)
14. Derive the phase-to-strain relation of a single-mode fibre, compute the phase
    produced by a given strain, and convert ground motion into strain.
    (Lesson 05)
15. Compute a gauge-length transfer function and the temperature
    cross-sensitivity in microstrain equivalent. (Lesson 05)

## Lessons

| # | Lesson | Level | Key idea |
|---|---|---|---|
| 01 | [Geometrical Optics, Refraction and Lenses](./01-geometrical-optics.md) | intermediate | Snell's law, the critical angle and the thin lens; total internal reflection is how a fibre works |
| 02 | [Interference and Diffraction in Optical Instruments](./02-interference-diffraction-optics.md) | advanced | **The resolution lesson**: $\theta_{\min}=1.2197\lambda/D$, the Airy pattern, and what sets the limit of any optical instrument |
| 03 | [Radiative Transfer, Blackbody Radiation and Kirchhoff's Law](./03-radiative-transfer.md) | graduate | Planck, $\sigma T^4$, Wien, and the transfer equation behind every satellite radiometer |
| 04 | [Spectroscopy Principles for Remote Sensing](./04-spectroscopy.md) | graduate | Absorption features, spectral resolution, and why mineral identification from reflectance works |
| 05 | [Fibre-Optic Sensing and Distributed Acoustic Sensing](./05-fiber-optics-sensing.md) | graduate | Rayleigh scattering, optical phase, and how strain becomes a measurable phase shift |

## Suggested path

**If you are working through the physics folder in order:** lessons 01–05 in
numeric order. Lesson 01 establishes the ray picture, lesson 02 replaces it with
waves and derives the resolution limit, lesson 03 moves to the radiometric
quantities that an instrument actually measures, and lessons 04 and 05 apply all
of it to the two sensing modalities.

**If you are here for remote sensing:** read [01](./01-geometrical-optics.md)
§2–§4 (the interface, the window and the lens), [02](./02-interference-diffraction-optics.md)
§3 in full (resolution, GSD and the pixel limit),
[03](./03-radiative-transfer.md) in full (radiance, Planck, brightness
temperature), then [04](./04-spectroscopy.md) §1–§4 and §7. Finish with
[17 Remote Sensing and GIS](../../17-remote-sensing-gis/README.md) and the
[Open Data: Remote Sensing and Earth Observation](../../26-reference-library/05-open-datasets-catalogue/04-datasets-remote-sensing.md)
catalogue.

**If you are here for fibre sensing or DAS:** read [01](./01-geometrical-optics.md)
§3 (total internal reflection, numerical aperture and V) in full, then
[05](./05-fiber-optics-sensing.md) in full, then
[02](./02-interference-diffraction-optics.md) §1.2 (coherence, which sets the
laser specification). Follow with
[06 Seismology](../../06-seismology/README.md) for the wavefields DAS records and
[15 Oceanography and Marine Geophysics](../../15-oceanography-marine/README.md)
for submarine-cable seismology.

**If you already have an optics background:** attempt ★★★9 of
[01](./exercises/01-geometrical-optics-solutions.md), ★★★9 and ★★★10 of
[02](./exercises/02-interference-diffraction-optics-solutions.md), ★★★9 and
★★★10 of [03](./exercises/03-radiative-transfer-solutions.md), ★★★10 of
[04](./exercises/04-spectroscopy-solutions.md) and ★★★9–11 of
[05](./exercises/05-fiber-optics-sensing-solutions.md) first. If those close
cleanly, use lessons 01–03 as reference and work lesson 05 in full — it is the
one whose details are least likely to be familiar.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-geometrical-optics.md`](./01-geometrical-optics.md) … [`05-fiber-optics-sensing.md`](./05-fiber-optics-sensing.md) | The five lessons |
| [`exercises/01-geometrical-optics-exercises.md`](./exercises/01-geometrical-optics-exercises.md) | Snell's law, the critical angle, the lens and the fibre design |
| [`exercises/02-interference-diffraction-optics-exercises.md`](./exercises/02-interference-diffraction-optics-exercises.md) | Interference, the Airy integral, resolution and coatings |
| [`exercises/03-radiative-transfer-exercises.md`](./exercises/03-radiative-transfer-exercises.md) | Planck, Wien, the transfer equation and brightness temperature |
| [`exercises/04-spectroscopy-exercises.md`](./exercises/04-spectroscopy-exercises.md) | Band depths, resolution and sampling, and the continuum problem |
| [`exercises/05-fiber-optics-sensing-exercises.md`](./exercises/05-fiber-optics-sensing-exercises.md) | Loss budgets, gauge response, aliasing and cross-sensitivity |
| [`code/geometrical_optics_demo.py`](./code/geometrical_optics_demo.py) | Snell and Fresnel tables, critical angles, fibre parameters, lens solutions |
| [`code/interference_diffraction_demo.py`](./code/interference_diffraction_demo.py) | Aperture quadrature, the Airy zeros, resolution limits, coatings, coherence |
| [`code/radiative_transfer_demo.py`](./code/radiative_transfer_demo.py) | The numerical Planck verification, band fractions, the transfer solution |
| [`code/spectroscopy_demo.py`](./code/spectroscopy_demo.py) | Band metrics, resolution and sampling losses, derivative spectroscopy |
| [`code/fibre_optics_sensing_demo.py`](./code/fibre_optics_sensing_demo.py) | Loss and backscatter budgets, phase-to-strain, gauge response, thermal terms |

Every script uses only the Python standard library, so they run in any Python 3
installation with no packages. Run them; do not read them.

## Mastery checkpoint

Complete this without notes, with a calculator and no code.

> A 5 km single-mode fibre is deployed in a borehole at 1550 nm
> ($n = 1.4504$, $n_g = 1.4682$, attenuation 0.20 dB km⁻¹). The rock has a wave
> speed of 3000 m s⁻¹; the interrogator uses 20 ns pulses and a 10 m gauge,
> and channels are spaced 1 m apart.
>
> **(a)** Compute the round-trip loss and the fraction of launched power returned
> by the attenuation alone.
> **(b)** Compute the spatial resolution and the maximum pulse repetition
> frequency.
> **(c)** Compute the optical phase produced by a strain of 50 nε over one gauge
> length, and the strain that a 0.1 K temperature change mimics.
> **(d)** Compute the gauge transfer function's first null and its 3 dB frequency,
> and state what happens to a 300 Hz signal.
> **(e)** Compute the number of channels and the spatial Nyquist frequency.
> **(f)** The cable is a loose tube, so the fibre is mechanically decoupled from
> the rock. A 2 K daily temperature swing appears in the record. Compute the
> apparent strain and state what it would be mistaken for.

**Worked answer for (b), (c) and (f):**

Propagation speed
$v = c/n_g = 2.997\,92\times10^8/1.4682 = 2.0419\times10^8$ m s⁻¹.

**(b)** $\Delta z = vW/2 = 2.0419\times10^8\times20\times10^{-9}/2
= 2.042$ m, so a 10 m gauge is five times the pulse resolution: the gauge, not
the pulse, sets the spatial resolution of this configuration.
$f_{\text{prf}} = v/(2L) = 2.0419\times10^8/(2\times5000) = 20\,419$ Hz, so the
record is Nyquist-limited to 10 210 Hz — far above the seismic band.

**(c)** With $\Delta\phi/L = 2\pi n\xi/\lambda = 4.6208\times10^6$ rad m⁻¹ per
unit strain and $\xi = 0.7859$,

$$\Delta\phi = 4.6208\times10^6\times10\times50\times10^{-9}
= 2.31\ \mathrm{rad} ,$$

i.e. $132°$ — a large phase signal, easily measured. A 0.1 K temperature change
produces $47.82\times10\times0.1 = 47.8$ rad over the same gauge, which is twenty
times larger than the 50 nε signal: **the temperature sensitivity of a
phase-based measurement is the dominant systematic, not a correction.**

**(f)** $\Delta T = 2$ K is equivalent to $2\times10.35 = 20.7$ µε — of the same
order as the strain from a moderate nearby earthquake, and two to four orders of
magnitude larger than the microseismic signals a borehole array is usually
deployed to detect. In a loose-tube cable the temperature response appears as
apparent strain with a strong diurnal periodicity and coherence across channels;
unremoved, it would be mistaken for a very large, very slow seismic signal. The
mitigation is a co-located temperature measurement (DTS on the same fibre, which
is a standard companion measurement) or a strain-free reference fibre in the same
cable.

## Common pitfalls across this module

1. **Quoting a refractive index without its wavelength and temperature.** 1.52 is
   meaningless; fused silica is 1.458 at 589 nm and 1.4447 at 1550 nm.
2. **Confusing resolution with sensitivity.** Aperture sets resolution; exposure,
   band width and noise set sensitivity. One does not buy the other.
3. **Using 1.22 instead of 1.2197.** Small, systematic and harmless in an
   estimate, damaging in a calibration.
4. **Assuming a satellite's ground sample distance is its diffraction limit.**
   Usually the pixel is coarser by a factor of several, and the aperture has
   resolution in reserve.
5. **Using degrees in a radian formula.** $\sin\theta$, $e^{i\theta}$ and every
   small-angle approximation in this module are radian statements.
6. **Quoting an emissivity as a single fact.** Emissivity varies with
   wavelength, mineralogy, grain size, roughness and moisture; give a range and
   a source, and never present a nominal value as a measurement.
7. **Forgetting the Jacobian between $B_\lambda$ and $B_\nu$.** The two peak at
   different places and $c/\lambda$ is not the conversion.
8. **Inverting the Planck function incorrectly.** $T_B$ requires
   $\ln(1+c_1/(\lambda^5I))$; the reciprocal form returns $10^5$ K and still
   looks plausible on a plot.
9. **Treating a band depth as proportional to abundance.** It is proportional
   only for weak bands; the response has already lost 26 per cent of its
   linearity by $\tau = 0.6$.
10. **Confusing spectral resolution with spectral sampling.** Many bands is not
    the same as narrow bands, and narrow bands correctly spaced is not the same
    as well-sampled. All three must be specified.
11. **Assuming a feature position is a mineral constant.** Cation substitution,
    grain size and the host assemblage move it; give a range with a source.
12. **Mixing decibels and nepers.** The factor is 8.686 and the error is silent.
13. **Forgetting the factor 2 in a round-trip measurement.** Both the loss and the
    spatial resolution of a backscatter-based system carry it.
14. **Reporting a DAS amplitude without the gauge and the installation.** The
    gauge is a spatial filter and the cable coupling is part of the instrument
    response; neither is a constant.
15. **Ignoring thermal cross-sensitivity in fibre strain measurements.** 1 K is
    equivalent to about 10 µε, which is larger than most seismic strains.

## Related folders

- [02-physics/03 Oscillations and Waves](../03-oscillations-and-waves/README.md)
  — the wave foundations: refraction, diffraction, attenuation and the
  Fresnel-zone geometry.
- [02-physics/05 Thermodynamics](../05-thermodynamics/README.md) — the $T^4$ flux
  and the radiative heat-transfer coefficient, from the heat-transfer side.
- [02-physics/07 Electromagnetism](../07-electromagnetism/README.md) — the field
  description of light, the wave/diffusion dichotomy, and the impedance view of
  reflection.
- [17 Remote Sensing and GIS](../../17-remote-sensing-gis/README.md) — where
  these optics become an observing system.
- [16 Atmosphere and Climate](../../16-atmosphere-climate/README.md) — radiative
  transfer in the atmosphere, the greenhouse effect and the planetary energy
  balance.
- [06 Seismology](../../06-seismology/README.md) — the wavefields that DAS
  records and the instruments it replaces.
- [26 Reference Library](../../26-reference-library/README.md) — the constants
  handbook and the open-data catalogues used throughout this module.
