"""Gradient, divergence, curl and Laplacian in cylindrical and spherical frames.

Run:  python3 curvilinear_operators_demo.py
Requires: Python standard library only.

Companion to lesson 01-15-04.

Method. Every curvilinear formula is tested the same way: take an analytic
Cartesian field, express it in the curvilinear components, apply the formula
using NUMERICAL derivatives in the curvilinear coordinates, and compare with the
Cartesian operator applied to the same field at the same physical point. The
numerical derivatives carry no information about the formula, so agreement is
evidence that the scale factors and the metric weights are right.

Potential convention (identical to lesson 01-06-08): V = GM/r, g = grad V,
laplacian(V) = -4 pi G rho, hence laplacian(1/r) = -4 pi delta^3(r).
"""

import math

H = 1.0e-5
G = 6.674e-11           # m^3 kg^-1 s^-2


def section(title: str) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


# --------------------------------------------------------------------------
# Coordinate maps
# --------------------------------------------------------------------------

def cyl(x, y, z):
    return math.hypot(x, y), math.atan2(y, x), z


def sph(x, y, z):
    r = math.sqrt(x * x + y * y + z * z)
    return r, math.acos(max(-1.0, min(1.0, z / r))), math.atan2(y, x)


def from_cyl(rho, phi, z):
    return rho * math.cos(phi), rho * math.sin(phi), z


def from_sph(r, theta, phi):
    return (r * math.sin(theta) * math.cos(phi),
            r * math.sin(theta) * math.sin(phi),
            r * math.cos(theta))


def e_cyl(phi):
    return ((math.cos(phi), math.sin(phi), 0.0),
            (-math.sin(phi), math.cos(phi), 0.0),
            (0.0, 0.0, 1.0))


def e_sph(theta, phi):
    return ((math.sin(theta) * math.cos(phi), math.sin(theta) * math.sin(phi), math.cos(theta)),
            (math.cos(theta) * math.cos(phi), math.cos(theta) * math.sin(phi), -math.sin(theta)),
            (-math.sin(phi), math.cos(phi), 0.0))


def d(f, q, i):
    """Central difference of a scalar function of a coordinate triple."""
    a, b = list(q), list(q)
    a[i] += H
    b[i] -= H
    return (f(a) - f(b)) / (2.0 * H)


def dv(field, q, i, k):
    """d(field_k)/dq_i for a vector field of a curvilinear coordinate triple."""
    a, b = list(q), list(q)
    a[i] += H
    b[i] -= H
    return (field(a)[k] - field(b)[k]) / (2.0 * H)


def _component(field, p, k):
    return field(p[0], p[1], p[2])[k]


def d_comp(field, p, i, k):
    """d(field_k)/dx_i by central differences."""
    a, b = list(p), list(p)
    a[i] += H
    b[i] -= H
    return (_component(field, a, k) - _component(field, b, k)) / (2.0 * H)


def cart_operator(field, p, kind):
    """div or curl of a Cartesian VECTOR field, by central differences."""
    if kind == "div":
        return sum(d_comp(field, p, i, i) for i in range(3))
    perm = ((1, 2), (2, 0), (0, 1))
    out = []
    for i in range(3):
        j, k = perm[i]
        out.append(d_comp(field, p, j, k) - d_comp(field, p, k, j))
    return out


def lap_cart(f, p):
    """Laplacian of a Cartesian SCALAR field, by central differences."""
    total = 0.0
    for i in range(3):
        a, b = list(p), list(p)
        a[i] += H
        b[i] -= H
        total += (f(a[0], a[1], a[2]) - 2.0 * f(p[0], p[1], p[2])
                  + f(b[0], b[1], b[2])) / (H * H)
    return total


# --------------------------------------------------------------------------
# 1. Scale factors come out of the parametrisation
# --------------------------------------------------------------------------

section("1. Scale factors h_i = |d r / d q_i|, computed and compared with theory")

point_cart = (1.3, 0.9, 2.1)
rho, phi, z = cyl(*point_cart)
r, theta, phis = sph(*point_cart)

