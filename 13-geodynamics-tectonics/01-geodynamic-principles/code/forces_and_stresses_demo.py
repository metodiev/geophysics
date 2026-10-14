#!/usr/bin/env python3
"""Driving forces, gravitational potential energy and intraplate stress.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python forces_and_stresses_demo.py

Everything here is SYNTHETIC: the thermal model is the classical half-space
cooling model, but all parameters (age, temperature, viscosity, plate length)
are chosen teaching values, and the viscosity is not a measurement.  Print-only.

Contents
--------
1. Half-space cooling: temperature, density and thermal subsidence.
2. Ridge push by direct double integration of the density anomaly.
3. Independence of the answer from the arbitrary compensation depth (a check).
4. Slab pull: the same integral applied to a downgoing slab.
5. Force balance and the implied plate speed.
6. Gravitational potential energy of thickened crust and intraplate stress.
"""

import numpy as np
from scipy.special import erf

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC teaching parameters (chosen, not measured) --------------------
RHO_M = 3300.0         # kg/m^3
RHO_W = 1030.0         # kg/m^3
RHO_C = 2800.0         # kg/m^3
G = 9.81               # m/s^2 (standard)
ALPHA = 3.0e-5         # 1/K
T_M = 1300.0           # K   mantle temperature
KAPPA = 1.0e-6         # m^2/s thermal diffusivity
ETA_ASTH = 1.0e21      # Pa s  SYNTHETIC asthenosphere viscosity
D_ASTH = 200.0e3       # m     SYNTHETIC drag-layer thickness
L_PLATE = 5000.0e3     # m     SYNTHETIC plate length
SEC_PER_MYR = 3.1557e7 * 1.0e6


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def cooling_temperature(z, t, kappa=KAPPA, Tm=T_M):
    """Half-space cooling: T(z,t) = Tm erf(z / (2 sqrt(kappa t))), K."""
    return Tm * erf(z / (2.0 * np.sqrt(kappa * t)))


def density_anomaly(z, t):
    """rho(z,t) - rho_m for a cooling half-space, kg/m^3 (positive = dense)."""
    T = cooling_temperature(z, t)
    return RHO_M * ALPHA * (T_M - T)


def subsidence(t, rho_m=RHO_M, rho_w=RHO_W):
    """Isostatic subsidence of a cooling half-space, m."""
    deficit = RHO_M * ALPHA * T_M * 2.0 * np.sqrt(KAPPA * t / np.pi)
    return deficit / (rho_m - rho_w)


def gpe_difference(rho_a, rho_b, zeta):
    """g * integral zeta (rho_a - rho_b) dzeta, N/m.

    zeta is height above a common compensation depth.  Because both columns are
    isostatically balanced, the first moment of (rho_a - rho_b) vanishes and the
    integral is independent of the chosen compensation depth.
    """
    return G * np.trapezoid(zeta * (rho_a - rho_b), zeta)


