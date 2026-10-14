---
id: 20-07-01
title: "Sparse and L1 Deconvolution"
level: research
prereqs: ["20-04-01", "20-01-03", "18-02-02"]
tags: [signal-processing, time-series, sparse-inversion, l1-norm, deconvolution, regularisation]
---

# Sparse and L1 Deconvolution

**All models and data in this module are SYNTHETIC.** The trace used below is a
chosen spike train convolved with a chosen Ricker wavelet plus seeded noise. No
field data and no published measurement appears anywhere in this lesson.

## Learning objectives

By the end of this lesson you will be able to:

1. **Formulate** deconvolution as a linear inverse problem and **identify** the
   three ingredients that make it ill-posed: band limitation, noise and the
   null space of the convolution operator.
2. **Derive** the soft-thresholding operator as the proximal map of the L1 norm
   and **verify** it numerically against a direct minimisation.
3. **Implement** ISTA and FISTA and **state** why the step size is $1/L$ with
   $L = \lVert W \rVert_2^2$.
4. **Measure** the three-way trade-off of the L1 model — residual, sparsity and
   amplitude shrinkage — and **choose** a penalty against a stated criterion.
5. **Explain** why L1 recovers a spike train that damped least squares smears,
   and **quantify** the resolution difference.
6. **Check** the first-order optimality conditions of an L1 solution, including
   the subgradient condition at the exactly-zero entries.
7. **State** the assumptions under which a sparse solution is meaningful and the
   regime in which it is not.

## Prerequisites

- [20-04-01 Deconvolution: Concept, Ill-Posedness and Stabilisation](../04-deconvolution-and-inverse-filtering/01-deconvolution-concept.md)
  — the convolutional model, water level and the language of ill-posedness.
- [20-01-03 Convolution, Correlation and Filtering](../01-signals-and-systems/03-convolution-and-filters.md)
  — the discrete convolution matrix and its adjoint.
- [18-02-02 Underdetermined Problems](../../18-inverse-problems/02-linear-inverse-problems/02-underdetermined.md)
  — why a null space forces a choice, and how a norm makes the choice.

The runnable companion is
[`code/sparse_deconvolution_demo.py`](code/sparse_deconvolution_demo.py); the
graded problems are in
[`exercises/01-sparse-deconvolution-exercises.md`](exercises/01-sparse-deconvolution-exercises.md).

## 1. The problem, and why it is not a matrix inversion

Write the convolutional model as a matrix equation. With $d \in \mathbb{R}^{n}$
the recorded trace, $r \in \mathbb{R}^{n}$ the reflectivity we want, $g$ the
wavelet and $W$ the convolution operator,

$$
d = W r + \eta, \qquad \eta \sim \mathcal{N}(0, \sigma^{2} I).
$$

$W$ is a Toeplitz matrix, band-limited in the sense that $G(\omega) = \hat{g}$
decays to zero outside a passband, so its smallest singular values are tiny
rather than zero. The demonstration builds $W$ explicitly for $n = 400$ samples
at $\Delta t = 4\ \mathrm{ms}$ with a 30 Hz Ricker wavelet of 61 samples, and
measures

$$
\lVert W \rVert_2^{2} = 11.961 \quad \text{(from the SVD)}, \qquad
\kappa(W) = 3.659 \times 10^{5}.
$$

A condition number of $3.7\times10^{5}$ is not catastrophic in double precision
by itself, but it means a plain solve amplifies the noise by that factor in the
worst case, and the noise here is real: the demonstration adds
$\sigma = 0.00815$, exactly 5.0 % of the signal rms.

Two independent checks of the same scalar make the first section useful rather
than decorative:

| route | $\lVert W \rVert_2^2$ |
|---|---|
| exact, largest singular value of $W$ | 11.961 |
| power iteration on $W^{T}W$, 200 steps | 11.934 |

The 0.2 % difference is the power iteration still converging, not an
inconsistency; the iteration converges at a rate set by the ratio of the two
largest singular values, which is why 200 steps are enough for two significant
figures and not for six. The demonstration also reports
$\max\lvert W - W^{T}\rvert = 0$, i.e. the operator is **symmetric**: a
zero-phase wavelet gives a symmetric convolution matrix, and every fact we
derive for symmetric $W$ (real eigenvalues, an orthonormal eigenbasis) is
applicable.

## 2. Two estimators, one fit

