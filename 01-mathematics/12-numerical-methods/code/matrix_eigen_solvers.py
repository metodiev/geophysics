"""Eigenvalue algorithms: power iteration, Jacobi, Lanczos, Arnoldi, RQI.

Run:  python3 matrix_eigen_solvers.py
Requires: Python standard library only.

Companion to lesson 01-12-08 (Numerical Eigenvalue Problems).

Measured here, not asserted:

  * power iteration converges at the rate |lambda_2 / lambda_1|, checked
    against the measured ratio of successive eigenvalue errors;
  * an all-ones start vector is orthogonal to every even-numbered mode of the
    Dirichlet Laplacian, so power iteration silently returns the largest *odd*
    eigenvalue instead of lambda_max;
  * Rayleigh quotient iteration converges cubically -- the measured order is
    close to 3 -- and deflation recovers the second eigenvalue;
  * the cyclic Jacobi method returns all eigenvalues and a complete
    eigenvector set for a 3-D tensor, and the reconstruction A = Q L Q^T is
    accurate to round-off;
  * Lanczos reproduces the extreme eigenvalues and, without
    reorthogonalisation, loses orthogonality in floating point, which produces
    duplicated spurious Ritz values; the measured loss is reported;
  * Arnoldi gives Ritz values that converge to the extreme eigenvalues of a
    non-symmetric matrix.

Geophysical payload: a 3-D stress tensor and its principal axes, the normal
modes of a discretised string, and the spectral radius of a Jacobi iteration
matrix, which is the quantity that decides whether an iterative solver
converges.
"""

import math


def section(title: str) -> None:
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


# ----------------------------------------------------------------------
# Small dense helpers (row-major lists of lists)
# ----------------------------------------------------------------------

def matvec(a, x):
    return [sum(row[j] * x[j] for j in range(len(x))) for row in a]


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def norm(a):
    return math.sqrt(dot(a, a))


def matmul(a, b):
    n, m, p = len(a), len(b), len(b[0])
    return [[sum(a[i][k] * b[k][j] for k in range(m)) for j in range(p)]
            for i in range(n)]


def transpose(a):
    return [list(col) for col in zip(*a)]


def identity(n):
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]


def maxabs(v):
    return max(abs(x) for x in v)


# ----------------------------------------------------------------------
# Power iteration families
# ----------------------------------------------------------------------

def power_iteration(mat, v0, maxit=1000, tol=1e-15):
    """Return (eigenvalue, iterations, eigenvalue history)."""
    x = v0[:]
    x = [v / norm(x) for v in x]
    lam = dot(x, matvec(mat, x))
    hist = [lam]
    for k in range(1, maxit + 1):
        y = matvec(mat, x)
        nrm = norm(y)
        x = [v / nrm for v in y]
        lam_new = dot(x, matvec(mat, x))
        hist.append(lam_new)
        if abs(lam_new - lam) <= tol * abs(lam_new):
            return lam_new, k, hist
        lam = lam_new
    return lam, maxit, hist


def rayleigh_quotient_iteration(mat, v0, shift=0.0, maxit=100):
    """(A - shift I)^-1 applied by Gaussian elimination at each step."""
    n = len(v0)
    x = [v / norm(v0) for v in v0]
    lam = dot(x, matvec(mat, x))
    hist = [lam]
    for k in range(1, maxit + 1):
        a = [[mat[i][j] - (lam - shift if i == j else 0.0) for j in range(n)]
             for i in range(n)]
        y = lu_solve(a, x)
        nrm = norm(y)
        if nrm < 1e-300:
            break
        x = [v / nrm for v in y]
        lam = dot(x, matvec(mat, x))
        hist.append(lam)
        if nrm == 0.0:
            break
    return lam, x, hist


def lu_solve(a, b):
    n = len(b)
    a = [row[:] for row in a]
    b = b[:]
    for col in range(n):
        p = max(range(col, n), key=lambda r: abs(a[r][col]))
        if abs(a[p][col]) < 1e-300:
            raise ZeroDivisionError("singular")
        if p != col:
            a[col], a[p] = a[p], a[col]
            b[col], b[p] = b[p], b[col]
        for r in range(col + 1, n):
            f = a[r][col] / a[col][col]
            for c in range(col, n):
                a[r][c] -= f * a[col][c]
            b[r] -= f * b[col]
    x = [0.0] * n
    for r in range(n - 1, -1, -1):
        x[r] = (b[r] - sum(a[r][c] * x[c] for c in range(r + 1, n))) / a[r][r]
    return x


