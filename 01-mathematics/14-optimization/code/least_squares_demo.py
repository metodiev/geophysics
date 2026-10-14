"""Linear and nonlinear least squares: normal equations, QR, Gauss-Newton.

Run:  python3 least_squares_demo.py
Requires: Python standard library only.

Companion to lesson 01-14-04.

The central claim of the lesson is that solving a least-squares problem by the
normal equations squares the condition number and therefore costs accuracy,
which is why production codes use QR or the SVD. That claim is measured here: a
kernel with integer entries and integer data has an *exact* rational solution, so
each float route can be compared with the truth. The same section is repeated for
a well-scaled kernel, a badly scaled one, and two nearly parallel rays whose
normal-equation system cannot even be factored.

The nonlinear part of the lesson (Gauss-Newton, Levenberg-Marquardt) is measured
the same way: iteration counts, the observed convergence of the residual, and the
starting model from which each method fails.
"""

import math
from decimal import Decimal, localcontext
from fractions import Fraction

Vector = list[float]
Matrix = list[list[float]]


def section(title: str) -> None:
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


# --------------------------------------------------------------------------
# Floating-point linear algebra
# --------------------------------------------------------------------------

def matmul(a, b):
    n, k, m = len(a), len(b), len(b[0])
    return [[sum(a[i][t] * b[t][j] for t in range(k)) for j in range(m)]
            for i in range(n)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def matvec(a, x):
    return [sum(a[i][j] * x[j] for j in range(len(x))) for i in range(len(a))]


def dot(x, y) -> float:
    return sum(a * b for a, b in zip(x, y))


def norm(x) -> float:
    return math.sqrt(dot(x, x))


def solve(a, b):
    """Gaussian elimination with partial pivoting (raises on a singular system)."""
    n = len(a)
    m = [list(row) + [b[i]] for i, row in enumerate(a)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(m[r][col]))
        if abs(m[pivot][col]) < 1e-300:
            raise ZeroDivisionError(f"zero pivot at column {col}")
        m[col], m[pivot] = m[pivot], m[col]
        for r in range(col + 1, n):
            factor = m[r][col] / m[col][col]
            for c in range(col, n + 1):
                m[r][c] -= factor * m[col][c]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (m[i][n] - sum(m[i][j] * x[j] for j in range(i + 1, n))) / m[i][i]
    return x


def symmetric_eigenvalues(a, sweeps: int = 60):
    n = len(a)
    w = [[float(x) for x in row] for row in a]
    for _ in range(sweeps):
        off = math.sqrt(sum(w[i][j] ** 2 for i in range(n) for j in range(n)
                           if i != j))
        if off < 1e-16:
            break
        for p in range(n - 1):
            for q in range(p + 1, n):
                if abs(w[p][q]) < 1e-300:
                    continue
                theta = (w[q][q] - w[p][p]) / (2.0 * w[p][q])
                t = math.copysign(1.0, theta) / (abs(theta) + math.sqrt(theta * theta + 1.0))
                c = 1.0 / math.sqrt(t * t + 1.0)
                s = t * c
                for k in range(n):
                    wk_p, wk_q = w[k][p], w[k][q]
                    w[k][p] = c * wk_p - s * wk_q
                    w[k][q] = s * wk_p + c * wk_q
                for k in range(n):
                    wp_k, wq_k = w[p][k], w[q][k]
                    w[p][k] = c * wp_k - s * wq_k
                    w[q][k] = s * wp_k + c * wq_k
    return sorted(w[i][i] for i in range(n))


def condition(a) -> float:
    """Condition number of a matrix with full column rank, from A^T A."""
    eigs = symmetric_eigenvalues(matmul(transpose(a), a))
    return math.sqrt(eigs[-1] / eigs[0])


def condition_decimal(a, prec: int = 60) -> float:
    """kappa(A) in extended precision, with A^T A formed exactly.

    A badly scaled basis has a condition number whose square exceeds 1/eps, so
    A^T A cannot be formed in double precision without losing its smallest
    eigenvalue entirely. A^T A is therefore built in Decimal arithmetic and the
    Jacobi iteration is repeated there, which is the only way to *measure* the
    quantity the lesson talks about.
    """
    with localcontext() as ctx:
        ctx.prec = prec
        ad = [[Decimal(v) for v in row] for row in a]
        n_cols = len(ad[0])
        ata = [[sum(ad[k][i] * ad[k][j] for k in range(len(ad)))
                for j in range(n_cols)] for i in range(n_cols)]
        n = n_cols
        w = [row[:] for row in ata]
        for _ in range(120):
            off = sum(w[i][j] ** 2 for i in range(n) for j in range(n) if i != j)
            total = sum(w[i][j] ** 2 for i in range(n) for j in range(n))
            if off <= total * Decimal(10) ** (-(prec - 10)):
                break
            for p in range(n - 1):
                for q in range(p + 1, n):
                    if w[p][q] == 0:
                        continue
                    theta = (w[q][q] - w[p][p]) / (2 * w[p][q])
                    t = (Decimal(1) / (abs(theta) + (theta * theta + 1).sqrt())
                         * (1 if theta >= 0 else -1))
                    c = 1 / (t * t + 1).sqrt()
                    s = t * c
                    for k in range(n):
                        wk_p, wk_q = w[k][p], w[k][q]
                        w[k][p] = c * wk_p - s * wk_q
                        w[k][q] = s * wk_p + c * wk_q
                    for k in range(n):
                        wp_k, wq_k = w[p][k], w[q][k]
                        w[p][k] = c * wp_k - s * wq_k
                        w[q][k] = s * wp_k + c * wq_k
        eigs = sorted(w[i][i] for i in range(n))
        if eigs[0] <= 0:
            return float("inf")
        return float((eigs[-1] / eigs[0]).sqrt())


def normal_equations(a, d):
    ata = matmul(transpose(a), a)
    atd = matvec(transpose(a), d)
    return solve(ata, atd)


def qr_least_squares(a, d):
    """Householder QR, then back-substitution on the leading square block."""
    m, n = len(a), len(a[0])
    r = [[float(a[i][j]) for j in range(n)] for i in range(m)]
    qt_d = [float(v) for v in d]
    for k in range(n):
        column = [r[i][k] for i in range(k, m)]
        alpha = -math.copysign(norm(column), column[0]) if column[0] != 0 else -norm(column)
        v = column[:]
        v[0] -= alpha
        vnorm2 = dot(v, v)
        if vnorm2 < 1e-300:
            continue
        for j in range(n):
            s = sum(v[i] * r[k + i][j] for i in range(len(v)))
            for i in range(len(v)):
                r[k + i][j] -= 2.0 * v[i] * s / vnorm2
        s = sum(v[i] * qt_d[k + i] for i in range(len(v)))
        for i in range(len(v)):
            qt_d[k + i] -= 2.0 * v[i] * s / vnorm2
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (qt_d[i] - sum(r[i][j] * x[j] for j in range(i + 1, n))) / r[i][i]
    return x


def fraction_solve(a, b):
    """Exact rational Gaussian elimination; used as the reference solution."""
    n = len(a)
    m = [[Fraction(v) for v in row] + [Fraction(b[i])] for i, row in enumerate(a)]
    for col in range(n):
        pivot = next(r for r in range(col, n) if m[r][col] != 0)
        m[col], m[pivot] = m[pivot], m[col]
        for r in range(col + 1, n):
            factor = m[r][col] / m[col][col]
            for c in range(col, n + 1):
                m[r][c] -= factor * m[col][c]
    x = [Fraction(0)] * n
    for i in range(n - 1, -1, -1):
        x[i] = (m[i][n] - sum(m[i][j] * x[j] for j in range(i + 1, n))) / m[i][i]
    return x


def exact_least_squares(a, d):
    """Exact rational solution of the normal equations."""
    return fraction_solve(matmul(transpose(a), a), matvec(transpose(a), d))


def rel_error(approx, exact) -> float:
    scale = max(abs(float(v)) for v in exact) or 1.0
    return max(abs(approx[i] - float(exact[i])) for i in range(len(exact))) / scale


# --------------------------------------------------------------------------
# A cross-hole tomography kernel with integer entries
# --------------------------------------------------------------------------

A_SIX = [[1, 1, 0, 0],
         [0, 1, 1, 0],
         [0, 0, 1, 1],
         [1, 0, 0, 1],
         [1, 1, 1, 1],
         [2, 1, 0, 2]]
D_SIX = [3, 4, 5, 3, 7, 8]             # travel-time residuals, s (ILLUSTRATIVE)


def main() -> None:
    section("1. Normal equations versus Householder QR, against exact arithmetic")

    exact = exact_least_squares(A_SIX, D_SIX)
    print("  six-ray, four-cell kernel with integer path lengths (SYNTHETIC):")
    print("    exact rational solution (s/km): "
          + ", ".join(f"{float(v):+.12f}" for v in exact))
    print("    the solution is a ratio of small integers, so every float route")
    print("    can be scored against it")

    m_ne = normal_equations(A_SIX, D_SIX)
    m_qr = qr_least_squares(A_SIX, D_SIX)
    print(f"    kappa(A)                 = {condition(A_SIX):.6f}")
    print(f"    kappa(A^T A)             = "
          f"{condition(A_SIX) ** 2:.6f}   (= kappa(A)^2, by identity)")
    print("    normal equations (s/km): "
          + ", ".join(f"{v:+.12f}" for v in m_ne))
    print(f"      max relative error     = {rel_error(m_ne, exact):.3e}")
    print("    Householder QR (s/km):   "
          + ", ".join(f"{v:+.12f}" for v in m_qr))
    print(f"      max relative error     = {rel_error(m_qr, exact):.3e}")

    r_ne = [matvec(A_SIX, m_ne)[i] - D_SIX[i] for i in range(6)]
    print(f"    ||r||, normal equations  = {norm(r_ne):.12f}")
    print(f"    ||A^T r||, normal eqs    = "
          f"{norm(matvec(transpose(A_SIX), r_ne)):.3e}   (zero to round-off)")

    section("2. The same comparison across a range of condition numbers")

    print("  A = [[1, 1], [1, 1+d]] (two nearly parallel rays), exact data from")
    print("  m = (0.05, -0.02) s/km, so the exact solution is known.")

    exact2 = [Fraction(5, 100), Fraction(-2, 100)]
    print(f"  {'delta':>10}{'kappa(A)':>14}{'normal eq. error':>20}"
          f"{'QR error':>14}{'ratio':>10}")
    for delta in (1e-2, 1e-4, 1e-6, 1e-8):
        a = [[1.0, 1.0], [1.0, 1.0 + delta]]
        d = matvec(a, [0.05, -0.02])
        # The reference is the exact least-squares solution of this float
        # system, computed in rational arithmetic.
        a_exact = [[Fraction(v) for v in row] for row in a]
        d_exact = [Fraction(v) for v in d]
        exact_ref = fraction_solve(matmul(transpose(a_exact), a_exact),
                                   matvec(transpose(a_exact), d_exact))
        try:
            m_ne = normal_equations(a, d)
            err_ne = rel_error(m_ne, exact_ref)
        except ZeroDivisionError:
            err_ne = float("nan")
        m_qr = qr_least_squares(a, d)
        err_qr = rel_error(m_qr, exact_ref)
        kap = condition_decimal(a)
        ratio = err_ne / err_qr if err_qr > 0 else float("nan")
        ne_text = "no solution" if math.isnan(err_ne) else f"{err_ne:.3e}"
        print(f"  {delta:>10.0e}{kap:>14.3e}{ne_text:>20}"
              f"{err_qr:>14.3e}{ratio:>10.3e}")
        ata_float = matmul(transpose(a), a)
        d_f = ata_float[0][0] * ata_float[1][1] - ata_float[0][1] ** 2
        print(f"              kappa(A)^2 = {kap * kap:.3e},"
              f" 1/eps = {1.0 / 2.220446049250313e-16:.3e}"
              f", det(A^T A) in float = {d_f:+.3e}")
    print("  The QR error tracks kappa(A) * eps; the normal-equation error")
    print("  tracks kappa(A)^2 * eps and stops being a solution at all once")
    print("  kappa(A)^2 approaches 1/eps.")

    section("3. A badly scaled basis: the same physics, a different basis")

    x = [0.0, 200.0, 400.0, 600.0, 800.0, 1000.0, 1200.0, 1400.0]
    g_raw = [[1.0, xi, xi * xi, xi ** 3] for xi in x]
    g_scaled = [[1.0, (xi - 700.0) / 1400.0, ((xi - 700.0) / 1400.0) ** 2,
                 ((xi - 700.0) / 1400.0) ** 3] for xi in x]
    d8 = [25.0 - 0.3086 * xi for xi in x]

    print("  Same cubic trend fitted in two bases; the data are exact decimals,")
    print("  so a rational reference solution exists for each basis.")
    print(f"  {'basis':<22}{'kappa(G)':>14}{'kappa(G)^2':>14}"
          f"{'normal eq. err':>18}{'QR err':>14}")
    for label, g in (("raw cubic in metres", g_raw),
                     ("centred and scaled", g_scaled)):
        g_exact = [[Fraction(v) for v in row] for row in g]
        d_exact = [Fraction(v) for v in d8]
        exact8 = fraction_solve(matmul(transpose(g_exact), g_exact),
                                matvec(transpose(g_exact), d_exact))
        m_ne = normal_equations(g, d8)
        m_qr = qr_least_squares(g, d8)
        kap = condition_decimal(g)
        print(f"  {label:<22}{kap:>14.4e}{kap * kap:>14.4e}"
              f"{rel_error(m_ne, exact8):>18.3e}{rel_error(m_qr, exact8):>14.3e}")
    print("  In double precision kappa(G^T G) for the raw basis cannot be formed")
    print("  at all: it is kappa(G)^2, which exceeds 1/eps. The extended-precision")
    print("  values quoted above are the ones the lesson should be judged against.")

    section("4. Nonlinear least squares: Gauss-Newton on a gravity profile")

    def model(params, xv):
        """Vertical-cylinder gravity profile, arbitrary units (SYNTHETIC)."""
        amp, depth = params
        return amp * depth / (xv * xv + depth * depth) ** 1.5

    xv = [-8.0, -6.0, -4.0, -2.0, 0.0, 2.0, 4.0, 6.0, 8.0]
    true = [100.0, 20.0]
    clean = [model(true, xi) for xi in xv]
    # Deterministic perturbation, below 0.5 per cent of the peak value.
    noise = [0.0010, 0.0004, -0.0006, 0.0009, -0.0003, 0.0007, -0.0009,
             0.0005, 0.0002]
    data = [clean[i] + noise[i] for i in range(len(xv))]

    def jacobian(params):
        amp, depth = params
        rows = []
        for xi in xv:
            r2 = xi * xi + depth * depth
            j_amp = depth / r2 ** 1.5
            j_depth = amp * ((1.0 / r2 ** 1.5) - 3.0 * depth * depth / r2 ** 2.5)
            rows.append([j_amp, j_depth])
        return rows

    def residual(params):
        return [model(params, xv[i]) - data[i] for i in range(len(xv))]

    def gn(params, iters=40, damping=0.0, line_search=True):
        """Gauss-Newton with optional scaled Levenberg damping and a line search.

        Returns (model, residual history, status). Failures are reported rather
        than hidden: a zero pivot in J^T J and an unbounded step are both real
        outcomes of an undamped Gauss-Newton iteration.
        """
        p = params[:]
        history = [norm(residual(p))]
        for _ in range(iters):
            r = residual(p)
            f0 = 0.5 * dot(r, r)
            j = jacobian(p)
            jtj = matmul(transpose(j), j)
            jtr = matvec(transpose(j), r)
            if norm(jtr) <= 1e-12:
                return p, history, "converged (gradient below tolerance)"
            if damping:
                mean_diag = 0.5 * (jtj[0][0] + jtj[1][1])
                for i in range(2):
                    jtj[i][i] += damping * mean_diag
            try:
                step = solve(jtj, jtr)
            except ZeroDivisionError:
                return p, history, "singular J^T J"
            alpha = 1.0
            accepted = not line_search
            while alpha > 1e-10:
                trial = [p[0] - alpha * step[0], p[1] - alpha * step[1]]
                if not all(math.isfinite(v) for v in trial) or abs(trial[1]) > 1e6:
                    alpha *= 0.5
                    continue
                trial_cost = 0.5 * norm(residual(trial)) ** 2
                if (not line_search
                        or trial_cost <= f0 * (1.0 - 1e-4 * alpha)
                        or trial_cost <= f0 * (1.0 + 1e-12)):
                    accepted = True
                    break
                alpha *= 0.5
            if not accepted:
                return p, history, "line search failed"
            p = trial
            history.append(norm(residual(p)))
        return p, history, "ok"

    p_start = [100.0, 20.0]
    p_gn, hist_gn, status_gn = gn(p_start, iters=25)
    print("  model d_i = A h / (x_i^2 + h^2)^{3/2}, true (A, h) = (100, 20)")
    print(f"  9 stations; largest perturbation {max(abs(v) for v in noise):.4f},"
          f" which is {max(abs(v) for v in noise) / max(clean) * 100.0:.2f}"
          f" per cent of the peak")
    print(f"  start (A, h) = {p_start}, residual norm = {hist_gn[0]:.6f}")
    print(f"  Gauss-Newton result: ({p_gn[0]:.8f}, {p_gn[1]:.8f}) after 25"
          f" iterations")
    print(f"  residual norm {hist_gn[-1]:.8f}, initial {hist_gn[0]:.6f},"
          f" ratio {hist_gn[-1] / hist_gn[0]:.3e}")
    print("  residual norms after each of the first six iterations:")
    print("    " + ", ".join(f"{h:.6e}" for h in hist_gn[:6]))

    section("5. Convergence of Gauss-Newton, and why it needs a good start")

    p_best, hist_best, _ = gn([100.0, 20.0], iters=400)
    best_res = hist_best[-1]
    print(f"  best residual reachable (400 iterations from a good start):"
          f" {best_res:.10f}")
    print("  From a start inside the basin the linearisation is accurate; from a")
    print("  start outside it the linearisation is simply wrong.")
    print(f"  {'start h':>8}{'GN h':>13}{'GN res':>12}{'status':>11}"
          f"{'iters to 1%':>13}{'LM h':>11}{'LM res':>12}")
    for h0 in (20.0, 30.0, 45.0, 60.0, 90.0):
        p_gn_s, hist, status = gn([100.0, h0], iters=200)
        reached = next((k for k, h in enumerate(hist)
                        if h <= 1.01 * best_res), None)
        p_lm, hist_lm, _ = gn([100.0, h0], iters=200, damping=1.0)
        short = "ok" if status.startswith(("ok", "converged")) else status
        print(f"  {h0:>8.1f}{p_gn_s[1]:>13.6f}{hist[-1]:>12.3e}{short:>11}"
              f"{(str(reached) if reached is not None else 'no'):>13}"
              f"{p_lm[1]:>11.6f}{hist_lm[-1]:>12.3e}")
    print("  Gauss-Newton reaches the basin quickly when it is already inside it,")
    print("  and barely moves when it is not; the damped version keeps making")
    print("  progress from every start, at the cost of many more iterations.")

    section("6. Weighting: the data covariance is part of the problem")

    a = [[1.0, 0.0], [1.0, 1.0], [1.0, 2.0], [1.0, 3.0], [1.0, 4.0]]
    d5 = [1.0, 2.0, 2.0, 4.0, 4.6]
    m_plain = normal_equations(a, d5)
    sigma = [0.1, 0.1, 0.1, 1.0, 1.0]
    w = [[1.0 / (sigma[i] ** 2) if i == j else 0.0 for j in range(5)]
         for i in range(5)]
    atw = matmul(transpose(a), w)
    m_weighted = solve(matmul(atw, a), matvec(atw, d5))
    print(f"  ordinary fit:  a = {m_plain[0]:.8f}, b = {m_plain[1]:.8f}")
    print(f"  weighted fit:  a = {m_weighted[0]:.8f}, b = {m_weighted[1]:.8f}")
    print(f"  data uncertainties (sigma): {sigma}")
    print(f"  change in slope: {m_weighted[1] - m_plain[1]:+.6f}"
          f"   ({(m_weighted[1] / m_plain[1] - 1.0) * 100.0:+.2f} per cent)")

    section("7. Outliers: what least squares does with them")

    d_out = d5[:]
    d_out[4] = 9.0                                # one bad datum
    m_out = normal_equations(a, d_out)
    print(f"  clean data fit:        b = {m_plain[1]:.8f}")
    print(f"  one outlier at x = 4:  b = {m_out[1]:.8f}"
          f"   shift {m_out[1] - m_plain[1]:+.6f}")
    # L1 fit by a small coordinate-descent search on the intercept and slope.
    best = None
    b_try = -2.0
    while b_try <= 4.0:
        a_try = -4.0
        while a_try <= 6.0:
            cost = sum(abs(a_try + b_try * a[i][1] - d_out[i]) for i in range(5))
            if best is None or cost < best[0]:
                best = (cost, a_try, b_try)
            a_try += 0.001
        b_try += 0.001
    print(f"  L1 fit on a coarse 2-D grid: a = {best[1]:.3f}, b = {best[2]:.3f}"
          f" (grid step 0.001)")
    print(f"  shift of the L1 slope from the clean-data least-squares slope:"
          f" {best[2] - m_plain[1]:+.6f}")
    print("  The L1 slope moves far less than the L2 slope, which is why the")
    print("  robust-fit problem is stated as a linear program in lesson 07.")

    section("8. Leverage: which data control the fit")

    ata = matmul(transpose(a), a)
    at_inv = [[0.0] * 2 for _ in range(2)]
    det = ata[0][0] * ata[1][1] - ata[0][1] * ata[1][0]
    at_inv[0][0] = ata[1][1] / det
    at_inv[1][1] = ata[0][0] / det
    at_inv[0][1] = at_inv[1][0] = -ata[0][1] / det
    leverages = [a[i][0] * (at_inv[0][0] * a[i][0] + at_inv[0][1] * a[i][1])
                 + a[i][1] * (at_inv[1][0] * a[i][0] + at_inv[1][1] * a[i][1])
                 for i in range(5)]
    print("  five-station line fit: x = 0, 1, 2, 3, 4 m")
    print("    leverages h_i: " + ", ".join(f"{h:.8f}" for h in leverages))
    print(f"    sum h_i = {sum(leverages):.8f}  (= number of parameters, 2)")
    print("  The outermost stations carry the most leverage on the slope, so a")
    print("  blunder there damages the fit more than one in the middle.")


if __name__ == "__main__":
    main()
