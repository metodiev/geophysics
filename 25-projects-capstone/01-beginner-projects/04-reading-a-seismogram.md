---
id: 25-01-04
title: "Project: Reading and Describing a Real Seismogram"
level: beginner
prereqs: ["25-01-01", "03-10-02", "03-10-03", "06-04-04"]
estimated_minutes: 120
tags: [projects, seismology, waveform, picking, amplitude, teaching]
---

# Project: Reading and Describing a Real Seismogram

## Learning objectives

1. **Describe** a seismogram by the five quantities that can be measured from one record:
 sampling rate, noise level, arrival times, peak ground velocity and duration.
2. **Convert** instrument counts to ground motion given a response, and **state** the unit of
 each stage.
3. **Pick** P and S arrivals automatically with an STA/LTA detector and **measure** the pick
 error against a known arrival.
4. **Derive** the S−P distance formula and **compute** a hypocentral distance under a stated
 velocity model.
5. **Estimate** the dominant frequency of a window from its amplitude spectrum and **state** the
 spectral resolution that limits it.
6. **Distinguish** what one record determines (S−P, PGV, duration) from what it does not
 (magnitude, moment, depth), and **refuse** to report the latter.

## Prerequisites

- [25-01-01 Project: Units, Conversions and First Scientific Plots](./01-units-and-plotting.md) —
  the unit audit every amplitude must survive.
- [03-10-02 Reading MiniSEED/SAC: Trace and Stream](../../03-scientific-computing/10-obspy-and-seismic-data/02-reading-waveforms.md) —
  the file formats and the `Trace`/`Stream` objects a real record arrives in.
- [03-10-03 StationXML Inventory, Response and Instrument Correction](../../03-scientific-computing/10-obspy-and-seismic-data/03-inventory-and-metadata.md) —
  the response that turns counts into metres per second.
- [06-04-04 Magnitude Scales: Local, Body, Surface, Duration, Moment](../../06-seismology/04-earthquake-location-and-magnitude/04-magnitude-scales.md) —
  why a magnitude needs more than one record.

## 1. The question

*What can you honestly say about an earthquake from a single seismogram?*

The project is deliberately a *description* task, not a detection or an
inversion task, because the boundary between what one record determines and what
it does not is the first thing a beginner gets wrong. A single three-component
record gives you an S−P time, a peak amplitude, a duration and a dominant
frequency. It does not give you a magnitude, a moment, a focal mechanism or a
depth, and no amount of arithmetic converts one into the other.

## 2. The data

**Real archive.** A waveform is retrieved from the IRIS/EarthScope FDSN
dataselect service at
<https://service.iris.edu/fdsnws/dataselect/1/query> using a network, station,
location, channel and time window, and the matching instrument response from the
station service at <https://service.iris.edu/fdsnws/station/1/query>. The
retrieval URL, the channel code and the response stage chain belong in the
report: a velocity in counts without a response is not a velocity.

**Synthetic teaching record.** The demonstration builds a 60 s record at
$f_s = 100\ \mathrm{Hz}$ from a P wavelet at $2.0\ \mathrm{Hz}$ arriving at
$10.00\ \mathrm{s}$, an S wavelet at $1.0\ \mathrm{Hz}$ arriving at
$16.00\ \mathrm{s}$, and Gaussian noise of RMS $0.05\ \mathrm{\mu m\,s^{-1}}$.

**Provenance: SYNTHETIC.** No instrument, no archive and no real event is used
below. The velocities are in micrometres per second because that is a convenient
scale for local events; the arithmetic would be identical in metres per second.

## 3. The project specification

**Steps.**

1. Retrieve one record and its response, and correct it to ground velocity.
   Print the sampling rate, the number of samples, the duration and the Nyquist
   frequency.
2. Measure the pre-event noise RMS over a window before the first arrival.
3. Pick P and S with an STA/LTA detector at a stated short and long window and a
   stated threshold. Report both picks **and** their uncertainty — from the
   detector's time resolution and from the difference between the two channels
   or components.
4. Convert S−P to distance under a stated velocity model, and state the
   assumption that makes it a hypocentral distance.
5. Measure the peak ground velocity, the S/P amplitude ratio, and the dominant
   frequency and period of the S window from its amplitude spectrum.
6. Measure the coda duration to a stated amplitude threshold.
7. Write the description: five measured quantities with units and uncertainties,
   plus a sentence on each of the four things the record does not determine.

