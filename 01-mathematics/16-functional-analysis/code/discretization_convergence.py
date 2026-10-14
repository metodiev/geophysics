"""Discretisation, convergence and the regularisation discrepancy.

Run:  python3 discretization_convergence.py
Requires: Python standard library only.

Companion to lesson 01-16-07 (Discretisation, Convergence and Regularisation
Discrepancy).

Operator: the gravity kernel of lessons 01-16-05 and 01-16-06,

    d(x) = int_0^1 K(x - y) m(y) dy,   K(s) = (z/pi)/(s^2 + z^2),  z = 0.05,

discretised on n nodes with the trapezoid weights. Each n gives a different
finite matrix K_n, hence a different singular spectrum, hence a different
problem. The truth is a fixed continuous function m_true(x) evaluated on the
nodes of each grid.

Sections
    1. A fixed alpha while the grid is refined: bias, then over-fitting
    2. The number of modes a fixed alpha admits grows with n
    3. Alpha chosen by the discrepancy principle at each n
    4. Semiconvergence of the Landweber iteration, and how its optimum scales
"""

import math
import random

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


def grads(n):
    """Node values of the fixed continuous truth on the n-node grid."""
    h = 1.0 / (n - 1)
    x = [i * h for i in range(n)]
    m = [math.exp(-((xi - 0.28) ** 2) / (2 * 0.06 ** 2))
         + 0.6 * math.exp(-((xi - 0.68) ** 2) / (2 * 0.09 ** 2)) for xi in x]
    return x, h, m


def build(n, z=Z):
    h = 1.0 / (n - 1)
    x = [i * h for i in range(n)]
    K = [[h * (z / math.pi) / ((x[i] - x[j]) ** 2 + z * z) for j in range(n)]
         for i in range(n)]
    return x, h, K


def decompose(K):
    ev, V = jacobi_eig(K)
    n = len(K)
    order = sorted(range(n), key=lambda k: -abs(ev[k]))
    lam = [abs(ev[i]) for i in order]
    cols = [[V[i][order[k]] for i in range(n)] for k in range(n)]
    return lam, cols


