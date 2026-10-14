---
id: 03-01-02
title: "Types, Variables, Expressions and Operator Semantics"
level: beginner
prereqs: ["03-01-01", "01-01-04"]
estimated_minutes: 75
tags: [types, floating-point, operators, precision, gravity]
---

# Types, Variables, Expressions and Operator Semantics

Every number a geophysicist writes down is an approximation to a real quantity,
and every number a computer stores is an approximation to the number you wrote.
The two approximations are different, and only one of them is under your control.
This lesson is about that one: the representation.

The reason it matters is scale. A relative gravimeter resolves a few microgal —
one part in about $10^{10}$ of the Earth's field. A `float64` carries about 15.95
significant decimal digits. That is enough, with a margin of roughly six orders of
magnitude, which is why gravity is done in double precision and not in
single precision, and why the accumulated rounding error in a million-term sum is
worth measuring rather than assuming away.

## Learning objectives

By the end of this lesson you will be able to:

1. **Classify** every literal and expression by type, and predict the result of
   `/`, `//`, `%` and `**`, including for negative operands.
2. **Explain** what a `float64` is: sign, 11-bit exponent, 53-bit significand,
   and why `0.1 + 0.2` is not `0.3`.
3. **Compute** the worst-case absolute resolution of a stored geophysical
   quantity from its magnitude, using the unit in the last place.
4. **Measure** the accumulation error of a naive sum and remove it with
   `math.fsum`, quoting the before-and-after numbers.
5. **Identify** integer-division and mixed-type traps in an expression before
   running it.
6. **Choose** between `int`, `float`, `Fraction` and `Decimal` on the grounds of
   what the quantity actually is.

## Prerequisites

- [03-01-01 Why Python for Geophysics](./01-why-python.md) — the instrument
  framing and the forward model used throughout.
- [01-01-04 Floating Point Representation and Rounding](../../01-mathematics/01-arithmetic/04-floating-point.md)
  — the mathematical treatment of IEEE-754 and rounding, which this lesson uses
  rather than repeats.

## 1. Types, and what each one is for

Python has four numeric types you will use constantly.

| Type | Representation | Range | Use it for |
|---|---|---|---|
| `int` | Arbitrary precision | Unbounded (memory-limited) | Counts, indices, event numbers, epoch seconds |
| `float` | IEEE-754 binary64 | $\pm 1.8\times10^{308}$, ~16 decimal digits | Every measured or modelled real quantity |
| `complex` | Pair of `float` | As above per component | Fourier, impedance, analytic signals |
| `bool` | Subclass of `int` | `True`/`False` = 1/0 | Flags; it is *not* a numeric type to compute with |

`int` being arbitrary precision is not a curiosity. An earthquake catalogue
counter, a sample index into a 10⁹-point record, and a Unix timestamp all exceed
32 bits without warning, and in a language with fixed-width integers each is an
overflow waiting to happen. Here, `10 ** 30` is computed exactly:

```text
  expression   value                            type
  7            7                                int
  7.0          7.0                              float
  7 / 2        3.5                              float
  7 // 2       3                                int
  -7 // 2      -4                               int
  7 % 2        1                                int
  -7 % 2       1                                int
  2 ** 10      1024                             int
  -2 ** 2      -4                               int
  (-2) ** 2    4                                int
  2 ** -1      0.5                              float
  3 * 0.1      0.30000000000000004              float
  10 ** 30     1000000000000000000000000000000  int
  10.0 ** 30   1e+30                            float
```

Five facts to memorise from that table.

- **`/` always returns a float, `//` floors.** `7 / 2` is `3.5`; `7 // 2` is
  `3`. In most other languages `/` on two integers truncates, so a MATLAB or C
  programmer's habits transfer *incorrectly* in the opposite direction: here,
  code that intends integer division but writes `/` will produce a float index and
  fail loudly, which is a mercy.
- **`//` floors towards minus infinity, not towards zero.** `-7 // 2` is `-4`,
  not `-3`. This matters whenever you bin a signed quantity — depth below sea
  level, a residual anomaly, a UTC offset.
- **`%` follows the sign of the divisor.** `-7 % 2` is `1`. It is a true
  modulo, not a C-style remainder.
- **`**` binds tighter than unary minus.** `-2 ** 2` is `-4`. When in doubt,
  parenthesise; a misplaced sign in an exponent is a silent sign error in a
  physically meaningful quantity.
