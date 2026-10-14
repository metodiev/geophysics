#!/usr/bin/env python3
"""Spherical harmonics, Legendre expansion and multipole coefficients.

Standard library only.  Every printed number is computed here.

Conventions used throughout (state them in every calculation):
  * Y_lm(theta, phi) = sqrt((2l+1)(l-m)!/(4 pi (l+m)!)) P_l^m(cos theta) e^{i m phi}
    with the Condon-Shortley phase in P_l^m.
  * Exterior potential of a body of total mass M confined inside radius a:
       V(r,theta,phi) = (GM/r) sum_l (a/r)^l sum_m C_lm Y_lm(theta,phi),
       C_lm = (4 pi /(2l+1)) q_lm /(M a^l),  q_lm = integral rho r'^l Y_lm* dV'.
  * For an axisymmetric body the same content is written
       V = (GM/r) [1 - sum_{l>=1} J_l (a/r)^l P_l(cos theta)],
       J_l = -(1/(M a^l)) * integral rho r'^l P_l(cos theta') dV'.

Contents
--------
1. Legendre polynomials: recurrence, endpoint values, orthogonality.
2. Associated Legendre functions: verified by the Legendre differential
   equation, not by comparison with a table.
3. Spherical harmonic orthonormality by two-dimensional quadrature.
4. The Green's-function (Legendre) expansion of 1/|r - r'| and its convergence.
5. Multipole expansion of a point-mass system, and the vanishing of the dipole
   when the origin is placed at the centre of mass.
6. A uniform ball has only l = 0: computed coefficients, not asserted.
7. The quadrupole coefficient J_2 of a homogeneous oblate spheroid, and the
   comparison with the measured value for the Earth.
"""

import cmath
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


def legendre_p(n, x):
    """P_n(x) by the Bonnet recurrence."""
    if n == 0:
        return 1.0
    if n == 1:
        return x
    p0, p1 = 1.0, x
    for k in range(2, n + 1):
        p0, p1 = p1, ((2 * k - 1) * x * p1 - (k - 1) * p0) / k
    return p1


def assoc_legendre(l, m, x):
    """P_l^m(x) with the Condon-Shortley phase, m >= 0."""
    if m > l:
        return 0.0
    somx2 = math.sqrt(max(0.0, 1.0 - x * x))
    pmm = 1.0
    fact = 1.0
    for _ in range(1, m + 1):
        pmm *= -fact * somx2
        fact += 2.0
    if l == m:
        return pmm
    pmmp1 = x * (2 * m + 1) * pmm
    if l == m + 1:
        return pmmp1
    pll = 0.0
    for ll in range(m + 2, l + 1):
        pll = (x * (2 * ll - 1) * pmmp1 - (ll + m - 1) * pmm) / (ll - m)
        pmm, pmmp1 = pmmp1, pll
    return pll


def ylm(l, m, theta, phi):
    """Complex spherical harmonic Y_lm(theta, phi), including negative m."""
    if m < 0:
        return ((-1) ** m) * ylm(l, -m, theta, phi).conjugate()
    norm = math.sqrt((2 * l + 1) / (4 * math.pi)
                     * math.factorial(l - m) / math.factorial(l + m))
    return norm * assoc_legendre(l, m, math.cos(theta)) * cmath.exp(1j * m * phi)


def rule(title):
    print()
    print("=" * 74)
    print(title)
    print("=" * 74)


