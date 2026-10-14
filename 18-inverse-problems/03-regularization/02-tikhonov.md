---
id: 18-03-02
title: "Tikhonov Regularisation and the Smoothing Trade-Off"
level: doctoral
prereqs: ["18-03-01", "18-02-03", "18-02-04", "01-14-04"]
tags: [inverse-problems, regularization, tikhonov, bias-variance, resolution]
---

# Tikhonov Regularisation and the Smoothing Trade-Off

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the Tikhonov estimator from the penalised functional for a general
   penalty operator $L$, and **explain** what the two terms compete for.
2. **Derive** the SVD filter factors $f_i = \sigma_i^2/(\sigma_i^2+\alpha)$ and
   use them to say which model components survive at a given $\alpha$.
3. **Derive** the exact bias and variance of the estimator, and **compute** the
   $\alpha$ that minimises their sum.
4. **Verify** the decomposition numerically against a Monte Carlo experiment and
   **state** the size of the agreement you expect.
5. **Measure** the resolution–variance trade-off as a point-spread width and as
   the effective number of parameters $\sum_i f_i$.
6. **Compare** a magnitude penalty $L=I$ with a roughness penalty $L=D$, and
   **explain** why their parameters are not interchangeable and why the choice
   of $L$ is a statement about the Earth.

All models and data in this module are **SYNTHETIC**. The kernel is the exact
2-D line-mass gravity formula of a textbook forward model; the density
distribution, the station grid, the target depth and the noise are chosen
teaching values. The only physical constant is
$G = 6.67430\times10^{-11}\ \mathrm{m^3\,kg^{-1}\,s^{-2}}$.

## Prerequisites

- [18-03-01 Why Regularisation Is Physically and Statistically Justified](01-why-regularize.md) —
  the singular-value spectrum, the Picard condition and the two error bounds.
- [18-02-03 The Generalised (Moore-Penrose) Inverse](../02-linear-inverse-problems/03-generalized-inverse.md) —
  the pseudo-inverse that Tikhonov is a filter of.
- [18-02-04 SVD Analysis: Model Resolution and Data Importance](../02-linear-inverse-problems/04-svd-analysis-inverse.md) —
  model- and data-space resolution matrices.
- [01-14-04 Linear and Nonlinear Least Squares](../../01-mathematics/14-optimization/04-least-squares.md) —
  the normal equations used below.

## 1. Intuition: from a hard truncation to a graded filter

The previous lesson ended with truncated SVD: keep the first $k$ coefficients,
discard the rest. It works, it is biased, and it is brutally discontinuous — the
$k$-th component is either fully kept or fully discarded, so a tiny change in
the data can switch it on or off and the estimate jumps.

Tikhonov regularisation does the same job *smoothly*. Instead of a rank cut, it
applies a graded filter to the model coefficients: components that the data
constrain well are passed, components that they do not are attenuated, and the
transition is controlled by a single continuous parameter $\alpha$. Everything
in this lesson follows from that idea, and the interesting content is what the
attenuation does to the answer's *bias* and its *variance* — both of which can be
written down exactly.

## 2. The functional, the normal equations and standard form

### 2.1 Statement and solution

For a data vector $d \in \mathbb{R}^{n}$, a model $m \in \mathbb{R}^{n}$ and a
penalty operator $L \in \mathbb{R}^{p\times n}$, the Tikhonov estimate solves

$$m_\alpha = \arg\min_{m}\;\|Km - d\|_2^2 + \alpha\|Lm\|_2^2,
\qquad \alpha > 0 .$$

The functional is strictly convex when $\mathcal N(K)\cap\mathcal N(L) =
\{0\}$, so the minimiser is unique and is given by the normal equations

$$\left(K^{\mathsf T}K + \alpha L^{\mathsf T}L\right) m_\alpha
= K^{\mathsf T} d .$$

