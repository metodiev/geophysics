# Solutions — 01-08-05 Sturm–Liouville Theory and Eigenfunction Expansions

> **Read this after attempting the exercises, not before.** Every integral below
> was evaluated numerically with composite Simpson quadrature on at least
> $2\times10^{4}$ intervals, and every eigenvalue identity was checked by
> substitution.

---

## ★1 — Self-adjoint form

**(a)** $y'' + \lambda y = 0$. Already in the form
$-(py')'+qy = \lambda wy$ with $p = 1$, $q = 0$, $w = 1$. The interval is
whatever it is; if it is $[a,b]$ with finite $a$ and $b$ and $p>0$ on it, both
endpoints are **regular** and ordinary Dirichlet/Neumann/Robin conditions apply.

**(b)** $(1-x^{2})y'' - 2xy' + \lambda y = 0$. The first two terms are already a
perfect derivative: $\dfrac{d}{dx}\left[(1-x^{2})y'\right] = (1-x^{2})y'' - 2xy'$.
So

$$-\frac{d}{dx}\left[(1-x^{2})y'\right] = \lambda y
\quad\Longrightarrow\quad p = 1-x^{2},\ q = 0,\ w = 1 .$$

**Both endpoints are singular**, because $p(\pm1) = 0$. The boundary condition
that replaces the usual one is **boundedness** of the solution at $x = \pm1$; it
is a *consequence* of the equation rather than a separate physical statement.

**(c)** $y'' + 2y' + \lambda y = 0$. Multiply by the integrating factor
$e^{\int 2\,dx} = e^{2x}$:

$$e^{2x}y'' + 2e^{2x}y' = \left(e^{2x}y'\right)'
\quad\Longrightarrow\quad
-\left(e^{2x}y'\right)' = \lambda\,e^{2x}y,$$

so $p = w = e^{2x}$ and $q = 0$. **Note $w\neq1$**: this problem's
orthogonality relation carries an exponential weight, and using $\int y_my_ndx$
would be wrong.

**(d)** $xy'' + y' + \lambda y/x = 0$. Here $xy''+y' = (xy')'$, so

$$-(xy')' = \lambda\,\frac{y}{x}, \qquad p = x,\ q = 0,\ w = \frac{1}{x}.$$

The endpoint $x = 0$ is singular; on an interval like $[1,e]$ both endpoints are
regular.

---

## ★2 — The sine–cosine problem on $[0,2]$

**(a)** With $y(0) = 0$ the solution is $y = \sin(kx)$ with $\lambda = k^{2}$.
The second condition $y'(2) = k\cos(2k) = 0$ requires $\cos(2k) = 0$, i.e.
$2k = (2n+1)\pi/2$, so

$$k_n = \frac{(2n+1)\pi}{4}, \qquad
\lambda_n = \left(\frac{(2n+1)\pi}{4}\right)^{2}, \qquad
y_n = \sin\!\left(\frac{(2n+1)\pi x}{4}\right), \quad n = 0,1,2,\dots$$

| $n$ | $k_n$ | $\lambda_n$ |
|---|---|---|
| 0 | 0.785398 | 0.616850 |
| 1 | 2.356194 | 5.551652 |
| 2 | 3.926991 | 15.421257 |
| 3 | 5.497787 | 30.225663 |

**(b)** Weight $w = 1$, and $\int_0^{2}y_n^{2}dx = 1$ exactly for every $n$. Using
$\int_0^{L}\sin^{2}(kx)\,dx = \frac{L}{2}-\frac{\sin(2kL)}{4k}$ with $L = 2$ and
$2k_nL = 4k_n = (2n+1)\pi$:

$$\int_0^{2}\sin^{2}(k_nx)\,dx = 1 - \frac{\sin\!\big((2n+1)\pi\big)}{4k_n} = 1,$$

since the sine of a multiple of $\pi$ vanishes. The normalisation constant is
therefore 1, which is a convenience of this particular interval.

**(c)** Numerical quadrature gives

$$\int_0^{2}y_0y_1\,dx = 8.3\times10^{-16}, \qquad
\int_0^{2}y_0^{2}dx = 1.0000000000 .$$

The off-diagonal value is at the round-off floor of the quadrature, which is the
strongest statement a numerical check can make.

---

## ★3 — Expansion of $f(x) = x$

**(a)** The coefficients are $b_n = \int_0^{2}x\,y_n\,dx / \int_0^{2}y_n^{2}dx$.
With $k = k_n$ and $k\cdot2 = (2n+1)\pi/2$,

$$\int_0^{2}x\sin(kx)\,dx
= \left[-\frac{x\cos(kx)}{k}+\frac{\sin(kx)}{k^{2}}\right]_0^{2}
= -\frac{2\cos(2k)}{k}+\frac{\sin(2k)}{k^{2}}
= \frac{(-1)^{n}}{k^{2}},$$

since $\cos((2n+1)\pi/2) = 0$ and $\sin((2n+1)\pi/2) = (-1)^{n}$. Hence

$$b_n = \frac{(-1)^{n}}{k_n^{2}} = \frac{(-1)^{n}16}{(2n+1)^{2}\pi^{2}},$$

$$b_0 = 1.621139, \qquad b_1 = -0.180127, \qquad b_2 = 0.064846 .$$

**(b)** $L^{2}$ error of the partial sum, $\left(\int_0^{2}(u_N-x)^{2}dx
\right)^{1/2}$:

| $N$ | 1 | 2 | 3 | 5 | 10 | 20 | 50 |
|---|---|---|---|---|---|---|---|
| error | $1.964\times10^{-1}$ | $7.829\times10^{-2}$ | $4.387\times10^{-2}$ | $2.073\times10^{-2}$ | $7.381\times10^{-3}$ | $2.614\times10^{-3}$ | $6.618\times10^{-4}$ |

**(c)** Between $N = 20$ and $N = 50$ the error falls by a factor $3.951$,
against $(50/20)^{3/2} = 3.953$: the observed rate is **$N^{-3/2}$**, i.e. the
coefficients decay like $n^{-2}$, and integrating the squared tail gives
$N^{-3}$, whose square root is $N^{-3/2}$.

The reason for the $n^{-2}$ decay is worth stating precisely. The
eigenfunctions $\sin((2n+1)\pi x/4)$ have period 8, so the expansion represents
the **period-8 extension** of $f$, namely $f(x) = x$ on $[0,2]$,
$f(x) = 4-x$ on $[2,6]$, $f(x) = x-8$ on $[6,8]$. That extension is
*continuous* (so the coefficients decay faster than $n^{-1}$) but has a **jump in
its first derivative at $x = 2$** (slope $+1$ on the left, $-1$ on the right),
which prevents the faster $n^{-3}$ decay that a smooth extension would give.
**The convergence rate is a statement about the periodic extension, not about
the function on the interval.** This is why the boundary conditions cannot be
chosen independently of the physics: they determine the extension, and hence the
rate at which the expansion can represent the data.

---

## ★★4 — Legendre polynomials and orthogonality

**(a)** Write $x^{2} = aP_0+bP_2$ with $P_0 = 1$, $P_2 = (3x^{2}-1)/2$:

$$x^{2} = a + \frac{b}{2}(3x^{2}-1) = \left(a-\frac{b}{2}\right)+\frac{3b}{2}x^{2}
\;\Longrightarrow\; \frac{3b}{2} = 1,\ a = \frac{b}{2}
\;\Longrightarrow\; b = \frac{2}{3},\ a = \frac{1}{3}.$$

So $x^{2} = \tfrac13P_0 + \tfrac23P_2$.

**(b)** Since $P_3$ is orthogonal to every lower polynomial, and $x^{2}$ is a
combination of $P_0$ and $P_2$,

$$\int_{-1}^{1}x^{2}P_3\,dx = \tfrac13\int P_0P_3\,dx + \tfrac23\int P_2P_3\,dx = 0,$$

confirmed numerically as $1.1\times10^{-16}$. **No integration is needed once the
expansion is known** — that is the whole practical value of orthogonality.

For $P_2$ the $P_0$ term vanishes by orthogonality and only the $P_2$ term
survives:

$$\int_{-1}^{1}x^{2}P_2\,dx = \frac{2}{3}\int_{-1}^{1}P_2^{2}dx
= \frac{2}{3}\cdot\frac{2}{5} = \frac{4}{15} = 0.266667 .$$

**(c)** At $x = \pm1$ the coefficient $p = 1-x^{2}$ vanishes, so the operator is
**singular** there and the natural condition is that the solution remain
**bounded**. Imposing a derivative condition at a singular endpoint would be
meaningless: $p\,y'$ need not vanish, and the endpoint is not part of the domain
in which the equation has to hold in the classical sense.

---

## ★★5 — The weight function is the substitution

**(a)** Put $t = \ln x$, so $x = e^{t}$, $t\in[0,1]$, and write
$Y(t) = y(e^{t})$. Then

$$\frac{dy}{dx} = \frac{1}{x}\frac{dY}{dt}, \qquad
x\frac{dy}{dx} = \frac{dY}{dt}, \qquad
\frac{d}{dx}\left(x\frac{dy}{dx}\right)
= \frac{1}{x}\frac{d^{2}Y}{dt^{2}},$$

so $-(xy')' = -\dfrac{1}{x}\dfrac{d^{2}Y}{dt^{2}}$ and the equation becomes

$$-\frac{1}{x}\frac{d^{2}Y}{dt^{2}} = \lambda\,\frac{Y}{x}
\;\Longrightarrow\;
-\frac{d^{2}Y}{dt^{2}} = \lambda Y .$$

The measure also transforms correctly: $dx = e^{t}dt = x\,dt$, so the integral
$\int_1^{e}(\cdot)\,\dfrac{1}{x}dx$ becomes $\int_0^{1}(\cdot)\,dt$. Hence the
problem in $t$ is exactly $-Y'' = \lambda Y$ with $Y(0) = Y(1) = 0$, and

$$\lambda_n = n^{2}\pi^{2}, \qquad Y_n = \sin(n\pi t)
\;\Longrightarrow\; y_n(x) = \sin(n\pi\ln x).$$

**(b)** The weight is essential because $w\,dx = \frac{1}{x}dx = dt$: **$w = 1/x$
is precisely the Jacobian of the substitution $t = \ln x$.** If the weight is
omitted — if one imposes orthogonality with respect to $dx$ instead of
$dx/x$ — the resulting functions are not sines in $t$, the eigenvalues are not
$n^{2}\pi^{2}$, and the expansion coefficients computed with the wrong measure
are wrong in a way that looks numerically reasonable.

**(c)** With $y = \ln x(1-\ln x) = t(1-t)$ and $y' = (1-2t)/x$,

$$R[y] = \frac{\int_1^{e}x(y')^{2}dx}{\int_1^{e}y^{2}\frac{dx}{x}}
= \frac{\int_0^{1}(1-2t)^{2}dt}{\int_0^{1}t^{2}(1-t)^{2}dt}
= \frac{1/3}{1/30} = 10.000000 .$$

The numerical evaluation gives $10.000000000$. Compare
$\lambda_1 = \pi^{2} = 9.869604$: the excess is **1.321 %**, and it is an upper
bound, as the Rayleigh quotient must be. Note that the trial function "wastes"
the entire shift in the eigenvalue in spite of being a good match in shape to
$\sin(\pi t) = \sin(\pi\ln x)$ — because $R$ is stationary at the true
eigenfunction, not at a shape that merely looks similar.

---

## ★★6 — Modal decay in a slab with one insulated face

**(a)** $\kappa = 2\times10^{-6}\ \mathrm{m^{2}\,s^{-1}}$ and the eigenvalues of
★2 give rates $\kappa\lambda_n$ and time constants $1/(\kappa\lambda_n)$:

| $n$ | $\lambda_n$ | rate (s⁻¹) | time constant |
|---|---|---|---|
| 0 | 0.616850 | $1.2337\times10^{-6}$ | $8.106\times10^{5}$ s $= 9.38$ d |
| 1 | 5.551652 | $1.1103\times10^{-5}$ | $9.006\times10^{4}$ s $= 1.042$ d |
| 2 | 15.421257 | $3.0843\times10^{-5}$ | $3.242\times10^{4}$ s $= 0.375$ d |

**(b)** At $t = 1/(\kappa\lambda_0)$ the factors $\exp(-\kappa\lambda_nt)$ are
$e^{-1} = 0.367879$ for $n = 0$, and for the higher modes
$e^{-\lambda_1/\lambda_0} = e^{-9.0000} = 1.234\times10^{-4}$ (mode 1) and
$e^{-\lambda_2/\lambda_0} = e^{-25.0} = 1.389\times10^{-11}$ (mode 2).

**(c)** The fundamental mode controls the long-time behaviour: by one fundamental
time constant the second mode is already $10^{-4}$ of its initial size. The
practical consequence is that **the cooling time of the slab is set by the
fundamental mode alone**, i.e.

$$t_{\text{cooling}} \sim \frac{1}{\kappa\lambda_0}
= \frac{16}{\pi^{2}\kappa} = 9.4\ \mathrm{d}.$$

Compare the same slab with both faces held at zero, for which
$\lambda_1 = (\pi/2)^{2} = 2.4674$ and $t_{\text{cooling}} = 4/(\pi^{2}\kappa)
= 2.35$ d. **The insulated face makes the slab cool four times more slowly**,
and the reason is visible in the eigenvalue rather than in $\kappa$: with half
the boundary area available to carry heat away, heat has to travel twice as far
on average to escape, which costs a factor of about 4 in the diffusion time.
**The eigenvalue, not only the diffusivity, carries the geometry** — so a change
of boundary condition is a change of timescale by a factor that is computed, not
guessed.

---

## ★★★7 — Two-term Rayleigh–Ritz

**(a)** With basis functions $\phi_1 = t(1-t)$ and $\phi_2 = t^{2}(1-t)^{2}$
($t = \ln x$), the generalised eigenvalue problem is
$\mathsf{A}\mathbf{c} = \lambda\mathsf{B}\mathbf{c}$ where, using the
transformed problem of ★5,

$$A_{ij} = \int_0^{1}\phi_i'(t)\,\phi_j'(t)\,dt, \qquad
B_{ij} = \int_0^{1}\phi_i(t)\,\phi_j(t)\,dt .$$

(The inner products are *not* weighted in the $t$ variable: the weight has been
absorbed by the substitution. Equivalently, in the original variable,
$A_{ij} = \int_1^{e}x\phi_i'\phi_j'\,dx$ and
$B_{ij} = \int_1^{e}\phi_i\phi_j\,dx/x$.)

**(b)** Evaluating the integrals by quadrature and solving the quadratic
$\det(\mathsf{A}-\lambda\mathsf{B}) = 0$ for its smaller root gives

$$\lambda_{\text{Ritz}} = 9.869749621,$$

with a coefficient ratio (one arbitrary normalisation) that reproduces that
value when the Rayleigh quotient of the resulting trial vector is evaluated
directly — the check that the algebra and the integrals are consistent.

**(c)** The excess over $\lambda_1 = 9.869604401$ is

$$\frac{9.869749621}{9.869604401}-1 = 1.4714\times10^{-5},
\quad\text{i.e. } 0.001471\ \% ,$$

against $1.321$ % for the one-term trial of ★5(c): **a factor of 898
improvement from adding one extra basis function.**

**(d)** The result must be an upper bound because for any admissible, non-zero
$y$,

$$\lambda_1 = \min_{y}\frac{\int(py'^{2}+qy^{2})dx}{\int wy^{2}dx}
\le \frac{\int(py'^{2}+qy^{2})dx}{\int wy^{2}dx} = R[y],$$

so enlarging the trial space can only lower the smallest Ritz value toward
$\lambda_1$. **Two lines of algebra, and they are what turn a numerical
eigenvalue estimate into a certified bound** — the reason the variational
characterisation matters in practice, not only in theory.

---

## ★★★8 — Robin conditions and a non-symmetric case

**(a)** For Robin conditions the boundary contributions to
$\int(yL[z]-zL[y])dx$ are the bracket

$$\left[p\left(zy'-yz'\right)\right]_a^{b}
= p(b)\left(z(b)y'(b)-y(b)z'(b)\right)
- p(a)\left(z(a)y'(a)-y(a)z'(a)\right).$$

At $x = a$ the conditions $\alpha y(a)+\beta y'(a) = 0$ and the identical
condition for $z$ give $y'(a) = -(\alpha/\beta)y(a)$ and
$z'(a) = -(\alpha/\beta)z(a)$. Substituting,

$$z(a)y'(a) - y(a)z'(a)
= -\frac{\alpha}{\beta}z(a)y(a) + \frac{\alpha}{\beta}y(a)z(a) = 0 .$$

The same argument at $x = b$ with $(\gamma,\delta)$ gives zero again. **Any
separated boundary condition — Dirichlet ($\beta = 0$), Neumann
($\alpha = 0$) or Robin — annihilates the bracket, because the condition fixes
the ratio $y'/y$ at each endpoint, and the bracket is antisymmetric in that
ratio.** This is the general content of "separated boundary conditions make the
operator symmetric", and it is worth seeing once in full.

**(b)** A **mixed-endpoint** condition, which relates the values at the two ends
rather than at one each, e.g.

$$y'(0) = y'(1), \qquad\text{or}\qquad y(0) = y(1),$$

does not fix $y'/y$ at either endpoint separately, so the two terms in the
bracket do not cancel. The classic physical source is a **periodic** problem,
such as a wave on a closed loop or the temperature in an annular basin, where
the domain has no boundary at all and the "conditions" identify the two ends.
Thus the reason periodic problems do not have the orthogonality structure of
§2 automatically is not an accident: it is a statement about the boundary terms.
(They do have such a structure — with a complex inner product and, in general,
degenerate eigenvalues — but it must be re-derived.)

**(c)** With $p = 1$, $y = \cos\pi x$ (not satisfying $y(0) = 0$),
$z = \sin2\pi x$ (satisfying Dirichlet) on $[0,1]$:

$$\int_0^{1}\left(yL[z]-zL[y]\right)dx = 12.566371, \qquad
\left[zy'-yz'\right]_0^{1} = 12.566371,$$

both equal to $4\pi$, agreeing to six decimals. **The identity holds; the
boundary term is simply not zero.** For comparison, replacing $y$ with
$\sin\pi x$ — which does satisfy the conditions — reduces the left side to
$-2.4\times10^{-15}$, i.e. zero at the quadrature's round-off floor.

---

## Extension notes

- The Legendre problem's second solution, $Q_n$, diverges logarithmically at
  $x = \pm1$. Boundedness is therefore not a matter of taste: admitting $Q_n$
  would make the eigenfunctions non-normalisable, and the expansion coefficients
  would diverge.
- Minimising $R[y]$ over $y = \sum_ic_i\phi_i$ gives
  $\partial R/\partial c_k = 0$, which after multiplying through by
  $\int wy^{2}dx$ becomes $\sum_iA_{ki}c_i = R\sum_iB_{ki}c_i$: the generalised
  eigenproblem, with $R$ playing the role of the eigenvalue. This is the cleanest
  derivation, and it shows why no separate variational principle needs to be
  invented.
- For a uniform initial condition on the slab of ★6, the coefficients are
  $b_n = \int_0^{2}y_ndx/\int_0^{2}y_n^{2}dx
  = \left[1-\cos(2k_n)\right]/k_n = 1/k_n = 4/((2n+1)\pi)$, since
  $\cos\!\big((2n+1)\pi/2\big) = 0$. At one fundamental time constant the
  surviving amplitude is dominated by $n = 0$; the number of modes needed for
  1 % accuracy at that time is governed by $\lambda_1/\lambda_0 = 9.0$ (mode 1
  decays nine times faster than mode 0), so the answer is small — in practice
  three or four modes suffice. That is a direct illustration of why a *few*
  modes are enough for long-time diffusive problems, and why early-time data are
  the only place where many modes are needed.
