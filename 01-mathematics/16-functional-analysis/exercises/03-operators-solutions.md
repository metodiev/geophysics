# Solutions — 01-16-03 Linear Operators, Adjoints and Compactness

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output; values marked "computed for these solutions"
> come from the computation described.

---

## ★1 — The operator norm

**(N1)** If $\lVert L\rVert = 0$ then $\lVert Lf\rVert = 0$ for every $f$ with
$\lVert f\rVert\le1$; by homogeneity, for *every* $f$, so $L = 0$. Conversely
$L = 0$ gives $\lVert L\rVert = 0$.

**(N2)** $\lVert\alpha L\rVert = \sup_{\lVert f\rVert\le1}\lVert\alpha
Lf\rVert = \lvert\alpha\rvert\sup\lVert Lf\rVert =
\lvert\alpha\rvert\lVert L\rVert$, because $\lvert\alpha\rvert\ge0$ pulls out of
a supremum.

**(N3)** $\lVert(L+M)f\rVert \le \lVert Lf\rVert + \lVert Mf\rVert \le
\lVert L\rVert + \lVert M\rVert$ for every $f$ in the unit ball; taking the
supremum gives the bound.

**Adjoint norm.** $\lVert L^*\rVert = \lVert L\rVert$. Indeed

$$\lVert L^*\rVert = \sup_{\lVert g\rVert\le1}\lVert L^*g\rVert
= \sup_{\lVert g\rVert\le1}\sup_{\lVert f\rVert\le1}\lvert\langle L^*g,f\rangle\rvert
= \sup_{\lVert f\rVert\le1}\sup_{\lVert g\rVert\le1}\lvert\langle g,Lf\rangle\rvert
= \sup_{\lVert f\rVert\le1}\lVert Lf\rVert ,$$

using $\langle L^*g,f\rangle = \overline{\langle f,L^*g\rangle} =
\overline{\langle Lf,g\rangle} = \langle g,Lf\rangle$ and the fact that for fixed
$Lf$ the supremum over $g$ of $\lvert\langle g,Lf\rangle\rvert$ is
$\lVert Lf\rVert$. So a bound on the forward operator is a bound on the adjoint:
they have the same amplification.

---

## ★2 — The adjoint kernel of a Fredholm operator

$$\langle Kf,g\rangle = \int_0^1\!\!\int_0^1 k(x,y)f(y)g(x)\,dy\,dx
= \int_0^1 f(y)\left[\int_0^1 k(x,y)g(x)\,dx\right]dy
= \langle f, K^*g\rangle ,$$

so

$$(K^*g)(y) = \int_0^1 k(x,y)g(x)\,dx .$$

**The adjoint kernel is $k^*(x,y) = k(y,x)$**: swap the arguments (which for a
matrix is the transpose). $K$ is self-adjoint exactly when $k(x,y) = k(y,x)$ for
almost all $(x,y)$.

- **Symmetric example:** the gravity kernel of a line mass,
  $k(x,y) = (z/\pi)/((x-y)^2 + z^2)$, depends only on $x - y$, hence is symmetric.
- **Non-symmetric example:** the advection Green's function or, in the discrete
  setting, a causal convolutional kernel $g_{i-j}$ with support only for
  $i \ge j$; $g_{i-j} \ne g_{j-i}$, so the operator is not self-adjoint, and its
  adjoint is the correlation of Section 3.4.

Averaging kernels of the form $(z/\pi)/((x-y)^2+z^2)$ arise whenever the physics
is translation-invariant and reciprocal, which is why so much of potential-field
inversion gets self-adjoint operators for free.

---

## ★3 — Compactness

**Definition.** $K: V\to W$ is compact if the image of the closed unit ball has
compact closure (equivalently, every bounded sequence has a subsequence whose
image converges).

**Singular-value criterion.** For $K$ between Hilbert spaces there is an expansion
$Kf = \sum_k\sigma_k\langle f,u_k\rangle v_k$ with orthonormal $\{u_k\}$,
$\{v_k\}$ and $\sigma_1\ge\sigma_2\ge\cdots\ge0$; $K$ is compact **if and only
if** $\sigma_k\to0$. (If $K$ has finite rank then all but finitely many
$\sigma_k$ vanish, which is the degenerate case.)

**Why the identity is not compact.** For $P = I$ on an infinite-dimensional $H$,
$\sigma_k = 1$ for every $k$, so $\sigma_k$ has no limit in $0$. In the
demonstration's terms, the image of the unit ball is the unit ball, which is not
relatively compact in infinite dimensions: an orthonormal sequence has no
convergent subsequence, since $\lVert e_m - e_n\rVert = \sqrt2$ for $m \ne n$. On
a finite-dimensional space the unit ball *is* compact, so every operator,
including the identity matrix, is compact — the table of Section 4.2 is showing
that the number of unit singular values grows with $n$, i.e. that the
finite-dimensional operator becomes *less* able to approximate a compact operator
as the dimension grows.

