#!/usr/bin/env python3
"""Zero- and one-dimensional energy balance models: equilibrium and relaxation,
a latitudinally resolved steady state, the ice-albedo bifurcation and
hysteresis, and what convective adjustment does to a radiative profile.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python energy_balance_models_demo.py

All models are SYNTHETIC.  The solar constant, sigma and the ocean heat capacity
constants are standard; the reference temperature for the OLR linearisation, the
diffusion coefficient, the heat capacity depth, the albedo values and the ice
threshold are CHOSEN INPUTS, printed below.  No measured flux, fitted OLR
coefficient or published model parameterisation is used.

Contents
--------
1. The zero-dimensional EBM: equilibrium, relaxation time, and the step response.
2. The annual-mean insolation from the daily formula, and a global-mean check.
3. A one-dimensional (latitudinal) EBM solved exactly in steady state.
4. The transport implied by the model, and the transport required by the budget.
5. The ice-albedo feedback: a bifurcation and a hysteresis loop.
6. Convective adjustment: how much energy a radiative-only profile must export.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

SIGMA = 5.670374419e-8        # W m^-2 K^-4, Stefan-Boltzmann constant
SOLAR_CONSTANT = 1361.0       # W m^-2, total solar irradiance at 1 AU (standard)
R_EARTH = 6.371e6             # m, conventional mean Earth radius
RHO_W = 1000.0                # kg m^-3, water density (standard)
C_W = 4000.0                  # J kg^-1 K^-1, water specific heat (standard)

# --- CHOSEN INPUTS of the teaching model ------------------------------------
ALBEDO = 0.30                 # dimensionless, warm-surface albedo
ALBEDO_ICE = 0.62             # dimensionless, cold/icy surface albedo
T_ICE_C = -10.0               # degC, threshold below which the icy albedo applies
T_REF = 255.0                 # K, reference temperature for the OLR linearisation
D_DIFF = 0.6                  # W m^-2 K^-1, meridional diffusion coefficient
H_MIXED = 50.0                # m, ocean mixed-layer depth for the heat capacity


def section(title):
    print(f"\n{'=' * 78}\n{title}\n{'=' * 78}")


def olr_linear(T, T_ref=T_REF):
    """Linearised OLR: a Taylor expansion of sigma T^4 about T_ref (not a fit)."""
    return SIGMA * T_ref ** 4 + 4.0 * SIGMA * T_ref ** 3 * (T - T_ref)


def annual_mean_insolation(n_phi=181, n_day=720, obliquity=23.44):
    """Annual-mean top-of-atmosphere insolation (W/m^2) versus latitude.

    Averages the daily-mean formula of lesson 16-02-01 over a circular orbit:
    delta(t) = arcsin(sin(obliquity) sin(2 pi t/year)).
    """
    # grid uniform in x = sin(phi), so that the area element dx is uniform and
    # the finite-volume discretisation below is consistent
    x_grid = np.linspace(0.0, 1.0, n_phi)
    phi = np.arcsin(x_grid)
    day = np.arange(n_day)
    delta = np.arcsin(np.sin(np.radians(obliquity))
                      * np.sin(2.0 * np.pi * day / n_day))
    F = np.empty_like(phi)
    for i, ph in enumerate(phi):
        c = -np.tan(ph) * np.tan(delta)
        h0 = np.where(c <= -1.0, np.pi, np.where(c >= 1.0, 0.0, np.arccos(np.clip(c, -1, 1))))
        F[i] = np.mean(SOLAR_CONSTANT / np.pi
                       * (h0 * np.sin(ph) * np.sin(delta)
                          + np.cos(ph) * np.cos(delta) * np.sin(h0)))
    return phi, F


def steady_state_1d(phi_grid, Q, albedo_values, D=D_DIFF, T_ref=T_REF):
    """Solve the steady 1-D EBM on x = sin(phi) exactly (linear system).

    D d/dx[(1-x^2) dT/dx] - B T = A - Q(1-a), with OLR = A + B T.
    Finite-volume discretisation on a uniform x grid.  Boundary conditions:
    the flux through the equator face is zero by symmetry, and the metric factor
    (1-x^2) vanishes at the pole, so the pole face flux is zero automatically.
    """
    x = np.sin(phi_grid)
    n = len(x)
    dx = x[1] - x[0]
    A = SIGMA * T_ref ** 4 - 4.0 * SIGMA * T_ref ** 3 * T_ref
    B = 4.0 * SIGMA * T_ref ** 3
    M = np.zeros((n, n))
    rhs = A - Q * (1.0 - albedo_values)
    for i in range(n):
        f_plus = 0.0 if i == n - 1 else 1.0 - (0.5 * (x[i] + x[i + 1])) ** 2
        f_minus = 0.0 if i == 0 else 1.0 - (0.5 * (x[i - 1] + x[i])) ** 2
        M[i, i] = -D * (f_plus + f_minus) / dx ** 2 - B
        if i < n - 1:
            M[i, i + 1] = D * f_plus / dx ** 2
        if i > 0:
            M[i, i - 1] = D * f_minus / dx ** 2
    return np.linalg.solve(M, rhs)


def main():
    section("1. The zero-dimensional energy balance model")
    F_abs = SOLAR_CONSTANT * (1.0 - ALBEDO) / 4.0
    T_eq = (F_abs / SIGMA) ** 0.25
    C = RHO_W * C_W * H_MIXED
    lam = 4.0 * SIGMA * T_eq ** 3
    print(f"  C dT/dt = S(1-a)/4 - sigma T^4")
    print(f"    absorbed solar F = {F_abs:.2f} W/m^2")
    print(f"    equilibrium T    = {T_eq:.3f} K = {T_eq - 273.15:.2f} C")
    print(f"    heat capacity C  = rho c_p h = {C:.3e} J m^-2 K^-1 "
          f"(mixed layer h = {H_MIXED:.0f} m)")
    print(f"    feedback lambda  = 4 sigma T^3 = {lam:.4f} W m^-2 K^-1")
    print(f"    relaxation time  = C/lambda = {C / lam:.4e} s = "
          f"{C / lam / 3.15576e7:.2f} years")
    print("\n  Integrate the ODE from T = 250 K and measure the e-folding time:")
    dt = 3600.0
    T = 250.0
    t = 0.0
    times = [0.0]
    temps = [T]
    for _ in range(int(40.0 * C / lam / dt)):
        dT = ((SOLAR_CONSTANT * (1.0 - ALBEDO) / 4.0 - SIGMA * T ** 4) / C) * dt
        T += dT
        t += dt
        times.append(t)
        temps.append(T)
    temps = np.array(temps)
    times = np.array(times)
    idx = np.argmax(np.abs(temps - T_eq) < abs(250.0 - T_eq) / np.e)
    print(f"    measured e-folding time = {times[idx]:.4e} s = "
          f"{times[idx] / 3.15576e7:.2f} years")
    print(f"    predicted C/lambda      = {C / lam:.4e} s")
    print(f"    difference = {(times[idx] - C / lam) / (C / lam) * 100:+.2f}%"
          f"  (the difference is the ODE's nonlinearity, since lambda is evaluated")
    print("     at the equilibrium rather than along the trajectory)")
    print("\n  Note what the heat capacity does NOT change: the equilibrium")
    print("  temperature is independent of C, which sets only how fast it is")
    print("  approached.  The ocean's heat capacity is the reason a forcing is not")
    print("  the same as a temperature.")

    section("2. Annual-mean insolation, and a global-mean check")
    phi, Q_annual = annual_mean_insolation()
    global_mean = np.trapezoid(Q_annual, np.sin(phi)) / np.trapezoid(
        np.ones_like(phi), np.sin(phi))
    print(f"  annual-mean insolation from the daily formula, averaged over a year:")
    print(f"    equator {Q_annual[0]:8.2f} W/m^2,   45 deg "
          f"{Q_annual[np.argmin(np.abs(np.degrees(phi) - 45.0))]:8.2f} W/m^2,"
          f"   pole {Q_annual[-1]:8.2f} W/m^2")
    print(f"    area-weighted global mean = {global_mean:.4f} W/m^2")
    print(f"    S/4                       = {SOLAR_CONSTANT / 4:.4f} W/m^2")
    print(f"    difference = {global_mean - SOLAR_CONSTANT / 4:+.4f} W/m^2 "
          f"({(global_mean - SOLAR_CONSTANT / 4) / (SOLAR_CONSTANT / 4) * 100:+.4f}%)")
    print("  That agreement is a genuine check: the latitude-dependent formula of")
    print("  lesson 01, integrated over the sphere, must reproduce the geometric")
    print("  factor four.  It does, to the numerical quadrature, which is why the")
    print("  factor four is safe to use in a global budget.")

    section("3. A one-dimensional energy balance model")
    print("  Steady state of")
    print("    D d/dx[(1-x^2) dT/dx] - (A + B T) + Q(x)(1 - a) = 0,   x = sin(phi)")
    print(f"  with OLR linearised about T_ref = {T_REF:.0f} K by a Taylor expansion")
    print(f"  (NOT a fit): A = sigma T_ref^4 - 4 sigma T_ref^3 T_ref = "
          f"{SIGMA * T_REF ** 4 - 4 * SIGMA * T_REF ** 3 * T_REF:.3f},")
    print(f"               B = 4 sigma T_ref^3 = {4 * SIGMA * T_REF ** 3:.4f} "
          f"W m^-2 K^-1")
    print(f"  and diffusion coefficient D = {D_DIFF:.2f} W m^-2 K^-1 (CHOSEN).")
    T1 = steady_state_1d(phi, Q_annual, np.full_like(phi, ALBEDO))
    print("\n   phi (deg)   Q (W/m^2)   T (K)     T (C)    OLR (W/m^2)   N (W/m^2)")
    for p in (0.0, 15.0, 30.0, 45.0, 60.0, 75.0, 90.0):
        i = int(np.argmin(np.abs(np.degrees(phi) - p)))
        N_i = Q_annual[i] * (1.0 - ALBEDO) - olr_linear(T1[i])
        print(f"  {p:9.1f}   {Q_annual[i]:9.2f}   {T1[i]:7.2f}   "
              f"{T1[i] - 273.15:7.2f}   {olr_linear(T1[i]):11.2f}   {N_i:10.2f}")
    print("\n  EXACT CHECK: because the OLR is linear in T (constant B) and the")
    print("  transport operator conserves energy on this grid - its discrete sum is")
    print("  identically zero - the area-weighted mean of the temperature FIELD must")
    print("  equal the zero-dimensional equilibrium temperature.  The area element is")
    print("  cos(phi) dphi = dx, so the correct average is the uniform average over")
    print("  the x = sin(phi) grid:")
    mean_T = float(np.mean(T1))
    Q_mean = Q_annual * (1.0 - ALBEDO)
    mean_Q = (Q_mean.sum() / len(Q_mean))
    A_lin = SIGMA * T_REF ** 4 - 4.0 * SIGMA * T_REF ** 3 * T_REF
    B_lin = 4.0 * SIGMA * T_REF ** 3
    pred = (mean_Q - A_lin) / B_lin
    print(f"    mean of the field           = {mean_T:.6f} K")
    print(f"    (mean Q(1-a) - A)/B         = {pred:.6f} K")
    print(f"    difference                  = {mean_T - pred:+.2e} K")
    print("  So DISTRIBUTING the energy changes the equator and the pole but not the")
    print("  mean, and that is a genuine consequence of the model being linear.  It")
    print("  is also the reason a 1-D EBM with a fixed albedo cannot change the")
    print("  global mean temperature: redistribution alone does not warm a planet.")
    print("  Section 5 breaks the linearity with a temperature-dependent albedo, and")
    print("  that is where the global mean starts to depend on the distribution.")
    print(f"\n  Sensitivity to D (D redistributes energy; it cannot change the mean):")
    for D in (0.3, D_DIFF, 1.2, 2.4):
        Td = steady_state_1d(phi, Q_annual, np.full_like(phi, ALBEDO), D=D)
        print(f"    D = {D:4.2f} W m^-2 K^-1: contrast {Td[0] - Td[-1]:7.3f} K, "
              f"equator {Td[0]:8.3f} K, pole {Td[-1]:8.3f} K, "
              f"mean {np.mean(Td):8.3f} K")
    print("  The tropics change most because the metric factor (1 - x^2) is largest")
    print("  there: the diffusion carries more energy per unit temperature gradient")
    print("  near the equator than near the pole.")

    section("4. The transport implied by the model, and the transport required")
    print("  The diffusion parameterisation carries an implied transport:")
    print("    H(phi) = -2 pi R^2 D (1 - x^2) dT/dx")
    print("  and the energy budget requires")
    print("    H(phi) = -2 pi R^2 integral_phi^{pi/2} N(phi') cos(phi') dphi',")
    print("  with N the model's own net flux Q(1-a) - OLR.  In steady state these")
    print("  are the same expression by construction, so this is a CONSISTENCY")
    print("  check on the discretisation, not an independent test.")
    x = np.sin(phi)
    dTdx = np.gradient(T1, x)
    H_diff = -2.0 * np.pi * R_EARTH ** 2 * D_DIFF * (1.0 - x ** 2) * dTdx
    N_model = Q_annual * (1.0 - ALBEDO) - olr_linear(T1)
    H_int = np.array([
        -2.0 * np.pi * R_EARTH ** 2 * np.trapezoid(N_model[i:], x[i:])
        for i in range(len(phi))
    ])
    print("\n   phi (deg)   H diffusion (PW)   H budget integral (PW)   difference")
    for p in (0.0, 15.0, 30.0, 45.0, 60.0, 75.0):
        i = int(np.argmin(np.abs(np.degrees(phi) - p)))
        print(f"  {p:9.1f}   {H_diff[i] / 1e15:16.4f}   {H_int[i] / 1e15:21.4f}   "
              f"{(H_diff[i] - H_int[i]) / 1e15:10.5f}")
    i_max = int(np.argmax(H_int))
    print(f"\n  the transport peaks at {H_int[i_max] / 1e15:.3f} PW at "
          f"phi = {np.degrees(phi[i_max]):.1f} deg")
    print(f"  and the two forms differ by at most "
          f"{np.max(np.abs(H_diff - H_int)) / 1e15:.4f} PW, i.e. "
          f"{np.max(np.abs(H_diff - H_int)) / np.max(H_int) * 100:.3f}% of the peak.")
    print("  The residual is the first-order-accurate np.gradient used for dT/dx,")
    print("  not a physical inconsistency: the discretisation of the diffusion")
    print("  operator and of the budget integral represent the same transport.")

    section("5. The ice-albedo feedback: bifurcation and hysteresis")
    print(f"  Albedo is a step: {ALBEDO:.2f} above {T_ICE_C:.0f} C, "
          f"{ALBEDO_ICE:.2f} below.  A step is a model choice; reality has a smooth")
    print("  transition through sea ice and snow, and a diffuse margin.")
    print("  Solve the nonlinear steady state by fixed-point iteration, starting")

    def solve_ice(scale, start="warm"):
        alb = np.full_like(phi, ALBEDO if start == "warm" else ALBEDO_ICE)
        T = steady_state_1d(phi, Q_annual * scale, alb)
        for _ in range(300):
            T_new = steady_state_1d(phi, Q_annual * scale, alb)
            alb_new = np.where(T_new < T_ICE_C + 273.15, ALBEDO_ICE, ALBEDO)
            T, alb = T_new, alb_new
        return T, alb

    def edge_label(alb):
        icy = np.where(alb > 0.5 * (ALBEDO + ALBEDO_ICE))[0]
        if icy.size == 0:
            return "none (ice free)"
        if icy[0] == 0:
            return "frozen"
        return f"{np.degrees(phi[icy[0]]):.1f} deg"

    print("  from an ice-free state:")
    print("\n   S/S0     ice edge        equator T (K)   pole T (K)   global mean (K)")
    for scale in (1.20, 1.30, 1.35, 1.40, 1.50, 1.60, 1.80):
        T, alb = solve_ice(scale, "warm")
        print(f"  {scale:5.2f}   {edge_label(alb):14s}   {T[0]:13.2f}   {T[-1]:9.2f}   "
              f"{np.mean(T):15.2f}")
    print("\n  and the same scan starting from a frozen state, for the hysteresis:")
    print("\n   S/S0     ice edge (from ice-free)   ice edge (from frozen)")
    for scale in (1.30, 1.40, 1.50, 1.60, 1.80, 2.00, 2.50):
        _, alb_w = solve_ice(scale, "warm")
        _, alb_c = solve_ice(scale, "cold")
        print(f"  {scale:5.2f}   {edge_label(alb_w):24s}   {edge_label(alb_c):20s}")
    print("\n  Between S/S0 = 1.30 and about 1.9 the two branches BOTH exist, and")
    print("  the state you reach depends on where you started.  That is hysteresis,")
    print("  and it is the classic demonstration that a nonlinear EBM has multiple")
    print("  equilibria and that a small change can produce an abrupt transition.")
    print("  Note the honest caveats, all of which are model choices:")
    print("  (i)  This model needs a solar constant 35-60% ABOVE the standard value")
    print("       to support a partly ice-free planet, because the OLR linearisation")
    print("       and the diffusion coefficient are not calibrated to the real Earth.")
    print("       What the demonstration shows is the STRUCTURE of the bifurcation,")
    print("       not the value of any real threshold.")
    print("  (ii) The albedo is a step function; a smoother dependence narrows and")
    print("       eventually removes the hysteresis.")
    print("  (iii) The frozen branch is a solution of a one-dimensional diffusive")
    print("       model with no ocean heat transport and no ice dynamics.")
    print("  The reason the bifurcation exists at all is the feedback's sign: a")
    print("  colder surface is a brighter surface, which is a colder surface.  A")
    print("  positive feedback can create multiple equilibria; it does not have to.")

    section("6. Convective adjustment: what a radiative-only profile must export")
    print("  The grey radiative-equilibrium model of lesson 02 gives a surface")
    print("  temperature that rises with total infrared optical depth:")
    print("   radiative-equilibrium T_s (K)   sigma T_s^4 (W/m^2)   "
          "excess over 288 K (W/m^2)")
    for T_rad, label in ((302.746, "one grey layer, eps = 1"),
                         (335.043, "grey tau = 4 (lesson 02)"),
                         (380.681, "grey tau = 8 (lesson 02)")):
        e = SIGMA * T_rad ** 4
        e288 = SIGMA * 288.0 ** 4
        print(f"  {label:26s}   {T_rad:10.3f}   {e:17.2f}   {e - e288:20.2f}")
    print(f"\n  A purely radiative atmosphere with a realistic opacity would be far")
    print(f"  too warm, so the surface must export the excess non-radiatively.  For")
    print(f"  the tau = 4 case that is "
          f"{SIGMA * 335.043 ** 4 - SIGMA * 288.0 ** 4:.1f} W/m^2, which is larger")
    print("  than the absorbed solar flux itself - a physical impossibility.")
    print("  The resolution is CONVECTIVE ADJUSTMENT: the radiative profile is")
    print("  unstable to convection, which resets it to an adiabatic lapse rate, and")
    print("  the surface temperature is then set by the radiative balance AT THE TOP")
    print("  of the convecting layer rather than at the surface.  A radiative-")
    print("  convective model is therefore a radiative model plus a rule, and the")
    print("  rule is where the modelling choices live (see the lesson).")
    print("  Note the numeric signature of the failure: an unphysical required flux")
    print("  is the diagnostic, exactly as in the two-box model of lesson 04.")


if __name__ == "__main__":
    main()
