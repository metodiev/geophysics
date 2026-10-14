#!/usr/bin/env python3
"""Site characterisation: Vs30 averaging, its layer sensitivity, the site
period, and the 1-D SH transfer function of a layered soil column.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python seismic_hazards_site_demo.py

Everything is SYNTHETIC.  The two soil profiles, the densities, the damping and
the Monte Carlo perturbation size are chosen teaching values, not measurements.
No real site, borehole or recording is used.

Contents
--------
1. Vs30 as a travel-time average; comparison with the arithmetic and harmonic
   means of the same layer velocities.
2. Why Vs30 weights layers by travel time: measured d ln Vs30 / d ln Vs_i
   against the exact time-weighted fraction h_i/(Vs_i T).
3. Two different profiles with the same Vs30, and the site classes they share.
4. Site period: 4H/Vs30 against the fundamental resonance measured from the
   transfer function.
5. Verification of the layered transfer matrix against the closed form for a
   single layer on a half-space.
6. Peak amplification against the impedance contrast, and the effect of damping.
7. "The" amplification factor depends on the band it is averaged over.
8. Monte Carlo and analytic uncertainty of Vs30 for a 10 % layer-velocity error.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC soil columns (chosen, not measured) ---------------------------
# Each layer: (thickness m, Vs m/s, density kg/m^3), ordered top to bottom.
PROFILE_A = ((6.0, 120.0, 1800.0), (9.0, 180.0, 1850.0), (15.0, 300.0, 1900.0))
PROFILE_B = ((10.0, 100.0, 1750.0), (20.0, 400.0, 1950.0))
HALFSPACE_VS = 900.0        # m/s, bedrock
HALFSPACE_RHO = 2200.0      # kg/m^3
Q_SOIL = 20.0               # constant-Q teaching value for the soil layers
Q_ROCK = 100.0              # and for the half-space
DEPTH_REF_M = 30.0          # the reference depth of Vs30

# NEHRP / IBC site-class boundaries in Vs30 (m/s): exact standard constants.
NEHRP_BOUNDARIES = (1500.0, 760.0, 360.0, 180.0)
NEHRP_CLASSES = ("A", "B", "C", "D", "E")


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def vs30_of_profile(layers, depth_m=DEPTH_REF_M):
    """Vs30 = depth / sum(thickness/Vs) over the top ``depth_m`` metres.

    Layers must sum to ``depth_m`` (or more, in which case the deepest is
    truncated).  Units: (m) / (s) = m/s.
    """
    travel = 0.0
    used = 0.0
    for h, vs, _rho in layers:
        take = min(h, depth_m - used)
        if take <= 0.0:
            break
        travel += take / vs
        used += take
    if used < depth_m:
        raise ValueError("profile is thinner than the reference depth")
    return depth_m / travel


def transfer_function(freqs_hz, layers, vs_hs, rho_hs, q_soil, q_hs):
    """1-D SH transfer function, surface / bedrock outcrop, complex.

    Vertical incidence.  Damping is the standard first-order constant-Q
    substitution with a complex velocity,

        v* = v (1 - i/(2Q)),   k = omega/v*,   mu* = rho v*^2,

    which keeps the medium consistent (k = omega/v* and mu* = rho v*^2 are the
    same statement).  The propagator of a layer maps (u, tau) at its top to
    (u, tau) at its bottom:

        M = [[cos(k h), sin(k h)/(mu k)], [-mu k sin(k h), cos(k h)]]

    The free surface has tau = 0 and the transfer function follows from matching
    to the half-space field.  Q = np.inf recovers the elastic case exactly.
    """
    out = np.empty(freqs_hz.shape, dtype=complex)
    for index, f in enumerate(freqs_hz):
        omega = 2.0 * np.pi * f
        M = np.eye(2, dtype=complex)
        for h, vs, rho in layers:
            v_star = vs * (1.0 - 1j / (2.0 * q_soil))
            k = omega / v_star
            mu = rho * v_star ** 2
            P = k * h
            layer = np.array(
                [[np.cos(P), np.sin(P) / (mu * k)],
                 [-mu * k * np.sin(P), np.cos(P)]],
                dtype=complex,
            )
            M = layer @ M
        z_hs = rho_hs * vs_hs * (1.0 - 1j / (2.0 * q_hs))
        out[index] = 1.0 / (M[0, 0] - M[1, 0] / (1j * z_hs * omega))
    return out


def closed_form_single_layer(freqs_hz, h, vs, rho, vs_hs, rho_hs):
    """|T| for one elastic layer on a half-space: 1/sqrt(cos^2 P + a^2 sin^2 P)."""
    P = 2.0 * np.pi * freqs_hz * h / vs
    alpha = (rho * vs) / (rho_hs * vs_hs)
    return 1.0 / np.sqrt(np.cos(P) ** 2 + alpha ** 2 * np.sin(P) ** 2)


def site_class(vs30):
    """NEHRP-style class from Vs30 using the standard boundaries."""
    for name, bound in zip(NEHRP_CLASSES, NEHRP_BOUNDARIES):
        if vs30 > bound:
            return name
    return "E"


def peak_of(freqs, amp, lo=0.1, hi=12.0):
    """Largest amplitude in a band, with its frequency (grid resolution)."""
    mask = (freqs >= lo) & (freqs <= hi)
    idx = np.argmax(amp[mask])
    return amp[mask][idx], freqs[mask][idx]


def first_peak(freqs, amp, lo=0.05, hi=12.0, floor=1.2):
    """First local maximum inside a band that rises above ``floor``.

    The fundamental resonance of a layered column is the lowest such peak; the
    global maximum in the band can belong to a higher mode.
    """
    mask = (freqs >= lo) & (freqs <= hi)
    f, a = freqs[mask], amp[mask]
    for i in range(1, len(a) - 1):
        if a[i] > a[i - 1] and a[i] >= a[i + 1] and a[i] > floor:
            return a[i], f[i]
    return float("nan"), float("nan")


def band_mean(freqs, amp, lo, hi):
    mask = (freqs >= lo) & (freqs <= hi)
    return float(amp[mask].mean())


def main():
    print("06-10-05 site characterisation -- SYNTHETIC profiles, no field data")

    layers_a = PROFILE_A
    layers_b = PROFILE_B
    vs30_a = vs30_of_profile(layers_a)
    vs30_b = vs30_of_profile(layers_b)

    section("1. Vs30 is a travel-time average, not an arithmetic mean")
    for name, layers, vs30 in (("A", layers_a, vs30_a), ("B", layers_b, vs30_b)):
        hs = np.array([h for h, _, _ in layers])
        vss = np.array([vs for _, vs, _ in layers])
        travel = float(np.sum(hs / vss))
        arith = float(np.sum(hs * vss) / hs.sum())
        print(f"  profile {name}: " +
              ", ".join(f"{h:.0f} m @ {vs:.0f} m/s" for h, vs, _ in layers))
        print(f"    vertical travel time to {DEPTH_REF_M:.0f} m = {travel:.6f} s")
        print(f"    Vs30 = {DEPTH_REF_M:.0f} m / {travel:.6f} s = {vs30:.2f} m/s")
        print(f"    thickness-weighted arithmetic mean        = {arith:.2f} m/s"
              f"   ({arith / vs30 - 1.0:+.2%} against Vs30)")
    print("  -> Vs30 is exactly the thickness-weighted harmonic mean of the layer")
    print("     velocities, so the arithmetic/harmonic inequality forces it to sit")
    print("     below the arithmetic mean; the gap grows with the velocity spread.")

    section("2. Which layer does Vs30 actually constrain?")
    print("  exact result: d ln Vs30 / d ln Vs_i equals the fraction of the")
    print("  vertical travel time spent in layer i, w_i = (h_i/Vs_i)/T.")
    for name, layers, vs30 in (("A", layers_a, vs30_a), ("B", layers_b, vs30_b)):
        hs = np.array([h for h, _, _ in layers])
        vss = np.array([vs for _, vs, _ in layers])
        travel = np.sum(hs / vss)
        w = (hs / vss) / travel
        print(f"  profile {name} (Vs30 = {vs30:.2f} m/s):")
        print("    layer   h (m)   Vs (m/s)   w_i (exact)   w_i (measured, "
              "central +/-1 %)")
        for i, (h, vs, _) in enumerate(layers):
            up = list(layers)
            up[i] = (h, vs * 1.01, layers[i][2])
            down = list(layers)
            down[i] = (h, vs * 0.99, layers[i][2])
            meas = ((vs30_of_profile(up) / vs30_of_profile(down)) - 1.0) / 0.02
            print(f"      {i + 1}     {h:5.1f}   {vs:8.1f}   {w[i]:9.4f}     "
                  f"{meas:11.4f}")
        print(f"    sum of w_i = {w.sum():.4f}  (the sensitivities add to one)")

    section("3. Two profiles, one Vs30, one site class")
    print(f"  Vs30(A) = {vs30_a:.2f} m/s, Vs30(B) = {vs30_b:.2f} m/s, "
          f"difference = {abs(vs30_a - vs30_b):.2e} m/s")
    print(f"  site class from the standard boundaries "
          f"{'/'.join(f'{b:.0f}' for b in NEHRP_BOUNDARIES)} m/s:")
    for name, vs30 in (("A", vs30_a), ("B", vs30_b)):
        print(f"    profile {name}: Vs30 = {vs30:.2f} m/s -> class {site_class(vs30)}")
    print("  -> identical Vs30, identical site class: by themselves these two")
    print("     profiles cannot be told apart.")

    section("4. Site period: the 4H/Vs30 rule against the measured resonance")
    freqs = np.arange(0.02, 12.0, 0.002)
    T_pred = 4.0 * DEPTH_REF_M / vs30_a
    print(f"  uniform-column rule: T0 = 4H/Vs30 = 4 x {DEPTH_REF_M:.0f} m / "
          f"{vs30_a:.2f} m/s = {T_pred:.4f} s  (f0 = {1.0 / T_pred:.4f} Hz)")
    peaks = {}
    for name, layers in (("A", layers_a), ("B", layers_b)):
        amp = np.abs(transfer_function(freqs, layers, HALFSPACE_VS,
                                       HALFSPACE_RHO, Q_SOIL, Q_ROCK))
        pk, f_pk = first_peak(freqs, amp)
        peaks[name] = (pk, 1.0 / f_pk)
        print(f"  profile {name}: fundamental resonance at f = {f_pk:.4f} Hz "
              f"(T = {1.0 / f_pk:.4f} s), |T| = {pk:.4f}")
        print(f"             T_rule/T_measured = {T_pred * f_pk:.3f}; band mean "
              f"0.1-10 Hz = {band_mean(freqs, amp, 0.1, 10.0):.4f}")
    print(f"  the two peaks differ by a factor {peaks['B'][0] / peaks['A'][0]:.3f}"
          f" and their periods by {peaks['B'][1] / peaks['A'][1]:.3f}")
    print("  -> the rule gives the right order of magnitude and the wrong number:")
    print("     it is exact only for a uniform column on rigid rock. Two profiles")
    print("     with identical Vs30 have different periods and different peaks.")

    section("5. Verification: layered transfer matrix vs the single-layer closed form")
    single = ((30.0, 200.0, 1900.0),)
    tm = np.abs(transfer_function(freqs, single, HALFSPACE_VS, HALFSPACE_RHO,
                                  np.inf, np.inf))   # Q -> infinity: elastic
    cf = closed_form_single_layer(freqs, 30.0, 200.0, 1900.0,
                                  HALFSPACE_VS, HALFSPACE_RHO)
    dev = np.max(np.abs(tm - cf))
    print("  lossless single layer: 30 m, Vs = 200 m/s, rho = 1900 kg/m^3 over")
    print(f"  {HALFSPACE_VS:.0f} m/s, {HALFSPACE_RHO:.0f} kg/m^3, Q -> infinity")
    print(f"  impedance ratio Z_hs/Z_soil = "
          f"{HALFSPACE_RHO * HALFSPACE_VS / (1900.0 * 200.0):.4f}")
    print(f"  max |transfer matrix - closed form| over {freqs.size} frequencies "
          f"= {dev:.3e}")
    rigid = 1e15
    tm_q = np.abs(transfer_function(freqs, single, rigid, 1900.0, Q_SOIL, np.inf))
    v_star = 200.0 * (1.0 - 1j / (2.0 * Q_SOIL))
    kh = 2.0 * np.pi * freqs * 30.0 / v_star
    cf_q = np.abs(1.0 / np.cos(kh))
    dev_q = np.max(np.abs(tm_q - cf_q))
    print(f"  damped layer (Q = {Q_SOIL:.0f}) on a rigid base: the closed form is")
    print(f"  1/|cos(k h)| with the same k = omega/v*, v* = v(1 - i/(2Q));")
    print(f"  max deviation over {freqs.size} frequencies = {dev_q:.3e}")
    print(f"  peak: transfer matrix {tm_q.max():.4f}, closed form {cf_q.max():.4f}")
    kh_alt = (2.0 * np.pi * freqs / 200.0) * (1.0 - 1j / (2.0 * Q_SOIL)) * 30.0
    pk_alt = np.abs(1.0 / np.cos(kh_alt)).max()
    print("  the alternative first-order form k = (omega/v)(1 - i/(2Q)) gives a")
    print(f"  peak of {pk_alt:.4f} ({pk_alt / cf_q.max() - 1.0:+.2%}): the two")
    print("  conventions differ at second order in 1/Q, which is the level at")
    print("  which any constant-Q statement is defined.")
    print("  -> the agreement is to about 1e-10 in absolute terms, the residual")
    print("     being amplified by the sharpness of the resonance. It validates")
    print("     the propagator and the free-surface / half-space matching, with")
    print("     and without damping.")

    section("6. Peak amplification scales with the impedance contrast")
    print("  lossless single layer, Vs = 200 m/s over a half-space:")
    print("    Vs_hs (m/s)   Z_hs/Z_soil   peak |T| (measured)   f_peak (Hz)")
    for vs_hs in (400.0, 600.0, 900.0, 1800.0):
        amp = np.abs(transfer_function(freqs, single, vs_hs, HALFSPACE_RHO,
                                       np.inf, np.inf))
        peak, f_peak = peak_of(freqs, amp)
        print(f"    {vs_hs:10.0f}   {HALFSPACE_RHO * vs_hs / (1900.0 * 200.0):11.4f}"
              f"   {peak:17.4f}   {f_peak:10.4f}")
    print("  damping for the synthetic soil profile A (Vs30 = "
          f"{vs30_a:.2f} m/s):")
    print("    Q          fundamental |T|   f0 (Hz)      largest |T| in band")
    for q in (np.inf, 1000.0, 100.0, 50.0, 20.0, 10.0, 5.0):
        amp = np.abs(transfer_function(freqs, layers_a, HALFSPACE_VS,
                                       HALFSPACE_RHO, q, Q_ROCK))
        peak, f_peak = first_peak(freqs, amp)
        gmx, _ = peak_of(freqs, amp)
        label = "inf" if not np.isfinite(q) else f"{q:.0f}"
        print(f"    {label:>6}   {peak:13.4f}   {f_peak:9.4f}   {gmx:14.4f}")
    print("  -> for a single layer the lossless peak is exactly the impedance")
    print("     ratio; for the layered column it is set by the whole stack. Damping")
    print("     decides how much of that peak is realised, and it also moves it.")

    section("7. 'The' amplification factor is a band average")
    amp_a = np.abs(transfer_function(freqs, layers_a, HALFSPACE_VS,
                                     HALFSPACE_RHO, Q_SOIL, Q_ROCK))
    amp_b = np.abs(transfer_function(freqs, layers_b, HALFSPACE_VS,
                                     HALFSPACE_RHO, Q_SOIL, Q_ROCK))
    print("    band (Hz)    mean |T| profile A   mean |T| profile B")
    for lo, hi in ((0.05, 1.0), (0.1, 10.0), (0.5, 2.0), (0.5, 10.0), (2.0, 10.0)):
        print(f"    {lo:4.2f}-{hi:4.1f}   {band_mean(freqs, amp_a, lo, hi):18.4f}"
              f"   {band_mean(freqs, amp_b, lo, hi):18.4f}")
    print("  -> the same site has factors from 1.11 to 2.49 depending only on the")
    print("     band: a site factor is meaningless without its band. Note also that")
    print("     the two profiles differ by ~1 % in band mean but by 43 % in peak,")
    print("     so a band-averaged factor hides exactly what Vs30 failed to see.")

    section("8. Uncertainty of Vs30 for a 10 % layer-velocity error")
    sigma_frac = 0.10
    hs = np.array([h for h, _, _ in layers_a])
    vss = np.array([vs for _, vs, _ in layers_a])
    w = (hs / vss) / np.sum(hs / vss)
    analytic = vs30_a * np.sqrt(np.sum((w * sigma_frac) ** 2))
    n_mc = 20000
    draws = vss[None, :] * (1.0 + sigma_frac * RNG.standard_normal((n_mc, vss.size)))
    vs30_draws = DEPTH_REF_M / np.sum(hs[None, :] / draws, axis=1)
    print(f"  profile A, each layer Vs perturbed independently by sigma = "
          f"{sigma_frac:.0%}")
    print(f"  analytic (quadrature of the w_i weights): sigma_Vs30 = "
          f"{analytic:.3f} m/s ({analytic / vs30_a:.2%})")
    print(f"  Monte Carlo, {n_mc} realisations           : sigma_Vs30 = "
          f"{vs30_draws.std(ddof=1):.3f} m/s "
          f"({vs30_draws.std(ddof=1) / vs30_a:.2%})")
    print(f"  Monte Carlo mean Vs30 = {vs30_draws.mean():.2f} m/s "
          f"(profile value {vs30_a:.2f} m/s)")
    print(f"  5th-95th percentile range: {np.percentile(vs30_draws, 5):.1f} to "
          f"{np.percentile(vs30_draws, 95):.1f} m/s")
    print("  -> the relative uncertainty of Vs30 is smaller than the relative")
    print("     uncertainty of the velocities, because the weights sum to one")
    print("     and the errors are independent: quadrature averages them down.")

    print("\ndone")


if __name__ == "__main__":
    main()
