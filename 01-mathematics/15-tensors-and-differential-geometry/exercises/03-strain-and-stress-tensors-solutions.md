# Solutions — 01-15-03 Strain and Stress Tensors as Physical Tensors

> **Read this after attempting the exercises, not before.** Every number below was
> computed (eigenvalues by a Jacobi iteration on the symmetric matrix, verified
> against the characteristic polynomial). Conventions are the lesson's: tension
> positive, scientific strain.

---

## ★1 — Traction on planes

**(a)** The traction on the face with normal $\hat x_i$ is the $i$-th **row** of
$\boldsymbol\sigma$ (because $t_j = \sigma_{ji}n_i$ with $n = \hat x_i$), i.e. the
$i$-th column of the symmetric matrix:

$$t(\hat x_1) = (100, 25, -10), \qquad t(\hat x_2) = (25, 60, 5), \qquad
t(\hat x_3) = (-10, 5, 40)\ \text{MPa}.$$

**(b)** For $n = (0.6, 0.8, 0)$:

$$t_i = \sigma_{ij}n_j = (100(0.6) + 25(0.8),\ 25(0.6) + 60(0.8),\
-10(0.6) + 5(0.8)) = (80, 63, -2)\ \text{MPa}.$$

**(c)** The normal stress is the projection on the normal:

$$\sigma_n = t\cdot n = 80(0.6) + 63(0.8) = 48 + 50.4 = 98.4\ \text{MPa},$$

and the shear stress is the rest:

$$\tau = \sqrt{|t|^{2} - \sigma_n^{2}} = \sqrt{6400 + 3969 + 4 - 9682.56}
= \sqrt{690.44} = 26.276225\ \text{MPa}.$$

The identity holds by construction — $\tau^{2} = |t|^{2} - \sigma_n^{2}$ is the
definition of the decomposition — so this is a check on the arithmetic, not on the
physics. The shear *vector* itself, $t - \sigma_n n = (20.96, -15.72, -2.00)$ MPa,
has components along all three axes, including the normal direction's
perpendiculars in the plane; only its magnitude is frame-independent.

**(d)** Six independent components (the symmetry of $\boldsymbol\sigma$ halves the
nine). Each plane with a known normal supplies a traction *vector*, i.e. three
equations, so **two** planes with linearly independent normals give six equations
for six unknowns — the minimum in principle. In practice three planes are used:
a measurement device rarely delivers all three components of traction on one plane,
and the third plane turns the symmetry into an over-determined check rather than an
assumption. A single plane gives one vector, which cannot determine a tensor —
the lesson's first common mistake.

---

## ★2 — Principal stresses and invariants

**(a)** Diagonalising by Jacobi gives

$$\sigma_1 = 112.671652, \qquad \sigma_2 = 53.461588, \qquad
\sigma_3 = 33.866760\ \text{MPa},$$

and the sum of the three is $200.000000$ — the trace, to all printed digits.

**(b)** From the components:

$$I_1 = \sigma_{ii} = 100 + 60 + 40 = 200\ \text{MPa},$$

$$I_2 = \tfrac12\left(\sigma_{ii}\sigma_{jj} - \sigma_{ij}\sigma_{ji}\right)
= \tfrac12\left(200^{2} - 15800\right) = 11650\ \text{MPa}^{2},$$

$$I_3 = \det\boldsymbol\sigma = 204000\ \text{MPa}^{3}.$$

As elementary symmetric functions of the principal stresses:
$\sum\sigma_k = 200$ ✓;
$\sum_{k<l}\sigma_k\sigma_l = 112.671652(53.461588) +
112.671652(33.866760) + 53.461588(33.866760) = 11650.000000$ ✓;
$\sigma_1\sigma_2\sigma_3 = 204000$ ✓. (The middle identity is the one worth
checking by hand: $I_2$ is the sum of pairwise products *only after*
diagonalisation, which is why the component formula carries the
$-\tfrac12\sigma_{ij}\sigma_{ji}$ term.)

**(c)** $p = I_1/3 = 66.666667$ MPa and

