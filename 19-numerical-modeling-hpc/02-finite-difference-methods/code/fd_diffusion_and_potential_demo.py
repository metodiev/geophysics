#!/usr/bin/env python3
"""Finite differences for diffusion and potential problems: measured order for a
Poisson problem with a closed-form solution, measured solver scaling, and the
diffusive timescale recovered from a time-dependent run.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python fd_diffusion_and_potential_demo.py

All models and data in this module are SYNTHETIC.  The exact solutions below are
chosen teaching functions, not measurements of any physical system.

Contents
--------
1. Two-dimensional Poisson problem with the exact solution sin(pi x) sin(pi y):
   observed order and the exact error constant pi^2/12.
2. Solver scaling: conjugate gradients against Jacobi, measured exponents.
3. Three-dimensional storage arithmetic and the measured iteration growth.
4. The diffusive timescale of the fundamental mode, measured against the exact
   exponential decay.
"""

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def poisson_2d(n):
    """Solve -laplacian(u) = 2 pi^2 sin(pi x) sin(pi y) on the unit square.

    Dirichlet zeros on the boundary; the exact solution is u = sin(pi x) sin(pi y).
    Returns (h, discrete solution, exact solution on the interior nodes).
    """
    h = 1.0 / (n + 1)
    x = np.arange(1, n + 1) * h
    X, Y = np.meshgrid(x, x, indexing="ij")
    exact = np.sin(np.pi * X) * np.sin(np.pi * Y)
    f = 2.0 * np.pi ** 2 * exact
    # five-point Laplacian, scaled by h^2 to keep the matrix well conditioned
    T = sp.diags([-1.0, 2.0, -1.0], [-1, 0, 1], shape=(n, n)).tocsr()
    I = sp.identity(n, format="csr")
    A = (sp.kron(I, T) + sp.kron(T, I)).tocsr()
    u = spla.spsolve(A, (h ** 2) * f.ravel()).reshape(n, n)
    return h, u, exact, A


def poisson_study():
    print("model: -lap(u) = 2 pi^2 sin(pi x) sin(pi y) on the unit square,")
    print("u = 0 on the boundary, exact solution u = sin(pi x) sin(pi y)")
    print("smooth-error prediction: e -> -(h^2 pi^2/12) u, so")
    print(f"  max|e|/h^2 -> pi^2/12 = {np.pi ** 2 / 12:.6f}")
    print(f"{'n':>5} {'h':>10} {'unknowns':>9} {'max|e|':>14} "
          f"{'max|e|/h^2':>12} {'observed order':>16}")
    prev = None
    for n in (16, 32, 64, 128):
        h, u, exact, _ = poisson_study_cache(n)
        err = np.max(np.abs(u - exact))
        order = "n/a" if prev is None else f"{np.log(prev / err) / np.log(2.0):.5f}"
        print(f"{n:>5} {h:>10.6f} {n * n:>9} {err:>14.6e} "
              f"{err / h ** 2:>12.6f} {order:>16}")
        prev = err
    print("the observed order is 2 and the measured constant approaches the")
    print("predicted pi^2/12, which is the second-difference truncation constant")


_CACHE: dict[int, tuple] = {}


def poisson_study_cache(n):
    if n not in _CACHE:
        _CACHE[n] = poisson_2d(n)
    return _CACHE[n]


def jacobi_iterations(A, b, tol=1e-10, maxiter=200000):
    """Plain Jacobi iteration, counted until the relative residual falls below tol."""
    d = A.diagonal()
    x = np.zeros_like(b)
    nb = np.linalg.norm(b)
    for k in range(1, maxiter + 1):
        x = x + (b - A @ x) / d
        if np.linalg.norm(b - A @ x) / nb < tol:
            return k
    return maxiter


