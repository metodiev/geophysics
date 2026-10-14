"""Types, variables and operator semantics in a gravity calculation.

Run:  python3 types_variables_demo.py
Requires: Python standard library only.

Companion to lesson 03-01-02.  Every claim about floating point made in the
lesson is demonstrated here and the output quoted in the lesson is this script's
actual output.

Demonstrates:

1. The type of every literal and result, and what ``/`` versus ``//`` gives.
2. Why ``0.1 + 0.2 != 0.3`` and what "IEEE-754 double" actually means.
3. Accumulation error in a 1,000,000-term reduction, and ``math.fsum``.
4. A mixed int/float gravity model and the integer-division trap in it.
5. Exact arithmetic with ``fractions`` and ``decimal`` when it is warranted.
6. Aliasing: two names, one object.
"""

import math
from decimal import Decimal
from fractions import Fraction

from geophys_core import G, M_PER_S2_PER_MGAL, FREE_AIR_GRADIENT_MGAL_PER_M

DELTA_RHO = 300.0
RADIUS = 200.0
DEPTH = 500.0


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def part1_types():
    section("1. Literals, types and the two division operators")
    samples = [
        ("7", 7),
        ("7.0", 7.0),
        ("7 / 2", 7 / 2),
        ("7 // 2", 7 // 2),
        ("-7 // 2", -7 // 2),
        ("7 % 2", 7 % 2),
        ("-7 % 2", -7 % 2),
        ("2 ** 10", 2 ** 10),
        ("-2 ** 2", -2 ** 2),
        ("(-2) ** 2", (-2) ** 2),
        ("2 ** -1", 2 ** -1),
        ("3 * 0.1", 3 * 0.1),
        ("10 ** 30", 10 ** 30),
        ("10.0 ** 30", 10.0 ** 30),
    ]
    print(f"  {'expression':<12} {'value':<32} type")
    for expr, value in samples:
        print(f"  {expr:<12} {repr(value):<32} {type(value).__name__}")
    print()
    print("  Two facts worth memorising: '//' floors towards minus infinity,")
    print("  and '**' binds tighter than unary minus, so -2 ** 2 is -4.")


def part2_float():
    section("2. What a float is, and what 0.1 + 0.2 really is")
    print(f"  sys.float_info.epsilon = {__import__('sys').float_info.epsilon!r}")
    print(f"  0.1                    = {0.1!r}")
    print(f"  0.1 + 0.2              = {0.1 + 0.2!r}")
    print(f"  (0.1 + 0.2) == 0.3     = {(0.1 + 0.2) == 0.3}")
    print(f"  0.1 + 0.2 - 0.3        = {(0.1 + 0.2) - 0.3!r}")
    print(f"  math.isclose to 1e-15  = {math.isclose(0.1 + 0.2, 0.3, rel_tol=1e-15)}")
    print()
    print("  A double carries about 15.95 significant decimal digits.  For a")
    print("  gravity value near 9.8e5 mGal that is a resolution of about")
    print(f"  1e-10 mGal - far below instrument noise, which is the reason")
    print("  nobody needs more than a double for a gravity survey.")
    print()
    print("  The same 53-bit mantissa is why coordinates have a hard floor:")
    print(f"  the smallest representable longitude step near 0 deg is"
          f" {math.ulp(0.0) or 5e-324:.1e} deg,")
    print(f"  but near 180 deg it is {math.ulp(180.0):.3e} deg"
          f" = {math.ulp(180.0) * 111.32e3:.3e} m.")


def part3_accumulation():
    section("3. Accumulation error over a 1,000,000-station profile")
    n = 1_000_000
    step = FREE_AIR_GRADIENT_MGAL_PER_M
    naive = 0.0
    for _ in range(n):
        naive += step
    compensated = math.fsum([step] * n)
    exact = Fraction(3086, 10000) * n
    print(f"  adding {step} mGal exactly {n:,} times")
    print(f"  naive loop sum        = {naive!r}")
    print(f"  math.fsum             = {compensated!r}")
    print(f"  exact rational value  = {exact}")
    print(f"  naive  - exact        = {naive - float(exact):.4e} mGal"
          f"   ({(naive - float(exact)) / float(exact):.2e} relative)")
    print(f"  fsum   - exact        = {compensated - float(exact):.4e} mGal")
    print(f"  ulp of the final sum  = {math.ulp(float(exact)):.4e} mGal")
    print()
    print("  The naive error is about 96 thousand ulps of the running total:")
    print("  each addition rounds to the current magnitude, and the running total")
    print("  grows, so later steps inject larger absolute errors than earlier")
    print("  ones.  The result is an error of order n*eps times the final")
    print("  magnitude, of which the measured value here is a few per cent.")
    print("  Eleven significant digits survive, which is harmless for a total")
    print("  anomaly but *not* harmless when the same 5.6e-6 mGal is the signal")
    print("  you are trying to resolve - a microgravity survey.")
    print("  math.fsum uses compensated (Neumaier) summation and returns the")
    print("  correctly rounded result.")


def part4_int_float_trap():
    section("4. The integer-division trap inside a gravity model")
    n_stations = 7
    spacing_m = 20.0
    # WRONG: true division is fine here, but the *mean offset* of the first
    # half of the line is a classic place where people write // by accident.
    print(f"  n_stations = {n_stations}, spacing = {spacing_m} m")
    print(f"  half the line (/)  = {n_stations / 2} stations")
    print(f"  half the line (//) = {n_stations // 2} stations")
    print()
    mass = (4.0 / 3.0) * math.pi * RADIUS ** 3 * DELTA_RHO
    peak = G * mass * DEPTH / (DEPTH ** 2) ** 1.5 / M_PER_S2_PER_MGAL
    print(f"  mass   (floats) = {mass:.6e} kg    type {type(mass).__name__}")
    print(f"  peak   (floats) = {peak:.6f} mGal")
    print()
    print("  Had the mass been written with '//' the 4/3 would have become 1,")
    print("  silently losing 25 per cent of the source mass and 25 per cent of")
    print("  the anomaly.  Python does not warn: 4 // 3 is a perfectly legal")
    print("  int.  Test the forward model against a known value (lesson 07).")


def part5_exact():
    section("5. When exactness is worth it: Fraction and Decimal")
    print("  A station interval of 0.1 m cannot be stored exactly as a float:")
    naive = 0.0
    for _ in range(10):
        naive += 0.1
    print(f"  ten additions of 0.1 m   = {naive!r} m")
    exact = Fraction(1, 10) * 10
    print(f"  Fraction(1,10) * 10      = {exact}  -> exactly one metre")
    print(f"  Decimal('0.1') * 10      = {Decimal('0.1') * 10}")
    print()
    print("  Use Fraction for small closed-form checks and Decimal when a")
    print("  contract or a log file specifies decimal digits.  Use float for")
    print("  everything physical: sensors do not deliver 16 exact digits.")


def part6_aliasing():
    section("6. Variables are names for objects, not boxes")
    a = [0.1, 0.2, 0.3]
    b = a                # not a copy
    c = a[:]             # a copy
    b.append(0.4)
    print(f"  a = {a}")
    print(f"  b = a, then b.append(0.4)")
    print(f"  a is b                  -> {a is b}")
    print(f"  a == b                  -> {a == b}")
    print(f"  c = a[:] before the append: c = {c}  (c is a -> {c is a})")
    print()
    print("  This is the single most common source of 'impossible' bugs in")
    print("  array code: two names, one buffer.  Lesson 05 gives the rules for")
    print("  which types are mutable; lesson 02-02's NumPy views make the same")
    print("  distinction one directory over.")


if __name__ == "__main__":
    part1_types()
    part2_float()
    part3_accumulation()
    part4_int_float_trap()
    part5_exact()
    part6_aliasing()
