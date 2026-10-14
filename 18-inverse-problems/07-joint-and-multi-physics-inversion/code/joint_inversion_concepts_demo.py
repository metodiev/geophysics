#!/usr/bin/env python3
"""Why joint inversion works: complementary sensitivities, and one ambiguity
that a second datum genuinely resolves.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python joint_inversion_concepts_demo.py

All models and data in this demonstration are SYNTHETIC.  The two forward
operators below are chosen teaching operators that reproduce the *sensitivity
shape* of a broad potential-field survey (deep-sensitive, smooth) and of a
depth-decaying diffusive sounding (shallow-sensitive, exponentially damped).
They are not simulations of a real survey, and no number below is a measurement.

Contents
--------
1. Two forward operators and their depth sensitivity.
2. Singular-value spectra: what each method resolves alone.
3. Model resolution matrices and the unresolved subspace.
4. The joint operator: resolution that neither method has alone.
5. A two-parameter ambiguity (mass = drho * H) broken by a second datum.
6. How correlated errors between the two data sets shrink the gain.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC discretisation (chosen, not measured) ------------------------
NLAY = 40                       # model cells
DZ_KM = 0.5                     # cell thickness, km
Z = (np.arange(NLAY) + 0.5) * DZ_KM          # cell-centre depths, km

R_STATIONS = np.linspace(1.0, 20.0, 20)      # surface offsets, km
ZC_KM = np.linspace(1.0, 18.0, 10)           # centres of the localised channels
W_LOC_KM = 1.2                               # localisation half-width, km

TOL = 1e-3                      # relative singular-value cut for "resolved"


def section(title: str) -> None:
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def build_operators():
    """Return the two SYNTHETIC forward operators G1 (20x40) and G2 (10x40).

    G1: vertical gravity per unit density of a horizontal slice at depth z,
        observed at horizontal offset r.  With a point mass dm at depth z the
        vertical attraction at the surface is  G dm z / (r^2 + z^2)^(3/2); a
        slice of thickness dz therefore contributes a kernel proportional to
        dz * z / (r^2 + z^2)^(3/2).  The kernel is broad and peaks at depth,
        which is why gravity sees deep mass and resolves it poorly.
    G2: a chosen localised-sensitivity operator, one channel per centre zc,
        with kernel  exp(-(z - zc)^2 / (2 w^2)).  It stands in for any
        measurement whose sensitivity is concentrated at a known depth -- a
        migrated seismic amplitude, a cross-hole travel time, a narrow-band
        sounding -- and it resolves the top of the model far better than
        gravity does, while carrying no information at all between channels.
    """
    g1 = DZ_KM * Z[None, :] / (R_STATIONS[:, None] ** 2 + Z[None, :] ** 2) ** 1.5
    g2 = np.exp(-(Z[None, :] - ZC_KM[:, None]) ** 2 / (2 * W_LOC_KM ** 2))
    return g1, g2


def singular_report(name, G):
    """Print the singular-value spectrum summary of one operator."""
    U, s, Vt = np.linalg.svd(G, full_matrices=False)
    smax = s[0]
    rank = int(np.sum(s > TOL * smax))
    print(f"  {name}: {G.shape[0]} data, {G.shape[1]} model cells")
    print(f"    largest singular value      = {smax:.6e}")
    print(f"    smallest singular value     = {s[-1]:.6e}")
    print(f"    condition number s_max/s_min= {smax / s[-1]:.3e}")
    print(f"    rank at {TOL:.0e} relative cut = {rank} of {G.shape[1]}")
    print("    first 8 singular values (normalised):")
    print("      " + "  ".join(f"{v / smax:.4f}" for v in s[:8]))
    return U, s, Vt, rank


def resolution_diagonal(Vt, rank):
    """Diagonal of the model resolution matrix R = V_r V_r^T (rank-truncated)."""
    Vr = Vt[:rank].T
    return np.einsum("ij,ij->i", Vr, Vr)


def main():
    G1, G2 = build_operators()

    section("1. Two forward operators with different depth sensitivity")
    print(f"  model: {NLAY} cells of {DZ_KM:.2f} km, depths "
          f"{Z[0]:.2f}-{Z[-1]:.2f} km")
    print(f"  G1 (gravity-like):       {G1.shape[0]} data x {G1.shape[1]} cells")
    print(f"  G2 (localised channels): {G2.shape[0]} data x {G2.shape[1]} cells")
    col1 = np.linalg.norm(G1, axis=0)
    print(f"  G1: sensitivity norm peaks at z = {Z[np.argmax(col1)]:.2f} km and")
    print(f"      falls from {col1[1]:.3e} at z = 1 km to {col1[29]:.3e} at "
          f"z = 15 km")
    print(f"  G2: {ZC_KM.size} channels centred at z = "
          f"{', '.join(f'{c:.1f}' for c in ZC_KM)} km")
    print("      each channel has unit weight at its centre and no weight")
    print("      between centres; this is the complement of G1's broad kernel.")

    section("2. Singular-value spectra: what each method resolves alone")
    _, s1, Vt1, r1 = singular_report("G1 alone", G1)
    _, s2, Vt2, r2 = singular_report("G2 alone", G2)
    print(f"  G1 leaves {NLAY - r1} model directions unresolved; "
          f"G2 leaves {NLAY - r2}.")

    section("3. Model resolution matrices and the unresolved subspace")
    R1 = resolution_diagonal(Vt1, r1)
    R2 = resolution_diagonal(Vt2, r2)
    bands = [(0, 5), (5, 10), (10, 20), (20, 30), (30, 40)]
    print("  depth band (km)   mean diag(R1)   mean diag(R2)   better method")
    for lo, hi in bands:
        m1, m2 = R1[lo:hi].mean(), R2[lo:hi].mean()
        who = "G1" if m1 > m2 else "G2"
        print(f"   {Z[lo]:5.2f}-{Z[hi - 1]:5.2f}      {m1:11.4f}     {m2:11.4f}"
              f"     {who}")
    print("  G1 resolves only 6 directions, concentrated near the surface where")
    print("  its sensitivity is largest; its diagonal decays with depth, so a deep")
    print("  cell is barely separated from its neighbours.  The localised operator")
    print("  is exact at its channel depths and blind between them, so its 10")
    print("  channels buy 10 directions and its diagonal is flat at about 10/40.")
    print(f"  cells with R1 diagonal < 0.5: "
          f"{int(np.sum(R1 < 0.5))};  with R2 diagonal < 0.5: {int(np.sum(R2 < 0.5))}")

    section("4. The joint operator: resolution neither method has alone")
    Gj = np.vstack([G1 / np.linalg.norm(G1), G2 / np.linalg.norm(G2)])
    _, sj, Vtj, rj = singular_report("joint (row-normalised)", Gj)
    Rj = resolution_diagonal(Vtj, rj)
    print(f"  unresolved directions: G1 alone {NLAY - r1}, "
          f"G2 alone {NLAY - r2}, joint {NLAY - rj}")
    print(f"  cells with joint diagonal < 0.5: {int(np.sum(Rj < 0.5))}")
    print(f"  mean resolution: G1 {R1.mean():.4f}, G2 {R2.mean():.4f}, "
          f"joint {Rj.mean():.4f}")
    print("  the joint operator inherits the deep, broad directions of G1 and the")
    print("  shallow localised directions of G2, so its rank exceeds either.")
    print("  mean diag(R) by depth band:")
    print("  band (km)        G1        G2     joint")
    for lo, hi in bands:
        print(f"   {Z[lo]:5.2f}-{Z[hi - 1]:5.2f}   {R1[lo:hi].mean():7.4f}  "
              f"{R2[lo:hi].mean():7.4f}  {Rj[lo:hi].mean():7.4f}")
    print("  But the gain is bounded: both operators are smooth, and their spans")
    print("  overlap in the low-order directions.  Complementarity is limited by")
    print("  how different the two sensitivities actually are, not by good will.")

    section("5. A two-parameter ambiguity broken by a second datum")
    # SYNTHETIC teaching problem.  Gravity measures the product H * drho (a mass
    # per unit area); the depth H alone is not determined by it.
    H_TRUE_KM = 4.0
    DRHO_TRUE = 0.30          # g/cm^3
    SIGMA1 = 0.02             # gravity datum error (arbitrary teaching unit)
    SIGMA2 = 0.10             # depth datum error, km
    d1_true = H_TRUE_KM * DRHO_TRUE
    print(f"  true model: H = {H_TRUE_KM:.2f} km, drho = {DRHO_TRUE:.2f} g/cm^3")
    print(f"  datum 1 (gravity-like) = H*drho = {d1_true:.4f} "
          f"(teaching unit), sigma = {SIGMA1:.3f}")
    print(f"  datum 2 (depth)        = H      = {H_TRUE_KM:.4f} km, "
          f"sigma = {SIGMA2:.2f} km")
    print("  datum 1 fixes only the product, i.e. the hyperbola drho = d1/H:")
    print("     H (km)     drho = d1/H (g/cm^3)        H*drho")
    for Hv in (2.0, 3.0, 4.0, 5.0, 6.0):
        print(f"     {Hv:5.2f}          {d1_true / Hv:9.4f}              "
              f"{Hv * (d1_true / Hv):8.5f}")
    print("  every row reproduces datum 1 exactly, and the models differ in BOTH")
    print("  parameters: this is the equivalence class a single datum leaves.")
    print("  Linearising about the truth gives the tangent (null) direction")
    print("  (dH, d(drho)) proportional to (H, -drho), so a small first-order")
    print("  step changes the datum only to second order:")
    n1 = np.array([H_TRUE_KM, -DRHO_TRUE])
    n1 = n1 / np.linalg.norm(n1)
    for t in (0.05, 0.10, 0.20):
        p = np.array([H_TRUE_KM, DRHO_TRUE]) + t * n1
        print(f"     step {t:.2f}: H = {p[0]:.3f} km, drho = {p[1]:.4f} g/cm^3, "
              f"H*drho = {p[0] * p[1]:.5f} "
              f"(change {p[0] * p[1] - d1_true:+.5f})")
    print("  the residual change is second order in the step, exactly as the")
    print("  tangent analysis predicts; the exact invariant is the hyperbola.")
    H, DRHO = H_TRUE_KM, DRHO_TRUE
    Gmat = np.array([[DRHO, H],      # d(H*drho)/dH = drho ; d/d(drho) = H
                     [1.0, 0.0]])    # depth datum constrains H
    Cd = np.diag([SIGMA1 ** 2, SIGMA2 ** 2])
    post_cov = np.linalg.inv(Gmat.T @ np.linalg.inv(Cd) @ Gmat)
    sd = np.sqrt(np.diag(post_cov))
    rho = post_cov[0, 1] / (sd[0] * sd[1])
    print(f"  joint posterior: sigma(H) = {sd[0]:.4f} km, "
          f"sigma(drho) = {sd[1]:.4f} g/cm^3, correlation = {rho:+.3f}")
    print(f"  gravity alone leaves drho entirely free (infinite standard")
    print(f"  deviation) because of the null direction above.  Datum 2 removes")
    print(f"  that direction, and the product then pins drho to "
          f"{sd[1]:.4f} g/cm^3 while leaving sigma(H) unchanged at datum 2's")
    print(f"  own {SIGMA2:.2f} km: the second datum fixes the ambiguous")
    print("  combination, it does not improve the quantity it already measures.")

    section("6. Correlated errors: the gain is not automatic, and it has a sign")
    print("  the two data errors are rarely independent: a shared structural")
    print("  mistake (a wrong datum, a wrong wavelet) enters both.  Model the")
    print("  error covariance as sigma1*sigma2 [[1, rho], [rho, 1]] and measure")
    print("  the joint spread:")
    print("     rho      sigma(H) km    sigma(drho) g/cm^3")
    for rho_e in (-0.9, -0.6, -0.3, 0.0, 0.3, 0.6, 0.9):
        C = np.array([[SIGMA1 ** 2, rho_e * SIGMA1 * SIGMA2],
                      [rho_e * SIGMA1 * SIGMA2, SIGMA2 ** 2]])
        pc = np.linalg.inv(Gmat.T @ np.linalg.inv(C) @ Gmat)
        s = np.sqrt(np.diag(pc))
        print(f"    {rho_e:5.2f}      {s[0]:9.4f}       {s[1]:9.4f}")
    print("  the reported drho uncertainty moves by a factor of several over a")
    print("  plausible range of rho, and it can fall or rise: the sign relative")
    print("  to the model relation decides.  Section 5 quoted the rho = 0 answer,")
    print("  and rho = 0 is a choice that the data do not make for you.")


if __name__ == "__main__":
    main()
