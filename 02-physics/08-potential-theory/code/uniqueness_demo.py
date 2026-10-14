#!/usr/bin/env python3
"""Uniqueness of the boundary-value problem, and non-uniqueness of the source.

Standard library only.  Every printed number is computed here.

The two results this file makes numerical are different and are often confused:

  * Given boundary data, the harmonic field above the boundary is UNIQUE
    (part 1).
  * Given the field, the source distribution below the boundary is NOT unique;
    the null space is infinite-dimensional (parts 2-5).

The equivalent stratum used in parts 2-4 is exact.  A line mass of strength
lambda at depth z0 produces, on a surface, the vertical field

    g_z(x) = 2 G lambda z0 / (x^2 + z0^2) .

A horizontal sheet of mass per unit area sigma(x) at depth h produces

    g_z(x) = 2 G h * integral sigma(x') / ((x - x')^2 + h^2) dx' .

Taking sigma_h(x) = (lambda / pi) (z0 - h) / (x^2 + (z0 - h)^2), whose total mass
per unit length is exactly lambda, reproduces the line-mass field for EVERY depth
h < z0.  That family is the equivalent stratum.
"""

import math

G = 6.67430e-11  # CODATA 2018 measured value


def rule(title):
    print()
    print("=" * 74)
    print(title)
    print("=" * 74)


def line_mass_gz(lam, z0, x):
    return 2.0 * G * lam * z0 / (x * x + z0 * z0)


def sigma_equiv(lam, z0, h, x):
    """Areal density of the sheet at depth h equivalent to a line mass at z0."""
    a = z0 - h
    return lam / math.pi * a / (x * x + a * a)


def sheet_gz(sigma_of_x, h, x, half_width, n=20001):
    """Vertical field of a sheet at depth h, trapezoid rule over sigma.

    An infinite line of mass per unit length lambda at depth h produces
    2 G lambda h / (x^2 + h^2).  A sheet is a continuum of such lines with
    lambda = sigma(x') dx', so the kernel here is h / ((x-x')^2 + h^2) with no
    additional power -- this is the two-dimensional kernel, not the 3-D one.
    """
    step = 2.0 * half_width / (n - 1)
    tot = 0.0
    for i in range(n):
        xp = -half_width + i * step
        w = 0.5 * step if (i == 0 or i == n - 1) else step
        r2 = (x - xp) ** 2 + h * h
        tot += w * sigma_of_x(xp) * h / r2
    return 2.0 * G * tot


def sheet_gz_deriv(sigma_of_x, h, x, half_width, n=20001):
    """Horizontal derivative of the sheet field, by finite differences."""
    d = 1.0
    return ((sheet_gz(sigma_of_x, h, x + d, half_width, n)
             - sheet_gz(sigma_of_x, h, x - d, half_width, n)) / (2 * d))


def solve_dirichlet(n, u_top, sweeps, init):
    """Gauss-Seidel solution of Laplace's equation on the unit square.

    u = u_top on y = 1 and u = 0 on the other three sides.
    """
    h = 1.0 / (n - 1)
    u = [[init(i, j) for j in range(n)] for i in range(n)]
    for i in range(n):
        u[i][0] = 0.0
        u[i][n - 1] = u_top
        u[0][i] = 0.0
        u[n - 1][i] = 0.0
    for _ in range(sweeps):
        for i in range(1, n - 1):
            for j in range(1, n - 1):
                u[i][j] = 0.25 * (u[i - 1][j] + u[i + 1][j]
                                  + u[i][j - 1] + u[i][j + 1])
    return h, u


def dirichlet_series(x, y, nterms=80):
    """Exact solution u(x,y) with u = 1 on y = 1 and 0 on the other sides."""
    tot = 0.0
    for k in range(nterms):
        m = 2 * k + 1
        tot += (4.0 / (m * math.pi) * math.sin(m * math.pi * x)
                * math.sinh(m * math.pi * y) / math.sinh(m * math.pi))
    return tot


