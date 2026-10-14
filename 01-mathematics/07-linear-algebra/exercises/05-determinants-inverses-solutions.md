# Solutions — 01-07-05 Determinants, Inverses and Matrix Conditioning

> **Read this after attempting the exercises, not before.**
>
> Numeric answers were computed and verified. Condition numbers are quoted to six
> significant figures; they were obtained from the singular values, not from a
> determinant.

---

## ★1 — Determinant, adjugate, inverse

$$A = \begin{bmatrix} 3 & 1 \\ 2 & 4\end{bmatrix}, \qquad
\det A = 12 - 2 = 10 .$$

Cofactors: $C_{11} = 4$, $C_{12} = -2$, $C_{21} = -1$, $C_{22} = 3$. The **adjugate**
is the transpose of the cofactor matrix:

$$\operatorname{adj}A = \begin{bmatrix} 4 & -1 \\ -2 & 3\end{bmatrix}, \qquad
A^{-1} = \frac{\operatorname{adj}A}{\det A} = \frac{1}{10}
\begin{bmatrix} 4 & -1 \\ -2 & 3\end{bmatrix}
= \begin{bmatrix} 0.4 & -0.1 \\ -0.2 & 0.3\end{bmatrix}.$$

Check:

$$AA^{-1} = \frac{1}{10}\begin{bmatrix} 3 & 1 \\ 2 & 4\end{bmatrix}
\begin{bmatrix} 4 & -1 \\ -2 & 3\end{bmatrix}
= \frac{1}{10}\begin{bmatrix} 12-2 & -3+3 \\ 8-8 & -2+12\end{bmatrix}
= \begin{bmatrix} 1 & 0 \\ 0 & 1\end{bmatrix}. ✓$$

**Geometry:** $\det A = 10$ means the map scales areas by 10 and preserves orientation
(the sign is positive).

---

## ★2 — Determinant two ways

$$B = \begin{bmatrix} 1 & 2 & 0 \\ 0 & 3 & 1 \\ 2 & 1 & 1\end{bmatrix}.$$

(a) **Cofactor expansion along the first row:**

$$\det B = 1\begin{vmatrix} 3 & 1 \\ 1 & 1\end{vmatrix}
- 2\begin{vmatrix} 0 & 1 \\ 2 & 1\end{vmatrix}
+ 0\begin{vmatrix} 0 & 3 \\ 2 & 1\end{vmatrix}
= 1(3 - 1) - 2(0 - 2) + 0 = 2 + 4 = 6 .$$

(b) **Elimination.** Row 3 already has a zero in column 1, and row 1's leading entry is
1, which is the largest in the column ($|1| > |0|$), so **no swap is needed**:

$$B \to \begin{bmatrix} 1 & 2 & 0 \\ 0 & 3 & 1 \\ 0 & -3 & 1\end{bmatrix}
\to \begin{bmatrix} 1 & 2 & 0 \\ 0 & 3 & 1 \\ 0 & 0 & 2\end{bmatrix},$$

with multipliers $\ell_{31} = 2$, $\ell_{32} = -1$ (add row 2 to row 3). Pivots
$1$, $3$, $2$; product $= 6$; **zero swaps**, so $\det B = +6$. Both routes agree.

---

## ★★3 — A two-station experiment, in two sets of units

(a) Singular values of $G = \begin{bmatrix} 1 & 1 \\ 1 & 1.05\end{bmatrix}$:

$$\sigma = (2.0253125,\ 0.0246875), \qquad \kappa_2 = 82.037810, \qquad
\det G = 1(1.05) - 1(1) = 0.05 .$$

(b) Worst case, the relative model error is bounded by
$\kappa_2 \times 10^{-3} = 8.20\times10^{-2}$, that is **8.2 %**. In the worst
direction — the difference $m_1 - m_2$ — the amplification is real, not merely
permitted: $\|G^{-1}\|_2 = 1/\sigma_{\min} = 40.51$, so a $0.5$ ms error gives a model
error of up to $0.5\times10^{-3} \times 40.51 = 2.0\times10^{-2}$ $\mathrm{s/km}$.

(c) $G' = 1000\,G$, so every singular value is multiplied by 1000 and

$$\sigma(G') = (2025.312451,\ 24.687549), \qquad \kappa_2(G') = 82.037810, \qquad
\det G' = 50\,000 .$$

**$\det$ changed by a factor of $10^{6}$ — exactly $10^{3}$ per column — while
$\kappa_2$ is unchanged**, because multiplying the whole matrix by a scalar multiplies
every singular value by the same factor. This is the cleanest demonstration that a
determinant is a statement about units as much as about geometry, and that $\kappa_2$ is
the scale-invariant measure.

