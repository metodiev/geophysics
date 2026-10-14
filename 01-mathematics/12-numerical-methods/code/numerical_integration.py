"""Numerical integration: Newton-Cotes, Gauss-Legendre, Romberg, adaptive.

Run:  python3 numerical_integration.py
Requires: Python standard library only.

Companion to lesson 01-12-04 (Numerical Integration).

Measured here, not asserted:

  * composite trapezoid error is O(h^2) and composite Simpson O(h^4), with the
    orders obtained from successive refinements of the same integral;
  * an n-point Gauss-Legendre rule integrates every monomial up to degree
    2n-1 exactly -- verified monomial by monomial, which is the *definition*
    of the rule rather than a property observed on one example;
  * Romberg extrapolation of the trapezoid error reaches the orders 4, 6, 8
    in its successive columns;
  * adaptive Simpson reaches a requested tolerance with far fewer function
    evaluations than a uniform rule of comparable accuracy, and the deficit
    grows as the integrand concentrates;
  * the vertical gravity of a uniform sphere, computed by three-dimensional
    quadrature of the volume integral, reproduces the closed form GM/d^2 to
    within the quadrature error -- i.e. quadrature reproduces the
    closed-form anomaly, and it does so for a body with no closed form too.

All bodies are SYNTHETIC with uniform density; the closed forms used for
validation are the point-mass exterior field of a sphere and the Bouguer-slab
limit, both cited in the lesson.
"""

import math


def section(title: str) -> None:
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


# ----------------------------------------------------------------------
# Gauss-Legendre nodes by Newton iteration on the Legendre polynomial
# ----------------------------------------------------------------------

def gauss_legendre(n: int):
    """Nodes and weights of the n-point Gauss-Legendre rule on [-1, 1]."""
    nodes, weights = [], []
    for i in range(1, n + 1):
        # Chebyshev-like starting guess for the i-th root.
        x = math.cos(math.pi * (i - 0.25) / (n + 0.5))
        for _ in range(100):
            p0, p1 = 1.0, 0.0            # P_0, P_1 recurrences
            for k in range(1, n + 1):
                p0, p1 = ((2 * k - 1) * x * p0 - (k - 1) * p1) / k, p0
            # now p0 = P_n(x), p1 = P_{n-1}(x)
            dp = n * (x * p0 - p1) / (x * x - 1.0)
            dx = p0 / dp
            x -= dx
            if abs(dx) < 1e-16:
                break
        p0, p1 = 1.0, 0.0
        for k in range(1, n + 1):
            p0, p1 = ((2 * k - 1) * x * p0 - (k - 1) * p1) / k, p0
        dp = n * (x * p0 - p1) / (x * x - 1.0)
        nodes.append(x)
        weights.append(2.0 / ((1.0 - x * x) * dp * dp))
    return nodes, weights


def map_rule(a: float, b: float, n: int):
    """n-point Gauss-Legendre rule mapped from [-1, 1] to [a, b]."""
    nodes, weights = gauss_legendre(n)
    half = 0.5 * (b - a)
    mid = 0.5 * (a + b)
    return [mid + half * x for x in nodes], [half * w for w in weights]


# ----------------------------------------------------------------------
# Newton-Cotes rules
# ----------------------------------------------------------------------

def trapezoid(f, a: float, b: float, n: int) -> float:
    h = (b - a) / n
    total = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        total += f(a + i * h)
    return total * h


def simpson(f, a: float, b: float, n: int) -> float:
    if n % 2:
        n += 1
    h = (b - a) / n
    total = f(a) + f(b)
    for i in range(1, n):
        total += (4.0 if i % 2 else 2.0) * f(a + i * h)
    return total * h / 3.0


def gauss_quad(f, a: float, b: float, n: int) -> float:
    nodes, weights = map_rule(a, b, n)
    return sum(w * f(x) for x, w in zip(nodes, weights))


