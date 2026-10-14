# Module 01-02 — Algebra, Functions and Modelling

**Stages:** beginner → intermediate · **Prerequisites:**
[Module 01-01 Arithmetic and Numerical Reasoning](../01-arithmetic/README.md)

This module is where mathematics starts to *describe* the Earth. Algebra is the
grammar of physical laws: rearranging an equation is how you turn a measured
travel time into a depth, a decay series into a date, an anomaly into a mass.
Functions are the shapes those laws take, and the four families that dominate
geophysics — linear, polynomial, exponential and logarithmic — are the ones you
will meet again in seismology, geochronology, hydrology, heat flow and potential
fields.

The module is deliberately hands-on. Every lesson contains a runnable
demonstration, and every demonstration uses synthetic data generated from a
stated model, so you can check the recovery of the parameters exactly rather than
taking a number on trust.

## Learning objectives

By the end of this module you will be able to:

1. Rearrange an equation for any symbol, solve linear, quadratic and
   exponential equations, and check each solution by substitution.
2. Read a function's domain, range, symmetry, monotonicity and asymptotes from
   its formula and its graph, and predict how a transformation moves the graph.
3. Convert between exponential and logarithmic form, and apply decay and growth
   laws to radiometric dating, geothermal gradients, attenuation and Newton
   cooling.
4. Locate the roots of a polynomial by closed form, bisection or Newton's method,
   and explain what happens when a root is repeated or nearly repeated.
5. Solve small linear systems exactly, solve nonlinear systems by Newton's
   method, and explain when a system has no solution, many solutions, or an
   ill-conditioned one.

## Lessons

| # | Lesson | Level | Key idea |
|---|---|---|---|
| 01 | [Algebraic Manipulation and Solving Equations](./01-algebraic-manipulation.md) | beginner | Rearranging is the core skill; always substitute back |
| 02 | [Functions, Graphs and Transformations](./02-functions-and-graphs.md) | beginner | A function is a rule plus a domain; the graph is the rule made visible |
| 03 | [Exponentials, Logarithms and Decay Laws in Earth Science](./03-exponentials-logarithms.md) | beginner | Multiplicative change becomes linear in the logarithm |
| 04 | [Polynomials, Roots and Asymptotic Behaviour](./04-polynomials-roots.md) | beginner | Local shape from roots, global shape from the leading term |
| 05 | [Linear and Nonlinear Systems of Equations](./05-systems-of-equations.md) | intermediate | More equations than unknowns is the normal geophysical situation |

## Suggested path

**If you are new to algebra:** all five lessons in order, doing the exercises on
paper and then the code demonstrations. Budget 8–12 hours.

**If you are returning to algebra after a break:** attempt
[01-02-01](./01-algebraic-manipulation.md) exercises ★1–★4 and
[01-02-03](./03-exponentials-logarithms.md) exercises ★★5–★★6 first. If those are
comfortable, start at [01-02-04](./04-polynomials-roots.md).

**If you already use algebra routinely:** read
[01-02-05](./05-systems-of-equations.md) for the linear-versus-nonlinear
distinction and the non-uniqueness example, then continue to
[01-03 Trigonometry](../03-trigonometry/README.md).

## Materials in this module

| Path | Contents |
|---|---|
| [`01-algebraic-manipulation.md`](./01-algebraic-manipulation.md) | Lesson 01 — rearranging and solving |
| [`02-functions-and-graphs.md`](./02-functions-and-graphs.md) | Lesson 02 — domains, graphs, transformations |
| [`03-exponentials-logarithms.md`](./03-exponentials-logarithms.md) | Lesson 03 — decay laws and logarithms |
| [`04-polynomials-roots.md`](./04-polynomials-roots.md) | Lesson 04 — roots, multiplicity, asymptotics |
| [`05-systems-of-equations.md`](./05-systems-of-equations.md) | Lesson 05 — linear and nonlinear systems |
| [`exercises/`](./exercises/) | Ten graded exercises and worked solutions for each lesson |
| [`code/algebraic_manipulation_demo.py`](./code/algebraic_manipulation_demo.py) | Solving, checking, extraneous roots, no-division-by-zero |
| [`code/functions_demo.py`](./code/functions_demo.py) | Function tables, transformations, ASCII plots, asymptotics |
| [`code/exponential_decay_demo.py`](./code/exponential_decay_demo.py) | Radiometric dating, attenuation, Newton cooling, log-linear fitting |
| [`code/polynomials_roots_demo.py`](./code/polynomials_roots_demo.py) | Horner evaluation, bisection, Newton, root sensitivity |
| [`code/systems_demo.py`](./code/systems_demo.py) | Gaussian elimination, ill-conditioning, nonlinear Newton inversion |

## Mastery checkpoint

Complete this without notes.

> A radioactive parent decays with half-life $T$. **(a)** Write the decay law and
> express the decay constant in terms of $T$. **(b)** Solve for the age $t$ in
> terms of the measured ratio $D/P$ of daughter to parent, assuming no initial
> daughter. **(c)** A sample gives $D/P = 0.5$ with $T = 4.468\times10^{9}$ yr;
> compute the age. **(d)** Rewrite the decay law in a form that is linear in $t$,
> and explain why that form is the one you would fit to a data series.
> **(e)** State two assumptions your age calculation makes, and say what happens
> to the answer if each is violated.

A worked version of parts (a)–(d) appears in
[lesson 01-02-03](./03-exponentials-logarithms.md), Section 5, and in the
solutions for
[exercise ★★6 of lesson 01-02-03](./exercises/03-exponentials-logarithms-solutions.md).

## Common pitfalls across this module

1. **Dividing by something that can be zero.** Velocities, density contrasts and
   gradients all vanish in real data; check before dividing.
2. **Squaring without substituting back.** Squaring is not an equivalence
   transformation and creates extraneous roots.
3. **Confusing a function with its formula.** The domain is part of the function,
   and the same formula on a different domain is a different function.
4. **Treating a straight line on a log plot as proof of an exponential law.** A
   power law also looks straight on log–log axes; plot the residual and check the
   domain before concluding.
5. **Believing that one solution is the solution.** Nonlinear systems can have
   several solutions, and the one Newton finds depends on where you start.

## Related modules

- [01-01 Arithmetic and Numerical Reasoning](../01-arithmetic/README.md) — the
  numerical habits this module assumes.
- [01-03 Trigonometry and Periodic Phenomena](../03-trigonometry/README.md) — the
  next mathematical step, and the language of waves.
- [02-physics](../../02-physics/README.md) — where these functions acquire
  physical meaning.
- [01-13 Probability and Statistics Foundations](../13-probability-and-statistics-foundations/README.md)
  — fitting the functions of this module to noisy data.
