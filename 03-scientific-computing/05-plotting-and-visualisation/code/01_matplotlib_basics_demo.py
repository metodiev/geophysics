"""Matplotlib figure/axes model and the anatomy of a plot.

Run:  .venv/bin/python 01_matplotlib_basics_demo.py
Requires: numpy, matplotlib (headless Agg backend).

Companion to lesson 03-05-01.

The script contrasts the two Matplotlib entry points -- the pyplot "state
machine" and the explicit object-oriented Figure/Axes API -- and counts the
objects each one creates, so the difference is measured rather than asserted.
It then labels every part of a plot that a reader needs, saves one figure at
three dots-per-inch settings to show that the pixel count is
(physical size in inches) x (dots per inch), and builds a shared-axis subplot
grid.

All numeric output is computed here. Data are synthetic and labelled as such.
No figure is written into the repository: images go to a temporary directory,
whose path is printed.
"""

import os
import tempfile

import matplotlib

matplotlib.use("Agg")  # headless: no window, so the script cannot block
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

OUTDIR = tempfile.mkdtemp(prefix="plotting_demo01_")


def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


def part1_state_machine_vs_oo():
    section("1. The pyplot state machine versus the object-oriented API")

    # --- pyplot state machine: implicit current figure and current axes ---
    plt.figure()
    print("after plt.figure():           fignums =", plt.get_fignums())
    plt.plot([0, 1, 2], [0, 1, 4])
    ax = plt.gca()
    print("after plt.plot(...):          current axes has",
          len(ax.lines), "line(s),", len(ax.collections), "collection(s)")
    print("   plt.gca() is the only handle on that axes: it was never named.")

    # Every further plt.* call acts on whatever is 'current'. Create a second
    # figure and watch the implicit pointer move.
    plt.figure()
    plt.plot([0, 1, 2], [4, 1, 0])
    print("after a second plt.figure():  fignums =", plt.get_fignums())
    print("number of axes on the *current* figure:",
          len(plt.gcf().axes))

    # --- object-oriented API: every object is named and addressable ---
    fig, ax = plt.subplots()
    ax.plot([0, 1, 2], [0, 1, 4], color="C0", label="explicit")
    print("OO: fig and ax are ordinary Python names;",
          "type(fig) =", type(fig).__name__ + ",", "type(ax) =", type(ax).__name__)

    n_fig = len(plt.get_fignums())
    print(f"\nfigures created so far (both APIs share one registry): {n_fig}")
    print("Total Axes in existence:",
          sum(len(plt.figure(i).axes) for i in plt.get_fignums()))

    plt.close("all")
    print("after plt.close('all'):       fignums =", plt.get_fignums())
    print()
    print("Consequence: the state machine is fine for a throwaway inspection,")
    print("but as soon as a second figure exists, 'plt.something' is ambiguous")
    print("about which axes it means. Naming fig and ax removes the ambiguity.")


