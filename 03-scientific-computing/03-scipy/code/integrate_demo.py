"""scipy.integrate: quadrature and ODE integration, verified.

Run:  .venv/bin/python integrate_demo.py
Requires: scipy, numpy.

Companion to lesson 03-03-02.

Part 1  quadrature accuracy on integrands whose exact value is known;
        including a genuinely improper integral (infinite limits).
Part 2  the vertical gravity anomaly of an arbitrary 2-D body by quadrature.
        The quadrature engine is validated against two exact limits before it
        is trusted: an infinite horizontal slab (2*pi*G*rho*t) and a circular
        cross-section (2*G*pi*R^2*rho*z_c/(x^2+z_c^2), the 2-D analogue of the
        shell theorem). All densities, depths and vertex coordinates are
        SYNTHETIC values chosen for the demonstration.
Part 3  solve_ivp on a decay/chain problem, against the analytic exponential,
        and a controlled comparison of RK45, BDF and Radau on the same problem.
"""

import math

import numpy as np
from scipy import constants, integrate

G = constants.G           # 6.6743e-11 m3 kg-1 s-2
YEAR = 3.15576e7          # s, Julian year


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


# --------------------------------------------------------------------------
# Part 1 -- quadrature accuracy
# --------------------------------------------------------------------------

def part1_quadrature_accuracy():
    section("1. Quadrature accuracy against a known value")
    exact = math.pi
    f = lambda x: 4.0 / (1.0 + x * x)

    class Counter:
        def __init__(self, g):
            self.g = g
            self.n = 0

        def __call__(self, x):
            self.n += 1
            return self.g(x)

    cf = Counter(f)
    val, err = integrate.quad(cf, 0.0, 1.0, epsabs=1e-13, epsrel=1e-13)
    print(f"  I = integral_0^1 4/(1+x^2) dx = pi = {exact:.15f}")
    print("    quad (adaptive Gauss-Kronrod, QUADPACK QAGS)")
    print(f"      value = {val:.15f}   |error| = {abs(val - exact):.2e}"
          f"   reported abserr = {err:.2e}")
    print(f"      function evaluations actually used: {cf.n}")
    print()

    print("  Same integral, fixed-order and fixed-grid rules:")
    print(f"    {'rule':<34}{'value':<22}{'|error|':>10}")
    for order in (2, 3, 5, 10, 20):
        v = integrate.fixed_quad(f, 0.0, 1.0, n=order)[0]
        print(f"    {'fixed_quad (Gauss-Legendre), n=%2d' % order:<34}"
              f"{v:<22.15f}{abs(v - exact):>10.2e}")
    for n in (11, 101, 1001):
        x = np.linspace(0.0, 1.0, n)
        vt = np.trapezoid(f(x), x)
        vs = integrate.simpson(f(x), x=x)
        print(f"    {'trapezoid on n=%d' % n:<34}{vt:<22.15f}{abs(vt - exact):>10.2e}")
        print(f"    {'simpson   on n=%d' % n:<34}{vs:<22.15f}{abs(vs - exact):>10.2e}")
    print()
    print("  Fixed-order Gauss-Legendre benefits from an analytic integrand:")
    print("  n=10 already beats the trapezoid rule with 10 times as many nodes.")
    print("  On this integrand the trapezoid error falls as n^-2 -- from n=11")
    print("  to n=101 (a factor 9.18) it drops from 1.67e-3 to 1.67e-5, and its")
    print("  leading term is exactly 1/(6 n^2), because f'(1)-f'(0) = -2.")
    print("  The Simpson error falls as n^-6 here, not n^-4, because")
    print("  f''' = 96x(1-x^2)(1+x^2)^-4 vanishes at BOTH endpoints, so the")
    print("  leading h^4 term cancels: 3.97e-8 -> 3.95e-14 is a factor of 1e6")
    print("  against the 7.1e3 that n^-4 would predict. Adaptive quad reaches")
    print("  machine precision with 21 evaluations -- far fewer than any fixed")
    print("  grid needs.")

    print()
    print("  Improper integrals: quad handles infinite limits directly.")
    v1, e1 = integrate.quad(lambda x: math.exp(-x), 0.0, np.inf)
    v2, e2 = integrate.quad(lambda x: math.exp(-x * x), -np.inf, np.inf)
    print(f"    integral_0^inf  exp(-x) dx  = {v1:.15f}  (exact 1)      "
          f"|error| = {abs(v1 - 1):.2e}")
    print(f"    integral_-inf^inf exp(-x^2) dx = {v2:.15f}  (exact sqrt(pi) = "
          f"{math.sqrt(math.pi):.15f})  |error| = {abs(v2 - math.sqrt(math.pi)):.2e}")

    print()
    print("  Two cases where the *definition of the problem* matters more than")
    print("  the algorithm:")
    v3, e3 = integrate.quad(lambda x: x ** -0.5, 0.0, 1.0)
    print(f"    integral_0^1 x^(-1/2) dx = {v3:.15f}  (exact 2)   "
          f"|error| = {abs(v3 - 2):.2e}")
    print("      an integrable endpoint singularity; QUADPACK extrapolates it")

    spike = lambda x: 1.0e4 if 0.5 < x < 0.5 + 1.0e-4 else 0.0
    v4, e4 = integrate.quad(spike, 0.0, 1.0)
    v5, e5 = integrate.quad(spike, 0.0, 1.0,
                            points=[0.5, 0.5 + 1.0e-4])
    print(f"    integral_0^1 (spike of width 1e-4, exact 1.0):")
    print(f"      without points=  {v4:.6f}   reported abserr {e4:.2e}"
          f"   |error| {abs(v4 - 1.0):.2e}")
    print(f"      with    points=  {v5:.6f}   reported abserr {e5:.2e}"
          f"   |error| {abs(v5 - 1.0):.2e}")
    print("      The adaptive rule samples where the *estimator* says the")
    print("      error is; a feature it never sees cannot be found. Telling")
    print("      quad where the structure is (points=) is part of the input.")


