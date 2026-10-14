---
id: 23-02-05
title: "Deployment, Orientation, Timing and Metadata"
level: advanced
prereqs: ["23-02-01", "03-10-03"]
estimated_minutes: 90
tags: [seismology, deployment, orientation, timing, coupling, metadata]
---

# Deployment, Orientation, Timing and Metadata

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the leakage between the radial and transverse components produced by a sensor orientation error, and **state** the bias it puts on a
   single-station anisotropy measurement.
2. **Compute** the expected number of stations affected by a loss of clock lock,
   and the timing error accumulated during an unlocked interval.
3. **Compute** the deviation a ground-coupling resonance adds to the response, and
   **state** the frequency below which the installation is harmless.
4. **Compute** the apparent horizontal acceleration produced by a sensor tilt, and
   **derive** the tilt that imitates a stated acceleration level.
5. **List** the metadata a deployment must record, and **classify** each item as
   recoverable or not.
6. **Order** the deployment tasks so that the irreversible measurements are taken
   while the information still exists.

All orientation errors, clock accuracies, lock-loss rates, coupling resonances and
tilt angles in this lesson are **SYNTHETIC** teaching values printed by the
demonstration. No measured installation response, no manufacturer clock
specification and no field record is used or reproduced.

## Prerequisites

- [01 Seismometers: Broadband, Short-Period, Geophones, MEMS](01-seismometers.md) —
  the instrument whose response the installation modifies.
- [03-10-03 StationXML Inventory, Response and Instrument Correction](../../03-scientific-computing/10-obspy-and-seismic-data/03-inventory-and-metadata.md) —
  the format the metadata must eventually satisfy.

## 1. Intuition: the installation is part of the instrument

A seismometer's specification describes the sensor on a test bench. What is
deployed is a *system*: the sensor, the way it is coupled to the ground, its
levelling, the clock that timestamps its output, and the metadata that records all
of it. Each of these can dominate the measurement in a frequency band, and none of
them is visible in the data.

The organising principle of this lesson is that **the deployment is a set of
measurements, not a set of tasks**. Orientation is measured; the clock's state is
recorded; the levelling is checked; the coupling is described. A deployment that
treats these as formalities produces data that look correct and are wrong in ways
that cannot be repaired afterwards.

## 2. Orientation

A three-component sensor measures three orthogonal directions of its own frame. To
compare with a source, with a model, or with another station, those components must
be rotated into a geographic frame, which requires knowing the rotation — usually
the angle of the north component relative to true or magnetic north, with the
reference stated.

If the orientation used is wrong by $\delta$, then a wave arriving purely in the
radial plane appears partly in the transverse component:

$$\frac{A_T}{A_R} = \sin\delta, \qquad
20\log_{10}\left(\frac{A_T}{A_R}\right)\ \text{in dB}.$$

The demonstration's table:

| $\delta$ (deg) | $\sin\delta$ | $A_T/A_R$ (dB) | fast-direction bias |
|---|---|---|---|
| 0.5 | 0.00873 | −41.18 | 0.5° |
| 1.0 | 0.01745 | −35.16 | 1.0° |
| 2.0 | 0.03490 | −29.14 | 2.0° |
| 5.0 | 0.08716 | −21.19 | 5.0° |
| 10.0 | 0.17365 | −15.21 | 10.0° |
| 20.0 | 0.34202 | −9.32 | 20.0° |
| 30.0 | 0.50000 | −6.02 | 30.0° |

Two consequences follow. First, **a small error is a large leakage**: 5° puts
transverse energy at −21.2 dB, which is larger than many genuine anisotropy
signals, so an unmeasured orientation can be mistaken for a physical result.
Second, **the bias transfers directly to a single-station measurement**: a
shear-wave splitting fast direction determined at one station is biased by up to
the orientation error itself, so a dataset claiming 5° resolution of fast
directions needs orientations known to much better than 5°.

The orientations must be *measured*, not assumed: by a gyrocompass, by a
compass with the local declination applied, by a GNSS-based heading, or by
polarisation analysis of a known event. Whichever is used, the metadata must record
the method, the reference (true or magnetic north), the local declination applied
if any, and the uncertainty.

## 3. Timing

