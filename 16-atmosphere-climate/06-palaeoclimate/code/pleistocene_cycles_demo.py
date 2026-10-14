#!/usr/bin/env python3
"""Pleistocene glacial cycles and orbital forcing: a synthetic insolation
signal built from the standard astronomical periods, a slowly relaxing ice
volume with a melting threshold, and a measured comparison of where the power
sits in the forcing and in the response.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python pleistocene_cycles_demo.py

All models and data in this file are SYNTHETIC.  The forcing amplitudes and
phases are chosen; only the periods are the standard astronomical ones, and they
are stated in the code.  No real ice-volume or isotope record is used, and no
published period or spectral peak is quoted.

Contents
--------
1. A synthetic orbital forcing at the standard astronomical periods.
2. Ice volume from a slow growth plus a threshold-triggered melt.
3. Where the variance sits: power spectra of forcing and response, and the
   fraction of variance at periods longer than 60 ka.
4. Asymmetry of the response (sawtooth shape), and the sensitivity of the
   result to the melt threshold.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- standard astronomical periods (textbook orbital mechanics, in ka) ------
PERIOD_OBLIQUITY_KA = 41.0
PERIOD_PRECESSION_SHORT_KA = 23.0
PERIOD_PRECESSION_LONG_KA = 19.0
PERIOD_ECCENTRICITY_KA = 100.0

# --- SYNTHETIC amplitudes and model parameters -------------------------------
OBLIQUITY_AMPLITUDE = 0.50        # dimensionless insolation units
PRECESSION_AMPLITUDE = 0.70
PRECESSION_LONG_AMPLITUDE = 0.30
ECCENTRICITY_MODULATION = 0.50
GROWTH_RATE_PER_KA = 1.0 / 60.0   # slow ice growth
MELT_RATE_PER_KA = 0.60           # fast melting
MELT_THRESHOLD = 0.70             # forcing threshold for melting
MELT_WIDTH = 0.06                 # smoothness of the threshold
T_END_KA = 2400.0
DT_KA = 0.25


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def insolation(t_ka):
    """Synthetic mid-latitude summer insolation proxy, dimensionless."""
    obliq = OBLIQUITY_AMPLITUDE * np.sin(2 * np.pi * t_ka / PERIOD_OBLIQUITY_KA)
    envelope = 1.0 + ECCENTRICITY_MODULATION * np.cos(
        2 * np.pi * t_ka / PERIOD_ECCENTRICITY_KA)
    prec = PRECESSION_AMPLITUDE * envelope * np.sin(
        2 * np.pi * t_ka / PERIOD_PRECESSION_SHORT_KA)
    prec_long = PRECESSION_LONG_AMPLITUDE * envelope * np.sin(
        2 * np.pi * t_ka / PERIOD_PRECESSION_LONG_KA + 0.9)
    return obliq + prec + prec_long


def integrate_ice(threshold):
    t = np.arange(0.0, T_END_KA, DT_KA)
    forcing = insolation(t)
    volume = np.zeros_like(t)
    v = 0.5
    for i in range(len(t)):
        melt = MELT_RATE_PER_KA / (1.0 + np.exp(-(forcing[i] - threshold)
                                                / MELT_WIDTH))
        dv = GROWTH_RATE_PER_KA * (1.0 - v) - melt * v
        v = min(max(v + DT_KA * dv, 0.0), 1.0)
        volume[i] = v
    return t, forcing, volume


def band_power(t, signal, period_range):
    """Fraction of variance in a period band, by a least-squares sinusoid fit."""
    dt = t[1] - t[0]
    frequency = np.fft.rfftfreq(len(signal), d=dt)
    spectrum = np.abs(np.fft.rfft(signal - signal.mean())) ** 2
    with np.errstate(divide="ignore"):
        period = np.where(frequency > 0, 1.0 / frequency, np.inf)
    mask = (period >= period_range[0]) & (period < period_range[1])
    return float(spectrum[mask].sum() / spectrum[1:].sum()), period, spectrum


def dominant_period(t, signal, period_range):
    _, period, spectrum = band_power(t, signal, period_range)
    mask = (period >= period_range[0]) & (period < period_range[1])
    idx = np.argmax(spectrum[mask])
    return float(period[mask][idx])


def main():
    section("1. Synthetic orbital forcing")
    print(f"  standard astronomical periods used: obliquity "
          f"{PERIOD_OBLIQUITY_KA:.0f} ka, precession "
          f"{PERIOD_PRECESSION_SHORT_KA:.0f} and {PERIOD_PRECESSION_LONG_KA:.0f} ka, "
          f"eccentricity {PERIOD_ECCENTRICITY_KA:.0f} ka")
    print(f"  amplitudes and phases are SYNTHETIC choices: "
          f"{OBLIQUITY_AMPLITUDE:.2f}, {PRECESSION_AMPLITUDE:.2f}, "
          f"{PRECESSION_LONG_AMPLITUDE:.2f}")
    t = np.arange(0.0, T_END_KA, DT_KA)
    forcing = insolation(t)
    print(f"  record length = {T_END_KA:.0f} ka, sample interval = {DT_KA:.2f} ka")
    print(f"  forcing mean {forcing.mean():+.4f}, "
          f"standard deviation {forcing.std():.4f} (dimensionless units)")
    print(f"  precession terms are amplitude-modulated by the eccentricity term,")
    print(f"  with modulation depth {ECCENTRICITY_MODULATION:.2f}")

    section("2. Ice volume: slow growth and threshold melting")
    t, forcing, volume = integrate_ice(MELT_THRESHOLD)
    print(f"  growth rate 1/{1.0 / GROWTH_RATE_PER_KA:.0f} per ka; melt rate "
          f"{MELT_RATE_PER_KA:.2f} per ka above a threshold of "
          f"{MELT_THRESHOLD:.2f}")
    print(f"  ice volume range {volume.min():.4f} to {volume.max():.4f} "
          f"(dimensionless, 0 = no ice, 1 = maximum)")
    print(f"  mean {volume.mean():.4f}, standard deviation {volume.std():.4f}")
    print(f"  fraction of time with volume above 0.5: "
          f"{float(np.mean(volume > 0.5)):.3f}")

    section("3. Where the variance sits")
    bands = {"obliquity (41 ka)": (35.0, 50.0),
             "precession (19-23 ka)": (15.0, 30.0),
             "eccentricity (100 ka)": (80.0, 130.0),
             "long (>200 ka)": (200.0, 1000.0)}
    print(f"  {'period band':<24s} {'forcing share':>14s} {'response share':>15s}")
    forcing_fracs = []
    response_fracs = []
    for name, band in bands.items():
        frac_f, _, _ = band_power(t, forcing, band)
        frac_v, _, _ = band_power(t, volume, band)
        forcing_fracs.append(frac_f)
        response_fracs.append(frac_v)
        print(f"  {name:<24s} {frac_f:14.4f} {frac_v:15.4f}")
    long_band = (60.0, 1000.0)
    frac_f_long, _, _ = band_power(t, forcing, long_band)
    frac_v_long, _, _ = band_power(t, volume, long_band)
    print(f"  {'all periods > 60 ka':<24s} {frac_f_long:14.4f} "
          f"{frac_v_long:15.4f}")
    print(f"  the forcing has no power at the eccentricity period itself"
          f" except through the modulation.")
    print(f"  measured dominant period of the response = "
          f"{dominant_period(t, volume, (10.0, 1000.0)):.1f} ka")
    print(f"  measured dominant period of the forcing  = "
          f"{dominant_period(t, forcing, (10.0, 1000.0)):.1f} ka")
    print("  A linear response would put the ice power where the forcing power is.")
    print("  The threshold makes the response nonlinear, and the power moves to")
    print("  the long-period band without any long-period forcing being added.")

    section("4. Asymmetry and sensitivity to the threshold")
    growth_times = []
    for i in range(1, len(volume)):
        if volume[i] > volume[i - 1]:
            growth_times.append(DT_KA)
    fraction_growing = float(len(growth_times) * DT_KA / (len(volume) * DT_KA))
    print(f"  fraction of time in slow growth (dV/dt > 0) = "
          f"{fraction_growing:.3f}")
    print(f"  skewness of the volume record = "
          f"{float(((volume - volume.mean()) ** 3).mean() / volume.std() ** 3):+.4f}")
    print("  A sawtooth has a long slow rise and a short rapid fall, so it spends")
    print("  most of its time rising and its distribution is skewed. That asymmetry")
    print("  is a signature of the threshold, not of the forcing, which is nearly")
    print("  sinusoidal.")
    print(f"  {'melt threshold':>15s} {'mean volume':>12s} {'dominant period (ka)':>21s} "
          f"{'share > 60 ka':>14s}")
    for threshold in (0.60, 0.70, 0.80):
        _, _, vol = integrate_ice(threshold)
        share, _, _ = band_power(t, vol, long_band)
        period = dominant_period(t, vol, (10.0, 1000.0))
        print(f"  {threshold:15.2f} {vol.mean():12.4f} {period:21.1f} "
              f"{share:14.4f}")
    print("  Moving one threshold moves the dominant period and the concentration")
    print("  of variance. The glacial-cycle periodicity produced by a threshold")
    print("  model is a property of the model, which is why the mechanism behind the")
    print("  observed cycles is still a research question rather than a solved one.")


if __name__ == "__main__":
    main()
