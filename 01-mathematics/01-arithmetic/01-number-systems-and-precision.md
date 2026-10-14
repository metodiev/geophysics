---
id: 01-01-01
title: "Number Systems, Precision and Scientific Notation"
level: beginner
prereqs: []
estimated_minutes: 90
tags: [arithmetic, floating-point, precision, si-units]
---

# Number Systems, Precision and Scientific Notation

## Learning objectives

By the end of this lesson you will be able to:

1. **Represent** any geophysical quantity in scientific notation and in the
   engineering notation conventionally used in the field.
2. **Distinguish** exact numbers from measured numbers, and state the
   precision implied by a written value.
3. **Identify** the geophysics-specific unit conventions (mGal, nT, Ω·m, Ma)
   and convert between them and SI base units.
4. **Determine** the number of significant figures a computed result may
   defensibly carry, and explain why carrying more is a form of dishonesty.
5. **Recognise** that decimal fractions such as $0.1$ have no exact binary
   floating-point representation, and predict where this causes trouble.

## Prerequisites

None. This is the first lesson of the curriculum.

## 1. Intuition: numbers in geophysics span an absurd range

Before any formalism, appreciate the scale of the problem. A geophysicist must
handle, in a single working day:

| Quantity | Typical magnitude | In SI |
|---|---|---|
| Gravitational acceleration anomaly over an orebody | 2 mGal | $2\times10^{-5}\ \mathrm{m\,s^{-2}}$ |
| Magnetic anomaly over a dyke | 500 nT | $5\times10^{-7}\ \mathrm{T}$ |
| Seismic P-wave speed in granite | 5.5 km/s | $5.5\times10^{3}\ \mathrm{m\,s^{-1}}$ |
| Mantle viscosity | 10²¹ Pa·s | $10^{21}\ \mathrm{Pa\,s}$ |
| Earth's age | 4.54 Ga | $1.43\times10^{17}\ \mathrm{s}$ |
| Gravitational constant $G$ | 6.674×10⁻¹¹ | $6.674\times10^{-11}\ \mathrm{m^3\,kg^{-1}\,s^{-2}}$ |

That is roughly **32 orders of magnitude** in a single discipline. Writing these
as `0.00002`, `0.0000005`, and `1000000000000000000000` is an invitation to
error — miscounting a zero in a decimal expansion has caused real
interpretation mistakes. Scientific notation exists to make the magnitude and
the precision *visible at a glance*.

## 2. Precise definitions

### 2.1 Scientific notation

Any nonzero real number $x$ can be written uniquely as

$$x = \pm a \times 10^{n}, \qquad 1 \le a < 10,\quad n \in \mathbb{Z}.$$

The number $a$ is the **significand** (or mantissa) and $n$ is the **exponent**.

- $2\times10^{-5}$ m/s² (a gravity anomaly)
- $5\times10^{-7}$ T (a magnetic anomaly)
- $6.674\times10^{-11}$ m³ kg⁻¹ s⁻² (the gravitational constant)

### 2.2 Engineering notation

Engineering notation constrains the exponent to a multiple of 3, so it aligns
with SI prefixes (kilo, mega, milli, micro, nano):

$$x = \pm a \times 10^{3m}, \qquad 1 \le a < 1000,\quad m \in \mathbb{Z}.$$

Thus $2\times10^{-5}\ \mathrm{m\,s^{-2}}$ becomes $20\times10^{-6}\ \mathrm{m\,s^{-2}}$
or, with the SI prefix, $20\ \mu\mathrm{m\,s^{-2}}$. In practice gravity is never
written in SI; it is written in **mGal**, where

$$1\ \mathrm{Gal} = 10^{-2}\ \mathrm{m\,s^{-2}}, \qquad
1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}.$$

So a 2 mGal anomaly is $2\times10^{-5}\ \mathrm{m\,s^{-2}}$. **The unit is not
decoration — it carries the exponent for you.**

### 2.3 Exact vs measured numbers

This distinction governs everything that follows.

- An **exact** number is defined or counted: 12 stations, $\pi$, the number of
  metres in a kilometre. It has infinite precision and never limits a result.
- A **measured** number is obtained by observation and is therefore uncertain:
  a station elevation of 412.3 m, a velocity of 5.5 km/s, a gravity reading of
  979 812.37 mGal.

> **Rule of consequence.** Only measured numbers limit precision. If you compute
> a distance from an exact speed and a measured time, the uncertainty of the
> *time* controls the answer.