$$\mathbf s = \boldsymbol\sigma - p\mathbf I = \begin{pmatrix}33.333333 & 25 &
-10\\ 25 & -6.666667 & 5\\ -10 & 5 & -26.666667\end{pmatrix}\ \text{MPa},$$

with $\operatorname{tr}\mathbf s = 0$ (computed as $-4\times10^{-15}$, i.e. zero).

**(d)** $J_2 = \tfrac12s_{ij}s_{ij} = 1683.333333$ MPa$^{2}$, and

$$\sqrt{3J_2} = \sqrt{5050} = 71.063352\ \text{MPa},$$

the von Mises equivalent stress. Also $I_2(\mathbf s) = -1683.333333$ MPa$^{2}$: for
a trace-free tensor the two invariants coincide up to sign, which is the
"different texts call the same number by either name" remark of §4.2.

All of the quantities in (c) and (d) are invariant under $\boldsymbol\sigma\to
-\boldsymbol\sigma$, since they are quadratic; $I_1$ and $p$ change sign. That is
the convention-dependence to state whenever comparing with a compression-positive
source.

---

## ★3 — A two-dimensional state

**(a)** For $\boldsymbol\sigma = \begin{pmatrix}8&3\\3&2\end{pmatrix}$,
$\operatorname{tr} = 10$ and $\det = 16 - 9 = 7$, so

$$\sigma_{1,2} = \frac{10 \pm \sqrt{100 - 28}}{2} = 5 \pm \sqrt{18}
= \boxed{5 \pm 3\sqrt2} = 9.242641,\ 0.757359\ \text{MPa}.$$

**(b)** $I_1 = 10$ MPa and $I_2 = \tfrac12(10^{2} - (64+9+9+4)) =
\tfrac12(100 - 86) = 7$ MPa$^{2}$, which equals $\det\boldsymbol\sigma = 7$ in two
dimensions. The check $\sigma_1\sigma_2 = (5+3\sqrt2)(5-3\sqrt2) = 25 - 18 = 7$ ✓.

**(c)** $p = 5$ MPa and
$\mathbf s = \begin{pmatrix}3&3\\3&-3\end{pmatrix}$, so
$J_2 = \tfrac12(9+9+9+9) = \boxed{18}$ MPa$^{2}$.

**(d)** The principal directions satisfy $\tan 2\theta = \dfrac{2\sigma_{xy}}
{\sigma_{xx} - \sigma_{yy}} = \dfrac{6}{6} = 1$, so

$$2\theta = 45^\circ, \qquad \theta = \boxed{22.5^\circ}$$

from the $x_1$ axis; the second axis is at $112.5^\circ$. The choice of $45^\circ$
versus $225^\circ$ is a choice between the two eigenvector directions, which are
defined up to sign.

---

## ★4 — Strain, rotation and dilatation

**(a)** Splitting the given gradient:

$$e_{ij} = \begin{pmatrix}0.002 & 0.000 & 0.000\\ 0.000 & -0.004 & 0.002\\
0.000 & 0.002 & 0.002\end{pmatrix}, \qquad
\omega_{ij} = \begin{pmatrix}0.000 & 0.005 & -0.001\\ -0.005 & 0.000 & -0.001\\
0.001 & 0.001 & 0.000\end{pmatrix}.$$

The check $e_{ij} + \omega_{ij} = u_{i,j}$ holds entry by entry; note that the
symmetric part is diagonal in the $(1,2)$ and $(1,3)$ slots only because the
corresponding off-diagonal entries of $u_{i,j}$ happen to be equal and opposite
($0.005$ and $-0.005$, $-0.001$ and $+0.001$) — those pairs are pure rotation, and
they carry no strain at all.

**(b)** $e_{ii} = 0.002 - 0.004 + 0.002 = 0.000$: the deformation is
**volume-preserving** to the given precision, i.e. $\delta V/V = 0$. The strain is
therefore pure shear in the sense of the decomposition of §2.3, and any isotropic
constitutive response ($\sigma_{kk} = (3\lambda + 2\mu)e_{kk}$) vanishes for it.

