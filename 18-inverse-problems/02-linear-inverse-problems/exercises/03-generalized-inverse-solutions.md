# Solutions — 18-02-03 The Generalised (Moore-Penrose) Inverse

> **Read after attempting the exercises.** Lesson:
> [03 The Generalised Inverse](../03-generalized-inverse.md).

---

## ★1 — The four conditions

1. $GG^{+}G = G$ — $G^{+}$ is a *generalised* inverse: it undoes $G$ on the range.
2. $G^{+}GG^{+} = G^{+}$ — the same statement the other way round.
3. $(GG^{+})^{\!\top} = GG^{+}$ — the data-side projection is **orthogonal**.
4. $(G^{+}G)^{\!\top} = G^{+}G$ — the model-side projection is **orthogonal**.

Without (3) and (4) there are infinitely many generalised inverses; with them the
inverse is unique.

---

## ★2 — SVD construction

$G = U\Sigma V^{\!\top} = \sum_i \sigma_i\mathbf{u}_i\mathbf{v}_i^{\!\top}$, so

$$G^{+} = V_r\Sigma_r^{-1}U_r^{\!\top}
= \sum_{i:\sigma_i>0}\frac{\mathbf{v}_i\mathbf{u}_i^{\!\top}}{\sigma_i}.$$

Zeros are excluded because $1/0$ is undefined; excluding them is exactly what
defines the minimum-norm/least-squares behaviour, since the omitted directions lie
in $\mathcal{N}(G)$ or in $\operatorname{range}(G)^{\perp}$.

---

## ★3 — Shapes and ranks

$G^{+}$: $6\times8$. $GG^{+}G$: $8\times6$ (equals $G$). $G^{+}GG^{+}$:
$6\times8$ (equals $G^{+}$). $GG^{+}$: $8\times8$ projector of rank $4$.
$G^{+}G$: $6\times6$ projector of rank $4$.

---

## ★4 — Uniqueness

Suppose both $X$ and $Y$ satisfy (1)–(4).

$$X \overset{(2)}{=} XGX \overset{(1)}{=} XG\,Y\,GX
\overset{(4)}{=} X\,(GY)^{\!\top}GX = X Y^{\!\top}G^{\!\top}G X
\overset{(1)}{=} XY^{\!\top}G^{\!\top}G Y G X,$$

and continuing with (4) and (2) together with $GX = GY$ and $XG = YG$ (both of which
follow from (1) and (2) applied to both matrices) gives $X = Y$. The essential step
is (4)/(3): they turn $GY$ into $(GY)^{\!\top} = Y^{\!\top}G^{\!\top}$, which lets the
products be reassociated; without them no uniqueness can be proved.

---

## ★5 — The silent wrong answer

(a) `numpy.linalg.solve` only raises when the matrix is *exactly* singular to
within its LAPACK test. Here two eigenvalues of $G^{\!\top}G$ are
$\approx10^{-31}$ rather than $0$, so the factorisation "succeeds" and the huge
$\kappa = 3.357\times10^{17}$ is never reported.

(b) Two checks: (i) compute and print $\kappa(G)$ (or the singular spectrum) and
refuse when $\kappa$ exceeds $1/\varepsilon$; (ii) verify the algebraic residuals
$\lVert GG^{+}G - G\rVert$ and $\lVert G^{+}GG^{+} - G^{+}\rVert$, or simply compare
the solution with the SVD-based one, which is what the demonstration did to detect
the $1.902$ error.

---

## ★6 — Norms in the solution set

Both terms are orthogonal, so
$\lVert\mathbf{m}\rVert^{2} = \lVert\hat{\mathbf{m}}\rVert^{2}
+ \lVert(I-G^{+}G)\mathbf{z}\rVert^{2}$. The second term is the projection of
$\mathbf{z}$ onto the 2-dimensional null space, so its norm is
$\le\lVert\mathbf{z}\rVert$, with equality when $\mathbf{z}$ lies entirely in that
space; in general it is a fraction.

At $\lVert\mathbf{z}\rVert = 0.5$: measured $\lVert\mathbf{m}\rVert = 9.4120$, so
$9.4120^{2} - 9.402127^{2} = 88.5857 - 88.3999 = 0.1858$, giving a null-space
component of norm $\sqrt{0.1858} = 0.4311$ (the demonstrated displacement
$0.4316$).

At $\lVert\mathbf{z}\rVert = 2.0$: $9.4415^{2} - 88.3999 = 89.1419 - 88.3999 =
0.7420$, component norm $0.8614$ against the demonstrated $0.8619$. This is the
expected scaling: doubling $\lVert\mathbf{z}\rVert$ doubles the null-space
component to within the projection factor.

---

## ★★★7 — Growth law and pipeline

The values $730.0\ (\delta = 10^{-2})$, $14334.9\ (10^{-3})$ and
$43071.9\ (10^{-4})$ give ratios $19.6$ and $3.0$. As $\delta$ shrinks the growth
approaches the $1/\delta$ law predicted by the argument that a perturbation
$\delta$ promotes an empty direction to $\sigma\sim\delta$, whose inverse is
$1/\delta$: indeed $14334.9\times10 = 143349$ and $43071.9\times10 = 430719$ are
the same order, and the ratio $3.0$ instead of $10$ reflects the transition to the
$1/\delta$ regime (the smallest *retained* singular value also limits the change).
Prediction at $\delta = 10^{-5}$: of order $10^{5}$–$10^{6}$, i.e. the inverse is
completely unstable to perturbations of the operator.

**Consequence for a pipeline.** A rank tolerance fixed in *absolute* terms is
meaningless: the same $\delta$ produces wildly different $G^{+}$. Therefore
(i) state the tolerance relative to $\sigma_1$, (ii) recompute and print the
spectrum for every data set, (iii) refuse to invert when no spectral gap is present
at the chosen tolerance, and (iv) prefer a continuous regulariser over a hard
truncation when the spectrum decays smoothly
([18-03-02](../../03-regularization/02-tikhonov.md)).

---

## ★★★8 — Specification for a rank decision

1. **Tolerance rule.** $\tau = \max(\text{eps}\cdot\kappa_{\text{warn}}, \tau_{\text{user}})$
   with a default $\tau_{\text{user}} = 10^{-10}$ relative to $\sigma_1$, and a
   documented increase to the *data precision* when the data are noisy (e.g.
   $10^{-6}$ for $1\%$ data). Justification: the rank is tolerance-dependent —
   measured rank 4, 5 and 6 at tolerances $10^{-6}$, $10^{-10}$ and $10^{-12}$ in
   [18-01-02 §6](../../01-inverse-problem-foundations/02-hadamard-well-posedness.md).
2. **Diagnostics printed.** Full relative spectrum, numerical rank at the declared
   tolerance, $\kappa$ of the retained part, and the four Moore–Penrose residuals
   $(\le10^{-15}$ in the demonstration). Justification: the residual checks caught
   the silent normal-equation failure of §5.
3. **Refusal conditions.** Refuse when (i) no gap in the spectrum at $\tau$ (the
   rank cut is arbitrary), (ii) $\kappa$ of the retained part exceeds
   $1/\varepsilon$ so the inverse amplifies roundoff to $O(1)$, (iii) the number of
   requested model parameters exceeds the retained rank while the user asked for
   per-parameter values. Justification: the continuity table — a
   $10^{-3}$ perturbation moved $G^{+}$ by $10^{4}$ — makes silent acceptance of
   (i)–(iii) indefensible.
4. **Reporting.** Emit the tolerance, the retained singular values, and a
   resolution summary ([18-02-05](../05-resolution-matrices.md)) with every model.
