#!/usr/bin/env python3
"""Red noise, spectral peaks and modes of variability in SYNTHETIC series.

Run with the project virtual environment:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python climate_timeseries_demo.py

All models and data are SYNTHETIC: seeded AR(1) red noise, a chosen weak
oscillation and a chosen two-mode field.  Nothing here is a measurement of the
climate system.

Contents
--------
1. Red noise and its lag-1 autocorrelation.
2. Periodogram thresholds: white-noise versus red-noise null hypotheses.
3. The multiplicity problem: how often a red-noise series beats the pointwise
   threshold, and how much the corrected threshold moves.
4. Effective sample size under autocorrelation.
5. EOFs of a two-mode synthetic field, and their sampling error.
6. Running-mean smoothing and the autocorrelation it manufactures.
7. Windowing: main-lobe width, sidelobe level, and the variance/bias trade of
   segment averaging, all measured.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

N = 600                 # months = 50 years
RHO = 0.7
SIGMA = 1.0
PERIOD_MONTHS = 44.4    # 3.7 years, a weak ENSO-like oscillation
AMP = 0.35


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def ar1(n, rho, sigma, rng):
    e = rng.standard_normal(n) * sigma * np.sqrt(1.0 - rho ** 2)
    x = np.zeros(n)
    for i in range(1, n):
        x[i] = rho * x[i - 1] + e[i]
    return x


def periodogram(x):
    """One-sided raw periodogram, frequencies in cycles per sample, k = 1..n/2."""
    n = x.size
    X = np.fft.rfft(x - x.mean())
    P = 2.0 * np.abs(X) ** 2 / n
    return P[1:n // 2 + 1], np.arange(1, n // 2 + 1) / n


def ar1_spectrum(f, rho, sigma):
    """One-sided AR(1) power spectral density, variance per cycle/sample."""
    se2 = sigma ** 2 * (1.0 - rho ** 2)
    return 2.0 * se2 / (1.0 - 2.0 * rho * np.cos(2.0 * np.pi * f) + rho ** 2)


def main():
    section("1. Red noise and its lag-1 autocorrelation")
    x = ar1(N, RHO, SIGMA, RNG)
    rho_hat = float(np.corrcoef(x[:-1], x[1:])[0, 1])
    print(f"SYNTHETIC AR(1): n = {N} monthly samples ({N/12:.0f} years), "
          f"rho = {RHO:.2f}, sigma = {SIGMA:.2f}")
    print(f"measured lag-1 autocorrelation = {rho_hat:.3f}")
    print(f"one-sided PSD at f = 0: S(0) = {ar1_spectrum(0.0, RHO, SIGMA):.3f} "
          f"(variance per cycle/sample)")
    print(f"S(1/2) = {ar1_spectrum(0.5, RHO, SIGMA):.3f}; the ratio S(0)/S(1/2) "
          f"= {ar1_spectrum(0.0, RHO, SIGMA)/ar1_spectrum(0.5, RHO, SIGMA):.1f}")
    print("  red noise is not 'noise with a peak': it is a spectrum that falls")
    print("  monotonically with frequency, and any peak must be judged against")
    print("  that slope, not against a flat line.")

    # ------------------------------------------------ null hypotheses -------
    section("2. Periodogram thresholds: white versus red null")
    signal = ar1(N, RHO, SIGMA, RNG)
    t = np.arange(N, dtype=float)
    signal = signal + AMP * np.cos(2.0 * np.pi * t / PERIOD_MONTHS)
    P, f = periodogram(signal)
    white_level = 2.0 * SIGMA ** 2 * (-np.log(0.05))
    red_level = ar1_spectrum(f, RHO, SIGMA) * (-np.log(0.05))
    print(f"  {f.size} frequency bins from 1/{N} to 1/2 cycles/sample")
    print(f"  white-noise 95% pointwise level = 2 sigma^2 * 2.996 = "
          f"{white_level:.3f}")
    print(f"  red-noise 95% pointwise level rises from "
          f"{red_level[0]:.3f} at the lowest frequency")
    print(f"  to {red_level[-1]:.3f} at the highest, a factor of "
          f"{red_level[0]/red_level[-1]:.1f}")
    print(f"  bins above the white level : {int((P > white_level).sum())}")
    print(f"  bins above the red level   : {int((P > red_level).sum())}")
    j = int(np.argmax(P))
    print(f"  largest bin: f = {f[j]:.4f} cycles/sample = "
          f"{1.0/f[j]/12.0:.2f} years, P = {P[j]:.3f}")
    print(f"  the embedded oscillation is at {PERIOD_MONTHS:.1f} months = "
          f"{PERIOD_MONTHS/12.0:.2f} years")
    jb = int(np.argmin(np.abs(f - 1.0 / PERIOD_MONTHS)))
    lo, hi = max(1, jb - 3), min(f.size, jb + 4)
    jm = lo + int(np.argmax(P[lo:hi]))
    print(f"  the embedded oscillation is at f = {1.0/PERIOD_MONTHS:.5f} "
          f"cycles/sample")
    print(f"    nearest bin f = {f[jb]:.5f} ({1.0/f[jb]/12.0:.2f} years): "
          f"P = {P[jb]:.3f}")
    print(f"    largest bin within +/-3 bins: f = {f[jm]:.5f} "
          f"({1.0/f[jm]/12.0:.2f} years), P = {P[jm]:.3f}")
    print(f"    white-noise level {white_level:.3f}, red-noise level there "
          f"{red_level[jm]:.3f}, ratio to red level "
          f"{P[jm]/red_level[jm]:.3f}")
    print("  the oscillation would be declared against the white-noise null and")
    print("  is NOT declared against the red-noise null: this is the central")
    print("  honest difficulty of climate spectral analysis.")
    print(f"  so {int((P > white_level).sum())} bins clear the white-noise level and")
    print(f"  {int((P > red_level).sum())} clear the red-noise level.  The count is")
    print("  the honest one only if the null is the right model for the background.")

    # ---------------------------------------------------- multiplicity -------
    section("3. The multiplicity problem (measured)")
    n_mc = 300
    m = f.size
    exceed_point, exceed_corrected = 0, 0
    alpha_local = 0.05 / m
    corr_level = ar1_spectrum(f, RHO, SIGMA) * (-np.log(alpha_local))
    for _ in range(n_mc):
        xr = ar1(N, RHO, SIGMA, RNG)
        Pr, fr = periodogram(xr)
        lvl = ar1_spectrum(fr, RHO, SIGMA) * (-np.log(0.05))
        if np.any(Pr > lvl):
            exceed_point += 1
        if np.any(Pr > corr_level):
            exceed_corrected += 1
    print(f"  {n_mc} realisations of PURE red noise, {m} frequencies tested")
    print(f"  fraction with any bin above the pointwise 95% red level = "
          f"{exceed_point/n_mc:.3f}")
    print(f"  fraction with any bin above the corrected level           = "
          f"{exceed_corrected/n_mc:.3f}")
    print(f"  pointwise multiplier -ln(0.05)                = {-np.log(0.05):.3f}")
    print(f"  corrected multiplier -ln(0.05/{m})            = "
          f"{-np.log(alpha_local):.3f}")
    print(f"  i.e. the threshold must rise by a factor "
          f"{-np.log(alpha_local)/(-np.log(0.05)):.2f} to hold the family-wise")
    print("  rate near 5%.  A single 'significant peak' from a search over")
    print("  hundreds of frequencies is the expected outcome of red noise.")

    # --------------------------------------------- effective sample size -----
    section("4. Effective sample size under autocorrelation")
    n_eff = N * (1.0 - rho_hat) / (1.0 + rho_hat)
    print(f"  n = {N} samples, measured lag-1 rho = {rho_hat:.3f}")
    print(f"  effective sample size n(1-rho)/(1+rho) = {n_eff:.1f} "
          f"({n_eff/N*100:.1f}% of n)")
    print(f"  inflation of a sample mean's standard error = "
          f"sqrt((1+rho)/(1-rho)) = {np.sqrt((1+rho_hat)/(1-rho_hat)):.3f}")
    print("  any statistic whose standard error assumes independent samples is")
    print(f"  too precise by a factor of about "
          f"{np.sqrt((1+rho_hat)/(1-rho_hat)):.1f} here.  For a flicker-noise")
    print("  series, as in lesson 03, no single factor suffices at all.")

    # ------------------------------------------------------------- EOFs ------
    section("5. EOFs of a two-mode synthetic field")
    n_space = 30
    s = np.arange(n_space, dtype=float)
    p1 = np.cos(np.pi * s / (n_space - 1))                  # north-south dipole
    p2 = np.sin(2.0 * np.pi * s / (n_space - 1))            # three-lobe
    p2 = p2 - (p2 @ p1) / (p1 @ p1) * p1
    p1 /= np.linalg.norm(p1)
    p2 /= np.linalg.norm(p2)
    pc1 = ar1(N, 0.8, 1.0, RNG)
    pc2 = 0.8 * np.cos(2.0 * np.pi * t / 44.4) + 0.3 * ar1(N, 0.5, 1.0, RNG)
    field = (np.outer(pc1, p1) + np.outer(pc2, p2)
             + 0.5 * RNG.standard_normal((N, n_space)))
    X = field - field.mean(axis=0)
    U, sv, Vt = np.linalg.svd(X, full_matrices=False)
    var = sv ** 2 / np.sum(sv ** 2)
    print(f"  field: {N} times x {n_space} sites, two chosen patterns plus "
          f"white noise (sigma = 0.5)")
    print("   EOF   variance explained   |correlation| with nearest true pattern")
    for k in range(4):
        c1 = abs(float(Vt[k] @ p1))
        c2 = abs(float(Vt[k] @ p2))
        print(f"   {k+1:3d}   {var[k]*100:17.2f}%   {max(c1, c2):32.3f}")
    print("  the two modes are recovered in variance order, and the fraction is")
    print("  a statement about THIS sample: the same analysis of another noise")
    print("  realisation gives a different fraction.")

    field2 = (np.outer(ar1(N, 0.8, 1.0, RNG), p1)
              + np.outer(0.8 * np.cos(2.0 * np.pi * t / 44.4)
                         + 0.3 * ar1(N, 0.5, 1.0, RNG), p2)
              + 0.5 * RNG.standard_normal((N, n_space)))
    X2 = field2 - field2.mean(axis=0)
    _, sv2, Vt2 = np.linalg.svd(X2, full_matrices=False)
    var2 = sv2 ** 2 / np.sum(sv2 ** 2)
    print(f"  EOF 1 from an independent realisation: variance "
          f"{var2[0]*100:.2f}%, |correlation| with EOF 1 above = "
          f"{abs(float(Vt[0] @ Vt2[0])):.3f}")
    print("  EOFs are orthogonal by construction (that is a model statement, not")
    print("  a property of the atmosphere) and they have sampling error: two")
    print("  finite realisations of the same generator do not give the same")
    print("  pattern or the same explained variance.")

    # ---------------------------------------------------- running means -----
    section("6. Running-mean smoothing and the autocorrelation it manufactures")
    y = ar1(N, 0.0, 1.0, RNG)          # WHITE noise, to isolate the smoothing
    print(f"  input: white noise, lag-1 autocorrelation = "
          f"{np.corrcoef(y[:-1], y[1:])[0, 1]:+.3f}")
    print("   window   std retained   lag-1 autocorr   lag-W autocorr")
    for w in (3, 7, 13, 25):
        k = np.ones(w) / w
        yy = np.convolve(y, k, mode="valid")
        print(f"  {w:6d}   {yy.std():12.3f}   "
              f"{np.corrcoef(yy[:-1], yy[1:])[0, 1]:14.3f}   "
              f"{np.corrcoef(yy[:-w], yy[w:])[0, 1]:15.3f}")
    print("  smoothing creates autocorrelation that was not in the data: the")
    print("  output of a filter is a filtered model, and any test that assumes")
    print("  independent samples will be wrong when applied to it.")


    # ---------------------------------------------------- windowing ---------
    section("7. Windowing and the bias-variance trade-off, measured")
    nw = 4096
    fine = 16                     # zero-padding factor: interpolates, adds no power
    tww = np.arange(nw, dtype=float)
    tone_only = np.cos(2.0 * np.pi * (64.5 / nw) * tww)   # halfway between bins
    print(f"  (a) one tone halfway between bins (bin 64.5 of {nw}); the transform")
    print(f"      is sampled on a {fine}x zero-padded grid, which interpolates the")
    print("      same transform and adds no power.  Main lobe = between the two")
    print("      first nulls of the transform.")
    print("      window        half-power width (bins)   highest sidelobe (dB)")
    for name, w in (("rectangular", np.ones(nw)), ("Hann", np.hanning(nw)),
                    ("Hamming", np.hamming(nw)), ("Blackman", np.blackman(nw))):
        Pz = np.abs(np.fft.rfft(tone_only * w, n=nw * fine)) ** 2
        pk = Pz.max()
        i0 = int(np.argmax(Pz))
        # walk out to the first local minimum on each side: the main lobe
        il = i0
        while il > 1 and Pz[il - 1] <= Pz[il]:
            il -= 1
        ir = i0
        while ir < Pz.size - 2 and Pz[ir + 1] <= Pz[ir]:
            ir += 1
        above = np.nonzero(Pz > 0.5 * pk)[0]
        width_bins = (above[-1] - above[0] + 1) / fine
        mask = np.ones(Pz.size, dtype=bool)
        mask[il:ir + 1] = False
        db = 10.0 * np.log10(Pz[mask].max() / pk)
        print(f"      {name:12s}  {width_bins:23.2f}   {db:20.1f}")
    print("  (b) white noise, n = 4096, 200 realisations, at f = 0.25")
    print("      cycles/sample (one bin, the same physical frequency for all K);")
    print("      K non-overlapping Hann-windowed segments averaged.")
    print("      truth: one-sided PSD of white noise = 2 sigma^2 = 2.000")
    print("       K   segment length   mean level   relative std   1/sqrt(K)")
    for K in (1, 2, 4, 8, 16, 32):
        L = nw // K
        w = np.hanning(L)
        j = int(round(0.25 * L))
        est = np.empty(200)
        for i in range(200):
            x = RNG.standard_normal(nw)
            segs = x.reshape(K, L) * w
            P = (np.abs(np.fft.rfft(segs, axis=1)) ** 2).mean(axis=0)
            est[i] = 2.0 * P[j] / np.sum(w ** 2)
        print(f"      {K:3d}   {L:15d}   {est.mean():10.4f}   "
              f"{est.std()/est.mean():12.3f}   {1.0/np.sqrt(K):10.3f}")
    print("  (c) a single tone of unit amplitude in white noise: what averaging")
    print("      costs in the height of a line")
    tone_noisy = np.cos(2.0 * np.pi * (64.5 / nw) * tww) + RNG.standard_normal(nw)
    ref = None
    for K in (1, 2, 4, 8, 16, 32):
        L = nw // K
        w = np.hanning(L)
        P = (np.abs(np.fft.rfft(tone_noisy.reshape(K, L) * w, axis=1)) ** 2).mean(axis=0)
        P = 2.0 * P / np.sum(w ** 2)
        if ref is None:
            ref = P.max()
        print(f"      K = {K:2d}: segment length {L:4d}, peak height "
              f"{P.max():8.3f}, ratio to the unaveraged peak {P.max()/ref:6.3f}")
    print("  (a) is the leakage/resolution trade: the rectangular window has the")
    print("  narrowest main lobe and the worst sidelobes; Hann, Hamming and")
    print("  Blackman buy sidelobe suppression with a wider main lobe, and the")
    print("  measured widths and sidelobe levels are the numbers to quote when a")
    print("  weak signal sits next to a strong one.")
    print("  (b) is the variance side: the estimator stays centred on the true")
    print("  level 2.000 (the bias for a flat spectrum is essentially zero) while")
    print("  its relative standard deviation falls as 1/sqrt(K), as the last")
    print("  column predicts.  (c) is what it costs: the height of a narrow line")
    print("  falls roughly as 1/K, so averaging reduces variance by flattening")
    print("  peaks.  The estimator is unbiased for a flat spectrum and biased for")
    print("  a peak, and both statements are measurable on the same run.")


if __name__ == "__main__":
    main()
