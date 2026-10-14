#!/usr/bin/env python3
"""Multichannel (array) filtering in the f-k domain: separate two linear events
that overlap in time by their apparent slowness, MEASURE how much of the wanted
event is retained and how much of the unwanted event leaks through, and show how
spatial aliasing lets a steep event masquerade as the signal dip.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python multichannel_filtering_demo.py

Everything is SYNTHETIC.  The array geometry is a chosen teaching geometry.

Contents
--------
1. Build a synthetic shot gather: a signal event and a slower, opposite-dip noise event.
2. The 2-D spectrum: each linear event is a line k = -f p through the origin.
3. Design a dip (fan) filter from the measured slowness.
4. Measure retention of the signal and leakage of the noise versus fan width.
5. Spatial aliasing: a steep event can fold onto the signal dip.
"""

import numpy as np
from scipy import signal

RNG = np.random.default_rng(20261014)

NT = 256          # time samples per trace
NX = 64           # traces
DT = 0.004        # s
DX = 25.0         # m


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def ricker(t, f0):
    a = (np.pi * f0) ** 2
    return (1.0 - 2.0 * a * t ** 2) * np.exp(-a * t ** 2)


def event(p_samples, t0_samples, f0):
    """A linear event with p (samples/trace) dip, t0 on trace 0."""
    t = np.arange(NT) * DT
    g = np.zeros((NT, NX))
    for m in range(NX):
        g[:, m] = ricker(t - ((t0_samples + p_samples * m) * DT), f0)
    return g


def tone_event(f_hz, p_samples):
    """A continuous sinusoid with dip p (samples/trace) -- a single f-k line."""
    t = np.arange(NT) * DT
    g = np.zeros((NT, NX))
    for m in range(NX):
        g[:, m] = np.cos(2.0 * np.pi * f_hz * (t - p_samples * m * DT))
    return g


def fk_mask(shape, p_sig, half_width):
    """Raised-cosine fan keeping slowness near p_sig (samples/trace).

    An event t = t0 + p m localises on k = -f p, with f in cycles/sample and k in
    cycles/trace, so the fan is centred on k = -f p_sig.
    """
    nt, nx = shape
    f = np.fft.fftfreq(nt)[:, None]
    k = np.fft.fftfreq(nx)[None, :]
    dist = np.abs(k + f * p_sig)
    taper = 0.5 * half_width
    return np.where(
        dist <= half_width, 1.0,
        np.where(dist >= half_width + taper, 0.0,
                 0.5 * (1.0 + np.cos(np.pi * (dist - half_width) / taper))))


def fk_filter(g, p_sig, half_width):
    G = np.fft.fft2(g)
    return np.real(np.fft.ifft2(G * fk_mask(g.shape, p_sig, half_width)))


def peak(g):
    return np.abs(g).max()


def energy(g):
    """RMS amplitude of the gather: a stable scalar measure of retained energy."""
    return np.linalg.norm(g) / np.sqrt(g.size)


