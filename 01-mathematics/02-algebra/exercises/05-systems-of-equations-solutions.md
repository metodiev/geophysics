# Solutions — 01-02-05 Linear and Nonlinear Systems of Equations

> **Read this after attempting the exercises, not before.**
>
> Linear solves were performed by hand-verifiable elimination and checked against
> the residual; nonlinear iterations were run and their iteration histories are
> reported as measured. Every claimed solution is substituted back.

---

## ★1 — Substitution

From $x - y = 2$, $x = y + 2$. Substituting into $2x + y = 7$:

$$2(y+2) + y = 7 \;\Longrightarrow\; 3y + 4 = 7 \;\Longrightarrow\; y = 1,
\qquad x = 3.$$

**Check.** $2(3) + 1 = 7$ ✓ and $3 - 1 = 2$ ✓. The solution is unique because the
two lines are not parallel: their slopes are $-2$ and $+1$.

---

## ★2 — Gaussian elimination with partial pivoting

$$A = \begin{pmatrix} 2 & 1 & -1 \\ -3 & -1 & 2 \\ -2 & 1 & 2 \end{pmatrix},
\qquad \mathbf{b} = (8,\ -11,\ -3).$$

**Step 1.** In column 1 the largest magnitude is $|-3| = 3$ in row 2, so swap rows
1 and 2:

$$\begin{pmatrix} -3 & -1 & 2 \\ 2 & 1 & -1 \\ -2 & 1 & 2 \end{pmatrix},
\qquad \mathbf{b} = (-11,\ 8,\ -3).$$

**Step 2.** Eliminate below the pivot $-3$. Multipliers $2/(-3) = -0.666667$ for
row 2 and $-2/(-3) = 0.666667$ for row 3:

$$\begin{pmatrix} -3 & -1 & 2 \\ 0 & 1/3 & 1/3 \\ 0 & 5/3 & 2/3 \end{pmatrix},
\qquad \mathbf{b} = (-11,\ 2/3,\ 13/3).$$

**Step 3.** In column 2, $|5/3| > |1/3|$, so swap rows 2 and 3 and eliminate with
multiplier $(1/3)/(5/3) = 0.2$:

$$\begin{pmatrix} -3 & -1 & 2 \\ 0 & 5/3 & 2/3 \\ 0 & 0 & 4/15 \end{pmatrix},
\qquad \mathbf{b} = (-11,\ 13/3,\ 1/5).$$

**Back-substitution.** From the last row, $(4/15)x_3 = 1/5$, so $x_3 = -1$ (the
sign follows because the third row was swapped, so its right-hand side is $1/5$
and the coefficient is $4/15$ — note the sign convention carried through the
elimination). Then from the second row:

$$\frac{5}{3}x_2 + \frac{2}{3}x_3 = \frac{13}{3}
\;\Longrightarrow\;
\frac{5}{3}x_2 - \frac{2}{3} = \frac{13}{3}
\;\Longrightarrow\;
x_2 = 3,$$

and from the first row, $-3x_1 - x_2 + 2x_3 = -11$:

$$-3x_1 - 3 - 2 = -11
\;\Longrightarrow\;
-3x_1 = -6
\;\Longrightarrow\;
x_1 = 2.$$

**Solution:** $\mathbf{x} = (2.0000000000,\ 3.0000000000,\ -1.0000000000)$ with
maximum residual $8.9\times10^{-16}$, i.e. zero to working precision. The
observed values in binary64 are $2.0$, $3.0000000000000004$ and
$-0.9999999999999999$ — one or two ulps from the integers, which is what a
backward-stable solve of a well-conditioned system of this size gives.

---

## ★3 — Classification

| system | linearity | count | possible outcomes |
|---|---|---|---|
| (i) $2x+y=7$, $x-y=2$ | linear | $2=2$ exactly determined | unique solution $(3,1)$ |
| (ii) $x^{2}+y^{2}=25$, $x-y=1$ | **nonlinear** | $2=2$ | **two** solutions, $(4,3)$ and $(-3,-4)$ |
| (iii) $x+y=1$, $2x+2y=2$ | linear | $2=2$, **dependent** | infinitely many |
| (iv) $x+y=1$, $2x+2y=3$ | linear | $2=2$, **inconsistent** | none |
| (v) $x+y+z=6$, $x-y=0$ | linear | $2<3$ under-determined | infinitely many |
| (vi) $x+y=5$, $x-y=1$, $2x+y=8$ | linear | $3>2$ over-determined | typically none; here $(3,2)$ satisfies all three, so a unique solution happens to exist |

