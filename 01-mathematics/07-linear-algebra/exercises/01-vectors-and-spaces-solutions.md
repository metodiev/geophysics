# Solutions — 01-07-01 Vectors, Vector Spaces and Basis

> **Read this after attempting the exercises, not before.**
>
> These are *worked solutions*, showing a valid route and the reasoning. They are
> not the only correct route. Where a numeric answer is given, it was computed and
> verified numerically. Several problems have more than one defensible answer;
> where that is true it is stated explicitly.

---

## ★1 — Norms, inner product, angle

$$a = (2,-1,2), \quad b = (1,3,-2).$$

$$\|a\| = \sqrt{4+1+4} = 3, \qquad \|b\| = \sqrt{1+9+4} = \sqrt{14} = 3.741657,$$

$$\langle a,b\rangle = 2 - 3 - 4 = -5, \qquad
\theta = \arccos\frac{-5}{3\sqrt{14}} = 116.451199^{\circ} ,$$

$$\|a+b\| = \|(3,2,0)\| = \sqrt{13} = 3.605551, \qquad
\|a-b\| = \|(1,-4,4)\| = \sqrt{33} = 5.744563 .$$

**Cauchy–Schwarz:** $|\langle a,b\rangle| = 5 \le \|a\|\,\|b\| = 11.224972$. Holds
with room to spare, and the angle is obtuse, which is what a negative inner product
means.

**Parallelogram identity:**
$\|a+b\|^{2} + \|a-b\|^{2} = 13 + 33 = 46$ and
$2\|a\|^{2} + 2\|b\|^{2} = 2\cdot9 + 2\cdot14 = 46$. ✓

**Key point.** The inner product is $-5$ because the vectors point in opposing
directions overall, not because they are unrelated. A correlation would subtract the
means first; an inner product does not.

---

## ★2 — Which sets are vector spaces

| Set | Vector space? | Reason |
|---|---|---|
| (a) $x + 2y - z = 0$ | **yes** | a plane through the origin: closed under addition and scaling, contains $\mathbf{0}$ |
| (b) $x + 2y - z = 1$ | **no** | contains no additive identity: $\mathbf{0}$ does not satisfy the equation |
| (c) zero-trace $2\times2$ matrices | **yes** | $\operatorname{tr}(A+B) = 0$ and $\operatorname{tr}(\alpha A) = 0$ when $\operatorname{tr}A = 0$ |
| (d) invertible $2\times2$ matrices | **no** | $I + (-I) = 0$ is not invertible; the set is not closed under addition |
| (e) profiles $a + bz$ | **yes** | a sum of two linear functions is linear, and so is a scalar multiple |

**Common trap.** (d) looks closed because every element has an inverse *within* the
set. But a vector space requires the sum of any two elements to be an element, and
two invertible matrices can sum to a singular one. This is the reason a
"non-singularity constraint" cannot be expressed by restricting the model space; it
has to enter as a penalty or a bound.

---

## ★3 — Two directions at a station

(a) $\langle v_1, v_2\rangle = 1$, $\|v_1\| = 1$, $\|v_2\| = \sqrt2$, so
$\theta = \arccos(1/\sqrt2) = 45^{\circ}$.

(b) $\hat v_1 = (1,0,0)$ with norm 1; $\hat v_2 = (1,1,0)/\sqrt2 = (0.707107,
0.707107, 0)$ with norm $\sqrt{0.5+0.5} = 1$. ✓

(c) Independent. They are not scalar multiples of one another ($v_2$ has an east
component $v_1$ lacks), so the only solution of $c_1v_1 + c_2v_2 = \mathbf{0}$ is
$c_1 = c_2 = 0$.

**Note on the geometry.** Both vectors are horizontal and $45^{\circ}$ apart in the
horizontal plane, so this pair spans the horizontal plane, not $\mathbb{R}^{3}$. The
third direction needed to complete a basis of $\mathbb{R}^{3}$ is the vertical one —
which is exactly the physical reason a three-component sensor is required.

---

## ★4 — Three-component recording, and a rotation

(a) $\|\mathbf{u}\| = \sqrt{1.2^{2} + 0.9^{2} + 1.4^{2}} = \sqrt{4.21} = 2.051828$.

Incidence angle from the vertical: the vertical amplitude is $-1.4$, so

$$\theta = \arccos\frac{|u_Z|}{\|\mathbf{u}\|} = \arccos\frac{1.4}{2.051828} = 46.974934^{\circ}.$$

Back azimuth (clockwise from north, with $E$ positive east):

$$\operatorname{atan2}(-E, N) = \operatorname{atan2}(-0.9,\ 1.2) = -36.869898^{\circ}
\equiv 323.130102^{\circ}.$$

(b) Rotating the horizontal pair $40^{\circ}$ clockwise means

