---
id: 16-09-01
title: "Seismic and Geodetic Monitoring of Cryosphere Change"
level: research
prereqs: ["06-11-07", "16-08-01", "16-04-04"]
tags: [atmosphere, climate, cryosphere, seismology, geodesy, monitoring, coda-interferometry]
---

# Seismic and Geodetic Monitoring of Cryosphere Change

> **All models and data in this module are SYNTHETIC.** The seismic noise,
> icequakes and coda waveforms in `code/seismic_monitoring_climate_demo.py` are
> generated from chosen formulas. No real station, glacier, event catalogue,
> satellite or published measurement is used.

Glaciers and ice sheets are mechanically active, and that is why geophysics can
watch them. A calving front emits seismic energy; crevasses open and close; basal
sliding and subglacial water generate tremor; and the elastic properties of firn
and ice depend on density, temperature and water content, so a seismic velocity
in the ice column is a *state variable* of the cryosphere. Two observables carry
most of the load: **event detection** (how many icequakes, when) and **relative
velocity change** (how the medium's elastic properties evolve between two states).

Both are exercised in this lesson with measured numbers, and both illustrate the
module's recurring theme: a geophysical measurement of the cryosphere is a
measurement of a *proxy*, and the proxy does not identify the mechanism on its
own. A detected event is a statement about the instrument, its band and its
threshold before it is a statement about a glacier; a measured velocity change can
come from thinning, warming, water or scattering, and separating those requires an
independent constraint — geodesy for mass, boreholes for temperature.

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** which cryospheric processes generate seismic and geodetic signals,
   and **state** which physical property each observable samples.
2. **Implement** an STA/LTA detector, and **quantify** its detection and
   false-alarm rates as a function of threshold and detection band.
3. **State** why a seismic catalogue is an operating point (threshold and band)
   rather than a property of the glacier.
4. **Derive** the relation between a relative velocity change and a coda stretch.
5. **Measure** a relative velocity change by a stretch search and **estimate** its
   noise floor as a function of the coda signal-to-noise ratio.
6. **Distinguish** measured from inferred quantities, and **name** the additional
   observation needed to attribute a velocity change to a mechanism.
7. **Combine** seismic and geodetic constraints and **state** what the combination
   resolves that neither does alone.

## Prerequisites

- [06-11-07 Declustering, Completeness and Catalogue Physics](../../06-seismology/11-earthquake-statistics-and-hazard/07-catalog-declustering.md) —
  the catalogue logic that a detection threshold creates, in its mature form.
- [16-08-01 Surface, Radiosonde and Satellite Climate Records](../08-climate-observation-and-data/01-surface-and-satellite-records.md) —
  how an observing system's changes enter a series, the same problem in a
  different instrument.
- [16-04-04 Natural Variability: ENSO, NAO, PDO, Solar and Volcanic](../04-climate-system-and-feedbacks/04-natural-variability.md) —
  the variability a monitoring series must be compared against.

## 1. What in the cryosphere makes a signal

| Process | Observable | Physical quantity sampled |
|---|---|---|
| Calving, iceberg detachment | impulsive seismic events | the event, and its source mechanism (inferred) |
| Crevasse formation and closing | impulsive events, tremor | fracture, inferred strain rate |
| Basal slip, subglacial water flow | tremor, repeating events | water pressure and sliding, inferred |
| Ocean swell and storm waves | microseism noise | ocean state, not ice |
| Thermal and density change in firn/ice | relative velocity change | elastic moduli and density, inferred from $v$ |
| Ice loss and unloading | surface uplift, gravity change | mass and its redistribution |

The right-hand column is *inferred* in every row. The measured quantity is always
ground motion or a position, and the inference is a modelling step with
assumptions attached. This is why the same seismic data can be interpreted as a
change in ice thickness, a change in temperature, a change in water content, or a
change in the scattering medium — as the lesson's final section states.

## 2. Detection is an operating point, not a catalogue

The standard automated detector is the **short-term average / long-term average**
(STA/LTA) trigger: form the signal envelope, take its average over a short window
and a long window, and declare a detection when their ratio exceeds a threshold.
Two design choices dominate the result — the windows and the **detection band**,
because events and noise have different spectra, so the band decides how separable
they are.

The demonstration builds a $600\ \mathrm{s}$ synthetic continuous record at
$100\ \mathrm{Hz}$ with smooth noise of unit standard deviation, $40$ impulsive
events whose amplitudes are drawn uniformly between $3$ and $20$ times that noise
level, and a separate noise-only record of the same length. The detector uses
windows of $0.5\ \mathrm{s}$ (STA) and $20\ \mathrm{s}$ (LTA) on the envelope of
the record band-passed between $5$ and $15\ \mathrm{Hz}$, and reports trigger
onsets at least $2\ \mathrm{s}$ apart:

| threshold | triggers | events found | false alarms | missed |
|---|---|---|---|---|
| 2.0 | 43 | 40/40 | 15 | 0 |
| 3.0 | 40 | 40/40 | 2 | 0 |
| 4.0 | 38 | 39/40 | 1 | 1 |
| 6.0 | 37 | 39/40 | 0 | 1 |
| 8.0 | 34 | 36/40 | 0 | 4 |
| 12.0 | 29 | 30/40 | 0 | 10 |

Reading the table: at a threshold of $2.0$ every event is found and the detector
also fires $15$ times on a record containing no events at all; at $12.0$ it misses
ten of the $40$ events and makes no false alarms. **Neither column is "the"
catalogue.** The pair (events found, false alarms) is the detector's operating
characteristic, and a published catalogue that does not state its threshold, its
band and its window lengths is not reproducible — an exact analogue of the
magnitude-of-completeness argument in
[06-11-07](../../06-seismology/11-earthquake-statistics-and-hazard/07-catalog-declustering.md).

A further subtlety worth carrying forward: a spatially distributed array with a
*fixed* threshold produces a *time-varying* completeness, because the noise level
changes seasonally (storms, melt, wind) and so does the event rate it suppresses.

## 3. Coda-wave interferometry: turning a waveform into a velocity change

The second observable is far more sensitive than a travel time. Compare a
**reference** coda waveform recorded at one time with a **current** one recorded
later. If the medium's wave speed changes by a fractional amount
$\mathrm{d}v/v$, every travel time changes by the same fractional amount, so the
later waveform is the earlier one **stretched in time** by

$$\varepsilon = -\frac{\mathrm{d}v}{v},$$

where $\varepsilon$ is the relative stretch. The sign convention is worth
stating explicitly: a *slower* medium lengthens travel times and *stretches* the
coda, so $\varepsilon>0$ corresponds to $\mathrm{d}v/v<0$.

The measurement is a search over trial stretch factors $\varepsilon$, maximising
the correlation between the stretched reference and the current waveform. The
demonstration builds a synthetic $30\ \mathrm{s}$ coda, applies a known stretch,
and recovers it on a $1201$-point grid. In the absence of added noise, recovery is
exact to machine precision:

| true stretch | recovered | error |
|---|---|---|
| $+0.50\%$ | $+0.005000$ | $+5.7\times10^{-16}$ |
| $+0.05\%$ | $+0.000500$ | $+4.5\times10^{-16}$ |

So the *method* is unbiased and exact; what limits it is noise, which is measured
next.

## 4. The noise floor, and why it is the real resolution

Adding noise at various levels and repeating over $40$ realisations converts the
problem into a familiar one: the resolution is the standard deviation of the
estimate. Noise is expressed as a standard deviation relative to the coda's peak
amplitude:

| true stretch | noise sd | mean estimate | sd of estimate | sd / signal |
|---|---|---|---|---|
| 0.50% | 0.01 | $+0.005001$ | $6.8\times10^{-6}$ | 0.00 |
| 0.50% | 0.05 | $+0.005001$ | $3.5\times10^{-5}$ | 0.01 |
| 0.50% | 0.20 | $+0.005005$ | $1.1\times10^{-4}$ | 0.02 |
| 0.50% | 0.50 | $+0.005036$ | $3.5\times10^{-4}$ | 0.07 |
| 0.05% | 0.01 | $+0.000501$ | $3.9\times10^{-6}$ | 0.01 |
| 0.05% | 0.05 | $+0.000498$ | $3.3\times10^{-5}$ | 0.07 |
| 0.05% | 0.20 | $+0.000488$ | $1.2\times10^{-4}$ | 0.25 |
| 0.05% | 0.50 | $+0.000526$ | $2.9\times10^{-4}$ | 0.57 |

Two results to carry away. First, the bias is negligible at every noise level: the
*estimate* is fine, and only its *uncertainty* grows. Second, the uncertainty is a
*relative* quantity: the same absolute noise sd of $0.20$ gives
$1.1\times10^{-4}$ on a $0.5\%$ change ($2\%$ of the signal) and
$1.2\times10^{-4}$ on a $0.05\%$ change ($25\%$ of the signal). **The resolution of
coda interferometry is set by the coda signal-to-noise ratio and the window
length, not by a fixed instrumental sensitivity** — which is why the same method
that resolves a seasonal cycle in a noisy glacier also resolves a fraction of a
per cent on a quiet one.

The generalization: a measurement must be reported as *value $\pm$ uncertainty with
a stated noise level*, and the noise level is a property of the site and the
season, not of the method.

## 5. What geodesy adds, and what the combination resolves

Seismology measures **motion and elastic state**; geodesy measures **position and
mass**. They are complementary and neither is redundant:

- **GNSS vertical motion** at a glacier or ice-sheet margin measures the
  viscoelastic and elastic response to unloading: uplift follows thinning, with a
  timescale set by mantle viscosity and a spatial pattern set by the load. This
  is the subject of [16-09-02](02-geodesy-climate.md).
- **Repeat gravimetry and satellite gravimetry** measure the mass change directly,
  which is what a sea-level budget needs.
- **Seismic velocity change** responds to temperature, water content and damage —
  state variables that mass alone does not determine.

A combination therefore resolves what neither does alone: mass change plus
velocity change constrains the *cause* of a velocity change (a thinning signal
should move the surface and the mass; a meltwater pulse changes velocity with a
seasonal signature but no comparable mass signature). Building that argument
requires a forward model linking each mechanism to each observable — the same
non-uniqueness problem the whole curriculum keeps meeting.

## 6. Assumptions and regime of validity

1. **The coda is a repeatable, scattered wavefield.** The stretch method assumes
   the reference and current coda sample the same paths; a change in source
   position, in scattering geometry, or in the noise field breaks it.
2. **The stretch is homogeneous over the sampled volume.** A velocity change in
   part of the volume produces an apparent stretch that depends on the depth
   sensitivity of the late coda, which must be modelled.
3. **The detection band separates events from noise.** If the event spectrum
   overlaps the noise, no threshold gives both a high detection rate and few false
   alarms.
4. **The event threshold and band are stable in time.** Otherwise the apparent
   event rate changes when the detector does.
5. **The coda signal-to-noise ratio is stated.** A velocity change quoted without
   it is not reproducible.
6. **Seismic observations are proxies.** Calving, sliding and thinning are
   *inferred* from ground motion; the inference needs a mechanical model and
   independent validation.

## 7. Python demonstration

[`code/seismic_monitoring_climate_demo.py`](code/seismic_monitoring_climate_demo.py)
builds the synthetic record and runs the whole analysis, printing labelled results
with units. It:

1. generates coloured noise, a distribution of impulsive events and a noise-only
   reference record;
2. runs an STA/LTA detector in a stated band and tabulates detection and
   false-alarm rates versus threshold;
3. recovers a known coda stretch by a correlation search;
4. measures the noise floor of that estimate over $40$ realisations;
5. states what is measured and what is inferred.

Every number in this lesson is printed by that demonstration.

## Mastery checkpoint

> The demonstration detects $40/40$ events with $15$ false alarms at threshold
> $2.0$, and $30/40$ events with $0$ false alarms at threshold $12.0$, on a record
> with a noise-only companion.
>
> **(a)** Explain why neither operating point is "the" catalogue, and name the
> three detector parameters that must accompany a seismic catalogue.
> **(b)** A coda stretch of $+0.0005$ is recovered with a standard deviation of
> $2.9\times10^{-4}$ at a noise level of $0.50$, and with
> $3.9\times10^{-6}$ at $0.01$. Interpret the two numbers as resolution, and state
> the sign convention relating stretch to velocity change.
> **(c)** The recovered stretch is unbiased at every noise level. Explain what
> that tells you about the bias-versus-variance distinction in this measurement.
> **(d)** A study reports a $0.1\%$ velocity decrease in a glacier's firn. List
> three mechanisms that could produce it, and for each name one independent
> observation that would distinguish it.
> **(e)** State what a GNSS uplift series adds to the seismic velocity series that
> the velocity series cannot supply on its own.

## Common pitfalls

1. **Publishing a catalogue without its operating point.** Threshold, band and
   windows decide the count.
2. **Comparing event rates across seasons or years with a fixed threshold.** The
   noise level changes, so the completeness changes.
3. **Quoting a velocity change without its noise floor.** The resolution is
   relative to the coda signal-to-noise ratio, not absolute.
4. **Forgetting the sign convention.** A stretch is a *slower* medium.
5. **Treating a velocity change as a thinning measurement.** It is a state
   variable; mass requires geodesy or gravimetry.
6. **Assuming coda repeatability.** A change in source or scattering invalidates
   the stretch estimate.
7. **Reading tremor as an event rate.** Continuous tremor is a different
   observable with different detection logic.

## Related modules

- [16-09-02 Geodesy for Sea Level, Ice Mass and Water Storage](02-geodesy-climate.md) —
  the mass-based observable that makes the seismic proxy interpretable.
- [16-09-05 Climate–Geohazard Interactions (Sea Level, Permafrost, Slopes)](05-climate-geohazards.md) —
  where cryospheric change becomes a hazard.
- [16-09-03 Borehole Temperature Records of Past Climate](03-geothermal-climate-records.md) —
  the temperature history a velocity change could reflect.
- [16-09-04 Geophysics for Carbon Capture and Storage Monitoring](04-geophysics-carbon-storage.md) —
  the same time-lapse logic applied to a different target.
- [06-11 Earthquake Statistics and Hazard](../../06-seismology/11-earthquake-statistics-and-hazard/README.md) —
  the catalogue, completeness and detection-limit discipline in full.
- [16-04-04 Natural Variability: ENSO, NAO, PDO, Solar and Volcanic](../04-climate-system-and-feedbacks/04-natural-variability.md) —
  separating a forced signal from internal wobble.

## Self-assessment checklist

- [ ] I can implement an STA/LTA detector and tabulate its operating curve.
- [ ] I can state why a seismic catalogue is an operating point.
- [ ] I can derive $\varepsilon = -\mathrm{d}v/v$ and use the sign convention.
- [ ] I can estimate a velocity-change noise floor and report it with the value.
- [ ] I can separate measured from inferred quantities in a cryospheric study.
- [ ] I can state what geodesy adds that seismology cannot.
