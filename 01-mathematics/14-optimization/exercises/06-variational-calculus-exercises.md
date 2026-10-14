# Exercises — 01-14-06 Calculus of Variations and Its Geophysical Uses

Attempt these **closed-book** before opening the
[solutions](./06-variational-calculus-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Conventions: $F[y] = \int_a^b L(x,y,y')\,dx$; the first variation is
$\delta F[y;\delta y] = \frac{d}{d\epsilon}F[y+\epsilon\,\delta y]|_{\epsilon=0}$;
the variational derivative $g$ is defined by
$\delta F = \int_a^b g\,\delta y\,dx$. Always write the boundary term before
dropping it. Where a numerical value is asked for, state the quadrature or mesh
used.

Problems referring to
[`../code/variational_calculus_demo.py`](../code/variational_calculus_demo.py)
require you to run it and report its actual output.

---

## ★ Foundational

**★1.** Derive the Euler–Lagrange equation and solve it for
$F[y] = \int_0^1\left(y'^{2} + 2xy\right)dx$ with $y(0) = y(1) = 0$.

(a) Compute $\partial L/\partial y$ and $\partial L/\partial y'$.
(b) Write the Euler–Lagrange equation and reduce it to an ordinary differential
equation for $y$.
(c) Apply both boundary conditions and give the solution.
(d) Evaluate the solution at $x = 1/2$ and state whether it is a minimum or a
maximum of $F$.

---

**★2.** For $F[y] = \int_0^1 y'^{2}\,dx$ with $y(0) = 0$ and $y(1)$ **free**:

(a) State the Euler–Lagrange equation and the natural boundary condition.
(b) Solve the boundary-value problem and give $y(1)$.
(c) State what would have changed had the natural condition been imposed *and*
$\delta y(1) = 0$ been required as well.
(d) In one sentence, state what a natural boundary condition means physically.

---

**★3.** Write the direct-method system for
$F[y] = \int_0^1\left(y'^{2} + k^{2}y^{2}\right)dx$ with fixed endpoints.

(a) Write the discrete functional $F_h$ using a forward difference for $y'$ and
the trapezoid rule for $y^{2}$.
(b) Differentiate with respect to an interior node $y_j$ and obtain
$(2 + h^{2}k^{2})y_j - y_{j-1} - y_{j+1} = 0$.
(c) Identify the conditions under which the same matrix becomes an eigenvalue
problem, and write it.
(d) State the order of accuracy of the scheme and where the order comes from.

---

**★4.** Show that the Rayleigh quotient is bounded below by the smallest
eigenvalue.

(a) Write $R[y] = \int p y'^{2}/\int y^{2}$ with $y(a) = y(b) = 0$ and expand $y$
in the eigenfunctions of $-(py')' = \lambda y$.
(b) Show $R\ge\lambda_1$ with equality only for $y = \phi_1$.
(c) Explain why a discretisation restricted to a subspace can only *raise* $R$ and
hence why the discrete eigenvalue is a lower bound... or, if your expansion shows
the opposite, state which inequality holds and why.
(d) State why this bound is useful in practice.

---

## ★★ Applied

**★★5.** Verify a variational derivative numerically.

Take $y = x$, $\delta y = \sin\pi x$ on $[0,1]$, and
$F[y] = \int_0^1\left(y'^{2} + y^{2}\right)dx$, so that $y$ is not a minimiser.

(a) Show analytically that $g(x) = 2y - 2y''$ and evaluate $\int_0^1 g\,\delta y\,dx$.
(b) Compute the central difference
$\left(F[y+\epsilon\delta y] - F[y-\epsilon\delta y]\right)/(2\epsilon)$ by
quadrature for $\epsilon = 10^{-3}$ and $10^{-5}$.
(c) Compare the two routes and state what limits the agreement.
(d) State what the check proves and what it does not prove.

---

**★★6.** Free end, natural condition, and the discrete evidence.

For $F[y] = \int_0^1\left(y'^{2} - 2y\right)dx$ with $y(0) = 0$ and $y(1)$ free:

(a) Derive the Euler–Lagrange equation and the natural condition at $x = 1$.
(b) Solve the problem exactly and give $y(1)$.
(c) The discrete solution obeys $y_n - y_{n-1} = h^{2}/2$ at $n = 10$. Show that
this is the natural condition discretised, and state the finite-difference
approximation of $y'(1)$ it implies.
(d) Explain why the error of that example is at round-off for every $n$, and what
that implies about using it to measure a convergence rate.

---

**★★7.** Condition number of the direct-method matrix.

The matrix $K = \operatorname{tridiag}(-1,2,-1)$ of order $m$ has
$\kappa(K) = \frac{2 + 2\cos(\pi/(m+1))}{2 - 2\cos(\pi/(m+1))}$.

(a) Evaluate $\kappa$ at $n = 10, 20, 40, 80, 160$ (with $m = n-1$).
(b) Compare each with the asymptotic form $4(m+1)^{2}/\pi^{2}$.
(c) State how many digits the solve loses at the finest mesh and whether that
matters in binary64.
(d) Show that the resolution-versus-conditioning trade is
accuracy $O(h^{2})$ against conditioning $O(h^{-2})$, and state the practical rule.

---

**★★8.** Solve the direct-method system explicitly.

For $F[y] = \int_0^1\left(y'^{2} + y^{2}\right)dx$, $y(0) = 0$, $y(1) = 1$, whose
exact solution is $y = \sinh x/\sinh 1$:

(a) Write the tridiagonal system and solve it with the Thomas algorithm at
$n = 10$.
(b) Report the computed and exact values at the nine interior nodes.
(c) Report the maximum error at $n = 10$ and $n = 20$ and the measured order.
(d) Evaluate the discrete functional at the discrete minimiser and at the sampled
exact solution at $n = 40$, and state which is larger and why the *discrete*
value is not a lower bound for the continuous functional.

---

## ★★★ Research-oriented

**★★★9.** The Rayleigh quotient as a discrete eigenproblem.

Discretise $R[y] = \int_0^1 y'^{2}/\int_0^1 y^{2}$ with $y(0) = y(1) = 0$ using the
three-point stencil and lumped mass, giving $\frac{1}{h^{2}}Ky = \lambda y$.

(a) Show the exact eigenvalues of $K/\Delta x^{2}$ are
$\lambda_k = (4/\Delta x^{2})\sin^{2}(k\pi\Delta x/2)$.
(b) Evaluate $\lambda_{\min}$ at $n = 10, 20, 40, 80$ and the error against
$\pi^{2} = 9.8696044011$.
(c) Report the measured order of the error and compare it with the asymptotic
prediction $\lambda_{\min} = \pi^{2}\left(1 + \pi^{2}/(12n^{2}) + O(n^{-4})\right)$.
(d) State why inverse iteration, not power iteration, is the right method here, and
how many exact digits you would claim at $n = 80$.

---

**★★★10.** The price of refinement.

(a) State the two error terms in a finite-difference solve of the direct-method
system: truncation and round-off, with their powers of $h$.
(b) Derive the optimal $h$ that minimises their sum, in terms of $u$ and the
constant of the truncation term.
(c) Evaluate the optimal $h$ and the resulting total error for $u = 2.2\times10^{-16}$
and unit truncation constant, and compare the working mesh of a typical problem
(ten to a few hundred nodes) with it.
(d) State what that comparison implies about round-off in practice, and the one
situation in which the trade-off becomes visible.