h_cyl = []
for i in range(3):
    a, b = list((rho, phi, z)), list((rho, phi, z))
    a[i] += H
    b[i] -= H
    pa, pb = from_cyl(*a), from_cyl(*b)
    h_cyl.append(math.sqrt(sum((pa[k] - pb[k]) ** 2 for k in range(3))) / (2.0 * H))
h_sph = []
for i in range(3):
    a, b = list((r, theta, phis)), list((r, theta, phis))
    a[i] += H
    b[i] -= H
    pa, pb = from_sph(*a), from_sph(*b)
    h_sph.append(math.sqrt(sum((pa[k] - pb[k]) ** 2 for k in range(3))) / (2.0 * H))

print(f"  test point (x,y,z) = {point_cart}")
print(f"  cylindrical (rho, phi, z)    = ({rho:.6f}, {phi:.6f}, {z:.6f})")
print(f"    h_rho = {h_cyl[0]:.12f}   (theory 1)")
print(f"    h_phi = {h_cyl[1]:.12f}   (theory rho = {rho:.12f})")
print(f"    h_z   = {h_cyl[2]:.12f}   (theory 1)")
print(f"  spherical (r, theta, phi)    = ({r:.6f}, {theta:.6f}, {phis:.6f})")
print(f"    h_r     = {h_sph[0]:.12f}   (theory 1)")
print(f"    h_theta = {h_sph[1]:.12f}   (theory r = {r:.12f})")
print(f"    h_phi   = {h_sph[2]:.12f}   (theory r sin(theta) = "
      f"{r * math.sin(theta):.12f})")
print("  One of the two '1's is the reason nobody writes the metric out in")
print("  Cartesian coordinates: the coordinates are already arc lengths.")


# --------------------------------------------------------------------------
# 2. Gradient in spherical coordinates
# --------------------------------------------------------------------------

section("2. Gradient: spherical formula against Cartesian differences")

def f_cart(x, y, z):
    return x * math.sqrt(x * x + y * y + z * z)          # = r^2 sin(theta) cos(phi)


def f_sph(q):
    rr, tt, pp = q
    return rr * rr * math.sin(tt) * math.cos(pp)


q_sph = (r, theta, phis)
grad_cart = [d(lambda q: f_cart(q[0], q[1], q[2]), point_cart, i) for i in range(3)]

gr = d(f_sph, q_sph, 0)
gt = d(f_sph, q_sph, 1) / r
gp = d(f_sph, q_sph, 2) / (r * math.sin(theta))
basis = e_sph(theta, phis)
grad_sph_cart = [gr * basis[0][i] + gt * basis[1][i] + gp * basis[2][i]
                 for i in range(3)]

print(f"  f = r^2 sin(theta) cos(phi) = x r")
print(f"  d f / d r, (1/r) d f / d theta, (1/(r sin theta)) d f / d phi")
print(f"     = {gr:.6f}, {gt:.6f}, {gp:.6f}")
print(f"  Cartesian differences   = {[f'{v:.6f}' for v in grad_cart]}")
print(f"  spherical formula, in Cartesian components = "
      f"{[f'{v:.6f}' for v in grad_sph_cart]}")
print(f"  largest difference = "
      f"{max(abs(grad_cart[i] - grad_sph_cart[i]) for i in range(3)):.3e}")
print("  The 1/r and 1/(r sin theta) factors are not decoration: they convert a")
print("  derivative with respect to an angle into a derivative per unit length.")


# --------------------------------------------------------------------------
# 3. Divergence in cylindrical coordinates
# --------------------------------------------------------------------------

section("3. Divergence: cylindrical formula against Cartesian differences")

def FIELD_DIV(x, y, z):
    return (y * z + x, z * x + y * y, x * y + z ** 3)


def F_cyl(q):
    rr, pp, zz = q
    x, y, z2 = from_cyl(rr, pp, zz)
    fx, fy, fz = FIELD_DIV(x, y, z2)
    er, ep, ez = e_cyl(pp)
    return (fx * er[0] + fy * er[1], fx * ep[0] + fy * ep[1], fz)


qc = (rho, phi, z)
F_rho, F_phi, F_z = F_cyl(qc)
div_cart = cart_operator(FIELD_DIV, point_cart, "div")
div_cyl = (d(lambda q: q[0] * F_cyl(q)[0], qc, 0) / rho
           + dv(F_cyl, qc, 1, 1) / rho
           + dv(F_cyl, qc, 2, 2))