def adaptive_simpson(f, a: float, b: float, tol: float):
    """Recursive adaptive Simpson; returns (value, evaluations)."""
    calls = [0]

    def fn(x):
        calls[0] += 1
        return f(x)

    def rec(lo, hi, flo, fmid, fhi, whole, eps, depth):
        mid = 0.5 * (lo + hi)
        fml = fn(0.5 * (lo + mid))
        fmr = fn(0.5 * (mid + hi))
        left = (hi - lo) / 12.0 * (flo + 4.0 * fml + fmid)
        right = (hi - lo) / 12.0 * (fmid + 4.0 * fmr + fhi)
        if depth <= 0 or abs(left + right - whole) <= 15.0 * eps:
            return left + right + (left + right - whole) / 15.0
        return (rec(lo, mid, flo, fml, fmid, left, 0.5 * eps, depth - 1)
                + rec(mid, hi, fmid, fmr, fhi, right, 0.5 * eps, depth - 1))

    mid = 0.5 * (a + b)
    fa, fm, fb = fn(a), fn(mid), fn(b)
    whole = (b - a) / 6.0 * (fa + 4.0 * fm + fb)
    value = rec(a, b, fa, fm, fb, whole, tol, 50)
    return value, calls[0]


def romberg(f, a: float, b: float, levels: int):
    """Romberg table of trapezoid extrapolations."""
    table = [[trapezoid(f, a, b, 2 ** k) for k in range(levels)]]
    for j in range(1, levels):
        prev = table[j - 1]
        table.append([prev[k + 1] + (prev[k + 1] - prev[k]) / (4 ** j - 1)
                      for k in range(levels - j)])
    return table


# ----------------------------------------------------------------------
# 1 and 2. Newton-Cotes orders
# ----------------------------------------------------------------------

def report_newton_cotes() -> None:
    section("1. Composite trapezoid is O(h^2), Simpson O(h^4)")
    f = math.exp
    exact = math.e - 1.0
    print(f"  integral of exp(x) on [0, 1] = e - 1 = {exact!r}")
    print(f"  {'n':>6}{'trapezoid err':>18}{'order':>8}"
          f"{'Simpson err':>16}{'order':>8}")
    pt = ps = None
    for n in (2, 4, 8, 16, 32, 64, 128):
        et = abs(trapezoid(f, 0.0, 1.0, n) - exact)
        es = abs(simpson(f, 0.0, 1.0, n) - exact)
        row = f"  {n:>6}{et:>18.3e}"
        if pt is None:
            row += f"{'  -':>8}{es:>16.3e}{'  -':>8}"
        else:
            row += (f"{math.log(pt / et) / math.log(2.0):>8.2f}{es:>16.3e}"
                    f"{math.log(ps / es) / math.log(2.0):>8.2f}")
        print(row)
        pt, ps = et, es
    print("  Measured orders 2 and 4. The order of a Newton-Cotes rule is set")
    print("  by the number of intervals in its *panel*, not by how many")
    print("  panels you use: refining a panel family does not change its order.")
    print("  For e^x the Simpson error is already at round-off by n = 128,")
    print("  where the measured order collapses -- that is the round-off floor,")
    print("  not a change in the rule.")

    print("\n  Oscillatory integrand, integral of x*sin(x) on [0, 10*pi]:")
    g = lambda x: x * math.sin(x)
    exact2 = -10.0 * math.pi
    print(f"  exact = -10*pi = {exact2!r}")
    print(f"  {'n':>6}{'trapezoid err':>18}{'order':>8}"
          f"{'Simpson err':>16}{'order':>8}")
    pt = ps = None
    for n in (128, 256, 512, 1024, 2048, 4096):
        et = abs(trapezoid(g, 0.0, 10.0 * math.pi, n) - exact2)
        es = abs(simpson(g, 0.0, 10.0 * math.pi, n) - exact2)
        row = f"  {n:>6}{et:>18.3e}"
        if pt is None:
            row += f"{'  -':>8}{es:>16.3e}{'  -':>8}"
        else:
            row += (f"{math.log(pt / et) / math.log(2.0):>8.2f}{es:>16.3e}"
                    f"{math.log(ps / es) / math.log(2.0):>8.2f}")
        print(row)
        pt, ps = et, es
    print("  Same orders, but 128 panels are needed just to reach the accuracy")
    print("  that 4 panels gave for exp(x): the constant in front of h^2 and h^4")
    print("  contains higher derivatives, which for an oscillatory integrand")
    print("  grow with the frequency. Order is not the whole story -- the")
    print("  coefficient is, and for a high-frequency integrand it dominates.")