Two choices of $L$ cover most practice: $L = I$ penalises the *magnitude* of the
model, and $L = D$, a first-difference operator, penalises its *roughness*. They
are not the same prior and, as Section 6 measures, they are not the same
estimator.

### 2.2 Standard form

Physical units make $\alpha$ awkward to interpret: $K$ may be in
$\mathrm{mGal}$ per $(\mathrm{kg\,m^{-1}})$, $D$ in $\mathrm{m^{-1}}$, and $\alpha$
inherits whatever combination results. The clean move is to put the problem in
**standard form** first: divide $K$ by its spectral norm $\sigma_1$, divide the
model by $\|m_{\mathrm{true}}\|$, and divide the data by $\sigma_1\|m_{\mathrm{true}}\|$
so that $\hat K \hat m = \hat d$ holds exactly. Then $\alpha$ is dimensionless,
sweeps over decades can be compared between problems, and any quoted $\alpha$
carries the normalisation with it.

For the synthetic profile used throughout
($\sigma_1 = 2.82760\times10^{-7}\ \mathrm{mGal}$ per $(\mathrm{kg\,m^{-1}})$,
$\|m_{\mathrm{true}}\| = 3.8477\times10^{9}\ \mathrm{kg\,m^{-1}}$,
$\|d\| = 1.0880\times10^{3}\ \mathrm{mGal}$), the rescaled spectrum runs from
$\hat\sigma_1 = 1$ down to $\hat\sigma_{64} = 8.599\times10^{-7}$ and the noise
becomes $\hat\sigma_e = 1.0169\times10^{-3}$. The demonstration checks that the
rescaling is consistent by printing
$\|\hat K\hat m - \hat d\| = 1.7\times10^{-16}$.

## 3. Filter factors

With $K = U\Sigma V^{\mathsf T}$ the normal equations give, component by
component,

$$m_\alpha = \sum_{i=1}^{n} f_i\,\frac{y_i}{\sigma_i}\,v_i,
\qquad
\boxed{\;f_i = \frac{\sigma_i^2}{\sigma_i^2+\alpha}\;}
\qquad y_i = u_i^{\mathsf T}d .$$

The filter factor $f_i$ is a low-pass filter on the model spectrum:

- $\sigma_i^2 \gg \alpha$: $f_i \to 1$, the data determine that component;
- $\sigma_i^2 \ll \alpha$: $f_i \to \sigma_i^2/\alpha \to 0$, the penalty
  dominates and the component is suppressed;
- $\sigma_i^2 = \alpha$: $f_i = 1/2$, the crossover.

Two consequences are worth stating because they are easy to miss:

1. **The data are never modified.** Regularisation acts on the model *basis*;
   the residual is a consequence, not a filter setting.
2. **The filter is the model choice.** $\sum_i f_i$ is the effective number of
   parameters the estimate is using, and it replaces the integer rank $k$ of
   Lesson 01. The demonstration prints, for example,
   $\sum f_i = 31.291$ at $\alpha = 10^{-6}$ and $16.009$ at $\alpha = 10^{-3}$.

A verification from the same run: at $\alpha = 10^{-6}$, $\hat\sigma_{31} =
1.19945\times10^{-3}$ so $\hat\sigma_{31}^2 = 1.43868\times10^{-6}$ and

$$f_{31} = \frac{1.43868\times10^{-6}}{1.43868\times10^{-6}+10^{-6}} = 0.58994,$$

which is the value tabulated by the demonstration. For the smallest component,
$f_{64} = 7.395\times10^{-13}/(7.395\times10^{-13}+10^{-6}) =
7.4\times10^{-7}$: completely suppressed. The SVD form and the direct solution of
the normal equations agree to $1.2\times10^{-10}$ relative, which is a check of
the implementation rather than of the mathematics.

## 4. The exact bias–variance decomposition

