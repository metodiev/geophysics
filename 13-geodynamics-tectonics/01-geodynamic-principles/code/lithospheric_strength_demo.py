#!/usr/bin/env python3
"""Lithospheric strength: flexure, effective elastic thickness and the yield
strength envelope.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python lithospheric_strength_demo.py

Everything here is SYNTHETIC: the loads, the deflection profile and both creep
laws are chosen teaching models.  Print-only; no figures.

Contents
--------
1. Flexural rigidity and the flexural parameter for several Te.
2. Deflection under a line load; the isostatic-area identity checked.
3. Narrow versus wide loads: flexural support against local (Airy) compensation.
4. Inverting a noisy synthetic deflection profile for Te (and its admitted range).
5. Te from a yield strength envelope (brittle + ductile), self-consistently.
6. How Te responds to the geotherm.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC teaching parameters (chosen, not measured) --------------------
E_YOUNG = 70.0e9       # Pa
NU = 0.25              # -
G = 9.81               # m/s^2 (standard)
DRHO = 2300.0          # kg/m^3  infill minus crustal-load density (top load)
RHO_LOAD = 2800.0      # kg/m^3
RHO_CRUST = 2800.0     # kg/m^3
RHO_MANTLE = 3300.0    # kg/m^3
H_LOAD = 2000.0        # m       load thickness of the synthetic feature
R_GAS = 8.314          # J/(mol K) (standard)
MU_SHEAR = 70.0e9      # Pa
# SYNTHETIC flow laws (same form as the rheology demo)
A_Q, N_Q, E_Q = 1.0e-19, 3.0, 200.0e3
A_O, N_O, E_O = 2.0e-28, 3.5, 350.0e3
EPS_REF = 1.0e-15      # 1/s reference strain rate for the envelope
MU_FRIC, LAMBDA_P = 0.75, 0.37
T_S = 273.15           # K


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def rigidity(Te):
    """Flexural rigidity D = E Te^3 / (12 (1 - nu^2)), N m."""
    return E_YOUNG * Te ** 3 / (12.0 * (1.0 - NU ** 2))


def flexural_parameter(Te, drho=DRHO):
    """alpha = (D / (drho g))^(1/4), m."""
    return (rigidity(Te) / (drho * G)) ** 0.25


def green_line(x, Te, drho=DRHO):
    """Deflection from a unit line load on an infinite elastic plate, m per N/m.

    w(x) = (alpha^3 / 2D) exp(-|x|/alpha) [cos(|x|/alpha) + sin(|x|/alpha)].
    """
    D = rigidity(Te)
    al = flexural_parameter(Te, drho)
    r = np.abs(x) / al
    return al ** 3 / (2.0 * D) * np.exp(-r) * (np.cos(r) + np.sin(r))


def geotherm(z, gamma_c=20.0, gamma_m=12.0, h_crust=35.0e3):
    """Synthetic piecewise-linear geotherm, K (gamma in K/km, z in m)."""
    return np.where(
        z <= h_crust,
        T_S + gamma_c * z / 1e3,
        T_S + gamma_c * h_crust / 1e3 + gamma_m * (z - h_crust) / 1e3,
    )


def sigma_yield(z, gamma_c=20.0, gamma_m=12.0, h_crust=35.0e3):
    """Yield strength envelope sigma_y(z), Pa (min of brittle and ductile)."""
    T = geotherm(z, gamma_c, gamma_m, h_crust)
    rho = np.where(z <= h_crust, RHO_CRUST, RHO_MANTLE)
    brittle = MU_FRIC * (1.0 - LAMBDA_P) * rho * G * z
    duct = np.where(
        z <= h_crust,
        (EPS_REF / (A_Q * np.exp(-E_Q / (R_GAS * T)))) ** (1.0 / N_Q),
        (EPS_REF / (A_O * np.exp(-E_O / (R_GAS * T)))) ** (1.0 / N_O),
    )
    return np.minimum(brittle, duct)


def yse_te(kappa, z, sy, Te_guess=40.0e3):
    """Effective elastic thickness from a yield strength envelope.

    The plate bends with curvature kappa.  The fibre stress is
        sigma(z) = clamp(-E kappa (z - z_n), -sigma_y, +sigma_y)
    where the neutral depth z_n is set by the condition of zero net axial force,
        integral sigma dz = 0.
    The bending moment M = integral sigma (z - z_n) dz then defines Te through
    M = E kappa Te^3 / (12 (1 - nu^2)).
    """
    zn0 = np.trapezoid(sy * z, z) / np.trapezoid(sy, z)  # start near the centroid

    def net_force(zn):
        sig = np.clip(-E_YOUNG * kappa * (z - zn), -sy, sy)
        return np.trapezoid(sig, z)

    lo, hi = -1.0e5, 3.0e5
    f_lo, f_hi = net_force(lo), net_force(hi)
    if f_lo * f_hi > 0:                     # no bracket: fall back to centroid
        zn = zn0
    else:
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            if f_lo * net_force(mid) <= 0:
                hi = mid
            else:
                lo, f_lo = mid, net_force(mid)
        zn = 0.5 * (lo + hi)
    sig = np.clip(-E_YOUNG * kappa * (z - zn), -sy, sy)
    M = np.trapezoid(sig * (z - zn), z)
    Te = (12.0 * (1.0 - NU ** 2) * abs(M) / (E_YOUNG * kappa)) ** (1.0 / 3.0)
    return Te, zn, M


def main():
    print(f"SYNTHETIC constants: E = {E_YOUNG / 1e9:.1f} GPa, nu = {NU:.2f}, "
          f"drho = {DRHO:.0f} kg/m^3")

    section("1. Flexural rigidity and the flexural parameter")
    print("   Te (km)     D (N m)         alpha (km)    flexural wavelength 2 pi alpha (km)")
    for Te_km in (10.0, 25.0, 40.0):
        Te = Te_km * 1e3
        D = rigidity(Te)
        al = flexural_parameter(Te)
        print(f"   {Te_km:6.0f}   {D:.4e}   {al / 1e3:12.1f}    "
              f"{2 * np.pi * al / 1e3:24.1f}")
    print("  Te is the single free parameter that sets how far a load is felt.")

    section("2. Deflection under a line load, and the isostatic-area identity")
    Te = 25.0e3
    D, al = rigidity(Te), flexural_parameter(Te)
    A_load = H_LOAD * 100.0e3              # m^2, cross-section of a 100 km wide load
    V0 = RHO_LOAD * G * A_load             # N/m
    w0 = V0 * al ** 3 / (2.0 * D)
    w0_broken = V0 * al ** 3 / D
    print(f"  SYNTHETIC load: {H_LOAD / 1e3:.0f} km high, 100 km wide, "
          f"rho = {RHO_LOAD:.0f} kg/m^3")
    print(f"  line load V0 = rho g A = {V0:.4e} N/m")
    print(f"  D = {D:.4e} N m, alpha = {al / 1e3:.2f} km")
    print(f"  continuous plate:  w(0) = V0 alpha^3/(2D) = {w0:.1f} m")
    print(f"  broken plate:      w(0) = V0 alpha^3/D    = {w0_broken:.1f} m")
    dxg = 2.0e3
    xg = np.arange(-1.0e6, 1.0e6 + dxg, dxg)
    wg = green_line(xg, Te) * V0
    area_num = np.trapezoid(wg, xg)
    area_exact = V0 / (DRHO * G)
    print(f"  isostatic-area check: integral w dx = {area_num:.6e} m^2")
    print(f"                        V0/(drho g)   = {area_exact:.6e} m^2")
    print(f"  relative error = {abs(area_num - area_exact) / area_exact:.2e}")

    section("3. Narrow versus wide loads: flexure against local compensation")
    w_airy = RHO_LOAD * H_LOAD / DRHO       # locally compensated root, m
    print(f"  local (Airy) compensation depth for this load = {w_airy:.0f} m")
    print("   half-width a (km)   w(0) (m)   w(0)/w_Airy   area check (should be 1)")
    for a_km in (10.0, 25.0, 50.0, 100.0, 300.0):
        a = a_km * 1e3
        qx = np.where(np.abs(xg) <= a, RHO_LOAD * G * H_LOAD, 0.0)   # N/m^2
        # convolution with the line-load Green's function (trapezoid on a fine grid)
        w = np.convolve(qx, green_line(xg, Te), mode="same") * dxg
        i0 = np.argmin(np.abs(xg))
        area_q = np.trapezoid(qx, xg) / (DRHO * G)
        area_w = np.trapezoid(w, xg)
        print(f"   {a_km:14.0f}   {w[i0]:8.0f}   {w[i0] / w_airy:11.2f}   "
              f"{area_w / area_q:18.4f}")
    print("  narrow loads are held up by plate bending (w < Airy root); wide loads")
    print("  are compensated locally as Airy assumed.  The area identity holds for all.")

    section("4. Inverting a synthetic deflection profile for Te")
    Te_true = 25.0e3
    a = 100.0e3
    qx = np.where(np.abs(xg) <= a, RHO_LOAD * G * H_LOAD, 0.0)
    w_true = np.convolve(qx, green_line(xg, Te_true), mode="same") * (xg[1] - xg[0])
    band = np.abs(xg) <= 4.0e5
    noise = 0.05 * np.std(w_true[band]) * RNG.standard_normal(xg.size)
    w_meas = w_true + noise
    print(f"  SYNTHETIC data: Te_true = {Te_true / 1e3:.0f} km, "
          f"{band.sum()} samples, 5% noise")
    print("   Te (km)   rms misfit (m)   ratio to minimum")
    Te_grid = np.arange(5.0, 61.0, 1.0) * 1e3
    misfits = []
    for Te_g in Te_grid:
        wg2 = np.convolve(qx, green_line(xg, Te_g), mode="same") * dxg
        misfits.append(np.sqrt(np.mean((wg2[band] - w_meas[band]) ** 2)))
    misfits = np.array(misfits)
    i_best = int(np.argmin(misfits))
    best = Te_grid[i_best]
    admitted = Te_grid[misfits <= 1.5 * misfits[i_best]]
    for Te_g, m in zip(Te_grid[::5], misfits[::5]):
        print(f"   {Te_g / 1e3:6.0f}   {m:14.1f}   {m / misfits[i_best]:14.2f}")
    print(f"  best-fit Te = {best / 1e3:.0f} km (true {Te_true / 1e3:.0f} km)")
    print(f"  admitted range (misfit <= 1.5 x minimum): "
          f"{admitted.min() / 1e3:.0f} - {admitted.max() / 1e3:.0f} km")
    print("  the profile constrains Te well because loading is known; in nature the")
    print("  load is the largest single uncertainty and biases Te.")

    section("5. Te from a yield strength envelope (self-consistent)")
    z = np.arange(0.0, 150.0e3, 100.0)
    sy = sigma_yield(z)
    i_peak = int(np.argmax(sy))
    print(f"  maximum yield strength in the envelope = {sy[i_peak] / 1e6:.0f} MPa "
          f"at z = {z[i_peak] / 1e3:.1f} km")
    print("   curvature kappa (1/m)   neutral depth (km)   Te (km)   moment (N)")
    for kappa in (1e-8, 1e-7, 1e-6):
        Te_yse, zn, M = yse_te(kappa, z, sy)
        print(f"   {kappa:.1e}              {zn / 1e3:16.1f}   "
              f"{Te_yse / 1e3:7.1f}   {M:.4e}")
    print("  at small curvature the whole envelope stays elastic and Te is large;")
    print("  as curvature grows the weak layers yield and the moment saturates, so")
    print("  Te falls.  A single Te therefore describes a range of curvatures only.")

    section("6. How Te responds to the geotherm")
    for gam_c, gam_m, label in ((10.0, 6.0, "cold"), (20.0, 12.0, "reference"),
                                (30.0, 18.0, "hot")):
        sy = sigma_yield(z, gam_c, gam_m)
        Te_yse, zn, M = yse_te(1e-7, z, sy)
        print(f"  {label:9s} geotherm {gam_c:4.1f}/{gam_m:4.1f} K/km -> "
              f"Te = {Te_yse / 1e3:6.1f} km, neutral depth {zn / 1e3:5.1f} km")
    print("  Te tracks the depth of the brittle-ductile transition, which is set by")
    print("  temperature: Te is a thermometer, not a material property.")

    print("\n" + "=" * 72)
    print("All loads, deflections, geotherms and flow laws are SYNTHETIC.")
    print("Only g = 9.81 m/s^2 and R = 8.314 J/(mol K) are standard constants.")
    print("=" * 72)


if __name__ == "__main__":
    main()
