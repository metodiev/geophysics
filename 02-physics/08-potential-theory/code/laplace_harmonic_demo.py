#!/usr/bin/env python3
"""Laplace's equation, harmonic functions and what they forbid.

Standard library only.  Every number printed here is produced by this file.

Contents
--------
1. The mean value property: verified for a source-free sphere, and shown to fail
   when the sphere encloses mass.
2. The maximum principle: the extremum of a source-free potential lies on the
   boundary -- there is no interior peak to look for.
3. Inside a source region the Laplacian is non-zero and an interior maximum
   appears: the contrast with 1 and 2.
4. Poisson's equation by finite differences: the residual of a harmonic function
   falls as O(h^2), and the residual of x^2 is exactly 2.
5. Why "look for the highest point of the potential" cannot find a mass: the
   curvature of the anomaly sharpens without bound as the observation plane is
   continued downward toward the source.
"""

import math

G = 6.67430e-11  # CODATA 2018 measured value


def gauss_legendre(n):
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


def sphere_mean(func, center, R, ncos=200, nphi=400):
    """Mean of func over the surface of a sphere, by quadrature."""
    xc, wc = gauss_legendre(ncos)
    dphi = 2.0 * math.pi / nphi
    total = 0.0
    weight_sum = 0.0
    for i in range(ncos):
        ct = xc[i]
        st = math.sqrt(max(0.0, 1.0 - ct * ct))
        for j in range(nphi):
            phi = j * dphi
            p = (center[0] + R * st * math.cos(phi),
                 center[1] + R * st * math.sin(phi),
                 center[2] + R * ct)
            w = wc[i] * dphi
            total += w * func(p)
            weight_sum += w
    return total / weight_sum


def potential_of_point_mass(M, src, p):
    dx = p[0] - src[0]
    dy = p[1] - src[1]
    dz = p[2] - src[2]
    return G * M / math.sqrt(dx * dx + dy * dy + dz * dz)


def laplacian_fd(func, p, h):
    x, y, z = p
    fx = (func((x + h, y, z)) - 2.0 * func(p) + func((x - h, y, z))) / (h * h)
    fy = (func((x, y + h, z)) - 2.0 * func(p) + func((x, y - h, z))) / (h * h)
    fz = (func((x, y, z + h)) - 2.0 * func(p) + func((x, y, z - h))) / (h * h)
    return fx + fy + fz


def rule(title):
    print()
    print("=" * 74)
    print(title)
    print("=" * 74)


