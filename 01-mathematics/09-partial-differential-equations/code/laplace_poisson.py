"""Laplace and Poisson equations: harmonic functions, uniqueness, and the
non-uniqueness of potential-field inversion.

Run:  python3 laplace_poisson.py
Requires: Python standard library only.

Companion to lesson 01-09-04 (Laplace and Poisson Equations in Earth Systems).

Sections
    1. Laplace's equation on a square: relaxation, mean value property,
       maximum principle
    2. Poisson's equation: second-order convergence to a known solution
    3. Uniqueness of the Dirichlet problem in practice
    4. Why potential-field inversion is not unique:
       (a) a uniform ball and a point mass have the same exterior potential
       (b) any spherically symmetric perturbation of zero total mass has zero
           exterior potential - a concrete null space

Sign convention throughout: V is positive, g = grad V, laplacian(V) = -4 pi G rho
outside sources laplacian(V) = 0. All bodies and grids are SYNTHETIC.
"""

import math

G = 6.674e-11


def section(title: str) -> None:
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


# ----------------------------------------------------------------------
# 1-3. Laplace and Poisson on a square
# ----------------------------------------------------------------------

def sor_2d(n: int, boundary, rhs, tol: float = 1e-11,
           max_iter: int = 400_000, start: float = 0.0):
    """Solve -laplacian(u) = rhs on a unit square with Dirichlet boundary.

    Successive over-relaxation with the optimal relaxation factor for the
    five-point Laplacian on an n x n interior grid.  ``boundary(x, y)`` gives
    the boundary value.  Returns (u, iterations, final residual).
    """
    h = 1.0 / (n + 1)
    omega = 2.0 / (1.0 + math.sin(math.pi * h))
    u = [[start for _ in range(n)] for _ in range(n)]
    for iteration in range(1, max_iter + 1):
        residual = 0.0
        for j in range(n):
            y = (j + 1) * h
            for i in range(n):
                x = (i + 1) * h
                left = u[j][i - 1] if i > 0 else boundary(0.0, y)
                right = u[j][i + 1] if i < n - 1 else boundary(1.0, y)
                down = u[j - 1][i] if j > 0 else boundary(x, 0.0)
                up = u[j + 1][i] if j < n - 1 else boundary(x, 1.0)
                target = 0.25 * (left + right + down + up + h * h * rhs(x, y))
                change = omega * (target - u[j][i])
                u[j][i] += change
                residual = max(residual, abs(change))
        if residual < tol:
            return u, iteration, residual
    return u, max_iter, residual


def report_laplace() -> None:
    section("1. Laplace's equation on the unit square by successive over-relaxation")
    print("BC: u(x,1) = sin(pi x), u = 0 on the other three sides.")
    print("Exact harmonic solution: u = sinh(pi y) sin(pi x) / sinh(pi).")

    def boundary(x, y):
        if abs(y - 1.0) < 1e-12:
            return math.sin(math.pi * x)
        return 0.0

    def exact(x, y):
        return math.sinh(math.pi * y) * math.sin(math.pi * x) / math.sinh(math.pi)

    print(f"\n  {'N':>5}{'dx':>10}{'iterations':>12}{'max error':>13}{'order':>8}")
    previous = None
    last_field = None
    n_last = 0
    for n in (9, 19, 39, 79):
        u, iters, _res = sor_2d(n, boundary, lambda x, y: 0.0)
        h = 1.0 / (n + 1)
        err = max(abs(u[j][i] - exact((i + 1) * h, (j + 1) * h))
                  for j in range(n) for i in range(n))
        order = "" if previous is None else f"{math.log2(previous / err):.2f}"
        print(f"  {n:>5}{h:>10.4f}{iters:>12}{err:>13.3e}{order:>8}")
        previous = err
        last_field, n_last = u, n

    print("\n  Order ~ 2: the five-point stencil is second-order accurate. SOR with")
    print("  the optimal factor converges in O(N) iterations, which is why elliptic")
    print("  solvers are written as linear algebra and not as long time marches.")

    h = 1.0 / (n_last + 1)
    u = last_field
    worst_mean = 0.0
    interior_max = -1e300
    boundary_max = -1e300
    for j in range(1, n_last - 1):
        for i in range(1, n_last - 1):
            mean = 0.25 * (u[j][i - 1] + u[j][i + 1] + u[j - 1][i] + u[j + 1][i])
            worst_mean = max(worst_mean, abs(mean - u[j][i]))
            interior_max = max(interior_max, u[j][i])
    for i in range(n_last):
        boundary_max = max(boundary_max,
                           u[0][i], u[n_last - 1][i], u[i][0], u[i][n_last - 1])
    print(f"\n  Mean value property at converged state: the largest deviation of an")
    print(f"  interior node from the average of its four neighbours is {worst_mean:.2e}")
    print(f"  (zero to the residual tolerance of 1e-11, as Laplace's equation requires).")
    print(f"\n  Maximum principle: max interior = {interior_max:.6f}, "
          f"max on the boundary = {boundary_max:.6f}")
    print(f"  Interior <= boundary: {interior_max <= boundary_max + 1e-12}. A harmonic")
    print("  function attains its extremes on the boundary, so an interior")
    print("  extremum in a potential-field map is evidence of a source or of noise.")


