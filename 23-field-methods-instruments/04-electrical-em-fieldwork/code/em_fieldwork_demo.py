#!/usr/bin/env python3
"""EM fieldwork arithmetic: skin depth, induction number, TDEM diffusion time,
coil orientation, cultural coupling and stacking, on SYNTHETIC values.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python em_fieldwork_demo.py

Everything here is SYNTHETIC: the resistivities, coil spacings, times,
orientations and cultural-noise levels are chosen teaching values.  No field
dataset, instrument specification or commercial system is reproduced.

Sections
--------
1. Skin depth as a function of resistivity and frequency.
2. Induction number for a coil separation, and where the low-induction-number
   approximation stops applying.
3. Time-domain diffusion depth and the time at which a target depth is sensed.
4. Coil orientation and the depth of exploration.
5. Cultural coupling: the fall-off with distance from a power line.
6. Stacking: the sqrt(N) gain and the time it costs.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

MU0 = 4.0e-7 * np.pi


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def skin_depth(rho, f):
    """Plane-wave skin depth, m: delta = sqrt(2 / (omega mu0 sigma))."""
    return np.sqrt(2.0 * rho / (2.0 * np.pi * f * MU0))


def main():
    section("1. Skin depth")
    print("  delta = sqrt(2 rho / (omega mu0)) = 503.3 sqrt(rho / f) m")
    print(f"  {'rho (ohm m)':>12s} {'f (Hz)':>8s} {'delta (m)':>11s}"
          f" {'coefficient':>13s}")
    for rho in (10.0, 100.0, 1000.0):
        for f in (10.0, 100.0, 1000.0):
            d = skin_depth(rho, f)
            print(f"  {rho:12.0f} {f:8.0f} {d:11.2f} "
                  f"{d / np.sqrt(rho / f):13.2f}")
    print("  -> the coefficient 503.3 is not a constant of nature but the")
    print("     combination sqrt(2/(2 pi mu0)) of the definitions.")

    section("2. Induction number of a coil pair")
    spacing = 20.0
    print(f"  coil separation s = {spacing:.0f} m; induction number B = s/delta")
    print(f"  the low-induction-number approximation requires B << 1")
    print(f"  {'rho (ohm m)':>12s} {'f (Hz)':>8s} {'delta (m)':>11s}"
          f" {'B = s/delta':>12s} {'LIN valid?':>11s}")
    for rho in (10.0, 100.0, 1000.0):
        for f in (1000.0, 10000.0, 100000.0):
            d = skin_depth(rho, f)
            b = spacing / d
            print(f"  {rho:12.0f} {f:8.0f} {d:11.2f} {b:12.3f} "
                  f"{('yes' if b < 0.3 else 'no'):>11s}")
    print("  -> at 100 kHz over 10 ohm m the induction number exceeds 1 and the")
    print("     linear relation between response and conductivity fails.")

    section("3. Time-domain diffusion")
    print("  diffusion depth  delta_t = sqrt(2 t / (mu0 sigma))")
    print("  the smoke ring reaches depth d at about t = mu0 sigma d^2 / 2")
    print(f"  {'sigma (S/m)':>12s} {'d (m)':>7s} {'t (ms)':>10s}"
          f" {'delta_t at that t (m)':>23s}")
    for sigma in (0.01, 0.1, 1.0):
        for d in (50.0, 200.0, 500.0):
            t = MU0 * sigma * d ** 2 / 2.0
            print(f"  {sigma:12.2f} {d:7.0f} {t * 1000.0:10.3f} "
                  f"{np.sqrt(2.0 * t / (MU0 * sigma)):23.1f}")
    print("  -> the sensing time grows as sigma d^2: doubling the depth is four")
    print("     times the delay, which is what sets the recording window.")

    section("4. Coil orientation and depth of exploration")
    print("  the depth of exploration is conventionally of order 0.5-1.5 times")
    print("  the coil separation, and the coefficient depends on the orientation")
    print(f"  {'orientation':<26s} {'coefficient':>12s} {'depth at s = 20 m':>19s}")
    for label, coeff in (("horizontal coplanar", 1.5),
                         ("vertical coplanar", 1.0),
                         ("perpendicular", 0.5)):
        print(f"  {label:<26s} {coeff:12.1f} {coeff * spacing:19.1f} m")
    print("  (coefficients are conventions taken from the method's practice, not")
    print("   derived here; they depend on the target and the ground)")

    section("5. Cultural coupling from a power line")
    line_current = 100.0
    print(f"  a power line carries a current that produces a magnetic field")
    print(f"  falling roughly as 1/r for a long straight conductor, and the")
    print(f"  *induced* voltage in a coil falls as (1/r) x (1/r) for a small loop")
    print(f"  {'distance r (m)':>16s} {'relative coupling':>19s}"
          f" {'relative (dB)':>15s}")
    reference = None
    for r in (10.0, 20.0, 50.0, 100.0, 200.0):
        coupling = 1.0 / r ** 2
        if reference is None:
            reference = coupling
            rel = 1.0
        else:
            rel = coupling / reference
        print(f"  {r:16.0f} {rel:19.4f} {20.0 * np.log10(rel):15.1f}")
    print(f"  line current in the model = {line_current:.0f} A (chosen); the")
    print(f"  point is the exponent, not the level: doubling the distance costs")
    print(f"  12 dB, so a 40 dB reduction needs a factor of 100 in distance.")

    section("6. Stacking")
    print(f"  {'stacks':>8s} {'gain sqrt(N)':>13s} {'dB':>7s} {'time at 1 s each':>18s}")
    for n in (1, 4, 16, 64, 256):
        print(f"  {n:8d} {np.sqrt(n):13.3f} {10.0 * np.log10(n):7.2f} "
              f"{n:15d} s")
    print("  -> stacking buys 3 dB per doubling of the recording time, until")
    print("     the noise becomes correlated between stacks and the gain stops.")

    print("\nSYNTHETIC: every number above comes from chosen parameters in this")
    print("file.  They constrain an acquisition model, not any real system.")


if __name__ == "__main__":
    main()
