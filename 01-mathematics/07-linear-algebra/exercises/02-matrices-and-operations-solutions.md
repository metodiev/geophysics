# Solutions — 01-07-02 Matrices, Matrix Multiplication and Linear Maps

> **Read this after attempting the exercises, not before.**
>
> These are *worked solutions*, showing a valid route and the reasoning. They are
> not the only correct route. Numeric answers were computed and verified rather than
> estimated by hand.

---

## ★1 — Two products, two answers

$$A = \begin{bmatrix} 2 & 1 \\ 0 & 3\end{bmatrix}, \qquad
B = \begin{bmatrix} 1 & -1 \\ 4 & 2\end{bmatrix},$$

$$AB = \begin{bmatrix} 2\cdot1 + 1\cdot4 & 2(-1) + 1\cdot2 \\ 0\cdot1 + 3\cdot4 &
0(-1) + 3\cdot2\end{bmatrix}
= \begin{bmatrix} 6 & 0 \\ 12 & 6\end{bmatrix},$$

$$BA = \begin{bmatrix} 1\cdot2 + (-1)\cdot0 & 1\cdot1 + (-1)\cdot3 \\ 4\cdot2 +
2\cdot0 & 4\cdot1 + 2\cdot3\end{bmatrix}
= \begin{bmatrix} 2 & -2 \\ 8 & 10\end{bmatrix}.$$

They differ in every entry. A commuting pair: $A = \begin{bmatrix} 2 & 1 \\ 0 & 3
\end{bmatrix}$ commutes with $A^{2} = \begin{bmatrix} 4 & 5 \\ 0 & 9\end{bmatrix}$
(since $A A^{2} = A^{3} = A^{2}A$), and more generally with any polynomial in itself.
Also any two diagonal matrices commute. **Physically:** the two matrices of ★1 do not
commute because one of them ($A$) mixes the two components while the other ($B$)
re-weights them: the order decides whether the mixing happens before or after the
weighting.

---

## ★2 — Two-layer refraction

(a)

$$G = \begin{bmatrix} 0.4 & 0.6 \\ 0.5 & 0.5\end{bmatrix}, \qquad
d = \begin{bmatrix} t_1 \\ t_2\end{bmatrix} \ \mathrm{s}, \qquad
m = \begin{bmatrix} s_1 \\ s_2\end{bmatrix} \ \mathrm{s/km}.$$

$G_{ij}$ = path length of ray $i$ in layer $j$, in km: (time) = (path length) ×
(slowness) = $\mathrm{km}\times\mathrm{s/km} = \mathrm{s}$. ✓

(b) Column 2 has entries $0.6$ and $0.5$: ray 1 spends $0.6$ km in layer 2 and ray 2
spends $0.5$ km. So ray 1's travel time is $20$ % more sensitive to layer 2
($0.6/0.5 = 1.2$).

(c) $\det G = 0.4(0.5) - 0.6(0.5) = 0.2 - 0.3 = -0.1\
\mathrm{km^{2}}$. Geometrically: the unit square of slowness perturbations maps to a
parallelepiped of area $0.1$ (in $\mathrm{s^{2}/km^{2}}$), so the two rays are far
from redundant — the geometry is well conditioned.

(d) The null space is trivial ($\det \neq 0$), so no nonzero perturbation produces zero
data. The *near*-null direction is the eigenvector of $G$ belonging to the smaller
singular value: the ray geometries differ mainly in the ratio $0.4/0.6$ versus
$0.5/0.5$, so the weak direction is roughly the contrast between the two layers,
$m \propto (1,-1)$: check

$$G\begin{bmatrix} 1 \\ -1\end{bmatrix} = \begin{bmatrix} -0.2 \\ 0.0\end{bmatrix},$$

which is not zero but is small compared with the model size. The residual for the
$(1,-1)$ direction is $20$ % of the effect of $(1,1)$ — a mild trade-off, resolved
because $\det G \neq 0$.

---

## ★3 — The central-difference matrix

(a) With $h$ the spacing and columns corresponding to $z = 0, h, 2h, 3h, 4h$:

$$D = \frac{1}{h}\begin{bmatrix} -1 & 1 & 0 & 0 & 0 \\ -0.5 & 0 & 0.5 & 0 & 0 \\
0 & -0.5 & 0 & 0.5 & 0 \\ 0 & 0 & -0.5 & 0 & 0.5 \\ 0 & 0 & 0 & -1 & 1
\end{bmatrix}.$$

(b) $(D\mathbf{1})_i$ is the sum of the entries of row $i$, which is $0$ for every row:
$-1+1$, $-0.5+0.5$, $\ldots$, $-1+1$. ✓

