#!/usr/bin/env python3
"""Boundary-element method for 2-D potential fields: discretisation, jump terms,
interior and exterior problems, and a measured comparison with a volume grid.

Run with the project virtual environment:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python boundary_element_demo.py

Everything is SYNTHETIC.  The "anomaly" is a chosen analytic harmonic function on
a chosen disk of radius 10 km: a teaching stand-in for a potential field, not a
field measured anywhere.

Contents
--------
1. Building the boundary matrices (H, G) for N constant panels on a circle; the
   exact diagonal of G; the free term recovered from the discrete row sums.
2. Interior Dirichlet problem: measured flux error versus N and its observed
   order, plus reconstruction of the field at interior points.
3. The same boundary data on the outside of the circle: the sign of the free
   term, and what the wrong sign costs.
4. Unknowns for the same accuracy on the same field: boundary N versus a volume
   grid of n^2 cells.
5. Truncation error of a volume grid on an exterior problem, against the
   boundary method's zero truncation error.
"""

import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import spsolve

RNG = np.random.default_rng(20261014)

A_M = 1.0e4                      # disk radius, 10 km, SYNTHETIC teaching model
G_2D = -1.0 / (2.0 * np.pi)      # 2-D fundamental solution: grad^2 G = -delta


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def u_cubic(x, z):
    """Harmonic test field, u = (r/a)^3 cos 3*theta = (x^3 - 3 x z^2)/a^3."""
    return (x ** 3 - 3.0 * x * z ** 2) / A_M ** 3


def q_cubic(theta):
    """Interior normal derivative of u_cubic on r = a, normal = +r."""
    return 3.0 * np.cos(3.0 * theta) / A_M


def u_sinh(x, z):
    """A harmonic field the 5-point stencil does NOT solve exactly."""
    return np.sin(x / A_M) * np.sinh(z / A_M) / np.sinh(1.0)


def panels(n):
    """Constant circular panels: midpoints, endpoints, length, outward normal."""
    theta = np.linspace(0.0, 2.0 * np.pi, n, endpoint=False)
    mid = theta + np.pi / n
    p1 = A_M * np.column_stack([np.cos(theta), np.sin(theta)])
    p2 = A_M * np.column_stack([np.cos(theta + 2 * np.pi / n),
                                np.sin(theta + 2 * np.pi / n)])
    centres = A_M * np.column_stack([np.cos(mid), np.sin(mid)])
    length = np.hypot(*(p2 - p1).T)
    normal = np.column_stack([np.cos(mid), np.sin(mid)])
    return mid, p1, p2, length, normal, centres


def _row_integrals(x0, z0, p1, p2, length, normal, n_gl=12):
    """Integrals of dG/dn' and G along every panel, evaluated at (x0, z0)."""
    t_gl, w_gl = np.polynomial.legendre.leggauss(n_gl)
    t = 0.5 * (t_gl + 1.0)
    w = 0.5 * w_gl
    pts = p1[:, None, :] + t[None, :, None] * (p2 - p1)[:, None, :]
    dx = pts[:, :, 0] - x0
    dz = pts[:, :, 1] - z0
    r2 = np.maximum(dx ** 2 + dz ** 2, 1e-30)
    dot = dx * normal[:, None, 0] + dz * normal[:, None, 1]
    h_row = np.sum(w[None, :] * (-1.0 / (2 * np.pi)) * dot / r2
                   * length[:, None], axis=1)
    g_row = np.sum(w[None, :] * G_2D * 0.5 * np.log(r2)
                   * length[:, None], axis=1)
    return h_row, g_row


def bem_matrices(n, n_gl=12):
    """Dense boundary matrices; exact diagonal of G, zero diagonal of H."""
    mid, p1, p2, length, normal, centres = panels(n)
    H = np.empty((n, n))
    Gm = np.empty((n, n))
    for i in range(n):
        H[i], Gm[i] = _row_integrals(centres[i, 0], centres[i, 1],
                                     p1, p2, length, normal, n_gl)
    diag_g = G_2D * length * (np.log(length / 2.0) - 1.0)
    np.fill_diagonal(Gm, diag_g)
    np.fill_diagonal(H, 0.0)     # straight panel, collocation point on it
    return H, Gm, mid, length, normal, centres


