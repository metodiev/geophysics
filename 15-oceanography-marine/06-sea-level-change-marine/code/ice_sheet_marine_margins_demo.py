#!/usr/bin/env python3
"""Ice sheet marine margins: flotation, the grounding-line flux law, the marine
ice sheet instability, and the effect of losing ice-shelf buttressing.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python ice_sheet_marine_margins_demo.py

Everything here is SYNTHETIC.  The ice sheet, its bed and the ice shelf are
teaching models with the stated model constants.  No real ice sheet, glacier,
shelf, catchment or survey is referenced, and no number is quoted from a published
measurement.

Contents
--------
1. Flotation: the grounding-line thickness for a given water depth.
2. The grounding-line flux from the shallow-ice approximation with Glen's law,
   and the h^5 dependence.
3. The marine ice sheet instability: a retrograde bed, the flux excess, and the
   retreat rate.
4. Ice-shelf buttressing: the back stress, the inland shift for a given
   buttressing loss, and the melt-versus-accumulation competition.
5. Worked examples used in the lesson.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

RHO_ICE = 917.0          # kg/m^3
RHO_SW = 1028.0          # kg/m^3
G = 9.80665
A_GLEN = 2.4e-24         # Pa^-3 s^-1, model value for the flow-rate factor
N_GLEN = 3.0             # Glen's law exponent
SEC_PER_YR = 3.15576e7


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def flotation_thickness(depth_m):
    """Grounding-line thickness at flotation for a given water depth, m."""
    return RHO_SW / RHO_ICE * depth_m


def flux_deformation(h_m, alpha, A=A_GLEN, n=N_GLEN):
    """Depth-integrated flux (m^2/s) from internal deformation, shallow-ice approx."""
    return 2.0 * A / (n + 2.0) * (RHO_ICE * G * alpha) ** n * h_m ** (n + 2.0)


def flux_per_yr(h_m, alpha):
    return flux_deformation(h_m, alpha) * SEC_PER_YR


def main():
    section("1. Flotation at the grounding line")
    ratio = RHO_SW / RHO_ICE
    print(f"  densities: ice {RHO_ICE:.0f}, seawater {RHO_SW:.0f} kg/m^3")
    print(f"  flotation: h_g = (rho_sw/rho_ice) d = {ratio:.4f} d")
    print("\n   water depth d (m)   grounding-line thickness h_g (m)   freeboard (m)")
    for d in (200.0, 500.0, 800.0, 1000.0, 1500.0):
        h = flotation_thickness(d)
        print(f"   {d:17.0f}   {h:32.1f}   {h - d:12.1f}")
    print("  the freeboard is about 12% of the thickness: an ice sheet grounded in")
    print("  deeper water is thicker in direct proportion, and that is the coupling")
    print("  that makes the bed geometry so important.")

    section("2. The grounding-line flux law")
    alpha = 0.01
    print(f"  shallow-ice approximation with Glen's law (n = {N_GLEN:.0f}):")
    print("    u = 2A/(n+2) (rho_i g alpha)^n h^(n+1)")
    print("    q = u h = 2A/(n+2) (rho_i g alpha)^n h^(n+2)")
    print(f"  model constants: A = {A_GLEN:.2e} Pa^-3 s^-1, surface slope "
          f"alpha = {alpha:.3f}")
    print(f"    rho_i g alpha = {RHO_ICE * G * alpha:.2f} Pa/m")
    print("\n   h (m)   q (m^2/yr)   q/q(1000 m)")
    for h in (600.0, 800.0, 1000.0, 1200.0, 1500.0):
        q = flux_per_yr(h, alpha)
        print(f"   {h:6.0f}   {q:11.0f}   {q / flux_per_yr(1000.0, alpha):11.3f}")
    print(f"  the exponent is n+2 = {N_GLEN + 2:.0f}, so a 20% thicker ice")
    print(f"  discharges {(1.2 ** (N_GLEN + 2) - 1) * 100:.0f}% more: the flux is")
    print("  violently sensitive to thickness, which is the origin of the")
    print("  instability in the next section.")

    a_acc, W = 0.3, 200e3
    q_supply = a_acc * W
    h_eq = 1000.0 * (q_supply / flux_per_yr(1000.0, alpha)) ** (1.0 / (N_GLEN + 2))
    print(f"\n  balance for a catchment of width {W / 1e3:.0f} km with "
          f"accumulation {a_acc:.1f} m/yr:")
    print(f"    supply per unit width = a W = {q_supply:.0f} m^2/yr")
    print(f"    equilibrium thickness h = 1000 x (q/q(1000))^(1/5) = {h_eq:.1f} m")
    print(f"    equilibrium water depth = h/1.121 = "
          f"{flotation_thickness(h_eq / ratio) / ratio:.0f} m "
          f"(i.e. {h_eq / ratio:.0f} m)")

    section("3. The marine ice sheet instability")
    d0 = h_eq / ratio
    slope = 0.01          # bed deepening inland, m per m (retrograde)
    print(f"  a retrograde bed: the water depth increases inland at "
          f"{slope * 1e3:.0f} m/km")
    print(f"  starting at d = {d0:.0f} m (h = {h_eq:.1f} m, q = "
          f"{flux_per_yr(h_eq, alpha):.0f} m^2/yr)")
    print("\n   retreat (km)   water depth (m)   h (m)   q (m^2/yr)   excess over supply")
    for dx_km in (0.0, 5.0, 10.0, 20.0, 40.0):
        d = d0 + slope * dx_km * 1e3
        h = flotation_thickness(d)
        q = flux_per_yr(h, alpha)
        print(f"   {dx_km:12.0f}   {d:15.0f}   {h:7.1f}   {q:11.0f}   "
              f"{q - q_supply:17.0f}")
    dz = 10e3
    d1, d2 = d0 + slope * dz, d0 + slope * (dz + 1000.0)
    q1, q2 = flux_per_yr(flotation_thickness(d1), alpha), \
        flux_per_yr(flotation_thickness(d2), alpha)
    dqdx = (q2 - q1) / 1000.0
    excess = q1 - q_supply
    dist = excess / dqdx
    print(f"\n  at 10 km of retreat the flux exceeds the supply by "
          f"{excess:.0f} m^2/yr.")
    print(f"  Moving the grounding line 1 m further into the deeper water raises")
    print(f"  the flux by dq/dx = {dqdx:.2f} m^2/yr, so the retreat required to")
    print(f"  restore the balance is")
    print(f"    excess / (dq/dx) = {dist:.0f} m = {dist / 1e3:.1f} km.")
    print("  But the table shows the excess GROWING with retreat (33,061 at")
    print("  10 km, 79,312 at 20 km), so that disequilibrium distance grows too:")
    print("  there is no nearby equilibrium on this bed.  The model's honest")
    print("  output is not a retreat rate but the statement that a steady state")
    print("  does not exist for this geometry, and the retreat continues until")
    print("  the bed shallows, lateral drag rises, or the catchment shrinks")
    print("  enough to cut the supply.")
    print("\n  sensitivity to the bed slope (through dq/dx):")
    print("   bed slope (m/km)   excess at 10 km (m^2/yr)   disequilibrium distance (km)")
    for s_km in (5.0, 10.0, 20.0):
        sl = s_km / 1000.0
        d_a = d0 + sl * dz
        d_b = d0 + sl * (dz + 1000.0)
        qa = flux_per_yr(flotation_thickness(d_a), alpha)
        qb = flux_per_yr(flotation_thickness(d_b), alpha)
        dq = (qb - qa) / 1000.0
        print(f"   {s_km:17.0f}   {qa - q_supply:27.0f}   "
              f"{(qa - q_supply) / dq / 1e3:28.1f}")
    print("  a flatter bed retreats further for the same imbalance, and a bed")
    print("  that shallows inland (a prograde slope) reverses the sign and")
    print("  stabilises the margin: that is the classical stability criterion.")

    section("4. Buttressing, and the melt-versus-accumulation competition")
    h_shelf, d_shelf = 500.0, 560.0
    back = RHO_ICE * G * h_shelf * (1.0 - RHO_ICE / RHO_SW) / 2.0
    drive = RHO_ICE * G * h_shelf * alpha
    print(f"  for a thickness h = {h_shelf:.0f} m, the unconfined shelf's")
    print("  longitudinal back stress and the driving stress are compared like")
    print("  for like, at the SAME thickness:")
    print(f"    rho_i g h (1 - rho_i/rho_sw)/2 = {back / 1e6:.3f} MPa")
    print(f"    rho_i g h alpha                = {drive / 1e6:.4f} MPa")
    print(f"  ratio = {back / drive:.2f}; analytically the ratio is")
    print("  (1 - rho_i/rho_sw)/(2 alpha), so it is INDEPENDENT of thickness:")
    for a_ratio in (0.005, 0.010, 0.020):
        print(f"    alpha = {a_ratio:.3f} -> ratio "
              f"{(1.0 - RHO_ICE / RHO_SW) / (2.0 * a_ratio):.2f}")
    print("  an unconfined shelf therefore already exerts several times the")
    print("  driving stress.  What decides whether a margin holds is the")
    print("  ADDITIONAL resistance from lateral drag and pinning points, which")
    print("  is why the sensitivity is expressed through beta below rather than")
    print("  through the mere presence or absence of a shelf.")
    print(f"  (the equilibrium thickness at the grounding line, {h_eq:.0f} m, is")
    print(f"  {h_eq / h_shelf:.1f}x the shelf thickness, so a comparison made at")
    print("  different thicknesses would not be like for like.)")
    print("\n  effect of a buttressing loss on the equilibrium position (the flux")
    print("  must stay at the supply, so h must rise by (1/(1-beta))^(1/5)):")
    print("   buttressing beta   h required (m)   water depth (m)   inland shift (km)")
    for beta in (0.0, 0.2, 0.4, 0.6):
        h_req = h_eq * (1.0 / (1.0 - beta)) ** (1.0 / 5.0)
        d_req = h_req / ratio
        print(f"   {beta:16.1f}   {h_req:15.1f}   {d_req:15.0f}   "
              f"{(d_req - d0) / (slope * 1000):17.1f}")
    print("  the position is sensitive even though the flux is only weakly")
    print("  sensitive: the geometry absorbs the buttressing change, so losing")
    print("  60% of the buttressing moves the grounding line tens of kilometres")
    print("  inland without changing the flux much.")

    shelf_len, melt = 50e3, 10.0
    loss = melt * shelf_len
    print(f"\n  melt versus accumulation for a {shelf_len / 1e3:.0f} km shelf:")
    print(f"    accumulation supply = a W = {q_supply:.0f} m^2/yr")
    print(f"    basal melt of {melt:.0f} m/yr over {shelf_len / 1e3:.0f} km = "
          f"{loss:.0f} m^2/yr")
    print(f"    melt/accumulation = {loss / q_supply:.1f}")
    shelf_vol = h_shelf * shelf_len
    print(f"  the shelf's volume per unit width is {shelf_vol:.2e} m^2, so at that")
    print(f"  melt rate it would disappear in {shelf_vol / loss:.0f} yr unless the")
    print("  flow accelerates.  This is the competition that determines whether a")
    print("  marine margin retreats slowly by geometry or quickly by shelf loss.")

    section("5. Worked examples used in the lesson")
    print(f"(a) grounding line in 1000 m of water: h = {flotation_thickness(1000.0):.0f} m")
    print(f"(b) q(1000 m) = {flux_per_yr(1000.0, alpha):.0f} m^2/yr; "
          f"q(1200 m) = {flux_per_yr(1200.0, alpha):.0f} m^2/yr "
          f"(ratio {(1200.0 / 1000.0) ** 5:.3f})")
    print(f"(c) equilibrium thickness for a {W / 1e3:.0f} km catchment: "
          f"{h_eq:.1f} m")
    print(f"(d) at 10 km of retreat on a 10 m/km retrograde bed the excess is")
    print(f"    {excess:.0f} m^2/yr and the disequilibrium distance is "
          f"{dist / 1e3:.1f} km")
    h_loss = h_eq * (1.0 / 0.4) ** 0.2
    print(f"(e) 60% buttressing loss: h rises from {h_eq:.0f} to {h_loss:.0f} m,")
    print(f"    i.e. a water depth of {h_loss / ratio:.0f} m, an inland shift of "
          f"{(h_loss / ratio - d0) / (slope * 1000):.1f} km")
    print(f"(f) melt of 10 m/yr over 50 km = {loss / q_supply:.1f}x the "
          f"accumulation supply")
    print("\nAll numbers are SYNTHETIC model output.")


if __name__ == "__main__":
    main()
