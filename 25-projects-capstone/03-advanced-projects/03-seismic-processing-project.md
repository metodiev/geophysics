---
id: 25-03-03
title: "Project: Seismic Reflection Processing Flow"
level: advanced
prereqs: ["25-02-01", "06-09-01", "20-02-02", "05-06-02"]
estimated_minutes: 180
tags: [projects, seismology, reflection, nmo, stacking, semblance, teaching]
---

# Project: Seismic Reflection Processing Flow

## Learning objectives

By the end of this project you will be able to:

1. **Build** a CMP gather from a convolutional model and **state** every
   parameter that enters it.
2. **Derive** the normal-moveout equation and **measure** the residual moveout a
   velocity error leaves at the far offset, in milliseconds and in fractions of a
   wavelet period.
3. **Perform** a semblance velocity analysis and **report** the picked velocity
   with the width of its half-maximum band as its resolution.
4. **Compute** the NMO stretch as a function of offset and **apply** a mute,
   stating the threshold and how many traces it removes.
5. **Measure** the signal-to-noise gain of a stack and **compare** it with the
   $\sqrt{N}$ prediction, explaining any excess.
6. **State** which processing steps preserve amplitude and which do not, and
   **name** the quantity each step biases.
7. **Report** a processing flow as an ordered list of steps, each with its
   parameter, its purpose and the artefact it introduces.

All data in this project are **SYNTHETIC**: a two-primary CMP gather generated
by [`code/seismic_processing_demo.py`](./code/seismic_processing_demo.py) from a
convolutional model with a Ricker wavelet and Gaussian noise. No field shot
gather, no processing-software output and no published section is used.

## Prerequisites

- [25-02-01 Project: Travel-Time Curves and 1-D Velocity Structure](../02-intermediate-projects/01-travel-time-curves.md) —
  the moveout hyperbola this project corrects, at reflection rather than
  refraction geometry.
- [06-09-01 Acoustic Impedance, Reflection Coefficients and the Convolution Model](../../06-seismology/09-reflection-seismology/01-reflection-principle.md) —
  why a trace is a convolution of a wavelet with a reflectivity series.
- [20-02-02 Spectral Estimation: Periodogram, Welch, Multitaper](../../20-signal-processing/02-fourier-and-spectral-analysis/02-spectral-estimation.md) —
  the semblance statistic as a normalised energy measure.
- [05-06-02 Noise Suppression: Stacking, Filtering, Median, KL Transform](../../05-core-geophysics/06-data-processing-principles/02-noise-suppression.md) —
  the stacking gain and its assumptions.

## 1. The question

*How do you turn a CMP gather into a stacked section, and what does each step
cost?*

No single step in a reflection processing flow is hard; the difficulty is that
each one is a *commitment* that can only be judged after the next one. Velocity
analysis needs a mute, the mute needs the velocity, the stack needs both, and the
only feedback is whether the stacked wavelet is coherent. This project makes the
loop measurable: the semblance peak is compared with the true velocity, the
residual moveout from a $5\%$ velocity error is expressed in fractions of a
wavelet period, the mute is quantified as a stretch fraction, and the stack gain
is compared with $\sqrt{N}$.

## 2. The data

**Synthetic CMP gather (SYNTHETIC).** Two primaries at $t_0 = 1.000$ and
$2.000\ \mathrm{s}$ with stacking velocities $2500$ and
$3200\ \mathrm{m\,s^{-1}}$ and amplitudes 1.0 and 0.6, a $30\ \mathrm{Hz}$ Ricker
wavelet, 81 traces at offsets 0–2000 m with $\Delta t = 2\ \mathrm{ms}$ over 3 s,
and Gaussian noise with rms $0.08$ relative to the first primary.

**Provenance.** SYNTHETIC. The model is a convolutional idealisation: no
multiples, no attenuation, no anisotropy, no 3-D dip, and one wavelet for both
reflectors. Those omissions are the assumptions of §9, not accidental features.

## 3. The project specification

**Steps.**

1. State the model: $t_0$, $v_\text{rms}$, amplitudes, wavelet frequency, offsets,
   sample interval and noise level.
2. Compute $t(x) = \sqrt{t_0^{2} + (x/v_\text{rms})^{2}}$ for each primary and
   tabulate it at 1000 and 2000 m; record the NMO stretch
   $1 - t_0/t(x)$.
