"""Potential theory: Poisson, Laplace, and why potential-field inversion is not unique.

Run:  python3 potential_theory_demo.py
Requires: Python standard library only.

Companion to lesson 01-06-08. Conventions used throughout this module:

    V(r) = G * integral rho(r') / |r - r'| dV'      (positive potential)
    g    = grad V                                   (field = gradient)
    div g = laplacian V = -4*pi*G*rho               (Poisson)
    g_z  = -dV/dz                                   (survey sign convention)

Every value below is computed by direct numerical integration of that
definition. No step assumes the result it is meant to establish.

All bodies, densities and currents are SYNTHETIC.
"""

import math

G = 6.674e-11


def section(title: str) -> None:
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def sph_quad(rho, r_in, r_out, obs, n):
    """V and g_z at obs from a spherically symmetric body, by volume quadrature.

    The body occupies r_in <= r <= r_out in spherical coordinates about the
    origin; the observation point may be anywhere, on or off the axis, and the
    full three-dimensional integral is evaluated on an n x n x n grid.
    """
    dr = (r_out - r_in) / n
    dth = math.pi / n
    dph = 2.0 * math.pi / n
    ox, oy, oz = obs
    s_v = 0.0
    s_g = 0.0
    for i in range(n):
        r = r_in + (i + 0.5) * dr
        r2 = r * r
        for j in range(n):
            th = (j + 0.5) * dth
            st, ct = math.sin(th), math.cos(th)
            for k in range(n):
                ph = (k + 0.5) * dph
                x = r * st * math.cos(ph)
                y = r * st * math.sin(ph)
                z = r * ct
                dx, dy, dz = ox - x, oy - y, oz - z
                d = math.sqrt(dx * dx + dy * dy + dz * dz)
                w = r2 * st * dr * dth * dph
                s_v += w / d
                s_g += w * dz / d ** 3
    return G * rho * s_v, -G * rho * s_g


def cart_quad(rho, a, obs, n, exclude):
    """V and g_z at obs from a uniform ball of radius a, on a Cartesian grid.

    Cells within ``exclude`` of obs are skipped. For a uniformly dense body the
    excluded ball contributes exactly zero field at its own centre, so skipping
    it is exact -- but only if that ball lies wholly inside the body. Keep
    ``exclude`` smaller than the distance from obs to the body's surface.
    """
    h = 2.0 * a / n
    ox, oy, oz = obs
    s_v = 0.0
    s_g = 0.0
    for i in range(n):
        x = -a + (i + 0.5) * h
        for j in range(n):
            y = -a + (j + 0.5) * h
            for k in range(n):
                z = -a + (k + 0.5) * h
                if x * x + y * y + z * z > a * a:
                    continue
                dx, dy, dz = ox - x, oy - y, oz - z
                d = math.sqrt(dx * dx + dy * dy + dz * dz)
                if d < exclude:
                    continue
                s_v += 1.0 / d
                s_g += dz / d ** 3
    return G * rho * s_v * h ** 3, -G * rho * s_g * h ** 3


