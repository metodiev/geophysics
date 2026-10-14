#!/usr/bin/env python3
"""Climate-geohazard interactions: compound coastal flooding under a
sea-level rise, permafrost thaw settlement, and the factor of safety of a
slope as pore pressure rises, with the counterfactual stated for each.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python climate_geohazards_demo.py

Everything is SYNTHETIC.  The hazard distributions, ground-ice contents, slope
geometry and strength parameters are chosen teaching values.  No real coastline,
permafrost site, slope, event, instrument or published projection is used.

Contents
--------
1. Compound coastal flooding: joint exceedance with and without sea-level rise.
2. How the return period of a compound event changes when the mean sea level
   moves.
3. Permafrost thaw settlement from a deepening active layer.
4. Slope stability: the pore-pressure ratio at which a factor of safety crosses
   one.
5. The counterfactual each statement requires.
"""

import numpy as np
from scipy import stats

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC hazards (chosen, not measured) -------------------------------
SLR_M = 0.50             # m, a chosen sea-level rise
SURGE_MEDIAN = 1.20      # m, median storm surge above mean sea level
SURGE_SIGMA = 0.35       # log-scale
RIVER_MEDIAN = 1.00      # m, median river stage
RIVER_SIGMA = 0.40       # log-scale
RHO = 0.50               # correlation between the two drivers (Gaussian copula)
SURGE_THRESHOLD = 1.80   # m, coastal defence level above mean sea level
RIVER_THRESHOLD = 1.70   # m, river flood stage
EXCESS_ICE = 0.30        # volume fraction of excess ice in the frozen soil
THAW_DEPTH_NOW = 1.0     # m, active layer today
THAW_DEPTH_WARM = 1.8    # m, active layer in the warmer scenario
GAMMA = 18.0e3           # N/m^3, soil unit weight
COHESION = 5.0e3         # Pa, effective cohesion
PHI_FRICTION = 30.0      # degrees, effective friction angle
BETA_DEG = 22.0          # degrees, slope angle
Z_SLAB = 3.0             # m, slab thickness


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def compound_probability(surge_shift, rho=RHO):
    """P(surge + shift > s0 AND river > r0) with lognormal marginals."""
    zs = (np.log(SURGE_THRESHOLD - surge_shift) - np.log(SURGE_MEDIAN)) / SURGE_SIGMA
    zr = (np.log(RIVER_THRESHOLD) - np.log(RIVER_MEDIAN)) / RIVER_SIGMA
    cov = np.array([[1.0, rho], [rho, 1.0]])
    mvn = stats.multivariate_normal(mean=[0.0, 0.0], cov=cov)
    phi2 = float(mvn.cdf([zs, zr]))
    p_both = 1.0 - stats.norm.cdf(zs) - stats.norm.cdf(zr) + phi2
    p_either = 1.0 - phi2
    return p_both, p_either


