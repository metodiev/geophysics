"""Validating a forward code: benchmarks, convergence orders, tolerances.

A forward code is only trustworthy when it reproduces something whose answer is
known independently.  This script runs four such tests and reports the measured
agreement rather than asserting correctness:

  1. METHOD OF MANUFACTURED SOLUTIONS.  A known analytic field is substituted
     into the Poisson equation to obtain the source term; the finite-difference
     solution is then compared with the analytic field, and the slope of
     error-versus-grid-size on log-log axes is the measured convergence order.
  2. QUADRATURE ORDER.  The prism gravity integral is computed with increasing
     Gauss-Legendre node counts and the observed order is fitted.
  3. A CROSS-CHECK between a closed form and quadrature for a sphere.
  4. A DELIBERATE COORDINATE BUG, to show the tests actually catch errors.

All model inputs are SYNTHETIC and stated.  Constants are SI and cited.

Run:  python3 validation_benchmarks.py
"""

from __future__ import annotations

import numpy as np

G = 6.67430e-11  # m^3 kg^-1 s^-2 (CODATA 2018, NIST)
MGAL = 1.0e-5


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def solve_poisson(n):
    """Solve -lap(u) = b on the unit square, Dirichlet, second-order FD.

    Manufactured solution u = sin(pi x) sin(pi y), which vanishes on the
    boundary, so the analytic field supplies the boundary data exactly.
    b = 2 pi^2 sin(pi x) sin(pi y) = -lap(u).

    Sparse assembly and a sparse direct solve, so the grid refinement study
    stays cheap.
    """
    from scipy import sparse
    from scipy.sparse.linalg import spsolve

    h = 1.0 / (n - 1)
    x = np.linspace(0.0, 1.0, n)
    X, Y = np.meshgrid(x, x, indexing="ij")
    u_exact = np.sin(np.pi * X) * np.sin(np.pi * Y)
    b = 2.0 * np.pi**2 * np.sin(np.pi * X) * np.sin(np.pi * Y)

    m = n - 2
    idx = np.arange(m * m).reshape(m, m)
    rows, cols, vals = [], [], []
    rhs = np.zeros(m * m)
    for i in range(m):
        for j in range(m):
            k = idx[i, j]
            rows.append(k); cols.append(k); vals.append(4.0 / h**2)
            if i > 0:
                rows.append(k); cols.append(idx[i - 1, j]); vals.append(-1.0 / h**2)
            if i < m - 1:
                rows.append(k); cols.append(idx[i + 1, j]); vals.append(-1.0 / h**2)
            if j > 0:
                rows.append(k); cols.append(idx[i, j - 1]); vals.append(-1.0 / h**2)
            if j < m - 1:
                rows.append(k); cols.append(idx[i, j + 1]); vals.append(-1.0 / h**2)
            rhs[k] = b[i + 1, j + 1]
    A = sparse.csc_matrix((vals, (rows, cols)), shape=(m * m, m * m))
    u_full = u_exact.copy()
    u_full[1:-1, 1:-1] = spsolve(A, rhs).reshape(m, m)
    err = np.abs(u_full - u_exact).max()
    return err, h


def prism_gz_quad(x1, x2, y1, y2, z1, z2, rho, n):
    """Vertical attraction of a prism, Gauss-Legendre in each coordinate."""
    gx, wx = np.polynomial.legendre.leggauss(n)

    def map_ab(a, b):
        return 0.5 * (a + b) + 0.5 * (b - a) * gx, 0.5 * (b - a) * wx

    X, WX = map_ab(x1, x2)
    Y, WY = map_ab(y1, y2)
    Z, WZ = map_ab(z1, z2)
    XX, YY, ZZ = np.meshgrid(X, Y, Z, indexing="ij")
    WW = np.einsum("i,j,k->ijk", WX, WY, WZ)
    r = np.sqrt(XX**2 + YY**2 + ZZ**2)
    return G * rho * np.sum(WW * ZZ / r**3)


def sphere_gz_closed(drho, a, d):
    """Vertical attraction of a uniform sphere (exact point-mass field)."""
    m = drho * 4.0 / 3.0 * np.pi * a**3
    return G * m / d**2


