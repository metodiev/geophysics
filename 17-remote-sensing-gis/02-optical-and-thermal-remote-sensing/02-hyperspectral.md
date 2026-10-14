---
id: 17-02-02
title: "Hyperspectral Sensing and Spectral Unmixing"
level: doctoral
prereqs: ["17-02-01", "18-03-02"]
tags: [remote-sensing, gis, hyperspectral, spectral-unmixing, linear-mixture, simplex]
---

# Hyperspectral Sensing and Spectral Unmixing

A hyperspectral sensor measures reflectance in many narrow, contiguous bands. The
scientific promise is that materials can be identified by their diagnostic
absorption features, and the practical reality is that **almost every pixel is a
mixture**: the ground resolution element of a hyperspectral instrument is
typically metres to tens of metres, so a single measurement contains several
materials. Spectral unmixing is the inversion that recovers the fractions.

This lesson develops the **linear mixing model**

$$\mathbf{x} = \mathbf{M}\mathbf{a} + \mathbf{n},
\qquad \mathbf{M} = [\mathbf{e}_1 \cdots \mathbf{e}_p],$$

and then does something more useful than presenting the least-squares solution:
it solves the same synthetic scene three ways and measures the consequences.

- **Unconstrained** least squares gives the smallest residual and *unphysical*
  abundances: the demonstration recovers negative fractions in $9$ of $400$
  pixels ($2.2\%$), the most negative being $-0.0253$, and abundance sums
  spanning $0.9712$–$1.0271$ where the physics requires exactly $1$.
- **Sum-to-one** constrained least squares fixes the sum exactly and nothing
  else: the most negative abundance is still $-0.0158$.
- **Fully constrained** (non-negative and sum-to-one) least squares is
  physically admissible, and it *biases* abundances at the boundary: $8$ of the
  $2000$ recovered fractions sit exactly at zero, because the simplex projection
  pushes small true fractions to the edge.

The honesty point of the lesson is the last one. A small reconstruction residual
does **not** validate the physics. The demonstration's three solvers all
reconstruct the data to RMSE $\approx 0.0019$, below the $0.002$ band noise, while
a $5\%$ error in one endmember's *shape* biases the abundances by up to
$-0.047$ and raises the abundance RMSE to $0.03214$ — a factor $2.4$ above the
noise-only level and, crucially, **one-sided**. The residual cannot see the
error, because the error is in the model, not in the fit.

All models and data in this module are **SYNTHETIC**. The five endmembers are
smooth teaching spectra built in `code/hyperspectral_demo.py` from logistic and
Gaussian terms; the abundances are drawn from a Dirichlet distribution with a
chosen concentration; and the noise level, band grid and library perturbations are
parameters of that file. No real material, sensor or mission is represented.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the linear mixing model from area-weighted radiance and **state**
   the conditions under which it holds.
2. **Solve** the unconstrained least-squares unmixing problem and **compute** the
   abundance covariance matrix.
3. **Derive** the closed-form sum-to-one constrained solution by endmember
   reduction, and **explain** what it does and does not fix.
4. **Explain** why non-negativity requires an iterative (active-set) solver, and
   **quantify** the boundary bias it introduces.
5. **Interpret** the condition number of the endmember Gram matrix, and
   **quantify** the abundance-noise inflation of a nearly collinear library.
6. **Establish** the intrinsic dimensionality of a scene from the endmember rank
   and the data eigenvalues, and **state** what a principal-component rotation does
   and does not provide.
7. **Quantify** endmember variability as a model error, and **explain** why it is
   invisible in the residual.

## Prerequisites

- [17-02-01 Multispectral Imaging, Band Ratios and Indices](01-multispectral-imaging.md)
  — the reflectance quantities being mixed and the projection idea.
- [18-03-02 Tikhonov Regularisation and the Smoothing Trade-Off](../../18-inverse-problems/03-regularization/02-tikhonov.md)
  — the general treatment of an ill-conditioned inversion and the bias it buys.

---

## 1. Intuition: a pixel is an area, and an area is a sum