# --------------------------------------------------------------------------
# Part 2 -- gravity of an arbitrary 2-D body
# --------------------------------------------------------------------------

def polygon_intersections(poly, x):
    """z values where the vertical line at x crosses the polygon edges."""
    zs = []
    n = len(poly)
    for i in range(n):
        x1, z1 = poly[i]
        x2, z2 = poly[(i + 1) % n]
        if x1 == x2:
            continue
        if min(x1, x2) <= x <= max(x1, x2):
            t = (x - x1) / (x2 - x1)
            zs.append(z1 + t * (z2 - z1))
    return zs


def gz_profile(poly, rho, stations, eps=1e-12):
    """Vertical attraction of a polygon with unlimited strike, by quadrature.

    gz(x0) = 2*G*rho * integral over the body of  z / ((x-x0)^2 + z^2) dx dz
    The inner z-integral is analytic:
        integral_{z1}^{z2} z/( (x-x0)^2 + z^2 ) dz
            = 0.5 * ln( ((x-x0)^2 + z2^2) / ((x-x0)^2 + z1^2) )
    so one adaptive quadrature over x remains. The x range is split at every
    vertex abscissa so that no quadrature interval straddles a corner.
    """
    xs = sorted({p[0] for p in poly})
    out = np.empty_like(stations, dtype=float)
    for k, x0 in enumerate(stations):
        total = 0.0
        for lo, hi in zip(xs[:-1], xs[1:]):
            def inner(x, x0=x0):
                zs = polygon_intersections(poly, x)
                if len(zs) < 2:
                    return 0.0
                z1, z2 = min(zs), max(zs)
                return 0.5 * math.log(((x - x0) ** 2 + z2 * z2)
                                      / ((x - x0) ** 2 + z1 * z1))
            piece, _ = integrate.quad(inner, lo, hi, epsabs=eps, epsrel=eps,
                                      limit=200)
            total += piece
        out[k] = 2.0 * G * rho * total
    return out


def circle_polygon(n, radius, depth, cx=0.0):
    ang = np.arange(n) * 2.0 * np.pi / n
    return list(zip(cx + radius * np.cos(ang), depth - radius * np.sin(ang)))


def is_convex(poly):
    n = len(poly)
    signs = []
    for i in range(n):
        x1, z1 = poly[i]
        x2, z2 = poly[(i + 1) % n]
        x3, z3 = poly[(i + 2) % n]
        cross = (x2 - x1) * (z3 - z2) - (z2 - z1) * (x3 - x2)
        signs.append(math.copysign(1.0, cross))
    return all(s == signs[0] for s in signs) and signs[0] != 0.0


