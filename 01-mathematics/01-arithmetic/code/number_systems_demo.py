"""Precision, significant figures and floating-point limits.

Run:  python3 number_systems_demo.py
Requires: Python standard library only.

Companion to lesson 01-01-01. Predict each output before running it; the
predictions you get wrong are the ones that teach you something.
"""

from decimal import Decimal, getcontext
import sys


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
