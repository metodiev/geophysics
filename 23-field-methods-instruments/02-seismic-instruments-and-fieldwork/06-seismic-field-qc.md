---
id: 23-02-06
title: "Field QC: Noise Checks, Continuity, Station Uptime"
level: advanced
prereqs: ["23-02-05", "05-05-05"]
estimated_minutes: 90
tags: [seismology, quality-control, uptime, continuity, noise, field-work]
---

# Field QC: Noise Checks, Continuity, Station Uptime

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** uptime for a station and for a network, and **compute** both from
   gap statistics.
2. **Compute** availability from mean time between failures and mean time to
   repair, and **state** which of the two is the cheaper lever.
3. **Compute** the false-positive rate of a noise QC threshold on a Gaussian
   baseline, and **choose** a threshold from a stated error rate.
4. **Detect** constant, saturated and disconnected channels with deterministic
   tests, and **measure** their false-positive rates.
5. **Account** for continuity in samples, and **report** completeness, gaps and
   overlaps as three separate numbers.
6. **Design** a daily QC loop that runs during the campaign, and **state** which
   failures it cannot catch.

All gap rates, noise levels, thresholds and failure counts in this lesson are
**SYNTHETIC** teaching values printed by the demonstration. No real station, network
log or noise measurement is used or reproduced.

## Prerequisites

- [05 Deployment, Orientation, Timing and Metadata](05-seismic-deployment.md) —
  the deployment whose quality this lesson verifies.
- [05-05-05 Acquisition QC: Noise Tests, Repeatability, Metadata](../../05-core-geophysics/05-survey-design-and-acquisition/05-quality-control.md) —
  the acquisition-side view of the same duty.

## 1. Intuition: QC is a loop, not a report

Quality control during a field campaign exists to answer one question daily: **is
what is being recorded good enough, and if not, what do we do tomorrow?** A QC
report written a month after demobilisation is an obituary, not a control loop.

The reason QC has to be quantitative is that the failures are mostly silent. A dead
channel produces a file of zeros that a processing script will happily read; a
station that lost clock lock produces a record that looks perfect; a noisy station
produces data that will be blamed on the geology. None of these announces itself.
What catches them is a set of numbers, computed every day, compared with thresholds
chosen *in advance* from the required data quality.

Three families of numbers are needed:

- **Availability** — is there data at all? (uptime, gaps, overlaps)
- **Integrity** — is the data what it claims to be? (dead channels, saturation,
  clock state, gain settings)
- **Quality** — is the data good enough? (noise levels relative to the site's
  ambient expectation)

## 2. Uptime and availability

**Station uptime** is the fraction of the expected recording time that was actually
recorded:

$$U = 1 - \frac{\sum_j \tau_j^{\text{lost}}}{T_{\text{expected}}}.$$

For 20 stations over 30 days (720 h each) with a per-station-day gap probability of
0.04 and gaps of 2 h, the demonstration reports an expected 1.20 gaps and 2.40 h
lost per station, i.e. an expected uptime of 0.99667. The simulation gives a mean
uptime of 0.99653, a minimum of 0.98889 and a standard deviation of 0.00315, with

- **15 of 20 stations below 0.999**,
- 5 of 20 below 0.995,
- 1 of 20 below 0.990.

That distribution is the lesson. The *mean* uptime, 99.65 %, sounds excellent; the
tail matters, because a station with a 1.1 % outage is the station that will be
missing when the event of interest happens. Report the distribution, name the worst
stations, and investigate the ones in the tail — that is what a QC loop is for.

**Availability** is the model-based version of the same idea, useful for planning
because it requires no data:

$$A = \frac{\text{MTBF}}{\text{MTBF} + \text{MTTR}} .$$

The demonstration's table:

| MTBF (d) | MTTR (h) | availability | downtime (h/year) | repairs/year |
|---|---|---|---|---|
| 45 | 6 | 0.99448 | 48.4 | 8.1 |
| 45 | 2 | 0.99815 | 16.2 | 8.1 |
| 180 | 6 | 0.99861 | 12.1 | 2.0 |
| 20 | 6 | 0.98765 | 108.1 | 18.2 |

Compare the first two rows and the first with the third. Reducing the repair time
from 6 h to 2 h raises availability from 0.99448 to 0.99815 — cutting downtime by
two thirds — while tripling the MTBF from 45 d to 180 d raises it to 0.99861 at a
much greater cost in component reliability. **When the MTTR is not small compared
with the MTBF, repairing faster is the cheaper lever.**

## 3. Noise QC and its false-positive rate

The standard noise check measures a band-limited rms (or power) at each station and
compares it with the population. The comparison must be robust, because the
distribution of station noise levels is skewed and the outliers are exactly what
you are looking for. The usual approach uses the median and the median absolute
deviation converted to a Gaussian-equivalent scale,

