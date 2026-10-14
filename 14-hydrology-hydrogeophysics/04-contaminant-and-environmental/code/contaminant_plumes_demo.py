#!/usr/bin/env python3
"""Contaminant plumes and their geophysical signature: one-dimensional
advection with dispersion and retardation, the bulk-conductivity change a
generic ionic tracer produces, and the concentration that a stated
resistivity noise can detect.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python contaminant_plumes_demo.py

Everything is SYNTHETIC.  The tracer is a generic, idealised ionic solute
described in arbitrary concentration units (CU); no real contaminant, site,
spill or regulated limit is used or implied.

Contents
--------
1.  Transport parameters and the retardation factor.
2.  Concentration profiles at three times, after a step release.
3.  Front position and the 10-90% transition width.
4.  Retardation: the breakthrough delay for a range of Kd.
5.  The pore-fluid and bulk conductivity of the plume, and the resistivity.
6.  Detection: the smallest concentration a stated resistivity noise can see.
7.  Time-lapse: the resistivity change at one sensor against time.
8.  Reference numbers used in the lesson.
"""

import numpy as np
from scipy.special import erfc

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC transport model (chosen teaching values) ----------------------
V_SEEP = 0.050           # pore-water seepage velocity, m/day
ALPHA_L = 1.0            # longitudinal dispersivity, m
C0 = 1000.0              # source concentration, arbitrary CU
PHI = 0.30               # porosity
RHO_BULK = 1855.0        # bulk density, kg/m^3  (= (1-phi) * 2650)
KD = 0.05                # distribution coefficient, mL/g (teaching value)

# --- SYNTHETIC pore-fluid conductivity model (linear, teaching value) --------
SIG_W0 = 0.050           # background pore-fluid conductivity, S/m
BETA = 1.0e-4            # S/m per CU of tracer
M_ARCHIE = 2.0           # cementation exponent used for the bulk conversion
A_ARCHIE = 1.0

SIGMA_MEAS = 0.02        # stated relative resistivity noise, 1 sigma


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def retardation(kd_ml_g, rho_b_kg_m3, phi):
    """R = 1 + rho_b Kd / theta, with Kd in mL/g and rho_b in kg/m^3.

    rho_b/theta * Kd  has units of cm^3/g * g/cm^3 = dimensionless when
    rho_b is converted to g/cm^3 and Kd stays in cm^3/g (numerically mL/g).
    """
    rho_b_g_cm3 = rho_b_kg_m3 / 1000.0
    return 1.0 + rho_b_g_cm3 * kd_ml_g / phi


def ade_step(x, t, v, c0=C0):
    """1-D advection-dispersion behind a step input: the Ogata-Banks form.

    D = alpha_L v (mechanical dispersion dominates diffusion in the aquifer).
    Uses the retarded velocity v (m/day) and x (m), t (days).
    """
    d = ALPHA_L * v
    return 0.5 * c0 * (erfc((x - v * t) / (2.0 * np.sqrt(d * t)))
                       + np.exp(v * x / d) * erfc((x + v * t)
                                                 / (2.0 * np.sqrt(d * t))))


def sigma_w(c):
    """Pore-fluid conductivity in S/m for a tracer concentration c in CU."""
    return SIG_W0 + BETA * c


def rho_bulk(sigma_w_value):
    """Bulk resistivity from the pore-fluid conductivity via Archie (S_w = 1)."""
    sigma = A_ARCHIE ** -1 * sigma_w_value * PHI ** M_ARCHIE
    return 1.0 / sigma


