---
id: 01-01-04
title: "Floating-Point Representation, Round-Off and Catastrophic Cancellation"
level: intermediate
prereqs: ["01-01-01"]
estimated_minutes: 75
tags: [floating-point, ieee754, round-off, cancellation, numerical-stability]
---

# Floating-Point Representation, Round-Off and Catastrophic Cancellation

## Learning objectives

By the end of this lesson you will be able to:

1. **Decode** an IEEE 754 binary64 value into its sign, exponent and
   significand, and say how many significant digits it can carry.
2. **Explain** why decimal values such as $0.1$ are not represented exactly,
   and state the exact value a computer actually stores.
3. **Predict** where round-off appears: representation, accumulation,
   cancellation, and comparison of computed values.
4. **Quantify** round-off using the model $\mathrm{fl}(a \odot b) =
   (a \odot b)(1+\delta)$, $|\delta| \le u$, and use it to bound a summation
   error.
5. **Choose** an algorithm that avoids introducing avoidable error (Kahan
   summation, the stable quadratic formula, a sensible step size for numerical
   differentiation) and explain why it is better.

## Prerequisites

[01-01-01 Number Systems, Precision and Scientific Notation](./01-number-systems-and-precision.md)
for significant figures and scientific notation. Some familiarity with
summation notation is assumed; no calculus is needed beyond a derivative.

## 1. Intuition: the computer does not store the real numbers

A real number is a mathematical object; a computer register holds a pattern of
bits. The set of values a double-precision register can hold is **finite**, and
its members are **not evenly spaced**. That single sentence is the whole source
of floating-point difficulty.

Two consequences follow immediately, and they are worth holding in mind for the
rest of the module:

- **Most decimal fractions are not representable.** $0.1$ cannot be written
  exactly in binary, exactly as $1/3$ cannot be written exactly in decimal.
- **The absolute gap between neighbouring values depends on magnitude.** Near
  $10^{16}$ the gap is $2.0$; near $1$ it is $2.2\times10^{-16}$. So arithmetic
  that is harmless at one scale can be destructive at another.

The rest of this lesson makes both statements precise and shows where they bite
in geophysical computing.

## 2. The binary64 model

### 2.1 Anatomy

Python's `float` is IEEE 754 **binary64** (also called double precision). A
value is stored in 64 bits:

| Field | Bits | Meaning |
|---|---|---|
| sign $s$ | 1 | $s = 0$ positive, $s = 1$ negative |
| exponent $e$ | 11 | stored with a bias of 1023 |
| fraction $f$ | 52 | the stored part of the significand |

For normal numbers the value is

$$x = (-1)^{s}\left(1 + \frac{f}{2^{52}}\right) 2^{e-1023}.$$

The leading $1$ is **implicit**: it is not stored, because normalised binary
numbers always have a leading $1$. The effective precision is therefore

$$p = 52 + 1 = 53 \text{ bits},$$

which is about

$$53\log_{10}2 = 15.9546 \text{ decimal digits}.$$

That is the origin of the familiar claim that a double holds "about 16
significant digits". Python itself advertises 15, the safe value
(`sys.float_info.dig`).

### 2.2 Decoding a real value

The demonstration script prints the decomposition of several values. For
$x = 0.1$ it reports

```text
0.1: sign=0 biased_exp=1019 unbiased=-4 mantissa=0x999999999999a
```

Reading that: $2^{1019-1023} = 2^{-4}$, and the stored fraction is
$0x999999999999a / 2^{52} = 0.600000000000000088817841970012523\ldots$, so
$1 + f/2^{52} = 1.600000000000000088817841970012523\ldots$ and the value is
$1.6000000000000000888\ldots \times 2^{-4}$. Carried out exactly, that product is
$0.1000000000000000055511151231257827021181583404541015625$, not $0.1$. Note the
trailing `a` in the mantissa: it is not zero, precisely because $0.1$ is not
representable.

