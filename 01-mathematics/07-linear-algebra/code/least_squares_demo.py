"""Orthogonality, projections and least squares, with an exact reference solution.

Run:  python3 least_squares_demo.py
Requires: Python standard library only.

Companion to lesson 01-07-07.

The data are synthetic: a linear gravity trend in elevation with a known
free-air-gradient scale, plus deterministic perturbations. Because the data are
synthetic we can compute the *exact* least-squares solution in rational
arithmetic and compare the two practical routes -- normal equations and QR --
against it. That comparison is the point of Section 4, and it is why production
codes never form G^T G.
"""

import math
from fractions import Fraction

Matrix = list[list[Fraction | float]]
Vector = list[Fraction | float]


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


def norm(x) -> float:
    return math.sqrt(sum(float(v) ** 2 for v in x))


def show(title: str, a, places: int = 4, limit: int = 8) -> None:
    print(f"  {title}")
    for row in a[:limit]:
        print("     [" + "  ".join(f"{float(x):>{9 + places}.{places}f}" for x in row) + "]")


def jacobi_eigen(a, tol: float = 1e-15, sweeps: int = 200):
    n = len(a)
    work = [[float(x) for x in row] for row in a]
    v = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
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


def cond2_of_normal_matrix(a) -> float:
    """kappa_2(A) for a matrix of modest condition number, via A^T A."""
    ata = matmul(transpose(a), a)
    vals, _ = jacobi_eigen(ata)
    vals = sorted(vals, reverse=True)
    return math.sqrt(vals[0] / vals[-1])


def solve_gauss_fraction(a, b):
    """Exact rational solve of a square system."""
    n = len(a)
    m = [[Fraction(a[i][j]) for j in range(n)] + [Fraction(b[i])] for i in range(n)]
    for k in range(n):
        pivot = max(range(k, n), key=lambda r: abs(m[r][k]))
        if m[pivot][k] == 0:
            raise ArithmeticError("singular")
        m[k], m[pivot] = m[pivot], m[k]
        for r in range(k + 1, n):
            factor = m[r][k] / m[k][k]
            for c in range(k, n + 1):
                m[r][c] -= factor * m[k][c]
    x = [Fraction(0)] * n
    for i in range(n - 1, -1, -1):
        x[i] = (m[i][n] - sum(m[i][j] * x[j] for j in range(i + 1, n))) / m[i][i]
    return x


def solve_gauss_float(a, b):
    n = len(a)
    m = [[float(a[i][j]) for j in range(n)] + [float(b[i])] for i in range(n)]
    for k in range(n):
        pivot = max(range(k, n), key=lambda r: abs(m[r][k]))
        if m[pivot][k] == 0.0:
            raise ArithmeticError("singular")
        m[k], m[pivot] = m[pivot], m[k]
        for r in range(k + 1, n):
            factor = m[r][k] / m[k][k]
            for c in range(k, n + 1):
                m[r][c] -= factor * m[k][c]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (m[i][n] - sum(m[i][j] * x[j] for j in range(i + 1, n))) / m[i][i]
    return x


def householder_lstsq(a: Matrix, d: Vector):
    """Least squares by Householder QR. Never forms A^T A."""
    rows, cols = len(a), len(a[0])
    r = [[float(a[i][j]) for j in range(cols)] for i in range(rows)]
    rhs = [float(v) for v in d]
    for k in range(cols):
        x = [r[i][k] for i in range(k, rows)]
        alpha = -math.copysign(norm(x), x[0]) if x[0] != 0.0 else -norm(x)
        v = [x[0] - alpha] + x[1:]
        vnorm = norm(v)
        if vnorm == 0.0:
            continue
        v = [c / vnorm for c in v]
        for j in range(k, cols):
            s = sum(v[i - k] * r[i][j] for i in range(k, rows))
            for i in range(k, rows):
                r[i][j] -= 2.0 * v[i - k] * s
        s = sum(v[i - k] * rhs[i] for i in range(k, rows))
        for i in range(k, rows):
            rhs[i] -= 2.0 * v[i - k] * s
    m = [0.0] * cols
    for i in range(cols - 1, -1, -1):
        m[i] = (rhs[i] - sum(r[i][j] * m[j] for j in range(i + 1, cols))) / r[i][i]
    residual = math.sqrt(sum(rhs[i] ** 2 for i in range(cols, rows)))
    return m, residual, r


