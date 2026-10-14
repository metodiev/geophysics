"""Non-uniqueness of geophysical models: two different sources, one data set.

The single most important fact in forward modelling: a finite, noisy, band-
limited data set does NOT determine the source.  This script demonstrates it
three ways, all in the simplest possible setting -- the gravity field of a
sheet of mass in a 2D (x, z) world, infinite in y.

2D geometry: an infinite sheet (line in y) at depth d with surface density
sigma(x) in kg/m^2 produces the vertical attraction

    g_z(x) = 2 G * integral  sigma(x') d / ((x-x')^2 + d^2) dx'      [m/s^2]

which is just the line-mass formula 2 G lambda d / (x^2 + d^2) summed over
lines.  (Derived by integrating one coordinate; see the lesson.)

Convention: z positive downward; the sheet is below the observers; the
observers sit on z = 0.

Run:  python3 annihilator_nonuniqueness_demo.py
"""

from __future__ import annotations

import numpy as np

G = 6.67430e-11  # m^3 kg^-1 s^-2, CODATA 2018 (NIST)
MGAL = 1.0e-5    # m/s^2 per mGal


def kernel_matrix(x_obs, x_src, depth, dx_src):
    """Matrix K with g = K @ sigma for a sheet at the given depth.

    K[i, j] = 2 G * depth / ((x_obs[i] - x_src[j])^2 + depth^2) * dx_src
    Units: [G]=m^3 kg^-1 s^-2, [depth]=m, [x]^2=m^2, [dx]=m
           => K has units m^3 kg^-1 s^-2, and K @ sigma has units
              m^3 kg^-1 s^-2 * kg m^-2 = m s^-2.  Correct.
    """
    dx = x_obs[:, None] - x_src[None, :]
    return 2.0 * G * depth / (dx**2 + depth**2) * dx_src


