---
id: 23-07-04
title: "Case Study: A Marine Geophysical Cruise"
level: research
prereqs: ["23-07-03", "15-02-01"]
estimated_minutes: 115
tags: [case-study, marine, seismic-acquisition, streamer, cruise-planning, qc]
---

# Case Study: A Marine Geophysical Cruise

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the record length and the cable length a target depth requires, with the
   migration tail.
2. **Compute** a CDP fold from cable and shot geometry, and **state** what fold buys and what
   it does not.
3. **Compute** a cruise schedule: line kilometres, sail speed, turns, transit and weather
   downtime.
4. **Compute** the data volume and **compare** it with the vessel's day rate, and **state**
   which is the budget.
5. **Compute** the cross-line displacement a feather angle produces at each offset, and
   **choose** a tolerance from the cost of rejecting shots.
6. **Design** the at-sea QC that detects the three failures that actually occur, and
   **state** the deliverables the cruise cannot produce.

All numbers here are **SYNTHETIC** teaching values combined with the standard relations quoted
in the text (two-way travel time, the CDP fold relation, sail-speed and shot-interval
arithmetic, streamer feathering geometry, data-rate arithmetic). No real cruise, vessel,
operator, vendor figure or measured dataset is reproduced.

## Prerequisites

- [23-07-03 Case Study: A Magnetotelluric Campaign](03-case-study-mt-campaign.md) —
  the campaign-planning arithmetic at a fixed site.
- [15-02-01 Marine Seismic Reflection: Sources, Streamers and Processing](../../15-oceanography-marine/02-marine-geophysics-methods/01-marine-seismic-reflection.md) —
  the acquisition method this cruise executes.

## 1. The requirement, and the two numbers it fixes immediately

A synthetic cruise must **image a target at about 2 km below the seafloor** with a resolution
of a few tens of metres, over a 2400 line-km survey area. Two parameters follow from the depth
before anything else is decided:

$$t_{\text{two-way}} = \frac{2z}{v_{\text{rms}}}
= \frac{2 \times 2000}{2500} = 1.600\ \mathrm{s},$$

$$t_{\text{record}} = t_{\text{two-way}} + t_{\text{tail}} = 1.600 + 1.0
= 2.60\ \mathrm{s},$$

where the migration tail is the extra recording time that lets the deeper diffractions focus
rather than wrap around. The cable must be long enough to record the moveout the velocity
analysis needs, conventionally about 1.4× the target depth in far offset:

| Depth | Two-way time | Record length | Far offset |
|---|---|---|---|
| 0.5 km | 0.4000 s | 1.400 s | 700 m |
| 1.0 km | 0.8000 s | 1.800 s | 1400 m |
| **2.0 km** | **1.6000 s** | **2.600 s** | **2800 m** |
| 3.0 km | 2.4000 s | 3.400 s | 4200 m |
| 5.0 km | 4.0000 s | 5.000 s | 7000 m |

**These two numbers are booked, not adjusted.** The record length sets the shot cycle and hence
the achievable shot density, and the far offset sets the cable length; both are fixed when the
vessel and the spread are contracted, and neither can be changed at sea except by shortening
the record (which destroys the deep target) or dropping cable sections (which reduces the
velocity information).

## 2. Fold, binning, and what each one buys

The CDP fold of a 2-D line with $N$ channels at group interval $\Delta g$ and shot interval
$\Delta s$ is

$$F = \frac{N\Delta g}{2\Delta s} , \qquad \text{bin} = \frac{\Delta g}{2} ,$$

so 240 channels at 12.5 m with shots every 25 m give a 3.00 km cable, a 6.25 m bin and a
**60-fold** section:

| Channels | Cable | Shot interval | Fold | Bin |
|---|---|---|---|---|
| 120 | 1.50 km | 25 m | 30.0 | 6.25 m |
| **240** | **3.00 km** | **25 m** | **60.0** | **6.25 m** |
| 480 | 6.00 km | 25 m | 120.0 | 6.25 m |
| 480 | 6.00 km | 12.5 m | 240.0 | 6.25 m |

