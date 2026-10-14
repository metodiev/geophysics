# Solutions — 20-08-04 Change-Point Detection and Regime Shifts

> **Read after attempting the exercises.** Numbers were computed from the lesson
> demonstration or by exact arithmetic on its output.

Lesson: [04 Change-Point Detection and Regime Shifts](../04-change-point-and-detection.md).

---

## ★1 — The model and the objective

$$
y_t = \mu_k + \varepsilon_t,\quad t \in (\tau_{k-1}, \tau_k],
\qquad
\min_{K, \tau}\ \sum_k \mathrm{SSE}(\tau_{k-1},\tau_k) + \beta K .
$$

The fit term alone is degenerate because the sum of squared deviations from the
segment mean is zero for a segment of one sample, so the minimiser is every
sample as its own change point ($K = n$, objective 0). The complexity term
$\beta K$ is the only thing standing between the model and that answer, and it
is a free parameter that no data set determines.

---

## ★2 — Penalties at $n = 500$

$$
\log 500 = 6.2146 \approx 6.21, \qquad 2\log n = 12.43, \qquad 4\log n = 24.86 .
$$

(The demonstration's grid used 6.21, 12.42 and 24.84; the third is $4\log n$
rounded.) Detected counts were **2, 2 and 2** for the step series at 6.21, 12.42
and 24.84 — all correct — while $\beta = 2.00$ returned 11.

---

## ★3 — The segment cost

$\mathrm{SSE}(i,j) = \sum_{t=i+1}^{j}(y_t - \bar y_{i:j})^{2}$: the total squared
deviation of the samples in the interval $(i, j]$ from their own mean, i.e. the
residual sum of squares of a constant fit on that segment.

The dynamic program needs it for every pair because the objective is separable
by segment: $F(j) = \min_i [F(i) + \mathrm{SSE}(i,j) + \beta\mathbb{1}_{i>0}]$.
The separability is exactly what makes an *exact* solution possible in
$O(n^{2})$ rather than a search over all $\binom{n}{K}$ partitions, and it is
also a model statement — the segments are assumed independent.

---

## ★4 — The objective at $\beta = 2.0$

The fit term is a sum of squares; adding a split at the point that most reduces
the within-segment scatter reduces it by at least the local variance reduction,
which for a 500-point Gaussian series with $\sigma = 1$ is of order 1–3 per
split. The penalty is 2.0 per split, so any split that reduces the scatter by
more than 2 is accepted. Because pairwise splits of independent Gaussian data
reduce the SSE by an amount whose distribution has a mean of order
$\sigma^{2} = 1$ to 3, many are accepted, and the process stops only when every
remaining candidate split buys less than 2.0.

Hence 11 change points: the 2 real ones, whose splits reduce the scatter by
about $170 \times (2.5^{2}/4) \approx 265$ each (far above the penalty), and 9
extra splits of the within-regime noise. Each of the 9 is a genuine reduction of
the objective — this is not a bug. It is variance reduction purchased with
parameters, and the only defence is that the purchase price $\beta$ must exceed
the typical noise gain, which is why $\log n$ (6.21) works and 2.0 does not.

---

## ★5 — Choosing a penalty for an expensive false positive

Requirement: a false regime shift costs a year of work, so a per-series
false-detection rate of 1 % is a defensible requirement.

From the table: $\beta = 12.42$ (2 $\log n$) gave a measured rate of **0.015**
(1.5 %) and $\beta = 24.84$ gave **0.000** of 200 trials. With 200 trials the
latter is consistent with any rate below about 0.015, so the choice between them
is decided by detection power.

What is given up: from the ramp table, $\beta = 12.42$ and 24.84 both returned 4
steps for the ramp, while $\beta = 49.68$ returned 2. So raising the penalty from
12.42 to 24.84 cost nothing on that series, and raising it to 49.68 (8 $\log n$)
halved the number of detected steps in a gradual change — a real loss of
resolution for changes that are not abrupt. **Answer: $\beta = 24.84$**, with the
measured per-series error rate reported and the note that the rate is measured on
a *white-noise* null and would be higher for correlated noise.

