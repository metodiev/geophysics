"""Holomorphic functions: Cauchy-Riemann and the Laplacian, measured.

Run:  python3 holomorphic_laplace_demo.py
Requires: Python standard library only (``cmath``).

Companion to lesson 01-11-02 (Holomorphic Functions and Cauchy-Riemann
Equations).

Everything asserted in the lesson is checked here:

1. the Cauchy-Riemann residual of a candidate function, evaluated with central
   differences, for functions that are and are not holomorphic;
2. the five-point finite-difference Laplacian of the real and the imaginary
   part of a holomorphic function, with its measured O(h^2) convergence;
3. the same test for |z|^2, which is *not* the real part of a holomorphic
   function, so the test is shown to be able to fail;
4. reconstruction of the harmonic conjugate of a given harmonic function by
   integrating the Cauchy-Riemann equations;
5. the complex potential of a two-dimensional line mass, w = m log z, and of a
   two-dimensional dipole, w = mu / z, both of which are the exact analytic
   solutions of potential-field problems;
6. orthogonality of the equipotential and flux curves, which is what
   conjugacy means geometrically.
"""

import cmath
import math


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def simpson(f, a, b, n):
    """Composite Simpson rule; n is made even if it is not."""
    if n % 2:
        n += 1
    h = (b - a) / n
    total = f(a) + f(b)
    for j in range(1, n):
        total += (4.0 if j % 2 else 2.0) * f(a + j * h)
    return total * h / 3.0


def parts(f, x, y):
    """(u, v) = (Re f, Im f) at z = x + iy."""
    w = f(complex(x, y))
    return w.real, w.imag


def cr_residual(f, x, y, h=1e-4):
    """Max |u_x - v_y| and |u_y + v_x| at (x, y), by central differences."""
    ux = (parts(f, x + h, y)[0] - parts(f, x - h, y)[0]) / (2 * h)
    uy = (parts(f, x, y + h)[0] - parts(f, x, y - h)[0]) / (2 * h)
    vx = (parts(f, x + h, y)[1] - parts(f, x - h, y)[1]) / (2 * h)
    vy = (parts(f, x, y + h)[1] - parts(f, x, y - h)[1]) / (2 * h)
    return abs(ux - vy), abs(uy + vx)


def laplacian_u(f, x, y, h, component=0):
    """Five-point finite-difference Laplacian h^-2 (u_E+u_W+u_N+u_S-4u_C)."""
    centre = parts(f, x, y)[component]
    east = parts(f, x + h, y)[component]
    west = parts(f, x - h, y)[component]
    north = parts(f, x, y + h)[component]
    south = parts(f, x, y - h)[component]
    return (east + west + north + south - 4 * centre) / (h * h)


def conjugate_from_u(u, x, y, h=1e-7):
    """Harmonic conjugate v of a given harmonic u, by integrating v_x=-u_y.

    The line integral of the total differential dv = -u_y dx + u_x dy is taken
    along the coordinate axes from (0, 0) to (x, y); this is legitimate
    whenever the domain is simply connected and v(0,0) is fixed at zero.
    """
    # v(0, y): integrate v_y = u_x along the y-axis from 0 to y.
    v = 0.0
    n = 400
    dy = y / n
    for k in range(n):
        yy = (k + 0.5) * dy
        ux = (u(0.0 + h, yy) - u(0.0 - h, yy)) / (2 * h)
        v += ux * dy
    # v(x, y): integrate v_x = -u_y along x at fixed y.
    dx = x / n
    for k in range(n):
        xx = (k + 0.5) * dx
        uy = (u(xx, y + h) - u(xx, y - h)) / (2 * h)
        v += -uy * dx
    return v


