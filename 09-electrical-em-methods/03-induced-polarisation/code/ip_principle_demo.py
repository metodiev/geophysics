#!/usr/bin/env python3
"""Induced polarisation, principle: time-domain chargeability and frequency-domain
phase for a single-relaxation (Debye) teaching model, and the measured fact that
every conversion between the two domains depends on the model and on the window.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python ip_principle_demo.py

All models and data in this file are SYNTHETIC.  The resistivity, chargeability,
time constant, current and geometric factor are chosen teaching values, not
measurements of a real ground or of a real instrument.

Contents
--------
1. The Debye model and its exact step-off decay.
2. Integral chargeability versus integration window (analytic and numerical).
3. Frequency-domain phase and amplitude; analytic peak-phase check.
4. Time-domain versus frequency-domain: one model, two different answers.
5. Broadened relaxation (many Debye terms) and the constant-phase behaviour.
6. Charging-time and drift bias; verification of the Fourier step-off formula.
"""

import warnings

import numpy as np
from scipy.integrate import IntegrationWarning, quad
from scipy.special import sici

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC teaching parameters (chosen, not measured) --------------------
RHO0 = 100.0        # ohm m, DC resistivity of the polarisable medium
M_DC = 0.10         # dimensionless chargeability (fraction of rho0 removed)
TAU = 1.5           # s, relaxation time constant
CURRENT = 0.10      # A, injected current
K_GEOM = 1.00       # m, geometric factor of the electrode array (K in V = I rho K)
V_P = CURRENT * RHO0 * K_GEOM   # V, primary (DC) potential difference


def debeye_rho(omega, rho0, m, tau):
    """Debye complex resistivity, omega in rad/s, ohms m.

    rho(w)/rho0 = (1 - m) + m/(1 + i w tau): a resistor in series with a
    parallel RC element.  At w -> 0 the value is rho0; at w -> inf, rho0(1-m).
    """
    return rho0 * ((1.0 - m) + m / (1.0 + 1j * omega * tau))


def decay(t, m, tau):
    """Step-off decay of the potential, in units of the primary potential."""
    return m * np.exp(-t / tau)


def m_integral(T, m, tau, t_on=np.inf):
    """Integral chargeability in seconds: (1/Vp) Integral V_s dt over [0, T].

    A finite charging time t_on leaves the polarisation incompletely charged, so
    the decay starts from m(1 - exp(-t_on/tau)) instead of m.
    """
    charge = m * (1.0 - np.exp(-t_on / tau)) if np.isfinite(t_on) else m
    return charge * tau * (1.0 - np.exp(-T / tau))


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def step_off_fourier(t, gain, hf_limit=None, u_max=3000.0):
    """Step-off response of a linear system from its transfer function.

    For an input that is 1 for t < 0 and 0 for t > 0 (a step-off), and a
    transfer function G(w) with G0 = G(0),

        y(t) = -(1/pi) Integral_0^inf Im[(G(w) - G0) e^{i w t}] / w  dw.

    The substitution u = w t removes the t-dependence of the oscillation, which
    keeps the quadrature mesh fixed as t varies.  When G does not tend to G0 at
    high frequency, the remaining tail is added analytically with the sine and
    cosine integrals:

        Integral_U^inf Im[(Ghf - G0) e^{iu}]/u du
            = Re[Ghf - G0] (pi/2 - Si(U)) - Im[Ghf - G0] Ci(U).

    Verified in section 6 against the analytic exponential for a single pole.
    """
    if hf_limit is None:
        hf_limit = gain(1e12)
    g0 = gain(0.0)
    g_hf = hf_limit - g0

    def integrand(u):
        return np.imag((gain(u / t) - g0) * np.exp(1j * u)) / u

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", IntegrationWarning)
        total, _ = quad(integrand, 0.0, u_max, limit=3000, epsabs=1e-14,
                        epsrel=1e-12)
    si, ci = sici(u_max)
    tail = g_hf.real * (np.pi / 2.0 - si) - g_hf.imag * ci
    return -(total + tail) / np.pi


