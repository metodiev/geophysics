#!/usr/bin/env python3
"""Secular variation, jerks, and how much noise each time derivative costs.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python secular_variation_demo.py

Everything here is SYNTHETIC: the coefficient time series comes from a chosen
teaching model and the noise from a seeded generator.  No observatory record and
no published SV value is used.

Contents
--------
1. A synthetic g10(t) whose slope changes smoothly, and its derivatives.
2. The secular-variation spectrum by degree.
3. Westward drift measured from the phase of a spherical-harmonic pattern.
4. Noise amplification of the first, second and third derivatives (Monte Carlo).
5. Extrapolation error of a stale SV model.
6. How large a jerk must be to be detected at a given noise level.
7. Advection versus diffusion: why the two terms of the induction equation
   have to be compared with a dimensionless number.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

A_EARTH_KM = 6371.0
T_YEARS = np.arange(1950.0, 2021.0, 1.0)

# --- SYNTHETIC teaching series ----------------------------------------------
SV1 = -12.0          # nT/yr, secular variation before the jerk
SV2 = -34.0          # nT/yr, secular variation after the jerk
JERK_CENTRE = 1990.0
JERK_WIDTH = 1.5     # yr, controls how abrupt the change of slope is
G10_START = -30000.0


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def sv_of_t(t):
    """SYNTHETIC secular variation SV(t) = dg10/dt, in nT/yr."""
    return SV1 + (SV2 - SV1) * 0.5 * (1.0 + np.tanh((t - JERK_CENTRE) / JERK_WIDTH))


def g10_of_t(t):
    """Integrate the synthetic SV from 1950 to t with the trapezoid rule."""
    t = np.atleast_1d(t)
    out = np.empty_like(t, dtype=float)
    for i, tt in enumerate(t):
        grid = np.linspace(1950.0, tt, 2001) if tt > 1950.0 else np.array([1950.0])
        out[i] = G10_START + np.trapezoid(sv_of_t(grid), grid) if tt > 1950.0 \
            else G10_START
    return out


def deriv(y, dt, order=1):
    out = y.copy()
    for _ in range(order):
        out = (out[2:] - out[:-2]) / (2.0 * dt)
    return out


def main():
    section("1. A synthetic g10(t) with a smooth jerk, and its derivatives")
    g10 = g10_of_t(T_YEARS)
    sv = deriv(g10, 1.0, 1)
    sa = deriv(g10, 1.0, 2)
    sj = deriv(g10, 1.0, 3)
    print(f"SYNTHETIC series: g10(1950) = {G10_START:.1f} nT; SV changes from "
          f"{SV1:+.1f} to {SV2:+.1f} nT/yr")
    print(f"around {JERK_CENTRE:.0f} (tanh transition of width "
          f"{JERK_WIDTH:.1f} yr)")
    print("  year   g10 (nT)     SV (nT/yr)  acceleration (nT/yr^2)  "
          "jerk (nT/yr^3)")
    for yr in (1960.0, 1980.0, 1985.0, 1990.0, 1995.0, 2005.0, 2018.0):
        i = int(np.argmin(np.abs(T_YEARS - yr)))
        j1, j2 = i - 1, i - 2
        v1 = sv[j1] if 0 <= j1 < len(sv) else np.nan
        v2 = sa[j2] if 0 <= j2 < len(sa) else np.nan
        v3 = sj[j2 - 1] if 0 <= j2 - 1 < len(sj) else np.nan
        print(f"  {yr:.0f}   {g10[i]:10.2f}   {v1:9.3f}   {v2:19.3f}   {v3:13.3f}")
    print(f"  peak |jerk| in the series = {np.nanmax(np.abs(sj)):.3f} nT/yr^3")
    print("  a jerk is a third derivative phenomenon: it is invisible in the")
    print("  level of g10 and only a slope change in SV.")

    section("2. The secular-variation spectrum by degree")
    sv_coef = {
        1: [(-11.0, 0.0)],
        2: [(8.0, 0.0), (-4.0, 3.0)],
        3: [(5.0, 0.0), (-2.5, 1.5), (3.0, -2.0)],
        4: [(2.0, 0.0), (-1.0, 0.8), (1.4, -1.1), (-0.9, 0.6)],
    }
    powers = {n: (n + 1) * sum(g * g + h * h for (g, h) in lst)
              for n, lst in sv_coef.items()}
    tot = sum(powers.values())
    print("    n   SV power (nT/yr)^2   share    R_n_dot / R_1_dot")
    for n in sorted(powers):
        print(f"  {n:3d}   {powers[n]:18.1f}   {100*powers[n]/tot:6.2f}%   "
              f"{powers[n]/powers[1]:14.3e}")
    print("  the SV spectrum decays far more slowly with degree than the field")
    print("  spectrum does, so change is concentrated at the core surface on")
    print("  scales of a few thousand kilometres.")

    section("3. Westward drift from the phase of a harmonic pattern")
    drift_deg_per_yr = 0.15        # SYNTHETIC chosen drift rate
    lat = 20.0
    lons = np.arange(0.0, 360.0, 1.0)
    ph = np.radians(lons)
    m_harm = 2
    p0 = np.cos(m_harm * ph)
    dt = 10.0
    measured_shift = np.radians(drift_deg_per_yr * dt)
    p1 = np.cos(m_harm * (ph - measured_shift))
    # the phase of the complex Fourier coefficient of order m is m x shift
    C = np.sum(p1 * np.exp(-1j * m_harm * ph))
    shift_deg = np.degrees(np.angle(C) / m_harm)
    print(f"SYNTHETIC pattern drifts westward at {drift_deg_per_yr:.3f} deg/yr "
          f"(m = {m_harm} harmonic)")
    print(f"  pattern reused after {dt:.0f} yr; phase of the m = {m_harm} "
          f"coefficient gives a shift of {shift_deg:+.4f} deg")
    print(f"  measured drift rate = {abs(shift_deg)/dt:.4f} deg/yr "
          f"against a true {drift_deg_per_yr:.3f} deg/yr")
    print(f"  an m = {m_harm} pattern has a {180.0/m_harm:.0f} deg ambiguity, so "
          f"the method aliases at")
    print(f"  {180.0/m_harm/dt:.2f} deg/yr; a pattern with more longitude nodes "
          "aliases sooner.")
    km_per_deg = 2.0 * np.pi * A_EARTH_KM / 360.0
    print(f"  1 deg of longitude at the equator = {km_per_deg:.3f} km "
          f"(from R = {A_EARTH_KM:.0f} km)")
    speed = drift_deg_per_yr * km_per_deg * 1.0e3 / (365.25 * 86400.0)
    print(f"  {drift_deg_per_yr:.3f} deg/yr = {speed:.4e} m/s of rigid westward ")
    print("  motion at the equator - a kinematic statement, not proof of rigid")
    print("  motion; differential rotation fits the same data equally well.")

    section("4. Noise amplification of successive time derivatives")
    sigma = 1.0
    nreal = 20000
    print(f"Monte Carlo, {nreal} realisations, white noise rms = {sigma:.1f} nT "
          "on annual means")
    noise = RNG.normal(0.0, sigma, size=(nreal, len(T_YEARS)))
    d1 = (noise[:, 2:] - noise[:, :-2]) / 2.0
    d2 = (noise[:, 4:] - 2.0 * noise[:, 2:-2] + noise[:, :-4]) / 4.0
    d3 = (noise[:, 6:] - 3.0 * noise[:, 4:-2] + 3.0 * noise[:, 2:-4]
          - noise[:, :-6]) / 8.0
    print(f"  sigma of the SV estimator           = {d1.std():.4f} nT/yr   "
          f"(sqrt(1/2)/1 = {np.sqrt(0.5)*sigma:.4f})")
    print(f"  sigma of the acceleration estimator = {d2.std():.4f} nT/yr^2 "
          f"(sqrt(6)/4 = {np.sqrt(6.0)/4.0*sigma:.4f})")
    print(f"  sigma of the jerk estimator         = {d3.std():.4f} nT/yr^3 "
          f"(sqrt(20)/8 = {np.sqrt(20.0)/8.0*sigma:.4f})")
    print("  the gains are only mildly different for white noise; for the")
    print("  red noise of a real record the third derivative is dominated by")
    print("  the low-frequency part, which is why jerk epochs are contested.")

    section("5. Extrapolation error of a stale SV model")
    t0 = 1985.0
    print(f"a model fitted at {t0:.0f}, carrying the then-current slope "
          f"{SV1:+.1f} nT/yr, used afterwards:")
    print("  year   true g10 (nT)   model g10 (nT)   error (nT)")
    base = float(g10_of_t(np.array([t0]))[0])
    for yr in (1986.0, 1990.0, 1995.0, 2005.0, 2020.0):
        true_v = float(g10_of_t(np.array([yr]))[0])
        model_v = base + SV1 * (yr - t0)
        print(f"  {yr:.0f}   {true_v:13.2f}   {model_v:14.2f}   "
              f"{model_v-true_v:+9.2f}")
    print("  the error is the integral of the unmodelled slope change, so it")
    print("  grows linearly in the extrapolation interval, not with its square.")

    section("6. How large a jerk is detectable at a given noise level?")
    for sig in (0.5, 1.0, 2.0):
        thr = 3.0 * np.sqrt(20.0) / 8.0 * sig
        print(f"  noise sigma = {sig:.1f} nT on annual means -> jerk noise "
              f"{np.sqrt(20.0)/8.0*sig:.3f} nT/yr^3, 3-sigma threshold "
              f"{thr:.3f} nT/yr^3")
    print(f"  the SYNTHETIC jerk peaks at {np.nanmax(np.abs(sj)):.3f} nT/yr^3, "
          "so it is detected with")
    print("  a large margin - provided the record is long enough to contain the")
    print("  quiet periods on either side that define the baseline.")

    section("7. Advection versus diffusion of the same pattern")
    nx = 512
    x = np.linspace(0.0, 1.0, nx, endpoint=False)
    b = np.sin(2.0 * np.pi * x)
    k = 2.0 * np.pi * np.fft.rfftfreq(nx, d=1.0 / nx)
    T = 1.0
    u, D_num = 0.10, 0.02
    B = np.fft.rfft(b)
    b_adv = np.fft.irfft(B * np.exp(-1j * k * u * T), n=nx)
    b_diff = np.fft.irfft(B * np.exp(-D_num * k ** 2 * T), n=nx)
    print(f"  exact spectral operators over T = {T:.1f}: advection speed "
          f"u = {u:.2f}, diffusivity D = {D_num:.2f}")
    print("  peak amplitude relative to the initial field:")
    print(f"    advection: {np.abs(b_adv).max()/np.abs(b).max():.6f} "
          "(pattern moves, amplitude kept)")
    print(f"    diffusion: {np.abs(b_diff).max()/np.abs(b).max():.6f} "
          "(amplitude lost at a wavenumber-dependent rate)")
    print(f"  correlation with the initial field: advection "
          f"{np.corrcoef(b, b_adv)[0,1]:+.6f}, diffusion "
          f"{np.corrcoef(b, b_diff)[0,1]:+.6f}")
    print(f"  phase of the advected fundamental: "
          f"{np.degrees(np.angle(np.fft.rfft(b_adv)[1]/np.fft.rfft(b)[1])):.3f} deg "
          f"= -u T x 360 deg = {-u*T*360:.3f} deg")
    print("  the frozen-flux hypothesis is the statement that the first operator")
    print("  dominates on the advection time; the ratio of the two timescales is")
    print("  the magnetic Reynolds number.")


if __name__ == "__main__":
    main()
