# Solutions — 01-16-04 Spectral Theory of Operators and Eigenfunction Bases

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output; values marked "computed for these solutions"
> come from the calculation shown.

---

## ★1 — Reality and orthogonality of eigenvalues

**Reality.** Let $Lu = \lambda u$ with $\lVert u\rVert = 1$. Then

$$\lambda = \lambda\langle u,u\rangle = \langle Lu,u\rangle
= \langle u,Lu\rangle = \overline{\langle Lu,u\rangle} = \bar\lambda ,$$

where the third step is the definition of self-adjointness
$\langle L u,u\rangle = \langle u,Lu\rangle$ and the fourth is conjugate symmetry
of the inner product. So $\lambda = \bar\lambda$ and $\lambda \in \mathbb{R}$. The
hypotheses used: self-adjointness (third step) and conjugate symmetry (fourth).

**Orthogonality.** Let $Lu = \lambda u$ and $Lv = \mu v$ with
$\lambda \ne \mu$, both real. Then

$$\lambda\langle u,v\rangle = \langle Lu,v\rangle = \langle u,Lv\rangle
= \mu\langle u,v\rangle ,$$

so $(\lambda - \mu)\langle u,v\rangle = 0$; since $\lambda \ne \mu$, the inner
product vanishes. Only self-adjointness is used. Note that neither argument needs
compactness — compactness is needed for the existence of *enough* eigenvectors to
form a basis.

---

## ★2 — Discrete eigenvalues lie below the continuum ones

For $0 < x < \pi/2$ we have $0 < \sin x < x$; putting $x = k\pi h/2$ and squaring,

$$\sin^2\!\left(\frac{k\pi h}{2}\right) < \frac{k^2\pi^2h^2}{4}
\ \Longrightarrow\
\frac{4\sin^2(k\pi h/2)}{h^2} < k^2\pi^2 .$$

**Rayleigh quotient interpretation.** Write $A$ for the second-difference matrix
and $R(v) = v^{\mathsf T}\!Av/v^{\mathsf T}v$. For the continuum operator
$L = -d^2/dx^2$ with Dirichlet conditions,
$\lambda_k = \min_{\dim V = k}\max_{0\ne v\in V}R(v)$, the Courant–Fischer
characterisation. The $n$-dimensional trial space of the discretisation is a
*subspace* of the continuum energy space, so the minimum over it cannot be below
the minimum over the whole space: $\lambda_k^{(h)} \ge \lambda_k$. Combined with
the explicit formula, which shows the reverse inequality, the discrete eigenvalues
are lower bounds. The practical consequence is that a finite-element eigenvalue is
never too high and approaches from below, so a converged eigenvalue is identified
by stabilising, not by crossing.

---

## ★3 — The spectral theorem

**Statement.** If $K$ is compact and self-adjoint on a Hilbert space $H$, then $K$
has a complete orthonormal set of eigenvectors; the eigenvalues are real and the
eigenvectors for distinct eigenvalues are orthogonal; the nonzero eigenvalues form
a sequence tending to zero; and $Kf = \sum_k\lambda_k\langle f,u_k\rangle u_k$.

**Accumulation only at zero.** If infinitely many eigenvalues satisfied
$\lvert\lambda_k\rvert\ge\delta>0$, the corresponding orthonormal eigenvectors
would have $\lVert Ku_m - Ku_n\rVert^2 = \lambda_m^2 + \lambda_n^2 \ge
2\delta^2$, so the image of the bounded sequence $\{u_k\}$ would have no
convergent subsequence — contradicting compactness. Conversely, if $\sigma_k\to0$
the operator is a norm limit of finite-rank operators, and a norm limit of compact
operators is compact: this is the sense in which "the eigenvalues decay" and "the
operator is compact" are the same statement.

---

## ★4 — Truncation error in two norms

