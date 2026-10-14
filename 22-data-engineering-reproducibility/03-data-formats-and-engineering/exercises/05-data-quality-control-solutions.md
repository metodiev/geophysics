# Solutions — 22-03-05 Automated Quality Control and Flagging

> Read after attempting. Numbers are computed here and match the demonstration's
> printed output. Lesson:
> [05 Automated Quality Control and Flagging](../05-data-quality-control.md).

---

## ★1 — Two error types and their costs

- **False positive** — a good sample flagged. Cost: data loss. In a geodetic series a
  false flag removes a real transient, and if the QC deletes rather than flags, the
  removal is irreversible; in a strong-motion archive it can remove the large amplitude
  the analysis exists to measure.
- **False negative** — a bad sample passed. Cost: correctness, silently. A spike left
  in a record biases a spectrum, a magnitude, or a moment estimate, and nothing in the
  output indicates it.

## ★2 — The false-positive budget of a $3\sigma$ rule

(a) $P(|z|>3) = 2\Phi(-3) = 2 \times 0.001350 = 0.0027 = 0.27\ \%$.

(b) $0.0027 \times 2000 = 5.4$ samples, matching the printed budget.

(c) At $2\sigma$: $2\Phi(-2) = 2 \times 0.02275 = 0.0455 = 4.55\ \%$, i.e. 91 samples
of 2000 — a 17-fold increase in data spent for a modest gain in sensitivity.

## ★3 — The robust rule

$$|\hat{x} - \text{median}(x)| > 3 \times 1.4826 \times \text{MAD}(x),
\qquad \text{MAD} = \text{median}\left(|x - \text{median}(x)|\right).$$

The factor 1.4826 is the reciprocal of the median of the absolute value of a standard
normal ($\Phi^{-1}(0.75) = 0.6745$): for Gaussian data
$\text{MAD} = 0.6745\,\sigma$, so $1.4826 \times \text{MAD}$ estimates $\sigma$. The
rule uses the **median** (an order statistic, so it moves only if more than half the
data move) and the **MAD** (the median of absolute deviations, likewise).

## ★★4 — Reading the confusion matrices

(a) 12 spikes at $12\sigma$: naive precision 1.000, recall 1.000; robust precision
0.800, recall 1.000. Both find every spike; the robust rule additionally flags 3
in-budget false positives, which is expected at a $3\sigma$ threshold
(budget $\approx 5$).

(b) 100 spikes at $4\sigma$: naive precision 1.000, recall **0.470**; robust precision
0.961, recall **0.740**. Use the **robust** rule: it recovers 74 of 100 moderate
spikes against 47, at the cost of 3 false positives. Missing 53 % of the moderate
outliers is a correctness failure; three extra flags are a data-loss cost the analyst
can afford.

(c) The naive rule's precision is 1.000 because its threshold has been inflated by the
spikes themselves (§§3–4 of the lesson): at $3.99\sigma$ it flags nothing that is not
a spike, since the clean data's largest excursions fall below the widened threshold.
Its recall is 0.470 because the same widening puts many $4\sigma$ spikes *below* the
threshold. High precision with low recall is the signature of a threshold that has
drifted away from the noise scale.

## ★★5 — Threshold stability

(a) Naive: $4.094/2.933 = 1.40$; $4.041/2.933 = 1.38$. Robust:
$2.927/2.924 = 1.00$; $3.222/2.924 = 1.10$ (the printed ratios are 1.40 and 1.25
against the robust threshold; against the clean naive value the pattern is the same).
The naive threshold moves down as well as up depending on where the outliers land, but
it is never stable.

(b) The variance is the mean of the squared deviations. Adding one value at
$12\sigma$ to 2000 unit-variance samples adds $12^{2}/2000 = 144/2000 = 0.072$ to the
variance, taking it from $1.000$ to $1.072$ and the standard deviation from $1.000$ to
$\sqrt{1.072} = 1.035$ — a 3.5 % increase per single extreme value, and the
$3\sigma$ threshold moves with it. The demonstration's 12 spikes move the threshold
from 2.933 to 4.094, a 40 % rise, consistent with adding $12 \times 0.072 = 0.864$ to
the variance (giving $\sqrt{1.864} = 1.365$, and $3 \times 1.365 = 4.09$ — exactly the
measured threshold).

