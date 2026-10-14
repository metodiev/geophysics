"""Absolute vs relative error, conditioning and numerical stability.

Run:  python3 conditioning_demo.py
Requires: Python standard library only.

Companion to lesson 01-01-05. Every printed number comes from this script.
The two ideas to keep separate:

  conditioning  - a property of the *problem*; how much input error can grow
  stability     - a property of the *algorithm*; whether it introduces its own
                  error beyond what the conditioning forces
"""

import math
from decimal import Decimal, getcontext
from fractions import Fraction


def section(title: str) -> None:
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


# --------------------------------------------------------------------------
# Gaussian elimination: float (partial pivoting) and exact (Fraction)
# --------------------------------------------------------------------------

def solve_float(matrix: list[list[float]], rhs: list[float]) -> list[float]:
    n = len(matrix)
    a = [row[:] + [rhs[i]] for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(a[r][col]))
        a[col], a[pivot] = a[pivot], a[col]
        for r in range(col + 1, n):
            factor = a[r][col] / a[col][col]
            for c in range(col, n + 1):
                a[r][c] -= factor * a[col][c]
    x = [0.0] * n
    for r in range(n - 1, -1, -1):
        total = a[r][n] - sum(a[r][c] * x[c] for c in range(r + 1, n))
        x[r] = total / a[r][r]
    return x