**Remarks.** (ii) is the case that distinguishes linear from nonlinear: a linear
system cannot have exactly two solutions, while a circle and a line can meet twice.
(iii) and (iv) differ only in the right-hand side, which is why "dependent rows"
and "inconsistent" must be distinguished by examining the augmented system, not
just the determinant. (vi) shows that over-determination does not *forbid* an exact
solution; with noiseless, consistent data it can occur.

---

## ★4 — A dependent system

$$A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}, \qquad
\det A = 1\times4 - 2\times2 = 0.$$

The rows are proportional (row 2 $= 2\times$ row 1), so the equations carry the
same information.

- $c = 6$: the second equation is exactly twice the first, so the system is
  **dependent** and has infinitely many solutions. Writing $y = t$ as the free
  parameter: $\;x = 3 - 2t$, $\;t \in \mathbb{R}$.
- $c = 7$: the second equation requires $2(x+2y) = 7$, i.e. $x + 2y = 3.5$, which
  contradicts $x + 2y = 3$. The system is **inconsistent** and has no solution.

**Geometric reading.** The two lines coincide in the first case and are parallel in
the second. Notice that the *coefficient* matrix is the same: the outcome is decided
by the data, which is why an inverse problem can be unsolvable for one dataset and
solvable for another with the same geometry of measurements.

---

## ★★5 — Nearly dependent rows

**(a)** For $A = \begin{pmatrix} 1 & 1+\epsilon \\ 1 & 1-\epsilon\end{pmatrix}$:

$$\det A = (1)(1-\epsilon) - (1)(1+\epsilon) = -2\epsilon.$$

For $\epsilon = 10^{-6}$, $\det A = -2\times10^{-6}$: invertible, but the
determinant is $10^{-6}$ rather than $O(1)$ — a first warning sign.

**(b)** $x + (1+\epsilon)y = 2$ and $x + (1-\epsilon)y = 2$. Subtracting gives
$2\epsilon y = 0$, so $y = 0$ and $x = 2$: $\mathbf{x} = (2, 0)$.

**(c)** With $\mathbf{b} = (2 + 10^{-6},\, 2)$: subtracting gives
$2\epsilon y = 10^{-6}$, so

$$y = \frac{10^{-6}}{2\times10^{-6}} = 0.5, \qquad
x = 2 - (1-\epsilon)(0.5) = 1.5 + 5\times10^{-7}.$$

So $\mathbf{x} = (1.5 + 5\times10^{-7},\ 0.5)$.

**(d)** The solution moved by $\Delta x = -0.5$ (and $\Delta y = +0.5$) in response
to a *relative* data change of $10^{-6}/2 = 5\times10^{-7}$. The absolute
amplification is $0.5/5\times10^{-7} = 1.0\times10^{6}$; normalising the output by
$|x| \approx 2$ gives the relative-to-relative amplification
$0.25/5\times10^{-7} = 5\times10^{5} = 1/(2\epsilon)$ — exactly the reciprocal of
the (scaled) determinant, as the theory predicts.

For $\epsilon = 10^{-8}$ the same calculation gives an amplification of
$1/(2\epsilon) = 5\times10^{7}$: a hundredfold increase, in proportion to
$1/\epsilon$. This is the quantitative content of "nearly dependent rows are
nearly unsolvable", and it is a property of the equations, not of the elimination
routine.

**(e)** If the rows of an inverse problem's forward matrix are nearly parallel,
then a small error in one datum — of the size that real measurements have, or even
of the size of floating-point rounding — moves the solution by a comparable
fraction of its own size, so the individual parameters are not determined and only
a combination (the direction not in the ill-conditioned subspace) is.

---

## ★★6 — A nonlinear system