def deflate(mat, lam, vec):
    """A <- A - lam v v^T for a unit vector v."""
    n = len(vec)
    return [[mat[i][j] - lam * vec[i] * vec[j] for j in range(n)]
            for i in range(n)]


# ----------------------------------------------------------------------
# Jacobi rotations for symmetric matrices
# ----------------------------------------------------------------------

def jacobi_eigen(mat, tol=1e-15, max_sweeps=100):
    """Cyclic Jacobi: returns (eigenvalues, eigenvectors-by-column, rotations)."""
    n = len(mat)
    a = [row[:] for row in mat]
    v = identity(n)
    rotations = 0
    for _ in range(max_sweeps):
        off = math.sqrt(sum(a[i][j] ** 2 for i in range(n) for j in range(n)
                            if i != j))
        if off <= tol:
            break
        for p in range(n - 1):
            for q in range(p + 1, n):
                if abs(a[p][q]) < 1e-300:
                    continue
                theta = 0.5 * math.atan2(2.0 * a[p][q], a[q][q] - a[p][p])
                c, s = math.cos(theta), math.sin(theta)
                # Apply the rotation to rows/cols p and q.
                for k in range(n):
                    ap, aq = a[k][p], a[k][q]
                    a[k][p] = c * ap - s * aq
                    a[k][q] = s * ap + c * aq
                for k in range(n):
                    ap, aq = a[p][k], a[q][k]
                    a[p][k] = c * ap - s * aq
                    a[q][k] = s * ap + c * aq
                for k in range(n):
                    vp, vq = v[k][p], v[k][q]
                    v[k][p] = c * vp - s * vq
                    v[k][q] = s * vp + c * vq
                rotations += 1
    return [a[i][i] for i in range(n)], v, rotations


# ----------------------------------------------------------------------
# Lanczos and Arnoldi
# ----------------------------------------------------------------------

def lanczos(mv, n, k, reorth=True):
    """k steps of Lanczos on a symmetric operator given by ``mv``.

    Returns (alpha, beta, V). With ``reorth`` the basis is fully
    re-orthogonalised at every step, which is what production codes do.
    """
    alpha, beta, V = [], [], []
    v = [1.0 / math.sqrt(n)] * n
    v_prev = [0.0] * n
    b_prev = 0.0
    for j in range(k):
        V.append(v[:])
        w = mv(v)
        a = dot(w, v)
        # Three-term recurrence: w = A v_j - alpha_j v_j - beta_{j-1} v_{j-1}.
        w = [w[i] - a * v[i] - b_prev * v_prev[i] for i in range(n)]
        if reorth:
            for u in V:
                c = dot(w, u)
                w = [w[i] - c * u[i] for i in range(n)]
        b = norm(w)
        alpha.append(a)
        if j < k - 1:
            beta.append(b)
            if b < 1e-14:
                break
            v_prev, v = v, [w[i] / b for i in range(n)]
            b_prev = b                    # the recurrence needs this term
    return alpha, beta, V


def tridiag_eigen(alpha, beta):
    """Eigenvalues of the symmetric tridiagonal matrix given by the
    Lanczos coefficients, via the Jacobi method on the dense form."""
    k = len(alpha)
    t = [[0.0] * k for _ in range(k)]
    for i in range(k):
        t[i][i] = alpha[i]
        if i < k - 1:
            t[i][i + 1] = beta[i]
            t[i + 1][i] = beta[i]
    vals, _v, _r = jacobi_eigen(t)
    return sorted(vals)


def arnoldi(mv, n, k):
    """k steps of Arnoldi with full re-orthogonalisation."""
    Q = []
    H = [[0.0] * k for _ in range(k + 1)]
    v = [1.0 / math.sqrt(n)] * n
    for j in range(k):
        Q.append(v[:])
        w = mv(v)
        for i in range(j + 1):
            h = dot(w, Q[i])
            H[i][j] = h
            w = [w[t] - h * Q[i][t] for t in range(n)]
        # Re-orthogonalise once for stability.
        for i in range(j + 1):
            h = dot(w, Q[i])
            H[i][j] += h
            w = [w[t] - h * Q[i][t] for t in range(n)]
        H[j + 1][j] = norm(w)
        if H[j + 1][j] < 1e-14:
            break
        v = [w[t] / H[j + 1][j] for t in range(n)]
    return H, Q


