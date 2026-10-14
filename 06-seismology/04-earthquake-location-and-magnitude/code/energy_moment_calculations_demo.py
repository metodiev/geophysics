#!/usr/bin/env python3
"""Moment and energy from one synthetic spectrum and one synthetic pulse.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python energy_moment_calculations_demo.py

Requires: numpy, scipy (no network access).

Everything is SYNTHETIC.  The medium, the attenuation, the source family and the
reference corner frequency are teaching values.  Two pieces of physics are
imported and derived rather than assumed: the far-field relation between the
displacement spectrum and the seismic moment, and the radiated energy of a
far-field pulse over the focal sphere.  The one published coefficient used, the
2.34 of the Brune circular-crack corner frequency, is named where it is used and
is the only borrowed constant.

WHAT IS COMPUTED

1. The mean-square radiation coefficient for S waves from an exact
   double-couple pattern, by numerical integration over the focal sphere.
2. Recovery of the seismic moment M0 from the low-frequency plateau of the
   displacement spectrum, and of the corner frequency fc from the same
   spectrum, both with attenuation present in the data.
3. The source radius from fc, and the measured exponent in r proportional to
   M0^(1/3) that tests the self-similar assumption instead of asserting it.
4. Radiated energy from the far-field velocity pulse, integrated over the focal
   sphere; the measured slope d log10(E)/d(Mw), and the apparent stress.
5. What happens to the energy when the recording has a limited bandwidth: the
   same energy budget computed after a fixed low-pass, and the slope it then
   measures.

Units are stated in every column: N m for moment, Hz for frequency, km for
radius, J for energy, MPa for stress.
"""

import numpy as np
from scipy.optimize import least_squares

RNG = np.random.default_rng(20261014)

RHO = 2700.0             # kg/m^3
BETA = 3500.0            # m/s
MU = RHO * BETA ** 2     # Pa, rigidity at the source
R_M = 100.0e3            # m, fixed source-receiver distance
Q_PATH = 400.0           # SYNTHETIC path quality factor
T_STAR = R_M / BETA      # s
M0_REF = 1.0e15          # N m
FC_REF = 0.6             # Hz at M0_REF
BRUNE_COEF = 2.34        # Brune (1970) circular-crack corner-frequency coefficient
F_LP = 2.0               # Hz, the fixed low-pass of Section 5


def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


def dc_pattern_tensor():
    """A unit-normalised double-couple moment tensor (M0 = 1), strike 0, dip 90.

    x = north, y = east, z = up.  The far-field S-wave amplitude in a direction
    n is proportional to the component of M n perpendicular to n, so the
    radiation factor used below is
        a(n)^2 = |M n|^2 - (n^T M n)^2 ,
    which is exact for a point double couple and needs no approximation.
    """
    return np.array([[0.0, 1.0, 0.0],
                     [1.0, 0.0, 0.0],
                     [0.0, 0.0, 0.0]])


def sphere_directions(n_points):
    """Nearly uniform samples on the unit sphere (Fibonacci lattice)."""
    i = np.arange(n_points) + 0.5
    z = 1.0 - 2.0 * i / n_points
    phi = np.pi * (1.0 + 5.0 ** 0.5) * i
    r = np.sqrt(np.clip(1.0 - z ** 2, 0.0, None))
    return np.column_stack([r * np.cos(phi), r * np.sin(phi), z])


def mean_square_pattern(n_points=40000):
    """<a^2> over the focal sphere for the double couple, by integration."""
    m = dc_pattern_tensor()
    n = sphere_directions(n_points)
    mn = n @ m.T                      # (points, 3)
    radial = np.einsum("ij,jk,ik->i", n, m, n)
    a2 = np.sum(mn ** 2, axis=1) - radial ** 2
    return float(a2.mean()), float(a2.std() / np.sqrt(n_points))


def corner_frequency(m0):
    return FC_REF * (m0 / M0_REF) ** (-1.0 / 3.0)


def moment_magnitude(m0):
    return (2.0 / 3.0) * (np.log10(m0) - 9.1)


def mw_to_m0(mw):
    return 10.0 ** (1.5 * mw + 9.1)


