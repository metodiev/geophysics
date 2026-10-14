"""Laboratory density, porosity and permeability: a synthetic walk-through.

Every number is a chosen teaching value combined with the standard relations
quoted in the accompanying lesson (mass and volume definitions, Boyle's law,
Darcy's law, the Klinkenberg correction, first-order error propagation).  No
laboratory instrument specification or measured rock property is reproduced.
"""

import numpy as np

RNG_SEED = 20261014
M_DRY = 176.60          # g, the single dry mass used throughout
RHO_W, RHO_PAR = 0.998, 0.900       # g/cm3
V_CELL, V_EXP = 100.00, 50.00       # cm3, helium pycnometer
P1 = 100.0                          # kPa, gauge
MD_PER_M2 = 1.0 / 9.869233e-16       # mD in 1 m2


def banner(n, text):
    print("=" * 72)
    print(f"{n}. {text}")
    print("=" * 72)


def section_1():
    banner(1, "Bulk density: the coated-sample route for a friable specimen")
    m_coated, m_coated_imm = 176.915, 99.939
    v_par = (m_coated - M_DRY) / RHO_PAR
    v_bulk_coated = (m_coated - m_coated_imm) / RHO_W
    v_bulk = v_bulk_coated - v_par
    rho_b = M_DRY / v_bulk
    print(f"  dry mass {M_DRY:.3f} g; coated {m_coated:.3f} g, immersed "
          f"{m_coated_imm:.3f} g")
    print(f"  paraffin film volume  = {v_par:8.4f} cm3")
    print(f"  coated bulk volume    = {v_bulk_coated:8.4f} cm3")
    print(f"  corrected bulk volume = {v_bulk:8.4f} cm3  (film is "
          f"{v_par/v_bulk_coated*100:.2f} % of the coated volume)")
    print(f"  bulk density          = {rho_b:8.4f} g/cm3")
    print(f"  ignoring the film would give {M_DRY/v_bulk_coated:8.4f} g/cm3 "
          f"({(M_DRY/v_bulk_coated/rho_b-1)*100:+.3f} %)")
    print("  -> the film correction is small but systematic, and it is the largest")
    print("     error term for a friable or heavily coated specimen.")
    return rho_b, v_bulk


def section_2():
    banner(2, "Helium pycnometry: Boyle's law and its sensitivity")
    print(f"  cell {V_CELL:.2f} cm3, expansion volume {V_EXP:.2f} cm3, initial "
          f"pressure {P1:.1f} kPa gauge")
    print(f"  {'p2 (kPa)':>10}{'V_solid (cm3)':>16}{'dV/dp2 (cm3/kPa)':>19}"
          f"{'grain density':>15}")
    for p2 in (90.0, 70.0, 60.0, 50.0, 40.0):
        v_s = V_CELL - V_EXP * (P1 / p2 - 1.0)
        dvs = V_EXP * P1 / p2 ** 2
        print(f"  {p2:10.1f}{v_s:16.4f}{dvs:19.4f}{M_DRY/v_s:15.4f}")
    v_s = V_CELL - V_EXP * (P1 / 60.0 - 1.0)
    drift = V_EXP * P1 / 60.0 ** 2 * 0.5
    print(f"  at p2 = 60 kPa: V_solid = {v_s:.4f} cm3, grain density "
          f"{M_DRY/v_s:.4f} g/cm3")
    print(f"  a 0.5 kPa error in p2 moves V_solid by {drift:.4f} cm3 "
          f"({drift/v_s*100:.3f} %) and the grain density the other way")
    print("  -> the resolution is set by the expansion ratio and the pressure")
    print("     transducer, not by the balance; a leak or a thermal drift appears")
    print("     as a slow pycnometry drift, which is why a two-standard check runs")
    print("     before and after every batch.")
    return v_s


def section_3(rho_b, v_bulk, v_grain):
    banner(3, "Porosity from grain volume and bulk volume")
    rho_g = M_DRY / v_grain
    phi = 1.0 - v_grain / v_bulk
    phi_alt = 1.0 - rho_b / rho_g
    print(f"  bulk volume  {v_bulk:8.4f} cm3  (coated-immersion route)")
    print(f"  grain volume {v_grain:8.4f} cm3  (pycnometry, same material)")
    print(f"  grain density {rho_g:8.4f} g/cm3, bulk density {rho_b:.4f} g/cm3")
    print(f"  porosity, 1 - V_grain/V_bulk = {phi*100:8.4f} %")
    print(f"  porosity, 1 - rho_b/rho_g    = {phi_alt*100:8.4f} %  "
          f"(difference {abs(phi-phi_alt)*100:.2e} points)")
    print("  -> the two forms are algebraically identical: a disagreement means an")
    print("     arithmetic or a unit error, not a property of the rock.")
    print(f"  the water-saturation route of the previous lesson would need "
          f"{phi*v_bulk*RHO_W:6.2f} g of water to fill this pore volume")


