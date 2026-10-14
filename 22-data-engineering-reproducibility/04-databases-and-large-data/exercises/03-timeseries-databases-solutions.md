# Solutions — 22-04-03 Time-Series Databases for Sensor Networks

> Read after attempting. Numbers are computed here and match the demonstration's
> printed output. Lesson:
> [03 Time-Series Databases for Sensor Networks](../03-timeseries-databases.md).

---

## ★1 — Naive storage

Values: $10^{6} \times 8 = 8.0$ MB. With 4-byte timestamps:
$10^{6} \times 12 = 12.0$ MB. The span is $10^{6}/86\,400 = 11.57$ days, so a year
contains $365.25/11.57 = 31.6 \approx 32$ such spans — matching the demonstrated 32×.

## ★2 — What the second difference removes

$d_2$ annihilates any **linear** component of the series: if $x_i = a + bi$ then
$x_{i+1} - 2x_i + x_{i-1} = 0$. A drifting sensor's trend therefore disappears from the
residual, leaving only noise and curvature, whose magnitudes are smaller — which is what
makes a magnitude-based bit packing cheaper. The same idea underlies other predictor
schemes (first order, linear extrapolation, polynomial): predict the next value from
previous ones and store the residual.

## ★3 — The aggregate ratio

A one-hour query covers $3\,600$ raw samples (28.8 kB) against 60 one-minute means
(0.5 kB): a ratio of **60×**, which is the sampling rate divided by the aggregate rate
($3600\ \text{s} \div 60\ \text{s}$). The ratio is constant with the interval — 60× at
1 h, 24 h and 168 h — because both sides scale with the span.

## ★★4 — Bits and the loss

(a) Storage ratio against 64-bit float64: $64/12.8 = 5.00\times$ for the
noise-dominated series and $64/6.3 = 10.16\times$ for the smooth one, matching the
demonstration's 4.98× and 10.14× (the small differences are the mean over a finite
sample).

(b) The quantisation error bound is half a step: $5.0 \times 10^{-4}$ data units. For
the $\sigma = 1$ series it is 0.05 % of a standard deviation — negligible. For the
$\sigma = 0.01$ series it is 5 % of a standard deviation, so the compression is not
"lossless for practical purposes" but a small distortion of the signal. The correct
comparison is with the **measurement uncertainty**, not with the signal's amplitude.

(c) A paper quoting a compression ratio must state: the scheme and its settings
(here, second differences with a $10^{-3}$ step), the quantisation error or an upper
bound on it, the data it was measured on (the two series differ by a factor of two in
ratio), and the reference (ratio against float64, or against the previous storage).
Without those four, the number is not reproducible.

## ★★5 — A 200-channel, 10 Hz network

(a) Raw per channel-year: $10 \times 86\,400 \times 365 \times 8\ \text{B} =
2.52 \times 10^{9}\ \text{B} \approx 2.52$ GB. For 200 channels:
$\approx 505$ GB/year. Hourly means: $8\,760 \times 8\ \text{B} = 70$ kB per
channel-year, $\approx 14$ MB for the network per year — eight orders of magnitude
smaller.

(b) Overhead: $70\ \text{kB} / 2.52\ \text{GB} = 2.8 \times 10^{-5} = 0.0028\ \%$.

(c) The arithmetic supports keeping every aggregate tier the queries need — they are
effectively free — and it says nothing about whether raw must be kept. That question is
about what may need reprocessing (a calibration change, a sensor swap, a new method), not
about space, and it is answered by the data management plan rather than by the storage
budget.

## ★★6 — A drifting clock and a re-delivering service

(a) An **upsert on the primary key** `(channel, time)`: the re-delivered rows replace the
existing ones instead of multiplying them, which is the same idempotence requirement as
in [22-03-03](../../03-data-formats-and-engineering/03-data-pipelines.md) §5.

(b) Store **instrument time** (what the logger recorded, including its drift) and
**receipt time** (when the data arrived at the archive). The instrument time is the
physical fact to be corrected later; the receipt time is the audit trail that shows when
the archive learned of it — and it is the only way to reconstruct the arrival order of
late data.

(c) If only the instrument time were stored and the correction applied in place, the
original time would be lost: a later revision of the correction (a better drift model,
or the discovery that the drift was a step) could not be applied, and the change itself
would be untraceable — the archive would contain values whose timestamps cannot be
explained, which is the spatial-analogue of the unit error in
[22-03-06](../../03-data-formats-and-engineering/06-metadata-standards.md) §4.

## ★★★7 — A 500-channel, 100 Hz, ten-year network

**Requirements.** (i) live monitoring of the last day, (ii) a one-year, 1-minute-
resolution research query, (iii) reprocessing after a calibration change.

**Tiers and retention.**

