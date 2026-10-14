"""Root finding: bisection, Newton, secant and a robust hybrid.

Run:  python3 root_finding.py
Requires: Python standard library only.

Companion to lesson 01-12-01 (Root Finding).

Four algorithms are implemented from scratch and run on the same problems. The
convergence order is *measured* from the error sequence rather than asserted,
so every order quoted in the lesson is reproducible by running this file.

Geophysical framing:

  * a hypocentre location problem -- inverting a set of arrival-time relations
    for (x, y, origin time) with Newton's method on a residual vector;
  * solving a Murnaghan equation of state for the volume at a given pressure;
  * a classic two-cycle failure of Newton's method that a bracketing safeguard
    repairs.

All numerical examples are SYNTHETIC with an exactly known answer, so the
reported error is real error and not a difference between two approximations.
"""

import math


def section(title: str) -> None:
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


# ----------------------------------------------------------------------
# Algorithms
# ----------------------------------------------------------------------

def bisection(f, a: float, b: float, tol: float = 1e-16, maxit: int = 200):
    """Bracketing root find: halve [a, b] until the interval is below tol.

    Returns (root, iterations, half_width_history). Linear convergence with
    rate exactly 0.5 in the interval width.
    """
    fa = f(a)
    fb = f(b)
    if fa == 0.0:
        return a, 0, [0.0]
    if fb == 0.0:
        return b, 0, [0.0]
    if fa * fb > 0.0:
        raise ValueError("f(a) and f(b) must have opposite signs")
    widths = []
    for k in range(1, maxit + 1):
        mid = 0.5 * (a + b)
        fm = f(mid)
        widths.append(0.5 * (b - a))
        if fm == 0.0 or 0.5 * (b - a) < tol:
            return mid, k, widths
        if (fa < 0.0) != (fm < 0.0):
            b = mid
        else:
            a, fa = mid, fm
    return 0.5 * (a + b), maxit, widths


def newton(f, df, x0: float, tol: float = 1e-14, maxit: int = 60):
    """Newton-Raphson. Quadratic near a simple root, local, not guaranteed.

    The stopping test is on the *relative step size*, not on the residual: a
    residual test needs a tolerance scaled to the units of f, which is easy to
    get wrong (a pressure residual in pascals is a very different number from
    the same residual in gigapascals).
    """
    x = x0
    xs = [x]
    for _ in range(maxit):
        fx = f(x)
        if fx == 0.0:
            break
        dfx = df(x)
        if dfx == 0.0:
            raise ZeroDivisionError("vanishing derivative")
        x_new = x - fx / dfx
        xs.append(x_new)
        if abs(x_new - x) <= tol * (1.0 + abs(x_new)):
            break
        x = x_new
    return xs[-1], xs


def secant(f, x0: float, x1: float, tol: float = 1e-15, maxit: int = 80):
    """Secant method: a chord replaces the derivative. Order ~1.618."""
    xs = [x0, x1]
    for _ in range(maxit):
        f0, f1 = f(xs[-2]), f(xs[-1])
        if f1 == f0:
            break
        x2 = xs[-1] - f1 * (xs[-1] - xs[-2]) / (f1 - f0)
        xs.append(x2)
        if abs(f(x2)) < tol:
            break
    return xs[-1], xs


def hybrid(f, df, a: float, b: float, x0=None, tol: float = 1e-15,
           maxit: int = 200):
    """Safeguarded Newton: take Newton steps while they stay inside a shrinking
    bracket, otherwise take a bisection step. Returns (root, iterations, kind
    history) where kind is 'N' or 'B'."""
    fa, fb = f(a), f(b)
    if fa * fb > 0.0:
        raise ValueError("bracket required")
    x = 0.5 * (a + b) if x0 is None else x0
    kinds = []
    for _ in range(maxit):
        fx = f(x)
        if fx == 0.0:
            break
        # Accept a Newton step only if it lands strictly inside the bracket.
        dfx = df(x)
        xn = x - fx / dfx if dfx != 0.0 else 0.5 * (a + b)
        if not (min(a, b) < xn < max(a, b)):
            xn = 0.5 * (a + b)
            kinds.append("B")
        else:
            kinds.append("N")
        # Maintain the bracket.
        if (fa < 0.0) != (fx < 0.0):
            b = x
        else:
            a, fa = x, fx
        x = xn
        if abs(b - a) < tol:
            break
    return x, len(kinds), kinds


