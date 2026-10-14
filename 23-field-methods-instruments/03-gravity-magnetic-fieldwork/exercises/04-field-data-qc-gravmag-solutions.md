# Solutions — 23-03-04 Field Data QC for Potential-Field Surveys

> Read after attempting. Lesson:
> [04 Field Data QC](../04-field-data-qc-gravmag.md). All values are
> **SYNTHETIC**.

---

## ★1 — The four rejected loops

The overall mean square decomposes over the two groups:

$$n\,\text{MS}_{\text{all}} = n_1\text{MS}_1 + n_2\text{MS}_2,$$

with $n = 60$, $\text{RMS}_{\text{all}} = 0.0935$, $n_2 = 56$ (within tolerance),
$\text{RMS}_2 = 0.0832$ and $n_1 = 4$ unknown.

$$\text{MS}_{\text{all}} = 0.0935^{2} = 0.00874225
\;\Rightarrow\; 60\,\text{MS}_{\text{all}} = 0.5245350,$$

$$56\,\text{MS}_2 = 56 \times 0.0832^{2} = 56 \times 0.00692224 = 0.3876454,$$

$$4\,\text{MS}_1 = 0.5245350 - 0.3876454 = 0.1368896
\;\Rightarrow\; \text{MS}_1 = 0.0342224,$$

$$\text{RMS}_1 = \sqrt{0.0342224} = \mathbf{0.1850\ mGal}.$$

So the four rejected loops have a closure RMS of 0.185 mGal — well above the overall
0.0935 and consistent with their exceeding a 0.15 mGal tolerance.

**Is removal justified by the arithmetic alone?** No. Removing 6.7 % of the loops
lowers the RMS from 0.0935 to 0.0832 mGal, an improvement of 11 % in a summary
statistic, at the cost of discarding the loops that carry the largest measured
closures — which is to say the strongest evidence about the drift's variability.
The closure value is not an error in the station anomalies: it is a *measurement of
the drift term*, and a large value is informative rather than defective.
Rejection is justified only when an independent cause is recorded (a storm, an
interrupted base occupation, an instrument that was re-levelled), and the number of
rejections and their causes belong in the report so that a reader can judge whether
the rejection was principled.

---

## ★2 — Pooled repeatability

Pool the variances:

$$s_{\text{pooled}}^{2} = \frac{1}{8}\left(0.0017^{2} + 0.0028^{2} + 0.0036^{2}
+ 0.0044^{2} + 0.0051^{2} + 0.0062^{2} + 0.0070^{2} + 0.0081^{2}\right)
\times 10^{-6}.$$

Squares (in units of $10^{-6}$): 2.89, 7.84, 12.96, 19.36, 26.01, 38.44, 49.00,
65.61. Sum $= 222.11$.

$$s_{\text{pooled}}^{2} = \frac{222.11}{8} \times 10^{-6} = 27.76\times10^{-6}
\;\Rightarrow\; s_{\text{pooled}} = 0.00527\ \mathrm{mGal}.$$

$$\text{se of a 3-reading value} = \frac{0.00527}{\sqrt{3}}
= 0.00304\ \mathrm{mGal}.$$

**Check the contrast.** The arithmetic mean of the eight standard deviations is
$(0.0017 + 0.0028 + 0.0036 + 0.0044 + 0.0051 + 0.0062 + 0.0070 + 0.0081)/8
= 0.00486$ mGal, against the pooled 0.00527 — the mean of standard deviations is
biased low by 7.8 %. With eight stations the bias is modest; with two or three it is
severe, which is why pooling is the correct procedure and why the per-station values
should be reported alongside the pooled one: the range here is a factor of 4.8, so
one station has a site or procedure problem worth investigating.

---

## ★★3 — Testing the levelling adjustment

After a perfect constant-per-line adjustment, the remaining mis-tie between two
lines is the difference of two independent reading noises, so

$$\sigma_{\text{residual}} = \sigma_{\text{reading}}\sqrt{2}
= 1.5 \times 1.4142 = 2.121\ \mathrm{nT}.$$

Observed residual RMS: **1.981 nT**. The ratio is

$$\frac{1.981}{2.121} = 0.934,$$

