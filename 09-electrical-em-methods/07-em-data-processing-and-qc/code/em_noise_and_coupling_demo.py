#!/usr/bin/env python3
"""EM noise, coupling and cultural effects: what averages down, what does not,
and what the survivor does to an interpreted model.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python em_noise_and_coupling_demo.py

EVERYTHING IS SYNTHETIC.  The two-layer model is an exact image-series teaching
model, and the noise amplitudes are chosen values, not measurements.  No
instrument, site or published figure is referenced.

Contents
--------
1. Exact forward model for a Wenner sounding over a two-layer earth, with both
   asymptotic limits checked.
2. A noise budget: incoherent noise, a coherent powerline line, cultural spikes.
3. Stacking: measured reduction versus the number of repeats.  Incoherent noise
   falls as 1/sqrt(N); a phase-locked line does not fall at all.
4. Robust stacking under spikes: mean versus median versus trimmed mean.
5. Coupling: a phase-locked line is mathematically inseparable from the signal
   over repeats; a drifting phase is separable.  Measured both ways.
6. Consequence: the coherent survivor lands in an interpreted model as a
   systematic error, at a level the incoherent error does not explain.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC two-layer model ---------------------------------------------
RHO1 = 25.0        # ohm m, top layer
RHO2 = 500.0       # ohm m, half-space
H_LAYER = 8.0      # m, thickness of the top layer
NTERMS = 400       # terms kept in the image series
SPACINGS = np.array([1.0, 1.8, 3.2, 5.6, 10.0, 18.0, 32.0, 56.0])   # m
F_LINE = 50.0      # Hz
PHASE_LOCKED = 0.7  # rad, chosen phase of the coherent line


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def rho_a_two_layer(a, rho1=RHO1, rho2=RHO2, H=H_LAYER, nterms=NTERMS):
    """Exact Wenner apparent resistivity over a two-layer earth (image series).

        rho_a = rho1 [1 + 4a sum_n k^n ( 1/sqrt(a^2+(2nH)^2)
                                        - 1/sqrt(4a^2+(2nH)^2) ) ]
    with k = (rho2 - rho1)/(rho2 + rho1).  Limits: a -> 0 gives rho1 and
    a -> infinity gives rho2 (checked in section 1).
    """
    a = np.atleast_1d(np.asarray(a, float))
    k = (rho2 - rho1) / (rho2 + rho1)
    n = np.arange(1, nterms + 1)
    kn = k ** n
    term = kn[None, :] * (1.0 / np.sqrt(a[:, None] ** 2 + (2.0 * n[None, :] * H) ** 2)
                          - 1.0 / np.sqrt(4.0 * a[:, None] ** 2
                                          + (2.0 * n[None, :] * H) ** 2))
    return rho1 * (1.0 + 4.0 * a * term.sum(axis=1))


def two_layer_misfit(data, sig, rho1_fixed, rho2_grid, H_grid):
    """Least-squares misfit over a (rho2, H) grid with rho1 and sigma fixed."""
    chi2 = np.empty((len(rho2_grid), len(H_grid)))
    for i, rho2 in enumerate(rho2_grid):
        for j, H in enumerate(H_grid):
            pred = rho_a_two_layer(SPACINGS, rho1_fixed, rho2, H)
            chi2[i, j] = np.sum(((data - pred) / sig) ** 2)
    return chi2


def main():
    section("1. Exact forward model and its asymptotic limits")
    print("Wenner array, spacing a, over a two-layer earth.  The potential of a")
    print("point source at the surface is the image series")
    print("    Phi(r) = (I rho1 / 2 pi)[ 1/r + 2 sum_n k^n / sqrt(r^2+(2nH)^2) ],")
    print("which gives the apparent resistivity used throughout this module.")
    print(f"SYNTHETIC model: rho1 = {RHO1:.1f} ohm m, rho2 = {RHO2:.1f} ohm m, "
          f"H = {H_LAYER:.1f} m")
    print(f"reflection coefficient k = {(RHO2 - RHO1) / (RHO2 + RHO1):.4f}")
    print("\n   a (m)     rho_a (ohm m)")
    for a in (0.05, 0.5, 1.0, 4.0, 10.0, 40.0, 200.0):
        print(f"  {a:6.2f}   {rho_a_two_layer(a)[0]:10.4f}")
    print(f"limit a -> 0  : {rho_a_two_layer(1e-3)[0]:.6f} ohm m "
          f"(rho1 = {RHO1:.1f})")
    print(f"limit a -> inf: {rho_a_two_layer(1e5, nterms=200000)[0]:.6f} ohm m "
          f"(rho2 = {RHO2:.1f})")
    d_clean = rho_a_two_layer(SPACINGS)
    print("\nSYNTHETIC noise-free data at the eight Wenner spacings used below:")
    for a, d in zip(SPACINGS, d_clean):
        print(f"   a = {a:5.1f} m:  rho_a = {d:9.4f} ohm m")

    section("2. Noise budget")
    print("Noise is added to the measured potential difference, so the error in")
    print("rho_a grows with spacing through the geometric factor K = 2 pi a.")
    sig_V = 0.01 * d_clean[0] / (2.0 * np.pi * SPACINGS[0])   # 1% at smallest a
    sig_rhoa = 2.0 * np.pi * SPACINGS * sig_V
    print(f"constant potential noise sigma_V = {sig_V:.4e} (arbitrary volt units)")
    print("\n   a (m)   sigma_rhoa (ohm m)   relative error (%)")
    for a, s, d in zip(SPACINGS, sig_rhoa, d_clean):
        print(f"  {a:6.1f}   {s:16.5f}   {100.0 * s / d:18.2f}")
    amp_V_line = 2.5 * sig_V                       # coherent line, in volts
    line_rhoa = 2.0 * np.pi * SPACINGS * amp_V_line
    print(f"\ncoherent powerline line: {amp_V_line / sig_V:.1f} x the potential "
          f"noise, i.e.")
    for a, el, d in zip(SPACINGS, line_rhoa, d_clean):
        print(f"   a = {a:5.1f} m: line amplitude {el:8.4f} ohm m "
              f"({100 * el / d:5.2f}% of the datum)")
    p_spike = 0.02
    spike_size = 15.0
    print(f"cultural spikes: {100 * p_spike:.0f}% of repeats carry a spike of "
          f"{spike_size:.0f} sigma")

    def realisation(n, coherent="none", phase=None, spikes=True, rng=RNG):
        white = sig_rhoa[None, :] * rng.standard_normal((n, len(SPACINGS)))
        if coherent == "none":
            line = 0.0
        elif coherent == "locked":
            line = np.sin(np.full(n, PHASE_LOCKED))[:, None] * line_rhoa[None, :]
        else:                                             # drifting phase
            line = np.sin(phase[:, None]) * line_rhoa[None, :]
        sp = np.zeros_like(white)
        if spikes:
            hit = rng.random(n) < p_spike
            sp[hit, :] = spike_size * sig_rhoa[None, :] * rng.standard_normal(
                (int(hit.sum()), len(SPACINGS)))
        return d_clean[None, :] + white + line + sp

    section("3. Stacking: what averages down and what does not")
    print("Root-mean-square error of the stacked estimate at the widest spacing,")
    print("300 independent experiments, no spikes:")
    print("\n     N   incoherent   line locked   line drifting  1/sqrt(N) x sigma")
    trials = 300
    for N in (1, 4, 16, 64, 256):
        cols = {"white": [], "locked": [], "drift": []}
        for _ in range(trials):
            a0 = realisation(N, "none", spikes=False)
            a1 = realisation(N, "locked", spikes=False)
            a2 = realisation(N, "drift", 0.35 * np.arange(N), spikes=False)
            cols["white"].append(a0[:, -1].mean() - d_clean[-1])
            cols["locked"].append(a1[:, -1].mean() - d_clean[-1])
            cols["drift"].append(a2[:, -1].mean() - d_clean[-1])
        e = {k: np.sqrt(np.mean(np.square(v))) for k, v in cols.items()}
        print(f"  {N:5d}   {e['white']:9.4f}   {e['locked']:11.4f}   "
              f"{e['drift']:13.4f}   {sig_rhoa[-1] / np.sqrt(N):14.4f}")
    print("The incoherent error follows 1/sqrt(N) (columns 2 and 5 match).")
    print("The phase-locked line does not fall at all: to the stack it is signal.")
    print("A drifting phase recovers the 1/sqrt(N) behaviour, because the line")
    print("starts to cancel between repeats.")

    section("4. Robust stacking under cultural spikes")
    print(f"{100 * p_spike:.0f}% of repeats carry a spike of {spike_size:.0f} "
          f"sigma; N = 64, 300 experiments, widest spacing, no coherent line:")
    res = {"mean": [], "median": [], "trimmed": []}
    for _ in range(trials):
        col = realisation(64, "none")[:, -1]        # incoherent noise + spikes
        srt = np.sort(col)
        res["mean"].append(col.mean() - d_clean[-1])
        res["median"].append(np.median(col) - d_clean[-1])
        res["trimmed"].append(srt[10:54].mean() - d_clean[-1])
    for key, vals in res.items():
        v = np.array(vals)
        print(f"   {key:8s}: bias {v.mean():+9.5f}, rms error "
              f"{np.sqrt((v ** 2).mean()):9.5f} ohm m")
    print("The mean is dragged by the few large values; the median is not.  The")
    print("price is efficiency: for pure Gaussian noise the median is the slower")
    print("estimator, so the choice is a statement about the noise, not a taste.")

    section("5. Coupling: can a repeat-axis filter remove the line?")
    N = 64
    for label, ph in (("phase locked (constant)", np.full(N, PHASE_LOCKED)),
                      ("drifting (0.35 rad/repeat)", 0.35 * np.arange(N))):
        A = np.column_stack([np.cos(ph), np.sin(ph), np.ones(N)])
        sv = np.linalg.svd(A, compute_uv=False)
        print(f"\n{label}: design matrix [cos, sin, 1] over {N} repeats")
        print("   singular values: " + ", ".join(f"{s:.4f}" for s in sv))
        print(f"   condition number = {sv[0] / sv[-1]:.3e}")
        err_before, err_after = [], []
        for _ in range(trials):
            if label.startswith("phase"):
                col = realisation(N, "locked")[:, -1]
            else:
                col = realisation(N, "drift", ph)[:, -1]
            coef, *_ = np.linalg.lstsq(A, col, rcond=None)
            err_before.append(col.mean() - d_clean[-1])
            err_after.append(coef[2] - d_clean[-1])
        print(f"   rms error, plain average = "
              f"{np.sqrt(np.mean(np.square(err_before))):9.4f} ohm m")
        print(f"   rms error, notched       = "
              f"{np.sqrt(np.mean(np.square(err_after))):9.4f} ohm m")
    print("\nWhen the phase is identical in every repeat the three columns of the")
    print("design matrix are the same column: rank 1, and the line is EXACTLY")
    print("degenerate with the DC level.  No arithmetic can separate them; the fix")
    print("has to be physical (a repeat interval that is not a whole number of")
    print("line periods), which is what the drifting case represents.")

    section("6. Consequence: the survivor lands in the interpreted model")
    rho2_grid = np.linspace(150.0, 1200.0, 211)
    H_grid = np.linspace(1.0, 14.0, 261)
    chi = two_layer_misfit(d_clean, sig_rhoa[0], RHO1, rho2_grid, H_grid)
    i, j = np.unravel_index(np.argmin(chi), chi.shape)
    print(f"inverting the noise-free data (rho1 fixed at {RHO1:.1f} ohm m):")
    print(f"   rho2 = {rho2_grid[i]:.1f} ohm m (true {RHO2:.1f}), "
          f"H = {H_grid[j]:.2f} m (true {H_LAYER:.1f})")
    print("\nstack 64 repeats that contain the phase-locked line, then invert:")
    for _ in range(3):
        d_obs = realisation(64, "locked")[:, :].mean(axis=0)
        c = two_layer_misfit(d_obs, sig_rhoa[0], RHO1, rho2_grid, H_grid)
        i2, j2 = np.unravel_index(np.argmin(c), c.shape)
        print(f"   rho2 = {rho2_grid[i2]:7.1f} ohm m "
              f"({100 * (rho2_grid[i2] - RHO2) / RHO2:+6.1f}%), "
              f"H = {H_grid[j2]:6.2f} m ({H_grid[j2] - H_LAYER:+.2f} m)")
    print("\nNow with the line drifting between repeats and the same noise level:")
    for _ in range(3):
        d_obs = realisation(64, "drift", 0.35 * np.arange(64))[:, :].mean(axis=0)
        c = two_layer_misfit(d_obs, sig_rhoa[0], RHO1, rho2_grid, H_grid)
        i2, j2 = np.unravel_index(np.argmin(c), c.shape)
        print(f"   rho2 = {rho2_grid[i2]:7.1f} ohm m "
              f"({100 * (rho2_grid[i2] - RHO2) / RHO2:+6.1f}%), "
              f"H = {H_grid[j2]:6.2f} m ({H_grid[j2] - H_LAYER:+.2f} m)")
    print("The incoherent part of the error shrinks as 1/sqrt(N) and appears as")
    print("scatter; the coherent part does not shrink and appears as bias.")


if __name__ == "__main__":
    main()
