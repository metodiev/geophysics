"""Limits, one-sided limits and asymptotic behaviour, probed numerically.

Run:  python3 limits_demo.py
Requires: Python standard library only.

Companion to lesson 01-05-01. The point of every section is the same: a limit is
a *statement about a trend*, not the value you happen to compute on the way
there. Section 1 shows a limit that the arithmetic cannot reach; Section 3 shows
a limit that does not exist.
"""

import math

G = 6.674e-11  # gravitational constant, m^3 kg^-1 s^-2


def section(title: str) -> None:
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def main() -> None:
    section("1. lim_{x->0} sin(x)/x = 1, but the computer stops approaching")
    print(f"{'x':>10}  {'sin(x)/x':>22}  {'1 - sin(x)/x':>14}")
    for exponent in range(1, 17):
        x = 10.0 ** (-exponent)
        ratio = math.sin(x) / x
        print(f"{x:>10.0e}  {ratio!r:>22}  {1.0 - ratio:>14.3e}")
    print("\nReading: the ratio is 1 to seven digits by x = 1e-6, and from")
    print("x = 1e-8 onwards the printed value is exactly 1.0.")

    section("2. lim_{n->inf} (1 + 1/n)^n = e")
    print(f"{'n':>12}  {'(1+1/n)**n':>22}  {'e - value':>12}")
    for exponent in (0, 1, 2, 3, 4, 6, 8):
        n = 10 ** exponent
        value = (1.0 + 1.0 / n) ** n
        print(f"{n:>12}  {value!r:>22}  {math.e - value:>12.3e}")
    print(f"e = {math.e!r}")

    section("3. A one-sided limit that does not exist: a first-order discontinuity")
    # Uniform crust and mantle speeds (ILLUSTRATIVE, rounded to one figure of
    # accuracy). The Moho is modelled as a mathematical jump.
    v_crust, v_mantle, z_moho = 6.0, 8.0, 33.0

    def v_sharp(z: float) -> float:
        return v_crust if z < z_moho else v_mantle

    # A sigmoid replacement one ten-thousandth of a kilometre wide.
    def v_smooth(z: float, width: float = 1.0e-4) -> float:
        return v_crust + (v_mantle - v_crust) / (
            1.0 + math.exp(-(z - z_moho) / width)
        )

    for h in (1.0e-1, 1.0e-2, 1.0e-3, 1.0e-6):
        left = v_sharp(z_moho - h)
        right = v_sharp(z_moho + h)
        print(f"  h={h:8.0e}  v(z0-h)={left:.4f}  v(z0+h)={right:.4f}"
              f"  jump={right - left:.4f}")
    print("  smoothed model, 1e-6 km from the Moho:"
          f" v = {v_smooth(z_moho + 1.0e-6):.6f} km/s")
    print("  smoothed model, at the Moho:            "
          f"v = {v_smooth(z_moho):.6f} km/s")
    print("  smoothed model, 1e-6 km below:          "
          f"v = {v_smooth(z_moho - 1.0e-6):.6f} km/s")
    print("\nReading: the jump model has no limit at z0 - only one-sided")
    print("limits differing by the jump. Replacing the jump by any continuous")
    print("ramp restores a limit, and the value at z0 is the ramp midpoint.")

    section("4. Limit at infinity: a finite disc potential tends to GM/z")
    mass, radius = 1.0e10, 1000.0  # kg, m
    print(f"{'z (m)':>12}  {'V exact (J/kg)':>18}  {'GM/z (J/kg)':>16}"
          f"  {'rel. difference':>16}")
    for z in (1.0e3, 1.0e4, 1.0e5, 1.0e6, 1.0e7):
        exact = 2.0 * G * mass / (math.sqrt(radius * radius + z * z) + z)
        point = G * mass / z
        print(f"{z:>12.0e}  {exact:>18.6e}  {point:>16.6e}"
              f"  {(exact - point) / point:>16.3e}")
    print("\nReading: the relative difference falls as (a/z)^2. A finite body")
    print("is indistinguishable from a point mass only in the limit, and the")
    print("approach is second order in a/z - which is why gravity anomalies")
    print("need a depth smaller than the survey aperture to be resolvable.")

    section("5. Catastrophic cancellation in the naive disc formula")
    print(f"{'z (m)':>12}  {'naive':>20}  {'stable':>20}  {'rel. error':>12}")
    for z in (1.0e3, 1.0e5, 1.0e7, 1.0e9, 1.0e11):
        naive = (2.0 * G * mass / (radius ** 2)) * (
            math.sqrt(radius * radius + z * z) - z
        )
        stable = 2.0 * G * mass / (math.sqrt(radius * radius + z * z) + z)
        error = abs(naive - stable) / stable
        print(f"{z:>12.0e}  {naive:>20.8e}  {stable:>20.8e}  {error:>12.3e}")
    print("\nReading: both expressions have the same limit, but the naive one")
    print("loses every significant figure once z >> a. The limit is a")
    print("statement about exact arithmetic; your formula must survive the")
    print("floating point you actually have.")

    section("6. Divergence and integrable growth near a point source")
    print(f"{'r (m)':>10}  {'1/r (1/m)':>14}  {'r^2/r (m)':>14}  {'4 pi r^2 (m^2)':>16}")
    for exponent in (3, 1, -1, -3, -6):
        r = 10.0 ** exponent
        print(f"{r:>10.0e}  {1.0 / r:>14.3e}  {r * r / r:>14.3e}"
              f"  {4.0 * math.pi * r * r:>16.3e}")
    print("\nReading: 1/r is unbounded as r -> 0, yet the weighted quantity")
    print("4 pi r^2 * (1/r) = 4 pi r tends to zero. Whether a singularity")
    print("destroys an integral depends on the weight attached to it - the")
    print("subject of lesson 01-05-06.")


if __name__ == "__main__":
    main()