wrong = (d(lambda q: q[0] * F_cyl(q)[0], qc, 0)
         + dv(F_cyl, qc, 1, 1) / rho + dv(F_cyl, qc, 2, 2))
print(f"  F in cylindrical components at the point = "
      f"({F_rho:.6f}, {F_phi:.6f}, {F_z:.6f})")
print(f"  (1/rho) d(rho F_rho)/d rho = {d(lambda q: q[0] * F_cyl(q)[0], qc, 0) / rho:.6f}")
print(f"  (1/rho) d F_phi / d phi    = {dv(F_cyl, qc, 1, 1) / rho:.6f}")
print(f"  d F_z / d z                = {dv(F_cyl, qc, 2, 2):.6f}")
print(f"  cylindrical formula total  = {div_cyl:.6f}")
print(f"  Cartesian differences      = {div_cart:.6f}")
print(f"  difference                 = {abs(div_cyl - div_cart):.3e}")
print(f"  dropping the 1/rho factor of the first term gives {wrong:.6f}, "
      f"wrong by {abs(wrong - div_cart):.3e}")
print("  Divergence is a scalar, so it cannot depend on the frame; a mismatch")
print("  can only mean the formula is wrong. That is why it is a clean test.")


# --------------------------------------------------------------------------
# 4. Divergence in spherical coordinates
# --------------------------------------------------------------------------

section("4. Divergence: spherical formula against Cartesian differences")


def F_sph(q):
    rr, tt, pp = q
    x, y, z2 = from_sph(rr, tt, pp)
    fx, fy, fz = FIELD_DIV(x, y, z2)
    er, et, ep = e_sph(tt, pp)
    return (fx * er[0] + fy * er[1] + fz * er[2],
            fx * et[0] + fy * et[1] + fz * et[2],
            fx * ep[0] + fy * ep[1] + fz * ep[2])


F_r, F_t, F_p = F_sph(q_sph)
term_r = d(lambda q: q[0] ** 2 * F_sph(q)[0], q_sph, 0) / (r * r)
term_t = (d(lambda q: math.sin(q[1]) * F_sph(q)[1], q_sph, 1)
          / (r * math.sin(theta)))
term_p = dv(F_sph, q_sph, 2, 2) / (r * math.sin(theta))
div_sph = term_r + term_t + term_p
print(f"  F in spherical components = ({F_r:.6f}, {F_t:.6f}, {F_p:.6f})")
print(f"  (1/r^2) d(r^2 F_r)/dr        = {term_r:.6f}")
print(f"  (1/(r sin th)) d(sin th F_th)/d th = {term_t:.6f}")
print(f"  (1/(r sin th)) d F_phi/d phi       = {term_p:.6f}")
print(f"  spherical formula total      = {div_sph:.6f}")
print(f"  Cartesian differences        = {div_cart:.6f}")
print(f"  difference                   = {abs(div_sph - div_cart):.3e}")
print("  Note where sin(theta) appears: it is both the area weight of the theta")
print("  direction and, once divided out, the length scale of the phi direction.")


# --------------------------------------------------------------------------
# 5. Curl in spherical coordinates
# --------------------------------------------------------------------------

section("5. Curl: spherical formula against Cartesian differences")


def FIELD_CURL(x, y, z):
    return (-y * z, x * z, x * x - y * y)


def G_sph(q):
    rr, tt, pp = q
    x, y, z2 = from_sph(rr, tt, pp)
    gx, gy, gz = FIELD_CURL(x, y, z2)
    er, et, ep = e_sph(tt, pp)
    return (gx * er[0] + gy * er[1] + gz * er[2],
            gx * et[0] + gy * et[1] + gz * et[2],
            gx * ep[0] + gy * ep[1] + gz * ep[2])


curl_cart = cart_operator(FIELD_CURL, point_cart, "curl")
st = math.sin(theta)
curl_r = (d(lambda q: math.sin(q[1]) * G_sph(q)[2], q_sph, 1)
          - dv(G_sph, q_sph, 2, 1)) / (r * st)
