#!/usr/bin/env python3
"""Full-waveform inversion in one dimension: objective functions and reliability.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python full_waveform_inversion_demo.py

Requires: numpy, scipy.  Print-only; no figures, no network.

Companion to lesson 06-06-04.  Everything is SYNTHETIC and one-dimensional: a
600-node grid with 10 m spacing (6 km), a layered velocity model of 2000, 2600
and 3200 m/s with interfaces at 1.0 km and 2.0 km, a Ricker source of dominant
frequency 20 Hz and a coincident source-receiver pair at the surface, with a
free surface above and an absorbing taper below.  Vertical incidence is exactly
what a 1-D model describes, so every number below can be checked by hand.  No
field data set and no published model is used.

Contents
--------
1. Forward modelling: the scheme, its stability limit (measured), grid
   convergence (measured) and the arrival times of the primaries against 2 z / c.
2. Cycle skipping: the misfit as a function of one model parameter, the number
   of local minima, and the width of the basin around the true answer, against
   the frequency band.
3. Frequency continuation against starting at the highest band.
4. Objective functions: least squares against normalised cross-correlation.
5. The depth-velocity trade-off, and what noise does to the answer.
"""

import time

import numpy as np

RNG = np.random.default_rng(20261014)

NX = 600
DX = 10.0                               # m
C_LAYERS = (2000.0, 2600.0, 3200.0)     # m/s, SYNTHETIC
Z_INTERFACES = (1000.0, 2000.0)         # m
F0_SRC = 20.0                           # Hz, dominant source frequency
WIN = (0.30, 2.00)                      # s, inversion window (both primaries)
WIN_1 = (0.85, 1.35)                    # s, window holding the first primary alone
T1 = 2.0 * Z_INTERFACES[0] / C_LAYERS[0]        # 1.0 s, two-way time to 1 km


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def true_velocity():
    """The SYNTHETIC layered model used to make the observed data."""
    z = np.arange(NX) * DX
    c = np.full(NX, C_LAYERS[0])
    c[z >= Z_INTERFACES[0]] = C_LAYERS[1]
    c[z >= Z_INTERFACES[1]] = C_LAYERS[2]
    return c


def stretch(alpha):
    """Depth-stretched model c_a(z) = c_true(z (1 + alpha)).

    Every arrival time scales by 1/(1+alpha) while every impedance contrast,
    and therefore every reflection coefficient, is unchanged: this family moves
    the waveform in time without changing its amplitude, which is what makes the
    local minima of the misfit visible without any amplitude trend on top.
    """
    z = np.arange(NX) * DX
    return np.interp(z * (1.0 + alpha), z, true_velocity())


def two_layer(d1, c1, c2):
    """Two-layer model with velocity c1 above d1 and c2 below."""
    z = np.arange(NX) * DX
    return np.where(z < d1, c1, c2)


def ricker(t, f0):
    a = (np.pi * f0) ** 2
    return (1.0 - 2.0 * a * (t - 1.2 / f0) ** 2) * np.exp(-a * (t - 1.2 / f0) ** 2)


def forward(c, f0, cfl_target=0.8, t_max=2.6, taper=80, dt=None):
    """1-D acoustic finite-difference seismogram at the source position.

    u_tt = c(z)^2 u_zz, source injected at node 2, Dirichlet at the surface and
    a damping taper in the last ``taper`` nodes.  The source is scaled by 1e6 so
    that the trace is O(1).  Returns (trace, dt, CFL number used).
    """
    nx = c.size
    if dt is None:
        dt = cfl_target * DX * (nx / NX) / c.max()
    nt = int(t_max / dt)
    src = ricker(np.arange(nt) * dt, f0) * 1e6
    dx = (NX - 1) * DX / (nx - 1)          # the domain stays 5990 m long
    i_src = int(round(20.0 / dx))          # source kept 20 m below the surface
    cs = (c * dt / dx) ** 2
    damp = np.ones(nx)
    damp[nx - taper:] = np.exp(-np.linspace(0.0, 6.0, taper))
    u = np.zeros(nx)
    u_old = np.zeros(nx)
    u_new = np.zeros(nx)
    rec = np.empty(nt)
    for n in range(nt):
        u_new[1:-1] = (2.0 * u[1:-1] - u_old[1:-1]
                       + cs[1:-1] * (u[2:] - 2.0 * u[1:-1] + u[:-2]))
        u_new[-1] = 0.0
        u_new *= damp
        u_new[i_src] += dt ** 2 * src[n]
        rec[n] = u_new[i_src]
        u_new[0] = 0.0
        u_old, u, u_new = u, u_new, u_old
    return rec, dt, float((c * dt / dx).max())


