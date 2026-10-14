# Solutions — 01-12-08 Numerical Eigenvalue Problems (Power, Lanczos, Arnoldi)

> **Read this after attempting the exercises, not before.** Every number below was
> computed; the demonstration's values quoted in ★★6 are the output of
> [`../code/matrix_eigen_solvers.py`](../code/matrix_eigen_solvers.py).

---

## ★1 — Power iteration on a $2\times2$ matrix

**(a)** $\det(A - \lambda I) = (3-\lambda)^{2} - 1 = 0$ gives
$\lambda_1 = 4$, $\lambda_2 = 2$ with eigenvectors
$\mathbf v_1 = \frac{1}{\sqrt2}(1,1)^{\mathsf T}$ and
$\mathbf v_2 = \frac{1}{\sqrt2}(1,-1)^{\mathsf T}$.

**(b)** and **(c)** Iterating $\mathbf x \leftarrow A\mathbf x/\|A\mathbf x\|$
from $\mathbf x_0 = (1,0)^{\mathsf T}$:

| $k$ | $\mathbf x_k$ | $R(\mathbf x_k)$ | $|R - \lambda_1|$ |
|---|---|---|---|
| 0 | $(1.000000,\ 0.000000)$ | 3.000000 | $1.000\times10^{0}$ |
| 1 | $(0.948683,\ 0.316228)$ | 3.600000 | $4.000\times10^{-1}$ |
| 2 | $(0.857493,\ 0.514496)$ | 3.882353 | $1.176\times10^{-1}$ |
| 3 | $(0.789352,\ 0.613941)$ | 3.969231 | $3.077\times10^{-2}$ |
| 4 | $(0.749838,\ 0.661622)$ | 3.992218 | $7.782\times10^{-3}$ |
| 5 | $(0.728848,\ 0.684675)$ | 3.998049 | $1.951\times10^{-3}$ |
| 6 | $(0.718068,\ 0.695973)$ | 3.999512 | $4.882\times10^{-4}$ |

The first iterate is $\mathbf x_1 = (3,1)/\sqrt{10}$, as it must be.

**(d)** The error ratios are $0.4000$, $0.2941$, $0.2616$, $0.2528$, $0.2507$,
tending to $0.25 = (\lambda_2/\lambda_1)^{2} =
(2/4)^{2}$: the eigenvalue error falls at the **square** of the vector rate.
Without the squaring the ratio would be $0.5$ — the value the angle ratio
approaches in ★2.

---

## ★2 — Vector and eigenvalue rates separately

**(a)** The angle between $\mathbf x_k$ and
$\mathbf v_1 = (0.707107, 0.707107)^{\mathsf T}$:

| $k$ | angle to $\mathbf v_1$ (degrees) | ratio | residual $\|A\mathbf x - R\mathbf x\|$ |
|---|---|---|---|
| 0 | 45.000000 | — | $1.000\times10^{0}$ |
| 1 | 26.565051 | 0.5903 | $8.000\times10^{-1}$ |
| 2 | 14.036243 | 0.5284 | $4.706\times10^{-1}$ |
| 3 | 7.125016 | 0.5076 | $2.462\times10^{-1}$ |
| 4 | 3.576334 | 0.5019 | $1.245\times10^{-1}$ |
| 5 | 1.789911 | 0.5005 | $6.244\times10^{-2}$ |

**(b)** The ratios tend to $\lambda_2/\lambda_1 = 0.5$: the **vector** converges
linearly at the eigenvalue ratio.

**(c)** The residual falls by exactly a factor 2 per step, the same rate as the
angle. That is expected — the residual is the vector error times the spectral
scale — and it is why a residual tolerance and a vector-accuracy tolerance are
the same statement, whereas an *eigenvalue* tolerance is satisfied earlier.

**(d)** The eigenvalue error shrinks by $0.25$ per iteration, i.e.
$\log_{10}0.25 = -0.602$ decades per iteration, so **1.66 iterations per decimal
digit** of eigenvalue. The vector angle shrinks by $0.5$, i.e. $0.301$ decades per
iteration, so **3.32 iterations per decimal digit** of eigenvector accuracy — the
factor of two of the lesson's caution. Both counts are for *this* matrix; a
different $\lambda_2/\lambda_1$ gives different ones, and for $\lambda_2/\lambda_1$
close to 1 the method is useless.

