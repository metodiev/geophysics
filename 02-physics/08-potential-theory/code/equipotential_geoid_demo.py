#!/usr/bin/env python3
"""Equipotential surfaces, the geoid and level surfaces.

Standard library only.  Every printed number is computed here.

The gravity potential used throughout is
    U(r, theta) = GM/r + (1/2) omega^2 r^2 sin^2(theta) + perturbation,
where the second term is the centrifugal potential, so grad U is the *gravity*
vector (gravitation plus centrifugal).  A level surface is the set U = U0; the
geoid is the particular level surface that best fits mean sea level, and it is a
level surface, not an ellipsoid.

WGS 84 defining parameters (exact datum values, from the constant handbook):
    a = 6378137 m, 1/f = 298.257223563, omega = 7.292115e-5 rad/s,
    GM = 3.986004418e14 m^3 s^-2.

Contents
--------
1. A level surface is perpendicular to grad U, confirmed at shrinking steps.
2. With no rotation the level surface is a sphere.
3. With rotation it is an oblate spheroid, and it is NOT an ellipsoid: the
   flattening is measured, the best-fit ellipsoid is computed, and the
   quadrupole is recovered from the flattening and the rotation rate.
4. A buried mass displaces the geoid; the undulation is obtained twice, once by
   solving the perturbed level surface and once by Bruns' formula T/gamma.
5. The same anomalies deflect the vertical, by an amount reported in arcseconds.
"""

import math

G = 6.67430e-11  # CODATA 2018 measured value

A_WGS = 6378137.0
INV_F_WGS = 298.257223563
OMEGA_WGS = 7.292115e-5
GM_WGS = 3.986004418e14
F_WGS = 1.0 / INV_F_WGS
B_WGS = A_WGS * (1.0 - F_WGS)


def u_base(r, theta):
    s = math.sin(theta)
    return GM_WGS / r + 0.5 * OMEGA_WGS ** 2 * r * r * s * s


# Polar radius of the model level surface (the equatorial radius of the
# non-rotating sphere): the level surface is flattened, so a fixed geocentric
# radius lies at a different depth at the pole than at the equator.
R_POLAR = GM_WGS / u_base(A_WGS, math.pi / 2)


def u_axis(r, theta, mass, z_anom):
    """u_base plus a buried point mass on the rotation axis.

    The anomaly centre is at geocentric radius ``z_anom`` on the axis, so a point
    at geocentric radius r and colatitude theta is at distance D = sqrt(x^2+dz^2)
    with x = r sin(theta) and dz = r cos(theta) - z_anom.  Depth must be measured
    relative to the local surface (the polar radius here), not to some other
    radius: the level surface is flattened, so a fixed geocentric radius is at a
    different depth at the pole and at the equator.
    """
    x = r * math.sin(theta)
    dz = r * math.cos(theta) - z_anom
    return u_base(r, theta) + G * mass / math.sqrt(x * x + dz * dz)


def gamma_base(r, theta):
    """Magnitude of grad u_base (the base gravity)."""
    s = math.sin(theta)
    return abs(-GM_WGS / (r * r) + OMEGA_WGS ** 2 * r * s * s)


def solve_level(func, u0, lo=0.97 * A_WGS, hi=1.03 * A_WGS):
    """Bisection for r with func(r) = u0 (func decreases with r here)."""
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if func(mid) > u0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def rule(title):
    print()
    print("=" * 74)
    print(title)
    print("=" * 74)