def report_poisson() -> None:
    section("2. Poisson's equation: -laplacian(u) = f with a known solution")
    print("Take u = sin(pi x) sin(pi y), so f = 2 pi^2 sin(pi x) sin(pi y).")
    print("Solve with u = 0 on the boundary and compare with the exact u.")

    def boundary(_x, _y):
        return 0.0

    def rhs(x, y):
        return 2.0 * math.pi ** 2 * math.sin(math.pi * x) * math.sin(math.pi * y)

    print(f"\n  {'N':>5}{'dx':>10}{'iterations':>12}{'max error':>13}{'order':>8}")
    previous = None
    for n in (9, 19, 39, 79):
        u, iters, _res = sor_2d(n, boundary, rhs)
        h = 1.0 / (n + 1)
        err = max(abs(u[j][i] - math.sin(math.pi * (i + 1) * h)
                      * math.sin(math.pi * (j + 1) * h))
                  for j in range(n) for i in range(n))
        order = "" if previous is None else f"{math.log2(previous / err):.2f}"
        print(f"  {n:>5}{h:>10.4f}{iters:>12}{err:>13.3e}{order:>8}")
        previous = err
    print("\n  Order ~ 2. Poisson's equation is the elliptic equation of")
    print("  potential-field geophysics: -laplacian(V) = 4 pi G rho in the sign")
    print("  convention where V is the potential of positive mass.")


def report_uniqueness() -> None:
    section("3. Uniqueness: the boundary data, not the iteration, fixes the solution")

    def boundary(x, y):
        if abs(y - 1.0) < 1e-12:
            return math.sin(math.pi * x)
        return 0.0

    u_a, iters_a, _ = sor_2d(29, boundary, lambda x, y: 0.0, start=0.0)
    u_b, iters_b, _ = sor_2d(29, boundary, lambda x, y: 0.0, start=1.0)
    diff = max(abs(u_a[j][i] - u_b[j][i]) for j in range(29) for i in range(29))
    print(f"  Starting from u = 0 every internal node:   {iters_a} iterations")
    print(f"  Starting from u = 1 every internal node:   {iters_b} iterations")
    print(f"  Max difference between the two converged fields: {diff:.3e}")
    print("\n  Different initial guesses, same answer: the Dirichlet problem has at")
    print("  most one solution, and the iteration merely finds it. Equivalently,")
    print("  the only harmonic function that is zero on the boundary is zero")
    print("  everywhere, so the homogeneous problem has no null space and the map")
    print("  from boundary data to solution is invertible. That is what makes")
    print("  upward and downward continuation well posed.")
    print("\n  Change the boundary data, however, and the interior changes: the")
    print("  boundary is the only freedom in an elliptic problem. This is the")
    print("  structural difference from the parabolic and hyperbolic classes,")
    print("  where the solution also depends on an initial state.")


# ----------------------------------------------------------------------
# 4. Non-uniqueness of potential-field inversion
# ----------------------------------------------------------------------

