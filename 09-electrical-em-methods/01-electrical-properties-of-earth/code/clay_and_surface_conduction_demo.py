#!/usr/bin/env python3
"""Clay effects, CEC and membrane polarisation: Q_v, sigma_s, and the phase.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python clay_and_surface_conduction_demo.py

Everything is SYNTHETIC.  The cation exchange capacities, the grain density, the
counter-ion equivalent conductance and the Debye relaxation parameters are chosen
teaching values, not measurements.

Contents
--------
1. CEC to Q_v: the cation excess per unit pore volume.
2. Surface conductivity sigma_s = beta Q_v, and its size relative to Archie.
3. The clay problem: an apparent water saturation above 1, and its repair.
4. Membrane polarisation: Debye complex conductivity, amplitude and phase.
5. A verified phase-area identity: (2/pi) integral of |phase| d ln f = ln(sigma_inf/sigma_0).
6. Consistency checks.
"""

import numpy as np
from scipy.integrate import quad

RNG = np.random.default_rng(20261014)

RHO_GRAIN = 2.65            # g/cm^3, SYNTHETIC grain density
BETA_SURFACE = 0.10         # (S/m) per (eq/L), SYNTHETIC teaching constant
MEQ_PER_EQ = 1000.0

SIGMA_W = 0.10              # S/m, synthetic pore-water conductivity
PHI = 0.25                  # synthetic porosity
M_ARCHIE = 2.0

SIGMA_0 = 0.050             # S/m, DC conductivity of the Debye model
SIGMA_INF = 0.060           # S/m, high-frequency limit
F_C = 2.0                   # Hz, Debye relaxation frequency (teaching value)


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def qv_from_cec(cec_meq_per_100g, phi, rho_grain=RHO_GRAIN):
    """Cation excess per unit pore volume, in eq/L.

    CEC is in meq per 100 g of solid.  Mass of solid per unit bulk volume is
    rho_grain (1 - phi); pore volume per unit bulk volume is phi.  Converting
    meq to eq and cm^3 to L gives
        Q_v = (CEC/100) * rho_grain * (1 - phi) / phi   [eq/L]
    because 1 meq/cm^3 = 1 eq/L.
    """
    return (cec_meq_per_100g / 100.0) * rho_grain * (1.0 - phi) / phi


def debye_sigma(f_hz, sigma_0=SIGMA_0, sigma_inf=SIGMA_INF, f_c=F_C):
    """Debye complex conductivity: sigma*(f) = sigma_inf - (sigma_inf-sigma_0)/(1+i f/f_c)."""
    return sigma_inf - (sigma_inf - sigma_0) / (1.0 + 1j * f_hz / f_c)


