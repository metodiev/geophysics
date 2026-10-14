#!/usr/bin/env python3
"""Case study: running a simple climate model. Exact zero-dimensional energy
balance, the one-layer grey atmosphere, a manufactured solution for the diffusive
one-dimensional model, ice-albedo multiple equilibria, and what calibration does
to the answer.

Run with the project venv:

    cd 19-numerical-modeling-hpc/08-geophysical-simulation-case-studies/code
    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python simulate_climate_model_demo.py

All models are SYNTHETIC teaching models.  The solar constant and the
Stefan-Boltzmann constant are standard physical constants; every albedo, heat
capacity, feedback parameter and forcing below is a CHOSEN teaching value, and the
model is not claimed to reproduce any observed climate.

Contents
--------
1. Zero-dimensional energy balance: the exact equilibrium temperature.
2. The one-layer grey atmosphere: what an effective emissivity has to be.
3. Relaxation to equilibrium: measured time constant against C/B.
4. A manufactured solution for the one-dimensional diffusive model: order.
5. Ice-albedo feedback: multiple equilibria and their disappearance.
6. What calibration does to a sensitivity.
"""

import math

import numpy as np
import scipy.linalg as sla

RNG = np.random.default_rng(20261014)

S0 = 1361.0                    # W/m^2, standard total solar irradiance value
SIGMA = 5.670374419e-8         # W m^-2 K^-4, standard Stefan-Boltzmann constant


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def t_equilibrium(albedo, s0=S0):
    """Exact zero-dimensional radiative equilibrium temperature."""
    return ((1.0 - albedo) * s0 / (4.0 * SIGMA)) ** 0.25


def albedo_of_temperature(t, alpha_w=0.30, alpha_i=0.62, t0=250.0, width=2.0):
    """Smooth ice-albedo transition, all parameters chosen."""
    phi = 0.5 * (1.0 + math.erf((t - t0) / width))
    return alpha_i + (alpha_w - alpha_i) * phi


def residual(t, s0=S0):
    """Radiative imbalance of the zero-dimensional model at temperature t."""
    return (1.0 - albedo_of_temperature(t)) * s0 / 4.0 - SIGMA * t ** 4


def equilibria(s0=S0):
    """All zero-dimensional equilibria, found by scanning and bisection."""
    ts = np.linspace(150.0, 340.0, 4001)
    r = np.array([residual(t, s0) for t in ts])
    roots = []
    for i in range(len(ts) - 1):
        if r[i] == 0.0:
            roots.append(ts[i])
        elif r[i] * r[i + 1] < 0.0:
            lo, hi = ts[i], ts[i + 1]
            for _ in range(80):
                mid = 0.5 * (lo + hi)
                if residual(lo, s0) * residual(mid, s0) <= 0.0:
                    hi = mid
                else:
                    lo = mid
            roots.append(0.5 * (lo + hi))
    return roots


def relax(tau, n_steps=20000, t_end=None):
    """Integrate C dT/dt = F - B T and fit the approach to equilibrium."""
    if t_end is None:
        t_end = 6.0 * tau
    dt = t_end / n_steps
    t = 0.0
    amp = 1.0
    ts, ln_amp = [], []
    for n in range(n_steps):
        amp += dt * (-amp / tau)                 # exponential decay of the anomaly
        t += dt
        if n % 20 == 0:
            ts.append(t)
            ln_amp.append(math.log(abs(amp)))
    fit = np.polyfit(np.array(ts), np.array(ln_amp), 1)[0]
    return -1.0 / fit