curl_t = (dv(G_sph, q_sph, 2, 0) / st
          - d(lambda q: q[0] * G_sph(q)[2], q_sph, 0)) / r
curl_p = (d(lambda q: q[0] * G_sph(q)[1], q_sph, 0)
          - dv(G_sph, q_sph, 1, 0)) / r
basis = e_sph(theta, phis)
curl_sph_cart = [curl_r * basis[0][i] + curl_t * basis[1][i] + curl_p * basis[2][i]
                 for i in range(3)]
print(f"  G = (-y z, x z, x^2 - y^2)")
print(f"  Cartesian curl               = {[f'{v:.6f}' for v in curl_cart]}")
print(f"  spherical formula, Cartesian components = "
      f"{[f'{v:.6f}' for v in curl_sph_cart]}")
print(f"  largest difference = "
      f"{max(abs(curl_cart[i] - curl_sph_cart[i]) for i in range(3)):.3e}")
print("  The three spherical curl expressions look unrelated to the Cartesian")
print("  ones; they are the same object written in a basis that turns.")


# --------------------------------------------------------------------------
# 6. Laplacian
# --------------------------------------------------------------------------

section("6. Laplacian: r^2, x r, and the two-dimensional logarithm")


def lap_sph(fs, q):
    rr, tt, pp = q
    t1 = d(lambda qq: qq[0] ** 2 * d(fs, qq, 0), q, 0) / (rr * rr)
    t2 = (d(lambda qq: math.sin(qq[1]) * d(fs, qq, 1), q, 1)
          / (rr * rr * math.sin(tt)))
    t3 = d(lambda qq: d(fs, qq, 2), q, 2) / (rr * rr * math.sin(tt) ** 2)
    return t1 + t2 + t3


def lap_cyl(fs, q):
    rr, pp, zz = q
    t1 = d(lambda qq: qq[0] * d(fs, qq, 0), q, 0) / rr
    t2 = d(lambda qq: d(fs, qq, 1), q, 1) / (rr * rr)
    t3 = d(lambda qq: d(fs, qq, 2), q, 2)
    return t1 + t2 + t3


print("  laplacian(r^2) = 6 in three dimensions, 4 in two:")
print(f"    Cartesian: {lap_cart(lambda x, y, z: x * x + y * y + z * z, point_cart):.6f}")
print(f"    spherical: "
      f"{lap_sph(lambda q: q[0] ** 2, q_sph):.6f}")
print(f"    cylindrical in rho only: "
      f"{lap_cyl(lambda q: q[0] ** 2, qc):.6f}")


def f1_cart(x, y, z):
    return 1.0 / math.sqrt(x * x + y * y + z * z)


print("\n  laplacian(1/r) = 0 away from the origin. Evaluate on the equator")
print("  (theta = pi/2) so that the 1/sin(theta) factors are harmless:")
for radius in (0.5, 1.0, 3.0, 10.0):
    qq = (radius, 0.5 * math.pi, 0.0)
    value = lap_sph(lambda q: 1.0 / q[0], qq)
    scale = 1.0 / radius ** 3
    print(f"    r = {radius:5.1f}: {value:+.3e}   relative to the scale 1/r^3 = "
          f"{scale:.3e}: {abs(value) / scale:.1e}"
          f"   (Cartesian: {lap_cart(f1_cart, (radius, 0.0, 0.0)):+.3e})")
print("  Both frames give a residual that is the finite-difference error, not")
print("  zero digit for digit, because 1/r is not a polynomial.")

print("\n  but the flux of grad(1/r) through a sphere is -4 pi at EVERY radius,")
print("  which is the whole content of laplacian(1/r) = -4 pi delta^3(r):")
n_th = 20000
for radius in (0.5, 1.0, 3.0, 10.0):
    # grad(1/r) = -r_hat/r^2, so grad(1/r) . n dA = -(1/r^2) r^2 sin(th) dth dphi.
    # The phi integral is exact (the integrand is constant in phi) and gives 2 pi.
    total = 0.0
    for a in range(n_th):
        th = math.pi * (a + 0.5) / n_th
        total += -(1.0 / radius ** 2) * radius ** 2 * math.sin(th) * (math.pi / n_th)
    total *= 2.0 * math.pi
    print(f"    r = {radius:5.1f}: flux = {total:.10f}    -4 pi = {-4 * math.pi:.10f}")
