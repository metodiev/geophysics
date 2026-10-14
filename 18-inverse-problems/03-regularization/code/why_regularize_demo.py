#!/usr/bin/env python3
"""Why regularisation is justified: singular-value decay of a discretised
first-kind kernel, the discrete Picard condition, and the measured amplification
of data noise into model error.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python why_regularize_demo.py

All models and data are SYNTHETIC.  The kernel is the exact 2-D line-mass
gravity kernel of a textbook forward model, but the density distribution, the
station spacing, the target depth and the noise are chosen teaching values, not
measurements.  No measured data, no published spectra and no citations are used.
The only physical constant is the standard gravitational constant
G = 6.67430e-11 m^3 kg^-1 s^-2.

Contents
--------
1. The synthetic first-kind problem and its data.
2. Singular values, condition number, fitted degree of ill-posedness.
3. Exact-data least squares: the discrete problem looks harmless.
4. Noisy-data least squares: measured amplification of 0.5% data noise.
5. The discrete Picard condition: which coefficients still carry signal.
6. Truncated SVD as the crudest regulariser: measured error versus rank.
7. Two controls: the same noise on a better-conditioned geometry and on a
   second-kind (well-posed) operator.
"""

import numpy as np

RNG = np.random.default_rng(20261014)
G_CONST = 6.67430e-11      # m^3 kg^-1 s^-2, standard gravitational constant
MGAL = 1.0e5               # m/s^2 -> mGal


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def line_mass_kernel(x_obs_m, x_src_m, depth_m):
    """Vertical attraction of a 2-D line mass, per unit line density.

    g_z(x) = 2 G a z / ((x - s)^2 + z^2)                        [m/s^2]

    with ``a`` the line density in kg/m and all lengths in metres.  The returned
    matrix has units mGal per (kg/m): rows are observation points, columns are
    source positions.
    """
    dx = x_obs_m[:, None] - x_src_m[None, :]
    return 2.0 * G_CONST * depth_m / (dx**2 + depth_m**2) * MGAL


def rel_err(m, m_true):
    """Euclidean relative model error, dimensionless."""
    return np.linalg.norm(m - m_true) / np.linalg.norm(m_true)


def build(depth_m, n=64, half_length_m=4000.0):
    """Return (K, x, m_true, d_exact) for the synthetic line-mass problem."""
    x = np.linspace(-half_length_m, half_length_m, n)
    K = line_mass_kernel(x, x, depth_m)
    m_true = 1.0e9 * np.exp(-(x / 1500.0) ** 2)          # kg/m
    return K, x, m_true, K @ m_true


