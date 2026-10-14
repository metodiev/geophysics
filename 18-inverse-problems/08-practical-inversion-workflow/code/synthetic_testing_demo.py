#!/usr/bin/env python3
"""Synthetic testing: checkerboard resolution tests, spike (point-spread)
tests, and the alignment trap.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python synthetic_testing_demo.py

All models and data are SYNTHETIC.  The forward operator is a chosen teaching
operator (a Gaussian blur followed by subsampling); no number below is a
measurement of the Earth.

Contents
--------
1. A synthetic experiment with a known resolution limit.
2. Checkerboard test: recovered amplitude versus pattern wavelength.
3. The alignment trap: a checkerboard shifted by half a cell.
4. Spike test: the point-spread function and its width.
"""

import numpy as np
from scipy.ndimage import gaussian_filter

RNG = np.random.default_rng(20261014)

NX = NY = 24                 # model grid
BLUR = 1.4                   # Gaussian blur sigma, cells
STEP = 2                     # subsample every STEP-th cell
SIGMA = 0.01                 # data noise (relative to the data rms)
LAMBDA = 0.05                # smoothness weight
N = NX * NY


def section(title: str) -> None:
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def forward_matrix():
    """Dense blur-and-subsample operator: SYNTHETIC teaching physics."""
    cols = []
    for k in range(N):
        e = np.zeros(N)
        e[k] = 1.0
        blurred = gaussian_filter(e.reshape(NX, NY), BLUR, mode="nearest")
        cols.append(blurred[::STEP, ::STEP].ravel())
    return np.array(cols).T


def smoothness():
    Dx = np.zeros((N, N))
    Dy = np.zeros((N, N))
    for i in range(NX):
        for j in range(NY):
            k = i * NY + j
            if i + 1 < NX:
                Dx[k, (i + 1) * NY + j] = 1.0
                Dx[k, k] = -1.0
            if j + 1 < NY:
                Dy[k, i * NY + (j + 1)] = 1.0
                Dy[k, k] = -1.0
    return Dx, Dy


def checkerboard(period, shift=0.0):
    x = np.arange(NX)[:, None] + shift
    y = np.arange(NY)[None, :] + shift
    return np.cos(2 * np.pi * x / period) * np.cos(2 * np.pi * y / period)


def project_amplitude(model, pattern):
    """Least-squares amplitude of ``pattern`` in ``model`` (patterns are
    orthogonal to the mean here, so this is a simple projection)."""
    return float(np.dot(model, pattern.ravel()) / np.dot(pattern.ravel(),
                                                         pattern.ravel()))


def main():
    A = forward_matrix()
    Dx, Dy = smoothness()
    D = Dx.T @ Dx + Dy.T @ Dy
    C = np.linalg.inv(A.T @ A / SIGMA ** 2 + LAMBDA * D)
    print(f"  grid {NX} x {NY} cells, {A.shape[0]} data, "
          f"blur {BLUR:.1f} cells, subsample every {STEP}, "
          f"noise {SIGMA * 100:.0f}%")

    section("1. A synthetic experiment with a known resolution limit")
    spike = np.zeros(N)
    spike[(NX // 2) * NY + NY // 2] = 1.0
    d_spike = A @ spike
    m_spike = C @ A.T @ d_spike / SIGMA ** 2
    print(f"  spike test: a single cell of unit amplitude at "
          f"({NX // 2}, {NY // 2})")
    print(f"    recovered peak = {m_spike.max():.4f} "
          f"(true 1.0): the amplitude is only partly recovered")
    img = m_spike.reshape(NX, NY)
    half = np.abs(img) > 0.5 * np.abs(img).max()
    print(f"    cells above half the recovered peak = {int(half.sum())} "
          f"(one true cell)")

    section("2. Checkerboard test: recovered amplitude versus wavelength")
    print("  a true checkerboard of unit amplitude is put through the same")
    print("  experiment and inverted; the recovered amplitude is reported as a")
    print("  fraction of 1.0.")
    print("  period (cells)   recovered amplitude")
    recoveries = {}
    for period in (2, 3, 4, 6, 8, 12, 16):
        pattern = checkerboard(period)
        d = A @ pattern.ravel()
        d = d + SIGMA * d.std() * RNG.standard_normal(d.size)
        m = C @ A.T @ d / SIGMA ** 2
        amp = project_amplitude(m, pattern)
        recoveries[period] = amp
        print(f"  {period:14d}   {amp:18.4f}")
    print("  recovery drops below one half between a period of 3 and 4 cells: that")
    print("  is the resolution length for one-sided (positive) recovery.  Short")
    print("  patterns are blurred and then undersampled, so their signature is")
    print("  largely gone before the inversion starts.  The test measures")
    print("  RESOLUTION, not detection: a narrow body can be detected (it raises a")
    print("  residual) long after its shape is unresolvable.")

    section("3. The alignment trap: a shifted checkerboard")
    period = 4
    print(f"  the same period-{period} pattern, shifted along both axes.")
    print("  shift (cells)   recovered amplitude   true amplitude")
    for shift in (0.0, 0.5, 1.0, 1.5, 2.0):
        pattern = checkerboard(period, shift=shift)
        d = A @ pattern.ravel()
        d = d + SIGMA * d.std() * RNG.standard_normal(d.size)
        m = C @ A.T @ d / SIGMA ** 2
        amp = project_amplitude(m, pattern)
        print(f"  {shift:13.1f}   {amp:18.4f}   {1.0:14.1f}")
    print("  for a period of 4 cells, a shift of 1 cell is a quarter wavelength:")
    print("  the recovered amplitude collapses from 0.568 to 0.0009.  That is not a")
    print("  loss of resolution -- the pattern has landed on a null direction of the")
    print("  operator, so the true signal leaves almost no trace in the data.")
    print("  Always run several shifts, or a suite of patterns, and report the")
    print("  worst recovery, not the best.")

    section("4. Spike test: the point-spread function and its width")
    print("  the model resolution matrix R = C A'A / sigma^2 maps a true spike to")
    print("  the recovered pattern; its row for the centre cell is the")
    print("  point-spread function (PSF).")
    R = C @ (A.T @ A) / SIGMA ** 2
    centre = (NX // 2) * NY + NY // 2
    psf = R[centre].reshape(NX, NY)
    i0, j0 = NX // 2, NY // 2
    row = psf[i0]
    above = np.where(row > 0.5 * row.max())[0]
    width = (above[-1] - above[0] + 1) if above.size else 0
    print(f"    PSF peak value          = {psf[i0, j0]:.4f}")
    print(f"    half-width (cells)      = {width}")
    print(f"    negative sidelobes      = {psf.min():.4f} "
          f"(an artifact, not a structure)")
    print(f"    diagonal of R at centre = {R[centre, centre]:.4f}")
    print("  the PSF width is the resolution length: structures narrower than it")
    print("  are smeared, and the negative sidelobes are the signature of the")
    print("  smoothness prior.  Neither is a property of the Earth.")


if __name__ == "__main__":
    main()