$$\hat\sigma = 1.4826 \times \mathrm{median}\left(\left|x_i - \mathrm{median}(x)\right|\right),
\qquad z_i = \frac{x_i - \mathrm{median}(x)}{\hat\sigma}.$$

The demonstration's synthetic population of 60 channels (with 4 injected at 3× to
16× the median level) gives a median of $9.477\times10^{-7}$, a robust scale of
$3.856\times10^{-7}$ (0.407 of the median), and

| threshold | flagged | of which injected | clean flagged | expected under Gaussianity |
|---|---|---|---|---|
| $z > 2$ | 8 | 4 of 4 | 4 | 1.3 |
| $z > 3$ | 6 | 4 of 4 | 2 | 0.1 |
| $z > 4$ | 5 | 4 of 4 | 1 | 0.0 |

The expected count is $\tfrac{1}{2}\mathrm{erfc}(z/\sqrt{2})$ per channel
multiplied by the number of clean channels — the one-sided Gaussian tail. The
measured values are higher than the Gaussian expectation because the *clean*
population is genuinely skewed (it is lognormal by construction), which is itself
the important practical point: **a threshold justified by a Gaussian argument will
flag more channels than the argument predicts, because the real distribution has a
heavier tail.** Choose the threshold from a *measured* null (the campaign's own
stations on a quiet day), not from a Gaussian assumption, and report the observed
flag rate so that the next campaign can use it.

## 4. Dead, constant and saturated channels

Three deterministic tests, each computable in seconds per day and each with a
slightly different target:

| Test | Criterion | Detects |
|---|---|---|
| Constant channel | $\mathrm{std}(x) = 0$ exactly | Disconnected or powered-down sensor; a logger writing zeros |
| Saturation | fraction of samples at the extreme value $> 5\ \%$ | Clipped acquisition, a sensor driven beyond range |
| Disconnection | rms far below the population *and* no coherent noise | A sensor that is connected but not coupled, or a broken pair |

The demonstration applies the first two to 60 synthetic channels, 60 000 samples
each, and detects **6 of 6** constant channels and **3 of 3** saturated channels
with **zero** false positives on the clean channels. That is what a good
deterministic test looks like: full recall, no false alarms, no threshold
judgment.

The third test is the hard one, because "too quiet" is not a defect by itself — a
quiet station is the goal. It requires a *cross-check* against the other channels
or components: a channel whose noise is uncorrelated with its neighbours' *and*
far below them is suspicious, whereas a channel that is quiet because it is on
bedrock is not.

## 5. Continuity accounting

For $N$ stations, $D$ days and a sample rate $f_s$, the expected sample count is
$N D \times 86\,400 f_s$. The demonstration's 20 stations, 30 days at 100 sps give
$2.592\times10^{8}$ samples per station. Its SYNTHETIC set contains 25 gaps in
total (1.25 per station), $1.8\times10^{7}$ lost samples in total, and per-station
completeness with mean 0.996528 and minimum 0.988889.

Report continuity as three numbers, never as one:

1. **Completeness** — the fraction of expected samples present.
2. **Gaps** — count and total duration, with the cause (power, storage, connector).
3. **Overlaps** — count and total duration, which indicate clock or operator error
   rather than a hardware failure.

The three have different causes and different remedies, and a single "data
quality" percentage hides which one is costing you the dataset.

## 6. The daily QC loop

A loop that works in practice, in the order it should run:

1. **Ingest** the day's data and verify the file inventory against the plan
   (stations expected × channels × duration).
2. **Integrity**: dead, constant and saturated channel tests; verify the gain,
   filter and sample-rate settings against the deployment metadata.
3. **Continuity**: gaps and overlaps in samples, per channel.
4. **Clock**: lock status, offset against a reference, drift since the last visit.
5. **Noise**: band-limited rms per channel against the measured null, with the
   robust $z$ and the flag list.
6. **Acceptance**: compare the day's numbers with the campaign thresholds and
   produce a short list of actions for tomorrow — a station to visit, a channel to
   re-seat, a gain to change.
7. **Archive** the day's QC table with the data, so that a later analyst sees the
   same numbers the field team saw.

Steps 2–5 are automatable; step 6 is the one that requires a person, and it is the
one that is skipped when the schedule is tight — which is precisely when it is
worth the most.

## 7. Assumptions and regime of validity

1. **Expected counts are known.** Uptime and completeness require the planned
   schedule, sample rate and channel list; without them, completeness is
   unmeasurable, only gaps are.
2. **Noise levels are stationary.** A QC threshold calibrated on one season may
   flag stations that are merely recording a noisier season.
3. **The population is homogeneous.** A station on soft ground is genuinely noisier
   than one on bedrock, so a single global threshold misclassifies real site
   differences as defects. Where possible, compare stations with their own history
   rather than with each other.
4. **Deterministic tests have no false negatives for the failure they target, but
   no test is universal.** A channel with a small offset and normal-looking noise
   passes everything and is still wrong.
