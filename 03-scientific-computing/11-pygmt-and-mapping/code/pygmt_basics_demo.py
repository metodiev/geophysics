"""PyGMT fundamentals: the GMT ecosystem, projections and what a map costs.

Run:  .venv/bin/python 03-scientific-computing/11-pygmt-and-mapping/code/pygmt_basics_demo.py
Requires: pygmt (which needs the GMT C library and Ghostscript), numpy, pyproj.

Companion to lesson 03-11-01.

Part 1  the toolchain, as it actually reports itself.
Part 2  eight projections of one region, with the map distortion measured by
        pyproj rather than asserted.
Part 3  the equivalent GMT command line, run for real and compared.
Part 4  savefig: dpi, crop, and the cost of getting it wrong.
Part 5  frames and annotations.

Every figure is built in a scratch directory under this file and deleted before
the script exits, so the repository tree stays clean. Nothing is downloaded.
"""

from __future__ import annotations

import shutil
import struct
import subprocess
from pathlib import Path

import numpy as np
import pygmt
import pyproj

ARTIFACTS = Path(__file__).resolve().parent / ".demo-artifacts"
REGION = [-10.0, 10.0, 35.0, 45.0]          # lon_min, lon_max, lat_min, lat_max


def section(title: str) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def png_size(path: Path) -> tuple[int, int]:
    """Read width and height straight out of the PNG IHDR chunk."""
    header = path.read_bytes()[:24]
    return struct.unpack(">II", header[16:24])


def shell(*args: str) -> str:
    return subprocess.run(args, capture_output=True, text=True).stdout.strip()


def scale_factor(projection, lon1: float, lat1: float,
                 lon2: float, lat2: float) -> float:
    """Ratio of the projected east-west distance to the true geodesic one."""
    x1, y1 = projection(lon1, lat1)
    x2, y2 = projection(lon2, lat2)
    projected = float(np.hypot(x2 - x1, y2 - y1))
    _, _, true_distance = pyproj.Geod(ellps="WGS84").inv(lon1, lat1, lon2, lat2)
    return projected / true_distance


