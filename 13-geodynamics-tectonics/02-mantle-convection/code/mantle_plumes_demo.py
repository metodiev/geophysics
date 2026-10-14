#!/usr/bin/env python3
"""Mantle plumes, hotspot tracks and large igneous provinces.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python mantle_plumes_demo.py

Everything here is SYNTHETIC: the plume parameters, the buoyancy flux, the
solidus and the hotspot track are chosen teaching values, not measurements.
Print-only; no figures.

Contents
--------
1. Thermal buoyancy of a plume head and its Stokes rise speed.
2. Conduit flow: cylindrical Poiseuille, volume flux and buoyancy flux.
3. How many plumes of this strength would be needed for the mantle heat loss.
4. Incubation: the one-blob Rayleigh number (buoyancy versus diffusion).
5. Excess temperature, a synthetic melt column, and igneous crustal thickness.
6. Hotspot track kinematics: age-distance, plate speed and a track bend.
7. Sensitivity: how uncertainty in viscosity and excess temperature propagates.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC teaching parameters (chosen, not measured) --------------------
G = 9.81               # m/s^2 (standard)
RHO_M = 3300.0         # kg/m^3
ALPHA = 3.0e-5         # 1/K
CP = 1250.0            # J/(kg K)
KAPPA = 1.0e-6         # m^2/s
ETA_MANTLE = 1.0e21    # Pa s
ETA_CONDUIT = 1.0e19   # Pa s  (low-viscosity plume conduit)
DT_PLUME = 200.0       # K      excess potential temperature
D_MANTLE = 2900.0e3    # m
Q_MANTLE_LOSS = 44.4e12  # W  (SYNTHETIC, matches the module's energy budget)
SEC_PER_YR = 3.1557e7
SEC_PER_MYR = SEC_PER_YR * 1.0e6


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def stokes_speed(drho, a, eta, internal_fraction=0.0):
    """Rise speed of a sphere: 2 drho g a^2/(9 eta) for a rigid sphere.

    internal_fraction = 1 gives the Hadamard-Rybczynski result for a sphere of
    vanishing internal viscosity, 2 drho g a^2/(3 eta).
    """
    return 2.0 * drho * G * a ** 2 / (9.0 * eta) * (1.0 + 2.0 * internal_fraction)


def main():
    section("1. Thermal buoyancy of a plume head and its rise speed")
    drho = RHO_M * ALPHA * DT_PLUME
    print(f"  SYNTHETIC excess temperature dT = {DT_PLUME:.0f} K")
    print(f"  density anomaly drho = rho alpha dT = {drho:.2f} kg/m^3 "
          f"({drho / RHO_M * 100:.2f}% of rho)")
    print("   head radius a (km)   u rigid sphere (m/yr)   u low-viscosity (m/yr)"
          "   rise time 2900 km (Myr)")
    for a_km in (150.0, 250.0, 500.0):
        a = a_km * 1e3
        u_rigid = stokes_speed(drho, a, ETA_MANTLE)
        u_low = stokes_speed(drho, a, ETA_MANTLE, internal_fraction=1.0)
        print(f"   {a_km:18.0f}   {u_rigid * SEC_PER_YR:20.3f}   "
              f"{u_low * SEC_PER_YR:20.3f}   "
              f"{D_MANTLE / u_rigid / SEC_PER_MYR:20.1f}")
    a = 250.0e3
    u = stokes_speed(drho, a, ETA_MANTLE)
    print(f"  a 250 km head rises at {u * SEC_PER_YR:.3f} m/yr, i.e. "
          f"{u * SEC_PER_YR * 1e3:.2f} mm/yr, comparable to plate speeds:")
    print("  plume rise and plate motion are the same order of magnitude because")
    print("  both are Stokes velocities for a few-tens-of-kg/m^3 density anomaly.")

    section("2. Conduit flow, volume flux and buoyancy flux")
    a_c = 50.0e3
    for eta_c in (1.0e18, 1.0e19, 1.0e20):
        u_c = drho * G * a_c ** 2 / (8.0 * eta_c)      # Poiseuille, pipe
        Q = np.pi * a_c ** 2 * u_c                     # m^3/s
        B = drho * G * Q                               # kg/s
        print(f"  conduit radius {a_c / 1e3:.0f} km, eta = {eta_c:.0e} Pa s:")
        print(f"    u = drho g a^2/(8 eta) = {u_c:.4e} m/s = "
              f"{u_c * SEC_PER_YR:.3f} m/yr")
        print(f"    volume flux Q = {Q:.4e} m^3/s")
        print(f"    buoyancy flux B = drho g Q = {B:.4e} kg/s "
              f"= {B / 1e3:.3f} tonnes/s")
    eta_c = ETA_CONDUIT
    u_c = drho * G * a_c ** 2 / (8.0 * eta_c)
    Q = np.pi * a_c ** 2 * u_c
    B = drho * G * Q
    print("  the buoyancy flux is the observable: it is what a hotspot swell")
    print("  records, and it can be inverted for volume flux or excess temperature.")

    section("3. Heat transport by plumes against the mantle heat loss")
    print("  heat carried by a conduit = rho c_p dT Q; Q scales as 1/eta_conduit.")
    print("   eta_conduit (Pa s)   Q (m^3/s)   heat per plume (TW)   plumes needed")
    for eta_c2 in (1.0e18, 1.0e19):
        u2 = drho * G * a_c ** 2 / (8.0 * eta_c2)
        Q2 = np.pi * a_c ** 2 * u2
        q2 = RHO_M * CP * DT_PLUME * Q2
        print(f"   {eta_c2:.0e}   {Q2:11.4e}   {q2 / 1e12:19.4f}   "
              f"{Q_MANTLE_LOSS / q2:14.1f}")
    print(f"  the mantle loses {Q_MANTLE_LOSS / 1e12:.1f} TW (SYNTHETIC); even with")
    print("  the most favourable conduit viscosity it would take hundreds of such")
    print("  conduits to carry it.  Hotspot volcanism is a minor term in the heat")
    print("  budget: the plate-scale flow carries the great majority.")

    section("4. Incubation: buoyancy against thermal diffusion")
    print("  the same Rayleigh number used for a layer applies to a blob of size L:")
    print("  Ra_blob = drho g L^3 / (eta kappa), compared with Ra_c = 657.5")
    for L_km, dl in ((500.0, drho), (1000.0, drho), (1000.0, 30.0)):
        L = L_km * 1e3
        ra = dl * G * L ** 3 / (ETA_MANTLE * KAPPA)
        print(f"   L = {L_km:6.0f} km, drho = {dl:6.2f} kg/m^3: Ra_blob = "
              f"{ra:.3e}  ({ra / 657.51:.2e} x Ra_c)")
    print("  a buoyant blob of a few hundred kilometres and a few tens of kg/m^3")
    print("  is unstable by many orders of magnitude, because L^3 beats eta kappa.")
    print("  Survival against conduction is a separate question: compare the")
    print("  diffusive time L^2/kappa with the advective time L/u.")
    a_head = 250.0e3
    u_head = stokes_speed(drho, a_head, ETA_MANTLE)
    for L_km in (500.0, 1000.0):
        L = L_km * 1e3
        t_d, t_a = L ** 2 / KAPPA, L / u_head
        print(f"   blob L = {L_km:6.0f} km: t_diff = {t_d / SEC_PER_MYR:8.1f} Myr, "
              f"t_adv = {t_a / SEC_PER_MYR:6.2f} Myr, Pe = {t_d / t_a:8.1f}")
    print(f"  conduit radius {a_c / 1e3:.0f} km: t_diff = "
          f"{a_c ** 2 / KAPPA / SEC_PER_MYR:.1f} Myr")
    print("  the blob survives its ascent easily (Pe >> 1); the narrow conduit does")
    print("  not, so a plume must be fed continuously rather than rising as a")
    print("  one-off blob.")

    section("5. Excess temperature, melt column and igneous crust")
    print("  SYNTHETIC linear phase relations: solidus T_s = 1350 + 3 z (K, z in km),")
    print("  liquidus T_l = T_s + 400, on a potential-temperature adiabat that")
    print("  cools with depth as the plume decompresses.")
    z = np.arange(0.0, 120.0, 5.0)                     # km
    T_sol = 1350.0 + 3.0 * z
    T_liq = T_sol + 400.0
    T_plume = 1600.0 - 0.5 * z                          # SYNTHETIC adiabat
    F = np.clip((T_plume - T_sol) / (T_liq - T_sol), 0.0, 1.0)
    print("   z (km)   T_plume (K)   T_solidus (K)   melt fraction F")
    for zi, Tp, Ts, Fi in list(zip(z, T_plume, T_sol, F))[::4]:
        print(f"   {zi:6.0f}   {Tp:11.0f}   {Ts:13.0f}   {Fi:14.3f}")
    dz = z[1] - z[0]
    melt_thickness = np.sum(F > 0.0) * dz
    F_mean = float(np.mean(F[F > 0.0])) if (F > 0).any() else 0.0
    print(f"  the melting column is {melt_thickness:.0f} km deep with mean "
          f"melt fraction {F_mean:.3f}")
    print("  taking a melt-productivity factor of 1.0 (all melt extracted), the")
    print("  igneous crustal thickness is:")
    for factor in (0.5, 1.0):
        print(f"    productivity {factor:.1f}: crust = {melt_thickness * F_mean * factor:.1f} km")

    section("6. Hotspot track kinematics")
    track_km = 3000.0
    age_max_Myr = 60.0
    v = track_km * 1e3 / (age_max_Myr * SEC_PER_MYR)
    print(f"  SYNTHETIC track: {track_km:.0f} km long, oldest volcano "
          f"{age_max_Myr:.0f} Myr old")
    print(f"  plate speed = {v:.4e} m/s = {v * 1e3 * SEC_PER_YR:.1f} mm/yr")
    print("   distance (km)   age (Myr)   (from the same fixed hotspot)")
    for d in (0.0, 750.0, 1500.0, 2250.0, 3000.0):
        print(f"   {d:13.0f}   {d * 1e3 / v / SEC_PER_MYR:9.0f}")
    print("  a change of plate direction at 30 Myr through 40 degrees bends the")
    print("  younger part of the track; the bend angle equals the change of")
    print("  velocity direction only if the hotspot is fixed in the mantle frame.")
    print(f"   bend angle at 30 Myr for a 40 degree change: 40.0 degrees (assumed)")
    print("   the assumption of hotspot fixity is a testable approximation, not a")
    print("   theorem: hotspot motion of even a few mm/yr visibly bends a track.")

    section("7. Sensitivity of the rise speed and the buoyancy flux")
    print("  Monte Carlo over SYNTHETIC uncertainty ranges (9.81 is exact):")
    n = 20000
    dT = DT_PLUME * (1.0 + 0.15 * RNG.standard_normal(n))
    eta = ETA_MANTLE * 10.0 ** (0.5 * RNG.standard_normal(n))
    a_r = 250.0e3 * (1.0 + 0.10 * RNG.standard_normal(n))
    u_mc = stokes_speed(RHO_M * ALPHA * dT, a_r, eta)
    lo, mid, hi = np.percentile(u_mc * SEC_PER_YR, [16.0, 50.0, 84.0])
    print(f"  u = {mid:.3f} m/yr, +{hi - mid:.3f} / -{mid - lo:.3f} (1 sigma)")
    print("  viscosity dominates: an order-of-magnitude spread in eta produces")
    print("  nearly an order-of-magnitude spread in u, so plume speeds are far")
    print("  less constrained than the geometry of a hotspot track.")

    print("\n" + "=" * 72)
    print("All parameters, phase relations and tracks are SYNTHETIC.  Only")
    print("g = 9.81 m/s^2 is a standard constant.")
    print("=" * 72)


if __name__ == "__main__":
    main()
