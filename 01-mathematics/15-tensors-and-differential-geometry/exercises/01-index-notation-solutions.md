# Solutions — 01-15-01 Index Notation, Einstein Summation and Kronecker Delta

> **Read this after attempting the exercises, not before.**
>
> These are *worked solutions*, showing a valid route and the reasoning. They are
> not the only correct route. Every numeric value below was computed and checked
> rather than estimated by hand.

---

## ★1 — Translating between index and matrix form

| | Index form | Matrix/vector form |
|---|---|---|
| (a) | $A_{ij}x_j$ | $A\mathbf{x}$ |
| (b) | $x_iy_i$ | $\mathbf{x}\cdot\mathbf{y}$ |
| (c) | $A_{ii}$ | $\operatorname{tr}A$ |
| (d) | $\varepsilon_{ijk}A_{1i}A_{2j}A_{3k}$ | $\det A$ |
| (e) | $F_{i,i}$ | $\nabla\cdot\mathbf{F}$ |
| (f) | $A_{ij}B_{jk}$ | $AB$ (the product matrix) |
| (g) | $\varepsilon_{ijk}a_jb_k$ | $\mathbf{a}\times\mathbf{b}$ |
| (h) | $u_{i,i}$ | $\nabla\cdot\mathbf{u}$ |
| (i) | $\sigma_{ij}n_j$ | $\boldsymbol{\sigma}\mathbf{n}$, the traction |
| (j) | $T_{ij}n_in_j$ | $\mathbf{n}^{\mathsf T}T\mathbf{n}$ |

**Note on (j).** $T_{ij}n_in_j$ has no free indices, so it is a scalar. It is the
quadratic form $\mathbf{n}^{\mathsf T}T\mathbf{n}$, and if $T$ is symmetric it is
unchanged when the antisymmetric part of $T$ is removed — the argument of ★8.

---

## ★2 — Free and dummy indices

| | Expression | Free indices | Summed | Verdict |
|---|---|---|---|---|
| (a) | $a_ib_i$ | none (scalar) | $i$ | valid |
| (b) | $a_ib_j$ | $i,j$ (a rank-2 object) | none | valid |
| (c) | $A_{ii}B_{jj}$ | none | $i$ and $j$, separately | valid |
| (d) | $A_{ij}B_{jk}C_{ki}$ | none, after summation | $i,j,k$ | valid |
| (e) | $a_i + b_i$ | $i$ | none | valid (three equations) |
| (f) | $A_{ii} + B_{ii}$ | none | $i$ in each term | valid |
| (g) | $A_{ij}B_{jk}C_k$ | $i$ | $j$ and $k$ | valid, a vector |
| (h) | $\delta_{ij}a_ib_j$ | none | $i,j$ | valid, equals $a_ib_i$ |
| (i) | $\varepsilon_{ijk}a_ia_j$ | $k$ | $i,j$ | valid but identically zero |
| (j) | $A_{ij}B_{ij}$ | none | $i$ and $j$ | valid, a double sum |

**The interesting rows.**

- (c) is valid and is *not* a double contraction: $A_{ii}$ and $B_{jj}$ are separate
  traces, and $A_{ii}B_{jj} = (\operatorname{tr}A)(\operatorname{tr}B)$. Writing
  $A_{ii}B_{ii}$ would be invalid, because $i$ cannot be summed twice.
- (i) is valid but always zero: $\varepsilon_{ijk}$ is antisymmetric under
  $i \leftrightarrow j$ while $a_ia_j$ is symmetric, so the two factors cancel in
  pairs. This is the same argument as ★8.
- (h) is a case where the delta can be eliminated in two ways:
  $\delta_{ij}a_ib_j = a_ib_i = \mathbf{a}\cdot\mathbf{b}$.

---

## ★3 — The two symbols

**(a)** $\delta_{ij}a_j = a_i$, so the three components are
$(4,\ -2,\ 7)$: only the term with $j = i$ survives.