Almost every station in a temporary deployment timestamps its data with a clock
disciplined to a global navigation satellite system. The clock is the component
most likely to fail silently: when the lock is lost, the logger continues to record
with a free-running oscillator, and the record remains internally consistent while
its absolute time drifts.

Two numbers size the problem. First, the **fraction of stations affected**: for
$N$ stations over $D$ days with a per-station-day probability $p$ of losing the
lock,

$$P(\text{a given station is affected}) = 1 - (1-p)^{D},$$

and the expected number of affected stations is $N$ times that. For
$N = 30$, $D = 20$ and $p = 0.03$, the demonstration reports an expectation of
18 station-days with a loss, and **13.69 of 30 stations (45.6 %)** with at least
one — a number that surprises most first-time deployments.

Second, the **drift accumulated while unlocked**. A fractional clock error
$\epsilon$ accumulates $\epsilon t$:

| $\epsilon$ | drift in 1 day (s) | samples at 100 sps | drift in 20 days (s) |
|---|---|---|---|
| 1e−6 | 0.0864 | 8.6 | 1.728 |
| 5e−6 | 0.4320 | 43.2 | 8.640 |
| 1e−5 | 0.8640 | 86.4 | 17.280 |
| 5e−5 | 4.3200 | 432.0 | 86.400 |

A free-running uncompensated oscillator is typically worse than the largest value
in this table (parts in $10^{5}$ to $10^{6}$ per day or more, depending on type and
temperature), so an unlocked interval of a day is not a small error: it is a
timing error comparable to the whole travel-time budget. The practical protocol is
therefore:

1. Record the lock state and the time error *at both the start and the end* of
   each recording session, so the drift can be interpolated rather than guessed.
2. Compare the clock against a reference at every maintenance visit, and record
   the difference.
3. Treat a station-day with an unlogged loss of lock as unusable for absolute-time
   work, and say so in the metadata rather than silently correcting it.

## 4. Ground coupling

The sensor's mass sits on ground that has its own compliance. Because the sensor
base, the soil beneath it and the mass form a mechanical system, the installation
adds a resonance at a frequency set by the soil stiffness and the sensor mass and
base area. Modelling it as a single-degree-of-freedom system of natural frequency
$f_c$ and damping $h_c$ gives the same response function as Section 2 of the
seismometer lesson,

$$|H_c(f)| = \frac{r^{2}}{\sqrt{(1-r^{2})^{2}+(2h_c r)^{2}}}, \qquad r = \frac{f}{f_c},$$

applied now to the *installation* rather than the sensor. With
$f_c = 20\ \mathrm{Hz}$ and $h_c = 0.5$ the demonstration reports

| $f$ (Hz) | 1 | 2 | 5 | 10 | 20 | 40 | 80 |
|---|---|---|---|---|---|---|---|
| $\lvert H_c\rvert$ | 0.0025 | 0.0100 | 0.0644 | 0.2774 | 1.0000 | 1.1094 | 1.0307 |
| deviation (dB) | −52.03 | −39.96 | −23.82 | −11.14 | 0.00 | +0.90 | +0.26 |

The pattern is the reverse of the sensor's own: the coupling resonance
*attenuates* low frequencies and slightly amplifies frequencies just above
$f_c$. At 10 Hz the deviation is already −11.1 dB — a factor of 3.6 in amplitude —
so an installation on soft ground has a response that differs from the
specification by more than most reported amplitude anomalies.

The practical consequences:

- **The deviation is largest where the sensor's own signal is largest** for a
  short-period or geophone deployment, which is why buried installations are
  standard for active-source work.
- **The correct fix is measurement**, not modelling: an installation response
  cannot be predicted from first principles without the soil properties, and the
  cheapest reliable approach is a cross-check against a reference sensor, or an
  installation method that pushes the coupling resonance well above the band of
  interest (a pier on bedrock, a buried sensor in compacted sand, a screwed-in
  anchor).

## 5. Levelling and tilt

A sensor that is tilted by $\theta$ from vertical senses a component of gravity
along its nominally horizontal axes:

$$a_{\text{apparent}} = g\sin\theta .$$

The demonstration's values for $g = 9.81\ \mathrm{m/s^{2}}$:

