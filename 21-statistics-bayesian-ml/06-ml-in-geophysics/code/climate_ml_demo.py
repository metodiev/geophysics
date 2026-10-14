#!/usr/bin/env python3
"""Statistical downscaling: interpolation, a linear emulator and a quadratic one.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python climate_ml_demo.py

Everything here is SYNTHETIC.  The coarse fields, the elevation grid, the
regime-dependent lapse rate and the fine-scale truth are generated below; no
reanalysis, no climate model output and no station record is read.

Sections
--------
1. The synthetic coarse-to-fine problem.
2. Four evaluation splits of one fitted emulator.
3. Interpolation versus emulation on every split.
4. Which number a reader would have been shown, and which one matters.
"""

import numpy as np
from scipy.ndimage import zoom

RNG = np.random.default_rng(20261014)

NC = 6                  # coarse cells per side
FACTOR = 3              # fine cells per coarse cell
NF = NC * FACTOR        # fine cells per side
NMONTH = 200            # monthly means
N_TRAIN = 150           # months used for fitting
LAPSE_WET = 6.5e-3      # K/m, western half of the domain
LAPSE_DRY = 3.0e-3      # K/m, eastern half of the domain
NOISE_K = 0.15          # fine-scale residual scatter, K


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def elevation_fields():
    yy, xx = np.mgrid[0:NF, 0:NF] / NF
    fine = (400.0 * np.sin(2.0 * np.pi * xx) * np.cos(2.0 * np.pi * yy)
            + 300.0 * np.sin(6.0 * np.pi * xx) * np.cos(6.0 * np.pi * yy)
            + 250.0 * xx - 100.0 * yy)
    fine = fine - fine.min()
    coarse = fine.reshape(NC, FACTOR, NC, FACTOR).mean(axis=(1, 3))
    return fine, coarse


def upsample_nearest(coarse):
    return np.repeat(np.repeat(coarse, FACTOR, axis=0), FACTOR, axis=1)