**(b)** $\delta_{ii} = \delta_{11} + \delta_{22} + \delta_{33} = 3$. This is the
number of dimensions; in a two-dimensional problem it is 2.

**(c)** $\delta_{ij}\delta_{jk} = \delta_{ik}$: the first delta substitutes $j = i$,
then the second substitutes $j = k$; equivalently, the product of two identity
matrices is the identity.

**(d)** $\varepsilon_{ijk}\varepsilon_{ijk} = 6$. Six ordered triples of distinct
indices contribute $(\pm1)^2 = 1$.

**(e)** $\varepsilon_{123} = +1$ (even permutation).

**(f)** $\varepsilon_{213} = -1$ (one swap).

**(g)** $\varepsilon_{112} = 0$ (repeated index).

**(h)** Set $l = j$ in the identity of ★5:
$\varepsilon_{ijk}\varepsilon_{ilk} = \delta_{jj}\delta_{kl} - \delta_{jl}\delta_{kj}
= 3\delta_{kl} - \delta_{kl} = 2\delta_{kl}$, i.e. $2\delta_{jl}$ in the notation
of the question. Numerically: with $(j,l) = (1,1)$ the contraction gives 2; with
$(j,l) = (1,2)$ it gives 0 — both confirmed by direct enumeration.

---

## ★4 — Worked numbers

**(a)** $A_{ii} = 1 + 5 + 9 = 15$.

**(b)** $A_{ij}x_j$ has components
$(1\cdot1 + 2\cdot(-1) + 3\cdot2,\ 4 - 5 + 12,\ 7 - 8 + 18) = (5,\ 11,\ 17)$.

**(c)** $A_{ij}x_ix_j = \mathbf{x}^{\mathsf T}A\mathbf{x} = \mathbf{x}\cdot(A\mathbf{x})
= 1\cdot5 + (-1)\cdot11 + 2\cdot17 = 28$.

**(d)** $A_{ij}A_{ij} = 1+4+9+16+25+36+49+64+81 = 285$: a nine-term sum of squares,
which is **not** the trace.

**(e)** $A_{ij}A_{ji} = \operatorname{tr}(A^2)$:
$1\cdot1 + 2\cdot4 + 3\cdot7 + 4\cdot2 + 5\cdot5 + 6\cdot8 + 7\cdot3 + 8\cdot6 + 9\cdot9
= 261$.

Compare (d) and (e): $285$ and $261$. For a symmetric matrix they would be equal;
the difference measures the antisymmetric part, and it is exactly
$W_{ij}W_{ji}$ up to sign. This is the numerical form of the warning in Section 8
of the lesson: $A_{ij}A_{ij}$ and $A_{ij}A_{ji}$ are different contractions.

**(f)** $\det A = 0$. The rows are in arithmetic progression, so row 3 = 2·row 2 −
row 1 and the matrix is singular. A useful reminder that a tensor can be
non-invertible — a strain state with zero determinant is not possible, but a
stiffness state can be degenerate.

**(g)**

$$S_{ij} = \begin{pmatrix} 1&3&5\\3&5&7\\5&7&9\end{pmatrix}, \qquad
W_{ij} = \begin{pmatrix} 0&-1&-2\\1&0&-1\\2&1&0\end{pmatrix}.$$

Check: $S + W = A$ (evident), $W_{ii} = 0$, and
$W_{ij}x_ix_j = 0.0$ exactly for the $\mathbf{x}$ above — the antisymmetric part
of a quadratic form is always zero.

---

## ★5 — The epsilon-delta identity

**Claim.** $\varepsilon_{ijk}\varepsilon_{ilm} = \delta_{jl}\delta_{km} -
\delta_{jm}\delta_{kl}$.

**Proof by cases.**

*Case $j = k$.* The left side contains $\varepsilon_{ijk}$ with a repeated index
and vanishes. The right side is $\delta_{jl}\delta_{jm} - \delta_{jm}\delta_{jl}
= 0$, since the two products are identical. Both sides vanish.

