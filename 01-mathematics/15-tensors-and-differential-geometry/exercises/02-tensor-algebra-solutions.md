# Solutions — 01-15-02 Tensor Algebra, Transformation Laws and Invariants

> **Read this after attempting the exercises, not before.**
>
> These are *worked solutions*. Every numeric value was computed and checked;
> where a value depends on the rotation used, the rotation is stated.

---

## ★1 — Rotating a vector and a rank-2 tensor

**(a)** $v'_i = Q_{ij}v_j$:

$$v'_1 = 0.8660254\cdot3 + (-0.5)(-1) + 0\cdot2.5 = 3.0980762,$$
$$v'_2 = 0.5\cdot3 + 0.8660254\cdot(-1) + 0 = 0.6339746,$$
$$v'_3 = 2.5.$$

**(b)** $\lvert\mathbf{v}\rvert = \sqrt{9 + 1 + 6.25} = \sqrt{16.25} = 4.0311289$;
$\lvert\mathbf{v}'\rvert = \sqrt{3.0980762^2 + 0.6339746^2 + 2.5^2} = 4.0311289$. A
rotation preserves length, as $Q^{\mathsf T}Q = I$ requires.

**(c)** $T' = QTQ^{\mathsf T}$:

$$T' = \begin{pmatrix} 9.8481 & -0.2010 & -0.1340\\ -0.2010 & 3.1519 & 2.2321\\
-0.1340 & 2.2321 & -4.0000\end{pmatrix}.$$

The index form gives the same matrix to $1.1\times10^{-15}$, which is the
floating-point level; the two forms are the same statement, one written for a
computer and one written for a person.

---

## ★2 — Invariants and eigenvalues

$$I_1 = \operatorname{tr}T = 8 + 5 - 4 = 9,$$

$$I_2 = \tfrac{1}{2}\left[(\operatorname{tr}T)^2 - T_{ij}T_{ji}\right]
= \tfrac{1}{2}\left[81 - (64 + 9 + 1 + 25 + 4 + 16 + 1 + 4 + 16)\right]
= \tfrac{1}{2}\left[81 - 140\right] = -26,$$

$$I_3 = \det T = -173.$$

The eigenvalues are $-4.6398055434$, $3.7826295794$ and $9.857175964$, and the
elementary symmetric functions reproduce the invariants:

| Invariant | From components | From eigenvalues |
|---|---|---|
| $I_1$ | $9$ | $-4.6398055 + 3.7826296 + 9.8571760 = 9$ |
| $I_2$ | $-26$ | $(-4.6398055)(3.7826296) + (3.7826296)(9.8571760) + (9.8571760)(-4.6398055) = -26$ |
| $I_3$ | $-173$ | $(-4.6398055)(3.7826296)(9.8571760) = -173$ |

All equal to the precision shown. **This is the practical meaning of
"invariant":** three numbers per tensor that do not depend on the frame, and the
rest of the information is the orientation of the principal axes.

---

## ★3 — Which arrays are tensors

**(a) $\delta_{ij}$: yes, and it is the only rank-2 isotropic tensor (up to
scale).**

$$\delta'_{ij} = Q_{ip}Q_{jq}\delta_{pq} = Q_{ip}Q_{jp} = \delta_{ij}.$$

Verified numerically over 200 random rotations: the largest change is
$1.1\times10^{-15}$.

**(b) The engineering-shear array: no.** The array with $0.02$ in place of
$e_{12} = 0.01$ does not obey the rank-2 law. Under a $30^\circ$ rotation about
$z$, the correct engineering array is

$$\begin{pmatrix} -0.0086603 & 0.0100 & 0\\ 0.0100 & 0.0086603 & 0\\ 0&0&0
\end{pmatrix},$$

whereas rotating the array componentwise gives

$$\begin{pmatrix} -0.0173205 & 0.0100 & 0\\ 0.0100 & 0.0173205 & 0\\ 0&0&0
\end{pmatrix}:$$

the diagonal entries differ by a factor of two, and the largest discrepancy is
$0.0086603$. The array is not a tensor; it is a *storage convention* for the
components of one, and it must be converted (halve the shear entries) before any
transformation.

**(c) $\varepsilon_{ijk}$ under a proper rotation: yes, in the sense that the
components are unchanged**, because a proper rotation has $\det Q = +1$ and the
transformed components coincide with the original ones. It is nevertheless a
*pseudo-tensor*, not an ordinary one, for the reason in (d).

