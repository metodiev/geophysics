---
id: 21-04-07
title: "PCA, ICA and Manifold Learning"
level: research
prereqs: ["21-04-06", "01-13-03"]
estimated_minutes: 60
tags: [machine-learning, pca, ica, manifold-learning, dimensionality-reduction]
---

# PCA, ICA and Manifold Learning

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** principal components from the SVD of the centred data and
   **compute** the explained-variance fractions.
2. **Explain** why PCA maximises variance and **state** what that assumes about
   which structure is interesting.
3. **Distinguish** PCA from ICA and **compute** an ICA solution for two mixed
   sources, including the recovery correlation.
4. **Explain** why a curved manifold is not captured by any linear projection and
   **measure** the residual.
5. **Choose** between PCA, ICA and a manifold method for a stated Earth-data
   problem.
6. **State** what a reduced representation discards.

All data in this lesson are **SYNTHETIC**, generated in the demonstration. No
measured value is used.

## Prerequisites

- [21-04-06 Feature Engineering for Earth Data](06-feature-engineering.md) —
  the alternative to reducing dimensionality.
- [01-13-03 Expectation, Variance and Moments](../../01-mathematics/13-probability-and-statistics-foundations/03-expectation-variance.md) —
  covariance and its eigenstructure.
- [21-01-05 Nonparametric Statistics and Kernel Density Estimation](../01-statistics-in-practice/05-nonparametric-methods.md) —
  the density view of structure, which ICA's non-Gaussianity criterion uses.

## 1. Intuition: three different questions about structure

Dimensionality reduction is not one operation, because "structure" is not one
thing:

- **PCA** asks for the directions of maximum variance. It is a linear,
  variance-based projection, and it assumes that high variance is the signal and
  low variance is noise.
- **ICA** asks for the directions in which the projected data are most
  non-Gaussian, on the assumption that the underlying sources are independent and
  non-Gaussian. It recovers sources that PCA mixes.
- **Manifold learning** asks for a low-dimensional coordinate system that follows
  the shape of the data, on the assumption that the data lie near a low-dimensional
  curved surface embedded in a high-dimensional space.

For a covariance matrix with $p$ features the PCA solution is exact and unique; the
other two are iterative and identify their targets only up to sign and
permutation. The honest choice is made by asking which of the three assumptions
matches the problem.

## 2. PCA by the SVD

Centre the data and compute the singular value decomposition
$X_c = U\Sigma V^{\mathsf T}$. Then

$$S = \frac{1}{n-1}X_c^{\mathsf T}X_c = V\frac{\Sigma^{2}}{n-1}V^{\mathsf T},$$

so the columns of $V$ are the principal directions, the eigenvalues are
$\sigma_j^{2}/(n-1)$, and the **explained fraction** of component $j$ is
$\sigma_j^{2}/\sum_k\sigma_k^{2}$. The scores are $U\Sigma$, and the rank-$k$
reconstruction error for centred data is exactly the sum of the discarded
eigenvalues:

$$\|X_c - \hat X_c^{(k)}\|_F^{2} = \sum_{j>k}\sigma_j^{2} .$$

That identity is what makes the scree plot a quantitative device rather than a
heuristic: the discarded singular values **are** the squared reconstruction error.
PCA also minimises the reconstruction error among all rank-$k$ linear projections,
which is the sense in which it is optimal — optimal for a linear, squared-error
criterion and nothing else.

## 3. ICA and why variance is the wrong criterion

Two independent components added together are more Gaussian than either, by the
central limit theorem. So a mixture of non-Gaussian sources has projections whose
kurtosis is lower than the sources' own, and the directions that maximise
non-Gaussianity recover the sources. The demonstration measures exactly that,
after whitening:

| quantity | Gaussian source | Laplace source |
|---|---|---|
| source kurtosis | $-0.1155$ | $+2.4024$ |
| PCA component kurtosis | $+1.4293$ | $+0.0019$ |
| ICA component kurtosis | $+2.4210$ | $-0.1135$ |

