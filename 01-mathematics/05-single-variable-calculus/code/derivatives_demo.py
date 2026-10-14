"""Derivatives as rates of change, computed the way a geophysicist computes them.

Run:  python3 derivatives_demo.py
Requires: Python standard library only.

Companion to lesson 01-05-02. Every section takes a derivative that has a name
in geophysics - velocity gradient, free-air gradient, geothermal gradient,
strain rate - and computes it twice: once analytically and once by a finite
difference, so that the *difference between the two* is the lesson.
"""

import math
import random

G = 6.674e-11        # m^3 kg^-1 s^-2
M_EARTH = 5.972e24   # kg  (ILLUSTRATIVE round value)
R_EARTH = 6.371e6    # m   (ILLUSTRATIVE round value)
MGAL = 1.0e-5        # m/s^2 per mGal
YGAL = 1.0e-8        # m/s^2 per µGal
YEAR = 3.156e7       # s per Julian year


def section(title: str) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def g_of_z(z: float) -> float:
    """Vertical gravitational acceleration from a point mass at the centre."""
    return G * M_EARTH / (R_EARTH + z) ** 2


def main() -> None:
    section("1. Velocity gradient in a 1-D model: v(z) = 1500 + 0.5 z")
    # SYNTHETIC linear velocity model; dv/dz = 0.5 s^-1 exactly.

    def v(z: float) -> float:
        return 1500.0 + 0.5 * z

    z0, exact = 3000.0, 0.5
    print(f"{'h (m)':>8}  {'forward':>20}  {'central':>20}"
          f"  {'|err| fwd':>10}  {'|err| ctr':>10}")
    for h in (1.0e2, 1.0e1, 1.0, 1.0e-1, 1.0e-2, 1.0e-3, 1.0e-4, 1.0e-5):
        fwd = (v(z0 + h) - v(z0)) / h
        ctr = (v(z0 + h) - v(z0 - h)) / (2.0 * h)
        print(f"{h:>8.0e}  {fwd:>20.15f}  {ctr:>20.15f}"
              f"  {abs(fwd - exact):>10.2e}  {abs(ctr - exact):>10.2e}")
    print("\nReading: a linear model is differentiated exactly by both formulas")
    print("up to round-off. The error floor near h = 1e-5 m is floating point,")
    print("not calculus.")

    section("2. The same, for a curved function: g(z) = GM/(R+z)^2")
    print("Analytic derivative at z = 0:  g'(0) = -2GM/R^3")
    analytic = -2.0 * G * M_EARTH / R_EARTH ** 3
    print(f"  g(0)      = {g_of_z(0.0):.10f} m/s^2")
    print(f"  g'(0)     = {analytic:.10e} m/s^2 per m"
          f"  = {analytic / MGAL:.6f} mGal/m")
    print(f"  -2 g(0)/R = {-2.0 * g_of_z(0.0) / R_EARTH:.10e} m/s^2 per m")
    print(f"\n{'h (m)':>8}  {'forward':>18}  {'central':>18}"
          f"  {'fwd err':>10}  {'ctr err':>10}")
    for h in (1.0e3, 1.0e2, 1.0e1, 1.0, 1.0e-1):
        fwd = (g_of_z(h) - g_of_z(0.0)) / h
        ctr = (g_of_z(h) - g_of_z(-h)) / (2.0 * h)
        print(f"{h:>8.0e}  {fwd:>18.12e}  {ctr:>18.12e}"
              f"  {abs(fwd - analytic):>10.2e}  {abs(ctr - analytic):>10.2e}")
    print("\nReading: for a smooth function the forward difference error falls")
    print("like h and the central difference like h^2. Halving h buys one digit")
    print("with the forward formula and two with the central one.")

    section("3. Second derivative: the curvature scale of the gravity field")
    second = 6.0 * G * M_EARTH / R_EARTH ** 4
    print(f"  g''(0)  = 6GM/R^4 = {second:.6e} m/s^2 per m^2")
    print(f"  g(0)/g''(0)       = {g_of_z(0.0) / second:.6e} m^2")
    print(f"  sqrt(g/g'') = R/sqrt(6) = {math.sqrt(g_of_z(0.0) / second):.6e} m")
    print(f"  R/sqrt(6)         = {R_EARTH / math.sqrt(6.0):.6e} m")
    print("\nReading: no measurement can resolve a change of g'' over metres;")
    print("the length over which the field's curvature matters is thousands of")
    print("kilometres. Second derivatives set spatial scales, not small ones.")

    section("4. Geothermal gradient and heat flux: q = k dT/dz")
    gradient = 25.0 * 1.0e-3       # 25 K/km -> K/m (ILLUSTRATIVE value)
    print(f"  dT/dz = {gradient:.3e} K/m  (25 K/km, ILLUSTRATIVE)")
    for k in (2.5, 3.0):
        q = k * gradient
        print(f"  k = {k:>4.1f} W m^-1 K^-1 -> q = {q:.4e} W/m^2"
              f" = {q * 1.0e3:.2f} mW/m^2")
    print("  Earth's global mean surface heat flux is often quoted near")
    print("  90 mW/m^2; continental shield values are lower, young ocean floor")
    print("  higher. The gradient above is illustrative, not a measurement.")

    section("5. Strain rate from relative plate motion")
    velocity, width = 0.050, 100.0e3     # m/yr across a 100 km wide zone
    rate_year = velocity / width
    rate_second = rate_year / YEAR
    print(f"  50 mm/yr across 100 km: {rate_year:.3e} per year")
    print(f"                        = {rate_second:.3e} per second")
    print(f"  time to accumulate unit strain: {1.0 / rate_year:.3e} yr"
          f" = {1.0 / rate_year / 1.0e6:.3f} Myr")
    print("\nReading: strain rate is a derivative with respect to time and has")
    print("units of inverse time. Its reciprocal is the time to reach unit")
    print("strain - here about 2 Myr, which is why plate-boundary shear zones")
    print("are recognisable in rocks only millions of years old.")

    section("6. A discontinuous derivative: a kink in the velocity model")
    # v is continuous at the Moho but its gradient jumps from 0 to 0.05 s^-1.

    def v_kink(z: float, z_moho: float = 33.0) -> float:
        return 6.0 + 0.05 * max(0.0, z - z_moho)

    z_moho = 33.0
    for h in (1.0e-1, 1.0e-2, 1.0e-3):
        left = (v_kink(z_moho) - v_kink(z_moho - h)) / h
        right = (v_kink(z_moho + h) - v_kink(z_moho)) / h
        print(f"  h={h:8.0e}: left derivative = {left:.6f}"
              f"   right derivative = {right:.6f}")
    print("\nReading: the one-sided derivatives differ by the 0.05 s^-1 jump")
    print("and neither depends on h, so the derivative genuinely does not")
    print("exist at the Moho. A velocity discontinuity in a model is a")
    print("mathematical statement that rays will turn or refract there.")

    section("7. Differentiation amplifies noise (SYNTHETIC, seeded)")
    random.seed(20261014)
    sigma = 10.0                        # m/s of picking noise
    gradient_true = 0.5
    print(f"  true dv/dz = {gradient_true} s^-1, noise sigma = {sigma} m/s")
    print(f"{'h (m)':>8}  {'mean |error| over 200 samples':>30}")
    for h in (1000.0, 200.0, 50.0, 20.0, 5.0):
        errors = []
        for _ in range(200):
            z0 = 2000.0
            noisy = lambda z: 1500.0 + gradient_true * z + random.gauss(0.0, sigma)
            errors.append(abs((noisy(z0 + h) - noisy(z0 - h)) / (2.0 * h)
                              - gradient_true))
        mean_error = sum(errors) / len(errors)
        print(f"{h:>8.0f}  {mean_error:>30.4f}")
    print("\nReading: halving the interval doubles the noise in the answer.")
    print("With sigma = 10 m/s the 5 m interval is useless. The optimal step")
    print("trades truncation error (falls with h) against round-off and noise")
    print("(rises as 1/h); the best h is large compared with your data's")
    print("precision, not small.")


if __name__ == "__main__":
    main()
