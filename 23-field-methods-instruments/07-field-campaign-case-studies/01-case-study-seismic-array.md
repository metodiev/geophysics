---
id: 23-07-01
title: "Case Study: Deploying a Temporary Seismic Array"
level: research
prereqs: ["23-02-03", "23-05-06", "23-06-08"]
estimated_minutes: 115
tags: [case-study, seismic-array, deployment, logistics, resolution, availability]
---

# Case Study: Deploying a Temporary Seismic Array

## Learning objectives

By the end of this lesson you will be able to:

1. **Turn** a science requirement into an aperture, a station count and a station spacing,
   and **state** which of the three binds.
2. **Compute** the installation workload in station-hours and person-days, and **show** how
   the crew size changes the schedule but not the labour.
3. **Compute** the data volume, the archive and the download bench the campaign needs.
4. **Compute** the power budget and the visit plan, and **state** which visit is for the
   battery and which for the data.
5. **Compute** the availability and the *delivered* resolution after failures, and **state**
   the value of deploying spare stations up front.
6. **State** the four decisions that this campaign could not defer, and why.

All numbers here are **SYNTHETIC** teaching values combined with the standard relations
quoted in the text (array resolution and aliasing, data-rate arithmetic, duty-cycle power
budgets, binomial availability, person-day accounting). No real campaign, institution,
instrument or measured dataset is reproduced.

## Prerequisites

- [23-02-03 Seismic Network and Array Design](../02-seismic-instruments-and-fieldwork/03-seismic-network-design.md) —
  the array theory this lesson applies.
- [23-05-06 IoT and Autonomous Sensor Networks](../05-instrumentation-and-electronics/06-iot-sensor-networks.md) —
  the power, airtime and availability arithmetic used here.
- [23-06-08 Laboratory Uncertainty Budgets and Reporting](../06-laboratory-measurements/08-lab-data-uncertainty.md) —
  the reporting discipline the deliverables follow.

## 1. The requirement

A synthetic monitoring campaign is asked for one thing: **resolve a structure of about 1 km
lateral extent at 10 km depth**, using a surface array and ambient-noise or local-event
energy whose dominant wavelength at the target is about 2 km. Everything else in this lesson
follows from that sentence, and the sentence is unusually well posed — a requirement that
names a resolution, a depth and a wavelength can be turned into a design; a requirement that
names an instrument cannot.

## 2. From the requirement to the array geometry

The array's lateral resolution for a beamforming or migration estimate is set by the aperture
$D$ and the wavelength:

$$R \approx \frac{\lambda z}{D}
\qquad\Longrightarrow\qquad
D = \frac{\lambda z}{R} = \frac{2000 \times 10\,000}{1000} = 20\ \mathrm{km} .$$

The station *spacing* is set independently, by aliasing: a spacing $d$ misrepresents
wavelengths shorter than $2d$, so

$$d \le \frac{\lambda_{\min}}{2} = \frac{2000}{2} = 1000\ \mathrm{m} .$$

Together these fix the array:

| Aperture | Max spacing | Stations |
|---|---|---|
| 20 km | 1000 m | **21** |

and the table the demonstration prints shows why the two criteria must be stated separately:
varying the station count while holding the aperture fixed changes the redundancy and the
aliasing margin but **not** the resolution, which is why "we need more stations" and "we need
a better resolution" are different requests with different costs.

The 21-station design has *no* margin: the spacing is exactly at the aliasing limit, so one
lost station creates a 2 km gap and a local aliasing hole. The honest design therefore
specifies the spacing from a fraction of the limit — 500 m would give 41 stations for the
same aperture at a doubling of the installation cost — and states which the budget allows.

## 3. The installation workload

With a synthetic 3.0 h per station and a three-person crew:

| Item | Value |
|---|---|
| station-hours | $21 \times 3.0 = 63.0$ |
| person-days | $63 \times 3/8 = 23.6$ |
| 1 crew (2.7 stations/day) | 8 days to install |
| 2 crews (5.3 stations/day) | 4 days |
| 3 crews (8.0 stations/day) | 3 days |

**The labour is constant and the schedule is not.** Two crews halve the calendar time and
double the transport, accommodation and supervision cost; the trade is decided by whether the
weather window or the crew cost is the binding constraint, and it is the *campaign's* first
real decision. Two further items belong in the workload and are usually underestimated:
**site surveys and permissions** (a day per station in populated or protected terrain, and
they must precede the installation, not run parallel to it) and **the retrieval and download
visit**, which costs the same as the installation and is the only one that can be scheduled
against the data deadline.

## 4. Data volume and the archive

With 100 Hz, three components and four bytes per sample, one station produces 9.6 kbit/s, so

$$21 \times 60\ \mathrm{days} \times 103.68\ \mathrm{MB/day} = 130.64\ \mathrm{GB}
\text{ raw}, \qquad 43.55\ \mathrm{GB} \text{ at } 3\!:\!1 ,$$

