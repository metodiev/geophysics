---
id: 09-07-02
title: "EM Processing Workflow and Data Editing"
level: graduate
prereqs: ["09-07-01", "05-06-01", "05-06-02"]
tags: [electrical-methods, processing, editing, bias, qc]
---

# EM Processing Workflow and Data Editing

## Learning objectives

By the end of this lesson you will be able to:

1. **List** the steps of a standard EM time-series processing chain and **state**
   what each step removes and what each step costs.
2. **Derive** the amplitude bias of a centred moving average at a given gate
   from the curvature of the decay, and **check** the result against a measured
   table.
3. **Design** a spike detector whose threshold is estimated from the data, and
   **demonstrate** how the choice between a global and a local scale changes the
   false-positive rate on a record with multiplicative noise.
4. **Explain** what a "quiet window" for drift removal assumes, and **measure**
   the model error introduced when the assumption is false.
5. **Report** a processing result with its bias measured against an ideal
   synthetic, and **distinguish** a bias from scatter using a monotonicity test.
6. **Choose** a filter length, a despiking window and a drift-fit window against
   a stated error budget rather than against a visual impression.
7. **Write** a processing log that makes the chain reproducible, including the
   parameters that were *not* chosen and why.

## Prerequisites

- [09-07-01 EM Noise, Coupling and Cultural Effects](01-em-noise-and-coupling.md) —
  the noise taxonomy that decides which steps are needed.
- [05-06-01 The Processing Pipeline Concept](../../05-core-geophysics/06-data-processing-principles/01-processing-pipeline-concept.md) —
  filtering, stacking and the vocabulary of signal estimation.
- [05-06-02 Noise Suppression and Filtering](../../05-core-geophysics/06-data-processing-principles/02-noise-suppression.md) —
  convolution, transfer functions and the cost of a low-pass.

## 1. Intuition: processing is estimation, not cleaning

A processing chain is often drawn as a pipeline that turns raw data into good
data. It does not. Every step is an **estimator**: it replaces the data with a
quantity that has less noise and more structure, and it introduces a bias in
exchange. The only questions worth asking of a step are:

1. What does it estimate?
2. How large is its noise reduction, measured?
3. How large is its bias, measured — and on what?

This lesson answers those questions for the four steps that dominate an
electromagnetic time-domain data set: **despiking**, **drift removal**,
**low-pass filtering** and **stacking**. The workhorse is a synthetic transient
whose true value is known exactly, so that every bias can be measured rather than
argued about.

All models and data in this module are **SYNTHETIC**. The decay shape
$V(t) = A(t+t_0)^{-p}$ with $p = 2.5$ is a *chosen* teaching shape — not a
claimed physical law — and the noise, drift and spike amplitudes are chosen
values.

## 2. The record, and why the dynamic range matters

The demonstration builds a 40 ms record of 2048 samples from

$$V(t) = A\,(t+t_0)^{-p},\qquad A = 1.00,\ t_0 = 1.00\times10^{-4}\ \mathrm{s},\
p = 2.5,$$

with multiplicative noise $2\%$ of the local signal, a linear offset reaching
$2.000\times10^{6}$ at the last sample (in the same arbitrary units), and six
spikes at $0.50\times$ the local signal. The six data gates are

| gate | $t$ ($\mu$s) | clean signal |
|---|---|---|
| 1 | 300.0 | $3.2637\times10^{8}$ |
| 2 | 600.0 | $7.5570\times10^{7}$ |
| 3 | 1200.0 | $1.6667\times10^{7}$ |
| 4 | 2400.0 | $3.1888\times10^{6}$ |
| 5 | 4000.0 | $9.2574\times10^{5}$ |
| 6 | 6000.0 | $3.4423\times10^{5}$ |

The record spans a factor $3.22\times10^{6}$ from first sample to last. That
single number explains most of the processing difficulty in the method:

- The offset is $4.49\times10^{-5}$ of the signal at gate 1 — **unmeasurably
  small** — and 0.87 of the signal at gate 6, and 644 times the signal at the end
  of the record. An instrument offset that is invisible early *dominates late*.
- The noise is multiplicative, so the *relative* noise level falls by orders of
  magnitude along the record and any statistic computed over the whole record
  (a global MAD, a global standard deviation) is dominated by one end of it.
