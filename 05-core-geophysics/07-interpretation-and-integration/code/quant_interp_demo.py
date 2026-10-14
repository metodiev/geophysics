"""Quantitative interpretation: depth estimation, and the errors it accumulates.

Five estimates of source depth are computed from the *same* synthetic profile,
using the methods a practitioner actually applies, so the spread between them is
visible rather than described:

  1. Half-width rule             -- model-dependent, exact if the shape is right.
  2. Nonlinear least-squares fit -- a point-mass model and a line-mass model.
  3. Fourier spectral depth      -- model-independent, needs a wide profile.
  4. Contact gradient half-width -- depth from the horizontal gradient.
  5. Sensitivity to a regional trend left in the data.

Every depth reported is compared with the depth used to generate the data, and
every error is stated as a percentage.  The final section demonstrates that
refining the *sampling* does not reduce the *shape* ambiguity: the wrong model
gives the same wrong depth for 61 and for 601 stations.

All source parameters, noise levels and trend coefficients are SYNTHETIC.  They
are not measurements, and no instrument specification is quoted as universal.

Run:  python3 quant_interp_demo.py
"""

from __future__ import annotations

import warnings

import numpy as np
from scipy.optimize import OptimizeWarning, curve_fit

warnings.simplefilter("ignore", OptimizeWarning)

G = 6.674e-11  # m^3 kg^-1 s^-2
MGAL = 1.0e-5  # m s^-2 per mGal


def section(title: str) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def model_point(x, m, x0, z, a, b):
    """Point mass at (x0, z) plus a linear regional, in SI (m/s^2)."""
    return G * m * z / np.power((x - x0) ** 2 + z * z, 1.5) + a + b * x


def model_line(x, lam, x0, z, a, b):
    """Infinite horizontal line mass at (x0, z) plus a linear regional."""
    return 2.0 * G * lam * z / ((x - x0) ** 2 + z * z) + a + b * x


def width_at(x, g, fraction):
    peak = g.max()
    i0 = int(np.argmax(g))
    xs, gs = x[i0:], g[i0:]
    target = fraction * peak
    below = np.nonzero(gs <= target)[0]
    j = below[0]
    t = (gs[j - 1] - target) / (gs[j - 1] - gs[j])
    return float(xs[j - 1] + t * (xs[j] - xs[j - 1]))


