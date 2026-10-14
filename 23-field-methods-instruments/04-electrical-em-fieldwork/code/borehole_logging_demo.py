#!/usr/bin/env python3
"""Borehole logging operations arithmetic: cable stretch, tool resolution, depth
sampling, two-point calibration and run-to-run depth matching, on SYNTHETIC values.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python borehole_logging_demo.py

Everything here is SYNTHETIC.  The tool weights, cable properties, logging speeds,
detector lengths and calibration readings are chosen teaching values, and the
relations printed are the standard ones quoted in the text.  No field log,
tool specification or manufacturer figure is reproduced.

Sections
--------
1. Cable stretch: the depth error a hanging tool produces.
2. Tool response: what a detector of finite length does to a thin bed.
3. Depth sampling and logging speed.
4. Two-point calibration of a log against known values.
5. Depth matching between two runs of the same hole.
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def stretch(weight_n, length_m, area_m2, modulus_pa):
    """Elastic elongation of a cable supporting a weight at its end, m."""
    return weight_n * length_m / (area_m2 * modulus_pa)


def boxcar_response(bed_m, detector_m):
    """Peak response of a boxcar detector of length L to a bed of thickness b."""
    if bed_m >= detector_m:
        return 1.0
    return bed_m / detector_m


def main():
    section("1. Cable stretch and depth error")
    area = 1.0e-5          # m^2, 10 mm^2 effective section (chosen)
    modulus = 1.1e11       # Pa, steel-like elastic modulus (chosen)
    print("  elastic stretch of a hanging cable: dl = W L / (A E)")
    print(f"  cable section {area * 1e6:.0f} mm^2, modulus {modulus:.2e} Pa")
    print(f"  {'tool weight (N)':>16s} {'depth (m)':>10s} {'stretch (m)':>12s}"
          f" {'as sampling intervals':>23s}")
    for weight in (250.0, 500.0, 1000.0, 2000.0):
        for depth in (1000.0, 2000.0):
            s = stretch(weight, depth, area, modulus)
            print(f"  {weight:16.0f} {depth:10.0f} {s:12.4f} "
                  f"{s / 0.05:23.1f}")
    print("  (the last column counts 0.05 m depth-sampling intervals)")
    print("  -> a 500 N tool on 2000 m of this cable stretches it by 0.9 m: the")
    print("     depth scale must be corrected for it, and the correction changes")
    print("     when the tool changes.  The cable's own weight adds to W.")

    section("2. Tool response to a thin bed")
    detector = 0.5
    print(f"  detector length {detector:.2f} m; a bed thinner than the detector")
    print(f"  gives a peak response of bed/detector")
    print(f"  {'bed (m)':>9s} {'peak response':>14s} {'apparent thickness (m)':>23s}")
    for bed in (0.05, 0.10, 0.20, 0.35, 0.50, 1.00):
        response = boxcar_response(bed, detector)
        print(f"  {bed:9.2f} {response:14.3f} {detector:23.2f}")
    print("  -> below the detector length every thin bed is reported as"
          " the same")
    print("     apparent thickness with a reduced amplitude: thickness is lost,")
    print("     not merely blurred, and no deconvolution invents it back with")
    print("     certainty.")

    section("3. Depth sampling and logging speed")
    sample_rate = 20.0     # samples per second (chosen)
    print(f"  logging tool samples at {sample_rate:.0f} samples/s")
    print(f"  {'sampling (m)':>13s} {'speed (m/s)':>12s} {'speed (m/h)':>12s}"
          f" {'time for 2000 m (min)':>23s}")
    for interval in (0.02, 0.05, 0.10, 0.20):
        speed = interval * sample_rate
        print(f"  {interval:13.2f} {speed:12.3f} {speed * 3600.0:12.0f} "
              f"{2000.0 / speed / 60.0:23.1f}")
    print("  -> the sampling interval is speed/sample rate: slowing down buys")
    print("     resolution in depth but costs rig time, and the tool's own")
    print("     resolution may make the finer sampling pointless.")

    section("4. Two-point calibration")
    raw1, value1 = 1200.0, 10.0
    raw2, value2 = 8200.0, 90.0
    gain = (value2 - value1) / (raw2 - raw1)
    offset = value1 - gain * raw1
    print(f"  two readings with values: raw {raw1:.0f} -> {value1:.1f}, "
          f"raw {raw2:.0f} -> {value2:.1f}")
    print(f"  gain = {gain:.6f} value units per count")
    print(f"  offset = {offset:.4f} value units")
    print(f"  check: raw {raw1:.0f} -> {gain * raw1 + offset:.4f}, "
          f"raw {raw2:.0f} -> {gain * raw2 + offset:.4f}")
    print(f"  a {value2 - value1:.1f}-unit span across {raw2 - raw1:.0f} counts")
    print(f"  means one count is {gain:.6f} value units; the calibration is only")
    print(f"  as good as the two reference values, so their uncertainty sets the")
    print(f"  scale uncertainty directly.")

    section("5. Depth matching between runs")
    n_marker = 20
    true_shift = 0.60
    read_sd = 0.08
    shifts = true_shift + read_sd * RNG.standard_normal(n_marker)
    fitted = shifts.mean()
    residual = shifts - fitted
    print(f"  {n_marker} markers picked independently on two runs of the same hole")
    print(f"  SYNTHETIC true shift {true_shift:.2f} m, picking scatter "
          f"{read_sd:.2f} m")
    print(f"  measured mean shift = {fitted:.4f} m")
    print(f"  residual scatter about the mean = {residual.std(ddof=1):.4f} m")
    print(f"  standard error of the fitted shift = "
          f"{residual.std(ddof=1) / np.sqrt(n_marker):.4f} m")
    print(f"  markers with |shift - mean| > 0.20 m = "
          f"{int((np.abs(residual) > 0.20).sum())} of {n_marker}")
    print("  -> report the fitted shift AND the residual scatter: a shift is")
    print("     correctable, a scatter is not, and a large residual means the")
    print("     marker identification, not the depth, is the problem.")

    print("\nSYNTHETIC: every number above comes from chosen parameters in this")
    print("file, combined with the standard relations quoted in the text.")


if __name__ == "__main__":
    main()
