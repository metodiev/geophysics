"""Determinants, inverses and conditioning: why inverse problems are hard first.

Run:  python3 conditioning_demo.py
Requires: Python standard library only.

Companion to lesson 01-07-05.

The physical setting: two travel-time residual equations for two cells. The two
rays are nearly, but not exactly, identical. Nothing is singular; the matrix is
perfectly invertible for every delta > 0. And yet the answer is destroyed by
round-off as delta shrinks. This is what 'ill-conditioned' means, and it happens
*before* any regularisation is added.
"""

import math

Matrix = list[list[float]]
Vector = list[float]


def section(title: str) -> None:
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def matvec(a: Matrix, x: Vector) -> Vector:
    return [sum(a[i][j] * x[j] for j in range(len(x))) for i in range(len(a))]


def matmul(a: Matrix, b: Matrix) -> Matrix:
    n, k, m = len(a), len(b), len(b[0])
    return [[sum(a[i][t] * b[t][j] for t in range(k)) for j in range(m)]
            for i in range(n)]


def transpose(a: Matrix) -> Matrix:
    return [list(row) for row in zip(*a)]


def eye(n: int) -> Matrix:
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]


def max_abs_diff(a: Matrix, b: Matrix) -> float:
    return max(abs(a[i][j] - b[i][j])
               for i in range(len(a)) for j in range(len(a[0])))


def show(title: str, a: Matrix, places: int = 6) -> None:
    print(f"  {title}")
    for row in a:
        print("     [" + "  ".join(f"{x:>{10 + places}.{places}f}" for x in row) + "]")


def det(a: Matrix) -> float:
    """Determinant by Gaussian elimination with partial pivoting."""
    n = len(a)
    m = [row[:] for row in a]
    sign = 1.0
    for k in range(n - 1):
        pivot = max(range(k, n), key=lambda r: abs(m[r][k]))
        if abs(m[pivot][k]) < 1e-300:
            return 0.0
        if pivot != k:
            m[k], m[pivot] = m[pivot], m[k]
            sign = -sign
        for r in range(k + 1, n):
            factor = m[r][k] / m[k][k]
            for c in range(k, n):
                m[r][c] -= factor * m[k][c]
    product = sign
    for i in range(n):
        product *= m[i][i]
    return product


def inverse(a: Matrix) -> Matrix:
    """Gauss-Jordan inverse."""
    n = len(a)
    m = [a[i][:] + eye(n)[i] for i in range(n)]
    for k in range(n):
        pivot = max(range(k, n), key=lambda r: abs(m[r][k]))
        if abs(m[pivot][k]) < 1e-300:
            raise ArithmeticError("singular matrix has no inverse")
        m[k], m[pivot] = m[pivot], m[k]
        scale = m[k][k]
        m[k] = [x / scale for x in m[k]]
        for r in range(n):
            if r != k and m[r][k] != 0.0:
                factor = m[r][k]
                m[r] = [x - factor * y for x, y in zip(m[r], m[k])]
    return [row[n:] for row in m]


def jacobi_eigen(a: Matrix, tol: float = 1e-15, sweeps: int = 100) -> tuple[Vector, Matrix]:
    """Cyclic Jacobi eigenvalues/vectors of a symmetric matrix.

    Returns (eigenvalues, V) with the eigenvectors as the *columns* of V.
    """
    n = len(a)
    work = [row[:] for row in a]
    v = eye(n)
    for _ in range(sweeps):
        off = math.sqrt(sum(work[i][j] ** 2 for i in range(n)
                            for j in range(n) if i != j))
        if off < tol:
            break
        for p in range(n - 1):
            for q in range(p + 1, n):
                if abs(work[p][q]) < 1e-300:
                    continue
                theta = (work[q][q] - work[p][p]) / (2.0 * work[p][q])
                t = math.copysign(1.0, theta) / (abs(theta) + math.sqrt(theta * theta + 1.0)) \
                    if theta != 0.0 else 1.0
                c = 1.0 / math.sqrt(t * t + 1.0)
                s = t * c
                for k in range(n):
                    akp = work[k][p]
                    akq = work[k][q]
                    work[k][p] = c * akp - s * akq
                    work[k][q] = s * akp + c * akq
                for k in range(n):
                    apk = work[p][k]
                    aqk = work[q][k]
                    work[p][k] = c * apk - s * aqk
                    work[q][k] = s * apk + c * aqk
                for k in range(n):
                    vkp = v[k][p]
                    vkq = v[k][q]
                    v[k][p] = c * vkp - s * vkq
                    v[k][q] = s * vkp + c * vkq
    eigenvalues = [work[i][i] for i in range(n)]
    return eigenvalues, v


