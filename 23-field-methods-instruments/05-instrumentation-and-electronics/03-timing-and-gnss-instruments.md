---
id: 23-05-03
title: "Timing, GNSS Disciplining and Clock Accuracy"
level: graduate
prereqs: ["23-02-05", "07-04-03"]
estimated_minutes: 95
tags: [timing, gnss, clocks, holdover, allan-deviation, instrumentation]
---

# Timing, GNSS Disciplining and Clock Accuracy

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the time a fractional clock error accumulates over any interval, and
   **convert** it into samples and into apparent distance.
2. **Compute** the holdover time a timing budget allows after a loss of lock, and
   **state** the maintenance interval it implies.
3. **Compute** the reduction of pulse-per-second jitter by averaging, and **state**
   what averaging cannot remove.
4. **Compute** the accumulated random time error from a clock's Allan deviation, and
   **distinguish** it from the systematic offset.
5. **Build** a timing budget for a sensor array, and **state** which term dominates.
6. **State** what a clock specification does not tell you and what must be measured.

All fractional errors, holdover stabilities, jitter figures and timing budgets in
this lesson are **SYNTHETIC** teaching values, combined with the standard relations
quoted in the text. No measured oscillator specification and no manufacturer figure
is used or reproduced.

## Prerequisites

- [23-02-05 Deployment, Orientation, Timing and Metadata](../02-seismic-instruments-and-fieldwork/05-seismic-deployment.md) —
  the deployment context for these clocks.
- [07-04-03 GNSS Positioning: Pseudorange, Carrier Phase and Ambiguity Resolution](../../07-gravity-geodesy/04-geodesy-reference-frames/03-gnss-positioning.md) —
  the signal that disciplines the clock.

## 1. Intuition: a clock is a frequency standard first

A clock is an oscillator plus a counter. Its error is therefore a *frequency* error
that accumulates as a *time* error:

$$\delta t = \epsilon\,T,$$

with $\epsilon$ the fractional frequency error and $T$ the elapsed time. Everything
in this lesson follows from that one line, plus the distinction between the error's
**systematic** part (a constant fractional offset, which accumulates linearly and
without bound) and its **random** part (frequency fluctuations, which accumulate as
a random walk and grow only as $\sqrt{T}$).

A global navigation satellite system provides an external reference of very high
long-term accuracy, and a receiver's pulse-per-second output lets a local oscillator
be *disciplined* to it. A disciplined clock has the GNSS's long-term stability and
the local oscillator's short-term stability — until the lock is lost, at which point
it reverts to the oscillator's own performance, which is the **holdover** regime
that every field deployment must plan for.

## 2. Fractional error and accumulated time

| $\epsilon$ | 1 h | 1 day | 30 days | 1 day in samples at 100 sps |
|---|---|---|---|---|
| 1e−6 | 3.6000e−3 s | 8.6400e−2 s | 2.5920 s | 8.6 |
| 1e−7 | 3.6000e−4 s | 8.6400e−3 s | 2.5920e−1 s | 0.9 |
| 1e−8 | 3.6000e−5 s | 8.6400e−4 s | 2.5920e−2 s | 0.1 |
| 1e−9 | 3.6000e−6 s | 8.6400e−5 s | 2.5920e−3 s | 0.0 |

Read the first row against a seismic application: one part per million is 86.4 ms
per day, which at a 3 km/s apparent velocity is

$$\delta R = V\,\delta t = 3.0 \times 10^{3} \times 0.0864 = 259.2\ \mathrm{m}$$

of apparent distance error after a single day. The last row — one part per billion,
which a disciplined oscillator holds — is 86.4 µs per day, or 0.26 m of apparent
distance. **The difference between a free-running crystal and a disciplined
oscillator is four orders of magnitude in timing error, and it is the difference
between a usable and an unusable array.**

## 3. Holdover: the arithmetic a deployment plan needs

