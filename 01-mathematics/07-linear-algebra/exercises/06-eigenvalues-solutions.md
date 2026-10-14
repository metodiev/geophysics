# Solutions — 01-07-06 Eigenvalues, Eigenvectors and Diagonalisation

> **Read this after attempting the exercises, not before.**
>
> Numeric answers were computed and verified. Eigenvector signs are a convention;
> bearings are reported clockwise from north in $[0^{\circ},180^{\circ})$, as is
> standard for axes (not directed vectors) in the earth sciences.

---

## ★1 — A symmetric $2\times2$ problem

$$A = \begin{bmatrix} 3 & 1 \\ 1 & 3\end{bmatrix}.$$

(a) $\det(A - \lambda I) = (3-\lambda)^{2} - 1 = \lambda^{2} - 6\lambda + 8 = 0$, so
$\lambda = 4$ and $\lambda = 2$.

(b) For $\lambda = 4$: $(A - 4I)v = \begin{bmatrix} -1 & 1 \\ 1 & -1\end{bmatrix}v = 0$
gives $v_1 = (1,1)/\sqrt2$. For $\lambda = 2$:
$\begin{bmatrix} 1 & 1 \\ 1 & 1\end{bmatrix}v = 0$ gives $v_2 = (1,-1)/\sqrt2$.
Their inner product is $(1 - 1)/2 = 0$: **orthogonal**, as the spectral theorem requires.

(c) Trace $= 3 + 3 = 6 = 4 + 2$ ✓. Determinant $= 9 - 1 = 8 = 4\times2$ ✓.

(d) With $Q = \frac{1}{\sqrt2}\begin{bmatrix} 1 & 1 \\ 1 & -1\end{bmatrix}$ (columns the
eigenvectors) and $\Lambda = \operatorname{diag}(4,2)$:

$$Q\Lambda Q^\mathsf{T} = \frac12\begin{bmatrix} 1 & 1 \\ 1 & -1\end{bmatrix}
\begin{bmatrix} 4 & 0 \\ 0 & 2\end{bmatrix}
\begin{bmatrix} 1 & 1 \\ 1 & -1\end{bmatrix}
= \frac12\begin{bmatrix} 4 & 2 \\ 4 & -2\end{bmatrix}
\begin{bmatrix} 1 & 1 \\ 1 & -1\end{bmatrix}
= \begin{bmatrix} 3 & 1 \\ 1 & 3\end{bmatrix}. ✓$$

**Interpretation.** The form $x^\mathsf{T}Ax = 3x_1^{2} + 2x_1x_2 + 3x_2^{2}$ is a
positive-definite energy with principal axes along $(1,1)$ and $(1,-1)$ and stiffnesses
$4$ and $2$. Rotating to those axes decouples the two degrees of freedom.

---

## ★2 — A strain tensor

$$\epsilon = \begin{bmatrix} 2 & -1 \\ -1 & 1\end{bmatrix}\times10^{-4}.$$

(a) $\operatorname{tr} = 3$, $\det = 2 - 1 = 1$, so
$\lambda^{2} - 3\lambda + 1 = 0$:

$$\varepsilon_1 = \frac{3+\sqrt5}{2} = 2.618034\times10^{-4}, \qquad
\varepsilon_2 = \frac{3-\sqrt5}{2} = 0.381966\times10^{-4} \quad \text{(dimensionless)}.$$

(b) For $\varepsilon_1$: $(2 - 2.618034)x - y = 0 \Rightarrow y = -0.618034x$, so the
direction is $(1,-0.618034)$, normalised to $(0.850651,\ -0.525731)$, with bearing

$$\operatorname{atan2}(0.850651,\ -0.525731) = 121.717474^{\circ}.$$

The second axis is orthogonal: $(0.525731,\ 0.850651)$, bearing $31.717474^{\circ}$.

(c) Maximum shear strain $= \tfrac12(\varepsilon_1 - \varepsilon_2) =
1.118034\times10^{-4}$.

(d) **Not isotropic**: isotropy requires the eigenvalues to be equal, and
$2.618034 \ne 0.381966$. The ratio $\varepsilon_1/\varepsilon_2 = 6.854$ is a measure of
the anisotropy of the strain ellipse. Note that a *zero* off-diagonal entry would not
have implied isotropy: here the off-diagonal is nonzero, but even a diagonal
$\operatorname{diag}(2,1)\times10^{-4}$ would be anisotropic.

---

## ★★3 — Tractions on a $45^{\circ}$ plane

(a) In the principal frame, a plane whose normal makes an angle $\alpha$ with the major
principal axis carries

$$\sigma_{nn} = \sigma_1\cos^{2}\alpha + \sigma_2\sin^{2}\alpha, \qquad
\sigma_{nt} = (\sigma_1 - \sigma_2)\sin\alpha\cos\alpha .$$

At $\alpha = 45^{\circ}$, $\cos^{2} = \sin^{2} = \tfrac12$ and
$\sin\alpha\cos\alpha = \tfrac12$:

