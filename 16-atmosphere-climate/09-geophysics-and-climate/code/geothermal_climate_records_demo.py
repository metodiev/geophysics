#!/usr/bin/env python3
"""Borehole temperature records of past climate: the forward problem of heat
conduction into the ground, the low-pass filtering of the surface history with
depth, and the ill-posed inverse problem of recovering that history.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python geothermal_climate_records_demo.py

Everything is SYNTHETIC.  The thermal properties, the surface history, the
profile noise and the depth range are chosen teaching values.  No real borehole,
site, measurement or published reconstruction is used.

Contents
--------
1. The forward problem: a surface step and its erfc signature at depth.
2. Diffusion as a low-pass filter: e-folding depth versus period.
3. A synthetic surface history and the noisy borehole profile it produces.
4. Unregularised inversion: why it explodes.
5. Truncated-SVD inversion: the resolution/noise trade-off, measured.
6. Non-uniqueness: the null-space direction and its amplification factor.
7. What a borehole record does and does not determine.
"""

import numpy as np
from scipy.special import erfc

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC thermal setting (chosen, not measured) -----------------------
KAPPA = 1.0e-6             # m^2/s, thermal diffusivity (a chosen rock value)
SEC_PER_YEAR = 365.25 * 24.0 * 3600.0
DEPTHS = np.arange(20.0, 320.0, 10.0)      # m, measurement depths
NOISE_K = 0.02             # K, profile measurement noise
HISTORY_YEARS = 300.0      # yr, the period we try to reconstruct
TRUE_GRADIENT = 0.025      # K/m, geothermal gradient (subtracted before analysis)


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def step_response(z_m, age_yr):
    """Temperature perturbation at depth z from a unit surface step at age_yr.

    The Green's function for the heat equation with a surface step is
    erfc(z / (2 sqrt(kappa t))); at age 0 the response is zero everywhere below
    the surface.
    """
    z_m = np.asarray(z_m, dtype=float)
    if age_yr <= 0.0:
        return np.zeros_like(z_m)
    u = z_m / (2.0 * np.sqrt(KAPPA * age_yr * SEC_PER_YEAR))
    return erfc(u)


def pulse_matrix(depths_m, edges_yr):
    """Green's function matrix for piecewise-constant bins in time.

    Bin i covers ages [edges[i+1], edges[i]]: a rectangular pulse in time is the
    difference of two steps.
    """
    G = np.zeros((depths_m.size, edges_yr.size - 1))
    for i in range(edges_yr.size - 1):
        G[:, i] = (step_response(depths_m, edges_yr[i])
                   - step_response(depths_m, edges_yr[i + 1]))
    return G


def true_history(edges_yr):
    """Synthetic surface history: linear cooling into the past (K)."""
    mids = 0.5 * (edges_yr[:-1] + edges_yr[1:])
    return -0.010 * mids


def tsvd(G, d, k):
    """Truncated-SVD solution using the k largest singular components."""
    U, s, Vt = np.linalg.svd(G, full_matrices=False)
    coeff = (U.T @ d)[:k] / s[:k]
    return Vt[:k].T @ coeff, s


