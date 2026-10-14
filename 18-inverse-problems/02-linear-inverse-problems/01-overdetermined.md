---
id: 18-02-01
title: "Overdetermined Problems and Least Squares"
level: advanced
prereqs: ["18-01-05", "01-07-07", "01-14-04"]
tags: [inverse-problems, least-squares, overdetermined, normal-equations, covariance, regression]
---

# Overdetermined Problems and Least Squares

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** an overdetermined system $\mathbf{d}=G\mathbf{m}+\mathbf{e}$ and
   **decide** from the dimensions and the singular values whether $N>M$ means the
   problem is well determined.
2. **Derive** the normal equations from the minimisation of
   $\lVert G\mathbf{m}-\mathbf{d}\rVert^{2}$ and **interpret** them as a residual
   orthogonality condition.
3. **Compute** the estimator covariance $\sigma^{2}(G^{\!\top}G)^{-1}$ and
   **validate** it against measured scatter over realisations.
4. **Read** a reduced $\chi^{2}$ correctly, distinguishing a bad fit from a wrong
   noise model.
5. **Implement** weighted least squares for heteroscedastic errors and
   **quantify** what ignoring the weights costs in efficiency and in reported
   uncertainty.
6. **Choose** between the normal equations, a QR factorisation and the SVD on
   conditioning grounds, not habit.

## Prerequisites

- [18-01-05 Model Space, Data Space and Mappings](../01-inverse-problem-foundations/05-model-space-data-space.md) —
  range, projection and why the residual lives in the orthogonal complement.
- [01-07-07 Orthogonality, Projections and Least Squares](../../01-mathematics/07-linear-algebra/07-orthogonality.md) —
  the projection theorem behind the normal equations.
- [01-14-04 Linear and Nonlinear Least Squares](../../01-mathematics/14-optimization/04-least-squares.md) —
  least squares as an optimisation problem, and when it is not the right loss.

## 1. The overdetermined case

With $N$ data, $M$ parameters and $N>M$, the system

$$\mathbf{d} = G\mathbf{m}+\mathbf{e},\qquad
G\in\mathbb{R}^{N\times M},\ N>M$$

generically has **no exact solution**: the data vector is not in
$\operatorname{range}(G)$ once any error is present (lesson
[18-01-02](../01-inverse-problem-foundations/02-hadamard-well-posedness.md)
quantified how far outside). The standard response is to minimise the misfit,

$$\hat{\mathbf{m}} = \arg\min_{\mathbf{m}}\ \lVert G\mathbf{m}-\mathbf{d}\rVert^{2},
\qquad
\lVert\mathbf{r}\rVert^{2} = \sum_{i=1}^{N}\left(d_i - (G\mathbf{m})_i\right)^{2},$$

which is the **least-squares** estimate. Two properties make it the default:

- the misfit is a **quadratic** function of $\mathbf{m}$, so the minimisation has a
  closed-form solution and a unique answer whenever $G^{\!\top}G$ is invertible;
- if $G^{\!\top}G$ is invertible, the estimator is the **minimum-variance unbiased
  linear estimator** under the assumption that the errors are independent with a
  common variance (the Gauss–Markov theorem).

The demonstration uses a SYNTHETIC regional-trend problem: gravity readings at
$N=20$ stations spread over $x\in[-20,20]\ \mathrm{km}$, fitted by

$$d(x) = m_1 + m_2 x,\qquad m_1\ \text{in mGal},\ m_2\ \text{in mGal\,km}^{-1},$$

with true values $m_1 = 12.000\ \mathrm{mGal}$,
$m_2 = -0.850\ \mathrm{mGal\,km^{-1}}$ and white noise of
$\sigma = 0.050\ \mathrm{mGal}$. Measured data span
$-5.0465$ to $28.9765\ \mathrm{mGal}$.

All models and data in this module are **SYNTHETIC**.

## 2. The normal equations, derived

