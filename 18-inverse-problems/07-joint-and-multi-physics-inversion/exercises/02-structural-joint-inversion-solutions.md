# Solutions — 18-07-02 Structural (Cross-Gradient) Coupling

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand. All models are **SYNTHETIC**.

Lesson: [02 Structural (Cross-Gradient) Coupling](../02-structural-joint-inversion.md).

---

## ★1 — Parallel gradients

$$\partial_x m_1 = 1,\quad \partial_y m_1 = 2,\quad
\partial_x m_2 = 3,\quad \partial_y m_2 = 6 .$$

$$t = \partial_x m_1\,\partial_y m_2 - \partial_y m_1\,\partial_x m_2
= (1)(6) - (2)(3) = 0 .$$

The gradients $\nabla m_1 = (1,2)$ and $\nabla m_2 = (3,6) = 3(1,2)$ are
parallel, so the fields share geometry. ✔ (They differ only by an amplitude
factor and a constant, which is exactly the case the coupling is designed for.)

---

## ★2 — Anti-parallel gradients

$$\partial_x m_2 = 3,\quad \partial_y m_2 = -6,\quad
t = (1)(-6) - (2)(3) = -12 .$$

The gradients $\nabla m_2 = (3,-6)$ and $\nabla m_1 = (1,2)$ are antiparallel
($\sin\theta$ with $\theta = 180^\circ$ gives a vanishing cross-product
magnitude), so the *sign* differs from the parallel case while the geometry is
still shared. The scalar $t$ changes sign; the penalty $\sum t^2$ does not, which
is why the coupling is insensitive to polarity reversals — a strength for
resistivity contrasts, a weakness when polarity carries information.

---

## ★3 — Constant fields

$\nabla m_1 = \nabla m_2 = \mathbf{0}$, so $t = 0$ exactly. The penalty
therefore has its global minimum at the least informative models in the space:
**a constant model satisfies the coupling perfectly**, so the term cannot by
itself prefer structure to no structure and must always be combined with a data
term that requires structure.

---

## ★4 — Choosing the weight

From the sweep, uncoupled misfits are 0.0147 and 0.0155; a 10% rise allows
0.0162 and 0.0171.

| $\lambda_x$ | misfit 1 | misfit 2 | both within 10%? |
|---|---|---|---|
| 0.3 | 0.0147 | 0.0156 | yes |
| 1.0 | 0.0148 | 0.0158 | yes |
| 3.0 | 0.0160 | 0.0162 | yes |
| 10.0 | 0.0237 | 0.0221 | no |

The largest admissible weight is $\lambda_x = 3$ (0.0160 and 0.0162, both within
the 10% band); $\lambda_x = 10$ fails on both misfits. At $\lambda_x = 3$ the
structural disagreement is *not* lower than at $\lambda_x = 1$
($5.455\times10^{-3}$ versus $2.452\times10^{-3}$), and the model errors are
higher (0.0929/0.0765 versus 0.0847/0.0764). So the misfit-only rule chooses a
worse model: **the requirement you write down determines the answer you get**,
which is the practical reason to state the requirement before the sweep.

---

## ★5 — Scaling identity

$t(\alpha m_1, \beta m_2)
= (\alpha\partial_x m_1)(\beta\partial_y m_2)
- (\alpha\partial_y m_1)(\beta\partial_x m_2)
= \alpha\beta\,t(m_1,m_2)$.

With $\alpha=3,\beta=2$: every cross-gradient is exactly 6 times the original.

Practical consequence: the numerical size of $t$ depends on the *units* of the two
properties, so a fixed $\lambda_x$ means different strengths for g cm$^{-3}$ and
$\Omega$ m. Either normalise each property to unit variance before coupling, or
report $\lambda_x$ together with the units — otherwise the weight is not
reproducible.

---

## ★6 — Why the misfit is the diagnostic

A practitioner who only inspected forward-modelled predictions would compare
them with the observed data and find a residual that is larger than the noise
but *not absurd*; nothing in the coupled model's own plot says "there is a blob
here that I am ignoring". The information that the second structure exists is
only in the residual pattern, and only if the noise level is known.

Diagnostic: the per-datum chi of **each** data set, computed at the coupled
solution and compared with the stated noise (misfit 2 = 0.0315 against a
noise-level expectation near 0.0107). A jointly inverted model with one residual
far above its noise level has not converged to a physically consistent answer; it
has converged to the best compromise the false hypothesis allows.

---

## ★7 — Distinguishing the two failure modes

Diagnostic quantity: $\mathrm{rms}\,|t|$ of the recovered pair, plus each misfit,
swept over $\lambda_x$.

- Control experiment: the *same* two data sets generated from two truths that
  **do** share geometry, inverted over the same $\lambda_x$ grid. This gives the
  shape of the misfit-versus-weight curve when the hypothesis is true.
- Decision rule: if $\mathrm{rms}|t|$ falls and both misfits stay flat as
  $\lambda_x$ grows, the structures agree. If $\mathrm{rms}|t|$ fails to fall
  while the misfits rise, the hypothesis is false. Increasing the weight further
  must not be used to force the first outcome.

---

## ★8 — Removing the flat minimum

Normalise the cross-gradient by the gradient magnitudes,

$$\tilde t = \frac{\partial_x m_1\,\partial_y m_2 - \partial_y m_1\,\partial_x m_2}
{\sqrt{\left(|\nabla m_1|^2+\epsilon^2\right)\left(|\nabla m_2|^2+\epsilon^2\right)}} ,$$

which equals $\sin\theta$ and is invariant to amplitude, so the penalty measures
orientation at every cell regardless of how strong the gradients are.

New failure mode: $\tilde t$ is *undefined* where a gradient vanishes, so
$\epsilon$ becomes a hidden smoothing parameter, and the penalty now fires
loudly in regions where the gradients are tiny but not parallel — noise-dominated
cells where the orientation is meaningless. The flat-minimum loophole is closed
and a noise-amplification loophole is opened; the honest choice depends on
whether the weakly structured regions are of interest.