## 3. Significant figures: the honest bookkeeping of precision

### 3.1 Definition

The **significant figures** of a written measured value are the digits that
carry information about the quantity, excluding leading zeros used only to place
the decimal point.

| Written value | Significant figures | Why |
|---|---|---|
| `0.00250` | 3 | leading zeros are placeholders; the trailing zero is significant |
| `2500` | ambiguous (2, 3 or 4) | trailing zeros with no decimal point |
| `2.500 × 10³` | 4 | the notation removes the ambiguity |
| `6.674 × 10⁻¹¹` | 4 | |

**This ambiguity is the single best argument for scientific notation.** Writing
`2500` does not tell the reader whether the last two zeros are meaningful.
Writing `2.500×10³` does.

### 3.2 Arithmetic rules

**Multiplication and division.** The result carries the *fewest* significant
figures of any input.

$$2.5 \times 10^{3}\ \mathrm{m} \;\div\; 3.1\times10^{2}\ \mathrm{s}
= 8.1\ \mathrm{m\,s^{-1}} \quad (\text{2 s.f., not } 8.0645\ldots)$$

**Addition and subtraction.** The result is limited by the *least precise
decimal place*, not the fewest digits.

$$412.3\ \mathrm{m} + 0.05\ \mathrm{m} = 412.4\ \mathrm{m} \quad (\text{tenths})$$

Note the trap: addition can *lose* significant figures even though no digits
were rounded away in an obvious way.

### 3.3 Why over-reporting is a form of dishonesty

If a gravimeter resolves 0.01 mGal and you report an anomaly as
`2.0437 mGal`, you have implied a precision of 5 significant figures that your
instrument cannot deliver. A reader who trusts that number may conclude the
target is deeper than it is. Reporting `2.04 mGal` communicates the real
information content.

> **The principle.** Report all the digits your measurement supports, and not
> one more. Both over- and under-reporting destroy information: the first
> invents precision, the second discards it.

## 4. Derivations and worked reasoning

### 4.1 Converting between unit systems — with dimensional checking

**Problem.** A gravity anomaly is given as 20.4 mGal. Express it in SI and in
µm/s² (a unit used by some modern instruments).

**Step 1 — write the conversion as an exact identity.**
$1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$ (by definition of the Gal).

**Step 2 — multiply by a dimensionless ratio equal to one.**

$$20.4\ \mathrm{mGal} \times \frac{10^{-5}\ \mathrm{m\,s^{-2}}}{1\ \mathrm{mGal}}
= 20.4 \times 10^{-5}\ \mathrm{m\,s^{-2}} = 2.04\times10^{-4}\ \mathrm{m\,s^{-2}}.$$

**Step 3 — convert to µm/s².** Since $\mu = 10^{-6}$,

$$2.04\times10^{-4}\ \mathrm{m\,s^{-2}} \times \frac{10^{6}\ \mu\mathrm{m}}{1\ \mathrm{m}}
= 204\ \mu\mathrm{m\,s^{-2}}.$$

**Step 4 — sanity-check the direction.** A mGal is a *small* unit, so the
numeric value should get *larger* when expressed in a smaller unit
(20.4 → 204). It did. Fixing unit errors is mostly this kind of reasoning.

**Step 5 — significant figures.** All conversions here are exact, so the 3
significant figures of `20.4` are preserved: $2.04\times10^{-4}$ m/s².

### 4.2 A dimensional check that catches real mistakes

Suppose a student derives the gravitational acceleration inside a uniform
sphere as $g = -\tfrac{4}{3}\pi G \rho r^{3}$ and reports it in m/s².

Check the dimensions. With $[G] = \mathrm{m^{3}\,kg^{-1}\,s^{-2}}$,
$[\rho] = \mathrm{kg\,m^{-3}}$, $[r] = \mathrm{m}$:

$$[\text{RHS}] = \mathrm{m^{3}\,kg^{-1}\,s^{-2}} \cdot \mathrm{kg\,m^{-3}} \cdot \mathrm{m^{3}}
= \mathrm{m^{3}\,s^{-2}} \neq \mathrm{m\,s^{-2}}.$$

The expression is dimensionally wrong. The correct interior field, derived
properly in [00-01-01 of the orientation module](../../00-orientation/01-study-roadmap/01-how-to-learn-geophysics.md),
is

$$g(r) = -\tfrac{4}{3}\pi G \rho\, r,$$

