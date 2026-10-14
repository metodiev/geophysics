#!/usr/bin/env python3
"""EM for geothermal systems and permafrost: the temperature dependence of rock
conductivity, the layered response of a frozen layer and of a clay-capped
geothermal section, the detectability of a thickness change, and the
temperature change a monitoring survey can resolve.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python em_geothermal_permafrost_demo.py

Everything is SYNTHETIC.  Conductivities, temperatures, activation energies,
layer thicknesses, frequencies and noise are chosen teaching values, not
measurements of any real field, well, reservoir or instrument.

Contents
--------
1. Conductivity against temperature: an Arrhenius pore-fluid model.
2. A frozen layer over unfrozen ground: response and detection limit.
3. A clay cap over a reservoir: what the response constrains.
4. Monitoring: the temperature change a 1% measurement can resolve.
"""

import numpy as np
from scipy.integrate import simpson
from scipy.special import j0

RNG = np.random.default_rng(20261014)
MU0 = 4.0e-7 * np.pi
H_COIL = 0.5
R_GAS = 8.314462618          # J/(mol K), exact by definition


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def field_reflection(lam, omega, layers):
    """Magnetic-field reflection coefficient (image convention) of a layered
    earth, from the TE-mode admittance recursion."""
    lam = np.asarray(lam, dtype=float)
    q = 1j * omega * MU0
    sig_b, _ = layers[-1]
    u = np.sqrt(lam ** 2 + q * sig_b)
    Z = 1j * omega * MU0 / u
    for sig, h in reversed(layers[:-1]):
        u = np.sqrt(lam ** 2 + q * sig)
        Zj = 1j * omega * MU0 / u
        t = np.tanh(u * h)
        Z = Zj * (Z + Zj * t) / (Zj + Z * t)
    Z0 = 1j * omega * MU0 / lam
    return -(Z - Z0) / (Z + Z0)


def secondary_field(omega, layers, r, h=H_COIL, n_lam=4000, factor=60.0):
    """Secondary vertical field per unit source moment (1/m); see the TEM lesson
    for the kernel and its validation."""
    sig_max = max(sig for sig, _ in layers)
    lam_max = max(factor / r, factor * np.sqrt(omega * MU0 * sig_max),
                  factor / (2.0 * h))
    lam = np.logspace(np.log10(1.0e-9 / r), np.log10(lam_max), n_lam)
    integrand = (lam ** 2 * field_reflection(lam, omega, layers)
                 * np.exp(-2.0 * lam * h) * j0(lam * r))
    return simpson(integrand, x=lam) / (4.0 * np.pi)


def ratio(omega, layers, ref_layers, r, h=H_COIL):
    """|H_s| for a model divided by |H_s| for a reference model."""
    return abs(secondary_field(omega, layers, r, h)) \
        / abs(secondary_field(omega, ref_layers, r, h))


