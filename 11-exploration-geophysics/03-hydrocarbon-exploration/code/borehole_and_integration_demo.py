#!/usr/bin/env python3
"""Integrating borehole data with seismic: the well tie, time-depth conversion,
layer-induced anisotropy, and how much calibration is enough.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python borehole_and_integration_demo.py

Contents
--------
1. A synthetic sonic and density log, its reflectivity, and a synthetic
   seismogram.
2. The well tie: what a single bulk shift recovers and what only a stretch can.
3. Time-depth conversion: the two-way time of v(z) = v0 + k z, and the depth
   error produced by velocity errors.
4. How many calibration points are enough, with noisy picks, and what model
   mismatch costs.
5. Layer-induced (Backus) anisotropy from a two-component layered medium.
6. Wavelet phase: what a phase error does to a tie.

All models and numbers are SYNTHETIC teaching values: a chosen log model, a
chosen wavelet and chosen calibration geometries.
"""

import numpy as np
from scipy.optimize import least_squares
from scipy.signal import hilbert

RNG = np.random.default_rng(20261014)

DZ = 0.5                # m, log sample interval
Z_MAX = 3000.0          # m, logged interval
DT = 0.001              # s, seismic sample interval
F0 = 30.0               # Hz, wavelet dominant frequency
V0_TRUE = 1800.0        # m/s, velocity at the datum
K_TRUE = 0.45           # 1/s, velocity gradient of the model
RHO0, RHO_GRAD = 2100.0, 0.30   # kg/m^3, chosen linear density model


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def ricker(f0, dt, length=0.081):
    n = int(round(length / dt)) | 1
    t = (np.arange(n) - n // 2) * dt
    a = (np.pi * f0) ** 2
    return (1.0 - 2.0 * a * t ** 2) * np.exp(-a * t ** 2)


def t_of_z(zarr, v0, k):
    """Two-way time for v(z) = v0 + k z."""
    return 2.0 / k * np.log(1.0 + k * np.asarray(zarr) / v0)


def z_of_t(tarr, v0, k):
    """Depth for a two-way time, inverting v(z) = v0 + k z."""
    return v0 / k * (np.exp(k * np.asarray(tarr) / 2.0) - 1.0)


def log_model():
    """Synthetic vp(z) and rho(z): compaction trend plus layering."""
    z = np.arange(0.0, Z_MAX + DZ, DZ)
    trend = V0_TRUE + K_TRUE * z
    raw = RNG.normal(0.0, 1.0, z.size)
    kernel = np.exp(-0.5 * (np.arange(-40, 41) * DZ / 20.0) ** 2)
    kernel /= kernel.sum()
    lay = np.convolve(raw, kernel, mode="same") * 220.0
    vp = trend + lay
    rho = RHO0 + RHO_GRAD * (vp - V0_TRUE) + 0.02 * RNG.normal(0.0, 10.0, z.size)
    return z, vp, rho


def two_way_time(vp, dz):
    t = 2.0 * np.cumsum(dz / vp)
    return t - t[0]


def reflectivity(vp, rho):
    imp = rho * vp
    return (imp[1:] - imp[:-1]) / (imp[1:] + imp[:-1])


def to_time_grid(t_log, r, dt, n):
    out = np.zeros(n)
    idx = np.round(t_log[1:] / dt).astype(int)
    keep = (idx >= 0) & (idx < n)
    np.add.at(out, idx[keep], r[keep])
    return out


def main():
    section("1. Log model, reflectivity and synthetic seismogram")
    z, vp, rho = log_model()
    t_log = two_way_time(vp, DZ)
    r = reflectivity(vp, rho)
    n_time = int(np.ceil(t_log[-1] / DT)) + 1
    r_time = to_time_grid(t_log, r, DT, n_time)
    wavelet = ricker(F0, DT)
    synthetic = np.convolve(r_time, wavelet)[:n_time]
    print(f"log: {z.size} samples at {DZ:.1f} m, 0 to {Z_MAX:.0f} m")
    print(f"vp {vp.min():.0f} to {vp.max():.0f} m/s; rho {rho.min():.0f} to "
          f"{rho.max():.0f} kg/m^3")
    print(f"two-way time to {Z_MAX:.0f} m on the well velocity = "
          f"{t_log[-1]:.4f} s")
    print(f"reflectivity: rms {np.sqrt(np.mean(r ** 2)):.4f}, max "
          f"{np.abs(r).max():.4f}")
    print(f"time grid {n_time} samples at {DT * 1000:.0f} ms "
          f"({n_time * DT:.3f} s)")
    print(f"synthetic seismogram rms = {np.sqrt(np.mean(synthetic ** 2)):.4f}")

    section("2. The well tie: a shift, and what only a stretch recovers")
    v_err = 0.05
    t_seis = t_log / (1.0 + v_err)
    r_seis = to_time_grid(t_seis, r, DT, n_time)
    seismic_clean = np.convolve(r_seis, wavelet)[:n_time]
    seismic = seismic_clean + 0.05 * np.std(seismic_clean) \
        * RNG.standard_normal(n_time)
    lags = np.arange(-80, 81)
    cors = [np.dot(synthetic, np.roll(seismic, int(lag))) for lag in lags]
    best_lag = int(lags[int(np.argmax(cors))])
    print(f"the seismic volume was migrated with a velocity "
          f"{v_err * 100:.0f}% too high,")
    print(f"so every event sits at t_well/{1 + v_err:.2f}")
    print(f"\n   tie applied                          correlation with the log "
          f"synthetic")
    print(f"   none (raw seismic)                   "
          f"{np.corrcoef(synthetic, seismic)[0, 1]:.3f}")
    print(f"   best single bulk shift ({best_lag * DT * 1000:+.0f} ms)   "
          f"{np.corrcoef(synthetic, np.roll(seismic, best_lag))[0, 1]:.3f}")
    t_s_grid = np.arange(n_time) * DT
    stretched = np.interp(t_s_grid / (1.0 + v_err), t_s_grid, seismic)
    print(f"   shift + correct stretch              "
          f"{np.corrcoef(synthetic, stretched)[0, 1]:.3f}")
    print("   (the correlation stops at 0.93: the 5% noise on the seismic trace")
    print("    and the interpolation of a stretched trace are the limits)")
    print("\nthe shift each part of the log would need:")
    for t_target in (0.5, 1.0, 1.5, 2.0):
        i = int(np.argmin(np.abs(t_log - t_target)))
        print(f"  at {t_target:.1f} s: {(t_log[i] - t_seis[i]) * 1000:6.1f} ms")
    print("The required shift grows with time, so one constant shift cannot tie")
    print("the log: the tie needs a velocity function or a stretch.  A tie that")
    print("is good at the top and poor at the bottom is telling you about")
    print("velocity, not about the wavelet.")

    section("3. Time-depth conversion and the depth error from velocity error")
    print("model v(z) = v0 + k z  ->  t(z) = (2/k) ln(1 + k z/v0)")
    print(f"chosen v0 = {V0_TRUE:.0f} m/s, k = {K_TRUE:.3f} 1/s")
    print("\n   depth (m)   log time (s)   analytic time (s)   difference (ms)")
    for z_target in (500.0, 1000.0, 2000.0, 3000.0):
        i = int(np.argmin(np.abs(z - z_target)))
        t_an = t_of_z(z_target, V0_TRUE, K_TRUE)
        print(f"  {z_target:9.0f}   {t_log[i]:13.4f}   {t_an:17.4f}   "
              f"{(t_log[i] - t_an) * 1000:14.2f}")
    t_ref = t_of_z(np.array([1000.0, 2000.0, 3000.0]), V0_TRUE, K_TRUE)
    print("\ndepth error produced by a 5% error in each parameter:")
    print("\n   depth (m)   v0 +5%   v0 -5%   k +5%   k -5%   (metres)")
    for z_target, t_z in zip((1000.0, 2000.0, 3000.0), t_ref):
        row = [z_of_t(t_z, v0, k) - z_target
               for v0, k in ((V0_TRUE * 1.05, K_TRUE), (V0_TRUE * 0.95, K_TRUE),
                             (V0_TRUE, K_TRUE * 1.05), (V0_TRUE, K_TRUE * 0.95))]
        print(f"  {z_target:9.0f}   {row[0]:+7.1f}   {row[1]:+7.1f}   "
              f"{row[2]:+6.1f}   {row[3]:+6.1f}")
    print("A 5% error in the velocity at the datum moves the target by about 5%")
    print("of its depth: 150 m at 3 km, two orders of magnitude larger than the")
    print("seismic vertical resolution.  Depth conversion is a velocity problem,")
    print("and the gradient term matters about three times less than v0 here.")

    section("4. How many calibration points are enough?")
    print("fit v(z) = v0 + k z to n check-shot picks with a 2 ms time error,")
    print("then convert the true two-way time at 3 km.  200 realisations each.")
    print("\n   n levels   mean depth error (m)   90th percentile (m)")
    for n_lev in (2, 3, 5, 10, 20):
        z_lev = np.linspace(0.0, Z_MAX, n_lev)
        t_lev_true = t_of_z(z_lev, V0_TRUE, K_TRUE)
        errs = []
        for _ in range(200):
            picks = t_lev_true + 0.002 * RNG.standard_normal(n_lev)

            def res(p):
                return t_of_z(z_lev, p[0], p[1]) - picks
            fit = least_squares(res, np.array([1500.0, 0.6]), method="lm").x
            errs.append(z_of_t(t_of_z(Z_MAX, V0_TRUE, K_TRUE), fit[0], fit[1])
                        - Z_MAX)
        errs = np.array(errs)
        print(f"  {n_lev:8d}   {np.abs(errs).mean():19.1f}   "
              f"{np.percentile(np.abs(errs), 90):17.1f}")
    print("\nmodel mismatch: fitting a straight time-depth line t = a + b z to")
    print("20 noise-free picks of the same log (the true t(z) is logarithmic):")
    z_lev = np.linspace(0.0, Z_MAX, 20)
    t_lev = t_of_z(z_lev, V0_TRUE, K_TRUE)
    b, a = np.polyfit(z_lev, t_lev, 1)
    t_wrong = a + b * Z_MAX
    z_wrong = z_of_t(t_wrong, V0_TRUE, K_TRUE)
    print(f"  straight-line fit: t(3 km) = {t_wrong:.4f} s against the true "
          f"{t_lev[-1]:.4f} s")
    print(f"  depth error from that mismatch = {z_wrong - Z_MAX:+.1f} m at 3 km")
    print("Noise is not the limiting factor here: with the right model form a")
    print("handful of levels suffices, and with the wrong form any number of")
    print("levels gives the wrong depth.  VSP levels through the interval of")
    print("interest, and a stated velocity form, are what remove the error.")

    section("5. Layer-induced (Backus) anisotropy")
    sand = (3600.0, 2100.0, 2200.0)     # vp, vs, rho
    shale = (2900.0, 1550.0, 2400.0)
    frac_sand = 0.40

    def lam_mu(vp_i, vs_i, rho_i):
        mu = rho_i * vs_i ** 2
        lam = rho_i * (vp_i ** 2 - 2.0 * vs_i ** 2)
        return lam, mu

    comps = [(frac_sand, sand), (1.0 - frac_sand, shale)]
    lam = np.array([lam_mu(v, s, r)[0] for _, (v, s, r) in comps])
    mu = np.array([lam_mu(v, s, r)[1] for _, (v, s, r) in comps])
    f = np.array([c[0] for c in comps])
    vp_i = np.array([sand[0], shale[0]])
    rho_i = np.array([sand[2], shale[2]])
    rho_bar = float(np.sum(f * rho_i))
    m_p = lam + 2.0 * mu
    inv_m = 1.0 / np.sum(f / m_p)                      # harmonic mean of M
    c33 = inv_m
    c11 = float(np.sum(f * 4.0 * mu * (lam + mu) / m_p)
                + inv_m * np.sum(f * lam / m_p) ** 2)
    c13 = inv_m * float(np.sum(f * lam / m_p))
    c44 = 1.0 / np.sum(f / mu)
    c66 = float(np.sum(f * mu))
    print(f"sand  fraction {frac_sand:.2f}: vp = {sand[0]:.0f} m/s, "
          f"vs = {sand[1]:.0f} m/s, rho = {sand[2]:.0f} kg/m^3")
    print(f"shale fraction {1 - frac_sand:.2f}: vp = {shale[0]:.0f} m/s, "
          f"vs = {shale[1]:.0f} m/s, rho = {shale[2]:.0f} kg/m^3")
    print(f"\nBackus equivalent medium, rho = {rho_bar:.0f} kg/m^3:")
    print(f"  C11 = {c11 / 1e9:6.2f} GPa   C33 = {c33 / 1e9:6.2f} GPa   "
          f"C13 = {c13 / 1e9:6.2f} GPa")
    print(f"  C44 = {c44 / 1e9:6.2f} GPa   C66 = {c66 / 1e9:6.2f} GPa")
    v_pv, v_ph = np.sqrt(c33 / rho_bar), np.sqrt(c11 / rho_bar)
    v_sv, v_sh = np.sqrt(c44 / rho_bar), np.sqrt(c66 / rho_bar)
    eps_b = (c11 - c33) / (2.0 * c33)
    delta_b = ((c13 + c44) ** 2 - (c33 - c44) ** 2) / (2.0 * c33 * (c33 - c44))
    gamma_b = (c66 - c44) / (2.0 * c44)
    print(f"  vp vertical   = {v_pv:7.1f} m/s     vp horizontal = {v_ph:7.1f} m/s")
    print(f"  vs vertical   = {v_sv:7.1f} m/s     vs horizontal = {v_sh:7.1f} m/s")
    print(f"  Thomsen: eps = {eps_b:+.4f}, delta = {delta_b:+.4f}, "
          f"gamma = {gamma_b:+.4f}")
    v_time_avg = 1.0 / np.sum(f / vp_i)
    print(f"\nexact kinematic check: the vertical travel time through the stack")
    print(f"is the sum of the layer times, giving v = {v_time_avg:.1f} m/s")
    print(f"Backus vertical P velocity = {v_pv:.1f} m/s, "
          f"{abs(v_pv - v_time_avg) / v_time_avg * 100:.2f}% different")
    print("Fine layering of isotropic layers produces POSITIVE eps (horizontal")
    print("faster) because horizontal averaging is closer to a parallel")
    print("combination: the horizontal stiffness is the arithmetic-like term and")
    print("the vertical one the harmonic term.  In real shale, intrinsic clay")
    print("anisotropy adds to this, which is why measured eps in shale usually")
    print("exceeds what layering alone would give.")

    section("6. Wavelet phase: what a phase error does to a tie")
    w_0 = ricker(F0, DT)
    freqs = np.fft.fftfreq(w_0.size, DT)
    print("\n   phase rotation   correlation with the trace   wavelet peak (ms)"
          "   wavelet trough (ms)")
    trough = {}
    for deg in (0.0, 15.0, 30.0, 45.0, 60.0, 90.0):
        phase = np.exp(1j * np.radians(deg) * np.sign(freqs))
        w_rot = np.real(np.fft.ifft(np.fft.fft(w_0) * phase))
        syn = np.convolve(r_time, w_rot)[:n_time]
        corr = np.corrcoef(synthetic, syn)[0, 1]
        c = w_rot.size // 2
        t_pk = (int(np.argmax(w_rot)) - c) * DT * 1000.0
        t_tr = (int(np.argmin(w_rot)) - c) * DT * 1000.0
        trough[deg] = t_tr
        print(f"  {deg:12.0f}   {corr:25.3f}   {t_pk:18.1f}   {t_tr:20.1f}")
    v_deep = V0_TRUE + K_TRUE * Z_MAX
    d_shift = trough[90.0] - trough[0.0]
    print(f"\nthe picked trough moves {abs(d_shift):.1f} ms between the zero-phase")
    print(f"and 90 degree wavelets, which is {abs(d_shift) / 1000.0 * v_deep / 2:.0f}"
          f" m of depth at 3 km.")
    print("A 90 degree rotation is the Hilbert transform: it is orthogonal to")
    print("the zero-phase wavelet, so the tie correlation collapses to nothing")
    print("even though the events are in the right place.  A phase error also")
    print("destroys amplitude-versus-offset gradients and biases inversion.")
    print("Wavelet phase must be estimated (statistically, or from a VSP) and")
    print("stated, not assumed.")


if __name__ == "__main__":
    main()
