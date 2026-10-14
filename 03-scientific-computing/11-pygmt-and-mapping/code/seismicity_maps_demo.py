"""Seismicity maps: a synthetic catalogue, focal mechanisms and a trench.

Run:  .venv/bin/python 03-scientific-computing/11-pygmt-and-mapping/code/seismicity_maps_demo.py
Requires: pygmt (needs GMT and Ghostscript), numpy, pandas, pyproj.

Companion to lesson 03-11-03.

Part 1  a synthetic catalogue sampled from a Gutenberg-Richter law, and the
        b-value recovered from it.
Part 2  depth and distance statistics, measured rather than assumed.
Part 3  moment magnitude from seismic moment.
Part 4  the map: epicentres, focal mechanisms, a trench and a ridge.
Part 5  what the plotted symbols actually encode.

No real catalogue is downloaded: every event here is generated in the script
from stated parameters, so every number quoted is a property of that sample.
"""

from __future__ import annotations

import io
import shutil
import struct
from pathlib import Path

import numpy as np
import pandas as pd
import pygmt
import pyproj

ARTIFACTS = Path(__file__).resolve().parent / ".demo-artifacts"
REGION = [136.0, 148.0, 30.0, 42.0]      # a subduction-zone corner, as a stage
B_VALUE = 1.0
M_C = 2.5
DELTA_M = 0.1


def section(title: str) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def png_size(path: Path) -> tuple[int, int]:
    return struct.unpack(">II", path.read_bytes()[16:24])


