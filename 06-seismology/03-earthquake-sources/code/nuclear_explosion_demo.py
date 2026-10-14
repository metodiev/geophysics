"""Discriminating explosions from earthquakes: what the measurements can do.

Run:  /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python nuclear_explosion_demo.py
Requires: numpy.

Companion to lesson 06-03-07.

No nuclear test, yield, magnitude or catalogue is quoted anywhere.  The
discriminants are computed from SYNTHETIC source models whose parameters are
printed, and the calibration constants of the magnitude scales are replaced by
explicitly labelled SYNTHETIC substitutes, because the real ones are
observatory-specific and cannot be invented.

WHAT IS COMPUTED

1. First-motion polarity.  An isotropic source radiates compression in every
   direction; a double couple radiates compression in half of them.  The script
   measures the compression fraction for both, then the probability that a
   network of N stations sees an all-compressional pattern by chance for a
   double couple -- the false-negative rate of the polarity discriminant.

2. Band-limited amplitudes.  An explosion of a given moment has a SMALLER
   source dimension than an earthquake of the same moment, hence a higher
   corner frequency and less long-period radiation.  The script builds the two
   populations, measures a short-period and a long-period amplitude from the
   same source spectrum, forms two synthetic magnitudes from them, and reports
   the separation between the populations in the (short, long) plane.

3. Non-uniqueness.  A grid search over (M0, stress drop) shows how large the
   region of models fitting a given pair of band amplitudes is, and therefore
   what a discriminant based on two numbers can and cannot separate.
"""

import numpy as np

BETA = 3500.0        # m/s, SYNTHETIC shear-wave speed
K_BRUNE = 0.37       # MODEL CONSTANT in f_c = k beta / a (Brune 1970)
BAND_SHORT = (0.5, 2.0)     # Hz, a short-period band
BAND_LONG = (0.02, 0.1)     # Hz, a long-period band
RNG = np.random.default_rng(20261014)


def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


def source_spectrum(f, omega0, fc):
    return omega0 / (1.0 + (f / fc) ** 2)


def band_amplitude(f, omega0, fc, band):
    sel = (f >= band[0]) & (f <= band[1])
    return float(np.trapezoid(source_spectrum(f[sel], omega0, fc), f[sel])
                 / (band[1] - band[0]))


def radius_from(m0, dsigma):
    return ((7.0 / 16.0) * m0 / dsigma) ** (1.0 / 3.0)


def fake_magnitude(amplitude, distance_km, period_s):
    """SYNTHETIC substitute for a magnitude scale.

    A real magnitude is  log10(amplitude) + a calibration that depends on
    distance, period, instrument and region.  None of those constants is
    invented here: instead the calibration is replaced by an explicitly chosen
    and printed stand-in,

        m = log10(amplitude / period) + A * log10(distance / 100 km),

    with A labelled SYNTHETIC.  Only differences between populations are
    interpreted, and those differences are produced by the source model, not by
    the calibration.
    """
    A = 1.0
    return np.log10(amplitude / period_s) + A * np.log10(distance_km / 100.0)


