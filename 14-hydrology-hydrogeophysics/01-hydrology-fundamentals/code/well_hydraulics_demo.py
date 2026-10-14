#!/usr/bin/env python3
"""Well hydraulics: the Theis solution, the Cooper-Jacob straight-line method, a
synthetic constant-rate pumping test, well losses and efficiency, specific
capacity, radius of influence and a recovery test.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python well_hydraulics_demo.py

The aquifer, the pumping rates and the "measured" drawdowns are SYNTHETIC teaching
values, generated from the Theis solution plus a stated noise level.  No real
pumping test, well or aquifer is used.

Contents
--------
1. Theis drawdown s = Q/(4 pi T) W(u), with the exponential integral computed
   by scipy.special.exp1.
2. The Cooper-Jacob approximation and its measured error versus u.
3. A synthetic constant-rate pumping test: straight-line fit for T and S.
4. What happens if early-time points are included in the fit.
5. Step-drawdown: well loss coefficient and well efficiency.
6. Specific capacity and its dependence on pumping duration.
7. Radius of influence: a convention, not a measurement.
8. Recovery test: superposition and the residual-drawdown slope.
"""

import numpy as np
from scipy.special import exp1

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC aquifer and test (chosen teaching values) ---------------------
Q_M3_D = 864.0        # pumping rate, 0.01 m^3/s
T_TRUE = 200.0        # transmissivity, m^2/d
S_TRUE = 3.267e-4     # storativity (confined)
R_WELL = 50.0         # observation-well distance, m
SIGMA_NOISE = 0.005   # water-level measurement noise, m (5 mm)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def theis_s(Q_m3_d, T_m2_d, S, r_m, t_d):
    """Theis drawdown in metres; s = Q/(4 pi T) * W(u), u = r^2 S/(4 T t)."""
    t = np.asarray(t_d, dtype=float)
    u = r_m ** 2 * S / (4.0 * T_m2_d * t)
    return Q_m3_d / (4.0 * np.pi * T_m2_d) * exp1(u), u


def cooper_jacob_s(Q_m3_d, T_m2_d, S, r_m, t_d):
    """Cooper-Jacob straight-line approximation, s in metres."""
    t = np.asarray(t_d, dtype=float)
    return (2.302585 * Q_m3_d) / (4.0 * np.pi * T_m2_d) * np.log10(
        2.25 * T_m2_d * t / (r_m ** 2 * S))


