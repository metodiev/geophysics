"""Check the gravity, magnetics and potential-theory formula sheet.

Print-only, seeded, no plots, no file I/O. Numbers quoted in
26-03-04-formulas-potential-fields.md come from this output.

Run with:  .venv/bin/python 26-reference-library/03-formula-handbook/code/formulas_potential_fields_demo.py
"""

from __future__ import annotations

import math

import numpy as np
from scipy.constants import G, mu_0

SEED = 20261014
M_GAL = 1.0e-5            # m/s^2 per mGal
EOTVOS = 1.0e-9           # s^-2 per Eotvos


def banner(n: int, title: str) -> None:
    print(f"\n[{n}] {title}")


def main() -> None:
    rng = np.random.default_rng(SEED)
    print("Gravity, magnetics and potential theory formula sheet -- numerical checks")
    print(f"numpy {np.__version__}, seeded rng = default_rng({SEED})")
    print(f"G = {G:.6e} m^3 kg^-1 s^-2 (CODATA), mu_0 = {mu_0:.6e} H/m")
    print("PROVENANCE: SYNTHETIC -- the source bodies below are illustrative models.")

    banner(1, "Bouguer slab and free-air corrections")
    rho, thick = 2670.0, 100.0
    slab = 2.0 * math.pi * G * rho * thick
    print(f"  rho = {rho:.0f} kg/m^3, thickness = {thick:.0f} m")
    rho_cgs = rho / 1000.0
    print(f"  slab attraction 2*pi*G*rho*h = {slab:.6e} m/s^2 = {slab / M_GAL:.4f} mGal")
    print(f"  rule of thumb 0.04193*rho[g/cm^3]*h = {0.04193 * rho_cgs * thick:.4f} mGal")
    g_n = 9.80665
    print(f"  free-air gradient 2*g_n/a, a = 6371 km   = {2.0 * g_n / 6371.0e3 / M_GAL:.6f} mGal/m")
    print(f"  free-air gradient 2*g_n/a, a = 6356.752 km = {2.0 * g_n / 6356752.0 / M_GAL:.6f} mGal/m")

    banner(2, "Vertical and horizontal attraction of a buried sphere")
    radius, drho, depth = 500.0, 300.0, 1000.0
    mass = (4.0 / 3.0) * math.pi * radius**3 * drho
    gm = G * mass
    print(f"  radius = {radius:.0f} m, density contrast = {drho:.0f} kg/m^3, depth to centre = {depth:.0f} m")
    print(f"  mass = {mass:.6e} kg, G*m = {gm:.6e} m^3/s^2")
    for offset in (0.0, 1000.0):
        rr = offset**2 + depth**2
        gz = gm * depth / rr**1.5
        gx = gm * offset / rr**1.5
        print(
            f"  x = {offset:6.0f} m: g_z = {gz / M_GAL:+.6f} mGal, "
            f"g_x = {gx / M_GAL:+.6f} mGal, |g| = {math.hypot(gz, gx) / M_GAL:.6f} mGal"
        )
    gz_max = gm / depth**2
    print(f"  maximum g_z (at x = 0)        = {gz_max / M_GAL:.6f} mGal")
    x_half = math.sqrt(2.0 ** (2.0 / 3.0) - 1.0) * depth
    print(f"  x at half maximum = 0.766*z = {x_half:.1f} m")
    print(f"  inverse half-width rule: z = 1.305 * x_half = {1.305 * x_half:.1f} m")

    banner(3, "Vertical derivative of the sphere anomaly (gradient units)")
    x0, z0 = 0.0, depth
    r2 = x0**2 + z0**2
    dgz_dz = gm * (x0**2 - 2.0 * z0**2) / r2**2.5
    print(f"  d g_z / d z at x = 0 = {dgz_dz:.6e} s^-2 = {dgz_dz / EOTVOS:.4f} E")
    print(f"  analytic check -2*G*m/z^3 = {-2.0 * gm / z0**3 / EOTVOS:.4f} E")

    banner(4, "Upward continuation of a sinusoid")
    amplitude, wavelength, height = 50.0, 20000.0, 2000.0
    k_wave = 2.0 * math.pi / wavelength
    factor = math.exp(-k_wave * height)
    print(f"  amplitude = {amplitude:.1f} nT, wavelength = {wavelength:.0f} m, height = {height:.0f} m")
    print(f"  wavenumber k = {k_wave:.6e} m^-1, continuation factor = {factor:.6f}")
    print(f"  amplitude after continuation = {amplitude * factor:.4f} nT")

    banner(5, "Magnetic dipole field of a uniformly magnetised sphere")
    magnetisation = 1.0
    dipole = magnetisation * (4.0 / 3.0) * math.pi * radius**3
    axial = {}
    for distance in (1000.0, 2000.0):
        axial[distance] = mu_0 * dipole * 2.0 / (4.0 * math.pi * distance**3)
        equatorial = mu_0 * dipole * 1.0 / (4.0 * math.pi * distance**3)
        print(
            f"  r = {distance:6.0f} m: B_axial = {axial[distance] * 1e9:8.4f} nT, "
            f"B_equatorial = {equatorial * 1e9:8.4f} nT"
        )
    print(f"  dipole moment m = {dipole:.6e} A m^2 (M = {magnetisation:.1f} A/m)")
    print(f"  1/r^3 test: B(1000)/B(2000) = {axial[1000.0] / axial[2000.0]:.4f} (exact 8)")

    print("\nAll five checks completed; exit status 0.")


if __name__ == "__main__":
    main()
