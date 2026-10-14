"""Linear algebra with numpy.linalg.

Run:  .venv/bin/python linalg_demo.py
Requires: numpy only.

Companion to lesson 03-02-05. The observations are SYNTHETIC: the gravity
profile is a parabola (the far-field shape of a 2-D body's anomaly) evaluated on
a synthetic station line, with seeded Gaussian noise added.

The script:

1. Solves a small exact system and checks the residual.
2. Fits a parabola to a synthetic gravity profile three ways: normal equations
   with solve, normal equations with inv, and lstsq -- and compares accuracy
   and conditioning.
3. Times solve against inv on a larger system and reports the residuals.
4. Computes eigenvalues of a matrix whose eigenvalues are known analytically.
5. Quantifies the conditioning of the Hilbert matrix, the standard warning
   example that a matrix can be non-singular yet unusable.
6. Factors a symmetric positive-definite matrix with Cholesky.
"""

import time

import numpy as np


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


SEED = 20261014


def part1_small_system():
    section("1. A small exact system")

    A = np.array([[3.0, 2.0, -1.0],
                  [2.0, -2.0, 4.0],
                  [-1.0, 0.5, -1.0]])
    b = np.array([1.0, -2.0, 0.0])
    x = np.linalg.solve(A, b)
    print("A =\n", A)
    print("b =", b)
    print("x = np.linalg.solve(A, b) =", x)
    print("residual ||Ax - b||_inf    =", np.abs(A @ x - b).max())
    print("det(A)                    =", np.linalg.det(A))
    print("cond(A)                   =", np.linalg.cond(A))
    print("np.allclose(A @ x, b)     =", np.allclose(A @ x, b))
    print("\n  solve performs an LU factorisation and back-substitution. It")
    print("  never forms an inverse, and it is the only one of the three")
    print("  standard routes that has a backward-stable error bound.")


def part2_least_squares():
    section("2. Least squares: fitting a parabola to a synthetic gravity profile")

    rng = np.random.default_rng(SEED)
    m = 40
    x = np.linspace(-4000.0, 4000.0, m)          # m, station offset
    true = np.array([12.0, -0.0004, 2.0e-8])     # mGal, mGal/m, mGal/m^2
    clean = true[0] + true[1] * x + true[2] * x ** 2
    sigma = 0.35
    d = clean + rng.normal(0.0, sigma, size=m)

    A = np.column_stack([np.ones_like(x), x, x ** 2])
    print(f"A.shape = {A.shape}, d.shape = {d.shape}   (m = {m}, n = 3)")
    print(f"condition number of A                 = {np.linalg.cond(A):.4e}")

    # The same parabola fitted after centring and scaling x to [-1, 1].
    xc = (x - x.mean()) / np.abs(x - x.mean()).max()
    As = np.column_stack([np.ones_like(xc), xc, xc ** 2])
    print(f"condition number of A (centred/scaled)= {np.linalg.cond(As):.4e}")
    ms = np.linalg.solve(As.T @ As, As.T @ d)
    print(f"  scaled coefficients = {np.round(ms, 6)}")
    print("  (a0 + a1*xc + a2*xc^2 with xc in [-1, 1]; a0 is the value at the")
    print("   profile centre and no longer directly comparable to m0)")

    normal = A.T @ A
    rhs = A.T @ d
    print(f"\ncondition number of A^T A             = {np.linalg.cond(normal):.4e}")
    print(f"                     (squared, as expected: {np.linalg.cond(A) ** 2:.4e})")

    m_solve = np.linalg.solve(normal, rhs)
    m_inv = np.linalg.inv(normal) @ rhs
    m_lstsq, residuals, rank, sv = np.linalg.lstsq(A, d, rcond=None)

    print(f"\n{'route':<34}{'m0':>12}{'m1':>16}{'m2':>16}")
    labels = ("normal equations + solve", "normal equations + inv",
              "lstsq (QR / SVD)", "true (synthetic)")
    for label, vec in zip(labels, (m_solve, m_inv, m_lstsq, true)):
        print(f"{label:<34}{vec[0]:>12.6f}{vec[1]:>16.3e}{vec[2]:>16.3e}")

    for label, vec in zip(labels[:3], (m_solve, m_inv, m_lstsq)):
        r = np.linalg.norm(A @ vec - d)
        print(f"  ||A x - d||_2 for {label:<28} = {r:.10f}")
    print(f"\nbest possible residual (sigma*sqrt(m-n)) = "
          f"{sigma * np.sqrt(m - 3):.6f}   nominal, synthetic sigma = {sigma}")
    print("  All three routes agree to better than 1e-10 here. They can,")
    print(f"  because cond(A^T A) = {np.linalg.cond(normal):.3e} is still far")
    print("  below 1/eps (about 1e16 in float64), so roughly 14 - 2*7 = 2")
    print("  digits are left after the squaring -- enough to agree, not enough")
    print("  to trust blindly. Centring and scaling x, as above, removes the")
    print("  problem at the source: the condition number falls from")
    print(f"  {np.linalg.cond(A):.2e} to {np.linalg.cond(As):.2e}. lstsq is the")
    print("  safe default route; the normal equations are acceptable only")
    print("  after the design matrix has been rescaled.")


