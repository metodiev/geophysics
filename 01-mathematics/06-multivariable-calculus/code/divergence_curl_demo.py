"""Divergence and curl: what they measure, computed on real fields.

Run:  python3 divergence_curl_demo.py
Requires: Python standard library only.

Companion to lesson 01-06-04. Three fields, three jobs:

  * a point-mass gravity field:  div g = 0 and curl g = 0 away from the source,
  * a rotating medium:           curl v = 2*Omega (vorticity of solid rotation),
  * a magnetic dipole:           div B = 0 and B = -grad V in source-free space.

All sources, masses and currents are SYNTHETIC.
"""

import math

G = 6.674e-11
MU0 = 4.0e-7 * math.pi      # H/m, conventional rounded value
EARTH_RATE = 7.2921e-5      # rad/s, Earth's mean rotation rate (standard value)


def section(title: str) -> None:
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def norm(v):
    return math.sqrt(sum(c * c for c in v))


def div_central(F, p, h):
    """Central-difference divergence of the vector field F at p."""
    x, y, z = p
    dx = (F(x + h, y, z)[0] - F(x - h, y, z)[0]) / (2.0 * h)
    dy = (F(x, y + h, z)[1] - F(x, y - h, z)[1]) / (2.0 * h)
    dz = (F(x, y, z + h)[2] - F(x, y, z - h)[2]) / (2.0 * h)
    return dx + dy + dz


def curl_central(F, p, h):
    """Central-difference curl of the vector field F at p."""
    x, y, z = p
    dxp, dxm = F(x + h, y, z), F(x - h, y, z)
    dyp, dym = F(x, y + h, z), F(x, y - h, z)
    dzp, dzm = F(x, y, z + h), F(x, y, z - h)
    # (curl F)_x = dFz/dy - dFy/dz, and cyclically.
    cx = (dzp[1] - dzm[1]) / (2.0 * h) - (dyp[2] - dym[2]) / (2.0 * h)
    cy = (dxp[2] - dxm[2]) / (2.0 * h) - (dzp[0] - dzm[0]) / (2.0 * h)
    cz = (dyp[0] - dym[0]) / (2.0 * h) - (dxp[1] - dxm[1]) / (2.0 * h)
    # dzp[1] is F_y at z+h, so it supplies dFy/dz; dxp[2] is F_z at x+h, dFz/dx.
    return ((dyp[2] - dym[2]) / (2.0 * h) - (dzp[1] - dzm[1]) / (2.0 * h),
            (dzp[0] - dzm[0]) / (2.0 * h) - (dxp[2] - dxm[2]) / (2.0 * h),
            (dxp[1] - dxm[1]) / (2.0 * h) - (dyp[0] - dym[0]) / (2.0 * h))


