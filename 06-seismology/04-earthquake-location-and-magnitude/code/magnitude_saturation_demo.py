#!/usr/bin/env python3
"""Magnitude saturation, measured: how a fixed-band magnitude stops responding
to event size, and what that does to a catalogue.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python magnitude_saturation_demo.py

Requires: numpy.  No network access.

Everything is SYNTHETIC.  The source family, the path, the bands and the
internal calibration of the band magnitudes are teaching values chosen here;
the only imported physics is the standard definition of moment magnitude and
the standard maximum-likelihood b-value estimator.  No published magnitude
correction or catalogue is used.

WHAT IS COMPUTED

1. The mb(Mw) and Ms(Mw) curves of the same self-similar source family, and
   the SIZE at which each stops responding (saturation onset), measured as the
   point where the local slope d(scale)/d(Mw) first falls below 0.75.
2. A synthetic Gutenberg-Richter catalogue specified in Mw, converted to mb
   through that curve, and the b-value recovered from the converted magnitudes.
   The difference between the two b-values is a catalogue artefact, not a
   change in the Earth.
3. What the conversion costs: recovering Mw from mb when mb is saturated, and
   the spread of true Mw hidden inside one mb value.
4. The contrast that makes saturation a reporting problem rather than a
   physical one: a radiated-energy proxy measured from the same pulses keeps
   growing with slope 1.5 in Mw exactly where mb has stopped.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

RHO = 2700.0            # kg/m^3
BETA = 3500.0           # m/s
R_M = 100.0e3           # m, fixed source-receiver distance
PATTERN = np.sqrt(2.0 / 5.0)
Q_PATH = 400.0
T_STAR = R_M / BETA
M0_REF = 1.0e15         # N m
FC_REF = 0.6            # Hz
F_BODY = 1.00           # Hz
F_SURFACE = 0.05        # Hz (20 s)


def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


def corner_frequency(m0):
    return FC_REF * (m0 / M0_REF) ** (-1.0 / 3.0)


def moment_magnitude(m0):
    return (2.0 / 3.0) * (np.log10(m0) - 9.1)


def mw_to_m0(mw):
    return 10.0 ** (1.5 * mw + 9.1)


def spectrum_amplitude_um(f, m0):
    """Far-field displacement amplitude at frequency f, in micrometres."""
    plateau = m0 * PATTERN / (4.0 * np.pi * RHO * BETA ** 3 * R_M)
    fc = corner_frequency(m0)
    return (plateau / (1.0 + (f / fc) ** 2)
            * np.exp(-np.pi * f * T_STAR / Q_PATH)) * 1e6


# Internal calibration: the band magnitudes equal Mw at M0_REF.
C_BODY = moment_magnitude(M0_REF) - np.log10(spectrum_amplitude_um(F_BODY, M0_REF))
C_SURF = moment_magnitude(M0_REF) - np.log10(spectrum_amplitude_um(F_SURFACE, M0_REF))


def mb_of_mw(mw):
    return np.log10(spectrum_amplitude_um(F_BODY, mw_to_m0(mw))) + C_BODY


def ms_of_mw(mw):
    return np.log10(spectrum_amplitude_um(F_SURFACE, mw_to_m0(mw))) + C_SURF


def energy_proxy(m0):
    """Integral of far-field velocity squared over the pulse, in (m/s)^2 s.

    Far-field displacement u(t) = A (t/tau^2) exp(-t/tau) with tau = 1/(2 pi fc)
    and A the spectral plateau; the far-field velocity is du/dt and this
    function returns its time integral of squares, computed numerically.
    """
    fc = corner_frequency(m0)
    tau = 1.0 / (2.0 * np.pi * fc)
    t = np.arange(0.0, 30.0 * tau, tau / 400.0)
    amp = m0 * PATTERN / (4.0 * np.pi * RHO * BETA ** 3 * R_M)
    v = amp * (1.0 / tau ** 2) * np.exp(-t / tau) * (1.0 - t / tau)
    return float(np.sum(v ** 2) * (t[1] - t[0]))


def local_slope(mws, vals, step=0.25):
    """Numerical d(value)/d(Mw) at every sample, by central difference."""
    return np.gradient(vals, mws)


def onset(mws, vals, threshold=0.75):
    """Smallest Mw above which the local slope stays below `threshold`."""
    sl = local_slope(mws, vals)
    below = np.where(sl < threshold)[0]
    # index where the curve first enters and never recovers
    for i in below:
        if np.all(sl[i:] < threshold):
            return float(mws[i])
    return float("nan")


def main():
    print("Magnitude saturation, measured on a synthetic self-similar family")
    print(f"numpy {np.__version__}")
    print()
    print(f"  SYNTHETIC medium: rho = {RHO:.0f} kg/m^3, beta = {BETA:.0f} m/s, "
          f"R = {R_M / 1e3:.0f} km")
    print(f"  path Q = {Q_PATH:.0f};  bands: {F_BODY:.2f} Hz (mb), "
          f"{F_SURFACE:.2f} Hz (Ms)")
    print(f"  internal calibration constants: c_body = {C_BODY:+.4f}, "
          f"c_surface = {C_SURF:+.4f}")
    print("  both fixed by requiring the scale to equal Mw at "
          f"M0 = {M0_REF:.1e} N m")

    mws = np.arange(3.0, 9.51, 0.05)
    mb_vals = mb_of_mw(mws)
    ms_vals = ms_of_mw(mws)

    section("1. The saturation curves and where they stop responding")
    print(f"  {'Mw':>6}{'mb':>8}{'dmb/dMw':>10}{'Ms':>8}{'dMs/dMw':>10}")
    for i in range(0, mws.size, 10):
        sl_b = local_slope(mws, mb_vals)[i]
        sl_s = local_slope(mws, ms_vals)[i]
        print(f"  {mws[i]:6.2f}{mb_vals[i]:8.2f}{sl_b:10.3f}"
              f"{ms_vals[i]:8.2f}{sl_s:10.3f}")
    print()
    ob, oms = onset(mws, mb_vals), onset(mws, ms_vals)
    print("  the band crosses the corner frequency (fc = f_band) at")
    for name, fb in (("mb", F_BODY), ("Ms", F_SURFACE)):
        m0_cross = M0_REF * (FC_REF / fb) ** 3
        print(f"    {name}: M0 = {m0_cross:.3e} N m, Mw = "
              f"{moment_magnitude(m0_cross):.2f}")
    print("  but the SLOPE only falls below the 0.75 threshold further along:")
    print(f"  saturation onset by threshold (slope first falls below 0.75 and")
    print(f"  stays there):")
    print(f"    mb: Mw = {ob:.2f}, value there {mb_of_mw(ob):.2f}")
    print(f"    Ms: Mw = {oms:.2f}, value there {ms_of_mw(oms):.2f}")
    print(f"  largest values on the grid (up to Mw = {mws[-1]:.1f}):")
    print(f"    mb = {mb_vals[-1]:.2f}, Ms = {ms_vals[-1]:.2f}")
    print(f"  asymptotic slope in the last 1.0 magnitude units:")
    tail = mws > mws[-1] - 1.0
    print(f"    dmb/dMw = {np.polyfit(mws[tail], mb_vals[tail], 1)[0]:.3f}, "
          f"dMs/dMw = {np.polyfit(mws[tail], ms_vals[tail], 1)[0]:.3f}")
    print()
    print("  Both curves approach a slope of 0.5, not 0.  A band on the f^-2")
    print("  branch still grows, as M0^(1/3); what it stops doing is growing")
    print("  fast enough to keep pace with the moment.  'Saturation' is a")
    print("  statement about the slope, and a scale with a slope of 0.5 is still")
    print("  usable if the slope is known.")

    section("2. A synthetic Gutenberg-Richter catalogue, specified in Mw")
    b_input = 1.0
    mw_min, mw_max = 4.0, 8.5
    n_events = 2000
    # Truncated exponential in Mw: inverse-CDF sampling for a GR law.
    u = RNG.random(n_events)
    beta_gr = b_input * np.log(10.0)
    mw_cat = mw_min - np.log(1.0 - u * (1.0 - np.exp(-beta_gr * (mw_max - mw_min)))) / beta_gr
    mb_cat = mb_of_mw(mw_cat)
    print(f"  {n_events} events, Mw drawn from a truncated GR law between")
    print(f"  Mw = {mw_min:.1f} and {mw_max:.1f} with b = {b_input:.2f} (SYNTHETIC).")
    print()

    def b_mle(mags):
        """Standard maximum-likelihood b-value: log10(e) / (mean - min)."""
        return np.log10(np.e) / (mags.mean() - mags.min())

    print(f"  recovered b from the Mw sample      = {b_mle(mw_cat):.3f}")
    print(f"  recovered b from the mb sample      = {b_mle(mb_cat):.3f}")
    print(f"  mb range spanned by the catalogue   = "
          f"{mb_cat.min():.2f} to {mb_cat.max():.2f}")
    print(f"  Mw range spanned by the catalogue   = "
          f"{mw_cat.min():.2f} to {mw_cat.max():.2f}")
    print()
    for thr in (6.0, 6.5, 7.0):
        n_mw = int(np.sum(mw_cat >= thr))
        n_mb = int(np.sum(mb_cat >= thr))
        print(f"    events with Mw >= {thr:.1f}: {n_mw:4d}   "
              f"events with mb >= {thr:.1f}: {n_mb:4d}")
    print()
    print("  The b-value of the mb sample is different from the b-value of the Mw")
    print("  sample even though both describe the SAME earthquakes.  Compression")
    print("  of the large end steepens the fitted line, and the count above any")
    print("  mb threshold is not the count above the corresponding Mw threshold.")
    print("  A b-value is therefore a property of the catalogue's measurement, not")
    print("  of the seismicity alone.")

    section("3. What converting mb to Mw costs")
    # A practitioner's conversion: a straight line fitted to the SMALL events.
    small = mws <= 5.0
    a_fit, c_fit = np.polyfit(mb_vals[small], mws[small], 1)
    print("  A common shortcut is to fit a linear Mw-to-mb conversion on the")
    print("  small events, where both scales behave, and apply it everywhere.")
    print(f"  Fitted here on Mw <= 5.0:  Mw_est = {a_fit:.3f} x mb {c_fit:+.3f}")
    print()
    print(f"  {'Mw':>6}{'mb':>7}{'Mw_est':>9}{'bias':>8}"
          f"{'Mw range implied by mb +- 0.2':>32}")
    for target in (3.0, 3.5, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0):
        mbv = float(mb_of_mw(target))
        est = a_fit * mbv + c_fit
        lo = float(np.interp(mbv - 0.2, mb_vals, mws))
        hi = float(np.interp(mbv + 0.2, mb_vals, mws))
        print(f"  {target:6.1f}{mbv:7.2f}{est:9.2f}{est - target:8.2f}"
              f"{hi - lo:32.2f}")
    mb_top = float(mb_of_mw(9.0))
    bias_top = (a_fit * mb_top + c_fit) - 9.0
    print()
    print("  Two separate defects, in order of importance:")
    print("   (1) BIAS.  A conversion calibrated where the scale is linear, applied")
    print("       where it is saturated, under-reports a Mw 9.0 event as "
          f"Mw {a_fit * mb_top + c_fit:.2f}:")
    print(f"       a bias of {bias_top:.2f} magnitude units, or a factor of "
          f"{10 ** (-1.5 * bias_top):.0f} in moment.  A")
    print("       catalogue that converts magnitudes this way is not merely")
    print("       imprecise, it is inconsistent with itself across the size range.")
    print("   (2) UNCERTAINTY.  Give mb its own honest uncertainty (0.2 magnitude")
    print("       units is assumed here) and invert exactly.  Below the onset the")
    print("       implied Mw range is a few tenths; above it the range settles near")
    print("       0.8, because a slope of 0.5 doubles any magnitude uncertainty.")
    print("       The slope is what makes the inversion useless in practice: the")
    print("       same mb, to within its stated uncertainty, is produced by events")
    print("       whose moments differ by a factor of about 16, and no arithmetic")
    print("       can undo that.")
    print("  Mw is therefore obtained from the low-frequency spectrum, never by")
    print("  inverting a saturated band magnitude.")

    section("4. The physical information is still there: energy does not saturate")
    e_vals = np.array([energy_proxy(mw_to_m0(v)) for v in mws])
    log_e = np.log10(e_vals)
    slope_e = np.polyfit(mws, log_e, 1)[0]
    tail_slope_e = np.polyfit(mws[tail], log_e[tail], 1)[0]
    print(f"  radiated-energy proxy E = integral of (far-field velocity)^2 dt,")
    print(f"  same source family, computed from the synthetic pulses:")
    print(f"    d log10(E) / d Mw  over the whole range = {slope_e:.3f}")
    print(f"    d log10(E) / d Mw  in the last 1.0 Mw unit = {tail_slope_e:.3f}")
    print()
    print("  Compare the two rows with Section 1.  Where mb has a slope of 0.5,")
    print(f"  the energy proxy still has a slope of {tail_slope_e:.2f}: the source is")
    print("  radiating more and more, and the band-limited magnitude has simply")
    print("  stopped listening.  Saturation is a defect of the reporting scale, not")
    print("  a limitation of the earthquake.  Lesson 06 turns this proxy into a")
    print("  proper energy budget.")
    print()
    print("  Honest limit of the model: a point source has no finite-fault effect,")
    print("  so Ms here saturates only once the 20 s band falls below fc.  For the")
    print("  largest earthquakes the source duration itself exceeds the 20 s")
    print("  period, which requires a finite fault to represent, and that effect")
    print("  reinforces the same conclusion.")
    print()
    print("=" * 72)
    print("Source family, path, bands, calibration and catalogue are SYNTHETIC.")
    print("=" * 72)


if __name__ == "__main__":
    main()