- **Mixing `int` and `float` promotes to `float`.** That is usually what you
  want, and occasionally — see §4 — the source of a 25 per cent error.

## 2. What a float actually is

A `float64` stores a real number as $\pm m \times 2^{e}$ where $m$ is a 53-bit
significand and $e$ an 11-bit exponent. Three consequences, in increasing order
of how often they bite.

**Consequence 1: most decimal fractions are not representable.** A number is
representable exactly only if it is a dyadic rational with no more than 53
significant bits. $0.1 = 1/10$ is not, because 10 has a factor of 5. Hence

```text
  0.1                    = 0.1
  0.1 + 0.2              = 0.30000000000000004
  (0.1 + 0.2) == 0.3     = False
  0.1 + 0.2 - 0.3        = 5.551115123125783e-17
  math.isclose to 1e-15  = True
```

The residual is $5.55\times10^{-17}$, which is one unit in the last place of the
result. Note the repr: `0.1` prints as `0.1` because Python displays the shortest
decimal string that round-trips to the same double — the stored value is
$0.1000000000000000055511151231257827\ldots$. The display is a courtesy, not the
value.

**Consequence 2: relative precision is constant, absolute precision is not.** The
gap between adjacent doubles near a value $x$ is about $|x| \times 2.22\times10^{-16}$.
For a stored gravity value near $9.8\times10^{5}$ mGal the absolute resolution is
therefore

$$\mathrm{ulp}(9.8\times10^{5}) \approx 9.8\times10^{5} \times 2.22\times10^{-16}
\approx 2.2\times10^{-10}\ \text{mGal},$$

roughly a tenth of a nanogal. Instrument noise is orders of magnitude larger, so
double precision is not the limitation for a gravity survey. The same arithmetic
is why a coordinate has a hard floor. The demo prints

```text
  the smallest representable longitude step near 0 deg is 4.9e-324 deg,
  but near 180 deg it is 2.842e-14 deg = 3.164e-09 m.
```

Two numbers, same type, wildly different resolution — because the *exponent*
moves. A longitude stored as a double can express a position to about 3 nm in
absolute terms near 180°, but the moment you take a difference of two positions
the subtraction is exact only if the two share an exponent. Differences of large
nearly equal numbers are the classic loss of significance, and the fix is to
compute the difference *before* the large numbers are formed — which is why
haversine formulas are written with half-angle terms.

**Consequence 3: floating-point addition is not associative.** This is what makes
accumulation error grow.

## 3. Worked walkthrough: accumulation error, measured

The demo sums the free-air gradient, 0.3086 mGal per metre, a million times — a
one-million-station line, admittedly an extreme one:

```text
  adding 0.3086 mGal exactly 1,000,000 times
  naive loop sum        = 308599.9999943999
  math.fsum             = 308600.0
  exact rational value  = 308600
  naive  - exact        = -5.6001e-06 mGal   (-1.81e-11 relative)
  fsum   - exact        = 0.0000e+00 mGal
  ulp of the final sum  = 5.8208e-11 mGal
```

The exact answer is $10^{6} \times 0.3086 = 308600$ mGal exactly (as a rational
number, since $0.3086 = 3086/10000$). The naive loop is wrong by 5.6 µGal, which
is about 96 ulps of the final total and a relative error of $1.8\times10^{-11}$.
`math.fsum` returns the correctly rounded result, exactly.

Whether 5.6 µGal matters depends entirely on the problem. In a regional gravity
survey with a 10 µGal repeatability it is at the edge; in a microgravity
monitoring survey resolving 5 µGal it is the entire signal. The honest statement
is: **the error grows like $\sqrt{n}$ times the per-step ulp, so it enters the
budget as a scale-dependent term, and you should know which side of your noise
floor it falls on.** For microgravity work the answer is to use `math.fsum`, or
NumPy's pairwise summation, or a compensated scheme. Lesson 05's exercises ask
you to find the crossing point.

## 4. Worked walkthrough: the integer-division trap, in situ

Here is a mistake that ships. The source mass of the sphere in the forward model
is

$$M = \tfrac{4}{3}\pi a^3 \Delta\rho .$$

If the demo had written `4 // 3` instead of `4 / 3`, the code would have computed
`M = π a³ Δρ` with no error message and no warning:

