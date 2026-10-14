"""Laboratory thermal measurements: a synthetic walk-through.

Every number is a chosen teaching value combined with the standard relations
quoted in the accompanying lesson (Fourier's law in a divided bar, the
temperature integral of thermal resistance, heat capacity and diffusivity, the
error-function penetration of a surface-temperature step, mixing laws).  No
instrument specification or measured rock property is reproduced.
"""

import math
import numpy as np

RNG_SEED = 20261014


def banner(n, text):
    print("=" * 72)
    print(f"{n}. {text}")
    print("=" * 72)


def section_1():
    banner(1, "Steady-state thermal conductivity in a divided bar")
    k_ref, dx_ref, dt_ref = 1.50, 0.010, 4.0     # W/m/K, m, K
    dx_s, dt_s = 0.015, 6.0
    flux = k_ref * dt_ref / dx_ref
    k_s = flux * dx_s / dt_s
    print(f"  reference: K = {k_ref:.2f} W/(m K), dx = {dx_ref*1e3:.1f} mm, "
          f"dT = {dt_ref:.1f} K")
    print(f"  heat flux through the stack = K dT/dx = {flux:8.1f} W/m2")
    print(f"  specimen: dx = {dx_s*1e3:.1f} mm, dT = {dt_s:.1f} K -> "
          f"K = {k_s:.4f} W/(m K)")
    print(f"  {'error source':<26}{'input error':>13}{'K error':>10}")
    for name, inp, sens in (("specimen thickness", 0.10, 1.0),
                            ("specimen dT", 1.0, -1.0),
                            ("reference K", 1.0, 1.0),
                            ("reference dT", 1.0, -1.0),
                            ("reference thickness", 0.10, 1.0)):
        print(f"  {name:<26}{inp:12.2f} %{inp*abs(sens):9.2f} %")
    print("  -> K is linear in every ratio, so the sensitivity is the sensitivity")
    print("     of the temperature measurement: a 1 K error on a 6 K drop is 17 %.")


def section_2():
    banner(2, "Temperature dependence and the effect on a heat flow")
    k0, slope, t0 = 3.00, 1.5e-3, 0.0
    z_top, z_bot = 0.0, 3000.0
    grad = 25.0e-3                       # K/m
    print(f"  synthetic K(T) = {k0:.2f} - {slope:.1e} T  [W/(m K), T in degC]")
    print(f"  {'T (degC)':>10}{'K (W/m/K)':>12}{'change from 0 degC (%)':>24}")
    for t in (0.0, 25.0, 50.0, 100.0, 200.0, 400.0, 800.0):
        k = k0 - slope * t
        print(f"  {t:10.1f}{k:12.4f}{100*(k/k0-1):24.2f}")
    n = 2000
    t_surf, t_moho = 10.0, 10.0 + grad * z_bot
    t_arr = np.linspace(t_surf, t_moho, n)
    k_arr = k0 - slope * t_arr
    r_int = np.trapezoid(1.0 / k_arr, t_arr)      # dT / K = resistance per area
    r_top = (t_moho - t_surf) / k0
    q_int = (t_moho - t_surf) / r_int
    q_top = (t_moho - t_surf) / r_top
    print(f"  over {z_top/1000:.0f}-{z_bot/1000:.0f} km at 25 K/km: T = "
          f"{t_surf:.1f} to {t_moho:.1f} degC")
    print(f"  using the surface K:        q = {q_top*1e3:8.2f} mW/m2")
    print(f"  integrating K(T):           q = {q_int*1e3:8.2f} mW/m2")
    print(f"  error from ignoring K(T):   {100*(q_top/q_int-1):+8.2f} %")
    print("  -> K(T) must be integrated, not evaluated at the surface, and the")
    print("     integration makes the deeper, hotter rock the dominant resistance.")