def main() -> None:
    section("1. Gravity of a point mass: divergence-free and curl-free outside it")
    mass = 1.0e12

    def g(x, y, z):
        r2 = x * x + y * y + z * z
        r = math.sqrt(r2)
        k = -G * mass / (r2 * r)
        return (k * x, k * y, k * z)

    p = (700.0, 400.0, -900.0)
    r = norm(p)
    for h in (1.0, 0.1):
        d = div_central(g, p, h)
        c = curl_central(g, p, h)
        print(f"h = {h:>4} m:  div g = {d: .6e} 1/s^2   "
              f"|curl g| = {norm(c):.6e} 1/s^2")
    print(f"scale for comparison: |g|/r = {norm(g(*p)) / r:.6e} 1/s^2")
    print("Both are zero to within truncation error: outside a point source the")
    print("field is solenoidal (no sources) and irrotational (a gradient field).")

    section("2. The flux of g through a sphere: Gauss's law in integral form")
    R = 1000.0
    for n in (100, 400):
        dtheta = math.pi / n
        dphi = 2.0 * math.pi / (2 * n)
        total = 0.0
        for i in range(n):
            theta = (i + 0.5) * dtheta
            for j in range(2 * n):
                phi = (j + 0.5) * dphi
                x = R * math.sin(theta) * math.cos(phi)
                y = R * math.sin(theta) * math.sin(phi)
                z = R * math.cos(theta)
                gr = -G * mass / R ** 2                 # g . r_hat
                total += gr * R ** 2 * math.sin(theta) * dtheta * dphi
        print(f"n_theta = {n:>3}: surface integral = {total:.6f} m^3/s^2"
              f"   relative error = {abs(total + 4 * math.pi * G * mass) / (4 * math.pi * G * mass):.3e}")
    print(f"exact -4*pi*G*M = {-4.0 * math.pi * G * mass:.6f} m^3/s^2")

    section("3. Solid-body rotation: divergence zero, curl 2*Omega")
    Omega = (0.0, 0.0, EARTH_RATE)

    def v_rot(x, y, z):
        # v = Omega x r with Omega along z
        return (-Omega[2] * y, Omega[2] * x, 0.0)

    p = (2.0e6, 1.0e6, 5.0e5)
    d = div_central(v_rot, p, 1000.0)
    c = curl_central(v_rot, p, 1000.0)
    print(f"at {p} m:  div v = {d: .6e} 1/s")
    print(f"curl v = ({c[0]: .6e}, {c[1]: .6e}, {c[2]: .6e}) 1/s")
    print(f"2*Omega = {2.0 * EARTH_RATE:.6e} 1/s")
    print("A rigid rotation moves material without compressing it, yet it has")
    print("vorticity: every parcel spins at the rotation rate, so curl v = 2*Omega.")

    section("4. Ampere's law: circulation of B around a current-carrying wire")
    current = 5.0e3        # A, SYNTHETIC
    rho = 50.0             # m, distance from the wire

    def B_wire(x, y, z):
        rr = math.hypot(x, y)
        b = MU0 * current / (2.0 * math.pi * rr)
        return (-b * y / rr, b * x / rr, 0.0)

    n = 20000
    loop = 0.0
    dphi = 2.0 * math.pi / n
    for k in range(n):
        phi = (k + 0.5) * dphi
        x = rho * math.cos(phi)
        y = rho * math.sin(phi)
        bx, by, _ = B_wire(x, y, 0.0)
        # dl = (-rho sin phi, rho cos phi, 0) dphi
        loop += (bx * (-rho * math.sin(phi)) + by * (rho * math.cos(phi))) * dphi
    print(f"loop integral of B . dl around a circle of radius {rho:.0f} m = {loop:.9e} T m")
    print(f"mu0 * I                                                  = {MU0 * current:.9e} T m")
    print(f"relative error                                           = "
          f"{abs(loop - MU0 * current) / (MU0 * current):.3e}")
    p = (30.0, 40.0, 12.0)
    c = curl_central(B_wire, p, 1e-3)
    print(f"curl B away from the wire at {p}: ({c[0]: .3e}, {c[1]: .3e}, {c[2]: .3e}) 1/s")
    print("Off the wire curl B vanishes, so B is a gradient there. On the wire the")
    print("field is singular and the circulation is the enclosed current times mu0.")

    section("5. A magnetic dipole: div B = 0 everywhere, B = -grad V outside")
    moment = 8.0e22        # A m^2, the order of magnitude of Earth's dipole moment
    m = (0.0, 0.0, moment)

    def B_dipole(x, y, z):
        r2 = x * x + y * y + z * z
        r = math.sqrt(r2)
        mdotr = m[0] * x + m[1] * y + m[2] * z
        k = MU0 / (4.0 * math.pi * r ** 5)
        return (k * (3.0 * mdotr * x - m[0] * r2),
                k * (3.0 * mdotr * y - m[1] * r2),
                k * (3.0 * mdotr * z - m[2] * r2))

    p = (5.0e6, 3.0e6, 4.0e6)
    d = div_central(B_dipole, p, 1.0e3)
    c = curl_central(B_dipole, p, 1.0e3)
    print(f"at |r| = {norm(p) / 1e6:.3f} Mm:  div B = {d: .6e} T/m")
    print(f"                       |curl B| = {norm(c):.6e} T/m")
    print(f"scale |B|/r = {norm(B_dipole(*p)) / norm(p):.6e} T/m")

    def V_dipole(x, y, z):
        r2 = x * x + y * y + z * z
        r = math.sqrt(r2)
        return MU0 / (4.0 * math.pi) * (m[2] * z) / (r2 * r)

    h = 1.0e2
    num = tuple(-(V_dipole(p[0] + (h if i == 0 else 0), p[1] + (h if i == 1 else 0),
                            p[2] + (h if i == 2 else 0))
                  - V_dipole(p[0] - (h if i == 0 else 0), p[1] - (h if i == 1 else 0),
                             p[2] - (h if i == 2 else 0))) / (2.0 * h)
               for i in range(3))
    ana = B_dipole(*p)
    print(f"-grad V = ({num[0]: .6e}, {num[1]: .6e}, {num[2]: .6e}) T")
    print(f"B       = ({ana[0]: .6e}, {ana[1]: .6e}, {ana[2]: .6e}) T")
    print(f"relative difference = "
          f"{norm([num[i] - ana[i] for i in range(3)]) / norm(ana):.3e}")
    print("Outside the magnetised body B is both divergence-free and curl-free, so")
    print("it is exactly minus the gradient of a scalar potential. That is the")
    print("starting point of all magnetic interpretation.")


if __name__ == "__main__":
    main()