whose dimensions are $\mathrm{m^3 kg^{-1} s^{-2} \cdot kg\,m^{-3} \cdot m}
= \mathrm{m\,s^{-2}}$, as required. **Dimensional analysis caught a cubed-radius
error in one line.** This technique is developed systematically in
[01-03 Units and Dimensional Analysis](./03-units-and-dimensional-analysis.md).

### 4.3 Orders of magnitude and the scale of the target

**Problem.** An orebody of mass $M = 10^{9}\ \mathrm{kg}$ (about a 100 m sphere
of dense ore) lies at 300 m depth. Its peak surface gravity anomaly $g_z$ is
approximately that of a point mass,

$$g_{z} \approx \frac{G M}{d^{2}}.$$

Compute it.

$$g_{z} \approx \frac{(6.674\times10^{-11})(10^{9})}{(300)^{2}}
= \frac{6.674\times10^{-2}}{9.0\times10^{4}}
= 7.4\times10^{-7}\ \mathrm{m\,s^{-2}}.$$

Convert: $7.4\times10^{-7} / 10^{-5} = 7.4\times10^{-2}$ mGal, i.e. **0.074
mGal.** This is a *detectable* anomaly for a modern gravimeter (repeatability
~0.01–0.02 mGal) but only just, and it demands careful terrain and tidal
corrections. You have just done a first-order feasibility study in three lines —
this is what orders-of-magnitude reasoning buys you (developed in
[01-02 Orders of Magnitude](./02-orders-of-magnitude.md)).

## 5. Python demonstration

Save the following as `code/number_systems_demo.py` (provided in this module's
`code/` directory) and run it. Predict each output before running.

```python
"""Precision, significant figures and floating-point limits.

Run:  python3 number_systems_demo.py
Requires: Python standard library only.
"""

from decimal import Decimal, getcontext


def section(title: str) -> None:
    print(f"\n{'=' * 62}\n{title}\n{'=' * 62}")


def main() -> None:
    section("1. Binary floating point cannot represent most decimals")
    # 0.1 has no finite binary expansion, exactly as 1/3 has no finite decimal one.
    print(f"0.1 + 0.1 + 0.1 == 0.3 ?  {0.1 + 0.1 + 0.1 == 0.3}")
    print(f"0.1 + 0.1 + 0.1        =  {0.1 + 0.1 + 0.1!r}")
    print(f"exactly 0.3 as stored  =  {0.3!r}")
    print(f"difference             =  {(0.1 + 0.1 + 0.1) - 0.3:.3e}")

    section("2. Catastrophic cancellation")
    big = 1.0e16
    print(f"(1e16 + 1) - 1e16      =  {(big + 1.0) - big}   <- expected 1.0")
    print("Explanation: 1e16+1 rounds back to 1e16, so the 1 is lost entirely.")

    section("3. Machine epsilon: the spacing between representable numbers")
    import sys
    eps = sys.float_info.epsilon
    print(f"sys.float_info.epsilon =  {eps:.3e}")
    print(f"1.0 + eps/2 == 1.0 ?     {1.0 + eps / 2 == 1.0}")
    print(f"1.0 + eps   == 1.0 ?     {1.0 + eps == 1.0}")

    section("4. Naive summation accumulates error")
    # Sum n copies of 0.1 three ways and compare with the exact answer n/10.
    n = 100_000
    naive = 0.0
    for _ in range(n):
        naive += 0.1
    compensated = 0.0
    carry = 0.0
    for _ in range(n):
        y = 0.1 - carry
        t = compensated + y
        carry = (t - compensated) - y
        compensated = t
    exact = Decimal(n) / Decimal(10)
    print(f"naive sum       = {naive!r}")
    print(f"compensated sum = {compensated!r}")
    print(f"exact           = {exact}")
    print(f"naive error     = {float(abs(Decimal(naive) - exact)):.3e}")
    print(f"compensated err = {float(abs(Decimal(compensated) - exact)):.3e}")

    section("5. Decimal arithmetic when exactness is required")
    getcontext().prec = 50
    tenth = Decimal("0.1")
    print(f"Decimal('0.1') * 3 = {tenth * 3}")
    print(f"Decimal('0.1')*3 == Decimal('0.3') ? {tenth * 3 == Decimal('0.3')}")

    section("6. Significant figures: the honest way to report")
    # A gravimeter reading with 0.01 mGal resolution.
    reading = 2.0437          # instrument reports many digits...
    resolution = 0.01         # ...but resolves only hundredths
    # Defensible reporting: round to the resolution, then keep those digits.
    report = round(reading / resolution) * resolution
    print(f"raw reading      = {reading}")
    print(f"resolution       = {resolution} mGal")
    print(f"defensible value = {report:.2f} mGal   (3 significant figures)")

    section("7. Gravity worked example: point-mass anomaly (Section 4.3)")
    G = 6.674e-11              # m^3 kg^-1 s^-2
    mass = 1.0e9               # kg
    depth = 300.0              # m
    g_si = G * mass / depth ** 2
    print(f"g_z = {g_si:.3e} m/s^2")
    print(f"g_z = {g_si / 1e-5:.3e} mGal")
    print(f"Detectable at 0.01 mGal repeatability?  {g_si / 1e-5 > 0.01}")


if __name__ == "__main__":
    main()
```