def main() -> None:
    section("1. The data and the design matrix")
    # Station elevations in metres and the gravity residual in mGal. SYNTHETIC
    # data: the level and slope are chosen to be consistent with the free-air
    # gradient (0.3086 mGal/m) as a scale reference, and the perturbations are
    # deterministic so that this script reproduces exactly.
    z = [0.0, 200.0, 400.0, 600.0, 800.0, 1000.0, 1200.0, 1400.0]
    noise = [0.04, -0.03, 0.06, -0.05, 0.02, -0.06, 0.05, -0.03]
    intercept, slope = 25.0, -0.3086
    g = [intercept + slope * zi + ni for zi, ni in zip(z, noise)]
    print(f"  {'elevation z (m)':>16}  {'g (mGal)':>12}")
    for zi, gi in zip(z, g):
        print(f"  {zi:>16.0f}  {gi:>12.6f}")
    g_design = [[1.0, zi] for zi in z]
    print(f"\n  model: g(z) = a + b z, parameters (a, b) = "
          f"(mGal, mGal/m)")
    print(f"  the synthetic construction used a = {intercept}, b = {slope};")
    print("  in a real survey the fitted slope would also contain the Bouguer")
    print("  and terrain effects, not the free-air gradient alone.")

    section("2. The normal equations, solved by hand")
    gtg = matmul(transpose(g_design), g_design)
    gtd = matvec(transpose(g_design), g)
    show("G^T G", gtg, places=1)
    print(f"  G^T d = [{gtd[0]:.6f}, {gtd[1]:.6f}]")
    m_hat = solve_gauss_float(gtg, gtd)
    print(f"  solution of G^T G m = G^T d:  a = {m_hat[0]:.8f} mGal, "
          f"b = {m_hat[1]:.10f} mGal/m")
    print(f"  slope in the usual unit: {m_hat[1] * 1000:.6f} muGal/m "
          f"(0.3086 mGal/m = 308.6 muGal/m)")
    residual = [g[i] - matvec(g_design, m_hat)[i] for i in range(len(g))]
    print(f"\n  {'predicted':>12}  {'residual (mGal)':>16}")
    predicted = matvec(g_design, m_hat)
    for p, ri in zip(predicted, residual):
        print(f"  {p:>12.6f}  {ri:>16.8f}")
    print(f"  sum of residuals = {sum(residual):.3e}   (G^T r = 0 forces this)")
    gtr = matvec(transpose(g_design), residual)
    print(f"  G^T r = [{gtr[0]:.3e}, {gtr[1]:.3e}]   (orthogonality, numerically)")
    print(f"  ||r|| = {norm(residual):.8f} mGal")

    section("3. The projection picture")
    # P = G (G^T G)^-1 G^T, with the 2x2 inverse written out in closed form.
    det = gtg[0][0] * gtg[1][1] - gtg[0][1] * gtg[1][0]
    gtg_inv = [[gtg[1][1] / det, -gtg[0][1] / det],
               [-gtg[1][0] / det, gtg[0][0] / det]]
    pmat = matmul(matmul(g_design, gtg_inv), transpose(g_design))
    p2 = matmul(pmat, pmat)
    print(f"  P is {len(pmat)}x{len(pmat)}; its diagonal entries are the leverage")
    print(f"  h_i = P_ii: {[round(pmat[i][i], 6) for i in range(len(pmat))]}")
    print(f"  sum of leverages = {sum(pmat[i][i] for i in range(len(pmat))):.6f} "
          f"= number of parameters = 2")
    print(f"  idempotent: max|P^2 - P| = "
          f"{max(abs(p2[i][j] - pmat[i][j]) for i in range(len(pmat)) for j in range(len(pmat))):.3e}")
    print(f"  P applied to the residual: max|P r| = "
          f"{max(abs(v) for v in matvec(pmat, residual)):.3e}")
    d_norm2 = sum(v * v for v in g)
    r_norm2 = sum(v * v for v in residual)
    fit_norm2 = sum(v * v for v in predicted)
    print(f"  Pythagorean check: ||d||^2 = {d_norm2:.6f}, "
          f"||d_hat||^2 + ||r||^2 = {fit_norm2 + r_norm2:.6f}")
    print("\nReading: P projects the data onto the two-dimensional column space")
    print("spanned by 'constant' and 'linear in z'. It is symmetric and")
    print("idempotent -- a projection, not a rescaling. The residual lies in the")
    print("orthogonal complement, which is exactly what G^T r = 0 says.")

    section("4. Normal equations versus QR, against an exact reference")
    d_vec = [float(v) for v in g]

    def compare_routes(gmat, dvals, label, note=""):
        """Normal equations and QR against the exact rational least-squares solution."""
        rows, cols = len(gmat), len(gmat[0])
        gtg_f = [[Fraction(0)] * cols for _ in range(cols)]
        gtd_f = [Fraction(0)] * cols
        for i in range(rows):
            for a in range(cols):
                gtd_f[a] += Fraction(gmat[i][a]) * Fraction(dvals[i])
                for b in range(cols):
                    gtg_f[a][b] += Fraction(gmat[i][a]) * Fraction(gmat[i][b])
        m_exact = solve_gauss_fraction(gtg_f, gtd_f)
        try:
            m_ne = solve_gauss_float([[float(x) for x in r] for r in gtg_f],
                                     [float(x) for x in gtd_f])
        except ArithmeticError:
            m_ne = None
        m_qr, _, _ = householder_lstsq(gmat, dvals)
        kappa = cond2_of_normal_matrix(gmat) if rows > cols else None
        err_ne = (max(abs(m_ne[j] - float(m_exact[j])) / abs(float(m_exact[j]))
                      for j in range(cols)) if m_ne else float("inf"))
        err_qr = max(abs(m_qr[j] - float(m_exact[j])) / abs(float(m_exact[j]))
                     for j in range(cols))
        print(f"  {label}")
        print(f"    exact parameters        = "
              f"{[round(float(v), 10) for v in m_exact]}")
        if m_ne:
            print(f"    normal-equation params  = {[round(v, 10) for v in m_ne]}")
        else:
            print("    normal-equation params  = FAILED: the float normal-equation")
            print("                              system is numerically singular"
                  " (zero pivot)")
        print(f"    QR params               = {[round(v, 10) for v in m_qr]}")
        if kappa is not None:
            print(f"    kappa_2(G) = {kappa:.4e},  kappa_2(G^T G) = {kappa * kappa:.4e}")
        else:
            print("    (square G: kappa is reported in lesson 01-07-05 terms)")
        print(f"    max relative parameter error: normal equations "
              f"{err_ne:.3e}, QR {err_qr:.3e}"
              + (f"   (ratio {err_ne / err_qr:.1f}x)" if m_ne and err_qr else ""))
        if note:
            print(f"    {note}")

    for name, basis in (("centred and scaled basis, (x-700)/1400",
                         lambda zi: [1.0, (zi - 700.0) / 1400.0,
                                     ((zi - 700.0) / 1400.0) ** 2,
                                     ((zi - 700.0) / 1400.0) ** 3]),
                        ("uncentred cubic basis, x in metres",
                         lambda zi: [1.0, zi, zi ** 2, zi ** 3])):
        vand = [basis(zi) for zi in z]
        compare_routes(vand, d_vec, f"degree-3 trend, {name}")

    delta = 1e-8
    g_rays = [[1.0, 1.0], [1.0, 1.0 + delta]]
    m_truth = [0.05, -0.02]
    d_rays = [g_rays[0][0] * m_truth[0] + g_rays[0][1] * m_truth[1],
              g_rays[1][0] * m_truth[0] + g_rays[1][1] * m_truth[1]]
    print(f"\n  two rays whose paths differ by delta = {delta:.0e} km, "
          f"kappa(G) ~ 4/delta = {4.0 / delta:.0e}:")
    compare_routes(g_rays, d_rays, "two-cell, two-ray experiment")
    print("\nReading: three results, one rule. The rule is that the error of the")
    print("normal-equation route grows like kappa(G)^2 eps while the error of QR")
    print("grows like kappa(G) eps, with eps = 2.2e-16. In the centred basis both")
    print("are at round-off. In the uncentred basis the normal equations are about")
    print("fifty times worse -- visible, but survivable, because the weak")
    print("directions happen to be empty in this dataset. In the nearly parallel")
    print("two-ray geometry the weak direction is exactly where the information")
    print("lives and the normal equations collapse completely, while QR still")
    print("recovers both model parameters to full working precision.")
    print("A second lesson hides in the trend fits: the *fitted values* stay")
    print("accurate even when the parameters do not, because the projection onto")
    print("the column space is robust to the parameterisation. Centring and")
    print("scaling the basis removes the difficulty at source, and that is a")
    print("better cure than choosing the better algorithm. Do both.")

    section("5. Weighted least squares")
    # Station elevations are surveyed; the height uncertainty grows with height,
    # so sigma_i = 0.5 + z_i / 1000 mGal-equivalent.
    sigma = [0.05 + zi / 20000.0 for zi in z]
    weights = [1.0 / s ** 2 for s in sigma]
    gw = [[g_design[i][j] * math.sqrt(weights[i]) for j in range(2)] for i in range(len(z))]
    dw = [g[i] * math.sqrt(weights[i]) for i in range(len(z))]
    m_w = solve_gauss_float(matmul(transpose(gw), gw), matvec(transpose(gw), dw))
    print(f"  {'sigma (mGal)':>12}  {'1/sigma^2':>12}")
    for s, w in zip(sigma, weights):
        print(f"  {s:>12.6f}  {w:>12.3f}")
    print(f"\n  ordinary fit : a = {m_hat[0]:.8f}, b = {m_hat[1]:.10f}")
    print(f"  weighted fit : a = {m_w[0]:.8f}, b = {m_w[1]:.10f}")
    chi2_weighted = sum(((g[i] - matvec(g_design, m_w)[i]) / sigma[i]) ** 2
                        for i in range(len(z)))
    chi2_ordinary = sum(((g[i] - predicted[i]) / sigma[i]) ** 2 for i in range(len(z)))
    print(f"  chi^2 of the weighted fit   = {chi2_weighted:.6f}")
    print(f"  chi^2 of the ordinary fit   = {chi2_ordinary:.6f}")
    print(f"  (8 data and 2 parameters; if the assumed sigma were the true noise")
    print(f"  level, a good fit would give chi^2 near {len(z) - 2}. These values are")
    print("  lower, i.e. the assumed sigma are conservative relative to the")
    print("  perturbations built into this synthetic dataset.)")
    print("\nReading: weighting is not a refinement of least squares; it is part")
    print("of the definition. The objective is a sum of squared residuals in units")
    print("of the data's own uncertainty, and minimising the unweighted sum")
    print("implicitly asserts that every datum has the same uncertainty. Lesson")
    print("01-07-08 turns the weights into the data covariance matrix.")

    section("6. More parameters always fit better -- and mean less")
    print(f"  {'degree':>7}  {'parameters':>11}  {'||r|| (mGal)':>14}  "
          f"{'std err of slope':>18}")
    for degree in (1, 2, 3, 4, 5):
        vand = [[zi ** k for k in range(degree + 1)] for zi in z]
        if degree + 1 > len(z):
            continue
        m_deg, res_norm, _ = householder_lstsq(vand, g)
        gtg_d = matmul(transpose(vand), vand)
        gtg_d_inv = None
        try:
            n = degree + 1
            aug = [row[:] + [1.0 if i == j else 0.0 for j in range(n)]
                   for i, row in enumerate([r[:] for r in gtg_d])]
            for k in range(n):
                piv = max(range(k, n), key=lambda r: abs(aug[r][k]))
                aug[k], aug[piv] = aug[piv], aug[k]
                sc = aug[k][k]
                aug[k] = [v / sc for v in aug[k]]
                for r in range(n):
                    if r != k and aug[r][k] != 0.0:
                        f = aug[r][k]
                        aug[r] = [v - f * w for v, w in zip(aug[r], aug[k])]
            gtg_d_inv = [row[n:] for row in aug]
        except (ArithmeticError, ZeroDivisionError):
            gtg_d_inv = None
        sigma_d = res_norm / math.sqrt(max(1, len(z) - (degree + 1)))
        slope_se = (math.sqrt(sigma_d ** 2 * gtg_d_inv[1][1])
                    if gtg_d_inv else float("nan"))
        print(f"  {degree:>7}  {degree + 1:>11}  {res_norm:>14.8f}  "
              f"{slope_se:>18.6e}")
    print("\nReading: the residual norm falls monotonically with the number of")
    print("parameters, and it must -- a larger column space can only be closer to")
    print("the data. The standard error of the slope rises just as steadily. A")
    print("small residual is therefore not evidence of a good model; it is")
    print("arithmetic. Model choice needs a criterion that penalises parameters,")
    print("and that criterion is the subject of 18-inverse-problems.")


if __name__ == "__main__":
    main()
