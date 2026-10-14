# Solutions — 17-02-02 Hyperspectral Sensing and Spectral Unmixing

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> All libraries and spectra are **SYNTHETIC** teaching values.

Lesson: [02 Hyperspectral Sensing and Spectral Unmixing](../02-hyperspectral.md).

Example library: $\mathbf{e}_1 = (0.10, 0.30)$, $\mathbf{e}_2 = (0.40, 0.50)$;
$\mathbf{G} = \begin{pmatrix}0.100 & 0.190\\ 0.190 & 0.410\end{pmatrix}$,
$\det\mathbf{G} = 0.0049$,
$\mathbf{G}^{-1} = \begin{pmatrix}83.673 & -38.776\\ -38.776 & 20.408\end{pmatrix}$.

---

## ★1 — Unconstrained unmixing

$$\mathbf{M}^{\!\top}\mathbf{x} =
\begin{pmatrix}0.10\times0.25 + 0.30\times0.40\\
0.40\times0.25 + 0.50\times0.40\end{pmatrix}
= \begin{pmatrix}0.145\\ 0.300\end{pmatrix},$$

$$\hat{\mathbf{a}} = \mathbf{G}^{-1}\mathbf{M}^{\!\top}\mathbf{x}
= \begin{pmatrix}83.673\times0.145 - 38.776\times0.300\\
-38.776\times0.145 + 20.408\times0.300\end{pmatrix}
= \begin{pmatrix}12.133 - 11.633\\ -5.623 + 6.122\end{pmatrix}
= \begin{pmatrix}0.500\\ 0.499\end{pmatrix}.$$

Sum $= 0.999$. **Admissible:** both entries are non-negative and the sum is one to
three decimals. This pixel sits on the line segment between the two endmembers
exactly, which is why the unconstrained answer happens to be physical; the
demonstration shows that with $5$ endmembers and real noise, $2.2\%$ of pixels are
not.

---

## ★2 — Condition numbers

Eigenvalues of $\mathbf{G}$: solving $\lambda^{2} - 0.510\lambda + 0.0049 = 0$
gives $\lambda_{1,2} = (0.510 \pm \sqrt{0.2601-0.0196})/2
= (0.510\pm0.4904)/2$, i.e.

$$\lambda_1 = 0.5002,\qquad \lambda_2 = 0.009796,
\qquad
\kappa(\mathbf{G}) = \frac{0.5002}{0.009796} = 51.06.$$

For $\mathbf{M}$, $\kappa(\mathbf{M}) = \sqrt{\kappa(\mathbf{G})}$ because the
singular values of $\mathbf{M}$ are the square roots of the eigenvalues of
$\mathbf{G}$:

$$\kappa(\mathbf{M}) = \sqrt{51.06} = 7.146 .$$

Verification: the singular values of $\mathbf{M}$ are $\sqrt{0.5002} = 0.70725$
and $\sqrt{0.009796} = 0.09898$, whose ratio is $7.146$. ✔

---

## ★3 — The simplex

$$\mathcal{S} = \left\{\mathbf{a} : a_i \ge 0\ \forall i,\
\mathbf{1}^{\!\top}\mathbf{a} = 1\right\}.$$

The **equality** constraint can be enforced in closed form by eliminating one
abundance (Section 3.3 of the lesson). The **inequality** constraints cannot: which
entries sit at their bound is data-dependent, so the active set must be found
iteratively (Lawson–Hanson NNLS, or any quadratic-programming solver). A single
closed-form projection onto the simplex exists for the Euclidean metric, but it is
not the least-squares solution because the metric differs.

---

## ★4 — Sum-to-one solution for three endmembers

Reduce against the last endmember:

$$\mathbf{M}_{\rm red} = \left[\mathbf{e}_1-\mathbf{e}_3,\ \mathbf{e}_2-\mathbf{e}_3\right]
= \begin{pmatrix}-0.10 & 0.20\\ -0.10 & 0.10\\ -0.60 & -0.20\end{pmatrix},
\qquad
\mathbf{x}-\mathbf{e}_3 = \begin{pmatrix}0.07\\ 0.02\\ -0.28\end{pmatrix}.$$

$$\mathbf{M}_{\rm red}^{\!\top}\mathbf{M}_{\rm red}
= \begin{pmatrix}0.380 & 0.090\\ 0.090 & 0.090\end{pmatrix},
\qquad
\det = 0.0342-0.0081 = 0.0261,$$
$$\mathbf{M}_{\rm red}^{\!\top}\left(\mathbf{x}-\mathbf{e}_3\right)
= \begin{pmatrix}0.159\\ 0.072\end{pmatrix}.$$

Solving the $2\times2$ system:

$$\hat{a}_1 = \frac{0.090\times0.159 - 0.090\times0.072}{0.0261}
= \frac{0.01431-0.00648}{0.0261} = \frac{0.00783}{0.0261} = 0.300,$$
$$\hat{a}_2 = \frac{0.380\times0.072 - 0.090\times0.159}{0.0261}
= \frac{0.02736-0.01431}{0.0261} = \frac{0.01305}{0.0261} = 0.500,$$
$$\hat{a}_3 = 1 - 0.300 - 0.500 = 0.200 .$$

The exact construction was $\mathbf{a} = (0.30, 0.50, 0.20)$, so the reduce-and-solve
recovers it exactly, and the sum is $1$ by construction rather than by luck.
**Check:** $\mathbf{M}^{\!\top}\mathbf{x}$ reconstructed from the library gives
$\mathbf{x} = (0.27, 0.42, 0.52)$, matching the stated pixel.

---

## ★5 — Abundance precision

$$\sigma_{a_j} = \sigma\sqrt{\left(\mathbf{G}^{-1}\right)_{jj}}.$$

$$\sigma_{a_1} = 0.005\sqrt{83.673} = 0.005\times9.147 = 0.04574,$$
$$\sigma_{a_2} = 0.005\sqrt{20.408} = 0.005\times4.518 = 0.02259.$$

Endmember 1's fraction is $2.03\times$ **worse** even though both bands have the
same noise, because $\mathbf{e}_1$ is the darker and more "ordinary-looking"
direction of the library: the small eigenvalue of $\mathbf{G}$ is dominated by the
contrast between the two endmembers, and a dark endmember contributes little to
that contrast.

**Averaging requirement.** $\sigma$ falls as $1/\sqrt{n}$, so to reduce
$\sigma_{a_1}$ from $0.04574$ to $0.02259$ we need

$$\frac{n_{\rm new}}{n} = \left(\frac{0.04574}{0.02259}\right)^{2} = 4.10,$$

i.e. about $4.1\times$ as many pixels (for a spatially uniform target), or a
library with a better-conditioned contrast. Note also that both $\sigma$ values
exceed $0.02$: **at $\sigma_{\rm band} = 0.005$ this two-endmember pair does not
deliver fractions to better than a couple of per cent.**

---

## ★6 — The unconstrained abundance direction

The data constrain only the $\mathbf{G}$-weighted combination of abundances, and
the poorly determined direction is the eigenvector of the smallest eigenvalue. For
this library the endmembers are nearly collinear, so the trade is approximately

$$a_1 \to a_1 + t,\qquad a_2 \to a_2 - t
\qquad(\text{sum preserved}).$$

The induced change in the spectrum is

$$\Delta\mathbf{x} = t\left(\mathbf{e}_1-\mathbf{e}_2\right)
= t\begin{pmatrix}-0.30\\ -0.20\end{pmatrix},
\qquad
\|\Delta\mathbf{x}\| = |t|\times0.3606 .$$

For $t = 0.10$: $\Delta\mathbf{x} = (-0.030, -0.020)$, so each band changes by
$0.030$ and $0.020$ — respectively $15\times$ and $10\times$ the band noise
$\sigma = 0.002$. **So a $0.10$ abundance trade is easily detectable here.** The
direction that is *hard* is not this one but the smallest-eigenvalue direction of
$\mathbf{G}$, and its uncertainty is obtained from the quadratric form of the
covariance. For the trade $a_1-a_2$,

$$\operatorname{var}\left(\hat{a}_1-\hat{a}_2\right)
= \sigma^{2}\,[1,-1]\,\mathbf{G}^{-1}\,[1,-1]^{\!\top}
= \sigma^{2}\left(83.673+20.408+2\times38.776\right)
= \sigma^{2}\times181.63,$$

so $\operatorname{sd}(\hat{a}_1-\hat{a}_2) = 0.002\times13.477 = 0.0270$: a trade
of $\pm0.027$ is a $1\sigma$ effect despite producing a spectral change of
$0.0097$ — about $5\times$ the band noise. **The lesson's general rule is therefore
to report $\kappa(\mathbf{G})$ together with the smallest eigenvector and the noise
level**, since the direction that is difficult to determine is a *specific* linear
combination, and it is not the same as the visually obvious trade between two
adjacent endmembers.

For the 5-endmember demonstration library, $\lambda_{\min} = 5.529\times10^{-3}$,
so the worst direction has
$\sigma_t = \sigma/\sqrt{\lambda_{\min}} = 0.002/0.07436 = 0.0269$ — an
unidentifiable trade of $\pm0.027$ at those noise levels, the same order as the
two-endmember case above.

---

## ★7 — Why more endmembers can be worse

**Explanation.** The sixth endmember is a linear combination of two existing
members, so its column adds no new direction to the column space of $\mathbf{M}$;
it only *rotates* the basis toward collinearity. The Gram matrix then has an
eigenvalue at the level of the perturbation (numerically $6.7\times10^{16}$
condition number), and the abundance covariance $\sigma^{2}\mathbf{G}^{-1}$ carries
a factor $1/\lambda_{\min}$ that is astronomically large along that direction. The
fit can improve (a more flexible model always fits at least as well), while the
abundances become meaningless.