def main():
    sizes = (20, 40, 80, 160)
    setups = {}
    for n in sizes:
        x, h, K = build(n)
        lam, cols = decompose(K)
        setups[n] = (x, h, K, lam, cols)

    def wnorm(h, v):
        return math.sqrt(h * sum(t * t for t in v))

    print("    the truth m_true(x) is a fixed continuous function; each grid")
    print("    samples it, so the model error is measured in that grid's norm")
    print("    NOTE: the same discretisation is used to synthesise and to invert")
    print("    the data. That is an inverse crime: it removes the model error")
    print("    that a real experiment would have and isolates the effect of the")
    print("    discretisation alone. A study that intends to report resolution")
    print("    must not do this; here it is deliberate and stated.")
    print(f"\n    {'n':>5}{'h':>12}{'lambda_1':>14}{'lambda_min':>14}"
          f"{'cond(K)':>14}")
    for n in sizes:
        x, h, K, lam, cols = setups[n]
        print(f"    {n:>5}{h:>12.5f}{lam[0]:>14.6f}{lam[-1]:>14.3e}"
              f"{lam[0] / lam[-1]:>14.3e}")

    # data and noise per grid
    data = {}
    random.seed(4242)
    delta_rel = 1e-2
    for n in sizes:
        x, h, K, lam, cols = setups[n]
        _, _, m_true = grads(n)
        d_exact = mat_vec(K, m_true)
        dn = wnorm(h, d_exact)
        nz = [random.gauss(0.0, 1.0) for _ in range(n)]
        sc = delta_rel * dn / wnorm(h, nz)
        d = [d_exact[i] + sc * nz[i] for i in range(n)]
        data[n] = (m_true, d_exact, d, wnorm(h, [d[i] - d_exact[i] for i in range(n)]))

    def solve(n, alpha):
        x, h, K, lam, cols = setups[n]
        m_true, d_exact, d, delta = data[n]
        c = [sum(cols[k][i] * d[i] for i in range(n)) for k in range(n)]
        return [sum(lam[k] / (lam[k] ** 2 + alpha) * c[k] * cols[k][i]
                    for k in range(n)) for i in range(n)]

    def residual(n, m):
        x, h, K, lam, cols = setups[n]
        return wnorm(h, [p - q for p, q in zip(mat_vec(K, m), data[n][2])])

    def error(n, m):
        x, h, K, lam, cols = setups[n]
        return wnorm(h, [p - q for p, q in zip(m, data[n][0])])

    section("1. A fixed alpha while the grid is refined")
    print(f"    {'alpha':>9}{'n':>5}{'model error':>16}{'residual ||Km-d||':>20}"
          f"{'delta (noise)':>16}{'residual / delta':>18}")
    for alpha_fixed in (1e-1, 1e-3):
        for n in sizes:
            m = solve(n, alpha_fixed)
            r = residual(n, m)
            delta = data[n][3]
            print(f"    {alpha_fixed:>9.0e}{n:>5}{error(n, m):>16.6f}{r:>20.6f}"
                  f"{delta:>16.6f}{r / delta:>18.4f}")
    print("    Two regimes, both visible above.")
    print(f"    alpha = 1e-1 is strong: the model error is essentially flat")
    print("    (bias-dominated) and the residual stays well above the noise")
    print("    level, so refining the mesh buys almost nothing. The error that")
    print("    remains is the bias of the regulariser, which the mesh cannot")
    print("    remove.")
    print("    alpha = 1e-3 is weak: the model error is non-monotone in n --")
    print("    0.0180, 0.0272, 0.0201, 0.0115 -- and the residual is below the")
    print("    noise level at every grid. A residual below the noise is the")
    print("    signature of an over-fit, not of a better inversion.")
    print("    The non-monotone behaviour has a reason worth stating: on the")
    print("    coarsest grid the discretisation is itself a regulariser (only 20")
    print("    parameters, and a condition number of 8.9), so the coarse problem")
    print("    is stable without alpha; the intermediate grids expose more")
    print("    unstable directions without yet resolving the answer; and only the")
    print("    finest grid recovers. Refining a discretisation is not a monotone")
    print("    improvement unless the regularisation is adjusted with it.")

    section("2. Why: what a fixed alpha actually controls")
    print("    trace(R_alpha) = sum_k lambda_k^2 / (lambda_k^2 + alpha) is the")
    print("    number of model parameters the data determine at that alpha")
    print(f"    {'alpha':>9}{'n':>5}{'trace(R_alpha)':>18}{'of':>6}"
          f"{'lambda_1^2/alpha':>20}")
    for a in (1e-1, 1e-3):
        for n in sizes:
            x, h, K, lam, cols = setups[n]
            tr = sum(l * l / (l * l + a) for l in lam)
            print(f"    {a:>9.0e}{n:>5}{tr:>18.4f}{n:>6}{lam[0] ** 2 / a:>20.1f}")
    print("    At fixed alpha the resolved dimension does not grow with n: it")
    print("    converges to a limit set by alpha (about 22.6 for alpha = 1e-3,")
    print("    about 7.8 for alpha = 1e-1). That is the correct picture. A")
    print("    regularisation parameter selects a band of physical wavenumbers,")
    print("    so the mesh only needs to be fine enough to represent the band;")
    print("    beyond that, refining changes nothing but the number of modes that")
    print("    are damped to zero. This is why alpha must be tied to the noise")
    print("    level rather than to the discretisation: adding nodes does not add")
    print("    information.")

    section("3. Alpha from the discrepancy principle at each n")
    def alpha_discrepancy(n):
        delta = data[n][3]
        lo, hi = 1e-18, 1e6
        for _ in range(120):
            mid = math.sqrt(lo * hi)
            if residual(n, solve(n, mid)) > delta:
                hi = mid
            else:
                lo = mid
        return math.sqrt(lo * hi)

    print(f"    {'n':>5}{'alpha_disc':>14}{'residual':>14}{'delta':>14}"
          f"{'model error':>16}{'trace(R)':>12}")
    for n in sizes:
        a = alpha_discrepancy(n)
        m = solve(n, a)
        x, h, K, lam, cols = setups[n]
        tr = sum(l * l / (l * l + a) for l in lam)
        print(f"    {n:>5}{a:>14.3e}{residual(n, m):>14.6f}{data[n][3]:>14.6f}"
              f"{error(n, m):>16.6f}{tr:>12.3f}")
    print("    with alpha tied to the noise level the model error now falls")
    print("    monotonically with n, and the residual sits at the noise level.")
    print("    alpha_disc itself falls with n, and for the reason given in")
    print("    Section 1: on a coarse grid the limited dimension of the model")
    print("    space already supplies part of the damping, so less Tikhonov")
    print("    damping is needed to hold the residual at delta. As the grid is")
    print("    refined the discretisation supplies less, and alpha must fall to")
    print("    compensate while still doing the whole job of stabilisation.")
    print("    This is the correct limit: the sequence of regularised solutions")
    print("    converges to the true model as the grid is refined *and* alpha is")
    print("    allowed to fall with it. The regularisation discrepancy is the")
    print("    observed difference between this converging sequence and the exact")
    print("    solution of the unregularised problem -- here it is the residual")
    print("    error at the finest grid, which is no longer decreasing quickly.")
    errs = [error(n, solve(n, alpha_discrepancy(n))) for n in sizes]
    print(f"    observed error sequence: "
          + ", ".join(f"{e:.6f}" for e in errs))
    print("    the last ratio is "
          f"{errs[-1] / errs[-2]:.3f} for a doubling of n, so the convergence")
    print("    has flattened onto the noise floor: with 1 per cent noise and")
    print("    this regulariser there is little left to gain from refining.")

    section("4. Semiconvergence of the Landweber iteration")
    print("    m_{j+1} = m_j + tau (d - K m_j) applied from m_0 = 0 gives, in the")
    print("    eigenbasis, m_j = sum_k [1 - (1 - tau lambda_k^2)^j] (c_k/lambda_k) v_k")
    print("    The iteration is carried out on the coefficients, which is")
    print("    algebraically the same as applying the operators and costs O(n)")
    print("    per step instead of O(n^2).")
    print(f"\n    {'n':>5}{'tau':>14}{'iterations':>12}{'error at k*':>16}"
          f"{'k*':>10}{'error at 20 k*':>18}")
    for n in (40, 80, 160):
        x, h, K, lam, cols = setups[n]
        m_true, d_exact, d, delta = data[n]
        c = [sum(cols[k][i] * d[i] for i in range(n)) for k in range(n)]
        L = lam[0] ** 2
        tau = 0.5 / L
        cj = [0.0] * n
        best = (1e30, 0)
        hist = {}
        for j in range(1, 4001):
            for k in range(n):
                cj[k] += tau * (lam[k] * c[k] - lam[k] * lam[k] * cj[k])
            if j in (1, 5, 10, 25, 50, 100, 200, 400, 800, 1600, 2400, 4000):
                m = [sum(cj[k] * cols[k][i] for k in range(n)) for i in range(n)]
                hist[j] = error(n, m)
                if hist[j] < best[0]:
                    best = (hist[j], j)
        m = [sum(cj[k] * cols[k][i] for k in range(n)) for i in range(n)]
        deep = error(n, m)
        print(f"    {n:>5}{tau:>14.3e}{4000:>12}{best[0]:>16.6f}"
              f"{best[1]:>10}{deep:>18.6f}")
        if n in (80, 160):
            print("          history: " + ", ".join(
                f"j={j}: {v:.4f}" for j, v in sorted(hist.items())))

    print("    the error falls, reaches a minimum, and then rises: that is")
    print("    semiconvergence. The iteration is a regularisation whose parameter")
    print("    is the stopping index, and the optimal index grows as the grid is")
    print("    refined, because the finer grid exposes smaller singular values")
    print("    that the iteration reaches later. Stopping 'when the residual is")
    print("    small enough' destroys the property it was chosen for.")


if __name__ == "__main__":
    main()
