---
id: 03-07-01
title: "Symbolic Variables, Expressions and Assumptions"
level: intermediate
prereqs: ["03-01-04", "01-01-01"]
estimated_minutes: 90
tags: [sympy, symbolic-computation, exact-arithmetic, assumptions]
---

# Symbolic Variables, Expressions and Assumptions

Every formula in geophysics exists twice: once as a derivation, on paper, and
once as code, on a machine. Keeping the two in agreement is a manual chore that
humans perform badly, and the mistakes it produces — a dropped factor, a sign
flipped in the third term of an expansion — are exactly the mistakes that survive
review, because the code runs and the number looks plausible.

Symbolic computation removes the chore by making the derivation executable.
Everything a numerical library does to *numbers*, SymPy does to *expressions*:
$\sqrt{x^2}$ stays a square root until you tell it what $x$ is, $\frac{1}{3}$
stays a ratio of integers forever, and differentiating a potential is a function
call rather than a finite difference with a step size to defend.

This lesson is about the two ideas that make it work: **exact representations**
and **assumptions**. Both are demonstrated with measured output; run the
demonstration first.

```bash
.venv/bin/python 03-scientific-computing/07-sympy/code/symbolic_basics_demo.py
```

## Learning objectives

By the end of this lesson you will be able to:

1. **Declare** symbols with the assumptions a derivation actually uses, and
   **predict** how each assumption changes the result.
2. **Explain** why $\sqrt{x^2}$ has three different answers depending on what is
   known about $x$, with the measured outputs.
3. **Perform** exact arithmetic on rationals and compare it with binary floating
   point on cases where the float fails.
4. **Recover** the rational a float was intended to represent, and **state** when
   that recovery is legitimate and when it destroys information.
5. **Evaluate** a symbolic result to arbitrary precision, and **say** what
   precision does and does not establish.
6. **Choose** between `simplify` and a named transformation, with the operation
   counts that justify the choice.

## Prerequisites

- [03-01-04 Functions, Scope, Modules and Packages](../01-python-fundamentals/04-functions-modules.md)
  — the import and call model SymPy uses.
- [01-01-01 Number Systems, Precision and Scientific Notation](../../01-mathematics/01-arithmetic/01-number-systems-and-precision.md)
  — exact versus measured numbers, and why over-reported digits are a form of
  dishonesty. That lesson's arithmetic is re-derived here from the symbolic side.

## 1. Intuition: an expression is a program you have not run yet

A numerical library evaluates immediately. `math.sqrt(x**2)` takes a float and
returns a float; the intermediate expression never exists. SymPy does the
opposite: it builds a tree, and evaluation is an explicit act (`subs`, `evalf`,
`lambdify`). Between construction and evaluation you can inspect the tree,
differentiate it, simplify it, or ask what it is equal to.

That change of order — build, manipulate, then evaluate — is the whole idea. It
buys three things:

- **Exactness where it matters.** A rational stays exact; a symbol stays symbolic.
- **Structure you can query.** `count_ops`, `free_symbols`, `latex`.
- **One source for many consumers.** A derivation written once can be printed as
  LaTeX, evaluated for a scalar, vectorised for arrays, or emitted as C —
  the subject of [lesson 05](./05-code-generation.md).

It costs two things: speed, and the need to state what you know.

## 2. Precise definitions

**Symbol.** A named variable with an *assumption set*. `sp.Symbol("x")` knows
nothing about `x`; `sp.Symbol("x", positive=True)` knows it is positive.

**Assumption.** A predicate attached to a symbol that a simplification may use.
The demonstration printed the assumption sets for four declarations:

```
  Symbol('x')                  ->  1 assumptions: commutative
  Symbol('x', real=True)       ->  8 assumptions: commutative, complex,
                                   extended_real, finite, hermitian, real, ...
  Symbol('x', positive=True)   -> 12 assumptions: ..., nonnegative, nonzero,
                                   positive, real
  Symbol('n', integer=True)    ->  9 assumptions: ..., integer, rational, real
```

The counts are not decoration. Each assumption is a fact that the simplifier is
allowed to use, so declaring one you do not have is how a symbolic system
produces a confidently wrong answer.

**Expression.** An immutable tree of symbols, numbers and operations.

**Exact number.** `sp.Rational`, `sp.Integer`, `sp.sqrt(2)`, `sp.pi`. These are
*not* floats; they carry their full value.

**`nsimplify`.** A function that guesses the simplest exact expression consistent
with a float, subject to a tolerance.

**`evalf(n)` / `N(expr, n)`.** Evaluate to `n` decimal digits using `mpmath`.