Consider a pixel that is $70\%$ soil, $20\%$ vegetation and $10$% water. If the
materials are physically separate at the scale of the resolution element, the
radiance leaving the pixel is the *area-weighted sum* of the radiances each
material would produce alone, because radiance from disjoint areas adds. That is
the whole content of the linear mixing model, and the assumption it needs is
exactly that: **the materials are arranged in separate patches large enough for
each to be described by its own single-scattering reflectance, with no significant
interaction.**

Interaction is where linearity fails: multiple scattering between adjacent
materials, transmittance through a canopy onto soil, and shadowing all violate it.
The lesson proceeds with the linear model because it is the standard first-order
description and because every failure mode of the constrained inversion can be
demonstrated inside it. Nonlinear mixing is discussed in Section 5.8 but not
solved here.

The geometry is worth holding in mind: with $p$ endmembers the admissible
abundances lie on the **probability simplex** $\{a_i \ge 0,\ \sum_i a_i = 1\}$, a
flat triangular (or higher) region. Unconstrained least squares projects the
measurement onto the whole $p$-dimensional plane spanned by the endmembers and
therefore lands outside the simplex whenever the data are noisy. Constrained
unmixing projects onto the simplex. The different answers in the demonstration are
the difference between those two projections.

## 2. Precise definitions and units

| Quantity | Symbol | Shape | Unit |
|---|---|---|---|
| pixel spectrum | $\mathbf{x}$ | $m$ | reflectance (dimensionless) |
| endmember library | $\mathbf{M}$ | $m\times p$ | reflectance columns |
| endmember $j$ | $\mathbf{e}_j$ | $m$ | reflectance |
| abundance vector | $\mathbf{a}$ | $p$ | dimensionless, on the simplex |
| noise | $\mathbf{n}$ | $m$ | reflectance |
| Gram matrix | $\mathbf{G} = \mathbf{M}^{\!\top}\mathbf{M}$ | $p\times p$ | reflectance² |
| condition number | $\kappa(\mathbf{G})$ | — | dimensionless |
| reconstruction residual | $\|\mathbf{M}\mathbf{a}-\mathbf{x}\|$ | — | reflectance |

Here $m$ is the number of bands ($60$ in the demonstration) and $p$ the number of
endmembers ($5$). The system is **overdetermined in bands** ($m \gg p$) and
**underdetermined in abundance** unless the constraints are imposed — the simplex
has $p-1$ degrees of freedom, and without it the inversion has $p$.

## 3. Derivations

### 3.1 The linear mixing model

Let the pixel have area $A$ partitioned into $p$ materials with areas $A_j$, and
let material $j$ have a reflectance spectrum $\mathbf{e}_j(\lambda)$ as measured
over an area much larger than the photon mean free path. Because radiance from
disjoint areas is additive and the sensor integrates over the pixel,

$$\mathbf{x} = \sum_{j=1}^{p}\frac{A_j}{A}\,\mathbf{e}_j
= \sum_{j=1}^{p} a_j \mathbf{e}_j,
\qquad a_j = \frac{A_j}{A} \ge 0, \quad \sum_j a_j = 1 .$$

In matrix form $\mathbf{x} = \mathbf{M}\mathbf{a}$, with $\mathbf{M}$ assembled
from the endmember columns. Adding sensor noise and any model error $\mathbf{n}$:

$$\boxed{\;\mathbf{x} = \mathbf{M}\mathbf{a} + \mathbf{n}\;.}$$

### 3.2 Unconstrained least squares

Minimise $J(\mathbf{a}) = \|\mathbf{M}\mathbf{a}-\mathbf{x}\|^{2}$. Setting
$\partial J/\partial \mathbf{a} = 0$ gives the normal equations

$$\mathbf{M}^{\!\top}\mathbf{M}\,\hat{\mathbf{a}} = \mathbf{M}^{\!\top}\mathbf{x}
\;\Longrightarrow\;
\boxed{\;\hat{\mathbf{a}} = \left(\mathbf{M}^{\!\top}\mathbf{M}\right)^{-1}
\mathbf{M}^{\!\top}\mathbf{x} = \mathbf{G}^{-1}\mathbf{M}^{\!\top}\mathbf{x}\;.}$$

