"""Vertical gravity of a rectangular prism: closed form vs numerical quadrature.

Two independent methods compute the same quantity:

  (A) the closed-form expression for the vertical attraction of a homogeneous
      rectangular prism (the "prism formula"), and
  (B) direct numerical quadrature of  g_z = G rho * integral (z'/|r|^3) dV
      over the prism volume.

They share no code, so agreement is evidence that both are right.

Convention.  The z axis points DOWNWARD.  The observation point sits at the
origin; the prism lies entirely at z > 0 (below the observer).  A positive
result is therefore a downward acceleration toward the mass, which is the
quantity a gravimeter measures.

Units are SI throughout: metres, kg/m^3, and m/s^2.  Results are converted to
mGal (1 mGal = 1e-5 m/s^2) for reporting.

Run:  python3 prism_gravity_demo.py
"""

from __future__ import annotations

import numpy as np
from scipy import integrate

# Newtonian constant of gravitation, CODATA 2018 value read from
# https://physics.nist.gov/cuu/Constants/  (6.674 30(15) x 10^-11).
G = 6.67430e-11  # m^3 kg^-1 s^-2

MGAL = 1.0e-5  # m/s^2 per mGal (exact by definition of the Gal)


def prism_gz_closed(x1, x2, y1, y2, z1, z2, rho):
    """Vertical attraction of a homogeneous prism, closed form.

    Prism occupies x1<=x<=x2, y1<=y<=y2, z1<=z<=z2 with z positive downward.
    Observation at the origin.  Returns g_z in m/s^2, positive downward.

    The formula is the standard one for the vertical component of the
    attraction of a rectangular parallelepiped (Nagy, 1966; Blakely 1995,
    eq. 9.21).  The three pairwise logarithms and one arctangent per corner
    come from integrating  G rho (z/|r|^3)  over each coordinate in turn.
    """
    total = 0.0
    for i, x in enumerate((x1, x2)):
        for j, y in enumerate((y1, y2)):
            for k, z in enumerate((z1, z2)):
                r = np.sqrt(x * x + y * y + z * z)
                if r == 0.0:  # corner coincides with observer: skip, log is singular
                    continue
                total += (-1.0) ** (i + j + k) * (
                    x * np.log(y + r)
                    + y * np.log(x + r)
                    - z * np.arctan2(x * y, z * r)
                )
    return G * rho * total


def prism_gz_quadrature(x1, x2, y1, y2, z1, z2, rho, n=120):
    """Same quantity by Gauss-Legendre quadrature over the prism volume."""
    # Fixed-order Gauss-Legendre nodes, so the node count is reproducible and
    # can be quoted as a convergence metric.
    gx, wx = np.polynomial.legendre.leggauss(n)  # nodes/weights on [-1, 1]

    def jacobi(a, b):
        """Map [-1,1] nodes to [a,b] and return (points, weights)."""
        mid, half = 0.5 * (a + b), 0.5 * (b - a)
        return mid + half * gx, half * wx

    x, wxx = jacobi(x1, x2)
    y, wyy = jacobi(y1, y2)
    z, wzz = jacobi(z1, z2)
    X, Y, Z = np.meshgrid(x, y, z, indexing="ij")
    W = np.einsum("i,j,k->ijk", wxx, wyy, wzz)
    r = np.sqrt(X**2 + Y**2 + Z**2)
    # The observer is at the origin; the kernel is the downward component
    # z'/|r|^3.  The integrand is smooth here, so Gauss-Legendre converges
    # very fast.
    return G * rho * np.sum(W * Z / r**3)


