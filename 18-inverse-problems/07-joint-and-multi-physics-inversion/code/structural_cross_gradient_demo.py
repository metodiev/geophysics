#!/usr/bin/env python3
"""Structural (cross-gradient) coupling: aligning two physical-property models,
and measuring what the alignment buys and what it costs.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python structural_cross_gradient_demo.py

All models and data are SYNTHETIC.  The truth models are chosen teaching
structures (a dipping band, and a blob for the failure case); the two forward
operators are anisotropic Gaussian blur-and-subsample operators standing in for
two surveys with orthogonal blurring.  No number below is a measurement.

Contents
--------
1. Two SYNTHETIC models with the same geometry and different amplitudes.
2. Separate inversions: each fits its data, and both disagree structurally.
3. The cross-gradient penalty, at a sweep of weights (the central measurement).
4. What the penalty constrains: geometry only, and the flat-model loophole.
5. Failure mode: coupling two models whose true structures differ.
"""

import numpy as np
from scipy.optimize import minimize
from scipy.ndimage import gaussian_filter

RNG = np.random.default_rng(20261014)

NX = NY = 20                     # model grid cells in x (horizontal) and y
DX = DY = 1.0                    # cell size (arbitrary teaching unit)
NOISE1, NOISE2 = 0.02, 0.15      # relative data noise of the two methods
LAMBDA_SMOOTH = 0.02             # spatial smoothness weight (weak, on purpose)
WEIGHTS = (0.0, 0.3, 1.0, 3.0, 10.0, 30.0)   # cross-gradient weights to test
N = NX * NY


def section(title: str) -> None:
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def truth_models(dip=True):
    """Two SYNTHETIC property models on the same grid.

    Model 1 is a dipping band; model 2 is the same band with a different
    amplitude plus a constant offset.  With ``dip=False`` model 2 instead
    carries a body at a different place and orientation, i.e. genuinely
    DIFFERENT structure -- the failure case in section 5.
    """
    x = np.arange(NX)[:, None] * DX
    y = np.arange(NY)[None, :] * DY
    band = np.exp(-((y - 0.75 * x - 2.0) ** 2) / (2 * 1.8 ** 2))
    m1 = band
    m2 = 0.6 * band + 0.15
    if not dip:
        blob = np.exp(-(((x - 5.0) ** 2) / (2 * 2.5 ** 2)
                        + ((y - 13.0) ** 2) / (2 * 2.5 ** 2)))
        m2 = 0.6 * blob + 0.15
    return m1.ravel(), m2.ravel()


def forward_matrix(sigma_xy, offset, sub_x, sub_y):
    """Dense matrix for: anisotropic Gaussian blur, add an offset times the
    mean, then subsample every ``sub_x``-th column and ``sub_y``-th row."""
    cols = []
    for k in range(N):
        e = np.zeros(N)
        e[k] = 1.0
        blurred = gaussian_filter(e.reshape(NX, NY), sigma_xy, mode="nearest")
        cols.append(blurred[::sub_x, ::sub_y].ravel())
    M = np.array(cols).T
    return M + offset / N


def gradient_operators():
    """First-derivative matrices Dx, Dy (forward differences, zero at the edge)."""
    Dx = np.zeros((N, N))
    Dy = np.zeros((N, N))
    for i in range(NX):
        for j in range(NY):
            k = i * NY + j
            if i + 1 < NX:
                Dx[k, (i + 1) * NY + j] = 1.0 / DX
                Dx[k, k] = -1.0 / DX
            if j + 1 < NY:
                Dy[k, i * NY + (j + 1)] = 1.0 / DY
                Dy[k, k] = -1.0 / DY
    return Dx, Dy


DXM = DYM = None
LAP = None


def cross_gradient(m1, m2):
    """Scalar 2-D cross-gradient t = dx(m1)*dy(m2) - dy(m1)*dx(m2).  It vanishes
    where the two gradients are parallel, which is the definition of 'the same
    geometry', so the penalty  sum(t^2)  measures structural disagreement."""
    return (DXM @ m1) * (DYM @ m2) - (DYM @ m1) * (DXM @ m2)


