"""Check the electromagnetics and electrical-methods formula sheet.

Print-only, seeded, no plots, no file I/O. Numbers quoted in
26-03-05-formulas-em-electrical.md come from this output.

Run with:  .venv/bin/python 26-reference-library/03-formula-handbook/code/formulas_em_electrical_demo.py
"""

from __future__ import annotations

import cmath
import math

import numpy as np
from scipy.constants import c, mu_0

SEED = 20261014


def banner(n: int, title: str) -> None:
    print(f"\n[{n}] {title}")


def main() -> None:
    rng = np.random.default_rng(SEED)
    print("Electromagnetics and electrical methods formula sheet -- numerical checks")
    print(f"numpy {np.__version__}, seeded rng = default_rng({SEED})")
    print(f"mu_0 = {mu_0:.6e} H/m, c = {c:.6e} m/s")
    print("PROVENANCE: SYNTHETIC -- conductivities below are chosen test values.")

    banner(1, "Skin depth in a conductive half-space")
    for freq, sigma in ((1.0, 0.01), (1.0, 0.001), (100.0, 0.01)):
        omega = 2.0 * math.pi * freq
        delta = math.sqrt(2.0 / (omega * mu_0 * sigma))
        print(
            f"  f = {freq:6.1f} Hz, sigma = {sigma:.3f} S/m -> "
            f"delta = {delta:10.1f} m = {delta / 1000.0:6.3f} km"
        )
    omega = 2.0 * math.pi * 1.0
    print(f"  ratio test (sigma 0.01 -> 0.001, f = 1 Hz): {math.sqrt(10.0):.4f} (= sqrt 10)")

    banner(2, "Magnetotelluric impedance of a uniform half-space")
    sigma = 0.01
    for period in (10.0, 100.0, 1000.0):
        omega = 2.0 * math.pi / period
        z_imp = cmath.sqrt(1j * omega * mu_0 / sigma)
        rho_app = abs(z_imp) ** 2 / (omega * mu_0)
        phase = math.degrees(cmath.phase(z_imp))
        print(
            f"  T = {period:7.1f} s: |Z| = {abs(z_imp):.6e} ohm, "
            f"rho_a = {rho_app:.4f} ohm m, phase = {phase:.3f} deg"
        )
    print(f"  half-space identity 1/sigma = {1.0 / sigma:.4f} ohm m")

    banner(3, "DC resistivity: geometric factors and apparent resistivity")
    a_spacing = 10.0
    resistance = 10.0
    print(f"  Wenner array, a = {a_spacing:.1f} m, V/I = {resistance:.1f} ohm")
    print(f"  geometric factor K = 2*pi*a = {2.0 * math.pi * a_spacing:.6f} m")
    print(f"  apparent resistivity = K*V/I = {2.0 * math.pi * a_spacing * resistance:.4f} ohm m")
    half_current, half_potential = 100.0, 10.0
    k_schl = math.pi * (half_current**2 - half_potential**2) / (2.0 * half_potential)
    print(f"  Schlumberger, L = {half_current:.0f} m, l = {half_potential:.0f} m:")
    print(f"    K = pi*(L^2 - l^2)/(2*l) = {k_schl:.6f} m")
    print(f"    apparent resistivity = {k_schl * resistance:.4f} ohm m (same V/I)")
    print(f"  current density J = I/A for I = 1 A in 0.01 m^2 = {1.0 / 0.01:.3f} A/m^2")

    banner(4, "Ground-penetrating radar: velocity, wavelength and resolution")
    eps_r = 9.0
    velocity = c / math.sqrt(eps_r)
    for freq_mhz in (100.0, 400.0):
        wavelength = velocity / (freq_mhz * 1e6)
        print(
            f"  f = {freq_mhz:5.1f} MHz: v = {velocity:.6e} m/s, "
            f"lambda = {wavelength:.4f} m, lambda/4 = {wavelength / 4.0:.4f} m"
        )

    banner(5, "Induction number and low-frequency limit")
    spacing, delta = 20.0, 100.0
    print(f"  spacing = {spacing:.1f} m, skin depth = {delta:.1f} m")
    print(f"  induction number B = spacing/delta = {spacing / delta:.6f}")
    print(f"  regime: {'resistive (low induction)' if spacing / delta < 1 else 'inductive'}")

    banner(6, "Transient EM: time constant of a conductive sphere")
    sigma_sphere, radius_sphere = 0.01, 500.0
    tau = mu_0 * sigma_sphere * radius_sphere**2 / math.pi**2
    print(f"  sigma = {sigma_sphere:.3f} S/m, radius = {radius_sphere:.0f} m")
    print(f"  tau = mu_0*sigma*a^2/pi^2 = {tau:.6e} s = {tau * 1e3:.6f} ms")
    for ratio in (1.0, 3.0, 5.0):
        print(f"  t = {ratio:4.1f} tau: normalised response exp(-t/tau) = {math.exp(-ratio):.6e}")
    print("  note: a real transient response is a sum over modes; the single-time-constant")
    print("        form is the leading behaviour, not an exact waveform")

    banner(7, "Magnetic field of a current loop")
    current, loop_radius = 10.0, 0.5
    b_centre = mu_0 * current / (2.0 * loop_radius)
    print(f"  I = {current:.1f} A, a = {loop_radius:.1f} m")
    print(f"  B at the centre = {b_centre:.6e} T = {b_centre * 1e6:.4f} uT")
    print(f"  Earth's field for scale: 50 uT = {50e-6:.1e} T (nominal mid-latitude total field)")

    print("\nAll seven checks completed; exit status 0.")


if __name__ == "__main__":
    main()