def main():
    section("1. The forward problem: a surface step and its depth signature")
    print(f"  thermal diffusivity kappa = {KAPPA:.1e} m^2/s (chosen)")
    print("  a unit step in surface temperature produces a perturbation")
    print("  T(z) = erfc( z / (2 sqrt(kappa t)) ) at depth z after time t")
    print("   z (m)   response at 10 yr   100 yr   1000 yr")
    for z in (10.0, 50.0, 100.0, 200.0, 300.0):
        vals = [step_response(z, t) for t in (10.0, 100.0, 1000.0)]
        print(f"  {z:6.0f}   {vals[0]:14.4f}   {vals[1]:7.4f}   {vals[2]:8.4f}")
    print("  A recent change is confined to shallow depths; an old change has")
    print("  penetrated deeper.  That is the basis of borehole climatology --")
    print("  and the reason its time resolution degrades into the past.")

    section("2. Diffusion as a low-pass filter: e-folding depth versus period")
    print("  for a surface oscillation of period P the amplitude decays as")
    print("  exp(-z/d) with d = sqrt(kappa P / pi)")
    print("  period       e-folding depth (m)")
    for P in (1.0, 10.0, 100.0, 1000.0):
        d = np.sqrt(KAPPA * P * SEC_PER_YEAR / np.pi)
        print(f"  {P:6.0f} yr   {d:18.2f}")
    print("  The annual cycle is gone within a few metres; the century scale")
    print("  reaches tens of metres.  A borehole profile is a low-pass-filtered")
    print("  record of surface temperature: it resolves century-scale change and")
    print("  cannot resolve interannual wiggles.")

    section("3. A synthetic surface history and the profile it produces")
    edges = np.linspace(0.0, HISTORY_YEARS, 7)     # 6 bins of 50 yr
    G = pulse_matrix(DEPTHS, edges)
    truth_bins = true_history(edges)
    clean = G @ truth_bins
    observed = clean + NOISE_K * RNG.standard_normal(DEPTHS.size)
    print(f"  history period {HISTORY_YEARS:.0f} yr in 6 bins of 50 yr")
    print("  true bin values (K, anomaly relative to present):")
    print("    " + "  ".join(f"{v:+.2f}" for v in truth_bins))
    print(f"  profile depths {DEPTHS[0]:.0f}-{DEPTHS[-1]:.0f} m, "
          f"{DEPTHS.size} points, noise sd {NOISE_K:.2f} K")
    print(f"  the geothermal gradient {TRUE_GRADIENT:.3f} K/m is removed first:")
    print(f"    at {DEPTHS[-1]:.0f} m it contributes {TRUE_GRADIENT * DEPTHS[-1]:.2f} K, "
          f"the perturbation only {clean.max():.2f} K")
    print("  so the reconstruction depends on a gradient that is itself")
    print("  estimated, often from the deepest part of the same profile.")

    section("4. Unregularised inversion: why it explodes")
    h_raw = np.linalg.lstsq(G, observed, rcond=None)[0]
    s = np.linalg.svd(G, compute_uv=False)
    print(f"  ordinary least squares on {G.shape[0]} depths and "
          f"{G.shape[1]} bins")
    print(f"  recovered bins (K): "
          + "  ".join(f"{v:+.1f}" for v in h_raw))
    print(f"  largest magnitude {np.abs(h_raw).max():.1f} K against a true")
    print(f"  history whose largest value is {np.abs(truth_bins).max():.2f} K")
    print(f"  condition number of the design matrix: {s[0] / s[-1]:.2e}")
    print("  The fit is excellent and the answer is meaningless: the small")
    print("  singular values amplify the profile noise without limit.  This is")
    print("  what an ill-posed inverse problem looks like in numbers.")

    section("5. Truncated-SVD inversion: the resolution/noise trade-off")
    print("  singular values of the 6-bin design matrix:")
    print("    " + "  ".join(f"{v:.3f}" for v in s))
    print("   k    rms misfit (K)   rms bin error (K)   recovered bins (K)")
    for k in (1, 2, 3, 4, 5, 6):
        hk, _ = tsvd(G, observed, k)
        mis = np.linalg.norm(observed - G @ hk) / np.sqrt(observed.size)
        err = np.sqrt(np.mean((hk - truth_bins) ** 2))
        print(f"  {k:2d}   {mis:14.4f}   {err:18.3f}   "
              + " ".join(f"{v:+.2f}" for v in hk))
    best_k = int(np.argmin([np.sqrt(np.mean((tsvd(G, observed, k)[0]
                                             - truth_bins) ** 2))
                            for k in range(1, 7)])) + 1
    hb, _ = tsvd(G, observed, best_k)
    mis_b = np.linalg.norm(observed - G @ hb) / np.sqrt(observed.size)
    err_b = np.sqrt(np.mean((hb - truth_bins) ** 2))
    print(f"  the best truncation is k = {best_k}: its misfit ({mis_b:.4f} K) is")
    print(f"  at the noise level ({NOISE_K:.2f} K) and its rms bin error "
          f"({err_b:.3f} K)")
    print("  is the smallest of the row.  Beyond that, components lower the")
    print("  misfit by less than a few thousandths of a kelvin while the bin")
    print("  error grows: the extra detail is fitting the noise.  Choosing k is")
    print("  the regularisation choice, and it must be stated.")

    print("\n  more bins do not buy more information:")
    print("   bins   bin width (yr)   components above 0.01   rms bin error "
          "(k = 3)")
    for nb in (6, 9, 12, 18):
        e = np.linspace(0.0, HISTORY_YEARS, nb + 1)
        Gb = pulse_matrix(DEPTHS, e)
        tb = true_history(e)
        sb = np.linalg.svd(Gb, compute_uv=False)
        kk = int(np.sum(sb > 0.01))
        hk, _ = tsvd(Gb, observed, min(3, nb))
        err = np.sqrt(np.mean((hk - tb) ** 2))
        print(f"  {nb:5d}   {HISTORY_YEARS / nb:13.1f}   {kk:13d}   "
              f"{err:14.3f}")
    print("  the number of well-determined components saturates near 4-5, so")
    print("  refining the time grid past that only reshuffles the same")
    print("  information.  Resolution in time is bought by lowering the noise")
    print("  and by deeper profiles, not by adding parameters.")

    section("6. Non-uniqueness: the direction the data cannot see")
    print(f"  smallest retained component with k = 5 on the 6-bin matrix has")
    print(f"  singular value ~{s[4]:.4f}, so a profile error of {NOISE_K:.2f} K is")
    print(f"  amplified into a history error of order "
          f"{NOISE_K / s[4]:.1f} K along that direction:")
    U6, s6, V6 = np.linalg.svd(G, full_matrices=False)
    v5 = V6[4] / np.abs(V6[4]).max()
    print("    " + "  ".join(f"{v:+.2f}" for v in v5))
    change5 = np.linalg.norm(G @ v5) / np.sqrt(G.shape[0])
    print(f"  unit change along it alters the predicted profile by only")
    print(f"  {change5:.4f} K rms, well below the {NOISE_K:.2f} K noise: that is")
    print("  the practical non-uniqueness, and it is why the k = 5 row had")
    print("  kelvin-scale errors.")

    edges_f = np.linspace(0.0, HISTORY_YEARS, 13)
    Gf = pulse_matrix(DEPTHS, edges_f)
    U, sf, Vt = np.linalg.svd(Gf, full_matrices=False)
    v_null = Vt[-1] / np.abs(Vt[-1]).max()
    change = np.linalg.norm(Gf @ v_null) / np.sqrt(Gf.shape[0])
    print(f"\n  on a finer 12-bin grid the smallest singular value is "
          f"{sf[-1]:.2e},")
    print(f"  i.e. an exact null direction: a unit change along it alters the")
    print(f"  profile by {change:.1e} K rms, which the noise can never see.")
    print("  the pattern over the 12 bins:")
    print("    " + "  ".join(f"{v:+.2f}" for v in v_null))
    print("  Any reconstruction can be slid along these directions without")
    print("  spoiling the fit, so a borehole reconstruction must report an")
    print("  admitted set of histories, not a single curve.")

    section("7. What a borehole record does and does not determine")
    print("  determines : a low-pass filtered, vertically averaged surface")
    print("               temperature history, with resolution degrading into the")
    print("               past and a resolution/noise trade-off set by the")
    print("               profile noise.")
    print("  assumes    : pure conduction (no groundwater advection, no latent")
    print("               heat effects), a known constant thermal diffusivity, a")
    print("               horizontally uniform surface forcing, and a correctly")
    print("               removed geothermal gradient.")
    print("  does NOT   : resolve individual years, identify a cause, or separate")
    print("  determine    a change in air temperature from a change in snow")
    print("               cover, land use or groundwater flow.")
    print("  All numbers above are SYNTHETIC.")


if __name__ == "__main__":
    main()
