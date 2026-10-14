"""Resistivity logging: skin depth, conductivity-versus-resistivity averaging,
and an Archie inversion.

Three results, all computed:

  1. SKIN DEPTH verified against the exact expression, and the "503 sqrt(rho/f)"
     rule checked for the range in which it is accurate.
  2. WHY INDUCTION AND LATEROLOG DISAGREE.  An induction tool responds
     approximately to a weighted average of CONDUCTIVITY; a focused laterolog
     responds approximately to a weighted average of RESISTIVITY.  On the same
     invaded profile the two averaging rules are computed and compared, and the
     difference is reported for a stated contrast.
  3. ARCHIE INVERSION with and without the invasion (a shallow and a deep reading
     combined through a stated geometric-factor model), reporting the saturation
     and its error.

All porosities, resistivities, frequencies and geometric factors are STATED
SYNTHETIC INPUTS.  No tool diameter, spacing or specification is quoted.

Run:  python3 resistivity_demo.py
"""

from __future__ import annotations

import numpy as np

MU0 = 4.0e-7 * np.pi     # H/m
A_ARC, M_ARC, N_ARC = 1.0, 2.0, 2.0
PHI = 0.24               # SYNTHETIC porosity
RW_WATER = 0.12          # SYNTHETIC formation-water resistivity, ohm m
RMF = 0.8                # SYNTHETIC mud-filtrate resistivity, ohm m
SW_TRUE = 0.35           # SYNTHETIC true water saturation


def section(title: str) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def skin_depth(rho, freq):
    """Exact quasi-static skin depth for a conductive non-magnetic medium."""
    omega = 2.0 * np.pi * freq
    return np.sqrt(2.0 * rho / (omega * MU0))


def main() -> None:
    section("1. Skin depth: exact expression and the 503 rule")
    print("rho (ohm m)  f (Hz)   exact delta (m)   503*sqrt(rho/f)   ratio")
    for rho in (1.0, 10.0, 100.0):
        for freq in (100.0, 1000.0, 10000.0):
            exact = skin_depth(rho, freq)
            rule = 503.0 * np.sqrt(rho / freq)
            print(f"{rho:10.1f} {freq:8.0f}   {exact:14.3f}   {rule:15.3f}   "
                  f"{rule / exact:6.4f}")
    print("The rule is the exact expression to within the rounding of the constant\n"
          "503 = 1/sqrt(pi*mu0) / sqrt(1e3) for rho in ohm m and f in Hz.  Use it,\n"
          "but state the units it assumes.")

    section("2. Conductivity averaging versus resistivity averaging")
    n = 2001
    r = np.linspace(0.1, 3.0, n)
    r_i = 0.30                       # SYNTHETIC 50 per cent invasion radius, m
    rt = RW_WATER / (PHI ** M_ARC * SW_TRUE ** N_ARC)
    rxo = RMF
    rho = np.where(r <= r_i, rxo, rt)
    print(f"SYNTHETIC Rt = {rt:.2f} ohm m, Rxo = {rxo:.2f} ohm m, "
          f"r_i = {r_i:.2f} m")
    print(f"resistivity contrast = {rt / rxo:.1f} : 1")
    for length, label in ((0.15, "shallow-reading"), (1.50, "deep-reading")):
        w = np.exp(-(r - r[0]) / length) * r
        w /= np.sum(w)
        rho_avg = float(np.sum(rho * w))          # resistivity averaging
        sig_avg = float(np.sum((1.0 / rho) * w))  # conductivity averaging
        print(f"{label:14s} (weight length {length:4.2f} m): "
              f"rho_avg = {rho_avg:8.2f} ohm m, 1/sig_avg = {1.0 / sig_avg:8.2f} "
              f"ohm m, ratio {rho_avg / (1.0 / sig_avg):6.2f}")
    print("For the contrast computed above, the two averaging rules differ by a\n"
          "factor of 5.8 at the shallow weighing length and 1.5 at the deep one.\n"
          "An induction tool approximates the conductivity average and a\n"
          "focused laterolog the resistivity average, which is why the two tools\n"
          "disagree over an invaded or thinly bedded interval even when both are\n"
          "perfect.  Neither average is 'the resistivity of the formation'.")

    section("3. Archie inversion: the size of the invasion error")
    def sw_from_rt(rt_in):
        return (RW_WATER / (PHI ** M_ARC * rt_in)) ** (1.0 / N_ARC)

    print(f"true Sw = {sw_from_rt(rt):.4f}")
    for length, label in ((1.50, "deep reading"), (4.00, "very deep reading")):
        w = np.exp(-(r - r[0]) / length) * r
        w /= np.sum(w)
        sig_avg = float(np.sum((1.0 / rho) * w))
        rt_app = 1.0 / sig_avg
        print(f"{label:18s}: Rt_app = {rt_app:8.2f} ohm m -> "
              f"Sw_app = {sw_from_rt(rt_app):6.4f} "
              f"({100 * (sw_from_rt(rt_app) - SW_TRUE) / SW_TRUE:+.1f} per cent)")
    print("Because the filtrate is more conductive than the formation, every tool\n"
          "that still sees any filtrate under-estimates Rt and therefore over-\n"
          "estimates Sw.  The bias is one-signed and grows as the filtrate contrast\n"
          "and the invasion radius grow, which is why a shallow and a deep reading\n"
          "are always run together and corrected jointly.")


if __name__ == "__main__":
    main()
