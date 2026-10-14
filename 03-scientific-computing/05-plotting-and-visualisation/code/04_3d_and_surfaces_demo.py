"""3-D surfaces and voxels, and the measurements that expose their limits.

Run:  .venv/bin/python 04_3d_and_surfaces_demo.py
Requires: numpy, matplotlib (Agg).

Companion to lesson 03-05-04.

A 3-D rendering is a 2-D picture of a 3-D object, produced by throwing away
one dimension. This script makes that loss quantitative:

* Part 1 projects the same data maximum to screen coordinates under four
  camera orientations, using Matplotlib's own projection matrix, and shows
  that the pixel position moves even though the data never change.
* Part 2 finds two data points that land on the same screen pixel but at
  different depths -- the ambiguity a reader cannot resolve.
* Part 3 counts the graphics primitives a surface and a voxel volume cost, so
  the expense is a number rather than an impression.
* Part 4 times the render, showing that cost grows with the grid, and that the
  orthogonal-slice alternative carries the same data for a fraction of it.

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
from mpl_toolkits.mplot3d import proj3d  # noqa: E402

OUTDIR = tempfile.mkdtemp(prefix="plotting_demo04_")


def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


def anomaly_surface(n=90, extent=10.0):
    """SYNTHETIC potential-field anomaly: a Gaussian high plus a dipping low."""
    g = np.linspace(-extent, extent, n)
    X, Y = np.meshgrid(g, g)
    high = 40.0 * np.exp(-(((X + 2.2) ** 2 + (Y - 1.5) ** 2) / 6.0))
    low = -25.0 * np.exp(-(((X - 3.0) ** 2 + (Y + 2.0) ** 2) / 9.0))
    ridge = 8.0 * np.exp(-((Y - 0.4 * X) ** 2) / 4.0)
    return X, Y, high + low + ridge


def part1_viewpoint_changes_the_picture():
    section("1. The same data project to different pixels from different angles")

    X, Y, Z = anomaly_surface()
    k = int(np.argmax(Z))
    i, j = divmod(k, Z.shape[1])
    xm, ym, zm = X[i, j], Y[i, j], Z[i, j]
    print(f"  data maximum at (x, y, z) = ({xm:.3f}, {ym:.3f}, {zm:.3f})"
          "   -- identical for every camera")
    print()
    print(f"  {'elev':>6}{'azim':>7}{'screen x (px)':>16}{'screen y (px)':>16}")

    fig = plt.figure(figsize=(4.0, 4.0), dpi=100)
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_surface(X, Y, Z, cmap="viridis", rstride=4, cstride=4,
                    linewidth=0, antialiased=True)
    fig.canvas.draw()

    for elev, azim in ((30, -60), (30, 30), (70, -60), (10, -120)):
        ax.view_init(elev=elev, azim=azim)
        fig.canvas.draw()
        x2, y2, _ = proj3d.proj_transform(xm, ym, zm, ax.get_proj())
        px, py = ax.transData.transform((x2, y2))
        print(f"  {elev:>6}{azim:>7}{px:>16.1f}{py:>16.1f}")
    plt.close(fig)

    print()
    print("  The peak's pixel position moves by tens of pixels between rows while")
    print("  the data are unchanged. Any reader who measures a distance or an")
    print("  apparent dip off the picture is measuring the camera, not the field.")


def part2_occlusion_ambiguity():
    section("2. Two distinct points that collide on screen at different depths")

    rng = np.random.default_rng(18921108)
    fig = plt.figure(figsize=(5.0, 5.0), dpi=100)
    ax = fig.add_subplot(111, projection="3d")
    ax.view_init(elev=20, azim=-60)
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_zlim(-30, 50)
    fig.canvas.draw()
    P = ax.get_proj()

    cloud = rng.uniform([-9, -9, -25], [9, 9, 45], size=(500, 3))
    proj = np.array([proj3d.proj_transform(*p, P)[:2] for p in cloud])
    span = proj.max(axis=0) - proj.min(axis=0)

    # Closest projected pair whose DEPTH separation exceeds 30 % of the box.
    d2 = ((proj[:, None, :] - proj[None, :, :]) ** 2).sum(-1)
    np.fill_diagonal(d2, np.inf)
    depth_gap = np.abs(cloud[:, 2][:, None] - cloud[:, 2][None, :])
    d2[depth_gap < 0.3 * 75.0] = np.inf
    i, j = np.unravel_index(np.argmin(d2), d2.shape)

    sep = np.sqrt(d2[i, j])
    print(f"  {len(cloud)} candidate points projected through the camera matrix")
    print(f"  closest pair separated by {sep / np.hypot(*span) * 100:.4f} %"
          " of the field of view yet")
    print(f"  separated in z by {abs(cloud[i, 2] - cloud[j, 2]):.2f} mGal"
          " (30 % threshold applied)")
    print()
    print(f"    point 1: data {np.round(cloud[i], 2)}"
          f"  ->  projected ({proj[i, 0]:+.6f}, {proj[i, 1]:+.6f})")
    print(f"    point 2: data {np.round(cloud[j], 2)}"
          f"  ->  projected ({proj[j, 0]:+.6f}, {proj[j, 1]:+.6f})")
    plt.close(fig)
    print()
    print("  Two points with completely different amplitudes land on the same")
    print("  pixel. Which one a reader sees is decided by the renderer's depth")
    print("  sort, not by the data, and no amount of staring resolves it. This is")
    print("  why a hidden peak in a 3-D surface plot is an artefact of the view:")
    print("  the information exists in the array and is absent from the figure.")


def part3_primitive_count():
    section("3. plot_surface silently downsamples, and voxels cost per cell")

    print("  facecolors carried by the returned Poly3DCollection, i.e. the")
    print("  number of coloured quads actually drawn:")
    print()
    print(f"  {'input grid':>11}{'quads drawn':>14}{'quads if full':>15}"
          f"{'data dropped':>14}")
    for n in (30, 50, 90, 180, 360):
        g = np.linspace(-10.0, 10.0, n)
        X, Y = np.meshgrid(g, g)
        Z = np.sin(X / 2.0) * np.cos(Y / 2.0)
        fig = plt.figure(figsize=(3, 3), dpi=100)
        ax = fig.add_subplot(111, projection="3d")
        surf = ax.plot_surface(X, Y, Z, cmap="viridis", linewidth=0)
        quads = surf.get_facecolors().shape[0]
        plt.close(fig)
        full = (n - 1) ** 2
        print(f"  {n:>5} x {n:<5}{quads:>14}{full:>15}"
              f"{100 * (1 - quads / full):>13.2f} %")
    print()
    print("  The default rcount=ccount=50 caps the drawn resolution. A 90 x 90")
    print("  grid and a 360 x 360 grid produce the SAME 2025 quads: refining the")
    print("  data past ~50 points per axis changes nothing on the screen, which")
    print("  is a silent loss of detail that no warning announces. Pass")
    print("  rcount=n, ccount=n (or rstride=1, cstride=1) to draw every cell and")
    print("  accept the cost you asked for.")

    # SYNTHETIC voxel body: a rectangular slab dipping through a small box.
    nx = ny = nz = 14
    zz, yy, xx = np.meshgrid(np.arange(nz), np.arange(ny), np.arange(nx),
                             indexing="ij")
    filled = (zz > 3 + 0.6 * xx) & (zz < 6 + 0.6 * xx)
    print()
    print(f"  ax.voxels on a {nx} x {ny} x {nz} lattice")
    print(f"    filled cells: {int(filled.sum())} of {filled.size}"
          f"  ({100 * filled.mean():.2f} %)")
    fig = plt.figure(figsize=(5, 5), dpi=100)
    ax = fig.add_subplot(111, projection="3d")
    ax.voxels(filled, edgecolor="k", linewidth=0.2, alpha=0.6)
    print(f"    Poly3DCollections created: {len(ax.collections)}")
    fig.canvas.draw()
    faces = sum(len(c.get_facecolors()) for c in ax.collections)
    print(f"    coloured faces actually drawn: {faces}")
    path = os.path.join(OUTDIR, "04_voxels.png")
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"    saved {os.path.basename(path)}  (150 dpi)")
    print()
    print("  Voxels also carry an alpha channel, so the far side of the body is")
    print("  visible through the near side. That helps shape perception and")
    print("  destroys depth order: a transparent rendering cannot tell you which")
    print("  of two touching bodies is in front.")


def part4_cost_and_the_alternative():
    section("4. Render cost grows with drawn primitives; sections do not")

    print(f"  {'grid':>8}{'rcount':>9}{'quads':>9}{'savefig (s)':>13}"
          f"{'file (kB)':>11}")
    for n, rc in ((40, 40), (80, 80), (160, 160), (320, 50)):
        g = np.linspace(-10.0, 10.0, n)
        X, Y = np.meshgrid(g, g)
        Z = anomaly_surface(n, extent=10.0)[2]
        fig = plt.figure(figsize=(4, 4), dpi=100)
        ax = fig.add_subplot(111, projection="3d")
        surf = ax.plot_surface(X, Y, Z, cmap="viridis", linewidth=0,
                              rcount=rc, ccount=rc)
        quads = surf.get_facecolors().shape[0]
        path = os.path.join(OUTDIR, f"04_cost{n}_{rc}.png")
        t0 = time.perf_counter()
        fig.savefig(path, dpi=150)
        dt = time.perf_counter() - t0
        plt.close(fig)
        print(f"  {n:>4} x {n:<3}{rc:>9}{quads:>9}{dt:>13.3f}"
              f"{os.path.getsize(path) / 1024:>11.1f}")
    print()
    print("  Rows 1-3 draw every cell; row 4 has four times the data of row 3 but")
    print("  the default cap, and is back to the cost of row 2. Time and file")
    print("  size follow the number of DRAWN quads, not the number of numbers.")

    # The alternative: one 2-D panel per section, each quantitatively readable.
    X, Y, Z = anomaly_surface(180)
    fig, axes = plt.subplots(1, 3, figsize=(10.5, 3.2), dpi=150,
                             sharey=True)
    for ax, y_target in zip(axes, (-3.0, 0.0, 3.0)):
        k = int(np.argmin(np.abs(Y[:, 0] - y_target)))
        ax.plot(X[k, :], Z[k, :], color="C0", lw=1.4)
        ax.fill_between(X[k, :], Z[k, :], color="C0", alpha=0.18, linewidth=0)
        ax.axhline(0.0, color="0.6", lw=0.6)
        ax.set_xlim(-10, 10)
        ax.set_title(f"section at y = {Y[k, 0]:+.1f} km", fontsize=9)
        ax.set_xlabel("x (km)")
        ax.grid(True, lw=0.4, alpha=0.35)
    axes[0].set_ylabel("anomaly (mGal, SYNTHETIC)")
    fig.suptitle("Three sections of the same field: quantitative and unoccluded",
                 fontsize=10)
    fig.tight_layout()
    path = os.path.join(OUTDIR, "04_slices.png")
    t0 = time.perf_counter()
    fig.savefig(path, dpi=150)
    dt = time.perf_counter() - t0
    plt.close(fig)
    print(f"\n  3 section panels, 180 x 180 of data: {dt:.3f} s,"
          f" {os.path.getsize(path) / 1024:.1f} kB")
    print("  Each amplitude is read against a labelled axis, the horizontal")
    print("  scale is true, and nothing is hidden behind anything. A 3-D view")
    print("  earns its place when the *shape* is the message; stacked sections")
    print("  win whenever a number is.")

    # The alternative: one 2-D panel per section, each quantitatively readable.
    X, Y, Z = anomaly_surface(180)
    fig, axes = plt.subplots(1, 3, figsize=(10.5, 3.2), dpi=150,
                             sharey=True)
    for ax, y_target in zip(axes, (-3.0, 0.0, 3.0)):
        k = int(np.argmin(np.abs(Y[:, 0] - y_target)))
        ax.plot(X[k, :], Z[k, :], color="C0", lw=1.4)
        ax.fill_between(X[k, :], Z[k, :], color="C0", alpha=0.18, linewidth=0)
        ax.axhline(0.0, color="0.6", lw=0.6)
        ax.set_xlim(-10, 10)
        ax.set_title(f"section at y = {Y[k, 0]:+.1f} km", fontsize=9)
        ax.set_xlabel("x (km)")
        ax.grid(True, lw=0.4, alpha=0.35)
    axes[0].set_ylabel("anomaly (mGal, SYNTHETIC)")
    fig.suptitle("Three sections of the same field: quantitative and unoccluded",
                 fontsize=10)
    fig.tight_layout()
    path = os.path.join(OUTDIR, "04_slices.png")
    t0 = time.perf_counter()
    fig.savefig(path, dpi=150)


def main():
    part1_viewpoint_changes_the_picture()
    part2_occlusion_ambiguity()
    part3_primitive_count()
    part4_cost_and_the_alternative()
    print()
    print("Images written to:", OUTDIR)
    print("Nothing was written inside the repository.")


if __name__ == "__main__":
    main()
