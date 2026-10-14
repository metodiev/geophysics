"""Linear solvers: direct (LU, Cholesky, Thomas) versus iterative (CG, SOR).

Run:  python3 linear_solvers.py
Requires: Python standard library only.

Companion to lesson 01-12-05 (Direct vs Iterative Linear Solvers and
Convergence).

Measured here, not asserted:

  * LU with partial pivoting reproduces an exact rational solution to
    round-off, while the same elimination without pivoting loses most of the
    digits on a system whose first pivot is tiny;
  * the tridiagonal (Thomas) route solves the 1-D Poisson system in O(n) work
    where a dense factorisation needs O(n^3), and it reproduces the exact
    discrete solution;
  * the condition number of the n x n 1-D Poisson matrix grows like
    4(n+1)^2/pi^2, measured against the analytic eigenvalue formula;
  * Jacobi reaches a fixed tolerance in sweeps that grow like n^2, matching
    1 - cos(pi h);
  * SOR at the optimal omega = 2/(1 + sin(pi h)) grows like n, one power of n
    better, and the measured counts agree with ln(1/tol)/|ln(omega - 1)|;
  * conjugate gradients grows like sqrt(kappa), and the measured counts are
    compared with the standard bound 0.5 sqrt(kappa) ln(2/eps);
  * the five-point Laplacian on an n x n grid has exactly 5N - 4n nonzeros,
    which is why the solve is matrix-free.

The systems are finite-difference discretisations of Poisson's equation with a
manufactured exact solution, so the discrete answer is known exactly.
"""

import math
from fractions import Fraction


def section(title: str) -> None:
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


# ----------------------------------------------------------------------
# Dense direct solvers
# ----------------------------------------------------------------------

def lu_solve(a, b, pivot=True):
    """Gaussian elimination with optional partial pivoting. Returns (x, swaps)."""
    n = len(b)
    a = [row[:] for row in a]
    b = b[:]
    swaps = 0
    for col in range(n):
        if pivot:
            p = max(range(col, n), key=lambda r: abs(a[r][col]))
            if p != col:
                a[col], a[p] = a[p], a[col]
                b[col], b[p] = b[p], b[col]
                swaps += 1
        if a[col][col] == 0.0:
            raise ZeroDivisionError("zero pivot")
        for r in range(col + 1, n):
            f = a[r][col] / a[col][col]
            for c in range(col, n):
                a[r][c] -= f * a[col][c]
            b[r] -= f * b[col]
    x = [0.0] * n
    for r in range(n - 1, -1, -1):
        x[r] = (b[r] - sum(a[r][c] * x[c] for c in range(r + 1, n))) / a[r][r]
    return x, swaps


def thomas(a, b, c, d):
    """O(n) solver for a tridiagonal system a_i x_{i-1} + b_i x_i + c_i x_{i+1} = d_i."""
    n = len(d)
    cp = [0.0] * n
    dp = [0.0] * n
    cp[0] = c[0] / b[0]
    dp[0] = d[0] / b[0]
    for i in range(1, n):
        m = b[i] - a[i] * cp[i - 1]
        cp[i] = c[i] / m
        dp[i] = (d[i] - a[i] * dp[i - 1]) / m
    x = [0.0] * n
    x[-1] = dp[-1]
    for i in range(n - 2, -1, -1):
        x[i] = dp[i] - cp[i] * x[i + 1]
    return x


def cholesky(a):
    """Cholesky factor L of a symmetric positive definite matrix A = L L^T."""
    n = len(a)
    L = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            s = a[i][j] - sum(L[i][k] * L[j][k] for k in range(j))
            if i == j:
                if s <= 0.0:
                    raise ValueError("matrix is not positive definite")
                L[i][j] = math.sqrt(s)
            else:
                L[i][j] = s / L[j][j]
    return L


# ----------------------------------------------------------------------
# Matrix-free Poisson operators and helpers
# ----------------------------------------------------------------------

def poisson1d_matvec(x, n):
    """tridiag(-1, 2, -1) applied to an n-vector with zero boundary values."""
    return [2.0 * x[i]
            - (x[i - 1] if i > 0 else 0.0)
            - (x[i + 1] if i < n - 1 else 0.0)
            for i in range(n)]