### 2.3 Rounding: nearest, ties to even

Every arithmetic operation on two doubles produces an exact real result, which
is then **rounded** to the nearest representable double; when the exact result
lies exactly halfway, the tie is broken towards the even final bit. This is the
IEEE 754 default and it is what Python uses.

The relative error of a single rounded operation is therefore bounded by the
**unit roundoff**

$$u = \frac{1}{2}\varepsilon_{\text{mach}} = \frac{1}{2}2^{-52}
\approx 1.11\times10^{-16}.$$

The name matters: $\varepsilon_{\text{mach}} = 2^{-52}$ is the gap from $1$ to
the next double, while $u$ is half that gap and is the quantity that appears in
error bounds. Python exposes the gap as `math.ulp(1.0)` and
`sys.float_info.epsilon`, both $2.220446\times10^{-16}$.

### 2.4 The representable set is finite and uneven

The **ulp** ("unit in the last place") is the gap between neighbouring doubles
at a given magnitude:

| magnitude | observed `math.ulp(x)` |
|---|---|
| $1$ | $2.220446\times10^{-16}$ |
| $1024$ | $2.273737\times10^{-13}$ |
| $10^{6}$ | $1.164153\times10^{-10}$ |
| $10^{16}$ | $2.0$ |

Every doubling of the magnitude doubles the gap. The range of binary64 spans
roughly $2.2\times10^{-308}$ to $1.8\times10^{308}$ in magnitude (the smallest
normal and largest finite values, from `sys.float_info.min` and
`sys.float_info.max`), and below the smallest normal the leading bit becomes
implicit-zero: those **subnormal** values extend the range down to
$2^{-1074} \approx 5\times10^{-324}$, at the cost of losing significant bits as
they get smaller.

## 3. Machine epsilon, and what it is not

It is easy to misread $\varepsilon_{\text{mach}}$ as "the error of any
computation". It is nothing of the kind. It is:

- the spacing between $1$ and the next double;
- the largest $\varepsilon$ for which $1 + \varepsilon/2$ still rounds to $1$;
- a **relative** bound, so it says nothing by itself about absolute error.

The demonstration confirms the second bullet: `1.0 + eps/2 == 1.0` is `True`,
while `1.0 + eps == 1.0` is `False`. Any quantity added to $1$ that is smaller
than $u$ is simply lost.

## 4. Where round-off becomes visible

### 4.1 Representation error

An input that is not exactly representable enters the calculation already
carrying an error of up to $u$ relative. Nothing downstream can remove it.

### 4.2 Accumulation

Each operation rounds, so a loop that performs $n$ operations can carry $n$
roundings. The classic case is summation: adding a million copies of $0.1$
gives a result that is visibly wrong in the tenth digit.

### 4.3 Cancellation

If $a$ and $b$ are nearly equal, $a - b$ is computed from two numbers whose
*stored* values each carry a relative error of order $u$. Their absolute errors
are of order $u|a|$, but the difference is tiny, so the **relative** error of
the result is of order $u|a|/|a-b|$ — amplified without limit as $a \to b$.

This is often called "catastrophic cancellation". Two points are worth
separating, because they are usually conflated:

- The subtraction itself is often **exact**. By Sterbenz's lemma, if
  $b/2 \le a \le 2b$ then $a-b$ is computed exactly. The demonstration checks
  this for several pairs.
- What is destroyed is the **information** the operands encode. The answer is
  exact *given the stored inputs*, and those inputs are not the numbers you
  think you have.

### 4.4 Non-associativity and comparison

Floating-point addition is not associative: `(a + b) + c` may differ from
`a + (b + c)`. Consequently:

- `0.1 + 0.1 + 0.1 == 0.3` is `False`; the left side is
  `0.30000000000000004`.
- Testing computed floats for exact equality is a latent bug. Compare with a
  tolerance derived from the physics, not chosen arbitrarily.

