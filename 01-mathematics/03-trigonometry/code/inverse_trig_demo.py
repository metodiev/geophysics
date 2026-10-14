"""Inverse trigonometric functions, branch ambiguity and take-off angles.

Run:  python3 inverse_trig_demo.py
Requires: Python standard library only.

Companion to lesson 01-03-03. The theme is that an inverse trigonometric
function cannot return information that was destroyed before you called it.

Sections
--------
1. Principal branches, and the second solution they discard
2. atan2 versus atan: quadrant bookkeeping
3. Recovering an azimuth when a naive arctangent fails
4. Sensitivity: the derivative of arcsin near a grazing ray
5. Take-off angle on a uniform sphere, and p = dT/dDelta checked exactly
6. Wrapped phases and phase unwrapping
"""

from __future__ import annotations

import math

DEG = math.pi / 180.0
R_EARTH = 6371.0  # km, IUGG mean radius


def section(title: str) -> None:
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def wrap_to_pi(x: float) -> float:
    """Wrap an angle in radians into the interval (-pi, pi]."""
    y = (x + math.pi) % (2.0 * math.pi) - math.pi
    return math.pi if y == -math.pi else y


def main() -> None:
    section("1. Principal branches, and the second solution they discard")
    print(f"{'input c':>10} {'asin c (deg)':>14} {'180 - asin':>12} {'acos c (deg)':>14}"
          f" {'atan c (deg)':>14}")
    for c in (-1.0, -0.5, 0.0, 0.5, math.sqrt(3) / 2, 1.0):
        a = math.degrees(math.asin(c))
        print(f"{c:>10.5f} {a:>14.6f} {180.0 - a:>12.6f} "
              f"{math.degrees(math.acos(c)):>14.6f} "
              f"{math.degrees(math.atan(c)):>14.6f}")
    print("\nasin returns values in [-90, 90] and acos in [0, 180]. Both are")
    print("principal branches: they discard all but one of the infinitely many")
    print("angles with that sine or cosine. The '180 - asin' column is the other")
    print("solution in [0, 360), which is what you need when the physics says the")
    print("answer lies outside the principal range. The two solutions merge only")
    print("at the extremes, c = -1 and c = 1.")

    section("2. atan2 versus atan: quadrant bookkeeping")
    print(f"{'y':>8} {'x':>8} {'atan(y/x) deg':>16} {'atan2(y,x) deg':>16}")
    for y, x in ((1.0, 1.0), (1.0, -1.0), (-1.0, -1.0), (-1.0, 1.0),
                 (1.0, 0.0), (0.0, 0.0)):
        if x != 0.0:
            naive = f"{math.degrees(math.atan(y / x)):>16.4f}"
        else:
            naive = f"{'undefined':>16}"
        print(f"{y:>8.1f} {x:>8.1f} {naive} {math.degrees(math.atan2(y, x)):>16.4f}")
    print("\nRows 2 and 3 have the same ratio y/x = -1, so atan cannot tell them")
    print("apart: it reports -45 for both. atan2 keeps the signs, returns 135 and")
    print("-135 respectively, and handles x = 0 without a special case. In")
    print("geophysics, if you compute an angle from a ratio, you have probably")
    print("made a sign error that only shows up in half of your survey.")

    section("3. Recovering an azimuth when a naive arctangent fails")
    # Station at the origin; compute the azimuth to four sources placed
    # symmetrically. Only atan2 gets all four right.
    print(f"{'east (km)':>10} {'north (km)':>11} {'atan(E/N) deg':>15}"
          f" {'atan2(E,N) deg':>16} {'true quadrant':>15}")
    for east, north in ((10.0, 10.0), (10.0, -10.0), (-10.0, -10.0), (-10.0, 10.0)):
        naive = math.degrees(math.atan(east / north))
        correct = math.degrees(math.atan2(east, north)) % 360.0
        name = ("NE" if north > 0 else "SE") if east > 0 else ("SW" if north < 0 else "NW")
        print(f"{east:>10.1f} {north:>11.1f} {naive:>15.4f} {correct:>16.4f} {name:>15}")
    print("\nThe naive column is wrong in three of four cases, and the sign")
    print("error is not visible unless you plot the result. Always atan2 for")
    print("azimuths, back-azimuths and dip directions.")

    section("4. Sensitivity: the derivative of arcsin near a grazing ray")
    print("d(asin x)/dx = 1/sqrt(1 - x^2), so it diverges as |x| approaches 1.")
    print(f"{'x':>10} {'asin x (deg)':>14} {'d(asin)/dx':>14} "
          f"{'angle error for dx=1e-9':>24}")
    for x in (0.0, 0.5, 0.9, 0.99, 0.9999, 1.0):
        if abs(x) < 1.0:
            der = 1.0 / math.sqrt(1.0 - x * x)
            err = math.degrees(der * 1e-9)
            der_text = f"{der:14.5f}"
            err_text = f"{err:24.6e}"
        else:
            der_text = "         inf"
            err_text = "                     inf"
        print(f"{x:>10.4f} {math.degrees(math.asin(min(1.0, x))):>14.6f} "
              f"{der_text} {err_text}")
    print("\nPractical consequence: an interface velocity inferred from a ray")
    print("that grazes a refractor at near-critical incidence inherits this")
    print("amplification. The measurement is fine; the inversion of it is not.")

    section("5. Take-off angle on a uniform sphere, and p = dT/dDelta checked")
    print("For a sphere of constant velocity v the rays are straight chords, and")
    print("the epicentral distance is Delta = pi - 2i, with i the take-off angle")
    print("from the downward vertical. Benndorf's law gives p = R sin(i)/v, and")
    print("the ray parameter must also equal dT/dDelta. Here everything is in")
    print("radians and seconds, so no degree conversion appears in the algebra.")
    v = 6.0  # km/s placeholder used for arithmetic only; not a real Earth model
    table = []
    for i_deg in range(0, 91, 10):
        i = i_deg * DEG
        delta = math.pi - 2.0 * i          # radians
        travel = 2.0 * R_EARTH * math.cos(i) / v
        table.append((i, delta, travel, R_EARTH * math.sin(i) / v))
    print(f"\n{'i (deg)':>9} {'Delta (deg)':>13} {'chord (km)':>13}"
          f" {'T (s)':>11} {'p = R sin i / v (s/rad)':>24}")
    for i, delta, travel, p in table:
        print(f"{math.degrees(i):>9.1f} {math.degrees(delta):>13.6f}"
              f" {2.0 * R_EARTH * math.cos(i):>13.4f} {travel:>11.4f} {p:>24.6f}")
    print("\nNow check numerically that the ray parameter equals dT/dDelta. The")
    print("midpoint rows use a 10 degree step; the fine rows repeat the test")
    print("with a 0.5 degree step to expose the truncation error.")
    print(f"\n{'midpoint i (deg)':>17} {'step (deg)':>11} {'dT/dDelta (s/rad)':>18}"
          f" {'p exact (s/rad)':>17} {'difference':>13}")
    for step_deg, label in ((10.0, "coarse"), (0.5, "fine")):
        step = step_deg * DEG
        i = 0.0
        while i < 89.9 * DEG:
            i2 = i + step
            d1 = math.pi - 2.0 * i
            d2 = math.pi - 2.0 * i2
            t1 = 2.0 * R_EARTH * math.cos(i) / v
            t2 = 2.0 * R_EARTH * math.cos(i2) / v
            slope = (t2 - t1) / (d2 - d1)
            mid = 0.5 * (i + i2)
            p_exact = R_EARTH * math.sin(mid) / v
            if label == "fine" and not (0.0 <= math.degrees(mid) <= 21.0):
                i = i2
                continue
            print(f"{math.degrees(mid):>17.2f} {step_deg:>11.2f} {slope:>18.6f}"
                  f" {p_exact:>17.6f} {abs(slope - p_exact):>13.3e}")
            i = i2
    print("\nThe identity dT/dDelta = p is exact, so every number in the last")
    print("column is truncation error of the finite difference, and it shrinks")
    print("as the step shrinks. This is the same trade-off you meet whenever a")
    print("derivative is estimated from a travel-time curve.")

    section("6. Wrapped phases and phase unwrapping")
    # A smooth phase ramp sampled coarsely, then wrapped into (-pi, pi].
    true_phase = [0.0 + 0.9 * k for k in range(24)]   # up to about 20 rad
    wrapped = [wrap_to_pi(p) for p in true_phase]
    unwrapped = [wrapped[0]]
    for value in wrapped[1:]:
        prev = unwrapped[-1]
        delta = wrap_to_pi(value - prev)
        unwrapped.append(prev + delta)
    print(f"{'k':>3} {'true (rad)':>12} {'wrapped (rad)':>14} {'unwrapped (rad)':>16}")
    for k in (0, 3, 7, 8, 11, 14, 20, 23):
        print(f"{k:>3} {true_phase[k]:>12.5f} {wrapped[k]:>14.5f} "
              f"{unwrapped[k]:>16.5f}")
    max_err = max(abs(u - t) for u, t in zip(unwrapped, true_phase))
    print(f"\nmaximum error after unwrapping = {max_err:.3e} rad")
    print("Unwrapping assumes the phase changes by less than pi between")
    print("samples. In interferometry and in phase-picking this assumption is")
    print("the whole method, and violating it is the standard failure mode.")


if __name__ == "__main__":
    main()
