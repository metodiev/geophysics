#!/usr/bin/env python3
"""Case study archetype: geothermal field development.

Entirely SYNTHETIC.  No real field, resource estimate, well or report is used or
implied; the lesson names settings only as argument archetypes.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python case_study_geothermal_demo.py

Print-only; no network access.
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def main():
    section("1. Stored-heat resource: a wide, bimodal distribution")
    print("  SYNTHETIC teaching model H = rho c V (T - T_ref), with triangular")
    print("  distributions for area, thickness and temperature (no real field)")
    n = 400000
    area = RNG.triangular(5.0, 20.0, 40.0, n)          # km^2
    thick = RNG.triangular(0.3, 1.0, 2.0, n)           # km
    dtemp = RNG.triangular(40.0, 80.0, 150.0, n)       # K above the reference
    rho_c = 2.5e6                                      # J m^-3 K^-1 (teaching value)
    volume = area * 1e6 * thick * 1e3                  # m^3
    heat = rho_c * volume * dtemp                      # J
    for label, q in (("P90 (conservative)", 10), ("P50", 50), ("P10", 90)):
        print(f"  {label:20s} = {np.percentile(heat, q)/1e18:8.2f} EJ "
              f"({np.percentile(heat, q)/3.6e15:10.0f} TWh-thermal)")
    print(f"  ratio P10/P90 = {np.percentile(heat, 90)/np.percentile(heat, 10):.1f}")
    print("  A factor of four between the conservative and optimistic estimate comes")
    print("  from area, thickness and temperature -- the parameters the geophysics")
    print("  constrains only indirectly.  Report the distribution, not the P50.")
    recovery = 0.10
    print(f"\n  with a stated recovery factor of {recovery:.2f}, the recoverable heat")
    print(f"  is P90 = {np.percentile(heat, 10)*recovery/1e18:.2f} EJ, "
          f"P50 = {np.percentile(heat, 50)*recovery/1e18:.2f} EJ")

    section("2. Resource is not reserve: the flow-rate constraint")
    target_mw = 30.0            # MWe target (synthetic)
    conv = 0.10                 # thermal-to-electric conversion (teaching value)
    flow = RNG.triangular(20.0, 40.0, 80.0, n)          # kg/s per well
    dtemp_wh = 100.0            # K across the plant (synthetic)
    cp = 4200.0                 # J kg^-1 K^-1
    well_mw_e = flow * cp * dtemp_wh * conv / 1e6
    print(f"  target = {target_mw:.0f} MWe, conversion {conv:.2f}, "
          f"wellhead dT = {dtemp_wh:.0f} K")
    well_mw = flow * cp * dtemp_wh * conv / 1e6          # MWe per well
    print(f"  electric power per well: P10 = {np.percentile(well_mw, 10):.2f}, "
          f"P50 = {np.percentile(well_mw, 50):.2f}, "
          f"P90 = {np.percentile(well_mw, 90):.2f} MWe")
    for q in (10, 50, 90):
        wells = target_mw / np.percentile(well_mw, q)
        print(f"    at the P{q} well output, wells needed = {wells:5.1f}")
    print(f"\n  The well count spans from {target_mw/np.percentile(well_mw, 90):.0f} to")
    print(f"  {target_mw/np.percentile(well_mw, 10):.0f} wells between the P90 and P10 flow")
    print("  outcomes.  A stored-heat number with no flow-rate distribution cannot")
    print("  size a plant: that is the difference between 'resource' and 'reserve'.")

    section("3. The magnetotelluric conductor: a favourable sign or a hazard?")
    print("  ARGUMENT ARCHETYPE.  A conductive layer in an MT section can be")
    print("  clay alteration (a seal above a reservoir) or a saline/conductive")
    print("  zone in permeable rock.  The MT response alone is similar.")
    prior_prod = 0.30           # SYNTHETIC prior that a conductor overlies a reservoir
    p_cond_given_prod = 0.85    # P(conductor | productive)
    p_cond_given_dry = 0.55     # P(conductor | not productive)
    post = prior_prod * p_cond_given_prod / (
        prior_prod * p_cond_given_prod + (1 - prior_prod) * p_cond_given_dry)
    print(f"  prior P(productive) = {prior_prod:.2f}")
    print(f"  P(conductor | productive) = {p_cond_given_prod:.2f}; "
          f"P(conductor | dry) = {p_cond_given_dry:.2f}")
    print(f"  posterior P(productive | conductor) = {post:.3f}")
    print(f"  the conductor raises the odds, and {1-post:.0%} of conductors still")
    print("  overlie a non-productive target.")
    for pp in (0.10, 0.30, 0.60):
        po = pp * p_cond_given_prod / (pp * p_cond_given_prod
                                       + (1 - pp) * p_cond_given_dry)
        print(f"    prior {pp:.2f} -> posterior {po:.3f}")
    print("  Distinguishing the two conductors needs something MT cannot give: a")
    print("  temperature-gradient well, a mud/water sample, or a resistivity")
    print("  spectrum that separates clay conduction from saline conduction.")

    section("4. Induced-seismicity risk from a Gutenberg-Richter sequence")
    b = 1.0                     # stated teaching b-value, dimensionless
    m_min = 0.0                 # catalogue threshold of the synthetic sequence
    n_events = 2000             # events >= m_min in the synthetic sequence
    print(f"  stated b = {b:.1f}, catalogued events (M >= {m_min:.0f}) = {n_events}")
    print("  P(M >= m | M >= m0) = 10^(-b (m - m0))")
    print("\n   magnitude m   P(M >= m | M>=0)   expected number in the sequence")
    for m in (1.0, 2.0, 3.0, 4.0):
        prob = 10 ** (-b * (m - m_min))
        print(f"   {m:11.1f}   {prob:16.4f}   {n_events*prob:24.1f}")
    print("\n  The probability of a large event in a sequence is fixed by the")
    print("  b-value and the number of events, not by the operation's intent.  A")
    print("  traffic-light threshold is a decision about which tail risk to accept.")
    p_felt = 10 ** (-b * (2.5 - m_min))
    print(f"  P(M >= 2.5 | M >= 0) = {p_felt:.4f}, so {n_events*p_felt:.1f} events of")
    print(f"  M >= 2.5 are expected per {n_events} catalogued events at b = 1.0.")
    print("\n  All models and data in this module are SYNTHETIC.")


if __name__ == "__main__":
    main()
