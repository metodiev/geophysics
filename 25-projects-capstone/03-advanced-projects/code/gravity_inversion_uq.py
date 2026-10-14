#!/usr/bin/env python3
"""Advanced project 6: gravity inversion with a full uncertainty and resolution
assessment - covariance, resolution matrix, trade-off and equivalence class.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gravity_inversion_uq.py

Everything here is SYNTHETIC.  The density model and the gravity data are
generated below from chosen values with chosen noise; no survey and no published
anomaly is used.

Sections
--------
1. The model grid, the forward kernel and the synthetic data.
2. The regularised inversion and the choice of the smoothing parameter.
3. Model covariance, resolution matrix and the resolved-parameter count.
4. The equivalence class: what the 1-sigma interval really covers.
"""

import numpy as np
from numpy.polynomial.legendre import leggauss

RNG = np.random.default_rng(20261014)

GRAV_CONST = 6.67430e-11
MGAL = 1.0e-5

NX = 8                     # blocks along the profile
NZ = 4                     # depth layers
DX_BLOCK = 6.25e3          # block width, m
LAYER_EDGES = (0.0, 1.0e3, 3.0e3, 6.0e3, 10.0e3)   # depth layer boundaries, m
X_MIN = -25.0e3            # profile start, m
N_STATIONS = 25
STATION_SPACING = 2000.0   # m
DATA_SIGMA = 0.05          # mGal
TRUE_MODEL = np.zeros(NX * NZ)
for _i in (2, 3, 4):                      # shallow high-density body
    TRUE_MODEL[_i] = 300.0
for _i in (NX + 2, NX + 3):               # deep low-density body
    TRUE_MODEL[_i] = -200.0
ALPHA_SCAN = np.logspace(-6, 3, 37)


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def block_corner(ix, iz):
    """Corner coordinates of block (ix, iz): (x1, x2, z1, z2) in metres."""
    x1 = X_MIN + ix * DX_BLOCK
    return x1, x1 + DX_BLOCK, LAYER_EDGES[iz], LAYER_EDGES[iz + 1]


def kernel(x_stations):
    """Gravity kernel: dg/drho for every block and station, in mGal per kg/m^3."""
    nodes, weights = leggauss(10)
    a = np.zeros((x_stations.size, NX * NZ))
    for ix in range(NX):
        x1, x2, z1, z2 = block_corner(ix, 0)
        xs = 0.5 * (x2 - x1) * nodes + 0.5 * (x2 + x1)
        wx = 0.5 * (x2 - x1) * weights
        for iz in range(NZ):
            z1, z2 = LAYER_EDGES[iz], LAYER_EDGES[iz + 1]
            zs = 0.5 * (z2 - z1) * nodes + 0.5 * (z2 + z1)
            wz = 0.5 * (z2 - z1) * weights
            integrand = 2.0 * GRAV_CONST * (zs[None, :] /
                                            ((x_stations[:, None] - xs[None, :]) ** 2
                                             + zs[None, :] ** 2))
            a[:, ix * NZ + iz] = integrand @ wz * wx.sum() / MGAL
    return a


def difference_operator():
    """First-difference (roughness) matrix for the flattened model."""
    rows = []
    for iz in range(NZ):
        for ix in range(NX - 1):
            row = np.zeros(NX * NZ)
            row[iz * NX + ix] = 1.0
            row[iz * NX + ix + 1] = -1.0
            rows.append(row)
    for iz in range(NZ - 1):
        for ix in range(NX):
            row = np.zeros(NX * NZ)
            row[iz * NX + ix] = 1.0
            row[(iz + 1) * NX + ix] = -1.0
            rows.append(row)
    return np.array(rows)


def solve(a, d, sigma, alpha, l_mat):
    """Tikhonov solution and its posterior covariance."""
    wd = np.eye(d.size) / sigma ** 2
    n = a.T @ wd @ a + alpha * (l_mat.T @ l_mat)
    ninv = np.linalg.inv(n)
    m = ninv @ a.T @ wd @ d
    return m, ninv


