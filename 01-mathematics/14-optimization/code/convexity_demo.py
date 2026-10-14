"""Convexity, stationarity and optimality conditions, checked numerically.

Run:  python3 convexity_demo.py
Requires: Python standard library only.

Companion to lesson 01-14-01.

The lesson claims that a convex objective has one answer while a non-convex one
can have many, and that non-uniqueness in an inverse problem is the flat-valley
version of the same geometry. Every number these claims rest on is printed here:
the chord test for convexity, Hessian spectra as curvature, the second-order
optimality condition, a saddle that satisfies the first-order condition, and a
rank-deficient data kernel whose misfit is exactly constant along a direction in
model space.
"""

import math

Vector = list[float]
Matrix = list[list[float]]


def section(title: str) -> None:
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


# --------------------------------------------------------------------------
# Small dense linear algebra (standard library only)
# --------------------------------------------------------------------------

def matmul(a: Matrix, b: Matrix) -> Matrix:
    n, k, m = len(a), len(b), len(b[0])
    return [[sum(a[i][t] * b[t][j] for t in range(k)) for j in range(m)]
            for i in range(n)]


def transpose(a: Matrix) -> Matrix:
    return [list(row) for row in zip(*a)]


def matvec(a: Matrix, x: Vector) -> Vector:
    return [sum(a[i][j] * x[j] for j in range(len(x))) for i in range(len(a))]


def dot(x: Vector, y: Vector) -> float:
    return sum(a * b for a, b in zip(x, y))


def norm(x: Vector) -> float:
    return math.sqrt(dot(x, x))


def sub(x: Vector, y: Vector) -> Vector:
    return [a - b for a, b in zip(x, y)]


def solve(a: Matrix, b: Vector) -> Vector:
    """Gaussian elimination with partial pivoting."""
    n = len(a)
    m = [row[:] + [b[i]] for i, row in enumerate(a)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(m[r][col]))
        if abs(m[pivot][col]) < 1e-300:
            raise ZeroDivisionError(f"singular at column {col}")
        m[col], m[pivot] = m[pivot], m[col]
        for r in range(col + 1, n):
            factor = m[r][col] / m[col][col]
            for c in range(col, n + 1):
                m[r][c] -= factor * m[col][c]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (m[i][n] - sum(m[i][j] * x[j] for j in range(i + 1, n))) / m[i][i]
    return x


def symmetric_eigenvalues(a: Matrix, sweeps: int = 100) -> Vector:
    """Eigenvalues of a symmetric matrix by the cyclic Jacobi method."""
    n = len(a)
    w = [[float(x) for x in row] for row in a]
    for _ in range(sweeps):
        off = math.sqrt(sum(w[i][j] ** 2 for i in range(n) for j in range(n)
                           if i != j))
        if off < 1e-14:
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


# --------------------------------------------------------------------------
# Test functions
# --------------------------------------------------------------------------

def chord_violation(f, lo: float, hi: float, steps: int = 120) -> float:
    """Largest violation of f(t*x+(1-t)*y) <= t*f(x)+(1-t)*f(y)."""
    xs = [lo + (hi - lo) * i / (steps - 1) for i in range(steps)]
    worst = -math.inf
    for x in xs:
        for y in xs:
            for t in (0.25, 0.5, 0.75):
                worst = max(worst, f(t * x + (1.0 - t) * y)
                            - (t * f(x) + (1.0 - t) * f(y)))
    return worst


def jensen_probe(f, lo: float, hi: float, n: int = 2000) -> tuple[float, float]:
    """Compare E[f(X)] with f(E[X]) for X uniform on [lo, hi]."""
    step = (hi - lo) / n
    mean = sum(lo + (i + 0.5) * step for i in range(n)) / n
    mean_f = sum(f(lo + (i + 0.5) * step) for i in range(n)) / n
    return mean_f, f(mean)


def bimodal(m: float) -> float:
    """Misfit with two wells; m is a layer thickness in km (SYNTHETIC)."""
    return m ** 4 - 2.0 * m ** 2 + 0.3 * m


