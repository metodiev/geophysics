---
id: 20-08-04
title: "Change-Point Detection and Regime Shifts"
level: research
prereqs: ["20-08-01", "20-08-03", "21-01-03"]
tags: [signal-processing, time-series, change-point, segmentation, model-selection, penalty]
---

# Change-Point Detection and Regime Shifts

**All models and data in this module are SYNTHETIC.** The series below are
chosen piecewise-constant levels, a chosen ramp and chosen variance changes, all
with seeded Gaussian noise. No real series, catalogue or instrumental record is
used.

## Learning objectives

By the end of this lesson you will be able to:

1. **Formulate** change-point detection as penalised model selection and
   **write** the objective, naming the penalty as a free parameter.
2. **Solve** the single-mean change-point problem exactly by dynamic
   programming over all partitions.
3. **Derive** the cost of a segment and **explain** why the search must be
   penalised, using the measured number of change points at small penalty.
4. **Measure** the false-positive rate of the detector as a function of the
   penalty, and **choose** a penalty from a stated error rate.
5. **Demonstrate** that a gradual change is represented by several steps, and
   **state** why the count is not a property of the process.
6. **Compare** a mean-change detector with a variance-change detector on the same
   data and **state** what each is allowed to detect.
7. **State** the assumptions under which a detected change point is a regime
   shift in the Earth rather than an artefact of the model.

## Prerequisites

- [20-08-01 Detrending, Deseasonalising and Anomalies](01-detrending-seasonality.md)
  — trend fitting, and the slope-change case that motivates this lesson.
- [20-08-03 Geodetic Time Series: Trends, Offsets, Noise Models](03-geodetic-time-series.md)
  — offsets in a regression design, which is the same problem with the epochs
  given.
- [21-01-03 Resampling](../../21-statistics-bayesian-ml/01-statistics-in-practice/03-resampling.md)
  — the general problem of choosing a decision threshold against a stated error
  rate.

The runnable companion is
[`code/change_point_demo.py`](code/change_point_demo.py); the graded problems are
in
[`exercises/04-change-point-and-detection-exercises.md`](exercises/04-change-point-and-detection-exercises.md).

## 1. The problem as penalised model selection

A piecewise-constant mean model with change points at
$\tau_1 < \dots < \tau_K$ is

$$
y_t = \mu_k + \varepsilon_t, \qquad t \in \left(\tau_{k-1}, \tau_k\right],
\qquad \varepsilon_t \sim \mathcal{N}(0, \sigma^{2}) ,
$$

and the least-squares fit for a fixed set of change points is just the segment
means. The number and location of the change points are the unknowns, so the
problem is one of **model selection**, and the objective is

$$
\min_{K, \tau_1, \dots, \tau_K}\
\underbrace{\sum_{k} \mathrm{SSE}(\tau_{k-1}, \tau_k)}_{\text{fit}}
\; + \; \underbrace{\beta K}_{\text{complexity}} ,
$$

with $\mathrm{SSE}(i,j) = \sum_{t=i+1}^{j}\left(y_t - \bar y_{i:j}\right)^{2}$.
The first term always decreases as $K$ grows — take $K = n$ and it is zero — so
without $\beta K$ the answer is "every sample is a change point". This lesson is
about $\beta$, and about the fact that no data set determines it.

The demonstration uses a 500-sample series with means $0.0$, $-2.5$ and $+2.0$
over three regimes separated at samples 170 and 340, with $\sigma = 1.0$, and
solves the problem **exactly** by dynamic programming over all partitions:

$$
F(j) = \min_{i} \left[ F(i) + \mathrm{SSE}(i, j) + \beta\,\mathbb{1}_{i>0} \right],
\qquad F(0) = 0 ,
$$

with backtracking to recover the change points. It also imposes a minimum
segment length of 20 samples, which is itself a modelling choice: it caps the
time resolution of any regime the analysis can report, and it must be stated
because a detector with a 1-sample minimum will always find something.

## 2. The penalty, and what it controls

| $\beta$ | $\beta / \log n$ | change points detected | locations |
|---|---|---|---|
| 2.00 | 0.32 | **11** | 21, 42, 170, 200, 243, 283, 311, 340, … |
| 6.21 | 1.00 | 2 | 170, 340 |
| 12.42 | 2.00 | 2 | 170, 340 |
| 24.84 | 4.00 | 2 | 170, 340 |
| 49.68 | 7.99 | 2 | 170, 340 |
| 99.36 | 15.99 | 2 | 170, 340 |

$\log n = 6.21$ for $n = 500$. The behaviour has the shape it must have:

- At $\beta = 2.0$ the detector returns 11 change points. Exactly **two** of
  them are real. The other nine are extra splits of the regions between the true
  changes, and none of them corresponds to anything in the generator. They are
  the fit term buying variance reduction with parameters, which is the entire
  reason a penalty exists.
- From $\beta = \log n$ upward the answer is stable at the two true points. The
  stability across a factor of 16 in $\beta$ (6.21 to 99.36) is the reassuring
  feature: the conclusion does not depend on fine-tuning the penalty *here*.

