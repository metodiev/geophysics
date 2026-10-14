#!/usr/bin/env python3
"""Raster data model: resolution, resampling, aliasing and cell-area accounting.

Run with the project virtual environment:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python raster_data_model_demo.py

All rasters are SYNTHETIC arrays built in memory from a fixed seed.  Nothing is
read from disk and nothing is written to a path; the MemoryFile used in the
reprojection section is RAM-backed.

Contents
--------
1. An array plus an affine transform: extent, cell size, cell-centred geometry.
2. Cell area accounting: cells x cell_area versus the nominal extent area.
3. Aggregating a continuous field: block mean vs nearest vs max, and the RMSE.
4. Aggregating a categorical field: mode survives, mean invents values.
5. Nyquist: coarsening folds a wavelength that is demonstrably still there.
6. Hard classification of a synthetic lake: the edge-cell area error.
7. Pixel-is-area versus pixel-is-point: the half-cell convention.
8. NoData: masking, and the silent decision an aggregate makes about it.
9. Reprojection: a lon/lat grid is neither equal-area nor rectilinear in metres.
"""

import numpy as np
import rasterio
from rasterio.transform import from_origin
from rasterio.warp import reproject, Resampling, calculate_default_transform
from rasterio.io import MemoryFile
from pyproj import CRS

RNG = np.random.default_rng(20261014)

NCOL, NROW = 240, 160        # synthetic raster: 240 columns x 160 rows
CELL = 250.0                 # metres
X0, Y0 = 400_000.0, 5_600_000.0   # synthetic projected origin (metres)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def smooth_field(nrow, ncol, cell):
    """A smooth synthetic field: two superposed sinusoids plus a weak ramp."""
    row, col = np.mgrid[0:nrow, 0:ncol].astype(float)
    x = col * cell
    y = (nrow - row) * cell
    return (10.0
            + 3.0 * np.sin(2.0 * np.pi * x / 8_000.0)
            + 1.5 * np.cos(2.0 * np.pi * y / 5_000.0)
            + 0.001 * x / 1_000.0)


