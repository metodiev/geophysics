"""Publication-quality figures: physical size, type size, lines and palettes.

Run:  .venv/bin/python 07_publication_figures_demo.py
Requires: numpy, matplotlib (Agg).

Companion to lesson 03-05-07.

A journal does not accept a figure, it accepts a physical object of specified
width, in which every glyph must remain legible. This script works in those
units from the start and measures each requirement:

* Part 1 converts column widths in millimetres to the pixel counts a given dpi
  demands, so "300 dpi" becomes a number of pixels for a specific column.
* Part 2 shows that scaling a finished figure destroys type size, by
  computing the effective point size after reduction.
* Part 3 converts line weights from points to pixels, which is where a
  hairline either survives the rasteriser or disappears.
* Part 4 measures the pairwise perceptual distance (CIE L*a*b*, dE*ab) within
  the Okabe-Ito colour-blind-safe palette and within Matplotlib's default
  colour cycle, and reports the smallest lightness gap inside each.
* Part 5 checks that a saved PDF really embeds its fonts, by looking for the
  font-program objects in the file.
* Part 6 reports what automatic layout actually moves, by printing the axes
  bounding boxes.

Images go to a temporary directory, never into the repository.
"""

import os
import tempfile

import matplotlib

matplotlib.use("Agg")  # headless: no window, so the script cannot block
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

OUTDIR = tempfile.mkdtemp(prefix="plotting_demo07_")
MM_PER_INCH = 25.4

# Okabe, M., & Ito, K. (2008). "Color Universal Design" palette, the eight
# values as published. Black is included last.
OKABE_ITO = {
    "black": "#000000",
    "orange": "#E69F00",
    "sky blue": "#56B4E9",
    "bluish green": "#009E73",
    "yellow": "#F0E442",
    "blue": "#0072B2",
    "vermillion": "#D55E00",
    "reddish purple": "#CC79A7",
}


def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


def hex_to_rgb(colour):
    if isinstance(colour, str):
        h = colour.lstrip("#")
        return np.array([int(h[i:i + 2], 16) for i in (0, 2, 4)]) / 255.0
    return np.asarray(colour, dtype=float)[:3]


def srgb_to_lab(rgb):
    """CIE L*a*b* (D65) from sRGB in [0, 1]. Standard published transform."""
    lin = np.where(rgb <= 0.04045, rgb / 12.92, ((rgb + 0.055) / 1.055) ** 2.4)
    M = np.array([[0.4124564, 0.3575761, 0.1804375],
                  [0.2126729, 0.7151522, 0.0721750],
                  [0.0193339, 0.1191920, 0.9503041]])
    X, Y, Z = M @ lin
    Xn, Yn, Zn = 0.95047, 1.00000, 1.08883
    eps = 216.0 / 24389.0
    kappa = 24389.0 / 27.0

    def f(t):
        return np.where(t > eps, np.cbrt(t), (kappa * t + 16.0) / 116.0)

    fx, fy, fz = f(X / Xn), f(Y / Yn), f(Z / Zn)
    return np.array([116.0 * fy - 16.0, 500.0 * (fx - fy),
                     200.0 * (fy - fz)])


def pairwise_deltaE(colors):
    labs = np.array([srgb_to_lab(hex_to_rgb(c)) for c in colors])
    n = len(labs)
    de = np.full((n, n), np.inf)
    dl = np.full((n, n), np.inf)
    for i in range(n):
        for j in range(i + 1, n):
            de[i, j] = de[j, i] = np.linalg.norm(labs[i] - labs[j])
            dl[i, j] = dl[j, i] = abs(labs[i][0] - labs[j][0])
    return de, dl, labs


