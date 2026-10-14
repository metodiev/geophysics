"""Multiple integrals: iterated integration, regions and total mass.

Run:  python3 multiple_integrals_demo.py
Requires: Python standard library only.

Companion to lesson 01-06-02. The point of every example is the same: an
integral over a body in the Earth is the sum of a property over that body, and
you compute it by reducing it to iterated one-dimensional integrals.

Everything here is SYNTHETIC.
"""

import math
import random


def section(title: str) -> None:
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def midpoint_1d(f, a, b, n):
    """Composite midpoint rule for the integral of f over [a, b]."""
    h = (b - a) / n
    total = 0.0
    for k in range(n):
        total += f(a + (k + 0.5) * h)
    return total * h


def midpoint_2d(f, xa, xb, ya, yb, n):
    """Composite midpoint rule for the integral over a rectangle."""
    hx = (xb - xa) / n
    hy = (yb - ya) / n
    total = 0.0
    for i in range(n):
        x = xa + (i + 0.5) * hx
        for j in range(n):
            y = ya + (j + 0.5) * hy
            total += f(x, y)
    return total * hx * hy


def main() -> None:
    section("1. A double integral over a rectangle, two ways, and exactly")
    # I = integral over [0,2]x[0,1] of (x^2 + y^2)
    #   = integral_0^2 (x^2 + 1/3) dx = 8/3 + 2/3 = 10/3
    f = lambda x, y: x * x + y * y                                     # noqa: E731
    exact = 10.0 / 3.0
    print(f"exact value                          = {exact:.10f}")
    print("order dx dy (x outer):")
    for n in (10, 50, 200):
        val = midpoint_2d(f, 0.0, 2.0, 0.0, 1.0, n)
        print(f"   n = {n:>3}: value = {val:.10f}   error = {abs(val - exact):.3e}")
    print("order dy dx (y outer):")
    for n in (10, 50, 200):
        val = midpoint_2d(lambda y, x: f(x, y), 0.0, 1.0, 0.0, 2.0, n)
        print(f"   n = {n:>3}: value = {val:.10f}   error = {abs(val - exact):.3e}")
    print("Both orders converge to the same number: Fubini's theorem in practice.")

    section("2. A region that is not a rectangle")
    # Area between y = x and y = x^2 on [0,1]: integral_0^1 (x - x^2) dx = 1/6
    print(f"exact area                          = {1.0 / 6.0:.10f}")
    for n in (20, 100, 500):
        val = midpoint_1d(lambda x: x - x * x, 0.0, 1.0, n)
        print(f"   n = {n:>3}: area = {val:.10f}   error = {abs(val - 1.0 / 6.0):.3e}")
    print("The inner integration was done by hand (the vertical extent of the")
    print("region at each x), leaving a single numerical integral.")

    section("3. Area of a disk: the integration limits encode the geometry")
    radius = 4.0
    print(f"exact area = pi*R^2                  = {math.pi * radius ** 2:.8f}")
    for n in (50, 200, 800):
        val = midpoint_1d(lambda x: 2.0 * math.sqrt(radius ** 2 - x * x),
                          -radius, radius, n)
        print(f"   n = {n:>3}: area = {val:.8f}   error = {abs(val - math.pi * radius ** 2):.3e}")
    print("Near x = +-R the integrand has infinite slope, so the midpoint rule")
    print("loses accuracy there; that is a property of the integrand, not the method.")

    section("4. Volume of the unit ball, two independent computations")
    # (a) Cartesian Monte Carlo: fraction of the cube that lies inside the ball.
    random.seed(20240214)
    n_samples = 400000
    inside = 0
    for _ in range(n_samples):
        x = random.uniform(-1.0, 1.0)
        y = random.uniform(-1.0, 1.0)
        z = random.uniform(-1.0, 1.0)
        if x * x + y * y + z * z <= 1.0:
            inside += 1
    mc_volume = 8.0 * inside / n_samples
    # (b) Spherical element: integral_0^1 4*pi*r^2 dr = 4*pi/3
    sphere_volume = midpoint_1d(lambda r: 4.0 * math.pi * r * r, 0.0, 1.0, 2000)
    print(f"Monte Carlo (4e5 samples)           = {mc_volume:.6f}")
    print(f"spherical element, 4*pi*r^2 dr      = {sphere_volume:.12f}")
    print(f"exact 4*pi/3                        = {4.0 * math.pi / 3.0:.12f}")
    print(f"Monte Carlo relative error          = "
          f"{abs(mc_volume - 4.0 * math.pi / 3.0) / (4.0 * math.pi / 3.0):.3e}")
    print("The Monte Carlo error is statistical (~1/sqrt(N) here); the quadrature")
    print("error is truncation error, and it is far smaller for the same effort.")

    section("5. Mass of a sphere with a linear density profile")
    # rho(r) = rho0 * (1 - r/R) -> M = 4*pi*rho0*(R^3/3 - R^4/(4R)) = pi*rho0*R^3/3
    rho0 = 3500.0
    R = 3.0e5                      # 300 km: a small planetary body, SYNTHETIC
    exact_mass = math.pi * rho0 * R ** 3 / 3.0
    print(f"rho0 = {rho0:.0f} kg/m^3,  R = {R:.3e} m")
    for n in (200, 2000, 20000):
        val = midpoint_1d(lambda r: 4.0 * math.pi * rho0 * (1.0 - r / R) * r * r,
                          0.0, R, n)
        print(f"   n = {n:>5}: M = {val:.6e} kg   error = {abs(val - exact_mass):.3e} kg")
    print(f"exact pi*rho0*R^3/3                 = {exact_mass:.6e} kg")
    volume = 4.0 * math.pi * R ** 3 / 3.0
    print(f"model volume 4*pi*R^3/3             = {volume:.6e} m^3")
    print(f"mean density M/V                    = {exact_mass / volume:.6f} kg/m^3"
          f"   (exactly rho0/4 = {rho0 / 4.0:.1f})")
    print("Mean density is a volume average: the dense centre is weighted by r^2,")
    print("so a body whose centre is 3500 kg/m^3 can average far less.")


if __name__ == "__main__":
    main()
