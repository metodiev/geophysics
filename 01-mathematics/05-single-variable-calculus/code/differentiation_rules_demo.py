"""Differentiation rules, checked numerically, on geophysical functions.

Run:  python3 differentiation_rules_demo.py
Requires: Python standard library only.

Companion to lesson 01-05-03. The strategy of the whole file is: write down the
analytic derivative from the rules, then *measure* the derivative with a central
difference and print the disagreement. If the rules are right the disagreement
is at the level of the finite-difference error, and that is a real check rather
than a ritual.
"""

import math

CENTRAL_H = 1.0e-5


def section(title: str) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def numeric_derivative(f, x: float, h: float = CENTRAL_H) -> float:
    return (f(x + h) - f(x - h)) / (2.0 * h)


def check(name: str, analytic: float, numeric: float) -> None:
    denom = abs(analytic) if analytic != 0.0 else 1.0
    print(f"  {name:<28} analytic = {analytic:>18.10e}"
          f"   numeric = {numeric:>18.10e}   rel. diff = {abs(analytic - numeric) / denom:.2e}")


def main() -> None:
    section("1. Product rule on acoustic impedance Z(z) = rho(z) v(z)")
    # SYNTHETIC linear profiles: rho = 2600 + 0.10 z, v = 1500 + 0.5 z.
    def rho(z: float) -> float:
        return 2600.0 + 0.10 * z

    def vel(z: float) -> float:
        return 1500.0 + 0.5 * z

    impedance = lambda z: rho(z) * vel(z)
    z0 = 1000.0
    analytic = 0.10 * vel(z0) + rho(z0) * 0.5          # rho' v + rho v'
    check("d(rho v)/dz", analytic, numeric_derivative(impedance, z0))
    print(f"  at z = {z0:.0f} m: Z = {impedance(z0):.4e} kg m^-2 s^-1")
    print("  Reading: impedance sets reflection coefficients; its gradient is")
    print("  what converts a geological transition into a seismic reflection.")

    section("2. Quotient rule: travel time t(x) = x/v")
    v_rock = 2500.0
    check("d(x/v)/dx", 1.0 / v_rock,
          numeric_derivative(lambda x: x / v_rock, 4000.0))
    print(f"  1/v = {1.0 / v_rock:.6e} s/m: slowness is the derivative of")
    print("  travel time with respect to distance. Tomography inverts")
    print("  slowness, not velocity, precisely because travel time is linear")
    print("  in it.")

    section("3. Chain rule through a two-step physical model")
    G, M, R = 6.674e-11, 5.972e24, 6.371e6
    g = lambda z: G * M / (R + z) ** 2
    dg_dz_analytic = -2.0 * G * M / R ** 3
    dg_dz_numeric = numeric_derivative(g, 0.0, 10.0)
    check("dg/dz at z=0", dg_dz_analytic, dg_dz_numeric)
    uplift = 5.0e-3                                   # m per year
    rate = dg_dz_analytic * uplift                    # chain rule: dg/dt
    print(f"  uplift dz/dt = {uplift * 1.0e3:.1f} mm/yr")
    print(f"  dg/dt = (dg/dz)(dz/dt) = {rate:.6e} m s^-2 per yr")
    print(f"        = {rate / 1.0e-8:.4f} µGal/yr")
    print("  Reading: the free-air gradient converts uplift into a gravity")
    print("  rate, and the answer is a few µGal per year. This is why")
    print("  repeated microgravity surveys need µGal repeatability to see")
    print("  secular vertical motion.")

    section("4. Logarithmic differentiation: d(ln A)/dt = -lambda")
    half_life = 5730.0                                # conventional 14C half-life, yr
    lam = math.log(2.0) / half_life
    activity = lambda t: math.exp(-lam * t)
    check("d(ln A)/dt", -lam,
          numeric_derivative(lambda t: math.log(activity(t)), 1000.0, 1.0))
    print(f"  lambda = ln2 / t_half = {lam:.6e} per year, t_half = {half_life:.0f} yr")
    print(f"  activity after 10 half-lives = {activity(10 * half_life):.6e}"
          f" (expected 1/1024 = {1.0 / 1024.0:.6e})")
    print("  Reading: logarithmic differentiation turns a multiplicative")
    print("  decay law into a constant rate, which is why decay constants are")
    print("  quoted rather than 'fractions remaining'.")

    section("5. Power law and elasticity: rho = a v^b")
    a, b, v0 = 2.1, 0.25, 3000.0        # SYNTHETIC illustrative coefficients
    power = lambda v: a * v ** b
    analytic = a * b * v0 ** (b - 1.0)
    check("d(a v^b)/dv", analytic, numeric_derivative(power, v0, 1.0))
    print(f"  fractional form: (d rho / rho) / (dv / v) = b = {b}")
    print(f"  a 1 % increase in v raises rho by {b:.2f} %")
    print("\n  Reading: empirical rock-physics relations of the form rho = a v^b")
    print("  (Gardner-type) are power laws, so their logarithmic derivative is")
    print("  a constant. Note that a and b depend on the unit system used to")
    print("  fit them; never transplant coefficients between unit systems.")

    section("6. Implicit differentiation: the slope of an elliptical interface")
    # (x/a)^2 + (z/b)^2 = 1  ->  dz/dx = -(b^2 x)/(a^2 z)
    a_axis, b_axis = 2000.0, 1000.0

    def z_on_ellipse(x: float) -> float:
        return b_axis * math.sqrt(max(0.0, 1.0 - (x / a_axis) ** 2))

    print(f"{'x (m)':>8}  {'analytic dz/dx':>18}  {'numeric dz/dx':>18}")
    for x in (200.0, 600.0, 1000.0, 1400.0, 1800.0):
        z = z_on_ellipse(x)
        analytic = -(b_axis ** 2 * x) / (a_axis ** 2 * z)
        numeric = numeric_derivative(z_on_ellipse, x, 1.0e-3)
        print(f"{x:>8.0f}  {analytic:>18.10f}  {numeric:>18.10f}")
    print("\n  Reading: z is defined implicitly, and near the ends the slope")
    print("  becomes vertical - the derivative diverges. Compare with lesson")
    print("  01-05-06 on singular behaviour.")

    section("7. The chain rule behind Snell's law: dt/dx = sin(theta)/v = p")
    # Single horizontal layer: t(x) = sqrt(t0^2 + x^2/v^2), sin(theta) = x/(v t).
    v_layer, t0 = 2000.0, 1.0
    t = lambda x: math.sqrt(t0 ** 2 + x ** 2 / v_layer ** 2)
    print(f"{'x (m)':>8}  {'t (s)':>14}  {'dt/dx (s/m)':>16}"
          f"  {'sin(theta)/v':>16}  {'difference':>12}")
    for x in (0.0, 500.0, 1000.0, 2000.0, 3000.0):
        tt = t(x)
        ray_param = x / (v_layer ** 2 * tt)
        sin_over_v = (x / (v_layer * tt)) / v_layer
        print(f"{x:>8.0f}  {tt:>14.9f}  {ray_param:>16.10e}"
              f"  {sin_over_v:>16.10e}  {abs(ray_param - sin_over_v):>12.2e}")
    print("\n  Reading: the derivative of the travel-time curve with respect to")
    print("  offset *is* the ray parameter p = sin(theta)/v. No trigonometry")
    print("  was assumed to derive it; the identity between the two columns is")
    print("  the statement that Fermat's principle and Snell's law agree.")


if __name__ == "__main__":
    main()
