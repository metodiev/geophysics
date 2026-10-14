#!/usr/bin/env python3
"""Moving-platform gravity: the Eotvos correction derived from first principles and
checked against the familiar knots coefficient, the correction for aircraft and ship
speeds including turns, the separation of platform accelerations from gravity using
GNSS, the residual left by filtering, and the cross-over adjustment of a marine
grid.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python airborne_marine_gravity_demo.py

Everything is SYNTHETIC: the platform speeds, headings, GNSS noise, filter cut-offs,
line biases and noise are chosen teaching values.  The only exact constants are the
WGS84 rotation rate omega = 7.292115e-5 rad/s, G = 6.67430e-11 m^3 kg^-1 s^-2 and
the unit relations 1 mGal = 1e-5 m/s^2 and 1 uGal = 1e-8 m/s^2.
No aircraft, ship, survey or published dataset is used or implied.

Contents
--------
1. The Eotvos correction derived, and the knots coefficient checked.
2. Aircraft and ship speeds: the size of the correction and its heading dependence.
3. Turns: the centrifugal term V^2/R, which can dwarf everything else.
4. Separating platform acceleration from gravity with GNSS positions.
5. What filtering leaves behind, measured on a SYNTHETIC acceleration spectrum.
6. Cross-over adjustment of a SYNTHETIC marine grid, before and after.
7. A moving-platform error budget.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

OMEGA = 7.292115e-5              # rad/s, WGS84 defining constant
G = 6.67430e-11
M_PER_KNOT = 0.514444            # m/s per knot
LAT_TEST = 45.0                  # deg
DEFAULT_VERTICAL_NOISE = 0.05    # m, GNSS vertical position noise
DRAPER_FREQ = 0.005              # Hz, cut-off for the platform-acceleration band


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def eotvos_mgal(speed_m_s, lat_deg, heading_deg, turn_radius_m=None):
    """Eotvos correction in mGal: Coriolis plus centrifugal terms.

    a_E = 2 Omega V cos(phi) sin(alpha) + V^2 / R, with alpha measured from north.
    The centrifugal term is zero on a straight course.
    """
    ph = np.radians(lat_deg)
    a = 2.0 * OMEGA * speed_m_s * np.cos(ph) * np.sin(np.radians(heading_deg))
    if turn_radius_m is not None:
        a = a + speed_m_s ** 2 / turn_radius_m
    return a * 1e5


def main():
    print("SYNTHETIC moving-platform study")
    print(f"  rotation rate omega = {OMEGA:.7e} rad/s (WGS84 defining constant)")
    print(f"  test latitude       = {LAT_TEST:.1f} deg")
    print(f"  1 knot              = {M_PER_KNOT:.6f} m/s")

    section("1. The Eotvos correction, derived and checked")
    print("  On a rotating Earth a moving observer experiences an additional vertical")
    print("  acceleration: the Coriolis term 2 Omega V cos(phi) sin(alpha) and, on a")
    print("  curved or turning path, the centrifugal term V^2/R.")
    print(f"  2 Omega = {2 * OMEGA:.7e} s^-1, so in mGal the east-component is")
    coeff_si = 2.0 * OMEGA * 1e5
    coeff_knot = 2.0 * OMEGA * M_PER_KNOT * 1e5
    print(f"   a_E = {coeff_si:.4f} V(m/s) cos(phi) sin(alpha) mGal")
    print(f"       = {coeff_knot:.4f} V(knots) cos(phi) sin(alpha) mGal")
    print(f"  The familiar coefficient for speeds in knots is {coeff_knot:.3f}: it is")
    print("  DERIVED here from omega and the definition of the knot, not quoted.")
    print("  At the equator on a due-east heading the whole correction is")
    print(f"   {coeff_knot:.3f} mGal per knot; at 45 deg it is "
          f"{coeff_knot * np.cos(np.radians(45.0)):.3f} mGal per knot.")

    section("2. Aircraft and ship speeds")
    print("   platform   speed              heading   Eotvos (mGal)")
    for label, v_ms in (("aircraft", 70.0), ("aircraft", 90.0), ("ship", 5.0),
                        ("ship", 10.0)):
        kn = v_ms / M_PER_KNOT
        for heading in (0.0, 45.0, 90.0, 180.0, 270.0):
            e = eotvos_mgal(v_ms, LAT_TEST, heading)
            print(f"   {label:9s}  {v_ms:5.1f} m/s ({kn:6.1f} kn)  {heading:7.1f}   "
                  f"{e:+12.2f}")
    print("  At 70 m/s a due-east heading and a due-west heading differ by")
    d = eotvos_mgal(70.0, LAT_TEST, 90.0) - eotvos_mgal(70.0, LAT_TEST, 270.0)
    print(f"  {d:.2f} mGal - three orders of magnitude larger than the anomalies an")
    print("  airborne survey targets.  The sensitivity to heading is itself")
    print("  heading-dependent: E = 721.88 sin(alpha) mGal at this speed and")
    print("  latitude, so dE/d(alpha) = 721.88 cos(alpha) mGal per radian, i.e.")
    for heading in (0.0, 45.0, 90.0):
        sens = 721.8765 * np.cos(np.radians(heading)) * np.pi / 180.0
        print(f"   at heading {heading:5.1f} deg: {sens:+7.3f} mGal per degree of "
              f"heading error")
    print("  MEASURED COUNTER-INTUITION: the correction is LARGEST on the east-west")
    print("  lines (721.88 mGal at 90 deg) but its DERIVATIVE with respect to heading")
    print("  vanishes there.  The largest heading sensitivity is on the north-south")
    print("  lines (12.599 mGal per degree at 0 deg), where the correction itself is")
    print("  zero.  A 0.1 deg heading error costs 1.26 mGal on a north-south line and")
    print("  only 0.89 mGal at 45 deg.  The heading must therefore be known best")
    print("  where the correction is smallest, which is the opposite of what the")
    print("  size of the correction suggests.")

    section("3. Turns: the centrifugal term")
    print("  During a turn the platform also feels V^2/R toward the turn centre, whose")
    print("  vertical component must be modelled or the line abandoned.")
    print("   speed (m/s)   turn radius (m)   V^2/R (m/s^2)   V^2/R (mGal)")
    for v in (5.0, 70.0):
        for radius in (2000.0, 5000.0, 20000.0):
            a = v ** 2 / radius
            print(f"   {v:11.1f}   {radius:15.0f}   {a:14.6f}   {a * 1e5:14.1f}")
    print("  An aircraft turn of 70 m/s at a 5 km radius produces")
    print(f"  {70.0 ** 2 / 5000.0 * 1e5:.0f} mGal of vertical acceleration; no gravity")
    print("  signal of interest is five orders of magnitude below that.  The")
    print("  standard practices follow: fly straight and level while measuring, model")
    print("  the turn, or discard the turn lines and use the cross-overs instead.")

    section("4. Separating platform acceleration from gravity with GNSS")
    print("  The measured vertical acceleration is g + a_platform.  GNSS positions give")
    print("  a second differentiation, whose noise is amplified by (2 pi f)^2:")
    print("        sigma_a ~ sigma_z (2 pi f)^2")
    print(f"  SYNTHETIC draper cut-off f = {DRAPER_FREQ:.3f} Hz "
          f"(period {1.0 / DRAPER_FREQ:.0f} s)")
    print("   sigma_z (m)   sigma_a (m/s^2)   sigma_a (mGal)")
    for sz in (0.01, 0.05, 0.10, 0.50):
        sa = sz * (2.0 * np.pi * DRAPER_FREQ) ** 2
        print(f"   {sz:11.2f}   {sa:15.3e}   {sa * 1e5:14.3f}")
    print("  A 5 cm vertical position accuracy gives")
    print(f"  {DEFAULT_VERTICAL_NOISE * (2.0 * np.pi * DRAPER_FREQ) ** 2 * 1e5:.2f} mGal "
          f"of noise in the band that matters, and a 50 cm one gives")
    print(f"  {0.50 * (2.0 * np.pi * DRAPER_FREQ) ** 2 * 1e5:.1f} mGal: the survey's")
    print("  accuracy is set by the position accuracy, not by the gravimeter.")
    print("  The strong dependence on f is the reason the correction is split: a")
    print("  long-wavelength part from GNSS and a short-wavelength part from a")
    print("  vertical accelerometer (or a stabilised platform).")

    section("5. What filtering leaves behind")
    print("  SYNTHETIC vertical acceleration spectrum: white acceleration of")
    print("  amplitude 0.5 m/s^2 (aircraft turbulence) at frequencies below 0.05 Hz,")
    print("  plus the gravity signal band at frequencies above 0.0005 Hz.")
    n_freq = 4000
    freqs = np.logspace(-5.0, -0.5, n_freq)
    turbulence = 0.5 * np.ones_like(freqs)          # m/s^2, white in frequency
    gravity_band = 1.0e-4 * np.ones_like(freqs)     # m/s^2, the target band
    separator = 1.0 / (1.0 + (freqs / DRAPER_FREQ) ** 4)
    leakage = turbulence * 0.5 * (1.0 - separator) / (
        1.0 + (freqs / (0.5 * DRAPER_FREQ)) ** 4)
    total_leak = np.sqrt(np.trapezoid(leakage ** 2, freqs))
    print(f"  turbulence amplitude: {0.5:.3f} m/s^2 = {0.5 * 1e5:.0f} mGal")
    print(f"  gravity band amplitude: {1.0e-4:.1e} m/s^2 = {1.0e-4 * 1e5:.1f} mGal")
    print(f"  after a 4-pole filter at {DRAPER_FREQ:.3f} Hz the residual turbulence")
    print(f"  leaks into the gravity band at {total_leak:.3e} m/s^2 = "
          f"{total_leak * 1e5:.3f} mGal")
    print("  The ratio of the two amplitudes is 5000:1, and no filter removes a")
    print("  component that overlaps the signal band.  The practical consequence is")
    print("  that the platform acceleration must be MEASURED (accelerometer, GNSS,")
    print("  or a gyro-stabilised platform) rather than filtered out, and that the")
    print("  filter's job is only to define which measurement is used where.")

    section("6. Cross-over adjustment of a SYNTHETIC marine grid")
    n_line = 6
    lines = [f"E{i + 1}" for i in range(n_line)] + [f"N{i + 1}" for i in range(n_line)]
    true_bias = 3.0 * RNG.standard_normal(len(lines))       # mGal, per line
    noise = 0.3                                             # mGal per cross-over
    cross = []
    for i, e_line in enumerate(lines[:n_line]):
        for j, n_line_local in enumerate(lines[n_line:]):
            cross.append((e_line, n_line_local,
                          true_bias[i] - true_bias[n_line + j]
                          + noise * RNG.standard_normal()))
    print(f"  {n_line} east-west lines and {n_line} north-south lines give "
          f"{len(cross)} cross-overs")
    print(f"  SYNTHETIC per-line bias scatter {true_bias.std():.2f} mGal, cross-over")
    print(f"  noise {noise:.1f} mGal")
    d_raw = np.array([c[2] for c in cross])
    print(f"  before adjustment: cross-over difference rms = "
          f"{np.sqrt(np.mean(d_raw ** 2)):.3f} mGal")
    # weighted least squares for the line biases, with a gauge fixing one line at 0
    A = np.zeros((len(cross), len(lines)))
    for k, (a, b, _) in enumerate(cross):
        A[k, lines.index(a)] = 1.0
        A[k, lines.index(b)] = -1.0
    A[:, 0] = 0.0        # gauge: the first line's bias is the reference (set to 0)
    W = np.eye(len(cross)) / noise ** 2
    est = np.linalg.lstsq(A, d_raw, rcond=None)[0]
    resid = d_raw - A @ est
    print(f"  after adjustment: cross-over residual rms = "
          f"{np.sqrt(np.mean(resid ** 2)):.3f} mGal "
          f"(predicted by the noise level: {noise:.2f})")
    recovered = est[1:] - est[1:].mean()
    truth_rel = true_bias[1:] - true_bias[1:].mean()
    print(f"  the adjustment determines only RELATIVE line biases: the gauge fixes one")
    print(f"  line to zero, so a common offset of all lines is unobservable from")
    print(f"  cross-overs alone.  Difference between recovered and true relative")
    print(f"  biases: rms {np.sqrt(np.mean((recovered - truth_rel) ** 2)):.3f} mGal.")

    section("7. A moving-platform error budget")
    terms = {
        "gravimeter noise (1 mGal resolution, 0.1 mGal after averaging)": 0.10,
        "Eotvos correction, heading error 0.1 deg at 70 m/s, 45 deg heading": float(
            abs(eotvos_mgal(70.0, LAT_TEST, 45.1) - eotvos_mgal(70.0, LAT_TEST, 45.0))),
        "Eotvos correction, speed error 0.5 m/s at 70 m/s": float(
            abs(eotvos_mgal(70.5, LAT_TEST, 90.0) - eotvos_mgal(70.0, LAT_TEST, 90.0))),
        "platform acceleration leaking through the filter (Section 5)": float(
            total_leak * 1e5),
        "GNSS-derived vertical acceleration at 5 cm, 5 mHz": float(
            DEFAULT_VERTICAL_NOISE * (2.0 * np.pi * DRAPER_FREQ) ** 2 * 1e5),
        "position/latitude error (0.0001 deg)": 0.045,
        "reduction density error (100 kg/m^3 at 500 m of terrain)": 0.5,
    }
    print("   term                                                        mGal")
    for k, v in terms.items():
        print(f"   {k:58s} {v:6.3f}")
    total = float(np.sqrt(sum(v ** 2 for v in terms.values())))
    print(f"   {'total in quadrature':58s} {total:6.3f}")
    print("  The 'platform acceleration leaking through the filter' row is the cost of")
    print("  trying to FILTER the platform motion out.  Measuring it instead (an")
    print("  accelerometer plus GNSS) replaces that row with the GNSS term above it,")
    print(f"  i.e. {DEFAULT_VERTICAL_NOISE * (2.0 * np.pi * DRAPER_FREQ) ** 2 * 1e5:.2f} "
          f"mGal, and the budget falls by an order of magnitude: this single")
    print("  comparison is the design argument for modern airborne gravity.")
    print("  The Eotvos correction's sensitivity to heading and speed, and the")
    print("  platform-acceleration term, dominate every instrumental term: on a")
    print("  moving platform the navigation IS the gravimeter, and the survey's")
    print("  accuracy is a statement about the navigation as much as about the sensor.")


if __name__ == "__main__":
    main()
