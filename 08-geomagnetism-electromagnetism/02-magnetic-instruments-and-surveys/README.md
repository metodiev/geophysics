# Module 08-02 — Magnetic Instruments and Surveys

**Stages:** advanced → graduate · **Prerequisites:** modules 02-07 and 02-09;
[08-01](../01-earth-magnetic-field/README.md).

This module is about the gap between a field that exists and a number in a
database. Six lessons take the reader from the physics of a single sensor to the
error budget of a finished survey, and the organising question is always the same:
**what is actually being measured, and what has to be subtracted before the answer
means anything?** A fluxgate measures components and therefore needs a frame; a
proton or alkali sensor measures a scalar and therefore cannot separate the
anomaly from the diurnal variation; a gradiometer cancels what is common and
attenuates what is broad; an aircraft adds its own field to everything it flies
over; and a survey grid inherits a level error from every step of the chain.

Two themes recur. The first is that **sensitivity is not resolution, and
resolution is not accuracy**: a magnetometer that resolves a picotesla reads
0.1 nT differently depending on its heading, and a survey's accuracy is set by its
levelling and its base station rather than by its sensor. The second is that
**every subtraction has a signature**: an epoch error is an offset and is absorbed
by levelling, a timing lag is a ramp and is not, a line-spacing error folds an
anomaly to a longer apparent wavelength and leaves no trace of its absence.

All models and data in this module are **SYNTHETIC**. No instrument, aircraft,
survey, manufacturer or published specification is described. The standard values
used are exact constants: $\mu_0$, the proton gyromagnetic ratio, the Bohr
magneton, the Planck constant, the electron spin $g$-factor, the
electron/proton mass ratio, the caesium hyperfine frequency that defines the SI
second, the mean Earth radius $6371\ \mathrm{km}$ and the $11.5^{\circ}$ dipole
tilt.

## Learning objectives

By the end of this module you will be able to:

1. **Derive** the sense-coil EMF of a fluxgate, explain its harmonic structure,
   and compute its sensitivity, linearity range and cross-axis error.
2. **State** the Larmor relation for a proton and for an alkali atom, compute the
   frequency and sensitivity for each, and derive the Landé factor from the
   quantum numbers.
3. **Quantify** how the precision of a scalar reading depends on
   signal-to-noise ratio and counting time, and explain why the latter saturates.
4. **Compute** the noise rejection of a gradiometer from the sensors' correlation,
   the gradient tensor's properties, and the wavelength response of a difference.
5. **Construct** the Tolles–Lawson interference model, compensate a manoeuvre by
   least squares, and choose the model order against a stated noise floor.
6. **Compute** the loss of anomaly amplitude with flying height and with line
   spacing, and state the quarter-wavelength design rule.
7. **Build** a diurnal correction, a main-field removal and a tie-line levelling
   adjustment, and quantify the residual of each.
8. **Assemble** an error budget in quadrature and use it to decide where to
   improve a survey.

## Prerequisites

