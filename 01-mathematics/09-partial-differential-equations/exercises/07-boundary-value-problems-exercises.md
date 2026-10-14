# Exercises — 01-09-07 Boundary and Initial-Boundary Value Problems

Attempt these **closed-book** before opening the
[solutions](./07-boundary-value-problems-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Conventions: $\kappa$ is a diffusivity in $\mathrm{m^2\,s^{-1}}$; a *condition* at
a boundary means one scalar relation at that boundary point; $n$ is the outward
normal. State the class of the equation before counting conditions. Use
$\kappa = 1$, $L = 1$ where a numerical value of the amplification is requested
(so that the eigenvalues are $n^2\pi^2$).

---

## ★ Foundational

**★1.** State Hadamard's three conditions and say which is violated by the backward
heat problem. Give the amplification factor for mode $n = 8$ at $t = 0.1$ with
$\kappa = 1$ and $L = 1$, and say what that implies for a data error of $10^{-6}$.

---

**★2.** Count the boundary and initial conditions required for:

(a) $\nabla^2V = 0$ on a disc;
(b) $u_t = \kappa u_{xx}$ on a rod $0<x<L$;
(c) $u_{tt} = c^2u_{xx}$ on a string $0<x<L$;
(d) $u_t + cu_x = 0$ on $0<x<L$ (transport with $c>0$).

Justify each count from the characteristics, and state *where* the conditions go.

---

**★3.** Write the energy identity for the heat equation with homogeneous Robin data
$u_x(0,t) = hu(0,t)$ and $u(L,t) = 0$, and show that $\int w^2\,dx$ still decays for
the difference $w$ of two solutions. State whether the decay is faster or slower
than with homogeneous Neumann data at $x = 0$, and why.

---

**★4.** A rod has $u(x,0) = 1$ everywhere, $u(0,t) = 0$ and $u(L,t) = 0$.

(a) State the compatibility failure at the corners.
(b) Describe qualitatively what the exact solution does at $(0,0)$ and immediately
afterwards.
(c) State two defensible responses to the failure.

---

## ★★ Applied

**★★5.** Derive the ghost-node update for the Robin condition
$-u_x(L,t) = h\left(u(L,t) - u_\infty\right)$ on a uniform grid with spacing
$\Delta x$, and show that the resulting discrete boundary condition is second-order
accurate. State what degrades to first order if a one-sided difference is used
instead.

---

**★★6.** Duhamel's principle: write the solution of
$u_t = \kappa u_{xx} + f(x,t)$ with zero initial and boundary data as an integral
over the source history, state what the kernel is, and explain in one sentence why
the principle is the continuous analogue of adding up impulses in a linear system.

---

**★★7.** A first-order absorbing boundary leaves a reflection coefficient of
$10^{-3}$.

(a) Compute the amplitude of the residual after ten round trips.
(b) Compare it with the reflection from a physical interface with a 10 % impedance
contrast.
(c) State, with a number, the weakest physical reflection that this boundary
condition could resolve confidently, and hence when a higher-order absorbing
condition is required.

---

**★★8.** The backward heat problem is made well posed by discarding all modes above
a cutoff $n_c$, which bounds the amplification by $\exp(\kappa n_c^2\pi^2t)$.

(a) Choose $n_c$ so that a data error of $10^{-6}$ is amplified by at most $10^{3}$
for $\kappa = 1$, $L = 1$, $t = 0.05$.
(b) State what has been given up to achieve the bound.
(c) Explain why this is regularisation rather than a solution of the original
problem.

---

## ★★★ Research-oriented

**★★★9.** Implement the heat equation with (a) Dirichlet and (b) Robin boundary
conditions at both ends, starting from the same initial condition.

(a) Measure the decay of the first mode in each case.
(b) Compare the measured rates with the eigenvalues you predict analytically.
(c) Explain the difference physically.
(d) State the limits of the comparison, including what happens when the two
problems' initial conditions excite different mixtures of modes.

---

**★★★10.** A numerical model of a reservoir is run for 30 years of simulation and
then inverted for a change in rock properties between two surveys.

Write a short design note that covers:

(a) which boundary conditions must be identical between the two runs, and why;
(b) why an absorbing boundary is not appropriate for the ground surface;
(c) what regularisation you would apply to the time-lapse inversion and how you
would choose its parameter;
(d) one diagnostic that would detect a boundary-condition inconsistency between the
two runs before the inversion is attempted.
