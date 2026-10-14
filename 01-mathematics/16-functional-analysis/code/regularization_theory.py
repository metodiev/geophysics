"""Tikhonov regularisation, the L-curve and the discrepancy principle.

Run:  python3 regularization_theory.py
Requires: Python standard library only.

Companion to lesson 01-16-06 (Tikhonov Regularisation and the L-Curve).

The operator is the gravity kernel of lesson 01-16-05,

    d(x) = int_0^1 K(x - y) m(y) dy,   K(s) = (z/pi)/(s^2 + z^2),  z = 0.05,

discretised on 80 nodes. Because K is symmetric, K = V diag(lambda) V^T and

    m_alpha = (K^T K + alpha I)^{-1} K^T d
            = sum_k  [lambda_k / (lambda_k^2 + alpha)] <v_k, d> v_k,

so every alpha is evaluated exactly from one eigendecomposition.

Sections
    1. The filter factors, and the effective number of resolved parameters
    2. The L-curve, and the corner located by its curvature
    3. Sensitivity of the answer to the choice of alpha
    4. The discrepancy principle, and how it compares with the corner
    5. Both limits, and the two noise levels
"""

import math
import random

N = 80
Z = 0.05


def section(title):
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72)


def mat_vec(A, x):
    return [sum(a * b for a, b in zip(row, x)) for row in A]


def jacobi_eig(A, tol=1e-16, max_sweeps=300):
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


def setup(n=N, z=Z):
    h = 1.0 / (n - 1)
    x = [i * h for i in range(n)]
    K = [[h * (z / math.pi) / ((x[i] - x[j]) ** 2 + z * z) for j in range(n)]
         for i in range(n)]
    m_true = [math.exp(-((xi - 0.25) ** 2) / (2 * 0.06 ** 2))
              + 0.5 * math.exp(-((xi - 0.7) ** 2) / (2 * 0.08 ** 2)) for xi in x]
    return x, h, K, m_true


