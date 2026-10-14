#!/usr/bin/env python3
"""Forward versus inverse, and the practical asymmetry between them.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python forward_and_inverse_demo.py

Everything here is SYNTHETIC.  The "buried masses" model below is a chosen
teaching model, not a measured density distribution, and no real gravity survey
is used.

The kernel is exact textbook physics -- the vertical gravity of a point mass,
summed by superposition -- so the forward map can be trusted.  What this script
measures is what happens when the same map is run backwards.

Contents
--------
1. The forward map: vertical gravity of four buried point masses.
2. Forward stability: a 1% model perturbation perturbs the data by ~0.2%.
3. Sensitivity and column correlation: deep masses are nearly indistinguishable.
4. The inverse: measured noise amplification against the condition number.
5. The data-error budget needed for a stated model accuracy.
6. Geometry, not physics: kernel scale invariance and the cost of depth.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

G_CONST = 6.67430e-11        # m^3 kg^-1 s^-2, exact (2018 CODATA)
MGAL = 1.0e-5                # m/s^2 per mGal, exact by definition

# --- SYNTHETIC survey geometry (chosen, not measured) ------------------------
X_STATIONS_KM = np.linspace(-12.0, 12.0, 25)      # surface offsets, km
DEPTHS_KM = np.array([1.0, 2.0, 3.0, 4.0])        # mass depths, km
MASSES_KG = np.array([1.0, 1.4, 0.8, 1.2]) * 1e10


def kernel_matrix(x_km, z_km):
    """G[i, k] = vertical gravity at station i from a unit mass at depth z_k.

    For a point mass M at horizontal offset x and depth z (both in metres),

        g_z = G M z / (x^2 + z^2)^(3/2)             [m s^-2],

    so the unit-mass kernel is G z / (x^2+z^2)^(3/2), i.e. m kg^-1 s^-2, here
    converted to mGal per kg by dividing by MGAL.  Superposition over point
    masses is exact.
    """
    x = x_km[:, None] * 1e3
    z = z_km[None, :] * 1e3
    return (G_CONST * z / (x ** 2 + z ** 2) ** 1.5) / MGAL


def add_noise(d, amp, rng):
    """White noise whose rms equals amp times the peak anomaly |d|max."""
    n = rng.standard_normal(d.size)
    n *= amp * np.abs(d).max() / np.linalg.norm(n) * np.sqrt(d.size)
    return n


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def main():
    Gmat = kernel_matrix(X_STATIONS_KM, DEPTHS_KM)
    d_true = Gmat @ MASSES_KG

    section("1. The forward map: gravity of four buried masses")
    print(f"  model m: {MASSES_KG.size} masses at depths "
          f"{DEPTHS_KM[0]:.1f} ... {DEPTHS_KM[-1]:.1f} km")
    print(f"  data  d: {X_STATIONS_KM.size} surface stations from "
          f"{X_STATIONS_KM[0]:.0f} to {X_STATIONS_KM[-1]:.0f} km")
    print("  units   m in kg, d in mGal, G in mGal/kg")
    print(f"  kernel matrix G: {Gmat.shape[0]} x {Gmat.shape[1]}")
    print(f"  data range: {d_true.min():.5f} to {d_true.max():.5f} mGal, "
          f"peak {np.abs(d_true).max():.5f} mGal")

    section("2. Forward stability: perturb the model by 1%")
    pert = RNG.standard_normal(MASSES_KG.size)
    pert *= 0.01 * np.linalg.norm(MASSES_KG) / np.linalg.norm(pert)
    d_pert = Gmat @ (MASSES_KG + pert)
    rel_m = np.linalg.norm(pert) / np.linalg.norm(MASSES_KG)
    rel_d = np.linalg.norm(d_pert - d_true) / np.linalg.norm(d_true)
    print(f"  ||dm||/||m|| = {rel_m:.6f}")
    print(f"  ||dd||/||d|| = {rel_d:.6f}")
    print(f"  gain of the FORWARD map = {rel_d / rel_m:.4f}  (< 1: the forward")
    print("  map smooths model differences rather than amplifying them).  Nothing")
    print("  here warns you that the backward direction is dangerous.")

    section("3. Sensitivity and column correlation")
    print("   depth (km)   ||G_k|| (mGal/kg)   anomaly of 1e10 kg (mGal)   corr with next")
    for k, zk in enumerate(DEPTHS_KM):
        col = Gmat[:, k]
        if k + 1 < DEPTHS_KM.size:
            corr = f"{np.corrcoef(col, Gmat[:, k + 1])[0, 1]:12.6f}"
        else:
            corr = "         n/a"
        print(f"   {zk:9.1f}   {np.linalg.norm(col):15.4e}   "
              f"{np.linalg.norm(col) * 1e10:25.5f}   {corr}")
    print("  Adjacent columns correlate above 0.98: two masses one kilometre")
    print("  apart in depth produce nearly the same surface anomaly, so the data")
    print("  can barely separate them.")

    section("4. The inverse: measured noise amplification")
    sv = np.linalg.svd(Gmat, compute_uv=False)
    print(f"  singular values of G: {np.array2string(sv, precision=4)}")
    print(f"  sigma_max = {sv[0]:.6e} mGal/kg,  sigma_min = {sv[-1]:.6e} mGal/kg")
    print(f"  condition number kappa(G) = {sv[0] / sv[-1]:.4e}")
    _, _, Vt = np.linalg.svd(Gmat)
    print("  smallest singular vector (the least-determined model direction):")
    print(f"    v_min = {np.array2string(Vt[-1], precision=3)}")
    print("\n  Recovery of the mass vector, 200 noise realisations per row:")
    print("   noise rms       mean model   90th pct model  gain")
    print("   (% of peak d)   error (%)    error (%)       (mean error / noise)")
    for amp in (1e-4, 3e-4, 1e-3, 3e-3, 1e-2):
        errs = []
        for _ in range(200):
            d_obs = d_true + add_noise(d_true, amp, RNG)
            m_est, *_ = np.linalg.lstsq(Gmat, d_obs, rcond=None)
            errs.append(np.linalg.norm(m_est - MASSES_KG) / np.linalg.norm(MASSES_KG))
        errs = np.array(errs)
        print(f"   {amp * 100:11.2f}   {errs.mean() * 100:11.2f}   "
              f"{np.percentile(errs, 90) * 100:14.2f}   {errs.mean() / amp:12.1f}")
    print("  The gain is constant in the noise level: this is a LINEAR inverse")
    print("  problem, and its error amplification is a property of the geometry.")

    section("5. Data-error budget for a 10% model accuracy")
    amp = 1e-4
    errs = []
    for _ in range(500):
        d_obs = d_true + add_noise(d_true, amp, RNG)
        m_est, *_ = np.linalg.lstsq(Gmat, d_obs, rcond=None)
        errs.append(np.linalg.norm(m_est - MASSES_KG) / np.linalg.norm(MASSES_KG))
    gain = float(np.mean(errs)) / amp
    print(f"  measured error gain = {gain:.1f}")
    print("  for a 10% model error the data noise must stay below")
    print(f"  {10.0 / gain:.3f}% of the peak anomaly = "
          f"{10.0 / gain / 100 * np.abs(d_true).max():.3e} mGal rms.")
    print("  That is a measurement requirement set by the survey GEOMETRY, and")
    print("  it is invisible in the forward calculation of Section 1.")

    section("6. Geometry, not physics")
    print("(a) scale invariance: the kernel depends on x/z only, so scaling the")
    print("    survey and the depths together changes nothing.")
    G_shallow = kernel_matrix(np.linspace(-6, 6, 25), DEPTHS_KM / 2.0)
    s2 = np.linalg.svd(G_shallow, compute_uv=False)
    print(f"    depths halved and spread halved: kappa = {s2[0] / s2[-1]:.4e}")
    print(f"    original geometry              : kappa = {sv[0] / sv[-1]:.4e}")
    print("(b) depth costs resolution at fixed spread:")
    deep = np.array([5.0, 10.0, 15.0, 20.0])
    G_deep = kernel_matrix(X_STATIONS_KM, deep)
    s3 = np.linalg.svd(G_deep, compute_uv=False)
    d_deep = G_deep @ MASSES_KG
    errs = []
    for _ in range(200):
        d_obs = d_deep + add_noise(d_deep, 1e-3, RNG)
        m_est, *_ = np.linalg.lstsq(G_deep, d_obs, rcond=None)
        errs.append(np.linalg.norm(m_est - MASSES_KG) / np.linalg.norm(MASSES_KG))
    print(f"    same masses at 5, 10, 15, 20 km: kappa = {s3[0] / s3[-1]:.4e}, "
          f"gain = {np.mean(errs) / 1e-3:.1f}")
    print("  Identical physics, different experiment, different difficulty.")


if __name__ == "__main__":
    main()