def part2_anatomy():
    section("2. Anatomy of a plot: every element a reader needs")

    x = np.linspace(0.0, 10.0, 200)
    y = np.sin(x) * np.exp(-x / 8.0)

    fig, ax = plt.subplots(figsize=(6.0, 4.0), dpi=150)
    ax.plot(x, y, color="C0", linewidth=1.8, label="damped oscillation")
    ax.fill_between(x, y - 0.05, y + 0.05, color="C0", alpha=0.25,
                    linewidth=0, label=r"$\pm 0.05$ envelope (SYNTHETIC)")

    ax.set_title("Anatomy of a scientific plot")
    ax.set_xlabel("time t (s)")
    ax.set_ylabel("amplitude a (arb. units)")
    ax.set_xlim(0.0, 10.0)
    ax.set_ylim(-1.1, 1.1)
    ax.grid(True, which="major", linewidth=0.5, alpha=0.4)
    ax.legend(loc="upper right", frameon=False)
    ax.annotate("first zero crossing\nat t = pi",
                xy=(np.pi, 0.0), xytext=(4.4, 0.55),
                arrowprops=dict(arrowstyle="->", linewidth=0.8))
    ax.text(0.02, 0.04, "SYNTHETIC data", transform=ax.transAxes,
            fontsize=7, color="0.4", va="bottom")

    path = os.path.join(OUTDIR, "01_anatomy.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    print(f"saved {os.path.basename(path)} at dpi=150")

    print()
    print("artist inventory of this Axes")
    print(f"  title text        : {ax.get_title()!r}")
    print(f"  x label           : {ax.get_xlabel()!r}")
    print(f"  y label           : {ax.get_ylabel()!r}")
    print(f"  number of Line2D  : {len(ax.lines)}")
    print(f"  number of PolyColl: {len(ax.collections)}  (the fill_between band)")
    print(f"  legend entries    : {len(ax.get_legend().get_texts())}")
    print(f"  annotations       : {len(ax.texts)} Text artists (annotate + label)")
    print(f"  visible spines    : {[k for k, s in ax.spines.items() if s.get_visible()]}")
    plt.close(fig)


def part3_dpi_and_pixels():
    section("3. Dots per inch sets pixels: pixels = inches x dpi")

    from PIL import Image  # Pillow ships with Matplotlib's dependency set

    w_in, h_in = 6.4, 4.8
    t = np.linspace(0, 2 * np.pi, 1000)
    for dpi in (72, 150, 300):
        fig, ax = plt.subplots(figsize=(w_in, h_in), dpi=dpi)
        ax.plot(t, np.sin(3 * t) + 0.15 * t)
        ax.set_xlabel("t (rad)")
        ax.set_ylabel("signal (arb. units)")
        stem = f"01_dpi{dpi}.png"
        path = os.path.join(OUTDIR, stem)
        fig.savefig(path)
        plt.close(fig)
        with Image.open(path) as im:  # measured from the file on disk
            W, H = im.size
        print(f"  figsize=({w_in}, {h_in}) in, dpi={dpi:>3}  ->  file {W:>4} x {H:>4} px"
              f"  = {W * H / 1e6:6.3f} Mpx  ({os.path.getsize(path) / 1024:7.1f} kB)")

    print()
    print("The physical size is fixed; raising dpi raises the raster resolution")
    print("of the same layout. Vector formats (PDF, SVG) carry no dpi at all and")
    print("are resolution-independent, at the cost of larger files and font")
    print("requirements on the reader's machine.")

    fig, ax = plt.subplots(figsize=(w_in, h_in))
    ax.plot(t, np.sin(3 * t) + 0.15 * t)
    ax.set_xlabel("t (rad)")
    ax.set_ylabel("signal (arb. units)")
    pdf = os.path.join(OUTDIR, "01_vector.pdf")
    svg = os.path.join(OUTDIR, "01_vector.svg")
    fig.savefig(pdf)
    fig.savefig(svg)
    plt.close(fig)
    blob = open(pdf, "rb").read()
    has_raster = b"/Subtype /Image" in blob
    print(f"  {os.path.basename(pdf)}: {len(blob) / 1024:.1f} kB, "
          f"contains a raster image object: {has_raster}")
    print(f"  {os.path.basename(svg)}: {os.path.getsize(svg) / 1024:.1f} kB, "
          f"text as glyph paths/strings: {'<path' in open(svg, encoding='utf-8', errors='ignore').read()}")


def part4_subplot_grid():
    section("4. A shared-axis grid: one panel per trace, aligned by construction")

    t = np.linspace(0, 1.0, 500)
    rng = np.random.default_rng(20240401)  # named seed -> reproducible
    fig, axes = plt.subplots(3, 1, figsize=(7.0, 5.0), sharex=True, dpi=150)
    print("fig, axes = plt.subplots(3, 1, sharex=True)")
    print("  type(axes)      =", type(axes).__name__)
    print("  axes.shape      =", axes.shape)
    print("  axes[0] is axes.flat[0]:", axes[0] is axes.flat[0])
    for i, ax in enumerate(axes):
        noisy = np.sin(2 * np.pi * (i + 1) * t) + 0.08 * rng.standard_normal(t.size)
        ax.plot(t, noisy, linewidth=0.7)
        ax.set_ylabel(f"ch {i + 1}")
        ax.grid(True, linewidth=0.4, alpha=0.35)
    axes[-1].set_xlabel("time t (s)")
    axes[0].set_title("Stacked channels, shared time axis")
    path = os.path.join(OUTDIR, "01_grid.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    print(f"  saved {os.path.basename(path)}")
    print("  sharex=True makes the axes physically aligned: the vertical guide")
    print("  lines a reader draws with their eye correspond to one instant in all")
    print("  three channels. Sub-panels placed by hand cannot guarantee that.")
    plt.close(fig)


def main():
    part1_state_machine_vs_oo()
    part2_anatomy()
    part3_dpi_and_pixels()
    part4_subplot_grid()
    print()
    print("Images written to:", OUTDIR)
    print("Nothing was written inside the repository.")


if __name__ == "__main__":
    main()
