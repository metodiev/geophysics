#!/usr/bin/env python3
"""Vegetation indices, geobotany and mineral alteration mapping (synthetic).

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python vegetation_geobotany_demo.py

Everything is SYNTHETIC.  The vegetation relation, the mineral spectra, the
absorption features, the abundance fields and the stress relations are chosen
teaching values in this file.  No real material, mineral, plant, deposit, sensor
or product is represented.

Contents
--------
1. NDVI against a synthetic leaf area index, with and without a soil background.
2. Soil adjustment: SAVI and EVI against the same target.
3. Continuum removal by an upper convex hull, and the band depth it defines.
4. Endpoint dependence: the same feature measured with a different continuum.
5. Band-depth ratio against a single band depth under brightness and slope changes.
6. A synthetic alteration scene: a depth map and a ratio map, with false alarms.
7. Geobotany: a vegetation-stress index confounded by a moisture gradient.
8. Verification: the continuum-removed spectrum is 1 at its endpoints and <= 1 inside.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC vegetation relation -------------------------------------------
NDVI_INF = 0.90
NDVI_SOIL = 0.10
K_EXT = 0.70
SOIL_LINE_SLOPE = 1.15
SOIL_LINE_INTERCEPT = 0.06

# --- SYNTHETIC spectrum model, 2.00-2.50 um ----------------------------------
LAM = np.linspace(2.00, 2.50, 251)
FEATURE_A = 2.20          # um, "clay-like" absorption
FEATURE_B = 2.33          # um, "carbonate-like" absorption
WIDTH = 0.02              # um
AMP_A = 0.030             # reference amplitude of the 2.20 um feature
AMP_B = 0.006             # reference amplitude of the 2.33 um feature

N = 120


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def upper_hull(x, y):
    """Indices of the upper convex hull of the points (x, y), x increasing."""
    pts = sorted(range(len(x)), key=lambda i: x[i])
    hull = []
    for i in pts:
        while len(hull) >= 2:
            j, k = hull[-2], hull[-1]
            cross = (x[k] - x[j]) * (y[i] - y[j]) - (y[k] - y[j]) * (x[i] - x[j])
            if cross >= 0:
                hull.pop()
            else:
                break
        hull.append(i)
    return hull


def continuum_removed(lam, rho):
    """Divide a spectrum by its upper convex hull (continuum removal)."""
    hull = upper_hull(lam, rho)
    cont = np.interp(lam, lam[hull], rho[hull])
    return rho / cont, cont, hull


def curved_soil(lam, brightness=1.0, redness=0.0, amp_a=AMP_A, amp_b=0.0):
    """SYNTHETIC curved soil continuum with two optional Gaussian absorptions.

    The base carries a quadratic term, so continua built between different
    endpoint pairs are genuinely different lines -- which is what makes endpoint
    dependence and continuum-slope bias measurable rather than asserted.
    """
    u = (lam - 2.00) / 0.50
    r = brightness * (0.18 + 0.30 * u) + redness * u ** 2
    r = r - amp_a * np.exp(-((lam - FEATURE_A) / WIDTH) ** 2)
    r = r - amp_b * np.exp(-((lam - FEATURE_B) / WIDTH) ** 2)
    return r


def band_depth(lam, rho, centre, lo, hi):
    """Depth of a feature at 'centre' above a straight-line continuum lo-hi."""
    r_lo = float(np.interp(lo, lam, rho))
    r_hi = float(np.interp(hi, lam, rho))
    cont = r_lo + (r_hi - r_lo) * (centre - lo) / (hi - lo)
    r_c = float(np.interp(centre, lam, rho))
    return 1.0 - r_c / cont


def analytic_depths(brightness, redness, amp_a, amp_b,
                    end_a=(2.10, 2.40), end_b=(2.25, 2.45)):
    """The same depths as band_depth, evaluated analytically from the model."""
    def r(lam):
        return float(curved_soil(np.array([lam]), brightness, redness, amp_a, amp_b)[0])
    lo, hi = end_a
    cont_a = r(lo) + (r(hi) - r(lo)) * (FEATURE_A - lo) / (hi - lo)
    d_a = 1.0 - r(FEATURE_A) / cont_a
    lo, hi = end_b
    cont_b = r(lo) + (r(hi) - r(lo)) * (FEATURE_B - lo) / (hi - lo)
    d_b = 1.0 - r(FEATURE_B) / cont_b
    return d_a, d_b


def main():
    section("1. NDVI against a synthetic leaf area index")
    print(f"  SYNTHETIC relation: NDVI(LAI) = {NDVI_INF:.2f} - "
          f"({NDVI_INF:.2f} - {NDVI_SOIL:.2f}) exp(-{K_EXT:.2f} LAI)")
    print("   LAI    NDVI (pure)   NDVI (30% soil)   dNDVI/dLAI   LAI from NDVI +/-0.02")
    soil_red, soil_nir = 0.30, 0.40
    for lai in (0.5, 1.0, 2.0, 4.0, 6.0, 8.0):
        v = NDVI_INF - (NDVI_INF - NDVI_SOIL) * np.exp(-K_EXT * lai)
        dv = K_EXT * (NDVI_INF - NDVI_SOIL) * np.exp(-K_EXT * lai)
        canopy = 1.0 - np.exp(-K_EXT * lai)
        red = 0.10 * (1.0 - 0.8 * canopy)
        nir = red + v * (red + 0.45 * canopy + 0.08)
        fs = 0.30
        mix_red = (1 - fs) * red + fs * soil_red
        mix_nir = (1 - fs) * nir + fs * soil_nir
        vs = (mix_nir - mix_red) / (mix_nir + mix_red)
        lin_mix = (1 - fs) * v + fs * NDVI_SOIL
        if lai == 4.0:
            print(f"  (reflectance mixture at LAI 4: red {mix_red:.4f}, NIR "
                  f"{mix_nir:.4f} -> NDVI {vs:.4f};")
            print(f"   the linear INDEX mixture gives {lin_mix:.4f}, a difference of "
                  f"{vs - lin_mix:+.4f})")
        lo = -np.log(max(NDVI_INF - (v - 0.02), 1e-9) / (NDVI_INF - NDVI_SOIL)) / K_EXT
        if v + 0.02 >= NDVI_INF:
            hi_txt = "unbounded"
        else:
            hi = -np.log((NDVI_INF - (v + 0.02)) / (NDVI_INF - NDVI_SOIL)) / K_EXT
            hi_txt = f"{hi:.2f}"
        print(f"  {lai:5.1f}   {v:11.4f}   {vs:16.4f}   {dv:11.4f}   "
              f"{lo:.2f} to {hi_txt}")
    print("  Two effects at once: SATURATION (dNDVI/dLAI falls an order of magnitude")
    print("  between LAI 1 and 8, so the upper limit becomes unbounded) and the SOIL")
    print("  BACKGROUND (a 30% soil fraction depresses the index, mimicking a thinner")
    print("  canopy).  Both must be stated; neither is a defect of the index.")

    section("2. Soil adjustment: SAVI and EVI")
    L_savi = 0.5
    print(f"  SAVI = (1+L)(NIR-red)/(NIR+red+L) with L = {L_savi:.1f}")
    print("  EVI  = 2.5 (NIR-red)/(NIR + 6 red + 1)   [coefficients chosen here]")
    print("   LAI    red    NIR    NDVI     SAVI     EVI")
    for lai in (0.5, 1.0, 2.0, 4.0, 6.0):
        v = NDVI_INF - (NDVI_INF - NDVI_SOIL) * np.exp(-K_EXT * lai)
        canopy = 1.0 - np.exp(-K_EXT * lai)
        red = 0.10 * (1.0 - 0.8 * canopy)
        nir = red + v * (red + 0.45 * canopy + 0.08)
        nd = (nir - red) / (nir + red)
        savi = (1 + L_savi) * (nir - red) / (nir + red + L_savi)
        evi = 2.5 * (nir - red) / (nir + 6.0 * red + 1.0)
        print(f"  {lai:5.1f}   {red:5.3f}  {nir:5.3f}  {nd:6.3f}   {savi:6.3f}   {evi:6.3f}")
    print("  The soil-adjustment parameter that makes an index invariant to soil")
    print("  brightness along a linear soil line is L = 2b/(a-1) = "
          f"{2 * SOIL_LINE_INTERCEPT / (SOIL_LINE_SLOPE - 1):.4f} for this synthetic")
    print("  soil line (derived in 17-02-01); 0.5 here is a compromise, so SAVI only")
    print("  partly removes the background.  Every index is a chosen projection with a")
    print("  residual confound, and the residual is the thing to report.")

    section("3. Continuum removal by an upper convex hull")
    rho = curved_soil(LAM, brightness=1.0, redness=0.0, amp_a=AMP_A, amp_b=0.0)
    cr, cont, hull = continuum_removed(LAM, rho)
    print("  SYNTHETIC spectrum 2.00-2.50 um: quadratic continuum plus a Gaussian")
    print(f"  absorption of amplitude {AMP_A:.3f} at {FEATURE_A:.2f} um")
    print(f"  upper hull vertices = {len(hull)}; the continuum is the straight line")
    print("  between the hull vertices that bracket the feature")
    print(f"  reflectance at {FEATURE_A:.2f} um                     = "
          f"{float(np.interp(FEATURE_A, LAM, rho)):.4f}")
    print(f"  continuum value at {FEATURE_A:.2f} um                 = "
          f"{float(np.interp(FEATURE_A, LAM, cont)):.4f}")
    print(f"  continuum-removed value at {FEATURE_A:.2f} um         = "
          f"{float(np.interp(FEATURE_A, LAM, cr)):.4f}")
    print(f"  band depth D = 1 - rho/continuum           = "
          f"{1 - float(np.interp(FEATURE_A, LAM, cr)):.4f}")
    print(f"  minimum of the continuum-removed spectrum  = {cr.min():.4f} "
          f"at {LAM[cr.argmin()]:.3f} um")
    print("  Continuum removal normalises away the background level and slope, which")
    print("  is what makes a feature comparable between spectra of different")
    print("  brightness.  The recovered POSITION and DEPTH are the diagnostics.")

    section("4. Endpoint dependence of a band depth")
    rho_curve = curved_soil(LAM, brightness=1.0, redness=0.30, amp_a=AMP_A, amp_b=0.0)
    print("  same feature, but now on a CURVED background (redness 0.30): the")
    print("  continuum is a straight line and the true background is not.")
    print("   endpoints (um)   continuum at 2.20   band depth   change from 2.00-2.50")
    ref = band_depth(LAM, rho_curve, FEATURE_A, 2.00, 2.50)
    for lo, hi in ((2.00, 2.50), (2.05, 2.45), (2.10, 2.40), (2.15, 2.25)):
        d = band_depth(LAM, rho_curve, FEATURE_A, lo, hi)
        r_lo = float(np.interp(lo, LAM, rho_curve))
        r_hi = float(np.interp(hi, LAM, rho_curve))
        cc = r_lo + (r_hi - r_lo) * (FEATURE_A - lo) / (hi - lo)
        print(f"  {lo:.2f}-{hi:.2f}   {cc:16.4f}   {d:10.4f}   {(d - ref) / ref:+18.1%}")
    cr_curve, _, hull_curve = continuum_removed(LAM, rho_curve)
    print(f"  the upper convex hull of this UPWARD-curving background is the chord")
    print(f"  itself ({len(hull_curve)} vertices), so the hull depth is "
          f"{1 - float(np.interp(FEATURE_A, LAM, cr_curve)):.4f}, the same as the")
    print("  widest straight-line continuum.  A downward-curving background would give")
    print("  a 3-vertex hull and a different value again.  A band depth is defined")
    print("  RELATIVE to its continuum, so the continuum rule is part of the")
    print("  measurement: report it, and never compare depths measured under")
    print("  different rules.")

    section("5. Band-depth ratio against a single band depth")
    print("  two SYNTHETIC features: clay-like at 2.20 um, carbonate-like at 2.33 um")
    print("   case                                  D(2.20)   D(2.33)   ratio")
    for name, bright, red, a, b in (
            ("clay-rich, reference", 1.00, 0.00, AMP_A, AMP_B),
            ("carbonate-rich, reference", 1.00, 0.00, AMP_B, AMP_A),
            ("clay-rich, 20% brighter", 1.20, 0.00, AMP_A, AMP_B),
            ("clay-rich, redder continuum", 1.00, 0.30, AMP_A, AMP_B),
            ("NO feature, redder continuum only", 1.00, 0.30, 0.0, AMP_B)):
        da, db = analytic_depths(bright, red, a, b)
        print(f"  {name:36s} {da:8.4f}  {db:8.4f}  {da / max(db, 1e-6):7.4f}")
    print("  Row 3: a MULTIPLICATIVE brightness change scales BOTH depths by the same")
    print("  factor (here 1/1.20), so each depth moves by 17% while their RATIO is")
    print("  essentially unchanged (6.3361 to 6.3362).  A depth is a ratio, so a")
    print("  common factor cancels from the ratio of two depths exactly.")
    print("  Row 4: a change in the CONTINUUM SLOPE (a redder background, with no")
    print("  change in the absorption) moves the 2.20 um depth, while the ratio of the")
    print("  two depths moves much less because both depths share the bias.")
    print("  Row 5 is the warning: with NO 2.20 um feature at all, the same slope")
    print("  change produces a spurious depth comparable to the real one.  A depth")
    print("  ratio is slope-ROBUST, not slope-immune, and it fails outright when the")
    print("  material genuinely lacks one of the two features.")

    section("6. A synthetic alteration scene with a false-positive confound")
    print("  scene: a compact 2.20 um feature patch (truth) plus a broad moisture")
    print("  gradient that changes the continuum slope and adds NO absorption")
    y_grid, x_grid = np.mgrid[0:N, 0:N]
    amp_a = AMP_A * np.exp(-(((x_grid - 40) / 12.0) ** 2 + ((y_grid - 40) / 12.0) ** 2))
    redness = 0.30 * (x_grid / N) ** 1.5
    d_a = np.zeros((N, N))
    d_b = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            d_a[i, j], d_b[i, j] = analytic_depths(
                1.0, float(redness[i, j]), float(amp_a[i, j]), AMP_B)
    noise = 0.0015
    depth_map = d_a + noise * RNG.standard_normal((N, N))
    ratio_map = d_a / np.maximum(d_b, 1e-6) + 0.05 * RNG.standard_normal((N, N))
    truth = amp_a > 0.005
    red_only, _ = analytic_depths(1.0, 0.30, 0.0, AMP_B)
    print(f"  true patch pixels = {int(truth.sum())}")
    print(f"  D(2.20) with redness 0.30 and NO feature = {red_only:.4f}, against")
    print(f"  {analytic_depths(1.0, 0.0, AMP_A, AMP_B)[0]:.4f} for the real patch:")
    print("  the slope confound is the same order as the signal.")
    print("   estimator    false-alarm rate   detection rate   threshold")
    for name, m in (("band depth", depth_map), ("depth ratio", ratio_map)):
        bg = m[~truth]
        for fa in (0.01, 0.05, 0.10):
            thr = float(np.quantile(bg, 1.0 - fa))
            flag = m > thr
            det = float((flag & truth).sum() / max(truth.sum(), 1))
            print(f"  {name:12s} {fa:16.2f}   {det:14.4f}   {thr:9.4f}")
    print("  At EQUAL false-alarm rate the depth RATIO detects far more of the patch,")
    print("  because both of its depths share the continuum-slope bias and it cancels.")
    print("  The single band depth spends its threshold on the moisture gradient.  The")
    print("  ratio is the")
    print("  right default for alteration mapping -- and it still rests on the")
    print("  assumption that the denominator feature is present at a knowable level,")
    print("  which is a geological statement, not a numerical one.")

    section("7. Geobotany: a stress index confounded by moisture")
    k_metal, k_water = 3.0, 3.0
    metal = np.exp(-(((x_grid - 40) / 14.0) ** 2 + ((y_grid - 40) / 14.0) ** 2))
    water_deficit = (x_grid / N) ** 1.5
    stress = (1.0 - np.exp(-k_metal * metal)
              + 0.55 * (1.0 - np.exp(-k_water * water_deficit)))
    stress = stress + 0.03 * RNG.standard_normal((N, N))
    print("  SYNTHETIC stress = 1 - exp(-k x metal) + 0.55 (1 - exp(-k x deficit))")
    print("  the metal anomaly is compact and the moisture deficit is a broad gradient")
    print("   threshold   detection of the metal patch   false alarms from moisture")
    for thr in (0.30, 0.40, 0.50, 0.60):
        flag = stress > thr
        det = float((flag & (metal > 0.5)).sum() / max((metal > 0.5).sum(), 1))
        fa = float((flag & (metal <= 0.5)).sum() / max((metal <= 0.5).sum(), 1))
        print(f"  {thr:10.2f}   {det:27.4f}   {fa:28.4f}")
    print("  A vegetation-stress map detects BOTH causes.  Reporting it as a")
    print("  mineralisation map assumes the moisture term is absent or known, and the")
    print("  false-alarm fraction above is what that assumption costs.  Geobotanical")
    print("  exploration therefore needs an independent layer -- terrain, drainage,")
    print("  rainfall, or a direct mineral-absorption map -- to separate the causes.")

    section("8. Verification of continuum removal")
    print("   case                              cr first   cr last    max cr")
    for name, a, b in (("no feature", 0.0, 0.0),
                       ("clay-like only", AMP_A, 0.0),
                       ("carbonate-like only", 0.0, AMP_A),
                       ("both", AMP_A, AMP_A)):
        r = curved_soil(LAM, 1.0, 0.0, a, b)
        c, _, _ = continuum_removed(LAM, r)
        print(f"  {name:32s} {c[0]:10.6f} {c[-1]:10.6f} {c.max():9.6f}")
    print("  By construction the continuum-removed spectrum equals 1 at the hull")
    print("  endpoints and lies at or below 1 everywhere: it is a normalised shape,")
    print("  which is exactly what makes it comparable between spectra.  A value above")
    print("  1 would indicate a hull-interpolation bug, not a discovery.")


if __name__ == "__main__":
    main()