(c) "We flag at $3\sigma$" is then not a reproducible statement: the threshold is
2.93 in one window and 4.09 in another, and the difference is caused by the data
rather than by the analyst's choice. A paper must state *how the scale was estimated*
(mean/standard deviation, robust scale, a per-channel calibration, a fixed physical
bound) and ideally report the resulting threshold distribution.

## ★★6 — A record that is 30 % zeros

(a) Measured: the standard deviation falls from 1.0069 (NaN-skipped) to 0.8677
(zero-filled), and 515 fake zeros are presented as measurements.

(b) The zeros are samples of value 0 drawn from a distribution with mean
$\approx 0$, so they contribute nothing to the *value* of the mean but dilute it: with
fraction $f = 0.30$ missing, the filled mean is approximately
$\bar x_{\text{fill}} \approx (1 - f)\bar x_{\text{clean}} +
f \cdot 0 = 0.70 \times 0.02781 = 0.01947$, close to the measured $+0.02065$; and the
variance is scaled to $\approx (1-f)\sigma^{2} = 0.70$, giving
$\sigma_{\text{fill}} \approx \sqrt{0.70} = 0.837$ against the measured 0.868 (the
small differences come from the finite sample and from the clean mean not being
exactly zero). The bias is therefore **proportional to the missing fraction** and
directed towards zero.

(c) Two representational changes: store the gaps as an explicit **fill value that can
never be a valid measurement** (a NaN, or a declared sentinel such as $-9999$ with a
`_FillValue` attribute), and record the convention in the file's metadata so every
reader knows it. Then either skip the fill values (and state so) or interpolate them as
an explicit modelling choice, never as a silent substitution.

## ★★★7 — QC for a 40-station accelerometer network

**Rule sequence** (each rule writes its own flag; later rules ignore data flagged by
earlier ones):

1. *Structural*: sample-interval continuity, duplicate time stamps, monotonic time,
   declared gaps. No threshold; a violation is a data-management fact.
2. *Physical bounds*: absolute amplitude outside the instrument's documented range
   (per channel and sensitivity), flag `out-of-range`.
3. *Flat-line / clipping*: zero variance over a window, or a long run at the
   full-scale value, flag `clipped` or `dead`.
4. *Robust statistical*: median $\pm 3 \times 1.4826\,\text{MAD}$ on a per-channel
   basis after a conservative first pass, flag `spike`.
5. *Rate of change*: $|\Delta x|$ beyond a per-channel threshold, flag `transient`
   (which is deliberately not the same flag as `spike` — a real transient is data).
6. *Multichannel consistency*: coherence or amplitude ratio against neighbours, flag
   `inconsistent`.

**Scale estimator per rule.** Median and MAD for the statistical rules, estimated per
channel from a documented reference interval (a quiet period) and stored with the
results; physical bounds from the instrument documentation; rate-of-change thresholds
from the sampling interval and the sensor's bandwidth, not from a global constant.

**Confusion-matrix evaluation plan.** Because labels do not exist, evaluate by
injection: for each rule, generate copies of a reference record with synthetic defects
of varying size (and with known timing for the structural rules) and measure TP, FP, FN
per rule and per defect size; also evaluate against documented real events (a known
earthquake that must *not* be flagged) to estimate the false-positive cost on genuine
signal.

**Flag vocabulary.** A small, versioned, documented list (`gap`, `out-of-range`,
`clipped`, `dead`, `spike`, `transient`, `inconsistent`), stored as a controlled
vocabulary so downstream queries are meaningful — the subject of
[22-03-06](../06-metadata-standards.md). Flags are
per-sample bit fields, never strings.

**Storage of raw and flagged values.** Raw values are immutable and archived; flags are
stored beside them in the same container (or a parallel group) so a reader always has
both. Derived products (a cleaned series) are regenerated from raw plus flags, never
overwriting raw.