def part1_geometry():
    section("1. Column widths in millimetres decide the pixel budget")

    print(f"  {'target':<28}{'width (mm)':>12}{'width (in)':>12}"
          f"{'px @150':>9}{'px @300':>9}{'px @600':>9}")
    for name, mm in (("single column (typical)", 85.0),
                     ("1.5 column (typical)", 114.0),
                     ("double column (typical)", 174.0),
                     ("US letter text width", 6.5 * MM_PER_INCH)):
        inch = mm / MM_PER_INCH
        px = [round(inch * d) for d in (150, 300, 600)]
        print(f"  {name:<28}{mm:>12.1f}{inch:>12.3f}{px[0]:>9}{px[1]:>9}{px[2]:>9}")
    print()
    print("  Editors state a minimum dpi for raster figures (commonly 300 for")
    print("  photographs and colour, higher for line art) and a maximum physical")
    print("  width. Those two numbers together fix the pixel dimensions, and a")
    print("  file whose pixel width exceeds the budget is either rejected or")
    print("  silently downsampled -- which is the same as reducing its dpi.")
    inch = 174.0 / MM_PER_INCH
    print(f"  A double-column figure at 300 dpi is {inch * 300:.0f} px wide;"
          f" that is the number to check, not the dpi alone.")


def part2_type_size_survives_scaling():
    section("2. Scaling a finished figure changes the type size, not the fonts")

    print("  A figure authored at one width and placed at another has every point")
    print("  size multiplied by the placement ratio:")
    print()
    print(f"  {'authored at':>12}{'placed at':>11}{'ratio':>8}"
          f"{'8 pt becomes':>14}{'6 pt becomes':>14}")
    for authored, placed in ((180, 85), (180, 174), (120, 85), (85, 85)):
        r = placed / authored
        print(f"  {authored:>8} mm{placed:>8} mm{r:>8.3f}"
              f"{8 * r:>13.2f} pt{6 * r:>13.2f} pt")
    print()
    print("  Placed at 85 mm, a figure authored at 180 mm turns its 8 pt labels")
    print(f"  into {8 * 85 / 180:.2f} pt -- below the 6-7 pt floor most journals set.")
    print("  The fix is to author at the FINAL size and choose point sizes there,")
    print("  not to enlarge the fonts and hope. Because the reduction is uniform,")
    print("  line weights and marker sizes shrink with the type, so a figure that")
    print("  looked balanced at 180 mm looks uniformly faint at 85 mm.")


def part3_line_weights():
    section("3. Line weights in points and in pixels")

    print(f"  {'width (pt)':>11}{'@150 dpi (px)':>15}{'@300 dpi (px)':>15}"
          f"{'@600 dpi (px)':>15}")
    for pt in (0.25, 0.5, 0.75, 1.0, 1.5, 2.0):
        row = "".join(f"{pt / 72 * d:>15.2f}" for d in (150, 300, 600))
        print(f"  {pt:>11.2f}{row}")
    print()
    print("  A 0.25 pt line is 0.5 px at 150 dpi and 2.1 px at 600 dpi: the same")
    print("  instruction produces a line that breaks up at low resolution and a")
    print("  clean line at high resolution. Set the axis line weight explicitly")
    print("  rather than relying on the default, and never go below about 0.5 pt")
    print("  for anything that must survive a 300 dpi rasteriser.")


