#!/usr/bin/env python3
"""Physics-informed neural networks: fitting a boundary-value problem with a
physics residual instead of data, and what happens when the physics is wrong.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python physics_informed_demo.py

All models and data are SYNTHETIC.  The equation, its source term and the exact
solution below are chosen teaching ingredients, not measurements.  Training is
deliberately tiny (one hidden layer, a few hundred optimiser iterations) so the
script finishes in seconds.

Contents
--------
1. A boundary-value problem with a known exact solution.
2. A physics-informed fit: the network sees the equation, not the solution.
3. A data-only fit: what happens when there is no physics.
4. Physics plus data.
5. Mis-specified physics: the honest failure mode.
"""

import time
import numpy as np
from scipy.optimize import minimize

RNG = np.random.default_rng(20261014)

HIDDEN = 16
N_COLLOC = 200
BC_WEIGHT = 100.0
N_DATA_POINTS = 5
DATA_NOISE = 0.02


def section(title: str) -> None:
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def unpack(p):
    W1 = p[:HIDDEN]
    b1 = p[HIDDEN:2 * HIDDEN]
    W2 = p[2 * HIDDEN:3 * HIDDEN]
    b2 = p[3 * HIDDEN]
    return W1, b1, W2, b2


def u_of_z(p, z):
    """Network u(z) = W2 . tanh(W1 z + b1) + b2, one hidden layer."""
    W1, b1, W2, b2 = unpack(p)
    h = np.tanh(z[:, None] * W1[None, :] + b1[None, :])
    return h @ W2 + b2


def u_double_prime(p, z):
    """Analytic second derivative of the network w.r.t. z."""
    W1, b1, W2, b2 = unpack(p)
    h = np.tanh(z[:, None] * W1[None, :] + b1[None, :])
    return ((-2.0 * h * (1.0 - h ** 2)) * (W1 ** 2)[None, :]) @ W2


def init_params(seed=0):
    rng = np.random.default_rng(seed)
    return np.concatenate([rng.standard_normal(HIDDEN) * 1.0,      # W1
                           rng.standard_normal(HIDDEN) * 0.1,      # b1
                           rng.standard_normal(HIDDEN) * 0.5,      # W2
                           np.zeros(1)])                           # b2


def loss_physics(p, z, f):
    res = u_double_prime(p, z) + f(z)
    bc = u_of_z(p, np.array([0.0, 1.0]))
    return np.mean(res ** 2) + BC_WEIGHT * np.mean(bc ** 2)


def loss_data_only(p, z_d, u_d):
    return np.mean((u_of_z(p, z_d) - u_d) ** 2)


def loss_both(p, z, f, z_d, u_d, w=10.0):
    return loss_physics(p, z, f) + w * loss_data_only(p, z_d, u_d)


def optimise(loss, p0):
    res = minimize(loss, p0, method="L-BFGS-B",
                   options={"maxiter": 600, "ftol": 1e-14})
    return res.x, res


