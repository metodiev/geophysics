#!/usr/bin/env python3
"""Airborne EM for regional aquifer mapping: the diffusion depth, the depth
sensitivity kernel and depth of investigation, the effect of survey altitude,
the conductance equivalence of a layered section, and the base-rate logic of
interpreting a conductivity anomaly.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python airborne_groundwater_demo.py

Everything is SYNTHETIC: the section, the system geometry and the noise level are
chosen teaching values.  The forward model is a stated 1-D diffusion-kernel
approximation, not a real system's response.  Print-only; no network access.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

MU0 = 4.0e-7 * np.pi       # H/m (standard constant)
LOOP_RADIUS = 10.0         # m, synthetic transmitter loop radius
NOISE = 0.02               # stated relative noise floor of the system
SIGMA_REF = 0.20           # S/m, reference conductivity setting the diffusion rate


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def diffusion_depth(rho_ohm_m, t_s):
    """Depth of maximum sensitivity of a step in a uniform conductor, metres."""
    return np.sqrt(2.0 * rho_ohm_m * t_s / MU0)


def kernel(z, t, sigma_s_m):
    """1-D diffusion sensitivity kernel, normalised so that its integral is 1."""
    d = 1.0 / (MU0 * sigma_s_m)              # m^2/s
    return z / (2.0 * d * t) * np.exp(-z ** 2 / (4.0 * d * t))


def apparent_conductivity(t, z_nodes, sigma_layers, sigma_ref):
    dz = z_nodes[1] - z_nodes[0]
    return np.sum(sigma_layers * kernel(z_nodes, t, sigma_ref)) * dz


def kernel_fraction(t, z_nodes, lo, hi, sigma_ref):
    """Fraction of the kernel's weight inside the depth interval [lo, hi)."""
    dz = z_nodes[1] - z_nodes[0]
    k = kernel(z_nodes, t, sigma_ref) * dz
    return k[(z_nodes >= lo) & (z_nodes < hi)].sum()


def coupling(h, z):
    """Synthetic geometric coupling of a loop at height h to a layer at depth z."""
    return 1.0 / ((h + z) ** 2 + LOOP_RADIUS ** 2) ** 1.5


