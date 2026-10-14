#!/usr/bin/env python3
"""Aquifer signatures: the Ghyben-Herzberg fresh/salt interface, the ambiguity of
bulk electrical conductivity (Archie), the saturated/unsaturated velocity
contrast from Gassmann fluid substitution, and the gravity effect of a water
table.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python aquifer_signatures_demo.py

Everything is SYNTHETIC.  The fluid densities, Archie exponents, elastic moduli
and porosities below are chosen teaching values, not measurements of any site.
Print-only; no network access.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- Standard constants ------------------------------------------------------
G = 6.67430e-11          # m^3 kg^-1 s^-2, CODATA 2018 (standard constant)
RHO_FRESH = 1000.0       # kg/m^3, chosen teaching value for fresh water
RHO_SALT = 1025.0        # kg/m^3, chosen teaching value for sea water
RHO_BRACKISH = 1010.0    # kg/m^3, chosen teaching value for brackish water

# --- SYNTHETIC rock/fluid model for the Gassmann calculation -----------------
K_MIN = 37.0e9           # Pa, quartz bulk modulus (standard mineral value)
MU_MIN = 44.0e9          # Pa, quartz shear modulus (standard mineral value)
RHO_MIN = 2650.0         # kg/m^3, quartz grain density (standard value)
K_DRY = 1.0e9            # Pa, chosen dry-frame bulk modulus of the teaching rock
MU_DRY = 3.0e9           # Pa, chosen dry-frame shear modulus
PHI = 0.30               # chosen porosity
K_AIR = 1.0e5            # Pa, air bulk modulus (~1 atm, standard value)
K_WATER = 2.2e9          # Pa, water bulk modulus (standard value)
RHO_AIR = 1.2            # kg/m^3
RHO_WATER = 1000.0       # kg/m^3


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def ghyben_herzberg(h_fresh_m, rho_fresh, rho_salt):
    """Depth of a sharp fresh/salt interface below sea level, in metres.

    Hydrostatic equilibrium at the interface requires
    rho_fresh g (h + z) = rho_salt g z, where h is the fresh-water head above
    sea level and z the interface depth below sea level.
    """
    return h_fresh_m * rho_fresh / (rho_salt - rho_fresh)


def archie_conductivity(sigma_w, phi, a=1.0, m=2.0, sw=1.0, n=2.0):
    """Bulk conductivity sigma_b = (sigma_w/a) phi^m S_w^n, in S/m."""
    return (sigma_w / a) * phi ** m * sw ** n


def gassmann_ksat(k_dry, k_min, k_fl, phi):
    """Gassmann saturated bulk modulus, Pa."""
    num = (1.0 - k_dry / k_min) ** 2
    den = phi / k_fl + (1.0 - phi) / k_min - k_dry / k_min ** 2
    return k_dry + num / den


def velocities(k_bulk, mu, rho):
    """P- and S-wave speed in m/s from bulk modulus, shear modulus, density."""
    vp = np.sqrt((k_bulk + 4.0 / 3.0 * mu) / rho)
    vs = np.sqrt(mu / rho)
    return vp, vs


def main():
    section("1. Ghyben-Herzberg: the sharp fresh/salt interface")
    print("z = h_f * rho_f / (rho_s - rho_f)   [hydrostatic equilibrium]")
    for rho_s, name in ((RHO_SALT, "sea water"), (RHO_BRACKISH, "brackish")):
        ratio = rho_s / (rho_s - RHO_FRESH)
        print(f"\n  rho_salt = {rho_s:.0f} kg/m^3 ({name}): "
              f"z/h_f = {ratio:6.1f}  (i.e. z = {ratio:.1f} h_f)")
        for h in (0.5, 1.0, 2.0, 5.0, 10.0):
            print(f"    fresh head h_f = {h:5.1f} m  ->  interface depth "
                  f"z = {ghyben_herzberg(h, RHO_FRESH, rho_s):8.1f} m below sea level")
    print("\n  A 1 m change in fresh-water head moves a sharp interface by "
          f"{RHO_SALT / (RHO_SALT - RHO_FRESH):.0f} m (ratio 40 for sea water).")

    section("2. Archie's law: three knobs, one measured conductivity")
    print("sigma_b = sigma_w * phi^2 (a=1, m=2, S_w=1), in S/m")
    print("\n   sigma_w (S/m)   water type        phi     sigma_b (S/m)")
    for sw_, name in ((0.05, "fresh (low TDS)"), (0.5, "brackish"),
                      (4.0, "saline / sea water")):
        for phi in (0.10, 0.15, 0.20, 0.30):
            sb = archie_conductivity(sw_, phi)
            print(f"   {sw_:11.2f}   {name:16s}  {phi:4.2f}   {sb:11.5f}")
    sb_target = 0.05
    print(f"\n  Target bulk conductivity sigma_b = {sb_target:.3f} S/m is produced by:")
    for sw_, name in ((0.5, "brackish"), (4.0, "saline")):
        phi = np.sqrt(sb_target / sw_)
        print(f"    {name:8s} water (sigma_w = {sw_:4.2f} S/m) at porosity "
              f"phi = {phi:.3f}")
    print("  Both are plausible aquifer porosities: the SAME measurement, two")
    print("  materially different interpretations (brackish/high-phi vs saline/low-phi).")
    sw_part = 0.5
    phi_eq = np.sqrt(sb_target / (4.0 * sw_part ** 2))
    print(f"  Partial saturation adds a third knob: saline water at S_w = "
          f"{sw_part:.1f} (n=2) needs phi = {phi_eq:.3f} for the same sigma_b.")

    section("3. Gassmann fluid substitution: Vp jumps, Vs barely moves")
    print(f"  dry frame: K_dry = {K_DRY/1e9:.1f} GPa, mu_dry = {MU_DRY/1e9:.1f} GPa, "
          f"phi = {PHI:.2f}, rho_grain = {RHO_MIN:.0f} kg/m^3")
    rho_dry = (1.0 - PHI) * RHO_MIN + PHI * RHO_AIR
    rho_sat = (1.0 - PHI) * RHO_MIN + PHI * RHO_WATER
    k_dry_state = gassmann_ksat(K_DRY, K_MIN, K_AIR, PHI)
    k_wet_state = gassmann_ksat(K_DRY, K_MIN, K_WATER, PHI)
    vp_dry, vs_dry = velocities(k_dry_state, MU_DRY, rho_dry)
    vp_sat, vs_sat = velocities(k_wet_state, MU_DRY, rho_sat)
    print(f"  saturated bulk modulus: K(air-filled) = {k_dry_state/1e9:.3f} GPa, "
          f"K(water-filled) = {k_wet_state/1e9:.3f} GPa "
          f"(+{(k_wet_state-k_dry_state)/1e9:.3f} GPa of fluid stiffening)")
    print(f"\n  unsaturated (pores = air):  rho = {rho_dry:7.1f} kg/m^3, "
          f"Vp = {vp_dry:6.0f} m/s,  Vs = {vs_dry:6.0f} m/s")
    print(f"  saturated   (pores = water): rho = {rho_sat:7.1f} kg/m^3, "
          f"Vp = {vp_sat:6.0f} m/s,  Vs = {vs_sat:6.0f} m/s")
    print(f"  bulk density change across the water table = "
          f"{(rho_sat-rho_dry)/rho_dry*100:+6.1f}%")
    print(f"\n  Vp change across the water table = "
          f"{(vp_sat - vp_dry) / vp_dry * 100:+6.1f}%")
    print(f"  Vs change across the water table = "
          f"{(vs_sat - vs_dry) / vs_dry * 100:+6.1f}%")
    print("  Gassmann leaves the SHEAR modulus unchanged, so Vs responds only to")
    print("  the density change: Vp is the saturation indicator, Vs is not.")

    section("4. Gravity effect of a water table (Bouguer slab)")
    d_rho = PHI * (RHO_WATER - RHO_AIR)
    print(f"  density change on saturation: d_rho = phi (rho_w - rho_air) = "
          f"{d_rho:.1f} kg/m^3 = {d_rho/1000:.4f} g/cm^3")
    conv = 2.0 * np.pi * G * 1000.0 / 1.0e-5
    print(f"  slab formula dg = 2*pi*G*d_rho*h  ->  in mGal this is "
          f"{conv:.5f} * d_rho[g/cm^3] * h[m]")
    print("\n   saturated thickness h (m)     dg (mGal)")
    for h in (5.0, 10.0, 20.0, 50.0, 100.0):
        print(f"   {h:23.1f}     {conv * (d_rho / 1000.0) * h:8.3f}")
    print(f"\n  A 5 microGal (= 0.005 mGal) survey noise is exceeded once the")
    print(f"  saturated thickness is about "
          f"{0.005 / (conv * d_rho / 1000.0):.1f} m. Gravity sees the total")
    print("  saturated mass, not the water table depth: it cannot separate a thick")
    print("  poorly saturated layer from a thin fully saturated one.")
    print("\n  All models and data in this module are SYNTHETIC.")


if __name__ == "__main__":
    main()
