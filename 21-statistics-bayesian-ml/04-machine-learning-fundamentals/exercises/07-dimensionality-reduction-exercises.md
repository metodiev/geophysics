# Exercises — 21-04-07 PCA, ICA and Manifold Learning

Attempt these before reading the
[solutions](./07-dimensionality-reduction-solutions.md). The lesson is
[07 Dimensionality Reduction](../07-dimensionality-reduction.md). All data are
**SYNTHETIC**.

## ★ Foundational

**★1.** A data set gives singular values $61.036$ and $9.890$. Compute the
explained fractions and state the reconstruction MSE for one component using
$\sum_{j>k}\sigma_j^{2}/(n-1)$ with $n = 400$.

**★2.** Source kurtoses are $-0.1155$ and $+2.4024$; PCA components give
$+1.4293$ and $+0.0019$; ICA components give $+2.4210$ and $-0.1135$. State which
method recovered the sources and by what numerical evidence.

**★3.** A one-component PCA on a parabola gives a reconstruction MSE of
$0.043851$, of which $0.0001$ is injected noise. Compute the fraction attributable
to curvature.

## ★★ Applied

**★★4.** Derive PCA from the SVD of the centred data matrix and show that the rank-
$k$ reconstruction error equals the sum of the discarded singular values squared.

**★★5.** Explain why two independent non-Gaussian sources become more Gaussian when
mixed, and how that fact is used by an ICA algorithm.

**★★6.** Give the correlation of each method with the true sources
(PCA $0.8553$, ICA $0.9982$). Compute the ratio and state why PCA is not thereby a
failure.

## ★★★ Research-oriented

**★★★7.** Specify a study that measures PCA's explained variance and
reconstruction error when a fraction of the data are contaminated by outliers.
State the data, the contamination levels, the metric, the replicate count, and the
predicted degradation of the first component. A specification that could not be
executed is a failed answer.

**★★★8.** Design an experiment that compares PCA, ICA and a manifold method on a
stated Earth-data analogue (for example two mixed geochemical end-members on a
curved mixing line), with an explicit external criterion for success.
