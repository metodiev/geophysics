# Solutions — 18-07-03 Petrophysically Coupled Joint Inversion

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand. All models are **SYNTHETIC**.

Lesson: [03 Petrophysically Coupled Joint Inversion](../03-petrophysical-joint-inversion.md).

---

## ★1 — Normal-equation structure

With $\mathbf{x} = (\mathbf{m}_1,\mathbf{m}_2)$,

$$\left(
\begin{array}{c|c}
G_1^{T}G_1 + \lambda_p a^2 I & -\lambda_p a I\\[1mm]
\hline
-\lambda_p a I & G_2^{T}G_2 + \lambda_p I
\end{array}
\right)
\begin{pmatrix}\mathbf{m}_1\\ \mathbf{m}_2\end{pmatrix}
=
\begin{pmatrix}G_1^{T}\mathbf{d}_1 - \lambda_p ab\,\mathbf{1}\\
G_2^{T}\mathbf{d}_2 + \lambda_p b\,\mathbf{1}\end{pmatrix}.$$

The two diagonal blocks are each $n\times n$; the off-diagonal blocks
$-\lambda_p a I$ are the coupling, and they are what makes the system
non-separable. With smoothness added, $G_i^{T}G_i$ becomes
$G_i^{T}G_i + \lambda_s D^{T}D$.

---

## ★2 — What the coupling changes

Setting $\lambda_p=0$ leaves
$G_1^{T}G_1\mathbf{m}_1 = G_1^{T}\mathbf{d}_1$ and
$G_2^{T}G_2\mathbf{m}_2 = G_2^{T}\mathbf{d}_2$: two independent inversions.

For $\lambda_p>0$ both diagonal blocks gain a term
($+\lambda_p a^2 I$ on property 1, $+\lambda_p I$ on property 2) and the
off-diagonal blocks $-\lambda_p a I$ appear. Eliminating $\mathbf{m}_2$ gives

$$\left(G_1^{T}G_1 + \lambda_p a^2 I
- \lambda_p^2 a^2\left(G_2^{T}G_2+\lambda_p I\right)^{-1}\right)\mathbf{m}_1
= G_1^{T}\mathbf{d}_1 - \lambda_p ab\mathbf{1}
+ \lambda_p a\left(G_2^{T}G_2+\lambda_p I\right)^{-1}
\left(G_2^{T}\mathbf{d}_2+\lambda_p b\mathbf{1}\right),$$

so the coupling acts as a *rank-one-per-cell shrinkage* towards the relation:
as $\lambda_p\to\infty$, $\mathbf{m}_2 \to a\mathbf{m}_1 + b$.

---

## ★3 — Statistically consistent weight

For a Gaussian relation error with variance $\sigma_p^2$ and Gaussian data with
variance $\sigma_i^2$, the maximum-likelihood weights are
$\lambda_p = 1/\sigma_p^2$ (up to the common scale of the data weights). For
$\sigma_p = 0.03$ this is $\lambda_p = 1/0.03^2 = 1111$.

Assumption needed: the relation error is **independent** of the data errors and
is unbiased. If the calibration cores came from the same rocks the survey sees,
the errors are correlated and $\lambda_p$ must be reduced; if the relation is a
regional average applied to a different unit, $\lambda_p = 1/\sigma_p^2$
over-weights a model that is known to be wrong here.

---

## ★4 — Optimal weight from the sweep

From the printed table: error 2 is minimised at $\lambda_p = 0.05$, with

- error 2: $0.0599 \to 0.0423$, a reduction of
  $(0.0599-0.0423)/0.0599 = 29\%$;
- misfit 2: $0.0082 \to 0.0277$. The stated noise level is 20% of the data rms,
  i.e. $0.0411$, so the misfit sits at $0.0277/0.0411 = 0.67$ times the noise
  level — **inside** the noise floor, not at it.