def main():
    section("1. Diffusion depth: the depth an airborne system can see at time t")
    factor = np.sqrt(2.0 / MU0)
    print(f"d(t) = sqrt(2 rho t / mu0) = {factor:.1f} * sqrt(rho * t)  "
          f"[rho in ohm m, t in s, d in m]")
    print("\n   rho (ohm m)   t = 0.1 ms   t = 1 ms   t = 10 ms   t = 100 ms")
    for rho in (10.0, 30.0, 100.0):
        row = "   ".join(f"{diffusion_depth(rho, t):10.1f}"
                         for t in (1e-4, 1e-3, 1e-2, 1e-1))
        print(f"   {rho:11.1f}   {row}")
    print("\n  At 1 ms a 10 ohm m conductor is probed near 126 m and a 100 ohm m")
    print("  resistor near 399 m; at 10 ms the same material is probed four times")
    print("  deeper.  Later gates probe deeper and average over a wider window.")

    section("2. The sensitivity kernel: a moving, finite window")
    z_nodes = np.arange(0.0, 4000.0, 1.0)
    dz = z_nodes[1] - z_nodes[0]
    for t in (1e-4, 1e-3, 1e-2):
        k = kernel(z_nodes, t, SIGMA_REF)
        print(f"  t = {t*1e3:6.2f} ms: integral over 0-4000 m = {k.sum()*dz:.5f}, "
              f"peak at z = {z_nodes[k.argmax()]:6.1f} m, "
              f"diffusion depth = {diffusion_depth(1/SIGMA_REF, t):6.1f} m")
    print("  The kernel is not a depth probe but a window of finite width.  Whatever")
    print("  the ground does at two to three times the peak depth is still averaged in,")
    print("  so a deep anomaly biases an apparent conductivity read at early time.")

    section("3. Apparent conductivity of a layered section (SYNTHETIC 1-D model)")
    sigma_top, sigma_mid, sigma_base = 0.02, 0.40, 0.02     # S/m
    top_base, mid_base = 10.0, 30.0
    sigma_layers = np.where(z_nodes < top_base, sigma_top,
                            np.where(z_nodes < mid_base, sigma_mid, sigma_base))
    times = np.array([5e-5, 1e-4, 3e-4, 1e-3, 3e-3, 1e-2, 3e-2])
    print(f"  section: {sigma_top:.2f} S/m to {top_base:.0f} m, "
          f"{sigma_mid:.2f} S/m to {mid_base:.0f} m, then {sigma_base:.2f} S/m")
    print("\n     t (ms)   peak depth (m)   kernel in target   sigma_a (S/m)")
    for t in times:
        sa = apparent_conductivity(t, z_nodes, sigma_layers, SIGMA_REF)
        frac = kernel_fraction(t, z_nodes, top_base, mid_base, SIGMA_REF)
        print(f"   {t*1e3:7.3f}   {diffusion_depth(1/SIGMA_REF, t):14.1f}   "
              f"{frac:16.4f}   {sa:13.4f}")
    print("\n  As the window moves past the target the apparent conductivity falls back")
    print("  to the background: sigma_a(t) is a weighted average, and its value alone")
    print("  does not give the target's conductivity or its depth.")

    section("4. Depth of investigation and the cost of altitude")
    print("  depth below which less than 30% of the kernel's weight lies:")
    for t in (1e-4, 1e-3, 1e-2):
        d = diffusion_depth(1 / SIGMA_REF, t)
        doi = np.sqrt(4.0 * (1.0 / (MU0 * SIGMA_REF)) * t * np.log(1.0 / 0.3))
        print(f"    t = {t*1e3:6.2f} ms -> DOI = {doi:6.1f} m "
              f"({doi/d:.2f} x the diffusion depth)")
    print("\n  altitude effect: synthetic loop coupling to a layer at depth z,")
    print("  normalised to the surface layer under a 30 m survey altitude")
    print("\n   depth z (m)   h=30 m   h=60 m   h=90 m   h=120 m")
    for z in (0.0, 20.0, 50.0, 100.0):
        row = "   ".join(f"{coupling(h, z)/coupling(30.0, 0.0):.4f}"
                         for h in (30.0, 60.0, 90.0, 120.0))
        print(f"   {z:11.1f}   {row}")
    print(f"\n  deepest layer whose coupling still exceeds 3 x the {NOISE:.0%} noise:")
    for h in (30.0, 60.0, 90.0, 120.0):
        det = [z for z in np.arange(0.0, 400.0, 1.0)
               if coupling(h, z) / coupling(30.0, 0.0) > 3.0 * NOISE]
        print(f"    altitude {h:5.0f} m -> depth limit "
              f"{max(det) if det else 0.0:6.0f} m")
    print("  Flying higher buys coverage and costs signal: at 120 m the coupling to a")
    print("  near-surface conductor is ~2% of its 30 m value, below this system's noise.")
    print("  Altitude is exchanged for penetration, and paying it back needs a larger")
    print("  transmitter moment, not a better interpretation.")

    section("5. Equivalence: the same conductance, two different sections")
    print("  two models with the same conductance S = sigma * h in the same window")
    print("  A: 20 m of 0.10 S/m (S = 2.0 S)   B: 5 m of 0.40 S/m (S = 2.0 S)")

    def sigma_a(t, thick, sigma):
        prof = np.where((z_nodes >= 10.0) & (z_nodes < 10.0 + thick), sigma, 0.02)
        return apparent_conductivity(t, z_nodes, prof, SIGMA_REF)

    print("\n     t (ms)   A (S/m)   B (S/m)   difference")
    for t in times:
        sa = sigma_a(t, 20.0, 0.10)
        sb = sigma_a(t, 5.0, 0.40)
        print(f"   {t*1e3:7.3f}   {sa:7.4f}   {sb:7.4f}   {(sb/sa-1)*100:+7.2f}%")
    diffs = [(t, abs(sigma_a(t, 5.0, 0.40) / sigma_a(t, 20.0, 0.10) - 1.0))
             for t in times]
    worst_t, worst = max(diffs, key=lambda p: p[1])
    print(f"\n  largest difference = {worst*100:.1f}% at t = {worst_t*1e3:.3f} ms; "
          f"the system noise is {NOISE:.0%}")
    print("  Where the two curves agree to within the noise, the thickness and the")
    print("  conductivity cannot be separated: only their product, the conductance S,")
    print("  is resolved.  That is why AEM products are quoted as conductance maps.")

    section("6. From anomaly to decision: the base rate dominates")
    prior = 0.08               # stated prior: 8% of conductive AEM anomalies are aquifers
    tpr = 0.80                 # P(saline signature | usable aquifer)
    fpr = 0.30                 # P(saline signature | clay, no aquifer)
    post = prior * tpr / (prior * tpr + (1.0 - prior) * fpr)
    print(f"  prior P(usable aquifer) = {prior:.2f}")
    print(f"  P(conductive anomaly | aquifer) = {tpr:.2f}; "
          f"P(conductive anomaly | clay) = {fpr:.2f}")
    print(f"  posterior P(aquifer | conductive anomaly) = {post:.3f}")
    print(f"  of every 100 conductive anomalies, {post*100:.0f} are aquifers and "
          f"{(1-post)*100:.0f} are clay:")
    print("  the test is informative, and four fifths of the anomalies are still clay.")
    for pri in (0.02, 0.20, 0.50):
        p = pri * tpr / (pri * tpr + (1 - pri) * fpr)
        print(f"    with prior {pri:.2f} -> posterior {p:.3f}")
    print("  A geophysical anomaly is not a resource.  Its meaning is set by the")
    print("  prior, and the prior is set by the regional geology, not by the survey.")
    print("\n  All models and data in this module are SYNTHETIC.")


if __name__ == "__main__":
    main()