def main():
    section("1. Conductivity against temperature: an Arrhenius model")
    sigma_25 = 0.05      # S/m at 25 degC (synthetic pore-fluid-dominated value)
    E_act = 15.0e3       # J/mol, assumed activation energy (stated)
    print("model: sigma(T) = sigma25 exp[ (Ea/R) (1/298.15 - 1/T) ]")
    print(f"  sigma25 = {sigma_25:.4f} S/m at 298.15 K, Ea = "
          f"{E_act / 1000:.1f} kJ/mol (assumed), R = {R_GAS:.9f} J/(mol K)")
    print("\n  T (degC)   T (K)     sigma (S/m)   rho (ohm m)   sigma/sigma25")
    for tc in (0.0, 25.0, 50.0, 100.0, 200.0, 300.0):
        t_k = tc + 273.15
        sig = sigma_25 * np.exp(E_act / R_GAS * (1.0 / 298.15 - 1.0 / t_k))
        print(f"  {tc:8.1f}   {t_k:7.2f}   {sig:11.5f}   {1.0 / sig:11.2f}   "
              f"{sig / sigma_25:12.4f}")
    print("the conductivity rises by a factor 5.87 from 0 to 100 degC and by")
    print("31.7 from 0 to 300 degC at this assumed activation energy: a hot rock")
    print("is a")
    print("conductor, which is why a conductive anomaly is a geothermal")
    print("indicator - and why a cold, resistive one is a permafrost indicator.")
    print("the activation energy is the dominant uncertainty: it controls the")
    print("exponent, and it is a property of the pore fluid and the mineral")
    print("surfaces, not something an EM survey measures.")

    section("2. A frozen layer over unfrozen ground")
    print("frozen ground is modelled as a resistive layer (sigma = 0.002 S/m,")
    print("about 500 ohm m) of thickness t over an unfrozen half-space of")
    print("0.05 S/m (20 ohm m); a loop at 0.5 m height, offset 20 m")
    print("\n  t (m)    f = 10 Hz    f = 100 Hz   f = 1000 Hz   f = 10000 Hz")
    unfrozen = [(0.05, np.inf)]
    for t in (2.0, 5.0, 10.0, 20.0, 40.0):
        row = []
        for f in (10.0, 100.0, 1000.0, 10000.0):
            w = 2.0 * np.pi * f
            row.append(ratio(w, [(0.002, t), (0.05, np.inf)], unfrozen, 20.0))
        print(f"  {t:6.1f}   {row[0]:11.4f}   {row[1]:11.4f}   "
              f"{row[2]:11.4f}   {row[3]:12.4f}")
    print("(each entry is the |H_s| of the frozen model divided by the |H_s| of")
    print("the unfrozen half-space)")
    print("a 2 m frozen layer is already a 2.9% response change at 1000 Hz, and a")
    print("20 m layer is a factor 2.4 at 100 Hz: the detectable thickness is")
    print("therefore a stated-noise question, not a physics question.  At a 1%")
    print("response threshold the table gives a detection limit of about 2 m")
    print("across the whole band, and the response keeps growing with thickness")
    print("(0.4202 for 20 m against 0.2201 for 40 m at 100 Hz), so the method")
    print("trades thickness resolution against the noise level rather than")
    print("saturating.")

    section("3. A clay cap over a reservoir")
    print("a conductive clay cap (sigma = 0.2 S/m) of thickness t over a")
    print("resistive reservoir (0.001 S/m) of thickness 200 m, over a basement")
    print("of 0.02 S/m; the reference is the same model without the cap")
    print("\n  cap thickness (m)   f = 1 Hz   f = 10 Hz   f = 100 Hz   f = 1000 Hz")
    no_cap = [(0.001, 200.0), (0.02, np.inf)]
    for t in (10.0, 50.0, 100.0, 200.0):
        row = []
        for f in (1.0, 10.0, 100.0, 1000.0):
            w = 2.0 * np.pi * f
            row.append(ratio(w, [(0.2, t), (0.001, 200.0), (0.02, np.inf)],
                             no_cap, 20.0))
        print(f"  {t:17.1f}   {row[0]:9.4f}   {row[1]:10.4f}   "
              f"{row[2]:11.4f}   {row[3]:12.4f}")
    print("the cap's influence is large everywhere in this band (a factor 34 to")
    print("126), and its maximum moves from 1000 Hz for a 10 m cap to 100 Hz for")
    print("a 50-200 m cap: the sensitivity tracks the cap in the diffusive way.")
    print("Once the cap is thick the response saturates (126.31 for 100 m against")
    print("126.10 for 200 m at 100 Hz), so a thick cap cannot be separated from a")
    print("thicker one.  Two consequences: the response reports the cap, not the")
    print("reservoir 100 m below it, and the mapping from response to cap")
    print("thickness is many-to-one.  That is the classical geothermal problem,")
    print("and it is why an MT or EM survey over a geothermal field is inverted")
    print("for a conductivity model and then interpreted jointly with")
    print("temperature and alteration data rather than read as a temperature.")

    section("4. Monitoring: the temperature change a 1% measurement resolves")
    print("take the Arrhenius model of section 1 and ask what temperature change")
    print("moves the response of a half-space by 1%, the stated noise level")
    print("(a 1% change in |H_s| is a 0.5% change in conductivity in the LIN")
    print("regime, since the quadrature is linear in sigma)")
    print("\n  T (degC)   dsigma/dT per K (relative)   dT for a 0.5% sigma "
          "change (K)")
    base = [(0.05, np.inf)]
    for tc in (0.0, 25.0, 100.0, 200.0):
        t_k = tc + 273.15
        sig = 0.05 * np.exp(E_act / R_GAS * (1.0 / 298.15 - 1.0 / t_k))
        dsig = sig * E_act / (R_GAS * t_k ** 2)      # per kelvin
        d_rel = dsig / sig
        print(f"  {tc:8.1f}   {d_rel:26.6f}   {0.005 / d_rel:29.2f}")
    print("the measured numbers are 0.21 K at 0 degC, 0.25 K at 25 degC and")
    print("0.62 K at 200 degC: the relative sensitivity to temperature is LARGEST")
    print("at low temperature, because the Arrhenius exponent carries Ea/(R T^2).")
    print("Monitoring is therefore easier in a cool system than in a hot one -")
    print("the opposite of the naive expectation, and a direct consequence of")
    print("the assumed model.  A temperature change")
    print("that is resolved by the resistivity is not a temperature *at* a")
    print("depth - converting one into the other needs the petrophysical model")
    print("of section 1, which is exactly the assumption that a monitoring")
    print("survey cannot check.  Every number in this demo is therefore a")
    print("statement about a synthetic model, not a measurement of any field.")


if __name__ == "__main__":
    main()
