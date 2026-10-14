#!/usr/bin/env python3
"""Sensor and transducer arithmetic: sensitivity, bridge output, piezoelectric
high-pass corner, Johnson noise and a selection table, on SYNTHETIC values.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python sensors_and_transducers_demo.py

Everything here is SYNTHETIC.  The gauge factors, capacitances, resistances,
temperature and bandwidths are chosen teaching values, and the relations printed
are the standard ones quoted in the text.  No component data sheet, manufacturer
figure or measured instrument is used or reproduced.

Sections
--------
1. Dynamic range of a sensor, and the resolution a stated range implies.
2. Resistive strain gauge in a quarter bridge: what a strain produces.
3. Piezoelectric sensor: the high-pass corner set by the sensor capacitance and
   the amplifier resistance.
4. Johnson noise of a resistive sensor, and the resolution limit it sets.
5. A selection table by band, dynamic range and environment.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

BOLTZMANN = 1.380649e-23


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def main():
    section("1. Dynamic range and the resolution it implies")
    print("  dynamic range (dB) = 20 log10(full scale / resolution)")
    print(f"  {'full scale':>12s} {'resolution':>13s} {'range (dB)':>12s}"
          f" {'equivalent bits':>17s}")
    cases = [("1 mm displacement", 1.0e-3, 1.0e-9),
             ("10 m/s velocity", 10.0, 1.0e-9),
             ("10 g acceleration", 98.1, 1.0e-6),
             ("1 K temperature", 1.0, 1.0e-4)]
    for label, full, res in cases:
        ratio = full / res
        bits = np.log2(ratio)
        print(f"  {label:>12s} {res:13.1e} {20.0 * np.log10(ratio):12.1f} "
              f"{bits:17.1f}")
    print("  -> the last column is the number of bits a perfect converter would")
    print("     need to cover the range at that resolution; real systems lose")
    print("     several bits to noise and linearity.")

    section("2. Resistive strain gauge in a quarter bridge")
    r_gauge = 350.0
    gauge_factor = 2.0
    bridge_excitation = 5.0
    print(f"  gauge {r_gauge:.0f} ohm, gauge factor {gauge_factor:.1f}, "
          f"bridge excitation {bridge_excitation:.1f} V")
    print(f"  dR = GF R strain; quarter-bridge output = V dR / (4 R)")
    print(f"  {'strain':>12s} {'dR (ohm)':>11s} {'output (mV)':>13s}")
    for strain_micro in (1.0, 10.0, 100.0, 1000.0):
        strain = strain_micro * 1.0e-6
        dr = gauge_factor * r_gauge * strain
        v_out = bridge_excitation * dr / (4.0 * r_gauge)
        print(f"  {strain_micro:12.0f} {dr:11.5f} {v_out * 1000:13.4f}")
    print("  -> a microstrain gives microvolts: the bridge output is small, which")
    print("     is why strain and pressure sensors need instrumentation amplifiers")
    print("     and why their cables must be short and shielded.")

    section("3. Piezoelectric sensor: the high-pass corner")
    capacitance = 1.0e-9
    amplifier_resistance = 1.0e9
    corner = 1.0 / (2.0 * np.pi * amplifier_resistance * capacitance)
    print(f"  sensor capacitance {capacitance * 1e9:.1f} nF, amplifier input")
    print(f"  resistance {amplifier_resistance / 1e9:.1f} Gohm")
    print(f"  corner frequency f = 1/(2 pi R C) = {corner:.4f} Hz")
    print(f"  {'f (Hz)':>9s} {'response (relative)':>20s} {'dB':>8s}")
    for f in (0.01, 0.05, 0.16, 1.0, 10.0, 100.0):
        rel = (f / corner) / np.sqrt(1.0 + (f / corner) ** 2)
        print(f"  {f:9.2f} {rel:20.4f} {20.0 * np.log10(rel):8.2f}")
    print("  -> a piezoelectric sensor cannot measure a static quantity; it")
    print("     measures from the corner upward, and the corner moves if the")
    print("     amplifier or the cable changes the capacitance.")

    section("4. Johnson noise and the resolution floor")
    temperature = 300.0
    bandwidth = 1000.0
    print(f"  v_n = sqrt(4 k T R B) at {temperature:.0f} K over "
          f"{bandwidth:.0f} Hz")
    print(f"  {'R (ohm)':>10s} {'v_n (nV)':>11s} {'v_n/sqrt(B) (nV/rtHz)':>24s}")
    for resistance in (100.0, 1000.0, 10000.0, 100000.0, 1000000.0):
        vn = np.sqrt(4.0 * BOLTZMANN * temperature * resistance * bandwidth)
        print(f"  {resistance:10.0f} {vn * 1e9:11.3f} "
              f"{vn / np.sqrt(bandwidth) * 1e9:24.3f}")
    print("  -> the noise rises as sqrt(R) while the signal from a bridge falls")
    print("     only weakly with R: high-resistance sensors are quieter in")
    print("     *current* terms but need low input noise voltage, and the")
    print("     amplifier's own current noise then dominates.")

    section("5. Selection by band, range and environment")
    print(f"  {'principle':<22s} {'band':<18s} {'strength':<28s} {'limitation':<26s}")
    rows = [("resistive strain", "DC to kHz", "simple, absolute, rugged",
             "self-heating, drift"),
            ("piezoelectric", "0.1 Hz to MHz", "wide band, high sensitivity",
             "no DC, charge leakage"),
            ("capacitive", "DC to kHz", "very high resolution",
             "stray capacitance, humidity"),
            ("inductive/eddy", "DC to tens of kHz", "non-contact, robust",
             "conductive targets only"),
            ("optical fibre", "DC to GHz", "immune to EMI, distributed",
             "fragile, costlier"),
            ("MEMS", "DC to tens of kHz", "small, cheap, arrayable",
             "higher noise, drift")]
    for principle, band, strength, limitation in rows:
        print(f"  {principle:<22s} {band:<18s} {strength:<28s} {limitation:<26s}")
    print("  -> the selection is driven by the band, the environment and the")
    print("     required dynamic range; no single principle wins everywhere.")

    print("\nSYNTHETIC: every number above comes from chosen parameters in this")
    print("file, combined with the standard relations quoted in the text.")


if __name__ == "__main__":
    main()
