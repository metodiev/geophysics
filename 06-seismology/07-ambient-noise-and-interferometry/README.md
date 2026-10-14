# Module 06-07 — Ambient Noise and Seismic Interferometry

**Stages:** advanced → research · **Prerequisites:** modules 06-01 and 06-02;
basic signal processing.

This module turns the ground motion that exists *between* earthquakes into an
image. The method is interferometry: cross-correlate the noise recorded at two
stations and the result looks like the response of the Earth to a source at one
of them. The idea is powerful and the arithmetic is short, which is exactly why
it is so easy to misuse.

The module is built around one honest difficulty: **the retrieved function is a
property of the noise sources as much as of the Earth.** A station pair in an
isotropic noise field retrieves a symmetric Green's function; the same pair under
a one-sided storm track retrieves one branch and an artefact, and no amount of
processing distinguishes the two from a single measurement. Every lesson states
which of the two it is measuring: the source field (lessons 01-02), the
structure (lessons 03-04), or a change in the structure through a source field
that is assumed stationary (lesson 05).

The second recurring theme is the uncertainty budget. Each method here has a
precision that improves predictably with recording time (measured exponents near
$-0.5$ for noise and error floors) and a bias that does not improve at all — a
stretching approximation, a finite source ring, a damping choice, a null space.
The lessons measure both, and they report the bias as a number.

All models and data in this module are **SYNTHETIC**. No real station, event or
waveform is used, and no number is quoted from a published measurement.

## Learning objectives

By the end of this module you will be able to:

1. Derive the double-frequency relation between ocean swell and the secondary
   microseism, and measure the microseism bands in a synthetic spectrum.
2. Derive the coherence $C(f)=S(f)J_0(kd)$ of a diffuse 2-D field, evaluate it,
   and quantify how a directional source sector makes it complex.
3. Derive the Green's-function retrieval by stationary phase, measure the
   retrieved arrival against $d/c$, and decompose the timing error into its
   causes.
4. Fit the emergence of a retrieval with stack length and interpret the measured
   exponent against the $\sqrt{N}$ law.
5. Derive the Love-wave dispersion relation, solve it numerically, and measure
   phase and group velocity from a retrieved correlation — including the
   frequency grid that avoids a $2\pi$ ambiguity.
6. Invert path-averaged dispersion for a 2-D map, report the damping trade-off,
   the resolution matrix and the cells in the null space of the geometry.
7. Derive the zero-offset reflection response from an autocorrelation, and
   measure the resolution limit and the tuning curve of a thin bed.
8. Measure a velocity change by coda stretching, report its precision and its
   window dependence, and name the four ways the number can be wrong.

## Prerequisites

- [06-01 Elastic Wave Propagation](../01-elastic-wave-propagation/README.md) —
  surface waves, dispersion, body-wave reflection and conversion.
- [06-02 Ray Theory and Travel Times](../02-ray-theory-and-travel-times/README.md) —
  travel times, slowness and layered media.
- [03-03-05 scipy.signal: Filters, Windows and Spectral Estimation](../../03-scientific-computing/03-scipy/05-signal.md) —
  the estimators used in every demonstration.

## Lesson map

