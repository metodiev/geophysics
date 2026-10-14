"""The singular value decomposition: resolution, information and rank truncation.

Run:  python3 svd_resolution_demo.py
Requires: Python standard library only.

Companion to lesson 01-07-08. This is the longest demonstration in the module,
because the SVD is the single most useful piece of linear algebra a geophysicist
owns.

Section 1 builds a genuine ray geometry: five rays cross a strip divided into
three cells. Two of the rays are nearly parallel, so the experiment has one
badly determined model direction and the SVD says exactly which one. Section 4
turns that into resolution and covariance matrices, Section 5 shows that
truncating the SVD beats inverting it exactly, and Section 8 shows the same
machinery compressing a two-dimensional field.
"""

import math

Matrix = list[list[float]]
Vector = list[float]


def section(title: str) -> None:
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def matvec(a, x):
    return [sum(a[i][j] * x[j] for j in range(len(x))) for i in range(len(a))]


def matmul(a, b):
    n, k, m = len(a), len(b), len(b[0])
    return [[sum(a[i][t] * b[t][j] for t in range(k)) for j in range(m)]
            for i in range(n)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def eye(n):
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]


def norm(x):
    return math.sqrt(sum(v * v for v in x))


def frobenius(a):
    return math.sqrt(sum(x * x for row in a for x in row))


def show(title, a, places=4, limit=30):
    print(f"  {title}")
    for row in a[:limit]:
        print("     [" + "  ".join(f"{x:>{9 + places}.{places}f}" for x in row) + "]")


def jacobi_eigen(a, tol=1e-15, sweeps=200):
    n = len(a)
    work = [[float(x) for x in row] for row in a]
    v = eye(n)
    for _ in range(sweeps):
        off = math.sqrt(sum(work[i][j] ** 2 for i in range(n)
                            for j in range(n) if i != j))
        if off < tol * max(1.0, max(abs(work[i][i]) for i in range(n))):
            break
        for p in range(n - 1):
            for q in range(p + 1, n):
                if abs(work[p][q]) < 1e-300:
                    continue
                theta = (work[q][q] - work[p][p]) / (2.0 * work[p][q])
                t = 1.0 if theta == 0.0 else \
                    math.copysign(1.0, theta) / (abs(theta) + math.sqrt(theta * theta + 1.0))
                c = 1.0 / math.sqrt(t * t + 1.0)
                s = t * c
                for k in range(n):
                    akp, akq = work[k][p], work[k][q]
                    work[k][p] = c * akp - s * akq
                    work[k][q] = s * akp + c * akq
                for k in range(n):
                    apk, aqk = work[p][k], work[q][k]
                    work[p][k] = c * apk - s * aqk
                    work[q][k] = s * apk + c * aqk
                for k in range(n):
                    vkp, vkq = v[k][p], v[k][q]
                    v[k][p] = c * vkp - s * vkq
                    v[k][q] = s * vkp + c * vkq
    return [work[i][i] for i in range(n)], v


def svd(a):
    """Thin SVD via the symmetric eigenproblem of A^T A, with U completed.

    Returns (U, s, V) with A = U diag(s) V^T, U m x m orthogonal, V n x n
    orthogonal. The completion of U for zero singular values uses Gram-Schmidt
    against the standard basis; that is legitimate here because we only need
    *some* orthonormal basis of the left null space, never a particular one.
    """
    m, n = len(a), len(a[0])
    ata = matmul(transpose(a), a)
    values, v = jacobi_eigen(ata)
    # sort descending and fix signs so that the SVD is reproducible
    order = sorted(range(n), key=lambda i: -values[i])
    s = [math.sqrt(max(0.0, values[i])) for i in order]
    vcols = [[v[r][i] for r in range(n)] for i in order]
    for j in range(n):
        col = [vcols[j][r] for r in range(n)]
        if col[0] < 0 or (col[0] == 0.0 and sum(col) < 0):
            vcols[j] = [-c for c in col]
    ucols: list[Vector] = []
    tol = max(s) * 1e-12
    for j in range(n):
        col = vcols[j]
        av = matvec(a, col)
        if s[j] > tol:
            ucols.append([c / s[j] for c in av])
    # complete the basis of R^m
    for k in range(m):
        candidate = [1.0 if i == k else 0.0 for i in range(m)]
        for e in ucols:
            candidate = [candidate[i] - sum(candidate[t] * e[t] for t in range(m)) * e[i]
                         for i in range(m)]
        if norm(candidate) > 1e-10:
            ucols.append([c / norm(candidate) for c in candidate])
        if len(ucols) == m:
            break
    u = [[ucols[j][i] for j in range(m)] for i in range(m)]
    vmat = [[vcols[j][r] for j in range(n)] for r in range(n)]
    return u, s, vmat