def gz_circle(radius, depth, rho, stations, eps=1e-12):
    """Same quadrature reduction, for a body whose vertical extent is a circle."""
    out = np.empty_like(stations, dtype=float)
    for k, x0 in enumerate(stations):
        def inner(x, x0=x0):
            h = math.sqrt(max(radius * radius - x * x, 0.0))
            z1, z2 = depth - h, depth + h
            return 0.5 * math.log(((x - x0) ** 2 + z2 * z2)
                                  / ((x - x0) ** 2 + z1 * z1))
        piece, _ = integrate.quad(inner, -radius, radius, epsabs=eps, epsrel=eps,
                                  limit=200)
        out[k] = 2.0 * G * rho * piece
    return out


def gz_grid(poly, rho, x0, n=601):
    """An independent evaluation of the same integral on a uniform 2-D grid."""
    xs = np.array([p[0] for p in poly])
    zs = np.array([p[1] for p in poly])
    pad = 0.05 * max(np.ptp(xs), np.ptp(zs))
    gx = np.linspace(xs.min() - pad, xs.max() + pad, n)
    gz_ = np.linspace(zs.min() - pad, zs.max() + pad, n)
    X, Z = np.meshgrid(gx, gz_, indexing="ij")
    inside = _inside_polygon(X, Z, poly)
    integrand = np.where(inside, Z / ((X - x0) ** 2 + Z ** 2), 0.0)
    return 2.0 * G * rho * integrate.simpson(
        integrate.simpson(integrand, x=gz_, axis=1), x=gx)


def _inside_polygon(X, Z, poly):
    """Even-odd ray casting, vectorised (no library call, so it is inspectable)."""
    inside = np.zeros(X.shape, dtype=bool)
    n = len(poly)
    for i in range(n):
        x1, z1 = poly[i]
        x2, z2 = poly[(i + 1) % n]
        straddles = (z1 > Z) != (z2 > Z)
        with np.errstate(divide="ignore", invalid="ignore"):
            x_cross = x1 + (Z - z1) * (x2 - x1) / (z2 - z1)
        inside ^= straddles & (X < x_cross)
    return inside