The damped least-squares (L2) estimator solves

$$
\hat{r}_{\mathrm{L2}} = \arg\min_{r}\ \tfrac{1}{2}\lVert W r - d \rVert_2^{2}
+ \tfrac{\mu}{2}\lVert r \rVert_2^{2}
= \left( W^{T}W + \mu I \right)^{-1} W^{T} d .
$$

The L1 estimator solves

$$
\hat{r}_{\mathrm{L1}} = \arg\min_{r}\ \tfrac{1}{2}\lVert W r - d \rVert_2^{2}
+ \lambda \lVert r \rVert_1 , \qquad \lVert r \rVert_1 = \sum_i \lvert r_i \rvert .
$$

Only the second is nonlinear, because $\lVert r \rVert_1$ is not
differentiable at zero. That non-differentiability is the entire reason L1
returns exact zeros: at $r_i = 0$ the objective has a kink, and the subdifferential

$$
\partial \lvert r_i \rvert =
\begin{cases}
\{\operatorname{sign}(r_i)\}, & r_i \neq 0,\\
[-1, 1], & r_i = 0,
\end{cases}
$$

admits zero as a solution whenever the data gradient is not too large. L2 has no
such interval and never produces a zero.

### 2.1 The one worked number to carry

Before any algorithm, the demonstration verifies the scalar fact on which every
ISTA/FISTA implementation depends:

$$
\operatorname{prox}_{t\lvert\cdot\rvert}(x)
= \arg\min_{u}\ \tfrac{1}{2}(u - x)^{2} + t\lvert u \rvert
= \operatorname{sign}(x)\max(\lvert x \rvert - t,\ 0).
$$

Numerically minimising the right-hand side on a grid of $2\times10^{6}$ points
and comparing with the closed form gives:

| $x$ | $t$ | closed form | numerical argmin | difference |
|---|---|---|---|---|
| $2.00$ | $1.00$ | $1.000000$ | $1.000000$ | $8.9\times10^{-16}$ |
| $2.00$ | $0.20$ | $1.800000$ | $1.800000$ | $6.7\times10^{-16}$ |
| $-0.40$ | $1.00$ | $0.000000$ | $0.000000$ | $0.0$ |
| $-0.40$ | $0.20$ | $-0.200000$ | $-0.200000$ | $7.2\times10^{-16}$ |
| $0.15$ | $1.00$ | $0.000000$ | $0.000000$ | $0.0$ |
| $0.15$ | $0.20$ | $0.000000$ | $0.000000$ | $0.0$ |

The last three rows are the mechanism: any coefficient whose magnitude is below
the threshold is **set to exactly zero**, and the information it carried is
discarded rather than reduced. Everything L1 does well and everything it does
badly follows from this single line.

## 3. ISTA and FISTA

The proximal gradient iteration for the L1 problem is

$$
r^{(k+1)} = \operatorname{prox}_{\lambda/L\,\lvert\cdot\rvert}
\left( r^{(k)} - \tfrac{1}{L} W^{T}\left( W r^{(k)} - d \right) \right),
\qquad L = \lVert W \rVert_2^{2},
$$

which is ISTA. FISTA adds the momentum sequence
$t_{k+1} = \tfrac{1}{2}\left(1 + \sqrt{1 + 4t_k^{2}}\right)$ and evaluates the
gradient at the extrapolated point
$y^{(k)} = r^{(k)} + \tfrac{t_k - 1}{t_{k+1}}\left(r^{(k)} - r^{(k-1)}\right)$.
FISTA needs $L$ (it may overestimate but never underestimate, or the iteration
diverges) and needs no line search. The demonstration uses the exact
$L = 11.961$ from the SVD and 800 iterations.

## 4. The trade-off, measured

The demonstration draws a reflectivity of 12 spikes in 400 samples. Its kurtosis
is **45.961**, i.e. it is strongly non-Gaussian; convolution with the wavelet
lowers the measured kurtosis of the data to **13.114**, and the noise is 5 % of
the signal rms. Then it solves the L1 problem for a range of $\lambda$:

| $\lambda$ | nonzero samples | residual (%) | amplitude ratio on true support | kurtosis of the solution |
|---|---|---|---|---|
| 0.01 | 73 | 4.23 | 0.895 | 46.420 |
| 0.05 | 18 | 6.35 | 0.857 | 47.505 |
| 0.10 | 19 | 9.62 | 0.806 | 49.190 |
| 0.30 | 19 | 25.46 | 0.599 | 60.745 |
| 1.00 | 9 | 65.76 | 0.196 | 120.393 |
| 3.00 | 0 | 100.00 | 0.000 | n/a |
| 10.00 | 0 | 100.00 | 0.000 | n/a |