- The early samples change fastest, so any convolution over a fixed window
  biases the early gates and barely touches the late ones.

## 3. Despiking

### 3.1 The detector

A spike detector compares a sample with a robust local estimate and a robust
scale:

$$r_i = \frac{x_i - \operatorname{med}(x_{i-k/2..i+k/2})}
{\operatorname{med}(x_{i-k/2..i+k/2})},
\qquad \text{flag if } |r_i| > c\cdot1.4826\,\mathrm{MAD}(r).$$

The residual is *relative* because the noise is multiplicative; the constant
1.4826 converts a median absolute deviation into a Gaussian-equivalent standard
deviation; $c$ is a threshold in units of that scale.

### 3.2 What the demonstration measures

| $k$ | detector | flagged | true hits | false positives | mean gate error | fitted exponent |
|---|---|---|---|---|---|---|
| 3 | global MAD | 481 | 6 | 475 | 1.084% | 2.0320 |
| 3 | local MAD | 249 | 6 | 243 | 1.095% | 2.0320 |
| 5 | global MAD | 557 | 6 | 551 | 0.920% | 2.0317 |
| 5 | local MAD | 156 | 6 | 150 | 1.031% | 2.0320 |
| 9 | global MAD | 604 | 6 | 598 | 0.813% | 2.0312 |
| 9 | local MAD | 127 | 6 | 121 | 1.031% | 2.0321 |

(The gate error is measured against the clean measurement, signal plus drift, so
that it isolates the despiker instead of the un-removed offset.)

Three measured facts, each of which is a lesson:

1. **Every window finds all six spikes.** Detection was never the problem.
2. **The false-positive rate is one to two orders of magnitude worse than the
   detection rate.** Between 121 and 598 clean samples are flagged as spikes,
   because where the decay curves faster than the median window can follow, the
   residual is genuinely large. Estimating the scale *locally* halves the count
   (156 against 557 at $k=5$): a global MAD is dominated by the quiet late-time
   samples, where the relative noise is tiny, and so it sets a threshold that the
   normal-accuracy early samples violate.
3. **The measured consequences are small but non-zero.** A $1\%$ gate error and a
   fitted-exponent change that is visible in the fourth decimal (2.0317 against
   2.4126 for the ideal record — though most of that gap is the drift, not the
   despiker; see §7).

## 4. Drift removal and the "quiet window"

Drift removal is usually a straight-line (or polynomial) fit in a window that is
supposed to contain no signal, subtracted from the whole record. The
demonstration fits $x = a + bt$ in several windows of the same record and
measures the mean absolute gate error and the fitted decay exponent after
subtraction:

| window (ms) | fitted offset $a$ | fitted slope $b$ (s$^{-1}$) | mean gate error | fitted exponent |
|---|---|---|---|---|
| 30–40 | $1.570\times10^{4}$ | $4.968\times10^{7}$ | 1.93% | 2.4328 |
| 20–40 | $2.663\times10^{4}$ | $4.936\times10^{7}$ | 2.48% | 2.4494 |
| 10–40 | $6.893\times10^{4}$ | $4.801\times10^{7}$ | 4.92% | 2.5158 |
| 4–40 | $2.554\times10^{5}$ | $4.149\times10^{7}$ | 16.03% | 2.9032 |
| 0–40 | $6.777\times10^{7}$ | $-2.485\times10^{9}$ | 3988% | no positive signal left |

The ideal record fits an exponent of 2.4126 (the -3.5% offset from 2.5 is the
finite window and the curvature of $(t+t_0)^{-p}$). The genuinely quiet window
(30–40 ms, where the drift is 644 times the signal) recovers 2.4328 — within
0.8% — and the window that still contains signal absorbs part of the decay and
drives the exponent to 2.90. The last row is the failure mode to remember: fitting
the drift over the *whole* record fits the signal, subtracts it, and leaves the
late-time gates negative, so the exponent cannot even be computed.

**"Quiet window" is a model claim.** It asserts that within the window the
signal is negligible compared with the drift. That claim is testable (fit the
window, extrapolate, compare with an independent late-time model) and it should be
stated, because if it is false the error it introduces is a fixed fraction of the
*drift*, not of the noise — which is why row 4 is much worse than row 1 while the
noise is identical in both.

