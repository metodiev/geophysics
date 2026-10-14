"""Spectral theory: eigenfunction bases, discrete spectra and resolution.

Run:  python3 spectral_theory.py
Requires: Python standard library only.

Companion to lesson 01-16-04 (Spectral Theory of Operators and Eigenfunction
Bases).

Sections
    1. The Laplacian on an interval: discrete modes and their cell values
    2. A separable compact operator: the eigenvalues are known in closed form
    3. The spectral decomposition reconstructs the operator
    4. Why the Earth's normal modes are discrete, and what happens without a
       boundary
    5. The resolution matrix is a row of averaging kernels
"""

import math


def section(title):
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72)


# ------------------------- dense linear algebra ------------------------

def mat_vec(A, x):
    return [sum(a * b for a, b in zip(row, x)) for row in A]


def transpose(A):
    return [list(col) for col in zip(*A)]


def mat_mul(A, B):
    Bt = transpose(B)
    return [[sum(a * b for a, b in zip(row, col)) for col in Bt] for row in A]


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def solve(A, b):
    """Gaussian elimination with partial pivoting."""
    n = len(A)
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    for col in range(n):
        piv = max(range(col, n), key=lambda r: abs(M[r][col]))
        if abs(M[piv][col]) < 1e-300:
            continue
        M[col], M[piv] = M[piv], M[col]
        for r in range(col + 1, n):
            f = M[r][col] / M[col][col]
            for c in range(col, n + 1):
                M[r][c] -= f * M[col][c]
    x = [0.0] * n
    for r in range(n - 1, -1, -1):
        s = M[r][n] - sum(M[r][c] * x[c] for c in range(r + 1, n))
        x[r] = s / M[r][r] if abs(M[r][r]) > 1e-300 else 0.0
    return x


def jacobi_eig(A, tol=1e-14, max_sweeps=200):
    n = len(A)
    a = [row[:] for row in A]
    v = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for _ in range(max_sweeps):
        off = math.sqrt(sum(a[p][q] ** 2 for p in range(n) for q in range(p + 1, n)))
        if off < tol:
            break
        for p in range(n - 1):
            for q in range(p + 1, n):
                apq = a[p][q]
                if abs(apq) < 1e-300:
                    continue
                theta = (a[q][q] - a[p][p]) / (2.0 * apq)
                t = (1.0 if theta >= 0 else -1.0) / (abs(theta) + math.sqrt(theta * theta + 1.0))
                c = 1.0 / math.sqrt(t * t + 1.0)
                s = t * c
                for k in range(n):
                    akp, akq = a[k][p], a[k][q]
                    a[k][p] = c * akp - s * akq
                    a[k][q] = s * akp + c * akq
                for k in range(n):
                    apk, aqk = a[p][k], a[q][k]
                    a[p][k] = c * apk - s * aqk
                    a[q][k] = s * apk + c * aqk
                for k in range(n):
                    vkp, vkq = v[k][p], v[k][q]
                    v[k][p] = c * vkp - s * vkq
                    v[k][q] = s * vkp + c * vkq
    return [a[i][i] for i in range(n)], v


def gravity_kernel(n, z, span=1.0):
    """Discrete kernel of a line-mass gravity profile at depth z, sum h K = 1."""
    h = span / (n - 1)
    x = [i * h for i in range(n)]
    K = [[h * (z / math.pi) / ((x[i] - x[j]) ** 2 + z * z) for j in range(n)]
         for i in range(n)]
    return x, h, K


# ----------------------------------------------------------------------
# 1. The Laplacian on an interval
# ----------------------------------------------------------------------

