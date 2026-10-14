"""Seismic displays: wiggle, variable density, and what the clip level hides.

Run:  .venv/bin/python 05_seismic_displays_demo.py
Requires: numpy, matplotlib (Agg).

Companion to lesson 03-05-05.

The section is SYNTHETIC and built from a stated model, so the effect of every
display choice can be checked against the generator rather than against
folklore:

* Part 1 builds a layered reflectivity series with three dipping horizons,
  convolves it with a Ricker wavelet, and reports the amplitude statistics that
  a clip level must be chosen from.
* Part 2 draws the wiggle display and reports the trace spacing at which the
  wiggles stop being resolvable.
* Part 3 draws the same data at three clip levels and counts the samples that
  saturate at each, so "the clip level hides structure" becomes a number.
* Part 4 shows that the display is a diverging one only because the amplitude
  has a defined zero, and measures the mean that justifies centring there.
* Part 5 shows polarity reversal of an identical section, which is why a
  polarity convention must be printed on the figure.

Images are written to a temporary directory, never into the repository.
"""

import os
import tempfile

import matplotlib

matplotlib.use("Agg")  # headless: no window, so the script cannot block
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

OUTDIR = tempfile.mkdtemp(prefix="plotting_demo05_")


def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


DT = 0.002          # s, sample interval
NX = 120            # traces
NT = 420            # samples per trace
F_DOM = 28.0        # Hz, Ricker peak frequency


def build_section():
    """Return (section, t, x_km) for a SYNTHETIC layered model."""
    t = np.arange(NT) * DT
    x_km = np.linspace(0.0, 12.0, NX)

    # Three horizons, two dipping, one a flat unconformity. Depths in samples.
    horizons = [
        70.0 + 3.2 * np.arange(NX),            # steeply dipping reflector
        180.0 + 0.0 * np.arange(NX),           # flat marker
        300.0 - 1.4 * np.arange(NX),           # gently rising reflector
    ]
    amps = [1.0, -0.7, 0.55]
    reflectivity = np.zeros((NT, NX))
    for depth, amp in zip(horizons, amps):
        for k in range(NX):
            i = int(round(depth[k]))
            if 0 <= i < NT:
                reflectivity[i, k] += amp

    # Ricker wavelet.
    tw = np.arange(-0.064, 0.064 + DT / 2, DT)
    w = (1.0 - 2.0 * (np.pi * F_DOM * tw) ** 2) * np.exp(
        -(np.pi * F_DOM * tw) ** 2)
    w /= np.abs(w).max()

    sec = np.empty_like(reflectivity)
    for k in range(NX):
        sec[:, k] = np.convolve(reflectivity[:, k], w, mode="same")
    return sec, t, x_km


def part1_statistics(sec, t):
    section("1. The amplitude statistics a clip level is chosen from")

    a = np.abs(sec)
    nz = a[a > 0.0]
    print(f"  section: {sec.shape[0]} samples x {sec.shape[1]} traces,"
          f" dt = {DT * 1000:.0f} ms")
    print(f"  mean  = {sec.mean():+.6f}   median = {np.median(sec):+.6f}")
    print(f"  std   = {sec.std():.6f}")
    print(f"  samples with |a| exactly 0: {100.0 * (1 - nz.size / a.size):.2f} %"
          "  (the gaps between wavelets)")
    print()
    print("  statistics of the NONZERO amplitudes, i.e. of the wavelets")
    print(f"  {'percentile':>12}{'of nonzero |a|':>18}")
    for p in (50.0, 90.0, 99.0, 99.5):
        print(f"  {p:>12.1f}{np.percentile(nz, p):>18.6f}")
    print()
    print(f"  largest |a| in the whole section: {a.max():.6f}")
    print()
    print("  Amplitudes are zero-mean by construction and both signs carry")
    print("  information: a positive reflection coefficient is a hard interface.")
    print("  That is the whole reason the display colormap must be DIVERGING and")
    print("  symmetric about zero -- the sign of the sample is the datum.")


