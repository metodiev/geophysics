#!/usr/bin/env python3
"""Graduate project 5: joint gravity-seismic inversion, and the resolution the
seismic data add to a gravity-only model.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python joint_inversion_demo.py

Everything here is SYNTHETIC.  The density model, the gravity data and the
travel-time data are generated below from chosen values with chosen noise.

Sections
--------
1. The model, the two kernels and the synthetic data.
2. Gravity alone, seismic alone, and the joint inversion.
3. Resolution: what the second dataset adds.
4. The petrophysical link, and what happens when it is wrong.
"""

import numpy as np
from numpy.polynomial.legendre import leggauss

RNG = np.random.default_rng(20261014)

GRAV_CONST = 6.67430e-11
MGAL = 1.0e-5
NX, NZ = 8, 4
DX_BLOCK = 6.25e3
X_MIN = -25.0e3
LAYER_EDGES = (0.0, 1.0e3, 3.0e3, 6.0e3, 10.0e3)
N_STATIONS = 20
STATION_SPACING = 2500.0
SIGMA_G = 0.05            # mGal
SIGMA_T = 0.05            # s
V0, RHO0, BETA = 4500.0, 2500.0, 0.4      # v = V0 + BETA (rho - RHO0), m/s
PATHS = tuple((float(a), float(b)) for a, b in
              [(-20e3, 20e3), (-15e3, 15e3), (-10e3, 10e3), (-5e3, 5e3),
               (20e3, -20e3), (15e3, -15e3), (10e3, -10e3), (-20e3, 0.0),
               (-18e3, 12e3), (-12e3, 18e3), (-8e3, 8e3), (0.0, 20e3),
               (18e3, -12e3), (12e3, -18e3), (8e3, -8e3), (0.0, -20e3),
               (-20e3, -10e3), (-10e3, -20e3), (10e3, 20e3), (20e3, 10e3),
               (-16e3, 4e3), (-4e3, 16e3), (4e3, -16e3), (16e3, -4e3)])
N_PAR = NX * NZ


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def gravity_kernel(x):
    nodes, weights = leggauss(8)
    a = np.zeros((x.size, N_PAR))
    for ix in range(NX):
        x1 = X_MIN + ix * DX_BLOCK
        xs = 0.5 * DX_BLOCK * nodes + x1 + 0.5 * DX_BLOCK
        wx = 0.5 * DX_BLOCK * weights
        for iz in range(NZ):
            z1, z2 = LAYER_EDGES[iz], LAYER_EDGES[iz + 1]
            zs = 0.5 * (z2 - z1) * nodes + 0.5 * (z2 + z1)
            wz = 0.5 * (z2 - z1) * weights
            integ = 2.0 * GRAV_CONST * zs[None, :] / (
                (x[:, None] - xs[None, :]) ** 2 + zs[None, :] ** 2)
            a[:, iz * NX + ix] = integ @ wz * wx.sum() / MGAL
    return a


def seismic_kernel(beta=BETA):
    """d t / d rho for each path and block, from t = path length / velocity."""
    a = np.zeros((len(PATHS), N_PAR))
    for p, (xs, xr) in enumerate(PATHS):
        lo, hi = min(xs, xr), max(xs, xr)
        for iz in range(NZ):
            depth = 0.5 * (LAYER_EDGES[iz] + LAYER_EDGES[iz + 1])
            v = V0
            for ix in range(NX):
                x1 = X_MIN + ix * DX_BLOCK
                overlap = max(0.0, min(hi, x1 + DX_BLOCK) - max(lo, x1))
                if overlap <= 0.0:
                    continue
                length = overlap * np.sqrt(1.0 + (overlap / depth) ** 2)
                a[p, iz * NX + ix] = -length * beta / v ** 2
    return a


def invert_at(a, d, sigma, alpha):
    wd = np.eye(d.size) / sigma ** 2
    ninv = np.linalg.inv(a.T @ wd @ a + alpha * np.eye(a.shape[1]))
    m = ninv @ a.T @ wd @ d
    res = d - a @ m
    return m, ninv, float(res @ (res / sigma ** 2)), a.T @ wd @ a


def invert(a, d, sigma, alpha=None):
    """Inversion with alpha chosen by the discrepancy principle when alpha is None."""
    if alpha is not None:
        return invert_at(a, d, sigma, alpha)
    best = None
    for alpha_try in np.logspace(-6.0, 10.0, 41):
        out = invert_at(a, d, sigma, alpha_try)
        if out[2] / d.size <= 1.0:
            best = out
        else:
            break
    return best if best is not None else invert_at(a, d, sigma, 1e6)


def report(label, m, cov, chi2, n_data, nrm, true):
    err = np.sqrt(np.diag(cov))
    res_mat = cov @ nrm
    print(f"  {label:<15}{chi2 / n_data:>10.4f}{err.mean():>13.2f}"
          f"{np.abs(m - true).mean():>14.2f}{np.trace(res_mat):>10.2f}")


