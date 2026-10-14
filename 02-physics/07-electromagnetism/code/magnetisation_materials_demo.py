"""Magnetisation, susceptibility and magnetic materials: the physical origin of
rock magnetism, induced versus remanent magnetisation, and the numbers that make
magnetic surveys work.

Run:  python3 magnetisation_materials_demo.py
Requires: Python standard library only.

Companion to lesson 02-07-07. The script:

1. Verifies B = mu0 (H + M) = mu0 (1 + chi) H and tabulates the induced
   magnetisation and anomaly for a range of susceptibilities in a 50 uT field.
   B is in tesla, H is in amperes per metre: they have different dimensions.
2. Computes the Curie depth for stated geothermal gradients, with the Curie
   temperature of magnetite treated as a measured mineral-physical value.
3. Computes Koenigsberger ratios Q = M_r/(chi H) for representative rock types,
   showing which are induced-dominated and which are remanence-dominated.
4. Computes the surface magnetic anomaly of buried dipoles of given moment, and
   shows what moment is needed for a nanotesla-scale anomaly.
5. Computes the mean magnetisation of the core implied by the geomagnetic dipole
   moment, and compares it with the surface field.
6. Applies the demagnetising factor of a sphere and the resulting effective
   susceptibility chi/(1 + N chi).

Every number printed below was produced by this script.
"""

import math

MU0 = 1.25663706212e-6
R_EARTH = 6371000.0


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def part1_basic_relations():
    section("1. B, H and M: the basic relations and their dimensions")
    b_ambient = 50.0e-6                     # 50 uT, the geomagnetic field
    h = b_ambient / MU0
    print(f"  ambient B = {b_ambient * 1e6:.0f} uT = {b_ambient * 1e9:.0f} nT")
    print(f"  ambient H = B/mu0 = {h:.4f} A/m")
    print("  Units are different and must not be conflated:")
    print("    [H] = A/m,   [M] = A/m,   [B] = T = kg s^-2 A^-1")
    print("    B = mu0 (H + M),  so  B = mu0 (1 + chi) H  and  mu_r = 1 + chi.")
    print(f"{'chi':>10}{'M (A/m)':>14}{'B = mu0(1+chi)H (T)':>22}"
          f"{'B/B0':>10}{'B - B0 (nT)':>14}")
    for chi in (-1.0e-5, 1.0e-4, 1.0e-3, 0.01, 0.1, 1.0):
        m = chi * h
        b = MU0 * (1.0 + chi) * h
        print(f"{chi:10.5f}{m:14.6f}{b:22.9e}{b / b_ambient:10.5f}"
              f"{(b - b_ambient) * 1e9:14.4f}")
    print("  Negative chi is diamagnetism (a small decrease); geologically relevant")
    print("  susceptibilities run from ~-1e-5 (pure quartz) to ~1 (magnetite-rich")
    print("  rock). Even chi = 1 changes the field by only a factor 2 - the reason")
    print("  magnetic anomalies are a *small perturbation* on the ambient field.")


def part2_curie_depth():
    section("2. Curie depth: where rock magnetism stops")
    print("  Magnetite becomes paramagnetic above its Curie temperature, widely")
    print("  quoted as about 580 C (853 K). That value is a MEASURED mineral-physical")
    print("  property: check it against a mineral-physics or rock-magnetism")
    print("  reference before using it quantitatively, since the exact figure")
    print("  depends on composition and pressure.")
    t_curie, t_surface = 580.0, 10.0
    print(f"{'geothermal gradient (C/km)':>28}{'Curie depth (km)':>20}")
    for gradient in (10.0, 15.0, 20.0, 25.0, 30.0, 40.0):
        depth = (t_curie - t_surface) / gradient
        print(f"{gradient:28.0f}{depth:20.2f}")
    print("  The gradient is a NOMINAL choice here; real gradients depend on heat")
    print("  flow, crustal radiogenic heating and thermal conductivity, and should be")
    print("  measured locally (see 05-09 geothermal and 08-07 rock magnetism).")
    print("  Below the Curie depth the crust carries no remanent magnetisation, so")
    print("  long-wavelength magnetic anomalies must come from the magnetic crust")
    print("  above it.")