Write $d = K m_{\mathrm{true}} + e$, with $e$ zero-mean, white, of variance
$\sigma_e^2$ per datum, and let $x_i = v_i^{\mathsf T} m_{\mathrm{true}}$,
$e_i = u_i^{\mathsf T}e$. Because $u_i^{\mathsf T}d = \sigma_i x_i + e_i$,

$$m_\alpha - m_{\mathrm{true}}
= \sum_{i=1}^{n}\Big[(f_i-1)x_i + f_i\,\frac{e_i}{\sigma_i}\Big]v_i .$$

The two terms are orthogonal as random variables, so the mean squared error
splits exactly:

$$\mathbb E\|m_\alpha - m_{\mathrm{true}}\|^2
= \sum_i (1-f_i)^2x_i^2
+ \sigma_e^2\sum_i \frac{f_i^2}{\sigma_i^2}
= \text{bias}^2(\alpha) + \text{variance}(\alpha).$$

This is not an approximation and not a heuristic. With the true model known, as
it is in a synthetic study, bias and variance can be computed separately *before*
any noise is drawn.

The demonstration evaluates both on a grid of 57 values of $\alpha$ and compares
the predicted total with a Monte Carlo average over 400 noise realisations:

| $\alpha$ | bias$^2$ | variance | predicted total | measured mean |
|---|---|---|---|---|
| $10^{-12}$ | $2.44\times10^{-13}$ | $1.82\times10^{6}$ | $1.822\times10^{6}$ | $1.780\times10^{6}$ |
| $10^{-8}$ | $4.96\times10^{-10}$ | $2.243\times10^{2}$ | $2.2427\times10^{2}$ | $2.181\times10^{2}$ |
| $10^{-6}$ | $8.78\times10^{-9}$ | $2.272$ | $2.27245$ | $2.2461$ |
| $10^{-4}$ | $1.93\times10^{-7}$ | $2.293\times10^{-2}$ | $2.2928\times10^{-2}$ | $2.2299\times10^{-2}$ |
| $10^{-2}$ | $3.44\times10^{-4}$ | $2.294\times10^{-4}$ | $5.731\times10^{-4}$ | $5.660\times10^{-4}$ |
| $10^{-1}$ | $2.14\times10^{-2}$ | $2.156\times10^{-5}$ | $2.1425\times10^{-2}$ | $2.1396\times10^{-2}$ |

The largest relative discrepancy between prediction and measurement, over the
whole sweep and restricted to the region where the total is within two orders of
its maximum, is $0.029$ — about $3\%$, which is what 400 realisations of a
quadratic form in Gaussian noise should give. **The theory is verified, not
assumed.**

The structure is exactly what the trade-off predicts:

- the variance is monotonically decreasing in $\alpha$ (from
  $1.82\times10^{6}$ to $2.2\times10^{-5}$, ten orders of magnitude);
- the bias is monotonically increasing ($2.4\times10^{-13}$ to
  $2.1\times10^{-2}$);
- the sum has an interior minimum at $\alpha^\star = 5.623\times10^{-3}$, where
  bias$^2 = 1.133\times10^{-4}$ and variance $= 4.089\times10^{-4}$, giving a
  predicted relative model error of $0.02285$.

At the optimum, **the variance is about 3.6 times the squared bias**. That ratio
is not a coincidence to be quoted as a rule; it is what this problem's spectrum
and noise level produce, and it changes when they do.

### Asking the oracle for advice

The $\alpha^\star$ above is an *oracle*: it was computed from knowledge of
$m_{\mathrm{true}}$. It cannot be used in practice. Its only role here is as a
benchmark. Computed empirically from the 400 realisations, the best $\alpha$ is
the same value, $5.623\times10^{-3}$, with a measured relative error of
$0.02269$ — and that statement is only available because the truth is synthetic.
[18-03-03](03-parameter-choice.md) is about what to do when it is not.

## 5. Resolution