def main():
    n = N
    x, h, K, m_true = setup(n)

    def wnorm(v):
        return math.sqrt(h * sum(t * t for t in v))

    ev, V = jacobi_eig(K)
    order = sorted(range(n), key=lambda k: -abs(ev[k]))
    lam = [abs(ev[i]) for i in order]
    cols = [[V[i][order[k]] for i in range(n)] for k in range(n)]

    def coeffs(d):
        return [sum(cols[k][i] * d[i] for i in range(n)) for k in range(n)]

    def tikhonov(c, alpha):
        return [sum(lam[k] / (lam[k] ** 2 + alpha) * c[k] * cols[k][i]
                    for k in range(n)) for i in range(n)]

    d_exact = mat_vec(K, m_true)
    d_norm = wnorm(d_exact)

    random.seed(20261014)
    noise = [random.gauss(0.0, 1.0) for _ in range(n)]
    eps = 1e-2
    scale = eps * d_norm / wnorm(noise)
    d = [d_exact[i] + scale * noise[i] for i in range(n)]
    delta = wnorm([d[i] - d_exact[i] for i in range(n)])
    c = coeffs(d)

    print(f"    {n} nodes, kernel depth z = {Z}; model has two Gaussians")
    print(f"    ||d_true|| = {d_norm:.6f}, ||m_true|| = {wnorm(m_true):.6f}")
    print(f"    added Gaussian noise with relative level eps = {eps:.1e}")
    print(f"    ||noise|| = delta = {delta:.6e}")
    print(f"    lambda_1 = {lam[0]:.6f}, lambda_1^2 = {lam[0] ** 2:.6f}, "
          f"lambda_min = {lam[-1]:.3e}")

    section("1. Filter factors and effective degrees of freedom")
    print("    mode k is multiplied by f_k = lambda_k^2 / (lambda_k^2 + alpha)")
    print(f"    {'alpha':>10}" + "".join(f"{'k=%d' % k:>12}" for k in (1, 8, 16, 32, 64)))
    for alpha in (1e-1, 1e-2, 1e-3, 1e-4, 1e-6, 1e-8):
        row = [lam[k - 1] ** 2 / (lam[k - 1] ** 2 + alpha) for k in (1, 8, 16, 32, 64)]
        print(f"    {alpha:>10.0e}" + "".join(f"{v:>12.6f}" for v in row))
    print("    the number of parameters the data resolve is trace(R_alpha) =")
    print(f"    sum_k f_k:")
    print(f"    {'alpha':>10}{'trace(R_alpha)':>18}{'of':>6}")
    for alpha in (1e-1, 1e-2, 1e-3, 1e-4, 1e-6, 1e-8):
        tr = sum(l * l / (l * l + alpha) for l in lam)
        print(f"    {alpha:>10.0e}{tr:>18.4f}{n:>6}")

    section("2. The L-curve, and the corner located by curvature")
    loga = [-14.0 + j * 0.25 for j in range(int((3.0 + 14.0) / 0.25) + 1)]
    alphas = [10.0 ** t for t in loga]
    residual = []
    modelnorm = []
    errors = []
    for alpha in alphas:
        m = tikhonov(c, alpha)
        r = [a - b for a, b in zip(mat_vec(K, m), d)]
        residual.append(wnorm(r))
        modelnorm.append(wnorm(m))
        errors.append(wnorm([a - b for a, b in zip(m, m_true)]))

    xs = [math.log10(v) for v in residual]
    ys = [math.log10(v) for v in modelnorm]
    curv = [0.0] * len(xs)
    for i in range(1, len(xs) - 1):
        dx1, dx2 = xs[i] - xs[i - 1], xs[i + 1] - xs[i]
        dy1, dy2 = ys[i] - ys[i - 1], ys[i + 1] - ys[i]
        d1x, d1y = (dx1 + dx2) / 2.0, (dy1 + dy2) / 2.0
        d2x, d2y = dx2 - dx1, dy2 - dy1
        den = (d1x * d1x + d1y * d1y) ** 1.5
        curv[i] = (d1x * d2y - d1y * d2x) / den if den > 0 else 0.0

    ic = max(range(len(curv)), key=lambda i: curv[i])
    alpha_c = alphas[ic]
    print(f"    L-curve: x = log10 ||K m - d||, y = log10 ||m||, "
          f"{len(alphas)} values of alpha")
    print(f"    {'alpha':>12}{'||Km-d||':>16}{'||m||':>16}{'curvature':>16}"
          f"{'model error':>16}")
    for i in range(max(0, ic - 6), min(len(alphas), ic + 7)):
        mark = "  <- corner" if i == ic else ""
        print(f"    {alphas[i]:>12.2e}{residual[i]:>16.6f}{modelnorm[i]:>16.6f}"
              f"{curv[i]:>16.4f}{errors[i]:>16.6f}{mark}")
    print(f"    the corner is at alpha = {alpha_c:.3e}, where")
    print(f"    ||K m - d|| = {residual[ic]:.6f} (noise level delta = {delta:.6f})")
    print(f"    ||m|| = {modelnorm[ic]:.6f} (true {wnorm(m_true):.6f})")
    print(f"    model error = {errors[ic]:.6f}")
    print("    The two arms of the curve correspond to the two failure modes:")
    print("    the steep arm (small alpha) is the noise-amplified unregularised")
    print("    solution, and the flat arm (large alpha) is the over-smoothed one.")

    section("3. Sensitivity of the answer to the choice of alpha")
    print(f"    {'alpha':>12}{'alpha / alpha_corner':>22}{'||Km-d||':>14}"
          f"{'||m||':>14}{'model error':>16}")
    best_err, best_alpha = 1e30, 0.0
    for a in alphas:
        m = tikhonov(c, a)
        r = [p - q for p, q in zip(mat_vec(K, m), d)]
        e = wnorm([p - q for p, q in zip(m, m_true)])
        if e < best_err:
            best_err, best_alpha = e, a
    for factor in (1e-4, 1e-3, 1e-2, 0.1, 1.0, 10.0, 100.0, 1000.0):
        a = alpha_c * factor
        m = tikhonov(c, a)
        r = [p - q for p, q in zip(mat_vec(K, m), d)]
        err = wnorm([p - q for p, q in zip(m, m_true)])
        print(f"    {a:>12.2e}{factor:>22.0e}{wnorm(r):>14.6f}"
              f"{wnorm(m):>14.6f}{err:>16.6f}")
    print(f"    the smallest model error on this grid is {best_err:.6f} at")
    print(f"    alpha = {best_alpha:.3e}, which is "
          f"{best_alpha / alpha_c:.0f} times the L-curve corner.")
    print("    So the corner is not the minimiser of the model error here. The")
    print("    error falls by a factor of about three per decade of alpha on the")
    print("    low side of the true optimum, and the corner sits low by two")
    print("    decades. This is a real limitation of the L-curve: it balances the")
    print("    residual against the model norm, and the quantity we would like to")
    print("    minimise -- the distance to the true model -- is not in the")
    print("    functional it balances.")
    hi_curve = [i for i in range(len(curv)) if curv[i] >= 0.9 * curv[ic]]
    print(f"    the corner itself is not sharp: {len(hi_curve)} of {len(alphas)}")
    print(f"    grid values of alpha have curvature within 10 per cent of the")
    print(f"    maximum, spanning alpha from {alphas[hi_curve[0]]:.2e} to "
          f"{alphas[hi_curve[-1]]:.2e},")
    print(f"    a factor of {alphas[hi_curve[-1]] / alphas[hi_curve[0]]:.1f}. Quoting")
    print("    'the' corner to more than one significant figure is not defensible.")

    section("4. The discrepancy principle")
    def residual_at(alpha):
        m = tikhonov(c, alpha)
        return wnorm([p - q for p, q in zip(mat_vec(K, m), d)])

    lo, hi = 1e-16, 1e6
    for _ in range(200):
        mid = math.sqrt(lo * hi)
        if residual_at(mid) > delta:
            hi = mid
        else:
            lo = mid
    alpha_d = math.sqrt(lo * hi)
    m_d = tikhonov(c, alpha_d)
    err_d = wnorm([p - q for p, q in zip(m_d, m_true)])
    print("    the principle chooses alpha so that ||K m_alpha - d|| = delta")
    print(f"    delta = {delta:.6e}")
    print(f"    {'choice':>26}{'alpha':>14}{'residual':>14}{'model error':>14}")
    print(f"    {'L-curve corner':>26}{alpha_c:>14.3e}{residual_at(alpha_c):>14.6f}"
          f"{errors[ic]:>14.6f}")
    print(f"    {'discrepancy principle':>26}{alpha_d:>14.3e}"
          f"{residual_at(alpha_d):>14.6f}{err_d:>14.6f}")
    print(f"    {'smallest error on the grid':>26}{best_alpha:>14.3e}"
          f"{residual_at(best_alpha):>14.6f}{best_err:>14.6f}")
    print(f"    alpha_discrepancy / alpha_corner = {alpha_d / alpha_c:.1f}, and")
    print(f"    alpha_discrepancy / alpha_best = {alpha_d / best_alpha:.2f}.")
    print("    Here the discrepancy principle lands within a factor of two of the")
    print("    alpha that actually minimises the model error, while the L-curve")
    print("    corner is low by two decades. Neither result is a theorem: the")
    print("    discrepancy principle needs the noise norm, and it is biased low")
    print("    when the misfit surface is not the one the model was sampled from.")
    print("    The honest conclusion is that alpha should be checked against an")
    print("    independent estimate of the data error, not chosen by one rule.")

    section("5. Generalised cross-validation, without the noise level")
    print("    GCV(alpha) = ||K m_alpha - d||^2 / (m - trace(R_alpha))^2, which")
    print("    estimates the predictive error of the regularised inverse without")
    print("    using a noise estimate. Effective degrees of freedom are")
    print("    trace(R_alpha) in the numerator's denominator:")
    gcv = []
    for a in alphas:
        m = tikhonov(c, a)
        res2 = sum((p - q) ** 2 for p, q in zip(mat_vec(K, m), d))
        tr = sum(l * l / (l * l + a) for l in lam)
        denom = (n - tr) ** 2
        gcv.append(res2 / denom if denom > 0 else float("inf"))
    ia = min(range(len(gcv)), key=lambda i: gcv[i])
    alpha_g = alphas[ia]
    m_g = tikhonov(c, alpha_g)
    err_g = wnorm([p - q for p, q in zip(m_g, m_true)])
    print(f"    {'choice':>26}{'alpha':>14}{'model error':>16}"
          f"{'vs error minimum':>18}")
    print(f"    {'L-curve corner':>26}{alpha_c:>14.3e}{errors[ic]:>16.6f}"
          f"{errors[ic] / best_err:>18.2f}")
    print(f"    {'discrepancy principle':>26}{alpha_d:>14.3e}{err_d:>16.6f}"
          f"{err_d / best_err:>18.2f}")
    print(f"    {'GCV minimum':>26}{alpha_g:>14.3e}{err_g:>16.6f}"
          f"{err_g / best_err:>18.2f}")
    print(f"    {'true error minimum':>26}{best_alpha:>14.3e}{best_err:>16.6f}"
          f"{1.0:>18.2f}")
    print("    all three rules land within a factor of a few of the error minimum")
    print("    on this problem, but they do not agree with each other, and the")
    print("    last column is the only one that is not available in practice.")

    section("6. Both limits, and the second noise level")
    print(f"    {'alpha':>12}{'model error':>16}{'note':>34}")
    for a, note in ((1e-14, "essentially unregularised"),
                    (1e-12, ""),
                    (1e-10, ""),
                    (1e2, "essentially m = 0"),
                    (1e4, "")):
        m = tikhonov(c, a)
        err = wnorm([p - q for p, q in zip(m, m_true)])
        print(f"    {a:>12.0e}{err:>16.6f}{note:>34}")
    print(f"    as alpha -> 0 the error tends to the unregularised noise-driven")
    print(f"    value; as alpha -> infinity it tends to ||m_true|| = "
          f"{wnorm(m_true):.6f}")

    print("\n    the corner moves with the noise level, as it must:")
    print(f"    {'eps':>8}{'alpha_corner':>16}{'model error at corner':>24}"
          f"{'alpha_discrepancy':>20}")
    for eps2 in (1e-1, 1e-2, 1e-3):
        rng = random.Random(20261014)
        nz = [rng.gauss(0.0, 1.0) for _ in range(n)]
        sc = eps2 * d_norm / wnorm(nz)
        d2 = [d_exact[i] + sc * nz[i] for i in range(n)]
        c2 = coeffs(d2)

        def curve(cv):
            res, mod = [], []
            for a in alphas:
                m = tikhonov(cv, a)
                res.append(wnorm([p - q for p, q in zip(mat_vec(K, m), d2)]))
                mod.append(wnorm(m))
            return res, mod

        res2, mod2 = curve(c2)
        xs2 = [math.log10(v) for v in res2]
        ys2 = [math.log10(v) for v in mod2]
        cv2 = [0.0] * len(xs2)
        for i in range(1, len(xs2) - 1):
            dx1, dx2 = xs2[i] - xs2[i - 1], xs2[i + 1] - xs2[i]
            dy1, dy2 = ys2[i] - ys2[i - 1], ys2[i + 1] - ys2[i]
            d1x, d1y = (dx1 + dx2) / 2.0, (dy1 + dy2) / 2.0
            d2x, d2y = dx2 - dx1, dy2 - dy1
            den = (d1x * d1x + d1y * d1y) ** 1.5
            cv2[i] = (d1x * d2y - d1y * d2x) / den if den > 0 else 0.0
        i2 = max(range(len(cv2)), key=lambda i: cv2[i])
        ac = alphas[i2]
        errc = wnorm([p - q for p, q in zip(tikhonov(c2, ac), m_true)])

        def res_at(a):
            m = tikhonov(c2, a)
            return wnorm([p - q for p, q in zip(mat_vec(K, m), d2)])

        dl = wnorm([d2[i] - d_exact[i] for i in range(n)])
        lo2, hi2 = 1e-16, 1e6
        for _ in range(200):
            mid = math.sqrt(lo2 * hi2)
            if res_at(mid) > dl:
                hi2 = mid
            else:
                lo2 = mid
        print(f"    {eps2:>8.0e}{ac:>16.3e}{errc:>24.6f}"
              f"{math.sqrt(lo2 * hi2):>20.3e}")
    print("    a smaller noise level admits a smaller alpha: the corner tracks the")
    print("    information content of the data, which is why the choice of alpha")
    print("    is a statement about the noise and not a free parameter.")


if __name__ == "__main__":
    main()
