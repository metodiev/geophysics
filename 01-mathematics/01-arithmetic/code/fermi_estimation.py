"""Order-of-magnitude estimation utilities for geophysics.

Run:  python3 fermi_estimation.py
Requires: Python standard library only.

Companion to lesson 01-01-02. These helpers are written to be reused later as
quick feasibility checks before committing to a survey design or a costly
computation.
"""

from __future__ import annotations

import math

G = 6.674e-11          # gravitational constant, m^3 kg^-1 s^-2
MGAL = 1.0e-5          # 1 mGal in m/s^2
YEAR = 3.156e7         # seconds in a Julian year

# Anchors, quoted to roughly one significant figure (see lesson Section 2.3).
ANCHORS = {
    "earth_radius_m": 6.371e6,
    "earth_mass_kg": 5.972e24,
    "mean_crust_density_kg_m3": 2.7e3,
    "p_velocity_crust_m_s": 6.0e3,
    "g_surface_m_s2": 9.81,
    "surface_heat_flow_mW_m2": 7.0e1,
    "mantle_viscosity_Pa_s": 1.0e21,
    "thermal_diffusivity_m2_s": 1.0e-6,
}


def gravity_anomaly_cylinder_mgal(
    radius_m: float, depth_m: float, density_contrast_kg_m3: float
) -> float:
    """Peak vertical gravity anomaly above an infinite horizontal cylinder.

    g_z = 2*pi*G*drho*a^2 / z, converted from m/s^2 to mGal.

    Validity: the cylinder length must greatly exceed the observation distance,
    and the observation point must lie directly above the axis. Note the two
    scalings worth memorising: g_z ~ 1/z with depth, and g_z ~ a^2 with radius.
    """
    g_si = 2.0 * math.pi * G * density_contrast_kg_m3 * radius_m ** 2 / depth_m
    return g_si / MGAL


def diffusion_time_seconds(length_m: float, diffusivity_m2_s: float) -> float:
    """Characteristic diffusion time, tau ~ L^2 / kappa (order of magnitude).

    The prefactor (of order 0.1 for the usual step-change problem) is not
    supplied by dimensional analysis; only the scaling exponents are. See
    exercise ***9.
    """
    return length_m ** 2 / diffusivity_m2_s


def magnetic_dipole_field_nT(
    moment_A_m2: float, distance_m: float, mu0: float = 4e-7 * math.pi
) -> float:
    """Approximate equatorial field of a dipole, in nanotesla.

    On the magnetic equator the field magnitude is mu0*m/(4*pi*r^3). This is
    also the formula used to estimate the anomaly of a small buried ferrous
    object treated as an induced dipole.
    """
    b_tesla = mu0 * moment_A_m2 / (4.0 * math.pi * distance_m ** 3)
    return b_tesla * 1e9


def report(label: str, value: float, unit: str) -> None:
    print(f"{label:<52} {value:>12.3e} {unit}")


def main() -> None:
    print("=" * 80)
    print("1. Feasibility: air-filled tunnel under 25 m of soil")
    print("=" * 80)
    a = 3.0                    # radius of a 6 m diameter tunnel
    z = 25.0                   # depth to axis
    drho = -(2000.0 - 1.0)     # air in soil: a large NEGATIVE contrast
    anomaly = gravity_anomaly_cylinder_mgal(a, z, drho)
    resolution = 0.010         # mGal
    report("peak anomaly", anomaly, "mGal")
    report("survey resolution", resolution, "mGal")
    print(f"{'signal-to-resolution ratio':<52} {abs(anomaly) / resolution:>12.2f}")
    verdict = ("DETECTABLE but marginal (SNR < 10)"
               if 1 < abs(anomaly) / resolution < 10
               else "review survey design")
    print("Verdict:", verdict)

    print()
    print("=" * 80)
    print("2. Point-mass anomaly vs mass and depth")
    print("=" * 80)
    for mass_kg in (1e9, 1e10, 1e11):
        for depth in (100.0, 300.0, 1000.0):
            g_si = G * mass_kg / depth ** 2
            print(f"  M = {mass_kg:.0e} kg, depth = {depth:>6.0f} m -> "
                  f"{g_si / MGAL:>10.4f} mGal")

    print()
    print("=" * 80)
    print("3. Diffusion timescale tau ~ L^2 / kappa")
    print("=" * 80)
    for length, name in ((10.0, "10 m"), (100.0, "100 m"),
                         (1000.0, "1 km"), (1e5, "100 km")):
        tau = diffusion_time_seconds(length, ANCHORS["thermal_diffusivity_m2_s"])
        print(f"  heat over {name:>7}: {tau:>10.3e} s = {tau / YEAR:>10.3e} yr")
        tau_h = diffusion_time_seconds(length, 1e-2)
        print(f"  {'':>11} (hydraulic, kappa=1e-2 m^2/s): "
              f"{tau_h / 86400:>10.3e} days")

    print()
    print("=" * 80)
    print("4. Earth's dipole moment and surface field at the equator")
    print("=" * 80)
    # Order-of-magnitude anchor for the present geomagnetic dipole moment.
    dip = 8.0e22   # A m^2, approximately the current axial dipole moment
    r = ANCHORS["earth_radius_m"]
    report("equatorial dipole field", magnetic_dipole_field_nT(dip, r), "nT")
    print("Compare with the anchored surface range 25 000 - 65 000 nT.")

    print()
    print("=" * 80)
    print("5. Sanity check: catch an absurd model output")
    print("=" * 80)
    implausible = 2400.0   # mGal claimed over a mine shaft
    plausible_max = 300.0  # mGal, crustal-scale Bouguer anomaly
    print(f"claimed anomaly       = {implausible} mGal")
    print(f"plausible upper bound = {plausible_max} mGal")
    print("Verdict:", "REJECT - physically implausible"
          if implausible > 3 * plausible_max else "plausible")


if __name__ == "__main__":
    main()
