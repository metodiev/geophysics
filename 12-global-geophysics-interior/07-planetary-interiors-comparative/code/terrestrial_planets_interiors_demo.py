#!/usr/bin/env python3
"""Comparative interior scaling of solid planets: what mass, radius and moment
of inertia do and do not determine.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python terrestrial_planets_interiors_demo.py

Everything is SYNTHETIC.  The "planets" are dimensionless teaching bodies built
by scaling a single interior structure; they are not Mars, Venus, Mercury or the
Moon, and no number here is a measurement of one.  The only externally quoted
quantity is the exact standard constant G.

The point of the exercise is scaling, not planetary numbers: the same interior
structure scaled to different masses and radii gives the SAME dimensionless
central pressure, and the observables that are available for a real body
(mass, radius, static moment of inertia) leave a family of structures.

Sections
--------
1  the hydrostatic interior of a two-layer body: central pressure exact for a
   uniform sphere and by integration for layered bodies
2  dimensionless central pressure: invariance under scaling, and the exponents
   in M and R measured
3  the inverse problem: (mass, radius, C/MR^2) leaves a curve of core models
4  adding a second observable: the fluid Love number k_f = 3 J2/q, computed from
   the figure response, narrows the curve to a point within the family
5  thermal and compression scalings: surface-to-volume, and the compression
   parameter that decides whether a body is self-compressed
"""

import numpy as np

RNG = np.random.default_rng(20261014)

G = 6.67430e-11  # m^3 kg^-1 s^-2 (CODATA)


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


# --------------------------------------------------------------------------
# interior structure
# --------------------------------------------------------------------------

def two_layer_structure(x_core, alpha):
    """Densities (core, mantle) for a body of unit mean density.

    x_core = r_core/R, alpha = rho_core/rho_mantle.
    """
    rho_m = 1.0 / ((1.0 - x_core ** 3) + alpha * x_core ** 3)
    return alpha * rho_m, rho_m


def mass_inside(r, R, x_core, rho_c, rho_m):
    r_c = x_core * R
    if r <= r_c:
        return (4.0 / 3.0) * np.pi * rho_c * r ** 3
    return (4.0 / 3.0) * np.pi * (rho_c * r_c ** 3 + rho_m * (r ** 3 - r_c ** 3))


def central_pressure(M, R, x_core, alpha, n_steps=200000):
    """Central pressure from dP/dr = -rho g(r), by quadrature (SI: Pa)."""
    rho_c, rho_m = two_layer_structure(x_core, alpha)
    rho_c *= M / ((4.0 / 3.0) * np.pi * R ** 3)
    rho_m *= M / ((4.0 / 3.0) * np.pi * R ** 3)
    r = (np.arange(n_steps) + 0.5) * R / n_steps
    m_in = np.array([mass_inside(ri, R, x_core, rho_c, rho_m) for ri in r[::1000]])
    m_full = np.interp(r, r[::1000], m_in)
    g = G * m_full / r ** 2
    rho = np.where(r <= x_core * R, rho_c, rho_m)
    return np.sum(rho * g) * (R / n_steps)


def cmr2_two_layer(x_core, alpha):
    """C/(M R^2) for two uniform layers (exact)."""
    m_core = x_core ** 3 * alpha
    m_mantle = 1.0 - x_core ** 3
    M = m_core + m_mantle
    I_core = 0.4 * m_core * x_core ** 2
    I_shell = 0.4 * m_mantle * (1.0 - x_core ** 5) / (1.0 - x_core ** 3)
    return (I_core + I_shell) / M


# --------------------------------------------------------------------------
# figure response of a layered fluid body (first-order, jump based)
# --------------------------------------------------------------------------

def shell_p2_closed(r_obs, R, sigma2):
    """Degree-2 potential coefficient of a P2 shell of radius R."""
    if r_obs >= R:
        return -(4.0 * np.pi * G * sigma2 / 5.0) * R ** 4 / r_obs ** 3
    return -(4.0 * np.pi * G * sigma2 / 5.0) * r_obs ** 2 / R