def part3_solve_vs_inv():
    section("3. solve versus inv on a larger system")

    rng = np.random.default_rng(SEED + 1)
    k, n = 2500, 1000
    A = rng.normal(size=(k, n))
    x_true = rng.normal(size=n)
    b = A @ x_true + 1e-6 * rng.normal(size=k)
    normal = A.T @ A
    rhs = A.T @ b

    t0 = time.perf_counter()
    for _ in range(3):
        x_solve = np.linalg.solve(normal, rhs)
    t_solve = (time.perf_counter() - t0) / 3

    t0 = time.perf_counter()
    for _ in range(3):
        x_inv = np.linalg.inv(normal) @ rhs
    t_inv = (time.perf_counter() - t0) / 3

    print(f"A is {k} x {n}; normal equations are {n} x {n}")
    print(f"np.linalg.solve : {t_solve * 1e3:8.3f} ms   "
          f"||x - x_true||_2 = {np.linalg.norm(x_solve - x_true):.6e}")
    print(f"np.linalg.inv   : {t_inv * 1e3:8.3f} ms   "
          f"||x - x_true||_2 = {np.linalg.norm(x_inv - x_true):.6e}")
    print(f"ratio inv/solve = {t_inv / t_solve:.2f}x   (machine dependent)")
    print(f"difference between the two solutions = "
          f"{np.linalg.norm(x_solve - x_inv):.3e}")
    print("\n  Cost is the reproducible part: inv costs one factorisation plus")
    print(f"  a full {n} x {n} matrix multiply; solve costs the factorisation")
    print("  alone. inv is never needed unless the inverse itself is the")
    print("  quantity you must report (for example a full resolution matrix).")


def part4_eigen():
    section("4. Eigenvalues of a matrix whose eigenvalues are known")

    A = np.array([[2.0, 1.0], [1.0, 2.0]])
    values, vectors = np.linalg.eigh(A)     # symmetric -> eigh
    print("A =\n", A)
    print("analytical eigenvalues: 3 and 1")
    print(f"np.linalg.eigh -> {values}")
    print("eigenvectors (columns) =\n", vectors)
    print(f"A @ v == lambda * v : {np.allclose(A @ vectors, vectors * values)}")
    print(f"eigenvectors orthonormal: "
          f"{np.allclose(vectors.T @ vectors, np.eye(2))}")
    print("\n  eigh exploits symmetry and returns real, sorted eigenvalues.")
    print("  eig would work too but gives no symmetry guarantee, and for a")
    print("  symmetric matrix it is both slower and less accurate.")


def part5_conditioning():
    section("5. Conditioning: the Hilbert matrix")

    for n in (4, 8, 12):
        H = np.array([[1.0 / (i + j + 1) for j in range(n)] for i in range(n)])
        print(f"n = {n:>2}: cond(H) = {np.linalg.cond(H):.4e}, "
              f"1/cond(H) = {1.0 / np.linalg.cond(H):.3e}")

    n = 12
    H = np.array([[1.0 / (i + j + 1) for j in range(n)] for i in range(n)])
    x_true = np.ones(n)
    b = H @ x_true
    x = np.linalg.solve(H, b)
    print(f"\nH is non-singular; det(H) = {np.linalg.det(H):.3e}")
    print(f"exact solution x = ones({n}); computed solution error = "
          f"{np.abs(x - 1.0).max():.3e}")
    print(f"that is {np.abs(x - 1.0).max():.1e} of absolute error while the")
    print("right-hand side is O(1) -- the classic demonstration that a")
    print("non-singular matrix can still be numerically unusable.")
    print("\n  Practical rule: if cond(A) approaches 1/eps (about 1e16 in")
    print("  float64), the solution has no correct digits left. Regularise or")
    print("  reparameterise the model instead of blaming the solver.")


def part6_cholesky():
    section("6. Cholesky factorisation of a symmetric positive-definite matrix")

    rng = np.random.default_rng(SEED + 2)
    n = 5
    B = rng.normal(size=(n, n))
    S = B @ B.T + n * np.eye(n)             # symmetric positive definite
    L = np.linalg.cholesky(S)
    print(f"S.shape = {S.shape}")
    print(f"L is lower triangular: "
          f"{np.allclose(L, np.tril(L))}")
    print(f"||L @ L.T - S||_inf = {np.abs(L @ L.T - S).max():.3e}")
    print(f"symmetry of S: {np.allclose(S, S.T)}")
    print(f"all eigenvalues positive: {np.all(np.linalg.eigvalsh(S) > 0)}")
    print(f"cond(S) = {np.linalg.cond(S):.4f}")
    print("\n  Cholesky needs half the work and half the storage of LU and is")
    print("  roughly twice as fast. Least-squares normal matrices and")
    print("  covariance matrices are symmetric positive definite, so it is the")
    print("  right factorisation whenever you can prove definiteness.")


def main():
    print("numpy.linalg -- companion to lesson 03-02-05")
    print(f"numpy version: {np.__version__}, SEED = {SEED}")
    part1_small_system()
    part2_least_squares()
    part3_solve_vs_inv()
    part4_eigen()
    part5_conditioning()
    part6_cholesky()


if __name__ == "__main__":
    main()
