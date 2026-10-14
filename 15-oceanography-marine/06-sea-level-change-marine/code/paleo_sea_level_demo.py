#!/usr/bin/env python3
"""Palaeo sea level: the ice-volume and temperature contributions to a carbonate
delta-18O record, the non-uniqueness of the sea-level inversion, the ice-volume
equivalent sea level, and the propagation of chronological uncertainty.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python paleo_sea_level_demo.py

Everything here is SYNTHETIC.  The isotope model, the records and the age models
are teaching models with the stated model constants.  No real core, site,
terrace, speleothem or published record is referenced, and no number is quoted
from a published measurement.

Contents
--------
1. The forward isotope model: carbonate delta-18O from sea level and temperature,
   with each coefficient stated.
2. The inversion and its non-uniqueness: one isotope value, two unknowns, and the
   sea-level error per kelvin of temperature error.
3. The ice-volume equivalent sea level from a synthetic ice volume, using the
   ocean area.
4. Chronology: age-model error propagated into a sea-level rate, and the GIA term.
5. Worked examples used in the lesson.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

K_ICE = 0.010            # per mil of delta18O_sw per metre of sea-level change
D_TEMP = 0.22            # per mil of carbonate delta18O per kelvin of cooling
RHO_ICE = 917.0          # kg/m^3
RHO_W = 1000.0           # kg/m^3
RHO_SW = 1025.0          # kg/m^3
A_OCEAN = 3.61e14        # m^2, the standard ocean area constant
G = 9.80665


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def d18o_carb(sl_m, T_C, d_sw0=0.0, T0=15.0):
    """Carbonate delta18O (per mil) for a sea level and a temperature."""
    d_sw = d_sw0 - K_ICE * sl_m          # ice growth raises delta18O_sw
    return d_sw + D_TEMP * (T0 - T_C)


def sl_from_d18o(d18o, T_C, d_sw0=0.0, T0=15.0):
    """Sea level (m) implied by a carbonate delta18O at an assumed temperature."""
    return (d_sw0 + D_TEMP * (T0 - T_C) - d18o) / K_ICE


def sea_level_equivalent(volume_m3):
    """Global mean sea-level rise from a volume of ice, m."""
    return RHO_ICE * volume_m3 / (RHO_SW * A_OCEAN)


def main():
    section("1. The forward isotope model")
    print("  model: delta18O_carb = delta18O_sw + 0.22 (T0 - T),  T0 = 15 C")
    print(f"         delta18O_sw = delta_sw0 - {K_ICE:.3f} x SL_m")
    print("  both coefficients are model values of the standard magnitude.  The")
    print("  ice-volume coefficient is the one usually calibrated against an")
    print("  independent sea-level record, and the temperature slope against")
    print("  laboratory fractionation experiments.  Neither is measured here.")
    print("\n   SL (m)   T (C)   delta18O_sw   delta18O_carb (per mil)")
    for sl, T in ((0.0, 15.0), (-40.0, 13.0), (-80.0, 10.0), (-120.0, 8.0),
                  (-120.0, 12.0)):
        d_sw = -K_ICE * sl
        print(f"  {sl:7.0f}   {T:5.1f}   {d_sw:11.3f}   "
              f"{d18o_carb(sl, T):22.3f}")

    section("2. The inversion and its non-uniqueness")
    d_obs = 1.60
    print(f"  a single measured value: delta18O_carb = {d_obs:.2f} per mil")
    print("  one equation, two unknowns (SL and T), so T must be assumed:")
    print("\n   assumed T (C)   implied SL (m)   error from T = 15 C assumption")
    for T in (15.0, 14.0, 13.0, 12.0, 10.0, 8.0):
        sl = sl_from_d18o(d_obs, T)
        print(f"   {T:13.1f}   {sl:14.1f}   {sl - sl_from_d18o(d_obs, 15.0):+29.1f}")
    print(f"\n  the sensitivity is d(SL)/dT = {D_TEMP / K_ICE:.0f} m per kelvin:")
    print(f"  a 1 C temperature error is a {D_TEMP / K_ICE:.0f} m sea-level error,")
    print("  which is larger than most of the sea-level changes being studied.")
    print("  This is why every delta18O-based sea-level curve needs an independent")
    print("  temperature proxy (Mg/Ca, alkenones, or a climate model) and why the")
    print("  two are always reported together.")
    print("\n  the same non-uniqueness seen as a ridge:")
    print("   T (C)   Mg/Ca-derived T uncertainty (C)   SL (m)   SL uncertainty (m)")
    for T, sT in ((14.0, 0.5), (14.0, 1.0), (14.0, 2.0)):
        sl = sl_from_d18o(d_obs, T)
        print(f"   {T:5.1f}   {sT:32.1f}   {sl:7.1f}   "
              f"{sT * D_TEMP / K_ICE:18.1f}")

    section("3. Ice-volume equivalent sea level")
    print(f"  model: SL = rho_ice V / (rho_sw A_ocean) with rho_ice = "
          f"{RHO_ICE:.0f} kg/m^3,")
    print(f"         rho_sw = {RHO_SW:.0f} kg/m^3, A_ocean = {A_OCEAN:.3e} m^2")
    print(f"  the ratio rho_ice/(rho_sw A_ocean) = "
          f"{RHO_ICE / (RHO_SW * A_OCEAN):.3e} m per m^3")
    print("\n   ice volume (10^15 m^3)   equivalent sea level (m)")
    for V in (1.0, 5.0, 10.0, 20.0, 30.0):
        print(f"   {V:22.1f}   {sea_level_equivalent(V * 1e15):22.2f}")
    print("\n  the same calculation in mass terms: 1 mm of global mean sea level")
    mm_mass = 1e-3 * A_OCEAN * RHO_W     # water density for the mass conversion
    print(f"    = rho_w A_ocean x 1 mm = {mm_mass:.3e} kg = "
          f"{mm_mass / 1e12:.0f} Gt")
    print("  (1 Gt = 10^12 kg, rho_w = 1000 kg/m^3 for the mass conversion).")
    print("  The 361 Gt per millimetre is the standard constant used throughout")
    print("  the modern sea-level budget.")

    section("4. Chronology and the GIA term")
    print("  a rate is a difference over a time interval, so age errors enter")
    print("  directly.  For a rise of 60 m between two dated horizons:")
    print("   age1 (ka)   age2 (ka)   duration (ka)   rate (mm/yr)")
    for a1, a2 in ((20.0, 10.0), (20.0, 11.0), (19.0, 10.0), (20.0, 12.0)):
        dur_kyr = (a1 - a2) * 1e3
        rate = 60.0 / dur_kyr * 1e3
        print(f"   {a1:10.1f}   {a2:10.1f}   {a1 - a2:13.1f}   {rate:13.2f}")
    dur = 10e3
    rate = 60.0 / dur * 1e3
    sig_dur = np.sqrt(2.0) * 1e3
    sig_rate = rate * sig_dur / dur
    print(f"  with +/-1 ka on each age (so +/-1.41 ka on the 10 ka duration), a")
    print(f"  6.00 mm/yr rate carries an uncertainty of {sig_rate:.2f} mm/yr")
    print(f"  ({sig_rate / rate * 100:.0f}%): the chronology, not the depth")
    print("  measurement, limits the rate.")
    print("\n  the GIA term: the solid Earth and the geoid both respond to ice and")
    print("  water loading, so a measured local sea level differs from the")
    print("  eustatic value.  Model values:")
    print("   site character         GIA correction (m)   effect on a 120 m signal")
    for name, gia in (("near a former ice sheet", 80.0), ("far field, stable",
                                                           5.0),
                      ("intermediate", 20.0)):
        print(f"   {name:22s} {gia:19.0f}   {gia / 120 * 100:22.0f}%")
    print("  a GIA correction that is wrong by even 10% of its own size is a")
    print("  8 m error near a former ice sheet, which is larger than most of the")
    print("  millennial-scale changes being reconstructed.")

    section("5. Worked examples used in the lesson")
    print(f"(a) delta18O_carb for SL = -80 m, T = 10 C: "
          f"{d18o_carb(-80.0, 10.0):.3f} per mil")
    print(f"    the ice-volume part is {K_ICE * 80:.3f} per mil and the temperature")
    print(f"    part {D_TEMP * 5:.3f} per mil: the temperature contribution is")
    print(f"    {D_TEMP * 5 / (K_ICE * 80) * 100:.0f}% of the ice-volume one.")
    print(f"(b) with delta18O_carb = {d_obs:.2f} per mil and T = 14 C, "
          f"SL = {sl_from_d18o(d_obs, 14.0):.1f} m; at T = 12 C, "
          f"SL = {sl_from_d18o(d_obs, 12.0):.1f} m")
    print(f"(c) 1 mm of global mean sea level = {mm_mass / 1e12:.0f} Gt of water")
    print(f"(d) 20 x 10^15 m^3 of ice = "
          f"{sea_level_equivalent(20e15):.2f} m of sea level")
    print(f"(e) a 60 m rise over 10 ka = {rate:.2f} mm/yr; with +/-1 ka ages the")
    print(f"    rate uncertainty is {sig_rate:.2f} mm/yr")
    print("\nAll numbers are SYNTHETIC model output.")


if __name__ == "__main__":
    main()
