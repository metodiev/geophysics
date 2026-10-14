#!/usr/bin/env python3
"""Earth energy balance: the top-of-atmosphere constraint, the surface budget,
the trade-off between opacity and non-radiative cooling, and the poleward heat
transport required by the zonal imbalance.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python earth_energy_balance_demo.py

All models are SYNTHETIC.  The solar constant and sigma are standard constants;
the albedo, the surface temperature, the atmospheric emissivity, the solar
partition between surface and atmosphere, the Bowen ratio and the zonal albedo
profile are CHOSEN INPUTS, printed below.  No measured flux, satellite product,
reanalysis value or published budget is used.

Contents
--------
1. The top-of-atmosphere constraint: incident, reflected, absorbed, emitted.
2. Why the net balance can be small while every gross flux is large.
3. The surface budget: emitted, absorbed, net longwave, non-radiative residual.
4. The opacity/non-radiative trade-off: several models, one surface temperature.
5. The zonal imbalance and the required poleward heat transport.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

SIGMA = 5.670374419e-8        # W m^-2 K^-4, Stefan-Boltzmann constant
SOLAR_CONSTANT = 1361.0       # W m^-2, total solar irradiance at 1 AU (standard)
R_EARTH = 6.371e6             # m, conventional mean Earth radius

# --- CHOSEN INPUTS of the teaching model ------------------------------------
ALBEDO = 0.30                 # dimensionless, planetary albedo
T_SURFACE = 288.0             # K, illustrative surface temperature
F_SURFACE_SOLAR = 1.00        # fraction of absorbed solar absorbed at the surface
BOWEN = 0.25                  # dimensionless, sensible/latent heat ratio
EPS_OPAQUE = 1.00             # atmospheric emissivity of the "opaque" model
EPS_GREY = 0.80               # atmospheric emissivity of the "grey" model
A_ZONAL_0 = 0.30              # dimensionless, equatorial albedo (chosen)
A_ZONAL_2 = 0.30              # albedo increase toward the pole, a0 + a2 sin^2 phi


def section(title):
    print(f"\n{'=' * 76}\n{title}\n{'=' * 76}")


def main():
    F_ABS = SOLAR_CONSTANT * (1.0 - ALBEDO) / 4.0
    T_EFF = (F_ABS / SIGMA) ** 0.25
    E_S = SIGMA * T_SURFACE ** 4

    section("1. The top-of-atmosphere constraint")
    print("  Global annual mean, per square metre of surface:")
    print(f"    incident solar (S/4)          = {SOLAR_CONSTANT / 4:8.2f} W/m^2")
    print(f"    reflected (albedo {ALBEDO:.2f})      = "
          f"{SOLAR_CONSTANT * ALBEDO / 4:8.2f} W/m^2")
    print(f"    absorbed  F = S(1-a)/4        = {F_ABS:8.2f} W/m^2")
    print(f"    emitted longwave at equilibrium= {F_ABS:8.2f} W/m^2   (by definition)")
    print(f"    net top-of-atmosphere          = {F_ABS - F_ABS:8.2f} W/m^2")
    print(f"    implied effective radiating T  = {T_EFF:8.2f} K "
          f"= {T_EFF - 273.15:.2f} C")
    print("\n  The equality of absorbed and emitted is not a result; it is the")
    print("  definition of equilibrium, and it is a strong constraint: the outgoing")
    print("  longwave flux is fixed by the albedo and the solar constant, whatever")
    print("  the composition.  What composition changes is the TEMPERATURE at which")
    print("  that flux is emitted, and therefore the surface temperature.")

    section("2. Small net, large gross")
    print("  The constraint above is on the NET flux.  The individual fluxes are")
    print("  far larger, and the smallness of the net is what makes the system")
    print("  sensitive to small imbalances.")
    print(f"    emitted by the surface, sigma T_s^4 at {T_SURFACE:.0f} K = "
          f"{E_S:8.2f} W/m^2")
    print(f"    ratio surface emission / absorbed solar          = "
          f"{E_S / F_ABS:8.4f}")
    print(f"    a net imbalance of 1 W/m^2 is                     = "
          f"{1 / F_ABS * 100:8.4f}% of the absorbed solar flux")
    print(f"    ... but 1 W/m^2 is                              "
          f"{F_ABS:8.2f}x smaller than the absorbed flux")
    print("  An energy imbalance of a few W/m^2 is a fraction of a per cent of the")
    print("  throughput, and it is the quantity that a changing composition can")
    print("  produce.  That is why the observational problem is measuring a")
    print("  difference of large numbers, and why the uncertainty is dominated by")
    print("  calibration and sampling rather than by the physics.")

    section("3. The surface budget")
    print(f"  CHOSEN INPUTS: T_s = {T_SURFACE:.2f} K, "
          f"f_surface = {F_SURFACE_SOLAR:.2f} of absorbed solar to the surface,")
    print(f"                 Bowen ratio beta = H/LE = {BOWEN:.2f}, "
          f"layer emissivity eps = {EPS_OPAQUE:.2f}")
    D = F_ABS                                  # downward IR for an opaque layer
    NH = F_SURFACE_SOLAR * F_ABS + D - E_S      # residual = H + LE
    print(f"\n    surface receives  f_s x F              = "
          f"{F_SURFACE_SOLAR * F_ABS:8.2f} W/m^2")
    print(f"    surface receives  downwelling IR       = {D:8.2f} W/m^2")
    print(f"    surface emits     sigma T_s^4          = {-E_S:8.2f} W/m^2")
    print(f"    residual          H + LE               = {-NH:8.2f} W/m^2")
    print(f"    net surface budget                     = "
          f"{F_SURFACE_SOLAR * F_ABS + D - E_S - NH:8.2f} W/m^2")
    LE = NH / (1.0 + BOWEN)
    H = BOWEN * LE
    print(f"\n    partitioned with beta = {BOWEN:.2f}: "
          f"latent LE = {LE:.2f}, sensible H = {H:.2f}")
    print(f"    (H + LE = {H + LE:.2f}, reproducing the residual)")
    print("\n  Read the sign: the surface must LOSE energy non-radiatively, not")
    print("  gain it, because it receives more infrared from the atmosphere than")
    print("  the net longwave loss it needs.  The non-radiative flux is carried by")
    print("  evaporation (latent) and by turbulent contact with the air (sensible),")
    print("  and it is the atmosphere's own energy source from below.")
    print("  The split between H and LE is a CHOSEN Bowen ratio here; in reality it")
    print("  depends on surface moisture, stability and wind, which is the subject")
    print("  of boundary-layer meteorology and is not modelled in this module.")

    section("4. The opacity / non-radiative trade-off")
    print("  The same surface temperature can be produced by different combinations")
    print("  of atmospheric opacity and non-radiative cooling.  Extend the one-layer")
    print("  model by letting the surface also lose a non-radiative flux H + LE and")
    print("  letting the atmosphere absorb a fraction f_a = 1 - f_s of the solar")
    print("  beam.  The result, derived below, is")
    print("    sigma T_s^4 (2 - eps) = F (1 + f_s) - (H + LE) .")
    print("  With f_s = 1 and H + LE = 0 this reduces to the lesson-02 result")
    print("  sigma T_s^4 = 2F/(2 - eps).")
    print("\n  Derivation (two-box energy balance; T_a is the layer temperature):")
    print("    TOA        (1-eps) sigma T_s^4 + eps sigma T_a^4 = F")
    print("    surface    f_s F + eps sigma T_a^4 = sigma T_s^4 + (H+LE)")
    print("    layer      f_a F + eps sigma T_s^4 + (H+LE) = 2 eps sigma T_a^4")
    print("  Eliminating gives, with f_s + f_a = 1,")
    print("    sigma T_s^4 (2 - eps) = F (1 + f_s) - (H + LE)")
    print("\n   eps     radiative-only T_s (K)   required H+LE for T_s = 288 K (W/m^2)")
    for eps in (0.5, 0.7, 0.7789, 0.9, 1.0):
        T_rad = (2.0 * F_ABS / (SIGMA * (2.0 - eps))) ** 0.25
        nh = F_ABS * (1.0 + F_SURFACE_SOLAR) - E_S * (2.0 - eps)
        print(f"  {eps:5.4f}   {T_rad:20.3f}   {nh:33.2f}")
    print("\n  How to read the sign of the required residual:")
    print("  - If the required H+LE is POSITIVE, the radiative-only model is too")
    print("    WARM and the surface must export the excess non-radiatively.  At")
    print("    eps = 1 the radiative-only surface is 302.75 K, 14.7 K above the")
    print("    chosen 288 K, and the excess is 86.24 W/m^2.")
    print("  - If it is NEGATIVE, the model is too COLD and the surface would need")
    print("    a non-radiative HEATING, which does not exist at a planetary surface.")
    print("    So opacities below about 0.78 are inconsistent with a 288 K surface")
    print("    in this two-box model: the atmosphere must be at least that opaque.")
    print("  - At eps = 0.7789 the required residual is -0.01 W/m^2, i.e. zero:")
    print("    that is the fitted value of lesson 03, and it is the value at which")
    print("    the purely radiative model happens to reproduce the surface")
    print("    temperature.  The fit is therefore equivalent to assuming that")
    print("    convection and evaporation do not exist.")
    print("  So opacity and non-radiative flux are DEGENERATE in a surface energy")
    print("  budget: (eps = 0.779, H+LE = 0) and (eps = 1, H+LE = 86 W/m^2) give the")
    print("  same surface temperature.  Breaking the degeneracy needs the vertical")
    print("  structure, which is what a radiative-convective model supplies (lesson")
    print("  05).  A surface energy budget alone cannot determine either quantity.")

    section("5. The zonal imbalance and the required poleward transport")
    print("  The global mean hides the latitudinal structure.  CHOSEN INPUT of the")
    print("  model: a net top-of-atmosphere flux")
    print("    N(phi) = 40 - 120 sin^2(phi) W/m^2,")
    print("  which is +40 W/m^2 at the equator, zero at sin(phi) = sqrt(1/3) and")
    print("  -80 W/m^2 at the pole, and whose area-weighted mean is exactly zero")
    print("  (that last property is required: a globally unbalanced N would violate")
    print("  the constraint of Section 1, and an early version of this model used")
    print("  N = 60 - 120 sin^2(phi), which has a global mean of +40 W/m^2 and is")
    print("  therefore not a steady state - a mistake worth making once).")
    print("\n  A latitudinally varying N requires poleward energy transport.  In")
    print("  steady state the region poleward of latitude phi neither gains nor")
    print("  loses energy, so the northward transport across phi is")
    print("    H(phi) = -2 pi R^2 integral_phi^{pi/2} N(phi') cos(phi') dphi'")
    print("  which for this N evaluates analytically to")
    print("    H(phi) = 80 pi R^2 sin(phi) [1 - sin^2(phi)] .")
    print("\n   phi (deg)   N (W/m^2)   H (PW, northward)")
    for p_ in (0.0, 15.0, 30.0, 35.26, 45.0, 60.0, 75.0, 90.0):
        sn = np.sin(np.radians(p_))
        N = 40.0 - 120.0 * sn ** 2
        H = 80.0 * np.pi * R_EARTH ** 2 * sn * (1.0 - sn ** 2)
        print(f"  {p_:9.2f}   {N:9.2f}   {H / 1e15:17.4f}")
    print("\n  The transport vanishes at the equator (by symmetry: the two")
    print("  hemispheres cannot exchange net energy in a symmetric state) and at the")
    print("  pole (nothing is beyond it), and peaks at sin^2(phi) = 1/3, i.e.")
    print("  phi = 35.26 deg, with a value of")
    H_peak = 80.0 * np.pi * R_EARTH ** 2 * (1.0 / np.sqrt(3.0)) * (2.0 / 3.0)
    print(f"    H_max = 80 pi R^2 x (2/(3 sqrt3)) = {H_peak / 1e15:.3f} PW")
    print("  That is the rate at which the atmosphere and ocean must move energy")
    print("  poleward to keep the tropics from warming without limit and the poles")
    print("  from cooling without limit.  It is the largest number in this lesson,")
    print("  and it is derived from geometry, equilibrium and a chosen SHAPE for")
    print("  N(phi) - so the magnitude is a model result that a measurement of the")
    print("  net flux would test, while the structure (zero at both ends, one")
    print("  maximum in each hemisphere) follows from the symmetry alone.")
    print("  Note what does NOT enter: no composition, no radiative transfer and no")
    print("  dynamics.  The energy-transport requirement is a consequence of")
    print("  geometry and equilibrium, which is why it is among the most robust")
    print("  statements about the climate system.")


if __name__ == "__main__":
    main()