- [08-01 The Earth's Magnetic Field](../01-earth-magnetic-field/README.md) —
  the elements, the models and the secular variation that instruments measure.
- [02-07-04 Faraday's Law, Induction and Eddy Currents](../../02-physics/07-electromagnetism/04-em-induction.md)
  — the basis of every induction-based sensor.
- [02-09-01 Atomic Structure and Energy Levels](../../02-physics/09-radiation-and-atomic-physics/01-atomic-structure.md)
  — hyperfine structure, for the alkali sensors.
- [20-05-01 Stochastic Processes, Stationarity and Ergodicity](../../20-signal-processing/05-noise-and-random-signals/01-stochastic-processes.md)
  — the noise model used throughout.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Fluxgate Magnetometers: Principle and Use](01-fluxgate-magnetometers.md) | advanced | Faraday induction in a saturating core: the second harmonic is the measurement, and misalignment is a first-order error |
| 02 | [Proton Precession and Overhauser Magnetometers](02-proton-overhauser.md) | advanced | Frequency is the measurement: 42.6 mHz per nT, and precision scales with SNR until the signal decays away |
| 03 | [Optically Pumped Cesium and Potassium Magnetometers](03-cesium-optically-pumped.md) | graduate | The stretched state is exactly linear; heading error is second order; the dead zone is a cone |
| 04 | [Gradiometers, Arrays and Noise Rejection](04-gradiometers-arrays.md) | advanced | A difference cancels the common signal and attenuates the broad one: both are computable |
| 05 | [Airborne Magnetic Surveys and Compensation](05-airborne-magnetic-surveys.md) | graduate | 18 coefficients describe the aircraft; height and line spacing are computed losses, not rules of thumb |
| 06 | [Magnetic Survey Design, Diurnal Correction and Levelling](06-magnetic-survey-procedures.md) | advanced | Every subtraction has a signature; the error budget says where to spend |

## Suggested path

**If you are new to instruments:** lessons 01, 02 and 06 in order, running each
demonstration. Lesson 06 is where the readings become a survey.

**If you come from physics or optics:** start at 03, which derives the alkali
frequency from the quantum numbers, then 02 for the contrast, then 05 for what
happens when the sensor is required to fly.

**If you are designing a survey:** 04, 05 and 06, plus the ★★★ exercises — each
one ends with a specification you should be able to write.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-fluxgate-magnetometers.md`](01-fluxgate-magnetometers.md) | Lesson 01 |
| [`02-proton-overhauser.md`](02-proton-overhauser.md) | Lesson 02 |
| [`03-cesium-optically-pumped.md`](03-cesium-optically-pumped.md) | Lesson 03 |
| [`04-gradiometers-arrays.md`](04-gradiometers-arrays.md) | Lesson 04 |
| [`05-airborne-magnetic-surveys.md`](05-airborne-magnetic-surveys.md) | Lesson 05 |
| [`06-magnetic-survey-procedures.md`](06-magnetic-survey-procedures.md) | Lesson 06 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Six runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib,
pandas and SymPy:

```bash
cd 08-geomagnetism-electromagnetism/02-magnetic-instruments-and-surveys/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python fluxgate_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python proton_precession_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python cesium_optically_pumped_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gradiometers_arrays_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python airborne_magnetic_surveys_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python magnetic_survey_procedures_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), uses no plotting and exits 0. They require no
network access.

## Mastery checkpoint

Complete this without notes:

> A scalar magnetometer with a $0.1\ \mathrm{nT}$ reading noise is read once per
> second along lines spaced $100\ \mathrm{m}$ apart at a flying height of $60\
> \mathrm{m}$, with a base station 8 km away whose clock is 10 s late.
> **(a)** Compute the frequency sensitivity of a proton sensor and of a caesium
> sensor in $\mathrm{Hz\,nT^{-1}}$. **(b)** Compute the anomaly of a
> $3000\ \mathrm{A\,m^{2}}$ dipole at $30\ \mathrm{m}$ depth as measured at the
> flying height, and state whether a $100\ \mathrm{m}$ line spacing is adequate
> for it. **(c)** Compute the diurnal residual left by the 10 s clock error for a
> $20\ \mathrm{nT}$ daily wave. **(d)** Name the two largest terms you would
> expect in the error budget and say which one you would fix first.

A worked version of (a)–(c) appears in the lesson-02 and lesson-06
[solutions](exercises/02-proton-overhauser-solutions.md).

## Common pitfalls across this module

1. **Quoting a sensitivity without a noise floor**, or a resolution without an
   accuracy.
2. **Confusing $\mathrm{Hz\,T^{-1}}$ with $\mathrm{Hz\,nT^{-1}}$**, a factor of
   $10^{9}$ in every scalar-sensor calculation.
3. **Assuming a gradiometer is quieter.** At zero correlation it is noisier by
   $\sqrt{2}$.
4. **Keeping a large compensation model because it fits.** Compare with the noise
   floor instead.
5. **Designing at Nyquist spacing.** It is the aliasing threshold, not a target.
6. **Correcting for the diurnal variation with an un-synchronised base station.**
   The residual scales linearly with the lag.
7. **Reporting levelled data without the residual misfit.**

## Related modules

- [08-01 The Earth's Magnetic Field](../01-earth-magnetic-field/README.md) —
  what these instruments measure.
- [08-03 Magnetic Anomalies and Modelling](../03-magnetic-anomalies-and-modelling/README.md) —
  what the reduced data are interpreted with.
- [05-05 Survey Design and Acquisition](../../05-core-geophysics/05-survey-design-and-acquisition/README.md) —
  the general framework for sampling, geometry and QC.
- [07-02 Gravity Instruments and Surveys](../../07-gravity-geodesy/02-gravity-instruments-and-surveys/README.md) —
  the parallel instrument chain for a different potential field.
- [09-07 EM Data Processing, QC and Uncertainty](../../09-electrical-em-methods/07-em-data-processing-and-qc/README.md) —
  the same processing logic for electromagnetic data.
