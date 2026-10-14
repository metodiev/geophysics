#!/usr/bin/env python3
"""Resistivity and conductivity: definitions, units, geometry and error control.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python resistivity_conductivity_demo.py

Everything here is SYNTHETIC.  The resistivity catalogue below is a chosen
teaching catalogue, not a set of measurements, and no field site or instrument is
referred to.

Contents
--------
1. A synthetic teaching catalogue of resistivities, with conductivities.
2. Ohm's law in the continuum: J = sigma E, resistance R = rho L / A.
3. Verification that the half-space point-source field carries the injected
   current, by direct numerical integration of the current density over the
   hemisphere.
4. Resistance of a hemispherical electrode: R = rho / (2 pi a).
5. Error propagation: which measurement error matters for a laboratory
   conductivity estimate, and for an in-situ one.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC teaching catalogue (chosen values, not measurements) ----------
# Resistivity in ohm m.  Chosen to span the range met in near-surface work.
CATALOGUE = [
    ("massive sulphide ore (connected)", 0.1),
    ("graphitic schist", 1.0),
    ("clay, saturated", 5.0),
    ("shale", 20.0),
    ("sandstone, saturated brackish water", 30.0),
    ("sandstone, saturated fresh water", 200.0),
    ("limestone, dry", 5000.0),
    ("granite, dry", 100000.0),
]

RHO_REF = 100.0          # ohm m, reference half-space used throughout
I_REF = 0.1              # A, reference injected current
L_CORE, R_CORE = 0.100, 0.025   # m, core-plug length and radius


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def half_space_potential(rho, I, r):
    """Potential of a point current source on a uniform half-space, in volts.

    V(r) = rho I / (2 pi r): current spreads over a hemisphere, so the current
    density is J(r) = I / (2 pi r^2) and E = rho J.
    """
    return rho * I / (2.0 * np.pi * r)


def main():
    section("1. A SYNTHETIC teaching catalogue: resistivity and conductivity")
    print("  material                                 rho (ohm m)     sigma (S/m)")
    sig = []
    for name, rho in CATALOGUE:
        sigma = 1.0 / rho
        sig.append(sigma)
        print(f"  {name:<40s} {rho:11.3g}   {sigma:11.3g}")
    sig = np.array(sig)
    print(f"\n  conductivity span of this catalogue: {sig.max():.3g} to "
          f"{sig.min():.3g} S/m")
    print(f"  ratio most / least conductive = {sig.max() / sig.min():.3g} "
          f"({np.log10(sig.max() / sig.min()):.1f} decades)")
    print("  the resistivity scale is logarithmic; this is why resistivity")
    print("  arrows and colour bars are also logarithmic.")

    section("2. Ohm's law: J = sigma E and R = rho L / A")
    A = np.pi * R_CORE ** 2
    print(f"  core plug: L = {L_CORE:.3f} m, radius = {R_CORE:.3f} m, "
          f"A = {A:.6f} m^2")
    for rho in (10.0, 100.0, 1000.0):
        R = rho * L_CORE / A
        print(f"  rho = {rho:8.1f} ohm m -> R = {R:12.1f} ohm")
    R_demo = 1000.0 * L_CORE / A
    I_lab = 1.0e-3                      # A
    print(f"\n  for a 1000 ohm m plug carrying I = {I_lab * 1e3:.1f} mA:")
    J = I_lab / A
    E = 1000.0 * J
    print(f"    current density J = I/A = {J:.4f} A/m^2")
    print(f"    field E = rho J = {E:.4f} V/m")
    print(f"    voltage across the plug V = R I = {R_demo * I_lab:.4f} V")
    print(f"    check: V/L = {R_demo * I_lab / L_CORE:.4f} V/m  (= E)")

    section("3. The half-space point source carries exactly the injected current")
    rho, I = RHO_REF, I_REF
    print(f"  rho = {rho:.1f} ohm m, I = {I:.2f} A")
    print("  V(r) = rho I / (2 pi r);  J(r) = I / (2 pi r^2)")
    print("      r (m)      V (V)      J (A/m^2)   E = rho J (mV/m)")
    for r in (0.5, 1.0, 2.0, 5.0, 10.0, 20.0):
        V = half_space_potential(rho, I, r)
        J = I / (2.0 * np.pi * r ** 2)
        print(f"  {r:8.2f} {V:11.5f} {J:12.4e} {rho * J * 1e3:15.4f}")
    # Verify by numerical integration of the current density over the hemisphere.
    # dA = r^2 sin(theta) dtheta dphi and J = I/(2 pi r^2), so
    #   integral = (I / 2 pi) * 2 pi * integral_0^{pi/2} sin(theta) dtheta = I.
    # Gauss-Legendre quadrature on theta in [0, pi/2] reproduces the exact 1.
    xg, wg = np.polynomial.legendre.leggauss(200)
    theta = 0.5 * np.pi * (xg + 1.0)
    wtheta = 0.5 * np.pi * wg
    hemispheric_integral = np.sum(wtheta * np.sin(theta))
    current = (I / (2.0 * np.pi)) * 2.0 * np.pi * hemispheric_integral
    print(f"\n  quadrature check: integral of sin(theta) over the hemisphere")
    print(f"    = {hemispheric_integral:.12f} (exact value 1)")
    print(f"  numerical check: integral of J over the hemisphere = {current:.12f} A")
    print(f"  injected current                                          = {I:.12f} A")
    print(f"  absolute difference = {abs(current - I):.3e} A")

    section("4. Hemispherical electrode: R = rho / (2 pi a)")
    print("      a (m)    R for rho=100 ohm m (ohm)   R for rho=1000 (ohm)")
    for a in (0.02, 0.05, 0.10, 0.25):
        R1 = RHO_REF / (2.0 * np.pi * a)
        R2 = 1000.0 / (2.0 * np.pi * a)
        print(f"  {a:8.3f} {R1:26.2f} {R2:24.2f}")
    print("  a larger electrode lowers the resistance: contact geometry, not")
    print("  ground resistivity, sets the contact impedance.")

    section("5. Error propagation: which error matters?")
    # (a) Laboratory: sigma = L / (R A).  With L and A known, the error in sigma
    #     equals minus the relative error in R; but a length error scales as
    #     d(sigma)/sigma = -dL/L and a radius error as -2 dr/r.
    print("(a) laboratory core plug, sigma = L/(R A):")
    for dL in (1e-3, 5e-3):
        print(f"    length error {dL * 1e3:+.1f} mm on L = {L_CORE * 1e3:.0f} mm"
              f" -> sigma error {dL / L_CORE * 100:+.2f}%")
    for dr in (0.2e-3, 1.0e-3):
        print(f"    radius error {dr * 1e3:+.1f} mm on r = {R_CORE * 1e3:.0f} mm"
              f" -> sigma error {-2 * dr / R_CORE * 100:+.2f}%")
    print("    a radius is the worse hole to drill: the error is doubled, and")
    print("    a core plug is rarely a perfect cylinder.")

    # (b) In situ: a two-electrode measurement sees the contact resistance.
    print("\n(b) in-situ resistance of an electrode with an added contact")
    print("    resistance (e.g. 200 ohm for a poor contact):")
    for a in (0.02, 0.05, 0.10):
        R_true = RHO_REF / (2.0 * np.pi * a)
        Rc = 200.0
        err = (R_true + Rc) / R_true
        print(f"    a = {a:.2f} m: R_true = {R_true:8.2f} ohm, with contact "
              f"{Rc:.0f} ohm -> {err:.2f}x too large")
    print("    the geometric resistance falls as the electrode grows, so a")
    print("    fixed contact resistance matters MORE for a large electrode:")
    print("    you end up measuring the contact, not the ground.  This is the")
    print("    argument for four electrodes, developed in module 09-02.")

    section("6. Conductivity from a measured resistance (worked inversion)")
    R_meas = R_demo * (1.0 + RNG.normal(0.0, 0.02))     # 2% noise, SYNTHETIC
    sigma_est = L_CORE / (R_meas * A)
    print(f"  synthetic measurement: R = {R_meas:.2f} ohm (2% noise added to "
          f"{R_demo:.2f} ohm)")
    print(f"  sigma = L/(R A) = {sigma_est:.4f} S/m")
    print(f"  rho   = 1/sigma = {1.0 / sigma_est:.1f} ohm m  (true value "
          f"1000.0 ohm m)")
    print(f"  relative error in rho = "
          f"{(1.0 / sigma_est - 1000.0) / 1000.0 * 100:+.2f}% for a 2% "
          f"resistance error")


if __name__ == "__main__":
    main()
