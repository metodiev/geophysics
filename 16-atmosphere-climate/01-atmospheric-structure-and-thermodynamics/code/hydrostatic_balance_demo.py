#!/usr/bin/env python3
"""Hydrostatic balance and pressure-height relations: the hypsometric equation,
geopotential versus geometric height, thickness errors from temperature errors,
and the measured smallness of the vertical acceleration term.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python hydrostatic_balance_demo.py

All models are SYNTHETIC teaching models.  Surface pressure, surface temperature
and lapse rate are chosen inputs of the model (standard-atmosphere conventions),
printed below; no quantity here is a measurement made by this module.

Contents
--------
1. The hypsometric equation: layer thickness from two pressures.
2. Exact thickness from the analytic profile, versus the hypsometric estimate
   with three different choices of layer-mean temperature.
3. Inverting the hypsometric equation: a mean temperature from a thickness.
4. Geopotential versus geometric height: how big is the g(z) correction?
5. Sensitivity of thickness to temperature error (the altimetry error budget).
6. How small the vertical acceleration term really is (the validity of rho g).
"""

import numpy as np

RNG = np.random.default_rng(20261014)

R_D = 287.041          # J kg^-1 K^-1, dry-air gas constant (derived in lesson 01)
G0 = 9.80665           # m s^-2, standard gravity
R_EARTH = 6.371e6      # m, conventional mean Earth radius
P0 = 101325.0          # Pa, standard sea-level pressure (standard-atmosphere definition)
T0 = 288.15            # K, standard sea-level temperature
LAPSE = 6.5e-3         # K m^-1, conventional tropospheric lapse rate


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def p_of_z(z):
    """Pressure (Pa) at geometric height z (m) in the polytropic teaching model."""
    return P0 * (1.0 - LAPSE * z / T0) ** (G0 / (R_D * LAPSE))


def z_of_p(p):
    """Invert the polytropic profile for geometric height (m)."""
    return (T0 / LAPSE) * (1.0 - (p / P0) ** (R_D * LAPSE / G0))


def hypsometric(p1, p2, T_mean):
    """Thickness (m) of the layer between p1 and p2 for a mean temperature."""
    return R_D * T_mean / G0 * np.log(p1 / p2)


def layer_mean_T_polytropic(p1, p2):
    """The ln(p)-weighted mean temperature that makes the hypsometric equation exact."""
    kappa = R_D * LAPSE / G0
    return T0 * (p1 ** kappa - p2 ** kappa) / (kappa * P0 ** kappa * np.log(p1 / p2))


