#!/usr/bin/env python3
"""Multispectral imaging, band ratios and indices, measured on synthetic scenes.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python multispectral_imaging_demo.py

Everything is SYNTHETIC.  The four "bands" are four reflectances assigned in this
file; the endmembers, the soil line, the noise levels and the LAI relation are
chosen teaching values, not measurements of any real material.

Contents
--------
1. A synthetic four-band scene built from four endmembers.
2. Band ratios cancel a multiplicative gain: measured.
3. An additive haze term does NOT cancel: the error versus target brightness.
4. A normalised difference index and its values for the endmembers.
5. Index saturation: NDVI versus a synthetic leaf area index.
6. The soil line and the perpendicular vegetation index.
7. Noise propagation into a band ratio, by Monte Carlo.
8. A two-band ratio index for a synthetic alteration abundance.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# SYNTHETIC endmember reflectances in four notional bands, in this file's order
# (blue, green, red, near-infrared).  Chosen teaching shapes only.
BANDS = ("blue", "green", "red", "near-infrared")
ENDMEMBERS = {
    "soil":    np.array([0.30, 0.34, 0.42, 0.45]),
    "vegetation": np.array([0.05, 0.08, 0.04, 0.48]),
    "water":   np.array([0.06, 0.05, 0.04, 0.02]),
    "bright":  np.array([0.45, 0.50, 0.55, 0.58]),
}
SOIL_LINE_SLOPE = 1.15      # NIR = slope x red + intercept for bare soil
SOIL_LINE_INTERCEPT = 0.06

NDVI_INF = 0.90             # synthetic asymptote of the NDVI-LAI relation
NDVI_SOIL = 0.10
K_EXT = 0.70                # synthetic extinction coefficient


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def ndvi(red, nir):
    """Normalised difference index (NIR - red) / (NIR + red)."""
    return (nir - red) / (nir + red)


def ratio_nd(a, b):
    """Normalised difference of two bands."""
    return (a - b) / (a + b)


def make_scene(n=200):
    """SYNTHETIC fractional-cover scene: four classes plus a brightness field."""
    abundance = np.zeros((n, n, len(ENDMEMBERS)))
    quarter = n // 2
    classes = [(slice(0, quarter), slice(0, quarter), 0),
               (slice(0, quarter), slice(quarter, n), 1),
               (slice(quarter, n), slice(0, quarter), 2),
               (slice(quarter, n), slice(quarter, n), 3)]
    for rs, cs, idx in classes:
        abundance[rs, cs, idx] = 1.0
    rho = np.tensordot(abundance, np.array(list(ENDMEMBERS.values())), axes=1)
    rho = rho + 0.01 * RNG.standard_normal(rho.shape)
    return np.clip(rho, 1e-4, 1.0)


def main():
    section("1. A SYNTHETIC four-band scene")
    scene = make_scene()
    print(f"  scene shape = {scene.shape} (rows, cols, bands), bands = {BANDS}")
    print("   endmember           " + "".join(f"{b:>16s}" for b in BANDS))
    for name, rho in ENDMEMBERS.items():
        print(f"  {name:18s} " + "".join(f"{v:16.3f}" for v in rho))
    print("  whole-scene band means: " + "".join(
        f"{scene[:, :, i].mean():.4f} " for i in range(4)))
    print("  (band order: " + ", ".join(BANDS) + ")")

    section("2. Band ratios cancel a multiplicative gain")
    g = 1.15
    print(f"  apply a uniform gain g = {g:.2f} to every band (sensor gain or a")
    print("  change in illumination) and recompute the indices.")
    print("   index definition                          original   after gain   difference")
    red = scene[:, :, 2]
    nir = scene[:, :, 3]
    cases = [
        ("NDVI  = (NIR - red)/(NIR + red)", ndvi(red, nir), ndvi(g * red, g * nir)),
        ("ratio = NIR / red", nir / red, (g * nir) / (g * red)),
        ("ND(blue,red) = (B - R)/(B + R)",
         ratio_nd(scene[:, :, 0], red), ratio_nd(g * scene[:, :, 0], g * red)),
    ]
    for name, before, after in cases:
        d = np.max(np.abs(after - before))
        print(f"  {name:40s} {np.mean(before):9.5f}   {np.mean(after):10.5f} "
              f"  {d:10.2e}")
    print("  Every difference is at the level of floating-point round-off: a")
    print("  ratio of two bands is invariant to any factor COMMON to both.")

    section("3. An additive haze term does not cancel")
    h = 0.02
    print(f"  add a constant path reflectance h = {h:.3f} to both bands")
    print("  (the additive atmospheric term, expressed in reflectance units).")
    print("   surface              true NDVI   NDVI with haze   error")
    for name, rho in ENDMEMBERS.items():
        true_i = ndvi(rho[2], rho[3])
        haze_i = ndvi(rho[2] + h, rho[3] + h)
        print(f"  {name:18s} {true_i:11.4f} {haze_i:16.4f} {haze_i - true_i:+8.4f}")
    print("  The error is largest for DARK targets: adding h to a small sum changes")
    print("  the ratio more.  This is why haze correction matters most over water")
    print("  and shadow, and why an index computed on raw digital numbers is not a")
    print("  surface property.")

    section("4. Normalised difference indices for the endmembers")
    print("   endmember          NDVI     ND(blue,red)   NIR/red ratio")
    for name, rho in ENDMEMBERS.items():
        print(f"  {name:18s} {ndvi(rho[2], rho[3]):8.3f} "
              f"{ratio_nd(rho[0], rho[2]):14.3f} {rho[3] / rho[2]:15.3f}")
    print("  A single index separates vegetation from the rest here, but note that")
    print("  the ratio NIR/red is unbounded as red -> 0 and is therefore unstable for")
    print("  dark targets, while the normalised difference stays in [-1, +1].")

    section("5. Index saturation against a synthetic leaf area index")
    print(f"  SYNTHETIC relation: NDVI(LAI) = {NDVI_INF:.2f} - "
          f"({NDVI_INF:.2f} - {NDVI_SOIL:.2f}) exp(-{K_EXT:.2f} LAI)")
    print("   LAI     NDVI      dNDVI/dLAI   LAI implied by NDVI +/- 0.02")
    for lai in (0.25, 0.5, 1.0, 2.0, 4.0, 6.0, 8.0):
        v = NDVI_INF - (NDVI_INF - NDVI_SOIL) * np.exp(-K_EXT * lai)
        dv = K_EXT * (NDVI_INF - NDVI_SOIL) * np.exp(-K_EXT * lai)
        lo = -np.log((NDVI_INF - (v - 0.02)) / (NDVI_INF - NDVI_SOIL)) / K_EXT
        if v + 0.02 >= NDVI_INF:
            print(f"  {lai:5.2f}   {v:7.4f}   {dv:11.4f}   {lo:8.2f} to "
                  "UNBOUNDED (index saturates)")
        else:
            hi = -np.log((NDVI_INF - (v + 0.02)) / (NDVI_INF - NDVI_SOIL)) / K_EXT
            print(f"  {lai:5.2f}   {v:7.4f}   {dv:11.4f}   {lo:8.2f} to {hi:6.2f}"
                  f"  (width {hi - lo:5.2f})")
    print("  The sensitivity dNDVI/dLAI falls by an order of magnitude between")
    print("  LAI = 1 and LAI = 8, and beyond LAI ~ 5 the upper bound becomes")
    print("  unbounded: the index cannot distinguish LAI = 6 from LAI = 8 at all,")
    print("  so the retrieval there reports the prior, not the measurement.")

    section("6. The soil line and the perpendicular vegetation index")
    print(f"  SYNTHETIC bare-soil line: NIR = {SOIL_LINE_SLOPE:.2f} red + "
          f"{SOIL_LINE_INTERCEPT:.2f}, traversed by varying soil brightness")
    norm = np.sqrt(1.0 + SOIL_LINE_SLOPE ** 2)
    print("   red    NIR      NDVI      PVI      PVI of a vegetation pixel")
    red_veg, nir_veg = 0.040, 0.480
    pvi_veg = (nir_veg - SOIL_LINE_SLOPE * red_veg - SOIL_LINE_INTERCEPT) / norm
    for red_s in (0.12, 0.16, 0.20, 0.24, 0.28):
        nir_s = SOIL_LINE_SLOPE * red_s + SOIL_LINE_INTERCEPT
        pvi = (nir_s - SOIL_LINE_SLOPE * red_s - SOIL_LINE_INTERCEPT) / norm
        print(f"  {red_s:5.2f}  {nir_s:6.3f}   {ndvi(red_s, nir_s):7.4f}   "
              f"{pvi:+7.4f}   {pvi_veg:+7.4f}")
    print("  Along the soil line NDVI moves from 0.245 to 0.154 -- a spread of 0.09,")
    print("  comparable to a real vegetation signal -- while the perpendicular")
    print("  distance PVI is identically zero.  A distance measured PERPENDICULAR to")
    print("  the soil line removes the soil-brightness confound that a ratio index")
    print("  mistakes for vegetation, and it separates the vegetation pixel, whose")
    print(f"  PVI is {pvi_veg:+.4f}, from every soil pixel.")
    L_tune = 2.0 * SOIL_LINE_INTERCEPT / (SOIL_LINE_SLOPE - 1.0)
    print(f"\n  The same confound can be removed with a SOIL-ADJUSTED index")
    print(f"  I_adj = (1+L)(NIR - red)/(NIR + red + L).  Differentiating along the")
    print(f"  soil line gives dI_adj/dred = (1+L)[(a-1)L - 2b]/((a+1)red + b + L)^2,")
    print(f"  which vanishes identically when L = 2b/(a-1) = {L_tune:.4f} here.")
    print("   red    plain (scaled) index   soil-adjusted index")
    for red_s in (0.12, 0.16, 0.20, 0.24, 0.28):
        nir_s = SOIL_LINE_SLOPE * red_s + SOIL_LINE_INTERCEPT
        plain = (nir_s - red_s) / (nir_s + red_s)
        adj = (1 + L_tune) * (nir_s - red_s) / (nir_s + red_s + L_tune)
        print(f"  {red_s:5.2f}   {plain:20.4f}   {adj:19.4f}")
    print("  The adjusted index is constant along the whole soil line, so its value")
    print("  carries no soil-brightness information at all in this model.  The")
    print("  invariance is EXACT for a linear soil line and conditional on the")
    print("  fitted slope and intercept; with a wrong soil line it degrades smoothly")

    section("7. Noise propagation into an index (Monte Carlo)")
    n = 200000
    sigma = 0.010
    red_v, nir_v = 0.04, 0.48
    r = red_v + sigma * RNG.standard_normal(n)
    nir_n = nir_v + sigma * RNG.standard_normal(n)
    idx = ndvi(r, nir_n)
    true_i = ndvi(red_v, nir_v)
    d_red = -2.0 * nir_v / (nir_v + red_v) ** 2
    d_nir = 2.0 * red_v / (nir_v + red_v) ** 2
    pred = sigma * np.sqrt(d_red ** 2 + d_nir ** 2)
    print(f"  vegetation-like spectrum: red = {red_v:.2f}, NIR = {nir_v:.2f}, "
          f"band noise sigma = {sigma:.3f}")
    print(f"  {n} draws: NDVI = {idx.mean():.5f} +/- {idx.std(ddof=1):.5f} "
          f"(1 sigma), true value {true_i:.5f}")
    print(f"  first-order prediction: dNDVI/dred = {d_red:.4f}, "
          f"dNDVI/dNIR = {d_nir:.4f}")
    print(f"  sigma_NDVI predicted = {pred:.5f} (Monte Carlo {idx.std(ddof=1):.5f})")
    print("  An index built from two bands carries BOTH bands' noise, and the")
    print("  sensitivity to the DARK band is the larger of the two.  A band ratio is")
    print("  not a noise-reduction device.")

    section("8. A two-band ratio for a synthetic alteration abundance")
    print("  SYNTHETIC band ratio R = band2/band1, with a monotone mapping to a")
    print("  notional alteration abundance A: R = 1 + 0.8 A/(A + 1.5)")
    print("   abundance A   band1   band2   ratio R   dR/dA")
    for A in (0.0, 0.25, 0.5, 1.0, 2.0, 4.0):
        Rb = 1.0 + 0.8 * A / (A + 1.5)
        dR = 0.8 * 1.5 / (A + 1.5) ** 2
        b1 = 0.30 / (1.0 + 0.1 * A)
        b2 = b1 * Rb
        print(f"  {A:11.2f}   {b1:6.3f}  {b2:6.3f}   {Rb:7.4f}   {dR:9.4f}")
    print("  The ratio increases monotonically with abundance but its SENSITIVITY")
    print("  falls off as A grows: the same mapping problem as the saturation in")
    print("  section 5.  A ratio index is a monotone but non-linear, saturating")
    print("  function of the quantity of interest.")


if __name__ == "__main__":
    main()