Expand the objective:

$$J(\mathbf{m}) = \lVert G\mathbf{m}-\mathbf{d}\rVert^{2}
= \mathbf{m}^{\!\top}G^{\!\top}G\mathbf{m}
- 2\,\mathbf{m}^{\!\top}G^{\!\top}\mathbf{d}+\mathbf{d}^{\!\top}\mathbf{d}.$$

The gradient is $\nabla J = 2G^{\!\top}G\mathbf{m}-2G^{\!\top}\mathbf{d}$, so
stationarity gives the **normal equations**

$$\boxed{\;G^{\!\top}G\,\hat{\mathbf{m}} = G^{\!\top}\mathbf{d}
\quad\Longleftrightarrow\quad
\hat{\mathbf{m}} = (G^{\!\top}G)^{-1}G^{\!\top}\mathbf{d}\;}$$

whenever $G^{\!\top}G$ is invertible. The same condition reads
$G^{\!\top}(\mathbf{d}-G\hat{\mathbf{m}}) = \mathbf{0}$, i.e. **the residual is
orthogonal to every column of $G$**. In the language of lesson
[18-01-05](../01-inverse-problem-foundations/05-model-space-data-space.md), $G\hat{\mathbf{m}}$
is the orthogonal projection of $\mathbf{d}$ onto $\operatorname{range}(G)$.

Measured in the demonstration:

$$\hat{\mathbf{m}} = (11.990525,\ -0.851064),\qquad
\lVert\mathbf{r}\rVert = 2.484452\times10^{-1}\ \mathrm{mGal},$$

$$G^{\!\top}\mathbf{r} = (1.549\times10^{-14},\ 7.948\times10^{-13})
\ \mathrm{mGal}^{2}\,\mathrm{km}^{?},$$

i.e. orthogonality holds to $7.9\times10^{-13}$, which is the level set by
double precision given the magnitudes involved ($\lVert G\rVert\sim54$,
$\lVert\mathbf{r}\rVert\sim0.25$, so the natural scale is
$54\times0.25\times\varepsilon \approx 3\times10^{-15}$ per entry — the printed
value is a few orders above that because $G^{\!\top}\mathbf{r}$ sums 20 terms of
size up to $20\times0.25$). The check is worth running in any implementation: a
$G^{\!\top}\mathbf{r}$ that is *large* means the solver did not converge or the
model is constrained.

## 3. Which route to solve it

Three routes give the same answer in exact arithmetic and very different
behaviour in floating point. Measured:

$$\sigma(G) = (54.2897,\ 4.4721),\qquad
\sigma(G^{\!\top}G) = (2947.3684,\ 20.0000),$$

$$\kappa(G) = 12.1395,\qquad \kappa(G^{\!\top}G) = 147.3684,\qquad
\frac{\kappa(G^{\!\top}G)}{\kappa(G)^{2}} = 1.000000 .$$

The two solutions agree here to $3.553\times10^{-15}$, so this problem is safe
either way. But the identity $\kappa(G^{\!\top}G) = \kappa(G)^{2}$ is exact, so a
problem with $\kappa(G)=10^{6}$ becomes $\kappa(G^{\!\top}G)=10^{12}$ and the
normal equations lose twice as many digits. **Recommendation of this module:**
form $G$'s QR factorisation (or its SVD) and solve with that; form $G^{\!\top}G$
only if you can show it is harmless.

## 4. Uncertainty of the estimate

Under $\mathbf{e}\sim\mathcal{N}(\mathbf{0},\sigma^{2}I)$,

$$\hat{\mathbf{m}}-\mathbf{m} = (G^{\!\top}G)^{-1}G^{\!\top}\mathbf{e},
\qquad
\operatorname{Cov}(\hat{\mathbf{m}}) = \sigma^{2}(G^{\!\top}G)^{-1},$$