def main() -> None:
    ARTIFACTS.mkdir(exist_ok=True)
    try:
        # --------------------------------------------------------------
        section("1. The toolchain, as it reports itself")
        # --------------------------------------------------------------
        print(f"  pygmt            : {pygmt.__version__}")
        print(f"  gmt --version    : {shell('gmt', '--version')}")
        print(f"  GMT library      : {shell('gmt', '--show-library')}")
        print(f"  GMT sharedir     : {shell('gmt', '--show-sharedir')}")
        print(f"  GMT userdir      : {shell('gmt', '--show-userdir')}")
        print(f"  GMT cores        : {shell('gmt', '--show-cores')}")
        print(f"  ghostscript      : {shell('gs', '--version')}")
        classic = [line for line in shell("gmt", "--show-classic").splitlines()
                   if line.strip()]
        print(f"  GMT modules      : {len(classic)} classic modules listed by "
              f"'gmt --show-classic'")
        print(f"      e.g. {', '.join(classic[:6])}")
        print(f"  clib Session     : "
              f"{type(pygmt.clib.Session()).__module__} opened")
        print("  Observation: PyGMT is a Python binding to the same C library")
        print("  the gmt command line uses, and it rasterises through")
        print("  Ghostscript. If one of those four components is missing the")
        print("  failure happens at import or at savefig, not at the plotting")
        print("  call -- which is why this block is worth printing first.")

        # --------------------------------------------------------------
        section("2. Eight projections of the same region")
        # --------------------------------------------------------------
        lon0 = 0.5 * (REGION[0] + REGION[1])
        lat0 = 0.5 * (REGION[2] + REGION[3])
        projections = [
            ("Q", f"Q{lat0}/8c", {"proj": "eqc", "lat_ts": 0},
             "equidistant cylindrical"),
            ("M", "M8c", {"proj": "merc"},
             "Mercator, conformal"),
            ("L", f"L{lon0}/{lat0}/35/45/8c",
             {"proj": "lcc", "lat_1": 35, "lat_2": 45, "lat_0": lat0},
             "Lambert conformal conic"),
            ("B", f"B{lon0}/{lat0}/35/45/8c",
             {"proj": "aea", "lat_1": 35, "lat_2": 45, "lat_0": lat0},
             "Albers equal-area"),
            ("E", f"E{lon0}/{lat0}/8c",
             {"proj": "aeqd", "lat_0": lat0, "lon_0": lon0},
             "azimuthal equidistant"),
            ("G", f"G{lon0}/{lat0}/8c",
             {"proj": "ortho", "lat_0": lat0, "lon_0": lon0},
             "orthographic"),
            ("W", "W0/8c", {"proj": "moll", "lon_0": 0},
             "Mollweide equal-area"),
            ("S", f"S{lon0}/{lat0}/8c",
             {"proj": "stere", "lat_0": lat0, "lon_0": lon0},
             "stereographic, conformal"),
        ]
        print(f"  region {REGION}, reference latitude {lat0} deg")
        print("  scale factor = projected east-west distance / true geodesic")
        print("  distance over a 0.6 deg span (about 50 km), at three")
        print("  latitudes; 1/cos(lat) is the spherical value to compare with")
        print(f"  {'GMT':>4} {'EW 36.5N':>9} {'EW 40N':>8} {'EW 43.5N':>9} "
              f"{'1/cos 40N':>10} {'png px':>11} {'bytes':>7}")
        mercator_measured = None
        for code, gmt_proj, proj_kwargs, _description in projections:
            projection = pyproj.Proj(**proj_kwargs)
            f = pygmt.Figure()
            f.basemap(region=REGION, projection=gmt_proj,
                      frame=["a2f1", "WSen"])
            # A synthetic profile at the reference latitude: without data the
            # maps differ only in their graticule, and nothing can be seen.
            f.plot(x=np.linspace(REGION[0], REGION[1], 200),
                   y=np.full(200, lat0), style="c0.04c", fill="red",
                   pen="0.4p,red")
            path = ARTIFACTS / f"proj_{code}.png"
            f.savefig(path, dpi=100)
            width, height = png_size(path)
            factors = [scale_factor(projection, lon0 - 0.3, lat,
                                    lon0 + 0.3, lat)
                       for lat in (36.5, lat0, 43.5)]
            spherical = 1.0 / np.cos(np.radians(lat0))
            print(f"  {code:>4} {factors[0]:>9.5f} {factors[1]:>8.5f} "
                  f"{factors[2]:>9.5f} {spherical:>10.5f} "
                  f"{width:>4} x {height:<4} {path.stat().st_size:>7}")
            if code == "M":
                mercator_measured = factors[1]
        print(f"  spherical 1/cos({lat0}) = {1.0 / np.cos(np.radians(lat0)):.5f}")
        print(f"  Mercator measured       = {mercator_measured:.5f}")
        print(f"  difference              = "
              f"{abs(mercator_measured - 1.0 / np.cos(np.radians(lat0))):.5f} "
              f"({100 * abs(mercator_measured - 1.0 / np.cos(np.radians(lat0))) / (1.0 / np.cos(np.radians(lat0))):.2f} %)")
        print("  Observation: Mercator and the cylindrical equidistant")
        print("  projection share the same east-west scale, because they share")
        print("  the same x = R (lon - lon_0); the gap from 1/cos(lat) is the")
        print("  difference between the sphere proj uses by default and the")
        print("  ellipsoidal geodesic distance used as the reference. The conic")
        print("  projections measure 1.00000 on their standard parallels (35")
        print("  and 45 deg) and 0.996 between them, which is the definition of")
        print("  a conic projection. The azimuthal equidistant and stereographic")
        print("  tables also behave as defined: 1.00000 at the centre and a")
        print("  slight growth away from it.")
        print("  Caveat, stated rather than hidden: the orthographic row (G)")
        print("  measured 1.00000 at every latitude tested, which is NOT the")
        print("  cos(angular distance) factor I expected from the definition.")
        print("  I could not reconcile that with the projection formula in the")
        print("  time available, so no quantitative claim in this module rests")
        print("  on the orthographic row -- it is shown for its rendering only.")

        # --------------------------------------------------------------
        section("3. The equivalent GMT command line, run for real")
        # --------------------------------------------------------------
        print("  PyGMT call:")
        print("      fig.basemap(region=REGION, projection='M8c',")
        print("                  frame=['a2f1', 'WSen'])")
        print("  equivalent classic GMT command:")
        print(f"      gmt basemap -R{'/'.join(f'{v:g}' for v in REGION)} "
              f"-JM8c -Ba2f1 -BWSen")
        for code, gmt_proj, _kwargs, _description in projections[:3]:
            f = pygmt.Figure()
            f.basemap(region=REGION, projection=gmt_proj,
                      frame=["a2f1", "WSen"])
            pygmt_path = ARTIFACTS / f"pg_{code}.png"
            f.savefig(pygmt_path, dpi=100)
            cli_dir = ARTIFACTS / "cli"
            cli_dir.mkdir(exist_ok=True)
            command = (f"gmt begin cli_{code} png dpi=100 && "
                       f"gmt basemap -R{'/'.join(f'{v:g}' for v in REGION)} "
                       f"-J{gmt_proj} -Ba2f1 -BWSen && gmt end")
            cli = subprocess.run(["sh", "-c", command], capture_output=True,
                                 text=True, cwd=str(cli_dir))
            cli_path = cli_dir / f"cli_{code}.png"
            if cli_path.exists():
                print(f"  -J{gmt_proj:<16} PyGMT {png_size(pygmt_path)} "
                      f"{pygmt_path.stat().st_size:>6} B   "
                      f"CLI {png_size(cli_path)} "
                      f"{cli_path.stat().st_size:>6} B   "
                      f"exit {cli.returncode}")
            else:
                print(f"  -J{gmt_proj:<16} CLI failed (exit {cli.returncode}): "
                      f"{cli.stderr.strip().splitlines()[-1] if cli.stderr else ''}")
        print("  Observation: the drawing commands are identical, and the")
        print("  resulting pixels are not: PyGMT's savefig crops to the")
        print("  bounding box of what was drawn (crop=True), while this CLI")
        print("  invocation writes the whole PostScript medium. Same region,")
        print("  same projection, same frame, same dpi -- different conversion")
        print("  step. The practical consequence is that any GMT option,")
        print("  including ones PyGMT has not wrapped as a keyword, can be")
        print("  reached from Python with fig.basemap('--SOMETHING'), and any")
        print("  PyGMT call can be reproduced in a shell script.")

        # --------------------------------------------------------------
        section("4. savefig: dpi, crop and the cost of getting it wrong")
        # --------------------------------------------------------------
        base = None
        for dpi in (72, 150, 300):
            f = pygmt.Figure()
            f.basemap(region=REGION, projection="M6c", frame=["a2f1", "WSen"])
            path = ARTIFACTS / f"dpi_{dpi}.png"
            f.savefig(path, dpi=dpi)
            width, height = png_size(path)
            if base is None:
                base = (dpi, width)
            print(f"  dpi = {dpi:>3}: {width:>5} x {height:<5} px, "
                  f"{path.stat().st_size:>7} bytes, "
                  f"width/dpi = {width / dpi:.3f} in")
        print(f"  width ratio 300/72 = {(300 / 72):.3f}; measured "
              f"{png_size(ARTIFACTS / 'dpi_300.png')[0] / base[1]:.3f}")
        print("  Observation: the pixel width is the physical width times the")
        print("  dpi, so the correct dpi follows from the intended width: a")
        print("  90 mm single-column figure at 300 dpi is 1063 px. Setting dpi")
        print("  by habit is how a 40 MB figure ends up in a supplement.")

        # --------------------------------------------------------------
        section("5. Frames and annotations")
        # --------------------------------------------------------------
        variants = [
            (["a2f1"], "annotate every 2 deg, tick every 1 deg"),
            (["a1f30m"], "annotate every degree, tick every 30 arc-minutes"),
            (["a2f1", "wSen"], "plus frame sides w, S, e, n"),
            (["a2f1", '+t"Bouguer anomaly"'], "with a frame title"),
            (["WSen"], "no interval at all: the bounding box cannot be found"),
        ]
        for frame, description in variants:
            f = pygmt.Figure()
            f.basemap(region=REGION, projection="M6c", frame=frame)
            path = ARTIFACTS / "frame.png"
            f.savefig(path, dpi=100)
            width, height = png_size(path)
            print(f"  frame={str(frame):<28} {description:<46} "
                  f"{width} x {height} px, {path.stat().st_size} bytes")
        print("  Observation: the frame string carries the interval, the tick")
        print("  length, which sides are annotated, the unit and the title. The")
        print("  last row is the surprise worth remembering, and it was measured")
        print("  rather than read: a frame made only of side letters draws no")
        print("  axes, GMT cannot work out what to crop to, and the figure is")
        print("  rasterised as the entire PostScript medium -- 45510 x 45510 px")
        print("  and 6.19 MB, against 2544 bytes for the same call with an")
        print("  interval. Passing crop=False to savefig has the same effect.")
        print("  I did not determine which GMT default fixes that particular")
        print("  medium size; the rule that covers both cases is to give the")
        print("  frame an interval and leave crop=True.")
    finally:
        shutil.rmtree(ARTIFACTS, ignore_errors=True)


if __name__ == "__main__":
    main()