The estimator is linear in the data, $m_\alpha = R_\alpha m_{\mathrm{true}} +
\text{noise}$, with the model resolution matrix

$$R_\alpha = \left(K^{\mathsf T}K+\alpha I\right)^{-1}K^{\mathsf T}K
= V\,\mathrm{diag}(f_i)\,V^{\mathsf T}.$$

$R_\alpha = I$ would mean perfect resolution; each row of $R_\alpha$ is the
point-spread function of the corresponding cell, i.e. the blurred version of a
unit spike that the estimate produces. Because $R_\alpha$ is
$\mathrm{diag}(f_i)$ in the singular basis, resolution and variance are controlled
by the *same* numbers:

$$f_i\uparrow \;\Rightarrow\; \text{resolution}\uparrow,\ \text{variance}\uparrow .$$

The demonstration measures the point-spread spread (second moment of the central
row of $R_\alpha$, in metres) and the mean diagonal:

| $\alpha$ | $\sum f_i$ | mean $\mathrm{diag}(R)$ | PSF spread (m) | measured relative error |
|---|---|---|---|---|
| $10^{-9}$ | 46.325 | 0.724 | 109.4 | 47.07 |
| $10^{-7}$ | 36.337 | 0.568 | 124.7 | 4.715 |
| $10^{-6}$ | 31.291 | 0.489 | 135.2 | 1.499 |
| $10^{-5}$ | 26.218 | 0.410 | 148.9 | 0.473 |
| $10^{-4}$ | 21.123 | 0.330 | 167.8 | 0.149 |
| $10^{-3}$ | 16.009 | 0.250 | 196.4 | 0.0476 |
| $10^{-2}$ | 10.887 | 0.170 | 247.1 | 0.0238 |
| $10^{-1}$ | 5.876 | 0.092 | 367.2 | 0.146 |

The pattern is unambiguous: as $\alpha$ rises, resolution is lost (spread
$109 \to 367\ \mathrm{m}$, diagonal $0.72 \to 0.09$) and the error first falls
and then rises. The minimum error sits at the same $\alpha$ as the analytic
optimum. **There is no $\alpha$ that improves both resolution and error**: the
"best" $\alpha$ is a statement about which of the two the interpreter cares
about, and that statement is a model choice.

## 6. Choosing the penalty operator: magnitude against roughness

The parameter $\alpha$ is not the only choice; $L$ is a choice too, and it is the
more consequential one because it says *what kind of model is plausible*.

The demonstration compares $L=I$ with $L=D$, where $D$ is a first difference
divided by the $127.0\ \mathrm{m}$ cell size and then normalised to unit spectral
norm so that both penalties multiply a unit-norm operator. Three measured facts:

1. **$D^{\mathsf T}D$ is singular**, with the constant model in its null space.
   The penalty therefore controls roughness but not magnitude: the data must fix
   the mean. Measured at its best $\alpha$, the $L=D$ solution has mean
   $0.32711\times10^{9}\ \mathrm{kg\,m^{-1}}$ against a true mean of
   $0.32710\times10^{9}\ \mathrm{kg\,m^{-1}}$ — the mean is recovered to four
   decimals, while the $L=I$ penalty shrinks every direction including the
   constant one.
2. **The errors are not equal at equal $\alpha$.** At $\alpha = 10^{-3}$,
   $L=I$ gives $0.0472$ and $L=D$ gives $0.0999$; at $\alpha = 10^{-1}$, $L=I$
   gives $0.146$ and $L=D$ gives $0.0161$. The two $\alpha$ axes are not
   interchangeable, and a paper that quotes $\alpha$ without the operator $L$
   has not specified its method.