For $\mathbf{n}\sim\mathcal{N}(\mathbf{0},\sigma^{2}\mathbf{I})$ the estimator is
unbiased with covariance

$$\operatorname{cov}(\hat{\mathbf{a}}) = \sigma^{2}\left(\mathbf{M}^{\!\top}
\mathbf{M}\right)^{-1} = \sigma^{2}\mathbf{G}^{-1},$$

so the abundance standard deviations are
$\sigma\sqrt{\operatorname{diag}(\mathbf{G}^{-1})}$.

*Numerical check.* In the demonstration, $\sigma = 0.001$ gives Monte Carlo
abundance standard deviations of $0.00117$ (vegetation-like) and $0.00885$
(carbonate-like) against predictions $0.00120$ and $0.00884$. So

$$\sqrt{\operatorname{diag}(\mathbf{G}^{-1})} = 1.20\ \text{and}\ 8.84
\qquad\Longrightarrow\qquad
\sigma_{a,\text{carbonate}} = 7.4\,\sigma_{a,\text{vegetation}}$$

**with identical band noise in both cases.** The library, not the sensor, sets
which abundances are precise.

### 3.3 The sum-to-one constraint, in closed form

Eliminate one abundance using $\sum_j a_j = 1$, i.e. $a_p = 1 - \sum_{j<p}a_j$:

$$\mathbf{x} = \sum_{j<p}a_j\mathbf{e}_j + \left(1-\sum_{j<p}a_j\right)\mathbf{e}_p
= \mathbf{e}_p + \sum_{j<p}a_j\left(\mathbf{e}_j-\mathbf{e}_p\right).$$

Therefore

$$\mathbf{x} - \mathbf{e}_p = \mathbf{M}_{\rm red}\mathbf{a}_{\rm red},
\qquad \mathbf{M}_{\rm red} = \left[\mathbf{e}_1-\mathbf{e}_p,\ \dots,\
\mathbf{e}_{p-1}-\mathbf{e}_p\right],$$

and the reduced problem is again a least-squares problem with $p-1$ unknowns:

$$\hat{\mathbf{a}}_{\rm red} = \left(\mathbf{M}_{\rm red}^{\!\top}
\mathbf{M}_{\rm red}\right)^{-1}\mathbf{M}_{\rm red}^{\!\top}
\left(\mathbf{x}-\mathbf{e}_p\right),\qquad
\hat{a}_p = 1 - \sum_{j<p}\hat{a}_j .$$

*Numerical check.* The demonstration's row sums are $1.000000$ to six decimals,
exactly as constructed, while the most negative abundance is $-0.0158$: **the
constraint removed the sum error and left the sign error** (the unconstrained
most-negative value was $-0.0253$). Fixing one algebraic property of the answer
does not make the answer physical.

### 3.4 Non-negativity and the boundary bias

The fully constrained problem

$$\min_{\mathbf{a}}\ \|\mathbf{M}\mathbf{a}-\mathbf{x}\|^{2}
\quad\text{subject to}\quad \mathbf{a}\ge \mathbf{0},\ \ \mathbf{1}^{\!\top}
\mathbf{a}=1$$

has no closed-form solution: the active set (which abundances are at zero) is
unknown in advance and must be found iteratively. The standard route augments the
library with a heavily weighted row enforcing the sum and applies
non-negative least squares (Lawson–Hanson), which solves the inequality-constrained
problem exactly for each active set and updates the set until the KKT conditions
hold.

The price is **bias**. The solution is the metric projection of the unconstrained
answer onto the simplex, and a projection onto a boundary is one-sided: an
abundance whose true value is small is pushed to exactly zero, and the deficit is
redistributed to the others. In the demonstration, $8$ of $2000$ entries are
exactly zero at $\sigma = 0.002$; at higher noise the fraction becomes
substantial. Consequences:

- the **mean** abundance of a rare material is biased **low**, and the bias grows
  with noise;