**(c)** $\gamma_{12} = 2e_{12} = 0$, $\gamma_{13} = 2e_{13} = 0$, and
$\gamma_{23} = 2e_{23} = 0.004$. Only the $(2,3)$ pair carries engineering shear;
the rotation components $\omega_{12} = 0.005$ and $\omega_{23} = -0.001$ carry
none.

**(d)** Only $e$ can store elastic energy, because the stored energy is a *quadratic*
form in the gradient and $\omega_{ij}dx_idx_j$ vanishes identically for an
antisymmetric $\omega$ (the argument of
[01-15-01](../01-index-notation.md) §3.6). Physically: a rigid rotation changes no
length and therefore no strain energy. The rotation is not nothing, however — it
reorients material and is what shear-wave splitting measures.

---

## ★★5 — Why the stress tensor is symmetric

**(a)** A cube of side $\ell$ has faces at $\pm\ell/2$ in each direction. The force
on a face is traction $\times$ area, so it scales as $\ell^{2}$, and its moment
arm about the centre is $\ell/2$: each face's contribution to the moment scales as
$\ell^{3}$. Summing the six faces,

$$0 = \varepsilon_{ijk}\sigma_{jl}\ell_j + c_k \quad\text{per unit volume},$$

with $c_k$ a body-couple density (moment per unit volume).

**(b)** A volume couple produces a moment $c_k\ell^{3}$, the same power of $\ell$ as
the surface terms — so the two survive together in the limit $\ell\to0$ and must
cancel. With $c_k = 0$ the surface term must vanish on its own, and since $\ell_j$
is arbitrary,

$$\varepsilon_{ijk}\sigma_{jk} = 0 \quad\Longrightarrow\quad \sigma_{jk} =
\sigma_{kj}. \qquad\square$$

The step from the volume to the pointwise statement uses the arbitrariness of both
$\ell_j$ and the position of the cube; if the cube were of a fixed size the
statement would be about an average, not a point.

**(c)** The assumption that fails in a **Cosserat** (micropolar) medium is
$c_k = 0$: individual grains carry their own couples, the antisymmetric part of the
stress is *not* zero, and it is balanced by a couple-stress tensor (a rank-3
object). The force balance is unaffected; it is the moment balance that acquires a
volume term.

**(d)** A good case is a granular or blocky rock mass — a fault gouge, a heavily
jointed volcanic edifice, a rubble zone — where grains of finite size rotate
independently and the continuum limit is reached only over many grains. The
Cosserat length scale is the grain or block size, so the effect vanishes for
long-wavelength seismic probing and can be significant for borehole-scale or
laboratory measurements.

---

## ★★6 — A strike-slip state

**(a)** $\sigma_1$ is N–S, $\sigma_3$ is E–W, so the maximum-shear planes bisect
those directions: their normals lie $45^\circ$ from $\sigma_1$ in the horizontal
plane. Since $\sigma_2$ is vertical, the planes contain the vertical direction:
two vertical planes striking **N45°E** and **N45°W**.

**(b)** Both planes are vertical, so slip on either is horizontal — **strike-slip
faulting**. This is Anderson's classification at work: the fault dip is controlled
by which principal stress is vertical, and here it is $\sigma_2$, which is
precisely the definition of a strike-slip regime.

**(c)** With $\sigma_1 = 120$, $\sigma_2 = 80$, $\sigma_3 = 40$ MPa:

$$\tau_{\max} = \frac{\sigma_1 - \sigma_3}{2} = \frac{120 - 40}{2}
= \boxed{40}\ \text{MPa}, \qquad
\sigma_n = \frac{\sigma_1 + \sigma_3}{2} = \boxed{80}\ \text{MPa}.$$

The normal stress on the maximum-shear plane is the mean of the extreme principal
stresses, *not* the mean stress $p = (120+80+40)/3 = 80$ MPa — the two coincide
here only because $\sigma_2 = p$; that coincidence is specific to this state and is
worth noticing rather than generalising.