def main() -> None:
    rng = np.random.default_rng(20261014)
    z_true = 500.0                       # SYNTHETIC depth to source centre, m
    m_true = 1.0e10                      # SYNTHETIC point mass, kg
    sigma = 0.02 * MGAL                  # SYNTHETIC noise, mGal -> SI

    x = np.linspace(-3000.0, 3000.0, 601)
    g_clean = model_point(x, m_true, 0.0, z_true, 0.0, 0.0)
    g = g_clean + rng.normal(0.0, sigma, x.size)

    section("1. Half-width rule, with the correct shape assumed")
    w_half = width_at(x, g_clean, 0.5)
    print(f"half-width                         = {w_half:8.2f} m")
    print(f"depth from point-mass rule (1.3048)= {1.30477 * w_half:8.2f} m")
    print(f"depth from line-mass rule  (1.0)   = {w_half:8.2f} m")
    print(f"true depth                         = {z_true:8.2f} m")
    print(f"error from using the wrong rule    = "
          f"{100 * (w_half - z_true) / z_true:8.2f} per cent")

    section("2. Nonlinear least-squares fits, both models, with noise")
    for name, fn, p0 in (("point mass", model_point, [1e10, 0.0, 500.0, 0.0, 0.0]),
                         ("line mass", model_line, [1e9, 0.0, 500.0, 0.0, 0.0])):
        popt, pcov = curve_fit(fn, x, g, p0=p0, maxfev=20000)
        z = popt[2]
        z_err = np.sqrt(pcov[2, 2])
        resid = np.sqrt(np.mean((fn(x, *popt) - g) ** 2)) / MGAL
        print(f"{name:11s} recovered depth = {z:8.2f} +/- {z_err:6.2f} m "
              f"({100 * (z - z_true) / z_true:7.2f} per cent), RMS {resid:.4f} mGal")
    print("The line-mass fit is as good by RMS as the point-mass fit: the residual "
          "does\nnot tell you which model is right, and the two models disagree on "
          "depth by\nabout 26 per cent -- from identical data that both fit to "
          "0.02 mGal RMS.")

    section("3. Fourier spectral depth: exact for 2-D sources, biased for 3-D")
    for label, fn, shape in (("line mass", model_line, 2), ("point mass", model_point, 3)):
        for half_length in (3000.0, 15000.0):
            xf = np.linspace(-half_length, half_length, 4 * int(half_length / 10) + 1)
            gf = fn(xf, 1.0e10 if shape == 3 else 1.0e10, 0.0, z_true, 0.0, 0.0)
            win = np.hanning(xf.size)
            dx = xf[1] - xf[0]
            amp = np.abs(np.fft.rfft((gf - gf.mean()) * win) * dx)
            k = 2.0 * np.pi * np.fft.rfftfreq(xf.size, dx)
            band = (k * z_true > 2.0) & (k * z_true < 8.0)
            slope = float(np.polyfit(k[band], np.log(amp[band]), 1)[0])
            print(f"{label:11s} {2 * half_length / 1000:5.0f} km: kz "
                  f"{k[band].min() * z_true:.1f}-{k[band].max() * z_true:.1f}, "
                  f"implied depth {-slope:7.2f} m "
                  f"({100 * (-slope - z_true) / z_true:+7.2f} per cent)")
    print("For a 2-D (line) source the profile spectrum is exactly proportional to\n"
          "exp(-k z), so the slope is the depth to 0.01 per cent.  For a 3-D "
          "(point) source\nthe profile spectrum is proportional to k K1(k z), so "
          "the slope rule is only\nasymptotic: over the band kz = 2 to 8 measured "
          "here the depth is biased shallow\nby about 10 per cent, and the bias "
          "grows as the band moves to smaller kz.  It is\nnot noise and not window "
          "length -- it is the wrong spectral model.")

    section("4. Depth from a contact's horizontal gradient")
    for z_contact in (100.0, 300.0):
        xs = np.linspace(-2000.0, 2000.0, 40001)
        grad = 2.0 * 1.0e-3 * (z_contact / (xs * xs + z_contact * z_contact))
        hw = width_at(xs, grad, 0.5)
        print(f"true depth {z_contact:6.0f} m -> gradient half-width {hw:8.2f} m "
              f"({100 * (hw - z_contact) / z_contact:+5.2f} per cent)")

    section("5. Depth error from an unremoved regional trend")
    a_reg, b_reg = 0.30 * MGAL, 1.0e-4 * MGAL      # SYNTHETIC, mGal -> SI
    x2 = np.linspace(-5000.0, 5000.0, 1001)
    g_reg = model_point(x2, m_true, 0.0, z_true, a_reg, b_reg)
    g_reg += rng.normal(0.0, sigma, x2.size)

    popt_full, _ = curve_fit(model_point, x2, g_reg,
                             p0=[1e10, 0.0, 400.0, 0.0, 0.0], maxfev=20000)
    popt_noslope, _ = curve_fit(lambda xx, m, x0, z, a: model_point(xx, m, x0, z, a, 0.0),
                                x2, g_reg, p0=[1e10, 0.0, 400.0, 0.0], maxfev=20000)
    wings = np.abs(x2) > 3.0 * z_true
    detrend_coef = np.polyfit(x2[wings], g_reg[wings], 1)
    g_detrended = g_reg - np.polyval(detrend_coef, x2)
    popt_det, _ = curve_fit(lambda xx, m, x0, z, a: model_point(xx, m, x0, z, a, 0.0),
                            x2, g_detrended, p0=[1e10, 0.0, 400.0, 0.0], maxfev=20000)
    print(f"fit with a trend term       -> depth {popt_full[2]:9.2f} m "
          f"({100 * (popt_full[2] - z_true) / z_true:+8.2f} per cent)")
    print(f"detrended on the wings first-> depth {popt_det[2]:9.2f} m "
          f"({100 * (popt_det[2] - z_true) / z_true:+8.2f} per cent)")
    print(f"fit with a constant only    -> depth {popt_noslope[2]:9.2f} m "
          f"({100 * (popt_noslope[2] - z_true) / z_true:+8.2f} per cent)")
    print(f"trend actually present       = {a_reg / MGAL:.2f} mGal + "
          f"{b_reg / MGAL:.1e} (mGal/m) x")
    rms_noslope = float(np.sqrt(np.mean(
        (model_point(x2, *popt_noslope, 0.0) - g_reg) ** 2)) / MGAL)
    print(f"RMS of the constant-only fit = {rms_noslope:.4f} mGal")
    print("A 0.30 mGal offset and a 0.1 mGal/km slope, both comparable with the "
          "0.27 mGal\nanomaly, drive the constant-only depth estimate to an "
          "unphysical 75 km -- and\nits RMS residual is still small.  A small "
          "residual is not evidence that a model\nis right.  Removing the trend, "
          "either as a fitted term or on the wings,\nrecovers the depth to a few "
          "per cent.")

    section("6. Refining the sampling does not remove the shape ambiguity")
    for n in (61, 601, 6001):
        xs = np.linspace(-3000.0, 3000.0, n)
        gs = model_point(xs, m_true, 0.0, z_true, 0.0, 0.0)
        popt, _ = curve_fit(model_line, xs, gs, p0=[1e9, 0.0, 400.0, 0.0, 0.0],
                            maxfev=20000)
        print(f"{n:5d} stations -> line-mass depth {popt[2]:8.2f} m "
              f"({100 * (popt[2] - z_true) / z_true:+5.2f} per cent)")
    print("The wrong model is wrong by the same amount at every sampling: the "
          "ambiguity\nis in the physics, not in the data density.")


if __name__ == "__main__":
    main()