The stability is a property of this signal-to-noise ratio. The jumps are 2.5 and
2.0 in units of $\sigma = 1.0$, which is a strong signal; at a jump of
$0.5\sigma$ the interval of $\beta$ giving the right answer would be narrower,
and below some amplitude no penalty recovers the truth.

## 3. The false-positive rate: the penalty is an error rate

To choose $\beta$ you need the null distribution, and the null is the answer to
"how often does the detector fire when nothing changed?". The demonstration runs
200 realisations of pure Gaussian noise and counts the fraction with at least
one change point:

| $\beta$ | $\beta/\log n$ | fraction with $\ge 1$ change point |
|---|---|---|
| 6.21 | 1.00 | 0.415 |
| 12.42 | 2.00 | 0.015 |
| 24.84 | 4.00 | 0.000 |
| 49.68 | 7.99 | 0.000 |

The classical BIC penalty, $\beta = \log n$ (one parameter per change point),
produces a **41.5 %** false-positive rate in this setting, not the 5 % a reader
of a $p$-value might expect. The failure has a known cause: the model-selection
penalty is asymptotic, and it is being used to control a finite-sample
family-wise error rate over $\binom{n}{2}$ candidate splits. Doubling it to
$2\log n$ brings the rate to 1.5 %, and $4\log n$ to 0 in 200 trials.

The relevant error rate is **per series**, not per sample, because the detector
searched the whole record for the best split. This is the multiplicity problem
of lesson 05 in a different guise, and it has the same remedy: state the error
rate you intend, measure the penalty that achieves it on your own null, and
report both.

### 3.1 Where the penalty values come from

The two penalty scales used above are worth deriving, because they explain both
why $\log n$ is the natural starting point and why it under-performs here.

For a Gaussian mean-shift model the maximised log-likelihood of a segmentation
with total sum of squares $\mathrm{SSE}$ over $n$ samples is, up to constants,
$-\tfrac{n}{2}\log(\mathrm{SSE}/n)$. The BIC criterion is

$$
\mathrm{BIC} = -2\log\hat L + p\log n
= n\log\!\left(\frac{\mathrm{SSE}}{n}\right) + p\log n + \text{const},
$$

where $p$ is the number of free parameters. Adding one change point adds **one**
new segment mean (one parameter) and, if the epoch is also estimated, **two**.
That is the origin of $\beta = \log n$ and $\beta = 2\log n$: the first counts
only the mean, the second also counts the epoch.

The reason $\beta = \log n$ yields a 41.5 % per-series false-positive rate is not
that the derivation is wrong but that it answers a different question. BIC is
consistent for **model order**: given a fixed family and a true model of finite
order, it selects that order with probability tending to 1. It says nothing about
the false-positive *rate* at a finite $n$ when the procedure also searches over
all epochs — there are $\binom{n}{2}$ candidate splits, each with its own
fluctuation, and the resulting per-series error is not the $\alpha$ of a
pointwise test. Doubling the penalty to $2\log n$ (counting the epoch as a
parameter as well) is the cheapest repair, and it measured 0.015; calibration
against the measured null is the honest one.

**Worked example.** With $n = 500$, $\log n = 6.21$ and the two scales are 6.21
and 12.42. The measured per-series false-positive rates were 0.415 and 0.015 —
the same statistic, a factor 28 apart, from two penalty values that differ by a
factor 2 in a formula whose justification is asymptotic.

### 3.2 Choosing $\beta$, in order

1. **State the error rate.** A false detection of a regime shift is usually the
   expensive error, so a per-series rate of 1–5 % is a common requirement.
2. **Generate the null.** For a mean-shift detector on Gaussian noise, simulate
   the same length with the same noise; for correlated noise, simulate *that*.
   The demonstration's null is white, and a red-noise series would move every
   number in §3 upward.
3. **Measure the rate at several penalties** and pick the smallest that meets
   the requirement — smaller penalties detect weaker real changes.
4. **Report the penalty, the minimum segment length and the measured false
   positive rate**, because none of the three is inferable from the other two.

## 4. A ramp is not a step

The cleanest illustration that the detected number is a property of the model,
not of the process: a series whose *slope* changes (0.004 per sample for 250
samples, then 0.016 after) segmented with a mean-shift model.

| $\beta$ | steps detected | locations |
|---|---|---|
| 12.42 | 4 | 188, 299, 370, 447 |
| 24.84 | 4 | 188, 299, 370, 447 |
| 49.68 | 2 | 283, 371 |

The best 4-step model reconstructs the ramp with rms error **0.292** against a
noise level of 1.0 — a good fit by any measure — and the penalty-per-step column
of the demonstration (125.29, 137.71 and 305.06 for the three penalties) shows
that each step is earning its place in the objective. Nothing here is
misbehaving. What the analysis has done is approximate one physical process (a
gradual change) by several of a different kind (abrupt shifts), because that is
what the model family allows.

Two consequences:

- **"The series has $K$ regime shifts" is not a measurement.** It is
  $\left(K, \text{model family}, \beta, \text{minimum segment}\right)$.
