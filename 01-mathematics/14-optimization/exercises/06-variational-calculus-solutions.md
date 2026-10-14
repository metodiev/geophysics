# Solutions — 01-14-06 Calculus of Variations and Its Geophysical Uses

> **Read this after attempting the exercises, not before.** Every value below was
> computed: the direct-method solves used the Thomas algorithm, the functional
> values used the trapezoid rule of the scheme itself, and the numerical first
> variations used the composite trapezoid rule with $2\times10^{4}$ intervals.
> Values attributed to the demonstration are its output.

---

## ★1 — A forced quadratic functional

**(a)** $L = y'^{2} + 2xy$, so
$\dfrac{\partial L}{\partial y} = 2x$ and
$\dfrac{\partial L}{\partial y'} = 2y'$.

**(b)** The Euler–Lagrange equation is
$2x - \dfrac{d}{dx}(2y') = 0$, i.e.

$$2x - 2y'' = 0 \quad\Longrightarrow\quad y'' = x .$$

**(c)** Integrating twice, $y = x^{3}/6 + Cx + D$. The boundary conditions give
$D = 0$ and $1/6 + C = 0$, so

$$y = \frac{x^{3} - x}{6} .$$

**(d)** $y(1/2) = (0.125 - 0.5)/6 = \boxed{-0.0625}$. It is a **minimum**: the
functional is $\int(y'^{2} + 2xy)dx$, whose second variation is
$2\int(\delta y')^{2}dx > 0$ for every nonzero admissible variation, so the
quadratic form is positive definite and the stationary point is the unique
minimiser. The sign of the solution is not evidence of anything — the minimum has
a negative value because the linear forcing term $2xy$ is negative on most of the
interval.

---

## ★2 — A free end

**(a)** $L = y'^{2}$ gives $\partial L/\partial y = 0$ and
$\partial L/\partial y' = 2y'$, so the equation is $y'' = 0$. At the free end
$x = 1$ the boundary term $\left[\partial L/\partial y'\cdot\delta y\right]$ must
vanish for arbitrary $\delta y(1)$, giving the natural condition

$$2y'(1) = 0 \quad\Longrightarrow\quad y'(1) = 0 .$$

**(b)** From $y'' = 0$, $y = Cx + D$; $y(0) = 0$ gives $D = 0$ and $y'(1) = C = 0$,
so $y\equiv0$ and $y(1) = \boxed{0}$.

**(c)** Requiring $\delta y(1) = 0$ as well as the natural condition would be
redundant *for this functional*, because the natural condition already forces the
same constant to zero; but in general imposing both is over-specification, and if
the two disagree the problem has no solution. The correct procedure is to decide
for each end whether the value is imposed (then $\delta y = 0$ there) or free
(then the natural condition applies) — never both.

**(d)** A natural boundary condition is the physics that the functional already
knows: it is the statement "no force/moment/flux is transmitted through this
surface", and it appears automatically when the energy is minimised rather than
imposed by hand.

---

## ★3 — The direct-method system

**(a)** With $h = 1/n$ and a forward difference for $y'$,

$$F_h(y) = \sum_{i=0}^{n-1}\left[\frac{(y_{i+1} - y_i)^{2}}{h}
+ \frac{h}{2}\left(k^{2}y_i^{2} + k^{2}y_{i+1}^{2}\right)\right].$$

**(b)** Differentiating with respect to an interior node $y_j$: the difference
terms contribute $-\tfrac{2}{h}(y_j - y_{j-1})$ and $+\tfrac{2}{h}(y_{j+1} - y_j)$,
and the trapezoid terms contribute $hk^{2}y_j$ (the node appears in exactly two
panels, each with weight $\tfrac{h}{2}$). Setting the sum to zero:

$$-\frac{2}{h}\left(2y_j - y_{j-1} - y_{j+1}\right) + hk^{2}y_j = 0
\quad\Longrightarrow\quad
\left(2 + h^{2}k^{2}\right)y_j - y_{j-1} - y_{j+1} = 0. \qquad\square$$

**(c)** With $\mu = h^{2}k^{2}$ acting as the eigenvalue parameter and the
boundary values zero, the same matrix is the generalised eigenproblem

$$Ky = \lambda y, \qquad K = \operatorname{tridiag}(-1,\ 2,\ -1), \qquad
\lambda = -h^{2}k^{2},$$

or, equivalently, $y'' = -k^{2}y$ discretised directly. The connection matters
because it makes the direct method a *matrix* problem: a positive-definite
tridiagonal solve in the boundary-value case, an eigenproblem in the
oscillation case.

**(d)** The scheme is **second order** in $h$. The order is inherited from the two
discretisation choices: the forward difference is first order locally but the
*functional* built from it has an $O(h)$ term that cancels when the products are
summed (the leading error of a centred difference is recovered), and the trapezoid
rule for $y^{2}$ is second order. The general principle is that the order of the
discrete minimiser is set by the *worst consistent discretisation* in the
functional.

---

## ★4 — The Rayleigh quotient and the discrete eigenvalue

**(a)** For $-(p\phi_k')' = \lambda_k\phi_k$ with $\phi_k(a) = \phi_k(b) = 0$, the
eigenfunctions are complete and orthogonal in the weighted inner product with
weight $1$, so $y = \sum_kc_k\phi_k$. Then

$$\int_a^bp\,y'^{2}dx = \sum_k\lambda_kc_k^{2}\int_a^b\phi_k^{2}dx, \qquad
\int_a^by^{2}dx = \sum_kc_k^{2}\int_a^b\phi_k^{2}dx,$$

using the identity $\int py'\phi_k' = \lambda_k\int y\phi_k$ (integration by parts
with the eigenrelation).

**(b)** Dividing, and writing $w_k = c_k^{2}\int\phi_k^{2}$,

$$R[y] = \frac{\sum_k\lambda_kw_k}{\sum_kw_k} \ge
\frac{\lambda_1\sum_kw_k}{\sum_kw_k} = \lambda_1,$$

a weighted average of the eigenvalues and therefore at least the smallest. Equality
requires $w_k = 0$ for every $k\ge2$, i.e. $y\propto\phi_1$. $\square$

**(c)** A subspace argument says that the minimum of $R$ over a subspace of the
admissible functions is an **upper** bound for $\lambda_1$: restricting the trial
set cannot lower the minimum. Yet the discrete eigenvalues computed here
($9.7887$, $9.8493$, $9.8645$, $9.8683$ at $n = 10,20,40,80$) all lie **below**
$\pi^{2}$, and they *rise* toward it as the mesh is refined. The resolution is that
the discrete quotient is not the same functional: the mass term is evaluated with a
lumped (trapezoid) quadrature rather than by exact integration, and lumping makes
the denominator smaller than the true $\int y^{2}$, which lowers the ratio. The
bound of (b) applies to the *continuous* $R$; this discretisation is
non-conforming through its quadrature, so neither bound is guaranteed and the
measured answer is below. In the lesson's §4.5 the same table is reported, and the
sentence there that "refining the mesh can only lower the discrete eigenvalue
toward the truth" should read that refining *raises* it toward the truth from
below — the numbers in its own table are unambiguous.

**(d)** The bound is useful because it turns every trial function into a
*guaranteed* statement about $\lambda_1$: compute $R$ for any admissible $y$ and you
have an upper bound on the smallest eigenvalue, with no solving required. Physical
applications use this deliberately — a Rayleigh quotient evaluated with a plausible
mode shape brackets the true eigenfrequency, and a sequence of trial functions
converges monotonically from above. It is also the reason the discrete answer must
be compared with care: monotone convergence from *above* holds for a conforming
discretisation, not for a lumped one.

---

## ★★5 — Verifying a variational derivative

**(a)** With $L = y'^{2} + y^{2}$,
$\partial L/\partial y = 2y$ and
$\dfrac{d}{dx}\dfrac{\partial L}{\partial y'} = 2y''$, so

$$g(x) = 2y - 2y'' .$$

For $y = x$ (so $y'' = 0$) and $\delta y = \sin\pi x$:

$$\int_0^1 g\,\delta y\,dx = 2\int_0^1x\sin\pi x\,dx
= 2\left[-\frac{x\cos\pi x}{\pi} + \frac{\sin\pi x}{\pi^{2}}\right]_0^1
= 2\left(\frac1\pi\right) = \frac{2}{\pi} = 0.6366197724 .$$

**(b)** Evaluating the functional by composite trapezoid quadrature at
$y + \epsilon\delta y$ and $y - \epsilon\delta y$ and forming the central
difference:

| $\epsilon$ | $\left(F[y+\epsilon\delta y] - F[y-\epsilon\delta y]\right)/(2\epsilon)$ | analytic $2/\pi$ | difference |
|---|---|---|---|
| $10^{-3}$ | 0.6366197710 | 0.6366197724 | $1.3\times10^{-9}$ |
| $10^{-5}$ | 0.6366197708 | 0.6366197724 | $1.5\times10^{-9}$ |

**(c)** The two routes agree to about $10^{-9}$, and the agreement does **not**
improve when $\epsilon$ is reduced from $10^{-3}$ to $10^{-5}$: what limits it is
the quadrature used to evaluate $F$, not the finite difference in $\epsilon$. The
central difference has truncation error $O(\epsilon^{2})$ — at $\epsilon = 10^{-3}$
that is $10^{-6}$ relative to the second derivative scale, comfortably below the
observed $10^{-9}$ — while the trapezoid rule on a smooth integrand converges as
$h_q^{2}$ with $h_q = 5\times10^{-5}$, i.e. $\sim10^{-9}$. The measured floor *is*
the quadrature floor, which is the correct diagnosis.

**(d)** The check verifies the whole chain: that the variational derivative of this
functional is $g = 2y - 2y''$, and that setting $g = 0$ for all admissible $\delta y$
is the Euler–Lagrange equation. It does **not** verify that a given $y$ minimises
$F$ — a stationary point can be a maximum or a saddle — and it does not verify the
boundary terms, which were assumed to vanish because $\delta y(0) = \delta y(1) = 0$
was imposed. Testing a free end requires a perturbation that is nonzero there.

---

## ★★6 — A free end, with the discrete evidence

**(a)** $L = y'^{2} - 2y$ gives $\partial L/\partial y = -2$ and
$\partial L/\partial y' = 2y'$, so the equation is

$$-2 - 2y'' = 0 \quad\Longrightarrow\quad y'' = -1,$$

and the boundary term at the free end $x=1$ forces
$\partial L/\partial y' = 2y'(1) = 0$, the natural (Neumann) condition.

**(b)** Integrating, $y = -x^{2}/2 + Cx + D$; $y(0) = 0$ gives $D = 0$ and
$y'(1) = -1 + C = 0$ gives $C = 1$, so

$$y = x - \frac{x^{2}}{2}, \qquad y(1) = \boxed{0.5} .$$

**(c)** The discrete minimiser satisfies
$2y_j - y_{j-1} - y_{j+1} = h^{2}$, i.e. the second difference equals $h^{2}$,
which is the discretisation of $-y'' = 1$ — the Euler–Lagrange equation. At the
last node the *same* equation holds with $y_{j+1}$ absent (there is no node beyond
$x = 1$), and it reads

$$y_n - y_{n-1} = \frac{h^{2}}{2}, \qquad\text{so}\qquad
\frac{y_n - y_{n-1}}{h} = \frac h2 \to 0 .$$

A one-sided difference with $O(h)$ truncation approximates $y'(1) = 0$; the
discrete solution satisfies it automatically, because it arose from the boundary
term of the variation and was never imposed. At $n = 10$, $h^{2}/2 = 0.005$, which
is the value the demonstration prints.

**(d)** The exact solution is a quadratic and the scheme is *exact* for quadratics,
so the truncation error vanishes identically and the error is at round-off
($10^{-15}$-level) for every $n$. No convergence rate can be extracted from such a
problem — the measured order would be meaningless ("order zero" if the errors do
not fall) — which is why the convergence study of §4.1 uses
$y = \sinh x/\sinh 1$, a solution outside the scheme's exact class. The lesson
states this explicitly as one of the module's most transferable cautions: a test
problem must not be one that the scheme solves exactly.

---

## ★★7 — Conditioning of the direct-method matrix

**(a)** and **(b)** With $m = n-1$ unknowns:

| $n$ | $m$ | $\kappa(K)$ | $4(m+1)^{2}/\pi^{2}$ | ratio |
|---|---|---|---|---|
| 10 | 9 | 39.8635 | 40.5285 | 0.9836 |
| 20 | 19 | 161.4476 | 162.1139 | 0.9959 |
| 40 | 39 | 647.7890 | 648.4556 | 0.9990 |
| 80 | 79 | 2593.1557 | 2593.8223 | 0.9997 |
| 160 | 159 | 10374.6225 | 10375.2892 | 0.9999 |

The measured $\kappa$ tracks the asymptotic form to better than 0.1 per cent at
$n = 40$ and improves as $n$ grows, exactly as the next term in the expansion
predicts.

**(c)** At $n = 160$ the solve loses $\log_{10}\kappa = 4.016$ digits, i.e. about
**four digits** of the available sixteen. In binary64 that leaves twelve digits,
which is harmless. In single precision (seven digits) the same solve loses more
than half its precision, which is why single-precision finite-element codes are
confined to coarse meshes.

**(d)** Truncation falls as $h^{2} = 1/n^{2}$ while conditioning grows as
$n^{2} = h^{-2}$, so the two trade at exactly the same rate and the *product* is
scale-free. The practical rule is therefore not to balance them but to choose the
mesh from the data's resolution: refine only while the mesh is coarse relative to
the shortest wavelength the data constrain, and stop — additional nodes that carry
no information buy only conditioning loss. The lesson's §5 states the same
conclusion from the physics side ("fix the mesh by the resolution of the data and
then stop").

---

## ★★8 — Solving the direct-method system

**(a)** With $a = 2 + h^{2}$ on the diagonal, $-1$ off-diagonal, right-hand side
$0$ everywhere except $1$ at the last equation (from $y_n = 1$), and $m = n-1$
unknowns, the Thomas algorithm solves the system in $O(n)$ operations.

**(b)** At $n = 10$:

| $x$ | computed $y$ | exact $\sinh x/\sinh 1$ | difference |
|---|---|---|---|
| 0.1 | 0.085245 | 0.085234 | $1.1\times10^{-5}$ |
| 0.2 | 0.171342 | 0.171320 | $2.2\times10^{-5}$ |
| 0.3 | 0.259152 | 0.259122 | $3.0\times10^{-5}$ |
| 0.4 | 0.349554 | 0.349517 | $3.7\times10^{-5}$ |
| 0.5 | 0.443452 | 0.443409 | $4.3\times10^{-5}$ |
| 0.6 | 0.541784 | 0.541740 | $4.4\times10^{-5}$ |
| 0.7 | 0.645534 | 0.645493 | $4.1\times10^{-5}$ |
| 0.8 | 0.755740 | 0.755705 | $3.5\times10^{-5}$ |
| 0.9 | 0.873502 | 0.873482 | $2.0\times10^{-5}$ |

The discrete solution lies *above* the exact one everywhere and the maximum error
occurs near $x = 0.6$; that is the signature of an $O(h^{2})$ error in a
smooth convex solution, not of a systematic bias.

**(c)** Maximum errors: $4.414591\times10^{-5}$ at $n = 10$ and
$1.104689\times10^{-5}$ at $n = 20$, whose ratio is $3.9962$ — an order of
$1.9986$, i.e. **second order**. Continuing the refinement gives ratios $3.9991$
($n=40$), $3.9982$ ($n=80$), $3.9999$ ($n=160$) and $3.9999$ ($n=320$), with the
error at $n = 320$ equal to $4.318\times10^{-8}$.

**(d)** At $n = 40$ the discrete functional at the discrete minimiser is

$$F_h(y_h) = 1.313156718939,$$

and at the *sampled* exact solution it is $1.313156718985$ — higher by
$4.6\times10^{-11}$, i.e. equal to round-off. Every perturbation of an interior
node raises $F_h$: a bump of $+10^{-3}$ raises it by $8.0025\times10^{-5}$, a bump
of $+10^{-2}$ by $8.0025\times10^{-3}$, and a dip of $-10^{-3}$ by exactly the same
amount as the corresponding bump — the signature of a quadratic form, whose
curvature is the same in both directions.

The discrete value is **not a lower bound** for the continuous functional. The
exact value is $F[y] = \coth 1 = 1.3130352855$, and the discrete minimiser's
$1.3131567$ is *above* it by $1.2\times10^{-4}$. The reason is that $F_h$ is not
$F$: it uses the trapezoid rule for the mass term and a difference quotient for
the derivative, so its minimum is the minimum of a *different* functional, and the
difference between the two functionals is $O(h^{2})$ in general. A Rayleigh quotient
does give a one-sided bound (§★4), but a quadrature-based functional does not.

---

## ★★★9 — The Rayleigh quotient as an eigenproblem

**(a)** $K$ is the Dirichlet Laplacian of order $n-1$ with spacing $h = 1/n$. Its
eigenvectors are $\sin(ik\pi h)$ for $k = 1,\dots,n-1$, and using
$\sin\theta(i-1) + \sin\theta(i+1) = 2\sin\theta i\cos\theta$ with
$\theta = k\pi h$,

$$K\mathbf v = (2 - 2\cos k\pi h)\mathbf v
\quad\Longrightarrow\quad
\lambda_k = \frac{4}{h^{2}}\sin^{2}\frac{k\pi h}{2}. \qquad\square$$

**(b)** The smallest eigenvalue:

| $n$ | $\lambda_{\min}$ | error against $\pi^{2}$ | ratio |
|---|---|---|---|
| 10 | 9.7886967410 | $8.091\times10^{-2}$ | — |
| 20 | 9.8493275239 | $2.028\times10^{-2}$ | 3.990 |
| 40 | 9.8645320540 | $5.072\times10^{-3}$ | 3.998 |
| 80 | 9.8683361187 | $1.268\times10^{-3}$ | 4.000 |

**(c)** The measured order is $\log_2 3.99 = 1.996$ at the first refinement and
$2.000$ thereafter: **second order**, matching
$\lambda_{\min} = \pi^{2}\left(1 + \pi^{2}/(12n^{2}) + O(n^{-4})\right)$. The
prediction at $n = 10$ is $\pi^{2}\pi^{2}/(12\times100) = 0.0811$ against the
measured $0.0809$ — agreement to 0.2 per cent even at the coarsest mesh, which is
better than the asymptotics has any right to claim and is the usual behaviour of
this particular expansion.

**(d)** Inverse iteration is right because the wanted eigenvalue is the
**smallest**: power iteration on $K/h^{2}$ converges to the *largest* eigenvalue
(fastest oscillation), which is the one a seismic or flexural problem cares about
least. Solving $Ky = x$ repeatedly converges to the smallest eigenvalue at the rate
$(\lambda_1/\lambda_2)^{k}$, and each solve is $O(n)$ by the Thomas algorithm, so
the cost per iteration is the same as a matvec. At $n = 80$ the computed
$9.8683361187$ agrees with $\pi^{2}$ to four decimal places, i.e. four digits, and
the *remaining* error is purely the $O(h^{2})$ discretisation — refining the mesh,
not the iteration, is what buys the other digits. That distinction is the practical
answer: report the discrete eigenvalue with its discretisation error, and do not
claim the exact continuum value.

---

## ★★★10 — The price of refinement

**(a)** Two independent contributions to the error of a finite-difference solve:

* **Truncation**: $C_{t}h^{2}$ for the second-order scheme here (in general
  $C_th^{p}$, and for a first-order scheme $C_th$).
* **Round-off**: each of the $O(1/h)$ arithmetic operations contributes a relative
  $u$, and the solution is an $O(1)$ quantity amplified by the conditioning
  $O(h^{-2})$, so the accumulated error is $C_{r}u h^{-2}$ — matching the
  $\kappa\sim h^{-2}$ of ★★7, since the amplification is the condition number.

**(b)** Minimising $E(h) = C_{t}h^{2} + C_{r}uh^{-2}$:

$$E'(h) = 2C_{t}h - 2C_{r}uh^{-3} = 0
\quad\Longrightarrow\quad
h^{4} = \frac{C_{r}u}{C_{t}}
\quad\Longrightarrow\quad
h_{\text{opt}} = \left(\frac{C_{r}u}{C_{t}}\right)^{1/4} \propto u^{1/4}.$$

The optimal step scales as the **fourth root** of the unit round-off — not the
square root — because the two competing errors have orders 2 and $-2$ rather than 1
and $-1$. This is the same structure as the numerical-differentiation trade-off of
the module on numerical methods, where the exponents $u^{1/2}$ and $u^{1/3}$ appear
for forward and centred differences; the exponent is set by the order of the
truncation term.

**(c)** With $C_t = C_r = 1$ and $u = 2.2\times10^{-16}$:

$$h_{\text{opt}} = u^{1/4} = \left(2.2\times10^{-16}\right)^{1/4}
= \boxed{1.2179\times10^{-4}}, \qquad
E(h_{\text{opt}}) = 2\sqrt{u} = \boxed{2.966\times10^{-8}} .$$

So the crossover mesh has about $10^{4}$ cells, and the best achievable relative
accuracy of this second-order scheme in binary64 is about $3\times10^{-8}$ — seven
digits, not sixteen. A typical working mesh of ten to a few hundred nodes is two to
three orders of magnitude coarser than the crossover, so its error is entirely
truncation ($10^{-2}$ to $10^{-5}$) and round-off is irrelevant.

**(d)** The implication is that round-off is not the limiting factor at working
meshes, and that refining a mesh to "get more digits" hits a wall at about
$10^{4}$ nodes per unit length beyond which the answer gets *worse* while the cost
keeps rising. The trade-off becomes visible in one situation: when the scheme is
formulated in physical units with badly scaled coefficients, so that the
$C_r$ constant is enormous — the lesson's §3.6 example, where evaluating
$\nabla^{2}V$ in physical units with $h = 10^{-5}$ m failed because $V\sim10^{7}$
times $u$ divided by $h^{2}$ swamps a Laplacian of order $10^{-6}$. The remedy is
non-dimensionalisation before differencing, which restores $C_r$ to order unity and
the crossover to the estimate above.
