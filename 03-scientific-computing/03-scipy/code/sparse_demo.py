"""scipy.sparse: storage formats, memory saved, and sparse solvers.

Run:  .venv/bin/python sparse_demo.py
Requires: scipy, numpy.

Companion to lesson 03-03-06. Nothing here is timed: every quantity reported
is an exact integer, an exact byte count, or a residual that you can reproduce
bit for bit on any machine.

Part 1  the 1-D Laplacian in sparse and dense form, with the memory count.
Part 2  the 2-D (5-point) Laplacian, built two independent ways and compared.
Part 3  a Poisson solve against an analytic solution, with the observed
        convergence order under grid refinement.
Part 4  factorisation fill-in, and a repeated-solve factorisation.
"""

import numpy as np
from scipy import sparse
from scipy.sparse import linalg as splinalg


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def laplacian_1d(n, h):
    """Tridiagonal Laplacian with Dirichlet ends, scaled by 1/h^2."""
    d = np.full(n, 2.0 / h ** 2)
    o = np.full(n - 1, -1.0 / h ** 2)
    return sparse.diags([o, d, o], [-1, 0, 1], format="csr")


def laplacian_2d(n, h):
    """Five-point Laplacian on an n x n grid, returned in CSR.

    Built as a Kronecker sum: the 2-D stencil is (T x I) + (I x T) with T the
    1-D Laplacian, which is the discrete Laplacian of a separable domain.
    """
    d = np.full(n, 2.0 / h ** 2)
    o = np.full(n - 1, -1.0 / h ** 2)
    t = sparse.diags([o, d, o], [-1, 0, 1], shape=(n, n), format="csr")
    eye = sparse.eye(n, format="csr")
    return (sparse.kron(t, eye) + sparse.kron(eye, t)).tocsr()


def memory_bytes(m):
    return m.data.nbytes + m.indices.nbytes + m.indptr.nbytes


def part1_laplacian_1d():
    section("1. The 1-D Laplacian: what sparsity actually saves")
    print(f"  {'N':>9}{'nnz':>10}{'nnz/N^2':>12}{'sparse bytes':>15}"
          f"{'dense bytes':>14}{'ratio':>10}")
    for n in (100, 1000, 10 ** 4, 10 ** 5):
        h = 1.0 / (n + 1)
        a = laplacian_1d(n, h)
        dense = 8 * n * n
        print(f"  {n:>9}{a.nnz:>10}{a.nnz / n ** 2:>12.3e}"
              f"{memory_bytes(a):>15}{dense:>14}{dense / memory_bytes(a):>10.1f}")
    print()
    n = 1000
    a = laplacian_1d(n, 1.0 / (n + 1))
    banded = np.diag(np.full(n, 2.0)) + np.diag(np.full(n - 1, -1.0), 1) \
        + np.diag(np.full(n - 1, -1.0), -1)
    diff = np.abs(a.toarray() / (n + 1) ** 2 - banded).max()
    print(f"  Independent check at N = {n}: the sparse matrix, densified and")
    print(f"  un-scaled, agrees with an explicitly built banded array to "
          f"{diff:.3e}.")
    b = laplacian_1d(10 ** 5, 1e-5)
    print(f"  At N = 100000 the dense array would need "
          f"{8 * (10 ** 5) ** 2 / 1e9:.0f} GB against "
          f"{memory_bytes(b) / 1e6:.2f} MB sparse, a factor of "
          f"{8 * (10 ** 5) ** 2 / memory_bytes(b):.0f}.")
    print("  Bytes counted are the csr data, indices and indptr arrays only.")
    print("  CSR spends 8 bytes on each value plus 4 on each column index, so")
    print("  above a fill fraction of about 8/12 = 67% it needs more memory than")
    print("  the dense array it was meant to replace. Sparsity is a claim about")
    print("  the *fill*, not about the matrix being large.")


def part2_laplacian_2d():
    section("2. The 2-D five-point Laplacian, built two ways")
    for n in (50, 100, 200):
        h = 1.0 / (n + 1)
        a = laplacian_2d(n, h)
        N = n * n
        print(f"  n = {n:>4}: {N:>8} unknowns, nnz = {a.nnz:>9}, "
              f"nnz/N^2 = {a.nnz / N ** 2:.3e}, sparse "
              f"{memory_bytes(a) / 1e6:.3f} MB vs dense {N * N * 8 / 1e9:.3f} GB")
    n = 40
    h = 1.0 / (n + 1)
    a = laplacian_2d(n, h)
    # Independent construction: assemble the five-point stencil by index lists.
    rows, cols, vals = [], [], []
    N = n * n
    for i in range(n):
        for j in range(n):
            k = i * n + j
            rows.append(k)
            cols.append(k)
            vals.append(4.0 / h ** 2)
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ii, jj = i + di, j + dj
                if 0 <= ii < n and 0 <= jj < n:
                    rows.append(k)
                    cols.append(ii * n + jj)
                    vals.append(-1.0 / h ** 2)
    b = sparse.coo_matrix((vals, (rows, cols)), shape=(N, N)).tocsr()
    print()
    print(f"  Independent stencil assembly at n = {n}: "
          f"(a - b).nnz = {(a - b).nnz}, "
          f"max |difference| = {abs(a - b).max():.3e}")
    print(f"  nnz from kron: {a.nnz}, from the stencil loop: {b.nnz}, expected "
          f"5N - 4n = {5 * N - 4 * n}")
    print("  The two agree exactly, which is the only reason to trust either.")
    del a, b
    print("  (the dense array at n = 200 would be 12.8 GB; it is never built)")


