#!/usr/bin/env python3
"""Height systems: geopotential numbers, orthometric, dynamic and normal heights,
and what happens when gravity is ignored in levelling.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python height_systems_demo.py

The normal-gravity formula is the standard closed-form Somigliana expression
evaluated with WGS 84 defining constants (gamma_e and k are WGS 84 defining
values, quoted exactly).  Every levelling line, gravity reading, loop and geoid
undulation in this module is a SYNTHETIC teaching value.

Contents
--------
1. Normal gravity on the WGS 84 ellipsoid.
2. A levelling line: geopotential number and the four height systems.
3. The error from ignoring gravity, quantified.
4. Loop closure from measurement error: raw misclosure and adjustment.
5. One station, several legitimate heights.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

GAMMA_E = 9.7803253359        # m/s^2, WGS 84 normal gravity at the equator
K_WGS84 = 0.00193185265241    # dimensionless, WGS 84
A_WGS84 = 6378137.0           # m
F_WGS84 = 1.0 / 298.257223563
E2_WGS84 = 2.0 * F_WGS84 - F_WGS84 ** 2
MGAL = 1.0e-5                 # m/s^2 per mGal


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def gamma(phi_deg):
    """Somigliana normal gravity on the WGS 84 ellipsoid, m/s^2."""
    s2 = np.sin(np.radians(phi_deg)) ** 2
    return GAMMA_E * (1.0 + K_WGS84 * s2) / np.sqrt(1.0 - E2_WGS84 * s2)


def main():
    section("1. Normal gravity on the WGS 84 ellipsoid")
    print("   latitude (deg)   gamma (m/s^2)   gamma - gamma_eq (mGal)")
    for phi in (0.0, 15.0, 30.0, 45.0, 60.0, 75.0, 90.0):
        g = gamma(phi)
        print(f"  {phi:15.1f}   {g:13.6f}   {(g - gamma(0.0)) / MGAL:18.2f}")
    gp, ge = gamma(90.0), gamma(0.0)
    print(f"  gamma_pole / gamma_equator = {gp / ge:.9f}")
    print(f"  the polar value exceeds the equatorial by "
          f"{(gp - ge) / MGAL:.0f} mGal, about 0.53 % of g.")
    print("  Normal gravity is a defined function of latitude on a chosen")
    print("  ellipsoid.  It is not a measurement, and it is not real gravity.")

    section("2. A levelling line: geopotential number and height systems")
    n = 101
    s = np.linspace(0.0, 100.0e3, n)                    # 100 km line
    phi = 45.0 + s / 111.0e3 * 0.90                     # latitude rises north
    hline = 45.0 * s / s[-1] + 6.0 * np.sin(2.0 * np.pi * s / 40.0e3)
    dh = np.diff(hline)
    anomaly = -40.0 * MGAL * np.exp(-((s - 60.0e3) / 25.0e3) ** 2)
    g_mid = gamma(0.5 * (phi[:-1] + phi[1:])) + 0.5 * (anomaly[:-1] + anomaly[1:])
    C = np.concatenate([[0.0], np.cumsum(g_mid * dh)])   # m^2/s^2
    gamma45 = gamma(45.0)
    g_bar = np.mean(np.concatenate([[g_mid[0]], g_mid]))
    H_ortho = C / g_bar
    H_dyn = C / gamma45
    H_norm = C / gamma(phi)
    H_naive = np.concatenate([[0.0], np.cumsum(dh)])
    print(f"line: {s[-1] / 1000:.0f} km, latitude {phi[0]:.2f} to {phi[-1]:.2f} "
          "degrees")
    print(f"height profile: rises {hline[-1] - hline[0]:.2f} m with a "
          f"+/-{6.0:.0f} m undulation (SYNTHETIC)")
    print(f"SYNTHETIC gravity anomaly in the middle of the line: "
          f"{anomaly.min() / MGAL:.0f} mGal")
    hh = hline[-1] - hline[0]
    print(f"  geopotential number at the far end  C = {C[-1]:.6f} m^2/s^2")
    print(f"  mean gravity along the line         = {g_bar:.6f} m/s^2")
    print(f"  orthometric  H = C / g_bar          = {H_ortho[-1]:.6f} m")
    print(f"  dynamic      H = C / gamma_45       = {H_dyn[-1]:.6f} m")
    print(f"  normal       H = C / gamma(phi)     = {H_norm[-1]:.6f} m")
    print(f"  unweighted   H = sum of increments  = {H_naive[-1]:.6f} m")
    print(f"  dynamic - orthometric  = {(H_dyn[-1] - H_ortho[-1]) * 1000:+.2f} mm")
    print(f"  normal  - orthometric  = {(H_norm[-1] - H_ortho[-1]) * 1000:+.2f} mm")
    print(f"  unweighted - orthometric = "
          f"{(H_naive[-1] - H_ortho[-1]) * 1000:+.2f} mm")
    print(f"  (the height difference itself is {hh:.3f} m)")
    print("  Same physics, four conventions, and four different numbers: the spread")
    print("  is 0.02 to 2.5 mm of a 45 m height difference, that is 0.5 to 56 parts")
    print("  per million.  Scale the relief to 1000 m and the same spread becomes")
    print("  0.5 to 56 mm; over a 4 km mountain pass it reaches 2 to 220 mm.  The")
    print("  height system must be named whenever a height is quoted, because two")
    print("  systems differ by more than most of the effects one is trying to see.")

    section("3. The error from ignoring gravity")
    print("  The plain sum of increments differs from the orthometric height by")
    print("       (1/g_bar) * sum over setups of (g_i - g_bar) * dh_i,")
    print("  so it is a COVARIANCE between the gravity variation and the height")
    print("  gain, not the size of the gravity variation as such.")
    for label, prof in (("latitude variation, steady climb",
                         45.0 * s / s[-1] + 6.0 * np.sin(2.0 * np.pi * s / 40.0e3)),
                        ("same, but the climb is confined to the anomaly",
                         45.0 * np.clip((s - 40.0e3) / 40.0e3, 0.0, 1.0))):
        d = np.diff(prof)
        cc = np.cumsum(g_mid * d)
        gb = np.mean(np.concatenate([[g_mid[0]], g_mid]))
        err = (np.sum(d) - cc[-1] / gb) * 1000.0
        print(f"    {label:44s}: error {err:+8.3f} mm on a "
              f"{prof[-1] - prof[0]:.1f} m rise")
    print("  The first case cancels because the gravity excess is antisymmetric")
    print("  about the midpoint while the height gain is not: a first-order effect")
    print("  vanishes in a symmetric example and reappears the moment the terrain")
    print("  and the gravity field stop being symmetric.  Both numbers are small")
    print("  because this SYNTHETIC line has only 45 m of relief and a 40 mGal")
    print("  anomaly; with 1 km of relief against the same anomaly the covariance")
    print("  term reaches about 40 mm, and it is systematic.  That is why levelling")
    print("  is weighted by measured gravity always, not only in mountains.")

    section("4. Loop closure from measurement error")
    steps = 60
    sigma_setup = 0.0005                      # m per setup (SYNTHETIC)
    systematic = 0.0001                       # m per setup, a collimation-like tilt
    k = np.arange(steps)
    true_inc = 0.75 * np.sin(2.0 * np.pi * k / steps)      # sums to zero exactly
    obs = true_inc + systematic + sigma_setup * RNG.standard_normal(steps)
    raw = obs.sum()
    print(f"SYNTHETIC loop of {steps} setups whose true increments sum to zero")
    print(f"  (a sinusoid over one period), plus {sigma_setup * 1000:.2f} mm random")
    print(f"  per setup and a systematic {systematic * 1000:.2f} mm per setup")
    print(f"  true closing value                  = {true_inc.sum() * 1e3:+.6f} mm")
    print(f"  raw misclosure                      = {raw * 1000:+.3f} mm")
    print(f"  expected from noise, 1 sigma        = "
          f"{sigma_setup * np.sqrt(steps) * 1000:.3f} mm")
    print(f"  expected from the systematic part   = "
          f"{systematic * steps * 1000:.3f} mm")
    print(f"  systematic part estimated from the closure = "
          f"{raw / steps * 1e3:.3f} mm per setup")
    adjusted = obs - raw / steps
    print(f"  after distributing the misclosure   = {adjusted.sum() * 1e3:+.6f} mm")
    print(f"  residual scatter about the trend    = "
          f"{np.std(obs - true_inc - raw / steps) * 1000:.3f} mm per setup")
    print("  A misclosure that grows in proportion to the number of setups is")
    print("  systematic -- an instrument or procedure effect -- and repeating the")
    print("  loop does not average it away.  A misclosure that grows as the square")
    print("  root of the number of setups is random and does.")

    section("5. One station, several legitimate heights")
    H_o, Nund, C_station = 250.000, 44.500, 250.0 * 9.8062
    print(f"  orthometric height H         = {H_o:.3f} m")
    print(f"  geoid undulation N           = {Nund:.3f} m (SYNTHETIC)")
    print(f"  ellipsoidal height h = H + N = {H_o + Nund:.3f} m")
    print(f"  dynamic height C / gamma_45  = {C_station / gamma45:.3f} m")
    print(f"  normal height  C / gamma(45) = {C_station / gamma(45.0):.3f} m")
    print("  Four defensible numbers for one point.  They agree here because the")
    print("  synthetic C was built from normal gravity at 45 degrees; give the")
    print("  station a real gravity field and they separate by the amounts measured")
    print("  in section 2, in proportion to the height.  A height reference frame")
    print("  must therefore name the system its numbers belong to.")


if __name__ == "__main__":
    main()
