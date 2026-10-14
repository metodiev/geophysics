---
id: 01-14-06
title: "Calculus of Variations and Its Geophysical Uses"
level: graduate
prereqs: ["01-14-01", "01-14-04", "01-09-07"]
estimated_minutes: 90
tags: [variational-calculus, euler-lagrange, free-surface, data-assimilation]
---

# Calculus of Variations and Its Geophysical Uses

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the Euler–Lagrange equation from the first variation of a
   functional, including the boundary terms, and say when a natural boundary
   condition appears.
2. **Verify** a variational derivative numerically by differentiating the
   functional along a perturbation and comparing with the integral of the
   gradient against that perturbation.
3. **Discretise** a functional directly, solve the resulting linear system or
   eigenproblem, and measure the convergence rate of the discrete minimiser.
4. **Explain** why the direct method replaces a boundary-value-problem solver
   with a matrix solve, and name the geophysical problems where that is what
   practitioners do.
5. **Recognise** natural boundary conditions in free-surface, geoid and flexure
   problems, and say what physics an imposed-versus-natural condition encodes.
6. **Quantify** the trade between mesh refinement and conditioning in the direct
   method.

## Prerequisites

[01-14-01 Convexity, Stationarity and Optimality Conditions](./01-convexity.md)
for stationarity and curvature,
[01-14-04 Linear and Nonlinear Least Squares](./04-least-squares.md) for the
linear-algebraic machinery the discretisation produces, and
[01-09-07 Boundary Value Problems](../09-partial-differential-equations/07-boundary-value-problems.md)
for the boundary-value language used throughout.

## 1. Intuition: optimising over functions, not numbers

Up to here the unknown has been a finite list of numbers, $m \in
\mathbb{R}^{p}$. Many geophysical unknowns are functions: the shape of a
free surface, the height of the geoid, the state of the atmosphere at every time,
the interface between two layers, a velocity field. The calculus of variations
is the version of optimisation for those problems, and its central result is
that **a minimiser of an integral satisfies a differential equation** — the
Euler–Lagrange equation — together with boundary conditions that either are
imposed or emerge from the stationarity condition itself.

Two facts make this more than a formal exercise.

First, the variational form is *frequently the natural way to write the physics*.
Free-surface problems minimise an energy; geoid determination minimises a
functional of the disturbing potential; variational data assimilation minimises a
cost functional over a whole trajectory in time; flexure of the lithosphere
minimises bending energy. In each case the physics is the functional and the
differential equation is a consequence.

Second, the direct method inverts the logical order. Discretise the functional
(rather than discretise the differential equation), minimise over the node
values, and you get a linear system — or an eigenvalue problem — that you already
know how to solve from [01-14-04](./04-least-squares.md). No boundary-value-problem
solver is needed, natural boundary conditions appear automatically, and the whole
apparatus of this module (conditioning, damping, regularisation) applies
immediately.

## 2. Precise definitions

### 2.1 Functionals

A **functional** maps a function to a real number:

$$F[y] = \int_{a}^{b} L\bigl(x, y(x), y'(x)\bigr)\,dx . \tag{2.1}$$

$L$ is the **Lagrangian density**. The set of admissible functions is constrained
by boundary conditions on $y(a)$ and $y(b)$; if a boundary value is not imposed,
it is **free** and the variational principle supplies a condition for it.

### 2.2 The first variation

Let $\delta y$ be an admissible perturbation and compute

$$\delta F[y; \delta y] = \left.\frac{d}{d\epsilon} F[y + \epsilon\,\delta y]
\right|_{\epsilon = 0}. \tag{2.2}$$

Stationarity means $\delta F = 0$ for every admissible $\delta y$. The
calculation gives the Euler–Lagrange equation plus boundary terms:

$$\frac{\partial L}{\partial y} - \frac{d}{dx}\left(\frac{\partial L}{\partial
y'}\right) = 0 \quad \text{on } (a,b), \tag{2.3}$$

$$\left[\frac{\partial L}{\partial y'}\,\delta y\right]_{a}^{b} = 0
\qquad\text{(boundary term)}. \tag{2.4}$$

Equation (2.4) is the one students skip and practitioners need: if $\delta y(a) =
0$ is imposed, that end contributes nothing; if $\delta y(a)$ is arbitrary (a free
end), the boundary term forces $\partial L/\partial y' = 0$ at that end. Such a
condition is called **natural**, and it is what makes free-surface problems
soluble without inventing a boundary condition.

### 2.3 The variational derivative

When the functional is used as an objective to be minimised numerically, its
gradient in the $L^{2}$ sense is the function $g$ satisfying

$$\delta F[y;\delta y] = \int_{a}^{b} g(x)\,\delta y(x)\,dx
\qquad\text{for all admissible } \delta y. \tag{2.5}$$

For (2.1) with boundary terms vanishing, integration by parts gives

$$g(x) = \frac{\partial L}{\partial y}
- \frac{d}{dx}\frac{\partial L}{\partial y'}. \tag{2.6}$$

Setting $g = 0$ recovers (2.3). In a numerical implementation, $g$ is the
gradient that a descent method consumes.

### 2.4 The Rayleigh quotient

The simplest variational eigenvalue problem:

$$R[y] = \frac{\int_a^b p(x)\,y'(x)^{2}\,dx}{\int_a^b y(x)^{2}\,dx},
\qquad y(a) = y(b) = 0. \tag{2.7}$$

Its stationary values are the generalised eigenvalues of
$-(p y')' = \lambda y$; its minimum is the smallest eigenvalue and its maximum
the largest. For $p = 1$ on $[0,1]$ the minimum is $\pi^{2}$, attained at
$y = \sin \pi x$. This is the form in which free oscillations, normal modes and
many geoid problems are actually posed.

### 2.5 Discretisation choices

Two routes:

| route | what is discretised | what you solve |
|---|---|---|
| Indirect | the Euler–Lagrange equation | a boundary-value problem |
| Direct | the functional | a linear system or an eigenproblem |

The direct method is used when the functional is easier to write than its
equation, when natural boundary conditions are wanted for free, and when the
problem is a constrained optimisation over functions — the discrete problem is
then exactly the finite-dimensional optimisation of this module.

## 3. Derivations

### 3.1 Euler–Lagrange by parts

Substituting $y + \epsilon \delta y$ into (2.1) and differentiating under the
integral:

$$\frac{d}{d\epsilon}F[y + \epsilon\delta y]\Big|_{\epsilon=0}
= \int_a^b \left(\frac{\partial L}{\partial y}\delta y
+ \frac{\partial L}{\partial y'}\delta y'\right)dx .$$

Integrate the second term by parts:

$$\int_a^b \frac{\partial L}{\partial y'}\,\delta y'\,dx
= \left[\frac{\partial L}{\partial y'}\delta y\right]_a^b
- \int_a^b \frac{d}{dx}\left(\frac{\partial L}{\partial y'}\right)\delta y\,dx .$$

Collecting,

$$\delta F = \int_a^b \left[\frac{\partial L}{\partial y}
- \frac{d}{dx}\frac{\partial L}{\partial y'}\right]\delta y\,dx
+ \left[\frac{\partial L}{\partial y'}\delta y\right]_a^b . \tag{3.1}$$

Since $\delta y$ is arbitrary in the interior, the bracket must vanish — equation
(2.3) — and the boundary term must vanish for every admissible perturbation,
which yields either an imposed condition ($\delta y = 0$) or the natural
condition $\partial L/\partial y' = 0$.

### 3.2 Two worked examples

**Fixed endpoints, $L = y'^{2} + y$.** Then
$\partial L/\partial y = 1$, $\partial L/\partial y' = 2y'$, so (2.3) is
$1 - 2y'' = 0$, i.e. $y'' = 1/2$ with $y(0) = 0$, $y(1) = 1$:
$y = x^{2}/4 + 3x/4$. Section 4.3 verifies the first variation of exactly this
functional numerically.

**Free end, $L = y'^{2} - 2y$ with $y(1)$ free.** The equation is
$y'' = -1$, and the boundary term at $x = 1$ forces $\partial L/\partial y' =
2y'(1) = 0$: a natural (Neumann) condition, $y'(1) = 0$. With $y(0) = 0$ the
solution is $y = -x^{2}/2 + x$, whose value at the free end is $y(1) = 0.5$.
Section 4.5 shows the discrete solution obeying $y_n - y_{n-1} = h^{2}/2$, i.e.
$y'(1) = h/2 \to 0$ as the mesh is refined: the condition was never imposed.

**A quadratic functional, $L = y'^{2} + y^{2}$.** Equation (2.3) gives
$y'' = y$, with the hyperbolic solution $y = \sinh x/\sinh 1$ for
$y(0) = 0, y(1) = 1$. This is the example used to measure the convergence rate,
because its solution is *not* a polynomial and therefore the discretisation
error is nonzero (Section 4.1).

### 3.3 The direct method in detail

Approximate the integral by a sum on a uniform grid $x_i = ih$, $h = 1/n$, and
the derivative by a forward difference $y' \approx (y_{i+1} - y_i)/h$:

$$F_h(y) = \sum_{i=0}^{n-1}\left[\frac{(y_{i+1}-y_i)^{2}}{h}
+ \frac{h}{2}\bigl(g(y_i) + g(y_{i+1})\bigr)\right] \tag{3.2}$$

for a functional $\int (y'^{2} + g(y))dx$, with the trapezoid rule for the
non-derivative part. Requiring $\partial F_h/\partial y_j = 0$ for the interior
nodes gives

$$2y_j - y_{j-1} - y_{j+1} + \frac{h^{2}}{2}\,g'(y_j) = 0, \tag{3.3}$$

which is the three-point finite-difference approximation of $y'' = g'(y)/2$ —
the Euler–Lagrange equation, to $O(h^{2})$. For the linear case $g(y) = y^{2}$
this is a symmetric tridiagonal system

$$\left(2 + h^{2}\right)y_j - y_{j-1} - y_{j+1} = 0,$$

solvable in $O(n)$ by the Thomas algorithm; for a nonlinear $g$ it is a nonlinear
system, solved by Newton or Gauss–Newton from
[01-14-02](./02-unconstrained.md) and [01-14-04](./04-least-squares.md).

Two properties follow from the construction and are worth stating explicitly:

- **The discretisation is a convex quadratic** for linear $g$, so the discrete
  minimiser is unique and any solver finds it.
- **Its error is second order in $h$**, because the trapezoid rule and the central
  difference are both $O(h^{2})$ accurate; Section 4.1 measures exactly that.

### 3.4 The Rayleigh quotient as a generalised eigenproblem

Discretising (2.7) with the same scheme (and lumped mass, which keeps the problem
tridiagonal well posed) gives

$$\frac{1}{h^{2}}\,K\,y = \lambda\,y, \qquad
K = \operatorname{tridiag}(-1, 2, -1), \qquad y \in \mathbb{R}^{n-1}. \tag{3.4}$$

The eigenvalues of $K$ are $2 - 2\cos(k\pi/n)$ for $k = 1,\dots,n-1$, so the
smallest is

$$\lambda_{\min} = \frac{2 - 2\cos(\pi/n)}{h^{2}} = \frac{4\sin^{2}(\pi/2n)}{h^{2}}
= \pi^{2}\left(1 + \frac{\pi^{2}}{12n^{2}} + O(n^{-4})\right), \tag{3.5}$$

whose error is $O(n^{-2}) = O(h^{2})$, measured in Section 4.6. Inverse iteration
— solving $A y = x$ repeatedly with the Thomas algorithm — converges to the
smallest eigenvalue; power iteration would give the largest.

### 3.5 Why refinement costs conditioning

The matrix $K$ in (3.4) has condition number

$$\kappa(K) = \frac{2 + 2\cos(\pi/n)}{2 - 2\cos(\pi/n)}
\approx \frac{4(n+1)^{2}}{\pi^{2}} \quad (m = n-1 \text{ unknowns}),
\tag{3.6}$$

which grows like $n^{2}$. Refinement therefore buys accuracy at the price of
digits: at $n = 160$ the measured $\kappa$ is $10\,374.6$ against the formula's
$10\,375.3$. Sixteen hundred parameters cost four digits of conditioning; this is
the direct-method version of the resolution-versus-stability trade-off that
[01-07-05](../07-linear-algebra/05-determinants-inverses.md) states for linear
systems, and it is why practical codes use a moderate mesh with a preconditioner
rather than an arbitrarily fine one.

## 4. Numerical results

All numbers are from
[`code/variational_calculus_demo.py`](./code/variational_calculus_demo.py), which
implements the Thomas algorithm, the direct method, the Rayleigh-quotient
eigenproblem and a numerical first variation with the standard library alone.

### 4.1 Convergence of the direct method

Minimising $F[y] = \int_0^1 (y'^{2} + y^{2})dx$ with $y(0)=0$, $y(1)=1$, whose
exact solution is $y = \sinh(x)/\sinh(1) = 0.8509181282\sinh x$:

| $n$ | $h$ | max error | error ratio | measured order |
|---|---|---|---|---|
| $10$ | $0.10000$ | $4.4146\times10^{-5}$ | — | — |
| $20$ | $0.05000$ | $1.1047\times10^{-5}$ | $3.9962$ | $1.9986$ |
| $40$ | $0.02500$ | $2.7624\times10^{-6}$ | $3.9991$ | $1.9997$ |
| $80$ | $0.01250$ | $6.9090\times10^{-7}$ | $3.9982$ | $1.9994$ |
| $160$ | $0.00625$ | $1.7273\times10^{-7}$ | $3.9999$ | $2.0000$ |
| $320$ | $0.00313$ | $4.3182\times10^{-8}$ | $3.9999$ | $2.0000$ |

The measured order is $2.000$ to four decimals — as clean a convergence
measurement as this curriculum contains. It also shows why the *choice of test
problem* matters: the fixed-endpoint example $L = y'^{2}+y$ has a quadratic
solution and the scheme reproduces it exactly to round-off, so it cannot measure
any rate at all. A convergence study needs a solution outside the scheme's exact
class.

### 4.2 The discrete minimiser really minimises

At $n = 40$ the discrete functional at the discrete minimiser is
$1.313156718939$, and at the *sampled* exact solution it is $1.313156718985$ —
higher by $4.596\times10^{-11}$, i.e. equal to round-off. Perturbations of the
midpoint node confirm minimality:

| perturbation | $F_h$ | difference |
|---|---|---|
| bump $+10^{-3}$ | $1.313236743939$ | $+8.003\times10^{-5}$ |
| bump $+10^{-2}$ | $1.321159218939$ | $+8.002\times10^{-3}$ |
| dip $-10^{-3}$ | $1.313236743939$ | $+8.003\times10^{-5}$ |

Every perturbation increases the functional, and a bump costs exactly as much as
a dip — a signature of the quadratic form. The distinction to keep in mind: the
discrete minimiser minimises the *discrete* functional exactly, and the
continuous one only to $O(h^{2})$.

### 4.3 The first variation, verified

Take $y = x^{2}$ (not a minimiser) and $\delta y = \sin \pi x$, with the
functional $F[y] = \int_0^1(y'^{2}+y)dx$:

| route | value |
|---|---|
| $(F[y+\epsilon\delta y] - F[y-\epsilon\delta y])/(2\epsilon)$ at $\epsilon$ small, by numerical quadrature | $-1.9098592190$ |
| $\int_0^1 (1 - 2y'')\,\delta y\,dx = -3\int_0^1 \sin\pi x\,dx$ | $-1.9098593171$ |
| exact value $-6/\pi$ | $-1.9098593171$ |

The two routes agree to $9.813\times10^{-8}$, which is the accuracy of the
numerical quadrature and of the central difference in $\epsilon$, not a
discrepancy in the theory. What has been verified is the whole chain: the
variational derivative of this functional is $g(x) = 1 - 2y''$, and setting it to
zero for every admissible $\delta y$ is the Euler–Lagrange equation.

### 4.4 The natural boundary condition appears by itself

For $F[y] = \int_0^1 (y'^{2}-2y)dx$ with $y(0)=0$ and $y(1)$ free, whose exact
solution is $y = -x^{2}/2 + x$:

| $n$ | max error | $y(1)$ | $y_n - y_{n-1}$ | $h/2$ |
|---|---|---|---|---|
| $10$ | $3.886\times10^{-16}$ | $0.500000$ | $0.005000$ | $0.050000$ |
| $20$ | $1.499\times10^{-15}$ | $0.500000$ | $0.001250$ | $0.025000$ |
| $40$ | $8.604\times10^{-15}$ | $0.500000$ | $0.000312$ | $0.012500$ |
| $80$ | $3.386\times10^{-15}$ | $0.500000$ | $0.000078$ | $0.006250$ |

Two readings of the same table. The error is at round-off because the exact
solution is a quadratic and the scheme is exact for quadratics — this example
cannot measure convergence either (Section 4.1 does that). But the last three
columns are the interesting ones: the discrete solution satisfies
$y_n - y_{n-1} = h^{2}/2$, i.e. $y'(1) = h/2$, which tends to zero with $h$.
**The Neumann condition at the free end was never imposed; it emerged from
minimising the functional.** The practitioner's version of this statement: if you
discretise the energy and minimise, you get the physics' boundary condition
whether or not you know what it is; if you instead discretise the equation, you
must get it right by hand.

### 4.5 The Rayleigh quotient converges to $\pi^{2}$

Minimising $R[y] = \int y'^{2}/\int y^{2}$ over $y(0)=y(1)=0$, by inverse
iteration on (3.4):

| $n$ | $\lambda_{\min}$ | error against $\pi^{2} = 9.8696044011$ | measured order |
|---|---|---|---|
| $10$ | $9.7886967410$ | $8.091\times10^{-2}$ | — |
| $20$ | $9.8493275239$ | $2.028\times10^{-2}$ | $1.9964$ |
| $40$ | $9.8645320540$ | $5.072\times10^{-3}$ | $1.9991$ |
| $80$ | $9.8683361187$ | $1.268\times10^{-3}$ | $1.9998$ |

Order $2$ again, and the discrete eigenvalue is systematically *below* $\pi^{2}$
— the discrete Rayleigh quotient is a lower bound for the continuous one when
the trial space is a subspace of the admissible set, which is a Rayleigh–Ritz
property worth knowing: **refining the mesh can only lower the discrete
eigenvalue toward the truth.**

### 4.6 The price of refinement

| $n$ | unknowns $m$ | $\kappa(K)$ measured | $4(m+1)^{2}/\pi^{2}$ |
|---|---|---|---|
| $10$ | $9$ | $39.8635$ | $40.5285$ |
| $20$ | $19$ | $161.4476$ | $162.1139$ |
| $40$ | $39$ | $647.7890$ | $648.4556$ |
| $80$ | $79$ | $2593.1557$ | $2593.8223$ |
| $160$ | $159$ | $10\,374.6225$ | $10\,375.2892$ |

The measured condition number tracks the asymptotic formula (3.6) closely, and
it grows as $n^{2}$: doubling the mesh quadruples $\kappa$. At $n = 160$ the
solve has already lost roughly four digits, which is fine for a double-precision
problem and fatal for a single-precision one.

## 5. Physical interpretation

**A functional is a statement of energy or cost, and the Euler–Lagrange equation
is its equation of motion.** The flexure of the lithosphere under a load
minimises bending energy; a free surface minimises total potential energy;
Fermat's principle in seismology says the ray minimises travel time. When you see
a variational principle in a geophysics paper, the Euler–Lagrange equation of
that principle is the differential equation the paper then solves.

**Natural boundary conditions are physics that the functional already knows.**
"Zero traction at the free surface", "no bending moment at a plate edge", "zero
stress at infinity": written as conditions they look like extra assumptions, but
they are the boundary terms of (2.4) vanishing. Imposing them explicitly is
fine; forgetting them changes the answer.

**The direct method is inversion in disguise.** Discretising a functional and
minimising its node values is a finite-dimensional optimisation with a
tridiagonal Hessian. Everything from this module applies: conditioning (Section
4.6), damping, bounds on $y$, and evaluation of the misfit gradient. That is why
variational data assimilation and free-surface codes are written as
optimisation problems rather than as ODE solvers.

**The Rayleigh quotient is how normal modes are computed.** The eigenvalues of a
discretised Rayleigh quotient are the free-oscillation frequencies; the
eigenvectors are the mode shapes. Using the quotient rather than differentiating
the operator also gives the Rayleigh–Ritz bound of Section 4.5: your discrete
answer is a lower bound, and refining the trial space can only improve it.

**Mesh refinement is not free.** Accuracy improves as $h^{2}$ while conditioning
degrades as $h^{-2}$; the crossover is where round-off overtakes truncation. The
practical rule is to fix the mesh by the resolution of the data and then stop —
added nodes that are not constrained by data buy nothing but conditioning loss.

## 6. Assumptions and regime of validity

1. **Smoothness of the Lagrangian and the minimiser.** The classical
   Euler–Lagrange derivation assumes $y \in C^{2}$; problems with kinks, shocks
   or discontinuous coefficients need weak or variational solutions, which exist
   but require more care.
2. **Convexity for the minimiser to be unique.** Convergence of the discrete
   minimiser to the continuous one requires the functional to be well posed
   (coercive and weakly lower semi-continuous); a non-convex energy can have a
   discrete solution that converges to something that is not a minimiser.
3. **The discretisation must be consistent.** In (3.2) the trapezoid quadrature
   and the forward difference are both $O(h^{2})$; mixing an $O(h)$ quadrature with
   an $O(h^{2})$ derivative would degrade the measured rate. Consistency of the
   *functional*, not just of the equation, is what guarantees the rate.
4. **Natural versus imposed conditions must be chosen deliberately.** A free end
   in the model must be free in the functional; if you impose a Neumann condition
   *and* leave the end free, you have over-specified the problem.
5. **Conditioning limits the usable mesh** (Section 4.6). The measured $\kappa$
   at $n = 160$ is $10^{4}$; at $n = 10^{5}$ it would be $\sim10^{10}$ and the
   direct solve would need preconditioning or an iterative method.
6. **Second-order accuracy is the generic case, not a law.** The $O(h^{2})$ rate
   measured here follows from the trapezoid and central-difference choices. A
   higher-order quadrature with a higher-order derivative approximation gives a
   higher rate, at the cost of a wider stencil and boundary technicalities.

## 7. Python demonstration

The companion script is
[`code/variational_calculus_demo.py`](./code/variational_calculus_demo.py), with
six sections: the direct method with a measured rate, the minimality check, the
first-variation verification, a free end with a natural boundary condition, the
Rayleigh-quotient eigenproblem, and the conditioning price of refinement.

| Section | Measured | Interpretation |
|---|---|---|
| 1, rate | errors $4.41\times10^{-5} \to 4.32\times10^{-8}$ for $n = 10 \to 320$, order $2.0000$ | the direct method inherits $O(h^{2})$ |
| 2, minimality | every midpoint perturbation raises $F_h$; sampled exact solution higher by $4.6\times10^{-11}$ | the discrete solution is the discrete minimiser |
| 3, first variation | $-1.9098592190$ against $-1.9098593171$ (exact $-6/\pi$) | the variational derivative is verified |
| 4, natural BC | $y_n - y_{n-1} = h^{2}/2 = 0.005, 0.00125, \dots$ | the Neumann condition emerges from the minimisation |
| 5, Rayleigh | $\lambda_{\min} = 9.8683361187$ at $n = 80$ against $\pi^{2} = 9.8696044011$ | order $2$, and a lower bound |
| 6, conditioning | $\kappa = 10\,374.6$ at $n = 160$ against the formula's $10\,375.3$ | accuracy is bought with digits |

> **Breaking exercise.** In Section 1, replace the trapezoid rule for
> $\int y^{2}\,dx$ with the midpoint rule ($h\,y_j^{2}$ at the midpoints, i.e.
> using a doubled grid) and predict, before running, whether the measured order
> falls to $1$ or stays at $2$. Then run it. The general principle is that the
> order of the discrete minimiser is set by the *worst* consistent
> discretisation in the functional, which is why quadrature and differentiation
> errors must be matched.

## 8. Exercises

Full set and worked solutions:
[`exercises/06-variational-calculus-exercises.md`](./exercises/06-variational-calculus-exercises.md)
and
[`exercises/06-variational-calculus-solutions.md`](./exercises/06-variational-calculus-solutions.md).
Four to start with:

**★1.** Derive the Euler–Lagrange equation for $F[y] = \int_0^1 (y'^{2} +
2xy)\,dx$ with $y(0)=y(1)=0$ and solve it.

**★2.** For $F[y] = \int_0^1 y'^{2}\,dx$ with $y(0) = 0$ and $y(1)$ free, state
the equation and the natural condition, and solve.

**★★3.** Write the direct-method system for $\int (y'^{2} + k^{2}y^{2})dx$ with
fixed endpoints and identify the discrete eigenvalue problem that arises.

**★★4.** Show that the minimum of the Rayleigh quotient over all admissible $y$
is bounded below by the smallest eigenvalue of the differential operator, and
explain why this makes the discrete quotient a lower bound.

## 9. Common mistakes

1. **Dropping the boundary term.** Equation (3.1)'s surface term is where natural
   conditions come from; dropping it silently imposes $\delta y = 0$ where the
   problem does not want it.
2. **Discretising the equation when the functional is available.** The direct
   method gives a symmetric, solvable system and the natural condition for free.
3. **Measuring a convergence rate on a problem the scheme solves exactly.**
   Section 4.4's error is $10^{-15}$ for every $n$: no rate can be extracted, and
   a careless study would report "order zero".
4. **Refining without preconditioning.** $\kappa \sim n^{2}$ (Section 4.6).
5. **Confusing the discrete minimiser with the exact solution.** They differ by
   $O(h^{2})$, which is the whole content of the convergence table.
6. **Over-specifying a free boundary.** Imposing $y'(1) = 0$ *and* leaving the end
   free is either redundant or wrong.
7. **Assuming a higher-order scheme is always the better choice.** A wider
   stencil means more boundary exceptions and often worse conditioning.

## 10. Real-world applications

- **Free-surface and fluid-solid boundary problems.** The free surface is a
  natural boundary condition of the elastic energy functional; codes that solve
  the variational form get it without prescribing a surface traction.
- **Geoid determination.** Minimising a functional of the disturbing potential
  (with a Stokes-type kernel) is the classical variational formulation, and the
  normal equations are the least-squares problem of
  [01-14-04](./04-least-squares.md).
- **Variational (4D-Var) data assimilation.** Minimise a cost functional over an
  entire model trajectory; the gradient is computed by the adjoint of the model,
  which is the discrete version of (2.6). The Euler–Lagrange equations of the
  cost functional are the model equations plus the adjoint equations.
- **Isostasy and flexure.** Bending-energy minimisation gives the flexure
  equation and its natural conditions (no shear, no moment at a free end).
- **Normal modes and free oscillations.** The Rayleigh quotient yields the
  eigenfrequencies; the lower-bound property of Section 4.5 is used deliberately
  to bracket them.
- **Optimal survey design.** Minimising a functional of the model covariance over
  sensor positions is a variational problem whose Euler–Lagrange equation gives
  stationarity conditions on the design.

## 11. Further reading

- **Gelfand, I. M., & Fomin, S. V. *Calculus of Variations*. Dover.** Level:
  advanced. The classical treatment, including the natural boundary conditions
  and the first variation done carefully.
- **Lanczos, C. *The Variational Principles of Mechanics* (4th ed.). Dover.**
  Level: intermediate to advanced. Why variational formulations are the natural
  language of physics, with the Rayleigh quotient as a central tool.
- **Courant, R., & Hilbert, R. *Methods of Mathematical Physics*, Vol. I.**
  Level: research. The direct method in its original form, including the
  convergence theory behind Section 4.1.
- **Strang, G., & Fix, G. *An Analysis of the Finite Element Method*.**
  Level: advanced. The direct method generalised; finite elements are this lesson
  with a better basis.
- **Bennett, A. F. *Inverse Methods in Physical Oceanography*. Cambridge
  University Press.** Level: graduate. Variational data assimilation written as a
  variational problem, with the adjoint and the cost functional.
- **Tarantola, A. *Inverse Problem Theory and Methods for Model Parameter
  Estimation*. SIAM.** Level: graduate. The variational formulation of inversion
  in general.

> Note on citations: bibliographic details above are given so that you can locate
> the works. This repository does not host or reproduce copyrighted text, and you
> should confirm editions and current availability through your library before
> citing them yourself.

## 12. Self-assessment checklist

- [ ] I can derive the Euler–Lagrange equation including the boundary term.
- [ ] I can decide whether a boundary condition is imposed or natural, and find
      the natural one.
- [ ] I can verify a variational derivative numerically against a finite
      difference of the functional.
- [ ] I can discretise a functional and assemble the resulting tridiagonal
      system.
- [ ] I can measure the convergence order of a direct method and explain why the
      test problem must not be one the scheme solves exactly.
- [ ] I can set up and solve a Rayleigh-quotient eigenproblem by inverse
      iteration.
- [ ] I can state the conditioning cost of refinement and the measured rate
      $\kappa \sim n^{2}$.

## 13. Related lessons

- [01-14-01 Convexity, Stationarity and Optimality Conditions](./01-convexity.md) —
  stationarity, of which the first variation is the infinite-dimensional case.
- [01-14-04 Linear and Nonlinear Least Squares](./04-least-squares.md) — the
  discrete problem the direct method produces.
- [01-14-05 Global Optimisation](./05-global-optimization.md) — what to do when
  the energy functional is not convex.
- [01-09-07 Boundary Value Problems](../09-partial-differential-equations/07-boundary-value-problems.md) —
  the indirect route, and the boundary conditions compared here.
- [01-08-05 Sturm–Liouville Theory](../08-ordinary-differential-equations/05-sturm-liouville.md) —
  the eigenproblem whose variational form is the Rayleigh quotient.
- [01-18 Inverse Problems](../../18-inverse-problems/README.md) — variational
  formulations with regularisation and priors.