def main():
    section("1. From CEC to the pore-volume cation excess Q_v")
    print(f"  SYNTHETIC constants: grain density {RHO_GRAIN:.2f} g/cm^3,")
    print("  Q_v = (CEC/100) rho_g (1-phi)/phi   [eq/L]")
    print("     CEC (meq/100 g)   phi     Q_v (eq/L)   Q_v (meq/mL)")
    for phi in (0.15, 0.25, 0.40):
        for cec in (1.0, 5.0, 10.0, 25.0):
            qv = qv_from_cec(cec, phi)
            print(f"  {cec:16.1f} {phi:6.2f} {qv:13.4f} {qv * MEQ_PER_EQ:14.1f}")
    print("  Q_v rises as porosity falls at fixed CEC: the same clay fabric is")
    print("  concentrated into less pore space.")

    section("2. Surface conductivity sigma_s = beta Q_v versus sigma_w / F")
    F_ar = PHI ** (-M_ARCHIE)
    sig_ar = SIGMA_W / F_ar
    print(f"  SYNTHETIC sample: phi = {PHI:.2f} -> F = {F_ar:.2f}, "
          f"sigma_w = {SIGMA_W:.2f} S/m")
    print(f"  purely electrolytic (Archie) conductivity sigma_w/F = "
          f"{sig_ar:.5f} S/m")
    print(f"  counter-ion conductance beta = {BETA_SURFACE:.3f} (S/m) per (eq/L)")
    print("     CEC (meq/100 g)   Q_v (eq/L)   sigma_s (S/m)   sigma_s * F/sigma_w")
    for cec in (1.0, 5.0, 10.0, 25.0):
        qv = qv_from_cec(cec, PHI)
        s_s = BETA_SURFACE * qv
        print(f"  {cec:16.1f} {qv:13.4f} {s_s:14.5f} {s_s / sig_ar:20.1f}")
    print("  at CEC = 10 meq/100 g the surface term is already more than ten")
    print("  times the electrolytic term in this synthetic rock.")

    section("3. The clay problem: an impossible water saturation")
    cec = 10.0
    qv = qv_from_cec(cec, PHI)
    s_s = BETA_SURFACE * qv
    sigma_meas = sig_ar + s_s
    print(f"  CEC = {cec:.1f} meq/100 g, phi = {PHI:.2f}, "
          f"sigma_w = {SIGMA_W:.2f} S/m")
    print(f"  sigma_measured = sigma_w/F + sigma_s = {sig_ar:.5f} + {s_s:.5f} "
          f"= {sigma_meas:.5f} S/m")
    print(f"  surface term is {s_s / sigma_meas * 100:.1f}% of the total")
    S_naive = (sigma_meas / sig_ar) ** (1.0 / 2.0)
    print(f"\n  Archie read directly: S = (sigma/sigma_0)^(1/n) with n = 2 gives")
    print(f"    S = {S_naive:.3f}   <-- a saturation of {S_naive * 100:.0f}%, "
          f"physically impossible")
    S_fixed = ((sigma_meas - s_s) / sig_ar) ** (1.0 / 2.0)
    print(f"  after subtracting sigma_s: S = "
          f"((sigma - sigma_s)/sigma_0)^(1/2) = {S_fixed:.3f}")
    print("  the clay term was being read as water: the uncorrected answer is")
    print("  not merely wrong, it violates the definition of saturation.")
    print("\n  sensitivity: what a wrong beta does to the saturation estimate")
    for beta_try in (0.0, 0.05, 0.10, 0.20, 0.30):
        s_try = beta_try * qv
        numer = sigma_meas - s_try
        if numer <= 0.0:
            print(f"    beta = {beta_try:.2f}: no real solution "
                  f"(over-corrected; the model itself is inconsistent)")
        else:
            print(f"    beta = {beta_try:.2f}: S = {np.sqrt(numer / sig_ar):.4f}")
    print("  S is a square root of a difference of two similar numbers: this is")
    print("  the worst-conditioned step in the whole workflow.")

    section("4. Membrane polarisation: Debye complex conductivity")
    m_dc = (SIGMA_INF - SIGMA_0) / SIGMA_INF
    tau = 1.0 / (2.0 * np.pi * F_C)
    print(f"  SYNTHETIC Debye model: sigma_0 = {SIGMA_0:.3f} S/m (DC), "
          f"sigma_inf = {SIGMA_INF:.3f} S/m, f_c = {F_C:.2f} Hz")
    print(f"  chargeability m = (sigma_inf - sigma_0)/sigma_inf = {m_dc:.4f}")
    print(f"  relaxation time tau = 1/(2 pi f_c) = {tau * 1e3:.3f} ms")
    print("      f (Hz)   |sigma| (S/m)   phase (mrad)   phase (deg)")
    for f in (1e-3, 1e-2, 1e-1, 0.5, F_C, 5.0, 50.0, 500.0, 1e4):
        s = debye_sigma(f)
        ph = np.angle(s)
        print(f"  {f:10.4g} {abs(s):14.6f} {ph * 1e3:15.4f} "
              f"{np.degrees(ph):14.5f}")
    fgrid = np.logspace(-4, 6, 2001)
    phg = np.abs(np.angle(debye_sigma(fgrid)))
    print(f"\n  peak |phase| = {np.degrees(phg.max()):.4f} deg at "
          f"f = {fgrid[phg.argmax()]:.4f} Hz")
    print("  the phase peaks near f_c, not at the lowest frequency: a DC")
    print("  resistivity survey sits at the far left of this table.")

    section("5. Phase-area identity, verified numerically")
    integrand = lambda lnf: np.abs(np.angle(debye_sigma(np.exp(lnf))))
    area, err = quad(integrand, np.log(1e-7), np.log(1e7), limit=500)
    lhs = 2.0 / np.pi * area
    rhs = np.log(SIGMA_INF / SIGMA_0)
    print(f"  (2/pi) * integral |phase| d ln f = {lhs:.9f}")
    print(f"  ln(sigma_inf/sigma_0)            = {rhs:.9f}")
    print(f"  -ln(1 - m)                       = {-np.log(1 - m_dc):.9f}")
    print(f"  |difference| = {abs(lhs - rhs):.3e} (quadrature error estimate "
          f"{err:.1e})")
    print(f"  first-order reading: m = {m_dc:.6f} differs from the area "
          f"{lhs:.6f} by {(lhs - m_dc) / m_dc * 100:.2f}%")
    print("  so a phase measurement gives ln(sigma_inf/sigma_0), and calling")
    print("  that number 'chargeability' is a first-order approximation.")

    section("6. Consistency checks")
    print(f"  Q_v at CEC = 10, phi = 0.25: {qv_from_cec(10.0, 0.25):.6f} eq/L")
    print(f"  sigma at f -> 0: {abs(debye_sigma(1e-9)):.9f} S/m "
          f"(model sigma_0 = {SIGMA_0:.3f})")
    print(f"  sigma at f -> inf: {abs(debye_sigma(1e9)):.9f} S/m "
          f"(model sigma_inf = {SIGMA_INF:.3f})")
    print(f"  S_fixed * sigma_0 should return the measured conductivity minus the")
    print(f"    surface term: {S_fixed ** 2 * sig_ar:.6f} versus "
          f"{sigma_meas - s_s:.6f}")


if __name__ == "__main__":
    main()