$$N' = N\cos40^{\circ} + E\sin40^{\circ}, \qquad
E' = -N\sin40^{\circ} + E\cos40^{\circ},$$

giving $N' = 1.49776218$ and $E' = -0.08190513$, so
$\mathbf{u}' = (1.49776218,\ -0.08190513,\ -1.4)$. The horizontal magnitude is
$\sqrt{1.49776218^{2} + 0.08190513^{2}} = 1.50000000$, against the original
$\sqrt{1.2^{2}+0.9^{2}} = 1.5$. ✓

(c) **Invariant:** the norm $\|\mathbf{u}\| = 2.051828$, the incidence angle
$46.974934^{\circ}$ (the vertical component is untouched and the horizontal magnitude
is preserved, so their ratio is preserved), and the count of independent physical
quantities. **Not invariant:** the triple itself, and the back azimuth, which
decreases by exactly $40^{\circ}$ — from $323.130102^{\circ}$ to
$283.130102^{\circ}$, matching the computed value
$\operatorname{atan2}(0.08190513,\ 1.49776218) = 3.130102^{\circ}$, which is the
azimuth measured from the *rotation's* reference axis (the rotated north), and is
therefore the same direction expressed in the rotated frame.

(d) **Two.** Amplitude and direction. Three numbers were written down, but one degree
of freedom is the arbitrary orientation of the reference frame, which is not a
property of the ground motion.

---

## ★5 — Gram–Schmidt

$$v_1 = (1,1,1), \quad v_2 = (1,-1,0), \quad v_3 = (0,1,-1).$$

**Step 1.** $w_1 = v_1$, $\|w_1\| = \sqrt3 = 1.732051$,
$e_1 = (1,1,1)/\sqrt3 = (0.577350,\ 0.577350,\ 0.577350)$.

**Step 2.** $\langle v_2, e_1\rangle = (1-1+0)/\sqrt3 = 0$, so $w_2 = v_2$ unchanged,
$\|w_2\| = \sqrt2 = 1.414214$, $e_2 = (1,-1,0)/\sqrt2 = (0.707107,\ -0.707107,\ 0)$.

**Step 3.** $\langle v_3,e_1\rangle = (0+1-1)/\sqrt3 = 0$ and
$\langle v_3,e_2\rangle = (0-1+0)/\sqrt2 = -1/\sqrt2$, so

$$w_3 = v_3 + \tfrac{1}{\sqrt2}e_2 = (0,1,-1) + (0.5,-0.5,0) = (0.5,\ 0.5,\ -1),
\qquad \|w_3\| = \sqrt{1.5} = 1.224745 ,$$
$$e_3 = w_3/\|w_3\| = (0.408248,\ 0.408248,\ -0.816497) .$$

**Residual norms:** $\sqrt3 = 1.732051$, $\sqrt2 = 1.414214$, $\sqrt{1.5} =
1.224745$. All three are of the same size, so the set is comfortably independent.

(b) All six inner products: $\langle e_i,e_i\rangle = 1$ for $i = 1,2,3$ and
$\langle e_i,e_j\rangle = 0$ for $i \neq j$, to round-off. The construction guarantees
this; the check is that no arithmetic error crept in.

(c) Coordinates of $c = (1,2,3)$: $\langle c,e_1\rangle = 6/\sqrt3 = 3.464102$,
$\langle c,e_2\rangle = (1-2)/\sqrt2 = -0.707107$,
$\langle c,e_3\rangle = 0.408248 + 0.816497 - 2.449490 = -1.224745$. Reconstruction:

$$3.464102\,e_1 - 0.707107\,e_2 - 1.224745\,e_3 = (2 - 0.5 - 0.5,\ 2 + 0.5 - 0.5,\
2 + 0 + 1) = (1,2,3). ✓$$

(d) The smallest residual, $1.224745$, is $71$ % of $\|v_3\| = \sqrt2$, so the third
vector contributes substantial new direction. Had the smallest residual been of order
$10^{-10}$, the set would have been numerically rank-deficient at working precision
and every subsequent computation would inherit that.

(e) $v_1$ happens to be orthogonal to both others, which simplifies the arithmetic but
says nothing about the conditioning. The negative $\langle v_2,v_3\rangle = -1$ is the
only genuine coupling, and it is removed by the third projection. Gram–Schmidt does
not need orthogonality to *start*; it needs independence.

---

## ★6 — A ray-path kernel

$$r_1 = (1,1,0), \quad r_2 = (1,1,0.001), \quad r_3 = (0,0,1) \ \text{(km)}.$$

(a) **Independent.** The determinant of the matrix with these rows is $0.001 \neq 0$
(equivalently, $r_3$ has a nonzero third component that neither $r_1$ nor $r_2$
carries in a matching way, and $r_1 - r_2 = (0,0,-0.001)$ is nonzero). Rank 3.

