# Exercises — 01-06-06 Gauss, Stokes and Green Theorems

Attempt these **closed-book** before opening the
[solutions](./06-integral-theorems-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Use $G = 6.674\times10^{-11}$.

---

## ★ Foundational

**★1.** Verify the divergence theorem for
$\mathbf{F} = (x,\ 2y,\ 3z)$ on the cube $[0,1]^3$ by computing both sides
independently.

---

**★2.** Verify Stokes' theorem for $\mathbf{F} = (z,\ x,\ y)$ on the triangular
surface with vertices $(1,0,0)$, $(0,1,0)$ and $(0,0,0)$ in the plane $z=0$.

(a) Compute the curl.
(b) Compute the surface integral.
(c) Compute the circulation around the boundary, traversed counterclockwise as
seen from $+z$.
(d) Confirm equality.

---

**★3.** Verify Green's theorem for $P = -y^2$, $Q = x^2$ on the unit square
$[0,1]^2$ with counterclockwise boundary.

---

**★4.** For $\mathbf{F} = \mathbf{r} = (x,y,z)$:

(a) compute $\nabla\cdot\mathbf{F}$;
(b) state, without further integration, the flux of $\mathbf{F}$ out of any
region of volume $V$;
(c) verify the statement for a cube of side 2 centred at the origin and for the
unit ball.

---

## ★★ Applied

**★★5.** A uniform ball of radius $a$ and density $\rho$ has total mass $M$.

(a) Use Gauss's law for gravity to derive $g(r)$ for $r \le a$ and $r \ge a$,
stating which surface you chose and why.
(b) Confirm that the two expressions agree at $r = a$.
(c) Show that the potential difference between the centre and the surface is
$\Delta V = -\tfrac{2}{3}\pi G\rho a^2$ (careful with the sign convention), and
evaluate it for $\rho = 3000\ \mathrm{kg\,m^{-3}}$ and $a = 6.4\times10^6$ m.
(d) State why the flux argument also gives the interior field of a *shell*-free
cavity inside an arbitrary spherically symmetric body.

---

**★★6.** Derive and verify Green's first identity for
$\phi = x^2$, $\psi = y^2$ on the cube $[0,1]^3$, computing both sides
independently.

---

**★★7.** Mass conservation in a deforming medium.

(a) Write the continuity equation in divergence form and identify each term.
(b) Integrate it over a fixed volume and apply the divergence theorem to obtain
the integral form.
(c) For a steady state in which density does not change with time but material
flows, state the resulting condition on the velocity field.
(d) A numerical convection code reports a maximum $\lvert\nabla\cdot\mathbf{v}\rvert$
of $10^{-9}\ \mathrm{s^{-1}}$ in a velocity field with typical magnitude
$10^{-9}$ m/s and a domain of $10^6$ m. Assess whether this indicates a
convergence problem.

---

**★★8.** A horizontal interface at $z = 0$ separates two media. The gravitational
field satisfies $\nabla\cdot\mathbf{g} = -4\pi G\rho$ on either side, with a
density jump $\Delta\rho$ across the interface.

(a) Apply the divergence theorem to a thin pillbox straddling the interface, of
area $A$ and thickness $\epsilon$, and take $\epsilon \to 0$.
(b) State the resulting jump condition on the normal component $g_z$.
(c) Interpret the result physically, and explain why the differential form
$\nabla\cdot\mathbf{g} = -4\pi G\rho$ is unusable exactly on the interface while
the jump condition is not.

---

## ★★★ Research-oriented

**★★★9.** Stokes' theorem on a curved surface, verified numerically.

Take $\mathbf{F} = (-y,\ x,\ 0)$ with $\nabla\times\mathbf{F} = (0,0,2)$ and let
$S$ be the upper hemisphere of radius $R = 1$ about the origin.

(a) Compute $\oint_{\partial S}\mathbf{F}\cdot d\mathbf{l}$ analytically, being
explicit about the boundary orientation induced by the outward normal of the
hemisphere.
(b) Compute $\iint_S(\nabla\times\mathbf{F})\cdot d\mathbf{A}$ analytically, and
confirm equality.
(c) Compute the surface integral numerically on an $n_\theta \times n_\phi$
midpoint grid and report the relative error for $n = 100$ and $n = 400$.
(d) Explain why the surface integral is easier numerically here than in the disk
case of the course demonstration, and identify what property of the integrand
makes the difference.

---

**★★★10.** Uniqueness in the exterior.

State and prove the uniqueness of the exterior Dirichlet problem: let
$\Omega$ be the region outside a closed surface $S$ with
$\nabla^2u = 0$ in $\Omega$, $u = f$ on $S$, and
$u \to 0$ as $\lvert\mathbf{r}\rvert \to \infty$ uniformly.

(a) Set $w = u_1 - u_2$ for two candidate solutions and write down what $w$
satisfies.
(b) Apply Green's first identity on the region bounded by $S$ and a sphere of
radius $R$, take $R \to \infty$, and identify the hypothesis that makes the
surface term at infinity vanish.
(c) Conclude that $\nabla w = \mathbf{0}$ and hence that $u_1 = u_2$.
(d) State whether the same conclusion holds if the regularity hypothesis is
replaced by $u \to c$ for an unknown constant $c$, and justify your answer.