**(d) $\varepsilon_{ijk}$ under a reflection: no.** With the reflection
$\operatorname{diag}(1,1,-1)$ the component $\varepsilon_{123}$ transforms to
$-1$: the maximal difference is $2$, i.e. sign reversal on every non-zero
component. This is why the cross product of two vectors is a pseudo-vector, and
why angular velocity, vorticity and (as a vector) the magnetic field behave
differently from ordinary vectors under a change of handedness.

---

## ★4 — Antisymmetric tensor to axial vector

$$w_i = -\tfrac{1}{2}\varepsilon_{ijk}W_{jk}.$$

Component by component:

$$w_1 = -\tfrac{1}{2}\left(\varepsilon_{123}W_{23} + \varepsilon_{132}W_{32}\right)
= -\tfrac{1}{2}\left((-0.7) - (0.7)\right) = 0.7,$$

$$w_2 = -\tfrac{1}{2}\left(\varepsilon_{231}W_{31} + \varepsilon_{213}W_{13}\right)
= -\tfrac{1}{2}\left((-2) - (2)\right) = 2.0,$$

$$w_3 = -\tfrac{1}{2}\left(\varepsilon_{312}W_{12} + \varepsilon_{321}W_{21}\right)
= -\tfrac{1}{2}\left((-1.5) - (1.5)\right) = 1.5.$$

So $\mathbf{w} = (0.7, 2.0, 1.5)$. Reconstructing,
$W_{ij} = -\varepsilon_{ijk}w_k$ returns the original matrix exactly
(maximal discrepancy $0.0$), and under a rotation about $z$ the extracted $w$
transforms as $\mathbf{w}' = Q\mathbf{w}$ — verified numerically to
$10^{-16}$. Under a reflection it would acquire an extra sign, which is the
pseudo-vector statement of ★3(d).

---

## ★5 — Symmetry is preserved

Let $T_{ij} = T_{ji}$. Then

$$T'_{ij} = Q_{ip}Q_{jq}T_{pq} = Q_{jq}Q_{ip}T_{qp} = T'_{ji},$$

using (i) the renaming of the dummy indices $p \leftrightarrow q$ in the second
step, which is always allowed, and (ii) $T_{pq} = T_{qp}$ in the third. For
antisymmetry the identical argument with $T_{pq} = -T_{qp}$ gives
$T'_{ij} = -T'_{ji}$.

**Why this matters.** Symmetry of the stress tensor is a physical statement
(balance of angular momentum), and this result is what makes it a statement about
the *material* rather than about the coordinate system: if you verify
$\sigma_{ij} = \sigma_{ji}$ in one frame, you have verified it in all of them.

---

## ★6 — The trace is invariant, a component is not

$$T'_{ii} = Q_{ip}Q_{iq}T_{pq} = \delta_{pq}T_{pq} = T_{ii},$$

using $Q_{ip}Q_{iq} = \delta_{pq}$ (orthogonality). Trace invariance is a one-line
consequence of the transformation law, and it holds for every tensor with two
indices that can be contracted.

A single component has no such protection. For the $30^\circ$ rotation of ★1,
$T'_{11} = 9.8481$ against $T_{11} = 8$: a change of $1.8481$. Rotating by a
further $30^\circ$ changes it again. The largest change of a diagonal component
over 200 random rotations in the demonstration was $13.78$, while the three
invariants moved by less than $3\times10^{-13}$.

**Why no argument of the ★5 type can prove a single component invariant:** the
proof for the trace used the *contraction* $Q_{ip}Q_{iq} = \delta_{pq}$. With only
one index contracted, the transformation matrix survives and the expression
depends on the frame. Invariance requires every index to be contracted — which is
exactly the definition of a scalar.

---

## ★7 — The two isotropic rank-4 tensors are independent

$$I_{ijkl} = \delta_{ij}\delta_{kl}, \qquad
J_{ijkl} = \tfrac{1}{2}\left(\delta_{ik}\delta_{jl} + \delta_{il}\delta_{jk}\right).$$

Contract the first pair of indices in each:

$$I_{iikl} = \delta_{ii}\delta_{kl} = 3\delta_{kl}, \qquad
J_{iikl} = \tfrac{1}{2}\left(\delta_{ik}\delta_{il} + \delta_{il}\delta_{ik}\right)
= \tfrac{1}{2}\left(\delta_{kl} + \delta_{kl}\right) = \delta_{kl}.$$