def main():
    section("1. Transport parameters and retardation")
    r_fac = retardation(KD, RHO_BULK, PHI)
    v_c = V_SEEP / r_fac
    d_mech = ALPHA_L * v_c
    print(f"  SYNTHETIC seepage velocity        v      = {V_SEEP:.4f} m/day")
    print(f"  porosity                          phi    = {PHI:.2f}")
    print(f"  bulk density                      rho_b  = {RHO_BULK:.0f} kg/m^3")
    print(f"  distribution coefficient          Kd     = {KD:.3f} mL/g")
    print(f"  retardation factor  R = 1 + rho_b Kd/phi = {r_fac:.4f}")
    print(f"  retarded front velocity           v/R    = {v_c:.4f} m/day")
    print(f"  mechanical dispersion D = alpha_L v      = {d_mech:.5f} m^2/day")
    print(f"  with R = 1 exactly (conservative tracer, Kd = 0) the front velocity")
    print(f"  would be {V_SEEP:.4f} m/day, i.e. {V_SEEP / v_c:.2f} times faster.")

    section("2. Concentration profiles behind a step release")
    x = np.linspace(0.0, 200.0, 9)
    for t_days in (365.0, 1095.0, 3650.0):
        c = ade_step(x, t_days, v_c)
        print(f"  t = {t_days:.0f} days ({t_days / 365.25:.1f} years):")
        print("      x (m)   " + "  ".join(f"{xi:8.1f}" for xi in x))
        print("      C (CU)  " + "  ".join(f"{ci:8.1f}" for ci in c))
    print("  the 50% point is the advected front; the spread about it is dispersion")

    section("3. Front position and the 10-90% transition width")
    print("      t (days)   front x = (v/R) t (m)   sigma (m)   10-90 width (m)")
    for t_days in (365.0, 1095.0, 3650.0):
        front = v_c * t_days
        sigma = np.sqrt(2.0 * d_mech * t_days)
        width = 2.0 * 1.281552 * sigma
        print(f"  {t_days:11.0f}   {front:22.1f}   {sigma:9.2f}   {width:15.2f}")
    print("  the width grows as sqrt(t) while the front grows as t: a young plume")
    print("  is wide relative to its travel distance, an old plume is sharp")

    section("4. Retardation: breakthrough delay from Kd")
    print("      Kd (mL/g)       R        v/R (m/day)   time to reach 50 m (days)")
    for kd in (0.0, 0.01, 0.05, 0.20, 1.00):
        r = retardation(kd, RHO_BULK, PHI)
        vv = V_SEEP / r
        print(f"  {kd:11.2f}   {r:8.4f}   {vv:12.5f}   {50.0 / vv:23.0f}")
    print(f"  at Kd = 0.20 mL/g the tracer arrives "
          f"{retardation(0.20, RHO_BULK, PHI):.2f}x later than a conservative")
    print(f"  tracer; at 1.00 mL/g it is slowed by R = "
          f"{retardation(1.0, RHO_BULK, PHI):.2f}, so a ten-year forecast changes "
          f"by the same factor.")

    section("5. Pore-fluid and bulk conductivity, and the resistivity")
    print("      C (CU)   sigma_w (S/m)   sigma_bulk (S/m)   rho_bulk (ohm m)")
    for c in (0.0, 50.0, 100.0, 250.0, 500.0, 1000.0):
        sw = sigma_w(c)
        sb = A_ARCHIE ** -1 * sw * PHI ** M_ARCHIE
        print(f"  {c:9.1f}   {sw:13.5f}   {sb:16.6f}   {1.0 / sb:16.2f}")
    rho_bg = rho_bulk(sigma_w(0.0))
    rho_full = rho_bulk(sigma_w(C0))
    print(f"  background rho = {rho_bg:.2f} ohm m; at C = {C0:.0f} CU "
          f"rho = {rho_full:.2f} ohm m")
    print(f"  the plume lowers the resistivity by a factor "
          f"{rho_bg / rho_full:.2f}")

    section("6. Detection: the smallest concentration a 2% noise can see")
    print(f"  stated noise on rho_bulk: {100 * SIGMA_MEAS:.0f}% (1 sigma)")
    for n_sigma, label in ((1.0, "1 sigma"), (2.0, "2 sigma")):
        need = n_sigma * SIGMA_MEAS
        c_min = need * SIG_W0 / (BETA * (1.0 - need))
        print(f"  threshold at {label}:  d rho/rho = {need:.3f}, so sigma_w must "
              f"rise by {100 * need:.1f}%")
        print(f"    C_min = {c_min:.1f} CU = {100 * c_min / C0:.2f}% of the source")
    c_det = 2.0 * SIGMA_MEAS * SIG_W0 / (BETA * (1.0 - 2.0 * SIGMA_MEAS))
    print(f"  the detection threshold is set by the BACKGROUND conductivity:")
    print(f"  a fresher background (smaller sigma_w0) lowers C_min proportionally,")
    print(f"  while a saltier one raises it.")

    section("7. Time-lapse: the resistivity change at one sensor")
    x_sensor = 50.0
    print(f"  sensor at x = {x_sensor:.0f} m; rho_bg = {rho_bg:.2f} ohm m")
    print("      t (days)   C (CU)   rho (ohm m)   change (%)")
    for t_days in (365.0, 1095.0, 1825.0, 2555.0, 3650.0, 5475.0):
        c = float(ade_step(np.array([x_sensor]), t_days, v_c)[0])
        rho = rho_bulk(sigma_w(c))
        print(f"  {t_days:11.0f}   {c:7.1f}   {rho:11.2f}   "
              f"{100 * (rho - rho_bg) / rho_bg:+10.2f}")
    t_arr = float(50.0 / v_c)
    print(f"  the front reaches the sensor at (v/R) t = 50 m -> t = "
          f"{t_arr:.0f} days")
    print("  before that the signal is absent, not small: a monitoring network")
    print("  that only samples after arrival misses the only part of the record")
    print("  that constrains the transport parameters.")

    section("8. Reference numbers used in the lesson")
    print(f"  R = {r_fac:.4f}; v/R = {v_c:.4f} m/day; front at 3650 days = "
          f"{v_c * 3650.0:.1f} m")
    print(f"  rho_background = {rho_bg:.2f} ohm m; rho_at_source = "
          f"{rho_full:.2f} ohm m")
    print(f"  10-90% width at 3650 days = "
          f"{2.0 * 1.281552 * np.sqrt(2.0 * d_mech * 3650.0):.1f} m")
    print(f"  two-sigma detection threshold = {100 * 2 * SIGMA_MEAS:.0f}% of rho, "
          f"C_min = {c_det:.1f} CU")


if __name__ == "__main__":
    main()