and one 4 TB disk holds **92 repeats** of the whole campaign. The archive is therefore never
the constraint; three things that follow from the arithmetic are:

1. **The download bench is the constraint.** Reading 21 stations' media takes hours per
   station, so plan the bench, the number of readers and the disk staging — and keep the
   media until the data are verified twice, not once.
2. **Store losslessly and never decimate in the field.** With this much headroom there is no
   justification for throwing away bandwidth in a campaign whose resolution depends on it.
3. **Archive the metadata with the data**, at the same time: the station coordinates as
   *measured*, the sensor orientation, the gain, the clock discipline and the visit log. A
   volume of waveforms without its geometry is not a dataset.

## 5. Power and the visit plan

With a synthetic 25 µA sleep current, 30 mA acquisition and 150 mA transmit, a 1/6 acquisition
duty cycle and 20 s of transmission per day:

$$\bar I = 25\ \mathrm{\mu A} + \frac{30\ \mathrm{mA}}{6}
+ \frac{150\ \mathrm{mA} \times 20}{86\,400} = 5.060\ \mathrm{mA},$$

and a 40 Ah battery with 70 % usable gives **230.6 days** — far beyond the 60-day deployment:

| Duty | $\bar I$ | Life | Visits in 60 days |
|---|---|---|---|
| continuous | 30.060 mA | 38.81 days | 2 |
| 1/2 | 15.060 mA | 77.47 days | 1 |
| 1/6 | 5.060 mA | 230.58 days | 1 |
| 1/24 | 1.310 mA | 890.77 days | 1 |

So the campaign's single visit is **for the data, not for the battery** — and that is a risk,
not an economy: a defective cell, a flooded connector or a stuck disk is not discovered until
the last day, and the 1/6 duty cycle means only one sixth of the campaign's possible data
exists. The remedies are the ones the campaign must choose between *before* mobilisation: a
higher duty cycle with a second visit (77.47 days of life at 1/2 duty still covers the
deployment with one visit, and doubles the data), continuous acquisition with two visits, or
a daily telemetry heartbeat that reports battery and health for the cost of a few seconds of
airtime.

The demonstration's `continuous` row is the honest counter-example: at full duty the battery
dies at 38.81 days, so a 60-day continuous campaign needs either a bigger battery, a mid-term
visit, or mains/solar power — and a campaign that discovers this in the field has lost the
second half of its data.

## 6. What the campaign actually delivers

Per-station survival is never 100 %, and the synthetic assumption of 0.90 combined with
6 days lost to access gives

| Quantity | Planned | Delivered |
|---|---|---|
| Stations | 21 | 18.90 expected |
| Station-days | 1134 | 1021 (90.0 %) |
| Aperture | 20.0 km | 18.0 km |
| Resolution cell | 1000 m | **1064 m** |

Two consequences that decide the campaign's scientific value:

1. **A failure is a resolution loss, not just a data loss.** Two missing stations cost about
   106 m of resolution — 10.6 % — and the loss is *systematic* if the failures are clustered
   (a whole ridge, a landowner, a river), because the aperture becomes asymmetric as well as
   smaller.
2. **Two spare stations are cheap insurance.** Deploying 23 instead of 21 costs two sites of
   installation (about 6 station-hours, or 2.2 person-days) and buys back the aperture of the
   expected failures. The comparison to make in the plan is that against the cost of an extra
   field visit or of a *failed* science requirement.

## 7. The four decisions that could not be deferred

Every campaign has decisions that are cheap at the planning stage and impossible later:

1. **The aperture.** It is set by the land access and the array's extent, and no amount of
   post-processing recovers resolution the geometry never had.
2. **The station spacing relative to the aliasing limit.** A spacing at the limit leaves no
   margin for the stations that fail.
3. **The sensor orientation and its measurement.** A three-component station whose
   orientation is unknown post-mobilisation is a one-component station plus a puzzle.
4. **The duty cycle and the visit schedule**, because they set both the data volume and the
   failure detection; and the **metadata plan**, because the geometry is unrecoverable once
   the markers are gone.

## 8. Assumptions and regime of validity

1. **The wavelength and the depth are known before the design.** $R \approx \lambda z/D$ is a
   rule of thumb whose constant depends on the estimator, the noise field and the array
   shape; it is a design guide, not a guarantee, and the honest plan quotes a synthetic-test
   resolution from the actual geometry.
2. **The array is planar and the noise is not directional.** A strong directional source (a
   road, a pump, a river) biases the array response, and no aperture fixes it.
3. **The station-hour estimate holds.** Site conditions, access, frozen ground and landowner
   negotiations dominate this number; it is the first thing to be re-estimated on the
   reconnaissance.
4. **Survival is independent.** Clustered failures (a fire, a flood, a firmware update) make
   the binomial estimate optimistic — the honest model adds a common-cause term.