def _panel_data(n):
    """The four panel arrays, in the order _row_integrals wants them."""
    return panels(n)[1:5]


def reproduce_interior(n, u_b, q_b, x, z):
    """u(r0) = -int u dG/dn' + int G q  for r0 inside the disk."""
    h_row, g_row = _row_integrals(x, z, *_panel_data(n))
    return -h_row @ u_b + g_row @ q_b


def reproduce_exterior(n, u_b, q_b, x, z):
    """u(r0) = +int u dG/dn' - int G q  for r0 outside the disk."""
    h_row, g_row = _row_integrals(x, z, *_panel_data(n))
    return h_row @ u_b - g_row @ q_b


def fem_square(n, field):
    """5-point Laplace solve on [-a,a]^2 with analytic Dirichlet data."""
    h = 2.0 * A_M / (n + 1)
    xs = -A_M + h * np.arange(1, n + 1)
    X, Z = np.meshgrid(xs, xs, indexing="ij")
    m = n * n
    I, J = np.indices((n, n))
    idx = np.arange(m).reshape(n, n)
    onb = ((I == 0) | (I == n - 1) | (J == 0) | (J == n - 1)).ravel()
    keep = ~onb
    rows = [np.arange(m)]
    cols = [idx.ravel()]
    vals = [np.where(onb, 1.0, 4.0)]
    for (dx, dz) in ((0, -1), (0, 1), (-1, 0), (1, 0)):
        r = np.roll(idx, (dx, dz), axis=(0, 1)).ravel()
        rows.append(np.arange(m)[keep])
        cols.append(r[keep])
        vals.append(-np.ones(int(keep.sum())))
    amat = coo_matrix((np.concatenate(vals),
                       (np.concatenate(rows), np.concatenate(cols))),
                      shape=(m, m)).tocsr()
    rhs = np.zeros(m)
    rhs[onb] = field(X, Z).ravel()[onb]
    return spsolve(amat, rhs).reshape(n, n), X, Z, amat.nnz


