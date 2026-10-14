#!/usr/bin/env python3
"""Seismic stratigraphy: wedge tuning, the resolution limit of a sequence
boundary, and accommodation-driven systems tracts.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python seismic_stratigraphy_demo.py

Contents
--------
1. Wedge model: peak-to-trough amplitude versus bed thickness (tuning curve).
2. Measured tuning thickness compared with the lambda/4 prediction.
3. Apparent (read-off) thickness: the plateau below tuning.
4. Detectability: the thinnest bed visible at a stated noise level.
5. Accommodation, eustasy and subsidence: a synthetic systems-tract sequence.

All models and numbers are SYNTHETIC teaching values: a chosen wavelet, chosen
velocities and chosen sea-level and subsidence curves, not measured data.  The
only externally fixed quantities are the definitions (two-way time 2h/v, the
Ricker wavelet, and the accommodation balance).
"""

import numpy as np

RNG = np.random.default_rng(20261014)

V_BED = 3.00          # km/s, chosen velocity of the wedge
R_COEFF = 0.10        # dimensionless, chosen reflection coefficient magnitude
F_DOM = 30.0          # Hz, chosen dominant frequency

# Synthetic sea-level / subsidence model (chosen, not measured)
EUSTASY_AMPL = 40.0   # m, amplitude of the eustatic cycle
EUSTASY_T = 1.0       # Myr, period of the eustatic cycle
SUBSIDENCE_RATE = 60.0   # m/Myr, tectonic subsidence of the shelf
SED_SUPPLY_RATE = 50.0   # m/Myr, sediment supply when accommodation exists


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def ricker(t, f0, t0=0.0):
    """Zero-phase Ricker wavelet of dominant frequency f0 (Hz), peak at t0."""
    tau = t - t0
    a = (np.pi * f0) ** 2
    return (1.0 - 2.0 * a * tau ** 2) * np.exp(-a * tau ** 2)


def wedge_response(h_m, v_km_s, f0, dt_s=0.0002, t_len=0.20):
    """Composite wavelet of a thin bed: top (+R) and base (-R) spikes."""
    t = np.arange(0.0, t_len, dt_s)
    two_way = 2.0 * (h_m / 1000.0) / v_km_s
    w = R_COEFF * ricker(t, f0, 0.05) - R_COEFF * ricker(t, f0, 0.05 + two_way)
    return t, w


