# Solutions — 21-04-07 PCA, ICA and Manifold Learning

> Read after attempting. Lesson:
> [07 Dimensionality Reduction](../07-dimensionality-reduction.md). Numbers quoted
> from the demonstration reproduce its output.

---

## ★1 — Explained fractions and reconstruction error

$$\text{fraction}_1 = \frac{61.036^{2}}{61.036^{2} + 9.890^{2}}
= \frac{3725.4}{3725.4 + 97.8} = \frac{3725.4}{3823.2} = 0.9744,$$

$$\text{fraction}_2 = \frac{97.8}{3823.2} = 0.0256,$$

matching the printed values ✔.

**One-component reconstruction MSE:** discarding the second component leaves

$$\frac{\sigma_2^{2}}{n-1} = \frac{97.811}{399} = 0.24514 .$$

The demonstration prints $0.12227$, exactly **half** of $0.24514$. The factor of
two is the convention: the reconstruction error is a mean squared error computed as
$\|X_c - \hat X_c\|_F^{2}/(n\,p)$ with $p = 2$ columns, i.e. the discarded squared
singular value is divided by both $n-1$ and the number of variables. The identity
$\|X_c - \hat X_c^{(k)}\|_F^{2} = \sum_{j>k}\sigma_j^{2}$ is therefore exact up to
this normalisation, and the useful statement is the *ratio*: one component leaves
$2.56\ \%$ of the total squared deviation, whatever normalisation is chosen.

---

## ★2 — Which method recovered the sources

**ICA.** Its component kurtoses, $+2.4210$ and $-0.1135$, match the source
kurtoses $+2.4024$ and $-0.1155$ to within $0.02$ — for a kurtosis estimated from
$2000$ samples whose own standard error is $\sqrt{24/n} = 0.11$, that is an exact
match. PCA's components give $+1.4293$ and $+0.0019$: the first is between the two
source values and the second is essentially Gaussian, which is what a **mixture**
of two sources looks like.

The reason is the central limit theorem: sums of independent variables are more
Gaussian than their components, so any mixed direction has kurtosis closer to zero
than the sources. ICA searches for the directions that minimise Gaussianity and
therefore undoes the mixing.

---

## ★3 — Curvature versus noise in the residual

$$\text{curvature fraction} = \frac{0.043851 - 0.0001}{0.043851}
= \frac{0.043751}{0.043851} = 0.9977,$$

i.e. **$99.77\ \%$** of the one-component residual is curvature, and only
$0.23\ \%$ is the injected noise. The single-component PCA has therefore not failed
to find "some" structure — it has found all the linear structure there is, and the
residual is the systematic part of the shape that a straight line cannot represent.
A manifold method that measures distance along the curve would remove it.

---

## ★★4 — PCA from the SVD

Centre the data: $X_c = X - \mathbf 1\bar x^{\mathsf T}$, then take the thin SVD
$X_c = U\Sigma V^{\mathsf T}$ with $\Sigma$ the $p\times p$ diagonal of singular
values in decreasing order and $V$ orthogonal. Then

$$S = \frac{1}{n-1}X_c^{\mathsf T}X_c
= \frac{1}{n-1}V\Sigma U^{\mathsf T}U\Sigma V^{\mathsf T}
= V\,\frac{\Sigma^{2}}{n-1}\,V^{\mathsf T},$$

which is an eigendecomposition of the sample covariance: the columns of $V$ are
the eigenvectors (principal directions) and $\sigma_j^{2}/(n-1)$ the eigenvalues
(variances of the scores).

**Rank-$k$ reconstruction.** The best rank-$k$ approximation in the Frobenius norm
is obtained by truncating the SVD (Eckart–Young):

$$\hat X_c^{(k)} = U_k\Sigma_k V_k^{\mathsf T}, \qquad
\|X_c - \hat X_c^{(k)}\|_F^{2} = \sum_{j>k}\sigma_j^{2},$$

so the discarded squared singular values **are** the squared reconstruction error.
This is why a scree plot is a quantitative device rather than a heuristic: the
height of each bar is literally the error its component would save.

---

## ★★5 — Why mixing Gaussianises, and what ICA does with it

Let $s_1, s_2$ be independent with finite variance. For any unit vector $w$, the
projection $w^{\mathsf T}s$ is a weighted sum of independent variables. By the
CLT its distribution is closer to Gaussian than either component, and for
non-Gaussian sources this is a theorem (the entropy of a sum of independent
variables is at least that of a Gaussian with the same variance). A mixture
therefore has projections whose **kurtosis is pulled towards zero** relative to the
sources — which is exactly the pattern measured: sources at $+2.4024$ and
$-0.1155$, PCA mixture directions at $+1.4293$ and $+0.0019$.