The two contractions give **different multiples of $\delta_{kl}$**, and that
difference is what proves independence: no single scalar multiple of one can
reproduce the other, since a multiple $\alpha I$ would contract to $3\alpha\delta$
and a multiple $\beta J$ to $\beta\delta$, so equality would require
$3\alpha = \beta$ *and* $\alpha = \beta$, i.e. $\alpha = \beta = 0$.

**Physical reading.** $I_{ijkl}$ is the "pure volumetric" projector: it responds
only to the trace of the strain. $J_{ijkl}$ is the "deviatoric-and-shear" part,
contracting to $\delta_{kl}$, i.e. it does couple to the trace. Their relative
weight is what turns into $\lambda$ and $\mu$ (equivalently $K$ and $\mu$), and
the count of exactly two independent constants for an isotropic elastic solid
follows. The demonstration measures the rank of the fixed space of a small
generating set of rotations and finds 2, which is the same statement computed
rather than argued.

---

## ★8 — The engineering trap, quantified

**(a)** With $Q = R_z(30^\circ)$ and $e$ the pure shear,

$$e' = QeQ^{\mathsf T} = \begin{pmatrix} -0.0086603 & 0.0050 & 0\\ 0.0050 &
0.0086603 & 0\\ 0&0&0\end{pmatrix}.$$

The engineering array of the same tensor has $\gamma'_{12} = 2e'_{12} = 0.0100$
and diagonal entries unchanged:

$$\begin{pmatrix} -0.0086603 & 0.0100 & 0\\ 0.0100 & 0.0086603 & 0\\ 0&0&0
\end{pmatrix}.$$

**(b)** Rotating the *engineering array* componentwise (i.e. treating $0.02$ as a
tensor component) gives

$$\begin{pmatrix} -0.0173205 & 0.0100 & 0\\ 0.0100 & 0.0173205 & 0\\ 0&0&0
\end{pmatrix}.$$

Largest discrepancy against the correct array: $0.0086603$, i.e. a factor of two
on the diagonal entries. The reason is transparent: the array with $2e_{12}$ is a
*scaled* version of the tensor with one entry doubled, and rotations mix the
doubled entry with the ordinary ones, so the rescaling cannot commute with the
rotation.

**(c)** Second invariant:

| Array | $I_2$ |
|---|---|
| strain tensor $e$ | $-0.000100$ |
| engineering array | $-0.000400$ |
| rotated strain $e'$ | $-0.000100$ |
| componentwise-rotated engineering array | $-0.000400$ |

Each array's $I_2$ is preserved by its own rotation — the componentwise rotation
of the engineering array is a rotation of a *different* tensor, so it is
internally consistent — but the engineering array's $I_2$ is four times the true
strain invariant, because $I_2$ is quadratic in the shear entries. Any invariant
computed from an engineering array is wrong by a factor, and the factor depends
on how many shear components participate.

**The rule.** Convert to scientific strain, transform, convert back. Never
transform an engineering array.

---

## ★9 — A non-symmetric matrix: invariants and norms

$$A = \begin{pmatrix} 0&-1&0\\1&0&0\\0&0&2\end{pmatrix}.$$

**Characteristic polynomial.** The matrix acts as a $90^\circ$ rotation in the
$(x,y)$ plane and as multiplication by 2 along $z$, so the eigenvalues are
$i$, $-i$ and $2$. Directly:

$$I_1 = \operatorname{tr}A = 2, \qquad
I_2 = \tfrac{1}{2}\left[(\operatorname{tr}A)^2 - A_{ij}A_{ji}\right]
= \tfrac{1}{2}\left[4 - (-2)\right] = 1, \qquad
I_3 = \det A = 2.$$

Check against the eigenvalues: $i + (-i) + 2 = 2$; $i(-i) + i\cdot2 + (-i)\cdot2 =
1 + 0 = 1$; $i\cdot(-i)\cdot2 = 2$. All three agree.

**Frobenius decomposition.**

$$S = \begin{pmatrix} 0&0&0\\0&0&0\\0&0&2\end{pmatrix}, \qquad
W = \begin{pmatrix} 0&-1&0\\1&0&0\\0&0&0\end{pmatrix},$$

$$A_{ij}A_{ij} = 6, \qquad S_{ij}S_{ij} = 4, \qquad W_{ij}W_{ij} = 2, \qquad
4 + 2 = 6.$$