## 3. Assumptions change the answer, with the measured cases

The demonstration evaluates six expressions under three declarations:

```
  sqrt(x**2), x unconstrained  -> sqrt(x**2)
  sqrt(x**2), x real           -> Abs(x)
  sqrt(x**2), x positive       -> x
  cos(n*pi), n integer         -> (-1)**n
  Abs(x), x positive           -> x
  log(exp(x)), x real          -> x
```

Three lessons in six lines:

- **The unconstrained case is not a failure.** SymPy is refusing to guess, which
  is the correct behaviour. If the answer depended on the sign of $x$, a
  numerical library would have silently chosen a branch.
- **`real=True` is weaker than people expect.** For real $x$,
  $\sqrt{x^2} = |x|$, which is still not $x$. Statements of the form "it's real,
  so the root is the variable" are a common source of sign errors in potential
  and elasticity derivations.
- **Integer assumptions expose periodic structure.** $\cos(n\pi) = (-1)^n$ for
  integer $n$, which is what makes Fourier series arguments and Newtonian
  multipole expansions simplify rather than stall.

### 3.1 A worked derivation with an assumption that does work

The mean density of a spherically symmetric Earth follows from surface gravity
alone. With $\rho$, $G$, $R$ positive symbols and $g$ the measured surface value,

$$g = \frac{4}{3}\pi G \rho R \quad\Longrightarrow\quad \rho =
\frac{3g}{4\pi G R}.$$

The demonstration solves it symbolically and prints the LaTeX:

```
  solving g = (4/3) pi G rho R for rho:
      rho = \frac{3 g}{4 G R \pi}
```

Then evaluates with measured constants:

```
  g = 9.80665 m/s^2, R = 6.3710e+06 m, G = 6.67430e-11 m^3 kg^-1 s^-2
      rho = 5505.8 kg m^-3
  PREM mean density (textbook reference value, not measured here): 5514.0 kg m^-3
      difference = -8.2 kg m^-3 (0.15 %)
```

The dimensional check, done once by hand:

$$[\rho] = \frac{\mathrm{m\,s^{-2}}}{\mathrm{m^3\,kg^{-1}\,s^{-2}}\cdot
\mathrm{m}} = \mathrm{kg\,m^{-3}}.$$

The 0.15 % residual has two contributions — the centripetal acceleration at the
equator, which this formula ignores, and the fact that the Earth is not uniform.
**I have not separated them here, so I do not attribute the 0.15 % to either.**
That is the honest reading of a two-effect residual from a one-effect model.

## 4. Exact arithmetic against binary floating point

The demonstration's measurements:

```
  Rational(1, 3): 1/3  (exact ratio of two Python ints)
  3 * Rational(1,3) == 1                 : True
  3 * (1/3) == 1 in binary64             : True
      ^ measured True: rounding hid the error here, which is why
      'it worked in my test' is not evidence that a float is exact.
  0.1 + 0.2 == 0.3 in binary64           : False
      0.1 + 0.2 - 0.3 = 5.551e-17
  Rational(0.1) - Rational(1,10) exactly : 1/180143985094819840
      as a decimal: 5.551e-18, relative 5.551e-17
  Rational(10)**16 + 1 - Rational(10)**16 : 1
  1e16 + 1.0 - 1e16 in binary64           : 0.0
  Exact value of float 1/3 as a rational: 6004799503160661/18014398509481984
```

Four things to read out of it.

**Float failure is not automatic.** `3 * (1/3)` *is* exactly 1.0 in binary64,
because the rounding error of the literal $\frac13$ round-trips through the
multiplication. A test suite that happens to use such an expression will pass,
which is exactly why "it worked in my test" is not evidence.

**Floats fail predictably.** $0.1 + 0.2 \neq 0.3$, with the measured discrepancy
$5.551\times10^{-17}$. The exact size of that error is a rational with a
denominator of $2^{54}$:

$$0.1 + 0.2 - 0.3 = \frac{1}{180143985094819840}
= \frac{1}{2^{54}}.$$

**The failure has a scale.** $10^{16} + 1 - 10^{16} = 0$ in binary64, because
$\epsilon \cdot 10^{16} = 2.2 > 1$: the $+1$ is below the spacing of
representable numbers at that magnitude. Symbolically the answer is exactly 1.

**A float is a rational.** `Rational(1/3)` returns
$6004799503160661/18014398509481984$, the *exact* value of the binary64 number,
not $\frac13$. This is the distinction that matters for `nsimplify`: reading a
float exactly and guessing what it meant are different operations.