(b) The rows become dependent exactly when $\delta = 0$: then $r_1 = r_2$ and
$\operatorname{rank} = 2$.

(c) $\langle r_1, r_2\rangle = 2 + \delta$, $\|r_1\| = \sqrt2$, and
$\|r_2\| = \sqrt{2 + 2\delta + \delta^{2}}$. At $\delta = 0.001$:

$$\theta = \arccos\frac{2.001}{\sqrt2\,\sqrt{2.002001}} = \arccos(0.99975) = 1.281^{\circ} .$$

At $\delta = 0$ the angle is exactly $0^{\circ}$. The diagnostic is ill-conditioned
because $\arccos$ has an infinite derivative at 1: a rounding error of
$\epsilon_{\text{mach}}$ in the cosine produces an angle error of
$\sqrt{2\epsilon_{\text{mach}}} \approx 2\times10^{-8}$ rad $\approx 1.2\times10^{-6}$
degrees, regardless of how near-parallel the vectors are. A stable alternative is to
measure the perpendicular residual directly: for these two rows,
$\|w_2\|/\|r_2\| = \delta/\sqrt{2} + O(\delta^{2})$, which is computed by the
orthogonalisation itself and does not lose relative accuracy. The lesson's demo shows
exactly this discrepancy: at $\delta = 10^{-9}$ the angle is reported as
$1.2\times10^{-6}$ degrees where the exact value is $2.9\times10^{-8}$.

(d) **Survey interpretation:** the third ray is the only one that distinguishes the
third cell, and the first two rays are nearly the same measurement. Two consequences:
(a) the survey has a near-null direction — the difference of cells 1 and 2 — that
$\delta = 0.001$ barely constrains, and (b) if $\delta$ were actually zero, the survey
would have a genuine null space and a redundant datum, exactly the geometry of
[01-07-04](../04-rank-and-nullspace.md). Repetition of nearly identical rays is
wasteful; that is a design conclusion drawn before any data are collected.

---

## ★★★7 — Three parameterisations of one model space

Bases: $A = \{(1,0),(0,1)\}$, $B = \{(1,0.5),(0,1)\}$, $C = \{(1,1)/\sqrt2,
(1,-1)/\sqrt2\}$, and $m = (0.05,-0.02)$ $\mathrm{s/km}$.

(a) **Coordinates.** In $A$ the coordinates are the components: $(0.05,\ -0.02)$.
In $C$ (orthonormal) they are inner products:

$$\langle m, c_1\rangle = \frac{0.05-0.02}{\sqrt2} = 0.0212132, \qquad
\langle m, c_2\rangle = \frac{0.05+0.02}{\sqrt2} = 0.0494975 .$$

In $B$ solve $m = c_1b_1 + c_2b_2$: from the first component $c_1 = 0.05$; then
$0.5(0.05) + c_2 = -0.02$ gives $c_2 = -0.045$. So the coordinates in $B$ are
$(0.05,\ -0.045)$.

Reconstructions: $A$ trivially; $B$ gives $(0.05,\ 0.025 - 0.045) = (0.05,-0.02)$ ✓;
$C$ gives $(0.0150+0.0350,\ 0.0150-0.0350) = (0.05,-0.02)$ ✓.

(b) $\|m\| = \sqrt{0.0025+0.0004} = \sqrt{0.0029} = 0.0538516$.

| basis | coordinates | Euclidean norm of coordinates | equals $\|m\|$? |
|---|---|---|---|
| $A$ | $(0.05,\ -0.02)$ | $0.0538516$ | **yes** |
| $B$ | $(0.05,\ -0.045)$ | $0.0672681$ | no |
| $C$ | $(0.0212132,\ 0.0494975)$ | $0.0538516$ | **yes** |

The distinguishing property is **orthonormality**: $A$ and $C$ are orthonormal, $B$
is not (its two vectors are orthogonal but not unit, so $\|b_1\| = \sqrt{1.25}$).
Only an orthonormal change of coordinates preserves the Euclidean norm of the
coordinate vector.

(c) Penalties $\|c\|^{2}$:

| basis | $\|c\|^{2}$ | relative to $A$ |
|---|---|---|
| $A$ | $0.0029000$ | $1.000$ |
| $B$ | $0.0045250$ | $1.560$ |
| $C$ | $0.0029000$ | $1.000$ |

The same physical model is penalised $56$ % more in basis $B$ than in $A$. **The
penalty changed and the model did not.** A minimum-norm regularisation with an
unnormalised basis is therefore optimising a different functional from the one
intended, and the difference is not a small numerical effect: it is a factor that
grows with the condition number of the basis.

(d) Write $c = P^{-1}m$. Then