def main():
    section("1. Synthetic shot gather")
    print(f"  {NX} traces, {NT} samples, dt = {DT * 1000:.0f} ms, dx = {DX:.0f} m")
    print(f"  signal event dip p_sig = +2 samples/trace "
          f"(= {2 * DT * 1000 / DX:.3f} ms/m, apparent velocity {DX / (2 * DT):.0f} m/s)")
    print(f"  noise  event dip p_noise = -4 samples/trace "
          f"(opposite dip, apparent velocity {abs(DX / (-4 * DT)):.0f} m/s)")
    g_sig = event(2.0, 40.0, 30.0)
    g_noi = event(-4.0, 120.0, 30.0)
    g_all = g_sig + g_noi
    print(f"  peak signal amplitude = {peak(g_sig):.3f}, "
          f"peak noise amplitude = {peak(g_noi):.3f}")

    section("2. The 2-D spectrum is a set of lines through the origin")
    G = np.fft.fft2(g_all)
    f = np.fft.fftfreq(NT)
    kk = np.fft.fftfreq(NX)
    print("  For a linear event the energy lies on k = -f p.  Measured locus of the")
    print("  largest spectral peak per frequency, and the dip it implies:")
    print("     f (cyc/sample)   argmax |G| k (cyc/trace)   implied p (samples/trace)")
    for fv in (0.05, 0.08, 0.10, 0.12):
        i = int(np.argmin(np.abs(f - fv)))
        j = int(np.argmax(np.abs(G[i, :NX // 2])))
        print(f"     {f[i]:15.3f}   {kk[j]:23.4f}   {-kk[j] / f[i]:20.3f}")
    print("  The steep noise event (-4) dominates the spectrum; the signal event")
    print("  (+2) sits on the other side of the origin and is weaker.")

    section("3. Fan filter designed for the signal dip")
    print("  grid spacing in k is 1/NX = "
          f"{1.0 / NX:.4f} cyc/trace, so the half-width below spans grid cells.")
    print("  retention/leakage are RMS-amplitude ratios of the filtered gather to")
    print("  the input gather, each event filtered on its own.")
    print("   half-width (cyc/trace)   cells   signal retained   noise leaked   rejection (dB)")
    for hw in (0.008, 0.016, 0.023, 0.031, 0.047, 0.0625):
        ret = energy(fk_filter(g_sig, 2.0, hw)) / energy(g_sig)
        rej = energy(fk_filter(g_noi, 2.0, hw)) / energy(g_noi)
        print(f"   {hw:22.4f}   {hw * NX:5.1f}   {ret * 100:14.1f}%   "
              f"{rej * 100:12.2f}%   {20 * np.log10(max(rej, 1e-12)):13.1f}")
    print("  A wider fan keeps more of the finite-aperture signal event but lets more")
    print("  of the noise event through: resolution against contamination, in the")
    print("  wavenumber domain rather than the frequency domain.")

    section("4. Applied to the summed gather")
    hw = 0.023
    filt = fk_filter(g_all, 2.0, hw)
    resid = filt - g_sig
    print(f"  fan half-width = {hw:.3f} cyc/trace")
    print(f"  retained RMS of the filtered gather: {energy(filt):.4f} "
          f"(ideal signal event {energy(g_sig):.4f})")
    print(f"  residual RMS / noise-event RMS = {energy(resid) / energy(g_noi):.3f}")
    print("  Residual energy is the part of the noise event that leaked through plus")
    print("  transform edge effects: the gather is not periodic in space, so a 2-D")
    print("  FFT filter always creates a boundary artefact.")

    section("5. Spatial aliasing: a steep event can fold onto the signal dip")
    print("  Spatial Nyquist: |k| <= 0.5 cyc/trace.  An event with dip p is aliased")
    print("  for f > 0.5/|p|; its true wavenumber k = -f p wraps modulo 1 into the")
    print("  visible range and the event appears at a different (aliased) dip.")
    f_tone = 40.0
    fv = f_tone * DT                          # cyc/sample
    print(f"  a continuous {f_tone:.0f} Hz event therefore has f = {fv:.3f} cyc/sample")
    print("     p (samples/trace)   true k   aliased k   aliased p   retained by +2 fan")
    for p_test in (2.0, 5.0, 8.25, 12.0):
        gg = tone_event(f_tone, p_test)
        true_k = -fv * p_test
        alias_k = ((true_k + 0.5) % 1.0) - 0.5
        ret = energy(fk_filter(gg, 2.0, hw)) / energy(gg)
        print(f"   {p_test:18.2f}   {true_k:8.3f}   {alias_k:10.3f}   "
              f"{-alias_k / fv:10.3f}   {ret * 100:19.1f}%")
    print("  p = 8.25 samples/trace is beyond the spatial Nyquist, but it aliases to")
    print("  an apparent dip of exactly +2 -- the signal dip -- so it passes the fan.")
    print("  Array filtering is only as good as the spatial sampling that supports it.")


if __name__ == "__main__":
    main()
