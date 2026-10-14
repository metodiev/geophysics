"""Colour perception: sequential, diverging and the case against rainbow.

Run:  .venv/bin/python 06_colormaps_perception_demo.py
Requires: numpy, matplotlib (Agg).

Companion to lesson 03-05-06.

Instead of asserting that rainbow colormaps are bad, this script measures three
properties of every candidate palette by converting its 256 sRGB entries to CIE
L* (the perceptually uniform lightness):

* ``L* span``            -- how much lightness the map has to work with.
* ``reversals``          -- how many times the lightness changes direction as
                            the data value increases. Each reversal is a place
                            where a smooth ramp of data looks like it has an
                            edge, because the eye reads lightness, not hue.
* ``max/median |dL*/dv|`` -- the steepest lightness gradient divided by the
                            typical one. A large value means the map amplifies
                            some data gradients and suppresses others.

A grayscale-collision count is added, because it is the direct test of whether
two different data values can be told apart when colour is unavailable.

All fields are SYNTHETIC. Images go to a temporary directory, never into the
repository.
"""

import os
import tempfile

import matplotlib

matplotlib.use("Agg")  # headless: no window, so the script cannot block
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib import colormaps  # noqa: E402

OUTDIR = tempfile.mkdtemp(prefix="plotting_demo06_")
N_SAMPLE = 256


def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


def srgb_to_Lstar(rgb):
    """CIE 1976 lightness L* from sRGB in [0, 1], D65 white (Y_n = 1)."""
    c = np.asarray(rgb, dtype=float)
    lin = np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    Y = 0.2126 * lin[..., 0] + 0.7152 * lin[..., 1] + 0.0722 * lin[..., 2]
    eps = 216.0 / 24389.0          # CIE 1976 (6/29)^3
    kappa = 24389.0 / 27.0
    f = np.where(Y > eps, np.cbrt(Y), (kappa * Y + 16.0) / 116.0)
    return 116.0 * f - 16.0


def colormap_metrics(name):
    cmap = colormaps[name]
    v = np.linspace(0.0, 1.0, N_SAMPLE)
    rgb = np.array([cmap(t)[:3] for t in v])
    L = srgb_to_Lstar(rgb)
    dL = np.diff(L)                        # per unit data step (dv = 1/255)
    reversals = int(np.sum(np.diff(np.sign(dL)) != 0))
    median_slope = float(np.median(np.abs(dL)))
    ratio = float(np.abs(dL).max() / median_slope)
    # Grayscale ambiguity: quantise L* to integer levels and, for each level,
    # measure how far apart in data space the values sharing it are.
    q = np.round(L).astype(int)
    spans = []
    for level in np.unique(q):
        idx = np.flatnonzero(q == level)
        spans.append(idx.max() - idx.min())
    max_spread = 100.0 * max(spans) / (N_SAMPLE - 1)
    wide = int(sum(1 for s in spans
                   if 100.0 * s / (N_SAMPLE - 1) > 10.0))
    return dict(L_min=float(L.min()), L_max=float(L.max()),
                L_span=float(L.max() - L.min()), reversals=reversals,
                ratio=ratio, max_spread=max_spread, wide=wide,
                L=L, dL=dL, rgb=rgb)


def part1_metrics_table():
    section("1. Measured lightness metrics for the maps in common use")

    families = {
        "viridis": "sequential (perceptually uniform)",
        "cividis": "sequential, colour-vision-deficiency optimised",
        "Greys": "sequential, monochrome",
        "magma": "sequential (perceptually uniform)",
        "jet": "rainbow (legacy default)",
        "turbo": "rainbow (smoother legacy default)",
        "hsv": "cyclic / hue-only",
        "RdBu_r": "diverging",
        "seismic": "diverging",
    }
    print(f"  {'colormap':<10}{'family':<46}{'L* span':>8}{'rev':>5}"
          f"{'max/med':>9}")
    metrics = {}
    for name, fam in families.items():
        m = colormap_metrics(name)
        metrics[name] = m
        print(f"  {name:<10}{fam:<46}{m['L_span']:>8.1f}{m['reversals']:>5}"
              f"{m['ratio']:>9.2f}")
    print()
    print("  'rev' counts the sign changes of dL*/dv. Zero means lightness rises")
    print("  monotonically with the data, so brightness is a faithful proxy for")
    print("  value. viridis, cividis, Greys and magma all score 0. jet and hsv")
    print("  each score 5 and turbo 1; every one of those reversals is a place")
    print("  where a smooth ramp of data renders with a lightness step the data")
    print("  do not contain. RdBu_r and seismic also score 1, and that reversal")
    print("  is not a defect: a diverging map is DEFINED by lightness peaking in")
    print("  the middle, because its job is to make the centre conspicuous.")
    return metrics, families


