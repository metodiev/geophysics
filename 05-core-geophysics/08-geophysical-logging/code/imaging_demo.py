"""Borehole imaging and dipmeter: dip from a sinusoid, and its failure modes.

Four results:

  1. DIP FROM A SINUSOID.  A planar bed boundary crossing a cylindrical borehole
     appears on an unwrapped image as a sinusoid whose amplitude gives the dip and
     whose phase gives the azimuth.  A synthetic image is built, the sinusoid is
     fitted, and the recovered dip and azimuth are compared with the truth.
  2. SAMPLING LIMIT.  The fit is repeated with azimuthal sampling coarser than the
     feature's wavelength, and the recovered dip error is reported.
  3. BOREHOLE DEVIATION.  The apparent dip of a bed in a deviated hole is
     computed, and the error incurred by ignoring the deviation is reported.
  4. FRACTURE APERTURE.  A synthetic conductive fracture trace is inverted with a
     stated empirical aperture relation, and the spread of the estimate over three
     assumed cementation exponents is reported -- a demonstration of how much of
     an aperture estimate is the calibration rather than the measurement.

All bed dips, hole deviations, fracture apertures and calibration constants are
STATED SYNTHETIC INPUTS.

Run:  python3 imaging_demo.py
"""

from __future__ import annotations

import numpy as np

DIAMETER = 0.20      # SYNTHETIC borehole diameter, m


def section(title: str) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def sinusoid(azimuth_deg, amp, phase_deg, offset):
    return offset + amp * np.cos(np.radians(azimuth_deg - phase_deg))