- **The alternative model family is usually available.** A piecewise-linear fit
  with one slope change would represent the ramp with two parameters instead of
  five, and would be preferred by any sensible criterion — but it requires
  fitting slopes, i.e. changing the family, which is a decision the detector
  cannot make for you.

## 5. What is allowed to change?

A mean-shift detector searches for changes in the mean. Give it a series whose
*mean is zero throughout* and whose standard deviation steps from 1.0 to 3.0 at
sample 250, and it still returns changes:

| search | cost function | change points |
|---|---|---|
| mean-based, $\beta = 24.84$ | SSE | 6: 274, 348, 368, 391, 432, 459 |
| variance-based, $\beta = 12.42$ | $m\log(\mathrm{SSE}/m)$ | 1: 250 |

Not one of the six mean-based change points is at 250; all six lie in the
noisier second half, where a level shift is the best available way to reduce the
sum of squares. The segment standard deviations of that fit run 1.33, 2.75,
2.07, 2.86, 2.29, 3.10 — alternating on either side of the true 3.0, which is the
signature of mean-fitting to a heteroscedastic series. The variance-based cost
places its single change point exactly at 250, and the segment standard
deviations it reports are 0.97 and 2.90 against a truth of 1.0 and 3.0.

The mean-based detector is not wrong. It is answering a different question, and
the answer it gives is dominated by the feature the model permits. **Before
detecting change, state which distributional feature is allowed to change:**
mean, variance, slope, autocorrelation or spectrum. Each choice gives a
different answer on the same numbers, and several of them will be internally
consistent.

## 6. Assumptions and regime of validity

1. **The noise is stationary and Gaussian within each segment.** The cost
   $\mathrm{SSE}$ is a Gaussian likelihood. Autocorrelated noise inflates the
   effective number of independent samples, and — as in lesson 05 — the penalty
   must rise accordingly or the false-positive rate explodes.
2. **Abrupt changes.** A gradual change is represented by several steps (§4);
   the detector cannot distinguish that representation from several real steps.
3. **The signal-to-noise ratio is adequate.** With jumps of 2–2.5$\sigma$ here,
   a wide range of penalties works. Nothing in this lesson quantifies the
   detection limit, which depends on the segment lengths and is a subject in its
   own right.
4. **One change type at a time.** The commonest failure in practice is fitting a
   mean change to a variance change (§5) or vice versa. A defensible analysis
   fits the model with both terms, or states explicitly which is excluded.
5. **The dynamic program is exact; the choice of family is not.** Optimality
   within a family says nothing about the family being right.
6. **Independence between segments is assumed when comparing penalties.** The
   objective is separable by construction, which is what makes the dynamic
   program valid, and it is a model statement about the process rather than a
   property of it.
7. **SYNTHETIC.** Levels, epochs, ramp and variance step are all chosen.

## Mastery checkpoint

Without notes: **(a)** write the penalised objective and explain why the fit term
alone is degenerate; **(b)** state the measured false-positive rate at
$\beta = \log n$ and at $2\log n$ and say which you would report; **(c)** from
§4, state the rms error of the best 4-step reconstruction of the ramp and
explain why the number of detected steps changes when the penalty is tripled;
**(d)** design, in words, a test for whether a series has a step in the mean
rather than in the variance, naming the two cost functions; **(e)** state three
numbers you would report alongside a detected change point so that a reader
could reproduce your error rate.

A worked answer to (a)–(c) appears in the
[solutions](exercises/04-change-point-and-detection-solutions.md).

## Common pitfalls

1. **Reporting a change point without the penalty.** At $\beta = 2.0$ the
   detector returned 11, of which 2 were real.
2. **Using the BIC penalty as though it controlled the error rate.** It gave
   0.415 here; the requirement is per series and driven by the search.
3. **Treating $K$ as a measurement.** The count moved from 4 to 2 for the same
   ramp when $\beta$ rose from 24.84 to 49.68.
4. **Fitting mean shifts to a heteroscedastic series.** Six mean change points,
   none of them at the true variance change.
5. **Forgetting the minimum segment length.** It is a modelling choice, it caps
   the resolution, and it is invisible in the output if unreported.
6. **Assuming Gaussian white noise because it is the default.** With
   autocorrelated noise the false-positive rate rises and the penalty must
   change; the demonstration's null is white, and that is a documented
   simplification.
7. **Ignoring the signed size of the change.** A change point's epoch and its
   magnitude are both estimates with uncertainties; reporting only the epoch
   hides the second.

## Related modules

- [20-08-01 Detrending, Deseasonalising and Anomalies](01-detrending-seasonality.md)
  — the slope-change series that §4 generalises.
- [20-08-03 Geodetic Time Series: Trends, Offsets, Noise Models](03-geodetic-time-series.md)
  — offsets with known epochs, which is this problem with the search removed.
- [20-08-05 Climate Time-Series Analysis and Modes of Variability](05-climate-timeseries.md)
  — the same multiplicity logic applied to spectral peaks.
- [21-07-02 State-Space Models](../../21-statistics-bayesian-ml/07-time-series-and-forecasting/02-state-space.md)
  — change points as latent states, with the penalty replaced by a prior.
