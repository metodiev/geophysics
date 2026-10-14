"""Check the linear-algebra formula sheet: SVD, conditioning, least squares, damping.

Print-only, seeded, no plots, no file I/O. Numbers quoted in
26-03-02-formulas-linear-algebra-numerics.md come from this output.

Run with:  .venv/bin/python 26-reference-library/03-formula-handbook/code/formulas_linear_algebra_demo.py
"""

from __future__ import annotations

import numpy as np

SEED = 20261014


def banner(n: int, title: str) -> None:
    print(f"\n[{n}] {title}")


def main() -> None:
    rng = np.random.default_rng(SEED)
    print("Linear algebra and numerics formula sheet -- numerical checks")
    print(f"numpy {np.__version__}, seeded rng = default_rng({SEED})")
    print("PROVENANCE: SYNTHETIC -- matrices are drawn from the seeded rng, not measured.")

    # 1. SVD of a deliberately ill-conditioned 4x3 system.
    banner(1, "SVD, singular values and condition number")
    a_mat = np.array(
        [
            [1.0, 2.0, 3.0],
            [4.0, 5.0, 6.0],
            [7.0, 8.0, 10.0],
            [1.0, 2.0, 3.0001],
        ]
    )
    u_mat, s_vals, vt_mat = np.linalg.svd(a_mat, full_matrices=False)
    print(f"  matrix shape          = {a_mat.shape} (rows = data, cols = parameters)")
    print(f"  singular values       = {np.array2string(s_vals, precision=6)}")
    print(f"  s_max/s_min           = {s_vals[0] / s_vals[-1]:.6e}")
    print(f"  numerical rank (tol)  = {np.sum(s_vals > s_vals[0] * 1e-12)}")
    print(f"  ||U^T U - I||_inf     = {np.max(np.abs(u_mat.T @ u_mat - np.eye(3))):.3e}")

    # 2. Normal equations versus the pseudoinverse for a small least-squares fit.
    banner(2, "Normal equations, QR and pseudoinverse for a linear fit")
    n_data = 12
    t_obs = np.linspace(0.0, 1.0, n_data)
    design = np.column_stack([np.ones_like(t_obs), t_obs])
    true_params = np.array([2.0, -1.5])
    d_obs = design @ true_params + rng.normal(0.0, 0.05, n_data)
    normal = np.linalg.solve(design.T @ design, design.T @ d_obs)
    q_mat, r_mat = np.linalg.qr(design)
    qr_sol = np.linalg.solve(r_mat, q_mat.T @ d_obs)
    pinv_sol = np.linalg.pinv(design) @ d_obs
    print(f"  true parameters       = {np.array2string(true_params, precision=6)}")
    print(f"  normal-equation solve = {np.array2string(normal, precision=6)}")
    print(f"  QR solve              = {np.array2string(qr_sol, precision=6)}")
    print(f"  pseudoinverse solve   = {np.array2string(pinv_sol, precision=6)}")
    print(f"  condition number(design) = {np.linalg.cond(design):.6e}")
    resid = d_obs - design @ qr_sol
    print(f"  residual RMS          = {np.sqrt(np.mean(resid**2)):.6f} (data units)")

    # 3. Tikhonov damping: trade-off between misfit and model norm.
    banner(3, "Tikhonov damping: misfit versus model norm")
    for alpha in (0.0, 0.1, 1.0):
        damped = np.linalg.solve(
            design.T @ design + alpha * np.eye(2), design.T @ d_obs
        )
        misfit = float(np.sqrt(np.mean((d_obs - design @ damped) ** 2)))
        print(
            f"  alpha = {alpha:4.1f}: cost = {np.dot(damped, damped):.6f}, "
            f"residual RMS = {misfit:.6f}"
        )

    # 4. Symmetric eigenproblem invariants.
    banner(4, "Symmetric eigenproblem invariants")
    sym = np.array([[4.0, 1.0, 0.0], [1.0, 3.0, 1.0], [0.0, 1.0, 2.0]])
    eig_vals = np.linalg.eigvalsh(sym)
    print(f"  eigenvalues           = {np.array2string(eig_vals, precision=6)}")
    print(f"  sum(eigenvalues)      = {eig_vals.sum():.6f}  trace = {np.trace(sym):.6f}")
    print(f"  prod(eigenvalues)     = {eig_vals.prod():.6f}  det   = {np.linalg.det(sym):.6f}")
    print(f"  ||A - A^T||_inf       = {np.max(np.abs(sym - sym.T)):.3e}")

    print("\nAll four checks completed; exit status 0.")


if __name__ == "__main__":
    main()