def main():
    section("1. Wedge model: amplitude and read-off thickness versus h")
    print(f"chosen bed velocity {V_BED:.2f} km/s, wavelet {F_DOM:.0f} Hz Ricker,")
    print(f"reflection coefficients +{R_COEFF:.2f} and -{R_COEFF:.2f}")
    print("\n   h (m)   two-way dt (ms)   peak-trough amp   read-off dt (ms)")
    rows = []
    for h in (2.0, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 40.0, 50.0, 60.0):
        t, w = wedge_response(h, V_BED, F_DOM)
        two_way = 2.0 * (h / 1000.0) / V_BED
        amp = w.max() - w.min()
        i_peak = int(np.argmax(w))
        i_tr = int(np.argmin(w))
        read_off = abs(t[i_tr] - t[i_peak])
        rows.append((h, two_way, amp, read_off))
        print(f"  {h:6.1f}   {two_way * 1000:15.1f}   {amp:16.3f}   "
              f"{read_off * 1000:16.1f}")

    section("2. Measured tuning thickness versus the lambda/4 rule of thumb")
    def tuning_and_readoff(f0):
        hs = np.arange(0.5, 200.0, 0.05)
        amps = []
        for h in hs:
            t, w = wedge_response(h, V_BED, f0)
            amps.append(w.max() - w.min())
        amps = np.array(amps)
        h_tune = hs[int(np.argmax(amps))]
        h_read = np.nan
        for h in hs:
            t, w = wedge_response(h, V_BED, f0)
            true_dt = 2.0 * (h / 1000.0) / V_BED
            read_off = abs(t[int(np.argmin(w))] - t[int(np.argmax(w))])
            if 0.9 <= read_off / true_dt <= 1.1:
                h_read = h
                break
        return h_tune, h_read

    print("\n   f0 (Hz)   lambda/4 (m)   tuning h (m)   tuning/(lam/4)   "
          "smallest h with read-off within 10% of truth")
    for f0 in (15.0, 20.0, 30.0, 50.0):
        h_tune, h_read = tuning_and_readoff(f0)
        lam4 = V_BED * 1000.0 / f0 / 4.0
        print(f"  {f0:8.0f}   {lam4:12.1f}   {h_tune:12.2f}   "
              f"{h_tune / lam4:15.2f}   {h_read:41.2f}")
    print("Two different numbers, and both are needed.  The interference maximum")
    print("sits at 0.195 v/f0 = 0.78 lambda/4 for this Ricker wavelet, so the")
    print("composite amplitude is largest for a bed thinner than lambda/4.  The")
    print("thickness that can be READ from the wavelet to 10% needs 0.17 v/f0 =")
    print("0.68 lambda/4.  lambda/4 is the rule of thumb for both, and it is")
    print("conservative here: the exact coefficient is wavelet-dependent, so state")
    print("the wavelet and measure the coefficient rather than assuming it.")

    section("3. Apparent thickness: the resolution plateau")
    print("\n   h (m)   true dt (ms)   read-off dt (ms)   read-off/true")
    for h in (5.0, 10.0, 20.0, 25.0, 30.0, 40.0, 60.0):
        t, w = wedge_response(h, V_BED, F_DOM)
        true_dt = 2.0 * (h / 1000.0) / V_BED
        read_off = abs(t[int(np.argmin(w))] - t[int(np.argmax(w))])
        print(f"  {h:6.1f}   {true_dt * 1000:12.1f}   {read_off * 1000:16.1f}   "
              f"{read_off / true_dt:12.2f}")
    print("Below tuning the read-off time stops tracking thickness: a 5 m bed")
    print("reads 11.2 ms instead of 3.3 ms and a 10 m bed reads 11.4 ms instead of")
    print("6.7 ms.  The reflectivity is still imaged; the thickness is not.")

    section("4. Detectability at a stated noise level")
    amp_max = 2.0 * R_COEFF
    noise_level = 0.05 * amp_max
    print(f"thick-bed composite amplitude = 2R = {amp_max:.3f}")
    print(f"stated noise level = 5% of that = {noise_level:.4f}")
    print("\n   h (m)   composite amp   amp/noise   read-off/true   readable?")
    for h in (0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 25.0, 50.0):
        t, w = wedge_response(h, V_BED, F_DOM)
        amp = w.max() - w.min()
        true_dt = 2.0 * (h / 1000.0) / V_BED
        read_off = abs(t[int(np.argmin(w))] - t[int(np.argmax(w))])
        ratio = read_off / true_dt
        ok = "yes" if 0.89 <= ratio <= 1.11 and amp >= 3 * noise_level else "no"
        print(f"  {h:6.1f}   {amp:13.3f}   {amp / noise_level:9.1f}   "
              f"{ratio:13.2f}   {ok}")
    print("A 1 m bed returns an amplitude 2.4x the noise and is still not")
    print("resolvable; a 5 m bed at 12x the noise reads 3.4x too thick.  Detection")
    print("is an amplitude question, resolution is a bandwidth question, and they")
    print("fail at different thicknesses.")

    section("5. Accommodation, eustasy and subsidence: systems tracts")
    print(f"eustasy: {EUSTASY_AMPL:.0f} m amplitude, {EUSTASY_T:.1f} Myr period")
    print(f"subsidence {SUBSIDENCE_RATE:.0f} m/Myr, sediment supply "
          f"{SED_SUPPLY_RATE:.0f} m/Myr")
    print("\n   t (Myr)   eustasy (m)   rel. sea level (m)   accom. rate (m/Myr)"
          "   tract")
    t_grid = np.arange(0.0, 1.01, 0.05)
    prev = None
    tracts = []
    for tt in t_grid:
        e = EUSTASY_AMPL * np.sin(2.0 * np.pi * tt / EUSTASY_T)
        sub = -SUBSIDENCE_RATE * tt
        # water depth = sea level minus sediment-free basement top (relative)
        depth = e - sub
        if prev is None:
            rate = np.nan
            tract = "-"
        else:
            rate = (e - prev) / 0.05 + SUBSIDENCE_RATE
            if rate < 0.0:
                tract = "forced regression / sequence boundary"
            elif rate > SED_SUPPLY_RATE:
                tract = "transgressive"
            else:
                tract = "highstand / normal regression"
        tracts.append(tract)
        print(f"  {tt:6.2f}   {e:11.1f}   {depth:15.1f}   {rate:18.1f}   {tract}")
        prev = e
    n_fr = sum(1 for x in tracts if x.startswith("forced"))
    n_tr = sum(1 for x in tracts if x.startswith("trans"))
    n_hs = sum(1 for x in tracts if x.startswith("high"))
    print(f"\nsummary over one eustatic cycle: {n_tr} transgressive steps, "
          f"{n_hs} highstand steps, {n_fr} forced-regression steps")
    print(f"total accommodation created in 1 Myr = {SUBSIDENCE_RATE:.0f} m of "
          f"subsidence, of which the eustatic cycle can add or remove "
          f"{2 * EUSTASY_AMPL:.0f} m")
    print("The sequence boundary is set by the rate balance, not by a fixed")
    print("sea-level value: the same eustatic fall gives a forced regression")
    print("only when it outpaces subsidence.")


if __name__ == "__main__":
    main()