(c) $\operatorname{rank}D = 4$ and $\mathcal{N}(D) = \operatorname{span}\{(1,1,1,1,1)
^\mathsf{T}\}$. (Eliminate: rows 1 and 5 each reduce one dimension, and the three
central rows are independent; the null space has dimension $5 - 4 = 1$ and contains
$\mathbf{1}$, so it *is* $\operatorname{span}\mathbf{1}$.)

(d) $D(0,1,2,3,4)^\mathsf{T} = (1,1,1,1,1)^\mathsf{T}$ and
$D(5,6,7,8,9)^\mathsf{T} = (1,1,1,1,1)^\mathsf{T}$: identical, because the two inputs
differ by $5\cdot\mathbf{1}$ and $D$ annihilates $\mathbf{1}$ linearly:
$D(x + 5\mathbf{1}) = Dx + 5D\mathbf{1} = Dx$. This is *linearity plus the null
space*, and it is a two-line argument rather than a computation.

(e) A strain rate computed from GPS velocities is a derivative of the displacement
field; a uniform translation of the whole network (every station moving by the same
vector) produces zero strain. The translation is the null space of the
differentiation operator, exactly as the constant profile is the null space of $D$.
Any strain field must therefore be reported relative to some reference frame, and the
choice of frame is a modelling decision that the data cannot make.

---

## ★★4 — Rotation matrices

(a) Multiply:

$$R(\theta)R(\phi) = \begin{bmatrix} \cos\theta\cos\phi - \sin\theta\sin\phi &
-\cos\theta\sin\phi - \sin\theta\cos\phi \\ \sin\theta\cos\phi + \cos\theta\sin\phi &
-\sin\theta\sin\phi + \cos\theta\cos\phi\end{bmatrix}
= \begin{bmatrix} \cos(\theta+\phi) & -\sin(\theta+\phi) \\ \sin(\theta+\phi) &
\cos(\theta+\phi)\end{bmatrix},$$

using the addition formulas for sine and cosine. ✓

(b) Set $\phi = -\theta$ in (a): $R(\theta)R(-\theta) = R(0) = I$, so
$R(\theta)^{-1} = R(-\theta)$. And $R(\theta)^\mathsf{T}$ has its off-diagonal entries
swapped and negated: $R(\theta)^\mathsf{T} = \begin{bmatrix} \cos\theta & \sin\theta
\\ -\sin\theta & \cos\theta\end{bmatrix} = R(-\theta)$. Hence
$R^{-1} = R^\mathsf{T}$: the matrix is orthogonal. ✓

(c) $\det R(\theta) = \cos^{2}\theta + \sin^{2}\theta = 1$. Orthogonality forces
$|\det| = 1$ because for an orthogonal $Q$,
$\det(Q^\mathsf{T}Q) = \det I = 1$ and $\det(Q^\mathsf{T}Q) = (\det Q)^{2}$, so
$(\det Q)^{2} = 1$. The rotation takes the $+1$ root because it does not reflect.

(d) $\|R(\theta)x\|^{2} = x^\mathsf{T}R(\theta)^\mathsf{T}R(\theta)x =
x^\mathsf{T}x = \|x\|^{2}$, so lengths are preserved. Physically: rotating the
coordinate frame does not change the magnitude of the ground motion, which is the
statement that a rotation changes coordinates and not the vector.

---

## ★★5 — Reflection travel times, and the depth–velocity trade-off

(a) With $r = \sqrt{x^{2}+4h^{2}}$,

$$J = \begin{bmatrix} \dfrac{4h}{vr} & -\dfrac{r}{v^{2}} \end{bmatrix}
\ \text{with columns in } \mathrm{s/km} \text{ and } \mathrm{s/(km/s)} .$$

At $(h,v) = (1.2, 3.7)$:

| $x$ (km) | $\partial T/\partial h$ (s/km) | $\partial T/\partial v$ (s per km/s) |
|---|---|---|
| 0 | $0.540540541$ | $-0.175310446$ |
| 1 | $0.498960499$ | $-0.189919649$ |
| 2 | $0.415254746$ | $-0.228203058$ |
| 3 | $0.337672999$ | $-0.280633641$ |
| 4 | $0.278105814$ | $-0.340742258$ |
| 5 | $0.233908685$ | $-0.405125628$ |

(b) For $\delta = (0.01\ \mathrm{km},\ 0.01\ \mathrm{km/s})$:

| $x$ (km) | linear prediction (s) | exact change (s) | difference (s) |
|---|---|---|---|
| 0 | $3.652\times10^{-3}$ | $3.642\times10^{-3}$ | $-9.844\times10^{-6}$ |
| 3 | $5.704\times10^{-4}$ | $5.774\times10^{-4}$ | $+6.991\times10^{-6}$ |
| 5 | $-1.712\times10^{-3}$ | $-1.700\times10^{-3}$ | $+1.250\times10^{-5}$ |