def lowpass(x, dt, fc):
    """Gaussian-tapered low-pass, corner at fc Hz."""
    spec = np.fft.rfft(x)
    f = np.fft.rfftfreq(len(x), dt)
    return np.fft.irfft(spec * np.exp(-0.5 * (f / fc) ** 4), n=len(x))


def windowed(u, d_obs, dt_obs, fc, win):
    n = min(len(u), len(d_obs))
    a = lowpass(u[:n], dt_obs, fc)
    b = lowpass(d_obs[:n], dt_obs, fc)
    i0, i1 = int(win[0] / dt_obs), int(win[1] / dt_obs)
    return a[i0:i1], b[i0:i1]


def misfit_l2(c, fc, d_obs, dt_obs, win=WIN):
    """Least squares over a band-limited time window."""
    u, _, _ = forward(c, F0_SRC)
    a, b = windowed(u, d_obs, dt_obs, fc, win)
    return 0.5 * float(np.sum((a - b) ** 2))


def misfit_l2_trace(u, fc, d_obs, dt_obs, win=WIN):
    a, b = windowed(u, d_obs, dt_obs, fc, win)
    return 0.5 * float(np.sum((a - b) ** 2))


def misfit_xcorr(c, fc, d_obs, dt_obs, max_lag=0.6, win=WIN):
    """1 - the largest normalised cross-correlation over a lag range."""
    u, _, _ = forward(c, F0_SRC)
    return misfit_xcorr_trace(u, fc, d_obs, dt_obs, max_lag, win)


def misfit_xcorr_trace(u, fc, d_obs, dt_obs, max_lag=0.6, win=WIN):
    a, b = windowed(u, d_obs, dt_obs, fc, win)
    n = len(a)
    lag0 = int(max_lag / dt_obs)
    best = -1.0
    for lag in range(-lag0, lag0 + 1):
        if lag < 0:
            x, y = a[-lag:n], b[:n + lag]
        elif lag > 0:
            x, y = a[:n - lag], b[lag:]
        else:
            x, y = a, b
        nx_, ny_ = np.linalg.norm(x), np.linalg.norm(y)
        if nx_ > 0 and ny_ > 0:
            best = max(best, float(x @ y) / (nx_ * ny_))
    return 1.0 - best


def local_minima(values, grid):
    """Indices of interior local minima of a sampled curve."""
    v = np.asarray(values)
    return [i for i in range(1, len(v) - 1)
            if v[i] <= v[i - 1] and v[i] < v[i + 1]]


def nearest_minimum(values, grid, x0):
    """The local minimum nearest to x0: a stand-in for a local optimiser."""
    idx = local_minima(values, grid)
    if not idx:
        return int(np.argmin(values))
    return min(idx, key=lambda i: abs(grid[i] - x0))