**Diagnostic to report.** $\kappa(\mathbf{G})$, together with the library's
singular values and the smallest eigenvector's composition (which endmembers it
mixes). A model-selection criterion that penalises description length — the
abundance covariance, Akaike/Bayesian information criteria, or cross-validated
abundance RMSE — is the quantitative decision rule. The demonstration's numbers
are the worked example: abundance RMSE $0.01320$ with $5$ endmembers against
$0.05484$ with $6$.

---

## ★8 — Designing a boundary-bias experiment

**Metric.** Let the true abundance be $a_{\rm true} = 0.02$ for one endmember in
a scene where the other abundances are well separated from their bounds. Define

$$B(\sigma) = \left\langle \hat{a}_{\rm FCLS} - a_{\rm true}\right\rangle_{\rm pixels}
\quad\text{and}\quad
S(\sigma) = \operatorname{sd}\left(\hat{a}_{\rm FCLS}\right)_{\rm pixels},$$

averaged over at least $10^{4}$ synthetic pixels with fresh noise realisations at
each $\sigma$, using the *same* true abundances so that $B$ is not contaminated by
the spread of true values.

**Prediction.** $B(\sigma) < 0$ and grows in magnitude with $\sigma$ (the fraction
of pixels whose unconstrained estimate falls below zero rises). $S(\sigma)$ grows
linearly in $\sigma$ until the projection saturates it, and then more slowly,
because the boundary truncates the distribution. Hence the **relative** bias
$B/a_{\rm true}$ becomes large (order unity) for a modest $\sigma$. Compare with
the unconstrained estimator, whose bias is zero by construction and whose RMSE is
$\sigma\sqrt{(\mathbf{G}^{-1})_{jj}}$.

**The false conclusion to avoid.** Comparing only RMSE would conclude "FCLS is
better" whenever its RMSE is smaller, which it often is — but a smaller RMSE with
a one-sided bias means the map systematically under-reports the material, which is
exactly the wrong error for a resource or hazard application. Report $B$ and $S$
separately, and report the fraction of pixels at the boundary, which is the
diagnostic that reveals the mechanism.

---

## ★9 — A multiple-endmember formulation for ±8% variability

**Algebra.** Replace one endmember column by a set of $k$ variant spectra
$\{\mathbf{e}_j^{(1)},\dots,\mathbf{e}_j^{(k)}\}$ generated by perturbing the shape
within the stated $\pm8\%$ (deterministically, e.g. by scaling the absorption
depth, or by sampling a library of measured variants). Solve the **grouped**
non-negative least-squares problem

$$\min_{\mathbf{a}\ge0}\ \left\|\mathbf{x} -
\sum_{j'\ne j}a_{j'}\mathbf{e}_{j'} -
\sum_{m=1}^{k}a_j^{(m)}\mathbf{e}_j^{(m)}\right\|^{2}
\quad\text{subject to}\quad \sum_{j'\ne j}a_{j'} +
\sum_{m=1}^{k}a_j^{(m)} = 1,$$

that is, the abundance of the mineral is the **sum** of its variants' weights.
With $k=1$ this reduces to the standard model; the change is that the library gains
$k-1$ extra columns confined to a known shape family, so the inversion absorbs the
variability into a distribution of variant weights instead of into a bias on the
other endmembers. Solver: the same NNLS on the row-augmented system, or a
lightweight projected-gradient method; the problem stays convex, so there is a
unique optimum.

**Validation without ground truth.** Use three in-scene, self-consistent tests:
(i) **hold-out bands** — fit on a subset of bands and predict the withheld ones;
the multiple-endmember model should reduce the hold-out residual without
increasing $\kappa$ past a stated threshold; (ii) **spatial coherence** — the
variant weights should vary smoothly across the scene if the variability is
physical (grain size, moisture), and noisily if it is fitting noise; (iii)
**simplex plausibility** — the *summed* mineral abundance should be less
boundary-biased than the single-endmember version at the same noise, and the
fraction of boundary pixels should fall.

**Residual diagnostic that separates variability from processing error.** Fit the
residual spectrum $\mathbf{r} = \mathbf{x} - \mathbf{M}\hat{\mathbf{a}}$ and ask
whether it (a) lies along the span of the endmember variants, (b) is spectrally
structured at absorption features, or (c) is broadband and correlated with
illumination, geometry or band index. Case (a) is endmember variability, and the
multiple-endmember model should remove it. Case (b) indicates a *missing* material
in the library. Case (c) is a residual atmospheric or calibration error
(common-mode across the scene, or striped in the cross-track direction), and
adding endmembers will merely launder it into abundance. **Report the map of
$\mathbf{r}$ alongside the abundances**; an unmixing result without its residual
map cannot be diagnosed.