The differences are second order: the residual is dominated by the cross term
$(\partial^{2}T/\partial h\,\partial v)\delta h\,\delta v$, which is
$-1.46\times10^{-5}$ s at these values — matching the observed $x = 0$ difference of
$-9.8\times10^{-6}$ s together with the $v$-curvature contribution
$+\tfrac12(\partial^{2}T/\partial v^{2})(\delta v)^{2} = +4.7\times10^{-6}$ s.

(c) $J^\mathsf{T}J = \begin{bmatrix} 0.959661330 & -0.568574418 \\
-0.568574418 & 0.477867163\end{bmatrix}$, $\det = 0.135313768$, and the eigenvalues
are $1.336265885$ and $0.101262608$, so

$$\kappa_2(J) = \sqrt{1.336265885/0.101262608} = 3.632636 .$$

(d) **Yes, they determine $h$ and $v$ separately.** $\kappa_2 = 3.63$ is small: a 1 %
data error produces at most a 3.6 % model error, and the two parameters are separable.
The offset range is the decisive factor — the maximum offset (5 km) is more than four
times the reflector depth (1.2 km), which is exactly the condition that decouples the
two columns. Note the strong negative correlation of the two Jacobian columns
($J^\mathsf{T}J_{12} = -0.569$ against diagonal entries $0.96$ and $0.48$): the
trade-off is present, but the wide aperture resolves it. Truncating the offsets at
$x = 2$ km would raise $\kappa$ from $3.63$ to $13.07$, a factor of $3.6$, and this is
why the maximum offset in a reflection survey is chosen as a multiple of the target
depth.

---

## ★★6 — Repeated smoothing

(a) Row sums are $(0.75,\ 1.0,\ 1.0,\ 1.0,\ 0.75)$, so
$\|C\|_\infty = \max_i\sum_j|C_{ij}| = 1$; the three interior rows achieve it. Since
$\|C\|_2 \le \sqrt{\|C\|_1\|C\|_\infty}$ and $C$ is symmetric so $\|C\|_1 =
\|C\|_\infty = 1$, we get $\|C\|_2 \le 1$; in fact $\|C\|_2 = \rho(C) = 0.9330127$
because $C$ is symmetric.

(b) $\det C = 0.005859375 = 3/512$ exactly. It is small but nonzero because the
matrix is a *smearing* operation: it nearly — but not exactly — maps a whole family of
vectors into a lower-dimensional set, and the eigenvalues (below) are all distinct and
positive, with product $3/512$.

(c) Eigenvalues:

$$(0.9330127,\ 0.7500000,\ 0.5000000,\ 0.2500000,\ 0.0669873),$$

the largest being $(2+\sqrt3)/4 = 0.9330127$. All lie in $(0,1)$, so repeated
application converges to zero.

(d) After 100 applications, $(1,2,4,3,1.5) \mapsto
(0.00155588,\ 0.00269486,\ 0.00311176,\ 0.00269486,\ 0.00155588)$. The trace has
decayed by a factor of about $900$ and become symmetric and smooth. The observed decay
per application, $(0.00311176/4)^{1/100} \approx 0.933$, matches the largest
eigenvalue: after many applications only the dominant mode survives, and that mode is
the smooth one.

(e) The connection is the same phenomenon from the opposite direction. Repeated
smoothing destroys exactly the components that the *derivative* is sensitive to: the
derivative of a smooth (low-wavenumber) function is small, so its contribution to the
data is small, so it is the direction that the data resemble least. In the limit of
infinite smoothing, the surviving directions are the ones the derivative operator maps
to zero — constants. The null space of a derivative and the slow-decaying modes of a
smoother are the two faces of "flat functions are invisible to derivatives".

---

## ★★★7 — Composition of a rotation, a stretch and a rotation back

(a) $M = R(-\theta)SR(\theta)$. For $\theta = 30^{\circ}$:

$$M = \begin{bmatrix} 1.25 & 0.433013 \\ 0.433013 & 1.75\end{bmatrix}.$$

**Derivation worth doing once by hand:** $M$ is a similarity transform of $S$, so it
has the same eigenvalues as $S$; it is symmetric because for symmetric $S$ and
orthogonal $Q$, $(QSQ^\mathsf{T})^\mathsf{T} = QS^\mathsf{T}Q^\mathsf{T} =
QSQ^\mathsf{T}$.