*Case $j \neq k$.* The sum over $i$ then has exactly one non-zero term: the one in
which $i = i_0$ is the third value, distinct from $j$ and $k$. Then
$\varepsilon_{i_0jk} = \pm 1$. The second epsilon,
$\varepsilon_{i_0lm}$, is non-zero only if $\{l,m\} = \{j,k\}$; if
$\{l,m\} \neq \{j,k\}$ then both sides are zero.

It remains to check the two orderings:

| $(l,m)$ | left side | right side |
|---|---|---|
| $(j,k)$ | $\varepsilon_{i_0jk}^2 = 1$ | $\delta_{jj}\delta_{kk} - \delta_{jk}\delta_{kj} = 1 - 0 = 1$ |
| $(k,j)$ | $\varepsilon_{i_0jk}\varepsilon_{i_0kj} = -1$ | $\delta_{jk}\delta_{kj} - \delta_{jj}\delta_{kk} = 0 - 1 = -1$ |

Both sides agree in every case. $\square$

**Contractions.** Setting $l = j$:

$$\varepsilon_{ijk}\varepsilon_{ijm} = \delta_{jj}\delta_{km} - \delta_{jm}\delta_{kj}
= 3\delta_{km} - \delta_{km} = 2\delta_{km}.$$

Setting $m = k$ in that result:

$$\varepsilon_{ijk}\varepsilon_{ijk} = 2\delta_{kk} = 6.$$

The value 6 is $3!$: the number of permutations of three symbols, which is what
the symbol is counting.

---

## ★6 — The two structural identities

**(a) $\nabla\cdot(\nabla\times\mathbf{F}) = 0$.** In index form the object is
$\varepsilon_{ijk}F_{k,ji}$. Swap the names of the dummy indices $i$ and $j$:

$$\varepsilon_{ijk}F_{k,ji} = \varepsilon_{jik}F_{k,ij}
= -\varepsilon_{ijk}F_{k,ij} = -\varepsilon_{ijk}F_{k,ji}.$$

The second step uses antisymmetry of $\varepsilon$, the third uses
$F_{k,ij} = F_{k,ji}$, i.e. **equality of mixed partial derivatives**, which
requires $F$ to be twice continuously differentiable. A quantity equal to its own
negative is zero. $\square$

**(b) $\nabla\times(\nabla f) = \mathbf{0}$.** Component $i$ is
$\varepsilon_{ijk}f_{,kj}$. Swapping $j \leftrightarrow k$:
$f_{,kj} = f_{,jk}$ (symmetry) and $\varepsilon_{ikj} = -\varepsilon_{ijk}$
(antisymmetry), so the expression equals its own negative. $\square$

**The numerical caveat.** Both identities are *algebraic*. When a central
difference is used, the mixed differences in (b) cancel digit for digit and the
computed residual is exactly zero — not because the field is curl-free, but
because the stencil is symmetric. A zero residual there therefore proves nothing
about the code; it only proves the stencil is symmetric. Contrast the check of
(a) on a field with genuinely non-cancelling terms, where the residual sits at
the truncation level ($\sim10^{-12}$ for $h = 10^{-4}$) and *is* informative.

---

## ★7 — Isotropic stiffness, expanded step by step

Start from

$$C_{ijkl} = \lambda\delta_{ij}\delta_{kl} +
\mu\left(\delta_{ik}\delta_{jl} + \delta_{il}\delta_{jk}\right)$$

and contract with $u_{k,l}$:

$$\sigma_{ij} = \lambda\underbrace{\delta_{ij}\delta_{kl}u_{k,l}}_{(1)}
+ \mu\underbrace{\delta_{ik}\delta_{jl}u_{k,l}}_{(2)}
+ \mu\underbrace{\delta_{il}\delta_{jk}u_{k,l}}_{(3)}.$$

Term by term:

1. $\delta_{ij}\delta_{kl}u_{k,l} = \delta_{ij}\,u_{k,k}$: the inner contraction is
   the divergence, and the outer delta leaves it as an isotropic contribution.
