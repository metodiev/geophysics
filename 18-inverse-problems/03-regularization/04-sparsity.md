---
id: 18-03-04
title: "L1 Regularisation, Sparsity and Compressive Sensing"
level: research
prereqs: ["18-03-02", "18-03-03"]
tags: [inverse-problems, regularization, sparsity, compressive-sensing, lasso]
---

# L1 Regularisation, Sparsity and Compressive Sensing

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the optimality conditions of $\ell_1$-regularised least squares and
   **explain** why they force exact zeros, unlike the quadratic penalty.
2. **Derive** the critical parameter $\alpha_{\max} = \|A^{\mathsf T}d\|_\infty$
   at which the solution is exactly zero, and **test** it numerically.
3. **Derive** the closed-form amplitude bias of the $\ell_1$ solution on a known
   support and **verify** it against a solver to machine precision.
4. **Measure** the phase transition in support recovery as a function of the
   number of measurements, and **state** what constant it implies for
   $m \propto k\log(n/k)$.
5. **Distinguish** support recovery from exact recovery, and **explain** the
   over-selection regime that separates them.
6. **Measure** why a coherent measurement operator destroys the sparsity
   advantage, using a real geophysical kernel as the counter-example.
7. **Apply** debiasing and state the risk it inherits.

All models and data in this module are **SYNTHETIC**: random measurement
matrices, chosen spike models and computer-generated noise. Nothing is measured
and no published recovery threshold is quoted; every number below is computed by
`code/sparsity_demo.py`. The one geophysical element is the exact 2-D line-mass
gravity kernel, used in Section 6 as an example of a coherent operator.

## Prerequisites

- [18-03-02 Tikhonov Regularisation and the Smoothing Trade-Off](02-tikhonov.md) —
  the quadratic penalty this lesson replaces.
- [18-03-03 Choosing the Trade-Off: L-Curve, GCV, Discrepancy Principle](03-parameter-choice.md) —
  why the parameter choice is a model choice, which the Lasso inherits.
- [01-14-01 Convexity, Stationarity and Optimality Conditions](../../01-mathematics/14-optimization/01-convexity.md) —
  subgradients and subdifferentials, used without further introduction.

## 1. Why the $\ell_1$ norm produces zeros

Consider the two regularised problems

$$\min_m\ \tfrac12\|Am-d\|_2^2 + \alpha\|m\|_2^2
\qquad\text{and}\qquad
\min_m\ \tfrac12\|Am-d\|_2^2 + \alpha\|m\|_1 .$$

The level sets of the two penalties are the $\ell_2$ ball (a sphere) and the
$\ell_1$ ball (a diamond in two dimensions, a cross-polytope in $n$). The
data-fidelity term is a quadratic whose level sets are ellipsoids. The minimiser
is the point where the expand ellipse first touches the penalty ball, and

- an ellipsoid generically touches a **sphere** at a point with all coordinates
  non-zero;
- an ellipsoid generically touches a **cross-polytope** at one of its **vertices**,
  where all but one coordinate are exactly zero.

That geometric fact is the whole difference. The $\ell_1$ penalty is the convex
hull of the $\ell_0$ "count of non-zeros" penalty on the unit $\ell_\infty$ ball,
so it is the tightest convex relaxation of the combinatorial problem
$\min\|m\|_0$ subject to $Am=d$. A sparsity prior is therefore not a numerical
trick; it is a *statement* that the model is composed of a few isolated features
— a layered density, a sparse set of sources, a spike train.

## 2. Optimality conditions, the critical parameter, and the solver

### 2.1 Optimality

The functional is convex but not differentiable at $m_i = 0$. Its minimiser
$m$ satisfies

$$-A^{\mathsf T}(Am-d) \in \alpha\,\partial\|m\|_1,
\qquad\text{i.e.}\qquad
\begin{cases}
\left(A^{\mathsf T}(Am-d)\right)_i = -\alpha\,\mathrm{sign}(m_i), & m_i \neq 0,\\[2pt]
\left|(A^{\mathsf T}(Am-d))_i\right| \le \alpha, & m_i = 0 .
\end{cases}$$

