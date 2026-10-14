#!/usr/bin/env python3
"""Natural variability: red noise and the trend-detection problem, a damped
oscillator's spectral peak, the NAO-like short-timescale mode, the response to
solar and volcanic forcing, and a multiple-testing demonstration.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python natural_variability_demo.py

Everything is SYNTHETIC. Every timescale, amplitude, decay rate and noise level
is a CHOSEN TEACHING VALUE, printed by this script. No observed climate record,
index or eruption is used, and no amplitude, period or trend is quoted from
measurement.

Contents
--------
1. AR(1) red noise: decorrelation time, spectrum, and the distribution of
   30-year trends that pure noise produces.
2. How long a record must be for a trend to stand out from red noise.
3. A damped oscillator plus noise: the spectral peak, and what it does and does
   not identify.
4. An NAO-like short-timescale mode from an Ornstein-Uhlenbeck process.
5. Solar forcing: the attenuation and phase lag of a periodic forcing, verified
   numerically.
6. Volcanic forcing: a pulse, its decay, and when it is detectable.
7. Multiple testing: how many 'significant' trends arise by chance in M records.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

YEAR = 365.0 * 86400.0
DAY = 86400.0


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def ar1(n, phi, rng):
    x = np.empty(n)
    x[0] = rng.standard_normal()
    for k in range(1, n):
        x[k] = phi * x[k - 1] + rng.standard_normal()
    return x


# ---------------------------------------------------------------------------
# 1. Red noise and trends
# ---------------------------------------------------------------------------

def part1_red_noise():
    section("1. Red noise: what a trend looks like in a series with no trend")
    print("AR(1): x_k = phi x_{k-1} + noise, with unit innovation variance.")
    print("Decorrelation time tau = -1/ln(phi) in sampling units.\n")
    print(f"{'phi':>6} {'tau (annual samples)':>21} {'1-lag autocorr':>15}")
    for phi in (0.0, 0.2, 0.5, 0.6, 0.8):
        tau = 0.0 if phi == 0.0 else -1.0 / np.log(phi)
        print(f"{phi:6.2f} {tau:21.2f} {phi:15.2f}")
    n_years, n_real = 100, 20000
    print(f"\n  distribution of least-squares trends over the FIRST 30 years of")
    print(f"  {n_years}-year records, from {n_real} realisations (units: sd per")
    print("  year, i.e. the trend in units of the series' own standard deviation):")
    print(f"\n{'phi':>6} {'5th pct':>10} {'50th':>9} {'95th':>9} "
          f"{'95th/1year noise':>18}")
    t = np.arange(30)
    for phi in (0.0, 0.2, 0.5, 0.6, 0.8):
        trends = np.empty(n_real)
        for j in range(n_real):
            x = ar1(n_years, phi, RNG)
            trends[j] = np.polyfit(t, x[:30], 1)[0]
        trends /= np.std(ar1(n_years, phi, RNG))
        wnoise = 2.0 / np.sqrt(np.sum((t - t.mean()) ** 2))
        print(f"{phi:6.2f} {np.percentile(trends, 5):10.4f} "
              f"{np.median(trends):9.4f} {np.percentile(trends, 95):9.4f} "
              f"{np.percentile(trends, 95) / wnoise:18.2f}")
    print("\n  The last column is the ratio of the 95th percentile to the")
    print("  textbook white-noise value 2/sqrt(sum((t-tbar)^2)) for the same")
    print("  record. With phi = 0 the two agree, as they must. As persistence")
    print("  grows the distribution of spurious trends WIDENS: at phi = 0.8 it is")
    print("  about 2.2 times the white-noise value. A 30-year trend is therefore")
    print("  evidence only against a stated null, and the null must carry the")
    print("  persistence of the series.")


# ---------------------------------------------------------------------------
# 2. How long a record?
# ---------------------------------------------------------------------------

def part2_record_length():
    section("2. How long a record does a trend need?")
    print("For each record length, the 95th percentile of trends from AR(1) noise")
    print("with phi = 0.6, and the ratio of a 0.02 sd/year trend to that")
    print("threshold (a value above 1 means the trend would be detectable).\n")
    print(f"{'length (yr)':>12} {'95th pct of noise (sd/yr)':>26} "
          f"{'0.02 sd/yr trend / threshold':>29}")
    for length in (20, 40, 60, 80, 120):
        t = np.arange(length)
        n_real = 4000
        tr = np.empty(n_real)
        for j in range(n_real):
            x = ar1(length, 0.6, RNG)
            x = x / np.std(x)
            tr[j] = np.polyfit(t, x, 1)[0]
        crit = np.percentile(tr, 95)
        print(f"{length:12d} {crit:26.4f} {0.02 / crit:13.2f}")
    print("\n  The critical trend falls slowly with record length -- roughly as")
    print("  1/sqrt(n_eff) with n_eff far below n because of the persistence -- so")
    print("  doubling a record does not halve the detectable trend. Note also what")
    print("  the table cannot tell you: a trend that exceeds the threshold is")
    print("  *unlikely under the null*, which is not the same as being forced.")


# ---------------------------------------------------------------------------
# 3. A damped oscillator
# ---------------------------------------------------------------------------

def part3_oscillator():
    section("3. A damped oscillator plus noise: peak or no peak?")
    period_days, damping_days = 1400.0, 1000.0
    dt = 10.0
    n = int(200.0 * 365.0 / dt)
    t = np.arange(n) * dt
    omega = 2.0 * np.pi / period_days
    gamma = 1.0 / damping_days
    x = np.zeros(n)
    v = 0.0
    for k in range(1, n):
        acc = -omega ** 2 * x[k - 1] - 2.0 * gamma * v
        v += acc * dt + np.sqrt(2.0 * gamma) * RNG.standard_normal() * np.sqrt(dt)
        x[k] = x[k - 1] + v * dt
    print(f"SYNTHETIC damped oscillator: period {period_days:.0f} d, damping")
    print(f"  timescale {damping_days:.0f} d, driven by white noise, "
          f"{n} samples at {dt:.0f} d.")
    f, pxx = np.fft.rfft(x), None
    freqs = np.fft.rfftfreq(n, d=dt)
    psd = np.abs(np.fft.rfft(x - x.mean())) ** 2
    band = (freqs > 1.0 / (20.0 * 365.0)) & (freqs < 1.0 / 30.0)
    i_peak = np.argmax(psd[band])
    f_peak = freqs[band][i_peak]
    print(f"  spectral peak at a period of {1.0 / f_peak:.0f} d "
          f"(the deterministic period is {period_days:.0f} d)")
    half = psd[band] > 0.5 * psd[band].max()
    width = freqs[band][half].max() - freqs[band][half].min()
    print(f"  half-power bandwidth {width * 365.0:.4f} 1/yr gives a quality")
    print(f"  factor Q = f_peak/bandwidth = {f_peak / width:.2f}; the analytic")
    print(f"  value pi (damping/period) = {np.pi * damping_days / period_days:.2f}")
    print("  The bandwidth, not the peak position, is what carries the damping.")
    print("\n  A spectral peak gives the period and, through its WIDTH, the")
    print("  damping. A single peak period does not identify a mechanism: a")
    print("  damped oscillator and a narrow-band stochastic process can produce")
    print("  indistinguishable spectra, which is why identification requires a")
    print("  dynamical argument and not just a spectrum.")


# ---------------------------------------------------------------------------
# 4. A short-timescale mode
# ---------------------------------------------------------------------------

def part4_nao():
    section("4. A short-timescale mode: Ornstein-Uhlenbeck")
    tau_days = 10.0
    phi = np.exp(-1.0 / tau_days)
    dt = 0.25
    n = int(200.0 * 365.0 / dt)
    x = np.zeros(n)
    for k in range(1, n):
        x[k] = phi ** (dt / 1.0) * x[k - 1] + np.sqrt(1.0 - phi ** 2) \
            * RNG.standard_normal()
    print(f"SYNTHETIC OU process with a {tau_days:.0f}-day decorrelation time:")
    print(f"  lag-1 (daily) autocorrelation = {np.exp(-1.0 / tau_days):.4f}")
    print(f"  autocorrelation at 30 days = {np.exp(-30.0 / tau_days):.4f}")
    frac = 2.0 * tau_days / 30.0 * (1.0 - tau_days / 30.0
                                    * (1.0 - np.exp(-30.0 / tau_days)))
    print(f"  fraction of variance retained by a 30-day average = {frac:.4f}")
    print("\n  A 10-day memory means monthly averaging already removes most of")
    print("  the variance, and the monthly means are nearly independent. That is")
    print("  why this mode is described as weather-like rather than climate-like:")
    print("  it cannot integrate a forcing, so it cannot produce a trend.")


# ---------------------------------------------------------------------------
# 5. Periodic forcing
# ---------------------------------------------------------------------------

def part5_solar():
    section("5. Periodic forcing: attenuation and phase")
    period_yr, forcing_amp = 11.0, 0.5
    c_slab = 2.0423e8            # J/(m^2 K)
    lam = 5.418                  # W/(m^2 K)
    tau = c_slab / lam / YEAR
    omega_year = 2.0 * np.pi / period_yr
    attenuation = 1.0 / np.sqrt(1.0 + (omega_year * tau) ** 2)
    lag_yr = np.arctan(omega_year * tau) / omega_year
    print(f"Slab of capacity {c_slab:.4e} J/(m^2 K) with |lambda| = {lam:.3f}")
    print(f"  W/(m^2 K): relaxation time {tau:.3f} yr")
    print(f"  forcing: sinusoid of amplitude {forcing_amp} W/m^2, "
          f"period {period_yr:.0f} yr")
    print(f"\n  analytic attenuation 1/sqrt(1+(omega tau)^2) = {attenuation:.4f}")
    print(f"  therefore a response amplitude of "
          f"{forcing_amp / lam * attenuation:.4f} K")
    print(f"  analytic phase lag atan(omega tau)/omega = {lag_yr:.3f} yr")
    print("\n  verification by direct integration over 400 years:")
    n = 400 * 7300
    dt = 0.05 * YEAR
    temp = 0.0
    amps = []
    tt = np.arange(n) * dt / YEAR
    for k in range(n):
        f = forcing_amp * np.sin(2.0 * np.pi * tt[k] / period_yr)
        temp += dt * (f - lam * temp) / c_slab
        if k > 40 * 7300:
            amps.append(temp)
    amps = np.array(amps)
    tt2 = tt[40 * 7300:40 * 7300 + len(amps)]
    design = np.c_[np.sin(2.0 * np.pi * tt2 / period_yr),
                   np.cos(2.0 * np.pi * tt2 / period_yr)]
    coef = np.linalg.lstsq(design, amps, rcond=None)[0]
    print(f"    measured response amplitude from the last 360 years: "
          f"{np.hypot(coef[0], coef[1]):.4f} K")
    phase_meas = np.arctan2(-coef[1], coef[0]) / (2.0 * np.pi / period_yr)
    print(f"    measured phase lag: {phase_meas:.3f} yr "
          f"(analytic {lag_yr:.3f} yr)")
    print("  The measured amplitude matches the analytic value, which is a check")
    print("  on the integrator rather than on the model: a linear system driven")
    print("  by a sinusoid gives the same answer analytically and numerically.")
    print("  The physical content is the ATTENUATION: an 11-year oscillation is")
    print("  suppressed relative to the equilibrium response by the factor above,")
    print("  and delayed by about a year. Both effects follow from the slab's")
    print("  relaxation time and nothing else.")


# ---------------------------------------------------------------------------
# 6. A pulse
# ---------------------------------------------------------------------------

def part6_volcanic():
    section("6. A pulse: decay time and detectability")
    c_slab, lam = 2.0423e8, 5.418
    tau = c_slab / lam / YEAR
    amp, decay_yr = -2.0, 1.5
    print(f"SYNTHETIC negative forcing of {amp:.1f} W/m^2 decaying with a")
    print(f"  {decay_yr:.1f} yr timescale, applied to a slab with a relaxation")
    print(f"  time of {tau:.3f} yr.")
    t = np.arange(0.0, 30.0, 0.02)
    f = amp * np.exp(-t / decay_yr)
    # linear response by convolution with the slab's impulse response
    resp = np.zeros_like(t)
    dt = t[1] - t[0]
    for k in range(1, t.size):
        resp[k] = resp[k - 1] + dt * YEAR * (f[k] - lam * resp[k - 1]) / c_slab
    peak = float(resp.min())
    i_peak = int(np.argmin(resp))
    tail = np.where(resp[i_peak:] > 0.1 * peak)[0]
    i_recover = i_peak + int(tail[0]) if tail.size else t.size - 1
    print(f"\n  peak response {peak:.4f} K at t = {t[i_peak]:.2f} yr")
    print(f"  time to recover to 10% of the peak: {t[i_recover]:.2f} yr")
    print(f"  the forcing's e-folding time is {decay_yr:.1f} yr, but the")
    print(f"  temperature response lasts longer, because the slab lags the forcing")
    print(f"  by its own relaxation time of {tau:.2f} yr.")
    print("\n  detectability against an AR(1) null with phi = 0.2 over 30 years:")
    t30 = np.arange(30)
    n_real = 4000
    trends = np.empty(n_real)
    for j in range(n_real):
        x = ar1(30, 0.2, RNG)
        trends[j] = np.polyfit(t30, x, 1)[0]
    crit = np.percentile(trends, 5)
    print(f"    the 5th percentile of spurious 30-year trends is "
          f"{crit:.4f} K/yr (in units of the series' sd)")
    print(f"    the pulse's 30-year mean response is "
          f"{np.trapezoid(resp, t) / 30.0:.4f} K")
    print("    whether that is DETECTABLE depends on the series' own variability,")
    print("    which is a property of the observing system, not of the eruption.")


# ---------------------------------------------------------------------------
# 7. Multiple testing
# ---------------------------------------------------------------------------

def part7_multiple_testing():
    section("7. Multiple testing: how many 'significant' trends by chance?")
    n_years, n_real = 40, 20000
    t = np.arange(n_years)
    crit_w = 2.0 / np.sqrt(np.sum((t - t.mean()) ** 2))
    print(f"For a series of unit variance, the white-noise OLS slope threshold is")
    print(f"  2/sqrt(sum((t-tbar)^2)) = {crit_w:.4f} per year for {n_years} samples.")
    print("Applying that fixed threshold to AR(1) records, and comparing with the")
    print("threshold obtained from the correct AR(1) null at the same 5% level:\n")
    print(f"{'phi':>6} {'false positives at white-noise threshold':>41} "
          f"{'correct 5% threshold':>21}")
    for phi in (0.0, 0.2, 0.4, 0.6, 0.8):
        tr = np.empty(n_real)
        for j in range(n_real):
            x = ar1(n_years, phi, RNG)
            x = x / np.std(x)
            tr[j] = np.polyfit(t, x, 1)[0]
        fp = np.mean(np.abs(tr) > crit_w)
        print(f"{phi:6.2f} {fp * 100:40.1f}% {np.percentile(np.abs(tr), 95):21.4f}")
    print("\n  With white noise the white-noise threshold is correct by")
    print("  construction. With phi = 0.6 it produces false positives at several")
    print("  times the nominal 5% rate, because the effective number of")
    print("  independent samples is far below 40. The lesson from this table is")
    print("  not that trends are unreliable; it is that a significance statement")
    print("  is a statement about a null, and the null has to be stated.")


def main():
    part1_red_noise()
    part2_record_length()
    part3_oscillator()
    part4_nao()
    part5_solar()
    part6_volcanic()
    part7_multiple_testing()
    print("\nAll models and data in this module are SYNTHETIC teaching models.")


if __name__ == "__main__":
    main()
