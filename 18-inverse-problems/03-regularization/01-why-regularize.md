---
id: 18-03-01
title: "Why Regularisation Is Physically and Statistically Justified"
level: graduate
prereqs: ["18-01-02", "18-02-04", "05-03-01"]
tags: [inverse-problems, regularization, ill-posedness, picard-condition, bias-variance]
---

# Why Regularisation Is Physically and Statistically Justified

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** a discretised geophysical inverse problem as a first-kind equation
   $K m = d$ and **explain** why its singular-value spectrum decides whether the
   data can determine the model.
2. **Derive** the relative error bound $\|\delta m\|/\|m\| \le \kappa_2(K)\,
   \|\delta d\|/\|d\|$ and **measure** how badly it is attained.
3. **State and test** the discrete Picard condition on a synthetic data set, and
   identify the index beyond which the data stop carrying information about the
   model.
4. **Justify** regularisation physically (the measurement operator is a smoother
   whose resolution is set by depth and station spacing) and statistically (a
   prior on the model gives an estimator that is biased by construction).
5. **Measure** the bias–variance decomposition of a rank-truncated estimator and
   report the model choice it implies.
6. **Distinguish** three things that are routinely confused: an exact-data
   solution (which exists), a usable estimate from noisy data (which does not,
   unregularised), and a justifiable estimate (which requires a stated prior).

All models and data in this module are **SYNTHETIC**. The kernel used throughout
is the exact 2-D line-mass gravity formula of a textbook forward model, but the
density distribution, the station grid, the target depth and the noise are
chosen teaching values, not field measurements. The only physical constant used
is the standard gravitational constant $G = 6.67430\times10^{-11}\ \mathrm{m^3\,
kg^{-1}\,s^{-2}}$.

## Prerequisites

