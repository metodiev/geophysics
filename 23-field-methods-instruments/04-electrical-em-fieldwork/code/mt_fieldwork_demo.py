#!/usr/bin/env python3
"""Magnetotelluric fieldwork arithmetic: impedance levels, coherence requirements,
dead-band recording time, telluric dipole response, remote-reference bias and site
footprint, on SYNTHETIC values.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python mt_fieldwork_demo.py

Everything here is SYNTHETIC.  The resistivities, dipole lengths, noise levels and
coherences are chosen teaching values, and every relation is the standard MT
formula quoted in the printed text.  No field dataset, instrument specification or
published MT response is reproduced.

Sections
--------
1. Impedance magnitude for a stated apparent resistivity and frequency.
2. The coherence required for a stated accuracy from a stated number of estimates.
3. Dead-band recording time: the cost of a weaker natural signal.
4. Telluric dipole length and the signal it produces against a stated noise floor.
5. Remote reference: the bias a coherent local noise source produces.
6. Site footprint: cables, electrodes and the area a site occupies.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

MU0 = 4.0e-7 * np.pi


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def impedance_magnitude(rho, f):
    """|Z| = sqrt(omega mu0 rho) for a uniform half-space."""
    return np.sqrt(2.0 * np.pi * f * MU0 * rho)


def main():
    section("1. Impedance magnitude from apparent resistivity")
    print("  rho_a = |Z|^2 / (omega mu0), so |Z| = sqrt(omega mu0 rho_a)")
    b_test = 1.0e-9                      # 1 nT
    h_test = b_test / MU0                # equivalent H in A/m
    print(f"  the E field produced by a {b_test * 1e9:.1f} nT magnetic signal is")
    print(f"  E = Z H with H = {h_test * 1e3:.6f} mA/m")
    print(f"  {'rho_a (ohm m)':>14s} {'f (Hz)':>8s} {'|Z| (ohm)':>12s}"
          f" {'E for 1 nT (mV/km)':>21s}")
    for f in (0.1, 1.0, 10.0):
        for rho in (10.0, 100.0, 1000.0):
            z = impedance_magnitude(rho, f)
            e_mv_km = z * h_test * 1.0e6
            print(f"  {rho:14.0f} {f:8.1f} {z:12.5f} {e_mv_km:21.3f}")
    print("  -> a 1 nT signal at 1 Hz over 100 ohm m produces about 22 mV/km:")
    print("     the telluric signal is small and grows with the impedance.")

    section("2. Coherence required for a stated accuracy")
    print("  the impedance estimator has sigma/|Z| = sqrt((1-g^2)/(2 N g^2)),")
    print("  so the coherence required is g = 1/sqrt(1 + 2 N sigma^2)")
    print(f"  {'target sigma':>14s}" + "".join(f"{'N=' + str(n):>12s}"
                                               for n in (20, 100, 400)))
    for sigma in (0.01, 0.02, 0.05):
        row = f"  {100.0 * sigma:13.0f}%"
        for n in (20, 100, 400):
            g = 1.0 / np.sqrt(1.0 + 2.0 * n * sigma ** 2)
            row += f"{g:12.4f}"
        print(row)
    print("  -> a 1 % accuracy needs a coherence of 0.998 from 20 estimates and")
    print("     0.990 from 400: coherence, not averaging alone, sets the quality.")

    section("3. Dead-band recording time")
    print("  for a fixed accuracy the number of independent estimates scales as")
    print("  N ~ (1 - g^2)/g^2, so the recording time scales the same way")
    print(f"  {'coherence g':>13s} {'relative time':>15s} {'relative to g=0.99':>20s}")
    reference = (1.0 - 0.99 ** 2) / 0.99 ** 2
    for g in (0.99, 0.98, 0.95, 0.90, 0.80):
        n_rel = (1.0 - g ** 2) / g ** 2
        print(f"  {g:13.2f} {n_rel:15.5f} {n_rel / reference:20.2f}")
    print("  -> a band whose coherence falls from 0.99 to 0.90 needs about 11.6")
    print("     times the recording time for the same impedance accuracy.  This")
    print("     is the quantitative statement of the MT dead band.")

    section("4. Telluric dipole length against the noise floor")
    e_field = 1.0e-6      # V/m, i.e. 1 mV/km (chosen)
    noise = 5.0e-6        # V, electrode pair plus preamplifier (chosen)
    print(f"  telluric field = {e_field * 1e6:.1f} mV/km, electrode noise = "
          f"{noise * 1e6:.1f} uV")
    print(f"  {'dipole L (m)':>13s} {'signal (uV)':>13s} {'SNR (dB)':>10s}")
    for length in (25.0, 50.0, 100.0, 200.0, 400.0):
        v = e_field * length
        print(f"  {length:13.0f} {v * 1e6:13.2f} "
              f"{20.0 * np.log10(v / noise):10.1f}")
    print("  -> the signal is proportional to the dipole length, so a 200 m")
    print("     dipole buys 18 dB over a 25 m dipole at the same field.")

    section("5. Remote reference: the bias a coherent noise source produces")
    print("  single-station bias factor = 1/sqrt(1 - g_noise^2), where g_noise is")
    print("  the coherence between the local noise in E and in H")
    print(f"  {'g_noise':>9s} {'bias factor':>13s} {'apparent rho error':>20s}")
    for g in (0.3, 0.5, 0.7, 0.9):
        factor = 1.0 / np.sqrt(1.0 - g ** 2)
        print(f"  {g:9.1f} {factor:13.4f} {100.0 * (factor ** 2 - 1.0):19.1f} %")
    print("  -> a coherent noise source with 0.9 coherence doubles the impedance")
    print("     and quadruples the apparent resistivity; a remote reference that")
    print("     is uncorrelated with that noise removes the bias.")

    section("6. Site footprint")
    dipole = 100.0
    n_electrode = 4
    magnetic_offset = 10.0
    print(f"  two orthogonal telluric dipoles of {dipole:.0f} m, "
          f"{n_electrode} electrodes per dipole")
    print(f"  three magnetic sensors offset at least {magnetic_offset:.0f} m from")
    print(f"  the electrodes")
    print(f"  footprint = {dipole:.0f} m x {dipole:.0f} m = "
          f"{(dipole / 1000.0) ** 2:.4f} km2")
    print(f"  electrodes = {2 * n_electrode}, plus earth pits for each")
    print(f"  cable length (two dipoles, four leads) = "
          f"{4 * dipole:.0f} m of telluric cable")
    print("  -> a site occupies about 0.01 km2 at this dipole length, which is")
    print("     the quantity to compare with the land available and the grid.")

    print("\nSYNTHETIC: every number above comes from chosen parameters in this")
    print("file, combined with the standard MT formulas quoted in the text.")


if __name__ == "__main__":
    main()