def main():
    print("Uniqueness of the boundary-value problem, non-uniqueness of the source")
    print("G = %.5e m^3 kg^-1 s^-2 (CODATA 2018, measured)" % G)

    # ---------------------------------------------------------------- 1
    rule("1. Uniqueness: one boundary-value problem, one solution")
    print("  Solve Laplace's equation on the unit square, u = 1 on the top edge")
    print("  and u = 0 on the other three, by Gauss-Seidel relaxation from two")
    print("  completely different starting fields.")
    n, sweeps = 25, 4000
    print("     grid %d x %d" % (n, n))
    print("     sweeps     max |u_a - u_b| over the interior")
    ua_prev = None
    for s in (10, 100, 1000, 4000):
        if s > sweeps:
            break
        h, ua = solve_dirichlet(n, 1.0, s, lambda i, j: 0.0)
        h2, ub = solve_dirichlet(n, 1.0, s,
                                 lambda i, j: math.sin(3.0 * math.pi * i / (n - 1))
                                 * math.cos(5.0 * math.pi * j / (n - 1)))
        d = max(abs(ua[i][j] - ub[i][j])
                for i in range(1, n - 1) for j in range(1, n - 1))
        print("     %5d      %.3e" % (s, d))
    diff = d
    h, ua = solve_dirichlet(n, 1.0, sweeps, lambda i, j: 0.0)
    scale = max(ua[i][j] for i in range(n) for j in range(n))
    print("     peak value of the solution = %.6f" % scale)
    err = 0.0
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            err = max(err, abs(ua[i][j] - dirichlet_series(i * h, j * h)))
    print("     max |u_numerical - u_series|        = %.3e" % err)
    print("  Two different initial guesses converge to the same field, and it is")
    print("  the exact solution of the series: the Dirichlet boundary-value")
    print("  problem has one solution and the iteration finds it.")

    # ---------------------------------------------------------------- 2
    rule("2. The equivalent stratum: one field, one source per chosen depth")
    lam = 5.0e8          # kg/m, a line mass
    z0 = 2000.0          # m, depth of the line mass
    half = 50.0 * z0     # quadrature half-width
    print("  Line mass lambda = %.3e kg/m at depth z0 = %.0f m." % (lam, z0))
    print("  Its surface field: g_z(x) = 2 G lambda z0/(x^2 + z0^2).")
    print("  Sheet at depth h with sigma_h(x) = (lambda/pi)(z0-h)/(x^2+(z0-h)^2).")
    print()
    print("  sheet depth h   peak sigma (kg/m^2)   FWHM (m)   g_z(0) (m/s^2)")
    depths = (0.25 * z0, 0.5 * z0, 0.75 * z0, 0.9 * z0)
    for hh in depths:
        peak = lam / math.pi / (z0 - hh)
        fwhm = 2.0 * (z0 - hh)
        g0 = sheet_gz(lambda x, hh=hh: sigma_equiv(lam, z0, hh, x), hh, 0.0, half)
        print("     %8.0f m     %14.6e      %8.1f   %.10e"
              % (hh, peak, fwhm, g0))
    print("  Line mass reference g_z(0)                      = %.10e"
          % line_mass_gz(lam, z0, 0.0))
    print()
    print("  Compare the fields station by station:")
    print("     x (m)    line mass g_z      h = 500 m         h = 1000 m        h = 1500 m")
    worst = 0.0
    for x in (0.0, 500.0, 1000.0, 2000.0, 5000.0):
        gl = line_mass_gz(lam, z0, x)
        row = []
        for hh in (500.0, 1000.0, 1500.0):
            gs = sheet_gz(lambda xp, hh=hh: sigma_equiv(lam, z0, hh, xp), hh, x, half)
            row.append(gs)
            worst = max(worst, abs(gs - gl) / gl)
        print("     %6.0f   %.10e   %.10e   %.10e   %.10e"
              % (x, gl, row[0], row[1], row[2]))
    print("  Worst relative difference over the stations: %.3e" % worst)
    print()
    print("  The residual is the quadrature, not the physics.  Refining the sheet")
    print("  integral at x = 0 for h = 1000 m:")
    gl0 = line_mass_gz(lam, z0, 0.0)
    for (mult, nn) in ((50.0, 20001), (200.0, 80001), (800.0, 320001)):
        gs = sheet_gz(lambda xp: sigma_equiv(lam, z0, 1000.0, xp), 1000.0, 0.0,
                      mult * z0, nn)
        print("     half-width %6.0f z0, %7d points: rel.diff = %.3e"
              % (mult, nn, abs(gs - gl0) / gl0))

    # ---------------------------------------------------------------- 3
    rule("3. The null space: two equivalent strata differ by an annihilator")
    print("  Take the difference of the density profiles at h = 500 m and")
    print("  h = 1500 m.  Both reproduce the same field, so the difference")
    print("  distribution must produce zero field everywhere above the survey.")
    h1, h2 = 500.0, 1500.0
    s1 = lambda x: sigma_equiv(lam, z0, h1, x)
    s2 = lambda x: sigma_equiv(lam, z0, h2, x)
    delta = lambda x: s1(x) - s2(x)
    peak = max(abs(s1(x)) for x in (0.0,))
    print("     peak |sigma(h=500)|  = %.6e kg/m^2" % s1(0.0))
    print("     peak |sigma(h=1500)| = %.6e kg/m^2" % s2(0.0))
    print("     peak |sigma_1 - sigma_2| = %.6e kg/m^2" % abs(delta(0.0)))
    print("     relative size of the annihilator at x = 0 : %.4f"
          % (abs(delta(0.0)) / s1(0.0)))
    print()
    print("     x (m)     field of the annihilator (m/s^2)   as fraction of the peak")
    g_peak = line_mass_gz(lam, z0, 0.0)
    worst_ann = 0.0
    for x in (0.0, 500.0, 1000.0, 2000.0, 5000.0, 10000.0):
        # the annihilator sheet is the difference of two sheets at different depths,
        # so integrate each and subtract
        ga = (sheet_gz(s1, h1, x, half) - sheet_gz(s2, h2, x, half))
        frac = abs(ga) / g_peak
        worst_ann = max(worst_ann, frac)
        print("     %6.0f     %+.6e              %.3e" % (x, ga, frac))
    print("  The annihilator carries structure of order the signal itself and")
    print("  produces a field of order %.1e of the peak: the forward operator has a"
          % worst_ann)
    print("  non-trivial kernel, and every source in the kernel is invisible.")

    # ---------------------------------------------------------------- 4
    rule("4. The derivatives do not break the ambiguity")
    print("  Horizontal gradient dg_z/dx of the line mass and of an equivalent")
    print("  sheet: if the fields agree, all their derivatives agree too.")
    x = 1000.0
    d = 1.0
    gl_deriv = ((line_mass_gz(lam, z0, x + d) - line_mass_gz(lam, z0, x - d))
                / (2 * d))
    gs_deriv = sheet_gz_deriv(lambda xp: sigma_equiv(lam, z0, 1000.0, xp),
                              1000.0, x, half)
    print("     dg_z/dx, line mass            = %.10e s^-2" % gl_deriv)
    print("     dg_z/dx, equivalent sheet     = %.10e s^-2" % gs_deriv)
    print("     relative difference           = %.3e"
          % (abs(gs_deriv - gl_deriv) / abs(gl_deriv)))

    # ---------------------------------------------------------------- 5
    rule("5. The slab ambiguity, for completeness")
    print("  An infinite slab of density rho and thickness t gives g_z = 2 pi G rho t,")
    print("  so every pair with the same product is indistinguishable:")
    g_ref = None
    for rho, t in ((2670.0, 400.0), (5340.0, 200.0), (10680.0, 100.0),
                   (42720.0, 25.0)):
        g = 2 * math.pi * G * rho * t
        if g_ref is None:
            g_ref = g
        print("     rho = %7.1f kg/m^3, t = %6.1f m : g_z = %.12e m/s^2   rel.dev = %.1e"
              % (rho, t, g, abs(g - g_ref) / g_ref))
    print("  Every real Bouguer reduction needs an assumed density for exactly")
    print("  this reason, and the residual ambiguity propagates into the anomaly.")

    print()
    print("SUMMARY OF MEASURED AGREEMENTS (every value is program output)")
    print("  Dirichlet: two initial guesses, max difference = %.2e" % diff)
    print("  Dirichlet numerical vs series, max error       = %.2e" % err)
    print("  equivalent stratum vs line mass, worst rel.diff= %.2e" % worst)
    print("  annihilator field as fraction of the peak      = %.2e" % worst_ann)


if __name__ == "__main__":
    main()
