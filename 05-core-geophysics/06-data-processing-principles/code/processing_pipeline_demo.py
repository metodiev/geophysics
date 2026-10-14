#!/usr/bin/env python3
"""The processing chain, step by step: what each step fixes and what it destroys.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python processing_pipeline_demo.py

The synthetic "truth" is a gravity profile from two buried spheres plus a smooth
regional field.  The "observed" data add three spikes, a linear instrument drift
and Gaussian noise.  Every stage is measured against the truth, so the cost of
each step is a number rather than an opinion.

Contents
--------
1. Build truth and contaminated data; report the initial error.
2. EDIT: despiking.  A robust noise scale is estimated from adjacent differences;
   the trap of estimating it from a running-median residual is measured, not
   asserted.
3. TIE / LEVEL: remove a straight line.  Report how much of the REAL anomaly the
   levelling also removes -- the step is not free.
4. FILTER: sweep the cutoff wavelength of a zero-phase Gaussian low-pass and find
   the cutoff that actually minimises the error.  Noise reduction and signal loss
   are both measured.
5. TRANSFORM: first derivative.  Measure the noise gain as a function of sample
   spacing and compare it with the derived value sigma * k_N / sqrt(3).
6. Summary table: RMS error against the truth after each cumulative stage.
"""

import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

G = 6.67430e-11
MGAL = 1.0e-5
RNG_SEED = 20261014


def sphere_gz(x, mass, depth):
    return G * mass * depth / (x ** 2 + depth ** 2) ** 1.5 / MGAL


def robust_sigma(y):
    """Robust noise scale from adjacent differences (von Neumann / Immerkaer).

    For white noise of standard deviation s the successive differences have
    standard deviation s*sqrt(2), so

        sigma_hat = 1.4826 * median|diff - median(diff)| / sqrt(2).

    Half the differences would have to be outliers before this fails.
    """
    d = np.diff(y)
    mad = np.median(np.abs(d - np.median(d)))
    return float(1.4826 * mad / np.sqrt(2.0))


def running_median_mad(y, window=5):
    """The NAIVE scale: MAD of the residual from a running median.

    Reported only to show that it fails: the residual is exactly zero whenever the
    sample happens to be the middle value of its own window, which happens with
    probability 1/window, so the MAD is far too small.
    """
    pad = window // 2
    med = np.median(sliding_window_view(np.pad(y, pad, mode="edge"), window), axis=-1)
    resid = y - med
    mad = np.median(np.abs(resid - np.median(resid)))
    return float(1.4826 * mad), med


def gaussian_lowpass(y, dx, cutoff_wavelength):
    """Fourier low-pass with a Gaussian transfer function; zero phase."""
    n = y.size
    k = 2.0 * np.pi * np.fft.rfftfreq(n, d=dx)
    kc = 2.0 * np.pi / cutoff_wavelength
    H = np.exp(-0.5 * (k / kc) ** 2)
    return np.fft.irfft(np.fft.rfft(y) * H, n=n)


