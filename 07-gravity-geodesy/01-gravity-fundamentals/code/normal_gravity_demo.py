#!/usr/bin/env python3
"""Normal gravity: the reference ellipsoid, the Somigliana closed form derived
from the four WGS84 defining constants, the gravity flattening, Clairaut's
relation, the latitude gradient, and normal gravity at height.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python normal_gravity_demo.py

Everything is SYNTHETIC except the four WGS84 defining constants, which are used
as stated:  a = 6378137 m (exact), f = 1/298.257223563 (exact),
GM = 3.986004418e14 m^3 s^-2 (exact), omega = 7.292115e-5 rad/s (exact).
Every gravity number below is computed from those four numbers.

Contents
--------
1. Ellipsoid parameters derived from the four defining constants.
2. Normal gravity at the equator and the pole from the exact closed form.
3. The Somigliana formula: gamma(latitude) over the globe.
4. Fit of the closed form to the three-term series; coefficients measured.
5. Clairaut's relation beta + f = (5/2) m, and the size of the omitted term.
6. The latitude correction: mGal per km of north-south travel.
7. Normal gravity at height: the free-air gradient and the h^2 term.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

A_WGS84 = 6378137.0                 # m
F_WGS84 = 1.0 / 298.257223563
GM_WGS84 = 3.986004418e14           # m^3 s^-2
OMEGA_WGS84 = 7.292115e-5           # rad/s
M_PER_DEG_LAT = 111320.0            # m, SYNTHETIC round value for the arc length


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def ellipsoid_parameters():
    """Derive the ellipsoid parameters and the closed-form constants."""
    a = A_WGS84
    f = F_WGS84
    b = a * (1.0 - f)
    e2 = f * (2.0 - f)
    ep2 = e2 / (1.0 - e2)                     # second eccentricity squared
    ep = np.sqrt(ep2)
    m = OMEGA_WGS84 ** 2 * a ** 2 * b / GM_WGS84
    q0 = 0.5 * ((1.0 + 3.0 / ep2) * np.arctan(ep) - 3.0 / ep)
    q0p = 3.0 * (1.0 + 1.0 / ep2) * (1.0 - np.arctan(ep) / ep) - 1.0
    gamma_e = GM_WGS84 / (a * b) * (1.0 - m - m * ep * q0p / (6.0 * q0))
    gamma_p = GM_WGS84 / a ** 2 * (1.0 + m * ep * q0p / (3.0 * q0))
    return dict(a=a, f=f, b=b, e2=e2, ep2=ep2, ep=ep, m=m, q0=q0, q0p=q0p,
                gamma_e=gamma_e, gamma_p=gamma_p)


def somigliana(lat_deg, par):
    """Normal gravity on the ellipsoid at geodetic latitude lat_deg, m/s^2."""
    ph = np.radians(lat_deg)
    a, b = par["a"], par["b"]
    ge, gp = par["gamma_e"], par["gamma_p"]
    return (a * ge * np.cos(ph) ** 2 + b * gp * np.sin(ph) ** 2) / np.sqrt(
        a ** 2 * np.cos(ph) ** 2 + b ** 2 * np.sin(ph) ** 2)


def main():
    section("1. Ellipsoid parameters from the four defining constants")
    par = ellipsoid_parameters()
    print(f"  a            = {par['a']:.1f} m          (defining)")
    print(f"  f            = {par['f']:.12f}   (defining)")
    print(f"  GM           = {GM_WGS84:.9e} m^3/s^2 (defining)")
    print(f"  omega        = {OMEGA_WGS84:.8e} rad/s   (defining)")
    print(f"  b = a(1-f)   = {par['b']:.3f} m")
    print(f"  e^2          = {par['e2']:.9e}")
    print(f"  e'^2         = {par['ep2']:.9e}   (second eccentricity squared)")
    print(f"  m = w^2 a^2 b / GM = {par['m']:.9e}")
    print(f"  q0           = {par['q0']:.9e}")
    print(f"  q0'          = {par['q0p']:.9e}")
    print(f"  m e' q0'/(6 q0) = {par['m'] * par['ep'] * par['q0p'] / (6.0 * par['q0']):.9e}")

    section("2. Normal gravity at the equator and the pole (closed form)")
    ge, gp = par["gamma_e"], par["gamma_p"]
    print(f"  gamma_e = GM/(a b) (1 - m - m e' q0'/(6 q0)) = {ge:.9f} m/s^2"
          f" = {ge * 1e5:.4f} mGal")
    print(f"  gamma_p = GM/a^2  (1 + m e' q0'/(3 q0))      = {gp:.9f} m/s^2"
          f" = {gp * 1e5:.4f} mGal")
    beta = (gp - ge) / ge
    print(f"  gravity flattening beta = (gamma_p - gamma_e)/gamma_e = {beta:.9e}")

    section("3. The Somigliana formula: normal gravity versus latitude")
    lats = np.array([0.0, 15.0, 30.0, 45.0, 60.0, 75.0, 90.0])
    vals = np.array([somigliana(lat, par) for lat in lats])
    print("   latitude    gamma (m/s^2)     gamma (mGal)    difference from 45 deg")
    g45 = somigliana(45.0, par)
    for lat, val in zip(lats, vals):
        print(f"   {lat:7.1f}    {val:.9f}    {val * 1e5:12.4f}    {val - g45:+.6f}")
    print(f"  formula: gamma = (a gamma_e cos^2 phi + b gamma_p sin^2 phi) /")
    print(f"           sqrt(a^2 cos^2 phi + b^2 sin^2 phi); at phi = 0 it returns")
    print(f"           gamma_e = {somigliana(0.0, par):.9f} and at phi = 90 deg")
    print(f"           gamma_p = {somigliana(90.0, par):.9f} m/s^2, as it must.")

    section("4. Series fit: gamma = gamma_e (1 + beta sin^2 phi + beta1 sin^4 phi)")
    phi = np.radians(np.linspace(0.0, 90.0, 181))
    y = np.array([somigliana(np.degrees(p), par) for p in phi]) / ge - 1.0
    print("   terms   beta            beta1            max |residual| (mGal)")
    for k in (1, 2, 3, 4):
        design = np.column_stack([np.sin(phi) ** (2 * (i + 1)) for i in range(k)])
        coef, *_ = np.linalg.lstsq(design, y, rcond=None)
        resid = np.max(np.abs(design @ coef - y)) * 1e5
        b1 = f"{coef[1]:.9e}" if k > 1 else "        -        "
        print(f"   {k:5d}   {coef[0]:.9e}   {b1}   {resid:16.6f}")
    print(f"  exact pole-to-equator difference beta = {beta:.9e}")
    print("  MEASURED POINT: the coefficient of sin^2 phi in a two-term fit is")
    print("  5.278987e-3, which is NOT the pole-to-equator difference 5.302441e-3;")
    print("  they differ by 0.44% because the latter is the SUM of all the series")
    print("  coefficients.  A quoted 'gravity coefficient' is meaningless unless the")
    print("  series it belongs to is stated, and the residual is the proof of fit.")

    section("5. Clairaut's relation and the size of the omitted term")
    clairaut = 2.5 * par["m"] - par["f"]
    print(f"  beta                     = {beta:.9e}")
    print(f"  (5/2) m - f              = {clairaut:.9e}")
    print(f"  relative difference      = {(beta - clairaut) / clairaut * 100:+.4f}%")
    print(f"  absolute difference      = {beta - clairaut:+.6e}")
    print("  Clairaut's theorem is a first-order statement in f and m; the residual")
    print("  above is its second-order term, so the relation is verified to the")
    print("  accuracy its derivation claims and not to machine precision.")
    print("\n  The same first-order derivation predicts, with J2 = 2f/3 - m/3:")
    J2 = 2.0 * par["f"] / 3.0 - par["m"] / 3.0
    ge_1 = GM_WGS84 / par["a"] ** 2 * (1.0 + par["f"] - 1.5 * par["m"])
    gp_1 = GM_WGS84 / par["a"] ** 2 * (1.0 + 2.0 * par["f"] - 3.0 * J2)
    print(f"    gamma_e (first order) = {ge_1:.9f} m/s^2 vs closed form "
          f"{ge:.9f} m/s^2, difference {(ge_1 - ge) * 1e5:+.4f} mGal")
    print(f"    gamma_p (first order) = {gp_1:.9f} m/s^2 vs closed form "
          f"{gp:.9f} m/s^2, difference {(gp_1 - gp) * 1e5:+.4f} mGal")
    print("  With J2 = 1.082629821e-3 from the closed form instead of the first-order")
    J2c = par["e2"] / 3.0 * (1.0 - 2.0 * par["m"] * par["ep"] / (15.0 * par["q0"]))
    gp_1c = GM_WGS84 / par["a"] ** 2 * (1.0 + 2.0 * par["f"] - 3.0 * J2c)
    print(f"  estimate ({J2c:.9e}), gamma_p (first order) = {gp_1c:.9f} m/s^2, "
          f"difference {(gp_1c - gp) * 1e5:+.4f} mGal")

    section("6. The latitude correction: mGal per km of north-south travel")
    print("   latitude   dgamma/dphi (mGal/deg)   per km north (mGal/km)")
    for lat in (0.0, 15.0, 30.0, 45.0, 60.0, 75.0):
        h = 1e-4
        d = (somigliana(lat + h, par) - somigliana(lat - h, par)) / (2.0 * h)
        per_km = d * 1e5 / (M_PER_DEG_LAT / 1000.0)      # mGal per deg / (km per deg)
        print(f"   {lat:7.1f}   {d * 1e5:18.4f}   {per_km:18.4f}")
    d45 = (somigliana(45.0 + 1e-4, par) - somigliana(45.0 - 1e-4, par)) / 2e-4
    per_km_45 = d45 * 1e5 / (M_PER_DEG_LAT / 1000.0)
    print(f"  At 45 deg the correction is {per_km_45:.4f} mGal per km.  Because")
    print("  dgamma/dphi is proportional to sin(2 phi), it VANISHES at the equator and")
    print("  at the pole and is LARGEST at 45 deg.  A correction that vanished at")
    print("  45 deg would be the derivative of a sin^2 profile, which is not this")
    print("  function: the measured shape is what settles the question.")

    section("7. Normal gravity at height: free-air gradient and the h^2 term")
    print("   latitude   dgamma/dh (mGal/m)   gamma(1000 m) - gamma(0) (mGal)")
    for lat in (0.0, 45.0, 90.0):
        ph = np.radians(lat)
        g0 = somigliana(lat, par)
        grad = -2.0 * g0 / par["a"] * (
            1.0 + par["f"] + par["m"] - 2.0 * par["f"] * np.sin(ph) ** 2)
        h_m = 1000.0
        factor = (1.0 - 2.0 / par["a"] * (
            1.0 + par["f"] + par["m"] - 2.0 * par["f"] * np.sin(ph) ** 2) * h_m
            + 3.0 * (h_m / par["a"]) ** 2)
        print(f"   {lat:7.1f}   {grad * 1e5:16.4f}   {(g0 * factor - g0) * 1e5:16.4f}")
    ph = np.radians(45.0)
    g0 = somigliana(45.0, par)
    k = 1.0 + par["f"] + par["m"] - 2.0 * par["f"] * np.sin(ph) ** 2
    grad45 = -2.0 * g0 / par["a"] * k
    for h_m in (1000.0, 4000.0):
        factor = 1.0 - 2.0 / par["a"] * k * h_m + 3.0 * (h_m / par["a"]) ** 2
        exact = (g0 * factor - g0) * 1e5
        linear = grad45 * 1e5 * h_m
        print(f"  at 45 deg, h = {h_m:6.0f} m: exact {exact:+9.4f} mGal, "
              f"linear {linear:+9.4f} mGal, difference {exact - linear:+.4f} mGal")
    print("  The h^2 term is +3 h^2/a^2 relative, which is +0.072 mGal at 1 km and")
    print("  +1.157 mGal at 4 km as measured above.  A linear free-air reduction")
    print("  therefore leaves a systematic 1 mGal error at 4 km of elevation.")


if __name__ == "__main__":
    main()