5. **The duty cycle is achievable with the power available**, including cold nights and
   degraded cells; the budget is a target until the first deployment confirms it.
6. **The science can use 90 % of the planned station-days.** If the inversion needs a
   minimum count, the availability calculation must be done against *that* threshold, not
   against the mean.

## 9. The honest summary

- One sentence — 1 km at 10 km depth, λ = 2 km — fixed the array: a 20 km aperture from
  $R = \lambda z/D$ and a 1000 m spacing from the aliasing limit, i.e. 21 stations.
- Resolution and aliasing are separate constraints, and only the aperture fixes the
  resolution.
- 21 stations × 3 h is 63 station-hours, 23.6 person-days; the crew size changes the calendar
  (8, 4 or 3 days) and not the labour.
- The data volume is 130.64 GB raw and 43.55 GB compressed; one 4 TB disk holds 92 repeats,
  so the download bench, not the archive, is the constraint.
- A 1/6 duty cycle gave 230.6 days of battery life, so the single visit is for the data; at
  continuous duty the battery dies at 38.81 days.
- With 0.90 survival the array delivers 18.90 stations, a 18.0 km aperture and a 1064 m
  resolution cell — 10.6 % worse than designed.
- The aperture, the spacing margin, the sensor orientation and the duty cycle are the four
  decisions that cannot be deferred.

## 10. Python demonstration

[`code/case_study_seismic_array_demo.py`](./code/case_study_seismic_array_demo.py) prints
every number quoted above: the geometry from the requirement, the workload table, the volume
and archive, the power and visit plan, and the delivered availability with its resolution
consequence.

```bash
cd 23-field-methods-instruments/07-field-campaign-case-studies/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python case_study_seismic_array_demo.py
```

## 11. Exercises

Worked problem sets are in
[`exercises/01-case-study-seismic-array-exercises.md`](./exercises/01-case-study-seismic-array-exercises.md)
and
[`exercises/01-case-study-seismic-array-solutions.md`](./exercises/01-case-study-seismic-array-solutions.md).

## 12. Mastery checkpoint

Without notes:

1. A target is 2 km at 15 km depth with $\lambda = 3$ km. Compute the aperture and the
   required station count for a spacing at half the aliasing limit.
2. A campaign has 30 stations, 4 h per station and 4 people. Compute the station-hours, the
   person-days and the days to install with two crews.
3. Compute the raw volume for 30 stations at 200 Hz, 3 components, 4 bytes for 45 days.
4. With a 60 µA sleep current, 40 mA acquisition at 1/4 duty and 200 mA transmission for 30 s
   per day, compute the average current and the life on a 30 Ah battery at 60 % usable.
5. With per-station survival 0.85 for 30 stations at 900 m spacing, compute the expected
   aperture loss and the resolution consequence for $\lambda z = 15$ km².

## 13. Common pitfalls

1. **Asking for stations instead of resolution.** They are different purchases.
2. **Designing the spacing at the aliasing limit.** One failure leaves a hole.
3. **Forgetting the second visit.** Retrieval and download cost as much as installation.
4. **Budgeting the archive instead of the download bench.**
5. **Planning continuous acquisition on a duty-cycle battery.** It dies at half the campaign.
6. **Recording station coordinates from a map.** The measured geometry is the dataset.
7. **Assuming independent failures.** Clustered failures cost aperture, not just data.

## 14. Where this is used

- Temporary arrays for local-earthquake, microseismic and ambient-noise studies — see
  [23-02-03 Seismic Network and Array Design](../02-seismic-instruments-and-fieldwork/03-seismic-network-design.md).
- Monitoring networks for induced seismicity, volcanoes and glaciers, where availability is a
  safety figure.
- Any campaign whose design is a resolution requirement rather than an instrument choice.

## 15. Related lessons

- [02 Case Study: An ERT Survey from Design to Report](02-case-study-ert-survey.md) —
  the same design discipline for a near-surface electrical survey.
- [23-05-06 IoT and Autonomous Sensor Networks](../05-instrumentation-and-electronics/06-iot-sensor-networks.md) —
  the network arithmetic in general form.
- [23-02-05 Seismic Deployment, Installation and Field Records](../02-seismic-instruments-and-fieldwork/05-seismic-deployment.md) —
  the field procedure this case study schedules.
- [23-06-08 Laboratory Uncertainty Budgets and Reporting](../06-laboratory-measurements/08-lab-data-uncertainty.md) —
  the reporting discipline the deliverables follow.

## 16. Self-assessment checklist

- [ ] I can turn a resolution requirement into an aperture and a station count.
- [ ] I can separate the resolution constraint from the aliasing constraint.
- [ ] I can compute a workload in station-hours and person-days.
- [ ] I can compute the data volume, the archive and the download requirement.
- [ ] I can compute a duty-cycle power budget and the visit plan it implies.
- [ ] I can compute the delivered resolution after failures.
- [ ] I can name the decisions that cannot be deferred.
