---
id: 18-02-05
title: "Resolution and Information Matrices in Interpretation"
level: doctoral
prereqs: ["18-02-04", "18-02-03", "06-06-03"]
tags: [inverse-problems, resolution-matrix, information-matrix, covariance, interpretation]
---

# Resolution and Information Matrices in Interpretation

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** the model resolution matrix $R=G^{+}G$, the data resolution matrix
   $D=GG^{+}$ and the null-space projector $N=I-R$, and **derive** the four
   identities they satisfy.
2. **Compute** per-cell self-resolution and averaging-kernel width, and **rank**
   cells by how well they are determined.
3. **Quantify** how much of a test pattern (smooth, checkerboard, spike) is
   invisible, and **use** that number in place of adjectives.
4. **Form** the information matrix $G^{\!\top}C_d^{-1}G$ and **interpret** its
   eigenvalues as inverse variances.
5. **Compare** the posterior standard deviation of a single cell with that of a
   resolved combination, and **explain** why combinations beat cells.
6. **Verify** that the covariance plus the resolution bias predicts the achieved
   accuracy of an inversion, and **use** that as a pre-report check.
7. **Rewrite** an unsupportable claim about a cell into a supportable claim about
   a resolved combination.

## Prerequisites

- [18-02-04 SVD Analysis: Model Resolution and Data Importance](04-svd-analysis-inverse.md) —
  the singular triplets and the truncation analysis used to build the matrices here.
- [18-02-03 The Generalised (Moore-Penrose) Inverse](03-generalized-inverse.md) —
  $G^{+}$ and the projectors it defines.
- [06-06-03 Resolution, Null Space and Model Covariance](../../06-seismology/06-seismic-tomography/03-resolution-and-nullspace.md) —
  the same matrices as they appear in a tomographic study.

## 1. Two matrices and a projector

The whole of this lesson follows from two products and one difference:

$$R = G^{+}G \quad\text{(model resolution)},\qquad
D = GG^{+} \quad\text{(data resolution)},\qquad
N = I-R \quad\text{(null-space projector)} .$$

Their meanings are operational rather than abstract. Substituting
$\mathbf{d} = G\mathbf{m}_{\text{true}}+\mathbf{e}$ into
$\hat{\mathbf{m}} = G^{+}\mathbf{d}$:

$$\hat{\mathbf{m}} = R\,\mathbf{m}_{\text{true}} + G^{+}\mathbf{e}.$$

So $R$ is exactly the operator that the estimator applies to the truth: the answer
is always a **filtered** version of the Earth (and $R=I$ would mean perfect
recovery), while the second term is the noise. The complementary projector $N$
identifies what the experiment cannot see at all. The data-side matrix satisfies
$D\mathbf{d} = G\hat{\mathbf{m}}$: it is the projector onto the fitted part of the
data.

All models and data in this module are **SYNTHETIC**.

## 2. The demonstration geometry

Sixteen cells at $0.5,\dots,15.5\ \mathrm{km}$ are probed by twelve rays, each a
$0.6/1.0/0.6$ weighted sum over three consecutive cells: five rays over cells
0–6, four over cells 6–12 and three over cells 10–14. The measured spectrum is

$$\sigma = (2.11672,\ 2.05633,\ 1.87779,\ 1.66584,\ 1.51297,\ 1.15291,\
1.05231,\ 0.68264,\ 0.53800,\ 0.30666,\ 0.19815,\ 0.12456),$$

so $\operatorname{rank}(G) = 12$, $\dim\mathcal{N}(G) = 4$,
$\dim\operatorname{range}(G)^{\perp} = 0$, and
$\kappa(G) = 16.99$ — a benign spectrum, deliberately, so that the resolution
structure rather than the conditioning is the subject. The true model is
$\mathbf{m}_{\text{true}} = 0.30 + 0.08\cos(2\pi x/16)\ \mathrm{s}$ and the noise
is $\sigma_{\text{data}} = 0.004\ \mathrm{s}$.

## 3. The identities, checked

These four checks catch almost every implementation error in this area:

| identity | meaning | measured $\max\lvert\cdot\rvert$ |
|---|---|---|
| $GR - G$ | $R$ leaves the data unchanged | $1.332\times10^{-15}$ |
| $RG^{+} - G^{+}$ | $G^{+}$ lies in the resolved subspace | $2.220\times10^{-15}$ |
| $R^{2} - R$ | $R$ is a projector | $1.221\times10^{-15}$ |
| $D^{2} - D$ | $D$ is a projector | $1.332\times10^{-15}$ |
| $GN$ | the null space is annihilated | $1.273\times10^{-15}$ |

and the traces:

$$\operatorname{tr}R = 12.000000 = \operatorname{tr}D = \operatorname{rank}(G).$$

The trace identity is the counting statement of the whole folder: the number of
independent model combinations equals the number of independent data. It gives a
one-line answer to "how much model does this experiment support?".

## 4. Per-cell resolution

For each cell $j$, the row $R_{j\cdot}$ is the averaging kernel and $R_{jj}$ is the
self-resolution. Measured:

| cell | $x$ (km) | $R_{jj}$ | width (km) | verdict |
|---|---|---|---|---|
| 0 | 0.5 | 0.846 | 5.9933 | coarsely |
| 1 | 1.5 | 0.852 | 5.4575 | coarsely |
| 2 | 2.5 | 0.740 | 4.3380 | coarsely |
| 3 | 3.5 | 0.646 | 2.6507 | well |
| 4 | 4.5 | 0.686 | 2.6041 | well |
| 5 | 5.5 | 0.811 | 3.2798 | coarsely |
| 6 | 6.5 | 0.868 | 3.4351 | coarsely |
| 7 | 7.5 | 0.860 | 3.5914 | coarsely |
| 8 | 8.5 | 0.803 | 3.1700 | coarsely |
| 9 | 9.5 | 0.768 | 3.1370 | coarsely |
| 10 | 10.5 | 0.796 | 4.0736 | coarsely |
| 11 | 11.5 | 0.854 | 4.9721 | coarsely |
| 12 | 12.5 | 0.870 | 5.2810 | coarsely |
| 13 | 13.5 | 0.826 | 4.7210 | coarsely |
| 14 | 14.5 | 0.774 | 4.2700 | coarsely |
| 15 | 15.5 | 0.000 | — | **not measured** |

("well" = width below 3 km; the threshold is a reporting choice and should be
stated.) The number to internalise: **mean width over the covered cells is
4.0650 km** — the inversion cannot honestly report structure finer than a few
kilometres, even though the cells are 1 km wide. The best cells are 3 and 4
(widths 2.65 and 2.60 km), which lie in the overlap of two ray families; the ends
are worst, and cell 15 has $R_{jj} = 0$ because no ray reaches it.

Note that $R_{jj}$ is *largest* at the ends (0.846 at cell 0) and smallest in the
middle (0.646 at cell 3), while the widths go the other way. Self-resolution and
resolution are different quantities; report both or you will mislead a reader.

## 5. Pattern tests, quantified

Instead of arguing about whether a feature "should" be resolvable, test the
pattern. For a pattern $\mathbf{p}$, measure the fraction of its norm that survives
the resolution operator, and the complementary null-space energy:

$$\text{recovered} = \frac{\lVert R\mathbf{p}\rVert}{\lVert\mathbf{p}\rVert},
\qquad
\text{invisible} = 1 - \frac{\lVert R\mathbf{p}\rVert^{2}}{\lVert\mathbf{p}\rVert^{2}} .$$

Measured:

| pattern | $\lVert G\mathbf{p}\rVert/\lVert\mathbf{p}\rVert$ | recovered | invisible |
|---|---|---|---|
| smooth cosine $\cos(2\pi x/16)$ | 1.6151 | 0.9348 | 0.066 |
| 2-cell checkerboard | 0.1732 | 0.7923 | 0.372 |
| end spike (cell 0) | 0.6000 | 0.9200 | 0.154 |

The smooth pattern is almost fully visible; the checkerboard keeps 79.2% of its
norm, so **37.2% of its energy is invisible to these rays**. The end spike is
visible in norm terms (92%) because its data image is large, but the recovered
pattern is a smeared version of it — its *location* is not recovered to one cell.
Note the difference between "energy recovered" and "position recovered"; the
resolution matrix answers the first, and the width of the kernel in §4 answers the
second.

## 6. The information matrix and what it measures

With a known data covariance $C_d = \sigma^{2}I$ the **information matrix** is

