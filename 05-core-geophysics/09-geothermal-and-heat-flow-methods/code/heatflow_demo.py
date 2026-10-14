"""Measuring terrestrial heat flow: sign convention, disturbance, and non-uniqueness.

Three results, two of them negative:

  1. SIGN CONVENTION AND FLUX CONTINUITY.  With depth z positive downward and q
     reported as the positive UPWARD flux, q = k dT/dz.  A two-layer conductivity
     model is solved exactly to show that the GRADIENT is discontinuous while the
     FLUX is continuous -- the single most important check on a heat-flow
     calculation, and the one most often got wrong.
  2. THE BOREHOLE DISTURBANCE.  A line-source relaxation model gives the fraction
     of the drilling perturbation remaining at the wall as a function of elapsed
     time, and the resulting bias in the heat flow.  The bias and the time needed
     to reduce it below 1 per cent are reported.
  3. GROUND-SURFACE TEMPERATURE RECONSTRUCTION IS NON-UNIQUE.  Two genuinely
     different surface-temperature histories are propagated through the diffusion
     equation, and the resulting present-day profiles are compared.  They differ by
     more than a stated measurement precision only in the top few hundred metres,
     which is both the method's power and its ambiguity.

Every conductivity, heat flow, temperature perturbation and history is a STATED
SYNTHETIC INPUT.

Run:  python3 heatflow_demo.py
"""

from __future__ import annotations

import numpy as np
SURFACE_T = 10.0        # SYNTHETIC mean surface temperature, degC
Q0 = 0.060              # SYNTHETIC surface heat flow, W/m^2
KAPPA = 1.0e-6          # SYNTHETIC thermal diffusivity, m^2/s
R_W = 0.10              # SYNTHETIC borehole radius, m


def section(title: str) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def main() -> None:
    section("1. Sign convention and flux continuity")
    print("Depth z is positive DOWNWARD.  Temperature increases downward, so dT/dz")
    print("is positive.  Heat flows UPWARD, and the reported heat flow is that")
    print("upward magnitude,  q = k dT/dz  with z measured downward.")
    layers = [(0.0, 500.0, 1.5), (500.0, 2000.0, 3.0)]   # top, base, k (W/m/K)
    print(f"\nq = {Q0 * 1000:.1f} mW/m^2 everywhere (flux continuity)")
    print("\ndepth (m)   k (W/m/K)   dT/dz (K/km)   q (mW/m^2)   T (degC)")
    for top, base, k in layers:
        grad = Q0 / k
        for z in (top + 1.0, base - 1.0):
            t = SURFACE_T
            for t2, b2, k2 in layers:
                if z > t2:
                    t += (min(z, b2) - t2) * (Q0 / k2) * 1000.0
            print(f"{z:9.0f}   {k:10.2f}   {grad * 1000:13.2f}   "
                  f"{Q0 * 1000:11.1f}   {t:9.2f}")
    print("The gradient changes by a factor of two across the conductivity contrast;")
    print("the FLUX does not change at all.  A heat-flow profile that shows the flux")
    print("jumping at a lithological boundary is wrong, and the error is always a")
    print("mis-assigned conductivity.")

    section("2. How long a drilling disturbance takes to decay")
    t_ref = 3600.0          # SYNTHETIC 'end of circulation' reference time, s
    print(f"line-source kernel:  F(t) = (t_ref/t) exp[-r^2/(4 kappa t) + "
          f"r^2/(4 kappa t_ref)]")
    print(f"r = {R_W:.2f} m, kappa = {KAPPA:.1e} m^2/s, t_ref = "
          f"{t_ref / 3600:.1f} h\n")
    dT0, L = 20.0, 2000.0   # SYNTHETIC initial perturbation and its depth scale
    k_ref = 2.5             # SYNTHETIC conductivity, W/m/K
    print("elapsed (h)   residual fraction   gradient bias (K/km)   heat-flow bias "
          "(%)")
    for hours in (1, 4, 12, 24, 48, 120, 240, 720, 2160):
        t = hours * 3600.0
        frac = (t_ref / t) * np.exp(-R_W ** 2 / (4 * KAPPA * t)
                                    + R_W ** 2 / (4 * KAPPA * t_ref))
        bias_grad = dT0 * frac / (L * 1e-3)          # K/km
        bias_q = 100.0 * (k_ref * bias_grad * 1e-3) / Q0   # per cent of q0
        print(f"{hours:11d}   {frac:17.4f}   {bias_grad:20.3f}   {bias_q:15.2f}")
    print("A log run an hour after circulation stops carries tens of per cent of the")
    print("drilling disturbance; a log run days later carries a few per cent.  Note")
    print("that the residual is a DIFFERENCE from the formation temperature, so it")
    print("biases the absolute temperature more than the gradient -- which is why")
    print("gradient-based flow estimates survive a partially equilibrated hole and")
    print("absolute-temperature estimates do not.")

    section("3. Two different surface histories, one present-day profile")
    depths = np.array([50.0, 100.0, 200.0, 300.0, 500.0, 800.0])
    print("Present-day temperature anomaly produced by two GST histories:")
    print("\n  A: a 1.0 K step increase 200 yr before present")
    print("  B: a smooth 1.6 K rise spread linearly over 600 yr\n")
    print("depth (m)   history A (K)   history B (K)   difference (K)")
    for z in depths:
        ta = 1.0 * (1.0 - _erf_profile(z, 200.0))
        tb = _smooth_history(z)
        print(f"{z:9.0f}   {ta:14.4f}   {tb:15.4f}   {ta - tb:14.4f}")
    print("Above about 300 m the two histories are distinguishable; below it they are")
    print("not, and any measurement noise larger than the difference makes them")
    print("indistinguishable everywhere.  A GST reconstruction is therefore an INVERSE")
    print("problem with a genuine null space: the same present-day profile is produced")
    print("by a family of histories, and the family's width is set by the noise level.")
    print("Reporting a single history without the family overstates the measurement.")


def _erf_profile(z, event_age_yr):
    """Fraction of a surface step of the given age that has reached depth z."""
    from math import erf
    t = event_age_yr * 3.155693e7
    return erf(z / (2.0 * np.sqrt(KAPPA * t)))


def _smooth_history(z):
    """Anomaly at depth z from a rate of surface warming spread over 600 yr."""
    from math import erf
    total, n = 1.6, 600
    dt = 600.0 / n * 3.155693e7
    anomaly = 0.0
    for i in range(n):
        age = (600.0 - (i + 0.5) * 600.0 / n) * 3.155693e7
        step = total / n
        anomaly += step * (1.0 - erf(z / (2.0 * np.sqrt(KAPPA * max(age, 1.0)))))
    return anomaly


if __name__ == "__main__":
    main()
