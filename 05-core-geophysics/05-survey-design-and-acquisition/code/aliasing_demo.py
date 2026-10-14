#!/usr/bin/env python3
"""Spatial aliasing: a sinusoid sampled too coarsely appears at the wrong wavelength.

Everything printed here is computed by this file. Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python aliasing_demo.py

Contents
--------
1. Exact folding of a true wavenumber into the first Nyquist zone, in closed form.
2. A coarse and a fine sampling of the SAME 100 m sinusoid; least-squares fits of
   sinusoids at the true and at the *apparent* wavelength, with the residuals.
3. Proof by construction that the coarse samples are exactly fitted by a genuine
   sinusoid of a different wavelength: the two fields are indistinguishable at the
   sample locations, so no processing step can separate them.
4. The measured spectrum of the coarse samples, showing that the analysis band ends
   at the Nyquist wavenumber and that the true wavenumber lies outside it.
"""

import numpy as np

# --- survey parameters (SYNTHETIC; chosen to make the fold clean) -------------
TRUE_WAVELENGTH_M = 100.0     # m, the geological wavelength actually present
FINE_DX_M = 2.0               # m, "ground truth" sampling for plotting
COARSE_DX_M = 60.0            # m, the too-coarse survey spacing (Nyquist = 50 m)
PROFILE_LENGTH_M = 600.0      # m


def fold_wavenumber(k: np.ndarray | float, k_nyq: float) -> np.ndarray:
    """Fold a signed wavenumber into the first Nyquist zone [-k_nyq, k_nyq)."""
    return (k + k_nyq) % (2.0 * k_nyq) - k_nyq


def fit_sinusoid(x: np.ndarray, y: np.ndarray, wavelength: float) -> tuple[float, float, float]:
    """Least-squares fit y ~ A cos(2 pi x / lam) + B sin(2 pi x / lam).

    Returns (amplitude, phase, rms_residual). A linear least-squares problem in
    (A, B); the residual tells us how well the samples are described by a pure
    sinusoid of the stated wavelength.
    """
    k = 2.0 * np.pi / wavelength
    design = np.column_stack([np.cos(k * x), np.sin(k * x)])
    coeffs, *_ = np.linalg.lstsq(design, y, rcond=None)
    model = design @ coeffs
    amp = float(np.hypot(*coeffs))
    phase_deg = float(np.degrees(np.arctan2(-coeffs[1], coeffs[0])))
    if abs(phase_deg) < 1e-9:
        phase_deg = 0.0
    rms = float(np.sqrt(np.mean((y - model) ** 2)))
    return amp, phase_deg, rms


