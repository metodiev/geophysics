# Exercises — 01-15-02 Tensor Algebra, Transformation Laws and Invariants

Attempt these **closed-book** before opening the
[solutions](./02-tensor-algebra-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Use the rotation about $z$ by $30^\circ$,

$$Q = \begin{pmatrix} 0.8660254 & -0.5 & 0\\ 0.5 & 0.8660254 & 0\\ 0&0&1
\end{pmatrix},$$

where needed, and

$$T = \begin{pmatrix} 8 & -3 & 1\\ -3 & 5 & 2\\ 1 & 2 & -4\end{pmatrix}, \qquad
W = \begin{pmatrix} 0 & -1.5 & 2\\ 1.5 & 0 & -0.7\\ -2 & 0.7 & 0\end{pmatrix}.$$

---

## ★ Foundational

**★1.** (a) Transform $\mathbf{v} = (3,-1,2.5)$ with $Q$ using the vector law.
(b) Verify $\lvert\mathbf{v}'\rvert = \lvert\mathbf{v}\rvert$.
(c) Transform $T$ with $Q$ using the rank-2 law, both as a matrix product and as
the index sum $T'_{ij} = Q_{ip}Q_{jq}T_{pq}$.

---

**★2.** Compute $I_1$, $I_2$ and $I_3$ of $T$ directly from the components, then
compute the eigenvalues and verify that the invariants are the elementary
symmetric functions of the eigenvalues.

---

**★3.** Which of the following arrays are tensors under the transformation law?
Justify each answer by a calculation or by a counterexample.
(a) $\delta_{ij}$, (b) the array with $\gamma_{12} = 2e_{12}$ in place of $e_{12}$,
(c) $\varepsilon_{ijk}$ under a proper rotation, (d) $\varepsilon_{ijk}$ under a
reflection.

---

**★4.** Recover the axial vector $w_i$ of $W$ from
$w_i = -\tfrac{1}{2}\varepsilon_{ijk}W_{jk}$, then reconstruct $W$ from $w_i$ and
check that you recover the original.

---

## ★★ Applied

**★★5.** Prove from the transformation law that symmetry and antisymmetry of a
rank-2 tensor are preserved by every orthogonal transformation.

---

**★★6.** Prove that $T_{ii}$ is invariant. Then exhibit an explicit pair of
rotations under which a single component $T_{11}$ changes, and state why no
argument of the ★★5 type can ever prove the invariance of one component.

---

**★★7.** Write down the two tensors
$I_{ijkl} = \delta_{ij}\delta_{kl}$ and
$J_{ijkl} = \tfrac{1}{2}(\delta_{ik}\delta_{jl} + \delta_{il}\delta_{jk})$, and
show that they are independent by contracting each with $\delta_{ij}$ and reading
off the results. Explain what the two resulting multiples of $\delta_{kl}$ mean.

---

**★★8.** Take the pure shear strain $e_{12} = e_{21} = 0.01$ and rotate it by
$30^\circ$ about $z$.
(a) Compute $e'$ with the tensor law.
(b) Rotate the engineering array ($\gamma_{12} = 0.02$) componentwise and compare
with the correct engineering array of $e'$. Quantify the largest discrepancy.
(c) Compute the second invariant of the strain tensor and of the engineering array
before and after the rotation, and comment.

---

## ★★★ Research-oriented

**★★★9.** For

$$A = \begin{pmatrix} 0&-1&0\\1&0&0\\0&0&2\end{pmatrix},$$

compute the eigenvalues (they are not all real), the three invariants of the
characteristic polynomial, and the squared Frobenius norms of the symmetric and
antisymmetric parts. Verify numerically that
$A_{ij}A_{ij} = S_{ij}S_{ij} + W_{ij}W_{ij}$, that all four quantities are
invariant under an orthogonal transformation, and state what additional
structure the *reality* of the eigenvalues requires.

---

**★★★10.** Build two $6\times6$ Voigt stiffness matrices with the identical
transverse-isotropic zero pattern, one with $C_{12} = C_{11} - 2C_{66}$ and one
with $C_{12}$ set to a different value. Show by explicit rotation of the full
rank-4 tensor that only the first is invariant under a six-fold rotation, and
explain what goes wrong if the second is used as a hexagonal stiffness.