**Audit trail.** Every flag records the rule identifier and version, the parameters
(the estimated scale, the threshold), and the reference interval used; a run-level
record lists the rule versions and the code commit. Without this, an archive's flags
become unexplainable after the second revision of the rules.

**The rule decision that cannot be automated.** Distinguishing a `spike` (instrumental)
from a `transient` (physical) where they are the same amplitude in one channel. Present
it to a user as an explicit, reviewable list: the candidate events with their context
(neighbouring channels, spectral content, time coincidence with other stations) and the
rule that raised them, so a person can accept or reclassify them — and record that
decision, with a name and a date, as part of the archive.

## ★★★8 — Labelling a real record without injections

**Evidence used to label a sample bad.** (i) An independent sensor: a co-located
instrument, a second channel of the same sensor, or a neighbouring station recording
the same time window; (ii) documentation of a real event that coincides (a documented
power outage, a maintenance log, a known cultural noise source); (iii) internal
inconsistency: a value that violates a physical bound, a channel that disagrees with
the array; (iv) expert visual assessment of the raw record with the rule's output
hidden.

**Inter-analyst agreement required.** Have at least two analysts label a stratified
sample of the same windows independently and report agreement (for example Cohen's
$\kappa$, or the raw per-sample agreement). A workable threshold for a QC study is
$\kappa \ge 0.6$ (substantial agreement); below that, the labels are not a ground truth
and the confusion matrix measures the analysts, not the rule.

**Two ways the labels could be biased towards the rule.** (i) **Availability bias**:
analysts label the samples the rule flagged, so the "truth" contains only the rule's
candidates and the evaluation cannot penalise a missed defect. Mitigate by sampling
windows independently of the rule's output. (ii) **Anchoring**: analysts see the rule's
flag while labelling and agree with it. Mitigate by hiding the rule's output during
labelling and revealing it only for the comparison.

**What the evaluation cannot establish.** How the rule performs on the defects *nobody
labelled* — the class of failure that is neither in the injected set nor in the
analysts' review. That residual risk is why a QC procedure keeps raw data and flags
separately: a future analyst with better labels can re-evaluate the same raw record.

## ★★★9 — Sampling error of a robust scale under correlated noise

**Dependence.** For $n$ independent Gaussian samples the MAD is asymptotically normal
with variance approximately

$$\operatorname{Var}(\widehat{\text{MAD}}) \approx \frac{1}{4\,n\,f(m)^{2}},$$

where $f$ is the density at the median; for Gaussian data this gives a relative
standard error of about $0.79/\sqrt{n}$. For a correlated record the effective sample
count $n_{\text{eff}} = T/\tau_{\text{int}}$ replaces $n$
([20-05-01](../../../20-signal-processing/05-noise-and-random-signals/01-stochastic-processes.md)
§3), so the relative error of the scale estimate becomes $\approx
0.79/\sqrt{n_{\text{eff}}}$.

**Practical consequence.** A station dominated by long-period noise with
$\tau_{\text{int}} = 50\ \text{s}$ has an effective count of $n_{\text{eff}} = T/50$:
for a one-day record, $86\,400/50 = 1728$ effective samples, so the scale estimate has a
relative standard error of $0.79/\sqrt{1728} = 1.9\ \%$. That is tolerable. For a
one-hour record, $n_{\text{eff}} = 72$ and the error is $9.3\ \%$; for a ten-minute
record, $n_{\text{eff}} = 12$ and the error is $23\ \%$. The threshold therefore moves
by tens of per cent between short windows, and quoting a single $3\sigma$ number for
short windows is not defensible.

**What to measure before quoting a threshold.** The integrated autocorrelation time of
the channel's noise (so $n_{\text{eff}}$ is known), the resulting sampling error of the
scale estimate for the window length in use, and the sensitivity of the flag count to
that error (by re-estimating the scale on bootstrap or block-resampled copies of the
record and observing the spread of flagged counts). Report the threshold as an interval
with that spread, or lengthen the window until the spread is acceptable.
