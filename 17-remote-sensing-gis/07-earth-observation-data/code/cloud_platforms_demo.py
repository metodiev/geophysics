#!/usr/bin/env python3
"""Cloud platforms: a synthetic lazy data cube, cloud masking, temporal
compositing, and the arithmetic of compute-at-source versus download.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python cloud_platforms_demo.py

Everything here is SYNTHETIC.  The cube, cloud cover, mask accuracy, band count
and archive "versions" are chosen teaching values, not measurements.  No file is
read or written, no account or network access is used.

Contents
--------
1. A synthetic observation cube and its download volume.
2. Temporal compositing with and without a cloud mask.
3. Valid-observation counts, and pixels that never clear.
4. An archive version change and its effect on the composite.
5. Compute-at-source versus download: the egress arithmetic.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

T = 60           # observations in the stack
H, W = 8, 8      # pixels
BYTES_PER_VALUE = 4      # float32 payload, bytes
N_BANDS = 3


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def main():
    # --- SYNTHETIC cube: surface reflectance + season + noise ---------------
    base = RNG.uniform(0.10, 0.35, size=(H, W))
    season = 0.08 * np.sin(2.0 * np.pi * np.arange(T) / 12.0)
    # cloud probability is not uniform: one corner sits under persistent cloud
    cloud_prob = np.full((H, W), 0.15)
    cloud_prob[:2, :3] = 0.85
    cloud_corner = np.zeros((H, W), dtype=bool)
    cloud_corner[:2, :3] = True
    clean = base[None, :, :] + season[:, None, None] + RNG.normal(0.0, 0.02, (T, H, W))
    # clouds are real, but a mask detects only a fraction of them
    cloud_true = RNG.random((T, H, W)) < cloud_prob[None, :, :]
    cloud_flag = cloud_true & (RNG.random((T, H, W)) < 0.80)   # 20% of clouds missed
    observed = np.where(cloud_true, clean + 0.25, clean)        # clouds are bright

    section("1. The synthetic cube and its size (SYNTHETIC)")
    print(f"cube shape = {observed.shape} (time x rows x cols), "
          f"{N_BANDS} bands if band-stacked")
    volume = T * H * W * N_BANDS * BYTES_PER_VALUE
    print(f"payload for one band = {T * H * W * BYTES_PER_VALUE / 1024:.1f} KiB")
    print(f"payload for {N_BANDS} bands    = {volume / 1024:.1f} KiB")
    print("Multiply by scene area and stack length to get the archive-scale")
    print("number; the point is that this is the quantity a download bill counts.")

    section("2. Temporal compositing: the mask matters (SYNTHETIC)")
    comp_raw = np.median(observed, axis=0)
    obs_masked = observed.copy()
    obs_masked[cloud_flag] = np.nan
    comp_masked = np.nanmedian(obs_masked, axis=0)
    # truth: composite of the clear observations
    truth = np.median(clean, axis=0)
    err_raw = comp_raw - truth
    err_masked = comp_masked - truth
    print(f"mean reflectance, unmasked median = {comp_raw.mean():.4f}")
    print(f"mean reflectance, masked median   = {comp_masked.mean():.4f}")
    print(f"clear-sky truth                   = {truth.mean():.4f}")
    print(f"mean bias, unmasked = {err_raw.mean():+.4f}; "
          f"rms = {np.sqrt(np.mean(err_raw ** 2)):.4f}")
    print(f"mean bias, masked   = {err_masked.mean():+.4f}; "
          f"rms = {np.sqrt(np.mean(err_masked ** 2)):.4f}")
    worst = np.unravel_index(np.abs(err_masked).argmax(), err_masked.shape)
    print(f"worst masked error  = {np.abs(err_masked).max():.4f} at row {worst[0]}, "
          f"col {worst[1]}")
    print(f"mean |error| in the cloudy corner, masked = "
          f"{np.abs(err_masked[cloud_corner]).mean():.4f}")
    print(f"mean |error| elsewhere, masked            = "
          f"{np.abs(err_masked[~cloud_corner]).mean():.4f}")
    print("A median is robust to a minority of bright clouds, so unmasked")
    print("compositing is not catastrophic -- but it is biased, and the bias")
    print("is largest where cloud cover is high. The mask is a model, not data.")

    section("3. Valid-observation counts and the mask's blind spot (SYNTHETIC)")
    valid_flagged = (~cloud_flag).sum(axis=0)     # what the mask says is clear
    valid_true = (~cloud_true).sum(axis=0)        # what is actually clear
    print(f"flagged cloud-free obs per pixel: min = {valid_flagged.min()}, "
          f"mean = {valid_flagged.mean():.1f}, max = {valid_flagged.max()} of {T}")
    print(f"actually clear    obs per pixel: min = {valid_true.min()}, "
          f"mean = {valid_true.mean():.1f}, max = {valid_true.max()} of {T}")
    print(f"the mask over-counts clear looks by "
          f"{(valid_flagged - valid_true).mean():.1f} obs on average")
    need = 25
    print(f"pixels with fewer than {need} actually-clear observations = "
          f"{(valid_true < need).sum()} of {valid_true.size} "
          f"(all in the cloudy corner: {cloud_corner.sum()} pixels)")
    print("A composite is only as good as the number of clear looks behind it,")
    print("and the mask's false negatives inflate that count. Report both the")
    print("count and the mask, because a smooth-looking pixel is still a gap.")

    section("4. An archive version change shifts the product (SYNTHETIC)")
    # version B recalibrates with a small additive offset
    offset_b = 0.010
    comp_b = np.median(observed + offset_b, axis=0)
    print(f"composite, version A mean = {comp_raw.mean():.4f}")
    print(f"composite, version B mean = {comp_b.mean():.4f}")
    print(f"shift from the reprocessing = {(comp_b - comp_raw).mean():+.4f}")
    print("Two identical requests against different archive versions return")
    print("different numbers. A reproducible result pins the version.")

    section("5. Compute-at-source versus download (SYNTHETIC arithmetic)")
    n_pixels = 10_000 * 10_000          # a full scene
    n_obs = 200
    full_bytes = n_pixels * n_obs * N_BANDS * BYTES_PER_VALUE
    print(f"full stack = {n_pixels * n_obs * N_BANDS} values "
          f"= {full_bytes / 1e9:.2f} GB (decimal)")
    # computing a single summary at source returns one value per pixel
    out_bytes = n_pixels * BYTES_PER_VALUE
    print(f"a one-number-per-pixel summary returned = {out_bytes / 1e6:.1f} MB")
    print(f"ratio download : compute = {full_bytes / out_bytes:.0f} : 1")
    print("Moving the reducer to the archive avoids the egress, but the reducer")
    print("(mask, compositor, resampler) is then part of the result and must be")
    print("recorded, because it, not the pixels, decides the answer.")


if __name__ == "__main__":
    main()
