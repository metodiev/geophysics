# Solutions — 23-02-06 Field QC: Noise Checks, Continuity, Station Uptime

> Read after attempting. Lesson:
> [06 Field QC](../06-seismic-field-qc.md). All values are **SYNTHETIC**.

---

## ★1 — Uptime from four gaps

Expected recording time:

$$T_{\text{expected}} = 45 \times 24 = 1080\ \mathrm{h}.$$

Lost time:

$$T_{\text{lost}} = 4 \times 3 = 12\ \mathrm{h}.$$

$$U = 1 - \frac{12}{1080} = 1 - 0.011111 = 0.988889 \quad (98.89\ \%).$$

**Samples lost at 100 sps:**

$$n = 12 \times 3600 \times 100 = 4.32\times10^{6}\ \text{samples}.$$

Note that this is exactly the worst station in the lesson's simulation (minimum
uptime 0.988889), which is a useful coincidence to check the arithmetic against.
An uptime of 98.9 % means the station was absent for about 1 % of the deployment —
and if the four gaps happened during the aftershock sequence, the loss is not
1 % of the *information*, because the largest events are few and the chances of
missing one are what matters.

---

## ★2 — Availability and where to spend effort

$$A = \frac{\text{MTBF}}{\text{MTBF}+\text{MTTR}}
= \frac{30 \times 24}{30 \times 24 + 4} = \frac{720}{724} = 0.994475 .$$

Annual downtime:

$$(1 - A) \times 8760 = 0.005525 \times 8760 = 48.4\ \text{h/year}.$$

**Halving the MTTR** to 2 h:

$$A = \frac{720}{722} = 0.997230, \qquad
(1-A) \times 8760 = 24.3\ \text{h/year}.$$

So halving the repair time removes 24.1 h of annual downtime. To achieve the same
by improving reliability alone, keep MTTR = 4 h and solve

$$\frac{24\,\text{MTBF}}{24\,\text{MTBF}+4} = 0.997230
\;\Rightarrow\; \text{MTBF} = 60\ \text{days}:$$

doubling the mean time between failures is required — usually a much larger
engineering effort than arranging faster access to the sites. The cheaper lever is
the repair time, and it gets cheaper still if the MTTR is dominated by *travel*
rather than by repair, because then the intervention is logistics (spares on site,
a local technician, a documented procedure) rather than reliability engineering.

---

## ★3 — Noise QC false positives on 40 stations

**Expected false positives** at a 5 % one-sided rate:

$$40 \times 0.05 = 2.0 \text{ stations}.$$

**Observed 12.** That is six times the expectation, so the hypothesis "all 12 are
chance" is untenable: under a binomial(40, 0.05) null, $P(X \ge 12)$ is of order
$10^{-6}$. Two conclusions are possible and both must be considered:

1. The threshold is mis-calibrated — most likely because the true population is
   *not* Gaussian but skewed with a heavier tail (the lesson's synthetic population
   gave 4 clean flags against 1.3 expected at $z > 2$), or because the stations are
   genuinely heterogeneous.
2. The stations are genuinely noisy — a real, actionable finding.

**Check before naming a station faulty.** Recompute the flag list on a *quiet*
reference day for the same stations, using each station's own history rather than
the population. A station that is flagged on the survey day *and* on its own quiet
days is faulty; a station that is flagged only on the survey day is recording a
noisier day (weather, cultural activity), which is a physical difference rather
than a defect. Reporting the observed flag rate alongside the threshold is what
makes the difference visible.

---

## ★★4 — A station that is "too quiet"

The measured band-limited rms is $1.0\times10^{-6}\ \mathrm{m/s}$ while an
independent estimate of the true ground noise at the site is
$2.5\times10^{-6}\ \mathrm{m/s}$. The ratio is

$$\frac{A_{\text{measured}}}{A_{\text{true}}} = \frac{1.0}{2.5} = 0.4, \qquad
20\log_{10}(0.4) = -7.96\ \mathrm{dB}.$$

So the station is missing a factor of 2.5 in amplitude. Since the missing
amplitude is *coherent across the band* (it is a factor, not a random scatter), the
cause is a systematic one, and there are three candidates in order of likelihood:

1. **A gain or full-scale mismatch** between the recorded metadata and the actual
   configuration — the most common cause of a frequency-independent factor.
2. **An installation response attenuated at the frequency of interest.** A coupling
   resonance above the band attenuates below it: solving
   $|H_c| = 0.4$ with $h_c = 0.5$ at $f = 10\ \mathrm{Hz}$ gives $r = 0.5926$, so

   $$f_c = \frac{10}{0.5926} = 16.87\ \mathrm{Hz}, \qquad
   |H_c(10)| = \frac{0.3512}{\sqrt{(0.6488)^{2}+(0.5926)^{2}}} = 0.4000
   \;\Rightarrow\; -7.96\ \mathrm{dB},$$

   which is precisely the observed deficit. So a coupling resonance at about
   17 Hz with this damping is a quantitatively sufficient explanation, and any
   resonance in the region 15–19 Hz would produce a similar factor.
3. **A sensor that is not properly coupled** (loose base, backfill not compacted),
   which is the physical mechanism behind case 2.

