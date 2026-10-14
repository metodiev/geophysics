#!/usr/bin/env python3
"""Seismic velocity versus saturation: Gassmann fluid substitution with a
uniform (Wood) and a patchy (Hill) pore fluid, the Vp softening they predict,
and the two analytic checks that validate the implementation.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python seismic_velocity_saturation_demo.py

Every model here is SYNTHETIC: the mineral moduli, the dry-rock moduli and the
porosity are chosen teaching values.  The only numbers treated as standard
constants are the bulk moduli and densities of water, air and (in the last
section) ice.  No measured rock is reported.

Contents
--------
1.  Inputs, and the two analytic limits of the Gassmann relation.
2.  Uniform saturation: Wood (Reuss) fluid mixing and Vp(Sw), Vs(Sw), rho(Sw).
3.  Patchy saturation: the Hill average of the two end-member rocks.
4.  Uniform versus patchy: the crossover and the magnitude of the difference.
5.  Why Vs carries no fluid signal (Gassmann) and what that is worth.
6.  Sensitivity to the dry-rock modulus: stiff and soft end members.
7.  The empirical Brie fluid mixing and where it sits between the two.
8.  Reference numbers used in the lesson.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC dry-rock and mineral model (chosen, not measured) -------------
PHI = 0.30
K_MIN, MU_MIN, RHO_MIN = 36.0, 45.0, 2650.0     # GPa, GPa, kg/m^3
K_DRY, MU_DRY = 8.0, 7.0                        # GPa, GPa

# --- standard material constants ---------------------------------------------
K_WATER, RHO_WATER = 2.20, 1000.0               # GPa, kg/m^3
K_AIR, RHO_AIR = 1.0e-4, 1.2                    # GPa (1e5 Pa), kg/m^3


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def gassmann(k_dry, k_min, k_fl, phi):
    """Gassmann saturated bulk modulus (GPa)."""
    num = (1.0 - k_dry / k_min) ** 2
    den = phi / k_fl + (1.0 - phi) / k_min - k_dry / k_min ** 2
    return k_dry + num / den


def velocities(k_sat, mu_sat, rho_kg_m3):
    """Vp and Vs in km/s from moduli in GPa and density in kg/m^3."""
    k_pa = k_sat * 1.0e9
    mu_pa = mu_sat * 1.0e9
    vp = np.sqrt((k_pa + 4.0 * mu_pa / 3.0) / rho_kg_m3) / 1.0e3
    vs = np.sqrt(mu_pa / rho_kg_m3) / 1.0e3
    return vp, vs


def wood_fluid(sw, k_w=K_WATER, k_g=K_AIR):
    """Reuss (harmonic) average of the fluid bulk moduli, in GPa."""
    return 1.0 / (sw / k_w + (1.0 - sw) / k_g)


def brie_fluid(sw, e=3.0, k_w=K_WATER, k_g=K_AIR):
    """Brie's empirical fluid mixing, in GPa."""
    return (k_w - k_g) * sw ** e + k_g


def saturated_state(sw, k_dry=K_DRY, mu_dry=MU_DRY, patchy=False):
    """Return (K_sat, mu_sat, rho, Vp, Vs) for a given water saturation."""
    if patchy:
        k1 = gassmann(k_dry, K_MIN, K_WATER, PHI)
        k0 = gassmann(k_dry, K_MIN, K_AIR, PHI)
        k_sat = sw * k1 + (1.0 - sw) * k0
    else:
        k_sat = gassmann(k_dry, K_MIN, wood_fluid(sw), PHI)
    mu_sat = mu_dry
    rho = (1.0 - PHI) * RHO_MIN + PHI * (sw * RHO_WATER + (1.0 - sw) * RHO_AIR)
    vp, vs = velocities(k_sat, mu_sat, rho)
    return k_sat, mu_sat, rho, vp, vs


