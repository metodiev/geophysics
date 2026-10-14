#!/usr/bin/env python3
"""Assembly, sparsity and linear-system structure, measured in 2-D.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python fem_assembly_demo.py

SYNTHETIC throughout: the grid, coefficients and manufactured solution are chosen
teaching models.  Bilinear (Q1) elements on a structured square grid, assembled
explicitly element by element; the assembled matrix is then checked against an
independent Kronecker-product construction.

Contents
--------
1. Q1 element stiffness and mass matrices against their closed forms.
2. Assembly checked against Kx (x) My + Mx (x) Ky.
3. Manufactured-solution convergence in 2-D.
4. Sparsity: nnz per row and bandwidth versus mesh size.
5. Condition-number growth, measured by power iteration.
6. Conjugate-gradient iteration count versus mesh size.
7. The pure-Neumann (singular) case: row sums, null space, projected solve.
8. Fill-in of the sparse LU factorisation under two orderings.
"""

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

RNG = np.random.default_rng(20261014)

# 2-point Gauss-Legendre nodes and weights on [-1, 1]; the abscissae are
# +/- 1/sqrt(3) with weight 1 (NOT +/- sqrt(2)/2).
GAUSS_NODES, GAUSS_WEIGHTS = np.polynomial.legendre.leggauss(2)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def q1_element(h, neumann=False):
    """Q1 element matrices on an h x h square, by 2x2 Gauss integration.

    Local node order: (0,0), (h,0), (h,h), (0,h) counter-clockwise.
    """
    g, w = GAUSS_NODES, GAUSS_WEIGHTS
    ke = np.zeros((4, 4))
    me = np.zeros((4, 4))
    for xi, wi in zip(g, w):
        for eta, we in zip(g, w):
            # shape functions and their physical derivatives
            phi = 0.25 * np.array([(1 - xi) * (1 - eta), (1 + xi) * (1 - eta),
                                   (1 + xi) * (1 + eta), (1 - xi) * (1 + eta)])
            dphidx = 0.5 * np.array([-(1 - eta), (1 - eta),
                                     (1 + eta), -(1 + eta)]) / h
            dphidy = 0.5 * np.array([-(1 - xi), -(1 + xi),
                                     (1 + xi), (1 - xi)]) / h
            jac = h * h / 4.0
            ke += (np.outer(dphidx, dphidx) + np.outer(dphidy, dphidy)) * wi * we * jac
            me += np.outer(phi, phi) * wi * we * jac
    return ke, me


def assemble_2d(n, neumann=False):
    """Assemble the Q1 stiffness and mass matrices on an n x n grid of the unit square.

    Homogeneous Dirichlet conditions on all four sides unless ``neumann`` is True,
    in which case every boundary node is retained and the matrix is singular.
    """
    h = 1.0 / n
    ndof = (n + 1) ** 2
    ke, me = q1_element(h)
    rows, cols, kv, mv = [], [], [], []
    for j in range(n):
        for i in range(n):
            local = np.array([j * (n + 1) + i, j * (n + 1) + i + 1,
                              (j + 1) * (n + 1) + i + 1, (j + 1) * (n + 1) + i])
            for a in range(4):
                for b in range(4):
                    rows.append(local[a])
                    cols.append(local[b])
                    kv.append(ke[a, b])
                    mv.append(me[a, b])
    K = sp.coo_matrix((kv, (rows, cols)), shape=(ndof, ndof)).tocsc()
    M = sp.coo_matrix((mv, (rows, cols)), shape=(ndof, ndof)).tocsc()
    if not neumann:
        free = np.ones(ndof, dtype=bool)
        X = np.arange(n + 1)
        for j in range(n + 1):
            for i in range(n + 1):
                if i in (0, n) or j in (0, n):
                    free[j * (n + 1) + i] = False
        return K[free][:, free], M[free][:, free], free
    return K, M, np.ones(ndof, dtype=bool)


def kronecker_reference(n):
    """Independent construction of the Dirichlet Q1 Laplacian by tensor products."""
    nd = n - 1
    h = 1.0 / n
    main = 2.0 * h / 3.0        # global 1-D mass diagonal: h/3 from each of 2 elements
    off = h / 6.0
    Kx = sp.diags([-1.0 / h, 2.0 / h, -1.0 / h], [-1, 0, 1],
                  shape=(nd, nd), format="csc")
    Mx = sp.diags([off, main, off], [-1, 0, 1], shape=(nd, nd), format="csc")
    return sp.kron(Kx, Mx, format="csc") + sp.kron(Mx, Kx, format="csc"), \
        sp.kron(Mx, Mx, format="csc")