**Deliverable.** A one-page record description: a labelled waveform section, the
five numbers with units and uncertainties, and the limitations paragraph.

**Success criterion.** Every number carries a unit and an uncertainty; the
velocity model is stated; no magnitude is reported; the pick error is measured
against something, not asserted.

## 4. From counts to ground motion

A digitised record is $c[n]$ in counts. The instrument's response converts it,
frequency by frequency, to ground motion: dividing the spectrum by the complex
response and transforming back gives velocity in $\mathrm{m\,s^{-1}}$. The
statement "the peak was 1.8 µm/s" is meaningless without the response used, and
the four error sources are:

1. **the response itself** — a stage-gain error propagates linearly;
2. **the sensor's orientation** — a channel pointing 5° off vertical mixes
   horizontal motion into the vertical component;
3. **the clip level** — a clipped peak is a lower bound, not a measurement;
4. **the timing** — a clock error shifts every pick by the same amount.

The record used here has a flat velocity response by construction, so counts and
velocity are proportional with a factor of 1 µm/s per count.

## 5. Picking, and the size of a pick error

The demonstration applies an STA/LTA detector with a 1.0 s short window, a 10.0 s
long window and a threshold of 4.0, and compares each pick with the known arrival:

| arrival | true time (s) | picked (s) | error (s) |
|---|---|---|---|
| P | 10.00 | 9.91 | $-0.09$ |
| S | 16.00 | 15.72 | $-0.28$ |

Both picks are **early**, and the S pick is three times worse than the P pick.
The mechanism is the detector's definition: STA/LTA exceeds the threshold when
the *ratio* rises, which happens on the first noise excursion above the LTA
baseline, before the true onset. The bias grows with the wavelet's rise time, so
a 1 Hz S wavelet is picked much earlier than a 2 Hz P wavelet. The measured
S−P time is therefore $5.81\ \mathrm{s}$ against a true $6.00\ \mathrm{s}$ — a
$3.2\%$ error that will propagate directly into the distance of §6.

This is why host-to-pick errors are quoted: the *systematic* early bias is not
reduced by picking more carefully with the same statistic, only by using a
different statistic (a higher-order detector, a matched filter, or manual
review).

## 6. Distance from S minus P

For a direct ray in a medium with constant $V_p$ and $V_s$, the two travel times
to hypocentral distance $D$ are $t_P = D/V_p$ and $t_S = D/V_s$, so

$$t_S - t_P = D\left(\frac{1}{V_s} - \frac{1}{V_p}\right)
= D\,\frac{V_p - V_s}{V_p V_s},
\qquad
\boxed{\,D = (t_S - t_P)\,\frac{V_p V_s}{V_p - V_s}\,}$$

With the demonstration's model ($V_p = 6.00\ \mathrm{km\,s^{-1}}$,
$V_s = 3.46\ \mathrm{km\,s^{-1}}$, $V_p/V_s = 1.734$) the factor is

$$\frac{V_p V_s}{V_p - V_s} = \frac{6.00 \times 3.46}{2.54} = 8.17\ \mathrm{km\,s^{-1}},$$

so $D = 5.81 \times 8.17 = 47.49\ \mathrm{km}$. For a surface focus that is the
epicentral distance; for a focus 10 km deep the hypocentral distance for the same
epicentre is $\sqrt{47.49^{2} + 10^{2}} = 48.53\ \mathrm{km}$.

Two properties of the formula matter more than the number. First, it is
**independent of the origin time**, which is why a single station can locate an
event to a distance at all. Second, it is **strongly sensitive to the velocity
model**: the factor 8.17 changes to 8.40 if $V_s$ rises to $3.50\ \mathrm{km/s}$
(that is $+1.2\%$ in $V_s$), a $+2.8\%$ change in distance. The velocity model
belongs in the report, next to the distance.

## 7. Amplitude, period and duration

| quantity | demonstration value |
|---|---|
| PGV, P window | $0.768\ \mathrm{\mu m\,s^{-1}}$ |
| PGV, S window | $1.785\ \mathrm{\mu m\,s^{-1}}$ |
| S/P amplitude ratio | $2.32$ (chosen $2.50$) |
| signal-to-noise ratio of the S peak | $35.7$ |
| dominant frequency of the S window | $0.82\ \mathrm{Hz}$ (period $1.216\ \mathrm{s}$) |
| spectral resolution of that estimate | $0.118\ \mathrm{Hz}$ |
| coda duration (to 10% of peak envelope) | $6.69\ \mathrm{s}$ |
| $\log_{10}(\mathrm{PGV}/1\ \mathrm{\mu m\,s^{-1}})$ | $0.252$ |