def plateau(m0, pattern_rms):
    """Far-field displacement plateau in m s, for one direction."""
    return m0 * pattern_rms / (4.0 * np.pi * RHO * BETA ** 3 * R_M)


def observed_amplitude(f, m0, pattern_rms):
    """Attenuated far-field displacement spectral amplitude, m s."""
    return (plateau(m0, pattern_rms) / (1.0 + (f / corner_frequency(m0)) ** 2)
            * np.exp(-np.pi * f * T_STAR / Q_PATH))


def velocity_pulse(m0, pattern, n_points_tau=800, n_tau=30.0):
    """Far-field velocity pulse du/dt for one direction, with its time base.

    u(t) = A (t/tau^2) exp(-t/tau), tau = 1/(2 pi fc), A the displacement
    plateau.  Returned in m/s, with t in seconds.
    """
    fc = corner_frequency(m0)
    tau = 1.0 / (2.0 * np.pi * fc)
    t = np.arange(0.0, n_tau * tau, tau / n_points_tau)
    amp = m0 * pattern / (4.0 * np.pi * RHO * BETA ** 3 * R_M)
    v = amp * (1.0 / tau ** 2) * np.exp(-t / tau) * (1.0 - t / tau)
    return t, v


def band_fraction(m0, f_lp):
    """Fraction of the pulse energy a low-pass at f_lp keeps (exact).

    With X = 2 pi f_lp tau = f_lp/fc, the velocity spectrum magnitude is
    2 pi f A / (1 + (2 pi f tau)^2), and

        fraction = (2/pi) [ arctan X - X/(1 + X^2) ] ,

    which is checked numerically against the band integral in the demo.
    """
    x = f_lp / corner_frequency(m0)
    return float((2.0 / np.pi) * (np.arctan(x) - x / (1.0 + x ** 2)))


def fit_spectrum(f, a_obs, m0_start, fc_start, with_attenuation, pattern_rms):
    """Least-squares fit of (M0, fc) to a displacement spectrum.

    Both parameters are fitted in log10 space, which is the space in which a
    spectrum is actually measured.  `with_attenuation` decides whether the
    model includes the e^{-pi f t*/Q} factor; setting it False is the honest
    mistake a study makes when it does not know the path.
    """
    def model(p):
        m0 = 10.0 ** p[0]
        fc = 10.0 ** p[1]
        amp = m0 * pattern_rms / (4.0 * np.pi * RHO * BETA ** 3 * R_M)
        s = amp / (1.0 + (f / fc) ** 2)
        if with_attenuation:
            s = s * np.exp(-np.pi * f * T_STAR / Q_PATH)
        return np.log10(s)

    p0 = np.array([np.log10(m0_start), np.log10(fc_start)])
    sol = least_squares(lambda p: model(p) - np.log10(a_obs), p0)
    return 10.0 ** sol.x[0], 10.0 ** sol.x[1]