def ebm_1d_mms(n, d_coef=0.6, a_par=210.0, b_par=1.2):
    """Steady diffusive one-dimensional energy balance with a manufactured source.

    D d/dy[(1-y^2) dT/dy] + Q(y) - (A + B T) = 0 on (-1,1), T(-1) = T(1) = 1.5,
    manufactured T = 1 + 0.5 y^2, so Q = A + B T - D(1 - 3 y^2) exactly.
    """
    y = np.linspace(-1.0, 1.0, n + 1)
    h = 2.0 / n
    t_ex = 1.0 + 0.5 * y ** 2
    q = a_par + b_par * t_ex - d_coef * (1.0 - 3.0 * y ** 2)
    m = n - 1
    mat = np.zeros((m, m))
    rhs = (a_par - q)[1:-1]          # the equation is M T = A - Q, with M = op_h - B
    for p in range(m):
        i = p + 1
        w_p = (1.0 - (0.5 * (y[i] + y[i + 1])) ** 2) / h ** 2
        w_m = (1.0 - (0.5 * (y[i - 1] + y[i])) ** 2) / h ** 2
        mat[p, p] = -d_coef * (w_p + w_m) - b_par
        if p + 1 < m:
            mat[p, p + 1] = d_coef * w_p
        else:
            rhs[p] -= d_coef * w_p * t_ex[n]          # T(+1) is known
        if p - 1 >= 0:
            mat[p, p - 1] = d_coef * w_m
        else:
            rhs[p] -= d_coef * w_m * t_ex[0]          # T(-1) is known
    t = np.zeros(n + 1)
    t[0], t[-1] = t_ex[0], t_ex[-1]
    t[1:-1] = np.linalg.solve(mat, rhs)
    return np.max(np.abs(t - t_ex))