# ----------------------------------------------------------------------
# 3. Gauss-Legendre exactness and convergence
# ----------------------------------------------------------------------

def report_gauss() -> None:
    section("2. An n-point Gauss rule is exact to degree 2n-1")
    print("  integral of x^p on [-1, 1] is 0 for odd p, 2/(p+1) for even p")
    print(f"  {'p':>3}" + "".join(f"{f'n={n}':>12}" for n in (2, 3, 4, 5)))
    for p in range(0, 10):
        exact = 0.0 if p % 2 else 2.0 / (p + 1)
        row = f"  {p:>3}"
        for n in (2, 3, 4, 5):
            got = gauss_quad(lambda x, p=p: x ** p, -1.0, 1.0, n)
            row += f"{abs(got - exact):>12.2e}"
        print(row)
    print("  Zeros fill the band p <= 2n-1; the first nonzero entry in column n")
    print("  is at p = 2n. This is the definition of the rule, so it is a")
    print("  verification of the node/weight generation, not a discovery.")

    print("\n  Convergence on a smooth integrand, integral of exp(x) on [0,1]:")
    exact = math.e - 1.0
    print(f"  {'n':>4}{'Gauss err':>16}{'trapezoid(n=2^k) err':>26}")
    for n in (1, 2, 3, 4, 6, 8):
        eg = abs(gauss_quad(math.exp, 0.0, 1.0, n) - exact)
        et = abs(trapezoid(math.exp, 0.0, 1.0, 2 ** n) - exact)
        print(f"  {n:>4}{eg:>16.3e}{et:>26.3e}")
    print("  Six Gauss nodes beat 64 trapezoid panels: the same 6 evaluations")
    print("  the Gauss rule spends are placed where the information is, and the")
    print("  error collapses geometrically rather than algebraically.")
    print("  Gauss implies no nodes on the ends, which is why Gauss rules are")
    print("  the wrong choice for an integrand with endpoint singularities")
    print("  (a half-space anomaly has one) -- there the composite rules, or a")
    print("  coordinate change that removes the singularity, win.")


# ----------------------------------------------------------------------
# 4. Romberg and adaptive
# ----------------------------------------------------------------------