| # | Lesson | Level | Central point |
|---|---|---|---|
| 01 | [Sources of Ambient Seismic Noise](01-noise-sources.md) | advanced | The microseism bands come from the nonlinear wave interaction; the diffuse-field coherence is $J_0(kd)$ and a one-sided source makes it complex |
| 02 | [Retrieving the Green's Function by Cross-Correlation](02-cross-correlation-green.md) | doctoral | Stationary phase gives the retrieval; its timing error is $0.75\ \mathrm{s}$ here, and its noise floor falls as $N^{-0.47}$ |
| 03 | [Ambient-Noise Tomography and Monitoring](03-noise-tomography.md) | doctoral | Solve the Love dispersion relation, measure $c(T)$ and $U(T)$, then invert for a map whose null space is a property of the path geometry |
| 04 | [Autocorrelation and Body-Wave Microseismics](04-autocorrelation.md) | doctoral | A single station retrieves the zero-offset reflectivity — with a unit arrival at zero lag, a resolution limit, and multiples that bias amplitudes by $14$-$26\%$ |
| 05 | [Monitoring Velocity Changes with Coda-Wave Interferometry](05-velocity-change-monitoring.md) | research | $\delta v/v$ is precise ($\approx19\ \mathrm{ppm}$ in the $4$-$8\ \mathrm{Hz}$ band) and ambiguous: the same data give $+1546$ or $-23\ \mathrm{ppm}$ depending on the window |

## Suggested path

**If you are new to ambient noise:** lessons 01 and 02 in order, running each
demonstration. Lesson 02 is where the retrieval first appears and where its
biases are quantified.

**If you already know interferometry:** read 01 §5-§6 (the Bessel result and the
directional bias), then 03 and 05 — the two applications, tomography and
monitoring.

**If you are preparing a research project:** 02 §5 and §7 (directional bias and
equipartition), 03 §6 (resolution and null space), 04 §5 (multiple
contamination) and 05 §7 (the four error channels), plus the exercises at ★★★
level.

## Materials in this module

| Path | Contents |
|---|---|
| [`01-noise-sources.md`](01-noise-sources.md) | Lesson 01 |
| [`02-cross-correlation-green.md`](02-cross-correlation-green.md) | Lesson 02 |
| [`03-noise-tomography.md`](03-noise-tomography.md) | Lesson 03 |
| [`04-autocorrelation.md`](04-autocorrelation.md) | Lesson 04 |
| [`05-velocity-change-monitoring.md`](05-velocity-change-monitoring.md) | Lesson 05 |
| [`exercises/`](exercises) | Graded exercises and worked solutions for every lesson |
| [`code/`](code) | Five runnable demonstrations |

## How to run the demos

Use the project virtual environment, which provides NumPy, SciPy, Matplotlib and
ObsPy:

```bash
cd 06-seismology/07-ambient-noise-and-interferometry/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python noise_sources_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python cross_correlation_green_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python noise_tomography_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python autocorrelation_demo.py
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python velocity_change_monitoring_demo.py
```

Every demo prints labelled results with units, uses a fixed random seed
(`np.random.default_rng(20261014)`), runs in under two seconds and exits 0. They
require no network access.

## Mastery checkpoint

Complete this without notes:

> A station pair separated by $d = 60\ \mathrm{km}$ in a medium with
> $c = 3.20\ \mathrm{km\,s^{-1}}$ records three months of noise.
> **(a)** State where the two arrivals of the retrieved correlation must appear,
> and compute the Bessel argument $kd$ at $T = 7\ \mathrm{s}$.
> **(b)** The causal branch is $11$ times the acausal one. Give the physical
> interpretation and the test that would confirm it.
> **(c)** The retrieval's noise floor falls by a factor of $8.7$ when the stack
> grows from $1$ to $64$ segments: what exponent is that, and what does the
> theory predict?
> **(d)** The measured phase velocity at $T = 10\ \mathrm{s}$ is
> $2.06\ \mathrm{km\,s^{-1}}$; compute the group velocity given
> $dc/dT = 0.0121\ \mathrm{km\,s^{-1}\,s^{-1}}$.
> **(e)** A $\delta v/v$ of $+2000\ \mathrm{ppm}$ is imposed only above $8\
> \mathrm{km}$ depth. State qualitatively what the early and late lapse-time
> windows will report.

A worked version of (a)-(d) appears in the lesson solutions:
[01](exercises/01-noise-sources-solutions.md),
[02](exercises/02-cross-correlation-green-solutions.md),
[03](exercises/03-noise-tomography-solutions.md),
[05](exercises/05-velocity-change-monitoring-solutions.md).

## Common pitfalls across this module

1. **Assuming an isotropic source field.** It is the hypothesis of the
   mathematics, not a property of the Earth; report the causal/acausal ratio
   with every retrieval.
2. **Reading a phase velocity from an envelope.** The envelope measures the
   group velocity; at 30 s in lesson 03's model the two differ by $34\%$.
3. **Publishing a map without its null space.** Four cells in the demonstrated
   grid are crossed by no path and have a resolution diagonal of exactly zero.
4. **Quoting $\delta v/v$ without its window.** The same synthetic data give
   $+1546$ or $-23\ \mathrm{ppm}$ depending on the lapse-time window.
5. **Confusing precision with accuracy.** The demonstrated retrieval is precise
   to $9.5\ \mathrm{SNR}$ and biased by $4\%$ in velocity at the same time.

## Related modules

- [06-06 Seismic Tomography](../06-seismic-tomography/README.md) — the general
  theory of path-based inversion and resolution.
- [06-08 Receiver Functions and Crustal Structure](../08-receiver-functions-and-crustal-structure/README.md) —
  the single-station method that uses conversions instead of correlations.
- [06-09 Reflection Seismology](../09-reflection-seismology/README.md) — the
  same reflectivity with a controlled source.
- [18-inverse-problems](../../18-inverse-problems/README.md) — regularisation,
  null space and uncertainty quantification.
- [20-signal-processing](../../20-signal-processing/README.md) — correlation,
  spectral estimation and deconvolution in full.