## 5. Worked derivations

### 5.1 Why 0.1 has no finite binary expansion

Write $0.1 = 1/10$ in base 2. Multiplying numerator and denominator by a power
of two never removes the factor $5$: $1/10 = 1/(2\cdot5)$, and $1/5$ in binary
is the repeating sequence $0.\overline{0011}_2$. So the expansion never
terminates. The nearest binary64 value is

$$0.1000000000000000055511151231257827021181583404541015625,$$

which is what Python's `Decimal(0.1)` prints exactly. The stored value is not
$0.1$; it is the nearest double to $0.1$. Since $0.1$ is converted once and then
used consistently, the error is a fixed relative offset of order
$5.6\times10^{-17}$ — harmless if understood, fatal if you test for equality.

### 5.2 Why `(1e16 + 1) - 1e16` is `0.0`

At $10^{16}$ the ulp is $2.0$. Adding $1$ to $10^{16}$ gives an exact real result
that lies *exactly halfway* between two representable values
($10^{16}$ and $10^{16}+2$), and the ties-to-even rule sends it back to
$10^{16}$. The `1` is gone before the subtraction happens. The demonstration
prints:

```text
(1e16 + 1) - 1e16 = 0.0
math.nextafter(1e16, inf) - 1e16 = 2.0
```

Two lessons follow. First, adding a small number to a large one can be a no-op.
Second, an "accurate" accumulation of many tiny increments into a large running
total is exactly the situation where this happens — see Section 6, Section 10 of
the demo.

### 5.3 The standard error model, and a summation bound

Model each rounded operation by

$$\mathrm{fl}(a \odot b) = (a \odot b)(1+\delta), \qquad |\delta| \le u,$$

where $\odot$ is any of $+,-,\times,\div$ and division requires $b \ne 0$. This
model is a theorem of IEEE 754 arithmetic, not an approximation.

Apply it to left-to-right summation of $x_1,\dots,x_n$. Write $s_k$ for the
running sum. The error after $n$ steps is bounded by

$$\left|\hat{s}_n - s_n\right| \;\le\; (n-1)\,u \sum_{k=1}^{n} |x_k| + O(u^2).$$

The bound is *pessimistic*: it assumes every rounding error has the worst
possible sign. The demonstration shows the bound is not tight but that its
scaling in $n$ can be real.

### 5.4 Compensated summation removes the growth in $n$

Kahan's compensated summation keeps a second variable `c` for the low-order
bits that the addition discarded:

```text
y = x - c
t = s + y
c = (t - s) - y
s = t
```

The quantity `(t - s) - y` recovers the part of `y` that was lost when forming
`t = s + y`; that residue is fed back on the next iteration. The resulting error
bound is independent of $n$:

$$\left|\hat{s} - s\right| \le 2u\sum_k |x_k| + O(u^2).$$

The demonstration is decisive: for $n = 10^{6}$ copies of $0.1$, the plain
accumulation loop gives `100000.00000133288` (absolute error
$1.33\times10^{-6}$), while Kahan summation, `math.fsum` and the built-in
`sum()` all return exactly `100000.0`. `math.fsum` does not merely compensate —
it computes an exactly rounded sum — and the built-in `sum()` is compensated for
floats in CPython 3.12 and later, so the loop, not `sum`, is the naive choice in
modern Python.

### 5.5 The stable quadratic formula

For $ax^2 + bx + c = 0$ with $b^2 \gg 4ac$, the two roots differ enormously in
magnitude, and the smaller root is computed as $(-b - \mathrm{sign}(b)\sqrt{b^2 -
4ac})/(2a)$. That numerator subtracts two nearly equal numbers.

Take $x^2 - 10^8x + 1 = 0$. The roots are approximately $10^8$ and
$10^{-8}$, and their product is exactly $c/a = 1$. Compute the large root first,
then obtain the small root from the product of the roots rather than from the
subtraction:

$$x_1 = \frac{-b + \sqrt{b^2-4ac}}{2a}, \qquad x_2 = \frac{c}{a\,x_1}.$$

The demonstration reports the naive small root as `7.450580596923828e-09` and
the stable one as `1e-08`; against the exact root from 50-digit decimal
arithmetic, the naive value is wrong by $2.55\times10^{-9}$ (a relative error of
about 25%, i.e. one correct significant digit) while the stable value is wrong
by $7.9\times10^{-25}$. The formula was never the problem; the route through the
subtraction was.

### 5.6 A prediction you can check: the best step for numerical differentiation

Approximate $f'(x)$ by the forward difference $\big(f(x+h)-f(x)\big)/h$. Two
errors compete:

- **truncation**: $\dfrac{h}{2}|f''(x)| + O(h^2)$, from Taylor's theorem;
- **round-off**: each computed $f$ value carries absolute error at most $u|f|$,
  so the difference carries about $2u|f|$, and dividing by $h$ gives
  $\dfrac{2u|f(x)|}{h}$.

Add them and minimise over $h$:

$$E(h) \approx \frac{h|f''|}{2} + \frac{2u|f|}{h},
\qquad \frac{dE}{dh} = \frac{|f''|}{2} - \frac{2u|f|}{h^2} = 0
\;\Longrightarrow\; h^{*} = 2\sqrt{\frac{u|f|}{|f''|}}.$$

For $f(x)=\sin x$ at $x=1$: $|f| = |f''| = \sin 1 = 0.84147$, so
$h^{*} = 2\sqrt{u} = 2.1\times10^{-8}$ and $E(h^{*}) \approx 1.8\times10^{-8}$.

The demonstration's error table reaches its **smallest** error at $h = 10^{-8}$
with $1.407\times10^{-8}$, while at $h=10^{-1}$ the truncation-dominated error
is $4.294\times10^{-2}$. The predicted optimal step $2.1\times10^{-8}$ and the
measured optimum $10^{-8}$ agree to within a factor of about two, and the
predicted minimum error $1.8\times10^{-8}$ matches the measured
$1.41\times10^{-8}$ to within 30%. That is a useful, checkable result, and it is
why no finite-difference derivative in scientific code should use an arbitrarily
small step.

### 5.7 Cancellation in an anomaly

A Bouguer anomaly is the difference of two gravity values of order $10^{5}$
mGal. The demonstration subtracts `979812.37 - 979802.15 = 10.22` mGal. The
subtraction is exact for those two stored values, but each datum carries a
relative error of order $u$, i.e. an absolute error of order
$10^{5} \times 10^{-16} \approx 10^{-11}$ mGal — about $10^{-12}$ of the
anomaly. That is why gravity work demands that observed and theoretical values be
computed consistently, and why differencing two nearly equal large numbers is
acceptable here **only** because the quantity subtracted is genuinely known to
many digits.

## 6. Python demonstration

Run

```bash
python3 code/floating_point_demo.py
```

The script `code/floating_point_demo.py` uses only the standard library
(`math`, `struct`, `decimal`, `fractions`) and covers: the anatomy of binary64,
the exact stored value of $0.1$, ulp at four magnitudes, cancellation in
$(1-\cos x)/x^2$, the stable quadratic formula, four summation strategies,
the finite-difference error floor, a Bouguer-anomaly difference, Sterbenz's
lemma, and the $\mathcal{O}(n^2)$ growth of naive summation error.

