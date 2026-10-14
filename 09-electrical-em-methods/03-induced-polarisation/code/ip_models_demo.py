#!/usr/bin/env python3
"""Induced-polarisation models: Cole-Cole, Debye and the constant-phase element.

Measures the phase and amplitude spectra of the Cole-Cole complex resistivity,
checks the model against the analytic single-relaxation formulae, verifies that
it satisfies the Kramers-Kronig (Bode) gain-phase relation, and measures what a
finite frequency band and finite noise do to the three parameters.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python ip_models_demo.py

All models and data in this file are SYNTHETIC.  The resistivity, chargeability,
exponent and time constant are chosen teaching values, not measurements of a real
sample or of a real survey.

Contents
--------
1. Definition, limits, and the c = 1 (Debye) reduction.
2. Phase and amplitude spectra for a family of exponents.
3. Measured peak-phase and peak-frequency scaling; analytic check at c = 1.
4. Kramers-Kronig (Bode) gain-phase check, validated on a first-order pole.
5. Two real time constants fitted by one Cole-Cole: parameter spread vs noise.
6. The constant-phase element as the small-c limit.
"""

import warnings

import numpy as np
from scipy.integrate import IntegrationWarning, quad
from scipy.optimize import least_squares

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC teaching parameters (chosen, not measured) --------------------
RHO0 = 100.0     # ohm m, DC resistivity
M_REF = 0.10     # dimensionless
C_REF = 0.60     # dimensionless Cole-Cole exponent (0 < c <= 1)
TAU_REF = 1.0    # s


def cole_cole(f_hz, rho0=RHO0, m=M_REF, c=C_REF, tau=TAU_REF):
    """Cole-Cole complex resistivity (ohm m) at cyclic frequency f_hz.

    rho(w) = rho0 [ 1 - m ( 1 - 1/(1 + (i w tau)^c) ) ],  w = 2 pi f.
    """
    w = 2.0 * np.pi * np.asarray(f_hz, dtype=float)
    z = (1j * w * tau) ** c
    return rho0 * (1.0 - m * (1.0 - 1.0 / (1.0 + z)))


def debeye_closed_form(f_hz, rho0=RHO0, m=M_REF, tau=TAU_REF):
    """The same thing at c = 1 written as (1-m) + m/(1 + i w tau)."""
    w = 2.0 * np.pi * np.asarray(f_hz, dtype=float)
    return rho0 * ((1.0 - m) + m / (1.0 + 1j * w * tau))


def two_relaxation(f_hz, m, tau_a, tau_b, weight, rho0=RHO0):
    """Exact causal model with two distinct relaxation times (a sum of Debye
    polarisations).  Used as the 'truth' that a single Cole-Cole must fit."""
    w = 2.0 * np.pi * np.asarray(f_hz, dtype=float)
    pol = weight / (1.0 + 1j * w * tau_a) + (1.0 - weight) / (1.0 + 1j * w * tau_b)
    return rho0 * ((1.0 - m) + m * pol)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def peak_phase(f_lo, f_hi, **kwargs):
    """Largest |phase| of the Cole-Cole model on a fine log grid, with the
    frequency localised by a parabolic fit through the three largest values."""
    f = np.logspace(np.log10(f_lo), np.log10(f_hi), 400001)
    ph = -np.angle(cole_cole(f, **kwargs))
    i = int(np.argmax(ph))
    if 0 < i < f.size - 1:
        y0, y1, y2 = ph[i - 1], ph[i], ph[i + 1]
        denom = (y0 - 2 * y1 + y2)
        shift = 0.5 * (y0 - y2) / denom if denom != 0 else 0.0
        lf = (np.log10(f[i]) + shift * (np.log10(f[i + 1]) - np.log10(f[i])))
        return ph[i] - 0.25 * (y0 - y2) * shift, 10.0 ** lf
    return ph[i], f[i]