Read the table from small $\lambda$ to large and three things move together:

- **Residual** rises monotonically. This is not failure; it is the definition of
  a penalised estimator. At $\lambda = 0.01$ the residual is 4.23 %, which is
  at the noise level (5 %), so that solution is fitting signal and noise alike.
- **Sparsity** improves at first (73 $\to$ 18 $\to$ 19) and then collapses to
  zero. The true reflectivity has 12 nonzero samples; no $\lambda$ returns
  exactly 12, because the estimator does not know the truth and the spikes have
  unequal amplitudes.
- **Amplitude ratio**, the mean of $\hat r_i / r_i$ over the true support, falls
  below 1 immediately and keeps falling: 0.895, 0.857, 0.806, 0.599, 0.196. This
  is the **L1 shrinkage bias**, and it is a bias, not scatter — averaging more
  data does not remove it. A spiking-deconvolution workflow that quotes L1
  amplitudes without correcting this is quoting a number that is systematically
  too small.

The kurtosis column is a diagnostic rather than a target: an L1 solution at
$\lambda = 0.1$ has kurtosis 49.2, close to the true 45.96, whereas the damped
L2 solution below reaches only 15.3. Sparsity, in this measured sense, is what
L1 restores.

### 4.1 Choosing $\lambda$ against a criterion, not a taste

The demonstration picks $\lambda = 0.1$ and then searches $\mu$ over
$\log_{10}$ steps from $10^{-6}$ to $10^{2}$ to find the L2 solution with the
**same residual**:

- L1, $\lambda = 0.10$: 19 nonzero samples, residual 9.62 %, amplitude ratio 0.806.
- L2, $\mu = 2.256\times10^{-1}$: 351 samples above $10^{-3}$, residual 9.54 %,
  73 samples above 10 % of the peak, 13 above 50 % of the peak.

Same fit, different answer, and neither is "the" answer: the difference is the
prior. Matching the residual is the minimum courtesy if the two methods are to
be compared at all; comparing a well-fit L2 with a badly-fit L1 proves nothing.

## 5. Why a spike train needs L1: resolution

A band-limited wavelet has a width. Convolving a spike with it produces a
sidelobe pattern, and inverting it with an L2 penalty spreads energy along that
pattern because spreading is cheap in the $\ell_2$ sense. Two unit spikes were
placed with a controlled separation, noise-free so that the comparison is about
resolution and not about noise, and the solution was called **resolved** when
the value midway between the two recovered peaks was below 60 % of the weaker
peak:

| separation (ms) | L1 mid/weak | L1 resolved | L2 mid/weak | L2 resolved |
|---|---|---|---|---|
| 4 | 1.000 | no | 1.000 | no |
| 8 | 0.059 | yes | 1.025 | no |
| 12 | 0.005 | yes | 0.174 | yes |
| 16 | 0.000 | yes | 0.425 | yes |
| 24 | 0.002 | yes | 0.049 | yes |
| 32 | 0.001 | yes | 0.141 | yes |

With this 30 Hz wavelet at 4 ms sampling, L1 separates the pair at 8 ms and the
damped L2 solution does not manage it until 12 ms — a factor of 1.5 in
separation, which is the practical content of "sparse inversion buys
resolution". The demonstration states the price in the same breath: the
shrinkage bias of §4. Resolution and amplitude fidelity are traded against each
other by the same parameter.

## 6. Did it actually solve the problem? Optimality checks

An iteration returning a plausible-looking vector is not evidence that it
minimised anything. For $\lambda = 0.1$ the demonstration evaluates the
first-order conditions of the convex problem. At the 19 nonzero samples,
stationarity requires $W^{T}(W r - d) + \lambda\operatorname{sign}(r) = 0$, and
the measured maximum absolute violation is $1.739\times10^{-7}$. At the other
381 samples, the subgradient condition is
$\lvert W^{T}(W r - d)_i \rvert \le \lambda$, and the measured
$\max(0, \lvert\cdot\rvert_i - \lambda)$ is exactly $0.000$.

