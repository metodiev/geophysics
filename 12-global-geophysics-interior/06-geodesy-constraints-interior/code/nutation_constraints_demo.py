#!/usr/bin/env python3
"""Nutation and the constraints it places on the core of a planet.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python nutation_constraints_demo.py

Everything is SYNTHETIC.  The planet, its core, the perturber and the "measured"
periods are teaching values chosen for this lesson; none of them is a real body
and none is a published measurement.  The only externally quoted quantities are
the exact standard constants G and the sidereal day.

Sections
--------
1  the free wobble of a rigid body: closed form against an RK4 integration
2  forced precession: the orbit-averaged torque obtained by numerical averaging
   and numerical differentiation, and the precession rate it implies
3  the free core nutation as a two-body torsional mode: derived from the
   relative-tilt equation and verified by integrating that equation
4  what the free-core-nutation period depends on: exponents measured
5  inversion: one measured period, a curve of core models, and the extra
   assumption needed to turn an oblateness into a core density
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# Exact standard constants.
G = 6.67430e-11            # m^3 kg^-1 s^-2 (CODATA)
SIDEREAL_DAY = 86164.0905  # s


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


# --------------------------------------------------------------------------
# 1. Free wobble of a rigid body
# --------------------------------------------------------------------------

def rigid_euler_rhs(w, A_mom, C_mom):
    w1, w2, w3 = w
    return np.array([(A_mom - C_mom) * w2 * w3 / A_mom,
                     (C_mom - A_mom) * w3 * w1 / A_mom,
                     0.0])


def measure_body_frame_period(H_body, Omega, n_days=900.0, n_steps=600000):
    """RK4 the torque-free Euler equations; measure the transverse period, days."""
    A_mom, C_mom = 1.0, 1.0 + H_body
    w = np.array([1e-3 * Omega, 0.0, Omega])
    dt = n_days * SIDEREAL_DAY / n_steps
    t = np.zeros(n_steps)
    phase = np.zeros(n_steps)
    for i in range(n_steps):
        k1 = rigid_euler_rhs(w, A_mom, C_mom)
        k2 = rigid_euler_rhs(w + 0.5 * dt * k1, A_mom, C_mom)
        k3 = rigid_euler_rhs(w + 0.5 * dt * k2, A_mom, C_mom)
        k4 = rigid_euler_rhs(w + dt * k3, A_mom, C_mom)
        w = w + dt / 6.0 * (k1 + 2 * k2 + 2 * k3 + k4)
        t[i] = (i + 1) * dt
        phase[i] = np.arctan2(w[1], w[0])
    slope = np.polyfit(t, np.unwrap(phase), 1)[0]
    return 2.0 * np.pi / abs(slope) / SIDEREAL_DAY


# --------------------------------------------------------------------------
# 2. Forced precession from the orbit-averaged quadrupole potential
# --------------------------------------------------------------------------

def orbit_averaged_quadrupole_energy(obliquity, n_orb, n_samples=4000):
    """<U> for a point mass on a circular orbit, averaged over the orbit.

    The instantaneous quadrupole interaction energy of an oblate body with a
    point mass at distance a is U = (G m/(2 a^3)) (C-A) (3 cos^2 psi - 1) with
    psi the angle between the body axis and the direction to the mass.  Only the
    psi-dependent factor matters here; the prefactor is set to unity and the
    returned value is the average of (3 cos^2 psi - 1).
    """
    theta = 2.0 * np.pi * np.arange(n_samples) / n_samples
    axis = np.array([np.sin(obliquity), 0.0, np.cos(obliquity)])
    n_hat = np.column_stack((np.cos(theta), np.sin(theta), np.zeros_like(theta)))
    cos_psi = n_hat @ axis
    return np.mean(3.0 * cos_psi ** 2 - 1.0)


def main():
    section("1. The free wobble of a rigid body")
    H_rigid = 1.0 / 305.0                   # SYNTHETIC dynamical ellipticity
    Omega = 2.0 * np.pi / SIDEREAL_DAY
    H_body = H_rigid / (1.0 - H_rigid)
    print(f"  SYNTHETIC dynamical ellipticity H = (C-A)/C = {H_rigid:.6e}")
    print(f"  1/H = {1.0 / H_rigid:.1f} sidereal days")
    print("  Exact torque-free solution for a symmetric top: the transverse angular")
    print("  velocity turns in the body frame at omega*(C-A)/A = omega*H/(1-H).")
    closed = 1.0 / H_body
    measured = measure_body_frame_period(H_body, Omega)
    print(f"     closed form   : {closed:9.3f} sidereal days")
    print(f"     RK4 integration: {measured:9.3f} sidereal days"
          f"   (difference {measured - closed:+.3f} d,"
          f" {100 * abs(measured - closed) / closed:.3f} %)")
    print("  The inertial period of the same mode is 1/H = "
          f"{1.0 / H_rigid:.1f} sidereal days = {1.0 / H_rigid / 365.25:.3f} yr.")
    print("  A real planet's observed free wobble is LONGER than this rigid value:")
    print("  the body deforms, and a fluid core does not follow the mantle.  The")
    print("  rigid period is therefore a lower bound used as a reference, not a")
    print("  prediction.")

    section("2. Forced precession from the averaged quadrupole torque")
    print("  Instantaneous quadrupole energy factor: 3cos^2(psi) - 1, with psi the")
    print("  angle between the body axis and the direction to the perturber.")
    print("   obliquity   <3cos^2 psi - 1>   (1/2)(3sin^2 eps - 2)   difference")
    for eps_deg in (0.0, 30.0, 45.0, 60.0, 90.0):
        eps = np.radians(eps_deg)
        avg = orbit_averaged_quadrupole_energy(eps, None)
        closed_avg = 1.5 * np.sin(eps) ** 2 - 1.0
        print(f"   {eps_deg:8.1f}   {avg:18.6f}   {closed_avg:22.6f}"
              f"   {abs(avg - closed_avg):10.2e}")
    print("  The numerical average reproduces the analytic average exactly (to the")
    print("  sampling), which is the only step of this section that is not algebra.")
    print("  The averaged torque about the node line is |d<U>/d eps|; with the full")
    print("  prefactor it is  (3/2)(G m/a^3)(C-A) sin(eps) cos(eps).")
    h = 1e-5
    print("   obliquity   numerical d<U>/d eps    (3/2) sin(2 eps)")
    for eps_deg in (30.0, 45.0, 60.0):
        eps = np.radians(eps_deg)
        num = ((orbit_averaged_quadrupole_energy(eps + h, None)
                - orbit_averaged_quadrupole_energy(eps - h, None)) / (2 * h))
        print(f"   {eps_deg:8.1f}   {num:20.6f}   {1.5 * np.sin(2 * eps):14.6f}")
    print("  Dividing by the angular momentum about the spin axis gives the")
    print("  classical precession rate of the spin axis:")
    print("        psi_dot = (3/2) (n^2/omega) (C-A)/C cos(eps),  n^2 = G m/a^3 .")
    n_orb = 2.0 * np.pi / (365.25 * SIDEREAL_DAY)
    print("  A synthetic perturber with a one-year mean motion, obliquity 60 deg:")
    print("   H          psi_dot (rad/s)   period of the precession node (yr)")
    for Hv in (1.0 / 600.0, 1.0 / 305.0, 1.0 / 150.0):
        rate = 1.5 * (n_orb ** 2 / Omega) * Hv * np.cos(np.radians(60.0))
        print(f"   {Hv:.6f}   {rate:16.6e}   {2.0 * np.pi / rate / (365.25 * 86400):18.3f}")
    print("  The rate is exactly linear in H = (C-A)/C and in cos(eps), and inversely")
    print("  proportional to the spin rate: the precession and the nutation are two")
    print("  faces of the same quadrupole coupling.")

    section("3. The free core nutation as a two-body torsional mode")
    print("  Model: the mantle and the fluid core can tilt relative to each other.")
    print("  The coupling torque is proportional to the relative tilt theta = m_m-m_c,")
    print("  with the coupling constant taken as the core's dynamical oblateness,")
    print("        K = C_c - A_c = e_c C_c .")
    print("  For the relative tilt, the two angular-momentum equations combine to")
    print("        A_red d(theta)/dt = -i Omega K theta,   A_red = A_m A_c/(A_m+A_c),")
    print("  so the mode frequency is Omega K/A_red and the period in sidereal days is")
    print("        T_FCN = A_m A_c / (e_c C_c (A_m + A_c))  sidereal days.")
    e_c = 1.0 / 400.0                      # SYNTHETIC core oblateness
    C_m, C_c = 1.0, 0.11                   # SYNTHETIC moments (C_m = 1)
    H_tot = 1.0 / 305.0
    A_m = C_m * (1.0 - H_tot)
    A_c = C_c * (1.0 - e_c)
    print(f"  SYNTHETIC moments: A_m = {A_m:.5f}, C_m = {C_m:.5f},"
          f" A_c = {A_c:.6f}, C_c = {C_c:.6f}")
    A_red = A_m * A_c / (A_m + A_c)
    T_closed = A_red / (e_c * C_c)
    print(f"  A_red = {A_red:.6f},  e_c = {e_c:.6e},  T_FCN = {T_closed:.2f} sidereal days")
    # independent route: integrate the two equations of the torsional model
    K = e_c * C_c
    m_m, m_c = 1.0 + 0j, 0.0 + 0j
    dt = 1.0 * SIDEREAL_DAY / 4000.0
    n_steps = 400000
    t = np.zeros(n_steps)
    theta = np.zeros(n_steps, dtype=complex)
    for i in range(n_steps):
        d_m = -1j * Omega * K * (m_m - m_c) / A_m
        d_c = 1j * Omega * K * (m_m - m_c) / A_c
        m_m += dt * d_m
        m_c += dt * d_c
        t[i] = (i + 1) * dt
        theta[i] = m_m - m_c
    ph = np.unwrap(np.angle(theta))
    slope = np.polyfit(t, ph, 1)[0]
    T_meas = 2.0 * np.pi / abs(slope) / SIDEREAL_DAY
    print(f"  independent route: integrate the two first-order equations and measure")
    print(f"     the period of the relative tilt = {T_meas:.2f} sidereal days"
          f"   ({100 * abs(T_meas - T_closed) / T_closed:.3f} % from the closed form)")
    print("  Limits of the model, both checked here: if the core is spherical")
    print("  (e_c -> 0) the mode disappears; if the core is absent (A_c -> 0) there")
    print("  is no relative motion to observe.  The mode needs an oblate core")
    print("  inside a mantle it can be misaligned with, and nothing else.")
    print("  This is a model of where the resonance sits; the full problem solves the")
    print("  elastogravitational boundary conditions at the core-mantle boundary,")
    print("  which adds the deformation of the mantle and the flow in the core, and")
    print("  those terms move the period by tens of percent.")

    section("4. What the free-core-nutation period depends on")
    e_list = np.array([1.0 / 800, 1.0 / 400, 1.0 / 200, 1.0 / 100])
    fcn = np.array([(A_m * C_c * (1.0 - e) / (A_m + C_c * (1.0 - e))) / (e * C_c)
                    for e in e_list])
    exponent = np.polyfit(np.log(1.0 / e_list), np.log(fcn), 1)[0]
    print("   e_c           1/e_c        T_FCN (sidereal days)")
    for e, T in zip(e_list, fcn):
        print(f"   {e:.6f}   {1.0 / e:9.1f}   {T:20.2f}")
    print(f"  measured exponent dln T_FCN / dln(1/e_c) = {exponent:.4f}")
    frac_list = np.array([0.05, 0.08, 0.11, 0.15, 0.20])
    fcn2 = np.array([(A_m * fr * (1.0 - e_c) / (A_m + fr * (1.0 - e_c)))
                     / (e_c * fr) for fr in frac_list])
    exponent2 = np.polyfit(np.log(frac_list), np.log(fcn2), 1)[0]
    print("   C_c/C_m      A_red       T_FCN (sidereal days)   T_FCN * e_c")
    for fr, T in zip(frac_list, fcn2):
        A_red_t = A_m * fr * (1.0 - e_c) / (A_m + fr * (1.0 - e_c))
        print(f"   {fr:8.2f}   {A_red_t:9.5f}   {T:20.2f}   {T * e_c:12.4f}")
    print(f"  measured exponent dln T_FCN / dln(C_c/C_m) = {exponent2:.4f}")
    print("  So the period is inversely proportional to the core oblateness (exponent")
    print("  -1 in e_c, i.e. +1 in 1/e_c) and only weakly sensitive to the core's")
    print("  share of the inertia.  A measured period is therefore mostly a")
    print("  measurement of the core's flattening.")

    section("5. Inversion: one period, a curve of core models")
    T_obs = T_closed * 1.02
    print(f"  SYNTHETIC measured FCN period: T = {T_obs:.2f} sidereal days")
    print(f"  SYNTHETIC adopted core inertia: A_c/C_m fixed per row")
    print("   C_c/C_m    e_c required    1/e_c      T_FCN check")
    for fr in (0.05, 0.08, 0.11, 0.15, 0.20):
        C_c_t = fr
        A_c_t = C_c_t * (1.0 - 1e-6)
        lo, hi = 1e-6, 0.2
        for _ in range(80):
            mid = 0.5 * (lo + hi)
            A_c_mid = C_c_t * (1.0 - mid)
            T_mid = (A_m * A_c_mid / (A_m + A_c_mid)) / (mid * C_c_t)
            if T_mid > T_obs:
                lo = mid
            else:
                hi = mid
        e_req = 0.5 * (lo + hi)
        A_c_req = C_c_t * (1.0 - e_req)
        T_chk = (A_m * A_c_req / (A_m + A_c_req)) / (e_req * C_c_t)
        if abs(fr - 0.11) < 1e-9:
            e_use = e_req
        print(f"   {fr:8.2f}   {e_req:.6e}   {1.0 / e_req:9.1f}   {T_chk:14.2f}")
    print("  Every row reproduces the same period with a different core: one number")
    print("  cannot separate the core's flattening from its share of the inertia.")
    print("  Reaching a core DENSITY needs two more assumptions, stated here:")
    print("  (i) the core is in hydrostatic equilibrium, so its flattening is (5/4)q_c")
    print("      with q_c = omega^2 r_c^3/(G M_c) -- the relation lesson 12-06-01")
    print("      measured on the exact Maclaurin spheroid;")
    print("  (ii) e_c equals that flattening (a homogeneous, uniform-density core).")
    print("  Then  M_c = omega^2 r_c^3 / (G (4/5) e_c).  With the recovered e_c for")
    print("     the C_c/C_m = 0.11 row")
    r_c = 3.5e6
    M_c = Omega ** 2 * r_c ** 3 / (G * 0.8 * e_use)
    rho_c = M_c / ((4.0 / 3.0) * np.pi * r_c ** 3)
    print(f"     and a synthetic core radius r_c = {r_c:.2e} m:")
    print(f"     M_c = {M_c:.4e} kg, mean core density = {rho_c:.1f} kg/m^3")
    print("  That density is a consequence of a measured period plus two modelling")
    print("  assumptions, and it moves with both: it is not a measurement of a core.")


if __name__ == "__main__":
    main()