def part4_palettes():
    section("4. Two palettes measured in CIE L*a*b*")

    names = list(OKABE_ITO)
    colours = [OKABE_ITO[n] for n in names]
    de, dl, labs = pairwise_deltaE(colours)
    print(f"  {'Okabe-Ito colour':<18}{'hex':>9}{'L*':>8}{'a*':>8}{'b*':>8}")
    for name, colour, lab in zip(names, colours, labs):
        print(f"  {name:<18}{colour:>9}{lab[0]:>8.1f}{lab[1]:>8.1f}{lab[2]:>8.1f}")
    i, j = np.unravel_index(np.argmin(de), de.shape)
    k, l = np.unravel_index(np.argmin(dl), dl.shape)
    print()
    print(f"  closest pair by dE*ab : {names[i]} / {names[j]}  dE = {de[i, j]:.1f}")
    print(f"  closest pair by dL*   : {names[k]} / {names[l]}  dL* = {dl[k, l]:.1f}")

    import matplotlib as mpl
    cycle = [mpl.rcParams["axes.prop_cycle"].by_key()["color"][t]
             for t in range(8)]
    de2, dl2, labs2 = pairwise_deltaE(cycle)
    i2, j2 = np.unravel_index(np.argmin(de2), de2.shape)
    k2, l2 = np.unravel_index(np.argmin(dl2), dl2.shape)
    print()
    print(f"  {'Matplotlib default cycle (C0..C7)':<34}")
    print(f"  closest pair by dE*ab : C{i2} / C{j2}  dE = {de2[i2, j2]:.1f}")
    print(f"  closest pair by dL*   : C{k2} / C{l2}  dL* = {dl2[k2, l2]:.1f}")
    print()
    print("  dE*ab is a distance in a space built to match perceived difference:")
    print(f"  the closest pair inside Okabe-Ito is {de[i, j]:.1f} apart and the")
    print(f"  closest pair inside the default cycle is {de2[i2, j2]:.1f} apart, so")
    print("  both keep every categorical pair visibly distinct.")
    print()
    print(f"  The lightness minima tell a different story: {dl[k, l]:.1f} for")
    print(f"  Okabe-Ito ({names[k]} against {names[l]}) and {dl2[k2, l2]:.1f} for")
    print(f"  the default cycle (C{k2} against C{l2}). At least one pair in EACH")
    print("  palette has almost identical brightness, so that pair is separated by")
    print("  hue alone. If the figure must survive a monochrome print or a")
    print("  colour-blind reader, the palette is not enough on its own: add a")
    print("  second channel -- marker shape, line style, or a direct label on the")
    print("  curve -- so the distinction does not rest on one dimension.")

    # The palette in use, plus the same categorical data through a paper-size
    # figure, drawn at the final physical width.
    fig, axes = plt.subplots(1, 2, figsize=(85.0 / MM_PER_INCH, 55.0 / MM_PER_INCH),
                             dpi=300, constrained_layout=True)
    x = np.linspace(0, 1, 200)
    for name in ("bluish green", "orange", "blue", "vermillion"):
        freq = 1 + names.index(name) * 0.7
        axes[0].plot(x, np.sin(2 * np.pi * freq * x),
                     color=OKABE_ITO[name], lw=1.0, label=name)
    axes[0].legend(frameon=False, fontsize=6)
    axes[0].set_xlabel("x (normalised)", fontsize=7)
    axes[0].set_ylabel("signal", fontsize=7)
    axes[0].tick_params(labelsize=6)
    axes[0].set_title("Okabe-Ito palette", fontsize=7)

    axes[1].bar(range(8), np.arange(1.0, 9.0),
                color=[OKABE_ITO[n] for n in names], width=0.8)
    axes[1].set_xticks(range(8))
    axes[1].set_xticklabels([n.split()[0] for n in names], rotation=45,
                            ha="right", fontsize=6)
    axes[1].set_ylabel("category index", fontsize=7)
    axes[1].tick_params(labelsize=6)
    axes[1].set_title("categorical use", fontsize=7)

    png = os.path.join(OUTDIR, "07_journal_85mm.png")
    fig.savefig(png, dpi=300)
    plt.close(fig)
    from PIL import Image
    with Image.open(png) as im:
        W, H = im.size
    print()
    print(f"  saved {os.path.basename(png)}: {W} x {H} px at 300 dpi"
          f" = {W / 300 * MM_PER_INCH:.1f} x {H / 300 * MM_PER_INCH:.1f} mm")
    print("  That is a physical object 85 mm wide with 6-7 pt type, exactly as")
    print("  the column requires; nothing needs to be scaled afterwards.")


