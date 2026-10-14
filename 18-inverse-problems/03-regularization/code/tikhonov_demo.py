#!/usr/bin/env python3
"""Tikhonov regularisation: the SVD filter factors, the exact bias-variance
decomposition, and the measured resolution/roughness trade-off.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python tikhonov_demo.py

All models and data are SYNTHETIC: the exact 2-D line-mass gravity kernel of a
textbook forward model, a chosen density distribution, a chosen station grid and
computer-generated noise.  No measured data and no published numbers are used.

Convention: the problem is put in STANDARD FORM first.  The kernel is divided by
its spectral norm sigma_1 and the model by its Euclidean norm, and the data are
divided by s1*||m_true|| so that K_hat m_hat = d_hat exactly.  After that the
regularisation parameter alpha is dimensionless and can be swept over decades.
Every error statistic is reported relative to ||m_true||, so it is a relative
model error in the physical model.

Contents
--------
1. The synthetic problem and the standard-form rescaling.
2. Verification of the filter-factor formula against a direct solve.
3. Filter factors: which model components survive, and effective parameters.
4. The exact bias-variance decomposition, checked by Monte Carlo.
5. Resolution: the diagonals and the spread of the point-spread functions.
6. Roughness penalty L = D against L = I, averaged over noise realisations.
"""

import numpy as np

RNG = np.random.default_rng(20261014)
G_CONST = 6.67430e-11
MGAL = 1.0e5


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def line_mass_kernel(x_obs_m, x_src_m, depth_m):
    """2-D line-mass gravity kernel in mGal per (kg/m); see the lesson."""
    dx = x_obs_m[:, None] - x_src_m[None, :]
    return 2.0 * G_CONST * depth_m / (dx**2 + depth_m**2) * MGAL


def rel_err(m, m_true):
    return np.linalg.norm(m - m_true) / np.linalg.norm(m_true)


def psf_spread(R, x, i):
    """Second-moment spread of the i-th point-spread function, in metres."""
    w = R[i] ** 2
    return float(np.sqrt(np.sum(w * (x - x[i]) ** 2) / np.sum(w)))