3. **Their best achievable errors differ, and so does their resolution.** Over
   the sweep, the best $L=I$ error is $0.02220$ at $\alpha = 5.62\times10^{-3}$
   with a PSF spread of $213\ \mathrm{m}$; the best $L=D$ error is $0.01175$ at
   $\alpha = 0.316$ with a spread of $305\ \mathrm{m}$. The roughness penalty
   wins on *error* by a factor of $1.9$ and loses on *resolution* by a factor of
   $1.4$ — and it wins at all here only because the true model is a smooth
   Gaussian bump, which is exactly the kind of model $L=D$ asserts.

Read those last two sentences together. The superior performance of $L=D$ is not
a discovery about inversion; it is a coincidence between the prior and the model
the demonstrator chose. Change the true model to a layered step and the ranking
reverses — that is the experiment of
[18-03-05 Total Variation and Edge-Preserving Inversion](05-total-variation.md).

## 7. A fully worked numeric example

**Problem.** With the synthetic profile above, compute the filter factors at
$\alpha = 10^{-6}$ for components $i = 1, 31, 64$; the effective number of
parameters; and the bias and variance contributions of component 31.

**Step 1 — component 1.** $\hat\sigma_1 = 1$, so
$f_1 = 1/(1+10^{-6}) = 0.999999$. The leading component is untouched.

**Step 2 — component 31.** $\hat\sigma_{31} = 1.19945\times10^{-3}$,
$\hat\sigma_{31}^2 = 1.43868\times10^{-6}$:

$$f_{31} = \frac{1.43868\times10^{-6}}{1.43868\times10^{-6}+1.00000\times10^{-6}}
= \frac{1.43868}{2.43868} = 0.58994 .$$

**Step 3 — component 64.** $\hat\sigma_{64}^2 = 7.395\times10^{-13}$:

$$f_{64} = \frac{7.395\times10^{-13}}{7.395\times10^{-13}+10^{-6}}
= 7.395\times10^{-7} \approx 0 .$$

**Step 4 — effective parameters.** $\sum_i f_i = 31.291$ from the tabulated
value: the estimate behaves like a 31-parameter model, not a 64-parameter one.

**Step 5 — component contributions at $i = 31$.** With
$|x_{31}| = 8.800\times10^{-5}$ (tabulated) and $(1-f_{31}) = 0.41006$:

$$\text{bias}_{31}^2 = (0.41006)^2 (8.800\times10^{-5})^2
= 1.302\times10^{-9},$$
$$\text{variance}_{31} = \hat\sigma_e^2
\frac{f_{31}^2}{\hat\sigma_{31}^2}
= (1.0169\times10^{-3})^2\frac{0.58994^2}{1.43868\times10^{-6}}
= 0.2502 .$$

Component 31 therefore contributes about eight orders of magnitude more variance
than squared bias, and it alone accounts for
$0.2502/2.272 = 11\%$ of the total variance. Compare component 1: $f_1 \approx 1$ gives
bias$_1^2 \approx 0$ and variance$_1 \approx \hat\sigma_e^2/\hat\sigma_1^2 =
1.03\times10^{-6}$ — negligible. **The error of the estimate is carried by the
mid-spectrum components**, not by the ones the data see best nor by the ones it
cannot see at all. Their bias is small because $x_i$ is small there; their
variance is moderate because $f_i/\sigma_i$ is still appreciable.

**Step 6 — total.** Summing all 64 contributions gives
bias$^2 = 8.8\times10^{-9}$ and variance $= 2.272$, matching the table, and a
relative model error of $\sqrt{2.2724} = 1.507$ at $\alpha=10^{-6}$ — which is why
$10^{-6}$ is a poor choice even though the SVD and the direct solve agree
perfectly at it. Choosing $\alpha$ is a *statistical* decision, independent of
the linear algebra.

## 8. Assumptions and regime of validity

1. **$e$ is zero-mean, white and uncorrelated with the model.** The variance
   formula $\sigma_e^2\sum f_i^2/\sigma_i^2$ presumes
   $\mathbb E[e_ie_j]=\sigma_e^2\delta_{ij}$. For correlated noise the expression
   becomes $\sum_{ij}f_if_j\,\mathrm{Cov}(e_i,e_j)/(\sigma_i\sigma_j)$ and the
   optimum moves; see
   [18-02-06 Data Weighting and Error Covariance Specification](../02-linear-inverse-problems/06-weighting-and-covariance.md).