### 4.1 When to recover a rational, and when not to

```
  Rational(0.1)  = 3602879701896397/36028797018963968
      denominator = 36028797018963968 = 2**55, the signature of a binary float
  nsimplify(0.1) = 1/10
  nsimplify(0.1000000000001) = 1/10
```

A denominator that is a power of two is the signature of a binary float — a
useful diagnostic in its own right. `nsimplify` maps both $0.1$ and
$0.1000000000001$ onto $\frac{1}{10}$, which is right for a hand-typed constant
and wrong for a measurement. The rule: **`nsimplify` for constants a human
wrote, never for data.** On data it will manufacture a clean fraction from a
genuinely messy value, and the cleanliness will look like insight.

## 5. Precision versus accuracy

```
  sympy N(pi, 50)          : 3.1415926535897932384626433832795028841971693993751
  mpmath.nstr(mp.pi, 50)   : 3.1415926535897932384626433832795028841971693993751
  characters in agreement  : 51
  math.pi (binary64)       : 3.141592653589793
  measured |math.pi - pi|  = 1.225e-16
  decimal places of agreement for the binary64 value: 15.91
```

Fifty digits are available on demand and they are the right fifty digits. Binary64
carries about 16 significant digits of $\pi$, measured as 15.91 decimal places of
agreement.

The distinction this lesson insists on:

- **Precision** is how many digits a representation carries.
- **Accuracy** is how close a value is to the truth of the *model*.

A 50-digit evaluation of a formula whose derivation is wrong is a
50-digit-wrong answer. This is the same point as in
[01-01-01](../../01-mathematics/01-arithmetic/01-number-systems-and-precision.md),
made mechanical: SymPy can give you more digits, and it cannot tell you whether
you wanted them.

## 6. What `simplify` buys, counted

```
  rational cancellation        ops   4 ->   1   (x**2 - 1)/(x - 1)  ->  x + 1
  Pythagorean identity         ops   5 ->   0   sin(x)**2 + cos(x)**2  ->  1
  exponential addition         ops   7 ->   0   exp(x)*exp(y)*exp(-x - y)  ->  1
  expansion of a fourth power  ops   2 ->   2   (x + 1)**4  ->  (x + 1)**4
  cancel() named explicitly      : x + 1 (ops 1)
  verification: cancel(...) - (x + 1) simplifies to 0
```

`simplify` is a heuristic search over rewrite rules. It succeeded three times and
did nothing on the fourth, which is correct: $(x+1)^4$ expanded is longer, so
there is nothing to simplify. When you know which identity you want, name it —
`cancel`, `trigsimp`, `expand`, `factor`, `powsimp`, `radsimp` — and **verify the
result by substitution**, as the last line does. A verification that simplifies
to exactly 0 is stronger than any tolerance.

## 7. Assumptions and limitations

- **Assumptions are trusted, not checked.** `Symbol("x", positive=True)` will
  happily accept a negative substitution later. SymPy does not police you.
- **Exact arithmetic grows.** A long chain of rational operations accumulates
  numerator and denominator digits; evaluate to a float before storing in an
  array.
- **`simplify` can be slow and can fail to terminate** on expressions with many
  special functions. Bound the work with a named transformation.
- **Symbolic ≠ general.** A symbolic result is only as general as the
  assumptions its symbols carry and the branches it kept. A simplification that
  assumed $x > 1$ is invalid for $x < 1$, and SymPy will not say so.
- **Branch cuts are real.** $\log$ and $\sqrt$ have branches; `log(exp(x)) = x`
  holds under `real=True` here, and fails in the complex plane. Whether that
  matters is a physics question.
- **No timing claims.** Everything quoted is an operation count, a digit count or
  an exact value; no wall-clock measurements are reported, because they are
  machine-dependent.

## 8. Worked examples

### 8.1 Free-air versus Bouguer gradients, symbolically

Consider two one-line models for the vertical gradient of gravity above the
surface: free air (no mass between the stations) and Bouguer (a slab of density
$\rho$ in between):

$$g_{\mathrm{FA}}(h) = g_0 - \frac{2g_0}{R}h, \qquad
g_{\mathrm{B}}(h) = g_{\mathrm{FA}}(h) + 2\pi G\rho h.$$

Their difference is the slab term $2\pi G \rho h$, linear in $h$, so a symbolic
subtraction returns it exactly:

```python
h, rho, G, g0, R = sp.symbols("h rho G g_0 R", positive=True)
g_fa = g0 - 2 * g0 * h / R
g_b = g_fa + 2 * sp.pi * G * rho * h
print(sp.simplify(g_b - g_fa))
```

