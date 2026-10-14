#!/usr/bin/env python3
"""Marine gravity and magnetics: the Eoetvoes correction derived from scratch,
the free-air and Bouguer corrections, the geocentric dipole field, and a
magnetic anomaly over a synthetic dipole body.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python marine_gravity_magnetics_demo.py

Everything here is SYNTHETIC.  The densities, dipole moment and body geometry are
chosen teaching values, printed below.  No survey, chart, satellite model or
published anomaly is reproduced.  The geodetic and electromagnetic constants
(G, Omega, R, mu_0, the knot) are standard values with units.

Contents
--------
1. The Eoetvoes correction, derived from Omega, R and the knot.
2. Free-air and Bouguer corrections; a reduced anomaly at two synthetic stations.
3. An error budget for a marine gravity survey.
4. The geocentric dipole field: total intensity and inclination against latitude.
5. A magnetic anomaly over a synthetic dipole body.
6. Verification: the derived Eoetvoes coefficients against the standard form, and
   the dipole field against its closed form.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- Standard constants ------------------------------------------------------
G = 6.674e-11            # m^3 kg^-1 s^-2, gravitational constant
OMEGA = 7.292115e-5      # rad/s, Earth's rotation rate
R_EARTH = 6.371e6        # m, mean Earth radius
G0 = 9.80665             # m/s^2, standard gravity
MU0 = 4.0e-7 * np.pi     # H/m, vacuum permeability (exact: 4 pi e-7)
KNOT = 0.514444          # m/s per knot
MGAL = 1.0e5             # mGal per (m/s^2)

# --- SYNTHETIC survey and model parameters (chosen values) ------------------
DENSITY = 2500.0         # kg/m^3, chosen crustal density for the slab correction
DIPOLE_M = 8.0e22        # A m^2, chosen synthetic geocentric dipole moment
BODY_DEPTH = 3000.0      # m, chosen depth of the magnetic body
BODY_MOMENT = 6.0e10     # A m^2, chosen dipole moment of the body


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def eotvos_coefficients():
    """Derive the two Eoetvoes coefficients in mGal per knot and per knot^2."""
    linear = 2.0 * OMEGA * MGAL * KNOT          # mGal per knot, per unit cos(phi)
    quadratic = MGAL * KNOT ** 2 / R_EARTH      # mGal per knot^2
    return linear, quadratic


def dipole_field(lat_deg, m, r=R_EARTH):
    """Geocentric dipole field magnitude in nT at a given latitude."""
    B0 = MU0 * m / (4.0 * np.pi * r ** 3)
    return B0 * np.sqrt(1.0 + 3.0 * np.sin(np.radians(lat_deg)) ** 2)


def dipole_inclination(lat_deg):
    """tan(I) = 2 tan(latitude) for a centred dipole."""
    return np.degrees(np.arctan(2.0 * np.tan(np.radians(lat_deg))))


def dipole_anomaly(x, d, moment):
    """Vertical-component anomaly of a vertical dipole at depth d, offset x."""
    k = MU0 * moment / (4.0 * np.pi)
    return 1e9 * k * (2.0 * d ** 2 - x ** 2) / (x ** 2 + d ** 2) ** 2.5


def main():
    section("1. The Eoetvoes correction, derived")
    print("  A gravimeter on a moving platform measures the vector sum of gravity")
    print("  and two kinematic accelerations: the change in centrifugal")
    print("  acceleration caused by the platform's eastward motion, and the")
    print("  curvature acceleration V^2/R of the platform's path.")
    print("\n  With V the speed, alpha the heading measured from north, and phi the")
    print("  latitude, the eastward velocity is u = V sin(alpha), and")
    print("    delta g = -[ 2 Omega cos(phi) u + V^2/R ]")
    lin, quad = eotvos_coefficients()
    print(f"\n  linear coefficient: 2 Omega * 1e5 mGal/(m/s^2) * 0.514444 m/s/knot")
    print(f"    = 2({OMEGA:.6e})(1e5)({KNOT:.6f}) = {lin:.4f} mGal per knot")
    print(f"  quadratic coefficient: 1e5 * 0.514444^2 / R")
    print(f"    = 1e5({KNOT:.6f})^2/{R_EARTH:.3e} = {quad:.6f} mGal per knot^2")
    print("\n  so the correction is written in the familiar form")
    print(f"    E = {lin:.3f} V cos(phi) sin(alpha) + {quad:.4f} V^2   [mGal]")
    print("  with V in knots.  Both coefficients are DERIVED here from Omega, R")
    print("  and the knot; nothing was quoted.")
    print("\n   speed (kn)   heading   latitude   E (mGal)")
    for V in (6.0, 10.0):
        for alpha in (0.0, 45.0, 90.0, 180.0, 270.0):
            for phi in (30.0,):
                E = (lin * V * np.cos(np.radians(phi)) * np.sin(np.radians(alpha))
                     + quad * V ** 2)
                print(f"  {V:11.1f}   {alpha:7.0f}   {phi:8.0f}   {E:8.3f}")
    print("\n  The V^2 term is independent of heading and latitude: it is the")
    print("  curvature of the platform's path, and it is always positive (the")
    print("  platform is pushed outward, so it reads LESS gravity).  The linear")
    print("  term vanishes on a north-south heading and reverses between east and")
    print("  west, which is why a survey is usually steered on reciprocal headings")
    print("  so that the Eoetvoes term averages out along a line.")

    section("2. Free-air and Bouguer corrections")
    dgdz = -2.0 * G0 / R_EARTH * MGAL
    print("  Free-air: g falls with height above the reference as")
    print("    dg/dh = -2 g / R = -2(9.80665)/6.371e6 = "
          f"{2.0 * G0 / R_EARTH * MGAL:.5f} mGal/m")
    print("  (the same magnitude applies downward, so a station 100 m BELOW the")
    print("  reference reads HIGHER by that amount times 100).")
    print("\n  Bouguer slab: an infinite slab of density rho and thickness h")
    print("  contributes 2 pi G rho h:")
    for h in (10.0, 50.0, 100.0, 500.0):
        b = 2.0 * np.pi * G * DENSITY * h * MGAL
        print(f"    h = {h:6.1f} m, rho = {DENSITY:.0f} kg/m^3 -> {b:9.4f} mGal")
    print("\n  Worked reduction.  Let the reference value at sea level be")
    print("  g_ref = 981 000.000 mGal and let the underlying crustal anomaly be a")
    print("  synthetic +20.0 mGal.  A seabed station in 1200 m of water then reads")
    h = 1200.0
    g_ref = 981000.000
    anomaly_true = 20.0
    dgdz = -2.0 * G0 / R_EARTH * MGAL
    free_air = -dgdz * h
    bouguer = 2.0 * np.pi * G * (DENSITY - 1030.0) * h * MGAL
    g_obs = g_ref - free_air + anomaly_true
    print(f"    g_obs = g_ref + {dgdz * h:+.4f} mGal (free-air effect) + "
          f"{anomaly_true:+.1f} mGal")
    print(f"          = {g_obs:.4f} mGal")
    print("  Reducing it:")
    fa = g_obs - g_ref + free_air
    print(f"    free-air anomaly  = g_obs - g_ref + {free_air:.4f} = "
          f"{fa:+.4f} mGal   (recovers the crustal signal exactly)")
    print(f"    Bouguer correction (density contrast {DENSITY:.0f} - 1030 kg/m^3)")
    print(f"                      = {bouguer:.4f} mGal")
    print(f"    simple Bouguer anomaly = {fa - bouguer:+.4f} mGal")
    print("  The point of the exercise: the free-air reduction removes the whole")
    print("  of the 1200 m of missing rock and returns the crustal signal, provided")
    print("  the DEPTH is known.  The Bouguer reduction then removes the attraction")
    print("  of the rock between the station and the datum, and it is the quantity")
    print("  that is compared with a model.  Neither correction knows anything about")
    print("  the anomaly; both are arithmetic on geometry and density.")

    section("3. An error budget for a marine gravity survey")
    print("  Terms, in mGal, combined in quadrature.  The Eoetvoes term uses a")
    print("  speed known to 0.1 kn and a heading known to 1 degree on an")
    print("  east-west line at 10 kn, 45 degrees latitude.")
    lin, quad = eotvos_coefficients()
    V, phi = 10.0, 45.0
    e_speed = lin * 0.1 * np.cos(np.radians(phi)) + 2 * quad * V * 0.1
    e_head = lin * V * np.cos(np.radians(phi)) * np.radians(1.0)
    terms = (
        ("gravimeter reading noise", 0.2),
        ("Eoetvoes, speed error 0.1 kn", abs(e_speed)),
        ("Eoetvoes, heading error 1 deg", abs(e_head)),
        ("depth error 0.5 m through the free-air gradient", 0.308 * 0.5),
        ("datum and drift", 0.3),
        ("tide and ocean-loading model", 0.1),
    )
    tot = 0.0
    print("\n   term                                       contribution (mGal)")
    for name, val in terms:
        tot += val ** 2
        print(f"  {name:40s} {val:19.3f}")
    tot = np.sqrt(tot)
    print(f"  {'total (quadrature)':40s} {tot:19.3f}")
    print(f"\n  total = {tot:.3f} mGal.  The Eoetvoes terms dominate: the heading")
    print("  term alone is larger than the instrument noise, which is why a")
    print("  gravimeter on a ship needs a good heading and a modern system on an")
    print("  aircraft needs a GNSS-derived acceleration correction.  The")
    print("  quadrature combination also shows why improving the instrument beyond")
    print(f"  about {np.sqrt(tot ** 2 - 0.2 ** 2):.2f} mGal would buy nothing.")

    section("4. The geocentric dipole field")
    B0 = MU0 * DIPOLE_M / (4.0 * np.pi * R_EARTH ** 3)
    print(f"  chosen synthetic dipole moment m = {DIPOLE_M:.1e} A m^2")
    print(f"  B(r, lat) = (mu0 m / 4 pi R^3) sqrt(1 + 3 sin^2(lat)),")
    print(f"  with the equatorial value mu0 m / (4 pi R^3) = {1e9 * B0:.1f} nT")
    print("\n   latitude (deg)   B (nT)   inclination (deg)")
    for lat in (0.0, 15.0, 30.0, 45.0, 60.0, 75.0, 90.0):
        print(f"  {lat:14.1f}   {1e9 * dipole_field(lat, DIPOLE_M):8.1f}   "
              f"{dipole_inclination(lat):17.2f}")
    print("\n  Three facts that follow from the closed form and are worth checking:")
    print(f"    the polar field is exactly twice the equatorial field "
          f"({1e9 * dipole_field(90.0, DIPOLE_M):.1f} vs "
          f"{1e9 * B0:.1f} nT)")
    print("    the inclination passes through 90 deg at the poles and 0 at the")
    print("    equator, and tan(I) = 2 tan(lat) is the whole 'magnetic latitude'")
    print("    relation -- it is what allows a palaeolatitude to be read from a")
    print("    fossil magnetisation direction, and it is a property of the dipole")
    print("    assumption, not of the field.")
    print("  A real field is not a centred dipole: the non-dipole part is a large")
    print("  fraction of the total, and it is obtained from a spherical-harmonic")
    print("  model rather than from this two-line formula.  Nothing here substitutes")
    print("  for such a model.")

    section("5. A magnetic anomaly over a synthetic dipole body")
    print(f"  a vertical dipole of moment {BODY_MOMENT:.1e} A m^2 at "
          f"{BODY_DEPTH:.0f} m depth; anomaly of the vertical component:")
    print("    Ba(x) = (mu0 m / 4 pi) (2 d^2 - x^2)/(x^2 + d^2)^(5/2)")
    print("\n   offset x (m)   Ba (nT)")
    xs = np.array([-6000.0, -4000.0, -3000.0, -2000.0, -1000.0, 0.0,
                   1000.0, 2000.0, 3000.0, 4000.0, 6000.0])
    prof = dipole_anomaly(xs, BODY_DEPTH, BODY_MOMENT)
    for xi, bi in zip(xs, prof):
        print(f"  {xi:12.0f}   {bi:8.2f}")
    print(f"\n  peak positive anomaly = {prof.max():.2f} nT at x = "
          f"{xs[np.argmax(prof)]:.0f} m")
    print(f"  peak negative anomaly = {prof.min():.2f} nT at x = "
          f"{xs[np.argmin(prof)]:.0f} m")
    print(f"  the zero crossing is at 2d^2 = x^2, i.e. |x| = "
          f"{BODY_DEPTH * np.sqrt(2.0):.0f} m = sqrt(2) d")
    print("\n  A vertical dipole gives a symmetric, bipolar anomaly whose positive")
    print("  lobe sits over the body.  An INCLINED magnetisation rotates and skews")
    print("  that pattern, which is why reduction to the pole -- transforming the")
    print("  anomaly to what it would look like if the field were vertical -- is a")
    print("  standard step, and why it is only valid if the magnetisation direction")
    print("  is known.")

    section("6. Verification")
    print("(a) the derived Eoetvoes coefficients against the standard form")
    lin, quad = eotvos_coefficients()
    print(f"    derived linear coefficient    = {lin:.4f} mGal per knot")
    print("    the conventional coefficient quoted for this correction is 7.503")
    print(f"    difference = {abs(lin - 7.503):.4f} mGal per knot, i.e. "
          f"{100 * abs(lin - 7.503) / 7.503:.3f} per cent")
    print(f"    derived quadratic coefficient = {quad:.6f} mGal per knot^2")
    print("    the conventional coefficient for the quadratic term is 0.004154")
    print(f"    difference = {abs(quad - 0.004154):.6f} mGal per knot^2")
    print("    The agreement to a few parts in 10^4 is limited by the rounded")
    print("    values of Omega, R and the knot used here; the derivation is exact.")
    print("(b) the dipole field against its closed form at two latitudes:")
    for lat in (0.0, 90.0):
        closed = MU0 * DIPOLE_M / (4.0 * np.pi * R_EARTH ** 3) * (
            1.0 if lat == 0.0 else 2.0)
        print(f"    lat = {lat:4.0f}: function = "
              f"{1e9 * dipole_field(lat, DIPOLE_M):.4f} nT, closed form = "
              f"{1e9 * closed:.4f} nT")
    print("(c) unit check of the Eoetvoes term: [2 Omega u] has units")
    print("    (1/s)(m/s) = m/s^2, a gravitational acceleration.  ok")
    print("(d) symmetry of the dipole anomaly: Ba(-x) = Ba(x) for a vertical")
    print(f"    dipole.  Check: Ba(1000) = {dipole_anomaly(1000.0, BODY_DEPTH, BODY_MOMENT):.6f} nT,")
    print(f"    Ba(-1000) = {dipole_anomaly(-1000.0, BODY_DEPTH, BODY_MOMENT):.6f} nT.  ok")


if __name__ == "__main__":
    main()