def part2_false_boundaries(metrics):
    section("2. Where the false boundaries sit in a smooth ramp")

    v = np.linspace(0.0, 1.0, N_SAMPLE)[:-1]
    for name in ("viridis", "jet", "turbo", "hsv"):
        m = metrics[name]
        dL = m["dL"]
        k = int(np.argmax(np.abs(dL)))
        col = tuple(int(c) for c in (m["rgb"][k] * 255).round())
        print(f"  {name:<8} steepest step at data fraction {v[k]:.3f}:"
              f" |dL*| = {abs(dL[k]):.3f} against a median of"
              f" {np.median(np.abs(dL)):.3f}")
        print(f"           so the map runs {m['ratio']:.2f} times faster"
              f" through lightness there than it typically does;")
        print(f"           colour at that step: sRGB {col}")
    print()
    print("  Read the jet row against the viridis row. viridis's largest")
    print("  acceleration is 1.19 times its own median rate; turbo reaches 2.36")
    print("  and hsv 5.64. The jet step sits at data fraction 0.333, in the")
    print("  blue-to-cyan transition, where the map runs 1.69 times its typical")
    print("  rate through lightness. An isopleth of constant data value rendered")
    print("  through such a step acquires a brightness halo, and the eye draws a")
    print("  contour the data never asked for. The lightness channel is what")
    print("  carries the edge; the hue change on top of it only makes the")
    print("  artefact look more like structure.")

    fig, axes = plt.subplots(4, 1, figsize=(8.0, 6.0), dpi=150,
                            gridspec_kw=dict(height_ratios=[1, 3, 1, 3]))
    ramp = np.linspace(0, 1, 512)[None, :]
    for row, name in zip((0, 2), ("viridis", "jet")):
        ax = axes[row]
        ax.imshow(ramp, aspect="auto", cmap=name, extent=[0, 1, 0, 1])
        ax.set_yticks([])
        ax.set_title(f"{name}: a smooth ramp of data", fontsize=8)
        ax2 = axes[row + 1]
        vv = np.linspace(0, 1, N_SAMPLE)
        ax2.plot(vv, metrics[name]["L"], color="k", lw=1.3)
        ax2.set_ylabel(r"$L^*$")
        ax2.set_xlim(0, 1)
        ax2.grid(True, lw=0.4, alpha=0.4)
        if name == "jet":
            k = int(np.argmax(np.abs(metrics[name]["dL"])))
            ax2.axvline(vv[k], color="crimson", lw=1.0, ls="--")
            ax2.annotate("steepest dL*/dv", xy=(vv[k], metrics[name]["L"][k]),
                         xytext=(0.1, 20), fontsize=7, color="crimson",
                         arrowprops=dict(arrowstyle="->", color="crimson",
                                         lw=0.7))
    axes[3].set_xlabel("data value (normalised)")
    axes[1].set_xlabel("data value (normalised)")
    fig.suptitle("Lightness of the rendered colour versus data value "
                 "(SYNTHETIC ramp)", fontsize=10)
    fig.tight_layout()
    path = os.path.join(OUTDIR, "06_lightness.png")
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"  saved {os.path.basename(path)}  (150 dpi, 4 stacked panels)")