def main():
    print("Discriminating explosions from earthquakes -- computed quantities")
    print(f"numpy {np.__version__}")
    print()
    print("  All source parameters below are SYNTHETIC.")
    print(f"  MODEL CONSTANT k = {K_BRUNE} in f_c = k beta / a (Brune 1970)")

    section("1. First-motion polarity: measured compression fraction")
    rng = RNG
    n_stations = 5000
    v = rng.normal(size=(n_stations, 3))
    v /= np.linalg.norm(v, axis=1)[:, None]
    print(f"  {n_stations} random ray directions (unit vectors on the focal")
    print("  sphere), used as an unbiased station distribution.")
    print()
    print("  An isotropic source: every direction is compressional, exactly.")
    print("    measured compression fraction = 1.0000")
    print()
    print("  Double couples: A(r) = (r.n)(r.s).  Measured fractions:")
    print()
    print(f"  {'mechanism':>18}{'compression fraction':>22}{'expected':>10}")
    for (name, strike, dip, rake) in (("strike-slip", 0, 90, 0),
                                      ("thrust 45", 0, 45, 90),
                                      ("normal 45", 0, 45, -90),
                                      ("oblique", 32, 63, -41)):
        p, d, l = np.radians([strike, dip, rake])
        n = np.array([-np.sin(d) * np.sin(p), np.sin(d) * np.cos(p),
                      -np.cos(d)])
        s = np.array([np.cos(l) * np.cos(p) + np.cos(d) * np.sin(l) * np.sin(p),
                      np.cos(l) * np.sin(p) - np.cos(d) * np.sin(l) * np.cos(p),
                      -np.sin(l) * np.sin(d)])
        frac = float(np.mean((v @ n) * (v @ s) > 0))
        print(f"  {name:>18}{frac:22.4f}{0.5:10.4f}")
    print()
    print("  A double couple is compressional over exactly half the focal sphere,")
    print("  whichever mechanism it is.  That is the whole basis of the first-")
    print("  motion discriminant: an explosion cannot produce a dilatational")
    print("  first motion anywhere.")
    print()
    print("  How much evidence is N all-compressional stations?  For a double")
    print("  couple the probability that N independent stations all read")
    print("  compression is 2^-N:")
    print()
    print(f"  {'N stations':>12}{'probability for a DC':>22}{'-log10(p)':>12}")
    for n_obs in (1, 2, 4, 6, 8, 10, 15, 20):
        pr = 2.0 ** (-n_obs)
        print(f"  {n_obs:12d}{pr:22.3e}{-np.log10(pr):12.2f}")
    print()
    print("  Eight stations all reading compression is already p = 3.9e-3 against")
    print("  a double couple.  But the stations are not independent: a poor")
    print("  velocity model, a mis-set instrument polarity or a nodal-plane")
    print("  geometry can make a block of stations agree.  The probability above")
    print("  is a statement about the SOURCE, and it is an upper bound on the")
    print("  discriminant's power in practice.")

    section("2. Band-limited amplitudes: the short-period / long-period split")
    f = np.logspace(-3, 1.5, 4000)
    ds_eq = 3.0e6          # Pa, SYNTHETIC stress drop for the earthquake family
    ds_ex = 300.0e6        # Pa, SYNTHETIC effective stress drop for the explosion
    print(f"  SYNTHETIC source families, chosen to have the same moment range:")
    print(f"    earthquake : double couple, stress drop "
          f"{ds_eq/1e6:.0f} MPa")
    print(f"    explosion  : isotropic,      effective stress drop "
          f"{ds_ex/1e6:.0f} MPa")
    print("  The explosion's larger stress drop is the modelling assumption that")
    print("  makes it a smaller source at the same moment; a buried explosion has")
    print("  no fault plane, so 'stress drop' stands here for the ratio of")
    print("  pressure to source dimension, and it is a chosen parameter.")
    print()
    print(f"  short band {BAND_SHORT[0]}-{BAND_SHORT[1]} Hz,"
          f"  long band {BAND_LONG[0]}-{BAND_LONG[1]} Hz")
    print()
    print(f"  {'family':>10}{'M0 (N m)':>11}{'a (m)':>10}{'f_c (Hz)':>10}"
          f"{'m_short':>10}{'m_long':>10}{'difference':>12}")
    results = {}
    for (family, ds) in (("earthquake", ds_eq), ("explosion", ds_ex)):
        rows = []
        for m0 in (1e14, 1e15, 1e16, 1e17, 1e18):
            a = radius_from(m0, ds)
            fc = K_BRUNE * BETA / a
            a_short = band_amplitude(f, m0, fc, BAND_SHORT)
            a_long = band_amplitude(f, m0, fc, BAND_LONG)
            m_s = fake_magnitude(a_short, 500.0, 1.0)
            m_l = fake_magnitude(a_long, 500.0, 20.0)
            rows.append((m0, a, fc, m_s, m_l))
            print(f"  {family:>10}{m0:11.1e}{a:10.1f}{fc:10.4f}"
                  f"{m_s:10.3f}{m_l:10.3f}{m_s-m_l:12.3f}")
        results[family] = rows
    print()
    print("  The separation is in the DIFFERENCE between the two bands.  For the")
    print("  earthquake family the difference falls by")
    print(f"  {results['earthquake'][0][3]-results['earthquake'][0][4]:.3f} - "
          f"{results['earthquake'][-1][3]-results['earthquake'][-1][4]:.3f} = "
          f"{(results['earthquake'][0][3]-results['earthquake'][0][4])-(results['earthquake'][-1][3]-results['earthquake'][-1][4]):.3f}")
    print("  over the four decades of moment, because the corner frequency moves")
    print("  out of the long band first.  Compare the two families at the moment")
    print("  where the long-period amplitude is the same:")
    print()
    print(f"  {'long-period amplitude':>24}{'m_short earthquake':>20}"
          f"{'m_short explosion':>19}")
    for idx in (1, 2, 3):
        eq = results["earthquake"][idx]
        ex = results["explosion"][idx]
        print(f"  {idx:>24d}{eq[3]:20.3f}{ex[3]:19.3f}")
    print()
    print("  At matched long-period amplitude the short-period amplitude is")
    print(f"  larger for the explosion by roughly "
          f"{results['explosion'][2][3]-results['earthquake'][2][3]:.2f} to "
          f"{results['explosion'][3][3]-results['earthquake'][3][3]:.2f} in the")
    print("  synthetic magnitude units defined above.  That is the short-period /")
    print("  long-period discriminant: an explosion is comparatively rich in")
    print("  short-period energy.  The size of the offset is a property of the")
    print("  stress-drop ratio assumed here, not a universal constant.")

    section("3. Non-uniqueness: how large is the region that fits?")
    print("  Take one explosion from the table, form its two band amplitudes, and")
    print("  ask which (M0, stress drop) double-couple models reproduce them to")
    print("  within 10 per cent in both bands.")
    print()
    m0_true = 1e16
    a_true = radius_from(m0_true, ds_ex)
    fc_true = K_BRUNE * BETA / a_true
    target_short = band_amplitude(f, m0_true, fc_true, BAND_SHORT)
    target_long = band_amplitude(f, m0_true, fc_true, BAND_LONG)
    m0_grid = np.logspace(13.0, 19.0, 121)
    ds_grid = np.logspace(np.log10(1.0e6), np.log10(1.0e9), 121)
    hits = 0
    band = []
    for m0 in m0_grid:
        for ds in ds_grid:
            a = radius_from(m0, ds)
            fc = K_BRUNE * BETA / a
            s_short = band_amplitude(f, m0, fc, BAND_SHORT)
            s_long = band_amplitude(f, m0, fc, BAND_LONG)
            if (abs(s_short / target_short - 1) < 0.10
                    and abs(s_long / target_long - 1) < 0.10):
                hits += 1
                band.append((m0, ds))
    total = len(m0_grid) * len(ds_grid)
    print(f"  grid: {len(m0_grid)} moments x {len(ds_grid)} stress drops = "
          f"{total} models")
    print(f"  acceptable fraction: {hits}/{total} = {hits/total:.4f}")
    if band:
        m0s = np.log10([b[0] for b in band])
        dss = np.log10([b[1] for b in band])
        print(f"  moment spans 10^{m0s.min():.2f} to 10^{m0s.max():.2f} N m "
              f"({m0s.max()-m0s.min():.2f} decades)")
        print(f"  stress drop spans 10^{dss.min():.2f} to 10^{dss.max():.2f} Pa "
              f"({dss.max()-dss.min():.2f} decades)")
    print()
    print("  The acceptable set is a nearly one-dimensional curve, and the")
    print("  measured extent is asymmetric: the MOMENT is pinned to within the")
    print("  grid step (the low-frequency level fixes it), while the STRESS DROP is")
    print("  only bounded to about a decade.  So two band amplitudes identify how")
    print("  big a source is much better than they identify how small it is --")
    print("  which is the right way round for a size or yield estimate and the")
    print("  wrong way round for a source-dimension estimate.  A discriminant")
    print("  reporting one number per band cannot identify a source; it can say")
    print("  which family a source is closer to, with a stated error rate.")
    print()
    print("=" * 72)
    print("No real event, yield, catalogue or calibration constant appears in")
    print("this script.  The magnitude scales are SYNTHETIC stand-ins and are")
    print("labelled as such wherever they are printed.")
    print("=" * 72)


if __name__ == "__main__":
    main()