2. **The spectrum is not so steep that the variance is infinite in practice.**
   With double precision the smallest useful $\hat\sigma_i$ is about
   $10^{-16}$; below that the computed filter factors are noise.
3. **The prior is Gaussian-like in its effect.** A quadratic penalty asserts
   that large model values are exponentially unlikely. For a model with
   occasional large jumps this is false, and the assertion is what produces the
   smearing measured in Section 6 — see
   [18-03-04](04-sparsity.md) and [18-03-05](05-total-variation.md).
4. **One $\alpha$ for the whole model.** Non-uniform or adaptive penalties are
   legitimate but they add parameters whose selection is a separate problem.
5. **$m_{\mathrm{true}}$ is used only in validation.** Everything quoted as an
   error in this lesson is a synthetic-study diagnostic; in field work the
   oracle columns must be replaced by a residual-based rule, which is less
   reliable by a measurable amount measured in [18-03-03](03-parameter-choice.md).

## 9. The honest summary

- Tikhonov is a low-pass filter on the model spectrum. The smoothing is not a
  side effect; it is the mechanism.
- Bias and variance are both computable exactly, and they move in opposite
  directions. The optimum is a genuine interior minimum, not a heuristic
  compromise.
- At the optimum of this synthetic problem the variance is 3.6 times the
  squared bias; that number is a property of the spectrum and the noise level,
  not a universal constant.
- Choosing $L$ is a statement about which Earth models are plausible. Choosing
  $\alpha$ is a statement about how much the analyst trusts the data.
- Both choices belong in the report, together with the residual that resulted.

## 10. Python demonstration

`code/tikhonov_demo.py` prints: the standard-form rescaling and a consistency
check; the filter-factor formula verified against a direct solve; the filter
factors and effective parameter count at several $\alpha$; the exact
bias–variance decomposition against a 400-realisation Monte Carlo with the
oracle $\alpha$; the resolution matrix diagnostics; and the $L=I$ versus $L=D$
comparison including the data-determined mean.

```bash
cd 18-inverse-problems/03-regularization/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python tikhonov_demo.py
```

It is print-only, seeded with `np.random.default_rng(20261014)`, and runs in
under a second.

## 11. Exercises

Full sets with worked solutions are in
[`exercises/02-tikhonov-exercises.md`](exercises/02-tikhonov-exercises.md) and
[`exercises/02-tikhonov-solutions.md`](exercises/02-tikhonov-solutions.md).

- **★** Compute $f_i$ for $\alpha = 10^{-4}$ at $\hat\sigma_i = 10^{-2}$ and
  $10^{-4}$, and state which component is closer to the crossover.
- **★★** Derive $\mathrm{d}\,\mathbb E\|m_\alpha - m_{\mathrm{true}}\|^2
  /\mathrm{d}\alpha$ from the filter-factor form and show that the optimum
  satisfies $\sum_i f_i^2(1-f_i)x_i^2/\sigma_i^2
  = \sigma_e^2\sum_i f_i^3/\sigma_i^4$.
- **★★★** Extend the demonstration to a rank-deficient $K$ (two identical
  columns) and measure how the bias–variance decomposition and the noise-gain
  curve change.

## 12. Mastery checkpoint

Complete this without notes:

> For the standard-form problem above with $\hat\sigma_e = 1.017\times10^{-3}$,
> **(a)** write $f_i$ and state its two limits; **(b)** compute the bias and
> variance of component 46 at $\alpha = 10^{-6}$ given $\hat\sigma_{46} =
> 3.8405\times10^{-5}$ and $|x_{46}| = 3.1\times10^{-17}$; **(c)** explain in one
> sentence why that component contributes essentially nothing to either term;
> **(d)** the $\alpha$ minimising the total error is $\approx 5.6\times10^{-3}$,
> which is four orders of magnitude above the noise variance per coefficient
> $\hat\sigma_e^2 \approx 1.0\times10^{-6}$. Account for the gap.

