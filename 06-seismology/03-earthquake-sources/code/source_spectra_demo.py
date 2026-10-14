"""Source spectra: the corner-frequency model, stress drop and scaling.

Run:  /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python source_spectra_demo.py
Requires: numpy.

Companion to lesson 06-03-05.

MODEL.  The far-field displacement amplitude spectrum of the Brune (1970,
1971) circular-crack model is

    u(f) = Omega0 / (1 + (f/f_c)^2) ,        Omega0 proportional to M0,

which is flat below the corner frequency f_c and falls as f^-2 above it.  The
velocity spectrum then rises as f below f_c and falls as f^-1 above it.  The
single free constant that links f_c to a physical length is written here as

    f_c = k * beta / a ,     a = crack radius, beta = shear speed,

with k a MODEL CONSTANT, not a measurement: it is O(1) and its value depends on
the assumed slip-velocity time function.  It is called K_BRUNE below and its
value is labelled as a model choice.  Everything that this lesson claims about
SCALING is independent of k; only the absolute stress drop depends on it.

The script

  1. builds spectra for nominal (M0, Delta_sigma) and MEASURES the corner
     frequency by locating the intersection of the low- and high-frequency
     asymptotes, comparing the measurement with the value used to build it;
  2. recovers the stress drop from the measured f_c and M0 using
     M0 = (16/7) Delta_sigma a^3 (Eshelby circular crack) and reports the
     error, so that the reader sees how the model constant propagates;
  3. generates a family of sources with CONSTANT stress drop and varying size
     and fits the exponent in M0 ~ f_c^p, recovering p = -3;
  4. does the same for constant M0 and varying stress drop, where f_c is
     independent of M0, which is the statement that f_c is not a size measure
     unless the stress drop is known or assumed;
  5. shows what a narrow-band measurement sees, which is the mechanism behind
     magnitude saturation in lesson 04-05.

All sources are SYNTHETIC with every input printed.
"""

import numpy as np

BETA = 3500.0          # m/s, SYNTHETIC shear-wave speed
MU = 3.0e10            # Pa, SYNTHETIC shear modulus
K_BRUNE = 0.37         # MODEL CONSTANT (Brune 1970); see the module note


def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


def spectre(f, omega0, fc):
    return omega0 / (1.0 + (f / fc) ** 2)


def measure_fc(f, amp):
    """Corner frequency from the intersection of the two asymptotes.

    The low-frequency asymptote is the first value (flat part); the
    high-frequency one is a straight line in log-log through the last decade.
    """
    logf = np.log10(f)
    loga = np.log10(amp)
    plateau = loga[0]
    # fit the highest decade
    mask = logf > logf[-1] - 1.0
    slope, intercept = np.polyfit(logf[mask], loga[mask], 1)
    # intersection of loga = plateau and loga = slope*logf + intercept
    logf_c = (plateau - intercept) / slope
    return 10.0 ** logf_c, slope


def stress_drop(m0, fc, beta=BETA, k=K_BRUNE, mu=MU):
    """Delta_sigma from M0 and f_c, using M0 = (16/7) dsigma a^3, f_c = k beta / a."""
    a = k * beta / fc
    return (7.0 / 16.0) * m0 / a ** 3


def source_parameters(m0, dsigma, beta=BETA, k=K_BRUNE, mu=MU):
    """Radius, corner frequency and mean slip for a circular crack."""
    a = ((7.0 / 16.0) * m0 / dsigma) ** (1.0 / 3.0)
    fc = k * beta / a
    slip = (16.0 / (7.0 * np.pi)) * (dsigma / mu) * a
    return a, fc, slip


