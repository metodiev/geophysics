"""Interpolation: Lagrange, divided differences, splines, the Runge phenomenon.

Run:  python3 interpolation.py
Requires: Python standard library only.

Companion to lesson 01-12-02 (Interpolation, Splines and Approximation Theory).

What is measured here, not asserted:

  * the Lagrange and Newton forms of the interpolating polynomial agree to
    round-off on the same data;
  * equispaced polynomial interpolation of a smooth function diverges as the
    node count grows (the Runge phenomenon), while Chebyshev nodes converge;
  * linear interpolation error is O(h^2), a complete (clamped) cubic spline is
    O(h^4), and a natural cubic spline is O(h^2) in max norm because its
    artificial end conditions are wrong -- an honest case where the textbook
    order for "the spline" depends on which spline is meant;
  * a spline overshoots a step, so it is not a safe default for a layered
    well log without a monotonicity constraint.

Data are SYNTHETIC with exact answers, so every reported error is real error.
"""

import math


def section(title: str) -> None:
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


# ----------------------------------------------------------------------
# Polynomial interpolation
# ----------------------------------------------------------------------

def lagrange(xs, ys, x: float) -> float:
    """Direct Lagrange evaluation. O(n^2), numerically poor for large n."""
    total = 0.0
    n = len(xs)
    for i in range(n):
        term = ys[i]
        for j in range(n):
            if j != i:
                term *= (x - xs[j]) / (xs[i] - xs[j])
        total += term
    return total


def divided_differences(xs, ys):
    """Newton coefficients a_0..a_n from the divided-difference table."""
    n = len(xs)
    coef = list(ys)
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (xs[i] - xs[i - j])
    return coef


def newton_eval(xs, coef, x: float) -> float:
    """Horner evaluation of the Newton form."""
    n = len(coef)
    total = coef[n - 1]
    for i in range(n - 2, -1, -1):
        total = total * (x - xs[i]) + coef[i]
    return total


# ----------------------------------------------------------------------
# Cubic splines
# ----------------------------------------------------------------------

def thomas(a, b, c, d):
    """Solve a tridiagonal system a_i x_{i-1} + b_i x_i + c_i x_{i+1} = d_i."""
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


def spline_second_derivatives(xs, ys, clamped=None):
    """Moments M_i = s''(x_i).

    ``clamped`` is (y'_0, y'_n) for a complete spline; if None, the natural
    conditions M_0 = M_n = 0 are used.
    """
    n = len(xs) - 1
    h = [xs[i + 1] - xs[i] for i in range(n)]
    rhs = [6.0 * ((ys[i + 1] - ys[i]) / h[i] - (ys[i] - ys[i - 1]) / h[i - 1])
           for i in range(1, n)]

    if clamped is None:
        # (n-1) x (n-1) system for M_1 .. M_{n-1}; M_0 = M_n = 0.
        m = n - 1
        if m == 1:
            M = [0.0, -0.0, 0.0] if n == 2 else None
            # single interior equation, solved directly
            b = [2.0 * (h[0] + h[1])] if n >= 2 else []
            if b:
                return [0.0] + [rhs[0] / b[0]] + [0.0]
        a = [0.0] * m
        bb = [0.0] * m
        c = [0.0] * m
        d = [0.0] * m
        for j in range(m):
            i = j + 1
            a[j] = h[i - 1] if j >= 1 else 0.0
            bb[j] = 2.0 * (h[i - 1] + h[i])
            c[j] = h[i] if j <= m - 2 else 0.0
            d[j] = rhs[j]
        interior = thomas(a, bb, c, d)
        return [0.0] + interior + [0.0]

    # Complete spline: (n+1) x (n+1) system for all moments.
    dp0, dpn = clamped
    size = n + 1
    a = [0.0] * size
    bb = [0.0] * size
    c = [0.0] * size
    d = [0.0] * size
    bb[0], c[0] = 2.0, 1.0
    d[0] = 6.0 / h[0] * ((ys[1] - ys[0]) / h[0] - dp0)
    for j in range(1, n):
        a[j] = h[j - 1]
        bb[j] = 2.0 * (h[j - 1] + h[j])
        c[j] = h[j]
        d[j] = rhs[j - 1]
    a[n], bb[n] = 1.0, 2.0
    d[n] = 6.0 / h[n - 1] * (dpn - (ys[n] - ys[n - 1]) / h[n - 1])
    return thomas(a, bb, c, d)