The PCA components have swapped the structure: the first PCA direction carries
kurtosis $+1.4293$, between the two sources, and the second is nearly Gaussian at
$+0.0019$. The ICA components recover the sources' kurtoses almost exactly
($+2.4210$ against $+2.4024$, and $-0.1135$ against $-0.1155$), and the recovery
correlations confirm it: $0.9982$ for ICA against $0.8553$ for PCA.

## 4. Manifolds

PCA is linear, so a curved manifold cannot be represented by any projection onto a
line. The demonstration places $400$ points on the parabola $y = x^{2}$ with a
tiny amount of noise, so the intrinsic dimension is $1$ and the embedding
dimension is $2$. PCA assigns explained fractions of $0.7993$ and $0.2007$ and
leaves a reconstruction MSE of $0.043851$ with one component — a $20\ \%$
residual that no choice of a straight line can remove, because the residual is the
curvature itself. A manifold method that measured distance along the curve, or a
feature $x^{2}$, would reduce it to the noise level.

The practical diagnostic is the same one PCA gives: examine the residual. If the
residual is structure rather than noise — a systematic curve, a spiral, a
branching pattern — a linear method is the wrong tool.

## 5. Worked example

**PCA.** Five hundred and fifty-one samples of a two-dimensional latent variable
scaled by $(3.0, 0.5)$, mixed by a rotation and perturbed by $\mathcal N(0,
0.15^{2})$ noise. The singular values are $61.036$ and $9.890$, giving explained
fractions of $0.9744$ and $0.0256$, and the first principal direction is
$[+0.8036, +0.5951]$ — the rotation angle recovered from the data. Reconstructing
with one component leaves an MSE of $0.12227$; with two, $0.00000$ to the printed
precision, as it must, since the data are two-dimensional.

**ICA.** Two thousand samples of a unit-variance Gaussian and a unit-variance
Laplace source mixed by $A = \big(\begin{smallmatrix}1 & 0.4\\ 0.6 & 1\end{smallmatrix}\big)$.
The source kurtoses are $-0.1155$ (Gaussian, as expected) and $+2.4024$
(Laplace). PCA yields component kurtoses of $+1.4293$ and $+0.0019$ — a mixing
of the two — while fixed-point ICA yields $+2.4210$ and $-0.1135$, matching the
sources. The best absolute correlation with a true source is $0.8553$ for PCA and
$0.9982$ for ICA. **PCA was not wrong**: it found the maximum-variance
directions, which is what it is defined to do. It was answering a different
question.

**Manifold.** The parabola example above: intrinsic dimension $1$, but a linear
one-component projection leaves $0.043851$ of reconstruction MSE. Only $0.0001$
of that is the injected noise; the rest is curvature.

## Assumptions and regime of validity

1. **PCA needs the data centred and (usually) scaled**, or the largest-variance
   feature dominates the first component.
2. **PCA assumes variance is signal.** A high-variance direction caused by one
   outlier will be selected first.
3. **ICA assumes independent, non-Gaussian sources and as many mixtures as
   sources**, and is identifiable only up to scaling, sign and permutation.
4. **Manifold methods assume the data lie near a low-dimensional manifold** and
   reconstruct poorly for data that do not.
5. **Every reduction discards information.** A component dropped for being
   low-variance may still be the physically relevant one; a subspace of
   $99\ \%$ explained variance can omit the signal entirely if the signal is
   small.
6. **Components are not physical.** A principal direction is a linear combination
   chosen by the data's covariance; naming it after a physical quantity requires
   an independent argument.

## The honest summary

The three methods answer three different questions and the demonstration makes
the differences measurable. PCA on a correlated two-dimensional cloud explained
$97.44\ \%$ of the variance with one component and reconstructed with an MSE of
$0.12227$; ICA on two mixed sources recovered their kurtoses to within $0.02$ and
their waveforms to a correlation of $0.9982$ where PCA reached only $0.8553$; and
a one-dimensional parabola left a $0.043851$ reconstruction MSE that no linear
projection can remove. The trap is that all three produce a small number of
"factors" with plausible names; only the assumption behind the method makes any of
them interpretable. What the numbers do **not** establish is that a component is
physical, and no amount of explained variance substitutes for that argument.