def main():
    print("Spherical harmonics, Legendre expansion and multipole coefficients")

    # ---------------------------------------------------------------- 1
    rule("1. Legendre polynomials")
    xc, wc = gauss_legendre(80)
    print("  P_l(1) = 1 and P_l(-1) = (-1)^l for l = 0..8:")
    worst_end = 0.0
    for l in range(0, 9):
        a = legendre_p(l, 1.0)
        b = legendre_p(l, -1.0)
        dev = max(abs(a - 1.0), abs(b - (-1.0) ** l))
        worst_end = max(worst_end, dev)
        print("     l = %d : P_l(1) = %+.12f   P_l(-1) = %+.12f   dev = %.1e"
              % (l, a, b, dev))
    worst_orth = 0.0
    for l in range(0, 6):
        for m in range(0, 6):
            val = sum(wc[i] * legendre_p(l, xc[i]) * legendre_p(m, xc[i])
                      for i in range(80))
            target = 2.0 / (2 * l + 1) if l == m else 0.0
            worst_orth = max(worst_orth, abs(val - target))
    print("  Orthogonality integral P_l P_m dx = 2/(2l+1) delta_lm,")
    print("  worst deviation over l,m = 0..5 : %.3e" % worst_orth)

    # ---------------------------------------------------------------- 2
    rule("2. Associated Legendre functions and the Legendre equation")
    print("  The associated functions must satisfy")
    print("     (1-x^2) P'' - 2x P' + [l(l+1) - m^2/(1-x^2)] P = 0 .")
    print("  Residual by central differences (h = 1e-4) at x = 0.3, scaled by the")
    print("  magnitude of the terms so that large-P cases are comparable:")
    worst_ode = 0.0
    for (l, m) in ((1, 1), (2, 0), (2, 2), (3, 1), (4, 3), (5, 5)):
        x = 0.3
        h = 1e-4
        p0 = assoc_legendre(l, m, x)
        d1 = (assoc_legendre(l, m, x + h) - assoc_legendre(l, m, x - h)) / (2 * h)
        d2 = (assoc_legendre(l, m, x + h) - 2 * p0 + assoc_legendre(l, m, x - h)) / (h * h)
        res = ((1 - x * x) * d2 - 2 * x * d1
               + (l * (l + 1) - m * m / (1 - x * x)) * p0)
        scale = (abs((1 - x * x) * d2) + abs(2 * x * d1)
                 + abs(l * (l + 1) * p0) + abs(m * m / (1 - x * x) * p0))
        worst_ode = max(worst_ode, abs(res) / scale)
        print("     P_%d^%d(0.3) = %+.10f   normalised residual = %+.2e"
              % (l, m, p0, res / scale))

    # ---------------------------------------------------------------- 3
    rule("3. Spherical harmonic orthonormality")
    print("  Check integral Y_lm conj(Y_l'm') dOmega = delta_ll' delta_mm' for")
    print("  l, l' <= 3, by Gauss-Legendre quadrature in cos(theta) (40 nodes)")
    print("  and the trapezoid rule in phi (60 nodes).")
    nc, nphi = 40, 60
    xc, wc = gauss_legendre(nc)
    dphi = 2 * math.pi / nphi
    worst = 0.0
    worst_pair = None
    for l in range(0, 4):
        for m in range(-l, l + 1):
            for lp in range(0, 4):
                for mp in range(-lp, lp + 1):
                    acc = 0.0 + 0.0j
                    for i in range(nc):
                        th = math.acos(xc[i])
                        for j in range(nphi):
                            phi = j * dphi
                            acc += (wc[i] * dphi * ylm(l, m, th, phi)
                                    * ylm(lp, mp, th, phi).conjugate())
                    target = 1.0 if (l == lp and m == mp) else 0.0
                    dev = abs(acc - target)
                    if dev > worst:
                        worst, worst_pair = dev, (l, m, lp, mp)
    print("     worst deviation = %.3e at (l,m,l',m') = %s" % (worst, worst_pair))

    # ---------------------------------------------------------------- 4
    rule("4. The Legendre expansion of 1/|r - r'|")
    print("  For r > r':  1/|r-r'| = sum_l (r'^l / r^{l+1}) P_l(cos gamma).")
    r, rp, cg = 3.0, 1.2, 0.6
    exact = 1.0 / math.sqrt(r * r + rp * rp - 2 * r * rp * cg)
    print("     r = %.1f m, r' = %.1f m, cos(gamma) = %.1f, exact = %.12f"
          % (r, rp, cg, exact))
    print("     L     partial sum             rel.err")
    for L in (0, 1, 2, 4, 8, 16):
        s = sum((rp ** l) / r ** (l + 1) * legendre_p(l, cg) for l in range(0, L + 1))
        print("     %-5d %.12f      %.3e" % (L, s, abs(s - exact) / exact))
    print("  Every term is bounded by (r'/r)^l = %.1f^l, so the series converges"
          % (rp / r))
    print("  geometrically at worst; the individual P_l(0.6) oscillate, which is")
    print("  why the partial sums are not monotone at low L.")

    # ---------------------------------------------------------------- 5
    rule("5. Multipole coefficients of a point-mass system")
    a_ref = 1000.0
    theta_obs = math.radians(70.0)
    phi_obs = math.radians(110.0)
    r_obs = 2000.0
    # one mass, off axis
    M1, r1, t1, p1 = 1.0e11, 500.0, math.radians(40.0), math.radians(20.0)
    x1 = r1 * math.sin(t1) * math.cos(p1)
    y1 = r1 * math.sin(t1) * math.sin(p1)
    z1 = r1 * math.cos(t1)
    xo = r_obs * math.sin(theta_obs) * math.cos(phi_obs)
    yo = r_obs * math.sin(theta_obs) * math.sin(phi_obs)
    zo = r_obs * math.cos(theta_obs)
    direct = G * M1 / math.sqrt((xo - x1) ** 2 + (yo - y1) ** 2 + (zo - z1) ** 2)
    print("  Single mass M = %.1e kg at r' = %.0f m, theta' = 40 deg, phi' = 20 deg"
          % (M1, r1))
    print("  Observation at r = %.0f m, theta = 70 deg, phi = 110 deg:" % r_obs)
    print("     direct sum 1/|r-r'| form : V = %.12e" % direct)
    print("     L      truncated series V          rel.err")
    for L in (0, 1, 2, 3, 4, 6, 8):
        acc = 0.0 + 0.0j
        for l in range(0, L + 1):
            for m in range(-l, l + 1):
                q = M1 * r1 ** l * ylm(l, m, t1, p1).conjugate()
                C = (4 * math.pi / (2 * l + 1)) * q / (M1 * a_ref ** l)
                acc += (a_ref / r_obs) ** l * C * ylm(l, m, theta_obs, phi_obs)
        series = (G * M1 / r_obs) * acc
        print("     %-6d %.12e           %.3e"
              % (L, series.real, abs(series.real - direct) / direct))

    print()
    print("  The dipole and the centre of mass.  Two equal masses on the x axis at")
    print("  x = +400 m and x = -400 m (total 1.0e11 kg):")
    pts = [(5.0e10, 400.0), (5.0e10, -400.0)]
    for label, shift in (("origin at the centre of mass", 0.0),
                         ("origin shifted to x = +200 m", 200.0)):
        q1 = [0.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j]  # m = -1, 0, +1
        for (Mi, xi) in pts:
            xr = xi - shift
            rr = abs(xr)
            tr = 0.0 if xr >= 0 else math.pi
            for idx, m in enumerate((-1, 0, 1)):
                q1[idx] += Mi * rr * ylm(1, m, tr, 0.0).conjugate()
        mag = math.sqrt(sum(abs(v) ** 2 for v in q1))
        print("     %-32s |q_1| = %.6e kg m" % (label, mag))
    print("  The dipole vanishes when the origin is at the centre of mass -- which")
    print("  is why global field models put the origin there.")

    # ---------------------------------------------------------------- 6
    rule("6. A uniform ball has only the monopole outside itself")
    rho = 3000.0
    a_ball = 1000.0
    M_ball = 4.0 / 3.0 * math.pi * a_ball ** 3 * rho
    print("  Uniform ball: a = %.0f m, rho = %.0f kg/m^3, M = %.6e kg"
          % (a_ball, rho, M_ball))
    print("  C_l0 from quadrature over the ball, relative to C_00:")
    nc, nphi, nr = 24, 32, 24
    xc, wc = gauss_legendre(nc)
    xr, wr = gauss_legendre(nr)
    dphi = 2 * math.pi / nphi
    C00 = None
    for l in range(0, 7):
        acc = 0.0 + 0.0j
        for i in range(nc):
            th = math.acos(xc[i])
            for j in range(nphi):
                phi = j * dphi
                yst = ylm(l, 0, th, phi).conjugate()
                for k in range(nr):
                    rr = 0.5 * a_ball * (xr[k] + 1.0)
                    acc += (wc[i] * dphi * wr[k] * 0.5 * a_ball
                            * rr * rr * yst)
        q = rho * acc
        C = (4 * math.pi / (2 * l + 1)) * q / (M_ball * a_ball ** l)
        if l == 0:
            C00 = C
            print("     l = 0 : C_00 = %.10f   (= sqrt(4 pi) = %.10f)"
                  % (C.real, math.sqrt(4 * math.pi)))
        else:
            print("     l = %d : C_l0 = %+.6e   |C_l0 / C_00| = %.3e"
                  % (l, C.real, abs(C) / abs(C00)))
    print("  Only l = 0 survives: a spherically symmetric body is a pure monopole.")

    # ---------------------------------------------------------------- 7
    rule("7. The quadrupole coefficient J_2 of a homogeneous oblate spheroid")
    print("  For a homogeneous oblate spheroid with equatorial radius a and polar")
    print("  semi-axis c = a(1-f), the principal moments give exactly")
    print("      J_2 = (1 - (1-f)^2)/5 = (2f - f^2)/5 .")
    print("  The same number is computed here from the volume definition")
    print("      J_2 = -(1/(M a^2)) * integral rho r'^2 P_2(cos theta') dV'")
    print("  by mapping the ellipsoid onto the unit ball, (x,y,z) -> (a u, a v, c w).")
    worst_j2 = 0.0
    for f in (0.001, 0.0033528106647474805, 0.01, 0.05):
        a, c = 1.0, 1.0 - f
        nr, nc, nphi = 32, 32, 8
        xr, wr = gauss_legendre(nr)
        xc, wc = gauss_legendre(nc)
        dphi = 2 * math.pi / nphi
        vol = 4.0 / 3.0 * math.pi * a * a * c
        Mv = vol
        acc = 0.0
        for k in range(nr):
            u = 0.5 * (xr[k] + 1.0)
            for i in range(nc):
                w_ = xc[i]
                s_ = math.sqrt(max(0.0, 1.0 - w_ * w_))
                for j in range(nphi):
                    ph = j * dphi
                    X = a * u * s_ * math.cos(ph)
                    Y = a * u * s_ * math.sin(ph)
                    Z = c * u * w_
                    r2 = X * X + Y * Y + Z * Z
                    ct2 = Z * Z / r2 if r2 > 0 else 1.0
                    P2 = 0.5 * (3.0 * ct2 - 1.0)
                    acc += (wr[k] * 0.5 * wc[i] * dphi * (u * u)
                            * r2 * P2 * a * a * c)
        J2_num = -acc / (Mv * a * a)
        J2_form = (1.0 - (1.0 - f) ** 2) / 5.0
        worst_j2 = max(worst_j2, abs(J2_num - J2_form) / J2_form)
        print("     f = %.10f : J_2 quadrature = %.10e   (2f-f^2)/5 = %.10e"
              % (f, J2_num, J2_form))
        print("                  rel.diff = %.3e" % (abs(J2_num - J2_form) / J2_form))
    f_wgs = 1.0 / 298.257223563  # WGS 84 defining inverse flattening (exact datum)
    J2_hom = (1.0 - (1.0 - f_wgs) ** 2) / 5.0
    print("  With the WGS 84 defining flattening f = 1/298.257223563:")
    print("     homogeneous spheroid J_2 = %.6e" % J2_hom)
    J2_earth = 1.08e-3  # MEASURED; authoritative digits from ICGEM (see links)
    print("     measured Earth J_2       = %.6e  (measured input, not computed)"
          % J2_earth)
    print("     ratio measured / homogeneous = %.4f" % (J2_earth / J2_hom))
    print("  A ratio below 1 says the real Earth carries less quadrupole than a")
    print("  uniform body: its mass is concentrated toward the centre.")

    print()
    print("SUMMARY OF MEASURED AGREEMENTS (every value is program output)")
    print("  Legendre endpoint error            : max %.2e" % worst_end)
    print("  Legendre orthogonality residual    : max %.2e" % worst_orth)
    print("  Legendre-equation residual         : max %.2e" % worst_ode)
    print("  spherical harmonic orthonormality  : max %.2e" % worst)
    print("  homogeneous spheroid J_2 vs formula: worst rel.err = %.2e" % worst_j2)


if __name__ == "__main__":
    main()