**(d)** The focal mechanism would show nodal planes striking N45°E and N45°W with
vertical dips, and the **P axis** (the compression axis of the moment tensor)
would lie along $\sigma_1$, i.e. N–S horizontal; the **T axis** along $\sigma_3$,
E–W horizontal. The mechanism gives the *orientation* of the principal axes but not
their magnitudes: the beach-ball pattern is unchanged by adding any isotropic
pressure, which is why focal mechanisms cannot be used to estimate absolute stress
magnitudes.

---

## ★★7 — Pure shear versus simple shear

**(a)** For $e_{ij}$ with only $e_{12} = e_{21} = \epsilon$, the trace is
$e_{ii} = e_{11} + e_{22} + e_{33} = 0 + 0 + 0 = 0$. From the length-change identity
with $dx = (\ell, 0, 0)$: $\ell'^{2} - \ell^{2} = 2e_{11}\ell^{2} = 0$, and the same
for the other axes; a volume element $dV$ changes by $dV\,e_{ii} = 0$, so pure shear
**preserves volume**. Physically it is a change of shape at constant volume — the
shear of a deck of cards without compression.

**(b)** A displacement field producing pure shear is
$u_1 = \epsilon x_2$, $u_2 = \epsilon x_1$ (so $u_{1,2} = u_{2,1} = \epsilon$ and
the gradient is symmetric), which gives $\omega_{ij} = 0$: the deformation contains
**no rotation**, which is the defining property of pure shear in this convention.

**(c)** Simple shear $u_1 = \kappa x_2$, $u_2 = u_3 = 0$ has

$$u_{i,j} = \begin{pmatrix}0&\kappa&0\\0&0&0\\0&0&0\end{pmatrix}, \qquad
e_{ij} = \begin{pmatrix}0&\kappa/2&0\\ \kappa/2&0&0\\0&0&0\end{pmatrix}, \qquad
\omega_{ij} = \begin{pmatrix}0&\kappa/2&0\\ -\kappa/2&0&0\\0&0&0\end{pmatrix}.$$

So simple shear is **pure shear plus a rigid rotation** of angle $\kappa/2$. The
strain tensors of the two fields are identical (with $\kappa = 2\epsilon$), which
is the whole content of the next part.

**(d)** An isotropic material responds only to the symmetric part of the gradient
($\sigma_{ij} = \lambda e_{kk}\delta_{ij} + 2\mu e_{ij}$), and the two fields have
the same $e_{ij}$, so they produce the same stress. Microstructurally they differ
because the rotation part reorients grains: simple shear continuously rotates the
fabric (a finite simple shear of a rock produces a shape-preferred orientation and
a foliation at a predictable angle to the shear plane), while pure shear leaves the
rotation at zero and the fabric orientation is set by the strain axes. This is why
shear-wave splitting is analysed in terms of the *symmetry axes* rather than the
stress alone.

---

## ★★8 — Compatibility

The two-dimensional form of the compatibility condition, for a state with
$e_{zz} = e_{xz} = e_{yz} = 0$, reduces to

$$2\frac{\partial^{2}e_{xy}}{\partial x\,\partial y}
= \frac{\partial^{2}e_{xx}}{\partial y^{2}} +
\frac{\partial^{2}e_{yy}}{\partial x^{2}} .$$

**(a)**

| field | $\partial^{2}e_{xx}/\partial y^{2}$ | $\partial^{2}e_{yy}/\partial x^{2}$ | $2\partial^{2}e_{xy}/\partial x\partial y$ | residual |
|---|---|---|---|---|
| (i) $e_{xx} = y^{2}$, $e_{yy} = x^{2}$ | 2 | 2 | 0 | **4** |
| (ii) $e_{xx} = x^{2}$, $e_{yy} = y^{2}$ | 0 | 0 | 0 | **0** |
| (iii) $e_{xx} = x^{2}$, $e_{yy} = y^{2}$, $e_{xy} = xy/2$ | 0 | 0 | 1 | **1** |

