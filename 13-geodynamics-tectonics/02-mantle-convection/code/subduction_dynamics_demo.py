#!/usr/bin/env python3
"""Subduction dynamics: slab pull, sinking speed, bending, and slab heating.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python subduction_dynamics_demo.py

Everything here is SYNTHETIC: the slab thermal model, plate age, viscosity,
plate length and rheology are chosen teaching values, not measurements of any
real subduction zone.  Print-only; no figures.

Contents
--------
1. Slab thermal buoyancy and slab pull per unit trench length.
2. Sinking speed from the balance of slab buoyancy and mantle drag.
3. Bending: the bending stiffness, the bending length scale and yield curvature.
4. Force inventory: slab pull, ridge push, basal drag, and the plate speed.
5. Thermal equilibration depth of a slab.
6. Slab dip, trench migration and what geometry can and cannot be inferred.
"""

import numpy as np
from scipy.special import erf

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC teaching parameters (chosen, not measured) --------------------
G = 9.81               # m/s^2 (standard)
RHO_M = 3300.0         # kg/m^3
RHO_W = 1030.0         # kg/m^3
ALPHA = 3.0e-5         # 1/K
T_M = 1300.0           # K
KAPPA = 1.0e-6         # m^2/s
CP = 1250.0            # J/(kg K)
E_YOUNG = 70.0e9       # Pa
NU = 0.25              # -
ETA_MANTLE = 1.0e21    # Pa s
ETA_ASTH = 1.0e21      # Pa s
D_ASTH = 200.0e3       # m
PLATE_AGE = 100.0      # Myr
SEC_PER_MYR = 3.1557e7 * 1.0e6
YIELD_STRESS = 700.0e6  # Pa  SYNTHETIC yield strength of slab material


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def density_anomaly(z, t):
    """rho(z,t) - rho_m for a cooling half-space, kg/m^3 (positive = dense)."""
    return RHO_M * ALPHA * T_M * (1.0 - erf(z / (2.0 * np.sqrt(KAPPA * t))))


def slab_pull(h, L, t=PLATE_AGE * SEC_PER_MYR):
    """Slab pull per unit trench length, N/m.

    F = g L * integral(drho dy), with drho(y) the density anomaly across the
    slab; for a thin slab the result is independent of where the slab is.
    """
    y = np.linspace(0.0, h, 200001)
    integral = np.trapezoid(density_anomaly(y, t), y)
    return G * L * integral, integral


def flexural_rigidity(Te):
    return E_YOUNG * Te ** 3 / (12.0 * (1.0 - NU ** 2))