**(a)** For $R = h\sum_{k=1}^{4}a_k\varphi_k\varphi_k^{\mathsf T}$ with orthonormal
$\varphi_k$, truncating after $r$ terms leaves
$R - R_r = h\sum_{k>r}a_k\varphi_k\varphi_k^{\mathsf T}$, a self-adjoint operator
whose nonzero eigenvalues are $a_{r+1},\dots$ with orthonormal eigenvectors. Its
operator norm is therefore the largest remaining eigenvalue,
$\lvert a_{r+1}\rvert$. Dividing by $\lVert R\rVert = \lvert a_1\rvert$:

| $r$ | $\lvert a_{r+1}\rvert/\lvert a_1\rvert$ |
|---|---|
| 1 | $0.4$ |
| 2 | $0.1$ |
| 3 | $0.02$ |

**(b)** For the gravity kernel the quoted normalised eigenvalues are
$1.0000, 0.7924, 0.6299, 0.4989, 0.3953, 0.3127, \dots$, so the operator-norm
relative truncation errors are $\lvert\lambda_{r+1}\rvert/\lvert\lambda_1\rvert$:

| $r$ | measured entrywise | operator norm |
|---|---|---|
| 1 | $9.613\times10^{-1}$ | $0.7924$ |
| 2 | $8.833\times10^{-1}$ | $0.6299$ |
| 4 | $6.770\times10^{-1}$ | $0.3953$ |
| 8 | $3.048\times10^{-1}$ | $0.1546$ |

The entrywise error is larger because it is a *maximum over entries* of
$\lvert\sum_{k>r}\lambda_ku_k(x_i)u_k(x_j)\rvert$ — a sum whose terms can add
constructively at some $(i,j)$ — while the operator norm is the largest single
coefficient. Neither is "the" error; the operator norm is the right one for
questions about how much the operator changes an input, and the entrywise norm is
the right one for questions about a specific predicted datum. Both must be named.

---

## ★5 — Mode counting and spacing

**Counting.** Wavenumbers on a fixed-fixed string are $k_n = n\pi/L$, spaced by
$\pi/L$. The number below $K$ is the number of integers $n$ with $n\pi/L \le K$,
i.e. $\lfloor KL/\pi\rfloor \approx KL/\pi$.

For $L = 25$ m and $K = 40$ rad/m: $KL/\pi = 1000/\pi = 318.31$, so **318 modes**
(slightly fewer than the continuous estimate because of the floor).

**Spacing.** $\lambda_1 = (\pi/25)^2 = 0.01579105$ and
$\lambda_2 = 4\lambda_1 = 0.06316419$, so
$\lambda_2 - \lambda_1 = 3\lambda_1 = 0.04737314$. Doubling $L$ quarters every
eigenvalue and therefore quarters the spacing to $0.01184329$: the low-frequency
modes crowd together as the resonator grows, which is the mechanism of Section 5
of the lesson.

---

## ★6 — Eigenvalues of the second difference

**Derivation.** Take $v_i = \sin(ik\pi h)$ for $i = 1,\dots,n$ with
$h = 1/(n+1)$. Then

$$\frac{-v_{i-1} + 2v_i - v_{i+1}}{h^2}
= \frac{2 - 2\cos(k\pi h)}{h^2}v_i
= \frac{4\sin^2(k\pi h/2)}{h^2}v_i ,$$

using the identity $1 - \cos\theta = 2\sin^2(\theta/2)$. The boundary conditions
$v_0 = v_{n+1} = 0$ are satisfied because $\sin(0) = 0$ and
$\sin((n+1)k\pi h) = \sin(k\pi) = 0$ for integer $k$. So the eigenvalues are
$4\sin^2(k\pi h/2)/h^2$, $k = 1,\dots,n$, and the eigenvectors are the sampled
sines. The demonstration confirms both numerically for $n=24$: the eigensolver
output agrees with the formula to every printed digit, and the eigenvectors match
the sampled sines to $4.1\times10^{-15}$ after normalisation — i.e. exactly, up to
round-off, because the identity above is exact.

**Largest eigenvalue.** Taking $k = n$ and using $\sin(x) = \cos(\pi/2 - x)$,

$$\lambda_{\max} = \frac{4\sin^2\!\big(\frac{n\pi h}{2}\big)}{h^2}
= \frac{4\cos^2\!\big(\frac{\pi h}{2}\big)}{h^2}
\ \xrightarrow[h\to0]{}\ \frac{4}{h^2} ,$$

