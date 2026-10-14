#!/usr/bin/env python3
"""Gas hydrates: the gas yield of structure-I clathrate, the base of the hydrate
stability zone, velocity-to-saturation inversion with two competing rock-physics
models, and the resulting resource estimate.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gas_hydrates_demo.py

Everything here is SYNTHETIC.  The phase boundary, the rock-physics models and the
reservoir geometry are teaching models with the stated model constants.  No real
field, well, basin, hydrate deposit or cruise is referenced, and no number is
quoted from a published measurement.

Contents
--------
1. Structure-I stoichiometry: gas yield per cubic metre of hydrate, derived.
2. The base of the hydrate stability zone from a stated phase-boundary model and
   a conductive geotherm; sensitivity to seafloor temperature and gradient.
3. Velocity versus hydrate saturation for a pore-filling model and a
   cementation model, the inversion of one observed velocity, and the
   (porosity, saturation) trade-off.
4. Gas in place and its sensitivity to the parameters that are not measured.
5. Worked examples used in the lesson.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- standard and model constants -------------------------------------------
R_GAS = 8.314            # J/(mol K)
M_CH4 = 16.043e-3        # kg/mol
M_H2O = 18.015e-3        # kg/mol
N_WATER_S1 = 46.0        # water molecules per structure-I unit cell (ideal)
N_METHANE_S1 = 8.0       # methane molecules at full occupancy
RHO_HYDRATE = 900.0      # kg/m^3, model value for structure-I methane hydrate
V_MOLAR_STP = 22.414e-3  # m^3/mol at 273.15 K, 101.325 kPa (standard)
RHO_W_GEO = 1028.0       # kg/m^3, seawater for the pressure profile
G = 9.81                 # m/s^2

# phase-boundary teaching model:  ln(p/p_ref) = -(dH/R)(1/T - 1/T_ref)
A_CLAPEYRON = 6516.0     # K, i.e. dH/R with dH = 54.2 kJ/mol (model value)
T_REF, P_REF = 273.15, 2.60e6   # K, Pa  (model reference point)

# rock-physics end-members (model constants)
K_QUARTZ, G_QUARTZ, RHO_QUARTZ = 36.0e9, 45.0e9, 2650.0
K_WATER, RHO_W = 2.2e9, 1030.0
K_HYDRATE, G_HYDRATE, RHO_HYDRATE_EL = 7.9e9, 3.3e9, 920.0
PHI_REF, KDRY_REF, GDRY_REF = 0.35, 1.0e9, 0.6e9
PHI_SENS = 0.20          # fractional change of the dry moduli per unit porosity


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def gas_yield_per_m3(occupancy=1.0, rho_h=RHO_HYDRATE):
    """Gas volume at STP released by 1 m^3 of structure-I methane hydrate."""
    n_ch4 = occupancy * N_METHANE_S1
    mass_ch4 = n_ch4 * M_CH4
    mass_water = N_WATER_S1 * M_H2O
    mass_fraction = mass_ch4 / (mass_ch4 + mass_water)
    m3_gas_per_kg = 1.0 / M_CH4 * V_MOLAR_STP
    return rho_h * mass_fraction * m3_gas_per_kg, mass_fraction


def p_equilibrium(T_K):
    """Hydrate dissociation pressure in Pa from the Clausius-Clapeyron model."""
    return P_REF * np.exp(-A_CLAPEYRON * (1.0 / T_K - 1.0 / T_REF))


def depth_base_hsz(T_surf_C, gradient_C_per_km, water_depth_m, dz=0.5):
    """Depth below the seafloor (m) where the geotherm crosses the phase boundary."""
    p_seafloor = 101325.0 + RHO_W_GEO * G * water_depth_m
    z = 0.0
    while z < 5000.0:
        T = 273.15 + T_surf_C + gradient_C_per_km / 1000.0 * z
        p = p_seafloor + RHO_W_GEO * G * z
        if p < p_equilibrium(T):
            return z
        z += dz
    return np.nan


def dry_moduli(phi):
    """Stated linear dry-frame model: moduli fall as porosity rises."""
    f = 1.0 - (phi - PHI_REF) / PHI_SENS
    return KDRY_REF * f, GDRY_REF * f


def shear_pore_filling(phi):
    """Shear modulus for the pore-filling model: Gassmann leaves it unchanged."""
    _, g_dry = dry_moduli(phi)
    return g_dry


def shear_cementation(phi, sh):
    """Shear modulus for the cementation model: the frame is stiffened."""
    _, g_dry = dry_moduli(phi)
    return g_dry + 3.0e9 * np.sqrt(sh)


def density_sat(phi, sh):
    return ((1.0 - phi) * RHO_QUARTZ +
            phi * (sh * RHO_HYDRATE_EL + (1.0 - sh) * RHO_W))


def vel_pore_filling(phi, sh, water_only=False):
    """Gassmann velocity for hydrate as part of the pore fluid."""
    k_dry, g_dry = dry_moduli(phi)
    if water_only or sh <= 0.0:
        k_fl = K_WATER
    elif sh >= 1.0:
        k_fl = K_HYDRATE
    else:
        k_fl = 1.0 / (sh / K_HYDRATE + (1.0 - sh) / K_WATER)
    num = (1.0 - k_dry / K_QUARTZ) ** 2
    den = phi / k_fl + (1.0 - phi) / K_QUARTZ - k_dry / K_QUARTZ ** 2
    k_sat = k_dry + num / den
    rho = (1.0 - phi) * RHO_QUARTZ + phi * (sh * RHO_HYDRATE_EL +
                                           (1.0 - sh) * RHO_W)
    return np.sqrt((k_sat + 4.0 * g_dry / 3.0) / rho)


def vel_cementation(phi, sh):
    """Gassmann velocity with hydrate stiffening the frame (cementation model)."""
    k_dry, g_dry = dry_moduli(phi)
    k_dry = k_dry + 4.0e9 * np.sqrt(sh)
    g_dry = g_dry + 3.0e9 * np.sqrt(sh)
    k_fl = K_WATER
    num = (1.0 - k_dry / K_QUARTZ) ** 2
    den = phi / k_fl + (1.0 - phi) / K_QUARTZ - k_dry / K_QUARTZ ** 2
    k_sat = k_dry + num / den
    rho = (1.0 - phi) * RHO_QUARTZ + phi * (sh * RHO_HYDRATE_EL +
                                           (1.0 - sh) * RHO_W)
    return np.sqrt((k_sat + 4.0 * g_dry / 3.0) / rho)


def main():
    section("1. Structure-I stoichiometry and the gas yield")
    y, frac = gas_yield_per_m3()
    print("  ideal structure-I unit cell: 46 H2O and up to 8 CH4 (model)")
    print(f"  mass fraction CH4 at full occupancy = 8 x {M_CH4 * 1e3:.3f} / "
          f"(8 x {M_CH4 * 1e3:.3f} + 46 x {M_H2O * 1e3:.3f}) = {frac:.5f}")
    print(f"  molar volume at STP = {V_MOLAR_STP * 1e3:.3f} L/mol "
          f"(273.15 K, 101.325 kPa)")
    print(f"  hydrate density (model) = {RHO_HYDRATE:.0f} kg/m^3")
    print(f"  gas yield = {y:.1f} m^3 (STP) per m^3 of hydrate")
    print("\n  sensitivity to the two assumed constants:")
    print("   density (kg/m^3)   occupancy   yield (m^3/m^3)")
    for rho in (850.0, 900.0, 950.0):
        for occ in (0.8, 1.0):
            yy, _ = gas_yield_per_m3(occupancy=occ, rho_h=rho)
            print(f"   {rho:16.0f}   {occ:9.2f}   {yy:17.1f}")
    print("  the yield is a ratio of constants, not a measurement: it is the one")
    print("  number in a hydrate resource estimate that can be stated exactly.")

    section("2. Base of the hydrate stability zone")
    print(f"  phase-boundary model: ln(p/p_ref) = -({A_CLAPEYRON:.0f})(1/T - "
          f"1/{T_REF:.2f}), p_ref = {P_REF / 1e6:.2f} MPa")
    print("  (a model equivalent to a constant dissociation enthalpy of "
          f"{A_CLAPEYRON * R_GAS / 1e3:.1f} kJ/mol)")
    print("\n   T (K)   p_eq (MPa)   hydrostatic depth (m)")
    for T in (275.15, 280.15, 285.15, 290.15, 295.15, 300.15):
        pe = p_equilibrium(T)
        print(f"  {T:7.2f}   {pe / 1e6:10.2f}   "
              f"{(pe - 101325.0) / (RHO_W_GEO * G):16.0f}")
    print("\n  base of the stability zone below the seafloor:")
    print("   water depth (m)   T_surf (C)   gradient (C/km)   base (m)")
    for wd in (500.0, 1000.0, 2000.0):
        for ts in (2.0, 4.0):
            for gr in (25.0, 40.0):
                zb = depth_base_hsz(ts, gr, wd)
                print(f"  {wd:15.0f}   {ts:10.1f}   {gr:15.0f}   {zb:8.0f}")
    print("  a warmer seafloor or a steeper gradient shallows the base; the base is")
    print("  what a bottom-simulating reflector is taken to mark.")

    section("3. Velocity versus hydrate saturation and its inversion")
    phi = 0.35
    print(f"  fixed porosity {phi:.2f}; dry-frame model: K_dry = {KDRY_REF / 1e9:.2f}"
          f" GPa, G_dry = {GDRY_REF / 1e9:.2f} GPa at phi = {PHI_REF:.2f}")
    print("\n   S_h   vp pore (m/s)   vp cem (m/s)   vs pore   vs cem   vp/vs pore   vp/vs cem")
    sh_grid = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.7, 1.0])
    for sh in sh_grid:
        rho = density_sat(phi, sh)
        vs_p = np.sqrt(shear_pore_filling(phi) / rho)
        vs_c = np.sqrt(shear_cementation(phi, sh) / rho)
        print(f"  {sh:4.2f}   {vel_pore_filling(phi, sh):13.1f}   "
              f"{vel_cementation(phi, sh):12.1f}   {vs_p:7.1f}   {vs_c:6.1f}   "
              f"{vel_pore_filling(phi, sh) / vs_p:11.2f}   "
              f"{vel_cementation(phi, sh) / vs_c:9.2f}")
    print("  the two models differ most in vs, not in vp: fluid substitution leaves")
    print("  the shear modulus untouched, so a pore-filling hydrate barely changes vs")
    print("  while a cementing one raises it by a factor of about two.")
    vp_obs = 2300.0
    print(f"\n  observed velocity (model measurement): vp = {vp_obs:.0f} m/s")
    from scipy.optimize import brentq
    sh_pf = brentq(lambda s: vel_pore_filling(phi, s) - vp_obs, 0.0, 1.0)
    sh_cem = brentq(lambda s: vel_cementation(phi, s) - vp_obs, 0.0, 1.0)
    print(f"    pore-filling model implies S_h = {sh_pf:.3f}")
    print(f"    cementation model  implies S_h = {sh_cem:.3f}")
    print(f"    ratio = {sh_pf / sh_cem:.2f}: the same velocity supports two "
          f"saturations")
    print("    that differ by a factor "
          f"{abs(sh_pf / sh_cem - 1) * 100:.0f}%.")
    check = vel_pore_filling(phi, sh_pf)
    print(f"    round-trip check of the pore-filling inversion: forward vp = "
          f"{check:.3f} m/s")

    print("\n  (porosity, saturation) pairs that reproduce vp = "
          f"{vp_obs:.0f} m/s in the pore-filling model:")
    print("   phi    S_h")
    for phi_t in (0.25, 0.30, 0.35, 0.40, 0.45):
        try:
            s = brentq(lambda ss: vel_pore_filling(phi_t, ss) - vp_obs, 1e-6,
                       0.999)
            print(f"  {phi_t:5.2f}   {s:5.3f}")
        except ValueError:
            print(f"  {phi_t:5.2f}   no solution in [0,1]")
    print("  velocity therefore constrains a curve in (porosity, saturation), not")
    print("  either parameter: it measures the product that controls the elastic")
    print("  moduli, and an independent porosity (a log, a core) is required.")

    section("4. Gas in place and its sensitivity")
    area_km2, thick_m, phi_r, sh_r = 100.0, 50.0, 0.35, 0.40
    area = area_km2 * 1e6
    hydrate_volume = area * thick_m * phi_r * sh_r
    gas_m3 = hydrate_volume * y
    print(f"  area {area_km2:.0f} km^2, thickness {thick_m:.0f} m, porosity "
          f"{phi_r:.2f}, saturation {sh_r:.2f}")
    print(f"  hydrate volume = A h phi S_h = {hydrate_volume:.3e} m^3")
    print(f"  gas in place = hydrate volume x {y:.1f} = {gas_m3:.3e} m^3 (STP)")
    print(f"  = {gas_m3 / 1e9:.1f} x 10^9 m^3 = {gas_m3 * 35.3147 / 1e12:.2f} "
          f"x 10^12 ft^3")
    print("\n  sensitivity (gas in place, 10^9 m^3):")
    print("   porosity   S_h = 0.2   S_h = 0.4   S_h = 0.6")
    for phi_t in (0.25, 0.35, 0.45):
        row = []
        for sh_t in (0.2, 0.4, 0.6):
            row.append(area * thick_m * phi_t * sh_t * y / 1e9)
        print(f"  {phi_t:9.2f}   {row[0]:11.1f}   {row[1]:11.1f}   {row[2]:11.1f}")
    print(f"  the range from (0.25, 0.2) to (0.45, 0.6) is "
          f"{(0.45 * 0.6) / (0.25 * 0.2):.1f}x from these two parameters alone,")
    print("  and they are exactly the two that the velocity cannot separate.  A")
    print("  recovery factor multiplying the result would widen it again, and the")
    print("  saturation model of section 3 would move it by a further factor of")
    print(f"  about {sh_pf / sh_cem:.1f}.")

    section("5. Worked examples used in the lesson")
    print(f"(a) gas yield = {y:.1f} m^3 (STP) per m^3 of hydrate "
          f"(mass fraction {frac:.4f})")
    print(f"(b) p_eq(285.15 K) = {p_equilibrium(285.15) / 1e6:.2f} MPa")
    print(f"    p_eq(295.15 K) = {p_equilibrium(295.15) / 1e6:.2f} MPa")
    print(f"(c) base of the stability zone, 1000 m water, 2 C, 40 C/km = "
          f"{depth_base_hsz(2.0, 40.0, 1000.0):.0f} m below the seafloor")
    print(f"    and for 4 C, 40 C/km = "
          f"{depth_base_hsz(4.0, 40.0, 1000.0):.0f} m")
    print(f"(d) at S_h = 0.5: pore-filling vp = {vel_pore_filling(0.35, 0.5):.0f} "
          f"m/s, vs = {np.sqrt(shear_pore_filling(0.35) / density_sat(0.35, 0.5)):.0f} "
          f"m/s (vp/vs = {vel_pore_filling(0.35, 0.5) / np.sqrt(shear_pore_filling(0.35) / density_sat(0.35, 0.5)):.2f})")
    print(f"    cementation vp = {vel_cementation(0.35, 0.5):.0f} m/s, vs = "
          f"{np.sqrt(shear_cementation(0.35, 0.5) / density_sat(0.35, 0.5)):.0f} m/s "
          f"(vp/vs = {vel_cementation(0.35, 0.5) / np.sqrt(shear_cementation(0.35, 0.5) / density_sat(0.35, 0.5)):.2f})")
    print(f"    vp = 2300 m/s inverts to S_h = {sh_pf:.3f} or {sh_cem:.3f} "
          f"depending on the model")
    print(f"(e) gas in place = {gas_m3:.3e} m^3 (STP) for the model accumulation")
    print("\nAll numbers are SYNTHETIC model output.")


if __name__ == "__main__":
    main()