(b) $M$ is symmetric with eigenvalues $1$ and $2$ and eigenvectors along the rotated
axes, i.e. along $(\cos30^{\circ},\sin30^{\circ})$ for $\lambda = 1$ and
$(-\sin30^{\circ},\cos30^{\circ})$ for $\lambda = 2$. Reducing the map to two numbers
loses nothing because a symmetric matrix's action is completely described by its
spectral decomposition $M = Q\Lambda Q^\mathsf{T}$ — that is
[01-07-06](../06-eigenvalues.md). The two numbers are the *gains* along the two
principal directions.

(c) Invariants:

| $\theta$ | $M$ | trace | determinant | eigenvalues |
|---|---|---|---|---|
| $0^{\circ}$ | $\begin{bmatrix} 1 & 0 \\ 0 & 2\end{bmatrix}$ | $3.000000$ | $2.000000$ | $1,\ 2$ |
| $30^{\circ}$ | $\begin{bmatrix} 1.25 & 0.433013 \\ 0.433013 & 1.75\end{bmatrix}$ | $3.000000$ | $2.000000$ | $1,\ 2$ |

Similar matrices have identical characteristic polynomials, hence identical trace and
determinant. **Physically:** the trace is the sum of the principal gains and the
determinant their product, so neither depends on the orientation of the anisotropy
frame. The *off-diagonal* entry does depend on orientation
($0 \to 0.433013$), which is why an off-diagonal term in a stiffness tensor is a
statement about the coordinate frame as much as about the rock.

(d) Replace $S$ by a non-symmetric $T$. With
$T = \begin{bmatrix} 1 & 0.7 \\ 0.5 & 2\end{bmatrix}$ and $\theta = 30^{\circ}$,

$$R(-\theta)TR(\theta) = \begin{bmatrix} 1.769615 & 0.833013 \\ 0.633013 &
1.230385\end{bmatrix},$$

whose off-diagonal entries differ by $0.2$: **not symmetric**. The general algebraic
statement is exact: $(QSQ^\mathsf{T})^\mathsf{T} = QS^\mathsf{T}Q^\mathsf{T}$, so
$QSQ^\mathsf{T}$ is symmetric for every orthogonal $Q$ if and only if $S$ is
symmetric. The symmetry of the result in (b) was therefore a consequence of $S$ being
symmetric, not of the rotation. In mechanics this is the distinction between an
elastic stiffness and a general linear constitutive relation.

---

## ★★★8 — Scaling one model parameter

(a) Scaling the first model parameter by $10^{3}$ multiplies the first *column* of the
kernel by $10^{3}$: $G' = G\operatorname{diag}(1000, 1)$, so with $\delta = 0.01$,

$$G = \begin{bmatrix} 1 & 1 \\ 1 & 1.01\end{bmatrix}
\ \text{km}, \qquad
G' = \begin{bmatrix} 1000 & 1 \\ 1000 & 1.01\end{bmatrix} .$$

(b) The two kernels represent the same experiment because the same data are produced
by the rescaled models: $G'm' = d$ with $m' = \operatorname{diag}(1/1000, 1)m$. The
model space has been reparameterised, not changed — the set of achievable data,
$\mathcal{C}(G') = \mathcal{C}(G)$, is identical.

(c) $\det G = 1.01 - 1 = 0.01$ and $\det G' = 1000(1.01) - 1000(1) = 10$, a ratio of
$1000$ — exactly the factor by which the first column was scaled. The determinant is
multilinear, so scaling one column by $k$ multiplies it by $k$.

(d) Singular values:

$$\sigma(G) = (2.0050125,\ 0.0049875), \qquad \kappa_2(G) = 402.007513 ,$$
$$\sigma(G') = (1414.2142766,\ 0.0070711), \qquad \kappa_2(G') = 200\,000.202005 ,$$

so $\kappa_2$ changed by a factor of $497.5$.

(e) **Both changed, and for the same reason: a determinant and a condition number are
both sensitive to scaling when the scaling is not uniform.** Here the first column
grew by $10^{3}$ while the second did not, so the matrix became much more anisotropic
in its column norms — the weak direction $(1,-1)$-like combination became even weaker
relative to the strong one, and $\kappa$ grew. (If instead *both* columns were scaled
by $10^{3}$ — measuring all path lengths in metres — then the matrix would merely be
multiplied by an overall constant, $\kappa$ would be unchanged, and only $\det$ would
change, by $10^{6}$.) The honest measure of the difficulty of the *experiment* is
$\kappa$, because it is invariant under orthogonal changes of coordinates; but the
figure of merit for a *parameterisation* is also $\kappa$, and part (d) shows that a
bad parameterisation can inflate it by two orders of magnitude. The practical rule:
**make the model parameters dimensionless and of comparable magnitude before
computing $\kappa$, and quote the parameterisation with the number.**