2. $\delta_{ik}\delta_{jl}u_{k,l} = u_{i,j}$: the first delta sets $k = i$, the
   second sets $l = j$.
3. $\delta_{il}\delta_{jk}u_{k,l} = u_{j,i}$: the first delta sets $l = i$, the
   second sets $k = j$.

Collecting:

$$\sigma_{ij} = \lambda u_{k,k}\delta_{ij} + \mu\left(u_{i,j} + u_{j,i}\right)
= \lambda u_{k,k}\delta_{ij} + 2\mu e_{ij}, \qquad
e_{ij} = \tfrac{1}{2}\left(u_{i,j} + u_{j,i}\right). \tag{S1}$$

Two checks. First, contracting with $\delta_{ij}$:
$\sigma_{ii} = 3\lambda u_{k,k} + 2\mu e_{ii} = (3\lambda + 2\mu)u_{k,k}$, and the
coefficient three comes from $\delta_{ii} = 3$, not from any property of the rock.
Second, the antisymmetric part of $u_{k,l}$ cancels between terms 2 and 3 of the
contraction, which is why the symmetric form $2\mu e_{ij}$ is legitimate.

---

## ★8 — The antisymmetric part cannot store energy

Let $\sigma_{ij} = \sigma_{ji}$ and $\omega_{ij} = -\omega_{ji}$. Then

$$\sigma_{ij}\omega_{ij} = -\sigma_{ji}\omega_{ji} = -\sigma_{ij}\omega_{ij},$$

where the first step renames the dummy indices and uses both symmetries, and the
second renames them back. A number equal to its own negative is zero, so
$\sigma_{ij}\omega_{ij} = 0$ identically.

**Physical reading.** The rate of working of the stress on the deformation is
$\sigma_{ij}\dot e_{ij}$, and the rotation part of the velocity gradient
contributes nothing to it. A rigid rotation of a stressed body changes the
orientation of the stress field but does work on nothing; it cannot store elastic
energy, and no strain energy can depend on $\omega_{ij}$. Equivalently: the
symmetric and antisymmetric parts of a second-rank object are orthogonal under the
double contraction, so a symmetric stress cannot "see" a rotation.

Numerically, $W_{ij}x_ix_j = 0.0$ exactly for the antisymmetric matrix of ★4(g),
and $x_iA_{ij}x_j = x_iS_{ij}x_j$.

---

## ★9 — An index-notation engine

A minimal implementation needs four steps, in this order:

1. **Parse** each term into factors, each factor being a name and a list of
   indices (upper/lower not distinguished in Cartesian work).
2. **Classify** indices: count occurrences across the term's factors. A count of
   1 is free; a count of 2 is summed; a count of 3 or more is an error.
3. **Check term consistency**: every term in a sum must have the same set of free
   indices, and both sides of an equation must agree.
4. **Evaluate** by nested loops over the free indices (outer) and the summed
   indices (inner), building the result.

Two classes of expression that must be rejected rather than evaluated:

- **An index appearing three times, e.g. $A_{ii}B_{ii}$.** There is no
  convention that makes this a tensor expression; accepting it would silently
  invent a meaning (sum over $i$ once or twice?) and any number it returned would
  be convention-dependent. The engine must raise an error.
- **A term whose free-index set differs from the others in the same equation,
  e.g. $c_i = A_{ij}b_j + d_k$.** The equation is not a valid component
  statement, because the left side has one free index and the second term has a
  different one. Rejection is required; the "obvious" fix (sum over $k$) is not
  determined by the expression.

A third failure mode is worth handling explicitly: **a stated index range that is
not the one used in the derivation.** If the range is set to $\{1,2\}$ while the
expression contains $\delta_{ii}$, the engine returns 2 instead of 3, which is
correct arithmetic and wrong physics. The range must be an explicit argument, not
a global constant.

---

## ★10 — Expanding the isotropic law in two dimensions

Take the three-dimensional expansion (S1),