def spline_eval(xs, ys, M, x: float) -> float:
    """Evaluate the cubic spline defined by its moments M at x."""
    n = len(xs) - 1
    # Locate the interval.
    lo, hi = 0, n
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if x < xs[mid]:
            hi = mid
        else:
            lo = mid
    i = min(lo, n - 1)
    h = xs[i + 1] - xs[i]
    b = (ys[i + 1] - ys[i]) / h - h * (2.0 * M[i] + M[i + 1]) / 6.0
    dx = x - xs[i]
    return (ys[i] + b * dx + 0.5 * M[i] * dx ** 2
            + (M[i + 1] - M[i]) / (6.0 * h) * dx ** 3)


def linear_eval(xs, ys, x: float) -> float:
    n = len(xs) - 1
    lo = 0
    for i in range(n):
        if xs[i] <= x <= xs[i + 1]:
            lo = i
            break
    h = xs[lo + 1] - xs[lo]
    t = (x - xs[lo]) / h
    return (1.0 - t) * ys[lo] + t * ys[lo + 1]


# ----------------------------------------------------------------------
# Experiments
# ----------------------------------------------------------------------

def report_equivalence() -> None:
    section("1. Lagrange and Newton forms are the same polynomial")
    xs = [0.0, 1.0, 2.0, 3.0, 4.0]
    ys = [math.exp(x) for x in xs]
    coef = divided_differences(xs, ys)
    print(f"  divided-difference coefficients: "
          f"{' '.join(f'{c:.6f}' for c in coef)}")
    worst = 0.0
    for k in range(41):
        x = 4.0 * k / 40.0
        a = lagrange(xs, ys, x)
        b = newton_eval(xs, coef, x)
        worst = max(worst, abs(a - b))
    print(f"  max |Lagrange - Newton| on 41 points = {worst:.3e}")
    print("  They are algebraically identical; the difference is round-off.")
    print(f"  At x = 4.0 both reproduce exp(4) = {math.exp(4.0)!r}:")
    print(f"    Lagrange {lagrange(xs, ys, 4.0)!r}   "
          f"Newton {newton_eval(xs, coef, 4.0)!r}")
    print("  => restating interpolation as a basis choice does not change the")
    print("     interpolant; it changes the stability of computing it.")


def report_runge() -> None:
    section("2. Runge phenomenon: equispaced nodes diverge, Chebyshev converge")
    f = lambda x: 1.0 / (1.0 + 25.0 * x * x)
    probe = [math.cos(math.pi * k / 400.0) for k in range(401)]
    print(f"  f(x) = 1/(1 + 25 x^2) on [-1, 1], max error on a 401-point grid")
    print(f"  {'n':>4}{'uniform':>16}{'Chebyshev':>16}")
    for n in (4, 8, 12, 16, 20, 24):
        xu = [-1.0 + 2.0 * k / n for k in range(n + 1)]
        xc = [-math.cos(math.pi * k / n) for k in range(n + 1)]
        eu = max(abs(newton_eval(xu, divided_differences(xu, [f(x) for x in xu]), x) - f(x))
                 for x in probe)
        ec = max(abs(newton_eval(xc, divided_differences(xc, [f(x) for x in xc]), x) - f(x))
                 for x in probe)
        print(f"  {n:>4}{eu:>16.3e}{ec:>16.3e}")
    print("  Uniform error GROWS with n: the interpolant develops violent")
    print("  oscillations near the ends. Clustering nodes toward the ends")
    print("  (Chebyshev) removes the growth and gives error ~ 1e-2 or better.")
    print("  The lesson: 'add more data points' is not a convergence strategy")
    print("  when the node distribution is the problem.")


