---
id: 23-05-06
title: "IoT and Autonomous Sensor Networks for Earth Monitoring"
level: research
prereqs: ["23-05-05", "23-05-03", "23-02-03"]
estimated_minutes: 110
tags: [sensor-networks, autonomy, telemetry, duty-cycle, availability, edge-computing]
---

# IoT and Autonomous Sensor Networks for Earth Monitoring

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the data volume of a network from sample rate, channel count, node
   count and duration, and the storage it implies.
2. **Compare** the airtime a data volume needs against the duty-cycle limit of a
   licence-free band, and **state** what a shortfall forces the design to do.
3. **Compute** the detection probability of a randomly timed event for a given wake
   interval, and the wake interval a target probability requires.
4. **Compute** a link budget and **distinguish** the free-space range from the range an
   empirical path-loss model predicts.
5. **Compute** network availability for a per-node survival probability, and the
   node-days redundancy costs and returns.
6. **State** the two timing requirements a network can have and why one of them is
   orders of magnitude cheaper.
7. **State** what an autonomous network cannot deliver, and how to report it.

All rates, currents, sensitivities, path-loss parameters and survival probabilities
here are **SYNTHETIC** teaching values combined with the standard relations quoted in
the text. No vendor specification, regulatory figure or measured radio link is
reproduced.

## Prerequisites

- [05 Building Low-Cost Instruments](05-instrument-design-lowo.md) — the node's own
  noise, power and timing budgets.
- [03 Timing, GNSS Disciplining and Clock Accuracy](03-timing-and-gnss-instruments.md) —
  the clock discipline a network depends on.
- [23-02-03 Seismic Network and Array Design](../02-seismic-instruments-and-fieldwork/03-seismic-network-design.md) —
  the geometry a network is designed around.

## 1. Intuition: a network is not a bigger instrument

A single instrument is judged by its accuracy. A network is judged by four other
properties, and they are the ones that fail:

- **Coverage**: which places and times are observed at all, i.e. node-days.
- **Availability**: the fraction of planned node-days that actually produce usable
  data.
- **Latency**: how long after an event the result exists.
- **Autonomy**: how long the network runs without a visit, and how much of its failure
  is silent.

Every one of those is a *system* property rather than a sensor property, and the
design discipline is to budget them the way a single instrument budgets noise. The
three budgets that bind a network are data volume, energy and clock — in that order,
because each one can make the others impossible.

## 2. The requirement, written as network properties

| Property | Example value | Why it binds |
|---|---|---|
| Coverage | 20 nodes, 180 days | node-days and the failure budget |
| Resolution per node | as the single-station design | the node's noise budget |
| Latency | none required (store and collect) | whether telemetry is needed at all |
| Availability | ≥ 16 of 20 nodes at any time | redundancy and spares |
| Autonomy | one visit in 6 months | power and clock budgets |

The single most valuable entry is **latency**, because "no latency required" removes the
telemetry problem entirely: a network that stores data and is visited twice produces
better data than one that streams everything at the edge of its duty-cycle budget.

## 3. Data volume

For a node with $f_s$ per component, $C$ components and $b$ bytes per sample, the rate
is $f_s C b$ bytes per second. With 100 Hz, three components and four bytes per sample:

$$\text{rate} = 100 \times 3 \times 4 = 1200\ \mathrm{B/s} = 9.6\ \mathrm{kbit/s} ,$$

$$\text{per node per day} = 1200 \times 86\,400 = 103.68\ \mathrm{MB} ,$$

$$20 \text{ nodes} \times 180 \text{ days} = 373.25\ \mathrm{GB},$$

$$\text{after } 3\!:\!1 \text{ lossless compression} = 124.42\ \mathrm{GB} .$$

Two conclusions. First, the *volume* is unremarkable for storage — 124 GB is a single
disk — which is why store-and-collect is the right default. Second, the volume is
remarkable for **radio**, which the next section quantifies. The design habit that
follows: decide the archive before the radio, because the archive is cheap and the radio
is not.

## 4. Airtime and the duty-cycle limit

Licence-free sub-GHz bands typically impose a duty-cycle limit — the illustrative
figure used here is **1 %** — and a node's raw data stream needs