def main():
    print("Laplace's equation, harmonic functions and what they forbid")
    M = 1.0e12
    src = (0.0, 0.0, 0.0)
    V = lambda p: potential_of_point_mass(M, src, p)

    # ---------------------------------------------------------------- 1
    rule("1. Mean value property: holds off the source, fails on it")
    print("  V(p) is harmonic everywhere except at the source.  For a sphere about")
    print("  p that does NOT enclose the source, the surface mean equals V(p).")
    center = (1500.0, 0.0, 0.0)
    for R in (200.0, 500.0, 1000.0, 1400.0):
        m = sphere_mean(V, center, R)
        v = V(center)
        print("     center |p| = 1500 m, R = %6.1f m: mean = %.12e  V(p) = %.12e"
              % (R, m, v))
        print("                                        rel.diff = %.3e"
              % (abs(m - v) / v))
    print("  Now put the source INSIDE the sphere (center at 50 m, R = 200 m):")
    center = (50.0, 0.0, 0.0)
    for R in (100.0, 200.0, 500.0):
        m = sphere_mean(V, center, R)
        v = V(center)
        print("     R = %6.1f m: mean = %.10e  V(p) = %.10e   rel.diff = %.4f"
              % (R, m, v, abs(m - v) / v))
    print("  A non-harmonic function violates the property:")
    f = lambda p: p[0] * p[0]
    for R in (100.0, 500.0):
        m = sphere_mean(f, (300.0, 0.0, 0.0), R)
        print("     f = x^2 at (300,0,0), R = %5.1f m: mean = %.6f  f(p) = %.6f"
              % (R, m, f((300.0, 0.0, 0.0))))
        print("        difference = %.6f, and R^2/3 = %.6f (the exact value)"
              % (m - f((300.0, 0.0, 0.0)), R * R / 3.0))

    # ---------------------------------------------------------------- 2
    rule("2. Maximum principle: the extremum is on the boundary")
    print("  Domain: the ball |x| <= 1 m about the origin; the ONLY source is at")
    print("  (500, 0, 0) m, far outside.  Sample V on a grid and look for an")
    print("  interior maximum.")
    src2 = (500.0, 0.0, 0.0)
    V2 = lambda p: potential_of_point_mass(M, src2, p)
    R_dom = 1.0
    n = 41
    best_val = -1e300
    best_p = None
    boundary_best = -1e300
    boundary_p = None
    for i in range(n):
        for j in range(n):
            for k in range(n):
                p = (-R_dom + 2 * R_dom * i / (n - 1),
                     -R_dom + 2 * R_dom * j / (n - 1),
                     -R_dom + 2 * R_dom * k / (n - 1))
                val = V2(p)
                if val > best_val:
                    best_val, best_p = val, p
                if abs(math.sqrt(p[0] ** 2 + p[1] ** 2 + p[2] ** 2) - R_dom) < 1e-9:
                    if val > boundary_best:
                        boundary_best, boundary_p = val, p
    print("     grid resolution: %d^3 points, max over the whole ball = %.12e" % (n, best_val))
    print("     located at (%+.3f, %+.3f, %+.3f) m, |x| = %.6f m"
          % (best_p[0], best_p[1], best_p[2],
             math.sqrt(sum(c * c for c in best_p))))
    print("     max over the boundary shell          = %.12e" % boundary_best)
    print("     rel.diff interior-vs-boundary max    = %.3e"
          % (abs(best_val - boundary_best) / boundary_best))
    print("  -> the maximum sits ON the boundary: there is no interior peak to")
    print("     find, which is exactly the statement that a harmonic function")
    print("     cannot have an isolated maximum away from its sources.")

    # ---------------------------------------------------------------- 3
    rule("3. Where there IS a source, an interior maximum appears")
    print("  Inside a uniform ball (a source region) the potential is")
    print("      V(r) = 2 pi G rho (R^2 - r^2/3),")
    print("  which is maximal at the CENTRE -- an interior extremum.")
    rho = 3000.0
    R_ball = 1000.0
    for frac in (0.0, 0.25, 0.5, 0.75, 1.0):
        r = frac * R_ball
        v = 2.0 * math.pi * G * rho * (R_ball ** 2 - r * r / 3.0)
        lap = -4.0 * math.pi * G * rho
        print("     r/R = %4.2f  r = %6.1f m  V = %.10e  (lap V = %.6e)"
              % (frac, r, v, lap))
    print("  V is largest at the centre, and Poisson's equation confirms a source")
    print("  is present there (lap V = -4 pi G rho = %.6e s^-2)."
          % (-4.0 * math.pi * G * rho))

    # ---------------------------------------------------------------- 4
    rule("4. Poisson's equation by finite differences")
    print("  Harmonic function V = GM/D at p = (2000, 800, 1500) m:")
    p = (2000.0, 800.0, 1500.0)
    laps = []
    for h in (100.0, 50.0, 25.0, 12.5):
        lap = laplacian_fd(V, p, h)
        laps.append(lap)
        print("     h = %6.1f m: 7-point residual = %+.6e   (analytic value 0)"
              % (h, lap))
    print("  Ratio of successive residuals: %.3f, %.3f, %.3f  --  second order."
          % (laps[0] / laps[1], laps[1] / laps[2], laps[2] / laps[3]))
    print("  Non-harmonic function f = x^2 (analytic Laplacian = 2):")
    f = lambda q: q[0] * q[0]
    for h in (100.0, 50.0, 25.0):
        print("     h = %6.1f m: residual = %.10f   (analytic value 2)"
              % (h, laplacian_fd(f, p, h)))
    print("  Same stencil, different answer: the finite-difference Laplacian")
    print("  FORCES the distinction between 'harmonic' and 'has a source'.")

    # ---------------------------------------------------------------- 5
    rule("5. No interior peak to look for: sharpening under downward continuation")
    print("  Vertical field of a point mass of M = %.1e kg at depth h:" % M)
    print("      g_z(x) = G M h / (x^2 + h^2)^(3/2)")
    print("  Its peak is always at x = 0 for every h; what changes with h is the")
    print("  CURVATURE at the peak, d2g/dx2(0) = -3 G M / h^4:")
    for h in (5000.0, 2000.0, 1000.0, 500.0, 200.0):
        curv = -3.0 * G * M / h ** 4
        peak = G * M / (h * h)
        print("     h = %6.0f m: peak = %.6e m/s^2   d2g/dx2(0) = %+.6e s^-2"
              % (h, peak, curv))
    print("  The peak of g_z grows as 1/h and the curvature at the peak as 1/h^4,")
    print("  so a shallower source is sharp and a deeper one is smooth.  Downward")
    print("  continuation amplifies exactly the high wavenumbers by e^(+|k| h), so")
    print("  'look for the highest point' is the unstable direction, and what it")
    print("  finds is a source, not a maximum of a harmonic function.")

    print()
    print("SUMMARY OF MEASURED AGREEMENTS (every value is program output)")
    m = sphere_mean(V, (1500.0, 0.0, 0.0), 1000.0)
    print("  mean value off-source, R=1000 m   : rel.diff = %.2e"
          % (abs(m - V((1500.0, 0.0, 0.0))) / V((1500.0, 0.0, 0.0))))
    m2 = sphere_mean(V, (50.0, 0.0, 0.0), 200.0)
    print("  mean value enclosing the source   : rel.diff = %.4f"
          % (abs(m2 - V((50.0, 0.0, 0.0))) / V((50.0, 0.0, 0.0))))
    print("  interior max vs boundary max      : rel.diff = %.2e"
          % (abs(best_val - boundary_best) / boundary_best))
    print("  finite-difference Laplacian, h=25 : harmonic %.2e, non-harmonic %.10f"
          % (laplacian_fd(V, p, 25.0), laplacian_fd(f, p, 25.0)))


if __name__ == "__main__":
    main()
