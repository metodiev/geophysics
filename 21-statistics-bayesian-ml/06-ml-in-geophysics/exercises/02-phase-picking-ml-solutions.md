# Solutions — 21-06-02 Deep-Learning Phase Picking: SeisBench and Beyond

> Read after attempting. Lesson:
> [02 Phase Picking](../02-phase-picking-ml.md). Numbers are **SYNTHETIC**
> values printed by
> [`code/phase_picking_ml_demo.py`](../code/phase_picking_ml_demo.py).

---

## ★1 — Errors in samples

At 100 Hz, 1 sample is $0.01\ \mathrm{s}$.

| Statistic | 10 dB STA/LTA | 10 dB learned | 4 dB STA/LTA | 4 dB learned |
|---|---|---|---|---|
| bias (samples) | $+0.2$ | $-18.0$ | $+6.1$ | $+2.9$ |
| MAE (samples) | $34.2$ | $56.8$ | $92.7$ | $91.7$ |
| scatter (samples) | $63.5$ | $77.7$ | $106.2$ | $104.0$ |
| MAE/scatter | $0.539$ | $0.731$ | $0.873$ | $0.882$ |

Counts inside $\pm0.05\ \mathrm{s}$ (5 samples) out of 200 records: STA/LTA
$0.475 \times 200 = 95$ records; learned $0.090\times200 = 18$ records.

For a Gaussian, $\mathrm{MAE}/\sigma = \sqrt{2/\pi} = 0.798$ exactly. Every column
is below that, and the 10 dB STA/LTA column (0.539) is far below: the error
distribution has more mass at small errors *and* a longer tail than a Gaussian of
the same width. A ratio below 0.798 is the signature of a spike-and-tail — a
mixture of good picks and gross misses.

---

## ★2 — The bias against the label window

$$-0.180\ \mathrm{s} \times 100\ \mathrm{Hz} = -18\ \text{samples}.$$

The label window is $W = 20$ samples wide, so the bias is $1.8$ times $W/2 = 10$
samples and $0.9$ times the full window width. The label convention therefore
permits an error of order $W$ — the picker is free to fire anywhere the ladder of
positively-labelled windows begins, and the labels start at the onset, not at the
wavelet's leading edge. The statement "the maximum precision of a
window-label picker is half a window" is an *optimistic* bound; the measured
value here is twice it.

---

## ★3 — Does the comparison discriminate?

- 10 dB: $(0.568-0.342)/0.342 = +66.1\%$ in MAE for the learned picker.
- 4 dB: $(0.927-0.917)/0.917 = +1.09\%$.

At 10 dB the comparison separates the methods; at 4 dB it does not — the
difference is $1\%$ of MAE, far below the $\pm0.035$ binomial uncertainty on the
underlying fractions at 200 records. "Method B is worse" is a statement about the
signal-to-noise regime, and it must be reported as one.

---

## ★4 — Gaussian prediction versus measurement

With bias $\mu = 0.002\ \mathrm{s}$ and scatter $\sigma = 0.635\ \mathrm{s}$,

$$P(|X| \le 0.05) = \Phi\!\left(\frac{0.05-0.002}{0.635}\right) -
\Phi\!\left(\frac{-0.05-0.002}{0.635}\right)
= \Phi(0.0756) - \Phi(-0.0819) = 0.530 - 0.467 = 0.063 .$$

The measured fraction is $0.475$ — **7.5 times larger**. A Gaussian with this
scatter puts almost no mass inside a 0.05 s tolerance, yet nearly half of the
picks are there.

**Two-component mixture.** If the "good" component is essentially inside the
tolerance and the "gross-error" component is essentially outside it, then the
measured fraction *is* the mixture weight: $p_{\text{good}} \approx 0.475$, and
the remaining $0.525$ of picks are grossly misplaced, spread with a large tail
that inflates the standard deviation to 0.635 s. (A refined fit would let the
good component have some spread and would then need $p_{\text{good}} > 0.475$.)

The message: **mean and standard deviation are the wrong summary for a pick
residual.** The distribution is bimodal, and the two modes have different causes
(a correct latch on the wavelet versus a latch on a noise burst). Reporting
$0.342 \pm 0.635\ \mathrm{s}$ hides the fact that fewer than half the picks are
usable at any tolerance a network would accept.

---

## ★5 — Separating label bias from waveform bias

**Design.** Hold everything fixed — records, features, model family, split, SNR —
and vary only the label window width $W \in \{10, 20, 40\}$ samples. Train one
model per $W$, and score on identical held-out records with the true onset known.

**Metrics.** (i) bias in samples, $b(W)$; (ii) MAE, $\mathrm{MAE}(W)$;
(iii) the fraction of picks inside the label half-width, $W/2$ samples.

**Plot.** $b(W)$ against $W$ on a linear-linear axis, with the least-squares
slope and intercept.

**Hypothesis A — "bias scales with the label window".** The classifier cannot
resolve within the labelled span, so it fires at the earliest positively-labelled
window: $b(W) \approx -W/2$ (slope $-0.5$, intercept $\approx 0$). A refinement
accounting for the symmetric wavelet gives slope $-1$ with a negative intercept.

**Hypothesis B — "bias is set by the waveform".** The earliest feature the
classifier can see is the wavelet's leading edge, which is fixed by the dominant
frequency ($1/(2f) = 6.25$ samples at 8 Hz): $b(W) \approx \text{const}$,
independent of $W$.

**Decision rule.** If the fitted slope is significantly different from zero, the
label is implicated; if not, the waveform is. Both outcomes are informative, and
the experiment is cheap because only the labels change, not the data.

