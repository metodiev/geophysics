#!/usr/bin/env python3
"""Thermal methods in the shallow subsurface: the periodic temperature wave, its
damping depth, the amplitude-ratio and phase-lag estimates of thermal diffusivity,
the needle-probe (line source) solution and its validity window, and the
sensitivity of conductivity to water content.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python thermal_nearsurface_demo.py

Everything here is SYNTHETIC.  The thermal properties, water contents and depths
are chosen teaching values, not measurements and not site parameters.

Contents
--------
1. Thermal diffusivity kappa = k/(rho c) for teaching materials.
2. The periodic solution T(z,t) = Tbar + A exp(-z/mu) cos(omega t - z/mu) with
   mu = sqrt(2 kappa/omega), verified against a finite-difference solution.
3. Two ways to measure kappa from field temperatures (amplitude ratio, phase lag),
   and a Monte Carlo propagation of a 0.1 K temperature error.
4. The needle probe: the exact line-source solution in terms of E1, the late-time
   logarithmic approximation, and the time after which it is good to 1%.
5. Sensitivity of thermal conductivity to volumetric water content.
"""

import numpy as np
from scipy.special import exp1

RNG = np.random.default_rng(20261014)

DAY = 86400.0          # s
YEAR = 365.25 * DAY    # s
GAMMA = 0.5772156649015329   # Euler-Mascheroni constant, exact

MATERIALS = {
    "dry soil":      dict(k=0.30, rho=1500.0, c=800.0),
    "moist soil":    dict(k=1.20, rho=1600.0, c=1000.0),
    "saturated soil": dict(k=2.00, rho=1800.0, c=1400.0),
    "granite":       dict(k=2.50, rho=2650.0, c=790.0),
}


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def diffusivity(k_w_mk, rho, c):
    """Thermal diffusivity kappa = k/(rho c) in m^2/s."""
    return k_w_mk / (rho * c)


def damping_depth(kappa, period_s):
    """Depth over which a periodic temperature wave falls by 1/e, in metres."""
    return np.sqrt(2.0 * kappa * period_s / (2.0 * np.pi))


