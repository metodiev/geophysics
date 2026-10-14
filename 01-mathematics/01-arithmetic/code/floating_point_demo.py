"""Floating-point representation, round-off and catastrophic cancellation.

Run:  python3 floating_point_demo.py
Requires: Python standard library only.

Companion to lesson 01-01-04. Every number printed here was produced by this
script; predict each output before running it.
"""

import math
import struct
from decimal import Decimal, getcontext


def section(title: str) -> None:
    print(f"\n{'=' * 66}\n{title}\n{'=' * 66}")


def decompose(x: float) -> tuple[int, int, int]:
    """Split a binary64 value into (sign, biased exponent, mantissa field)."""
    bits = struct.unpack(">Q", struct.pack(">d", x))[0]
    return bits >> 63, (bits >> 52) & 0x7FF, bits & ((1 << 52) - 1)


def main() -> None:
    section("1. Anatomy of a binary64 value")
    print(f"sys.float_info.epsilon = {math.ulp(1.0):.6e}  (= 2**-52 = {2.0 ** -52:.6e})")
    print(f"decimal digits guaranteed: {53 * math.log10(2):.15f} -> ~16 significant digits")
    for value in (1.0, 0.1, -2.5, 6.674e-11):
        sign, exponent, mantissa = decompose(value)
        print(f"  {value!r:>12}: sign={sign} biased_exp={exponent} "
              f"unbiased={exponent - 1023} mantissa=0x{mantissa:013x}")

    section("2. 0.1 has no exact binary representation")
    getcontext().prec = 60
    print(f"stored value of 0.1 = {Decimal(0.1)}")
    print(f"0.1 + 0.1 + 0.1 == 0.3 ?  {0.1 + 0.1 + 0.1 == 0.3}")
    print(f"0.1 + 0.1 + 0.1        =  {0.1 + 0.1 + 0.1!r}")
    print(f"1/3 in decimal has the same problem: 0.333... is not 1/3")

    section("3. The gap between representable numbers (ulp)")
    for x in (1.0, 1024.0, 1.0e6, 1.0e16):
        print(f"  ulp({x:.0e}) = {math.ulp(x):.6e}   nextafter - x = "
              f"{math.nextafter(x, math.inf) - x:.6e}")
    big = 1.0e16
    print(f"(1e16 + 1) - 1e16 = {(big + 1.0) - big}   <- the 1 disappears")
    print(f"math.nextafter(1e16, inf) - 1e16 = {math.nextafter(big, math.inf) - big}")
    print("Explanation: at 1e16 the spacing is 2.0, so 1e16 + 1 rounds to 1e16.")

    section("4. Catastrophic cancellation: (1 - cos x) / x**2")
    print(f"{'x':>10} {'naive':>22} {'stable (half-angle)':>22} {'rel. err naive':>16}")
    for exponent in range(2, 10):
        x = 10.0 ** (-exponent)
        naive = (1.0 - math.cos(x)) / (x * x)
        s = math.sin(x / 2.0)
        stable = 2.0 * s * s / (x * x)
        rel_err = abs(naive - stable) / stable
        print(f"{x:>10.0e} {naive:>22.13f} {stable:>22.13f} {rel_err:>16.3e}")
    print("Limit as x -> 0 is 1/2. The naive form loses all precision once")
    print("1 - cos x is dominated by the rounding of cos x near 1.")

    section("5. Quadratic formula: avoid subtracting nearly equal numbers")
    # x**2 + b*x + c = 0 with b large: one root is well conditioned, the
    # other is computed as (-b + sqrt(b**2 - 4c))/2 and cancels.
    b, c = -1.0e8, 1.0
    disc = math.sqrt(b * b - 4.0 * c)
    root_big = (-b + disc) / 2.0
    root_small_naive = (-b - disc) / 2.0
    root_small_stable = 2.0 * c / (-b + disc)
    getcontext().prec = 50
    B, C = Decimal(-1.0e8), Decimal(1)
    exact_small = (-B - (B * B - 4 * C).sqrt()) / 2
    print(f"equation: x**2 + {b:.0e} x + {c} = 0")
    print(f"large root (naive)   = {root_big!r}")
    print(f"small root (naive)   = {root_small_naive!r}")
    print(f"small root (c/a/x1)  = {root_small_stable!r}")
    print(f"small root (exact)   = {float(exact_small)!r}")
    print(f"naive abs. error     = {float(abs(Decimal(root_small_naive) - exact_small)):.3e}")
    print(f"stable abs. error    = {float(abs(Decimal(root_small_stable) - exact_small)):.3e}")
    print(f"relative size of the two roots: {exact_small / Decimal(root_big):.1e}")

    section("6. Round-off accumulates differently in different summations")
    # Sum n copies of 0.1 four ways; compare with the exact value n/10.
    n = 1_000_000
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
    pairwise = math.fsum([0.1] * n)
    exact = Decimal(n) / Decimal(10)
    for name, value in (("naive (left to right)", naive),
                        ("Kahan compensated", compensated),
                        ("math.fsum (exact)", pairwise)):
        err = float(abs(Decimal(value) - exact))
        print(f"{name:>22}: {value!r}  abs err = {err:.3e}  rel err = {err / 1.0e5:.2e}")
    print(f"{'exact n/10':>22}: {exact}")

    section("7. Round-off sets the floor of numerical differentiation")
    # Forward difference of sin(x) at x = 1: truncation error ~ h/2,
    # round-off error ~ eps/h. The best h is near sqrt(eps) for this scheme.
    x0, true_derivative = 1.0, math.cos(1.0)
    print(f"f(x) = sin x, f'(1) = cos(1) = {true_derivative:.16f}")
    print(f"{'h':>10} {'forward difference':>22} {'abs error':>14}")
    h = 1.0e-1
    while h > 1.0e-17:
        approx = (math.sin(x0 + h) - math.sin(x0)) / h
        print(f"{h:>10.0e} {approx:>22.16f} {abs(approx - true_derivative):>14.3e}")
        h *= 0.1
    print(f"sqrt(eps) = {math.sqrt(math.ulp(1.0)):.3e} (the expected best h here);")
    print("the central difference (f(x+h)-f(x-h))/(2h) has a better floor, "
          "because its truncation error is O(h**2), so its best h is ~eps**(1/3).")

    section("8. Geophysics: Bouguer anomaly by differencing huge numbers")
    # Observed and theoretical gravity differ by a small anomaly.
    observed = 979_812.37       # mGal, made-up but realistic magnitude
    theoretical = 979_802.15    # mGal
    anomaly = observed - theoretical
    print(f"observed    = {observed} mGal   (16 significant digits stored)")
    print(f"theoretical = {theoretical} mGal")
    print(f"anomaly     = {anomaly:.2f} mGal")
    print(f"decimal digits absorbed by the common part: "
          f"{math.log10(observed / anomaly):.2f}")
    print("The subtraction is exact for these two values, but the ~1e-10 mGal")
    print("rounding in each 979000 mGal datum is itself ~1e-5 of the anomaly.")


    section("9. Subtraction is not always lossy: exact cancellation (Sterbenz)")
    # If two floats are within a factor of two of each other, their difference
    # is computed exactly. Compare each float difference with the exact result
    # taken from the decimal expansions of the two inputs.
    print(f"{'a':>20} {'b':>20} {'exact?':>7} {'within factor 2?':>17}")
    for a, b in ((1e5, 99999.9999999999), (1.0, 0.5000000000000001),
                 (10.0, 3.0), (1.0, 1.0 / 3.0)):
        exact = Decimal(a - b) == Decimal(a) - Decimal(b)
        within = (b / 2.0 <= a <= 2.0 * b) or (a / 2.0 <= b <= 2.0 * a)
        print(f"{a:>20} {b:>20} {str(exact):>7} {str(within):>17}")
    print("Exact when it is inside the factor-of-two range, inexact outside it.")
    print("The loss attributed to 'cancellation' is therefore the loss of the")
    print("*inputs*' stored precision, not an error introduced by the subtraction.")


if __name__ == "__main__":
    main()
