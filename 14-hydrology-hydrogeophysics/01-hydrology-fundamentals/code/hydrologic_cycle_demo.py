#!/usr/bin/env python3
"""The hydrologic cycle as a store-and-flux accounting: water balance closure,
the cancellation problem, unit conversions, residence time, and baseflow
separation on a SYNTHETIC daily hydrograph.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python hydrologic_cycle_demo.py

Everything here is SYNTHETIC.  The catchment, the rainfall series and the daily
discharge series are invented teaching values, not measurements of any real
basin.  No real gauge, aquifer or published inventory is used.

Contents
--------
1. Annual water balance of a synthetic catchment, closed and reported in mm.
2. Error amplification: why delta S is the hardest term to measure.
3. Unit conversions for depth-of-water (mm) over a catchment area.
4. Residence time of a synthetic groundwater store.
5. Baseflow separation with a first-order low-pass, and how the answer
   depends on the time constant chosen.
6. Verification: recovery of the storage constant from a recession curve.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC catchment (chosen teaching values, not measurements) ----------
AREA_KM2 = 250.0        # catchment area
P_MM = 850.0            # annual precipitation depth
ET_MM = 480.0           # annual evapotranspiration depth
Q_MM = 320.0            # annual streamflow depth (runoff)
GW_STORAGE_M3 = 1.5e8   # stored groundwater volume of the synthetic catchment
TAU_TRUE_D = 30.0       # true linear-reservoir constant of the synthetic basin
N_DAYS = 365


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def mm_to_volume_m3(depth_mm, area_km2):
    """Depth of water in mm over an area in km^2, returned in m^3.

    1 mm over 1 km^2 = 1e-3 m * 1e6 m^2 = 1e3 m^3 exactly.
    """
    return depth_mm * 1.0e-3 * area_km2 * 1.0e6


def synthetic_hydrograph(n_days, tau_d, seed_rng):
    """Daily precipitation and discharge from a single linear reservoir.

    Storage S is in mm of water over the catchment.  Each day:
        S <- S + P_eff - Q,      Q = S / tau_d
    A fraction of the daily rainfall becomes effective runoff; the rest is a
    loss to evapotranspiration.  This is a teaching model, not a hydrological
    model of any real basin.
    """
    day = np.arange(n_days)
    seasonal = 0.5 * (1.0 + np.cos(2.0 * np.pi * (day - 15.0) / 365.0))
    wet = RNG.gamma(shape=1.4, scale=1.0, size=n_days)
    precip = 6.0 * seasonal * wet
    p_eff = 0.45 * precip
    q = np.zeros(n_days)
    s = 5.0
    for i in range(n_days):
        s += p_eff[i]
        q[i] = s / tau_d
        s -= q[i]
    return precip, p_eff, q


def lowpass_1st_order(q, dt_d, tau_filter_d):
    """First-order low-pass of a discharge series, clipped to the hydrograph."""
    alpha = np.exp(-dt_d / tau_filter_d)
    h = np.zeros_like(q)
    for i in range(q.size):
        h[i] = alpha * h[i - 1] + (1.0 - alpha) * q[i] if i else (1.0 - alpha) * q[i]
    return np.minimum(h, q)


def main():
    section("1. Annual water balance of a SYNTHETIC catchment")
    print(f"SYNTHETIC catchment: area = {AREA_KM2:.0f} km^2")
    print(f"  precipitation        P  = {P_MM:8.1f} mm/yr")
    print(f"  evapotranspiration   ET = {ET_MM:8.1f} mm/yr")
    print(f"  streamflow (runoff)  Q  = {Q_MM:8.1f} mm/yr")
    dS = P_MM - ET_MM - Q_MM
    print(f"  storage change       dS = P - ET - Q = {dS:8.1f} mm/yr")
    print(f"  runoff coefficient   Q/P  = {Q_MM / P_MM:.3f}  (dimensionless)")
    print(f"  evaporative index    ET/P = {ET_MM / P_MM:.3f}  (dimensionless)")
    print(f"  closure check        |P - (ET + Q + dS)| = "
          f"{abs(P_MM - (ET_MM + Q_MM + dS)):.2e} mm/yr")
    print(f"  as volumes: P  = {mm_to_volume_m3(P_MM, AREA_KM2):.4e} m^3/yr")
    print(f"              Q  = {mm_to_volume_m3(Q_MM, AREA_KM2):.4e} m^3/yr")
    print(f"              dS = {mm_to_volume_m3(dS, AREA_KM2):.4e} m^3/yr "
          f"(a surplus: the store gains {dS:.0f} mm this year)")
    sec_per_year = 365.25 * 86400.0
    q_vol_rate = mm_to_volume_m3(Q_MM, AREA_KM2) / sec_per_year
    print(f"  mean discharge at the outlet: {q_vol_rate:.3f} m^3/s "
          f"= {q_vol_rate * 1e3:.1f} L/s")
    print(f"  (1 Julian year = 365.25 x 86400 s = {sec_per_year:.0f} s exactly)")

    section("2. Error amplification in a residual term")
    print("The balance is a difference of large numbers, so a small relative")
    print("error in a large term becomes a large relative error in dS.")
    print(f"  dS itself                 = {dS:.1f} mm/yr")
    for name, val, err_frac in (("P", P_MM, 0.05), ("ET", ET_MM, 0.10), ("Q", Q_MM, 0.05)):
        # dS = P - ET - Q: an error in ET enters with the opposite sign
        d = val * err_frac
        print(f"  {name:2s} = {val:7.1f} +/- {d:5.1f} mm/yr ({err_frac * 100:.0f}%) "
              f"-> dS shift {(-d if name != 'P' else d):+7.1f} mm/yr "
              f"({abs(d) / dS * 100:5.1f}% of dS)")
    print(f"  amplification factor for Q: |dQ| / |dS| = "
          f"{0.05 * Q_MM / dS:.2f}  (measure Q to 1% to get dS to "
          f"{0.01 * Q_MM / dS * 100:.0f}%)")

    section("3. Depth of water to volume: 1 mm over 1 km^2 = 1000 m^3 exactly")
    print("   area (km^2)    1 mm (m^3)   100 mm (m^3)   1 m (m^3)")
    for a in (1.0, 10.0, 100.0, 1000.0):
        print(f"   {a:11.0f}   {mm_to_volume_m3(1.0, a):10.3e}   "
              f"{mm_to_volume_m3(100.0, a):10.3e}   {mm_to_volume_m3(1000.0, a):10.3e}")
    print(f"  a 1 mm/yr change over this catchment = "
          f"{mm_to_volume_m3(1.0, AREA_KM2):.3e} m^3/yr")

    section("4. Residence time of the synthetic groundwater store")
    q_vol = mm_to_volume_m3(Q_MM, AREA_KM2)
    tau_res = GW_STORAGE_M3 / q_vol
    print(f"  groundwater storage V = {GW_STORAGE_M3:.3e} m^3")
    print(f"  annual discharge Q     = {q_vol:.3e} m^3/yr")
    print(f"  mean residence time tau = V / Q = {tau_res:.3f} yr "
          f"= {tau_res * 365.25:.1f} d")

    section("5. Baseflow separation: a definition, not a measurement")
    precip, p_eff, q = synthetic_hydrograph(N_DAYS, TAU_TRUE_D, RNG)
    print(f"SYNTHETIC daily series: {N_DAYS} days, mean P = {precip.mean():.2f} mm/d,")
    print(f"  mean discharge = {q.mean():.3f} mm/d, peak = {q.max():.3f} mm/d")
    print(f"  total discharge = {q.sum():.1f} mm over the year")
    print("\n   filter tau (d)   baseflow index   baseflow (mm/yr)   stormflow (mm/yr)")
    for tau_f in (5.0, 10.0, 30.0, 60.0, 120.0):
        qb = lowpass_1st_order(q, 1.0, tau_f)
        bfi = qb.sum() / q.sum()
        print(f"   {tau_f:13.1f}   {bfi:14.3f}   {qb.sum():15.1f}   "
              f"{q.sum() - qb.sum():16.1f}")
    print("  The separation is defined by the time constant, so the baseflow index")
    print("  is a modelling choice unless the time constant is fixed by a tracer or")
    print("  by a stated recession constant.")

    section("6. Verification: recover the storage constant from a recession")
    qb = lowpass_1st_order(q, 1.0, TAU_TRUE_D)
    dry = np.where((p_eff < 0.2) & (q > 1e-3))[0]
    runs, current = [], []
    for i in range(N_DAYS):
        if i in set(dry.tolist()):
            current.append(i)
        else:
            if len(current) >= 12:
                runs.append(current)
            current = []
    if len(current) >= 12:
        runs.append(current)
    seg = runs[len(runs) // 2]
    t = np.arange(seg[0], seg[-1] + 1, dtype=float)
    qs = q[seg[0]:seg[-1] + 1]
    slope, intercept = np.polyfit(t, np.log(qs), 1)
    tau_fit = -1.0 / slope
    print(f"  longest clean recession used: days {seg[0]} to {seg[-1]} "
          f"({len(seg)} days)")
    print(f"  fit ln Q = a + b t :  b = {slope:+.5f} 1/d -> tau = {-1.0 / slope:.2f} d")
    print(f"  true storage constant of the synthetic basin = {TAU_TRUE_D:.2f} d")
    print(f"  relative error = {abs(tau_fit - TAU_TRUE_D) / TAU_TRUE_D * 100:.1f}%")
    print("  check: Q(t) = Q0 exp(-t/tau) has slope -1/tau, so the recession")
    print("  constant IS the reservoir time constant.  The recovery is only")
    print("  approximate because the chosen window is not perfectly rain-free.")
    print(f"  drainable storage implied by tau and mean Q: "
          f"{tau_fit * q.mean():.2f} mm over the catchment")


if __name__ == "__main__":
    main()