def main():
    print("Source spectra, corner frequency and stress drop")
    print(f"numpy {np.__version__}")
    print()
    print("  SYNTHETIC material: beta = %.0f m/s, mu = %.3e Pa" % (BETA, MU))
    print(f"  MODEL CONSTANT k in f_c = k beta / a:  k = {K_BRUNE}  (Brune 1970;")
    print("  this is a model choice, and the literature uses values of order")
    print("  0.2 to 0.5 depending on the assumed slip time function -- it is NOT")
    print("  a measured number)")

    f = np.logspace(-4, 2.5, 6000)

    section("1. Measuring the corner frequency of a synthetic spectrum")
    print(f"  {'M0 (N m)':>11}{'dsigma (MPa)':>14}{'radius a (m)':>14}"
          f"{'f_c input (Hz)':>16}{'f_c measured (Hz)':>19}{'relative error':>16}")
    for (m0, ds) in ((1e17, 3e6), (1e19, 3e6), (1e21, 3e6), (1e19, 30e6)):
        a, fc_in, _ = source_parameters(m0, ds)
        amp = spectre(f, 1.0, fc_in)
        fc_out, slope = measure_fc(f, amp)
        print(f"  {m0:11.1e}{ds/1e6:14.1f}{a:14.1f}{fc_in:16.5f}{fc_out:19.5f}"
              f"{abs(fc_out-fc_in)/fc_in:15.4f}")
    print()
    print(f"  The fitted high-frequency slope is {slope:.4f} (the model is exactly")
    print("  -2.0), so the measurement is accurate to the fit window and the error")
    print("  column is the intersection method, not the model.")

    section("2. Recovering the stress drop, and how the model constant enters")
    print("  M0 = (16/7) dsigma a^3 is the Eshelby circular-crack relation; with")
    print("  a = k beta / f_c it becomes dsigma = (7/16) M0 (f_c / (k beta))^3.")
    print()
    m0_build, ds_true = 1.0e19, 3.0e6
    a_true, fc_build, _ = source_parameters(m0_build, ds_true)
    print(f"  built with M0 = {m0_build:.1e} N m, dsigma = {ds_true/1e6:.1f} MPa,")
    print(f"  k_build = {K_BRUNE}, giving a = {a_true:.1f} m and f_c = "
          f"{fc_build:.5f} Hz")
    print()
    print(f"  {'k used to invert':>18}{'dsigma out (MPa)':>18}{'ratio to true':>15}"
          f"{'error factor':>14}")
    for k in (0.20, K_BRUNE, 0.50):
        ds_out = stress_drop(m0_build, fc_build, k=k)
        print(f"  {k:18.2f}{ds_out/1e6:18.4f}{ds_out/ds_true:15.4f}"
              f"{ds_out/ds_true:14.4f}")
    print()
    print("  With the correct k the stress drop is recovered exactly (ratio 1.0")
    print("  to the print precision), and with a wrong k it is wrong in the THIRD")
    print("  power, because f_c = k beta / a enters cubed.  k = 0.20 against")
    print("  k = 0.37 is a factor 6.3 in the answer and both values are in the")
    print("  literature.  A stress drop quoted without stating k is therefore not")
    print("  a measurement of the Earth; it is a measurement of the Earth times a")
    print("  model constant that the author chose.")

    section("3. M0 against f_c at constant stress drop: the -3 exponent")
    print("  A family of self-similar circular ruptures with the same stress drop:")
    print()
    dsigma = 3.0e6
    radii = np.logspace(1.0, 4.0, 60)          # 10 m to 10 km
    fc = K_BRUNE * BETA / radii
    m0 = (16.0 / 7.0) * dsigma * radii ** 3
    slope, intercept = np.polyfit(np.log10(fc), np.log10(m0), 1)
    print(f"  measured exponent in M0 ~ f_c^p over {len(radii)} sources:"
          f"  p = {slope:.6f}")
    print("  predicted p = -3 exactly, because M0 ~ a^3 and f_c ~ 1/a.")
    print()
    print(f"  {'radius a (m)':>13}{'f_c (Hz)':>12}{'M0 (N m)':>13}"
          f"{'mean slip (m)':>15}")
    for a in (50.0, 500.0, 5000.0):
        _, fc_i, slip = source_parameters((16.0 / 7.0) * dsigma * a ** 3, dsigma)
        print(f"  {a:13.1f}{fc_i:12.5f}{(16.0/7.0)*dsigma*a**3:13.4e}{slip:15.4f}")
    print()
    print("  Note what is happening to the slip: it grows linearly with radius at")
    print("  constant stress drop.  A tenfold longer rupture means ten times the")
    print("  slip, a thousand times the moment, and a tenth of the corner")
    print("  frequency.  This is self-similarity, and it is the reason a single")
    print("  exponent describes the whole small-earthquake population.")

    section("4. The same M0 with different stress drops: f_c is not a size meter")
    print("  Fix the moment and vary the stress drop:")
    print()
    print(f"  {'dsigma (MPa)':>14}{'radius a (m)':>14}{'f_c (Hz)':>12}"
          f"{'M0 (N m)':>13}")
    m0_fixed = 1.0e19
    for ds in (0.3e6, 3e6, 30e6, 300e6):
        a, fc_i, _ = source_parameters(m0_fixed, ds)
        print(f"  {ds/1e6:14.2f}{a:14.1f}{fc_i:12.5f}{m0_fixed:13.4e}")
    print()
    print("  The moment is identical in all four rows and the corner frequency")
    print("  differs by a factor 10.  So a measured f_c alone does not give a size")
    print("  or a moment: it gives the ratio M0 / a^3, which is the stress drop")
    print("  (up to the model constant).  The pair (M0, f_c) determines the stress")
    print("  drop; neither alone determines the other.")

    section("5. Saturation from the finite bandwidth of the measurement")
    print("  Keep the stress drop fixed and let the source grow.  The low-")
    print("  frequency plateau grows with M0 and the corner frequency falls as")
    print("  M0^(-1/3).  A band placed BELOW f_c therefore tracks M0, while a band")
    print("  placed ABOVE f_c sees only the tail of the spectrum and tracks it")
    print("  more weakly.  Measuring the exponent is the whole of saturation.")
    print()
    f_low = (f >= 1e-4) & (f <= 1e-3)
    f_high = (f >= 2.0) & (f <= 10.0)
    ds = 3.0e6
    m0s = np.array([1e18, 1e19, 1e20, 1e21, 1e22, 1e23])
    a_low, a_high, fcs = [], [], []
    for m0 in m0s:
        a, fc_i, _ = source_parameters(m0, ds)
        fcs.append(fc_i)
        # spectrum scaled so that the low-frequency plateau is proportional to M0
        amp_low = np.trapezoid(spectre(f[f_low], m0, fc_i), f[f_low]) / (1e-3 - 1e-4)
        amp_high = np.trapezoid(spectre(f[f_high], m0, fc_i), f[f_high]) / (10.0 - 2.0)
        a_low.append(amp_low)
        a_high.append(amp_high)
    slope_low = np.polyfit(np.log10(m0s), np.log10(a_low), 1)[0]
    slope_high = np.polyfit(np.log10(m0s), np.log10(a_high), 1)[0]
    print(f"  {'M0 (N m)':>11}{'f_c (Hz)':>11}{'band 1e-4..1e-3 Hz':>20}"
          f"{'band 2..10 Hz':>17}")
    for i, m0 in enumerate(m0s):
        print(f"  {m0:11.1e}{fcs[i]:11.5f}{a_low[i]:20.4e}{a_high[i]:17.4e}")
    print()
    print(f"  measured d log10(amplitude) / d log10(M0):")
    print(f"    band below f_c : {slope_low:.6f}   (predicted 1)")
    print(f"    band above f_c : {slope_high:.6f}   (predicted 1/3)")
    print()
    print("  Both come out to the predicted values.  A magnitude defined from a")
    print("  band-limited amplitude is therefore a logarithmic measure of M0 in the")
    print("  low band, and of M0^(1/3) in the high band.  That is saturation: as")
    print("  the source grows, a fixed high-frequency band stops recording the")
    print("  growth.  The exponent 1/3 is measured here from a spectral model; in")
    print("  lesson 04-05 the same arithmetic is applied to the conventional")
    print("  magnitude scales, with the band edges of the instruments as inputs.")
    print()
    print("=" * 72)
    print("All sources SYNTHETIC.  The model constant k and the Eshelby factor")
    print("16/7 are labelled as model inputs; the exponent -3 and the")
    print("independence of f_c from M0 at fixed stress drop are derived, and")
    print("are what the script measures.")
    print("=" * 72)


if __name__ == "__main__":
    main()