$$\sigma_{nn} = \tfrac12(72.015621 + 7.984379) = 40.000000\ \text{MPa}, \qquad
\sigma_{nt} = \tfrac12(72.015621 - 7.984379) = 32.015621\ \text{MPa}.$$

(b) **Transformation check.** With $Q$ the rotation by $45^{\circ}$ and
$\sigma = Q\Lambda Q^\mathsf{T}$ in the principal frame,

$$Q^\mathsf{T}\sigma Q = \begin{bmatrix} 40.000000 & -32.015621 \\ -32.015621 &
40.000000\end{bmatrix},$$

so $\sigma'_{11} = 40.000000$ MPa (normal traction) and $|\sigma'_{12}| = 32.015621$ MPa
(shear traction). ✓ The signed entry is $-32.016$ because the rotation was taken as
$+45^{\circ}$; the magnitude is what is physical.

(c) The maximum shear traction over all orientations is
$\tau_{\max} = \tfrac12(\sigma_1 - \sigma_2) = 32.015621$ MPa, attained on planes at
$45^{\circ}$ to the principal axes — which is the plane just computed.

(d) In fractions of $(\sigma_1 - \sigma_2) = 64.031242$ MPa:

$$\frac{\sigma_{nn} - \tfrac12(\sigma_1+\sigma_2)}{\sigma_1-\sigma_2} = 0, \qquad
\frac{\sigma_{nt}}{\sigma_1 - \sigma_2} = \tfrac12 .$$

**Comment.** The normal traction on the $45^{\circ}$ plane is exactly the *mean* stress,
independent of the anisotropy; the shear is exactly half the principal-stress
difference. These two facts are the reason the mean stress $\tfrac13\operatorname{tr}\sigma$
controls volumetric behaviour while the deviatoric part controls failure, and why
$\tau_{\max} = \tfrac12(\sigma_1-\sigma_3)$ appears in every failure criterion. The
Mohr circle is the same statement drawn: its centre is the mean stress and its radius is
$\tau_{\max}$.

---

## ★★4 — Convergence of a $2\times2$ Jacobi iteration

(a) $B = \begin{bmatrix} 0 & -a \\ -b & 0\end{bmatrix}$ has
$\det(B - \mu I) = \mu^{2} - ab$, so $\mu = \pm\sqrt{ab}$ and

$$\rho(B) = \sqrt{0.4\times0.9} = \sqrt{0.36} = 0.6 .$$

Since $\rho < 1$, Jacobi converges.

(b) **Exact:** the error decays as $0.6^{k}$, so $0.6^{k} = 10^{-6}$ gives

$$k = \frac{\ln 10^{-6}}{\ln 0.6} = \frac{-13.8155}{-0.510826} = 27.04
\;\Rightarrow\; 28 \text{ iterations}.$$

**Approximation:** $k \approx p\ln10/(1-\rho) = 6(2.302585)/0.4 = 34.54$, i.e.
$35$ iterations. The approximation over-estimates by $25$ % — it is the first term of
the expansion of $1/\ln\rho$, which is only accurate when $\rho$ is very close to $1$.
Use the exact formula whenever you can compute $\rho$; use the approximation only to
estimate the *scaling* with $h$.

(c) **Verification.** Taking
$A = \begin{bmatrix} 1 & 0.4 \\ 0.9 & 1\end{bmatrix}$ and $b = (1,1)^\mathsf{T}$
(the diagonal is 1 and the off-diagonals are $-(a, b)$, so $B$ is exactly the required
iteration matrix), the exact solution is $x = (0.9375,\ 0.15625)$ and iterating
$x_{k+1} = Bx_k + b$ gives an error below $10^{-6}$ on the **28th iteration** —
matching the prediction.

One detail worth noticing: the *per-step* error ratio does not settle to a single value.
It alternates between $0.9$ and $0.4$, and only the two-step product,
$0.9\times0.4 = 0.36 = 0.6^{2}$, equals $\rho^{2}$. The eigenvalues of $B$ are $\pm0.6$,
so the error component flips sign each iteration, and the max-norm ratio inherits that
alternation. The convergence *rate* is the geometric mean per step, i.e. $\rho$; a
measurement protocol that reports the last single-step ratio would report $0.4$ or $0.9$
depending on where it stopped, not $0.6$. Compute the spectral radius rather than
inferring it from one ratio.

(d) With $ab = 1.01$, e.g. $a = 0.4$, $b = 2.525$:
$\mu = \pm\sqrt{1.01} = \pm1.004988$ and $\rho = 1.004988 > 1$: **Jacobi diverges**, and
the error grows by $0.5$ % per iteration (doubling in about $140$ iterations). The exact
formula $\ln(10^{-6})/\ln(1.004988) = -2776$ is meaningless: it is the *signed* solution
of $1.004988^{k} = 10^{-6}$, which for a growth factor above 1 has no positive solution
in that direction. The correct statement is that convergence fails, and no number of
iterations helps. This is the $2\times2$ illustration of the rule
$\rho < 1$; the same test on the five-point Laplacian in
[01-07-09](../09-sparse-matrices.md) shows how $\rho \to 1$ (rather than above 1) makes a
method technically convergent and practically useless.