- the abundance RMSE of the constrained answer is not necessarily smaller than the
  unconstrained one — in the demonstration $0.01046$ (FCLS) against $0.01320$
  (unconstrained), an improvement here, but the improvement is in the *physical
  admissibility*, not guaranteed in a least-squares sense;
- a map of "abundance $= 0$" must be read as "abundance below the detection
  limit", not as "absent".

### 3.5 Conditioning and identifiability

The abundance covariance is $\sigma^{2}\mathbf{G}^{-1}$, so its size is governed
by the smallest eigenvalues of $\mathbf{G}$. Writing the eigendecomposition
$\mathbf{G} = \sum_i\lambda_i\mathbf{v}_i\mathbf{v}_i^{\!\top}$ with
$\lambda_1 \ge \dots \ge \lambda_p$,

$$\mathbf{G}^{-1} = \sum_i \frac{1}{\lambda_i}\mathbf{v}_i\mathbf{v}_i^{\!\top},
\qquad
\kappa(\mathbf{G}) = \frac{\lambda_1}{\lambda_p}
= \kappa(\mathbf{M})^{2}.$$

Noise along the eigenvector of the smallest eigenvalue is amplified by
$1/\sqrt{\lambda_p}$; if $\lambda_p$ is small compared with the noise, that
direction of abundance space is **not identifiable**.

*Numerical check.* The demonstration's library has $\kappa(\mathbf{G}) = 5328.5$
and $\kappa(\mathbf{M}) = 73.0$ — note the square relation
($73.0^{2} = 5329$). Appending a sixth endmember that is $99\%$ carbonate-like and
$1\%$ clay-like raises $\kappa(\mathbf{G})$ to $6.7\times10^{16}$, a factor
$1.3\times10^{13}$: the new direction is numerically null, and the abundance RMSE
rises from $0.01320$ to $0.05484$. **Adding an endmember to a library increases
the possible descriptions without increasing the information available to
distinguish them.**

### 3.6 Dimensionality

The mixed data lie in the column space of $\mathbf{M}$, whose dimension is at
most $p$. In the demonstration the data covariance eigenvalues are

| component | eigenvalue | share | cumulative |
|---|---|---|---|
| 1 | 0.12890 | 90.653% | 90.653% |
| 2 | 0.01235 | 8.686% | 99.339% |
| 3 | 0.00071 | 0.498% | 99.837% |
| 4 | 0.00023 | 0.163% | 100.000% |
| 5 | $\sim10^{-19}$ (numerical zero) | 0.000% | 100.000% |

with $\operatorname{rank}(\mathbf{M}) = 5$ of $5$. So a scene with $60$ bands has
only $5$ significant dimensions. A principal-component rotation finds those
dimensions; it does **not** label them, and its components are linear combinations
of endmembers, not materials. Interpretability must be supplied by the physics
(the simplex, the features, an external library), not by the rotation.

### 3.7 Endmember variability as model error

Real endmembers vary within a scene: the same nominal mineral has different
grain sizes, the same vegetation has different leaf water content. Model this by
writing the true library as $\mathbf{M}_{\rm t} = \mathbf{M} + \Delta$ while the
analyst inverts with $\mathbf{M}$. Then

$$\hat{\mathbf{a}} = \mathbf{G}^{-1}\mathbf{M}^{\!\top}
\left(\mathbf{M}_{\rm t}\mathbf{a}_{\rm t} + \mathbf{n}\right)
= \mathbf{a}_{\rm t} + \mathbf{G}^{-1}\mathbf{M}^{\!\top}
\Delta\mathbf{a}_{\rm t} + \mathbf{G}^{-1}\mathbf{M}^{\!\top}\mathbf{n},$$

so the estimator is **biased** by
$\mathbf{b} = \mathbf{G}^{-1}\mathbf{M}^{\!\top}\Delta\mathbf{a}_{\rm t}$, a term
proportional to the perturbation and to the true abundances. The bias is not
reduced by more bands, better radiometry or averaging pixels: it is a systematic
error in the model.

