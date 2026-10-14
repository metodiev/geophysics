---
id: 01-02-04
title: "Polynomials, Roots and Asymptotic Behaviour"
level: beginner
prereqs: ["01-02-02"]
estimated_minutes: 75
tags: [polynomials, roots, newton-method, asymptotics]
---

# Polynomials, Roots and Asymptotic Behaviour

## Learning objectives

By the end of this lesson you will be able to:

1. **Read** a polynomial's global behaviour from its leading term and its local
   behaviour from its roots.
2. **Evaluate** a polynomial accurately and efficiently by Horner's rule, and say
   why the nested form is better than the expanded one.
3. **Find** roots by factoring, by the quadratic formula, by bisection and by
   Newton's method, and state what each method guarantees.
4. **Explain** how the convergence rate of Newton's method degrades from
   quadratic to linear at a repeated root.
5. **Quantify** how sensitive a root is to a perturbation of a coefficient, and
   connect that sensitivity to the conditioning of the problem.

## Prerequisites

[01-02-02 Functions, Graphs and Transformations](./02-functions-and-graphs.md) for
the polynomial family, and
[01-02-01 Algebraic Manipulation and Solving Equations](./01-algebraic-manipulation.md)
Section 5.5 for the refraction calculation reused here.

## 1. Intuition: polynomials are the local language of approximation

A polynomial is built from additions and multiplications only — which is exactly
what a computer does fastest and most accurately. That is why polynomials appear
in three different roles in geophysics:

- **As physical models** in their own right: a density that varies linearly with
  depth, a velocity that varies quadratically, a temperature profile fitted by a
  quadratic in a borehole.
- **As local approximations** to functions that are not polynomials: a truncated
  Taylor series *is* a polynomial, and the demonstration shows how its accuracy
  collapses outside a limited range.
- **As the expression of a root-finding problem**: "at what depth does this
  anomaly vanish?", "where does the head wave overtake the direct arrival?",
  "what velocity makes this misfit stationary?"

The practical content of the lesson is therefore: read the shape, find the roots,
and know how accurately either can be done.

## 2. Definitions

A **polynomial** of degree $n$ is

$$p(x) = a_nx^{n} + a_{n-1}x^{n-1} + \cdots + a_1x + a_0, \qquad a_n \ne 0.$$

- $a_n$ is the **leading coefficient**; $a_nx^{n}$ is the **leading term**.
- A **root** (or zero) is a value $r$ with $p(r) = 0$.
- The **multiplicity** of a root $r$ is the largest $m$ with $(x-r)^{m}$ dividing
  $p$ exactly. A root of multiplicity 1 is **simple**; multiplicity $>1$ is
  **repeated**.

**Factor theorem.** $r$ is a root of $p$ if and only if $(x - r)$ is a factor of
$p$. This is the bridge between solving $p(x) = 0$ and factoring $p$.

**Fundamental theorem of algebra.** A degree-$n$ polynomial has exactly $n$ roots
in the complex plane, counted with multiplicity. Over the *real* numbers it may
have fewer — a quadratic with negative discriminant has none.

## 3. Reading a polynomial

### 3.1 Global behaviour: the leading term

For large $|x|$ the leading term dominates:

$$p(x) \sim a_nx^{n} \quad \text{as } |x| \to \infty.$$

So the **end behaviour** is set by $n$ (odd polynomials go opposite ways at the
two ends; even polynomials go the same way) and by the sign of $a_n$. On a table,
$p(-1) = -24$ and $p(4) = +6$ for $p(x) = x^{3}-6x^{2}+11x-6$: an odd polynomial
with a positive leading coefficient runs from $-\infty$ to $+\infty$.

### 3.2 Local behaviour: the roots and their multiplicity

Between consecutive simple roots the sign of $p$ alternates. At a root of
**even** multiplicity the graph touches the axis and turns back; at **odd**
multiplicity it crosses. This is why a "double root" is numerically awkward: near
it, the graph is flat, and a small change in the coefficients moves the root a
long way — quantified in Section 5.4.

### 3.3 Turning points

A degree-$n$ polynomial has at most $n-1$ turning points. Equivalently, between
any two distinct real roots there is at least one stationary point (Rolle's
theorem), which is the standard argument for why fitting a high-degree polynomial
through noisy data is dangerous: it will invent oscillations between the data
points.

