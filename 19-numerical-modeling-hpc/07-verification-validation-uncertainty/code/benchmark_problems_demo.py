#!/usr/bin/env python3
"""Benchmark problems and method comparison: what a benchmark must specify,
and why two codes agreeing is not verification.

Run with the project venv:

    cd 19-numerical-modeling-hpc/07-verification-validation-uncertainty/code
    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python benchmark_problems_demo.py

All models and data here are SYNTHETIC teaching problems.  The analytic
solutions are exact solutions of the stated equations.

Contents
--------
1. The benchmark problem and its exact solution.
2. Three methods on the same benchmark: measured orders.
3. A hidden choice both codes are free to make: the spread between them.
4. Agreement is not verification: two codes sharing one bug.
5. Applicability: a method whose boundary conditions do not fit the benchmark.
6. Cost: resolution needed for a stated tolerance.
"""

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def modes(n):
    """Fourier wavenumbers (cycles per unit length) for n periodic nodes."""
    k = np.fft.rfftfreq(n, d=1.0 / n)
    return k, 2.0 * np.pi * k                    # k and angular wavenumber


def solve_fd(n, order=2):
    """Periodic -u'' = (2 pi)^2 sin(2 pi x) solved in Fourier space.

    The circulant FD operator is diagonal in the DFT basis, so this is the exact
    solution of the discrete equations, not an iterative approximation."""
    h = 1.0 / n
    x = np.arange(n) * h
    f = (2.0 * np.pi) ** 2 * np.sin(2.0 * np.pi * x)
    k, om = modes(n)
    if order == 2:
        lam = (2.0 - 2.0 * np.cos(om * h)) / h ** 2
    else:
        lam = ((30.0 - 32.0 * np.cos(om * h) + 2.0 * np.cos(2.0 * om * h))
               / (12.0 * h ** 2))
    lam = lam.copy()
    lam[0] = 1.0                                 # gauge: set the mean mode to zero
    fh = np.fft.rfft(f)
    fh[0] = 0.0
    return x, np.fft.irfft(fh / lam, n=n)


def solve_spectral(n):
    """Same problem with exact (spectral) differentiation."""
    h = 1.0 / n
    x = np.arange(n) * h
    f = (2.0 * np.pi) ** 2 * np.sin(2.0 * np.pi * x)
    k, om = modes(n)
    lam = om ** 2
    lam = lam.copy()
    lam[0] = 1.0
    fh = np.fft.rfft(f)
    fh[0] = 0.0
    return x, np.fft.irfft(fh / lam, n=n)


def solve_dirichlet_fd2(n):
    """-u'' = pi^2 sin(pi x) on (0,1), u(0) = u(1) = 0; 2nd-order FD."""
    h = 1.0 / n
    x = np.linspace(0.0, 1.0, n + 1)
    u_ex = np.sin(np.pi * x)
    f = np.pi ** 2 * np.sin(np.pi * x)
    m = n - 1
    off = np.full(m - 1, 1.0 / h ** 2)
    main = np.full(m, -2.0 / h ** 2)
    A = sp.diags([off, main, off], [-1, 0, 1], format="csc")
    u = np.zeros(n + 1)
    u[1:-1] = spla.spsolve(A, -f[1:-1])
    return x, u, u_ex