(d) For $G'' = \begin{bmatrix} 1 & 1 \\ 1 & 1.5\end{bmatrix}$:

$$\sigma = (2.280776,\ 0.219224), \qquad \kappa_2 = 10.403882 .$$

**Reduction factor: $82.037810/10.403882 = 7.887$.** Moving the second station so that
it samples the second layer $50$ % more strongly, instead of $5$ %, improves the
conditioning by nearly a factor of eight — a survey-design decision worth more than any
improvement in solver.

---

## ★★4 — Why the normal equations die

(a) **The argument.** For full-column-rank $G$, $G^\mathsf{T}G$ has singular values
$\sigma_i^{2}$, so

$$\kappa_2(G^\mathsf{T}G) = \frac{\sigma_{\max}^{2}}{\sigma_{\min}^{2}}
= \kappa_2(G)^{2} .$$

Solving a system with condition number $\kappa$ costs $\log_{10}\kappa$ digits, so the
normal-equation route costs twice as many digits as solving with $G$ itself. Double
precision holds about $16$ digits, so the normal equations have nothing left once
$\kappa_2(G^\mathsf{T}G) = \kappa_2(G)^{2} \ge 1/\epsilon_{\text{mach}}$, i.e. once
$\kappa_2(G) \ge 1/\sqrt{\epsilon_{\text{mach}}} = 6.7\times10^{7}$.

(b) For $G(\delta) = \begin{bmatrix} 1 & 1 \\ 1 & 1+\delta\end{bmatrix}$,
$\kappa_2 \approx 4/\delta$, so the threshold is

$$\delta \approx \frac{4}{6.7\times10^{7}} = 6.0\times10^{-8} .$$

(c) Numerically, with $\kappa_2(G) = 4/\delta$:

| $\delta$ | $\kappa_2(G)$ | $\kappa_2(G^\mathsf{T}G) = \kappa_2(G)^{2}$ | exceeds $1/\epsilon = 4.5\times10^{15}$? |
|---|---|---|---|
| $10^{-7}$ | $4.0\times10^{7}$ | $1.6\times10^{15}$ | no |
| $10^{-8}$ | $4.0\times10^{8}$ | $1.6\times10^{17}$ | **yes** |

The threshold lies between the two, at $\delta \approx 6\times10^{-8}$, as predicted.

(d) **What happens is not gradual degradation but failure of the algorithm.** At
$\delta = 10^{-8}$ the floating-point $G^\mathsf{T}G$ has a zero pivot in Gaussian
elimination — the computed matrix is numerically singular — and the solve either aborts
or returns a meaningless vector. QR applied to the same $G$ returns both parameters to
about eight significant figures. The matrix has not changed, and its conditioning is
tolerable ($\kappa = 4\times10^{8}$ leaves eight digits); it is the *reformulation* that
has been destroyed.

---

## ★★★5 — Equilibration

(a) For $A = \begin{bmatrix} 10^{3} & 1 \\ 1 & 1.001\times10^{-3}\end{bmatrix}$:

$$\det A = 10^{3}\times1.001\times10^{-3} - 1 = 1.001 - 1 = 1.0\times10^{-3},$$
$$\sigma = (1.000001\times10^{3},\ 1.000044\times10^{-6}), \qquad
\kappa_2 = 9.999568\times10^{8} .$$

(b) Row scaling by the reciprocal of each row's largest absolute entry
($1000$ and $1$) gives $\begin{bmatrix} 1 & 10^{-3} \\ 1 & 1.001\times10^{-3}
\end{bmatrix}$; column scaling similarly (column maxima $1$ and $1.001\times10^{-3}$)
gives

$$\bar A = \begin{bmatrix} 1 & 0.999000999 \\ 1 & 1\end{bmatrix}, \qquad
\sigma = (1.999501,\ 4.996253\times10^{-4}), \qquad \kappa_2 = 4.002001\times10^{3} .$$

(c) **Reduction factor: $9.999568\times10^{8}/4.002001\times10^{3} = 2.499\times10^{5}$**,
i.e. $\kappa_2$ falls by a factor of about $250\,000$, from $10^{9}$ to $4\times10^{3}$.

(d) **No.** If $Ax = b$ is consistent and $D_1$, $D_2$ are invertible diagonal matrices,
then $\bar A\bar x = \bar b$ with $\bar A = D_1AD_2$, $\bar x = D_2^{-1}x$,
$\bar b = D_1b$ has exactly the same set of solutions, transformed by the known scaling:
any solution $x$ of the original gives $\bar x = D_2^{-1}x$ for the scaled system, and
conversely. Equilibration is a change of units on the rows (measurements) and columns
(parameters); it cannot change the mathematics.

