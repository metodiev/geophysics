#!/usr/bin/env python3
"""Gridding: interpolation is the invention of data you did not measure.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gridding_demo.py

The "truth" is an analytic potential-field anomaly evaluated on a fine grid.  It is
then sampled sparsely, and several interpolators are asked to rebuild the full
grid.  Every number printed is measured against the truth.

Contents
--------
1. Truth field and its peak, on a fine grid; a coarse grid and scattered stations.
2. Interpolator comparison (nearest, linear, cubic, inverse-distance weighting,
   thin-plate and multiquadric radial basis functions): RMS error and peak error.
3. The peak-anomaly spread between methods, quoted as a percentage of the true peak.
4. Undersampling: the same interpolator on grids of 400, 200 and 100 m spacing --
   the peak error grows and no interpolator can recover it.
5. Noise sensitivity: interpolation of noisy data, showing that an interpolator
   that fits the samples exactly (RBF, cubic) also fits the noise.
"""

import numpy as np
from scipy.interpolate import griddata, Rbf

G = 6.67430e-11
MGAL = 1.0e-5
RNG_SEED = 20261014


def anomaly_mgal(x, y):
    """Vertical gravity of two point masses at depths 400 and 900 m (mGal).

    The bodies are deliberately placed OFF the coarse grid nodes, so that the
    anomaly peak falls between samples: that is the case that exposes the
    interpolator.
    """
    m1, h1, x1, y1 = 8.0e9, 400.0, 1150.0, 1250.0
    m2, h2, x2, y2 = 3.0e10, 900.0, 2650.0, 2750.0
    def pm(mass, h, xc, yc):
        r = np.sqrt((x - xc) ** 2 + (y - yc) ** 2 + h ** 2)
        return G * mass * h / r ** 3
    return (pm(m1, h1, x1, y1) + pm(m2, h2, x2, y2)) / MGAL


def idw(xs, ys, vs, xq, yq, power=2.0):
    """Inverse-distance weighting with a cutoff for numerical sanity."""
    out = np.empty_like(xq, dtype=float)
    for i in range(xq.size):
        d = np.hypot(xs - xq[i], ys - yq[i])
        if np.min(d) < 1e-9:
            out[i] = vs[np.argmin(d)]
            continue
        w = 1.0 / d ** power
        out[i] = float(np.sum(w * vs) / np.sum(w))
    return out


