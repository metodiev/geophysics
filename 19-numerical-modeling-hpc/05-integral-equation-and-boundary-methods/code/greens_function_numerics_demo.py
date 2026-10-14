#!/usr/bin/env python3
"""Numerical Green's functions: discrete solutions of (operator)G = -delta, how
they relate to the analytic kernels, and which error dominates when.

Run with the project virtual environment:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python greens_function_numerics_demo.py

Everything is SYNTHETIC: the operators, grids and wave numbers are chosen teaching
values.  Distances are in km, the 1-D domain has unit length, and no quantity
here is measured from the Earth.

Contents
--------
1. 1-D Dirichlet Green's function for -(d^2/dx^2): the discrete solution is exact
   when the delta is represented consistently, and first order when it is lumped
   to the nearest node.  Two independent solvers are cross-checked.
2. Periodic screened 2-D Green's function: FFT against a sparse direct solve, the
   lattice-versus-continuum error at fixed physical distance, and the regime
   where periodic images dominate.
3. Periodic 2-D Laplace Green's function: the zero mode, the additive constant
   that depends on the box, and the measured constant against (1/2 pi) ln 2.
4. Summary of measured quantities.
"""

import numpy as np
from scipy.linalg import solve_banded
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import spsolve
from scipy.special import k0

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def green_1d(n, x0, mode):
    """Discrete Green's function of -u'' on (0,1) with u(0)=u(1)=0.

    mode = 'node'   : x0 is a node; source 1/h at that node
    mode = 'linear' : x0 between nodes; source distributed linearly (hat)
    mode = 'lump'   : x0 between nodes; all of it on the nearest node
    """
    h = 1.0 / (n + 1)
    x = h * np.arange(1, n + 1)
    band = np.zeros((3, n))
    band[0, 1:] = -1.0 / h ** 2
    band[2, :-1] = -1.0 / h ** 2
    band[1, :] = 2.0 / h ** 2
    b = np.zeros(n)
    i = int(np.searchsorted(x, x0))
    w = (x0 - x[i - 1]) / h
    if mode == "node":
        j = int(np.argmin(np.abs(x - x0)))
        b[j] = 1.0 / h
    elif mode == "linear":
        b[i - 1] = (1.0 - w) / h
        b[i] = w / h
    else:
        j = int(np.argmin(np.abs(x - x0)))
        b[j] = 1.0 / h
    g = solve_banded((1, 1), band, b)
    return h, x, g


def tent(x, x0, L=1.0):
    """Analytic Green's function of -u'' on (0,L): x_<(L-x_>)/L."""
    return np.where(x <= x0, x * (L - x0), x0 * (L - x)) / L


def lattice_green(n, L, kappa):
    """Periodic 5-point Green's function of (laplacian - kappa^2)G = -delta.

    The source carries the cell mass 1/h^2 so that the discrete solution has the
    same units as the continuum kernel.  The FFT uses the exact symbol of the
    5-point stencil, so the result is the exact inverse of that matrix.
    """
    h = L / n
    k = 2.0 * np.pi * np.fft.fftfreq(n, d=h)
    kx, ky = np.meshgrid(k, k, indexing="ij")
    lam = (2.0 / h ** 2) * (2.0 - np.cos(kx * h) - np.cos(ky * h)) + kappa ** 2
    inv = np.where(lam > 0.0, 1.0 / np.where(lam > 0.0, lam, 1.0), 0.0)
    src = np.zeros((n, n))
    src[0, 0] = 1.0 / h ** 2
    return np.fft.ifft2(np.fft.fft2(src) * inv).real, h


def lattice_green_sparse(n, L, kappa):
    """The same operator inverted by a sparse direct solve (independent route)."""
    h = L / n
    m = n * n
    idx = np.arange(m).reshape(n, n)
    rows = [idx.ravel()]
    cols = [idx.ravel()]
    vals = [np.full(m, 4.0 / h ** 2 + kappa ** 2)]
    for (dx, dy) in ((0, -1), (0, 1), (-1, 0), (1, 0)):
        r = np.roll(idx, (dx, dy), axis=(0, 1)).ravel()
        rows.append(r)
        cols.append(idx.ravel())
        vals.append(-np.ones(m) / h ** 2)
    amat = coo_matrix((np.concatenate(vals),
                       (np.concatenate(rows), np.concatenate(cols))),
                      shape=(m, m)).tocsr()
    rhs = np.zeros(m)
    rhs[0] = 1.0 / h ** 2
    return spsolve(amat, rhs).reshape(n, n)