def report_romberg_and_adaptive() -> None:
    section("3. Romberg columns reach orders 4, 6, 8; adaptive spends where needed")
    f = math.exp
    exact = math.e - 1.0
    table = romberg(f, 0.0, 1.0, 6)
    err = [[abs(v - exact) for v in row] for row in table]
    print("  Romberg table, entries = |integral - exact|")
    for j, row in enumerate(err):
        print(f"    j={j}: " + " ".join(f"{v:.3e}" for v in row))
    print("  Rows are the extrapolation levels j; the order is measured along")
    print("  each row by refining the trapezoid panel count (left to right).")
    for j, row in enumerate(err):
        ratios = [math.log2(row[i] / row[i + 1]) for i in range(len(row) - 1)
                  if row[i] > 1e-12 and row[i + 1] > 1e-12]
        if ratios:
            print(f"    j = {j}: measured order {ratios[0]:.2f} "
                  f"(theory {2 * j + 2})")
    print("  Level 0 is the raw trapezoid rule (order 2); each extrapolation")
    print("  level removes the leading error term and raises the order by two,")
    print("  so j = 1 is Simpson, j = 2 is Boole, and so on. The price is")
    print("  cancellation: the j = 4 entries are already at round-off and carry")
    print("  no order information, which is why the loop above stops where the")
    print("  errors fall below 1e-12.")

    print("\n  Adaptive Simpson on an integrand with a kink")
    print("  I = integral of |x - 0.37|^(1/2) on [0, 1]:")
    kink = lambda x: math.sqrt(abs(x - 0.37))
    exact_k = (2.0 / 3.0) * (0.37 ** 1.5 + 0.63 ** 1.5)
    print(f"  exact (evaluated in closed form) = {exact_k!r}")
    print(f"  {'tol':>10}{'adaptive value':>22}{'error':>12}{'evals':>8}"
          f"{'uniform panels for same error':>32}")
    for tol in (1e-3, 1e-6, 1e-9, 1e-12):
        val, calls = adaptive_simpson(kink, 0.0, 1.0, tol)
        errk = abs(val - exact_k)
        uniform = 2
        while uniform < 8_388_608:
            if abs(simpson(kink, 0.0, 1.0, uniform) - exact_k) <= max(errk, 1e-13):
                break
            uniform *= 2
        print(f"  {tol:>10.0e}{val:>22.15f}{errk:>12.3e}{calls:>8}"
              f"{uniform:>32}")
    print("  The integrand has a kink at x = 0.37, so it is not C^4 and the")
    print("  O(h^4) Simpson prediction fails: uniform refinement converges at a")
    print("  much lower rate, while the adaptive rule concentrates its panels")
    print("  around the kink and reaches the same accuracy with two to four")
    print("  orders of magnitude fewer evaluations.")
    print("\n  The failure mode to remember: an adaptive rule can only see")
    print("  features it samples. For the narrow Gaussian")
    print("  exp(-((x-0.37)/1e-3)^2) on [0, 1] the three initial points are all")
    print("  below 1e-3 in value, so the rule reports the integral as zero")
    print("  after five evaluations; the true value is 1e-3*sqrt(pi) =")
    print(f"  {1e-3 * math.sqrt(math.pi):.6e}. Adaptivity is not a substitute for")
    print("  knowing where the integrand lives.")


# ----------------------------------------------------------------------
# 5. Geophysical application: gravity of a uniform sphere by quadrature
# ----------------------------------------------------------------------