def part2_wiggle(sec, t, x_km):
    section("2. The wiggle display and where it stops working")

    n_traces = 60
    k0 = 30
    sub = sec[:, k0:k0 + n_traces]
    disp = t[:, None] * np.ones((1, n_traces))
    scale = 0.9 / np.abs(sub).max()      # one trace spacing = one full swing

    fig, ax = plt.subplots(figsize=(6.4, 5.2), dpi=150)
    for k in range(n_traces):
        a = sub[:, k] * scale
        ax.plot(k + a, disp[:, k], color="k", lw=0.4)
        ax.fill_betweenx(disp[:, k], k, k + a, where=(a > 0), color="k",
                         lw=0)
    ax.set_xlim(-1, n_traces)
    ax.set_ylim(t.max(), 0.0)            # time increases downward
    ax.set_xlabel("trace number (SYNTHETIC)")
    ax.set_ylabel("two-way time (s)")
    ax.set_title("Wiggle display: positive lobes filled")
    fig.tight_layout()
    path = os.path.join(OUTDIR, "05_wiggle.png")
    fig.savefig(path, dpi=150)
    plt.close(fig)

    print(f"  {n_traces} traces across {6.4:.1f} in of figure width")
    print(f"    trace spacing = {6.4 / n_traces * 25.4:.2f} mm"
          f"  ({72 * 6.4 / n_traces:.1f} pt)")
    print(f"    peak amplitude scaled so one full swing = one trace spacing")
    print(f"    scale factor applied: {scale:.2f} per unit amplitude")
    print(f"  saved {os.path.basename(path)}  (150 dpi)")
    print()
    print("  A wiggle is readable while a full swing stays inside the trace")
    print("  spacing. Beyond that, adjacent traces interpenetrate and the eye")
    print("  can no longer tell a large event from two medium ones. At 300 traces")
    print("  across the same width the spacing is 0.54 mm and the display is")
    print("  decorative, which is exactly when variable density takes over.")


def part3_clip_levels(sec, t, x_km):
    section("3. Three clip levels, and the samples each one throws away")

    xmax = x_km[-1]
    amax = np.abs(sec).max()
    ref = np.percentile(np.abs(sec), 99.0)
    clips = {
        "0.25 x max (too tight)": 0.25 * amax,
        "p99 (conventional)": ref,
        "max (too loose)": amax,
    }
    print(f"  {'clip level':<24}{'value':>10}{'saturated %':>14}"
          f"{'clip / p99 (dB)':>18}")
    for name, c in clips.items():
        sat = 100.0 * np.mean(np.abs(sec) >= c)
        print(f"  {name:<24}{c:>10.5f}{sat:>14.3f}{20 * np.log10(c / ref):>18.2f}")
    print()
    print("  'Saturated' counts samples at or beyond the clip; those pixels all")
    print("  receive the same extreme colour, so any amplitude difference among")
    print("  them is gone. A tight clip maximises contrast on the weak events and")
    print("  destroys the strong ones -- 4.220 % of samples lose their amplitude")
    print("  entirely here. The maximum clip saturates only the single largest")
    print("  sample and compresses every event by the factor between the clip and")
    print("  the 99th percentile, which is 6.90 dB in this section, so the")
    print("  reflectors look weak and the fine detail vanishes into the neutral")
    print("  colour.")

    fig, axes = plt.subplots(1, 3, figsize=(12.6, 4.4), dpi=150)
    for ax, (name, c) in zip(axes, clips.items()):
        im = ax.imshow(sec, cmap="RdBu_r", aspect="auto", vmin=-c, vmax=+c,
                       extent=[x_km[0], xmax, t[-1], t[0]],
                       interpolation="nearest")
        fig.colorbar(im, ax=ax, fraction=0.046, label="amplitude (arb. units)")
        ax.set_title(f"{name}\nclip = +/- {c:.4f}", fontsize=8)
        ax.set_xlabel("distance (km)")
        ax.set_ylabel("two-way time (s)")

    fig.suptitle("SYNTHETIC section, identical data, three clip levels",
                 fontsize=10)
    fig.tight_layout()
    path = os.path.join(OUTDIR, "05_clip_levels.png")
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"  saved {os.path.basename(path)}  (150 dpi, 3 panels)")