| Tier | Resolution | Retention | Why |
|---|---|---|---|
| raw | 100 Hz | full ten years | the only tier that can be reprocessed |
| 1-second means | 1 Hz | ten years | cheap, and the natural working resolution |
| 1-minute means | 1/min | ten years | the research query tier |
| 1-hour means | 1/h | indefinite | the "forever" summary and the live view's history |

**Volumes.** Raw: $500 \times 100 \times 86\,400 \times 365 \times 8\ \text{B} =
1.26 \times 10^{13}\ \text{B} \approx 12.6$ TB/year, so **126 TB over ten years** before
compression. With a measured second-difference ratio of 5× (noise-dominated channels are
typical at 100 Hz), about **25 TB**. The 1-second tier is 1 % of raw (0.126 TB/year),
the 1-minute tier 0.017 % (21 GB/year), the hourly tier negligible.

**Compression per tier.** Raw and the 1-second tier use the lossless-or-nearly scheme
with a documented error bound; the 1-minute and hourly tiers are themselves aggregates,
so they compress well and lose nothing more than the averaging already lost.

**Partitioning.** By month, per channel group: each partition holds one channel-month of
raw (~3.5 GB) so pruning is effective, retention is a partition drop, and a reprocessing
job can operate partition by partition.

**The requirement that dominates the cost.** **Retaining raw for reprocessing** (iii):
it is 99 % of the archive's bytes and the only tier that cannot be regenerated. Everything
else is a rounding error — which is why the retention decision, not the compression codec,
is the design decision.

## ★★★8 — Choosing the quantisation step for a channel

**Statistic.** Compare the analysis's output computed on the raw series with the output
computed on the compressed-and-reconstructed series, as a function of the quantisation
step $\Delta$. The statistic is the relative change in the *analysis's output* — a
spectral level in a band, a moment estimate, a strain rate — not the reconstruction error,
because the analysis's sensitivity to $\Delta$ is what matters.

**Reference.** The analysis's own uncertainty: the change caused by $\Delta$ must be well
below the stated uncertainty of the output, typically by an order of magnitude, so that
the compression does not consume the error budget.

**Confounder.** The analysis's sensitivity depends on the band and on the method: a
narrow-band spectral estimate near the Nyquist rate is far more sensitive to quantisation
noise than a broadband amplitude. A $\Delta$ derived for a band-limited analysis can be
wrong for a later broadband one, and the confounder is not in the data but in the
question.

**What the measurement cannot guarantee.** That an analysis not yet imagined will be
insensitive: the measurement characterises the steps tested on the analyses tested. The
defensible policy is a quantisation step at least an order of magnitude below the
instrument's noise floor (so the compression adds no measurable noise for any reasonable
analysis) plus the retention of the raw tier for cases where that assumption is doubted.

## ★★★9 — Deleting raw after one year

**Fraction unreprocessable.** After five years with a one-year raw window, **80 %** of
the archive (years 2–5) cannot be reprocessed; after ten years, 90 %. The 1-hour means
are all that remains for those spans.

**Blocked scenarios.**

1. **A calibration change** with a nonlinear response: hourly means cannot be
   re-calibrated exactly, because averaging and a nonlinear correction do not commute.
2. **A time correction** (a drift model revision): the aggregated timestamps are on the
   old time base, and re-binning to the corrected times requires the raw samples.
3. **A new method at higher resolution** (ambient-noise correlations, small-event
   detection, spectral studies): the hourly tier has lost the band above
   $1/3600$ Hz, permanently.
4. **A quality-control revision**: a despiking rule applied to the raw record cannot be
   re-run on hourly means, which have already averaged the spikes into the data.

**Storage that would have avoided it.** Keeping raw costs, for a 200-channel 10 Hz
network, about 505 GB/year (from ★★5); the hourly tier costs 14 MB/year. Over five years
the difference is 2.5 TB against 0.07 GB — the raw tier is the whole cost, and the
aggregates were never the problem. The decision to delete raw saved the raw tier's cost
and destroyed the ability to reprocess 80 % of the archive.

**Retention policy to propose.** (i) raw retained for the lifetime of the data management
plan, with the span justified by the instrument's calibration interval and the group's
research horizon (a defensible default is 5–10 years, or "as long as the instrument
operates plus one reprocessing cycle"); (ii) aggregates rebuilt automatically whenever
raw changes, so the tiers cannot diverge; (iii) all tiers versioned together
([22-02-05](../../02-reproducible-workflows/05-data-versioning.md)) with the calibration
version stored per value; (iv) a documented deletion policy for the aggregates only.

**Evidence needed to defend it.** The measured annual volume of each tier (the
arithmetic above), the list of research questions that need the band above the aggregate's
Nyquist frequency, the instrument's calibration-change history with the fraction of changes
that were nonlinear, and the storage budget the group actually has. With those four, the
retention span is a decision with a number attached rather than a preference.