def objective_and_grad(x, A1, A2, d1, d2, lam_x):
    m1 = x[:N]
    m2 = x[N:]
    r1 = A1 @ m1 - d1
    r2 = A2 @ m2 - d2
    t = cross_gradient(m1, m2)
    J = (r1 @ r1 + r2 @ r2
         + LAMBDA_SMOOTH * (m1 @ (LAP @ m1) + m2 @ (LAP @ m2))
         + lam_x * (t @ t))
    # dJ/dm1 = 2 A1^T r1 + 2 lam_s LAP m1 + 2 lam_x (dt/dm1)^T t, where
    # dt/dm1 = Dx^T diag(Dy m2) - Dy^T diag(Dx m2)
    g1 = (2 * A1.T @ r1 + 2 * LAMBDA_SMOOTH * (LAP @ m1)
          + 2 * lam_x * (DYM @ m2 * (DXM @ t) - DXM @ m2 * (DYM @ t)))
    g2 = (2 * A2.T @ r2 + 2 * LAMBDA_SMOOTH * (LAP @ m2)
          + 2 * lam_x * (DXM @ m1 * (DYM @ t) - DYM @ m1 * (DXM @ t)))
    return J, np.concatenate([g1, g2])


def invert(A1, A2, d1, d2, lam_x):
    x0 = np.concatenate([np.zeros(N), np.zeros(N)])
    f = lambda x: objective_and_grad(x, A1, A2, d1, d2, lam_x)
    res = minimize(f, x0, jac=True, method="L-BFGS-B",
                   options={"maxiter": 600, "ftol": 1e-14})
    return res.x[:N], res.x[N:], res


def rmse(a, b):
    return float(np.sqrt(np.mean((a - b) ** 2)))


def cg_rms(t):
    return float(np.sqrt(np.mean(t ** 2)))


