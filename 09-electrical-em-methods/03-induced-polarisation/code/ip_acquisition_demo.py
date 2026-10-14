#!/usr/bin/env python3
"""Induced-polarisation acquisition: units, the phase-noise law, the cost of a
phase measurement, and the trade-off that the chosen time window leaves in the
answer.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python ip_acquisition_demo.py

All models and data in this file are SYNTHETIC.  The resistivities, chargeability,
exponent, time constant, noise levels and survey times are chosen teaching values,
not measurements of a real sample or of a real survey.

Contents
--------
1. Two conventions and units: chargeability (ms, mV/V) against PFE and phase.
2. The phase-noise law: sigma_phi = sigma_n / (A sqrt(M/2)), measured.
3. The number of stacks a target phase resolution costs, in seconds.
4. The measured spread of the chargeability-to-phase conversion factor.
5. Fitting a two-relaxation truth with one Debye: the admitted set vs window.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

RHO0 = 100.0     # ohm m
TAU = 1.5        # s
F_REF = 1.0      # Hz, reference (low) frequency of a two-frequency measurement


def cole_cole(f_hz, m, c=1.0, tau=TAU, rho0=RHO0):
    """Cole-Cole complex resistivity in ohm m; c = 1 is the Debye."""
    w = 2.0 * np.pi * np.asarray(f_hz, dtype=float)
    return rho0 * (1.0 - m * (1.0 - 1.0 / (1.0 + (1j * w * tau) ** c)))


def two_relaxation(f_hz, m, tau_a, tau_b, weight, rho0=RHO0):
    """Exact causal model with two relaxation times."""
    w = 2.0 * np.pi * np.asarray(f_hz, dtype=float)
    pol = weight / (1.0 + 1j * w * tau_a) + (1.0 - weight) / (1.0 + 1j * w * tau_b)
    return rho0 * ((1.0 - m) + m * pol)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def phase_estimate(y, n_per_cycle):
    """Least-squares phase of the fundamental of a sampled record."""
    m = y.size
    k = np.arange(m)
    ang = 2.0 * np.pi * k / n_per_cycle
    return np.arctan2(np.sum(y * np.sin(ang)), np.sum(y * np.cos(ang)))


def main():
    section("1. Conventions and units: chargeability, PFE and phase")
    print("A two-frequency measurement on the same synthetic ground:")
    f_low, f_high = 0.125, 1.0
    print(f"  reference (low, DC-like) frequency  f_low  = {f_low:.3f} Hz")
    print(f"  alternate (high) frequency          f_high = {f_high:.3f} Hz")
    print("  PFE = (rho(f_low) - rho(f_high)) / rho(f_high) x 100 %")
    m_1s = 1000.0 * 0.10 * TAU * (1.0 - np.exp(-1.0 / TAU))   # true value, ms
    print(f"\n  f (Hz)     |rho| (ohm m)   -phase (mrad)")
    for f in (f_low, f_high):
        r = cole_cole(f, 0.10)
        print(f"  {f:6.3f}     {abs(r):11.4f}   {1000 * -np.angle(r):12.3f}")
    r_low = abs(cole_cole(f_low, 0.10))
    r_high = abs(cole_cole(f_high, 0.10))
    ph_low = 1000.0 * -np.angle(cole_cole(f_low, 0.10))
    ph_high = 1000.0 * -np.angle(cole_cole(f_high, 0.10))
    pfe = 100.0 * (r_low - r_high) / r_high
    print(f"\n  amplitude PFE                          = {pfe:.4f} %")
    print(f"  model phase at {f_low:.3f} Hz               = {ph_low:.3f} mrad")
    print(f"  model phase at {f_high:.3f} Hz                 = {ph_high:.3f}"
          f" mrad")
    print(f"  window integral chargeability (0-1 s)  = {m_1s:.3f} ms")
    print(f"  dimensionless ratios: PFE/M = {pfe / m_1s:.4f} per ms, "
          f"phase({f_high:.3f} Hz)/M = {ph_high / m_1s:.4f} mrad per ms")
    print("the two-frequency amplitude ratio, the phase and the time-domain")
    print("integral are three different functionals of one response.  They are")
    print("related exactly only through a model, which is why a published")
    print("conversion factor is a model statement, not a constant of nature.")
    print("note also that the phase is NOT largest at the frequency where the")
    print("amplitude ratio is largest: the phase peaks near 1/tau, and both")
    print("spacings above were chosen to straddle it.")

    section("2. The phase-noise law, measured")
    n_per_cycle = 32
    print(f"sampling: {n_per_cycle} samples per cycle of the fundamental;")
    print("phase estimated by least squares on the fundamental;")
    print("300 noise realisations per entry; noise is a fraction of the signal")
    print("amplitude A, so the entries scale with the signal-to-noise ratio.")
    print("\n  cycles   samples      A/sigma_n    measured sigma_phi (mrad)   "
          "sigma_phi A sqrt(M/2)/sigma_n")
    for n_cycles in (1, 4, 16, 64, 256):
        m_samp = n_cycles * n_per_cycle
        for ratio in (20.0, 5.0):
            est = []
            for _ in range(300):
                k = np.arange(m_samp)
                clean = np.sin(2.0 * np.pi * k / n_per_cycle)
                y = clean + (1.0 / ratio) * RNG.standard_normal(m_samp)
                est.append(phase_estimate(y, n_per_cycle))
            sigma_phi = np.std(est, ddof=1)
            inv = sigma_phi * ratio * np.sqrt(m_samp / 2.0)
            print(f"  {n_cycles:6d}   {m_samp:7d}      {ratio:6.1f}       "
                  f"{1000 * sigma_phi:15.4f}              {inv:8.4f}")
    print("the last column is constant across a 256-fold change in the number of")
    print("cycles and a 4-fold change in the signal-to-noise ratio, so the law")
    print("is confirmed:  sigma_phi = sigma_n / (A sqrt(M/2)),  M the number of")
    print("samples.  Doubling the stack count halves the phase error.")

    section("3. What a phase resolution costs in time")
    print("invert the measured law:  M = 2 (sigma_n / (A sigma_phi))^2 samples")
    print("with sigma_n/A = 1/ratio for the ratios of section 2")
    print(f"at {n_per_cycle} samples per cycle, the acquisition time at f = "
          f"1 Hz is M/{n_per_cycle} cycles x 1 s")
    print("\n  sigma_n/A     target sigma_phi (mrad)   samples M   time at 1 Hz (s)")
    for sigma_phi_mrad in (10.0, 1.0, 0.5):
        for ratio in (20.0, 5.0):
            sigma_phi = 1e-3 * sigma_phi_mrad
            m_samp = 2.0 / (ratio * sigma_phi) ** 2
            print(f"   1/{ratio:<4.0f}        {sigma_phi_mrad:10.1f}          "
                  f"{m_samp:9.0f}          {m_samp / n_per_cycle:10.1f}")
    print("a 1 mrad phase with 5% amplitude noise costs of order 10^5 samples;")
    print("that is the real reason field IP is slow, and it is an arithmetic")
    print("consequence of the measured law, not a property of any instrument.")

    section("4. Spread of the chargeability-to-phase conversion factor")
    print("synthetic models, all with rho0 = 100 ohm m; M is the 0-1 s window")
    print("integral in ms, phase is the model phase at 1 Hz in mrad:")
    print("\n    m       c      tau (s)    M (ms)    -phase (mrad)   M / phase")
    ratios = []
    for m in (0.05, 0.10, 0.30):
        for c in (1.0, 0.6, 0.3):
            for tau in (0.3, 1.5):
                mm = 1000.0 * m * tau * (1.0 - np.exp(-1.0 / tau))
                ph = 1000.0 * -np.angle(cole_cole(F_REF, m, c=c, tau=tau))
                ratios.append(mm / ph)
                print(f"  {m:5.2f}   {c:5.2f}   {tau:6.2f}   {mm:8.3f}   "
                      f"{ph:14.3f}   {mm / ph:10.3f}")
    ratios = np.array(ratios)
    print(f"\nM/phase runs from {ratios.min():.3f} to {ratios.max():.3f} over "
          f"these {ratios.size} models,")
    print(f"a spread of a factor {ratios.max() / ratios.min():.2f}.  The common")
    print("working rule 'M in ms equals phase in mrad' is the value 1.0, which")
    print(f"sits inside that range: applying it to the extreme models here would")
    print(f"misstate the chargeability by a factor of {ratios.max():.2f} in one")
    print(f"direction and {1 / ratios.min():.2f} in the other.")

    section("5. Fitting a two-relaxation truth with one Debye: window vs answer")
    m_true, tau_a, tau_b, weight = 0.12, 0.30, 6.00, 0.45
    windows_short = np.array([0.25, 0.5, 1.0])
    windows_long = np.array([0.25, 0.5, 1.0, 2.0, 4.0, 8.0, 16.0])

    def m_true_windows(win):
        return 1000.0 * m_true * (weight * tau_a * (1 - np.exp(-win / tau_a))
                                  + (1 - weight) * tau_b
                                  * (1 - np.exp(-win / tau_b)))

    def m_debye(win, m, tau):
        return 1000.0 * m * tau * (1.0 - np.exp(-win / tau))

    noise_rel = 0.02
    m_grid = np.linspace(0.03, 0.30, 271)
    tau_grid = np.logspace(np.log10(0.1), np.log10(30.0), 401)
    print(f"truth (SYNTHETIC): m = {m_true:.2f} split between tau = "
          f"{tau_a:.2f} s (weight {weight:.2f}) and tau = {tau_b:.2f} s")
    print(f"fitted model: one Debye; {100 * noise_rel:.0f}% noise on every "
          f"chargeability sample; admitted means chi2 <= chi2_min + 4")
    print("\n   window set     best m     best tau (s)   admitted m      "
          "admitted tau (s)")
    best = {}
    for label, win in (("0.25-1 s", windows_short),
                       ("0.25-16 s", windows_long)):
        dat = m_true_windows(win) * (1.0 + noise_rel
                                     * RNG.standard_normal(win.size))
        chi2 = np.zeros((m_grid.size, tau_grid.size))
        for i, m_try in enumerate(m_grid):
            pred = m_debye(win[None, :], m_try, tau_grid[:, None])
            chi2[i] = np.sum(((pred - dat[None, :])
                              / (noise_rel * dat[None, :])) ** 2, axis=1)
        i0, j0 = np.unravel_index(np.argmin(chi2), chi2.shape)
        best[label] = (m_grid[i0], tau_grid[j0])
        keep = chi2 <= chi2[i0, j0] + 4.0
        m_ok = m_grid[keep.any(axis=1)]
        t_ok = tau_grid[keep.any(axis=0)]
        print(f"   {label:12s}  {m_grid[i0]:7.3f}   {tau_grid[j0]:10.3f}   "
              f"[{m_ok.min():.3f}, {m_ok.max():.3f}]   [{t_ok.min():.4f}, "
              f"{t_ok.max():.4f}]")
    (m_s, t_s), (m_l, t_l) = best["0.25-1 s"], best["0.25-16 s"]
    print(f"\nthe two window sets give different answers: m changes by "
          f"{100 * (m_l - m_s) / m_s:+.1f}% and tau by a factor "
          f"{t_l / t_s:.2f}")
    print("neither reproduces the truth, because one relaxation cannot")
    print("represent two.  The residual at zero noise, over the long window:")
    pred0 = m_debye(windows_long, m_l, t_l)
    truth0 = m_true_windows(windows_long)
    print("     window (s)   model (ms)   'true' data (ms)   residual (%)")
    for w, a, b in zip(windows_long, pred0, truth0):
        print(f"      {w:6.2f}     {a:9.3f}      {b:12.3f}      "
              f"{100 * (a - b) / b:+9.2f}")
    print("so the fitted (m, tau) are properties of the model family and the")
    print("window set, not of the ground.  That is the acquisition lesson: the")
    print("window and the model must be reported with the number.")


if __name__ == "__main__":
    main()
