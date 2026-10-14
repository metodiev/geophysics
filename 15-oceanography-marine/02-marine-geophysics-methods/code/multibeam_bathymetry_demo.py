#!/usr/bin/env python3
"""Multibeam bathymetry: swath geometry, beam footprints, the sound-speed error,
attitude errors, sounding density and grid resolution.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python multibeam_bathymetry_demo.py

Everything here is SYNTHETIC.  The sonar parameters, depths and attitudes are
chosen teaching values, printed below; no survey, vessel or chart is reproduced
and no acquisition parameter is quoted from a real system.

Contents
--------
1. Swath geometry: swath width against depth and the outer beam angle.
2. Beam footprint: along-track and across-track, including the 1/cos^2 growth.
3. Sound-speed error: the depth error it produces, and its sign convention.
4. Attitude errors: roll and pitch, converted to depth errors.
5. Sounding density and grid resolution.
6. A depth-error budget, combined in quadrature.
7. Verification: the closed-form footprint against a direct geometric estimate.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC sonar and survey parameters (chosen values) ------------------
C_NOMINAL = 1500.0       # m/s, sound speed the system is assumed to use
BEAM_WIDTH_DEG = 1.0     # deg, across-track beam width
BEAM_SPACING_DEG = 0.3   # deg, angular spacing between beams
HALF_SWATH_DEG = 60.0    # deg, maximum beam angle from vertical
VESSEL_SPEED_KN = 8.0    # knots
PING_RATE_HZ = 10.0      # pings per second
KNOT = 0.514444          # m/s per knot


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def swath_width(z, half_deg):
    """Full swath width in m: 2 z tan(theta_max)."""
    return 2.0 * z * np.tan(np.radians(half_deg))


def footprint_across(z, theta_deg, beam_width_deg):
    """Across-track footprint: slant range times beam width, projected."""
    R = z / np.cos(np.radians(theta_deg))
    return R * np.radians(beam_width_deg) / np.cos(np.radians(theta_deg))


def footprint_across_direct(z, theta_deg, beam_width_deg):
    """Edges-of-beam slant ranges differenced, then projected on the seafloor."""
    t1 = theta_deg - beam_width_deg / 2.0
    t2 = theta_deg + beam_width_deg / 2.0
    g1 = z * np.tan(np.radians(t1))
    g2 = z * np.tan(np.radians(t2))
    return abs(g2 - g1)


def main():
    section("1. Swath geometry")
    print("  Coverage is set by the maximum beam angle: swath width = 2 z tan(theta).")
    print(f"  chosen half-swath angle = {HALF_SWATH_DEG:.0f} deg; "
          f"nominal sound speed = {C_NOMINAL:.0f} m/s")
    print("\n   depth (m)   swath width (m)   width/depth   outer-beam slant range (m)")
    for z in (50.0, 200.0, 1000.0, 2000.0, 4000.0):
        w = swath_width(z, HALF_SWATH_DEG)
        R = z / np.cos(np.radians(HALF_SWATH_DEG))
        print(f"  {z:9.0f}   {w:15.0f}   {w / z:11.3f}   {R:26.0f}")
    print(f"\n  the width/depth ratio is constant at 2 tan({HALF_SWATH_DEG:.0f} deg) = "
          f"{swath_width(1.0, HALF_SWATH_DEG):.4f}.")
    print("  Coverage is therefore a property of the BEAM ANGLE, not of the depth:")
    print("  a deeper survey covers proportionally more seafloor per line, and a")
    print("  constant-beam-spacing system therefore has a resolution that falls")
    print("  linearly with depth.")

    section("2. Beam footprint")
    print("  Across-track footprint = R * dtheta / cos(theta) with R = z/cos(theta),")
    print("  i.e. footprint = z * dtheta / cos^2(theta).  It diverges at high angle.")
    print(f"  beam width = {BEAM_WIDTH_DEG:.2f} deg = "
          f"{np.radians(BEAM_WIDTH_DEG):.6f} rad")
    print("\n   theta (deg)   slant range (m, z=2000)   across-track footprint (m)   "
          "growth factor vs nadir")
    z = 2000.0
    base = footprint_across(z, 0.0, BEAM_WIDTH_DEG)
    for th in (0.0, 15.0, 30.0, 45.0, 55.0, 60.0):
        fp = footprint_across(z, th, BEAM_WIDTH_DEG)
        print(f"  {th:11.1f}   {z / np.cos(np.radians(th)):23.0f}   "
              f"{fp:27.1f}   {fp / base:20.3f}")
    print(f"\n  At {z:.0f} m depth the nadir footprint is {base:.1f} m, but at the")
    print(f"  {HALF_SWATH_DEG:.0f} deg outer beams it is "
          f"{footprint_across(z, HALF_SWATH_DEG, BEAM_WIDTH_DEG):.1f} m -- "
          f"a factor {footprint_across(z, HALF_SWATH_DEG, BEAM_WIDTH_DEG) / base:.1f}.")
    print("  This is the single most important fact about swath sonar: the outer")
    print("  beams resolve a patch of seafloor four times longer than the nadir")
    print("  beams, so a swath's resolution is not one number.")
    f_along = z / np.cos(np.radians(HALF_SWATH_DEG)) * np.radians(BEAM_WIDTH_DEG)
    print(f"\n  Along-track the footprint is R * dtheta = {f_along:.1f} m at the")
    print(f"  outer beam (it does not grow as 1/cos), because the along-track")
    print("  angular width is not projected onto a slope.")

    section("3. Sound-speed error")
    print("  The system converts a measured travel time t to a slant range with an")
    print("  ASSUMED sound speed: R = c t / 2, so dR/R = dc/c exactly.")
    print(f"\n   c error (%)   depth error at 200 m (m)   at 2000 m (m)   at 4000 m (m)")
    for ec in (0.1, 0.5, 1.0, 2.0, 5.0):
        e = ec / 100.0
        print(f"  {ec:12.1f}   {200.0 * e:22.2f}   {2000.0 * e:13.2f}   "
              f"{4000.0 * e:13.2f}")
    print("\n  A 1 per cent sound-speed error is 20 m of depth error at 2 km --")
    print("  larger than most survey accuracy specifications.  This is why")
    print("  sound-speed profiles are measured, not assumed, and why the error is")
    print("  a SCALE error: it moves the whole swath, and it is invisible in the")
    print("  data because a uniformly mis-scaled bathymetry looks perfectly")
    print("  plausible.")
    print("  In shallow water the same percentage error is harmless: 0.5 m at")
    print("  200 m depth.  Sound-speed accuracy matters with depth, not with")
    print("  precision.")

    section("4. Attitude errors")
    print("  Roll mis-points the beams.  At slant range R an attitude error dtheta")
    print("  displaces the sounding across-track by R dtheta; the resulting DEPTH")
    print("  error is that displacement times tan(theta) for a horizontal seafloor,")
    print("  so the leading term at moderate angle is the cross-track displacement")
    print("  R dtheta.  The table below reports R dtheta, which is the quantity that")
    print("  competes with the beam footprint.")
    print("\n   roll error (deg)   R (m, 60 deg, z=2000)   cross-track shift (m)")
    z = 2000.0
    R = z / np.cos(np.radians(HALF_SWATH_DEG))
    for er in (0.02, 0.05, 0.1, 0.5, 1.0):
        print(f"  {er:16.2f}   {R:23.0f}   {R * np.radians(er):19.2f}")
    print(f"\n  A 0.1 deg roll error shifts the outer beam by "
          f"{R * np.radians(0.1):.1f} m, which is comparable to the")
    print("  across-track footprint itself.  Attitude accuracy is therefore not a")
    print("  secondary concern: it competes directly with the resolution.")
    print("  The same arithmetic applies to pitch (along-track) and, more")
    print("  seriously, to heave, which moves the whole swath vertically and is")
    print("  not distinguishable from a real depth change.")

    section("5. Sounding density and grid resolution")
    v = VESSEL_SPEED_KN * KNOT
    along_spacing = v / PING_RATE_HZ
    print(f"  vessel speed = {VESSEL_SPEED_KN:.1f} knots = {v:.3f} m/s; "
          f"ping rate = {PING_RATE_HZ:.0f} Hz")
    print(f"  along-track ping spacing = v / PRF = {along_spacing:.3f} m")
    print(f"  beams per ping = 2*{HALF_SWATH_DEG:.0f}/{BEAM_SPACING_DEG:.1f} = "
          f"{int(2 * HALF_SWATH_DEG / BEAM_SPACING_DEG)}")
    print("\n   depth (m)   swath width (m)   soundings per m^2 at nadir   "
          "recommended cell (m)")
    for z in (100.0, 500.0, 2000.0, 4000.0):
        w = swath_width(z, HALF_SWATH_DEG)
        nbeams = int(2 * HALF_SWATH_DEG / BEAM_SPACING_DEG)
        # sounding density per unit area, using the nadir footprint for the
        # along-track spacing and the beam spacing for the across-track spacing
        across_spacing = z * np.radians(BEAM_SPACING_DEG)
        dens = 1.0 / (along_spacing * across_spacing)
        print(f"  {z:9.0f}   {w:15.0f}   {dens:27.4f}   {across_spacing:23.2f}")
    print("\n  The recommended grid cell is set by the across-track beam spacing at")
    print("  NADIR, not by the outer-beam footprint: gridding to the worst")
    print("  footprint would discard most of the data, and gridding finer than")
    print("  the nadir spacing would interpolate.")
    print("  This choice -- cell size against footprint -- is the resolution")
    print("  decision in a bathymetric product, and different defensible choices")
    print("  give different cell sizes for the same data.")

    section("6. A depth-error budget")
    print("  Terms, each as a fraction of depth (sound speed) or an absolute")
    print("  length (attitude), combined in quadrature.")
    z = 2000.0
    terms = (
        ("sound speed, 0.5 % of depth", 0.005 * z),
        ("time measurement, 0.05 ms of travel time -> 0.04 m", 0.04),
        ("roll, 0.05 deg at 4000 m slant range", R * np.radians(0.05)),
        ("heave residuals, 0.10 m", 0.10),
        ("beam-angle calibration, 0.02 deg", R * np.radians(0.02)),
    )
    tot = 0.0
    print("\n   term                                          contribution (m)")
    for name, val in terms:
        tot += val ** 2
        print(f"  {name:44s} {val:16.3f}")
    tot = np.sqrt(tot)
    print(f"  {'total (quadrature)':44s} {tot:16.3f}")
    print(f"\n  total = {tot:.2f} m at {z:.0f} m depth = "
          f"{100 * tot / z:.3f} per cent of depth.")
    print("  At this depth the DOMINANT term is the acoustic one, because it is a")
    print("  SCALE error proportional to depth (0.5 % of 2000 m = 10 m), while the")
    print("  attitude terms are proportional to the slant range at which the beam")
    print("  soundings occur and only reach 3.5 m at the outer beam.  The two scale")
    print("  differently: shallow surveys are attitude-limited, deep surveys are")
    print("  sound-speed-limited, and a single 'percentage of depth' specification")
    print("  hides both facts.  Note also that the acoustic error moves the whole")
    print("  swath coherently, while attitude errors are largest at the edges -- a")
    print("  distinction that matters when the errors are later inverted for.")

    section("7. Verification")
    print("(a) the closed-form footprint z dtheta/cos^2(theta) against a direct")
    print("    difference of the two beam-edge ground ranges:")
    print("\n   theta (deg)   closed form (m)   direct (m)   difference (m)")
    for th in (0.0, 30.0, 50.0, 60.0):
        cf = footprint_across(z, th, BEAM_WIDTH_DEG)
        dr = footprint_across_direct(z, th, BEAM_WIDTH_DEG)
        print(f"  {th:11.1f}   {cf:15.3f}   {dr:11.3f}   {cf - dr:14.4f}")
    print("    they agree to the first order in dtheta, and the difference grows")
    print("    with the beam angle because the closed form is a small-angle")
    print("    approximation.  For a 1 deg beam the error is small; for a wide")
    print("    outer beam it is not.")
    print("(b) unit check of the sound-speed error: R = c t / 2 has units")
    print("    (m/s)(s) = m; a fractional error in c is a fractional error in R.  ok")
    print("(c) consistency: the outer-beam slant range used in sections 4 and 6 is")
    print(f"    z/cos(60 deg) = {R:.1f} m, which is exactly twice the depth at a")
    print("    60 deg beam angle.  That factor of two is why attitude errors")
    print("    double at the swath edge.")


if __name__ == "__main__":
    main()