The S/P ratio of $2.32$ is smaller than the chosen $2.50$ because the noise
inflates the P peak — a measurement error that a higher SNR would remove. The
dominant frequency of $0.82\ \mathrm{Hz}$ is below the chosen $1.0\ \mathrm{Hz}$
for a different reason: the 8.5 s S window has a spectral resolution of only
$0.118\ \mathrm{Hz}$, and the Gaussian envelope broadens the peak, so the
*argmax* of a broad spectral lobe is not the wavelet's centre frequency. Both
deficits are honest measurement errors and both shrink with better data.

**What the record does not give.** A magnitude requires an amplitude *and* a
distance *and* a site term *and* a calibration constant; the
$\log_{10}$ of the PGV is a raw, unit-carrying number, not $M_L$. A seismic
moment requires a source spectrum over a bandwidth the record may not cover. A
depth requires either a depth phase or a second station. A focal mechanism
requires three components at three or more azimuths. Reporting any of these from
one record is the failure this project exists to prevent.

## 8. Failure modes and how to detect them

1. **Reporting counts as velocity.** *Detect:* check that the number's magnitude
   matches the sensor's sensitivity times the expected ground motion.
2. **A pick error ignored.** *Detect:* compute the S−P distance with the pick
   shifted by its own stated uncertainty; the demonstration's $0.28\ \mathrm{s}$
   error moves the distance by $2.3\ \mathrm{km}$.
3. **A velocity model assumed silently.** *Detect:* state $V_p$, $V_s$ and
   $V_p/V_s$; re-run with $\pm2\%$ on $V_s$ and report the change.
4. **A dominant frequency read from a window shorter than a few periods.**
   *Detect:* compare the window length with $1/f$; the demonstration's
   $1.216\ \mathrm{s}$ period fits 7.0 times into its 8.5 s S window, which is
   adequate, while an 0.2 Hz estimate over 3 s is not.
5. **A magnitude quoted from a PGV.** *Detect:* ask for the calibration
   constant, the distance and the site term; if any is missing, the number is not
   a magnitude.

## 9. Rubric

| Criterion | 4 — exemplary | 3 — competent | 2 — developing | 1 — incomplete |
|---|---|---|---|---|
| Metadata | $f_s$, $N$, duration, Nyquist, response all recorded | $f_s$ and duration | $f_s$ only | None |
| Noise | Pre-event RMS with the window stated | RMS | Qualitative | Absent |
| Picks | Both picks with measured errors | Both picks | One pick | No picks |
| Distance | Formula derived, model stated, sensitivity shown | Distance with model | Distance only | Absent |
| Amplitudes | PGV with unit, SNR, period, duration | PGV and duration | PGV only | Counts |
| Limitations | Four items named with the reason | Two items | One | Absent |

## 10. Assumptions and regime of validity

1. **A flat velocity response.** The demonstration's counts-to-velocity factor is
   1 µm/s per count by construction; a real record needs the full response
   deconvolution, including the sensor's corner frequency.
2. **Constant $V_p$ and $V_s$.** The S−P formula uses a homogeneous medium; a
   layered structure changes the distance by several percent, and a Moho
   refraction can change it more.
3. **A direct ray.** At distances where the first arrival is a head wave or a
   core phase, the S−P time no longer measures a hypocentral distance.
4. **Gaussian, stationary noise.** Real noise is coloured and has transients
   (trains, footsteps, cultural noise); the SNR of 35.7 measured here is
   optimistic for a real station.
5. **One event per record.** A record with a second event contaminates the coda
   duration and the noise estimate.

## The honest summary