def part3_gray_and_signed():
    section("3. Grayscale collapse and the diverging choice")

    print("  For a viewer who cannot separate hues, or a black-and-white print,")
    print("  the figure is its own lightness map. Two data values that share a")
    print("  lightness are then indistinguishable, and the measure of the damage")
    print("  is how far apart in data space those values are.")
    print()
    print(f"  {'colormap':<10}{'widest shared L* bin':>22}{'bins spanning >10 %':>21}")
    for name in ("viridis", "cividis", "Greys", "jet", "turbo", "hsv"):
        m = colormap_metrics(name)
        print(f"  {name:<10}{m['max_spread']:>21.1f} %{m['wide']:>21}")
    print()
    print("  For a monotone map every shared bin holds consecutive data values,")
    print("  so the widest bin spans a fraction of a per cent of the range. For")
    print("  the rainbow maps the widest bin spans tens of per cent, because two")
    print("  values at opposite ends of the scale have the same brightness and")
    print("  the figure says they are the same.")

    # SYNTHETIC signed anomaly field.
    g = np.linspace(-8, 8, 240)
    X, Y = np.meshgrid(g, g)
    field = (30 * np.exp(-((X + 2.5) ** 2 + (Y - 1.5) ** 2) / 7)
             - 22 * np.exp(-((X - 3.0) ** 2 + (Y + 2.0) ** 2) / 11))

    vmax = np.abs(field).max()
    fig, axes = plt.subplots(2, 2, figsize=(9.0, 8.0), dpi=150)
    panels = [
        (axes[0, 0], "viridis", None, None, "sequential map on signed data:\n"
         "zero anomaly becomes a mid colour and the sign is lost"),
        (axes[0, 1], "jet", None, None, "rainbow map on signed data:\n"
         "zero is a green band and residuals look like anomalies"),
        (axes[1, 0], "RdBu_r", -vmax, +vmax, "diverging map centred on zero:\n"
         "white is unambiguously no anomaly"),
        (axes[1, 1], "RdBu_r", None, None, "diverging map centred on the data\n"
         "range instead: the neutral colour is off by the mean"),
    ]
    for ax, cmap, vmin, vmax_, note in panels:
        im = ax.imshow(field, cmap=cmap, origin="lower",
                       extent=[g[0], g[-1], g[0], g[-1]],
                       vmin=vmin, vmax=vmax_)
        fig.colorbar(im, ax=ax, fraction=0.046)
        ax.set_title(note, fontsize=7.5)
        ax.set_xlabel("x (km)")
        ax.set_ylabel("y (km)")
    fig.suptitle("SYNTHETIC residual anomaly: palette class decides what the "
                 "eye reads as structure", fontsize=10)
    fig.tight_layout()
    path = os.path.join(OUTDIR, "06_sequential_vs_diverging.png")
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"  saved {os.path.basename(path)}  (150 dpi, 4 panels)")

    print()
    lo, hi = field.min(), field.max()
    midrange = 0.5 * (lo + hi)
    print(f"  field statistics: min {lo:+.3f}, max {hi:+.3f},"
          f" mean {field.mean():+.3f} mGal")
    print(f"  With vmin/vmax set to the data range ({lo:+.3f}, {hi:+.3f}), the")
    print(f"  neutral colour of a diverging palette sits at the MIDRANGE")
    print(f"  {midrange:+.3f} mGal -- not at zero, and not at the mean either.")
    print(f"  So a {abs(midrange):.3f} mGal anomaly is rendered as 'no anomaly',")
    print(f"  while the field's own mean is only {field.mean():+.3f} mGal. The two")
    print("  candidates are different numbers; neither is zero, which is the value")
    print("  the physics requires.")


def part4_cyclic():
    section("4. A cyclic quantity needs a cyclic map, and the seam must be shown")

    phase = np.linspace(0.0, 2 * np.pi, 512)[None, :]
    fig, axes = plt.subplots(3, 1, figsize=(8.0, 4.2), dpi=150)
    for ax, cmap, note in zip(
            axes, ("hsv", "twilight", "viridis"),
            ("cyclic map (hsv): 0 and 2*pi meet in red -- correct for phase",
             "cyclic map (twilight): the seam is dark and visible",
             "sequential map on phase: 0 and 2*pi differ, inventing a "
             "discontinuity")):
        im = ax.imshow(phase, aspect="auto", cmap=cmap,
                       extent=[0, 2 * np.pi, 0, 1])
        ax.set_yticks([])
        ax.set_title(note, fontsize=8)
        for ax2 in (ax,):
            ax2.set_xticks([0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi])
            ax2.set_xticklabels(["0", "$\\pi/2$", "$\\pi$", "$3\\pi/2$",
                                 "$2\\pi$"], fontsize=7)
    axes[-1].set_xlabel("phase (rad)")
    fig.suptitle("One period of a phase field under three maps", fontsize=10)
    fig.tight_layout()
    path = os.path.join(OUTDIR, "06_cyclic.png")
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"  saved {os.path.basename(path)}  (150 dpi, 3 panels)")
    end_gap = float(np.linalg.norm(np.array(colormaps["viridis"](1.0)[:3])
                                   - np.array(colormaps["viridis"](0.0)[:3])))
    wrap_gap = float(np.linalg.norm(np.array(colormaps["hsv"](1.0)[:3])
                                    - np.array(colormaps["hsv"](0.0)[:3])))
    print(f"  viridis: sRGB distance between the two ends = {end_gap:.4f}")
    print(f"  hsv    : sRGB distance between the two ends = {wrap_gap:.4f}")
    print()
    print("  A sequential map gives the first and last sample of the period")
    print(f"  clearly different colours (distance {end_gap:.4f}), so the wrap at")
    print("  the period boundary appears as a discontinuity in the field. A")
    print(f"  cyclic map nearly closes the loop (distance {wrap_gap:.4f},"
          f" {end_gap / wrap_gap:.0f} times smaller)")
    print("  and the seam carries almost no information. That is the property")
    print("  the data have, so it is the property the palette must have.")


def main():
    metrics, _ = part1_metrics_table()
    part2_false_boundaries(metrics)
    part3_gray_and_signed()
    part4_cyclic()
    print()
    print("Images written to:", OUTDIR)
    print("Nothing was written inside the repository.")


if __name__ == "__main__":
    main()