*Numerical check.* Perturbing the vegetation-like endmember by a $5\%$
sinusoidal shape change gives

| endmember | mean bias | RMSE |
|---|---|---|
| vegetation-like | $-0.0210$ | 0.0254 |
| bright-soil-like | $+0.0109$ | 0.0226 |
| water-like | $-0.0469$ | 0.0567 |
| carbonate-like | $+0.0135$ | 0.0239 |
| clay-like | $+0.0060$ | 0.0149 |

overall RMSE $0.03214$ against $0.01320$ from measurement noise alone. Note the
*sign structure*: perturbing one endmember biases *all* of them, in both
directions, because the abundances must still sum to one.

## 4. Physical interpretation

- **The model is a projection.** Unconstrained, constrained and fully constrained
  solutions differ by which set they project onto; the choice is physical
  modelling, not numerical preference.
- **The Gram matrix is the whole story for precision.** $\sigma^{2}\mathbf{G}^{-1}$
  says that the *endmember library*, not the sensor, decides which fractions are
  measurable. The demonstration's carbonate-like abundance is $7.4\times$ noisier
  than the vegetation-like one at the same band noise.
- **Constraints buy admissibility and cost bias.** FCLS is the right answer to
  "what is physically admissible", not to "what is the minimum-variance
  estimate".
- **A small residual is not a validation.** All three solvers reach
  $\approx0.0019$, while a $5\%$ endmember shape error biases abundances by up to
  $-0.047$.
- **Nonlinearity is not a detail.** Multiple scattering between materials breaks
  the area-weighted argument. It is the dominant error in vegetation and in
  rough, high-albedo surfaces.

## 5. Assumptions and regime of validity

1. **Area-additive radiance** — the materials are spatially disjoint at the
   resolution scale, with no multiple scattering between them. Violated by
   canopies, mixtures of bright and dark grains, and thin coatings.
2. **A single, correct endmember library** — the same spectrum applies to every
   pixel where the material occurs. Section 3.7 quantifies the consequence.
3. **Additive, zero-mean, Gaussian band noise** with known or estimable $\sigma$.
   Correlated noise (striping) makes $\sigma^{2}\mathbf{I}$ wrong and the
   covariance expression optimistic.
4. **Band-independent reflectance**, i.e. no spectral convolution effects beyond
   the band response. A band response wider than the feature it is meant to
   resolve destroys the diagnostic (see
   [17-01-04](../01-remote-sensing-physics/04-resolution-concepts.md)).
5. **Atmospherically corrected input.** Unmixing top-of-atmosphere reflectance
   mixes an atmospheric endmember into every abundance
   ([17-01-03](../01-remote-sensing-physics/03-atmospheric-effects.md)).
6. **The number of endmembers is known.** Choosing $p$ is itself an inverse
   problem; Section 3.6 is the diagnostic, and Section 3.5 is the penalty for
   choosing too large.
7. **The synthetic parameters are teaching values**, as stated above: the
   endmembers, noise, Dirichlet concentration and perturbation are parameters of
   the demonstration, and the numbers in this lesson are that demonstration's
   output.

## 6. Units and dimensional analysis

| Expression | Unit arithmetic | Result |
|---|---|---|
| $\mathbf{x} = \mathbf{M}\mathbf{a}$ | reflectance = reflectance × dimensionless | reflectance |
| $\mathbf{M}^{\!\top}\mathbf{M}$ | reflectance² | reflectance² |
| $\mathbf{G}^{-1}\mathbf{M}^{\!\top}\mathbf{x}$ | (reflectance⁻²)(reflectance)(reflectance) | dimensionless |
| $\sigma^{2}\mathbf{G}^{-1}$ | reflectance² / reflectance² | dimensionless (variance of a fraction) |
| $\sum_j a_j$ | dimensionless | $=1$ on the simplex |
| $\kappa(\mathbf{G})$ | reflectance²/reflectance² | dimensionless |

