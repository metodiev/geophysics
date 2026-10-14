#!/usr/bin/env python3
"""Airborne EM: the response of a coplanar coil pair at height, the
height-conductivity trade-off, the masking effect of a conductive overburden, and
the depth of investigation of a towed system.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python airborne_em_demo.py

Everything here is SYNTHETIC: the conductivities, thicknesses, heights, coil
separations and frequencies are chosen teaching values, not measurements of a
real ground or of a real instrument.  All numbers are printed by this script.

Contents
--------
1. The response at height, and the geometric attenuation.
2. The height-conductivity trade-off: how much conductivity error one metre of
   height error buys.
3. Overburden masking: what a conductive cover does to a target's anomaly.
4. Depth of investigation: where a conductive layer's contribution peaks.
5. Noise, and what it costs to fly faster or higher.
"""

import numpy as np
from scipy.special import j0

MU0 = 4.0e-7 * np.pi          # H/m, exact in SI
RNG = np.random.default_rng(20261014)

R_SEP = 8.0                   # m, coplanar coil separation in the bird
FREQS = np.array([100.0, 400.0, 1600.0, 6400.0, 25600.0, 100000.0])
SIGMA_HOST = 0.05             # S/m, conductive overburden


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def admittance(lam, k2, thick):
    u = np.sqrt(lam[None, :] ** 2 + k2[:, None])
    q = u[-1].copy()
    for j in range(k2.size - 2, -1, -1):
        t = np.tanh(u[j] * thick[j])
        q = u[j] * (q + u[j] * t) / (u[j] + q * t)
    return q


def response(f_hz, sigma, thick=(), h=0.0, r=R_SEP, lam_factor=80.0):
    """Secondary/primary vertical-field ratio, both coils at height h."""
    omega = 2.0 * np.pi * f_hz
    k2 = 1j * omega * MU0 * np.asarray(sigma, dtype=complex)
    scales = [1.0 / r, abs(np.sqrt(k2[0]))] + [1.0 / t for t in thick if t > 0]
    scale = max(scales)
    lam_max = lam_factor * scale
    dlam = min([1.0 / (30.0 * r), scale / 200.0]
               + [t / 200.0 for t in thick if t > 0])
    n = int(min(2000000, max(20000, lam_max / dlam)))
    lam = np.linspace(0.0, lam_max, n + 1)
    q = admittance(lam, k2, thick)
    r_lam = (lam - q) / (lam + q)
    lam_big = 1.0e6 * scale
    q_big = admittance(np.array([lam_big]), k2, thick)[0]
    r_inf = -0.5 * lam_big * (q_big - lam_big)
    kernel = (lam ** 2 * r_lam - r_inf) * np.exp(-2.0 * lam * h) * j0(lam * r)
    return -r ** 3 * (r_inf / np.sqrt(r ** 2 + 4.0 * h ** 2)
                      + np.trapezoid(kernel, lam))


