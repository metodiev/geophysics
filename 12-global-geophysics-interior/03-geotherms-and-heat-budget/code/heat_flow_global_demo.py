#!/usr/bin/env python3
"""Global heat flow and its distribution.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python heat_flow_global_demo.py

Everything here is a SYNTHETIC teaching model.  The sea-floor age distribution,
the province heat-flow values and the rock properties are *adopted inputs*
chosen to be representative; none is a measurement at a place, and no real
borehole, survey or station is used.

Contents
--------
1. Half-space cooling: the heat-flow-age law and the q*sqrt(t) invariant.
2. The plate model: where the half-space model fails and by how much.
3. Inverting heat flow for age, and the error amplification that comes with it.
4. Global heat loss from a synthetic sea-floor age distribution.
5. The near-ridge heat-flow deficit and the advective transport it implies.
6. Continental heat-flow provinces: recovering the reduced heat flow and the
   depth scale, with the uncertainty the regression actually carries.
7. Verification: series convergence, the small-age limit, and the regression
   against a direct linear solve.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- adopted thermal and geometric inputs (synthetic teaching model) ---------
K_ROCK = 3.0            # W m^-1 K^-1, lithospheric thermal conductivity
KAPPA = 1.0e-6          # m^2 s^-1, thermal diffusivity
DT_LITH = 1300.0        # K, mantle-to-surface temperature contrast
PLATE_D_KM = 90.0       # km, adopted asymptotic plate thickness (plate model)
A_OCEAN = 3.6e14        # m^2, adopted sea-floor area (nominal)
A_CONT = 2.0e14         # m^2, adopted continental area (nominal)
Q_CONT = 65.0           # mW m^-2, adopted continental mean heat flow (nominal)
S_MA = 3.1557e13        # s per million years (365.25 d/yr)
MYR = 1.0e6


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def q_halfspace(t_ma, k=K_ROCK, kappa=KAPPA, dt=DT_LITH):
    """Surface heat flow of a cooling half-space, in mW/m^2, age in Myr."""
    t = np.asarray(t_ma, dtype=float) * S_MA
    return k * dt / np.sqrt(np.pi * kappa * t) * 1.0e3


def q_plate(t_ma, d_km=PLATE_D_KM, n_terms=60, k=K_ROCK, kappa=KAPPA, dt=DT_LITH):
    """Plate-model surface heat flow, in mW/m^2, plate base at fixed temperature.

    q = (k*dT/d) * [1 + 2 * sum_{n=1..N} exp(-n^2 pi^2 kappa t / d^2)]
    """
    t = np.atleast_1d(np.asarray(t_ma, dtype=float)) * S_MA
    d = d_km * 1.0e3
    n = np.arange(1, n_terms + 1)
    s = 2.0 * np.exp(-np.outer(n**2, t) * np.pi**2 * kappa / d**2).sum(axis=0)
    out = k * dt / d * (1.0 + s) * 1.0e3
    return float(out[0]) if np.ndim(t_ma) == 0 else out


def q_age_coefficient():
    """The constant q*sqrt(age), in mW/m^2 per Ma^0.5, for the adopted parameters."""
    return K_ROCK * DT_LITH / np.sqrt(np.pi * KAPPA * S_MA) * 1.0e3


def main():
    section("1. Half-space cooling: q(t) and the q*sqrt(t) invariant")
    print(f"adopted: k = {K_ROCK:.1f} W m^-1 K^-1, kappa = {KAPPA * 1e6:.1f}e-6 m^2/s,"
          f" dT = {DT_LITH:.0f} K")
    print("  age (Ma)   q_halfspace (mW/m^2)   q*sqrt(age) (mW/m^2 * Ma^0.5)"
          "   plate thickness 2*sqrt(kappa*t) (km)")
    ages = np.array([1.0, 2.0, 5.0, 10.0, 20.0, 40.0, 80.0, 120.0, 160.0])
    for t in ages:
        q = float(q_halfspace(t))
        d_km = 2.0 * np.sqrt(KAPPA * t * S_MA) / 1.0e3
        print(f"  {t:8.0f}   {q:18.1f}   {q * np.sqrt(t):29.1f}   {d_km:26.1f}")
    print(f"\ninvariant q*sqrt(t) = k*dT/sqrt(pi*kappa*S_MA) = "
          f"{q_age_coefficient():.1f} mW/m^2 per Ma^0.5")
    spread = float(np.max(q_halfspace(ages) * np.sqrt(ages))
                   - np.min(q_halfspace(ages) * np.sqrt(ages)))
    print(f"measured spread of that column across 1-160 Ma: {spread:.2e} mW/m^2"
          " (zero by construction: q*sqrt(t) is a constant of the model)")

    section("2. The plate model and where the half-space model fails")
    print(f"adopted plate thickness d = {PLATE_D_KM:.0f} km ->"
          f" asymptotic flux k*dT/d = {K_ROCK * DT_LITH / (PLATE_D_KM * 1e3) * 1e3:.1f} mW/m^2")
    print("  age (Ma)   q_halfspace   q_plate   plate/half-space")
    for t in (1.0, 5.0, 20.0, 40.0, 80.0, 120.0, 160.0):
        qh = float(q_halfspace(t))
        qp = q_plate(t)
        print(f"  {t:8.0f}   {qh:11.1f}   {qp:7.1f}   {qp / qh:16.3f}")
    print(f"\nhalf-space plate thickness at 160 Ma = "
          f"{2 * np.sqrt(KAPPA * 160 * S_MA) / 1e3:.0f} km, against the adopted"
          f" {PLATE_D_KM:.0f} km: the two models disagree about the plate itself")

    section("3. Inverting heat flow for age")
    coeff = q_age_coefficient()   # mW/m^2 per Ma^0.5
    print(f"age t = (q*sqrt(t)/q)^2 with q*sqrt(t) = {coeff:.1f} mW/m^2 per Ma^0.5")
    print("  true age (Ma)   q (mW/m^2)   dq = 5 -> dt (Ma)   relative dt/t")
    for t in (5.0, 20.0, 60.0):
        q = float(q_halfspace(t))
        t_plus = (coeff / q) ** 2
        t_minus = (coeff / (q - 5.0)) ** 2
        print(f"  {t:14.0f}   {q:11.1f}   {t_minus - t_plus:16.1f}   "
              f"{(t_minus - t_plus) / t:13.3f}")
    print("dt/t = 2*dq/q exactly, so the age is twice as uncertain as the flux;"
          " on young crust that is cheap, on old crust it is not")

    section("4. Global heat loss from a synthetic sea-floor age distribution")
    edges = np.array([0.0, 2.0, 5.0, 10.0, 20.0, 30.0, 50.0, 80.0, 120.0, 180.0])
    mids = 0.5 * (edges[:-1] + edges[1:])
    # adopted age-distribution weights: a realistic-looking, area-weighted
    # distribution of sea-floor age, concentrated in the 10-80 Ma range
    weights = np.array([0.015, 0.030, 0.070, 0.140, 0.120, 0.200, 0.200,
                        0.120, 0.105])
    weights = weights / weights.sum()
    area_frac = weights
    area = area_frac * A_OCEAN
    q_hs = q_halfspace(mids)
    q_pl = q_plate(mids)
    loss_hs = float(np.sum(q_hs * 1.0e-3 * area)) / 1.0e12
    loss_pl = float(np.sum(q_pl * 1.0e-3 * area)) / 1.0e12
    print("  age bin (Ma)   area (1e14 m^2)   q_halfspace   q_plate   (mW/m^2)")
    for i in range(len(mids)):
        print(f"  {edges[i]:5.0f}-{edges[i + 1]:<5.0f}   {area[i] / 1e14:14.3f}"
              f"   {q_hs[i]:11.1f}   {q_pl[i]:7.1f}")
    print(f"\noceanic heat loss, half-space model : {loss_hs:.1f} TW")
    print(f"oceanic heat loss, plate model      : {loss_pl:.1f} TW"
          f"  ({(1 - loss_pl / loss_hs) * 100:.1f}% less)")
    cont_tw = Q_CONT * 1.0e-3 * A_CONT / 1.0e12
    print(f"continental heat loss, {Q_CONT:.0f} mW/m^2 over {A_CONT / 1e14:.1f}e14 m^2"
          f" = {cont_tw:.1f} TW")
    print(f"total, plate model + continents     : {loss_pl + cont_tw:.1f} TW")
    print(f"area-weighted mean over the whole surface:"
          f" {(loss_pl + cont_tw) / ((A_OCEAN + A_CONT) / 1e12) * 1e3:.1f} mW/m^2")
    young = mids <= 20.0
    print(f"the {area[young].sum() / A_OCEAN * 100:.0f}% of sea floor younger than"
          f" 20 Ma carries {np.sum(q_pl[young] * 1e-3 * area[young]) / 1e12 / loss_pl * 100:.0f}%"
          " of the oceanic loss")

    section("5. The near-ridge deficit and advective transport")
    print("adopted measured/model ratio r(t) = 1 - 0.8*exp(-t/8 Ma): conduction"
          " misses the heat near the ridge")
    deficit = 0.0
    print("  age bin (Ma)   r(t)   deficit (TW)")
    for i in range(len(mids)):
        r = 1.0 - 0.8 * np.exp(-mids[i] / 8.0)
        d_tw = float((1.0 - r) * q_pl[i] * 1.0e-3 * area[i]) / 1.0e12
        deficit += d_tw
        print(f"  {edges[i]:5.0f}-{edges[i + 1]:<5.0f}   {r:5.3f}   {d_tw:11.2f}")
    print(f"\ntotal deficit = {deficit:.1f} TW = {deficit / loss_pl * 100:.0f}% of the"
          " plate-model oceanic loss")
    print(f"this is heat carried by water, not by conduction: it is why a"
          f" 'heat flow map' near a ridge is a map of hydrothermal circulation")

    section("6. Continental heat-flow provinces")
    a0 = np.array([0.4, 0.7, 1.0, 1.4, 1.9, 2.5])      # uW/m^3, adopted
    q_true = 40.0 + 10.0 * a0                            # reduced flow 40, h = 10 km
    noise = RNG.normal(0.0, 4.0, size=a0.size)           # mW/m^2, scatter
    q_obs = q_true + noise
    slope, intercept = np.polyfit(a0, q_obs, 1)
    resid = q_obs - (intercept + slope * a0)
    dof = a0.size - 2
    s2 = float(np.sum(resid**2) / dof)
    sxx = float(np.sum((a0 - a0.mean()) ** 2))
    se_slope = np.sqrt(s2 / sxx)
    se_int = np.sqrt(s2 * (1.0 / a0.size + a0.mean() ** 2 / sxx))
    t_crit = 2.776                                        # t(0.975, 4 dof)
    print("  A0 (uW/m^3)   q_true   noise   q_observed (mW/m^2)")
    for i in range(a0.size):
        print(f"  {a0[i]:11.1f}   {q_true[i]:7.1f}   {noise[i]:+5.1f}   {q_obs[i]:9.1f}")
    print(f"\nleast-squares fit: q = q_reduced + A0*h")
    print(f"  reduced heat flow q_reduced = {intercept:.1f} +/- {t_crit * se_int:.1f} mW/m^2"
          f"  (adopted 40.0)")
    print(f"  slope A0*h-scale = {slope:.1f} +/- {t_crit * se_slope:.1f} km"
          f"  (adopted 10.0 km)")
    print(f"  the fit recovers h = {slope:.1f} km, i.e. a 95% interval of"
          f" [{slope - t_crit * se_slope:.1f}, {slope + t_crit * se_slope:.1f}] km")
    print("  note what the regression assumes: that every province shares one"
          " q_reduced and one h, and that A0 is known without error")

    section("7. Verification")
    q_terms = q_plate(20.0, n_terms=5) - q_plate(20.0, n_terms=200)
    print(f"plate-model series: 5 terms vs 200 terms at 20 Ma differ by"
          f" {float(q_terms):.3e} mW/m^2")
    ratio = float(q_plate(0.5) / q_halfspace(0.5))
    print(f"plate/half-space at 0.5 Ma (t << d^2/kappa): {ratio:.4f}"
          " -> the two models must agree when cooling has not reached the base")
    d2_kappa = (PLATE_D_KM * 1e3) ** 2 / KAPPA / S_MA
    print(f"the base is reached at t = d^2/kappa = {d2_kappa:.1f} Ma, so agreement"
          " at 0.5 Ma is expected and disagreement at 160 Ma is inevitable")
    direct = np.linalg.lstsq(np.vstack([np.ones_like(a0), a0]).T, q_obs, rcond=None)[0]
    print(f"regression cross-check: polyfit intercept {intercept:.6f} vs normal"
          f" equations {direct[0]:.6f} mW/m^2")
    print(f"regression cross-check: polyfit slope     {slope:.6f} vs normal"
          f" equations {direct[1]:.6f} km")
    print("\nSYNTHETIC teaching model; no measured value is used anywhere above.")


if __name__ == "__main__":
    main()
