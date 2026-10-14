#!/usr/bin/env python3
"""GCMs, resolution and parameterisation: a measured demonstration that a
discretised model generates its own diffusion, and that a sub-grid process left
out of the resolved equations must be added back as a closure whose form is a
choice.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gcms_and_parameterisation_demo.py

All models and data in this file are SYNTHETIC teaching models.  Parameters are
chosen for transparency, not fitted to observations.  The only standard
constants used are the gravitational acceleration and the specific heat of dry
air, both stated in the code.

Contents
--------
1. Upwind advection of a tracer at four grid resolutions: the numerical
   diffusion coefficient measured from the growth of the tracer variance, and
   compared with its analytic upwind value.
2. A superadiabatic column and two different convective-adjustment schemes:
   dry static energy conservation, and the structural uncertainty of the closure.
3. Resolution scale versus process scale: what a grid of given spacing resolves.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- standard constants ------------------------------------------------------
GRAVITY_M_S2 = 9.81                # m s^-2, standard gravity
CP_DRY_AIR_J_KG_K = 1004.0         # J kg^-1 K^-1, dry air (standard value)

# --- SYNTHETIC teaching parameters -------------------------------------------
DOMAIN_M = 1.0e6                   # 1000 km periodic channel
WIND_M_S = 10.0                    # uniform advecting wind, m s^-1
COURANT = 0.5                      # u*dt/dx, chosen
INITIAL_WIDTH_M = 8.0e4            # initial Gaussian sigma, 80 km
RUN_TIME_S = 86400.0               # one day
RESOLUTIONS = (64, 128, 256, 512)
COLUMN_HEIGHT_KM = 5.0
COLUMN_LEVELS = 21
INITIAL_LAPSE_K_KM = 10.5          # superadiabatic initial lapse rate
SURFACE_T_K = 300.0


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def gaussian(x, centre, width):
    return np.exp(-0.5 * ((x - centre) / width) ** 2)


def periodic_moments(conc, x):
    """Mean and variance of a concentration profile on a periodic domain.

    The tracer crosses the periodic boundary during the run, so the mean is
    taken as the phase of the first Fourier coefficient and the variance uses
    the shortest (periodic) distance.  A naive first moment would split the
    blob between x = 0 and x = L and report a spuriously large variance.
    """
    dx = x[1] - x[0]
    total = conc.sum() * dx
    z = np.sum(conc * np.exp(2j * np.pi * x / DOMAIN_M)) * dx / total
    mean = (np.arctan2(z.imag, z.real) / (2.0 * np.pi)) * DOMAIN_M % DOMAIN_M
    distance = np.abs((x - mean + 0.5 * DOMAIN_M) % DOMAIN_M - 0.5 * DOMAIN_M)
    return mean, float(np.sum(conc * distance ** 2) * dx / total)


def upwind_advance(n_cells):
    """Advect a Gaussian with the first-order upwind scheme; return K measured."""
    dx = DOMAIN_M / n_cells
    dt = COURANT * dx / WIND_M_S
    n_steps = int(round(RUN_TIME_S / dt))
    x = (np.arange(n_cells) + 0.5) * dx
    c = gaussian(x, 0.30 * DOMAIN_M, INITIAL_WIDTH_M)
    c /= c.sum() * dx
    variance_0 = periodic_moments(c, x)[1]
    for _ in range(n_steps):
        c_new = c.copy()
        c_new[1:] = c[1:] - COURANT * (c[1:] - c[:-1])
        c_new[0] = c[0] - COURANT * (c[0] - c[-1])
        c = c_new
    variance_t = periodic_moments(c, x)[1]
    k_measured = (variance_t - variance_0) / (2.0 * n_steps * dt)
    return dx, dt, n_steps, variance_0, variance_t, k_measured


def dry_static_energy(t_k, z_km):
    return CP_DRY_AIR_J_KG_K * t_k + GRAVITY_M_S2 * z_km * 1.0e3


def temperature_from_s(s, z_km):
    return (s - GRAVITY_M_S2 * z_km * 1.0e3) / CP_DRY_AIR_J_KG_K


def convective_adjust(s, mixing_fraction):
    """Relax adjacent levels toward a common dry static energy where unstable.

    mixing_fraction = 1.0 gives the full adjustment to a neutral profile;
    smaller values only partly remove the instability.  Total dry static energy
    is conserved because each pair replaces two values with a weighted mean.
    """
    s = s.copy()
    for _ in range(200):
        unstable = False
        for i in range(len(s) - 1):
            if s[i] > s[i + 1] + 1e-9:
                unstable = True
                mean = 0.5 * (s[i] + s[i + 1])
                s[i] += mixing_fraction * (mean - s[i])
                s[i + 1] += mixing_fraction * (mean - s[i + 1])
        if not unstable:
            break
    return s


def main():
    gamma_d = GRAVITY_M_S2 / CP_DRY_AIR_J_KG_K * 1000.0
    section("1. Grid resolution sets the numerical diffusion (upwind advection)")
    print(f"  domain = {DOMAIN_M / 1.0e3:.0f} km, wind u = {WIND_M_S:.1f} m/s, "
          f"Courant number c = u dt/dx = {COURANT:.2f}")
    print(f"  initial Gaussian sigma = {INITIAL_WIDTH_M / 1.0e3:.0f} km, "
          f"run time = {RUN_TIME_S / 3600.0:.0f} h")
    print("  analytic upwind diffusion  K_num = 0.5 u dx (1 - c)")
    print(f"  {'N':>5s} {'dx (km)':>9s} {'steps':>7s} "
          f"{'var0 (km^2)':>12s} {'variance (km^2)':>16s} "
          f"{'K analytic':>12s} {'K measured':>12s} {'ratio':>7s}")
    k_analytic_all = []
    k_measured_all = []
    for n in RESOLUTIONS:
        dx, dt, n_steps, v0, vt, k_meas = upwind_advance(n)
        k_ana = 0.5 * WIND_M_S * dx * (1.0 - COURANT)
        k_analytic_all.append(k_ana)
        k_measured_all.append(k_meas)
        print(f"  {n:5d} {dx / 1.0e3:9.3f} {n_steps:7d} "
              f"{v0 / 1.0e6:12.4f} {vt / 1.0e6:16.4f} "
              f"{k_ana:12.1f} {k_meas:12.1f} {k_meas / k_ana:7.3f}")
    print(f"  K_num is proportional to dx: halving dx halves the numerical "
          f"diffusion.")
    print(f"  measured ratio K(128)/K(512) = "
          f"{k_measured_all[1] / k_measured_all[3]:.2f} (a factor of 4 expected)")
    print("  Unit check: [u dx] = (m/s)(m) = m^2/s, the unit of a diffusivity.")

    section("2a. A superadiabatic column and its convective adjustment")
    z = np.linspace(0.0, COLUMN_HEIGHT_KM, COLUMN_LEVELS)
    dz = z[1] - z[0]
    t_initial = SURFACE_T_K - INITIAL_LAPSE_K_KM * z
    s_initial = dry_static_energy(t_initial, z)
    print(f"  column {COLUMN_HEIGHT_KM:.1f} km, {COLUMN_LEVELS} levels, dz = "
          f"{dz * 1e3:.0f} m")
    print(f"  dry adiabatic lapse rate gamma_d = g/cp = {gamma_d:.2f} K/km")
    print(f"  initial lapse rate              = {INITIAL_LAPSE_K_KM:.2f} K/km "
          f"(superadiabatic: unstable)")
    print(f"  initial surface T = {t_initial[0]:.2f} K, top T = {t_initial[-1]:.2f} K")

    s_full = convective_adjust(s_initial, 1.0)
    s_half = convective_adjust(s_initial, 0.5)
    t_full = temperature_from_s(s_full, z)
    t_half = temperature_from_s(s_half, z)
    print(f"  total dry static energy conserved to "
          f"{abs(s_full.sum() - s_initial.sum()) / abs(s_initial.sum()):.2e} "
          f"(relative), same for the partial scheme")

    def lapse_of(t_profile):
        return -(t_profile[1:] - t_profile[:-1]).mean() / dz

    print(f"  {'scheme':<26s} {'surface T (K)':>14s} {'top T (K)':>11s} "
          f"{'lapse (K/km)':>13s}")
    print(f"  {'unadjusted (no closure)':<26s} {t_initial[0]:14.2f} "
          f"{t_initial[-1]:11.2f} {INITIAL_LAPSE_K_KM:13.2f}")
    print(f"  {'full adjustment':<26s} {t_full[0]:14.2f} {t_full[-1]:11.2f} "
          f"{lapse_of(t_full):13.2f}")
    print(f"  {'half adjustment':<26s} {t_half[0]:14.2f} {t_half[-1]:11.2f} "
          f"{lapse_of(t_half):13.2f}")
    print("  Both adjustment schemes conserve energy and remove the instability;")
    print("  they disagree on the final surface temperature by "
          f"{t_half[0] - t_full[0]:+.2f} K. That difference is structural")
    print("  uncertainty of the parameterisation, not a numerical error.")

    section("2b. Parameterisation is a closure, not a measurement")
    print("  A convective plume is of order 1 km across. A climate model with a")
    print(f"  100 km horizontal grid cannot resolve it: the grid resolves features")
    print("  larger than a few grid spacings, so the plume is entirely sub-grid.")
    print("  The adjustment above is a closure. Its threshold, its mixing")
    print("  fraction and its timescale are choices; the energy budget constrains")
    print("  the column, not the closure. Two energy-conserving closures give")
    print("  different surface temperatures, which is why parameterised processes")
    print("  are a leading source of inter-model spread.")

    section("3. Resolution versus process scale")
    print(f"  effective resolution (features larger than ~4 grid spacings):")
    for dx_km in (100.0, 25.0, 10.0, 1.0):
        print(f"    grid {dx_km:6.1f} km -> resolved scales > {4 * dx_km:7.1f} km")
    print("  Convective plumes (~1 km), clouds (~0.1-10 km), boundary-layer")
    print("  turbulence (<1 km) and gravity waves (<10 km) are sub-grid at every")
    print("  climate-model resolution in routine use, so all are parameterised.")
    print("  Increasing resolution shrinks the parameterised part; it does not")
    print("  remove it.")


if __name__ == "__main__":
    main()
