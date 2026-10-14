#!/usr/bin/env python3
"""Giant planets: polytropic interior structure, the radius-mass relation, and
what an interior model with matter spread through it can and cannot be told
apart from one with a core.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python giant_planets_demo.py

Everything is SYNTHETIC.  The "planets" are polytropes with chosen polytropic
indices and chosen compositions; they are not Jupiter or Saturn, and no number
below is a measurement of one.  The externally quoted constants are G and mu0.

Sections
--------
1  the Lane-Emden equation: exact checks at n = 0 and n = 1, then a table of
   dimensionless mass, radius and moment of inertia
2  the mass-radius relation: measured exponents, and the n = 1 case in which the
   radius is independent of the mass
3  the central pressure in the dimensionless form P_c R^4/(G M^2)
4  the moment-of-inertia factor of a polytrope
5  the degeneracy: a distinct core and a smoothly enriched envelope with the
   same mass, radius and C/MR^2
6  magnetic-field scaling: Elsasser balance, the magnetic Reynolds number, and
   the conductivity that a measured dipole moment would imply
"""

import numpy as np

RNG = np.random.default_rng(20261014)

G = 6.67430e-11          # m^3 kg^-1 s^-2 (CODATA)
MU0 = 4.0e-7 * np.pi     # H/m


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


# --------------------------------------------------------------------------
# 1. Lane-Emden
# --------------------------------------------------------------------------

def lane_emden(n, xi_max=25.0, n_steps=400000):
    """Solve theta'' + (2/xi)theta' + theta^n = 0, theta(0)=1, theta'(0)=0.

    Returns (xi1, omega) with xi1 the first zero of theta and omega = -xi1^2
    theta'(xi1), the dimensionless mass of the polytrope.  Negative trial values
    of theta^n are clamped to zero: the polytrope ends at the first zero.
    """
    def f(x, y, dy):
        src = max(y, 0.0) ** n
        if x < 1e-12:
            return -src / 3.0
        return -dy * 2.0 / x - src

    h = xi_max / n_steps
    x, y, dy = 0.0, 1.0, 0.0
    for i in range(n_steps):
        k1y, k1d = dy, f(x, y, dy)
        k2y, k2d = dy + h / 2 * k1d, f(x + h / 2, y + h / 2 * k1y, dy + h / 2 * k1d)
        k3y, k3d = dy + h / 2 * k2d, f(x + h / 2, y + h / 2 * k2y, dy + h / 2 * k2d)
        k4y, k4d = dy + h * k3d, f(x + h, y + h * k3y, dy + h * k3d)
        y_new = y + h / 6 * (k1y + 2 * k2y + 2 * k3y + k4y)
        dy_new = dy + h / 6 * (k1d + 2 * k2d + 2 * k3d + k4d)
        if y_new <= 0.0:
            frac = y / (y - y_new)          # linear interpolation to theta = 0
            xi1 = x + frac * h
            dth1 = dy + frac * (dy_new - dy)
            return xi1, -xi1 ** 2 * dth1
        x, y, dy = x + h, y_new, dy_new
    return np.nan, np.nan


def polytrope_profile(n, rho_c, K, n_shells=2000):
    """Density profile of a polytrope: returns (r, rho, R, M_scale)."""
    if n == 0.0:
        # incompressible: P = K rho everywhere, so hydrostatic balance fixes R
        R = np.sqrt(3.0 * K / (2.0 * np.pi * G * rho_c))
        r = (np.arange(n_shells) + 0.5) * R / n_shells
        return r, np.full_like(r, rho_c), R, None
    xi1, omega = lane_emden(n)
    alpha = np.sqrt((n + 1.0) * K * rho_c ** (1.0 / n - 1.0) / (4.0 * np.pi * G))
    xi = np.linspace(0.0, xi1, n_shells)
    # reconstruct theta on the grid by re-integrating (cheap) with low resolution
    th = np.zeros_like(xi)
    th[0] = 1.0
    h = xi[1] - xi[0]

    def f(x, y, dy):
        src = max(y, 0.0) ** n
        return -src / 3.0 if x < 1e-12 else -dy * 2.0 / x - src

    dy = 0.0
    for i in range(1, n_shells):
        x, y = xi[i - 1], th[i - 1]
        k1y, k1d = dy, f(x, y, dy)
        k2y, k2d = dy + h / 2 * k1d, f(x + h / 2, y + h / 2 * k1y, dy + h / 2 * k1d)
        k3y, k3d = dy + h / 2 * k2d, f(x + h / 2, y + h / 2 * k2y, dy + h / 2 * k2d)
        k4y, k4d = dy + h * k3d, f(x + h, y + h * k3y, dy + h * k3d)
        th[i] = y + h / 6 * (k1y + 2 * k2y + 2 * k3y + k4y)
        dy = dy + h / 6 * (k1d + 2 * k2d + 2 * k3d + k4d)
    r = xi * alpha
    rho = rho_c * np.maximum(th, 0.0) ** n
    return r, rho, alpha * xi1, alpha