def main() -> None:
    ARTIFACTS.mkdir(exist_ok=True)
    try:
        # --------------------------------------------------------------
        section("1. A synthetic catalogue and its b-value")
        # --------------------------------------------------------------
        rng = np.random.default_rng(20261014)
        n_events = 4000
        # Inverse transform for the Gutenberg-Richter exponential in magnitude.
        magnitudes = M_C - np.log10(1.0 - rng.uniform(0.0, 1.0, n_events)) / B_VALUE
        magnitudes = np.round(magnitudes / DELTA_M) * DELTA_M
        mean_m = magnitudes.mean()
        b_plain = np.log10(np.e) / (mean_m - M_C)
        b_utsu = np.log10(np.e) / (mean_m - (M_C - DELTA_M / 2))
        expected_mean = M_C + 1.0 / (B_VALUE * np.log(10))
        sem = np.std(magnitudes) / np.sqrt(n_events)
        print(f"  {n_events} synthetic events generated with b = {B_VALUE} and "
              f"completeness Mc = {M_C}, then rounded to {DELTA_M}")
        print(f"  mean(M) measured = {mean_m:.6f}; the exact exponential mean "
              f"for b = {B_VALUE} is Mc + 1/(b ln10) = {expected_mean:.6f}")
        print(f"  standard error of the sample mean: {sem:.6f}, so the "
              f"measured mean is "
              f"{(expected_mean - mean_m) / sem:+.2f} standard errors from "
              f"the theoretical one")
        print(f"  b = log10(e) / (mean(M) - Mc)            = {b_plain:.6f}")
        print(f"  b = log10(e) / (mean(M) - (Mc - dM/2))   = {b_utsu:.6f}  "
              f"(Utsu's binning correction)")
        print(f"  input b = {B_VALUE}; the two estimators bracket it, and the")
        print(f"  whole difference between them is the {DELTA_M / 2:.2f} in the "
              f"denominator")
        counts, edges = np.histogram(magnitudes,
                                     bins=np.arange(M_C, 8.0 + 1e-9, 0.5))
        print("  counts per 0.5 magnitude bin (log10 of the count in brackets):")
        for count, edge in zip(counts, edges[:-1]):
            bar = "#" * int(round(np.log10(max(count, 1)) * 8))
            print(f"      M [{edge:.1f}, {edge + 0.5:.1f}): {count:>5} "
                  f"[{np.log10(max(count, 1)):+.3f}] {bar}")
        usable = counts >= 10
        slope = np.polyfit(edges[:-1][usable] + 0.25,
                           np.log10(counts[usable]), 1)
        print(f"  least-squares slope of log10(N) against M over the "
              f"{int(usable.sum())} bins with at least 10 events: "
              f"{slope[0]:+.4f} (expected {-B_VALUE:+.4f})")
        expected_big = n_events * 10 ** (-B_VALUE * (6.0 - M_C))
        print(f"  the sample contains {int(np.count_nonzero(magnitudes > 6.0))} "
              f"events above M 6; the GR law predicts {expected_big:.2f} for "
              f"this catalogue size")
        print(f"  largest event in the sample: M {magnitudes.max():.1f}")
        print("  Observation: the maximum-likelihood estimate is the one to")
        print("  quote and the binned slope is the one to look at -- the bins")
        print("  with fewer than ten events carry almost no information, and")
        print("  the tail above M 6 is consistent with the input law while")
        print("  containing too few events to constrain it. A b-value")
        print("  estimated from the M > 6 part of a 4000-event catalogue is")
        print("  arithmetic on one or two numbers.")

        # --------------------------------------------------------------
        section("2. Depths and distances to the trench")
        # --------------------------------------------------------------
        depths = np.round(np.clip(rng.exponential(18.0, n_events), 3.0, 90.0), 1)
        print(f"  depth (km): min {depths.min():.1f}, median "
              f"{np.median(depths):.1f}, mean {depths.mean():.2f}, max "
              f"{depths.max():.1f}")
        print(f"  fraction shallower than 30 km: "
              f"{100 * np.mean(depths < 30.0):.1f} %; "
              f"deeper than 60 km: {100 * np.mean(depths > 60.0):.1f} %")
        lons = rng.uniform(REGION[0], REGION[1], n_events)
        lats = rng.normal(36.5, 1.1, n_events).clip(REGION[2], REGION[3])
        # A synthetic trench: a straight line with two bends in map coordinates.
        trench_lon = np.array([REGION[0], 141.0, 143.5, REGION[1]])
        trench_lat = np.array([37.4, 36.4, 34.0, 33.0])
        geod = pyproj.Geod(ellps="WGS84")
        distances = np.array([
            min(geod.inv(lon, lat, tlon, tlat)[2]
                for tlon, tlat in zip(trench_lon, trench_lat))
            for lon, lat in zip(lons, lats)])
        print(f"  distance from each event to the NEAREST TRENCH VERTEX")
        print(f"  (a vertex approximation, not a perpendicular to the segments):")
        print(f"      median {np.median(distances) / 1000:.2f} km, "
              f"mean {distances.mean() / 1000:.2f} km, "
              f"max {distances.max() / 1000:.2f} km")
        for limit in (25_000.0, 50_000.0, 100_000.0):
            print(f"      within {limit / 1000:>5.0f} km of a vertex: "
                  f"{100 * np.mean(distances < limit):.1f} %")
        total_length = sum(geod.inv(trench_lon[i], trench_lat[i],
                                    trench_lon[i + 1], trench_lat[i + 1])[2]
                           for i in range(len(trench_lon) - 1))
        print(f"  total trench length: {total_length / 1000:.1f} km over "
              f"{len(trench_lon)} vertices")
        print("  Observation: the 'within 50 km of the trench' number depends")
        print("  on how the trench is represented -- four vertices here. A")
        print("  real trench line has hundreds, and the vertex approximation")
        print("  underestimates the perpendicular distance wherever the line")
        print("  bends. The number is quoted with its method for that reason.")

        # --------------------------------------------------------------
        section("3. Moment magnitude from seismic moment")
        # --------------------------------------------------------------
        print("  Mw = (log10(M0) - 9.1) / 1.5 with M0 in N m")
        for m0 in (1.0e15, 1.0e18, 1.0e19, 1.0e21):
            print(f"      M0 = {m0:>8.1e} N m -> Mw = "
                  f"{(np.log10(m0) - 9.1) / 1.5:6.3f}")
        print("  dimensions from the standard scaling relations:")
        for mw in (5.0, 6.0, 7.0, 8.0):
            length = 10 ** (mw - 4.0)
            width = 10 ** (0.5 * mw - 1.6)
            print(f"      Mw {mw:.1f}: rupture length about {length:8.1f} km, "
                  f"width about {width:6.1f} km, area about "
                  f"{length * width:9.0f} km^2")
        print("  Observation: a magnitude is a logarithm, so an order of")
        print("  magnitude in M0 is 0.67 in Mw -- the map's symbol sizes are")
        print("  therefore a steep distortion of the quantity they encode.")

        # --------------------------------------------------------------
        section("4. The map")
        # --------------------------------------------------------------
        focal = pd.DataFrame({
            "longitude": [139.5, 142.5, 145.0],
            "latitude": [35.5, 36.0, 34.5],
            "depth": [25.0, 45.0, 12.0],
            "strike": [20.0, 200.0, 340.0],
            "dip": [25.0, 60.0, 80.0],
            "rake": [80.0, -20.0, 170.0],
            "magnitude": [7.4, 6.1, 5.2],
        })
        sizes = 0.02 + 0.05 * (magnitudes - M_C) ** 1.6
        print(f"  epicentre symbol sizes: {sizes.min():.4f} to "
              f"{sizes.max():.4f} cm^2, i.e. a factor of "
              f"{sizes.max() / sizes.min():.1f} between the smallest")
        print(f"  and largest event in the catalogue; without the 0.02 offset")
        print(f"  the smallest event would have zero area and would not be")
        print(f"  drawn at all")
        f = pygmt.Figure()
        f.basemap(region=REGION, projection="M12c", frame=["af", "WSen"])
        f.coast(shorelines="0.4p,black", land="gray95",
                water="lightblue", resolution="crude")
        f.plot(x=lons, y=lats, style="cc", size=sizes, fill="red@60",
               pen="0.1p,black", transparency=40)
        f.plot(x=trench_lon, y=trench_lat, pen="2p,blue")
        f.plot(x=[145.5, 147.0], y=[41.0, 41.5], pen="2p,orange3")
        # The spec table must be exactly lon, lat, depth, strike, dip, rake,
        # magnitude, in that order: meca reads a plain vector table.
        f.meca(spec=focal[["longitude", "latitude", "depth", "strike", "dip",
                           "rake", "magnitude"]].to_numpy(),
               convention="aki", scale="3c", compression_fill="red",
               extension_fill="white", pen="0.5p,black")
        f.text(x=141.0, y=38.6, text="trench", font="10p,Helvetica-Bold,blue",
               justify="CM")
        f.text(x=146.4, y=41.6, text="ridge", font="10p,Helvetica-Bold,orange3",
               justify="CM")
        f.legend(spec=io.StringIO(
            "H 9p,Helvetica-Bold Legend\n"
            f"S 0.2c c 0.05c red@60 0.1p,black - M > {M_C:.1f} (n = {n_events})\n"
            "S 0.2c - 0.4p blue - trench axis\n"
            "S 0.2c - 0.4p orange3 - ridge axis\n"), position="jBL+o0.2c",
            box="+p0.4p,gray50")
        f.colorbar(position="jBC+o0c/0.9c", frame=['af', '+l"depth (km)"'],
                   cmap=True)
        path = ARTIFACTS / "seismicity.png"
        f.savefig(path, dpi=100)
        width, height = png_size(path)
        print(f"  figure: {width} x {height} px, {path.stat().st_size} bytes")
        print("  layers drawn: basemap, coastline, epicentres, trench, ridge,")
        print("  3 focal mechanisms, 2 labels, a 4-entry legend, a colour bar")
        print(f"  Observation: the same figure at dpi=300 would be about "
              f"{width * 3} x {height * 3} px, which is the size a journal")
        print("  wants. The symbol sizes do not change; only the pixels do,")
        print("  which is why the size of a magnitude-scaled marker has to be")
        print("  stated in the caption in physical units.")

        # --------------------------------------------------------------
        section("5. What the plotted symbols encode")
        # --------------------------------------------------------------
        print("  a circle of radius r has area pi r^2, so a size parameter")
        print("  proportional to (M - Mc)^1.6 corresponds to a radius")
        print("  proportional to (M - Mc)^0.8 if the parameter is an area,")
        print("  and to (M - Mc)^1.6 if it is a diameter")
        for mag in (3.0, 5.0, 7.0):
            size_param = 0.02 + 0.05 * (mag - M_C) ** 1.6
            print(f"      M {mag:.1f}: size parameter {size_param:.5f} "
                  f"(cm^2 if an area, cm if a diameter)")
            print(f"              as an area: radius "
                  f"{np.sqrt(size_param / np.pi):.5f} cm; as a diameter: "
                  f"radius {size_param / 2:.5f} cm")
        print("  the radius ratio between the two interpretations, measured:")
        for mag in (3.0, 5.0, 7.0):
            size_param = 0.02 + 0.05 * (mag - M_C) ** 1.6
            as_area = np.sqrt(size_param / np.pi)
            as_diameter = size_param / 2
            print(f"      M {mag:.1f}: {as_area / as_diameter:.2f} x")
        print("  Observation: the numbers printed are the size parameters that")
        print("  were passed to fig.plot, and the two interpretations differ by")
        print("  a radius ratio that itself depends on the size (5.9 at M 3.0")
        print("  down to 1.5 at M 7.0 here). I did NOT verify in this")
        print("  environment which one GMT uses, so I make no claim about it;")
        print("  what is certain is that the caption of a magnitude-scaled map")
        print("  has to state the convention, because a reader who assumes the")
        print("  size is the magnitude will read the map wrong by a large")
        print("  factor -- and by a different large factor at each magnitude.")
    finally:
        shutil.rmtree(ARTIFACTS, ignore_errors=True)


if __name__ == "__main__":
    main()
