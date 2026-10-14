"""The integral theorems, checked numerically statement by statement.

Run:  python3 integral_theorems_demo.py
Requires: Python standard library only.

Companion to lesson 01-06-06. Each section computes both sides of a theorem
independently:

  * divergence theorem for a polynomial field on the unit cube,
  * Gauss's law for gravity through a cube (shape-independent flux),
  * Stokes' theorem for a rotating field on a disk, and Green's theorem in 2-D,
  * the mean value property of harmonic functions.

All sources are SYNTHETIC.
"""

import math

G = 6.674e-11


def section(title: str) -> None:
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def norm(v):
    return math.sqrt(sum(c * c for c in v))


def main() -> None:
    section("1. Divergence theorem on the unit cube")
    # F = (x^3 y, y^3 z, z^3 x);  div F = 3x^2 y + 3y^2 z + 3z^2 x; the integral
    # over [0,1]^3 is 3 * (1/3)(1/2) = 1/2 each, total 3/2.
    F = lambda x, y, z: (x ** 3 * y, y ** 3 * z, z ** 3 * x)            # noqa: E731
    dF = lambda x, y, z: 3.0 * (x * x * y + y * y * z + z * z * x)      # noqa: E731
    for n in (50, 200):
        # volume integral of the divergence, midpoint rule
        h = 1.0 / n
        vol = 0.0
        for i in range(n):
            x = (i + 0.5) * h
            for j in range(n):
                y = (j + 0.5) * h
                for k in range(n):
                    z = (k + 0.5) * h
                    vol += dF(x, y, z)
        vol *= h ** 3
        # surface integral of F . n over the six faces
        surf = 0.0
        for axis in range(3):
            for sign in (1.0, -1.0):
                face = 0.0
                for i in range(n):
                    u = (i + 0.5) * h
                    for j in range(n):
                        v = (j + 0.5) * h
                        p = [None, None, None]
                        others = [q for q in range(3) if q != axis]
                        p[axis] = 1.0 if sign > 0 else 0.0
                        p[others[0]] = u
                        p[others[1]] = v
                        face += sign * F(*p)[axis]
                surf += face * h * h
        print(f"n = {n:>3}:  volume integral of div F = {vol:.10f}")
        print(f"          surface flux of F        = {surf:.10f}")
        print(f"          exact 3/2                = {1.5:.10f}")
    print("The surface side is exact here because each face integrand is linear, so")
    print("the midpoint rule is exact; the volume side is a cubic integrand and")
    print("converges from below.")

    section("2. Gauss's law for gravity through a cube: the shape does not matter")
    mass = 1.0e12
    a = 500.0                  # cube half-side; mass at the cube centre
    for n in (60, 240):
        h = 2.0 * a / n
        total = 0.0
        for axis in range(3):
            for sign in (1.0, -1.0):
                face = 0.0
                for i in range(n):
                    u = -a + (i + 0.5) * h
                    for j in range(n):
                        v = -a + (j + 0.5) * h
                        p = [None, None, None]
                        others = [q for q in range(3) if q != axis]
                        p[axis] = sign * a
                        p[others[0]] = u
                        p[others[1]] = v
                        r2 = sum(c * c for c in p)
                        r = math.sqrt(r2)
                        gr = -G * mass / r2                     # g . r_hat
                        # g . n = (g . r_hat) * (r_hat . n); n = sign * e_axis
                        face += sign * gr * p[axis] / r
                total += face * h * h
        print(f"n = {n:>3}:  flux of g through the cube = {total:.6f} m^3/s^2"
              f"   relative error = "
              f"{abs(total + 4 * math.pi * G * mass) / (4 * math.pi * G * mass):.3e}")
    print(f"exact -4*pi*G*M = {-4.0 * math.pi * G * mass:.6f} m^3/s^2")
    print("The same flux would come out of a sphere of any radius, an ellipsoid or")
    print("a cylinder: what matters is the enclosed mass, not the surface shape.")

    section("3. Stokes' theorem and Green's theorem on the unit disk")
    # F = (-y, x, 0) -> curl F = (0, 0, 2)
    Fv = lambda x, y, z: (-y, x, 0.0)                                  # noqa: E731
    n = 20000
    dphi = 2.0 * math.pi / n
    circ = 0.0
    for k in range(n):
        phi = (k + 0.5) * dphi
        x, y = math.cos(phi), math.sin(phi)
        circ += (Fv(x, y, 0.0)[0] * (-math.sin(phi))
                 + Fv(x, y, 0.0)[1] * (math.cos(phi))) * dphi
    print(f"circulation of F on the unit circle        = {circ:.10f}")
    for m in (200, 800):
        h = 1.0 / m
        flux = 0.0
        for i in range(m):
            for j in range(m):
                x = -1.0 + (i + 0.5) * h * 2.0
                y = -1.0 + (j + 0.5) * h * 2.0
                if x * x + y * y <= 1.0:
                    flux += 2.0          # (curl F) . z_hat = 2
        flux *= (2.0 * h) ** 2
        print(f"m = {m:>3}:  flux of curl F over the disk = {flux:.10f}")
    print(f"exact 2*pi                                 = {2.0 * math.pi:.10f}")

    section("4. Mean value property of harmonic functions")
    mass = 1.0e12
    R = 1000.0
    # The mass sits 5000 m from the origin; the test sphere is centred on the
    # origin and has radius 1000 m, so it contains no source and V is harmonic
    # on and inside it.
    source = (5000.0, 0.0, 0.0)

    def V(x, y, z):
        return G * mass / math.sqrt((x - source[0]) ** 2 + (y - source[1]) ** 2
                                    + (z - source[2]) ** 2)

    for n in (100, 400):
        dtheta = math.pi / n
        dphi = 2.0 * math.pi / n
        acc = 0.0
        for i in range(n):
            theta = (i + 0.5) * dtheta
            for j in range(n):
                phi = (j + 0.5) * dphi
                x = R * math.sin(theta) * math.cos(phi)
                y = R * math.sin(theta) * math.sin(phi)
                z = R * math.cos(theta)
                acc += V(x, y, z) * math.sin(theta)
        acc *= dtheta * dphi / (4.0 * math.pi)
        print(f"n = {n:>3}:  sphere average of V = {acc:.9e}"
              f"   V at the centre = {V(0.0, 0.0, 0.0):.9e}"
              f"   rel. diff = {abs(acc - V(0.0, 0.0, 0.0)) / V(0.0, 0.0, 0.0):.3e}")
    print("V is harmonic on and inside that sphere, so its average equals its value")
    print("at the centre, however large the sphere is made (up to the source).")

    def r2(x, y, z):
        return x * x + y * y + z * z

    n = 400
    dtheta = math.pi / n
    dphi = 2.0 * math.pi / n
    acc = 0.0
    for i in range(n):
        theta = (i + 0.5) * dtheta
        for j in range(n):
            phi = (j + 0.5) * dphi
            acc += R * R * math.sin(theta)
    acc *= dtheta * dphi / (4.0 * math.pi)
    print(f"same test for f = x^2 + y^2 + z^2: sphere average = {acc:.6f}"
          f"   centre value = {r2(0.0, 0.0, 0.0):.6f}")
    print(f"analytic average of f over the sphere is R^2 = {R * R:.6f}; the numeric")
    print("value is off by 2.6e-6, which is midpoint truncation error on sin(theta).")
    print("The centre value 0 is off by 100 per cent: the laplacian of f is 6, not 0,")
    print("so the mean value property fails. It is a test of harmonicity.")


if __name__ == "__main__":
    main()
