# Exercises — 01-08-01 First-Order ODEs: Separation of Variables and Integrating Factors

Attempt these **closed-book** before opening the
[solutions](./01-first-order-odes-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Companion lesson: [01 First-Order ODEs](../01-first-order-odes.md).

---

## ★ Foundational

**★1.** Classify each equation as separable, linear, both, or neither. For those
that can be solved by the methods of the lesson, solve them.

(a) $y' = x^{2}y$ (b) $y' + \dfrac{y}{x} = x^{2}$ (c) $y' = y^{2} - x^{2}$
(d) $y' = \dfrac{x+y}{x}$

---

**★2.** A first-order process has rate constant $k = 0.2\ \mathrm{d^{-1}}$, with
$y(0) = y_0$.

(a) Write $y(t)$ and give the relaxation time $\tau$ and the half-life in days.
(b) What fraction remains at $t = 10$ d? Give it as a percentage.
(c) At what time does $y$ differ from its initial value by 1 %?

---

**★3.** Solve $T' = -k(T-T_a)$ with $T(0) = T_0$, $T_a$ constant.

(a) Write the general solution and impose the initial condition.
(b) Show that the time to reduce the *excess* $T-T_a$ to a fraction $f$ of its
initial value is $t = \tau\ln(1/f)$, and evaluate it for $f = 0.2$ and
$\tau = 5$ d.

---

## ★★ Applied

**★★4.** A charcoal sample has a $^{14}\mathrm{C}$ activity 0.42 times that of
the modern reference, and the decay constant is derived from a half-life of
5730 yr.

(a) Compute the age.
(b) The activity ratio is measured to $\pm 1\ \%$. What age uncertainty does
that impose, to first order? Derive the relation rather than quoting it.
(c) The answer depends on the half-life used. Recompute the age with the
conventional Libby half-life of 5568 yr and state the difference.

---

**★★5.** A confined aquifer of length $L$ drained at one end relaxes as
$\exp(-\pi^{2}Tt/4SL^{2})$. Take $T = 2\times10^{-3}\ \mathrm{m^{2}\,s^{-1}}$,
$S = 5\times10^{-4}$ and $L = 2000$ m.

(a) Compute the time constant in days.
(b) Compute the time to reach 95 % of the final head change.
(c) The same aquifer is drained over $L = 1000$ m instead. State the new time
constant and explain the direction of the change physically.

---

**★★6.** A spherical rock of radius 0.5 m is cooled by a wind with heat-transfer
coefficient $h = 10\ \mathrm{W\,m^{-2}\,K^{-1}}$. Its density is
$2700\ \mathrm{kg\,m^{-3}}$, specific heat $900\ \mathrm{J\,kg^{-1}\,K^{-1}}$,
thermal conductivity $2.5\ \mathrm{W\,m^{-1}\,K^{-1}}$.

(a) Show that the lumped cooling rate is $k = 3h/(\rho c r)$ and compute
$\tau = 1/k$ in hours.
(b) Compute the Biot number $\mathrm{Bi} = h(r/3)/k_{\text{cond}}$ and state
whether the lumped model is admissible. Name the criterion you are using.
(c) If the model is not admissible, state what the true cooling behaviour would
look like and why.

---

## ★★★ Research-oriented

**★★★7.** A radionuclide is produced at a constant rate $c$ (atoms per unit
time) and decays with constant $\lambda$, so $\dot N = c - \lambda N$ with
$N(0) = 0$.

(a) Solve the equation and identify the secular-equilibrium value $N_\infty$.
(b) Compute the time to reach 90 % of secular equilibrium, as a multiple of the
half-life, and explain why the answer does not depend on $c$.
(c) A different sample starts with an excess, $N(0) = 3c/\lambda$. Write
$N(t)$ and describe its behaviour qualitatively, including the sign of the
initial slope.

---

**★★★8.** Measure the order of a numerical method rather than asserting it.
Integrate $y' = -\lambda y$, $y(0) = 1$, over $[0,1]$ to obtain $y(1)$ with

(i) explicit Euler and (ii) classical fourth-order Runge–Kutta, for
$h = 0.2, 0.1, 0.05, 0.025$.

(a) For $\lambda = 1$, tabulate the errors against $\exp(-\lambda)$ and report
the observed order for each method.
(b) Repeat with $\lambda = 50$ and the same step sizes. Explain, using
$h\lambda$, why the observed order degrades, and say whether the method has
changed its order.
(c) For $\lambda = 50$, find the largest $h$ in this sequence at which Euler is
stable, and check against the theoretical limit $h\lambda<2$.

---

## Extension ideas

- Solve $y' = (x+y)/x$ by the substitution $v = y/x$ and verify your answer by
  substitution.
- A first-order equation is *exact* if it can be written as the total derivative
  of a function $F(x,y)$. Show that the integrating factor $\mu$ of Section 2.2
  of the lesson is exactly what makes the linear equation exact, and find the
  corresponding $F$.
- Compute how the age uncertainty in ★4(b) grows when the activity ratio
  approaches zero, and explain physically why an almost-undecayed sample has a
  very uncertain age.
