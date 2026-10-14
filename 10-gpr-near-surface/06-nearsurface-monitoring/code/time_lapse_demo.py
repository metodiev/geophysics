#!/usr/bin/env python3
"""Time-lapse near-surface geophysics: repeatability, the detection threshold of a
travel-time shift, coda-wave interferometry by stretching, and the ambiguity
between a distributed change and a localised one.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python time_lapse_demo.py

Everything here is SYNTHETIC.  The velocities, path lengths, noise levels,
environmental sensitivity, coda length and change magnitudes are chosen teaching
values, not measurements and not site parameters.

Contents
--------
1. Repeatability: NRMS between two noise-only repeats, and its distribution.
2. Travel-time detection threshold: dv/v from a picking error and a path time.
3. Coda-wave interferometry: the stretching estimator and its measured scatter.
4. Environmental aliasing: a temperature change that mimics a target change.
5. The ambiguity: a uniform velocity drop versus a localised water-table rise
   fitted to the same travel-time changes.
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def nrms(a, b):
    """Normalised RMS difference between two traces, in per cent."""
    return 100.0 * np.sqrt(np.mean((a - b) ** 2)) / np.sqrt(
        np.mean(((a + b) / 2.0) ** 2))


def coda_trace(t, rng, band=60.0):
    """A synthetic band-limited coda: random phases in a Gaussian passband."""
    n = t.size
    freq = np.fft.rfftfreq(n, d=t[1] - t[0])
    spectrum = np.exp(-0.5 * ((freq - band) / (band / 3.0)) ** 2) \
        * np.exp(-t[:freq.size] / (t[-1] / 2.5))
    phase = rng.uniform(0.0, 2.0 * np.pi, freq.size)
    return np.fft.irfft(spectrum * np.exp(1j * phase), n=n)


def main():
    section("1. Repeatability of a baseline pair (NRMS)")
    n = 2000
    t = np.linspace(0.0, 2.0, n)
    signal = np.sin(2.0 * np.pi * 30.0 * t) * np.exp(-t / 0.8)
    rms_signal = np.sqrt(np.mean(signal ** 2))
    print(f"  synthetic trace: {n} samples over {t[-1]:.2f} s, rms = {rms_signal:.4f}")
    print("   noise level (%)   measured NRMS (%)")
    for level in (0.5, 1.0, 2.0, 5.0, 10.0):
        a = signal + level / 100.0 * rms_signal * RNG.standard_normal(n)
        b = signal + level / 100.0 * rms_signal * RNG.standard_normal(n)
        print(f"   {level:15.1f}   {nrms(a, b):18.2f}")
    print("  NRMS measures repeatability, not detectability: it compares two")
    print("  independent repeats of the same state, so it sets the noise floor above")
    print("  which a time-lapse change has to rise.")

    section("2. Detection threshold of a travel-time shift")
    print("   path length (m)   v (m/s)   travel time (ms)   dv/v for a 0.5 ms pick")
    for length, v in ((10.0, 400.0), (20.0, 400.0), (20.0, 1500.0), (50.0, 1500.0)):
        tt = length / v
        res = 0.0005 / tt
        print(f"   {length:14.1f}   {v:7.1f}   {tt * 1e3:16.2f}   {res * 100:23.3f}%")
    print("  A travel-time measurement resolves dv/v through the ratio of the picking")
    print("  error to the total travel time: longer paths and slower media buy")
    print("  resolution.  Two per cent on a 10 m path in a 400 m/s medium is the")
    print("  practical floor for a picking-based survey; coda methods beat it.")

    section("3. Coda-wave interferometry by stretching")
    t_coda = np.linspace(0.0, 4.0, 4000)
    dv_true = -0.010        # -1% velocity change, teaching value
    print(f"  synthetic coda: {t_coda.size} samples over {t_coda[-1]:.1f} s with a")
    print(f"  band centred on 60 Hz; the perturbed state is stretched by "
          f"dv/v = {dv_true:+.4f}")
    base_clean = coda_trace(t_coda, RNG)
    rms_c = np.sqrt(np.mean(base_clean ** 2))

    def stretch_estimate(perturbed, t_axis, base):
        """Coarse-to-fine stretch estimate: the epsilon minimising the L2 misfit."""
        coarse = np.linspace(-0.03, 0.03, 121)
        costs = np.array([
            np.mean((base - np.interp(t_axis * (1.0 + e), t_axis, perturbed,
                                     left=0.0, right=0.0)) ** 2)
            for e in coarse])
        e0 = coarse[int(np.argmin(costs))]
        fine = np.linspace(e0 - 0.001, e0 + 0.001, 201)
        costs = np.array([
            np.mean((base - np.interp(t_axis * (1.0 + e), t_axis, perturbed,
                                     left=0.0, right=0.0)) ** 2)
            for e in fine])
        return float(fine[int(np.argmin(costs))])

    # predicted precision: sigma_eps = sigma_noise / sqrt(SUM (t g'(t))^2)
    t_base = t_coda
    deriv = np.gradient(base_clean, t_coda)
    denom = float(np.sum((t_base * deriv) ** 2))
    print("   noise (%)   recovered dv/v   bias (x1e-4)   1-sigma scatter (x1e-4)   predicted (x1e-4)")
    for level in (5.0, 10.0, 20.0, 50.0, 100.0):
        est = []
        for _ in range(60):
            noise = level / 100.0 * rms_c * RNG.standard_normal(t_coda.size)
            perturbed = np.interp(t_coda / (1.0 + dv_true), t_coda, base_clean) + noise
            est.append(stretch_estimate(perturbed, t_coda, base_clean))
        est = np.array(est)
        sigma_n = level / 100.0 * rms_c
        pred = sigma_n / np.sqrt(denom) / np.sqrt(t_coda.size / t_coda.size)
        pred = sigma_n / np.sqrt(denom)
        print(f"   {level:9.1f}   {est.mean():+.6f}   "
              f"{(est.mean() - dv_true) * 1e4:+13.2f}   {est.std(ddof=1) * 1e4:22.3f}   "
              f"{pred * 1e4:15.3f}")
    print("  (bias and scatter are quoted in units of 1e-4 of dv/v, i.e. 0.01 percentage")
    print("   points; the last column is the Cramer-Rao prediction")
    print("   sigma_eps = sigma_noise / sqrt(SUM (t g'(t))^2) evaluated on the clean coda.)")
    print("  The estimator is essentially unbiased.  Where the measured scatter is well")
    print("  above the 0.1 search-grid step (20% noise and above), it exceeds the")
    print("  prediction by a factor of about 1.9: the simple bound is optimistic because")
    print("  the estimator resamples by linear interpolation.  Both are far below the")
    print("  picking-based threshold of section 2.")

    print("\n  precision against coda length, 20% noise:")
    print("   coda length (s)   samples   1-sigma scatter (x1e-4)")
    for duration in (1.0, 2.0, 4.0, 8.0):
        n_c = int(1000.0 * duration)
        t_loc = np.linspace(0.0, duration, n_c)
        base_loc = coda_trace(t_loc, RNG)
        rms_loc = np.sqrt(np.mean(base_loc ** 2))
        est = []
        for _ in range(40):
            noise = 0.20 * rms_loc * RNG.standard_normal(n_c)
            perturbed = np.interp(t_loc / (1.0 + dv_true), t_loc, base_loc) + noise
            est.append(stretch_estimate(perturbed, t_loc, base_loc))
        print(f"   {duration:15.1f}   {n_c:8d}   {np.std(est, ddof=1) * 1e4:22.3f}")
    print("  (the fine search grid steps by 1e-5 in dv/v = 0.1 in these units, so")
    print("   entries below 0.1 are grid-limited rather than noise-limited.)")
    print("  A longer coda is a longer ruler: the precision improves with the scattered")
    print("  record length, which is why monitoring experiments use as much coda as")
    print("  the repeat time allows.")

    section("4. Environmental aliasing")
    dv_dT = -0.5            # m/s per K, teaching value
    v_ref = 400.0
    print(f"  teaching environmental sensitivity dv/dT = {dv_dT:.2f} m/s per K at "
          f"v = {v_ref:.0f} m/s")
    print("   temperature change (K)   dv/v (%)   equivalent travel-time change on a 20 m path (ms)")
    for dT in (1.0, 2.0, 5.0, 10.0):
        rel = dv_dT * dT / v_ref
        tt = 20.0 / v_ref
        print(f"   {dT:22.1f}   {rel * 100:8.3f}   {-rel * tt * 1e3:42.3f}")
    print("  A seasonal swing of a few kelvin therefore produces a dv/v of the same")
    print("  order as the changes a monitoring survey is usually looking for: the")
    print("  target and the weather are entangled unless a reference site or a")
    print("  temperature measurement is used to separate them.")

    section("5. The ambiguity: what coverage breaks and what it does not")
    v_layer = np.array([300.0, 400.0, 800.0])      # m/s, teaching layered model
    thick = np.array([2.0, 4.0, 10.0])             # m
    print("  teaching model (from the surface): " +
          ", ".join(f"{v:.0f} m/s over {h:.0f} m" for v, h in zip(v_layer, thick)))
    print("  hypotheses: A = every layer slows by the same fraction (a uniform change)")
    print("              B = only the top layer slows (a thaw or wetting front)")
    print("  the truth is B with a 5% slowdown of the top layer; the data are the")
    print("  per-path travel-time changes with a 0.5 ms picking error.")

    def signatures(paths_in_layer):
        p = np.asarray(paths_in_layer, dtype=float)
        t_base = p @ (thick / v_layer)
        return t_base, t_base.copy(), p[:, 0] * thick[0] / v_layer[0]

    path_sets = {
        "three deep paths (same depth range)": [[0.2, 1.0, 4.0], [0.3, 1.2, 5.0],
                                                [0.4, 1.4, 6.0]],
        "mixed depths (shallow, mid, deep)": [[2.0, 0.0, 0.0], [1.0, 1.0, 0.0],
                                              [0.5, 1.5, 1.0]],
    }
    sigma_t = 5e-4
    chi2_95 = 5.991          # 95% point of chi^2 with 2 degrees of freedom
    for name, paths in path_sets.items():
        t_base, sig_a, sig_b = signatures(paths)
        corr = float(np.corrcoef(sig_a, sig_b)[0, 1])
        n_trials = 300
        rejected = 0
        for _ in range(n_trials):
            data = 0.05 * sig_b + sigma_t * RNG.standard_normal(len(paths))
            scale = float(np.dot(sig_a, data) / np.dot(sig_a, sig_a))
            chi2 = float(np.sum(((data - scale * sig_a) / sigma_t) ** 2))
            rejected += int(chi2 > chi2_95)
        data_clean = 0.05 * sig_b
        scale0 = float(np.dot(sig_a, data_clean) / np.dot(sig_a, sig_a))
        chi2_clean = float(np.sum(((data_clean - scale0 * sig_a) / sigma_t) ** 2))
        print(f"\n  {name}")
        print(f"    baseline travel times (ms): "
              f"{', '.join(f'{x * 1e3:.3f}' for x in t_base)}")
        print(f"    correlation of the two signatures: {corr:+.4f}")
        print(f"    noiseless chi2 of hypothesis A against the truth B: {chi2_clean:8.2f}")
        print(f"    fraction of {n_trials} noisy trials rejecting A at 95%: "
              f"{rejected / n_trials * 100:5.1f}%")
    # how large a top-layer change would be needed for a decisive rejection?
    t_base, sig_a, sig_b = signatures(path_sets["mixed depths (shallow, mid, deep)"])
    data1 = sig_b
    s0 = float(np.dot(sig_a, data1) / np.dot(sig_a, sig_a))
    chi2_unit = float(np.sum(((data1 - s0 * sig_a) / sigma_t) ** 2))
    amp_needed = float(np.sqrt(chi2_95 / chi2_unit))
    print(f"\n  the noiseless chi2 of the wrong hypothesis grows as the square of the")
    print(f"  change amplitude, so a decisive rejection at 95% (chi2 > {chi2_95:.2f}) with")
    print(f"  a 0.5 ms picking error needs a top-layer change of {amp_needed * 100:.1f}%")
    print(f"  instead of the {5.0:.1f}% used here (the noiseless chi2 at unit")
    print(f"  amplitude is {chi2_unit:.0f}, and chi2 scales as the square of it).")
    print("  With paths confined to one depth range the two signatures are parallel, the")
    print("  wrong hypothesis absorbs the data by rescaling, and it is essentially never")
    print("  rejected: the rejection rate equals the false-positive rate.  With paths")
    print("  that sample different depths the signatures diverge and the rejection rate")
    print("  rises to 19% -- the wrong hypothesis becomes detectable, but the DECISION")
    print("  still needs the difference of the signatures to exceed the noise.  Coverage")
    print("  is what creates the possibility of separation; signal-to-noise decides it.")

    section("6. Summary")
    print("  Time-lapse interpretation rests on three numbers: the repeatability")
    print("  (NRMS), the change (dv/v or dsigma/sigma), and the ratio of the two.")
    print("  Coda stretching measures a velocity change an order of magnitude below")
    print("  the picking-based threshold because it uses the whole scattered record.")
    print("  Any environmental change that alters the near surface at the same time")
    print("  is indistinguishable from the target unless a reference or an")
    print("  independent measurement separates them, and a change that is uniform")
    print("  cannot be localised from travel times alone.")


if __name__ == "__main__":
    main()
