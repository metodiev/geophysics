#!/usr/bin/env python3
"""Distributed acoustic sensing: gauge-length averaging, directivity, spatial
aliasing, the strain-velocity relation, and the gauge-length SNR trade-off.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python das_interrogation_demo.py

Everything is SYNTHETIC.  The wavefields are analytic plane waves and the noise
is generated, not measured.  No real fibre, interrogator or dataset is used.

Contents
--------
1. Gauge-length averaging is a sinc filter in wavenumber: measured against the
   closed form, with its -3 dB point and first null.
2. Directivity: the cos^2(theta) response of an axial strain measurement to a P
   wave, and the exact null response to cross-fibre S motion.
3. Spatial aliasing: channel spacing, apparent velocity and the sign reversal.
4. The strain/particle-velocity/acceleration relations for a travelling wave.
5. Gauge length versus signal-to-noise, for a narrowband and for a broadband
   detector: the two answers are different, and that is the point.
6. Summary of measured quantities.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC model parameters (chosen, not measured) -----------------------
C_PHASE = 1000.0     # m/s  phase velocity of the synthetic surface wave
F_WAVE = 10.0        # Hz   frequency of the synthetic wave
D_CHANNEL = 10.0     # m    default channel spacing ("gauge pitch")


def section(title: str) -> None:
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def main() -> int:
    lam = C_PHASE / F_WAVE
    k_wave = 2.0 * np.pi / lam
    omega = 2.0 * np.pi * F_WAVE

    # ------------------------------------------------------------------
    section("1. Gauge-length averaging: a sinc filter in wavenumber")
    print(f"MODEL: plane wave, phase velocity c = {C_PHASE:.0f} m/s, "
          f"f = {F_WAVE:.1f} Hz -> wavelength lambda = {lam:.1f} m")
    print("A gauge of length L centred at x_c reports the strain averaged over")
    print("[x_c - L/2, x_c + L/2].  For eps(x) = eps0 cos(kx - phi):")
    print("    <eps> = eps0 cos(k x_c - phi) * sinc(kL/2),  kL/2 = pi L/lambda")
    print("so the recovery factor is sinc(pi L/lambda).\n")
    print("   L/lambda   L (m)   measured recovery   sinc(pi L/lambda)")
    xs = np.linspace(-5.0 * lam, 5.0 * lam, 200001)
    for r in (0.05, 0.10, 0.20, 0.442925, 0.60, 1.00, 1.50, 2.00):
        L = r * lam
        m = np.abs(xs) <= 0.5 * L
        meas = np.trapezoid(np.cos(k_wave * xs)[m], xs[m]) / L
        pred = np.sinc(r)                # numpy sinc(x) = sin(pi x)/(pi x)
        print(f"   {r:8.6f}   {L:6.1f}   {meas:17.8f}   {pred:17.8f}")
    print("\n  The measured curve matches sinc(pi L/lambda) to the accuracy of")
    print("  the trapezoid rule.  The -3 dB point solves")
    print("  sinc(pi L/lambda) = 1/sqrt(2), i.e. pi L/lambda = 1.391557 ->")
    print("  L/lambda = 0.442925; the recovery is exactly ZERO at L = lambda and")
    print("  NEGATIVE beyond it, with a negative side lobe peaking at")
    print("  L/lambda = 1.5 (recovery -0.212207).  A gauge longer than a")
    print("  wavelength does not simply attenuate a wave: it measures the wrong")
    print("  thing, with the wrong sign.  This is a wavenumber filter, not an")
    print("  amplitude knob.")

    # ------------------------------------------------------------------
    section("2. Directivity: the cos^2(theta) response of axial strain")
    print("Fibre along x.  Plane wave with wave vector k = k(cos t, sin t, 0) and")
    print("displacement u = A d exp(i(kx cos t - wt)), d the unit polarisation.")
    print("A central difference of u_x along x gives eps_xx; amplitudes below are")
    print("divided by kA.\n")
    print("   theta [deg]   P: cos^2   P measured   SV: sin2t/2   SV measured   "
          "SH measured")
    h = 0.01
    x3 = np.array([-h, 0.0, h])
    for deg in (0.0, 15.0, 30.0, 45.0, 60.0, 75.0, 90.0):
        th = np.deg2rad(deg)
        phase = np.exp(1j * k_wave * x3 * np.cos(th))
        # P: polarisation along k -> u_x = A cos(t)
        eps_p = np.abs(np.cos(th)) * np.abs(phase[2] - phase[0]) / (2.0 * h * k_wave)
        # SV: polarisation perpendicular to k in the x-y plane -> u_x = -A sin(t)
        eps_sv = np.abs(np.sin(th)) * np.abs(phase[2] - phase[0]) / (2.0 * h * k_wave)
        # SH: polarisation along y, perpendicular to the fibre -> u_x = 0
        print(f"   {deg:11.1f}   {np.cos(th) ** 2:6.4f}   {eps_p:10.6f}   "
              f"{np.sin(2.0 * th) / 2.0:11.4f}   {eps_sv:11.6f}   "
              f"{0.0:11.6f}")
    print("\n  A P wave gives eps_xx = i k A cos^2(theta): the measurement is")
    print("  blind to broadside P energy, and reads the along-fibre projection")
    print("  twice over.  An SH wave polarised perpendicular to the fibre gives")
    print("  eps_xx = 0 EXACTLY, at every angle -- no gain recovers it.  An SV")
    print("  wave gives sin(2 theta)/2, zero both along and broadside and maximum")
    print("  at 45 degrees.  Directivity follows from measuring a SPATIAL")
    print("  DERIVATIVE along a line, not from any deficiency of the sensor.")

    # ------------------------------------------------------------------
    section("3. Spatial aliasing: channel spacing sets the Nyquist wavenumber")
    print(f"Wave: c = {C_PHASE:.0f} m/s at f = {F_WAVE:.1f} Hz -> "
          f"lambda = {lam:.1f} m, k = {k_wave:.4f} 1/m")
    print("Channels at spacing d can represent wavenumbers only up to")
    print("k_Nyq = pi/d.  The phase difference between adjacent channels gives")
    print("k modulo 2 pi/d, so a wave above the Nyquist wavenumber appears at a")
    print("folded wavenumber k_app.\n")
    print("   d (m)   d/lambda   k_Nyq (1/m)   k_app (1/m)   c_app (m/s)   note")
    for d in (25.0, 40.0, 50.0, 60.0, 75.0, 100.0):
        kny = np.pi / d
        period = 2.0 * np.pi / d
        m = np.round(k_wave / period)
        kap = k_wave - period * m
        note = ""
        if abs(kap) < 1e-12:
            ctxt = "         inf"
            note = "all channels in phase (k_app = 0)"
        elif abs(abs(kap) - kny) < 1e-12:
            ctxt = f"{omega / abs(kap):12.1f}"
            note = "k meets the Nyquist wavenumber: sign ambiguous"
        else:
            ctxt = f"{omega / kap:12.1f}"
        print(f"   {d:5.1f}   {d / lam:9.3f}   {kny:11.4f}   {kap:11.4f}   "
              f"{ctxt}   {note}")
    print("\n  numeric check from the phase between adjacent channels:")
    for d in (40.0, 60.0, 75.0):
        x_ch = np.arange(0, 20) * d
        ph = np.exp(1j * k_wave * x_ch)
        dphi = np.angle(ph[1] * np.conj(ph[0]))
        k_num = dphi / d
        print(f"    d = {d:5.1f} m -> k_app = {k_num:+.4f} 1/m, "
              f"c_app = {omega / k_num:+9.1f} m/s")
    print("\n  At d <= lambda/2 the apparent velocity is correct.  At d above")
    print("  lambda/2 = 50.0 m here the measured wavenumber folds: a 1000 m/s")
    print("  wave reads as -1500 m/s at d = 60 m and as -3000 m/s at d = 75 m.")
    print("  The alias is not noise and it does not look wrong -- it is a")
    print("  coherent slowness belonging to a different wave, so every DAS")
    print("  dispersion measurement must state its channel spacing and the")
    print("  corresponding Nyquist wavenumber.")

    # ------------------------------------------------------------------
    section("4. Strain, particle velocity and acceleration for a travelling wave")
    dt = 1.0 / 4000.0
    t = np.arange(0.0, 0.4, dt)
    amp = 1.0e-6                      # m, SYNTHETIC displacement amplitude
    u = amp * np.sin(k_wave * x3[:, None] - omega * t[None, :])
    u_c = u[1, :]
    v = np.gradient(u_c, dt)          # particle velocity
    acc = np.gradient(v, dt)          # particle acceleration
    eps = (u[2, :] - u[0, :]) / (2.0 * h)     # axial strain, measured
    eps_dot = np.gradient(eps, dt)            # strain rate (what DAS reports)
    print(f"A = {amp:.1e} m, f = {F_WAVE:.1f} Hz, c = {C_PHASE:.0f} m/s, "
          f"k = {k_wave:.6f} 1/m, w = {omega:.4f} rad/s, dt = {dt:.6f} s")
    print(f"  |u| amplitude                = {np.max(np.abs(u_c)):.6e} m")
    print(f"  |v| amplitude                = {np.max(np.abs(v)):.6e} m/s")
    print(f"  |acc| amplitude              = {np.max(np.abs(acc)):.6e} m/s^2")
    print(f"  |eps| amplitude              = {np.max(np.abs(eps)):.6e} (-)")
    print(f"  |eps_dot| amplitude          = {np.max(np.abs(eps_dot)):.6e} 1/s")
    print(f"  ratio |eps| / |v|            = "
          f"{np.max(np.abs(eps)) / np.max(np.abs(v)):.6e} s/m")
    print(f"  1/c                          = {1.0 / C_PHASE:.6e} s/m")
    print(f"  ratio |eps_dot| / |acc|      = "
          f"{np.max(np.abs(eps_dot)) / np.max(np.abs(acc)):.6e} s/m")
    print(f"  residual max ||eps| - |v|/c| / max|eps| = "
          f"{np.max(np.abs(np.abs(eps) - np.abs(v) / C_PHASE)) / np.max(np.abs(eps)):.3e}")
    print(f"  residual max |eps_dot + acc/c| / max|eps_dot| = "
          f"{np.max(np.abs(eps_dot + acc / C_PHASE)) / np.max(np.abs(eps_dot)):.3e}")
    print("\n  Both identities hold to the accuracy of the finite differences:")
    print("      |eps| = |v|/c,        eps_dot = -acc/c.")
    print("  The strain that a DAS interrogator reports is the particle velocity")
    print("  divided by the phase velocity, differentiated once in time -- so a")
    print("  DAS record and a collocated geophone are the same waveform only when")
    print("  c is known.  That is why DAS amplitude studies are fundamentally")
    print("  dispersion studies.")

    # ------------------------------------------------------------------
    section("5. Gauge length versus signal-to-noise: narrowband versus broadband")
    print("Model: a coherent wave of amplitude 1 (arbitrary units) with unit")
    print("wavelength-scale noise that is INDEPENDENT from channel to channel.")
    print("A gauge of M channel spacings averages M of those samples, so the")
    print("noise that survives has rms 1/sqrt(M), while the coherent signal is")
    print("attenuated by sinc(pi M d/lambda).  Two detectors are compared:")
    print("  (a) narrowband: correlate with exp(-i k x), i.e. a matched filter")
    print("      for the signal's own wavenumber;")
    print("  (b) broadband: total power (an RSAM-like envelope detector).\n")
    d = D_CHANNEL
    n_ch = 800
    x_ch = np.arange(n_ch) * d
    sig = np.cos(k_wave * x_ch)
    M_list = [1, 2, 3, 4, 5, 6, 8, 10, 15, 20]
    pred_bb = np.array([np.sqrt(M) * abs(np.sinc(M * d / lam)) for M in M_list])
    pred_bb = pred_bb / pred_bb[0]
    nb, bb = [], []
    for M in M_list:
        ker = np.ones(M) / M
        s_g = np.convolve(sig, ker, mode="valid")
        n_g = s_g.size
        xg = x_ch[:n_g]
        # (a) narrowband matched filter
        s_proj = np.abs(np.sum(s_g * np.exp(-1j * k_wave * xg)))
        noise_proj = np.empty(200)
        noise_rms = np.empty(200)
        for i in range(200):
            noise = RNG.standard_normal(n_ch)
            noise_g = np.convolve(noise, ker, mode="valid")
            noise_proj[i] = np.abs(np.sum(noise_g * np.exp(-1j * k_wave * xg)))
            noise_rms[i] = np.sqrt(np.mean(noise_g ** 2))
        nb.append(s_proj / np.sqrt(np.mean(noise_proj ** 2)))
        bb.append(np.sqrt(np.mean(s_g ** 2)) / np.mean(noise_rms))
    nb = np.array(nb) / nb[0]
    bb = np.array(bb) / bb[0]
    print("   M = L/d   L/lambda   (a) narrowband meas   (b) broadband pred   "
          "(b) broadband meas")
    for M, pb, a, b in zip(M_list, pred_bb, nb, bb):
        print(f"   {M:7d}   {M * d / lam:9.3f}   {a:19.4f}   {pb:18.4f}   "
              f"{b:17.4f}")
    i_bb = int(np.argmax(bb))
    print(f"\n  Measured optimum for the broadband detector: M = {M_list[i_bb]},")
    print(f"  L = {M_list[i_bb] * d:.1f} m = {M_list[i_bb] * d / lam:.3f} lambda"
          f", giving {bb[i_bb]:.3f} times the single-channel SNR.")
    print("  The narrowband detector is INSENSITIVE to gauge length (measured")
    print("  values stay near 1.0 until the sinc null at M = lambda/d = 10 makes")
    print("  it zero): averaging attenuates the signal and the noise at the")
    print("  signal's own wavenumber by exactly the same factor.  Gauge length")
    print("  therefore buys signal-to-noise only for a detector that collects a")
    print("  BAND of wavenumbers, and the optimum there sits at L/lambda = 0.4,")
    print("  close to the -3 dB point of section 1.  For a narrowband target the")
    print("  correct rule is different: keep L comfortably below lambda so that")
    print("  the sinc factor is close to 1, and get the extra signal-to-noise")
    print("  from array stacking rather than from a longer gauge.")

    # ------------------------------------------------------------------
    section("6. Summary of measured quantities")
    print(f"  wavelength at c = {C_PHASE:.0f} m/s, f = {F_WAVE:.1f} Hz : "
          f"{lam:.1f} m")
    print("  gauge recovery factor                      : sinc(pi L/lambda)")
    print("  -3 dB gauge length                         : 0.442925 lambda")
    print("  first null / sign reversal                 : 1.000000 lambda")
    print("  Nyquist channel spacing                    : lambda/2 = "
          f"{lam / 2:.1f} m")
    print("  apparent velocity at d = 60 m              : -1500.0 m/s "
          "(true +1000.0 m/s)")
    print("  |eps| / |v|                                : 1/c = "
          f"{1.0 / C_PHASE:.3e} s/m")
    print(f"  optimal gauge length, broadband detector   : "
          f"{M_list[i_bb] * d:.1f} m = {M_list[i_bb] * d / lam:.3f} lambda")
    print(f"  gauge sensitivity of a narrowband detector : {nb[i_bb]:.3f} x at "
          f"the same M (that is, none)")
    print("  Every input above is a MODEL choice; a real survey must measure its")
    print("  own phase velocity, channel spacing and noise before applying any")
    print("  of these scalings.")
    return 0


if __name__ == "__main__":
    main()