def part5_fonts_embedded():
    section("5. A PDF must embed its fonts, and the default does not always")

    def render(path):
        fig, ax = plt.subplots(figsize=(85.0 / MM_PER_INCH, 50.0 / MM_PER_INCH),
                               dpi=300)
        ax.plot(np.linspace(0, 1, 50), np.linspace(0, 1, 50) ** 2)
        ax.set_xlabel("x", fontsize=7)
        ax.set_ylabel(r"$y = x^2$", fontsize=7)
        fig.savefig(path)
        plt.close(fig)
        return open(path, "rb").read()

    print(f"  matplotlib rcParams['pdf.fonttype'] ="
          f" {matplotlib.rcParams['pdf.fonttype']} by default")
    print()
    for label, fonttype in (("default", None), ("fonttype = 42", 42)):
        if fonttype is not None:
            matplotlib.rcParams["pdf.fonttype"] = fonttype
        blob = render(os.path.join(OUTDIR, f"07_font_{fonttype}.pdf"))
        checks = {
            "TrueType font program (/FontFile2)": b"/FontFile2" in blob,
            "Type 1 font program (/FontFile)": b"/FontFile " in blob,
            "Type 3 fonts (/Subtype /Type3)": b"/Type3" in blob,
            "raster image object (/Subtype /Image)": b"/Subtype /Image" in blob,
        }
        print(f"  {label}  ({len(blob) / 1024:.1f} kB)")
        for name, present in checks.items():
            print(f"    {name:<40}{'present' if present else 'absent':>9}")
        print()
    matplotlib.rcParams["pdf.fonttype"] = 3

    print("  Type 3 fonts are the historic Matplotlib default and they embed the")
    print("  glyph programs generated by the renderer, which most journals accept")
    print("  and some do not. Setting pdf.fonttype = 42 embeds TrueType instead,")
    print("  which is what production systems prefer. Either way the test is the")
    print("  same five lines used above: look for the font-program object in the")
    print("  file rather than trusting that 'it saved as PDF, so it is fine'. A")
    print("  figure with a raster image object inside it is a raster figure")
    print("  wearing a vector extension, and will print soft.")


def part6_layout():
    section("6. What the layout engine actually moves")

    fig, ax = plt.subplots(figsize=(4.0, 3.0), dpi=100)
    ax.set_ylabel("a long y label that needs room")
    fig.canvas.draw()
    box_default = ax.get_position().bounds
    print(f"  default layout, axes bounds (l, b, w, h) ="
          f" ({box_default[0]:.3f}, {box_default[1]:.3f},"
          f" {box_default[2]:.3f}, {box_default[3]:.3f})")
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(4.0, 3.0), dpi=100, constrained_layout=True)
    ax.set_ylabel("a long y label that needs room")
    fig.canvas.draw()
    box_cl = ax.get_position().bounds
    print(f"  constrained_layout,       axes bounds ="
          f" ({box_cl[0]:.3f}, {box_cl[1]:.3f},"
          f" {box_cl[2]:.3f}, {box_cl[3]:.3f})")
    plt.close(fig)

    print()
    print(f"  constrained_layout changed the left edge by"
          f" {box_cl[0] - box_default[0]:+.3f} of the figure width, the width by"
          f" {box_cl[2] - box_default[2]:+.3f}")
    print(f"  and the height by {box_cl[3] - box_default[3]:+.3f}. The figure size"
          " never changed.")
    print("  The plotted area is therefore a property of the LAYOUT ENGINE, not of")
    print("  the figsize. Here the default engine reserved more margin than the")
    print("  label needed and the constrained engine reclaimed it, so the data")
    print("  area is larger under constrained_layout for the same canvas.")
    print("  The practical consequence: never infer the plotted area from the")
    print("  figure dimensions when choosing an aspect ratio. For a figure that")
    print("  must hit an exact ratio -- a map, a cross-section -- set the aspect")
    print("  on the axes, which then fixes the data area and lets the layout move")
    print("  only the margins.")


def main():
    part1_geometry()
    part2_type_size_survives_scaling()
    part3_line_weights()
    part4_palettes()
    part5_fonts_embedded()
    part6_layout()
    print()
    print("Images written to:", OUTDIR)
    print("Nothing was written inside the repository.")


if __name__ == "__main__":
    main()