---

## ★6 — Why 18 samples, not 10?

The event is a Ricker wavelet, which is symmetric about the onset. Consider two
sibling windows:

- $[150, 170)$: the onset at its left edge, containing the wavelet's trailing
  half;
- $[140, 160)$: the onset 10 samples in, containing the wavelet's leading half.

Because the wavelet is symmetric, these two windows contain **mirror images** of
the same waveform, and the four features (mean square, peak STA/LTA, peakedness,
band ratio) are nearly the same for both. A classifier cannot separate them on
those features, so it picks the earlier one: exactly the extra 10 samples
observed on top of the trivial half-window effect. The measured $-18$ samples is
therefore about $W/2$ (from the ladder of labels) plus about $W/2$ of
mirror-image ambiguity, minus the wavelet's own leading-edge information.

**Removing the ambiguity** requires information the symmetric amplitude features
do not carry:

1. a label anchored on the wavelet's **first break** rather than its centre, so
   the leading edge is the target;
2. an **asymmetric** feature, such as the amplitude-normalised envelope or the
   instantaneous-phase onset, which distinguishes a rising edge from a falling
   one;
3. a **regression target** (see ★★★7) rather than a binary window label, so the
   model is rewarded for sub-window precision.

---

## ★★★7 — Offset-regression picker

**Target.** For each window with start index $i$ within $\pm W$ of the onset,
the target is the signed offset $y_i = (i - i_{\text{onset}})$ in samples; all
other windows are excluded from training rather than labelled 0, so the model is
never asked to learn "not here".

**Loss.** Mean absolute error on the offset. Huber or MAE is preferred to MSE
because the residual distribution of §★4 is heavy-tailed, and MSE would let a few
grossly misplaced training windows dominate.

**Metric.** On held-out records: bias (mean predicted offset plus the window
centre correction), MAE in seconds, and the fraction inside
$\pm0.01,\pm0.02,\pm0.05\ \mathrm{s}$. Report the residual distribution, not only
its first two moments (see ★★4).

**Sizing.** To resolve a residual bias of $0.01\ \mathrm{s} = 1$ sample, an
*unpaired* design needs $\mathrm{SE} \le 1/3$ sample with a residual standard
deviation of about 60 samples, i.e.
$n \ge (60/(1/3))^2 = 32\,400$ records. That is the wrong experiment.
Use a **paired** design: for every record, pick with both the old and the new
picker and difference the residuals. The paired standard deviation is the spread
of the *difference*, which in this generator is dominated by the shared
waveform-ambiguity term and can be an order of magnitude smaller; with
$\mathrm{sd}(\Delta) = 5$ samples, $n \ge (5/(1/3))^2 = 225$ records suffices.
Paired designs are the standard way to make a timing bias measurable.

---

## ★★★8 — A transfer test for a pretrained picker

**Strata.** Report every metric within strata, because an average hides the
failure: magnitude bins (four bins spanning the catalogue's range), hypocentral
distance bins, site class (rock versus soft sediment), and time of day (cultural
noise). Add a per-station column.

**Reference labels.** Analyst picks on a randomly drawn subset, each picked twice
by different analysts, so that the *reference* scatter — the floor below which no
model can be measured — is estimated rather than assumed. Without it, a
disagreement of 0.06 s between model and analyst may be the analyst's noise.

**Metrics.** Bias, MAE, and the fraction inside the tolerance demanded by the
downstream product (for relative location, typically a few tens of milliseconds);
report the residual distribution's tail, not only the mean.

**Split.** Station-disjoint and time-disjoint: train or fine-tune on some
stations and a past period, test on held-out stations and a later period. This
makes the test sensitive to site response and to instrument or network changes,
which are the two dominant transfer failures.

**The result that blocks deployment.** A stratum in which the tolerance fraction
falls below the downstream requirement *while the stratum carries a substantial
share of events* — for instance MAE of $0.15\ \mathrm{s}$ on the soft-sediment
stations that provide a quarter of detections, or a per-station bias that varies
by more than the tolerance and therefore maps into hypocentre error.

**What it cannot establish.** It cannot establish the benchmark's general
performance, whether the pretrained weights encode physics or the source
catalogue's style, or how the model behaves on signals absent from both the
training set and the test set (very small, very large, or out-of-network events).

---

## ★★★9 — Uncertainty on a tolerance fraction

$$\mathrm{SE} = \sqrt{\frac{p(1-p)}{n}} = \sqrt{\frac{0.475\times0.525}{200}}
= \sqrt{1.247\times10^{-3}} = 0.0353 .$$

For a target half-width of $0.005$:

$$n = \frac{p(1-p)}{0.005^2} = \frac{0.2494}{2.5\times10^{-5}} \approx 9\,975
\ \text{records}.$$

**Why the binomial interval is too narrow.** Records are not independent draws:
several records typically belong to the same event, sharing the same source
wavelet, the same path and the same station noise field, so their picks are
correlated and their residuals move together. The binomial formula assumes
independent Bernoulli trials, so it underestimates the variance by roughly a
factor equal to the average cluster size — with 10 records per event, an honest
interval is about $\sqrt{10} \approx 3$ times wider, and $n$ must be about 10
times larger for the same resolution.

**Resampling unit.** Resample **events** (clusters), not records: draw events
with replacement, take all of their records together, recompute the fraction, and
form the interval from the bootstrap replicates. This is the cluster (block)
bootstrap, and it automatically widens when the clipping or the noise field
correlates the picks.