$$\text{airtime} = \frac{103.68\ \mathrm{MB} \times 8}{50\ \mathrm{kbit/s}}
= 16\,589\ \mathrm{s} = 4.61\ \mathrm{h/day} = 19.2\ \% \text{ of the day},$$

against an allowance of $0.01 \times 86\,400 = 864$ s/day, i.e.

$$\text{deliverable at the limit} = \frac{864 \times 50\,000}{8}
= 5.40\ \mathrm{MB/day}, \qquad \text{shortfall} = 19.20\times .$$

So **the raw stream cannot be streamed**, by a factor of 19. The four honest options,
in the order that preserves the most science:

1. **Store and collect** (option zero): no telemetry at all, plus a health beacon. Costs
   a visit; loses nothing.
2. **Trigger and buffer**: send a short summary per event, keep the waveform locally.
   This is what makes a network scientifically useful at 1 % duty.
3. **Decimate**: send a low-rate channel continuously and the full-rate channel only on
   trigger — cheap, and it changes the *science* rather than just the engineering, so it
   must be agreed with the scientist.
4. **Change the medium**: a licensed link, a wired backhaul to a few gateways, or a
   physical pick-up. Usually the correct answer for a large campaign.

## 5. Detection probability and the wake interval

An autonomous node that sleeps wakes on a schedule, so a randomly timed event of
duration $\tau$ is detected only if it overlaps a recording window $w$:

$$P(\text{detect}) = \min\left(1, \frac{\tau + w}{\Delta}\right) ,$$

with $\Delta$ the wake interval. For $\tau = 2$ s and $w = 5$ s:

| Wake interval | $P$ | Acquisition duty |
|---|---|---|
| 300 s | 0.0233 | 0.0167 |
| 120 s | 0.0583 | 0.0417 |
| 60 s | 0.1167 | 0.0833 |
| 30 s | 0.2333 | 0.1667 |
| 7.78 s | 0.8997 | 0.6427 |

Reaching $P = 0.90$ requires $\Delta = 7/0.9 = 7.78$ s, i.e. a **64 % acquisition duty
cycle** — which the airtime budget of the previous section rules out for raw data and
which the power budget usually rules out as well. This is the central tension of
autonomous monitoring: **probability of detection is bought with duty cycle, and duty
cycle is bought with energy**. The resolutions are a longer recording window (cheap,
because the window is mostly digitisation), on-board detection so that only interesting
windows are kept (the standard design), and accepting a stated $P$ rather than
pretending it is 1. The $P$ must appear in the methods section.

## 6. Link budget and range

With a synthetic transmit level of 14 dBm, 2 dBi at each end and a receiver sensitivity
of −120 dBm, the allowable path loss is

$$L_{\text{allowed}} = 14 + 2 + 2 - (-120) = 138\ \mathrm{dB} .$$

In free space $L = 20\log_{10}(d) + 20\log_{10}(f) - 147.55$ (with $d$ in metres and $f$
in hertz), which at 868 MHz gives $d = 218.3$ km. **That is a geometric statement, not
a prediction**: free space ignores the ground, clutter, the antenna's height and the
Fresnel zone, and a 218 km link from a battery-powered surface node is not a thing that
happens.

An empirical model is the honest alternative:
$L(d) = L(10\ \mathrm{m}) + 10n\log_{10}(d/10)$ with a synthetic reference
$L(10\ \mathrm{m}) = 60$ dB and path-loss exponent $n = 3.5$, giving

| Case | Range |
|---|---|
| allowable loss 138 dB, no margin | 1692.7 m |
| allowable loss 118 dB (20 dB fade margin) | 454.1 m |

so a 20 dB margin costs a factor of 3.73 in range. The design consequences are the ones
that matter in the field: **the fade margin dominates the range**, the exponent is what
must be measured on site (a pilot link, not a specification), and the number to quote in
a plan is the one with the margin included, because a link that works only in dry
weather is a link that does not work.

## 7. Time in a network

A network has two possible timing requirements and they are not comparable in cost:

- **Absolute timing** (each node's clock correct to a stated tolerance against UTC),
  which needs GNSS discipline at intervals set by the oscillator: 33.33 s for an
  uncompensated crystal at a 1 ms tolerance, 16.67 min for a TCXO, 55.56 h for an OCXO.
- **Relative timing** (node-to-node alignment to a stated tolerance), which is usually
  what the science needs and which cancels the common clock error when all nodes are
  disciplined at a common epoch or when a common reference signal is recorded.

The cost of the absolute route is often fatal: continuous GNSS disciplining at a
synthetic 25 mA average draws $25 \times 24 = 600$ mAh/day, which is 14 Ah in 23 days —
more than a 20 Ah pack delivers usable over a six-month campaign. So a network whose
timing is specified as absolute and continuous is a network whose battery is the design
driver, and the first question to ask is whether the requirement is truly absolute.

## 8. Availability, redundancy and node-days

With a per-node survival probability $p$ over the campaign, the number of surviving nodes
is binomial. For 20 nodes, $p = 0.90$ and a demand of at least 16 nodes:

$$P(X \ge 16) = \sum_{k=16}^{20} \binom{20}{k} 0.9^{k} 0.1^{20-k} = 0.9568 ,$$

and a seeded Monte Carlo of 200 000 trials gives 0.9569 — a difference of 0.0001, which
is the expected sampling error and a useful regression test for the arithmetic.

The better metric, though, is **node-days**:

| Quantity | Value |
|---|---|
| planned node-days | 3600 |
| expected node-days (90 % survival) | 3240 |
| lost to failure | 360 |
| node-days returned by two extra nodes from the start | 324 |

Two extra nodes deployed from the beginning return 324 node-days for the cost of two
sites set up once, against the 360 node-days lost to the failures that spares absorb.
**Spares deployed up front are almost always cheaper than a revisit**, and the reason is
that the revisit costs crew time, access permission and risk, while the spare costs a
socket. This is the quantitative form of the redundancy argument, and it is the reason
networks are designed with more nodes than the inversion strictly needs.

## 9. Autonomy, edge processing and honest failure

Three design rules separate a network that produces data from one that produces
disappointment:

1. **Failure must be visible.** A node that silently stops reporting and a node whose
   data are wrong look identical in a volume count. Every node needs a heartbeat, a
   battery voltage, a temperature, a clock-offset estimate, and a counter of rejected or
   clipped samples in each report.
2. **Decide at the edge what to keep, but keep enough to check.** On-board detection
   saves the airtime; on-board *deletion* destroys the ability to audit the detector.
   Keep the rejected windows' statistics, at least.
3. **State the degradation, not just the availability.** "16 of 20 nodes returned 91 % of
   their planned samples; the 9 % are the six hours before each visit" is a defensible
   statement. "The network worked well" is not.

## 10. Assumptions and regime of validity

1. **The rates are sustained.** Duty-cycle and airtime arithmetic assume the link
   achieves its nominal throughput; a retransmitting link with 30 % packet loss spends
   1.4× the energy.
2. **The nodes are independent.** The binomial availability model assumes independent
   failures. A shared firmware bug, a common power design or a regional heat wave
   correlates failures and makes the binomial estimate optimistic — the honest model is
   a common-cause term plus the independent one.
3. **The path-loss model is local.** $n$ and the reference loss are site properties;
   quoting a range without stating them is quoting a measurement that was never made.
4. **The event process is uniform in time.** $P = (\tau + w)/\Delta$ assumes a random
   arrival; a clustered process (aftershocks) makes it wrong in both directions.
5. **The clock holds.** All timing claims are holdover claims, and holdover is
   temperature-dependent.
6. **The archive exists.** Store-and-collect assumes someone will collect, verify and
   archive; absent that, the network's data volume is a liability rather than an asset.

## 11. The honest summary

- A network is judged on coverage, availability, latency and autonomy, not on a single
  node's accuracy.
- 20 nodes at 100 Hz, 3 components, 180 days is 373 GB raw and 124 GB compressed: a
  trivial archive and an impossible radio stream.
- The raw stream needs 19.2× the airtime a 1 % duty cycle allows, so "store and
  collect" or "trigger and buffer" is the design, not a compromise.
- A 90 % detection probability for a 2 s event requires a 7.78 s wake interval and a
  64 % duty cycle: state the probability you actually achieve instead.
- The free-space range at 868 MHz for a 138 dB budget is 218 km, which is why an
  empirical path-loss model with a fade margin — 454 m at 20 dB margin here — is the
  number to plan with.
- Absolute timing can be unaffordable; relative timing is usually free.
- Two spare nodes return 324 node-days for the price of two sockets.

## 12. Python demonstration

[`code/iot_sensor_networks_demo.py`](./code/iot_sensor_networks_demo.py) prints every
number quoted above: the data volume and archive, the airtime against the duty-cycle
limit, the detection-probability table and the required wake interval, the link budget
with free-space and empirical ranges, a binomial-versus-Monte-Carlo availability check,
and the node-days budget.

```bash
cd 23-field-methods-instruments/05-instrumentation-and-electronics/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python iot_sensor_networks_demo.py
```

## 13. Exercises

Worked problem sets are in
[`exercises/06-iot-sensor-networks-exercises.md`](./exercises/06-iot-sensor-networks-exercises.md)
and
[`exercises/06-iot-sensor-networks-solutions.md`](./exercises/06-iot-sensor-networks-solutions.md).

## 14. Mastery checkpoint

Without notes:

1. Compute the daily volume per node for 50 Hz, one component, two bytes per sample.
2. Compute the airtime for that volume over a 25 kbit/s link and compare it with a 1 %
   duty limit.
3. Compute the detection probability for a 1 s event with a 4 s window at a 120 s wake
   interval, and the wake interval needed for 0.8.
4. Compute the allowable path loss for 10 dBm, 0 dBi at each end and −110 dBm
   sensitivity.
5. Compute the expected node-days for 12 nodes, 90 days and a survival probability of
   0.85, and the number of extra nodes that would return half of the loss.

## 15. Common pitfalls

1. **Specifying latency when none is needed.** It converts a solved problem into a radio
   problem.
2. **Planning with the free-space range.** It is a geometric statement, not a prediction.
3. **Hiding the detection probability.** A network that misses 90 % of events is a
   scientific claim, and it must be stated.
4. **Quoting a range without the fade margin or path-loss exponent.**
5. **Assuming independent node failures.** Shared firmware and a shared power design are
   common causes.
6. **Silent failure modes.** No heartbeat, no health telemetry, no way to tell a dead
   node from a quiet one.
7. **No archive plan.** Store-and-collect requires collecting, verifying and archiving.

## 16. Where this is used

- Temporary seismic arrays and microseismic monitoring networks, where node-days and
  redundancy are the currency — see
  [23-02-03 Seismic Network and Array Design](../02-seismic-instruments-and-fieldwork/03-seismic-network-design.md).
- Long-term environmental and hydrological monitoring, where visits are the dominant
  cost.
- Landslide, volcano and permafrost monitoring, where detection probability is a safety
  figure rather than a scientific one.
- Smart-city and infrastructure monitoring, where the latency requirement is real and a
  licensed or wired backhaul is the answer.
- Any campaign whose data will be reused: the network's health telemetry is what makes
  the archive interpretable.

## 17. Related lessons

- [05 Building Low-Cost Instruments for Teaching and Research](05-instrument-design-lowo.md) —
  the node-level noise, power and timing budgets.
- [03 Timing, GNSS Disciplining and Clock Accuracy](03-timing-and-gnss-instruments.md) —
  holdover and disciplining arithmetic.
- [23-02-03 Seismic Network and Array Design](../02-seismic-instruments-and-fieldwork/03-seismic-network-design.md) —
  the geometry a network's coverage is designed around.
- [07 Field Campaign Case Studies](../07-field-campaign-case-studies/01-case-study-seismic-array.md) —
  a full campaign worked through from requirement to report.

## 18. Self-assessment checklist

- [ ] I can compute a network's data volume and archive size.
- [ ] I can compare airtime against a duty-cycle limit and name the options.
- [ ] I can compute detection probability and the wake interval a target requires.
- [ ] I can compute a link budget and an empirical range with a fade margin.
- [ ] I can compute availability and the node-days redundancy costs.
- [ ] I can state the two timing requirements and which is cheaper.
- [ ] I can state what an autonomous network cannot deliver.