$$\sigma_{ij} = \lambda u_{k,k}\delta_{ij} + \mu\left(u_{i,j} + u_{j,i}\right),$$

and evaluate it for $i,j \in \{1,2\}$ with the understanding that the *body* is
still three-dimensional. Two distinct 2-D problems arise, and they differ.

**Plane strain** ($u_3 = 0$ and no $x_3$ dependence). Then $u_{k,k} = u_{1,1} +
u_{2,2} \equiv \Delta_2$, and

$$\sigma_{11} = \lambda\Delta_2 + 2\mu u_{1,1}, \qquad
\sigma_{22} = \lambda\Delta_2 + 2\mu u_{2,2}, \qquad
\sigma_{12} = \mu\left(u_{1,2} + u_{2,1}\right),$$

$$\sigma_{33} = \lambda\Delta_2 \neq 0.$$

The in-plane relations look exactly like the 3-D ones with the same $\lambda$ and
$\mu$, but the out-of-plane stress is non-zero and a 2-D code that needs it must
compute it. The trace contraction changes: $\sigma_{kk}$ over the three
dimensions is $(3\lambda + 2\mu)\Delta_2$; over the two in-plane dimensions, with
$\delta_{ii} = 2$, it is $(2\lambda + 2\mu)\Delta_2$. With
$\lambda = 30$ GPa, $\mu = 20$ GPa these are $130\Delta_2$ and $100\Delta_2$
GPa: the coefficient is **not** obtained from the 3-D one.

**Plane stress** ($\sigma_{33} = 0$, a thin sheet). Eliminating $u_{3,3}$ gives an
effective in-plane stiffness

$$\lambda^\star = \frac{2\lambda\mu}{\lambda + 2\mu} = \frac{2\cdot30\cdot20}{70}
= 17.142857\ \text{GPa},$$

i.e. $17.143$ GPa against the 3-D $\lambda = 30$ GPa — a factor of 1.75. The
failure of the naive 2-D model is not a small correction.

**The specific terms that differ.** The list is short and worth memorising:

| Quantity | 3-D | 2-D plane strain | 2-D plane stress |
|---|---|---|---|
| $\delta_{ii}$ | 3 | 2 | 2 |
| in-plane trace coefficient | $3\lambda + 2\mu = 130$ | $2\lambda + 2\mu = 100$ | $2(\lambda^\star + \mu) = 74.286$ |
| $\lambda$ in the constitutive law | 30 | 30 (plus $\sigma_{33}$) | $\lambda^\star = 17.143$ |
| shear modulus $\mu$ | 20 | 20 | 20 |
| $P$-wave speed at $\rho = 2400$ kg m$^{-3}$ | 5400.617 m s$^{-1}$ | 5400.617 m s$^{-1}$ | 4879.500 m s$^{-1}$ |

(The plane-stress $P$ speed uses $v_p = \sqrt{E/(\rho(1-\nu^2))}$ with
$E = 52.0$ GPa and $\nu = 0.3$ for this material; the plane-strain speed is
unchanged because the in-plane $\lambda + 2\mu$ combination does not change.)

**The lesson.** A contraction's value depends on the range, and the range depends
on the physical problem, not on how many components you chose to store. Any
"2-D" elastic code must state which 2-D problem it solves.

---

## Self-assessment: have you actually learned this?

- [ ] I got ★1 and ★2 completely right, including the invalid cases.
- [ ] I computed ★3 and ★4 without writing out sums by hand more than once.
- [ ] I can reproduce the case proof of ★5 from memory and see why the
      $j = k$ case is trivial.
- [ ] I can prove both identities of ★6 and can state the differentiability
      assumption in each.
- [ ] I can expand ★7 in one pass, tracking which delta sets which index.
- [ ] I can explain ★8 physically, not just algebraically.
- [ ] I can state two expressions that must be rejected by an index-notation
      engine, and why rejection (not evaluation) is the correct behaviour.
- [ ] I can say what changes in the constitutive law when the problem is
      two-dimensional, and give a number for at least one changed coefficient.