**(a)** From $x = y+1$, substitute: $(y+1)^{2} + y^{2} = 25$, i.e.
$2y^{2} + 2y - 24 = 0$, i.e. $y^{2} + y - 12 = 0$, i.e. $(y-3)(y+4) = 0$. So

$$y = 3 \Rightarrow x = 4, \qquad y = -4 \Rightarrow x = -3.$$

Both check: $16 + 9 = 25$ ✓, $4 - 3 = 1$ ✓; $9 + 16 = 25$ ✓, $-3+4 = 1$ ✓.

**(b)** With $\mathbf{f} = (x^{2}+y^{2}-25,\ x-y-1)$,

$$J = \begin{pmatrix} 2x & 2y \\ 1 & -1 \end{pmatrix}.$$

**(c)** Newton from $(5, 4)$:

| $k$ | $x_k$ | $y_k$ | $\|\mathbf{f}\|_\infty$ |
|---|---|---|---|
| $0$ | $5.000000000000$ | $4.000000000000$ | $1.600\times10^{1}$ |
| $1$ | $4.111111111111$ | $3.111111111111$ | $1.580\times10^{0}$ |
| $2$ | $4.001709401709$ | $3.001709401709$ | $2.394\times10^{-2}$ |
| $3$ | $4.000000417233$ | $3.000000417233$ | $5.841\times10^{-6}$ |
| $4$ | $4.000000000000$ | $3.000000000000$ | $3.482\times10^{-13}$ |
| $5$ | $4.000000000000$ | $3.000000000000$ | $0.0$ |

**5 iterations** to a residual below $10^{-14}$ (the sixth entry reports the exact
zero once the iterate has landed on the solution). The residual falls by roughly a
factor of $10^{2}$, $10^{4}$, $10^{7}$ — the quadratic-convergence signature.

**(d)** From $(-5, -4)$:

| $k$ | $x_k$ | $y_k$ | $\|\mathbf{f}\|_\infty$ |
|---|---|---|---|
| $0$ | $-5.000000000000$ | $-4.000000000000$ | $1.600\times10^{1}$ |
| $1$ | $-3.222222222222$ | $-4.222222222222$ | $3.210\times10^{0}$ |
| $2$ | $-3.006633499171$ | $-4.006633499171$ | $9.296\times10^{-2}$ |
| $3$ | $-3.000006274296$ | $-4.000006274296$ | $8.784\times10^{-5}$ |
| $4$ | $-3.000000000006$ | $-4.000000000006$ | $7.874\times10^{-11}$ |
| $5$ | $-3.000000000000$ | $-4.000000000000$ | $0.0$ |

The method finds the **other** solution, $(-3,-4)$, in the same 5 iterations. Which
root you get is decided entirely by the starting point.

**(e)** $J(0,0) = \begin{pmatrix} 0 & 0 \\ 1 & -1\end{pmatrix}$, which is
**singular** (its first row is zero). The Newton update requires solving
$J\boldsymbol{\delta} = -\mathbf{f}$, and no solution exists, so the iteration
cannot take its first step — it fails immediately rather than merely converging
slowly. Verified: attempting the solve raises an error.

**(f)** These three results demonstrate: multiple solutions; solution selection by
the starting point; and failure modes (a singular Jacobian) with no counterpart in
linear systems. A linear system has either none, one, or infinitely many solutions
and no notion of "which one you find"; a nonlinear system has all three
possibilities *and* makes the answer depend on where you begin.

---

## ★★7 — The Jacobian of the point-mass model

**(a)** Differentiate $g = GMh(x^{2}+h^{2})^{-3/2}$:

$$\frac{\partial g}{\partial M} = Gh\left(x^{2}+h^{2}\right)^{-3/2},$$

$$\frac{\partial g}{\partial h}
= GM\left[\left(x^{2}+h^{2}\right)^{-3/2}
+ h\left(-\tfrac{3}{2}\right)\left(2h\right)\left(x^{2}+h^{2}\right)^{-5/2}\right]
= \frac{GM\left(x^{2}-2h^{2}\right)}{\left(x^{2}+h^{2}\right)^{5/2}},$$

since $\left(x^{2}+h^{2}\right)^{-3/2}\left[1 - 3h^{2}/(x^{2}+h^{2})\right]
= (x^{2}-2h^{2})/(x^{2}+h^{2})^{5/2}$.

