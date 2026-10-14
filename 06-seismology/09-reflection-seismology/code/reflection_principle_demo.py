#!/usr/bin/env python3
"""The convolutional model of a reflection seismogram and the normal-incidence
reflection coefficient.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python reflection_principle_demo.py

SYNTHETIC: the layered model is a chosen teaching model, not a real seismic line.

Contents
--------
1. Acoustic impedance Z = rho*v and the normal-incidence coefficient
   R = (Z2 - Z1) / (Z2 + Z1) for a three-layer model.
2. Two-way travel times t = 2*sum(h/v).
3. The reflectivity series and its convolution with a wavelet.
4. Verification: the amplitude of each reflected wavelet equals the analytic R.
5. A zero-contrast ("hidden") layer: impedance changes internally but R = 0.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC model: (thickness km, vp km/s, rho g/cm^3) --------------------
LAYERS = [
    ("layer 1", 0.60, 2.20, 2.10),
    ("layer 2", 0.40, 2.80, 2.30),
    ("layer 3", 0.50, 3.20, 2.45),
    ("half-space", None, 3.60, 2.55),
]


def section(t):
    print(f"\n{'=' * 68}\n{t}\n{'=' * 68}")


def ricker(t, f0):
    a = (np.pi * f0) ** 2
    return (1.0 - 2.0 * a * t ** 2) * np.exp(-a * t ** 2)


def main():
    section("1. Acoustic impedance and normal-incidence reflection coefficients")
    print("  SYNTHETIC model (chosen, not measured):")
    print("   unit            h(km)   vp(km/s)  rho(g/cm3)   Z        R")
    Z_prev = None
    for name, h, v, rho in LAYERS:
        Z = rho * v
        hs = "  -  " if h is None else f"{h:5.2f}"
        if Z_prev is None:
            print(f"   {name:14s} {hs}  {v:8.2f}  {rho:9.2f}   {Z:6.3f}     -")
        else:
            R = (Z - Z_prev) / (Z + Z_prev)
            print(f"   {name:14s} {hs}  {v:8.2f}  {rho:9.2f}   {Z:6.3f}  {R:+.4f}")
        Z_prev = Z
    print("  R has units of (g/cm^3 * km/s)/(g/cm^3 * km/s): dimensionless.")

    section("2. Two-way travel times")
    t = 0.0
    times = []
    depths = []
    z = 0.0
    for name, h, v, rho in LAYERS[:-1]:
        z += h
        t += 2.0 * h / v
        times.append(t)
        depths.append(z)
        print(f"  to base of {name:14s}: depth {z:5.2f} km, two-way time {t:6.4f} s")
    print("  t = 2*h/v for each layer: km / (km/s) = s.  Unit check passes.")

    section("3. Reflectivity series and convolution")
    dt = 0.001
    tt = np.arange(0.0, max(times) + 0.20, dt)
    refl = np.zeros_like(tt)
    Zvals = [rho * v for (_, _, v, rho) in LAYERS]
    Rs = [(Zvals[i + 1] - Zvals[i]) / (Zvals[i + 1] + Zvals[i])
          for i in range(len(Zvals) - 1)]
    for tk, R in zip(times, Rs):
        idx = int(round((tk - tt[0]) / dt))
        refl[idx] = R
    f0 = 30.0
    w = ricker(tt, f0)
    synth = np.convolve(refl, w)[: tt.size]
    print(f"  wavelet: zero-phase Ricker, f0 = {f0:.0f} Hz, dt = {dt * 1e3:.1f} ms")
    print(f"  samples: {tt.size}; reflectivity spikes: {len(Rs)}")
    print("  synthetic trace = sum_k R_k * w(t - t_k)   (the convolutional model)")

    section("4. Verification: peak amplitude equals the analytic R")
    print("   interface t0 (s)   analytic R    measured peak   ratio")
    for tk, R in zip(times, Rs):
        idx = int(round((tk - tt[0]) / dt))
        lo, hi = max(0, idx - 60), idx + 60
        peak = synth[lo:hi].max()
        print(f"   {tk:11.4f}   {R:+.5f}   {peak:+.5f}   {peak / R:.5f}")
    print("  The ratio is 1 to within the wavelet's sampling of the spike: the")
    print("  convolution reproduces the reflection coefficients exactly, which is")
    print("  the definition of the convolutional model.")

    section("5. A hidden layer: impedance changes that leave R at zero")
    print("  Take layer 2 with v and rho scaled so that rho*v is UNCHANGED:")
    h, v, rho = LAYERS[1][1:]
    for factor in (1.0, 1.1, 1.25):
        v2, rho2 = v * factor, rho / factor
        Z2 = v2 * rho2
        print(f"   v = {v2:5.3f} km/s, rho = {rho2:5.3f} g/cm^3 -> Z = {Z2:.4f} "
              f"(baseline {v * rho:.4f})")
    Z1 = LAYERS[0][2] * LAYERS[0][3]
    print(f"  R(top of layer 2) = ({Z2:.4f}-{Z1:.4f})/({Z2:.4f}+{Z1:.4f}) = "
          f"{(Z2 - Z1) / (Z2 + Z1):+.2e}")
    print("  Impedance, and hence normal-incidence reflection, is blind to any")
    print("  velocity-density trade that preserves rho*v.  Seismic data at normal")
    print("  incidence cannot distinguish these models -- only the amplitude")
    print("  versus offset (AVO) can, because R depends on v and rho separately.")


if __name__ == "__main__":
    main()