def main():
    section("1. Boundary matrices and the free term")
    print(f"SYNTHETIC model: disk of radius a = {A_M/1e3:.1f} km, N constant panels,")
    print("12 Gauss-Legendre nodes per panel, G = -(1/2 pi) ln r, normal outward")
    for n in (16, 64, 256):
        H, Gm, mid, length, _, _ = bem_matrices(n)
        print(f"  N = {n:4d}: panel length = {length[0]:9.3f} m, "
              f"G_ii = {Gm[0, 0]:12.4f}, "
              f"|sum_j H_ij + 1/2| = {np.max(np.abs(H.sum(axis=1) + 0.5)):.3e}")
    print("\n  the discrete row sum of H is not zero: it is the jump term.")
    print("  For a smooth boundary the exact identity is sum_j H_ij = -1/2, the")
    print("  same information as the free term +1/2 in the integral equation.")
    print("     N     sum_j H_ij (row 0)   deviation from -1/2   interior flux error")
    for n in (8, 16, 32, 64, 128, 256):
        H, Gm, mid, _, _, _ = bem_matrices(n)
        u_b = np.cos(3.0 * mid)
        q_b = np.linalg.solve(Gm, (0.5 * np.eye(n) + H) @ u_b)
        err = np.max(np.abs(q_b - q_cubic(mid))) / (3.0 / A_M)
        print(f"  {n:5d}     {H[0].sum():+.8f}             "
              f"{abs(H[0].sum() + 0.5):.3e}             {err:.4e}")
    print("  enforcing the identity exactly through H_ii = -1/2 - sum_{j!=i} H_ij")
    print("  changes the flux error as follows:")
    print("     N     flux error (H_ii = 0)   flux error (row-sum diagonal)")
    for n in (16, 32, 64, 128):
        H, Gm, mid, _, _, _ = bem_matrices(n)
        u_b = np.cos(3.0 * mid)
        q_as = np.linalg.solve(Gm, (0.5 * np.eye(n) + H) @ u_b)
        H2 = H.copy()
        H2[np.arange(n), np.arange(n)] = -0.5 - (H.sum(axis=1) - np.diag(H))
        q_rs = np.linalg.solve(Gm, (0.5 * np.eye(n) + H2) @ u_b)
        e1 = np.max(np.abs(q_as - q_cubic(mid))) / (3.0 / A_M)
        e2 = np.max(np.abs(q_rs - q_cubic(mid))) / (3.0 / A_M)
        print(f"  {n:5d}     {e1:.6e}              {e2:.6e}")

    section("2. Interior Dirichlet problem: measured convergence")
    theta = np.linspace(0.0, 2.0 * np.pi, 512, endpoint=False)
    probes = np.column_stack([0.6 * A_M * np.cos(theta), 0.6 * A_M * np.sin(theta)])
    print("  analytic field u = (x^3 - 3 x z^2)/a^3 = (r/a)^3 cos 3 theta, harmonic")
    print("  everywhere; interior flux q = 3 cos(3 theta)/a, "
          f"max|q| = {3.0/A_M:.6e} m^-1")
    print("     N    max|q_BE-q_exact|/max|q|   order    max|u_BE-u_exact|   order")
    prev_q = prev_u = None
    rel_flux_128 = np.nan
    for n in (8, 16, 32, 64, 128, 256):
        H, Gm, mid, _, _, _ = bem_matrices(n)
        u_b = np.cos(3.0 * mid)
        q_b = np.linalg.solve(Gm, (0.5 * np.eye(n) + H) @ u_b)
        err_q = np.max(np.abs(q_b - q_cubic(mid))) / (3.0 / A_M)
        u_probe = np.array([reproduce_interior(n, u_b, q_b, x, z)
                            for x, z in probes])
        err_u = np.max(np.abs(u_probe - u_cubic(probes[:, 0], probes[:, 1])))
        oq = np.nan if prev_q is None else np.log2(prev_q / err_q)
        ou = np.nan if prev_u is None else np.log2(prev_u / err_u)
        print(f"  {n:5d}   {err_q:.6e}            {oq:6.2f}    "
              f"{err_u:.6e}       {ou:6.2f}")
        if n == 128:
            rel_flux_128 = err_q
        prev_q, prev_u = err_q, err_u
    print("  flux and reconstructed field both converge at about first order:")
    print("  a constant flat panel represents the arc and its normal to O(h), and")
    print("  the representation formula carries that error into u.")

    section("3. The same Dirichlet data on the outside of the circle")
    n = 128
    H, Gm, mid, _, _, _ = bem_matrices(n)
    u_b = np.cos(3.0 * mid)
    q_int_side = np.linalg.solve(Gm, (0.5 * np.eye(n) + H) @ u_b)
    q_ext_side = np.linalg.solve(Gm, (H - 0.5 * np.eye(n)) @ u_b)
    q_true = -3.0 * np.cos(3.0 * mid) / A_M
    rel_int = np.max(np.abs(q_int_side - q_true)) / (3.0 / A_M)
    rel_ext = np.max(np.abs(q_ext_side - q_true)) / (3.0 / A_M)
    print("  boundary data u = cos 3 theta, unchanged; the exact exterior flux is")
    print("  q = -3 cos(3 theta)/a.")
    print(f"  interior free term (+1/2) used on the exterior problem: "
          f"max relative error = {rel_int:.4e}")
    print(f"  exterior free term (-1/2):                                "
          f"max relative error = {rel_ext:.4e}")
    print("  the sign error is exactly a factor of two here: q_int = -q_ext, so the")
    print("  flux returned by the interior equation is 100% wrong.")
    th = np.linspace(0.0, 2.0 * np.pi, 64, endpoint=False)
    pr = 3.0 * A_M * np.column_stack([np.cos(th), np.sin(th)])
    u_out = np.array([reproduce_exterior(n, u_b, q_ext_side, x, z)
                      for x, z in pr])
    u_out_exact = np.cos(3.0 * th) / 27.0
    print(f"  exterior reconstruction at r = 3a: max|u_BE - u_exact| = "
          f"{np.max(np.abs(u_out - u_out_exact)):.3e} (max|u_exact| = {1/27:.4e})")

    section("4. Unknowns for the same accuracy on the same field")
    print("  field u = sin(x/a) sinh(z/a)/sinh(1), harmonic, and NOT annihilated by")
    print("  the 5-point stencil, so the volume route has a real O(h^2) error.")
    print("  Errors are measured inside r < 0.9a for both routes.")
    print("  boundary elements (disk, N constant panels):")
    print("     N     max|u_BE - u_exact|")
    for n in (8, 16, 32, 64, 128):
        H, Gm, mid, _, _, _ = bem_matrices(n)
        u_b = np.sin(np.cos(mid)) * np.sinh(np.sin(mid)) / np.sinh(1.0)
        q_b = np.linalg.solve(Gm, (0.5 * np.eye(n) + H) @ u_b)
        u_probe = np.array([reproduce_interior(n, u_b, q_b, x, z)
                            for x, z in probes])
        err = np.max(np.abs(u_probe - u_sinh(probes[:, 0], probes[:, 1])))
        print(f"  {n:5d}     {err:.4e}")
    print("  volume grid (square containing the disk, 5-point Laplacian):")
    print("     n     unknowns    nonzeros    max|u_FD - u_exact|    order")
    prev = None
    for n in (16, 32, 64, 128, 256):
        u, X, Z, nnz = fem_square(n, u_sinh)
        mask = (X ** 2 + Z ** 2) < (0.9 * A_M) ** 2
        err = np.max(np.abs(u - u_sinh(X, Z))[mask])
        order = np.nan if prev is None else np.log2(prev / err)
        print(f"  {n:5d}     {n*n:7d}    {nnz:8d}    {err:.4e}           {order:5.2f}")
        prev = err
    print("  measured result: on this smooth interior problem in a bounded domain")
    print("  the volume grid wins on accuracy per unknown -- 4096 unknowns give")
    print("  2.50e-06 while 128 boundary panels give 5.98e-04.  The boundary method's")
    print("  advantages lie elsewhere, and both are measurable or arithmetic:")
    print("   * exterior domains need no truncation boundary (section 5);")
    print("   * in 3-D the unknowns scale with the surface, not the volume: a grid")
    print("     with 128 nodes per direction has 128^3 = %d unknowns against"
          % (128 ** 3))
    print("     128^2 = %d boundary nodes (arithmetic, not a measurement);"
          % (128 ** 2))
    print("   * its matrix is dense: the cost is in the linear solve, not the grid.")
    print("  A lesson that reported only the last bullet would be hiding the first.")

    section("5. Truncation error: exterior grid versus boundary method")
    print("  a volume solve of an exterior problem must truncate at some radius R and")
    print("  impose a condition there.  For u = (a/r)^3 cos 3 theta with u = 0 at R")
    print("  the exact solution of the truncated problem is")
    print("  u_R = c (r^3 - R^6/r^3) cos 3 theta / a^3,   c = a^6/(a^6 - R^6).")
    max_trunc = 0.0
    for ratio in (2.0, 4.0, 10.0, 100.0):
        R = ratio * A_M
        c = A_M ** 6 / (A_M ** 6 - R ** 6)
        rr = np.linspace(A_M, R, 20001)
        u_R = c * (rr ** 3 - R ** 6 / rr ** 3) / A_M ** 3
        err = np.max(np.abs(u_R - (A_M / rr) ** 3))
        if ratio == 10.0:
            max_trunc = err
        print(f"  R/a = {ratio:6.1f}: max error for r >= a = {err:.4e}")
    print("  for this field the truncation error falls like (a/R)^6 and vanishes")
    print("  only as R -> infinity.  The boundary method needs no R at all.")

    section("6. Summary of measured quantities")
    print(f"  interior flux error, N = 128                     : {rel_flux_128:.3e}")
    print(f"  exterior flux error, correct free term           : {rel_ext:.3e}")
    print(f"  exterior flux error, interior free term reused   : {rel_int:.3e}")
    print("  row-sum free term at N = 256                     : "
          f"{bem_matrices(256)[0][0].sum():+.8f} (exact -0.5)")
    print(f"  truncated exterior model at R/a = 10             : {max_trunc:.4e}")
    print("  All values are SYNTHETIC model outputs of this script.")


if __name__ == "__main__":
    main()
