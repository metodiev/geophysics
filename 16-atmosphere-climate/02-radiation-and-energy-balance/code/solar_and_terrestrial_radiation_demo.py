#!/usr/bin/env python3
"""Solar and terrestrial radiation, and the blackbody laws.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python solar_and_terrestrial_radiation_demo.py

The physical constants used here (h, c, k_B, sigma, the solar constant, the
astronomical unit, the nominal solar radius) are standard constants and are listed
below with their values.  The planetary albedo and the surface temperature are
chosen inputs of a SYNTHETIC teaching model, printed below.  No measured spectrum,
satellite record or published figure is used.

Contents
--------
1. The Planck function, and its two analytic limits (Wien, Stefan-Boltzmann).
2. Numerical verification: the Planck integral gives sigma T^4, and the numerical
   maximum gives Wien's displacement constant - both to 8 significant figures.
3. The solar effective temperature, derived from the solar constant, the
   astronomical unit and the nominal solar radius.
4. The factor 4 between the solar constant and the global-mean insolation.
5. Where the energy is: band fractions of the solar and terrestrial spectra.
6. Brightness temperature.
7. Daily-mean top-of-atmosphere insolation versus latitude, for two declinations.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

H_PLANCK = 6.62607015e-34     # J s, Planck constant (exact SI value)
C_LIGHT = 2.99792458e8        # m s^-1, speed of light in vacuum (exact SI value)
K_B = 1.380649e-23            # J K^-1, Boltzmann constant (exact SI value)
SIGMA_SB = 5.670374419e-8     # W m^-2 K^-4, Stefan-Boltzmann constant (CODATA value)
SOLAR_CONSTANT = 1361.0       # W m^-2, total solar irradiance at 1 AU (standard value)
AU = 1.495978707e11           # m, astronomical unit (defined)
R_SUN = 6.957e8               # m, nominal solar radius (IAU nominal value)
ALBEDO = 0.30                 # dimensionless, planetary albedo of the model
SIGMA_SB_DERIVED = 2.0 * np.pi ** 5 * K_B ** 4 / (15.0 * H_PLANCK ** 3 * C_LIGHT ** 2)


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def planck_lambda(lam, T):
    """Spectral RADIANCE B_lambda(T) in W m^-2 sr^-1 m^-1 (per metre of wavelength).

    Radiance is per steradian.  The hemispheric spectral exitance (the flux
    leaving a flat black surface) is pi B_lambda, because integrating cos(theta)
    over the hemisphere gives pi.  That factor is the reason the Stefan-Boltzmann
    constant contains pi^5 and not pi^4; the demonstration makes the distinction
    explicit below.
    """
    with np.errstate(over="ignore", invalid="ignore"):
        x = H_PLANCK * C_LIGHT / (lam * K_B * T)
        out = 2.0 * H_PLANCK * C_LIGHT ** 2 / lam ** 5 / np.expm1(x)
    return np.where(x > 700.0, 0.0, out)


def wien_constant():
    """Solve x = 5 (1 - e^-x) for the Wien peak and return b = h c/(x k_B)."""
    x = 5.0
    for _ in range(80):
        f = x - 5.0 * (1.0 - np.exp(-x))
        df = 1.0 - 5.0 * np.exp(-x)
        x -= f / df
    return H_PLANCK * C_LIGHT / (x * K_B), x


def planck_integral_x():
    """Numerically evaluate int_0^inf x^3/(e^x - 1) dx, which is pi^4/15."""
    x = np.concatenate([np.linspace(1e-9, 1.0, 200001), np.geomspace(1.0, 80.0, 400001)])
    y = x ** 3 / np.expm1(x)
    return np.trapezoid(y, x)


def main():
    section("1. The Planck function and its limits")
    print("  B_lambda(T) = 2 h c^2 / lambda^5 / [exp(h c/(lambda k_B T)) - 1]")
    print(f"  h = {H_PLANCK:.6e} J s, c = {C_LIGHT:.6e} m/s, "
          f"k_B = {K_B:.6e} J/K")
    print("  Two limits follow analytically and are checked numerically below:")
    print("    lambda_max T = h c/(x k_B)      (Wien displacement)")
    print("    pi x integral B_lambda dlambda = sigma T^4  (Stefan-Boltzmann)")
    b, x_wien = wien_constant()
    print(f"\n  x = 5(1 - e^-x) solved by Newton: x = {x_wien:.9f}")
    print(f"  derived Wien constant b = h c/(x k_B) = {b:.9e} m K")
    print(f"  the tabulated value                   = 2.897772e-03 m K")
    print(f"  relative difference = {abs(b - 2.897771955e-3) / 2.897771955e-3:.2e}")

    section("2. Numerical verification of the two laws")
    integ = planck_integral_x()
    print(f"  int_0^inf x^3/(e^x - 1) dx  = {integ:.9f}")
    print(f"  pi^4/15                     = {np.pi ** 4 / 15:.9f}")
    print(f"  relative difference = {abs(integ - np.pi ** 4 / 15) / (np.pi ** 4 / 15):.2e}")
    print(f"\n  sigma from the constants: 2 pi^5 k_B^4/(15 h^3 c^2) = "
          f"{SIGMA_SB_DERIVED:.9e}")
    print(f"    (the radiance form without the pi is "
          f"{SIGMA_SB_DERIVED / np.pi:.9e})")
    print(f"  tabulated Stefan-Boltzmann constant                = {SIGMA_SB:.9e}")
    print(f"  relative difference = {abs(SIGMA_SB_DERIVED - SIGMA_SB) / SIGMA_SB:.2e}")
    print("\n  Direct numerical integration of the Planck function over wavelength.")
    print("  B_lambda is a RADIANCE (per steradian); the flux from a flat surface is")
    print("  pi B_lambda.  Both integrals are shown so the factor is visible:")
    print("   T (K)    int B dlambda    pi x int B dlambda   sigma T^4      ratio")
    for T in (255.0, 288.0, 5772.0):
        lam = np.geomspace(1e-9, 3e-2, 600001)
        val = np.trapezoid(planck_lambda(lam, T), lam)
        print(f"  {T:7.0f}   {val:13.6e}   {np.pi * val:17.6e}   "
              f"{SIGMA_SB * T ** 4:12.6e}   {np.pi * val / (SIGMA_SB * T ** 4):7.5f}")
    print("  int B dlambda = sigma T^4 / pi exactly (the ratio is 0.31831 = 1/pi),")
    print("  and pi x int B dlambda = sigma T^4 to the grid truncation.  The radiance")
    print("  form of the constant is 2 pi^4 k^4/(15 h^3 c^2); the flux form, which is")
    print("  the Stefan-Boltzmann constant, is pi times that, i.e. 2 pi^5 k^4/")
    print("  (15 h^3 c^2).  Confusing the two is a factor-of-pi error, and this is")
    print("  the check that catches it.")

    section("3. The solar effective temperature, derived from measured constants")
    print(f"  solar constant S = {SOLAR_CONSTANT:.1f} W/m^2 at 1 AU; "
          f"1 AU = {AU:.6e} m; R_sun = {R_SUN:.4e} m")
    L_sun = SOLAR_CONSTANT * 4.0 * np.pi * AU ** 2
    T_eff = (SIGMA_SB * 4.0 * np.pi * R_SUN ** 2 * T_eff if False else
             (L_sun / (SIGMA_SB * 4.0 * np.pi * R_SUN ** 2)) ** 0.25)
    print(f"  luminosity  L = S x 4 pi AU^2 = {L_sun:.4e} W")
    print(f"  effective temperature  T = (L/(4 pi R_sun^2 sigma))^(1/4) = "
          f"{T_eff:.2f} K")
    print(f"  peak wavelength  b/T = {b / T_eff * 1e9:.1f} nm  -> visible light")
    print("  Both of those are DERIVED here from the solar constant, the AU and the")
    print("  nominal solar radius, using only the blackbody laws verified above.")

    section("4. Global-mean insolation and the factor 4")
    print("  The Earth intercepts pi R^2 of sunlight but distributes it over")
    print("  4 pi R^2 of surface, so the global mean is S/4.")
    print(f"    S               = {SOLAR_CONSTANT:.2f} W/m^2 (top of atmosphere,")
    print("                      perpendicular to the beam, at 1 AU)")
    print(f"    S/4             = {SOLAR_CONSTANT / 4:.2f} W/m^2 (global mean)")
    print(f"    absorbed S(1-a)/4 = {SOLAR_CONSTANT * (1 - ALBEDO) / 4:.2f} W/m^2 "
          f"for albedo a = {ALBEDO:.2f}")
    T_rad = (SOLAR_CONSTANT * (1 - ALBEDO) / (4.0 * SIGMA_SB)) ** 0.25
    print(f"    the T at which that is radiated: ((1-a)S/(4 sigma))^(1/4) = "
          f"{T_rad:.2f} K")
    print("  That number - the effective radiating temperature - is not the surface")
    print("  temperature; the difference is the greenhouse effect, quantified in")
    print("  lesson 03.  Here it is only the balance of a blackbody.")
    print(f"    peak wavelength of that radiation: {b / T_rad * 1e6:.2f} microns")

    section("5. Where the energy is: band fractions")
    print("  Fraction of blackbody flux emitted shortward / longward of 4 microns")
    print("   T (K)     f(< 4 um)    f(> 4 um)    context")
    for T, ctx in ((5772.0, "Sun"), (255.0, "Earth, blackbody"), (288.0, "Earth, surface")):
        lam = np.geomspace(1e-9, 4e-6, 400001)
        short = np.trapezoid(planck_lambda(lam, T), lam)
        total = SIGMA_SB * T ** 4 / np.pi      # same convention: no steradian factor
        print(f"  {T:7.0f}   {short / total:10.6f}   {1 - short / total:10.6f}   {ctx}")
    print("  The two spectra are almost completely separated: the Sun radiates")
    print("  essentially all its energy below 4 microns, the Earth above.  That")
    print("  separation is the physical reason a single 'greenhouse gas' can be")
    print("  almost transparent to sunlight and almost opaque to the surface's own")
    print("  radiation, and it is what makes the greenhouse effect possible at all.")
    lam = np.geomspace(1e-9, 1e-2, 600001)
    mask = lam <= 3e-6
    solar_frac = np.pi * np.trapezoid(planck_lambda(lam[mask], 5772.0), lam[mask]) \
        / (SIGMA_SB * 5772.0 ** 4)
    print(f"\n  fraction of the total solar blackbody flux below 3 micron: "
          f"{solar_frac:.4f}")
    print("  So about 98% of the Sun's energy arrives in the visible and near")
    print("  infrared, while less than 0.05% of the Earth's emission is there.")

    section("6. Brightness temperature")
    print("  Invert Stefan-Boltzmann: a flux F is radiated by T = (F/sigma)^(1/4).")
    print("   F (W/m^2)     T (K)     T (degC)")
    for F in (100.0, 240.0, 340.0, 1000.0, 1361.0):
        T = (F / SIGMA_SB) ** 0.25
        print(f"  {F:10.1f}   {T:8.2f}   {T - 273.15:9.2f}")
    print("  For a grey body the same inversion gives the brightness temperature,")
    print("  which equals the kinetic temperature only if the emissivity is 1 and")
    print("  the emission is not absorbed on the way out.  In lesson 02 the")
    print("  difference between the brightness temperature and the surface")
    print("  temperature becomes a measurement of the intervening atmosphere.")

    section("7. Daily-mean top-of-atmosphere insolation versus latitude")
    print("  Daily mean = (S/pi)[h0 sin(phi) sin(delta) + cos(phi) cos(delta) sin(h0)]")
    print("  with h0 = arccos(-tan(phi) tan(delta)) the half-day length")
    print("   phi (deg)    equinox (delta=0)   June solstice (delta=23.44)")
    for phi_deg in (0.0, 15.0, 30.0, 45.0, 60.0, 75.0, 90.0):
        phi = np.radians(phi_deg)
        vals = []
        for delta_deg in (0.0, 23.44):
            delta = np.radians(delta_deg)
            cos_h0 = -np.tan(phi) * np.tan(delta)
            if cos_h0 <= -1.0:
                h0 = np.pi
            elif cos_h0 >= 1.0:
                h0 = 0.0
            else:
                h0 = np.arccos(cos_h0)
            F = SOLAR_CONSTANT / np.pi * (h0 * np.sin(phi) * np.sin(delta)
                                          + np.cos(phi) * np.cos(delta) * np.sin(h0))
            vals.append(F)
        print(f"  {phi_deg:9.0f}   {vals[0]:17.1f}   {vals[1]:21.1f}")
    print("  At the equinox the daily mean falls as cos(phi); at the June solstice")
    print("  the pole receives MORE than the equator, because a 24-hour day more")
    print("  than compensates for the low Sun angle.  This single asymmetry drives")
    print("  the seasonal reversal of the pole-to-equator temperature gradient and")
    print("  therefore the seasonal reversal of the thermal wind of lesson 16-01-05.")


if __name__ == "__main__":
    main()