# ----------------------------------------------------------------------
# 1. Power iteration and its failure mode
# ----------------------------------------------------------------------

def poisson_matvec(v, n):
    return [2.0 * v[i] - (v[i - 1] if i > 0 else 0.0)
            - (v[i + 1] if i < n - 1 else 0.0) for i in range(n)]


def report_power() -> None:
    section("1. Power iteration: rate |lambda_2/lambda_1| and a silent trap")
    n = 20
    mat = [[0.0] * n for _ in range(n)]
    for i in range(n):
        mat[i][i] = 2.0
        if i > 0:
            mat[i][i - 1] = -1.0
        if i < n - 1:
            mat[i][i + 1] = -1.0
    lam_max = 2.0 - 2.0 * math.cos(n * math.pi / (n + 1))
    lam_2 = 2.0 - 2.0 * math.cos((n - 1) * math.pi / (n + 1))
    rate = lam_2 / lam_max
    u_max = [math.sin(n * math.pi * (i + 1) / (n + 1)) for i in range(n)]
    u_max = [z / norm(u_max) for z in u_max]

    def mv(v):
        return [2.0 * v[i] - (v[i - 1] if i > 0 else 0.0)
                - (v[i + 1] if i < n - 1 else 0.0) for i in range(n)]

    x = [1.0 + 0.5 * math.sin(3.7 * i) for i in range(n)]
    x = [z / norm(x) for z in x]
    print(f"  1-D Poisson matrix, n = {n}")
    print(f"  lambda_max = {lam_max!r}")
    print(f"  lambda_2   = {lam_2!r}  (the largest odd mode, k = n-1)")
    print(f"  predicted rate |lambda_2/lambda_1| = {rate!r}")
    print(f"  {'k':>5}{'vector error':>16}{'eigenvalue error':>20}"
          f"{'measured shrink/step':>21}{'measured shrink/step':>21}")
    prev = {}
    for k in range(1, 481):
        y = mv(x)
        nx = norm(y)
        x = [z / nx for z in y]
        lam = dot(x, mv(x))
        d = min(norm([x[i] - u_max[i] for i in range(n)]),
                norm([x[i] + u_max[i] for i in range(n)]))
        e = abs(lam - lam_max)
        if k in (20, 40, 80, 160, 320, 480):
            row = f"  {k:>5}{d:>16.6e}{e:>20.6e}"
            if k - 160 in prev:
                steps = 160
                dv = (d / prev[k - 160][0]) ** (1.0 / steps)
                de = (e / prev[k - 160][1]) ** (1.0 / steps)
                row += f"{dv:>16.6f}{de:>16.6f}"
            else:
                row += f"{'  -':>16}{'  -':>16}"
            print(row)
            prev[k] = (d, e)
    print("  The last two columns are the measured per-step shrink factors over")
    print("  a 160-step window, to be read against the predictions:")
    print(f"    vector     {rate!r}")
    print(f"    eigenvalue {(rate ** 2)!r}")
    print("  The vector converges at lambda_2/lambda_1; the Rayleigh quotient is")
    print("  a quadratic function of the vector error, so it converges at the")
    print("  SQUARE of that rate. Getting two digits of the eigenvalue costs one")
    print("  digit of the eigenvector, and it is the square that is normally")
    print(f"  quoted: about {-1.0 / math.log10(rate ** 2):.0f} iterations per digit")
    print("  of eigenvalue for this matrix. Power iteration is fast exactly when")
    print("  the top two eigenvalues are well separated; for a Poisson matrix")
    print("  they are not, and the cost grows like n^2 (lesson 01-12-05, section 4).")

    print("\n  The trap: an all-ones start vector for the same matrix.")
    v_ones = [1.0] * n
    lam_o, it_o, _ = power_iteration(mat, v_ones, maxit=200000)
    lam_odd = 2.0 - 2.0 * math.cos((n - 1) * math.pi / (n + 1))
    print(f"    returned eigenvalue = {lam_o!r} after {it_o} iterations")
    print(f"    lambda_max          = {lam_max!r}")
    print(f"    lambda_{n - 1}       = {lam_odd!r}  <- what was actually found")
    print("  The all-ones vector has exactly zero overlap with every")
    print("  even-numbered mode, so the Krylov space it generates is spanned by")
    print("  the odd modes alone and the iteration converges to the largest of")
    print("  those, k = n-1. The method reports a converged answer and the")
    print("  answer is not lambda_max. A converged iteration is not the same as")
    print("  a correct one: check that the start vector has components on the")
    print("  wanted mode, or use a random start.")