## 4. Evaluating and solving

### 4.1 Horner's rule

Evaluate by nesting:

$$p(x) = \bigl((a_nx + a_{n-1})x + a_{n-2}\bigr)x + \cdots + a_0.$$

This uses $n$ multiplications and $n$ additions — no powers, and fewer roundings.
The demonstration evaluates $p(x) = x^{3}-6x^{2}+11x-6$ at $x = 2.0000000001$:

| method | value |
|---|---|
| expanded powers | $-1.000017846309\times10^{-10}$ |
| Horner | $-1.000000082740\times10^{-10}$ |

The two differ by $1.8\times10^{-15}$, i.e. a few ulps of the true value
$-1.0\times10^{-10}$. The point is not that Horner is dramatically more accurate
here, but that it is always at least as accurate and strictly cheaper. There is no
reason ever to evaluate a polynomial the other way.

### 4.2 Bisection: slow, certain

If $p$ is continuous and $p(a)p(b) < 0$, there is a root in $(a,b)$. Bisection
halves the interval repeatedly:

$$|x_n - r| \le \frac{b-a}{2^{n}},$$

so each iteration buys exactly one **bit**. Solving $x^{3}-x-2 = 0$ on $[1,2]$
with a tolerance of $10^{-14}$ takes 46 iterations and gives
$1.521379706804574$. Bisection cannot fail and cannot be fooled; it is also
unbearably slow, and it finds *a* root, not a specified one.

### 4.3 Newton's method: fast, conditional

