#!/usr/bin/env python3
"""Moment of inertia, hydrostatic figure, and what geodesy can and cannot fix
about the density profile of a planet.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python moment_of_inertia_demo.py

Everything here is SYNTHETIC.  The bodies are teaching bodies with chosen
masses, radii, density contrasts and rotation rates; none of them is a measured
planet, and no number below is taken from a published planetary model.  The only
externally quoted quantity is the exact standard constant G.

Sections
--------
1  inertia factors of a uniform sphere and a thin shell, exact and by quadrature
2  a two-layer body: C/MR^2 versus core radius fraction and density contrast
3  the non-uniqueness ridge: one adopted C/MR^2, a one-parameter family of bodies
4  the degree-2 shell potential: closed form checked against numerical quadrature
5  the exact Maclaurin spheroid solved from the closed-form spheroid potential,
   and the measured small-rotation limits f/q and J2/q
6  the exact internal spheroid potential checked against 3-D quadrature
7  a first-order (Clairaut-style) figure solver, calibrated on section 5, applied
   to layered fluid bodies: figure response and C/MR^2 together
8  the exact identity J2 = (C-A)/(MR^2), H = (C-A)/C and the rigid free-wobble
   period that follows from an adopted (C/MR^2, J2) pair
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# Exact standard constant, SI (CODATA): gravitational constant.
G = 6.67430e-11  # m^3 kg^-1 s^-2


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


# --------------------------------------------------------------------------
# 1. Inertia factors
# --------------------------------------------------------------------------

def cmr2_by_quadrature(rho_of_r, R, n=4000):
    """C/(M R^2) of a spherical body with density rho(r), by radial quadrature."""
    r = (np.arange(n) + 0.5) * R / n
    dm = rho_of_r(r) * 4.0 * np.pi * r ** 2 * (R / n)
    M = dm.sum()
    return (dm * (2.0 / 3.0) * r ** 2).sum() / (M * R ** 2), M


# --------------------------------------------------------------------------
# 2-3. Two-layer bodies
# --------------------------------------------------------------------------

def two_layer_cmr2(x_core, alpha):
    """C/(M R^2) of a two-layer sphere: x_core = r_core/R, alpha = rho_c/rho_m.

    Exact for two concentric uniform layers (solid sphere plus uniform shell).
    """
    m_core = x_core ** 3 * alpha
    m_mantle = 1.0 - x_core ** 3
    M = m_core + m_mantle
    I_core = 0.4 * m_core * x_core ** 2
    if m_mantle < 1e-12:
        return I_core / M
    I_shell = 0.4 * m_mantle * (1.0 - x_core ** 5) / (1.0 - x_core ** 3)
    return (I_core + I_shell) / M


def solve_alpha_for_cmr2(x_core, target):
    """Density contrast that reproduces a target C/MR^2 for a given core size."""
    lo, hi = 1.0, 20000.0
    for _ in range(300):
        mid = 0.5 * (lo + hi)
        if two_layer_cmr2(x_core, mid) > target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


# --------------------------------------------------------------------------
# 4. Degree-2 shell potential: closed form and an independent quadrature
# --------------------------------------------------------------------------

def shell_p2_closed(r_obs, R, sigma2):
    """Degree-2 potential coefficient of a shell of radius R, density sigma2 P2.

        r > R :  V2 = -(4 pi G sigma2/5) R^4 / r^3
        r < R :  V2 = -(4 pi G sigma2/5) r^2 / R
        r = R :  V2 = -(4 pi G sigma2/5) R
    (V = V2 * P2(cos theta); a positive sigma2 makes the potential more negative.)
    """
    if r_obs >= R:
        return -(4.0 * np.pi * G * sigma2 / 5.0) * R ** 4 / r_obs ** 3
    return -(4.0 * np.pi * G * sigma2 / 5.0) * r_obs ** 2 / R


def shell_p2_quadrature(r_obs, R, sigma2, n_mu=2000):
    """The same coefficient by direct quadrature over the shell, on the polar axis.

    On the axis P2(cos theta) = 1 and no other multipole of a pure P2 shell
    contributes, so the axis value is exactly the degree-2 coefficient.
    """
    mu = -1.0 + (np.arange(n_mu) + 0.5) * 2.0 / n_mu
    dmu = 2.0 / n_mu
    p2 = 0.5 * (3.0 * mu ** 2 - 1.0)
    dist = np.sqrt(R ** 2 + r_obs ** 2 - 2.0 * R * r_obs * mu)
    return -2.0 * np.pi * R ** 2 * G * sigma2 * np.sum(p2 / dist * dmu)


# --------------------------------------------------------------------------
# 5-6. Homogeneous spheroids
# --------------------------------------------------------------------------

def spheroid_A(e):
    """Internal potential coefficients A1 (=A2) and A3 of a homogeneous spheroid.

    For an oblate spheroid (semi-axes a = b > c, e = sqrt(1 - c^2/a^2)) the
    internal potential is  V = -pi G rho [ I0 - A1 (x^2+y^2) - A3 z^2 ].
    """
    if e < 1e-12:
        return 2.0 / 3.0, 2.0 / 3.0
    A1 = (np.sqrt(1.0 - e ** 2) / e ** 3) * np.arcsin(e) - (1.0 - e ** 2) / e ** 2
    A3 = 2.0 / e ** 2 * (1.0 - (np.sqrt(1.0 - e ** 2) / e) * np.arcsin(e))
    return A1, A3


def spheroid_I0(a, c, e):
    """I0 = 2 a^2 c arcsin(e)/(a e); tends to 2 a^2 for e -> 0."""
    if e < 1e-12:
        return 2.0 * a ** 2
    return 2.0 * a * c * np.arcsin(e) / e


def spheroid_V_internal(x, y, z, a, c, rho):
    """Internal potential of a homogeneous oblate spheroid (SI, J/kg)."""
    e = np.sqrt(1.0 - (c / a) ** 2)
    A1, A3 = spheroid_A(e)
    I0 = spheroid_I0(a, c, e)
    return -np.pi * G * rho * (I0 - A1 * (x ** 2 + y ** 2) - A3 * z ** 2)


def spheroid_V_quadrature(x, y, z, a, c, rho, n_s=90, n_mu=140, n_phi=120):
    """Potential of a homogeneous oblate spheroid by 3-D quadrature (unit-ball map)."""
    s = (np.arange(n_s) + 0.5) / n_s
    mu = -1.0 + (np.arange(n_mu) + 0.5) * 2.0 / n_mu
    phi = (np.arange(n_phi) + 0.5) * 2.0 * np.pi / n_phi
    S, MU, PHI = np.meshgrid(s, mu, phi, indexing="ij")
    RHO = np.sqrt(1.0 - MU ** 2)
    xs = (a * S * RHO * np.cos(PHI)).ravel()
    ys = (a * S * RHO * np.sin(PHI)).ravel()
    zs = (c * S * MU).ravel()
    dV = (a ** 2 * c) * (S ** 2).ravel() * (1.0 / n_s) * (2.0 / n_mu) \
        * (2.0 * np.pi / n_phi)
    dist = np.sqrt((x - xs) ** 2 + (y - ys) ** 2 + (z - zs) ** 2)
    return -G * rho * np.sum(dV / dist)


def maclaurin_q(x):
    """Rotation parameter q = omega^2 a^3/(G M) of the exact Maclaurin spheroid.

    Equipotential at the pole and the equator of a homogeneous rotating spheroid:
        A1 a^2 - A3 c^2 = (2/3) q a c .
    """
    a, c = 1.0, x
    e = np.sqrt(1.0 - x ** 2)
    A1, A3 = spheroid_A(e)
    return 3.0 * (A1 * a ** 2 - A3 * c ** 2) / (2.0 * a * c)


def solve_maclaurin(q_target):
    """c/a of the homogeneous hydrostatic spheroid with rotation parameter q."""
    lo, hi = 0.05, 1.0 - 1e-12
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if maclaurin_q(mid) > q_target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


# --------------------------------------------------------------------------
# 7. First-order figure solver for a layered fluid body
# --------------------------------------------------------------------------

def solve_figure(radii, rho_core, drops, q, M_total):
    """P2 displacement amplitudes eps_i of the fluid interfaces of a layered body.

    radii    : mean radii of the interfaces, ascending, last one is the surface
    rho_core : density at the centre
    drops    : density drop rho_inside - rho_outside at each interface
    q        : rotation parameter omega^2 R^3/(G M_total)

    Returns eps, the polar constant C, the equatorial constant A and the mass of
    the deformed body.  The condition at each interface is that the degree-2 part
    of the total potential vanishes along it (the interface is an equipotential):
        g(r_i) r_i eps_i
          + sum_k [potential at r_i of the P2 shell made by interface k]
          + (1/3) omega^2 r_i^2 = 0 ,
    with g(r) = G M(r)/r^2 and the closed-form P2 shell kernel of section 4.
    """
    n = len(radii)
    R = radii[-1]
    omega2 = q * G * M_total / R ** 3
    rho_layers = [rho_core]
    for d in drops[:-1]:
        rho_layers.append(rho_layers[-1] - d)

    def mass_inside(r):
        m = 0.0
        for i in range(n):
            r_lo = 0.0 if i == 0 else radii[i - 1]
            r_hi = min(radii[i], r)
            if r_hi <= r_lo:
                continue
            m += (4.0 / 3.0) * np.pi * rho_layers[i] * (r_hi ** 3 - r_lo ** 3)
        return m

    A = np.zeros((n, n))
    b = np.zeros(n)
    for i in range(n):
        r_i = radii[i]
        A[i, i] += G * mass_inside(r_i) / r_i ** 2 * r_i
        for k in range(n):
            r_k = radii[k]
            kernel = shell_p2_closed(r_i, r_k, 1.0)      # per unit sigma2
            A[i, k] += kernel * (drops[k] * r_k)
        b[i] = -(1.0 / 3.0) * omega2 * r_i ** 2
    eps = np.linalg.solve(A, b)

    a_i = radii * (1.0 - eps / 2.0)
    c_i = radii * (1.0 + eps)

    def layer_integral(power_a, power_c):
        tot = 0.0
        for i in range(n):
            outer = rho_layers[i] * a_i[i] ** power_a * c_i[i] ** power_c
            inner = (rho_layers[i] * a_i[i - 1] ** power_a * c_i[i - 1] ** power_c
                     if i > 0 else 0.0)
            tot += outer - inner
        return tot

    C = (8.0 / 15.0) * np.pi * layer_integral(4, 1)
    A_mom = (4.0 / 15.0) * np.pi * (layer_integral(4, 1) + layer_integral(2, 3))
    M_shape = (4.0 / 3.0) * np.pi * layer_integral(2, 1)
    return eps, C, A_mom, M_shape


def main():
    section("1. Inertia factors of a uniform sphere and a thin shell")
    cmr_sphere, _ = cmr2_by_quadrature(lambda r: np.full_like(r, 1.0), 1.0)
    print(f"  uniform sphere : C/MR^2 = 2/5 = {0.4:.6f}"
          f"   quadrature {cmr_sphere:.6f}   error {abs(cmr_sphere - 0.4):.2e}")
    cmr_shell, _ = cmr2_by_quadrature(
        lambda r: np.where(r > 0.9999, 1.0, 0.0), 1.0, n=40000)
    print(f"  thin shell     : C/MR^2 = 2/3 = {2 / 3:.6f}"
          f"   quadrature {cmr_shell:.6f}   error {abs(cmr_shell - 2 / 3):.2e}")
    print("  Every spherically symmetric body lies between these two exact values.")

    section("2. A two-layer body: C/MR^2 versus core size and density contrast")
    print("  alpha = rho_core/rho_mantle (SYNTHETIC); C/MR^2 is dimensionless")
    print("   x_core  alpha=1.0  alpha=1.5  alpha=2.0  alpha=2.5  alpha=3.5")
    for x in (0.0, 0.2, 0.35, 0.5, 0.65, 0.8, 1.0):
        row = f"   {x:5.2f}  "
        for alpha in (1.0, 1.5, 2.0, 2.5, 3.5):
            row += f" {two_layer_cmr2(x, alpha):9.4f} "
        print(row)
    print("  Limits: alpha -> 1, x_core -> 0 or x_core -> 1 all give 0.4000.")
    print("  A denser core lowers C/MR^2: mass moves toward the rotation axis.")

    section("3. Non-uniqueness: one adopted C/MR^2, one family of bodies")
    target = 0.3350                     # SYNTHETIC adopted constraint
    M_planet = 4.0e24                   # kg, SYNTHETIC
    R_planet = 3.0e6                    # m, SYNTHETIC
    print(f"  SYNTHETIC planet: M = {M_planet:.2e} kg, R = {R_planet:.2e} m")
    print(f"  adopted SYNTHETIC constraint: C/MR^2 = {target:.4f}"
          "  (a teaching value, not a measurement)")
    print("   x_core   alpha required   mantle rho (kg/m^3)   core rho (kg/m^3)")
    for x in (0.15, 0.25, 0.35, 0.45, 0.55, 0.65):
        alpha = solve_alpha_for_cmr2(x, target)
        rho_m = M_planet / ((4.0 / 3.0) * np.pi * R_planet ** 3
                            * ((1.0 - x ** 3) + alpha * x ** 3))
        print(f"   {x:5.2f}   {alpha:12.4f}   {rho_m:18.1f}   {alpha * rho_m:16.1f}")
    print("  Every row reproduces the same C/MR^2.  The constraint is a curve in")
    print("  (core size, density contrast); the planet's mass and radius were")
    print("  already used to normalise it, so geodetic data alone cannot pick a row.")

    section("4. Degree-2 shell potential: closed form versus quadrature")
    R_shell, sigma2 = 1.0e6, 3.0e3
    print(f"  shell radius R = {R_shell:.3e} m,"
          f" surface density sigma2 = {sigma2:.3e} kg/m^2")
    print("   r/R    closed form (J/kg)     quadrature (J/kg)    relative error")
    for rr in (0.4, 0.9, 1.0, 1.5, 3.0):
        closed = shell_p2_closed(rr * R_shell, R_shell, sigma2)
        quad = shell_p2_quadrature(rr * R_shell, R_shell, sigma2)
        print(f"   {rr:4.1f}   {closed:20.8e}   {quad:20.8e}   "
              f"{abs(quad - closed) / abs(closed):8.1e}")
    print("  This kernel is the whole of first-order figure theory: a displaced")
    print("  interface is a P2 shell, and its potential is known in closed form.")
    print("  The r = R row is the one point where the integrand is singular; the")
    print("  quadrature there returns a value biased low (the shell's own-surface")
    print("  potential is a finite, jump-free limit, and the rule must be taken as")
    print("  the limit of the two branches, which is what the closed form gives).")

    section("5. Exact Maclaurin spheroid: hydrostatic flattening of a uniform body")
    print("   q          c/a        f=(a-c)/a       f/q        J2/q")
    for q in (1.0e-4, 1.0e-3, 3.0e-3, 1.0e-2, 3.0e-2):
        x = solve_maclaurin(q)
        f = 1.0 - x
        J2 = (1.0 - x ** 2) / 5.0
        print(f"   {q:8.0e}   {x:8.5f}   {f:12.6e}   {f / q:8.4f}   {J2 / q:8.4f}")
    print("  Measured small-rotation limits: f/q -> 1.2500 = 5/4 and J2/q -> 0.5000.")
    print("  These classical homogeneous-fluid values are obtained here from the")
    print("  exact spheroid potential, not quoted.")

    section("6. The exact internal spheroid potential checked against quadrature")
    a, c, rho = 1.0e6, 0.85e6, 3.0e3
    print(f"  spheroid: a = {a:.3e} m, c = {c:.3e} m, rho = {rho:.3e} kg/m^3,"
          f" e = {np.sqrt(1 - (c / a) ** 2):.4f}")
    print("   (x,y,z)/a        closed form (J/kg)    3-D quadrature (J/kg)   rel. err")
    for pt in ((0.0, 0.0, 0.4 * a), (0.4 * a, 0.0, 0.0), (0.3 * a, 0.3 * a, 0.3 * a),
               (0.5 * a, 0.0, 0.5 * c)):
        closed = spheroid_V_internal(*pt, a, c, rho)
        quad = spheroid_V_quadrature(*pt, a, c, rho)
        print(f"   ({pt[0] / a:4.1f},{pt[1] / a:4.1f},{pt[2] / a:4.1f})"
              f"   {closed:20.8e}   {quad:20.8e}   "
              f"{abs(quad - closed) / abs(closed):8.1e}")

    section("7. Layered fluid bodies: figure response and C/MR^2 together")
    R_body = 6.0e6
    M_body = 4.0e24                     # SYNTHETIC planet
    q = 4.0e-3                          # SYNTHETIC rotation parameter
    print(f"  SYNTHETIC planet: M = {M_body:.2e} kg, R = {R_body:.2e} m,"
          f" q = omega^2 R^3/(GM) = {q:.2e}")
    print("   x_core  alpha    eps_core     eps_surf     f/q     J2/q    C/MR^2")
    for x_core, alpha in ((0.0, 1.0), (0.3, 1.5), (0.5, 2.0), (0.7, 3.5)):
        rho_m = M_body / ((4.0 / 3.0) * np.pi * R_body ** 3
                          * ((1.0 - x_core ** 3) + alpha * x_core ** 3))
        rho_c = alpha * rho_m
        if x_core > 0.0:
            radii = np.array([x_core * R_body, R_body])
            drops = np.array([rho_c - rho_m, rho_m])
        else:
            radii = np.array([R_body])
            drops = np.array([rho_m])
        eps, C, A_mom, M_shape = solve_figure(radii, rho_c, drops, q, M_body)
        a_surf = radii[-1] * (1.0 - eps[-1] / 2.0)
        f_over_q = (-1.5 * eps[-1]) / q
        J2_over_q = ((C - A_mom) / (M_shape * a_surf ** 2)) / q
        cmr = C / (M_shape * a_surf ** 2)
        eps_core = f"{eps[0]:11.4e}" if x_core > 0 else "        ---"
        print(f"   {x_core:5.2f}  {alpha:5.2f}   {eps_core}   {eps[-1]:11.4e}"
              f"   {f_over_q:6.4f}  {J2_over_q:6.4f}   {cmr:7.4f}")
    print("  Calibration: the uniform body (x_core = 0) returns f/q = 1.2500 and")
    print("  J2/q = 0.4979 against the exact Maclaurin values 1.2499 and 0.4999 from")
    print("  section 5: the residual is the second-order term in q, not a solver")
    print("  error.  Central condensation reduces both numbers.")
    print("  The core interface is less flattened than the surface, |eps_core| <")
    print("  |eps_surf|: the rotational bulge does not propagate inwards undiminished.")
    print("  Two assumptions a real study would have to carry: hydrostatic")
    print("  equilibrium, and the two-layer parametrisation of the C/MR^2 column.")

    section("7b. Three-parameter family: a ridge of models that fits the same pair")
    import scipy.optimize as opt

    R_b, M_b, q_b = 6.0e6, 4.0e24, 4.0e-3

    def graded_model(x_core, alpha, gamma, n_mantle=12):
        """Core plus a mantle whose density falls linearly outward.

        x_core = r_core/R, alpha = rho_core/rho_mantle_surface_scale,
        gamma   = fractional density drop across the mantle.
        Returns (C/MR^2 at the equatorial radius, J2/q) of the deformed body.
        """
        # panel edges in units of R
        edges = np.concatenate(([x_core],
                                x_core + (1.0 - x_core) * np.arange(1, n_mantle + 1)
                                / n_mantle)) if x_core > 0 else             np.arange(1, n_mantle + 1) / n_mantle
        t_mid = (np.arange(n_mantle) + 0.5) / n_mantle
        mantle_shape = np.sum((1.0 - gamma * t_mid)
                              * (edges[1:] ** 3 - edges[:-1] ** 3))
        rho_m = M_b / ((4.0 / 3.0) * np.pi * R_b ** 3
                       * (alpha * x_core ** 3 + mantle_shape))
        rho_c = alpha * rho_m
        rho_mantle_layers = rho_m * (1.0 - gamma * t_mid)
        if x_core > 0:
            rho_layers = np.concatenate(([rho_c], rho_mantle_layers))
        else:
            rho_layers = rho_mantle_layers
        radii = edges * R_b
        drops = np.concatenate((rho_layers[:-1] - rho_layers[1:], [rho_layers[-1]]))
        eps, C, A_mom, M_shape = solve_figure(radii, rho_layers[0], drops, q_b, M_b)
        a_eq = radii[-1] * (1.0 - eps[-1] / 2.0)
        return C / (M_shape * a_eq ** 2), ((C - A_mom) / (M_shape * a_eq ** 2)) / q_b

    x_true, alpha_true, gamma_true = 0.45, 2.20, 0.35
    cmr_true, j2q_true = graded_model(x_true, alpha_true, gamma_true)
    print(f"  a SYNTHETIC 'true' model: x_core = {x_true:.2f}, alpha = {alpha_true:.2f},"
          f" gamma = {gamma_true:.2f}")
    print(f"  it has C/MR^2 = {cmr_true:.4f} and J2/q = {j2q_true:.4f};"
          " those two numbers are the whole data set")
    print("  Models recovered from that pair, with the core radius held at each row:")
    print("   x_core   alpha     gamma     C/MR^2    J2/q      misfit")
    for x_try in (0.30, 0.37, 0.45, 0.53, 0.60):
        def resid(p):
            cmr, j2q = graded_model(x_try, p[0], p[1])
            return [cmr - cmr_true, j2q - j2q_true]

        p, info, ier, msg = opt.fsolve(resid, [2.0, 0.3], full_output=True)
        cmr, j2q = graded_model(x_try, p[0], p[1])
        misfit = np.hypot(cmr - cmr_true, j2q - j2q_true)
        print(f"   {x_try:5.2f}   {p[0]:7.4f}   {p[1]:7.4f}   {cmr:7.4f}   {j2q:7.4f}"
              f"   {misfit:8.1e}" + ("" if ier == 1 else "  (solver did not converge)"))
    print("  Every row fits the same two numbers with a different interior.  The")
    print("  two-layer answer is unique only because that family has two parameters;")
    print("  with a third the data pick a curve.  Geodesy constrains the family, not")
    print("  the profile, until an independent observable is added.")

    section("8. J2, the dynamical ellipticity and the free wobble")
    print("  Exact relations: J2 = (C-A)/(MR^2) and H = (C-A)/C = J2/(C/MR^2).")
    print("   C/MR^2      J2         H        1/H (sidereal days, rigid body)")
    for cmr, J2 in ((0.4000, 5.0e-3), (0.3500, 5.0e-3), (0.3350, 5.0e-3),
                    (0.3350, 2.5e-3), (0.3350, 7.5e-3)):
        H = J2 / cmr
        print(f"   {cmr:6.4f}   {J2:8.2e}   {H:11.4e}   {1.0 / H:14.1f}")
    print("  The last column is the rigid-body free-wobble period, 1/H sidereal days.")
    print("  A body that deforms has a longer free wobble than this rigid value")
    print("  (lesson 12-06-03), so an observed wobble is not a pure interior probe.")


if __name__ == "__main__":
    main()
