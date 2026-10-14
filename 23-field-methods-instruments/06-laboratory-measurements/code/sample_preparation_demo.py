"""Sample preparation, coring and drying: a synthetic laboratory walk-through.

Every number is a chosen teaching value combined with the standard relations
quoted in the accompanying lesson (Boyle's law, the mass and volume definitions
of density and porosity, the standard error of a mean).  No laboratory standard,
procedure or measured rock property is reproduced.
"""

import numpy as np

RNG_SEED = 20261014
P_ATM = 101325.0


def banner(n, text):
    print("=" * 72)
    print(f"{n}. {text}")
    print("=" * 72)


def section_1():
    banner(1, "Plug geometry: what an end effect does to a velocity")
    d_plug = 38.10e-3                      # m
    v_nom = 4500.0                         # m/s
    print(f"  plug diameter {d_plug*1e3:.1f} mm, nominal velocity {v_nom:.0f} m/s")
    print(f"  {'L/D':>6}{'length (mm)':>13}{'length excess':>15}{'velocity bias':>15}")
    for ratio in (1.0, 1.5, 2.0, 2.5, 3.0):
        length = ratio * d_plug
        excess = 0.10 * d_plug / length    # synthetic end-effect model
        print(f"  {ratio:6.1f}{length*1e3:13.2f}{excess*100:13.2f} %"
              f"{excess*v_nom:11.1f} m/s")
    print("  -> the bias falls as 1/(L/D), so a plug is cut long enough that the")
    print("     end effect is smaller than the velocity uncertainty it feeds.")


def section_2():
    banner(2, "Drying to constant mass: the stopping criterion")
    m_wet, m_dry = 215.90, 200.80          # g
    tau = 6.0                              # h, synthetic drying time constant
    print(f"  wet mass {m_wet:.2f} g, dry mass {m_dry:.2f} g, water "
          f"{m_wet-m_dry:.2f} g ({(m_wet-m_dry)/m_wet*100:.2f} % of wet mass)")
    print(f"  {'hours':>6}{'mass (g)':>12}{'change vs 24 h earlier':>24}{'stop?':>8}")
    for t in (24.0, 48.0, 72.0, 96.0):
        m = m_dry + (m_wet - m_dry) * np.exp(-t / tau)
        m_prev = m_dry + (m_wet - m_dry) * np.exp(-(t - 24.0) / tau)
        chg = (m - m_prev) / m_dry * 100.0
        ok = "yes" if abs(chg) < 0.01 else "no"
        print(f"  {t:6.1f}{m:12.3f}{chg:21.4f} %{ok:>8}")
    print("  -> the criterion is a mass change per 24 h, not a clock: a fixed oven")
    print("     time does not dry a clay-rich plug.")


def section_3():
    banner(3, "Porosity three ways, and what each route assumes")
    m_dry, m_sat, m_imm = 200.80, 219.70, 126.39       # g
    rho_w, rho_g = 0.998, 2.65                         # g/cm3
    d, length = 38.10e-3, 83.0e-3                      # m
    v_cal_cm3 = np.pi * (d / 2.0 * 100.0) ** 2 * (length * 100.0)
    v_arch_cm3 = (m_sat - m_imm) / rho_w
    v_pore_cm3 = (m_sat - m_dry) / rho_w
    phi_cal = v_pore_cm3 / v_cal_cm3
    phi_arch = v_pore_cm3 / v_arch_cm3
    phi_grain = 1.0 - (m_dry / rho_g) / v_cal_cm3
    print(f"  masses: dry {m_dry:.2f} g, saturated {m_sat:.2f} g, immersed {m_imm:.2f} g")
    print(f"  pore water volume = {v_pore_cm3:8.3f} cm3")
    print(f"  caliper bulk volume  = {v_cal_cm3:8.3f} cm3 -> porosity {phi_cal*100:6.2f} %")
    print(f"  Archimedes bulk vol. = {v_arch_cm3:8.3f} cm3 -> porosity {phi_arch*100:6.2f} %")
    print(f"  grain density {rho_g:.2f} g/cm3, no bulk volume -> porosity "
          f"{phi_grain*100:6.2f} %")
    print(f"  caliper / Archimedes volume ratio = {v_cal_cm3/v_arch_cm3:6.4f} "
          f"({(v_cal_cm3/v_arch_cm3-1)*100:+.2f} %)")
    print("  -> the caliper volume is an envelope and overstates the solid+void")
    print("     volume by the surface roughness; the grain-density route needs no")
    print("     bulk volume but assumes a grain density that is itself measured.")
    return phi_cal, phi_arch


def section_4():
    banner(4, "Vacuum saturation: the residual gas that spoils the porosity")
    v_pore = 18.94e-6                     # m3
    print(f"  pore volume {v_pore*1e6:.2f} cm3, initially air-filled at "
          f"{P_ATM/1000:.1f} kPa")
    print(f"  {'evacuation (Pa)':>17}{'residual air (cm3)':>21}{'S_air':>9}")
    for p_vac in (1.0e5, 1.0e4, 1.0e3, 1.0e2, 1.0e1):
        v_res = v_pore * p_vac / P_ATM
        print(f"  {p_vac:17.1f}{v_res*1e6:21.4f}{v_res/v_pore:9.4f}")
    print("  -> the residual gas fraction is the pressure ratio, so a 10 kPa")
    print("     vacuum leaves 9.87 % of the pore space air-filled and the measured")
    print("     water saturation -- and hence the porosity -- is low by that amount.")


def section_5(phi_cal, phi_arch):
    banner(5, "How many plugs to quote a porosity mean")
    rng = np.random.default_rng(RNG_SEED)
    sd_true = 1.20                        # porosity points, synthetic
    mean_true = 0.5 * (phi_cal + phi_arch) * 100.0
    print(f"  synthetic between-plug sd = {sd_true:.2f} porosity points")
    print(f"  {'n':>4}{'se of mean':>13}{'95 % half-width':>18}{'simulated se':>15}")
    for n in (3, 5, 8, 12, 20, 40):
        se = sd_true / np.sqrt(n)
        sim = float(np.std([rng.normal(mean_true, sd_true, n).mean()
                            for _ in range(2000)], ddof=1))
        print(f"  {n:4d}{se:13.4f}{1.96*se:18.4f}{sim:15.4f}")
    print("  -> the standard error falls as 1/sqrt(n): buying the last 0.1 point of")
    print("     precision costs four times as many plugs, and the simulated column")
    print("     confirms the analytic one.")


def main():
    print()
    banner(0, "SAMPLE PREPARATION AND CORING: SYNTHETIC WALK-THROUGH")
    section_1()
    section_2()
    phi_cal, phi_arch = section_3()
    section_4()
    section_5(phi_cal, phi_arch)
    print()
    print("SYNTHETIC: every number above is a chosen parameter in this file combined")
    print("with the standard relations quoted in the lesson; no laboratory standard,")
    print("procedure or measured rock property is reproduced.")


if __name__ == "__main__":
    main()