$$x_{k+1} = x_k - \frac{p(x_k)}{p'(x_k)}.$$

Newton needs a derivative, a starting point, and a root where $p' \ne 0$. When it
works, it converges **quadratically**: the number of correct digits roughly
doubles each step. The same cubic, started from $x_0 = 1.5$, converges in 4 steps
to $1.521379706804568$:

| step | $x_k$ | $|e_k|$ | $|e_k|/|e_{k-1}|^{2}$ |
|---|---|---|---|
| $0$ | $1.500000000000000$ | $2.138\times10^{-2}$ | — |
| $1$ | $1.521739130434783$ | $3.594\times10^{-4}$ | $0.7863$ |
| $2$ | $1.521379805964786$ | $9.916\times10^{-8}$ | $0.7676$ |
| $3$ | $1.521379706804575$ | $7.550\times10^{-15}$ | $0.7678$ |

The last column is nearly constant, which is the numerical signature of quadratic
convergence. Compare with bisection: 46 steps against 4.

## 5. Worked derivations

### 5.1 Newton's method from Taylor's theorem

Suppose $x_k$ is close to a root $r$ and write $r = x_k + h$ with $h$ small.
Taylor-expanding $p(r) = 0$ about $x_k$:

$$0 = p(x_k + h) \approx p(x_k) + h\,p'(x_k)
\qquad\Longrightarrow\qquad
h \approx -\frac{p(x_k)}{p'(x_k)}.$$

Newton's step is exactly this estimate. The error recurrence follows by keeping
the next term:

$$0 = p(x_k) + h p'(x_k) + \frac{h^{2}}{2}p''(x_k) + \cdots$$

and, since $e_k = r - x_k = h$ and $e_{k+1} = e_k - h_{\text{used}}$,

$$e_{k+1} \approx \frac{p''(r)}{2p'(r)}\,e_k^{2}.$$

The **square** on $e_k$ is why Newton's method is called quadratic: the error is
roughly squared each step, so the correct digits double.

### 5.2 Why a repeated root degrades Newton to linear

Let $p(x) = (x-r)^{m}q(x)$ with $q(r) \ne 0$ and $m \ge 2$. Then

$$p'(x) = m(x-r)^{m-1}q(x) + (x-r)^{m}q'(x),$$

so both $p$ and $p'$ vanish at $r$. Substituting into the error recurrence gives

$$e_{k+1} \approx \frac{m-1}{m}\,e_k,$$

a **linear** recurrence with ratio $(m-1)/m$: for $m = 2$ the ratio is $1/2$. The
demonstration confirms it for $g(x) = (x-2)^{2}(x+1)$: the measured ratios of
successive errors settle at $0.555556$, $0.536232$, $0.521607$, $\ldots$ and
approach $0.5$ monotonically. Each step now buys one binary digit instead of
doubling the digits, and it takes about 50 iterations to reach double precision
where a simple root needed 4.

**Practical rule.** If Newton crawls, look for a repeated or nearly repeated root,
or for a stationary point where $p' \approx 0$. Either reformulate the problem
(for example, find the root of $p'(x)$ and locate a well-conditioned combination),
or use a method that accounts for multiplicity.

### 5.3 Root sensitivity to a coefficient perturbation

How much does a root move when a coefficient changes? Let $r$ be a simple root and
perturb the coefficient $a_k$ of $x^{k}$ by $\delta a_k$. To first order,

$$0 = p(r + \delta r) + \delta a_k\,r^{k}
\approx p(r) + p'(r)\,\delta r + \delta a_k\,r^{k},$$

so, since $p(r) = 0$,

$$\delta r = -\frac{r^{k}}{p'(r)}\,\delta a_k.$$

The amplification factor is $|r^{k}/p'(r)|$. Two consequences:

- A **small derivative** at the root (a flat function, as at a repeated root)
  amplifies the perturbation without bound. As roots coalesce, $p'(r) \to 0$ and
  every root becomes infinitely sensitive.
- The factor grows with $|r|^{k}$: roots far from the origin are more sensitive to
  perturbations in the high-order coefficients.

**Check against the demonstration.** For $p(x) = x^{3}-6x^{2}+11x-6$ with a root at
$r = 2$: $p'(x) = 3x^{2}-12x+11$, so $p'(2) = 12-24+11 = -1$. Perturbing $a_2$
from $-6$ to $-6+\delta$ with $\delta = 10^{-6}$:

$$\delta r = -\frac{2^{2}}{-1}\times10^{-6} = +4\times10^{-6},$$

against a measured shift of $+4.000016\times10^{-6}$ — the amplification factor
is exactly 4, as predicted, and the small excess is the second-order term. The
same algebra is the reason
[01-01-05](../01-arithmetic/05-error-and-conditioning.md) describes root finding
as a conditioning problem, not an algorithmic one.

### 5.4 Asymptotic behaviour, and the difference between "big" and "big enough"

Asymptotics is the study of limits — but the limit is often reached only far away.
The profile of a buried point mass (equivalently, by Newton's shell theorem, of a
uniform sphere) is

$$g(x) = \frac{GMh}{(x^{2}+h^{2})^{3/2}}, \qquad
\frac{g(x)}{g(0)} = \left(1 + \frac{x^{2}}{h^{2}}\right)^{-3/2}.$$

In the far field $x \gg h$ the binomial expansion gives

$$g(x) \sim \frac{GMh}{x^{3}}, \qquad
\frac{g(x)x^{3}}{GMh} = 1 - \frac{3}{2}\frac{h^{2}}{x^{2}} + \cdots$$

The demonstration's measured values of that ratio are $0.942866$ at $x/h = 5$ and
$0.985185$ at $x/h = 10$: even at ten depths, the leading asymptotic term is only
good to 1.5%. Meanwhile the *peak* of the profile is exact and trivially
computed — $g(0) = GM/h^{2}$.

That asymmetry is the practical lesson of asymptotics: **use the exact form where
you have it, and use the asymptote only where you have verified its error.** Two
other numbers from the same family, both exact:

- $g(h)/g(0) = 1/(2\sqrt{2}) = 0.353553$: at an offset equal to the depth the
  anomaly has already fallen to 35% of its peak.
- The half-width at half maximum satisfies $x_{1/2} = h\sqrt{2^{2/3}-1}$, i.e.
  $h = 1.304766\,x_{1/2}$.

### 5.5 A truncated series is a polynomial

The Taylor polynomial of degree 2 for $e^{-x}$ about 0 is

$$T_2(x) = 1 - x + \frac{x^{2}}{2}.$$

The demonstration's comparison with the exact value:

| $x$ | $e^{-x}$ | $T_2(x)$ | relative error |
|---|---|---|---|
| $0.1$ | $0.904837418$ | $0.905000000$ | $1.80\times10^{-4}$ |
| $0.5$ | $0.606530660$ | $0.625000000$ | $3.05\times10^{-2}$ |
| $1.0$ | $0.367879441$ | $0.500000000$ | $0.359$ |
| $2.0$ | $0.135335283$ | $1.000000000$ | $6.39$ |
| $5.0$ | $0.006737947$ | $8.500000000$ | $1261$ |

The truncation is a good model for $x \lesssim 0.5$ and actively harmful beyond
$x \approx 2$, where the polynomial — which grows without bound — predicts a
*negative* quantity as a positive large one. Every approximation has a domain of
validity, and the polynomial does not know where its own ends. This is the reason
that series-based formulas in geophysics (inverse-problem linearisations, ray
approximations, small-parameter expansions) must be reported together with the
range over which the truncation error was checked.

### 5.6 Solving a root problem that comes from the field

The refraction crossover distance (derived in
[01-02-01](./01-algebraic-manipulation.md), Section 5.5) is

$$x_c = 2H\sqrt{\frac{v_2+v_1}{v_2-v_1}}
\qquad\Longrightarrow\qquad
H = \frac{x_c}{2}\sqrt{\frac{v_2-v_1}{v_2+v_1}}.$$

With $v_1 = 1200$ m/s, $v_2 = 3000$ m/s and $x_c = 60$ m: $H = 19.639610$ m by
the closed form, and $19.639610$ m by bisection on the residual
$x_c - 2H\sqrt{(v_2+v_1)/(v_2-v_1)}$ — agreement to all printed digits, and the
critical angle is $\theta_c = 23.5782^\circ$. The closed form is preferable when
it exists; the numerical method is the general tool, and having both is how you
validate a solver.

## 6. Python demonstration

```bash
python3 code/polynomials_roots_demo.py
```

`code/polynomials_roots_demo.py` uses only the standard library and contains its
own Horner evaluation, bisection and Newton implementations, so that the
convergence behaviour can be inspected rather than assumed. It covers: Horner
versus expanded evaluation; the quadratic formula; bisection and Newton on a
cubic, with the error history; the repeated-root slowdown; root sensitivity to a
coefficient; the point-mass profile and its asymptotics; Taylor truncation of
$e^{-x}$; and the refraction thickness from the closed form and by bisection.

Two outputs worth dwelling on:

```text
   0      1.500000000000000    2.138e-02
   1      1.521739130434783    3.594e-04                 0.7863
   2      1.521379805964786    9.916e-08                 0.7676
   3      1.521379706804575    7.550e-15                 0.7678
```

```text
coefficient of x**2 changed from -6 to -5.999999
root near 2: 2.000000000000001 -> 2.000004000016002
amplification = 4.0000
```

| Observation | Consequence in geophysics |
|---|---|
| Newton needs 4 steps, bisection 46 | use Newton where the derivative is cheap; keep bisection for safety |
| the error ratio settles at 0.77 | quadratic convergence is visible in the data, not just the textbooks |
| repeated root ⇒ ratio 0.5 | a flat misfit surface makes inversion slow and ill-conditioned |
| a $10^{-6}$ coefficient change moves the root by $4\times10^{-6}$ | root positions are only as good as the coefficients, amplified by $|r^{k}/p'|$ |
| $T_2$ is useless at $x = 5$ | state the range over which a series expansion was validated |

## 7. Exercises

Ten graded exercises with worked solutions are in
[`exercises/04-polynomials-roots-exercises.md`](./exercises/04-polynomials-roots-exercises.md)
and
[`exercises/04-polynomials-roots-solutions.md`](./exercises/04-polynomials-roots-solutions.md).

**★1.** For $p(x) = x^{3} - 6x^{2} + 11x - 6$: state the degree, the leading
coefficient and the end behaviour, and evaluate $p$ at $x = 0, 1, 2, 3, 4$.

**★★2.** Use the sensitivity formula $\delta r = -\delta a_k\,r^{k}/p'(r)$ to
predict the shift of the root at $r = 3$ when the constant term of
$x^{3}-6x^{2}+11x-6$ changes by $10^{-4}$, and verify numerically.

**★★★3.** Design an experiment that measures how the number of Newton iterations
needed to reach a relative error of $10^{-15}$ scales as two roots coalesce.
Report the method, the measured scaling and the limits of your conclusion.

## 8. Common mistakes

1. **Evaluating a polynomial with explicit powers.** Horner is cheaper and at
   least as accurate; there is no trade-off.
2. **Trusting a root from a solver without checking the residual.** Always
   evaluate $p$ at the answer.
3. **Using Newton where $p' \approx 0$.** At a repeated root, convergence degrades
   to linear; diagnose by watching the error ratio.
4. **Treating a repeated root as two roots.** It is one root with multiplicity two,
   and it is unstable to perturbations of the coefficients.
5. **Fitting a high-degree polynomial through scattered data.** The extra degrees
   of freedom create oscillations between the points, not information.
6. **Assuming an asymptotic form is valid at moderate separation.** The point-mass
   far field is only good to 1.5% at ten depths.
7. **Extrapolating a truncated series outside its validated range.** $T_2(x)$ for
   $e^{-x}$ fails completely by $x = 5$.

## 9. Real-world applications

- **Velocity and density profiles.** Polynomial (often linear or quadratic)
  approximations are used for well logs and for analytic rays; the accuracy of
  the approximation controls the accuracy of the arrival time.
- **Travel-time crossover and layer thickness.** A closed-form root problem in
  refraction surveying, Section 5.6.
- **Potential-field depth estimation.** Half-width rules and profile-shape
  relations are root/sensitivity problems; the calibration constant depends on the
  assumed body geometry.
- **Inversion as root finding.** Minimising a misfit means solving
  $\nabla m = 0$; Gauss–Newton is Newton's method applied to a vector equation,
  and its convergence behaviour is governed by the same algebra. See
  [01-14 Optimization](../14-optimization/README.md) and
  [18-inverse-problems](../../18-inverse-problems/README.md).
- **Instrument and filter design.** Polynomial approximations of responses are
  used throughout signal processing; their roots give poles and zeros of the
  filter. See [01-10 Fourier Analysis](../10-fourier-analysis/README.md).

## 10. Further reading

- **Higham, N. J. (2002). *Accuracy and Stability of Numerical Algorithms*
  (2nd ed.). SIAM.** Chapter 5 (polynomial evaluation) and Section 4.7 on
  Horner's rule and its error. Level: advanced undergraduate upward.
- **Trefethen, L. N. (2013). *Approximation Theory and Approximation Practice*.
  SIAM.** Level: advanced. The modern treatment of why polynomial approximation
  works where it does, and fails where it does; the source for the caution about
  high-degree fits.
- **Burden, R. L., & Faires, J. D. *Numerical Analysis* (current edition).**
  Chapters on solutions of equations in one variable and on error analysis for
  iterative methods. Level: intermediate. Standard on bisection, Newton and the
  convergence rates used here.
- **Stewart, J. *Calculus: Early Transcendentals* (current edition).** Chapters on
  polynomials, the factor theorem and Taylor polynomials. Level: beginner.

> Note on citations: bibliographic details are given so you can locate the works;
> editions vary and page numbers are deliberately omitted. This repository does
> not reproduce copyrighted text.

## 11. Related lessons

- [02 Functions, Graphs and Transformations](./02-functions-and-graphs.md) —
  Section 3.2 is the graphical prequel to Section 3 here.
- [03 Exponentials, Logarithms and Decay Laws](./03-exponentials-logarithms.md)
  — the other family you must be able to distinguish from a polynomial.
- [05 Linear and Nonlinear Systems of Equations](./05-systems-of-equations.md) —
  the multivariate version of root finding.
- [01-05 Single-Variable Calculus](../05-single-variable-calculus/README.md) —
  Taylor series, and the derivative used by Newton's method.
- [01-01-05 Absolute vs Relative Error, Conditioning and Stability](../01-arithmetic/05-error-and-conditioning.md)
  — the conditioning framework behind Section 5.3.

## Self-assessment checklist

- [ ] I can read end behaviour from the leading term.
- [ ] I can evaluate a polynomial by Horner's rule and explain the advantage.
- [ ] I can find a root by bisection and by Newton, and state the guarantee each
      provides.
- [ ] I can derive the quadratic convergence of Newton's method and explain the
      repeated-root exception.
- [ ] I can estimate how far a root moves when a coefficient changes.
- [ ] I can state the range over which a truncated series is valid, and how I
      would check it.