Three distinctions that decide the specification:

1. **Fold buys signal-to-noise, not resolution.** The bin size (set by the group interval) and
   the source signature set the resolution; doubling the fold halves the random-noise level but
   leaves the wavelet unchanged. For a target that is *noisy* (deep, below a rough seafloor, in
   a high-velocity cover) fold is the parameter to raise; for a target that is *thin*, it is not.
2. **Shot density and fold trade against time.** Halving the shot interval doubles the fold and
   doubles the time per line kilometre; with a 10.8 s shot cycle at 4.5 knots, the survey can
   only get so dense before the schedule collapses.
3. **The 3.00 km cable and the 2800 m far offset agree to 7 %.** That is not a coincidence: the
   cable was chosen from the offset rule, and a design in which the cable is shorter than the
   rule is a design that cannot invert for velocity below the target depth — a statement to make
   explicit, because the velocity model is what the depth conversion rests on.

## 3. The schedule

With 40 lines of 60 km, a sail speed of 4.5 knots (2.315 m/s = 8.33 km/h) and a 0.5 h turn per
line:

| Item | Value |
|---|---|
| Line kilometres | 2400 |
| Per line | 7.20 h steaming + 0.5 h turn |
| Survey time | 308.0 h = 12.83 days |
| With 20 % weather downtime | 15.40 days |
| Plus 144 h transit | **21.40 days** |

and the shot count is 96 000 at a 25 m interval, i.e. one shot every **10.80 s**.

The two terms that plans most often omit are the **turn** and the **transit**:

- **Turns** are 40 × 0.5 h = 20 h here, 6.5 % of the steaming time — small, but they are also
  the time when the streamer is most vulnerable and when the next line's start is set up, so
  the realistic figure is higher than the geometric one.
- **Transit** is 144 h — nearly half as long as the survey itself for this synthetic area, and
  it is entirely determined by the port, not by the science. Choosing the port is therefore a
  schedule decision of the same order as the line spacing.

**Weather downtime is not a contingency.** A 20 % figure applied to the survey time is the
*expected* loss; the plan should also state the loss it can absorb before the science fails —
here, losing the deepest lines is the acceptable degradation, and the priority order of the
lines is part of the plan.

## 4. Data volume and the real budget

With a 2.60 s record at 4.0 ms sampling (650 samples per trace), 240 traces per shot and 96 000
shots:

$$240 \times 650 \times 4\ \mathrm{B} = 0.6240\ \mathrm{MB\ per\ shot},
\qquad 96\,000 \times 0.6240 = \mathbf{59.9\ GB} ,$$

| Day rate (k units) | 20 days | 30 days | 40 days |
|---|---|---|---|
| 50 | 1000 | 1500 | 2000 |
| 100 | 2000 | 3000 | 4000 |
| 200 | 4000 | 6000 | 8000 |

So the *whole archive* is 59.9 GB — a single modern disk — while 30 days of vessel time is 3000 k
units at the synthetic day rate of 100. **Every hour of schedule slippage costs more than the
entire dataset is worth in storage**, which is the defining economic fact of marine acquisition
and the reason the plan optimises days, not file size.

Two consequences for the science:

1. **Do not trade daytime for volume.** Continuous recording, generous record length and full
   trace density are nearly free compared with the ship; the temptation to save crew or disk
   space at sea is almost always wrong.
2. **Reserve budget for the processing, not only the acquisition.** The processing is where the
   velocity model, the multiple removal and the depth conversion happen, and a cruise that
   consumes its whole budget at sea produces a dataset nobody can finish.

## 5. Feathering, positioning and the at-sea QC

A streamer is towed, so it never lies straight: the **feather angle** between the cable and the
ship's track displaces every offset cross-line by

$$\Delta y = x\sin\alpha ,$$