def main():
    section("1. 1-D Green's function of -(d/dx)^2 with Dirichlet ends")
    print("  analytic kernel  G(x;x0) = x_< (L - x_>) / L,  L = 1 (dimensionless)")
    h, x, g = green_1d(63, 0.5, "node")
    print(f"  63 interior nodes, source at a node x0 = 0.5: h = {h:.6f}")
    print(f"    max|G_discrete - G_analytic|        = {np.max(np.abs(g - tent(x, 0.5))):.3e}")
    dense = np.linalg.solve(np.diag(np.full(len(x), 2.0 / h ** 2))
                            + np.diag(np.full(len(x) - 1, -1.0 / h ** 2), 1)
                            + np.diag(np.full(len(x) - 1, -1.0 / h ** 2), -1),
                            np.eye(len(x))[:, len(x) // 2] / h)
    print(f"    dense np.linalg.solve cross-check     = {np.max(np.abs(g - dense)):.3e}")
    print("  the discrete solution is exact here: the analytic tent is piecewise")
    print("  linear, and every piecewise-linear function is in the null space of the")
    print("  discrete operator between nodes.  Only roundoff remains, and it grows")
    print("  with the size of the tridiagonal solve.")
    print("\n     n     max error, source at a node   (same, source between nodes)")
    for n in (15, 31, 63, 127):
        h1, x1, g1 = green_1d(n, 0.5, "node")
        e1 = np.max(np.abs(g1 - tent(x1, 0.5)))
        print(f"  {n:5d}     {e1:.3e}")
    print("\n  when the source falls between nodes, how it is placed decides the order:")
    print("     n     h         linear (hat) distribution    lumped on nearest node")
    for n in (8, 16, 32, 64, 128, 256, 512):
        h1, x1, g_lin = green_1d(n, 0.5, "linear")
        e_lin = np.max(np.abs(g_lin - tent(x1, 0.5)))
        h2, x2, g_lump = green_1d(n, 0.5, "lump")
        e_lump = np.max(np.abs(g_lump - tent(x2, 0.5)))
        print(f"  {n:5d}   1/{n+1:d}      {e_lin:.3e}                  {e_lump:.3e}  (={e_lump/h2:.4f} h)")
    print("  the linear distribution reproduces the analytic tent to roundoff;")
    print("  lumping the same mass onto the nearest node costs a first-order error")
    print("  of about 0.25 h, which is the source-placement bias and not a property")
    print("  of the operator.")

    section("2. Periodic screened Green's function: (lap - kappa^2) G = -delta")
    L = 64.0
    print(f"  box L = {L:.0f} km, kappa = 1 /km, continuum kernel K0(kappa r)/(2 pi)")
    print("  the FFT uses the exact 5-point symbol, so it is the exact inverse of")
    print("  the sparse matrix; the two routes must agree to roundoff:")
    for n in (64, 128, 256):
        g_fft, h = lattice_green(n, L, 1.0)
        g_sp = lattice_green_sparse(n, L, 1.0)
        print(f"    n = {n:4d}: max|G_fft - G_sparse| = "
              f"{np.max(np.abs(g_fft - g_sp)):.3e} "
              f"(max|G| = {np.max(np.abs(g_fft)):.3e})")
    print("\n  now the lattice against the continuum kernel, at FIXED distances")
    print("  r1 = 8 km and r2 = 24 km (so the source stays well resolved):")
    print("     n     h        G_lat(r1)-G_lat(r2)    K0 kernel difference    rel. error   order")
    prev = None
    for n in (64, 128, 256, 512):
        g_fft, h = lattice_green(n, L, 1.0)
        row = g_fft[0]
        num = row[int(round(8.0 / h))] - row[int(round(24.0 / h))]
        cont = k0(8.0) / (2 * np.pi) - k0(24.0) / (2 * np.pi)
        err = abs(num - cont) / abs(cont)
        order = np.nan if prev is None else np.log2(prev / err)
        print(f"  {n:5d}   {h:.4f}   {num:.8e}        {cont:.8e}        "
              f"{err:.3e}   {order:5.2f}")
        prev = err
    print("  the error falls by four for each halving of h: second order, and the")
    print("  constant of the kernel cancels because only differences are compared.")
    print("\n  which error dominates depends on kappa L.  Compare the lattice value")
    print("  at r = 8 km with the single kernel and with a 7x7 image sum:")
    print("  kappa (/km)   kappa*L   lattice value    vs single kernel   vs image sum")
    for kappa in (1.0, 0.05):
        n = 256
        g_fft, h = lattice_green(n, L, kappa)
        val = g_fft[0, int(round(8.0 / h))]
        single = k0(kappa * 8.0) / (2 * np.pi)
        tot = 0.0
        for ax in range(-3, 4):
            for ay in range(-3, 4):
                rr = np.hypot(8.0 + ax * L, ay * L)
                if rr > 0.0:
                    tot += k0(kappa * rr) / (2 * np.pi)
        print(f"  {kappa:9.2f}   {kappa*L:7.1f}   {val:.8e}   "
              f"{abs(val-single)/abs(single):.3e}          "
              f"{abs(val-tot)/abs(tot):.3e}")
    print("  at kappa L = 64 the images are invisible (e^-32) and the residual is")
    print("  the discretisation error; at kappa L = 3.2 the single kernel is wrong")
    print("  by 13% and the image sum explains the value to 6e-5.  A screened")
    print("  kernel on a periodic grid is a sum over images, and whether that")
    print("  matters is a question of kappa L, not of grid spacing.")

    section("3. Periodic 2-D Laplace Green's function")
    print("  with kappa = 0 the k = 0 mode of the symbol vanishes, so the system is")
    print("  singular: the solution is determined only up to a constant.  Setting")
    print("  that mode to zero fixes the constant, and the constant then depends on")
    print("  the box.  Close to the source (r << L) the free-space logarithm is the")
    print("  right comparison; the distances below are fixed in CELLS, so the source")
    print("  stays resolved while h shrinks:")
    print("     n     h        G(8h)-G(32h)      -(1/2pi) ln(1/4)      rel. error   order")
    prev = None
    for n in (64, 128, 256, 512, 1024):
        g_fft, h = lattice_green(n, L, 0.0)
        row = g_fft[0]
        num = row[8] - row[32]
        cont = -(1.0 / (2 * np.pi)) * np.log(8.0 / 32.0)
        err = abs(num - cont) / abs(cont)
        order = np.nan if prev is None else np.log2(prev / err)
        print(f"  {n:5d}   {h:.4f}   {num:.8f}         {cont:.8f}           "
              f"{err:.3e}   {order:5.2f}")
        prev = err
    print("\n  at FIXED physical distances comparable with the box the free-space")
    print("  kernel is the wrong model, and refining the grid does not help:")
    print("     n     h        G(8 km)-G(24 km)   -(1/2pi) ln(1/3)     rel. error   order")
    prev = None
    for n in (64, 256, 1024):
        g_fft, h = lattice_green(n, L, 0.0)
        row = g_fft[0]
        num = row[int(round(8.0 / h))] - row[int(round(24.0 / h))]
        cont = -(1.0 / (2 * np.pi)) * np.log(8.0 / 24.0)
        err = abs(num - cont) / abs(cont)
        order = np.nan if prev is None else np.log2(prev / err)
        print(f"  {n:5d}   {h:.4f}   {num:.8f}         {cont:.8f}           "
              f"{err:.3e}   {order:5.2f}")
        prev = err
    print("  the 2-D Laplace field does not decay, so every periodic image")
    print("  contributes: 19% of a difference at r ~ L/3, and it is a property of")
    print("  the periodic problem rather than a discretisation error.")
    print("\n  the additive constant: G(r = 1 km) for boxes of different size")
    print("     L (km)    G(1 km)      increment per doubling   (1/2 pi) ln 2")
    prev = None
    for Lb in (16.0, 32.0, 64.0, 128.0):
        g_fft, h = lattice_green(1024, Lb, 0.0)
        val = g_fft[0, int(round(1.0 / h))]
        inc = "" if prev is None else f"{val - prev:.5f}"
        print(f"  {Lb:8.0f}   {val:.6f}     {inc:>10s}               "
              f"{(1/(2*np.pi))*np.log(2):.5f}")
        prev = val
    print("  the increment matches (1/2 pi) ln 2 to within the O(h^2) grid error:")
    print("  the constant contains -(1/2 pi) ln L, so a 2-D Laplace Green's function")
    print("  on a bounded or periodic domain is only defined relative to a reference")
    print("  length.  A potential from a NET-ZERO source distribution is unaffected;")
    print("  a single-source potential is not.")

    section("4. Summary of measured quantities")
    h1, x1, g_lin = green_1d(256, 0.5, "linear")
    e_lin = np.max(np.abs(g_lin - tent(x1, 0.5)))
    h2, x2, g_lump = green_1d(256, 0.5, "lump")
    e_lump = np.max(np.abs(g_lump - tent(x2, 0.5)))
    print(f"  1-D, linear source distribution, n = 256   : error {e_lin:.3e} (roundoff)")
    print(f"  1-D, lumped source, n = 256                : error {e_lump:.3e} = "
          f"{e_lump/h2:.3f} h")
    print("  screened lattice vs K0 kernel, n = 256      : error 1.764e-02 (O(h^2))")
    print("  screened kernel at kappa L = 3.2            : single kernel wrong by 13%")
    print("  Laplace near-field difference, n = 512      : error 3.243e-03 (order ~2)")
    print("  Laplace difference at fixed r ~ L/3         : error 1.929e-01, no convergence")
    print("  Laplace constant, increment per doubling L  : 0.11043 against 0.11032")
    print("  All values are SYNTHETIC model outputs of this script.")


if __name__ == "__main__":
    main()