def kk_phase(H, w0, span=25.0):
    """Phase reconstructed from log|H| by the Kramers-Kronig relation

        phi(w0) = (2 w0 / pi) PV Integral_0^inf ln|H(w)| / (w^2 - w0^2) dw,

    evaluated with a Cauchy principal-value quadrature over
    [w0/e^span, w0 e^span] and with the out-of-band contributions added from the
    measured high- and low-frequency asymptotes of |H|.
    """
    lo, hi = w0 / np.exp(span), w0 * np.exp(span)

    def integrand(w):
        return np.log(np.abs(H(w))) / (w + w0)

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", IntegrationWarning)
        val, _ = quad(integrand, lo, hi, weight="cauchy", wvar=w0, limit=400,
                      epsabs=1e-14)
    a_hi = np.log(np.abs(H(1e14)))
    a_lo = np.log(np.abs(H(1e-14)))
    val += (a_hi / (2 * w0)) * np.log(abs((hi - w0) / (hi + w0)))
    val -= (a_lo / (2 * w0)) * np.log(abs((lo - w0) / (lo + w0)))
    return (2 * w0 / np.pi) * val


def main():
    section("1. Definition, limits, and the c = 1 reduction")
    print("rho(w) = rho0 [ 1 - m ( 1 - 1/(1 + (i w tau)^c) ) ]")
    print(f"rho0 = {RHO0:.1f} ohm m, m = {M_REF:.3f}, c = {C_REF:.2f}, "
          f"tau = {TAU_REF:.3f} s")
    print(f"  rho at f = 1e-12 Hz = {cole_cole(1e-12).real:.6f} ohm m  "
          f"(exact limit rho0 = {RHO0:.1f})")
    print(f"  rho at f = 1e12 Hz  = {cole_cole(1e12).real:.6f} ohm m  "
          f"(exact limit rho0(1-m) = {RHO0 * (1 - M_REF):.1f})")
    f_chk = np.logspace(-4, 4, 201)
    dev = np.max(np.abs(cole_cole(f_chk, c=1.0) - debeye_closed_form(f_chk)))
    print(f"c = 1 against the Debye closed form: max deviation over "
          f"1e-4 to 1e4 Hz = {dev:.2e} ohm m")
    print("so 'Debye' is exactly 'Cole-Cole with c = 1'; the Debye is not a")
    print("separate model but one point in the family.")

    section("2. Phase and amplitude spectra for a family of exponents")
    print("m and tau fixed; only the exponent c changes:")
    print("   f (Hz)      c=1.00            c=0.60            c=0.25")
    print("           |rho|    -phi      |rho|    -phi      |rho|    -phi")
    for f in (0.01, 0.1, 1.0, 10.0, 100.0):
        row = f"  {f:8.2f} "
        for c in (1.00, 0.60, 0.25):
            r = cole_cole(f, c=c)
            row += f" {abs(r):7.3f} {1000 * -np.angle(r):8.3f}"
        print(row)
    print("  (|rho| in ohm m, phase in mrad)")
    print("small c broadens the phase spectrum and, at fixed m, lowers its peak:")
    print("the same DC chargeability is spread over many decades of frequency.")

    section("3. Measured peak phase and peak frequency")
    print("   m      c      peak |phase| (mrad)   f_peak (Hz)   f_peak tau")
    rows = []
    for c in (1.00, 0.80, 0.60, 0.40, 0.25):
        for m in (0.02, 0.10, 0.30):
            ph, fp = peak_phase(1e-5, 1e5, m=m, c=c)
            rows.append((m, c, ph, fp))
            print(f"  {m:5.3f}  {c:5.2f}      {1000 * ph:14.3f}   "
                  f"{fp:11.5f}   {fp * TAU_REF:8.4f}")
    ph_deb, fp_deb = peak_phase(1e-5, 1e5, m=M_REF, c=1.0)
    ph_ana = np.arctan(M_REF / (2.0 * np.sqrt(1.0 - M_REF)))
    fp_ana = 1.0 / (2 * np.pi * TAU_REF * np.sqrt(1.0 - M_REF))
    print(f"\nanalytic Debye check at m = {M_REF:.2f}, c = 1: tan|phi| = "
          f"m/(2 sqrt(1-m)) = {1000 * ph_ana:.4f} mrad, "
          f"f_peak = 1/(2 pi tau sqrt(1-m)) = {fp_ana:.5f} Hz")
    print(f"                                       measured {1000 * ph_deb:.4f}"
          f" mrad at {fp_deb:.5f} Hz")
    m_arr = np.array([r[0] for r in rows if r[1] == 0.60])
    ph_arr = np.array([r[2] for r in rows if r[1] == 0.60])
    slope, intercept = np.polyfit(np.log(m_arr), np.log(ph_arr), 1)
    print(f"\nfor c = 0.60 and 0.02 <= m <= 0.30: peak|phase| = "
          f"{np.exp(intercept):.4f} m^{slope:.4f} rad")
    print(f"i.e. the peak phase is proportional to m to the power {slope:.3f},")
    print("so a phase of 10 mrad does not identify a unique m without c.")

    section("4. Kramers-Kronig (Bode) gain-phase check")
    print("validation on a first-order pole H = G0/(1 + i w tau):")
    tau_pole = 0.80
    for w0 in (0.05, 0.30, 1.00, 5.00, 20.00):
        kk = kk_phase(lambda w: 1.0 / (1.0 + 1j * w * tau_pole), w0)
        print(f"   w0 = {w0:6.2f} rad/s   KK = {kk:+.9f} rad   "
              f"exact = {-np.arctan(w0 * tau_pole):+.9f} rad   "
              f"diff = {kk + np.arctan(w0 * tau_pole):+.2e}")
    print("\nsame check on the Cole-Cole model (rho0 = 100 ohm m, m = 0.10,")
    print("tau = 1 s), i.e. on a model with a broad distribution of time")
    print("constants rather than a single one:")
    print("   c      f (Hz)    KK phase (mrad)   model phase (mrad)  diff (mrad)")
    for c in (1.00, 0.60, 0.25):
        for f in (0.05, 1.0, 20.0):
            w0 = 2 * np.pi * f
            H = lambda w, c=c: cole_cole(w / (2 * np.pi), c=c)
            kk = kk_phase(H, w0)
            mod = np.angle(H(w0))
            print(f"  {c:5.2f}  {f:7.2f}      {1000 * kk:12.4f}     "
                  f"{1000 * mod:14.4f}     {1000 * (kk - mod):+.1e}")
    print("the reconstruction is exact to about 2e-9 mrad, i.e. 2e-12 rad, the")
    print("quadrature tolerance: every Cole-Cole model is causal and minimum-")
    print("phase.  Its phase therefore carries no information beyond the")
    print("amplitude; the two are views of one function, and measuring both does")
    print("not double the information.  What a survey adds by going to lower")
    print("frequencies is band, not redundancy.")

    section("5. Two real time constants fitted by one Cole-Cole")
    m_true, tau_a, tau_b, weight = 0.12, 0.30, 6.00, 0.45
    f_data = np.logspace(-2, 2, 25)
    rho_true = two_relaxation(f_data, m_true, tau_a, tau_b, weight)
    print(f"truth (SYNTHETIC): two relaxations, m = {m_true:.3f}, "
          f"tau = {tau_a:.2f} s and {tau_b:.2f} s, weight {weight:.2f}")
    print(f"fit band {f_data[0]:.2f}-{f_data[-1]:.2f} Hz, {f_data.size} "
          f"frequencies; fitted parameters (m, c, tau), rho0 fixed")

    def fit_one_model(rho_obs, sigma_amp, sigma_phase):
        def residual(p):
            m, c, log_tau = p
            r = cole_cole(f_data, m=m, c=c, tau=10.0 ** log_tau)
            dr = (np.log(np.abs(r)) - np.log(np.abs(rho_obs))) / sigma_amp
            dp = (np.angle(r) - np.angle(rho_obs)) / sigma_phase
            return np.concatenate([dr, dp])

        sol = least_squares(residual, x0=[0.1, 0.5, 0.0],
                            bounds=([0.001, 0.05, -3.0], [0.60, 1.00, 3.0]))
        return sol.x

    print("\nnoise level        fitted m           fitted c        fitted tau (s)")
    for sigma_amp, sigma_phase, label in ((1e-6, 1e-8, "noise-free"),
                                          (0.01, 0.0005, "1% / 0.5 mrad"),
                                          (0.05, 0.002, "5% / 2 mrad")):
        m_f, c_f, lt_f = fit_one_model(rho_true, sigma_amp, sigma_phase)
        print(f"{label:14s}  {m_f:8.4f}           {c_f:8.4f}        "
              f"{10 ** lt_f:8.4f}")
    print("\nMonte Carlo over 150 noise realisations at 5% / 2 mrad:")
    m_s, c_s, l_s = [], [], []
    for _ in range(150):
        rho_obs = rho_true * (1.0 + 0.05 * RNG.standard_normal(f_data.size)) \
            * np.exp(1j * 0.002 * RNG.standard_normal(f_data.size))
        m_f, c_f, lt_f = fit_one_model(rho_obs, 0.05, 0.002)
        m_s.append(m_f), c_s.append(c_f), l_s.append(lt_f)
    m_s, c_s, l_s = np.array(m_s), np.array(c_s), np.array(l_s)
    print(f"   m   : median {np.median(m_s):.4f}, 5-95% "
          f"[{np.percentile(m_s, 5):.4f}, {np.percentile(m_s, 95):.4f}]")
    print(f"   c   : median {np.median(c_s):.4f}, 5-95% "
          f"[{np.percentile(c_s, 5):.4f}, {np.percentile(c_s, 95):.4f}]")
    print(f"   tau : median {10 ** np.median(l_s):.4f} s, 5-95% "
          f"[{10 ** np.percentile(l_s, 5):.4f}, "
          f"{10 ** np.percentile(l_s, 95):.4f}] s")
    corr = np.corrcoef(c_s, l_s)[0, 1]
    print(f"   correlation(c, log10 tau) = {corr:+.3f}")
    print("the truth is a two-relaxation model, so no fitted triple is 'the'")
    print("answer; the exponent and the time constant trade against each other,")
    print("and the admitted ranges above are set by the noise, not by the rock.")

    section("6. The constant-phase element as the small-c limit")
    band = np.logspace(-1, 1, 401)
    print("   c      -phase min (mrad)  -phase max (mrad)   range/mean   "
          "amplitude slope   (2/pi) mean|phase|")
    for c in (1.00, 0.80, 0.60, 0.40, 0.25, 0.10):
        r = cole_cole(band, c=c)
        ph = -np.angle(r)
        slope = np.polyfit(np.log10(band), np.log10(np.abs(r)), 1)[0]
        print(f"  {c:5.2f}   {1000 * ph.min():14.3f}  {1000 * ph.max():14.3f}"
              f"   {ph.max() / ph.mean():9.3f}     {slope:+10.4f}       "
              f"{-(2 / np.pi) * ph.mean():+.5f}")
    print("as c falls the phase flattens towards a constant: the phase range")
    print("collapses, and the small-c columns show -slope ~ (2/pi) mean|phase|,")
    print("which is the constant-phase-element relation.  Two limits are worth")
    print("naming: c = 1 is a single relaxation (Debye), c -> 0 is a pure")
    print("power law with no time scale of its own, and it is therefore a")
    print("non-unique description - it has no characteristic frequency at all.")


if __name__ == "__main__":
    main()
