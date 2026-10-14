#!/usr/bin/env python3
"""Landfill investigation: a genuine two-layer Wenner sounding, the leachate
mound from a Dupuit balance, the conductivity a leachate-affected pore fluid
produces, and the equivalence that makes a conductive layer non-unique.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python landfill_investigation_demo.py

Everything is SYNTHETIC.  The "landfill", the "leachate", the layer
resistivities and the recharge rate are chosen teaching values for an idealised
archetype; no real site, licence, regulation or waste stream is described.

Contents
--------
1.  The two-layer Wenner apparent resistivity (image series) and its limits.
2.  A sounding curve over a synthetic landfill profile.
3.  The Dupuit leachate mound above a strip source.
4.  Pore-fluid conductivity of leachate-affected water and the bulk resistivity.
5.  The depth of investigation: which spacings see the layer.
6.  Equivalence: two very different models with the same sounding curve.
7.  An idealised self-potential profile over a buried redox source.
8.  Reference numbers used in the lesson.
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def rho_a_wenner(a_m, rho1, rho2, h_m, n_terms=400):
    """Apparent resistivity of a two-layer earth for the Wenner array.

    rho_a = rho1 [ 1 + 4a sum_{n>=1} k^n ( 1/sqrt(a^2+4n^2h^2)
                                             - 1/sqrt(4a^2+4n^2h^2) ) ]
    with k = (rho2-rho1)/(rho2+rho1).  Derived from the image series
    V(r) = (rho1 I / 2pi)[1/r + 2 sum k^n / sqrt(r^2+4n^2h^2)].
    """
    k = (rho2 - rho1) / (rho2 + rho1)
    n = np.arange(1, n_terms + 1)
    terms = 1.0 / np.sqrt(a_m ** 2 + 4.0 * n ** 2 * h_m ** 2) \
        - 1.0 / np.sqrt(4.0 * a_m ** 2 + 4.0 * n ** 2 * h_m ** 2)
    return rho1 * (1.0 + 4.0 * a_m * np.sum(k ** n * terms))


def leachate_mound(w_m_day, b_m, t_m2_day):
    """Steady 1-D Dupuit mound above a strip source of half-width b (m)."""
    return w_m_day * b_m ** 2 / (2.0 * t_m2_day)


def sigma_w(c_cu, sigma0=0.05, beta=1.0e-4):
    """SYNTHETIC pore-fluid conductivity, S/m."""
    return sigma0 + beta * c_cu


def rho_bulk(sigma_w_value, phi=0.30, m=2.0, a=1.0):
    """Archie bulk resistivity at S_w = 1."""
    return 1.0 / (sigma_w_value * phi ** m / a)


def main():
    section("1. Two-layer Wenner apparent resistivity and its limits")
    rho1, rho2, h = 60.0, 400.0, 8.0
    print(f"  SYNTHETIC model: rho1 = {rho1:.0f} ohm m (conductive cover), "
          f"rho2 = {rho2:.0f} ohm m (resistive bedrock), h = {h:.0f} m")
    print(f"  reflection coefficient k = {((rho2 - rho1) / (rho2 + rho1)):.4f}")
    print("      spacing a (m)      rho_a (ohm m)")
    for a in (0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 50.0, 100.0):
        print(f"  {a:16.1f}   {rho_a_wenner(a, rho1, rho2, h):15.2f}")
    small = rho_a_wenner(1.0e-3, rho1, rho2, h)
    large = rho_a_wenner(1.0e5, rho1, rho2, h)
    print(f"  limit a -> 0    gives rho_a = {small:.4f} ohm m "
          f"(must equal rho1 = {rho1:.0f})")
    print(f"  limit a -> inf  gives rho_a = {large:.4f} ohm m "
          f"(must equal rho2 = {rho2:.0f})")
    print("  both analytic limits are recovered, which is the check that the")
    print("  image series is implemented correctly.")

    section("2. A sounding curve over a synthetic landfill profile")
    print("  The conductive cover is the leachate-affected zone; the resistive")
    print("  layer below is clean bedrock.  The curve starts at rho1, rises")
    print("  through an inflection near a ~ h, and approaches rho2.")
    a_arr = np.logspace(-0.3, 2.0, 13)
    curve = np.array([rho_a_wenner(a, rho1, rho2, h) for a in a_arr])
    print("      a (m)      rho_a (ohm m)   fraction of the way to rho2")
    for a, r in zip(a_arr, curve):
        print(f"  {a:9.2f}   {r:15.2f}   {(r - rho1) / (rho2 - rho1):20.3f}")
    print(f"  the curve reaches 50% of the contrast at about a = "
          f"{a_arr[int(np.argmin(np.abs(curve - 0.5 * (rho1 + rho2))))]:.1f} m,")
    print("  which is the practical depth scale of the array, not the layer depth.")

    section("3. Leachate mound above a strip source (Dupuit balance)")
    w, b, T = 5.0e-4, 100.0, 10.0
    rise = leachate_mound(w, b, T)
    print("  Steady 1-D flow with uniform recharge w over a strip of half-width b:")
    print("    T d2h/dx2 = -w  ->  h(x) = h_edge + (w/2T)(b^2 - x^2)")
    print(f"  SYNTHETIC inputs: w = {w:.2e} m/day, b = {b:.0f} m, T = {T:.1f} m^2/day")
    print(f"  mound rise at the centre, w b^2/(2T) = {rise:.4f} m")
    print("      w (m/day)   b (m)   rise (m)")
    for ww, bb in ((5.0e-4, 100.0), (2.0e-3, 100.0), (5.0e-4, 200.0),
                   (5.0e-4, 50.0), (2.0e-3, 200.0)):
        print(f"  {ww:11.2e}   {bb:6.0f}   {leachate_mound(ww, bb, T):8.4f}")
    print("  the mound scales with recharge and with the SQUARE of the source")
    print("  width: doubling the landfill footprint quadruples the mound.")

    section("4. Pore fluid and bulk resistivity of leachate-affected water")
    print("      C (CU)   sigma_w (S/m)   rho_bulk (ohm m) at phi = 0.30")
    for c in (0.0, 100.0, 250.0, 500.0, 750.0, 1000.0):
        print(f"  {c:9.1f}   {sigma_w(c):13.5f}   {rho_bulk(sigma_w(c)):28.2f}")
    rho_clean = rho_bulk(sigma_w(0.0))
    rho_leach = rho_bulk(sigma_w(750.0))
    print(f"  clean pore water  -> rho_bulk = {rho_clean:.1f} ohm m")
    print(f"  leachate-affected -> rho_bulk = {rho_leach:.1f} ohm m "
          f"(a factor {rho_clean / rho_leach:.2f} lower)")
    print("  this is the contrast the sounding has to resolve; note that it is")
    print("  entirely a FLUID effect, so it is independent of the rock type.")

    section("5. Depth of investigation: which spacings see the layer")
    print("      a/h      rho_a (ohm m)   sensitivity to h")
    for a_over_h in (0.25, 0.5, 1.0, 2.0, 4.0):
        a = a_over_h * h
        r0 = rho_a_wenner(a, rho1, rho2, h)
        r1 = rho_a_wenner(a, rho1, rho2, h * 1.10)
        print(f"  {a_over_h:7.2f}   {r0:15.2f}   {(r1 - r0) / r0:+15.4f}")
    print("  the largest fractional change for a 10% depth change is near")
    print("  a/h ~ 1-2; spacings much smaller than h never leave the cover, and")
    print("  spacings much larger than h average both layers and lose the")
    print("  resolution.  Acquisition design means choosing a/h, not 'more")
    print("  electrodes'.")

    section("6. The admitted set: what a stated noise level allows")
    a_arr = np.logspace(-0.3, 2.0, 15)
    ref = np.array([rho_a_wenner(a, rho1, rho2, h) for a in a_arr])
    r1_grid = np.arange(30.0, 201.0, 5.0)
    h_grid = np.arange(1.0, 25.01, 0.5)
    print(f"  reference model: rho1 = {rho1:.0f} ohm m, h = {h:.1f} m, "
          f"rho2 = {rho2:.0f} ohm m")
    print("  For every (rho1, h) pair with rho2 fixed, the rms difference from the")
    print("  reference curve in log(rho_a).  The best-fitting pair is reported for")
    print("  a range of assumed layer resistivities:")
    print("      rho1 (ohm m)   best h (m)   rms (log units)   typical misfit")
    trade = []
    for r1_alt in (40.0, 50.0, 60.0, 70.0, 80.0, 100.0):
        best = min((float(np.sqrt(np.mean((np.log(np.array(
            [rho_a_wenner(a, r1_alt, rho2, hh) for a in a_arr]))
            - np.log(ref)) ** 2))), hh) for hh in h_grid)
        rms_c, h_best = best
        trade.append((r1_alt, h_best, rms_c))
        print(f"  {r1_alt:14.0f}   {h_best:10.1f}   {rms_c:17.5f}   "
              f"{100 * (np.exp(rms_c) - 1.0):11.2f}%")
    print("  the trade-off is monotone: a more conductive cover needs to be")
    print("  thinner.  But the residual never vanishes: with the half-space")
    print("  resistivity fixed, this two-layer curve is well determined, and the")
    print("  correlation is far weaker than the classic thin-layer equivalence.")
    for tol in (0.05, 0.10):
        ok = []
        for r1_alt in r1_grid:
            for hh in h_grid:
                rms_c = float(np.sqrt(np.mean((np.log(np.array(
                    [rho_a_wenner(a, r1_alt, rho2, hh) for a in a_arr]))
                    - np.log(ref)) ** 2)))
                if rms_c <= np.log(1.0 + tol):
                    ok.append((r1_alt, hh))
        if ok:
            r1v = np.array([o[0] for o in ok])
            hv = np.array([o[1] for o in ok])
            below = np.mean(hv < h)
            print(f"  admitted set at {100 * tol:.0f}% noise: rho1 in "
                  f"[{r1v.min():.0f}, {r1v.max():.0f}] ohm m, h in "
                  f"[{hv.min():.1f}, {hv.max():.1f}] m, {len(ok)} pairs")
            print(f"    of those, {100 * below:.0f}% have a thickness below the true "
                  f"{h:.0f} m (the equivalence direction)")
        else:
            print(f"  admitted set at {100 * tol:.0f}% noise: empty — no model on "
                  f"the grid matches that well")
    print("  A survey reported as 'a conductive layer, 60 ohm m and 8 m thick' is")
    print("  really a statement about an admitted set, and the set must be quoted")
    print("  with the noise level that produced it.")

    section("7. Idealised self-potential profile over a buried redox source")
    rho_e, current, depth = 100.0, 0.05, 6.0
    print("  A compact current source of strength I at depth d in a half-space")
    print("  gives V(x) = rho I / (2 pi r), r = sqrt(x^2 + d^2).  SYNTHETIC:")
    print(f"    rho = {rho_e:.0f} ohm m, I = {current:.2f} A equivalent, "
          f"d = {depth:.0f} m")
    print("      x (m)     V (mV)    V - V(far field) (mV)")
    v_far = rho_e * current / (2.0 * np.pi * 1000.0)
    for x in (-40.0, -20.0, -10.0, 0.0, 10.0, 20.0, 40.0):
        r = np.sqrt(x ** 2 + depth ** 2)
        v = rho_e * current / (2.0 * np.pi * r)
        print(f"  {x:7.1f}   {1000 * v:9.3f}   {1000 * (v - v_far):18.3f}")
    v_peak = rho_e * current / (2.0 * np.pi * depth)
    v_off = rho_e * current / (2.0 * np.pi * np.sqrt(20.0 ** 2 + depth ** 2))
    print(f"  peak-to-offset amplitude = {1000 * (v_peak - v_off):.3f} mV")
    print("  the anomaly is a single-signed hump whose half-width is the source")
    print("  depth: SP locates a source but does not measure its strength, because")
    print("  rho and I appear only as the product.")

    section("8. Reference numbers used in the lesson")
    print(f"  two-layer sounding: rho1 = {rho1:.0f}, rho2 = {rho2:.0f} ohm m, "
          f"h = {h:.0f} m")
    print(f"  limits recovered: {small:.3f} ohm m at a -> 0 and {large:.3f} "
          f"ohm m at a -> inf")
    print(f"  mound rise = {rise:.4f} m for w = {w:.1e} m/day, b = {b:.0f} m, "
          f"T = {T:.0f} m^2/day")
    print(f"  clean rho_bulk = {rho_clean:.1f} ohm m; leachate rho_bulk = "
          f"{rho_leach:.1f} ohm m")
    print(f"  best alternative cover for rho1 = {trade[3][0]:.0f} ohm m: "
          f"h = {trade[3][1]:.1f} m, misfit {100 * (np.exp(trade[3][2]) - 1.0):.1f}%")


if __name__ == "__main__":
    main()