- [18-01-02 Hadamard's Conditions: Existence, Uniqueness, Stability](../01-inverse-problem-foundations/02-hadamard-well-posedness.md) —
  the three conditions a well-posed problem must satisfy.
- [18-02-04 SVD Analysis: Model Resolution and Data Importance](../02-linear-inverse-problems/04-svd-analysis-inverse.md) —
  the singular value decomposition as the natural coordinate system of an
  inverse problem.
- [05-03-01 The Forward Problem: From Model to Data](../../05-core-geophysics/03-forward-modelling-principles/01-forward-problem.md) —
  how a kernel matrix is built and what its entries mean physically.
- [01-07-08 Singular Value Decomposition and Rank Truncation](../../01-mathematics/07-linear-algebra/08-svd.md) —
  the linear algebra used below without proof.

## 1. The situation that forces the issue

Every geophysical inversion ends up as a linear system

$$K m = d, \qquad K \in \mathbb{R}^{n\times n},\quad m \in \mathbb{R}^{n},\quad
d \in \mathbb{R}^{n},$$

or the least-squares version of it, where $K$ is a discretisation of a
first-kind Fredholm equation $d(x) = \int k(x,s)\,m(s)\,\mathrm{d}s$. The kernel
$k$ is a *smoothing* function: neighbouring model cells produce nearly identical
data, so the columns of $K$ are nearly parallel. A matrix whose columns are
nearly parallel is nearly rank-deficient, and inverting it is the problem.

The empirical fact that drives this whole module is measured in
`code/why_regularize_demo.py` on a synthetic gravity profile. The kernel is the
exact vertical attraction of 2-D line masses at $0.6\ \mathrm{km}$ depth,
evaluated at 64 stations spaced $127\ \mathrm{m}$ apart; the model is the line
density in 64 cells. Its singular values decay from
$\sigma_1 = 2.8276\times10^{-7}\ \mathrm{mGal}$ per $(\mathrm{kg\,m^{-1}})$ to
$\sigma_{64} = 8.6\times10^{-7}\,\sigma_1$, giving

$$\kappa_2(K) = \frac{\sigma_1}{\sigma_{64}} = 1.16\times10^{6}.$$

The fitted algebraic decay $\sigma_i \sim i^{-q}$ on $i = 1,\dots,48$ gives
$q = 3.24$. Both numbers are properties of the *physics* — target depth, station
spacing, profile length — and not of the algorithm used to solve the system.

## 2. Definitions and the exact motivation for regularisation

### 2.1 The unregularised solution and its error

Let the data be $d = K m_{\mathrm{true}} + e$ with noise $e$. The least-squares
solution of a square, full-rank $K$ is

$$m_{\mathrm{LS}} = K^{-1}d = m_{\mathrm{true}} + K^{-1}e.$$

In the singular-value basis $K = U\Sigma V^{\mathsf T}$, with $u_i$, $v_i$ the
left and right singular vectors and $y_i = u_i^{\mathsf T} d$, this is

$$m_{\mathrm{LS}} = \sum_{i=1}^{n} \frac{y_i}{\sigma_i}\,v_i
= \underbrace{\sum_i \frac{\sigma_i x_i}{\sigma_i}v_i}_{m_{\mathrm{true}}}
+ \sum_i \frac{u_i^{\mathsf T} e}{\sigma_i}\,v_i,
\qquad x_i = v_i^{\mathsf T} m_{\mathrm{true}}.$$

The model error is a sum of noise components divided by $\sigma_i$. For a
decaying spectrum the last terms dominate, and there is no bound on
$\|K^{-1}e\|$ as the discretisation is refined: refining the grid adds *smaller*
singular values and therefore a *larger* error. This is the discrete face of
Hadamard's stability failure, met in
[18-01-02](../01-inverse-problem-foundations/02-hadamard-well-posedness.md).

### 2.2 The deterministic bound, and how badly it is attained

Two elementary bounds are worth knowing because they are the honest summary of
how much can go wrong:

$$\frac{\|\delta m\|}{\|m\|} \le \kappa_2(K)\,\frac{\|\delta d\|}{\|d\|}
\quad\text{and}\quad
\left\|K^{-1}e\right\| \le \frac{\|e\|}{\sigma_{\min}}.$$

The first is the *worst case over data perturbations*; the second is what
actually happens for a *random* perturbation. The demonstration measures both.

### 2.3 The discrete Picard condition

A meaningful solution requires the model coefficients $x_i$ to decay faster than
the singular values:

$$\left|u_i^{\mathsf T} d\right| = \sigma_i\,|x_i| \quad\text{must decay to
zero with }\sigma_i.$$

If instead the coefficients stall at the noise level, the ratio $y_i/\sigma_i$
grows without bound and those components are pure noise amplification. The
Picard condition is a statement about the *data and the model*, and it can be
plotted without knowing the answer.

## 3. What is measured

`code/why_regularize_demo.py` prints the following, all in one run.

**Exact data.** With $d = Km_{\mathrm{true}}$ and no noise, the least-squares
solution has relative model error $1.3\times10^{-10}$ and data misfit
$8.7\times10^{-16}$. The discrete problem therefore inverts to machine
precision: ill-posedness is **not** a property of the discrete operator. It is a
statement about what noise does to it, and this measurement is the reason the
word "regularisation" does not appear in the exact-data part of inverse theory.

**Noisy data.** Adding white noise with rms $1.1063\ \mathrm{mGal}$, which is
$0.50\%$ of the peak anomaly, and solving the same way gives a relative model
error of $1.42\times10^{3}$ in one realisation. Over 200 realisations the mean
is $2.23\times10^{3}$, with 5th and 95th percentiles $1.38\times10^{3}$ and
$3.41\times10^{3}$. The failure is not marginal and it is not rare.

The unregularised solution also achieves a data misfit of $0.0000\%$: it fits
the noise exactly. **A perfect fit is the signature of the problem, not of a
good answer.** The worst-case bound $\kappa_2(K)\|e\|/\|d\|$ evaluates to
$1.33\times10^{3}$, of the same order as the measured error, so the bound is
tight enough to be useful as an order-of-magnitude warning.

**The Picard plot.** The single-coefficient noise level is
$\sigma_e = 1.1063\ \mathrm{mGal}$ because $u_i$ is orthonormal. Only
$3$ of the 64 exact coefficients exceed $10\sigma_e$, and they stop at
$i = 5$. Beyond that, the exact coefficients fall to $\sim10^{-13}\ \mathrm{mGal}$
— numerical zero, because the smooth true model simply has no energy in those
directions — while the noisy coefficients stall near $0.3$–$1.0\ \mathrm{mGal}$.
The crossing index *is* the useful rank of the problem, and it is about $5$–$7$
out of 64.

A detail worth noticing: 51 of the 64 exact coefficients are below $10^{-6}$ of
the largest, starting at $i = 2$. That is not noise. The true model is
**symmetric** about $x = 0$, so its projection onto every antisymmetric singular
vector is zero. Data can only see what the model contains; a parameter that does
not appear in the data cannot be recovered from it, no matter the algorithm.

**One crude regulariser, measured.** Truncated SVD — keep the first $k$
coefficients and set the rest to zero — gives the following errors on the noisy
data: $k=4$: $1.72\times10^{-1}$; $k=8$: $7.91\times10^{-3}$; $k=16$:
$7.17\times10^{-2}$; $k=32$: $1.11\times10^{3}$; $k=64$: $1.42\times10^{3}$. The
measured optimum is $k^\star = 7$ with error $7.36\times10^{-3}$, an improvement
of $1.9\times10^{5}$ over the unregularised solution.

Two things are true at once, and the rest of the module is about them. The
truncated solution is *enormously* better, and it is *biased*: it lives in a
7-dimensional subspace and therefore cannot equal the true model even when the
noise is zero. The rank is a model choice, made by the analyst, and the next
lessons turn "how many coefficients" into "which prior, and with what weight".

## 4. The physical justification

Regularisation is not a numerical trick applied at the end of an inversion. It
enters at the moment the experiment is designed, because the measurement
operator itself is a smoother.

`code/why_regularize_demo.py` makes this concrete by changing one thing: the
depth of the source sheet, with station spacing, profile, grid, true model and
noise held fixed.

| target depth (m) | $\kappa_2(K)$ | fitted $q$ | noisy least-squares error | best rank / error |
|---|---|---|---|---|
| 300 | $7.66\times10^{2}$ | 1.64 | $2.75$ | 7 / $5.13\times10^{-3}$ |
| 600 | $1.16\times10^{6}$ | 3.24 | $2.16\times10^{3}$ | 7 / $4.53\times10^{-3}$ |
| 1200 | $2.53\times10^{12}$ | 6.34 | $2.26\times10^{9}$ | 7 / $1.46\times10^{-2}$ |

The deeper target is not "harder to compute"; it is *less observable*. Its
gravity field is smoother, so more of the model's spatial detail is carried by
singular values below the noise floor. The regularised answer, by contrast,
stays usable at all three depths (errors of order $10^{-2}$), because the
truncation removes the components that the data cannot support anyway.

That is the physical statement of regularisation: **discard what the experiment
never measured.** In potential-field work the discarded directions are the
shallow, high-wavenumber ones; the depth-to-spacing ratio is what puts them
where they are.

### The same thing in second-kind form

A control experiment isolates noise from ill-posedness. Form
$A = cI + K$ with $c$ the largest absolute row sum of $K$, so that $A$ is a
compact perturbation of a scaled identity: $\sigma(A) \in [2.9942\times10^{-7},
5.8218\times10^{-7}]$, $\kappa_2(A) = 1.944$. Generating data with $A$ itself,
at the same *relative* noise level of $0.50\%$ (peak $520.150\ \mathrm{mGal}$,
noise $2.6007\ \mathrm{mGal}$), the least-squares error is $1.76\times10^{-2}$,
against $1.42\times10^{3}$ for the first-kind operator. The measured ratio is
$8.1\times10^{4}$.

Same grid, same noise level, same true model. The only difference is the shape
of the singular-value spectrum. **Noise is not the problem; the spectrum is.**

## 5. The statistical justification

The second justification is Bayesian, and it explains why a *biased* estimator
is not a defect but the point.

Put a Gaussian prior $m \sim \mathcal N(0, \alpha^{-1}L^{\mathsf T}L^{-1})$
loosely written, and a Gaussian likelihood for the data. The maximum a posteriori
estimate is the minimiser of

$$\|Km - d\|_2^2 + \alpha\|Lm\|_2^2,$$

which is exactly Tikhonov regularisation with parameter $\alpha$ (see
[18-05-01 Bayes' Theorem as an Inverse-Problem Formulation](../05-bayesian-inversion/01-bayes-inverse-formulation.md)
for the full derivation). Two consequences follow immediately and they are the
honest content of this lesson:

1. **The estimator is biased by construction.** Under the prior the expected
   posterior mean is not the truth; it is truth plus the shrinkage imposed by
   the prior. A method advertised as "unbiased inversion" is advertising the
   absence of a prior, which for an ill-posed problem means an infinite-variance
   estimator — unbiased, and useless.
2. **Choosing $\alpha$ is choosing a model.** $\alpha$ is not a numerical
   tolerance. It is the ratio of the assumed data variance to the assumed prior
   variance, and it has units. Setting it by taste, or by the default of a
   software package, is a model decision made silently.

The bias–variance decomposition of the rank-truncated estimator makes the trade
explicit. With $f_i$ the filter factor (1 for retained, 0 for discarded),

$$\mathbb E\|m_{\mathrm{reg}} - m_{\mathrm{true}}\|^2
= \underbrace{\sum_i (1-f_i)^2 x_i^2}_{\text{bias}^2}
+ \underbrace{\sigma_e^2\sum_i \frac{f_i^2}{\sigma_i^2}}_{\text{variance}}.$$

Discarding a coefficient removes its variance contribution
$\sigma_e^2 f_i^2/\sigma_i^2$, which is largest for the *smallest* $\sigma_i$,
and adds its bias contribution $(1-f_i)^2x_i^2$, which is largest for the
*most important* coefficients. The trade-off is unavoidable, and
[18-03-02](02-tikhonov.md) measures its minimum exactly.

## 6. A fully worked numeric example

Take the synthetic profile above ($\kappa_2 = 1.16\times10^{6}$) and suppose an
analyst reports an unregularised density model from data with $0.5\%$ noise.

1. **Noise level.** Peak anomaly $221.27\ \mathrm{mGal}$, so
   $\sigma_e = 0.005\times221.27 = 1.106\ \mathrm{mGal}$.
2. **Worst-case bounds.** The demonstration evaluates both forms. Perturbing a
   single datum by $\sigma_e$ gives
   $\kappa_2(K)\sigma_e/\|d\| = 1.327\times10^{3}$; perturbing the whole
   vector by $\|e\| = \sigma_e\sqrt n$ gives
   $\kappa_2(K)\|e\|/\|d\| = 1.062\times10^{4}$. Both are worst-case
   statements.
3. **Measured.** The demonstration gives a mean relative error
   $2.231\times10^{3}$ over 200 noise realisations, so the worst-case bound is
   attained to within a factor of $1.7$ in this geometry: the bound is not
   pessimistic by orders of magnitude, it is descriptive.
4. **Interpretation in physical units.** $\|m_{\mathrm{true}}\| =
   3.85\times10^{9}\ \mathrm{kg\,m^{-1}}$, so an error of $2.23\times10^{3}$
   times that is a model whose fluctuations are thousands of times the size of
   the model itself. The number is not "large"; it is meaningless.
5. **The regularised alternative.** Truncating at the Picard index gives
   $7.4\times10^{-3}$ relative error, i.e. $2.8\times10^{7}\ \mathrm{kg\,m^{-1}}$
   of rms error against a model norm of $3.85\times10^{9}\ \mathrm{kg\,m^{-1}}$.
6. **The price.** The rank-7 model cannot represent any feature that projects
   onto $v_8,\dots,v_{64}$. Those features are, by the Picard measurement,
   below the noise floor, so the price is paid in principle and not in this
   data set. On another data set with a smaller noise level the same rank would
   be wrong, and the analyst would have to raise it.

## 7. Assumptions and regime of validity

Everything above rests on the following, and each can fail:

1. **The forward operator is known exactly.** Model error in $K$ (an incorrect
   density contrast, a wrong station elevation) is not reduced by
   regularisation and can dominate the bias.
2. **The noise is additive and independent of the signal.** Multiplicative or
   correlated noise changes the Picard plot: the coefficients do not stall at a
   constant level, so the crossing index has to be estimated differently
   ([18-02-06 Data Weighting and Error Covariance Specification](../02-linear-inverse-problems/06-weighting-and-covariance.md)).
3. **The noise variance is known or estimable.** The discrepancy principle
   ([18-03-03](03-parameter-choice.md)) needs it; GCV does not but assumes
   whiteness.
4. **The model is discretised on a fixed grid.** Refining the grid changes the
   spectrum and therefore the difficulty. Comparisons between inversions on
   different grids are not comparisons of the same problem.
5. **The truncation index is chosen from the data, not from the answer.** The
   optimum rank 7 reported above was found by comparing with the known truth. In
   practice it must be chosen by a rule that does not use the truth, and such
   rules are imperfect; the measurement of their failure is the subject of
   [18-03-03](03-parameter-choice.md).

The regime in which the unregularised solution is acceptable is narrow but real:
it requires $\sigma_e/\sigma_i \ll |x_i|$ for every retained $i$, i.e. a data
noise level far below the smallest singular value times the smallest model
coefficient of interest. For a first-kind problem that condition fails for all
but the first few coefficients, always.

## 8. The honest summary

- An unregularised solution of a first-kind problem with noise is not a bad
  estimate; it is an estimate of something else, namely the noise.
- Every remedy biases the answer, and the bias is chosen, not discovered.
- The choice is defensible when the analyst states (i) the prior or penalty,
  (ii) the parameter and how it was set, and (iii) the residual obtained
  relative to the noise level.
- The physical content of the prior is the resolution the experiment can
  support, and the demonstration measures it: the same data support a 7-component
  model at $0.6\ \mathrm{km}$ depth and only about the same number at
  $1.2\ \mathrm{km}$, with a completely different error.

## 9. Python demonstration

`code/why_regularize_demo.py` builds the synthetic kernel, computes the SVD, and
prints: the singular values and the fitted decay; the exact-data error; the
noisy-data error and its distribution over 200 realisations; the discrete Picard
plot; the truncated-SVD error curve and its measured optimum; the
depth-dependence table; and the second-kind control. Run it with

```bash
cd 18-inverse-problems/03-regularization/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python why_regularize_demo.py
```

It is print-only, uses the fixed seed `np.random.default_rng(20261014)`, and
finishes in well under a second.

## 10. Exercises

Full sets with worked solutions are in
[`exercises/01-why-regularize-exercises.md`](exercises/01-why-regularize-exercises.md)
and
[`exercises/01-why-regularize-solutions.md`](exercises/01-why-regularize-solutions.md).

- **★** Compute the relative error bound for a $0.1\%$ noise level on the
  synthetic profile, and state in one sentence what the bound does and does not
  guarantee.
- **★★** From the Picard table, choose a truncation index by the criterion
  "the last coefficient above $10\sigma_e$" and compare the resulting error with
  the measured optimum of 7.
- **★★★** Design a synthetic experiment that separates the effect of noise level
  from the effect of target depth, and predict the sign of each effect on the
  crossing index before running it.

## 11. Mastery checkpoint

Complete this without notes, in about ten minutes:

> A colleague inverts a synthetic gravity profile of 64 stations with
> $0.5\%$ noise and reports a density model whose relative error, against the
> truth they generated, is $2\,200$. **(a)** Compute both worst-case bounds for
> $\kappa_2 = 1.16\times10^{6}$, $\sigma_e/\|d\| = 1.14\times10^{-3}$ and
> $\|e\| = \sigma_e\sqrt{64}$, and state where the reported error falls.
> **(b)** Explain in two sentences why the unregularised
> solution reports a data misfit of $0.0000\%$. **(c)** The analysis reports
> that only 3 of 64 coefficients exceed ten times the noise level. State what
> those three coefficients are and what the other 61 are. **(d)** Propose one
> measurable change to the experiment that would raise the number of usable
> coefficients, and say which quantity in this lesson would move as a result.

Parts (a)–(d) are worked in
[`exercises/01-why-regularize-solutions.md`](exercises/01-why-regularize-solutions.md).

## 12. Common pitfalls

1. **Confusing "the exact-data problem is invertible" with "the problem is
   well-posed".** The demonstration prints both: an error of $10^{-10}$ with
   exact data and $10^{3}$ with $0.5\%$ noise.
2. **Believing a small residual.** The unregularised solution fits the data to
   four decimal places and is meaningless.
3. **Attributing the difficulty to the solver.** The fitted decay $q$ changed
   from 1.64 to 6.34 while the solver stayed the same.
4. **Treating the truncation rank as a numerical detail.** It is the analyst's
   statement about which model components the data support.
5. **Comparing errors between different grids.** $\kappa_2$ and $q$ are
   discretisation-dependent.
6. **Forgetting that a model component cannot be recovered if it is absent from
   the data.** The 51 vanishing coefficients in the Picard table are a symmetry,
   not a numerical failure.

## 13. Where this is used

- **Potential fields.** Depth-to-basement and density inversions are first-kind
  problems whose resolution falls with depth; the depth-dependence measured
  here is the reason surveys are designed with station spacing matched to the
  expected target depth.
- **Seismic and electromagnetic imaging.** The same structure appears as a
  resolution limit set by wavelength and aperture, and it is why migration
  images are band-limited.
- **Signal processing.** Water-level deconvolution, Wiener filtering and
  spiking deconvolution are the same mathematics in a different basis; see
  [20-04-01 Deconvolution: Concept, Ill-Posedness and Stabilisation](../../20-signal-processing/04-deconvolution-and-inverse-filtering/01-deconvolution-concept.md).
- **Reporting.** The three numbers that make an inversion reproducible —
  penalty, parameter, residual — come directly from the measurements in this
  lesson; see [05-06-06 Documenting Processing: Reproducibility in Practice](../../05-core-geophysics/06-data-processing-principles/06-processing-transparency.md).

## 14. Related modules

- [18-01-03 Null Space, Non-Uniqueness and Equivalence Classes](../01-inverse-problem-foundations/03-null-space.md) —
  what the truncated components are.
- [18-02-04 SVD Analysis: Model Resolution and Data Importance](../02-linear-inverse-problems/04-svd-analysis-inverse.md) —
  the resolution matrix whose rank this lesson truncates.
- [18-03-02 Tikhonov Regularisation and the Smoothing Trade-Off](02-tikhonov.md) —
  replaces the discrete truncation with a continuous filter factor and measures
  the exact bias–variance minimum.
- [18-03-03 Choosing the Trade-Off: L-Curve, GCV, Discrepancy Principle](03-parameter-choice.md) —
  how the parameter is chosen when the truth is unknown.
- [21-04-02 Bias-Variance Trade-Off, Underfitting and Overfitting](../../21-statistics-bayesian-ml/04-machine-learning-fundamentals/02-bias-variance.md) —
  the same decomposition in a statistical-learning setting.
- [18-06-01 Taxonomy of Uncertainty: Aleatory, Epistemic, Structural](../06-uncertainty-quantification/01-uncertainty-taxonomy.md) —
  how the structural uncertainty of the discretisation enters the error budget.

## 15. Self-assessment checklist

- [ ] I can write the SVD of $K$ and the least-squares solution in that basis.
- [ ] I can state the two error bounds and say which is worst-case and which is
      typical.
- [ ] I can sketch the Picard plot and mark the crossing index.
- [ ] I can explain the exact-data error of $10^{-10}$ without invoking
      conditioning.
- [ ] I can give both a physical and a statistical reason for the same penalty
      term.
- [ ] I can say what the truncation rank trades away, and in which units the
      trade is measured.