def axisymmetric_potential(density, radius: float, z0: float, n_r: int = 300,
                           n_th: int = 300) -> float:
    """V on the axis at height z0 from an axisymmetric body.

    density(r, theta) is the density in spherical coordinates about the centre.

    V = 2 pi G integral rho r'^2 sin(theta') / D dr' dtheta',
    D = sqrt(z0^2 + r'^2 - 2 z0 r' cos(theta')).
    Valid for z0 outside the body, where the integrand is smooth.
    """
    dr = radius / n_r
    dth = math.pi / n_th
    total = 0.0
    for i in range(n_r):
        r = (i + 0.5) * dr
        r2 = r * r
        for j in range(n_th):
            th = (j + 0.5) * dth
            rho = density(r, th)
            if rho == 0.0:
                continue
            d = math.sqrt(z0 * z0 + r2 - 2.0 * z0 * r * math.cos(th))
            total += rho * r2 * math.sin(th) / d
    return 2.0 * math.pi * G * total * dr * dth


def total_mass(density, radius: float, n: int = 200_000) -> float:
    """M = 4 pi integral rho(r) r^2 dr by the midpoint rule."""
    dr = radius / n
    return 4.0 * math.pi * sum(density((i + 0.5) * dr) * ((i + 0.5) * dr) ** 2
                               for i in range(n)) * dr


def report_non_uniqueness() -> None:
    section("4a. A uniform ball and a point mass give the same exterior potential")
    radius = 3.0e4                     # 30 km
    rho0 = 2800.0                      # kg/m^3
    mass = total_mass(lambda r: rho0, radius)
    ball_density = lambda r, th: rho0
    print(f"  ball radius R = {radius:.3e} m, density = {rho0} kg/m^3")
    print(f"  total mass (volume integral) = {mass:.6e} kg")
    print(f"\n  {'z0 / R':>10}{'V(ball), quadrature':>24}{'G M / z0':>17}"
          f"{'relative difference':>22}")
    for ratio in (1.5, 2.0, 4.0):
        z0 = ratio * radius
        v_ball = axisymmetric_potential(ball_density, radius, z0)
        v_point = G * mass / z0
        print(f"  {ratio:>10.1f}{v_ball:>24.12e}{v_point:>17.10e}"
              f"{abs(v_ball - v_point)/v_point:>22.2e}")
    print("\n  The exterior potential of any spherically symmetric body is G M / r,")
    print("  independent of how the mass is distributed inside (Newton's theorem;")
    print("  the shell theorem). The residual above is the quadrature error of the")
    print("  numerical integration, not a physical difference: the identity is exact.")
    print("  Outside the body the different densities are indistinguishable: a point")
    print("  mass, a ball, and a set of concentric shells of the same total mass are")
    print("  one equivalence class. This is the first and simplest reason")
    print("  potential-field inversion is non-unique.")

    section("4b. A concrete null space: zero-total-mass spherical perturbation")
    r1, r2, r3 = 0.4 * radius, 0.7 * radius, 1.0 * radius
    delta = 500.0                      # kg/m^3

    def ball(r, th):
        return rho0

    shell_a = 4.0 * math.pi / 3.0 * (r2 ** 3 - r1 ** 3)
    shell_b = 4.0 * math.pi / 3.0 * (r3 ** 3 - r2 ** 3)
    delta_b = -delta * shell_a / shell_b

    def perturbed(r, th):
        if r1 <= r < r2:
            return rho0 + delta
        if r2 <= r < r3:
            return rho0 + delta_b
        return rho0

    def perturbation(r):
        return perturbed(r, 0.0) - ball(r, 0.0)

    mass_delta = total_mass(perturbation, radius, n=400_000)
    m_a = delta * shell_a
    m_b = delta_b * shell_b
    print(f"  add  {delta:+.1f} kg/m^3 on  {r1:.3e} <= r < {r2:.3e}")
    print(f"  add  {delta_b:+.4f} kg/m^3 on  {r2:.3e} <= r < {r3:.3e}")
    print(f"  analytic mass of the positive shell  = {m_a:+.6e} kg")
    print(f"  analytic mass of the negative shell  = {m_b:+.6e} kg")
    print(f"  analytic net mass of the perturbation = {m_a + m_b:+.3e} kg (exactly zero)")
    print(f"  numerical volume integral of the perturbation = {mass_delta:+.3e} kg")
    print(f"  (relative to the shell mass: {abs(mass_delta)/abs(m_a):.1e}, i.e. quadrature noise)")

    def plus_only(r, th):
        return rho0 + delta if r1 <= r < r2 else rho0

    print(f"\n  Comparing at z0 = 2R = {2*radius:.3e} m:")
    z0 = 2.0 * radius
    v_ball = axisymmetric_potential(ball, radius, z0)
    v_plus = axisymmetric_potential(plus_only, radius, z0)
    v_null = axisymmetric_potential(perturbed, radius, z0)
    print(f"    V(ball)                        = {v_ball:.10e}")
    print(f"    V(ball + positive shell)       = {v_plus:.10e}"
          f"   relative change {(v_plus - v_ball)/v_ball:+.3e}")
    print(f"    V(ball + compensated pair)     = {v_null:.10e}"
          f"   relative change {(v_null - v_ball)/v_ball:+.3e}")
    print(f"    cancellation factor            = "
          f"{abs((v_plus - v_ball)/(v_null - v_ball)):.3e}")
    print("\n  The positive shell alone would change the exterior potential by about")
    print("  5 per cent. Adding the compensating negative shell removes that change")
    print("  to the level of the quadrature error: the pair is a null-space vector,")
    print("  a density model that leaves the exterior field untouched.")
    print("\n  The change is exactly zero analytically; the residual -1.2e-07 is the")
    print("  quadrature noise of the two numerical integrations. A survey that could")
    print("  measure V to 1 part in 10^6 would therefore be completely blind to this")
    print("  500 kg/m^3 density change, and no least-squares fit to real data could")
    print("  rule it out. Uniqueness of the PDE solution from boundary data does NOT")
    print("  imply uniqueness of the inverse problem for the source. Lesson 08 of the")
    print("  multivariable-calculus module and the inverse-problems folder develop")
    print("  this into the theory of ill-posedness.")