def report_spline_orders() -> None:
    section("3. Measured convergence orders: linear, natural, clamped spline")
    f = math.exp
    print("  f(x) = exp(x) on [0, 1]; max error over 20 points per interval")
    print(f"  {'nodes':>6}{'h':>10}{'linear':>12}{'natural':>12}{'clamped':>12}"
          f"{'  orders':>22}")
    prev = None
    for n in (8, 16, 32, 64, 128, 256):
        xs = [k / n for k in range(n + 1)]
        ys = [f(x) for x in xs]
        grid = [k / (20.0 * n) for k in range(20 * n + 1)]
        el = max(abs(linear_eval(xs, ys, x) - f(x)) for x in grid)
        Mn = spline_second_derivatives(xs, ys)
        en = max(abs(spline_eval(xs, ys, Mn, x) - f(x)) for x in grid)
        Mc = spline_second_derivatives(xs, ys, clamped=(f(0.0), f(1.0)))
        ec = max(abs(spline_eval(xs, ys, Mc, x) - f(x)) for x in grid)
        row = f"  {n:>6}{1.0 / n:>10.4f}{el:>12.3e}{en:>12.3e}{ec:>12.3e}"
        if prev is not None:
            ol = math.log(prev[0] / el) / math.log(2.0)
            on = math.log(prev[1] / en) / math.log(2.0)
            oc = math.log(prev[2] / ec) / math.log(2.0)
            row += f"   {ol:>5.2f} {on:>5.2f} {oc:>5.2f}"
        print(row)
        prev = (el, en, ec)
    print("  Measured max-norm orders: linear 2.0, natural 2.0, clamped 4.0.")
    print("  Why the natural spline disappoints: setting s''=0 at the ends is an")
    print("  assumption about the function, not a fact about it. For exp the")
    print("  true curvature at the ends is 1, so the assumption is wrong and the")
    print("  error near x=0 and x=1 is O(h^2) -- the boundary error, not the")
    print("  interior stencil, controls the max norm.")
    print("\n  Natural spline, same nodes, max error over an interior window")
    print("  and over the whole interval:")
    gmid = [0.25 + 0.5 * k / 400.0 for k in range(401)]
    print(f"    {'nodes':>6}{'interior [0.25,0.75]':>24}{'order':>8}"
          f"{'whole interval':>18}{'order':>8}")
    prev = None
    for n in (16, 32, 64, 128, 256, 512):
        xs = [k / n for k in range(n + 1)]
        ys = [f(x) for x in xs]
        Mn = spline_second_derivatives(xs, ys)
        e_int = max(abs(spline_eval(xs, ys, Mn, x) - f(x)) for x in gmid)
        gi = [k / (10.0 * n) for k in range(10 * n + 1)]
        e_all = max(abs(spline_eval(xs, ys, Mn, x) - f(x)) for x in gi)
        line = f"    {n:>6}{e_int:>24.3e}"
        if prev is None:
            line += f"{'  -':>8}{e_all:>18.3e}{'  -':>8}"
        else:
            line += (f"{math.log(prev[0] / e_int) / math.log(2.0):>8.2f}"
                     f"{e_all:>18.3e}"
                     f"{math.log(prev[1] / e_all) / math.log(2.0):>8.2f}")
        print(line)
        prev = (e_int, e_all)
    print("  The interior error settles at order 4 while the max norm stays at")
    print("  order 2: the O(h^2) boundary layer *is* the global error, and the")
    print("  pre-asymptotic columns above n=32 show the layer separating from")
    print("  the window. Quote the order with the window it was measured on.")


def report_overshoot() -> None:
    section("4. A spline overshoots a step: not a safe default for layered logs")
    xs = [0.0, 0.25, 0.5, 0.75, 1.0]
    ys = [0.0, 0.0, 1.0, 1.0, 1.0]
    M = spline_second_derivatives(xs, ys)
    grid = [k / 1000.0 for k in range(1001)]
    vals = [spline_eval(xs, ys, M, x) for x in grid]
    worst = max(vals)
    where = grid[vals.index(worst)]
    print(f"  data at depths 0, 0.25, 0.5, 0.75, 1.0: {ys}")
    print(f"  spline maximum      = {worst:.6f} at x = {where:.3f}")
    print(f"  overshoot above the largest datum (1.0) = {worst - 1.0:.6f}")
    print(f"  undershoot below the smallest datum (0.0) = "
          f"{min(vals):.6f}")
    print("  The interpolant leaves the range of the data. For a measured")
    print("  quantity that cannot do that (a porosity, a concentration, a")
    print("  monotone velocity), a shape-preserving scheme is required, not")
    print("  the smooth interpolant that minimises curvature.")


def main() -> None:
    report_equivalence()
    report_runge()
    report_spline_orders()
    report_overshoot()
    section("Summary")
    print("polynomial : high order in theory, unstable for many equispaced nodes")
    print("Chebyshev  : the node choice that makes high order work")
    print("linear     : order 2, no overshoot, needs many nodes")
    print("clamped    : order 4 when the end slopes are known")
    print("natural    : order 4 inside, order 2 at the ends")
    print("extrapolation beyond the data is never justified by any of them")


if __name__ == "__main__":
    main()
