"""Check the inverse-theory and statistics formula sheet.

Print-only, seeded, no plots, no file I/O. Numbers quoted in
26-03-06-formulas-inverse-statistics.md come from this output.

Run with:  .venv/bin/python 26-reference-library/03-formula-handbook/code/formulas_inverse_statistics_demo.py
"""

from __future__ import annotations

import numpy as np
from scipy import stats

SEED = 20261014


def banner(n: int, title: str) -> None:
    print(f"\n[{n}] {title}")


def scaled_sigmas(cov_m: np.ndarray, chi2: float, dof: int) -> str:
    """Standard errors rescaled by the reduced chi-square as a variance factor."""
    scale = np.sqrt(chi2 / dof)
    return np.array2string(np.sqrt(np.diag(cov_m)) * scale, precision=4)


def main() -> None:
    rng = np.random.default_rng(SEED)
    print("Inverse theory and statistics formula sheet -- numerical checks")
    print(f"numpy {np.__version__}, seeded rng = default_rng({SEED})")
    print("PROVENANCE: SYNTHETIC -- data are drawn from the seeded rng.")

    banner(1, "Weighted mean, standard error and reduced chi-square")
    values = np.array([10.2, 9.7, 10.4, 9.9, 10.1])
    sigmas = np.array([0.30, 0.45, 0.20, 0.50, 0.35])
    weights = 1.0 / sigmas**2
    w_mean = float(np.sum(weights * values) / np.sum(weights))
    w_sigma = float(1.0 / np.sqrt(np.sum(weights)))
    unweighted = float(np.mean(values))
    print(f"  values  = {np.array2string(values, precision=2)} (data units)")
    print(f"  sigmas  = {np.array2string(sigmas, precision=2)} (data units)")
    print(f"  unweighted mean = {unweighted:.6f}, sample std = {np.std(values, ddof=1):.6f}")
    print(f"  weighted mean   = {w_mean:.6f} +/- {w_sigma:.6f} (1 sigma)")
    chi2 = float(np.sum(((values - w_mean) / sigmas) ** 2))
    dof = len(values) - 1
    print(f"  chi-square = {chi2:.6f} with {dof} dof, reduced chi-square = {chi2 / dof:.6f}")
    print(f"  coverage factor k for 95 % (normal) = {stats.norm.ppf(0.975):.6f}")
    print(f"  t quantile (95 %, {dof} dof) = {stats.t.ppf(0.975, dof):.6f}")

    banner(2, "Linear least squares with first-order uncertainty propagation")
    n_data = 15
    x_obs = np.linspace(0.0, 1.0, n_data)
    design = np.column_stack([np.ones_like(x_obs), x_obs])
    true_params = np.array([1.5, 0.8])
    data_sigma = 0.10
    d_obs = design @ true_params + rng.normal(0.0, data_sigma, n_data)
    cov_d = np.eye(n_data) * data_sigma**2
    cov_m = np.linalg.inv(design.T @ np.linalg.inv(cov_d) @ design)
    params = cov_m @ design.T @ np.linalg.inv(cov_d) @ d_obs
    print(f"  true parameters         = {np.array2string(true_params, precision=4)}")
    print(f"  estimated parameters    = {np.array2string(params, precision=4)}")
    print(f"  parameter sigma         = {np.array2string(np.sqrt(np.diag(cov_m)), precision=4)}")
    corr = cov_m[0, 1] / np.sqrt(cov_m[0, 0] * cov_m[1, 1])
    print(f"  parameter correlation   = {corr:+.6f}")
    resid = d_obs - design @ params
    dof_ls = n_data - 2
    chi2_ls = float(np.sum((resid / data_sigma) ** 2))
    print(f"  residual RMS = {np.sqrt(np.mean(resid**2)):.6f}, chi2/dof = {chi2_ls / dof_ls:.6f}")
    print(f"  standard error from chi2 = {scaled_sigmas(cov_m, chi2_ls, dof_ls)}")

    banner(3, "Tikhonov damping: solution norm against data misfit")
    a_matrix = np.array([[1.0, 0.0], [0.0, 0.01], [1.0, 1.0]])
    d_vec = np.array([1.0, 0.0, 2.0])
    for alpha in (0.0, 1e-4, 1e-2, 1.0):
        model = np.linalg.solve(a_matrix.T @ a_matrix + alpha * np.eye(2), a_matrix.T @ d_vec)
        misfit = float(np.linalg.norm(d_vec - a_matrix @ model))
        print(
            f"  alpha = {alpha:7.0e}: |m| = {np.linalg.norm(model):8.5f}, "
            f"|d - Am| = {misfit:8.5f}, m = {np.array2string(model, precision=5)}"
        )

    banner(4, "Monte Carlo check of the 1/sqrt(N) law and of a Gaussian interval")
    population_sigma = 2.0
    for n_samples in (100, 400, 1600):
        draws = rng.normal(0.0, population_sigma, n_samples)
        print(
            f"  N = {n_samples:5d}: sample mean = {draws.mean():+.5f} "
            f"(se = {draws.std(ddof=1) / np.sqrt(n_samples):.5f}), "
            f"sample std = {draws.std(ddof=1):.5f} (true {population_sigma:.1f})"
        )
    inside = np.mean(np.abs(rng.normal(0.0, 1.0, 20000)) <= 1.96)
    print(f"  fraction of standard normals within +/-1.96 sigma = {inside:.4f} (theory 0.95)")

    banner(5, "Resolution and averaging kernel of a damped inverse problem")
    gram = a_matrix.T @ a_matrix
    resolution = gram @ np.linalg.inv(gram + 0.1 * np.eye(2))
    print(f"  G^T G = {np.array2string(gram, precision=4)}")
    print(f"  resolution matrix (alpha = 0.1) = {np.array2string(resolution, precision=4)}")
    print(f"  trace of resolution matrix = {np.trace(resolution):.6f} (2 = perfect resolution)")

    print("\nAll five checks completed; exit status 0.")



if __name__ == "__main__":
    main()
