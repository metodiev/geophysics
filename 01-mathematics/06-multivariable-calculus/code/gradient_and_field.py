"""Gradients, directional derivatives and fields obtained from a potential.

Run:  python3 gradient_and_field.py
Requires: Python standard library only.

Companion to lesson 01-06-01. Every number printed below is computed at run
time; the lesson quotes these outputs rather than hand-copied values.

Sign convention used throughout this module (the gravity/geodesy convention):

    V(r) = G * sum over sources of  m / |r - r_source|      (positive potential)
    g    = grad V                                           (field = gradient)
    div g = laplacian V = -4*pi*G*rho                       (Poisson)
    g_z  = -dV/dz                                           (survey convention)

All masses and distances here are SYNTHETIC: they are chosen to make the
arithmetic readable, not to represent a real survey.
"""

import math

G = 6.674e-11  # m^3 kg^-1 s^-2, rounded value used throughout the module
MGAL = 1.0e-5  # m s^-2 per mGal


def section(title: str) -> None:
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def norm(v):
    return math.sqrt(sum(c * c for c in v))


def potential_point(mass, x, y, z):
    """V = G*M/r for a point mass at the origin."""
    r = math.sqrt(x * x + y * y + z * z)
    return G * mass / r


def grad_central(f, p, h):
    """Central-difference gradient of the scalar field f at the point p."""
    x, y, z = p
    gx = (f(x + h, y, z) - f(x - h, y, z)) / (2.0 * h)
    gy = (f(x, y + h, z) - f(x, y - h, z)) / (2.0 * h)
    gz = (f(x, y, z + h) - f(x, y, z - h)) / (2.0 * h)
    return (gx, gy, gz)


