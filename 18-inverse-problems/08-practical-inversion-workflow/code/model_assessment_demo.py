#!/usr/bin/env python3
"""Assessing a model: resolution, artifacts and admissible alternatives.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python model_assessment_demo.py

All models and data are SYNTHETIC.  The forward operator is a chosen teaching
operator (Gaussian sensitivity kernels); no number below is a measurement.

Contents
--------
1. A produced model and its data misfit.
2. Resolution: diagonal of the resolution matrix and a point-spread function.
3. An artifact: a feature the data do not require.
4. Alternatives: the spread of models that fit the data equally well.
5. What to report, in numbers.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

N = 40                      # model cells
N_DATA = 15                 # observations
Z_MAX = 20.0                # km
SIGMA = 0.25                # data standard deviation
LAMBDA = 30.0               # smoothness weight (chi ~ 1, section 1)


def section(title: str) -> None:
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def build():
    dz = Z_MAX / N
    zc = (np.arange(N) + 0.5) * dz
    zobs = np.linspace(1.0, Z_MAX - 1.0, N_DATA)
    A = dz * np.exp(-(zobs[:, None] - zc[None, :]) ** 2 / (2 * 2.0 ** 2))
    D = np.zeros((N - 1, N))
    for k in range(N - 1):
        D[k, k] = -1.0 / dz            # a physical gradient, not a cell difference
        D[k, k + 1] = 1.0 / dz
    return zc, A, D


def m_true(zc):
    return (0.6 * np.exp(-((zc - 6.0) ** 2) / (2 * 1.5 ** 2))
            + 0.35 * (zc > 12.0))


def main():
    zc, A, D = build()
    m_t = m_true(zc)
    d = A @ m_t + SIGMA * RNG.standard_normal(A.shape[0])
    C = np.linalg.inv(A.T @ A / SIGMA ** 2 + LAMBDA * (D.T @ D))
    m_hat = C @ A.T @ d / SIGMA ** 2
    R = C @ (A.T @ A) / SIGMA ** 2

    section("1. A produced model and its data misfit")
    chi = np.sqrt(np.mean((A @ m_hat - d) ** 2)) / SIGMA
    print(f"  {N} cells over {Z_MAX:.0f} km, {N_DATA} observations, "
          f"sigma = {SIGMA:.2f}")
    print(f"  chi per datum (model) = {chi:.3f}")
    print(f"  error against the SYNTHETIC truth = "
          f"{np.sqrt(np.mean((m_hat - m_t) ** 2)):.4f}")
    print("  a chi near 1 says the model explains the data at the stated noise")
    print("  level.  It says nothing yet about which parts of the model are real.")

    section("2. Resolution: diagonal of R and a point-spread function")
    diag = np.diag(R)
    print(f"  trace(R) = {np.trace(R):.2f} effective parameters out of {N}")
    print(f"  mean diag(R) = {diag.mean():.4f}; cells with diag(R) > 0.5: "
          f"{int(np.sum(diag > 0.5))} of {N}")
    target = 12                                   # cell index near 6 km
    psf = R[target]
    width_idx = np.where(psf > 0.5 * psf[target])[0]
    width = zc[width_idx[-1]] - zc[width_idx[0]] if width_idx.size else 0.0
    print(f"  point-spread function of cell {target} (z = {zc[target]:.2f} km):")
    print(f"    peak value        = {psf[target]:.4f}")
    print(f"    width at half max = {width:.2f} km")
    print(f"    minimum (sidelobe)= {psf.min():+.4f}")
    print("  the PSF is the answer to 'if the Earth had a spike here, what would")
    print("  the inversion return?'.  It is wide (the data are smoothed) and it")
    print("  has negative lobes, which are produced by the smoothness prior.")

    section("3. Which features do the data require?  A perturbation test")
    print("  ask the data directly: if a small feature were added or removed,")
    print("  would the data notice?  A localised perturbation of width w and")
    print("  amplitude 0.1 (a plausible small contrast) is added to the model and")
    print("  two numbers are reported:")
    print("    signature = rms data change / sigma            (>1: the data see it)")
    print("    posterior = sqrt(dm' C^-1 dm / N)              (<1: admitted)")
    print("  width (km)   signature (sigma)   posterior norm   verdict")
    for w in (0.25, 0.5, 1.0, 3.0, 8.0):
        pert = 0.1 * np.exp(-((zc - zc[12]) ** 2) / (2 * w ** 2))
        signature = np.sqrt(np.mean((A @ pert) ** 2)) / SIGMA
        post = np.sqrt(pert @ np.linalg.solve(C, pert) / N)
        verdict = "required" if signature > 1.0 else "not required"
        print(f"  {w:10.2f}   {signature:15.3f}   {post:14.3f}   {verdict}")
    print("  features much narrower than the PSF width move the data far less than")
    print("  the noise: the data cannot require them, and the inversion may or may")
    print("  not produce one depending on the regularisation.  Such a feature must")
    print("  never be reported as a resolved layer.")

    section("4. Alternatives: models that fit the data equally well")
    L = np.linalg.cholesky(C + 1e-12 * np.eye(N))
    alts = np.array([m_hat + L @ RNG.standard_normal(N) for _ in range(2000)])
    chi_alts = [np.sqrt(np.mean((A @ a - d) ** 2)) / SIGMA for a in alts[:50]]
    spread = alts.std(axis=0)
    print(f"  2000 posterior samples; their chi per datum ranges "
          f"{min(chi_alts):.2f} to {max(chi_alts):.2f}")
    print("  (all at the noise level: they are equally acceptable explanations)")
    worst = int(np.argmax(spread))
    best = int(np.argmin(spread))
    print("  cell depth (km)   admissible range (95%, +/-2 sigma)")
    for cell in (4, 12, 20, 30, 36):
        print(f"  {zc[cell]:14.2f}   {4 * spread[cell]:22.4f}")
    print(f"  widest spread at z = {zc[worst]:.2f} km "
          f"({4 * spread[worst]:.4f}); narrowest at z = {zc[best]:.2f} km "
          f"({4 * spread[best]:.4f})")
    print("  the model is not one model.  It is a distribution, and the width of")
    print("  that distribution varies with depth by a factor of "
          f"{spread[worst] / spread[best]:.1f}:")
    print("  the least constrained cell is the one at the edge of the kernel")
    print("  coverage, which no observation sits over.")

    section("5. What to report, in numbers")
    print(f"  1. misfit: chi per datum = {chi:.2f} for {N_DATA} observations")
    print(f"  2. complexity: trace(R) = {np.trace(R):.2f} effective parameters")
    print(f"  3. resolution: PSF width {width:.2f} km at z = {zc[target]:.2f} km")
    sig_small = np.sqrt(np.mean((A @ (0.1 * np.exp(
        -((zc - zc[12]) ** 2) / (2 * 0.5 ** 2)))) ** 2)) / SIGMA
    print(f"  4. admissibility: a feature of width 0.5 km and amplitude 0.1 has")
    print(f"     signature {sig_small:.3f} sigma, i.e. the data do not require it")
    print(f"  5. alternatives: 95% admissible range from "
          f"{4 * spread[best]:.4f} to {4 * spread[worst]:.4f} across depth")
    print("  a report that omits items 3-5 has not assessed the model; it has")
    print("  only displayed it.")


if __name__ == "__main__":
    main()
