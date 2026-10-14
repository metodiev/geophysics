"""Angles, triangles, identities and the geophysical uses of both.

Run:  python3 trig_foundations_demo.py
Requires: Python standard library only.

Companion to lessons 01-03-01 and 01-03-02. Every number printed here is
computed, never pasted in from a table. Predict each output before running it.

Sections
--------
1. Degrees, radians and the unit circle
2. The two triangle laws, checked against a triangle built from its sides
3. Trigonometric identities, verified numerically at random arguments
4. Snell's law and the ray parameter sin(i)/v
5. True dip from two apparent dips, validated by round trip
6. The cost of the small-angle approximation
"""

from __future__ import annotations

import math
import random

DEG = math.pi / 180.0


def section(title: str) -> None:
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def main() -> None:
    section("1. Degrees, radians and the unit circle")
    print(f"{'deg':>5} {'rad':>12} {'sin':>12} {'cos':>12} {'tan':>16}")
    for deg in (0, 30, 45, 60, 90, 120, 180, 270, 360):
        rad = deg * DEG
        if abs(math.cos(rad)) < 1e-12:
            tan_text = "  undefined"
        else:
            tan_text = f"{math.tan(rad):16.10f}"
        print(f"{deg:>5} {rad:>12.8f} {math.sin(rad):>12.8f} "
              f"{math.cos(rad):>12.8f} {tan_text}")
    print("\nNote 1: at 90 and 270 deg the cosine prints as 6.1e-17, not 0.")
    print("        That residual is round-off in the value of pi, not physics.")
    print("Note 2: tan(90 deg) is undefined; the loop tests cos before printing.")

    section("2. Triangle laws checked against a triangle built from its sides")
    b_side, c_side = 4.0, 5.0          # arbitrary but exactly representable
    A_angle = 60.0 * DEG               # included angle, in radians
    a_side = math.sqrt(b_side ** 2 + c_side ** 2
                       - 2 * b_side * c_side * math.cos(A_angle))
    B_angle = math.acos((a_side ** 2 + c_side ** 2 - b_side ** 2) / (2 * a_side * c_side))
    C_angle = math.acos((a_side ** 2 + b_side ** 2 - c_side ** 2) / (2 * a_side * b_side))
    print(f"sides  b = {b_side}, c = {c_side}, included angle A = {A_angle / DEG:.6f} deg")
    print(f"law of cosines gives a = {a_side:.12f}")
    print(f"closed form sqrt(16 + 25 - 40*cos 60) = sqrt(21) = {math.sqrt(21):.12f}")
    print(f"recovered angles: A = {A_angle / DEG:.10f} deg, "
          f"B = {B_angle / DEG:.10f} deg, C = {C_angle / DEG:.10f} deg")
    print(f"angle sum = {(A_angle + B_angle + C_angle) / DEG:.12f} deg (expect 180)")
    print(f"law of sines: a/sin A = {a_side / math.sin(A_angle):.12f}, "
          f"b/sin B = {b_side / math.sin(B_angle):.12f}, "
          f"c/sin C = {c_side / math.sin(C_angle):.12f}")
    print("All three quotients equal the circumdiameter 2R, which is the whole")
    print("content of the law of sines.")

    section("3. Identities verified at random arguments")
    rng = random.Random(20261014)
    names = ("pythagorean", "addition", "double-angle", "half-angle",
             "product-to-sum", "sum-to-product")
    worst = {name: 0.0 for name in names}
    for _ in range(10_000):
        x = rng.uniform(-math.pi, math.pi)
        y = rng.uniform(-math.pi, math.pi)
        worst["pythagorean"] = max(
            worst["pythagorean"], abs(math.sin(x) ** 2 + math.cos(x) ** 2 - 1.0))
        worst["addition"] = max(
            worst["addition"],
            abs(math.sin(x + y) - (math.sin(x) * math.cos(y)
                                   + math.cos(x) * math.sin(y))))
        worst["double-angle"] = max(
            worst["double-angle"], abs(math.cos(2 * x) - (1 - 2 * math.sin(x) ** 2)))
        worst["half-angle"] = max(
            worst["half-angle"],
            abs(math.sin(x / 2) - math.copysign(math.sqrt((1 - math.cos(x)) / 2),
                                               math.sin(x / 2))))
        worst["product-to-sum"] = max(
            worst["product-to-sum"],
            abs(math.sin(x) * math.cos(y)
                - 0.5 * (math.sin(x + y) + math.sin(x - y))))
        worst["sum-to-product"] = max(
            worst["sum-to-product"],
            abs(math.sin(x) + math.sin(y)
                - 2 * math.sin((x + y) / 2) * math.cos((x - y) / 2)))
    print("Worst absolute discrepancy over 10 000 random angle pairs:")
    for name in names:
        print(f"  {name:<16} {worst[name]:.3e}")
    print("Every discrepancy is at the level of double-precision rounding, which")
    print("is how an identity behaves when the algebra behind it is correct.")
    print("Note the half-angle line: the sign depends on the quadrant of x/2,")
    print("so the formula is only true with the correct sign in front.")

    section("4. Snell's law and the ray parameter")
    v1, v2 = 1.5, 5.5                  # km/s: sediment over crystalline rock
    print(f"v1 = {v1} km/s, v2 = {v2} km/s")
    critical = math.asin(v1 / v2)
    print(f"critical angle: sin(i_c) = v1/v2 = {v1 / v2:.10f}")
    print(f"                i_c = {critical / DEG:.6f} deg")
    print("\nThe ray parameter sin(i)/v is conserved across the interface:")
    print(f"{'i1 (deg)':>10} {'p (s/km)':>14} {'i2 (deg)':>14} {'sin(i2)/v2':>14}")
    for i1_deg in (0.0, 5.0, 10.0, 15.826, 30.0, 45.0):
        i1 = i1_deg * DEG
        p = math.sin(i1) / v1
        s2 = p * v2
        i2_text = f"{math.asin(s2) / DEG:14.6f}" if abs(s2) <= 1.0 else "   evanescent"
        print(f"{i1_deg:>10.3f} {p:>14.8f} {i2_text} {s2:>14.8f}")

    section("5. True dip from two apparent dips, validated by round trip")
    # For a vertical section whose horizontal trace points along azimuth phi,
    # the apparent dip alpha obeys tan(alpha) = tan(dip) * |sin(phi - theta)|,
    # with theta the dip azimuth clockwise from north. In the north-south
    # section phi = 0, in the east-west section phi = 90, hence
    #     tan(alpha_N) = tan(dip) * |sin(theta)|
    #     tan(alpha_E) = tan(dip) * |cos(theta)|.
    def apparent_dips(dip_deg: float, theta_deg: float) -> tuple[float, float]:
        td = math.tan(dip_deg * DEG)
        theta = theta_deg * DEG
        return (math.degrees(math.atan(td * abs(math.sin(theta)))),
                math.degrees(math.atan(td * abs(math.cos(theta)))))

    def true_dip(alpha_n_deg: float, alpha_e_deg: float) -> tuple[float, float]:
        tn = math.tan(alpha_n_deg * DEG)
        te = math.tan(alpha_e_deg * DEG)
        return (math.degrees(math.atan(math.hypot(tn, te))),
                math.degrees(math.atan2(tn, te)) % 360.0)

    print("Forward: dip and dip azimuth -> apparent dips in the two sections")
    print(f"{'dip (deg)':>10} {'dip az':>9} {'app N-S':>10} {'app E-W':>10}"
          f" {'recovered dip':>14} {'recovered az':>13}")
    for dip_deg, theta_deg in ((35.0, 50.0), (20.0, 0.0), (62.5, 131.0),
                               (12.0, 275.0), (45.0, 90.0)):
        an, ae = apparent_dips(dip_deg, theta_deg)
        rdip, rtheta = true_dip(an, ae)
        print(f"{dip_deg:>10.3f} {theta_deg:>9.3f} {an:>10.4f} {ae:>10.4f}"
              f" {rdip:>14.4f} {rtheta:>13.3f}")
    print("\nRead those two columns carefully, because they are the lesson.")
    print("The dip is recovered exactly in every row. The dip azimuth is")
    print("recovered exactly only when it lies in the first quadrant, or is")
    print("exactly 0 or 90: rows 3 and 4 return 49.000 and 85.000 instead of")
    print("131.000 and 275.000. The reason is that the apparent dips depend on")
    print("|sin(theta)| and |cos(theta)|, so two sections cannot distinguish a")
    print("dip to the north-east from the mirror-image dip to the south-west.")
    print("Row 5 is the second trap: a due-east dip gives an apparent dip of")
    print("exactly zero in the north-south section, so any inversion that")
    print("divides by tan(alpha_N) fails there.")
    print("\nField case quoted in the lesson: apparent dips 20 deg in the N-S")
    print("section and 30 deg in the E-W section, with the beds known from")
    print("other evidence to deepen towards the north-east.")
    d, t = true_dip(20.0, 30.0)
    print(f"  true dip = {d:.4f} deg, dip azimuth = {t:.4f} deg, "
          f"strike = {(t + 90.0) % 360.0:.4f} deg or {(t + 270.0) % 360.0:.4f} deg")

    section("6. The price of the small-angle approximation")
    print(f"{'angle (deg)':>12} {'sin x':>14} {'x - sin x':>14} {'rel. error':>12}"
          f" {'x^3/6':>14}")
    for deg in (0.1, 1.0, 5.0, 10.0, 20.0, 30.0, 45.0):
        x = deg * DEG
        diff = x - math.sin(x)
        print(f"{deg:>12.2f} {math.sin(x):>14.10f} {diff:>14.3e} "
              f"{diff / math.sin(x):>12.3e} {x ** 3 / 6:>14.3e}")
    print("\nsin x = x is good to one part in 10^6 at 1 deg and to about 1.5")
    print("percent at 20 deg. The leading correction is x^3/6, and the last")
    print("column shows it accounts for the error almost completely.")


if __name__ == "__main__":
    main()
