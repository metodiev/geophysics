#!/usr/bin/env python3
"""Spectral estimation: the bias and variance of the periodogram, the variance
reduction of Welch averaging, multitaper estimation and leakage suppression, the
exact log-PSD bias of Euler's constant, chi-square confidence intervals, and the
window bias of a red spectrum against its closed-form expectation.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python spectral_estimation_demo.py

All models and data in this module are SYNTHETIC.  The noise is generated here and
the AR(1) spectrum is used in closed form, so every comparison is against algebra
rather than against a recording.

Contents
--------
1.  Periodogram of white noise: level, units, and a coefficient of variation of 1.
2.  The variance does not fall with record length -- measured for three N.
3.  Welch averaging: scatter against the number of segments, without and with
    50 % overlap.
4.  Multitaper (DPSS) estimation and the measured leakage suppression.
5.  The log-PSD bias: E[ln P_hat] = ln P - gamma, gamma = 0.5772156649.
6.  Chi-square confidence intervals, verified by coverage.
7.  The window bias of a red spectrum, against the exact expectation
    E[P_hat(f)] = (2/(fs sum w^2)) sum_tau c_w[tau] R[tau] exp(-i omega tau).
"""

import numpy as np
from scipy import signal as sps
from scipy import stats as sps_stats

RNG = np.random.default_rng(20261014)

FS = 100.0
DT = 1.0 / FS
GAMMA = 0.5772156649015329          # Euler-Mascheroni constant


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def ar1_psd_one_sided(phi, sigma_eps, f):
    """One-sided PSD of x[n] = phi x[n-1] + eps[n] for 0 <= f <= fs/2."""
    z = np.exp(-2j * np.pi * f * DT)
    return 2.0 * sigma_eps ** 2 * DT / np.abs(1.0 - phi * z) ** 2


def ar1_expectation(window, phi, sigma_eps, f):
    """Exact E[Welch PSD] for an AR(1) process, in the scipy 'density' scaling.

    E[P_hat(f)] = (2 / (fs sum w^2)) Re sum_tau c_w[tau] R[tau] e^{-i omega tau},
    with c_w[tau] = sum_n w[n] w[n+tau] and R[tau] = sigma_x^2 phi^|tau|.
    The factor 2 is the one-sided convention and is omitted at f = 0 and at
    f = fs/2, which scipy's one-sided density does not double either.
    """
    w = np.asarray(window, dtype=float)
    length = len(w)
    sigma_x2 = sigma_eps ** 2 / (1.0 - phi ** 2)
    taus = np.arange(-(length - 1), length)
    c_w = np.array([
        np.sum(w[:length - t] * w[t:]) if t >= 0
        else np.sum(w[-t:] * w[:length + t])
        for t in taus])
    r = sigma_x2 * phi ** np.abs(taus)
    f = np.atleast_1d(np.asarray(f, dtype=float))
    omega = 2 * np.pi * f * DT
    spec = np.real(c_w[None, :] * r[None, :]
                   * np.exp(-1j * np.outer(omega, taus))).sum(axis=1)
    factor = np.full(f.shape, 2.0)
    factor[f == 0.0] = 1.0
    factor[f == FS / 2] = 1.0
    return factor * spec / (FS * np.sum(w ** 2))