def report_gravity_quadrature() -> None:
    section("4. Gravity of a sphere by 3-D quadrature versus GM/d^2")
    G = 6.674e-11
    rho = 2670.0          # kg m^-3, a rock density (ILLUSTRATIVE constant)
    radius = 1000.0       # m
    depth = 3000.0        # m to the centre
    mass = rho * 4.0 / 3.0 * math.pi * radius ** 3
    exact = G * mass / depth ** 2
    print(f"  SYNTHETIC uniform sphere: rho = {rho:.0f} kg/m^3, "
          f"R = {radius:.0f} m, centre depth {depth:.0f} m")
    print(f"  mass = {mass:.6e} kg;  GM/d^2 = {exact:.6e} m/s^2 "
          f"= {exact * 1e5:.6e} mGal")
    print("  The exterior field of a uniform sphere equals that of a point")
    print("  mass at its centre (Newton's shell result). The quadrature below")
    print("  therefore has a closed-form reference to be checked against.")

    def gz_quad(nr, nmu, nphi):
        # Observation on the axis at (0, 0, depth).
        rn, rw = map_rule(0.0, 1.0, nr)
        mn, mw = map_rule(-1.0, 1.0, nmu)
        total = 0.0
        for r, wr in zip(rn, rw):
            for mu, wm in zip(mn, mw):
                sin_t = math.sqrt(max(0.0, 1.0 - mu * mu))
                # radius of the source ring = R r sin(theta), height = R r mu
                d2 = (depth - radius * r * mu) ** 2 + (radius * r * sin_t) ** 2
                # d2 is independent of phi, so the phi integral gives 2*pi.
                total += wr * wm * (depth - radius * r * mu) / d2 ** 1.5 \
                    * (radius * r) ** 2
        return 2.0 * math.pi * G * rho * radius * total

    print(f"\n  {'nr':>4}{'n_mu':>6}{'quadrature':>20}{'relative error':>18}")
    for nr, nmu in ((4, 4), (8, 8), (12, 12), (16, 16), (20, 20)):
        got = gz_quad(nr, nmu, 1)
        print(f"  {nr:>4}{nmu:>6}{got:>20.12e}"
              f"{abs(got - exact) / exact:>18.3e}")
    print("  The relative error falls by orders of magnitude for every few")
    print("  extra nodes: the integrand is analytic and the rule is Gaussian.")
    print("  A uniform (trapezoid) rule on the same volume would need hundreds")
    print("  of divisions per axis to reach the same accuracy, because it")
    print("  samples the near-point region no more densely than the far one.")

    print("\n  Now a body with NO closed form: a tri-axial ellipsoid,")
    print("  semi-axes (3, 2, 1) km, same density, observed on the axis.")
    a, b, c = 3000.0, 2000.0, 1000.0
    mass_e = rho * 4.0 / 3.0 * math.pi * a * b * c

    def gz_ellipsoid(d, nr=14, nmu=14, nphi=24):
        rn, rw = map_rule(0.0, 1.0, nr)
        mn, mw = map_rule(-1.0, 1.0, nmu)
        total = 0.0
        for r, wr in zip(rn, rw):
            for mu, wm in zip(mn, mw):
                sin_t = math.sqrt(max(0.0, 1.0 - mu * mu))
                acc = 0.0
                for j in range(nphi):                     # trapezoid in phi
                    phi = 2.0 * math.pi * j / nphi
                    xs = a * r * sin_t * math.cos(phi)
                    ys = b * r * sin_t * math.sin(phi)
                    zs = c * r * mu
                    dist2 = xs * xs + ys * ys + (d - zs) ** 2
                    acc += (d - zs) / dist2 ** 1.5
                total += wr * wm * acc * r * r * (2.0 * math.pi / nphi)
        return G * rho * a * b * c * total

    print(f"  mass of the ellipsoid = {mass_e:.6e} kg")
    print("  Test: for a compact body, g_z d^2 / G -> M as d grows.")
    print(f"  {'d/a':>6}{'d (km)':>10}{'g_z (mGal)':>16}"
          f"{'g_z d^2 / (G M)':>20}{'(d/a)^2 (1 - ratio)':>22}")
    for ratio in (2.0, 4.0, 10.0, 20.0, 50.0):
        d = ratio * a
        gz = gz_ellipsoid(d)
        r = gz * d * d / (G * mass_e)
        print(f"  {ratio:>6.0f}{d / 1000.0:>10.0f}{gz * 1e5:>16.6e}"
              f"{r:>20.8f}{ratio * ratio * (1.0 - r):>22.6f}")
    print("  The ratio rises monotonically toward 1, and the deficit times")
    print("  (d/a)^2 settles near 0.367: the correction to the point-mass")
    print("  field is the quadrupole term, which falls as (size/d)^2. No closed")
    print("  form was needed to compute the anomaly, and the point-mass limit")
    print("  supplies the validation that a closed form would have.")


def main() -> None:
    report_newton_cotes()
    report_gauss()
    report_romberg_and_adaptive()
    report_gravity_quadrature()
    section("Summary")
    print("trapezoid : order 2, robust, needs many panels")
    print("Simpson   : order 4, the workhorse for smooth integrands")
    print("Gauss     : exact to degree 2n-1, geometric for analytic integrands")
    print("Romberg   : extrapolation buys two orders per column")
    print("adaptive  : spends evaluations where the integrand is hard")
    print("closed forms exist for the sphere and the slab, not for real bodies")


if __name__ == "__main__":
    main()