def main():
    p_bot, p_top = 100000.0, 50000.0

    section("1. The hypsometric equation")
    print("  Thickness of a layer from hydrostatic balance + ideal gas:")
    print("      dz = (R_d T_mean / g) ln(p1/p2)")
    print(f"  Model: p0 = {P0:.0f} Pa, T0 = {T0:.2f} K, lapse = {LAPSE * 1e3:.1f} K/km")
    print(f"  Layer: {p_bot / 100:.0f} hPa -> {p_top / 100:.0f} hPa")

    z_bot_true = z_of_p(p_bot)
    z_top_true = z_of_p(p_top)
    dz_true = z_top_true - z_bot_true
    T_bot = T0 - LAPSE * z_bot_true
    T_top = T0 - LAPSE * z_top_true
    T_arith = 0.5 * (T_bot + T_top)
    T_lnmean = layer_mean_T_polytropic(p_bot, p_top)
    print(f"  exact geometric heights: z(1000 hPa) = {z_bot_true:.3f} m, "
          f"z(500 hPa) = {z_top_true:.3f} m")
    print(f"  exact thickness = {dz_true:.3f} m")

    section("2. Thickness estimates with three layer-mean temperatures")
    print("   choice of layer-mean T          T_mean (K)   thickness (m)   error (m)    error (%)")
    for label, T in (("surface temperature", T_bot),
                     ("arithmetic mean of layer", T_arith),
                     ("ln(p)-weighted mean (exact)", T_lnmean)):
        th = hypsometric(p_bot, p_top, T)
        print(f"   {label:30s} {T:10.3f} {th:14.3f} {th - dz_true:+11.3f} "
              f"{(th - dz_true) / dz_true * 100:+10.3f}")
    print("\n  Temperature at the two levels:")
    print(f"    T(1000 hPa) = {T_bot:.3f} K,  T(500 hPa) = {T_top:.3f} K")
    print(f"    arithmetic mean = {T_arith:.3f} K, ln-weighted mean = {T_lnmean:.3f} K")
    print(f"    difference of means = {T_arith - T_lnmean:.3f} K")
    print("  The ln(p)-weighted mean is the one the hypsometric equation defines;")
    print("  the arithmetic mean is biased WARM here (+0.390 K), because the layer")
    print("  spends more of its log-pressure depth at the colder, upper end.")

    section("3. Inverting the hypsometric equation: T_mean from a thickness")
    recovered = G0 * dz_true / (R_D * np.log(p_bot / p_top))
    print(f"  given exact thickness {dz_true:.3f} m:")
    print(f"    recovered T_mean = g dz /(R_d ln(p1/p2)) = {recovered:.3f} K")
    print("  This inversion is how a radiosonde thickness gives a layer temperature,")
    print("  and it is the same number as the ln-weighted mean above: the equation")
    print("  is exact, it is the INTERPRETATION of T_mean that must be stated.")

    section("4. Geopotential versus geometric height")
    print("  Geopotential Phi(z) = int_0^z g(z') dz',  with g(z) = g0 (R/(R+z))^2")
    for z_km in (0.0, 5.0, 10.0, 20.0):
        z = z_km * 1e3
        g_ratio = (R_EARTH / (R_EARTH + z)) ** 2
        # analytic integral of g0 (R/(R+z))^2 from 0 to z:
        Phi = G0 * R_EARTH * z / (R_EARTH + z)
        Z_gpm = Phi / G0
        print(f"   z = {z_km:5.1f} km:  g(z)/g0 = {g_ratio:.6f}   "
              f"geopotential height Z = {Z_gpm:12.2f} m   (Z - z = {Z_gpm - z:+8.2f} m)")
    print("  The separation reaches 4 m at 5 km, 16 m at 10 km and 63 m at 20 km:")
    print("  small, but the 10 km value is of the same order as the thickness errors")
    print("  of Section 2 and therefore part of the error budget, not a refinement.")

    section("5. Sensitivity of thickness to temperature error")
    print("  dz/z = dT/T, so a temperature error of dT changes the thickness by")
    print("  (R_d/g) ln(p1/p2) dT.")
    coeff = R_D / G0 * np.log(p_bot / p_top)
    print(f"  coefficient (R_d/g) ln(p1/p2) = {coeff:.3f} m per K")
    for dT in (0.5, 1.0, 2.0, 5.0):
        print(f"    dT = {dT:4.1f} K -> d(thickness) = {coeff * dT:7.3f} m "
              f"({coeff * dT / dz_true * 100:5.3f}% of the 1000-500 hPa layer)")
    print("  For a target thickness accuracy of 10 m, T_mean must be known to")
    print(f"    dT = 10 / {coeff:.3f} = {10.0 / coeff:.3f} K")
    print("  That is the number that motivates the careful humidity and radiation")
    print("  corrections in lessons 04 and 16-02-01.")

    section("6. How small the vertical acceleration term is")
    print("  For an air parcel, dp/dz = -rho (g + a_z), so the fractional departure")
    print("  from exact hydrostatic balance equals a_z/g.")
    col = P0 / G0
    print(f"  column mass p0/g = {col:.2f} kg m^-2")
    for a in (0.01, 0.1, 1.0):
        print(f"    a_z = {a:5.2f} m s^-2 -> non-hydrostatic fraction "
              f"{a / G0 * 100:8.4f}%  "
              f"(pressure error over the whole column {a / G0 * P0:7.3f} Pa)")
    print("  A vigorous thunderstorm updraught reaches a_z of a few tenths of a")
    print("  m/s^2, i.e. a few per cent of g: hydrostatic balance fails by percent,")
    print("  not by orders of magnitude, and the SEVERE cases matter for the")
    print("  dynamics of lesson 05 even though the pressure profile barely notices.")

    section("7. Two independent checks")
    # (a) integrate dp/dz numerically and compare with the analytic profile
    def rk4_pressure(z_end, n=20000):
        z = 0.0
        p = P0
        h = z_end / n
        def dpdz(pp, zz):
            return -pp * G0 / (R_D * (T0 - LAPSE * zz))
        for _ in range(n):
            k1 = dpdz(p, z)
            k2 = dpdz(p + 0.5 * h * k1, z + 0.5 * h)
            k3 = dpdz(p + 0.5 * h * k2, z + 0.5 * h)
            k4 = dpdz(p + h * k3, z + h)
            p += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6.0
            z += h
        return p

    p_num = rk4_pressure(z_top_true)
    print(f"(a) RK4 integration to z = {z_top_true:.3f} m gives p = {p_num:.4f} Pa,")
    print(f"    analytic p(500 hPa level) = {p_top:.4f} Pa, difference "
          f"{p_num - p_top:+.6f} Pa")
    # (b) the hypsometric equation must reproduce an exactly known thickness
    dz_exact_model = z_of_p(60000.0) - z_of_p(90000.0)
    dz_hyp = hypsometric(90000.0, 60000.0, layer_mean_T_polytropic(90000.0, 60000.0))
    print(f"(b) 900-600 hPa thickness: model {dz_exact_model:.4f} m, "
          f"hypsometric {dz_hyp:.4f} m, difference {dz_hyp - dz_exact_model:+.2e} m")
    print("    Both checks agree to machine precision: the analytic profiles and the")
    print("    integral form are the same physics, so any disagreement in a real")
    print("    analysis comes from the data, not from the equation.")


if __name__ == "__main__":
    main()
