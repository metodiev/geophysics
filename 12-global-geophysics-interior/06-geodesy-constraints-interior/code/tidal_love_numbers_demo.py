#!/usr/bin/env python3
"""Love numbers and theoretical tides: how the tidal response of a body is
measured, what it constrains about the interior, and what it leaves open.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python tidal_love_numbers_demo.py

Everything is SYNTHETIC.  The body is a teaching body with chosen mass, radius,
density and rigidity; no number below is a measurement of a real planet.  The
only externally quoted quantity is the exact standard constant G.

Sections
--------
1  the degree-2 shell potential kernel, closed form against quadrature, and the
   exact ratio k2 = (3/5) h2 that follows for any homogeneous body
2  the fluid limit derived from the kernel: h2 = 5/2, k2 = 3/2, h2 = 1 + k2, and
   a cross-check against the exact Maclaurin spheroid figure
3  the elastic (Kelvin) homogeneous-sphere Love numbers: limits, ratio and the
   1/mu asymptote measured
4  the observables built from h2 and k2: the gravity-tide amplitude factor and
   the surface-tilt factor, both evaluated across the rigidity range
5  the inverse problem: a synthetic measured h2 and the range of rigidity it
   admits, with the amplification measured
6  the degeneracy: one h2, a one-parameter family of (density, rigidity) pairs
7  frequency dependence: a Maxwell body, the phase lag of the tide, and the
   amplitude of k2 across frequency
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# Exact standard constant, SI (CODATA): gravitational constant.
G = 6.67430e-11  # m^3 kg^-1 s^-2


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


# --------------------------------------------------------------------------
# 1. The degree-2 shell kernel
# --------------------------------------------------------------------------

def shell_p2_closed(r_obs, R, sigma2):
    """Degree-2 potential coefficient of a shell of radius R, density sigma2 P2."""
    if r_obs >= R:
        return -(4.0 * np.pi * G * sigma2 / 5.0) * R ** 4 / r_obs ** 3
    return -(4.0 * np.pi * G * sigma2 / 5.0) * r_obs ** 2 / R


def shell_p2_quadrature(r_obs, R, sigma2, n_mu=4000):
    """The same coefficient by direct quadrature on the polar axis."""
    mu = -1.0 + (np.arange(n_mu) + 0.5) * 2.0 / n_mu
    dmu = 2.0 / n_mu
    p2 = 0.5 * (3.0 * mu ** 2 - 1.0)
    dist = np.sqrt(R ** 2 + r_obs ** 2 - 2.0 * R * r_obs * mu)
    return -2.0 * np.pi * R ** 2 * G * sigma2 * np.sum(p2 / dist * dmu)


# --------------------------------------------------------------------------
# 2. Exact Maclaurin spheroid (for the cross-check)
# --------------------------------------------------------------------------

def spheroid_A(e):
    """Internal potential coefficients A1 (=A2) and A3 of a homogeneous spheroid."""
    if e < 1e-12:
        return 2.0 / 3.0, 2.0 / 3.0
    A1 = (np.sqrt(1.0 - e ** 2) / e ** 3) * np.arcsin(e) - (1.0 - e ** 2) / e ** 2
    A3 = 2.0 / e ** 2 * (1.0 - (np.sqrt(1.0 - e ** 2) / e) * np.arcsin(e))
    return A1, A3


def maclaurin_q(x):
    """Rotation parameter q = omega^2 a^3/(GM) of the exact Maclaurin spheroid."""
    a, c = 1.0, x
    e = np.sqrt(1.0 - x ** 2)
    A1, A3 = spheroid_A(e)
    return 3.0 * (A1 * a ** 2 - A3 * c ** 2) / (2.0 * a * c)


def solve_maclaurin(q_target):
    lo, hi = 0.05, 1.0 - 1e-12
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if maclaurin_q(mid) > q_target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


# --------------------------------------------------------------------------
# 3. Love numbers of a homogeneous body
# --------------------------------------------------------------------------

def love_numbers_homogeneous(mu_over_rho_g_R):
    """Degree-2 static Love numbers of a homogeneous incompressible sphere.

    Fluid limit (the classical result, derived in section 2 of the lesson):
        h2 = 5/2, k2 = 3/2, l2 = 0.
    Kelvin's elastic result for a homogeneous incompressible sphere:
        h2 = (5/2) / (1 + (19/2) mu/(rho g R)),  k2 = (3/5) h2.
    """
    x = 1.0 + 9.5 * mu_over_rho_g_R
    h2 = 2.5 / x
    return h2, 0.6 * h2


def main():
    section("1. The degree-2 shell kernel and the exact ratio k2 = (3/5) h2")
    R, rho = 1.0e6, 3.0e3                      # SYNTHETIC body
    g = (4.0 / 3.0) * np.pi * G * rho * R      # surface gravity of the uniform sphere
    print(f"  SYNTHETIC homogeneous sphere: R = {R:.3e} m, rho = {rho:.3e} kg/m^3")
    print(f"  surface gravity g = GM/R^2 = {g:.4f} m/s^2")
    sigma2 = rho * 1.0                          # unit surface displacement (u = 1 m)
    u = 1.0
    shell_val = shell_p2_closed(R, R, sigma2 * u)
    print(f"  a P2 surface layer of density rho*u, u = {u:.1f} m, at r = R:")
    print(f"    closed form  V2 = {shell_val:.6e} J/kg")
    print(f"    quadrature   V2 = {shell_p2_quadrature(R, R, sigma2 * u):.6e} J/kg"
          "   (on-shell point: the quadrature is biased, see below)")
    for rr in (0.5, 1.5, 2.0):
        c = shell_p2_closed(rr * R, R, sigma2 * u)
        q = shell_p2_quadrature(rr * R, R, sigma2 * u)
        print(f"    r/R = {rr:3.1f}: closed {c:14.6e}   quadrature {q:14.6e}"
              f"   rel. err {abs(q - c) / abs(c):.1e}")
    ratio = abs(shell_val) / (g * u)
    print(f"  the induced degree-2 potential at the surface per unit displacement,")
    print(f"  divided by g*u, is {ratio:.6f}; the kernel gives exactly 3/5 = 0.6.")
    print("  Hence for ANY homogeneous body k2 = (3/5) h2, whatever its rheology:")
    print("  the ratio is geometry, not material.  (The on-shell quadrature is biased")
    print("  because the integrand is singular there; the closed form is the limit of")
    print("  its two branches, which the off-shell rows confirm to about 2e-6.)")

    section("2. The fluid limit, and a cross-check against the exact figure")
    print("  Equipotential condition on the deformed surface (+: as above):")
    print("     V0 + g u - (3/5) g u = 0  =>  u = (5/2) V0/g,  so h2 = 5/2")
    print("     k2 = |V_induced|/V0 = (3/5) g u / V0 = 3/2, and h2 = 1 + k2.")
    h2_fluid, k2_fluid = 2.5, 1.5
    print(f"  h2 = {h2_fluid:.4f}, k2 = {k2_fluid:.4f}, h2 - (1 + k2) ="
          f" {h2_fluid - (1.0 + k2_fluid):.1e}")
    print("  Cross-check with the rotational tide V0 = (1/3) omega^2 R^2 P2:")
    print("     u/R = h2 (1/3) q  =>  f = (a-c)/a = -1.5 u/R = (5/4) q.")
    rows = []
    for q in (1.0e-3, 3.0e-3, 1.0e-2):
        x = solve_maclaurin(q)
        rows.append((q, 1.0 - x, (1.0 - x) / q))
    print("     exact Maclaurin spheroid:  q        f/q")
    for q, f, fq in rows:
        print(f"                               {q:8.0e}  {fq:8.4f}")
    print("     the fluid Love number h2 = 5/2 predicts f/q = 5/4 = 1.2500, which is")
    print("     what the exact figure gives in the small-rotation limit.")
    h2_rot_pred = h2_fluid * (1.0 / 3.0)
    print(f"     the same number is obtained from u/R = h2*(1/3)q -> f = 1.5*u/R"
          f" = {1.5 * h2_rot_pred:.4f} q")

    section("3. The elastic homogeneous sphere: Kelvin's Love numbers")
    M = (4.0 / 3.0) * np.pi * rho * R ** 3
    print(f"  SYNTHETIC body: M = {M:.3e} kg, and mu/(rho g R) is the single")
    print("  dimensionless rigidity that a homogeneous body has.")
    print("   mu/(rho g R)     mu (Pa)      h2        k2      k2/h2    h2*mu_hat")
    for mu_hat in (0.0, 0.05, 0.1, 0.5, 1.0, 5.0, 50.0, 500.0):
        h2, k2 = love_numbers_homogeneous(mu_hat)
        mu_Pa = mu_hat * rho * g * R
        print(f"   {mu_hat:11.3f}   {mu_Pa:11.3e}   {h2:7.4f}   {k2:7.4f}   "
              f"{(k2 / h2 if h2 > 0 else 0.0):6.4f}   {h2 * mu_hat:8.4f}")
    print("  Fluid limit mu -> 0: h2 -> 2.5000, k2 -> 1.5000, as section 2 requires.")
    print("  Rigid limit mu -> inf: h2 -> 0 (no deformation, no induced potential).")
    print(f"  Large-mu asymptote: h2 * mu_hat -> 5/19 = {5.0 / 19.0:.5f}; the table")
    print("  approaches it, which is the only place the coefficient 19 appears.")
    print("  The ratio k2/h2 = 0.6 throughout, as section 1 proved it must be.")

    section("4. What a tide gauge and a gravimeter see")
    print("  Two observable combinations of the Love numbers:")
    print("     gravity-tide amplitude factor  delta = 1 + h2 - (3/2) k2")
    print("     surface-tilt factor            tau   = 1 + k2 - h2")
    print("   mu/(rho g R)      h2       k2      delta      tau")
    for mu_hat in (0.0, 0.1, 0.5, 1.0, 5.0, 50.0):
        h2, k2 = love_numbers_homogeneous(mu_hat)
        delta = 1.0 + h2 - 1.5 * k2
        tau = 1.0 + k2 - h2
        print(f"   {mu_hat:11.3f}   {h2:7.4f}   {k2:7.4f}   {delta:8.4f}   {tau:8.4f}")
    print("  Limits: a fluid body has delta = 1.25 and tau = 0 (its surface is an")
    print("  equipotential, so there is no tilt relative to the equilibrium tide);")
    print("  a rigid body has delta = tau = 1.  The measured delta therefore says how")
    print("  fluid the body is, but only through the single combination mu/(rho g R).")

    section("5. Inversion: one measured number, one admitted range")
    h2_obs, sigma_obs = 0.60, 0.01              # SYNTHETIC measured value
    print(f"  SYNTHETIC measurement: h2 = {h2_obs:.2f} +/- {sigma_obs:.2f}")
    print("  Invert h2 = (5/2)/(1 + (19/2) mu_hat) for mu_hat = mu/(rho g R):")

    def mu_hat_of_h2(h2):
        return (2.5 / h2 - 1.0) / 9.5

    for h2v in (h2_obs - sigma_obs, h2_obs, h2_obs + sigma_obs):
        print(f"     h2 = {h2v:4.2f}  ->  mu_hat = {mu_hat_of_h2(h2v):7.4f}"
              f"   mu = {mu_hat_of_h2(h2v) * rho * g * R:.4e} Pa")
    sens = abs((mu_hat_of_h2(h2_obs + 1e-4) - mu_hat_of_h2(h2_obs - 1e-4))
               / (2e-4) * h2_obs / mu_hat_of_h2(h2_obs))
    print(f"  measured amplification |dln mu_hat/dln h2| = {sens:.3f}: a 1% error in")
    print(f"  h2 moves the inferred rigidity by about {100 * sens:.0f}%, so the rigidity is")
    print("  comparatively well determined -- but only for THIS parametrisation.")
    print("  The real limit is that h2 is a functional of the whole profile: a body")
    print("  with a stiff lid and a weak interior can return the same h2 as a uniform")
    print("  body with an intermediate rigidity.  A single h2 cannot see the profile.")

    section("6. Degeneracy: one h2, one family of (density, rigidity) pairs")
    print(f"  With g and R fixed by mass and radius, only mu/rho is constrained.")
    print(f"  For the measured value h2 = {h2_obs:.2f}: mu_hat ="
          f" {mu_hat_of_h2(h2_obs):.4f}, so mu = {mu_hat_of_h2(h2_obs) * g * R:.4e} * rho.")
    print("   rho (kg/m^3)      mu (Pa)        h2 check")
    for rho_try in (2.5e3, 3.5e3, 5.0e3, 6.0e3):
        mu_Pa = mu_hat_of_h2(h2_obs) * rho_try * g * R
        h2chk, _ = love_numbers_homogeneous(mu_Pa / (rho_try * g * R))
        print(f"   {rho_try:12.1f}   {mu_Pa:11.4e}   {h2chk:8.4f}")
    print("  Every row reproduces the same h2 with a different (rho, mu): the tide")
    print("  measures a ratio, and mass and radius are already used in mu_hat.")

    section("7. Frequency dependence: a Maxwell body")
    tau_M = 3.0e3 * 3.15e7                      # Maxwell time, SYNTHETIC (3000 yr)
    mu_e = 0.5 * rho * g * R                    # SYNTHETIC elastic rigidity
    mu_hat_e = mu_e / (rho * g * R)
    print(f"  SYNTHETIC Maxwell body: mu_hat = {mu_hat_e:.3f},"
          f" Maxwell time tau = {tau_M:.3e} s")
    print(f"  complex rigidity mu(omega) = mu * i omega tau / (1 + i omega tau)")
    print("   period (h)     omega (1/s)     |h2|      |k2|     arg k2 (deg)")
    for period_h in (12.0, 1.0e3, 1.0e6, 1.0e8, 1.0e9, 1.0e11):
        omega = 2.0 * np.pi / (period_h * 3600.0)
        mu_c = mu_e * (1j * omega * tau_M) / (1.0 + 1j * omega * tau_M)
        h2_c, k2_c = love_numbers_homogeneous(mu_c / (rho * g * R))
        print(f"   {period_h:10.1f}   {omega:12.3e}   {abs(h2_c):7.4f}   "
              f"{abs(k2_c):7.4f}   {np.degrees(np.angle(k2_c)):12.3f}")
    print("  At periods much shorter than tau the body is elastic (|k2| ~ 0.26); at")
    print("  periods longer than tau it relaxes toward the fluid value |k2| = 1.5.")
    print("  The phase lag separates dissipation from elasticity, and it is what makes")
    print("  the tide a dissipation (Q) measurement and not only a rigidity one.")
    print("  A real body has a spectrum of Maxwell times, so a single-frequency")
    print("  inversion again returns an effective, not a local, property.")


if __name__ == "__main__":
    main()