ICA inverts the logic: since mixing Gaussianises, the **sources are the directions
of maximum non-Gaussianity**. After whitening (so that the search is over
rotations only), ICA maximises a non-Gaussianity measure — kurtosis, or the
fixed-point criterion $\mathbb E[z\,g(w^{\mathsf T}z)] - \mathbb E[g'(\cdot)]w = 0$
used in FastICA — and the resulting directions recover the sources up to sign,
scale and permutation.

---

## ★★6 — Correlation ratios

$$\frac{0.9982}{0.8553} = 1.167 .$$

ICA recovers the sources $16.7\ \%$ better in correlation, and — more decisively —
it recovers their *distributional shape* (the kurtoses match to $0.02$).

PCA is not a failure: it solved the problem it defines, which is to find the
directions of maximum variance. It simply mixed the sources, because a rotation
that mixes independent components has, in general, a larger variance along its
first axis than either source direction. Reporting PCA components as "the sources"
would be a modelling error — not an arithmetic one — and the kurtosis comparison is
the evidence that the components are still mixtures.

---

## ★★★7 — PCA under contamination

**Data.** The demonstration's two-dimensional cloud: $n = 400$ samples from a
latent $\mathcal N(0, \mathrm{diag}(3.0^{2}, 0.5^{2}))$ rotated by $40^{\circ}$ and
perturbed with $\mathcal N(0, 0.15^{2})$ noise.

**Contamination.** Replace a fraction $f \in \{0, 0.01, 0.02, 0.05, 0.10, 0.20\}$
of randomly chosen rows with points drawn from $\mathcal N(0, 20^{2}I)$ in one
coordinate — gross outliers at $20$ times the scale.

**Metric.** The angle between the first principal direction and its
outlier-free value; the explained fraction of the first component; and the
one-component reconstruction MSE. All are reported against $f$.

**Replicates.** $M = 1000$ data sets per $f$; the angle estimate then has a
standard error well below $1^{\circ}$.

**Prediction.** Because PCA is a **least-squares** procedure, a single outlier at
$20\sigma$ carries $400\times(20/3)^{2} \approx 1.8\times10^{4}$ times the weight of
a typical point, so even $f = 0.01$ rotates the first direction substantially —
typically by tens of degrees — and reduces its explained fraction. By $f = 0.05$ the
first component points at the outliers and the explained fraction is dominated by
contamination rather than by the latent structure. The headline is the angle
versus $f$, together with the closing recommendation: use a robust covariance
estimate or remove outliers before PCA, since the method has no built-in resistance
at all.

---

## ★★★8 — PCA, ICA and a manifold method on a curved mixing line

**Data.** Two independent geochemical end-members, $s_1$ uniform on
$[0, 1]$ and $s_2$ with a heavy-tailed positive distribution, mixed by a stated
matrix $A$ and then mapped through a **curved** mixing relation, for example
$c_1 = e^{s_1}$, $c_2 = s_1 + s_2^{2}$, so that the sampled points lie on a curve
in the measured space. Add $1\ \%$ relative measurement noise.

**Methods.** PCA (linear variance), FastICA (independence), and a manifold method
such as Isomap or a locally linear embedding, or simply a feature engineering step
$(\ln c_1, \sqrt{c_2 - c_1})$ that linearises the mixing.

**External criterion.** The correlation of the recovered coordinates with the
**true** end-member fractions $s_1, s_2$ — available here because the data are
simulated, and the only honest test of a source-recovery method. Report the best
absolute correlation for each method, as in the demonstration, together with the
kurtosis of each recovered coordinate against the source kurtosis.

**Replicates.** $M = 500$ data sets; the correlation of an ICA coordinate with its
source has a sampling standard error of about $1/\sqrt{n}$ at $n = 2000$, i.e.
$0.02$.

**Prediction.** PCA recovers the curved mixing line's chord and correlates about
$0.85$ with the leading source, but conflates the two end-members on the curved
portions. ICA improves the correlation substantially (above $0.95$) where the
sources are non-Gaussian and the mixing is close to linear, but degrades where the
curvature dominates, because its transformation model is linear. The manifold
method — or the explicit linearising feature — recovers the parameter *along* the
curve with the highest correlation of the three, which is the point: on a curved
mixing relation the right transformation is the one that undoes the curvature, and
neither PCA nor ICA contains it.
