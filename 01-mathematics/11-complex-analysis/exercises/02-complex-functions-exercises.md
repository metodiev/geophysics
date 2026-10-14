# Exercises — 01-11-02 Holomorphic Functions and Cauchy-Riemann Equations

Attempt these **closed-book**, then open the
[solutions](./02-complex-functions-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Where a numerical check is requested, say explicitly which quantity you expect to
be zero and how fast you expect the residual to shrink as the step shrinks.

---

## ★ Foundational

**★1.** For $f(z) = z^{3}$, write $u(x,y)$ and $v(x,y)$, compute the four partial
derivatives, and verify the Cauchy-Riemann equations. State $f'(z)$ in two ways.

---

**★2.** Show that $u(x,y) = x^{3} - 3xy^{2}$ is harmonic, find its harmonic
conjugate $v$, and identify $u + iv$ as a known function of $z$. Evaluate
$u$ and $v$ at $(x,y) = (2,1)$.

---

**★3.** Decide, with reasons, whether each function can be holomorphic on an open
set. Where it can, name the largest open set.

(a) $f(z) = \bar z$
(b) $f(z) = \operatorname{Re} z$
(c) $f(z) = 1/z$
(d) $f(z) = |z|^{2}$

---

**★4.** For $f(z) = e^{z}$ write $u$ and $v$, verify the Cauchy-Riemann
equations, and confirm that $f'(z) = f(z)$ by computing $u_{x} + iv_{x}$.

---

## ★★ Applied

**★★5.** The complex potential $w(z) = m\log z$ represents a line mass.

(a) Give the potential $\phi$ and the stream function $\psi$ in polar
coordinates.
(b) Verify that $\phi$ satisfies Laplace's equation in polar form,
$\phi_{rr} + \phi_{r}/r + \phi_{\theta\theta}/r^{2} = 0$.
(c) Explain why the potential decays logarithmically rather than as $1/r$, and
say what that implies for the interpretation of a 2-D gravity profile.
(d) A finite-difference Laplacian of $\phi$ at a point a unit away from the source
gives $2.7\times10^{-6}$ with $h = 0.01$ and $6.7\times10^{-7}$ with $h = 0.005$.
What do these two numbers establish, and what would it mean if they were both
$4.0$?

---

**★★6.** A two-dimensional anomaly is described by $w(z) = \mu/z$ with
$\mu = 2.5$ (units of potential × length).

(a) Write $\phi$ and $\psi$ in polar form and in Cartesian form.
(b) Compute the field components $-\phi_{x}$ and $-\phi_{y}$ and describe the
pattern of the anomaly.
(c) A colleague proposes using the same formula for a buried sphere at depth
$d$. State the two distinct reasons this is wrong.

---

**★★7.** Given $u(x,y) = e^{x}\cos y$:

(a) verify $u$ is harmonic;
(b) find $v$ by integrating the Cauchy-Riemann equations, and fix the constant by
$v(0,0) = 0$;
(c) evaluate $v(0.5,1.0)$ and compare with the value obtained from the closed
form for $u + iv$.

---

**★★8.** The map $w = z^{2}$ acts on the wedge
$0 \le \arg z \le \pi/4$.

(a) What is the image wedge?
(b) Where is the map conformal, and where is it not?
(c) Explain, in terms of (b), why a numerical solution of Laplace's equation in a
region with a right-angled re-entrant corner develops a singularity at the corner.

---

## ★★★ Research-oriented

**★★★9.** The half-plane Dirichlet problem with boundary value
$f(t) = 1/(1+t^{2})$ has the solution $\phi(x,y) = (1+y)/[(1+y)^{2}+x^{2}]$.

(a) Verify that this $\phi$ is the real part of $g(z) = 1/(1-iz)$.
(b) State where the singularity of $g$ lies and why that location is what makes
the solution legitimate in the upper half plane.
(c) Verify by direct integration that $\phi$ is harmonic away from the
singularity.
(d) Explain what changes if the boundary data are given on the *lower* half
plane instead, and how the formula would be modified.

---

**★★★10.** Design a numerical test for holomorphy of a black-box function
$f(z)$ that returns $u$ and $v$ to full double precision, and answer:

(a) What quantity do you compute, and at what step sizes?
(b) What convergence do you expect, and what is the round-off floor?
(c) Your test reports residuals of $1.1\times10^{-12}$ at $h = 10^{-4}$ for a
polynomial and $2.3\times10^{-9}$ for a transcendental function. Explain why the
two differ and why neither is evidence against holomorphy.
(d) The function $g(z) = \sqrt{z}$ is tested at $z = 0.01$ and passes; at
$z = -0.01$ it fails. Explain.

---

## Self-assessment before the solutions

- [ ] I derived the Cauchy-Riemann equations by matching two directions, not by
      looking them up.
- [ ] I stated which partial derivatives must be continuous for sufficiency.
- [ ] I wrote down explicitly which quantity should be zero in ★5(d).
- [ ] I explained the two halves of ★6(c) separately.