def solver_scaling():
    print("cost of solving the same five-point Poisson system by two methods, to")
    print("a relative residual of 1e-10")
    print(f"{'n':>5} {'unknowns':>9} {'nnz':>9} {'CG iterations':>14} "
          f"{'Jacobi iterations':>18}")
    cg_counts, jac_counts = [], []
    print("the right-hand side is a localised Gaussian bump, which excites every")
    print("eigenmode: a single sine mode is an eigenvector of the discrete")
    print("Laplacian and CG would solve it in one iteration, measuring nothing")
    for n in (16, 32, 64):
        h, u, exact, A = poisson_study_cache(n)
        x1 = np.arange(1, n + 1) * h
        X1, Y1 = np.meshgrid(x1, x1, indexing="ij")
        grid = np.exp(-((X1 - 0.5) ** 2 + (Y1 - 0.5) ** 2) / 0.02)
        rhs = (h ** 2) * np.pi ** 2 * grid.ravel()
        count = {"cg": 0}

        def cg_cb(_xk):
            count["cg"] += 1

        spla.cg(A, rhs, rtol=1e-10, maxiter=20000, callback=cg_cb)
        jac = jacobi_iterations(A, rhs)
        cg_counts.append(count["cg"])
        jac_counts.append(jac)
        print(f"{n:>5} {n * n:>9} {A.nnz:>9} {count['cg']:>14} {jac:>18}")
    exp_cg = np.log(cg_counts[-1] / cg_counts[-2]) / np.log(2.0)
    exp_jac = np.log(jac_counts[-1] / jac_counts[-2]) / np.log(2.0)
    print(f"measured growth exponent per halving of h: CG {exp_cg:.3f}, "
          f"Jacobi {exp_jac:.3f}")
    print("CG is driven by sqrt(kappa) with kappa = O(h^-2), so it needs O(h^-1)")
    print("iterations; Jacobi is driven by kappa and needs O(h^-2).  The solver,")
    print("not the stencil, is what usually decides the run time.")


def three_d_arithmetic():
    print("three-dimensional Poisson problem on the unit cube, n cells per side")
    print(f"{'n':>5} {'unknowns':>12} {'float64 field (MiB)':>21} "
          f"{'explicit diffusion steps':>25}")
    for n in (50, 100, 200):
        dof = n ** 3
        mib = dof * 8 / 1024.0 ** 2
        h = 1.0 / (n + 1)
        steps = int(round(1.0 / (0.5 * h ** 2 / 6.0)))
        print(f"{n:>5} {dof:>12} {mib:>21.1f} {steps:>25}")
    print("with the five-point stencil in d dimensions the explicit diffusion")
    print("limit is dt <= h^2/(2 alpha d); the step count to a fixed physical time")
    print("therefore grows as n^2 while the number of unknowns grows as n^3, so a")
    print("three-dimensional refinement costs about n^5 times as much work.")
    print("a single float64 field of 200^3 cells occupies the memory column: the")
    print("numbers are exact arithmetic on the array size, not measurements.")


def diffusion_timescale():
    print("2-D heat equation u_t = alpha lap(u) with Dirichlet zeros and the")
    print("exact solution u = exp(-2 pi^2 alpha t) sin(pi x) sin(pi y)")
    print("implicit (backward Euler) march with alpha = 1, n = 32, dt = 1e-3")
    n = 32
    h, u, exact, A = poisson_study_cache(n)
    dt = 1e-3
    alpha = 1.0
    M = (sp.identity(n * n, format="csr") + (dt * alpha / h ** 2) * A).tocsc()
    v = exact.ravel().copy()
    amps, times = [], []
    for k in range(1, 201):
        v = spla.spsolve(M, v)
        if k % 20 == 0:
            t = k * dt
            amps.append(np.max(np.abs(v)))
            times.append(t)
    print(f"{'t':>8} {'measured amplitude':>20} {'exact amplitude':>18} "
          f"{'ratio':>10}")
    for t, a in zip(times, amps):
        exact_amp = np.exp(-2.0 * np.pi ** 2 * alpha * t)
        print(f"{t:>8.3f} {a:>20.6e} {exact_amp:>18.6e} {a / exact_amp:>10.5f}")
    print("the measured decay tracks the exact exponential, and the ratio drifts")
    print("upwards because backward Euler under-damps: its amplification")
    print("1/(1 + dt lambda) exceeds exp(-dt lambda) at every step, and the gap is")
    print("first order in dt.  The exact timescale of the mode is")
    print(f"  tau = 1/(2 pi^2 alpha) = {1.0 / (2.0 * np.pi ** 2):.6f} s")


def main():
    section("1. Poisson problem with a closed-form solution")
    poisson_study()

    section("2. Solver scaling: conjugate gradients against Jacobi")
    solver_scaling()

    section("3. Storage and step counts in three dimensions")
    three_d_arithmetic()

    section("4. The diffusive timescale of the fundamental mode")
    diffusion_timescale()


if __name__ == "__main__":
    main()