def main() -> None:
    # --- 1. The survey grid and the field ------------------------------------
    dx = COARSE_DX_M
    # 10 samples: the folded wavenumber then lands exactly on a DFT bin, so the
    # measured spectral peak can be compared with the closed-form fold.
    x_coarse = np.arange(0.0, PROFILE_LENGTH_M, dx)
    k_true = 2.0 * np.pi / TRUE_WAVELENGTH_M          # rad/m
    k_nyq = np.pi / dx                                # rad/m
    y_coarse = np.cos(k_true * x_coarse)              # unit-amplitude sinusoid

    k_app = float(fold_wavenumber(k_true, k_nyq))
    lam_app = 2.0 * np.pi / abs(k_app)

    print("1. Sampling parameters and the folded wavenumber")
    print(f"   true wavelength                 = {TRUE_WAVELENGTH_M:.3f} m")
    print(f"   true wavenumber k               = {k_true:.6f} rad/m")
    print(f"   station spacing dx              = {dx:.3f} m")
    print(f"   Nyquist wavelength 2 dx         = {2.0 * dx:.3f} m")
    print(f"   Nyquist wavenumber k_N = pi/dx  = {k_nyq:.6f} rad/m")
    print(f"   k_true / k_N                    = {k_true / k_nyq:.4f}  (> 1 means aliased)")
    print(f"   folded (apparent) wavenumber    = {k_app:.6f} rad/m")
    print(f"   apparent wavelength 2 pi/|k_app|= {lam_app:.3f} m")
    print(f"   sample count in profile         = {x_coarse.size}")

    # --- 2. Is the apparent sinusoid an exact description of the samples? -----
    amp_app, phase_app, rms_app = fit_sinusoid(x_coarse, y_coarse, lam_app)
    amp_true, phase_true, rms_true = fit_sinusoid(x_coarse, y_coarse, TRUE_WAVELENGTH_M)
    max_gap = float(np.max(np.abs(
        amp_app * np.cos(k_app * x_coarse - np.radians(phase_app))
        - amp_true * np.cos(k_true * x_coarse - np.radians(phase_true)))))
    print("\n2. Least-squares description of the coarse samples")
    print(f"   fit at apparent wavelength {lam_app:.3f} m:")
    print(f"        amplitude = {amp_app:.6f}   phase = {phase_app:+.3f} deg   rms residual = {rms_app:.3e}")
    print(f"   fit at true wavelength     {TRUE_WAVELENGTH_M:.3f} m:")
    print(f"        amplitude = {amp_true:.6f}   phase = {phase_true:+.3f} deg   rms residual = {rms_true:.3e}")
    print(f"   max |apparent fit - true fit| at the samples = {max_gap:.3e}")
    print("   -> BOTH fits are exact to machine precision. The record does not")
    print("      prefer either Earth; that is what 'aliased' means.")

    # --- 3. Two different fields, identical samples --------------------------
    # A genuine sinusoid of the apparent wavelength, sampled on the same grid.
    y_apparent = np.cos(k_app * x_coarse)
    max_diff = float(np.max(np.abs(y_coarse - y_apparent)))
    print("\n3. Indistinguishability of the alias")
    print(f"   max |true samples - apparent-wavelength samples| = {max_diff:.3e}")
    print("   -> the two distinct Earths give the same numbers on the grid;")
    print("      no processing step can tell which one was measured.")

    # --- 4. Where is the energy in the sampled spectrum? ---------------------
    y = y_coarse - y_coarse.mean()
    n = y.size
    spec = np.abs(np.fft.rfft(y)) / n
    freqs = np.fft.rfftfreq(n, d=dx)                  # cycles/m
    k_bins = 2.0 * np.pi * freqs                      # rad/m
    peak = int(np.argmax(spec))
    print("\n4. Spectrum of the coarse samples (length n = %d)" % n)
    print(f"   representable band |k| <= k_N = {k_nyq:.6f} rad/m")
    print(f"   peak spectral bin  k = {k_bins[peak]:+.6f} rad/m  "
          f"(wavelength {2*np.pi/abs(k_bins[peak]):.3f} m)")
    print(f"   folded wavenumber  k = {k_app:+.6f} rad/m  "
          f"(wavelength {lam_app:.3f} m)  [closed form, section 1]")
    print(f"   |k_true| = {k_true:.6f} rad/m vs k_N = {k_nyq:.6f} rad/m: "
          f"ratio {k_true/k_nyq:.3f}")
    print("   -> the true wavenumber lies OUTSIDE the representable band, so the")
    print("      measured peak can only sit at the folded wavenumber. A low-pass")
    print("      filter would remove the peak and leave nothing, not the truth.")

    # --- 5. What a finer grid would have shown -------------------------------
    x_fine = np.arange(0.0, PROFILE_LENGTH_M + FINE_DX_M, FINE_DX_M)
    y_fine = np.cos(k_true * x_fine)
    amp_fine, _, rms_fine = fit_sinusoid(x_fine, y_fine, TRUE_WAVELENGTH_M)
    print("\n5. Same field sampled at dx = %.1f m (below Nyquist)" % FINE_DX_M)
    print(f"   fit at true wavelength: amplitude = {amp_fine:.6f}, rms residual = {rms_fine:.3e}")

    print("\nSummary")
    print(f"   a {TRUE_WAVELENGTH_M:.0f} m anomaly sampled every {dx:.0f} m is reported as "
          f"a {lam_app:.0f} m anomaly, with a {rms_app:.1e} fit residual.")


if __name__ == "__main__":
    main()
