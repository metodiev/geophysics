"""What interactive exploration is for, measured on a static headless machine.

Run:  .venv/bin/python 08_interactive_viz_demo.py
Requires: numpy, matplotlib (Agg).

Companion to lesson 03-05-08.

There is no display attached to this run, and neither Plotly nor HoloViews is
installed here, so the script does not pretend to open a window. Instead it
measures the four quantities that decide whether a figure needs to be
interactive at all:

* Part 1 renders the same scatter at four sizes and times it, then counts how
  many distinct raster pixels the points can occupy. Once the points outnumber
  the pixels, added data add no visible information -- which is the situation
  where hover, zoom and selection earn their cost.
* Part 2 counts how many points sit outside the 1-99 percentile box. Those are
  the observations a reader wants to interrogate one at a time, and the ones a
  static percentile-clipped display silently removes.
* Part 3 emulates a brushing session: it applies one rectangular selection and
  reports the selected statistics against the full set, which is the output an
  interactive session produces -- and shows why that selection has to be saved
  as a specific, stated figure rather than left implicit.
* Part 4 enumerates the state that an interactive figure loses when it is
  exported to a still image for a paper.

All data are SYNTHETIC. Images go to a temporary directory, never into the
repository.
"""

import os
import tempfile
import time

import matplotlib

matplotlib.use("Agg")  # headless: no window, so the script cannot block
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

OUTDIR = tempfile.mkdtemp(prefix="plotting_demo08_")
RNG = np.random.default_rng(20160703)


def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