def solve_figure(radii, rho_core, drops, q, M_total):
    """P2 interface displacements, then C, A and the deformed mass."""
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
            if r_hi > r_lo:
                m += (4.0 / 3.0) * np.pi * rho_layers[i] * (r_hi ** 3 - r_lo ** 3)
        return m

    A = np.zeros((n, n))
    b = np.zeros(n)
    for i in range(n):
        r_i = radii[i]
        A[i, i] += G * mass_inside(r_i) / r_i ** 2 * r_i
        for k in range(n):
            A[i, k] += shell_p2_closed(r_i, radii[k], 1.0) * drops[k] * radii[k]
        b[i] = -(1.0 / 3.0) * omega2 * r_i ** 2
    eps = np.linalg.solve(A, b)
    a_i = radii * (1.0 - eps / 2.0)
    c_i = radii * (1.0 + eps)

    def layer_integral(pa, pc):
        tot = 0.0
        for i in range(n):
            outer = rho_layers[i] * a_i[i] ** pa * c_i[i] ** pc
            inner = (rho_layers[i] * a_i[i - 1] ** pa * c_i[i - 1] ** pc
                     if i > 0 else 0.0)
            tot += outer - inner
        return tot

    C = (8.0 / 15.0) * np.pi * layer_integral(4, 1)
    A_mom = (4.0 / 15.0) * np.pi * (layer_integral(4, 1) + layer_integral(2, 3))
    M_shape = (4.0 / 3.0) * np.pi * layer_integral(2, 1)
    return eps, C, A_mom, M_shape


def figure_observables(M, R, x_core, alpha, q=4.0e-3, n_shells=8):
    """Return (C/MR^2, J2/q, k_f = 3 J2/q) for a two-layer hydrostatic body."""
    rho_c0, rho_m0 = two_layer_structure(x_core, alpha)
    scale = M / ((4.0 / 3.0) * np.pi * R ** 3)
    rho_c, rho_m = rho_c0 * scale, rho_m0 * scale
    if x_core > 0.001:
        radii = np.array([x_core * R, R])
        drops = np.array([rho_c - rho_m, rho_m])
    else:
        radii = np.array([R])
        drops = np.array([rho_m])
    eps, C, A_mom, M_shape = solve_figure(radii, rho_c, drops, q, M)
    a_eq = radii[-1] * (1.0 - eps[-1] / 2.0)
    cmr = C / (M_shape * a_eq ** 2)
    J2 = (C - A_mom) / (M_shape * a_eq ** 2)
    return cmr, J2 / q, 3.0 * J2 / q


def row_is(x, row):
    """True when the ridge row starts with the x value of the best row."""
    return abs(x - row[0]) < 1e-9