def observed_orders(errors):
    """Given error e_k -> 0, return [(k, p)] with p = log(e_{k+1}/e_k)/log(e_k/e_{k-1}).

    Only defined while the errors decrease by a sensible factor; entries where
    the ratio is not informative are reported as None.
    """
    out = []
    for k in range(1, len(errors) - 1):
        e0, e1, e2 = errors[k - 1], errors[k], errors[k + 1]
        if e0 > 0.0 and e1 > 0.0 and e2 > 0.0 and e1 != e0:
            denom = math.log(e1 / e0)
            if denom != 0.0:
                out.append((k, math.log(e2 / e1) / denom))
                continue
        out.append((k, None))
    return out


def gauss_solve(a, b):
    """Solve a small dense system by Gaussian elimination with partial pivoting.

    ``a`` is a list of rows (modified in place), ``b`` the right-hand side.
    Used here only for the 3x3 normal equations of the location problem.
    """
    n = len(b)
    a = [row[:] for row in a]
    b = b[:]
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(a[r][col]))
        if abs(a[pivot][col]) < 1e-300:
            raise ZeroDivisionError("singular system")
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            b[col], b[pivot] = b[pivot], b[col]
        for r in range(col + 1, n):
            factor = a[r][col] / a[col][col]
            for c in range(col, n):
                a[r][c] -= factor * a[col][c]
            b[r] -= factor * b[col]
    x = [0.0] * n
    for r in range(n - 1, -1, -1):
        s = b[r] - sum(a[r][c] * x[c] for c in range(r + 1, n))
        x[r] = s / a[r][r]
    return x


# ----------------------------------------------------------------------
# 1. Three methods, one root, measured orders
# ----------------------------------------------------------------------

def report_orders() -> None:
    section("1. One root, three algorithms, measured convergence orders")
    f = lambda x: math.cos(x) - x
    df = lambda x: -math.sin(x) - 1.0
    # Reference root to machine precision by exhaustive bisection.
    root, _, _ = bisection(f, 0.0, 1.0, tol=0.0, maxit=200)
    print(f"f(x) = cos(x) - x ;  reference root = {root!r}")

    print("\nBisection on [0, 1]: interval width halves exactly at every step")
    r, it, widths = bisection(f, 0.0, 1.0, tol=1e-15)
    print(f"  iterations = {it},  final error = {abs(r - root):.3e}")
    print("  widths k = 1..8:", " ".join(f"{w:.3e}" for w in widths[:8]))
    ratios = [widths[k] / widths[k - 1] for k in range(1, min(8, len(widths)))]
    print("  width ratio (should be 0.5):",
          " ".join(f"{q:.3f}" for q in ratios))
    print("  => order 1: each halving buys one binary digit, not one digit.")

    print("\nNewton from x0 = 0.0:")
    r, xs = newton(f, df, 0.0)
    errs = [abs(x - root) for x in xs]
    print(f"  iterations = {len(xs) - 1},  final error = {errs[-1]:.3e}")
    for k, e in enumerate(errs):
        print(f"    k={k:>2}  x={xs[k]:.16f}  |x-root|={e:.3e}")
    print("  observed order p from consecutive error triples:")
    for k, p in observed_orders(errs):
        if p is not None and errs[k] > 1e-14:
            print(f"    k={k:>2}  p={p:.3f}")

    print("\nSecant from x0 = 0.0, x1 = 1.0 (no derivative used):")
    r, xs = secant(f, 0.0, 1.0)
    errs = [abs(x - root) for x in xs]
    print(f"  iterations = {len(xs) - 1},  final error = {errs[-1]:.3e}")
    print("  observed order p:")
    for k, p in observed_orders(errs):
        if p is not None and 1e-16 < errs[k] < 1e-1:
            print(f"    k={k:>2}  p={p:.3f}")
    print("  Theory: p solves p^2 = p + 1, so p = (1+sqrt(5))/2 = 1.618034.")
    print("  The measured orders scatter about 1.62 as the iterates approach")
    print("  the root; a single-step order estimate is noisy by construction.")


