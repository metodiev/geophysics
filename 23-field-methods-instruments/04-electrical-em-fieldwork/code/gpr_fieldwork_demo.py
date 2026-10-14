#!/usr/bin/env python3
"""GPR fieldwork arithmetic: velocity, wavelength, resolution, hyperbola velocity
analysis, trace spacing, attenuation budget, grid size and calibration, on
SYNTHETIC values.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gpr_fieldwork_demo.py

Everything here is SYNTHETIC.  The permittivities, antenna frequencies, attenuation
rates, grid geometry and measured times are chosen teaching values, and the
relations printed are the standard ones quoted in the text.  No field dataset,
antenna specification or commercial system is reproduced.

Sections
--------
1. Velocity, wavelength and vertical resolution against permittivity and frequency.
2. Velocity from a diffraction hyperbola, and the depth it implies.
3. Trace spacing required for migration.
4. Attenuation budget and the maximum depth for a stated dynamic range.
5. Grid size, data volume and acquisition time.
6. Calibration against a known target, and the depth error of a wrong permittivity.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

C_M_PER_NS = 0.299792458      # speed of light in vacuum, m/ns


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def velocity(eps_r):
    """Propagation velocity in a low-loss dielectric, m/ns."""
    return C_M_PER_NS / np.sqrt(eps_r)


def main():
    section("1. Velocity, wavelength and vertical resolution")
    print("  v = c / sqrt(eps_r) with c = 0.299792458 m/ns; lambda = v/f")
    print("  vertical resolution is conventionally lambda/4")
    print(f"  {'eps_r':>7s} {'v (m/ns)':>10s} {'f (MHz)':>9s} {'lambda (m)':>11s}"
          f" {'lambda/4 (m)':>13s}")
    for eps_r in (4.0, 9.0, 16.0):
        for f_mhz in (100.0, 250.0, 500.0, 900.0):
            v = velocity(eps_r)
            lam = v * 1.0e3 / f_mhz
            print(f"  {eps_r:7.1f} {v:10.5f} {f_mhz:9.0f} {lam:11.4f} "
                  f"{lam / 4.0:13.4f}")
    print("  -> resolution and penetration move together: a 900 MHz antenna in")
    print("     dry soil resolves 4 cm and reaches very shallow; a 100 MHz")
    print("     antenna in wet soil resolves 25 cm and reaches metres.")

    section("2. Velocity from a diffraction hyperbola")
    t0, x, tx = 10.0, 1.0, 12.8      # ns, m, ns (chosen)
    v = 2.0 * x / np.sqrt(tx ** 2 - t0 ** 2)
    depth = v * t0 / 2.0
    print(f"  apex two-way time t0 = {t0:.1f} ns, at horizontal offset "
          f"x = {x:.1f} m the time is {tx:.1f} ns")
    print(f"  v = 2x / sqrt(tx^2 - t0^2) = 2({x:.1f}) / "
          f"sqrt({tx:.1f}^2 - {t0:.1f}^2) = {v:.4f} m/ns")
    print(f"  implied relative permittivity = (c/v)^2 = "
          f"{(C_M_PER_NS / v) ** 2:.3f}")
    print(f"  depth = v t0 / 2 = {depth:.4f} m")
    print("  -> one hyperbola gives both the velocity and the depth, which is")
    print("     why a single isolated target is the standard field calibration.")
    print("     The offset x must be measured on the ground, not from the file")

    section("3. Trace spacing for migration")
    print("  the sampling requirement is a quarter of the wavelength or finer")
    print(f"  {'eps_r':>7s} {'f (MHz)':>9s} {'lambda (m)':>11s}"
          f" {'required spacing (m)':>21s}")
    for eps_r in (9.0, 16.0):
        for f_mhz in (100.0, 250.0, 500.0):
            lam = velocity(eps_r) * 1.0e3 / f_mhz
            print(f"  {eps_r:7.1f} {f_mhz:9.0f} {lam:11.4f} "
                  f"{lam / 4.0:21.4f}")
    print("  -> a 250 MHz survey in a material of eps_r = 9 needs a trace every")
    print("     0.10 m; pacing at 0.5 m aliases the diffractions that migration")
    print("     is meant to collapse.")

    section("4. Attenuation budget")
    loss_per_m = 1.0        # dB/m one-way (chosen, typical of a lossy material)
    dynamic_range = 100.0   # dB, system dynamic range (chosen)
    print(f"  one-way attenuation {loss_per_m:.1f} dB/m, system dynamic range "
          f"{dynamic_range:.0f} dB")
    print(f"  {'depth (m)':>10s} {'two-way loss (dB)':>18s} {'within range?':>14s}")
    for d in (2.0, 5.0, 10.0, 20.0, 50.0, 100.0):
        loss = 2.0 * loss_per_m * d
        print(f"  {d:10.0f} {loss:18.1f} "
              f"{('yes' if loss <= dynamic_range else 'no'):>14s}")
    print(f"  the maximum depth at this attenuation and range is "
          f"{dynamic_range / (2.0 * loss_per_m):.0f} m")
    print("  -> the depth range is a budget, not a specification: halving the")
    print("     attenuation doubles the range, and attenuation rises with water")
    print("     content and with clay, not only with frequency.")

    section("5. Grid size, data volume and acquisition time")
    n_trace_side = 81
    samples = 512
    bytes_per_sample = 4
    seconds_per_trace = 5.0
    traces = n_trace_side ** 2
    volume_mb = traces * samples * bytes_per_sample / 1.0e6
    hours = traces * seconds_per_trace / 3600.0
    print(f"  a 20 m x 20 m grid at 0.25 m spacing in both directions gives")
    print(f"  {n_trace_side} x {n_trace_side} = {traces} traces")
    print(f"  data volume at {samples} samples and {bytes_per_sample} bytes = "
          f"{volume_mb:.1f} MB")
    print(f"  acquisition time at {seconds_per_trace:.0f} s per trace = "
          f"{hours:.2f} h of continuous work")
    print("  -> the grid must be planned with the crew's realistic rate, which")
    print("     includes moving the antenna, marking, and re-walking lines.")

    section("6. Calibration against a known target")
    true_depth = 1.5
    eps_assumed = 9.0
    t_measured = 31.5
    v_assumed = velocity(eps_assumed)
    v_true = 2.0 * true_depth / t_measured
    depth_reported = v_assumed * t_measured / 2.0
    print(f"  a known target at {true_depth:.2f} m is measured at "
          f"{t_measured:.1f} ns two-way time")
    print(f"  implied true velocity = 2 d / t = {v_true:.5f} m/ns, "
          f"eps_r = {(C_M_PER_NS / v_true) ** 2:.3f}")
    print(f"  depth reported with the assumed eps_r = {eps_assumed:.0f}: "
          f"{depth_reported:.4f} m "
          f"({100.0 * (depth_reported - true_depth) / true_depth:+.2f} %)")
    print("  -> calibration is not optional: the depth scale is the velocity,")
    print("     and the velocity is a property of the ground, not of the antenna.")

    print("\nSYNTHETIC: every number above comes from chosen parameters in this")
    print("file, combined with the standard relations quoted in the text.")


if __name__ == "__main__":
    main()