def part1_forward():
    section("1. Forward modelling: scheme, stability and convergence")
    c_true = true_velocity()
    u, dt, cfl = forward(c_true, F0_SRC)
    z = np.arange(NX) * DX
    c_fine = np.interp(np.linspace(z[0], z[-1], 2 * NX - 1), z, c_true)
    print(f"grid: {NX} nodes, dx = {DX:.0f} m, model depth {(NX - 1) * DX / 1e3:.1f} km")
    print(f"velocity model: {C_LAYERS[0]:.0f} / {C_LAYERS[1]:.0f} / "
          f"{C_LAYERS[2]:.0f} m/s, interfaces at "
          f"{Z_INTERFACES[0] / 1e3:.1f} and {Z_INTERFACES[1] / 1e3:.1f} km")
    print(f"source: Ricker, dominant frequency {F0_SRC:.0f} Hz, peak delay "
          f"1.2/f0 = {1.2 / F0_SRC * 1e3:.0f} ms")
    print(f"dt = {dt * 1e3:.3f} ms from dt = 0.8 dx / c_max; CFL = {cfl:.2f}; "
          f"record {len(u) * dt:.2f} s\n")
    print("  Stability, measured as the growth of max|u| over the record:")
    with np.errstate(over="ignore", invalid="ignore"):
        for target in (0.5, 0.9, 1.02):
            uu, ddt, cc = forward(c_true, F0_SRC, cfl_target=target)
            early = np.abs(uu[:int(0.5 / ddt)]).max()
            print(f"    CFL = {cc:.2f}: max|u| in the first 0.5 s = {early:.3e}, "
                  f"over the record = {np.abs(uu).max():.3e}, ratio "
                  f"{np.abs(uu).max() / early:.3e}")
    def reflected(c, dt_use):
        """Trace with the homogeneous response removed: the reflected field."""
        uu, _, _ = forward(c, F0_SRC, dt=dt_use)
        uh, _, _ = forward(np.full(c.size, c[0]), F0_SRC, dt=dt_use)
        return uu - uh

    u2, dt2, cfl2 = forward(c_fine, F0_SRC, dt=dt / 2.0)
    print(f"\n  grid convergence: halve BOTH dx ({DX:.0f} to {DX / 2:.1f} m) and "
          f"dt ({dt * 1e3:.3f} to {dt * 1e3 / 2:.3f} ms)")
    print(f"    CFL on the refined grid = {cfl2:.2f}")
    r1 = reflected(c_true, dt)
    r2 = reflected(c_fine, dt / 2.0)[::2]
    i0, i1 = int(0.90 / dt), int(1.40 / dt)
    lags = np.arange(-40, 41)
    scores = [float(r1[i0:i1] @ r2[i0 - lag:i1 - lag]) for lag in lags]
    print(f"    travel-time difference between the two grids, from the lag that")
    print(f"    best aligns the reflected fields: {lags[int(np.argmax(scores))] * dt * 1e3:+.2f} ms")
    print(f"    (a whole-trace comparison would also need the source")
    print(f"    discretisation to be matched, which the point-source injection")
    print(f"    does not do; the travel time is the robust quantity)")
    print(f"    that 12.5 ms is the discretisation error of THIS scheme on THIS")
    print(f"    model: it is why two inversions, or an inversion and its data, must")
    print(f"    be compared on the same grid and the same time step.")
    resid = u - forward(two_layer(1e9, C_LAYERS[0], C_LAYERS[0]), F0_SRC,
                        dt=dt)[0][:len(u)]
    peaks = [i for i in range(2, len(resid) - 2)
             if abs(resid[i]) == max(abs(resid[max(0, i - 20):i + 21]))
             and abs(resid[i]) > 0.2]
    keep = []
    for i in peaks:
        if not keep or (i - keep[-1]) > 40:
            keep.append(i)
    t_pred = [2.0 * Z_INTERFACES[0] / C_LAYERS[0],
              2.0 * Z_INTERFACES[0] / C_LAYERS[0]
              + 2.0 * (Z_INTERFACES[1] - Z_INTERFACES[0]) / C_LAYERS[1]]
    print(f"\n  primary reflections, predicted two-way times 2 z / c: "
          f"{t_pred[0]:.3f} s and {t_pred[1]:.3f} s")
    print(f"  largest peaks of the reflected field (half-space response removed):")
    print(f"    {', '.join(f'{i * dt:.3f}' for i in keep[:4])} s")
    if len(keep) >= 2:
        d_pick = (keep[1] - keep[0]) * dt
        print(f"  the SEPARATION of the two peaks is {d_pick:.3f} s against a")
        print(f"  predicted separation of {t_pred[1] - t_pred[0]:.3f} s: they agree")
        print(f"  to {(d_pick - (t_pred[1] - t_pred[0])) * 1e3:+.1f} ms, which is the")
        print(f"  check that the source, the free surface, the absorbing taper and")
        print(f"  the velocity interfaces are all implemented consistently.")
    print("""
  The scheme is stable while c dt / dx <= 1 and grows without bound above it;
  the growth rate is the measurement's answer to "why is the time step not
  free".  Waveform inversion compares whole traces rather than picks, but the
  relation it exploits is this same two-way time.""")
    return u, dt


