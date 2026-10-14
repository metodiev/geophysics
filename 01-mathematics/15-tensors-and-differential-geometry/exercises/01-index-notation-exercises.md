# Exercises — 01-15-01 Index Notation, Einstein Summation and Kronecker Delta

Attempt these **closed-book** before opening the
[solutions](./01-index-notation-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Unless stated otherwise, the index range is $1,2,3$ and summation is over that
range.

---

## ★ Foundational

**★1.** Write each expression in index form.
(a) $A\mathbf{x}$, (b) $\mathbf{x}\cdot\mathbf{y}$, (c) $\operatorname{tr}A$,
(d) $\det A$, (e) $\nabla\cdot\mathbf{F}$.

Write each index expression in matrix or vector form.
(f) $A_{ij}B_{jk}$, (g) $\varepsilon_{ijk}a_jb_k$, (h) $u_{i,i}$,
(i) $\sigma_{ij}n_j$, (j) $T_{ij}n_in_j$.

---

**★2.** For each expression, state how many free indices there are and which
indices are summed. Mark as invalid any expression that cannot be interpreted.
(a) $a_ib_i$, (b) $a_ib_j$, (c) $A_{ii}B_{jj}$, (d) $A_{ij}B_{jk}C_{ki}$,
(e) $a_i + b_i$, (f) $A_{ii} + B_{ii}$, (g) $A_{ij}B_{jk}C_k$,
(h) $\delta_{ij}a_ib_j$, (i) $\varepsilon_{ijk}a_ia_j$, (j) $A_{ij}B_{ij}$.

---

**★3.** Evaluate, stating the value for each $i,j,k$ where relevant:
(a) $\delta_{ij}a_j$ for $a = (4,-2,7)$, (b) $\delta_{ii}$,
(c) $\delta_{ij}\delta_{jk}$, (d) $\varepsilon_{ijk}\varepsilon_{ijk}$,
(e) $\varepsilon_{123}$, (f) $\varepsilon_{213}$, (g) $\varepsilon_{112}$,
(h) $\varepsilon_{ijk}\varepsilon_{ilk}$.

---

**★4.** With

$$A = \begin{pmatrix} 1&2&3\\4&5&6\\7&8&9\end{pmatrix}, \qquad
\mathbf{x} = \begin{pmatrix}1\\-1\\2\end{pmatrix},$$

compute (a) $A_{ii}$, (b) $A_{ij}x_j$, (c) $A_{ij}x_ix_j$, (d) $A_{ij}A_{ij}$,
(e) $A_{ij}A_{ji}$, (f) $\det A$, and (g) the symmetric and antisymmetric parts
$S_{ij}$ and $W_{ij}$.

---

## ★★ Applied

**★★5.** Prove $\varepsilon_{ijk}\varepsilon_{ilm} = \delta_{jl}\delta_{km} -
\delta_{jm}\delta_{kl}$ by considering the cases $j = k$ and $j \neq k$.
Then set $l = j$ to obtain $\varepsilon_{ijk}\varepsilon_{ijm} = 2\delta_{km}$ and
contract once more to obtain $\varepsilon_{ijk}\varepsilon_{ijk} = 6$.

---

**★★6.** Using the epsilon-delta identity, prove
(a) $\nabla\cdot(\nabla\times\mathbf{F}) = 0$ and
(b) $\nabla\times(\nabla f) = \mathbf{0}$.
State the differentiability assumption used, and explain why the numerical check
of (b) on a symmetric stencil cannot fail.

---

**★★7.** Expand $\sigma_{ij} = C_{ijkl}u_{k,l}$ for an isotropic medium with
$C_{ijkl} = \lambda\delta_{ij}\delta_{kl} +
\mu(\delta_{ik}\delta_{jl} + \delta_{il}\delta_{jk})$, showing every delta
contraction explicitly, and conclude that
$\sigma_{ij} = \lambda u_{k,k}\delta_{ij} + \mu(u_{i,j} + u_{j,i})$.

---

**★★8.** Show that the antisymmetric part of a displacement gradient cannot
appear in the quadratic form $\tfrac{1}{2}\sigma_{ij}\omega_{ij}$ when $\sigma$ is
symmetric. State the physical reading of the result.

---

## ★★★ Research-oriented

**★★★9.** Implement a small index-notation engine: functions that take an
expression written as a string of indexed factors and a stated index range,
identify free and summed indices, and evaluate the contraction numerically.
Verify it against matrix multiplication, the trace and a quadratic form, and
report at least two classes of expression it must reject rather than evaluate
(justify each rejection).

---

**★★★10.** Take the isotropic constitutive law in the form
$\sigma_{ij} = \lambda u_{k,k}\delta_{ij} + \mu(u_{i,j} + u_{j,i})$ and expand it
component by component for $i,j \in \{1,2\}$ as if the problem were
two-dimensional. State which contractions change, what $\delta_{ii}$ becomes, and
what a three-dimensional code would compute instead. Your answer should identify
the specific terms that differ.