def bimodal_grad(m: float) -> float:
    return 4.0 * m ** 3 - 4.0 * m + 0.3


def bimodal_hess(m: float) -> float:
    return 12.0 * m ** 2 - 4.0


def newton_1d(grad, hess, start: float, tol: float = 1e-13,
              max_iter: int = 100) -> tuple[float, int]:
    """Newton in one dimension, used purely to locate stationary points."""
    m = start
    for k in range(max_iter):
        g = grad(m)
        if abs(g) < tol:
            return m, k
        m = m - g / hess(m)
    return m, max_iter


def cycle_skipped_misfit(v: float, v_true: float = 3.0, period: float = 0.5) -> float:
    """Synthetic cycle-skipped seismic misfit over a 2-layer velocity model.

    Predicted travel time at offset x (km): t = x/2 + x^2/(4v), with v in km/s.
    The misfit is the sum of (1 - cos(2 pi dt / period)) over the offsets
    x = 1, 2, 3, 4 km, with the period fixed at 0.5 s. Cosine wrapping creates
    extra minima, which is what an oscillatory seismic misfit does whenever the
    observed and predicted arrivals differ by more than half a period.
    """
    total = 0.0
    for x in (1.0, 2.0, 3.0, 4.0):
        t_pred = x / 2.0 + x ** 2 / (4.0 * v)
        t_obs = x / 2.0 + x ** 2 / (4.0 * v_true)
        total += 1.0 - math.cos(2.0 * math.pi * (t_obs - t_pred) / period)
    return total