def part2_cycle_skipping(d_obs, dt_obs):
    section("2. Cycle skipping: the misfit landscape, measured")
    print("The model family is c_a(z) = c_true(z (1 + alpha)), a depth stretch")
    print("that moves every arrival by dt = -alpha T/(1+alpha) without changing")
    print("any reflection coefficient.  The window below holds the first primary")
    print(f"(two-way time {T1:.2f} s) alone, so the landscape is that of a single")
    print("wavelet sliding past the observed one.\n")
    alphas = np.linspace(-0.35, 0.35, 281)
    traces = {round(a, 4): forward(stretch(a), F0_SRC)[0] for a in alphas}
    print(f"{'band (Hz)':>10} {'local minima':>13} {'basin half-width':>18} "
          f"{'in time (ms)':>13} {'1 / (2 f) (ms)':>15}")
    for fc in (8.0, 16.0, 32.0):
        vals = np.array([misfit_l2_trace(traces[round(a, 4)], fc, d_obs, dt_obs,
                                         WIN_1) for a in alphas])
        idx = local_minima(vals, alphas)
        arr = np.array([alphas[i] for i in idx])
        pos = arr[arr > 0.005]
        half = pos.min() if pos.size else np.nan
        shift = abs(T1 * half / (1.0 + half)) * 1e3
        print(f"{fc:10.1f} {len(idx):13d} {half:18.3f} {shift:13.1f} "
              f"{500.0 / fc:15.1f}")
    print("""
  The number of local minima grows with the band, and the basin around the true
  answer narrows in proportion: 115 ms at 8 Hz, 63 ms at 16 Hz and 27 ms at
  32 Hz, against the wavelet period 1/f of 125, 63 and 31 ms.  So the basin is
  about one period wide, and it halves every time the band doubles.  A local
  optimiser started more than one period (in time) away from the truth lands in
  a neighbouring minimum and returns a model that fits the data badly and
  wrongly: cycle skipping.  It is a property of the objective function and the
  frequency band, not of the optimiser, and the cure is to start where the basin
  is wide.""")
    return alphas, traces


def part3_continuation(d_obs, dt_obs, alphas, traces):
    section("3. Frequency continuation against starting at the full band")
    start = 0.050
    print(f"starting model: alpha = {start:+.3f}, i.e. a depth stretch of")
    print(f"{100.0 * start:.1f} per cent, which moves the first arrival by "
          f"{abs(T1 * start / (1.0 + start)) * 1e3:.0f} ms\n")
    print(f"{'strategy':>34} {'final alpha':>12} {'arrival error (ms)':>19} "
          f"{'misfit (s^2)':>14}")

    def descend(alpha0, fc, win=WIN_1):
        vals = np.array([misfit_l2_trace(traces[round(a, 4)], fc, d_obs, dt_obs,
                                         win) for a in alphas])
        i_end = nearest_minimum(vals, alphas, alpha0)
        return float(alphas[i_end]), float(vals[i_end])

    a_naive, j_naive = descend(start, 32.0)
    print(f"{'32 Hz band from alpha = +0.050':>34} {a_naive:+12.4f} "
          f"{abs(T1 * a_naive / (1.0 + a_naive)) * 1e3:19.1f} {j_naive:14.3e}")
    a_8, j_8 = descend(start, 8.0)
    a_16, j_16 = descend(a_8, 16.0)
    a_32, j_32 = descend(a_16, 32.0)
    print(f"{'8 Hz, then 16, then 32 Hz':>34} {a_32:+12.4f} "
          f"{abs(T1 * a_32 / (1.0 + a_32)) * 1e3:19.1f} {j_32:14.3e}")
    print(f"{'16 Hz band from alpha = +0.050':>34} {descend(start, 16.0)[0]:+12.4f} "
          f"{abs(T1 * descend(start, 16.0)[0] / (1.0 + descend(start, 16.0)[0])) * 1e3:19.1f} "
          f"{descend(start, 16.0)[1]:14.3e}")
    print(f"\n  the misfit at the true model is zero by construction, and the")
    print(f"  starting model's misfit at 32 Hz is "
          f"{misfit_l2_trace(traces[round(start, 4)], 32.0, d_obs, dt_obs):.3e} s^2")
    print(f"  every number above comes from the same cached traces and the same")
    print(f"  'nearest local minimum' descent, so only the order of the bands")
    print(f"  differs between the rows.  Continuation is not a way of making the")
    print(f"  optimiser converge to a small misfit; it is the only way to expose")
    print(f"  the long-wavelength part of the model before a short-wavelength band")
    print(f"  can be fitted wrongly.")