def section_4():
    banner(4, "Gas permeability and the Klinkenberg correction")
    k_l, b_kl = 1.00, 0.80               # mD, MPa
    p_mean = np.array([0.5, 1.0, 2.0, 4.0])
    k_g = k_l * (1.0 + b_kl / p_mean)
    print(f"  synthetic K_L = {k_l:.2f} mD, b = {b_kl:.2f} MPa")
    print(f"  {'mean pressure (MPa)':>20}{'K_gas (mD)':>13}{'1/P (1/MPa)':>13}")
    for p, k in zip(p_mean, k_g):
        print(f"  {p:20.2f}{k:13.4f}{1.0/p:13.4f}")
    fit = np.polyfit(1.0 / p_mean, k_g, 1)
    k_l_fit, slope = fit[1], fit[0]
    b_fit = slope / k_l_fit
    print(f"  least-squares fit: K_gas = {k_l_fit:.4f} + {slope:.4f} (1/P)")
    print(f"  recovered K_L = {k_l_fit:.4f} mD and b = {b_fit:.4f} MPa "
          f"(exact to 4 decimals)")
    print(f"  the uncorrected 0.5 MPa value is {k_g[0]:.2f} mD, i.e. "
          f"{k_g[0]/k_l_fit:.2f} x the liquid-equivalent value")
    print("  -> the correction is a straight line in 1/P; the intercept is what")
    print("     gets reported, and it is never measured directly.")


def section_5():
    banner(5, "Steady-state flow test: permeability and its uncertainty")
    mu = 1.0e-3                          # Pa s, water at room temperature
    area, length = 1.14e-3, 0.080        # m2, m
    d_p = 2.0e5                          # Pa
    k = 1.0e-15                          # m2
    q = k * area * d_p / (mu * length)
    print(f"  A = {area*1e4:.2f} cm2, L = {length*1e3:.1f} mm, "
          f"dP = {d_p/1e6:.2f} MPa, mu = {mu*1e3:.3f} mPa s (water)")
    print(f"  flow rate for K = {k*MD_PER_M2:.3f} mD: Q = {q*1e9:.4f} mm3/s "
          f"= {q*86400*1e3:.4f} L/day")
    terms = [("flow rate", 1.0), ("length", 0.1), ("area", 0.2),
             ("differential pressure", 2.0), ("viscosity", 0.5)]
    var = [(name, (v / 100.0) ** 2) for name, v in terms]
    tot = sum(v for _, v in var)
    print(f"  {'term':<26}{'relative (%)':>14}{'variance share (%)':>20}")
    for (name, v), (_, vv) in zip(terms, var):
        print(f"  {name:<26}{v:14.2f}{vv/tot*100:20.2f}")
    print(f"  combined relative uncertainty {np.sqrt(tot)*100:8.3f} %")
    a_coef = d_p / q                     # Darcy coefficient, Pa s/m3
    b_coef = 0.01 * a_coef / q           # inertial term equals Darcy at 20x rate
    print(f"  {'Q (mm3/s)':>11}{'dP (MPa)':>11}{'apparent K (mD)':>18}{'fall (%)':>10}")
    k_apps = []
    for mult in (1.0, 2.0, 5.0, 10.0, 20.0):
        qq = mult * q
        dp = a_coef * qq + b_coef * qq ** 2
        k_app = qq * mu * length / (area * dp) * MD_PER_M2
        k_apps.append(k_app)
        print(f"  {qq*1e9:11.4f}{dp/1e6:11.4f}{k_app:18.4f}"
              f"{100*(1-k_app/k_apps[0]):10.2f}")
    print(f"  the apparent permeability falls {100*(1-k_apps[-1]/k_apps[0]):.2f} % over a")
    print("  20x range of rate: that is non-Darcy (inertial) flow, not a property of")
    print("  the rock, so a steady-state test must be run where K is independent of")
    print("  Q -- and the independence must be demonstrated, not assumed.")


def main():
    print()
    banner(0, "DENSITY, POROSITY AND PERMEABILITY: SYNTHETIC WALK-THROUGH")
    rho_b, v_bulk = section_1()
    v_grain = section_2()
    section_3(rho_b, v_bulk, v_grain)
    section_4()
    section_5()
    print()
    print("SYNTHETIC: every number above is a chosen parameter in this file combined")
    print("with the standard relations quoted in the lesson; no instrument")
    print("specification or measured rock property is reproduced.")


if __name__ == "__main__":
    main()