def main():
    n = 64
    depth = 600.0

    section("1. The synthetic first-kind problem")
    K, x, m_true, d_exact = build(depth, n)
    noise = 0.005 * np.abs(d_exact).max()                # 0.5% of peak anomaly
    print("kernel: 2-D line masses in a sheet below a profile of gravity stations")
    print(f"  observations : {n} stations, -4.0 to 4.0 km, spacing "
          f"{np.diff(x)[0]:.1f} m")
    print(f"  model cells  : {n} cells of {np.diff(x)[0]:.1f} m at 0.6 km depth")
    print(f"  true model   : peak {m_true.max():.3e} kg/m, Gaussian half-width "
          f"1.50 km (SYNTHETIC)")
    print(f"  exact data   : peak {d_exact.max():.3f} mGal, rms "
          f"{np.std(d_exact):.3f} mGal")
    print(f"  noise added  : rms {noise:.4f} mGal = "
          f"{noise / np.abs(d_exact).max() * 100:.2f}% of the peak anomaly")
    print("  The map m -> d is d_i = sum_j K_ij m_j: a first-kind Fredholm")
    print("  equation discretised on the grid, i.e. a convolution with a")
    print("  smoothing kernel -- a low-pass filter of the model.")

    # ------------------------------------------------------- singular values
    U, s, Vt = np.linalg.svd(K)
    V = Vt.T
    section("2. Singular values of the kernel")
    print("    index        sigma_i      sigma_i/sigma_1")
    for i in (0, 3, 7, 15, 31, 47, 63):
        print(f"    {i + 1:5d}  {s[i]:12.5e}   {s[i] / s[0]:12.5e}")
    print(f"  condition number kappa_2(K) = sigma_1/sigma_64 = {s[0] / s[-1]:.3e}")
    kfit = 48
    q = -np.polyfit(np.log(np.arange(1, kfit + 1)), np.log(s[:kfit]), 1)[0]
    print(f"  fitted decay sigma_i ~ i^(-q) on i = 1..{kfit}:  q = {q:.2f}")
    print("  A decaying spectrum is what makes the discrete problem ill-posed: the")
    print("  singular values are not bounded away from zero, so 1/sigma_i is not")
    print("  bounded either.  q is a property of the PHYSICS (target depth and")
    print("  station spacing), not of the algorithm.")

    # ------------------------------------------------ exact-data least squares
    m_ls_exact = V @ ((U.T @ d_exact) / s)
    section("3. Least squares solution from exact data")
    print(f"  relative model error ||m - m_true||/||m_true|| = "
          f"{rel_err(m_ls_exact, m_true):.3e}")
    print(f"  data misfit          ||Km - d||/||d||          = "
          f"{np.linalg.norm(K @ m_ls_exact - d_exact) / np.linalg.norm(d_exact):.3e}")
    print("  With noiseless data the discrete problem inverts to about machine")
    print("  precision.  The ill-posedness is therefore invisible here: it is a")
    print("  statement about what NOISE does, not about invertibility.")

    # ------------------------------------------------ noisy-data least squares
    n_real = 200
    errs = np.empty(n_real)
    for r in range(n_real):
        d = d_exact + noise * RNG.standard_normal(n)
        m = V @ ((U.T @ d) / s)
        errs[r] = rel_err(m, m_true)
    d_noisy = d_exact + noise * RNG.standard_normal(n)
    m_ls = V @ ((U.T @ d_noisy) / s)
    resid = np.linalg.norm(K @ m_ls - d_noisy) / np.linalg.norm(d_noisy)
    section("4. Least squares solution from noisy data")
    print(f"  data misfit achieved : {resid * 100:.4f}%  (the noise is fitted)")
    print(f"  relative model error : {rel_err(m_ls, m_true):.3e}  "
          f"(single realisation)")
    print(f"  mean over {n_real} noise realisations : {errs.mean():.3e}")
    print(f"    percentiles 5% / 50% / 95% : {np.percentile(errs, 5):.3e} / "
          f"{np.percentile(errs, 50):.3e} / {np.percentile(errs, 95):.3e}")
    print(f"  noise amplification factor = {errs.mean() / (noise / np.linalg.norm(d_exact)):.3e}")
    norm_d = float(np.linalg.norm(d_exact))
    norm_e = noise * np.sqrt(n)
    print(f"  worst-case bound, one datum perturbed by sigma_e:")
    print(f"    kappa_2(K) * sigma_e / ||d|| = "
          f"{s[0] / s[-1] * noise / norm_d:.3e}")
    print(f"  worst-case bound, the whole vector perturbed, ||e|| = sigma_e*sqrt(n):")
    print(f"    kappa_2(K) * ||e|| / ||d||   = "
          f"{s[0] / s[-1] * norm_e / norm_d:.3e}")
    print("  Both are worst-case statements; the measured mean error below is the")
    print("  ordinary-case size and is quoted for comparison.")
    print("  The unregularised solution fits the data to four decimal places and")
    print("  is wrong by a factor of thousands.  It is fitting the noise: every")
    print("  component with sigma_i below the noise floor gets an arbitrary,")
    print("  enormous coefficient 1/sigma_i times noise.")

    # ---------------------------------------------------- Picard condition
    section("5. The discrete Picard condition")
    coeff_exact = np.abs(U.T @ d_exact)
    coeff_noisy = np.abs(U.T @ d_noisy)
    print("     i      sigma_i      |u_i^T d_exact|   |u_i^T d_noisy|")
    for i in list(range(0, 12, 2)) + [15, 23, 31, 47, 63]:
        print(f"  {i + 1:5d}  {s[i]:11.4e}   {coeff_exact[i]:14.5e}   "
              f"{coeff_noisy[i]:14.5e}")
    print(f"  single-coefficient noise level sqrt(E[(u_i^T e)^2]) = {noise:.4f} mGal")
    above = coeff_exact > 10.0 * noise
    print(f"  components with |u_i^T d_exact| > 10 x noise level : {int(above.sum())} of {n}")
    print(f"    (their indices run up to i = {int(np.max(np.where(above)[0])) + 1})")
    odd = [i + 1 for i in range(n) if coeff_exact[i] < 1e-6 * coeff_exact[0]]
    print(f"  coefficients below 1e-6 of the largest : {len(odd)} "
          f"(starting at i = {odd[0]})")
    print("  Those vanishing coefficients are not noise: the true model is")
    print("  SYMMETRIC about x = 0, so its projection onto every antisymmetric")
    print("  singular vector is zero.  Data can only see what the model contains.")
    print("  Where the exact coefficients fall with sigma_i, the data")
    print("  genuinely contain those components.  Beyond that the exact coefficients")
    print("  stall at ~1e-13 mGal -- numerical zero, because the smooth true model")
    print("  has essentially no energy in those model-space directions -- while the")
    print("  noisy coefficients stall at the noise floor.  That is the discrete")
    print("  PICARD condition: 1/sigma_i times a noise-floor coefficient is a huge,")
    print("  meaningless number, and the trustworthy components come first.")

    # --------------------------------------------- truncated SVD (rank filter)
    section("6. Truncated SVD: discarding small singular values is regularisation")
    coef = U.T @ d_noisy
    ks = [1, 2, 4, 6, 8, 10, 12, 16, 20, 28, 40, 64]
    print("   rank k    relative model error    data misfit")
    for k in ks:
        m_k = V[:, :k] @ (coef[:k] / s[:k])
        e = rel_err(m_k, m_true)
        print(f"   {k:5d}     {e:18.5e}     "
              f"{np.linalg.norm(K @ m_k - d_noisy) / np.linalg.norm(d_noisy) * 100:8.3f}%")
    err_fine = np.array([rel_err(V[:, :k] @ (coef[:k] / s[:k]), m_true)
                         for k in range(1, n + 1)])
    k_opt = int(np.argmin(err_fine)) + 1
    print(f"  measured optimum: rank {k_opt}, relative model error "
          f"{err_fine.min():.5e}")
    print(f"  improvement over the unregularised solution: "
          f"{rel_err(m_ls, m_true) / err_fine.min():.3e} x")
    print(f"  the rank-{k_opt} solution lives in a {k_opt}-dimensional subspace, so it")
    print("  cannot equal the true model even in the absence of noise: it is a")
    print("  BIASED estimator.  The bias is the price paid to kill the variance,")
    print("  and the rank is a model choice made by the analyst.")

    # ------------------------------------------------------------- controls
    section("7a. Control: a shallower target is better conditioned")
    print("  depth (m)   kappa_2(K)      q     noisy LS rel. error   best rank / error")
    for z in (300.0, 600.0, 1200.0):
        K2, x2, mt2, d2 = build(z, n)
        U2, s2, V2t = np.linalg.svd(K2)
        q2 = -np.polyfit(np.log(np.arange(1, 49)), np.log(s2[:48]), 1)[0]
        nz2 = 0.005 * np.abs(d2).max()
        dn2 = d2 + nz2 * RNG.standard_normal(n)
        e2 = rel_err(V2t.T @ ((U2.T @ dn2) / s2), mt2)
        co2 = U2.T @ dn2
        ef2 = np.array([rel_err(V2t.T[:, :k] @ (co2[:k] / s2[:k]), mt2)
                        for k in range(1, n + 1)])
        print(f"  {z:9.0f}   {s2[0] / s2[-1]:10.3e}   {q2:5.2f}   {e2:17.3e}   "
              f"{int(np.argmin(ef2)) + 1:4d} / {ef2.min():.2e}")
    print("  Same stations, same cells, same noise, same true model: only the")
    print("  target depth changed, and the difficulty changed with it.  Resolution")
    print("  in a potential-field problem is set by depth, not by the solver.")

    section("7b. Control: a second-kind operator with the same noise")
    c = np.abs(K).sum(axis=1).max()          # >= ||K||_2, so c*I + K is stable
    A = c * np.eye(n) + K
    dA_exact = A @ m_true
    nzA = 0.005 * np.abs(dA_exact).max()
    dA_noisy = dA_exact + nzA * RNG.standard_normal(n)
    mA = np.linalg.solve(A, dA_noisy)
    sA = np.linalg.svd(A, compute_uv=False)
    print(f"  A = c*I + K with c = max row sum |K| = {c:.4e} (same units as K)")
    print(f"  sigma(A) in [{sA.min():.4e}, {sA.max():.4e}], "
          f"kappa_2(A) = {sA[0] / sA[-1]:.3f}")
    print(f"  data generated by A itself, peak anomaly {dA_exact.max():.3f} mGal, "
          f"noise {nzA:.4f} mGal (0.50%)")
    print(f"  second-kind noisy relative error = {rel_err(mA, m_true):.5f}")
    print(f"  first-kind noisy relative error  = {rel_err(m_ls, m_true):.3e}")
    print(f"  ratio = {rel_err(m_ls, m_true) / rel_err(mA, m_true):.3e}")
    print("  The same relative noise in the data produces an error of order 1e-2")
    print("  for the second-kind operator and of order 1e3 for the first-kind one.")
    print("  What separates them is the singular-value spectrum, not the noise.")


if __name__ == "__main__":
    main()
