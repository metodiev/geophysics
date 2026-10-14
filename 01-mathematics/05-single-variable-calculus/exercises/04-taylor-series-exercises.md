# Exercises — 01-05-04 Taylor Series, Linearisation and Small-Angle Approximations

Attempt these **closed-book** before opening the
[solutions](./04-taylor-series-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

---

## ★ Foundational

**★1.** Write the Maclaurin series to four nonzero terms and state the radius of
convergence:

(a) $e^{-x}$ (b) $\cos(2x)$ (c) $\ln(1+x)$ (d) $(1+x)^{-1}$

---

**★2.** Use the linearisation about $x = 0$ to estimate (i) $\sqrt{1.02}$ and
(ii) $\sin(0.05)$. For each, bound the error with the Lagrange remainder and compare
your bound with the true error (use a calculator for the true values).

---

**★3.** State the relative error of each approximation, in terms of the stated
variable, and the value of the variable at which the error reaches 1 %:

(a) $\sin\theta \approx \theta$
(b) $\cos\theta \approx 1 - \theta^{2}/2$
(c) $e^{-x} \approx 1 - x$
(d) $(1+u)^{-2} \approx 1 - 2u$

---

## ★★ Applied

**★★4.** A gravity anomaly of a point mass of $10^{10}$ kg is measured at
$d = 500$ m with a relative precision of $10^{-3}$.

(a) Using $\delta g \approx -2g\,\delta d/d$, what uncertainty in $d$ does that
precision support?
(b) Using the result of the lesson's Section 3.7, at what perturbation
$u = \delta d/d$ does the linearisation error itself reach $10^{-3}$?
(c) Compare (a) and (b). Is a linearised inversion with $u = 0.05$ consistent with
the data precision? State the conclusion in one sentence about *model* perturbation
versus *data* precision.

---

**★★5.** A wave travels a distance $L$ through a medium whose speed increases
linearly along the path: $v(s) = v_0 + \alpha s$.

(a) Write the travel time as an integral and expand $1/v(s)$ to first order in
$\alpha s/v_0$.
(b) Evaluate the integral to first order and identify the correction to the
straight-ray time $L/v_0$.
(c) State the dimensionless expansion parameter and the condition under which the
first-order result is accurate to 1 %.

---

## ★★★ Research-oriented

**★★★6.** The parabolic normal-moveout equation of the lesson,

$$t(x) \approx t_0 + \frac{x^{2}}{2v^{2}t_0},$$

is the truncation of $t = t_0\sqrt{1+u}$, $u = (x/(vt_0))^{2}$, after the term
linear in $u$.

(a) Carry the expansion to order $u^{2}$ and write the resulting $x^{4}$ correction.
(b) Using the exact bracket of the lesson's Section 3.6, compute the offset at which
the parabolic approximation is wrong by 1 % for $v = 2000$ m/s and $t_0 = 1$ s.
(c) Check your answer against the lesson's table and against the 1 % crossover you
can read off the table, and reconcile any difference.
(d) State the limitation of your conclusion: why does the 1 % offset scale with
$v t_0$ rather than with $v$ or $t_0$ separately?

---

**★★★7.** A thermal expansion relation is linearised as
$\rho(T) \approx \rho_0[1 - \alpha(T-T_0)]$ with
$\alpha \approx 3\times10^{-5}\ \mathrm{K^{-1}}$ and $\rho_0 = 2700\ \mathrm{kg\,m^{-3}}$.

(a) Using the binomial/Taylor machinery, write the second-order term and show that it
is negligible for $\lvert T-T_0\rvert = 100$ K.
(b) Compute the density change for $\lvert T-T_0\rvert = 100$ K at first and second
order, and the relative difference between them.
(c) The relation fails physically long before it fails numerically. State two
physical reasons why a linear thermal expansion cannot be applied over 1000 K, even
though the arithmetic is fine.

---

## Extension ideas

- Derive the Maclaurin series of $\tan x$ to three nonzero terms by dividing the
  series for $\sin x$ by that for $\cos x$, and verify the leading coefficient
  against the lesson's threshold for $\tan(x)/x$.
- Expand the gravitational potential of a point mass at height $z$ about the surface
  to third order and identify the term that would produce an error of $10^{-9}$ in
  mGal at $z = 10$ km.
- Use the ratio test to confirm the radii of convergence of ★1(c) and ★1(d)
  directly from the coefficients.
