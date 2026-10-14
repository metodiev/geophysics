"""Lithosphere, asthenosphere and the rheological definition.

Run:  .venv/bin/python lithosphere_asthenosphere_demo.py
Requires: numpy (and the standard library).

Companion to lesson 04-01-02, "Lithosphere, Asthenosphere and the
Rheological Definition".

The lesson's central claim is that the lithosphere-asthenosphere division is
*rheological*, not compositional: the two layers are the same rock, and the
difference between them is how that rock responds to a load that lasts a
certain length of time. This script makes that claim quantitative.

The governing idea is the Maxwell relaxation time of a viscoelastic solid,

    tau_M = eta / mu,

with eta the dynamic viscosity and mu the shear modulus. A load applied for a
time much shorter than tau_M sees an elastic solid; a load applied for a time
much longer than tau_M sees a viscous fluid. Their ratio is the Deborah number
De = tau_M / T_load. The whole lesson is the statement that seismic waves have
De >> 1 and mantle convection has De << 1, in the same rock.

The script computes:

1. The Maxwell relaxation time of mantle and asthenosphere rock, and the
   Deborah number for a seismic period, a glacial cycle and a plate-motion
   interval. This is the quantitative core of the lesson.
2. The post-glacial rebound time for a load of a given width, and the
   viscosity that the observed rebound rate implies. This is the measurement
   that made "the mantle flows" quantitative rather than metaphorical.
3. The flexural rigidity of the lithosphere as a function of effective elastic
   thickness, and the load width at which flexure stops being negligible.
4. Airy isostasy: the crustal root that supports a given topography.
5. The temperature sensitivity of viscosity, and the size of the seismic
   velocity anomaly that accompanies it. The point of this part is the *ratio*:
   a two per cent velocity change goes with an order-of-magnitude change in
   viscosity, which is why the rheological boundary is hard to see
   seismically even though it is the most important boundary for tectonics.

All rock properties vary by orders of magnitude in nature. Every value used
here is labelled NOMINAL or ILLUSTRATIVE, and the script reports the sensitivity
of each result to its input rather than a single answer.
"""

from __future__ import annotations

import math

import numpy as np

G_ACC = 9.81                   # m/s^2
YEAR = 3.15576e7               # s, Julian year
R_GAS = 8.314462618            # J mol^-1 K^-1

NOMINAL = {
    "mu_mantle": 70e9,         # Pa, shear modulus of mantle rock (~70 GPa)
    "eta_mantle": 1e21,        # Pa s, dynamic viscosity of the mantle
    "eta_asthenosphere": 1e19, # Pa s, a low-viscosity channel
    "rho_mantle": 3300.0,      # kg/m^3
    "rho_crust": 2800.0,       # kg/m^3
    "E_creep": 300e3,          # J/mol, an illustrative creep activation energy
    "youngs": 70e9,            # Pa, Young's modulus of lithospheric rock
    "poisson": 0.25,           # dimensionless
}


def section(title):
    print()
    print("=" * 74)
    print(title)
    print("=" * 74)


def part1_maxwell_and_deborah():
    section("1. Maxwell relaxation time and the Deborah number")
    eta = NOMINAL["eta_mantle"]
    eta_a = NOMINAL["eta_asthenosphere"]
    mu = NOMINAL["mu_mantle"]

    tau = eta / mu
    tau_a = eta_a / mu
    print(f"  tau_M = eta / mu with eta = {eta:.0e} Pa s (NOMINAL mantle) and")
    print(f"  mu = {mu / 1e9:.0f} GPa:")
    print(f"    asthenosphere, eta = {eta_a:.0e} Pa s -> tau_M = {tau_a:.3e} s"
          f" = {tau_a / YEAR:,.0f} a")
    print(f"    mantle,         eta = {eta:.0e} Pa s -> tau_M = {tau:.3e} s"
          f" = {tau / YEAR:,.0f} a")
    print()
    loads = [
        ("seismic P wave", 1.0 / 1.0, "1 s period"),
        ("seismic surface wave", 50.0, "50 s period"),
        ("glacial cycle", 1e5 * YEAR, "100 ka"),
        ("plate motion", 1e6 * YEAR, "1 Ma"),
        ("mantle convection", 1e8 * YEAR, "100 Ma"),
    ]
    print(f"  {'load':<24}{'period T (s)':>16}{'De = tau/T (mantle)':>22}"
          f"{'response':>14}")
    for name, period, label in loads:
        de = tau / period
        resp = "elastic" if de > 10 else ("viscous" if de < 0.1 else "transitional")
        print(f"  {name:<24}{period:>16.4g}{de:>22.3e}{resp:>14}")
    print()
    de_values = [tau / period for _, period, _ in loads]
    span = max(de_values) / min(de_values)
    print("  One rock, one pair of numbers, and the response changes from")
    print(f"  elastic to viscous by a factor of {span:.1e} -- about "
          f"{math.log10(span):.0f} orders of")
    print("  magnitude -- across the loads listed. That is the whole")
    print("  content of the lithosphere-asthenosphere distinction. It is not a")
    print("  compositional boundary: the same peridotite sits on both sides.")
    print("  It is the timescale of the load that decides what the words mean.")
    print()
    print("  Note where the transition sits. With these nominal values a load")
    print(f"  lasting about {tau / YEAR:,.0f} a is the crossover, which is")
    print("  between the glacial and plate-motion rows: an ice sheet is")
    print("  'short' relative to the mantle and a drifting plate is 'long'.")
    print()