Under a rotation by $30^\circ$ about $z$: $A_{ij}A_{ij} = 6$,
$S_{ij}S_{ij} = 4$, $W_{ij}W_{ij} = 2$, and the three polynomial invariants
remain $2$, $1$ and $2$. All preserved.

**Why the decomposition works, and what is not invariant.** The identity
$A_{ij}A_{ij} = S_{ij}S_{ij} + W_{ij}W_{ij}$ holds because the cross term
$S_{ij}W_{ij}$ vanishes identically: $S$ is symmetric, $W$ antisymmetric, and
their double contraction is zero — the same argument as ★8 of
[01-15-01](./01-index-notation-solutions.md). Because $S$ and $W$ live in
orthogonal subspaces that are each invariant under rotations, each norm is
separately invariant. That is extra information beyond the three polynomial
invariants, and it is specific to *orthogonal* transformations: a general linear
change of basis preserves the eigenvalues and the three invariants but not the
split into symmetric and antisymmetric parts.

**What reality of the eigenvalues requires.** Symmetry (or, over the complex
numbers, Hermiticity). The matrix above is a rotation generator: its complex
eigenvalues $e^{\pm i\pi/2}$ have modulus one, and no real eigenvector exists in
the rotation plane. Physically, this is the difference between a stress tensor
(always diagonalisable with real eigenvalues) and a rotation or a strain-rate-like
operator (generally not).

---

## ★10 — Hexagonal versus tetragonal, by rotation

Use the VTI constants $C_{11} = 30$, $C_{33} = 22$, $C_{44} = 7$, $C_{66} = 10$,
$C_{13} = 12$ GPa, with the constraint $C_{12} = C_{11} - 2C_{66} = 10$ GPa in
the first matrix and $C_{12} = 20$ GPa in the second. Both have the same zero
pattern.

Rotating the full rank-4 tensor by $60^\circ$ about $z$:

| Matrix | max $\lvert C'_{ijkl} - C_{ijkl}\rvert$ | relative |
|---|---|---|
| $C_{12} = 10$ GPa | $1.907\times10^{-6}$ GPa | $6.4\times10^{-17}$ |
| $C_{12} = 20$ GPa | $3.750\times10^{9}$ GPa | $1.3\times10^{-1}$ |

(In SI these are the same numbers with a factor $10^9$; the relative column is
the meaningful one.) The first is invariant to round-off — it is hexagonal. The
second changes by 13 per cent of its own scale under a symmetry operation of the
group it is supposed to belong to, so it is not hexagonal at all; it has
*tetragonal* symmetry, which is a larger group with six independent constants.

**What goes wrong in practice.** A hexagonal tensor is invariant under any
rotation about its axis; a tetragonal one only under multiples of $90^\circ$. If
the second matrix is used as a hexagonal stiffness:

- Wave speeds computed for propagation directions separated by less than
  $90^\circ$ in azimuth will disagree with one another by amounts of order the
  anisotropy — of order 10 per cent in velocity here — even though the medium is
  supposed to be azimuthally isotropic about the axis.
- Shear-wave splitting for propagation along the axis would vanish in a真正的
  hexagonal medium, but acquires a spurious azimuthal dependence.
- An inversion that assumes hexagonal symmetry and recovers these constants would
  be fitting a model that cannot represent the data, and the residual would be
  attributed to noise rather than to a wrong symmetry assumption.

The check is cheap and should always be run: build the full tensor, rotate it by
an element of the claimed symmetry group, and compare. Picking $C_{12}$ to
satisfy $C_{12} = C_{11} - 2C_{66}$ is part of the definition of the hexagonal
class, not an optional cosmetic detail.

---

## Self-assessment: have you actually learned this?

- [ ] I can rotate a vector and a tensor by hand and check the invariants.
- [ ] I can compute $I_1, I_2, I_3$ from components and from eigenvalues and get
      the same numbers.
- [ ] I can decide whether an array is a tensor by testing the law, and I can
      name the two arrays of ★3 that fail.
- [ ] I can extract an axial vector and state what changes under a reflection.
- [ ] I can prove trace invariance in one line and explain why the same proof
      cannot work for a single component.
- [ ] I can show $I_{ijkl}$ and $J_{ijkl}$ are independent by contracting.
- [ ] I can quantify the engineering-shear error under rotation, including the
      factor of four in $I_2$.
- [ ] I can explain what the Frobenius split into symmetric and antisymmetric
      norms buys, and what it does not.
- [ ] I can demonstrate hexagonal-versus-tetragonal by a rotation test rather than
      by looking at the pattern of zeros.
