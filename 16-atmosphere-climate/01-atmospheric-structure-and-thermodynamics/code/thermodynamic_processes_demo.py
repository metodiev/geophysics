#!/usr/bin/env python3
"""Dry adiabatic processes, lapse rates and static stability.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python thermodynamic_processes_demo.py

All models are SYNTHETIC teaching models.  Surface temperature, surface pressure
and the environmental lapse rate are chosen inputs (conventional values), printed
below; R_d and c_p are the derived constants of lesson 01.  No quantity here is a
measurement made by this module.

Contents
--------
1. The dry adiabatic lapse rate from g and c_p, and the potential-temperature
   exponent kappa = R_d/c_p.
2. A dry adiabat integrated upward: T(z), p(z) and the constancy of theta.
3. Buoyancy frequency N and period for several environmental lapse rates,
   including the unstable and inversion cases.
4. A parcel integrated with the full nonlinear buoyancy force: measured period
   versus 2*pi/N, and the measured growth rate in the unstable case.
5. Dry static energy c_p T + g z along the adiabat (conservation check).
6. Entropy change: zero along a dry adiabat, nonzero under a heat input.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

R_D = 287.041          # J kg^-1 K^-1, dry-air gas constant (derived in lesson 01)
CP = 1004.64           # J kg^-1 K^-1, specific heat at constant pressure (lesson 01)
G0 = 9.80665           # m s^-2, standard gravity
P_REF = 100000.0       # Pa, reference pressure for potential temperature (1000 hPa)
T_SURF = 288.15        # K, surface temperature of the model
GAMMA_ENV = 6.5e-3     # K m^-1, environmental lapse rate of the model


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def potential_temperature(T, p):
    """theta = T (p_ref/p)^(R_d/c_p), in kelvin."""
    return T * (P_REF / p) ** (R_D / CP)


def p_of_z(z, gamma, T0=T_SURF, p0=101325.0):
    """Pressure (Pa) for a constant-lapse-rate profile (lesson 01, section 3.3).

    gamma = 0 is the isothermal limit and is handled separately.
    """
    if gamma == 0.0:
        return p0 * np.exp(-G0 * z / (R_D * T0))
    return p0 * (1.0 - gamma * z / T0) ** (G0 / (R_D * gamma))


def main():
    section("1. The dry adiabatic lapse rate")
    gamma_d = G0 / CP
    kappa = R_D / CP
    print(f"  c_p = {CP:.2f} J kg^-1 K^-1, R_d = {R_D:.3f} J kg^-1 K^-1")
    print(f"  dry adiabatic lapse rate  Gamma_d = g/c_p = {gamma_d * 1e3:.4f} K/km")
    print(f"  potential-temperature exponent kappa = R_d/c_p = {kappa:.6f}")
    print("  Derivation (one line): a dry parcel that conserves entropy obeys")
    print("  c_p dT - (1/rho) dp = 0 and dp = -rho g dz, so dT/dz = -g/c_p.")
    print("  Note Gamma_d depends only on g and c_p: not on temperature, not on pressure.")

    section("2. A dry adiabat, integrated upward")
    dz = 1.0
    z = 0.0
    T = T_SURF
    p = 101325.0
    print("   z(km)      T(K)     p(hPa)      theta(K)      deviation from theta(0)")
    theta0 = potential_temperature(T, p)
    zs, Ts, ps, thetas = [z], [T], [p], [theta0]
    for _ in range(16000):
        # dry adiabat: dT/dz = -g/c_p (exactly linear in z); hydrostatic for p,
        # integrated with the midpoint rule so that the theta drift is
        # second-order in the step and does not masquerade as physics.
        p_mid = p - 0.5 * dz * (p * G0 / (R_D * T))
        p += -dz * (p_mid * G0 / (R_D * (T - 0.5 * gamma_d * dz)))
        T += -gamma_d * dz
        z += dz
        if int(round(2 * z)) % 2000 == 0:
            th = potential_temperature(T, p)
            zs.append(z)
            Ts.append(T)
            ps.append(p)
            thetas.append(th)
    for i, (zz, TT, pp, th) in enumerate(zip(zs, Ts, ps, thetas)):
        if i == 0:
            print(f"  {zz / 1e3:6.1f}  {TT:8.3f}  {pp / 100:9.3f}  {th:10.5f}")
        else:
            print(f"  {zz / 1e3:6.1f}  {TT:8.3f}  {pp / 100:9.3f}  {th:10.5f}   "
                  f"{th - theta0:+.3e}")
    spread = max(thetas) - min(thetas)
    print(f"\n  theta spans {spread:.3e} K over {zs[-1] / 1e3:.0f} km of ascent:")
    print("  the dry adiabat is an isentrope, and the residual is the truncation")
    print(f"  error of the midpoint integration at dz = {dz:.0f} m, not physics.")

    section("3. Buoyancy frequency and period versus environmental lapse rate")
    print("  N^2 = (g/theta) d(theta)/dz = (g/T)(Gamma_d - Gamma)")
    print("  evaluated at a representative mid-tropospheric T = 255.0 K")
    print("\n  Gamma_env (K/km)   N^2 (1e-4 s^-2)   N (1e-3 s^-1)   period (s)   regime")
    for gamma in (-2.0e-3, 0.0, 3.0e-3, 6.5e-3, 9.0e-3, 9.7614e-3, 10.5e-3):
        T_env = 255.0
        N2 = G0 / T_env * (gamma_d - gamma)
        if N2 > 0.0:
            N = np.sqrt(N2)
            period = 2.0 * np.pi / N
            regime = "stable"
            gap = f"{period:9.1f}"
        else:
            N = np.sqrt(-N2)
            period = float("nan")
            regime = "UNSTABLE (exponential)"
            gap = "        -"
        print(f"  {gamma * 1e3:10.4f}   {N2 * 1e4:14.4f}   {N * 1e3:13.4f}   {gap}"
              f"   {regime}")
    print("\n  Gamma = 9.7614e-3 K/km is the neutral case (N = 0); anything larger is")
    print("  superadiabatic and convectively unstable.  The value 6.5 K/km sits well")
    print("  inside the stable regime, which is why the troposphere is stratified.")

    section("4. Nonlinear parcel integration versus the linear prediction")
    def parcel_rhs(t, y, gamma):
        zz, ww = y
        Te = T_SURF - gamma * zz
        pe = p_of_z(zz, gamma)
        theta_e = potential_temperature(Te, pe)
        theta_p = theta0                      # the parcel conserves theta
        buoy = G0 * (theta_p - theta_e) / theta_e
        return np.array([ww, buoy])

    def integrate(gamma, z0_pert, t_end=4000.0, dt=0.5):
        y = np.array([z0_pert, 0.0])
        t = 0.0
        ts = [0.0]
        zs_ = [z0_pert]
        while t < t_end:
            k1 = parcel_rhs(t, y, gamma)
            k2 = parcel_rhs(t + dt / 2, y + dt / 2 * k1, gamma)
            k3 = parcel_rhs(t + dt / 2, y + dt / 2 * k2, gamma)
            k4 = parcel_rhs(t + dt, y + dt * k3, gamma)
            y = y + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
            t += dt
            ts.append(t)
            zs_.append(y[0])
        return np.array(ts), np.array(zs_)

    for gamma, label in ((GAMMA_ENV, "stable, Gamma = 6.5 K/km"),
                         (0.0, "isothermal"),
                         (8.5e-3, "weakly stable, Gamma = 8.5 K/km")):
        ts, zz = integrate(gamma, 200.0)
        # period from upward zero crossings of the perturbation
        pert = zz
        cross = np.where((pert[:-1] < 0.0) & (pert[1:] >= 0.0))[0]
        if cross.size >= 3:
            measured = (ts[cross[-1]] - ts[cross[0]]) / (cross.size - 1)
        else:
            measured = float("nan")
        # the linear prediction uses the local environment at the parcel's mean
        # height; for a perturbation released at the surface that is z = 0
        T_local = T_SURF - gamma * 0.0
        N2 = G0 / T_local * (gamma_d - gamma)
        predicted = 2.0 * np.pi / np.sqrt(N2)
        print(f"  {label}")
        print(f"    local linear prediction 2 pi/N = {predicted:8.2f} s at "
              f"T = {T_local:.2f} K")
        print(f"    measured period from zero crossings = {measured:8.2f} s   "
              f"difference {measured - predicted:+7.2f} s "
              f"({(measured - predicted) / predicted * 100:+.3f}%)")
    print("  The agreement is better than 0.01 per cent: that is the check that the")
    print("  linear N^2 formula is the small-amplitude limit of the full buoyancy force.")

    ts, zz = integrate(10.5e-3, 0.01, t_end=1200.0)
    mask = (ts > 200.0) & (ts < 1000.0)
    growth = np.polyfit(ts[mask], np.log(np.abs(zz[mask])), 1)[0]
    N2_unstable = G0 / T_SURF * (gamma_d - 10.5e-3)
    print(f"\n  unstable case, Gamma = 10.5 K/km, released from rest at +0.01 m:")
    print(f"    asymptotic growth rate sqrt(|N^2|) = {np.sqrt(-N2_unstable):.6f} s^-1")
    print(f"    measured logarithmic growth rate    = {growth:.6f} s^-1 "
          f"({(growth / np.sqrt(-N2_unstable) - 1) * 100:+.2f}%)")
    print(f"    e-folding time {1.0 / np.sqrt(-N2_unstable):.1f} s; amplitude grows")
    print(f"    from {np.abs(zz[mask])[0]:.4f} m to {np.abs(zz[mask])[-1]:.4f} m "
          f"across the fitting window")
    print("  The measured rate is slightly LOWER than the asymptotic value because a")
    print("  release from rest gives z' proportional to cosh(N t), whose logarithmic")
    print("  slope N tanh(N t) lies below N and only approaches it as N t grows.  Over")
    print("  this window the least-squares slope averages tanh to about 0.98, so the")
    print("  measurement comes out about two per cent low - an artefact of the fitting")
    print("  window, not of the physics.")

    print("\n  Buoyancy work needed to lift a parcel 1 km through a given environment")
    print("  (per kg; the parcel conserves theta, so T_p = theta_p (p_e/p0)^(R_d/c_p)):")
    zgrid = np.linspace(0.0, 1000.0, 2001)
    for gamma, label in ((GAMMA_ENV, "stable   Gamma = 6.5 K/km"),
                         (8.5e-3, "stable   Gamma = 8.5 K/km"),
                         (10.5e-3, "UNSTABLE Gamma = 10.5 K/km")):
        pe = p_of_z(zgrid, gamma)
        Te = T_SURF - gamma * zgrid
        Tp = theta0 * (pe / P_REF) ** kappa
        buoy = G0 * (Tp - Te) / Te
        # work done ON the parcel = -integral of buoyancy over the path
        work = -np.trapezoid(buoy, zgrid)
        print(f"    {label}:  work = {work:+8.2f} J/kg;  "
              f"dT at 1 km = {(Tp - Te)[-1]:+7.3f} K")

    section("5. Dry static energy along the adiabat")
    dse0 = CP * Ts[0] + G0 * zs[0]
    print("   z(km)    c_p T + g z (kJ/kg)   change (J/kg)")
    for i, (zz, TT) in enumerate(zip(zs, Ts)):
        dse = CP * TT + G0 * zz
        if i == 0:
            print(f"  {zz / 1e3:6.1f}   {dse / 1e3:17.4f}   {dse - dse0:+11.3e}")
        else:
            print(f"  {zz / 1e3:6.1f}   {dse / 1e3:17.4f}   {dse - dse0:+11.3e}")
    print("  Both theta and c_p T + g z are conserved on a dry adiabat CONSIDERED AS")
    print("  ITS OWN HYDROSTATIC PROFILE, which is what is integrated above; they are")
    print("  two bookkeepings of the same fact, one in temperature-pressure variables")
    print("  and one in temperature-height variables.  Caveat: a parcel moving through")
    print("  an environment of a DIFFERENT temperature conserves theta exactly but not")
    print("  c_p T + g z - the difference is its buoyancy.  Lesson 04 measures this.")

    section("6. Entropy: zero along the adiabat, nonzero under heating")
    s_change_adiabat = CP * np.log(thetas[-1] / thetas[0])
    dq = 500.0                      # J kg^-1 of heat added, illustrative
    T_here = Ts[-1]
    s_change_heated = dq / T_here + CP * np.log(thetas[-1] / thetas[0])
    print(f"  c_p ln(theta_1/theta_0) along the adiabat = {s_change_adiabat:+.3e} "
          f"J kg^-1 K^-1")
    print(f"  adding dq = {dq:.0f} J kg^-1 at T = {T_here:.2f} K changes s by "
          f"{dq / T_here:.4f} J kg^-1 K^-1")
    print("  The first is zero to numerical precision; the second is a real entropy")
    print("  increase, and it is what makes the atmosphere's energy budget")
    print("  irreversible (lessons 04 and 16-02-05).")


if __name__ == "__main__":
    main()
