# Exercises — 01-07-04 Rank, Null Space and Solvability

Attempt these **closed-book**, on paper, before opening the
[solutions](./04-rank-and-nullspace-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

---

## ★ Foundational

**★1.** For $A = \begin{bmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 1 & 1 & 1\end{bmatrix}$:

(a) Compute the rank by row reduction and give a basis of the null space.
(b) Give a basis of the left null space and state the consistency condition it implies.
(c) Decide whether $d = (1,2,1)^\mathsf{T}$ and $d = (1,0,0)^\mathsf{T}$ are
consistent. For each, state which of the two failures — existence or uniqueness — it
exhibits.
(d) Verify the rank–nullity theorem in both the model space and the data space.

---

**★2.** For the lesson's redundant-ray kernel,
$G = \begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 2 & 1\end{bmatrix}$ km:

(a) Decide consistency for $d = (2,-1,1)^\mathsf{T}$ and $d = (2,-1,2)^\mathsf{T}$ using
the rank test.
(b) Confirm by attempting to solve.
(c) For the consistent one, give two distinct models that fit it.

---

## ★★ Applied

**★★3.** A cross-hole survey uses four rays through three cells, with path lengths

$$G = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 1 & 1
\end{bmatrix} \ \text{km}.$$

(a) Compute the rank and the null space.
(b) Give a basis of the left null space and the consistency condition it implies.
(c) Omit the fourth ray and compute the condition number of both kernels. State
precisely what the fourth ray buys and what it does not.
(d) For the full four-ray geometry, compute the minimum-norm model that fits
$d = (0.01, 0.02, 0.03, 0.06)^\mathsf{T}$ s, verify it satisfies $Gm = d$, and explain
why the phrase "minimum norm" is vacuous here.

---

**★★4.** For the kernel $G$ of ★2, compute the resolution matrix $R$ by hand from a
basis of the row space, and verify

(a) $R^{2} = R$ and $R = R^\mathsf{T}$,
(b) $\operatorname{tr}R = 2$,
(c) that $m - Rm$ is parallel to the null vector $\hat n$ for $m = (1,2,3)^\mathsf{T}$,
and give the proportionality constant,
(d) which cells are resolved and which are not, from $\operatorname{diag}R$.

---

## ★★★ Research-oriented

**★★★5.** Design a survey with a **two-dimensional** null space. Use four cells and
four rays.

(a) Give the kernel explicitly, with a physical reading of each ray.
(b) Verify that the rank is 2 and give bases of the null space and the left null space.
(c) State the consistency conditions the data must satisfy, and interpret them.
(d) Explain how you would use the left null vectors as noise checks, and what
information about the noise you would obtain.
(e) State what additional measurement would reduce the null space to one dimension,
and give the resulting kernel.

---

**★★★6.** The resolution matrix for a full-column-rank $G$ is the identity, yet the
model error can still be large.

(a) Explain in two sentences why $R = I$ is not contradictory with a large model error.
(b) For $G = \begin{bmatrix} 1 & 1 \\ 1 & 1.01\end{bmatrix}$ and
$\sigma_d = 10^{-3}$ s, compute $R$ and the model covariance
$C_m = \sigma_d^{2}(G^\mathsf{T}G)^{-1}$.
(c) Report the standard deviation of $m_1$, of $m_2$, of the difference $m_1 - m_2$ and
of the sum $m_1 + m_2$.
(d) State which of those four quantities is "resolved", and justify the word with the
numbers you obtained.
(e) Explain, in one sentence, why the sum is so much better determined than either
parameter individually.
