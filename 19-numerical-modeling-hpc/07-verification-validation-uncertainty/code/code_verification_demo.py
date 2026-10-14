#!/usr/bin/env python3
"""Code verification by the method of manufactured solutions (MMS).

Run with the project venv:

    cd 19-numerical-modeling-hpc/07-verification-validation-uncertainty/code
    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python code_verification_demo.py

Everything here is SYNTHETIC.  The PDEs are teaching problems with chosen
manufactured solutions; no number is a measurement of the Earth.

Contents
--------
1. 1-D manufactured solution: measured order of accuracy of a 2nd-order scheme.
2. 2-D manufactured solution: same question in two dimensions.
3. A deliberately first-order stencil: what a wrong order looks like.
4. A 2% wrong source term: machine-precision residual, O(1) error.
5. Summary: what a convergence study catches and what it cannot.
"""

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


# ---------------------------------------------------------------------------
# 1-D:  -u'' = f on (0,1),  u(0) = u(1) = 0.
# Manufactured: u(x) = sin(pi x)  =>  f(x) = pi^2 sin(pi x).
# ---------------------------------------------------------------------------
def poisson_1d_fd2(n):
    """Second-order FD solution on n cells; returns h, u_num, u_exact, L2 error."""
    h = 1.0 / n
    x = np.linspace(0.0, 1.0, n + 1)
    u_ex = np.sin(np.pi * x)
    f = np.pi ** 2 * np.sin(np.pi * x)
    m = n - 1                                    # interior unknowns
    main = np.full(m, -2.0 / h ** 2)
    off = np.full(m - 1, 1.0 / h ** 2)
    A = sp.diags([off, main, off], [-1, 0, 1], format="csc")
    b = -f[1:-1]                                 # (u_{i-1}-2u_i+u_{i+1})/h^2 = -f_i
    u = np.zeros(n + 1)
    u[1:-1] = spla.spsolve(A, b)
    err = u - u_ex
    return h, u, u_ex, np.sqrt(h * np.sum(err ** 2))


# ---------------------------------------------------------------------------
# 1-D:  a u' = f on (0,1), u(0) = 0;  upwind (backward) difference, O(h).
# Manufactured: u = sin(pi x / 2)  =>  f = (pi/2) cos(pi x / 2).
# ---------------------------------------------------------------------------
def advection_1d_upwind(n):
    h = 1.0 / n
    x = np.linspace(0.0, 1.0, n + 1)
    u_ex = np.sin(0.5 * np.pi * x)
    f = 0.5 * np.pi * np.cos(0.5 * np.pi * x)
    u = np.zeros(n + 1)
    for i in range(1, n + 1):
        u[i] = u[i - 1] + h * f[i]          # (u_i - u_{i-1})/h = f_i
    return h, u, u_ex, np.sqrt(h * np.sum((u - u_ex) ** 2))


# ---------------------------------------------------------------------------
# 2-D:  Lap(u) = f on the unit square, u = 0 on the boundary.
# Manufactured: u(x,y) = sin(pi x) sin(2 pi y) => f = -5 pi^2 u.
# ---------------------------------------------------------------------------
def laplacian_2d(n, h):
    """5-point Laplacian on the (n-1)^2 interior nodes; C-order index = (ix-1)*m + (iy-1)."""
    m = n - 1
    off = np.full(m - 1, 1.0 / h ** 2)
    main = np.full(m, -2.0 / h ** 2)             # 1-D second difference: -2/h^2
    T = sp.diags([off, main, off], [-1, 0, 1], format="csc")
    I = sp.identity(m, format="csc")
    return (sp.kron(I, T) + sp.kron(T, I)).tocsc()


def poisson_2d_fd2(n, source_scale=1.0):
    h = 1.0 / n
    x = np.linspace(0.0, 1.0, n + 1)
    u_ex = np.outer(np.sin(np.pi * x), np.sin(2.0 * np.pi * x))  # u_ex[i, j] = sin(pi x_i) sin(2 pi y_j)
    f = -5.0 * np.pi ** 2 * u_ex * source_scale
    A = laplacian_2d(n, h)
    V = u_ex[1:-1, 1:-1].reshape(-1)             # same ordering: ix-major, iy-minor
    rhs = f[1:-1, 1:-1].reshape(-1)
    sol = spla.spsolve(A, rhs)
    return h, sol, V, np.sqrt(h * h * np.sum((sol - V) ** 2)), A, rhs


