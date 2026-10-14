#!/usr/bin/env python3
"""The Moho as a receiver-function target: depth error from a wrong reference
slowness, the response to a finite-width transition, and how a multiple can
masquerade as real structure.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python moho_interface_demo.py

SYNTHETIC: the model numbers are chosen teaching values, not measurements of any
real crust.

Contents
--------
1. Depth as a function of the measured Ps delay, and its sensitivity to the
   reference ray parameter used for moveout correction.
2. Moveout-correction error: stacking with the wrong reference slowness smears
   the pulse; the stacked amplitude is measured against the error.
3. Transition width: conversion amplitude versus gradient thickness.
4. Multiple misidentification: moveout SIGN separates a primary from a multiple.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC model ---------------------------------------------------------
H_TRUE = 32.0        # km
VP, VS = 6.00, 3.50  # km/s
K = VP / VS
P_TRUE = 0.060       # s/km
F_DOM = 0.30         # Hz, dominant frequency of the receiver-function band


def q(v, p):
    """Vertical slowness sqrt(v^-2 - p^2); v in km/s, p in s/km -> s/km."""
    return np.sqrt(1.0 / v ** 2 - p ** 2)


def dt_ps(H, vp, vs, p):
    return H * (q(vs, p) - q(vp, p))


def main():
    print("=" * 70)
    print("1. Depth from the measured delay, and sensitivity to reference slowness")
    print("=" * 70)
    dt_true = dt_ps(H_TRUE, VP, VS, P_TRUE)
    print(f"SYNTHETIC truth: H = {H_TRUE:.1f} km, vp = {VP:.2f} km/s, "
          f"vs = {VS:.2f} km/s, k = {K:.3f}, p = {P_TRUE:.3f} s/km")
    print(f"  measured Ps delay = {dt_true:.4f} s")
    print("\n  If the analyst uses the WRONG reference slowness p_ref to remove the")
    print("  moveout but keeps the delay as if it were at p_ref:")
    print("   p_ref (s/km)  dt(p_ref)   H inferred   depth error")
    for pr in (0.050, 0.055, 0.060, 0.065, 0.070):
        dt_ref = dt_ps(H_TRUE, VP, VS, pr)
        H_inf = dt_ref / (q(VS, P_TRUE) - q(VP, P_TRUE))
        print(f"   {pr:9.3f}   {dt_ref:8.4f}   {H_inf:9.2f} km   "
              f"{H_inf - H_TRUE:+7.2f} km ({100 * (H_inf - H_TRUE) / H_TRUE:+.2f}%)")
    print("  A 0.010 s/km error (17%) in the reference slowness produces a ~ "
          f"{abs(dt_ps(H_TRUE,VP,VS,0.050) - dt_ps(H_TRUE,VP,VS,0.060)) / (q(VS,P_TRUE)-q(VP,P_TRUE)):.1f} km")
    print("  depth error here.  Note it is the DELAY that shifts, not the velocity.")

    print("\n" + "=" * 70)
    print("2. Moveout correction: a wrong reference shifts, a wrong velocity biases depth")
    print("=" * 70)
    ps = np.linspace(0.030, 0.090, 13)
    dt_at_p = np.array([dt_ps(H_TRUE, VP, VS, p) for p in ps])
    dt_s = 0.02
    tt = np.arange(-3.0, 3.0, dt_s)

    def pulse(t0):
        w = 1.0 / (np.pi * F_DOM)
        return np.exp(-0.5 * ((tt - t0) / w) ** 2)

    # (a) wrong reference slowness only: the whole stack just translates.
    shapes = []
    for pr in (0.045, 0.050, 0.055, 0.060, 0.065, 0.075):
        stack = np.sum([pulse(d - dt_ps(H_TRUE, VP, VS, pr)) for d in dt_at_p], axis=0)
        shapes.append((pr, stack.max(), tt[np.argmax(stack)]))
    print("  (a) wrong REFERENCE slowness p_ref (velocity model still correct):")
    print("      p_ref   stack peak   peak time (s)")
    for pr, mx, tmx in shapes:
        print(f"      {pr:.3f}   {mx / ps.size:10.4f}   {tmx:+.3f}")
    print("      The peak amplitude is IDENTICAL for every p_ref and the peak time")
    print("      translates by exactly dt(p_ref): a wrong reference is a constant")
    print("      depth bias, not a loss of resolution.")

    # (b) wrong model velocity: the correction is wrong in a p-dependent way.
    print("\n  (b) wrong model k = vp/vs used to compute the moveout.")
    print("      corrected time = dt_true(p) - dt_model(p) + dt_model(p_ref)")
    print("      so the stack peaks near  mean_p[dt_true - dt_model] + dt_model(p_ref).")
    print("      Analysing that peak with dt_model gives an INFERRED H.")
    f_pulse = 1.0                     # Hz, a typical high-frequency RF pulse
    tt2 = np.arange(-1.5, 1.5, 0.004)

    def pulse2(t0):
        w = 1.0 / (np.pi * f_pulse)
        return np.exp(-0.5 * ((tt2 - t0) / w) ** 2)

    pr = P_TRUE
    base = dt_ps(H_TRUE, VP, VS, pr) / (q(VS, pr) - q(VP, pr))   # = H_TRUE
    print("      k_try  vs (km/s)  mean res(s)  spread(s)  H_inf(km)  err(km)  peak%")
    for k_try in (1.55, 1.60, 1.65, K, 1.80, 1.90):
        vs_try = VP / k_try
        res = np.array([dt_ps(H_TRUE, VP, VS, p) - dt_ps(H_TRUE, VP, vs_try, p)
                        for p in ps])
        d_model_ref = q(vs_try, pr) - q(VP, pr)
        t_peak = res.mean() + H_TRUE * d_model_ref
        H_inf = t_peak / d_model_ref
        stack = np.sum([pulse2(r) for r in (res - res.mean())], axis=0)
        amp = stack.max() / ps.size * 100.0
        print(f"      {k_try:5.3f}  {vs_try:8.3f}  {res.mean():10.4f}  "
              f"{res.std():9.4f}  {H_inf:9.2f}  {H_inf - H_TRUE:+7.2f}  {amp:5.1f}")
    print(f"      Correct k = {K:.3f}: zero residual, H_inf = {base:.2f} km, peak = 100%.")
    print("      The dominant effect of a wrong velocity is a DEPTH BIAS (columns")
    print("      H_inf and err); the p-spread is small, so the stack peak stays high.")
    print("      Smearing matters when several layers' moveouts must be reconciled")
    print("      at once, not for a single converter.")

    print("\n" + "=" * 70)
    print("3. Transition width: conversion amplitude versus gradient thickness")
    print("=" * 70)
    print("  Model: the vertical velocity gradient is a boxcar of thickness w_z.")
    print("  The conversion amplitude is proportional to the gradient spectrum at")
    print("  the dominant frequency f = "
          f"{F_DOM:.2f} Hz (a CHOSEN band parameter).")
    print("  In time, the ramp spreads the delay by dtau = w_z * q_s;")
    print("  the amplitude factor is sinc(pi f dtau).")
    qs = q(VS, P_TRUE)
    print("   w_z (km)   dtau (s)   amplitude factor   interpreted as")
    for wz in (0.0, 0.5, 1.0, 2.0, 3.0, 5.0, 8.0):
        dtau = wz * qs
        # limit of sinc at 0 is 1
        arg = np.pi * F_DOM * dtau
        amp = 1.0 if arg == 0.0 else np.sin(arg) / arg
        print(f"   {wz:8.1f}   {dtau:8.3f}   {amp:16.4f}   "
              f"{'sharp' if amp > 0.8 else 'gradational' if amp > 0.4 else 'diffuse'}")
    half = np.pi / (2.0 * np.pi * F_DOM * qs)  # arg = pi/2 -> sinc = 0.637
    print(f"  amplitude = 0.637 (sinc half-width) at w_z = {half:.2f} km;")
    print("  below ~2 km the Moho reads as sharp, above ~6 km it reads as a")
    print("  broad gradient for this frequency.  This is a RESOLUTION statement,")
    print("  not a measurement of any real Moho.")

    print("\n" + "=" * 70)
    print("4. Primary versus multiple: the moveout sign is the diagnostic")
    print("=" * 70)
    p_grid = np.linspace(0.030, 0.080, 11)
    t_ps = np.array([dt_ps(H_TRUE, VP, VS, p) for p in p_grid])
    t_ppps = np.array([H_TRUE * (q(VS, p) + q(VP, p)) for p in p_grid])
    t_ppss = np.array([2.0 * H_TRUE * q(VS, p) for p in p_grid])
    for name, arr in (("Ps (primary)", t_ps), ("PpPs (multiple)", t_ppps),
                      ("PpSs+PsPs (multiple)", t_ppss)):
        slope = np.polyfit(p_grid ** 2, arr, 1)[0]
        print(f"  {name:22s}: d(dt)/d(p^2) = {slope:+8.1f} s per (s/km)^2")
    print("  The primary's delay INCREASES with p^2; the multiples' delays DECREASE.")
    print("  A peak that sharpens under the wrong moveout sign is a multiple, not")
    print("  a deeper converter.  Amplitude alone cannot make this distinction.")


if __name__ == "__main__":
    main()