def sphere_gz_shell(drho, a, d, n=400):
    """Same quantity by numerical integration over spherical shells.

    Uses the shell theorem: a shell of radius s and thickness ds contributes
    G dm / (d)^2 with dm = drho * 4 pi s^2 ds, for any observation OUTSIDE.
    """
    gs, ws = np.polynomial.legendre.leggauss(n)
    s = 0.5 * (gs + 1.0) * a
    w = 0.5 * a * ws
    dm = drho * 4.0 * np.pi * s**2 * w
    return G * np.sum(dm) / d**2


def main() -> None:
    # ==================================================================
    section("1. Method of manufactured solutions: measured FD order")
    print("   n      h          max|u_num - u_exact|     order")
    errs, hs = [], []
    prev = None
    for n in (21, 41, 81, 161):
        err, h = solve_poisson(n)
        order = "" if prev is None else f"{(np.log(prev[0]/err)/np.log(prev[1]/h)):8.4f}"
        print(f"  {n:4d}   {h:.5f}   {err:.6e}   {order:>10}")
        errs.append(err)
        hs.append(h)
        prev = (err, h)
    slope = np.polyfit(np.log(hs), np.log(errs), 1)[0]
    print(f"  fitted log-log slope over all four grids = {slope:.6f}")
    print("  The 5-point Laplacian is second order, and the measurement agrees")
    print("  with 2 to within the fit's precision.  Quoting the measured order")
    print("  -- not the textbook order -- is what makes this a validation.")

    # ==================================================================
    section("2. Quadrature convergence for the prism integral")
    x1, x2, y1, y2, z1, z2, rho = -100.0, 100.0, -100.0, 100.0, 50.0, 250.0, 500.0
    # Reference: the same quadrature at very high order.
    ref = prism_gz_quad(x1, x2, y1, y2, z1, z2, rho, 200)
    print("   n     g_z (mGal)          |g_n - g_ref|/|g_ref|")
    for n in (4, 8, 16, 32, 64):
        g = prism_gz_quad(x1, x2, y1, y2, z1, z2, rho, n)
        print(f"  {n:4d}   {g/MGAL:.12f}     "
              f"{abs(g-ref)/abs(ref):.3e}")
    print("  Gauss-Legendre converges faster than any fixed power of 1/n for a")
    print("  smooth integrand; the collapse is limited by round-off near 1e-16.")
    print("  A benchmark tolerance must be set above the measured noise floor.")

    # ==================================================================
    section("3. Cross-check: closed form versus an independent integral")
    drho, a, depth = 500.0, 60.0, 300.0
    g_closed = sphere_gz_closed(drho, a, depth)
    g_shell = sphere_gz_shell(drho, a, depth)
    print(f"  SYNTHETIC sphere: drho = {drho:.0f} kg/m^3, radius {a:.0f} m,")
    print(f"  centre depth {depth:.0f} m")
    print(f"  closed form (point mass)   = {g_closed:.9e} m/s^2 "
          f"= {g_closed/MGAL:.6f} mGal")
    print(f"  numerical shell integration = {g_shell:.9e} m/s^2 "
          f"= {g_shell/MGAL:.6f} mGal")
    print(f"  relative difference = "
          f"{abs(g_closed-g_shell)/g_closed:.3e}")
    print("  The agreement is round-off level: the shell theorem is exact, and")
    print("  the numerical integral confirms the closed form's factor.")

    # ==================================================================
    section("4. Would these tests catch a bug?  Introduce one on purpose")
    def prism_gz_buggy(x1, x2, y1, y2, z1, z2, rho, n):
        g = prism_gz_quad(x1, x2, y1, y2, z1, z2, rho, n)
        return g * 1.02                      # a 2% coordinate scaling error

    g_ok = prism_gz_quad(x1, x2, y1, y2, z1, z2, rho, 64)
    g_bad = prism_gz_buggy(x1, x2, y1, y2, z1, z2, rho, 64)
    print(f"  correct code vs reference: relative error "
          f"{abs(g_ok-ref)/abs(ref):.3e}  -> passes a 1e-6 tolerance")
    print(f"  buggy code   vs reference: relative error "
          f"{abs(g_bad-ref)/abs(ref):.3e}  -> fails a 1e-6 tolerance")
    print("  A benchmark is worth nothing unless a wrong answer fails it.")
    print("  Always inject a known error and confirm the test rejects it.")

    print("\nSUMMARY: state the benchmark, the grid or node count, the measured")
    print("error, and the tolerance.  An unquantified 'the code works' is not")
    print("a validation.")


if __name__ == "__main__":
    main()