Observed output worth dwelling on (all quoted verbatim from a run on this
repository's test machine):

```text
x                  naive    stable (half-angle)   rel. err naive
1e-04        0.4999999969613        0.4999999995833        5.244e-09
1e-06        0.5000444502912        0.5000000000000        8.890e-05
1e-08        0.0000000000000        0.5000000000000        1.000e+00
```

For $(1-\cos x)/x^2$ the true limit is $1/2$. The naive form has a relative
error of $5.2\times10^{-9}$ at $x = 10^{-4}$, rising to $8.9\times10^{-5}$ at
$x = 10^{-6}$, and it returns **exactly zero** at $x = 10^{-8}$, because
$\cos x$ rounds to exactly $1.0$ and the numerator becomes $0$. The half-angle
form $2\sin^2(x/2)/x^2$ is still correct to all printed digits, and it is not a
coincidence that the algebra removes the cancellation.

| Observation | Consequence in geophysics |
|---|---|
| `0.1 + 0.1 + 0.1 != 0.3` | never test computed floats for exact equality |
| `(1e16 + 1) - 1e16 == 0.0` | incrementing a large running total can do nothing |
| `(1 - cos x)/x**2` collapses to 0 | reformulate a difference of nearly equal functions algebraically |
| `error / n**2` constant (Section 10) | naive error in long sums grows quadratically, not linearly |
| Sterbenz: exact inside a factor of two | cancellation loses the *inputs'* precision, not the subtraction's |
| best forward-difference $h \approx 2\times10^{-8}$ | never shrink a finite-difference step blindly |

## 7. Exercises

Ten graded exercises, with full worked solutions, are in
[`exercises/04-floating-point-exercises.md`](./exercises/04-floating-point-exercises.md)
and
[`exercises/04-floating-point-solutions.md`](./exercises/04-floating-point-solutions.md).

Three to attempt now, closed-book:

**★1.** State the value of $\varepsilon_{\text{mach}}$ for binary64, and decide
whether $1 + 10^{-17}$ differs from $1$ in that format.

**★★2.** Convert the exact decimal expansion of the stored value of $0.1$ back
into the form $(1 + f/2^{52})2^{-4}$ and verify that $f = 0x999999999999a$
matches the bit decomposition printed by the demonstration.

**★★★3.** Show that estimating $1 - \cos x$ by the truncated series
$x^2/2 - x^4/24$ costs no accuracy for small $x$, and find empirically the
crossover value of $x$ below which the series beats the directly computed
$1-\cos x$. Report your method, your measured crossover, and the limitation of
your conclusion.

## 8. Common mistakes

1. **Believing a float "is" the decimal you typed.** It is the nearest
   representable value, and the difference is real.
2. **Comparing floats with `==`.** Use `math.isclose(a, b, rel_tol=...)` with a
   tolerance justified by the data, or compare exact integers/decimals.
3. **Assuming errors average out.** They may all share a sign, as the
   $\mathcal{O}(n^2)$ growth in Section 6 shows.
4. **Thinking cancellation is an arithmetic bug.** The subtraction is usually
   exact; the operands are the problem. The fix is algebraic reformulation, not
   a higher-precision type by reflex.
5. **Making a difference step as small as possible.** Below $h \approx
   \sqrt{u}$ the round-off term dominates and accuracy degrades (Section 5.6).
6. **Accumulating a long series with an explicit `for` loop.** Sum in blocks,
   sort by magnitude, or use `math.fsum`. (Careful: the built-in `sum()` is
   *not* naive — CPython 3.12 and later compensate it for floats. An explicit
   accumulation loop still is naive, and a vectorised NumPy `sum` reduces with a
   pairwise scheme whose accuracy is not the same as either.)
7. **Confusing $\varepsilon_{\text{mach}}$ with an absolute tolerance.** It is a
   relative spacing and says nothing about quantities near $10^{-30}$.

## 9. Real-world applications

- **Finite-difference modelling.** A FD Laplacian contains differences of
  nearly equal field values divided by $\Delta x^2$. In single precision,
  round-off and cancellation can dominate the discretisation error entirely;
  this is why production wave-propagation codes work in double precision and are
  validated by convergence tests rather than by inspection.
- **Time-series integration.** Seismic and geodetic time series are long sums of
  small increments. Compensated or blocked summation preserves the trend; naive
  accumulation of millions of samples can invent one.
- **Inversion and conditioning.** The normal equations $(A^\mathsf{T}A)x =
  A^\mathsf{T}b$ square the condition number, and cancellation inside them is
  one reason practitioners prefer QR or SVD factorisations. This is developed in
  [18-inverse-problems](../../18-inverse-problems/README.md).
- **Anomaly maps.** Potential-field anomalies are differences of large
  quantities, so the numerics of computing the theoretical field matter as much
  as the measurement precision. See
  [07-gravity-geodesy](../../07-gravity-geodesy/README.md).
- **Reproducibility.** Because floating-point addition is not associative, two
  mathematically identical codes can give different results. Reporting the
  algorithm and the precision is part of the method, not a detail — see
  [22-data-engineering-reproducibility](../../22-data-engineering-reproducibility/README.md).

## 10. Further reading

- **Higham, N. J. (2002). *Accuracy and Stability of Numerical Algorithms*
  (2nd ed.). SIAM.** Chapters 1–4. Level: advanced undergraduate upward.
  Chapter 2 (floating-point summation) is the reference for Sections 5.3–5.4,
  and Chapter 4 (summation) collects the historical results.
- **Goldberg, D. (1991). What every computer scientist should know about
  floating-point arithmetic. *ACM Computing Surveys*, 23(1), 5–48.** Level:
  intermediate. The classic accessible survey of the whole model.
- **Muller, J.-M., Brunie, N., de Dinechin, F., Jeannerod, C.-P., Joldes, M.,
  Lefèvre, V., Melquiond, G., Revol, N., & Torres, S. (2018). *Handbook of
  Floating-Point Arithmetic* (2nd ed.). Birkhäuser.** Level: reference. The
  definitive modern treatment, including correct rounding.
- **Kahan, W. (1965). Further remarks on reducing truncation errors.
  *Communications of the ACM*, 8(1), 40.** Level: intermediate. The original
  compensated-summation note; two pages that repay careful reading.
- **IEEE 754-2019, *IEEE Standard for Floating-Point Arithmetic*.** Level:
  reference. The normative definition, including the rounding rules of
  Section 2.3.
- **Python standard-library documentation for `math.fsum`, `math.ulp` and
  `sys.float_info`.** Level: reference. Always check the current documentation
  for your interpreter version.

> Note on citations: bibliographic details above are given so you can locate the
> works. This repository does not host or reproduce copyrighted text, and you
> should confirm current availability and editions through your library before
> citing them.

## 11. Related lessons

- [01 Number Systems, Precision and Scientific Notation](./01-number-systems-and-precision.md)
  — significant figures, the "honest reporting" rule, and the first warning
  about $0.1$.
- [05 Absolute vs Relative Error, Conditioning and Stability](./05-error-and-conditioning.md)
  — the next step: separating the error an algorithm adds from the error the
  problem makes unavoidable.
- [02 Algebra, Functions and Modelling](../02-algebra/README.md) — the
  algebraic reformulations (half-angle, stable quadratic formula) that remove
  cancellation.
- [03-scientific-computing](../../03-scientific-computing/README.md) — the
  practical tooling: NumPy dtypes, vectorised summation, and validation.

## Self-assessment checklist

- [ ] I can write the binary64 formula and explain the roles of $s$, $e$ and $f$.
- [ ] I can state $\varepsilon_{\text{mach}} = 2^{-52}$ and distinguish it from
      the unit roundoff $u = 2^{-53}$.
- [ ] I can explain why `0.1 + 0.1 + 0.1 != 0.3` without hand-waving.
- [ ] I can derive the optimal step size for a forward difference.
- [ ] I can name a case in my own work where cancellation is present and say how
      I would reformulate it.
- [ ] I know when to reach for `math.fsum` rather than `sum`.