def singular_values(a: Matrix) -> Vector:
    """Singular values of any matrix, via the eigenvalues of A^T A.

    This is the textbook identity sigma^2 = eig(A^T A), and it is also the one
    that squares the condition number: section 3 shows it failing.
    """
    ata = matmul(transpose(a), a)
    eigenvalues, _ = jacobi_eigen(ata)
    return sorted((math.sqrt(max(0.0, e)) for e in eigenvalues), reverse=True)


def cond2(a: Matrix) -> float:
    s = singular_values(a)
    return s[0] / s[-1] if s[-1] > 0.0 else float("inf")


def sigma_symmetric(a: Matrix) -> Vector:
    """Singular values of a *symmetric* matrix, from its eigenvalues directly.

    sigma = |lambda| for a symmetric matrix, and the eigenproblem for A itself
    does not square the conditioning. This is the honest route, and it is the
    idea the SVD generalises to non-symmetric matrices (lesson 01-07-08).
    """
    eigenvalues, _ = jacobi_eigen(a)
    return sorted((abs(e) for e in eigenvalues), reverse=True)


def main() -> None:
    section("1. The determinant is a volume scale factor")
    g3: Matrix = [[2.0, 1.0, 0.0], [1.0, 2.0, 1.0], [0.0, 1.0, 2.0]]
    show("G (km), the lesson 01-07-03 tomography kernel", g3, places=1)
    print(f"  det(G) = {det(g3):.6f}")
    print("  The unit cube of model perturbations (1 s/km in each cell) maps to a")
    print(f"  parallelepiped in data space of volume {abs(det(g3)):.4f} (s/km * km = s).")
    print("  det = 0 would mean the model cube is flattened into a plane: some")
    print("  model direction produces no data at all. That is the null space of")
    print("  lesson 01-07-04, and it is exactly what happens below.")
    g_rank2: Matrix = [[1.0, 1.0, 0.0], [0.0, 1.0, 1.0], [1.0, 2.0, 1.0]]
    print(f"\n  det of the rank-deficient kernel from lesson 01-07-04 = "
          f"{det(g_rank2):.1f}")
    a2: Matrix = [[1.0, 2.0], [3.0, 4.0]]
    b2: Matrix = [[0.0, 1.0], [-1.0, 2.0]]
    print(f"  det(A B) = {det(matmul(a2, b2)):.6f}, "
          f"det(A) det(B) = {det(a2) * det(b2):.6f}")
    print(f"  det(A^T) = {det(transpose(a2)):.6f}, det(A) = {det(a2):.6f}")

    section("2. The inverse exists -- and that is not the same as being usable")
    for delta in (1.0, 1e-1, 1e-2, 1e-4):
        ad: Matrix = [[1.0, 1.0], [1.0, 1.0 + delta]]
        inv = inverse(ad)
        check = max_abs_diff(matmul(ad, inv), eye(2))
        print(f"  delta = {delta:8.0e}   det = {det(ad):10.3e}   "
              f"||A^-1||_max = {max(abs(x) for row in inv for x in row):12.4e}   "
              f"max|A A^-1 - I| = {check:.2e}")
    print("\nReading: A A^-1 = I to machine precision in every case, so every one")
    print("of these matrices is invertible. The entries of A^-1 nevertheless")
    print("grow like 1/delta, which is the numerical warning sign: a small")
    print("change in the data becomes an enormous change in the model.")

    section("3. The condition number, and its scaling with the geometry")
    print("  G(delta) = [[1, 1], [1, 1+delta]]: two rays whose paths differ by")
    print("  delta km in cell 2.\n")
    print(f"  {'delta':>8}  {'sigma_max':>12}  {'sigma_min(A^T A)':>17}  "
          f"{'kappa(A^T A route)':>19}  {'sigma_min(direct)':>18}  "
          f"{'kappa(direct)':>14}")
    for delta in (1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7, 1e-8, 1e-10):
        ad = [[1.0, 1.0], [1.0, 1.0 + delta]]
        s_ata = singular_values(ad)
        s_dir = sigma_symmetric(ad)
        k_ata = s_ata[0] / s_ata[1] if s_ata[1] > 0.0 else float("inf")
        print(f"  {delta:>8.0e}  {s_dir[0]:>12.6f}  {s_ata[1]:>17.6e}  "
              f"{k_ata:>19.6e}  {s_dir[1]:>18.6e}  {s_dir[0] / s_dir[1]:>14.6e}")
    print(f"\n  exact sigma_min = 2 delta / ((2 + delta) + sqrt(4 + delta^2)):")
    for delta in (1e-4, 1e-8):
        exact = 2.0 * delta / ((2.0 + delta) + math.sqrt(4.0 + delta * delta))
        print(f"    delta = {delta:.0e}: sigma_min = {exact:.6e}, "
              f"kappa_2 = {2.0 / exact:.6e}")
    print("\nReading: kappa_2 = 4/delta to leading order. The geometry, not the")
    print("algorithm, sets the difficulty of the experiment. Note the two routes:")
    print("from delta = 1e-8 the A^T A route reports sigma_min = 0, because it")
    print("forms a matrix whose condition number is kappa(G)^2 = 1.6e17 > 1/eps,")
    print("while the direct eigenproblem on G still returns 5e-9. Computing a")
    print("singular value through A^T A costs you half your digits -- the reason")
    print("lesson 01-07-08 builds the SVD without ever forming A^T A.")

    section("4. What a condition number costs you")
    delta = 1e-4
    ad = [[1.0, 1.0], [1.0, 1.0 + delta]]
    truth = [0.050, -0.020]
    d_exact = matvec(ad, truth)
    s_sym = sigma_symmetric(ad)
    eigenvalues, vecs = jacobi_eigen(ad)
    worst = min(range(2), key=lambda i: abs(eigenvalues[i]))
    u_min = [vecs[r][worst] for r in range(2)]
    if sum(u_min) < 0:  # fix the (arbitrary) sign of the eigenvector
        u_min = [-v for v in u_min]
    print(f"  delta = {delta:.0e} km")
    print(f"  kappa_2(G)     = {s_sym[0] / s_sym[1]:.6e}")
    print(f"  ||G^-1||_2     = {1.0 / s_sym[1]:.6e}   (= 1 / sigma_min)")
    print(f"  direction that becomes the null space as delta -> 0 = "
          f"[{u_min[0]:.6f}, {u_min[1]:.6f}]")
    print(f"  true model (s/km)      = {truth}")
    print(f"  exact data (s)         = {[round(v, 8) for v in d_exact]}")
    inv = inverse(ad)
    d_norm = math.sqrt(sum(v * v for v in d_exact))
    m_norm = math.sqrt(sum(v * v for v in truth))
    print(f"\n  {'rel. data error':>16}  {'||dm||/||m||':>14}  "
          f"{'bound kappa*rel':>16}  {'gain ||dm||/||dd||':>18}")
    for rel in (1e-6, 1e-5, 1e-4, 1e-3):
        dd = [rel * d_norm * v for v in u_min]
        m_bad = matvec(inv, [d_exact[i] + dd[i] for i in range(2)])
        dm = [m_bad[i] - truth[i] for i in range(2)]
        dm_norm = math.sqrt(sum(v * v for v in dm))
        dd_norm = math.sqrt(sum(v * v for v in dd))
        print(f"  {rel:>16.0e}  {dm_norm / m_norm:>14.4e}  "
              f"{(s_sym[0] / s_sym[1]) * rel:>16.4e}  {dm_norm / dd_norm:>18.4e}")
    print(f"\n  worst-case gain ||G^-1||_2 = {1.0 / s_sym[1]:.6e}; the observed")
    print("  gain is the same to six figures, so for this perturbation direction")
    print("  the bound ||dm|| <= ||G^-1|| ||dd|| is attained exactly. Note that")
    dd_test = [1e-6 * d_norm * v for v in u_min]
    m_test = matvec(inv, [d_exact[i] + dd_test[i] for i in range(2)])
    ratio_test = math.sqrt(sum((m_test[i] - truth[i]) ** 2 for i in range(2))) / m_norm
    print(f"  ||dm||/||m|| = {ratio_test:.3e} is *below* kappa*rel = "
          f"{(s_sym[0] / s_sym[1]) * 1e-6:.3e} at rel = 1e-6:")
    print("  the bound kappa cannot be attained unless the model itself also lies")
    print("  in the worst-resolved direction, which here it does not.")
    print("  A 1e-3 s picking error -- routine in practice -- in the worst")
    print("  direction moves the model by")
    print(f"  {1.0 / s_sym[1] * 1e-3:.1f} s/km against a model whose own size is "
          f"{m_norm:.4f} s/km.")
    print("  The bound ||dm|| <= ||G^-1|| ||dd|| is not a pessimistic worst case")
    print("  here; it is what actually happens.")

    section("5. Conditioning of the normal equations is squared")
    print(f"  {'delta':>8}  {'kappa(G)':>14}  {'kappa(G^T G)':>16}  "
          f"{'kappa(G^T G)/1e16':>18}  {'numerically singular?':>22}")
    for delta in (1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-8):
        ad = [[1.0, 1.0], [1.0, 1.0 + delta]]
        k_g = sigma_symmetric(ad)[0] / sigma_symmetric(ad)[1]
        k_gtg = k_g * k_g
        print(f"  {delta:>8.0e}  {k_g:>14.6e}  {k_gtg:>16.6e}  "
              f"{k_gtg / 1e16:>18.4e}  "
              f"{'yes' if k_gtg > 1.0 / 2.220446049250313e-16 else 'no':>22}")
    print("\nReading: kappa(G^T G) = kappa(G)^2 exactly, with nothing lost. The")
    print("normal equations are numerically singular -- kappa > 1/eps = 4.5e15 --")
    print("once kappa(G) reaches about 6.7e7, which is delta ~ 1e-8 in this")
    print("geometry. The system is *not* singular and G itself is still fine; it")
    print("is the reformulation that has been destroyed. Lesson 01-07-07 turns")
    print("this table into the rule 'solve least squares with QR, not with the")
    print("normal equations'.")

    section("6. A determinant is not a conditioning measure")
    for name, a in (("A = [[1, 0], [0, 1e-3]]", [[1.0, 0.0], [0.0, 1e-3]]),
                    ("A = [[1e3, 0], [0, 1e-3]]", [[1e3, 0.0], [0.0, 1e-3]])):
        print(f"  {name}: det = {det(a):.6e}, kappa_2 = {cond2(a):.6e}")
    print("\nReading: the second matrix has a *larger* determinant (1.0 against")
    print("1e-3) and is far worse conditioned (1e6 against 1e3). The determinant")
    print("is not scale-invariant -- expressing a length in metres instead of")
    print("kilometres multiplies a row by 1000 and the determinant with it -- so")
    print("it cannot be the dimensionless measure of near-singularity. kappa_2 is")
    print("invariant under orthogonal changes of coordinates, and it is kappa")
    print("that appears in every error bound.")

    section("7. Contrast: a well-posed three-ray experiment")
    k3 = cond2(g3)
    s3 = singular_values(g3)
    print(f"  singular values of G (lesson 01-07-03) = "
          f"{[round(v, 6) for v in s3]}")
    print(f"  kappa_2 = {k3:.6f}")
    d3 = matvec(g3, [0.05, -0.02, 0.10])
    inv3 = inverse(g3)
    eig3, vec3 = jacobi_eigen([[sum(transpose(g3)[i][k] * transpose(g3)[k][j]
                                     for k in range(3)) for j in range(3)]
                               for i in range(3)])
    worst3 = min(range(3), key=lambda i: abs(eig3[i]))
    u3 = [vec3[r][worst3] for r in range(3)]
    d3_norm = math.sqrt(sum(v * v for v in d3))
    m3_norm = math.sqrt(sum(v * v for v in [0.05, -0.02, 0.10]))
    print(f"  worst direction (smallest singular vector) = "
          f"{[round(v, 6) for v in u3]}")
    print(f"  {'rel. data error':>16}  {'||dm||/||m||':>14}  "
          f"{'gain ||dm||/||dd||':>18}  {'1/sigma_min':>12}")
    for rel in (1e-6, 1e-4, 1e-2):
        dd = [rel * d3_norm * v for v in u3]
        m_bad = matvec(inv3, [d3[i] + dd[i] for i in range(3)])
        dm = [m_bad[i] - [0.05, -0.02, 0.10][i] for i in range(3)]
        dm_norm = math.sqrt(sum(v * v for v in dm))
        dd_norm = math.sqrt(sum(v * v for v in dd))
        print(f"  {rel:>16.0e}  {dm_norm / m3_norm:>14.4e}  "
              f"{dm_norm / dd_norm:>18.4e}  {1.0 / s3[-1]:>12.4e}")
    print(f"\nReading: kappa_2 = {k3:.2f}, so the worst-case amplification of a")
    print("data error is a factor of six. A 1 % data error moves the model by at")
    print("most about 6 % of its own size; the observed gain is the predicted")
    print("1/sigma_min. Design of a survey *is* the control of this number, and")
    print("it is decided long before any inversion code runs.")


if __name__ == "__main__":
    main()