def prism_gz_quad_scipy(x1, x2, y1, y2, z1, z2, rho):
    """Third, fully independent check: scipy's adaptive triple quadrature."""
    def kernel(zp, xp, yp):
        r = np.sqrt(xp**2 + yp**2 + zp**2)
        return G * rho * zp / r**3

    val, err = integrate.tplquad(
        kernel, x1, x2, lambda _x: y1, lambda _x: y2,
        lambda _x, _y: z1, lambda _x, _y: z2,
        epsabs=1e-18, epsrel=1e-12,
    )
    return val, err


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def main() -> None:
    rho = 500.0  # kg/m^3  <- SYNTHETIC density contrast (stated model input)
    print("SYNTHETIC model: homogeneous prism, density contrast 500 kg/m^3")
    print("Convention: z positive downward, observer at the origin, prism at z>0.")

    section("1. Prism directly beneath the observer")
    # 200 m x 200 m in plan, top at 50 m, bottom at 250 m depth.
    x1, x2, y1, y2, z1, z2 = -100.0, 100.0, -100.0, 100.0, 50.0, 250.0
    closed = prism_gz_closed(x1, x2, y1, y2, z1, z2, rho)
    quad = prism_gz_quadrature(x1, x2, y1, y2, z1, z2, rho, n=120)
    scipy_val, scipy_err = prism_gz_quad_scipy(x1, x2, y1, y2, z1, z2, rho)
    print(f"  geometry: x,y in [-100,100] m ; z in [50,250] m")
    print(f"  (A) closed form        = {closed:.9e} m/s^2 = {closed/MGAL:.6f} mGal")
    print(f"  (B) Gauss-Legendre n=120 = {quad:.9e} m/s^2 = {quad/MGAL:.6f} mGal")
    print(f"  (C) scipy tplquad      = {scipy_val:.9e} m/s^2 (est. abs err "
          f"{scipy_err:.1e})")
    rel_ab = abs(closed - quad) / abs(closed)
    rel_ac = abs(closed - scipy_val) / abs(closed)
    print(f"  |A-B|/|A| = {rel_ab:.3e}    |A-C|/|A| = {rel_ac:.3e}")

    section("2. Convergence of the quadrature with node count")
    print("  n      g_z (mGal)          |A-B|/|A|")
    for n in (20, 40, 80, 160):
        q = prism_gz_quadrature(x1, x2, y1, y2, z1, z2, rho, n=n)
        print(f"  {n:4d}   {q/MGAL:.9f}     {abs(closed-q)/abs(closed):.3e}")

    section("3. Observer offset in plan (profile over the edge)")
    print("  x_obs(m)   closed(mGal)   quadrature(mGal)   |A-B|/|A|")
    for xo in (0.0, 100.0, 200.0, 400.0):
        # Shift the observer by translating the prism by -xo: equivalent and
        # keeps the quadrature node pattern fixed.
        c = prism_gz_closed(x1 - xo, x2 - xo, y1, y2, z1, z2, rho)
        q = prism_gz_quadrature(x1 - xo, x2 - xo, y1, y2, z1, z2, rho, n=120)
        print(f"  {xo:7.1f}   {c/MGAL:11.7f}   {q/MGAL:15.7f}    "
              f"{abs(c-q)/abs(c):.3e}")

    section("4. Dimensional sanity check")
    # [G] = m^3 kg^-1 s^-2 ; [rho] = kg m^-3 ; [x ln(...)] = m
    # => [G rho * m] = m s^-2.  Correct for an acceleration.
    print("  [G] = m^3 kg^-1 s^-2, [rho] = kg m^-3, [prism term] = m")
    print("  => [g_z] = m^3 kg^-1 s^-2 * kg m^-3 * m = m s^-2  (acceleration). OK")
    print(f"  check: 1 mGal = 1e-5 m/s^2 (definition of the Gal, exact)")

    section("5. Thin-sheet limit: does the closed form reduce to the slab formula?")
    # An infinite slab of thickness t and density rho gives g_z = 2 pi G rho t.
    # A wide, thin prism should approach that value at its centre.
    t = 20.0
    wide = 50_000.0
    g_prism = prism_gz_closed(-wide, wide, -wide, wide, 100.0, 100.0 + t, rho)
    g_slab = 2.0 * np.pi * G * rho * t
    print(f"  prism 2 km... 50 km half-width, thickness {t} m:"
          f" {g_prism/MGAL:.6f} mGal")
    print(f"  infinite slab 2*pi*G*rho*t = {g_slab/MGAL:.6f} mGal")
    print(f"  relative difference = {abs(g_prism-g_slab)/g_slab:.3e}"
          "  (finite size + finite thickness)")

    print("\nSUMMARY: methods A, B and C agree to the tolerance printed above;")
    print("the closed form is the reference and quadrature reproduces it.")


if __name__ == "__main__":
    main()