The demonstration computes $4.000467$ for a field of type (i) — the same $4$ — the
difference being the finite-difference truncation of its numerical derivative.

**(b)** Fields (i) and (iii) are **impossible**: no single-valued displacement
field has them as its symmetric gradient. Field (i) describes a body that would
have to lengthen by $2y^{2}$ along $x$ while lengthening by $2x^{2}$ along $y$, with
no shear to reconcile the two — near the origin the two demands conflict and the
material would have to tear or overlap. Field (iii) is the subtler failure: its
normal strains are compatible *by themselves* but the shear it prescribes does not
match what those normal strains imply. Field (ii) is compatible.

**(c)** For (ii), integrate: $u_x = x^{3}/3 + f(y)$ and $u_y = y^{3}/3 + g(x)$, with
the requirement $e_{xy} = \tfrac12(f'(y) + g'(x)) = 0$, so $f' = -g' = $ constant
$= -c$; then

$$u_x = \frac{x^{3}}{3} - cy, \qquad u_y = \frac{y^{3}}{3} + cx .$$

The free constant $c$ is a rigid rotation of the whole body, which produces no
strain — the same statement as ★4(d): the antisymmetric part of the gradient is not
determined by the strain field.

**(d)** Imposing an incompatible strain field on a displacement-based finite-element
model is impossible by construction: the element's degrees of freedom are
displacements, so the computed strain is always compatible, and the model responds
by producing whatever stress pattern the interpolant can represent — typically
locking (spurious stiffness) and oscillating stresses that do not decrease under
refinement. The cure is not to enforce compatibility but to *relax* it: mixed or
enhanced-assumption formulations, or a variational formulation in which the strain
is an independent field. The diagnosis in practice is a stress field whose
magnitude grows as the mesh is refined, which no physical solution does.

---

## ★★★9 — Three-dimensional Mohr circles

**(a)** With $\sigma_1 = 112.671652$, $\sigma_2 = 53.461588$,
$\sigma_3 = 33.866760$ MPa, the three circle radii are the half-differences:

$$R_{13} = \frac{\sigma_1 - \sigma_3}{2} = 39.402446, \qquad
R_{12} = \frac{\sigma_1 - \sigma_2}{2} = 29.605032, \qquad
R_{23} = \frac{\sigma_2 - \sigma_3}{2} = 9.797414\ \text{MPa}.$$

The centres lie at the pairwise means: $73.269206$, $83.066620$ and $43.664174$ MPa.

**(b)** The three circles bound the region of attainable $(\sigma_n,\tau)$; the
largest admissible $\tau$ over *all* plane orientations is the radius of the largest
circle, $R_{13} = (\sigma_1 - \sigma_3)/2 = 39.402446$ MPa, attained on the planes
that bisect the $\sigma_1$ and $\sigma_3$ directions (and contain $\sigma_2$). The
demonstration's random search over 400 000 normals reached $39.402333$ against this
value — a difference of $1.1\times10^{-4}$, which is the resolution of the search,
not a discrepancy in the theory. $\square$

**(c)** The in-plane maximum shear computed from a 2-D analysis using only
$\sigma_1$ and $\sigma_2$ would be $R_{12} = 29.605032$ MPa — **24.9 per cent less**
than the true maximum, because the 2-D analysis excludes the plane that also uses
$\sigma_3$. Reporting an in-plane maximum shear as "the" maximum shear is a common
error whenever a third principal stress is available; the reduction is
$1 - R_{12}/R_{13} = 1 - (\sigma_1-\sigma_2)/(\sigma_1-\sigma_3)$.

**(d)** The lesson's §3.5 states the exact value as
$(I_1 - 3\sigma_2)/2$. Evaluating it with the numbers above:

$$\frac{I_1 - 3\sigma_2}{2} = \frac{200 - 3(53.461588)}{2}
= \frac{200 - 160.384764}{2} = 19.807619\ \text{MPa},$$