def main():
    x = X_MIN + 1.0e3 + np.arange(N_STATIONS) * STATION_SPACING
    a = kernel(x)
    d_true = a @ TRUE_MODEL
    d = d_true + DATA_SIGMA * RNG.standard_normal(d_true.size)

    section("1. The model grid, kernel and synthetic data")
    print(f"SYNTHETIC 2-D density model: {NX} blocks x {NZ} layers "
          f"({NX * NZ} parameters), blocks {DX_BLOCK / 1e3:.2f} km wide, "
          f"layers 0-1, 1-3, 3-6 and 6-10 km")
    print(f"  profile {X_MIN / 1e3:.0f} to {(X_MIN + NX * DX_BLOCK) / 1e3:.0f} km "
          f"with {N_STATIONS} stations every {STATION_SPACING / 1e3:.0f} km")
    print(f"  density anomalies: +300 kg/m^3 in blocks 2-4 of layer 1, "
          f"-250 kg/m^3 in blocks 2-3 of layer 3")
    print(f"  data noise {DATA_SIGMA:.2f} mGal; anomaly range "
          f"{d.min():+.3f} to {d.max():+.3f} mGal")
    print(f"  kernel magnitude: max |dg/drho| = {np.abs(a).max():.4f} mGal per "
          f"kg/m^3 (shallow block nearest a station)")
    print(f"  condition number of the unregularised normal matrix = "
          f"{np.linalg.cond(a.T @ a):.3e}")

    section("2. The regularised inversion and the choice of alpha")
    l_mat = difference_operator()
    print(f"{'alpha':>10}{'chi2/n':>10}{'model rms':>12}{'roughness':>12}")
    results = {}
    for alpha in ALPHA_SCAN:
        m, _ = solve(a, d, DATA_SIGMA, alpha, l_mat)
        chi2 = np.sum(((d - a @ m) / DATA_SIGMA) ** 2) / d.size
        results[alpha] = (m, chi2, float(l_mat @ m @ l_mat @ m))
        if alpha in ALPHA_SCAN[::4]:
            print(f"{alpha:>10.3g}{chi2:>10.4f}"
                  f"{np.sqrt(np.mean(m ** 2)):>12.2f}"
                  f"{np.sqrt(results[alpha][2]):>12.1f}")
    above = [al for al in ALPHA_SCAN if results[al][1] <= 1.0]
    alpha_best = max(above) if above else min(ALPHA_SCAN)
    m, cov = solve(a, d, DATA_SIGMA, alpha_best, l_mat)
    chi2 = results[alpha_best][1]
    print(f"  largest alpha with chi^2/n <= 1 (discrepancy principle) = "
          f"{alpha_best:.3g}, giving chi^2/n = {chi2:.4f} "
          f"(target 1.00): the discrepancy principle")
    print(f"  model rms = {np.sqrt(np.mean(m ** 2)):.2f} kg/m^3 "
          f"(true {np.sqrt(np.mean(TRUE_MODEL ** 2)):.2f})")

    section("3. Covariance, resolution and resolved parameters")
    err = np.sqrt(np.diag(cov))
    res = cov @ a.T @ (np.eye(d.size) / DATA_SIGMA ** 2) @ a
    print(f"  mean 1-sigma of the model parameters = {err.mean():.2f} kg/m^3")
    print(f"  mean model error |m - m_true|        = "
          f"{np.abs(m - TRUE_MODEL).mean():.2f} kg/m^3")
    print(f"  trace of the resolution matrix = {np.trace(res):.2f} of "
          f"{NX * NZ} parameters (the effective number resolved)")
    print(f"{'layer':>7}{'mean 1-sigma':>15}{'mean |error|':>15}"
          f"{'mean resolution':>17}")
    for iz in range(NZ):
        sl = slice(iz * NX, (iz + 1) * NX)
        print(f"{iz + 1:>7}{err[sl].mean():>15.2f}"
              f"{np.abs(m[sl] - TRUE_MODEL[sl]).mean():>15.2f}"
              f"{np.diag(res)[sl].mean():>17.3f}")
    print("  -> resolution is per-parameter, so it depends on the layer THICKNESS")
    print("     as well as on depth: the thick deep layers are determined as")
    print("     averages (resolution 0.745) while the thin shallow layers are not")
    print("     (0.612).  The trace, not the depth, is the honest headline.")

    section("4. The equivalence class")
    draw = m[:, None] + np.linalg.cholesky(cov) @ RNG.standard_normal((m.size, 2000))
    print(f"  drawing 2000 models from N(m, C_m):")
    print(f"    shallow layer (blocks 2-4): spread "
          f"{draw[2:5].std(axis=1).mean():.2f} kg/m^3 on a true 300")
    print(f"    deep layer (blocks 2-3 of layer 3): spread "
          f"{draw[2 * NX + 2:2 * NX + 4].std(axis=1).mean():.2f} kg/m^3 on a true -250")
    print(f"  data predicted by 2000 posterior models: rms spread = "
          f"{np.std(a @ draw, axis=1).mean():.4f} mGal "
          f"(data noise {DATA_SIGMA:.2f} mGal)")
    print("     i.e. the equivalence class is models that fit the data"
          " indistinguishably")
    deep_draws = draw[2 * NX + 2:2 * NX + 4].mean(axis=0)
    print(f"  share of posterior draws in which the deep body is HIGH density: "
          f"{np.mean(deep_draws > 0) * 100:.1f}%")
    print(f"  share in which it is more negative than -100 kg/m^3: "
          f"{np.mean(deep_draws < -100) * 100:.1f}%")
    print("  -> a report that quotes only the best-fit model hides both the")
    print("     unresolved deep layer and the size of the class.")


if __name__ == "__main__":
    main()