# ----------------------------------------------------------------------
# 2. Newton's famous two-cycle
# ----------------------------------------------------------------------

def report_cycle() -> None:
    section("2. Newton can cycle: f(x) = x^3 - 2x + 2 from x0 = 0")
    f = lambda x: x ** 3 - 2.0 * x + 2.0
    df = lambda x: 3.0 * x ** 2 - 2.0
    print("  x -> x - f/f':  0 -> 1 -> 0 -> 1 -> ...  forever")
    seq = []
    x = 0.0
    for _ in range(8):
        seq.append(x)
        x = x - f(x) / df(x)
    print("  orbit:", " -> ".join(f"{v:.6f}" for v in seq))
    print("\n  The same equation is a real cubic with one real root:")
    r, _, _ = bisection(f, -3.0, 0.0)
    print(f"    true root = {r!r}")
    print("  A bracketing safeguard (hybrid) started at the SAME x0 = 0.0,")
    print("  with the bracket [-3, 0], finds it:")
    rh, it, kinds = hybrid(f, df, -3.0, 0.0, x0=0.0)
    print(f"    hybrid root = {rh!r},  error = {abs(rh - r):.3e},  steps = {it}")
    print("  step kinds (N=Newton, B=bisection):", "".join(kinds))
    print("  => one bisection step escapes the cycle, then Newton takes over.")


# ----------------------------------------------------------------------
# 3. Equation of state
# ----------------------------------------------------------------------

def report_eos() -> None:
    section("3. Solving an equation of state for volume at fixed pressure")
    print("  Murnaghan EOS:  P(V) = (K0/K0') * ((V0/V)^K0' - 1)")
    print("  Parameters are ILLUSTRATIVE, not a measured mineral:")
    k0 = 130.0e9          # Pa
    k0p = 4.0
    v0 = 1.0              # normalised volume
    p_target = 20.0e9     # Pa

    def pressure(v):
        return (k0 / k0p) * ((v0 / v) ** k0p - 1.0)

    # Analytic solution of the EOS for V:  V = V0 * (1 + K0' P / K0)^(-1/K0')
    v_exact = v0 * (1.0 + k0p * p_target / k0) ** (-1.0 / k0p)
    print(f"  target pressure      = {p_target:.3e} Pa")
    print(f"  analytic volume      = {v_exact!r}")

    r, it, widths = bisection(lambda v: pressure(v) - p_target, 0.5, 1.0,
                              tol=1e-16)
    print(f"  bisection: V = {r!r},  error = {abs(r - v_exact):.3e},  "
          f"iterations = {it}")
    rn, xs = newton(lambda v: pressure(v) - p_target,
                    lambda v: -(k0 / v) * (v0 / v) ** k0p, 0.9)
    print(f"  Newton:    V = {rn!r},  error = {abs(rn - v_exact):.3e},  "
          f"iterations = {len(xs) - 1}")
    errs = [abs(x - v_exact) for x in xs]
    for k, p in observed_orders(errs):
        if p is not None and 1e-16 < errs[k] < 1e-2:
            print(f"    observed order at k={k}: p={p:.3f}")
    print(f"  relative volume change = {(v0 - v_exact) / v0:.6%} at "
          f"{p_target / 1e9:.1f} GPa")

    print("\n  Now start Newton at a physically absurd volume, V = 2.0:")
    f2 = pressure(2.0) - p_target
    df2 = -(k0 / 2.0) * (v0 / 2.0) ** k0p
    print("  the first Newton correction is")
    print(f"    f(2.0) = {f2:.4e} Pa,  f'(2.0) = {df2:.4e} Pa,  "
          f"step = {-f2 / df2:+.4f}")
    print(f"  which lands at V = {2.0 - f2 / df2:+.4f}: far outside any "
          "physical range,") 
    print("  and the second correction is worse still. An unsafeguarded Newton")
    print("  iteration is a local method with no obligation to stay physical.")
    print("  A safeguarded hybrid started at V = 2.0 with the bracket")
    print("  [0.5, 1.0] rejects that step and bisects instead:")
    rh, it, kinds = hybrid(lambda v: pressure(v) - p_target,
                           lambda v: -(k0 / v) * (v0 / v) ** k0p,
                           0.5, 1.0, x0=2.0)
    print(f"    hybrid V = {rh!r},  error = {abs(rh - v_exact):.3e},  "
          f"steps = {it}")
    print("  step kinds (N=Newton, B=bisection):", "".join(kinds))
    print("  => the safeguard costs one slow step and saves the solve.")