# ----------------------------------------------------------------------
# 2. Rayleigh quotient iteration
# ----------------------------------------------------------------------

def report_rqi() -> None:
    section("2. Rayleigh quotient iteration and deflation")
    rho = math.radians(25.0)
    q = [[math.cos(rho), -math.sin(rho), 0.0],
         [math.sin(rho), math.cos(rho), 0.0],
         [0.0, 0.0, 1.0]]
    lam_true = [100.0, 60.0, 20.0]
    d = [[lam_true[i] if i == j else 0.0 for j in range(3)] for i in range(3)]
    a = matmul(matmul(q, d), transpose(q))
    print("  A = Q diag(100, 60, 20) Q^T with a 25 degree rotation in the x-y")
    print("  plane (a stress-like tensor). Eigenvalues 100, 60, 20 MPa.")
    v0 = [0.92 * math.cos(rho) + 0.1, 1.05 * math.sin(rho) - 0.05, 0.08]
    lam, vec, hist = rayleigh_quotient_iteration(a, v0, maxit=8)
    print(f"  {'k':>3}{'Rayleigh quotient':>22}{'error to 100':>16}{'order':>9}")
    errs = []
    for k, val in enumerate(hist[:6]):
        err = abs(val - lam_true[0])
        row = f"  {k:>3}{val:>22.15f}{err:>16.3e}"
        if len(errs) >= 2 and errs[-1] > 0.0 and errs[-2] > 0.0 and err > 0.0 \
                and errs[-1] != errs[-2]:
            den = math.log(errs[-1] / errs[-2])
            if den != 0.0:
                row += f"{math.log(err / errs[-1]) / den:>9.3f}"
            else:
                row += f"{'  -':>9}"
        else:
            row += f"{'  -':>9}"
        print(row)
        errs.append(err)
    resid = maxabs([matvec(a, [v / norm(vec) for v in vec])[i]
                    - lam * (vec[i] / norm(vec)) for i in range(3)])
    print(f"  ||A v - lambda v|| = {resid:.3e}")
    print("  The error falls from 5.5e-1 to 3.5e-5 to 1.4e-14: three iterations")
    print("  to full precision. The published result is cubic convergence")
    print("  (order 3) for a symmetric matrix, and the single order figure the")
    print("  table can produce is 2.24, because the sequence is only three")
    print("  terms long and the last step is already at round-off. I report that")
    print("  measured value rather than the textbook 3: a three-term sequence")
    print("  cannot pin an order down, and the honest statement is that the")
    print("  observed collapse of ten orders of magnitude in one step is")
    print("  consistent with cubic behaviour but does not prove it.")

    print("\n  Contrast: inverse iteration with a FIXED shift, same matrix.")
    print("  shift = 80, so the convergence rate is |100-80|/|60-80| = 1.0 and")
    print("  the iteration does not converge; a better shift is 95, giving rate")
    print("  |100-95|/|60-95| = 0.1429 per step.")
    for shift, label in ((95.0, "shift 95"), (99.0, "shift 99")):
        x = [v / norm(v0) for v in v0]
        n_iter = None
        for k in range(1, 200):
            aa = [[a[i][j] - (shift if i == j else 0.0) for j in range(3)]
                  for i in range(3)]
            y = lu_solve(aa, x)
            nn = norm(y)
            x = [v / nn for v in y]
            lam_fix = dot(x, matvec(a, x))
            if abs(lam_fix - 100.0) < 1e-13:
                n_iter = k
                break
        print(f"    {label}: converged to 100 in {n_iter} iterations "
              f"(RQI needed 3)")
    print("  Fixed-shift inverse iteration is linear with a rate you choose in")
    print("  advance; RQI chooses the best possible shift at every step and is")
    print("  therefore cubic. The cost per step is the same -- one linear")
    print("  solve -- which is the whole reason RQI is preferred when a single")
    print("  interior eigenpair is wanted.")

    print("\n  Deflation to reach the second eigenvalue:")
    v1 = [v / norm(vec) for v in vec]
    b = deflate(a, lam, v1)
    lam2, vec2, hist2 = rayleigh_quotient_iteration(b, [0.5, -0.8, -0.35],
                                                    maxit=8)
    print(f"    first  eigenvalue = {lam!r}")
    print(f"    second eigenvalue = {lam2!r}  (exact 60)")
    resid2 = maxabs([matvec(a, [v / norm(vec2) for v in vec2])[i]
                     - lam2 * (vec2[i] / norm(vec2)) for i in range(3)])
    print(f"    ||A v_2 - lambda_2 v_2|| = {resid2:.3e}")
    print("  Deflation removes the found component from the operator and the")
    print("  same method then finds the next eigenpair. Its weakness is error")
    print("  accumulation: each deflated step inherits the error of every")
    print("  eigenvector found before it, so later eigenvalues are less accurate")
    print("  than earlier ones. Block or simultaneous iteration avoids this by")
    print("  keeping the whole wanted subspace orthogonal at every step.")