$$F = G^{\!\top}C_d^{-1}G = \frac{G^{\!\top}G}{\sigma^{2}},$$

whose eigenvalues are $\sigma_i^{2}/\sigma^{2}$ and whose eigenvectors are the
$\mathbf{v}_i$. In a Bayesian reading $F$ is the inverse of the (Gaussian) model
covariance, so a large eigenvalue means a well-determined direction. Measured:

$$\text{eig}(F) = (2.800\times10^{5},\ 2.643\times10^{5},\ 2.204\times10^{5},\
1.734\times10^{5},\ 1.431\times10^{5},\ 8.307\times10^{4},\ 6.921\times10^{4},\
2.912\times10^{4},\ 1.809\times10^{4},\ 5.877\times10^{3},\ 2.454\times10^{3},\
9.697\times10^{2}),$$

with exactly $12$ eigenvalues above $10^{-10}$ of the largest — the rank again,
recovered on the model side — and a largest-to-smallest ratio of
$3.463\times10^{-3}$. The model covariance is therefore

$$C_m = V_r\,\operatorname{diag}\!\left(\frac{\sigma^{2}}{\sigma_i^{2}}\right)
V_r^{\!\top},\qquad
\operatorname{Cov}(\hat{m}_j) = [C_m]_{jj}.$$

Measured per-cell standard deviations run from $0.003189\ \mathrm{s}$ (cell 3) to
$0.017106\ \mathrm{s}$ (cell 0) — a factor $5.4$ — and the cell-wise numbers are
*not* monotone in position, because they mix the geometry of the ray families.

## 7. Why combinations beat cells

Ask the same question of a three-cell average, $\mathbf{c} = (1/3,1/3,1/3)$ over
three adjacent cells: its standard deviation is $\sqrt{\mathbf{c}^{\!\top}C_m
\mathbf{c}}$. Measured:

$$\text{median per-cell sd} = 0.009500\ \mathrm{s},\qquad
\text{median three-cell-average sd} = 0.002835\ \mathrm{s},\qquad
\text{ratio} = 3.351 .$$

Averaging three cells is **3.35 times better determined** than the typical single
cell — because the average lies closer to the row space of $G$ than its
constituents do. This is the quantitative justification for the interpretive habit
of reporting regional averages rather than cell values, and it is the same
statement as $R$ having off-diagonal structure: smoothing along the kernel is what
the data actually do.

## 8. Verification: does the covariance predict the outcome?

Before trusting any resolution statement, run this check. For the same operator,
true model and noise level, the predicted rms retrieval error is

$$\text{predicted} = \sqrt{\operatorname{mean}_j[C_m]_{jj}
+ \operatorname{mean}_j[(R\mathbf{m}_{\text{true}}-\mathbf{m}_{\text{true}})_j]^{2}} .$$

Measured: $\lVert G\hat{\mathbf{m}}-\mathbf{d}_{\text{obs}}\rVert_\infty
= 1.443\times10^{-15}\ \mathrm{s}$ (the fit is exact to machine precision, since
the operator has full row rank), one-realisation rms error
$0.102611\ \mathrm{s}$, predicted $0.101689\ \mathrm{s}$, and over $300$
realisations a mean rms error of $0.101661\ \mathrm{s}$ with sd
$0.000398\ \mathrm{s}$ — a ratio of $0.9997$ to the prediction.

That is the test to run on any new problem: **if the covariance plus the resolution
bias does not predict the achieved error in a synthetic experiment, the error model
is wrong.**

## 9. Fully worked example: rewriting a claim

*(a) The unsupportable claims.* From §4 and §5, all three of these fail:

- "the anomaly is in cell 14" — cell 14 has a 4.27 km averaging kernel, so the
  estimated value at cell 14 is an average over neighbouring cells; the location is
  not resolved to one cell;
- "cell 15 is undisturbed" — cell 15 has $R_{jj}=0$: it was never measured, and
  nothing at all can be said about it;
- "the checkerboard is present" — 37.2% of the checkerboard's energy lies in the
  null space, so its amplitude is systematically underestimated and the pattern
  cannot be certified.

*(b) Supportable versions.*

- "the twelve ray sums are reproduced to within the data error;
- the smooth $\cos(2\pi x/16)$ component is recovered to 93.5% of its norm;
- a 2-cell checkerboard would be recovered at only 79.2%, with 37.2% of its energy
  invisible to this experiment."