def main() -> None:
    rng = np.random.default_rng(RNG_SEED)
    extent = 4000.0

    # --- 1. Truth ----------------------------------------------------------
    n_fine = 201
    xf = np.linspace(0.0, extent, n_fine)
    gx, gy = np.meshgrid(xf, xf)
    truth = anomaly_mgal(gx, gy)
    print("1. Truth field")
    print(f"   fine grid {n_fine} x {n_fine}, spacing {extent/(n_fine-1):.1f} m")
    print(f"   peak anomaly (fine grid)   = {truth.max():.5f} mGal")
    print(f"   RMS deviation from 0       = {truth.std():.5f} mGal")

    # --- 2. Interpolators from a coarse grid -------------------------------
    n_coarse = 21                     # 200 m spacing
    xc = np.linspace(0.0, extent, n_coarse)
    cx, cy = np.meshgrid(xc, xc)
    vc = anomaly_mgal(cx, cy)
    # Scattered stations: a jittered subset of the coarse nodes.
    n_scatter = 400
    sx = rng.uniform(0.0, extent, n_scatter)
    sy = rng.uniform(0.0, extent, n_scatter)
    sv = anomaly_mgal(sx, sy)

    pts_grid = np.column_stack([cx.ravel(), cy.ravel()])
    v_grid = vc.ravel()
    q = np.column_stack([gx.ravel(), gy.ravel()])

    print(f"\n2. Rebuilding the fine grid from a {n_coarse} x {n_coarse} grid "
          f"({extent/(n_coarse-1):.0f} m spacing)")
    print(f"   {'method':<22}{'RMS error (mGal)':>18}{'peak (mGal)':>14}"
          f"{'peak error (%)':>16}")
    results = {}
    for name, vals in (
        ("nearest", griddata(pts_grid, v_grid, q, method="nearest")),
        ("linear", griddata(pts_grid, v_grid, q, method="linear")),
        ("cubic", griddata(pts_grid, v_grid, q, method="cubic")),
        ("inverse distance p=2", idw(cx.ravel(), cy.ravel(), v_grid, q[:, 0], q[:, 1], 2.0)),
        ("inverse distance p=4", idw(cx.ravel(), cy.ravel(), v_grid, q[:, 0], q[:, 1], 4.0)),
    ):
        field = vals.reshape(n_fine, n_fine)
        err = float(np.sqrt(np.mean((field - truth) ** 2)))
        results[name] = field
        print(f"   {name:<22}{err:>18.5f}{field.max():>14.5f}"
              f"{(field.max()/truth.max()-1)*100:>16.2f}")
    for name, fn in (("thin-plate RBF", "thin_plate"),
                     ("multiquadric RBF", "multiquadric")):
        rbf = Rbf(cx.ravel(), cy.ravel(), v_grid, function=fn, smooth=0.0)
        field = rbf(gx, gy)
        err = float(np.sqrt(np.mean((field - truth) ** 2)))
        results[name] = field
        print(f"   {name:<22}{err:>18.5f}{field.max():>14.5f}"
              f"{(field.max()/truth.max()-1)*100:>16.2f}")

    # --- 3. Spread between methods ----------------------------------------
    peaks = np.array([f.max() for f in results.values()])
    print("\n3. Peak anomaly across methods")
    print(f"   minimum peak over methods = {peaks.min():.5f} mGal")
    print(f"   maximum peak over methods = {peaks.max():.5f} mGal")
    print(f"   spread                    = {peaks.max()-peaks.min():.5f} mGal"
          f"  = {(peaks.max()-peaks.min())/truth.max()*100:.1f} % of the true peak")
    print("   -> the CHOICE OF INTERPOLATOR moves the anomaly peak by a few per cent")
    print("      without any change to the data. That is a processing artefact")
    print("      masquerading as geology, and it must be reported.")

    # --- 4. Undersampling --------------------------------------------------
    print("\n4. Undersampling: linear interpolation at three grid spacings")
    print(f"   {'spacing (m)':>12}{'samples':>10}{'RMS error':>13}"
          f"{'peak (mGal)':>14}{'peak error (%)':>16}")
    for n_coarse in (5, 9, 17, 41):        # 1000, 500, 250, 100 m
        xc2 = np.linspace(0.0, extent, n_coarse)
        c2x, c2y = np.meshgrid(xc2, xc2)
        v2 = anomaly_mgal(c2x, c2y)
        f2 = griddata(np.column_stack([c2x.ravel(), c2y.ravel()]), v2.ravel(), q,
                      method="linear").reshape(n_fine, n_fine)
        print(f"   {extent/(n_coarse-1):>12.0f}{n_coarse**2:>10}"
              f"{float(np.sqrt(np.mean((f2-truth)**2))):>13.5f}"
              f"{f2.max():>14.5f}{(f2.max()/truth.max()-1)*100:>16.2f}")
    print("   -> interpolation cannot create information. Between samples the field")
    print("      is guessed, and the guess is wrong by an amount that grows as the")
    print("      sample spacing grows.")

    # --- 5. Noise and exact-fitting interpolators --------------------------
    sigma = 0.005
    v_noisy = v_grid + rng.normal(0.0, sigma, v_grid.size)
    print(f"\n5. Interpolating NOISY samples (sigma = {sigma:.3f} mGal, "
          f"{n_coarse}x{n_coarse} grid)")
    print(f"   {'method':<22}{'RMS vs truth':>15}{'RMS of value AT samples':>26}")
    for name, vals in (
        ("linear", griddata(pts_grid, v_noisy, q, method="linear")),
        ("cubic", griddata(pts_grid, v_noisy, q, method="cubic")),
    ):
        field = vals.reshape(n_fine, n_fine)
        at_samples = griddata(pts_grid, v_noisy, pts_grid, method=name)
        print(f"   {name:<22}{float(np.sqrt(np.mean((field-truth)**2))):>15.5f}"
              f"{float(np.std(at_samples-v_grid)):>26.5f}")
    rbf = Rbf(pts_grid[:, 0], pts_grid[:, 1], v_noisy, function="multiquadric", smooth=0.0)
    field = rbf(gx, gy)
    at_samples = rbf(pts_grid[:, 0], pts_grid[:, 1])
    print(f"   {'multiquadric RBF':<22}"
          f"{float(np.sqrt(np.mean((field-truth)**2))):>15.5f}"
          f"{float(np.std(at_samples-v_grid)):>26.5f}")
    print("   -> an interpolator that reproduces the samples exactly also reproduces")
    print("      their noise (column 3 equals the input sigma). Interpolation is not")
    print("      filtering: the noise passes straight through, and often grows.")


if __name__ == "__main__":
    main()