def main():
    section("1. Thermal properties and diffusivity (SYNTHETIC teaching values)")
    print("  material           k (W/m/K)  rho (kg/m3)  c (J/kg/K)  kappa (m^2/s)")
    kappas = {}
    for name, p in MATERIALS.items():
        kappa = diffusivity(p["k"], p["rho"], p["c"])
        kappas[name] = kappa
        print(f"  {name:16s} {p['k']:10.2f} {p['rho']:11.0f} {p['c']:11.0f} "
              f"{kappa:12.3e}")
    print("\n  Damping depth mu = sqrt(2 kappa / omega):")
    print("  material           mu, daily (m)   mu, annual (m)")
    for name, kappa in kappas.items():
        print(f"  {name:16s} {damping_depth(kappa, DAY):15.3f} "
              f"{damping_depth(kappa, YEAR):15.3f}")

    section("2. The periodic solution verified against a finite-difference model")
    kappa = kappas["moist soil"]
    period = DAY
    omega = 2.0 * np.pi / period
    mu = damping_depth(kappa, period)
    amp = 8.0          # K, surface amplitude (teaching value)
    t_mean = 12.0      # deg C
    print(f"  teaching case: moist soil, kappa = {kappa:.3e} m^2/s, period = 1 day,")
    print(f"  surface amplitude A = {amp:.1f} K, mean temperature {t_mean:.1f} C,")
    print(f"  damping depth mu = {mu:.4f} m")

    nz = 401
    z = np.linspace(0.0, 8.0 * mu, nz)
    dz = z[1] - z[0]
    dt = 0.4 * dz ** 2 / kappa
    nt = int(np.ceil(6.0 * period / dt))
    print(f"  finite-difference grid: {nz} nodes to {z[-1]:.3f} m, dz = {dz:.4f} m,")
    print(f"  dt = {dt:.1f} s, {nt} steps = {nt * dt / period:.2f} periods")
    temp = np.full(nz, t_mean)
    for n in range(nt):
        t_new = temp.copy()
        t_new[0] = t_mean + amp * np.cos(omega * (n + 1) * dt)
        t_new[1:-1] = temp[1:-1] + kappa * dt / dz ** 2 * (
            temp[2:] - 2.0 * temp[1:-1] + temp[:-2])
        t_new[-1] = t_mean
        temp = t_new
    t_now = nt * dt
    analytic = t_mean + amp * np.exp(-z / mu) * np.cos(omega * t_now - z / mu)
    err = np.max(np.abs(temp - analytic))
    print(f"  after {t_now / period:.2f} periods: max |FD - analytic| = {err:.4f} K "
          f"({err / amp * 100:.3f}% of A)")
    print(f"  RMS |FD - analytic| = {np.sqrt(np.mean((temp - analytic) ** 2)):.4f} K")
    print("  the residual is the transient that has not yet decayed plus the small")
    print("  Dirichlet error at the base, where the analytic amplitude is "
          f"{amp * np.exp(-8):.4f} K.")

    section("3. Measuring kappa from temperatures at two depths")
    z1, z2 = 0.05, 0.30
    A1 = amp * np.exp(-z1 / mu)
    A2 = amp * np.exp(-z2 / mu)
    phi1 = -z1 / mu
    phi2 = -z2 / mu
    print(f"  probe depths z1 = {z1:.2f} m, z2 = {z2:.2f} m; true kappa = {kappa:.4e}")
    print(f"    amplitude at z1 = {A1:.4f} K, at z2 = {A2:.4f} K")
    print(f"    phase lag at z1 = {abs(phi1):.4f} rad, at z2 = {abs(phi2):.4f} rad;")
    print(f"    the lag between the depths is {abs(phi2 - phi1):.4f} rad = "
          f"{abs(phi2 - phi1) / omega / 3600:.3f} h")
    d_ln_A = np.log(A1 / A2)
    d_phi = abs(phi2 - phi1)
    kappa_amp = omega * (z2 - z1) ** 2 / (2.0 * d_ln_A ** 2)
    kappa_ph = omega * (z2 - z1) ** 2 / (2.0 * d_phi ** 2)
    print(f"  from the amplitude ratio: kappa = {kappa_amp:.4e} m^2/s "
          f"({(kappa_amp / kappa - 1) * 100:+.4f}%)")
    print(f"  from the phase lag     : kappa = {kappa_ph:.4e} m^2/s "
          f"({(kappa_ph / kappa - 1) * 100:+.4f}%)")

    sigma_T = 0.05      # K, one-sigma temperature error (teaching value)
    n_mc = 20000
    A1n = np.abs(A1 + sigma_T * RNG.standard_normal(n_mc))
    A2n = np.abs(A2 + sigma_T * RNG.standard_normal(n_mc))
    ph1n = phi1 + (sigma_T / A1) * RNG.standard_normal(n_mc)
    ph2n = phi2 + (sigma_T / A2) * RNG.standard_normal(n_mc)
    k_amp = omega * (z2 - z1) ** 2 / (2.0 * np.log(A1n / A2n) ** 2)
    k_ph = omega * (z2 - z1) ** 2 / (2.0 * (ph2n - ph1n) ** 2)
    k_amp = k_amp[np.isfinite(k_amp)]
    k_ph = k_ph[np.isfinite(k_ph)]
    print(f"\n  Monte Carlo with a {sigma_T:.2f} K one-sigma temperature error "
          f"({n_mc} trials):")
    print(f"    amplitude-ratio kappa: {np.mean(k_amp):.4e} +/- {np.std(k_amp):.4e} "
          f"({np.std(k_amp) / np.mean(k_amp) * 100:.2f}% one-sigma)")
    print(f"    phase-lag kappa      : {np.mean(k_ph):.4e} +/- {np.std(k_ph):.4e} "
          f"({np.std(k_ph) / np.mean(k_ph) * 100:.2f}% one-sigma)")
    print("  Both estimators amplify a temperature error into a diffusivity error of")
    print("  roughly twice the fractional error of the amplitude or the phase.")

    section("4. The needle probe: line source and its late-time approximation")
    q = 1.0            # W/m, heat input per unit length (teaching value)
    k_probe = MATERIALS["moist soil"]["k"]
    r_probe = 0.0015   # m, distance from the line source (teaching value)
    print(f"  q = {q:.2f} W/m, k = {k_probe:.2f} W/m/K, r = {r_probe * 1e3:.2f} mm")
    print("    t (s)     exact T rise (K)   approximation (K)   relative error")
    for t in (1.0, 2.0, 5.0, 10.0, 20.0, 50.0, 100.0, 200.0):
        exact = q / (4.0 * np.pi * k_probe) * exp1(r_probe ** 2 / (4.0 * kappa * t))
        approx = q / (4.0 * np.pi * k_probe) * (
            np.log(4.0 * kappa * t / r_probe ** 2) - GAMMA)
        print(f"  {t:8.1f}   {exact:15.6f}   {approx:17.6f}   "
              f"{abs(approx - exact) / exact * 100:12.4f}%")
    def rel_err(t):
        exact = q / (4.0 * np.pi * k_probe) * exp1(r_probe ** 2 / (4.0 * kappa * t))
        approx = q / (4.0 * np.pi * k_probe) * (
            np.log(4.0 * kappa * t / r_probe ** 2) - GAMMA)
        return abs(approx - exact) / exact - 0.01

    from scipy.optimize import brentq
    t_valid = brentq(rel_err, 1.0, 200.0, xtol=1e-6)
    print(f"  the approximation crosses 1% at t = {t_valid:.2f} s, where "
          f"r^2/(4 kappa t) = {r_probe ** 2 / (4.0 * kappa * t_valid):.4f}.")
    print("  A probe fitted over the first second is fitting the wrong function; the")
    print("  measurement window must start well after the contact resistance settles.")

    section("5. Sensitivity of conductivity to water content")
    ks, kw, ka = 3.0, 0.60, 0.025       # W/m/K, teaching values
    phi = 0.45                          # porosity (teaching value)
    print(f"  geometric-mean mixing model: k = ks^(1-phi) kw^theta ka^(phi-theta)")
    print(f"  ks = {ks} W/m/K, kw = {kw}, ka = {ka}, porosity phi = {phi}")
    print("    theta (v/v)   k (W/m/K)   dk/dtheta (W/m/K per unit theta)")
    prev = None
    for theta in (0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35):
        k_eff = ks ** (1 - phi) * kw ** theta * ka ** (phi - theta)
        if prev is None:
            slope = (ks ** (1 - phi) * kw ** 0.06 * ka ** (phi - 0.06)
                     - k_eff) / 0.01
        else:
            slope = (k_eff - prev[1]) / (theta - prev[0])
        print(f"    {theta:11.2f}   {k_eff:9.3f}   {slope:27.3f}")
        prev = (theta, k_eff)
    k1 = ks ** (1 - phi) * kw ** 0.20 * ka ** (phi - 0.20)
    k2 = ks ** (1 - phi) * kw ** 0.25 * ka ** (phi - 0.25)
    print(f"  a change of 0.05 in volumetric water content changes k by "
          f"{(k2 - k1) / k1 * 100:.1f}% ({k1:.3f} -> {k2:.3f} W/m/K):")
    print("  that is the signal a thermal survey measures, and it is also why the")
    print("  method must know the mineral conductivity and the porosity to separate")
    print("  water content from material change.")

    section("6. Summary")
    print("  The shallow thermal field is a diffusion problem: periodic surface forcing")
    print("  penetrates one damping depth mu = sqrt(2 kappa/omega), which is decimetres")
    print("  for the daily cycle and metres for the annual one.  Both the attenuation")
    print("  and the phase lag measure kappa, and the needle probe measures the")
    print("  conductivity through the same diffusion equation, provided the measurement")
    print("  is taken late enough for the logarithmic approximation to hold.")


if __name__ == "__main__":
    main()