def main():
    z = np.linspace(0.0, 1.0, N_COLLOC)
    f_true = lambda zz: np.pi ** 2 * np.sin(np.pi * zz)
    u_exact = lambda zz: np.sin(np.pi * zz)

    section("1. A boundary-value problem with a known exact solution")
    print("  -u''(z) = f(z) on (0, 1),  u(0) = u(1) = 0")
    print("  f(z) = pi^2 sin(pi z)   ->   u(z) = sin(pi z)  (SYNTHETIC, chosen)")
    print(f"  collocation points: {N_COLLOC} on (0,1), network {HIDDEN} tanh "
          f"units, {4 * HIDDEN + 1} parameters")
    print("  the network NEVER sees u; it only sees the residual of the equation.")

    section("2. A physics-informed fit: the equation, not the solution")
    p0 = init_params()
    t0 = time.time()
    p_phys, res = optimise(lambda p: loss_physics(p, z, f_true), p0)
    t_phys = time.time() - t0
    err = np.sqrt(np.mean((u_of_z(p_phys, z) - u_exact(z)) ** 2))
    res_final = np.sqrt(np.mean((u_double_prime(p_phys, z) + f_true(z)) ** 2))
    bc = np.abs(u_of_z(p_phys, np.array([0.0, 1.0]))).max()
    print(f"  optimiser: {res.nit} L-BFGS-B iterations in {t_phys:.2f} s")
    print(f"  final physics residual (rms)  = {res_final:.3e}")
    print(f"  final boundary error (max)    = {bc:.3e}")
    print(f"  error against the exact u     = {err:.2e}  (L2 rms)")
    print("  with no interior measurements at all, the fit is accurate to better")
    print("  than one part in a thousand: the equation and the boundary conditions")
    print("  supply essentially all of the information.  The network is a")
    print("  representation, not a source of information.")

    section("3. A data-only fit: five noisy interior points, no physics")
    z_d = np.array([0.15, 0.3, 0.5, 0.7, 0.85])
    u_d = u_exact(z_d) + DATA_NOISE * RNG.standard_normal(z_d.size)
    p_data, res_d = optimise(lambda p: loss_data_only(p, z_d, u_d), init_params(1))
    err_d = np.sqrt(np.mean((u_of_z(p_data, z) - u_exact(z)) ** 2))
    res_d_phys = np.sqrt(np.mean((u_double_prime(p_data, z) + f_true(z)) ** 2))
    bc_d = np.abs(u_of_z(p_data, np.array([0.0, 1.0]))).max()
    print(f"  data fit at the 5 points (rms) = "
          f"{np.sqrt(loss_data_only(p_data, z_d, u_d)):.2e}")
    print(f"  error against the exact u      = {err_d:.4f}  (L2 rms)")
    print(f"  physics residual of that fit   = {res_d_phys:.3f}")
    print(f"  boundary error of that fit     = {bc_d:.3f}")
    print("  the data-only network is accurate AT the five points and meaningless")
    print("  between them, and it does not satisfy the equation or the boundary")
    print("  conditions.  Data alone is not a physical solution; it is an")
    print("  interpolation with "
          f"{4 * HIDDEN + 1} parameters and {N_DATA_POINTS} constraints.")

    section("4. Physics plus data")
    p_both, res_b = optimise(
        lambda p: loss_both(p, z, f_true, z_d, u_d), init_params(2))
    err_b = np.sqrt(np.mean((u_of_z(p_both, z) - u_exact(z)) ** 2))
    print(f"  error against the exact u = {err_b:.2e}  (physics-only "
          f"{err:.2e}, data-only {err_d:.4f})")
    print("  the noisy points act as a small correction to a solution that the")
    print("  physics already determines.  That is the intended use: data reduce")
    print("  the residual freedom, they do not replace the equation.")

    section("5. Mis-specified physics: the honest failure mode")
    f_wrong = lambda zz: 1.20 * np.pi ** 2 * np.sin(np.pi * zz)
    p_wrong, _ = optimise(lambda p: loss_physics(p, z, f_wrong), init_params(3))
    u_wrong = u_of_z(p_wrong, z)
    err_wrong = np.sqrt(np.mean((u_wrong - u_exact(z)) ** 2))
    print("  the equation is solved with a source term 20% too large; the network")
    print("  is never told, and its physics residual is as small as before:")
    print(f"    physics residual (rms) = "
          f"{np.sqrt(np.mean((u_double_prime(p_wrong, z) + f_wrong(z)) ** 2)):.3e}")
    print(f"    error against the TRUE u = {err_wrong:.4f}")
    amp = np.max(np.abs(u_wrong)) / np.max(np.abs(u_exact(z)))
    print(f"    amplitude recovered / true amplitude = {amp:.3f}")
    print("  The answer is smooth, satisfies the boundary conditions and solves a")
    print("  well-posed problem -- the WRONG one.  A physics-informed network")
    print("  cannot detect a mis-specified equation: every internal diagnostic")
    print("  looks healthy.  The only defence is to test the physics against data")
    print("  it did not generate, which is exactly the discipline an empirical")
    print("  inversion already requires.")


if __name__ == "__main__":
    main()