---

## ★3 — Repeated eigenvalues and non-unique axes

**(a)** $\boldsymbol\sigma = 40I$ has the single eigenvalue $40$ MPa with
multiplicity 3, and the eigenspace is all of $\mathbb{R}^{3}$ — every direction is
a principal axis.

**(b)** The tensor does not distinguish directions, so no direction can be
"the" principal axis: the eigenproblem is satisfied by every unit vector. A
transversely isotropic tensor with a repeated in-plane eigenvalue has the same
problem in two dimensions — the axis of symmetry is determined, but the two
in-plane axes may be any orthogonal pair in the plane.

**(c)** A solver may return any orthonormal basis of the eigenspace, and any
choice is correct. The question is ill-posed, not the algorithm; the only
requirement is that the returned vectors be orthonormal and that the residuals be
zero. Ranking the returned axes by "physical significance" is then the analyst's
problem, not the solver's.

**(d)** A nearly isotropic stress state produces axis directions that are
numerically reproducible but physically meaningless: the answer is decided by the
algorithm's rounding and by the tiny deviatoric part, so an azimuth quoted to a
degree is an artefact. The honest report is the deviatoric magnitude relative to
the pressure — here, at 40 MPa confining pressure a deviator of $0.1$ MPa moves
the axes arbitrarily.

---

## ★4 — The discrete Dirichlet Laplacian with four cells

**(a)** With $\Delta x = 1/4$ and three interior unknowns, the discrete operator
is $\frac{1}{\Delta x^{2}}\operatorname{tridiag}(-1,2,-1)$, and

$$\lambda_k = \frac{4}{\Delta x^{2}}\sin^{2}\frac{k\pi\Delta x}{2}
= 64\sin^{2}\frac{k\pi}{8}, \qquad k = 1,2,3 .$$

**(b)**

| $k$ | $\lambda_k$ | exact $(k\pi)^{2}$ | relative error |
|---|---|---|---|
| 1 | 9.372583 | 9.869604 | 5.036 % |
| 2 | 32.000000 | 39.478418 | 18.943 % |
| 3 | 54.627417 | 88.826440 | 38.501 % |

**(c)** The asymptotic estimate $(k\pi\Delta x)^{2}/12$ gives
$5.140$ %, $20.562$ % and $46.264$ %. It is right for $k = 1$, drifts for
$k = 2$, and overestimates by a factor 1.2 for $k = 3$.

**(d)** Only the $k=1$ comparison is legitimate: the series
$(k\pi\Delta x)^{2}/12$ assumes $k\pi\Delta x \ll 1$, and at $\Delta x = 1/4$,
$k = 3$ gives $k\pi\Delta x = 2.36$ rad — larger than 1, so the leading term is
not the whole story. The discrete eigenvalue is systematically *below* the exact
one for every $k$, which is the Rayleigh–Ritz lower-bound property: a subspace
trial space can only underestimate the eigenvalue.

---

## ★★5 — Deriving the two rates

**(a)** With $\mathbf x_0 = \sum_jc_j\mathbf v_j$ and
$A\mathbf v_j = \lambda_j\mathbf v_j$,

$$A^{k}\mathbf x_0 = c_1\lambda_1^{k}\left[\mathbf v_1
+ \sum_{j\ge2}\frac{c_j}{c_1}\left(\frac{\lambda_j}{\lambda_1}\right)^{k}
\mathbf v_j\right].$$

**(b)** Dividing by $c_1\lambda_1^{k}$ shows that the component transverse to
$\mathbf v_1$ has size $O\left((\lambda_2/\lambda_1)^{k}\right)$ relative to the
dominant one, and since the vectors are normalised the *angle* between
$\mathbf x_k$ and $\mathbf v_1$ is of that same order. $\square$