| Offset | 2° | 5° | 10° | 15° |
|---|---|---|---|---|
| 600 m | 20.9 m | 52.3 m | 104.2 m | 155.3 m |
| 1500 m | 52.3 m | 130.7 m | 260.5 m | 388.2 m |
| 3000 m | 104.7 m | 261.5 m | 520.9 m | 776.5 m |
| 6000 m | 209.4 m | 522.9 m | 1041.9 m | 1552.9 m |

so the *far offsets* of a feathered line illuminate a corridor more than a kilometre wide — good
for some 3-D geometries and bad for a 2-D line whose assumption is that everything lies in the
vertical plane. The synthetic feathering over a line has a mean of 3.97° and a standard deviation
of 1.99°, and the tolerance chosen decides how much data survives:

| Tolerance | Shots rejected |
|---|---|
| 6° | 15.58 % |
| 8° | 1.79 % |
| 10° | 0.12 % |
| 12° | 0.00 % |

The design point is that a tolerance is a **cost decision**, not a quality preference: rejecting
16 % of a line to hold 6° costs a schedule day, while accepting 12° keeps everything at the price
of a cross-line smearing that the processing must then handle.

The QC that actually matters at sea is short, and it is about detecting failures early enough to
fix them:

1. **Navigation and feathering** per shot: the actual shot point, the cable shape and the
   feather angle, logged continuously and checked against tolerance, because a positioning
   failure invalidates the geometry and cannot be fixed later.
2. **Source and receiver signatures** from a daily far-field or gun-array check: a misfiring
   element changes the wavelet and hence the resolution claim.
3. **Noise and environmental check**: a spectral check per day (streamer noise, swell noise,
   interference from other vessels), because a rise in noise can be seen in time to change the
   survey's weather limits or the line priority.
4. **Fold and bin coverage** daily, so that a gap (from a turn, a weather loss or a go-around)
   is found while the vessel is still on station rather than in the processing shop.
5. **A repeat line** (a short line acquired twice) to measure the true repeatability of the
   measurements — the marine analogue of the ERT reciprocal check, and the only direct evidence
   for a 4-D (time-lapse) claim.

## 6. Assumptions and regime of validity

1. **The rms velocity is known well enough for the record length.** It is not: the record length
   is deliberately generous because the velocity comes from the survey itself. The margin (1.0 s
   here) is the defence.
2. **The seafloor and the water velocity are simple.** A hard or irregular seafloor scatters
   energy and creates the multiples the processing must remove; a variable water velocity adds a
   depth-dependent time shift.
3. **The cable is straight enough for the 2-D assumption.** §5 quantifies the violation, and the
   processing must either correct it (binning by midpoint) or accept the smear.
4. **The day-rate model is linear.** Standby, mob/demob and port costs are not, so the plan's
   cost comparison is a comparison of *days*, not of money.
5. **Weather downtime is stationary.** It is strongly seasonal; a plan built on a summer average
   applied to a winter window is not conservative.
6. **The target's resolution claim is achievable by the source and bin.** A few tens of metres
   from a 6.25 m bin requires the processing chain to preserve the bandwidth, which is a
   processing claim as much as an acquisition one.

## 7. The honest summary

- The depth set the record (2.60 s) and the cable (3.00 km for a 2800 m far offset) before
  anything else; both are contract decisions.
- 240 channels at 12.5 m with 25 m shots is a 60-fold, 6.25 m-bin section; **fold buys
  signal-to-noise, not resolution**.
- 2400 line km at 4.5 knots is 12.83 days of survey, 15.40 with 20 % weather, 21.40 with
  transit; turns and transit are the terms most often omitted.
- The whole dataset is **59.9 GB** while 30 days of vessel time is 3000 k units: schedule risk is
  the financial risk, and the archive is never the constraint.
- Feathering displaces a 3000 m offset by 261.5 m at 5° and 520.9 m at 10°; a 6° tolerance
  rejects 15.58 % of a line and a 12° tolerance nothing.