def gaussian_sheet(x, centre, width, total_mass):
    """A Gaussian surface density in kg/m^2 carrying a stated total mass."""
    sigma = np.exp(-0.5 * ((x - centre) / width) ** 2)
    sigma *= total_mass / (np.sqrt(2.0 * np.pi) * width)
    return sigma


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def main() -> None:
    rng = np.random.default_rng(20240514)

    # --- SYNTHETIC experiment design (all numbers chosen, all labelled) -----
    span = 12_000.0          # m, horizontal extent of the model
    n_src = 400              # source cells on the sheet
    x_src = np.linspace(-span / 2, span / 2, n_src)
    dx_src = x_src[1] - x_src[0]
    n_obs = 120              # observation points (a sparse survey line)
    x_obs = np.linspace(-span / 2, span / 2, n_obs)

    depth_true = 300.0       # m  (the model we declare "true")
    width_true = 400.0       # m  Gaussian half-width of the true sheet
    mass_true = 1.0e10       # kg per unit y-length

    sigma_true = gaussian_sheet(x_src, 0.0, width_true, mass_true)
    K_true = kernel_matrix(x_obs, x_src, depth_true, dx_src)
    g_true = K_true @ sigma_true
    print("SYNTHETIC model: Gaussian sheet, depth 300 m, width 400 m,")
    print(f"  total mass {mass_true:.1e} kg per metre of strike length.")
    print(f"  grid: {n_src} source cells over {span/1000:.0f} km; "
          f"{n_obs} observation points.")
    print(f"  peak synthetic gravity = {g_true.max()/MGAL:.6f} mGal")

    # ------------------------------------------------------------------
    section("1. Equivalent source at a DIFFERENT depth fits the same data")
    # Suppose the survey is sparse (n_obs=120) and we model the source on a
    # fine grid (n_src=400).  The system is underdetermined: infinitely many
    # sheet densities reproduce the data.  Take two shallow/deep grids and fit
    # the SAME synthetic data with each.
    for depth_test in (100.0, 600.0):
        K = kernel_matrix(x_obs, x_src, depth_test, dx_src)
        sigma_fit, *_ = np.linalg.lstsq(K, g_true, rcond=None)
        resid = K @ sigma_fit - g_true
        rel_resid = np.linalg.norm(resid) / np.linalg.norm(g_true)
        rel_model = (np.linalg.norm(sigma_fit - sigma_true)
                     / np.linalg.norm(sigma_true))
        print(f"  assumed depth {depth_test:6.0f} m : data misfit "
              f"||K m - g||/||g|| = {rel_resid:.3e} ; "
              f"||m - m_true||/||m_true|| = {rel_model:.3f}")
    print("  Two models at depths 100 m and 600 m both explain the data to")
    print("  machine precision, yet differ from each other and from the truth.")
    print("  The data alone cannot select a depth without extra constraints.")

    # ------------------------------------------------------------------
    section("2. An exact discrete null-space vector (an 'annihilator')")
    # Any vector n with K n = 0 can be added to a model without changing the
    # data.  For n_src > n_obs such vectors exist by linear algebra.  Build
    # one as the right singular vector of K with the smallest singular value.
    K = kernel_matrix(x_obs, x_src, depth_true, dx_src)
    U, s, Vt = np.linalg.svd(K, full_matrices=True)
    n_null = Vt[-1]                     # in the null space of K (n_src columns)
    defect = np.linalg.norm(K @ n_null) / (s[0] * np.linalg.norm(n_null))
    print(f"  matrix shape {K.shape[0]} x {K.shape[1]} (observations x cells)")
    print(f"  nonzero singular values with sigma > 1e-12*sigma_max: "
          f"{int(np.sum(s > 1e-12 * s[0]))}")
    print(f"  null-space dimension >= {K.shape[1] - np.sum(s > 1e-12 * s[0])}")
    print(f"  ||K n_null|| / (sigma_max ||n_null||) = {defect:.3e}")
    print("  -> adding n_null changes the model but not the data.")
    # Demonstrate the effect on an interpretation: mass is redistributed.
    lam = 0.6 * np.linalg.norm(sigma_true) / np.linalg.norm(n_null)
    sigma_alt = sigma_true + lam * n_null
    g_alt = K @ sigma_alt
    print(f"  ||g(K m_true) - g(K m_true + n_null)||/||g|| = "
          f"{np.linalg.norm(g_alt - g_true)/np.linalg.norm(g_true):.3e}")
    print(f"  total mass of m_true = {np.sum(sigma_true)*dx_src:.4e} kg/m")
    print(f"  total mass of alternative = {np.sum(sigma_alt)*dx_src:.4e} kg/m")

    # ------------------------------------------------------------------
    section("3. Why deeper equivalents are unstable (with measurement noise)")
    # Invert noisy data for sources at increasing depth.  The operator
    # 1/e^{-|k|d} amplifies high wavenumbers, so deep models explode.
    noise_level = 0.02 * MGAL            # 0.02 mGal, a real repeatability
    g_noisy = g_true + rng.normal(0.0, noise_level, g_true.shape)
    print(f"  additive white noise, sigma = {noise_level/MGAL:.3f} mGal")
    print("   depth(m)   cond(K)      model RMS (kg/m^2)   data misfit")
    for depth_test in (50.0, 100.0, 300.0, 600.0, 1200.0):
        K = kernel_matrix(x_obs, x_src, depth_test, dx_src)
        sigma_fit, *_ = np.linalg.lstsq(K, g_noisy, rcond=None)
        cond = np.linalg.cond(K)
        rms = np.sqrt(np.mean(sigma_fit**2))
        misfit = np.linalg.norm(K @ sigma_fit - g_noisy) / np.linalg.norm(g_noisy)
        print(f"  {depth_test:8.0f}   {cond:9.2e}   {rms:16.4e}   {misfit:.3e}")
    print("  All five fit the noisy data equally well, but the deeper models")
    print("  oscillate violently and carry huge, physically absurd densities.")
    print("  Fitting the data is NOT evidence that a model is meaningful.")

    print("\nSUMMARY: the observations are a finite, noisy, band-limited set;")
    print("they constrain the field, not the source.  Regularisation and prior")
    print("information -- not the data -- choose among equivalent models.")


if __name__ == "__main__":
    main()
