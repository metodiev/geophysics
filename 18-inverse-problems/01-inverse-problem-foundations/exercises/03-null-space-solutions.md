# Solutions — 18-01-03 Null Space, Non-Uniqueness and Equivalence Classes

> **Read after attempting the exercises.** Lesson:
> [03 Null Space and Non-Uniqueness](../03-null-space.md).

---

## ★1 — Rank-nullity

Five non-zero singular values, so $\operatorname{rank}(G) = 5$ and
$\dim\operatorname{range}(G) = 5$ (the range is a subspace of
$\mathbb{R}^{5}$ — here it is all of it). $M = 16$, so
$\dim\mathcal{N}(G) = 16-5 = 11$, and $5+11 = 16$ ✔.

---

## ★2 — An exchange null vector

$\mathbf{n} = \mathbf{e}_2 - \mathbf{e}_3$: both cells lie in the same ray (row 0),
so every row of $G$ has the same entry in columns 2 and 3, and
$G\mathbf{n} = \mathbf{0}$ exactly — the demonstration measured
$0.000\times10^{0}$.

---

## ★3 — Structural null space

No row of $G$ has a non-zero entry in column 8, so $G\mathbf{e}_8 = \mathbf{0}$
trivially. Consequence: *nothing* the experiment measured constrains cell 8; any
value you report comes from your prior or estimator, and it must be flagged.

---

## ★4 — Reconstructing a lower bound

The diagonal reading is $1.2 = m_0+m_5+m_{10}+m_{15}$. The row-0 reading caps
$m_0\le0.4$; row 1 caps $m_5\le0.3$; row 3 caps $m_{15}\le0.3$. To minimise
$m_{10}$ make all three as large as possible:

$$m_{10} = 1.2 - 0.4 - 0.3 - 0.3 = 0.2 .$$

The bound is produced by the *combination* of the diagonal measurement with the
three row measurements — not by any single reading. This is what it means for the
data to carry more information than per-cell answers.

---

## ★5 — Resolved combinations

$m_0+m_1+m_2+m_3$ is exactly the reading of ray R1, so it lies in
$\operatorname{range}(G^{\!\top})$ and is fixed to $0.4$ with zero width.
$m_3+m_7+m_{11}+m_{15}$ mixes a column: only cell 15 of that column lies in a
measured row (row 3), and cell 11 is visited by no ray, so the sum contains
unconstrained pieces and its interval is wide.

---

## ★6 — Squared conditioning

$\kappa(G) = 2.6458/1.4142 = 1.8708$, so
$\kappa(G)^{2} = 3.5000$. The demonstration measured
$\kappa(G^{\!\top}G) = 7.0000/2.0000 = 3.5000$, and the ratio
$\kappa(G^{\!\top}G)/\kappa(G)^{2} = 1.000000$.

With $\kappa(G) = 10^{8}$ and $\varepsilon = 2.2\times10^{-16}$: the normal
equations lose $\log_{10}\kappa(G^{\!\top}G) = \log_{10}(10^{16}) = 16$ digits
while double precision carries about $16$, so the solution is entirely noise. The
SVD route costs $\log_{10}(10^{8}) = 8$ digits, leaving about $8$ — usable.

---

## ★★★7 — Testing a coverage claim

**Smallest analysis.** Build the ray-path matrix $G$ ($40\times200$, entries are
path lengths), compute its SVD, and report (i) the singular spectrum, (ii) the
numerical rank at a tolerance matched to the data precision, (iii) the dimension
of the null space.

**Report instead of per-cell values.** Averages over resolved combinations: the
projection $\mathbf{m}_{\text{row}} = V_rV_r^{\!\top}\mathbf{m}$ of the model onto
the row space, plus per-cell feasible intervals if bounds are available. Phrase
conclusions about *averages over regions* whose indicator vectors lie in
$\operatorname{range}(G^{\!\top})$.

**The one number.** The numerical rank: $r = 40$ at most (there are only 40 rays
and rows can be dependent), so at least $200-40 = 160$ dimensions are
unconstrained. A single ray is one constraint no matter how many cells it crosses;
"good coverage" is a statement about *angles*, and its quantitative test is the
condition number of the resolved part, not the number of rays.

---

## ★★★8 — Products of parameters

$m_0m_{10}$ is not linear in $\mathbf{m}$, so its feasible interval cannot be read
from the linear-programming intervals of $m_0$ and $m_{10}$: the extrema of a
product are attained at *corners* of the feasible set where the signs align, and
the interval endpoints are attained by different members of the class. Writing
$\min$ and $\max$ of $m_0m_{10}$ over
$\{\mathbf{m}:G\mathbf{m}=\mathbf{d},\ 0\le m\le1\}$ gives a **non-convex
quadratic program**: still solvable in low dimension, but not by the linear
machinery of the lesson.

**Class of problem and method.** It is a quadratically constrained optimisation, and
better framed probabilistically: sample the equivalence class (or, with noise, the
posterior). Methods that scale to $10^{4}$ parameters: constrained realisations
from the null space via (i) randomised null-space sampling as in the demonstration
(cheap, linear algebra only), or (ii) Markov chain Monte Carlo on the posterior
([18-05-04](../../05-bayesian-inversion/04-mcmc.md)), or (iii) interval/ellipsoidal
bounds from the singular spectrum (fast, conservative).
