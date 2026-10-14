"""Taylor series, linearisation and small-angle approximations in geophysics.

Run:  python3 taylor_linearisation_demo.py
Requires: Python standard library only.

Companion to lesson 01-05-04. Each section asks the same question in a different
physical costume: how large may the expansion variable be before the first-order
approximation stops being fit for purpose?
"""

import math

G = 6.674e-11        # m^3 kg^-1 s^-2
M_EARTH = 5.972e24   # kg (ILLUSTRATIVE round value)
R_EARTH = 6.371e6    # m  (ILLUSTRATIVE round value)
MGAL = 1.0e-5        # m/s^2 per mGal


def section(title: str) -> None:
    print(f"\n{'=' * 76}\n{title}\n{'=' * 76}")


def main() -> None:
    section("1. Truncation error of the Taylor series for sin(x) at x = 0.5 rad")
    exact = math.sin(0.5)
    print(f"  sin(0.5) = {exact!r}")
    print(f"{'order':>7}  {'partial sum':>22}  {'error':>12}"
          f"  {'next-term bound':>18}")
    terms = [0.5, -(0.5 ** 3) / 6.0, (0.5 ** 5) / 120.0,
             -(0.5 ** 7) / 5040.0, (0.5 ** 9) / 362880.0]
    total = 0.0
    for index, term in enumerate(terms):
        total += term
        order = 2 * index + 1
        next_bound = abs(terms[index + 1]) if index + 1 < len(terms) else float("nan")
        print(f"{order:>7}  {total:>22.17f}  {abs(total - exact):>12.3e}"
              f"  {next_bound:>18.3e}")
    print("  Reading: for an alternating series the error after truncating is")
    print("  bounded by the first omitted term, and here it essentially equals")
    print("  it. Each added pair of terms multiplies the error by about")
    print("  x^2/((k+1)(k+2)): at x = 0.5 that is 1/79, then 1/167, then")
    print("  1/279. Taylor series converge fast or they do not converge at all.")

    section("2. Small angle: sin(theta) ~ theta and its relative error")
    print(f"{'theta (deg)':>11}  {'theta (rad)':>12}  {'sin(theta)':>14}"
          f"  {'rel. error':>12}  {'theta^2/6':>12}")
    for degrees in (0.1, 1.0, 5.0, 10.0, 15.0, 30.0, 45.0, 60.0):
        theta = math.radians(degrees)
        s = math.sin(theta)
        print(f"{degrees:>11}  {theta:>12.7f}  {s:>14.10f}"
              f"  {(theta - s) / s:>12.4e}  {theta * theta / 6.0:>12.4e}")
    print("  Reading: the relative error is theta^2/6 to three digits up to")
    print("  about 15 degrees, so '1 % accurate' means theta below about 0.25")
    print("  rad. Seismic refraction angles of 30 degrees are NOT small and")
    print("  the approximation must not be used there.")

    section("3. Small angle: cos(theta) ~ 1 - theta^2/2")
    print(f"{'theta (deg)':>11}  {'cos(theta)':>16}  {'1 - theta^2/2':>16}"
          f"  {'rel. error':>12}")
    for degrees in (1.0, 5.0, 10.0, 30.0, 60.0):
        theta = math.radians(degrees)
        c = math.cos(theta)
        approx = 1.0 - 0.5 * theta * theta
        print(f"{degrees:>11}  {c:>16.12f}  {approx:>16.12f}"
              f"  {abs(approx - c) / c:>12.4e}")
    print("  Reading: cos is quadratic near zero, so the second-order")
    print("  approximation 1 - theta^2/2 has relative error theta^2/6 - the same")
    print("  size as the error of sin(theta) ~ theta at the same angle. What is")
    print("  NOT acceptable is the cruder 'cos ~ 1': its relative error is")
    print("  theta^2/2, three times larger. Moveout and NMO expansions keep the")
    print("  theta^2 term for exactly this reason.")

    section("4. Free-air gradient from the binomial expansion")
    g0 = G * M_EARTH / R_EARTH ** 2
    print(f"  g0 = {g0:.6f} m/s^2")
    print("  g(z) = GM/(R+z)^2 = g0 (1 + u)^-2,  u = z/R")
    print("  (1+u)^-2 = 1 - 2u + 3u^2 - ..., so dg/dz = -2 g0 / R for u -> 0")
    print(f"  -2 g0 / R = {-2.0 * g0 / R_EARTH:.6e} m/s^2 per m"
          f" = {-2.0 * g0 / R_EARTH / MGAL:.4f} mGal/m")
    print(f"  g0 = 9.80665, R = 6371000 gives"
          f" {-2.0 * 9.80665 / 6371000.0 / MGAL:.4f} mGal/m")
    print("\n  Reading: the textbook free-air gradient is about 0.3086 mGal/m.")
    print("  The spherical model above gives 0.3083 mGal/m with the mass and")
    print("  radius used here; part of that difference is the choice of g0 and")
    print("  R, and further differences come from rotation and ellipticity,")
    print("  which make the true gradient depend on latitude. Treat 0.3086 as")
    print("  a nominal value and use a gravity formula when precision matters.")

    section("5. Bouguer slab: a linearisation that is exactly linear")
    for rho in (2400.0, 2670.0):
        per_metre = 2.0 * math.pi * G * rho / MGAL
        print(f"  rho = {rho:.0f} kg/m^3: 2 pi G rho = {per_metre:.5f} mGal/m"
              f"   (Bouguer 0.04193*rho = {0.04193 * rho / 1000.0:.5f})")
    print("  Reading: the Bouguer slab correction is 2 pi G rho h, which has")
    print("  no approximation in it at all once the slab is infinite, even")
    print("  though it is often described as a 'linearisation'. It is exact;")
    print("  the approximation is the assumption of an infinite flat slab.")

    section("6. Normal moveout: exact hyperbola versus parabolic expansion")
    v, t0 = 2000.0, 1.0
    print(f"  one layer: v = {v:.0f} m/s, t0 = {t0:.1f} s")
    print(f"{'x (m)':>8}  {'t exact (s)':>14}  {'t parabolic':>14}"
          f"  {'rel. error':>12}  {'u = (x/(v t0))^2':>18}")
    for x in (100.0, 500.0, 1000.0, 2000.0, 3000.0):
        exact = math.sqrt(t0 * t0 + x * x / (v * v))
        parabolic = t0 + x * x / (2.0 * v * v * t0)
        u = x * x / (v * v * t0 * t0)
        print(f"{x:>8.0f}  {exact:>14.9f}  {parabolic:>14.9f}"
              f"  {(parabolic - exact) / exact:>12.3e}  {u:>18.4e}")
    print("  Reading: the exact moveout curve for a single layer IS the")
    print("  hyperbola t = sqrt(t0^2 + x^2/v^2). The NMO equation")
    print("  t = t0 + x^2/(2 v^2 t0) is its first-order expansion in x^2, and")
    print("  it is accurate only while x << v t0 - that is, at offsets much")
    print("  smaller than the reflector depth. Beyond that, higher-order")
    print("  moveout terms are needed.")

    section("7. Linearising a gravity perturbation: relative error 3(dd/d)^2")
    mass = 1.0e10
    for depth in (100.0, 500.0):
        g = G * mass / depth ** 2
        print(f"  depth {depth:.0f} m: g = {g:.6e} m/s^2"
              f" = {g / MGAL * 1000.0:.4f} µGal")
        for shift in (1.0, 5.0):
            exact = G * mass / (depth + shift) ** 2
            linear = g * (1.0 - 2.0 * shift / depth)
            u = shift / depth
            print(f"    shift {shift:>4.0f} m (u = {u:.3f}):"
                  f" exact = {exact:.6e}, linear = {linear:.6e},"
                  f" rel. error = {(linear - exact) / exact:+.3e}"
                  f"  [leading term -3u^2 = {-3.0 * u * u:+.3e}]")
    print("  Reading: the relative error of the linearised perturbation is")
    print("  3(delta d/d)^2, so 1 % in the perturbation variable already costs")
    print("  about 3e-4 in the answer. This is the arithmetic behind every")
    print("  'linearised inverse problem', and the reason a linearisation is")
    print("  invalidated by large model perturbations rather than by large")
    print("  data.")

    section("8. Where the expansion variable lives: ln(1+x) at two radii")
    print(f"{'n (terms)':>10}  {'x = 0.1':>20}  {'x = 1':>20}")
    for n in (1, 2, 3, 5, 10, 20, 100, 1000):
        s_small = sum(((-1) ** (k + 1)) * (0.1 ** k) / k for k in range(1, n + 1))
        s_edge = sum(((-1) ** (k + 1)) / k for k in range(1, n + 1))
        print(f"{n:>10}  {s_small:>20.15f}  {s_edge:>20.15f}")
    print(f"  ln(1.1) = {math.log(1.1)!r}")
    print(f"  ln(2)   = {math.log(2.0)!r}")
    print("  Reading: the series for ln(1+x) has radius of convergence 1. At")
    print("  x = 0.1 ten terms give twelve digits; at the edge x = 1 the error")
    print("  falls only like 1/n and ten terms give two digits. Convergence at")
    print("  the boundary of the radius is real but slow - the subject of")
    print("  lesson 01-05-07.")


if __name__ == "__main__":
    main()
