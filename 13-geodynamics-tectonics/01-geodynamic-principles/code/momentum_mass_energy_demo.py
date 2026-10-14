#!/usr/bin/env python3
"""Momentum, mass and energy balances in the solid Earth.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python momentum_mass_energy_demo.py

Everything here is SYNTHETIC.  The parameters below are chosen teaching values,
not measurements, and no number is taken from a published model.  The demo is
print-only (no figures) and needs no network access.

Contents
--------
1. Momentum balance: Stokes settling of a buoyant sphere; Reynolds number.
2. The terms of the momentum equation compared: why mantle flow is Stokes flow.
3. Mass balance: divergence of an analytic incompressible flow, measured.
4. Energy balance I: viscous dissipation of a simple shear layer.
5. Energy balance II: conductive geotherm with radiogenic heating.
6. Energy balance III: thermal diffusion versus advection (Peclet number).
7. Global energy budget: heat content, heat loss, Urey ratio, cooling time.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC teaching parameters (chosen, not measured) --------------------
RHO_M = 3300.0        # kg/m^3   mantle density
G = 9.81              # m/s^2    gravitational acceleration (standard)
ETA = 1.0e21          # Pa s     reference (upper-mantle) dynamic viscosity
KAPPA = 1.0e-6        # m^2/s    thermal diffusivity
K_COND = 3.0          # W/(m K)  thermal conductivity
CP = 1250.0           # J/(kg K) specific heat capacity
ALPHA = 3.0e-5        # 1/K      thermal expansivity
DT_MANTLE = 1300.0    # K        top-to-bottom temperature contrast
R_EARTH = 6.371e6     # m        Earth radius (standard)
R_CMB = 3.480e6       # m        core-mantle boundary radius (standard)
Q_AVG = 0.087         # W/m^2    SYNTHETIC area-averaged surface heat flux
Q_RAD = 20.0e12       # W        SYNTHETIC radiogenic heat production
SEC_PER_YR = 3.1557e7
SEC_PER_MYR = SEC_PER_YR * 1.0e6


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def stokes_velocity(drho, a, eta):
    """Terminal rise speed of a buoyant sphere in Stokes flow, m/s.

    u = 2 drho g a^2 / (9 eta): buoyancy (4/3 pi a^3 drho g) balanced by the
    Stokes drag (6 pi eta a u).
    """
    return 2.0 * drho * G * a ** 2 / (9.0 * eta)


def poisson_2d_periodic_check(n=129, L=1.0):
    """Max |div u| / (max|u| / L) for an analytic divergence-free field.

    psi = sin(k x) sin(m z);  u = d psi/dz,  w = -d psi/dx  -> div u = 0 exactly.
    The central-difference divergence is measured to show the level at which
    mass balance is satisfied on a grid.
    """
    x = np.linspace(0.0, L, n)
    z = np.linspace(0.0, L, n)
    X, Z = np.meshgrid(x, z, indexing="ij")
    k = 2.0 * np.pi / L
    m = 2.0 * np.pi / L
    # analytic derivatives u = d psi/dz and w = -d psi/dx, then
    # finite-difference the divergence
    u = np.sin(k * X) * np.cos(m * Z) * m
    w = -np.cos(k * X) * np.sin(m * Z) * k
    du_dx = np.gradient(u, x, axis=0)
    dw_dz = np.gradient(w, z, axis=1)
    div = du_dx + dw_dz
    scale = np.max(np.hypot(u, w)) / L
    return np.max(np.abs(div)) / scale


def geotherm_with_radiogenic_heat(k, H, h, T_s, T_moho):
    """Steady 1-D conduction with uniform radiogenic heating H (W/m^3).

    k T'' = -H  with T(0) = T_s and T(h) = T_moho:
        T(z) = T_s + [(T_moho - T_s)/h + H h/(2k)] z - (H/(2k)) z^2.
    Returns (surface heat flux, Moho heat flux, upward fluxes in W/m^2).
    """
    grad = (T_moho - T_s) / h + H * h / (2.0 * k)
    q_surface = k * grad          # magnitude of upward flux at z = 0
    q_moho = q_surface - H * h    # flux leaving the layer at z = h
    return q_surface, q_moho


def main():
    section("1. Momentum balance: Stokes settling of a buoyant sphere")
    for a, label in ((1.0e5, "100 km blob"), (1.0e6, "1000 km blob")):
        drho = 50.0
        u = stokes_velocity(drho, a, ETA)
        Re = RHO_M * u * a / ETA
        print(f"SYNTHETIC: drho = {drho:.0f} kg/m^3, a = {a / 1e3:.0f} km, "
              f"eta = {ETA:.0e} Pa s  ({label})")
        print(f"  Stokes rise speed  u = {u:.4e} m/s = {u * SEC_PER_YR * 1e3:.3f} mm/yr")
        print(f"  Reynolds number    Re = rho u a / eta = {Re:.3e}")
    print("\n  Re << 1 at every geodynamic scale: inertia is negligible, so the")
    print("  momentum equation is a force balance, not an equation of motion.")

    section("2. The terms of the momentum equation, compared")
    a = 1.0e5
    u = stokes_velocity(50.0, a, ETA)
    L = 1.0e5
    inertia = RHO_M * u ** 2 / L          # rho u . grad u  / unit volume
    viscous = ETA * u / L ** 2            # eta grad^2 u   / unit volume
    pressure = RHO_M * G * 50.0           # buoyancy-scale pressure gradient
    print(f"  rho u^2 / L   = {inertia:.4e} Pa/m")
    print(f"  eta u / L^2   = {viscous:.4e} Pa/m")
    print(f"  rho g drho/rho= {pressure:.4e} Pa/m  (buoyancy drive)")
    print(f"  inertia / viscous = {inertia / viscous:.3e}  (this is Re)")
    print(f"  viscous / buoyancy = {viscous / pressure:.3e}")
    print("  => the momentum balance reduces to grad p = eta grad^2 u + rho g.")

    section("3. Mass balance: divergence of an analytic incompressible flow")
    err = poisson_2d_periodic_check()
    print("  field from psi = sin(kx) sin(mz):  u = psi_z,  w = -psi_x")
    print(f"  max |div u| / (max|u| / L) = {err:.3e}")
    print("  a divergence-free velocity field is exactly what incompressibility")
    print("  means; the residual is pure central-difference truncation error.")

    section("4. Energy balance I: viscous dissipation of a shear layer")
    # plate speeds are quoted in mm/yr and converted to m/s here
    for u_mm_yr, d in ((50.0, 100.0e3), (50.0, 10.0e3), (100.0, 100.0e3)):
        u_plate = u_mm_yr * 1e-3 / SEC_PER_YR                # m/s
        rate = u_plate / d                                  # 1/s
        phi = ETA * rate ** 2                               # W/m^3
        total = phi * d                                     # W/m^2
        print(f"  SYNTHETIC shear: u = {u_mm_yr:.0f} mm/yr over "
              f"d = {d / 1e3:.0f} km  (u = {u_plate:.3e} m/s)")
        print(f"    strain rate   = {rate:.3e} 1/s")
        print(f"    dissipation   = {phi:.3e} W/m^3")
        print(f"    column total  = {total * 1e3:.3f} mW/m^2")
    print("  dissipating 10-25 mW/m^2 over a 10-100 km shear zone is a")
    print("  non-negligible fraction of a typical continental heat flux.")

    section("5. Energy balance II: conductive geotherm with radiogenic heating")
    k_c, H_rad, h_crust = 3.0, 1.0e-6, 35.0e3
    T_s, T_moho = 0.0, 600.0
    q_s, q_m = geotherm_with_radiogenic_heat(k_c, H_rad, h_crust, T_s, T_moho)
    print(f"  SYNTHETIC: k = {k_c:.1f} W/(m K), H = {H_rad:.1e} W/m^3, "
          f"crust {h_crust / 1e3:.0f} km, T_moho = {T_moho:.0f} C")
    print(f"  surface heat flux   q_s = {q_s:.4f} W/m^2 = {q_s * 1e3:.1f} mW/m^2")
    print(f"  Moho heat flux      q_m = {q_m:.4f} W/m^2 = {q_m * 1e3:.1f} mW/m^2")
    print(f"  radiogenic share of the surface flux = "
          f"{H_rad * h_crust / q_s * 100:.1f}%")
    print("  temperature profile T(z) = T_s + [(T_moho-T_s)/h + Hh/(2k)] z - Hz^2/(2k):")
    z = np.linspace(0.0, h_crust, 5)
    grad = (T_moho - T_s) / h_crust + H_rad * h_crust / (2.0 * k_c)
    T = T_s + grad * z - H_rad * z ** 2 / (2.0 * k_c)
    for zi, Ti in zip(z, T):
        print(f"    z = {zi / 1e3:6.1f} km   T = {Ti:7.1f} C")

    section("6. Energy balance III: diffusion versus advection (Peclet number)")
    L = 1.0e5
    u = stokes_velocity(50.0, L, ETA)
    t_diff = L ** 2 / KAPPA
    t_adv = L / u
    pe = u * L / KAPPA
    print(f"  convection speed u = {u:.4e} m/s, length L = {L / 1e3:.0f} km")
    print(f"  diffusive time  L^2/kappa = {t_diff:.3e} s = {t_diff / SEC_PER_MYR:.1f} Myr")
    print(f"  advective time  L/u       = {t_adv:.3e} s = {t_adv / SEC_PER_MYR:.3f} Myr")
    print(f"  Peclet number   Pe = uL/kappa = {pe:.4f}")
    print("  for the whole mantle, L = 2900 km:")
    Lm = 2.9e6
    print(f"    t_diff = {Lm ** 2 / KAPPA / SEC_PER_MYR:.1f} Myr, "
          f"t_adv = {Lm / u / SEC_PER_MYR:.1f} Myr, "
          f"Pe = {u * Lm / KAPPA:.1f}")

    section("7. Global energy budget")
    V_mantle = 4.0 / 3.0 * np.pi * (R_EARTH ** 3 - R_CMB ** 3)
    heat_content = RHO_M * CP * V_mantle * DT_MANTLE
    A_surface = 4.0 * np.pi * R_EARTH ** 2
    Q_loss = Q_AVG * A_surface
    print(f"  mantle volume        = {V_mantle:.3e} m^3")
    print(f"  heat content above CMB = rho c_p V dT = {heat_content:.3e} J")
    print(f"  surface area          = {A_surface:.3e} m^2")
    print(f"  heat loss (SYNTHETIC q_avg = {Q_AVG * 1e3:.0f} mW/m^2) "
          f"= {Q_loss:.3e} W = {Q_loss / 1e12:.1f} TW")
    print(f"  radiogenic production (SYNTHETIC) = {Q_RAD / 1e12:.1f} TW")
    print(f"  Urey ratio = production / loss = {Q_RAD / Q_loss:.3f}")
    t_cool = heat_content / (Q_loss - Q_RAD)
    print(f"  heat content / net loss = {t_cool:.3e} s = "
          f"{t_cool / (SEC_PER_YR * 1e9):.2f} Gyr")
    print("  the mantle holds a few billion years of heat at the present loss rate,")
    print("  so its thermal state is a balance of supply, transport and loss.")

    print("\n" + "=" * 72)
    print("All values above are SYNTHETIC teaching numbers (or standard constants")
    print("g = 9.81 m/s^2, R_Earth = 6371 km, R_CMB = 3480 km).")
    print("=" * 72)


if __name__ == "__main__":
    main()