| $\theta$ | 0.001° | 0.005° | 0.01° | 0.05° | 0.1° | 1° |
|---|---|---|---|---|---|---|
| $a$ (m/s²) | 1.712e−4 | 8.561e−4 | 1.712e−3 | 8.561e−3 | 1.712e−2 | 1.712e−1 |

and, inverted, the tilt that imitates a stated apparent acceleration:

| target $a$ (m/s²) | 1e−6 | 1e−5 | 1e−4 |
|---|---|---|---|
| $\theta$ (degrees) | 0.00006 | 0.0006 | 0.0058 |
| $\theta$ (arcsec) | 0.21 | 2.1 | 21.0 |

Even a fraction of an arcsecond of tilt imitates a horizontal acceleration of
order $10^{-6}\ \mathrm{m/s^{2}}$. Since long-period horizontal noise at a good
site is far below that, **tilt usually sets the horizontal long-period noise
floor**, not the sensor. This is why broadband installations are levelled
carefully, why the sensor is protected from temperature-driven base movement, and
why the best stations use tilt measurement or active tilt compensation. For
short-period and active-source work in the 5–50 Hz band the tilt contribution is
negligible in comparison, and the effort belongs elsewhere.

## 6. Metadata: what the deployment must deliver

| Item | Class | Recoverable after the campaign? |
|---|---|---|
| Station code, operator, date and time of deployment | Identity | Yes, from the roster |
| Position and its accuracy, with the CRS | Position | By re-survey |
| Elevation with the height system named | Position | Expensively |
| Sensor type and serial number; logger serial and firmware | Instrument | Only if recorded |
| Gain, filter settings, sample rate | Instrument | Only if recorded |
| Orientation angle, reference, method, uncertainty | Geometry | **No** |
| Levelling state, bubble or tilt readings | Geometry | **No** |
| Ground type, coupling method, burial depth | Condition | **No** |
| Clock source, lock status and time error at start and end | Timing | Partly, from the data |
| Deviations from plan and their reasons | Process | **No** |

The ordering rule that follows is simple and is the operational content of this
lesson: **do the irreversible things first.** Levelling and orientation are
measured while the sensor is open; clock state is read at power-up and power-down;
coupling is photographed and described before backfill. A team that packs up and
then fills in the forms will produce a dataset whose metadata is
irreconstructible.

## 7. Assumptions and regime of validity

1. **The leakage formula assumes a plane wave, a single arrival and no scattering.**
   With a scattered or multi-arrival wavefield the transverse energy is not zero
   for a perfectly oriented station, so the orientation error cannot be read
   directly from $T/R$. The measurement of orientation must use a method that
   identifies a single arrival.
2. **Independent losses of lock.** Real losses cluster with temperature, power
   quality and site visits, so the expected count is an average over a
   heterogeneous process.
3. **A single-degree-of-freedom coupling model.** The installation is more complex
   (the base, the backfill, the cable), and the model above is a scaling argument
   rather than a transfer function.
4. **Small tilt.** The relation is linear in $\theta$ for small angles, which is
   the regime of a levelled sensor; a badly tilted sensor is a different problem
   (it couples the vertical and horizontal channels and can clip).
5. **Metadata completeness can be measured but the score is not a quality
   measure** — see
   [23-01-03 Field Notebooks, Metadata and Data Provenance](../01-field-safety-and-planning/03-field-notebooks.md).

## 8. The honest summary

- Orientation is a measurement: 5° of error is −21.2 dB of leakage.
- Expect roughly half of a 30-station, 20-day deployment to lose clock lock at
  least once at $p = 0.03$ per station-day; log the clock state at power-up and
  power-down.
- A coupling resonance at 20 Hz costs −11.1 dB at 10 Hz; installation response is
  measured or unknown, never assumed.
- A tilt of 0.2 arcsec imitates $10^{-6}\ \mathrm{m/s^{2}}$; tilt usually sets the
  horizontal long-period floor.
- Record the irreversible items first.

## 9. Python demonstration

[`code/seismic_deployment_demo.py`](./code/seismic_deployment_demo.py) prints every
number quoted above. It:

1. tabulates the transverse-to-radial leakage and the fast-direction bias for
   seven orientation errors;