def main():
    section("1. Compound coastal flooding")
    p_both_0, p_either_0 = compound_probability(0.0)
    p_both_1, p_either_1 = compound_probability(SLR_M)
    print(f"  SYNTHETIC drivers: storm surge lognormal median "
          f"{SURGE_MEDIAN:.2f} m,")
    print(f"  log-sigma {SURGE_SIGMA:.2f}; river stage lognormal median "
          f"{RIVER_MEDIAN:.2f} m, log-sigma {RIVER_SIGMA:.2f}")
    print(f"  correlation (Gaussian copula) rho = {RHO:.2f}")
    print(f"  thresholds: defence level {SURGE_THRESHOLD:.2f} m, river stage "
          f"{RIVER_THRESHOLD:.2f} m")
    print(f"  scenario          P(both)      P(either)    1/ P(both) (yr)")
    print(f"  no sea-level rise {p_both_0:.5f}    {p_either_0:.5f}    "
          f"{1.0 / p_both_0:12.1f}")
    print(f"  +{SLR_M:.2f} m sea level  {p_both_1:.5f}    {p_either_1:.5f}    "
          f"{1.0 / p_both_1:12.1f}")
    print(f"  ratio after/before: {p_both_1 / p_both_0:.2f}x for the joint")
    print(f"  event, {p_either_1 / p_either_0:.2f}x for either.")
    print("  Both grow, and the joint event's return period falls from")
    print(f"  {1.0 / p_both_0:.1f} to {1.0 / p_both_1:.1f} years.  Note that the")
    print("  two ratios are not equal, and neither equals the ratio of the")
    print("  marginals: with fixed thresholds and a shift of one driver, every")
    print("  summary of the hazard has its own sensitivity.")

    section("2. Return period of the compound event")
    print("  sea-level rise (m)   P(both)       return period (yr)   "
          "factor vs today")
    for slr in (0.0, 0.2, 0.5, 0.8, 1.0):
        p, _ = compound_probability(slr)
        print(f"  {slr:18.2f}   {p:.5f}   {1.0 / p:18.1f}   "
              f"{p / p_both_0:14.2f}x")
    print("  The same defence structure, unchanged, experiences a compound event")
    print("  far more often: the hazard has moved, not the asset.  This is the")
    print("  mechanism by which a modest mean change becomes a large change in")
    print("  risk -- the design point sits in the tail.")

    section("3. Permafrost thaw settlement")
    print(f"  SYNTHETIC soil column: excess ice content {EXCESS_ICE:.2f}")
    print(f"  (volume fraction), active layer {THAW_DEPTH_NOW:.1f} m now and")
    print(f"  {THAW_DEPTH_WARM:.1f} m in the warmer scenario")
    d_thaw = THAW_DEPTH_WARM - THAW_DEPTH_NOW
    settlement = EXCESS_ICE * d_thaw
    print(f"  newly thawed thickness      : {d_thaw:.2f} m")
    print(f"  settlement (ice lost, excess ice fraction): "
          f"{EXCESS_ICE:.2f} x {d_thaw:.2f} = {settlement:.3f} m")
    print(f"  as a fraction of a road embankment of 1.0 m height: "
          f"{settlement / 1.0:.0%}")
    print("  settlement is a direct, geometric consequence of melting excess ice:")
    print("  it is not a small effect for infrastructure, and it is differential")
    print("  (varying with ice content), which is what damages structures.")
    print(f"  sensitivity: a thaw depth of {THAW_DEPTH_NOW + 0.4:.1f} m instead")
    print(f"  of {THAW_DEPTH_WARM:.1f} m gives "
          f"{EXCESS_ICE * 0.4:.3f} m of settlement --")
    print("  the displacement scales linearly with the newly thawed thickness.")

    section("4. Slope stability as pore pressure rises")
    beta = np.deg2rad(BETA_DEG)
    phi = np.deg2rad(PHI_FRICTION)
    # infinite-slope factor of safety with pore-pressure ratio ru = u/(gamma z)
    print(f"  infinite-slope model: gamma = {GAMMA / 1e3:.1f} kN/m^3, "
          f"c' = {COHESION / 1e3:.1f} kPa,")
    print(f"  phi' = {PHI_FRICTION:.1f} deg, slope {BETA_DEG:.1f} deg, "
          f"slab thickness {Z_SLAB:.1f} m")
    print("  ru (pore-pressure ratio)   factor of safety   state")
    ru_critical = None
    for ru in (0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6):
        cohesion_term = COHESION / (GAMMA * Z_SLAB * np.sin(beta) * np.cos(beta))
        fric_term = (np.cos(beta) ** 2 * (1.0 - ru) * np.tan(phi)) / \
            (np.sin(beta) * np.cos(beta))
        fos = cohesion_term + fric_term
        state = "stable" if fos > 1.0 else "FAILURE"
        print(f"  {ru:24.2f}   {fos:17.3f}   {state}")
        if ru_critical is None and fos <= 1.0:
            ru_critical = ru
    print(f"  the factor of safety crosses one between ru = "
          f"{ru_critical - 0.1:.1f} and {ru_critical:.1f}")
    print("  A thaw or a wetter period raises ru; the crossing point is where a")
    print("  geohazard becomes a landslide.  The relevant climate statement is")
    print("  about the *probability of reaching that ru*, not about the slope:")
    print("  the slope has no probability, the pore pressure does.")

    section("5. The counterfactual each statement requires")
    print("  A defensible climate-geohazard statement names:")
    print(f"  1. the hazard metric and threshold (here: surge > "
          f"{SURGE_THRESHOLD:.2f} m and river > {RIVER_THRESHOLD:.2f} m;")
    print(f"     or ru > {ru_critical - 0.1:.1f} for the slope);")
    print("  2. the counterfactual: the same distributions with the mean sea")
    print("     level (or the thaw depth, or the precipitation regime) set to the")
    print("     pre-change value, everything else equal;")
    print("  3. the probabilistic statement with its uncertainty: the joint")
    print(f"     exceedance probability rises from {p_both_0:.5f} to "
          f"{p_both_1:.5f} under the stated shift;")
    print("  4. the exposure and vulnerability, which are separate from the")
    print("     hazard and usually dominate the loss (see 16-07-04).")
    print("  All numbers above are SYNTHETIC.")


if __name__ == "__main__":
    main()
