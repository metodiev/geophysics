# Exercises — 01-07-08 Singular Value Decomposition and Rank Truncation

Attempt these **closed-book**, on paper, before opening the
[solutions](./08-svd-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

---

## ★ Foundational

**★1.** Compute the SVD by hand for
$A = \begin{bmatrix} 3 & 0 \\ 4 & 0 \\ 0 & 1\end{bmatrix}$.

(a) Give $U$, $\Sigma$ and $V$.
(b) State the rank and the condition number.
(c) Write the pseudoinverse $A^{+}$.
(d) Verify $A = U\Sigma V^\mathsf{T}$ entry by entry.

---

**★2.** For the $A$ of ★1, write down, from the SVD alone:

(a) orthonormal bases of the column space, the row space, the null space and the left
null space;
(b) the dimension of each;
(c) a check of the rank–nullity theorem in both the model and the data spaces.

---

## ★★ Applied

**★★3.** The lesson's five-ray kernel is

$$A = \begin{bmatrix} 1 & 1 & 0 \\ 1 & 1.02 & 0 \\ 0 & 0 & 1 \\ 0.5 & 0.5 & 0.5 \\
0.5 & 0.5 & 0\end{bmatrix} \ \text{km}.$$

A sixth ray with path lengths $(1,1,0)$ km is added — a duplicate of ray 1.

(a) Predict, before computing, the effect on the three singular values and on the
condition number. Justify the prediction from the geometry.
(b) Compute the new singular values and compare with your prediction.
(c) Explain why the smallest singular value barely changes even though the number of data
increased by 20 %.
(d) Compute the mean leverage before and after, and state whether the new datum
contributes information.

---

**★★4.** A survey has
$G = \begin{bmatrix} 1 & 1 \\ 1 & 1.1 \\ 1 & 1.2\end{bmatrix}$ km and
$d = (0.03,\ 0.032,\ 0.034)^\mathsf{T}$ s.

(a) Compute the SVD and the least-squares solution, and report the residual.
(b) Compute the model resolution matrix $R$ and the data resolution matrix $N$.
(c) With $\sigma_d = 10^{-3}$ s, compute the model covariance and the standard deviation
along each singular direction.
(d) State in one sentence each which model combination this survey determines and which
it does not.

---

## ★★★ Research-oriented

**★★★5.** Bias and variance. For the five-ray kernel of ★3 with
$m_{\text{true}} = (0.05,-0.02,0.03)$ $\mathrm{s/km}$:

(a) For truncation ranks $p = 1,2,3$, compute the squared bias
$\|(I - R_p)m_{\text{true}}\|^{2}$ and $\operatorname{tr}C_m^{(p)}$.
(b) Report the total expected squared error for each $p$ and the optimum, at
$\sigma_d = 10^{-3}$ s.
(c) Repeat at $\sigma_d = 10^{-1}$ s and $\sigma_d = 10^{-5}$ s, and state how the
optimal rank moves.
(d) Explain in a paragraph why the optimal rank depends on the noise level, and give the
one-line criterion that would let you compute it without iterating over $p$.

---

**★★★6.** Low-rank compression. Build a synthetic two-dimensional field representing a
gravity anomaly from two rectangular prisms of different size, depth and orientation
(for example, evaluate the vertical gravity of two prisms, or use any smooth
two-dimensional function of your choosing — state precisely what you used).

(a) Report the singular-value spectrum of the $12\times12$ (or larger) field matrix.
(b) Report the relative Frobenius error of the rank-$p$ approximation for $p = 1$ to
$10$.
(c) State the rank needed for $1$ % accuracy, and compare with the rank needed for the
lesson's rotated-ellipse field (which needed $6$ of $12$).
(d) Explain why a deeper, smoother source has a lower effective rank than a shallow,
compact one, and connect this with the resolution discussion of Section 4 of the lesson.