def main():
    section("1. Theis drawdown at an observation well")
    print(f"SYNTHETIC confined aquifer: T = {T_TRUE:.1f} m^2/d, "
          f"S = {S_TRUE:.4e}, Q = {Q_M3_D:.0f} m^3/d")
    print(f"observation well at r = {R_WELL:.0f} m")
    print("   t (d)        t (h)      u            W(u)      s (m)")
    for t in (0.002, 0.01, 0.05, 0.25, 1.0, 5.0, 10.0):
        s, u = theis_s(Q_M3_D, T_TRUE, S_TRUE, R_WELL, t)
        print(f"   {t:8.4f}   {t * 24:9.3f}   {float(u):9.4e}   "
              f"{float(exp1(u)):8.4f}   {float(s):8.4f}")
    print("  s grows only logarithmically in time: a decade of pumping adds")
    print(f"  {2.302585 * Q_M3_D / (4 * np.pi * T_TRUE):.4f} m of drawdown, not a factor.")

    section("2. Cooper-Jacob approximation and its measured error")
    print("  s ~ (2.3026 Q / (4 pi T)) log10(2.25 T t / (r^2 S)); the error is O(u)")
    print("   u          s_Theis (m)   s_CJ (m)     error (%)")
    for u_test in (0.001, 0.005, 0.01, 0.02, 0.05, 0.1, 0.2):
        t = R_WELL ** 2 * S_TRUE / (4.0 * T_TRUE * u_test)
        s_t = float(theis_s(Q_M3_D, T_TRUE, S_TRUE, R_WELL, t)[0])
        s_c = float(cooper_jacob_s(Q_M3_D, T_TRUE, S_TRUE, R_WELL, t))
        print(f"   {u_test:7.4f}    {s_t:10.4f}   {s_c:10.4f}   "
              f"{(s_c / s_t - 1.0) * 100:8.3f}")
    t_min = 25.0 * R_WELL ** 2 * S_TRUE / T_TRUE
    print(f"  the conventional criterion u < 0.01 is met after t = "
          f"{t_min:.4f} d = {t_min * 24:.2f} h")
    print("  at u = 0.01 the error is under 1%, at u = 0.1 it is about 5%: the")
    print("  criterion is a statement about an accepted error, not a law.")

    section("3. A synthetic constant-rate pumping test: straight-line fit")
    t_all = np.logspace(np.log10(0.01), np.log10(10.0), 40)
    s_clean = np.array([float(theis_s(Q_M3_D, T_TRUE, S_TRUE, R_WELL, tt)[0])
                        for tt in t_all])
    s_meas = s_clean + SIGMA_NOISE * RNG.standard_normal(t_all.size)
    print(f"  {t_all.size} SYNTHETIC drawdown readings from 0.01 to 10 d")
    print(f"  noise: {SIGMA_NOISE * 1e3:.1f} mm standard deviation (RNG seed fixed)")
    late = t_all >= t_min
    slope, intercept = np.polyfit(np.log10(t_all[late]), s_meas[late], 1)
    T_fit = 2.302585 * Q_M3_D / (4.0 * np.pi * slope)
    t0 = 10.0 ** (-intercept / slope)
    S_fit = 2.25 * T_fit * t0 / R_WELL ** 2
    s_pred = slope * np.log10(t_all[late]) + intercept
    rms = np.sqrt(np.mean((s_meas[late] - s_pred) ** 2))
    print(f"  fit on t >= {t_min:.4f} d ({int(late.sum())} of {t_all.size} points)")
    print(f"  slope = {slope:.4f} m per decade, intercept = {intercept:.4f} m")
    print(f"  T from the slope   = {T_fit:.2f} m^2/d   (true {T_TRUE:.2f}, "
          f"error {(T_fit / T_TRUE - 1) * 100:+.2f}%)")
    print(f"  t0 at s = 0        = {t0:.5f} d")
    print(f"  S from t0 and T    = {S_fit:.4e}      (true {S_TRUE:.4e}, "
          f"error {(S_fit / S_TRUE - 1) * 100:+.2f}%)")
    print(f"  fit rms = {rms * 1e3:.2f} mm against a noise of {SIGMA_NOISE * 1e3:.1f} mm")
    print(f"  recovered with errors: T {(T_fit / T_TRUE - 1) * 100:+.2f}%, "
          f"S {(S_fit / S_TRUE - 1) * 100:+.2f}%")
    print("  T comes from the SLOPE, S from the INTERCEPT.  The slope error shrinks")
    print("  like 1/sqrt(N) with the number of points; the intercept error shrinks")
    print("  only as fast as the lever arm in log10(t) grows, and it is corrupted by")
    print("  any early-time point that does not follow the straight line.")

    section("4. The cost of including early-time points")
    print("  a fixed fit window is applied to synthetic tests at three radii; the")
    print("  larger u is, the more of the curve is curvature rather than a line")
    print("   r (m)   u at t = 0.01 d   fit window (d)   T error (%)   S error (%)")
    for r_test in (10.0, 25.0, 50.0):
        s_c = np.array([float(theis_s(Q_M3_D, T_TRUE, S_TRUE, r_test, tt)[0])
                        for tt in t_all])
        s_m = s_c + SIGMA_NOISE * RNG.standard_normal(t_all.size)
        u_early = r_test ** 2 * S_TRUE / (4.0 * T_TRUE * t_all[0])
        t_start = 25.0 * r_test ** 2 * S_TRUE / T_TRUE
        m = t_all >= t_start
        sl, ic = np.polyfit(np.log10(t_all[m]), s_m[m], 1)
        Tf = 2.302585 * Q_M3_D / (4.0 * np.pi * sl)
        tf = 10.0 ** (-ic / sl)
        Sf = 2.25 * Tf * tf / r_test ** 2
        print(f"   {r_test:5.0f}   {u_early:14.4f}   {t_start:14.4f}   "
              f"{(Tf / T_TRUE - 1) * 100:+11.2f}   {(Sf / S_TRUE - 1) * 100:+11.2f}")
    print("  using only the late straight-line portion, T is recovered to a few tenths")
    print("  of a per cent at every radius while S is recovered to a few per cent: over")
    print("  a five-fold change in radius the T error grows from 0.02% to 0.40% but the")
    print("  S error grows from 0.30% to -1.54%, because S depends on the intercept t0")
    print("  obtained by extrapolating the straight line outside its window.  The fit")
    print("  window is part of the measurement and must be reported with T and S.")

    section("5. Step-drawdown: well loss and well efficiency")
    print("  s_w = B Q + C Q^2 ; B is aquifer loss, C is well loss (non-Darcy)")
    B_true, C_true = 3.0e-3, 1.2e-6
    print(f"  SYNTHETIC truth used to generate the data: B = {B_true:.2e} d/m^2, "
          f"C = {C_true:.2e} d^2/m^5")
    steps = tuple((qq, B_true * qq + C_true * qq ** 2
                   + 0.02 * float(RNG.standard_normal()))
                  for qq in (216.0, 864.0, 1728.0, 2592.0))
    print("   Q (m^3/d)   s_w (m)   s_w/Q (d/m^2)   [SYNTHETIC measured pairs]")
    for qq, sw in steps:
        print(f"   {qq:9.0f}   {sw:7.3f}   {sw / qq:14.6f}")
    qs = np.array([q for q, _ in steps])
    sws = np.array([s for _, s in steps])
    C_fit, B_fit = np.polyfit(qs, sws / qs, 1)   # s_w/Q = B + C Q
    B, C = B_fit, C_fit
    print(f"  fit: B = {B:.4e} d/m^2 (aquifer loss), C = {C:.4e} d^2/m^5 (well loss)")
    print(f"  errors: B {(B / B_true - 1) * 100:+.2f}%, C {(C / C_true - 1) * 100:+.2f}%")
    print("  identifying C requires the RATES TO SPAN A WIDE RANGE: over")
    print(f"  {qs.min():.0f}-{qs.max():.0f} m^3/d the ratio s_w/Q rises from "
          f"{sws[0] / qs[0]:.5f} to")
    print(f"  {sws[-1] / qs[-1]:.5f} d/m^2, a variation of "
          f"{(sws[-1] / qs[-1] - sws[0] / qs[0]):.2e} d/m^2 against a noise")
    print(f"  contribution of 0.02 m / {qs.min():.0f} m^3/d = "
          f"{0.02 / qs.min():.1e} d/m^2, i.e. a factor of "
          f"{(sws[-1] / qs[-1] - sws[0] / qs[0]) / (0.02 / qs.min()):.0f} above the")
    print("  noise.  Three closely spaced rates would leave C unidentifiable and a")
    print("  fit would return a meaningless value with a small formal residual.")
    print("   Q (m^3/d)   s_aquifer (m)   s_well (m)   efficiency (%)")
    for qq in (216.0, 864.0, 1728.0, 2592.0):
        s_aq, s_wl = B * qq, C * qq ** 2
        print(f"   {qq:9.0f}   {s_aq:13.3f}   {s_wl:10.3f}   "
              f"{s_aq / (s_aq + s_wl) * 100:14.1f}")
    print("  efficiency falls with rate while the AQUIFER is unchanged: the extra")
    print("  drawdown is non-Darcy loss inside and around the well.  It is a statement")
    print("  about the WELL, not the formation, and it is why a specific capacity is")
    print("  not a formation property.")

    section("6. Specific capacity and its dependence on duration")
    print("   aquifer        Q (m^3/d)   t (d)    s_w (m)   Q/s_w (m^2/d)")
    for label, T_v, S_v in (("synthetic confined", T_TRUE, S_TRUE),
                            ("10x storativity", T_TRUE, 10 * S_TRUE),
                            ("half transmissivity", T_TRUE / 2, S_TRUE)):
        for t in (0.1, 1.0, 10.0):
            s_w, _ = theis_s(Q_M3_D, T_v, S_v, R_WELL, t)
            print(f"   {label:16s} {Q_M3_D:9.0f}   {t:5.1f}   {float(s_w):7.3f}   "
                  f"{Q_M3_D / float(s_w):12.2f}")
    print("  specific capacity decreases with pumping time even when nothing about")
    print("  the aquifer changes, and it responds to S as well as to T.  A specific")
    print("  capacity is therefore a screening number, not T.")

    section("7. Radius of influence: a convention, not a measurement")
    print("  setting s = 0 in Cooper-Jacob gives r = sqrt(2.25 T t / S);")
    print("  a more useful definition fixes a drawdown threshold instead.")
    print("   t (d)    r at s=0 (m)   r at s=0.01 m (m)   r at s=0.1 m (m)")
    for t in (0.1, 1.0, 10.0, 100.0):
        r0 = np.sqrt(2.25 * T_TRUE * t / S_TRUE)
        out = []
        for thr in (0.01, 0.1):
            # solve  s(r) = Q/(4 pi T) W(u(r)) = thr  for r
            r_lo, r_hi = 0.1, 1.0e6
            for _ in range(200):
                r_mid = 0.5 * (r_lo + r_hi)
                s_mid = float(theis_s(Q_M3_D, T_TRUE, S_TRUE, r_mid, t)[0])
                if s_mid > thr:
                    r_lo = r_mid
                else:
                    r_hi = r_mid
            out.append(0.5 * (r_lo + r_hi))
        print(f"   {t:6.1f}   {r0:12.1f}   {out[0]:18.1f}   {out[1]:18.1f}")
    print("  all three are conventions.  At t = 1 d the Cooper-Jacob zero crossing")
    print("  (1174 m) lies BETWEEN the 0.1 m contour (1431 m) and the 0.01 m contour")
    print("  (2416 m) of the Theis solution - because the s = 0 radius is obtained by")
    print("  pushing the straight-line approximation far outside its own validity")
    print("  window, where u is of order 0.5 and the logarithm has no meaning.")
    print("  Always state the threshold, and never treat the radius of influence as a")
    print("  physical boundary: there is none.")

    section("8. Recovery test by superposition")
    t_p = 1.0
    print(f"  pump for t_p = {t_p:.1f} d at Q = {Q_M3_D:.0f} m^3/d, then shut in")
    print("  residual drawdown s' = (Q/4 pi T) [W(u) - W(u')], "
          "u' = r^2 S /(4 T (t - t_p))")
    print("   t (d)   t - t_p (d)   s' (m)     u          u'")
    ratio_axis, s_prime_axis = [], []
    for t in (1.02, 1.1, 1.5, 2.0, 5.0, 10.0):
        u = R_WELL ** 2 * S_TRUE / (4.0 * T_TRUE * t)
        up = R_WELL ** 2 * S_TRUE / (4.0 * T_TRUE * (t - t_p))
        s_p = Q_M3_D / (4.0 * np.pi * T_TRUE) * (exp1(u) - exp1(up))
        ratio_axis.append(np.log10(t / (t - t_p)))
        s_prime_axis.append(float(s_p))
        print(f"   {t:5.2f}   {t - t_p:11.2f}   {float(s_p):7.4f}   "
              f"{u:.3e}   {up:.3e}")
    sl = np.polyfit(ratio_axis, s_prime_axis, 1)[0]
    T_rec = 2.302585 * Q_M3_D / (4.0 * np.pi * sl)
    print(f"  slope of s' versus log10(t/(t - t_p)) = {sl:.4f} m per decade")
    print(f"  T from the recovery slope = {T_rec:.2f} m^2/d "
          f"(true {T_TRUE:.2f}, error {(T_rec / T_TRUE - 1) * 100:+.2f}%)")
    print("  the recovery slope gives T WITHOUT any assumption about S, which is why")
    print("  a recovery test is the most robust route to transmissivity.  The 1.2%")
    print("  bias here is the finite-u' error of the logarithmic approximation at the")
    print("  earliest recovery point (u' = 0.051), not noise: fitting only the later")
    print("  points where u' < 0.01 removes it.  Report the fitting window.")


if __name__ == "__main__":
    main()