### What to observe, and why it matters

| Observation | Consequence in geophysics |
|---|---|
| `0.1+0.1+0.1 != 0.3` | Never test equality of floats; use `abs(a-b) < tol` |
| `(1e16+1)-1e16 == 0.0` | Differencing large nearly-equal values destroys precision — the core of finite-difference error |
| `1.0 + eps/2 == 1.0` | There is a hard floor on the relative resolution of any float |
| Naive summation error grows with $n$ | Long time-series integrations must use compensated or block summation |
| `Decimal` is exact for decimal inputs | Financial-style exactness is available, but is *much* slower |

> **Breaking exercise.** Move the `n = 100_000` loop to `n = 10_000_000` and
> predict, before running, whether the naive error will grow roughly linearly
> with $n$. Then run it and check.

## 6. Exercises

Attempt these closed-book. Solutions are in
[`exercises/01-number-systems-and-precision-solutions.md`](./exercises/01-number-systems-and-precision-solutions.md).

### ★ Foundational

**★1.** Write each in scientific notation with 3 significant figures:
(a) 0.000482, (b) 91 300, (c) 0.6071, (d) 4 500 000.

**★2.** Convert to SI (m/s²): (a) 15.2 mGal, (b) −3.7 mGal, (c) 1.05 Gal.
Then convert each result to µm/s².

**★3.** State the number of significant figures: (a) `0.00340`, (b) `1.20×10⁴`,
(c) `700`, (d) `7.00×10²`.

**★4.** Perform the arithmetic and give the answer with the correct number of
significant figures: (a) $4.56 \times 2.1$, (b) $12.5 \div 0.25$,
(c) $101.3 + 0.44$.

### ★★ Applied

**★★5.** A magnetic anomaly is reported as `−1 250 nT`. Express it in tesla and
in gammas, given that $1\ \gamma = 1\ \mathrm{nT}$. If the instrument has 1 nT
resolution, how many significant figures may you defensibly quote?

**★★6.** A seismic wave travels 412 km in 68.4 s. Compute the average velocity
in km/s and in m/s, and state the significant figures your inputs justify.
Explain why reporting `6.02339 km/s` would be wrong.

**★★7.** Using the point-mass approximation $g_z = GM/d^2$, estimate the depth
at which a $10^{10}$ kg body produces exactly a 0.05 mGal anomaly. Work in
orders of magnitude first, then compute exactly. Does the answer depend on
whether the body is a sphere or a cube?

**★★8.** Propagate a rounding uncertainty: compute the area of a survey grid
measuring $1.25\ \mathrm{km} \times 0.80\ \mathrm{km}$, where each dimension is
known only to 2 significant figures. Give the area in km² and m² with the
correct number of significant figures, and state the relative uncertainty.

### ★★★ Research-oriented

**★★★9.** The naive-summation error in the demonstration grows with $n$. Design
and run an experiment that measures this growth: for $n$ in a geometric
sequence (10³, 10⁴, …, 10⁷), record the error of naive summation against the
exact `Decimal` result, and plot error versus $n$ on log–log axes. Report the
empirical growth exponent. Then explain, in terms of the floating-point model
in [01-04 Floating Point](./04-floating-point.md), why you would expect roughly
this exponent. This is a genuine numerical-experiment report: state the method,
the result, and the limits of your conclusion.