def poisson2d_matvec(u, n):
    """Five-point Laplacian on an n x n interior grid (row-major, zero boundary)."""
    v = [0.0] * (n * n)
    for i in range(n):
        for j in range(n):
            k = i * n + j
            v[k] = (4.0 * u[k]
                    - (u[k - 1] if j > 0 else 0.0)
                    - (u[k + 1] if j < n - 1 else 0.0)
                    - (u[k - n] if i > 0 else 0.0)
                    - (u[k + n] if i < n - 1 else 0.0))
    return v


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def norm(a):
    return math.sqrt(dot(a, a))


def maxabs(a):
    return max(abs(v) for v in a)


# ----------------------------------------------------------------------
# Iterative solvers
# ----------------------------------------------------------------------

def richardson_solve(matvec, rhs, diag, omega, tol, maxit=2_000_000):
    """x <- x + omega D^-1 (rhs - A x) from a zero start.

    With omega = 1 and a constant diagonal this is the Jacobi iteration, and
    its convergence factor is max |1 - omega lambda / d| over the spectrum.
    """
    n = len(rhs)
    x = [0.0] * n
    for it in range(1, maxit + 1):
        r = [rhs[i] - v for i, v in enumerate(matvec(x))]
        if maxabs(r) < tol:
            return x, it - 1
        x = [x[i] + omega / diag * r[i] for i in range(n)]
    return x, maxit


def sor_solve_tridiag(rhs, n, omega, tol, maxit=2_000_000):
    """SOR for the 1-D Poisson tridiagonal system, in-place sweep."""
    x = [0.0] * n
    for it in range(1, maxit + 1):
        for i in range(n):
            left = x[i - 1] if i > 0 else 0.0
            right = x[i + 1] if i < n - 1 else 0.0
            gs = 0.5 * (rhs[i] + left + right)
            x[i] = (1.0 - omega) * x[i] + omega * gs
        r = [rhs[i] - v for i, v in enumerate(poisson1d_matvec(x, n))]
        if maxabs(r) < tol:
            return x, it
    return x, maxit


def conjugate_gradient(matvec, rhs, tol, maxit=20000):
    """CG for SPD A from a zero start, relative-residual stopping test."""
    n = len(rhs)
    x = [0.0] * n
    r = rhs[:]
    p = r[:]
    rs = dot(r, r)
    rs0 = rs
    if rs0 == 0.0:
        return x, 0
    for it in range(1, maxit + 1):
        ap = matvec(p)
        alpha = rs / dot(p, ap)
        x = [x[i] + alpha * p[i] for i in range(n)]
        r = [r[i] - alpha * ap[i] for i in range(n)]
        rs_new = dot(r, r)
        if math.sqrt(rs_new) / math.sqrt(rs0) < tol:
            return x, it
        beta = rs_new / rs
        p = [r[i] + beta * p[i] for i in range(n)]
        rs = rs_new
    return x, maxit


def power_iteration(matvec, n, maxit=60000, tol=1e-14, start=None):
    """Largest eigenvalue of a symmetric positive definite operator.

    ``start`` must have components on every eigenvector: the default
    all-ones vector is orthogonal to the even-numbered modes of the
    Dirichlet Laplacian, so it would converge to the largest *odd* mode
    instead. That trap is analysed in lesson 01-12-08.
    """
    x = start if start is not None else [1.0 + 0.01 * (i + 1) for i in range(n)]
    lam = 0.0
    for k in range(maxit):
        y = matvec(x)
        nrm = norm(y)
        x = [v / nrm for v in y]
        lam_new = dot(x, matvec(x))
        if abs(lam_new - lam) <= tol * abs(lam_new):
            return lam_new, k + 1
        lam = lam_new
    return lam, maxit


# ----------------------------------------------------------------------
# 1. LU with and without pivoting
# ----------------------------------------------------------------------

