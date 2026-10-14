#!/usr/bin/env python3
"""Borehole geophysics for aquifers: a synthetic log suite interpreted for
porosity, saturation, clay content and permeability; a flowmeter profile; a
temperature log as a vertical-flow detector; a cross-hole travel-time shift from
salinity; and a packer test.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python borehole_hydrogeophysics_demo.py

Every log, aquifer and test result below is a SYNTHETIC teaching value.  No real
borehole, log, core or field test is used.

Standard constants used:
    rho_w = 1000 kg/m^3, rho_matrix = 2650 kg/m^3 (assumed mineral density)
    c_water = 4.18e6 J m^-3 K^-1, k_thermal = 2.0 W m^-1 K^-1 (stated model values)

Contents
--------
1. A synthetic log suite: natural gamma, resistivity, density, NMR T2.
2. Interpretation: clay volume, density porosity, and their cross-check.
3. Water saturation from Archie, and the uncertainty that dominates it.
4. Permeability from the NMR log (SDR) and the transmissivity by integration.
5. Flowmeter: where the water actually enters the borehole.
6. A temperature log as a vertical-flow detector, and the cross-hole link.
7. A packer test: K and transmissivity from a constant-head injection.
8. Verification: density-porosity mass balance, temperature ODE, flow closure.
"""

import numpy as np
from scipy.integrate import odeint, quad

RNG = np.random.default_rng(20261014)

RHO_W = 1000.0
RHO_MATRIX = 2650.0
C_WATER = 4.18e6        # J m^-3 K^-1
K_THERMAL = 2.0         # W m^-1 K^-1
SDR_C = 4.0e-9          # m^2/s^3 per (fraction^4 s^2): SYNTHETIC calibration

# --- SYNTHETIC stratigraphy (depth in metres below ground level) -------------
UNITS = (
    ("sand (unsaturated)", 0.0, 6.0, 0.30, 0.12, 25.0, 25.0),
    ("sand aquifer", 6.0, 24.0, 0.32, 0.05, 90.0, 20.0),
    ("silty aquitard", 24.0, 32.0, 0.38, 0.45, 12.0, 15.0),
    ("sand aquifer", 32.0, 48.0, 0.30, 0.08, 60.0, 18.0),
    ("clay basement", 48.0, 60.0, 0.42, 0.85, 5.0, 10.0),
)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def unit_at(z):
    for name, z0, z1, phi, vclay, t2ms, rw in UNITS:
        if z0 <= z < z1:
            return name, phi, vclay, t2ms, rw
    return UNITS[-1][0], UNITS[-1][3], UNITS[-1][4], UNITS[-1][5], UNITS[-1][6]


def density_porosity(rho_b):
    """n = (rho_matrix - rho_b) / (rho_matrix - rho_fluid), fluid = water."""
    return (RHO_MATRIX - rho_b) / (RHO_MATRIX - RHO_W)


def archie_sw(phi, rw, rt, a=1.0, m=2.0, n=2.0):
    """Archie: Sw = (a rw / (phi^m Rt))^(1/n)."""
    arg = a * rw / (phi ** m * rt)
    return np.clip(arg, 0.0, 1.0) ** (1.0 / n)


def sdr_permeability(phi, t2_ms, c=SDR_C):
    """SDR: k = C phi^4 T2^2, returned in m^2."""
    return c * phi ** 4 * (t2_ms * 1e-3) ** 2


def temperature_profile(z, v_z, t_surface, gradient, z_star):
    """Steady temperature with vertical Darcy velocity v_z (positive upward).

    Solution of k d2T/dz2 = rho_w c_w v_z dT/dz:
    T = T0 + G z + (rho c v / k) ... expressed through the length scale
    z* = k / (rho_w c_w v), giving T = T0 + G z* (1 - exp(-z/z*)) for downward
    flow (v_z < 0 uses the same form with -z*), which is the standard
    advection-perturbed geotherm.
    """
    return t_surface + gradient * z_star * (1.0 - np.exp(-z / z_star))