The demonstration checks both conditions and reports the maximum violation, the
KKT gap. At $\alpha = 0.05\,\alpha_{\max}$ it is $1.5\times10^{-15}$: the
returned point is the minimiser to machine precision, so everything that follows
is about the estimator rather than the solver.

### 2.2 The critical parameter is exact

Setting $m = 0$ satisfies the second condition for all $i$ exactly when
$\|A^{\mathsf T}d\|_\infty \le \alpha$. Hence

$$\boxed{\ \alpha_{\max} = \|A^{\mathsf T}d\|_\infty\ }$$

and the solution is identically zero for every $\alpha \ge \alpha_{\max}$. The
demonstration confirms both sides of the boundary:

| $\alpha/\alpha_{\max}$ | non-zeros | $\|m\|_2$ |
|---|---|---|
| 1.0001 | 0 | $0.0000$ |
| 0.9999 | 1 | $2.5075\times10^{-4}$ |

This is a rare thing in inverse theory: a parameter threshold that is *exact*,
not asymptotic. It also gives the natural scale for reporting $\alpha$: in units
of $\alpha_{\max}$, which the data determine.

### 2.3 The proximal step and FISTA

The proximal operator of $\alpha\|\cdot\|_1$ is soft thresholding,

$$\mathrm{soft}(x,t) = \mathrm{sign}(x)\max(|x|-t,0),$$

which is why the simplest solver is iterative soft thresholding,
$m^{k+1} = \mathrm{soft}(m^k - \tfrac{1}{L}A^{\mathsf T}(Am^k-d),\,\alpha/L)$
with $L = \|A^{\mathsf T}A\|_2$, and why its accelerated version (FISTA) is used
here. For the demonstration's Gaussian design, $L = 5.1616$. Continuation —
warm-starting from $\alpha_{\max}$ and stepping down — reduces the iterations
needed at small $\alpha$ by orders of magnitude, which is the practical reason
the results below are cheap.

## 3. The bias is exact, and it is not small

Consider the regime in which the support $S$ is recovered exactly. Because
$d = A m_{\mathrm{true}}$ with $m_{\mathrm{true}}$ supported on $S$, the
stationarity condition on $S$ reads

$$A_S^{\mathsf T}A_S\,m_S = A_S^{\mathsf T}d - \alpha\,\mathrm{sign}(m_S)
= A_S^{\mathsf T}A_S\,m_{\mathrm{true},S} - \alpha\,\mathrm{sign}(m_S),$$

so

$$\boxed{\ m_{\mathrm{hat},S} = m_{\mathrm{true},S}
- \alpha\,(A_S^{\mathsf T}A_S)^{-1}\mathrm{sign}(m_S)\ }$$

The estimator is **biased towards zero by an amount proportional to $\alpha$**,
and the direction of the bias is $-(A_S^{\mathsf T}A_S)^{-1}\mathrm{sign}(m_S)$,
which mixes the amplitudes of different spikes when the columns are correlated.

The demonstration verifies this closed form, using the true support, at five
values of $\alpha$:

| $\alpha/\alpha_{\max}$ | max $|$closed form $-$ measured$|$ | median $\hat m/m_{\mathrm{true}}$ |
|---|---|---|
| 0.5 | not applicable (support not exact) | 0.3965 |
| 0.3 | not applicable (support not exact) | 0.6333 |
| 0.1 | $2.2\times10^{-15}$ | 0.8772 |
| 0.05 | $1.8\times10^{-15}$ | 0.9386 |
| 0.02 | $1.6\times10^{-15}$ | 0.9754 |
| 0.01 | $5.6\times10^{-16}$ | 0.9877 |
| 0.001 | $4.4\times10^{-15}$ | 0.9988 |

The agreement is machine precision *where the support is exact*, and the rows
where it is not say so rather than quoting a meaningless number. Two lessons
follow that are easy to get wrong:

- $\ell_1$ is not "unbiased sparse inversion". It is a shrunk estimator, and the
  shrinkage is exactly the price of the sparsity.
- The shrinkage vanishes as $\alpha\to0$, but so does the noise suppression, so
  the bias cannot be removed by choosing a smaller $\alpha$ without paying in
  variance — the same trade-off as [18-03-02](02-tikhonov.md), in a different
  geometry.

## 4. Support recovery is not exact recovery, and over-selection is real

At $\alpha = 0.02\,\alpha_{\max}$ with noiseless data, the support the solver
finds depends on how many spikes are in the model relative to the number of
measurements:

| true $k$ | non-zeros found | true entries found | extra | max $|$extra$|$ |
|---|---|---|---|---|
| 2 | 2 | 2 | 0 | 0 |
| 4 | 4 | 4 | 0 | 0 |
| 6 | 6 | 6 | 0 | 0 |
| 8 | 10 | 8 | 2 | $1.50\times10^{-2}$ |
| 12 | 14 | 12 | 2 | $8.44\times10^{-3}$ |
| 16 | 30 | 16 | 14 | $1.55\times10^{-1}$ |

Three points, all measured:

1. **Exact support recovery has a boundary.** At $m=64$, $n=128$ it holds up to
   $k=6$ and fails from $k=8$. The failure is not a solver failure; it is the
   estimator's behaviour.
2. **The failure mode is over-selection, not under-selection.** Every true spike
   is still found; the estimator adds spurious small coefficients. That is why
   exact recovery requires *stronger* conditions than support recovery, and why
   the amplitude bias formula of Section 3 stops applying.
3. **The extra coefficients grow with $k$** ($1.5\times10^{-2}$ at $k=8$ to
   $1.55\times10^{-1}$ at $k=16$), so they are not numerical dust. A practitioner
   who thresholds the solution must say where the threshold is, and that
   threshold is another parameter.

## 5. The phase transition

The classical statement of compressive sensing is that $m$ measurements suffice
for a $k$-sparse model when $m$ grows like $k\log(n/k)$. The demonstration
measures the 50% support-recovery contour rather than assuming it, with 20 trials
per point, noiseless data, and $\alpha = 0.05\,\alpha_{\max}$:

| $m$ | $k=2$ | $k=4$ | $k=6$ | $k=8$ | $k=10$ | $k=12$ | $k=16$ | $k=20$ |
|---|---|---|---|---|---|---|---|---|
| 64 | 1.00 | 1.00 | 0.65 | 0.30 | 0.15 | 0.05 | 0.00 | 0.00 |
| 96 | 1.00 | 1.00 | 1.00 | 0.75 | 0.65 | 0.50 | 0.05 | 0.00 |

The 50% crossings, expressed as $C = m/(k\log(n/k))$:

- $m = 64$: between $k = 6$ ($C = 3.49$) and $k = 8$ ($C = 2.89$);
- $m = 96$: between $k = 12$ ($C = 3.38$) and $k = 16$ ($C = 2.89$).

So the recovered sparsity grows with the number of measurements in the predicted
*shape* ($m \propto k\log(n/k)$ with $C$ of order 3), while the constant is pinned
only to about a factor of 1.2 by this experiment. Anything more precise would be
over-claiming. Note also the two caveats that a phase-transition plot usually
hides: the result depends on the *rule for $\alpha$* (here
$0.05\,\alpha_{\max}$) as much as on the matrix, and it is a statement about
support recovery, not about the amplitudes.

## 6. The failure mode that matters in geophysics: coherence

The theory behind compressive sensing is a statement about the measurement
operator, and it is not satisfied by the operators geophysicists actually use.
Define the mutual coherence

$$\mu = \max_{i\neq j}\frac{|a_i^{\mathsf T}a_j|}{\|a_i\|_2\|a_j\|_2}.$$

For a random Gaussian design with unit-normalised columns the demonstration
measures $\mu = 0.4928$; for the line-mass gravity kernel (64 stations, 128
cells, sources at $600\ \mathrm{m}$ depth) it measures $\mu = 0.9999$. The two
operators then behave completely differently on identical spike models:

| operator | $k=2$ | $k=4$ | $k=6$ | $k=8$ | debiased error on the recovered support |
|---|---|---|---|---|---|
| Gaussian | 1.00 | 1.00 | 0.87 | 0.60 | $8.1\times10^{-17}$ |
| line-mass kernel | 0.00 | 0.00 | 0.00 | 0.00 | $0.3381$ |

(The columns are unit-normalised in both cases, so the comparison is like for
like.) The kernel never recovers the support, and even after debiasing its
smallest relative error stays at $0.34$: the information needed was never in the
data. This is the honest limit of sparse inversion in potential fields —
overlapping kernels for neighbouring cells make the problem coherent, and
coherence, not sparsity, decides whether $\ell_1$ will work.

## 7. $\ell_1$ against $\ell_2$, and debiasing

With the same noisy data (noise $\sigma = 0.0057$ per datum, $1\%$ of
$\|d\|/\sqrt m$), sweeping $\alpha$:

| estimator | best $\alpha$ | relative model error | non-zeros ($>1\%$ of max) |
|---|---|---|---|
| $\ell_1$ | $7.31\times10^{-3}$ | $0.00721$ | 4 |
| $\ell_2$ | $1.11\times10^{-3}$ | $0.71743$ | 119 |

The $\ell_1$ solution uses 4 coefficients where the model has 4; the $\ell_2$
solution uses 119 of 128. A quadratic penalty dislikes *large* values, so it
spreads each spike over its neighbours; an $\ell_1$ penalty dislikes *many*
values, so it concentrates. A ratio of 100 in model error is the measured
consequence.

**Debiasing.** A least-squares refit on the 4 columns that $\ell_1$ selected
gives a relative error of $0.00196$ at the same $\alpha$: a factor of $3.69$
better than the biased $\ell_1$ solution. The two-step estimator — select with
$\ell_1$, refit on the support — is standard practice and it is not free:

- it inherits the support error, and a wrong support stays wrong after the refit;
- it removes the shrinkage but also removes the protection against noise
  entering the selected columns.

The demonstration reports both numbers so the trade is visible rather than
implied.

## 8. A fully worked numeric example

**Problem (a).** Find the minimiser of $f(m) = \tfrac12(am-d)^2 + \alpha|m|$ for
$a = 1$, $d = 2$, $\alpha = 0.5$.

**Solution.** The gradient of the data term is $a(am-d) = m - 2$, so the
proximal step gives

$$m^\star = \mathrm{soft}\left(2 - 0,\; \frac{\alpha}{a^2}\right)
= \mathrm{soft}(2,\,0.5) = 1.5 .$$

Check the optimality condition: $a(am^\star-d) = 1.5-2 = -0.5
= -\alpha\,\mathrm{sign}(m^\star)$ with $\mathrm{sign}(1.5) = +1$. ✔ The bias is
$d - m^\star = 0.5 = \alpha/a^2$.

**Problem (b).** The same one-parameter problem with $d = 0.3$ and $\alpha = 0.5$.

**Solution.** $\mathrm{soft}(0.3,0.5) = 0$: the solution is *exactly* zero. The
threshold is $|d| \le \alpha/a^2$, i.e. $\alpha_{\max} = |a d| = 0.3$ — the general
$\|A^{\mathsf T}d\|_\infty$ in one dimension. ✔

**Problem (c).** For the demonstration's 128-cell problem at $\alpha =
0.05\,\alpha_{\max}$, the median recovered amplitude is $0.9386$ of the truth.
Compute the shrinkage implied by the closed form for a *single* isolated spike of
amplitude $2.5$ with $\|a_j\|_2 = 1$: the bias is
$\alpha(A_S^{\mathsf T}A_S)^{-1}\mathrm{sign}(m_S) = \alpha = 0.05\,\alpha_{\max}$,
so the recovered amplitude would be $2.5 - 0.05\,\alpha_{\max}$. With
$\alpha_{\max} = 2.6527$ (the value the demonstration prints), that is
$2.5 - 0.1326 = 2.367$, i.e. $94.7\%$ of the truth. The measured median is
$93.9\%$, slightly worse because $(A_S^{\mathsf T}A_S)^{-1}$ has off-diagonal
terms that transfer bias between neighbouring spikes. **The closed form is exact;
the single-spike approximation is not.**