def part3_koenigsberger():
    section("3. Induced versus remanent: the Koenigsberger ratio")
    b_ambient = 50.0e-6
    h = b_ambient / MU0
    print(f"  H = {h:.3f} A/m (from a 50 uT ambient field)")
    print("  Q = M_r / (chi H). All values below are NOMINAL ranges for the rock")
    print("  class, not measurements of a particular sample.")
    rows = [("sedimentary (weakly magnetic)", 1.0e-4, 0.001),
            ("granite (typical)", 1.0e-3, 0.05),
            ("basalt (typical)", 5.0e-2, 5.0),
            ("metamorphic (magnetite-bearing)", 1.0e-2, 1.0)]
    print(f"{'rock class':>34}{'chi':>10}{'M_r (A/m)':>12}{'M_i (A/m)':>12}"
          f"{'Q':>10}")
    for name, chi, mr in rows:
        mi = chi * h
        print(f"{name:>34}{chi:10.5f}{mr:12.4f}{mi:12.6f}{mr / mi:10.2f}")
    print("  Q < 1 means induced magnetisation dominates (sediments: the anomaly maps")
    print("  the present field); Q > 1 means remanence dominates (basalt: the anomaly")
    print("  records the field direction at the time of cooling). This single ratio")
    print("  decides whether a magnetic survey maps structure or geological history.")


def part4_dipole_anomaly():
    section("4. The surface anomaly of a buried dipole")
    print("  Vertical dipole of moment m = M V at depth d in a non-magnetic half-space.")
    print("  For a vertically polarised body the anomaly directly above it is")
    print("  B_z = mu0 2 m/(4 pi d^3) (the axial dipole term).")
    print(f"{'volume (km^3)':>16}{'M (A/m)':>10}{'m (A m^2)':>14}{'depth (km)':>12}"
          f"{'B_z (nT)':>12}")
    for volume_km3, mag, depth_km in ((1.0, 1.0, 2.0), (10.0, 1.0, 2.0),
                                      (100.0, 1.0, 5.0), (1.0, 5.0, 1.0),
                                      (1000.0, 0.1, 10.0)):
        m = mag * volume_km3 * 1.0e9
        d = depth_km * 1000.0
        b = MU0 * 2.0 * m / (4.0 * math.pi * d ** 3)
        print(f"{volume_km3:16.0f}{mag:10.2f}{m:14.3e}{depth_km:12.1f}"
              f"{b * 1e9:12.4f}")
    print("  Nanotesla-scale anomalies need moments of order 1e8-1e10 A m^2, i.e.")
    print("  bodies of order a cubic kilometre with magnetisation of order 1 A/m, or")
    print("  larger bodies deeper down. That is why aeromagnetic surveys detect")
    print("  magnetite-rich plutons and ore bodies but not individual magnetic")
    print("  minerals.")


def part5_core_magnetisation():
    section("5. How magnetised is the core?")
    b_eq = 30.0e-6                          # NOMINAL equatorial surface field
    m_earth = 4.0 * math.pi * R_EARTH ** 3 * b_eq / MU0
    v_core = 4.0 / 3.0 * math.pi * (3.48e6) ** 3
    m_mean = m_earth / v_core
    b_core = MU0 * m_mean
    print(f"  m_earth from B_equator = {b_eq * 1e9:.0f} nT (NOMINAL) and"
          f" R = {R_EARTH:.0f} m: {m_earth:.3e} A m^2")
    print(f"  outer-core volume = {v_core:.3e} m^3")
    print(f"  mean magnetisation M = m/V = {m_mean:.1f} A/m")
    print(f"  implied mean field inside the core B = mu0 M = {b_core * 1e3:.3f} mT"
          f" = {b_core * 1e6:.1f} uT")
    print(f"  surface equatorial field = {b_eq * 1e6:.1f} uT, i.e."
          f" {b_core / b_eq:.0f} times smaller")
    print("  Both numbers are NOMINAL: the dipole moment is time-varying and the")
    print("  field inside the core is not uniform. Dynamo models with core fields of")
    print("  order 1 mT are consistent with this estimate, but the estimate is not a")
    print("  measurement of the core field.")


def part6_demagnetising():
    section("6. Demagnetising factors: why shape matters")
    print("  For an ellipsoid, H_inside = H_0 - N M, so the effective susceptibility")
    print("  measured on the outside is chi_eff = chi/(1 + N chi).")
    print(f"{'chi':>8}{'N = 0 (needle)':>18}{'N = 1/3 (sphere)':>20}"
          f"{'N = 1 (thin sheet)':>22}")
    for chi in (0.001, 0.01, 0.1, 1.0, 10.0):
        vals = [chi / (1.0 + n * chi) for n in (0.0, 1.0 / 3.0, 1.0)]
        print(f"{chi:8.3f}{vals[0]:18.5f}{vals[1]:20.5f}{vals[2]:22.5f}")
    print("  Strongly magnetic material cannot exceed chi_eff = 1/N: the induced")
    print("  field opposes the applied one. This is why magnetite-rich bodies look")
    print("  far less magnetic than their mineral content suggests, and why the")
    print("  demagnetising factor must be specified in any inversion for")
    print("  susceptibility.")


def main():
    part1_basic_relations()
    part2_curie_depth()
    part3_koenigsberger()
    part4_dipole_anomaly()
    part5_core_magnetisation()
    part6_demagnetising()


if __name__ == "__main__":
    main()
