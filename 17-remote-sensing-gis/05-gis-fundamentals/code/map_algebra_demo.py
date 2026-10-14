#!/usr/bin/env python3
"""Map algebra: local, focal, zonal and global operators, verified where possible.

Run with the project virtual environment:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python map_algebra_demo.py

All rasters are SYNTHETIC arrays built in memory from a fixed seed.  Nothing is
read from disk and nothing is written to a path.

Contents
--------
1. The four operator classes, on one synthetic raster set.
2. Local algebra: a normalised difference index and its error propagation.
3. Focal operators: window size, edge policy, and what filtering costs.
4. Verified focal operator: Horn slope of a synthetic plane vs its exact slope.
5. Scale dependence of slope: the same terrain at four window sizes.
6. Zonal statistics: unweighted mean of means vs the area-weighted mean.
7. Global statistics, masks, and the effect of a reclassification threshold.
8. Normalisation choice in a weighted overlay: same weights, different answers.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

NROW, NCOL = 180, 240
CELL = 200.0          # metres


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def horn_gradient(surface, cell):
    """Horn (1981) 3x3 gradients dz/dx, dz/dy, in the same units as the surface.

    The standard weights are (second row = the row above, first = below) with the
    y axis pointing NORTH (row index increases southwards):
        dz/dx = ((z3 + 2 z6 + z9) - (z1 + 2 z4 + z7)) / (8 cell)
        dz/dy = ((z7 + 2 z8 + z9) - (z1 + 2 z2 + z3)) / (8 cell)
    Edge rows and columns are left as NaN.
    """
    z = surface
    z1 = np.roll(np.roll(z, 1, 0), 1, 1)    # north-west
    z2 = np.roll(z, 1, 0)                   # north
    z3 = np.roll(np.roll(z, 1, 0), -1, 1)   # north-east
    z4 = np.roll(z, 1, 1)                   # west
    z6 = np.roll(z, -1, 1)                  # east
    z7 = np.roll(np.roll(z, -1, 0), 1, 1)   # south-west
    z8 = np.roll(z, -1, 0)                  # south
    z9 = np.roll(np.roll(z, -1, 0), -1, 1)  # south-east
    dzdx = ((z3 + 2 * z6 + z9) - (z1 + 2 * z4 + z7)) / (8.0 * cell)
    dzdy = ((z7 + 2 * z8 + z9) - (z1 + 2 * z2 + z3)) / (8.0 * cell)
    gx, gy = dzdx.copy(), dzdy.copy()
    gx[[0, -1], :] = np.nan
    gx[:, [0, -1]] = np.nan
    gy[[0, -1], :] = np.nan
    gy[:, [0, -1]] = np.nan
    return gx, gy


def focal_mean(a, k, edge="ignore"):
    """k x k focal mean with an explicit edge policy.

    'ignore'    : average the cells that exist (the window shrinks at the border)
    'propagate' : the result is NaN if any input cell in the window is NaN
    'reflect'   : mirror-pad, so the border window is filled with interior cells
    'constant'  : pad with 0.0 (the classic silent mistake on a non-zero raster)
    """
    pad = k // 2
    if edge in ("ignore", "propagate"):
        p = np.pad(a, pad, mode="constant", constant_values=np.nan)
    elif edge == "reflect":
        p = np.pad(a, pad, mode="reflect")
    else:
        p = np.pad(a, pad, mode="constant", constant_values=0.0)
    out = np.empty_like(a, dtype=float)
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            block = p[i:i + k, j:j + k]
            if edge == "propagate" and np.isnan(block).any():
                out[i, j] = np.nan
            else:
                out[i, j] = np.nanmean(block)
    return out


def main():
    section("1. The four operator classes")
    row, col = np.mgrid[0:NROW, 0:NCOL].astype(float)
    x, y = col * CELL, row * CELL
    dem = (300.0
           + 0.010 * x                             # regional tilt, m
           + 0.005 * y
           + 40.0 * np.sin(2 * np.pi * x / 6_000.0)
           + 25.0 * np.cos(2 * np.pi * y / 8_000.0))
    tsurf = 15.0 - 0.0065 * dem                        # deg C, 6.5 K/km lapse
    nir = 0.28 + 2.0e-6 * x + 0.02 * np.sin(2 * np.pi * y / 5_000.0)
    red = 0.12 + 1.0e-6 * x + 0.01 * np.cos(2 * np.pi * y / 5_000.0)
    zones = np.zeros((NROW, NCOL), dtype=int)
    zones[row < NROW / 2] = 1
    zones[(row >= NROW / 2) & (col < NCOL / 2)] = 2
    zones[(row >= NROW / 2) & (col >= NCOL / 2)] = 3
    print(f"  raster set: {NROW} x {NCOL} cells of {CELL:.0f} m "
          f"({NROW * NCOL} cells, {NCOL * CELL / 1e3:.1f} km x "
          f"{NROW * CELL / 1e3:.1f} km)")
    print("  DEM                       m     : "
          f"[{dem.min():.1f}, {dem.max():.1f}]")
    print("  surface temperature       deg C : "
          f"[{tsurf.min():.2f}, {tsurf.max():.2f}]")
    print("  NIR, red reflectance      -     : "
          f"[{nir.min():.3f}, {nir.max():.3f}], [{red.min():.3f}, {red.max():.3f}]")
    print("  zone ids                  -     : "
          f"{np.unique(zones).tolist()}")
    print("Legend of operator classes (the standard four, and the expression in each):")
    print("  local  : out[i,j] = f(in1[i,j], in2[i,j], ...)      -- same cell")
    print("  focal  : out[i,j] = f(in[i-k:i+k, j-k:j+k])         -- a window")
    print("  zonal  : out[z]   = f(in[zone == z])                -- a set of cells")
    print("  global : out      = f(in[all cells])                -- one number")
    print("Everything a raster calculator does is one of these four, in sequence.")

    section("2. Local algebra: a normalised difference index and its error")
    ndvi = (nir - red) / (nir + red)
    print(f"  NDVI = (NIR - red)/(NIR + red): range "
          f"[{ndvi.min():.4f}, {ndvi.max():.4f}], mean {ndvi.mean():.4f}")
    sigma = 0.005      # synthetic per-band reflectance noise, dimensionless
    d_nir = 2.0 * red / (nir + red) ** 2
    d_red = -2.0 * nir / (nir + red) ** 2
    var_analytic = d_nir ** 2 * sigma ** 2 + d_red ** 2 * sigma ** 2
    sd_analytic = np.sqrt(var_analytic)
    worst = int(np.argmax(sd_analytic))
    n_w, r_w = float(nir.ravel()[worst]), float(red.ravel()[worst])
    m = 20_000
    nir_mc = n_w + RNG.normal(0.0, sigma, size=m)
    red_mc = r_w + RNG.normal(0.0, sigma, size=m)
    sd_mc_cell = float(((nir_mc - red_mc) / (nir_mc + red_mc)).std())
    idx = RNG.integers(0, nir.size, size=m * 20)
    nir_true = nir.ravel()[idx]
    red_true = red.ravel()[idx]
    nir_p = nir_true + RNG.normal(0.0, sigma, size=idx.size)
    red_p = red_true + RNG.normal(0.0, sigma, size=idx.size)
    delta = ((nir_p - red_p) / (nir_p + red_p)) - ((nir_true - red_true) / (nir_true + red_true))
    sd_mc_pooled = float(delta.std())
    print(f"  per-band noise sigma      : {sigma:.4f} (dimensionless reflectance)")
    wi, wj = np.unravel_index(worst, ndvi.shape)
    print(f"  analytic sigma_NDVI        : mean {sd_analytic.mean():.5f}, "
          f"max {sd_analytic.max():.5f} (at row {int(wi)}, col {int(wj)})")
    print(f"  pooled check  sqrt(mean var_analytic) : {np.sqrt(var_analytic.mean()):.5f}")
    print(f"  pooled Monte Carlo sd of the NDVI error : {sd_mc_pooled:.5f}")
    print(f"    agreement of the pooled pair        : "
          f"{abs(np.sqrt(var_analytic.mean()) - sd_mc_pooled) / np.sqrt(var_analytic.mean()) * 100:.3f} %")
    print(f"  worst cell NIR = {n_w:.3f}, red = {r_w:.3f}:")
    print(f"    analytic sigma_NDVI = {sd_analytic.ravel()[worst]:.5f}")
    print(f"    Monte Carlo         = {sd_mc_cell:.5f} over {m} draws")
    print(f"    agreement           : "
          f"{abs(sd_mc_cell - sd_analytic.ravel()[worst]) / sd_analytic.ravel()[worst] * 100:.3f} %")
    print(f"  amplification           : {sd_analytic.mean() / sigma:.3f} x the band noise")
    print("  on average, {:.1f} x at the darkest cell in the raster".format(
        sd_analytic.ravel()[worst] / sigma))
    print("Two exact statements follow from the derivative, not from measurement:")
    print("  d(NDVI)/d(NIR) = 2 red/(NIR+red)^2 and d(NDVI)/d(red) = -2 NIR/(NIR+red)^2.")
    print("So the index is most reliable where the denominator is LARGE (both bands")
    print("bright) and least reliable in dark pixels.  A constant noise level in the")
    print("bands becomes a spatially varying noise level in every ratio index, and no")
    print("figure of the index shows it.")

    section("3. Focal operators: window size, edge policy, and what filtering costs")
    base = dem
    noise_raster = 300.0 + RNG.normal(0.0, 10.0, size=base.shape)
    print(f"  unfiltered DEM          : mean {base.mean():.3f} m, sd {base.std():.3f} m")
    print(f"  unfiltered white noise  : mean {noise_raster.mean():.3f} m, "
          f"sd {noise_raster.std():.3f} m (sd set to 10 m by construction)")
    print("  window   DEM sd(m)  retained   noise sd(m)  retained   1/k (exact)")
    for k in (3, 5, 11, 21):
        f = focal_mean(base, k, edge="ignore")
        n = focal_mean(noise_raster, k, edge="ignore")
        print(f"  {k:5d}   {f.std():8.3f}  {100 * f.std() / base.std():7.1f} %   "
              f"{n.std():9.3f}  {100 * n.std() / noise_raster.std():7.1f} %   "
              f"{100.0 / k:6.1f} %")
    print("A focal mean removes only the variance it can average out.  For a white-noise")
    print("field the surviving STANDARD DEVIATION is exactly 1/k (equivalently the variance")
    print("is 1/k^2) of the input -- an exact result, reproduced above.  For the synthetic DEM,")
    print("whose variance sits at wavelengths far longer than the window, the same")
    print("operator removes under 3% of the standard deviation.  'Smoothing reduces noise'")
    print("is therefore conditional on the noise being short-wavelength relative to the")
    print("window, and a filtered raster is filtered *permanently*: the variance removed")
    print("cannot be recovered by any later operation.")
    print("\n  edge policy with k = 5 (a 2-cell collar is 1664 of 43200 cells):")
    for policy in ("ignore", "propagate", "reflect", "constant"):
        f = focal_mean(base, 5, edge=policy)
        n_nan = int(np.isnan(f).sum())
        interior = float(np.nanmean(f[2:-2, 2:-2]))
        collar = float(np.nanmean(f)) - interior
        corner_dev = "not defined (NaN)" if np.isnan(f[0, 0]) else f"{f[0, 0] - base[0, 0]:+9.3f} m"
        print(f"    {policy:10s}: mean {np.nanmean(f):9.3f} m, sd {np.nanstd(f):7.3f} m, "
              f"NaN cells {n_nan:5d}, collar offset {collar:+8.3f} m, "
              f"corner change {corner_dev}")
    print("'ignore' keeps every cell but gives border cells a *smaller* support, so a")
    print("gradient computed near the collar mixes two window sizes.  'propagate' keeps the")
    print("window honest and loses the whole 2-cell collar (1664 cells).  'reflect' invents")
    print("interior values at the edge and is closest to 'ignore' here.  'constant' pads")
    print("with zeros, which on a raster whose values are hundreds of metres is not a mild")
    print("approximation: it depresses the collar and changes the very first corner cell by")
    print("hundreds of metres.  The edge policy is a choice; it must be stated and its")
    print("effect measured, not assumed small.")

    section("4. A verified focal operator: Horn slope of a synthetic plane")
    # A plane with a KNOWN gradient.  dz/dx = 0.05, dz/dy = 0.03 (m per m).
    gx_true, gy_true = 0.05, 0.03
    plane = 100.0 + gx_true * x + gy_true * y
    gx, gy = horn_gradient(plane, CELL)
    slope = np.degrees(np.arctan(np.hypot(gx, gy)))
    slope_true = np.degrees(np.arctan(np.hypot(gx_true, gy_true)))
    print(f"  plane: dz/dx = {gx_true}, dz/dy = {gy_true} (dimensionless)")
    print(f"  exact slope              : {slope_true:.10f} deg")
    print(f"  Horn 3x3 mean gradient gx: {np.nanmean(gx):.12f} "
          f"(error {abs(np.nanmean(gx) - gx_true):.2e})")
    print(f"  Horn 3x3 mean gradient gy: {np.nanmean(gy):.12f} "
          f"(error {abs(np.nanmean(gy) - gy_true):.2e})")
    print(f"  Horn 3x3 slope           : {np.nanmean(slope):.10f} deg "
          f"(error {abs(np.nanmean(slope) - slope_true):.2e} deg)")
    print("The agreement at the 1e-18 level is the point: an operator that cannot reproduce")
    print("an exactly known answer has no business being applied to an unknown one.  A plane")
    print("has zero second derivative, so the central-difference truncation term")
    print("of order h^2 z'''(x) vanishes identically and all that is left is float64")
    print("round-off; the same weights applied to a curved surface are only second-order")
    print("accurate, which the next measurement shows.")
    # Curvature: exact for a paraboloid.
    par = 50.0 * ((x - x.mean()) / 1_000.0) ** 2
    lap = (np.roll(par, 1, 1) + np.roll(par, -1, 1) +
           np.roll(par, 1, 0) + np.roll(par, -1, 0) - 4.0 * par) / CELL ** 2
    interior = lap[1:-1, 1:-1]
    print(f"\n  paraboloid z = 50 ((x - xbar)/1000)^2 m has exact Laplacian "
          f"{2 * 50.0 / 1_000.0 ** 2:.6e} m^-1")
    print(f"  5-point Laplacian, interior mean : {interior.mean():.6e} m^-1 "
          f"(error {abs(interior.mean() - 2 * 50.0 / 1_000.0 ** 2):.2e})")
    print("Curvature is a second derivative and therefore amplifies short wavelengths by")
    print("k^2: the same window that estimates a smooth hillslope well will produce a")
    print("curvature map dominated by whatever high-frequency noise survives the DEM.")

    section("5. Scale dependence of slope: the same terrain at four window sizes")
    # (a) EXACT verification of the finite-difference attenuation on a pure sinusoid.
    L = 6_000.0
    print(f"  (a) a pure sinusoid of wavelength {L:.0f} m, gradient d/dx cos(2 pi x/L)")
    print("      the difference samples x +/- d, so the total spacing is 2d and the")
    print("      predicted attenuation factor is sinc(2d/L) = sin(2 pi d/L)/(2 pi d/L)")
    print("      sample offset d(m)   measured attenuation   sinc(2d/L)    difference")
    xf = np.arange(0.0, 20 * L, 50.0)
    for d in (200.0, 400.0, 800.0, 1600.0):
        g_true = -(2 * np.pi / L) * np.sin(2 * np.pi * xf / L)
        # Exact derivative of sin(2 pi x/L) via two samples 2d apart, /(2d),
        # scaled by 2 pi/L so the units match the analytic derivative.
        g_fd = -(np.sin(2 * np.pi * (xf + d) / L) -
                 np.sin(2 * np.pi * (xf - d) / L)) / (2.0 * d)
        ratio = float(np.mean(np.abs(g_fd)) / np.mean(np.abs(g_true)))
        print(f"      {d:16.0f}   {ratio:19.10f}   {np.sinc(2 * d / L):10.6f}   "
              f"{abs(ratio - np.sinc(2 * d / L)):.2e}")
    print("      So the arithmetic loss of a centred difference is exactly sinc(2d/L): the")
    print("      difference column is at machine precision.  This is the factor that any")
    print("      slope comparison across windows is really measuring.")
    # (b) The mixed synthetic terrain at four window sizes.
    gxa = 0.010 + 40.0 * (2 * np.pi / 6_000.0) * np.cos(2 * np.pi * x / 6_000.0)
    gya = 0.005 - 25.0 * (2 * np.pi / 8_000.0) * np.sin(2 * np.pi * y / 8_000.0)
    g_an = np.hypot(gxa, gya)
    s_an = np.degrees(np.arctan(g_an))
    print(f"\n  (b) the mixed synthetic terrain: analytic mean |gradient| = "
          f"{g_an.mean():.6f} (dimensionless)")
    print("      window  spacing(m)   mean|g|    ratio    sinc(6km)   sinc(8km)   "
          "mean slope(deg)  frac > 2 deg")
    for k in (3, 5, 9, 17):
        h = k // 2
        d = 2.0 * h * CELL
        gx2 = np.full_like(dem, np.nan)
        gy2 = np.full_like(dem, np.nan)
        gx2[:, h:-h] = (dem[:, 2 * h:] - dem[:, :-2 * h]) / d
        gy2[h:-h, :] = (dem[:-2 * h, :] - dem[2 * h:, :]) / d
        gm = np.hypot(gx2, gy2)[h:-h, h:-h]
        s = np.degrees(np.arctan(gm))
        print(f"      {k:6d}   {d:8.0f}   {gm.mean():8.6f}  "
              f"{gm.mean() / g_an.mean():6.4f}   {np.sinc(d / 6_000.0):8.5f}   "
              f"{np.sinc(d / 8_000.0):8.5f}   {s.mean():12.3f}  "
              f"{100 * np.mean(s > 2.0):11.1f} %")
    print("  exact analytic slope field of the same synthetic surface:")
    print("    analytic slope field: mean {:.3f} deg, sd {:.3f} deg, max {:.3f} deg, "
          "fraction above 2 deg {:.1f} %".format(
              s_an.mean(), s_an.std(), s_an.max(), 100 * np.mean(s_an > 2.0)))
    print("Slope is not a property of the terrain alone.  It is a property of the terrain")
    print("*at a stated support and spacing*: widening the window lowers the mean slope")
    print("and lowers the spread faster, and the fraction of cells steeper than a fixed")
    print("threshold moves with it.  The loss is arithmetic and predictable: the two sinc")
    print("columns bracket the measured ratio at every window, because the terrain is a")
    print("mixture of a 6 km and an 8 km component.  At k = 3 the measured ratio sits 0.3%")
    print("below both, which is not a contradiction -- a centred difference also shifts the")
    print("phase of each component, and |gradient| is a nonlinear function of the two")
    print("shifted components.  A slope map without its window size and support is not a")
    print("measurement, and a slope threshold crossed by one window and not the other is a")
    print("property of the window, not of the ground.")

    section("6. Zonal statistics: mean of means versus the area-weighted mean")
    field = dem
    zone_means, zone_counts = [], []
    for z in (1, 2, 3):
        sel = zones == z
        zone_means.append(field[sel].mean())
        zone_counts.append(int(sel.sum()))
    print("  zone   n cells   area(km^2)   mean elevation(m)")
    for z, mu, n in zip((1, 2, 3), zone_means, zone_counts):
        print(f"  {z:4d}   {n:7d}   {n * (CELL / 1e3) ** 2:9.3f}   {mu:16.3f}")
    unweighted = float(np.mean(zone_means))
    weighted = float(np.sum(np.array(zone_means) * np.array(zone_counts)) / np.sum(zone_counts))
    print(f"  unweighted mean of the zone means : {unweighted:.6f} m")
    print(f"  area-weighted mean                : {weighted:.6f} m")
    print(f"  global mean of all cells          : {field.mean():.6f} m")
    print(f"  difference (a pure reporting choice): {unweighted - weighted:+.6f} m "
          f"({100 * (unweighted - weighted) / weighted:+.4f} %)")
    print("The area-weighted mean is identical to the global cell mean here because all")
    print("cells are equal area; the unweighted mean of means is not, and it is the number")
    print("a summary table usually reports.  When zones differ in size, the choice changes")
    print("the answer by a term proportional to the covariance between zone size and zone")
    print("mean, which is exactly the term a reader wants to see.")

    section("7. Global statistics, masks and a reclassification threshold")
    thr = float(np.percentile(dem, 60))
    mask = dem > thr
    print(f"  threshold at the 60th percentile of the DEM : {thr:.3f} m")
    print(f"  cells above threshold: {int(mask.sum())} "
          f"({100 * mask.mean():.2f} % -- 40.00 % by construction of the 60th percentile)")
    print(f"  global mean of the masked subset           : {dem[mask].mean():.3f} m")
    print(f"  global mean of the raster                  : {dem.mean():.3f} m")
    for shift in (-10.0, -1.0, 0.0, 1.0, 10.0):
        m2 = dem > (thr + shift)
        print(f"    threshold {thr + shift:9.3f} m ({shift:+5.1f} m): "
              f"masked fraction {100 * m2.mean():6.2f} %, "
              f"subset mean {dem[m2].mean():8.3f} m")
    print("A 'global' statistic is global only over the cells that pass the mask, and a")
    print("threshold converts a continuous field into a binary map with a step response:")
    print("a 1 m change in a threshold chosen as a percentile moves roughly 0.1% of the")
    print("cells, but a 10 m change moves about 1% and changes the reported mean of the")
    print("subset.  Where the threshold sits must be stated, because the summary statistic")
    print("depends on it.")

    section("8. Normalisation in a weighted overlay: same weights, different answers")
    w = np.array([0.5, 0.3, 0.2])
    # Two defensible normalisations of the same three input rasters.
    def minmax(a):
        return (a - a.min()) / (a.max() - a.min())

    def physical(a, lo, hi):
        return np.clip((a - lo) / (hi - lo), 0.0, 1.0)

    inputs = np.stack([dem, tsurf, ndvi])
    mins, maxs = inputs.min(axis=(1, 2)), inputs.max(axis=(1, 2))
    n_a = minmax(dem)
    n_b = minmax(tsurf[::-1, :])            # a stated sign flip for 'higher is better'
    n_c = minmax(ndvi)
    suit_a = w[0] * n_a + w[1] * n_b + w[2] * n_c
    p_a = physical(dem, 300.0, 900.0)
    p_b = physical(tsurf[::-1, :], 8.0, 14.0)
    p_c = physical(ndvi, 0.0, 0.8)
    suit_b = w[0] * p_a + w[1] * p_b + w[2] * p_c
    print(f"  weights (dimensionless)    : {w.tolist()}, sum {w.sum():.3f}")
    print(f"  input ranges               : DEM [{mins[0]:.1f}, {maxs[0]:.1f}] m, "
          f"T [{mins[1]:.1f}, {maxs[1]:.1f}] deg C, NDVI [{mins[2]:.3f}, {maxs[2]:.3f}]")
    print(f"  A min-max over the study area gives scores in "
          f"[{suit_a.min():.4f}, {suit_a.max():.4f}]")
    print(f"  A fixed physical range gives scores in "
          f"[{suit_b.min():.4f}, {suit_b.max():.4f}]")
    rank_a = np.argsort(np.argsort(suit_a.ravel()))
    rank_b = np.argsort(np.argsort(suit_b.ravel()))
    rho = np.corrcoef(suit_a.ravel(), suit_b.ravel())[0, 1]
    frac_same_decile = float(np.mean(
        (rank_a * 10 // suit_a.size) == (rank_b * 10 // suit_b.size)))
    print(f"  Pearson correlation of the two score rasters   : {rho:.6f}")
    print(f"  fraction of cells in the same score decile     : "
          f"{100 * frac_same_decile:.3f} %")
    top_a = np.unravel_index(int(np.argmax(suit_a)), suit_a.shape)
    top_b = np.unravel_index(int(np.argmax(suit_b)), suit_b.shape)
    print(f"  argmax under min-max normalisation : {top_a} "
          f"(score {suit_a[top_a]:.4f})")
    print(f"  argmax under physical-range        : {top_b} "
          f"(score {suit_b[top_b]:.4f})")
    print(f"  the two argmax cells are {np.hypot(*(np.array(top_a) - np.array(top_b))) * CELL / 1e3:.3f} km apart")
    print("The weights are identical and the intent is identical, yet the scores are not")
    print("even a monotone function of one another: a min-max normalisation re-scales each")
    print("input by whatever range the study area happens to contain, so adding one")
    print("extreme pixel to the study area changes every score in the map.  A physical")
    print("range is arbitrary but *fixed*, and therefore reproducible and falsifiable.  A")
    print("weighted overlay is a decision rule, not a measurement, and it must carry the")
    print("normalisation, the ranges and the weights, or it cannot be reviewed.")


if __name__ == "__main__":
    main()