One well-described seismogram yields five numbers: a sampling rate
($100\ \mathrm{Hz}$, Nyquist $50\ \mathrm{Hz}$), a noise level
($0.0500\ \mathrm{\mu m\,s^{-1}}$ RMS), an S−P time ($5.81\ \mathrm{s}$, true
$6.00$, with picks biased early by $-0.09$ and $-0.28\ \mathrm{s}$), a distance
($47.49\ \mathrm{km}$ under a stated $V_p/V_s = 1.734$), and an amplitude with a
period ($1.785\ \mathrm{\mu m\,s^{-1}}$ S peak at $0.82\ \mathrm{Hz}$ over
$6.69\ \mathrm{s}$ of coda). It yields no magnitude, no moment, no depth and no
mechanism. The transferable skill is not the arithmetic — the S−P formula is
three lines — but the discipline of reporting exactly the five measured
quantities with units and the four missing ones by name.

## Python demonstration

[`code/reading_seismogram_demo.py`](./code/reading_seismogram_demo.py) prints every number quoted above, writes no files,
uses no network and exits 0:

```bash
cd 25-projects-capstone/01-beginner-projects/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python reading_seismogram_demo.py
```

It is seeded with `np.random.default_rng(20261014)` and runs in under a second.
## Exercises

Graded problems and worked solutions are in
[`exercises/04-reading-a-seismogram-exercises.md`](./exercises/04-reading-a-seismogram-exercises.md)
and
[`exercises/04-reading-a-seismogram-solutions.md`](./exercises/04-reading-a-seismogram-solutions.md).
The ★★★ item asks you to design a pick-error budget, not to pick a record by
hand.

## Mastery checkpoint

Without notes:

1. A record is sampled at 40 Hz. State the Nyquist frequency and the shortest
   representable period.
2. With $V_p = 6.2\ \mathrm{km\,s^{-1}}$ and $V_s = 3.55\ \mathrm{km\,s^{-1}}$,
   compute the S−P distance factor.
3. The measured S−P is $5.81\ \mathrm{s}$ but the S pick has a $0.28\ \mathrm{s}$
   early bias. Which way does the distance move, and by about how much?
4. Name the four quantities a single record does *not* determine, and the
   additional observation each one needs.

## Common pitfalls

1. **Reporting a time without an origin.** An arrival time is meaningless without the reference time and the instrument delay it was measured against.
2. **Reading amplitudes in counts.** Counts become ground motion only after the response is removed; a peak quoted in counts cannot be compared with anything.
3. **Trusting one STA/LTA parameter set.** The detector reports what its window and threshold were tuned to find, and the pick error must be measured, not assumed.
4. **Using S minus P with a single velocity.** The conversion needs a velocity model, and its error propagates directly into the distance.
5. **Quoting a duration without saying how it was defined.** Between which amplitude levels, and on which component, changes the number by a large fraction.

## Where this is used

Every later waveform project reuses this description step. The picking question
becomes a machine-learning problem in
[21-06-02](../../21-statistics-bayesian-ml/06-ml-in-geophysics/02-phase-picking-ml.md),
where the bias measured here reappears as a systematic pick offset. The distance
formula is a special case of the travel-time inversion of
[25-02-01](../02-intermediate-projects/01-travel-time-curves.md), and the coda
duration feeds the catalogue statistics of
[25-04-04](../04-graduate-projects/04-earthquake-catalog-analysis.md). In
professional practice this exact description is the first quality-control pass on
every station in a network: an analyst who cannot state the noise level, the
response and the pick error cannot defend any later measurement.

## Related lessons

- [20-01-05 Sampling, Nyquist and Reconstruction](../../20-signal-processing/01-signals-and-systems/05-sampling-theory.md) —
  the sampling theorem behind §1's Nyquist statement.
- [06-02-02 Snell's Law, Layered Media and the Travel-Time Curve](../../06-seismology/02-ray-theory-and-travel-times/02-snell-and-layering.md) —
  what changes when the velocity model is not constant.
- [03-10-06 Travel Times with TauP and Phase Naming](../../03-scientific-computing/10-obspy-and-seismic-data/06-taup-travel-times.md) —
  the proper tool for the distance conversion when the structure is known.
- [25-02-01 Project: Travel-Time Curves and 1-D Velocity Structure](../02-intermediate-projects/01-travel-time-curves.md) —
  the next project in this folder.

## Self-assessment checklist

- [ ] I can state the sampling rate, Nyquist frequency and duration of a record.
- [ ] I can measure a noise level over a stated window.
- [ ] I can pick P and S and measure the pick errors.
- [ ] I can derive and apply the S−P distance formula, stating the model.
- [ ] I can measure PGV, an S/P ratio, a spectral peak and a duration.
- [ ] I can name the four things one record cannot determine.