def solve_fraction(matrix: list[list[Fraction]], rhs: list[Fraction]) -> list[Fraction]:
    """Exact elimination over the rationals; the reference solution."""
    n = len(matrix)
    a = [row[:] + [rhs[i]] for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = next(r for r in range(col, n) if a[r][col] != 0)
        a[col], a[pivot] = a[pivot], a[col]
        for r in range(col + 1, n):
            factor = a[r][col] / a[col][col]
            for c in range(col, n + 1):
                a[r][c] -= factor * a[col][c]
    x = [Fraction(0)] * n
    for r in range(n - 1, -1, -1):
        total = a[r][n] - sum(a[r][c] * x[c] for c in range(r + 1, n))
        x[r] = total / a[r][r]
    return x


def hilbert(n: int) -> list[list[float]]:
    return [[1.0 / (i + j + 1.0) for j in range(n)] for i in range(n)]


def main() -> None:
    getcontext().prec = 60

    section("1. Absolute error is useless without a scale")
    print(f"{'case':>34} {'abs err':>12} {'rel err':>12}")
    cases = (
        ("P-wave speed, 6000 +- 1 m/s", 6000.0, 1.0),
        ("P-wave speed,   60 +- 1 m/s", 60.0, 1.0),
        ("Earth radius 6371e3 +- 1e3 m", 6371.0e3, 1.0e3),
        ("Mantle viscosity 1e21 +- 1e18", 1.0e21, 1.0e18),
    )
    for name, exact, err in cases:
        print(f"{name:>34} {err:>12.3e} {err / exact:>12.3e}")
    print("An absolute error of 1 m/s is negligible at 6000 m/s and a 1.7%")
    print("error at 60 m/s. Relative error is what propagates.")

    section("2. Condition number of a function: how much can f amplify x?")
    # cond(f, x) = |x f'(x) / f(x)|, estimated with a central difference.
    def cond(f, x: float) -> float:
        h = abs(x) * 1.0e-5 + 1.0e-12
        deriv = (f(x + h) - f(x - h)) / (2.0 * h)
        return abs(x * deriv / f(x))

    probes = (
        ("exp(x) at x = 10", math.exp, 10.0, 10.0),
        ("exp(x) at x = 20", math.exp, 20.0, 20.0),
        ("ln(x) at x = 1.0001", math.log, 1.0001, 1.0 / abs(math.log(1.0001))),
        ("ln(x) at x = 1e6", math.log, 1.0e6, 1.0 / abs(math.log(1.0e6))),
        ("sin(x) at x = 1.0", math.sin, 1.0, 1.0 / math.tan(1.0)),
        ("sqrt(x) at x = 1e-8", math.sqrt, 1.0e-8, 0.5),
    )
    print(f"{'function':>22} {'num. cond':>12} {'analytic':>12}")
    for name, f, x, analytic in probes:
        print(f"{name:>22} {cond(f, x):>12.4f} {analytic:>12.4f}")
    print("exp is mildly ill-conditioned with cond = x (so 20 at x = 20: a")
    print("1e-16 relative input error becomes 2e-15 relative output error).")
    print("ln has cond = 1/|ln x|: about 1e4 near x = 1, but only 0.07 at x = 1e6.")
    print("Conditioning is a property of the point as much as of the function.")

    section("3. Cancellation in exp(x) - 1 for small x")
    print(f"{'x':>8} {'exp(x) - 1':>22} {'expm1(x)':>22} {'rel err':>10} {'cond':>9}")
    for exponent in range(1, 12):
        x = 10.0 ** (-exponent)
        naive = math.exp(x) - 1.0
        good = math.expm1(x)
        print(f"{x:>8.0e} {naive:>22.13e} {good:>22.13e} "
              f"{abs(naive - good) / good:>10.2e} {1.0 / x:>9.1e}")
    print("cond = x/(e**x - 1) -> 1/x, so the relative error is amplified by 1/x.")

    section("4. Well-conditioned and ill-conditioned linear systems")
    print("Hilbert matrix H[i][j] = 1/(i+j-1), right-hand side = (1, ..., 1)")
    print(f"{'n':>3} {'max |x_float - x_exact|':>24} {'max rel err':>12}")
    for n in (3, 5, 8, 10):
        exact = solve_fraction(
            [[Fraction(1, i + j + 1) for j in range(n)] for i in range(n)],
            [Fraction(1) for _ in range(n)],
        )
        approx = solve_float(hilbert(n), [1.0] * n)
        abs_err = max(abs(Decimal(approx[i]) - Decimal(exact[i].numerator) / Decimal(exact[i].denominator))
                      for i in range(n))
        rel_err = max(abs(Decimal(approx[i]) - Decimal(exact[i].numerator) / Decimal(exact[i].denominator))
                      / abs(Decimal(exact[i].numerator) / Decimal(exact[i].denominator))
                      for i in range(n))
        print(f"{n:>3} {float(abs_err):>24.3e} {float(rel_err):>12.3e}")
    print("The data (1/(i+j-1)) are given to full double precision; nothing is")
    print("'noisy'. Yet the computed solution loses digits as n grows: the")
    print("problem itself is ill-conditioned, not the elimination routine.")

    section("5. Conditioning vs stability: I_n = integral of x**n/(x+10) on [0,1]")
    # Forward recurrence: I_n = 1/n - 10*I_{n-1}, starting from I_0 = ln(1.1).
    reference = {}
    prev = Decimal(11).ln() - Decimal(10).ln()  # ln(1.1) to 60 digits
    reference[0] = prev
    for n in range(1, 21):
        prev = Decimal(1) / Decimal(n) - 10 * prev
        reference[n] = prev

    forward = [math.log(1.1)]
    for n in range(1, 21):
        forward.append(1.0 / n - 10.0 * forward[n - 1])

    backward = [None] * 21
    backward[20] = float(Decimal(1) / Decimal(11 * 21))  # I_n is between 1/(11(n+1)) and 1/(10(n+1))
    for n in range(20, 0, -1):
        backward[n - 1] = (1.0 / n - backward[n]) / 10.0

    print(f"{'n':>3} {'reference I_n':>18} {'forward err':>12} {'backward err':>13}")
    for n in (0, 4, 8, 10, 12, 15, 18, 20):
        err_f = abs(Decimal(forward[n]) - reference[n]) / abs(reference[n])
        err_b = abs(Decimal(backward[n]) - reference[n]) / abs(reference[n])
        print(f"{n:>3} {float(reference[n]):>18.12f} {float(err_f):>12.2e} {float(err_b):>13.2e}")
    print(f"I_15 computed forward = {forward[15]!r}  (negative: meaningless, ")
    print("since the integrand is positive everywhere)")
    print("Reference values came from the same recurrence run in Decimal at 60")
    print("digits; the forward recurrence is a *stability* failure (factor 10")
    print("error growth per step), while the backward recurrence damps by 1/10.")


if __name__ == "__main__":
    main()