After the lock is lost, the clock drifts at its holdover rate. The time a given
timing budget survives is

$$T_{\text{holdover}} = \frac{\text{budget}}{\epsilon_{\text{holdover per unit time}}}.$$

For a 1 ms budget:

| Holdover (per day) | Drift per day | Days to exhaust the budget |
|---|---|---|
| 1e−5 | 864 000 µs | 0.0 |
| 1e−6 | 86 400 µs | 0.0 |
| 1e−7 | 8 640 µs | 0.1 |
| 1e−8 | 864 µs | 1.2 |
| 1e−9 | 86.4 µs | 11.6 |

The last row is the *maintenance re-visit interval*: at a 1e−9 holdover and a 1 ms
budget, a station can be left alone for about eleven days before its timing has
drifted out of specification. That number belongs in the deployment plan next to
the battery life, and it usually turns out to be the binding constraint on how long
a station can be left unattended.

The planning rules:

1. **Measure the holdover, do not assume it.** The oscillator's specification is
   taken under particular conditions (temperature, ageing, supply); a station in a
   cold vault or a hot enclosure is not those conditions.
2. **Log the lock state and the clock offset** at every opportunity, so the holdover
   interval is *known* rather than inferred (see
   [23-02-05 Deployment, Orientation, Timing and Metadata](../02-seismic-instruments-and-fieldwork/05-seismic-deployment.md)).
3. **Budget for the worst case** — a lost lock at the start of the deployment, not
   in the middle.
4. **Use the GNSS where it is available** and plan the holdover for where it is not;
   the two regimes have different requirements and should be reported separately.

## 4. Pulse-per-second jitter

A GNSS receiver's pulse-per-second (PPS) output has jitter — tens of nanoseconds rms
is typical of a good receiver — and a time-interval counter measures the offset
between the PPS and the local clock. Averaging $N$ pulses reduces the random part:

$$\sigma_{\text{eff}} = \frac{\sigma_{\text{PPS}}}{\sqrt{N}} .$$

With 20 ns rms:

| $N$ averaged | Effective jitter | Time error per day |
|---|---|---|
| 1 | 20.000 ns | 1728.000 µs |
| 10 | 6.325 ns | 546.417 µs |
| 100 | 2.000 ns | 172.800 µs |
| 1 000 | 0.632 ns | 54.642 µs |
| 10 000 | 0.200 ns | 17.280 µs |

(Note that the third column is the *jitter* integrated over a day, not a drift: a
jitter of 20 ns on each measurement does not accumulate as a frequency error, and
the column is there to show the scale, not a physical accumulation. The honest
statement is that jitter affects each comparison, while a frequency offset
accumulates.)

**What averaging cannot remove** is a constant offset between the PPS and the true
second — the receiver's own delay, the antenna cable delay and the receiver's
internal processing. That offset must be *calibrated* against a reference (a
time-transfer service, a co-located receiver with a known delay, or a
round-trip calibration), and it is a systematic error of the same order as the
jitter: tens of nanoseconds, which is 3 m of apparent distance at a 100 m/s
apparent velocity.

## 5. Allan deviation: how good is the oscillator?

The Allan deviation $\sigma_y(\tau)$ describes the fractional frequency instability
averaged over an interval $\tau$. For white frequency noise it falls as
$\tau^{-1/2}$:

$$\sigma_y(\tau) = \frac{\sigma_y(1\ \mathrm{s})}{\sqrt{\tau/1\ \mathrm{s}}} ,$$

so with $\sigma_y(1\ \mathrm{s}) = 1\times10^{-11}$:

| $\tau$ (s) | 1 | 10 | 100 | 1 000 | 10 000 |
|---|---|---|---|---|---|
| $\sigma_y(\tau)$ | 1.0000e−11 | 3.1623e−12 | 1.0000e−12 | 3.1623e−13 | 1.0000e−13 |

The accumulated *random* time error over an interval $T$ is