def main():
    section("1. The benchmark problem and its exact solution")
    print("  periodic problem on [0,1):   -u'' = (2 pi)^2 sin(2 pi x)")
    print("  exact solution            :   u(x) = sin(2 pi x), mean = 0")
    print("  gauge                     :   the mean of u is fixed to 0")
    print("  error norm                :   discrete L2, ||e|| = sqrt(h sum e_i^2)")
    print("  Any benchmark that omits the gauge or the norm is not yet a benchmark.")

    section("2. Three methods on the same benchmark: measured orders")
    x_ex = None
    print("     N      FD2 error    order      FD4 error    order    spectral error")
    prev = {}
    for n in (8, 16, 32, 64, 128):
        x, u2 = solve_fd(n, 2)
        _, u4 = solve_fd(n, 4)
        _, us = solve_spectral(n)
        ex = np.sin(2.0 * np.pi * x)
        e2 = np.sqrt(np.mean((u2 - ex) ** 2))
        e4 = np.sqrt(np.mean((u4 - ex) ** 2))
        es = np.sqrt(np.mean((us - ex) ** 2))
        o2 = "" if n == 8 else f"{np.log(prev['2'] / e2) / np.log(2.0):6.2f}"
        o4 = "" if n == 8 else f"{np.log(prev['4'] / e4) / np.log(2.0):6.2f}"
        print(f"  {n:5d}   {e2:.3e}  {o2:>6}   {e4:.3e}  {o4:>6}   {es:.3e}")
        prev = {"2": e2, "4": e4}
    print("  FD2 and FD4 converge at their design orders 2 and 4.  The spectral")
    print("  method reaches round-off at N = 8 and cannot be improved: the error is")
    print("  then the accumulated round-off, not a discretisation error.")

    section("3. A hidden choice both codes are free to make")
    print("  The source may be sampled at nodes or averaged over cells; both are")
    print("  consistent discretisations of the same continuum problem.")
    print("     N      |u_nodes - u_cellavg|   FD2 error vs exact")
    for n in (8, 16, 32, 64):
        h = 1.0 / n
        x = np.arange(n) * h
        k, om = modes(n)
        lam = (2.0 - 2.0 * np.cos(om * h)) / h ** 2
        lam = lam.copy()
        lam[0] = 1.0
        f_node = (2.0 * np.pi) ** 2 * np.sin(2.0 * np.pi * x)
        xh = x + 0.5 * h
        f_cell = 0.5 * ((2.0 * np.pi) ** 2 * np.sin(2.0 * np.pi * (x - 0.5 * h))
                        + (2.0 * np.pi) ** 2 * np.sin(2.0 * np.pi * (x + 0.5 * h)))
        u1 = np.fft.irfft(np.fft.rfft(f_node - f_node.mean()) / lam, n=n)
        u2 = np.fft.irfft(np.fft.rfft(f_cell - f_cell.mean()) / lam, n=n)
        ex = np.sin(2.0 * np.pi * x)
        print(f"  {n:5d}      {np.sqrt(np.mean((u1 - u2) ** 2)):.3e}"
              f"            {np.sqrt(np.mean((u1 - ex) ** 2)):.3e}")
    print("  The spread between two defensible codes is the same order as each one's")
    print("  error.  A benchmark that does not fix the source discretisation cannot")
    print("  distinguish 'two codes disagree by O(h^2)' from 'one code is wrong'.")

    section("4. Agreement is not verification")
    n = 64
    h = 1.0 / n
    x = np.arange(n) * h
    k, om = modes(n)
    lam = (2.0 - 2.0 * np.cos(om * h)) / h ** 2
    lam = lam.copy()
    lam[0] = 1.0
    f = (2.0 * np.pi) ** 2 * np.sin(2.0 * np.pi * x)
    ex = np.sin(2.0 * np.pi * x)
    u_a = np.fft.irfft(np.fft.rfft(f) / lam, n=n)                  # correct code
    u_b = np.fft.irfft(np.fft.rfft(1.01 * f) / lam, n=n)           # 1% source error
    u_c = np.fft.irfft(np.fft.rfft(1.01 * f) / lam, n=n)           # same error, other code
    print(f"  N = {n}, source scaled by 1.01 in codes B and C")
    print(f"  ||u_B - u_C|| / ||u||          = {np.sqrt(np.mean((u_b - u_c) ** 2)) / np.sqrt(np.mean(ex ** 2)):.3e}")
    print(f"  ||u_B - u_exact|| / ||u||      = {np.sqrt(np.mean((u_b - ex) ** 2)) / np.sqrt(np.mean(ex ** 2)):.3e}")
    print(f"  ||u_A - u_exact|| / ||u||      = {np.sqrt(np.mean((u_a - ex) ** 2)) / np.sqrt(np.mean(ex ** 2)):.3e}")
    print("  Two independently written codes agree to machine precision while both")
    print("  are about 1% wrong (here the difference is exactly zero because they")
    print("  share the same discretisation).  Agreement tests the sharing of an")
    print("  assumption; only a comparison with an exact solution tests correctness.")

    section("5. Applicability: a method whose boundary conditions do not fit")
    print("  The periodic spectral solver applied to the Dirichlet problem")
    print("  -u'' = pi^2 sin(pi x), u(0) = u(1) = 0:")
    print("     N      spectral (periodic) error    FD2 (Dirichlet) error")
    for n in (16, 32, 64, 128):
        h = 1.0 / n
        x = np.arange(n) * h
        k, om = modes(n)
        lam = om ** 2
        lam = lam.copy()
        lam[0] = 1.0
        f = np.pi ** 2 * np.sin(np.pi * x)
        u_per = np.fft.irfft(np.fft.rfft(f - f.mean()) / lam, n=n)
        e_per = np.sqrt(np.mean((u_per - np.sin(np.pi * x)) ** 2))
        x_d, u_dir, u_exd = solve_dirichlet_fd2(n)
        e_dir = np.sqrt(np.mean((u_dir - u_exd) ** 2))
        print(f"  {n:5d}      {e_per:.3e}                    {e_dir:.3e}")
    print("  The periodic solution is wrong by O(1) no matter how fine the grid: it")
    print("  solves a different problem.  Convergence order is meaningless outside")
    print("  the class of problems the method was built for, and a benchmark report")
    print("  must state the boundary conditions, not only the equation.")

    section("6. Cost: resolution needed for a stated tolerance")
    print("  periodic benchmark, target accuracy on the discrete RMS error:")
    print("     tolerance     FD2 (N)   FD4 (N)   spectral (N)")
    for tol in (1e-2, 1e-4, 1e-6):
        need = {}
        for name, fn in (("2", lambda m: solve_fd(m, 2)), ("4", lambda m: solve_fd(m, 4)),
                         ("s", solve_spectral)):
            for n in (4, 8, 16, 32, 64, 128, 256, 512):
                x, u = fn(n)
                e = np.sqrt(np.mean((u - np.sin(2.0 * np.pi * x)) ** 2))
                if e < tol:
                    need[name] = n
                    break
            else:
                need[name] = None
        print(f"     {tol:.0e}      {str(need['2']):>8}   {str(need['4']):>8}   "
              f"{str(need['s']):>10}")
    print("  On a smooth periodic problem the spectral method wins outright.  That")
    print("  result is a statement about smoothness and periodicity, so it cannot be")
    print("  transferred to a rough or irregular-geometry problem without a new")
    print("  benchmark that measures the transfer.")


if __name__ == "__main__":
    main()