def main():
    section("1. A synthetic log suite")
    print("  SYNTHETIC units (depth m, density porosity, clay volume, T2, Rw):")
    print("   unit                 z0     z1    phi   Vclay   T2 (ms)   Rw (ohm m)")
    for name, z0, z1, phi, vclay, t2ms, rw in UNITS:
        print(f"   {name:20s} {z0:5.1f} {z1:6.1f}   {phi:5.2f}   {vclay:5.2f}   "
              f"{t2ms:8.1f}   {rw:10.2f}")
    z = np.arange(0.5, 59.5, 0.5)
    print(f"\n  log sampled every 0.5 m from {z[0]} to {z[-1]} m "
          f"({z.size} samples)")
    print("   z (m)   GR (API)   Rt (ohm m)   rho_b (kg/m3)   T2 (ms)")
    for zz in (3.0, 10.0, 20.0, 28.0, 40.0, 52.0):
        name, phi, vclay, t2ms, rw = unit_at(zz)
        gr = 30.0 + 150.0 * vclay
        rt = rw / phi ** 2
        rho_b = RHO_MATRIX - phi * (RHO_MATRIX - RHO_W)
        print(f"   {zz:5.1f}   {gr:8.1f}   {rt:11.2f}   {rho_b:14.0f}   "
              f"{t2ms:8.1f}   [{name}]")
    print("  The four logs are deliberately redundant: gamma gives clay, density")
    print("  gives total porosity, resistivity plus porosity gives saturation, and")
    print("  NMR gives water content and pore size. No single log determines an")
    print("  aquifer; the interpretation is the agreement between them.")

    section("2. Interpretation: clay volume, porosity and their cross-check")
    print("  SYNTHETIC responses, with 2% log noise:")
    print("   Vclay from gamma = (GR - 30) / 150 (a stated linear mapping, matched")
    print("   to the synthetic response GR = 30 + 150 Vclay, so the units are API)")
    print("   phi from density  = (rho_matrix - rho_b)/(rho_matrix - rho_w)")
    print("   NMR total porosity = phi from T2 amplitude (stated equal to density")
    print("                        porosity in this synthetic suite)")
    print("\n   z (m)   Vclay   phi_density   phi_NMR   difference")
    errs = []
    for zz in (3.0, 10.0, 20.0, 28.0, 40.0, 52.0):
        name, phi, vclay, t2ms, rw = unit_at(zz)
        gr = 30.0 + 150.0 * vclay + 2.0 * RNG.standard_normal()
        vc = np.clip((gr - 30.0) / 150.0, 0.0, 1.0)
        rho_b = RHO_MATRIX - phi * (RHO_MATRIX - RHO_W) + \
            10.0 * RNG.standard_normal()
        phid = density_porosity(rho_b)
        phinmr = phi + 0.005 * RNG.standard_normal()
        errs.append(phid - phinmr)
        print(f"   {zz:5.1f}   {vc:5.2f}   {phid:11.4f}   {phinmr:7.4f}   "
              f"{phid - phinmr:+9.4f}")
    print(f"  rms density-minus-NMR porosity difference = "
          f"{np.sqrt(np.mean(np.square(errs))):.4f} "
          f"({np.sqrt(np.mean(np.square(errs))) / 0.3 * 100:.1f}% of a typical "
          f"porosity)")
    print("  A gas-bearing or clay-rich unit would show a systematic offset here;")
    print("  in this synthetic suite the two agree within their noise, which is the")
    print("  check that justifies using either alone.  Note also that the recovered")
    print("  clay volumes track the true values from section 1 (0.12, 0.05, 0.45,")
    print("  0.08, 0.85) to within the 2-API noise, which is what a correctly scaled")
    print("  gamma mapping must do - a mismatched scale between the response and the")
    print("  inversion would saturate the estimate at 0 and 1 instead.")

    section("3. Water saturation from Archie, and what dominates the error")
    print("  SYNTHETIC aquifer at 6-24 m: phi = 0.32, Rw = 20 ohm m, and a TRUE")
    print("  water saturation of 0.75 (the unit is 25% drained, as a water table at")
    print("  6 m over a 0.75-saturated capillary zone would be).")
    phi, rw, sw_true = 0.32, 20.0, 0.75
    rt = rw / (phi ** 2 * sw_true ** 2)
    print(f"  Archie forward: Rt = Rw / (phi^2 Sw^2) = {rt:.4f} ohm m")
    print("\n  what the log actually measures is Rt; the inversion needs m:")
    for m_try in (1.8, 2.0, 2.2):
        sw = float(archie_sw(phi, rw, rt, m=m_try))
        print(f"   m = {m_try:.1f}: Sw = {sw:.4f}  "
              f"(error {(sw / sw_true - 1) * 100:+.1f}%)")
    print("  and it needs the porosity, from a different log:")
    for phi_try in (0.28, 0.32, 0.36):
        sw = float(archie_sw(phi_try, rw, rt))
        print(f"   phi = {phi_try:.2f} (Rt fixed): Sw = {sw:.4f}  "
              f"(error {(sw / sw_true - 1) * 100:+.1f}%)")
    print("  and it needs the water resistivity, which comes from a SAMPLE:")
    for rw_try in (10.0, 20.0, 40.0):
        sw = float(archie_sw(phi, rw_try, rt))
        print(f"   Rw = {rw_try:.0f} ohm m: Sw = {sw:.4f}  "
              f"(error {(sw / sw_true - 1) * 100:+.1f}%)")
    print("  Sw scales as Rw^(-1/2), so a factor of two in Rw moves Sw by")
    print("  1/sqrt(2) = 0.71 or 1.41 depending on the direction; the upper row is")
    print("  clipped at Sw = 1, and that clipping is itself diagnostic - a log that")
    print("  reports full saturation almost always has the wrong Rw.  Porosity and")
    print("  m are model assumptions of comparable weight.  All three matter,")
    print("  and only the water resistivity is fixed by a measurement rather than")
    print("  by a model assumption - which is why a hydrogeophysical borehole")
    print("  programme must include sampling, not only logging.")

    section("4. Permeability from the NMR log, and the transmissivity")
    print(f"  SDR model: k = C phi^4 T2^2 with C = {SDR_C:.1e} m^2/s^3 "
          "(SYNTHETIC calibration)")
    print("\n   unit                 phi    T2 (ms)   k (m^2)      k (m/s)     "
          "k (m/d)")
    k_units = []
    for name, z0, z1, phi_u, vclay, t2ms, rw_u in UNITS:
        k = sdr_permeability(phi_u, t2ms)
        k_ms = k * RHO_W * 9.81 / 1.002e-3
        k_units.append((name, z0, z1, k_ms))
        print(f"   {name:20s} {phi_u:5.2f}   {t2ms:8.1f}   {k:11.4e}   "
              f"{k_ms:11.4e}   {k_ms * 86400:9.3f}")
    T_total = 0.0
    print("\n  transmissivity by integrating k over each unit:")
    for name, z0, z1, k_ms in k_units:
        T_u = k_ms * (z1 - z0)
        T_total += T_u
        print(f"   {name:20s} {z0:5.1f}-{z1:5.1f} m: T = {T_u:.4e} m^2/s "
              f"({T_u * 86400:8.2f} m^2/d)")
    print(f"   TOTAL T = {T_total:.4e} m^2/s = {T_total * 86400:.2f} m^2/d")
    print("  Note which units contribute.  The 18 m aquifer with T2 = 90 ms supplies")
    print("  most of the transmissivity, while the silty aquitard - which has the")
    print("  SECOND-LARGEST porosity in the suite (0.38) - supplies almost none,")
    print("  because its short T2 (12 ms) says its pores are small.  **Porosity is")
    print("  not transmissivity**, and the NMR log is the wireline measurement that")
    print("  separates the two.  The absolute values depend on the calibration")
    print("  constant C, which must be fixed against a core or a pumping test: the")
    print("  ratios between units are what the log delivers without calibration.")

    section("5. Flowmeter: where the water enters the borehole")
    print("  SYNTHETIC spinner survey during pumping at 5 L/s = 0.005 m^3/s")
    print("   depth (m)   flow (L/s)   incremental inflow (L/s)")
    depths = np.array([5.0, 10.0, 16.0, 22.0, 30.0, 38.0, 46.0])
    flows = np.array([0.05, 0.35, 1.80, 3.10, 3.35, 4.85, 5.00])
    inc = np.diff(flows, prepend=flows[0])
    for d, f, i in zip(depths, flows, inc):
        print(f"   {d:9.1f}   {f:11.2f}   {i:24.2f}")
    print(f"  closure: sum of increments = {inc.sum():.3f} L/s against the pumped "
          f"{flows[-1]:.2f} L/s "
          f"({abs(inc.sum() - flows[-1]) / flows[-1] * 100:.1f}% error)")
    top_inflow = inc[(depths >= 10.0) & (depths <= 22.0)].sum()
    print(f"  inflow between 10 and 22 m = {top_inflow:.2f} L/s "
          f"({top_inflow / flows[-1] * 100:.0f}% of the total)")
    print("  The flowmeter resolves WHICH unit produces water, which no surface")
    print("  method and no single log can: it is the direct check on an")
    print("  interpretation, and the reason a flowmeter log is worth its cost.")

    section("6. Temperature and cross-hole measurements")
    print("  Steady temperature with vertical water flow: T = T0 + G z*(1 - "
          "exp(-z/z*))")
    print(f"  with z* = k_thermal / (rho_w c_w v_z), k = {K_THERMAL:.1f} W/m/K,")
    print(f"  rho_w c_w = {C_WATER:.3e} J/m^3/K, T0 = 12.0 C, G = 0.025 C/m")
    print("   v_z (m/s)   z* (m)   T at 20 m   T at 50 m   gradient at 20 m (C/m)")
    for v in (0.0, 1e-9, 1e-8, 1e-7, 1e-6):
        if v == 0.0:
            t20, t50, g20 = 12.0 + 0.025 * 20, 12.0 + 0.025 * 50, 0.025
            print(f"   {v:9.1e}   {'inf':>7s}   {t20:9.3f}   {t50:9.3f}   "
                  f"{g20:21.5f}")
            continue
        z_star = K_THERMAL / (C_WATER * v)
        t20 = float(temperature_profile(20.0, -v, 12.0, 0.025, z_star))
        t50 = float(temperature_profile(50.0, -v, 12.0, 0.025, z_star))
        g20 = 0.025 * np.exp(-20.0 / z_star)
        print(f"   {v:9.1e}   {z_star:7.2f}   {t20:9.3f}   {t50:9.3f}   "
              f"{g20:21.5f}")
    print("  A downward Darcy velocity of 1e-8 m/s (0.86 mm/d) halves the gradient")
    print("  within ~48 m, and 1e-7 m/s suppresses it within 5 m: a temperature log")
    print("  is a sensitive vertical-flow detector, and it costs nothing extra")
    print("  because it runs in the same pass as the other logs.")
    print("\n  Cross-hole link, 12 m between two holes, in a unit of phi = 0.30:")
    print("  what a TRAVEL TIME measures is water content, not salinity:")
    print("   water content   eps_eff   v (m/ns)   travel time over 12 m (ns)")
    for theta in (0.10, 0.20, 0.30):
        phi_c = 0.30
        eps = ((1 - phi_c) * np.sqrt(4.5) + theta * np.sqrt(81) +
               (phi_c - theta) * 1.0) ** 2
        v = 0.299792458 / np.sqrt(eps)
        print(f"   {theta:13.2f}   {eps:7.3f}   {v:9.4f}   {12.0 / v:24.2f}")
    print(f"  a change of water content from 0.10 to 0.30 lowers the VELOCITY by")
    print("  about 38% and so raises the 12 m travel time by about 62%: easily")
    print("  resolved by a cross-hole seismic or GPR arrival time.")
    print("\n  what an AMPLITUDE measures is salinity, because the attenuation is")
    print("  linear in conductivity:")
    print("   TDS (mg/L)   sigma_w (S/m)   alpha at 50 MHz (dB/m)   one-way loss "
          "over 12 m (dB)   depth for 60 dB (m)")
    EPS0 = 8.8541878128e-12
    MU0 = 4.0e-7 * np.pi
    eps_val = 17.514
    for tds in (500.0, 5000.0, 35000.0):
        sigma_w = 0.15 * (tds / 1000.0)   # the calibration of lesson 14-01-05
        omega = 2.0 * np.pi * 50e6
        eps_abs = eps_val * EPS0
        lt = sigma_w / (omega * eps_abs)
        alpha = omega * np.sqrt(MU0 * eps_abs / 2.0) * \
            np.sqrt(np.sqrt(1.0 + lt ** 2) - 1.0)
        alpha_db = alpha * 8.686
        print(f"   {tds:11.0f}   {sigma_w:13.3f}   {alpha_db:22.2f}   "
              f"{alpha_db * 12.0:31.1f}   {60.0 / alpha_db:19.2f}")
    print("  (one-way loss over the 12 m separation, at a 60 dB dynamic range)")
    print("  A 5 g/L brine is opaque to 50 MHz radar within 0.6 m, so cross-hole")
    print("  RADAR cannot monitor salinity beyond very fresh contrasts: the same")
    print("  conductivity that makes the salinity an easy electrical target makes it")
    print("  an impossible radar one.  Salinity in a cross-hole setting is measured")
    print("  with low-frequency EM or cross-hole ERT (module 09-06), not with radar.")
    print("  The design rule follows directly from which parameter enters the")
    print("  velocity (water content) and which enters the attenuation (salinity).")

    section("7. A packer test")
    print("  Constant-head injection test: K = Q ln(R/r_w) / (2 pi L dh)")
    q_m3_s = 1.2e-4        # 0.12 L/s
    dh = 12.0
    L = 5.0
    rw_hole = 0.075
    R_inf = 30.0
    k_test = q_m3_s * np.log(R_inf / rw_hole) / (2.0 * np.pi * L * dh)
    print(f"  Q = {q_m3_s * 1e3:.2f} L/s, dh = {dh:.1f} m, L = {L:.1f} m, "
          f"r_w = {rw_hole * 1e3:.0f} mm, R = {R_inf:.0f} m")
    print(f"  ln(R/r_w) = {np.log(R_inf / rw_hole):.4f}")
    print(f"  K = {k_test:.4e} m/s = {k_test * 86400:.3f} m/d")
    print(f"  the same test expressed as transmissivity over the packed interval:")
    print(f"   T = K L = {k_test * L:.4e} m^2/s = {k_test * L * 86400:.2f} m^2/d")
    print("  The assumed R enters only logarithmically: changing R from 30 m to")
    print("  120 m changes ln(R/r_w) from 5.99 to 7.38, i.e. K by +23%.  State R,")
    print("  and prefer a radius-of-influence-free analysis (a slug test) where")
    print("  the formation is too tight for a steady test.")

    section("8. Verification")
    print("(a) density-porosity mass balance: for a sample of unit bulk volume,")
    print("    rho_b = (1-phi) rho_matrix + phi rho_w must invert to phi:")
    phi_t = 0.32
    rho_b = (1 - phi_t) * RHO_MATRIX + phi_t * RHO_W
    print(f"    forward: phi = {phi_t:.4f} -> rho_b = {rho_b:.1f} kg/m^3")
    print(f"    inverse: rho_b = {rho_b:.1f} -> phi = "
          f"{density_porosity(rho_b):.10f} (difference "
          f"{abs(density_porosity(rho_b) - phi_t):.2e})")
    print("(b) the temperature solution must satisfy the ODE")
    print("    k T'' = rho_w c_w v T' exactly; check the two sides numerically:")
    v = 1e-8
    z_star = K_THERMAL / (C_WATER * v)
    zz = np.linspace(0.0, 60.0, 601)
    tt = temperature_profile(zz, -v, 12.0, 0.025, z_star)
    d1 = np.gradient(tt, zz)
    d2 = np.gradient(d1, zz)
    lhs = K_THERMAL * d2
    rhs = C_WATER * v * -d1
    mask = (zz > 5) & (zz < 55)
    print(f"    max |k T'' - rho c v T'| = "
          f"{np.max(np.abs(lhs[mask] - rhs[mask])):.3e} (W/m^3)")
    print(f"    against the magnitude of the terms "
          f"{np.max(np.abs(rhs[mask])):.3e} W/m^3: a relative residual of "
          f"{np.max(np.abs(lhs[mask] - rhs[mask])) / np.max(np.abs(rhs[mask])):.1e},")
    print("    limited by the second-order finite difference, not by the solution.")
    print("(c) flowmeter closure: the increments must sum to the pumped rate, which")
    print("    they do by construction of the cumulation; the informative check is")
    print("    that each increment is non-negative, which a noisy spinner log can")
    print("    violate and which flags a measurement problem.")


if __name__ == "__main__":
    main()