**(c)** Write the unit vector
$\mathbf x = \mathbf v_1\sqrt{1-\epsilon^{2}} + \mathbf u\epsilon$ with
$\mathbf u\perp\mathbf v_1$ and $\|\mathbf u\| = 1$. Then

$$R(\mathbf x) = (1-\epsilon^{2})\lambda_1 + \epsilon^{2}\,\mathbf u^{\mathsf T}A\mathbf u,
\qquad
R(\mathbf x) - \lambda_1 = \epsilon^{2}\left(\mathbf u^{\mathsf T}A\mathbf u - \lambda_1\right)
= O(\epsilon^{2}).$$

The step that uses orthogonality is the cross term: it would contribute
$2\epsilon\sqrt{1-\epsilon^{2}}\,\mathbf v_1^{\mathsf T}A\mathbf u$, and
$\mathbf v_1^{\mathsf T}A\mathbf u = \lambda_1\mathbf v_1^{\mathsf T}\mathbf u = 0$
*only because the eigenbasis is orthogonal* — which for a symmetric matrix is the
spectral theorem, and for a non-normal matrix is false (hence the caveat in §5 of
the lesson). $\square$

**(d)** It assumes $c_1\ne0$ (otherwise the iteration converges to the largest
eigenvalue in the orthogonal complement — the trap of ★★6) and
$|\lambda_1| > |\lambda_2|$ (otherwise the ratio is 1 and there is no convergence
at all). It also assumes $\lambda_1$ is real; for a complex dominant pair the
iterate never settles into a single direction and the Rayleigh quotient does not
converge — the matrix must be deflated or the problem treated as a $2\times2$
block.

---

## ★★6 — The start-vector trap, quantitatively

**(a)** Use the identity $\sin\theta = \frac{\mathrm{e}^{\mathrm{i}\theta} -
\mathrm{e}^{-\mathrm{i}\theta}}{2\mathrm{i}}$ and sum the geometric series:

$$\sum_{i=1}^{n}\sin\frac{ik\pi}{n+1}
= \Im\left[\sum_{i=1}^{n}\mathrm{e}^{\mathrm{i}ik\pi/(n+1)}\right]
= \Im\left[\mathrm{e}^{\mathrm{i}k\pi/(n+1)}
\frac{1 - \mathrm{e}^{\mathrm{i}kn\pi/(n+1)}}{1 - \mathrm{e}^{\mathrm{i}k\pi/(n+1)}}\right].$$

For even $k$ the numerator is $1 - \mathrm{e}^{\mathrm{i}k\pi} = 1 - 1 = 0$,
so the sum vanishes; for odd $k$ it equals $\cot\frac{k\pi}{2(n+1)}\ne0$. The
all-ones vector therefore has no component on any *even* mode. $\square$

**(b)** With $n = 20$, $\lambda_k = 2 - 2\cos\frac{k\pi}{21}$:

$$\lambda_{20} = 3.977661652450257, \qquad
\lambda_{19} = 3.911145611572281, \qquad
\lambda_{17} = 3.652477548631990 .$$

The returned value $3.9111456115722545$ is $\lambda_{19}$ — the largest **odd**
mode, i.e. the largest eigenvalue in the orthogonal complement of the all-ones
vector. Since $\lambda_{\max} = \lambda_{20}$ is invisible, the iteration finds
the largest eigenvalue it can see.

**(c)** The relevant rate is not $\lambda_{19}/\lambda_{20}$ but the ratio inside
the visible subspace:

$$\text{full problem: } \frac{\lambda_{19}}{\lambda_{20}} = 0.9832776, \qquad
\text{trapped iteration: } \frac{\lambda_{17}}{\lambda_{19}} = 0.9338639 .$$

The trapped problem has a *better separated* top eigenvalue, so it converges
faster: the ratio of iteration counts for a given tolerance is
$\ln(0.9833)/\ln(0.9339) = 0.246$, i.e. about **four times fewer** iterations. At
229 iterations the trapped run has error of order
$0.93386^{229} \approx 1.6\times10^{-7}$, whereas an honest run at the full rate
would still be at $0.98328^{229} \approx 2.1\times10^{-2}$. The iteration reports
success five orders of magnitude more convincingly *because* it is solving the
wrong problem — there is no warning available from inside the algorithm.