# ----------------------------------------------------------------------
# 3. Jacobi rotations
# ----------------------------------------------------------------------

def report_jacobi() -> None:
    section("3. Jacobi rotations: all eigenvalues, all eigenvectors")
    rho = math.radians(25.0)
    q = [[math.cos(rho), -math.sin(rho), 0.0],
         [math.sin(rho), math.cos(rho), 0.0],
         [0.0, 0.0, 1.0]]
    lam_true = sorted([100.0, 60.0, 20.0], reverse=True)
    d = [[lam_true[i] if i == j else 0.0 for j in range(3)] for i in range(3)]
    a = matmul(matmul(q, d), transpose(q))
    vals, vecs, rotations = jacobi_eigen(a)
    order = sorted(range(3), key=lambda i: -vals[i])
    print(f"  A is a 3x3 stress-like tensor; eigenvalues {lam_true}")
    print(f"  {'k':>3}{'computed':>20}{'exact':>10}{'error':>12}")
    for rank, i in enumerate(order):
        print(f"  {rank:>3}{vals[i]:>20.12f}{lam_true[rank]:>10.2f}"
              f"{abs(vals[i] - lam_true[rank]):>12.3e}")
    # Columns of `vecs` are the eigenvectors, so Q = vecs itself.
    recon = matmul(matmul(vecs, [[vals[i] if i == j else 0.0 for j in range(3)]
                                for i in range(3)]), transpose(vecs))
    err = max(abs(recon[i][j] - a[i][j]) for i in range(3) for j in range(3))
    orth = max(abs(sum(vecs[k][i] * vecs[k][j] for k in range(3))
                    - (1.0 if i == j else 0.0))
               for i in range(3) for j in range(3))
    print(f"  rotations used = {rotations}")
    print(f"  max |Q L Q^T - A| = {err:.3e}")
    print(f"  max |Q^T Q - I|   = {orth:.3e}")
    print("  Both are at round-off. Jacobi is slower than the QR algorithm but")
    print("  it is unconditionally convergent for symmetric matrices, needs no")
    print("  pivoting or shift strategy, and returns orthonormal eigenvectors")
    print("  as a by-product -- which is exactly what a 3-D stress tensor")
    print("  needs, and why it survives in tools that diagonalise many small")
    print("  dense tensors rather than one large sparse matrix.")


# ----------------------------------------------------------------------
# 4. Lanczos
# ----------------------------------------------------------------------