since $\cos(\pi h/2)\to1$. For $h = 1/25 = 0.04$:
$\lambda_{\max} = 4\cos^2(\pi/50)/0.04^2 = 2490.1434$ against $4/h^2 = 2500$, a
ratio of 0.99606.

---

## ★7 — Resolution matrix bounds and a hand computation

**Trace bound.** In the eigenbasis of $F^{\mathsf T}F$ (or, for a symmetric $F$,
of $F$), $R_\alpha$ has entries $\lambda_k/(\lambda_k+\alpha)$ with
$0 \le \lambda_k/(\lambda_k+\alpha) < 1$ for $\alpha > 0$ and $\lambda_k \ge 0$.
Hence $\operatorname{tr}R_\alpha = \sum_{k=1}^n\lambda_k/(\lambda_k+\alpha) <
n$. (For $\alpha = 0$ with $\lambda_k > 0$ the trace equals $n$ exactly.)

**Convergence to the identity.** With full column rank, all $\lambda_k > 0$, so
for each $k$, $\lambda_k/(\lambda_k+\alpha)\to1$ as $\alpha\to0$. The eigenvalue
of largest magnitude of $R_\alpha - I$ is
$\max_k \alpha/(\lambda_k+\alpha) = \alpha/(\lambda_{\min}+\alpha)\to0$, so
$\lVert R_\alpha - I\rVert\to0$. **The limit is exact but useless**: taking
$\alpha\to0$ recovers the identity resolution matrix at the cost of unbounded
variance, which is the entire content of the regularisation trade-off.

**Hand computation** for the separable kernel, $\alpha = 10^{-2}$,
$a = (1,0.4,0.1,0.02)$ so $\lambda_k = a_k^2 = (1, 0.16, 0.01, 4\times10^{-4})$:

$$\operatorname{tr}R_\alpha
= \frac{1}{1+\alpha/1} + \frac{1}{1+\alpha/0.16}
+ \frac{1}{1+\alpha/0.01} + \frac{1}{1+\alpha/4\times10^{-4}}$$

$$= 0.99009901 + 0.94117647 + 0.50000000 + 0.03846154 = 2.46973702 .$$

So at $\alpha = 10^{-2}$ the data resolve **about 2.47 of the 4 retained
parameters** — or 2.47 of the 40 total, since the other 36 eigenvalues are zero
and contribute nothing. The fourth mode is essentially unresolved
(filter factor 0.038) and the third is resolved only halfway. This is exactly the
behaviour of the lesson's table for the gravity kernel, where
$\operatorname{tr}R_\alpha$ fell from 58.59 at $\alpha=10^{-8}$ to 15.19 at
$\alpha=10^{-2}$; the difference is that here the whole spectrum is known in
closed form.

---

## ★8 — Edge versus centre averaging kernels

Computed for these solutions on the gravity kernel at $z = 0.05$ with $n = 60$,
counting the number of grid nodes at or above half the kernel's peak:

| $\alpha$ | centre half-width (cells) | edge half-width (cells) |
|---|---|---|
| $10^{-2}$ | 5 | 3 |
| $10^{-3}$ | 3 | 2 |
| $10^{-4}$ | 3 | 1 |

**(a)** The edge kernels are consistently narrower: 3, 2, 1 cells against 5, 3, 3.

**(b)** The kernel is a function of $x - y$ and so is symmetric about the
parameter it belongs to, in the interior. At parameter index 1 there is no
parameter to its left, so only half the kernel is represented in the model vector:
the row of $R_\alpha$ is one-sided, and a half-width measured by counting nodes
above half the peak spans fewer nodes because the other side of the kernel does
not exist in the discretisation. The narrower half-width does **not** mean better
resolution at the edge.

