#!/usr/bin/env python3
"""The greenhouse effect: what it is, how large it is in a one-layer model, how
it responds to more absorber, and where band saturation comes from.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python greenhouse_effect_demo.py

All models are SYNTHETIC.  The solar constant, the albedo, the illustrative
surface temperature and the line shape parameters are chosen inputs of a teaching
model, printed below, EXCEPT for the solar constant and sigma which are standard
constants.  The demo does not use, quote or reproduce any measured spectrum,
satellite record or published radiative forcing.

Contents
--------
1. The three temperatures: effective, surface, and the difference.
2. What the surface must receive from the atmosphere to be that warm.
3. Fitting a one-layer model to the increment.
4. Sensitivity: how the surface responds to more broadband absorber.
5. The Planck response, and what it does to an imposed forcing.
6. Band saturation, measured with an explicitly synthetic Lorentz line.
7. What is measured, what is modelled, what is inferred.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

SIGMA = 5.670374419e-8        # W m^-2 K^-4, Stefan-Boltzmann constant
SOLAR_CONSTANT = 1361.0       # W m^-2, total solar irradiance at 1 AU (standard)
ALBEDO = 0.30                 # dimensionless, planetary albedo (CHOSEN INPUT)
T_SURFACE = 288.0             # K, illustrative surface temperature (CHOSEN INPUT)
H_PLANCK = 6.62607015e-34     # J s
C_LIGHT = 2.99792458e8        # m s^-1
K_B = 1.380649e-23            # J K^-1

F_SOLAR = SOLAR_CONSTANT * (1.0 - ALBEDO) / 4.0
T_EFF = (F_SOLAR / SIGMA) ** 0.25


def section(title):
    print(f"\n{'=' * 76}\n{title}\n{'=' * 76}")


def Ts_single_layer(eps, F=F_SOLAR):
    """Exact equilibrium surface temperature of a one-layer grey model."""
    return (2.0 * F / (SIGMA * (2.0 - eps))) ** 0.25


def planck_flux(lam, T):
    """Hemispheric spectral exitance (W m^-2 m^-1)."""
    with np.errstate(over="ignore", invalid="ignore"):
        x = H_PLANCK * C_LIGHT / (lam * K_B * T)
        out = np.pi * 2.0 * H_PLANCK * C_LIGHT ** 2 / lam ** 5 / np.expm1(x)
    return np.where(x > 700.0, 0.0, out)


def main():
    section("1. The three temperatures")
    print(f"  absorbed solar flux  F = S(1-a)/4 = {F_SOLAR:.2f} W/m^2")
    print(f"  effective radiating temperature  T_e = (F/sigma)^(1/4) = "
          f"{T_EFF:.3f} K = {T_EFF - 273.15:.2f} C")
    print(f"  illustrative surface temperature  T_s = {T_SURFACE:.2f} K = "
          f"{T_SURFACE - 273.15:.2f} C   (CHOSEN INPUT of the model)")
    print(f"  increment  T_s - T_e = {T_SURFACE - T_EFF:.2f} K")
    print("\n  The first is a MODEL output: it uses the blackbody laws and an albedo")
    print("  this demo chose.  The second is also a CHOSEN INPUT here.  The third is")
    print("  the difference of the two.  None of the three is a measurement made by")
    print("  this repository.  The real global mean surface temperature is an")
    print("  observational quantity, and this module deliberately does not assert a")
    print("  value for it: the point of the exercise is the STRUCTURE of the")
    print("  argument, not the number.")

    section("2. What the surface must receive from the atmosphere")
    E_surface = SIGMA * T_SURFACE ** 4
    deficit = E_surface - F_SOLAR
    print(f"  flux emitted by a black surface at {T_SURFACE:.0f} K: sigma T_s^4 = "
          f"{E_surface:.2f} W/m^2")
    print(f"  absorbed solar flux reaching the surface (all of it, in this model): "
          f"{F_SOLAR:.2f} W/m^2")
    print(f"  required downwelling infrared from the atmosphere = "
          f"{deficit:.2f} W/m^2")
    print(f"  ratio emitted/absorbed = {E_surface / F_SOLAR:.3f}")
    print("\n  So a surface 33 K above the effective radiating temperature must")
    print("  receive about 152 W/m^2 of infrared from the sky - more than half of")
    print("  its own emitted flux - to be in balance.  That downwelling flux is an")
    print("  OBSERVABLE quantity (a pyrgeometer measures it), and its existence is")
    print("  the greenhouse effect in its most direct form.  Turning the number")
    print("  above into a prediction requires solving the radiative transfer of")
    print("  lesson 02; here it is only an energy-budget inference from the chosen")
    print("  surface temperature.")

    section("3. Fitting a one-layer model to the increment")
    print("  The one-layer model of lesson 02 gives, exactly,")
    print("    sigma T_s^4 = 2F/(2-eps)   ->   eps = 2 - 2F/(sigma T_s^4)")
    eps_fit = 2.0 - 2.0 * F_SOLAR / E_surface
    print(f"  Solving for the emissivity that reproduces T_s = {T_SURFACE:.2f} K:")
    print(f"    eps = 2 - 2 x {F_SOLAR:.2f}/{E_surface:.2f} = {eps_fit:.5f}")
    print("  So ONE free parameter is enough to fit the surface temperature.  That")
    print("  is exactly why a one-layer fit carries no explanatory power: it is a")
    print("  two-parameter model (albedo and emissivity) tuned to reproduce one")
    print("  number.  It cannot also reproduce the outgoing spectrum, and lesson 02")
    print("  measured the size of the error that makes.")
    print("\n  T_s as a function of the layer emissivity, for reference:")
    print("   eps      T_s (K)    T_s - T_e (K)")
    for eps in (0.0, 0.25, 0.5, 0.75, eps_fit, 0.90, 1.0):
        ts = Ts_single_layer(eps)
        tag = "   <- fitted" if abs(eps - eps_fit) < 1e-9 else ""
        print(f"  {eps:5.4f}   {ts:8.3f}   {ts - T_EFF:13.3f}{tag}")

    section("4. Sensitivity to more broadband absorber")
    print("  dT_s/deps = T_s / (4 (2 - eps)), from differentiating the exact result.")
    print("   eps       T_s (K)   dT_s/deps (K)   dT_s/deps per K of T_s")
    for eps in (0.30, 0.50, eps_fit, 0.85, 0.95):
        ts = Ts_single_layer(eps)
        d = ts / (4.0 * (2.0 - eps))
        print(f"  {eps:5.4f}   {ts:8.3f}   {d:13.3f}   {d / ts:17.5f}")
    print("\n  Read the last column: the FRACTIONAL temperature response per unit of")
    print("  emissivity grows with eps, from about 0.089 to 0.123 per unit eps over")
    print("  this range - so this one-layer model does NOT saturate.  That is a real")
    print("  property of the one-layer idealisation, not of the atmosphere: with a")
    print("  single layer the whole atmosphere is either transparent or opaque, and")
    print("  there is no partial-saturation regime to flatten the response.")
    print("  Saturation in the real atmosphere comes from the SPECTRUM (Section 6),")
    print("  and a broadband emissivity cannot represent it.  Claiming otherwise is")
    print("  the single commonest misuse of the one-layer model.")
    print("\n  For illustration only, an increase of eps from "
          f"{eps_fit:.4f} to 0.85:")
    dT = Ts_single_layer(0.85) - Ts_single_layer(eps_fit)
    print(f"    T_s goes from {Ts_single_layer(eps_fit):.3f} to "
          f"{Ts_single_layer(0.85):.3f} K, a change of {dT:+.3f} K")
    print("  and this is a statement about a hypothetical emissivity, not about any")
    print("  gas, concentration or scenario.")

    section("5. The Planck response")
    print("  If the surface warms by dT, its emitted flux rises by 4 sigma T^3 dT.")
    print("  This is the reference - the 'no-feedback' response - against which all")
    print("  feedbacks of lesson 16-04-02 are measured.")
    print("   T (K)    4 sigma T^3 (W m^-2 K^-1)")
    for T in (254.578, 255.0, 288.0, 300.0):
        print(f"  {T:8.3f}   {4.0 * SIGMA * T ** 3:23.4f}")
    lam0 = 4.0 * SIGMA * T_EFF ** 3
    print(f"\n  At the effective radiating temperature the Planck response is")
    print(f"  lambda_0 = 4 sigma T_e^3 = {lam0:.4f} W m^-2 K^-1.")
    print("  An imposed radiative forcing F would therefore change the equilibrium")
    print("  temperature by F/lambda_0 in the absence of feedbacks:")
    print("   forcing (W/m^2)   no-feedback dT (K)")
    for forcing in (0.5, 1.0, 2.0, 4.0):
        print(f"  {forcing:15.1f}   {forcing / lam0:17.4f}")
    print("  These are derived from the constants and the model, and they are")
    print("  statements about a blackbody in balance - NOT about any particular")
    print("  forcing agent.  Converting a real forcing into a temperature change")
    print("  requires the radiative transfer of lesson 02, the feedbacks of")
    print("  16-04-02, and the model evaluation of 16-05, and it is not done here.")

    section("6. Band saturation, measured with an explicitly synthetic line")
    print("  SYNTHETIC line: Lorentz shape k(nu) = S alpha/(pi[(nu-nu0)^2+alpha^2])")
    print("  with a model-chosen line-centre wavenumber, strength and half-width.")
    print("  The numbers are chosen for the demonstration; they are not the")
    print("  parameters of any real spectral line, and no gas is identified.")
    nu0 = 1.0 / (15.0e-6)          # m^-1, a model line centre near 15 microns
    alpha = 5.0e2                  # m^-1, model half-width at half maximum
    S = 1.0 * np.pi * 5.0e2        # model strength, chosen so that the line-centre
                                   # absorption coefficient times the reference
                                   # column amount W = 1 equals 1.0
    lam = np.geomspace(11e-6, 20e-6, 400001)
    nu = 1.0 / lam
    B = planck_flux(lam, T_SURFACE)
    B250 = planck_flux(lam, 250.0)
    shape = S * alpha / (np.pi * ((nu - nu0) ** 2 + alpha ** 2))
    total_band = np.trapezoid(B, lam)
    print(f"  line centre {nu0:.4e} m^-1 (= {1e6 / nu0:.2f} micron in wavelength)")
    print(f"  model half-width {alpha:.4e} m^-1, model strength {S}")
    print(f"\n  The OLR deficit in the band, relative to a transparent atmosphere,")
    print(f"  is  D(W) = integral [1 - exp(-k(nu) W)] B(nu) dlambda.")
    print("   W (relative)   deficit (W/m^2)   D/W            local slope dlnD/dlnW")
    Ws = np.array([0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0])
    Ds = []
    for W in Ws:
        t = np.exp(-shape * W)
        Ds.append(np.trapezoid((1.0 - t) * B, lam))
    Ds = np.array(Ds)
    for i, W in enumerate(Ws):
        if 0 < i < len(Ws) - 1:
            slope = (np.log(Ds[i + 1]) - np.log(Ds[i - 1])) / (
                np.log(Ws[i + 1]) - np.log(Ws[i - 1]))
            s = f"{slope:20.4f}"
        else:
            s = "                   -"
        print(f"  {W:12.4g}   {Ds[i]:13.6f}   {Ds[i] / W:13.6f}   {s}")
    print("\n  The local slope d ln D / d ln W starts at 1.00 (unsaturated: doubling")
    print("  the absorber doubles the absorbed flux), passes through about 1/2 (the")
    print("  strong-line regime, where the saturated core stops growing and only the")
    print("  wings do, so their area grows as the square root of the amount), and")
    print("  then falls further as even the wings saturate.  THIS is the origin of")
    print("  the approximately logarithmic dependence of radiative forcing on")
    print("  absorber amount, and it is a property of the LINE SHAPE, not of the")
    print("  greenhouse effect in general.")
    print("  A consequence worth stating: the marginal effect of adding absorber is")
    print("  largest where the spectrum is NOT already saturated, which is why the")
    print("  weakly absorbing bands and the window edges matter disproportionately.")

    section("7. Measured, modelled and inferred")
    rows = [
        ("outgoing spectral radiance at the top of the atmosphere",
         "MEASURED", "by spectrometers; shows absorption bands"),
        ("downwelling infrared at the surface",
         "MEASURED", "by pyrgeometers; shows the sky radiating"),
        ("surface and atmospheric temperatures",
         "MEASURED", "with stated instrumental and sampling uncertainty"),
        ("effective radiating temperature for a stated albedo",
         "MODELLED", "a blackbody calculation, this demo"),
        ("one-layer effective emissivity fitted to a temperature",
         "MODELLED", "a one-parameter fit, no explanatory power"),
        ("the increment T_s - T_e as a greenhouse effect",
         "INFERRED", "requires the counterfactual of Section 2"),
        ("Radiative forcing from a change in a gas",
         "MODELLED + MEASURED",
         "line parameters are measured; the band integral is computed"),
        ("Equilibrium climate sensitivity",
         "MODELLED + INFERRED",
         "needs feedbacks; not computed in this module"),
    ]
    print("   item                                        status")
    for item, status, note in rows:
        print(f"   {item:43s} {status:17s} {note}")
    print("\n  The counterfactual that most needs care: 'the temperature without the")
    print("  greenhouse effect' is NOT the effective radiating temperature, because")
    print("  removing the atmosphere would also change the albedo (no clouds, no")
    print("  water vapour, different ice).  A world with the atmosphere's greenhouse")
    print("  gases removed but everything else held fixed is a MODEL, and a world")
    print("  with the whole atmosphere removed is a DIFFERENT planet.  Both are")
    print("  computed, neither is observed.")


if __name__ == "__main__":
    main()
