#!/usr/bin/env python3
"""ERT fieldwork arithmetic: geometric factors, contact resistance, injected
current, reciprocity, error propagation and data density, on SYNTHETIC values.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python ert_fieldwork_demo.py

Everything here is SYNTHETIC.  The electrode positions, contact resistances,
voltage limits, noise floors and electrode counts are chosen teaching values.  No
field measurement, instrument specification or commercial protocol is reproduced.

Sections
--------
1. Geometric factors of the standard arrays, from the exact four-electrode formula.
2. Apparent resistivity and its standard error from the measured voltage and current.
3. Contact resistance, injected current and what a dry surface costs in SNR.
4. Reciprocity: what difference between a measurement and its reciprocal is noise.
5. Data density: how many four-electrode configurations an electrode spread allows.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

TWO_PI = 2.0 * np.pi


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def geometric_factor(a_pos, b_pos, m_pos, n_pos):
    """K = 2 pi / (1/AM - 1/BM - 1/AN + 1/BN), positions in metres."""
    am = abs(m_pos - a_pos)
    bm = abs(m_pos - b_pos)
    an = abs(n_pos - a_pos)
    bn = abs(n_pos - b_pos)
    return TWO_PI / (1.0 / am - 1.0 / bm - 1.0 / an + 1.0 / bn)


def main():
    section("1. Geometric factors from the exact four-electrode formula")
    print("  K = 2 pi / (1/AM - 1/BM - 1/AN + 1/BN), positions in metres")
    print(f"  {'array':<22s} {'geometry':<34s} {'K (m)':>12s}")
    a = 5.0
    # Wenner: A=0, M=a, N=2a, B=3a
    k_wenner = geometric_factor(0.0, 3.0 * a, a, 2.0 * a)
    print(f"  {'Wenner':<22s} {'a = 5 m':<34s} {k_wenner:12.4f}")
    print(f"  {'  closed form 2 pi a':<22s} {'':<34s} {TWO_PI * a:12.4f}")
    # Schlumberger: A=-L, B=+L, M=-b, N=+b
    L, b = 50.0, 5.0
    k_schl = geometric_factor(-L, L, -b, b)
    approx = np.pi * (L ** 2 - b ** 2) / (2.0 * b)
    print(f"  {'Schlumberger':<22s} {'L = 50 m, b = 5 m':<34s} {k_schl:12.4f}")
    print(f"  {'  pi(L^2-b^2)/(2b)':<22s} {'':<34s} {approx:12.4f}")
    # Dipole-dipole: current dipole A=0, B=a; potential dipole at (n+1)a, (n+2)a
    for n in (1, 3, 6):
        k_dd = abs(geometric_factor(0.0, a, (1.0 + n) * a, (1.0 + n) * a + a))
        print(f"  {'Dipole-dipole n = ' + str(n):<22s} "
              f"{'a = 5 m':<34s} {k_dd:12.4f}")
        print(f"  {'  closed form':<22s} {'pi n (n+1)(n+2) a':<34s} "
              f"{np.pi * n * (n + 1) * (n + 2) * a:12.4f}")

    section("2. Apparent resistivity and its standard error")
    K = k_wenner
    dv = 12.5e-3      # V, measured potential difference (chosen)
    current = 5.0e-3  # A, injected current (chosen)
    rho = K * dv / current
    print(f"  Wenner a = {a:.0f} m: K = {K:.4f} m, dV = {dv * 1000:.2f} mV, "
          f"I = {current * 1000:.1f} mA")
    print(f"  apparent resistivity = K dV / I = {rho:.4f} ohm m")
    print(f"  {'dV error':>10s} {'I error':>10s} {'rho error (%)':>15s}")
    for e_dv, e_i in ((0.01, 0.005), (0.02, 0.01), (0.05, 0.02)):
        rel = np.sqrt(e_dv ** 2 + e_i ** 2)
        print(f"  {e_dv:10.3f} {e_i:10.3f} {100.0 * rel:15.3f}")
    print("  -> the relative error is the quadrature sum of the two relative")
    print("     errors; a 5 % voltage error and a 2 % current error give 5.4 %.")

    section("3. Contact resistance, injected current and signal level")
    v_max = 100.0          # V, transmitter compliance (chosen)
    print(f"  transmitter compliance = {v_max:.0f} V; the injected current is")
    print(f"  limited by the loop resistance R = 2 R_contact + R_ground")
    print(f"  {'contact R (ohm)':>15s} {'loop R (ohm)':>13s} {'I (mA)':>9s}"
          f" {'dV (mV)':>10s} {'relative (dB)':>14s}")
    reference = None
    for r_contact in (200.0, 1000.0, 5000.0, 20000.0, 100000.0):
        loop_r = 2.0 * r_contact + 50.0
        i = v_max / loop_r
        dv_signal = i * (rho / K)
        if reference is None:
            reference = dv_signal
        print(f"  {r_contact:15.0f} {loop_r:13.0f} {i * 1000:9.3f} "
              f"{dv_signal * 1000:10.4f} "
              f"{20.0 * np.log10(dv_signal / reference):14.1f}")
    print("  -> with a voltage-limited transmitter the signal falls as")
    print("     1/(2 R_contact + R_ground): a 100 kOhm contact against a 200 Ohm")
    print("     contact costs 54 dB of signal.  Improving the electrode contact")
    print("     (watering, deeper stakes, bentonite) is a data-quality action.")
    print("  (the receiver noise floor is not modelled here; the column is the")
    print("   signal relative to the best contact, not a signal-to-noise ratio)")

    section("4. Reciprocity")
    print("  a reciprocal measurement swaps the current and potential electrode")
    print("  pairs; in a correct system the apparent resistivity is unchanged")
    print("  to within the measurement error")
    print(f"  {'noise (% of dV)':>17s} {'expected |d rho|/rho (%)':>26s}")
    for frac in (0.01, 0.02, 0.05, 0.10):
        expected = frac * np.sqrt(2.0) * 100.0
        print(f"  {100.0 * frac:17.1f} {expected:26.3f}")
    print("  -> the tolerance is sqrt(2) times the voltage error, and a")
    print("     reciprocal difference that exceeds it by a factor of several")
    print("     indicates a geometry error, a cable fault or a non-linear")
    print("     coupling at an electrode, not noise.")

    section("5. Data density of an electrode spread")
    n_elec = 48
    print(f"  {n_elec} electrodes: number of distinct four-electrode")
    print(f"  configurations = C({n_elec},4) = "
          f"{n_elec * (n_elec - 1) * (n_elec - 2) * (n_elec - 3) // 24}")
    for n in (24, 48, 96):
        total = n * (n - 1) * (n - 2) * (n - 3) // 24
        print(f"  {n:3d} electrodes -> {total:8d} configurations, of which a")
        print(f"      typical protocol measures about {min(total, 20 * n)} "
              f"(~{min(total, 20 * n) / total * 100:.2f} % of the space)")
    print("  -> the configuration count grows as n^4 while the electrodes grow")
    print("     as n: a protocol is a choice of which few thousand to measure.")

    print("\nSYNTHETIC: every number above comes from chosen parameters in this")
    print("file.  They constrain an acquisition model, not any real survey.")


if __name__ == "__main__":
    main()