def part2_gravity_of_a_body():
    section("2. Vertical gravity of an arbitrary 2-D body, by quadrature")
    rho = 300.0                     # kg m-3, SYNTHETIC density contrast

    # ---- validation (a): the infinite-slab limit
    print("  Validation (a): a wide, thin polygon must approach the infinite")
    print("  slab value 2*pi*G*rho*t. The residual is the field of the two")
    print("  missing tails, so it must fall as 1/W:")
    t = 1000.0
    g_exact = 2.0 * math.pi * G * rho * t
    print(f"    {'half-width W (km)':>18}{'gz (mGal)':>14}{'exact (mGal)':>14}"
          f"{'relative':>12}")
    for width in (2.0e5, 2.0e6, 2.0e7):
        slab = [(-width, 3000.0), (width, 3000.0), (width, 4000.0),
                (-width, 4000.0)]
        g = gz_profile(slab, rho, np.array([0.0]))[0]
        print(f"    {width / 1e3:>18.0f}{g * 1e5:>14.6f}{g_exact * 1e5:>14.6f}"
              f"{abs(g - g_exact) / g_exact:>12.2e}")

    # ---- validation (b): circular cross-section -> 2-D shell theorem
    print()
    print("  Validation (b): outside a circular cross-section the field equals")
    print("  that of a line mass on the axis, gz = 2*G*pi*R^2*rho*z_c/(x^2+z_c^2),")
    print("  the 2-D analogue of the shell theorem.")
    R, zc = 3000.0, 5000.0
    prof = np.array([-6000.0, -2000.0, 0.0, 2500.0, 7000.0])
    g_ref_R = 2.0 * G * math.pi * R ** 2 * rho * zc / (prof ** 2 + zc ** 2)
    g_circ = gz_circle(R, zc, rho, prof)
    print("    same integrand, exact circular geometry, adaptive quadrature:")
    print(f"      {'x (km)':>8}{'quadrature (mGal)':>20}{'line mass (mGal)':>18}"
          f"{'relative':>12}")
    for x, a, b in zip(prof, g_circ, g_ref_R):
        print(f"      {x / 1e3:>8.1f}{a * 1e5:>20.9f}{b * 1e5:>18.9f}"
              f"{abs(a - b) / abs(b):>12.2e}")
    print("    Now replace the circle by an inscribed n-gon. Two different")
    print("    errors then appear: the quadrature error (measured against the")
    print("    line mass built from the polygon's own equal-area radius) and")
    print("    the geometry error (measured against the true radius R).")
    print(f"      {'n':>6}{'R_eff (m)':>12}{'quadrature err':>16}"
          f"{'geometry err':>14}")
    for n in (16, 64, 256, 1024):
        poly = circle_polygon(n, R, zc)
        r_eff = math.sqrt(polygon_area(poly) / math.pi)
        g_num = gz_profile(poly, rho, prof)
        ref_eff = 2.0 * G * math.pi * r_eff ** 2 * rho * zc / (prof ** 2 + zc ** 2)
        print(f"      {n:>6}{r_eff:>12.1f}"
              f"{np.abs(g_num / ref_eff - 1).max():>16.2e}"
              f"{np.abs(g_num / g_ref_R - 1).max():>14.2e}")
    print("    The geometry term falls as n^-2, exactly as the area deficit")
    print("    1 - (n/2)sin(2 pi/n)/(pi) does; the quadrature is exact to")
    print("    round-off in both cases.")

    # ---- the arbitrary body
    body = [(-6000.0, 2000.0), (-3500.0, 1200.0), (-400.0, 1000.0),
            (2200.0, 1600.0), (4600.0, 2600.0), (3000.0, 5200.0),
            (400.0, 6400.0), (-2600.0, 5600.0), (-5200.0, 4000.0)]
    print()
    print("  The arbitrary body (SYNTHETIC 9-vertex convex polygon, "
          f"rho = {rho:.0f} kg m-3):")
    area = polygon_area(body)
    print(f"    convex? {is_convex(body)}   "
          f"depth range {min(p[1] for p in body) / 1e3:.1f}-"
          f"{max(p[1] for p in body) / 1e3:.1f} km   "
          f"cross-sectional area {area / 1e6:.3f} km^2")
    stations = np.arange(-12000.0, 12001.0, 3000.0)
    gz = gz_profile(body, rho, stations)
    print(f"    {'x (km)':>8}{'gz (mGal)':>14}")
    for x, g in zip(stations, gz):
        print(f"    {x / 1e3:>8.1f}{g * 1e5:>14.4f}")
    i_max = int(np.argmax(gz))
    print(f"    maximum {gz[i_max] * 1e5:.4f} mGal at x = {stations[i_max] / 1e3:.0f} km")
    print(f"    mass per unit strike length = rho*A = {rho * area:.4e} kg/m")

    print()
    print("  Independent cross-check: the same integral on a uniform 601 x 601")
    print("  grid with Simpson's rule (a different algorithm, no shared code).")
    print(f"    {'x (km)':>8}{'adaptive (mGal)':>18}{'grid Simpson (mGal)':>22}"
          f"{'relative':>12}")
    for x0 in (-6000.0, 0.0, 3000.0):
        a = gz_profile(body, rho, np.array([x0]))[0]
        b = gz_grid(body, rho, x0)
        print(f"    {x0 / 1e3:>8.1f}{a * 1e5:>18.6f}{b * 1e5:>22.6f}"
              f"{abs(a - b) / abs(a):>12.2e}")

    # ---- 3-D check: a sphere integrated in volume equals a point mass
    print()
    print("  A 3-D check on the same idea: a uniform sphere (R = 5 km, centre")
    print("  10 km deep) integrated over its volume must reproduce G*M/d^2.")
    Rs, ds = 5000.0, 10000.0
    rho3 = 2700.0

    def sphere_integrand(phi, r):
        # spherical polar coordinates about the sphere's centre, polar axis
        # pointing at the observation point; phi is the polar angle
        xi = ds - r * math.cos(phi)
        rho_h = r * math.sin(phi)
        return (r * r * math.sin(phi) * xi
                / (xi * xi + rho_h * rho_h) ** 1.5)

    vol_int, verr = integrate.dblquad(sphere_integrand, 0.0, Rs, 0.0, math.pi,
                                      epsabs=1e-10, epsrel=1e-10)
    g_num = G * rho3 * 2.0 * math.pi * vol_int
    mass = rho3 * 4.0 / 3.0 * math.pi * Rs ** 3
    g_pt = G * mass / ds ** 2
    print(f"    volume quadrature  gz = {g_num * 1e5:.6f} mGal")
    print(f"    point mass G*M/d^2    = {g_pt * 1e5:.6f} mGal")
    print(f"    relative difference   = {abs(g_num - g_pt) / g_pt:.2e}")


