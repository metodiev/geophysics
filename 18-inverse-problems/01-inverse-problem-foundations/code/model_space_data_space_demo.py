#!/usr/bin/env python3
"""Model space, data space and the mappings between them.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python model_space_data_space_demo.py

Everything here is SYNTHETIC.  The kernel is a chosen teaching operator (a
discretised first-kind integral of the gravity type), not a survey.

Contents
--------
1. The two spaces and the rank-nullity split of the model space.
2. Range and orthogonal complement: the projection P = G G^+ and its identities.
3. The orthogonally unfittable part of data: measured against (N - rank)/N.
4. The null-space part of a model: G m_null = 0 and its effect on ||m||.
5. Many-to-one: 500 models, one data vector.
6. The model-space operator G^T G: same null space, squared condition number.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

NC = 12                                  # model parameters
X_STATIONS_KM = np.linspace(-9.0, 9.0, 20)
# Twelve masses 50 m apart inside one 550 m interval: the classic thin-layer
# ambiguity of potential-field interpretation.
DEPTHS_KM = 2.00 + 0.05 * np.arange(NC)
G_CONST = 6.67430e-11
MGAL = 1.0e-5
TOL = 1e-10


def build_G():
    """Vertical gravity kernel: G[i, k] = G z / (x^2 + z^2)^(3/2) in mGal/kg."""
    x = X_STATIONS_KM[:, None] * 1e3
    z = DEPTHS_KM[None, :] * 1e3
    return (G_CONST * z / (x ** 2 + z ** 2) ** 1.5) / MGAL


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def main():
    G = build_G()
    N, M = G.shape
    U, s, Vt = np.linalg.svd(G)
    V = Vt[:s.size].T
    keep = s > TOL * s[0]
    rank = int(keep.sum())
    nullity = M - rank

    section("1. The two spaces")
    print(f"  model space: R^M with M = {M} masses 50 m apart at about 2 km depth")
    print(f"  data space : R^N with N = {N} stations from {X_STATIONS_KM[0]:.0f} to "
          f"{X_STATIONS_KM[-1]:.0f} km")
    print(f"  forward map G: R^M -> R^N, shape {G.shape}")
    print(f"  singular values: {np.array2string(s, precision=4)}")
    print(f"  relative singular values: {np.array2string(s / s[0], precision=3)}")
    print(f"  rank = {rank},  dim N(G) = {nullity},  rank + nullity = "
          f"{rank + nullity} = M  ✔")
    print(f"  dim range(G) = {rank},  dim range(G)^perp = {N - rank}")
    print("  rank-nullity holds for the MODEL space; the data space splits as")
    print("  range(G) + range(G)^perp, and only the first part can ever be fitted.")

    section("2. The projection onto the range")
    # Truncated pseudo-inverse at the declared tolerance: this is the operator
    # that acts as an inverse only on directions the data can actually see.
    Uk, Vk = U[:, :s.size][:, keep], V[:, keep]
    Gp = (Vk / s[keep]) @ Uk.T
    P = G @ Gp
    print(f"  G^+ truncated at relative tolerance {TOL:.0e}: shape {Gp.shape}")
    print(f"  P = G G^+ has shape {P.shape} and acts on data space")
    print(f"  ||P^2 - P||_inf    = {np.max(np.abs(P @ P - P)):.3e}  (idempotent)")
    print(f"  ||P^T - P||_inf    = {np.max(np.abs(P.T - P)):.3e}  (symmetric, so an")
    print("  orthogonal projector)")
    print(f"  trace(P)           = {np.trace(P):.6f}, rank = {rank}  (trace = rank)")
    print(f"  P G = G check: ||P G - G||_inf = {np.max(np.abs(P @ G - G)):.3e}")
    print("  Everything G can produce lies in range(G); P is the identity on that")
    print("  subspace and zero on its orthogonal complement.")
    print("  projector identities versus truncation tolerance:")
    print("   tolerance   rank   kappa of retained part   measured ||P^2-P||   eps*kappa")
    for tol2 in (1e-10, 1e-8, 1e-6, 1e-4):
        k2 = s > tol2 * s[0]
        Gp2 = (V[:, k2] / s[k2]) @ U[:, :s.size][:, k2].T
        P2 = G @ Gp2
        kap = s[0] / s[k2][-1]
        print(f"   {tol2:9.0e}   {int(k2.sum()):4d}   {kap:22.3e}   "
              f"{np.max(np.abs(P2 @ P2 - P2)):17.3e}   {np.finfo(float).eps * kap:.1e}")
    print("  The projector error tracks eps times the condition number of the RETAINED")
    print("  part: an inverse you can actually use is never an exactly orthogonal")
    print("  projector, and a tolerance that makes the projector exact throws away")
    print("  most of the data.  The truncation tolerance is part of the definition of")
    print("  the inverse, not a numerical detail.")

    section("3. The unfittable part of data")
    d_model = G @ (np.array([1.0, 1.4, 0.8, 1.2, 1.0, 0.6, 1.1, 0.9,
                             1.3, 0.7, 1.1, 0.9]) * 1e10)
    n = RNG.standard_normal(N)
    n *= 1e-2 * np.abs(d_model).max()
    inrange = np.linalg.norm(P @ n) ** 2
    outrange = np.linalg.norm(n - P @ n) ** 2
    print(f"  data from a SYNTHETIC model: ||d_model|| = {np.linalg.norm(d_model):.4e} mGal")
    print(f"  a white-noise vector of rms {np.std(n):.4e} mGal is split as")
    print(f"    energy in range(G)        : {inrange / (inrange + outrange) * 100:7.3f}%"
          f"   (expected {rank / N * 100:.3f}%)")
    print(f"    energy in range(G)^perp   : {outrange / (inrange + outrange) * 100:7.3f}%"
          f"   (expected {(N - rank) / N * 100:.3f}%)")
    frac = []
    for _ in range(2000):
        w = RNG.standard_normal(N)
        frac.append(np.linalg.norm(w - P @ w) ** 2 / np.linalg.norm(w) ** 2)
    print(f"  mean over 2000 draws: fit {1 - np.mean(frac):.4f} of the energy, "
          f"unfittable {np.mean(frac):.4f}")
    print(f"  exact expectation: fit = rank/N = {rank / N:.4f}, unfittable = "
          f"(N-rank)/N = {(N - rank) / N:.4f}.")
    print("  The single draw above fluctuated well away from the expectation, as it")
    print("  must for one realisation; the average converges to the exact value.  Any")
    print("  attempt to fit the orthogonal complement is fitting noise.")

    section("4. The null-space part of a model")
    m1 = np.array([1.0, 1.4, 0.8, 1.2, 1.0, 0.6, 1.1, 0.9, 1.3, 0.7, 1.1, 0.9]) * 1e10
    m_row = V[:, keep] @ (V[:, keep].T @ m1)
    m_null = m1 - m_row
    print(f"  m_row  = part of m1 in the data-informed directions: ||m_row||  = "
          f"{np.linalg.norm(m_row):.4e} kg")
    print(f"  m_null = part in the directions cut at tolerance {TOL:.0e}: "
          f"||m_null|| = {np.linalg.norm(m_null):.4e} kg")
    print(f"  ||G m_null||_inf = {np.max(np.abs(G @ m_null)):.3e} mGal, which is "
          f"{np.max(np.abs(G @ m_null)) / (s[0] * np.linalg.norm(m_null)):.2e} of "
          f"sigma_1 ||m_null||")
    print(f"  the tolerance allows up to {s[rank] / s[0]:.1e} here, so the cut directions")
    print("  are 'null' only to the precision we declared.  There is no exactly")
    print("  singular direction in a discretised compact operator.")
    print(f"  ||m1||^2 - ||m_row||^2 - ||m_null||^2 = "
          f"{(np.linalg.norm(m1) ** 2 - np.linalg.norm(m_row) ** 2 - np.linalg.norm(m_null) ** 2) / np.linalg.norm(m1) ** 2:.3e}"
          f" relative  (Pythagoras)")
    print(f"  ||m_null|| is {np.linalg.norm(m_null) / np.linalg.norm(m1) * 100:.1f}% of "
          f"||m1||, yet it produces data at only "
          f"{np.max(np.abs(G @ m_null)) / np.linalg.norm(G @ m1):.1e} of ||d||: a large,")
    print("  physically meaningful-sounding change in the model that the experiment")
    print("  would not notice.")
    v0 = V[:, rank]
    print(f"  first cut direction: {np.array2string(v0, precision=3)}")
    print("  Its pattern is an exchange between neighbouring masses: the data see")
    print("  only the combination, so the split between them is unconstrained.")

    section("5. Many-to-one: 500 models, one data vector")
    d = G @ m1
    Z = V[:, rank:]
    fits, spread = [], []
    for _ in range(500):
        w = RNG.standard_normal(Z.shape[1])
        w *= 0.1 * np.linalg.norm(m1) / np.linalg.norm(w)
        m = m1 + Z @ w
        fits.append(np.linalg.norm(G @ m - d))
        spread.append(np.linalg.norm(m - m1))
    print(f"  data vector fixed at d = G m1, {N} numbers, ||d|| = {np.linalg.norm(d):.4e} mGal")
    print(f"  worst data discrepancy over 500 models: {max(fits):.3e} mGal")
    print(f"  relative discrepancy: {max(fits) / np.linalg.norm(d):.3e}, which is "
          f"{max(fits) / (1e-3 * np.abs(d).max()):.1e} of a")
    print("  plausible 0.1% data error.  The differences are unmeasurable.")
    print(f"  model displacement is {spread[0] / np.linalg.norm(m1) * 100:.1f}% of "
          f"||m1|| = {np.linalg.norm(m1):.4e} kg for every one of them")
    print("  (the perturbations are orthogonal to m1, with a fixed magnitude).")
    print("  The forward map is many-to-one; the inverse map is set-valued.  An")
    print("  inversion algorithm must add a selection rule, and that rule is an")
    print("  assumption about the Earth.")

    section("6. The model-space operator G^T G")
    GtG = G.T @ G
    sg = np.linalg.svd(GtG, compute_uv=False)
    print("  eigenvalues of G^T G equal the squared singular values of G:")
    print(f"    G^T G (first four): {np.array2string(sg[:4], precision=6)}")
    print(f"    sigma^2  (first four): {np.array2string(s[keep][:4] ** 2, precision=6)}")
    rel = np.max(np.abs(sg[:4] - s[keep][:4] ** 2) / s[keep][:4] ** 2)
    print(f"    max relative difference over those four: {rel:.3e}")
    print(f"    (the fourth eigenvalue is only (sigma_4/sigma_1)^2 = "
          f"{(s[3] / s[0]) ** 2:.1e} of the first, so computing")
    print("     G^T G explicitly has already thrown away half the significant digits)")
    print(f"  kappa(G)    = {s[0] / s[rank - 1]:.6e}")
    print(f"  kappa(G^T G)= {sg[0] / sg[rank - 1]:.6e}")
    print(f"  kappa(G)^2  = {(s[0] / s[rank - 1]) ** 2:.6e}   <- exact identity "
          f"kappa(G^T G) = kappa(G)^2")
    print(f"  measured ratio kappa(G^T G)/kappa(G)^2 = "
          f"{(sg[0] / sg[rank - 1]) / (s[0] / s[rank - 1]) ** 2:.6f}: the sixth")
    print(f"  eigenvalue of G^T G is (sigma_6/sigma_1)^2 = {(s[5] / s[0]) ** 2:.1e} of the first,")
    print("  which is roundoff, so the exact identity cannot be measured to better")
    print(f"  than this.  Numerical rank of G^T G at {TOL:.0e} is "
          f"{int(np.sum(sg > TOL * sg[0]))} against {rank} for G:")
    print("  forming the normal equations destroys two of the directions that the SVD")
    print("  resolves, and squares the conditioning.  Use the SVD or a QR factorisation.")
    print("\n  All models and data in this demonstration are SYNTHETIC.")


if __name__ == "__main__":
    main()