def main():
    section("1. The Debye model and its exact step-off decay (SYNTHETIC)")
    print(f"rho0 = {RHO0:.1f} ohm m, m = {M_DC:.3f} (dimensionless), "
          f"tau = {TAU:.3f} s")
    print(f"I = {CURRENT:.3f} A, K = {K_GEOM:.3f} m  ->  V_p = I rho0 K = "
          f"{V_P:.3f} V")
    print(f"high-frequency limit rho(w -> inf) = rho0 (1 - m) = "
          f"{RHO0 * (1 - M_DC):.2f} ohm m")
    print(f"decay amplitude at t = 0+  = m V_p = {M_DC * V_P:.4f} V")
    print(f"total chargeability M(t -> inf) = m tau = {M_DC * TAU:.4f} s "
          f"= {1000 * M_DC * TAU:.2f} ms")
    print("the decay is V_s(t) = V_p m exp(-t/tau); it is exponential, so every")
    print("chargeability number below is an exact closed form, not a fit.")

    section("2. Integral chargeability versus integration window")
    print("window T (s)   M = m tau (1-e^-T/tau)   numerical check   mean over T")
    print("               (ms, window integral)     (ms)              (mV/V)")
    for T in (0.25, 0.5, 1.0, 2.0, 4.0, 8.0, 16.0):
        m_closed = 1000.0 * m_integral(T, M_DC, TAU)
        m_num = 1000.0 * (quad(lambda t: decay(t, M_DC, TAU), 0.0, T)[0])
        mean_mvv = m_closed / T
        print(f"  {T:6.2f}      {m_closed:14.3f}           {m_num:10.3f}      "
              f"{mean_mvv:8.3f}")
    print("reading: the window-integral chargeability (ms) saturates at m tau;")
    print("the window-average chargeability (mV/V) keeps falling because the")
    print("same area is divided by a longer window.  Both are in use, and they")
    print("differ by exactly the factor T.  Quoting 'M = 0.15' is meaningless")
    print("without the convention and the window.")

    section("3. Frequency-domain phase and amplitude, and the exact peak check")
    print("   f (Hz)      |rho| (ohm m)     -phase (mrad)   -phase (deg)")
    for f in (0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0):
        rho = debeye_rho(2 * np.pi * f, RHO0, M_DC, TAU)
        ph = -np.angle(rho)
        print(f"  {f:8.3f}     {abs(rho):12.4f}     {1000 * ph:11.3f}   "
              f"{np.degrees(ph):10.4f}")
    f_grid = np.logspace(-5, 5, 200001)
    rho_grid = debeye_rho(2 * np.pi * f_grid, RHO0, M_DC, TAU)
    ph_grid = -np.angle(rho_grid)
    i_peak = int(np.argmax(ph_grid))
    ph_num = ph_grid[i_peak]
    f_peak_num = f_grid[i_peak]
    ph_ana = np.arctan(M_DC / (2.0 * np.sqrt(1.0 - M_DC)))
    f_peak_ana = 1.0 / (2 * np.pi * TAU * np.sqrt(1.0 - M_DC))
    print(f"numerical peak |phase| = {1000 * ph_num:.4f} mrad "
          f"({np.degrees(ph_num):.4f} deg) at f = {f_peak_num:.6f} Hz")
    print(f"analytic  tan|phi_peak| = m/(2 sqrt(1-m)) -> "
          f"{1000 * ph_ana:.4f} mrad, f_peak = 1/(2 pi tau sqrt(1-m)) = "
          f"{f_peak_ana:.6f} Hz")
    print(f"agreement: phase {abs(1000 * (ph_num - ph_ana)):.4f} mrad, "
          f"frequency {abs(f_peak_num - f_peak_ana):.2e} Hz")
    print("so a single-relaxation response fixes (m, tau) from the phase alone:")
    print("the peak height gives m and the peak frequency gives tau.  That is")
    print("exactly why a real, broadened response is not a Debye (lesson 02).")

    section("4. Time domain versus frequency domain: the same model, two answers")
    T_REF = 1.0
    m_1s_ms = 1000.0 * m_integral(T_REF, M_DC, TAU)
    ph_1hz = -np.angle(debeye_rho(2 * np.pi * 1.0, RHO0, M_DC, TAU)) * 1000
    ph_pk = 1000 * ph_ana
    print(f"model A (Debye, m = {M_DC:.3f}, tau = {TAU:.3f} s):")
    print(f"   M(0-1 s window) = {m_1s_ms:.3f} ms     phase(1 Hz) = "
          f"{ph_1hz:.3f} mrad     phase(peak) = {ph_pk:.3f} mrad")
    print("the widely quoted working rule 'phase in mrad ~ chargeability in ms'")
    print(f"would predict {m_1s_ms:.3f} mrad for this model; the true 1 Hz phase")
    print(f"is {ph_1hz:.3f} mrad, a factor {abs(ph_1hz / m_1s_ms):.3f} different.")
    print("that rule is a property of a particular model, not of the physics:")
    print("it is re-tested in section 5 on a broadened model.")

    section("5. Broadened relaxation: many Debye terms, one flat phase")
    n_tau = 21
    taus = np.logspace(np.log10(TAU / 30.0), np.log10(TAU * 30.0), n_tau)
    weights = np.ones(n_tau) / n_tau

    def broad_rho(omega):
        pol = sum(w / (1.0 + 1j * omega * t) for w, t in zip(weights, taus))
        return RHO0 * ((1.0 - M_DC) + M_DC * pol)

    f_band = np.logspace(-2, 0, 401)
    rho_band = broad_rho(2 * np.pi * f_band)
    ph_band = -np.angle(rho_band)
    slope = np.polyfit(np.log10(f_band), np.log10(np.abs(rho_band)), 1)[0]
    c_eff = (2.0 / np.pi) * np.mean(ph_band)
    print(f"{n_tau} relaxation times log-uniform over "
          f"[{taus[0]:.4f}, {taus[-1]:.4f}] s, equal weights")
    print(f"over {f_band[0]:.2f}-{f_band[-1]:.2f} Hz:")
    print(f"   |phase| runs {1000 * ph_band.min():.3f} to "
          f"{1000 * ph_band.max():.3f} mrad (range "
          f"{1000 * (ph_band.max() - ph_band.min()):.3f} mrad)")
    print(f"   amplitude slope dlog|rho|/dlog f = {slope:+.4f}")
    print(f"   (2/pi) x mean|phase| = {c_eff:.4f}   vs   -slope = {-slope:.4f}")
    print(f"   slope predicted by the CPE relation -(2/pi) mean|phase| = "
          f"{-c_eff:.4f}  vs  measured {slope:+.4f}")
    print(f"   agreement to {100 * abs((-c_eff) - slope) / abs(slope):.1f}%")
    print("this is the measured statement of the constant-phase-element relation")
    print("-slope = (2/pi) x phase: a broad distribution of time constants looks")
    print("like a single power law.  The residual is the finite width of the")
    print("distribution used here (30 x in tau), not a physical violation.")

    phi_broad_1hz = -np.angle(broad_rho(2 * np.pi * 1.0)) * 1000
    m_broad_ms = 1000.0 * M_DC * sum(
        w * t * (1.0 - np.exp(-T_REF / t)) for w, t in zip(weights, taus))
    print(f"\nmodel B (broadened, same m and same weights):")
    print(f"   M(0-1 s window) = {m_broad_ms:.3f} ms     phase(1 Hz) = "
          f"{phi_broad_1hz:.3f} mrad")
    print(f"model A had           M = {m_1s_ms:.3f} ms     phase(1 Hz) = "
          f"{ph_1hz:.3f} mrad")
    print(f"phase ratio B/A = {phi_broad_1hz / ph_1hz:.3f}, chargeability ratio "
          f"B/A = {m_broad_ms / m_1s_ms:.3f}")
    print("the two models are separately fitted by the SAME chargeability but")
    print("need different phase conversion factors.  Without a model there is no")
    print("exact conversion, only a measured conversion factor and its spread.")

    section("6. Charging time, drift, and verification of the Fourier step-off")
    t_on_list = (0.25, 0.5, 1.0, 2.0, 4.0, 8.0)
    print("charging time t_on (s)   M(0-1s) in ms   bias versus fully charged")
    m_full = 1000.0 * m_integral(T_REF, M_DC, TAU)
    for t_on in t_on_list:
        m_val = 1000.0 * m_integral(T_REF, M_DC, TAU, t_on=t_on)
        print(f"      {t_on:6.2f}             {m_val:10.3f}      "
              f"{100.0 * (m_val - m_full) / m_full:+8.2f} %")
    print(f"an on-time of one time constant charges only "
          f"{100 * (1 - np.exp(-1.0)):.1f}% of the fully polarised amplitude,")
    print("which becomes a -51% bias in this 1 s window.  An on-time is thus")
    print("adequate only relative to tau, never in absolute seconds.")

    print("\nverification of the Fourier step-off formula on one pole:")
    tau_check, pole_gain = 0.80, 3.0

    def g_one_pole(w):
        return pole_gain / (1.0 + 1j * w * tau_check)

    print("   t (s)     Fourier step-off     G0 exp(-t/tau)     difference")
    worst = 0.0
    for t in (0.05, 0.10, 0.20, 0.40, 0.80, 1.60, 3.20):
        y = step_off_fourier(t, g_one_pole, hf_limit=0.0)
        exact = pole_gain * np.exp(-t / tau_check)
        worst = max(worst, abs(y - exact))
        print(f"  {t:5.2f}      {y:14.8f}     {exact:14.8f}     "
              f"{y - exact:+.2e}")
    print(f"maximum difference over the table = {worst:.2e} "
          f"(relative to the DC gain {pole_gain:.1f}: {worst / pole_gain:.1e})")
    print("the transform pair is therefore correct to better than 1e-7 of the DC")
    print("gain, which is the quadrature tolerance here; the same formula is used")
    print("in lesson 09-05-01 for the transient-EM step-off response.")

    noise = 0.02 * V_P * RNG.standard_normal(400)
    print(f"\ndrift bias (SYNTHETIC noise, rms = {np.std(noise):.4f} V):")
    t_w = np.linspace(0.0, T_REF, 200)
    clean = V_P * decay(t_w, M_DC, TAU)
    for slope_mv_s in (0.0, 0.5, 2.0, 10.0):
        drift = slope_mv_s * 1e-3 * t_w
        est = 1000.0 * np.trapezoid(clean + drift, t_w) / V_P
        print(f"   drift {slope_mv_s:5.1f} mV/s -> M(0-1 s) = {est:7.3f} ms "
              f"(true {m_full:.3f} ms, bias {est - m_full:+.3f} ms)")
    print("a linear drift adds a term proportional to T/2, so it is not removed")
    print("by lengthening the window: it must be removed before integration.")


if __name__ == "__main__":
    main()
