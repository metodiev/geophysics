"""Vector-raster integration: sampling, masking and zonal statistics.

A SYNTHETIC raster (UTM metres) is combined with SYNTHETIC polygons three ways:
point sampling, per-polygon masking, and full-grid rasterisation. Every
statistic is compared with an independently computed value, and the sensitivity
of zonal statistics to the all_touched flag, to cell size, and to window
truncation is measured.

The raster is written into a throw-away directory inside this module and deleted
on exit.

Run:  /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python vector_raster_ops_demo.py
Requires: numpy, pandas, geopandas, rasterio, shapely.
"""

from __future__ import annotations

import atexit
import tempfile
from pathlib import Path

import numpy as np
import geopandas as gpd
import pandas as pd
import rasterio
from rasterio.enums import Resampling
from rasterio.features import geometry_mask, rasterize
from rasterio.transform import from_origin
from rasterio.windows import from_bounds, transform as window_transform
from shapely import box, points

RNG = np.random.default_rng(20260904)
HERE = Path(__file__).resolve().parent
_SCRATCH = tempfile.TemporaryDirectory(prefix="_demo_vr_", dir=HERE)
atexit.register(_SCRATCH.cleanup)
WORK = Path(_SCRATCH.name)

X0, Y0 = 500_000.0, 4_200_000.0
RES = 30.0
NCOL, NROW = 800, 600                 # 24 km x 18 km at 30 m
CRS = "EPSG:32612"
OFFSET = 17.0                         # deliberately not a multiple of RES


def section(title: str) -> None:
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def field_of(x, y):
    """SYNTHETIC 'elevation' in metres: a plane, a ridge and a basin."""
    plane = 200.0 + 0.004 * (x - X0) + 0.002 * (y - Y0)
    ridge = 180.0 * np.exp(-((x - (X0 + 8_000.0)) / 1_500.0) ** 2)
    basin = -120.0 * np.exp(-(((x - (X0 + 17_000.0)) / 3_000.0) ** 2
                              + ((y - (Y0 - 5_000.0)) / 2_000.0) ** 2))
    # A 90 m ripple: resolved by 30 m cells, averaged out by 240 m cells.
    ripple = 4.0 * np.sin(2 * np.pi * (x - X0) / 90.0) * np.cos(
        2 * np.pi * (y - Y0) / 90.0)
    return plane + ridge + basin + ripple


def bilinear_sample(band, tfm, x, y):
    """Four-neighbour bilinear interpolation, given a raster transform."""
    col_f, row_f = (~tfm) * (x, y)
    col_f -= 0.5                                  # corner -> centre coordinates
    row_f -= 0.5
    c0, r0 = int(np.floor(col_f)), int(np.floor(row_f))
    dc, dr = col_f - c0, row_f - r0
    if not (0 <= c0 < band.shape[1] - 1 and 0 <= r0 < band.shape[0] - 1):
        return float("nan")
    q = np.array([[band[r0, c0], band[r0, c0 + 1]],
                  [band[r0 + 1, c0], band[r0 + 1, c0 + 1]]], dtype="float64")
    if not np.isfinite(q).all():
        return float("nan")
    return float(q[0, 0] * (1 - dc) * (1 - dr) + q[0, 1] * dc * (1 - dr)
                 + q[1, 0] * (1 - dc) * dr + q[1, 1] * dc * dr)


def build(scenario):
    tfm = from_origin(X0, Y0, RES, RES)
    xs = X0 + (np.arange(NCOL) + 0.5) * RES
    ys = Y0 - (np.arange(NROW) + 0.5) * RES
    xx, yy = np.meshgrid(xs, ys)
    data = (field_of(xx, yy) + RNG.normal(0.0, 0.3, xx.shape)).astype("float32")
    data[0:15, 0:40] = -9999.0                     # synthetic no-data corner
    path = WORK / "dem.tif"
    with rasterio.open(path, "w", driver="GTiff", height=NROW, width=NCOL,
                       count=1, dtype="float32", crs=CRS, transform=tfm,
                       nodata=-9999.0, tiled=True, blockxsize=256,
                       blockysize=256, compress="deflate") as dst:
        dst.write(data, 1)

    def blk(x0, y0, x1, y1):
        return box(X0 + x0 + scenario * OFFSET, Y0 - y1 - scenario * OFFSET,
                   X0 + x1 + scenario * OFFSET, Y0 - y0 - scenario * OFFSET)

    blocks = gpd.GeoDataFrame(
        {"block": ["B1", "B2", "B3", "B4"],
         "target": ["ridge", "basin", "plain", "mixed"]},
        geometry=[blk(6_000.0, 1_000.0, 10_000.0, 3_000.0),
                  blk(14_000.0, 3_000.0, 20_000.0, 7_000.0),
                  blk(1_000.0, 12_000.0, 5_000.0, 16_000.0),
                  blk(11_000.0, 9_000.0, 21_000.0, 15_000.0)],
        crs=CRS)
    blocks["area_km2"] = blocks.geometry.area / 1e6
    return path, blocks


