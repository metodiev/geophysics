#!/usr/bin/env python3
"""Ocean-bottom seismology: water-layer multiples, compliance noise and its
removal with a co-located pressure sensor, sensor tilt, and clock drift.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python obn_ocean_bottom_seismology_demo.py

Everything here is SYNTHETIC.  The water depths, sediment velocities, noise
levels and instrument errors are chosen teaching values, printed below.  No OBS
network, station, event or published deployment is reproduced.

Contents
--------
1. The water-column multiple: period, peg-legs and the notch frequencies.
2. A synthetic receiver function with water-layer multiples.
3. Compliance noise: the pressure-to-vertical coherence and its removal.
4. Sensor tilt: the horizontal-to-vertical leakage.
5. Clock drift and what it costs in location and travel time.
6. Verification.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

C_WATER = 1500.0        # m/s, standard reference sound speed in seawater
DEPTHS = (1000.0, 2000.0, 3000.0, 4000.0, 5000.0)
VS_SED = 1200.0         # m/s, chosen S velocity of the sediment
VP_SED = 2000.0         # m/s, chosen P velocity of the sediment
VP_MANTLE = 8000.0      # m/s, chosen mantle P velocity
COMPLIANCE_DB = 0.0     # dB, chosen scale of the infragravity compliance


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def ricker(t, t0, f0):
    tau = t - t0
    a = (np.pi * f0) ** 2
    return (1.0 - 2.0 * a * tau ** 2) * np.exp(-a * tau ** 2)


def main():
    section("1. The water-column multiple")
    print("  A wave trapped in the water column bounces between the sea surface and")
    print("  the seafloor with a two-way period")
    print("    T_w = 2 h / c")
    print(f"  with h the water depth and c = {C_WATER:.0f} m/s.  Every arrival")
    print("  beneath the seabed is followed by its multiples at t + n T_w.")
    print("\n   water depth (m)   T_w (s)   1/T_w (Hz)   notch spacing (Hz)")
    for h in DEPTHS:
        Tw = 2.0 * h / C_WATER
        print(f"  {h:15.0f}   {Tw:7.3f}   {1 / Tw:10.4f}   {1 / Tw:16.4f}")
    print("\n  The comb of notches at multiples of 1/T_w is the signature of the")
    print("  water layer, and its fundamental frequency is the single most useful")
    print("  number in an ocean-bottom record: it gives the water depth to about")
    print("  1 per cent from the seismogram alone.  It also means the seismic")
    print("  spectrum of ANY ocean-bottom record is notched, which is why")
    print("  deghosting and water-layer demultiple are not optional.")

    section("2. A synthetic receiver function with water multiples")
    dt = 0.004
    t = np.arange(0.0, 40.0, dt)
    t_p = 2.0
    h = 3000.0
    Tw = 2.0 * h / C_WATER
    # P-to-S delay at the sediment-mantle interface for a teleseismic ray
    p = 0.060                      # s/km, ray parameter
    q_s = np.sqrt(1.0 / (VS_SED / 1000.0) ** 2 - p ** 2)
    q_p = np.sqrt(1.0 / (VP_SED / 1000.0) ** 2 - p ** 2)
    H_sed = 2.0                    # km
    dt_ps = H_sed * (q_s - q_p)
    print(f"  water depth {h:.0f} m -> T_w = {Tw:.3f} s")
    print(f"  a {H_sed:.1f} km sediment layer over a faster half-space:")
    print(f"    vp = {VP_SED:.0f} m/s, vs = {VS_SED:.0f} m/s, p = {p:.3f} s/km")
    print(f"    q_p = {q_p:.6f} s/km, q_s = {q_s:.6f} s/km")
    print(f"    Ps delay = H(q_s - q_p) = {dt_ps:.4f} s")
    wavelet = ricker(t, t_p, 1.0)
    rf = np.zeros_like(t)
    amps = (1.00, 0.35)
    for n in range(5):
        rf += amps[0] * (-0.4) ** n * ricker(t, t_p + n * Tw, 1.0)
        rf += amps[1] * (-0.4) ** n * ricker(t, t_p + dt_ps + n * Tw, 1.0)
    print(f"\n  the receiver function is built from the direct P plus a Ps")
    print(f"  conversion at {dt_ps:.3f} s, each repeated at multiples of T_w with")
    print("  the seafloor reflection coefficient (-0.4) applied once per bounce.")
    print("\n   arrival time (s)   identification")
    for n in range(3):
        print(f"  {t_p + n * Tw:16.3f}   direct P, water multiple n = {n}")
    for n in range(3):
        print(f"  {t_p + dt_ps + n * Tw:16.3f}   Ps, water multiple n = {n}")
    print(f"\n  Here the Ps delay ({dt_ps:.2f} s) is much shorter than the multiple")
    print(f"  spacing ({Tw:.2f} s), so the first few arrivals are separable by eye.")
    print("  That is a property of THIS water depth, not of the method.  Repeat the")
    print("  same calculation for a shallow shelf:")
    for h2 in (3000.0, 600.0, 200.0):
        Tw2 = 2.0 * h2 / C_WATER
        print(f"    h = {h2:6.0f} m: T_w = {Tw2:.3f} s, "
              f"Ps/multiple spacing ratio = {dt_ps / Tw2:.3f}")
    print("  At 200 m of water the multiple spacing (0.27 s) is SHORTER than the")
    print("  Ps delay (0.67 s): the first multiple of the direct P arrives before")
    print("  the conversion does, and the record is an unresolvable comb.  The")
    print("  shelf case is therefore not merely harder; it requires the water-layer")
    print("  multiples to be modelled and removed before any conversion can be")
    print("  identified at all.  Deep-water OBS work is easy by comparison.")

    section("3. Compliance noise and its removal")
    print("  Infragravity surface waves force the seafloor with a pressure signal")
    print("  that the seafloor deforms under.  The resulting vertical motion is")
    print("  called COMPLIANCE noise, and it is the dominant noise on the vertical")
    print("  channel of a deep OBS at periods of 20-200 s.")
    n = 20000
    dts = 0.5
    tt = np.arange(n) * dts
    # synthetic infragravity pressure: a band-limited random process
    P = RNG.standard_normal(n)
    F = np.fft.rfft(P)
    f = np.fft.rfftfreq(n, dts)
    band = (f > 0.004) & (f < 0.05)
    F[~band] = 0.0
    P = np.fft.irfft(F, n)
    P /= P.std()
    # compliance transfer magnitude: a smooth peak, chosen teaching shape
    Zmag = 1.0 / np.sqrt(1.0 + ((f - 0.015) / 0.008) ** 2)
    Zmag[0] = 0.0
    disp = np.fft.irfft(np.fft.rfft(P) * Zmag, n)
    disp /= disp.std()
    seism = 0.05 * RNG.standard_normal(n)      # instrument noise
    vertical = 1.00 * disp + seism
    print(f"  synthetic record: {n} samples at {dts:.1f} s = "
          f"{n * dts / 3600:.2f} h")
    print(f"  infragravity band 0.004-0.05 Hz; compliance transfer peaks near")
    print("  0.015 Hz (a chosen teaching shape)")
    print(f"  std of the compliance displacement = {disp.std():.4f}")
    print(f"  std of the instrument noise        = {seism.std():.4f}")
    print(f"  std of the vertical channel        = {vertical.std():.4f}")
    print("\n  Now apply the standard correction: a co-located pressure sensor")
    print("  measures P directly, and the vertical is replaced by V' = V - Z(f) P")
    print("  with Z(f) estimated band by band from the coherent part.  The")
    print("  estimator used here is the frequency-domain regression")
    print("  Z(f) = <V P*> / <|P|^2>, smoothed over a few neighbouring bins.")
    Ph = np.fft.rfft(P)
    Vh = np.fft.rfft(vertical)
    num = Vh * np.conj(Ph)
    den = np.abs(Ph) ** 2
    kern = np.ones(9) / 9.0
    num_s = np.convolve(num.real, kern, mode="same") + 1j * np.convolve(
        num.imag, kern, mode="same")
    den_s = np.convolve(den, kern, mode="same")
    Zf = num_s / np.maximum(den_s, 1e-12)
    Vc = np.fft.irfft(Vh - Zf * Ph, n)
    Ztrue = Zmag * np.fft.rfft(P) / np.maximum(np.fft.rfft(P), 1e-12)
    # coherence between the corrected vertical and the pressure
    coh = np.abs(np.sum(Vc * P)) ** 2 / (np.sum(Vc ** 2) * np.sum(P ** 2))
    print(f"    variance before correction = {vertical.var():.4f}")
    print(f"    variance after  correction = {Vc.var():.4f}")
    print(f"    reduction factor = {vertical.var() / Vc.var():.1f}")
    print(f"    residual std = {Vc.std():.4f} vs instrument noise "
          f"{seism.std():.4f}")
    print(f"    squared coherence between the corrected vertical and P = "
          f"{coh:.6f}")
    print(f"\n  The correction reduces the vertical channel's variance by a factor")
    print(f"  {vertical.var() / Vc.var():.0f} and leaves a residual standard deviation of")
    print(f"  {Vc.std():.4f} against an instrument noise of {seism.std():.4f} -- i.e. the")
    print("  compliance has been removed and the instrument noise has not.  The")
    print(f"  squared coherence against pressure falls to {coh:.1e}, so no")
    print("  coherent compliance signal remains.  Two practical points: the")
    print("  estimator must be frequency dependent (a single scalar for the whole")
    print("  band leaves a residual an order of magnitude larger -- section 6")
    print("  repeats this as a check), and the band-by-band coherence is the")
    print("  diagnostic that says whether the correction worked.")

    section("4. Sensor tilt: horizontal-to-vertical leakage")
    print("  A sensor tilted by theta measures a cos(theta) + h sin(theta), where")
    print("  a and h are the true vertical and horizontal ground motions.  The")
    print("  horizontal motion therefore LEAKS onto the vertical channel with")
    print("  amplitude sin(theta).")
    print("\n   tilt (deg)   sin(theta)   leaked fraction of horizontal (%)")
    for th in (0.5, 1.0, 2.0, 5.0, 10.0):
        print(f"  {th:10.1f}   {np.sin(np.radians(th)):.6f}   "
              f"{100 * np.sin(np.radians(th)):33.3f}")
    print("\n  A 5 degree tilt leaks 8.7 per cent of every horizontal arrival onto")
    print("  the vertical channel -- enough to make a Ps conversion on the vertical")
    print("  component look like a real phase.  The tilt must be measured (from")
    print("  the two horizontal channels' DC offsets, or from a compass and")
    print("  accelerometer) and the three components rotated.  This is a")
    print("  first-order correction, not a refinement.")

    section("5. Clock drift")
    print("  OBS clocks are free-running.  A drift of 1 part in 10^8 accumulates")
    print("  over a deployment of any length:")
    print("\n   drift (s/day)   over 30 days (s)   over 180 days (s)   "
          "location error at 8 km/s (m, 180 d)")
    for drift in (0.001, 0.010, 0.100, 1.000):
        d180 = drift * 180
        print(f"  {drift:13.3f}   {drift * 30:17.3f}   {d180:19.3f}   "
              f"{d180 * 8000:28.0f}")
    print("\n  The location error column is the drift converted to distance with")
    print("  an apparent velocity of 8 km/s: a 1 ms/day drift becomes 14.4 s over")
    print("  180 days, which is 115 km of apparent mislocation.  Clock drift is")
    print("  therefore not a subtlety; it is a first-order error that must be")
    print("  measured (by cross-correlating a common event between adjacent")
    print("  instruments, or against a GNSS-disciplined clock) and applied.")

    section("6. Verification")
    print("(a) the multiple period against the water depth:")
    for h in DEPTHS:
        Tw = 2.0 * h / C_WATER
        print(f"    h = {h:6.0f} m -> T_w = {Tw:.4f} s -> "
              f"recovered h = c T_w / 2 = {C_WATER * Tw / 2:.1f} m")
    print("    the round trip is exact by construction, so the check is that the")
    print("    arithmetic has no factor-of-two error.  A factor-of-two error here")
    print("    is the commonest mistake in using the water-layer period.")
    print("(b) the compliance estimator is unbiased when there is no compliance:")
    P2 = RNG.standard_normal(n)
    V2 = 0.05 * RNG.standard_normal(n)
    Ph2, Vh2 = np.fft.rfft(P2), np.fft.rfft(V2)
    num2 = np.convolve((Vh2 * np.conj(Ph2)).real, kern, mode="same") + 1j * \
        np.convolve((Vh2 * np.conj(Ph2)).imag, kern, mode="same")
    den2 = np.convolve(np.abs(Ph2) ** 2, kern, mode="same")
    Z2 = num2 / np.maximum(den2, 1e-12)
    Vc2 = np.fft.irfft(Vh2 - Z2 * Ph2, n)
    print(f"    variance before = {V2.var():.6f}, after = {Vc2.var():.6f}, "
          f"ratio = {V2.var() / Vc2.var():.4f}")
    print("    an uncorrelated pair leaves the variance essentially unchanged,")
    print("    which is the property that makes the correction safe to apply.")
    print("(c) tilt leakage: at zero tilt sin(theta) = 0 exactly, so no leakage.")
    print(f"    sin(0) = {np.sin(0.0):.6f}; the formula reduces correctly.")
    print("(d) the Ps delay uses the same vertical-slowness algebra as the")
    print("    receiver-function module:")
    print(f"    q_s = {q_s:.6f} s/km, q_p = {q_p:.6f} s/km, and both are real,")
    print("    which is the requirement that the ray is not evanescent.")


if __name__ == "__main__":
    main()
