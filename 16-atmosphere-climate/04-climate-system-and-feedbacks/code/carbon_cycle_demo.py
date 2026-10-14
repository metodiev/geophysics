#!/usr/bin/env python3
"""The carbon cycle: the ppm-to-GtC conversion derived from standard constants,
reservoir inventories, an impulse response function and what it implies for
pulse persistence, a ramp-emission experiment with a mass-balance check, the
beta-gamma feedback parameters, and the near-linear relation between cumulative
emissions and peak warming.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python carbon_cycle_demo.py

Everything is SYNTHETIC. Reservoir inventories, impulse-response coefficients,
emission pathways, uptake parameters and warming coefficients are CHOSEN
TEACHING VALUES printed by this script. They are order-of-magnitude
conventional magnitudes used to make the arithmetic concrete, not measurements
of the real carbon cycle, and no scenario or policy figure is quoted.

Contents
--------
1. The ppm-to-GtC conversion, derived from surface pressure, gravity, the molar
   masses and the Earth's area.
2. Reservoir inventories and their ratios, including the atmosphere content
   implied by the conversion.
3. The impulse response function: how much of a pulse remains, and where.
4. A ramp-emission experiment: the airborne fraction trajectory and a
   mass-balance residual.
5. beta and gamma: concentration-driven and climate-driven uptake.
6. Cumulative emissions versus peak warming, and the slope that relates them.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

G = 9.81
P_SURF = 1.013e5             # Pa, adopted standard sea-level pressure
R_EARTH = 6.371e6            # m
M_C, M_AIR = 12.011, 28.97   # g/mol
RHO_OCEAN, C_OCEAN = 1025.0, 3985.0
C_MIXED = RHO_OCEAN * C_OCEAN * 50.0
YEAR = 365.0 * 86400.0


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


# ---------------------------------------------------------------------------
# 1. The ppm-to-GtC conversion
# ---------------------------------------------------------------------------

def part1_conversion():
    section("1. How many GtC is one ppm of atmospheric CO2?")
    area = 4.0 * np.pi * R_EARTH ** 2
    m_atm = P_SURF / G * area
    per_ppm = 1e-6 * m_atm * (M_C / M_AIR) / 1e12      # GtC per ppm
    print("Derived entirely from adopted constants:")
    print(f"  Earth surface area 4 pi a^2      = {area:.4e} m^2")
    print(f"  atmospheric mass p_s A/g         = {m_atm:.4e} kg")
    print(f"  carbon mass fraction M_C/M_air   = {M_C / M_AIR:.5f}")
    print(f"  so 1 ppm by mole of CO2 = {per_ppm:.4f} GtC")
    print("\n  Cross-checks and the size of the assumption:")
    print(f"    2 ppm = {2 * per_ppm:.2f} GtC;  100 ppm = "
          f"{100 * per_ppm:.1f} GtC")
    print(f"    the often-quoted 2.12 GtC per ppm corresponds to an atmospheric")
    print(f"    mass of {2.124e12 * M_AIR / M_C / 1e-6:.4e} kg, about "
          f"{(m_atm / (2.124e12 * M_AIR / M_C / 1e-6) - 1) * 100:.1f}% less")
    print("    than the value above, because the real atmospheric mass is")
    print("    obtained by integrating the actual pressure field, which is lower")
    print("    over high terrain than the adopted sea-level value. The DERIVATION")
    print("    is the lesson; the constant inherits any convention that goes into")
    print("    it, at the few-per-cent level.")


# ---------------------------------------------------------------------------
# 2. Inventories
# ---------------------------------------------------------------------------

def part2_inventories():
    section("2. Inventories: chosen magnitudes, and their ratios")
    per_ppm = 1e-6 * (P_SURF / G * 4.0 * np.pi * R_EARTH ** 2) * (M_C / M_AIR) \
        / 1e12
    co2_ppm = 400.0
    atm = co2_ppm * per_ppm
    print(f"CHOSEN inventories (GtC), for arithmetic only:")
    res = {
        "atmosphere (at 400 ppm)": atm,
        "land biosphere": 550.0,
        "soils and permafrost": 1500.0,
        "surface ocean": 900.0,
        "deep ocean": 37000.0,
        "fossil and rock reservoir": 4000.0,
    }
    for k, v in res.items():
        print(f"  {k:>28}: {v:9.1f}")
    print(f"\n  conversion used: {per_ppm:.4f} GtC per ppm, from Section 1")
    print("  Note WHERE the carbon is: the atmosphere holds about "
          f"{atm / (atm + res['deep ocean']) * 100:.1f}%")
    print("  of the atmosphere-plus-deep-ocean total. Perturbing the atmosphere")
    print("  measurably requires moving mass that is small relative to the")
    print("  reservoirs it exchanges with, which is why the ocean's chemistry")
    print("  sets the long-term fate of an emitted pulse.")


# ---------------------------------------------------------------------------
# 3. Impulse response
# ---------------------------------------------------------------------------

A_COEFFS = [(0.20, np.inf), (0.30, 3.5), (0.30, 30.0), (0.20, 400.0)]


def irf(t):
    """Fraction of an emitted pulse still in the atmosphere at time t (years)."""
    total = A_COEFFS[0][0] * np.ones_like(t)
    for a, tau in A_COEFFS[1:]:
        total = total + a * np.exp(-t / tau)
    return total


def part3_irf():
    section("3. Impulse response: a pulse is not a lifetime")
    print("SYNTHETIC impulse response a(t) = sum a_i exp(-t/tau_i):")
    for a, tau in A_COEFFS:
        label = "permanent" if np.isinf(tau) else f"{tau:.1f} yr"
        print(f"    a_i = {a:.2f}, tau_i = {label:>10}")
    print(f"  coefficients sum to {sum(a for a, _ in A_COEFFS):.2f}")
    print(f"\n{'time (yr)':>10} {'fraction remaining':>19} {'implied lifetime':>17}")
    for t in (1.0, 10.0, 100.0, 1000.0, 10000.0):
        print(f"{t:10.0f} {float(irf(np.array([t]))[0]):19.4f} "
              f"{'n/a' if t == 0 else '':>17}")
    print("\n  The 'lifetime' of a CO2 pulse is not a number: after 10 years about")
    print(f"  {float(irf(np.array([10.0]))[0]) * 100:.0f}% of a pulse remains, after a century")
    print(f"  {float(irf(np.array([100.0]))[0]) * 100:.0f}%, and after 10000 years")
    print(f"  {float(irf(np.array([10000.0]))[0]) * 100:.0f}%. The tail is set by the")
    print("  coefficient that does not decay (a_1 = 0.20 here), which stands for the")
    print("  fraction that ocean chemistry and ultimately silicate weathering can")
    print("  remove only over millennia. Reporting 'the residence time of CO2' as a")
    print("  single number discards exactly the part that matters for long")
    print("  horizons.")
    mass = 1000.0
    print(f"\n  for a pulse of {mass:.0f} GtC, the mass in each reservoir:")
    print(f"{'time (yr)':>10} {'atmosphere':>12} {'elsewhere':>11} {'total':>9}")
    for t in (0.0, 10.0, 100.0, 1000.0, 10000.0):
        a = float(irf(np.array([t]))[0])
        print(f"{t:10.0f} {mass * a:12.1f} {mass * (1 - a):11.1f} "
              f"{mass:9.1f}")
    print("  the total column is the mass-balance check: it is constant to the")
    print("  printed digits by construction, because the sinks are DEFINED as the")
    print("  complement of what stays in the atmosphere.")


# ---------------------------------------------------------------------------
# 4. A ramp of emissions
# ---------------------------------------------------------------------------

def part4_ramp():
    section("4. A ramp of emissions: the airborne fraction over time")
    years = np.arange(0.0, 301.0, 0.25)
    e_rate = np.where(years <= 100.0, 10.0 * (years / 100.0), 10.0)
    e_cum = np.cumsum(e_rate) * 0.25
    dt = 0.25
    n = years.size
    atm_excess = np.zeros(n)
    # convolution of the emission rate with the impulse response
    for k in range(1, n):
        # exact update for a sum of exponentials: track four reservoirs
        if k == 1:
            reservoirs = [0.0, 0.0, 0.0, 0.0]
        for j, (a, tau) in enumerate(A_COEFFS):
            if np.isinf(tau):
                reservoirs[j] += a * e_rate[k] * dt
            else:
                reservoirs[j] = (reservoirs[j] * np.exp(-dt / tau)
                                 + a * e_rate[k] * dt * 0.5
                                 * (1.0 + np.exp(-dt / tau)))
        atm_excess[k] = sum(reservoirs)
    print("SYNTHETIC pathway: emissions rising linearly from 0 to 10 GtC/yr over")
    print("  100 years, then held at 10 GtC/yr for 200 more.")
    print(f"\n{'time (yr)':>10} {'cumulative emissions (GtC)':>27} "
          f"{'atmospheric excess (GtC)':>25} {'airborne fraction':>18}")
    for target in (25.0, 50.0, 100.0, 150.0, 200.0, 300.0):
        k = int(target / dt)
        af = atm_excess[k] / e_cum[k] if e_cum[k] > 0 else np.nan
        print(f"{years[k]:10.0f} {e_cum[k]:27.1f} {atm_excess[k]:25.1f} "
              f"{af:18.3f}")
    print("\n  The airborne fraction is a RATIO of two growing quantities and it")
    print("  changes with time: with these chosen coefficients it falls as the")
    print("  ocean and land sinks fill up. An 'airborne fraction' quoted without")
    print("  its time window is therefore not well defined, and a constant one is")
    print("  not a law of nature.")
    sinks = e_cum - atm_excess
    print("\n  consistency checks on the trajectory:")
    print(f"    cumulative emissions - atmospheric excess = land + ocean uptake")
    print(f"    minimum uptake over the run = {sinks.min():.3f} GtC (must be >= 0)")
    print(f"    the response function's coefficients sum to "
          f"{sum(a for a, _ in A_COEFFS):.2f}, which is what makes the")
    print("    atmosphere and the sinks partition the emissions exactly: the")
    print("    residual is round-off by construction, and the meaningful test is")
    print("    that no sink ever becomes a source, which a badly chosen set of")
    print("    coefficients would violate.")


# ---------------------------------------------------------------------------
# 5. beta and gamma
# ---------------------------------------------------------------------------

def equilibrium_state(emissions, beta, gamma, lam_abs, c0, f2x=3.7,
                      n_iter=600):
    """Solve dC = (E - gamma dT)/(1+beta) with the logarithmic forcing."""
    dc = emissions / (1.0 + beta)
    for _ in range(n_iter):
        f = f2x * np.log(1.0 + dc / c0) / np.log(2.0)
        dt = f / lam_abs
        dc_new = (emissions - gamma * dt) / (1.0 + beta)
        if abs(dc_new - dc) < 1e-13:
            dc = dc_new
            break
        dc = dc_new
    f = f2x * np.log(1.0 + dc / c0) / np.log(2.0)
    return dc, f, f / lam_abs


def part5_beta_gamma():
    section("5. beta and gamma: two uptake parameters, two mechanisms")
    c0, lam_abs = 800.0, 4.0
    print("dC = (E - gamma dT)/(1 + beta): beta is the uptake per unit excess")
    print("(concentration-driven), gamma the extra uptake per kelvin of warming")
    print("(climate-driven).")
    print(f"\n{'case':>26} {'dC (GtC)':>10} {'airborne':>10} {'dT (K)':>8}")
    for name, beta, gamma in (("beta only (gamma = 0)", 1.0, 0.0),
                              ("reference", 1.0, 100.0),
                              ("weak uptake (beta = 0.5)", 0.5, 100.0),
                              ("strong uptake (beta = 2.0)", 2.0, 100.0),
                              ("strong climate feedback", 1.0, 300.0)):
        dc, f, dt = equilibrium_state(1000.0, beta, gamma, lam_abs, c0)
        print(f"{name:>26} {dc:10.1f} {dc / 1000.0:10.3f} {dt:8.3f}")
    print("\n  beta controls how much of an emission stays airborne; gamma controls")
    print("  how much that share shrinks as the climate warms. They act in the")
    print("  same direction but on different timescales: beta acts within decades,")
    print("  gamma over the same decades to centuries as the temperature.")
    print("  Both are PARAMETERISATIONS of unresolved processes. The table's")
    print("  purpose is to show the sensitivity, not to estimate either one.")


# ---------------------------------------------------------------------------
# 6. Cumulative emissions and peak warming
# ---------------------------------------------------------------------------

def part6_tcre():
    section("6. Cumulative emissions versus warming")
    c0, lam_abs, beta, gamma = 800.0, 4.0, 1.0, 100.0
    per_ppm = 1e-6 * (P_SURF / G * 4.0 * np.pi * R_EARTH ** 2) * (M_C / M_AIR) \
        / 1e12
    print("Equilibrium warming against cumulative emissions, with the same")
    print("carbon budget each time (beta = 1, gamma = 100 GtC/K).\n")
    print(f"{'emissions (GtC)':>16} {'dC (GtC)':>10} {'ppm':>7} "
          f"{'dT (K)':>8} {'dT per 1000 GtC':>17}")
    e_list = [250.0, 500.0, 1000.0, 2000.0, 4000.0]
    dts = []
    for e in e_list:
        dc, f, dt = equilibrium_state(e, beta, gamma, lam_abs, c0)
        dts.append(dt)
        print(f"{e:16.0f} {dc:10.1f} {(c0 + dc) / per_ppm:7.0f} {dt:8.3f} "
              f"{dt / e * 1000.0:17.3f}")
    slope = np.polyfit(e_list, dts, 1)[0]
    resid = np.array(dts) - np.polyval(np.polyfit(e_list, dts, 1), e_list)
    print(f"\n  least-squares slope: {slope * 1000:.4f} K per 1000 GtC")
    print(f"  largest departure from the straight line: {np.max(np.abs(resid)):.4f} K")
    print("  The relation is close to linear over the low end of the range and")
    print("  falls away at the high end: the increment per 1000 GtC declines from")
    print("  0.72 K at 250 GtC to 0.41 K at 4000 GtC. The curvature comes from the")
    print("  logarithmic forcing, which saturates, and from the gamma term, which")
    print("  grows with warming. A single 'warming per 1000 GtC' is therefore an")
    print("  approximation valid over a limited range, and its value is an output")
    print("  of the chosen coefficients, not a constant of nature. Changing beta,")
    print("  gamma, the feedback parameter or the emissions PATHWAY would change")
    print("  it, since this calculation is an equilibrium one and the real system")
    print("  is transient.")


def main():
    part1_conversion()
    part2_inventories()
    part3_irf()
    part4_ramp()
    part5_beta_gamma()
    part6_tcre()
    print("\nAll models and data in this module are SYNTHETIC teaching models.")


if __name__ == "__main__":
    main()