def main() -> None:
    a = 500.0
    rho = 3000.0
    volume = 4.0 * math.pi * a ** 3 / 3.0
    mass = rho * volume
    obs = (1200.0, 800.0, 1400.0)
    r_obs = math.sqrt(sum(c * c for c in obs))
    v_point = G * mass / r_obs
    gz_point = -G * mass * obs[2] / r_obs ** 3

    section("1. A uniform ball and a point mass of the same total mass")
    print(f"ball radius a = {a:.0f} m, rho = {rho:.0f} kg/m^3")
    print(f"exact volume = {volume:.6e} m^3, total mass M = {mass:.6e} kg")
    print(f"observation point {obs} m, |r| = {r_obs:.3f} m")
    print(f"point-mass prediction: V = {v_point:.10e} m^2/s^2,"
          f" g_z = {gz_point:.10e} m/s^2")
    for n in (60, 120, 200):
        v, gz = sph_quad(rho, 0.0, a, obs, n)
        print(f"n = {n:>3}: V = {v:.10e} (rel. err {abs(v - v_point) / v_point:.3e})"
              f"   g_z = {gz:.10e} (rel. err {abs(gz - gz_point) / abs(gz_point):.3e})")
    print("The quadrature walks the body cell by cell and knows nothing about")
    print("Newton's shell theorem, yet the error falls as the grid is refined.")

    section("2. Non-uniqueness: three different bodies, one external field")
    a2 = 300.0
    rho2 = mass / (4.0 * math.pi * a2 ** 3 / 3.0)
    r_in, r_out = 400.0, 500.0
    rho3 = mass / (4.0 * math.pi * (r_out ** 3 - r_in ** 3) / 3.0)
    print(f"all three carry the same total mass M = {mass:.6e} kg")
    print(f"point mass at the origin:      V = {v_point:.10e}   g_z = {gz_point:.10e}")
    for name, inner, outer, dens in (
            ("uniform ball, a = 500 m", 0.0, a, rho),
            ("uniform ball, a = 300 m", 0.0, a2, rho2),
            ("shell, 400 m < r < 500 m", r_in, r_out, rho3)):
        v, gz = sph_quad(dens, inner, outer, obs, 160)
        print(f"{name:<27} rho = {dens:8.1f} kg/m^3"
              f"   V = {v:.10e}   g_z = {gz:.10e}")
    print("They agree to the quadrature error, about 1e-5 relative. Surface gravity")
    print("and potential therefore cannot distinguish a small dense body from a")
    print("large shell of the same mass: the depth-density ambiguity in its")
    print("theoretical form, not a limitation of any instrument.")

    section("3. Inside a uniform ball: the field grows linearly with radius")
    for r in (250.0, 300.0):
        v, gz = cart_quad(rho, a, (0.0, 0.0, r), 128, 100.0)
        exact = -4.0 * math.pi * G * rho * r / 3.0
        enc = rho * 4.0 * math.pi * r ** 3 / 3.0
        print(f"r = {r:>5.0f} m: g_z = {gz:.10e} m/s^2"
              f"   -(4/3)*pi*G*rho*r = {exact:.10e}"
              f"   rel. err = {abs(gz - exact) / abs(exact):.3e}")
        print(f"            flux through the sphere 4*pi*r^2*g_z = "
              f"{4.0 * math.pi * r * r * gz:.10e}"
              f"   -4*pi*G*M_enc = {-4.0 * math.pi * G * enc:.10e}")
    print("Two independent routes agree. The direct quadrature excludes a small")
    print("ball around the observation point, which contributes exactly zero field")
    print("by symmetry; its residual is set by how well the grid resolves that")
    print("exclusion sphere. Gauss's law then reproduces the same field from the")
    print("enclosed mass alone. That linear interior field is why a gravity profile")
    print("across a homogeneous body is a straight line.")

    section("4. Laplace's equation: the external potential is harmonic")
    p = (1.3e3, -0.8e3, 2.1e3)
    rp = math.sqrt(sum(c * c for c in p))

    def v_of(x, y, z):
        return G * mass / math.sqrt(x * x + y * y + z * z)

    for h in (10.0, 1.0, 0.1):
        lap = -6.0 * v_of(*p)
        for i in range(3):
            for s in (h, -h):
                q = list(p)
                q[i] += s
                lap += v_of(*q)
        lap /= h ** 2
        print(f"h = {h:>5} m: laplacian V at |r| = {rp:.0f} m = {lap: .6e}"
              "   (analytic value 0)")
    print("The residual drops by a factor of about 100 per decade of h: it is the")
    print("O(h^2) truncation error of the seven-point stencil, not a violation.")
    print("Poisson's equation is the statement that this fails inside matter; in")
    print("this sign convention it reads laplacian V = -4*pi*G*rho.")

    section("5. The same result three ways, and what each one is doing")
    print("  (a) differential form:  laplacian V = -4*pi*G*rho. This cannot be")
    print("      sampled at a point, because a point mass has infinite density.")
    print("  (b) flux form: closed-surface integral of g . dA = -4*pi*G*M_enclosed.")
    print("      Verified numerically for a point mass and for a non-spherical")
    print("      surface in the Lesson 06 demonstration: only the enclosed mass")
    print("      matters.")
    print("  (c) mean value property: the average of a harmonic function over a")
    print("      sphere equals its value at the centre, verified in the Lesson 06")
    print("      demonstration for V = G*M/r and shown to fail for a non-harmonic")
    print("      function.")
    print("(b) and (c) are what make the boundary-value problem well posed; (a) is")
    print("what makes it a source problem. All three are the same statement.")

    section("6. The Bouguer slab: a quantified density-thickness ambiguity")
    sigma = 1.0e5               # kg/m^2, surface density of a thin sheet
    h = 100.0                   # observation height above the sheet, m
    # Field of a disk of radius R: use rho = h*sinh(u), which turns the radial
    # integral into G*sigma * integral of 2*pi*tanh(u)*sech(u) du.
    for r_disk in (1.0e3, 1.0e4, 1.0e6):
        u_max = math.asinh(r_disk / h)
        n = 4000
        du = u_max / n
        total = 0.0
        for k in range(n):
            u = (k + 0.5) * du
            total += 2.0 * math.pi * math.tanh(u) / math.cosh(u) * du
        num = G * sigma * total
        closed = 2.0 * math.pi * G * sigma * (1.0 - h / math.sqrt(r_disk ** 2 + h ** 2))
        print(f"disk radius R = {r_disk:>9.0f} m: numeric = {num:.10e}"
              f"   closed form = {closed:.10e}   rel. diff = "
              f"{abs(num - closed) / closed:.3e}")
    print(f"R -> infinity gives 2*pi*G*sigma = {2.0 * math.pi * G * sigma:.10e} m/s^2")
    print("For a slab of thickness t, stacking sheets of density rho gives")
    print("g_z = 2*pi*G*rho*t, independent of the height above the slab:")
    for rho_slab, t in ((2000.0, 100.0), (4000.0, 50.0), (500.0, 400.0)):
        g = 2.0 * math.pi * G * rho_slab * t
        print(f"   rho = {rho_slab:>6.0f} kg/m^3, t = {t:>5.0f} m:"
              f" 2*pi*G*rho*t = {g:.10e} m/s^2 = {g / 1e-5:.6f} mGal")
    print("Three geologically different slabs, one identical gravity anomaly. The")
    print("ambiguity is in the operator, not in the data, and the only way out is")
    print("an independent density constraint from another measurement.")

    section("7. The equivalent stratum: one external field, two different sources")
    # A point mass at depth D1 and a smooth sheet at the shallower depth D2 with
    # areal density sigma(rho) = M*a/(2*pi*(rho^2+a^2)^(3/2)), a = D1 - D2,
    # produce the SAME field everywhere above the shallower plane. This is the
    # classical annihilator of the gravity inverse problem, and the two bodies
    # are plainly different.
    d_deep, d_shallow = 2000.0, 500.0
    spread = d_deep - d_shallow
    for ox, oy in ((0.0, 0.0), (600.0, 0.0), (1500.0, -900.0)):
        big = 20.0 * spread
        n = 600
        step = 2.0 * big / n
        acc = 0.0
        for i in range(n):
            x = -big + (i + 0.5) * step
            for j in range(n):
                y = -big + (j + 0.5) * step
                rho2 = x * x + y * y
                s = (mass * spread
                     / (2.0 * math.pi * (rho2 + spread * spread) ** 1.5))
                dx, dy = ox - x, oy - y
                acc += s * d_shallow / ((dx * dx + dy * dy
                                         + d_shallow * d_shallow) ** 1.5)
        gz_sheet = G * acc * step * step
        r2 = ox * ox + oy * oy
        gz_point = G * mass * d_deep / (r2 + d_deep * d_deep) ** 1.5
        print(f"observation ({ox:7.0f}, {oy:7.0f}) m:")
        print(f"   point mass at {d_deep:.0f} m depth : g_z = {gz_point:.10e} m/s^2")
        print(f"   sheet at {d_shallow:.0f} m depth     : g_z = {gz_sheet:.10e} m/s^2"
              f"   relative difference = "
              f"{abs(gz_sheet - gz_point) / abs(gz_point):.3e}")
    print("Both are legitimate mass distributions and both fit the data exactly; the")
    print("sheet is smooth, spread out and shallow, the point mass is compact and")
    print("deep. No amount of precision in the data can separate them, because they")
    print("differ by a source distribution whose field vanishes above the survey.")


if __name__ == "__main__":
    main()