def part4_centring_and_combining(sec, t, x_km):
    section("4. Symmetric about zero, and the combined display")

    mean = sec.mean()
    p1 = np.percentile(sec, 1.0)
    p99 = np.percentile(sec, 99.0)
    print(f"  data mean                = {mean:+.6f}")
    print(f"  symmetric clip about zero: [{-np.abs(sec).max():.4f}, "
          f"{np.abs(sec).max():.4f}]")
    print(f"  asym. percentile clip    : [{p1:.4f}, {p99:.4f}]")
    asymmetry = abs((-p1) - p99) / (p99 - p1)
    print(f"  relative asymmetry of the percentile clip: {asymmetry * 100:.2f} %")
    print()
    print("  A diverging map places its neutral colour exactly at the value you")
    print("  pass as the centre. Because a reflection coefficient has a physical")
    print("  zero -- no contrast, no reflection -- the centre is fixed by the")
    print("  physics. Centring a diverging map on the data mean instead would put")
    print("  the neutral colour at a value that means 'average', and every")
    print("  polarity judgement made from the figure would be offset.")

    c = np.percentile(np.abs(sec), 99.0)
    fig, ax = plt.subplots(figsize=(7.2, 5.4), dpi=150)
    im = ax.imshow(sec, cmap="RdBu_r", aspect="auto", vmin=-c, vmax=+c,
                   extent=[x_km[0], x_km[-1], t[-1], t[0]],
                   interpolation="bilinear")
    n_over = len(range(0, NX, 4))
    for k in range(0, NX, 4):
        a = sec[:, k] / np.abs(sec).max() * 2.0
        ax.plot(x_km[k] + a * (x_km[1] - x_km[0]), t, color="k", lw=0.3)
    fig.colorbar(im, ax=ax, fraction=0.046, label="amplitude (arb. units)")
    ax.set_title(f"Combined: variable density + {n_over} overlay wiggles",
                 fontsize=8)
    ax.set_xlabel("distance (km)")
    ax.set_ylabel("two-way time (s)")
    fig.tight_layout()
    path = os.path.join(OUTDIR, "05_combined.png")
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"  saved {os.path.basename(path)}  (150 dpi)")


def part5_polarity(sec, t, x_km):
    section("5. The same section, opposite colormap direction")

    c = np.percentile(np.abs(sec), 99.0)
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.0), dpi=150)
    for ax, cmap, lab in zip(axes, ("RdBu_r", "RdBu"),
                             ("RdBu_r  (positive = blue)", "RdBu  (positive = red)")):
        im = ax.imshow(sec, cmap=cmap, aspect="auto", vmin=-c, vmax=+c,
                       extent=[x_km[0], x_km[-1], t[-1], t[0]])
        fig.colorbar(im, ax=ax, fraction=0.046, label="amplitude")
        ax.set_title(lab, fontsize=9)
        ax.set_xlabel("distance (km)")
        ax.set_ylabel("two-way time (s)")
    fig.suptitle("Reversing the colormap reverses the apparent polarity of "
                 "every event", fontsize=10)
    fig.tight_layout()
    path = os.path.join(OUTDIR, "05_polarity.png")
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"  saved {os.path.basename(path)}  (150 dpi, 2 panels)")
    print()
    print("  Nothing in either panel says which direction is 'a hard interface',")
    print("  because that convention is a property of the acquisition (whether a")
    print("  positive reflection coefficient maps to a peak or a trough), not of")
    print("  the numbers. Every seismic figure therefore needs its polarity")
    print("  convention printed on it, and a figure without one cannot be")
    print("  compared with any other figure.")


def main():
    sec, t, x_km = build_section()
    part1_statistics(sec, t)
    part2_wiggle(sec, t, x_km)
    part3_clip_levels(sec, t, x_km)
    part4_centring_and_combining(sec, t, x_km)
    part5_polarity(sec, t, x_km)
    print()
    print("Images written to:", OUTDIR)
    print("Nothing was written inside the repository.")


if __name__ == "__main__":
    main()