def polygon_area(poly):
    n = len(poly)
    return 0.5 * abs(sum(poly[i][0] * poly[(i + 1) % n][1]
                         - poly[(i + 1) % n][0] * poly[i][1] for i in range(n)))


# --------------------------------------------------------------------------
# Part 3 -- ODE integration
# --------------------------------------------------------------------------

def part3_ode():
    section("3. solve_ivp: decay, a two-species chain, and method comparison")
    half_life = 1.0e9                                   # yr, chosen input
    lam = math.log(2.0) / (half_life * YEAR)            # s-1

    # ---- single species
    y0 = [1.0]
    t_end = 4.0 * half_life * YEAR
    sol = integrate.solve_ivp(lambda t, y: [-lam * y[0]], (0.0, t_end), y0,
                              method="RK45", rtol=1e-10, atol=1e-14,
                              dense_output=True)
    tq = np.array([0.0, 0.5, 1.0, 2.0, 3.0, 4.0]) * half_life * YEAR
    num = sol.sol(tq)[0]
    ana = np.exp(-lam * tq)
    print("  Single-species decay, N(t) = N0 exp(-lambda t), t_half = 1.0e9 yr:")
    print(f"    {'t (t_half)':>11}{'solve_ivp':>18}{'analytic':>18}{'|err|':>10}")
    for tt, n, a in zip(tq / (half_life * YEAR), num, ana):
        print(f"    {tt:>11.1f}{n:>18.12f}{a:>18.12f}{abs(n - a):>10.2e}")
    print(f"    steps taken {sol.t.size}, function evaluations {sol.nfev},"
          f" max relative error {np.abs(num / ana - 1).max():.2e}")

    # ---- two-species chain: secular equilibrium
    def chain(t, y):
        parent, daughter = y
        return [-lam * parent, lam * parent]

    sol2 = integrate.solve_ivp(chain, (0.0, t_end), [1.0, 0.0], rtol=1e-10,
                               atol=1e-14, dense_output=True)
    par, dau = sol2.sol(tq)
    print()
    print("  Parent -> daughter chain (conservation and secular equilibrium):")
    print(f"    {'t (t_half)':>11}{'parent':>14}{'daughter':>14}{'sum':>14}"
          f"{'D/P':>12}")
    for tt, p, d in zip(tq / (half_life * YEAR), par, dau):
        ratio = d / p if p > 0 else float("inf")
        print(f"    {tt:>11.1f}{p:>14.9f}{d:>14.9f}{p + d:>14.9f}{ratio:>12.6f}")
    print("    The sum stays 1 to round-off, and D/P -> 1: that is secular")
    print("    equilibrium, obtained here without ever writing it down.")

    # ---- method comparison on a problem with a fast transient
    print()
    print("  Method choice. Problem: y' = -1000(y - cos t) - sin t,  y(0)=1,")
    print("  exact y = cos t. The solution is smooth; the equation is stiff.")
    stiff = lambda t, y: [-1000.0 * (y[0] - math.cos(t)) - math.sin(t)]
    exact = np.cos
    print(f"    {'method':<8}{'steps':>8}{'nfev':>8}{'njac':>7}"
          f"{'max |err|':>14}")
    for method in ("RK45", "BDF", "Radau"):
        m = integrate.solve_ivp(stiff, (0.0, 3.0), [1.0], method=method,
                                rtol=1e-8, atol=1e-10)
        err = np.abs(m.y[0] - exact(m.t)).max()
        njac = getattr(m, "njev", 0)
        print(f"    {method:<8}{m.t.size:>8}{m.nfev:>8}{njac:>7}{err:>14.2e}")
    print("    All three reach the tolerance. RK45 needs many more function")
    print("    evaluations because its stability limit, not its accuracy,")
    print("    sets the step: 'stiff' means exactly this. BDF and Radau form")
    print("    and factor a Jacobian (njac > 0) and take large steps with it.")


def main():
    part1_quadrature_accuracy()
    part2_gravity_of_a_body()
    part3_ode()
    print("\nDone.")


if __name__ == "__main__":
    main()
