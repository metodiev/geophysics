#!/usr/bin/env python3
"""SAR polarimetry: canonical scattering matrices, the Pauli basis and the
coherency matrix, the eigenvector decomposition and its entropy / alpha /
anisotropy parameters, the entropy bias with few looks, the Bragg polarisation
ratio, and the non-uniqueness of a degenerate decomposition.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python polarimetry_demo.py

Everything is SYNTHETIC: the scattering matrices, dielectric constants,
roughness statistics and look counts are teaching values generated here.  No
real target, scene or measurement is used.

Print-only: nothing is downloaded, nothing is written to disk.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

C = 299_792_458.0
LAM = C / 5.300e9
EPS = 6.0                # dimensionless teaching dielectric constant
THETA = 35.0             # deg


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74)


def pauli(s_mat):
    """Pauli vector of a 2x2 scattering matrix, reciprocity assumed.

    k = 1/sqrt(2) [S_HH + S_VV, S_HH - S_VV, 2 S_HV]
    """
    return np.array([s_mat[0, 0] + s_mat[1, 1],
                     s_mat[0, 0] - s_mat[1, 1],
                     2.0 * s_mat[0, 1]]) / np.sqrt(2.0)


def coherency(cloud):
    """Multilook coherency matrix T3 = <k k^dagger> of a cloud of matrices."""
    ks = np.array([pauli(s) for s in cloud])
    return (ks[:, :, None] * np.conj(ks[:, None, :])).mean(axis=0)


def h_a_alpha(t3):
    """Entropy, anisotropy and mean alpha of a coherency matrix."""
    lam, vec = np.linalg.eigh(t3)
    order = np.argsort(lam)[::-1]
    lam = np.real(lam[order])
    vec = vec[:, order]
    p = lam / lam.sum()
    h = -np.sum(p * np.log(np.clip(p, 1e-12, None))) / np.log(3.0)
    alpha_i = np.degrees(np.arccos(np.clip(np.abs(vec[0, :]), 0.0, 1.0)))
    alpha = float(np.sum(p * alpha_i))
    aniso = float((lam[1] - lam[2]) / (lam[1] + lam[2])) if lam[1] + lam[2] > 0 else 0.0
    return h, alpha, aniso, lam, vec


def bragg_coeffs(eps, th_deg):
    """First-order (small-perturbation) Bragg coefficients for a flat interface."""
    th = np.radians(th_deg)
    root = np.sqrt(eps - np.sin(th) ** 2)
    g_hh = (eps - 1.0) / (np.cos(th) + root) ** 2
    g_vv = (eps - 1.0) * (eps * (1.0 + np.sin(th) ** 2) - np.sin(th) ** 2) \
        / (eps * np.cos(th) + root) ** 2
    return g_hh, g_vv


def main():
    section("1. Canonical scattering matrices and their Pauli vectors")
    print("  S is 2x2 complex in the (H, V) basis; the Pauli vector is")
    print("  k = 1/sqrt(2) [S_HH+S_VV, S_HH-S_VV, 2 S_HV], reciprocity assumed\n")
    targets = {
        "trihedral / sphere": np.array([[1.0, 0.0], [0.0, 1.0]], dtype=complex),
        "dihedral (double bounce)": np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex),
        "horizontal dipole": np.array([[1.0, 0.0], [0.0, 0.0]], dtype=complex),
        "45 deg dipole": np.array([[0.5, 0.5], [0.5, 0.5]], dtype=complex),
    }
    print("   target                      |S_HH|  |S_VV|  |S_HV|   Pauli k "
          "(2 decimals)")
    for name, s_mat in targets.items():
        k = pauli(s_mat)
        print(f"   {name:26s}  {abs(s_mat[0,0]):6.3f}  {abs(s_mat[1,1]):6.3f}  "
              f"{abs(s_mat[0,1]):6.3f}   "
              f"({k[0].real:+.2f}, {k[1].real:+.2f}, {k[2].real:+.2f})")
    print("\n  the Pauli vector separates the three canonical mechanisms:")
    print("    k_1 (HH+VV)  odd-bounce / surface,   k_2 (HH-VV)  double bounce,")
    print("    k_3 (2 HV)   volume (depolarising).  For a deterministic target the")
    print("  coherency matrix has a single non-zero eigenvalue: one mechanism.")

    section("2. Multilook coherency matrices: entropy, alpha, anisotropy")
    print("  a cloud of 200 realisations per target, each the canonical matrix plus")
    print("  a random complex perturbation of 8% (a 'noisy' distributed target)\n")
    print("   target                     H      alpha (deg)   anisotropy   lambda1/lambda2/lambda3")
    rows = {}
    for name, s_mat in targets.items():
        cloud = []
        for _ in range(200):
            noise = 0.08 * (RNG.standard_normal((2, 2))
                            + 1j * RNG.standard_normal((2, 2)))
            cloud.append(s_mat + (noise + noise.T) / 2.0)   # keep reciprocity
        t3 = coherency(cloud)
        h, alpha, aniso, lam, _ = h_a_alpha(t3)
        rows[name] = (h, alpha, aniso)
        print(f"   {name:26s}  {h:.4f}  {alpha:11.2f}   {aniso:10.4f}   "
              f"{lam[0]:.3f}/{lam[1]:.3f}/{lam[2]:.3f}")
    # a volume target: sum of many random dipoles with random orientation
    cloud = []
    for _ in range(200):
        s_tot = np.zeros((2, 2), dtype=complex)
        for _ in range(30):
            ang = RNG.uniform(0.0, np.pi)
            dip = np.array([[np.cos(ang) ** 2, np.cos(ang) * np.sin(ang)],
                            [np.cos(ang) * np.sin(ang), np.sin(ang) ** 2]])
            s_tot += dip * np.exp(1j * RNG.uniform(0.0, 2 * np.pi)) / np.sqrt(30.0)
        cloud.append(s_tot)
    t3v = coherency(cloud)
    h, alpha, aniso, lam, _ = h_a_alpha(t3v)
    rows["random volume"] = (h, alpha, aniso)
    print(f"   {'random volume':26s}  {h:.4f}  {alpha:11.2f}   {aniso:10.4f}   "
          f"{lam[0]:.3f}/{lam[1]:.3f}/{lam[2]:.3f}")
    print("\n  the pattern is the whole diagnostic: surface scattering gives low")
    print("  entropy and alpha near 0, double bounce gives low entropy and alpha near")
    print("  90, and a random volume gives high entropy with alpha near 45.  Entropy")
    print("  measures how many mechanisms are present; alpha measures which.")

    section("3. The entropy bias with few looks")
    print("  the same deterministic trihedral, with additive complex noise of 15%")
    print("  and only N looks; H should be zero on the noiseless target\n")
    print("   N looks   mean H   median H   10%   90%")
    for n_look in (1, 2, 4, 16, 64):
        hs = []
        for _ in range(2000):
            cloud = []
            for _ in range(n_look):
                noise = 0.15 * (RNG.standard_normal((2, 2))
                                + 1j * RNG.standard_normal((2, 2)))
                cloud.append(targets["trihedral / sphere"] + (noise + noise.T) / 2.0)
            t3 = coherency(cloud)
            hs.append(h_a_alpha(t3)[0])
        hs = np.array(hs)
        q = np.percentile(hs, [10, 50, 90])
        print(f"   {n_look:7d}   {hs.mean():.4f}   {q[1]:.4f}   {q[0]:.4f}   {q[2]:.4f}")
    print("\n  read the N = 1 row carefully: H is exactly zero for EVERY target,")
    print("  because a single outer product is rank one by construction.  A single-look")
    print("  entropy therefore carries no information at all - the same pathology as")
    print("  single-look coherence in the InSAR lesson.  As looks accumulate, H rises")
    print("  and converges to the value set by the physics and the noise level:")
    print("  0.18 here, far below the 0.5 that a naive threshold would call volume")
    print("  scattering.  Entropy must be reported with its look count and its")
    print("  convergence value, never as a bare number.")

    section("4. Bragg scattering: the resonant wavelength and the polarisation ratio")
    th = np.radians(THETA)
    k_bragg = 2.0 * (2.0 * np.pi / LAM) * np.sin(th)
    lam_bragg = 2.0 * np.pi / k_bragg
    print("  first-order surface scattering comes from the roughness component whose")
    print("  wavenumber satisfies  k_B = 2 k sin(theta) = 4 pi sin(theta)/lam")
    print(f"    k_B = {k_bragg:.2f} rad/m  ->  resonant surface wavelength "
          f"{lam_bragg*100:.4f} cm")
    print(f"    a {LAM*100:.4f} cm radar at {THETA:.0f} deg is resonant with surface")
    print(f"    ripples about {lam_bragg*100:.3f} cm long\n")
    g_hh, g_vv = bragg_coeffs(EPS, THETA)
    print(f"  first-order Bragg coefficients at dielectric constant {EPS:.1f}:")
    print(f"    g_HH = {g_hh:.6f}   g_VV = {g_vv:.6f}   "
          f"ratio HH/VV = {g_hh/g_vv:.6f} = {20*np.log10(g_hh/g_vv):+.3f} dB")
    print("\n   theta (deg)   HH/VV (linear)   HH/VV (dB)")
    for t in (0.0, 10.0, 23.0, 35.0, 45.0, 60.0):
        a, b = bragg_coeffs(EPS, t)
        print(f"   {t:11.0f}   {a/b:15.6f}   {20*np.log10(a/b):11.3f}")
    a0, b0 = bragg_coeffs(EPS, 0.0)
    print(f"\n  at normal incidence the two coefficients are equal to "
          f"{a0:.6f} (HH/VV = {a0/b0:.6f}, i.e. 0 dB), as symmetry requires,")
    print("  and the ratio falls steeply with incidence angle.  A measured HH/VV")
    print("  ratio therefore constrains the dielectric constant only if the")
    print("  incidence angle is known, which is the same caveat as for sigma0.")

    section("5. Non-uniqueness of a degenerate decomposition")
    print("  a coherency matrix with a degenerate PAIR of non-zero eigenvalues.")
    print("  Build it from an orthonormal eigenbasis; T3 = V diag(l) V^dagger with")
    print("  l = (2.0, 0.8, 0.8): eigenvectors inside the degenerate subspace are not")
    print("  unique, and any rotation of them leaves T3 exactly unchanged.\n")
    e1 = np.array([0.6, -0.8, 0.0])
    e2 = np.array([0.8, 0.6, 0.0])
    e3 = np.array([0.0, 0.0, 1.0])
    vec0 = np.column_stack([e1, e2, e3])
    lam = np.array([2.0, 0.8, 0.8])
    t3 = (vec0 * lam) @ vec0.conj().T
    h, alpha, aniso, lam_chk, vec = h_a_alpha(t3)
    print(f"  eigenvalues recovered: {lam_chk[0]:.4f}, {lam_chk[1]:.4f}, "
          f"{lam_chk[2]:.4f}")
    print(f"  H = {h:.6f}, A = {aniso:.6f}, alpha = {alpha:.4f} deg")
    rot = np.deg2rad(45.0)
    r_mat = np.array([[1.0, 0.0, 0.0],
                      [0.0, np.cos(rot), -np.sin(rot)],
                      [0.0, np.sin(rot), np.cos(rot)]])
    vec_rot = vec @ r_mat
    t3_rot = (vec_rot * lam_chk) @ vec_rot.conj().T
    p = lam_chk / lam_chk.sum()
    a_orig = np.degrees(np.arccos(np.clip(np.abs(vec[0, :]), 0.0, 1.0)))
    a_rot = np.degrees(np.arccos(np.clip(np.abs(vec_rot[0, :]), 0.0, 1.0)))
    print(f"\n  ||T3 - T3(rebuilt from the rotated eigenvectors)|| = "
          f"{np.linalg.norm(t3 - t3_rot):.3e}  (numerical zero)")
    print(f"  per-eigenvector alpha, convention 1: "
          f"{np.array2string(a_orig, precision=2)}")
    print(f"  per-eigenvector alpha, convention 2: "
          f"{np.array2string(a_rot, precision=2)}")
    print(f"  weighted mean alpha: convention 1 {np.sum(p*a_orig):.4f} deg, "
          f"convention 2 {np.sum(p*a_rot):.4f} deg, difference "
          f"{abs(np.sum(p*a_orig)-np.sum(p*a_rot)):.4f} deg")
    print("\n  two eigenvector sets that reproduce the SAME observable matrix give")
    print("  different per-eigenvector alpha values and a measurably different mean")
    print("  alpha, while H and A are identical because they depend only on the")
    print("  eigenvalues.  H and A are invariant; alpha is convention-dependent")
    print("  whenever a degeneracy exists, and the size of the discrepancy grows with")
    print("  how much the degenerate subspace overlaps the (HH+VV) axis.  A reported")
    print("  alpha therefore requires the convention used to define its eigenvectors.")
    print("  The deeper point: two mechanisms with equal weights and one mechanism")
    print("  plus noise can produce the SAME T3.  The number of scattering components")
    print("  is a model decision, not a measurement, and any decomposition should be")
    print("  reported with the fit residual and the alternative that fits as well.")


if __name__ == "__main__":
    main()