(e) **What it changes is the accuracy of the computation and the meaning of the
Euclidean norm.** Floating-point elimination on a matrix whose entries span many orders
of magnitude loses accuracy through the growth of the intermediate quantities; scaling
the rows and columns first makes the entries comparable and the growth moderate, which
is why every serious linear-algebra library offers equilibration. For an inverse
problem there is a second, more important effect: the Euclidean norm of the model
vector — and therefore the meaning of a *minimum-norm* constraint — depends on the units
in which the parameters are expressed, as
[01-07-01](../01-vectors-and-spaces.md) Section 3.3 shows. Equilibration makes the
conditioning better and simultaneously changes what "small model" means; both facts have
to be stated when a regularised inversion is reported.

---

## ★★★6 — Relative error versus conditioning, measured

(a) **Protocol.** Build $d = Gm_{\text{true}}$ exactly, then multiply the **second
datum** by $(1 + \eta)$ with $\eta = 10^{-8}$ — a relative perturbation well above
round-off so that its effect is unambiguous, and well below any realistic picking error
so that the experiment isolates the conditioning rather than the noise level. Solve the
$2\times2$ system in double precision by elimination with partial pivoting, and report
the relative error of the larger model component.

The scaling of the test is chosen so that the amplified result is measurable: any
perturbation applied to *both* data equally would scale the model and produce no error
at all, since the system is linear.

(b) Table:

| $\delta$ | $\kappa_2(G)$ approx. | $\kappa_2\epsilon_{\text{mach}}$ | observed relative model error |
|---|---|---|---|
| $10^{-2}$ | $4.0\times10^{2}$ | $8.9\times10^{-14}$ | $1.4900\times10^{-6}$ |
| $10^{-4}$ | $4.0\times10^{4}$ | $8.9\times10^{-12}$ | $1.4999\times10^{-4}$ |
| $10^{-6}$ | $4.0\times10^{6}$ | $8.9\times10^{-10}$ | $1.5000\times10^{-2}$ |
| $10^{-8}$ | $4.0\times10^{8}$ | $8.9\times10^{-8}$ | $1.5000\times10^{0}$ |
| $10^{-10}$ | $4.0\times10^{10}$ | $8.9\times10^{-6}$ | $1.5000\times10^{2}$ |
| $10^{-12}$ | $4.0\times10^{12}$ | $8.9\times10^{-4}$ | $1.4999\times10^{4}$ |
| $10^{-14}$ | $4.0\times10^{14}$ | $8.9\times10^{-2}$ | $1.5012\times10^{6}$ |

(c) **All digits are lost at $\delta \approx 1.5\times10^{-8}$**, where the relative
model error reaches $1.5$ — larger than the model itself. The observed error follows

$$\text{relative model error} \approx 1.5\times10^{-8}/\delta
= \kappa_2(G)\times(\text{relative size of the data error in the worst direction}) ,$$

since $\eta = 10^{-8}$ is much larger than round-off: the error is governed by $\eta$
amplified by $\kappa$, not by $\epsilon_{\text{mach}}$ amplified by $\kappa$. The last
column of the table shows the round-off *floor*, eight orders of magnitude below the
observed error throughout: **the experiment is limited by the data perturbation, and the
conditioning converts it into a model error.** Both scales matter and they must not be
confused.

(d) **The second, more brutal failure** occurs at $\delta = 10^{-16}$: then
$1 + \delta$ rounds to exactly $1$ in double precision, the two rows of $G$ become
identical bit patterns, the matrix is **exactly singular** in floating point, and the
solve divides by a zero pivot. The mechanism is representation, not conditioning: the
information that distinguished the two rays was never stored. The interesting warning is
that the failure is not announced by a large condition number computed from $G$ — it is
a property of the *matrix as stored*. Reporting $\kappa = 4\times10^{15}$ would be
misleading: the stored matrix has $\kappa = \infty$.

(e) **Limits of the conclusion.** The result depends on *which* datum is perturbed and
on $\eta$, through the factor $\eta\cos\psi$ where $\psi$ is the angle between the
perturbation vector and the worst data direction. Perturbing the second datum by a
relative $\eta$ gives a perturbation vector $\approx \eta d_2 e_2$; had the perturbation
been applied to both data equally, the model error would be zero. The dependence on
$m_{\text{true}}$ is different in kind: the *relative* error
$\|\delta m\|/\|m\|$ depends on the angle between $m_{\text{true}}$ and the worst model
direction, so the numbers in (b) would change if the true model were aligned with
$(1,-1)$ — they would be larger — or with $(1,1)$ — smaller. What does **not** depend on
any of these choices is the mechanism: the error factorises into a property of the
geometry ($\kappa$, or more precisely $1/\sigma_{\min}$) and a property of the data
perturbation.