i.e. the residual is 6.6 % *below* the expectation. For 24 mis-ties, the standard
deviation of a sample RMS is about $\text{RMS}/\sqrt{2n} = 2.121/\sqrt{48} = 0.306$
nT, so a value 0.14 nT below expectation is 0.46 standard deviations — entirely
consistent.

**Criterion used:** the model (a constant offset per line) is *adequate* when the
post-adjustment residual is statistically consistent with the reading noise. If the
residual had been several times the reading noise, the model would be wrong, and the
diagnosis would be that the mis-tie error is not a per-line constant — for example a
residual diurnal error varying along the line, a mis-located tie station, or a
localised magnetic anomaly at the crossings.

**A caveat worth stating.** The residual being consistent does **not** prove the
adjustment improved the data: a constant-per-line model with six parameters fitted to
24 mis-ties can nearly always reduce the RMS, and the reduction of the *residual* to
the noise floor is the meaningful evidence — together with the requirement that the
fitted offsets be plausible. An offset of 20 nT where the population scatters by
5 nT would signal a blunder that the adjustment is spreading rather than removing.

---

## ★★4 — Cross-over decomposition

$$\text{RMS} = \sqrt{\text{mean}^{2} + \text{sd}^{2}}
= \sqrt{8.155^{2} + 4.099^{2}} = \sqrt{66.504 + 16.802} = \sqrt{83.306}
= 9.127\ \mathrm{nT}.$$

(The demonstration reports 9.123 nT from the unrounded data; the 0.004 nT
difference is rounding of the mean and standard deviation.)

**Which part is removable.** The **mean** (8.155 nT) is a level error — a
systematic difference between the production and tie lines — and a levelling
adjustment removes it. The **scatter** (4.099 nT) is the noise of the measurement
system and is not removable. After removing the level, the RMS becomes

$$\text{RMS}_{\text{after}} = \sqrt{0.073^{2} + 4.099^{2}} \approx 4.099\ \mathrm{nT},$$

which is the irreducible noise floor of this dataset: 4.1 nT.

**Diagnostic for a non-constant level error.** If the level error drifts during the
survey (thermal drift of the sensor, a changing diurnal correction residual, a
slowly varying altitude error), it will not appear as a constant mean; it will
appear as a **correlation between the cross-over error and the time of day (or the
line number)**. The diagnostic is therefore to plot (or regress) the cross-over
error against the acquisition time of the production line: a systematic trend
indicates a time-varying level error, which must be modelled as a function of time
rather than as a constant per line. A second diagnostic is the sign asymmetry: a
constant level error gives the same sign whether line A crosses B or B crosses A,
whereas some processing artefacts reverse sign with the crossing direction.

---

## ★★★5 — A QC report for a 12-day ground gravity survey

**Daily statistics, computed at the end of each field day.**

| # | Statistic | Tolerance | Justification |
|---|---|---|---|
| 1 | Number of stations occupied vs planned | Report only | Scheduling, not quality |
| 2 | Loop closures, per loop | 0.15 mGal | From the lesson: the worst modelled closure over the durations used is 0.187 mGal; a tolerance below that would reject valid loops |
| 3 | Repeat stations, per day (at least one) | Difference within 2.78 s (95 %, $n = 5$) | Student-$t$ coverage for five repeats |
| 4 | Base re-occupation difference | 2.78 s of the reading noise | Detects an instrument offset |
| 5 | Drift rate fitted per day | Within a factor of 2 of the campaign's assumed rate | A larger value invalidates the looping interval |
| 6 | Missing readings, times, station identifiers | Every station complete | Completeness, cheap to check |
| 7 | Elevation and position recorded, with method | Every station | Without them the reductions cannot be made |
| 8 | Anomaly at the previous day's repeat station | Within the daily repeatability | Tests the whole chain, not just the instrument |

**End-of-survey statistics.**

| # | Statistic | Tolerance |
|---|---|---|
| 9 | Pooled repeatability across all repeat stations | Report with its scatter |
| 10 | Closure RMS and its distribution | Consistent with the drift model |
| 11 | Elevation error at check points against an independent method | Within the specification derived from the target |
| 12 | Number of stations rejected, each with a recorded cause | Report; zero rejections without causes |
| 13 | The error budget with the share of each term | Report; identify the dominant term |

