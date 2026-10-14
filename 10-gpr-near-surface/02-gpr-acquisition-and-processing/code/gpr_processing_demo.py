#!/usr/bin/env python3
"""GPR processing: dewow, gain, band-pass filtering, Kirchhoff migration of a
dipping reflector, and spatial (background) removal -- each step measured by
what it does to a synthetic trace or section.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gpr_processing_demo.py

Everything here is SYNTHETIC.  The attenuation, the drift, the noise level and
the AGC window are CHOSEN MODEL PARAMETERS, labelled where used.  No field data
and no instrument is involved.

Contents
--------
1. Dewow: a synthetic low-frequency drift and the pick bias it causes, before
   and after a running-mean removal.
2. Gain: constant gain and AGC measured against the true amplitude ratio of two
   reflections, and the noise they amplify.
3. Band-pass filtering: signal-to-noise gain and the pulse broadening it costs.
4. Kirchhoff migration of a dipping reflector: apparent dip before, true dip
   after, and the dip produced by a wrong migration velocity.
5. Background removal: a coherent horizontal ringing train and the
   target-to-clutter ratio before and after median subtraction.
6. Verification: migrated reflector position and focus.
"""

import numpy as np
from scipy.signal import butter, filtfilt, hilbert

RNG = np.random.default_rng(20261014)

V = 0.09993           # m/ns, eps_r = 9 (chosen)
F0 = 0.2              # GHz = 200 MHz
DT = 0.025            # ns
NT = 4000             # 100 ns window
DX = 0.05             # m trace spacing
ALPHA = 0.25          # 1/m, chosen attenuation for the synthetic gather
NOISE_RMS = 0.02      # chosen, relative to the first reflection amplitude


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def ricker(t, f0):
    a = (np.pi * f0) ** 2
    return (1.0 - 2.0 * a * t ** 2) * np.exp(-a * t ** 2)


def wiggle(t, tw, ww, t0):
    return np.interp(t - t0, tw, ww, left=0.0, right=0.0)


def envelope_fwhm(profile, d):
    env = np.abs(hilbert(profile))
    return float(np.sum(env > 0.5 * env.max()) * d)


def kirchhoff_migrate(d, x, t, xg, zg, v, aperture):
    m = np.zeros((zg.size, xg.size))
    ix = np.arange(x.size)[:, None]
    for iz, z in enumerate(zg):
        tt = 2.0 * np.sqrt(z ** 2 + (xg[None, :] - x[:, None]) ** 2) / v
        idx = np.clip(tt / DT, 0.0, t.size - 1.001)
        i0 = idx.astype(int)
        fr = idx - i0
        w = (np.abs(xg[None, :] - x[:, None]) <= aperture).astype(float)
        m[iz] = ((d[ix, i0] * (1.0 - fr) + d[ix, i0 + 1] * fr) * w).sum(axis=0)
    return m