def main() -> None:
    section("1. Dip and azimuth from the sinusoid of a planar boundary")
    true_dip, true_azimuth, azimuth = 22.0, 135.0, 40.0    # SYNTHETIC, degrees
    amp = 0.5 * DIAMETER * np.tan(np.radians(true_dip))
    az = np.linspace(0.0, 360.0, 361, endpoint=False)
    z = sinusoid(az, amp, true_azimuth, 0.0)
    # Least-squares fit of A cos(theta) + B sin(theta) + C
    design = np.column_stack([np.cos(np.radians(az)), np.sin(np.radians(az)),
                              np.ones_like(az)])
    coef, *_ = np.linalg.lstsq(design, z, rcond=None)
    a_fit, b_fit = coef[0], coef[1]
    amp_fit = float(np.hypot(a_fit, b_fit))
    phase_fit = float(np.degrees(np.arctan2(b_fit, a_fit)) % 360.0)
    dip_fit = float(np.degrees(np.arctan(2.0 * amp_fit / DIAMETER)))
    print(f"true dip {true_dip:.2f} deg, azimuth {true_azimuth:.1f} deg")
    print(f"fitted amplitude {amp_fit:.4f} m -> dip {dip_fit:.2f} deg "
          f"({100 * (dip_fit - true_dip) / true_dip:+.3f} per cent)")
    print(f"fitted phase {phase_fit:.1f} deg "
          f"(error {phase_fit - true_azimuth:+.2f} deg)")
    print(f"true amplitude {amp:.4f} m")

    section("2. What azimuthal sampling costs")
    print("A perfectly planar bed is one sinusoid, which ANY three or more azimuths")
    print("represent exactly.  A fold adds a harmonic of order m (m cycles per")
    print("revolution).  Sampling at P evenly spaced azimuths folds that harmonic to")
    print("order |m - P*round(m/P)|: if the folded order is 1 it lands on the")
    print("fundamental and biases the dip; if it is 0 or >=2 it does not.\n")
    print("m   P    folded order   dip error (deg)   azimuth error (deg)")
    for m in (2, 3, 4):
        for p in (3, 4, 5, 6, 8, 12, 360):
            az_s = np.linspace(0.0, 360.0, p, endpoint=False)
            z_s = (sinusoid(az_s, amp, true_azimuth, 0.0)
                   + 0.25 * amp * np.cos(m * np.radians(az_s - true_azimuth)))
            d_s = np.column_stack([np.cos(np.radians(az_s)),
                                   np.sin(np.radians(az_s)), np.ones_like(az_s)])
            c_s, *_ = np.linalg.lstsq(d_s, z_s, rcond=None)
            amp_s = float(np.hypot(c_s[0], c_s[1]))
            ph_s = float(np.degrees(np.arctan2(c_s[1], c_s[0])) % 360.0)
            dip_s = float(np.degrees(np.arctan(2.0 * amp_s / DIAMETER)))
            az_err = (ph_s - true_azimuth + 180.0) % 360.0 - 180.0
            folded = abs(m - p * round(m / p))
            print(f"{m:2d} {p:4d}   {folded:12d}   {dip_s - true_dip:+15.3f}   "
                  f"{az_err:+18.3f}")
    print("The folded-order formula predicts exactly which rows are wrong and which")
    print("are not.  A rotating tool with hundreds of azimuths is immune; a 4-pad")
    print("tool aliases any fold whose order is within one of 4, and the output shows")
    print("no warning -- it reports a dip, confidently, of the wrong bed.")

    section("3. Borehole deviation, and what ignoring it costs")
    hole_dev = 30.0        # SYNTHETIC hole inclination from vertical, degrees
    print(f"true bed dip from horizontal = {true_dip:.1f} deg, hole inclination = "
          f"{hole_dev:.1f} deg from vertical")
    print("The angle an image log actually measures is the angle BETWEEN the bed\n"
          "and the hole axis.  For a hole inclined theta from vertical and a bed\n"
          "dipping delta, with Delta the azimuth difference between hole direction\n"
          "and bed dip direction:")
    print("  cos(relative dip) = cos(theta) cos(delta) + sin(theta) sin(delta) "
          "cos(Delta)\n")
    print("azimuth difference   relative dip (deg)   error if called true dip (deg)")
    for delta_az in (0.0, 30.0, 60.0, 90.0, 150.0, 180.0):
        ct = (np.cos(np.radians(hole_dev)) * np.cos(np.radians(true_dip))
              + np.sin(np.radians(hole_dev)) * np.sin(np.radians(true_dip))
              * np.cos(np.radians(delta_az)))
        rel = float(np.degrees(np.arccos(np.clip(ct, -1.0, 1.0))))
        print(f"{delta_az:16.0f}   {rel:18.2f}   {rel - true_dip:+26.2f}")
    print("\nThe relative dip ranges from 8.0 to 52.0 degrees for a single true dip of\n"
          "22 degrees: the hole orientation, not the geology, moves the number by a\n"
          "factor of six.  Deviation must come from the same run as the image, and\n"
          "the correction must be applied before any structural map is drawn.")

    section("4. Fracture aperture: the answer is the calibration")
    # Synthetic conductive trace: aperture enters a stated empirical relation
    # (aperture ~ anomaly^exponent).  The exponent is NOT a measured constant here.
    anomaly = 0.35          # SYNTHETIC conductivity anomaly of the trace
    print(f"SYNTHETIC fracture conductivity anomaly = {anomaly:.2f}")
    for exponent, label in ((0.5, "square-root"), (0.725, "commonly used exponent"),
                            (1.0, "linear")):
        aperture_mm = 10.0 * anomaly ** exponent * 0.05
        print(f"  exponent {exponent:.3f} ({label:22s}): "
              f"aperture = {aperture_mm:.4f} mm")
    print("The three exponents differ by a factor of about 1.5 in the recovered\n"
          "aperture for the same trace.  An aperture from an image log is therefore\n"
          "a CALIBRATION-DEPENDENT estimate, and it must be reported with the\n"
          "relation used and its provenance; quoting a number to two decimals\n"
          "without the relation overstates the measurement.")


if __name__ == "__main__":
    main()
