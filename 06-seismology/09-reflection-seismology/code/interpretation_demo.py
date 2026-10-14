#!/usr/bin/env python3
"""Interpretation of a synthetic reflection section: a fault, a channel-like
lens, an attribute for edge detection, a well tie, and the throw uncertainty set
by vertical resolution.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python interpretation_demo.py

SYNTHETIC.  The geology is invented; nothing here is a real seismic line or well.

Contents
--------
1. Build a 2-D layered reflectivity model with a normal fault and a lens.
2. Convolve with a wavelet to make a post-stack section (the convolutional model).
3. A coherency (semblance) attribute that highlights the fault.
4. A synthetic well tie: an impedance log, its synthetic seismogram, and a
   correlation with the section at the well location.
5. Fault throw measured from the seismic against the true throw, and the
   uncertainty imposed by the vertical resolution lambda/4.
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(t):
    print(f"\n{'=' * 68}\n{t}\n{'=' * 68}")


def ricker(t, f0):
    a = (np.pi * f0) ** 2
    return (1.0 - 2.0 * a * t ** 2) * np.exp(-a * t ** 2)


NX, NZ = 121, 400
DX, DZ = 25.0, 5.0
X = np.arange(NX) * DX
V = 3000.0
F0 = 30.0
XF = 1500.0            # fault location (m)
THROW_Z = 40.0         # true fault throw (m), a CHOSEN value


def reflectivity_model():
    """Return (R in time, marker time map) for the synthetic geology."""
    # Layer boundaries as depth functions; the fault offsets everything by
    # THROW_Z for x > XF.
    R = np.zeros((NX, NZ))
    markers = []
    for base_depth, contrast in ((500.0, 0.18), (800.0, -0.14),
                                 (1150.0, 0.10), (1500.0, -0.08)):
        zmap = np.full(NX, base_depth)
        zmap[X > XF] += THROW_Z
        markers.append(zmap.copy())
        for ix in range(NX):
            k = int(round(zmap[ix] / DZ))
            if 0 <= k < NZ:
                R[ix, k] += contrast
    # a lens (channel-like) between 1200 and 1320 m, 600-1000 m in x
    for ix in range(NX):
        if 600.0 <= X[ix] <= 1000.0:
            for k in range(int(1200 / DZ), int(1320 / DZ)):
                R[ix, k] += 0.05 * np.sin(np.pi * (k * DZ - 1200.0) / 120.0)
    return R, markers


def main():
    section("1. Synthetic reflectivity model")
    R, markers = reflectivity_model()
    print(f"  grid: {NX} traces x {NZ} depth samples, "
          f"dx = {DX:.0f} m, dz = {DZ:.0f} m")
    print(f"  constant v = {V:.0f} m/s assumed for time conversion")
    print(f"  normal fault at x = {XF:.0f} m with throw {THROW_Z:.0f} m "
          f"(SYNTHETIC)")
    print(f"  four marker horizons plus a 120 m lens between 600 and 1000 m")

    section("2. Post-stack section by convolution (the convolutional model)")
    dz_to_dt = 2.0 * DZ / V            # two-way time per depth sample
    dt = dz_to_dt
    wlen = 81
    tw = (np.arange(wlen) - wlen // 2) * dt
    w = ricker(tw, F0)
    sec = np.zeros_like(R)
    for ix in range(NX):
        sec[ix] = np.convolve(R[ix], w, mode="same")
    print(f"  wavelet: {F0:.0f} Hz Ricker, dt = {dt * 1e3:.3f} ms "
          f"(from dz and v)")
    print(f"  lambda = v/f = {V / F0:.0f} m; lambda/4 = {V / F0 / 4:.0f} m "
          f"(vertical resolution scale)")
    print(f"  section amplitude range: {sec.min():.3f} to {sec.max():.3f}")

    section("3. Coherency attribute: detecting the fault")
    def coherency(sec, half=2):
        C = np.zeros_like(sec)
        for ix in range(half, NX - half):
            win = sec[ix - half:ix + half + 1, :]
            num = (win.sum(axis=0)) ** 2
            den = win.shape[0] * (win ** 2).sum(axis=0)
            with np.errstate(invalid="ignore", divide="ignore"):
                C[ix] = np.where(den > 0, num / den, 1.0)
        return C

    C = coherency(sec)
    prof = np.mean(C, axis=1)                 # coherency averaged over depth
    half = 2
    valid = np.arange(half, NX - half)        # edges have no full window
    prof_v = prof[valid]
    imin = valid[int(np.argmin(prof_v))]
    near = np.abs(X[valid] - XF) <= 2 * DX
    far = np.abs(X[valid] - XF) > 8 * DX
    print("  coherency computed on a 5-trace window, then averaged over depth")
    print(f"  mean coherency near the fault (|x - {XF:.0f}| <= 50 m): "
          f"{prof_v[near].mean():.3f}")
    print(f"  mean coherency away from it  (|x - {XF:.0f}| > 200 m): "
          f"{prof_v[far].mean():.3f}")
    print(f"  minimum-coherency trace at x = {X[imin]:.0f} m "
          f"(true fault {XF:.0f} m)")
    print("  The fault is a lateral discontinuity, so a coherency/trace-similarity")
    print("  attribute localises it even where the reflector is not obvious.")

    section("4. Well tie")
    ixw = 20
    imp = np.cumsum(R[ixw]) * 0 + 1.0 + R[ixw]        # pseudo-impedance
    syn = np.convolve(R[ixw], w, mode="same")
    corr = np.corrcoef(syn, sec[ixw])[0, 1]
    print(f"  well inserted at trace x = {X[ixw]:.0f} m")
    print(f"  correlation between the synthetic trace built from the well")
    print(f"  reflectivity and the seismic trace at that location = {corr:.4f}")
    print("  A tie is a correlation, not a proof: a high correlation confirms")
    print("  consistency of the wavelet and the time-depth relation, and a low one")
    print("  sends you back to both.")

    section("5. Fault throw from the seismic, and its uncertainty")
    zt = 500.0                                    # marker used for the throw
    kt = int(round(zt / DZ))
    t_marker = 2.0 * zt / V
    print(f"  marker at {zt:.0f} m -> two-way time {t_marker * 1e3:.1f} ms")
    print(f"  vertical resolution scale lambda/4 = {V / F0 / 4:.0f} m "
          f"= {2 * (V / F0 / 4) / V * 1e3:.1f} ms two-way")
    print("  Add noise and re-pick the marker's time on either side of the fault:")
    lam4 = V / F0 / 4.0
    print("   noise rms   picked throw (m)   error (m)")
    for noise in (0.0, 0.02, 0.05, 0.10):
        picks = []
        for side in (-1, 1):
            ixs = X < XF if side < 0 else X > XF
            col = sec[ixs][:, kt - 20:kt + 20].mean(axis=0)
            col = col + noise * RNG.standard_normal(col.size)
            picks.append((np.argmax(np.abs(col)) - 20) * DZ)
        throw = abs(picks[1] - picks[0])
        print(f"   {noise:9.2f}   {throw:15.1f}   {throw - THROW_Z:+8.1f}")
    print(f"  true throw = {THROW_Z:.0f} m.  Even with no noise the picked throw")
    print("  is quantised by the depth sample; with noise it is uncertain by a")
    print("  sizeable fraction of lambda/4.  A throw of 40 m is about "
          f"{THROW_Z / lam4:.2f} x lambda/4, so it is resolvable but not")
    print("  precisely measurable from the seismic alone.")
    print("  INTERPRETATION RULE: quote a fault throw with the resolution scale")
    print("  and the picking uncertainty; a two-significant-figure throw without")
    print("  either is not a measurement.")


if __name__ == "__main__":
    main()