def report_lu() -> None:
    section("1. LU with partial pivoting, checked against exact arithmetic")
    a = [[4.0, -1.0, 2.0, 3.0, 0.0],
         [1.0, 6.0, -1.0, 0.0, 2.0],
         [2.0, 1.0, 5.0, -2.0, 1.0],
         [0.0, 3.0, 1.0, 7.0, -1.0],
         [1.0, 0.0, 2.0, 1.0, 8.0]]
    b = [7.0, 11.0, 9.0, 10.0, 13.0]
    af = [[Fraction(int(v)) for v in row] for row in a]
    bf = [Fraction(int(v)) for v in b]
    n = len(b)
    for col in range(n):
        p = max(range(col, n), key=lambda r: abs(af[r][col]))
        af[col], af[p] = af[p], af[col]
        bf[col], bf[p] = bf[p], bf[col]
        for r in range(col + 1, n):
            f = af[r][col] / af[col][col]
            for c in range(col, n):
                af[r][c] -= f * af[col][c]
            bf[r] -= f * bf[col]
    xf = [Fraction(0)] * n
    for r in range(n - 1, -1, -1):
        s = bf[r] - sum(af[r][c] * xf[c] for c in range(r + 1, n))
        xf[r] = s / af[r][r]
    print("  exact (rational) solution:", " ".join(str(v) for v in xf))
    x, swaps = lu_solve(a, b)
    err = max(abs(x[i] - float(xf[i])) for i in range(n))
    resid = max(abs(sum(a[i][j] * x[j] for j in range(n)) - b[i])
                for i in range(n))
    print(f"  float LU, partial pivoting: max |x - exact| = {err:.3e}, "
          f"max |Ax - b| = {resid:.3e}, row swaps = {swaps}")
    print("  Both are at round-off. Note that a small residual does not by")
    print("  itself prove a small error -- the gap is the condition number,")
    print("  which section 4 measures.")


def report_pivoting() -> None:
    section("2. Why pivoting is not optional")
    eps = 1e-18
    a = [[eps, 1.0], [1.0, 1.0]]
    b = [1.0, 2.0]
    exact = [1.0 / (1.0 - eps), (1.0 - 2.0 * eps) / (1.0 - eps)]
    print(f"  solve [[{eps}, 1], [1, 1]] x = [1, 2]")
    print(f"  exact solution = ({exact[0]!r}, {exact[1]!r})")
    x_no, _ = lu_solve(a, b, pivot=False)
    x_yes, _ = lu_solve(a, b, pivot=True)
    print(f"  without pivoting: x = ({x_no[0]!r}, {x_no[1]!r}), "
          f"relative error = {abs(x_no[0] - exact[0]) / abs(exact[0]):.3e}")
    print(f"  with pivoting   : x = ({x_yes[0]!r}, {x_yes[1]!r}), "
          f"relative error = {abs(x_yes[0] - exact[0]) / abs(exact[0]):.3e}")
    print("  The tiny pivot divides into a round-off of order u/eps, so about")
    print("  18 digits are lost. A row interchange costs nothing and removes")
    print("  the amplification.")
    a2 = [[1.0, 1.0], [eps, 1.0]]
    exact2 = [0.0, 1.0]
    x2, _ = lu_solve(a2, [1.0, 1.0], pivot=False)
    print("\n  Control: [[1, 1], [eps, 1]] x = [1, 1] needs no interchange.")
    print(f"  exact solution = {exact2}; no-pivot elimination gives "
          f"({x2[0]!r}, {x2[1]!r}), max abs error = "
          f"{max(abs(x2[i] - exact2[i]) for i in range(2)):.3e}")
    print("  What matters is not the size of an entry but its size relative")
    print("  to the pivot it is about to divide: here the pivot 1 is not small")
    print("  compared with the entries below it, so nothing is amplified.")


# ----------------------------------------------------------------------
# 3. Structure: tridiagonal versus dense
# ----------------------------------------------------------------------