print("  A function whose Laplacian integrates to a nonzero number while being")
print("  zero pointwise can only be zero almost everywhere: the source is a")
print("  point. This is the statement the delta function exists to make.")


# --------------------------------------------------------------------------
# 7. Gauss's law for a uniform sphere, by the divergence theorem
# --------------------------------------------------------------------------

section("7. Gauss's law inside a uniform sphere, both sides computed")

RHO_BODY = 5514.0        # kg/m^3, the Earth's mean density
R_BODY = 6.371e6         # m, the Earth's mean radius
g_surface = (4.0 / 3.0) * math.pi * G * RHO_BODY * R_BODY
mass = (4.0 / 3.0) * math.pi * RHO_BODY * R_BODY ** 3
print(f"  uniform sphere: rho = {RHO_BODY:.0f} kg/m^3, R = {R_BODY:.3e} m")
print(f"  mass M = 4 pi R^3 rho / 3        = {mass:.4e} kg")
print(f"  surface gravity (4/3) pi G rho R = {g_surface:.4f} m/s^2")
print(f"  GM/R^2 in the same model        = {G * mass / R_BODY ** 2:.4f} m/s^2")
print("  (the two agree because both are the same model; the Earth's real")
print("   surface gravity is close to 9.82 m/s^2, but for a density profile")
print("   that is not uniform, and the agreement here is a coincidence of")
print("   using the true mean density in a uniform model)")

print("\n  laplacian(V) = -4 pi G rho inside, 0 outside. Work in the")
print("  dimensionless radius x = r/R and multiply the result by G rho, so the")
print("  finite differences resolve the curvature instead of drowning in V:")
for frac in (0.25, 0.50, 0.90):
    lap_scaled = lap_sph(lambda q: (2.0 / 3.0) * math.pi * (3.0 - q[0] ** 2),
                         (frac, 0.5 * math.pi, 0.0))
    print(f"    x = {frac:.2f}: laplacian(V) = {G * RHO_BODY * lap_scaled:+.6e}"
          f"   -4 pi G rho = {-4 * math.pi * G * RHO_BODY:+.6e}")
for frac in (1.5, 2.5):
    lap_scaled = lap_sph(lambda q: (4.0 / 3.0) * math.pi / q[0],
                         (frac, 0.5 * math.pi, 0.0))
    print(f"    x = {frac:.2f}: laplacian(V) = {G * RHO_BODY * lap_scaled:+.3e}"
          f"   (Laplace outside, i.e. {abs(lap_scaled) / (4 * math.pi):.1e}"
          f" of the interior value)")
print("  Scaling by R first is not a trick: it is the standard practice of")
print("  non-dimensionalising before differencing, and it is the difference")
print("  between a converged answer and numerical noise.")

print("\n  divergence theorem: volume integral of div g against the flux:")
n_r = 40000
vol_integral = 0.0
for a in range(n_r):
    rr = R_BODY * (a + 0.5) / n_r
    # integrate -4 pi G rho over the shell 4 pi r^2 dr, with the angular
    # integrals already done exactly (they contribute 4 pi)
    vol_integral += (-4.0 * math.pi * G * RHO_BODY) * 4.0 * math.pi * rr ** 2 * (R_BODY / n_r)
flux = (-(4.0 / 3.0) * math.pi * G * RHO_BODY * R_BODY) * 4.0 * math.pi * R_BODY ** 2
print(f"    volume integral of div g over the sphere = {vol_integral:.6e} m^3/s^2")
print(f"    flux of g through r = R                  = {flux:.6e} m^3/s^2")
print(f"    relative difference = {abs(vol_integral - flux) / abs(flux):.2e}")
print("  A radial field of this form has divergence -4 pi G rho everywhere")
print("  inside; the flux through the boundary is what a gravimeter at the")
print("  surface can actually see. Gauss's law says the two must agree.")


def main() -> None:
    print("Curvilinear differential operators, verified against Cartesian ones")


if __name__ == "__main__":
    main()
