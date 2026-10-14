# Solutions — 18-03-04 L1 Regularisation, Sparsity and Compressive Sensing

> **Read after attempting the exercises.** Numbers were computed by
> `code/sparsity_demo.py` unless shown as hand arithmetic.

Lesson: [04 L1 Regularisation, Sparsity and Compressive Sensing](../04-sparsity.md).
All models are **SYNTHETIC**.

---

## ★1 — Soft thresholding

$$\mathrm{soft}(1.4,0.6) = \mathrm{sign}(1.4)\max(1.4-0.6,0) = 0.8,$$
$$\mathrm{soft}(0.5,0.6) = \mathrm{sign}(0.5)\max(0.5-0.6,0) = 0,$$
$$\mathrm{soft}(-2.5,3.0) = \mathrm{sign}(-2.5)\max(2.5-3.0,0) = 0 .$$

Both the second and the third input satisfy $|x| \le t$ and are therefore mapped
to exactly zero; only the first has $|x| > t$. A zero output is the Lasso's "this
coefficient is discarded" decision, and the boundary $|x| = t$ is where the
subdifferential at zero starts to matter.

---

## ★2 — One-column Lasso

The unregularised solution is $m_{\mathrm{LS}} = ad/a^2 = d/a = 3/2 = 1.5$. The
soft-threshold form is

$$m^\star = \mathrm{soft}\Big(\frac{ad}{a^2},\ \frac{\alpha}{a^2}\Big)
= \mathrm{soft}\Big(1.5,\ \frac{0.4}{4}\Big) = \mathrm{soft}(1.5,0.1) = 1.4 .$$

**Optimality check.** $a(am^\star-d) = 2(2\times1.4-3) = 2(-0.2) = -0.4$, and
$-\alpha\,\mathrm{sign}(m^\star) = -0.4\times(+1) = -0.4$. ✔ The bias is
$1.5-1.4 = 0.1 = \alpha/a^2$, exactly as the general formula predicts with
$A_S^{\mathsf T}A_S = a^2 = 4$.

---

## ★3 — Critical parameter for one unknown

$$A^{\mathsf T}d = 2\times3 + 1\times1 = 7
\;\Rightarrow\; \alpha_{\max} = \|A^{\mathsf T}d\|_\infty = 7 .$$

For $\alpha = 8 > \alpha_{\max}$ the solution is **exactly zero**: the gradient of
the data term at the origin is $-A^{\mathsf T}d = -7$, whose largest component is
$7 \le \alpha$, so zero is in the subdifferential and no coordinate can reduce the
objective.

---

## ★★4 — Non-zeros as $\alpha$ falls

$\alpha = 0.05\times2.6527 = 0.13264$. From the measured table:

| $\alpha/\alpha_{\max}$ | non-zeros | support exact? |
|---|---|---|
| 0.5 | 3 | no |
| 0.3 | 3 | no |
| 0.1 | 4 | yes |
| 0.05 | 4 | yes |

The count grows monotonically as $\alpha$ falls: at large $\alpha$ the penalty
overwhelms the gradient for all but the strongest coordinate
(cf. the exact boundary at $\alpha_{\max}$, where one coordinate survives by
$2.5075\times10^{-4}$), and the support grows in from the largest coefficient
outwards. At $\alpha \le 0.1\,\alpha_{\max}$ all four true spikes are present and
the closed-form bias formula applies.

---

## ★★5 — Single-spike shrinkage

With $\|a_j\|_2 = 1$ the matrix $A_S^{\mathsf T}A_S$ is $1\times1$ in the
single-spike approximation, so the shrinkage is

$$\alpha\,(A_S^{\mathsf T}A_S)^{-1}\mathrm{sign}(m_S)
= 0.13264\times1\times1 = 0.13264,$$

and the recovered amplitude is $2.5 - 0.13264 = 2.367$: $94.7\%$ of the truth.

The measured median fraction is $93.9\%$, i.e. about $0.8$ percentage points
lower. The reason is that $(A_S^{\mathsf T}A_S)^{-1}$ is not diagonal: its
off-diagonal entries are positive for overlapping columns, so the bias vector
$\alpha(A_S^{\mathsf T}A_S)^{-1}\mathrm{sign}(m_S)$ has components larger than
$\alpha$ for spikes whose neighbours are also present. **The closed form is exact;
the single-spike approximation is what fails.**

