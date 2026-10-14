# Exercises — 01-09-08 Weak Solutions, Variational Forms and Well-Posedness

Attempt these **closed-book** before opening the
[solutions](./08-weak-solutions-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Conventions: the $L^2$ inner product is $\langle u,v\rangle = \int u v\,dx$;
$H^1(0,1)$ is the space of $L^2$ functions with $L^2$ weak derivative, and
$H^1_0$ is its subspace of functions vanishing at the endpoints; the energy norm is
$\lVert v\rVert_E = \lVert v'\rVert_{L^2}$. State the space you use for trial and
test functions in every weak formulation.

---

## ★ Foundational

**★1.** Write the weak formulation of $-u'' + u = f$ on $(0,1)$ with
$u(0) = u(1) = 0$. State which spaces $u$ and $v$ belong to, and say which
boundary condition is essential and which (if any) is natural.

---

**★2.** Show that $u(x) = \lvert x - \tfrac12\rvert$ has a weak derivative in
$L^2(0,1)$, state the derivative, and compute $\lVert u\rVert_{H^1}$.
Say whether $u\in H^1_0(0,1)$ and why.

---

**★3.** For a uniform mesh with spacing $h$, compute $A_{ii} = \int(\varphi_i')^2dx$
and $A_{i,i+1} = \int\varphi_i'\varphi_{i+1}'dx$ for the linear hat functions, and
verify the tridiagonal form of the stiffness matrix quoted in the lesson.

---

**★4.** State the two hypotheses of the Lax–Milgram theorem. Identify which one is
violated by a pure Neumann problem, and give the physical meaning of the failure.
What replaces the theorem's conclusion in that case?

---

## ★★ Applied

**★★5.** Derive the adjoint of $-d^2/dx^2$ on $(0,1)$ subject to the Robin
condition $u'(0) = hu(0)$ at $x = 0$ and $u(1) = 0$ at $x = 1$, including the
boundary terms. State whether the operator is self-adjoint, and what would change
if the boundary condition were replaced by $u(0) = 0$ with $u'(1) = g$.

---

**★★6.** Using the noise-amplification law $\varepsilon/h$ and a truncation error
$\propto h^2$, derive the optimal step $h^{\ast}$ and the resulting minimum error
for $\varepsilon = 10^{-6}$. Verify that the stationary point is a minimum, and
interpret the result as a resolution limit for a derivative-based inversion.

---

**★★7.** Show that the minimiser of the Tikhonov functional
$\lVert Fm - d\rVert^2 + \alpha\lVert m\rVert^2$ is
$m_\alpha = (F^{\mathsf T}F + \alpha I)^{-1}F^{\mathsf T}d$ and, in the
singular-value basis, that mode $n$ is filtered by
$\sigma_n^2/(\sigma_n^2+\alpha)$. Sketch the filter as a function of
$\sigma_n/\sqrt{\alpha}$ and state what happens in the two limits.

---

**★★8.** The Galerkin solution minimises the energy-norm error over the trial
space. For the problem of Section 4.2 of the lesson, verify numerically whether the
energy-norm error of the Galerkin solution is *smaller* than that of the linear
interpolant of the exact solution for $h = 1/41$, and report the two numbers. If
they are equal, explain why — the explanation is a one-dimensional special property
and is worth knowing.

---

## ★★★ Research-oriented

**★★★9.** Implement the finite-element solution of $-(ku')' = 1$ on $(0,1)$ with
$u(0) = u(1) = 0$ and $k = 1$ for $x<0.5$, $k = 10$ for $x>0.5$.

(a) Write down the exact solution (it is quadratic on each half with a kink at
$x = 0.5$) and confirm that $u\in H^1$ but $u\notin H^2$.
(b) Measure the convergence orders in $L^2$ and in the energy norm for a mesh
*aligned* with the interface and for one that is *not*.
(c) Report both sets of orders and explain the difference in terms of the
regularity of the solution and the approximation properties of the trial space.
(d) State the practical rule that follows for meshing a layered medium.

---

**★★★10.** Write a short methods section for a paper that inverts surface
potential-field data for a subsurface density distribution. It must state:

(a) the weak formulation used and why;
(b) the discretisation, with the convergence orders you would demonstrate;
(c) the coercivity or stability argument;
(d) the regularisation and how its parameter was chosen;
(e) the adjoint-consistency test performed;
(f) the resolution limits that follow from the singular spectrum.

Each of the eight lessons of this module should be visible in at least one
sentence.