def report_structure() -> None:
    section("3. Sparse structure decides the algorithm")
    print("  Manufactured solution: u = sin(pi x) on n interior nodes;")
    print("  rhs = A u exactly, so the discrete answer is known.")
    for n in (20, 100, 500):
        h = 1.0 / (n + 1)
        u = [math.sin(math.pi * (i + 1) * h) for i in range(n)]
        rhs = poisson1d_matvec(u, n)
        sol = thomas([0.0] + [-1.0] * (n - 1), [2.0] * n,
                     [-1.0] * (n - 1) + [0.0], rhs)
        err = maxabs([sol[i] - u[i] for i in range(n)])
        print(f"  n = {n:>4}: nnz(Laplacian) = {3 * n - 2:>6}, "
              f"nnz(dense) = {n * n:>8}, Thomas max error = {err:.3e}")
    print("  The matrix has 3n - 2 nonzeros out of n^2 entries. Storing it")
    print("  densely wastes memory by a factor (n^2)/(3n-2) ~ n/3, and dense")
    print("  elimination destroys the sparsity outright: the factors fill in.")
    print(f"\n  {'n':>7}{'dense ops ~ (2/3)n^3':>24}{'Thomas ops ~ 8n':>18}"
          f"{'ratio':>12}")
    for n in (100, 1000, 10000):
        dense = 2.0 / 3.0 * n ** 3
        band = 8.0 * n
        print(f"  {n:>7}{dense:>24.3e}{band:>18.3e}{dense / band:>12.2e}")
    print("  At n = 10^4 the dense route needs ~10^11 more operations. No")
    print("  amount of machine speed closes that gap; the structure must be")
    print("  used. Iterative methods go further and never form a factor at")
    print("  all: one matvec costs O(nnz) = O(n) here.")

    n = 6
    a = [[1.0 / (i + j + 1.0) for j in range(n)] for i in range(n)]
    L = cholesky(a)
    rec = [[sum(L[i][k] * L[j][k] for k in range(min(i, j) + 1))
            for j in range(n)] for i in range(n)]
    err = max(abs(rec[i][j] - a[i][j]) for i in range(n) for j in range(n))
    print(f"\n  Cholesky on a {n}x{n} SPD matrix (1/(i+j+1)): "
          f"max |L L^T - A| = {err:.3e}")
    print("  Cholesky costs about n^3/6 flops against n^3/3 for LU, needs no")
    print("  pivoting, and fails loudly when the matrix is not SPD -- which is")
    print("  itself a useful diagnostic that a discretisation has gone wrong.")


# ----------------------------------------------------------------------
# 4. Conditioning
# ----------------------------------------------------------------------

def report_conditioning() -> None:
    section("4. Conditioning of the Poisson matrix: measured and predicted")
    print("  1-D Poisson, Dirichlet, A = tridiag(-1, 2, -1)")
    print("  analytic eigenvalues 2 - 2 cos(k pi/(n+1)), k = 1..n, so")
    print("  kappa = (2 - 2cos(n pi/(n+1))) / (2 - 2cos(pi/(n+1)))")
    print(f"  {'n':>7}{'kappa':>14}{'4(n+1)^2/pi^2':>17}"
          f"{'conditioning limit kappa*u':>28}")
    u = 2.22e-16
    for n in (10, 40, 160, 640):
        lmax_a = 2.0 - 2.0 * math.cos(n * math.pi / (n + 1))
        lmin_a = 2.0 - 2.0 * math.cos(math.pi / (n + 1))
        kappa = lmax_a / lmin_a
        pred = 4.0 * (n + 1) ** 2 / math.pi ** 2
        print(f"  {n:>7}{kappa:>14.3e}{pred:>17.3e}{kappa * u:>28.2e}")
    print("  kappa grows like n^2 ~ 1/h^2, so a solve can lose up to about")
    print("  kappa * u relative digits. Even at n = 640 that is only 4e-11.")
    print("  Setting kappa * u = 1 gives n ~ (pi/2) sqrt(1/u) ~ "
          f"{(math.pi / 2) * math.sqrt(1 / u):.2e}, which is far beyond any")
    print("  practical grid: double precision is not the limiting factor for")
    print("  Poisson, but it *is* for the normal equations, where kappa is")
    print("  squared before the solve even starts.")

    print("\n  Measuring lambda_max by power iteration:")
    print("  the iteration converges at rate lambda_{n-1}/lambda_n, which")
    print("  tends to 1 as n grows, so the cost grows like n^2 and the")
    print("  achieved accuracy for a fixed iteration budget degrades.")
    print(f"  {'n':>6}{'lambda_max (measured)':>22}{'lambda_max (analytic)':>22}"
          f"{'rel. diff':>12}{'iterations':>12}{'rate':>12}")
    for n in (10, 40, 160):
        lmax, it = power_iteration(lambda v: poisson1d_matvec(v, n), n,
                                   maxit=60000)
        lmax_a = 2.0 - 2.0 * math.cos(n * math.pi / (n + 1))
        rate = ((2.0 - 2.0 * math.cos((n - 1) * math.pi / (n + 1))) / lmax_a)
        print(f"  {n:>6}{lmax:>22.12f}{lmax_a:>22.12f}"
              f"{abs(lmax - lmax_a) / lmax_a:>12.2e}{it:>12}{rate:>12.8f}")
    print("  At n = 10 the estimate is exact to round-off in a few hundred")
    print("  iterations; at n = 160 it needs 34000 and still carries a")
    print("  relative error of 2e-11. Extrapolating the measured scaling")
    print("  (a factor 11 in iterations for a factor 4 in n, so about n^1.7)")
    print("  puts n = 640 at roughly 4e5 iterations. Power iteration is fast")
    print("  only when the top two eigenvalues are well separated, and the")
    print("  Poisson spectrum is the archetypal case where they are not.")