*(c) The rule.* A statement is defensible exactly to the extent that its indicator
vector lies in $\operatorname{range}(G^{\!\top})$. Test it: project the indicator
vector, and report either the projection or the invisible fraction.

## 10. Assumptions and regime of validity

- **Known data covariance.** §6 uses $C_d=\sigma^{2}I$. With correlated errors the
  information matrix is $G^{\!\top}C_d^{-1}G$ and the whitened operator is what
  must be analysed ([18-02-06](06-weighting-and-covariance.md)).
- **A linear, correct $G$.** Resolution says nothing about model error, which
  enters as a systematic bias in every cell
  ([18-01-04](../01-inverse-problem-foundations/04-discretisation-reality.md)).
- **Cell size as the unit.** All widths are in kilometres *for these cells*;
  changing the parameterisation rescales them.
- **Unregularised or truncated estimators.** The matrices shown belong to the
  truncated-SVD estimator. Adding Tikhonov damping changes $R$ to
  $R_\alpha = (G^{\!\top}G+\alpha^{2}I)^{-1}G^{\!\top}G$
  ([18-03-02](../03-regularization/02-tikhonov.md)).
- **Gaussian errors for the covariance language.** The projectors and traces are
  distribution-free, but "standard deviation" is not.

## 11. Running the demonstration

The demonstration for this lesson is [`code/resolution_matrices_demo.py`](code/resolution_matrices_demo.py) — print-only, no network access, fixed seed
`np.random.default_rng(20261014)`.

```bash
cd 18-inverse-problems/02-linear-inverse-problems/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python resolution_matrices_demo.py
```

It prints the matrices, the identities, the per-cell table, the pattern tests, the
information spectrum, the covariance comparison and the end-to-end verification.
Runtime is under a second. Companion problems are in
[`exercises/05-resolution-matrices-exercises.md`](exercises/05-resolution-matrices-exercises.md).

## Mastery checkpoint

Without notes:

> An inversion returns a model on a 16-cell grid with $\operatorname{tr}R = 12$.
> **(a)** How many independent model combinations did the experiment provide, and
> how many cells could in principle be resolved? **(b)** Cell A has
> $R_{jj}=0.87$ and a kernel width of 5.3 km; cell B has $R_{jj}=0.65$ and a width
> of 2.6 km. Which cell's value would you quote to a colleague, and why?
> **(c)** Write the claim "the anomaly is confined to cells 12–15" in a form the
> data support. **(d)** The median three-cell-average standard deviation is 3.35
> times smaller than the median per-cell standard deviation. Explain this without
> referring to the numbers.

Worked solutions are in
[`exercises/05-resolution-matrices-solutions.md`](exercises/05-resolution-matrices-solutions.md).

## Common pitfalls

1. **Reporting $R_{jj}$ as "resolution".** It is self-resolution; add the kernel
   width.
2. **Assuming unmeasured cells are undisturbed.** $R_{jj}=0$ means *no*
   information, not *no anomaly*.
3. **Using adjectives where a fraction exists.** "Poorly resolved" → the invisible
   energy fraction.
4. **Comparing per-cell errors with regional errors.** Combinations are better
   determined, often by a factor of three or more.
5. **Omitting the covariance when quoting numbers.** A value without a standard
   deviation is not a result.
6. **Skipping the end-to-end verification of §8.** It is cheap and it catches a
   wrong error model before a reviewer does.

## Related modules

- [18-02-04 SVD Analysis: Model Resolution and Data Importance](04-svd-analysis-inverse.md) —
  the machinery behind these matrices.
- [18-02-06 Data Weighting and Error Covariance Specification](06-weighting-and-covariance.md) —
  $C_d$ in general and what happens when it is wrong.
- [18-08-03 Assessing a Model: Resolution, Artifacts, Alternatives](../08-practical-inversion-workflow/03-model-assessment.md) —
  how these diagnostics enter a review.
- [06-06-03 Resolution, Null Space and Model Covariance](../../06-seismology/06-seismic-tomography/03-resolution-and-nullspace.md) —
  the seismological usage.
- [21-03-02 Conjugate Priors and Analytic Posteriors](../../21-statistics-bayesian-ml/03-bayesian-inference/02-conjugate-priors.md) —
  the Bayesian version of the covariance statement.