The dimensions are forgiving here — everything is a reflectance ratio — which is
exactly why a dimensional error is easy to miss: an inversion using radiances
instead of reflectances gives the same *shape* of answer and a different
normalisation. The abundances are only comparable to area fractions if
$\mathbf{x}$ and $\mathbf{M}$ are both reflectance.

## 7. Worked examples

### Example 1 — the closed-form unconstrained answer

Take the smallest non-trivial case: $m = 2$ bands, $p = 2$ endmembers,
$\mathbf{e}_1 = (0.10, 0.30)^{\!\top}$, $\mathbf{e}_2 = (0.40, 0.50)^{\!\top}$,
and a measured pixel $\mathbf{x} = (0.28, 0.42)^{\!\top}$.

$$\mathbf{M} = \begin{pmatrix}0.10 & 0.40\\ 0.30 & 0.50\end{pmatrix},
\qquad
\mathbf{G} = \mathbf{M}^{\!\top}\mathbf{M} =
\begin{pmatrix}0.100 & 0.190\\ 0.190 & 0.410\end{pmatrix},$$
$$\det\mathbf{G} = 0.100\times0.410 - 0.190^{2} = 0.0410 - 0.0361 = 0.0049,$$
$$\mathbf{G}^{-1} = \frac{1}{0.0049}\begin{pmatrix}0.410 & -0.190\\
-0.190 & 0.100\end{pmatrix}
= \begin{pmatrix}83.67 & -38.78\\ -38.78 & 20.41\end{pmatrix},$$
$$\mathbf{M}^{\!\top}\mathbf{x} = (0.10\times0.28+0.30\times0.42,\
0.40\times0.28+0.50\times0.42)^{\!\top} = (0.154,\ 0.322)^{\!\top},$$
$$\hat{\mathbf{a}} = \mathbf{G}^{-1}\mathbf{M}^{\!\top}\mathbf{x}
= (83.67\times0.154 - 38.78\times0.322,\
-38.78\times0.154 + 20.41\times0.322)^{\!\top}
= (0.396,\ 0.600)^{\!\top}.$$

The sum is $0.996$, against the exact $1$ of the noise-free construction; with
noise it need not be. Note that $\mathbf{G}$ has eigenvalues $0.5002$ and
$0.009796$, so $\kappa(\mathbf{G}) = 51.06$ for this deliberately near-collinear
pair — nearly two orders of magnitude worse conditioned than an orthogonal
library, and already enough to matter.

### Example 2 — the sum-to-one solution, same data

$$\mathbf{M}_{\rm red} = \mathbf{e}_1 - \mathbf{e}_2 = (-0.30,\ -0.20)^{\!\top},
\qquad
\mathbf{x} - \mathbf{e}_2 = (-0.12,\ -0.08)^{\!\top}.$$

$$\hat{a}_1 = \frac{\mathbf{M}_{\rm red}^{\!\top}(\mathbf{x}-\mathbf{e}_2)}
{\mathbf{M}_{\rm red}^{\!\top}\mathbf{M}_{\rm red}}
= \frac{0.036+0.016}{0.09+0.04} = \frac{0.052}{0.130} = 0.400,$$
$$\hat{a}_2 = 1 - 0.400 = 0.600 .$$

The exact answer by construction was $a = (0.40, 0.60)$, and the reduced solve
recovers it to three decimals. The two examples agree here because the data are
barely noisy; with more noise they diverge by exactly the amount the sum
constraint redistributes.

### Example 3 — which abundance is measurable?

From the demonstration's noise table, at $\sigma = 0.002$:
$\operatorname{sd}(\hat{a}_{\rm veg}) = 0.00251$ (predicted $0.00239$) and
$\operatorname{sd}(\hat{a}_{\rm carbonate}) = 0.01693$ (predicted $0.01767$).

1. Both scale linearly in $\sigma$: at $\sigma = 0.010$ they are $0.01262$ and
   $0.08890$.
2. Their ratio, $6.7$–$7.4$, is a property of the library alone.
3. Consequence: a map of carbonate-like abundance needs $7\times$ more averaging
   (hence $7^{2} = 49\times$ the pixels, since $\sigma$ falls as $1/\sqrt{n}$) to
   reach the same precision as a map of vegetation-like abundance.