$$\sigma_x(T) = \sigma_y(1\ \mathrm{s})\sqrt{T \cdot 1\ \mathrm{s}} ,$$

which for $T = 86\,400$ s gives $2.9394\times10^{-9}$ s = **2.94 ns**. Compare that
with the *systematic* offset over the same day, $\epsilon T = 10^{-11} \times 86\,400
= 8.64\times10^{-7}$ s = **0.864 µs** — nearly 300 times larger.

The lesson is important enough to state plainly: **the random stability of a good
oscillator is not the limiting factor; its offset is.** Averaging more does not
remove an offset, which is why a clock comparison must be calibrated against a
reference and why a disciplined clock (whose offset is continually corrected) is so
much better than a free-running one.

## 6. A timing budget

| $\delta t$ | Apparent distance at 3 km/s | Holdover days at 1e−9 |
|---|---|---|
| 1e−6 s | 0.003 m | 0.01 |
| 1e−4 s | 0.300 m | 1.16 |
| 1e−3 s | 3.000 m | 11.57 |
| 1e−2 s | 30.000 m | 115.74 |
| 1e−1 s | 300.000 m | 1157.41 |

A timing budget is built from the science requirement, in this order:

1. **State the required relative timing** between the stations or the channels: for
   an array used for beamforming or relative location, 1 ms is a common requirement;
   for absolute location with a regional network, tens of milliseconds may be
   acceptable; for a global array working at teleseismic distances, the requirement
   is tighter again.
2. **Convert it into an apparent distance** at the relevant velocity, which is what
   makes the requirement meaningful to a non-specialist.
3. **Allocate it** among the terms: the GNSS lock's own accuracy, the holdover after
   a lock loss, the counter resolution, and the delay calibration.
4. **Derive the maintenance interval** from the holdover term (Section 3), and check
   it against the other logistics.
5. **Verify it in the field** with a common-view or a direct comparison at a site
   visit, and record the result.

## 7. Assumptions and regime of validity

1. **A single fractional error.** Real oscillators have ageing, temperature and
   supply sensitivity, and a frequency-versus-time curve that is not a straight
   line; the linear model holds over the intervals where the clock is stable.
2. **Holdover measured under the deployment conditions.** The specification's
   temperature range is not the enclosure's.
3. **Independent jitter samples.** Correlated jitter (multipath, ionospheric
   scintillation) does not average as $\sqrt{N}$.
4. **White frequency noise for the $\tau^{-1/2}$ scaling.** Real oscillators turn up
   at long $\tau$ (ageing, 1/f drift) and down at short $\tau$ (white phase noise);
   the Allan deviation's *shape* must come from the device's own data.
5. **The GNSS time is exact.** GNSS time is a realisation of a national or
   international time scale with its own offsets; for sub-microsecond work the
   reference's own accuracy and the receiver's calibration matter.
6. **The counter resolves the budget.** A time-interval counter with a 10 ns
   resolution cannot verify a 1 ns requirement, and a counter's own internal clock
   must be disciplined or the measurement is circular.

## 8. The honest summary

- $\delta t = \epsilon T$: 1 ppm is 86.4 ms/day, which is 259 m of apparent distance
  at 3 km/s.
- A 1e−9 holdover with a 1 ms budget sets an 11.6-day re-visit interval.
- Averaging reduces PPS jitter as $\sqrt{N}$ and never removes an offset.
- Random accumulated error is 2.94 ns/day for a 1e−11 oscillator; its systematic
  offset is 864 ns/day — the offset dominates.
- Build the budget from the science requirement, allocate it, and verify it in the
  field.

## 9. Python demonstration

[`code/timing_and_gnss_demo.py`](./code/timing_and_gnss_demo.py) prints every number
quoted above. It:

1. tabulates the accumulated time for four fractional errors over three intervals;
2. tabulates the holdover time a 1 ms budget allows for five holdover rates;
3. computes the effect of averaging PPS jitter over five counts;
4. tabulates the Allan deviation for five averaging times and compares random and
   systematic accumulation over a day;