**(c)** A boundary parameter is constrained by fewer data and its averaging
kernel is asymmetric, so its uncertainty is larger and its effective resolution
anisotropic. Two consequences for interpretation: a model feature at the edge of a
survey cannot be compared directly with an interior feature of the same apparent
width, and any resolution plot should show the rows at the edges as well as at the
centre — a centre-only display flatters the inversion. The honest measure at a
boundary is the one-sided moment or the full covariance, not a half-width.

---

## ★9 — Spectrum of the discretised Laplacian

**(a)** With $h = 1/(n+1)$ and
$\lambda_{\max} = 4\cos^2(\pi h/2)/h^2$ (computed for these solutions):

| $n$ | $h$ | $\lambda_{\max}$ | $4/h^2$ | ratio |
|---|---|---|---|---|
| 24 | 0.040000 | 2490.1434 | 2500.0 | 0.996057 |
| 48 | 0.020408 | 9594.1338 | 9604.0 | 0.998973 |
| 96 | 0.010309 | 37626.1313 | 37636.0 | 0.999738 |
| 192 | 0.005181 | 148986.1306 | 148996.0 | 0.999934 |

The ratio tends to 1 from below, confirming $\lambda_{\max}\sim4/h^2$.

**(b)** With $\lambda_{\min} = 4\sin^2(\pi h/2)/h^2$:

| $n$ | $\lambda_{\min}$ | $\lambda_{\max}/\lambda_{\min}$ |
|---|---|---|
| 24 | 9.856623 | $2.526\times10^{2}$ |
| 48 | 9.866224 | $9.724\times10^{2}$ |
| 96 | 9.868742 | $3.813\times10^{3}$ |
| 192 | 9.869386 | $1.510\times10^{4}$ |

$\lambda_{\min}\to\pi^2 = 9.8696$ while $\lambda_{\max}\sim4/h^2\sim4n^2$, so the
ratio grows like $n^2$ (each doubling multiplies it by about 3.9 to 4.0). This is
the $h^{-2}$ growth quoted in the lesson, and it is a property of the
discretisation, not of the physics: the physical operator's spectrum on a bounded
interval is bounded.

**(c)** A Krylov solver for $Au = b$ converges at a rate governed by the
eigenvalue *distribution* of $A$, and its worst-case bound depends on the ratio of
extreme eigenvalues (or, more precisely, on how well a polynomial can be made
small on the spectrum). The physical Poisson problem has a fixed continuous
spectrum, but the discretised matrix that the solver actually sees has
$\lambda_{\max}/\lambda_{\min}\sim n^2$; hence, roughly, the iteration count grows
like $n$ (and like $h^{-1}$) — the well-known behaviour of conjugate gradients on
the Poisson equation, and the reason multigrid and preconditioners exist. The
conditioning is an artefact of the mesh, and preconditioning is the act of
removing it.

---

## ★10 — Paragraph on a normal-mode measurement

> The measured spectrum is the point spectrum of the elastodynamic operator for a
> self-adjoint, gravitating, rotating, anelastic Earth model linearised about a
> hydrostatic reference, restricted to a finite volume with a free surface and
> regularity at the centre; its eigenfunctions are the spheroidal and toroidal
> modes and its eigenvalues are their squared frequencies. The spectrum is
> **discrete** because the domain is bounded and the operator is self-adjoint with
> a compact resolvent: enlarging the domain would shrink the spacing of the low
> modes and, in the unbounded limit, fill the axis with a continuum, at which
> point individual modes would no longer be identifiable. The eigenvalues depend
> on the boundary conditions as much as on the material properties — replacing the
> free surface by a rigid one changes every frequency — so a reported mode
> frequency is meaningless without the model's boundary conditions. A **split
> multiplet** is the first-order splitting of a $(2l+1)$-fold degenerate
> eigenfrequency by a perturbation of the operator (rotation, ellipticity, lateral
> heterogeneity): the degeneracy is an artefact of the symmetry of the reference
> operator, and the splitting measures the perturbation through the matrix
> elements of the perturbing operator in the unperturbed eigenbasis.

Every clause is supported by this lesson: discreteness and the bounded-domain
argument from Section 5, the role of boundary conditions from Section 7, and the
perturbative splitting from the eigenbasis expansion of Sections 2 and 3.