3. Run a semblance scan in velocity at each $t_0$, report the peak, and report
   the width of the half-maximum band as the pick's resolution.
4. Apply NMO with the correct velocity and with a $+5\%$ error; report the
   residual moveout at the far offset in milliseconds and in wavelet periods, and
   the amplitude remaining at $t_0$ on the far trace.
5. Compute the stretch curve, choose a mute threshold, and report how many traces
   the mute removes and from which offset.
6. Stack the corrected gather and measure the noise reduction in a quiet window;
   compare with $\sqrt{N}$ and account for any difference.
7. Write the flow: an ordered list of steps with parameters, purpose and artefact.

**Deliverable.** The gather parameters, the velocity picks with their resolution,
the residual-moveout table, the mute specification, the stacking-gain
measurement, and the annotated flow.

**Success criterion.** Every processing parameter is stated with its value and its
purpose; every artefact is quantified; the stack gain is compared with the
theoretical value and the difference is explained rather than ignored.

## 4. Moveout, NMO and residual moveout

For a single horizontal reflector, the reflection time at offset $x$ is

$$t(x) = \sqrt{t_0^{2} + \frac{x^{2}}{v_\text{rms}^{2}}},$$

and NMO correction maps each sample at $t(x)$ onto $t_0$ by evaluating the trace
at the shifted time. For the demonstration's first primary,

$$t(1000) = \sqrt{1 + 0.16} = 1.0770\ \mathrm{s},
\qquad
t(2000) = \sqrt{1 + 0.64} = 1.2806\ \mathrm{s}.$$

Applying NMO with a velocity that is $5\%$ too high ($2625\ \mathrm{m\,s^{-1}}$)
leaves a **residual moveout**

$$\Delta t = t(x; v_*) - t(x; v) = 1.2572 - 1.2806 = -23.45\ \mathrm{ms}
= 0.70\ \text{of a } 33\ \mathrm{ms}\ \text{wavelet period},$$

and the far trace's amplitude at $t_0$ collapses from $+1.0071$ to $-0.1338$: the
event has been smeared to a fraction of its amplitude and has changed sign,
because the mis-registration is close to half a wavelet period. This is the
quantitative justification of the usual working tolerance: **a velocity error of
a few percent is visible at the far offset**, and the far offset is where velocity
analysis must be accurate.

## 5. Velocity analysis and its resolution

Semblance along a trial hyperbola is

$$S(t_0, v) = \frac{\displaystyle\sum_{j}\Big(\sum_{i} a_{ij}\Big)^{2}}
{\displaystyle N\sum_{j}\sum_{i} a_{ij}^{2}},$$

with $i$ indexing traces and $j$ the samples in a short time window along the
trial curve. It is the energy of the stack divided by the total energy — 1 for a
perfectly coherent event and $1/N$ for incoherent noise.

Measured on the demonstration's gather:

| reflector | true $v_\text{rms}$ | semblance peak | half-maximum band | resolution |
|---|---|---|---|---|
| $t_0 = 1.00\ \mathrm{s}$ | $2500\ \mathrm{m\,s^{-1}}$ | $2500$ ($+0.00\%$) | $2440$–$2560$ | $\pm 60\ \mathrm{m\,s^{-1}}$ |
| $t_0 = 2.00\ \mathrm{s}$ | $3200\ \mathrm{m\,s^{-1}}$ | $3200$ ($+0.00\%$) | $2990$–$3470$ | $\pm 240\ \mathrm{m\,s^{-1}}$ |

Two results matter. The picks are **exact** on noise-free-modelled data, which
means the estimator is unbiased and the interesting number is the *width*. And the
width grows fourfold with $t_0$ for the same gather: the deeper reflector has
less moveout over the same offsets, so it constrains the velocity less. **A
velocity pick is a measurement with a resolution, and the resolution degrades with
depth** — a statement that is invisible if only the peak value is reported.

## 6. Mute: the price of the far offsets

NMO is a time shift that depends on offset, so it *stretches* the wavelet on the
far traces. The stretch factor is the fractional change in the reflection time:

$$\text{stretch}(x) = 1 - \frac{t_0}{t(x)}.$$