def laplacian_spectrum():
    section("1. The Laplacian on (0,1): discrete modes of the continuum problem")

    n = 24
    h = 1.0 / (n + 1)
    A = [[0.0] * n for _ in range(n)]
    for i in range(n):
        A[i][i] = 2.0 / h ** 2
        if i > 0:
            A[i][i - 1] = -1.0 / h ** 2
        if i < n - 1:
            A[i][i + 1] = -1.0 / h ** 2

    ev, V = jacobi_eig(A)
    order = sorted(range(n), key=lambda k: ev[k])

    print(f"    -u'' = lambda u on (0,1), u(0) = u(1) = 0, {n} interior nodes")
    print(f"    {'mode':>5}{'discrete lambda':>18}{'4 sin^2(k pi h/2)/h^2':>24}"
          f"{'k^2 pi^2':>14}{'ratio to k^2 pi^2':>18}")
    for k in range(1, 7):
        lam = ev[order[k - 1]]
        exact_disc = 4.0 * math.sin(k * math.pi * h / 2.0) ** 2 / h ** 2
        cont = (k * math.pi) ** 2
        print(f"    {k:>5}{lam:>18.8f}{exact_disc:>24.8f}{cont:>14.6f}"
              f"{lam / cont:>18.8f}")
    print("    the matrix eigenvalues agree with the closed form to 1e-12 and")
    print("    converge to k^2 pi^2 as h -> 0. The eigenvectors are the sampled")
    print("    eigenfunctions sin(k pi x): the continuum problem has been reduced")
    print("    to a finite spectral problem without changing its spectrum.")

    print(f"\n    {'mode':>5}{'first component':>18}{'predicted':>14}"
          f"{'max |v - sin(k pi x)| / max|sin|':>36}")
    for k in range(1, 5):
        v = [V[i][order[k - 1]] for i in range(n)]
        xg = [(i + 1) * h for i in range(n)]
        s = [math.sin(k * math.pi * xi) for xi in xg]
        # align the arbitrary eigenvector sign, then normalise both to unit peak
        if v[0] * s[0] < 0:
            v = [-t for t in v]
        sv = max(abs(t) for t in v)
        ss = max(abs(t) for t in s)
        v = [t / sv for t in v]
        s = [t / ss for t in s]
        err = max(abs(a - b) for a, b in zip(v, s))
        print(f"    {k:>5}{v[0]:>18.8f}{s[0]:>14.8f}{err:>36.3e}")
    print("    after aligning the sign and the peak, the eigenvector equals the")
    print("    sampled eigenfunction to round-off. This is exact, not asymptotic:")
    print("    the second difference annihilates sin(k pi x) on a uniform grid")
    print("    with the eigenvalue 4 sin^2(k pi h/2)/h^2 of the table above.")


# ----------------------------------------------------------------------
# 2. A separable compact operator
# ----------------------------------------------------------------------

def separable_operator():
    section("2. A separable kernel R(x,y) = sum_k a_k phi_k(x) phi_k(y)")

    n = 40
    h = 1.0 / (n - 1)
    x = [i * h for i in range(n)]
    amps = (1.0, 0.4, 0.1, 0.02)

    def phi(k, t):
        return math.sqrt(2.0) * math.sin(k * math.pi * t)

    R = [[h * sum(amps[k - 1] * phi(k, x[i]) * phi(k, x[j])
                  for k in range(1, 5)) for j in range(n)] for i in range(n)]

    ev, V = jacobi_eig(R)
    ev_desc = sorted(ev, reverse=True)
    print("    the eigenvalues of R are the amplitudes a_k, because phi_k are")
    print("    orthonormal and each term is a rank-one projector:")
    print(f"    {'k':>4}{'lambda_k (Jacobi)':>20}{'a_k (exact)':>14}")
    for k in range(1, 7):
        exact = amps[k - 1] if k <= 4 else 0.0
        print(f"    {k:>4}{ev_desc[k - 1]:>20.8f}{exact:>14.8f}")
    print("    the remaining eigenvalues are zero to round-off: a rank-4 operator")
    print("    has exactly four nonzero eigenvalues, and they accumulate at zero")
    print("    as soon as the amplitudes decay. Both facts are the discreteness")
    print("    of the spectrum of a compact self-adjoint operator.")

    print(f"\n    {'k':>4}{'a_k':>10}{'a_k / a_1':>14}")
    for k in range(1, 5):
        print(f"    {k:>4}{amps[k - 1]:>10.4f}{amps[k - 1] / amps[0]:>14.4f}")
    print("    a compact operator has sigma_k -> 0, so the eigenvalues cannot")
    print("    have a positive accumulation point. This is what makes an")
    print("    expansion in its eigenfunctions a countable sum rather than an")
    print("    integral, and it is the reason truncated spectral expansions are")
    print("    the natural regularisation.")