def order_table(rows, label):
    print(f"  {label}")
    print("     N        h          L2 error      observed order")
    prev = None
    for n, e in rows:
        p = "" if prev is None else f"{np.log(prev / e) / np.log(2.0):15.3f}"
        print(f"  {n:5d}   {1.0 / n:8.5f}   {e:13.6e}   {p}")
        prev = e


def main():
    section("1. 1-D manufactured solution: u = sin(pi x),   -u'' = pi^2 sin(pi x)")
    rows = []
    for n in (16, 32, 64, 128, 256, 512):
        h, u, u_ex, e = poisson_1d_fd2(n)
        rows.append((n, e))
    order_table(rows, "2nd-order central difference on n cells (uniform h = 1/N):")
    print("  Expected order: 2.  A code that does not converge at its design rate")
    print("  is either wrong or outside its asymptotic range.")

    section("2. 2-D manufactured solution: u = sin(pi x) sin(2 pi y)")
    rows2 = []
    for n in (16, 32, 64, 128):
        h, sol, V, e, A, rhs = poisson_2d_fd2(n)
        rows2.append((n, e))
    order_table(rows2, "5-point Laplacian, Dirichlet data, discrete L2 norm:")
    print("  Expected order: 2.  The 2-D study costs (N+1)^2 unknowns; the same")
    print("  conclusion needs 10x fewer flops in 1-D, which is why MMS studies are")
    print("  usually run in the cheapest geometry that exercises the code path.")

    section("3. A first-order upwind scheme: what a wrong ORDER looks like")
    rows3 = []
    for n in (32, 64, 128, 256, 512):
        h, u, u_ex, e = advection_1d_upwind(n)
        rows3.append((n, e))
    order_table(rows3, "backward (upwind) difference of u', local truncation O(h):")
    print(f"  The measured order is {np.log(rows3[-2][1] / rows3[-1][1]) / np.log(2.0):.3f}, not 2: the scheme is")
    print("  genuinely first order.")
    print(f"  A single error value carries no order information: the first-order scheme")
    print(f"  at N=512 has L2 error {rows3[-1][1]:.2e}, which is close to the SECOND-order scheme's")
    print(f"  {rows[1][1]:.2e} at N=32.  Only the rate of decrease reveals the order, so a")
    print("  verification study must refine rather than report one number.")

    section("4. A 2% wrong source term: residual vs error")
    n = 128
    h, sol_bad, V_bad, e_bad, A, rhs = poisson_2d_fd2(n, source_scale=1.02)
    r = A @ sol_bad - rhs                        # residual of the code's own equations
    print(f"  N = {n}, source scaled by 1.02 (a 2% coding or parameter error)")
    print(f"  || A u - f || / || f ||       = {np.linalg.norm(r) / np.linalg.norm(rhs):.3e}")
    print(f"  max |u - u_exact| / max|u|    = "
          f"{np.max(np.abs(sol_bad - V_bad)) / np.max(np.abs(V_bad)):.3e}")
    rows4 = []
    for nn in (32, 64, 128, 256):
        _, sol, V, e, _, _ = poisson_2d_fd2(nn, source_scale=1.02)
        rows4.append((nn, e))
    order_table(rows4, "the same wrong code, refined:")
    print("  The residual is at machine precision because the code solves the wrong")
    print("  equations EXACTLY.  The error converges to a non-zero constant, so the")
    print("  observed order of the wrong code is 0, not 2.  Residual = 0 is not a")
    print("  correctness test; a manufactured solution is.")

    section("5. What a convergence study catches")
    print("  test                                         catches a bug?")
    print("  -------------------------------------------  --------------")
    print("  measured order equals the design order       yes, if the rate is wrong")
    print("  error decreases monotonically with N         yes, floor implies a bug")
    print("  residual ||Au - f|| ~ 1e-14                  NO (true of any solver)")
    print(f"  single-grid error value ({rows2[-1][1]:.2e} at N=128)     NO")
    print("  sign convention, transposed loops            yes, error is O(1)")
    print("  wrong GOVERNING EQUATION                     NO - needs validation")


if __name__ == "__main__":
    main()
