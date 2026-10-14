#!/usr/bin/env python3
"""GPR attenuation and penetration: the loss constant alpha, the two-way
amplitude budget, the frequency trade-off, and two independent measurements of
alpha and Q from synthetic reflections.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gpr_attenuation_penetration_demo.py

Everything here is SYNTHETIC.  The conductivities, quality factors, reflection
coefficient, noise level and detectability threshold are CHOSEN MODEL
PARAMETERS, not measurements; each is labelled where it is used.  No field site,
instrument or published number is involved.

Contents
--------
1. alpha = (sigma/2) sqrt(mu/eps) in the low-loss regime: 1/m, dB/m, skin depth.
2. Two-way attenuation loss in dB over depth.
3. The frequency trade-off: alpha(f) = alpha_cond + pi f / (v Q), and the
   penetration depth implied by a stated dynamic-range budget.
4. A complete two-way amplitude budget: spreading, reflection and attenuation,
   with the depth at which a stated threshold is crossed.
5. Measuring alpha and Q from the spectral ratio of two reflections.
6. The spectral-centroid downshift as a Q estimator, tested in its own
   (weak-attenuation) regime of validity.
7. Cross-check of alpha by a second, amplitude-only route, and why it is biased.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

C_M_NS = 0.299792458
EPS0_F_M = 8.8541878128e-12
MU0_H_M = 4.0e-7 * np.pi

# SYNTHETIC site model (chosen teaching values, not measured)
EPS_R = 16.0            # wet sand, relative permittivity
SIGMA_S_M = 1.0e-3      # electrical conductivity, S/m
Q_MODEL = 12.0          # quality factor for the non-conduction loss (chosen)
V_M_NS = C_M_NS / np.sqrt(EPS_R)
F0_HZ = 200e6           # nominal antenna frequency
NOISE_FLOOR_DB = -80.0  # chosen detectability threshold, dB relative to 1 m
NOISE_FRAC = 1.0e-4     # chosen spectral noise amplitude, fraction of the source


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def alpha_cond(eps_r, sigma):
    """Low-loss conduction attenuation constant, 1/m."""
    return 0.5 * sigma * np.sqrt(MU0_H_M / (EPS0_F_M * eps_r))


def alpha_q(f_hz, q, v_ms=None):
    """Constant-Q attenuation constant pi f / (v Q), 1/m."""
    v = (v_ms if v_ms is not None else V_M_NS * 1e9)
    return np.pi * f_hz / (v * q)


def alpha_total(eps_r, sigma, f_hz, q):
    """Conduction plus constant-Q loss, 1/m."""
    return alpha_cond(eps_r, sigma) + alpha_q(f_hz, q)


def ricker(t, t0, f0):
    tau = t - t0
    a = (np.pi * f0) ** 2
    return (1.0 - 2.0 * a * tau ** 2) * np.exp(-a * tau ** 2)


def synth_pair(t, freqs, d1, d2, q, noise_frac=NOISE_FRAC):
    """Two synthetic reflection spectra at depths d1 and d2.

    The source wavelet is built at a finite reference time inside the window and
    shifted from there by an exact linear phase, so the only difference between
    the two spectra is the attenuation exp(-2 alpha(f) d).  Building the wavelet
    at t = 0 would truncate half of it and distort every spectrum.
    Returns (W1, W2, band, noise_mag).
    """
    f0_ghz = F0_HZ * 1e-9
    t_ref = 20.0                       # ns, the wavelet's own centre
    w0 = np.fft.rfft(ricker(t, t_ref, f0_ghz))
    a_f = alpha_cond(EPS_R, SIGMA_S_M) + np.pi * freqs / (V_M_NS * 1e9 * q)
    t1, t2 = 2.0 * d1 / V_M_NS, 2.0 * d2 / V_M_NS
    ph1 = np.exp(-2j * np.pi * freqs * (t1 - t_ref) * 1e-9)
    ph2 = np.exp(-2j * np.pi * freqs * (t2 - t_ref) * 1e-9)
    noise_mag = noise_frac * np.max(np.abs(w0))
    n1 = noise_mag * (RNG.standard_normal(freqs.size)
                      + 1j * RNG.standard_normal(freqs.size))
    n2 = noise_mag * (RNG.standard_normal(freqs.size)
                      + 1j * RNG.standard_normal(freqs.size))
    W1 = w0 * ph1 * np.exp(-2.0 * a_f * d1) + n1
    W2 = w0 * ph2 * np.exp(-2.0 * a_f * d2) + n2
    band = ((np.abs(w0) > 1e-3 * np.max(np.abs(w0)))
            & (np.abs(W1) > 10.0 * noise_mag * np.sqrt(2.0))
            & (np.abs(W2) > 10.0 * noise_mag * np.sqrt(2.0)))
    return W1, W2, band, noise_mag


def main():
    section("1. Conduction attenuation alpha = (sigma/2) sqrt(mu/eps)  [low loss]")
    print("   sigma (S/m)  eps_r    alpha (1/m)   alpha (dB/m)   skin depth (m)   "
          "2-way 1/e (m)")
    for sigma in (1e-4, 1e-3, 1e-2, 1e-1):
        for eps_r in (4.0, 16.0, 25.0):
            a = alpha_cond(eps_r, sigma)
            print(f"   {sigma:8.0e}   {eps_r:6.2f}   {a:11.4f}   {8.686*a:12.4f}   "
                  f"{1.0/a:14.3f}   {1.0/(2.0*a):12.3f}")
    print("   Field amplitude decays as exp(-alpha z) one way, so the two-way")
    print("   amplitude decays as exp(-2 alpha z); the last column is the depth")
    print("   at which the two-way amplitude has fallen to 1/e.  This alpha does")
    print("   NOT depend on frequency: conduction loss in the low-loss regime is")
    print("   broadband, so the frequency dependence of penetration must come")
    print("   from another loss mechanism (Section 3).")

    section("2. Two-way attenuation loss in dB over depth (sigma = 1e-3 S/m)")
    a = alpha_cond(EPS_R, SIGMA_S_M)
    print(f"   SYNTHETIC material: eps_r = {EPS_R:.1f}, sigma = {SIGMA_S_M:.0e} S/m,")
    print(f"   v = {V_M_NS:.5f} m/ns; alpha_cond = {a:.4f} 1/m, "
          f"{8.686*a:.3f} dB/m one way")
    print("   depth (m)   2-way loss (dB)   depth (m)   2-way loss (dB)")
    for d in (0.5, 1.0, 2.0, 4.0):
        d2 = d * 3.0
        print(f"   {d:8.1f}   {8.686*2*a*d:15.2f}   {d2:8.1f}   "
              f"{8.686*2*a*d2:15.2f}")
    print("   Both columns use 8.686 x 2 alpha d.  At sigma = 1e-3 S/m the loss")
    print("   is modest; a clay-rich soil at sigma = 0.1 S/m loses the same 3.3 dB")
    print(f"   in {a/alpha_cond(EPS_R, 0.1)*4.0:.3f} m instead of 4.0 m, i.e. a")
    print("   hundred times shallower.")

    section("3. Frequency trade-off: alpha(f) and penetration for a 60 dB budget")
    print(f"   SYNTHETIC model: alpha(f) = alpha_cond + pi f / (v Q), "
          f"Q = {Q_MODEL:.0f} (chosen), eps_r = {EPS_R:.1f}, "
          f"sigma = {SIGMA_S_M:.0e} S/m")
    print("   f (MHz)  lambda (m)   alpha_cond   alpha_Q   alpha total   "
          "alpha (dB/m)")
    v_ms = V_M_NS * 1e9
    for f_mhz in (50, 100, 200, 400, 900):
        f = f_mhz * 1e6
        print(f"   {f_mhz:7.0f}  {v_ms/f:10.3f}   "
              f"{alpha_cond(EPS_R, SIGMA_S_M):10.4f}   "
              f"{alpha_q(f, Q_MODEL):7.4f}   "
              f"{alpha_total(EPS_R, SIGMA_S_M, f, Q_MODEL):11.4f}   "
              f"{8.686*alpha_total(EPS_R, SIGMA_S_M, f, Q_MODEL):11.4f}")
    print("   penetration depth for a 60 dB two-way loss budget "
          "(60 = 8.686 x 2 alpha d):")
    for q in (10.0, 30.0):
        print(f"     Q = {q:4.0f}: ", end="")
        for f_mhz in (50, 100, 200, 400, 900):
            at = alpha_total(EPS_R, SIGMA_S_M, f_mhz * 1e6, q)
            print(f"{60.0/(8.686*2*at):6.2f} m", end=" ")
        print("  (50, 100, 200, 400, 900 MHz)")
    frac = (alpha_cond(EPS_R, SIGMA_S_M)
            / alpha_total(EPS_R, SIGMA_S_M, 50e6, 30.0) * 100.0)
    print("   Lower frequencies penetrate deeper, but the gain saturates as the")
    print("   conduction term takes over: at Q = 30 the conduction term is")
    print(f"   {frac:.0f}% of the total already at 50 MHz, so halving the frequency")
    print("   below 100 MHz buys much less than the factor two that the Q term")
    print("   alone would suggest.  Frequency choice is a competition between")
    print("   penetration and resolution, and the winner depends on the medium.")

    section("4. Two-way amplitude budget and the depth at which it fails")
    print("   SYNTHETIC budget: amplitude(d) = R exp(-2 alpha d) / (2 d), each")
    print("   term referenced to the field amplitude 1 m from the antenna.")
    print("   chosen reflection coefficient |R| = 0.2000, chosen detectability")
    print(f"   threshold {NOISE_FLOOR_DB:.1f} dB, f = {F0_HZ/1e6:.0f} MHz, "
          f"Q = {Q_MODEL:.0f}")
    R = 0.2
    print("   depth (m)  reflection (dB)  spreading (dB)  attenuation (dB)  "
          "total (dB)")
    for d in (0.5, 1.0, 2.0, 3.0, 4.0):
        at = alpha_total(EPS_R, SIGMA_S_M, F0_HZ, Q_MODEL)
        print(f"   {d:9.1f}  {20*np.log10(R):15.2f}  {20*np.log10(1/(2*d)):14.2f}"
              f"  {8.686*2*at*d:16.2f}  "
              f"{20*np.log10(R) + 20*np.log10(1/(2*d)) - 8.686*2*at*d:10.2f}")
    lo, hi = 0.05, 200.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        at = alpha_total(EPS_R, SIGMA_S_M, F0_HZ, Q_MODEL)
        amp_db = (20*np.log10(R) + 20*np.log10(1/(2*mid)) - 8.686*2*at*mid)
        if amp_db > NOISE_FLOOR_DB:
            lo = mid
        else:
            hi = mid
    d_max = 0.5 * (lo + hi)
    at = alpha_total(EPS_R, SIGMA_S_M, F0_HZ, Q_MODEL)
    print(f"   threshold crossed at d = {d_max:.3f} m")
    print(f"   budget at that depth: reflection {20*np.log10(R):+.2f} dB, "
          f"spreading {20*np.log10(1/(2*d_max)):+.2f} dB, "
          f"attenuation {-8.686*2*at*d_max:+.2f} dB")
    print("   Attenuation is by far the largest term: the limit is a LOSS")
    print("   question, not a geometry question, and it is set by the medium,")
    print("   not by the antenna.")

    section("5. Measuring alpha and Q from the spectral ratio of two reflections")
    dt_ns, n_t = 0.05, 4096
    t = np.arange(n_t) * dt_ns
    freqs = np.fft.rfftfreq(n_t, dt_ns * 1e-9)
    d1, d2 = 0.50, 2.50
    W1, W2, band, noise_mag = synth_pair(t, freqs, d1, d2, Q_MODEL)
    ratio = np.log(np.abs(W1) / np.abs(W2))
    slope, intercept = np.polyfit(freqs[band], ratio[band], 1)
    a_rec = intercept / (2.0 * (d2 - d1))
    q_rec = 2.0 * np.pi * (d2 - d1) / (V_M_NS * 1e9 * slope)
    print(f"   two reflectors at {d1:.2f} m and {d2:.2f} m, same reflection")
    print(f"   coefficient; SYNTHETIC model Q = {Q_MODEL:.1f}, "
          f"alpha_cond = {alpha_cond(EPS_R, SIGMA_S_M):.4f} 1/m")
    print(f"   noise amplitude {NOISE_FRAC:.0e} of the source peak; the fitting")
    print(f"   band, set where both spectra exceed ten times the noise, is "
          f"{freqs[band][0]/1e6:.1f}-{freqs[band][-1]/1e6:.1f} MHz "
          f"({band.sum()} bins)")
    print(f"   fitted ln(A1/A2) = {intercept:.4f} + {slope:.5e} x f   (f in Hz)")
    print(f"   recovered alpha_cond = {a_rec:.4f} 1/m "
          f"({(a_rec/alpha_cond(EPS_R, SIGMA_S_M)-1)*100:+.2f}% vs model)")
    print(f"   recovered Q          = {q_rec:.3f} "
          f"({(q_rec/Q_MODEL-1)*100:+.2f}% vs model)")
    print("   The intercept is the frequency-independent (conduction) loss and")
    print("   the slope is the frequency-dependent loss: one straight-line fit")
    print("   separates the two mechanisms.")

    section("6. Spectral centroid downshift: a weak-attenuation estimator")
    d1w, d2w, q_weak = 0.50, 1.00, 60.0
    W1w, W2w, bandw, _ = synth_pair(t, freqs, d1w, d2w, q_weak)
    # the centroid must be computed on the passband only: outside it the noise
    # sets the mean and the estimate becomes meaningless
    src_band = np.abs(np.fft.rfft(ricker(t, 20.0, F0_HZ * 1e-9))) > 1e-3 * np.max(
        np.abs(np.fft.rfft(ricker(t, 20.0, F0_HZ * 1e-9))))
    A1 = np.abs(W1w)[src_band]
    A2 = np.abs(W2w)[src_band]
    fb = freqs[src_band]
    fc1 = np.sum(fb * A1) / np.sum(A1)
    fc2 = np.sum(fb * A2) / np.sum(A2)
    var1 = np.sum(A1 * (fb - fc1) ** 2) / np.sum(A1)
    t_eff = 2.0 * (d2w - d1w) / V_M_NS * 1e-9
    q_cent = np.pi * t_eff * var1 / (fc1 - fc2)
    print("   SYNTHETIC case chosen with WEAK attenuation on purpose:")
    print(f"   Q = {q_weak:.0f}, reflectors at {d1w:.2f} m and {d2w:.2f} m, "
          f"two-way time difference {t_eff*1e9:.2f} ns")
    print(f"   centroids measured over the source passband "
          f"{fb[0]/1e6:.1f}-{fb[-1]/1e6:.1f} MHz")
    print(f"   centroid of the shallow reflection : {fc1/1e6:.3f} MHz")
    print(f"   centroid of the deep reflection    : {fc2/1e6:.3f} MHz")
    print(f"   measured downshift                 : {(fc1-fc2)/1e6:.3f} MHz "
          f"({(fc1-fc2)/fc1*100:.3f}% of the shallow centroid)")
    print(f"   rms bandwidth of the shallow spectrum: {np.sqrt(var1)/1e6:.3f} MHz")
    print(f"   estimator Q = pi t_eff var(f) / (fc1 - fc2) = {q_cent:.2f} "
          f"({(q_cent/q_weak-1)*100:+.2f}% vs model Q = {q_weak:.0f})")
    print("   The centroid formula is a FIRST-ORDER relation: it assumes the loss")
    print("   removes only a small part of the band, and it must be evaluated on")
    print("   the passband where the source has energy.  Applied instead to the")
    print("   strongly attenuating pair of Section 5 the same formula returns a")
    print("   value far from the model Q -- which is why the spectral-ratio fit,")
    print("   not the centroid, is the routine estimator.")

    section("7. Cross-check: alpha from peak amplitudes only, and its bias")
    p1 = np.max(np.abs(np.fft.irfft(W1, n=n_t)))
    p2 = np.max(np.abs(np.fft.irfft(W2, n=n_t)))
    a_amp = np.log(p1 / p2) / (2.0 * (d2 - d1))
    a_ref = alpha_total(EPS_R, SIGMA_S_M, F0_HZ, Q_MODEL)
    print(f"   peak amplitude at {d1:.2f} m: {p1:.4f}; at {d2:.2f} m: {p2:.4f}")
    print(f"   alpha from the peak-amplitude ratio: {a_amp:.4f} 1/m")
    print(f"   the model's total alpha at {F0_HZ/1e6:.0f} MHz is {a_ref:.4f} 1/m "
          f"({(a_amp/a_ref-1)*100:+.1f}%)")
    print(f"   the broadband spectral-ratio estimate of the conduction part was")
    print(f"   {a_rec:.4f} 1/m and the model's conduction part is "
          f"{alpha_cond(EPS_R, SIGMA_S_M):.4f} 1/m "
          f"({(a_rec/alpha_cond(EPS_R, SIGMA_S_M)-1)*100:+.2f}%)")
    print("   The peak-amplitude ratio mixes the frequency-independent loss with")
    print("   the frequency-dependent loss and with pulse broadening; it returns")
    print("   a number that is not any single model parameter.  Two routes that")
    print("   disagree is the signal to ask which quantity each one measures.")
    print("\n   Every number above comes from the SYNTHETIC model of this script;")
    print("   no measured attenuation, Q or penetration depth is quoted.")


if __name__ == "__main__":
    main()