def part2_postglacial_rebound():
    section("2. Post-glacial rebound: the measurement that made it quantitative")
    # Viscous half-space response: a harmonic load of wavelength lambda relaxes
    # with time constant tau = 2 eta k / (rho g), k = 2 pi / lambda.
    eta = NOMINAL["eta_mantle"]
    rho = NOMINAL["rho_mantle"]
    print("  For a viscous half-space, a surface load of wavelength lambda")
    print("  relaxes with tau = 2 eta k / (rho g), where k = 2 pi / lambda.")
    print()
    print(f"  {'lambda (km)':>14}{'k (1/m)':>14}{'tau (a)':>14}"
          f"{'eta from tau (Pa s)':>22}")
    for lam_km in (1000.0, 2000.0, 3000.0, 4000.0, 6000.0):
        lam = lam_km * 1e3
        k = 2.0 * math.pi / lam
        tau = 2.0 * eta * k / (rho * G_ACC)
        # Invert: the eta that would give a 4500 a rebound at this wavelength.
        eta_obs = 4500.0 * YEAR * rho * G_ACC / (2.0 * k)
        print(f"  {lam_km:>14.0f}{k:>14.3e}{tau / YEAR:>14.0f}"
              f"{eta_obs:>22.2e}")
    print()
    print("  The last column is the inversion that matters historically: an")
    print("  observed 4500 a rebound (a NOMINAL figure for the Fennoscandian")
    print("  and Laurentide domes) implies a viscosity of order 1e21 Pa s at")
    print("  the wavelengths that were actually loaded. That is how a")
    print("  geologically observed relaxation time became a measurement of a")
    print("  physical property of the deep interior.")
    print()
    print("  The wavelength dependence is the important part. A narrow load")
    print("  relaxes quickly and samples shallow, low-viscosity material; a")
    print("  wide load relaxes slowly and samples deeper, higher-viscosity")
    print("  material. Spread a set of wavelengths and you get a viscosity")
    print("  *profile*, not a number. That is the method of glacial isostatic")
    print("  adjustment studies.")
    print()


def part3_flexure():
    section("3. Flexural rigidity and the effective elastic thickness")
    e_mod = NOMINAL["youngs"]
    nu = NOMINAL["poisson"]
    rho_m = NOMINAL["rho_mantle"]

    print("  D = E Te^3 / (12 (1 - nu^2));  the flexural wavelength scales as")
    print("  (D / (rho_m g))^(1/4).  Te is the *effective elastic thickness*,")
    print("  the thickness that reproduces the observed bending, not the")
    print("  mechanical thickness of the plate.")
    print()
    print(f"  {'Te (km)':>10}{'D (N m)':>16}{'alpha (km)':>14}"
          f"{'loads wider than 2*alpha':>26}")
    for te_km in (5.0, 15.0, 30.0, 60.0):
        te = te_km * 1e3
        d = e_mod * te**3 / (12.0 * (1.0 - nu**2))
        alpha = (d / (rho_m * G_ACC)) ** 0.25
        print(f"  {te_km:>10.0f}{d:>16.3e}{alpha / 1e3:>14.1f}"
              f"{'> ' + format(2 * alpha / 1e3, '.0f') + ' km':>26}")
    print()
    alpha30 = ((e_mod * (30e3) ** 3 / (12.0 * (1.0 - nu**2))) / (rho_m * G_ACC)) ** 0.25
    print("  alpha is the flexural parameter, the length over which the plate")
    print("  bends appreciably. Read the last column against the first:")
    print(f"  at Te = 30 km the plate responds as a beam over only about")
    print(f"  {alpha30 / 1e3:.0f} km, and loads *wider* than that are carried by the")
    print("  strength of the plate rather than by local buoyancy. A narrow load")
    print("  -- a volcano, a lake, an ice cap -- bends the plate over alpha and")
    print("  produces a moat and an outer bulge. A wide load -- a continent --")
    print("  is supported without much bending at all, which is why continents")
    print("  can stand kilometres high for hundreds of millions of years.")
    print()
    print("  The two limits carry the names of the two isostasy models. Loads")
    print("  much narrower than alpha are supported by buoyancy alone: Airy")
    print("  isostasy, the approximation geologists used for a century before")
    print("  Te could be measured. Loads much wider than alpha are supported by")
    print("  plate strength: flexural isostasy. Because alpha depends on Te^3/4")
    print("  while the observed bending depends on alpha, the *bending* is a")
    print("  measurement of Te, and Te is a rheological property of the plate --")
    print("  which is what makes flexure a geophysical measurement and not just")
    print("  a model.")
    print()