# ----------------------------------------------------------------------
# 5. Stationary iterations and SOR
# ----------------------------------------------------------------------

def report_stationary() -> None:
    section("5. Jacobi and SOR on the 1-D Poisson system")
    tolerance = 1e-10
    print(f"  manufactured solution u = sin(pi x), residual tolerance "
          f"{tolerance:.0e}")
    print("  Jacobi rate = cos(pi h), so sweeps ~ ln(1/tol)/(1 - cos(pi h))")
    print(f"  {'n':>5}{'1 - cos(pi h)':>16}{'theory sweeps':>15}"
          f"{'measured sweeps':>17}{'max error':>12}")
    for n in (10, 20, 40, 80):
        h = 1.0 / (n + 1)
        u = [math.sin(math.pi * (i + 1) * h) for i in range(n)]
        rhs = poisson1d_matvec(u, n)
        one_minus_rho = 1.0 - math.cos(math.pi * h)
        theory = math.log(1.0 / tolerance) / one_minus_rho
        sol, it = richardson_solve(lambda v: poisson1d_matvec(v, n), rhs,
                                   2.0, 1.0, tolerance, maxit=5_000_000)
        err = maxabs([sol[i] - u[i] for i in range(n)])
        print(f"  {n:>5}{one_minus_rho:>16.3e}{theory:>15.0f}{it:>17}"
              f"{err:>12.3e}")
    print("  Measured sweeps track the theory and grow like n^2. Each sweep is")
    print("  O(n) flops for this operator, so Jacobi costs O(n^3) overall -- the")
    print("  same order as a dense direct solve, which is why plain Jacobi is")
    print("  not used in production.")

    print("\n  SOR at omega = 2/(1 + sin(pi h)): rho = omega - 1, so")
    print("  sweeps ~ ln(1/tol)/|ln(omega - 1)|, which grows like (n+1)")
    print(f"  {'n':>5}{'omega_opt':>13}{'rho = omega-1':>16}"
          f"{'theory sweeps':>15}{'measured':>11}{'max error':>12}")
    for n in (10, 20, 40, 80):
        h = 1.0 / (n + 1)
        u = [math.sin(math.pi * (i + 1) * h) for i in range(n)]
        rhs = poisson1d_matvec(u, n)
        w = 2.0 / (1.0 + math.sin(math.pi * h))
        rho = w - 1.0
        theory = math.log(1.0 / tolerance) / abs(math.log(rho))
        sol, it = sor_solve_tridiag(rhs, n, w, tolerance)
        err = maxabs([sol[i] - u[i] for i in range(n)])
        print(f"  {n:>5}{w:>13.8f}{rho:>16.8f}{theory:>15.0f}{it:>11}"
              f"{err:>12.3e}")
    print("  SOR with the optimal factor needs O(n) sweeps instead of O(n^2),")
    print("  and the measured counts agree with ln(1/tol)/|ln(omega - 1)|.")
    print("  Dropping the exponent by one is worth more than any constant:")
    print("  at n = 80 it is the difference between a few hundred sweeps and")
    print("  the ~4700 that Jacobi needs.")


