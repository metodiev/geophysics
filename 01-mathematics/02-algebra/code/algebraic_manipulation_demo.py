"""Algebraic manipulation: rearranging, solving and checking.

Run:  python3 algebraic_manipulation_demo.py
Requires: Python standard library only.

Companion to lesson 01-02-01. Every rearrangement below is checked
numerically, because the only honest way to test algebra is to substitute the
solution back and compare with the original equation.
"""

import math


def section(title: str) -> None:
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def main() -> None:
    section("1. Solving for a target variable: depth from a two-way travel time")
    # t = 2d/v  ->  d = v t / 2
    v = 4800.0        # m/s, an illustrative crustal speed
    t = 1.25          # s, two-way time
    d = v * t / 2.0
    print(f"given v = {v:.0f} m/s and two-way time t = {t} s")
    print(f"d = v t / 2 = {v:.0f} * {t} / 2 = {d:.3f} m")
    print(f"check by substitution: 2d/v = {2.0 * d / v:.12f} s = t")

    section("2. Rearranging a product: solve g = G M / d**2 for each symbol")
    big_g, mass, depth = 6.674e-11, 1.0e12, 1500.0
    g = big_g * mass / depth ** 2
    recovered_depth = math.sqrt(big_g * mass / g)
    recovered_mass = g * depth ** 2 / big_g
    print(f"g = {g:.6e} m/s**2 from M = {mass:.0e} kg at d = {depth:.0f} m")
    print(f"d = sqrt(G M / g) = {recovered_depth:.6f} m  (true {depth:.0f})")
    print(f"M = g d**2 / G     = {recovered_mass:.6e} kg (true {mass:.0e})")
    print("Each rearrangement isolates one symbol; the check is that both")
    print("recoveries return the input value to round-off.")

    section("3. The step that creates extraneous roots: squaring")
    # sqrt(x + 5) = x - 1. Squaring gives x + 5 = x**2 - 2x + 1, a quadratic
    # with roots 4 and -1. Substitution shows that only 4 works.
    print("solve sqrt(x + 5) = x - 1")
    for candidate in (4.0, -1.0):
        left = math.sqrt(candidate + 5.0)
        right = candidate - 1.0
        print(f"  x = {candidate:>5.1f}: left side = {left:.6f}, "
              f"right side = {right:.6f}, equal? {abs(left - right) < 1e-12}")
    print("Squaring is not an equivalence transformation: it can manufacture")
    print("solutions. Always substitute the candidates back into the original")
    print("equation, never into the squared version.")

    section("4. Verifying an identity by sampling instead of by algebra")
    pairs = [(2.0, 3.0), (-4.0, 0.5), (1e6, 1e-6), (7.5, -2.25)]
    print(f"{'a':>10} {'b':>9} {'(a+b)**2':>16} {'a**2+2ab+b**2':>16} "
          f"{'a**2+b**2':>14}")
    for a, b in pairs:
        correct = (a + b) ** 2
        expanded = a * a + 2.0 * a * b + b * b
        wrong = a * a + b * b
        print(f"{a:>10} {b:>9} {correct:>16.4f} {expanded:>16.4f} {wrong:>14.4f}")
    print("The identity holds for every pair; the 'freshman's dream' "
          "a**2 + b**2 does")
    print("not. Sampling many pairs does not prove an identity, but one")
    print("counterexample disproves it, and it is a cheap check on your own work.")

    section("5. A variable hidden inside an exponential")
    # Arrhenius-type relation D = D0 exp(-Ea/(R T)); solve for T.
    # ILLUSTRATIVE constants, not literature values for any real mineral.
    d0, ea = 1.0e-6, 2.0e5         # m**2/s, J/mol (ILLUSTRATIVE)
    r_gas = 8.31446261815324       # J/(mol K), defined exact value
    target = 1.0e-18               # m**2/s
    temperature = ea / (r_gas * math.log(d0 / target))
    print(f"D = D0 exp(-Ea / (R T)), ILLUSTRATIVE D0 = {d0:.1e} m**2/s,")
    print(f"Ea = {ea:.0e} J/mol, R = {r_gas:.4f} J/(mol K)")
    print(f"for D = {target:.0e} m**2/s:  T = Ea / (R ln(D0/D)) = "
          f"{temperature:.3f} K")
    print(f"check: D(T) = {d0 * math.exp(-ea / (r_gas * temperature)):.6e} m**2/s")
    print("The inversion needed three steps: divide by D0, take logarithms, then")
    print("divide by Ea/R. Lesson 01-02-03 develops this pattern systematically.")

    section("6. Solving a 2x2 system by substitution")
    # Two linear equations, solved by isolating y in the first.
    # (1) x + y = 9.5      (2) 2x - y = 7.0
    total, difference = 9.5, 7.0
    # From (1): y = total - x. Substitute into (2).
    x = (difference + total) / 3.0
    y = total - x
    print(f"x + y = {total}, 2x - y = {difference}")
    print(f"substitute y = {total} - x: 2x - ({total} - x) = {difference}")
    print(f"-> 3x = {difference + total} -> x = {x:.10f}, y = {y:.10f}")
    print(f"check (1): x + y = {x + y:.10f}")
    print(f"check (2): 2x - y = {2 * x - y:.10f}")
    print("Substitution is the reliable hand method for small systems; lesson")
    print("01-02-05 replaces it with elimination for larger ones.")

    section("7. Division by a quantity that might be zero")
    # Solving v = d/t for t is only allowed when v != 0; solving for d = v t is
    # always allowed. The demo shows what happens when v = 0.
    for velocity in (3000.0, 1e-12, 0.0):
        if velocity == 0.0:
            print(f"  v = {velocity}: t = d/v is undefined; the equation "
                  "v = d/t cannot be solved for t")
        else:
            print(f"  v = {velocity:>8.1e} m/s: t = d/v = "
                  f"{1200.0 / velocity:.6e} s for d = 1200 m")
    print("Before dividing by an expression, ask whether it can vanish. In")
    print("geophysics it usually can: zero velocity, zero density contrast,")
    print("zero gradient are all physical.")


if __name__ == "__main__":
    main()