## 5. Low-pass filtering: the exchange rate

Filtering a record that changes by a factor of $10^{3}$ within the first filter
length is a trade, and the exchange rate is measurable. The demonstration
contrasts two quantities for a centred moving average of $m$ samples (one sample
= 19.54 $\mu$s):

| $m$ | noise suppression (measured) | $\sqrt{m}$ | gate-1 bias | gate-6 bias |
|---|---|---|---|---|
| 1 | 1.000 | 1.000 | 0.0000% | 0.0000% |
| 3 | 1.725 | 1.732 | +0.7244% | +0.0030% |
| 5 | 2.768 | 2.236 | +2.2001% | +0.0090% |
| 9 | 4.681 | 3.000 | +7.6655% | +0.0299% |
| 17 | 6.313 | 4.123 | +33.0756% | +0.1079% |

The noise suppression follows $\sqrt{m}$ closely for small $m$ and falls behind
for large $m$ (because the *signal* is being suppressed too, which the
bias-cancelling measurement method reveals as a shortfall against
$\sqrt{m}$). The bias is concentrated entirely at the earliest gate, where the
decay changes fastest, and grows super-linearly: $m=9$ costs 7.7% and $m=17$
costs 33.1% at that gate. A filter that looks harmless in a plot of the whole
record is a 33% amplitude error in the datapoint the interpreter cares most
about.

**The rule that follows.** The filter length must be short compared with the
timescale over which the signal changes across the earliest gate you intend to
report:
$m\,\Delta t \ll V/|\mathrm{d}V/\mathrm{d}t|$ at that gate. For the
$(t+t_0)^{-p}$ shape this timescale is $(t+t_0)/p$; at $t = 300\ \mu$s it is
$(4.0\times10^{-4})/2.5 = 160\ \mu$s, i.e. eight samples. The table shows
$m=9$ already outside it — which is exactly why $m=9$ costs 7.7%.

## 6. Stacking, error bars and rejection

For $N$ repeats the standard error of the mean is
$\mathrm{sem} = s/\sqrt{N}$, and for the synthetic gates
($N = 40$, $2\%$ single-shot error) the demonstration measures a first-gate
sem of $0.3452\%$ against a predicted $2\%/\sqrt{40} = 0.316\%$ — the ratio
$5.799$ against $\sqrt{40} = 6.325$, the difference being the finite sample.

An error bar is only as good as its assumptions. Contaminating three of the 40
repeats with a $25\%$ gain error produces

| gate | mean error | sem | clipped mean error | clipped sem | rejected |
|---|---|---|---|---|---|
| 1 | +1.753% | 0.345% | $-0.004\%$ | 0.368% | 3 |
| 2 | +2.381% | 0.226% | +0.476% | 0.234% | 3 |
| 3 | +2.374% | 0.284% | +0.466% | 0.302% | 3 |
| 6 | +1.896% | 0.287% | +0.074% | 0.309% | 3 |

The contaminated mean is wrong by 1.75–2.38%, which is **five to ten times its
own standard error**: the bar is too small by that factor, not because the
arithmetic is wrong but because the noise is not stationary across repeats. A
sigma-clip using a median-based scale removes the three bad repeats and the bias
disappears. Note that the clip leaves the standard error essentially unchanged
(0.345% → 0.368%): **rejecting outliers improves accuracy, not precision.**

## 7. A model-independent diagnostic: the fitted exponent

The demonstration fits a power law to the gated record and reports the exponent
for each processed version. Because the true exponent is known, this is a direct
measurement of the total processing bias:

| version | fitted exponent | error |
|---|---|---|
| ideal signal | 2.4126 | $-3.50\%$ (windowing) |
| raw | 2.0218 | $-19.13\%$ |
| despiked ($k=5$, local scale) | 2.0320 | $-18.72\%$ |
| despiked + drift from a quiet window | 2.4328 | $-2.69\%$ |
| despiked + drift from a window containing signal | 2.6454 | $+5.81\%$ |
| quiet drift removal + $m=9$ filter | 2.4356 | $-2.58\%$ |