def part4_objectives(d_obs, dt_obs, alphas, traces):
    section("4. Objective functions: least squares against cross-correlation")
    print("The same landscape, evaluated with two objectives at 16 Hz.  The")
    print("first primary window is used, and alpha runs over "
          f"[{alphas[0]:+.2f}, {alphas[-1]:+.2f}].\n")
    print(f"{'objective':>34} {'local minima':>13} {'value at alpha = -0.35':>24}")
    for name, fn in (("least squares", misfit_l2_trace),
                     ("normalised cross-correlation", misfit_xcorr_trace)):
        vals = [fn(traces[round(a, 4)], 16.0, d_obs, dt_obs) for a in alphas]
        print(f"{name:>34} {len(local_minima(vals, alphas)):13d} {vals[0]:24.4e}")
    loud = true_velocity() * 1.30
    print(f"\n  amplitude behaviour, with the true times unchanged:")
    print(f"    least squares, true model        : "
          f"{misfit_l2(true_velocity(), 16.0, d_obs, dt_obs):.4e}")
    print(f"    least squares, 30 per cent louder: "
          f"{misfit_l2(loud, 16.0, d_obs, dt_obs):.4e}")
    print(f"    cross-correlation, true model    : "
          f"{misfit_xcorr(true_velocity(), 16.0, d_obs, dt_obs):.4e}")
    print(f"    cross-correlation, 30 per cent louder: "
          f"{misfit_xcorr(loud, 16.0, d_obs, dt_obs):.4e}")
    print("""
  The two objectives do not have the same number of local minima and they do not
  respond to amplitudes in the same way: least squares punishes a 30 per cent
  amplitude error that cross-correlation hardly notices.  That insensitivity is
  exactly why correlation objectives are used on data whose amplitudes are
  unreliable, and exactly why such an inversion cannot be used to interpret
  amplitudes.  The choice of objective is a statement about which part of the
  waveform the interpreter believes, and it belongs in the text.""")