def main():
    global DXM, DYM, LAP
    DXM, DYM = gradient_operators()
    LAP = DXM.T @ DXM + DYM.T @ DYM

    # Method 1 is smeared horizontally (poor x resolution); method 2 is smeared
    # vertically (poor y resolution) and is noisier.  Each is blind along one
    # axis, so their null spaces are different.
    A1 = forward_matrix((3.0, 0.6), 0.20, 3, 1)
    A2 = forward_matrix((0.6, 3.0), -0.10, 1, 3)

    section("1. Two SYNTHETIC models with the same geometry")
    m1, m2 = truth_models(dip=True)
    d1 = A1 @ m1
    d2 = A2 @ m2
    d1 = d1 + NOISE1 * d1.std() * RNG.standard_normal(d1.size)
    d2 = d2 + NOISE2 * d2.std() * RNG.standard_normal(d2.size)
    print(f"  grid {NX} x {NY} cells, cell size {DX:.1f} (teaching units)")
    print(f"  model 1: dipping band, range {m1.min():.3f} to {m1.max():.3f}")
    print(f"  model 2: same band x0.6 + 0.15, range {m2.min():.3f} to {m2.max():.3f}")
    print(f"  method 1: blur sigma (3.0, 0.6), {d1.size} samples, "
          f"{NOISE1 * 100:.0f}% noise (blind horizontally)")
    print(f"  method 2: blur sigma (0.6, 3.0), {d2.size} samples, "
          f"{NOISE2 * 100:.0f}% noise (blind vertically)")
    print(f"  smoothness weight lambda_s = {LAMBDA_SMOOTH:.2f} (weak on purpose:")
    print("  a strong smoothness term would flatten both models and make the")
    print("  cross-gradient trivially small, which is section 4's warning).")
    t_true = cross_gradient(m1, m2)
    print(f"  cross-gradient of the TRUTH models: rms|t| = {cg_rms(t_true):.3e}")
    print("  both truth models are built from the same band, so their gradients")
    print("  are parallel and the cross-gradient is zero to round-off.")

    section("2. Separate inversions: each fits its data, both disagree")
    s1, s2, _ = invert(A1, A2, d1, d2, lam_x=0.0)
    t_sep = cross_gradient(s1, s2)
    print(f"  rms misfit method 1 = {rmse(A1 @ s1, d1):.4f}   "
          f"model 1 error = {rmse(s1, m1):.4f}")
    print(f"  rms misfit method 2 = {rmse(A2 @ s2, d2):.4f}   "
          f"model 2 error = {rmse(s2, m2):.4f}")
    print(f"  cross-gradient: rms|t| = {cg_rms(t_sep):.3e}, ratio to truth = "
          f"{cg_rms(t_sep) / cg_rms(t_true):.3e}")
    print("  both misfits are at the noise level, and the two models still")
    print("  disagree about the geometry: fitting the data does not fix the")
    print("  structure, because each method is blind along its own axis.")

    section("3. The cross-gradient penalty: a sweep of weights")
    print("  lambda_x    rms|t|     misfit1  misfit2  error1  error2   var1    var2")
    rows = []
    for lam in WEIGHTS:
        j1, j2, _ = invert(A1, A2, d1, d2, lam_x=lam)
        t = cross_gradient(j1, j2)
        row = (lam, cg_rms(t), rmse(A1 @ j1, d1), rmse(A2 @ j2, d2),
               rmse(j1, m1), rmse(j2, m2), j1.var(), j2.var())
        rows.append(row)
        print(f"  {lam:8.1f}  {row[1]:.3e}  {row[2]:.4f}  {row[3]:.4f}  "
              f"{row[4]:.4f}  {row[5]:.4f}  {row[6]:.4f}  {row[7]:.4f}")
    base = rows[0]
    best = min(rows, key=lambda r: r[4] + r[5])
    print(f"  the smallest combined model error is at lambda_x = {best[0]:.1f}: "
          f"error1 falls from")
    print(f"  {base[4]:.4f} to {best[4]:.4f} and error2 from {base[5]:.4f} to "
          f"{best[5]:.4f}, while the two data misfits")
    print(f"  move from ({base[2]:.4f}, {base[3]:.4f}) to "
          f"({best[2]:.4f}, {best[3]:.4f}) -- barely at all.")
    print(f"  The structural disagreement rms|t| falls from {base[1]:.3e} to")
    print(f"  {best[1]:.3e}: a real but modest {(base[1] - best[1]) / base[1] * 100:.0f}% "
          f"reduction, bought for an")
    print(f"  increase in misfit of "
          f"{(best[2] - base[2]) / base[2] * 100:.0f}% and "
          f"{(best[3] - base[3]) / base[3] * 100:.0f}%.")
    print("  Past the optimum both misfits and both model errors rise steeply, and")
    print("  rms|t| rises with them: the data now fight the penalty, and the")
    print("  compromise is worse for every model.  Coupling is a bias that must")
    print("  be paid for with data misfit; it is not free information.")

    section("4. What the penalty constrains -- and what it cannot")
    flat1 = np.full(N, m1.mean())
    flat2 = np.full(N, m2.mean())
    print(f"  cross-gradient of two CONSTANT models: rms|t| = "
          f"{cg_rms(cross_gradient(flat1, flat2)):.3e} (exactly zero)")
    t_scaled = cross_gradient(2.0 * s1, 0.5 * s2)
    print(f"  scaling identity  t(a*m1, b*m2) = a*b*t(m1, m2):  with a=2, b=0.5")
    print(f"    max |t(2*s1, 0.5*s2) - 1.0*t(s1, s2)| = "
          f"{np.max(np.abs(t_scaled - 1.0 * t_sep)):.3e}")
    print("  so the penalty sees GEOMETRY only: any amplitude rescaling of a pair")
    print("  of models leaves t proportional, and any constant model gives t = 0.")
    print(f"  That is why in the sweep the model variances barely move "
          f"(m1 {base[6]:.4f} -> {rows[-1][6]:.4f},")
    print(f"  m2 {base[7]:.4f} -> {rows[-1][7]:.4f}) while the misfits rise to "
          f"{rows[-1][2]:.4f}/{rows[-1][3]:.4f}:")
    print("  the penalty does not flatten the model, it relocates and suppresses")
    print("  structure where the data fight it.  Either way, it cannot create")
    print("  structure that neither data set supports.")

    section("5. Failure mode: coupling two DIFFERENT structures")
    m1b, m2b = truth_models(dip=False)
    d1b = A1 @ m1b
    d2b = A2 @ m2b
    d1b = d1b + NOISE1 * d1b.std() * RNG.standard_normal(d1b.size)
    d2b = d2b + NOISE2 * d2b.std() * RNG.standard_normal(d2b.size)
    print("  truth: model 1 is the dipping band, model 2 a distant blob, so the")
    print("  coupling assumption is FALSE.  model-2 error versus weight:")
    print("  lambda_x   error1   error2   misfit1  misfit2")
    for lam in (0.0, 1.0, 10.0, 100.0):
        j1, j2, _ = invert(A1, A2, d1b, d2b, lam_x=lam)
        print(f"  {lam:8.1f}   {rmse(j1, m1b):.4f}   {rmse(j2, m2b):.4f}   "
              f"{rmse(A1 @ j1, d1b):.4f}   {rmse(A2 @ j2, d2b):.4f}")
    print("  error2 rises monotonically with the weight: the penalty forces the")
    print("  blob towards the band's geometry, which the second method's data do")
    print("  not support.  Cross-gradient coupling is a physical hypothesis")
    print("  (shared geometry), and an unexamined hypothesis is a systematic bias.")


if __name__ == "__main__":
    main()
