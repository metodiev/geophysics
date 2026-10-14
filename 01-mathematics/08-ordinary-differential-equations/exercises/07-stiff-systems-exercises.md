# Exercises — 01-08-07 Stiff Systems and Numerical Stability Challenges

Attempt these **closed-book** before opening the
[solutions](./07-stiff-systems-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Companion lesson: [07 Stiff Systems](../07-stiff-systems.md).

---

## ★ Foundational

**★1.** A one-dimensional diffusion problem $u_t = \kappa u_{xx}$ on
$(0,L)$ with $u(0,t) = u(L,t) = 0$ is discretised with the three-point stencil
on $N$ interior nodes, $\kappa = 10^{-6}\ \mathrm{m^{2}\,s^{-1}}$ and $L = 1$ m.

(a) For $N = 100$, $400$ and $1000$, compute $\Delta x$,
$|\lambda|_{\max}\approx4\kappa/\Delta x^{2}$, $|\lambda|_{\min}\approx
\kappa\pi^{2}/L^{2}$, the stiffness ratio $S$, the explicit step limit
$2/|\lambda|_{\max}$, and the number of explicit steps needed to cover one
physical decay time $L^{2}/(\pi^{2}\kappa)$.
(b) State how each of $S$ and the step count scales with $N$, and verify the
scaling against your numbers.

---

**★2.** For the model problem $y' = -\lambda y$ tabulate the amplification
factors $R(z)$, $z = -h\lambda$, of explicit Euler, implicit Euler and the
trapezoidal rule at $z = -0.5,\ -1,\ -2,\ -5,\ -100$, alongside $\exp(z)$.

(a) State the range of $z$ on which explicit Euler is stable.
(b) State which of the three methods are A-stable, and justify from the table.
(c) State which are L-stable, and justify from the behaviour as $z\to-\infty$.

---

**★3.** For each situation state whether the problem is stiff, and give the
ratio that justifies your answer:

(a) a two-box climate model with $\tau_{\text{fast}} = 0.1$ month and
$\tau_{\text{slow}} = 200$ months;
(b) the same model integrated for one month;
(c) a reaction chain with rate constants $10^{6}\ \mathrm{s^{-1}}$ and
$1\ \mathrm{s^{-1}}$, integrated over 10 s;
(d) a reaction chain with the same rates, integrated over $10^{-5}$ s.

---

## ★★ Applied

**★★4.** A confined aquifer with transmissivity $T = 10^{-2}\ \mathrm{m^{2}\,s^{-1}}$
and storativity $S = 10^{-3}$ has hydraulic diffusivity $D = T/S = 10\ \mathrm{m^{2}\,s^{-1}}$.
It is modelled on a square domain of side 4000 m with $u = 0$ on the boundary,
so the three-point stencil gives $\lambda_{\max}\approx4D/\Delta x^{2}$ and
$\lambda_{\min}\approx2D\pi^{2}/L^{2}$ (the factor 2 is the two-dimensional
Laplacian's).

(a) For $\Delta x = 100$ m, 25 m and 6.25 m compute $\lambda_{\max}$,
$\lambda_{\min}$, the stiffness ratio, the explicit step limit
$2/\lambda_{\max}$, the number of explicit steps per physical decay time
$1/\lambda_{\min}$, and the resulting number of grid-node updates
(steps $\times$ nodes).
(b) Show from your table that the cost per physical decay time scales as
$\Delta x^{-4}$, and explain the two exponents that multiply (steps $\propto
\Delta x^{-2}$, nodes $\propto\Delta x^{-2}$).
(c) An implicit scheme with $\Delta t = 0.1$ d needs only about ten steps per
decay time, but each step requires a sparse solve. Compare the *node-update*
counts and state for which grid the explicit scheme ceases to be competitive,
given that a good implicit solve costs roughly $10^{2}$–$10^{3}$
node-operations per unknown.
(d) State why the answer to (c) does not mean the implicit answer is *accurate*,
and name the check you would perform.

---

**★★5.** Take $\lambda = 1000$, $h = 1$ ($h\lambda = 1000$) and step
$y' = -\lambda y$ from $y(0) = 1$.

(a) Compute $R$ for the trapezoidal rule and for implicit Euler.
(b) Compute the numerical value after 1, 10, 50 and 100 steps for both, and
compare with $\exp(-1000n)$.
(c) State which method you would recommend for this problem and why, given that
the trapezoidal rule is second order and implicit Euler first order. Name the
property that decides it.

---

**★★6.** For $y' = -10y^{3}$, $y(0) = 1$:

(a) Solve the ODE exactly (it is separable) and evaluate $y(1)$.
(b) Write the implicit Euler step as a polynomial equation for $y_{n+1}$ with
$h = 0.1$ and show that it is a cubic.
(c) Compute the Newton iteration for the first step and report the number of
iterations required for $10^{-12}$ accuracy. Compare with $y_1$ from the exact
solution of the *step*, which is the root of the cubic.
(d) Repeat with explicit Euler and explain the failure mode. Its character is
different from the linear case — state how.

---

## ★★★ Research-oriented

**★★★7.** The Robertson system is

$$\dot y_1 = -k_1y_1+k_3y_2y_3, \quad
\dot y_2 = k_1y_1-k_3y_2y_3-k_2y_2^{2}, \quad
\dot y_3 = k_2y_2^{2},$$

with $k_1 = 0.04$, $k_2 = 3\times10^{7}$, $k_3 = 10^{4}$ and
$\mathbf{y}(0) = (1,0,0)$.

(a) Write the Jacobian and identify which entries produce the fast timescale.
(b) Using the reported solution at $t = 40$, $y_2 \approx 9.2\times10^{-6}$, and
$y_3 \approx 0.284$, estimate the largest-magnitude eigenvalue of the Jacobian
and hence the stiffness ratio against the slow rate $k_1 = 0.04$.
(c) From your estimate, compute the largest step explicit Euler could take at
that time, and compare with the 4000-step run of the lesson ($h = 0.01$).
(d) State in two sentences why the *slow* dynamics at $t = 40$ can be computed
with $h = 0.1$ by an implicit method but not by an explicit one, given that
both are first order.

---

**★★★8.** You must integrate the three-dimensional heat equation on a cubic
domain of side 1000 m with $\kappa = 10^{-6}\ \mathrm{m^{2}\,s^{-1}}$, and you
need the field over one physical decay time
$\tau = 1/\left[3\kappa\pi^{2}/L^{2}\right]$. For a seven-point Laplacian with
cubic cells, $\lambda_{\max}\approx12\kappa/\Delta x^{2}$.

| $\Delta x$ (m) | $N$ | nodes | $\Delta t_{\max}$ (s) | steps per $\tau$ | node-updates per $\tau$ |
|---|---|---|---|---|---|
| 20 | 50 | $1.25\times10^{5}$ | $6.67\times10^{7}$ | 507 | $6.3\times10^{7}$ |
| 10 | 100 | $1.0\times10^{6}$ | $1.67\times10^{7}$ | 2025 | $2.0\times10^{9}$ |
| 5 | 200 | $8.0\times10^{6}$ | $4.17\times10^{6}$ | 8100 | $6.5\times10^{10}$ |
| 2.5 | 400 | $6.4\times10^{7}$ | $1.04\times10^{6}$ | 32400 | $2.1\times10^{12}$ |

(a) Verify the table's arithmetic for $N = 100$ and $N = 400$ from
$\lambda_{\max}$, $\lambda_{\min} = 3\kappa\pi^{2}/L^{2}$, and the definitions of
$\Delta t_{\max}$ and the node-update count.
(b) Determine the exponent $p$ in "cost per decay time $\propto\Delta x^{-p}$"
and justify it from the grid dimension.
(c) **Assuming** (as a stipulated machine property, not a measured one) that the
code performs $10^{8}$ grid-node updates per second, convert the four
node-update counts into run times and state the finest grid that fits inside a
one-hour budget.
(d) Choose between (i) explicit Euler, (ii) backward Euler with a multigrid
solve, (iii) Crank–Nicolson with the same solve, and (iv) an IMEX scheme.
Justify each choice or rejection with a number or a named property.
(e) State which of the four you would reject on *accuracy* grounds rather than
on stability grounds, and why.
(f) State the single calculation you would do first, before writing any code,
and what it would tell you.

---

## Extension ideas

- Derive $R(z)$ for the second-order backward differentiation formula (BDF2),
  $(3y_{n+1}-4y_n+y_{n-1})/(2h) = f_{n+1}$, and show that $|R(z)|\to0$ as
  $z\to-\infty$ but only as $|z|^{-1/2}$. Compute $|R|$ at $z = -1$, $-10$,
  $-1000$ and compare with implicit Euler.
- Show that the trapezoidal rule is A-stable by proving
  $|R(iy)| = 1$ for all $y$ and $|R(z)|<1$ for $\operatorname{Re}z<0$.
- For the diffusion problem of ★1, determine the largest $\Delta t$ for which
  accuracy (not stability) is adequate in the sense that the fundamental mode is
  resolved with at least 20 time steps per decay time, and compare with the
  implicit stability-driven step of ★4.