The output is $2 \pi G \rho h$ — no residual, no tolerance. With $\rho = 2670\
\mathrm{kg\,m^{-3}}$ and $h = 100\ \mathrm{m}$ this is the
$1.119637\times10^{-4}\ \mathrm{m\,s^{-2}}$ measured in
[03-06-04](../06-jupyter-and-notebooks/04-notebooks-to-scripts.md), i.e. 11.196
mGal. The symbolic subtraction is what proves the two models differ by exactly
that term and not by a numerical approximation of it.

### 8.2 A dimensional analysis that only works symbolically

Given the geotherm of a conductively cooling half-space in the similarity
variable, the surface heat flux is

$$q_0(t) = \frac{k\,\Delta T}{\sqrt{\pi \kappa t}},$$

and the *ratio* of fluxes at two times is

$$\frac{q_0(t_1)}{q_0(t_2)} = \sqrt{\frac{t_2}{t_1}}.$$

SymPy returns exactly that, with the units cancelling symbolically. Numerically,
you would compute two fluxes and their ratio, each with its own rounding, and
the exact relation would be recovered only to a few ulp. When a relation is
*exact*, it is worth deriving exactly — it becomes an assertion you can test with
zero tolerance. The demonstration's verification line
(`cancel(...) - (x + 1) simplifies to 0`) is the same technique.

## 9. Python demonstration

`code/symbolic_basics_demo.py` runs in six parts:

| Part | Establishes | Measured key |
|---|---|---|
| 1 | Assumptions change results | `sqrt(x**2)` → `sqrt(x**2)`, `Abs(x)`, `x` |
| 2 | Exact vs binary arithmetic | `0.1 + 0.2 - 0.3 = 5.551e-17`; rationale exact |
| 3 | Recovering rationals | `Rational(0.1)` has denominator $2^{55}$ |
| 4 | Precision | 51 characters agree with `mpmath` |
| 5 | A full derivation | `rho = 5505.8 kg m^-3`, 0.15 % from 5514.0 |
| 6 | `simplify` versus named transforms | ops 4→1, 5→0, 7→0, 2→2 |

The demonstration imports `sympy 1.14.0` and reports `mpmath.mp.dps = 15` as the
default; the 50-digit block raises that to 50 explicitly.

## 10. Exercises

Solutions are in
[`exercises/01-symbolic-basics-solutions.md`](./exercises/01-symbolic-basics-solutions.md).

### ★ Foundational

**★1.** For each expression, say what SymPy returns with the symbol declared
(a) unconstrained, (b) `real=True`, (c) `positive=True`:
(i) $\sqrt[3]{x^3}$ (ii) $|x|$ (iii) $\sqrt{x}\sqrt{x}$ (iv) $e^{\ln x}$.

**★2.** Compute by hand and then with SymPy: $\frac{1}{7} \times 7$,
$\frac{1}{7}$ as a binary64, and the difference between the two as an exact
rational.

**★3.** Convert to exact rationals: (a) 0.375, (b) 2.5, (c) 0.1. Which of these
is exactly representable in binary64, and how can you tell from the denominator?

**★4.** The demonstration prints `mpmath.mp.dps = 15` rather than assuming a
value. Explain why a numeric claim about precision has to be measured in the
session that makes it, and give one way the default could differ.

### ★★ Applied

**★★5.** Declare symbols for the density, radius and gravitational constant of a
planet and derive the surface gravity of a uniform sphere symbolically. Evaluate
for Mars ($R = 3.390\times10^{6}$ m, $\rho = 3933\ \mathrm{kg\,m^{-3}}$,
$G = 6.67430\times10^{-11}$) and compare with the measured surface gravity
$3.71\ \mathrm{m\,s^{-2}}$. Report the discrepancy and two reasons for it.

**★★6.** Derive the depth at which a two-layer Earth model has equal
contributions from the free-air and slab terms, symbolically, and evaluate it for
$\rho = 2670\ \mathrm{kg\,m^{-3}}$. State the result in metres with the figures
the inputs justify.

**★★7.** Show symbolically that $\sin^2\theta + \cos^2\theta = 1$ only after
`trigsimp`, and report the operation counts before and after. Then show which
single named function gives the same result and whether it is faster to state.

**★★8.** Using `nsimplify`, demonstrate one case where it recovers the intended
constant and one where it destroys a genuinely different value. Report both
inputs and outputs, and state the rule you would apply.

### ★★★ Research-oriented