5. converts five timing errors into apparent distances and holdover days.

Run it with the project virtual environment:

```bash
cd 23-field-methods-instruments/05-instrumentation-and-electronics/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python timing_and_gnss_demo.py
```

## 10. Exercises

Worked problem sets are in
[`exercises/03-timing-and-gnss-instruments-exercises.md`](./exercises/03-timing-and-gnss-instruments-exercises.md)
and
[`exercises/03-timing-and-gnss-instruments-solutions.md`](./exercises/03-timing-and-gnss-instruments-solutions.md).

## 11. Mastery checkpoint

Without notes:

1. A clock has a fractional error of 2.5e−7. Compute the time error after 6 h and
   after 15 days, and the apparent distance at a 2.5 km/s velocity after 6 h.
2. A station's holdover is 5e−8 per day. Compute the days a 0.5 ms budget survives.
3. PPS jitter is 30 ns and 400 pulses are averaged. Compute the effective jitter.
4. An oscillator has $\sigma_y(1\ \mathrm{s}) = 5\times10^{-12}$. Compute
   $\sigma_y(1000\ \mathrm{s})$ and the random accumulated error over one day.
5. State the two parts of a clock's error and which one a comparison must remove.

## 12. Common pitfalls

1. **Assuming the holdover specification applies in the field enclosure.** It is a
   temperature-dependent quantity.
2. **Averaging to remove an offset.** It cannot be done.
3. **Quoting the oscillator's stability when the counter's resolution is worse.**
4. **Forgetting the antenna cable delay and the receiver's own delay.** They are
   tens of nanoseconds of systematic offset.
5. **Planning the battery life and not the timing holdover.** The holdover is often
   the shorter interval.
6. **Not logging the lock state.** Without it the holdover interval is unknown.
7. **Treating GNSS time as exact.** Sub-microsecond work needs the reference's own
   accuracy.

## 13. Where this is used

- Temporary seismic arrays, where relative timing between stations is the
  requirement that decides the deployment duration.
- Ocean-bottom and borehole deployments, where the clock is inaccessible for months
  and the holdover is the dominant risk.
- Active-source surveys with independent recorders, where the shot time is the
  common reference and the receivers must hold it.
- Distributed acoustic sensing, where the interrogator's clock sets the timing for
  thousands of channels at once.
- Any monitoring network whose data are compared with another network's, where the
  common time base is the tie.

## 14. Related lessons

- [23-02-05 Deployment, Orientation, Timing and Metadata](../02-seismic-instruments-and-fieldwork/05-seismic-deployment.md) —
  where these clocks are deployed and logged.
- [23-02-06 Field QC: Noise Checks, Continuity, Station Uptime](../02-seismic-instruments-and-fieldwork/06-seismic-field-qc.md) —
  how a timing failure is detected during a campaign.
- [04 Calibration, Testing and Traceability](04-calibration-and-testing.md) —
  how a clock's performance is established against a reference.
- [07-04-03 GNSS Positioning: Pseudorange, Carrier Phase and Ambiguity Resolution](../../07-gravity-geodesy/04-geodesy-reference-frames/03-gnss-positioning.md) —
  the positioning side of the same receiver.
- [03-10-03 StationXML Inventory, Response and Instrument Correction](../../03-scientific-computing/10-obspy-and-seismic-data/03-inventory-and-metadata.md) —
  where the clock state is recorded.

## 15. Self-assessment checklist

- [ ] I can compute accumulated time from a fractional error.
- [ ] I can compute a holdover interval from a timing budget.
- [ ] I can reduce PPS jitter by averaging and say what it cannot remove.
- [ ] I can compute Allan-deviation scaling and random accumulation.
- [ ] I can build and allocate a timing budget.
- [ ] I can state which term dominates and what must be measured.