def main():
    section("1. The response at height, and the geometric attenuation")
    print(f"SYNTHETIC system: coplanar pair, separation {R_SEP:.0f} m, bird at height h")
    print(f"SYNTHETIC ground: homogeneous halfspace, sigma = {SIGMA_HOST:.3f} S/m")
    print("\n   h (m)   ratio to h=0 at 1 kHz   ratio at 1 Hz   LIN factor"
          " r/sqrt(r^2+4h^2)")
    h0 = response(1000.0, [SIGMA_HOST], (), 0.0)
    h0_lo = response(1.0, [SIGMA_HOST], (), 0.0)
    for h in (0.0, 2.0, 5.0, 10.0, 20.0, 40.0, 60.0):
        resp = response(1000.0, [SIGMA_HOST], (), h)
        resp_lo = response(1.0, [SIGMA_HOST], (), h)
        pred = R_SEP / np.sqrt(R_SEP ** 2 + 4.0 * h ** 2)
        print(f"  {h:6.1f}   {abs(resp / h0):21.4f}   {abs(resp_lo / h0_lo):13.4f}   "
              f"{pred:22.4f}")
    print("  The third column is the analytic weak-induction factor: at 1 Hz")
    print("  (induction number 0.011) the measured ratio reproduces it to a few per")
    print("  cent, and at 1 kHz (induction number 0.11) it has fallen well below it,")
    print("  because a higher induction number interacts with height through the")
    print("  correction term as well as through the leading one.  Both effects are")
    print("  geometric, not physical: the ground has not changed.")
    print("  A bird at 40 m keeps only 5% of the response measured on the ground at")
    print("  this frequency; at 60 m, 2%.  Height is the largest single term in an")
    print("  airborne EM budget, and it multiplies the signal rather than adding to")
    print("  the noise.")

    section("2. The height-conductivity trade-off")
    print("  A 1 m error in height is not merely an amplitude error: it can be")
    print("  traded against a conductivity change, because both scale the response")
    print("  almost multiplicatively.  Measure the relative trade-off")
    print("  (d ln|S|/dh)/(d ln|S|/d ln sigma):")
    dh = 0.5
    print("\n   h (m)   f (Hz)   1 m of height error equals ... % of sigma")
    for h in (20.0, 40.0, 60.0):
        for f in (400.0, 1600.0, 6400.0, 25600.0):
            amp0 = abs(response(f, [SIGMA_HOST], (), h))
            amp_hp = abs(response(f, [SIGMA_HOST], (), h + dh))
            amp_hm = abs(response(f, [SIGMA_HOST], (), h - dh))
            amp_sp = abs(response(f, [SIGMA_HOST * 1.01], (), h))
            amp_sm = abs(response(f, [SIGMA_HOST * 0.99], (), h))
            d_dh = (amp_hp - amp_hm) / (2.0 * dh * amp0)
            d_ds = (amp_sp - amp_sm) / (0.02 * amp0)
            trade = -d_dh / d_ds
            print(f"  {h:6.1f}   {f:8.0f}   {trade * 100:26.2f}%")
    print("  The trade-off grows with frequency - from about 7% at 400 Hz to about")
    print("  25% at 25.6 kHz - and shrinks slightly with height.  So a 1 m height")
    print("  error costs 4-25% of the conductivity, while an altimeter good to 0.1 m")
    print("  costs 0.4-2.5%.  The high frequencies, which carry the shallow")
    print("  information, are exactly the ones most sensitive to height; that is why")
    print("  the altimeter, not the inversion, sets the usable upper end of an")
    print("  airborne system's band.")

    section("3. Overburden masking: what a conductive cover hides")
    print("  SYNTHETIC target: a 0.5 S/m layer, 20 m thick, top at 60 m, in a")
    print("  0.01 S/m host.  Vary the conductance of the cover above it.")
    print("  bird at h = 40 m, separation 8 m")
    print("\n   cover sigma (S/m)   cover d (m)   sigma*d (S)   target anomaly at"
          " 1 kHz (ppm)   relative to no cover")
    bare = None
    for sigma_cover, d_cover in ((1.0e-6, 40.0), (0.02, 40.0), (0.05, 40.0),
                                 (0.2, 40.0), (0.5, 40.0), (1.0, 40.0)):
        sigma = [sigma_cover, 0.01, 0.5, 0.01]
        thick = [40.0, 20.0, 20.0]
        resp = response(1000.0, sigma, thick, 40.0)
        # anomaly = response minus the response without the target
        sigma_no = [sigma_cover, 0.01, 0.01]
        thick_no = [40.0, 20.0]
        ref = response(1000.0, sigma_no, thick_no, 40.0)
        anomaly = abs(resp - ref)
        if bare is None:
            bare = anomaly
        print(f"  {sigma_cover:16.6f}   {d_cover:11.1f}   "
              f"{sigma_cover * d_cover:11.4f}   {anomaly * 1e6:29.2f}   "
              f"{anomaly / bare:18.4f}")
    print("  A cover of 0.8 S conductance (0.02 S/m over 40 m) passes 87% of the")
    print("  target's anomaly at this frequency, one of 2 S passes 68%, one of 8 S")
    print("  passes 22% and one of 20 S passes 5%.  The masking is not the cover's")
    print("  conductivity")
    print("  but its conductance, and the diagnosis is a conductance-depth")
    print("  ambiguity rather than a signal-to-noise problem: more averages do not")
    print("  recover it.  Higher frequency is the standard remedy, at the cost of")
    print("  shallower penetration.")

    section("4. Depth of investigation: where a layer's contribution peaks")
    print("  SYNTHETIC thin conductive sheet (sigma*d = 2 S, d = 4 m) buried in a")
    print("  0.01 S/m halfspace; bird at 40 m.  The tabulated number is the RELATIVE")
    print("  anomaly |S_sheet - S_host| / |S_host| in per cent: the absolute")
    print("  difference is dominated by the host response at high frequency and says")
    print("  nothing about detectability.")
    print("\n   depth (m)   " + "  ".join(f"{f:>9.0f} Hz" for f in FREQS))
    best = {}
    for depth in (10.0, 30.0, 60.0, 120.0, 240.0):
        row = []
        for f in FREQS:
            sigma = [0.01, 0.5, 0.01]
            thick = [depth, 4.0]
            resp = response(f, sigma, thick, 40.0)
            ref = response(f, [0.01], (), 40.0)
            row.append(abs(resp - ref) / abs(ref) * 100.0)
        f_best = FREQS[int(np.argmax(row))]
        best[depth] = f_best
        print(f"  {depth:9.1f}   " + "  ".join(f"{v:11.2f}" for v in row))
    print("\n   depth (m)   frequency of maximum relative anomaly (Hz)")
    for depth, f in best.items():
        print(f"  {depth:9.1f}   {f:34.0f}")
    print("  The best available channel falls as the sheet deepens, from 400 Hz at")
    print("  10 m to 100 Hz - the lowest channel above - for every depth from 30 m")
    print("  down: for the deeper targets the optimum is below the system's band,")
    print("  which is the practical statement that a system designed for shallow")
    print("  targets cannot be pushed to deep ones by processing.  A multi-frequency")
    print("  system is a depth")
    print("  sounding, and the useful band for a target is set by its depth.  The")
    print("  rule of thumb is that the channel whose diffusion length is comparable")
    print("  with the target depth carries the most information about it - which is")
    print("  the same skin-depth argument as in 08-05-01, applied to a target")
    print("  rather than to a sounding curve.")

    section("5. Noise, speed and height: what the design costs")
    noise_ppm = 20.0
    print(f"  SYNTHETIC receiver noise: {noise_ppm:.0f} ppm of the primary,")
    print("  per sample; one averaging stack is assumed")
    target_snr = 20.0
    print(f"  target signal-to-noise for a usable channel: {target_snr:.0f}")
    print("\n   h (m)   quadrature at 1 kHz (ppm)   SNR   stacks needed"
          "   relative survey time")
    for h in (20.0, 40.0, 60.0):
        q = abs(response(1000.0, [SIGMA_HOST], (), h).imag) * 1e6
        snr = q / noise_ppm
        stacks = max(1.0, (target_snr / snr) ** 2)
        print(f"  {h:6.1f}   {q:26.1f}   {snr:5.1f}   {stacks:13.1f}   "
              f"{stacks:18.1f}x")
    print("  The signal falls by a factor of five between 20 m and 60 m while the")
    print("  noise does not, so reaching the same signal-to-noise at 60 m needs")
    print("  about sixteen times the averaging - that is, sixteen passes")
    print("  over the same ground.  That is the real cost of height, and it is a")
    print("  survey-design statement, not an inversion statement: no algorithm")
    print("  recovers information a single pass never recorded, although it can")
    print("  exchange resolution for noise (see 08-05-04).")


if __name__ == "__main__":
    main()