def main():
    section("1. Half-space cooling: temperature, density and subsidence")
    print("  SYNTHETIC: Tm = 1300 K, kappa = 1e-6 m^2/s, alpha = 3e-5 1/K")
    print("   age (Myr)   half-space subsidence (m)   depth of 600 K (km)")
    for age in (10.0, 50.0, 100.0):
        t = age * SEC_PER_MYR
        s = subsidence(t)
        # depth at which the cooling plate reaches 600 K (erf(u) = 600/1300)
        lo, hi = 1e-6, 3.0
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            if erf(mid) < 600.0 / T_M:
                lo = mid
            else:
                hi = mid
        u = 0.5 * (lo + hi)
        depth_600 = 2.0 * np.sqrt(KAPPA * t) * u
        print(f"   {age:9.0f}   {s:24.1f}   {depth_600 / 1e3:19.1f}")
    print("  sqrt(t) subsidence and a sqrt(t) thickening boundary layer are the two")
    print("  signatures of conductive cooling of a half-space.")

    section("2. Ridge push by direct double integration")
    t_ref = 100.0 * SEC_PER_MYR
    s = subsidence(t_ref)
    print(f"  SYNTHETIC plate age = 100 Myr -> subsidence s = {s:.1f} m")
    print("  Columns: ridge (uniform rho_m) versus old plate (cold anomaly, with")
    print("  water above the subsided surface).  zeta = height above the common")
    print("  compensation depth; equal mass then fixes the water layer.")
    print("   compensation depth D (km)   ridge push F_RP (N/m)")
    F_list = []
    for D_km in (200.0, 400.0, 800.0):
        D = D_km * 1e3
        zeta = np.linspace(0.0, D, 400001)
        rho_ref = np.full_like(zeta, RHO_M)
        # depth below the OLD plate surface: its surface sits s below the ridge top
        depth = (D - s) - zeta
        rho_old = np.where(depth < 0.0, RHO_W,
                           RHO_M + density_anomaly(np.maximum(depth, 0.0), t_ref))
        F_list.append(gpe_difference(rho_old, rho_ref, zeta))
        print(f"   {D_km:22.0f}   {F_list[-1]:.4e}")
    F = F_list[-1]
    print(f"  ridge push per unit length of ridge: F_RP = {F:.3e} N/m "
          f"= {F / 1e12:.2f} TN/m")
    print(f"  spread over an eightfold change in D = "
          f"{(max(F_list) - min(F_list)) / abs(F):.2e} (isostasy makes it vanish)")

    section("3. Slab pull: the same integral for a downgoing slab")
    t_slab = 100.0 * SEC_PER_MYR
    h_slab = 100.0e3
    L_slab = 600.0e3
    y = np.linspace(0.0, h_slab, 200001)
    drho = density_anomaly(y, t_slab)
    integral = np.trapezoid(drho, y)
    print(f"  SYNTHETIC slab: age {t_slab / SEC_PER_MYR:.0f} Myr, "
          f"thickness {h_slab / 1e3:.0f} km, down-dip length {L_slab / 1e3:.0f} km")
    print(f"  integral of the density anomaly across the slab = {integral:.4e} kg/m^2")
    F_SP = G * L_slab * integral
    F_uniform = G * (RHO_M * ALPHA * T_M / 2.0) * h_slab * L_slab
    print(f"  slab pull F_SP = g L integral(drho dy) = {F_SP:.4e} N/m "
          f"= {F_SP / 1e12:.2f} TN/m")
    print(f"  crude block estimate g (rho_m alpha Tm/2) h L = {F_uniform:.4e} N/m "
          f"= {F_uniform / 1e12:.2f} TN/m")
    print(f"  the block estimate is low by {100 * (1 - F_uniform / F_SP):.1f}%: it")
    print("  replaces the error-function profile by its average.")
    print(f"  ratio |slab pull| / |ridge push| = {abs(F_SP / F):.1f}")

    section("4. Force balance and the implied plate speed")
    F_net = abs(F_SP) + abs(F)
    u = F_net * D_ASTH / (ETA_ASTH * L_PLATE)
    tau = ETA_ASTH * u / D_ASTH
    print(f"  net driving force = |F_SP| + |F_RP| = {F_net:.4e} N/m")
    print(f"  SYNTHETIC drag: eta = {ETA_ASTH:.0e} Pa s over d = "
          f"{D_ASTH / 1e3:.0f} km, plate length {L_PLATE / 1e3:.0f} km")
    print(f"  balancing F_net = eta u L/d gives u = {u:.4e} m/s "
          f"= {u * 1e3 * 3.1557e7:.2f} mm/yr")
    print(f"  basal shear stress tau = eta u/d = {tau:.4e} Pa = {tau / 1e6:.2f} MPa")
    print("  the speed comes out at plate-tectonic values because the driving force")
    print("  and the drag scale the same way; this is a consistency check, not a")
    print("  prediction, since eta is chosen.")

    section("5. Gravitational potential energy of thickened crust")
    h1, h2 = 35.0e3, 70.0e3
    D = 200.0e3
    e = (h2 - h1) * (RHO_M - RHO_C) / RHO_M
    zeta = np.linspace(0.0, D + e, 400001)
    # reference column: crust on top, mantle below, nothing above zeta = D
    rho_ref = np.where(zeta > D, 0.0, np.where(zeta >= D - h1, RHO_C, RHO_M))
    # plateau column: taller by the Airy elevation e, crust h2 thick
    rho_plateau = np.where(zeta >= (D + e) - h2, RHO_C, RHO_M)
    dgpe = gpe_difference(rho_plateau, rho_ref, zeta)
    print(f"  SYNTHETIC columns: normal crust {h1 / 1e3:.0f} km versus plateau "
          f"crust {h2 / 1e3:.0f} km")
    print(f"  Airy elevation of the plateau = {e:.1f} m")
    print(f"  dGPE = {dgpe:.4e} J/m^2 = {dgpe / 1e12:.2f} TN/m")
    d_analytic = (G / 2.0) * (h2 ** 2 - h1 ** 2) * (RHO_M - RHO_C) * RHO_C / RHO_M
    print(f"  analytic check (g/2)(h2^2-h1^2)(rho_m-rho_c) rho_c/rho_m = {d_analytic:.4e}")
    print(f"  relative error of the numerical integral = "
          f"{abs(dgpe - d_analytic) / d_analytic:.2e}")
    stress = dgpe / h2
    print(f"  upper bound on the mean deviatoric stress = dGPE/h2 = "
          f"{stress:.3e} Pa = {stress / 1e6:.1f} MPa")
    print("  an upper bound, not a measured stress: the real distribution is not")
    print("  uniform, and local strength matters.")

    section("6. Force inventory (all per unit length, SYNTHETIC)")
    rows = (("ridge push", F), ("slab pull", F_SP), ("basal drag",
                                                     tau * L_PLATE),
            ("plateau dGPE", dgpe))
    for name, val in rows:
        print(f"  {name:14s} {val:+.4e} N/m = {val / 1e12:+8.2f} TN/m")

    print("\n" + "=" * 72)
    print("All models are SYNTHETIC.  Only g = 9.81 m/s^2 is a standard constant.")
    print("=" * 72)


if __name__ == "__main__":
    main()