5. **MTBF and MTTR are summaries of a non-exponential process.** Real failures
   cluster after storms, power events and visits; the availability formula is a
   planning device.

## 8. The honest summary

- Mean uptime hides the tail; 15 of 20 stations were below 0.999 in the
  demonstration.
- Cutting repair time from 6 h to 2 h raised availability more than tripling the
  MTBF, at this ratio.
- A $z > 3$ noise threshold flagged 2 clean channels of 56, against 0.1 predicted
  by a Gaussian argument: calibrate the threshold on a measured null.
- Constant and saturated channels are detected perfectly by deterministic tests;
  "too quiet" is not.
- Report completeness, gaps and overlaps separately.
- QC is a daily loop with an action list, not a final report.

## 9. Python demonstration

[`code/seismic_field_qc_demo.py`](./code/seismic_field_qc_demo.py) prints every
number quoted above. It:

1. simulates gap statistics for 20 stations over 30 days and reports the uptime
   distribution and the tail counts;
2. tabulates availability for four MTBF/MTTR pairs;
3. builds a synthetic noise population, computes robust $z$ scores and reports the
   flagged counts against the Gaussian expectation at three thresholds;
4. detects constant and saturated channels and reports the false-positive counts;
5. accounts for continuity in samples per station.

Run it with the project virtual environment:

```bash
cd 23-field-methods-instruments/02-seismic-instruments-and-fieldwork/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python seismic_field_qc_demo.py
```

## 10. Exercises

Worked problem sets are in
[`exercises/06-seismic-field-qc-exercises.md`](./exercises/06-seismic-field-qc-exercises.md)
and
[`exercises/06-seismic-field-qc-solutions.md`](./exercises/06-seismic-field-qc-solutions.md).

## 11. Mastery checkpoint

Without notes:

1. A station loses 4 gaps of 3 h each over a 45-day deployment. Compute its uptime.
2. MTBF is 30 days and MTTR is 4 hours. Compute the availability and the annual
   downtime in hours.
3. A noise population has 40 stations; a threshold is expected to flag 5 % of them
   by chance. How many false positives do you expect, and what would you report if
   the observed count were 12?
4. State the test that detects a disconnected channel and the reason a quiet
   channel cannot be flagged on its own.
5. Name the three continuity numbers and the different cause each indicates.

## 12. Common pitfalls

1. **Reporting a mean uptime.** The tail is what costs the dataset.
2. **Spending effort on MTBF when MTTR is the cheaper lever.**
3. **A Gaussian threshold on a skewed noise population.** It flags more stations
   than advertised.
4. **One global noise threshold across a heterogeneous site.** Site differences
   are not defects.
5. **Running QC at the end of the campaign.** The failures are still present and
   can no longer be fixed.
6. **Treating "no data" and "quiet data" as equivalent.** The first is a gap; the
   second may be a dead channel.
7. **Not archiving the QC table.** A later analyst repeats the work and may reach a
   different conclusion.

## 13. Where this is used

- Every temporary and permanent network: the daily loop is the operational core of
  observatory work.
- Aftershock deployments, where the recording window is short and a lost day is a
  lost fraction of the dataset.
- Induced-seismicity monitoring, where a regulator may require documented station
  availability and detection performance.
- Active-source surveys, where the equivalent checks are per-spread rather than
  per-day, and the fixes are immediate.
- Data-centre ingestion: the same tests are what a quality-control pipeline runs
  when data arrive from the field — see
  [22-03-05 Automated Quality Control and Flagging](../../22-data-engineering-reproducibility/03-data-formats-and-engineering/05-data-quality-control.md).

## 14. Related lessons

- [05 Deployment, Orientation, Timing and Metadata](05-seismic-deployment.md) —
  the metadata the QC loop checks against.
- [03 Seismic Network Design and Station Siting](03-seismic-network-design.md) —
  the detection capability that station outages erode.
- [02 Digitizers, Dynamic Range, Gain and Anti-Alias Filtering](02-digitizers-and-gain.md) —
  the clipping arithmetic behind the saturation test.
- [23-01-02 Planning a Field Campaign: Objectives, Permits, Logistics](../01-field-safety-and-planning/02-field-planning.md) —
  the schedule the uptime is measured against.
- [22-03-05 Automated Quality Control and Flagging](../../22-data-engineering-reproducibility/03-data-formats-and-engineering/05-data-quality-control.md) —
  the same tests implemented in a data pipeline.

## 15. Self-assessment checklist

- [ ] I can compute station and network uptime from gap statistics.
- [ ] I can compute availability from MTBF and MTTR and argue which to improve.
- [ ] I can compute and interpret a robust $z$ score and its expected flag rate.
- [ ] I can specify the deterministic channel tests.
- [ ] I can account for continuity in samples.
- [ ] I can describe a daily QC loop with an action list.