def main():
    t = np.arange(NT) * DT
    tw = np.arange(-25.0, 25.0, DT)
    ww = ricker(tw, F0)
    print(f"SYNTHETIC parameters: v = {V:.5f} m/ns, f0 = {F0*1000:.0f} MHz, "
          f"dt = {DT:.3f} ns, {NT} samples = {NT*DT:.0f} ns")

    section("1. Dewow: the low-frequency drift and the bias it causes")
    t1, t2 = 16.0, 40.0
    a1 = 1.0
    a2 = float(np.exp(-2.0 * ALPHA * 1.2))       # two-way path difference 2.4 m
    clean = a1 * wiggle(t, tw, ww, t1) + a2 * wiggle(t, tw, ww, t2)
    drift = 0.18 * np.sin(2.0 * np.pi * t / 220.0) + 0.12 * (t / (NT * DT))
    trace = clean + drift + NOISE_RMS * RNG.standard_normal(t.size)
    n = int(round(20.0 / DT))
    running = np.convolve(trace, np.ones(n) / n, mode="same")
    trace_dw = trace - running

    def first_zero_after(tr, t_start):
        i0 = int(np.argmin(np.abs(t - t_start)))
        for i in range(i0, t.size - 1):
            if tr[i] > 0.0 >= tr[i + 1]:
                return t[i] + DT * tr[i] / (tr[i] - tr[i + 1])
        return np.nan

    zc_ref = first_zero_after(clean, t2)
    win = (t > t1 - 5.0) & (t < t1 + 5.0)
    win_d = (t > t2 - 6.0) & (t < t2 + 6.0)
    print(f"   two reflections at {t1:.1f} ns and {t2:.1f} ns; SYNTHETIC drift of")
    print(f"   amplitude about {np.ptp(drift):.2f} (chosen) against a first "
          f"reflection of {a1:.2f}")
    print(f"   additive noise rms {NOISE_RMS:.3f}; true amplitude ratio "
          f"a2/a1 = {a2:.4f}")
    print("   trace            first zero crossing after t2 (ns)   amplitude ratio")
    for label, tr in (("clean (reference)", clean), ("with drift", trace),
                      ("after dewow", trace_dw)):
        print(f"   {label:16s} {first_zero_after(tr, t2):24.4f}   "
              f"{np.abs(tr[win_d]).max()/np.abs(tr[win]).max():16.4f}")
    print(f"   the drift delays the zero crossing by "
          f"{(first_zero_after(trace, t2)-zc_ref)*1000:.0f} ps and biases the")
    print(f"   amplitude ratio from {a2:.4f} to "
          f"{np.abs(trace[win_d]).max()/np.abs(trace[win]).max():.4f} "
          f"({(np.abs(trace[win_d]).max()/np.abs(trace[win]).max()/a2-1)*100:+.1f}%)")
    print(f"   after a {20.0:.0f} ns running-mean removal (chosen window) the bias")
    print(f"   is {(first_zero_after(trace_dw, t2)-zc_ref)*1000:+.0f} ps and the ratio")
    print(f"   is {np.abs(trace_dw[win_d]).max()/np.abs(trace_dw[win]).max():.4f} "
          f"({(np.abs(trace_dw[win_d]).max()/np.abs(trace_dw[win]).max()/a2-1)*100:+.1f}%)")
    print("   Dewow is a high-pass filter applied before anything is measured: the")
    print("   drift is not signal, and every pick and amplitude downstream inherits")
    print("   its bias until it is removed.")

    section("2. Gain: constant gain versus AGC")
    t_agc = 20.0
    n_agc = int(round(t_agc / DT))
    kern_agc = np.ones(n_agc) / n_agc
    rms = np.sqrt(np.convolve(trace_dw ** 2, kern_agc, mode="same"))
    target = np.median(rms[rms > 0]) if np.any(rms > 0) else 1.0
    agc = trace_dw * (target / np.maximum(rms, 1e-12))
    print("   The SYNTHETIC attenuation is alpha = "
          f"{ALPHA:.2f} 1/m, so the second")
    print(f"   reflection is smaller than the first by exp(-2 alpha dz) = {a2:.4f}")
    print("   AGC here uses a running-rms window of "
          f"{t_agc:.0f} ns (chosen).")
    for label, tr in (("raw (dewowed)", trace_dw), ("constant gain x2", 2.0 * trace_dw),
                      ("AGC", agc)):
        r = np.abs(tr[win_d]).max() / np.abs(tr[win]).max()
        noise_win = (t > 70.0)
        print(f"   {label:16s}: measured a2/a1 = {r:.4f}, noise rms in the deep "
              f"window = {np.std(tr[noise_win]):.5f}")
    print("   A constant gain scales signal and noise together and preserves")
    print("   amplitudes; AGC makes every window look equally strong, which")
    print("   destroys the very ratio used to estimate attenuation and reflection")
    print("   coefficient.  AGC and dewow belong before display; amplitude work")
    print("   needs a gain that is known in closed form.")

    section("3. Band-pass filtering: signal-to-noise gain versus pulse width")
    b, a = butter(4, [2.0 * 0.4 * F0 / (1.0 / DT / 2.0),
                      2.0 * 2.5 * F0 / (1.0 / DT / 2.0)], btype="band")
    filt = filtfilt(b, a, trace)
    sig_win = (t > 38.0) & (t < 46.0)
    noise_win = (t > 70.0)
    for label, tr in (("raw", trace), ("band-passed", filt)):
        snr = 20.0 * np.log10(np.std(tr[sig_win]) / np.std(tr[noise_win]))
        fw = envelope_fwhm(tr[sig_win], DT)
        print(f"   {label:12s}: signal/noise in the target window = {snr:6.2f} dB, "
              f"envelope FWHM = {fw:.3f} ns = {fw*V/2*100:.2f} cm")
    print("   cut-offs: 0.4 f0 and 2.5 f0, i.e. "
          f"{0.4*F0*1000:.0f} MHz to {2.5*F0*1000:.0f} MHz (chosen, fourth-order")
    print("   Butterworth, zero-phase filtfilt).  The filter buys signal-to-noise")
    print("   and pays in pulse width: whatever is gained in detectability is spent")
    print("   in resolution, and both numbers must be reported.")

    section("4. Migration of a dipping reflector: apparent versus true dip")
    theta_true = np.radians(20.0)
    d0 = 2.00
    x = np.arange(-3.0, 3.0 + 1e-9, DX)
    sec = np.zeros((x.size, t.size))
    for i, xx in enumerate(x):
        d_x = d0 + xx * np.sin(theta_true)      # depth of the interface at xx
        sec[i] = wiggle(t, tw, ww, 2.0 * d_x / V)
    # depth-converted, unmigrated apparent dip
    iz_peak = np.argmax(np.abs(sec), axis=1)
    t_ev = t[iz_peak]
    d_app = V * t_ev / 2.0
    slope_un = np.polyfit(x, d_app, 1)[0]
    print(f"   SYNTHETIC interface dipping {np.degrees(theta_true):.1f} deg, "
          f"depth {d0:.2f} m at x = 0")
    print(f"   zero-offset time dip dt/dx = 2 sin(theta)/v = "
          f"{2*np.sin(theta_true)/V:.3f} ns/m")
    print(f"   depth-converted apparent dip: tan(theta_app) = "
          f"{slope_un:.4f} -> {np.degrees(np.arctan(slope_un)):.2f} deg "
          f"(predicted {np.degrees(np.arctan(np.sin(theta_true))):.2f} deg from "
          f"tan(theta_app) = sin(theta))")
    zg = np.arange(1.00, 4.001, 0.02)
    xg = x.copy()
    for v_mig, label in ((V, "correct velocity"), (0.9 * V, "velocity 10% low"),
                         (1.1 * V, "velocity 10% high")):
        m = kirchhoff_migrate(sec, x, t, xg, zg, v_mig, 3.0)
        z_img = zg[np.argmax(np.abs(m), axis=0)]
        th_mig = np.degrees(np.arctan(np.polyfit(xg, z_img, 1)[0]))
        pred = np.degrees(np.arcsin(np.clip((v_mig / V) * np.sin(theta_true),
                                            -1, 1)))
        print(f"   {label:18s}: imaged dip {th_mig:6.2f} deg (prediction "
              f"sin(theta_mig) = (v_mig/v) sin(theta) -> {pred:6.2f} deg); "
              f"depth at x = 0: {z_img[xg.size//2]:.3f} m")
    m = kirchhoff_migrate(sec, x, t, xg, zg, V, 3.0)
    z_img = zg[np.argmax(np.abs(m), axis=0)]
    print("   Migration moves the event from the apparent dip to the true dip and")
    print("   from the apparent position to the true position.  A velocity error")
    print("   tilts the image without collapsing it, which is why an unmigrated")
    print("   or badly migrated section can look perfectly plausible.")

    section("5. Background removal: coherent ringing versus a point target")
    ntr = 161
    x2 = np.arange(ntr) * DX - 4.0
    ring = np.zeros(t.size)
    for k in range(1, 6):
        ring += (0.35 / k) * wiggle(t, tw, ww, 6.0 * k)
    sec2 = np.tile(ring, (ntr, 1))
    t_pt = 2.0 * 1.20 / V
    for i, xx in enumerate(x2):
        sec2[i] += np.interp(t - 2.0 * np.sqrt(1.2 ** 2 + xx ** 2) / V,
                             tw, ww, left=0.0, right=0.0)
    sec2 += NOISE_RMS * RNG.standard_normal(sec2.shape)
    med = np.zeros_like(sec2)
    half = 2
    for i in range(ntr):
        lo, hi = max(0, i - half), min(ntr, i + half + 1)
        med[i] = np.median(sec2[lo:hi], axis=0)
    sec2b = sec2 - med
    tg = (t > t_pt - 4.0) & (t < t_pt + 4.0)
    cl = (t > 12.0) & (t < 24.0)
    for label, s in (("raw", sec2), ("background removed", sec2b)):
        peak = np.abs(s[:, tg]).max()
        clutter = np.std(s[:, cl])
        print(f"   {label:18s}: target peak {peak:.4f}, clutter rms "
              f"{clutter:.4f}, target/clutter {20*np.log10(peak/clutter):6.2f} dB")
    print("   The ringing train is horizontal and coherent across traces; a")
    print("   median over a short spatial window removes it and leaves the")
    print("   hyperbolic target, at the cost of smearing anything that is itself")
    print("   laterally coherent -- including a flat-lying real reflector.")

    section("6. Verification: focus of the migrated target and the dip recovered")
    d = np.zeros((ntr, t.size))
    for i, xx in enumerate(x2):
        d[i] = np.interp(t - 2.0 * np.sqrt(1.2 ** 2 + xx ** 2) / V,
                         tw, ww, left=0.0, right=0.0) + ring
    mg = kirchhoff_migrate(d, x2, t, x2, np.arange(0.2, 3.001, 0.02), V, 4.0)
    i_ap = np.unravel_index(np.argmax(mg), mg.shape)
    z_gn = np.arange(0.2, 3.001, 0.02)
    print(f"   point target built at x = 0.000 m, z = 1.200 m")
    print(f"   migrated apex at x = {x2[i_ap[1]]:.3f} m, "
          f"z = {z_gn[i_ap[0]]:.3f} m")
    print(f"   error: {abs(x2[i_ap[1]])*100:.2f} cm laterally, "
          f"{abs(z_gn[i_ap[0]]-1.2)*100:.2f} cm in depth")
    print(f"   recovered dip in Section 4 (correct velocity): "
          f"{np.degrees(np.arctan(np.polyfit(xg, z_img, 1)[0])):.2f} deg "
          f"against {np.degrees(theta_true):.1f} deg true")
    print("\n   Every number above comes from the SYNTHETIC models of this script;")
    print("   no measured processing gain or field dataset is quoted.")


if __name__ == "__main__":
    main()