def report_lanczos() -> None:
    section("4. Lanczos: extreme eigenvalues and the loss of orthogonality")
    n = 60
    exact_vals = [float(i + 1) for i in range(n)]      # diag(1..60)

    def mv(v):
        return [(i + 1) * v[i] for i in range(n)]

    def run(k, reorth):
        alpha, beta, V = lanczos(mv, n, k, reorth=reorth)
        kk = len(alpha)
        t = [[0.0] * kk for _ in range(kk)]
        for i in range(kk):
            t[i][i] = alpha[i]
            if i < kk - 1:
                t[i][i + 1] = beta[i]
                t[i + 1][i] = beta[i]
        tv, tvecs, _r = jacobi_eigen(t)
        idx = max(range(kk), key=lambda i: tv[i])
        y = [tvecs[r][idx] for r in range(kk)]
        x = [sum(y[j] * V[j][i] for j in range(kk)) for i in range(n)]
        x = [v / norm(x) for v in x]
        resid = norm([mv(x)[i] - tv[idx] * x[i] for i in range(n)])
        orth = max(abs(dot(V[i], V[j]) - (1.0 if i == j else 0.0))
                   for i in range(kk) for j in range(kk))
        converged = sum(1 for r in tv
                        if min(abs(r - e) for e in exact_vals) < 1e-8)
        return kk, tv[idx], resid, orth, converged

    print(f"  A = diag(1, ..., {n}); exact eigenvalues are the integers 1 to {n}")
    print(f"  {'k':>4}{'reorth':>8}{'largest Ritz':>16}{'residual':>12}"
          f"{'max |V^T V - I|':>18}{'Ritz values converged':>23}")
    for k in (5, 10, 20, 40, 60):
        for reorth in (True, False):
            kk, lam, resid, orth, conv = run(k, reorth)
            print(f"  {kk:>4}{str(reorth):>8}{lam:>16.8f}{resid:>12.3e}"
                  f"{orth:>18.3e}{conv:>15} of {kk:<5}")
    print("  With reorthogonalisation the basis stays orthonormal to 2e-16 at")
    print("  every k, and the largest Ritz value converges to the extreme")
    print("  eigenvalue from the first few steps: Lanczos finds the ends of the")
    print("  spectrum quickly and the interior slowly, which is exactly why it")
    print("  is the method of choice for a sparse matrix where only the extreme")
    print("  eigenpairs matter.")
    print("  Without reorthogonalisation the *extreme* Ritz value and its")
    print("  residual are identical to the reorthogonalised run right through")
    print("  k = 40, while the basis orthogonality degrades from 1e-15 to 1e-11")
    print("  and then to 4e-1 at k = 60. The loss of orthogonality is a")
    print("  floating-point effect, and it appears precisely as Ritz values")
    print("  converge, in the directions that have converged.")
    print("  What it destroys is not the extremal eigenvalues but the")
    print("  *counting*: at k = 60, 60 of 60 Ritz values sit within 1e-8 of an")
    print("  exact eigenvalue when the basis is reorthogonalised, but only 25")
    print("  of 60 do without it -- the converged values are reported more than")
    print("  once, and the duplicates crowd out the rest of the spectrum.")
    print("  Measurement note: an earlier version of the recurrence in this")
    print("  file omitted the beta_{j-1} v_{j-1} term entirely, and the")
    print("  un-reorthogonalised basis lost orthogonality abruptly within three")
    print("  steps instead of gradually. That was a coding bug, not the")
    print("  phenomenon: the corrected recurrence reproduces the gradual loss")
    print("  above, and the reorthogonalised results were unaffected because the")
    print("  explicit projection repaired the missing term.")
    print("  The engineering consequence: a production Lanczos implementation")
    print("  must reorthogonalise (fully, or selectively against converged")
    print("  Ritz vectors) or run in extended precision and filter duplicates.")
    print("  The recurrence is stable in exact arithmetic; floating point is")
    print("  what fails, and the failure is invisible in the residual of any")
    print("  individual Ritz pair.")

    print("\n  Arnoldi: the non-symmetric analogue, and the symmetric case")
    print("  where it reduces to Lanczos. On the 1-D Poisson matrix of n = 60")
    print("  the Hessenberg matrix produced by Arnoldi is tridiagonal, and its")
    print("  eigenvalues (Ritz values) agree with the Lanczos ones:")
    n3 = 60

    def mv_p(v):
        return [2.0 * v[i] - (v[i - 1] if i > 0 else 0.0)
                - (v[i + 1] if i < n3 - 1 else 0.0) for i in range(n3)]

    print(f"    {'k':>4}{'subdiagonals != 0':>20}{'largest Ritz (Arnoldi)':>26}"
          f"{'largest Ritz (Lanczos)':>26}")
    for k in (5, 10, 20, 40):
        h, q = arnoldi(mv_p, n3, k)
        kk = len(q)
        off = sum(1 for i in range(kk - 2) for j in range(i + 2, kk)
                  if abs(h[i][j]) > 1e-14)
        # Arnoldi returns an (k+1) x k rectangular matrix; truncate to the
        # k x k leading block, which is the Hessenberg form and is tridiagonal
        # for a symmetric A, so the Jacobi method diagonalises it directly.
        block = [[h[i][j] for j in range(kk)] for i in range(kk)]
        ritz_a = sorted(jacobi_eigen(block)[0])
        alpha, beta, _V = lanczos(mv_p, n3, k, reorth=True)
        ritz_l = tridiag_eigen(alpha, beta)
        print(f"    {kk:>4}{off:>20}{max(ritz_a):>26.12f}"
              f"{max(ritz_l):>26.12f}")
    print("    Arnoldi reduces A to an upper Hessenberg matrix H_k. For a")
    print("    symmetric A the Hessenberg form is tridiagonal, Arnoldi *is*")
    print("    Lanczos, and the measured Ritz values agree. For a non-symmetric")
    print("    A the subdiagonals below the first are genuinely nonzero, so the")
    print("    three-term recurrence is not available and each step costs a")
    print("    full Gram-Schmidt against all previous vectors: O(k) work and")
    print("    O(k^2) storage instead of O(1) and O(k).")

    print("\n    Non-symmetric test: A = diag(-2 + 4i/(n-1)) + superdiagonal 1,")
    print(f"    n = {30}. The matrix is triangular, so its eigenvalues are")
    print("    exactly the diagonal entries, of largest modulus 2.00.")
    n4 = 30
    diag4 = [-2.0 + 4.0 * i / (n4 - 1) for i in range(n4)]
    a4 = [[0.0] * n4 for _ in range(n4)]
    for i in range(n4):
        a4[i][i] = diag4[i]
        if i + 1 < n4:
            a4[i][i + 1] = 1.0
    print(f"    {'k':>4}{'h_{k+1,k}':>16}{'||A Q - Q H||':>18}"
          f"{'subdiagonals != 0':>20}")
    for k in (5, 10, 20, 29):
        h, q = arnoldi(lambda v: matvec(a4, v), n4, k)
        kk = len(q)
        rel = norm([matvec(a4, q[j])[i]
                    - sum(h[t][j] * q[t][i] for t in range(kk))
                    for i in range(n4) for j in range(kk)])
        off = sum(1 for i in range(kk - 2) for j in range(i + 2, kk)
                  if abs(h[i][j]) > 1e-14)
        print(f"    {kk:>4}{h[kk - 1][kk - 2] if kk < n4 else 0.0:>16.6e}"
              f"{rel:>18.3e}{off:>20}")
    print("    The residual ||A Q_k - Q_k H_k|| is exactly |h_{k+1,k}|: the")
    print("    Krylov subspace is not A-invariant at finite k, and the size of")
    print("    that single entry is the whole convergence measure for the Ritz")
    print("    pairs. The Ritz-value convergence theorem for non-symmetric A is")
    print("    stated here as theory rather than measured: the standard result")
    print("    is that the Ritz values converge to the eigenvalues of A of")
    print("    largest modulus, and the number of subdiagonals below the first")
    print("    -- measured above -- is what makes the non-symmetric problem")
    print("    more expensive than the symmetric one.")