- The at-sea QC that matters: geometry and feathering, signatures, noise, coverage, and a repeat
  line.

## 8. Python demonstration

[`code/case_study_marine_cruise_demo.py`](./code/case_study_marine_cruise_demo.py) prints every
number quoted above: the record-length and offset table, the fold and bin table, the schedule
with transit and weather, the data volume against synthetic day rates, and the feathering
geometry with a seeded feather-angle distribution and its rejection fractions.

```bash
cd 23-field-methods-instruments/07-field-campaign-case-studies/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python case_study_marine_cruise_demo.py
```

## 9. Exercises

Worked problem sets are in
[`exercises/04-case-study-marine-cruise-exercises.md`](./exercises/04-case-study-marine-cruise-exercises.md)
and
[`exercises/04-case-study-marine-cruise-solutions.md`](./exercises/04-case-study-marine-cruise-solutions.md).

## 10. Mastery checkpoint

Without notes:

1. For a 3 km target at 2200 m/s, compute the two-way time, a record length with a 0.8 s tail and
   the far offset from the 1.4× rule.
2. For 360 channels at 12.5 m and a 20 m shot interval, compute the cable length, the fold and
   the bin.
3. Compute the survey time for 30 lines of 45 km at 5.0 knots with a 0.4 h turn per line, then
   add 25 % weather and 100 h of transit.
4. Compute the data volume for 70 000 shots with 360 traces of 800 samples at 4 bytes.
5. Compute the cross-line displacement at a 2400 m offset for feather angles of 3°, 7° and 12°.

## 11. Common pitfalls

1. **Shortening the record to save space.** The tail is what focuses the target.
2. **Buying fold for resolution.** It buys signal-to-noise.
3. **Omitting turns and transit from the schedule.** Together they dominated this plan's transit
   leg.
4. **Treating weather as a contingency rather than an expectation.** It is expected; the plan
   states what it can absorb.
5. **A feather tolerance with no cost attached.** Every tolerance rejects shots and therefore
   days.
6. **Optimising storage at sea.** The archive is 60 GB against a vessel day rate of thousands.
7. **No repeat line.** Without one, the repeatability claim is unsupported.

## 12. Where this is used

- Exploration and site-characterisation cruises in any water depth — see
  [15-02-01 Marine Seismic Reflection: Sources, Streamers and Processing](../../15-oceanography-marine/02-marine-geophysics-methods/01-marine-seismic-reflection.md).
- 4-D (time-lapse) monitoring, where the repeat line and the geometry repeatability are the whole
  design.
- Academic and survey-vessel programmes, where the same arithmetic is applied to a shared
  vessel schedule.
- Any acquisition whose platform moves and whose budget is measured in days.

## 13. Related lessons

- [03 Case Study: A Magnetotelluric Campaign](03-case-study-mt-campaign.md) —
  where the schedule is set by coherence rather than by a moving platform.
- [02 Case Study: An ERT Survey from Design to Report](02-case-study-ert-survey.md) —
  the land analogue of geometry-first design.
- [23-02-03 Seismic Network and Array Design](../02-seismic-instruments-and-fieldwork/03-seismic-network-design.md) —
  the array geometry arithmetic that the fold relation parallels.
- [15-02-01 Marine Seismic Reflection: Sources, Streamers and Processing](../../15-oceanography-marine/02-marine-geophysics-methods/01-marine-seismic-reflection.md) —
  the processing chain the acquisition must feed.

## 14. Self-assessment checklist

- [ ] I can compute a record length and a cable length from a target depth.
- [ ] I can compute a fold and a bin and state what each buys.
- [ ] I can build a cruise schedule including turns, transit and weather.
- [ ] I can compare the data volume with the vessel cost and name the budget.
- [ ] I can compute feathering displacement at each offset.
- [ ] I can specify the at-sea QC and the repeat line.
- [ ] I can state what the cruise cannot produce.