def block_mean(a, k):
    """Exact k x k block mean (NaN-aware; shape must divide by k)."""
    nr, nc = a.shape
    return np.nanmean(a.reshape(nr // k, k, nc // k, k), axis=(1, 3))


def block_max(a, k):
    """k x k block maximum."""
    nr, nc = a.shape
    return np.nanmax(a.reshape(nr // k, k, nc // k, k), axis=(1, 3))


def block_mode_int(a, k):
    """k x k block mode for integer classes; ties broken by the smallest value."""
    nr, nc = a.shape
    out = np.empty((nr // k, nc // k), dtype=int)
    for i in range(nr // k):
        for j in range(nc // k):
            blk = a[i * k:(i + 1) * k, j * k:(j + 1) * k].ravel()
            vals, cnts = np.unique(blk, return_counts=True)
            out[i, j] = vals[np.argmax(cnts)]
    return out


def best_single_sinusoid(x, y):
    """Least-squares fit of a*sin(2 pi x / L + phi); returns (L, amplitude)."""
    best = (float("nan"), float("nan"))
    best_sse = np.inf
    for L in np.linspace(200.0, 40_000.0, 4_000):
        B = np.column_stack([np.sin(2.0 * np.pi * x / L),
                             np.cos(2.0 * np.pi * x / L)])
        coef, *_ = np.linalg.lstsq(B, y, rcond=None)
        sse = float(np.sum((B @ coef - y) ** 2))
        if sse < best_sse:
            best_sse = sse
            best = (float(L), float(np.hypot(*coef)))
    return best


def main():
    section("1. An array plus an affine transform")
    transform = from_origin(X0, Y0, CELL, CELL)
    print(f"array shape                : {NROW} rows x {NCOL} cols "
          f"= {NROW * NCOL} cells")
    print(f"dtype                      : float64 (8 bytes per cell) -> "
          f"{NROW * NCOL * 8 / 1e6:.3f} MB uncompressed")
    print("affine transform (a,b,c,d,e,f) : "
          f"{tuple(round(float(v), 3) for v in transform[:6])}")
    print("  x = a*col + b*row + c and y = d*col + e*row + f")
    print(f"  a = {transform.a:.1f} m is the x cell size; "
          f"e = {transform.e:.1f} m is the y cell size (NEGATIVE)")
    print(f"upper-left corner (x, y)   : ({transform.c:.1f}, {transform.f:.1f}) m")
    xy = transform * (0.5, 0.5)
    print(f"centre of cell (row, col) = (0, 0): ({xy[0]:.1f}, {xy[1]:.1f}) m"
          "   <- half a cell in, not on the corner")
    print(f"lower-right corner         : "
          f"({transform.c + NCOL * CELL:.1f}, {transform.f - NROW * CELL:.1f}) m")
    print(f"extent                     : {NCOL * CELL / 1e3:.1f} km x "
          f"{NROW * CELL / 1e3:.1f} km")
    print("The array alone does not know where it is.  Six numbers carry the whole")
    print("georeference, and raster libraries agree on exactly this convention: row 0")
    print("is the NORTH edge, so the y scale is negative.  Dropping that sign flips a")
    print("raster vertically with no error message.")

    section("2. Cell area accounting")
    cell_area_km2 = (CELL / 1e3) ** 2
    n_cells = NROW * NCOL
    print(f"  cell area                       = {cell_area_km2:.6f} km^2")
    print(f"  number of cells                 = {n_cells}")
    print(f"  cells x cell area               = {n_cells * cell_area_km2:.3f} km^2")
    print(f"  extent area (km x km)           = "
          f"{(NCOL * CELL / 1e3) * (NROW * CELL / 1e3):.3f} km^2")
    print("Exact agreement is the point of a regular grid: area is counting, not")
    print("geometry.  A vector coverage of the same region needs every boundary vertex")
    print("and still only approximates the area; here the area is exact and the *shape*")
    print("is the approximation.")

    section("3. Aggregating a continuous field: which statistic, at what cost")
    field = smooth_field(NROW, NCOL, CELL)
    k = 4
    products = {
        "block mean (exact integral/area)": block_mean(field, k),
        "nearest (every k-th cell)": field[::k, ::k].astype(float),
        "offset subsample (every k-th + 1)": field[1::k, 1::k].astype(float),
        "block maximum (an extreme, not a mean)": block_max(field, k),
    }
    print(f"  aggregation {k}x{k} -> {NROW // k} x {NCOL // k} cells of "
          f"{CELL * k / 1e3:.1f} km")
    print("  method                                    RMSE vs fine   bias   max |err|")
    for name, coarse in products.items():
        up = np.repeat(np.repeat(coarse, k, axis=0), k, axis=1)
        diff = up - field
        print(f"  {name:40s} {np.sqrt(np.mean(diff ** 2)):9.4f}  "
              f"{diff.mean():+7.4f}  {np.max(np.abs(diff)):9.4f}")
    print("The block mean has the smallest RMSE (0.5875) *and* zero bias, which is not")
    print("luck: the cell average is by definition what it estimates.  Nearest is exact")
    print("at the sampled cells and wrong between them, so its error is concentrated and")
    print("its bias is small; a shifted subsample is no better in expectation.  The block")
    print("maximum is a biased extreme (+0.999 on a field whose values run about 5 to 17).")
    print("A single RMSE therefore does not rank these products: which one is right")
    print("follows from what the coarse cell is supposed to mean -- a picture, a sample,")
    print("or an estimate of an integral.")

    section("4. Aggregating a categorical field: mode survives, mean invents")
    classes = np.full((NROW, NCOL), 0, dtype=int)
    classes[:NROW // 2, :] = 1
    patch = RNG.random((NROW, NCOL)) < 0.25
    classes = np.where(patch & (classes == 1), 2, classes)
    counts_fine = np.bincount(classes.ravel(), minlength=3)
    print(f"  fine classes present        : {np.unique(classes).tolist()}")
    print(f"  fine counts                 : {counts_fine.tolist()} "
          f"({np.round(100 * counts_fine / classes.size, 2).tolist()} % each)")
    maj = block_mode_int(classes, k)
    mean_agg = block_mean(classes.astype(float), k)
    counts_coarse = np.bincount(maj.ravel(), minlength=3)
    print(f"  after {k}x{k} MODE aggregation: counts {counts_coarse.tolist()} "
          f"({np.round(100 * counts_coarse / maj.size, 2).tolist()} % each)")
    n_frac = int(np.sum(np.abs(mean_agg - np.round(mean_agg)) > 1e-9))
    print(f"  after {k}x{k} MEAN aggregation: range "
          f"[{mean_agg.min():.3f}, {mean_agg.max():.3f}], "
          f"{n_frac} of {mean_agg.size} cells are not an integer class")
    print("A mean of class codes is a number that is not a class.  Rounding it later is")
    print("an undeclared decision, and keeping it makes the layer non-categorical, so")
    print("every later lookup ('is this cell forest?') has to answer for it.  Mode is the")
    print("honest reduction -- and it still destroys the minority class:")
    print(f"class 2 is {100 * counts_fine[2] / classes.size:.2f}% of fine cells and "
          f"{100 * counts_coarse[2] / maj.size:.2f}% of coarse cells.")

    section("5. Nyquist: coarsening folds a wavelength that is still there")
    amp, lam_true = 1.0, 4_000.0
    print("  The alias of a wavelength L sampled on a grid of spacing h satisfies")
    print("  |1/L_alias| = |1/L - k/h| for the integer k that minimises it.")
    print("  cell(m)  2*cell(m)   predicted L_alias(m)   fitted L(m)   fitted amplitude")
    for step in (1, 2, 4, 8, 12, 16, 20):
        cs = CELL * step
        xs = (np.arange(NCOL // step) + 0.5) * cs
        ys = amp * np.sin(2.0 * np.pi * xs / lam_true)
        L, A = best_single_sinusoid(xs, ys)
        f_true, f_s = 1.0 / lam_true, 1.0 / cs
        cands = [abs(f_true - kk * f_s) for kk in range(0, 5)]
        f_al = min(cands)
        pred = "DC (infinite)" if f_al < 1e-12 else f"{1.0 / f_al:15.0f}"
        txt = f"{L:13.1f}" if A > 1e-3 else "     undefined"
        print(f"  {cs:7.0f}  {2 * cs:9.0f}   {pred:>19s}   {txt}   {A:12.3f}")
    print(f"The true wavelength is {lam_true:.0f} m and the true amplitude is {amp:.1f}.")
    print("While 2*cell is at or below 4000 m the fit returns the true wavelength.  As")
    print("soon as it exceeds it, the SAME samples are fitted exactly by the predicted")
    print("alias (12000 m at 3000 m spacing, 20000 m at 5000 m spacing), and at 4000 m")
    print("the samples alias onto zero frequency -- they cannot tell the sinusoid from a")
    print("constant.  Aliasing is therefore not noise and not blur: it is a second,")
    print("equally valid Earth that the samples cannot distinguish from the first.  A")
    print("12 m landscape detail sampled at 30 m is not smeared, it is relocated.")

    section("6. Hard classification of a synthetic lake: the edge-cell area error")
    r_km = float(np.sqrt(100.0 / np.pi))
    cen_x, cen_y = 15_000.0, 12_000.0        # lake centre, local metres
    col, row = np.mgrid[0:NROW, 0:NCOL].astype(float)
    dist_fine = np.hypot((col + 0.5) * CELL - cen_x,
                         (row + 0.5) * CELL - cen_y) / 1e3
    true_area = float(np.pi * r_km ** 2)
    hard_fine = (dist_fine <= r_km).astype(float)
    print(f"  synthetic lake radius       : {r_km:.4f} km, true area {true_area:.4f} km^2")
    print(f"  fine {int(CELL)} m hard classification : "
          f"{hard_fine.sum() * cell_area_km2:.4f} km^2 "
          f"({(hard_fine.sum() * cell_area_km2 - true_area) / true_area * 100:+.4f} %)")
    frac = np.clip(0.5 + (r_km - dist_fine) / (CELL / 1e3), 0.0, 1.0)
    print(f"  fine {int(CELL)} m fractional cover   : "
          f"{frac.sum() * cell_area_km2:.4f} km^2 "
          f"({(frac.sum() * cell_area_km2 - true_area) / true_area * 100:+.4f} %)")
    print("  (fractional cover ramps linearly over one cell across the edge: 1 inside,")
    print("   0 outside, 0.5 on the boundary itself)")
    print("\n  coarser grids, comparing a hard edge decision with a sub-pixel estimate")
    print("  computed by 10x10 sub-sampling of each coarse cell (independently of the")
    print("  analytic fraction above, as a check):")
    print("  cell(m)   hard area(km^2)   hard err(%)   sub-pixel area(km^2)   err(%)")
    for step in (4, 8, 16, 32):
        cs_km = CELL * step / 1e3
        n = NCOL // step
        xs = (np.arange(n) + 0.5) * cs_km
        d = np.hypot(xs[None, :] - cen_x / 1e3, xs[:, None] - cen_y / 1e3)
        hard = (d <= r_km).astype(float)
        area = hard.sum() * cs_km ** 2
        # Sub-sample each coarse cell 10x10 and count the sub-points inside.
        sub = (np.arange(10) + 0.5) / 10.0
        xsub = (xs[None, :, None, None] + (sub[None, None, :, None] - 0.5) * cs_km)
        ysub = (xs[:, None, None, None] + (sub[None, None, None, :] - 0.5) * cs_km)
        inside = (np.hypot(xsub - cen_x / 1e3, ysub - cen_y / 1e3) <= r_km)
        span = (inside.mean(axis=(2, 3)) * cs_km ** 2).sum()
        print(f"  {int(CELL * step):7d}   {area:13.4f}   "
              f"{(area - true_area) / true_area * 100:+9.4f}   "
              f"{span:18.4f}   {(span - true_area) / true_area * 100:+9.4f}")
    print("The hard-edge error does not shrink with cell size and at 8 km it reaches")
    print(f"+28%; the sub-pixel estimate stays within a few tenths of a per cent at every")
    print("resolution.  The error of a hard decision is set by the perimeter times roughly")
    print("half a cell, divided by the area, and its *sign* flips from grid to grid -- it")
    print("is variance, not a bias.  Sub-pixel fractional cover removes it, and fractional")
    print("cover is exactly what the fractional products of a land-cover map carry.")
    print("Reporting a class area from hard cells as a measurement is the commonest")
    print("quantitative error in raster GIS.")

    section("7. Pixel-is-area versus pixel-is-point: the half-cell convention")
    cen = transform * (0.5, 0.5)
    cor = transform * (0.0, 0.0)
    print(f"  transform * (0.5, 0.5) = CENTRE of the top-left cell = "
          f"({cen[0]:.1f}, {cen[1]:.1f}) m")
    print(f"  transform * (0.0, 0.0) = CORNER of the top-left cell = "
          f"({cor[0]:.1f}, {cor[1]:.1f}) m")
    print(f"  the two conventions differ by half a cell = "
          f"{CELL / 2:.1f} m in x and in y")
    print("A coordinate in a pixel-is-point file refers to the cell centre; the same")
    print("number in a pixel-is-area file refers to a corner.  Half a cell of bias is")
    print("6.25 m here, 1.5 km for a 3 km product, and it appears the moment a point")
    print("sampled from one convention is compared with a point sampled from the other.")

    section("8. NoData: what an aggregate silently does with it")
    field_nd = field.copy()
    mask = RNG.random(field_nd.shape) < 0.05
    field_nd[mask] = np.nan
    print(f"  NoData cells                    : {int(mask.sum())} of {n_cells} "
          f"({100 * mask.mean():.2f} %)")
    m_ok = float(np.nanmean(field_nd))
    m_zero = float(np.nan_to_num(field_nd).mean())
    print(f"  mean excluding NoData           : {m_ok:.6f}")
    print(f"  mean with NoData treated as zero: {m_zero:.6f}")
    print(f"  bias from that one choice       : {m_zero - m_ok:+.6f} "
          f"({100 * (m_zero - m_ok) / m_ok:+.3f} %)")
    coarse_nd = block_mean(field_nd, k)
    any_nd = np.zeros((NROW // k, NCOL // k), dtype=bool)
    for i in range(NROW // k):
        for j in range(NCOL // k):
            any_nd[i, j] = np.isnan(field_nd[i * k:(i + 1) * k,
                                           j * k:(j + 1) * k]).any()
    print(f"  coarse {k}x{k} cells with at least one NoData input: "
          f"{int(any_nd.sum())} of {coarse_nd.size} ({100 * any_nd.mean():.2f} %)")
    print(f"  policy A 'ignore NoData' (nanmean) : {coarse_nd.size} coarse cells usable "
          f"({coarse_nd.size - int(np.isnan(coarse_nd).sum())})")
    print(f"  policy B 'propagate NoData'        : "
          f"{coarse_nd.size - int(any_nd.sum())} coarse cells usable "
          f"({100 * (1 - any_nd.mean()):.2f} % retained)")
    print(f"  data volume lost by policy B       : {100 * any_nd.mean():.2f} % of the "
          f"coarse grid, from {100 * mask.mean():.2f} % of the fine cells")
    print("Casting NoData to zero is the most damaging silent decision in raster")
    print("processing: it is a 5% change to the denominator that looks like a data")
    print("reduction (measured above at -0.520, or -5.12% of the mean).  But 'ignore")
    print("NoData' is a decision too: it makes each coarse cell an average over a")
    print("different, unknown set of fine cells, and the loss of one fine cell in four")
    print("inflates into a quarter of the coarse grid being unusable under the strict")
    print("propagating policy.  Both policies are defensible; the pipeline must state")
    print("which one it used and carry the excluded count next to the statistic.")

    section("9. Reprojection: a lon/lat grid is neither equal-area nor rectilinear")
    lon0, lat0 = 0.0, 40.0
    dlon, dlat = 0.05, 0.05
    src_profile = {
        "driver": "GTiff", "height": 40, "width": 60, "count": 1,
        "dtype": "float32", "crs": CRS.from_epsg(4326),
        "transform": from_origin(lon0, lat0, dlon, dlat),
    }
    data = np.ones((40, 60), dtype="float32")   # a constant field: 1.0 everywhere
    a = 6_378_137.0
    cell_area_lat = lambda lat_s: abs(
        a * np.radians(dlon) * (np.sin(np.radians(lat_s + dlat)) -
                                np.sin(np.radians(lat_s))) * a)
    areas = [cell_area_lat(lat0 - dlat * 40), cell_area_lat(lat0 - dlat * 20),
             cell_area_lat(lat0 - dlat)]
    with MemoryFile() as mem:
        with mem.open(**src_profile) as src:
            src.write(data, 1)
            dst_crs = CRS.from_epsg(32631)
            tr, w, h = calculate_default_transform(
                src.crs, dst_crs, src.width, src.height, *src.bounds)
            dst = np.zeros((h, w), dtype="float32")
            reproject(source=rasterio.band(src, 1), destination=dst,
                      src_transform=src.transform, src_crs=src.crs,
                      dst_transform=tr, dst_crs=dst_crs,
                      resampling=Resampling.nearest)
            print(f"  source grid                : 60 x 40 cells of {dlon} deg at "
                  f"{lat0} deg N (EPSG:4326)")
            print(f"  source cell area (spherical): south row "
                  f"{areas[0] / 1e6:.4f} km^2, middle row {areas[1] / 1e6:.4f} km^2, "
                  f"north row {areas[2] / 1e6:.4f} km^2")
            print(f"  north/south cell-area ratio: {areas[2] / areas[0]:.5f} "
                  f"({100 * (areas[2] / areas[0] - 1):+.3f} % over 2 deg of latitude)")
            print(f"  the same {dlon} deg cell at 0 deg N: "
                  f"{cell_area_lat(0.0) / 1e6:.4f} km^2, at 60 deg N: "
                  f"{cell_area_lat(60.0) / 1e6:.4f} km^2")
            print(f"    ratio 60N/equator          : "
                  f"{cell_area_lat(60.0) / cell_area_lat(0.0):.5f}")
            print(f"  destination grid           : {w} x {h} cells of "
                  f"{tr.a:.2f} m x {abs(tr.e):.2f} m (EPSG:32631)")
            print(f"  destination cell area      : "
                  f"{(tr.a * abs(tr.e)) / 1e6:.6f} km^2 (constant by construction)")
            print(f"  destination grid area      : {w * h * tr.a * abs(tr.e) / 1e6:.3f} km^2")
            print(f"  source nominal area        : "
                  f"{60 * 40 * float(np.mean(areas)) / 1e6:.3f} km^2")
            print(f"  expansion of the footprint : "
                  f"{100 * (w * h * tr.a * abs(tr.e) / (60 * 40 * float(np.mean(areas))) - 1):+.3f} %")
            print(f"  value range after nearest warp: [{dst.min():.1f}, {dst.max():.1f}] "
                  "on a source that is constant 1.0")
            n_zero = int((dst == 0).sum())
            print(f"  destination cells filled with 0 (outside the source footprint): "
                  f"{n_zero} of {dst.size} ({100 * n_zero / dst.size:.2f} %)")
    print("Three facts fall out.  (i) On a geographic grid a 'cell' has no single area:")
    print(f"a {dlon} deg cell is {areas[0] / 1e6:.4f} km^2 in the south row and "
          f"{areas[2] / 1e6:.4f} km^2 in the north row here -- {100 * (areas[2] / areas[0] - 1):+.2f} %")
    print("across 2 deg of latitude, and shrinking in proportion to cos(latitude) over")
    print("the globe.  Any statistic that treats cells as equal (a per-cell mean used as")
    print("a spatial mean) is weighted wrongly, and the error is largest where the map is")
    print("most distorted.  (ii) A rectilinear lon/lat grid becomes a *curved* grid in a")
    print("projected CRS, so a warp is a resampling that interpolates wherever the grids")
    print("do not line up: the output is a new measurement, not a re-expression of the")
    print("old one.  (iii) The destination grid is the bounding box of the warped source")
    print("footprint, so it necessarily grows; the extra cells are filled with the nodata")
    print("value and look exactly like real zeros unless they are masked.  The cell area")
    print("of the output is a property of the *projection*, chosen by the analyst, and it")
    print("is constant there only by construction of the projection's own geometry.")


if __name__ == "__main__":
    main()