2. computes the expected lock-loss statistics for a 30-station, 20-day deployment
   and the drift accumulated at four fractional clock errors;
3. evaluates a synthetic coupling resonance from 1 to 80 Hz;
4. tabulates the apparent horizontal acceleration for six tilt angles and inverts
   the relation for three target accelerations.

Run it with the project virtual environment:

```bash
cd 23-field-methods-instruments/02-seismic-instruments-and-fieldwork/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python seismic_deployment_demo.py
```

## 10. Exercises

Worked problem sets are in
[`exercises/05-seismic-deployment-exercises.md`](./exercises/05-seismic-deployment-exercises.md)
and
[`exercises/05-seismic-deployment-solutions.md`](./exercises/05-seismic-deployment-solutions.md).

## 11. Mastery checkpoint

Without notes:

1. An orientation error of 8° is suspected. Compute the transverse-to-radial ratio
   in dB and state whether it could be mistaken for anisotropy.
2. A 40-station deployment runs for 60 days with a per-station-day lock-loss
   probability of 0.02. Compute the expected number of affected stations.
3. A clock with a fractional error of $2\times10^{-6}$ is unlocked for 36 hours.
   Compute the timing error in seconds and in samples at 200 sps.
4. A coupling resonance sits at 15 Hz with damping 0.6. Compute the response
   deviation in dB at 5 Hz.
5. Compute the tilt, in arcseconds, that imitates an apparent horizontal
   acceleration of $5\times10^{-6}\ \mathrm{m/s^{2}}$.
6. Name three metadata items that cannot be recovered after the campaign.

## 12. Common pitfalls

1. **Assuming orientation from the site plan.** The sensor's frame, not the
   planned frame, is what was recorded.
2. **Recording "N" or "north" without a reference or a method.** An orientation
   without its reference is not a measurement.
3. **Trusting the lock indicator.** Verify by comparing the clock against a
   reference and record the difference.
4. **Treating the installation as ideal.** A −11 dB deviation at 10 Hz was
   produced by a resonance only 2× the frequency of interest.
5. **Levelling to the bubble and not recording the residual.** The residual is
   what lets a later analyst decide whether tilt contamination matters.
6. **Doing the paperwork after packing up.** Orientation, coupling and the clock
   state are gone.

## 13. Where this is used

- Every temporary deployment: the metadata produced here is the instrument
  response used by every later analysis.
- Permanent observatory stations, where the same measurements are repeated at
  installation and revisited when the station is upgraded.
- Active-source surveys, where receiver coupling and geometry repeatability
  dominate the data quality.
- Ocean-bottom and borehole deployments, where the equivalent tasks are the
  levelling and heading of the package and the recording of the release and
  landing times.
- Data centres and archives: incomplete station metadata is the most common reason
  a dataset cannot be reprocessed years later — see
  [22-03-06 Metadata Standards and Controlled Vocabularies](../../22-data-engineering-reproducibility/03-data-formats-and-engineering/06-metadata-standards.md).

## 14. Related lessons

- [01 Seismometers: Broadband, Short-Period, Geophones, MEMS](01-seismometers.md) —
  the response the installation modifies.
- [03 Seismic Network Design and Station Siting](03-seismic-network-design.md) —
  where the sites were chosen.
- [06 Field QC: Noise Checks, Continuity, Station Uptime](06-seismic-field-qc.md) —
  how a deployment's failures are detected while there is still time to fix them.
- [23-01-03 Field Notebooks, Metadata and Data Provenance](../01-field-safety-and-planning/03-field-notebooks.md) —
  the record-keeping protocol this lesson instantiates.
- [23-05-03 Timing, GNSS Disciplining and Clock Accuracy](../05-instrumentation-and-electronics/03-timing-and-gnss-instruments.md) —
  the clock side in more depth.

## 15. Self-assessment checklist

- [ ] I can compute orientation leakage and state its effect on anisotropy.
- [ ] I can compute expected lock-loss counts and drift.
- [ ] I can evaluate a coupling resonance deviation.
- [ ] I can convert between tilt and apparent horizontal acceleration.
- [ ] I can list the deployment metadata and mark what is irreversible.
- [ ] I can order the deployment tasks by irreversibility.