which is **not** equal to $(\sigma_1-\sigma_3)/2 = 39.402446$ MPa — it is exactly
half of $R_{12} + R_{23}$-type combination
$\left|(I_1 - 3\sigma_2)/2\right| = |(\sigma_1+\sigma_3-2\sigma_2)/2|
= R_{12} - R_{23} = 29.605032 - 9.797414 = 19.807618$ MPa. So the lesson's parenthetical
formula is mislabelled: the maximum shear is $(\sigma_1-\sigma_3)/2$, and
$(I_1-3\sigma_2)/2$ is a different (and generally negative or smaller) quantity. The
demonstration's output is correct — it prints
`exact result (sigma_1 - sigma_3)/2 = 39.402446` — and only the lesson prose
attaches the wrong expression to the number.

---

## ★★★10 — A moment tensor

**(a)** $M = \operatorname{diag}(3,-1,-2)\times10^{18}$ N m has
$\operatorname{tr}M = (3-1-2)\times10^{18} = 0$, so the isotropic part is zero and
the deviatoric part is $M$ itself. Physically the isotropic (volumetric) part of a
moment tensor measures the volume change of the source: it is essentially zero for
a tectonic earthquake on a shear fault and non-zero for volcanic, explosion,
implosion or phase-change sources.

**(b)** The deviatoric magnitude $M_0 = \left(\tfrac12M_{ij}M_{ij}\right)^{1/2}$
equals $\sqrt{J_2}$ with $J_2 = \tfrac12s_{ij}s_{ij}$. With
$s = \operatorname{diag}(3,-1,-2)\times10^{18}$:

$$J_2 = \tfrac12\left(9 + 1 + 4\right)\times10^{36} = 7\times10^{36}\ \text{N}^{2}\,\text{m}^{2},
\qquad M_0 = \sqrt{7}\times10^{18} = \boxed{2.645751\times10^{18}}\ \text{N m}.$$

For comparison the von Mises equivalent is
$\sqrt{3J_2} = \sqrt{21}\times10^{18} = 4.582576\times10^{18}$ N m — a different
scalar, as it must be, because $M_0$ is a $\sqrt{J_2}$ while von Mises is
$\sqrt{3J_2}$. The two differ by $\sqrt3$ and are not interchangeable.

**(c)** The principal axes are the coordinate axes (the tensor is already diagonal)
and the principal values are $\sigma_1 = 3$, $\sigma_2 = -1$, $\sigma_3 = -2$, all
in units of $10^{18}$ N m. The Lode angle follows from equation (11) with
$J_2 = 7$:

$$s_k = \frac{2\sqrt{J_2}}{\sqrt3}\cos\!\left(\theta_L -
\frac{2\pi(k-1)}{3}\right), \qquad
\frac{2\sqrt{7}}{\sqrt3} = 3.055050 .$$

Solving for $k=1$: $\cos\theta_L = 3/3.055050 = 0.981981$, i.e.

$$\theta_L = 0.190126\ \text{rad} = \boxed{10.8934^\circ},$$

and substituting back reproduces $s = (3.000000, -1.000000, -2.000000)$ to twelve
decimals. The third invariant is also consistent: $\det\mathbf s = 6\times10^{54}$
and $\tfrac13s_{ij}s_{jk}s_{ki} = \tfrac13(27 - 1 - 8) = 6$ ✓.

**(d)** From the mechanism alone a seismologist can infer: the **orientation** of
the principal axes (the two nodal planes, i.e. the fault geometry up to the
fault/auxiliary ambiguity), the **orientation** of the slip vector, the *ratio* of
principal values (through the Lode angle and $M_0$), and whether the isotropic part
is non-zero (source type). They **cannot** infer: absolute stress magnitudes (adding
$\pm p$ to the diagonal changes no mechanism), the actual fault surface from the two
nodal planes, the stress drop without a rupture model, or the sign convention of the
moment tensor without independent information (the same mechanism is produced by
$M$ and $-M$ with the slip direction reversed). Every one of those statements is a
statement about the invariants of this lesson — which is why mechanisms are reported
as axes and angles rather than as components.