**Arithmetic for two tolerances.**

- **Loop closure (row 2).** From
  [01 Gravity Fieldwork](../01-gravity-fieldwork.md), the worst closure at durations
  of 2–4 h is 0.1564 mGal at 4 h; at 0.5 mGal a 4 h loop would be almost certainly
  wrong (a factor of 3.2 above the model), and at 0.15 mGal one would reject valid
  loops. So the tolerance is set at about the worst modelled value: **0.15 mGal for
  loops up to 4 h**, and it is stated *with* the duration.
- **Repeat stations (row 3).** From the demonstration, the pooled repeatability with
  five repeats is 0.0050 mGal and the 95 % coverage factor for $n = 5$ is 2.78,
  giving a tolerance of $2.78 \times 0.0050 = 0.014$ mGal for the difference between
  the first and the repeat reading. (For a difference of two readings, the
  applicable standard deviation is $s\sqrt{2}$, so the tolerance becomes
  $2.78 \times 0.0050 \times \sqrt{2} = 0.020$ mGal if the *difference* rather than
  the repeat value is being tested; state which convention the tolerance uses,
  because the two differ by 41 %.)

**Actions each failure triggers.** A closure above tolerance: repeat the base
occupation and, if it persists, re-observe the loop on the next day. A repeat above
tolerance: re-seat and re-levelled the instrument, then repeat; if it persists,
check the site for traffic or wind, and record the site as noisy. A drift rate
anomaly: reduce the loop duration for the remainder of the survey. A missing
elevation or position: re-occupy the station, and never interpolate it from a map.
A chain check (row 8) outside tolerance: stop and find the cause before processing
further data, because it indicates a systematic error that will affect every
subsequent station.

**Archiving.** The QC table is written as a machine-readable file (one row per
loop, repeat or check with the value, the tolerance, the pass/fail and the cause
code), stored in the survey directory beside the data, and cited in the data
release notes. A QC report that exists only in a field notebook is not reusable; a
QC report that exists only as a summary percentage cannot be audited. The
combination — the per-measurement table plus a summary — is what allows a later
reader to recompute the survey's accuracy or to exclude a specific station.

---

## ★★★6 — Establishing the achieved accuracy independently

**Measurements.**

1. **Repeat occupations of a subset of stations**, ideally 10 % of them, spread
   across the survey area and across the campaign, occupying the *same* station
   (same monument, same sensor height, recorded in the notes) at a different time.
2. **An independent levelling or positioning check** at a smaller number of
   stations: spirit levelling from a benchmark, or a static GNSS session, or a total
   station traverse — a method different from the production method.
3. **A comparison with an external dataset** over the survey area: a national
   gravity database, a previous survey, an elevation model, or a published anomaly
   map. This is the only check that tests the *absolute* level of the result.

**Reference.** For (1), the production value itself at a different time (a
self-consistency test). For (2), the published coordinates or the levelling result.
For (3), the external dataset, with its own accuracy stated, and with the
conversion between datums and reductions documented.

**Metric.** For each check station, the difference in the final *anomaly* (not in
the raw reading), in mGal or nT, decomposed into a mean (systematic) and a standard
deviation (random), with the number of check stations. Also report the same
statistics restricted to the ends of the survey area, since systematic errors often
grow towards the edges (datum mismatch, geoid model degradation, reduction
approximations).

**Two failure modes internal QC cannot detect.**

1. **A uniform offset or tilt across the whole survey**, caused by a wrong datum, a
   wrong base value, a coordinate-system error or a wrong reduction constant. Every
   internal test is relative, so a common error cancels; the survey's grid looks
   perfectly levelled and is uniformly wrong. Only the comparison with an external
   dataset (or the occupation of a known absolute gravity or magnetic reference
   station) reveals it.
2. **An error that is consistent between the survey and its own metadata.** If the
   station heights were all derived from the same wrong terrain model, or all
   positions were shifted by the same datum transformation, the internal checks
   (which use those heights and positions) will show excellent consistency while the
   reductions are all biased in the same way. Detecting it requires an independent
   measurement of height or position at a few stations, not more internal checks.