## Python demonstration

[`code/dimensionality_reduction_demo.py`](./code/dimensionality_reduction_demo.py)
prints every number quoted above. It:

1. computes PCA by the SVD and the reconstruction error against the number of
   components;
2. separates two mixed independent sources by fixed-point ICA and compares the
   recovery with PCA;
3. measures the PCA residual on a one-dimensional curved manifold.

```bash
cd 21-statistics-bayesian-ml/04-machine-learning-fundamentals/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python dimensionality_reduction_demo.py
```

It runs in about a tenth of a second and prints only text.

## Exercises

Graded problems are in
[`exercises/07-dimensionality-reduction-exercises.md`](./exercises/07-dimensionality-reduction-exercises.md)
with worked solutions in
[`exercises/07-dimensionality-reduction-solutions.md`](./exercises/07-dimensionality-reduction-solutions.md).

## Mastery checkpoint

Without notes, PCA on a two-dimensional cloud gives singular values $61.036$ and
$9.890$ with explained fractions $0.9744$ and $0.0256$; ICA recovers source
kurtoses $+2.4024$ and $-0.1155$ to within $0.02$; and a one-dimensional parabola
leaves a one-component reconstruction MSE of $0.043851$.

1. Compute the reconstruction MSE of a one-component PCA from the singular values
   and $n = 400$, and compare it with the printed $0.12227$.
2. State the assumption PCA makes that ICA does not.
3. Compute the ratio of the ICA recovery correlation to the PCA one.
4. State what the parabola residual would be if the manifold were a straight line.

## Common pitfalls

1. **Naming components physically.** A direction of maximum variance is not a
   process.
2. **Forgetting to scale.** Unscaled features make the first component a function
   of the units.
3. **Using PCA to separate independent sources.** It mixes them; that is what the
   kurtosis comparison measures.
4. **Assuming a low explained-variance component is noise.** Small variance can
   be the entire signal in a precise measurement.
5. **Applying a linear method to a curved manifold.** The residual is curvature,
   not noise.
6. **Treating ICA components as ordered.** They are identifiable only up to
   permutation, sign and scale.

## Where this is used

- **Multivariate geochemistry**: PCA of element concentrations to find
  lithological end-members.
- **Seismic attribute analysis**: PCA to compress correlated attributes before
  classification.
- **Hyperspectral remote sensing**: ICA to separate end-members with
  non-Gaussian abundance distributions.
- **Geomagnetic and gravity field separation**: PCA of spatial harmonics.
- **Monitoring networks**: manifold coordinates as a low-dimensional state
  estimate for a sensor array.

## Related lessons

- [21-04-06 Feature Engineering for Earth Data](06-feature-engineering.md) —
  constructing features instead of projecting.
- [21-04-08 Clustering and Unsupervised Structure Discovery](08-clustering.md) —
  the discrete counterpart of a latent coordinate.
- [21-05-05 Autoencoders for Compression and Denoising](../05-deep-learning/05-autoencoders.md) —
  a learned nonlinear generalisation of PCA.
- [21-01-06 Spatial and Directional Statistics in Earth Science](../01-statistics-in-practice/06-spatial-statistics-geo.md) —
  directional statistics, where circular coordinates need their own treatment.
- [21-04-05 Decision Trees, Random Forests and Gradient Boosting](05-trees-and-ensembles.md) —
  an alternative way to handle many correlated features.

## Self-assessment checklist

- [ ] I can derive PCA from the SVD and compute explained fractions.
- [ ] I can state what PCA maximises and what that assumes.
- [ ] I can run an ICA and measure the source recovery.
- [ ] I can diagnose a curved manifold from the PCA residual.
- [ ] I can choose a method from the structure assumed.
- [ ] I can state what a reduced representation discards.