For the first primary the stretch reaches $21.9\%$ at 2000 m; for the second it is
only $4.6\%$, because the same offsets give less relative moveout at greater
depth. The demonstration's $20\%$ threshold mutes **5 of 81 traces**, from 1900 m
outward.

The mute is a **trade**: it removes stretched, low-frequency-contaminated data
that would bias the stack, and it removes coverage from exactly the offsets that
best constrain the velocity. Long-offset data should therefore be used *before*
the mute for velocity analysis and *after* it for stacking — different versions of
the same gather for different purposes.

## 7. Stacking gain, measured

Stacking $N$ traces whose signal is coherent and whose noise is independent
improves the signal-to-noise ratio by $\sqrt{N}$. The demonstration measures the
noise rms in a quiet window ($t > 2.5\ \mathrm{s}$):

| quantity | noise rms | gain |
|---|---|---|
| single trace | $0.07836$ | — |
| simple trace average | $0.00882$ | $8.88$ |
| NMO-corrected stack | $0.00702$ | $11.16$ |

The simple average gives $8.88$ against $\sqrt{81} = 9.00$, within $1.3\%$ — the
expected result. The NMO stack's gain is **$11.16$, $21\%$ higher**, and the
reason is instructive: resampling the traces during moveout correction is a
low-pass filter, so the stack's noise is attenuated by more than $1/\sqrt{N}$
while its signal (below the resampling's cut-off) is preserved. The stack's
apparent gain is therefore *partly an artefact of interpolation*, and quoting
$11.16$ as the stacking gain would overstate the method. This is the pattern for
every step in the flow: measure the effect, then ask which part of it is the
physics and which is the implementation.

## 8. The flow, annotated

| # | step | parameter | purpose | artefact introduced |
|---|---|---|---|---|
| 1 | edit/dead-trace removal | threshold | remove bad traces | coverage holes bias fold |
| 2 | velocity analysis | scan range, window | $v_\text{rms}(t_0)$ | resolution $\propto$ offset/moveout |
| 3 | NMO | picked $v(t_0)$ | flatten primaries | stretch on far traces |
| 4 | mute | stretch threshold | remove stretched data | loses far-offset coverage |
| 5 | stack | fold $N$ | $\sqrt{N}$ S/N gain | interpolated noise appears coherent |
| 6 | deconvolution (optional) | operator length | wavelet compression | alters amplitude and phase |

The interdependence is the point: step 3's accuracy is limited by step 2's
resolution, step 4 discards data that step 3 handled worst, and step 5's gain is
inflated by step 3's interpolation. A processing report that lists the steps
without these couplings is a recipe, not a result.

## 9. Assumptions and regime of validity

1. **A single, horizontal, isotropic reflector per hyperbolic event.** Dip moves
   the apex laterally and requires DMO or pre-stack migration; anisotropy makes
   moveout non-hyperbolic at long offsets.
2. **$v_\text{rms}$ is the correct moveout velocity.** It is a root-mean-square
   average over the overburden, not an interval velocity; converting between them
   requires Dix's equation and a layered model.
3. **No multiples.** A multiple has its own moveout and will be stacked, often
   constructively, at its own velocity.
4. **Source and receiver at the same elevation.** Topography and a weathered
   layer require static corrections before moveout means anything.
5. **The wavelet is stationary.** Transmission losses and attenuation change the
   wavelet with depth and offset, which no single NMO/stack flow repairs.

## The honest summary

The flow recovers the true velocities exactly ($2500$ and
$3200\ \mathrm{m\,s^{-1}}$) because the data are modelled with one wavelet and
Gaussian noise; the informative measurements are the error bars and the artefacts.
A $5\%$ velocity error leaves $-23.45\ \mathrm{ms}$, $0.70$ of a wavelet period,
and reduces the far trace's amplitude at $t_0$ from $1.0071$ to $-0.1338$. The
velocity pick's resolution is $\pm 60\ \mathrm{m\,s^{-1}}$ at
$t_0 = 1\ \mathrm{s}$ and $\pm 240\ \mathrm{m\,s^{-1}}$ at
$t_0 = 2\ \mathrm{s}$. A $20\%$ stretch mute removes 5 of 81 traces. And the stack
gain measures $8.88$ for a simple average against $\sqrt{81} = 9.00$, and
$11.16$ for the NMO stack, where the $21\%$ excess is interpolation, not
processing power.

## Python demonstration

[`code/seismic_processing_demo.py`](./code/seismic_processing_demo.py) prints
every number quoted above. It:

1. prints the gather parameters, the reflection times at 1000 and 2000 m and the
   NMO stretch for both primaries;
2. scans semblance in velocity at both $t_0$ values and prints each pick with its
   half-maximum bandwidth;
3. applies NMO with $0\%$ and $+5\%$ velocity errors and prints the residual
   moveout in ms and in wavelet periods, with the far-trace amplitude;
4. computes the stretch mute (5 of 81 traces from 1900 m) and measures the noise
   reduction in a quiet window for a single trace, a simple average and the NMO
   stack, with the corresponding gains.

Run it with the project virtual environment:

```bash
cd 25-projects-capstone/03-advanced-projects/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python seismic_processing_demo.py
```

The script prints only, writes no files, uses no network and exits 0. It runs in
under a second.

## Exercises

Graded problems and worked solutions are in
[`exercises/03-seismic-processing-project-exercises.md`](./exercises/03-seismic-processing-project-exercises.md)
and
[`exercises/03-seismic-processing-project-solutions.md`](./exercises/03-seismic-processing-project-solutions.md).
The ★★★ item asks you to design a velocity-analysis strategy for a target at a
stated depth and tolerance, not to re-run the scan.

## Mastery checkpoint

Without notes:

1. Write the NMO equation and compute $t(x)$ at 1500 m for $t_0 = 1.2\
   \mathrm{s}$ and $v_\text{rms} = 2800\ \mathrm{m\,s^{-1}}$.
2. Compute the residual moveout for a $2\%$ velocity error at that offset, in
   milliseconds and in fractions of a $40\ \mathrm{Hz}$ wavelet period.
3. State what semblance measures, and what its half-maximum bandwidth means.
4. A stack of 100 traces measures a noise reduction of 13. Which is more likely:
   a theoretical $\sqrt{100}$ gain or an interpolation artefact? Justify.

## Common pitfalls

1. **Reporting a velocity pick without its resolution.** The demonstration's
   resolution worsens from $\pm 60$ to $\pm 240\ \mathrm{m\,s^{-1}}$ between the
   two reflectors.
2. **Muting before velocity analysis.** The mute removes the far offsets that
   carry the velocity information.
3. **Quoting the measured stack gain as $\sqrt{N}$ without checking.** Here the
   NMO stack exceeds it by $21\%$, and the excess is not signal.
4. **Forgetting that $v_\text{rms}$ is not an interval velocity.** Dix's equation
   and a layered model are required.
5. **Treating a processing flow as order-independent.** Every step's output is
   the next step's assumption.

## Where this is used

The flow is the first half of a reflection workflow; the second half is migration
and inversion, where the velocity model built here becomes the input to
[25-04-01](../04-graduate-projects/01-fd-wave-propagation-project.md) and the
amplitude information is used for impedance and impedance-derived properties. In
professional practice the annotated flow of §8 is the deliverable that a client's
QC geophysicist reviews, and each artefact listed in it is a question they will
ask.

## Related lessons

- [06-09-02 Reflection Processing Flow: Deconvolution, NMO, Stack, Migration](../../06-seismology/09-reflection-seismology/02-processing-flow.md) —
  the full flow of which this project is one segment.
- [06-09-03 Velocity Analysis and Moveout Interpretation](../../06-seismology/09-reflection-seismology/03-velocity-analysis.md) —
  the method developed for real data, including non-hyperbolic moveout.
- [05-06-06 Documenting Processing: Reproducibility in Practice](../../05-core-geophysics/06-data-processing-principles/06-processing-transparency.md) —
  how to record the flow so that it can be reproduced.
- [25-04-01 Project: Finite-Difference Wave Propagation and Convergence Testing](../04-graduate-projects/01-fd-wave-propagation-project.md) —
  the modelling side of the same imaging problem.

## Self-assessment checklist

- [ ] I can write the NMO equation and tabulate moveout for a gather.
- [ ] I can compute a residual moveout in ms and in wavelet periods.
- [ ] I can run and interpret a semblance scan, with its resolution.
- [ ] I can compute an NMO stretch curve and choose a mute threshold.
- [ ] I can measure a stacking gain and explain a deviation from $\sqrt{N}$.
- [ ] I can list the artefacts introduced by each processing step.