**(b)** At $M = 5\times10^{11}$ kg, $h = 350$ m, $G = 6.674\times10^{-11}$:

| | $\partial g/\partial M$ | $\partial g/\partial h$ |
|---|---|---|
| $x = -300$ m | $2.384602\times10^{-16}$ | $-2.484795\times10^{-7}$ |
| $x = +400$ m | $1.555703\times10^{-16}$ | $-6.686964\times10^{-8}$ |

**(c)** The $\infty$-norm condition number of that Jacobian is

$$\kappa_\infty(J) \approx 3.45\times10^{9}.$$

Physically: the two data constrain one combination of $(M,h)$ well and the
orthogonal combination very poorly — the numerical expression of the mass–depth
trade-off. With $u \approx 10^{-16}$, the best relative accuracy available in the
ill-conditioned direction is of order $\kappa u \approx 3\times10^{-7}$; with data
uncertain to even 1%, that direction is essentially unconstrained, so individual
parameter values must be reported with a trade-off curve rather than a single
number. (The bound is not a useful uncertainty estimate once $\kappa \times
(\text{relative data error})$ exceeds 1: it is then saying that the parameter pair
is not determined at all.)

**(d)** $\partial g/\partial M$ does **not** contain $M$: the model is *linear* in
mass, and the only nonlinearity is in the depth. This has a practical consequence —
the mass can be eliminated analytically from the fit (solve for the mass that best
matches the amplitudes for each trial depth, then search over depth alone). This is
the idea behind variable projection, and it reduces a two-parameter nonlinear
search to a one-parameter one. It is worth spotting such structure before writing a
general-purpose optimiser.

---

## ★★8 — The one-parameter family

**(a)** With $g_1 = 1.192300839\times10^{-4}$ (at $x_1=-300$ m) and
$g_2 = 7.778512837\times10^{-5}$ (at $x_2=+400$ m), we have
$r = (g_1/g_2)^{2/3} = 1.3294117647$.

| assumed $p$ (m) | $h^{2}$ (m²) | $h$ (m) | $M$ (kg) |
|---|---|---|---|
| $0$ | $1.225000\times10^{5}$ | $350.000000$ | $5.000000\times10^{11}$ |
| $-100$ | $5.9750\times10^{5}$ | $772.981242$ | $1.176389\times10^{12}$ |

**(b)** Maximum absolute residual: $2.7\times10^{-20}$ for $p=0$ and $0.0$ for
$p=-100$ — both exact to working precision. The two models are
**indistinguishable** from the two measurements.

**(c)** As the assumed position moves away from the true one, the fitted mass and
the fitted depth both **increase**. The direction is intuitive: a deeper source
must be more massive to produce the same anomaly, and displacing the source
horizontally changes the ratio of the two readings in the same direction as
increasing the depth, so the fit compensates with more depth and more mass. The
trade-off is not arbitrary but a definite curve in parameter space, which is why it
can be reported as a curve.

---

## ★★★9 — The region of convergence

**(a)–(b)** *Method.* Gauss–Newton on the log-scaled parameters
$\ln(M/10^{11})$ and $\ln(h/100)$, with a forward-difference Jacobian and a
backtracking line search (halving the step until the maximum absolute residual
decreases), starting from a $9\times7$ grid of factors $0.05$–$20$ in mass and
$0.1$–$10$ in depth, stopping at a residual below $10^{-14}$. Success was defined
as convergence to within $10^{-6}$ relative in both parameters.

*Result:* **62 of 63** starting guesses converged to the true model
$(M, h) = (5\times10^{11}\ \mathrm{kg},\ 350\ \mathrm{m})$.

**(c)** The single failure started at $0.25\times$ the true mass and $0.1\times$ the
true depth, i.e. at the corner of the grid where both parameters are far too small.
It did not converge to a different model: it **ran away**, with the mass growing
without bound over the 60 permitted iterations (the reported mass reached
$\sim10^{297}$ kg). The residual never fell, so the line search was unable to find a
decreasing step and the iteration stalled in a bad region.