def section_3():
    banner(3, "Heat capacity, diffusivity and effusivity")
    mass, energy, d_temp = 0.250, 168.0, 2.40      # kg, J, K
    rho, k_cond = 2650.0, 2.60                     # kg/m3, W/(m K)
    cp = energy / (mass * d_temp)
    alpha = k_cond / (rho * cp)
    eff = math.sqrt(k_cond * rho * cp)
    print(f"  m = {mass:.3f} kg, Q = {energy:.1f} J, dT = {d_temp:.2f} K")
    print(f"  cp = Q / (m dT) = {cp:9.2f} J/(kg K)")
    print(f"  alpha = K / (rho cp) = {alpha:.4e} m2/s")
    print(f"  effusivity e = sqrt(K rho cp) = {eff:9.1f} J/(m2 K s^0.5)")
    print(f"  {'scenario':<24}{'Q':>6}{'dT':>6}{'m':>6}{'cp error':>11}")
    cases = [("best case", 0.5, 0.5, 0.1),
             ("realistic", 1.0, 1.0, 0.2),
             ("heat loss present", 3.0, 0.5, 0.2)]
    for name, q_e, dt_e, m_e in cases:
        print(f"  {name:<24}{q_e:5.1f}%{dt_e:5.1f}%{m_e:5.1f}%"
              f"{math.hypot(q_e, dt_e, m_e):10.3f}%")
    print("  -> cp needs the heat input and the mass, and the heat input is")
    print("     usually the term with the largest systematic error (losses to")
    print("     the enclosure), which is not in the budget unless it is measured.")


def section_4():
    banner(4, "Penetration of a surface-temperature step")
    alpha, d_temp = 1.0e-6, 5.0                   # m2/s, K
    year = 365.25 * 86400.0
    print(f"  alpha = {alpha:.1e} m2/s, surface step {d_temp:.1f} K")
    print(f"  {'depth (m)':>11}{'10 yr':>10}{'100 yr':>10}{'1000 yr':>10}")
    for z in (25.0, 50.0, 100.0, 200.0, 400.0):
        row = f"  {z:11.1f}"
        for t_yr in (10.0, 100.0, 1000.0):
            t = t_yr * year
            frac = math.erfc(z / (2.0 * math.sqrt(alpha * t)))
            row += f"{d_temp*frac:10.4f}"
        print(row)
    z100_100 = 2.0 * math.sqrt(alpha * 100.0 * year)
    print(f"  the 100-year penetration scale 2 sqrt(alpha t) = {z100_100:.1f} m")
    print("  -> a recent surface warming is a measurable perturbation for a few")
    print("     hundred metres below a century of change, and it must be modelled")
    print("     before any heat flow is interpreted as a deep signal.")


def section_5():
    banner(5, "Mixing laws: three models, three answers")
    k_matrix, k_fluid, phi = 3.00, 0.60, 0.20
    k_geo = k_matrix ** (1.0 - phi) * k_fluid ** phi
    k_arith = (1.0 - phi) * k_matrix + phi * k_fluid
    k_harm = 1.0 / ((1.0 - phi) / k_matrix + phi / k_fluid)
    print(f"  matrix K = {k_matrix:.2f}, fluid K = {k_fluid:.2f}, porosity {phi:.2f}")
    print(f"  geometric mean (typical of a rock) = {k_geo:8.4f} W/(m K)")
    print(f"  arithmetic mean (upper bound)      = {k_arith:8.4f} W/(m K)")
    print(f"  harmonic mean (lower bound)        = {k_harm:8.4f} W/(m K)")
    print(f"  spread from the model alone        = "
          f"{100*(k_arith/k_harm-1):8.2f} %")
    print(f"  geometric mean relative to the matrix = "
          f"{100*(k_geo/k_matrix-1):8.2f} %")
    print("  -> the mixing law is a modelling choice of the same size as the")
    print("     porosity effect it is meant to describe; measured K on the same")
    print("     specimen is the only way to choose between them.")


def main():
    print()
    banner(0, "LABORATORY THERMAL MEASUREMENTS: SYNTHETIC WALK-THROUGH")
    section_1()
    section_2()
    section_3()
    section_4()
    section_5()
    print()
    print("SYNTHETIC: every number above is a chosen parameter in this file combined")
    print("with the standard relations quoted in the lesson; no instrument")
    print("specification or measured rock property is reproduced.")


if __name__ == "__main__":
    main()