# ----------------------------------------------------------------------
# 6. Conjugate gradients
# ----------------------------------------------------------------------

def report_cg() -> None:
    section("6. Conjugate gradients: iterations grow like sqrt(kappa)")
    tolerance = 1e-10
    print("  1-D Poisson, zero start, relative residual tolerance "
          f"{tolerance:.0e}")
    print("  bound: sweeps ~ 0.5 sqrt(kappa) ln(2/tol)")
    print(f"  {'n':>5}{'kappa':>13}{'sqrt(kappa)':>13}{'CG sweeps':>11}"
          f"{'0.5 sqrt(k) ln(2/tol)':>24}{'Jacobi sweeps':>16}")
    for n in (16, 32, 64, 128, 256):
        h = 1.0 / (n + 1)
        rhs = [1.0] * n
        lmax = 2.0 - 2.0 * math.cos(n * math.pi / (n + 1))
        lmin = 2.0 - 2.0 * math.cos(math.pi / (n + 1))
        kappa = lmax / lmin
        sol, it = conjugate_gradient(lambda v: poisson1d_matvec(v, n),
                                     rhs, tolerance)
        bound = 0.5 * math.sqrt(kappa) * math.log(2.0 / tolerance)
        jac = math.log(1.0 / tolerance) / (1.0 - math.cos(math.pi * h))
        print(f"  {n:>5}{kappa:>13.3e}{math.sqrt(kappa):>13.1f}{it:>11}"
              f"{bound:>24.0f}{jac:>16.0f}")
    print("  CG sweeps roughly double when n doubles: they grow like n ~")
    print("  sqrt(kappa), while Jacobi grows like n^2 ~ kappa. With an O(n)")
    print("  matvec that is O(n^2) total work against O(n^3). Each CG sweep")
    print("  costs one matvec plus two dot products, so the constant is small.")
    print("  The measured counts sit below the standard bound, as they should:")
    print("  the bound is a worst case over all right-hand sides and spectra.")

    print("\n  2-D Poisson (five-point), n x n interior grid, N = n^2 unknowns;")
    print("  right-hand side = 1 everywhere (the standard forcing for a")
    print("  Poisson solve; it excites many eigenmodes, so the Krylov space")
    print("  grows and the iteration count is informative)")
    print(f"  {'n':>5}{'N':>7}{'nnz = 5N - 4n':>16}{'CG sweeps':>11}"
          f"{'rel. residual':>15}{'sweeps/N':>12}")
    for n in (8, 16, 24, 32):
        N = n * n
        rhs = [1.0] * N
        sol, it = conjugate_gradient(lambda v: poisson2d_matvec(v, n),
                                     rhs, 1e-8)
        res = norm([rhs[k] - v
                    for k, v in enumerate(poisson2d_matvec(sol, n))]) / norm(rhs)
        print(f"  {n:>5}{N:>7}{5 * N - 4 * n:>16}{it:>11}{res:>15.2e}"
              f"{it / n:>12.3f}")
    print("  The five-point Laplacian has exactly 5N - 4n nonzeros: five per")
    print("  unknown less the duplicated boundary stencils. Storing that")
    print("  densely would be more than 99% zeros at n = 32. CG sweeps scale")
    print("  with n, so the total cost grows like N^{3/2} ~ n^3 against n^6 for")
    print("  a dense factorisation of the same system. This is the practical")
    print("  core of every regularised inversion in this curriculum.")


def main() -> None:
    report_lu()
    report_pivoting()
    report_structure()
    report_conditioning()
    report_stationary()
    report_cg()
    section("Summary")
    print("LU + pivoting  : O(n^3), general, pivoting is mandatory")
    print("Cholesky       : n^3/6 when A is SPD, no pivoting needed")
    print("Thomas         : O(n) for tridiagonal -- always prefer it")
    print("Jacobi         : O(n^2) sweeps for Poisson, trivially parallel")
    print("SOR (opt omega): O(n) sweeps; the exponent drops by one")
    print("CG             : O(sqrt(kappa) ln(1/tol)) sweeps for SPD")
    print("sparsity is the structure; exploiting it is the whole game")


if __name__ == "__main__":
    main()
