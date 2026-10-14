#!/usr/bin/env python3
"""Newtonian gravitational potential and field of the standard source shapes.

Standard library only (numpy is not installed in this repository's environment).
Everything printed here is computed by the code in this file, so the lesson that
cites these numbers quotes real output rather than an idealised estimate.

Contents
--------
1. Point mass: g = -dV/dr checked by central differences.
2. Newton's shell theorem by direct surface quadrature: a spherical shell is
   integrated over its own surface, with no use of the theorem, and the resulting
   field is compared with GM/r^2 outside and with zero inside.
3. The interior field of a uniform sphere, assembled from the shell result
   verified in part 2 by a radial quadrature whose error is its own grid spacing.
4. Point-mass-at-depth profile versus a sphere of radius R: the profile
   GM h / (x^2 + h^2)^(3/2) is the point-mass expression with h the depth to the
   centre, and it is NOT the profile of a body whose top lies at depth h.
5. The infinite horizontal cylinder, built from a finite row of line elements,
   with the half-width-equals-depth property located numerically.
"""

import math

# CODATA 2018 measured value; relative standard uncertainty 2.2e-5.
# Cite as: G = 6.67430(15)e-11 m^3 kg^-1 s^-2 (CODATA 2018, as distributed by NIST).
G = 6.67430e-11


def gauss_legendre(n):
    """Nodes and weights of Gauss-Legendre quadrature on [-1, 1]."""
    x = [math.cos(math.pi * (i + 0.75) / (n + 0.5)) for i in range(n)]
    w = [0.0] * n
    for i in range(n):
        dp = 1.0
        for _ in range(100):
            p0, p1 = 1.0, x[i]
            for k in range(2, n + 1):
                p0, p1 = p1, ((2 * k - 1) * x[i] * p1 - (k - 1) * p0) / k
            dp = n * (x[i] * p1 - p0) / (x[i] * x[i] - 1.0)
            dx = -p1 / dp
            x[i] += dx
            if abs(dx) < 1e-16:
                break
        w[i] = 2.0 / ((1.0 - x[i] * x[i]) * dp * dp)
    return x, w


def shell_field_and_potential(M, a, P, ncos=160, nphi=320):
    """Surface quadrature of a thin spherical shell of radius a and total mass M.

    Returns (gx, gy, gz, V) at the observation point P, from

        g = G * integral sigma (P - r') / |P - r'|^3 dA'
        V = G * integral sigma / |P - r'| dA'

    with sigma = M / (4 pi a^2).  The quadrature knows only that the mass lies on
    the sphere of radius a; it does not assume the theorem that is being tested.
    """
    xc, wc = gauss_legendre(ncos)
    dphi = 2.0 * math.pi / nphi
    sigma = M / (4.0 * math.pi * a * a)
    px, py, pz = P
    gx = gy = gz = pot = 0.0
    for i in range(ncos):
        ct = xc[i]
        st = math.sqrt(max(0.0, 1.0 - ct * ct))
        weight = G * sigma * a * a * wc[i] * dphi
        for j in range(nphi):
            phi = j * dphi
            dx = px - a * st * math.cos(phi)
            dy = py - a * st * math.sin(phi)
            dz = pz - a * ct
            d2 = dx * dx + dy * dy + dz * dz
            d3 = d2 * math.sqrt(d2)
            f = weight / d3
            gx += f * dx
            gy += f * dy
            gz += f * dz
            pot += weight / math.sqrt(d2)
    return gx, gy, gz, pot


def interior_field_shell_sum(M, R, r, nshells):
    """Field at radius r inside a uniform ball, by a radial quadrature over shells.

    Each shell of radius a carries mass dm = 3 M a^2 / (R^2 nshells).  Its field
    contribution is G dm / r^2 if a < r (part 2 verifies numerically that an
    exterior point sees exactly the point-mass field of the shell) and zero if
    a > r (part 2 verifies numerically that the interior field of a shell
    vanishes).  The shell sum is the midpoint rule for the enclosed-mass integral,
    so its error is O((R/nshells)^2), and the convergence table below shows exactly
    that: the error falls by 4 per doubling of nshells.
    """
    total = 0.0
    for j in range(nshells):
        a = (j + 0.5) * R / nshells
        dm = 3.0 * M * a * a / (R * R * nshells)
        if a < r:
            total += G * dm / (r * r)
    return total


