#!/usr/bin/env python3
"""Magnitude scales from one synthetic source spectrum: local, body-wave,
surface-wave, duration and moment magnitude compared on the same events.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python magnitude_scales_demo.py

Requires: numpy.  No network access.

Everything is SYNTHETIC.  The source family, the path attenuation and every
additive constant below are chosen teaching values.  In particular, the
band-limited scales (ml, mb, Ms) are calibrated INSIDE this file so that they
agree with moment magnitude for one reference event; they are NOT the published
Gutenberg-Richter, Nuttli or IASPEI values, and those published corrections are
not reproduced or approximated here.  The only imported physics is the standard
definition of moment magnitude.

WHAT IS COMPUTED

1. A self-similar family of Brune-type sources: moment M0 sets the corner
   frequency fc through fc proportional to M0^(-1/3).
2. The far-field displacement spectrum of each event, with attenuation.
3. The amplitude a narrowband instrument would measure at 1.25 Hz (local),
   1.0 Hz (body wave) and 0.05 Hz (surface wave), and the magnitude that
   follows from each with an internal calibration constant.
4. A duration measured directly from the synthetic displacement pulse, and the
   duration magnitude that follows from it.
5. Moment magnitude from the standard definition.
6. The measured slopes d(scale)/d(Mw), which is where the scales stop being
   interchangeable.

All amplitudes are printed in micrometres and times in seconds, with the units
stated in the column headers.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC model constants -------------------------------------------------
RHO = 2700.0            # kg/m^3, crustal density
BETA = 3500.0           # m/s, S-wave speed at the source
R_KM = 100.0            # km, source-receiver distance (fixed, so the standard
R_M = R_KM * 1e3        #     distance correction of a real scale is constant)
PATTERN = np.sqrt(2.0 / 5.0)   # mean-square far-field radiation coefficient of a
                               # double couple: sqrt(<a^2>) with <a^2> = 2/5.
Q_PATH = 400.0          # quality factor of the path (SYNTHETIC)
T_STAR = R_M / BETA     # s, travel time; the attenuation exponent is pi f t*/Q

M0_REF = 1.0e15         # N m, reference moment at which every scale is calibrated
FC_REF = 0.6            # Hz, corner frequency of the reference event

F_LOCAL = 1.25          # Hz, local-magnitude band
F_BODY = 1.00           # Hz, body-wave-magnitude band
F_SURFACE = 0.05        # Hz, surface-wave (20 s) band

T = np.arange(0.0, 60.0, 0.05)   # s, pulse time base


def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


def corner_frequency(m0):
    """Self-similar corner frequency, Hz: fc proportional to M0^(-1/3)."""
    return FC_REF * (m0 / M0_REF) ** (-1.0 / 3.0)


def moment_magnitude(m0):
    """Standard moment magnitude, M0 in N m: Mw = (2/3)(log10 M0 - 9.1)."""
    return (2.0 / 3.0) * (np.log10(m0) - 9.1)


def plateau(m0):
    """Low-frequency level of the far-field displacement spectrum, in m s."""
    return m0 * PATTERN / (4.0 * np.pi * RHO * BETA ** 3 * R_M)


def displacement_spectrum(f, m0):
    """Far-field displacement spectrum in m s, with attenuation (m s)."""
    fc = corner_frequency(m0)
    return (plateau(m0) / (1.0 + (f / fc) ** 2)
            * np.exp(-np.pi * f * T_STAR / Q_PATH))


def band_amplitude(f_band, m0):
    """Amplitude at the centre of a narrowband instrument, converted to um."""
    return displacement_spectrum(f_band, m0) * 1e6


def pulse(m0):
    """Far-field displacement pulse u(t) for a Brune-type source, in um.

    u(t) is proportional to the moment rate of a one-sided exponential-decay
    source: u(t) = (t/tau^2) exp(-t/tau) with tau = 1/(2 pi fc).  Its low
    frequency spectrum is flat and equal to the plateau above, which is checked
    numerically in Section 1.
    """
    fc = corner_frequency(m0)
    tau = 1.0 / (2.0 * np.pi * fc)
    return plateau(m0) * (T / tau ** 2) * np.exp(-T / tau) * 1e6


def pulse_duration(m0):
    """1/e width of |u(t)| in seconds, measured from the synthetic pulse.

    The time base is rescaled per event (the pulse of a small event is short),
    which is what lets the same 1/e criterion be applied at every size.
    """
    fc = corner_frequency(m0)
    tau = 1.0 / (2.0 * np.pi * fc)
    t = np.arange(0.0, 30.0 * tau, tau / 200.0)
    u = np.abs((t / tau ** 2) * np.exp(-t / tau))
    peak = u.max()
    above = np.where(u > peak / np.e)[0]
    return float(t[above[-1]] - t[above[0]]) if above.size > 1 else np.nan


def main():
    print("Magnitude scales from one synthetic source spectrum")
    print(f"numpy {np.__version__}")
    print()
    print(f"  SYNTHETIC medium: rho = {RHO:.0f} kg/m^3, beta = {BETA:.0f} m/s")
    print(f"  fixed distance R = {R_KM:.0f} km, path Q = {Q_PATH:.0f}, "
          f"t* = {T_STAR:.2f} s")
    print(f"  radiation coefficient sqrt(<a^2>) = {PATTERN:.4f} "
          f"(from <a^2> = 2/5 for a double couple)")
    print(f"  reference event: M0 = {M0_REF:.1e} N m, fc = {FC_REF:.2f} Hz;")
    print("  every band-limited scale is calibrated to Mw at that one event.")

    section("1. The source family and one numerical check of the pulse")
    m0s = 10.0 ** np.arange(12.0, 22.5, 1.0)
    print(f"  {len(m0s)} events, self-similar: fc = fc_ref (M0/M0_ref)^(-1/3)")
    print()
    print(f"  {'M0 (N m)':>10}{'Mw':>7}{'fc (Hz)':>10}{'plateau (m s)':>16}"
          f"{'tau = 1/(2 pi fc) (s)':>24}")
    for m0 in m0s:
        fc = corner_frequency(m0)
        print(f"  {m0:10.1e}{moment_magnitude(m0):7.2f}{fc:10.4f}"
              f"{plateau(m0):16.3e}{1.0 / (2.0 * np.pi * fc):24.3f}")
    print()
    # Check that the time-domain pulse has the plateau as its low-frequency level.
    m0 = 1.0e16
    f_low = 0.001
    u = pulse(m0) * 1e-6
    dt = T[1] - T[0]
    dc = np.sum(u) * dt                      # integral of u(t) = spectrum at f=0
    print(f"  check at M0 = {m0:.1e} N m:")
    print(f"    integral of u(t) dt            = {dc:.6e} m s")
    print(f"    plateau from the closed form   = {plateau(m0):.6e} m s")
    print(f"    relative difference            = "
          f"{abs(dc - plateau(m0)) / plateau(m0):.2e}")
    print("  The pulse and the spectral plateau describe the same source, which is")
    print("  what makes a duration scale and an amplitude scale comparable at all.")

    section("2. Band amplitudes for a narrowband instrument (micrometres)")
    print(f"  local band   f = {F_LOCAL:.2f} Hz (about 0.8 s period)")
    print(f"  body band    f = {F_BODY:.2f} Hz (about 1 s period)")
    print(f"  surface band f = {F_SURFACE:.2f} Hz (20 s period)")
    print()
    print(f"  {'Mw':>6}{'fc (Hz)':>9}{'A_local (um)':>14}{'A_body (um)':>13}"
          f"{'A_surface (um)':>16}")
    for m0 in m0s:
        print(f"  {moment_magnitude(m0):6.2f}{corner_frequency(m0):9.4f}"
              f"{band_amplitude(F_LOCAL, m0):14.3e}"
              f"{band_amplitude(F_BODY, m0):13.3e}"
              f"{band_amplitude(F_SURFACE, m0):16.3e}")
    print()
    print("  Read the columns against fc.  While fc lies ABOVE the band, the band")
    print("  sits on the flat part of the spectrum and the amplitude grows in")
    print("  proportion to M0.  Once fc falls BELOW the band, the band sits on the")
    print("  f^-2 part, where the amplitude grows only as M0^(1/3) -- the band is")
    print("  then measuring the corner frequency, not the moment.")

    section("3. The five scales, calibrated to agree at the reference event")
    a_loc_ref = band_amplitude(F_LOCAL, M0_REF)
    a_body_ref = band_amplitude(F_BODY, M0_REF)
    a_surf_ref = band_amplitude(F_SURFACE, M0_REF)
    c_loc = moment_magnitude(M0_REF) - np.log10(a_loc_ref)
    c_body = moment_magnitude(M0_REF) - np.log10(a_body_ref)
    c_surf = moment_magnitude(M0_REF) - np.log10(a_surf_ref)
    print(f"  internal calibration constants (dimensionless), fixed by requiring")
    print(f"  each scale to equal Mw = {moment_magnitude(M0_REF):.2f} at "
          f"M0 = {M0_REF:.1e} N m:")
    print(f"    c_local   = {c_loc:+.4f}   (amplitude in um)")
    print(f"    c_body    = {c_body:+.4f}")
    print(f"    c_surface = {c_surf:+.4f}")
    print("  These are TEACHING constants internal to this synthetic model.  A real")
    print("  catalogue's scale carries an empirical distance correction and a")
    print("  station calibration; neither is imported here.")
    print()

    def ml(m0):
        return np.log10(band_amplitude(F_LOCAL, m0)) + c_loc

    def mb(m0):
        return np.log10(band_amplitude(F_BODY, m0)) + c_body

    def ms(m0):
        return np.log10(band_amplitude(F_SURFACE, m0)) + c_surf

    d_ref = pulse_duration(M0_REF)
    c_dur = moment_magnitude(M0_REF) - 2.0 * np.log10(d_ref)

    def md(m0):
        return 2.0 * np.log10(pulse_duration(m0)) + c_dur

    print(f"  duration scale: M_d = 2 log10(tau_d / 1 s) + {c_dur:+.4f}, with tau_d")
    print("  measured from the synthetic pulse as its 1/e width.")
    print()
    print(f"  {'Mw':>6}{'ml':>7}{'mb':>7}{'Ms':>7}{'M_d':>7}"
          f"{'tau_d (s)':>11}   difference from Mw")
    for m0 in m0s:
        mw = moment_magnitude(m0)
        print(f"  {mw:6.2f}{ml(m0):7.2f}{mb(m0):7.2f}{ms(m0):7.2f}{md(m0):7.2f}"
              f"{pulse_duration(m0):11.3f}   "
              f"{(ml(m0) - mw):+.2f} {(mb(m0) - mw):+.2f} "
              f"{(ms(m0) - mw):+.2f} {(md(m0) - mw):+.2f}")
    print()
    print("  Read the difference block row by row.  All five scales agree exactly")
    print("  at the calibration event by construction.  Away from it they separate,")
    print("  and the sign of the separation depends on the band:")
    print("    * ml and mb are set by bands SHORTER than the corner period of small")
    print("      events, so they grow faster than Mw there and then flatten;")
    print("    * Ms is set by a band LONGER than the corner period of small events,")
    print("      so it sits on the flat part and grows as (3/2) Mw, then flattens;")
    print("    * M_d follows Mw to a few hundredths at every size in this model.")
    print("  A catalogue that mixes these scales is mixing different measurements.")

    section("4. Measured slopes d(scale)/d(Mw)")
    mw = np.array([moment_magnitude(m0) for m0 in m0s])
    n3 = len(m0s) // 3
    print(f"  {len(m0s)} events split into thirds of {n3}; slope measured by least")
    print("  squares within each third.")
    print()
    print(f"  {'scale':>8}{'slope, first third':>21}{'middle third':>15}"
          f"{'last third':>13}{'last Mw bin':>15}")
    for name, fn in (("ml", ml), ("mb", mb), ("Ms", ms), ("M_d", md)):
        vals = np.array([fn(m0) for m0 in m0s])
        s1 = np.polyfit(mw[:n3], vals[:n3], 1)[0]
        s2 = np.polyfit(mw[n3:2 * n3], vals[n3:2 * n3], 1)[0]
        s3 = np.polyfit(mw[2 * n3:], vals[2 * n3:], 1)[0]
        print(f"  {name:>8}{s1:21.3f}{s2:15.3f}{s3:13.3f}"
              f"{mw[-1] - mw[2 * n3]:15.1f}")
    print(f"  {'Mw':>8}{1.0:21.3f}{1.0:15.3f}{1.0:13.3f}{'--':>15}")
    print()
    print("  A slope of 1 means the scale grows with the event exactly as Mw does,")
    print("  so it can stand in for Mw.  A slope near 0.5 in the last third is the")
    print("  signature of a measurement sitting on the f^-2 branch: it still grows,")
    print("  but as M0^(1/3), i.e. half as fast in Mw.  That is saturation, and it")
    print("  is a property of the BAND, not of the earthquake.")
    print()
    print("  Two honest limits of this model, both visible in the table.  First, a")
    print("  point source has no finite-fault effect, so the surface-wave column")
    print("  here saturates only when the 20 s band finally falls below fc (near the")
    print("  largest events); the familiar Ms saturation of great earthquakes is")
    print("  also driven by source duration exceeding the wave period, which needs a")
    print("  finite fault to model.  Second, a real scale is calibrated over a")
    print("  distance range, not at one distance, so its constants differ from the")
    print("  internal ones used here.")
    print()
    print("=" * 72)
    print("Source family, attenuation, bands and every calibration constant are")
    print("SYNTHETIC teaching values.  Mw uses the standard definition with")
    print("M0 in N m; no published magnitude correction is reproduced.")
    print("=" * 72)


if __name__ == "__main__":
    main()