```text
  mass   (floats) = 1.005310e+10 kg    type float
  peak   (floats) = 0.268390 mGal

  Had the mass been written with '//' the 4/3 would have become 1,
  silently losing 25 per cent of the source mass and 25 per cent of
  the anomaly.
```

`4 // 3` is a perfectly legal expression whose value is `1`. The program runs,
produces a plausible-looking anomaly curve, and is wrong by exactly 25 per cent
in mass and hence 25 per cent in the peak. Nothing about the output announces the
error: the curve has the right shape, because the shape does not depend on the
mass.

This is worth dwelling on because it generalises. **A scaling error is invisible
in the shape of a result.** It changes the amplitude, and amplitude is exactly the
quantity that a qualitative check ("the anomaly looks like a dipole, so the code
must be right") cannot detect. The defence is a test with a known answer: feed the
model a case whose mass you can compute by hand. That is lesson
[07](./07-errors-and-debugging.md)'s subject and the reason the module's shared
library carries a self-test.

Two more mixed-type traps that recur in geophysics:

- **Integer division of a count.** `n_stations // 2` gives a station *index*,
  `n_stations / 2` gives a coordinate in station units. Using the wrong one puts
  the line centre half a station off. The demo prints both for
  `n_stations = 7`: `3.5` and `3`.
- **`bool` is an `int`.** `True + True` is `2`. A flag that reaches an
  arithmetic expression will not raise; it will add 1.

## 5. When exactness is worth paying for

`float` is the right choice for everything measured. It is the wrong choice for
two situations: a small closed-form check you want to be exact, and a decimal
quantity whose digits are specified by something other than physics.

```text
  ten additions of 0.1 m   = 0.9999999999999999 m
  Fraction(1,10) * 10      = 1  -> exactly one metre
  Decimal('0.1') * 10      = 1.0
```

Ten station intervals of 0.1 m sum to `0.9999999999999999` m as doubles — an error
of $1.1\times10^{-16}$ m, harmless for a survey and unacceptable if you are
asserting that a closed traverse closes exactly.

- **`fractions.Fraction`** is exact rational arithmetic. Use it for small
  hand-checkable identities, for exactness in a unit test, and for diagnosing
  whether a discrepancy is a bug or rounding. It is slow, and it is not for
  arrays.
- **`decimal.Decimal`** is exact *decimal* arithmetic with a settable precision
  and rounding mode. Use it when the specification is decimal: financial-style
  reporting, a file format that specifies digits, or a reproducible audit trail.
  It is not a substitute for `float` in physics, because no sensor delivers
  sixteen exact decimal digits.

The rule: **use `float` for measurements, `Fraction` for proofs, `Decimal` for
contracts, and `int` for counts.**

## 6. Physical interpretation: what precision does a survey need?

The abstract statement "a double has 16 digits" becomes a design decision only
when it is compared with an instrument. Do the comparison for three common
geophysical measurements and the pattern is immediate.

| Measurement | Typical resolution | Relative resolution | Verdict for `float64` |
|---|---|---|---|
| Relative gravity | a few µGal on 9.8 × 10⁵ mGal | ~10⁻¹¹ | Adequate with ~5 orders of margin; accumulation order matters |
| GNSS position (daily) | ~3 mm horizontal | ~10⁻⁹ of the Earth's radius | Adequate; but a *difference* of two positions needs the difference formed early |
| Seismic amplitude (24-bit ADC) | 1 part in 1.7 × 10⁷ | ~10⁻⁷ | Adequate with 8 orders of margin; `float32` would already suffice |
| Magnetic field (proton precession) | ~0.1 nT on 5 × 10⁴ nT | ~10⁻¹² | Adequate; sensor noise dominates by orders of magnitude |

The resolutions in that table are *nominal order-of-magnitude* figures for classes
of instrument, not specifications of any named model; a factor-of-ten change in
any of them does not change the conclusion, which is the point of stating them
this way.

Three conclusions follow, and they are the practical content of this lesson.

**Double precision is not usually the limiting factor; the instrument is.** The
µGal-level survey enters the arithmetic with 11 significant digits and leaves it
with 16, so no plausible number of additions destroys the result — unless the
number of additions is $10^{11}$, which is where the $\sqrt{n}$ growth of §3
starts to matter.

**Differences are where precision is lost, not products.** Multiplication and
division preserve relative precision; subtraction of nearly equal large numbers
destroys it. A position difference, a residual (observed minus predicted), a
topographic correction (station minus reference level) — all are subtractions of
larger quantities, and all should be formed as early as the algebra allows. The
haversine form of a distance is written with half-angle terms for exactly this
reason.

**The unit tells you the required precision.** A quantity named `depth_km` and
recorded to three decimals is claiming metre precision. If the calculation behind
it only supports 10 m, the digits are decoration, and the honest response is to
name the variable for what it is. Units in variable names are not style; they are
part of the type.

## 7. Variables are names for objects

This is the single most consequential thing a beginner can learn about Python,
and the reason it belongs in a lesson about "types".

```text
  a = [0.1, 0.2, 0.3]
  b = a, then b.append(0.4)
  a is b                  -> True
  a == b                  -> True
  c = a[:] before the append: c = [0.1, 0.2, 0.3]  (c is a -> False)
```

`b = a` does not copy. It binds a second name to the same list object. When `b`
is mutated, `a` changes too — because there is only one list. `c = a[:]` makes a
copy, and `c` is unaffected.

The `is` operator tests identity (the same object); `==` tests equality (the same
value). They are different questions:

- `a is b` is `True` here because they are the same object.
- `[0.1] == [0.1]` is `True` for two distinct lists, because element-wise
  equality holds.
- `float('nan') == float('nan')` is `False`, because IEEE-754 says a NaN is not
  equal to itself. `nan is nan` can be `True` for the same object. This is a
  genuine hazard in a data-cleaning script: `value == float('nan')` never
  matches, which is why `math.isnan` exists.

The rule to carry forward: **assignment binds a name; slicing and `list()`,
`dict()` and `copy.copy` make shallow copies; and a shallow copy of a list of
lists still shares the inner lists.** Lesson
[05](./05-data-structures.md) makes this precise per container, and module
[03-02](../02-numpy/README.md) shows that the same distinction is the difference
between a NumPy view and a copy, where it costs a factor of two in memory and a
class of silent bugs.

## 8. Assumptions and limits

1. **`float` means IEEE-754 binary64.** Python's documentation permits other
   platforms in principle; in practice `sys.float_info.epsilon` is
   $2.22\times10^{-16}$ everywhere you will run this curriculum. Check it, as the
   demo does, rather than assuming.
2. **`math.isclose` needs a tolerance, and the tolerance is physics.** The
   default relative tolerance is $10^{-9}$. For a velocity comparison that is
   absurdly loose; for a 10⁹-sample sum it is too tight. Choose the tolerance from
   the measurement, never from the default.
3. **Comparisons involving NaN are always false**, including `nan < 1.0`. Code
   that sorts or filters measurement data must handle NaN explicitly or it will
   silently drop or silently keep every such row.
4. **`Fraction` and `Decimal` do not extend to arrays.** They are per-scalar
   tools; using them in a loop over 10⁶ samples costs orders of magnitude more
   than the accuracy is worth.
5. **`-0.0` exists and compares equal to `0.0`** while printing differently. It
   appears in practice after a sign-preserving multiplication by zero. It is
   harmless in arithmetic and occasionally confusing in output.
6. **The accumulation numbers are for this interpreter and machine.** The
   *scaling* (error $\propto \sqrt{n}$ ulps) is a property of IEEE-754 arithmetic;
   the exact last digit is not.

## 9. Python demonstration

```bash
cd 03-scientific-computing/01-python-fundamentals/code
python3 types_variables_demo.py
```

The script is organised as the six sections of this lesson and prints each claim
alongside its evidence. The three numbers to reproduce and remember are the
accumulated error 5.6001 × 10⁻⁶ mGal, the ulp of the final sum 5.8208 × 10⁻¹¹
mGal, and the ratio between them, about 96. If you can reproduce those three, you
understand the mechanism; if you can predict the third before running it, you
understand it quantitatively.

## 10. Common mistakes

1. **Testing floats for equality.** Use `math.isclose(x, y, rel_tol=...)`, and
   choose `rel_tol` from the physics.
2. **Assuming `0.1` is `0.1`.** It is the nearest double. Any exact identity built
   on decimal fractions will fail eventually.
3. **`4 / 3` versus `4 // 3`.** A 25 per cent amplitude error with no warning.
4. **Accumulating a long sum naively and then blaming the data.** `math.fsum` is
   one word.
5. **Sub-classing or comparing with `bool`.** `True + True == 2`; `1 == True` is
   `True`, which means a dict keyed on `True` and `1` collide.
6. **Forgetting that `-7 // 2 == -4`.** Bin a negative quantity with `//` and the
   bins are not centred where you think.
7. **Using `Decimal` for physics.** Sixteen exact decimal digits of a quantity
   measured to three is false precision dressed as rigour.
8. **Believing `repr` is `str`.** `print(x)` and `repr(x)` differ for many
   values; when you need to see the actual double, print `repr`.
9. **Comparing `nan` with `==`.** It is always `False`; use `math.isnan`.
10. **Copying a nested container with `[:]`.** A shallow copy still shares the
    inner objects.

## 11. Real-world applications

- **Gravity and microgravity surveys** work at the $10^{-10}$ relative level,
  which is why the reduction pipeline is done in `float64` and why accumulation
  order in the summation of a long tie-in loop is a real (if usually small)
  contribution to the closure error.
- **Geodetic coordinates** are the canonical example of absolute-precision loss:
  a longitude stored as a double is good to nanometres near 180° only if you also
  store the latitude, because the metric size of a longitude step shrinks as
  $\cos\phi$. Position differences taken naively across a wide span lose digits.
- **Catalogue statistics.** Counting events, summing moment release or binning
  magnitudes are all integer and floating-point operations whose type errors are
  silent. `4 // 3`-style bugs in a magnitude conversion factor survive review
  because the histogram still looks like a Gutenberg-Richter law.
- **Reproducibility.** Two runs that sum in a different order give bitwise
  different results. If a published number must be reproducible bit-for-bit, the
  summation order is part of the method, which is why parallel reduction
  libraries document their determinism guarantees.

## 12. Further reading

- NIST CODATA fundamental constants — [physics.nist.gov/cuu/Constants/](https://physics.nist.gov/cuu/Constants/):
  note that each constant carries a standard uncertainty and a unit, which is the
  habit this lesson is trying to install in code.
- NumPy — [numpy.org](https://numpy.org): the array dtypes and pairwise
  summation that this lesson's accumulation error motivates.

## 13. Related lessons

- [03-01-01 Why Python for Geophysics](./01-why-python.md) — where the 0.268 mGal
  forward model and its $z^{-2}$ scaling come from.
- [03-01-03 Conditionals, Loops and Loop-Invariant Reasoning](./03-control-flow.md)
  — the loop around these arithmetic operations, and its invariants.
- [03-01-05 Lists, Tuples, Dictionaries, Sets and Complexity](./05-data-structures.md)
  — the per-container rules for copying and mutation.
- [01-01-04 Floating Point Representation and Rounding](../../01-mathematics/01-arithmetic/04-floating-point.md)
  — the mathematics of subnormals, rounding modes and error analysis.
- [03-02 NumPy](../02-numpy/README.md) — `float32` versus `float64`, and why the
  choice is a memory decision made at $10^{8}$ samples.

## 14. Exercises

[`exercises/02-types-and-variables-exercises.md`](./exercises/02-types-and-variables-exercises.md) —
eight problems, ★ to ★★★. Problem ★★5 requires the demo's accumulated-error
numbers; problem ★★★7 asks you to measure the error as a function of the term
count and fit its growth, and problem ★★★8 to decide whether a stated
repeatability budget is safe.

## 15. Self-assessment checklist

- [ ] I can predict the type and value of `7 / 2`, `7 // 2`, `-7 // 2`, `-7 % 2`
      and `-2 ** 2` without running Python.
- [ ] I can explain why `0.1 + 0.2 != 0.3` in terms of dyadic rationals.
- [ ] I can compute the ulp of a stored value from its magnitude.
- [ ] I have reproduced the 5.6 µGal accumulation error and the 5.82 × 10⁻¹¹ mGal
      ulp of the final sum, and I can state their ratio.
- [ ] I can name two situations where `Fraction` or `Decimal` is the right choice
      and two where it is not.
- [ ] I can explain the difference between `is` and `==`, and why `b = a` does not
      copy a list.
- [ ] I can say what `math.isnan` is for and why `x == float('nan')` never works.