**(d)** Two defences:

1. **A start vector with components everywhere** — a pseudo-random vector, or
   explicitly the sum of several modes. Cost: none beyond the vector; the price is
   that the iteration count becomes the honest (slower) one.
2. **An independent check of the returned value** — the Gershgorin radius, a
   bound from $\|A\|_1$, or a few steps of a second method from a different start.
   Cost: one $O(n^{2})$ pass for the norm, or a doubled iteration budget. The
   appropriate check is a *lower* bound: if the returned $\lambda$ is far below
   the bound $\max_i\sum_j|a_{ij}|$, the run is suspect.

---

## ★★7 — Principal axes of a rotated tensor

**(a)** With $c = \cos40^\circ = 0.766044$ and $s = \sin40^\circ = 0.642788$,

$$Q = \begin{pmatrix} c & -s & 0\\ s & c & 0\\ 0 & 0 & 1\end{pmatrix}, \qquad
\boldsymbol\sigma = Q\operatorname{diag}(80,45,20)Q^{\mathsf T},$$

so the principal stresses are $80$, $45$ and $20$ MPa by construction — the
eigenvalues of a diagonal matrix are invariant under an orthogonal similarity.

**(b)** The eigenvectors are the columns of $Q$:
$(c, s, 0) = (0.766044, 0.642788, 0)$ for $80$ MPa,
$(-s, c, 0) = (-0.642788, 0.766044, 0)$ for $45$ MPa, and $(0,0,1)$ for
$20$ MPa. The lesson reports $(+0.7660, +0.6428, 0)$,
$(+0.6428, -0.7660, 0)$ and $(0,0,1)$: the second vector is the negative of the
computed one, which is the same eigenvector (eigenvectors are defined up to
sign), and the lesson's sign convention is the one that makes the first two
mutually orthogonal with a positive first component. Both are correct.

**(c)** The $z$ axis is invariant because the rotation axis is the vertical: a
vector along $\hat z$ is fixed by a rotation about $\hat z$, so the corresponding
eigenvector is unchanged, and its eigenvalue $20$ MPa is not mixed with the other
two. Physically, rotating the horizontal stress axes about the vertical leaves the
vertical stress alone.

**(d)** For a rotation about $\hat y$ the invariant direction becomes $\hat y$:
the eigenvector with the middle eigenvalue is $(0,1,0)$, and the other two
eigenvectors $(c,0,\pm s)$-type combinations rotate in the $x$–$z$ plane. The
eigenvalue set is unchanged — the same three numbers $80$, $45$, $20$ MPa — which
is the general statement that a similarity transformation moves eigenvectors and
leaves eigenvalues alone.

---

## ★★8 — The Jacobi rotation

**(a)** Apply $J(p,q,\theta)$ to $A$ on both sides. The $(p,q)$ entry of
$J^{\mathsf T}AJ$ is

$$a'_{pq} = \tfrac{1}{2}\sin 2\theta\,(a_{qq} - a_{pp}) + \cos 2\theta\,a_{pq},$$

so $a'_{pq} = 0$ requires $\tan 2\theta = \dfrac{2a_{pq}}{a_{pp} - a_{qq}}$, i.e.
$\cot 2\theta = \dfrac{a_{qq} - a_{pp}}{2a_{pq}}$. $\square$

**(b)** Taking $\theta = \tfrac12\arctan\!\left(\dfrac{2a_{pq}}{a_{qq}-a_{pp}}\right)$
gives the same $\tan 2\theta$ up to the sign convention of $\arctan$; the two
forms differ by $\pi/2$ in $2\theta$, i.e. by a swap of the two rotated axes,
which annihilates the same entry. Verifying: substitute
$2\theta = \arctan(u)$ where $u = 2a_{pq}/(a_{qq}-a_{pp})$, so
$\sin2\theta = u/\sqrt{1+u^{2}}$, $\cos2\theta = 1/\sqrt{1+u^{2}}$, and