def main() -> None:
    mass = 1.0e11          # kg  (SYNTHETIC: a ~200 m radius, 3000 kg/m^3 body)
    p = (400.0, -300.0, 1200.0)
    r = norm(p)

    f = lambda x, y, z: potential_point(mass, x, y, z)          # noqa: E731

    # grad(G*M/r) = -G*M*r_hat/r^2 = -G*M*(x,y,z)/r^3
    analytic = tuple(-G * mass * c / r ** 3 for c in p)

    section("1. The gradient of the potential is the field (times -1)")
    numeric = grad_central(f, p, 1.0)
    print(f"observation point          = {p} m,  |r| = {r:.1f} m")
    print(f"V at the point             = {f(*p):.6e} m^2/s^2")
    print(f"numeric grad V   (h = 1 m) = ({numeric[0]: .6e}, {numeric[1]: .6e}, {numeric[2]: .6e})")
    print(f"analytic grad V            = ({analytic[0]: .6e}, {analytic[1]: .6e}, {analytic[2]: .6e})")
    rel = norm(tuple(a - b for a, b in zip(numeric, analytic))) / norm(analytic)
    print(f"relative error             = {rel:.3e}")
    print(f"|grad V|                   = {norm(analytic):.6e} m/s^2"
          f" = {norm(analytic) / MGAL:.4f} mGal")
    print("Note: grad V points TOWARDS the mass; g = grad V, so |g| = G*M/r^2.")

    section("2. Central differences are second order; forward differences are not")
    print("central difference, step h:")
    for h in (10.0, 1.0, 0.1, 0.01, 0.001):
        num = grad_central(f, p, h)
        rel = norm(tuple(a - b for a, b in zip(num, analytic))) / norm(analytic)
        print(f"   h = {h:>7} m    relative error = {rel:.3e}")
    h = 1.0
    fwd = (f(p[0] + h, p[1], p[2]) - f(*p)) / h
    rel_fwd = abs(fwd - analytic[0]) / abs(analytic[0])
    print(f"forward difference dV/dx, h = 1 m: relative error = {rel_fwd:.3e}")
    print("The central-difference error falls by ~100 per decade of h until")
    print("round-off takes over; the forward difference only falls by ~10.")

    section("3. Directional derivative: D_u V = grad V . u_hat")
    # Straight down: the direction in which a gravimeter senses the field.
    u = (0.0, 0.0, -1.0)
    t = 1.0
    dv_dz_numeric = (f(p[0], p[1], p[2] + t) - f(p[0], p[1], p[2] - t)) / (2.0 * t)
    dv_dz_analytic = analytic[2]
    print(f"dV/dz (numeric, t = 1 m)   = {dv_dz_numeric:.6e} m/s^2")
    print(f"dV/dz (analytic)           = {dv_dz_analytic:.6e} m/s^2")
    print(f"grad V . (0,0,-1)          = {sum(a * b for a, b in zip(analytic, u)):.6e} m/s^2")
    print(f"reported gravity -dV/dz    = {-dv_dz_analytic / MGAL:.4f} mGal"
          "  (downward positive)")

    section("4. The gradient is perpendicular to the level surface")
    rhat = tuple(c / r for c in p)
    # w = z_hat x r_hat is perpendicular to r_hat by construction
    w = (1.0 * rhat[1] - 0.0 * rhat[2], 0.0 * rhat[2] - 1.0 * rhat[0], 0.0)
    w = tuple(c / norm(w) for c in w)
    print(f"r_hat . w_hat              = {sum(a * b for a, b in zip(rhat, w)):.3e}")
    print(f"grad V . w_hat             = {sum(a * b for a, b in zip(analytic, w)):.3e}")
    t = 100.0
    v_plus = f(p[0] + t * w[0], p[1] + t * w[1], p[2] + t * w[2])
    v_minus = f(p[0] - t * w[0], p[1] - t * w[1], p[2] - t * w[2])
    along = (v_plus - v_minus) / (2.0 * t)
    # Predict the second-order change: V(t) - V(0) ~ -(G M / r) * t^2 / (2 r^2).
    second_order = -f(*p) * t ** 2 / (2.0 * r ** 2)
    exact = potential_point(mass, *[p[i] + t * w[i] for i in range(3)]) - f(*p)
    print(f"central difference along w  = {along:.3e} m^2/s^2   (t = {t:.0f} m)")
    print(f"V at +t*w  -  V at -t*w     = {v_plus - v_minus:.3e} m^2/s^2")
    print(f"V(+t*w) - V(p), second order= {second_order:.6e} m^2/s^2")
    print(f"V(+t*w) - V(p), exact       = {exact:.6e} m^2/s^2")
    print("Both sample points lie on the same sphere about the mass, so they lie on")
    print("the same level surface and V is identical at them: the first-order term")
    print("grad V . w vanishes exactly, leaving a purely second-order change.")

    section("5. A second, independent field: travel time and the eikonal equation")
    v = 3000.0            # m/s  (SYNTHETIC homogeneous rock)

    def travel_time(x, y, z):
        return math.sqrt(x * x + y * y + z * z) / v

    gT = grad_central(travel_time, p, 0.1)
    print(f"|grad T| (numeric)          = {norm(gT):.9e} s/m")
    print(f"1/v                        = {1.0 / v:.9e} s/m")
    print(f"relative difference        = {abs(norm(gT) - 1.0 / v) / (1.0 / v):.3e}")
    print("In a homogeneous medium the travel-time field obeys |grad T| = 1/v:")
    print("the eikonal equation that ray tracing solves numerically.")

    section("6. Second derivatives: the gravity gradient tensor T_zz")
    depth = 800.0         # m
    obs = (0.0, 0.0, 0.0)
    # Mass at (0, 0, -depth) seen from (0, 0, z): g_z(z) = -dV/dz = G*M/(z+depth)^2
    gz = lambda z: G * mass / (z + depth) ** 2                            # noqa: E731
    d2V_dz2 = (potential_point(mass, 0.0, 0.0, depth + 1.0)
               - 2.0 * potential_point(mass, 0.0, 0.0, depth)
               + potential_point(mass, 0.0, 0.0, depth - 1.0)) / 1.0 ** 2
    Tzz_numeric = (gz(1.0) - gz(-1.0)) / 2.0
    Tzz_analytic = -2.0 * G * mass / depth ** 3
    print(f"g_z at the surface         = {gz(0.0):.6e} m/s^2"
          f" = {gz(0.0) / MGAL:.4f} mGal")
    print(f"d2V/dz2 (numeric, 1 m grid)= {d2V_dz2:.6e} 1/s^2")
    print(f"2*G*M/depth^3              = {2.0 * G * mass / depth ** 3:.6e} 1/s^2")
    print(f"T_zz = dg_z/dz (numeric)   = {Tzz_numeric:.6e} 1/s^2 = {Tzz_numeric * 1e9:.4f} E")
    print(f"T_zz = -2*G*M/depth^3      = {Tzz_analytic:.6e} 1/s^2 = {Tzz_analytic * 1e9:.4f} E")
    print("Observed: d2V/dz2 = +2GM/d^3 and T_zz = -2GM/d^3. The sign flip is")
    print("just the survey sign convention; the magnitude is what a gradiometer sees.")


if __name__ == "__main__":
    main()
