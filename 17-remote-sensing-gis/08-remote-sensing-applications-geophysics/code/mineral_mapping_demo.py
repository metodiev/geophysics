#!/usr/bin/env python3
"""Mineral and alteration mapping from space: synthetic reflectance spectra,
absorption-band depth, the degeneracy of a spectral index, and linear unmixing.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python mineral_mapping_demo.py

Everything here is SYNTHETIC.  The endmembers, absorption centres and depths,
grain-size model and scene are chosen teaching values, not measured spectra or a
real site.  Absorption positions are stated in micrometres only to give the
arithmetic a labelled axis.  No file is read or written and no network access is
used.

Contents
--------
1. A synthetic endmember library with two narrow absorptions.
2. A synthetic scene of linear mixtures, and an absorption-band-depth index.
3. Degeneracy: the same index from different abundance / grain-size pairs.
4. Linear unmixing, retrieval error, and the condition number of similar
   endmembers.
5. What an unmodelled illumination change does to the index.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

WL = np.linspace(0.40, 2.50, 421)          # wavelength axis, micrometres
CLAY_C, CLAY_D, CLAY_W = 2.20, 0.30, 0.060  # absorption centre, depth, width
CARB_C, CARB_D, CARB_W = 2.33, 0.25, 0.050
BASE_CLAY, BASE_CARB, BASE_UNALT = 0.50, 0.55, 0.48


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def gauss_abs(centre, depth, width, base):
    """Reflectance with a Gaussian absorption: R = base (1 - d exp(-((wl-c)/w)^2))."""
    return base * (1.0 - depth * np.exp(-((WL - centre) / width) ** 2))


def clay_spec(grain=1.0):
    """Clay-like endmember; a finer grain deepens the absorption (Beer-Lambert)."""
    return gauss_abs(CLAY_C, min(0.90, CLAY_D * grain), CLAY_W, BASE_CLAY)


def carb_spec():
    return gauss_abs(CARB_C, CARB_D, CARB_W, BASE_CARB)


def unalt_spec():
    return BASE_UNALT + 0.02 * (WL - 0.40) / 2.10


def mixture(a_clay, a_carb, grain=1.0):
    a_un = 1.0 - a_clay - a_carb
    return a_clay * clay_spec(grain) + a_carb * carb_spec() + a_un * unalt_spec()


def band_depth(spec, centre=CLAY_C, s0=CLAY_C - 0.10, s1=CLAY_C + 0.20):
    """Continuum-removed depth of the absorption at `centre` (dimensionless)."""
    i0, i1, ic = (np.argmin(np.abs(WL - s0)), np.argmin(np.abs(WL - s1)),
                  np.argmin(np.abs(WL - centre)))
    r0, r1, rc = spec[i0], spec[i1], spec[ic]
    cont = r0 + (r1 - r0) * (WL[ic] - s0) / (s1 - s0)
    return 1.0 - rc / cont


def solve_grain(a_clay, target, lo=0.30, hi=3.0):
    """Bisect the grain factor that reproduces `target` band depth at this abundance."""
    f = lambda g: band_depth(mixture(a_clay, 0.0, g)) - target
    flo, fhi = f(lo), f(hi)
    if flo * fhi > 0:
        return None
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        fm = f(mid)
        if flo * fm <= 0:
            hi, fhi = mid, fm
        else:
            lo, flo = mid, fm
    return 0.5 * (lo + hi)


def main():
    section("1. A synthetic endmember library (SYNTHETIC)")
    print(f"wavelength axis = {WL[0]:.2f} to {WL[-1]:.2f} um, {WL.size} channels")
    print(f"clay-like endmember     : centre {CLAY_C:.2f} um, depth {CLAY_D:.2f},"
          f" width {CLAY_W:.3f} um")
    print(f"carbonate-like endmember: centre {CARB_C:.2f} um, depth {CARB_D:.2f},"
          f" width {CARB_W:.3f} um")
    print(f"unaltered endmember     : near-flat continuum, base {BASE_UNALT:.2f}")
    print("A mineral is identified by WHERE it absorbs; how much it absorbs")
    print("depends on abundance, grain size and coating as well.")

    section("2. A synthetic scene and a band-depth index (SYNTHETIC)")
    n = 400
    a_clay = RNG.uniform(0.0, 0.6, n)
    a_carb = RNG.uniform(0.0, 0.3, n)
    a_carb = np.minimum(a_carb, 1.0 - a_clay)
    idx = np.array([band_depth(mixture(ac, ak)) for ac, ak in zip(a_clay, a_carb)])
    r = float(np.corrcoef(a_clay, idx)[0, 1])
    print(f"{n} synthetic pixels, clay abundance 0.00-0.60, carbonate 0.00-0.30")
    print(f"correlation of the band depth with clay abundance, r = {r:.3f}")
    resid = idx - np.polyval(np.polyfit(a_clay, idx, 1), a_clay)
    print(f"residual scatter of the index about that line, sd = {resid.std():.4f}")
    print("The index tracks abundance on average, but a single pixel's index is")
    print("not its abundance: carbonate at the other centre moves it too.")

    section("3. Degeneracy: one index, many (abundance, grain size) pairs")
    target = band_depth(mixture(0.25, 0.0, 1.0))
    print(f"reference: clay abundance 0.25, grain factor 1.00 -> depth "
          f"{target:.4f}")
    print("  clay abundance   grain factor   depth achieved")
    for a in (0.15, 0.18, 0.25, 0.35, 0.50):
        g = solve_grain(a, target)
        if g is None:
            print(f"  {a:14.2f}   (no grain factor matches)")
            continue
        print(f"  {a:14.2f}   {g:12.2f}   {band_depth(mixture(a, 0.0, g)):.4f}")
    print("A finer grain deepens the absorption, so a weakly abundant but very")
    print("fine material mimics a more abundant coarse one. The index alone")
    print("cannot separate them; that is the non-uniqueness of the method.")

    section("4. Linear unmixing and the condition number (SYNTHETIC)")
    E_well = np.column_stack([clay_spec(), carb_spec(), unalt_spec()])
    E_ill = np.column_stack([clay_spec(),
                             gauss_abs(2.22, 0.28, 0.055, 0.50), unalt_spec()])
    print(f"well-separated library (centres 2.20, 2.33 um): "
          f"condition number = {np.linalg.cond(E_well):.1f}")
    print(f"nearly collinear library (centres 2.20, 2.22 um): "
          f"condition number = {np.linalg.cond(E_ill):.1f}")
    n = 200
    a1 = RNG.uniform(0.0, 0.5, n)
    a2 = RNG.uniform(0.0, 0.3, n)
    ab_true = np.column_stack([a1, a2, 1.0 - a1 - a2])
    print("  library            cond    RMSE comp 1   RMSE comp 2")
    for name, E in (("well-separated", E_well), ("collinear", E_ill)):
        scene = ab_true @ E.T + RNG.normal(0.0, 0.005, (n, WL.size))
        ab_hat = np.linalg.lstsq(E, scene.T, rcond=None)[0].T
        rmse = np.sqrt(np.mean((ab_hat - ab_true) ** 2, axis=0))
        print(f"  {name:15s}  {np.linalg.cond(E):8.1f}   {rmse[0]:11.4f}   "
              f"{rmse[1]:11.4f}")
    print("Two endmembers close in wavelength are nearly the same column, so the")
    print("system is badly conditioned and a small spectral error becomes a large")
    print("abundance error. A mineral map is only as separable as its library.")

    section("5. A curved spectral error biases the index (SYNTHETIC)")
    spec = mixture(0.30, 0.05, 1.0)
    d0 = band_depth(spec)
    span = WL[-1] - WL[0]
    print(f"true depth of the mixture = {d0:.4f}")
    print("a LINEAR multiplicative error (a sloping continuum):")
    for slope in (0.0, 0.10, 0.20):
        d1 = band_depth(spec * (1.0 + slope * (WL - WL[0]) / span))
        print(f"  slope {slope:.2f} -> depth {d1:.4f}, bias {d1 - d0:+.4f}")
    print("a CURVED multiplicative error (a spectrally varying aerosol term):")
    for amp in (0.0, 0.05, 0.10, 0.20):
        d1 = band_depth(spec * (1.0 + amp * np.exp(-((WL - CLAY_C) / 0.12) ** 2)))
        print(f"  amplitude {amp:.2f} -> depth {d1:.4f}, bias {d1 - d0:+.4f}")
    print("A band depth is a ratio to a LINEAR continuum, so a linear error")
    print("cancels exactly and is invisible. A CURVED spectral error does not")
    print("cancel, and mimics a real absorption change; separating the two needs")
    print("a radiative-transfer correction and a careful continuum choice.")


if __name__ == "__main__":
    main()
