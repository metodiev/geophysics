#!/usr/bin/env python3
"""Signal-conditioning arithmetic: input-referred noise, noise figure, two-stage
gain, effective number of bits, oversampling and anti-alias filter order, on
SYNTHETIC values.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python signal_conditioning_demo.py

Everything here is SYNTHETIC.  The amplifier noise densities, gains, converter
figures, oversampling ratios and filter specifications are chosen teaching values,
and the relations printed are the standard ones quoted in the text.  No component
data sheet or manufacturer figure is used or reproduced.

Sections
--------
1. Input-referred noise of an amplifier plus source, and the noise figure.
2. Two-stage gain: why the first stage dominates.
3. Effective number of bits from SINAD.
4. What oversampling and decimation buy.
5. Anti-alias filter order from the transition ratio.
6. Gain-bandwidth: the amplifier's own frequency limit.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

BOLTZMANN = 1.380649e-23
TEMPERATURE = 300.0


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def main():
    section("1. Input-referred noise and the noise figure")
    e_n = 10.0e-9      # V/sqrt(Hz) amplifier voltage noise (chosen)
    i_n = 1.0e-12      # A/sqrt(Hz) amplifier current noise (chosen)
    print(f"  amplifier: e_n = {e_n * 1e9:.1f} nV/rtHz, "
          f"i_n = {i_n * 1e12:.1f} pA/rtHz")
    print(f"  source noise = sqrt(4 k T R) at T = {TEMPERATURE:.0f} K")
    print(f"  {'R (ohm)':>10s} {'source (nV/rtHz)':>17s} {'total (nV/rtHz)':>16s}"
          f" {'noise figure (dB)':>18s}")
    best = (None, 1e9)
    for resistance in (100.0, 1000.0, 10000.0, 100000.0, 1000000.0):
        source = np.sqrt(4.0 * BOLTZMANN * TEMPERATURE * resistance)
        total = np.sqrt(e_n ** 2 + (i_n * resistance) ** 2 + source ** 2)
        nf = 10.0 * np.log10(total ** 2 / source ** 2)
        if nf < best[1]:
            best = (resistance, nf)
        print(f"  {resistance:10.0f} {source * 1e9:17.3f} {total * 1e9:16.3f} "
              f"{nf:18.2f}")
    r_opt = e_n / i_n
    print(f"  the noise figure is minimised near R = e_n/i_n = "
          f"{r_opt / 1000.0:.1f} kohm (best tabulated: "
          f"{best[0] / 1000.0:.1f} kohm at {best[1]:.2f} dB)")
    print("  -> the *noise figure* is a ratio and has a minimum; the absolute")
    print("     input-referred noise falls monotonically as R falls, so the two")
    print("     optima are not the same quantity.")

    section("2. Two-stage gain and the Friis formula")
    print("  F_total = F1 + (F2 - 1)/G1")
    stages = [("low-noise first", 1.5, 100.0, 4.0),
              ("high-gain first", 4.0, 100.0, 1.5)]
    for label, f1, g1, f2 in stages:
        total = f1 + (f2 - 1.0) / g1
        print(f"  {label:<18s} F1 = {f1:.1f}, G1 = {g1:.0f}, F2 = {f2:.1f} -> "
              f"F_total = {total:.4f} ({10.0 * np.log10(total):.2f} dB)")
    print("  -> with a 20 dB first-stage gain the second stage contributes 1/G1")
    print("     of its excess noise: 3/100 here.  Reverse the order and the")
    print("     total noise figure is set by the noisy stage.")

    section("3. Effective number of bits from SINAD")
    print("  ENOB = (SINAD - 1.76)/6.02")
    print(f"  {'SINAD (dB)':>11s} {'ENOB (bits)':>12s}")
    for sinad in (60.0, 70.0, 90.0, 110.0, 130.0):
        print(f"  {sinad:11.1f} {(sinad - 1.76) / 6.02:12.2f}")
    print("  -> a converter quoted at 24 bits with a measured SINAD of 110 dB")
    print("     delivers 17.98 effective bits; the rest is lost to noise and")
    print("     distortion, and the loss is what the measurement actually sees.")

    section("4. Oversampling and decimation")
    print("  each doubling of the sample rate buys 0.5 bit, before decimation")
    print(f"  {'oversampling':>13s} {'bits bought':>12s} {'16-bit base':>12s}")
    for ratio in (1, 4, 16, 64, 256, 1024):
        bits = 0.5 * np.log2(ratio)
        print(f"  {ratio:13d} {bits:12.2f} {16.0 + bits:12.2f}")
    print("  -> 256x oversampling turns a 16-bit converter into an effective")
    print("     20-bit one, at the cost of the sample rate and the digital")
    print("     filtering, and only for noise that is white and uncorrelated.")

    section("5. Anti-alias filter order")
    print("  Butterworth attenuation 10 log10(1 + (f/fc)^(2n))")
    print(f"  {'f/fc':>7s} {'order for 60 dB':>16s} {'order for 100 dB':>17s}")
    for ratio in (1.5, 2.0, 4.0, 10.0):
        n60 = 60.0 / (20.0 * np.log10(ratio))
        n100 = 100.0 / (20.0 * np.log10(ratio))
        print(f"  {ratio:7.1f} {np.ceil(n60):16.0f} {np.ceil(n100):17.0f}")
    print("  -> the order is set by the *transition ratio*, not by the")
    print("     attenuation alone: asking for a corner close to the band edge")
    print("     is what makes the filter expensive.")

    section("6. Gain-bandwidth product")
    gbw = 10.0e6      # Hz, chosen op-amp gain-bandwidth product
    print(f"  op-amp gain-bandwidth product {gbw / 1e6:.1f} MHz")
    print(f"  {'gain':>8s} {'closed-loop bandwidth (kHz)':>27s}")
    for gain in (1.0, 10.0, 100.0, 1000.0, 10000.0):
        print(f"  {gain:8.0f} {gbw / gain / 1000.0:27.2f}")
    print("  -> gain and bandwidth trade directly: a gain of 1000 leaves 10 kHz,")
    print("     which may be below the anti-alias corner the design needs, and")
    print("     is why high-gain low-frequency instrumentation uses multi-stage")
    print("     designs rather than one large gain.")

    print("\nSYNTHETIC: every number above comes from chosen parameters in this")
    print("file, combined with the standard relations quoted in the text.")


if __name__ == "__main__":
    main()