**★★★9.** Derive the mean density of a two-layer Earth (crust of density
$\rho_1$ to depth $d$, mantle of density $\rho_2$ below) symbolically, then solve
for the mantle density given the PREM mean of $5514\ \mathrm{kg\,m^{-3}}$, a
crustal density of $2700\ \mathrm{kg\,m^{-3}}$, and a crustal thickness of 35 km.
Report the exact rational if one arises, the float, and the number of significant
figures the inputs justify.

**★★★10.** Quantify the growth of exact rational arithmetic. Build
$S_n = \sum_{k=1}^{n} \frac{1}{k}$ symbolically for $n = 10, 10^2, 10^3$, and
report for each: the number of digits in the numerator and denominator of the
exact sum, the value to 20 digits, and the time-free operation count
(`count_ops`). State where you would stop using exact arithmetic and why.

## 11. Common mistakes

1. **Declaring assumptions you do not have.** The simplifier believes you.
2. **Using `simplify` as a general-purpose fixer.** Name the transformation.
3. **Treating `sqrt(x**2)` as `x`.** It is $|x|$ for real $x$.
4. **`nsimplify` on measured data.** It will invent a clean fraction.
5. **Confusing precision with accuracy.** 50 digits of a wrong model.
6. **Forgetting that exact arithmetic grows.** Rationals become enormous; evaluate
   before storing.
7. **Comparing symbolic results with `==`.** Use `simplify(a - b) == 0`, or
   `sp.simplify(sp.Eq(a, b))`.
8. **Assuming branch cuts do not matter.** They do the moment a variable goes
   complex.

## 12. Real-world applications

- **Deriving an analytic anomaly.** The gravitational attraction of a prism is
  derived once, symbolically, and then evaluated for a survey — the subject of
  [lesson 05](./05-code-generation.md).
- **Error propagation.** A formula differentiated symbolically gives the
  sensitivity coefficients for an error budget without a finite-difference step
  size to choose.
- **Unit and dimensional checks.** Symbolic simplification of ratios cancels
  units exactly, which is how the free-air/Bouguer difference above is proved
  rather than tested.
- **Model comparison.** Two competing approximations subtracted symbolically give
  their exact difference, which is the cleanest way to state what a model adds.
- **Teaching.** Students see an assumption change an answer, which makes the role
  of assumptions concrete rather than abstract.

## 13. Further reading

- **SymPy documentation** (sympy.org). Level: beginner to intermediate. The
  tutorial's "Basic Operations", "Simplification" and "Assumptions" sections map
  directly onto Sections 2–6.
- **Meurer, A. et al. (2017). SymPy: symbolic computing in Python. *PeerJ
  Computer Science*, 3, e103.** Level: intermediate. The design and architecture
  of the library, including the assumption system.
- **mpmath documentation.** Level: intermediate. Arbitrary-precision arithmetic
  and the `nstr` used in Section 5.
- **Goldberg, D. (1991). What every computer scientist should know about
  floating-point arithmetic. *ACM Computing Surveys*, 23(1), 5–48.** Level:
  intermediate. The reference behind Section 4; check your library for access.
- **Higham, N. J. (2002). *Accuracy and Stability of Numerical Algorithms* (2nd
  ed.). SIAM.** Chapters 1–2. Level: advanced. The error analysis that explains
  why the exact-rational route is worth its cost.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text.

## 14. Related lessons

- [02 Symbolic Differentiation, Integration and Limits](./02-symbolic-calculus.md)
  — what to do with the expressions built here.
- [03 Symbolic Solvers for Algebraic and Differential Equations](./03-solving-equations.md)
- [04 Symbolic Tensors and Index Notation](./04-tensor-symbolic.md)
- [05 Generating Fast Numerical Code from Symbolic Results](./05-code-generation.md)
- [01-01-01 Number Systems, Precision and Scientific Notation](../../01-mathematics/01-arithmetic/01-number-systems-and-precision.md)
  — the numerical counterpart of Section 4.

## 15. Self-assessment checklist

- [ ] I can declare a symbol with exactly the assumptions a derivation uses. (§2)
- [ ] I can predict what $\sqrt{x^2}$ returns under three assumptions. (§3)
- [ ] I can state the exact value of $0.1 + 0.2 - 0.3$ as a rational. (§4)
- [ ] I can tell a hand-typed constant from a measurement in a float. (§4.1)
- [ ] I can say what 50-digit precision does and does not establish. (§5)
- [ ] I can choose `simplify` or a named transformation and justify it. (§6)
- [ ] I can verify a symbolic identity by simplifying a difference to zero. (§6)