The trade is worth it on any criterion that values model error over data misfit,
because the increased misfit does not exceed what the noise permits. Raising the
weight further breaks that condition: at $\lambda_p = 0.2$ the misfit is
$0.0521/0.0411 = 1.27$ times the noise level, at $\lambda_p = 1$ it is $1.81$
times, and the model error has also risen ($0.0599 \to 0.0728$ at
$\lambda_p = 0.5$). So the defensible window is $\lambda_p \lesssim 0.1$, and the
model-error minimum ($0.05$) lies inside it: **no criterion on which larger
weights win exists in this table.**

---

## ★5 — Plateau versus deviation

The deviation rms is the full size of the structure that the linear relation
cannot represent: $0.1061$. The plateau is $0.0918$, slightly smaller, because
the smoothness term $\lambda_s\|\nabla m_2\|^2$ already removes a part of the
high-frequency content of the deviation before the coupling acts. What remains
at infinite weight is the part of the deviation that is *smooth enough to survive
the smoothing* and *invisible to the relation*: that is the irreducible bias.

The plateau is therefore not "the deviation" but "the part of the deviation that
the combined prior cannot remove", which is why it must be computed rather than
assumed.

---

## ★6 — Two questions for a rock-physics claim

1. **"What is the residual of each coupled data set, and what is the stated
   noise level?"** Expected answer in a good report: a table of chi per datum
   for every data set. In the demonstration at $\lambda_p = 0.05$ the misfits are
   $0.0082$ and $0.0277$ against noise $0.0031$ and $0.0411$, i.e. chi of 2.65
   and 0.67: the coupling conforms the weak property to the relation (chi 0.67,
   inside its noise) at the cost of raising the strong property's residual to
   2.65 times its noise. Whether that is acceptable is precisely the question a
   reviewer must ask, and the answer turns on the relation's provenance — here
   the relation is known to be imperfect, since the truth contains a deviation
   of rms 0.106 that no linear relation represents. The wrong-relation model has
   $0.1265$ against $0.0411$, chi 3.08, and should have been rejected.
2. **"Where did the relation come from and what is its error bar?"** Expected
   answer: the provenance (core measurements, well logs, a stated ensemble) and a
   number for $\sigma_p$; without it, $\lambda_p$ is arbitrary and the result is
   not reproducible.

---

## ★7 — Relation from wells, weight from the discrepancy principle

Procedure: (i) fit the relation from the wells only, keeping those wells out of
the inversion, and record $\sigma_p$ and the number of wells; (ii) initialise
$\lambda_p = 1/\sigma_p^2$; (iii) compute chi per datum for the coupled property
at the solution; (iv) if chi $>1$ by more than, say, 20%, reduce $\lambda_p$
(e.g. by factors of 2) until chi is within that band or $\lambda_p$ reaches a
floor; (v) report the final $\lambda_p$, both misfits and the sensitivity of the
model to $\lambda_p$ over a factor of four either side.

If the misfit cannot be brought to the noise level at any admissible
$\lambda_p$, the conclusion is not "raise the weight": it is that the relation
and the data are mutually inconsistent for that property — exactly the situation
measured in the wrong-relation table, and the honest output is to report the
inconsistency.

---

## ★8 — Harmless versus circular clustering

*Harmless.* The ensemble used to fit the clusters comes from an independent data
set: well logs from the survey area that were not used in the geophysical
inversion. The clusters then carry external information, and the coupling is an
honest prior.

*Circular.* The clusters and lines are estimated from the two uncoupled
geophysical models, then the same models are re-inverted with a penalty towards
those lines. Nothing outside the two data sets enters, so the coupling cannot add
information; it can only select among models the data already allow. The
measured scatter falls, but that is a statement about the penalty, not the Earth.

The distinguishing experiment: split the inversion's model cells into two halves,
estimate the relation on one half only, and apply it to the other. If the
relation estimated from the models is informative, the coupling on the held-out
half should reduce its model error against an independent truth (or, with real
data, reduce the misfit of a data set held out of the estimation). If the gain
disappears, the relation was circular.