def main():
    # ------------------------------------------------------------- 1. problem
    n, depth = 64, 600.0
    x = np.linspace(-4000.0, 4000.0, n)
    K_phys = line_mass_kernel(x, x, depth)
    m_true = 1.0e9 * np.exp(-(x / 1500.0) ** 2)           # kg/m
    d_true = K_phys @ m_true                              # mGal
    noise = 0.005 * np.abs(d_true).max()                  # mGal

    U, sv, Vt = np.linalg.svd(K_phys)
    V = Vt.T
    s1 = sv[0]
    norm_m = np.linalg.norm(m_true)
    K = K_phys / s1                                       # ||K||_2 = 1
    norm_d = s1 * norm_m
    m_hat = m_true / norm_m
    d_hat = d_true / norm_d                               # = K @ m_hat exactly
    sig = noise / norm_d                                  # noise sigma per datum
    y = U.T @ d_hat
    xc = V.T @ m_hat
    sh = sv / s1

    section("1. The synthetic problem, in standard form")
    print(f"  kernel : 2-D line masses at {depth / 1e3:.2f} km depth, {n} stations")
    print(f"           and {n} cells, spacing {x[1] - x[0]:.1f} m")
    print(f"  sigma_1(K) = {s1:.5e} mGal per (kg/m), kappa_2(K) = "
          f"{sv[0] / sv[-1]:.3e}")
    print(f"  true model : peak {m_true.max():.3e} kg/m, ||m_true|| = "
          f"{norm_m:.4e} kg/m")
    print(f"  exact data : peak {d_true.max():.2f} mGal, ||d|| = {norm_d:.4e} mGal")
    print(f"  noise      : sigma = {noise:.4f} mGal per datum "
          f"({noise / np.abs(d_true).max() * 100:.2f}% of the peak anomaly)")
    print(f"  standard form: sigma_hat_i = sigma_i/sigma_1 in [{sh[-1]:.3e}, 1], "
          f"sigma = {sig:.4e}")
    print(f"  check K_hat m_hat = d_hat: residual "
          f"{np.linalg.norm(K @ m_hat - d_hat):.3e}")
    print("  alpha below is quoted as alpha/sigma_1^2 contraction-free and is")
    print("  dimensionless; all model errors are relative to ||m_true||.")

    # ------------------------------------------- 2. verify filter-factor formula
    section("2. Verification: filter factors against a direct solve")
    a_test = 1.0e-6
    f = sh**2 / (sh**2 + a_test)
    m_svd = V @ (f * y / sh) * norm_m
    m_dir = np.linalg.solve(K.T @ K + a_test * np.eye(n), K.T @ d_hat) * norm_m
    print(f"  alpha = {a_test:.1e}")
    print(f"  ||m_svd - m_direct|| / ||m_direct|| = "
          f"{np.linalg.norm(m_svd - m_dir) / np.linalg.norm(m_dir):.3e}")
    print("  m_alpha = sum_i f_i (u_i^T d / sigma_i) v_i,   "
          "f_i = sigma_i^2/(sigma_i^2 + alpha)")
    print("  f_i -> 1 when sigma_i^2 >> alpha (data-dominated);")
    print("  f_i -> sigma_i^2/alpha -> 0 when sigma_i^2 << alpha (penalty-dominated).")
    print("  The filter factors are a low-pass filter on the model spectrum.  That")
    print("  is where the smoothing comes from, and it is imposed on the model, not")
    print("  on the data: the data are never altered.")

    # ------------------------------------------- 3. filter factors at three alph
    section("3. Filter factors: which model components survive")
    print("     i    sigma_i/sigma_1   f_i(a=1e-9)   f_i(a=1e-6)   f_i(a=1e-3)"
          "   true |x_i|")
    for i in (0, 1, 2, 4, 6, 8, 10, 14, 20, 30, 45, 63):
        row = [sh[i] ** 2 / (sh[i] ** 2 + a) for a in (1e-9, 1e-6, 1e-3)]
        print(f"  {i + 1:5d}  {sh[i]:12.5e}   {row[0]:11.5f}   {row[1]:11.5f}   "
              f"{row[2]:11.5f}   {abs(xc[i]):11.3e}")
    print("\n   alpha   count(f_i > 0.5)   sum f_i (effective parameters)")
    for a in (1e-12, 1e-9, 1e-7, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2):
        fv = sh**2 / (sh**2 + a)
        print(f"  {a:7.0e}   {int((fv > 0.5).sum()):16d}   {fv.sum():23.3f}")
    print("  The model components that survive are those the data can support;")
    print("  sum f_i is the number of parameters the solution is actually using.")

    # ------------------------------------------- 4. bias-variance decomposition
    section("4. Exact bias-variance decomposition, checked by Monte Carlo")
    print("  m_alpha - m_true = sum_i [(f_i - 1) x_i + f_i e_i/sigma_i] v_i, so")
    print("     E||bias||^2  = sum_i (1-f_i)^2 x_i^2")
    print("     E||noise||^2 = sigma^2 sum_i (f_i/sigma_i)^2")
    print("  both relative to ||m_true||^2 = 1 in standard form.")
    n_real = 400
    E = RNG.standard_normal((n_real, n))
    Y = y[None, :] + E * sig                        # y_i for every realisation
    alphas = np.logspace(-14, 0, 57)
    pred = np.empty(alphas.size)
    bias2 = np.empty(alphas.size)
    var = np.empty(alphas.size)
    npar = np.empty(alphas.size)
    meas = np.empty(alphas.size)
    for j, a in enumerate(alphas):
        fv = sh**2 / (sh**2 + a)
        bias2[j] = np.sum((1.0 - fv) ** 2 * xc**2)
        var[j] = sig**2 * np.sum((fv / sh) ** 2)
        pred[j] = bias2[j] + var[j]
        npar[j] = fv.sum()
        m_r = (Y * fv[None, :] / sh[None, :]) @ V.T
        meas[j] = np.mean(np.sum((m_r - m_hat[None, :]) ** 2, axis=1))
    print("\n   alpha     bias^2      variance    predicted total    measured mean"
          "   eff. params")
    for a in (1e-12, 1e-9, 1e-8, 1e-7, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1):
        j = int(np.argmin(np.abs(alphas - a)))
        print(f"  {a:7.0e}  {bias2[j]:10.3e}  {var[j]:10.3e}  {pred[j]:13.5e}   "
              f"{meas[j]:13.5e}   {npar[j]:9.3f}")
    j_ora, j_emp = int(np.argmin(pred)), int(np.argmin(meas))
    keep = pred > 1e-2 * pred.max()
    print(f"\n  analytic oracle alpha = {alphas[j_ora]:.3e}: "
          f"bias^2 = {bias2[j_ora]:.3e}, variance = {var[j_ora]:.3e}, "
          f"expected relative error = {np.sqrt(pred[j_ora]):.5f}")
    print(f"  empirical  alpha      = {alphas[j_emp]:.3e}: measured relative "
          f"error = {np.sqrt(meas[j_emp]):.5f}")
    print(f"  max |measured-predicted|/predicted where predicted > 0.01 max = "
          f"{np.max(np.abs(meas[keep] - pred[keep]) / pred[keep]):.3f}")
    print("  The decomposition is exact for this estimator and the Monte Carlo")
    print("  reproduces it.  The optimum is interior: bias^2 grows monotonically")
    print("  with alpha while the variance falls monotonically, and the sum has a")
    print("  minimum.  The oracle alpha uses the unknown true model, so it is not")
    print("  available in practice.  It is only a benchmark for the rules that are.")

    # ------------------------------------------------------------- 5. resolution
    section("5. Resolution: point-spread functions")
    print("  R = (K^T K + alpha I)^-1 K^T K = V diag(f_i) V^T; row i of R is the")
    print("  point-spread function of cell i, and for a hard kernel R = I.")
    print("\n   alpha    sum f_i   mean diag(R)   PSF spread at centre (m)"
          "   measured ||err||/||m||")
    for a in (1e-12, 1e-9, 1e-7, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1):
        fv = sh**2 / (sh**2 + a)
        R = (V * fv) @ V.T
        spread = psf_spread(R, x, n // 2)
        j = int(np.argmin(np.abs(alphas - a)))
        print(f"  {a:7.0e}   {fv.sum():7.3f}   {np.mean(np.diag(R)):12.4f}   "
              f"{spread:26.1f}   {np.sqrt(meas[j]):21.5f}")
    print("  Resolution and variance are coupled: each increment of alpha reduces")
    print("  the variance and widens the point-spread function.  No alpha improves")
    print("  both.  The 'best' alpha therefore cannot be defined without saying")
    print("  which of the two the interpreter cares about.")

    # --------------------------------------------------- 6. roughness penalty
    section("6. Roughness penalty L = D against L = I")
    dx_m = float(x[1] - x[0])
    D = np.diff(np.eye(n), axis=0) / dx_m              # first difference, 1/m
    D = D / np.linalg.norm(D, 2)                       # normalise: alpha comparable
    DtD = D.T @ D
    print(f"  D is {D.shape[0]} x {D.shape[1]}, a first difference divided by the")
    print(f"  {dx_m:.1f} m cell size, then normalised to ||D||_2 = 1 so that alpha")
    print("  multiplies a unit-norm operator in both cases.")
    print("  D^T D is singular (its null space is the constant model), so the L=D")
    print("  penalty is on ROUGHNESS, not on magnitude.  The data still constrain")
    print("  the mean; a penalty on roughness alone cannot.")
    n_real2 = 60
    E2 = RNG.standard_normal((n_real2, n))
    Y2 = y[None, :] + E2 * sig
    Dhat = d_hat[None, :] + sig * (E2 @ U.T)          # noisy data, n_real2 rows
    alphas2 = np.logspace(-12, 1, 53)
    eI = np.empty(alphas2.size)
    eD = np.empty(alphas2.size)
    normD = np.empty(alphas2.size)
    spreadD = np.empty(alphas2.size)
    for j, a in enumerate(alphas2):
        fv = sh**2 / (sh**2 + a)
        m_r = (Y2 * fv[None, :] / sh[None, :]) @ V.T * norm_m
        eI[j] = np.mean([rel_err(r, m_true) for r in m_r])
        A = K.T @ K + a * DtD
        G = np.linalg.solve(A, K.T @ K)                # data resolution matrix
        spreadD[j] = psf_spread(G, x, n // 2)
        errs = []
        norms = []
        for r in range(n_real2):
            m_d = np.linalg.solve(A, K.T @ Dhat[r]) * norm_m
            errs.append(rel_err(m_d, m_true))
            norms.append(np.linalg.norm(m_d) / norm_m)
        eD[j] = float(np.mean(errs))
        normD[j] = float(np.mean(norms))
    print("\n   alpha    L=I  ||err||/||m||   L=D  ||err||/||m||   "
          "L=D ||m||/||m_true||   L=D PSF spread (m)")
    for a in (1e-10, 1e-8, 1e-7, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 1e0):
        j = int(np.argmin(np.abs(alphas2 - a)))
        print(f"  {a:7.0e}   {eI[j]:19.5f}   {eD[j]:19.5f}   {normD[j]:20.4f}   "
              f"{spreadD[j]:16.1f}")
    jI, jD = int(np.argmin(eI)), int(np.argmin(eD))
    print(f"\n  best over the sweep:  L=I alpha = {alphas2[jI]:.2e} -> error "
          f"{eI[jI]:.5f}, PSF spread {spreadD[jI]:.0f} m;")
    print(f"                        L=D alpha = {alphas2[jD]:.2e} -> error "
          f"{eD[jD]:.5f}, PSF spread {spreadD[jD]:.0f} m")
    print("  The roughness penalty reaches a lower error here because the true")
    print("  model is smooth: the prior happens to match the model.  That is a")
    print("  model choice, and it is stated as one.")
    A_opt = K.T @ K + alphas2[jD] * DtD
    m_opt = np.linalg.solve(A_opt, K.T @ d_hat) * norm_m
    print(f"\n  mean of the L=D solution at its best alpha : "
          f"{np.mean(m_opt) / 1e9:.5f} (1e9 kg/m)")
    print(f"  mean of the true model                     : "
          f"{np.mean(m_true) / 1e9:.5f} (1e9 kg/m)")
    print("  D^T D cannot see the constant component, so the roughness penalty")
    print("  neither shrinks nor inflates the mean: the data fix it.  The L=D")
    print("  solution relaxes to its data-determined mean as alpha grows, while")
    print("  the L=I solution shrinks towards zero along EVERY direction, including")
    print("  the constant one.  That difference is what the penalty operator means.")


if __name__ == "__main__":
    main()