def main():
    print("Moment and energy from a synthetic spectrum and pulse")
    print(f"numpy {np.__version__}")
    print()
    print(f"  SYNTHETIC medium: rho = {RHO:.0f} kg/m^3, beta = {BETA:.0f} m/s, "
          f"mu = {MU:.3e} Pa")
    print(f"  fixed distance R = {R_M / 1e3:.0f} km, Q = {Q_PATH:.0f}, "
          f"t* = {T_STAR:.2f} s")
    print(f"  self-similar family: fc = {FC_REF:.2f} Hz at "
          f"M0 = {M0_REF:.1e} N m")

    section("1. The radiation coefficient, integrated rather than assumed")
    a2_mean, a2_err = mean_square_pattern()
    pattern_rms = np.sqrt(a2_mean)
    print("  exact double-couple S pattern a(n)^2 = |M n|^2 - (n^T M n)^2")
    print(f"  Monte Carlo over the focal sphere (40000 directions):")
    print(f"    <a^2> = {a2_mean:.4f} +- {a2_err:.4f}   (integral, dimensionless)")
    print(f"    sqrt(<a^2>) = {pattern_rms:.4f}")
    print()
    print("  The measured value agrees with the analytic 2/5 = 0.4 to within the")
    print("  Monte Carlo error, and sqrt(2/5) = 0.6325 is the familiar average")
    print("  radiation coefficient of the double couple.  It is used below to")
    print("  convert a single-station amplitude into a moment, which is exactly")
    print("  the assumption a real study makes when it has no focal-sphere")
    print("  coverage: a real moment from one station carries this factor as an")
    print("  uncertainty of order 20 to 30 per cent, not as a known number.")

    section("2. Moment and corner frequency recovered from the spectrum")
    m0s = np.array([1.0e13, 1.0e14, 1.0e15, 1.0e16, 1.0e17])
    f_fit = np.logspace(np.log10(0.005), np.log10(20.0), 120)
    print("  A 120-point spectrum from 0.005 to 20 Hz is fitted for (M0, fc) in")
    print("  log space.  Two fits are made: one that knows the attenuation and one")
    print("  that does not, which is the mistake a study makes without a path")
    print("  calibration.")
    print()
    print(f"  {'M0 true (N m)':>14}{'Mw true':>8}{'M0 fit':>12}{'M0 err':>9}"
          f"{'fc fit':>9}{'fc err':>9}   then ignoring attenuation:")
    print(f"  {'':>14}{'':>8}{'':>12}{'':>9}{'':>9}{'':>9}"
          f"{'M0 err':>10}{'fc err':>10}")
    for m0 in m0s:
        fc = corner_frequency(m0)
        a_obs = observed_amplitude(f_fit, m0, pattern_rms)
        m0_hat, fc_hat = fit_spectrum(f_fit, a_obs, m0 * 3.0, fc * 2.0, True, pattern_rms)
        m0_naive, fc_naive = fit_spectrum(f_fit, a_obs, m0 * 3.0, fc * 2.0, False, pattern_rms)
        print(f"  {m0:14.1e}{moment_magnitude(m0):8.2f}{m0_hat:12.3e}"
              f"{m0_hat / m0 - 1:9.2%}{fc_hat:9.4f}{fc_hat / fc - 1:9.2%}"
              f"{m0_naive / m0 - 1:16.2%}{fc_naive / fc - 1:10.2%}")
    print()
    print("  The first fit recovers both parameters: the moment lives in the flat")
    print("  part of the spectrum and the corner frequency in the bend, and they")
    print("  are independent measurements.  The plateau alone gives the size of the")
    print("  event and says nothing about its duration; fc alone gives the duration")
    print("  and not the moment.")
    print()
    print("  The second fit is the interesting one, and its errors have a sign.")
    print("  Ignoring the attenuation forces the model to reproduce a spectrum")
    print("  that falls faster than f^-2, and the only way to do that is to move")
    print("  fc DOWN: the printed corner frequencies are 42 to 63 per cent too")
    print("  low.  The plateau is then read off the same over-steepened curve, so")
    print("  the moment comes out 5 to 15 per cent too HIGH, and the error grows")
    print("  with event size because a larger event has more of its spectrum in")
    print("  the attenuated band.  That is the cost of an unmodelled t*, and it is")
    print("  why an M0 must be quoted together with the attenuation correction")
    print("  that produced it.")

    section("3. Source radius, and a test of self-similarity rather than a claim")
    fcs = np.array([corner_frequency(m) for m in m0s])
    radii = BRUNE_COEF * BETA / (2.0 * np.pi * fcs) / 1e3      # km
    print(f"  radius from the Brune circular-crack relation r = "
          f"{BRUNE_COEF} beta / (2 pi fc)")
    print(f"  (the coefficient {BRUNE_COEF} is Brune 1970's; everything else here is")
    print(f"  computed from this file's own model)")
    print()
    print(f"  {'M0 (N m)':>12}{'fc (Hz)':>10}{'r (km)':>9}{'log10 M0':>10}"
          f"{'log10 r':>9}")
    for m0, fc, r in zip(m0s, fcs, radii):
        print(f"  {m0:12.1e}{fc:10.4f}{r:9.2f}{np.log10(m0):10.2f}"
              f"{np.log10(r):9.3f}")
    expo = np.polyfit(np.log10(m0s), np.log10(radii), 1)[0]
    print()
    print(f"  measured exponent in r proportional to M0^p:  p = {expo:.4f}")
    print("  The self-similar family was built with p = 1/3; measuring 0.333")
    print("  confirms the arithmetic of the model and, in a real study, is the")
    print("  test of whether the events obey constant-stress-drop scaling.  When")
    print("  the measured p departs from 1/3 the assumption has failed, and both")
    print("  M0 and fc must then be reported without it.")

    section("4. Radiated energy and apparent stress")
    print("  Far-field velocity v(t) is integrated over the focal sphere:")
    print("      E_R = rho beta R^2 * integral over directions of dt v(t)^2")
    print("  The pulse shape is the same in every direction, so the direction")
    print("  average acts only on the pattern and the closed form is")
    print("      E_R = rho beta R^2 * 4 pi <a^2> * (M0/(4 pi rho beta^3 R))^2")
    print("            * 0.25 / tau^3 ,")
    print("  with the 0.25/tau^3 coming from integrating ((1 - t/tau) e^{-t/tau})^2.")
    print("  The Monte Carlo below checks that closed form rather than replacing it.")
    dirs = sphere_directions(2000)
    m = dc_pattern_tensor()
    radial = np.einsum("ij,jk,ik->i", dirs, m, dirs)
    mn = dirs @ m.T
    a_of_dir = np.sqrt(np.sum(mn ** 2, axis=1) - radial ** 2)
    d_omega = 4.0 * np.pi / dirs.shape[0]
    print()
    print(f"  {'Mw':>6}{'E_R closed form (J)':>21}{'E_R Monte Carlo (J)':>21}"
          f"{'ratio':>9}")
    energies = []
    for m0 in m0s:
        tau = 1.0 / (2.0 * np.pi * corner_frequency(m0))
        amp0 = m0 / (4.0 * np.pi * RHO * BETA ** 3 * R_M)
        e_closed = (RHO * BETA * R_M ** 2 * 4.0 * np.pi * a2_mean
                    * amp0 ** 2 * 0.25 / tau ** 3)
        total = 0.0
        for a in a_of_dir:
            t, v = velocity_pulse(m0, a)
            total += np.sum(v ** 2) * (t[1] - t[0]) * d_omega
        e_mc = RHO * BETA * R_M ** 2 * total
        energies.append(e_closed)
        print(f"  {moment_magnitude(m0):6.2f}{e_closed:21.4e}{e_mc:21.4e}"
              f"{e_mc / e_closed:9.4f}")
    energies = np.array(energies)
    mws = np.array([moment_magnitude(m0) for m0 in m0s])
    slope_mw = np.polyfit(mws, np.log10(energies), 1)[0]
    slope_m0 = np.polyfit(np.log10(m0s), np.log10(energies), 1)[0]
    tau_a = MU * energies / m0s / 1e6
    print()
    print(f"  apparent stress mu E_R/M0 (MPa): "
          f"{np.array2string(tau_a, precision=4, floatmode='fixed')}")
    print(f"  measured slope d log10(E_R)/d(Mw) = {slope_mw:.3f}")
    print(f"  measured slope d log10(E_R)/d log10(M0) = {slope_m0:.3f}")
    print()
    print("  The second number is the physics: a self-similar family with a")
    print("  size-independent stress drop radiates an energy proportional to the")
    print("  moment, so log10 E grows as log10 M0 with slope 1.  Converting with")
    print("  Mw = (2/3)(log10 M0 - 9.1) turns that slope of 1 into a slope of 1.5")
    print("  in Mw, which is the exponent of the standard energy-magnitude")
    print("  relation.  That exponent is derived here from the model rather than")
    print("  fitted: it follows from constant stress drop, and it is a test of")
    print("  self-similarity, not a law of nature.")
    print()
    print("  The apparent stress is constant because both E_R and M0 scale")
    print("  together.  In real data its constancy is the interesting claim and its")
    print("  scatter is the measurement; the absolute value here is a property of")
    print("  this synthetic pulse shape and carries no information about any real")
    print("  earthquake.")
    radius_ref = BRUNE_COEF * BETA / (2.0 * np.pi * corner_frequency(1.0e16))
    ds_ref = (7.0 / 16.0) * 1.0e16 / radius_ref ** 3 / 1e6     # MPa
    print()
    print(f"  one arithmetic check at Mw = {moment_magnitude(1.0e16):.2f}, "
          f"r = {radius_ref / 1e3:.2f} km:")
    print(f"    static stress drop (7/16) M0 / r^3 = {ds_ref:.4f} MPa")
    print(f"    apparent stress mu E_R / M0        = {tau_a[3]:.4f} MPa")
    print(f"    ratio apparent stress / stress drop = {tau_a[3] / ds_ref:.2f}")
    print("  A ratio of order 0.1 to 0.3 is what this pulse shape gives; the ratio")
    print("  is the model-independent content of the comparison.")

    section("5. The energy you measure depends on the band you recorded")
    print(f"  Same sources, same integral, applied to the pulses after a "
          f"{F_LP:.1f} Hz")
    print("  low-pass.  For this pulse the fraction of the energy below f_lp has a")
    print("  closed form: with X = f_lp/fc,")
    print("      fraction = (2/pi) [ arctan X - X/(1 + X^2) ] ,")
    print("  which the demo checks against a direct numerical band integral.")
    print()
    # numerical check of the closed form for one event
    m0_chk = m0s[2]
    fc_chk = corner_frequency(m0_chk)
    tau_chk = 1.0 / (2.0 * np.pi * fc_chk)
    f_chk = np.arange(0.0, F_LP, F_LP / 400000.0)
    v_spec = 2.0 * np.pi * f_chk / (1.0 + (2.0 * np.pi * f_chk * tau_chk) ** 2)
    num = 2.0 * np.trapezoid(v_spec ** 2, f_chk) / (0.25 / tau_chk ** 3)
    print(f"  check at fc = {fc_chk:.4f} Hz: closed form "
          f"{band_fraction(m0_chk, F_LP):.6f}, band integral {num:.6f}")
    print()
    print(f"  {'Mw':>6}{'fc (Hz)':>9}{'fraction of E_R kept':>22}"
          f"{'E_R kept (J)':>15}{'shortfall (factor)':>20}")
    kept = []
    for m0 in m0s:
        frac = band_fraction(m0, F_LP)
        kept.append(frac)
        e_kept = frac * energies[m0s.tolist().index(m0)]
        print(f"  {moment_magnitude(m0):6.2f}{corner_frequency(m0):9.4f}"
              f"{frac:22.4f}{e_kept:15.4e}{1.0 / frac:20.1f}")
    kept = np.array(kept)
    print()
    lp_slope = np.polyfit(mws, np.log10(kept * energies), 1)[0]
    print(f"  d log10(E_R low-passed)/d(Mw) = {lp_slope:.3f} "
          f"against {slope_mw:.3f} broadband")
    print()
    print("  Watch the factor in the last column.  A fixed 2 Hz band keeps 92 per")
    print("  cent of the energy of the Mw 5.3 event and only 9 per cent of the")
    print("  Mw 2.6 event, because the small event puts its corner frequency above")
    print("  the band edge and radiates most of its energy beyond it.  The bias is")
    print("  therefore size dependent, and here it is the SMALL events that are")
    print("  underestimated; had the band edge been above every corner frequency")
    print("  the large events would carry the bias instead.")
    print()
    print("  This is the honest limit of every radiated-energy estimate: it is an")
    print("  integral over a band, the band must be stated with the number, and a")
    print("  band-limited energy cannot be compared with a broadband one without")
    print("  saying so.  The moment has no such problem: it is read from the")
    print("  low-frequency plateau, where every event has energy, and the bandwidth")
    print("  only has to reach the corner frequency.")
    print()
    print("=" * 72)
    print("All source, path and model parameters are SYNTHETIC.  The only")
    print("borrowed constant is the Brune crack coefficient, named in Section 3.")
    print("=" * 72)


if __name__ == "__main__":
    main()