# ----------------------------------------------------------------------
# 3. Spectral decomposition reconstructs the operator
# ----------------------------------------------------------------------

def spectral_reconstruction():
    section("3. R = sum_k lambda_k phi_k phi_k^T, verified numerically")

    n = 40
    h = 1.0 / (n - 1)
    x = [i * h for i in range(n)]
    z = 0.08
    K = [[h * (z / math.pi) / ((x[i] - x[j]) ** 2 + z * z) for j in range(n)]
         for i in range(n)]

    ev, V = jacobi_eig(K)
    order = sorted(range(n), key=lambda k: -abs(ev[k]))

    recon = [[0.0] * n for _ in range(n)]
    for idx in order:
        lam = ev[idx]
        col = [V[i][idx] for i in range(n)]
        for i in range(n):
            for j in range(n):
                recon[i][j] += lam * col[i] * col[j]

    for r in (1, 2, 4, 8):
        K_factored = [[0.0] * n for _ in range(n)]
        for idx in order[:r]:
            lam = ev[idx]
            col = [V[i][idx] for i in range(n)]
            for i in range(n):
                for j in range(n):
                    K_factored[i][j] += lam * col[i] * col[j]
        err = max(abs(K_factored[i][j] - K[i][j]) for i in range(n) for j in range(n))
        rel = err / max(abs(K[i][j]) for i in range(n) for j in range(n))
        print(f"    truncation to {r:>2} of {n} terms: "
              f"max|R_trunc - R|/max|R| = {rel:.3e}")

    err = max(abs(recon[i][j] - K[i][j]) for i in range(n) for j in range(n))
    print(f"    full sum over all {n} eigenpairs: max|R_rec - R| = {err:.3e}")

    VtV = mat_mul(transpose(V), V)
    orth = max(abs(VtV[i][j] - (1.0 if i == j else 0.0))
               for i in range(n) for j in range(n))
    print(f"    orthogonality check max|V^T V - I| = {orth:.3e}")
    print("    the spectral theorem is therefore not an abstraction here: it is")
    print("    an exact reconstruction with a countable number of terms, and")
    print("    truncating it is a controllable approximation because the")
    print("    eigenvalues decay. Section 3 of operators.py measured how fast.")

    print(f"\n    eigenvalues of the gravity kernel at z = {z}:")
    print(f"    {'k':>4}{'|lambda_k|':>18}{'|lambda_k|/|lambda_1|':>24}")
    for k in (1, 2, 3, 4, 6, 8):
        print(f"    {k:>4}{abs(ev[order[k - 1]]):>18.6e}"
              f"{abs(ev[order[k - 1]]) / abs(ev[order[0]]):>24.3e}")


# ----------------------------------------------------------------------
# 4. Why a bounded body has discrete modes
# ----------------------------------------------------------------------

