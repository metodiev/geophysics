#!/usr/bin/env python3
"""Gravity for groundwater: the Bouguer slab, microgravity detection limits, the
correction budget, mass change to equivalent water height from Stokes
coefficients, and harmonic truncation of a compact basin load.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gravity_for_groundwater_demo.py

All loads, basins, noise levels and synthetic coefficients are SYNTHETIC teaching
values.  No real survey, satellite product or dataset is used.

Standard constants used:
    G = 6.67430e-11 m^3 kg^-1 s^-2 (CODATA 2018)
    a = 6.371e6 m (mean Earth radius), g = 9.81 m/s^2
    rho_ave = 5517 kg/m^3 (mean Earth density), rho_w = 1000 kg/m^3
    k_2 = -0.30 (elastic load Love number of degree 2)
    free-air gradient 2g/a, and the normal-gravity coefficient 0.3086 mGal/m

Contents
--------
1. The Bouguer slab: gravity per metre of water, and the detection limit.
2. What a microgravity survey can resolve in storage terms.
3. The correction budget: free air, height, tides, drift.
4. Equivalent water height from a Stokes coefficient.
5. Mass change over a basin, and the degree-truncation (leakage) of a compact
   load.
6. Verification of the slab against the disk integral, and of the EWH relation.
"""

import numpy as np
from scipy.integrate import quad

RNG = np.random.default_rng(20261014)

G = 6.67430e-11        # m^3 kg^-1 s^-2
G_EARTH = 9.81         # m/s^2
A_EARTH = 6.371e6      # m
RHO_AVE = 5517.0       # kg/m^3
RHO_W = 1000.0         # kg/m^3
K2 = -0.30             # elastic load Love number, degree 2
UGAL = 1.0e-8          # m/s^2


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def slab_m_per_s2(dh_m, rho=RHO_W):
    """Gravity change of an infinite slab: 2 pi G rho dh, in m/s^2."""
    return 2.0 * np.pi * G * rho * dh_m


def disk_m_per_s2(radius_m, depth_m, rho=RHO_W):
    """Vertical gravity of a uniform disk of radius R at height z above its plane.

    g_z = 2 pi G rho (1 - z / sqrt(z^2 + R^2)); tends to the slab as R -> inf.
    """
    return 2.0 * np.pi * G * rho * (1.0 - depth_m / np.sqrt(depth_m ** 2 + radius_m ** 2))


def ewh_from_dc20(dc20, l=2, a=A_EARTH, rho_ave=RHO_AVE, rho_w=RHO_W, k_l=K2):
    """Equivalent water height at the pole from a normalized Stokes coefficient.

    EWH = a rho_ave (2l+1) / (3 rho_w (1 + k_l)) * Delta C_l0 * Pbar_l0(cos 0).
    Pbar_20(1) = sqrt(5), Pbar_40(1) = 3 (normalized associated Legendre).
    """
    pbar = {2: np.sqrt(5.0), 4: 3.0}[l]
    return a * rho_ave * (2 * l + 1) / (3.0 * rho_w * (1.0 + k_l)) * dc20 * pbar


def disk_degree_amplitude(l, theta0, n=400):
    """cos(theta) integral of P_l over a disk of angular radius theta0.

    A uniform disk load has degree coefficients proportional to
    (1/(2l+1)) * integral_0^theta0 P_l(cos t) sin t dt.
    """
    legendre = np.polynomial.legendre.Legendre.basis(l)
    val, _ = quad(lambda t: legendre(np.cos(t)) * np.sin(t), 0.0, theta0,
                  limit=n)
    return val