**What to do.** Neither adjust the QC threshold for this station nor flag it and
move on. A station whose *noise* is apparently low is a station whose *amplitudes*
are biased, and amplitudes are what most interpretations use. The correct actions
are, in order: check the gain and full-scale settings against the deployment
metadata (cheap, resolves case 1); if they match, treat the installation as
suspect and re-seat or re-bury the sensor (resolves cases 2 and 3). Until the cause
is identified, the station's amplitudes must not be compared with other stations',
and the uncertainty must be carried into any result that uses them. A quiet
*true* site looks identical in the data — which is exactly why an independent
reference (a second sensor, or this station's own history before the change) is
required before deciding.

---

## ★★★5 — A daily QC loop for a 25-station, 60-day deployment

**Tests, in order, with the time budget.**

| # | Test | Threshold and its derivation | Time |
|---|---|---|---|
| 1 | File inventory | Every station and channel expected, present; no unexpected file | 5 min (script) |
| 2 | Constant channel | $\mathrm{std}(x) = 0$ exactly | 2 min (script) |
| 3 | Saturation | $> 5\ \%$ of samples at the extreme value; the 5 % figure is chosen so that a brief transient does not trigger it | 2 min (script) |
| 4 | Gain, filter, sample rate | Compare with the deployment metadata; any difference is a defect regardless of data quality | 3 min (script) |
| 5 | Gaps and overlaps | Any gap $> 30\ \mathrm{s}$ listed with its exact position; overlaps flagged separately (they indicate clock or operator error) | 5 min (script) |
| 6 | Clock | Lock state, offset against a reference at the last visit, drift since; flag any station unlocked for $> 1\ \mathrm{h}$ | 5 min (script + 2 min reading the log) |
| 7 | Noise | Band-limited rms per channel; robust $z$ against the *campaign's own* median and MAD from the first quiet day, not a Gaussian assumption; flag $z > 3$ **and** record the observed flag rate | 5 min (script) |
| 8 | Horizontal/vertical coherence | Ratio of horizontal to vertical noise; a ratio far above the population indicates tilt or coupling problems | 3 min (script) |
| 9 | Action list | A named person, a station, an action, a deadline | 10 min (person) |

Total: about 40 minutes of which 10 require a person. The thresholds in rows 2, 3
and 6 are *absolute* (a device that returns zeros, a device at its limiter, a clock
that has lost lock) and need no calibration. The threshold in row 7 is *relative*
and must be calibrated on the campaign's own quietest day, because the population is
skewed and heterogeneous.

**Actions the loop can trigger.** A site visit for a station whose clock has
drifted (row 6); a channel re-seat for a saturation or a low-rms channel (rows 3
and 7); a gain change if the saturation persists (row 3); a power or storage fix
for a gap (row 5); a metadata correction for a settings mismatch (row 4); and, in
the worst case, the decision to relocate a station whose noise cannot be brought
inside the requirement (rows 7 and 8).

**Three failure classes the loop cannot detect.**

1. **A slowly developing error that remains inside every threshold.** An
  orientation change of a few degrees that moves a station's horizontal
  components, or a gain that changes by 20 %, passes all the tests above because
  each threshold is loose compared with the effect on a specialist measurement. Catching
  it needs an independent check (a polarisation estimate from a known event, a
  cross-station amplitude comparison).
2. **Errors in the state that is not measured.** If the deployment metadata are
  wrong in the same way for two channels — for example the components swapped in
  the record and in the log — every consistency test passes.
3. **Failures between the field and the processing centre.** Corruption or edit
  during transfer, conversion or reformatting is invisible to a QC loop that runs
  on the transferred files. It needs a checksum comparison against the field
  archive (see
  [23-01-03 Field Notebooks, Metadata and Data Provenance](../../01-field-safety-and-planning/03-field-notebooks.md)).

---

## ★★★6 — Measuring the effect of outages on completeness

**Data.** (i) The catalogue for the period and region, with origin times,
hypocentres, magnitudes and the number of stations contributing to each solution.
(ii) The station metadata and operational log, giving the *operating state of the
network* at each origin time: which stations were up, their gains, and their
distances from each event. (iii) The detection thresholds actually applied by the
processing.

**Estimator.** For each event in the catalogue, compute the number of operating
stations within a stated detection radius. Then estimate $M_c$ separately for
subsets of events defined by the *network strength* (for example 25 vs 20 vs 15
operating stations), using a standard $M_c$ estimator — maximum curvature of the
magnitude–frequency distribution with the fitting range reported, the $b$-value
stability criterion, and the goodness-of-fit $R$ statistic — and bootstrap the
confidence interval by resampling magnitudes.

**Metric.** $M_c$ in magnitude units as a function of network strength, with a
bootstrap confidence interval at each level, plus the slope $dM_c/dN_{\text{stations}}$.
The interpretable quantity is how much of the catalogue's apparent temporal
variation in $M_c$ is explained by the network's operating state alone.

**Control for the operating configuration.** Group events by *exact* configuration
(the set of operating stations and their gain settings), not by a coarse proxy such
as the year. Where the configuration is unique for a short interval, compare
configurations that overlap in time and space so that source-region and
seasonal effects are held roughly constant.

**Two confounding effects.**

1. **Circularity.** The catalogue is produced by the network being assessed, so the
   events that are missing are precisely the ones the analysis would need to count;
   $M_c$ estimated from the catalogue is a lower bound on the true completeness.
   Partially mitigated by comparing with an independent catalogue (a regional
   network, a template-matching detection run on archived continuous data) for an
   overlapping period.
2. **Changes in processing that are not changes in the network.** A revised
   detection threshold, an association-parameter change or a change of analyst can
   shift the apparent $M_c$ with no change in the hardware. Control for this by
   re-processing a fixed archived dataset with both the old and the new
   configuration and measuring the resulting $M_c$ difference directly.