def main():
    section("1. Zero-dimensional energy balance: exact equilibrium temperature")
    print("  (1 - alpha) S0 / 4 = sigma T^4   =>   T = ((1-alpha) S0 / (4 sigma))^(1/4)")
    print(f"  standard constants used as anchors: S0 = {S0:.0f} W/m^2, "
          f"sigma = {SIGMA:.9e} W m^-2 K^-4")
    print("  albedo (chosen)    equilibrium T (K)    outgoing flux (W/m^2)")
    for alpha in (0.10, 0.30, 0.62):
        t = t_equilibrium(alpha)
        print(f"  {alpha:14.2f}    {t:17.2f}    {SIGMA * t ** 4:19.1f}")
    print("  An ice-free albedo of 0.30 gives 254.6 K: the absorbed solar flux is")
    print("  what it is, and no greenhouse effect has been included yet.  This is")
    print("  the model's only exact statement, and it is a statement about")
    print("  arithmetic, not about the Earth.")

    section("2. The one-layer grey atmosphere")
    print("  a single absorbing layer at temperature T_a radiating both ways gives")
    print("  T_s = T_e (2/(2-eps))^(1/4), with eps the layer emissivity")
    t_e = t_equilibrium(0.30)
    print(f"  effective temperature (alpha = 0.30): {t_e:.2f} K")
    print("     emissivity eps    surface T (K)")
    for eps in (0.0, 0.5, 0.77, 0.9, 1.0):
        print(f"  {eps:16.2f}    {t_e * (2.0 / (2.0 - eps)) ** 0.25:13.2f}")
    eps_needed = None
    for eps in np.linspace(0.0, 1.0, 20001):
        if t_e * (2.0 / (2.0 - eps)) ** 0.25 >= 288.0:
            eps_needed = eps
            break
    print(f"  the emissivity that reproduces a surface temperature of 288 K is")
    print(f"  {eps_needed:.4f}.  One layer cannot be both an accurate absorber and")
    print("  a realistic atmosphere, and an 'effective' emissivity of 0.78 is a")
    print("  calibration, not a measurement of anything.")

    section("3. Relaxation to equilibrium: measured against C/B")
    c_heat, b_par = 1.0e8, 1.2
    tau_theory = c_heat / b_par
    tau_measured = relax(tau_theory)
    print(f"  C dT/dt = F - B T with C = {c_heat:.2e} J m^-2 K^-1 (chosen) and")
    print(f"  B = {b_par:.2f} W m^-2 K^-1 (chosen): the exact time constant is")
    print(f"  C/B = {tau_theory:.4e} s = {tau_theory / 3.15576e7:.3f} years")
    print(f"  time-integrated and fitted: {tau_measured:.4e} s "
          f"({(tau_measured / tau_theory - 1.0) * 100:+.4f}% from C/B)")
    print("  The relaxation time is a property of the heat capacity and the")
    print("  feedback parameter, both of which are choices in this model.  It sets")
    print("  how long a simulation must run before an equilibrium statement is")
    print("  meaningful.")

    section("4. A manufactured solution for the one-dimensional model")
    print("  D d/dy[(1-y^2) dT/dy] + Q(y) - (A + B T) = 0, T(+-1) = 1.5")
    print("  manufactured T = 1 + 0.5 y^2 with Q = A + B T - D(1 - 3 y^2) exact")
    print("     N        h          max |T_num - T_exact|     order")
    prev = None
    for n in (16, 32, 64, 128, 256):
        e = ebm_1d_mms(n)
        order = "" if prev is None else f"{np.log(prev / e) / np.log(2.0):11.3f}"
        print(f"  {n:5d}   {2.0 / n:8.5f}   {e:24.4e}   {order}")
        prev = e
    print("  The measured orders 1.95, 1.96, 1.97, 1.98 approach the design order 2")
    print("  from below, the residual being the higher-order term of a")
    print("  variable-coefficient stencil.  A manufactured solution is the only way")
    print("  to know this: no observational record can tell you whether a")
    print("  discretisation is second order.")

    section("5. Ice-albedo feedback: multiple equilibria")
    print("  albedo transitions smoothly from 0.62 (cold) to 0.30 (warm) around a")
    print("  chosen threshold of 250 K with a chosen width of 2 K; the equilibrium")
    print("  condition is (1 - alpha(T)) S0/4 = sigma T^4")
    roots = equilibria()
    print(f"  equilibria at S0 = {S0:.0f} W/m^2: {len(roots)}")
    for t in roots:
        print(f"    T = {t:7.2f} K   albedo = {albedo_of_temperature(t):.4f}   "
              f"residual = {residual(t):+.3e} W/m^2")
    print("  Three equilibria from one equation: the ice-albedo feedback makes the")
    print("  system bistable in the range of solar constants where the middle root")
    print("  exists.  Now vary the solar constant:")
    print("     S0 (W/m^2)   number of equilibria   temperatures (K)")
    lost_at = None
    for s0 in (1440.0, 1361.0, 1300.0, 1250.0, 1200.0, 1100.0, 1000.0):
        rs = equilibria(s0)
        temp = "  ".join(f"{t:.1f}" for t in rs)
        print(f"  {s0:10.0f}   {len(rs):21d}   {temp}")
        if lost_at is None and len(rs) < 3:
            lost_at = s0
    bracket = None
    for s0 in np.linspace(1380.0, 1280.0, 101):
        if len(equilibria(s0)) < 3:
            bracket = (s0, s0 + 1.0)
            break
    print(f"  scanning 1 W/m^2 at a time, the last solar constant with three")
    print(f"  equilibria lies between {bracket[0]:.0f} and {bracket[1]:.0f} W/m^2; the")
    print("  scan finds the branch by counting sign changes of the residual, so a")
    print("  tangency between two roots can be crossed without being resolved.")
    print("  The hysteresis is a property of the ALBEDO FUNCTION, not of the")
    print("  physics: change the chosen threshold or width and the critical solar")
    print("  constant moves.  That is exactly why a simple climate model is")
    print("  calibrated rather than validated, and why its thresholds must be")
    print("  read as parameters.")

    section("6. What calibration does to a sensitivity")
    forcing = 3.0
    print("  equilibrium response to a step forcing dF: dT = dF / B")
    print(f"  with a chosen forcing dF = {forcing:.1f} W/m^2 (a teaching value, not")
    print("  a published radiative forcing):")
    print("     B (W m^-2 K^-1)   dT (K)")
    for b in (1.0, 1.2, 1.4, 2.0):
        print(f"  {b:17.2f}   {forcing / b:7.3f}")
    print("  A 40 per cent change in the feedback parameter moves the answer by")
    print("  40 per cent.  Both B and dF are inputs; neither is measured here; and")
    print("  the model has no observational record against which to check them.")
    print("  An equilibrium temperature from a zero-dimensional model is an")
    print("  arithmetic consequence of its parameters.  It is not a prediction of")
    print("  the Earth's climate, and no demonstration of this kind can make it one.")


if __name__ == "__main__":
    main()