and $\hat{\mathbf{m}}$ is unbiased:
$\mathbb{E}\hat{\mathbf{m}} = \mathbf{m}$. The demonstration verifies both
numerically over 500 realisations:

| quantity | predicted | measured |
|---|---|---|
| sd of $m_1$ | 0.011180 mGal | 0.011116 mGal |
| sd of $m_2$ | 0.000921 mGal/km | 0.000977 mGal/km |
| bias of $m_1$ | 0 | $-7.37\times10^{-4}$ mGal |
| bias of $m_2$ | 0 | $+5.00\times10^{-5}$ mGal/km |
| correlation | 0.000000 | $-0.036150$ |

Two details worth understanding rather than skimming:

- the **predicted correlation is exactly zero** because the design is
  symmetric: $\sum_i x_i = 0$ makes $G^{\!\top}G$ diagonal. The measured
  $-0.036$ is the sampling fluctuation of a correlation coefficient estimated
  from 500 draws (its standard error is $\approx1/\sqrt{500}=0.045$), so it is
  consistent with zero;
- the **bias entries are proportional to $\sigma/\sqrt{500}$** in magnitude
  ($0.011180/\sqrt{500} = 5.0\times10^{-4}$), i.e. they are the standard error of
  the mean of the estimates, not a systematic effect.

The scale of the uncertainty is the practical content: with 20 stations and
$\sigma = 0.05\ \mathrm{mGal}$, the trend is determined to $0.011\
\mathrm{mGal}$ in level and $0.0009\ \mathrm{mGal\,km^{-1}}$ in slope. Multiply
the standard deviation by the noise you actually have and divide by
$\sqrt{N}$-like factors — that is the design arithmetic of a survey.

## 5. Residuals, degrees of freedom and $\chi^{2}$

The residual after a least-squares fit has $N-M$ degrees of freedom: fitting $M$
parameters removes $M$ dimensions from the data space. Measured for one
realisation of the demonstration:

$$\lVert\mathbf{r}\rVert = 0.2484452\ \mathrm{mGal},\qquad
\text{rms residual} = 0.055554\ \mathrm{mGal}\ (\sigma = 0.050),$$

$$\chi^{2} = \frac{\lVert\mathbf{r}\rVert^{2}}{\sigma^{2}} = 24.6900,\qquad
\text{d.o.f.} = 18,\qquad \chi^{2}/\text{d.o.f.} = 1.3717 .$$

That single realised value sits $1.12$ standard deviations above 1
($\mathrm{sd} = \sqrt{2/18} = 0.3333$), so it is unremarkable; over 500
realisations the mean reduced $\chi^{2}$ is $1.0065$ with sd $0.3485$, matching
the theoretical $1$ and $0.3333$. The correct reading of a reduced $\chi^{2}$ is
therefore:

- **near 1**: the misfit is consistent with the stated noise, *given* a correct
  linear model and correct $G$;
- **above 1**: either the noise is underestimated, or $G$ is wrong (unmodelled
  physics, wrong geometry), or the errors are correlated;
- **below 1**: the noise is overestimated, or the model has more freedom than the
  data support (over-fitting).

Never quote a misfit without the noise level it is compared with. The misfit
floor of a linear fit is $\sqrt{(N-r)/N}$ times the noise norm
([18-01-05 §3](../01-inverse-problem-foundations/05-model-space-data-space.md)),
and here $N-r = N-M = 18$, so the floor is
$\sqrt{18/20} = 0.949$ times the noise norm — residual *norm* close to the noise
norm is the expected outcome, not a failure.

## 6. Weighted least squares

When the errors have known, unequal variances
$\operatorname{Cov}(\mathbf{e}) = C_d = \operatorname{diag}(\sigma_i^{2})$, the
right loss is

