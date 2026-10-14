#!/usr/bin/env python3
"""Satellite laser ranging, DORIS and VLBI: the range equation and its timing
budget, normal points, station velocity from a ranging series, the radial-bias
degeneracy, the Doppler observation of DORIS, the VLBI delay and fringe rate,
and the sensitivity of every technique to Earth rotation.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python satellite_laser_ranging_demo.py

Everything is SYNTHETIC: the stations, targets, baselines, source directions,
noise and series are teaching data generated here.  The constants
(c, the Earth radius, the Earth rotation rate, the M2 period) are stated
standards.  No real station, satellite, baseline or catalogue source is used.

Print-only: nothing is downloaded, nothing is written to disk.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

C = 299_792_458.0
R_EARTH = 6_371_000.0
OMEGA_EARTH = 7.292_115e-5        # rad/s


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74)


def main():
    section("1. Ranging: time of flight to millimetres, and the averaging that buys it")
    print("  r = c t / 2; a picosecond is 0.15 mm of range\n")
    print("   timing precision   range precision   altitude error if the range is exact")
    for dt_ps in (1000.0, 100.0, 10.0, 1.0):
        dr = C * dt_ps * 1e-12 / 2.0
        print(f"   {dt_ps:13.0f} ps   {dr*1000:11.4f} mm   {dr*1000:31.4f} mm")
    print("\n  single-shot ranging is limited by the number of detected photons and by")
    print("  the pulse width, not by the clock.  Repeated shots are averaged into a")
    print("  NORMAL POINT, and the averaging follows the usual law:\n")
    print("   shots in the normal point   error (mm) if one shot has 50 mm")
    for n in (1, 10, 100, 1000):
        print(f"   {n:26d}   {50.0/np.sqrt(n):23.2f}")
    print("\n  a thousand shots turn 50 mm into 1.6 mm, which is the level at which")
    print("  plate motion over a few years becomes measurable.  The limit is then no")
    print("  longer the timing but the target: the retroreflector array's centre-of-")
    print("  mass offset and its orientation-dependent range signature are systematic")
    print("  at the centimetre level and must be modelled, not averaged.")

    section("2. Station velocity from a ranging series")
    t = np.linspace(2000.0, 2010.0, 400)
    v_true = -12.0        # mm/yr (a subsiding station, SYNTHETIC)
    annual = 8.0          # mm
    sigma = 6.0           # mm per normal point
    print(f"  SYNTHETIC: {t.size} normal points over {t[-1]-t[0]:.0f} yr, "
          f"range noise {sigma:.1f} mm")
    print(f"  truth: radial velocity {v_true:.1f} mm/yr, annual term "
          f"{annual:.1f} mm\n")
    y = v_true * (t - 2000.0) + annual * np.sin(2.0 * np.pi * (t - 2000.0)) \
        + sigma * RNG.standard_normal(t.size)
    lin = np.polyfit(t - 2000.0, y, 1)
    a_mat = np.column_stack([t - 2000.0, np.sin(2 * np.pi * (t - 2000.0)),
                             np.cos(2 * np.pi * (t - 2000.0)),
                             np.ones_like(t)])
    coef, *_ = np.linalg.lstsq(a_mat, y, rcond=None)
    print(f"   linear fit only      : velocity {lin[0]:+9.4f} mm/yr "
          f"(bias {lin[0]-v_true:+.4f})")
    print(f"   linear + annual fit  : velocity {coef[0]:+9.4f} mm/yr "
          f"(bias {coef[0]-v_true:+.4f})")
    amp = np.hypot(coef[1], coef[2])
    print(f"   recovered annual amplitude: {amp:.4f} mm against a true "
          f"{annual:.1f} mm")
    print("\n  a decade of data resolves the annual term, so the bias here is small;")
    print("  with a two-year record it would not be (see the GNSS processing lesson).")
    print("  The formal error of the fitted velocity falls as 1/sqrt(N) only while")
    print("  the noise is white: satellite rotation, atmosphere and station")
    print("  instability all add correlated terms that must be modelled or bounded.")

    section("3. The radial-bias degeneracy")
    print("  a constant range bias delta appears as a radial station shift of delta;")
    print("  a global scale error s shifts every station by s times its radius.  Since")
    print("  every station sits at almost the same radius, the two signatures are")
    print("  almost identical - so the data cannot separate them.\n")
    n_st = 40
    radii = R_EARTH + RNG.uniform(0.0, 3000.0, n_st)     # a few km of relief
    g = np.column_stack([np.ones(n_st), radii / R_EARTH])
    cov = np.linalg.inv(g.T @ g)
    corr = cov[0, 1] / np.sqrt(cov[0, 0] * cov[1, 1])
    print(f"  {n_st} stations spread over {np.ptp(radii)/1e3:.1f} km of radius")
    print(f"   correlation between the radial-bias and scale estimates: "
          f"{corr:+.6f}")
    print(f"   variance inflation of the bias estimate: {cov[0,0]:.4f} "
          f"(1.0 would mean no inflation)")
    print(f"   standard error of the bias estimate: {np.sqrt(cov[0,0]):.4f} x sigma")
    print("\n  the correlation is -1 to six decimals: the radial bias and the global")
    print("  scale are the same parameter as far as radial observations are concerned,")
    print("  because the fractional spread of station radii is 3000/6371000 = "
          f"{3000/R_EARTH:.2e}.")
    print("  That is why a global scale is never estimated from ranging alone: it is")
    print("  constrained by the geometry that breaks the degeneracy - the transverse")
    print("  directions (VLBI, GNSS) or the varying radius of a satellite's orbit.")
    print("\n  the general rule: any parameter whose signature mimics the error you")
    print("  are estimating will absorb it, and the CORRELATION between the two is the")
    print("  honest measure of what the data can separate.  This is the same")
    print("  non-uniqueness argument as the InSAR height trade-off of module 17-03;")
    print("  only the geometry and the parameter names change.")

    section("4. DORIS: the Doppler observation")
    f0 = 2.0e9
    print(f"  Doppler shift: f_d = -(f0/c) drho/dt, with a beacon at "
          f"{f0/1e9:.1f} GHz\n")
    print("   range rate (km/s)   Doppler shift (kHz)   range rate (m/s)   shift (Hz)")
    for vr_km_s in (-7.5, -3.0, 0.0, 3.0, 7.5):
        fd = -(f0 / C) * vr_km_s * 1e3
        print(f"   {vr_km_s:17.2f}   {fd/1e3:20.4f}   {vr_km_s*1e3:17.1f}   "
              f"{fd:10.2f}")
    print("\n  a 7.5 km/s satellite motion gives tens of kHz, easily measured; the")
    print("  science comes from the small departures from a smooth curve, i.e. from")
    print("  the *shape* of the Doppler history near closest approach, which encodes")
    print("  the geometry.  Note the sign: approaching (negative range rate) gives a")
    print("  positive shift.")
    print("\n  the observation is geometrically the same as ranging - a measurement of")
    print("  distance or its rate between a station and a satellite - so it shares the")
    print("  radial-bias degeneracy of Section 3 and the same need for independent")
    print("  constraints.")

    section("5. VLBI: delay, resolution and the source direction")
    bw = 1.0e9
    print(f"  the correlated signal between two antennas is delayed by")
    print(f"  tau = B . s_hat / c, and the delay resolution is 1/BW = {1.0/bw*1e12:.1f} ps")
    print(f"  = {C/bw*1e3:.1f} mm of path, for a {bw/1e9:.0f} GHz channel:")
    print("  one nanosecond of delay is 300 mm of geometric path, so a delay")
    print("  measured to a picosecond locates the source to a fraction of a")
    print("  milliarcsecond on a baseline of thousands of kilometres.\n")
    print("   baseline (km)   max geometric delay (us)   fringe period at 8.4 GHz (ns)")
    for b_km in (500.0, 2000.0, 6000.0, 12000.0):
        delay = b_km * 1e3 / C
        fringe = 1.0 / 8.4e9
        print(f"   {b_km:13.0f}   {delay*1e6:25.3f}   {fringe*1e9:29.3f}")
    print("\n  the delay is huge compared with the resolution, which is the point:")
    print("  a baseline of thousands of kilometres turns a nanosecond-scale delay")
    print("  into a measurement of a source direction to a fraction of a")
    print("  milliarcsecond.  Earth rotation makes the projection of the baseline")
    print("  change continuously, so a source is mapped by the Earth's own motion.\n")
    src_true = np.array([0.6, 0.7, 0.3])
    src_true = src_true / np.linalg.norm(src_true)
    baselines = RNG.standard_normal((3, 3)) * 2000e3
    angs = []
    for _ in range(200):
        delays = baselines @ src_true / C + RNG.normal(0.0, 1e-11, 3)
        est, *_ = np.linalg.lstsq(baselines / C, delays, rcond=None)
        est = est / np.linalg.norm(est)
        # the difference vector is numerically stable where arccos of a dot
        # product near one is not
        angs.append(np.linalg.norm(est - np.dot(est, src_true) * src_true))
    ang_err_rad = float(np.mean(angs))
    ang_err_mas = ang_err_rad * 206264806.2 / 1e3
    b_mean = np.linalg.norm(baselines, axis=1).mean()
    expected_mas = C * 1e-11 / b_mean * 206264806.2 / 1e3
    print("  SYNTHETIC solution from three baselines with 10 ps of delay noise:")
    print(f"   mean baseline length      : {b_mean/1e3:.1f} km")
    print(f"   expected angle precision  : c sigma_tau / B = "
          f"{expected_mas:.4f} milliarcsecond")
    print(f"   realized direction error  : {ang_err_mas:.4f} milliarcsecond "
          f"= {ang_err_mas*1e3:.2f} microarcsecond (mean of 200 noise draws)")
    print(f"   delay magnitude           : "
          f"{np.abs(baselines @ src_true / C).mean()*1e6:.2f} microseconds, so the")
    print("   fractional precision achieved is of order 1e-5 - the number that")
    print("   matters, since the delay itself is set by the baseline geometry.")
    print("  the precision is set by the baseline length times the delay noise,")
    print("  which is why VLBI baselines are intercontinental and why its products")
    print("  are the definition of the celestial frame.")

    section("6. Earth rotation is in every one of these measurements")
    print("  the rotation rate omega enters the geometry of all three techniques: it")
    print("  moves the stations (ranging and DORIS) and rotates the baseline (VLBI).\n")
    b_km = 6000.0
    print(f"   for a {b_km:.0f} km baseline, a UT1 error rotates the Earth by")
    print("   d_theta = omega x dt:\n")
    print("    UT1 offset   rotation (urad)   delay change (ps)   vs 1 ps noise")
    for dut1_ms in (10.0, 1.0, 0.1, 0.01):
        d_theta = OMEGA_EARTH * dut1_ms * 1e-3
        d_delay = b_km * 1e3 / C * d_theta
        print(f"    {dut1_ms:8.2f} ms   {d_theta*1e6:14.4f}   "
              f"{d_delay*1e12:17.2f}   {d_delay*1e12:13.1f} x")
    print("\n  these delay changes are enormous compared with the picosecond-level")
    print("  delay precision of an interferometer, so VLBI does not suffer from an")
    print("  uncertain Earth rotation - it MEASURES it, and its products define the")
    print("  Earth orientation parameters.  The direction of the argument matters for")
    print("  the analyst: a solution must state whether those parameters were")
    print("  estimated, fixed to an external series, or predicted, because all three")
    print("  are defensible and they give slightly different station coordinates.")
    print("\n  the same rotation, applied the other way, is why a catalogue source is")
    print("  observed over hours: the baseline projection onto the source direction")
    print("  sweeps as the Earth turns, filling the (u, v) plane and turning three")
    print("  delay measurements into an image.")


if __name__ == "__main__":
    main()