Both numbers are at the FISTA stopping tolerance, which is the honest statement:
the vector is the minimiser to about seven digits, and the optimality check is
what licenses that claim. With $\lambda = 1.0$ on the two-spike data, **3 of
400** samples are nonzero, so 397 are exactly zero — L1 returns sparse vectors,
and the L2 solution is dense for every $\mu > 0$ however small.

## 7. Assumptions and regime of validity

The sparse deconvolution of this lesson is valid only within the following
statements, each of which is a modelling choice:

1. **The Earth is a spike train.** The prior is that reflectivity is a sum of
   isolated spikes. A gradational or finely layered medium violates it, and L1
   will then return a plausible-looking but biased spike train. The demonstration
   shows the estimator never finds the true 12 spikes; the prior is approximate
   even in the case built to satisfy it.
2. **The wavelet is known and stationary.** $W$ is the same everywhere and at
   every time. A time-varying wavelet, a misestimated wavelet, or a
   depth-dependent source invalidates the operator. Sparse *blind* deconvolution
   is a harder and different problem.
3. **The noise is Gaussian and its level is known.** The stated residual is
   meaningful only against a stated noise level; here 5 % of the signal rms.
   Nothing in the estimator estimates $\sigma$ for you.
4. **The $\ell_1$ norm is a proxy for the $\ell_0$ count.** It is the tightest
   convex proxy, not an equivalence. Its cost is the shrinkage bias measured in
   §4; debiasing (unpenalised least squares on the identified support) or a
   nonconvex penalty are the standard repairs, and both introduce new choices.
5. **The operator norm is a fixed scalar.** $L$ is computed once from the SVD;
   the convergence results quoted are for the exact $L$, and an underestimated
   $L$ makes FISTA diverge rather than merely slow down.
6. **Nothing here is a measurement of the Earth.** The trace, the reflectivity
   and the noise are all SYNTHETIC, and the numbers above are properties of that
   model.

Outside this regime the estimator is not wrong so much as unlicensed: it will
still return a sparse vector, and the sparsity of the output is a property of
the penalty, not evidence that the Earth is spiky.

## Mastery checkpoint

Without notes: **(a)** state the L1 problem and the closed form of its proximal
operator; **(b)** explain why the step size in ISTA is $1/L$ and what happens if
it is too large; **(c)** using the table of §4, choose a $\lambda$ for a study
that must report amplitudes to 10 % and must not report a spike that is not
there, and justify the two halves of that requirement; **(d)** state the
subgradient condition at a zero entry and say what it means physically; **(e)**
name the three assumptions of §7 that a real data set would most likely break
and say how each would show up in the output.

A worked answer to (a)–(c) appears in the
[solutions](exercises/01-sparse-deconvolution-solutions.md).

## Common pitfalls

1. **Reporting L1 amplitudes as if they were Reflectivity.** They are shrunk by
   a factor that depends on the local signal-to-noise ratio; the demonstration
   measures 0.806 at a modest penalty.
2. **Comparing L1 and L2 at different residuals.** Match the residual, or the
   comparison is about the fit, not about the prior.
3. **Treating sparsity of the output as evidence about the Earth.** A $\lambda$
   of 3.0 returns *zero* nonzero samples. The penalty sets the sparsity.
4. **Ignoring the condition number.** $\kappa(W) = 3.659\times10^{5}$ here;
   the noise amplification is a property of the operator and the sampling, and
   it must be quoted with any resolution claim.
5. **Trusting the iteration.** Always check the subgradient conditions of §6.
6. **Calling the shrinkage a bias to be removed without cost.** Debiasing
   re-injects noise; the choice is a trade, not a correction.

## Related modules

- [20-04 Deconvolution and Inverse Filtering](../04-deconvolution-and-inverse-filtering/README.md)
  — the L2 branch of the same problem, including water-level and Wiener filters.
- [20-07-02 Compressive Sensing and Data Reconstruction](02-compressive-sensing-signals.md)
  — the same prior used to recover missing samples rather than to sharpen a
  wavelet.
- [18-03-04 Sparsity](../../18-inverse-problems/03-regularization/04-sparsity.md)
  — the systematic treatment of sparsity as regularisation, including the
  debiasing literature and the non-convex alternatives.
- [20-05-03 Colour of Noise](../05-noise-and-random-signals/03-noise-colour.md)
  — why the "noise level" in assumption 3 is rarely a single number.