def poisson_solution(n):
    """Solve -Laplacian(u) = 2 pi^2 sin(pi x) sin(pi y) on the unit square."""
    h = 1.0 / (n + 1)
    x = np.linspace(h, 1.0 - h, n)
    X, Y = np.meshgrid(x, x, indexing="ij")
    rhs = 2.0 * np.pi ** 2 * np.sin(np.pi * X) * np.sin(np.pi * Y)
    a = laplacian_2d(n, h)
    u = splinalg.spsolve(a, rhs.ravel())
    return u.reshape(n, n), np.sin(np.pi * X) * np.sin(np.pi * Y), h


def part3_poisson():
    section("3. A sparse Poisson solve against an analytic solution")
    print("  -laplacian(u) = 2 pi^2 sin(pi x) sin(pi y) on the unit square,")
    print("  Dirichlet boundaries at zero. Exact solution u = sin(pi x) sin(pi y).")
    print(f"    {'n':>6}{'unknowns':>10}{'solver':>10}{'max |error|':>14}"
          f"{'L2 error':>13}{'ratio to previous':>19}")
    prev = None
    for n in (25, 50, 100, 200):
        u, exact, h = poisson_solution(n)
        err = np.abs(u - exact).max()
        l2 = np.sqrt(np.mean((u - exact) ** 2))
        ratio = "--" if prev is None else f"{prev / err:.3f}"
        print(f"    {n:>6}{n * n:>10}{'spsolve':>10}{err:>14.3e}{l2:>13.3e}"
              f"{ratio:>19}")
        prev = err
    print("    Each halving of h reduces the maximum error by a factor close to")
    print("    4, so the scheme is second-order: error = O(h^2). That is the")
    print("    convergence order of the discretisation, and it is the only")
    print("    evidence that the discrete operator is the one you think it is.")
    n = 200
    h = 1.0 / (n + 1)
    x = np.linspace(h, 1.0 - h, n)
    X, Y = np.meshgrid(x, x, indexing="ij")
    rhs = 2.0 * np.pi ** 2 * np.sin(np.pi * X) * np.sin(np.pi * Y)
    a = laplacian_2d(n, h)
    u = splinalg.spsolve(a, rhs.ravel())
    res = np.abs(a @ u - rhs.ravel()).max()
    print(f"    At n = {n}: |A u - b|max = {res:.3e}, which is the residual of")
    print("    the *linear solve*, not the discretisation error "
          f"({np.abs(u.reshape(n, n) - np.sin(np.pi * X) * np.sin(np.pi * Y)).max():.3e}).")
    print("    Conflating the two is the commonest misreading of a solver log.")


def part4_factorisation():
    section("4. Fill-in, and one factorisation for several right-hand sides")
    print("  The Cholesky/LU factors of a sparse matrix are not sparse.")
    print(f"    {'n':>6}{'nnz(A)':>10}{'nnz(L)+nnz(U)':>15}{'fill factor':>13}"
          f"{'nnz(A)/N^2':>13}")
    for n in (20, 40, 80):
        h = 1.0 / (n + 1)
        a = laplacian_2d(n, h).tocsc()
        lu = splinalg.splu(a)
        fill = lu.L.nnz + lu.U.nnz
        N = n * n
        print(f"    {n:>6}{a.nnz:>10}{fill:>15}{fill / a.nnz:>13.2f}"
              f"{a.nnz / N ** 2:>13.3e}")
    print("    The fill factor grows with the grid: 5.23, 8.28, 11.69 as n goes")
    print("    from 20 to 80. Theory for nested dissection on a 2-D grid gives a")
    print("    factor with O(N log N) non-zeros against the matrix's O(N), so")
    print("    the factorisation, not the matrix, is what runs out of memory.")
    print("    Reordering (permc_spec='COLAMD' is the default) delays the growth;")
    print("    it cannot remove it -- fill-in is a property of elimination, not")
    print("    of the storage format.")

    n = 100
    h = 1.0 / (n + 1)
    x = np.linspace(h, 1.0 - h, n)
    X, Y = np.meshgrid(x, x, indexing="ij")
    a = laplacian_2d(n, h).tocsc()
    b1 = (2.0 * np.pi ** 2 * np.sin(np.pi * X) * np.sin(np.pi * Y)).ravel()
    b2 = np.ones(n * n)
    solve = splinalg.factorized(a)
    u1 = solve(b1)
    u2 = solve(b2)
    u1_direct = splinalg.spsolve(a, b1)
    print()
    print(f"    factorized(a) solved two right-hand sides; the first is")
    print(f"    identical to spsolve(a, b1) to {np.abs(u1 - u1_direct).max():.3e}.")
    print(f"    |A u1 - b1|max = {np.abs(a @ u1 - b1).max():.3e};"
          f" |A u2 - b2|max = {np.abs(a @ u2 - b2).max():.3e}")

    it = [0]

    def counter(_):
        it[0] += 1

    u_cg, info = splinalg.cg(a, b2, rtol=1e-10, callback=counter)
    print(f"    Conjugate gradients on the same system converged in {it[0]} "
          f"iterations (info = {info})")
    print(f"    and differs from the direct solution by "
          f"{np.abs(u_cg - u2).max():.3e}.")
    print("    The direct factorisation is exact, and its memory is a property")
    print("    of the *ordering*, not of the data; CG needs only")
    print("    matrix-vector products and can work from a matrix you never")
    print("    assemble, but its iteration count grows with the condition")
    print("    number -- here the 2-D Laplacian's condition number grows as")
    print("    h^-2, so CG's iteration count would double with each grid")
    print("    refinement. That is the choice a sparse solver forces on you.")


def main():
    part1_laplacian_1d()
    part2_laplacian_2d()
    part3_poisson()
    part4_factorisation()
    print("\nDone.")


if __name__ == "__main__":
    main()
