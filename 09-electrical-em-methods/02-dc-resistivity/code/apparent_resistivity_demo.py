#!/usr/bin/env python3
"""Apparent resistivity: sounding curves, the geometric factor, and equivalence.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python apparent_resistivity_demo.py

Everything is SYNTHETIC.  The layered models, the resistivities and the noise
level are chosen teaching values; no field data are used.

Contents
--------
1. Apparent resistivity of a two-layer model versus spacing, with asymptotes.
2. What the voltmeter actually reads: dV from the geometric factor.
3. Equivalence: families of thin layers with indistinguishable sounding curves.
4. Equivalence against noise: how many models the data cannot separate.
"""

import numpy as np
from scipy.integrate import quad
from scipy.special import j0

RNG = np.random.default_rng(20261014)

I_INJECT = 0.1          # A
NOISE_FLOOR_REL = 0.02  # 2% relative noise on dV


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def kernel_R(rhos, hs, lam):
    R = 0.0
    for i in range(len(hs) - 1, -1, -1):
        k = (rhos[i + 1] - rhos[i]) / (rhos[i + 1] + rhos[i])
        R = (k + R) * np.exp(-2.0 * lam * hs[i]) / (1.0 + k * R)
    return R


def layered_potential(rhos, hs, r, I=1.0):
    lam_max = 30.0 / min(hs)
    integrand = (lambda lam: (1.0 / (1.0 - kernel_R(rhos, hs, lam)) - 1.0)
                 * j0(lam * r))
    value, _ = quad(integrand, 0.0, lam_max, limit=600)
    return rhos[0] * I / (2.0 * np.pi) * (1.0 / abs(r) + value)


def wenner_rhoa(rhos, hs, a, I=I_INJECT):
    """Apparent resistivity of a Wenner array of spacing a on a layered model."""
    k = 2.0 * np.pi * a
    dV = (layered_potential(rhos, hs, a, I)
          - layered_potential(rhos, hs, 2.0 * a, I)
          - layered_potential(rhos, hs, 2.0 * a, I)
          + layered_potential(rhos, hs, a, I))
    return k * dV / I, dV