def main():
    section("1. Periodogram of white noise: level, units, variance")
    sigma = 2.0
    n = 4096
    x = RNG.normal(0.0, sigma, n)
    f, P = sps.periodogram(x, fs=FS, window="boxcar", detrend=False,
                           scaling="density")
    df = f[1] - f[0]
    nbins = len(P)
    print(f"white noise sigma = {sigma}, N = {n}, fs = {FS} Hz, df = {df:.6f} Hz")
    print(f"one-sided PSD: mean over bins = {P.mean():.6f} "
          f"(units: signal^2 / Hz)")
    print(f"exact for white noise: 2 sigma^2 dt = {2 * sigma ** 2 * DT:.6f}")
    print(f"integral sum(P) df = {np.sum(P) * df:.6f}, variance sigma^2 = "
          f"{sigma ** 2:.6f}")
    print(f"   the integral is itself a sum of {nbins} exponential variables, so")
    print(f"   its own relative scatter is 1/sqrt(nbins) = "
          f"{1 / np.sqrt(nbins):.4f} -- the same order as the shortfall seen")
    print(f"coefficient of variation std/mean over bins = "
          f"{P.std(ddof=1) / P.mean():.4f}  (exponential distribution: 1.0000)")
    print("a single periodogram ordinate is uncertain by 100 % of its own value")

    section("2. The variance does not fall with record length")
    print("   N       mean PSD     std/mean")
    for nn in (256, 1024, 8192):
        y = RNG.normal(0.0, sigma, nn)
        _, P = sps.periodogram(y, fs=FS, window="boxcar", detrend=False,
                               scaling="density")
        print(f"  {nn:5d}   {P.mean():9.6f}   {P.std(ddof=1) / P.mean():8.4f}")
    print("the mean is stable and the scatter is not: the periodogram is")
    print("asymptotically unbiased but inconsistent -- more data does not")
    print("reduce the scatter of a single ordinate")

    section("3. Welch averaging: scatter versus segments and overlap")
    n = 8192
    x = RNG.normal(0.0, sigma, n)
    print("   nperseg   overlap   segments   std/mean   1/sqrt(K)")
    for nperseg in (8192, 2048, 512, 128):
        _, P = sps.welch(x, fs=FS, window="hann", nperseg=nperseg,
                         noverlap=0, detrend=False, scaling="density")
        k = 1 + (n - nperseg) // nperseg
        print(f"   {nperseg:7d}        0%   {k:8d}   "
              f"{P.std(ddof=1) / P.mean():8.4f}   {1 / np.sqrt(k):.4f}")
    for nperseg in (4096, 1024, 256):
        _, P = sps.welch(x, fs=FS, window="hann", nperseg=nperseg,
                         noverlap=nperseg // 2, detrend=False,
                         scaling="density")
        k = 1 + (n - nperseg) // (nperseg - nperseg // 2)
        print(f"   {nperseg:7d}       50%   {k:8d}   "
              f"{P.std(ddof=1) / P.mean():8.4f}   {1 / np.sqrt(k):.4f}")
    print("averaging K segments reduces the scatter as 1/sqrt(K); 50 % overlap")
    print("extracts more segments from the same record for a little more")
    print("correlation between them, so the measured scatter tracks the same law")

    section("4. Multitaper (DPSS) estimation and leakage suppression")
    nw = 4.0
    k_tapers = 7
    seg = 1024
    tapers = sps.windows.dpss(seg, nw, Kmax=k_tapers, sym=False)
    n_seg = n // seg
    est = np.zeros((n_seg, k_tapers, seg // 2 + 1))
    for s in range(n_seg):
        chunk = x[s * seg:(s + 1) * seg]
        for j in range(k_tapers):
            _, P_h = sps.periodogram(chunk, fs=FS, window=tapers[j],
                                     detrend=False, scaling="density")
            est[s, j] = P_h
    mt = est.mean(axis=(0, 1))
    wl = np.zeros_like(mt)
    for s in range(n_seg):
        _, P_h = sps.welch(x[s * seg:(s + 1) * seg], fs=FS, window="hann",
                           nperseg=seg, noverlap=0, detrend=False,
                           scaling="density")
        wl += P_h
    wl /= n_seg
    print(f"NW = {nw}, K = {k_tapers} tapers, {n_seg} segments: nominal dof = "
          f"{2 * n_seg * k_tapers}")
    print(f"  multitaper mean = {mt.mean():.6f}, std/mean = "
          f"{mt.std(ddof=1) / mt.mean():.4f}")
    print(f"  Welch      mean = {wl.mean():.6f}, std/mean = "
          f"{wl.std(ddof=1) / wl.mean():.4f}  (1/sqrt({2 * n_seg}) = "
          f"{1 / np.sqrt(2 * n_seg):.4f})")
    print(f"  exact white-noise level 2 sigma^2 dt = {2 * sigma ** 2 * DT:.6f}")
    print("the multitaper scatter is smaller than the Welch scatter but larger")
    print("than 1/sqrt(nominal dof): the higher-order DPSS tapers are less")
    print("concentrated, so the nominal K overstates the independent information")

    tone = 100.0 * np.sin(2 * np.pi * (10.0 + 0.5 * FS / seg)
                          * np.arange(seg) * DT)
    print("\nleakage test: one strong off-bin tone of amplitude 100, no noise")
    print("levels are medians relative to each estimator's own peak")
    estimators = {}
    _, estimators["rectangular"] = sps.periodogram(
        tone, fs=FS, window="boxcar", detrend=False, scaling="density")
    _, estimators["Hann"] = sps.periodogram(
        tone, fs=FS, window="hann", detrend=False, scaling="density")
    for kk in (4, 7, 10):
        tp = sps.windows.dpss(seg, nw, Kmax=kk, sym=False)
        acc = np.zeros(seg // 2 + 1)
        for j in range(kk):
            _, P_h = sps.periodogram(tone, fs=FS, window=tp[j],
                                     detrend=False, scaling="density")
            acc += P_h
        estimators[f"DPSS NW=4, K={kk}"] = acc / kk
    f_grid = np.fft.rfftfreq(seg, d=DT)
    near = (f_grid > 10.5) & (f_grid < 12.0)
    far = (f_grid > 25.0) & (f_grid < 45.0)
    print("   estimator             near sidelobes 11-12 Hz   far field 25-45 Hz")
    for label, P_t in estimators.items():
        peak = P_t.max()
        print(f"   {label:20s}   {10 * np.log10(np.median(P_t[near]) / peak):20.1f} dB   "
              f"{10 * np.log10(np.median(P_t[far]) / peak):16.1f} dB")
    print("the multitaper's own leakage floor rises with K because the",
          "least-concentrated")
    print("taper in the set dominates the average; the Hann window wins in the")
    print("far field but not in the near field, and the DPSS family buys variance")
    print("reduction together with a bounded leakage instead of the best of one")

    section("5. The log-PSD bias: Euler's constant")
    n = 1024
    reps = 1500
    logs = np.empty(reps)
    for r in range(reps):
        y = RNG.normal(0.0, 1.0, n)
        _, P = sps.periodogram(y, fs=FS, window="boxcar", detrend=False,
                               scaling="density")
        logs[r] = np.mean(np.log(P[1:-1] / (2.0 * DT)))
    print(f"{reps} realisations of {n}-sample white noise, {n - 1} interior bins")
    print(f"mean ln(P_hat / P_true) = {logs.mean():+.6f} "
          f"(standard error {logs.std(ddof=1) / np.sqrt(reps):.6f})")
    print(f"-gamma                  = {-GAMMA:+.6f}")
    print(f"in dB: {10 * logs.mean() / np.log(10):+.4f} dB versus "
          f"{-10 * GAMMA / np.log(10):+.4f} dB")
    print("the interior bins of a periodogram of white Gaussian noise are exactly")
    print("chi-square with 2 dof, so E[ln P_hat] = ln P - gamma exactly; DC and")
    print("Nyquist have 1 dof and a different bias, which is why they are excluded")

    section("6. Chi-square confidence intervals, checked by coverage")
    trials = 4000
    true_psd = 2.0 * 1.0 ** 2 * DT
    print("   dof   lower factor   upper factor   95 % coverage measured")
    for dof in (2, 8, 32):
        lo = dof / sps_stats.chi2.ppf(0.975, dof)
        hi = dof / sps_stats.chi2.ppf(0.025, dof)
        inside = 0
        for _ in range(trials):
            y = RNG.normal(0.0, 1.0, 4096)
            _, P = sps.periodogram(y, fs=FS, window="boxcar", detrend=False,
                                   scaling="density")
            # averaging dof/2 adjacent bins of a white spectrum has exactly the
            # chi-square(dof) distribution of averaging dof/2 independent segments
            p_hat = P[1:1 + dof // 2].mean()
            if lo * p_hat <= true_psd <= hi * p_hat:
                inside += 1
        print(f"  {dof:5d}   {lo:12.4f}   {hi:12.4f}   "
              f"{inside / trials:^19.4f}")
    print("the interval [dof P_hat / chi2_0.975, dof P_hat / chi2_0.025] covers")
    print("the true PSD 95 % of the time; with dof = 2 (one periodogram ordinate)")
    print("that interval spans a factor of about 145, which is why a spectral")
    print("level quoted from one ordinate means almost nothing")

    section("7. The window bias of a red spectrum")
    phi = 0.95
    sigma_eps = 1.0
    n = 16384
    reps = 200
    print(f"AR(1) with phi = {phi}, sigma_eps = {sigma_eps}: analytic one-sided")
    print("PSD 2 sigma_eps^2 dt / |1 - phi exp(-i 2 pi f dt)|^2, variance "
          f"{sigma_eps ** 2 / (1 - phi ** 2):.4f}")
    print("   nperseg   ensemble mean vs exact expectation: max|ratio-1|   "
          "peak ratio")
    print("             (the deviation grows with nperseg because fewer segments")
    print("              are averaged, so the ensemble scatter is larger)")
    for nperseg in (128, 1024, 8192):
        win = sps.windows.hann(nperseg, sym=False)
        acc = None
        for _ in range(reps):
            eps = RNG.normal(0.0, sigma_eps, n)
            y = sps.lfilter([1.0], [1.0, -phi], eps)
            f_w, P_w = sps.welch(y, fs=FS, window=win, nperseg=nperseg,
                                 noverlap=nperseg // 2, detrend=False,
                                 scaling="density")
            acc = P_w if acc is None else acc + P_w
        acc /= reps
        exact = ar1_expectation(win, phi, sigma_eps, f_w)
        ratio = acc / exact
        print(f"   {nperseg:7d}   {np.max(np.abs(ratio - 1)):26.4f}   "
              f"{acc.max() / exact.max():.4f}")
    print("the ensemble-averaged Welch estimate matches the exact expectation to")
    print("about a per cent at nperseg = 128, so the smoothing is understood")
    print("rather than mysterious: the expectation is the true PSD convolved with")
    print("the window kernel, not the true PSD itself")
    win = sps.windows.hann(128, sym=False)
    f_fine = np.linspace(0.0, FS / 2, 4097)
    exact_small = ar1_expectation(win, phi, sigma_eps, f_fine)
    true_fine = ar1_psd_one_sided(phi, sigma_eps, f_fine)
    print(f"with nperseg = 128 the peak of the expectation is "
          f"{exact_small.max() / true_fine.max():.4f} of the true peak, and the")
    print("DC bin of a one-sided density carries a further factor 1/2 because")
    print(f"scipy does not double DC: exact ratio at DC = "
          f"{exact_small[0] / true_fine[0]:.4f} = 0.5 x "
          f"{exact_small.max() / true_fine.max():.4f}")
    print("resolving a peak costs variance: nperseg is the exchange rate")


if __name__ == "__main__":
    main()