---

## ★4 — The adjoint of $L = -d^2/dx^2$ with Robin conditions

Let $u$ satisfy $u'(0) = hu(0)$ and $u(1) = 0$; let $v$ satisfy conditions to be
determined. Integrate by parts:

$$\langle Lu,v\rangle = -\int_0^1u''v\,dx
= -\big[u'v - uv'\big]_0^1 - \int_0^1 uv''\,dx .$$

The boundary term is

$$-\big[u'(1)v(1) - u(1)v'(1) - u'(0)v(0) + u(0)v'(0)\big]
= -\big[-v'(1)\big] - \big[-u'(0)v(0) + u(0)v'(0)\big] ,$$

using $u(1) = 0$. Substituting $u'(0) = hu(0)$:

$$-\big[-v'(1)\big] - u(0)\big[-hv(0) + v'(0)\big] .$$

For this to vanish for all admissible $u$ (i.e. for all $u(0)$, since $u(1)=0$),
we need

$$v(1) = 0 \qquad\text{and}\qquad v'(0) = hv(0) .$$

Those are **the same conditions as on $u$**: the boundary term vanishes, and
$\langle Lu,v\rangle = \langle u,Lv\rangle$ with $Lv = -v''$ subject to the same
Robin condition. So **the operator is self-adjoint** for this pair, which is what
one expects of a Sturm–Liouville operator with a symmetric boundary form.

**If the condition is $u(0)=0$, $u'(1) = g$ instead:** the boundary term becomes
$-[-v'(1) + u'(1)v(1)] = v'(1) - g\,v(1)$, which must vanish for all $u$
satisfying $u'(1)=g$ — but $g$ is fixed, so this cannot hold for arbitrary $v$.
Taking $g=0$ (a homogeneous Neumann condition), vanishing requires
$v'(1) = 0$ and $v(0) = 0$: the conditions are the *same pair* again. The
general rule is that the boundary form must be symmetric between $u$ and $v$, and
a *non-homogeneous* datum at an end breaks self-adjointness of the homogeneous
operator, which is why inhomogeneous boundary data are handled as a source term
in the adjoint equation rather than as a condition on the adjoint field. This is
exactly the boundary-term bookkeeping that adjoint-state codes get wrong.

---

## ★5 — Projections: bounded, and sometimes compact

**Boundedness with norm 1.** For an orthogonal projection $P$ onto a closed
subspace $M$, write $f = Pf + (f - Pf)$ with the two terms orthogonal. Then
$\lVert f\rVert^2 = \lVert Pf\rVert^2 + \lVert f - Pf\rVert^2 \ge \lVert
Pf\rVert^2$, so $\lVert P\rVert\le1$; and $P$ fixes any nonzero element of $M$, so
$\lVert P\rVert\ge1$. Hence $\lVert P\rVert = 1$.

**Finite rank implies compact.** If $M$ is finite-dimensional, $P$ has finite
rank, and a finite-rank operator is compact: the image of the unit ball lies in a
bounded subset of a finite-dimensional space, hence has compact closure.

**Infinite-dimensional projection is not compact.** If $\dim M = \infty$, take an
orthonormal sequence $\{e_n\}\subset M$. It is bounded and $\lVert Pe_m -
Pe_n\rVert = \lVert e_m - e_n\rVert = \sqrt2$, so no subsequence converges: the
image of the unit ball is not relatively compact.

**Reconciling with the table.** The demonstration's $n\times n$ identity has $n$
singular values equal to 1 — but it is a finite-rank operator on $\mathbb{R}^n$
and *is* compact as such. What the table shows is the trend: as $n$ grows, the
number of unit singular values grows without bound, so the family of
finite-dimensional operators does not converge to a compact operator. The
practical reading is that refining a discretisation moves a projection-like
operator *away* from compactness, and this is why band-limited filters do not
smooth and their inverses stay bounded while smoothing operators do not.

---

## ★6 — Contraction factors

For $J = \lVert Km-d\rVert^2$, the steepest-descent update with step $\tau$ maps
the error $e = m - m_{\text{ls}}$ to $(I - 2\tau K^{\mathsf T}K)e$. In the
eigenbasis of $K^{\mathsf T}K$, mode $k$ is multiplied by $1 - 2\tau\lambda_k$;
the demonstration sets $\tau = 0.5/L$, giving the factor $1 - \lambda_k/L$
reported in its table.

From that table:

| $k$ | $\lambda_k/L$ | factor | steps to $10^{-3}$: $\log(10^{-3})/\log(\text{factor})$ |
|---|---|---|---|
| 8 | $9.509\times10^{-3}$ | 0.9904906 | 723 |
| 16 | $1.773\times10^{-8}$ | 0.99999998 | $3.9\times10^{8}$ |

Both agree with the reported values (723 and $3.9\times10^8$). The arithmetic is
worth doing once by hand: $\log(10^{-3}) = -6.9078$ and
$\log(0.9904906) = -0.0095547$, so the quotient is 723.0. For $k = 16$,
$\log(1 - 1.773\times10^{-8}) \approx -1.773\times10^{-8}$, so the quotient is
$6.9078/1.773\times10^{-8} = 3.9\times10^8$. A mode whose singular value is
$10^{-4}$ of the largest needs of order $10^8$ iterations — which is why
gradient methods are never used for this purpose and why the spectrum, not the
optimiser, decides what is recoverable.

---

## ★7 — The dot-product test

**Setup.** For a matrix $A$ and vectors $x$, $y$,

$$\langle Ax, y\rangle - \langle x, A^{\mathsf T}y\rangle
= y^{\mathsf T}\!Ax - (A^{\mathsf T}y)^{\mathsf T}x
= y^{\mathsf T}\!Ax - y^{\mathsf T}\!Ax = 0 .$$

For $A$ replaced by $A + \delta A$:

$$y^{\mathsf T}(A + \delta A)x - x^{\mathsf T}(A + \delta A)^{\mathsf T}y
= y^{\mathsf T}\delta A\,x = \langle \delta A\,x, y\rangle .$$

So the failure of the test is **exactly the inner product of the perturbation's
action with $y$** — a *linear* function of the error, not quadratic and not
masked by conditioning. Perturbing one entry $(p,q)$ by $\delta$ produces
discrepancy $\delta\,x_qy_p$, linear in $\delta$: a $10^{-6}$ perturbation gives a
$10^{-6}$-order discrepancy, which is far above the $10^{-15}$ round-off floor of
a correct implementation. That is why the test is decisive in practice.

**Why necessary but not sufficient.** The test verifies the *pairing* of the
forward and adjoint actions. It is blind to errors that affect both consistently:
a missing factor of $\tfrac12$ in both `forward` and `adjoint` passes; an
incorrect forward *physics* with a correctly matching adjoint passes; a
boundary-condition error that is applied identically in both passes may pass if
the interior pairing dominates. So: **a failing dot-product test guarantees a bug;
a passing one guarantees only that the adjoint matches the forward operator as
implemented.** The natural companion test is to compare the adjoint gradient with
a finite-difference gradient of the misfit — the test the demonstration runs to
$7.6\times10^{-10}$ — which checks the operator pair against the *misfit*, and so
also catches a misfit that is not the one the adjoint was derived for.

---

## ★8 — Rank-3 kernel with amplitudes $(1, 0.9, 0.8)$

**(a)** For $K(x,y) = h\sum_{k=1}^3a_k\varphi_k(x)\varphi_k(y)$ with orthonormal
$\varphi_k$, the operator is $K = h\sum_k a_k\langle\cdot,\varphi_k\rangle
\varphi_k$, so $K^{\mathsf T}K$ has the same eigenvectors with eigenvalues
$a_k^2$. Computed for these solutions:

$$\lambda(K^{\mathsf T}K) = \{1,\ 0.81,\ 0.64\}\ \text{plus 37 zeros},\qquad L = 1,
\qquad \tau = 0.5/L = 0.5 .$$

The contraction factor of the slowest retained mode is
$1 - 0.64/1 = 0.36$.

**(b)** Prediction: $\log(10^{-3})/\log(0.36) = -6.9078/-1.02165 = 6.76$, so
about 7 steps. Measured (computed for these solutions), the model error reaches
the null-space norm $0.26296363$ at iteration 7 and does not change afterwards:

| iteration | $J(m)$ | $\lVert m - m_{\text{true}}\rVert$ (weighted) |
|---|---|---|
| 0 | $3.598\times10^{0}$ | 0.40382232 |
| 1 | $1.139\times10^{-2}$ | 0.26371557 |
| 3 | $8.038\times10^{-5}$ | 0.26296960 |
| 7 | $2.006\times10^{-8}$ | 0.26296363 |
| 15 | $1.595\times10^{-15}$ | 0.26296363 |
| 30 | $7.785\times10^{-29}$ | 0.26296363 |

**(c)** Because the null-space component of the true model produces no data at
all: $K m_{\text{null}} = 0$ exactly, so $J$ depends only on the retained
component. The iteration drives the retained component to the truth (hence $J\to
0$ at machine precision and beyond), while the null component moves only through
the initial model. Here the iteration starts from $m_0 = 0$, so the null component
stays at zero and the final error is exactly the norm of the true model's
null-space content, $0.26296363$. **The misfit is a measure of data agreement and
carries no information about the null space**; the model error is bounded below by
the null-space norm for any algorithm whatsoever, which is the sharpest possible
statement of non-uniqueness.

---

## ★9 — Step-length sweep

**(a)** The iteration is $m_{j+1} = m_j - \tau\,\nabla J(m_j)$ with
$\nabla J = 2K^{\mathsf T}(Km-d)$. Writing $e_j = m_j -
m_{\text{ls}}$ and using $K^{\mathsf T}(Km_{\text{ls}} - d) = 0$,

$$e_{j+1} = \left(I - 2\tau K^{\mathsf T}K\right)e_j .$$

The iteration converges iff $\lvert 1 - 2\tau\lambda\rvert < 1$ for every
eigenvalue $\lambda$ of $K^{\mathsf T}K$, i.e. $0 < \tau < 1/\lambda_{\max} =
1/L$. So $\alpha = \tau L \in (0,1)$: the stability limit is $\alpha < 1$, and
$\alpha = 1$ has the largest mode oscillating with factor $-1$ (marginally
stable, no decay).

**(b)** Computed for these solutions at 500 steps, with $L = 0.058182$ and
$\tau_{\max} = 1/L = 17.1873$:

| $\tau/\tau_{\max}$ | $\tau$ | model error | misfit $J$ |
|---|---|---|---|
| 0.10 | 1.7187 | 0.178860 | $2.908\times10^{-4}$ |
| 0.25 | 4.2968 | 0.127824 | $1.216\times10^{-4}$ |
| 0.50 | 8.5937 | 0.083857 | $3.370\times10^{-5}$ |
| 0.75 | 12.8905 | 0.066261 | $9.869\times10^{-6}$ |
| 0.90 | 15.4686 | 0.061706 | $4.944\times10^{-6}$ |
| 1.00 | 17.1873 | 0.059923 | $1.441\times10^{-5}$ |
| 1.20 | 20.6248 | diverged | — |

**(c)** The fastest mode has $\lambda_1 = L$, so with $\tau = 0.5/L$ it already
converges in one step; raising $\tau$ towards $1/L$ speeds up the *slow* modes
without affecting the first, so the error keeps improving. The misfit is
minimised near $\alpha = 0.9$ and rises slightly at $\alpha = 1$, where the
dominant mode has factor exactly $-1$: it oscillates rather than decaying, which
raises $J$ while leaving the model error (dominated by slower modes that are still
improving) at its lowest. Beyond $\alpha = 1$ the dominant mode grows
geometrically and the iteration diverges, as the table shows. The pair of
observations — model error minimised at the stability limit while the misfit is
minimised slightly below it — is a good reminder that "the misfit stopped
decreasing" and "the model stopped improving" are different statements.

---

## ★10 — Documentation for a weighted-misfit inversion

**(a) The gradient.** With $W$ a symmetric positive definite data weight,

$$J(m) = \lVert W^{1/2}(Fm-d)\rVert^2
\quad\Longrightarrow\quad
\nabla J(m) = 2F^{\mathsf T}W(Fm-d).$$

Using $F^{\mathsf T}$ alone computes the gradient of the *unweighted* misfit; if
the weight is diagonal with entries $1/\sigma_i^2$, the error is a factor
$\sigma_i^2$ per datum, so a data set with a hundredfold spread in error level
gets a gradient wrong by four orders of magnitude in the affected components. The
documentation should state the formula and identity of $W$ explicitly, since
"implicit weighting" is the usual source of disagreement between two groups
inverting the same data.

**(b) Adjoint boundary conditions.** The adjoint field satisfies the *same*
homogeneous boundary conditions as the forward field when the forward problem's
boundary form is symmetric (Section ★4 and Section 3.3 of the lesson); the data
residual enters as a source term, and any *inhomogeneous* forward boundary datum
is moved to the right-hand side of the adjoint system. The documentation should
state which conditions are imposed where, because a mismatch there produces a
gradient that is nearly correct.

**(c) The dot-product test.** Provide an automated test that, for random $x$ and
$y$, computes $r = \langle Fx,y\rangle - \langle x,F^{\mathsf T}y\rangle$ and
fails if $\lvert r\rvert > \epsilon\,\lVert Fx\rVert\lVert y\rVert$ with, say,
$\epsilon = 10^{-10}$. Stating the threshold matters: the test is only meaningful
with a tolerance, and a relative criterion is the right form because the two
terms grow with the data magnitude.

**(d) The gradient is not the inverse.** $F^{\mathsf T}(d - Fm)$ is a
back-projection: it has the correct units and direction but weights modes by
$\sigma_k$ rather than by $1/\sigma_k$, so it over-weights the well-resolved modes
and under-weights (in relative terms) the poorly resolved ones. Reporting a model
therefore requires an additional step — a regularised solve, a preconditioner, or
a specified number of iterations — and the documentation should say which, and
report the misfit, the model norm and a resolution estimate alongside the model.