def main():
    section("1. The synthetic coarse-to-fine problem")
    elev_fine, elev_coarse = elevation_fields()
    elev_block = upsample_nearest(elev_coarse)
    xx = np.mgrid[0:NF, 0:NF][1] / NF
    lapse = LAPSE_DRY + (LAPSE_WET - LAPSE_DRY) / (1.0 + np.exp((xx - 0.5) * 40.0))

    t = np.arange(NMONTH)
    lat = np.linspace(3.0, -3.0, NC)[:, None] * np.ones((1, NC))
    seasonal = 3.0 * np.sin(2.0 * np.pi * t / 12.0)
    warming = 0.03 * t
    ar = np.zeros(NMONTH)
    for i in range(1, NMONTH):
        ar[i] = 0.8 * ar[i - 1] + 0.6 * RNG.standard_normal()
    T_coarse = (12.0 - 0.6 * lat[:, :, None] + seasonal[None, None, :]
                + warming[None, None, :] + ar[None, None, :])

    print(f"SYNTHETIC downscaling problem: coarse {NC}x{NC} cells, fine "
          f"{NF}x{NF} cells ({FACTOR}x{FACTOR} per coarse cell), "
          f"{NMONTH} monthly means")
    print("  coarse temperature: 12.0 - 0.6*lat + 3.0*sin(2 pi t/12) "
          "+ 0.03 t + AR(1) noise  [K]")
    print(f"  elevation {elev_fine.min():.0f} to {elev_fine.max():.0f} m; "
          f"lapse rate {LAPSE_WET * 1000:.1f} K/km in the west (x < 0.5) and "
          f"{LAPSE_DRY * 1000:.1f} K/km in the east")
    print(f"  fine truth: coarse value - lapse(x) x elevation anomaly")
    print(f"  + 0.8 tanh((T_coarse - 15 K)/4 K) + {NOISE_K:.2f} K noise")
    print(f"  mean coarse temperature: months 1-{N_TRAIN} = "
          f"{T_coarse[..., :N_TRAIN].mean():.2f} K, months "
          f"{N_TRAIN + 1}-{NMONTH} = {T_coarse[..., N_TRAIN:].mean():.2f} K")

    coarse_up = np.stack([upsample_nearest(T_coarse[..., m])
                          for m in range(NMONTH)], axis=0)
    dz = elev_fine - elev_block
    truth = (coarse_up - lapse[None, :, :] * dz[None, :, :]
             + 0.8 * np.tanh((coarse_up - 15.0) / 4.0)
             + NOISE_K * RNG.standard_normal((NMONTH, NF, NF)))

    tc = coarse_up.reshape(-1)
    dzr = np.tile(dz.ravel(), NMONTH)
    month_of = np.repeat(np.arange(NMONTH), NF * NF)
    east = np.tile((xx.ravel() >= 0.5), NMONTH)
    late = month_of >= N_TRAIN
    truth_flat = truth.reshape(-1)
    design = np.column_stack([np.ones(tc.size), tc, dzr])
    design_quad = np.column_stack([design, tc ** 2, tc * dzr])

    section("2. Four evaluation splits of one fitted emulator")
    print(f"  fitting uses the WESTERN half (x < 0.5) and months 1-{N_TRAIN} "
          f"only: {int((~east & ~late).sum())} fine-cell-months")
    print("  the four evaluation blocks are:")
    print(f"    in-sample        west half, months 1-{N_TRAIN}")
    print(f"    later period     west half, months {N_TRAIN + 1}-{NMONTH} "
          f"(warmer by "
          f"{T_coarse[..., N_TRAIN:].mean() - T_coarse[..., :N_TRAIN].mean():.2f} K)")
    print(f"    other region     east half, months 1-{N_TRAIN} (lapse-rate "
          f"regime changed)")
    print(f"    both shifts      east half, months {N_TRAIN + 1}-{NMONTH}")

    fit = ~east & ~late
    coef_lin, *_ = np.linalg.lstsq(design[fit], truth_flat[fit], rcond=None)
    coef_quad, *_ = np.linalg.lstsq(design_quad[fit], truth_flat[fit], rcond=None)
    print("  linear    (intercept, T_c, dz)                = "
          + ", ".join(f"{c:+.5f}" for c in coef_lin))
    print("  quadratic (intercept, T_c, dz, T_c^2, T_c*dz) = "
          + ", ".join(f"{c:+.5f}" for c in coef_quad))

    bilinear = np.stack([zoom(T_coarse[..., m], FACTOR, order=1,
                              mode="nearest") for m in range(NMONTH)]).reshape(-1)
    methods = (
        ("bilinear interpolation", bilinear),
        ("linear lapse-rate emulator", design @ coef_lin),
        ("quadratic emulator", design_quad @ coef_quad),
    )
    blocks = (
        ("in-sample (west, early)", ~east & ~late),
        ("later period (west, late)", ~east & late),
        ("other region (east, early)", east & ~late),
        ("both shifts (east, late)", east & late),
    )

    section("3. Interpolation versus emulation on every split")
    header = f"  {'method':<28s}" + "".join(f"{name.split(' (')[0]:>22s}"
                                            for name, _ in blocks)
    print(header + "   [RMSE in K, bias in parentheses]")
    for name, predict in methods:
        line = f"  {name:<28s}"
        for _label, mask in blocks:
            err = predict[mask] - truth_flat[mask]
            line += (f"{np.sqrt(np.mean(err ** 2)):>15.3f} "
                     f"({err.mean():+.3f})")
        print(line)

    section("4. Which number a reader would have been shown")
    for name, predict in methods:
        err_w = predict[~east] - truth_flat[~east]
        err_e = predict[east] - truth_flat[east]
        print(f"  {name:<28s} western half RMSE "
              f"{np.sqrt(np.mean(err_w ** 2)):.3f} K (bias {err_w.mean():+.3f}), "
              f"eastern half RMSE {np.sqrt(np.mean(err_e ** 2)):.3f} K "
              f"(bias {err_e.mean():+.3f})")
    lin = methods[1][1]
    e_w = lin[~east] - truth_flat[~east]
    e_e = lin[east] - truth_flat[east]
    r_w = np.sqrt(np.mean(e_w ** 2))
    r_e = np.sqrt(np.mean(e_e ** 2))
    print("  Fitting on the western half and validating on held-out cells and")
    print("  months from the SAME half gives an emulator that looks accurate.")
    print(f"  Applying it to the eastern half raises the RMSE from {r_w:.3f} K to")
    print(f"  {r_e:.3f} K, a factor of {r_e / r_w:.1f}, and the error is not a")
    print("  constant bias -- it is the mis-specified elevation response, because")
    print("  the western lapse rate is imposed on a region whose own lapse rate is")
    print("  weaker.  More data from the west would not fix it.")
    print("  The warming trend is the easier transfer: the temporal split alone")
    print("  leaves the linear emulator near 0.2 K, so a study that reports only")
    print("  that split has not tested transferability.")
    print("\nSYNTHETIC: these fields are generated here.  A real downscaling study")
    print("must state the reanalysis product, the station density, the elevation")
    print("dataset and the reference period, because all four enter the answer.")


if __name__ == "__main__":
    main()
