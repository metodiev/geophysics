"""Layout, insets, legends and multi-panel maps with PyGMT.

Run:  .venv/bin/python 03-scientific-computing/11-pygmt-and-mapping/code/inset_and_layout_demo.py
Requires: pygmt (needs GMT and Ghostscript), numpy, pyproj.

Companion to lesson 03-11-04.

Part 1  a 2 x 2 panel figure built with shift_origin, and the canvas it
        actually produces.
Part 2  a scale bar whose length is computed for the map's latitude.
Part 3  an inset, and the area it takes from the parent map.
Part 4  a legend from a spec file, and the layout arithmetic of a caption.
Part 5  the whole figure: what is measured and what is chosen.

Figures are built in a scratch directory and deleted before exit.
"""

from __future__ import annotations

import io
import shutil
import struct
from pathlib import Path

import numpy as np
import pygmt
import pyproj

ARTIFACTS = Path(__file__).resolve().parent / ".demo-artifacts"
REGION = [-6.0, 6.0, 42.0, 50.0]
PANEL_CM = 8.0
DPI = 100


def section(title: str) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def png_size(path: Path) -> tuple[int, int]:
    return struct.unpack(">II", path.read_bytes()[16:24])


def main() -> None:
    ARTIFACTS.mkdir(exist_ok=True)
    try:
        geod = pyproj.Geod(ellps="WGS84")
        centre_lat = 0.5 * (REGION[2] + REGION[3])

        # --------------------------------------------------------------
        section("1. A 2 x 2 panel figure")
        # --------------------------------------------------------------
        f = pygmt.Figure()
        panels = [("Q", REGION), ("M", REGION), ("R", REGION), ("X", REGION)]
        for index, (label, panel_region) in enumerate(panels):
            if index > 0:
                f.shift_origin(xshift=f"{PANEL_CM + 0.6}c" if index % 2
                               else f"-{PANEL_CM + 0.6}c",
                               yshift="0c" if index % 2 else f"-{PANEL_CM}c")
            f.basemap(region=panel_region,
                      projection=f"Q{centre_lat}/{PANEL_CM}c",
                      frame=["a2f1", "WSen"])
            f.coast(shorelines="0.2p,black", land="gray95",
                    water="lightblue", resolution="crude")
            f.text(x=panel_region[0] + 0.7, y=panel_region[3] - 0.7,
                   text=f"({chr(97 + index)})", font="10p,Helvetica-Bold,black",
                   justify="TL")
        layout_path = ARTIFACTS / "panels.png"
        f.savefig(layout_path, dpi=DPI)
        width, height = png_size(layout_path)
        expected = int(round((2 * PANEL_CM + 0.6) / 2.54 * DPI))
        print(f"  four panels of {PANEL_CM} cm width, 0.6 cm gap, {DPI} dpi")
        print(f"  measured canvas   : {width} x {height} px")
        print(f"  one panel width would be {PANEL_CM} cm = "
              f"{PANEL_CM / 2.54 * DPI:.0f} px")
        print(f"  two panels plus the gap = "
              f"{(2 * PANEL_CM + 0.6) / 2.54 * DPI:.0f} px "
              f"(measured {width} px, difference {width - expected:+d} px)")
        print(f"  the difference is the frame and annotation margin, which GMT")
        print(f"  adds outside the requested map width: a map '8c wide' is")
        print(f"  larger than 8 cm once it has axes")
        print(f"  bytes: {layout_path.stat().st_size}")
        print("  Observation: shift_origin translates the current origin, and")
        print("  the canvas follows the drawing rather than the other way round.")
        print("  A panel figure is therefore laid out by arithmetic on the")
        print("  panel width, and the number that matters is the pixel width of")
        print("  the final canvas -- which is what has to be checked against the")
        print("  journal's column width before the figure is submitted.")

        # --------------------------------------------------------------
        section("2. A scale bar computed for the map's latitude")
        # --------------------------------------------------------------
        km_per_degree = geod.inv(0.0, centre_lat, 1.0, centre_lat)[2] / 1000.0
        print(f"  at {centre_lat:.1f} deg N one degree of longitude is "
              f"{km_per_degree:.4f} km")
        map_width_km = geod.inv(REGION[0], centre_lat, REGION[1],
                                centre_lat)[2] / 1000.0
        print(f"  the map spans {map_width_km:.1f} km east-west at that "
              f"latitude, over {PANEL_CM} cm of paper")
        for bar_km in (100.0, 250.0, 500.0, 1000.0):
            print(f"      a {bar_km:>6.0f} km bar is "
                  f"{bar_km / km_per_degree:6.3f} deg of longitude and "
                  f"{100 * bar_km / map_width_km:5.1f} % of the map width")
        f = pygmt.Figure()
        f.basemap(region=REGION, projection=f"Q{centre_lat}/{PANEL_CM}c",
                  frame=["a2f1", "WSen"])
        f.coast(shorelines="0.2p,black", resolution="crude")
        scalebar_position = pygmt.params.Position("BL", offset=(0.6, 0.6))
        print(f"  pygmt.params.Position('BL', offset=(0.6, 0.6)) renders as "
              f"'{scalebar_position}'")
        f.scalebar(position=scalebar_position, length="250k", fancy=True,
                   unit=True, box="+p0.4p,gray30")
        bar_path = ARTIFACTS / "scalebar.png"
        f.savefig(bar_path, dpi=DPI)
        print(f"  with the scale bar: {png_size(bar_path)} px, "
              f"{bar_path.stat().st_size} bytes")
        f2 = pygmt.Figure()
        f2.basemap(region=REGION, projection=f"Q{centre_lat}/{PANEL_CM}c",
                   frame=["a2f1", "WSen"])
        f2.coast(shorelines="0.2p,black", resolution="crude")
        plain_path = ARTIFACTS / "noscalebar.png"
        f2.savefig(plain_path, dpi=DPI)
        print(f"  without it:        {png_size(plain_path)} px, "
              f"{plain_path.stat().st_size} bytes")
        print(f"  the bar therefore costs "
              f"{bar_path.stat().st_size - plain_path.stat().st_size} bytes of "
              f"PNG and occupies about {100 * 250.0 / map_width_km:.1f} % of "
              f"the map width")
        print(f"  a 1000 km bar would be wider than this map; the table above is")
        print(f"  how that is noticed before the figure is drawn")
        print("  Observation: a scale bar is a length in kilometres drawn on a")
        print("  projection, so it is only exact if the projection has a")
        print("  constant scale -- which is why the equidistant cylindrical")
        print("  projection above is the honest choice for a regional map with")
        print("  a bar on it, and why the bar on a Mercator map is only valid")
        print("  at the latitude at which it was drawn.")

        # --------------------------------------------------------------
        section("3. An inset, and the area it takes")
        # --------------------------------------------------------------
        inset_region = [-14.0, 14.0, 34.0, 58.0]
        inset_width_cm = 3.0
        f = pygmt.Figure()
        f.basemap(region=REGION, projection="M10c", frame=["a2f1", "WSen"])
        f.coast(shorelines="0.3p,black", land="gray90", water="lightblue",
                resolution="crude")
        f.inset(position="jBR+o0.25c+w3c", box="+p0.5p,gray20")
        f.basemap(region=inset_region, projection=f"M{inset_width_cm}c",
                  frame=["a10f5", "WSen"])
        f.coast(shorelines="0.2p", land="gray80", water="lightblue",
                resolution="crude")
        f.plot(x=[REGION[0], REGION[1], REGION[1], REGION[0], REGION[0]],
               y=[REGION[2], REGION[2], REGION[3], REGION[3], REGION[2]],
               pen="1p,red")
        inset_path = ARTIFACTS / "inset.png"
        f.savefig(inset_path, dpi=DPI)
        main_width_deg = REGION[1] - REGION[0]
        inset_width_deg = inset_region[1] - inset_region[0]
        main_height_deg = REGION[3] - REGION[2]
        inset_height_deg = inset_region[3] - inset_region[2]
        main_km2 = (main_width_deg * km_per_degree) * (main_height_deg * 111.32)
        inset_km2 = (inset_width_deg * km_per_degree) * (inset_height_deg * 111.32)
        print(f"  main map  : {REGION}, {main_width_deg:.0f} x "
              f"{main_height_deg:.0f} deg, about {main_km2:,.0f} km^2")
        print(f"  inset     : {inset_region}, {inset_width_deg:.0f} x "
              f"{inset_height_deg:.0f} deg, about {inset_km2:,.0f} km^2")
        print(f"  the inset therefore shows {inset_km2 / main_km2:.2f} times the")
        print(f"  area of the main map, in a box {inset_width_cm} cm wide against "
              f"10 cm -- which is the ratio that decides whether the locator")
        print(f"  is helpful or pointless")
        print(f"  measured canvas: {png_size(inset_path)} px, "
              f"{inset_path.stat().st_size} bytes")
        print("  Observation: an inset is usually a locator, so its job is to")
        print("  show where the study area is and not to be read for detail.")
        print(f"  The measured ratio here is {inset_km2 / main_km2:.1f}: the")
        print("  inset covers seven times the area of the region it is")
        print("  locating, which is enough context to be useful. Push that")
        print("  ratio towards 1 and the locator adds nothing.")

        # --------------------------------------------------------------
        section("4. A legend from a spec file")
        # --------------------------------------------------------------
        spec = io.StringIO(
            "H 9p,Helvetica-Bold Symbols\n"
            "G 0.05c\n"
            "S 0.25c c 0.08c red 0.2p - recorded event\n"
            "S 0.25c c 0.08c blue 0.2p - relocated event\n"
            "S 0.25c - 0.5p orange3 - proposed profile\n"
            "D 0.2p\n"
            "T station spacing 250 m\n")
        spec_text = spec.getvalue()
        f = pygmt.Figure()
        f.basemap(region=REGION, projection="M10c", frame=["a2f1", "WSen"])
        f.coast(shorelines="0.3p,black", resolution="crude")
        legend_position = pygmt.params.Position("TR", offset=0.2)
        print(f"  legend position object renders as '{legend_position}'")
        f.legend(spec=spec, position=legend_position, width="5c",
                 box="+p0.5p,gray30")
        f.colorbar(position="jBC+o0c/0.8c", frame=['af', '+l"mGal"'],
                   cmap="batlow")
        legend_path = ARTIFACTS / "legend.png"
        f.savefig(legend_path, dpi=DPI)
        lines = [line for line in spec_text.splitlines() if line.strip()]
        print(f"  legend spec: {len(lines)} non-empty lines")
        for line in lines:
            print(f"      {line}")
        print(f"  measured canvas: {png_size(legend_path)} px, "
              f"{legend_path.stat().st_size} bytes")
        print(f"  the legend is placed at the top right, offset 0.2 cm, so it")
        print(f"  moves with the frame instead of sitting at fixed paper")
        print(f"  coordinates -- which is what the 'j' in 'jTR' means")
        print("  Observation: the spec is a small language of its own -- H for a")
        print("  header, S for a symbol, D for a dividing line, T for plain")
        print("  text, G for a gap -- and the codes G and T only work once the")
        print("  legend has a width, which is the (-D...+w) that GMT asked for")
        print("  in its error message. Writing the spec as a string inside the")
        print("  analysis script means the legend is regenerated with the")
        print("  figure and cannot go stale.")

        # --------------------------------------------------------------
        section("5. The whole figure, and what is chosen")
        # --------------------------------------------------------------
        f = pygmt.Figure()
        f.basemap(region=REGION, projection="M10c", frame=["a2f1", "WSen"])
        f.coast(shorelines="0.3p,black", land="gray90", water="lightblue",
                resolution="crude")
        rng = np.random.default_rng(20261014)
        x = rng.uniform(REGION[0], REGION[1], 150)
        y = rng.uniform(REGION[2], REGION[3], 150)
        z = rng.normal(0.0, 1.0, 150)
        f.plot(x=x, y=y, style="cc", size=0.02 + 0.06 * np.abs(z),
               fill="red@40", pen="0.1p,black")
        f.scalebar(position=pygmt.params.Position("BL", offset=(0.5, 0.5)),
                   length="500k", fancy=True, unit=True,
                   box="+p0.4p,gray30")
        f.legend(spec=io.StringIO(
            "H 9p,Helvetica-Bold Stations\n"
            "S 0.25c c 0.08c red@40 0.2p - n = 150\n"),
            position=pygmt.params.Position("TR", offset=0.2), width="5c",
            box="+p0.5p,gray30")
        f.inset(position="jBR+o0.25c+w3c", box="+p0.5p,gray20")
        f.basemap(region=inset_region, projection=f"M{inset_width_cm}c",
                  frame=["a10f5", "WSen"])
        f.coast(shorelines="0.2p", land="gray80", resolution="crude")
        f.plot(x=[REGION[0], REGION[1], REGION[1], REGION[0], REGION[0]],
               y=[REGION[2], REGION[2], REGION[3], REGION[3], REGION[2]],
               pen="1p,red")
        full_path = ARTIFACTS / "full.png"
        f.savefig(full_path, dpi=DPI)
        width, height = png_size(full_path)
        print(f"  final canvas: {width} x {height} px at {DPI} dpi = "
              f"{width / DPI * 2.54:.2f} x {height / DPI * 2.54:.2f} cm")
        print(f"  bytes: {full_path.stat().st_size}")
        print(f"  elements drawn: frame, coastline, 150 stations, scale bar,")
        print(f"  legend, inset with a locator rectangle")
        print(f"  measured bytes per element, against the bare map "
              f"({png_size(plain_path)[0]} x {png_size(plain_path)[1]} px, "
              f"{plain_path.stat().st_size} bytes):")
        print(f"      full figure / bare map = "
              f"{full_path.stat().st_size / plain_path.stat().st_size:.2f} x "
              f"the file size")
        print("  Observation: every element above is a decision with a number")
        print("  attached -- the map width in cm, the dpi, the bar length in")
        print("  km, the inset's extent -- and each one can be checked against")
        print("  the journal's requirements before submission. A figure is")
        print("  finished when those numbers are recorded with it, not when it")
        print("  looks right on the screen.")
    finally:
        shutil.rmtree(ARTIFACTS, ignore_errors=True)


if __name__ == "__main__":
    main()