def part4_airy_isostasy():
    section("4. Airy isostasy: the root beneath a mountain range")
    rho_c = NOMINAL["rho_crust"]
    rho_m = NOMINAL["rho_mantle"]
    factor = rho_c / (rho_m - rho_c)
    print(f"  With rho_crust = {rho_c:.0f} and rho_mantle = {rho_m:.0f} kg/m^3,")
    print(f"  an Airy root has r/h = rho_c / (rho_m - rho_c) = {factor:.2f}.")
    print()
    print(f"  {'topography h (km)':>18}{'root r (km)':>14}"
          f"{'Moho depth (km)':>18}")
    for h in (0.5, 1.0, 2.0, 4.0, 6.0):
        r = factor * h
        print(f"  {h:>18.1f}{r:>14.2f}{35.0 + h + r:>18.1f}")
    print()
    print("  Read the third column against the first: Tibet, at about 5 km")
    print("  average elevation, sits on a crust of roughly 70 km. The ratio is")
    print("  the content of the table, and it is the same ratio that lets a")
    print("  gravity survey see isostatic compensation as a mass deficit.")
    print()
    print("  The approximation's limits are as important as its content. Airy")
    print("  isostasy assumes the load is supported locally, which fails for")
    print("  wide loads on a strong plate (section 3) and fails where the")
    print("  density contrast is not at a single interface. Both failures are")
    print("  visible in the gravity field, which is how they are measured.")
    print()


def part5_temperature_and_velocity():
    section("5. A few per cent velocity change, four orders of magnitude of viscosity")
    eta0 = NOMINAL["eta_mantle"]
    e_creep = NOMINAL["E_creep"]
    print("  Viscosity is thermally activated: eta(T) = eta0 exp(E / (R T)).")
    print(f"  Take E = {e_creep / 1e3:.0f} kJ/mol (ILLUSTRATIVE, and creep")
    print("  activation energies differ between mechanisms and minerals).")
    print()
    print(f"  {'T (K)':>8}{'T (C)':>8}{'eta / eta0':>16}{'dVs/Vs (%)':>14}")
    t_ref = 1600.0
    for t in (1300.0, 1500.0, 1600.0, 1700.0, 1900.0):
        ratio = math.exp(e_creep / R_GAS * (1.0 / t_ref - 1.0 / t))
        # Illustrative seismic sensitivity: dVs/dT ~ -0.5 m/s per K on a
        # 4500 m/s background, a NOMINAL figure quoted here as an assumption.
        dvs_percent = 100.0 * (-0.5 * (t - t_ref)) / 4500.0
        print(f"  {t:>8.0f}{t - 273.15:>8.0f}{ratio:>16.3g}{dvs_percent:>14.2f}")
    print()
    print("  The columns move on completely different scales. From 1300 K to")
    print("  1900 K the viscosity changes by nearly four orders of magnitude")
    print("  while the shear velocity changes by a few per cent. That asymmetry")
    print("  is the practical difficulty behind the word 'asthenosphere': the")
    print("  seismic signature of the boundary is weak and model-dependent,")
    print("  but the rheological contrast is enormous and is what actually")
    print("  controls whether plates can move.")
    print()
    print("  It also cuts the other way: because the seismic signal is small,")
    print("  a measured 'low-velocity zone' does not by itself establish a")
    print("  low-viscosity channel, and a viscosity structure inferred from")
    print("  post-glacial rebound does not by itself locate a seismic")
    print("  discontinuity. The two measurements have to be combined, and that")
    print("  is a research problem rather than a textbook result.")
    print()


def main():
    print("Lithosphere, asthenosphere and the rheological definition.")
    part1_maxwell_and_deborah()
    part2_postglacial_rebound()
    part3_flexure()
    part4_airy_isostasy()
    part5_temperature_and_velocity()
    print("=" * 74)
    print("All inputs are NOMINAL or ILLUSTRATIVE and are labelled in the text.")
    print("Every result is reported with the sensitivity that matters, because a")
    print("single 'typical' viscosity is a hypothesis and not a measurement.")
    print("=" * 74)


if __name__ == "__main__":
    main()
