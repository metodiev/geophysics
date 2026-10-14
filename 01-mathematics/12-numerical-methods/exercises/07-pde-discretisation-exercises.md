# Exercises — 01-12-07 Discretising PDEs: Consistency, Stability, Convergence

Attempt these **closed-book** before opening the
[solutions](./07-pde-discretisation-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Conventions: the von Neumann substitution is $u_i^n = G^n\mathrm{e}^{\mathrm{i}\theta i}$
with $\theta = k\Delta x$; $r = \kappa\Delta t/\Delta x^{2}$ for the heat
equation and $\sigma = c\Delta t/\Delta x$ for the wave and advection equations.
"Stable" always means $|G(\theta)|\le1$ for all $\theta$, and you should say
which $\theta$ is the worst case rather than assuming it. Work by hand unless a
problem names a code file.

Problems referring to
[`../code/pde_discretisation.py`](../code/pde_discretisation.py) require you to
run it and report its actual output.

---

## ★ Foundational

**★1.** Derive the local truncation error of the FTCS scheme for $u_t = \kappa u_{xx}$.

(a) Expand $u_i^{n+1}$ and the three-point second difference about $(t_n,x_i)$.
(b) State the order in $\Delta t$ and in $\Delta x$ separately.
(c) Use $u_{tt} = \kappa u_{xxxx}$ to show the two terms are comparable when
$\Delta t \sim \Delta x^{2}$, and state what the scheme's observed order would be
if instead $\Delta t$ were held fixed while $\Delta x \to 0$.
(d) State the definition of consistency you are using.

---

**★2.** Show that the leapfrog wave scheme
$u_i^{n+1} = 2u_i^n - u_i^{n-1} + \sigma^{2}(u_{i-1}^n - 2u_i^n + u_{i+1}^n)$
is consistent to second order in both $\Delta x$ and $\Delta t$.

(a) Expand the two time levels about $t_n$.
(b) Expand the spatial stencil and replace the result with $c^{2}u_{xx}$.
(c) State the residual and its order.
(d) Explain why consistency alone does not tell you that the scheme converges.

---

**★3.** A diffusion problem has $\kappa = 10^{-6}\ \mathrm{m^{2}\,s^{-1}}$ and a
grid spacing $\Delta x = 10$ m.

(a) Compute the largest explicit stable step from $r\le\tfrac12$.
(b) Express it in days.
(c) State what happens to the required step if $\Delta x$ is halved, and give the
new value.
(d) State the cost implication of (c) for a two-dimensional grid.

---

**★4.** Carry out the von Neumann analysis of the upwind advection scheme
$u_i^{n+1} = u_i^n - \sigma(u_i^n - u_{i-1}^n)$.

(a) Substitute the Fourier mode and obtain $G$.
(b) Compute $|G|^{2}$ and reduce it to
$1 - 2\sigma(1-\sigma)(1-\cos\theta)$.
(c) Hence derive the CFL condition and state which $\theta$ makes $|G|$ smallest.
(d) State the order of accuracy of the scheme and the price paid for upwinding.

---

## ★★ Applied

**★★5.** Show that forward Euler in time with centred differences in space is
unconditionally unstable for $u_t + cu_x = 0$.

(a) Derive $G = 1 - \mathrm{i}\sigma\sin\theta$ from the mode substitution.
(b) Compute $|G|^{2}$ and show it exceeds 1 for every $\sigma>0$ and every
$\theta \ne 0$.
(c) Evaluate $|G|$ at $\sigma = 0.5$, $\theta = \pi/2$, and at $\sigma = 1.0$,
$\theta = \pi/2$.
(d) Explain why halving $\Delta t$ does not repair the scheme, and state what the
half-measure of adding a small diffusion term does to the order.

---

**★★6.** Obtain the amplification factor of Crank–Nicolson for the heat equation.

(a) Average the spatial operator between time levels and solve for $G(\theta)$.
(b) Show $|G|\le1$ for every $r>0$ and every $\theta$, and identify the limit as
$r\to\infty$ at $\theta = \pi$.
(c) Evaluate $G$ at $\theta = \pi$ for $r = 0.5$ and $r = 5$, and at
$\theta = \pi/2$ for the same two values.
(d) Explain, using §3.3 of the lesson, why $r=5$ is a legitimate step for this
scheme and an impossible one for FTCS, and state what the step costs in work.

---

**★★7.** Derive the Lax–Wendroff scheme for $u_t + cu_x = 0$.

(a) Expand $u^{n+1}$ in time to second order and use the PDE to replace $u_{tt}$.
(b) Show the resulting scheme is
$u_i^{n+1} = u_i^n - \tfrac{\sigma}{2}(u_{i+1}^n - u_{i-1}^n)
+ \tfrac{\sigma^{2}}{2}(u_{i+1}^n - 2u_i^n + u_{i-1}^n)$.
(c) Derive $G$ and show $|G|^{2} = 1 - 4\sigma^{2}(1-\sigma^{2})\sin^{4}(\theta/2)$.
(d) Hence state the stability condition and compare it with the first-order
upwind scheme's, saying what Lax–Wendroff buys and what it costs.

---

**★★8.** A groundwater code integrates a diffusion equation with
$\kappa = 10^{-7}\ \mathrm{m^{2}\,s^{-1}}$ on a grid with $\Delta x = 0.5$ m, at a
step of $\Delta t = 10^{6}$ s (11.57 days).

(a) Compute $r$ and state whether the run is stable.
(b) Give the largest stable $\Delta t$, in seconds and in days.
(c) A colleague halves $\Delta x$ to 0.25 m and keeps $\Delta t = 10^{6}$ s,
arguing that a finer grid is more accurate. Compute the new $r$, state what
happens to the run, and give the largest stable step on the finer grid together
with the factor by which the step must change.
(d) State the diagnostic you would add to the code so that this failure cannot
pass silently, and say why a check on the Courant number of a separate advection
term would not find it.

---

## ★★★ Research-oriented

**★★★9.** Implement the leapfrog wave scheme with a *travelling* initial condition
and measure the effect of the startup.

Use a periodic domain of unit length with $c = 1$,
$u(x,0) = \sin 2\pi x$ and $u_t(x,0) = -2\pi\cos 2\pi x$, so the exact solution is
$u = \sin 2\pi(x-t)$.

(a) At $\sigma = 0.4$, take $n$ steps of size $\Delta t = \sigma/n$ so the run
always ends at $t = 0.4$, and use the second-order Taylor startup
$u^{1} = u^{0} + \Delta t\,g + \tfrac{\Delta t^{2}}{2}c^{2}u_{xx}^{0}$. Report the
maximum error at $n = 20, 40, 80, 160, 320$ and the measured order.
(b) Repeat with the naive startup $u^{1} = u^{0} + \Delta t\,g$. Report the errors,
the measured order, and the ratio of the first-step errors of the two runs.
(c) Measure the amplitude of the spurious (grid-Nyquist) mode,
$\left|\sum_i u_i(-1)^{i}\right|2/n$, in both runs and state whether the startup
excited it.
(d) Perturb the second time level by an alternating checkerboard of amplitude
$10^{-3}$ and measure the final Nyquist amplitude at $\sigma = 0.5$ and at
$\sigma = 1.0$ over 40 steps. State what the two results say about the
computational mode and about $\sigma = 1$ in particular.

---

**★★★10.** A modelling code crashed with a CFL violation after 400 time steps
although the reported Courant number was 0.85.

(a) List the three most likely causes, in order, each with the diagnostic that
would distinguish it from the others.
(b) Explain why a scalar "reported Courant number" can be misleading for a
variable-velocity model, and state the quantity that should be computed instead.
(c) For a scheme with growth $1.327$ per step at 1 per cent above the limit,
compute the number of steps in which round-off ($10^{-16}$) reaches order 1, and
comment on whether a crash at step 400 is consistent with a 1 per cent violation.
(d) State whether the reported 0.85 is consistent with an explicit heat-like
(diffusive) term in the same code, given the $r\le\tfrac12$ condition, and what
that implies about the diagnosis.
