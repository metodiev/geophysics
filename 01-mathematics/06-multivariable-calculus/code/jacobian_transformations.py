"""Jacobians: volume elements, coordinate transformations and uncertainty.

Run:  python3 jacobian_transformations.py
Requires: Python standard library only.

Companion to lesson 01-06-03. Three jobs for one object:

  * the Jacobian determinant is the local volume scale factor,
  * its columns transform derivatives (the chain rule in matrix form),
  * it propagates uncertainties through a coordinate change.

All positions, masses and uncertainties here are SYNTHETIC or ILLUSTRATIVE.
"""

import math
import random

EARTH_RADIUS = 6.371e6     # m, conventional mean radius used for scale


def section(title: str) -> None:
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def transpose3(m):
    return [[m[j][i] for j in range(3)] for i in range(3)]


def matmul3(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)]
            for i in range(3)]


def jacobian_fd(map3, u, h):
    """Finite-difference Jacobian of a map R^n -> R^n at the point u."""
    n = len(u)
    cols = []
    for axis in range(n):
        up = list(u)
        down = list(u)
        up[axis] += h
        down[axis] -= h
        fp = map3(*up)
        fm = map3(*down)
        cols.append([(fp[i] - fm[i]) / (2.0 * h) for i in range(n)])
    return [[cols[j][i] for j in range(n)] for i in range(n)]


def det_n(m):
    """Determinant by Laplace expansion; small n only."""
    n = len(m)
    if n == 1:
        return m[0][0]
    if n == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    total = 0.0
    for j in range(n):
        minor = [[m[i][k] for k in range(n) if k != j] for i in range(1, n)]
        total += (-1) ** j * m[0][j] * det_n(minor)
    return total