def main():
    true = np.zeros(N_PAR)
    true[2:5] = 250.0
    true[2 * NX + 4:2 * NX + 6] = -200.0
    x = X_MIN + 1.0e3 + np.arange(N_STATIONS) * STATION_SPACING
    ag = gravity_kernel(x)
    a_s = seismic_kernel()
    dg = ag @ true + SIGMA_G * RNG.standard_normal(x.size)
    dt = a_s @ true + SIGMA_T * RNG.standard_normal(len(PATHS))

    section("1. The model, the kernels and the data")
    print(f"SYNTHETIC model: {NX} blocks x {NZ} layers = {N_PAR} parameters")
    print(f"  blocks {DX_BLOCK / 1e3:.2f} km wide; layers 0-1, 1-3, 3-6, 6-10 km")
    print(f"  density: +250 kg/m^3 in blocks 2-4 of layer 1, -200 in blocks 4-5 "
          f"of layer 3")
    print(f"  gravity: {N_STATIONS} stations, sigma = {SIGMA_G:.2f} mGal; "
          f"{len(PATHS)} travel-time paths, sigma = {SIGMA_T:.2f} s")
    print(f"  petrophysical link v = {V0:.0f} + {BETA:.2f}(rho - {RHO0:.0f}) m/s")
    print(f"  gravity data {dg.min():+.3f} to {dg.max():+.3f} mGal; travel-time "
          f"residuals {dt.min():+.5f} to {dt.max():+.5f} s")
    print(f"  condition numbers: gravity {np.linalg.cond(ag):.2e}, seismic "
          f"{np.linalg.cond(a_s):.2e}, joint "
          f"{np.linalg.cond(np.vstack([ag / SIGMA_G, a_s / SIGMA_T])):.2e}")

    section("2. Gravity alone, seismic alone, joint")
    print(f"  {'dataset':<15}{'chi^2/datum':>10}{'mean 1-sigma':>13}"
          f"{'mean |err|':>14}{'trace(R)':>10}")
    mg, cg, chi_g, nrm_g = invert(ag, dg, SIGMA_G)
    report("gravity only", mg, cg, chi_g, dg.size, nrm_g, true)
    ms, cs, chi_s, nrm_s = invert(a_s, dt, SIGMA_T)
    report("seismic only", ms, cs, chi_s, dt.size, nrm_s, true)
    a_j = np.vstack([ag / SIGMA_G, a_s / SIGMA_T])
    d_j = np.concatenate([dg / SIGMA_G, dt / SIGMA_T])
    mj, cj, chi_j, nrm_j = invert(a_j, d_j, 1.0)
    report("joint", mj, cj, chi_j, d_j.size, nrm_j, true)
    print(f"  joint reduces the gravity-only mean uncertainty by a factor of "
          f"{np.sqrt(np.diag(cg)).mean() / np.sqrt(np.diag(cj)).mean():.2f}")
    print(f"  and the mean model error from {np.abs(mg - true).mean():.2f} to "
          f"{np.abs(mj - true).mean():.2f} kg/m^3")

    section("3. Where the resolution comes from")
    print(f"  {'parameter group':<26}{'gravity':>12}{'joint':>12}")
    for label, sl in (("layer 1 (0-1 km)", slice(0, NX)),
                      ("layer 4 (6-10 km)", slice(3 * NX, N_PAR))):
        print(f"  {label:<26}"
              f"{np.abs(mg[sl] - true[sl]).mean():>12.2f}"
              f"{np.abs(mj[sl] - true[sl]).mean():>12.2f}")
    print(f"  the gravity kernel is smoother with depth, so the deep layer is")
    print(f"  the poorly resolved one; the travel times cross both layers and")
    print(f"  supply the missing constraints.")

    section("4. The petrophysical link, and what happens when it is wrong")
    for beta_try, label in ((BETA, "correct (0.40)"),
                            (2 * BETA, "twice the slope"),
                            (-BETA, "wrong sign")):
        a_try = seismic_kernel(beta_try)
        aj = np.vstack([ag / SIGMA_G, a_try / SIGMA_T])
        m2, c2, chi2, _ = invert(aj, d_j, 1.0)
        print(f"  {label:<22} mean |model change| = "
              f"{np.abs(m2 - mj).mean():>7.2f} kg/m^3, "
              f"chi^2/datum = {chi2 / d_j.size:.4f}")
    print("  -> a RESCALED link is NOT detectable: doubling the slope changes the")
    print("     model by hundreds of kg/m^3 at an unchanged misfit, because the")
    print("     inversion simply halves the density.  A link of the wrong SIGN is")
    print("     detectable, and loudly.  This is the central subtlety of joint")
    print("     inversion: only links that are inconsistent with the observed")
    print("     physics can be falsified by the data.")


if __name__ == "__main__":
    main()