def main():
    section("1. Inputs and the analytic limits of the Gassmann relation")
    print("  SYNTHETIC dry rock: phi = 0.30, K_dry = 8.00 GPa, mu_dry = 7.00 GPa")
    print("  SYNTHETIC mineral:  K_min = 36.00 GPa, mu_min = 45.00 GPa, "
          "rho_min = 2650 kg/m^3")
    print("  standard fluids:    K_water = 2.20 GPa, K_air = 1.0e-4 GPa, "
          "rho_water = 1000 kg/m^3")
    k_sat_w = gassmann(K_DRY, K_MIN, K_WATER, PHI)
    k_sat_a = gassmann(K_DRY, K_MIN, K_AIR, PHI)
    k_limit = gassmann(K_DRY, K_MIN, K_MIN, PHI)
    print("  limit check 1: K_fl = K_air (a very compressible fluid) makes the rock")
    print(f"    barely softer than dry: K_sat = {k_sat_a:.4f} GPa vs K_dry = "
          f"{K_DRY:.2f} GPa, a {100 * (k_sat_a / K_DRY - 1.0):.2f}% increase")
    print("  limit check 2: K_fl = K_min (a fluid as stiff as the mineral) must")
    print(f"    return K_sat = K_min = {K_MIN:.2f} GPa; the code gives "
          f"{k_limit:.6f} GPa")
    print(f"  water-saturated end member: K_sat(Sw=1) = {k_sat_w:.4f} GPa")

    section("2. Uniform saturation: Wood fluid mixing and the velocities")
    print("      Sw     K_fl (GPa)   K_sat (GPa)   rho (kg/m^3)   Vp (km/s)   Vs (km/s)")
    for sw in np.linspace(0.0, 1.0, 11):
        k_fl = wood_fluid(sw)
        k_sat, mu_sat, rho, vp, vs = saturated_state(sw)
        print(f"  {sw:5.2f}   {k_fl:10.5f}   {k_sat:11.4f}   {rho:12.1f}   "
              f"{vp:9.4f}   {vs:9.4f}")
    sw_grid = np.linspace(0.0, 1.0, 1001)
    vp_uniform = np.array([saturated_state(s)[3] for s in sw_grid])
    i_min = int(np.argmin(vp_uniform))
    print(f"  the uniform model has an interior Vp minimum: Vp = "
          f"{vp_uniform[i_min]:.4f} km/s at Sw = {sw_grid[i_min]:.2f}")
    print("  the minimum sits next to Sw = 1 because the Wood average stays")
    print("  gas-dominated until the last few per cent of water (K_fl is only")
    print(f"  {wood_fluid(0.90):.5f} GPa at Sw = 0.90).")
    print(f"  Vp falls by {1000 * (saturated_state(0.0)[3] - vp_uniform[i_min]):.1f} m/s "
          f"from the dry value before rising again.")

    section("3. Patchy saturation: the Hill average of the two end members")
    print("      Sw     K_sat (GPa)   rho (kg/m^3)   Vp (km/s)   Vs (km/s)")
    for sw in np.linspace(0.0, 1.0, 11):
        k_sat, mu_sat, rho, vp, vs = saturated_state(sw, patchy=True)
        print(f"  {sw:5.2f}   {k_sat:11.4f}   {rho:12.1f}   {vp:9.4f}   {vs:9.4f}")
    vp_patchy = np.array([saturated_state(s, patchy=True)[3] for s in sw_grid])
    i_min_p = int(np.argmin(vp_patchy))
    print(f"  the patchy curve has its minimum at Sw = {sw_grid[i_min_p]:.2f} "
          f"(Vp = {vp_patchy[i_min_p]:.4f} km/s):")
    print("  for these inputs it rises monotonically, so the softening is a feature of")
    print("  the uniform-fluid geometry, not of saturation itself.")

    section("4. Uniform versus patchy: the size of the unsolved ambiguity")
    print("      Sw     Vp uniform   Vp patchy   patchy - uniform (m/s)")
    for sw in (0.0, 0.1, 0.2, 0.3, 0.5, 0.7, 0.9, 0.95, 1.0):
        vu = saturated_state(sw)[3]
        vp = saturated_state(sw, patchy=True)[3]
        print(f"  {sw:5.2f}   {vu:10.4f}   {vp:9.4f}   {1000 * (vp - vu):+19.1f}")
    diff = 1000.0 * (vp_patchy - vp_uniform)
    print(f"  maximum difference over the sweep = {np.max(np.abs(diff)):.1f} m/s "
          f"at Sw = {sw_grid[int(np.argmax(np.abs(diff)))]:.2f}")
    print("  the two curves touch only at Sw = 0.00 and Sw = 1.00; every intermediate")
    print("  saturation is model-dependent.")
    vp_target = 2.90
    idx = int(np.argmin(np.abs(vp_uniform - vp_target)))
    print(f"  a measured Vp = {vp_target:.2f} km/s sits closest to the uniform curve")
    print(f"  at Sw = {sw_grid[idx]:.3f} (Vp = {vp_uniform[idx]:.4f} km/s), but the")
    print(f"  patchy curve never reaches it (patchy minimum "
          f"{vp_patchy.min():.4f} km/s).  The same Vp is also reached by lowering")
    print("  K_dry, so Vp alone cannot separate saturation from frame stiffness.")

    section("5. Shear velocity and the fluid: Gassmann's rigid prediction")
    vs_all = [saturated_state(s)[4] for s in sw_grid]
    print(f"  mu_sat = mu_dry = {MU_DRY:.1f} GPa at every saturation; Vs varies only")
    print(f"  through rho, from {max(vs_all):.4f} to {min(vs_all):.4f} km/s.")
    for sw in (0.0, 0.5, 1.0):
        rho = saturated_state(sw)[2]
        print(f"    Sw = {sw:.1f}: rho = {rho:.1f} kg/m^3, "
              f"Vs = sqrt(mu_dry/rho) = {saturated_state(sw)[4]:.4f} km/s")
    print(f"  the whole Vs change is {1000 * (max(vs_all) - min(vs_all)):.1f} m/s over")
    print("  the full saturation range, versus "
          f"{1000 * (max(vp_uniform) - min(vp_uniform)):.1f} m/s for Vp.")
    print("  A measured Vs that drops far more than rho explains falsifies the")
    print("  dry-frame model, which is why Vs is the useful quality control.")

    section("6. Sensitivity to the dry-rock modulus (stiff versus soft frame)")
    print("      Sw     Vp (K_dry=12)   Vp (K_dry=8)   Vp (K_dry=4)   (km/s)")
    for sw in (0.0, 0.2, 0.5, 0.8, 1.0):
        a = saturated_state(sw, k_dry=12.0)[3]
        b = saturated_state(sw, k_dry=8.0)[3]
        c = saturated_state(sw, k_dry=4.0)[3]
        print(f"  {sw:5.2f}   {a:14.4f}   {b:13.4f}   {c:13.4f}")
    print("  drop from Sw = 0.00 to Sw = 0.80 at each frame stiffness:")
    for kd in (12.0, 8.0, 4.0):
        v0 = saturated_state(0.0, k_dry=kd)[3]
        v8 = saturated_state(0.8, k_dry=kd)[3]
        print(f"    K_dry = {kd:5.1f} GPa: {1000 * (v0 - v8):6.1f} m/s, "
              f"{100 * (v0 - v8) / v0:5.2f}% of Vp(dry)")
    print("  the frame stiffness shifts the level of the curve; the fractional")
    print("  softening is almost the same, so Vp cannot rank two sites by saturation")
    print("  without an independent constraint on the dry frame.")

    section("7. Brie's empirical fluid mixing for comparison")
    print("      Sw     K_fl Brie(e=3)   K_fl Wood   K_fl arithmetic (GPa)")
    for sw in (0.0, 0.2, 0.4, 0.6, 0.8, 1.0):
        print(f"  {sw:5.2f}   {brie_fluid(sw):15.5f}   {wood_fluid(sw):11.5f}   "
              f"{(sw * K_WATER + (1 - sw) * K_AIR):17.5f}")
    k_brie = [gassmann(K_DRY, K_MIN, brie_fluid(s), PHI) for s in sw_grid]
    vp_brie = np.array([velocities(k, MU_DRY,
                                   (1 - PHI) * RHO_MIN
                                   + PHI * (s * RHO_WATER + (1 - s) * RHO_AIR))[0]
                        for k, s in zip(k_brie, sw_grid)])
    i_b = int(np.argmin(vp_brie))
    print(f"  Brie gives an intermediate curve with Vp = {vp_brie[i_b]:.4f} km/s at")
    print(f"  Sw = {sw_grid[i_b]:.2f}.  The exponent e is fitted, so Brie interpolates")
    print("  between the two physical end members rather than predicting either.")

    section("8. Reference numbers used in the lesson")
    k_sat, mu_sat, rho, vp, vs = saturated_state(1.0)
    print(f"  fully water-saturated: K_sat = {k_sat:.4f} GPa, rho = {rho:.1f} kg/m^3,")
    print(f"    Vp = {vp:.4f} km/s, Vs = {vs:.4f} km/s")
    k_sat0, _, rho0, vp0, vs0 = saturated_state(0.0)
    print(f"  dry (gas-saturated):   K_sat = {k_sat0:.4f} GPa, rho = {rho0:.1f} kg/m^3,")
    print(f"    Vp = {vp0:.4f} km/s, Vs = {vs0:.4f} km/s")


if __name__ == "__main__":
    main()
