# Exercises — 01-02-01 Algebraic Manipulation and Solving Equations

Attempt these **closed-book**, on paper, before opening the
[solutions](./01-algebraic-manipulation-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Every physical answer needs units. Every solution needs a substitution check.

---

## ★ Foundational

**★1.** Solve for $v$:

$$\frac{1}{v} = \frac{1}{v_1} + \frac{1}{v_2}.$$

State the conditions under which your rearrangement is valid.

---

**★2.** The geothermal profile of a conductive crust is $T(z) = T_0 + \gamma z$.

(a) Solve for $z$.

(b) Solve for $\gamma$.

(c) Evaluate $z$ for $T = 135.0\,^\circ$C, $T_0 = 10.0\,^\circ$C,
$\gamma = 25.0\,^\circ$C/km.

(d) Evaluate $\gamma$ for $z = 3.5$ km, $T = 95.0\,^\circ$C,
$T_0 = 10.0\,^\circ$C. Comment on what the value means physically.

---

**★3.** Solve by factorisation *and* by the quadratic formula, and check:

(a) $x^{2} - 3x + 2 = 0$

(b) $x^{2} - 6x + 9 = 0$

(c) For (b), state the value of the discriminant and what it implies.

---

**★4.** The hydrostatic relation is $P = \rho g h$.

(a) Solve for $h$.

(b) Evaluate $h$ for $P = 1.0\times10^{7}$ Pa, $\rho = 1000\ \mathrm{kg\,m^{-3}}$,
$g = 9.81\ \mathrm{m\,s^{-2}}$.

(c) Check the dimensions of your expression for $h$.

(d) What does the formula predict for $\rho = 0$? Is that physically meaningful?

---

## ★★ Applied

**★★5.** Solve $\sqrt{2x + 3} = x$. Show your candidate solutions, then check
each in the **original** equation, and state which is genuine.

---

**★★6.** Radioactive decay follows $N(t) = N_0 e^{-\lambda t}$ with
$\lambda = \ln 2 / T_{1/2}$.

(a) Solve for $t$ in terms of $N/N_0$ and $\lambda$.

(b) Evaluate $t$ for $N_0/N = 4$ and $T_{1/2} = 5730$ yr.

(c) Without further calculation, explain why your answer in (b) must be a whole
number of half-lives, and state how many.

---

**★★7.** In a two-layer refraction survey the crossover distance is

$$x_c = 2H\sqrt{\frac{v_2 + v_1}{v_2 - v_1}}.$$

(a) Solve for $H$.

(b) Evaluate $H$ for $v_1 = 1500$ m/s, $v_2 = 4000$ m/s, $x_c = 120$ m.

(c) Solve the same relation for the ratio $v_2/v_1$ (keep $H$ and $x_c$ as
symbols), and state any condition your expression needs.

(d) The critical angle satisfies $\sin\theta_c = v_1/v_2$. Compute $\theta_c$ for
the values in (b).

---

**★★8.** Two travel-time picks from a refraction line are
$(x_1, t_1) = (100\ \mathrm{m}, 0.100\ \mathrm{s})$ and
$(x_2, t_2) = (400\ \mathrm{m}, 0.180\ \mathrm{s})$, with
$t = a + bx$.

(a) Write the two equations and solve them by substitution for $a$ and $b$.

(b) Interpret $b$ physically, and compute the corresponding velocity $v_2 = 1/b$.

(c) State the units of $a$ and $b$ and check that they are consistent with the
equation.

---

## ★★★ Research-oriented

**★★★9.** Consider the quadratic $x^{2} - (2-\delta)x + (1-\delta) = 0$, whose
roots are $x = 1$ and $x = 1-\delta$.

(a) Verify the roots by expansion.

(b) For $\delta \in \{10^{-3}, 10^{-6}, 10^{-7}, 10^{-8}, 10^{-9}\}$, compute the
smaller root with the naive formula $x = (-b - \sqrt{b^{2}-4ac})/(2a)$ and report
the relative error against the exact value $1-\delta$.

(c) Report what happens at $\delta = 10^{-9}$ and explain it in terms of
floating-point subtraction (lesson 01-01-04).

(d) Obtain the same root from the product of the roots, $x_1x_2 = c/a$, and
report its error.

(e) State the threshold value of $\delta$ below which the naive route fails, and
relate it to $u = 2^{-53}$ and to $\sqrt{u}$. Report the method, the measurements
and the limits of your conclusion.

---

**★★★10.** A diffusion coefficient follows
$D(T) = D_0\exp(-E_a/(RT))$ with **ILLUSTRATIVE** constants
$D_0 = 1.0\times10^{-6}\ \mathrm{m^{2}\,s^{-1}}$,
$E_a = 2.0\times10^{5}$ J/mol, $R = 8.31446261815324$ J/(mol K).

(a) Solve analytically for the temperature at which
$D = 1.0\times10^{-18}\ \mathrm{m^{2}\,s^{-1}}$.

(b) Solve the same problem numerically by bisection on
$g(T) = \ln D(T) - \ln D_{\text{target}}$ over the bracket $[300, 2000]$ K.
Report the number of iterations needed for $|T - T_{\text{exact}}| < 10^{-9}$ K
and confirm that the bracket is valid.

(c) Explain in three sentences when the numerical route is preferable, given that
the closed form exists.

(d) State one way in which the answer depends on the constants and one way in
which it does not (for example, by re-solving with $E_a$ doubled and reporting the
change).

---

## Extension ideas

- Take one equation from your own field, rearrange it for each symbol in turn, and
  write down the units of each result. Any symbol for which the units come out
  wrong is a sign error.
- The time-average equation for a layered medium is
  $\bar v = \left(\sum_i h_i\right) / \left(\sum_i h_i/v_i\right)$. Solve for
  $h_n$ given all other thicknesses and the average velocity.
- Find a formula in a textbook that is written in a form with the unknown in a
  denominator, and rewrite it so that the unknown is in the numerator. Explain
  why the rewritten form is safer to evaluate near the singular point.
