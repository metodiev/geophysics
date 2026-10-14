#!/usr/bin/env python3
"""Geophysics for carbon capture and storage monitoring: Gassmann fluid
substitution from brine to CO2 and its seismic signature, the reflectivity
change and polarity flip, the gravity signal of the plume's mass deficit, and
the difference between detecting a plume and quantifying its mass.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python geophysics_carbon_storage_demo.py

Everything is SYNTHETIC.  The rock and fluid properties, the plume geometry and
the instrument noise are chosen teaching values with standard mineral constants
as anchors.  No real storage site, reservoir, plume, instrument or published
monitoring result is used.

Contents
--------
1. Gassmann fluid substitution: brine-filled versus CO2-filled sandstone.
2. The seismic signature: impedance, reflection coefficient and its polarity.
3. The gravity signature of a mass deficit, in microgal.
4. Detection versus quantification: noise, depth amplification and
   non-uniqueness of (density contrast, volume, depth).
5. What a monitoring programme measures and what it must report.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC rock and fluid model (chosen, not measured) ------------------
PHI = 0.25                 # porosity, fraction
K_MIN, MU_MIN = 37.0, 44.0  # GPa, quartz bulk and shear modulus (standard values)
RHO_MIN = 2650.0           # kg/m^3, quartz grain density (standard value)
K_DRY, MU_DRY = 10.0, 8.0  # GPa, chosen dry-frame moduli for the sandstone
K_BRINE, RHO_BRINE = 2.5, 1050.0        # GPa, kg/m^3 (chosen)
K_CO2, RHO_CO2 = 0.05, 700.0            # GPa, kg/m^3, supercritical (chosen)
Z_CAPROCK = 7.0e6          # kg m^-2 s^-1, chosen caprock impedance
G = 6.674e-11              # m^3 kg^-1 s^-2, gravitational constant (standard)
GRAV_NOISE_MGAL = 5.0      # microGal, repeat-survey noise (chosen)


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def gassmann(K_dry, K_min, K_fl, phi):
    """Gassmann saturated bulk modulus (all moduli in the same units)."""
    num = (1.0 - K_dry / K_min) ** 2
    den = phi / K_fl + (1.0 - phi) / K_min - K_dry / K_min ** 2
    return K_dry + num / den


def velocities(K_sat, mu, rho):
    """P- and S-wave speeds from moduli in GPa and density in kg/m^3."""
    vp = np.sqrt((K_sat + 4.0 * mu / 3.0) * 1e9 / rho)
    vs = np.sqrt(mu * 1e9 / rho)
    return vp, vs


def main():
    section("1. Gassmann fluid substitution: brine versus CO2")
    rho_sat_b = (1 - PHI) * RHO_MIN + PHI * RHO_BRINE
    rho_sat_c = (1 - PHI) * RHO_MIN + PHI * RHO_CO2
    K_b = gassmann(K_DRY, K_MIN, K_BRINE, PHI)
    K_c = gassmann(K_DRY, K_MIN, K_CO2, PHI)
    print(f"  SYNTHETIC sandstone: porosity {PHI:.2f}, dry-frame moduli "
          f"{K_DRY:.0f}/{MU_DRY:.0f} GPa")
    print(f"  mineral: K = {K_MIN:.0f} GPa, mu = {MU_MIN:.0f} GPa, "
          f"rho = {RHO_MIN:.0f} kg/m^3")
    print(f"  fluids: brine K = {K_BRINE:.2f} GPa, rho = {RHO_BRINE:.0f}; "
          f"CO2 K = {K_CO2:.2f} GPa, rho = {RHO_CO2:.0f}")
    print("  note the shear modulus is unchanged by the fluid:")
    print(f"    mu = {MU_DRY:.1f} GPa in both cases")
    vp_b, vs_b = velocities(K_b, MU_DRY, rho_sat_b)
    vp_c, vs_c = velocities(K_c, MU_DRY, rho_sat_c)
    print("  quantity            brine-filled     CO2-filled     change")
    print(f"  saturated K (GPa)   {K_b:12.3f}   {K_c:12.3f}   "
          f"{100 * (K_c - K_b) / K_b:+7.1f}%")
    print(f"  density (kg/m^3)    {rho_sat_b:12.1f}   {rho_sat_c:12.1f}   "
          f"{100 * (rho_sat_c - rho_sat_b) / rho_sat_b:+7.1f}%")
    print(f"  vp (m/s)            {vp_b:12.1f}   {vp_c:12.1f}   "
          f"{100 * (vp_c - vp_b) / vp_b:+7.1f}%")
    print(f"  vs (m/s)            {vs_b:12.1f}   {vs_c:12.1f}   "
          f"{100 * (vs_c - vs_b) / vs_b:+7.1f}%")
    print("  The signature is diagnostic: vp falls strongly because the pore")
    print("  fluid becomes far more compressible, vs rises slightly because")
    print("  the density falls while the shear modulus does not, and the")
    print("  combination is unlike almost any other saturation change.")

    section("2. The seismic signature: impedance and polarity")
    Z_b = rho_sat_b * vp_b
    Z_c = rho_sat_c * vp_c
    R_b = (Z_b - Z_CAPROCK) / (Z_b + Z_CAPROCK)
    R_c = (Z_c - Z_CAPROCK) / (Z_c + Z_CAPROCK)
    print(f"  chosen caprock impedance: {Z_CAPROCK:.3e} kg m^-2 s^-1")
    print(f"  reservoir impedance, brine-filled: {Z_b:.4e} kg m^-2 s^-1")
    print(f"  reservoir impedance, CO2-filled  : {Z_c:.4e} kg m^-2 s^-1")
    print(f"  impedance change: {100 * (Z_c - Z_b) / Z_b:+.1f}%")
    print(f"  reflection coefficient (reservoir below caprock):")
    print(f"    brine-filled R = {R_b:+.4f}")
    print(f"    CO2-filled   R = {R_c:+.4f}")
    print(f"    time-lapse change in R = {R_c - R_b:+.4f}")
    print("  The reflection coefficient changes sign.  CO2 in this model turns")
    print("  a weak positive reflection into a negative one: an amplitude")
    print("  change AND a polarity flip, which is far easier to detect than")
    print("  either alone.")

    section("3. The gravity signature of the mass deficit")
    print("  a compact plume modelled as a sphere; mass deficit")
    print("  dm = (rho_CO2 - rho_brine) x volume")
    drho = RHO_CO2 - RHO_BRINE
    print(f"  density contrast = {drho:+.0f} kg/m^3 (CO2 lighter than brine)")
    print("  radius (m)   volume (m^3)   mass deficit (kg)   depth (m)   "
          "dG (microGal)")
    for r in (100.0, 200.0, 300.0):
        vol = 4.0 / 3.0 * np.pi * r ** 3
        dm = drho * vol
        for depth in (1200.0, 1800.0):
            dg = G * dm / depth ** 2          # m/s^2, point-mass approximation
            print(f"  {r:10.0f}   {vol:12.3e}   {dm:17.3e}   {depth:9.0f}   "
                  f"{dg * 1e8:14.1f}")
    print("  The signal is tens of microGal for a compact plume, and it decays")
    print("  as depth squared.  Modern repeat gravimetry resolves a few")
    print(f"  microGal; the repeated-survey noise here is "
          f"{GRAV_NOISE_MGAL:.1f} microGal.")

    section("4. Detection versus quantification")
    vol = 4.0 / 3.0 * np.pi * 200.0 ** 3
    dm = drho * vol
    print("  (a) detection: is the signal above the survey noise?")
    print("      depth (m)   signal (microGal)   signal/noise   detectable?")
    for depth in (800.0, 1200.0, 1800.0, 2500.0, 3500.0):
        dg = abs(G * dm / depth ** 2 * 1e8)
        print(f"      {depth:9.0f}   {-dg:17.1f}   {dg / GRAV_NOISE_MGAL:12.2f}   "
              f"{'yes' if dg > 2 * GRAV_NOISE_MGAL else 'no':>10s}")
    print("  (b) quantification: recovering the mass from the signal")
    print("      the same anomaly is produced by different (volume, depth)")
    print("      combinations.  Fixing the depth at a value that is wrong by")
    print("      10% changes the inferred mass by:")
    d_true = 1500.0
    sig = G * dm / d_true ** 2
    for err in (-0.10, -0.05, 0.05, 0.10):
        d_used = d_true * (1.0 + err)
        dm_inf = sig * d_used ** 2 / G
        print(f"        depth error {100 * err:+5.1f}%  ->  mass error "
              f"{100 * (dm_inf - dm) / dm:+6.1f}%")
    print("  The mass error is twice the depth error, because the signal")
    print("  depends on depth squared.  Detection is a robust statement;")
    print("  quantification inherits every geometric assumption.")
    print("  (c) a leakage case: 1% of the plume mass moved 100 m below the")
    print("      surface contributes a mass deficit of "
          f"{0.01 * abs(dm):.3e} kg")
    dg_leak = G * 0.01 * abs(dm) / 100.0 ** 2 * 1e8
    print(f"      at 100 m depth that is {dg_leak:.1f} microGal: a large but")
    print("      very shallow anomaly, easily confused with near-surface")
    print("      hydrology or instrument drift rather than with a leak.")

    section("5. What a monitoring programme measures and must report")
    print("  measured  : seismic reflection amplitudes and travel times;")
    print("              gravity differences between surveys; microseismic")
    print("              arrivals; well pressures and temperatures.")
    print("  inferred  : the presence of CO2, its saturation, its spatial")
    print("              distribution, and a mass estimate.")
    print("  assumed   : the rock-physics model (Gassmann, its applicability),")
    print("              the caprock properties, the plume geometry, the fluid")
    print("              density at reservoir conditions, and the depth.")
    print("  A monitoring statement must separate detection (robust) from")
    print("  quantification (assumption-laden), and report the geophysical")
    print("  detection threshold alongside the reported mass.  All numbers")
    print("  above are SYNTHETIC.")


if __name__ == "__main__":
    main()