def main():
    section("1. Two-layer sounding curves: rho_a versus spacing")
    rho1, h1 = 100.0, 10.0
    spacings = np.array([0.5, 1.0, 2.0, 3.0, 5.0, 8.0, 12.0, 20.0, 30.0, 50.0,
                         80.0, 120.0, 200.0])
    print(f"  SYNTHETIC model: rho_1 = {rho1:.0f} ohm m, h_1 = {h1:.0f} m;")
    print(f"  Wenner array, current I = {I_INJECT:.2f} A.")
    print("     a (m)   rho_a (rho_2 = 1000)   rho_a (rho_2 = 10)   dV (V, "
          "resistive case)")
    rows = {}
    for rho2 in (1000.0, 10.0):
        rows[rho2] = [wenner_rhoa([rho1, rho2], [h1], a) for a in spacings]
    for j, a in enumerate(spacings):
        print(f"  {a:8.1f} {rows[1000.0][j][0]:21.2f} {rows[10.0][j][0]:20.2f} "
              f"{rows[1000.0][j][1]:17.6f}")
    print(f"\n  small spacing: rho_a -> {rows[1000.0][0][0]:.2f} and "
          f"{rows[10.0][0][0]:.2f} ohm m (the top layer, {rho1:.0f} ohm m)")
    print(f"  large spacing: rho_a -> {rows[1000.0][-1][0]:.2f} and "
          f"{rows[10.0][-1][0]:.2f} ohm m (the half-space, 1000 and 10)")
    print("  a conductive half-space pulls rho_a DOWN, a resistive one pulls it")
    print("  UP, and both cross over near a ~ 2-3 x the layer thickness.")

    section("2. What the receiver sees: dV = rho_a I / k")
    print("  Wenner geometric factor k = 2 pi a, so dV falls as 1/a for a fixed")
    print("  apparent resistivity:")
    print("     a (m)     k (m)      dV (mV) for rho_a = 100 ohm m")
    for a in (1.0, 5.0, 20.0, 100.0, 500.0):
        k = 2.0 * np.pi * a
        print(f"  {a:8.1f} {k:10.2f} {100.0 * I_INJECT / k * 1e3:33.4f}")
    print("  a sounding is a battle between two trends: longer spacings carry")
    print("  deeper information and less signal, and the ratio is fixed.")

    section("3. Equivalence: a resistive thin layer")
    # S-equivalence: a thin resistive layer in a conductive host, h2/rho2 fixed.
    print("  SYNTHETIC three-layer model: rho_1 = 100, rho_3 = 20 ohm m,")
    print("  h_1 = 5 m; the middle layer is thin and resistive.")
    base = ([100.0, 500.0, 20.0], [5.0, 4.0])
    print(f"  reference: rho_2 = {base[0][1]:.0f} ohm m, h_2 = {base[1][1]:.1f} m")
    T_ref = base[1][1] * base[0][1]
    spacings3 = np.array([1.0, 2.0, 3.0, 5.0, 8.0, 12.0, 20.0, 30.0, 50.0,
                          80.0, 120.0])
    ref_curve = np.array([wenner_rhoa(base[0], base[1], a)[0] for a in spacings3])
    print(f"  a thin RESISTIVE layer is crossed by vertical current, so the")
    print(f"  measured parameter is its transverse resistance T = h_2 rho_2 = "
          f"{T_ref:.1f} ohm m^2")
    print("\n  family with the same T (h_2 rho_2 held fixed):")
    print("      h_2 (m)   rho_2 (ohm m)   max |d rho_a|/rho_a   mean rho_a")
    for h2 in (1.0, 2.0, 4.0, 8.0, 16.0):
        rho2 = T_ref / h2
        curve = np.array([wenner_rhoa([100.0, rho2, 20.0], [5.0, h2], a)[0]
                          for a in spacings3])
        dev = np.max(np.abs(curve - ref_curve) / ref_curve)
        print(f"  {h2:10.1f} {rho2:15.1f} {dev * 100:19.3f}% {curve.mean():13.2f}")
    print("  the sounding is nearly unchanged across a factor 16 in thickness")
    print("  (and in resistivity): the data measure T = h_2 rho_2, not h_2.")
    print("\n  the OTHER equivalence: a thin CONDUCTIVE layer carries current")
    print("  along itself, so the measured parameter is its longitudinal")
    print("  conductance S = h_2/rho_2.  Same demonstration:")
    base_c = ([100.0, 5.0, 500.0], [5.0, 4.0])
    S_c = base_c[1][1] / base_c[0][1]
    ref_c = np.array([wenner_rhoa(base_c[0], base_c[1], a)[0]
                      for a in spacings3])
    print(f"  reference: rho_2 = {base_c[0][1]:.0f} ohm m, "
          f"h_2 = {base_c[1][1]:.1f} m, S = {S_c:.3f} S")
    print("      h_2 (m)   rho_2 (ohm m)   max |d rho_a|/rho_a")
    for h2 in (1.0, 2.0, 4.0, 8.0, 16.0):
        rho2 = h2 / S_c
        curve = np.array([wenner_rhoa([100.0, rho2, 500.0], [5.0, h2], a)[0]
                          for a in spacings3])
        dev = np.max(np.abs(curve - ref_c) / ref_c)
        print(f"  {h2:10.1f} {rho2:15.2f} {dev * 100:19.3f}%")
    print("  in both cases the information content of a sounding is a")
    print("  resistance or a conductance, not a thickness.")

    section("4. Equivalence against 2% noise: which models survive?")
    print(f"  the drawing above assumes perfect data.  With "
          f"{NOISE_FLOOR_REL * 100:.0f}% noise on dV:")
    print("      h_2 (m)   max |d rho_a|/rho_a   inside noise?   chi^2")
    ndata = spacings3.size
    for h2 in (1.0, 2.0, 4.0, 8.0, 16.0):
        rho2 = T_ref / h2
        curve = np.array([wenner_rhoa([100.0, rho2, 20.0], [5.0, h2], a)[0]
                          for a in spacings3])
        dev = np.abs(curve - ref_curve) / ref_curve
        chi2 = np.sum((dev / NOISE_FLOOR_REL) ** 2) / ndata
        verdict = "yes" if chi2 < 1.0 else ("marginal" if chi2 < 4.0 else "no")
        print(f"  {h2:10.1f} {dev.max() * 100:20.3f}%   {verdict:>13s} "
              f"{chi2:8.2f}")
    print("  chi^2 here is (model difference / assumed noise)^2 per datum: with")
    print("  2% noise the equivalent family is the set of models with chi^2 ~ 1.")
    print("  Reporting a single thickness from this data is a choice, not a")
    print("  measurement.")


if __name__ == "__main__":
    main()