# ----------------------------------------------------------------------
# 4. Hypocentre location
# ----------------------------------------------------------------------

def report_hypocentre() -> None:
    section("4. Hypocentre location: inverting arrival-time relations")
    stations = [(0.0, 0.0), (20.0, 0.0), (20.0, 20.0), (0.0, 20.0)]   # km
    true = (7.0, 9.0, 0.0)          # x, y, origin time (s)
    v = 6.0                         # km/s, constant-velocity model
    arrivals = [true[2] + math.hypot(true[0] - sx, true[1] - sy) / v
                for sx, sy in stations]
    print("  SYNTHETIC catalogue; stations at the corners of a 20 x 20 km box")
    print(f"  true hypocentre (x, y, t0) = {true},  v = {v} km/s")
    for (sx, sy), t in zip(stations, arrivals):
        print(f"    station ({sx:>5.1f},{sy:>5.1f})  arrival = {t:.6f} s")

    def residuals(m):
        x, y, t0 = m
        return [t0 + math.hypot(x - sx, y - sy) / v - t
                for (sx, sy), t in zip(stations, arrivals)]

    def jacobian(m):
        x, y, _ = m
        rows = []
        for sx, sy in stations:
            d = math.hypot(x - sx, y - sy)
            rows.append([(x - sx) / (v * d), (y - sy) / (v * d), 1.0])
        return rows

    m = [1.0, 1.0, 1.0]
    print(f"\n  start guess = {m}")
    print(f"  {'it':>3}{'x (km)':>12}{'y (km)':>12}{'t0 (s)':>12}"
          f"{'|error| (km)':>15}{'||r|| (s)':>12}")
    for it in range(8):
        r = residuals(m)
        j = jacobian(m)
        # Normal equations J^T J dm = -J^T r for the over-determined system.
        n, k = len(r), 3
        a = [[sum(j[i][p] * j[i][q] for i in range(n)) for q in range(k)]
             for p in range(k)]
        b = [-sum(j[i][p] * r[i] for i in range(n)) for p in range(k)]
        dm = gauss_solve(a, b)
        m = [m[i] + dm[i] for i in range(k)]
        err = math.hypot(m[0] - true[0], m[1] - true[1])
        rn = math.sqrt(sum(vv * vv for vv in residuals(m)))
        print(f"  {it:>3}{m[0]:>12.6f}{m[1]:>12.6f}{m[2]:>12.6f}"
              f"{err:>15.3e}{rn:>12.3e}")
    print(f"\n  located hypocentre = ({m[0]:.6f}, {m[1]:.6f}) km, "
          f"t0 = {m[2]:.3e} s")
    print(f"  location error     = "
          f"{math.hypot(m[0] - true[0], m[1] - true[1]):.3e} km")
    print("  Newton on the normal equations converges superlinearly here")
    print("  because the residual is a smooth function of the hypocentre.")


def main() -> None:
    report_orders()
    report_cycle()
    report_eos()
    report_hypocentre()
    section("Summary")
    print("bisection : order 1, guaranteed, needs a bracket")
    print("secant    : order 1.618, no derivative, still local")
    print("Newton    : order 2, fastest, needs df and a good start")
    print("hybrid    : Newton speed with bisection safety")


if __name__ == "__main__":
    main()