$$\hat{\mathbf{m}} = \arg\min\ \sum_i
\frac{\left(d_i-(G\mathbf{m})_i\right)^{2}}{\sigma_i^{2}}
\quad\Longleftrightarrow\quad
\hat{\mathbf{m}} = (G^{\!\top}W G)^{-1}G^{\!\top}W\mathbf{d},\quad
W = C_d^{-1},$$

with covariance $(G^{\!\top}W G)^{-1}$. This is the *generalised least squares*
(GLS) estimator, treated in general form — including correlations, not just
variances — in [18-02-06](06-weighting-and-covariance.md).

The demonstration makes the errors heteroscedastic with
$\sigma_i$ rising linearly from $0.010$ to $0.100\ \mathrm{mGal}$ (a factor ten)
and runs 1000 realisations:

| estimator | sd of $m_2$ (mGal/km) |
|---|---|
| unweighted | 0.001170 |
| weighted (GLS) | 0.000756 |

so the variance ratio is $2.3906$ and the unweighted estimate is a factor
$1.546$ noisier. Predicted GLS sd from $(G^{\!\top}WG)^{-1}$: $0.000794$ against
a measured $0.000756$ — the formula is validated.

Now the subtle part. Suppose the analyst ignores the structure and assumes a
constant $\sigma = 0.0614\ \mathrm{mGal}$ (the rms of the true values). The
predicted sd of $m_2$ becomes $0.001131$ against a measured $0.001170$ — only
$3.4\%$ optimistic. **A symmetric design hides a wrong variance model.** The loss
here shows up in the efficiency of the estimate, not in its quoted error. With
clustered stations and a strongly varying $\sigma$ the error model itself becomes
badly wrong (that is the subject of [18-02-06](06-weighting-and-covariance.md)'s
experiment, where the understatement reaches a factor 33).

## 7. Fully worked example: the design arithmetic

*(a) Predicted uncertainty.* For the straight line through $N$ stations spread
symmetrically, $G^{\!\top}G = \operatorname{diag}(N,\sum x_i^{2})$, so

$$\operatorname{sd}(m_1) = \frac{\sigma}{\sqrt{N}} = \frac{0.05}{\sqrt{20}}
= 0.011180\ \mathrm{mGal},$$

$$\operatorname{sd}(m_2) = \frac{\sigma}{\sqrt{\sum x_i^{2}}} .$$

With $x_i = -20 + \frac{40}{19}i$, $i=0,\dots,19$:
$\sum x_i^{2} = 2947.37\ \mathrm{km^{2}}$ (the measured $\sigma_{\max}$ of
$G^{\!\top}G$), so $\operatorname{sd}(m_2) = 0.05/\sqrt{2947.37}
= 0.000921\ \mathrm{mGal\,km^{-1}}$. Both predictions match the table in §4 to
three digits.

*(b) Data needed for a target.* To halve $\operatorname{sd}(m_2)$ you must
quadruple $\sum x_i^{2}$. Spread the same 20 stations over
$\pm40\ \mathrm{km}$ instead of $\pm20\ \mathrm{km}$: $\sum x_i^{2}$ becomes
$4\times$ larger, so the slope uncertainty halves. This is the single most useful
sentence in survey design for trend estimation.

*(c) Checking a reported fit.* A colleague reports
$\hat{\mathbf{m}} = (12.4, -0.72)$ with $\lVert\mathbf{r}\rVert = 0.26\
\mathrm{mGal}$ and "an excellent fit". Compute
$\chi^{2} = 0.26^{2}/0.05^{2} = 27.0$ with 18 d.o.f. → reduced $\chi^{2} = 1.50$,
$1.5$ sd high: acceptable on its own, but combined with slopes $0.13\
\mathrm{mGal\,km^{-1}}$ away from truth — $142$ times the predicted sd of
$0.0009$ — the fit is inconsistent with the stated noise, or the reported noise
is wrong.

## 8. Assumptions and regime of validity