def main():
    section("1. Slab thermal buoyancy and slab pull")
    h = 100.0e3
    L = 600.0e3
    F_sp, integral = slab_pull(h, L)
    print(f"  SYNTHETIC slab: age {PLATE_AGE:.0f} Myr, thickness "
          f"{h / 1e3:.0f} km, down-dip length {L / 1e3:.0f} km")
    print(f"  density anomaly integral across the slab = {integral:.4e} kg/m^2")
    print(f"  mean density anomaly = {integral / h:.2f} kg/m^3")
    print(f"  slab pull per unit trench length F = g L integral = {F_sp:.4e} N/m "
          f"= {F_sp / 1e12:.2f} TN/m")
    print("  a slab is dense because it is cold; the force is set by the integral of")
    print("  rho alpha (T_m - T) through its thickness, not by its mass.")
    print("   slab thickness (km)   F (TN/m)")
    for hk in (50.0, 75.0, 100.0):
        Fh, _ = slab_pull(hk * 1e3, L)
        print(f"   {hk:18.0f}   {Fh / 1e12:9.2f}")

    section("2. Sinking speed from the balance of buoyancy and drag")
    print("  the slab is dragged on both faces over a distance h:")
    print("  buoyancy rho_m' g h per unit area balanced by eta u/h on each side,")
    print("  giving u = drho_eff g h^2 / (2 eta).")
    drho_eff = integral / h
    for eta in (1.0e20, 1.0e21, 1.0e22):
        u = drho_eff * G * h ** 2 / (2.0 * eta)
        print(f"   eta = {eta:.0e} Pa s: u = {u:.4e} m/s = "
              f"{u * 1e3 * 3.1557e7:.2f} mm/yr, descent time to 660 km = "
              f"{660.0e3 / u / SEC_PER_MYR:.1f} Myr")
    u = drho_eff * G * h ** 2 / (2.0 * ETA_MANTLE)
    print("  the reference viscosity gives a few tens to a hundred mm/yr, of the")
    print("  same order as observed plate and rollback speeds.  The coefficient is")
    print("  crude (a plane drag law, one viscosity, no pressure- and")
    print("  temperature-dependent rheology), so the agreement is a consistency")
    print("  check, not a measurement.")

    section("3. Bending: stiffness, bending length and the elastic core")
    Te, h = 30.0e3, 100.0e3
    D = flexural_rigidity(Te)
    q = drho_eff * G * h
    ell = (2.0 * D / q) ** (1.0 / 3.0)
    print(f"  SYNTHETIC slab: E = {E_YOUNG / 1e9:.0f} GPa, nu = {NU:.2f}, "
          f"Te = {Te / 1e3:.0f} km")
    print(f"  flexural rigidity D = E Te^3/(12(1-nu^2)) = {D:.4e} N m")
    print(f"  buoyancy per unit area q = drho g h = {q:.4e} Pa")
    print("  a bending length follows from balancing the bending moment D/l against")
    print("  the buoyancy torque q l^2/2 available over that length:")
    print(f"    l_b = (2 D/q)^(1/3) = {ell / 1e3:.1f} km")
    print(f"  check: D/l = {D / ell:.4e} N and q l^2/2 = {q * ell ** 2 / 2:.4e} N m")
    print("  the bending stress at that radius is E (h/2)/l_b =")
    sigma_b = E_YOUNG * (h / 2.0) / ell
    print(f"    {sigma_b:.4e} Pa = {sigma_b / 1e6:.0f} MPa, far above any plausible")
    print(f"  yield strength ({YIELD_STRESS / 1e6:.0f} MPa here).  A 100 km elastic slab")
    print("  therefore cannot bend at all at geological radii: bending is confined")
    print("  to a thin yielding core.  Solving sigma_y = E y/R for the core half-width:")
    print("   curvature radius R (km)   elastic core thickness (km)")
    for R_km in (100.0, 300.0, 1000.0):
        R = R_km * 1e3
        h_el = 2.0 * YIELD_STRESS * R / E_YOUNG
        print(f"   {R_km:22.0f}   {h_el / 1e3:26.1f}")
    print("  the elastic thickness that flexes in a subduction zone is a few km,")
    print("  not a hundred: the slab's strength is a thin outer shell, and the rest")
    print("  deforms plastically or viscously.")

    section("4. Force inventory and the plate speed")
    ridge = 4.11e12       # from the module 13-01-04 demonstration (SYNTHETIC)
    print(f"  slab pull  (this demo)      = {F_sp / 1e12:.2f} TN/m")
    print(f"  ridge push (module 13-01-04) = {ridge / 1e12:.2f} TN/m")
    F_net = F_sp + ridge
    u_plate = F_net * D_ASTH / (ETA_ASTH * 5000.0e3)
    print(f"  net driving force = {F_net / 1e12:.2f} TN/m (both act away from the")
    print("  ridge, so they add)")
    print(f"  compensating basal drag over a 5000 km plate, eta = {ETA_ASTH:.0e} Pa s,")
    print(f"  channel thickness {D_ASTH / 1e3:.0f} km gives u = {u_plate:.4e} m/s = "
          f"{u_plate * 1e3 * 3.1557e7:.1f} mm/yr")
    print("  this is not a prediction of plate speed: viscosity and channel")
    print("  thickness are chosen.  It shows the force balance closes at the right")
    print("  order of magnitude, which is why plate speed correlates with the")
    print("  length of subducting slab attached to a plate.")

    section("5. Thermal equilibration depth of a slab")
    print("  the slab's thermal anomaly diffuses away on h^2/(4 kappa):")
    t_eq = (h / 2.0) ** 2 / KAPPA
    print(f"  t_eq = {(h / 2) ** 2 / KAPPA / SEC_PER_MYR:.1f} Myr")
    for u_test in (50.0, 100.0):
        u_si = u_test * 1e-3 / 3.1557e7
        print(f"   sinking at {u_test:.0f} mm/yr -> equilibrates after "
              f"{u_si * t_eq / 1e3:.0f} km of descent")
    print("  a fast slab keeps its cold core to the transition zone; a slow one")
    print("  warms and loses slab pull as it goes, which is a feedback rather than")
    print("  a fixed property.")

    section("6. Slab dip and trench migration: geometry only")
    print("  pin the slab tip (say at the 660 km discontinuity) and let the trench")
    print("  retreat at v_r.  With a slab segment of down-dip length L, the dip theta")
    print("  satisfies sin(theta) = depth/L, so d(theta)/dt ~ v_r/L in radians per")
    print("  time.  Convergence rate V enters only through L, not directly.")
    L_seg = 800.0e3
    print("   rollback v_r (mm/yr)   dip change (deg/Myr) at L = 800 km")
    for vr in (0.0, 15.0, 30.0):
        vr_si = vr * 1e-3 / 3.1557e7
        rate = vr_si / L_seg * 180.0 / np.pi * (3.1557e13)
        print(f"   {vr:19.0f}   {rate:36.2f}")
    print("  a slab that rolls back steepens with no change in the driving force, so")
    print("  dip alone cannot be inverted for one force: dip rate is a kinematic")
    print("  diagnostic of trench motion, and only part of the force balance.")

    print("\n" + "=" * 72)
    print("All models are SYNTHETIC.  Only g = 9.81 m/s^2 is a standard constant.")
    print("=" * 72)


if __name__ == "__main__":
    main()
