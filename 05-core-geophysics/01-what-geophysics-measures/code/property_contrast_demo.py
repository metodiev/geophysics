"""Property contrast -> signal: what a geophysical method actually measures.

Every geophysical method is the same story three times: a *contrast* in a
physical property produces a *field* that a sensor records, and the record is
usable only if it rises above the *noise*.

This script quantifies that chain for three synthetic examples, using only
formulas derived in the lessons:

  1. gravity  -- excess mass at depth -> g_z
  2. magnetics -- magnetised body -> total-field anomaly dT
  3. seismics -- impedance contrast -> reflection coefficient R

All model inputs are SYNTHETIC and stated.  All constants are SI and labelled.

Run:  python3 property_contrast_demo.py
"""

from __future__ import annotations

import numpy as np

G = 6.67430e-11        # m^3 kg^-1 s^-2   (CODATA 2018, NIST)
MU0 = 1.25663706212e-6  # H/m              (CODATA 2018, NIST)
MGAL = 1.0e-5          # m/s^2 per mGal
NT = 1.0e-9            # T per nT


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def sphere_gz(delta_rho, radius, depth, obs_offset=0.0):
    """Vertical gravity of a buried uniform sphere, in m/s^2.

    Exact outside the sphere: the field is that of a point mass
    m = delta_rho * (4/3) pi a^3 at the centre.  Depth is to the centre.
    """
    m = delta_rho * 4.0 / 3.0 * np.pi * radius**3
    r = np.hypot(obs_offset, depth)
    return G * m * depth / r**3


def dipole_dT(m_moment, depth, inclination_deg, obs_offset=0.0):
    """Total-field anomaly of a vertical dipole at depth, in tesla.

    dT ~= B_hat . B_dipole with the ambient field at the stated inclination.
    """
    inc = np.radians(inclination_deg)
    bhat = np.array([np.cos(inc), 0.0, np.sin(inc)])
    rvec = np.array([obs_offset, 0.0, -depth])          # source -> observer
    r = np.linalg.norm(rvec)
    rhat = rvec / r
    mvec = np.array([0.0, 0.0, m_moment])
    b = MU0 / (4.0 * np.pi) * (3.0 * np.dot(mvec, rhat) * rhat - mvec) / r**3
    return float(np.dot(bhat, b))


def reflection_coefficient(rho1, v1, rho2, v2):
    """Normal-incidence P-wave reflection coefficient (impedance contrast)."""
    z1, z2 = rho1 * v1, rho2 * v2
    return (z2 - z1) / (z2 + z1)


def main() -> None:
    print("All model inputs below are SYNTHETIC and are stated explicitly.")

    # ==================================================================
    section("1. Gravity: excess mass at depth vs instrument noise")
    # SYNTHETIC: a sphere of 60 m radius with density contrast 500 kg/m^3.
    delta_rho, radius = 500.0, 60.0
    print(f"  SYNTHETIC sphere: radius {radius:.0f} m, density contrast "
          f"{delta_rho:.0f} kg/m^3")
    excess_mass = delta_rho * 4.0 / 3.0 * np.pi * radius**3
    print(f"  excess mass = {excess_mass:.4e} kg")
    print("   depth(m)   g_z(mGal)   depth/radius")
    for depth in (100.0, 200.0, 400.0, 800.0):
        gz = sphere_gz(delta_rho, radius, depth) / MGAL
        print(f"  {depth:8.0f}   {gz:9.5f}   {depth/radius:11.2f}")
    print("  A modern relative gravimeter resolves ~0.01 mGal.  The anomaly")
    print("  from this modest body is detectable only to a few hundred metres:")
    print("  gravity's reach is set by the mass, not by sensor cleverness.")

    # ==================================================================
    section("2. Magnetics: magnetisation contrast vs the ambient geometry")
    # SYNTHETIC: a body of volume 1e6 m^3 with magnetisation 5 A/m vertical.
    volume, mag = 1.0e6, 5.0
    moment = mag * volume
    print(f"  SYNTHETIC body: volume {volume:.1e} m^3, magnetisation "
          f"{mag:.1f} A/m vertical -> moment {moment:.3e} A m^2")
    print("   depth(m)   dT@inc=0(nT)  dT@inc=60(nT)  dT@inc=90(nT)")
    for depth in (100.0, 300.0, 900.0):
        vals = [dipole_dT(moment, depth, inc) / NT for inc in (0.0, 60.0, 90.0)]
        print(f"  {depth:8.0f}   {vals[0]:12.4f}   {vals[1]:12.4f}   "
              f"{vals[2]:12.4f}")
    print("  Directly over a vertical dipole under a HORIZONTAL ambient field")
    print("  (inc = 0) the total-field anomaly is exactly zero: dT is a")
    print("  projection, so the same body can be invisible in one geometry")
    print("  and obvious in another.  Never quote 'the magnetic anomaly of a")
    print("  body' without the ambient field direction.")

    # ==================================================================
    section("3. Seismics: impedance contrast -> reflection coefficient")
    # SYNTHETIC layered case: half-space properties, all stated.
    cases = [
        ("case A", 2400.0, 3000.0, 2550.0, 4500.0),
        ("case B", 2100.0, 2500.0, 2400.0, 3000.0),
        ("case C", 2050.0, 1800.0, 2150.0, 2800.0),
    ]
    print("   case    rho1(kg/m^3) v1(m/s)  rho2(kg/m^3) v2(m/s)    R      |R|")
    for name, r1, v1, r2, v2 in cases:
        r = reflection_coefficient(r1, v1, r2, v2)
        print(f"  {name:<8} {r1:10.0f} {v1:7.0f} {r2:11.0f} {v2:8.0f} "
              f"{r:+.4f} {abs(r):.4f}")
    print("  R depends only on the IMPEDANCE ratio rho*v, not on density or")
    print("  velocity separately.  Two rocks with the same impedance are")
    print("  seismically indistinguishable at normal incidence -- the seismic")
    print("  analogue of the gravity non-uniqueness in Module 03.")

    section("4. The unifying statement, quantified")
    print("  Every method answers: 'how large is the contrast, how deep is it,")
    print("  how big is the noise?'  Contrast x geometry / distance^p = signal.")
    print("  Detectability is signal/noise > ~1; the rest is detail.  The")
    print("  exponents p differ (2 for point-mass gravity, 3 for dipole")
    print("  field/1/r^3), which is why gravimeters reach deeper than")
    print("  magnetometers for the same source size.")

    print("\nSUMMARY: a contrast alone is not a signal; a signal alone is not")
    print("an anomaly; an anomaly alone is not a model.")


if __name__ == "__main__":
    main()