- **Correct $G$.** Least squares is only as good as the forward model; an
  incorrect kernel biases the estimate and inflates $\chi^{2}$
  ([18-01-02 §2](../01-inverse-problem-foundations/02-hadamard-well-posedness.md)).
- **Errors independent with common variance** for the unweighted estimator, and
  **known** $C_d$ for the weighted one. Unknown $C_d$ → estimate it, and say so
  ([18-02-06](06-weighting-and-covariance.md)).
- **Zero-mean errors.** A constant offset belongs in the model; an unmodelled
  offset appears as bias in $m_1$.
- **$G^{\!\top}G$ invertible.** If not, the problem is *mixed determined* and
  needs the generalised inverse ([18-02-03](03-generalized-inverse.md)).
- **Gaussian errors** for the $\chi^{2}$ interpretation; least squares itself only
  needs the second moments, but the $\chi^{2}$ distribution needs the shape.
- **Squared loss.** Outliers drag a least-squares fit; robust losses exist
  ([21-01-04](../../21-statistics-bayesian-ml/01-statistics-in-practice/04-regression.md)).

## 9. Running the demonstration

The demonstration for this lesson is [`code/overdetermined_demo.py`](code/overdetermined_demo.py) — print-only, no network access, fixed seed
`np.random.default_rng(20261014)`.

```bash
cd 18-inverse-problems/02-linear-inverse-problems/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python overdetermined_demo.py
```

It prints every table above with units, seeded with
`np.random.default_rng(20261014)`; runtime is under a second. Companion problems
are in
[`exercises/01-overdetermined-exercises.md`](exercises/01-overdetermined-exercises.md).

## Mastery checkpoint

Without notes:

> A trend is fitted to $N = 40$ stations spread symmetrically over
> $\pm10\ \mathrm{km}$ with $\sigma = 0.02\ \mathrm{mGal}$. **(a)** Write
> $G^{\!\top}G$ in closed form and give the predicted sds of the intercept and
> slope. **(b)** A fit returns reduced $\chi^{2} = 3.2$. Give three distinct
> explanations and the one test that would distinguish them. **(c)** The errors
> are known to be $0.01\ \mathrm{mGal}$ near the ends and $0.05\ \mathrm{mGal}$
> in the middle. Write the weighted estimator and say what changes in the
> predicted slope uncertainty. **(d)** Explain why the residual is orthogonal to
> the columns of $G$ without doing any algebra.

Worked solutions are in
[`exercises/01-overdetermined-solutions.md`](exercises/01-overdetermined-solutions.md).

## Common pitfalls

1. **Assuming $N>M$ means well determined.** Rank, not dimensions, decides.
2. **Reporting a model without its covariance.** A parameter value without a
   standard deviation is not a result.
3. **Reading reduced $\chi^{2}$ as a goodness-of-fit alone.** It tests the noise
   model as much as the fit.
4. **Using the normal equations out of habit.** Squared condition number.
5. **Ignoring known relative weights.** Costs efficiency and, with clustered
   designs, corrupts the quoted error.
6. **Dropping outliers to "improve" $\chi^{2}$.** Re-estimate the error model or
   use a robust loss, and report what you did.

## Related modules

- [18-02-02 Underdetermined Problems and Minimum-Norm Solutions](02-underdetermined.md) —
  the other extreme, where the fit is exact and the model is not unique.
- [18-02-03 The Generalised (Moore-Penrose) Inverse](03-generalized-inverse.md) —
  one formula that covers both cases.
- [18-02-06 Data Weighting and Error Covariance Specification](06-weighting-and-covariance.md) —
  the full covariance treatment.
- [01-14-04 Linear and Nonlinear Least Squares](../../01-mathematics/14-optimization/04-least-squares.md) —
  the optimisation view, including when to use another loss.
- [21-01-04 Linear, Multiple and Robust Regression](../../21-statistics-bayesian-ml/01-statistics-in-practice/04-regression.md) —
  the statistical view with diagnostics.
