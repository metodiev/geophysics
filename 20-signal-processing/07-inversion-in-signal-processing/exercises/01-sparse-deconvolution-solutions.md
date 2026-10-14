# Solutions — 20-07-01 Sparse and L1 Deconvolution

> **Read after attempting the exercises.** Numbers were computed from the lesson
> demonstration or by exact arithmetic on its output; where more than one answer
> is defensible, that is said.

Lesson: [01 Sparse and L1 Deconvolution](../01-sparse-deconvolution.md).

---

## ★1 — Soft thresholding

$\operatorname{prox}_{t\lvert\cdot\rvert}(x) = \operatorname{sign}(x)\max(\lvert x\rvert - t, 0)$.

| $x$ | $t$ | $\lvert x\rvert - t$ | result |
|---|---|---|---|
| 3.0 | 0.5 | 2.5 | $+2.5$ |
| $-0.2$ | 0.5 | $-0.3$ | $0$ |
| 0.4 | 0.5 | $-0.1$ | $0$ |
| 0.4 | 1.0 | $-0.6$ | $0$ |

The last three are the sparse outcomes: the coefficient is set to **exactly**
zero, not shrunk towards it. Sparsity in an L1 solution is produced by this
threshold and by nothing else.

---

## ★2 — Step size

$1/L$ with $L = 11.961$: $1/L = 0.083605$.
$1/L$ with $L = 11.934$: $1/L = 0.083794$.

Relative difference: $(0.083794 - 0.083605)/0.083605 = 2.26\times10^{-3}$, i.e.
0.23 %. Using the power-iteration estimate costs 0.2 % in step size and at most
that in convergence rate; the check is that it is an *over*-estimate or an
under-estimate that matters, not the size of the error.

---

## ★3 — Why ISTA diverges at $L = 8.0$

$L$ must satisfy $L \ge \lVert W \rVert_2^{2}$; the gradient step
$x - \frac{1}{L}W^{T}(Wx - d)$ is a contraction only for $\frac{1}{L} \le
1/\lVert W \rVert_2^{2}$. The measured $\lVert W \rVert_2^{2} = 11.961$, so
$L = 8.0$ is an **under**-estimate by a factor $11.961/8.0 = 1.495$, the
effective step is 1.495 times too long, and the iteration diverges (or oscillates
without converging). Over-estimating $L$ merely slows convergence; that is why
the safe implementation takes $L$ from the SVD or from a converged power
iteration and never from a guess.

---

## ★4 — Choosing a penalty

Constraints: amplitude ratio $\ge 0.85$ and residual $\le 12$ %.

| $\lambda$ | residual (%) | amplitude ratio | meets both? |
|---|---|---|---|
| 0.01 | 4.23 | 0.895 | residual yes, bias yes |
| 0.05 | 6.35 | 0.857 | yes |
| 0.10 | 9.62 | 0.806 | residual yes, bias **no** (0.806 < 0.85) |
| 0.30 | 25.46 | 0.599 | **no** |
| 1.00 | 65.76 | 0.196 | **no** |

**Answer: $\lambda = 0.05$**, with residual 6.35 % and amplitude ratio 0.857.
$\lambda = 0.01$ has a better amplitude ratio (0.895) and a residual of 4.23 %
that is *below* the 5 % noise level, i.e. it is fitting noise; if the requirement
is read as "residual at or below the noise level but not below it", 0.01 is
defensible and the two answers should be reported together with that reading.
What is given up at 0.05 is resolution: 18 nonzero samples against 73 at 0.01,
so closely spaced spikes are merged. The exchange must be stated; it cannot be
optimised away.

---

## ★5 — Counting samples at matched residual

L1 at $\lambda = 0.10$: 19 samples above $10^{-3}$, i.e. 19/400 = 4.8 % of the
record. L2 at $\mu = 0.2256$: using the 50 %-of-peak count as the fair analogue
of "clearly present", 13 samples, i.e. 3.3 %; using the 10 %-of-peak count, 73
samples, 18.3 %.