**★★★10.** The satellite-derived gravitational constant is
$G = 6.67430\times10^{-11}\ \mathrm{m^3\,kg^{-1}\,s^{-2}}$ with a relative
standard uncertainty of about $2.2\times10^{-5}$. A student computes the mass of
a body from measured $g_z$, $d$ using $M = g_z d^2/G$ and reports $M$ to 8
significant figures. Write a short critique: what relative uncertainty in $M$
does $G$ alone impose, and what would you report instead? (You do not need to
know the exact modern value to answer; use the relative uncertainty given.) The
systematic treatment of this kind of question is in
[01-13 Probability and Statistics Foundations](../13-probability-and-statistics-foundations/README.md).

## 7. Common mistakes

1. **Writing `2500` when you mean `2.500×10³`.** Ambiguous significant figures
   are a real communication failure, not pedantry.
2. **Carrying calculator digits into a report.** A calculator's `8.064516129...`
   is not a result; it is an intermediate.
3. **Testing float equality.** `if a == b:` on computed floats is a latent bug.
   Use a tolerance, and choose the tolerance from the physics, not arbitrarily.
4. **Treating a unit prefix as decoration.** `5.5` km/s and `5.5` m/s differ by
   three orders of magnitude and by whether your model is plausible.
5. **Believing that "more digits" means "more accurate".** Digits beyond the
   measurement's information content are noise presented as knowledge.
6. **Forgetting that subtraction can destroy precision.** $(a+\delta) - a$
   where $\delta \ll a$ loses almost all significant figures — central to
   numerical differentiation.

## 8. Real-world applications

- **Gravity and magnetic surveys.** Anomalies are quoted in mGal and nT, and
  the *precision* of the quoted value signals whether the anomaly is
  interpretable. A 0.02 mGal anomaly quoted from a 0.05 mGal-resolution survey
  is not evidence of anything.
- **Seismic velocity models.** Reporting $v_p = 6.02339$ km/s implies
  centimetre-per-second confidence in a quantity typically uncertain by
  ±0.05 km/s. Tomography papers that do this are misleading about their own
  resolution.
- **Instrument specification.** Dynamic range is specified in orders of
  magnitude, and it determines whether a target is detectable at all — the
  calculation in Section 4.3.
- **Satellite gravimetry.** GRACE-class missions measure mass changes
  corresponding to equivalent water heights of a few centimetres; the arithmetic
  of these tiny numbers is where the science actually lives.

## 9. Further reading

- **Higham, N. J. (2002). *Accuracy and Stability of Numerical Algorithms*
  (2nd ed.). SIAM.** Chapters 1–2. Level: advanced undergraduate upward. The
  definitive treatment of floating-point error analysis; Chapter 1 is the
  canonical reference for everything in Section 5.
- **Goldberg, D. (1991). What every computer scientist should know about
  floating-point arithmetic. *ACM Computing Surveys*, 23(1), 5–48.** Level:
  intermediate. The classic accessible survey. Widely available; check your
  library or the ACM Digital Library for current access.
- **IEEE 754-2019, *IEEE Standard for Floating-Point Arithmetic*.** Level:
  reference. The normative definition of binary floating point. Relevant
  because Python's `float` is IEEE 754 binary64.
- **Taylor, J. R. (1997). *An Introduction to Error Analysis* (2nd ed.).
  University Science Books.** Level: beginner to intermediate. The clearest
  treatment of significant figures, error propagation, and why measurement
  uncertainty rules everything. Chapters 1–3 map directly onto this lesson.
- **BIPM (2019). *The International System of Units (SI)* (9th ed.).**
  Level: reference. The authoritative source for SI definitions, including the
  2019 redefinition of the base units in terms of physical constants. Available
  from the BIPM.

> Note on citations: bibliographic details above are given so you can locate the
> works. This repository does not host or reproduce copyrighted text, and you
> should confirm current availability and editions through your library before
> citing them.

## 10. Related lessons

- [02 Orders of Magnitude and Fermi Estimation](./02-orders-of-magnitude.md) — uses the feasibility calculation from Section 4.3.
- [03 Units, SI Conventions and Dimensional Analysis](./03-units-and-dimensional-analysis.md) — the systematic version of Section 4.1–4.2.
- [04 Floating-Point Representation, Round-Off and Catastrophic Cancellation](./04-floating-point.md) — the full account of Section 5.
- [05 Absolute vs Relative Error, Conditioning and Stability](./05-error-and-conditioning.md) — where these numerical limits meet physical uncertainty.
- [00-01-01 How to Learn Geophysics](../../00-orientation/01-study-roadmap/01-how-to-learn-geophysics.md) — uses the sphere-gravity derivation from Section 4.2 as its worked example.
