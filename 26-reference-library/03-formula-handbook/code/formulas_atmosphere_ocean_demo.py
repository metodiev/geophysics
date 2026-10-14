"""Check the atmosphere, radiation and ocean formula sheet.

Print-only, seeded, no plots, no file I/O. Numbers quoted in
26-03-07-formulas-atmosphere-ocean.md come from this output.

Run with:  .venv/bin/python 26-reference-library/03-formula-handbook/code/formulas_atmosphere_ocean_demo.py
"""

from __future__ import annotations

import math

import numpy as np
from scipy.constants import G, R, Stefan_Boltzmann as SIGMA_SB, g as G_STD, h as H_PLANCK

SEED = 20261014
R_DRY = 287.05      # J kg^-1 K^-1, specific gas constant for dry air (nominal)
CP_DRY = 1005.0     # J kg^-1 K^-1, specific heat of dry air at constant pressure
OMEGA_EARTH = 7.292115e-5   # rad/s, nominal Earth rotation rate
WIEN_B = 2.897771955e-3     # m K, Wien displacement constant


def banner(n: int, title: str) -> None:
    print(f"\n[{n}] {title}")


def main() -> None:
    rng = np.random.default_rng(SEED)
    print("Atmosphere, radiation and ocean formula sheet -- numerical checks")
    print(f"numpy {np.__version__}, seeded rng = default_rng({SEED})")
    print(f"R = {R:.4f} J mol^-1 K^-1, sigma = {SIGMA_SB:.6e} W m^-2 K^-4")
    print("PROVENANCE: SYNTHETIC -- the atmospheric states below are chosen, not observed.")

    banner(1, "Thermodynamics of dry air")
    temp_k, press_hpa, press0_hpa = 288.15, 850.0, 1000.0
    theta = temp_k * (press0_hpa / press_hpa) ** (R_DRY / CP_DRY)
    rho_air = press_hpa * 100.0 / (R_DRY * temp_k)
    gamma_d = G_STD / CP_DRY
    print(f"  T = {temp_k:.2f} K, p = {press_hpa:.0f} hPa, p0 = {press0_hpa:.0f} hPa")
    print(f"  R/cp exponent                    = {R_DRY / CP_DRY:.6f}")
    print(f"  potential temperature theta      = {theta:.4f} K")
    print(f"  density from ideal gas rho = p/(R T) = {rho_air:.6f} kg/m^3")
    print(f"  dry adiabatic lapse rate g/cp    = {gamma_d:.6e} K/m = {gamma_d * 1000:.4f} K/km")

    banner(2, "Rotation, Coriolis parameter and Rossby radius")
    for lat in (0.0, 45.0, 60.0):
        f_cor = 2.0 * OMEGA_EARTH * math.sin(math.radians(lat))
        print(f"  latitude {lat:5.1f} deg: f = {f_cor:+.6e} s^-1")
    f45 = 2.0 * OMEGA_EARTH * math.sin(math.radians(45.0))
    depth_scale = 1000.0
    rossby = math.sqrt(G_STD * depth_scale) / f45
    print(f"  internal Rossby radius, H = {depth_scale:.0f} m -> {rossby / 1000.0:.3f} km")

    banner(3, "Geostrophic balance: wind and current speed")
    press_grad = 1.0e-3          # Pa/m, i.e. 100 Pa per 100 km
    rho_ref = 1.225
    u_geo = press_grad / (rho_ref * f45)
    print(f"  pressure gradient = {press_grad:.1e} Pa/m, rho = {rho_ref:.3f} kg/m^3")
    print(f"  geostrophic wind speed = {u_geo:.4f} m/s = {u_geo * 3.6:.3f} km/h")
    ssh_grad, g_acc = 1.0e-6, 9.81
    u_current = -g_acc / f45 * ssh_grad
    print(f"  sea-surface slope {ssh_grad:.1e} (1 mm per km) -> geostrophic current = {u_current:+.6f} m/s")
    kv_eddy = 0.01
    print(f"  Ekman depth sqrt(2*Kv/f) with Kv = {kv_eddy:.2f} m^2/s = {math.sqrt(2.0 * kv_eddy / f45):.4f} m")

    banner(4, "Radiation: Wien displacement and Stefan-Boltzmann flux")
    t_sun = 5772.0
    lambda_max = WIEN_B / t_sun
    flux = SIGMA_SB * t_sun**4
    print(f"  T = {t_sun:.0f} K: lambda_max = b/T = {lambda_max * 1e9:.4f} nm")
    print(f"  blackbody exitance sigma*T^4     = {flux:.6e} W/m^2")
    r_sun, d_earth = 6.957e8, 1.495979e11
    solar_const = flux * (r_sun / d_earth) ** 2
    print(f"  flux at Earth = F*(R_sun/d)^2    = {solar_const:.4f} W/m^2")
    print(f"  photon energy at 500 nm: E = hc/lambda = {H_PLANCK * 299792458.0 / 500e-9:.6e} J")

    banner(5, "Atmospheric attenuation and optical depth")
    k_ext, path = 0.02, 1500.0
    tau = k_ext * path
    transmit = math.exp(-tau)
    print(f"  extinction coefficient = {k_ext:.3f} m^-1, path = {path:.0f} m")
    print(f"  optical depth tau = {tau:.4f}, transmittance = {transmit:.6e}")
    print(f"  tau = 1 occurs at a path of {1.0 / k_ext:.1f} m")

    banner(6, "Sea-water properties and sound speed (simplified)")
    salinity, temp_c, depth_m = 35.0, 10.0, 1000.0
    sound = 1449.2 + 4.6 * temp_c - 0.055 * temp_c**2 + 0.00029 * temp_c**3
    sound += (1.34 - 0.01 * temp_c) * (salinity - 35.0) + 0.016 * depth_m
    print(f"  S = {salinity:.1f}, T = {temp_c:.1f} C, z = {depth_m:.0f} m")
    print(f"  simplified sound speed = {sound:.4f} m/s")
    a_sea = 1.4e-3
    print(f"  seawater thermal expansion coefficient (nominal) = {a_sea:.1e} K^-1")

    print("\nAll six checks completed; exit status 0.")


if __name__ == "__main__":
    main()
