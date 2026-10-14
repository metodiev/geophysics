#!/usr/bin/env python3
"""Monsoons, regional circulation and teleconnections: the land-sea annual
thermal cycle, the hydrostatic heat low, a synthetic monsoon index and its
threshold dependence, the delayed-oscillator ENSO period, the equatorial
thermocline tilt, stationary Rossby wavenumbers, and a Monte Carlo
significance test for a teleconnection correlation.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python monsoons_and_regional_demo.py

Everything is SYNTHETIC. The heat capacities, the forcing amplitudes, the
oscillator coefficients, the wind stresses and the paired time series are
*chosen teaching values*, not measurements or reconstructions of any real
monsoon, ENSO event or teleconnection. Standard constants (Omega, a, g, the
heat capacity of water) are used as constants.

Contents
--------
1. Land versus ocean annual cycle: amplitude and phase lag of a slab.
2. The heat low: hydrostatic surface-pressure drop from a column warming.
3. A synthetic monsoon index, the onset date it implies, and how much that
   date moves when only the threshold changes.
4. ENSO as a delayed oscillator: period versus delay, and a numerical
   verification of the period by integration.
5. Walker circulation: equatorial thermocline tilt from a zonal wind stress.
6. Stationary Rossby wavenumbers: which zonal wavenumbers propagate and which
   decay, and the direction energy travels.
7. A teleconnection correlation and the significance threshold that a
   short, autocorrelated record implies.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

OMEGA = 7.292115e-5
A_EARTH = 6.371e6
G = 9.81
C_P_WATER = 3985.0        # J/(kg K), seawater
RHO_WATER = 1025.0        # kg/m^3, chosen
C_P_AIR = 1004.0
DAY = 86400.0
DEG = np.pi / 180.0

# chosen effective heat capacities per unit area (J m^-2 K^-1)
C_LAND = 2.0e7            # ~10 m of rock/skin at 2.0e6 J m^-3 K^-1
C_OCEAN_MIXED = 50.0 * RHO_WATER * C_P_WATER     # 50 m mixed layer


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


# ---------------------------------------------------------------------------
# 1. Land versus ocean annual cycle
# ---------------------------------------------------------------------------

def slab_amplitude_phase(C, lam, period_days, F0):
    """Amplitude and phase lag of a slab  C dT/dt = F0 sin(wt) - lam T."""
    w = 2.0 * np.pi / (period_days * DAY)
    amp = F0 / np.sqrt(lam ** 2 + (C * w) ** 2)
    lag_rad = np.arctan2(C * w, lam)
    return amp, lag_rad, lag_rad / w / DAY, C * w


def part1_land_sea():
    section("1. Land versus ocean: the annual thermal cycle of a slab")
    period, f0, lam = 365.0, 40.0, 5.42
    print("Slab model C dT/dt = F0 sin(wt) - lam T with SYNTHETIC amplitudes:")
    print(f"  F0 = {f0:.1f} W/m^2, lam = {lam:.2f} W/(m^2 K), period = "
          f"{period:.0f} d")
    print(f"  C_land = {C_LAND:.3e} J/(m^2 K) (about 10 m of rock)")
    print(f"  C_ocean = {C_OCEAN_MIXED:.3e} J/(m^2 K) (50 m mixed layer, "
          f"rho = {RHO_WATER:.0f} kg/m^3, cp = {C_P_WATER:.0f} J/(kg K))")
    print(f"\n{'surface':>10} {'Cw (W/m^2K)':>13} {'amplitude (K)':>14} "
          f"{'lag (d)':>9} {'lag (deg of year)':>18}")
    out = {}
    for name, C in (("land", C_LAND), ("ocean", C_OCEAN_MIXED)):
        amp, lag_rad, lag_d, Cw = slab_amplitude_phase(C, lam, period, f0)
        out[name] = (amp, lag_d)
        print(f"{name:>10} {Cw:13.2f} {amp:14.2f} {lag_d:9.1f} "
              f"{np.degrees(lag_rad):18.1f}")
    print(f"\n  the land cycle is "
          f"{out['land'][0] / out['ocean'][0]:.1f}x larger and leads the ocean by "
          f"{out['ocean'][1] - out['land'][1]:.0f} days.")
    print("  That ratio and that lag are the thermodynamic origin of a monsoon:")
    print("  a continent and an ocean at the same latitude, under the same")
    print("  insolation, end up at different temperatures for five months of the")
    print("  year. The temperature difference is what drives the pressure")
    print("  difference, and the pressure difference drives the wind.")


# ---------------------------------------------------------------------------
# 2. The heat low
# ---------------------------------------------------------------------------

def part2_heat_low():
    section("2. The heat low: hydrostatic surface-pressure drop")
    t0, p0 = 300.0, 1.013e5
    print("For a column warmed uniformly by dT with the upper geopotential fixed,")
    print("hydrostatic balance gives dp_s = -p_s dT/T (a SYNTHETIC scaling).")
    print(f"\n{'column dT (K)':>15} {'dp_s (Pa)':>11} {'dp_s (hPa)':>11}")
    for dt in (0.5, 1.0, 2.0, 4.0, 6.0):
        dp = -p0 * dt / t0
        print(f"{dt:15.1f} {dp:11.1f} {dp / 100.0:11.2f}")
    print("\n  a 2 K whole-column warming corresponds to about -7 hPa. The real")
    print("  monsoon low is a fraction of that, because the warming is not uniform")
    print("  and the circulation partly cancels the pressure perturbation. The")
    print("  number is a scale, not a prediction.")


# ---------------------------------------------------------------------------
# 3. A synthetic monsoon index and its onset date
# ---------------------------------------------------------------------------

def synthetic_monsoon_wind(days, amp, noise_sd, rng):
    """Annual + semiannual harmonic plus AR(1) noise, in m/s (SYNTHETIC)."""
    t = np.arange(days)
    w = 2.0 * np.pi / 365.0
    seasonal = amp * (-np.cos(w * t) - 0.35 * np.cos(2.0 * w * t))
    noise = np.zeros(days)
    phi = 0.8
    for k in range(1, days):
        noise[k] = phi * noise[k - 1] + rng.standard_normal() * noise_sd
    return t, seasonal + noise


def onset_day(wind, threshold):
    """First day the index crosses the threshold from below, smoothed 5 days."""
    sm = np.convolve(wind, np.ones(5) / 5.0, mode="same")
    idx = np.where(sm > threshold)[0]
    return int(idx[0]) if idx.size else -1


def part3_monsoon_index():
    section("3. A synthetic monsoon index and the onset date it implies")
    days = 365
    t, wind = synthetic_monsoon_wind(days, 6.0, 1.0, RNG)
    print("SYNTHETIC index: annual + semiannual harmonic of amplitude 6.0 m/s,")
    print("plus AR(1) noise with phi = 0.8 and sd 1.0 m/s; 5-day running mean.")
    print(f"\n{'threshold (m/s)':>16} {'onset day':>10}")
    for thr in (1.0, 2.0, 3.0, 4.0, 5.0):
        d = onset_day(wind, thr)
        print(f"{thr:16.1f} {d:10d}")
    onsets = [onset_day(wind, thr) for thr in (1.0, 2.0, 3.0, 4.0, 5.0)]
    print(f"\n  moving the threshold from 1 to 5 m/s moves the onset date by "
          f"{max(onsets) - min(onsets)} days.")
    print("  The index is a single synthetic realisation, so this spread is a")
    print("  LOWER bound: an onset date is a definition, not a measurement, and")
    print("  two analysts reporting different onsets may both be right.")


# ---------------------------------------------------------------------------
# 4. Delayed-oscillator ENSO
# ---------------------------------------------------------------------------

def neutral_mode(a_coef, b_coef):
    """Neutral oscillatory mode of  dT/dt = a T(t) - b T(t - tau) - c T^3.

    With T ~ exp(i w t) the linear equation gives i w = a - b exp(-i w tau), so
    at neutrality (zero growth rate) a = b cos(w tau) and w = b sin(w tau).
    Eliminating tau gives w = sqrt(b^2 - a^2) and

        tau = arccos(a/b) / w,  period = 2 pi / w.

    Given (a, b) this returns the delay that makes the mode neutral and the
    period it oscillates at. tau is an OUTPUT here, not an input: a delayed
    oscillator does not let you choose both.
    """
    w = np.sqrt(b_coef ** 2 - a_coef ** 2)
    tau = np.arccos(a_coef / b_coef) / w
    return w, tau, 2.0 * np.pi / w


def integrate_oscillator(a_coef, b_coef, tau_days, c_coef, days,
                         dt=0.05, t0=1.0):
    """Integrate the nonlinear delayed oscillator and return T(t) and time."""
    n = int(days / dt)
    delay = max(1, int(round(tau_days / dt)))
    T = np.zeros(n + delay)
    T[:delay] = t0
    t = np.arange(n) * dt
    for k in range(delay, n + delay - 1):
        T[k + 1] = T[k] + dt * (a_coef * T[k] - b_coef * T[k - delay]
                                - c_coef * T[k] ** 3)
    return t, T[delay:]


def measure_period(t, T):
    """Period from the mean spacing of upward zero crossings."""
    cr = np.where((T[:-1] < 0.0) & (T[1:] >= 0.0))[0]
    if cr.size < 3:
        return float("nan")
    return float(np.mean(np.diff(cr)) * (t[1] - t[0]))


def part4_enso():
    section("4. ENSO as a delayed oscillator: period and delay are linked")
    a_coef, c_coef = 0.005, 0.25
    print("SYNTHETIC model dT/dt = a T(t) - b T(t - tau) - c T^3 with")
    print(f"  a = {a_coef:.4f} /d (growth), c = {c_coef:.2f} (1/(d K^2)).")
    print("At neutrality the pair a = b cos(w tau), w = b sin(w tau) gives")
    print("w = sqrt(b^2 - a^2) and tau = arccos(a/b)/w: choose b, and BOTH the")
    print("delay and the period follow. Then integrate the full nonlinear")
    print("equation with that delay and measure the period independently.")
    print()
    print(f"{'b (1/d)':>8} {'tau (months)':>13} {'period (months)':>16} "
          f"{'measured (months)':>18} {'amp at 60 yr (K)':>17}")
    rows = []
    for b_coef in (0.010, 0.015, 0.020, 0.030):
        w, tau_d, per_d = neutral_mode(a_coef, b_coef)
        t, T = integrate_oscillator(a_coef, b_coef, tau_d, c_coef, days=60 * 365.0)
        tail = t > 30 * 365.0
        measured = measure_period(t[tail], T[tail])
        amp = float(np.nanmax(np.abs(T[tail])))
        rows.append((b_coef, tau_d, per_d, measured, amp))
        print(f"{b_coef:8.3f} {tau_d / 30.44:13.2f} {per_d / 30.44:16.2f} "
              f"{measured / 30.44:18.2f} {amp:14.3f}")
    worst = max(abs(r[3] / r[2] - 1.0) for r in rows)
    print(f"\n  measured versus predicted period: worst disagreement "
          f"{worst * 100:.1f}%,")
    print("  the residual coming from the cubic term, which shifts the period")
    print("  slightly from the linear value.")
    print("  Read the first two columns together: a LONGER delay goes with a")
    print("  SMALLER b and hence a LONGER period. You cannot dial the period")
    print("  and the delay independently in this model.")
    print("  And a period is not an identification: two different oscillators can")
    print("  share a period of four years, so agreement with an observed period")
    print("  would not establish which mechanism is at work.")
    print("  The amplitude column is NOT predicted by this theory. At neutrality")
    print("  the linear mode neither grows nor decays, so the cubic term slowly")
    print("  damps the initial condition: the period is robust, the amplitude is")
    print("  not, and a real prediction of amplitude would need the nonlinear")
    print("  balance, not the linear dispersion relation.")


# ---------------------------------------------------------------------------
# 5. Walker circulation and thermocline tilt
# ---------------------------------------------------------------------------

def part5_walker():
    section("5. Walker circulation: equatorial thermocline tilt")
    g_prime, depth, basin = 0.02, 150.0, 1.5e7
    print("Shallow-water balance for the equatorial thermocline:")
    print("  g' dh/dx = tau/(rho0 H),  SYNTHETIC constant zonal wind stress.")
    print(f"  g' = {g_prime:.3f} m/s^2 (chosen), H = {depth:.0f} m, "
          f"rho0 = {RHO_WATER:.0f} kg/m^3, basin = {basin / 1e3:.0f} km")
    print(f"\n{'tau (N/m^2)':>12} {'dh/dx':>12} {'tilt over basin (m)':>21} "
          f"{'gravity-wave speed (m/s)':>26}")
    for tau in (0.02, 0.05, 0.08, 0.12):
        slope = tau / (RHO_WATER * g_prime * depth)
        print(f"{tau:12.2f} {slope:12.3e} {slope * basin:21.1f} "
              f"{np.sqrt(g_prime * depth):26.2f}")
    print("\n  a stress of 0.05 N/m^2 tilts the thermocline by about 240 m across")
    print("  a 15000 km basin, i.e. a west-minus-east depth anomaly of that order.")
    print("  The tilt IS the Walker circulation: the depth gradient supports an")
    print("  east-west pressure gradient which the wind balances. Change the wind")
    print("  and the tilt changes; that is the Bjerknes feedback in one line.")

    tau = 0.05
    print("\n  Bjerknes feedback, quantified with the same numbers:")
    slope = tau / (RHO_WATER * g_prime * depth)
    dslope = slope * 1.5          # a 50% wind increase, as a sensitivity test
    print(f"    a 50% wind increase deepens the tilt by "
          f"{(dslope - slope) * basin:.0f} m across the basin.")
    print("    A deeper west-east tilt corresponds to a stronger east-west SST")
    print("    gradient, which in this model drives a stronger wind: the loop is")
    print("    amplifying. Whether it oscillates or runs away depends on the")
    print("    delay in the adjustment -- Section 4 -- and on the damping.")


# ---------------------------------------------------------------------------
# 6. Stationary Rossby wavenumbers
# ---------------------------------------------------------------------------

def part6_rossby_waves():
    section("6. Stationary Rossby waves: the teleconnection waveguide")
    u = 15.0
    print("Stationary wavenumber K_s = sqrt(beta/U), beta = 2 Omega cos(phi)/a,")
    print(f"for a SYNTHETIC uniform westerly U = {u:.0f} m/s.")
    print(f"\n{'lat':>5} {'beta (1/m/s)':>14} {'K_s (1/m)':>12} "
          f"{'wavelength (km)':>16} {'m critical':>11}")
    for lat in (20.0, 30.0, 45.0, 60.0, 75.0):
        beta = 2.0 * OMEGA * np.cos(lat * DEG) / A_EARTH
        ks = np.sqrt(beta / u)
        m_crit = ks * A_EARTH * np.cos(lat * DEG)
        print(f"{lat:5.0f} {beta:14.4e} {ks:12.4e} "
              f"{2.0 * np.pi / ks / 1e3:16.0f} {m_crit:11.2f}")
    print("\n  a wave of zonal wavenumber m propagates meridionally where")
    print("  K_s^2 - k^2 > 0, with k = m/(a cos phi); otherwise it decays.")
    lat = 45.0
    beta = 2.0 * OMEGA * np.cos(lat * DEG) / A_EARTH
    ks = np.sqrt(beta / u)
    print(f"  at {lat:.0f} deg with U = {u:.0f} m/s:")
    print(f"{'m':>4} {'k (1/m)':>12} {'K_s^2 - k^2 (1/m^2)':>20} {'behaviour':>12}")
    for m in (1, 2, 3, 4, 5, 6, 8):
        k = m / (A_EARTH * np.cos(lat * DEG))
        disc = ks ** 2 - k ** 2
        behaviour = "propagates" if disc > 0 else "decays"
        print(f"{m:4d} {k:12.3e} {disc:20.3e} {behaviour:>12}")
    print("\n  only low wavenumbers reach a distant continent through this")
    print("  waveguide, which is why teleconnection patterns are planetary-scale")
    print("  and why a single regional anomaly does NOT imply a large-scale one.")
    k = 2.0 / (A_EARTH * np.cos(lat * DEG))
    cphase = -beta / (k ** 2)
    cgroup = beta / (k ** 2)
    print(f"\n  for m = 2 at {lat:.0f} deg, with meridional wavenumber l = 0:")
    print(f"    phase speed = {cphase:.1f} m/s (westward)")
    print(f"    group velocity = {cgroup:.1f} m/s (eastward)")
    print("  The crests travel westward while the energy travels eastward -- the")
    print("  opposite directions. A downstream region can therefore be modulated")
    print("  by a wave train whose crests are moving the other way.")


# ---------------------------------------------------------------------------
# 7. Teleconnection correlation and its significance threshold
# ---------------------------------------------------------------------------

def ar1(n, phi, rng):
    x = np.zeros(n)
    for k in range(1, n):
        x[k] = phi * x[k - 1] + rng.standard_normal()
    return x


def part7_significance():
    section("7. A teleconnection correlation and its significance threshold")
    n_years, phi, n_trials = 40, 0.6, 4000
    x = ar1(n_years, phi, RNG)
    y = 0.4 * x + np.sqrt(1.0 - 0.4 ** 2) * ar1(n_years, phi, RNG)
    r_obs = float(np.corrcoef(x, y)[0, 1])
    print(f"SYNTHETIC pair of annual indices, n = {n_years}, lag-1 "
          f"autocorrelation {phi:.1f}")
    print(f"the signal series was built with a specified correlation of 0.40;")
    print(f"the realised sample correlation is r = {r_obs:.3f}.")
    null = np.empty(n_trials)
    for k in range(n_trials):
        null[k] = np.corrcoef(ar1(n_years, phi, RNG),
                              ar1(n_years, phi, RNG))[0, 1]
    crit = float(np.percentile(np.abs(null), 95.0))
    p_obs = float(np.mean(np.abs(null) >= abs(r_obs)))
    p_hyp = float(np.mean(np.abs(null) >= 0.40))
    print(f"\n  null distribution from {n_trials} independent AR(1) pairs of the")
    print("  same length and autocorrelation:")
    print(f"    95th percentile of |r|                = {crit:.3f}")
    print(f"    empirical p-value of the observed r    = {p_obs:.3f}")
    print(f"    empirical p-value of a hypothetical r = 0.40: {p_hyp:.3f}")
    print(f"    white-noise threshold 2/sqrt(n)        = "
          f"{2.0 / np.sqrt(n_years):.3f}   (TOO SMALL)")
    print("\n  autocorrelation widens the null distribution, so an r that looks")
    print("  significant against white noise may not be significant here. Note")
    print("  also what a p-value is not: it does not measure the strength of the")
    print("  teleconnection, and a significant correlation is equally consistent")
    print("  with a common external driver as with a causal link between the two.")


def main():
    part1_land_sea()
    part2_heat_low()
    part3_monsoon_index()
    part4_enso()
    part5_walker()
    part6_rossby_waves()
    part7_significance()
    print("\nAll models and data in this module are SYNTHETIC teaching models.")


if __name__ == "__main__":
    main()
