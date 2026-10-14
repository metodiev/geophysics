#!/usr/bin/env python3
"""Aquifer properties: porosity, effective porosity, specific yield, storativity,
hydraulic conductivity and intrinsic permeability, on SYNTHETIC rock models.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python aquifer_types_and_properties_demo.py

Every rock, grain size and storage coefficient below is a SYNTHETIC teaching
value.  Nothing here is a measurement of a named formation.

Standard physical constants used (exact or tabulated properties of the model):
    rho_w = 1000 kg/m^3            density of fresh water at 20 C (to 4 digits)
    g     = 9.81 m/s^2             standard gravity used throughout this module
    mu_w  = 1.002e-3 Pa s          dynamic viscosity of water at 20 C
    beta_w = 4.4e-10 1/Pa          water compressibility at 20 C
    1 darcy = 9.869233e-13 m^2     definition of the darcy

Contents
--------
1. Total porosity from bulk and grain density, with a mass-balance verification.
2. Effective porosity, specific yield and specific retention.
3. Storativity: the confined and unconfined mechanisms and their ratio.
4. Hydraulic conductivity to intrinsic permeability, in m^2 and darcy.
5. Kozeny-Carman: K from grain size and porosity, and its sensitivity.
6. A layered aquifer: horizontal versus vertical effective conductivity.
7. How much water a unit area actually yields, by aquifer type.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

RHO_W = 1000.0          # kg/m^3
G = 9.81                # m/s^2
MU_W = 1.002e-3         # Pa s at 20 C
BETA_W = 4.4e-10        # 1/Pa, compressibility of water at 20 C
DARCY = 9.869233e-13    # m^2


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def porosity_from_density(rho_bulk_gcc, rho_grain_gcc):
    """n = 1 - rho_bulk / rho_grain, both in g/cm^3 (dimensionless ratio)."""
    return 1.0 - rho_bulk_gcc / rho_grain_gcc


def specific_storage(alpha_rock_pa_inv, n, rho_w=RHO_W, g=G, beta_w=BETA_W):
    """S_s = rho_w g (alpha_rock + n beta_w), in 1/m.

    alpha_rock is the vertical compressibility of the rock framework in 1/Pa.
    """
    return rho_w * g * (alpha_rock_pa_inv + n * beta_w)


def k_intrinsic_from_K(K_m_s, mu=MU_W, rho_w=RHO_W, g=G):
    """Darcy's law in intrinsic form: K = k rho g / mu  ->  k = K mu / (rho g)."""
    return K_m_s * mu / (rho_w * g)


def kozeny_carman_K(d_grain_m, n, mu=MU_W, rho_w=RHO_W, g=G, c_kc=180.0):
    """K = (rho_w g / mu) * d^2 n^3 / (c_kc (1-n)^2), a capillary-bundle model.

    c_kc = 180 is the Kozeny constant for a bundle of circular capillaries; it is
    a MODEL constant of order 10-200 depending on pore shape and tortuosity, not a
    measured property of any sediment.  Its value is stated so it can be changed.
    """
    k = d_grain_m ** 2 * n ** 3 / (c_kc * (1.0 - n) ** 2)
    return k * rho_w * g / mu