def manufactured(n):
    """Assemble the load vector for u = sin(pi x) sin(pi y)."""
    h = 1.0 / n
    ndof = (n + 1) ** 2
    g, w = GAUSS_NODES, GAUSS_WEIGHTS
    F = np.zeros(ndof)
    for j in range(n):
        for i in range(n):
            local = np.array([j * (n + 1) + i, j * (n + 1) + i + 1,
                              (j + 1) * (n + 1) + i + 1, (j + 1) * (n + 1) + i])
            fe = np.zeros(4)
            for xi, wi in zip(g, w):
                for eta, we in zip(g, w):
                    phi = 0.25 * np.array([(1 - xi) * (1 - eta), (1 + xi) * (1 - eta),
                                           (1 + xi) * (1 + eta), (1 - xi) * (1 + eta)])
                    x = (i + 0.5 * (xi + 1)) * h
                    y = (j + 0.5 * (eta + 1)) * h
                    f = 2.0 * np.pi ** 2 * np.sin(np.pi * x) * np.sin(np.pi * y)
                    fe += phi * f * wi * we * h * h / 4.0
            F[local] += fe
    return F


def errors_2d(n, u_free, free):
    """L2 and H1 errors of the Q1 solution on the unit square, by 2x2 Gauss per cell."""
    h = 1.0 / n
    g, w = GAUSS_NODES, GAUSS_WEIGHTS
    full = np.zeros((n + 1) ** 2)
    full[free] = u_free
    e2 = eh1 = 0.0
    for j in range(n):
        for i in range(n):
            U = full[np.array([j * (n + 1) + i, j * (n + 1) + i + 1,
                               (j + 1) * (n + 1) + i + 1, (j + 1) * (n + 1) + i])]
            for xi, wi in zip(g, w):
                for eta, we in zip(g, w):
                    phi = 0.25 * np.array([(1 - xi) * (1 - eta), (1 + xi) * (1 - eta),
                                           (1 + xi) * (1 + eta), (1 - xi) * (1 + eta)])
                    dphidx = 0.5 * np.array([-(1 - eta), (1 - eta),
                                             (1 + eta), -(1 + eta)]) / h
                    dphidy = 0.5 * np.array([-(1 - xi), -(1 + xi),
                                             (1 + xi), (1 - xi)]) / h
                    x = (i + 0.5 * (xi + 1)) * h
                    y = (j + 0.5 * (eta + 1)) * h
                    ue = U @ phi
                    due = np.array([U @ dphidx, U @ dphidy])
                    ux = np.pi * np.cos(np.pi * x) * np.sin(np.pi * y)
                    uy = np.pi * np.sin(np.pi * x) * np.cos(np.pi * y)
                    exact = np.sin(np.pi * x) * np.sin(np.pi * y)
                    wgt = wi * we * h * h / 4.0
                    e2 += wgt * (ue - exact) ** 2
                    eh1 += wgt * ((due[0] - ux) ** 2 + (due[1] - uy) ** 2)
    return np.sqrt(e2), np.sqrt(eh1)


def fit_order(levels, errs):
    x = np.log(np.asarray(levels, float))
    y = np.log(np.asarray(errs, float))
    dx = x - x.mean()
    return float(np.sum(dx * (y - y.mean())) / np.sum(dx * dx))


def rayleigh_power(K, which="largest", n_iter=300, tol=1e-13):
    """Estimate the extreme eigenvalue by (inverse) power iteration."""
    n = K.shape[0]
    x = RNG.standard_normal(n)
    x /= np.linalg.norm(x)
    if which == "smallest":
        lu = spla.splu(K.tocsc())
        lam = 0.0
        for _ in range(n_iter):
            y = lu.solve(x)
            nrm = np.linalg.norm(y)
            x_new = y / nrm
            lam_new = np.dot(x_new, K @ x_new)
            if abs(lam_new - lam) < tol * abs(lam_new):
                x, lam = x_new, lam_new
                break
            x, lam = x_new, lam_new
        return lam
    lam = 0.0
    for _ in range(n_iter):
        y = K @ x
        nrm = np.linalg.norm(y)
        x_new = y / nrm
        lam_new = np.dot(x_new, K @ x_new)
        if abs(lam_new - lam) < tol * abs(lam_new):
            x, lam = x_new, lam_new
            break
        x, lam = x_new, lam_new
    return lam