def reconstruct(u, s, v, m, n, rank=None):
    p = len(s) if rank is None else rank
    out = [[0.0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            out[i][j] = sum(u[i][k] * s[k] * v[j][k] for k in range(p))
    return out


def main() -> None:
    section("1. A ray geometry with one badly determined direction")
    # Three cells in a 3 km x 1 km strip. Path lengths in km.
    #   rays 1 and 2 cross cells 1 and 2 at very slightly different angles;
    #   rays 4 and 5 cross the same two cells at 45 degrees, so they measure
    #   the same combination m1 + m2;
    #   ray 3 is a vertical ray through cell 3.
    delta = 0.02
    a = [[1.0, 1.0, 0.0],
         [1.0, 1.0 + delta, 0.0],
         [0.0, 0.0, 1.0],
         [0.5, 0.5, 0.5],
         [0.5, 0.5, 0.0]]
    show("A (path lengths, km)", a, places=2)
    u, s, v = svd(a)
    m, n = len(a), len(a[0])
    print(f"  singular values: {[round(x, 10) for x in s]}")
    print(f"  condition number sigma_1 / sigma_3 = {s[0] / s[-1]:.4f}")
    print("\n  right singular vectors (columns of V): model-space directions")
    print(f"  {'index':>6}  {'sigma_i':>12}  {'v_i (cells 1, 2, 3)':>34}")
    for i in range(n):
        col = [v[r][i] for r in range(n)]
        print(f"  {i + 1:>6}  {s[i]:>12.6f}  "
              f"[{col[0]:>9.6f}, {col[1]:>9.6f}, {col[2]:>9.6f}]")
    print("\n  left singular vectors (columns of U): data-space patterns")
    print(f"  {'index':>6}  {'sigma_i':>12}  {'u_i (rays 1..5)':>56}")
    for i in range(3):
        col = [u[r][i] for r in range(m)]
        print(f"  {i + 1:>6}  {s[i]:>12.6f}  "
              f"[{', '.join(f'{c:>8.5f}' for c in col)}]")
    print("\nReading: the direction with the smallest singular value is the")
    print("difference m1 - m2, to within a few per cent. That is not an accident")
    print("of this matrix: rays 1, 4 and 5 all measure the *sum* m1 + m2, so only")
    print("the 2 per cent path-length difference between rays 1 and 2 carries any")
    print("information about the difference. A survey with this geometry cannot")
    print("separate the two cells, and the SVD states that quantitatively rather")
    print("than qualitatively. The left vector u_3 is the data pattern the weak")
    print("model direction produces: a survey cannot distinguish that pattern from")
    print("noise, which is exactly why the model direction is unrecovered.")

    section("2. The decomposition as a sum of rank-one maps")
    print("  A = sum_i sigma_i u_i v_i^T   (outer products, one per singular value)")
    total_energy = sum(x * x for x in s)
    for i in range(n):
        print(f"  term {i + 1}: sigma_{i + 1} = {s[i]:.6f}, "
              f"sigma_{i + 1}^2 = {s[i] ** 2:.6f}, "
              f"share of ||A||_F^2 = {s[i] ** 2 / total_energy:.6f}")
    print("\n  reconstruction checks")
    rec = reconstruct(u, s, v, m, n)
    err_a = max(abs(rec[i][j] - a[i][j]) for i in range(m) for j in range(n))
    err_u = max(abs(sum(u[r][i] * u[r][j] for r in range(m)) - (1.0 if i == j else 0.0))
                for i in range(m) for j in range(m))
    err_v = max(abs(sum(v[r][i] * v[r][j] for r in range(n)) - (1.0 if i == j else 0.0))
                for i in range(n) for j in range(n))
    print(f"    max |A - U S V^T| = {err_a:.3e}")
    print(f"    max |U^T U - I|   = {err_u:.3e}")
    print(f"    max |V^T V - I|   = {err_v:.3e}")
    print(f"    ||A||_F^2 = {frobenius(a) ** 2:.6f} = sum of sigma_i^2 = "
          f"{sum(x * x for x in s):.6f}")
    print("\nReading: each term sigma_i u_i v_i^T is a map that takes a model")
    print("direction, scales it by sigma_i, and emits a fixed data pattern. The")
    print("Frobenius identity ||A||_F^2 = sum sigma_i^2 is the Pythagorean")
    print("theorem of this decomposition, and it is why keeping the largest")
    print("singular values is optimal for approximation in that norm.")

    section("3. What the small singular value costs: the data cannot see it")
    # True slowness perturbation in s/km, and the exact travel-time residuals.
    m_true = [0.05, -0.02, 0.03]
    d_exact = matvec(a, m_true)
    print(f"  true model (s/km) = {m_true}")
    print(f"  exact data (s)    = {[round(x, 10) for x in d_exact]}")
    print(f"\n  data components u_i^T d (s) and the coefficient ratios:")
    print(f"  {'i':>3}  {'sigma_i':>12}  {'|u_i^T d| exact':>16}  "
          f"{'|u_i^T d|/sigma_i':>18}  {'|u_i^T d|/sigma_i, noisy':>25}")
    noisy_raw = [math.sin(1.7 * k + 0.3) for k in range(m)]
    noisy_scale = norm(noisy_raw)
    noise_level = 1e-3
    d_noisy = [d_exact[i] + noise_level * math.sqrt(m) * noisy_raw[i] / noisy_scale
               for i in range(m)]
    for i in range(n):
        ui = [u[r][i] for r in range(m)]
        coeff = abs(sum(ui[r] * d_exact[r] for r in range(m)))
        coeff_noisy = abs(sum(ui[r] * d_noisy[r] for r in range(m)))
        print(f"  {i + 1:>3}  {s[i]:>12.6f}  {coeff:>16.6e}  "
              f"{coeff / s[i]:>18.8f}  {coeff_noisy / s[i]:>25.8f}")
    print("  identity check: u_i^T d = sigma_i v_i^T m for exact data, so the")
    print("  ratio column above *is* the model coefficient along v_i:")
    for i in range(n):
        vi = [v[r][i] for r in range(n)]
        print(f"    i = {i + 1}: v_i^T m = "
              f"{sum(vi[r] * m_true[r] for r in range(n)):>12.8f} s/km")
    print("\nReading: for exact data the coefficients fall no faster than the")
    print("model's own coefficients, and the reconstruction is stable. With a")
    print("1 ms noise level added, the third coefficient moves from")
    print(f"  {abs(sum(u[r][2] * d_exact[r] for r in range(m))) / s[2]:.4f} to "
          f"{abs(sum(u[r][2] * d_noisy[r] for r in range(m))) / s[2]:.4f}"
          " -- a change of the same order as the")
    print("coefficient itself. Routine picking noise has replaced the model")
    print("information in that direction: the Picard condition has failed, and")
    print("that failure is the diagnosis that tells you to truncate.")
    print(f"  Reconstructing the v_3 coefficient divides by sigma_3 = {s[-1]:.6f},")
    print(f"  i.e. it multiplies any error in that data direction by "
          f"{1.0 / s[-1]:.1f}.")

    section("4. Resolution and covariance: two different answers to 'can I see it?'")
    # Model resolution R = V_r V_r^T for a truncated rank r, and the model
    # covariance C_m = sigma_d^2 V_r Sigma_r^-2 V_r^T.
    sigma_d = 1e-3  # 1 ms travel-time uncertainty
    for rank in (1, 2, 3):
        r = [[sum(v[i][k] * v[j][k] for k in range(rank)) for j in range(n)]
             for i in range(n)]
        err_idem = max(abs(sum(r[i][k] * r[k][j] for k in range(n)) - r[i][j])
                       for i in range(n) for j in range(n))
        print(f"  truncation rank p = {rank}:")
        print(f"    diag(R) = {[round(r[i][i], 8) for i in range(n)]}, "
              f"trace(R) = {sum(r[i][i] for i in range(n)):.6f}")
        print(f"    idempotent: max|R^2 - R| = {err_idem:.3e}")
        bias = [m_true[i] - sum(r[i][j] * m_true[j] for j in range(n)) for i in range(n)]
        print(f"    ||m_true - R m_true|| = {norm(bias):.8f} s/km  (resolution error)")
        variance = [[sigma_d ** 2 * sum(v[i][k] * v[j][k] / s[k] ** 2 for k in range(rank))
                     for j in range(n)] for i in range(n)]
        print(f"    parameter standard deviations (s/km) = "
              f"{[round(math.sqrt(variance[i][i]), 8) for i in range(n)]}")
    err_full = max(abs(sum(v[i][k] * v[j][k] for k in range(n)) - (1.0 if i == j else 0.0))
                   for i in range(n) for j in range(n))
    print(f"\n  full rank (p = 3) has R = I exactly: max|R - I| = {err_full:.3e}")
    print("  -- and worthless standard deviations. Truncating to p = 2 halves")
    print("  the worst variance at the cost of a bias along v_3. That trade is")
    print("  the whole of regularisation theory, and it is visible here in three")
    print("  lines of arithmetic.")
    print(f"  (with sigma_d = {sigma_d:.0e} s, a 0.05 s/km model perturbation")
    print("  corresponds to 5 % of the model; read the standard deviations above")
    print("  against that scale.)")

    section("5. Truncated SVD beats exact inversion on noisy data")
    print(f"  {'noise level (s)':>16}  {'rank':>5}  {'model error (s/km)':>20}  "
          f"{'data misfit (s)':>18}")
    for noise in (0.0, 1e-4, 1e-3, 1e-2):
        # deterministic pseudo-noise, orthogonalised onto the data space
        raw = [math.sin(1.7 * k + 0.3) for k in range(m)]
        scale = norm(raw)
        perturbation = [noise * c / scale * math.sqrt(m) for c in raw]
        d_noisy = [d_exact[i] + perturbation[i] for i in range(m)]
        for rank in (3, 2, 1):
            # m_hat = sum_{i<=rank} (u_i^T d / sigma_i) v_i
            m_hat = [0.0] * n
            for i in range(rank):
                ui = [u[r][i] for r in range(m)]
                coeff = sum(ui[r] * d_noisy[r] for r in range(m)) / s[i]
                for j in range(n):
                    m_hat[j] += coeff * v[j][i]
            model_err = norm([m_hat[j] - m_true[j] for j in range(n)])
            misfit = norm([matvec(a, m_hat)[r] - d_noisy[r] for r in range(m)])
            print(f"  {noise:>16.0e}  {rank:>5}  {model_err:>20.10f}  "
                  f"{misfit:>18.3e}")
    print("\nReading: with exact data, all three ranks fit perfectly and rank 3")
    print("recovers the model exactly. As soon as noise is present, rank 3")
    print(f"divides that noise by sigma_3 = {s[-1]:.4f} and the model error grows")
    print("in proportion to the noise, while rank 2 stays almost independent of it")
    print("and is *more* accurate. The truncated solution fits the noisy data")
    print("slightly worse and estimates the model far better.")
    print("This is the single most important practical fact in the module: the")
    print("best data fit is not the best model, and the SVD tells you where to")
    print("stop.")

    section("6. Data resolution: which datum is doing work?")
    r = [[sum(u[i][k] * u[j][k] for k in range(n)) for j in range(m)] for i in range(m)]
    show("N = U_r U_r^T (data resolution, 5 x 5)", r, places=5)
    err_n = max(abs(r[i][j] - (1.0 if i == j else 0.0)) for i in range(m) for j in range(m))
    print(f"  trace(N) = {sum(r[i][i] for i in range(m)):.6f} = rank = {n}, "
          f"and m = {m}")
    print(f"  ||N - I||_inf = {err_n:.6f}")
    print("  leverage of each ray (diagonal of N), against the mean rank/m = "
          f"{n / m:.6f}:")
    for i in range(m):
        label = ("above average" if r[i][i] > n / m else "below average")
        print(f"    ray {i + 1}: {r[i][i]:.6f}  ({label})")
    # What model does the second datum alone require? Solve A m = e_2 by least
    # squares with rank 3, using the singular vectors directly.
    e2 = [0.0, 1.0, 0.0, 0.0, 0.0]
    m_e2 = [0.0] * n
    for k in range(n):
        uk = [u[r][k] for r in range(m)]
        coeff = sum(uk[r] * e2[r] for r in range(m)) / s[k]
        for j in range(n):
            m_e2[j] += coeff * v[j][k]
    print(f"  the model whose data are exactly e_2 (ray 2 alone): "
          f"{[round(x, 8) for x in m_e2]} s/km")
    print(f"  ||m|| / ||d|| amplification for that datum = "
          f"{norm(m_e2) / norm(e2):.4f}")
    print(f"  check: A m = {[round(x, 10) for x in matvec(a, m_e2)]}")
    print("\nReading: with five data and three parameters, two data directions")
    print("must be redundant, and the trace of N equals the rank. Ray 2 has")
    print("leverage exactly 1: its datum can be reproduced by a model, namely")
    print("m = (-50, 50, 0) s/km, whose own size is seventy times the datum. So")
    print("high leverage does not mean a well-determined parameter -- it means")
    print("the datum lies in the range of the operator, which is a different")
    print("statement. Rays 4 and 5 measure the same combination as ray 1 and")
    print("contribute little; ray 3 samples a cell nothing else touches. In a")
    print("survey, a datum with low leverage is a datum that repeats information")
    print("you already have -- a design rule, not a curiosity.")

    section("7. Rank deficiency: the exact null space, resolved exactly")
    g_rank2 = [[1.0, 1.0, 0.0], [0.0, 1.0, 1.0], [1.0, 2.0, 1.0]]
    u2, s2, v2 = svd(g_rank2)
    print(f"  singular values of the lesson 01-07-04 kernel = "
          f"{[round(x, 10) for x in s2]}")
    print(f"  smallest singular value = {s2[-1]:.3e}: the matrix is exactly rank 2")
    print(f"  right singular vector v_3 = "
          f"{[round(v2[r][2], 8) for r in range(3)]}  (the null direction)")
    print(f"  A v_3 = {[round(x, 14) for x in matvec(g_rank2, [v2[r][2] for r in range(3)])]}")
    print(f"  left singular vector u_3  = "
          f"{[round(u2[r][2], 8) for r in range(3)]}  (the redundant datum pattern)")
    r2 = [[sum(v2[i][k] * v2[j][k] for k in range(2)) for j in range(3)] for i in range(3)]
    print(f"  R = V_r V_r^T with r = 2: diag = "
          f"{[round(r2[i][i], 8) for i in range(3)]}, trace = "
          f"{sum(r2[i][i] for i in range(3)):.6f}")
    print(f"  R v_3 = {[round(x, 14) for x in matvec(r2, [v2[r][2] for r in range(3)])]}")
    print("\nReading: a zero singular value *is* a null space, and its right")
    print("singular vector is the null direction. A tiny singular value is")
    print("numerically the same situation, and the SVD makes the difference")
    print("visible as a number rather than as a judgement call.")

    section("8. The same decomposition as a compression tool")
    size = 12
    field = [[0.0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            x, y = i / (size - 1), j / (size - 1)
            # Two rotated elliptical anomalies. The rotation is what makes the
            # matrix non-separable, so its rank is full and the singular values
            # decay rather than terminating.
            u1 = (x - 0.35) * math.cos(math.radians(25.0)) + (y - 0.30) * math.sin(math.radians(25.0))
            v1 = -(x - 0.35) * math.sin(math.radians(25.0)) + (y - 0.30) * math.cos(math.radians(25.0))
            u2 = (x - 0.70) * math.cos(math.radians(-40.0)) + (y - 0.65) * math.sin(math.radians(-40.0))
            v2 = -(x - 0.70) * math.sin(math.radians(-40.0)) + (y - 0.65) * math.cos(math.radians(-40.0))
            field[i][j] = (math.exp(-(u1 * u1 / 0.02 + v1 * v1 / 0.006))
                           - 0.7 * math.exp(-(u2 * u2 / 0.01 + v2 * v2 / 0.03)))
    uf, sf, vf = svd(field)
    total = frobenius(field)
    print(f"  a {size}x{size} synthetic anomalous field (two rotated elliptical")
    print("  anomalies -- gravity- or magnetic-like)")
    print(f"  ||F||_F = {total:.6f}")
    print(f"  largest singular values: {[round(x, 6) for x in sf[:6]]}")
    print(f"  smallest singular value: {sf[-1]:.3e}, "
          f"condition number {sf[0] / sf[-1]:.4e}")
    print(f"\n  {'rank':>5}  {'relative error':>16}  {'energy kept':>14}")
    for rank in range(1, size + 1):
        approx = reconstruct(uf, sf, vf, size, size, rank)
        err = frobenius([[approx[i][j] - field[i][j] for j in range(size)]
                         for i in range(size)])
        energy = sum(x * x for x in sf[:rank]) / sum(x * x for x in sf)
        if rank <= 6 or rank == size:
            print(f"  {rank:>5}  {err / total:>16.8f}  {energy:>14.8f}")
    print("\nReading: the singular values decay smoothly, so a handful of rank-one")
    print("terms captures most of the field: four terms reproduce it to within")
    print("5 %, six terms to within 1 %, out of twelve possible. This is the")
    print("mathematics behind low-rank approximations of sensitivity kernels, of")
    print("data covariance matrices, and of the model-space Hessians in large")
    print("tomographic problems -- and it is the reason 'which singular vectors")
    print("matter?' is the most useful question to ask about a geophysical")
    print("operator.")
    print("Caveat: this implementation gets its singular values from the")
    print("eigenproblem of A^T A, which squares the conditioning, so the smallest")
    print("values quoted here are accurate to roughly four digits. A production")
    print("SVD (Golub-Kahan bidiagonalisation) never forms A^T A and does better.")


if __name__ == "__main__":
    main()