The comparison is only fair at matched residual because the residual is the
common currency: with the same misfit, any difference in the solution is
attributable to the penalty and not to the fit. Comparing a well-fit L2 solution
with a badly-fit L1 solution would show, trivially, that the better fit looks
more like the data — and would say nothing about the two priors. The honest
statement is: *at 9.5 % residual, the L1 solution concentrates the same energy
into 13–19 samples where the L2 solution spreads it over 73 or more.*

---

## ★6 — Four kurtoses

The kurtosis $\mathbb{E}[(x-\mu)^{4}]/\sigma^{4}$ measures tail weight; it is 3
for a Gaussian. The four values:

- **Reflectivity, 45.961.** Twelve spikes in 400 samples is an extremely
  heavy-tailed distribution: almost all samples are zero.
- **Data, 13.114.** Convolution with the wavelet fills in the zeros; the
  band-limited trace is much closer to Gaussian than the spike train that made
  it. This is the loss the sparse prior has to undo.
- **L1 solution, 49.190.** The estimator has restored the heavy-tailed
  character, and slightly over-restored it.
- **L2 solution, 15.314.** Barely different from the data: the L2 prior assumes
  a Gaussian and returns something Gaussian-like.

The L1 solution's 49.190 is nearer the truth (45.961) than the data's 13.114
because the estimator *imposes* heavy tails by construction — the soft
threshold makes exact zeros and leaves the surviving coefficients large. The
number is therefore evidence that the prior is doing what it claims, and not
independent evidence that the Earth is spiky.

---

## ★7 — Experiment specification

**Generator.** A spike train of $K = 10$ spikes with amplitudes drawn once and
fixed, so that the amplitude bias is comparable across cells. Signal-to-noise
ratio varied by scaling a single seeded noise realisation across the sweep so
that the noise realisation is shared (paired design).

**Metric.** Mean of $\hat r_i / r_i$ over the true support, reported with the
scatter over 50 trials per cell. Secondary metric: the fraction of true spikes
recovered within one sample.

**Sweep.** Local SNR levels of 1, 2, 5, 10, 20, 50, at a fixed $\lambda$
chosen so that the false-discovery count stays below one; and, orthogonally, a
sweep of $\lambda$ at a fixed SNR of 10.

**Prediction.** The shrinkage ratio rises monotonically towards 1 with SNR,
following the soft-threshold arithmetic: a coefficient is recovered at
$\lvert c \rvert - \lambda/L$ in the coefficient domain, so the fractional bias
scales as $\lambda/(L\lvert c \rvert)$ and vanishes as $1/\text{SNR}$.

**Debiasing.** After support identification, refit by unpenalised least squares
on the support. Prediction: the bias goes to zero and the variance rises,
because the unpenalised fit amplifies noise on the selected support. Where it
should **hurt**: when the identified support is wrong (low SNR, close spikes),
the least-squares refit will assign large amplitudes to wrong locations, so the
bias metric improves while the false-discovery rate worsens. Reporting both
metrics is part of the design.

---

## ★8 — Two subgradient numbers

The two checks are different objects. On the support the condition is an
*equality* — a stationarity equation whose residual shrinks as the iteration
converges; at the level of the FISTA stopping tolerance it was $1.7\times10^{-7}$.
Off the support the condition is an *inequality*,
$\lvert W^{T}(Wr-d)_i\rvert \le \lambda$, and the reported quantity is the
violation $\max(0, \lvert\cdot\rvert_i - \lambda)$; a converged solution
satisfies it exactly, in the sense that the inequality is not marginally
satisfied but holds with room to spare, so the violation is exactly $0$.

With 20 iterations instead of 800, the support itself would differ: ISTA/FISTA
identify the support early and then spend most iterations refining amplitudes, so
the equality residual would be larger (order $10^{-2}$–$10^{-1}$) while the
inequality violation would likely still be 0 for the entries that were never
activated — a solution can be "sparse and infeasible" or "feasible and
non-stationary", and only the two numbers together distinguish them. The check is
worth running precisely because one of the two can be satisfied by an
unconverged iterate.