Read down the third column: the drift is responsible for almost the whole of the
raw record's error (−19.1% vs the ideal −3.5%), the despiker changes it by
+0.4%, the correct drift removal recovers the exponent to within 0.8% of the
ideal, and the wrong drift window costs +5.8%. **An exponent is a far better
quality-control statistic than a residual**, because it depends on the shape of
the decay and not on its amplitude, and because its true value is known the
moment you build a synthetic.

## 8. Verification: telling a bias from scatter

The final section of the demonstration isolates each step's own bias by applying
it to the *ideal* record, where there is neither noise nor drift nor any spike:

| step | gate-1 error | gate-6 error | fitted exponent |
|---|---|---|---|
| moving average $m=3$ | +0.7244% | +0.0030% | 2.4129 |
| moving average $m=5$ | +2.2001% | +0.0090% | 2.4135 |
| moving average $m=9$ | +7.6655% | +0.0299% | 2.4156 |
| moving average $m=17$ | +33.0756% | +0.1079% | 2.4232 |
| running median $k=5,9,15$ | 0.0000% | 0.0000% | 2.4126 |

Two properties make these numbers identifiable as bias rather than noise: they
**do not move when the noise realisation changes**, and they **do move
monotonically with the step's own control parameter**. That is the practical test
recommended at the end of the demonstration, and it costs one synthetic run.