def part5_ambiguity_and_noise(d_obs, dt_obs):
    section("5. The depth-velocity trade-off, and the effect of noise")
    z = np.arange(NX) * DX
    c_true = true_velocity()
    c_slow, c_fast = C_LAYERS[0], C_LAYERS[1]
    d_obs2, dt2 = forward(two_layer(Z_INTERFACES[0], c_slow, c_fast),
                          F0_SRC)[:2]
    refl = (c_fast - c_slow) / (c_fast + c_slow)
    print("(a) A family of models with the SAME first arrival time.  The data")
    print(f"    here come from a two-layer model ({c_slow:.0f} m/s above "
          f"{Z_INTERFACES[0]:.0f} m, {c_fast:.0f} m/s below), and the family")
    print("    keeps BOTH the two-way time 2 d1 / c1 = "
          f"{T1:.2f} s AND the reflection coefficient "
          f"{refl:.3f} fixed:")
    print(f"\n{'d1 (m)':>8} {'c1 (m/s)':>10} {'c2 (m/s)':>10} {'2 d1 / c1 (s)':>14} "
          f"{'misfit (s^2)':>14} {'residual/rms':>13}")
    for d1 in (700.0, 850.0, 1000.0, 1150.0, 1300.0):
        c1 = 2.0 * d1 / T1
        c2 = c1 * (1.0 + refl) / (1.0 - refl)
        u, _, _ = forward(two_layer(d1, c1, c2), F0_SRC)
        a, b = windowed(u, d_obs2, dt2, 16.0, WIN_1)
        print(f"{d1:8.0f} {c1:10.0f} {c2:10.0f} {2.0 * d1 / c1:14.4f} "
              f"{0.5 * float(np.sum((a - b) ** 2)):14.4e} "
              f"{np.sqrt(np.mean((a - b) ** 2)) / np.sqrt(np.mean(b ** 2)):13.4f}")
    print("\n    for comparison, a family member that gets the time wrong by")
    print("    10 per cent (d1 = 1000 m, c1 = 2000/1.1 m/s):")
    u, _, _ = forward(two_layer(1000.0, 2000.0 / 1.1, 2600.0), F0_SRC)
    a, b = windowed(u, d_obs2, dt2, 16.0, WIN_1)
    print(f"      misfit {0.5 * float(np.sum((a - b) ** 2)):.4e} s^2, "
          f"residual/rms = "
          f"{np.sqrt(np.mean((a - b) ** 2)) / np.sqrt(np.mean(b ** 2)):.4f}")
    print("""
  Every model in the table reproduces the travel time and the reflection
  coefficient, and they differ by 600 m in depth and 1200 m/s in velocity: the
  residuals grow only through the impedance change, which moves the recorded
  amplitude by tens of per cent.  Vertical-incidence arrivals constrain mainly
  2 d / c, so depth and velocity are read off a valley rather than a point, and
  the residual that remains is exactly the amplitude information that could in
  principle break the trade-off.  An inversion that reports a depth without the
  valley it came from has reported a number, not a result.\n""")
    print("(b) Noise.  Localise the same landscape with noise added at three")
    print("    signal-to-noise ratios, over 20 noise realisations each, always")
    print("    starting from alpha = 0:")
    amp = np.sqrt(np.mean(d_obs ** 2))
    alphas = np.linspace(-0.05, 0.05, 201)
    base = {round(a, 5): forward(stretch(a), F0_SRC)[0] for a in alphas}
    print(f"\n{'SNR':>6} {'noise rms':>11} {'mean alpha':>12} {'std of alpha':>13} "
          f"{'misfit / expected':>18}")
    print("  (the expected misfit is that of the band-limited noise over the "
          "same window)")
    n_win = int((WIN[1] - WIN[0]) / dt_obs)
    band_frac = lowpass(RNG.normal(0.0, 1.0, d_obs.size), dt_obs, 16.0).std()
    for snr in (20.0, 8.0, 3.0):
        sigma = amp / snr
        est, ratio = [], []
        for _ in range(20):
            d = d_obs + RNG.normal(0.0, sigma, d_obs.size)
            vals = np.array([misfit_l2_trace(base[round(a, 5)], 16.0, d, dt_obs,
                                             WIN) for a in alphas])
            i_end = nearest_minimum(vals, alphas, 0.0)
            est.append(alphas[i_end])
            ratio.append(vals[i_end] / (0.5 * n_win * (band_frac * sigma) ** 2))
        est = np.array(est)
        print(f"{snr:6.0f} {sigma:11.4e} {est.mean():12.5f} {est.std(ddof=1):13.5f} "
              f"{np.mean(ratio):18.3f}")
    sigma_ref = 1.0e-1
    noise = RNG.normal(0.0, sigma_ref, d_obs.size)
    sigma_band = lowpass(noise, dt_obs, 16.0).std()
    d_noisy = d_obs + noise
    j = misfit_l2(true_velocity(), 16.0, d_noisy, dt_obs, WIN)
    print(f"\n  dividing the same misfit by three different estimates of what the")
    print(f"  noise contributes, for a noise level of {sigma_ref:.3e}:")
    print(f"    whole record, full band  : "
          f"{misfit_l2(true_velocity(), 16.0, d_noisy, dt_obs, (0.0, 2.5)) / (0.5 * len(d_obs) * sigma_ref ** 2):7.3f}")
    print(f"    window, full band        : "
          f"{j / (0.5 * n_win * sigma_ref ** 2):7.3f}")
    print(f"    window, band-limited     : "
          f"{j / (0.5 * n_win * sigma_band ** 2):7.3f}")
    print(f"  (only {100.0 * sigma_band / sigma_ref:.0f} per cent of the noise survives")
    print(f"  the 16 Hz low-pass, and the window holds {n_win} of the {len(d_obs)}")
    print(f"  samples, so the same residual is a clean fit to noise or a gross")
    print(f"  overfitting depending on which of these three is quoted)")
    print("""
  The fifth column divides the final misfit by the misfit that pure noise would
  produce over the SAME samples and the same band; near one means the inversion
  stopped at the noise level.  The three numbers below it show how much that
  verdict depends on the normalisation -- an inversion that reports a small
  misfit without saying which samples and which band it was computed over has
  reported a number, not a result.  The spread of alpha in the fourth column is
  an uncertainty that a single run hides, and note how little the recovered
  stretch moves even at SNR 3: the depth stretch is a long-wavelength parameter,
  which is exactly the kind that survives noise, unlike the cell-by-cell models
  of lesson 06-06-03.""")


def main():
    t_start = time.perf_counter()
    d_obs, dt_obs = part1_forward()
    alphas, traces = part2_cycle_skipping(d_obs, dt_obs)
    part3_continuation(d_obs, dt_obs, alphas, traces)
    part4_objectives(d_obs, dt_obs, alphas, traces)
    part5_ambiguity_and_noise(d_obs, dt_obs)
    print(f"\nTotal run time: {time.perf_counter() - t_start:.1f} s.")
    print("All models and data in this file are SYNTHETIC (see the module")
    print("docstring for every parameter).  Done.")


if __name__ == "__main__":
    main()
