# Exercises — 01-02-04 Polynomials, Roots and Asymptotic Behaviour

Attempt these **closed-book** before opening the
[solutions](./04-polynomials-roots-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Write down the residual check for every root you find.

---

## ★ Foundational

**★1.** For $p(x) = x^{3} - 6x^{2} + 11x - 6$:

(a) state the degree and the leading coefficient;

(b) state the end behaviour as $x \to \pm\infty$;

(c) evaluate $p$ at $x = 0, 1, 2, 3, 4$;

(d) from (c), state the roots, and check the sign pattern between them.

---

**★2.** Evaluate $p(x) = 2x^{4} - 3x^{3} + x - 5$ at $x = 2$.

(a) By expanding the powers directly.

(b) By Horner's rule, showing each nested step.

(c) State how many multiplications each method needs.

---

**★3.** Show that $x^{3} - 3x + 2 = (x-1)^{2}(x+2)$.

(a) State the roots with their multiplicities.

(b) Describe what the graph does at each root: cross, touch, or both.

(c) Predict how a small perturbation of the coefficients will affect the root at
$x = 1$ compared with the root at $x = -2$, and say which derivative you used to
decide.

---

**★4.** Give the end behaviour (as $x \to +\infty$ and $x \to -\infty$) of:

(a) $x^{3} - 3x + 2$
(b) $x^{4} - x^{2} + 1$
(c) $-2x^{3} + x$
(d) $x^{2} + x$

---

## ★★ Applied

**★★5.** For $p(x) = x^{3} - x - 2$ on the bracket $[1, 2]$:

(a) Verify that the bracket contains a root.

(b) Compute the number of bisection iterations needed so that the half-width of
the bracket is below $10^{-3}$, using the bound $(b-a)/2^{n}$, and state the
resulting approximation.

(c) Repeat for a half-width below $10^{-6}$.

(d) State the advantage and the disadvantage of bisection relative to Newton's
method for this problem.

---

**★★6.** Let $p(x) = (x-1)^{2}(x+3)$, which has a double root at $x=1$.

(a) Compute five Newton iterations from $x_0 = 2$, tabulating $x_k$ and
$|x_k - 1|$.

(b) Compute the ratios $|e_k|/|e_{k-1}|$ and state the limit they approach.

(c) Relate the limit to the multiplicity of the root, and state what it would be
for a triple root.

(d) Contrast the number of iterations with the four iterations needed for the
simple root of $x^{3}-x-2$ in the lesson, and state the practical consequence for
an inversion code whose misfit surface is nearly flat in one direction.

---

**★★7.** For $p(x) = x^{3} - 3x + 2$, consider the root at $x = -2$.

(a) Compute $p'(-2)$.

(b) Use $\delta r = -\delta a_k\,r^{k}/p'(r)$ to predict the shift of that root
when the constant term changes from $+2$ to $2 + 10^{-3}$.

(c) Verify your prediction by finding the shifted root numerically (bisection or
Newton on the perturbed polynomial).

(d) State the amplification factor and say which property of the root controls it.

---

**★★8.** The profile of a buried point mass is
$g(x) = GMh/(x^{2}+h^{2})^{3/2}$.

(a) Show that $\dfrac{g(x)x^{3}}{GMh} = \left(1 + h^{2}/x^{2}\right)^{-3/2}$.

(b) Compute that ratio at $x/h = 2, 5, 10, 20$ and report the far-field error
$1 - \text{ratio}$ in each case.

(c) Find the value of $x/h$ at which the far-field error falls below $0.1\%$, both
by solving the inequality and by bracketing numerically.

(d) A colleague uses the $1/x^{3}$ form at $x/h = 3$ to estimate a mass. Estimate
the error they make in the mass and state the direction of the bias.

---

## ★★★ Research-oriented

**★★★9.** Root separation controls conditioning, not the solver.

Consider $p_\epsilon(x) = x^{2} - (2+\epsilon)x + (1+\epsilon)$, whose roots are
$x = 1$ and $x = 1+\epsilon$. Suppose the constant coefficient is known only to a
relative accuracy $\rho$: what you actually have is
$x^{2} - (2+\epsilon)x + (1+\epsilon)(1+\rho)$.

(a) Show that $p_\epsilon'$ evaluated at the upper root equals $\epsilon$, and
hence that the error in the constant coefficient, $\delta c = (1+\epsilon)\rho$,
shifts that root by

$$\delta r \approx -\frac{\delta c}{p'(r)} = -\frac{(1+\epsilon)\rho}{\epsilon}.$$

State the amplification factor and how it behaves as $\epsilon \to 0$.

(b) With $\rho = 10^{-10}$, compute the predicted and the measured shift of the
upper root for $\epsilon = 10^{-1}, 10^{-2}, 10^{-3}, 10^{-4}$. Perform the
calculation in high precision (at least 30 significant digits — `decimal` is
enough) so that you measure the *conditioning* and not the floating-point noise of
the quadratic formula. Tabulate the shift and the ratio $\delta r/\epsilon$.

(c) Show that the discriminant of the perturbed quadratic is
$\epsilon^{2} - 4(1+\epsilon)\rho$ and hence that the two roots stop being
resolvable — the perturbed polynomial has no real roots at all — once
$\epsilon < 2\sqrt{\rho}$. Verify this threshold numerically.

(d) Check that Newton's method, started at $x_0 = 1 + 2\epsilon$ with the *exact*
coefficients, still converges in 5–6 iterations for every $\epsilon$ in your
table. State what this demonstrates about the difference between a solver's speed
and a problem's conditioning.

(e) Report the method, the results, the trend and the limits of your conclusion,
including what changes if the perturbation is applied to the coefficient of $x$
instead of the constant term.

**★★★10.** The Taylor polynomial $T_n(x) = \sum_{k=0}^{n}(-x)^{k}/k!$ approximates
$e^{-x}$.

(a) For $n = 2, 4, 6, 8$, find the largest $x$ for which the relative error of
$T_n(x)$ is below $1\%$ (solve by bisection).

(b) Tabulate the range against the degree $n$, and state whether the growth is
linear, quadratic or faster in $n$.

(c) Explain, using the ratio of successive terms of the series, why the range
grows the way it does rather than saturating at a constant.

(d) Report one consequence for a geophysical model that is linearised by
truncating a series (for example a small-parameter ray expansion or a linearised
inverse problem), and state what a validation test should therefore include.

---

## Extension ideas

- Implement the secant method (Newton's method with a finite-difference derivative)
  and compare iterations and cost with Newton and with bisection on the same cubic.
- Take a real or synthetic well log, fit polynomials of degree 1, 2, 3 and 4 over
  the same interval, and plot (by table) the residuals. At which degree does the
  fit start to oscillate rather than improve?
- Find the half-width of the anomaly of an infinite horizontal cylinder,
  $g(x) \propto h/(x^{2}+h^{2})$, and compare the depth you would infer using the
  sphere rule $h = 1.304766\,x_{1/2}$. Report the percentage bias.
