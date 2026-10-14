#!/usr/bin/env python3
"""Seismic refraction and surface waves for aquifers: the two-layer travel-time
curve and its crossover distance, the depth error from a velocity error, the
water table as a refractor, and the resolution/non-uniqueness of a Rayleigh-wave
dispersion curve.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python seismic_groundwater_demo.py

Everything is SYNTHETIC.  Velocities, thicknesses and noise are chosen teaching
values.  Print-only; no network access.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC refraction model ---------------------------------------------
V1 = 800.0        # m/s, dry / unsaturated layer
V2 = 2400.0       # m/s, saturated and compacted unit below
Z_TRUE = 12.0     # m, depth to the refractor

# --- SYNTHETIC Gassmann model (identical to aquifer_signatures_demo.py) ------
K_MIN, MU_MIN, RHO_MIN = 37.0e9, 44.0e9, 2650.0
K_DRY, MU_DRY, PHI = 1.0e9, 3.0e9, 0.30
K_AIR, K_WATER = 1.0e5, 2.2e9
RHO_AIR, RHO_WATER = 1.2, 1000.0


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def head_wave_times(x, v1, v2, z):
    """Direct and head-wave travel times (s) at offset x (m)."""
    theta_c = np.arcsin(v1 / v2)
    t_direct = x / v1
    t_head = x / v2 + 2.0 * z * np.cos(theta_c) / v1
    return t_direct, t_head


def crossover(v1, v2, z):
    """Offset at which the head wave overtakes the direct wave, in metres."""
    return 2.0 * z * np.sqrt((v2 + v1) / (v2 - v1))


def depth_from_crossover(xc, v1, v2):
    """Depth of a two-layer refractor from its crossover distance, in metres."""
    return 0.5 * xc * np.sqrt((v2 - v1) / (v2 + v1))


def gassmann_ksat(k_dry, k_min, k_fl, phi):
    num = (1.0 - k_dry / k_min) ** 2
    den = phi / k_fl + (1.0 - phi) / k_min - k_dry / k_min ** 2
    return k_dry + num / den


def vp_of(k_bulk, mu, rho):
    return np.sqrt((k_bulk + 4.0 / 3.0 * mu) / rho)


def vr_dispersion(freqs, vs_profile, depth_nodes, kernel_width=1.0):
    """Rayleigh phase velocity from the stated lambda/3 sampling model.

    v_R(f) is the kernel-weighted average of Vs(z) with a Gaussian kernel centred
    at z = lambda/3 and width lambda/6, where lambda = v_R / f.  This is an
    explicitly stated SYNTHETIC sampling model, not an exact dispersion relation.
    """
    vr = np.full(freqs.size, vs_profile[0])
    for _ in range(60):
        lam = vr / freqs
        centre = lam / 3.0
        width = np.maximum(lam / 6.0, 1.0e-6)
        dz = depth_nodes[1] - depth_nodes[0]
        w = np.exp(-0.5 * ((depth_nodes[None, :] - centre[:, None]) / width[:, None]) ** 2)
        w /= (w.sum(axis=1, keepdims=True) * dz)
        vr_new = (w * vs_profile[None, :]).sum(axis=1) * dz
        if np.max(np.abs(vr_new - vr)) < 1.0e-6:
            vr = vr_new
            break
        vr = vr_new
    return vr


def main():
    section("1. Two-layer refraction: crossover distance and depth recovery")
    theta_c = np.arcsin(V1 / V2)
    print(f"  SYNTHETIC model: v1 = {V1:.0f} m/s, v2 = {V2:.0f} m/s, "
          f"z = {Z_TRUE:.0f} m")
    print(f"  critical angle theta_c = asin(v1/v2) = {np.degrees(theta_c):.2f} deg, "
          f"cos(theta_c) = {np.cos(theta_c):.4f}")
    print("\n    offset x (m)   t_direct (ms)   t_head (ms)   first arrival")
    for x in (5.0, 10.0, 20.0, 40.0, 60.0, 100.0):
        td, th = head_wave_times(x, V1, V2, Z_TRUE)
        first = "head" if th < td else "direct"
        print(f"    {x:12.1f}   {td*1e3:13.3f}   {th*1e3:11.3f}   {first}")
    xc = crossover(V1, V2, Z_TRUE)
    print(f"\n  crossover distance x_c = {xc:.2f} m")
    print(f"  depth recovered from x_c: z = {depth_from_crossover(xc, V1, V2):.3f} m "
          f"(true {Z_TRUE:.1f} m)")
    t_i = 2.0 * Z_TRUE * np.cos(theta_c) / V1
    print(f"  intercept time t_i = {t_i*1e3:.3f} ms -> z = {t_i*V1/(2*np.cos(theta_c)):.3f} m")
    print("  Two independent routes to the same depth: a real check, because both")
    print("  come from the same picked times.")

    section("2. How much does a velocity error move the depth?")
    print("  depth from x_c;  +5% error injected into each velocity in turn")
    print("\n   v2/v1    z (m)    z if v1+5%   z if v2+5%   err(v1)   err(v2)")
    for v2 in (1000.0, 1200.0, 1600.0, 2400.0, 4000.0):
        xc = crossover(V1, v2, Z_TRUE)
        z0 = depth_from_crossover(xc, V1, v2)
        z1 = depth_from_crossover(xc, V1 * 1.05, v2)
        z2 = depth_from_crossover(xc, V1, v2 * 1.05)
        print(f"   {v2/V1:5.2f}   {z0:6.2f}   {z1:10.2f}   {z2:10.2f}   "
              f"{(z1/z0-1)*100:+6.2f}%   {(z2/z0-1)*100:+6.2f}%")
    print("\n  Near a velocity contrast of 1.25 a 5% velocity error moves the depth")
    print("  by more than 10%; at a contrast of 5 it moves it by 1%.  A shallow")
    print("  refraction depth is only as good as the velocity contrast is large.")

    section("3. The water table as a seismic refractor (Gassmann velocities)")
    rho_dry = (1 - PHI) * RHO_MIN + PHI * RHO_AIR
    rho_sat = (1 - PHI) * RHO_MIN + PHI * RHO_WATER
    vp_dry = vp_of(gassmann_ksat(K_DRY, K_MIN, K_AIR, PHI), MU_DRY, rho_dry)
    vp_sat = vp_of(gassmann_ksat(K_DRY, K_MIN, K_WATER, PHI), MU_DRY, rho_sat)
    print(f"  unsaturated Vp = {vp_dry:.0f} m/s, saturated Vp = {vp_sat:.0f} m/s, "
          f"contrast = {vp_sat/vp_dry:.3f}")
    if vp_sat > vp_dry:
        th = np.arcsin(vp_dry / vp_sat)
        print(f"  a head wave exists (v2 > v1); theta_c = {np.degrees(th):.2f} deg, "
              f"cos(theta_c) = {np.cos(th):.4f}")
        for wtd in (2.0, 5.0, 10.0):
            print(f"    water table at {wtd:5.1f} m -> crossover "
                  f"x_c = {crossover(vp_dry, vp_sat, wtd):7.2f} m")
    print("  A velocity INCREASE with saturation is what makes the water table a")
    print("  refractor.  Where the dry and saturated velocities are nearly equal the")
    print("  head wave is not generated, whatever the water table does.")

    section("4. Rayleigh dispersion: what the dispersion curve resolves")
    depth_nodes = np.arange(0.0, 60.0, 0.25)
    prof_a = np.where(depth_nodes < 10.0, 200.0, 400.0)          # sharp step
    prof_b = np.clip(200.0 + 20.0 * (depth_nodes - 5.0), 200.0, 400.0)  # gradient
    freqs = np.array([2.0, 4.0, 8.0, 16.0, 32.0])
    vr_a = vr_dispersion(freqs, prof_a, depth_nodes)
    vr_b = vr_dispersion(freqs, prof_b, depth_nodes)
    print("   f (Hz)   lambda (m)   v_R step (m/s)   v_R gradient (m/s)   difference")
    for f, va, vb in zip(freqs, vr_a, vr_b):
        lam = va / f
        print(f"   {f:6.1f}   {lam:10.1f}   {va:15.1f}   {vb:17.1f}   "
              f"{(vb/va-1)*100:+7.2f}%")
    print(f"\n  maximum difference between the sharp-step and gradient profiles = "
          f"{np.max(np.abs(vr_b/vr_a-1))*100:.2f}%")
    print("  A step and a gradient with the same average velocity differ by at most")
    print(f"  {np.max(np.abs(vr_b/vr_a-1))*100:.1f}% here, and only at 16 Hz; below 8 Hz they are the same")
    print("  curve.  Against 3-5% data noise the deep part of the profile is a family,")
    print("  not a single answer.")
    print("\n  Sampling depth per frequency (kernel centre = lambda/3):")
    for f, va in zip(freqs, vr_a):
        print(f"    f = {f:5.1f} Hz -> lambda/3 = {va/f/3:6.2f} m")

    section("5. Vs is nearly blind to saturation (unlike Vp)")
    vs_dry = np.sqrt(MU_DRY / rho_dry)
    vs_sat = np.sqrt(MU_DRY / rho_sat)
    print(f"  Vp: {vp_dry:6.0f} -> {vp_sat:6.0f} m/s  "
          f"({(vp_sat/vp_dry-1)*100:+.1f}%)")
    print(f"  Vs: {vs_dry:6.0f} -> {vs_sat:6.0f} m/s  "
          f"({(vs_sat/vs_dry-1)*100:+.1f}%)")
    print("  Surface-wave methods map Vs, which responds to the density change only;")
    print("  refraction maps Vp, which responds to the pore fluid.  A surface-wave")
    print("  survey is therefore a poor water-table tool and a good porosity tool.")
    print("\n  All models and data in this module are SYNTHETIC.")


if __name__ == "__main__":
    main()
