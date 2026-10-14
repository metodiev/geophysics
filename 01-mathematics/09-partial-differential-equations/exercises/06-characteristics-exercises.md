# Exercises — 01-09-06 Method of Characteristics and First-Order PDEs

Attempt these **closed-book** before opening the
[solutions](./06-characteristics-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Conventions: characteristics are parametrised by $s$ or by $t$ (state which); the
conservation law is written $u_t + f(u)_x = 0$; shock speeds come from the
Rankine–Hugoniot condition. State any convention you add.

---

## ★ Foundational

**★1.** Solve $u_t + 3u_x = 0$ with $u(x,0) = \mathrm{e}^{-x^2}$ by
characteristics. State the value of the solution at $x = 10$, $t = 2$, and sketch
the characteristic through that point back to the initial line.

---

**★2.** For $u_t + xu_x = 0$ with $u(x,0) = \sin(\pi x)$:

(a) write the characteristic equations and solve them;
(b) compute the solution at $x = 1$, $t = 1$;
(c) compute the solution at $x = 2$, $t = \ln 2$;
(d) state where the initial feature at $x_0 = 0.5$ ends up after $t = 1$.

---

**★3.** Verify by substitution that $u = f(x-ct)$ solves $u_t + cu_x = 0$ for any
differentiable $f$. State what happens if $f$ has a jump, and whether the solution
remains a classical solution.

---

**★4.** For $u_t + uu_x = 0$ with $u_0(x) = \sin x$ on $[0,2\pi)$:

(a) compute the breaking time $t_s$ from $t_s = -1/\min u_0'$;
(b) state the location at which the shock first forms, and justify the answer from
the characteristic map;
(c) state what happens to the solution beyond $t_s$.

---

## ★★ Applied

**★★5.** For $u_0(x) = 1 - \tanh x$:

(a) compute $t_s$;
(b) compute the solution at $t = 0.4t_s$ at $x = -1$, $x = 0$ and $x = 1$ by
solving the characteristic equation numerically;
(c) comment on the asymmetry of the three values.

---

**★★6.** Derive
$u_x = u_0'(x_0)/(1 + u_0'(x_0)t)$ from the characteristic solution
$x = x_0 + u_0(x_0)t$, $u = u_0(x_0)$. Then show that for $u_0 = \sin x$ the
maximum gradient is $1/(1-t)$ attained at $x = \pi$, and evaluate it at $t = 0.5$,
$0.9$ and $0.99$.

---

**★★7.** For the upwind scheme with $c = 1$, $\Delta x = 0.01$ and $\nu = 0.6$:

(a) compute the numerical diffusion coefficient from
$D_{\text{num}} = (c\Delta x/2)(1-\nu)$;
(b) predict the variance growth rate of a pulse;
(c) state the sign of the error you would make if you omitted the scheme's
diffusion when interpreting a measured spread, and give the error as a percentage
for a run of duration $t = 1$ (in units where $c = 1$).

---

**★★8.** Derive the Rankine–Hugoniot speed $s = (f(u_R)-f(u_L))/(u_R-u_L)$ for
$u_t + f(u)_x = 0$ by integrating the conservation law over a small box straddling
the discontinuity and letting the box shrink to zero. Then compute $s$ for
$f(u) = \tfrac12u^2$ with $u_L = 1$, $u_R = -0.5$, and state the entropy condition
for a convex flux.

---

## ★★★ Research-oriented

**★★★9.** Implement the upwind scheme for $u_t + uu_x = 0$ with $u_0(x) = \sin x$
on $[0,2\pi)$ and measure the maximum gradient at $t = 0.3$, $0.6$ and $0.9$ for
three grids.

(a) Report the measured gradients alongside the exact $1/(1-t)$.
(b) Report how the required grid scales with $t$ to keep the gradient error below a
fixed tolerance, and explain the scaling.
(c) State which part of your result is a numerical artefact, and how you know.
(d) State the limits of your conclusion.

---

**★★★10.** A river reach is modelled with the kinematic wave equation and a
Manning-type flux $q = Ku^{5/3}$.

(a) Derive the kinematic wave speed $c(u) = q'(u)$ and show that the nonlinearity
is convex.
(b) Predict whether a flood hydrograph steepens or spreads as it travels
downstream, and where (in terms of the hydrograph's shape) the steepening begins.
(c) State two physical effects that the kinematic reduction cannot represent.
(d) Describe a field observation that would falsify your prediction, and say what
you would conclude if it contradicted you.