$$\|c\|^{2} = m^\mathsf{T}(P^{-1})^\mathsf{T}P^{-1}m .$$

This equals $m^\mathsf{T}m$ for **all** $m$ if and only if the symmetric matrix
$(P^{-1})^\mathsf{T}P^{-1} - I$ is zero, i.e. $(P^{-1})^\mathsf{T}P^{-1} = I$, i.e.
$P^\mathsf{T}P = I$: $P$ orthogonal. (Necessity: take $m$ to be an eigenvector of
$(P^{-1})^\mathsf{T}P^{-1} - I$ with nonzero eigenvalue.) Verified in (b): $A$ and
$C$ are orthogonal transformations of one another and of the standard basis, while
$B$'s matrix $P = \begin{bmatrix} 1 & 0 \\ 0.5 & 1\end{bmatrix}$ has
$P^\mathsf{T}P = \begin{bmatrix} 1.25 & 0.5 \\ 0.5 & 1\end{bmatrix} \neq I$.

(e) **Ranking for a prior of opposition:** $C$ first, then $A$, then $B$.

- **$C$ best.** Its second vector is $(1,-1)/\sqrt2$, which *is* the opposition
  pattern. The prior becomes "the second coordinate is small" — one scalar constraint,
  orthogonal to the first coordinate, so the penalty is separable and interpretable.
- **$A$ neutral.** Neither axis expresses opposition; the prior becomes the coupled
  constraint $c_1 \approx -c_2$, which a diagonal penalty cannot represent without
  cross terms.
- **$B$ worst.** It is non-orthonormal, so it distorts the norm (part (c)) *and* its
  axes express no useful physical contrast. There is no reason to prefer it except
  convenience.

**General rule.** Choose an orthonormal basis aligned with the physical structures you
care about. Orthonormality makes norms and penalties basis-independent (the statement
of part (d)); alignment makes the prior expressible as a small number of simple
scalar constraints.

---

## ★★★8 — Numerical rank versus $\delta$

(a) Project $w = (1, 1+\delta, 0)$ off $v = (1,1,0)$:

$$\langle w,v\rangle = 2 + \delta, \quad \|v\|^{2} = 2, \quad
w_{\perp} = w - \frac{2+\delta}{2}v = \left(-\frac{\delta}{2},\ \frac{\delta}{2},\ 0
\right),$$
$$\|w_{\perp}\| = \frac{\delta}{\sqrt2} .$$

(b) The numerical rank drops when $\|w_{\perp}\|$ falls below the tolerance:

| tolerance | predicted $\delta = \sqrt2\,\text{tol}$ |
|---|---|
| $10^{-8}$ | $1.414\times10^{-8}$ |
| $10^{-12}$ | $1.414\times10^{-12}$ |
| $10^{-15}$ | $1.414\times10^{-15}$ |

These match the observed transitions in the lesson's Section 3.4 table, where the rank
changed between $\delta = 10^{-9}$ and $10^{-12}$ for a tolerance of $10^{-12}$.

(c) Exact angle: $\sin\theta = \|w_{\perp}\|/\|w\| = (\delta/\sqrt2)/\sqrt{2+2\delta+
\delta^{2}} \approx \delta/2$ for small $\delta$, so
$\theta \approx \delta/2$ radians $= \delta/2 \cdot 180/\pi$ degrees. At
$\delta = 10^{-9}$:

$$\theta_{\text{exact}} = \arcsin\left(\frac{10^{-9}}{\sqrt2}\right) \cdot
\frac{180}{\pi} = 4.051\times10^{-8}\ \text{degrees},$$

whereas the computed value from $\arccos$ of a near-unit cosine was reported as
$1.207\times10^{-6}$ degrees — a factor of 30 too large.

(d) **Mechanism.** $\cos\theta = 1 - \theta^{2}/2 + O(\theta^{4})$. Computing
$\arccos$ of a number that differs from 1 by $10^{-18}$ requires that difference to be
represented, but $1 - 10^{-18}$ rounds to exactly $1$ in double precision, so the
computed cosine carries no information about $\theta$ beyond $\theta \gtrsim
\sqrt{2\epsilon_{\text{mach}}} = 2.1\times10^{-8}$ rad. The cure is to avoid forming a
near-unit cosine: use $\sin\theta = \|w_{\perp}\|/\|w\|$ with $w_{\perp}$ computed by
orthogonalisation, and then $\theta = \arcsin(\sin\theta)$. That expression retains
full relative accuracy in $\delta$ down to the point where $w_{\perp}$ itself is lost
to round-off.

(e) **Code-review comment.** "Any rank or independence decision must state its
tolerance and derive it from the data precision; and any angle between nearly parallel
vectors must be computed from an orthogonalisation residual or a $\sin$, never from
$\arccos$ of an inner product."