### Example 4 — the bias from a $5\%$ endmember error

Perturbing the vegetation-like endmember's shape by $5\%$ gives a vegetation-like
abundance bias of $-0.0210$ and a water-like bias of $-0.0469$.

1. The water-like bias is *larger* than the vegetation-like one even though the
   perturbed endmember was vegetation-like, because the simplex redistribution
   pushes the correction into the abundances that are already small.
2. The bias term $\mathbf{G}^{-1}\mathbf{M}^{\!\top}\Delta\mathbf{a}_{\rm t}$
   contains no noise, so improving radiometry, integration time or averaging does
   not reduce it. Adding bands helps only if the new bands constrain the
   perturbed *direction*; bands that duplicate existing information leave it
   untouched.
3. The only remedies are a better library (more endmembers covering the
   variability, or a spectral library matched to the scene) or a model that
   admits endmember variation explicitly — a multiple-endmember or Bayesian
   formulation.

## 8. Python demonstration

`code/hyperspectral_demo.py` prints, with units:

1. the five synthetic endmembers, $60$ bands from $0.40$ to $2.50\ \mathrm{\mu m}$
   (sampling $0.0356\ \mathrm{\mu m}$), with their feature centres;
2. a $400$-pixel Dirichlet scene with per-endmember abundance statistics;
3. the unconstrained solution: $2.2\%$ negative abundances, minimum $-0.0253$,
   sums $0.9712$–$1.0271$, RMSE $0.01320$;
4. the sum-to-one closed form: sums $1.000000$, minimum $-0.0158$, RMSE $0.01056$;
5. the FCLS solution: sums $1.000000$, minimum $0$, RMSE $0.01046$, $8$ boundary
   zeros;
6. conditioning: $\kappa(\mathbf{G}) = 5328.5$, $\kappa(\mathbf{M}) = 73.0$, and
   $6.7\times10^{16}$ with the near-duplicate endmember (RMSE $0.05484$);
7. the noise-propagation table, Monte Carlo against $\sigma\sqrt{\operatorname{diag}(\mathbf{G}^{-1})}$;
8. the data eigenvalue spectrum ($90.653\%$, $99.339\%$, $99.837\%$, $100.000\%$);
9. the endmember-variability bias table (RMSE $0.03214$ against $0.01320$);
10. reconstruction residuals for all three solvers ($0.001898$, $0.001914$,
    $0.001914$).

Everything is generated in code; there is no file input and no network access.

## 9. Exercises

Full sets with worked solutions are in
[`exercises/02-hyperspectral-exercises.md`](./exercises/02-hyperspectral-exercises.md)
and
[`exercises/02-hyperspectral-solutions.md`](./exercises/02-hyperspectral-solutions.md).

- **★** Unmix $\mathbf{x} = (0.25, 0.40)^{\!\top}$ with the Example-1 library and
  report whether the answer is admissible.
- **★** Verify $\kappa(\mathbf{G}) = \kappa(\mathbf{M})^{2}$ numerically for the
  Example-1 library.
- **★★** Derive the sum-to-one solution for a three-endmember library and check
  that the abundance sum is exactly one.
- **★★** Compute the abundance standard deviations for the Example-1 library at
  $\sigma = 0.005$ and state which fraction is measurable.
- **★★★** Show that a nearly collinear endmember pair cannot be separated,
  parametrise the null direction, and state the diagnostic you would report.

## Mastery checkpoint

Without notes: endmembers $\mathbf{e}_1 = (0.10, 0.30)$,
$\mathbf{e}_2 = (0.40, 0.50)$, pixel $\mathbf{x} = (0.26, 0.40)$. **(a)** Unmix
$\mathbf{x}$ unconstrained. **(b)** State whether the answer is admissible and
why. **(c)** Solve the sum-to-one constrained version. **(d)** Compute
$\kappa(\mathbf{G})$ and state which fraction is noisier.

## 10. Common pitfalls