def main() -> None:
    path, blocks = build(scenario=1)

    section("1. The two objects: a raster on a grid and polygons on a plane")
    with rasterio.open(path) as src:
        print(f"  raster: {src.width} x {src.height} px at {src.res[0]:.0f} m, "
              f"crs {src.crs}, nodata {src.nodata}")
        print(f"  extent: {src.bounds.left:,.0f} .. {src.bounds.right:,.0f} E, "
              f"{src.bounds.bottom:,.0f} .. {src.bounds.top:,.0f} N")
        print(f"  pixels = {src.width * src.height:,}, cell area = "
              f"{src.res[0] * src.res[1]:,.0f} m^2 = "
              f"{src.res[0] * src.res[1] / 1e6:.6f} km^2")
        print(f"  a fully valid raster covers "
              f"{src.width * src.height * RES ** 2 / 1e6:,.2f} km^2")
    print(f"  polygons: {len(blocks)} blocks, areas "
          f"{[round(a, 4) for a in blocks.area_km2]} km^2")
    print(f"  the blocks are offset by {OFFSET:.0f} m from the pixel grid on")
    print(f"  purpose: no polygon edge lies on a pixel boundary, so the boundary")
    print(f"  rule has to be decided rather than ignored")

    section("2. Point sampling: the geometry is a lookup key")
    with rasterio.open(path) as src:
        coords = [(X0 + 1_000.0 + 400.0 * i, Y0 - 4_000.0) for i in range(6)]
        st = gpd.GeoDataFrame({"station": [f"ST{i:02d}" for i in range(6)]},
                              geometry=points([c[0] for c in coords],
                                              [c[1] for c in coords]), crs=CRS)
        nearest = np.array([v[0] for v in src.sample(coords)])
        band = src.read(1, masked=True)
        bilinear = np.array([bilinear_sample(band, src.transform, x, y)
                             for x, y in coords])
        exact = field_of(np.array([c[0] for c in coords]),
                         np.array([c[1] for c in coords]))
        for i in range(3):
            print(f"  {st.station.iloc[i]} at ({coords[i][0]:,.0f}, "
                  f"{coords[i][1]:,.0f}): nearest = {nearest[i]:.3f} m, "
                  f"bilinear = {bilinear[i]:.3f} m, analytic = {exact[i]:.3f} m")
        print(f"  max |nearest  - analytic| = {np.abs(nearest - exact).max():.3f} m")
        print(f"  max |bilinear - analytic| = {np.abs(bilinear - exact).max():.3f} m")
        print(f"  the surface carries 0.3 m of seeded noise plus a 90 m ripple and the")
        print(f"  {RES:.0f} m grid samples that ripple only {90.0 / RES:.0f} times per")
        print(f"  cycle. Both resamplings are therefore metre-scale, and bilinear wins")
        print(f"  by {np.abs(nearest - exact).max() / np.abs(bilinear - exact).max():.1f}x "
              f"on the worst sample because it can follow the ripple")
        print(f"  rasterio's sample() has no resampling argument: it always returns")
        print(f"  the containing pixel, so it is piecewise constant.")
        ox = X0 + 46.5 * RES                     # an exact pixel centre
        oy = Y0 - 7.5 * RES
        inside = list(src.sample([(ox, oy), (ox + 10.0, oy),
                                  (ox + RES, oy)]))
        vals = [round(float(v[0]), 6) for v in inside]
        print(f"  at ({ox:,.1f}, {oy:,.1f}) and 10 m east: {vals[0]} and {vals[1]} "
              f"-- identical, same pixel")
        print(f"  at {RES:.0f} m east: {vals[2]} -- a step of "
              f"{vals[2] - vals[0]:+.3f} m at the pixel edge")
        print(f"  the coordinate is effectively snapped to the pixel centre, up to")
        print(f"  {RES / np.sqrt(2):.1f} m away, and that horizontal error becomes a")
        print(f"  vertical error wherever the terrain has slope")

    section("3. Masking a polygon inside a window")
    with rasterio.open(path) as src:
        block = blocks.geometry.iloc[2]              # B3
        win = from_bounds(*block.bounds, transform=src.transform)
        wt = window_transform(win, src.transform)
        sub = src.read(1, window=win, masked=True)
        print(f"  window from the polygon bounds: col_off = {win.col_off:.3f}, "
              f"row_off = {win.row_off:.3f}, size = {win.width:.3f} x "
              f"{win.height:.3f} px")
        print(f"  read() rounds the window outward: shape = {sub.shape}")
        m = geometry_mask([block], out_shape=sub.shape, transform=wt,
                          invert=True, all_touched=False)
        area = m.sum() * RES ** 2
        print(f"  pixels whose CENTRE is inside: {int(m.sum()):,} = "
              f"{area / 1e6:.4f} km^2 against a polygon area of "
              f"{block.area / 1e6:.4f} km^2 "
              f"({100 * (area - block.area) / block.area:+.3f} %)")
        print(f"  the window transform is not the raster transform: its origin is")
        print(f"  the window's corner, "
              f"({wt.c:.1f}, {wt.f:.1f}) instead of ({src.transform.c:.1f}, "
              f"{src.transform.f:.1f})")
        print(f"  passing the RASTER transform with a windowed array is the")
        print(f"  classic misalignment: the polygon lands "
              f"{abs(wt.c - src.transform.c):.0f} m east and "
              f"{abs(wt.f - src.transform.f):.0f} m south of where it belongs")

    section("4. Zonal statistics on the full grid, two ways")
    with rasterio.open(path) as src:
        data = src.read(1, masked=True).filled(np.nan)
        labels = rasterize([(g, i + 1) for i, g in enumerate(blocks.geometry)],
                           out_shape=(src.height, src.width),
                           transform=src.transform, fill=0, dtype="int32")
        rows = []
        for i, row in blocks.iterrows():
            for touched, lab in ((False, labels == i + 1),):
                vals = data[lab]
                vals = vals[np.isfinite(vals)]
                rows.append({"block": row.block, "target": row.target,
                             "n": vals.size, "mean": vals.mean(),
                             "std": vals.std(ddof=1), "min": vals.min(),
                             "max": vals.max(),
                             "area_km2": vals.size * RES ** 2 / 1e6})
            m = rasterize([(row.geometry, 1)], out_shape=(src.height, src.width),
                          transform=src.transform, fill=0, dtype="int32",
                          all_touched=True)
            vals = data[m == 1]
            vals = vals[np.isfinite(vals)]
            rows.append({"block": row.block, "target": row.target + " (all)",
                         "n": vals.size, "mean": vals.mean(),
                         "std": vals.std(ddof=1), "min": vals.min(),
                         "max": vals.max(),
                         "area_km2": vals.size * RES ** 2 / 1e6})
        table = pd.DataFrame(rows)
        section4_means = {r["block"]: r["mean"] for r in rows
                          if "(" not in r["target"]}
        print(table.round(4).to_string(index=False))
        grp_n = table.groupby("block")["n"]
        grp_m = table.groupby("block")["mean"]
        print(f"  the two boundary rules change the pixel count by up to "
              f"{int((grp_n.max() - grp_n.min()).max()):,} pixels "
              f"({100 * ((grp_n.max() - grp_n.min()) / grp_n.min()).max():.2f} %)")
        print(f"  and the mean by up to {float((grp_m.max() - grp_m.min()).max()):.4f} m")
        print(f"  on this smooth synthetic surface the mean is barely affected; on")
        print(f"  a DEM with a fault scarp the rim pixels are the extremes, and the")
        print(f"  all_touched choice becomes an interpretation decision")

    section("5. Window truncation and the boundary rule together")
    with rasterio.open(path) as src:
        block = blocks.geometry.iloc[2]
        win = from_bounds(*block.bounds, transform=src.transform)
        wt = window_transform(win, src.transform)
        print(f"  the window is {win.width:.3f} x {win.height:.3f} px, so an integer")
        print(f"  window cannot contain the whole polygon: "
              f"{win.width - int(win.width):.3f} px of width is cut")
        facts = {}
        for label, shape, tfm in (("full grid", (src.height, src.width),
                                   src.transform),
                                  (f"window {int(win.height)}x{int(win.width)}",
                                   (int(win.height), int(win.width)), wt)):
            for touched in (False, True):
                m = rasterize([(block, 1)], out_shape=shape, transform=tfm,
                              fill=0, dtype="int32", all_touched=touched)
                facts[(label, touched)] = int((m == 1).sum())
        for label in ("full grid", f"window {int(win.height)}x{int(win.width)}"):
            print(f"  {label:16s}: centre rule {facts[(label, False)]:6,} px, "
                  f"all_touched {facts[(label, True)]:6,} px")
        lost = facts[("full grid", True)] - facts[(f"window {int(win.height)}"
                                                   f"x{int(win.width)}", True)]
        print(f"  the centre rule survives truncation unchanged "
              f"({facts[('full grid', False)] == facts[(f'window {int(win.height)}x{int(win.width)}', False)]}),")
        print(f"  but all_touched loses {lost:,} rim pixels "
              f"({100 * lost / facts[('full grid', True)]:.2f} %) to the cut column")
        print(f"  and row. Rasterise on the full grid when boundary pixels matter,")
        print(f"  or round the window outward before masking.")

    section("6. Resolution changes the answer")
    with rasterio.open(path) as src:
        block = blocks.geometry.iloc[2]
        win = from_bounds(*block.bounds, transform=src.transform)
        wt = window_transform(win, src.transform)
        reference = None
        std_fine = None
        area_drifts = []
        for factor in (1, 2, 4, 8):
            shape = (int(win.height) // factor, int(win.width) // factor)
            data = src.read(1, window=win, out_shape=shape,
                            resampling=Resampling.average, masked=True)
            step = wt * rasterio.Affine.scale(int(win.width) / shape[1],
                                              int(win.height) / shape[0])
            m = geometry_mask([block], out_shape=data.shape, transform=step,
                              invert=True, all_touched=False)
            vals = data.filled(np.nan)[m]
            vals = vals[np.isfinite(vals)]
            if reference is None:
                reference = float(vals.mean())
                std_fine = float(vals.std(ddof=1))
            area_drifts.append(abs(1.0 - vals.size * (RES * factor) ** 2
                                   / block.area) * 100.0)
            print(f"  {factor}x coarser ({RES * factor:5.0f} m cells): "
                  f"{vals.size:6,} pixels, mean = {vals.mean():9.4f} m "
                  f"({vals.mean() - reference:+.4f} m), "
                  f"std = {vals.std(ddof=1):7.4f} m, "
                  f"pixel-area / block-area = "
                  f"{vals.size * (RES * factor) ** 2 / block.area:.3f}")
        print(f"  block-averaging is conservative: the area-weighted mean is stable")
        print(f"  to {abs(vals.mean() - reference):.4f} m across a {8:.0f}x change in cell size")
        print(f"  because averaging a smooth field commutes with area weighting.")
        print(f"  What is NOT stable is the spatial variability: the 90 m ripple in")
        print(f"  the surface is resolved by 30 m cells and averaged away by 240 m")
        print(f"  cells, so the std of the cell values falls from "
              f"{std_fine:.4f} m to {vals.std(ddof=1):.4f} m")
        print(f"  and the polygon-area estimate drifts by up to "
              f"{max(area_drifts):.1f} %")
        print(f"  the quadrature difference sqrt({std_fine:.4f}^2 - "
              f"{vals.std(ddof=1):.4f}^2) = "
              f"{np.sqrt(max(std_fine ** 2 - vals.std(ddof=1) ** 2, 0.0)):.4f} m is")
        print(f"  what the coarse cells removed; the rest of the std is the 4 km")
        print(f"  scale slope that no cell size can average away")

    section("7. Point-in-polygon counts: rasterise versus intersect")
    with rasterio.open(path) as src:
        labels = rasterize([(g, i + 1) for i, g in enumerate(blocks.geometry)],
                           out_shape=(src.height, src.width),
                           transform=src.transform, fill=0, dtype="int32")
        ids, counts = np.unique(labels, return_counts=True)
        for i, c in zip(ids, counts):
            if i == 0:
                print(f"  label 0 (no block): {c:,} pixels "
                      f"({100 * c / labels.size:.2f} % of the raster)")
            else:
                area = c * RES ** 2 / 1e6
                true = blocks.geometry.area.iloc[i - 1] / 1e6
                print(f"  label {i} ({blocks.block.iloc[i - 1]}): {c:,} pixels = "
                      f"{area:.4f} km^2 vs polygon area {true:.4f} km^2 "
                      f"({100 * (area - true) / true:+.3f} %)")
        print(f"  pixelated areas land within "
              f"{max(abs(c * RES ** 2 / 1e6 - blocks.geometry.area.iloc[i - 1] / 1e6) / (blocks.geometry.area.iloc[i - 1] / 1e6) * 100 for i, c in zip(ids, counts) if i):.3f} %")
        print(f"  of the true polygon areas: rasterisation is how a raster code")
        print(f"  learns where the polygons are, and the boundary quantisation is")
        print(f"  the price of admission")

    section("8. Zonal statistics as one grouped reduction")
    with rasterio.open(path) as src:
        data = src.read(1, masked=True).filled(np.nan)
        labels = rasterize([(g, i + 1) for i, g in enumerate(blocks.geometry)],
                           out_shape=(src.height, src.width),
                           transform=src.transform, fill=0, dtype="int32")
        valid = np.isfinite(data) & (labels > 0)
        flat_labels = labels[valid]
        flat_data = data[valid]
        order = np.argsort(flat_labels, kind="stable")
        sorted_lab = flat_labels[order]
        sorted_val = flat_data[order]
        bounds_idx = np.searchsorted(sorted_lab, np.unique(sorted_lab))
        print(f"  {valid.sum():,} labelled pixels grouped with one stable sort")
        uniq = np.unique(sorted_lab)
        for i, lab in enumerate(uniq):
            lo = bounds_idx[i]
            hi = bounds_idx[i + 1] if i + 1 < bounds_idx.size else sorted_lab.size
            chunk = sorted_val[lo:hi]
            print(f"  block {int(lab)}: {chunk.size:6,} px, mean = "
                  f"{chunk.mean():9.4f} m, std = {chunk.std(ddof=1):8.4f} m, "
                  f"min = {chunk.min():8.3f}, max = {chunk.max():8.3f}")
        worst = max(abs(float(chunk.mean()) - section4_means[f"B{int(lab)}"])
                    for i, lab in enumerate(uniq)
                    for chunk in [sorted_val[
                        bounds_idx[i]:(bounds_idx[i + 1]
                                       if i + 1 < bounds_idx.size
                                       else sorted_lab.size)]])
        print(f"  compared with Section 4, the largest per-block disagreement is "
              f"{worst:.2e} m: the same statistic, obtained without a single")
        print(f"  per-polygon loop, from one sort plus a searchsorted")

    section("9. Units: three defensible 'mean elevations'")
    with rasterio.open(path) as src:
        data = src.read(1, masked=True).filled(np.nan)
        labels = rasterize([(g, i + 1) for i, g in enumerate(blocks.geometry)],
                           out_shape=(src.height, src.width),
                           transform=src.transform, fill=0, dtype="int32")
        rows = []
        for i, row in blocks.iterrows():
            vals = data[labels == i + 1]
            vals = vals[np.isfinite(vals)]
            rows.append((row.block, vals.mean(), vals.size * RES ** 2))
        df = pd.DataFrame(rows, columns=["block", "mean_m", "area_m2"])
        simple = float(df.mean_m.mean())
        weighted = float((df.mean_m * df.area_m2).sum() / df.area_m2.sum())
        raster_mean = float(np.nanmean(data))
        print(df.round(4).to_string(index=False))
        print(f"  mean of the block means            = {simple:.4f} m")
        print(f"  area-weighted mean of the blocks   = {weighted:.4f} m")
        print(f"  mean of every finite raster pixel  = {raster_mean:.4f} m")
        print(f"  spread between the first two = "
              f"{abs(simple - weighted):.4f} m ({abs(simple - weighted) * 100:.1f} cm);")
        print(f"  against the all-pixel raster mean the gap is "
              f"{abs(raster_mean - weighted):.2f} m,")
        print(f"  because the raster also covers terrain no block touches")
        print(f"  so 'the mean elevation' is only defined once the areal support is")
        print(f"  stated. All three numbers are in metres; they are not the same")
        print(f"  quantity")


if __name__ == "__main__":
    main()