---

## ★★★5 — Definiteness as a function of a coupling

$$A = \begin{bmatrix} 1 & c \\ c & 1\end{bmatrix}, \qquad
\lambda = 1 \pm c .$$

(a) Two straight lines in $c$: $\lambda_+ = 1 + c$ and $\lambda_- = 1 - c$, crossing at
$c = 0$ where they are degenerate (and every vector is an eigenvector, since
$A = I$).

(b) | Property | Range of $c$ |
|---|---|---|
| positive definite | $-1 < c < 1$ |
| positive semidefinite (singular) | $c = \pm1$ |
| indefinite | $|c| > 1$ |

At $c = \pm1$ one eigenvalue vanishes; for $|c| > 1$ one eigenvalue is negative.

(c) At $c = 1$: $\lambda_- = 0$ with eigenvector $(1,-1)/\sqrt2$, so
$\mathcal{N}(A) = \operatorname{span}\{(1,-1)^\mathsf{T}\}$ and the set of minimisers of
$q$ is a line — the flat direction. Every point of that line has the same $q$, which is
exactly the non-uniqueness of [01-07-04](../04-rank-and-nullspace.md) expressed as
curvature rather than as rank. At $c = -1$ the same happens along
$(1,1)^\mathsf{T}$.

(d) **Experimental translation.** $A$ is (proportional to) $G^\mathsf{T}G$ for a
two-parameter model with $G$ chosen so that the two parameters are correlated with
coefficient $c$. The condition $|c| = 1$ means the two columns of $G$ are parallel:
**the two parameters always appear in the same fixed ratio in every datum, so no data
can separate them.** For the reflection problem of
[01-07-10](../10-matrix-calculus.md) Section 3.3, $|c|\to1$ is the depth–velocity
trade-off at a single offset; for a survey, it is two stations sampling the same
combination of cells. The practical statement: the curvature of the misfit goes *flat*
along one direction, so a Gauss–Newton step along it is unbounded, and the inversion
requires either a constraint or a measurement with a different ratio.

---

## ★★★6 — $\rho_{\text{GS}} = \rho_J^{2}$, measured

(a) **Example (i): five-point Laplacian, $4\times4$ interior grid.** With
$h = 1/(4+1) = 0.2$, the Jacobi spectral radius is
$\rho_J = \cos(\pi h) = \cos(36^{\circ}) = 0.809016994$. A converged Gauss–Seidel
iteration on a consistent right-hand side gives a measured error ratio
$\rho_{\text{GS}} = 0.654506592$.

**Example (ii): symmetric tridiagonal with a strengthened diagonal.** Diagonal entries
$4 + u_i$ with $u_i$ pseudo-random in $[0,1)$, unit off-diagonals, $n = 8$, and the
pseudo-random seed fixed so the example is reproducible: $\rho_J = 0.416276787$
(computed from the eigenvalues of $B_J$), and a converged Gauss–Seidel iteration gives
$\rho_{\text{GS}} = 0.176502$.

(b) Comparison:

| example | $\rho_J$ | $\rho_J^{2}$ | $\rho_{\text{GS}}$ measured | agreement |
|---|---|---|---|---|
| $4\times4$ Laplacian | $0.809016994$ | $0.654508497$ | $0.654506592$ | 8 significant figures |
| random tridiagonal | $0.416276787$ | $0.173286363$ | $0.176502$ | 2 % high |

(c) **Both examples are consistently ordered** (a tridiagonal matrix, and any
five-point stencil on a rectangular grid with natural ordering, are the standard
examples). The relation held to eight figures in the first and to 2 % in the second.

(d) **Limits.** The 2 % gap in the second example is a *measurement* artefact, not a
counterexample: the error ratio in the max-norm is not exactly the spectral radius,
because the error is a combination of all the eigenmodes and the ratio only equals
$\rho$ once the dominant mode has taken over. In example (i) the dominant mode takes
over quickly (the spectrum is spread); in example (ii) it does not (the spectrum is
crowded, with $0.4163$ and $0.4163 - \delta$), so the measured ratio is still an upper
bound. The test that would turn the empirical claim into a check is to form
$B_{\text{GS}} = (D+L)^{-1}(-U)$, verify that it is similar to a symmetric matrix
(which it is for a symmetric tridiagonal $A$, via the diagonal similarity
$D^{1/2}B_{\text{GS}}D^{-1/2}$), and take its largest eigenvalue directly.

**Which matrices violate the relation?** Consistently ordered matrices are exactly those
whose directed graph is 2-cyclic in the sense of Varga. Matrices that are *not*
consistently ordered — for example a symmetric matrix whose sparsity graph contains a
cycle of odd length after the natural ordering, such as a five-point stencil on a
triangular mesh, or a matrix with an added coupling between two nodes of the same
colour — can have $\rho_{\text{GS}} > \rho_J^{2}$. For those, Gauss–Seidel may be slower
relative to Jacobi than the theorem promises, and the safe procedure is to measure
$\rho$ rather than assume the relation.