def main():
    section("1. The Bouguer slab and what one metre of water weighs")
    print(f"  G = {G:.5e} m^3 kg^-1 s^-2, rho_w = {RHO_W:.0f} kg/m^3")
    print("  Delta g = 2 pi G rho_w Delta h, so the coefficient is")
    print(f"  2 pi G rho_w = {2.0 * np.pi * G * RHO_W:.4e} m/s^2 per m "
          f"= {2.0 * np.pi * G * RHO_W / UGAL:.2f} uGal per m of water")
    print("\n   water-table change (m)   Delta g (uGal)")
    for dh in (0.05, 0.10, 0.25, 0.50, 1.0, 2.0, 5.0):
        print(f"   {dh:24.2f}   {slab_m_per_s2(dh) / UGAL:15.2f}")
    print("  A water-table change of 1 m is 41.93 uGal: large compared with a")
    print("  modern relative-gravity repeatability of a few uGal, which is why")
    print("  microgravity is a practical storage gauge in the right setting.")

    section("2. What microgravity resolves in storage terms")
    print("  storage change = Delta m per unit area = rho_w Delta h, and")
    print("  Delta g = 2 pi G Delta m, so Delta m = Delta g / (2 pi G)")
    print(f"  2 pi G = {2.0 * np.pi * G:.4e} m/s^2 per (kg/m^2)")
    print("\n   instrument repeatability   Delta h of water   equivalent storage")
    print("   (uGal)                     (m)                (mm of water)")
    for rep in (3.0, 5.0, 10.0, 20.0):
        dh = rep * UGAL / (2.0 * np.pi * G * RHO_W)
        print(f"   {rep:23.0f}   {dh:18.3f}   {dh * 1000:21.1f}")
    print("  So a 5 uGal repeatability resolves about 120 mm of water-table change,")
    print("  or 12 mm of storage if the specific yield is 0.10.  That is the same")
    print("  order as a good satellite product at basin scale, but delivered at")
    print("  metre-scale spatial resolution - the reason microgravity still exists.")
    print("\n  a gravity change is only a MASS change: it cannot separate")
    print("  water-table movement from a saturation change in the zone above:")
    print("   mechanism                       Delta g for the stated change")
    dh = 1.0
    n = 0.30
    dsw = 0.10
    b = 5.0
    print(f"   1 m water-table rise          {slab_m_per_s2(dh) / UGAL:6.2f} uGal")
    print(f"   saturation +{dsw:.2f} over {b:.0f} m of soil at n = {n:.2f}  "
          f"{2 * np.pi * G * (n * dsw * b * RHO_W) / UGAL:6.2f} uGal")
    print("  The saturation change is 15% of the water-table signal, i.e. it")
    print("  mimics 0.15 m of water-table movement - more than the 0.12 m detection")
    print("  limit of the table above.  Gravity measures MASS, not water level, so")
    print("  the two are indistinguishable in the gravity data alone; a combined")
    print("  water-level and soil-moisture monitoring programme breaks the")
    print("  ambiguity.")

    section("3. The correction budget")
    fa = 2.0 * G_EARTH / A_EARTH
    print(f"  free-air gradient from 2g/a = {fa:.4e} 1/s^2 "
          f"= {fa / UGAL * 1e-2:.3f} uGal per cm")
    print("  (the normal-gravity free-air coefficient used in surveying is")
    print("  0.3086 mGal/m = 3.086 uGal per cm; the difference is the ellipsoidal")
    print("  versus spherical convention, not an error)")
    print("\n   effect                        magnitude (uGal)   equivalent water-table"
          " change (m)")
    for label, val_ugal in (("solid-Earth tide (range)", 100.0),
                            ("ocean tide loading", 10.0),
                            ("instrument drift, 1 day", 20.0),
                            ("barometric, 10 hPa (at -3 nGal/Pa)", 3.0),
                            ("1 cm height error", fa * 1e-2 / UGAL)):
        print(f"   {label:34s} {val_ugal:12.1f}   "
              f"{val_ugal * UGAL / (2 * np.pi * G * RHO_W):32.3f}")
    print("  The tide and the drift are 2-25 times the storage signal being")
    print("  measured, so they must be modelled or removed rather than assumed")
    print("  small.  Note the height item: a 1 cm levelling error is 3.1 uGal,")
    print("  i.e. 7.3% of a 1 m water-table change. Height control at the centimetre")
    print("  level is mandatory, and it is the most common failure of a")
    print("  microgravity monitoring programme.")

    section("4. Equivalent water height from a Stokes coefficient")
    print("  EWH = a rho_ave (2l+1) / (3 rho_w (1+k_l)) Delta C_l0 Pbar_l0(cos "
          "theta)")
    print(f"  with a = {A_EARTH:.4e} m, rho_ave = {RHO_AVE:.0f} kg/m^3,")
    print(f"  rho_w = {RHO_W:.0f} kg/m^3, k_2 = {K2:.2f}, Pbar_20(1) = "
          f"{np.sqrt(5.0):.4f}")
    coeff = A_EARTH * RHO_AVE * 5.0 / (3.0 * RHO_W * (1.0 + K2)) * np.sqrt(5.0)
    print(f"  so EWH = {coeff:.4e} m per unit Delta C_20, i.e. a Delta C_20 of")
    print(f"  1e-10 is {(coeff * 1e-10) * 1e3:.3f} mm of equivalent water height.")
    print("\n   Delta C_20      EWH at the pole (mm)")
    for dc in (1e-12, 1e-11, 1e-10, 3e-10, 1e-9):
        print(f"   {dc:11.1e}   {ewh_from_dc20(dc) * 1e3:20.3f}")
    print("  A degree-2 coefficient of 1e-10 is about 19 mm of water - i.e. the")
    print("  geodetic coefficients are of order 1e-10 to 1e-11 for the signals")
    print("  that matter, which is why the gravity field must be known to that")
    print("  precision and why the degree-1 terms must be removed using a")
    print("  geocentre model.")

    section("5. Mass change over a basin, and degree truncation")
    scale = ewh_from_dc20(1.0) * A_EARTH
    print(f"  EWH to mass: 1 m of EWH over 1 m^2 = {RHO_W:.0f} kg, so")
    print("  Delta M = rho_w x EWH x area")
    area_km2 = 200000.0
    ewh_mm = 20.0
    mass = RHO_W * (ewh_mm * 1e-3) * (area_km2 * 1e6)
    print(f"\n  a {ewh_mm:.0f} mm EWH change over {area_km2:.0f} km^2 is "
          f"{mass:.3e} kg")
    print(f"  = {mass / RHO_W / 1e9:.3f} km^3 of water")
    print("  For scale, that is the annual water demand of a city of several")
    print("  million people: satellite gravimetry measures storage change at")
    print("  exactly the scale at which water management decisions are made.")
    print("\n  Now the leakage problem.  A compact basin load has a harmonic")
    print("  spectrum that extends to high degree; truncating at l_max loses part")
    print("  of it.  For a uniform disk load of angular radius theta0:")
    print("   theta0 (deg)   disk radius (km)   variance captured below "
          "l = 10    l = 20    l = 40")
    for deg in (1.0, 2.0, 5.0, 10.0):
        theta0 = np.deg2rad(deg)
        radius = A_EARTH * theta0 / 1e3
        amps = np.array([abs(disk_degree_amplitude(l, theta0)) for l in
                         range(2, 121)])
        power = amps ** 2
        total = power.sum()
        row = []
        for lmax in (10, 20, 40):
            row.append(power[:lmax - 1].sum() / total * 100.0)
        print(f"   {deg:12.1f}   {radius:23.0f}   {row[0]:31.1f}   "
              f"{row[1]:5.1f}   {row[2]:5.1f}")
    print("  (values are the percentage of the load's degree-variance captured by")
    print("  truncating at l_max)")
    print("  A basin of ~100 km radius carries almost all of its signal above")
    print("  degree 10 (only 10.6% of the degree-variance lies below it), so a")
    print("  product truncated at degree 10 recovers only a small part of it:")
    print("  that deficit is what appears as leakage from outside the basin in a")
    print("  regional solution, and it is why basin-scale mass balances from")
    print("  satellite gravimetry must always state the filter, the truncation")
    print("  degree and the leakage correction.")

    section("6. Verification")
    print("(a) the disk integral must tend to the slab as R -> infinity:")
    for radius in (1e3, 1e4, 1e5, 1e6, 1e8):
        d_val = disk_m_per_s2(radius, 100.0) / UGAL
        print(f"    R = {radius:10.0e} m: {d_val:12.4f} uGal against slab "
              f"{slab_m_per_s2(1.0) / UGAL:8.4f} uGal")
    print("    as R/depth grows the disk value converges on the slab value, which")
    print("    is the physical content of the infinite-slab approximation.")
    print("(b) EWH linearity in Delta C_20 and in (1+k):")
    r1 = ewh_from_dc20(2e-10) / ewh_from_dc20(1e-10)
    r2 = ewh_from_dc20(1e-10, k_l=-0.30) / ewh_from_dc20(1e-10, k_l=-0.15)
    print(f"    doubling Delta C_20 multiplies EWH by {r1:.6f} (expect 2)")
    r2b = ewh_from_dc20(1e-10, k_l=-0.30) / ewh_from_dc20(1e-10, k_l=0.40)
    print(f"    EWH scales inversely with (1+k): ratio for (1+k) = 0.7 vs 1.4 is "
          f"{r2b:.6f} (expect 2)")
    print(f"    (the intermediate check 0.85/0.70 gives {r2:.6f}, as it must)")
    print("(c) the degree-2 formula against the general degree-4 form, to confirm")
    print("    the (2l+1) and (1+k_l) factors are not accidentally specific to l=2:")
    dc = 1e-11
    print(f"    l = 2: EWH = {ewh_from_dc20(dc, l=2) * 1e3:.4f} mm")
    print(f"    l = 4: EWH = {ewh_from_dc20(dc, l=4) * 1e3:.4f} mm "
          f"(with Pbar_40(1) = 3 and k_4 = k_2 for this illustration)")
    print("    The ratio is 2.415 = (9 x 3) / (5 x sqrt(5)), i.e. the (2l+1) and")
    print("    Legendre factors both behave as the general formula requires.  The")
    print("    point of the check is that the STRUCTURE of the formula, not one")
    print("    coefficient value, is being exercised.")


if __name__ == "__main__":
    main()