def main() -> None:
    rng = np.random.default_rng(RNG_SEED)

    def rms(a, b):
        return float(np.sqrt(np.mean((a - b) ** 2)))

    # --- 1. Truth and contaminated data -------------------------------------
    dx = 25.0
    x = np.arange(0.0, 5000.0, dx)
    truth = (sphere_gz(x - 1500.0, 1.2e10, 250.0)
             + sphere_gz(x - 3200.0, 6.0e9, 400.0)
             + 0.004 * (x - x.mean()) / 1000.0)
    drift = 0.02 * (x - x[0]) / 1000.0
    noise = rng.normal(0.0, 0.008, size=x.size)
    spikes = np.zeros_like(x)
    spike_idx = np.array([37, 121, 168])
    spikes[spike_idx] = np.array([0.9, -0.7, 1.4])
    observed = truth + drift + noise + spikes

    print("1. Synthetic profile")
    print(f"   samples                 = {x.size}, spacing = {dx:.0f} m")
    print(f"   true anomaly peak       = {truth.max():.4f} mGal")
    print(f"   spike amplitudes (mGal) = {spikes[spike_idx]}")
    print("   noise sigma (input)     = 0.0080 mGal")
    print(f"   drift over the line     = {drift[-1]:.4f} mGal")
    print(f"   RMS error vs truth      = {rms(observed, truth):.5f} mGal")

    # --- 2. Edit -------------------------------------------------------------
    sig_diff = robust_sigma(observed)
    sig_naive, med = running_median_mad(observed)
    flagged_naive = int(np.sum(np.abs(observed - med) > 4.0 * sig_naive))
    resid = observed - med
    bad = np.abs(resid) > 4.0 * sig_diff
    despiked = observed.copy()
    despiked[bad] = med[bad]
    print("\n2. EDIT (despike with a 5-sample running median)")
    print(f"   difference-based sigma estimate   = {sig_diff:.5f} mGal  (true 0.00800)")
    print(f"   naive running-median MAD sigma    = {sig_naive:.5f} mGal"
          f"  <- {sig_diff/sig_naive:.0f}x too small")
    print(f"   a 4-sigma test on that naive scale would flag {flagged_naive} of "
          f"{x.size} samples")
    print("   because the median residual is EXACTLY zero whenever the sample is")
    print("   the middle value of its own window, i.e. with probability 1/5.")
    print(f"   samples flagged at 4 sigma        = {int(bad.sum())} of {x.size}"
          f"  at indices {np.flatnonzero(bad)}")
    print(f"   RMS error vs truth                = {rms(despiked, truth):.5f} mGal"
          f"  (was {rms(observed, truth):.5f})")
    print("   assumption: spikes are rare, isolated and large compared with the")
    print("   local median. A dense spike train breaks this estimator.")

    # --- 3. Tie / level ------------------------------------------------------
    quiet = (x < 500.0) | (x > 4500.0)
    coeffs = np.polyfit(x[quiet], despiked[quiet], 1)
    line = np.polyval(coeffs, x)
    levelled = despiked - line
    truth_line = np.polyval(np.polyfit(x[quiet], truth[quiet], 1), x)
    print("\n3. TIE / LEVEL (straight line fitted to the two quiet ends)")
    print(f"   fitted slope              = {coeffs[0]:.6e} mGal/m")
    print(f"   range of the removed line = {line.max() - line.min():.4f} mGal")
    print(f"   drift actually in the data= {drift.max() - drift.min():.4f} mGal")
    print(f"   of the removed line, TRUE regional signal = "
          f"{truth_line.max() - truth_line.min():.4f} mGal")
    print(f"   RMS error vs truth        = {rms(levelled, truth):.5f} mGal"
          f"  (was {rms(despiked, truth):.5f})")
    print("   -> levelling removes real long-wavelength signal together with the")
    print("      drift. That is why the choice of datum is a scientific decision.")

    # --- 4. Filter: sweep the cutoff ----------------------------------------
    # The Gaussian transfer function is H(k) = exp(-0.5 (k/kc)^2) with
    # kc = 2 pi / lambda_c, so a LONGER cutoff wavelength is a MORE aggressive
    # filter: it passes only wavelengths longer than lambda_c.
    print("\n4. FILTER: sweep the Gaussian low-pass cutoff wavelength")
    print("   longer cutoff wavelength = more aggressive filter")
    print(f"   {'cutoff (m)':>11}{'noise on quiet ends':>21}{'peak (mGal)':>13}"
          f"{'peak error (%)':>16}{'RMS vs truth':>14}")
    best = (None, np.inf)
    no_filter_err = rms(levelled, truth)
    print(f"   {'none':>11}{levelled[quiet].std(ddof=1):>21.5f}"
          f"{levelled.max():>13.4f}{(levelled.max()/truth.max()-1)*100:>16.2f}"
          f"{no_filter_err:>14.5f}")
    for lam_c in (20.0, 50.0, 100.0, 150.0, 250.0, 400.0, 700.0, 1500.0):
        f = gaussian_lowpass(levelled, dx, lam_c)
        err = rms(f, truth)
        if err < best[1]:
            best = (lam_c, err)
        print(f"   {lam_c:>11.0f}{f[quiet].std(ddof=1):>21.5f}{f.max():>13.4f}"
              f"{(f.max()/truth.max()-1)*100:>16.2f}{err:>14.5f}")
    print(f"   best cutoff of those tried = {best[0]:.0f} m (RMS error "
          f"{best[1]:.5f} mGal, against {no_filter_err:.5f} unfiltered)")
    print("   -> the error has a minimum at a MILD cutoff. Below it the noise")
    print("      survives; above it the anomaly itself is removed. A filter is an")
    print("      improvement only if its pass band contains the signal, and the")
    print("      RMS-versus-cutoff curve is how you find out which you have.")

    # --- 5. Transform --------------------------------------------------------
    print("\n5. TRANSFORM: noise gain of the first derivative vs sample spacing")
    print(f"   {'dx (m)':>8}{'measured gain':>16}{'pi/(dx sqrt 3)':>18}"
          f"{'k_N (rad/m)':>14}")
    for dx_i in (10.0, 25.0, 50.0, 100.0):
        n = 2048
        w = rng.normal(0.0, 1.0, size=(40, n))
        k = 2.0 * np.pi * np.fft.rfftfreq(n, d=dx_i)
        gains = [np.fft.irfft(np.fft.rfft(row) * k, n=n).std() for row in w]
        g = float(np.mean(gains))
        print(f"   {dx_i:>8.0f}{g:>16.5f}{np.pi/(dx_i*np.sqrt(3)):>18.5f}"
              f"{np.pi/dx_i:>14.5f}")
    print("   -> the gain is independent of the record length and scales as 1/dx;")
    print("      the derivation is in the lesson. Finer sampling does not help the")
    print("      derivative: it admits higher wavenumbers, which is exactly where")
    print("      white noise lives.")

    print("\n6. Cumulative RMS error against the truth")
    for name, data in (("observed (raw)", observed), ("after edit", despiked),
                       ("after level", levelled),
                       ("after filter", gaussian_lowpass(levelled, dx, best[0]))):
        print(f"   {name:<18}{rms(data, truth):>10.5f} mGal")


if __name__ == "__main__":
    main()