A worked version of (a)–(c) appears in
[`exercises/02-tikhonov-solutions.md`](exercises/02-tikhonov-solutions.md).

## 13. Common pitfalls

1. **Quoting $\alpha$ without the operator $L$ and the normalisation.** The two
   $\alpha$ axes in Section 6 differ by more than two decades at equal error.
2. **Reading the noise-gain formula as a stability guarantee.** The variance is
   finite for every $\alpha>0$, but it can still be $10^{6}$ times the model
   norm.
3. **Treating the oracle $\alpha$ as a target.** It uses the answer; its only
   legitimate use is benchmarking a real rule.
4. **Assuming the smoother prior is the better prior.** $L=D$ won by a factor
   1.9 on this smooth truth and would lose on a blocky one.
5. **Forgetting that $L=D$ does not control magnitude.** With $D^{\mathsf T}D$
   singular the mean is set by the data; with poor data coverage that is a real
   risk.
6. **Comparing $\sum f_i$ with the number of cells.** It is the effective
   parameter count, not a resolution length; the PSF spread is the second.

## 14. Where this is used

- **Potential fields.** Density and depth inversions are almost always
  Tikhonov-regularised in some form; the roughness penalty is the standard
  choice because geological property fields are spatially correlated.
- **Seismic tomography and waveform inversion.** The same functional appears as
  damping plus smoothing, usually with a depth-dependent weight on $L$.
- **Signal processing.** Wiener filtering and water-level deconvolution are
  Tikhonov in the frequency domain; see
  [20-04-01 Deconvolution: Concept, Ill-Posedness and Stabilisation](../../20-signal-processing/04-deconvolution-and-inverse-filtering/01-deconvolution-concept.md).
- **Machine learning.** Ridge regression is $L=I$ Tikhonov with a design matrix;
  the bias–variance decomposition is the same one; see
  [21-04-02 Bias-Variance Trade-Off, Underfitting and Overfitting](../../21-statistics-bayesian-ml/04-machine-learning-fundamentals/02-bias-variance.md).

## 15. Related modules

- [18-03-03 Choosing the Trade-Off: L-Curve, GCV, Discrepancy Principle](03-parameter-choice.md) —
  replacing the oracle with a rule that works.
- [18-03-06 Physical Constraints, Bounds and Feasible Model Sets](06-constraints.md) —
  the same bias question when the prior is hard rather than soft.
- [18-07-01 Joint Inversion: Concepts and Weighting](../07-joint-and-multi-physics-inversion/01-joint-inversion-concepts.md) —
  several penalties and several data sets at once.
- [18-04-03 Conjugate Gradient and Large-Scale Inversion](../04-nonlinear-inversion/03-conjugate-gradient-inverse.md) —
  solving the normal equations when the matrix cannot be formed.
- [19-01-02 Truncation Error, Order of Accuracy and Convergence Rates](../../19-numerical-modeling-hpc/01-numerical-foundations/02-convergence-and-error.md) —
  the discretisation error that sits underneath this whole discussion.

## 16. Self-assessment checklist

- [ ] I can derive the normal equations from the penalised functional.
- [ ] I can write $m_\alpha$ in the SVD basis and read off the filter factors.
- [ ] I can compute the exact bias and variance for a given $\alpha$.
- [ ] I can explain why the optimum of this problem sits at
      $\alpha \gg \hat\sigma_e^2$.
- [ ] I can measure a point-spread width and argue from it about resolution.
- [ ] I can say what changes, and what does not, when $L=I$ becomes $L=D$.