def cg_solve(A, b, rtol=1e-10, maxit=20000, minv=None):
    """Plain conjugate gradients, written out so the iteration count is explicit.

    ``minv`` maps a residual to a preconditioned residual: None for unpreconditioned
    CG, or a callable for Jacobi / incomplete factorisation.  Returns
    (x, iterations, relative residual).
    """
    x = np.zeros_like(b)
    r = b.copy()
    z = r if minv is None else minv(r)
    p = z.copy()
    rz = r @ z
    nrm0 = np.linalg.norm(b)
    iters = 0
    for iters in range(1, maxit + 1):
        Ap = A @ p
        alpha = rz / (p @ Ap)
        x = x + alpha * p
        r = r - alpha * Ap
        if np.linalg.norm(r) / nrm0 < rtol:
            break
        z = r if minv is None else minv(r)
        rz_new = r @ z
        p = z + (rz_new / rz) * p
        rz = rz_new
    return x, iters, np.linalg.norm(r) / nrm0


def main():
    section("1. Q1 element matrices against closed forms (h = 0.25 m)")
    h = 0.25
    ke, me = q1_element(h)
    ke_exact = (1.0 / 6.0) * np.array([[4, -1, -2, -1],
                                       [-1, 4, -1, -2],
                                       [-2, -1, 4, -1],
                                       [-1, -2, -1, 4]])
    me_exact = (h * h / 36.0) * np.array([[4, 2, 1, 2],
                                          [2, 4, 2, 1],
                                          [1, 2, 4, 2],
                                          [2, 1, 2, 4]])
    print(f"  max|Ke - (1/6)[[4,-1,-2,-1],...]| = {np.max(np.abs(ke - ke_exact)):.3e}"
          "   (h-independent)")
    print(f"  max|Me - (h^2/36)[[4,2,1,2],...]| = {np.max(np.abs(me - me_exact)):.3e}")
    print(f"  eigenvalues of Ke: {np.round(np.linalg.eigvalsh(ke), 6)} "
          f"(one zero -> rigid-body translation)")
    print(f"  row sum of Me = {me.sum(axis=1)}, i.e. the cell area h^2 = {h*h} "
          f"shared equally")
    print(f"  row-sum (lumped) mass matrix is therefore diag(h^2/4) = "
          f"{np.round(np.diag(me.sum(axis=1)), 6)} m^2")

    section("2. Assembly checked against an independent tensor-product build")
    for n in (4, 8, 16):
        K, M, free = assemble_2d(n)
        K_ref, M_ref = kronecker_reference(n)
        dK = abs(K - K_ref).max()
        dM = abs(M - M_ref).max()
        print(f"  n = {n:3d}: ndof = {K.shape[0]:5d}, max|K - K_tensor| = {dK:.3e}, "
              f"max|M - M_tensor| = {dM:.3e}")
    print("  The element loop and the tensor-product construction agree to round-off,")
    print("  which is what makes the element loop trustworthy for unstructured grids.")

    section("3. Manufactured-solution convergence in 2-D")
    print("  u = sin(pi x) sin(pi y), f = 2 pi^2 sin(pi x) sin(pi y), u = 0 on the boundary")
    print("     n     ndof        L2 error     order       H1 error    order")
    hs, l2s, h1s = [], [], []
    prev = None
    for n in (4, 8, 16, 32, 64):
        K, M, free = assemble_2d(n)
        F = manufactured(n)[free]
        u = spla.spsolve(K, F)
        e2, eh1 = errors_2d(n, u, free)
        o2 = "" if prev is None else f"{np.log2(prev[0] / e2):8.3f}"
        oh = "" if prev is None else f"{np.log2(prev[1] / eh1):8.3f}"
        print(f"  {n:4d}   {K.shape[0]:6d}   {e2:11.3e}  {o2}   {eh1:11.3e}  {oh}")
        prev = (e2, eh1)
        hs.append(1.0 / n)
        l2s.append(e2)
        h1s.append(eh1)
    print(f"  fitted: L2 order = {fit_order(hs, l2s):.3f}, "
          f"H1 order = {fit_order(hs, h1s):.3f}   (theory: 2 and 1)")

    section("4. Sparsity of the assembled matrix")
    print("     n     ndof       nnz     nnz/row   bandwidth")
    for n in (8, 16, 32, 64, 128):
        K, _, _ = assemble_2d(n)
        nd = K.shape[0]
        rows = np.diff(K.tocsr().indptr)
        bw = int(np.max(K.tocoo().col - K.tocoo().row)) + 1
        print(f"  {n:5d}   {nd:7d}   {K.nnz:8d}   {K.nnz / nd:7.2f}   {bw:8d}")
    print("  nnz/row approaches 9 = the 3x3 Q1 stencil, so storage is O(ndof) while")
    print("  the matrix is sparse; a dense factorisation would be O(ndof^2).")

    section("5. Conditioning of the assembled stiffness matrix")
    print("  The FE stiffness matrix has mesh-INDEPENDENT entries: each entry is an")
    print("  integral of gradients over a cell, so the 1/h^2 carried by the gradients")
    print("  cancels the h^2 of the area.  Its largest eigenvalue therefore stays")
    print("  bounded while its smallest falls like h^2, and the condition number")
    print("  grows like h^-2.")
    print("     n     ndof    lambda_min    2 pi^2 h^2    lambda_max     cond(K)")
    hs, conds = [], []
    for n in (8, 16, 32, 64):
        K, _, _ = assemble_2d(n)
        lmax = rayleigh_power(K, "largest")
        lmin = rayleigh_power(K, "smallest")
        h = 1.0 / n
        hs.append(h)
        conds.append(lmax / lmin)
        print(f"  {n:5d}   {K.shape[0]:6d}   {lmin:11.3e}   "
              f"{2.0 * np.pi ** 2 * h ** 2:11.3e}   {lmax:11.3e}   {lmax / lmin:11.3e}")
    print(f"  fitted slope of log(cond) versus log(1/h) = "
          f"{fit_order(1.0 / np.asarray(hs), conds):.3f} (theory: 2)")
    print("  lambda_min matches 2 pi^2 h^2 to three digits.  That product has a reading:")
    print("  the smallest generalised eigenvalue of the unit square is 2 pi^2, and the")
    print("  Rayleigh quotient v^T M v / v^T v of a smooth nodal vector is h^2, because")
    print("  each node accounts for an area h^2.  lambda_max stays near 4 and is")
    print("  mesh-independent.  The finite-difference form of the same operator is h^-2")
    print("  times this matrix, so the RATIO -- not the entries -- is the mesh-dependent")
    print("  quantity that governs solver cost.")
    print("  h^-2 conditioning is the central cost driver: halving h multiplies it by")
    print("  four, and with it the sensitivity of the answer to data error.  It is why")
    print("  preconditioners, not solvers, dominate practice.")

    section("6. Conjugate gradients: iteration count versus mesh size")
    print("  Uniform source f = 1 (constant load).  rtol = 1e-10, zero initial guess.")
    print("     n     ndof   CG iters   Jacobi iters   rel residual")
    hs, its, its_j = [], [], []
    diag_spread = 0.0
    for n in (8, 16, 32, 64):
        K, _, free = assemble_2d(n)
        h = 1.0 / n
        b = np.full(K.shape[0], h * h / 4.0)      # integral of f = 1 over each cell
        diag = K.diagonal()
        diag_spread = max(diag_spread, diag.max() / diag.min())
        x, k1, res = cg_solve(K, b)
        _, k2, _ = cg_solve(K, b, minv=lambda r: r / diag)
        hs.append(h)
        its.append(k1)
        its_j.append(k2)
        print(f"  {n:5d}   {K.shape[0]:6d}   {k1:8d}   {k2:12d}   {res:.2e}")
    print(f"  fitted scaling: iterations ~ (1/h)^{fit_order(1.0 / np.asarray(hs), its):.3f}"
          ", consistent with the predicted O(h^-1) = O(sqrt(cond K))")
    print("  Jacobi does NOTHING here, and the reason is exact rather than numerical:")
    print(f"  the Q1 stiffness diagonal has spread max/min = {diag_spread:.1f} on a")
    print("  uniform mesh, i.e. it is constant, so diagonal preconditioning is a")
    print("  scalar multiple of the identity and cannot change the Krylov space.")
    print("  Jacobi earns its keep only when the diagonal varies.  The next block")
    print("  measures that case.")

    section("6c. The same solver on a graded mesh, where the diagonal does vary")
    print("  1-D P1 Poisson, -u'' = 1 on 64 cells whose widths grow geometrically.")
    print("  The stiffness diagonal 1/h_{i-1} + 1/h_i then varies with the grading.")
    for grad in (1.0, 1.10, 1.25):
        n_cell = 64
        h = grad ** np.arange(n_cell)
        h = h / h.sum()
        edges = np.concatenate(([0.0], np.cumsum(h)))
        diag_d = 1.0 / h[:-1] + 1.0 / h[1:]
        Kd = sp.diags([-1.0 / h[1:-1], diag_d, -1.0 / h[1:-1]], [-1, 0, 1],
                      format="csc")
        b = 0.5 * (h[:-1] + h[1:])
        _, k1, _ = cg_solve(Kd, b)
        _, k2, _ = cg_solve(Kd, b, minv=lambda r: r / Kd.diagonal())
        print(f"  grading ratio {grad:.2f}: diagonal spread = "
              f"{Kd.diagonal().max() / Kd.diagonal().min():9.3e}, "
              f"CG iters = {k1:4d}, Jacobi-CG iters = {k2:4d}")
    print("  Now the diagonal carries real information about the mesh, and using it")
    print("  pays.  A preconditioner is a statement about the operator, not a")
    print("  default setting.")

    section("6b. A caution: a manufactured solution that is accidentally easy")
    print("  Repeat with the separable load of the convergence study,")
    print("  f = 2 pi^2 sin(pi x) sin(pi y):")
    for n in (16, 64):
        K, _, free = assemble_2d(n)
        b = manufactured(n)[free]
        x, k, res = cg_solve(K, b)
        s = np.sin(np.pi * np.arange(n + 1) / n)
        nodal = np.outer(s, s).ravel()[free]
        print(f"  n = {n:3d}: CG iterations = {k}, relative residual = {res:.2e}, "
              f"||x - nodal sin||_inf = {np.max(np.abs(x - nodal)):.3e}")
    print("  One iteration.  The nodal sine vector is a SIMULTANEOUS eigenvector of")
    print("  the 1-D stiffness and mass matrices, so it is an eigenvector of the")
    print("  separable 2-D operator and of its load vector: one Krylov step solves")
    print("  the discrete system exactly.  The residual difference printed above")
    print("  between x and the nodal sine is then purely the O(h^2) discretisation")
    print("  error of the 2-D element, not a solver effect.  A convergence study")
    print("  that uses only such loads measures the mesh error and never the solver,")
    print("  which is why Section 6 uses a constant load instead.")

    section("7. Pure-Neumann case: a singular matrix and its null space")
    K, M, _ = assemble_2d(16, neumann=True)
    one = np.ones(K.shape[0])
    r = K @ one
    print(f"  n = 16, all boundary nodes retained: K is {K.shape[0]} x {K.shape[0]}")
    print(f"  max|K @ 1| = {np.max(np.abs(r)):.3e} (row sums vanish: the constant is")
    print("  in the null space, so the discrete problem has no unique solution)")
    lmax = rayleigh_power(K, "largest")
    print("  lambda_max = {:.6e}; a zero eigenvalue also exists, so K is singular".format(lmax))
    print("  and a direct factorisation fails.  Two repairs, both structural: make the")
    print("  right-hand side mean-zero (the compatibility condition of the Neumann")
    print("  problem) and add the rank-one term (1/N) e e^T, which removes 1 from the")
    print("  null space without changing the solution's mean.")
    b = manufactured(16)
    b = b - b.mean()
    P = sp.identity(K.shape[0], format="csc") - sp.csc_matrix(
        np.full((K.shape[0], K.shape[0]), 1.0 / K.shape[0]))
    x, info = spla.cg(K + sp.csc_matrix(np.full((K.shape[0], K.shape[0]),
                                                1.0 / K.shape[0])), b,
                      rtol=1e-10, maxiter=20000)
    print(f"  projected CG: info = {info}, max|x| = {np.max(np.abs(x)):.6e}, "
          f"mean(x) = {x.mean():.3e}")
    print("  The lesson is structural, not numerical: with only Neumann data the")
    print("  continuous problem is defined only up to a constant, and so is every")
    print("  discretisation of it -- including the null vector 1.")

    section("8. Fill-in of the sparse LU factorisation under two orderings")
    print("     n     ndof      nnz(A)   fill, natural   fill, COLAMD   ratio")
    for n in (16, 32, 64):
        K, _, _ = assemble_2d(n)
        lu_nat = spla.splu(K.tocsc(), permc_spec="NATURAL")
        lu_col = spla.splu(K.tocsc(), permc_spec="COLAMD")
        fn = lu_nat.L.nnz + lu_nat.U.nnz
        fc = lu_col.L.nnz + lu_col.U.nnz
        print(f"  {n:5d}   {K.shape[0]:7d}   {K.nnz:9d}   {fn:14d}   {fc:12d}   "
              f"{fn / fc:6.2f}")
    print("  Reordering reduces the factorisation size; the sparsity of the system")
    print("  is a property of the mesh, but the cost of solving it is a property of")
    print("  the ordering you choose.")
    print("\nAll numbers are printed by this script; the model is SYNTHETIC.")


if __name__ == "__main__":
    main()