def main() -> None:
    section("1. The chord test: does the defining inequality hold?")

    cases = [
        ("f(x) = x^2                     convex", lambda x: x * x, -2.0, 2.0),
        ("f(x) = exp(x)                  convex", math.exp, -1.0, 1.0),
        ("f(x) = cosh(x)                 convex", math.cosh, -1.0, 1.0),
        ("f(x) = 1-cos(x) on [-1.5,1.5]  convex", lambda x: 1.0 - math.cos(x), -1.5, 1.5),
        ("f(x) = 1-cos(x) on [-3,3]      NOT", lambda x: 1.0 - math.cos(x), -3.0, 3.0),
        ("f(x) = x^4 - 3x^2              NOT", lambda x: x ** 4 - 3.0 * x * x, -2.0, 2.0),
        ("f(x) = sin(x) on [0,pi]        NOT", math.sin, 0.0, math.pi),
    ]
    print(f"  {'function':<40}{'max violation':>16}{'verdict':>14}")
    for name, f, lo, hi in cases:
        v = chord_violation(f, lo, hi)
        verdict = "convex" if v <= 1e-12 else "NOT convex"
        print(f"  {name:<40}{v:>16.6e}{verdict:>14}")

    print("\n  Jensen's inequality E[f(X)] >= f(E[X]) for X ~ U[0,1]:")
    for name, f in (("f(x) = x^2", lambda x: x * x),
                    ("f(x) = exp(x)", math.exp),
                    ("f(x) = -x^2 (concave)", lambda x: -x * x)):
        lhs, rhs = jensen_probe(f, 0.0, 1.0)
        print(f"    {name:<24} E[f(X)] = {lhs:.6f}   f(E[X]) = {rhs:.6f}"
              f"   gap = {lhs - rhs:+.6f}")

    section("2. Curvature: the Hessian spectrum is the local geometry")

    quadratics = {
        "A = diag(1, 3)": [[1.0, 0.0], [0.0, 3.0]],
        "A = diag(1, 100)": [[1.0, 0.0], [0.0, 100.0]],
        "rotated, kappa = 100": [[50.5, -49.5], [-49.5, 50.5]],
        "A = diag(1, -1) (saddle)": [[1.0, 0.0], [0.0, -1.0]],
    }
    print(f"  {'quadratic form':<28}{'eigenvalues':>26}{'min':>10}{'kappa':>10}")
    for name, a in quadratics.items():
        eigs = symmetric_eigenvalues(a)
        kmax, kmin = max(eigs), min(eigs)
        kappa = kmax / kmin if kmin > 0 else float("inf")
        text = "(" + ", ".join(f"{e:9.4f}" for e in eigs) + ")"
        print(f"  {name:<28}{text:>26}{kmin:>10.4f}{kappa:>10.2f}")

    # A five-ray cross-hole kernel: SYNTHETIC path lengths in km.
    g = [[1.00, 1.00, 0.00],
         [1.00, 1.02, 0.00],
         [0.50, 0.50, 1.00],
         [0.00, 0.00, 1.00],
         [0.50, 0.50, 0.50]]
    d = [0.0310, 0.0296, 0.0620, 0.0300, 0.0460]     # residuals, s
    ata, atd = matmul(transpose(g), g), matvec(transpose(g), d)
    eigs = symmetric_eigenvalues(ata)
    m_star = solve(ata, atd)
    grad_star = sub(matvec(ata, m_star), atd)

    def misfit(m: Vector) -> float:
        r = sub(matvec(g, m), d)
        return 0.5 * dot(r, r)

    misfit_star = misfit(m_star)
    print("\n  Five-ray, three-cell cross-hole kernel (SYNTHETIC travel times):")
    print(f"    eigenvalues of G^T G  = ({eigs[2]:.6f}, {eigs[1]:.6f}, {eigs[0]:.6f})")
    print(f"    all positive?           {all(e > 0 for e in eigs)}")
    print(f"    condition number        {eigs[2] / eigs[0]:.4f}")
    print(f"    ||grad phi(m*)||        {norm(grad_star):.3e}   (first-order condition)")
    print(f"    m* (s/km)               ({m_star[0]:+.10f}, {m_star[1]:+.10f},"
          f" {m_star[2]:+.10f})")
    print(f"    misfit at m*            {misfit_star:+.10e}")

    direction = [0.13, -0.71, 0.42]
    worst = -math.inf
    curvature = dot(direction, matvec(ata, direction))
    for k in range(-100, 101):
        t = k / 100.0
        m = [m_star[i] + t * direction[i] for i in range(3)]
        chord = misfit_star + 0.5 * t * t * curvature
        worst = max(worst, misfit(m) - chord)
    print(f"    misfit along a random direction: exact quadratic, so the chord")
    print(f"    test in that direction is violated by at most {worst:.3e}")

    section("3. A non-convex misfit has several answers")

    lo, hi, n = -1.8, 1.8, 36001
    grid = [lo + (hi - lo) * i / (n - 1) for i in range(n)]
    values = [bimodal(m) for m in grid]
    local = [(grid[i], values[i]) for i in range(1, n - 1)
             if values[i] < values[i - 1] and values[i] <= values[i + 1]]
    print("  grid-search local minima of f(m) = m^4 - 2m^2 + 0.3m:")
    for m, v in local:
        print(f"    m = {m:+.6f} km   f = {v:+.8f}   f''(m) = {bimodal_hess(m):+.6f}")
    print(f"    number of local minima on [{lo}, {hi}]: {len(local)}")
    print("    grid spacing: "
          f"{hi - lo:.0f}/{n - 1} = {(hi - lo) / (n - 1):.3e} km")

    print("\n  Newton from three starting models:")
    print('  {:>8}{:>18}{:>16}{:>12}{:>7}'.format("start", "critical point",
                                                   "f value", "f''", "iters"))
    for start in (-1.5, 0.0, 1.5):
        m, iters = newton_1d(bimodal_grad, bimodal_hess, start)
        kind = "minimum" if bimodal_hess(m) > 0 else "maximum"
        print(f"  {start:>8.2f}{m:>18.8f}{bimodal(m):>16.8f}"
              f"{bimodal_hess(m):>12.6f}{iters:>7d}  {kind}")
    print("  Two different minima, and one local maximum: a local method converges")
    print("  to whichever critical point is in reach, so the model it returns")
    print("  depends on where the search started.")

    section("4. Non-uniqueness is a flat valley in the objective")

    g_rank = [[1.0, 1.0, 0.0], [1.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
    d_rank = [0.030, 0.030, 0.062]
    null = [1.0, -1.0, 0.0]              # direction the survey is blind to
    m0 = [0.030, 0.0, 0.062]
    print("  kernel with a duplicated ray (columns 1 and 2 identical):")
    print(f"  {'alpha':>7}{'model (km/s)':>40}{'misfit':>14}{'||m||':>12}")
    for alpha in (-2.0, -1.0, 0.0, 1.0, 2.0):
        m = [m0[i] + alpha * null[i] for i in range(3)]
        misfit = 0.5 * sum((a - b) ** 2 for a, b in zip(matvec(g_rank, m), d_rank))
        text = "(" + ", ".join(f"{v:+.4f}" for v in m) + ")"
        print(f"  {alpha:>7.1f}{text:>40}{misfit:>14.3e}{norm(m):>12.6f}")
    print(f"  G n = {matvec(g_rank, null)}  -> the null vector is annihilated by G")
    print("  Misfit is identical (to round-off) for every alpha: rank deficiency")
    print("  rendered as a flat direction of the objective.")

    section("5. First-order versus second-order optimality")

    m_star_1d, _ = newton_1d(bimodal_grad, bimodal_hess, 1.2)
    print(f"  stationary point m*        {m_star_1d:.12f}")
    print(f"  gradient there             {bimodal_grad(m_star_1d):+.3e}  first order OK")
    print(f"  curvature there            {bimodal_hess(m_star_1d):+.8f}  second order OK")

    eigs_s = symmetric_eigenvalues([[1.0, 0.0], [0.0, -1.0]])
    print("\n  A saddle: f(x, y) = x^2 - y^2, gradient zero at the origin")
    print("    ||grad f(0,0)||         0.0")
    print(f"    Hessian eigenvalues     ({eigs_s[0]:+.4f}, {eigs_s[1]:+.4f})")
    print("    The first-order condition holds and the point is not a minimum:")
    print("    stationarity alone certifies nothing about the type of critical point.")

    ata_rank = matmul(transpose(g_rank), g_rank)
    eigs_rank = symmetric_eigenvalues(ata_rank)
    zeros = sum(1 for e in eigs_rank if abs(e) < 1e-9)
    print(f"\n  Rank-deficient kernel, eigenvalues of G^T G = "
          f"({eigs_rank[0]:.6f}, {eigs_rank[1]:.6f}, {eigs_rank[2]:.6f})")
    print(f"    zero eigenvalues: {zeros}  -> convex but not strictly convex,")
    print("    so the minimiser exists but is not unique.")

    section("6. The same geometry in a seismic misfit")

    lo, hi, n = 1.5, 8.0, 65001
    grid = [lo + (hi - lo) * i / (n - 1) for i in range(n)]
    vals = [cycle_skipped_misfit(v) for v in grid]
    minima = [(grid[i], vals[i]) for i in range(1, n - 1)
              if vals[i] < vals[i - 1] and vals[i] <= vals[i + 1]]
    best = min(range(n), key=lambda i: vals[i])
    print("  synthetic cycle-skipped misfit for a 2-layer velocity (SYNTHETIC):")
    print("    true velocity             3.000 km/s")
    print(f"    local minima on [{lo}, {hi}]: {len(minima)}")
    for v, val in minima:
        print(f"      v = {v:8.5f} km/s   misfit = {val:.6f}")
    print(f"    grid minimum              v = {grid[best]:.5f} km/s"
          f"   misfit = {vals[best]:.3e}")
    # Local descent from a bad start, to show the basin it lands in.
    v, step = 5.0, 0.005
    for _ in range(40000):
        g = (cycle_skipped_misfit(v + step) - cycle_skipped_misfit(v - step)) / (2.0 * step)
        v -= 0.001 * g
    print(f"    descent from v = 5.0     v = {v:.5f} km/s"
          f"   misfit = {cycle_skipped_misfit(v):.6f}  (a local minimum)")
    print("    The global minimum sits exactly at the true velocity, but it is one")
    print("    basin among four, and a local method started above 4 km/s converges")
    print("    to the local minimum at 4.76230 km/s instead.")


if __name__ == "__main__":
    main()