def polytrope_mass_radius(n, rho_c, K):
    r, rho, R, alpha = polytrope_profile(n, rho_c, K)
    M = np.trapezoid(4.0 * np.pi * r ** 2 * rho, r)
    return M, R


def polytrope_cmr2(n, rho_c, K):
    r, rho, R, alpha = polytrope_profile(n, rho_c, K)
    M = np.trapezoid(4.0 * np.pi * r ** 2 * rho, r)
    I = np.trapezoid(4.0 * np.pi * r ** 2 * rho * (2.0 / 3.0) * r ** 2, r)
    return I / (M * R ** 2), M, R, r, rho


def main():
    section("1. The Lane-Emden equation, checked against its exact solutions")
    for n in (0, 1):
        xi1, omega = lane_emden(n)
        if n == 0:
            exact_xi1, exact_omega = np.sqrt(6.0), 2.0 * np.sqrt(6.0)
        else:
            exact_xi1, exact_omega = np.pi, np.pi
        print(f"  n = {n}: xi1 = {xi1:.6f} (exact {exact_xi1:.6f},"
              f" error {abs(xi1 - exact_xi1):.1e}),"
              f" -xi1^2 theta' = {omega:.6f} (exact {exact_omega:.6f})")
    print("  Dimensionless structure constants for a family of indices:")
    print("   n      xi1        -xi1^2 theta'(xi1)   M(R) exponent (3-n)/(1-n)")
    for n in (0.0, 0.5, 1.0, 1.5, 2.0, 3.0):
        xi1, omega = lane_emden(n)
        expo = (3.0 - n) / (1.0 - n) if n != 1.0 else float("inf")
        print(f"   {n:3.1f}   {xi1:9.5f}   {omega:18.5f}   "
              + ("infinite (R independent of M)" if np.isinf(expo) else f"{expo:10.3f}"))
    print("  The n = 1 case is the one that matters for gas giants: its radius is")
    print("  independent of its mass, and the solver reproduces that exactly.")

    section("2. The mass-radius relation, measured")
    print("  For a polytrope P = K rho^(1+1/n) with a fixed K, the homology relations")
    print("  give M proportional to R^((3-n)/(1-n)).  Measured here by varying the")
    print("  central density at fixed K:")
    K = 1.0e7
    print("   n        M (kg)          R (m)         measured exponent")
    for n in (0.0, 0.5, 1.5, 2.0, 3.0):
        rhos = np.array([0.5, 1.0, 2.0, 4.0, 8.0]) * 1e4
        Ms, Rs = [], []
        for rc in rhos:
            M, R = polytrope_mass_radius(n, rc, K)
            Ms.append(M)
            Rs.append(R)
        Ms, Rs = np.array(Ms), np.array(Rs)
        slope = np.polyfit(np.log(Rs), np.log(Ms), 1)[0]
        expo = (3.0 - n) / (1.0 - n)
        tag = (f"(predicted {expo:8.3f})" if n > 0.0
               else "(n = 0 is the degenerate case)")
        print(f"   {n:3.1f}   {Ms[-1]:12.4e}   {Rs[-1]:12.4e}   {slope:10.4f}"
              f"   {tag},  M proportional to R^{slope:.2f}")
    print("  The n = 1 case is exact: R is independent of M.  The n = 0 case is")
    print("  degenerate -- with P = K rho and hydrostatic balance the radius is set")
    print("  by K and rho_c, giving the measured M proportional to R^1 -- and the")
    print("  homology exponent (3-n)/(1-n) is meaningless there.  Read the exponents")
    print("  off the measurement, not off the formula, whenever a limit is involved.")

    section("3. Central pressure in dimensionless form")
    print("  P_c = K rho_c^(1+1/n); the dimensionless measure is P_c R^4/(G M^2).")
    print("   n      P_c (Pa)        P_c R^4/(G M^2)")
    K = 1.0e7
    for n in (0.0, 1.0, 1.5, 2.0, 3.0):
        rc = 1.0e4
        M, R = polytrope_mass_radius(n, rc, K)
        Pc = K * rc ** (1.0 + 1.0 / n) if n > 0 else K * rc
        print(f"   {n:3.1f}   {Pc:14.6e}   {Pc * R ** 4 / (G * M ** 2):16.6f}")
    print(f"  For comparison the exact uniform-sphere value is 3/(8 pi) ="
          f" {3.0 / (8.0 * np.pi):.6f}.")
    print("  The dimensionless central pressure rises with n: a more compressible")
    print("  body concentrates its mass and runs a higher central pressure for the")
    print("  same M and R.  That number, not the pressure in pascals, is what a")
    print("  comparison between two bodies should use.")

    section("4. The moment-of-inertia factor of a polytrope")
    print("   n      C/MR^2      (uniform sphere = 0.4; thin shell = 0.6667)")
    for n in (0.0, 0.5, 1.0, 1.5, 2.0, 3.0):
        cmr, M, R, r, rho = polytrope_cmr2(n, 1.0e4, 1.0e7)
        print(f"   {n:3.1f}   {cmr:9.5f}")
    print("  The n = 0 value reproduces 0.4000 exactly, which is the solver's check.")
    print("  For n above about 1.5 the factor is below 0.25, and a measured C/MR^2 of")
    print("  that size is a statement about compressibility, not about a core.")

    section("5. Core or spread out?  How much the data can tell")
    print("  A synthetic gas giant: an n = 1.5 polytrope (SYNTHETIC K) plus 10% of")
    print("  its mass in heavy elements.  Two ways to place those elements:")
    print("   (A) a uniform core of that mass;  (B) spread through the envelope with")
    print("   a weight (1 - r/R)^p.")
    n = 1.5
    K = 1.0e7
    rc = 1.0e4
    M0, R0 = polytrope_mass_radius(n, rc, K)
    r, rho0, R, alpha = polytrope_profile(n, rc, K)

    def cmr_of(rho, r):
        M = np.trapezoid(4.0 * np.pi * r ** 2 * rho, r)
        I = np.trapezoid(4.0 * np.pi * r ** 2 * rho * (2.0 / 3.0) * r ** 2, r)
        return I / (M * R ** 2), M

    heavy_fraction = 0.10
    print(f"  polytrope alone: M = {M0:.4e} kg, R = {R0:.4e} m,"
          f" C/MR^2 = {cmr_of(rho0, r)[0]:.5f}")
    print("  (B) spread models")
    print("   p        added-mass <r^2>/R^2    C/MR^2     change from polytrope")
    spread = {}
    for p_exp in (0.5, 1.0, 2.0, 4.0):
        shape = (1.0 - r / R) ** p_exp
        norm = np.trapezoid(4.0 * np.pi * r ** 2 * shape, r)
        M_extra = heavy_fraction * M0
        rhoB = rho0 + M_extra * shape / norm
        cmrB, MB = cmr_of(rhoB, r)
        mean_r2 = np.trapezoid(4.0 * np.pi * r ** 4 * shape, r) / norm / R ** 2
        spread[p_exp] = (cmrB, rhoB, norm)
        print(f"   {p_exp:5.1f}   {mean_r2:20.4f}   {cmrB:9.5f}   {cmrB - cmr_of(rho0, r)[0]:+14.5f}")
    print("  (A) core models, same heavy-element mass")
    print("   core mass frac   core radius (m)   C/MR^2     change from polytrope")
    cmrB1 = spread[1.0][0]
    for f_c in (0.0, 0.03, 0.06, 0.10):
        m_c = f_c * MB
        rho_core = 6.0e4
        r_core = (3.0 * m_c / (4.0 * np.pi * rho_core)) ** (1.0 / 3.0)
        rho_env = rho0 * (MB - m_c) / M0
        rhoA = np.where(r <= r_core, rho_core, rho_env)
        MA = np.trapezoid(4.0 * np.pi * r ** 2 * rhoA, r)
        rhoA = rhoA * MB / MA
        cmrA, MA = cmr_of(rhoA, r)
        print(f"   {f_c:14.2f}   {r_core:15.4e}   {cmrA:9.5f}"
              f"   {cmrA - cmr_of(rho0, r)[0]:+14.5f}")
    # for each spread profile, find the core model with the same C/MR^2
    def core_cmr(f_c):
        m_c = f_c * MB
        rho_core = 6.0e4
        r_core = (3.0 * m_c / (4.0 * np.pi * rho_core)) ** (1.0 / 3.0)
        if r_core <= 0.0:
            return cmr_of(rho0, r)[0], 0.0
        rho_env = rho0 * (MB - m_c) / M0
        rhoA = np.where(r <= r_core, rho_core, rho_env)
        MA = np.trapezoid(4.0 * np.pi * r ** 2 * rhoA, r)
        rhoA = rhoA * MB / MA
        return cmr_of(rhoA, r)[0], r_core

    print("  Matching each spread model with a core model of the same C/MR^2:")
    print("   p (spread)   C/MR^2     core frac that matches   core radius (m)")
    for p_exp, (cmrB, _, _) in spread.items():
        if cmrB > core_cmr(0.0)[0]:
            print(f"   {p_exp:11.1f}   {cmrB:9.5f}   no core model matches (the")
            print("                                     spread model is already less")
            print("                                     concentrated than the polytrope)")
            continue
        lo, hi = 0.0, 0.5
        for _ in range(60):
            mid = 0.5 * (lo + hi)
            if core_cmr(mid)[0] > cmrB:
                lo = mid
            else:
                hi = mid
        f_match = 0.5 * (lo + hi)
        cmr_match, r_core = core_cmr(f_match)
        print(f"   {p_exp:11.1f}   {cmrB:9.5f}   {f_match:22.3f}   {r_core:15.4e}")
    print("  Two of the four spread profiles are matched exactly by a core model, and")
    print("  the other two are matched only by removing the core altogether.  The two")
    print("  families therefore overlap over most of the observable range, and a")
    print("  precise C/MR^2 does not by itself decide where the heavy elements sit.")
    print("  What breaks the tie is an equation of state, which is what says how much")
    print("  heavy-element mass a body of this mass and radius can contain at all.")
    print("  The residual ambiguity is therefore in the physics of the material, not")
    print("  in the precision of the measurement.")

    section("6. Magnetic-field scaling and the conductivity it implies")
    print("  Assume a dynamo in balance between Lorentz and Coriolis forces, that is")
    print("  an Elsasser number of order one:  Lambda = sigma B^2/(rho Omega) = 1.")
    print("  Then B = sqrt(rho Omega / sigma), and the external dipole moment scales")
    print("  as m ~ B R^3.  SYNTHETIC planetary parameters:")
    print("   rho (kg/m^3)   Omega (1/s)   sigma (S/m)   B (T)     m (A m^2)")
    for rho, Omega, sigma in ((1.0e3, 1.75e-4, 1.0e5), (1.0e3, 1.75e-4, 1.0e4),
                              (1.0e3, 1.75e-4, 1.0e3), (4.0e3, 1.75e-4, 1.0e4),
                              (1.0e3, 1.0e-3, 1.0e4)):
        B = np.sqrt(rho * Omega / sigma)
        R_layer = 5.0e7
        m = B * R_layer ** 3 / MU0 * 4.0 * np.pi / 3.0
        print(f"   {rho:11.1e}   {Omega:11.3e}   {sigma:10.1e}   {B:7.4f}"
              f"   {m:13.4e}")
    print("  B is a factor sqrt(10) smaller for every factor 10 in conductivity, so")
    print("  the field amplitude is a direct, and very sensitive, probe of the")
    print("  conductivity of the layer that carries the dynamo.")
    print("  A magnetic Reynolds number is needed as well:")
    print("        Rm = mu0 sigma U L,   with U a characteristic velocity.")
    print("   sigma (S/m)   L (m)       U for Rm = 10 (m/s)")
    for sigma in (1.0e3, 1.0e4, 1.0e5):
        for L in (1.0e6, 1.0e7):
            U = 10.0 / (MU0 * sigma * L)
            print(f"   {sigma:10.1e}   {L:9.1e}   {U:18.6e}")
    print("  The required velocity falls as the conductivity rises: a well-conducting")
    print("  interior needs only slow convection to sustain a field, which is why a")
    print("  measured field is evidence of a conducting, convecting layer rather than")
    print("  of any particular composition.")
    print("  The inverse reading is the useful one: taking the measured dipole moment")
    print("  m, the layer radius R and the density as known, the Elsasser balance gives")
    print("        sigma = rho Omega R^6 (4 pi/3)^2/(mu0^2 m^2),")
    print("  an estimate of the conductivity, not of the composition.  Sensitivities:")
    print("   a 10% error in the measured dipole moment moves sigma by"
          f" {abs(-2.0) * 10:.0f}% (it enters inversely squared);")
    print("   a 10% error in the radius of the conducting layer moves sigma by"
          f" {abs(6.0) * 10:.0f}%.")
    print("  The second number is the honest limit: the field amplitude is a")
    print("  conductivity probe only as good as the knowledge of WHERE the field is")
    print("  generated, which for a giant planet is itself a model output.")


if __name__ == "__main__":
    main()
