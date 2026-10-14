#!/usr/bin/env python3
"""EM and ERT for groundwater: skin depth, the exact two-layer Schlumberger
sounding curve, the ambiguity valley of a layered-earth inversion, the depth of
investigation, and the salinity/porosity degeneracy of an ERT image.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python em_and_ert_groundwater_demo.py

Everything is SYNTHETIC: the resistivities, layer thicknesses and noise level
below are chosen teaching values.  Print-only; no network access.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

MU0 = 4.0e-7 * np.pi      # H/m, vacuum permeability (standard constant)

# --- SYNTHETIC survey settings ----------------------------------------------
RHO1_TRUE = 50.0          # ohm m, layer 1 (e.g. dry sand / gravel)
RHO2_TRUE = 10.0          # ohm m, layer 2 (e.g. saturated sand, clay-rich)
H1_TRUE = 8.0             # m, thickness of layer 1
NOISE_FRAC = 0.03         # 3% relative data noise, a stated survey quality


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def skin_depth(rho_ohm_m, f_hz):
    """Diffusive skin depth sqrt(2 rho / (omega mu0)) in metres."""
    return np.sqrt(2.0 * rho_ohm_m / (2.0 * np.pi * f_hz * MU0))


def rho_a_two_layer(ab2, rho1, rho2, h1, n_terms=400):
    """Schlumberger apparent resistivity for a two-layer earth.

    Classical image-series result (AB/2 = ab2, small MN):

        rho_a = rho1 [ 1 + 2 sum_{n>=1} k^n / (1 + (2 n h1 / ab2)^2)^{3/2} ]

    with k = (rho2 - rho1)/(rho2 + rho1).
    """
    k = (rho2 - rho1) / (rho2 + rho1)
    n = np.arange(1, n_terms + 1)
    term = k ** n / (1.0 + (2.0 * n * h1 / ab2) ** 2) ** 1.5
    return rho1 * (1.0 + 2.0 * term.sum())


def main():
    section("1. Diffusive skin depth: how deep an EM measurement looks")
    factor = 1.0 / np.sqrt(np.pi * MU0)
    print(f"delta = sqrt(2 rho /(omega mu0)) = {factor:.2f} * sqrt(rho / f)  [m]")
    print("\n   rho (ohm m)   f = 1 Hz   f = 10 Hz   f = 100 Hz   f = 1000 Hz")
    for rho in (10.0, 50.0, 100.0, 500.0):
        row = "   ".join(f"{skin_depth(rho, f):9.1f}" for f in (1.0, 10.0, 100.0, 1000.0))
        print(f"   {rho:11.1f}   {row}")
    print("\n  Depth scales as sqrt(rho): doubling resistivity does not double")
    print("  depth, while a 100x frequency increase cuts it by 10x.")

    section("2. Check the two-layer Schlumberger series against its asymptotes")
    print(f"  SYNTHETIC model: rho1 = {RHO1_TRUE:.0f} ohm m, rho2 = {RHO2_TRUE:.0f} "
          f"ohm m, h1 = {H1_TRUE:.0f} m")
    print("  k = (rho2-rho1)/(rho2+rho1) = "
          f"{(RHO2_TRUE - RHO1_TRUE) / (RHO2_TRUE + RHO1_TRUE):+.4f}")
    small = rho_a_two_layer(0.01, RHO1_TRUE, RHO2_TRUE, H1_TRUE)
    large = rho_a_two_layer(2.0e5, RHO1_TRUE, RHO2_TRUE, H1_TRUE)
    partial = rho_a_two_layer(20.0, RHO1_TRUE, RHO2_TRUE, H1_TRUE, n_terms=6)
    full = rho_a_two_layer(20.0, RHO1_TRUE, RHO2_TRUE, H1_TRUE, n_terms=400)
    print(f"\n  AB/2 = 0.01 m (very small): rho_a = {small:.4f} ohm m  "
          f"(expect rho1 = {RHO1_TRUE:.0f})")
    print(f"  AB/2 = 2e5 m  (very large): rho_a = {large:.4f} ohm m  "
          f"(expect rho2 = {RHO2_TRUE:.0f})")
    print(f"  series convergence at AB/2 = 20 m: 6 terms {partial:.6f}, "
          f"400 terms {full:.6f}  (difference {abs(partial-full):.2e})")

    section("3. The admitted set: how many models fit one sounding?")
    spac = np.logspace(0.3, 2.4, 14)                       # AB/2 in metres
    data = np.array([rho_a_two_layer(s, RHO1_TRUE, RHO2_TRUE, H1_TRUE) for s in spac])
    data_noisy = data * (1.0 + NOISE_FRAC * RNG.standard_normal(spac.size))
    print(f"  {spac.size} soundings from AB/2 = {spac[0]:.1f} to {spac[-1]:.1f} m, "
          f"with {NOISE_FRAC*100:.0f}% relative noise")
    print(f"  data span rho_a = {data_noisy.min():.2f} to {data_noisy.max():.2f} ohm m")

    rho2_grid = np.exp(np.linspace(np.log(3.0), np.log(80.0), 90))
    h1_grid = np.linspace(2.0, 25.0, 120)

    def admitted(rho2_g, h1_g, spac_use, label):
        d = np.array([rho_a_two_layer(s, RHO1_TRUE, RHO2_TRUE, H1_TRUE) for s in spac_use])
        dn = d * (1.0 + NOISE_FRAC * RNG.standard_normal(spac_use.size))
        chi2 = np.empty((rho2_g.size, h1_g.size))
        for i, r2 in enumerate(rho2_g):
            for j, hh in enumerate(h1_g):
                m = np.array([rho_a_two_layer(s, RHO1_TRUE, r2, hh) for s in spac_use])
                chi2[i, j] = np.sum(((m - dn) / (NOISE_FRAC * d)) ** 2)
        # 68% confidence region for two parameters around the weighted minimum.
        ok = chi2 <= chi2.min() + 2.30
        r2_acc = rho2_g[ok.any(axis=1)]
        h1_acc = h1_g[ok.any(axis=0)]
        print(f"\n  {label}: {spac_use.size} soundings, AB/2 = {spac_use[0]:.1f} to "
              f"{spac_use[-1]:.1f} m")
        print(f"    admitted models: {ok.sum()} of {ok.size}  (chi^2 <= chi^2_min + 2.30)")
        print(f"    rho2 admitted: {r2_acc.min():6.1f} to {r2_acc.max():6.1f} ohm m")
        print(f"    h1   admitted: {h1_acc.min():6.1f} to {h1_acc.max():6.1f} m  "
              f"(truth {H1_TRUE:.1f} m)")
        return h1_acc.max() - h1_acc.min()

    wide = admitted(rho2_grid, h1_grid, spac, "wide spacing range")
    narrow = admitted(rho2_grid, h1_grid, spac[spac <= 20.0], "short spacing range")
    print(f"\n  the admitted depth range grows from {wide:.1f} m to {narrow:.1f} m when the")
    print("  short spacings that see the first layer are dropped: resolution is set by")
    print("  the ACQUISITION, not only by the physics.")

    jac = np.zeros((spac.size, 2))
    step_r, step_h = 0.5, 0.2
    base = np.array([rho_a_two_layer(s, RHO1_TRUE, RHO2_TRUE, H1_TRUE) for s in spac])
    dr = np.array([rho_a_two_layer(s, RHO1_TRUE, RHO2_TRUE + step_r, H1_TRUE)
                   for s in spac])
    dh = np.array([rho_a_two_layer(s, RHO1_TRUE, RHO2_TRUE, H1_TRUE + step_h)
                   for s in spac])
    jac[:, 0] = (dr - base) / step_r * RHO2_TRUE / base
    jac[:, 1] = (dh - base) / step_h * H1_TRUE / base
    u, sv, vt = np.linalg.svd(jac, full_matrices=False)
    print(f"\n  log-sensitivity Jacobian (relative change of rho_a per relative change")
    print(f"  of rho2 and h1): singular values {sv[0]:.3f} and {sv[1]:.3f}, "
          f"condition number {sv[0]/sv[1]:.2f}")
    print(f"  least-determined direction (d ln rho2, d ln h1) = "
          f"({vt[-1, 0]:+.3f}, {vt[-1, 1]:+.3f})")
    print("  a positive rho2 perturbation must be paired with a negative h1 one:")
    print("  the data prefer the product rho2 * h1 (a transverse resistance) over either.")

    section("4. Depth of investigation: where the sounding is most sensitive")
    L = 100.0                                # AB/2 of the largest spread, m
    depths = np.linspace(1.0, 250.0, 500)
    for contrast in (2.0, 5.0):
        rho2 = RHO1_TRUE * contrast
        sens = []
        for hh in depths:
            step = 0.5
            up = rho_a_two_layer(L, RHO1_TRUE, rho2, hh + step)
            dn = rho_a_two_layer(L, RHO1_TRUE, rho2, hh - step)
            base = rho_a_two_layer(L, RHO1_TRUE, rho2, hh)
            sens.append(abs((up - dn) / (2.0 * step)) * hh / base)
        sens = np.array(sens)
        peak = depths[sens.argmax()]
        below = np.where(sens < 0.1 * sens.max())[0]
        doi = depths[below[below > sens.argmax()][0]] if (below > sens.argmax()).any() else np.nan
        print(f"  rho2/rho1 = {contrast:3.1f}, AB/2 = {L:.0f} m:")
        print(f"    most sensitive to a boundary at h1 = {peak:6.1f} m")
        print(f"    sensitivity falls to 10% of its peak at h1 = {doi:6.1f} m "
              f"(the spreading-limited depth of investigation)")
    print("\n  The depth of investigation is a property of the survey (its largest AB/2)")
    print("  and of the stated sensitivity level, not of the ground alone.")

    section("5. One conductivity, two interpretations (ERT sees sigma, not salinity)")
    sigma_b = 0.05                                  # S/m, the measured bulk value
    print(f"  measured bulk conductivity: sigma_b = {sigma_b:.2f} S/m "
          f"= {1.0/sigma_b:.1f} ohm m")
    for sigma_w, name in ((0.5, "brackish"), (4.0, "saline")):
        phi = np.sqrt(sigma_b / sigma_w)
        print(f"  sigma_b = {sigma_b:.2f} S/m could be {name:8s} water at phi = {phi:.3f}")
    print("  ERT measures bulk conductivity.  Salinity, porosity and clay content")
    print("  enter through different exponents, so the image alone cannot separate them:")
    print("  a drilling/water-sample constraint is what converts conductivity to salinity.")
    print("\n  All models and data in this module are SYNTHETIC.")

if __name__ == "__main__":
    main()