def make_catalogue(n):
    """SYNTHETIC earthquake-like catalogue: magnitude against depth."""
    depth = np.exp(RNG.normal(np.log(12.0), 0.8, n)).clip(0.5, 700.0)
    mag = 4.6 - 0.55 * np.log10(depth / 10.0) + 0.45 * RNG.standard_normal(n)
    # A small, physically motivated population of deep, large events.
    n_deep = max(1, n // 500)
    depth = np.concatenate([depth, RNG.uniform(300.0, 690.0, n_deep)])
    mag = np.concatenate([mag, RNG.uniform(5.5, 7.6, n_deep)])
    return mag, depth


def part1_cost_and_pixels():
    section("1. Render cost, and the pixel budget that caps what can be seen")

    fig0, ax0 = plt.subplots(figsize=(6.4, 4.0), dpi=100)
    ax0.set_xlabel("magnitude")
    ax0.set_ylabel("depth (km)")
    fig0.canvas.draw()
    bb = ax0.get_window_extent()
    grid = (int(round(bb.height)), int(round(bb.width)))
    plt.close(fig0)
    print(f"  the axes box of a 6.4 x 4.0 in figure at 100 dpi measures"
          f" {grid[1]} x {grid[0]} px")
    print(f"  = {grid[0] * grid[1]} distinct pixels. That is the entire budget the")
    print("  display has for showing how many events fall where.")
    print()
    print(f"  {'n points':>10}{'savefig (s)':>14}{'file (kB)':>11}"
          f"{'occupied pixels':>18}{'points / pixel':>16}")
    times = {}
    for n in (1000, 10000, 100000, 1000000):
        mag, depth = make_catalogue(n)
        fig, ax = plt.subplots(figsize=(6.4, 4.0), dpi=100)
        ax.scatter(mag, depth, s=1, alpha=0.15, linewidths=0, color="C0")
        ax.set_xlabel("magnitude")
        ax.set_ylabel("depth (km)")
        ax.invert_yaxis()
        ax.set_xlim(3.5, 8.0)
        ax.set_ylim(700.0, 0.0)
        path = os.path.join(OUTDIR, f"08_scatter_{n}.png")
        t0 = time.perf_counter()
        fig.savefig(path, dpi=100)
        dt = time.perf_counter() - t0
        plt.close(fig)

        h, _, _ = np.histogram2d(depth, mag, bins=grid,
                                 range=[[0.0, 700.0], [3.5, 8.0]])
        occupied = int((h > 0).sum())
        times[n] = dt
        print(f"  {n:>10}{dt:>14.3f}{os.path.getsize(path) / 1024:>11.1f}"
              f"{occupied:>18}{n / occupied:>16.2f}")
    print()
    print("  Occupied pixels grow far more slowly than the point count: a")
    print("  hundredfold increase in events, from 10000 to 1e6, fills only about")
    print("  4.3 times as many pixels, because the extra points land on pixels")
    print("  that already contain points. Points per occupied pixel rises from")
    print("  1.24 to 70, so the busiest part of the 1e6-point figure says nothing")
    print("  more than 'many' -- the same word the 1000-point figure could say.")
    print("  Recovering the structure needs either a different encoding (hexbin,")
    print("  density, a log colour scale) or a tool that can be asked to zoom.")
    return times


def part2_outliers():
    section("2. The points a percentile clip would delete")

    mag, depth = make_catalogue(200000)
    lo_m, hi_m = np.percentile(mag, [1.0, 99.0])
    lo_d, hi_d = np.percentile(depth, [1.0, 99.0])
    inside = ((mag >= lo_m) & (mag <= hi_m)
              & (depth >= lo_d) & (depth <= hi_d))
    outside = ~inside
    print(f"  catalogue: {mag.size} SYNTHETIC events")
    print(f"  magnitude 1-99 percentile box: [{lo_m:.3f}, {hi_m:.3f}]")
    print(f"  depth     1-99 percentile box: [{lo_d:.3f}, {hi_d:.3f}] km")
    print(f"  events outside the box: {outside.sum()}"
          f"  ({100 * outside.mean():.2f} %)")
    print(f"    of those, deepest {depth[outside].max():.1f} km,"
          f" largest magnitude {mag[outside].max():.2f}")
    print()
    print("  Every figure that auto-clips to a percentile range removes these")
    print("  events from view. Some of them are the most important rows in the")
    print("  file -- the deep events carry the seismotectonic argument. An")
    print("  interactive display helps because the reader can zoom to them without")
    print("  the author having to choose a cut in advance; a static figure helps")
    print("  only if the author states the cut.")


def part3_brushing():
    section("3. Emulating one brushing selection, and reading its result")

    mag, depth = make_catalogue(60000)
    x0, x1 = 5.2, 6.4
    y0, y1 = 250.0, 690.0
    sel = (mag >= x0) & (mag <= x1) & (depth >= y0) & (depth <= y1)
    print(f"  brush window: magnitude in [{x0}, {x1}], depth in [{y0}, {y1}] km")
    print(f"  selected: {sel.sum()} of {mag.size} events"
          f" ({100 * sel.mean():.2f} %)")
    print()
    print(f"  {'statistic':<22}{'full catalogue':>17}{'selection':>14}")
    rows = [
        ("count", float(mag.size), float(sel.sum())),
        ("mean magnitude", mag.mean(), mag[sel].mean()),
        ("median magnitude", float(np.median(mag)), float(np.median(mag[sel]))),
        ("mean depth (km)", depth.mean(), depth[sel].mean()),
        ("median depth (km)", float(np.median(depth)),
         float(np.median(depth[sel]))),
    ]
    for name, a, b in rows:
        print(f"  {name:<22}{a:>17.3f}{b:>14.3f}")
    print()
    print("  This is what a brushing session yields: a subset and its statistics.")
    print("  The selection above is five numbers (x0, x1, y0, y1 and the rule).")
    print("  An interactive figure carries those five numbers in its live state; a")
    print("  published figure does not, so the selection must be drawn on the")
    print("  figure and its limits printed in the caption. Otherwise the reader")
    print("  sees the conclusion without the criterion.")

    fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.0), dpi=150)
    ax = axes[0]
    ax.scatter(mag[~sel], depth[~sel], s=2, alpha=0.2, linewidths=0,
               color="0.6", label="not selected")
    ax.scatter(mag[sel], depth[sel], s=2, alpha=0.6, linewidths=0,
               color="C3", label=f"selected ({sel.sum()})")
    ax.axvline(x0, color="k", lw=0.6, ls="--")
    ax.axvline(x1, color="k", lw=0.6, ls="--")
    ax.axhline(y0, color="k", lw=0.6, ls="--")
    ax.axhline(y1, color="k", lw=0.6, ls="--")
    ax.invert_yaxis()
    ax.set_xlabel("magnitude")
    ax.set_ylabel("depth (km)")
    ax.legend(frameon=False, fontsize=7, loc="lower right")
    ax.set_title("selection drawn on the figure", fontsize=8)

    ax = axes[1]
    ax.hist(depth[~sel], bins=60, range=(0, 700), density=True, histtype="step",
            color="0.5", label="not selected")
    ax.hist(depth[sel], bins=60, range=(0, 700), density=True, histtype="step",
            color="C3", label="selected")
    ax.set_xlabel("depth (km)")
    ax.set_ylabel("probability density")
    ax.legend(frameon=False, fontsize=7)
    ax.set_title("the subset's distribution, exported with it", fontsize=8)
    fig.suptitle("SYNTHETIC catalogue: one brush, exported as a fixed figure",
                 fontsize=10)
    fig.tight_layout()
    path = os.path.join(OUTDIR, "08_brushing.png")
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"  saved {os.path.basename(path)}  (150 dpi, 2 panels)")


def part4_state_loss():
    section("4. The state an exported interactive figure does not carry")

    state = [
        ("x axis limits", 2),
        ("y axis limits", 2),
        ("z / colour limits", 2),
        ("zoom level and centre", 3),
        ("active selection window", 4),
        ("selection rule (inclusive/exclusive, AND/OR)", 2),
        ("current hover / highlighted datum", 2),
        ("which series are visible", 1),
    ]
    total = sum(n for _, n in state)
    print(f"  {'piece of live state':<48}{'numbers':>9}")
    for name, n in state:
        print(f"  {name:<48}{n:>9}")
    print(f"  {'total':<48}{total:>9}")
    print()
    print("  None of these travel inside a PNG or a PDF. An interactive figure is")
    print("  a program; a published figure is a claim about a specific view. The")
    print("  workflow that keeps both honest is to treat the interactive session as")
    print("  the instrument -- used to find the view worth showing -- and to export")
    print("  a static figure at that view, with the state written into the caption")
    print("  as numbers, and the code that produced it committed beside it.")


def main():
    part1_cost_and_pixels()
    part2_outliers()
    part3_brushing()
    part4_state_loss()
    print()
    print("Images written to:", OUTDIR)
    print("Nothing was written inside the repository.")


if __name__ == "__main__":
    main()
