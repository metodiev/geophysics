# Solutions — 19-03-02 Element Types, Shape Functions and Quadrature

> **Read after attempting the exercises.** Numbers were computed, not estimated.

Lesson: [02 Element Types, Shape Functions and Quadrature](../02-fem-element-types.md).

---

## ★1 — Quadratic Lagrange basis

With nodes $s \in \{0, \tfrac12, 1\}$,

$$\varphi_0 = \frac{(s-\tfrac12)(s-1)}{(0-\tfrac12)(0-1)} = 2s^2-3s+1,$$
$$\varphi_1 = \frac{(s-0)(s-1)}{(\tfrac12)(\tfrac12-1)} = -4s^2+4s,$$
$$\varphi_2 = \frac{(s-0)(s-\tfrac12)}{(1)(1-\tfrac12)} = 2s^2-s .$$

At $s = 0.3$: $\varphi_0 = 2(0.09)-0.9+1 = 0.28$;
$\varphi_1 = -4(0.09)+1.2 = 0.84$; $\varphi_2 = 0.18-0.3 = -0.12$. Sum
$= 0.28+0.84-0.12 = 1.000000$. ✔

(The third value is negative: a Lagrange basis function is not a probability
distribution, and a nodal value may be extrapolated negativity-weighted.)

---

## ★2 — Gauss exactness at $n = 3$

An $n$-point Gauss-Legendre rule is exact for degree $\le 2n-1$, so $n = 3$ is
exact to degree 5. The first failing degree is $2n = 6$, and the error there is

$$\left|\sum_j w_j x_j^6 - \frac{2}{7}\right| = 4.571\times10^{-2},$$

which is the measured value in the lesson's table. The error is not round-off:
the rule is simply not exact at that degree.

---

## ★3 — Quadrature order for $p = 3$, $\deg a = 2$

Stiffness integrand $a\,\varphi_i'\varphi_j'$: degree $2 + 2p - 2 = 6$, so
$2n - 1 \ge 6$, i.e. $n \ge 4$ points.

Mass integrand $a\,\varphi_i\varphi_j$: degree $2 + 2p = 8$, so
$2n - 1 \ge 8$, i.e. $n \ge 5$ points.

The rules must deliver exactness degrees of at least 6 and 8 respectively. Note
how quickly the requirement grows with $p$ and with the degree of the
coefficient: this is why quadrature policy is computed rather than guessed.

---

## ★4 — A quadratic element solved by hand

With $h = 0.5$ m, $a = 1$ and $f = 1$:

$$K^{(e)} = \frac{1}{3(0.5)}\begin{pmatrix}7&-8&1\\-8&16&-8\\1&-8&7\end{pmatrix}
= \begin{pmatrix}4.6667&-5.3333&0.6667\\-5.3333&10.6667&-5.3333\\
0.6667&-5.3333&4.6667\end{pmatrix},$$

and the load vector is $\int_0^h \varphi_j\,\mathrm{d}x = \frac{h}{6}(1,4,1)
= (0.083333,\ 0.333333,\ 0.083333)$. With both endpoints held at zero, the single
free equation is $K_{11}U_1 = F_1$:

$$U_1 = \frac{0.333333}{10.666667} = 0.031250000\ \text{m}.$$

The exact solution of $-u'' = 1$ with $u(0) = u(h) = 0$ is
$u = x(h-x)/2$, whose midpoint value is $h^2/8 = 0.031250000$ m. Agreement is
exact, because the exact solution is quadratic and the basis contains
quadratics: with one element there is nothing left for the method to
approximate. A single-element test is therefore a *consistency* check, not a
convergence test, and a convergence study needs at least two elements.

---

## ★5 — What a single quadrature point does