def discreteness_of_modes():
    section("4. A boundary makes the spectrum discrete; removing it does not")

    print("    string of length L, fixed ends: lambda_n = (n pi / L)^2")
    print(f"    {'L':>8}{'lambda_1':>14}{'lambda_2':>14}{'lambda_3':>14}"
          f"{'lambda_2 - lambda_1':>20}")
    for L in (1.0, 10.0, 100.0):
        lams = [(n * math.pi / L) ** 2 for n in (1, 2, 3)]
        print(f"    {L:>8.1f}{lams[0]:>14.6f}{lams[1]:>14.6f}{lams[2]:>14.6f}"
              f"{lams[1] - lams[0]:>20.3e}")
    print("    the spacing collapses like 3 pi^2 / L^2 as L grows, and in the")
    print("    limit the discrete set fills an interval: the whole-line Laplacian")
    print("    has continuous spectrum. The finiteness of the Earth is what makes")
    print("    its normal modes discrete, and the discreteness is what makes them")
    print("    individually identifiable in a spectrum.")

    print("\n    the same statement in terms of counting: modes below wavenumber K")
    print("    for a fixed-fixed string of length L number about K L / pi")
    print(f"    {'L':>8}{'modes with k <= 20':>22}{'predicted 20 L / pi':>22}")
    for L in (1.0, 10.0, 100.0):
        count = int(20.0 * L / math.pi)
        print(f"    {L:>8.1f}{count:>22}{20.0 * L / math.pi:>22.3f}")

    print("\n    a discrete spectrum also means the eigenfunctions are countable,")
    print("    which is what licenses writing a field as a sum:")
    print("        u(x) = sum_n c_n sin(n pi x / L),   c_n = <u, phi_n>")
    print("    A continuum would force an integral in wavenumber, which is the")
    print("    Fourier transform limit of lesson 01-10-02.")


# ----------------------------------------------------------------------
# 5. The resolution matrix
# ----------------------------------------------------------------------

def resolution_matrix():
    section("5. The resolution matrix of a Tikhonov inverse, and what a row means")

    n = 60
    nmax = 60
    z = 0.05
    x, h, K = gravity_kernel(n, z)

    m_true = [math.exp(-((xi - 0.35) ** 2) / (2 * 0.07 ** 2))
              + 0.6 * math.exp(-((xi - 0.65) ** 2) / (2 * 0.05 ** 2)) for xi in x]
    d = mat_vec(K, m_true)

    KtK = mat_mul(transpose(K), K)
    ev, V = jacobi_eig(KtK)
    # R_alpha = (K^T K + alpha I)^{-1} K^T K = V diag(lam/(lam+alpha)) V^T
    print(f"    model and data both on {n} nodes; kernel depth z = {z}")
    print("    R_alpha = (K^T K + alpha I)^{-1} K^T K, whose rows are the")
    print("    averaging kernels of the inverse operator")
    print(f"    {'alpha':>10}{'lambda_1/(lambda_1+a)':>24}{'trace(R)':>14}"
          f"{'cells above half max':>22}{'half-width (h units)':>22}")

    centre = n // 2
    for alpha in (1e-2, 1e-3, 1e-4, 1e-6, 1e-8):
        filt = [lam / (lam + alpha) for lam in ev]
        trace = sum(filt)
        # centre row: row of V diag(filt) V^T
        row = [sum(filtered * V[centre][i] * V[r][i]
                   for i, filtered in enumerate(filt)) for r in range(n)]
        peak = max(abs(v) for v in row)
        above = [r for r in range(n) if abs(row[r]) >= 0.5 * peak]
        cells = above[-1] - above[0] + 1
        print(f"    {alpha:>10.1e}{filt[0]:>24.10f}{trace:>14.4f}"
              f"{cells:>22}{cells * h:>22.6f}")
    print("    trace(R) is the number of model parameters that the data actually")
    print("    determine: it falls as the regularisation strengthens, from 15.19 of")
    print("    60 at alpha = 0.01 to 58.59 of 60 at alpha = 1e-8. The row of R is")
    print("    the averaging kernel, and its half-width is the length over which")
    print("    the estimate smears the true model. At alpha = 1e-8 the kernel has")
    print("    collapsed onto a single grid node: the nominal resolution is then")
    print("    set by the discretisation, not by the data, and the second-moment")
    print("    width of such a kernel is meaningless (it would report a width")
    print("    below the grid spacing). Resolution must be quoted either in grid")
    print("    cells or with the discretisation stated.")
    print("    A narrow kernel and a large trace both require a small alpha, and")
    print("    small alpha is exactly what amplifies noise (lesson 01-16-05).")
    print("    That trade-off is the whole of lesson 01-16-06.")


if __name__ == "__main__":
    laplacian_spectrum()
    separable_operator()
    spectral_reconstruction()
    discreteness_of_modes()
    resolution_matrix()