$$a'_{pq} = \frac{1}{2}\frac{u}{\sqrt{1+u^{2}}}(a_{qq}-a_{pp})
+ \frac{1}{\sqrt{1+u^{2}}}a_{pq}
= \frac{a_{pq} + a_{pq}}{\sqrt{1+u^{2}}} - \frac{a_{pq}}{\sqrt{1+u^{2}}} = 0. \qquad\square$$

**(c)** If $a_{pp} = a_{qq}$ then $u$ is infinite, $\arctan$ tends to $\pi/2$, and
$\theta = \pi/4$. Then $\sin2\theta = 1$, $\cos2\theta = 0$, and part (a) gives
$a'_{pq} = \tfrac12(a_{qq}-a_{pp}) + 0 = 0$ — annihilated. ($\sigma = \pi/2$ is
also the choice that diagonalises a $2\times2$ block with equal diagonal entries
of the form $\begin{pmatrix}a&b\\b&a\end{pmatrix}$, whose eigenvectors are
$(1,\pm1)/\sqrt2$.)

**(d)** A sweep consists of up to $n(n-1)/2$ rotations, each $O(n)$ when applied
to the rows and columns, so $O(n^{3})$ per sweep; convergence typically needs a
handful of sweeps, giving the classical $O(n^{3})$ cost with a larger constant
than the QR algorithm's. What it buys is unconditional convergence for symmetric
matrices — no shift strategy, no deflation, no failure modes — and eigenvectors
for free as the accumulated product of the rotations, with
$\|Q^{\mathsf T}Q - I\|$ at round-off. For a $3\times3$ stress tensor (the
lesson's case: 2 rotations, eigenvalues to $1.4\times10^{-14}$) that trade is
obviously right; for a dense $10^{4}$ matrix it is not.

---

## ★★★9 — Lanczos with and without reorthogonalisation

The matrix is $A = \operatorname{diag}(1,2,\dots,97,\ 1000.0,\ 1000.001,\ 1000.002)$
and the start vector is the normalised all-ones vector, so the run is
deterministic. The Ritz values are the eigenvalues of the Lanczos tridiagonal
$T_k$, computed by Sturm-sequence bisection.

| $k$ | reorth | $\|V^{\mathsf T}V-I\|_{\infty}$ | Ritz within $10^{-6}$ | distinct exact eigenvalues | duplicates | largest Ritz |
|---|---|---|---|---|---|---|
| 20 | yes | $2.22\times10^{-16}$ | 3 | 3 | 0 | 1000.002000000 |
| 20 | no | $3.22\times10^{-4}$ | 3 | 3 | 0 | 1000.002000000 |
| 40 | yes | $2.22\times10^{-16}$ | 3 | 3 | 0 | 1000.002000000 |
| 40 | no | $7.02\times10^{-1}$ | 6 | 3 | 3 | 1000.002000000 |
| 60 | yes | $2.22\times10^{-16}$ | 11 | 11 | 0 | 1000.002000000 |
| 60 | no | $8.47\times10^{-1}$ | 14 | 8 | 6 | 1000.002000000 |
| 80 | yes | $2.22\times10^{-16}$ | 27 | 27 | 0 | 1000.002000000 |
| 80 | no | $9.09\times10^{-1}$ | 28 | 19 | 9 | 1000.002000000 |

**(b)** The largest Ritz value has converged by $k = 20$ — it equals
$1000.002000000$ to ten digits — and reorthogonalisation made **no** difference
to it: the two $k = 20$ rows agree to every printed digit even though the
orthogonality deviations differ by twelve orders of magnitude. This is the
lesson's first conclusion, reproduced on a different matrix: the loss of
orthogonality appears in the directions that have *already* converged and does not
prevent the extremes from converging.

**(c)** The first duplicates appear at $k = 40$ without reorthogonalisation
(3 duplicates) and none appear with it. They then grow quickly: 6 at $k=60$ and 9
at $k=80$, against 0 in the reorthogonalised runs at every $k$. Without
reorthogonalisation the *count* of converged Ritz values is inflated by about a
factor 1.5 at $k=80$ ($28$ reported against $19$ distinct eigenvalues), and the
inflation grows with $k$.

**(d)** 

*"Find the largest eigenvalue and its eigenvector"*: the
non-reorthogonalised run is **adequate**, and for this matrix it is indistinguishable
from the reorthogonalised one — the extreme Ritz value and its residual are
identical. The saving is real: reorthogonalisation costs $2k$ inner products per
step, $O(nk^{2})$ work overall, which for large $k$ dominates the single matvec.

*"Count how many eigenvalues lie in $[1,97]$"*: the non-reorthogonalised run is
**unusable**. At $k = 80$ it reports 28 Ritz values matching exact eigenvalues
when only 19 distinct eigenvalues have been found; the duplicates crowd out the
rest of the spectrum, so an interval count built on it is wrong by an amount no
residual check can detect. Selective reorthogonalisation against the converged
Ritz vectors — the standard compromise — gives the count without the full cost.

---

## ★★★10 — "The smallest singular values are noise"

**(a)** For a matrix $A$ with singular values $\sigma_i$, the eigenvalues of
$A^{\mathsf T}A$ are $\sigma_i^{2}$, so
$\kappa_2(A^{\mathsf T}A) = (\sigma_{\max}/\sigma_{\min})^{2} =
\kappa_2(A)^{2}$. The relative error of an eigenvector-based computation is
bounded by roughly $\kappa$ times the unit round-off, so the normal-equation route
is at risk when $\kappa_2(A)^{2}\gtrsim 1/\epsilon$. With
$\epsilon = 2.2\times10^{-16}$, that is $\kappa_2(A)\gtrsim 6.7\times10^{7}$ — a
condition number that is ordinary for a tomographic kernel with $10^{5}$ unknowns,
since the singular values typically decay over many decades.

**(b)** Perturbing $A^{\mathsf T}A$ by a relative $O(\epsilon)$ moves its
smallest eigenvalue by up to $\epsilon\|A^{\mathsf T}A\| = \epsilon\sigma_{\max}^{2}$,
which is a relative change of $\epsilon\kappa_2(A^{\mathsf T}A) =
\epsilon\kappa_2(A)^{2}$ in $\sigma_{\min}^{2}$. The small singular values are
therefore the first to be overwhelmed: at $\kappa = 10^{9}$ the amplification is
$10^{18}\epsilon \approx 220$, so the computed value can have the wrong sign
entirely. Calling the result "noise" is a correct description of the *computed*
quantity and an incorrect description of the *problem*: the true small singular
values carry the information that the inversion's resolution depends on.

**(c)** The Ritz-value theory of §3.6 explains why the *extremes* of a Lanczos
run are reliable and why the *counting* is not; it does not say that a squaring of
the condition number is harmless. What it rescues is a Lanczos (or Arnoldi)
computation performed **on $A$ itself** — through the normal equations of the
eigenproblem of $A^{\mathsf T}A$, the squaring has already happened before any
iteration begins, and no iterative method can undo it.

**(d)** In order of preference:

1. **Use the SVD of $A$ directly** (bidiagonalisation, or a Lanczos-type
   bidiagonal method such as LSQR/Golub–Kahan) and truncate at a stated level.
   The error then scales as $\kappa_2(A)\epsilon$ instead of
   $\kappa_2(A)^{2}\epsilon$ — a saving of every digit the squaring destroyed — and
   the truncation level is an explicit, reportable decision. Cost: about twice the
   work per iteration of a symmetric solve and a bidiagonal factor to store.
2. **Regularise the normal equations** (Tikhonov: solve
   $(A^{\mathsf T}A + \alpha I)m = A^{\mathsf T}d$ instead) and report the
   resolution matrix rather than the model alone. Cost: one parameter to choose
   and justify, and the small singular values that were "noise" are now explicitly
   damped rather than implicitly corrupted. Note the honest framing: this does not
   recover the lost information, it replaces an uncontrolled error with a
   controlled bias.

Forming $A^{\mathsf T}A$ may still be worth it when the problem is small or
well conditioned — it halves the storage and allows a Cholesky solve — but for a
$10^{5}$-parameter tomographic kernel the decision should be made from a measured
condition number, not from convenience.