## 9. Assumptions and regime of validity

1. **The model really is sparse.** Every result above assumes the true model has
   few non-zeros. Applied to a smooth field, $\ell_1$ produces a blocky
   artefactual field, which is the failure measured in
   [18-03-05](05-total-variation.md) for its close relative.
2. **The design is incoherent enough.** Section 6 measures what happens when it
   is not: no recovery at any $\alpha$, and 114 times the error of the Gaussian
   design after debiasing.
3. **The noise is white.** In the noiseless experiments here it is zero by
   construction; the debiasing numbers use white noise at a stated level.
4. **The support-recovery boundary depends on $\alpha_{\max}$-relative rules.**
   The phase transition is a joint property of the matrix, the sparsity and the
   parameter rule; changing the rule moves the curve.
5. **The amplitude of the spikes matters.** The measured amplitudes here lie in
   $[0.7,3.0]$; smaller amplitudes are shrunk to zero earlier and are the first
   to be lost.
6. **Over-selection is not detected by the residual.** Extra small coefficients
   can improve the fit while being spurious, so a small residual is not evidence
   that the support is correct.

## 10. The honest summary

- The $\ell_1$ penalty buys exact zeros, and the price is a shrinkage bias that
  is known in closed form and verified to machine precision.
- The parameter has an exact scale, $\alpha_{\max} = \|A^{\mathsf T}d\|_\infty$,
  which makes reporting it much easier than for Tikhonov.
- Support recovery has a phase transition whose shape is
  $m \propto k\log(n/k)$, with a measured constant of order 3 here; the constant
  is a property of the experiment, not a law.
- The technique works when the measurement operator is incoherent, and
  geophysical kernels often are not; that is a property of the physics, not of
  the algorithm.
- Debiasing fixes the bias and keeps the support risk. Both numbers belong in a
  report.

## 11. Python demonstration

`code/sparsity_demo.py` prints: the KKT verification of the solver; the exact
$\alpha_{\max}$ boundary; the support and the closed-form bias check across
$\alpha$; the over-selection table; the 50% phase-transition contour for two
measurement counts with the implied constant $C$; the $\ell_1$–$\ell_2$
comparison and the debiasing result; and the coherence failure using the
line-mass kernel.

```bash
cd 18-inverse-problems/03-regularization/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python sparsity_demo.py
```

Print-only, seeded with `np.random.default_rng(20261014)`, about 1.3 seconds.

## 12. Exercises

Full sets with worked solutions are in
[`exercises/04-sparsity-exercises.md`](exercises/04-sparsity-exercises.md) and
[`exercises/04-sparsity-solutions.md`](exercises/04-sparsity-solutions.md).

- **★** Compute $\mathrm{soft}(-3.2, 0.7)$ and $\mathrm{soft}(0.4,0.7)$, and state
  which of the two is the solution of a one-parameter Lasso with $A=1$, $d=-3.2$
  and $d=0.4$ respectively.
- **★★** Derive $\alpha_{\max} = \|A^{\mathsf T}d\|_\infty$ from the optimality
  conditions, being explicit about the subdifferential of $\|\cdot\|_1$ at zero.
- **★★★** Design a measurement geometry for the line-mass problem that lowers
  the mutual coherence below $0.9$ (stations at non-uniform depths, multiple
  station lines, or a different cell size) and specify the measurement that
  would show whether support recovery improves.

## 13. Mastery checkpoint

Complete this without notes:

> A colleague applies an $\ell_1$ inversion to a gravity profile with the
> line-mass kernel and reports that five isolated sources were recovered.
> **(a)** Given the measured mutual coherence of that kernel, what is the most
> likely status of those five sources, and what single diagnostic would you ask
> for? **(b)** The colleague then debiases by least squares on the five selected
> cells and reports a residual of $0.9\,n\sigma^2$. Does that validate the
> selection? **(c)** Compute the shrinkage that a spike of amplitude $3.0$ would
> suffer at $\alpha = 0.05\,\alpha_{\max}$ with $\alpha_{\max} = 2.6527$ and
> $\|a_j\|_2 = 1$ in the single-spike approximation, and state what the
> demonstration measures instead.

A worked version of (a)–(c) appears in
[`exercises/04-sparsity-solutions.md`](exercises/04-sparsity-solutions.md).

## 14. Common pitfalls

1. **Calling $\ell_1$ "unbiased".** The bias is $\alpha(A_S^{\mathsf T}A_S)^{-1}
   \mathrm{sign}(m_S)$, verified to $10^{-15}$.
2. **Choosing $\alpha$ without the $\alpha_{\max}$ scale.** The natural range is
   $(0,\alpha_{\max})$; anything outside it is zero or noise.
3. **Reporting the support as if it were the model.** Recovered supports here
   over-select by up to 14 coefficients at $k=16$.
4. **Assuming sparsity theory transfers to geophysical kernels.** Measured
   recovery is $0.00$ for the line-mass kernel at every sparsity tested.
5. **Thresholding the solution by eye.** The threshold is a parameter and must be
   stated; the extra coefficients reach $1.55\times10^{-1}$ in amplitude.
6. **Believing a small residual proves the support.** The debiased fit can be
   good while the support is wrong, because a wrong support can still fit the
   data within the noise.

## 15. Where this is used

- **Potential fields.** Compact-source and sparse-layer models for gravity and
  magnetics; the coherence problem of Section 6 is the active research issue.
- **Seismic.** Sparse spike deconvolution and sparse reflectivity inversion are
  the same mathematics with a convolutional matrix; see
  [20-07-01 Sparse and L1 Deconvolution](../../20-signal-processing/07-inversion-in-signal-processing/01-sparse-deconvolution.md).
- **Data reconstruction.** Compressive sensing for missing traces and irregular
  acquisition geometries, where the design matrix is genuinely incoherent; see
  [20-07-02 Compressive Sensing and Data Reconstruction](../../20-signal-processing/07-inversion-in-signal-processing/02-compressive-sensing-signals.md).
- **Statistical learning.** The Lasso is the same estimator with a different
  vocabulary; the bias–variance and selection issues are identical; see
  [21-04-02 Bias-Variance Trade-Off, Underfitting and Overfitting](../../21-statistics-bayesian-ml/04-machine-learning-fundamentals/02-bias-variance.md).

## 16. Related modules

- [18-03-05 Total Variation and Edge-Preserving Inversion](05-total-variation.md) —
  the $\ell_1$ penalty applied to differences instead of coefficients.
- [18-03-06 Physical Constraints, Bounds and Feasible Model Sets](06-constraints.md) —
  hard constraints, which are the limit of an infinitely confident prior.
- [18-07-01 Joint Inversion: Concepts and Weighting](../07-joint-and-multi-physics-inversion/01-joint-inversion-concepts.md) —
  combining a sparse and a smooth penalty across data sets.
- [18-08-03 Assessing a Model: Resolution, Artifacts, Alternatives](../08-practical-inversion-workflow/03-model-assessment.md) —
  how a recovered support should be reported.
- [18-02-02 Underdetermined Problems and Minimum-Norm Solutions](../02-linear-inverse-problems/02-underdetermined.md) —
  the $\ell_2$ default that $\ell_1$ replaces.

## 17. Self-assessment checklist

- [ ] I can explain the vertex argument for sparsity without equations.
- [ ] I can write the two optimality conditions and check them numerically.
- [ ] I can derive and test $\alpha_{\max}$.
- [ ] I can derive the closed-form bias and say when it applies.
- [ ] I can state the measured phase transition and its caveats.
- [ ] I can define mutual coherence and say why it decides the outcome.