---

## ★6 — The six false mean change points

Segment standard deviations 1.33, 2.75, 2.07, 2.86, 2.29, 3.10 against true
values of 1.0 (before sample 250) and 3.0 (after). Every segment lies in the
second half, and the standard deviations alternate around 3.0 rather than
tracking 1.0.

The mechanism: in a region whose variance is 3.0, the *mean* of a short block
deviates from 0 by about $3/\sqrt{m}$, which for blocks of 20-ish samples is
0.67. Splitting such a region at the point of largest block-mean deviation
reduces the SSE by roughly that squared deviation times the block size, which
exceeds the penalty. The detector is therefore modelling heteroscedasticity as a
sequence of small level shifts, and the alternating standard deviations are the
signature: consecutive segments are above and below the local mean of a series
that has no level structure at all.

The remedy is not a larger penalty (which would suppress all detections) but a
different cost: the variance-based cost $m\log(\mathrm{SSE}/m)$, which found the
single true change point at 250 and reported segment standard deviations 0.97 and
2.90.

---

## ★7 — Change points under AR(1) noise

**Cost function.** The Gaussian log-likelihood is no longer separable into
independent segments, because the covariance matrix of an AR(1) process is not
banded. Two practical routes:

1. **Decorrelate first**: apply the AR(1) whitening filter
   $y_t \to y_t - \rho y_{t-1}$, fit the piecewise-constant model to the
   whitened series, and note that the *step* in the original series becomes a
   decaying transient in the whitened one — so the model family has changed.
2. **Keep the likelihood in the objective**: replace SSE with
   $\log\lvert C\rvert + r^{T}C^{-1}r$ for the AR(1) covariance $C$, which
   destroys the $O(n^{2})$ separability and requires either a restricted model or
   a coarser search.

**Calibration.** Simulate AR(1) series with the estimated $\rho$ and $\sigma$,
run the detector at a range of penalties, and pick the penalty that gives the
required per-series rate — exactly as in §3, with the null changed.

**Prediction.** The calibrated penalty is **larger** than for white noise at the
same per-series rate, because autocorrelation reduces the effective number of
independent observations, so the noise-driven scatter reduction available from a
split is larger relative to the number of independent samples. This is the same
$n_{\text{eff}}$ effect measured in lessons 01 and 05.

**Diagnostic.** Report the measured per-series false-detection rate at the chosen
penalty on the *simulated AR(1)* null, and — preferably — repeat the calibration
on a surrogate built by phase-randomising the residuals, so that the calibration
does not depend on the AR(1) assumption being exactly right.

---

## ★8 — Ramp versus steps: deciding

**Model families.** (A) Piecewise-linear, with $K$ slope changes at unknown
epochs; (B) piecewise-constant with $K'$ mean shifts. Family A has three
parameters per change (epoch, and the two slopes or the slope increment and the
level continuity), family B has two (epoch and the step size).

**Criterion.** Compare penalised likelihoods with a penalty that accounts for the
different parameter counts: $\mathrm{SSE} + \beta p$ with $p$ the number of free
parameters, or BIC with $p \log n$. Because A nests a ramp exactly and B does
not, A will fit a ramp with fewer parameters; B will fit a series of genuine steps
with fewer. A likelihood-ratio-like comparison is valid only if both are fitted
exhaustively, which for A requires a two-dimensional search over epoch and slope
increment (differentiable, so tractable).

**Smallest distinguishable step count.** Generate a sequence of $K$ equal steps
spaced evenly, and find the smallest $K$ for which family A is rejected at the
chosen level: as $K$ rises the staircase approaches a ramp and the two families
become indistinguishable, while for $K = 1$ they are trivially different. The
answer is a curve of detectability against $K$ at a stated record length; the
honest output is that curve, because it shows that "ramp or steps" is not
answerable in general and depends on how many steps the process actually has.