def report_dipole_perturbation() -> None:
    section("4c. A non-spherical zero-mass perturbation is NOT a null vector")
    print("Repeat 4b, but put the + and - density in the upper and lower")
    print("hemispheres of the same shell, so the total mass still vanishes while")
    print("the distribution is no longer spherically symmetric.")
    radius = 3.0e4
    rho0 = 2800.0
    r1, r2 = 0.4 * radius, 0.7 * radius
    delta = 500.0

    def ball(r, th):
        return rho0

    def dipole(r, th):
        if r1 <= r < r2:
            return rho0 + delta if th < math.pi / 2.0 else rho0 - delta
        return rho0

    print(f"\n  {'z0 / R':>10}{'V(ball)':>20}{'V(dipole)':>20}"
          f"{'relative change':>18}")
    for ratio in (1.2, 2.0, 4.0):
        z0 = ratio * radius
        v_ball = axisymmetric_potential(ball, radius, z0)
        v_dip = axisymmetric_potential(dipole, radius, z0)
        print(f"  {ratio:>10.1f}{v_ball:>20.10e}{v_dip:>20.10e}"
              f"{(v_dip - v_ball)/v_ball:>18.4e}")
    print("\n  The response is now non-zero: about 1 per cent at 1.2 R, falling")
    print("  roughly as 1/z0 (the difference 1.13e-2 -> 7.03e-3 -> 3.57e-3 is close")
    print("  to halving when the distance doubles). That is the signature of a")
    print("  dipole: its potential falls as 1/z0^2 while the monopole's falls as")
    print("  1/z0, so the RELATIVE difference falls as 1/z0.")
    print("  The lesson: the exact null space of the exterior-potential map is not")
    print("  'any zero-mass perturbation' but the SPHERICALLY SYMMETRIC zero-mass")
    print("  ones. A non-spherical perturbation with the same total mass is")
    print("  detectable in principle, though 1 per cent may still be below the noise")
    print("  of a real survey.")


def main() -> None:
    report_laplace()
    report_poisson()
    report_uniqueness()
    report_non_uniqueness()
    report_dipole_perturbation()


if __name__ == "__main__":
    main()