(The running median's zero error at the gates is a property of this particular
smooth, monotone signal sampled away from the record ends; a median filter is not
a no-op in general, and §3's false-positive counts are where it pays.)

## 9. Assumptions and regime of validity

1. **Knowledge of the true signal.** The bias measurements above are possible
   because a synthetic ground truth exists. On real data the same numbers must be
   *estimated* from a forward model — which is why the workflow must be validated
   on synthetic data that mimics the survey's dynamic range.
2. **A single decay shape.** A different $p$, or a multi-exponential decay,
   changes the bias table quantitatively (a flatter decay is filtered more
   gently). The qualitative rule — filter length $\ll$ the fastest timescale —
   does not change.
3. **Stationary, multiplicative noise.** The local-MAD detector assumes the
   relative noise level varies slowly compared with the detector window.
4. **Drift that is linear in time.** A thermally driven drift can be
   exponential; then the "quiet window" fit is a model misspecification, which is
   a *model* error, not a noise error.
5. **Independent repeats.** If the repeats share a coherent component (module
   [09-07-01](01-em-noise-and-coupling.md)), the standard error of the mean
   understates the true error by an unbounded factor.
6. **A recorded chain.** Every number above depends on the parameters; a result
   without them is not reproducible.

## 10. Worked examples

### Example 1 — filter length from the timescale rule

At the earliest gate of the synthetic record, $t = 300\ \mu$s and
$(t+t_0)/p = 160\ \mu$s. With $\Delta t = 19.54\ \mu$s, the largest filter that
still respects the rule is $m \approx 160/19.54 = 8.2$, i.e. $m = 7$ (odd
lengths keep the centre). The measured bias at $m=9$ is 7.7% and at $m=17$ is
33.1%, so the rule is close to the measured boundary: it is a design rule, and
its purpose is to keep you out of the 30% regime.

### Example 2 — what a despiker costs on clean data

The local-MAD detector flags 156 of 2048 samples ($7.6\%$) even though only six
are spikes. Each flagged sample is replaced by a running median, which on a
curved signal is a biased estimate. The measured mean gate error is 1.03%. That
is the *price of the detector*, and it is worth paying only if the spikes are
worse than 1%; with $0.5\times$ signal spikes present, they are.

### Example 3 — a drift budget

The demonstration's drift is $2.000\times10^{6}$ at the end of the record and the
late-time signal is $3.1056\times10^{3}$, so the drift is 644 times the signal.
Fitting a line in the window 30–40 ms leaves a mean absolute gate error of
1.93%, i.e. $6.6\times10^{3}$ in the units of the record — $0.33\%$ of the
drift. **The drift-removal error scales with the drift**, so a
drift that is negligible for an early-gate interpretation can be the dominant
error for a late-gate one, in the same record, with the same processing.

## 11. Python demonstration

[`code/em_processing_workflow_demo.py`](./code/em_processing_workflow_demo.py)
prints, with units:

1. the synthetic record: gates, dynamic range, and the drift/noise budget;
2. the despiking tables for global and local scale estimates, with true hits and
   false positives separated;
3. the drift-removal table across five windows;
4. the filtering table: measured suppression against $\sqrt{m}$, and the gate
   bias;
5. the stacking table with a contamination experiment, comparing the naive and
   clipped error bars;
6. the fitted exponent for six versions of the record;
7. the bias-isolation table on the ideal record.

```bash
cd 09-electrical-em-methods/07-em-data-processing-and-qc/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python em_processing_workflow_demo.py
```

It takes under half a second, requires no network, uses a fixed seed
(`np.random.default_rng(20261014)`) and exits 0.

## 12. Exercises

See
[`exercises/02-em-processing-workflow-exercises.md`](./exercises/02-em-processing-workflow-exercises.md)
and
[`exercises/02-em-processing-workflow-solutions.md`](./exercises/02-em-processing-workflow-solutions.md).

- **★** Compute the timescale $(t+t_0)/p$ at each of the six gates and state the
  longest filter that respects the rule at the first gate.
- **★★** Design a despiking rule for a record whose noise is additive and
  constant (not multiplicative), and explain why the detector statistic must
  change.
- **★★** Given the drift table, choose a window for a survey whose latest usable
  gate is 6 ms, and state the assumption you are relying on and how you would
  test it.
- **★★★** Write a processing log for the six-step chain of the demonstration that
  another analyst could reproduce, including the parameters you rejected and the
  measured bias that motivated each rejection.

## 13. Common mistakes

1. **Reporting the noise removed and not the bias introduced.** Both numbers
   belong in the log.
2. **Using a global scale for a multiplicative-noise record.** The threshold ends
   up set by the quietest part of the record.
3. **Fitting the drift where the signal lives.** The fit absorbs the signal.
4. **Choosing a filter length by eye.** Choose it from the fastest timescale in
   the data.
5. **Trusting the standard error of the mean.** It measures precision, not
   accuracy, and it assumes stationarity that data often lack.
6. **Treating the chain as a no-op on clean data.** The demonstration's ideal
   record shows that it is not.

## Mastery checkpoint

Complete this without notes.

> A time-domain EM record runs from 0.1 ms to 20 ms with 512 samples and a decay
> $V\propto t^{-2.5}$. **(a)** State the dynamic range of the signal and explain
> why an offset of $0.1\%$ of the first sample can matter. **(b)** Choose a
> moving-average length for a first gate at 0.3 ms, justify it with the timescale
> rule, and predict the gate-1 bias using the demonstration's measured ratio
> (bias grows roughly as $m^{3}$ in the measured table; state whether you are
> confident in that form and why). **(c)** Design a drift-removal window for a
> record whose latest usable gate is 6 ms, and state the assumption and the test.
> **(d)** Your stacked first gate has a standard error of 0.3% and a mean that
> differs from the previous repeat block's mean by 2%. State whether you believe
> the standard error, and name one diagnostic that decides it.

A worked version of (a) and (b) appears in the lesson-02
[solutions](./exercises/02-em-processing-workflow-solutions.md).

## Common pitfalls

1. **Removing noise and calling it improvement.** The distortion is the price.
2. **Treating a quiet window as a fact.** It is a claim about the data that must
   be tested.
3. **Letting the despiker decide the interpretation.** It sets the amplitude of
   the earliest gate, which is the one that carries the shallowest information.
4. **Confusing a small residual with a good model.** Residuals are largest where
   the data are largest, and the interesting gates are the small ones.
5. **Leaving the chain unrecorded.** Unrecorded parameters are unreproducible
   results.

## Related modules

- [09-07-01 EM Noise, Coupling and Cultural Effects](01-em-noise-and-coupling.md) —
  which of these steps is needed, decided by the noise taxonomy.
- [09-07-03 Quantifying Uncertainty in EM Interpretation](03-em-uncertainty.md) —
  how to carry the measured bias into a reported uncertainty.
- [05-06 Data Processing Principles](../../05-core-geophysics/06-data-processing-principles/README.md) —
  the general theory of the estimators used here.
- [22-data-engineering-reproducibility](../../22-data-engineering-reproducibility/README.md) —
  provenance, processing logs and reproducibility practice.