def main():
    section("1. Cauchy-Riemann residuals, holomorphic versus not")
    cases = [
        ("f(z) = z^2", lambda z: z * z, 1.3, -0.7, True),
        ("f(z) = exp(z)", cmath.exp, 0.4, 1.1, True),
        ("f(z) = 1/z", lambda z: 1 / z, -2.0, 1.5, True),
        ("f(z) = log z (principal)", cmath.log, 1.2, 0.8, True),
        ("f(z) = conj(z)", lambda z: z.conjugate(), 1.3, -0.7, False),
        ("f(z) = |z|^2", lambda z: complex(abs(z) ** 2), 1.3, -0.7, False),
        ("f(z) = Re(z)", lambda z: complex(z.real), 0.9, 0.4, False),
    ]
    print(f"  {'function':>28} {'point':>12} {'|u_x-v_y|':>12} {'|u_y+v_x|':>12}"
          f" {'verdict':>12}")
    for label, f, x, y, holomorphic in cases:
        r1, r2 = cr_residual(f, x, y)
        verdict = "holomorphic" if holomorphic else "NOT"
        print(f"  {label:>28} {x:.1f}{y:+.1f}i {r1:>12.3e} {r2:>12.3e}"
              f" {verdict:>12}")
    print("  For the holomorphic functions both residuals sit at either the")
    print("  round-off level (when the central difference happens to be exact for")
    print("  that polynomial) or at the truncation level O(h^2) = 1e-8 for")
    print("  h = 1e-4; for the others they are O(1) and do not shrink with h.")

    section("2. The Laplacian of Re f and Im f, and its O(h^2) convergence")
    for label, f in [("z^2", lambda z: z * z),
                     ("exp(z)", cmath.exp),
                     ("1/(z-3)", lambda z: 1 / (z - 3))]:
        print(f"  f(z) = {label} at z = 0.4 + 1.1i")
        print(f"    {'h':>8} {'Lap(Re f)':>16} {'Lap(Im f)':>16}")
        for h in (1e-2, 5e-3, 2.5e-3, 1.25e-3):
            lu = laplacian_u(f, 0.4, 1.1, h, 0)
            lv = laplacian_u(f, 0.4, 1.1, h, 1)
            print(f"    {h:>8.5f} {lu:>16.6e} {lv:>16.6e}")
    print("  Halving h cuts the residual by about four: the five-point Laplacian")
    print("  has truncation error h^2/12 * (u_xxxx + u_yyyy), and the exact")
    print("  Laplacian of both parts is zero.")

    section("3. The same test on a function with no holomorphic partner")
    f = lambda z: complex(abs(z) ** 2)          # u = x^2 + y^2, v = 0
    print("  f(z) = |z|^2: u = x^2 + y^2, v = 0, so u_x - v_y = 2x and")
    print("  u_y + v_x = 2y: the Cauchy-Riemann equations hold only at the")
    print("  origin, and the Laplacian of u is 4 everywhere.")
    for h in (1e-2, 5e-3, 2.5e-3):
        print(f"    h = {h:.5f}: Lap(u) = {laplacian_u(f, 1.3, -0.7, h, 0):.6f}"
              f" (exact 4), Lap(v) = {laplacian_u(f, 1.3, -0.7, h, 1):.6f}")
    print("  A function whose real part is harmonic but whose imaginary part is")
    print("  not cannot be holomorphic: holomorphy forces *both* parts to be")
    print("  harmonic, and it is the pair that matters, not either one alone.")
    print("  For |z|^2 the real part fails too, so the test catches it twice")
    print("  over.  A sharper case is u = x^2 - y^2 paired with v = 0: u *is*")
    print("  harmonic, yet x^2 - y^2 + 0i is not holomorphic at any point with")
    print("  x != 0, because u_x = 2x and v_y = 0.  Harmonic is necessary for a")
    print("  real part, never sufficient by itself.")
    paired = lambda z: complex(z.real ** 2 - z.imag ** 2)
    for x, y in [(0.0, 0.0), (1.0, 0.0), (0.5, 1.5)]:
        lu = laplacian_u(paired, x, y, 1e-3, 0)
        r1, r2 = cr_residual(paired, x, y)
        print(f"    u = x^2 - y^2, v = 0 at ({x:.1f}, {y:.1f}): Lap(u) ="
              f" {lu:>12.3e}, |u_x - v_y| = {r1:.3e}, |u_y + v_x| = {r2:.3e}")

    section("4. Reconstructing the harmonic conjugate of u = x^2 - y^2")
    u = lambda x, y: x * x - y * y
    print(f"  {'x':>7} {'y':>7} {'u':>12} {'v (integrated)':>16}"
          f" {'2xy (exact)':>14} {'error':>10}")
    for x, y in [(0.5, 0.5), (1.0, 0.25), (-0.75, 1.5), (2.0, -1.0)]:
        v = conjugate_from_u(u, x, y)
        print(f"  {x:>7.2f} {y:>7.2f} {u(x, y):>12.6f} {v:>16.9f}"
              f" {2 * x * y:>14.6f} {abs(v - 2 * x * y):>10.2e}")
    print("  The integration reproduces v = 2xy, which is exactly the imaginary")
    print("  part of z^2.  The conjugate is unique up to an additive constant,")
    print("  fixed here by v(0,0) = 0.")

    section("5. Complex potential of a 2-D line mass and of a 2-D dipole")
    m = 1.0
    line = lambda z: m * cmath.log(z)          # w = m log z
    print("  w(z) = m log z.  u = m ln r is the potential of a line mass (or a")
    print("  line charge); v = m theta is the stream function of the same field.")
    print(f"    {'r (unit)':>10} {'u = ln r (at theta=30deg)':>28}"
          f" {'v = theta (deg)':>18}")
    theta = math.radians(30.0)
    for r in (0.1, 1.0, 10.0, 100.0):
        uu, vv = parts(line, r * math.cos(theta), r * math.sin(theta))
        print(f"    {r:>10.2f} {uu:>28.6f} {math.degrees(vv):>18.6f}")
    print("  The potential is logarithmic in r and the stream function is the")
    print("  polar angle, which is exactly the second harmonic of the plane.")
    print("  Laplacian of u away from the source, by finite differences:")
    for h in (1e-2, 5e-3, 2.5e-3):
        val = laplacian_u(line, 1.7, -0.9, h, 0)
        print(f"    h = {h:.5f}: Lap(u) = {val:>14.6e},"
              f" Lap(v) = {laplacian_u(line, 1.7, -0.9, h, 1):>14.6e}")
    print("  The potential of a *three-dimensional* point mass or charge decays")
    print("  as 1/r and is *not* the real part of a holomorphic function; the")
    print("  logarithmic potential is the two-dimensional case, and that is why")
    print("  complex analysis solves 2-D potential problems exactly.")

    mu = 2.5
    dipole = lambda z: mu / z
    print(f"\n  w(z) = mu / z with mu = {mu}.  Writing w = phi + i psi:")
    print(f"    {'x':>7} {'y':>7} {'Re w':>14} {'(mu/r) cos t':>14}"
          f" {'Im w':>14} {'-(mu/r) sin t':>16}")
    for x, y in [(1.0, 0.0), (0.0, 1.0), (1.0, 1.0), (-2.0, 0.5)]:
        uu, vv = parts(dipole, x, y)
        r = math.hypot(x, y)
        theta = math.atan2(y, x)
        print(f"  {x:>7.2f} {y:>7.2f} {uu:>14.8f}"
              f" {mu / r * math.cos(theta):>14.8f} {vv:>14.8f}"
              f" {-mu / r * math.sin(theta):>16.8f}")
    print("  Both parts are harmonic: a 2-D dipole anomaly is a harmonic function")
    print("  of position, which is the reason its field can be continued upward")
    print("  and downward analytically.  Laplacian check:")
    for h in (1e-2, 5e-3, 2.5e-3):
        print(f"    h = {h:.5f}: Lap(Re w) ="
              f" {laplacian_u(dipole, 1.4, 0.9, h, 0):>14.6e}, Lap(Im w) ="
              f" {laplacian_u(dipole, 1.4, 0.9, h, 1):>14.6e}")

    section("6. Equipotentials and flux lines cross at right angles")
    print("  For w = phi + i psi the curves phi = const and psi = const are")
    print("  orthogonal wherever grad w does not vanish, because")
    print("      d w/dz = phi_x + i psi_x = phi_x - i phi_y")
    print("  so (phi_x, phi_y) . (psi_x, psi_y) = phi_x psi_x + phi_y psi_y")
    print("      = phi_x(-phi_y) + phi_y(phi_x) = 0.")
    h = 1e-5
    print(f"  {'x':>7} {'y':>7} {'grad phi . grad psi':>20} {'cos angle':>12}")
    for x, y in [(1.0, 1.0), (0.7, -1.3), (-1.1, 0.6)]:
        # w(z) = mu / z: phi = Re w, psi = Im w are the dipole potential and
        # stream function, and neither one is a coordinate function.
        phi = lambda z: (mu / z).real
        psi = lambda z: (mu / z).imag
        grad_phi = ((phi(complex(x + h, y)) - phi(complex(x - h, y))) / (2 * h),
                    (phi(complex(x, y + h)) - phi(complex(x, y - h))) / (2 * h))
        grad_psi = ((psi(complex(x + h, y)) - psi(complex(x - h, y))) / (2 * h),
                    (psi(complex(x, y + h)) - psi(complex(x, y - h))) / (2 * h))
        dot = grad_phi[0] * grad_psi[0] + grad_phi[1] * grad_psi[1]
        cosang = dot / (math.hypot(*grad_phi) * math.hypot(*grad_psi))
        print(f"  {x:>7.2f} {y:>7.2f} {dot:>20.3e} {cosang:>12.3e}")
    print("  The dot product vanishes to finite-difference precision, which is")
    print("  the geometric content of the Cauchy-Riemann equations.")


    section("7. The half-plane Dirichlet problem is a Poisson integral of an analytic function")
    print("  The Poisson kernel for the upper half plane is")
    print("      P(x - t, y) = (1/pi) y/((x-t)^2 + y^2) = (1/pi) Im[1/(t - z)]")
    print("  with z = x + i y, and the harmonic extension of a boundary value f is")
    print("      phi(x, y) = int_{-inf}^{inf} f(t) P(x - t, y) dt.")
    print("  For f(t) = 1/(1 + t^2) the analytic function is g(z) = 1/(1 - i z),")
    print("  whose real part on the real axis is f and whose only pole is z = -i,")
    print("  in the *lower* half plane.  So the extension must be")
    print("      phi = Re g(z) = (1 + y)/((1 + y)^2 + x^2).")

    def poisson(f, x, y, n=400000):
        # substitute t = tan u to map the whole real line onto (-pi/2, pi/2)
        def value(u):
            t = math.tan(u)
            return f(t) * (y / math.pi) / ((x - t) ** 2 + y ** 2) * (1.0 + t * t)
        return simpson(value, -math.pi / 2, math.pi / 2, n)

    bnd = lambda t: 1.0 / (1.0 + t * t)
    print(f"\n  {'x':>6} {'y':>6} {'Poisson integral':>18} {'Re g(z)':>18}"
          f" {'difference':>11}")
    for x, y in [(0.0, 0.5), (0.75, 0.25), (-1.25, 1.0), (2.0, 0.1)]:
        num = poisson(bnd, x, y)
        closed = (1.0 + y) / ((1.0 + y) ** 2 + x * x)
        print(f"  {x:>6.2f} {y:>6.2f} {num:>18.12f} {closed:>18.12f}"
              f" {abs(num - closed):>11.2e}")
    print("  Boundary values are recovered as y -> 0+:  phi(x, 0.0001) versus")
    print("  f(x):")
    for x in (0.0, 1.0, 3.0):
        print(f"    x = {x:>4.1f}: phi = {poisson(bnd, x, 1e-4):.9f},"
              f" f(x) = {bnd(x):.9f}")
    print("  The extension is harmonic in the upper half plane by finite")
    print("  differences (the closed form, evaluated on a grid):")
    g_real = lambda x, y: (1.0 + y) / ((1.0 + y) ** 2 + x * x)
    for h in (1e-2, 5e-3, 2.5e-3):
        val = (g_real(0.75 + h, 0.25) + g_real(0.75 - h, 0.25)
               + g_real(0.75, 0.25 + h) + g_real(0.75, 0.25 - h)
               - 4 * g_real(0.75, 0.25)) / (h * h)
        print(f"    h = {h:.5f}: Laplacian = {val:>14.6e}")
    print("  This is the bridge to potential fields: solving Laplace's equation in")
    print("  a half plane with a boundary value is taking the real part of an")
    print("  analytic function whose boundary value has that real part.")


if __name__ == "__main__":
    main()