---

## ★★6 — Coherence bound against measurement

The sufficient condition for exact $\ell_1$ recovery of a $k$-sparse model is
$k < \tfrac12(1+1/\mu)$.

| design | $\mu$ | bound $k <$ | measured support recovery |
|---|---|---|---|
| Gaussian | 0.4928 | $(1/2)(1+2.029) = 1.51$ | 1.00 at $k=2$ and $4$; 0.87 at $k=6$ |
| line-mass kernel | 0.9999 | $(1/2)(1+1.0001) = 1.000$ | 0.00 at every $k$ tested |

For the line-mass kernel the bound is consistent with the measurement: it
excludes $k \ge 2$ and nothing was recovered. For the Gaussian design the bound
guarantees recovery only for $k = 1$, yet $k = 4$ was recovered in every trial:
**the bound is sufficient, not necessary, and it is pessimistic by at least a
factor of four here.** That is why coherence is a useful *warning* about a design
and a poor *prediction* of performance; the quantity that actually governs
recovery is the restricted-isometry property of the whole matrix, which pairwise
coherence only bounds from below.

---

## ★★★7 — Two correlated columns

Take the true support to be two spikes of equal amplitude $c > 0$ with
$A_S^{\mathsf T}A_S = \begin{pmatrix}1 & \rho\\ \rho & 1\end{pmatrix}$, so
$\mathrm{sign}(m_S) = (1,1)^{\mathsf T}$ and

$$(A_S^{\mathsf T}A_S)^{-1} = \frac{1}{1-\rho^2}
\begin{pmatrix}1 & -\rho\\ -\rho & 1\end{pmatrix},$$

$$(A_S^{\mathsf T}A_S)^{-1}\mathrm{sign}(m_S) = \frac{1}{1-\rho^2}
\begin{pmatrix}1-\rho\\ 1-\rho\end{pmatrix}
= \frac{1}{1+\rho}\begin{pmatrix}1\\1\end{pmatrix}.$$

Hence

$$m_{\mathrm{hat},S} = \left(c - \frac{\alpha}{1+\rho}\right)(1,1)^{\mathsf T}.$$

**As $\rho\to+1$** the two columns become identical, the pair behaves like a
single column of doubled amplitude, and the *shrinkage per component halves*
(denominator $1+\rho \to 2$). **As $\rho\to-1$** the two columns nearly cancel,
the pair carries almost no signal, and the shrinkage diverges
($1+\rho \to 0$).

**Connection to the measured failure.** The measured coherence $\mu = 0.9999$ for
the line-mass kernel comes from neighbouring columns of the same sign, i.e. the
$\rho \to +1$ case, where a *pair* is not catastrophic. The observed
total failure of support recovery is therefore **not** explained by the worst
single pair: it is the cumulative effect of many overlapping columns, i.e. a
rank deficiency of the design over the resolution scale — the same phenomenon
measured as the singular-value decay and the Picard condition in lesson
[01](../01-why-regularize.md). The pairwise-coherence metric summarises a design
with one number, and that number is not sufficient to predict performance.

---

## ★★★8 — Separating noise-fitting from genuine extra coefficients

At $k = 16$ the solution has 14 extra coefficients whose largest amplitude is
$1.55\times10^{-1}$ — comparable to the smallest true amplitude ($0.7$), so the
question is real.

**Design.** Fix the matrix and the true model; generate 50 noise realisations at
each of three noise levels ($0.1\%$, $1\%$, $10\%$ of $\|d\|/\sqrt m$); solve at
a fixed $\alpha/\alpha_{\max}$; for each extra coefficient record (i) whether it
appears, (ii) its amplitude, (iii) its sign.

**Statistic.** The *appearance frequency* and the *sign consistency* of each
extra coefficient, and the slope of its mean amplitude against the noise level.

**Discrimination.**
- Noise-driven coefficients appear in roughly half the realisations, flip sign
  between realisations, and their mean amplitude scales **linearly with the noise
  level**.
- Genuine-but-unresolved features appear in nearly every realisation, keep a
  consistent sign, and their amplitude is **invariant to the noise level**
  (it is set by the data's small singular values, not by the noise).

A single experiment can therefore decide the question, and it needs no knowledge
of the truth beyond the ability to vary the noise.