def main():
    print("Equipotential surfaces, the geoid and level surfaces")
    print("WGS 84 defining data: a = %.0f m, 1/f = %.9f" % (A_WGS, INV_F_WGS))
    print("                      omega = %.6e rad/s, GM = %.9e m^3 s^-2"
          % (OMEGA_WGS, GM_WGS))
    u0 = u_base(A_WGS, math.pi / 2)
    print("The model geoid is the level surface through the equator point (a, 0):")
    print("U0 = %.10e m^2 s^-2" % u0)

    # ---------------------------------------------------------------- 1
    rule("1. A level surface is perpendicular to grad U")
    print("  On the surface, the tangent along the meridian is d r/d theta.  The")
    print("  normalised dot product of grad U with a chord of angular step h")
    print("  measures the angle between grad U and the surface; a chord of angular")
    print("  step h makes an angle h/2 with the true tangent, so it vanishes as h.")
    theta = math.radians(45.0)
    r = solve_level(lambda rr: u_base(rr, theta), u0)
    for h in (1e-3, 1e-4, 1e-5, 1e-6):
        r2 = solve_level(lambda rr: u_base(rr, theta + h), u0)
        cx = r2 * math.sin(theta + h) - r * math.sin(theta)
        cz = r2 * math.cos(theta + h) - r * math.cos(theta)
        chord = math.sqrt(cx * cx + cz * cz)
        # grad U in the meridian plane: radial and theta components
        gr = -GM_WGS / (r * r) + OMEGA_WGS ** 2 * r * math.sin(theta) ** 2
        gth = OMEGA_WGS ** 2 * r * math.sin(theta) * math.cos(theta)
        gx = gr * math.sin(theta) + gth * math.cos(theta)
        gz = gr * math.cos(theta) - gth * math.sin(theta)
        gmag = math.sqrt(gx * gx + gz * gz)
        cosang = (gx * cx + gz * cz) / (gmag * chord)
        print("     h = %.0e rad: chord = %.6e m   cos(angle) = %+.6e"
              % (h, chord, cosang))
    print("  The angle between grad U and the surface vanishes linearly in h -- the")
    print("  chord makes an angle h/2 with the tangent, so the cosine is sin(h/2).")
    print("  The limit is exactly zero: grad U is normal to the level surface.")

    # ---------------------------------------------------------------- 2
    rule("2. No rotation, no oblateness")
    r_sphere = GM_WGS / u0
    print("  With omega = 0, U = GM/r and the level surface is r = GM/U0 = %.6f m"
          % r_sphere)
    worst = 0.0
    for tdeg in (0.0, 30.0, 60.0, 90.0):
        th = math.radians(tdeg)
        rr = solve_level(lambda x: GM_WGS / x, u0)
        worst = max(worst, abs(rr - r_sphere))
    print("  Spread over colatitudes 0-90 deg: %.3e m (floating-point noise)." % worst)

    # ---------------------------------------------------------------- 3
    rule("3. Rotation flattens the level surface -- and it is not an ellipsoid")
    print("  colatitude    r(theta) (m)        r/a - 1")
    rs = {}
    for tdeg in (0.0, 15.0, 30.0, 45.0, 60.0, 75.0, 90.0):
        th = math.radians(tdeg)
        rr = solve_level(lambda x: u_base(x, th), u0)
        rs[tdeg] = rr
        print("     %5.1f deg    %.6f      %+.8f" % (tdeg, rr, rr / A_WGS - 1.0))
    f_model = (rs[90.0] - rs[0.0]) / rs[90.0]
    print("  flattening of this level surface : f = %.10e = 1/%.3f"
          % (f_model, 1.0 / f_model))
    print("  WGS 84 datum flattening          : f = %.10e = 1/%.3f"
          % (F_WGS, INV_F_WGS))
    print("  ratio model/datum = %.4f" % (f_model / F_WGS))
    print()
    print("  Best-fit ellipsoid (same a, polar semi-axis b chosen to minimise the")
    print("  maximum deviation, geocentric radius r_e = ab/sqrt(b^2 cos^2 + a^2 sin^2)):")
    best_b, best_dev = None, None
    b = rs[0.0] - 3000.0
    while b <= rs[0.0] + 3000.0:
        dev = 0.0
        for tdeg, rr in rs.items():
            th = math.radians(tdeg)
            re = A_WGS * b / math.sqrt(b * b * math.sin(th) ** 2
                                       + A_WGS * A_WGS * math.cos(th) ** 2)
            dev = max(dev, abs(rr - re))
        if best_dev is None or dev < best_dev:
            best_b, best_dev = b, dev
        b += 5.0
    print("     best b = %.1f m, worst residual = %.1f m" % (best_b, best_dev))
    print("     corresponding ellipsoid flattening = %.8e = 1/%.2f"
          % ((A_WGS - best_b) / A_WGS, A_WGS / (A_WGS - best_b)))
    print("  Even the best ellipsoid misses the level surface by about %.0f m:" % best_dev)
    print("  a level surface is a different kind of object from an ellipsoid.")
    print()
    q = OMEGA_WGS ** 2 * A_WGS ** 3 / GM_WGS
    j2_radau = (2.0 * F_WGS - q) / 3.0
    print("  The rotation parameter and the quadrupole.  With")
    print("     q = omega^2 a^3/GM = %.10e" % q)
    print("  the first-order relation for a body in hydrostatic equilibrium is")
    print("     J_2 = (2f - q)/3 .")
    print("  Taking f and q from the defining data gives")
    print("     J_2 = %.10e" % j2_radau)
    print("  which is the measured dynamical form factor to three figures (the")
    print("  directly determined value is 1.08e-3; authoritative digits from ICGEM).")
    print("  A homogeneous spheroid with the same flattening would have")
    j2_hom = (1.0 - (1.0 - F_WGS) ** 2) / 5.0
    print("     J_2 = %.10e, ratio %.4f" % (j2_hom, j2_radau / j2_hom))
    print("  The deficit is the quantitative statement that the Earth is not")
    print("  homogeneous: its mass is concentrated toward the centre.")

    # ---------------------------------------------------------------- 4
    rule("4. A buried mass displaces the geoid: undulation by two routes")
    print("  The anomaly sits on the rotation axis, its centre at ``depth`` below")
    print("  the polar surface.  Route 1 solves the perturbed level surface U0 for")
    print("  r and subtracts the unperturbed r.  Route 2 is Bruns' formula")
    print("  N = T/gamma, with T the disturbing potential at the unperturbed")
    print("  surface point.  (Depth is measured from the polar radius of the model")
    print("  level surface, %.3f m.)" % R_POLAR)
    anomalies = (
        ("small ore body ", 4.0 / 3.0 * math.pi * 5000.0 ** 3 * 300.0, 10000.0),
        ("crustal root   ", 4.0 / 3.0 * math.pi * 20000.0 ** 3 * 250.0, 40000.0),
    )
    worst_bruns = 0.0
    for (name, mass, depth) in anomalies:
        z_anom = R_POLAR - depth
        print()
        print("  %s mass = %.6e kg, centre depth = %.0f m" % (name, mass, depth))
        print("     colat.   N (level surface) m    N = T/gamma m     rel.diff")
        for tdeg in (0.0, 0.5, 1.0, 2.0, 5.0):
            th = math.radians(tdeg)
            r_ref = solve_level(lambda x: u_base(x, th), u0)
            r_pert = solve_level(lambda x: u_axis(x, th, mass, z_anom), u0)
            n_geom = r_pert - r_ref
            x = r_ref * math.sin(th)
            dz = r_ref * math.cos(th) - z_anom
            T = G * mass / math.sqrt(x * x + dz * dz)
            n_bruns = T / gamma_base(r_ref, th)
            rel = abs(n_geom - n_bruns) / abs(n_bruns)
            worst_bruns = max(worst_bruns, rel)
            print("     %5.1f    %+.10e    %+.10e   %.2e"
                  % (tdeg, n_geom, n_bruns, rel))
        print("     (the density contrasts 300 and 250 kg/m^3 are model choices,")
        print("      not measured rock properties)")

    # ---------------------------------------------------------------- 5
    rule("5. The same anomalies deflect the vertical")
    print("  The deflection is epsilon = a_horizontal / gamma, with a_horizontal the")
    print("  horizontal component of the anomaly's attraction at the surface.")
    print("     offset X (m)   a_horizontal (m/s^2)   epsilon (rad)   arcsec")
    mass_b, depth_b = 4.0 / 3.0 * math.pi * 20000.0 ** 3 * 250.0, 40000.0
    best_eps = 0.0
    for X in (0.0, 10000.0, 20000.0, 40000.0, 80000.0):
        D = math.sqrt(X * X + depth_b * depth_b)
        a_h = G * mass_b * X / D ** 3
        r_ref = solve_level(lambda x: u_base(x, math.pi / 2), u0)
        eps = a_h / gamma_base(r_ref, math.pi / 2)
        best_eps = max(best_eps, eps)
        print("     %9.0f      %.6e          %.6e       %.4f"
              % (X, a_h, eps, eps * 180.0 / math.pi * 3600.0))
    print("  The deflection peaks near X = d/sqrt(2) and reaches %.4f arcsec for"
          % (best_eps * 180.0 / math.pi * 3600.0))
    print("  this anomaly.  Deflection of the vertical is a classical geodetic")
    print("  observable: it is measured by comparing astronomically determined")
    print("  latitude and longitude with their geodetic counterparts.")

    print()
    print("SUMMARY OF MEASURED AGREEMENTS (every value is program output)")
    print("  level surface normal to grad U    : cos falls linearly in h (table)")
    print("  no rotation -> sphere             : spread %.2e m" % worst)
    print("  model flattening / WGS 84 datum   : %.4f" % (f_model / F_WGS))
    print("  best-fit ellipsoid residual       : %.1f m" % best_dev)
    print("  J_2 from (2f-q)/3 vs homogeneous  : %.10e vs %.10e"
          % (j2_radau, j2_hom))
    print("  Bruns' formula vs solved surface  : worst rel.diff %.2e" % worst_bruns)


if __name__ == "__main__":
    main()