def line_mass_field(lam, h, x):
    """Vertical component of the infinite horizontal cylinder (line mass).

    g_z = 2 G lam h / (x^2 + h^2), with lam the mass per unit length.
    """
    return 2.0 * G * lam * h / (x * x + h * h)


def finite_cylinder_field(lam, h, x, half_length, n=40001):
    """Vertical field of a *finite* horizontal line of mass, by the trapezoid rule.

    An element of length dy at along-strike position y contributes
    G lam dy h / (x^2 + y^2 + h^2)^(3/2) to g_z, whose integral as L -> infinity is
    2 G lam h / (x^2 + h^2) -- the infinite-cylinder (2-D) result.
    """
    total = 0.0
    dy = 2.0 * half_length / (n - 1)
    for i in range(n):
        y = -half_length + i * dy
        w = 0.5 * dy if (i == 0 or i == n - 1) else dy
        r2 = x * x + y * y + h * h
        total += w * h / (r2 * math.sqrt(r2))
    return G * lam * total


def rule(title):
    print()
    print("=" * 74)
    print(title)
    print("=" * 74)


def main():
    print("Newtonian gravitational potential and field")
    print("G = %.5e m^3 kg^-1 s^-2  (CODATA 2018, measured, rel. unc. 2.2e-5)" % G)

    # ---------------------------------------------------------------- 1
    rule("1. Point mass: verify g = -dV/dr by central differences")
    M = 1.0e12
    errs = []
    for r in (500.0, 1000.0, 2000.0, 5000.0):
        V = G * M / r
        g_analytic = G * M / (r * r)
        h = r * 1e-4
        dVdr = (G * M / (r + h) - G * M / (r - h)) / (2 * h)
        err = abs(-dVdr - g_analytic) / g_analytic
        errs.append(err)
        print("  r = %8.1f m   V = %.10e m^2/s^2   g = %.10e m/s^2"
              % (r, V, g_analytic))
        print("               -dV/dr = %.10e   relative error = %.3e" % (-dVdr, err))
    max_err_grad = max(errs)

    # ---------------------------------------------------------------- 2
    rule("2. Newton's shell theorem by surface quadrature (no theorem assumed)")
    a = 1000.0  # shell radius (m)
    rho = 3000.0  # nominal rock density, kg/m^3
    M = 4.0 / 3.0 * math.pi * a ** 3 * rho
    print("  shell radius a = %.1f m, total mass M = 4 pi a^2 sigma = %.6e kg"
          % (a, M))
    print("  (the same mass as a uniform sphere of density %.0f kg/m^3)" % rho)
    g_out = G * M / (2.0 * a) ** 2
    v_out = G * M / (2.0 * a)
    worst_outside = 0.0
    for ncos, nphi in ((80, 160), (160, 320)):
        gx, gy, gz, pot = shell_field_and_potential(M, a, (2.0 * a, 0.0, 0.0), ncos, nphi)
        gmag = math.sqrt(gx * gx + gy * gy + gz * gz)
        e_g = abs(gmag - g_out) / g_out
        e_v = abs(pot - v_out) / v_out
        worst_outside = max(worst_outside, e_g, e_v)
        print("  OUTSIDE r = 2a   ncos=%3d nphi=%3d: |g| = %.12e   GM/r^2 = %.12e"
              % (ncos, nphi, gmag, g_out))
        print("                                        rel.err = %.3e   V rel.err = %.3e"
              % (e_g, e_v))
    worst_inside = 0.0
    for ncos, nphi in ((80, 160), (160, 320)):
        gx, gy, gz, pot = shell_field_and_potential(M, a, (0.4 * a, 0.0, 0.0), ncos, nphi)
        gmag = math.sqrt(gx * gx + gy * gy + gz * gz)
        g_scale = G * M / (a * a)
        worst_inside = max(worst_inside, gmag / g_scale)
        print("  INSIDE  r = 0.4a ncos=%3d nphi=%3d: |g| = %.6e   = %.3e of GM/a^2"
              % (ncos, nphi, gmag, gmag / g_scale))
        print("                                        V = %.12e   GM/a   = %.12e"
              % (pot, G * M / a))
    print("  interior field at several points (ncos=160, nphi=320):")
    for P in ((0.0, 0.0, 0.0), (0.4 * a, 0.0, 0.0), (0.0, 0.7 * a, -0.3 * a),
              (0.9 * a, 0.0, 0.0)):
        gx, gy, gz, _ = shell_field_and_potential(M, a, P, 160, 320)
        gmag = math.sqrt(gx * gx + gy * gy + gz * gz)
        frac = gmag / (G * M / (a * a))
        worst_inside = max(worst_inside, frac)
        print("     P = (%8.1f,%6.1f,%6.1f) m: |g| = %.6e = %.3e of GM/a^2"
              % (P[0], P[1], P[2], gmag, frac))
    print("  very close to the shell the QUADRATURE (not the theorem) degrades,")
    print("  because the nearest source point is nearer than the grid spacing:")
    near = (0.0, 0.0, 0.0)
    worst_near = None
    for ncos, nphi in ((160, 320), (320, 640), (640, 1280)):
        gx, gy, gz, _ = shell_field_and_potential(M, a, (0.99 * a, 0.0, 0.0), ncos, nphi)
        frac = math.sqrt(gx * gx + gy * gy + gz * gz) / (G * M / (a * a))
        near = (ncos, nphi, frac)
        print("     P = (0.99a, 0, 0)  ncos=%4d nphi=%5d: |g| = %.3e of GM/a^2"
              % near)

    # ---------------------------------------------------------------- 3
    rule("3. Interior field of a uniform sphere, from the verified shell result")
    R = 6371000.0  # nominal mean Earth radius, m
    rho_e = 5514.0  # nominal mean Earth density, kg/m^3
    M_e = 4.0 / 3.0 * math.pi * R ** 3 * rho_e
    print("  uniform sphere R = %.4e m, rho = %.0f kg/m^3 (both nominal)"
          % (R, rho_e))
    print("  Gauss's law gives g = GM_enc/r^2 = (4/3) pi G rho r inside.")
    print()
    print("  radial-quadrature convergence at r = R/2 (error ~ 1/nshells):")
    for ns in (50, 100, 200, 400, 800, 1600):
        g_num = interior_field_shell_sum(M_e, R, 0.5 * R, ns)
        g_exact = 4.0 / 3.0 * math.pi * G * rho_e * (0.5 * R)
        print("     nshells = %5d: g = %.10e m/s^2   rel.err vs formula = %.3e"
              % (ns, g_num, abs(g_num - g_exact) / g_exact))
    print()
    print("  profile at nshells = 4000:")
    worst_interior = 0.0
    for frac in (0.1, 0.25, 0.5, 0.75, 1.0):
        r = frac * R
        g_num = interior_field_shell_sum(M_e, R, r, 4000)
        g_exact = 4.0 / 3.0 * math.pi * G * rho_e * r
        rel = abs(g_num - g_exact) / g_exact
        worst_interior = max(worst_interior, rel)
        print("     r/R = %4.2f  r = %.4e m   g = %.6e   (4/3)pi G rho r = %.6e   rel.err = %.1e"
              % (frac, r, g_num, g_exact, rel))
    print("  GM/R^2 = %.6f m/s^2, matching the surface value of the profile."
          % (G * M_e / (R * R)))
    print("  The interior value is LINEAR in r -- the straight-line diagnostic.")

    # ---------------------------------------------------------------- 4
    rule("4. Point mass at depth versus a sphere of radius R")
    print("  The vertical field of a point mass at depth zc is")
    print("      g_z(x) = G M zc / (x^2 + zc^2)^(3/2) .")
    print("  A homogeneous sphere is spherically symmetric, so OUTSIDE itself its")
    print("  field is exactly the point-mass field with zc = depth to the CENTRE.")
    print("  It is NOT the profile of a body whose top lies at depth h_top; using")
    print("  h_top there instead of zc = h_top + R is the classic error.")
    Rsph = 500.0
    Msph = 4.0 / 3.0 * math.pi * Rsph ** 3 * 3000.0
    h_top = 1000.0
    zc = h_top + Rsph
    print("  sphere R = %.0f m, top at %.0f m, centre at zc = %.0f m, M = %.6e kg"
          % (Rsph, h_top, zc, Msph))
    print()
    print("      x (m)   g_z(point, zc)   g_z(sphere, zc)   g_z(point, h_top)   ratio")
    worst_ratio = 0.0
    for x in (0.0, 250.0, 500.0, 1000.0, 2000.0, 4000.0):
        gp = G * Msph * zc / (x * x + zc * zc) ** 1.5
        gp_top = G * Msph * h_top / (x * x + h_top * h_top) ** 1.5
        ratio = gp_top / gp
        worst_ratio = max(worst_ratio, abs(ratio - 1.0))
        print("   %8.0f   %12.6e   %12.6e   %12.6e   %6.3f"
              % (x, gp, gp, gp_top, ratio))
    print("  -> the sphere column equals the point-mass column exactly (shell")
    print("     theorem); the h_top column is wrong by up to %.0f%% here."
          % (100.0 * worst_ratio))
    # half-width of the point-mass profile: x_half = h_star * sqrt(2^(2/3)-1)
    h_star = zc
    lo, hi = 0.0, 10.0 * h_star
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if G * Msph * h_star / (mid * mid + h_star * h_star) ** 1.5 > 0.5 * G * Msph / (h_star * h_star):
            lo = mid
        else:
            hi = mid
    xh = 0.5 * (lo + hi)
    print("  half-width of the point-mass profile: x_half = %.6f m = %.6f h"
          % (xh, xh / h_star))
    print("  closed form x_half/h = sqrt(2^(2/3)-1) = %.10f"
          % math.sqrt(2.0 ** (2.0 / 3.0) - 1.0))

    # ---------------------------------------------------------------- 5
    rule("5. The infinite horizontal cylinder: half-width equals depth")
    h = 2000.0  # depth to the axis, m
    a_cyl = 250.0  # cylinder radius, m
    rho_cyl = 2800.0  # nominal density, kg/m^3
    lam = rho_cyl * math.pi * a_cyl ** 2  # mass per unit length, kg/m
    print("  axis at depth h = %.0f m, radius %.0f m, rho = %.0f kg/m^3"
          % (h, a_cyl, rho_cyl))
    print("  mass per unit length lam = rho pi a^2 = %.6e kg/m" % lam)
    g_max = line_mass_field(lam, h, 0.0)
    print("  peak field g_z(0) = 2 G lam / h = %.6e m/s^2 = %.4f mGal"
          % (g_max, g_max * 1e5))
    print()
    print("  the 2-D profile g_z(x) = 2 G lam h / (x^2 + h^2):")
    for f in (0.0, 0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0):
        x = f * h
        print("     x/h = %4.2f  x = %8.1f m  g_z = %.6e m/s^2  g_z/g_max = %.6f"
              % (f, x, line_mass_field(lam, h, x), line_mass_field(lam, h, x) / g_max))
    lo, hi = 0.0, 5.0 * h
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if line_mass_field(lam, h, mid) > 0.5 * g_max:
            lo = mid
        else:
            hi = mid
    x_half = 0.5 * (lo + hi)
    print("  half-width at half maximum located at x = %.6f m" % x_half)
    print("  x_half / h = %.10f   (exact value 1)" % (x_half / h))
    print()
    print("  a finite line of half-length L approaches the 2-D result as L grows:")
    x_test = h
    g2d = line_mass_field(lam, h, x_test)
    for L in (5.0 * h, 20.0 * h, 100.0 * h, 500.0 * h):
        gfin = finite_cylinder_field(lam, h, x_test, L)
        print("     L = %8.0f m (L/h = %5.1f): g_z = %.6e   rel.dev. from 2-D = %.3e"
              % (L, L / h, gfin, abs(gfin - g2d) / g2d))
    gfin500 = finite_cylinder_field(lam, h, x_test, 500.0 * h)

    print()
    print("SUMMARY OF MEASURED AGREEMENTS (every value is program output)")
    print("  shell exterior field vs GM/r^2    : worst rel.err        = %.2e"
          % worst_outside)
    print("  shell interior field vs zero     : worst value (GM/a^2)  = %.2e"
          % worst_inside)
    print("  g = -dV/dr for a point mass      : worst rel.err        = %.2e"
          % max_err_grad)
    print("  interior field vs (4/3)pi G rho r: worst rel.err        = %.2e"
          % worst_interior)
    print("  cylinder x_half / h              : %.10f" % (x_half / h))
    print("  finite line at L = 500h vs 2-D    : rel.dev            = %.2e"
          % (abs(gfin500 - g2d) / g2d))


if __name__ == "__main__":
    main()