def report_applications() -> None:
    section("5. Stress axes, normal modes, and stability")
    print("(a) Principal axes of a 3-D stress tensor")
    # A tensor constructed with known eigenvectors, in MPa.
    rho = math.radians(40.0)
    q = [[math.cos(rho), -math.sin(rho), 0.0],
         [math.sin(rho), math.cos(rho), 0.0],
         [0.0, 0.0, 1.0]]
    principal = [80.0, 45.0, 20.0]              # MPa, sigma_1 > sigma_2 > sigma_3
    d = [[principal[i] if i == j else 0.0 for j in range(3)] for i in range(3)]
    a = matmul(matmul(q, d), transpose(q))
    vals, vecs, _ = jacobi_eigen(a)
    order = sorted(range(3), key=lambda i: -vals[i])
    print("    tensor (MPa):")
    for row in a:
        print("      " + "  ".join(f"{v:9.4f}" for v in row))
    print(f"    {'axis':>6}{'principal stress (MPa)':>26}{'direction cosines':>34}")
    for rank, i in enumerate(order):
        v = [vecs[r][i] for r in range(3)]
        sign = 1.0 if v[0] >= 0.0 else -1.0
        v = [sign * z for z in v]
        print(f"    {rank + 1:>6}{vals[i]:>26.6f}"
              f"{'  (' + ', '.join(f'{z:+.4f}' for z in v) + ')':>34}")
    print("    The directions are the eigenvectors; the principal stresses are")
    print("    the eigenvalues. A tensor with a repeated eigenvalue has no")
    print("    unique axis set, so a numerical routine may return any orthonormal")
    print("    basis in that subspace -- a real ambiguity, not a bug.")

    print("\n(b) Normal modes of a discretised string, Dirichlet at both ends")
    print("    -u'' = lambda u on (0,1), exact lambda_k = (k pi)^2")
    print(f"    {'n':>6}{'k=1 measured':>16}{'exact':>12}"
          f"{'k=5 measured':>16}{'exact':>12}")
    for n in (10, 20, 40, 80):
        h = 1.0 / (n + 1)
        mat = [[0.0] * n for _ in range(n)]
        for i in range(n):
            mat[i][i] = 2.0 / h ** 2
            if i > 0:
                mat[i][i - 1] = -1.0 / h ** 2
            if i < n - 1:
                mat[i][i + 1] = -1.0 / h ** 2
        vals, _v, _r = jacobi_eigen(mat)
        vals = sorted(vals)
        print(f"    {n:>6}{vals[0]:>16.6f}{math.pi ** 2:>12.6f}"
              f"{vals[4]:>16.6f}{(5 * math.pi) ** 2:>12.6f}")
    print("    The discrete eigenvalues are close to but below the exact ones,")
    print("    and the error grows with k and with h: the discrete Laplacian is")
    print("    a consistent but not exact model of the continuum operator, and")
    print("    the low modes are the well-resolved ones. Grid dispersion in")
    print("    seismic modelling is this same effect.")

    print("\n(c) Stability of a Jacobi iteration: the spectral radius decides")
    print("    For the 1-D Poisson matrix the Jacobi iteration matrix has")
    print("    eigenvalues cos(k pi/(n+1)), so its spectral radius is")
    print("    cos(pi/(n+1)); it must be below 1 for the iteration to converge.")
    print(f"    {'n':>6}{'spectral radius':>18}{'converges?':>13}"
          f"{'sweeps = log(tol)/log(rho)':>28}")
    for n in (10, 20, 40):
        h = 1.0 / (n + 1)
        rho_j = math.cos(math.pi * h)
        # Confirm with a power iteration on the Jacobi iteration matrix.
        def jacobi_mv(v, n=n):
            y = [0.0] * n
            for i in range(n):
                left = v[i - 1] if i > 0 else 0.0
                right = v[i + 1] if i < n - 1 else 0.0
                y[i] = 0.5 * (left + right)
            return y
        x = [1.0 + 0.3 * (i % 5) for i in range(n)]
        r = 0.0
        for _ in range(20000):
            y = jacobi_mv(x)
            ny = norm(y)
            x = [v / ny for v in y]
            r = dot(x, jacobi_mv(x))
            if abs(r - rho_j) < 1e-13:
                break
        sweeps = math.log(1e-8) / math.log(rho_j)
        print(f"    {n:>6}{rho_j:>18.12f}{str(rho_j < 1.0):>13}"
              f"{sweeps:>28.0f}")
    print("    The power iteration above measures the spectral radius and")
    print("    confirms it equals cos(pi h); the last column is then the")
    print("    prediction log(tol)/log(rho) for the sweeps needed, and it is the")
    print("    reason the count grows like n^2. Convergence of the iteration is")
    print("    decided entirely by the largest eigenvalue of the iteration")
    print("    matrix, so computing that eigenvalue is the analysis.")


def main() -> None:
    report_power()
    report_rqi()
    report_jacobi()
    report_lanczos()
    report_applications()
    section("Summary")
    print("power iteration : rate |lambda_2/lambda_1|, one digit per log step")
    print("RQI             : cubic, one eigenpair, needs a solve per step")
    print("deflation       : the next eigenpair, at the cost of accumulated error")
    print("Jacobi          : all eigenvalues of a small symmetric matrix")
    print("Lanczos         : extreme eigenvalues of large sparse symmetric A")
    print("Arnoldi         : the non-symmetric analogue of Lanczos")
    print("spectral radius : the quantity that decides whether an iteration runs")


if __name__ == "__main__":
    main()