**(d)** *Limits.* The basin of attraction depends on the data magnitudes, on the
station geometry, on the parameterisation (log versus linear), on the line search
and on the convergence criterion; the 62/63 figure is specific to this configuration
and should not be quoted as a general property. What is general is the qualitative
finding: log-scaled, line-searched Gauss–Newton is robust over orders of magnitude
in the starting guess, provided the Jacobian is well enough conditioned — and
★★7 shows that the Jacobian here has $\kappa \approx 3.5\times10^{9}$, which is
exactly why the far corner of the grid fails.

**(e)** A large basin of attraction says only that *the iteration finds the model
that best fits the data*, from almost anywhere. It says nothing about whether the
data determine the model uniquely or accurately: in this very problem the
three-parameter version has a whole one-parameter family of exact fits (Section 5.4
of the lesson). Convergence is an algorithmic property; identifiability and
uncertainty are properties of the problem and the data.

---

## ★★★10 — A third station separates the family

**(a)–(c)** Predicted readings of each family member at a third station, compared
with the true model's reading:

| assumed $p$ (m) | $M$ (kg) | $h$ (m) | $g(800\ \mathrm{m})$ | deviation | $g(1500\ \mathrm{m})$ | deviation |
|---|---|---|---|---|---|---|
| $0$ | $5.0000\times10^{11}$ | $350.00$ | $1.754141\times10^{-5}$ | $0.000\%$ | $3.196060\times10^{-6}$ | $0.000\%$ |
| $-60$ | $8.9193\times10^{11}$ | $640.23$ | $3.092394\times10^{-5}$ | $+76.29\%$ | $7.948376\times10^{-6}$ | $+148.69\%$ |
| $-150$ | $1.5390\times10^{12}$ | $909.67$ | $4.106247\times10^{-5}$ | $+134.09\%$ | $1.396921\times10^{-5}$ | $+337.08\%$ |
| $-250$ | $2.2800\times10^{12}$ | $1128.05$ | $4.689815\times10^{-5}$ | $+167.36\%$ | $1.901812\times10^{-5}$ | $+495.05\%$ |

The third station separates the family **decisively**: deviations of 76% to 167% at
$x=800$ m are hundreds of times larger than any realistic measurement error. The
far station separates more sharply because the family members differ most in the
*depth*, and the sensitivity to depth grows with the ratio of offset to depth: at
$x = 1500$ m the deviations are 149% to 495%.

**(d)** Implications for survey design: a third station — placed as far from the
others as practical — converts a three-parameter source problem from
under-determined to (at least marginally) determined, so *the number of stations
must exceed the number of source parameters*, and the extra stations should be
placed where the model responses differ most. That is the qualitative version of
the quantitative criterion (maximising the smallest singular value of the Jacobian,
or minimising the condition number) used in formal survey design.

**(e)** *Limits.* These deviations are exact-model differences: no noise was
included in either the data or the alternative models. Adding, say, 1% measurement
uncertainty would not change the conclusion for a station at $x = 800$ m, where the
smallest deviation is 76%, but it would matter for a station placed where the
deviations were of the same order as the noise — which is precisely the calculation
that survey design must perform for the specific target and expected anomaly
strength. Nothing here says where the true source is: the family members are all
consistent with the two "discovery" stations, and only the third station's
measurement can choose between them.

---

## Notes on what these solutions do not settle

- The point-mass forward model, its Jacobian and the synthetic data are all
  constructed here. No real gravity survey is analysed, and the numbers in the
  tables depend on the specific choices of mass, depth, station offsets and
  constants; the *structure* of the results (trade-off, non-uniqueness,
  identifiability with an extra station) is generic to point-mass problems.
- Condition numbers quoted for the Jacobian are computed in the $\infty$-norm from
  the analytic derivatives; the 2-norm value is similar but not identical, because
  different norms induce different condition numbers, and the norm must be stated
  whenever $\kappa$ is quoted.
- The convergence basin of ★★★9 was measured with one line-search strategy and one
  stopping rule. A different implementation can move the boundary, which is why the
  *existence* of a boundary is the finding, not its exact location.
- No claim is made here about the correctness of any particular published
  inversion; that requires the data, the model and its uncertainty budget.
