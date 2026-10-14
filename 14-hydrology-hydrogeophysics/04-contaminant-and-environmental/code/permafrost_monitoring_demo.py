#!/usr/bin/env python3
"""Permafrost monitoring: the Stefan thaw-depth solution and its energy balance,
the resistivity contrast between frozen and unfrozen ground, the velocity change
Gassmann can and cannot explain, and the salinity confound.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python permafrost_monitoring_demo.py

Everything is SYNTHETIC: the soil properties, the thermal conductivity, the
water content, the pore-fluid conductivities and the dry-frame moduli are chosen
teaching values.  The only standard constants used are the latent heat of fusion
of water, the bulk modulus of ice, and the moduli and densities of water and air.

Contents
--------
1.  The Stefan solution and its check against the energy balance.
2.  Thaw depth against time and against thawing degree-days.
3.  Sensitivity to temperature, water content and thermal conductivity.
4.  Resistivity against the unfrozen water fraction.
5.  Velocity: what Gassmann explains, what it does not, and the bracket.
6.  A monitoring scenario and the detection threshold.
7.  The salinity confound.
8.  Reference numbers used in the lesson.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- standard constants -------------------------------------------------------
L_FUSION = 334.0e3        # latent heat of fusion of water, J/kg
RHO_WATER = 1000.0        # kg/m^3
K_ICE, RHO_ICE = 9.0, 917.0        # GPa, kg/m^3 (standard ice properties)
K_WATER_F, RHO_WATER_F = 2.20, 1000.0
K_AIR, RHO_AIR = 1.0e-4, 1.2        # GPa, kg/m^3
K_MIN, MU_MIN, RHO_MIN = 36.0, 45.0, 2650.0

# --- SYNTHETIC soil and monitoring model -------------------------------------
THETA = 0.30              # volumetric water content
K_TH = 2.0                # thermal conductivity of the frozen soil, W/(m K)
SIG_FRESH = 0.05          # unfrozen pore-water conductivity, S/m
SIG_BRACKISH = 0.50       # a brackish alternative, S/m
PHI = 0.30                # porosity
M_ARCHIE = 2.0
N_SAT = 2.0


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def stefan_depth(dt_k, t_days, k_th=K_TH, theta=THETA):
    """Thaw depth in m from X = sqrt(2 k dT t / L_v), L_v = theta rho_w L_f."""
    l_v = theta * RHO_WATER * L_FUSION
    return np.sqrt(2.0 * k_th * dt_k * t_days * 86400.0 / l_v)


def latent_energy(depth, theta=THETA):
    """Latent heat absorbed per unit area, J/m^2."""
    return theta * RHO_WATER * L_FUSION * depth


def conducted_energy(dt_k, depth, t_days, k_th=K_TH):
    """Time integral of the conducted flux per unit area, J/m^2.

    With X(t) = a sqrt(t) the flux k dT/X(t) integrates to 2 k dT t / X(t):
    the factor 2 is the integral of 1/sqrt(t), and it is exactly what makes
    the Stefan balance close.
    """
    return 2.0 * k_th * dt_k / depth * t_days * 86400.0


def rho_bulk(sig_w, sw, phi=PHI, m=M_ARCHIE, n=N_SAT):
    """Archie bulk resistivity with the unfrozen water as the conducting phase."""
    return 1.0 / (sig_w * sw ** n * phi ** m)


def gassmann(k_dry, k_min, k_fl, phi):
    num = (1.0 - k_dry / k_min) ** 2
    den = phi / k_fl + (1.0 - phi) / k_min - k_dry / k_min ** 2
    return k_dry + num / den


def velocity(k_sat, mu, rho):
    return (np.sqrt((k_sat * 1e9 + 4.0 * mu * 1e9 / 3.0) / rho) / 1.0e3,
            np.sqrt(mu * 1e9 / rho) / 1.0e3)


def main():
    section("1. The Stefan solution and the energy-balance check")
    print("  Balance at a freezing front at depth X: the heat conducted to the front")
    print("  per unit area, integrated over the season, is 2 k dT t / X (the factor 2")
    print("  is the integral of 1/sqrt(t)); the latent heat absorbed is L_v X with")
    print("  L_v = theta rho_w L_f.  Equating and solving gives")
    print("    X(t) = sqrt(2 k dT t / (theta rho_w L_f)).")
    dt_k, t_days = 10.0, 100.0
    l_v = THETA * RHO_WATER * L_FUSION
    x = stefan_depth(dt_k, t_days)
    print(f"  SYNTHETIC: dT = {dt_k:.0f} K, t = {t_days:.0f} days, "
          f"k = {K_TH:.1f} W/(m K), theta = {THETA:.2f}")
    print(f"  L_f = {L_FUSION:.0e} J/kg (standard); "
          f"L_v = theta rho_w L_f = {l_v:.4e} J/m^3")
    print(f"  X = {x:.4f} m")
    print(f"  latent heat absorbed per m^2 = {latent_energy(x):.4e} J/m^2")
    print(f"  heat conducted per m^2       = {conducted_energy(dt_k, x, t_days):.4e}"
          f" J/m^2")
    print(f"  ratio (must be 1)           = "
          f"{conducted_energy(dt_k, x, t_days) / latent_energy(x):.10f}")
    print("  the balance closes exactly, which is the check that the solution and")
    print("  the energy bookkeeping are the same thing.")

    section("2. Thaw depth against time and against degree-days")
    print("      t (days)   X (m)   degree-days (K day)   X from degree-days (m)")
    for t in (30.0, 60.0, 90.0, 120.0, 200.0):
        x1 = stefan_depth(dt_k, t)
        ddt = dt_k * t
        x2 = stefan_depth(1.0, ddt)
        print(f"  {t:11.0f}   {x1:5.3f}   {ddt:20.0f}   {x2:23.3f}")
    print("  the two forms agree because the solution depends only on the product")
    print("  dT x t: a warm summer of 100 days at 10 K thaws exactly as deep as a")
    print("  cool one of 200 days at 5 K.  This is the degree-day method, and its")
    print("  failure mode is the assumption of a constant, uniform dT.")
    print(f"  X grows as sqrt(t): quadrupling the summer length only doubles the")
    print(f"  thaw depth ({stefan_depth(dt_k, 400.0) / stefan_depth(dt_k, 100.0):.2f}x "
          f"for 4x the time).")

    section("3. Sensitivity to temperature, water content and conductivity")
    print("      dT (K)   theta   k (W/m/K)   X at 100 days (m)")
    for dtk in (5.0, 10.0, 20.0):
        print(f"  {dtk:9.1f}   {THETA:5.2f}   {K_TH:9.1f}   "
              f"{stefan_depth(dtk, 100.0):17.3f}")
    for theta in (0.15, 0.30, 0.45):
        print(f"  {10.0:9.1f}   {theta:5.2f}   {K_TH:9.1f}   "
              f"{stefan_depth(10.0, 100.0, theta=theta):17.3f}")
    for kth in (1.0, 2.0, 4.0):
        print(f"  {10.0:9.1f}   {THETA:5.2f}   {kth:9.1f}   "
              f"{stefan_depth(10.0, 100.0, k_th=kth):17.3f}")
    print("  X depends on dT, k and theta only through the combinations above:")
    print(f"  doubling dT multiplies X by {np.sqrt(2.0):.3f}, halving theta by "
          f"{np.sqrt(2.0):.3f}.")
    print("  A monitoring programme that reports a thaw-depth change must say which")
    print("  of the three it is attributing it to; the geophysics sees the total.")

    section("4. Resistivity against the unfrozen water fraction")
    print("  The conducting phase in frozen ground is the UNFROZEN water, so Archie")
    print("  is applied with S_w = unfrozen fraction and ice treated as an")
    print("  insulating solid.  SYNTHETIC: rho_w = 20 ohm m, phi = 0.30, m = n = 2.")
    rho_w = 1.0 / SIG_FRESH
    print(f"  pore-fluid resistivity rho_w = {rho_w:.2f} ohm m")
    print("      unfrozen fraction   rho_bulk (ohm m)   ratio to fully thawed")
    rho_thawed = rho_bulk(SIG_FRESH, 1.0)
    for sw in (1.00, 0.50, 0.20, 0.10, 0.05, 0.02):
        r = rho_bulk(SIG_FRESH, sw)
        print(f"  {sw:19.2f}   {r:16.1f}   {r / rho_thawed:21.1f}")
    print(f"  a reduction of the unfrozen fraction from 1.00 to 0.10 raises the")
    print(f"  resistivity by a factor {rho_bulk(SIG_FRESH, 0.10) / rho_thawed:.0f}.")
    print("  This is the reason resistivity is the workhorse of permafrost")
    print("  monitoring: the contrast is large, and it is monotone in the unfrozen")
    print("  water content, which is the quantity models need.")

    section("5. Velocity: what Gassmann explains and what it does not")
    phi_d, k_dry, mu_dry = 0.30, 5.0, 4.0
    rho_dry = (1.0 - phi_d) * RHO_MIN
    print(f"  SYNTHETIC soil frame: phi = {phi_d:.2f}, K_dry = {k_dry:.1f} GPa, "
          f"mu_dry = {mu_dry:.1f} GPa")
    print("      pore phase          K_sat (GPa)   rho (kg/m^3)   Vp (km/s)   Vs (km/s)")
    for label, k_fl, rho_fl in (("air", K_AIR, RHO_AIR),
                                ("water", K_WATER_F, RHO_WATER_F),
                                ("ice", K_ICE, RHO_ICE)):
        k_sat = gassmann(k_dry, K_MIN, k_fl, phi_d)
        rho = (1.0 - phi_d) * RHO_MIN + phi_d * rho_fl
        vp, vs = velocity(k_sat, mu_dry, rho)
        print(f"  {label:>18s}   {k_sat:11.4f}   {rho:12.1f}   {vp:9.4f}   "
              f"{vs:9.4f}")
    vp_ice = velocity(gassmann(k_dry, K_MIN, K_ICE, phi_d), mu_dry,
                      (1 - phi_d) * RHO_MIN + phi_d * RHO_ICE)[0]
    vp_w = velocity(gassmann(k_dry, K_MIN, K_WATER_F, phi_d), mu_dry,
                    (1 - phi_d) * RHO_MIN + phi_d * RHO_WATER_F)[0]
    print(f"  Gassmann with ice as the pore fluid predicts a freezing shift of only")
    print(f"  {1000 * (vp_ice - vp_w):.1f} m/s.  This is a LOWER BOUND: Gassmann")
    print("  treats the pore phase as a fluid and cannot see the cementation that")
    print("  ice actually provides.  An illustrative cemented bracket, in which the")
    print("  shear modulus rises by a factor 3 on freezing, is next:")
    for mu_cement in (mu_dry, 2.0 * mu_dry, 4.0 * mu_dry):
        vp_i = velocity(gassmann(k_dry, K_MIN, K_ICE, phi_d), mu_cement,
                        (1 - phi_d) * RHO_MIN + phi_d * RHO_ICE)[0]
        print(f"    mu on freezing = {mu_cement:5.1f} GPa -> Vp(ice) = "
              f"{vp_i:.4f} km/s, Vs = "
              f"{velocity(0.0, mu_cement, (1 - phi_d) * RHO_MIN + phi_d * RHO_ICE)[1]:.4f}"
              f" km/s")
    print("  the measured Vp/Vs shift therefore bounds the ice content only if the")
    print("  cementation is known, which is a petrophysical calibration, not a")
    print("  derivation.  State the bracket, never a single velocity-derived ice")
    print("  content.")

    section("6. A monitoring scenario and the detection threshold")
    dt_season, t_season, z_sensor = 12.0, 120.0, 2.0
    x_max = stefan_depth(dt_season, t_season)
    rho_ref = rho_bulk(SIG_FRESH, 1.0)
    print(f"  SYNTHETIC seasonal cycle: dT = {dt_season:.0f} K over "
          f"{t_season:.0f} days; sensor at {z_sensor:.1f} m.")
    print(f"  maximum seasonal thaw depth = {x_max:.3f} m")
    print("      day   X (m)   state at the sensor   rho at the sensor (ohm m)")
    for day in (60.0, 90.0, 100.0, 120.0):
        x = stefan_depth(dt_season, day)
        thawed = z_sensor < x
        sw = 1.0 if thawed else 0.10
        print(f"  {day:6.0f}   {x:5.3f}   {'thawed' if thawed else 'frozen':>19s}   "
              f"{rho_bulk(SIG_FRESH, sw):24.1f}")
    t_cross = (z_sensor ** 2 * THETA * RHO_WATER * L_FUSION
               / (2.0 * K_TH * dt_season) / 86400.0)
    rate = z_sensor / (2.0 * t_cross)
    print(f"  the front reaches the sensor at t = {t_cross:.1f} days "
          f"(inverting X(t) = {z_sensor:.1f} m)")
    print(f"  the front moves at dX/dt = X/(2t) = {rate:.5f} m/day there, so a")
    print(f"  weekly survey dates the crossing to about "
          f"{100 * rate * 7.0 / z_sensor:.1f}% of the sensor depth "
          f"({100 * rate * 7.0:.1f} cm)")
    print(f"  and the resistivity flip is a factor "
          f"{rho_bulk(SIG_FRESH, 0.10) / rho_ref:.0f}, far above any survey noise.")
    print("  A single fixed sensor is therefore a precise but binary indicator:")
    print("  it dates the front, it does not profile it.")

    section("7. The salinity confound")
    print("      sigma_w (S/m)   rho frozen (ohm m)   rho thawed (ohm m)   ratio")
    for sig in (0.05, 0.20, 0.50, 1.00):
        rf = rho_bulk(sig, 0.10)
        rt = rho_bulk(sig, 1.00)
        print(f"  {sig:14.2f}   {rf:18.1f}   {rt:18.1f}   {rf / rt:6.2f}")
    print("  the frozen/thawed ratio is INDEPENDENT of the pore-fluid conductivity")
    print("  in this model (it is exactly 1/S_w^n = 100), so salinity does not")
    print("  destroy the contrast, it only moves both resistivities.  What salinity")
    print("  does destroy is the ability to distinguish unfrozen water content from")
    print("  salinity: a brackish, partly frozen layer and a fresher, more thawed")
    print("  layer can have the same resistivity.  Report both as a trade-off.")

    section("8. Reference numbers used in the lesson")
    print(f"  Stefan: dT = 10 K, 100 days, theta = 0.30, k = 2.0 -> X = "
          f"{stefan_depth(10.0, 100.0):.3f} m")
    print(f"  energy balance closes to "
          f"{conducted_energy(dt_k, stefan_depth(dt_k, t_days), t_days) / latent_energy(stefan_depth(dt_k, t_days)):.6f}")
    print(f"  rho ratio, unfrozen 1.00 -> 0.10: "
          f"{rho_bulk(SIG_FRESH, 0.10) / rho_thawed:.1f}")
    print(f"  Gassmann water -> ice velocity shift = "
          f"{1000 * (vp_ice - vp_w):.1f} m/s (lower bound)")
    print(f"  seasonal thaw depth = {x_max:.3f} m for dT = 12 K over 120 days")


if __name__ == "__main__":
    main()