The single Gauss point of a 1-point rule on the parent interval is the midpoint
$\xi = 0$, which maps to the element midpoint $s = \tfrac12$ — and the middle
quadratic shape function has $\varphi_1'(s) = 0$ exactly at that point
($\varphi_1 = -4s^2+4s$, so $\varphi_1' = -8s+4 = 0$ at $s = 0.5$). Every entry of
the middle row and column of the stiffness therefore vanishes:

$$K^{(e)}_{n_q=1} = \begin{pmatrix}4.25&0&-4.25\\0&0&0\\-4.25&0&4.25\end{pmatrix},
\qquad \text{eigenvalues } (0,\ 0,\ 8.5).$$

The element matrix is **singular**, not merely inaccurate. The measured
difference from the reference, $2.267\times10^{1}$, is exactly the missing
diagonal entry: $a_{\rm mid}\cdot16/(3h) = 1.0625\times16/0.75 = 22.667$.

Two consequences worth distinguishing:

1. *What the user sees.* The assembled system is singular, and the solve raises
   `LinAlgError: Singular matrix` — a loud failure. That is the good case.
2. *What is dangerous.* A scheme in which the under-integration is only partly
   degenerate (for example a $p=3$ element integrated with two points) does **not**
   raise; it returns a smooth, plausible, wrong answer, and the only defence is
   the degree count of Section 2.1 of the lesson: compare $2n-1$ with
   $\deg a + 2p$ and refuse to run otherwise.

In a convergence study, the degenerate case does not produce an order at all; the
partly degenerate case produces an order lower than $p+1$ with a large constant,
which is easy to mistake for a pre-asymptotic transient.

---

## ★6 — Degrees of freedom for a fixed tolerance

From the measured table (smallest mesh with $\mathrm{L}^2 < 10^{-8}$):

| $p$ | $n_{\rm elem}$ | ndof | $\mathrm{L}^2$ error |
|---|---|---|---|
| 1 | 8192 | 8193 | $9.49\times10^{-9}$ |
| 2 | 256 | 513 | $7.51\times10^{-9}$ |
| 3 | 64 | 193 | $1.36\times10^{-9}$ |

Degree-of-freedom ratios: $8193/513 = 15.97$ between $p=1$ and $p=2$, and

$$\frac{8193}{193} = 42.45$$

between $p = 1$ and $p = 3$.

Work ratios depend on the solver, which is the honest part of the answer:

- a **sparse banded** solve in one dimension costs $O(\mathrm{ndof})$ to
  $O(\mathrm{ndof}\cdot b)$ with bandwidth $b = p+1$, so the work ratio is
  between $42.45$ and $42.45 \times 4/2 = 85$;
- a **dense** solve costs $O(\mathrm{ndof}^3)$, giving
  $42.45^3 = 7.65\times10^{4}$;
- per-degree-of-freedom cost also grows with $p$ (assembly quadrature, and the
  stiffness spectrum of lesson [04-03](../../04-spectral-and-pseudospectral/03-spectral-elements.md)).

So "p-refinement saves a factor 42 in unknowns" is correct and solver-independent;
"p-refinement saves a factor 7.6×10⁴ in time" is true only for a dense solver and
is a claim about the solver, not about the method.

---

## ★7 — Fitting the conditioning growth of equally spaced nodes

Measured condition numbers of the element mass matrix with equally spaced nodes:

| $p$ | 4 | 6 | 8 | 10 |
|---|---|---|---|---|
| $\mathrm{cond}$ | $1.414\times10^{1}$ | $4.421\times10^{1}$ | $2.197\times10^{2}$ | $1.620\times10^{3}$ |

A least-squares fit of $\log(\mathrm{cond})$ against $p$ gives a slope of
**0.791 per unit $p$**, i.e. a factor $e^{0.791} = 2.206$ per unit order. The
prediction at $p = 20$ is

$$\mathrm{cond}(20) \approx 1.414\times10^{1}\,e^{0.791(20-4)}
= 4.459\times10^{6}.$$

At a condition number of $4.5\times10^{6}$ a double-precision solve loses about
$\log_{10}(4.5\times10^{6}) = 6.65$ digits — two thirds of the 16 available. The
consequence is that the mass matrix cannot be inverted reliably, and that the
*interpolation* itself (through the Vandermonde system that defines the basis) is
worse still. The remedy is measured in the lesson: Gauss-Lobatto nodes give
$1.99\times10^{1}$ at $p = 10$ and grow very slowly, a factor $8\times10^{4}$
better at that order and far more at $p = 20$.

Note the honest status of the extrapolation: it is a fit to four measured points
over a factor 2.5 in $p$. It is offered as an estimate with its method stated, not
as a law.

---

## ★8 — Separating lumping error from discretisation error

**Configurations.** Solve the same generalised eigenproblem
$Kv = \lambda Mv$ for $-u''$ with $u(0) = u(1) = 0$, on the same mesh, twice:
(A) with the mass matrix evaluated by a high-order Gauss rule (consistent), and
(B) with the mass matrix evaluated by the element's own node/weight rule (the
diagonal, lumped form). Everything else — $K$, the mesh, the boundary conditions —
is identical.

**Metric.** The relative error $|\lambda_1^{(A,B)}/\pi^2 - 1|$ of the smallest
eigenvalue, plus the *difference* between the two runs.

**Prediction.**

1. Both runs converge to $\pi^2$ under $h$-refinement at the same measured order
   (the lesson's P1 table: consistent $+3.22\times10^{-3} \to +2.01\times10^{-4}$
   and lumped $-1.63\times10^{-3} \to -1.76\times10^{-4}$, both improving by
   roughly the same factor).
2. At *fixed* $h$ the difference between the runs is a pure quadrature effect,
   because the discretisation error is common to both. If the two agree at fixed
   $h$, the lumping is not what limits the answer.
3. The difference must vanish under refinement — if it does not, one of the two
   implementations has an error that does not scale with $h$, and that is the
   finding.
4. The sign of the lumping error is not fixed: the measured table shows the
   lumped eigenvalue below the consistent one at $p=1$ and $p=2$ and *above* it at
   $p=3$, $n_{\rm elem}=8$ ($9.875672$ against $9.869605$). A design that assumes
   a sign is not supported by the measurement.

**Why this separates the two.** Refinement changes both errors, so it cannot
attribute them; a fixed-mesh comparison between the two mass matrices changes only
the quadrature, so the difference is the quadrature error *at that mesh*. Reporting
both, and both under refinement, is what makes the attribution defensible.