def main() -> None:
    section("1. Jacobian determinants as local volume scale factors")
    maps = [
        ("polar        (r,theta)    -> (x,y)",
         lambda r, t: (r * math.cos(t), r * math.sin(t)),
         lambda r, t: r,
         (3.0, 0.7)),
        ("cylindrical  (rho,phi,z)  -> (x,y,z)",
         lambda p, ph, z: (p * math.cos(ph), p * math.sin(ph), z),
         lambda p, ph, z: p,
         (3.0, 0.7, 1.5)),
        ("spherical    (r,theta,phi)-> (x,y,z)",
         lambda r, t, ph: (r * math.sin(t) * math.cos(ph),
                           r * math.sin(t) * math.sin(ph),
                           r * math.cos(t)),
         lambda r, t, ph: r * r * math.sin(t),
         (3.0, 0.7, 1.5)),
    ]
    for name, map_n, analytic, u in maps:
        num = det_n(jacobian_fd(map_n, u, 1e-6))
        ana = analytic(*u)
        print(f"{name}")
        print(f"   at {u}:  numeric det J = {num:.9f}   analytic = {ana:.9f}"
              f"   rel. diff = {abs(num - ana) / abs(ana):.3e}")
    print("For the spherical map the determinant is exactly r^2 sin(theta), which")
    print("is why the volume element is dV = r^2 sin(theta) dr dtheta dphi.")

    section("2. Same ball, two ways: the determinant does the work")
    R = 1.0
    # (a) spherical element, one integral
    n = 4000
    h = R / n
    vol_sph = sum(4.0 * math.pi * ((k + 0.5) * h) ** 2 * h for k in range(n))
    # (b) Cartesian Monte Carlo: count the fraction of the cube inside the ball
    random.seed(112358)
    samples = 400000
    inside = 0
    for _ in range(samples):
        x = random.uniform(-R, R)
        y = random.uniform(-R, R)
        z = random.uniform(-R, R)
        if x * x + y * y + z * z <= R * R:
            inside += 1
    vol_mc = 8.0 * R ** 3 * inside / samples
    print(f"spherical element, r^2 sin(theta) dr dtheta dphi = {vol_sph:.10f}")
    print(f"Cartesian Monte Carlo, {samples} samples          = {vol_mc:.10f}")
    print(f"exact 4*pi/3                                     = {4.0 * math.pi / 3.0:.10f}")

    section("3. Mass of a spherical shell and of a layered body")
    rho = 2700.0
    a_inner, a_outer = 6.0e5, 1.2e6
    exact_shell = 4.0 * math.pi * rho * (a_outer ** 3 - a_inner ** 3) / 3.0
    n = 20000
    dr = (a_outer - a_inner) / n
    num_shell = sum(4.0 * math.pi * rho * (a_inner + (k + 0.5) * dr) ** 2 * dr
                    for k in range(n))
    print(f"shell {a_inner:.1e} m < r < {a_outer:.1e} m, rho = {rho:.0f} kg/m^3")
    print(f"numeric 4*pi*rho*r^2 dr                  = {num_shell:.6e} kg")
    print(f"exact 4*pi*rho*(b^3-a^3)/3               = {exact_shell:.6e} kg")
    print(f"relative difference                      = "
          f"{abs(num_shell - exact_shell) / exact_shell:.3e}")

    section("4. The chain rule in matrix form: the gradient in spherical coordinates")
    L = 1.0e6
    f = lambda x, y, z: (math.sin(x / L) * math.cos(y / L) * math.exp(z / L))  # noqa: E731
    r, theta, phi = 5.0e6, 0.9, 1.2
    p = (r * math.sin(theta) * math.cos(phi),
         r * math.sin(theta) * math.sin(phi),
         r * math.cos(theta))
    hr = 1.0
    grad_cart = [(f(p[0] + hr, p[1], p[2]) - f(p[0] - hr, p[1], p[2])) / (2 * hr),
                 (f(p[0], p[1] + hr, p[2]) - f(p[0], p[1] - hr, p[2])) / (2 * hr),
                 (f(p[0], p[1], p[2] + hr) - f(p[0], p[1], p[2] - hr)) / (2 * hr)]
    rhat = (math.sin(theta) * math.cos(phi), math.sin(theta) * math.sin(phi),
            math.cos(theta))
    that = (math.cos(theta) * math.cos(phi), math.cos(theta) * math.sin(phi),
            -math.sin(theta))
    phat = (-math.sin(phi), math.cos(phi), 0.0)
    dot = lambda a, b: sum(x * y for x, y in zip(a, b))                 # noqa: E731
    proj = (dot(grad_cart, rhat), dot(grad_cart, that), dot(grad_cart, phat))

    def F(rr, tt, pp):
        return f(rr * math.sin(tt) * math.cos(pp),
                 rr * math.sin(tt) * math.sin(pp),
                 rr * math.cos(tt))

    ht = 1e-6
    formula = ((F(r + hr, theta, phi) - F(r - hr, theta, phi)) / (2 * hr),
               (F(r, theta + ht, phi) - F(r, theta - ht, phi)) / (2 * ht) / r,
               (F(r, theta, phi + ht) - F(r, theta, phi - ht)) / (2 * ht)
               / (r * math.sin(theta)))
    names = ("r", "theta", "phi")
    print("component   grad f . e_i (from Cartesian)   formula   relative difference")
    for i in range(3):
        rel = abs(proj[i] - formula[i]) / abs(formula[i])
        print(f"   {names[i]:>5}      {proj[i]: .10e}     {formula[i]: .10e}"
              f"     {rel:.3e}")
    print("Components: df/dr, (1/r) df/dtheta, (1/(r sin theta)) df/dphi.")

    section("5. Propagating uncertainty with the Jacobian: J C J^T vs Monte Carlo")
    r, theta, phi = EARTH_RADIUS, math.pi / 4.0, math.pi / 6.0
    sigma_r, sigma_t, sigma_p = 5.0, 1.0e-6, 1.0e-6
    J = jacobian_fd(
        lambda rr, tt, pp: (rr * math.sin(tt) * math.cos(pp),
                            rr * math.sin(tt) * math.sin(pp),
                            rr * math.cos(tt)),
        (r, theta, phi), 1e-3)
    C_sph = [[sigma_r ** 2, 0.0, 0.0],
             [0.0, sigma_t ** 2, 0.0],
             [0.0, 0.0, sigma_p ** 2]]
    C_cart = matmul3(matmul3(J, C_sph), transpose3(J))

    random.seed(31415)
    samples = 500000
    acc = [[0.0] * 3 for _ in range(3)]
    mean = [0.0] * 3
    pts = []
    for _ in range(samples):
        rr = r + random.gauss(0.0, sigma_r)
        tt = theta + random.gauss(0.0, sigma_t)
        pp = phi + random.gauss(0.0, sigma_p)
        q = [rr * math.sin(tt) * math.cos(pp),
             rr * math.sin(tt) * math.sin(pp),
             rr * math.cos(tt)]
        pts.append(q)
        for i in range(3):
            mean[i] += q[i] / samples
    for q in pts:
        for i in range(3):
            for j in range(3):
                acc[i][j] += (q[i] - mean[i]) * (q[j] - mean[j]) / (samples - 1)

    print("Cartesian covariance from J C J^T  (m^2):")
    for row in C_cart:
        print("   " + "  ".join(f"{v: .4e}" for v in row))
    print("Cartesian covariance from Monte Carlo (m^2):")
    for row in acc:
        print("   " + "  ".join(f"{v: .4e}" for v in row))
    print("diagonal relative differences between the two:")
    for i, name in enumerate("xyz"):
        rel = abs(C_cart[i][i] - acc[i][i]) / C_cart[i][i]
        print(f"   sigma_{name}^2: {C_cart[i][i]:.4e} vs {acc[i][i]:.4e}"
              f"   relative difference = {rel:.3e}")
    print(f"Monte Carlo noise floor on a variance is sqrt(2/N) = "
          f"{math.sqrt(2.0 / samples):.3e} in relative terms.")
    print("The 1e-6 rad angular uncertainties become metres of horizontal error")
    print("because they are multiplied by r; the 5 m radial uncertainty stays")
    print("vertical. That scaling is the Jacobian at work.")


if __name__ == "__main__":
    main()