def main():
    section("1. Hydrostatic interior: central pressure of a two-layer body")
    rho, R = 4000.0, 3.0e6
    M_uniform = (4.0 / 3.0) * np.pi * rho * R ** 3
    P_analytic = (2.0 / 3.0) * np.pi * G * rho ** 2 * R ** 2
    P_numeric = central_pressure(M_uniform, R, 0.0, 1.0)
    print(f"  SYNTHETIC uniform body: rho = {rho:.0f} kg/m^3, R = {R:.1e} m,"
          f" M = {M_uniform:.3e} kg")
    print("  Exact for a uniform sphere: P_c = (2/3) pi G rho^2 R^2")
    print(f"     closed form {P_analytic:.4e} Pa")
    print(f"     integration {P_numeric:.4e} Pa"
          f"   (difference {100 * abs(P_numeric - P_analytic) / P_analytic:.3f} %)")
    print(f"     in GPa: {P_analytic / 1e9:.2f} GPa")
    print("  The uniform case is the only exactly integrable one; layered bodies need")
    print("  the quadrature.  Everything below uses the quadrature.")

    section("2. Dimensionless central pressure: invariance and exponents")
    print("  For a body with a fixed internal structure, define")
    print("        Pi = P_c R^4 / (G M^2).")
    print("  For a uniform body Pi is an exact constant, 3/(8 pi):")
    print(f"     3/(8 pi) = {3.0 / (8.0 * np.pi):.6f}"
          f"   quadrature gives {central_pressure(1.0, 1.0, 0.0, 1.0) / G:.6f}")
    print("  Two-layer bodies, same structure numbers, different masses and radii:")
    print("   M (kg)      R (m)     P_c (Pa)      Pi = P_c R^4/(G M^2)")
    for M, Rr in ((3.0e23, 2.4e6), (6.0e23, 3.0e6), (6.0e24, 6.0e6), (6.0e25, 9.5e6)):
        Pc = central_pressure(M, Rr, 0.5, 2.0)
        print(f"   {M:.2e}   {Rr:.2e}   {Pc:12.4e}   {Pc * Rr ** 4 / (G * M ** 2):14.6f}")
    print("  Pi is the same to better than a percent: the interior STATE of a body")
    print("  with a given structure is a pure number, and only the combination")
    print("  GM^2/R^4 sets how large the pressures are.")
    print("  Measured exponents from a family with R fixed at 3.0e6 m:")
    Ms = np.array([1.0e23, 3.0e23, 1.0e24, 3.0e24])
    Ps = np.array([central_pressure(M, 3.0e6, 0.4, 1.8) for M in Ms])
    exp_M = np.polyfit(np.log(Ms), np.log(Ps), 1)[0]
    Rs = np.array([2.0e6, 3.0e6, 4.0e6, 5.0e6])
    Ps2 = np.array([central_pressure(6.0e23, Rr, 0.4, 1.8) for Rr in Rs])
    exp_R = np.polyfit(np.log(Rs), np.log(Ps2), 1)[0]
    print(f"     d ln P_c / d ln M = {exp_M:6.3f}   (two)")
    print(f"     d ln P_c / d ln R = {exp_R:6.3f}   (minus four)")
    print("  This is why comparisons between bodies must be made in the dimensionless")
    print("  numbers: a body twice as massive and twice as large has the same Pi but")
    print("  a central pressure smaller by a factor 2^2/2^4 = 1/4.")

    section("3. The inverse problem: (M, R, C/MR^2) leaves a curve")
    target = 0.3350                    # SYNTHETIC adopted moment-of-inertia factor
    M_p, R_p = 4.0e23, 3.0e6
    print(f"  SYNTHETIC body: M = {M_p:.2e} kg, R = {R_p:.2e} m,"
          f" C/MR^2 = {target:.4f} (adopted, not measured)")
    print("   x_core    alpha required   core rho (kg/m^3)   mean rho (kg/m^3)")
    for x in (0.10, 0.20, 0.30, 0.40, 0.50, 0.60):
        lo, hi = 1.0, 20000.0
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            if cmr2_two_layer(x, mid) > target:
                lo = mid
            else:
                hi = mid
        alpha = 0.5 * (lo + hi)
        rho_c0, rho_m0 = two_layer_structure(x, alpha)
        scale = M_p / ((4.0 / 3.0) * np.pi * R_p ** 3)
        print(f"   {x:5.2f}   {alpha:14.4f}   {alpha * rho_m0 * scale:15.1f}"
              f"   {scale:16.1f}")
    print("  Radius-to-the-mantle and density contrast trade off exactly: the moment")
    print("  of inertia sees a weighted radial average, not a boundary.")
    print("  A real study has a measured C/MR^2 with an error bar, so the answer is")
    print("  the band of rows inside that band, not a row.")

    section("4. A second observable narrows the curve")
    print("  The static figure of a hydrostatic body gives one more number: the fluid")
    print("  Love number k_f = 3 J2/q, where q = omega^2 R^3/(GM) is the rotation")
    print("  parameter.  Both numbers come from the same first-order figure solver.")
    print("  First, the ridge of section 3 again, now with k_f attached:")
    print("   x_core    alpha required    C/MR^2     J2/q      k_f")
    ridge = []
    for x in (0.20, 0.30, 0.40, 0.50, 0.60):
        lo, hi = 1.0, 20000.0
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            if cmr2_two_layer(x, mid) > target:
                lo = mid
            else:
                hi = mid
        alpha = 0.5 * (lo + hi)
        cmr, j2q, kf = figure_observables(M_p, R_p, x, alpha)
        ridge.append((x, alpha, cmr, j2q, kf))
        print(f"   {x:5.2f}   {alpha:15.4f}   {cmr:7.4f}   {j2q:7.4f}   {kf:8.4f}")
    print("  Along the ridge C/MR^2 is nearly constant by construction, while k_f falls")
    print("  monotonically: a measurement of k_f to a few percent selects one row.")
    kf_true = ridge[2][4] * 1.02       # SYNTHETIC measured value, 2% above row 0.40
    print(f"  SYNTHETIC measured k_f = {kf_true:.4f}.  Closest models on the ridge:")
    best = min(ridge, key=lambda row: abs(row[4] - kf_true))
    for x, alpha, cmr, j2q, kf in ridge:
        tag = "   <-- closest" if row_is(x, best) else ""
        print(f"     x_core = {x:4.2f}  k_f = {kf:.4f}   |k_f - measured| ="
              f" {abs(kf - kf_true):.4f}{tag}")
    print(f"  The pair (C/MR^2, k_f) thus determines (core size, density contrast)")
    print(f"  WITHIN this two-parameter family, to the point x_core = {best[0]:.2f},")
    print(f"  alpha = {best[1]:.2f}.  The residual ambiguity is no longer in the data:")
    print("  it is in the assumption that the interior is two uniform layers.")
    cmr_u, j2q_u, kf_u = figure_observables(M_p, R_p, 0.0, 1.0)
    print("  Sanity check on the solver: a homogeneous body gives k_f = 1.5, J2/q = 0.5")
    print(f"  in the small-rotation limit; at the finite q used here it gives")
    print(f"     C/MR^2 = {cmr_u:.4f}, J2/q = {j2q_u:.4f}, k_f = {kf_u:.4f}")
    print("  Two cautions, both testable and both neglected at cost: k_f is only")
    print("  meaningful if the body is hydrostatic, and a non-hydrostatic part of J2")
    print("  (a fossil or dynamically supported figure) contaminates it.")

    section("5. Thermal and compression scalings")
    print("  Surface-to-volume ratio sets how fast a body cools for a given heat")
    print("  production per unit mass: S/V = 3/R.")
    print("   R (m)        S/V (1/m)     ratio to R = 6.4e6 m")
    for Rr in (6.4e6, 3.0e6, 1.7e6, 1.0e6):
        print(f"   {Rr:.2e}   {3.0 / Rr:12.4e}   {(3.0 / Rr) / (3.0 / 6.4e6):14.2f}")
    print("  A body half the size has twice the surface-to-volume ratio: it loses its")
    print("  heat twice as fast per unit mass, all else equal.")
    print("  The compression parameter is the central pressure divided by a relevant")
    print("  elastic modulus.  With a SYNTHETIC bulk modulus K = 1.3e11 Pa:")
    K = 1.3e11
    print("   R (m)      M (kg)      P_c (Pa)     P_c/K")
    for M, Rr in ((4.0e23, 3.0e6), (4.0e24, 6.0e6)):
        Pc = central_pressure(M, Rr, 0.4, 2.0)
        print(f"   {Rr:.2e}   {M:.2e}   {Pc:12.4e}   {Pc / K:8.4f}")
    print("  P_c/K below about 0.1 means self-compression is a modest correction and a")
    print("  constant-density scaling is respectable; above it, the equation of state")
    print("  sets the structure and the dimensionless numbers drift with the interior.")
    print("  That crossover is the honest boundary of the scaling arguments in this")
    print("  module: they are exact for structure, and progressively weaker as bodies")
    print("  become large enough to compress themselves.")


if __name__ == "__main__":
    main()