def main():
    section("1. Total porosity from bulk and grain density")
    print("SYNTHETIC rocks: n = 1 - rho_bulk / rho_grain (both in g/cm^3)")
    print("   rock               rho_bulk  rho_grain   n_total")
    rocks = (("well-sorted sand", 1.90, 2.65),
             ("sandy limestone", 2.25, 2.71),
             ("low-porosity granite", 2.62, 2.66))
    for name, rb, rs in rocks:
        print(f"   {name:20s} {rb:8.2f} {rs:10.2f}   {porosity_from_density(rb, rs):7.4f}")
    print("\n  mass-balance verification on a synthetic saturated sample:")
    vol_bulk_cm3 = 100.0
    rho_b = 1.90
    rho_s = 2.65
    m_dry = rho_b * vol_bulk_cm3
    n = porosity_from_density(rho_b, rho_s)
    v_water = n * vol_bulk_cm3
    m_sat = m_dry + v_water * 1.0  # rho_w = 1.00 g/cm^3
    n_from_mass = (m_sat - m_dry) / vol_bulk_cm3
    print(f"   bulk volume = {vol_bulk_cm3:.1f} cm^3, dry mass = {m_dry:.3f} g")
    print(f"   water filling the pores at saturation = {v_water:.4f} cm^3")
    print(f"   saturated mass = {m_sat:.3f} g")
    print(f"   n from the mass balance = {n_from_mass:.4f}  vs  1 - rho_b/rho_s = "
          f"{n:.4f}   difference = {abs(n_from_mass - n):.2e}")

    section("2. Effective porosity, specific yield and specific retention")
    print("SYNTHETIC sandstone: n_total = 0.2830; some pores are dead-end or clay-bound")
    n_total = n
    for n_eff, sy in ((0.25, 0.20), (0.25, 0.12), (0.20, 0.06)):
        sr = n_eff - sy
        print(f"   n_total = {n_total:.4f}  n_eff = {n_eff:.2f}  "
              f"S_y = {sy:.2f}  S_r = n_eff - S_y = {sr:.2f}")
    print("  check: S_y + S_r = n_eff  and n_eff <= n_total for every row")
    print("  with n_eff = 0.25, S_y = 0.20: a 1 m drop of the water table in a")
    print("  column of unit area releases 0.20 m of water; the 0.05 m that stays")
    print("  is the specific retention (film water held against gravity).")

    section("3. Storativity: two different mechanisms")
    print("confined:  S = S_s b,  S_s = rho_w g (alpha_rock + n beta_w)")
    print("   alpha_rock (1/Pa)    n      S_s (1/m)    b (m)     S        mechanism")
    for alpha, nn, b, label in ((1.0e-9, 0.25, 30.0, "stiff sandstone"),
                                (5.0e-9, 0.25, 30.0, "soft sandstone"),
                                (3.0e-8, 0.25, 30.0, "loose sand/clay")):
        ss = specific_storage(alpha, nn)
        print(f"   {alpha:13.1e}   {nn:5.2f}   {ss:11.4e}   {b:5.1f}   "
              f"{ss * b:9.3e}   {label}")
    ss = specific_storage(1.0e-9, 0.25)
    S_conf = ss * 30.0
    S_unconf = 0.20
    print(f"\n  unconfined: S = S_y = {S_unconf:.2f} (drainage of pores)")
    print(f"  confined  : S = {S_conf:.3e} (water expansion + rock compression)")
    print(f"  ratio S_unconfined / S_confined = {S_unconf / S_conf:.0f}")
    print("  the two mechanisms differ by three orders of magnitude for the SAME rock:"
          )
    print("  that is why a confined aquifer is not dewatered by pumping, and why its")
    print("  pressure response is fast and its volume response is small.")

    section("4. Hydraulic conductivity to intrinsic permeability")
    print(f"  mu_w = {MU_W:.4e} Pa s, rho_w = {RHO_W:.0f} kg/m^3, g = {G} m/s^2")
    print("   K (m/s)     k (m^2)      k (darcy)    verdict")
    for K in (1.0e-2, 1.0e-4, 1.0e-6, 1.0e-8, 1.0e-10):
        k = k_intrinsic_from_K(K)
        print(f"   {K:9.1e}   {k:11.4e}   {k / DARCY:11.4e}    "
              f"{'fast' if K > 1e-5 else ('moderate' if K > 1e-7 else 'slow')}")
    print("  K is a property of the rock AND the fluid; k is a property of the rock")
    print("  only.  Reporting K without stating mu_w and rho_w is incomplete, and the")
    print("  error is a factor of about 2 between water at 5 C and at 30 C.")

    section("5. Kozeny-Carman: K from grain size and porosity")
    n_sand = 0.2830
    print(f"  K = (rho_w g / mu) d^2 n^3 / (180 (1-n)^2) with n = {n_sand:.4f}")
    print("   d (mm)      K (m/s)     classify (convention: >1e-4 high, "
          "1e-7..1e-4 moderate, <1e-7 low)")
    for d_mm in (0.05, 0.1, 0.2, 0.5, 1.0, 2.0):
        K = kozeny_carman_K(d_mm * 1e-3, n_sand)
        cls = "high" if K > 1e-4 else ("moderate" if K > 1e-7 else "low")
        print(f"   {d_mm:6.2f}   {K:11.4e}   {cls}")
    K_target = 1.0e-4
    print(f"\n  inversion: which grain size gives K = {K_target:.1e} m/s at n = {n_sand:.4f}?")
    print(f"   d = {np.sqrt(K_target * MU_W * 180.0 * (1 - n_sand) ** 2 / (RHO_W * G * n_sand ** 3)) * 1e3:.3f} mm")
    print("  sensitivity: K scales as d^2 and strongly with n.  A 10% error in d is a")
    print("  21% error in K; a 10% error in n is a "
          f"{abs((lambda f: (kozeny_carman_K(5e-4, n_sand * f) / kozeny_carman_K(5e-4, n_sand) - 1))(1.1)) * 100:.0f}% "
          "error in K at n = 0.2830.")

    section("6. A layered aquifer: horizontal versus vertical effective K")
    layers = (("clean sand", 2.0, 5.0e-4),
              ("silty sand", 5.0, 2.0e-5),
              ("clay lens", 1.0, 1.0e-9),
              ("clean sand", 3.0, 4.0e-4))
    b_tot = sum(b for _, b, _ in layers)
    K_arith = sum(b * K for _, b, K in layers) / b_tot
    K_harm = b_tot / sum(b / K for _, b, K in layers)
    print("   unit            b (m)     K (m/s)      T (m^2/s)")
    for name, b, K in layers:
        print(f"   {name:14s} {b:5.1f}   {K:10.3e}   {K * b:11.3e}")
    print(f"  total thickness b = {b_tot:.1f} m")
    print(f"  horizontal (arithmetic) K_h = sum(b_i K_i)/sum(b_i)      = {K_arith:.4e} m/s")
    print(f"  vertical   (harmonic)   K_v = sum(b_i) / sum(b_i/K_i)    = {K_harm:.4e} m/s")
    print(f"  anisotropy ratio K_h / K_v = {K_arith / K_harm:.1f}")
    print(f"  transmissivity using K_h: T = {K_arith * b_tot:.4e} m^2/s "
          f"(= {K_arith * b_tot * 86400:.1f} m^2/d)")
    print("  The SAME layers give two different conductivities depending on the flow")
    print("  direction, and the horizontal value is controlled by the most conductive")
    print("  layer while the vertical value is controlled by the least conductive one.")

    section("7. How much water a unit area actually yields")
    print("  storage released per unit area = S x head change (depth of water)")
    print("   case                          S          head change   water (mm)")
    cases = (("unconfined, S_y = 0.20", 0.20, 1.0),
             ("unconfined, S_y = 0.02", 0.02, 1.0),
             ("confined, S = 3.3e-4", 3.3e-4, 10.0),
             ("confined, S = 3.3e-4", 3.3e-4, 100.0))
    for name, S, dh in cases:
        print(f"   {name:28s} {S:9.4f}   {dh:8.1f} m   {S * dh * 1000:10.2f}")
    print("  A confined aquifer needs a hundred metres of head decline to release the")
    print("  water an unconfined aquifer releases from one metre of water-table drop.")
    print("  This is a statement about storage, and it is why the two cases must never")
    print("  be given the same specific-storage number.")


if __name__ == "__main__":
    main()
