# Solutions — 19-03-01 Weak Formulation and the Galerkin Method

> **Read after attempting the exercises.** Numbers were computed, not estimated;
> where a value is quoted from the demonstration it is identified as such.

Lesson: [01 Weak Formulation and the Galerkin Method](../01-fem-weak-form.md).

---

## ★1 — Integration by parts, twice

For $v \in H^1_0(0,1)$ (so $v(0) = v(1) = 0$):

$$-\int_0^1 u''v\,\mathrm{d}x
= \int_0^1 u'v'\,\mathrm{d}x - \left[u'v\right]_0^1
= \int_0^1 u'v'\,\mathrm{d}x,$$

because both boundary terms carry a factor $v = 0$. The test space removes the
boundary term by construction — this is what makes Dirichlet conditions
*essential*.

For $v$ with $v(0) = 0$ but $v(1) \ne 0$:

$$-\int_0^1 u''v\,\mathrm{d}x = \int_0^1 u'v'\,\mathrm{d}x - u'(1)v(1).$$

The extra term is $-u'(1)v(1)$, a **flux** term, and it moves to the right-hand
side with a sign flip. Nothing constrains the nodal value at $x = 1$; the
condition on the flux is *natural*.

---

## ★2 — Two element integrals directly

With $\varphi_0 = 1 - x/h$ and $\varphi_1 = x/h$ on $[0,h]$:

$$K_{00} = \int_0^h \left(-\frac{1}{h}\right)^2 \mathrm{d}x = \frac{1}{h^2}\cdot h
= \frac{1}{h},$$

$$M_{01} = \int_0^h \left(1-\frac{x}{h}\right)\frac{x}{h}\,\mathrm{d}x
= h\int_0^1 (1-s)s\,\mathrm{d}s = h\left(\frac{1}{2}-\frac{1}{3}\right)
= \frac{h}{6}.$$

Units: $K_{00}$ is 1/length and $M_{01}$ is length, matching
$\int (u')^2\,\mathrm{d}x$ and $\int u^2\,\mathrm{d}x$ for dimensionless $u$ —
so the ratio $K/M$ has units of 1/length², as a second derivative must.

---

## ★3 — The manufactured load

$u = \sin(\pi x)$ gives $u'' = -\pi^2\sin(\pi x)$, so

$$f = -u'' = \pi^2\sin(\pi x).$$

With $x$ in metres and $u$ dimensionless (say metres of displacement), $u''$ has
units m$^{-1}$ and so does $f$. A useful check: in the finite-element system the
right-hand side is $\int f\varphi\,\mathrm{d}x$ with units m$^{-1}\cdot$m $= 1$,
and dividing by $K_{ii} \sim 1/$m gives a nodal value in metres.

---

## ★4 — Two-element assembly for $f = 1$, $h = 1/2$

Element matrices: $K^{(e)} = 2\begin{pmatrix}1&-1\\-1&1\end{pmatrix}$ since
$1/h = 2$. Loads: for $f = 1$,

$$F_1^{(1)} = \int_0^{1/2}\frac{x}{1/2}\,\mathrm{d}x = 2\cdot\frac{(1/2)^2}{2}
= 0.25, \qquad F_1^{(2)} = 0.25,$$

so $F_1 = 0.50$ and

$$K_{11} = 2 + 2 = 4, \qquad U_1 = \frac{0.50}{4} = 0.125000.$$

The exact solution of $-u'' = 1$ with $u(0) = u(1) = 0$ is
$u = x(1-x)/2$, so $u(1/2) = 0.125000$. The values agree **exactly**: this is the
one-dimensional nodal-exactness result of the lesson, and it holds even with two
elements. The approximation is nevertheless poor between the nodes, since a
piecewise-linear function cannot follow a parabola.

---

## ★5 — Order from two measurements

The mesh ratio is

$$\frac{h_1}{h_2} = \frac{0.125}{1.953\times10^{-3}} = 64,$$

and the error ratio is

$$\frac{7.264\times10^{-2}}{1.188\times10^{-3}} = 61.14,$$

so the measured order is

$$p = \frac{\log(61.14)}{\log(64)} = 0.989 .$$

That is first order, to within the constant drift of the leading error term. The
implied leading constant is

$$C = \frac{1.188\times10^{-3}}{1.953\times10^{-3}} = 0.6082
\quad\text{(dimensionless)},$$

so at $h = 9.77\times10^{-4}$ m:

$$E \approx C h = 0.6082 \times 9.765\times10^{-4} = 5.94\times10^{-4}\ \text{m}.$$

Note the drift in $C$ itself: $0.5811$ at $h = 0.125$ against $0.6082$ at
$h = 1.953\times10^{-3}$. A first-order scheme with a slowly varying constant is
what "first order" means in practice, and it is why a single error/h ratio is not
a proof of order.

---

## ★6 — What the wrong boundary condition gives

With $u(0) = 0$ and the end at $x = 1$ left free, the problem being solved is
$-u'' = \pi^2\sin(\pi x)$ with $u'(1) = 0$. The general solution is
$u = \sin(\pi x) + Bx$; imposing $u'(1) = \pi\cos(\pi) + B = -\pi + B = 0$ gives
$B = \pi$, hence

$$u = \sin(\pi x) + \pi x, \qquad u(1) = \pi = 3.141592654 .$$

The demonstration measures $\max|u_h - (\sin\pi x + \pi x)| = 3.15\times10^{-14}$
at 64 elements, i.e. the discrete solution matches this closed form.

The colleague's $u_h(1) = 3.99$ is neither $0$ (the Dirichlet answer) nor $\pi$
(the natural answer). Since a one-dimensional P1 solve reproduces the nodal value
to round-off, a 27% discrepancy cannot be a discretisation error: the code is not
solving either stated problem. The confirming test is a refinement study against
$\pi$; if the value does not move, the error is in the formulation or the assembly
rather than in the mesh.

---

## ★7 — The leading constant of the $\mathrm{L}^2$ error

For P1 Galerkin in one dimension with an exactly integrated load the solution is
the interpolant, so the $\mathrm{L}^2$ error is the interpolation error. Standard
interpolation theory gives $\|u-I_hu\|_{L^2} = C h^2$ with
$C \propto \|u''\|_{L^2}$, and the dimensional argument is immediate: the error
integrand is $(u-I_hu)^2$, with $u - I_hu \sim h^2 u''$, so
$E^2 \sim h^4\|u''\|^2$ and $E \sim h^2\|u''\|$.

Estimating $C$ empirically from the measured table
($\|u''\|_{L^2} = \pi^2\sqrt{1/2} = 6.978$ for $u = \sin(\pi x)$):

| $h$ | measured $\mathrm{L}^2$ error | $C = E/h^2$ |
|---|---|---|
| 1/8 | $9.921\times10^{-3}$ | 0.6349 |
| 1/16 | $2.487\times10^{-3}$ | 0.6367 |
| 1/32 | $6.220\times10^{-4}$ | 0.6369 |
| 1/64 | $1.555\times10^{-4}$ | 0.6369 |
| 1/128 | $3.888\times10^{-5}$ | 0.6370 |

The constant stabilises at $0.6369$, and the estimate from $h = 1/8$ alone
(0.6349) is low by 0.3% — the $O(h^2)$ correction to the leading term. The ratio
$C/\|u''\|_{L^2} = 0.6369/6.978 = 0.09127$, so on this problem
$E \approx 0.0913\,h^2\|u''\|_{L^2}$: a form that is dimensionally consistent and
that predicts the whole table from one number. The point of the exercise is not
the constant but the method: **measure the constant, then use it to predict,
then check the prediction.**

---

## ★8 — A verification design for the natural boundary term

**Two runs.** Both solve $-u'' = \pi^2\sin(\pi x)$ and impose $u(0) = 0$; both
leave $x = 1$ free. Run A adds the boundary term $+g\,v(1)$ with $g = u'(1)$ from
the weak form; run B omits it (or takes the opposite sign), which is the
implemented error the test is designed to catch.

**Metric.** $\max_i|u_h(x_i) - (\sin\pi x_i + \pi x_i)|$ on a mesh of 64 elements,
i.e. the distance from the *known* closed-form solution of the natural-boundary
problem. Using a closed form rather than another code is what makes this
verification rather than a comparison.

**Expected for the correct implementation.** The measured value in the lesson is
$3.15\times10^{-14}$: round-off, because the natural boundary term is the only
thing that distinguishes this problem from the Dirichlet one and the closed form
includes it.

**Expected for the sign error.** The discrete problem is a different problem with
a different exact solution; the term $g\,v(1)$ contributes to a single equation,
so the last nodal value moves by an amount proportional to $g/K_{nn}$ — of order
0.1–1 here, i.e. ten to fourteen orders of magnitude above the correct run. The
test is therefore decisive with one number and no tuning.

**Why not use a Dirichlet run as the reference.** The Dirichlet problem has
$u(1) = 0$ imposed by row deletion, so it never exercises the natural term at
all. A test that cannot fail is not a test.