1. **Reporting unconstrained abundances as cover fractions.** $2.2\%$ of pixels
   go negative here; the value is a diagnostic, not a fraction.
2. **Believing the sum constraint makes the answer physical.** The most negative
   abundance after the sum constraint is $-0.0158$.
3. **Reading FCLS zeros as absence.** They are detections below the limit, with a
   one-sided bias.
4. **Adding endmembers for completeness.** The near-duplicate raises the condition
   number by $1.3\times10^{13}$ and the abundance RMSE from $0.01320$ to
   $0.05484$.
5. **Validating with the reconstruction residual.** All three solvers pass, while
   a $5\%$ library error biases abundances by $0.047$.
6. **Treating principal components as materials.** They are rotations, not
   endmembers.
7. **Ignoring the conditioning of the library.** Precision varies $7.4\times$
   between fractions at identical band noise.

## 11. Real-world applications

- **Mineral abundance mapping.** Linear unmixing of alteration minerals is the
  classical hyperspectral application, extended in
  [06 Vegetation Indices, Geobotany and Mineral Alteration Mapping](06-vegetation-and-geobotany.md)
  and [17-08-01](../08-remote-sensing-applications-geophysics/01-mineral-mapping-rs.md).
- **Crop residue and cover fraction.** Fractional vegetation cover from unmixing
  is more interpretable than a single index, at the cost of requiring a library.
- **Sub-pixel detection.** A target whose fraction is below the detection limit
  can still be *detected* by a matched-filter test even though its abundance
  cannot be *estimated* — a distinction that follows directly from Section 3.5.
- **Cross-sensor fusion.** A library assembled from laboratory or field spectra
  must be resampled to the sensor's band responses, and the residual mismatch is
  an endmember error of the kind in Section 3.7.
- **Regularised and Bayesian alternatives.** For libraries that are nearly
  collinear by construction, the constrained problem is solved with additional
  regularisation or a prior; that is the subject of
  [18-03 Regularisation](../../18-inverse-problems/03-regularization/01-why-regularize.md)
  and [21-04-04 Regularisation: Ridge, Lasso, Early
  Stopping](../../21-statistics-bayesian-ml/04-machine-learning-fundamentals/04-regularization-ml.md).

## 12. Further reading

- *Remote Sensing and Image Interpretation* (Lillesand and Kiefer) — the applied
  unmixing workflow.
- *Physical Principles of Remote Sensing* (Rees) — the reflectance quantities and
  mixing regimes.
- [18-03-02 Tikhonov Regularisation and the Smoothing Trade-Off](../../18-inverse-problems/03-regularization/02-tikhonov.md)
  — regularisation, which is what a constrained solution implicitly is.
- [21-04-08 Clustering and Unsupervised Structure Discovery](../../21-statistics-bayesian-ml/04-machine-learning-fundamentals/08-clustering.md)
  — the unsupervised route to endmembers when no library exists.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.

## 13. Related modules

- [01 Multispectral Imaging, Band Ratios and Indices](01-multispectral-imaging.md) —
  the projection view of spectral analysis that unmixing generalises.
- [03 Thermal Infrared: Land Surface Temperature and Heat Flow](03-thermal-infrared.md) —
  the other regime, where the mixture is of emissions rather than reflectances.
- [04 Land Cover Classification: Supervised and Unsupervised](04-land-cover-classification.md) —
  the hard-assignment alternative to fractional cover.
- [06 Vegetation Indices, Geobotany and Mineral Alteration Mapping](06-vegetation-and-geobotany.md) —
  the mineral-mapping application of unmixing.

## 14. Self-assessment checklist

- [ ] I can derive the linear mixing model and state its central assumption.
- [ ] I can solve the unconstrained problem and write down the abundance covariance.
- [ ] I can derive the sum-to-one closed form by endmember reduction.
- [ ] I can explain the boundary bias of a simplex projection.
- [ ] I can interpret $\kappa(\mathbf{G})$ and predict which abundance is noisiest.
- [ ] I can establish the intrinsic dimensionality of a scene.
- [ ] I can explain why a small residual does not validate an unmixing result.
