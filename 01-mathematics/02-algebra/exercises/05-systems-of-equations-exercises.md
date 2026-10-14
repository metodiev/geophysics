# Exercises — 01-02-05 Linear and Nonlinear Systems of Equations

Attempt these **closed-book** before opening the
[solutions](./05-systems-of-equations-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Check every linear solution with the residual, and state the starting point of
every nonlinear one.

---

## ★ Foundational

**★1.** Solve by substitution, then check both equations:

$$2x + y = 7, \qquad x - y = 2.$$

---

**★2.** Solve by Gaussian elimination with partial pivoting, showing the
elimination steps and the back-substitution:

$$\begin{pmatrix} 2 & 1 & -1 \\ -3 & -1 & 2 \\ -2 & 1 & 2 \end{pmatrix}
\mathbf{x} = \begin{pmatrix} 8 \\ -11 \\ -3 \end{pmatrix}.$$

Report the maximum residual $\|A\mathbf{x} - \mathbf{b}\|_\infty$.

---

**★3.** Classify each system as linear or nonlinear, and as exactly determined,
over-determined or under-determined. State, without solving, whether it can have
(a) no solution, (b) a unique solution, (c) infinitely many.

(i) $2x + y = 7$, $x - y = 2$
(ii) $x^{2} + y^{2} = 25$, $x - y = 1$
(iii) $x + y = 1$, $2x + 2y = 2$
(iv) $x + y = 1$, $2x + 2y = 3$
(v) $x + y + z = 6$, $x - y = 0$
(vi) $x + y = 5$, $x - y = 1$, $2x + y = 8$

---

**★4.** For the system

$$x + 2y = 3, \qquad 2x + 4y = c,$$

compute the determinant of the coefficient matrix, and describe the solution set
for $c = 6$ and for $c = 7$. For the solvable case, write the general solution in
terms of a free parameter.

---

## ★★ Applied

**★★5.** For the coefficient matrix

$$A = \begin{pmatrix} 1 & 1+\epsilon \\ 1 & 1-\epsilon \end{pmatrix},$$

with $\epsilon = 10^{-6}$:

(a) compute $\det A$ as a function of $\epsilon$;

(b) solve $A\mathbf{x} = (2,2)$ exactly;

(c) solve $A\mathbf{x} = (2 + 10^{-6},\, 2)$ exactly;

(d) report the change in the solution and the amplification factor relative to the
relative data change, and compare with the $\epsilon = 10^{-8}$ case from the
lesson ($\mathbf{x}$ moves from $(2,0)$ to $(1.5,0.5)$);

(e) state, in one sentence, what this means for an inversion whose forward matrix
has nearly parallel rows.

---

**★★6.** Consider the nonlinear system

$$x^{2} + y^{2} = 25, \qquad x - y = 1.$$

(a) Solve it algebraically and state both solutions exactly.

(b) Write the Jacobian.

(c) Starting from $(5, 4)$, perform Newton iterations and tabulate
$(x_k, y_k)$ and the maximum absolute residual. Report the number needed to reach
a residual below $10^{-14}$.

(d) Repeat from $(-5, -4)$ and report which solution is found.

(e) Evaluate the Jacobian at $(0,0)$ and explain what a Newton iteration started
there would do.

(f) State what (c)–(e) demonstrate about nonlinear systems that linear systems do
not share.

---

**★★7.** For a point mass at horizontal position $p = 0$ and depth $h$, the
vertical attraction at offset $x$ is

$$g(x) = \frac{GMh}{\left(x^{2}+h^{2}\right)^{3/2}}.$$

(a) Write the two partial derivatives

$$\frac{\partial g}{\partial M} = \frac{Gh}{\left(x^{2}+h^{2}\right)^{3/2}},
\qquad
\frac{\partial g}{\partial h} = \frac{GM\left(x^{2}-2h^{2}\right)}
{\left(x^{2}+h^{2}\right)^{5/2}},$$

and show that the second expression follows by differentiating the first form.

(b) Evaluate all four entries of the $2\times2$ Jacobian for stations at
$x = -300$ m and $x = +400$ m, at the true model $M = 5\times10^{11}$ kg,
$h = 350$ m.

(c) Compute $\kappa_\infty(J)$ and state what it means physically for the pair
$(M, h)$.

(d) Note that $\partial g/\partial M$ does not depend on $M$. State the structural
consequence: which part of the problem is linear, and which is not?

---

**★★8.** For the point-mass inversion with stations at $x_1 = -300$ m and
$x_2 = +400$ m, the two readings give a ratio
$r = (g_1/g_2)^{2/3} = 1.3294117647$.

(a) Use $h^{2} = \left[(x_2-p)^{2} - r(x_1-p)^{2}\right]/(r-1)$ to compute the
depth, and then $M = g_1\left[(x_1-p)^{2}+h^{2}\right]^{3/2}/(Gh)$ to compute the
mass, for $p = 0$ and $p = -100$ m.

(b) Verify that both models reproduce $g_1$ and $g_2$ to round-off.

(c) Comment on the direction of the trade-off: as the assumed position moves away
from the true one, what happens to the fitted mass and depth?

---

## ★★★ Research-oriented

**★★★9.** The region of convergence of a nonlinear inversion.

For the two-parameter model of Section 5 of the lesson (one point mass at a fixed
position $p = 0$, stations at $x = -300$ m and $x = +400$ m, true model
$M = 5\times10^{11}$ kg and $h = 350$ m):

(a) Implement Gauss–Newton with a backtracking line search on the log-scaled
parameters $\ln(M/10^{11})$ and $\ln(h/100)$, stopping when the maximum absolute
residual falls below $10^{-14}$.

(b) Run it from a grid of starting guesses spanning factors of $0.05$ to $20$ in
mass and $0.1$ to $10$ in depth. Count how many converge to the true model (within
$10^{-6}$ relative in both parameters) and list any that do not.

(c) Report the failure mode of any non-converging start: does it diverge, oscillate
or converge to a different model?

(d) Report the method, the measured success rate, the boundary of the region you
found, and the limits of your conclusion (in particular, that the basin depends on
the data magnitudes, the stations and the parameterisation chosen).

(e) Explain in two sentences why the existence of a large basin does **not** imply
that the parameters are well determined.

---

**★★★10.** A third station breaks the non-uniqueness. Using the same family as
★★8 (positions $p = 0, -60, -150, -250$ m, each with its fitted mass and depth):

(a) Compute each family member's predicted reading at a **third** station placed
at $x = 800$ m, and report the relative deviation from the true model's reading
(which is $1.7541409\times10^{-5}$ m/s²).

(b) Repeat at $x = 1500$ m (true reading $3.1960600\times10^{-6}$ m/s²).

(c) Tabulate the deviations and state which station separates the family more
sharply, and why the deviation grows with the assumed position offset.

(d) State what this result implies about the design of a survey intended to
resolve a source position, and what it implies about the minimum number of
stations needed for a three-parameter source model.

(e) Report the method, the numbers, the trend and the limits of your conclusion
(the deviations are exact-model differences with no noise; add a sentence on what
measurement uncertainty would do to the discrimination).

---

## Extension ideas

- Implement Gaussian elimination **without** partial pivoting and compare the
  residuals and solutions on the nearly singular system of ★★5 and on the
  Hilbert-matrix systems of lesson 01-01-05.
- Solve the two-loop mixing problem for a borehole: two water samples with known
  chloride concentrations and temperatures mix to a measured concentration and
  temperature; solve for the mixing fractions, and check whether the system is
  well conditioned for realistic contrasts.
- Add a third unknown to the point-mass model (the horizontal position) and show
  numerically that Gauss–Newton converges to *some* member of the family depending
  on the starting guess. Report the family member found from three different
  starting positions.
